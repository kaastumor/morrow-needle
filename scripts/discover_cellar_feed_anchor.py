#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import requests

from needle.updates.cellar_feed import parse_feed


ENDPOINT = "https://publications.europa.eu/webapi/notification/ingestion"
WINDOWS = [
    {
        "startDate":"2026-09-19T00:00:00+02:00",
        "endDate":"2026-09-20T23:59:59+02:00",
        "type":"UPDATE",
        "wemiClasses":"work",
        "page":"1",
    },
    {
        "startDate":"2026-09-18T00:00:00+02:00",
        "endDate":"2026-09-18T23:59:59+02:00",
        "type":"UPDATE",
        "wemiClasses":"work",
        "page":"1",
    },
    {
        "startDate":"2026-09-15T00:00:00+02:00",
        "endDate":"2026-09-17T23:59:59+02:00",
        "type":"UPDATE",
        "wemiClasses":"work",
        "page":"1",
    },
]


def fetch(params):
    response=requests.get(
        ENDPOINT,
        params=params,
        headers={
            "Accept":"application/rss+xml",
            "User-Agent":(
                "Morrow-Needle-Cellar-Feed-Anchor-Discovery/0.1 "
                "(+https://github.com/kaastumor/morrow-needle)"
            ),
        },
        timeout=120,
        allow_redirects=True,
    )
    response.raise_for_status()
    return response


def main() -> int:
    out_dir=Path("artifacts/cellar-feed-discovery")
    out_dir.mkdir(parents=True,exist_ok=True)
    attempts=[]

    for index,params in enumerate(WINDOWS, start=1):
        response=fetch(params)
        payload=response.content
        raw_path=out_dir/f"attempt-{index}.xml"
        raw_path.write_bytes(payload)
        try:
            page=parse_feed(payload)
        except Exception as exc:
            attempts.append({
                "query":params,
                "request_url":response.url,
                "status_code":response.status_code,
                "payload_sha256":hashlib.sha256(payload).hexdigest(),
                "parse_error":f"{type(exc).__name__}: {exc}",
            })
            continue
        events=list(page.events)
        attempt={
            "query":params,
            "request_url":response.url,
            "status_code":response.status_code,
            "payload_sha256":hashlib.sha256(payload).hexdigest(),
            "page":{
                "window_start":page.window_start,
                "window_end":page.window_end,
                "page":page.page,
                "more_entries":page.more_entries,
                "event_count":len(events),
            },
            "events":events[:25],
        }
        attempts.append(attempt)
        if events:
            event=events[0]
            result={
                "probe_version":"0.1",
                "selected_event":event,
                "selected_from_query":params,
                "attempts":attempts,
            }
            (out_dir/"anchor.json").write_text(
                json.dumps(result,indent=2,ensure_ascii=False),
                encoding="utf-8",
            )
            print(json.dumps(result,indent=2,ensure_ascii=False))
            return 0

    result={"probe_version":"0.1","selected_event":None,"attempts":attempts}
    (out_dir/"anchor.json").write_text(
        json.dumps(result,indent=2,ensure_ascii=False),
        encoding="utf-8",
    )
    print(json.dumps(result,indent=2,ensure_ascii=False))
    return 1


if __name__=="__main__":
    raise SystemExit(main())
