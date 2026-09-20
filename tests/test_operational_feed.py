import json
from pathlib import Path

from jsonschema import Draft202012Validator
import pytest

from needle.operations.pipeline import (
    OperationalPipelineError,
    build_feed_card,
    build_operational_result,
)
from needle.updates.classify import build_source_change


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


FIXTURE=load("fixtures/updates/source-change-adversaries-v0.1.json")
EVENT=FIXTURE["event"]
RESULT_SCHEMA=load("schemas/operational-result-v0.1.schema.json")
CARD_SCHEMA=load("schemas/feed-card-v0.1.schema.json")


def source_change(name):
    return build_source_change(
        EVENT,
        previous=FIXTURE["snapshots"]["before"],
        current=FIXTURE["snapshots"][name],
    )


def test_no_material_change_stays_out_of_legal_change_feed():
    result=build_operational_result(EVENT,source_change("same"))
    assert result["disposition"] == "NO_MATERIAL_CHANGE"
    assert result["stream"] == "AUDIT_FEED"
    assert result["canonical_refs"] == []

    card=build_feed_card(result)
    assert card["stream"] == "AUDIT_FEED"
    assert "No material source change" in card["headline"]
    assert card["evidence_character"] == "SOURCE_ONLY"
    assert card["source_mode"]["closed"] is True


def test_metadata_only_stays_source_only():
    result=build_operational_result(
        EVENT,source_change("metadata_changed")
    )
    assert result["disposition"] == "SOURCE_METADATA_ONLY"
    assert result["stream"] == "AUDIT_FEED"
    card=build_feed_card(result)
    assert "Metadata-only source update" in card["headline"]
    assert "legal content hash is unchanged" in card["what_changed"]


def test_content_change_without_legal_analysis_is_visible_abstention():
    result=build_operational_result(
        EVENT,source_change("content_changed")
    )
    assert result["disposition"] == (
        "SOURCE_CONTENT_CHANGED_UNRESOLVED"
    )
    assert result["stream"] == "ABSTENTION_FEED"
    assert result["unknowns"]

    card=build_feed_card(result)
    assert card["stream"] == "ABSTENTION_FEED"
    assert card["evidence_character"] == "UNRESOLVED"
    assert "Official source content changed" in card["headline"]


def test_verified_legal_change_requires_canonical_mutation_ref():
    change=source_change("content_changed")
    downstream={
        "disposition":"LEGAL_CHANGE_VERIFIED",
        "canonical_refs":[],
        "evidence_refs":["support-1"],
        "explanation":{
            "what_changed":"Article 3(3) was replaced.",
            "compared_with":"Previous Article 3(3).",
            "when_it_matters":"From 3 July 2025.",
            "affected":[],
            "evidence_character":"DIRECT",
        },
        "unknowns":[],
    }
    with pytest.raises(
        OperationalPipelineError,
        match="requires at least one canonical MUTATION ref",
    ):
        build_operational_result(
            EVENT,change,downstream=downstream
        )


def test_verified_legal_change_enters_main_feed_only_after_source_change():
    change=source_change("content_changed")
    downstream={
        "disposition":"LEGAL_CHANGE_VERIFIED",
        "canonical_refs":[
            {
                "kind":"MUTATION",
                "entity_id":"reg794-article3-p3-2025-live-verified-v0.1",
            },
            {
                "kind":"CHANGE_ATOM",
                "entity_id":"reg794-art3-2025-notification-channel-duty-v0.1",
            },
        ],
        "evidence_refs":[
            "support-mutation-p3-2025-cause",
            "support-atom-2025-notification-channel",
        ],
        "explanation":{
            "what_changed":"Article 3(3) was replaced with Commission-designated electronic channels.",
            "compared_with":"The prior SANI/PKI paragraph-3 channel rules.",
            "when_it_matters":"The replacement applies from 3 July 2025.",
            "affected":[],
            "evidence_character":"MIXED",
        },
        "unknowns":[
            "Technical identity between earlier named systems and later Commission-designated systems is not asserted."
        ],
    }
    result=build_operational_result(
        EVENT,change,downstream=downstream
    )
    assert result["disposition"] == "LEGAL_CHANGE_VERIFIED"
    assert result["stream"] == "CHANGE_FEED"

    card=build_feed_card(result)
    assert card["stream"] == "CHANGE_FEED"
    assert card["evidence_character"] == "MIXED"
    assert card["canonical_refs"][0]["kind"] == "MUTATION"
    assert card["unknowns"]


def test_metadata_only_cannot_be_laundered_into_verified_legal_change():
    downstream={
        "disposition":"LEGAL_CHANGE_VERIFIED",
        "canonical_refs":[{"kind":"MUTATION","entity_id":"fake"}],
        "evidence_refs":["support-fake"],
        "explanation":{
            "what_changed":"Fake legal change.",
            "compared_with":"Anything.",
            "when_it_matters":None,
            "affected":[],
            "evidence_character":"DIRECT",
        },
        "unknowns":[],
    }
    with pytest.raises(
        OperationalPipelineError,
        match="METADATA_ONLY source re-observation cannot emit",
    ):
        build_operational_result(
            EVENT,
            source_change("metadata_changed"),
            downstream=downstream,
        )


def test_result_and_card_ids_are_idempotent():
    change=source_change("same")
    first=build_operational_result(EVENT,change)
    second=build_operational_result(EVENT,change)
    assert first["result_id"] == second["result_id"]
    assert build_feed_card(first)["card_id"] == build_feed_card(second)["card_id"]


def test_source_mode_keeps_feed_event_source_change_and_observations():
    result=build_operational_result(EVENT,source_change("same"))
    refs=result["evidence_refs"]
    assert f"feed-event:{EVENT['event_key']}" in refs
    assert source_change("same")["change_id"] in refs
    assert "src-content-before" in refs
    assert "src-content-after-same" in refs


def test_operational_result_and_feed_card_schemas_validate():
    result=build_operational_result(EVENT,source_change("same"))

    # The operational schema intentionally embeds the complete canonical
    # source-change object. Validate that object with its owning schema, then
    # validate the process envelope using a local copy with the external
    # source-change reference replaced by a permissive object gate.
    source_schema=load("schemas/source-change-v0.1.schema.json")
    assert list(
        Draft202012Validator(source_schema).iter_errors(
            result["source_change"]
        )
    ) == []

    envelope=json.loads(json.dumps(RESULT_SCHEMA))
    envelope["properties"]["source_change"]={"type":"object"}
    assert list(
        Draft202012Validator(envelope).iter_errors(result)
    ) == []

    card=build_feed_card(result)
    assert list(
        Draft202012Validator(CARD_SCHEMA).iter_errors(card)
    ) == []
