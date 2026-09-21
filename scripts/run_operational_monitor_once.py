#!/usr/bin/env python3
from __future__ import annotations

from collections import defaultdict
from datetime import datetime, timedelta, timezone
import hashlib
import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator
import requests

from needle.operations.authentic_candidates import candidates_from_reobservation
from needle.operations.legal_analysis import (
    analyze_operational_legal,
    apply_operational_recency_gate,
    derive_publication_recency_from_reobservation,
    should_attempt_legal_analysis,
)
from needle.operations.pipeline import (
    build_feed_card,
    build_operational_result,
)
from needle.operations.state import (
    advance_baseline,
    complete_poll_window,
    lookup_baseline,
    mark_event_processed,
    validate_operational_state,
)
from needle.updates.cellar_feed import parse_feed
from needle.updates.classify import build_source_change
from needle.updates.relevance import classify_event_relevance
from needle.updates.reobserve import reobserve_event


ENDPOINT="https://publications.europa.eu/webapi/notification/ingestion"
ACTIONS=("UPDATE","CREATE","DELETE")
WEMI_CLASSES=("work","expression","manifestation")
MAX_PAGES=25
STATE_PATH=Path("data/operational-pilot-state-v0.1.json")
OUT=Path("artifacts/operational-cycle")
USER_AGENT=(
    "Morrow-Needle-Operational-Monitor/0.1 "
    "(+https://github.com/kaastumor/morrow-needle)"
)


