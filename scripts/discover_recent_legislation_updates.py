#!/usr/bin/env python3
from __future__ import annotations

from datetime import datetime, timedelta, timezone
import hashlib
import io
import json
from pathlib import Path
import re
import zipfile
import xml.etree.ElementTree as ET

import requests

from needle.updates.cellar_feed import parse_feed
from needle.updates.reobserve import celex_from_event


ENDPOINT="https://publications.europa.eu/webapi/notification/ingestion"
CELLAR_CELEX="https://publications.europa.eu/resource/celex/{celex}"
LOOKBACK_DAYS=7
MAX_PAGES=12
MAX_CANDIDATES=30
CURRENT_LEGISLATION_PREFIX="32026"

TITLE_AMEND_RE=re.compile(
    r"\bamending\s+(?:Regulation|Directive|Decision)\b",
    re.I,
)
OPERATIVE_AMEND_RE=re.compile(
    r"\b(?:Regulation|Directive|Decision)\b.{0,240}?"
    r"\bis amended as follows\b",
    re.I | re.S,
)


def iso(value):
    return value.astimezone(timezone.utc).replace(
        microsecond=0
    ).isoformat()


def normalized_visible_text(xml_bytes):
    root=ET.fromstring(xml_bytes)
    return " ".join("".join(root.itertext()).split())


def fetch_feed(start,end,page):
    response=requests.get(
        ENDPOINT,
        params={
            "startDate":iso(start),
            "endDate":iso(end),
            "type":"UPDATE",
            "wemiClasses":"work",
            "page":str(page),
        },
        headers={
            "Accept":"application/rss+xml",
            "User-Agent":"Morrow-Needle-Recent-Legislation-Update/0.1",
        },
        timeout=120,
        allow_redirects=True,
    )
    response.raise_for_status()
    return response.content,response


def fetch_text(celex):
    url=CELLAR_CELEX.format(celex=celex)
    attempts=[]
    for accept in (
        "application/zip;mtype=fmx4",
        "application/zip;mtype=xhtml",
        "application/zip;mtype=html",
        "text/html",
    ):
        response=requests.get(
            url,
            headers={
                "Accept":accept,
                "Accept-Language":"eng",
                "User-Agent":"Morrow-Needle-Recent-Legislation-Update/0.1",
            },
            timeout=120,
            allow_redirects=True,
        )
        attempts.append({
            "accept":accept,
            "status":response.status_code,
            "final_url":response.url,
            "content_type":response.headers.get("Content-Type"),
            "bytes":len(response.content),
        })
        if response.status_code != 200 or not response.content:
            continue
        texts=[]
        if accept.startswith("application/zip"):
            try:
                with zipfile.ZipFile(io.BytesIO(response.content)) as zf:
                    for name in sorted(zf.namelist()):
                        if not name.lower().endswith(
                            (".xml",".frg",".xhtml",".html")
                        ):
                            continue
                        try:
                            texts.append(
                                normalized_visible_text(zf.read(name))
                            )
                        except ET.ParseError:
                            continue
            except zipfile.BadZipFile:
                continue
        else:
            raw=response.content.decode("utf-8",errors="replace")
            texts.append(
                " ".join(re.sub(r"<[^>]+>"," ",raw).split())
            )
        text=" ".join(texts)
        if text:
            return text,{
                "accept":accept,
                "artifact_hash":"sha256:"+hashlib.sha256(
                    response.content
                ).hexdigest(),
                "final_url":response.url,
                "attempts":attempts,
            }
    return None,{"attempts":attempts}


def signal(text):
    if not text:
        return {
            "title_amending":False,
            "operative_amendment":False,
            "title_snippet":None,
            "operative_snippet":None,
        }

    title_zone=text[:5000]
    title_match=TITLE_AMEND_RE.search(title_zone)
    operative_match=OPERATIVE_AMEND_RE.search(text)

    def snippet(match,source,before=240,after=520):
        if match is None:
            return None
        return source[
            max(0,match.start()-before):
            min(len(source),match.end()+after)
        ]

    return {
        "title_amending":title_match is not None,
        "operative_amendment":operative_match is not None,
        "title_snippet":snippet(title_match,title_zone),
        "operative_snippet":snippet(operative_match,text),
    }


