#!/usr/bin/env python3
from __future__ import annotations

from datetime import date, datetime, timedelta, timezone
import hashlib
import io
import json
from pathlib import Path
import re
import zipfile
import xml.etree.ElementTree as ET

import requests

from needle.updates.cellar_feed import parse_feed


FEED="https://publications.europa.eu/webapi/notification/ingestion"
CELLAR="https://publications.europa.eu/resource/celex/{celex}"
CAUSE="32026R2104"
TARGET_BASE="02021R0404"
EVENT_START="2026-09-18T10:32:18+02:00"
EVENT_END="2026-09-18T10:32:23+02:00"
SCAN_START=date(2026,9,1)
SCAN_END=date(2026,9,20)
USER_AGENT=(
    "Morrow-Needle-2104-Live-Case/0.1 "
    "(+https://github.com/kaastumor/morrow-needle)"
)


def sha(payload: bytes) -> str:
    return "sha256:"+hashlib.sha256(payload).hexdigest()


def local(tag: str) -> str:
    return tag.rsplit("}",1)[-1]


def visible_xml(payload: bytes) -> str:
    root=ET.fromstring(payload)
    return " ".join("".join(root.itertext()).split())


def zip_text(payload: bytes) -> tuple[str,list[dict]]:
    chunks=[]
    entries=[]
    with zipfile.ZipFile(io.BytesIO(payload)) as zf:
        for name in sorted(zf.namelist()):
            if not name.lower().endswith((".xml",".frg",".xhtml",".html")):
                continue
            raw=zf.read(name)
            try:
                text=visible_xml(raw)
            except ET.ParseError:
                continue
            if not text:
                continue
            start=sum(len(chunk)+1 for chunk in chunks)
            chunks.append(text)
            entries.append({
                "name":name,
                "text_length":len(text),
                "joined_start":start,
                "joined_end":start+len(text),
            })
    return " ".join(chunks),entries


def fetch_celex(celex: str) -> dict:
    url=CELLAR.format(celex=celex)
    response=requests.get(
        url,
        headers={
            "Accept":"application/zip;mtype=fmx4",
            "Accept-Language":"eng",
            "User-Agent":USER_AGENT,
        },
        timeout=120,
        allow_redirects=True,
    )
    result={
        "celex":celex,
        "status":response.status_code,
        "final_url":response.url,
        "content_type":response.headers.get("Content-Type"),
        "bytes":len(response.content),
    }
    if response.status_code == 200 and response.content.startswith(b"PK"):
        result["artifact_hash"]=sha(response.content)
        text,entries=zip_text(response.content)
        result["text"]=text
        result["entries"]=entries
    return result


def find_span(text: str, pattern: str) -> dict | None:
    match=re.search(pattern,text,flags=re.I|re.S)
    if not match:
        return None
    value=match.group(0)
    return {
        "start":match.start(),
        "end":match.end(),
        "text":value,
        "text_hash":"sha256:"+hashlib.sha256(
            value.encode("utf-8")
        ).hexdigest(),
    }


def find_event() -> tuple[dict,list[dict]]:
    attempts=[]
    matches=[]
    for page_number in range(1,6):
        params={
            "startDate":EVENT_START,
            "endDate":EVENT_END,
            "type":"UPDATE",
            "wemiClasses":"work",
            "page":str(page_number),
        }
        response=requests.get(
            FEED,
            params=params,
            headers={
                "Accept":"application/rss+xml",
                "User-Agent":USER_AGENT,
            },
            timeout=120,
            allow_redirects=True,
        )
        response.raise_for_status()
        page=parse_feed(response.content)
        attempts.append({
            "query":params,
            "request_url":response.url,
            "payload_hash":sha(response.content),
            "event_count":len(page.events),
            "more_entries":page.more_entries,
        })
        for event in page.events:
            if any(
                value.lower()==f"celex:{CAUSE}".lower()
                for value in event.get("identifiers",[])
            ):
                matches.append(event)
        if not page.more_entries:
            break
    if len(matches) != 1:
        raise AssertionError(
            f"expected one live WORK/UPDATE event for CELEX:{CAUSE}, "
            f"got {len(matches)}"
        )
    return matches[0],attempts


def scan_checkpoints() -> list[dict]:
    current=SCAN_START
    found=[]
    while current <= SCAN_END:
        celex=f"{TARGET_BASE}-{current:%Y%m%d}"
        result=fetch_celex(celex)
        if result["status"] == 200 and result.get("text"):
            text=result.pop("text")
            result["markers"]={
                marker:(marker in text)
                for marker in (
                    "US-2.1404","US-2.1405","US-2.1406"
                )
            }
            found.append(result)
        current += timedelta(days=1)
    return found


