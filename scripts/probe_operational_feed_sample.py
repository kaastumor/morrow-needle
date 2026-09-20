#!/usr/bin/env python3
from __future__ import annotations

from datetime import datetime, timedelta, timezone
import hashlib
import json
from pathlib import Path
from typing import Any

import requests
from jsonschema import Draft202012Validator

from needle.operations.pipeline import (
    build_feed_card,
    build_operational_result,
)
from needle.provenance.ledger import verify_record_hash
from needle.updates.cellar_feed import parse_feed
from needle.updates.classify import build_source_change
from needle.updates.reobserve import reobserve_event


ENDPOINT="https://publications.europa.eu/webapi/notification/ingestion"
USER_AGENT=(
    "Morrow-Needle-Operational-Pilot/0.1 "
    "(+https://github.com/kaastumor/morrow-needle)"
)
ACTIONS=("UPDATE","CREATE","DELETE")
WEMI_CLASSES=("work","expression","manifestation")
MAX_LOOKBACK_DAYS=7
MAX_PAGES=3
TARGET_EVENTS=3


def iso(value: datetime) -> str:
    return value.astimezone(timezone.utc).replace(microsecond=0).isoformat()


def has_celex(event: dict[str,Any]) -> bool:
    return any(
        value.lower().startswith("celex:")
        for value in event.get("identifiers",[])
    )


def fetch_page(params: dict[str,str]) -> tuple[bytes,requests.Response]:
    response=requests.get(
        ENDPOINT,
        params=params,
        headers={
            "Accept":"application/rss+xml",
            "User-Agent":USER_AGENT,
        },
        timeout=120,
        allow_redirects=True,
    )
    response.raise_for_status()
    return response.content,response


def candidate_windows(now: datetime):
    # Search newest completed day/window first. Small one-day windows reduce
    # pagination pressure and keep the pilot reproducible from its artifact.
    for days_back in range(MAX_LOOKBACK_DAYS):
        end=(now - timedelta(days=days_back)).replace(
            hour=23,minute=59,second=59,microsecond=0
        )
        if days_back == 0:
            end=now.replace(microsecond=0)
        start=end.replace(hour=0,minute=0,second=0)
        yield start,end


def discover_events(now: datetime) -> tuple[list[dict[str,Any]],list[dict[str,Any]]]:
    found=[]
    attempts=[]
    seen_event_keys=set()
    seen_signatures=set()

    for start,end in candidate_windows(now):
        for action in ACTIONS:
            for wemi in WEMI_CLASSES:
                for page_number in range(1,MAX_PAGES+1):
                    params={
                        "startDate":iso(start),
                        "endDate":iso(end),
                        "type":action,
                        "wemiClasses":wemi,
                        "page":str(page_number),
                    }
                    try:
                        payload,response=fetch_page(params)
                        page=parse_feed(payload)
                    except Exception as exc:
                        attempts.append({
                            "query":params,
                            "state":"FETCH_OR_PARSE_ERROR",
                            "error":f"{type(exc).__name__}: {exc}",
                        })
                        break

                    attempts.append({
                        "query":params,
                        "state":"PARSED",
                        "request_url":response.url,
                        "payload_sha256":hashlib.sha256(payload).hexdigest(),
                        "event_count":len(page.events),
                        "more_entries":page.more_entries,
                    })

                    ordered=sorted(
                        page.events,
                        key=lambda event:(
                            not has_celex(event),
                            event["ingestion_time"],
                            event["event_key"],
                        ),
                    )
                    for event in ordered:
                        if event["event_key"] in seen_event_keys:
                            continue
                        signature=(
                            event["action"],
                            tuple(event.get("wemi_levels",[])),
                        )
                        # Prefer heterogeneity until we have three signatures.
                        if signature in seen_signatures:
                            continue
                        seen_event_keys.add(event["event_key"])
                        seen_signatures.add(signature)
                        found.append(event)
                        if len(found) >= TARGET_EVENTS:
                            return found,attempts

                    if not page.more_entries:
                        break

    return found,attempts


def validate_provenance_record(record: dict[str,Any] | None) -> None:
    if record is None:
        return
    if not verify_record_hash(record):
        raise AssertionError(
            f"provenance record hash invalid: {record['record_id']}"
        )


