#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import requests

from needle.updates.cellar_feed import parse_feed


ENDPOINT="https://publications.europa.eu/webapi/notification/ingestion"
TARGETS=[
    {
        "celex":"32025R0905",
        "start":"2025-06-12T00:00:00+02:00",
        "end":"2025-06-20T23:59:59+02:00",
    },
    {
        "celex":"32023R2055",
        "start":"2023-09-25T00:00:00+02:00",
        "end":"2023-10-05T23:59:59+02:00",
    },
]
ACTIONS=("CREATE","UPDATE")
WEMI=("work","expression","manifestation")
MAX_PAGES=20


def fetch(params):
    response=requests.get(
        ENDPOINT,
        params=params,
        headers={
            "Accept":"application/rss+xml",
            "User-Agent":(
                "Morrow-Needle-Operational-Replay-Discovery/0.1 "
                "(+https://github.com/kaastumor/morrow-needle)"
            ),
        },
        timeout=120,
        allow_redirects=True,
    )
    response.raise_for_status()
    return response.content,response


def find_target(target):
    wanted=f"celex:{target['celex']}".lower()
    attempts=[]
    matches=[]
    for action in ACTIONS:
        for wemi in WEMI:
            for page_number in range(1,MAX_PAGES+1):
                params={
                    "startDate":target["start"],
                    "endDate":target["end"],
                    "type":action,
                    "wemiClasses":wemi,
                    "page":str(page_number),
                }
                payload,response=fetch(params)
                page=parse_feed(payload)
                attempts.append({
                    "query":params,
                    "request_url":response.url,
                    "payload_sha256":hashlib.sha256(payload).hexdigest(),
                    "event_count":len(page.events),
                    "more_entries":page.more_entries,
                })
                for event in page.events:
                    identifiers={
                        value.lower() for value in event.get("identifiers",[])
                    }
                    if wanted in identifiers:
                        matches.append(event)
                if not page.more_entries:
                    break
    # The same underlying update may appear at several WEMI levels. Prefer
    # WORK, then CREATE, then earliest ingestion time.
    matches.sort(key=lambda event:(
        "WORK" not in event.get("wemi_levels",[]),
        event["action"] != "CREATE",
        event["ingestion_time"],
        event["event_key"],
    ))
    return matches,attempts


def main() -> int:
    results={}
    for target in TARGETS:
        matches,attempts=find_target(target)
        if not matches:
            raise AssertionError(
                f"no official feed event found for CELEX:{target['celex']}"
            )
        results[target["celex"]]={
            "selected_event":matches[0],
            "match_count":len(matches),
            "matches":matches,
            "attempts":attempts,
        }

    out=Path("artifacts/operational-replay-discovery")
    out.mkdir(parents=True,exist_ok=True)
    path=out/"events.json"
    path.write_text(
        json.dumps(
            {
                "probe_version":"0.1",
                "targets":results,
            },
            indent=2,
            ensure_ascii=False,
        )+"\n",
        encoding="utf-8",
    )
    print(json.dumps({
        celex:{
            "action":result["selected_event"]["action"],
            "wemi_levels":result["selected_event"]["wemi_levels"],
            "ingestion_time":result["selected_event"]["ingestion_time"],
            "event_key":result["selected_event"]["event_key"],
            "match_count":result["match_count"],
        }
        for celex,result in results.items()
    },indent=2))
    return 0


if __name__=="__main__":
    raise SystemExit(main())