def instant(value: str) -> datetime:
    parsed=datetime.fromisoformat(value.replace("Z","+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("operational monitor timestamps must be offset-aware")
    return parsed


def iso(value: datetime) -> str:
    return value.astimezone(timezone.utc).replace(
        microsecond=0
    ).isoformat()


def fetch_feed(params: dict[str,str]):
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


def fetch_window(*,start: datetime,end: datetime) -> tuple[list[dict[str,Any]],list[dict[str,Any]]]:
    events=[]; observations=[]
    for action in ACTIONS:
        for wemi in WEMI_CLASSES:
            for page_number in range(1,MAX_PAGES+1):
                params={"startDate":iso(start),"endDate":iso(end),"type":action,"wemiClasses":wemi,"page":str(page_number)}
                payload,response=fetch_feed(params); page=parse_feed(payload)
                observations.append({"query":params,"request_url":response.url,"payload_sha256":hashlib.sha256(payload).hexdigest(),"event_count":len(page.events),"more_entries":page.more_entries})
                events.extend(page.events)
                if not page.more_entries: break
            else: raise AssertionError(f"feed pagination exceeded {MAX_PAGES} pages: {action}/{wemi}")
    by_key={}
    for event in events: by_key.setdefault(event["event_key"],event)
    return list(by_key.values()),observations


def select_representative(events: list[dict[str,Any]]) -> dict[str,Any]:
    wemi_rank={"WORK":0,"EXPRESSION":1,"MANIFESTATION":2,"ITEM":3}
    def key(event):
        relevance_rank=0 if classify_event_relevance(event)=="LEGAL_RESOURCE_CANDIDATE" else 1
        when=-instant(event["ingestion_time"]).timestamp()
        level=min((wemi_rank.get(value,9) for value in event.get("wemi_levels",[])),default=9)
        return (relevance_rank,when,level,event["event_key"])
    return sorted(events,key=key)[0]


def validate_card(card, schema):
    errors=list(Draft202012Validator(schema).iter_errors(card))
    if errors: raise AssertionError("feed card schema errors: "+"; ".join(error.message for error in errors))


def main() -> int:
    state=json.loads(STATE_PATH.read_text(encoding="utf-8")); errors=validate_operational_state(state)
    if errors: raise AssertionError("invalid operational state: "+"; ".join(errors))
    cursor=state["poll_cursor"]; last=instant(cursor["last_completed_end"]); overlap=timedelta(seconds=cursor["overlap_seconds"]); start=last-overlap; end=datetime.now(timezone.utc)
    if end <= last: raise AssertionError("monitor end must advance beyond completed cursor")
    events,feed_observations=fetch_window(start=start,end=end); processed=set(state.get("processed_event_keys",[])); new_events=[event for event in events if event["event_key"] not in processed]
    grouped=defaultdict(list)
    for event in new_events: grouped[event["root_cellar_id"]].append(event)

    cards=[]; results=[]; group_records=[]; next_state=state
    for root in sorted(grouped):
        group=sorted(grouped[root],key=lambda event:(instant(event["ingestion_time"]),event["event_key"])); representative=select_representative(group)
        related=[event["event_key"] for event in group if event["event_key"] != representative["event_key"]]
        relevance=classify_event_relevance(representative); source_unknowns=[]
        if len(group)>1: source_unknowns.append("Multiple feed notifications for this root were collapsed into one current-state refresh; intermediate source states were not reconstructed in this operational cycle.")
        lookup=lookup_baseline(next_state,representative)
        if lookup["state"] != "ELIGIBLE": source_unknowns.append(lookup["reason"]); previous=None
        else: previous=lookup["snapshot"]
        if relevance == "SOURCE_INFRASTRUCTURE":
            reobservation={"state":"OUT_OF_SCOPE_SOURCE_INFRASTRUCTURE","snapshot":None,"unknowns":[]}; current=None
        elif representative["action"] == "DELETE":
            reobservation={"state":"DELETE_EVENT_NO_CURRENT_REOBSERVATION","snapshot":None,"unknowns":["DELETE notification is an availability hint; no current artifact is assumed."]}; current=None
        else:
            reobservation=reobserve_event(representative,observed_at=end.isoformat()); current=reobservation.get("snapshot"); source_unknowns.extend(reobservation.get("unknowns",[]))
        change=build_source_change(representative,previous=previous,current=current)

        # Source comparison and legal verification are independent evidence
        # branches. A cold-start MISSING_BASELINE state must still cross the
        # legal-analysis boundary because an authentic legal cause can verify a
        # mutation independently. Missing current observation remains closed.
        downstream=None; candidates=[]
        if should_attempt_legal_analysis(relevance=relevance,source_change=change):
            candidates=candidates_from_reobservation(
                representative,reobservation
            )
            legal_analysis=analyze_operational_legal(
                representative,change,candidates=candidates
            )
            # The feed timestamp establishes only operational novelty. Legal
            # recency comes from explicit canonical temporal metadata for the
            # same authentic act; a later refresh of an old act remains
            # historical rather than being resurrected by Cellar activity.
            recency=derive_publication_recency_from_reobservation(
                legal_analysis,representative,reobservation
            )
            downstream=apply_operational_recency_gate(
                legal_analysis,recency=recency
            )
            downstream["unknowns"]=[
                *source_unknowns,*downstream.get("unknowns",[])
            ]

        result=build_operational_result(representative,change,downstream=downstream,source_unknowns=source_unknowns,related_event_keys=related); card=build_feed_card(result)
        results.append(result); cards.append(card)
        group_records.append({"root_cellar_id":root,"representative_event_key":representative["event_key"],"related_event_keys":related,"event_count":len(group),"baseline_lookup_state":lookup["state"],"reobservation_state":reobservation["state"],"source_change_classification":change["classification"],"legal_analysis_attempted":downstream is not None,"legal_candidate_count":len(candidates),"verification_route":downstream.get("verification_route") if downstream else None,"recency_state":(downstream.get("recency") or {}).get("state") if downstream else None,"disposition":result["disposition"],"stream":card["stream"]})
        if relevance == "LEGAL_RESOURCE_CANDIDATE" and current is not None and current.get("available") is True and (current.get("content_observation_id") or current.get("metadata_observation_id")):
            seed_character="POST_EVENT_REFRESH" if lookup["state"] == "ELIGIBLE" else "COLD_START_SEED"
            next_state=advance_baseline(next_state,representative,reobservation,updated_at=end.isoformat(),seed_character=seed_character,eligible_for_event_ingestion_after=end.isoformat())
        else: next_state=mark_event_processed(next_state,representative["event_key"],updated_at=end.isoformat())
        for event in group: next_state=mark_event_processed(next_state,event["event_key"],updated_at=end.isoformat())

    next_state=complete_poll_window(next_state,window_end=end.isoformat(),updated_at=end.isoformat()); errors=validate_operational_state(next_state)
    if errors: raise AssertionError("invalid next operational state: "+"; ".join(errors))
    card_schema=json.loads(Path("schemas/feed-card-v0.1.schema.json").read_text(encoding="utf-8"))
    for card in cards: validate_card(card,card_schema)
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/"state.json").write_text(json.dumps(next_state,indent=2,ensure_ascii=False)+"\n",encoding="utf-8"); (OUT/"cards.json").write_text(json.dumps(cards,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    report={"cycle_version":"0.1","window":{"start":iso(start),"previous_completed_end":cursor["last_completed_end"],"end":iso(end),"overlap_seconds":cursor["overlap_seconds"]},"feed_observations":feed_observations,"event_count_total":len(events),"event_count_new":len(new_events),"root_group_count":len(grouped),"groups":group_records,"stream_counts":{stream:sum(card["stream"] == stream for card in cards) for stream in ("CHANGE_FEED","AUDIT_FEED","ABSTENTION_FEED")},"disposition_counts":{disposition:sum(result["disposition"] == disposition for result in results) for disposition in sorted({result["disposition"] for result in results})},"baseline_count_before":len(state["baselines"]),"baseline_count_after":len(next_state["baselines"]),"source_observation_count_before":len(state["source_observations"]),"source_observation_count_after":len(next_state["source_observations"])}
    (OUT/"report.json").write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n",encoding="utf-8"); print(json.dumps(report,indent=2,ensure_ascii=False)); return 0


if __name__=="__main__": raise SystemExit(main())