def main() -> int:
    now=datetime.now(timezone.utc)
    events,attempts=discover_events(now)
    if len(events) < TARGET_EVENTS:
        raise AssertionError(
            f"expected {TARGET_EVENTS} heterogeneous live Cellar events "
            f"within {MAX_LOOKBACK_DAYS} days, found {len(events)}"
        )

    event_schema=json.loads(
        Path("schemas/cellar-ingestion-event-v0.1.schema.json").read_text(
            encoding="utf-8"
        )
    )
    source_change_schema=json.loads(
        Path("schemas/source-change-v0.1.schema.json").read_text(
            encoding="utf-8"
        )
    )
    card_schema=json.loads(
        Path("schemas/feed-card-v0.1.schema.json").read_text(
            encoding="utf-8"
        )
    )

    cohort=[]
    for event in events:
        event_errors=list(
            Draft202012Validator(event_schema).iter_errors(event)
        )
        if event_errors:
            raise AssertionError(
                "live event schema failure: "
                + "; ".join(error.message for error in event_errors)
            )

        if event["action"] == "DELETE":
            observation={
                "state":"DELETE_EVENT_NO_CURRENT_REOBSERVATION",
                "celex":None,
                "snapshot":None,
                "metadata_observation":None,
                "content_observation":None,
                "attempts":[],
                "unknowns":[
                    "DELETE feed action is recorded as an availability-change hint; no current artifact is assumed."
                ],
            }
            current=None
        else:
            observation=reobserve_event(
                event,
                observed_at=now.isoformat(),
            )
            current=observation["snapshot"]

        validate_provenance_record(
            observation.get("metadata_observation")
        )
        validate_provenance_record(
            observation.get("content_observation")
        )

        change=build_source_change(
            event,
            previous=None,
            current=current,
        )
        change_errors=list(
            Draft202012Validator(source_change_schema).iter_errors(change)
        )
        if change_errors:
            raise AssertionError(
                "source-change schema failure: "
                + "; ".join(error.message for error in change_errors)
            )

        result=build_operational_result(event,change)
        card=build_feed_card(result)
        card_errors=list(
            Draft202012Validator(card_schema).iter_errors(card)
        )
        if card_errors:
            raise AssertionError(
                "feed-card schema failure: "
                + "; ".join(error.message for error in card_errors)
            )

        cohort.append({
            "event":event,
            "reobservation":observation,
            "source_change":change,
            "operational_result":result,
            "feed_card":card,
        })

    result={
        "pilot_version":"0.1",
        "character":"LIVE_COLD_START_OPERATIONAL_SAMPLE",
        "sampled_at":now.isoformat(),
        "lookback_days":MAX_LOOKBACK_DAYS,
        "selection_rule":(
            "first three distinct (feed action, WEMI level set) signatures; "
            "CELEX-addressable events preferred within each page"
        ),
        "attempts":attempts,
        "cohort":cohort,
        "summary":{
            "event_count":len(cohort),
            "signatures":[
                {
                    "action":item["event"]["action"],
                    "wemi_levels":item["event"]["wemi_levels"],
                }
                for item in cohort
            ],
            "source_change_classifications":[
                item["source_change"]["classification"]
                for item in cohort
            ],
            "operational_dispositions":[
                item["operational_result"]["disposition"]
                for item in cohort
            ],
            "streams":[
                item["feed_card"]["stream"]
                for item in cohort
            ],
        },
        "cold_start_guardrail":(
            "No pre-event baseline snapshots are available in this pilot. "
            "UPDATE events therefore remain unresolved rather than being "
            "interpreted from the feed action alone."
        ),
    }

    out=Path("artifacts/operational-pilot")
    out.mkdir(parents=True,exist_ok=True)
    (out/"live-cold-start-v0.1.json").write_text(
        json.dumps(result,indent=2,ensure_ascii=False)+"\n",
        encoding="utf-8",
    )
    (out/"feed-cards-v0.1.json").write_text(
        json.dumps(
            [item["feed_card"] for item in cohort],
            indent=2,
            ensure_ascii=False,
        )+"\n",
        encoding="utf-8",
    )
    print(json.dumps(result["summary"],indent=2,ensure_ascii=False))
    return 0


if __name__=="__main__":
    raise SystemExit(main())
