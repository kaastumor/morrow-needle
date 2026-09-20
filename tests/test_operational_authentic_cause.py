import json
from pathlib import Path

import pytest

from needle.operations.pipeline import OperationalPipelineError, build_feed_card, build_operational_result
from needle.updates.classify import build_source_change


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


FIXTURE=load("fixtures/updates/source-change-adversaries-v0.1.json")
EVENT=FIXTURE["event"]
CURRENT=FIXTURE["snapshots"]["same"]


def downstream(route="AUTHENTIC_LEGAL_CAUSE"):
    return {
        "disposition":"LEGAL_CHANGE_VERIFIED",
        "verification_route":route,
        "canonical_refs":[{"kind":"MUTATION","entity_id":"reg2104-annexv-us-zones-1405-1406-v0.1"}],
        "evidence_refs":["CELEX:32026R2104#Annex-V-instruction"],
        "explanation":{
            "what_changed":"Annex V adds zones US-2.1405 and US-2.1406 after US-2.1404.",
            "compared_with":"The authentic amendment instruction; no consolidated after-state is asserted.",
            "when_it_matters":None,
            "affected":[],
            "evidence_character":"DIRECT",
        },
        "unknowns":["Consolidated text has not yet provided an after-state checkpoint."],
    }


def test_missing_baseline_can_emit_change_only_from_independent_authentic_cause():
    unresolved=build_source_change(EVENT,previous=None,current=CURRENT)
    assert unresolved["classification"] == "UNRESOLVED"
    assert "MISSING_BASELINE" in unresolved["classification_basis"]

    result=build_operational_result(EVENT,unresolved,downstream=downstream())
    assert result["stream"] == "CHANGE_FEED"
    assert result["disposition"] == "LEGAL_CHANGE_VERIFIED"
    assert result["source_change"]["classification"] == "UNRESOLVED"
    assert any("verified independently" in item for item in result["unknowns"])
    card=build_feed_card(result)
    assert card["stream"] == "CHANGE_FEED"
    assert card["evidence_character"] == "DIRECT"
    assert card["source_mode"]["closed"] is True


def test_missing_baseline_without_explicit_authentic_route_still_abstains():
    unresolved=build_source_change(EVENT,previous=None,current=CURRENT)
    with pytest.raises(OperationalPipelineError,match="independent authentic legal cause"):
        build_operational_result(EVENT,unresolved,downstream=downstream(route="SOURCE_DIFF"))


def test_missing_current_observation_cannot_be_overridden_by_authentic_route():
    unresolved=build_source_change(EVENT,previous=None,current=None)
    assert "MISSING_OBSERVATION" in unresolved["classification_basis"]
    with pytest.raises(OperationalPipelineError,match="independent authentic legal cause"):
        build_operational_result(EVENT,unresolved,downstream=downstream())