def main():
    now=datetime.now(timezone.utc)
    roots={}
    feed_attempts=[]

    for days_back in range(LOOKBACK_DAYS):
        end=(now-timedelta(days=days_back)).replace(
            hour=23,minute=59,second=59,microsecond=0
        )
        if days_back == 0:
            end=now.replace(microsecond=0)
        start=end.replace(hour=0,minute=0,second=0)

        for page_number in range(1,MAX_PAGES+1):
            payload,response=fetch_feed(start,end,page_number)
            page=parse_feed(payload)
            feed_attempts.append({
                "start":iso(start),
                "end":iso(end),
                "page":page_number,
                "payload_sha256":hashlib.sha256(payload).hexdigest(),
                "event_count":len(page.events),
                "more_entries":page.more_entries,
            })
            for event in page.events:
                celex=celex_from_event(event)
                if not celex:
                    continue
                if not celex.startswith(CURRENT_LEGISLATION_PREFIX):
                    continue
                roots.setdefault(
                    event["root_cellar_id"],
                    {"event":event,"celex":celex},
                )
            if len(roots) >= MAX_CANDIDATES:
                break
            if not page.more_entries:
                break
        else:
            raise AssertionError(
                f"UPDATE/work pagination exceeded {MAX_PAGES} pages "
                f"for {iso(start)}"
            )
        if len(roots) >= MAX_CANDIDATES:
            break

    ordered=sorted(
        roots.values(),
        key=lambda item:(
            item["event"]["ingestion_time"],
            item["celex"],
        ),
        reverse=True,
    )[:MAX_CANDIDATES]

    candidates=[]
    for item in ordered:
        text,observation=fetch_text(item["celex"])
        signals=signal(text)
        candidates.append({
            "event":item["event"],
            "celex":item["celex"],
            "source_observation":observation,
            "signals":signals,
            "amendment_candidate":(
                signals["title_amending"]
                or signals["operative_amendment"]
            ),
        })

    result={
        "probe_version":"0.1",
        "character":"RECENT_LEGISLATION_UPDATE_DISCOVERY",
        "sampled_at":now.isoformat(),
        "lookback_days":LOOKBACK_DAYS,
        "candidate_selection":(
            "Cellar UPDATE at WORK level with CELEX prefix 32026. "
            "This is a discovery heuristic only; UPDATE is not interpreted "
            "as legal change or as proof the act is newly published."
        ),
        "candidate_count":len(candidates),
        "amendment_candidate_count":sum(
            item["amendment_candidate"] for item in candidates
        ),
        "feed_attempts":feed_attempts,
        "candidates":candidates,
        "guardrail":(
            "Title and operative-clause matches nominate an act for canonical "
            "amendment analysis only. Mutation truth still requires authentic "
            "instruction parsing and target/comparator reconciliation."
        ),
    }

    out=Path("artifacts/recent-legislation-update-discovery")
    out.mkdir(parents=True,exist_ok=True)
    (out/"candidates.json").write_text(
        json.dumps(result,indent=2,ensure_ascii=False)+"\n",
        encoding="utf-8",
    )
    print(json.dumps([
        {
            "celex":item["celex"],
            "event_key":item["event"]["event_key"],
            "ingestion_time":item["event"]["ingestion_time"],
            "priority":item["event"]["priority"],
            "title_amending":item["signals"]["title_amending"],
            "operative_amendment":item["signals"][
                "operative_amendment"
            ],
        }
        for item in candidates
    ],indent=2))
    return 0


if __name__=="__main__":
    raise SystemExit(main())
