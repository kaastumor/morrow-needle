#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator, RefResolver

from needle.operations.authentic_candidates import candidates_from_reobservation
from needle.operations.legal_analysis import (
    analyze_operational_legal,
    apply_operational_recency_gate,
    derive_publication_recency_from_reobservation,
    should_attempt_legal_analysis,
)
from needle.operations.pipeline import build_feed_card, build_operational_result
from needle.updates.classify import build_source_change
from needle.updates.relevance import classify_event_relevance
from needle.updates.reobserve import reobserve_event
from probe_reg2104_live_case import find_event


ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"artifacts"/"reg2104-live-case"


def validate(instance, schema_name):
    schema_path=ROOT/"schemas"/schema_name
    schema=json.loads(schema_path.read_text(encoding="utf-8"))
    store={}
    for path in (ROOT/"schemas").glob("*.json"):
        candidate=json.loads(path.read_text(encoding="utf-8"))
        if candidate.get("$id"):
            store[candidate["$id"]]=candidate
        store[path.name]=candidate
        store[path.resolve().as_uri()]=candidate
        store[
            f"https://morrow-needle.invalid/schemas/{path.name}"
        ]=candidate
    Draft202012Validator(
        schema,
        resolver=RefResolver(
            base_uri=schema.get("$id",schema_path.resolve().as_uri()),
            referrer=schema,
            store=store,
        ),
    ).validate(instance)


def main() -> int:
    event,_=find_event()
    reobservation=reobserve_event(event)
    if reobservation["state"] != "OBSERVED":
        raise AssertionError(
            "expected complete current re-observation for live replay, got "
            +reobservation["state"]
        )

    publication=reobservation["temporal_metadata"]["publication"]
    if publication["state"] != "RESOLVED":
        raise AssertionError(
            "expected resolved official publication metadata, got "
            +publication["state"]
        )
    if publication["assertion"]["normalized_date"] != "2026-09-18":
        raise AssertionError(
            "unexpected publication date: "
            +str(publication["assertion"]["normalized_date"])
        )

    change=build_source_change(
        event,
        previous=None,
        current=reobservation["snapshot"],
    )
    if not should_attempt_legal_analysis(
        relevance=classify_event_relevance(event),
        source_change=change,
    ):
        raise AssertionError(
            "cold-start live event did not reach canonical legal analysis"
        )

    candidates=candidates_from_reobservation(event,reobservation)
    legal=analyze_operational_legal(
        event,change,candidates=candidates
    )
    if legal["disposition"] != "LEGAL_CHANGE_VERIFIED":
        raise AssertionError(
            "generic authentic analyzer did not yield one verified mutation: "
            +json.dumps({
                "candidate_count":len(candidates),
                "candidates":[{
                    "semantic_key":item.get("semantic_key"),
                    "canonical_refs":item.get("canonical_refs"),
                    "what_changed":(
                        item.get("explanation") or {}
                    ).get("what_changed"),
                } for item in candidates],
                "legal":legal,
            },ensure_ascii=False)
        )

    recency=derive_publication_recency_from_reobservation(
        legal,event,reobservation
    )
    if recency is None or recency["state"] != "CURRENT_RELEVANT":
        raise AssertionError(
            "official publication did not establish current event-day "
            "relevance: "+json.dumps(recency,ensure_ascii=False)
        )

    downstream=apply_operational_recency_gate(
        legal,recency=recency
    )
    result=build_operational_result(
        event,
        change,
        downstream=downstream,
        source_unknowns=reobservation.get("unknowns",[]),
    )
    card=build_feed_card(result)
    validate(change,"source-change-v0.1.schema.json")
    validate(result,"operational-result-v0.1.schema.json")
    validate(card,"feed-card-v0.1.schema.json")

    if result["disposition"] != "LEGAL_CHANGE_VERIFIED":
        raise AssertionError("generic replay did not retain verified change")
    if card["stream"] != "CHANGE_FEED":
        raise AssertionError("generic replay did not emit CHANGE_FEED")
    if not any(
        ref.get("kind")=="TEMPORAL_ASSERTION"
        for ref in result["canonical_refs"]
    ):
        raise AssertionError(
            "positive result lacks canonical temporal assertion reference"
        )
    metadata_ref=reobservation["metadata_observation"]["record_id"]
    content_ref=reobservation["content_observation"]["record_id"]
    if metadata_ref not in card["source_mode"]["refs"]:
        raise AssertionError(
            "Source Mode lost publication-metadata observation provenance"
        )
    if content_ref not in card["source_mode"]["refs"]:
        raise AssertionError(
            "Source Mode lost authentic legal-text observation provenance"
        )

    later_event={
        **event,
        "ingestion_time":"2026-09-21T14:00:00+02:00",
    }
    historical_recency=derive_publication_recency_from_reobservation(
        legal,later_event,reobservation
    )
    historical=apply_operational_recency_gate(
        legal,recency=historical_recency
    )
    if historical_recency["state"] != "HISTORICAL_NOT_CURRENT":
        raise AssertionError(
            "later source refresh did not classify publication as historical"
        )
    if historical["disposition"] != "ABSTAIN_LEGAL_UNRESOLVED":
        raise AssertionError(
            "later source refresh resurrected an old legal publication"
        )

    bundle={
        "character":"GENERIC_OPERATIONAL_REPLAY",
        "trigger_event":event,
        "reobservation":{
            "state":reobservation["state"],
            "celex":reobservation["celex"],
            "metadata_observation_id":metadata_ref,
            "content_observation_id":content_ref,
            "publication":publication,
        },
        "source_change":change,
        "candidate_count":len(candidates),
        "legal_analysis":legal,
        "recency":recency,
        "operational_result":result,
        "feed_card":card,
        "historical_refresh_adversary":{
            "event_ingestion_time":later_event["ingestion_time"],
            "recency":historical_recency,
            "disposition":historical["disposition"],
        },
        "guardrail":(
            "Feed ingestion establishes operational novelty only. The legal "
            "relevance date comes from explicit Cellar publication metadata."
        ),
    }
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/"generic-operational-replay.json").write_text(
        json.dumps(bundle,indent=2,ensure_ascii=False)+"\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "event_key":event["event_key"],
        "candidate_count":len(candidates),
        "publication_date":publication["assertion"]["normalized_date"],
        "recency_state":recency["state"],
        "relevance_dimension":recency["relevance_dimension"],
        "stream":card["stream"],
        "headline":card["headline"],
        "source_mode_ref_count":len(card["source_mode"]["refs"]),
        "later_refresh_state":historical_recency["state"],
        "later_refresh_disposition":historical["disposition"],
    },indent=2,ensure_ascii=False))
    return 0


if __name__=="__main__":
    raise SystemExit(main())
