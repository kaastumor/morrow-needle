#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from jsonschema import Draft202012Validator, RefResolver

from needle.mutation.instructions import (
    candidate_from_authentic_instruction,
    parse_authentic_keyed_row_insertions,
)
from needle.operations.pipeline import build_feed_card, build_operational_result
from probe_reg2104_live_case import CAUSE, fetch_celex, find_event

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts" / "reg2104-live-case"
PARENT = "Annex V"


def digest(value: dict) -> str:
    raw=json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()[:32]


def validate(instance: dict, schema_name: str) -> None:
    schema_path=ROOT / "schemas" / schema_name
    schema=json.loads(schema_path.read_text(encoding="utf-8"))
    resolver=RefResolver(base_uri=schema_path.resolve().as_uri(),referrer=schema)
    Draft202012Validator(schema,resolver=resolver).validate(instance)


def main() -> int:
    event,_=find_event()
    cause=fetch_celex(CAUSE)
    if cause.get("status") != 200 or not cause.get("text"):
        raise AssertionError("authentic 2026/2104 source unavailable")
    text=cause.pop("text")
    instructions=parse_authentic_keyed_row_insertions(text,source_id=f"CELEX:{CAUSE}",parent_locator=PARENT,locator=cause["final_url"])
    matches=[item for item in instructions if item.get("inserted_keys") == ["US-2.1405","US-2.1406"] and item.get("placement_anchor") == "US-2.1404"]
    if len(matches) != 1:
        raise AssertionError(f"expected exactly one evidenced US-2.1405/1406 insertion, got {len(matches)} from {len(instructions)} authentic insertion instructions")
    instruction=matches[0]

    mutation=candidate_from_authentic_instruction(instruction,kind="TABLE_ROWS",language="eng",candidate_id="mutation:reg2026-2104-annex-v-us-zones-1405-1406")
    validate(mutation,"mutation-candidate-v0.3.schema.json")

    content_hash=cause["artifact_hash"]
    observation_id=f"source-observation:{content_hash.removeprefix('sha256:')[:32]}"
    change_material={"event_key":event["event_key"],"content_hash":content_hash,"basis":"MISSING_BASELINE"}
    source_change={
        "change_id":f"source-change:{digest(change_material)}","event_key":event["event_key"],"feed_action":event["action"],"classification":"UNRESOLVED",
        "target_cellar_id":event["cellar_id"],"root_cellar_id":event["root_cellar_id"],"refresh_scope":"WORK","previous":None,
        "current":{"available":True,"content_hash":content_hash,"metadata_hash":None,"content_observation_id":observation_id,"metadata_observation_id":None},
        "classification_basis":["FEED_ACTION","MISSING_BASELINE"],"notes":"Live official UPDATE re-observed successfully; no pre-event comparator is asserted.",
    }
    validate(source_change,"source-change-v0.1.schema.json")

    downstream={
        "disposition":"LEGAL_CHANGE_VERIFIED","verification_route":"AUTHENTIC_LEGAL_CAUSE",
        "canonical_refs":[{"kind":"MUTATION","entity_id":mutation["candidate_id"]}],
        "evidence_refs":[f"authentic-act:CELEX:{CAUSE}",f"authentic-instruction:{mutation['candidate_id']}"],
        "explanation":{
            "what_changed":"Annex V, Part 1, Section B adds United States zones US-2.1405 and US-2.1406 after zone US-2.1404.",
            "compared_with":"The placement anchor US-2.1404 named by the authentic amending instruction; no before/after consolidated source pair is asserted.",
            "when_it_matters":"The legal change is established by Regulation (EU) 2026/2104; source-state comparison remains unresolved until an evidenced comparator exists.",
            "affected":["United States"],"evidence_character":"DIRECT",
        },"unknowns":[],
    }
    result=build_operational_result(event,source_change,downstream=downstream)
    card=build_feed_card(result)
    validate(result,"operational-result-v0.1.schema.json")
    validate(card,"feed-card-v0.1.schema.json")

    OUT.mkdir(parents=True,exist_ok=True)
    bundle={"character":"LIVE_OFFICIAL_EVENT_TO_PUBLIC_CARD","trigger_event":event,"authentic_source":cause,"authentic_instruction":instruction,"canonical_mutation":mutation,"source_change":source_change,"operational_result":result,"feed_card":card,"guardrail":"The CHANGE_FEED disposition is verified by the authentic legal cause, not by the unresolved source-diff branch."}
    (OUT/"change-feed-card.json").write_text(json.dumps(bundle,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps({"event_key":event["event_key"],"mutation_id":mutation["candidate_id"],"stream":card["stream"],"headline":card["headline"],"verification_route":card["verification_route"],"unknowns":card["unknowns"]},indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
