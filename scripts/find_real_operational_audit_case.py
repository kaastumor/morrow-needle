#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
from typing import Any

import requests

from needle.operations.pipeline import build_feed_card, build_operational_result
from needle.operations.state import lookup_baseline, validate_operational_state
from needle.updates.cellar_feed import parse_feed
from needle.updates.classify import build_source_change
from needle.updates.reobserve import reobserve_event


ENDPOINT="https://publications.europa.eu/webapi/notification/ingestion"
USER_AGENT=(
    "Morrow-Needle-Product-Audit-Hunter/0.1 "
    "(+https://github.com/kaastumor/morrow-needle)"
)


def iso(value: datetime) -> str:
    return value.astimezone(timezone.utc).replace(microsecond=0).isoformat()


def fetch_work_updates(start: datetime,end: datetime,max_pages: int) -> list[dict[str,Any]]:
    events=[]
    for page_number in range(1,max_pages+1):
        params={
            "startDate":iso(start),
            "endDate":iso(end),
            "type":"UPDATE",
            "wemiClasses":"work",
            "page":str(page_number),
        }
        response=requests.get(
            ENDPOINT,
            params=params,
            headers={"Accept":"application/rss+xml","User-Agent":USER_AGENT},
            timeout=120,
            allow_redirects=True,
        )
        response.raise_for_status()
        page=parse_feed(response.content)
        events.extend(page.events)
        if not page.more_entries:
            break
    else:
        raise AssertionError(
            f"work-update scan exceeded {max_pages} pages"
        )

    by_key={}
    for event in events:
        by_key.setdefault(event["event_key"],event)
    return sorted(
        by_key.values(),
        key=lambda e:(e["ingestion_time"],e["event_key"]),
        reverse=True,
    )


def main() -> int:
    parser=argparse.ArgumentParser()
    parser.add_argument("--state",default="data/operational-pilot-state-v0.1.json")
    parser.add_argument("--hours",type=int,default=8)
    parser.add_argument("--max-pages",type=int,default=20)
    parser.add_argument("--max-reobservations",type=int,default=20)
    parser.add_argument("--out",default="artifacts/product-audit-hunt")
    args=parser.parse_args()

    state=json.loads(Path(args.state).read_text(encoding="utf-8"))
    errors=validate_operational_state(state)
    if errors:
        raise AssertionError("invalid operational state: "+"; ".join(errors))

    end=datetime.now(timezone.utc)
    start=end-timedelta(hours=args.hours)
    events=fetch_work_updates(start,end,args.max_pages)

    processed=set(state.get("processed_event_keys",[]))
    eligible=[]
    rejected={}
    for event in events:
        if event["event_key"] in processed:
            rejected["ALREADY_PROCESSED"]=rejected.get("ALREADY_PROCESSED",0)+1
            continue
        lookup=lookup_baseline(state,event)
        if lookup["state"]!="ELIGIBLE":
            rejected[lookup["state"]]=rejected.get(lookup["state"],0)+1
            continue
        eligible.append((event,lookup))

    attempts=[]
    found=None
    for event,lookup in eligible[:args.max_reobservations]:
        reobservation=reobserve_event(event)
        change=build_source_change(
            event,
            previous=lookup["snapshot"],
            current=reobservation.get("snapshot"),
        )
        attempt={
            "event_key":event["event_key"],
            "identifiers":event.get("identifiers",[]),
            "ingestion_time":event["ingestion_time"],
            "baseline_key":lookup["baseline"]["baseline_key"],
            "baseline_observed_at":lookup["baseline"]["observed_at"],
            "reobservation_state":reobservation["state"],
            "classification":change["classification"],
        }
        attempts.append(attempt)
        if change["classification"] not in {
            "NO_MATERIAL_CHANGE","METADATA_ONLY"
        }:
            continue

        result=build_operational_result(
            event,
            change,
            downstream=None,
            source_unknowns=reobservation.get("unknowns",[]),
        )
        card=build_feed_card(result)
        if card["stream"]!="AUDIT_FEED":
            raise AssertionError(
                "accepted audit source classification did not route to AUDIT_FEED"
            )
        found={
            "character":"REAL_OPERATIONAL_AUDIT_CASE",
            "scan":{
                "start":iso(start),
                "end":iso(end),
                "work_update_count":len(events),
                "eligible_event_count":len(eligible),
                "rejected":rejected,
                "reobservation_attempt_count":len(attempts),
            },
            "event":event,
            "baseline":lookup["baseline"],
            "previous_snapshot":lookup["snapshot"],
            "reobservation":{
                "state":reobservation["state"],
                "snapshot":reobservation.get("snapshot"),
                "metadata_observation":reobservation.get("metadata_observation"),
                "content_observation":reobservation.get("content_observation"),
                "unknowns":reobservation.get("unknowns",[]),
            },
            "source_change":change,
            "operational_result":result,
            "feed_card":card,
            "acceptance_basis":(
                "A real official Work UPDATE occurred strictly after an existing "
                "prospective baseline, targeted re-observation completed, and "
                f"hash comparison classified it as {change['classification']}."
            ),
        }
        break

    out=Path(args.out)
    out.mkdir(parents=True,exist_ok=True)
    report={
        "scan":{
            "start":iso(start),
            "end":iso(end),
            "work_update_count":len(events),
            "eligible_event_count":len(eligible),
            "rejected":rejected,
            "reobservation_attempt_count":len(attempts),
        },
        "attempts":attempts,
        "found":found,
    }
    (out/"report.json").write_text(
        json.dumps(report,indent=2,ensure_ascii=False)+"\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "scan":report["scan"],
        "attempts":attempts,
        "found":None if found is None else {
            "event_key":found["event"]["event_key"],
            "identifiers":found["event"].get("identifiers",[]),
            "classification":found["source_change"]["classification"],
            "stream":found["feed_card"]["stream"],
            "headline":found["feed_card"]["headline"],
        },
    },indent=2,ensure_ascii=False))
    return 0 if found is not None else 2


if __name__=="__main__":
    raise SystemExit(main())
