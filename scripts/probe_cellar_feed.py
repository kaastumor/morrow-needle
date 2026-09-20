#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import requests
from jsonschema import Draft202012Validator

from needle.updates.cellar_feed import parse_feed


ENDPOINT = "https://publications.europa.eu/webapi/notification/ingestion"
TARGET_NOTIFICATION_ID = "7081775"
WINDOW = {
    "startDate":"2012-06-11T09:13:00+01:00",
    "endDate":"2012-06-11T09:14:59+01:00",
    "type":"UPDATE",
    "wemiClasses":"work",
    "page":"1",
}


def fetch_feed(accept: str) -> tuple[bytes, requests.Response]:
    response = requests.get(
        ENDPOINT,
        params=WINDOW,
        headers={
            "Accept":accept,
            "User-Agent":(
                "Morrow-Needle-Cellar-Feed-Probe/0.1 "
                "(+https://github.com/kaastumor/morrow-needle)"
            ),
        },
        timeout=120,
        allow_redirects=True,
    )
    response.raise_for_status()
    return response.content, response


def target(page):
    matches = [
        event
        for event in page.events
        if event["notification_id"] == TARGET_NOTIFICATION_ID
    ]
    if len(matches) != 1:
        raise AssertionError(
            f"expected one notification {TARGET_NOTIFICATION_ID}, "
            f"got {len(matches)}"
        )
    return matches[0]


def comparable(event: dict) -> dict:
    return {
        "notification_id":event["notification_id"],
        "action":event["action"],
        "cellar_id":event["cellar_id"],
        "root_cellar_id":event["root_cellar_id"],
        "ingestion_time":event["ingestion_time"],
        "priority":event["priority"],
        "classes":event["classes"],
        "wemi_levels":event["wemi_levels"],
        "identifiers":event["identifiers"],
    }


def main() -> int:
    schema = json.loads(
        Path("schemas/cellar-ingestion-event-v0.1.schema.json").read_text(
            encoding="utf-8"
        )
    )
    validator = Draft202012Validator(schema)

    out_dir = Path("artifacts/cellar-feed")
    out_dir.mkdir(parents=True, exist_ok=True)

    outputs = {}
    for name, accept in {
        "rss":"application/rss+xml",
        "atom":"application/atom+xml",
    }.items():
        payload, response = fetch_feed(accept)
        raw_path = out_dir / f"live-{name}.xml"
        raw_path.write_bytes(payload)

        page = parse_feed(payload)
        parsed_events = list(page.events)
        event_ids = [event["notification_id"] for event in parsed_events]

        debug = {
            "accept":accept,
            "request_url":response.url,
            "status_code":response.status_code,
            "content_type":response.headers.get("Content-Type"),
            "payload_sha256":hashlib.sha256(payload).hexdigest(),
            "payload_bytes":len(payload),
            "page":{
                "format":page.format,
                "window_start":page.window_start,
                "window_end":page.window_end,
                "page":page.page,
                "more_entries":page.more_entries,
                "event_count":len(parsed_events),
                "event_ids":event_ids,
            },
        }
        (out_dir / f"live-{name}-debug.json").write_text(
            json.dumps(debug,indent=2,ensure_ascii=False),
            encoding="utf-8",
        )

        event = target(page)

        errors = list(validator.iter_errors(event))
        if errors:
            raise AssertionError(
                f"{name} event failed schema: "
                + "; ".join(error.message for error in errors)
            )

        if event["action"] != "UPDATE":
            raise AssertionError(f"{name}: expected UPDATE")
        if "celex:32006D0241" not in event["identifiers"]:
            raise AssertionError(f"{name}: CELEX identifier missing")
        if event["wemi_levels"] != ["WORK"]:
            raise AssertionError(
                f"{name}: unexpected WEMI levels {event['wemi_levels']}"
            )

        outputs[name] = {
            "accept":accept,
            "request_url":response.url,
            "final_url":response.url,
            "status_code":response.status_code,
            "content_type":response.headers.get("Content-Type"),
            "payload_sha256":hashlib.sha256(payload).hexdigest(),
            "payload_bytes":len(payload),
            "page":{
                "format":page.format,
                "window_start":page.window_start,
                "window_end":page.window_end,
                "page":page.page,
                "more_entries":page.more_entries,
                "event_count":len(page.events),
            },
            "target_event":event,
        }

    if comparable(outputs["rss"]["target_event"]) != comparable(
        outputs["atom"]["target_event"]
    ):
        raise AssertionError(
            "RSS and Atom disagree on the durable notification payload"
        )

    result = {
        "probe_version":"0.1",
        "endpoint":ENDPOINT,
        "query":WINDOW,
        "target_notification_id":TARGET_NOTIFICATION_ID,
        "rss_atom_semantically_equal":True,
        "representations":outputs,
    }

    out = out_dir / "live-7081775.json"
    out.write_text(
        json.dumps(result,indent=2,ensure_ascii=False),
        encoding="utf-8",
    )
    print(json.dumps(result,indent=2,ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