def main() -> int:
    event,event_attempts=find_event()
    cause=fetch_celex(CAUSE)
    if cause["status"] != 200 or not cause.get("text"):
        raise AssertionError("authentic 2026/2104 FMX4 unavailable")
    cause_text=cause.pop("text")

    spans={
        "annexes_amended":find_span(
            cause_text,
            r"Annexes\s+V\s+and\s+XIV\s+to\s+Implementing "
            r"Regulation\s*\(EU\)\s*2021/404\s+are\s+amended\s+"
            r"as\s+follows"
        ),
        "annex_v_rows_added":find_span(
            cause_text,
            r"in\s+Part\s+1,\s*Section\s+B,\s*in\s+the\s+entry\s+"
            r"for\s+the\s+United\s+States,\s*the\s+following\s+rows\s+"
            r"for\s+the\s+zones\s+US-2\.1405\s+and\s+US-2\.1406\s+"
            r"are\s+added\s+after\s+the\s+row\s+for\s+the\s+zone\s+"
            r"US-2\.1404"
        ),
        "zone_1405_row":find_span(
            cause_text,
            r"US\s+United\s+States\s+US-2\.1405\s+BPP,\s*BPR,\s*DOC,"
            r"\s*DOR,\s*SP,\s*SR,\s*POU-LT20,\s*HEP,\s*HER,\s*"
            r"HE-LT20\s+N,\s*P1\s+27\.8\.2026"
        ),
        "entry_into_force":find_span(
            cause_text,
            r"This\s+Regulation\s+shall\s+enter\s+into\s+force\s+"
            r"on\s+the\s+day\s+following\s+that\s+of\s+its\s+"
            r"publication\s+in\s+the\s+Official\s+Journal\s+of\s+"
            r"the\s+European\s+Union"
        ),
    }
    missing=[name for name,value in spans.items() if value is None]
    if missing:
        raise AssertionError(
            "missing expected authentic source spans: "+", ".join(missing)
        )

    checkpoints=scan_checkpoints()
    before=[
        item for item in checkpoints
        if item["markers"]["US-2.1404"]
        and not item["markers"]["US-2.1405"]
        and not item["markers"]["US-2.1406"]
    ]
    after=[
        item for item in checkpoints
        if item["markers"]["US-2.1405"]
        and item["markers"]["US-2.1406"]
    ]

    verification_route=(
        "AUTHENTIC_CAUSE_PLUS_BEFORE_AFTER_CHECKPOINTS"
        if before and after
        else "AUTHENTIC_CAUSE_WITHOUT_COMPLETE_CHECKPOINT_PAIR"
    )
    result={
        "probe_version":"0.1",
        "character":"LIVE_EVENT_DRIVEN_MUTATION_DISCOVERY",
        "observed_at":datetime.now(timezone.utc).isoformat(),
        "trigger_event":event,
        "feed_attempts":event_attempts,
        "authentic_cause":{
            **cause,
            "source_spans":spans,
        },
        "target":{
            "base_celex":"32021R0404",
            "consolidated_celex_prefix":TARGET_BASE,
            "scan_start":SCAN_START.isoformat(),
            "scan_end":SCAN_END.isoformat(),
            "checkpoint_count":len(checkpoints),
            "checkpoints":checkpoints,
        },
        "candidate":{
            "operation":"INSERT",
            "target_locator":(
                "Annex V > Part 1 > Section B > United States > "
                "zone US-2.1405"
            ),
            "instruction_character":"AUTHENTIC_EXPLICIT_INSERTION",
            "verification_route":verification_route,
            "before_checkpoint_count":len(before),
            "after_checkpoint_count":len(after),
            "verification_state":(
                "VERIFIABLE_WITH_EXISTING_V0_2_RULES"
                if before and after
                else "DO_NOT_PROMOTE_WITHOUT_MORE_OFFICIAL_EVIDENCE"
            ),
        },
        "guardrails":[
            "The Cellar UPDATE is only the operational trigger.",
            "The authentic amending act is the canonical legal cause.",
            "No consolidated checkpoint is invented when Cellar does not expose one.",
            "The candidate is not emitted as a VERIFIED mutation unless the v0.2 evidence contract is satisfied.",
        ],
    }
    out=Path("artifacts/reg2104-live-case")
    out.mkdir(parents=True,exist_ok=True)
    (out/"evidence.json").write_text(
        json.dumps(result,indent=2,ensure_ascii=False)+"\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "event_key":event["event_key"],
        "root_cellar_id":event["root_cellar_id"],
        "cause_hash":cause["artifact_hash"],
        "checkpoint_count":len(checkpoints),
        "before_count":len(before),
        "after_count":len(after),
        "candidate":result["candidate"],
        "checkpoints":[
            {
                "celex":item["celex"],
                "artifact_hash":item["artifact_hash"],
                "markers":item["markers"],
            }
            for item in checkpoints
        ],
    },indent=2,ensure_ascii=False))
    return 0


if __name__=="__main__":
    raise SystemExit(main())
