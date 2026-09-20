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
from needle.updates.relevance import classify_event_relevance
from needle.updates.reobserve import celex_from_event


ENDPOINT="https://publications.europa.eu/webapi/notification/ingestion"
CELLAR_CELEX="https://publications.europa.eu/resource/celex/{celex}"
WEMI=("work","expression","manifestation")
MAX_PAGES=25
LOOKBACK_DAYS=7
MAX_CANDIDATES=20
AMEND_PATTERNS=(
    re.compile(r"\bis amended as follows\b",re.I),
    re.compile(r"\bamending Regulation\b",re.I),
    re.compile(r"\bamending Directive\b",re.I),
    re.compile(r"\bis replaced by the following\b",re.I),
    re.compile(r"\bthe following .*? is inserted\b",re.I),
)


def iso(value):
    return value.astimezone(timezone.utc).replace(
        microsecond=0
    ).isoformat()


def normalized_visible_text(xml_bytes):
    root=ET.fromstring(xml_bytes)
    return " ".join("".join(root.itertext()).split())


def fetch_feed(start,end,wemi,page):
    response=requests.get(
        ENDPOINT,
        params={
            "startDate":iso(start),
            "endDate":iso(end),
            "type":"CREATE",
            "wemiClasses":wemi,
            "page":str(page),
        },
        headers={
            "Accept":"application/rss+xml",
            "User-Agent":"Morrow-Needle-Recent-Create-Discovery/0.1",
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
                "User-Agent":"Morrow-Needle-Recent-Create-Discovery/0.1",
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
                        if not name.lower().endswith((".xml",".frg",".xhtml",".html")):
                            continue
                        try:
                            texts.append(normalized_visible_text(zf.read(name)))
                        except ET.ParseError:
                            continue
            except zipfile.BadZipFile:
                continue
        else:
            # Discovery only: strip tags sufficiently to find drafting phrases.
            raw=response.content.decode("utf-8",errors="replace")
            texts.append(" ".join(re.sub(r"<[^>]+>"," ",raw).split()))
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


def snippets(text):
    hits=[]
    for pattern in AMEND_PATTERNS:
        for match in pattern.finditer(text):
            start=max(0,match.start()-220)
            end=min(len(text),match.end()+500)
            value=text[start:end]
            hits.append({
                "pattern":pattern.pattern,
                "start":start,
                "end":end,
                "snippet":value,
                "snippet_hash":hashlib.sha256(
                    value.encode("utf-8")
                ).hexdigest(),
            })
            if len(hits) >= 4:
                return hits
    return hits


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
        for wemi in WEMI:
            for page_number in range(1,MAX_PAGES+1):
                payload,response=fetch_feed(
                    start,end,wemi,page_number
                )
                page=parse_feed(payload)
                feed_attempts.append({
                    "start":iso(start),
                    "end":iso(end),
                    "wemi":wemi,
                    "page":page_number,
                    "payload_sha256":hashlib.sha256(payload).hexdigest(),
                    "event_count":len(page.events),
                    "more_entries":page.more_entries,
                })
                for event in page.events:
                    if (
                        classify_event_relevance(event)
                        != "LEGAL_RESOURCE_CANDIDATE"
                    ):
                        continue
                    celex=celex_from_event(event)
                    if not celex:
                        continue
                    current=roots.get(event["root_cellar_id"])
                    candidate={
                        "event":event,
                        "celex":celex,
                    }
                    if current is None:
                        roots[event["root_cellar_id"]]=candidate
                    elif (
                        "WORK" in event["wemi_levels"]
                        and "WORK" not in current["event"]["wemi_levels"]
                    ):
                        roots[event["root_cellar_id"]]=candidate
                if not page.more_entries:
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
        hits=snippets(text) if text else []
        candidates.append({
            "event":item["event"],
            "celex":item["celex"],
            "source_observation":observation,
            "amendment_language_hits":hits,
            "looks_like_amending_act":bool(hits),
        })

    result={
        "probe_version":"0.1",
        "character":"RECENT_CREATE_OPERATIONAL_DISCOVERY",
        "sampled_at":now.isoformat(),
        "lookback_days":LOOKBACK_DAYS,
        "feed_attempts":feed_attempts,
        "candidate_count":len(candidates),
        "amending_candidate_count":sum(
            item["looks_like_amending_act"] for item in candidates
        ),
        "candidates":candidates,
        "guardrail":(
            "Drafting-language matches are discovery hints only. They do not "
            "establish a legal mutation until target, comparator and authentic "
            "instruction evidence are reconciled."
        ),
    }
    out=Path("artifacts/recent-create-discovery")
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
            "wemi_levels":item["event"]["wemi_levels"],
            "looks_like_amending_act":item["looks_like_amending_act"],
            "hit_count":len(item["amendment_language_hits"]),
        }
        for item in candidates
    ],indent=2))
    return 0


if __name__=="__main__":
    raise SystemExit(main())
