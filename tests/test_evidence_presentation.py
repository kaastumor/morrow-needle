from copy import deepcopy
import json
from pathlib import Path

import pytest

from needle.operations.pipeline import build_feed_card, build_operational_result
from needle.presentation.evidence import (
    EvidencePresentationError,
    build_evidence_view,
)
from needle.provenance.ledger import seal_record
from needle.updates.classify import build_source_change


FIXTURE=json.loads(
    Path("fixtures/updates/source-change-adversaries-v0.1.json").read_text(
        encoding="utf-8"
    )
)
EVENT=FIXTURE["event"]


def source_change(name):
    return build_source_change(
        EVENT,
        previous=FIXTURE["snapshots"]["before"],
        current=FIXTURE["snapshots"][name],
    )


def observation(
    record_id,
    *,
    identifier="CELEX:32026R0001",
    language="ENG",
    representation="STRUCTURED_LEGAL_XML",
):
    return seal_record({
        "record_id":record_id,
        "record_type":"SOURCE_OBSERVATION",
        "created_at":"2026-09-20T10:01:00+00:00",
        "payload":{
            "source_type":"CELLAR",
            "identifier":identifier,
            "resource_uri":"https://publications.europa.eu/resource/celex/32026R0001",
            "language":language,
            "representation_class":representation,
            "observed_at":"2026-09-20T10:01:00+00:00",
            "artifact_hash":"sha256:"+"a"*64,
            "retrieval":{
                "final_uri":"https://publications.europa.eu/resource/cellar/example",
                "media_type":"application/xml",
                "http_status":200,
            },
        },
    })


def records_for(change):
    ids=[]
    for side in ("previous","current"):
        snapshot=change[side]
        for field in ("content_observation_id","metadata_observation_id"):
            if snapshot and snapshot.get(field):
                ids.append(snapshot[field])
    return [
        observation(
            record_id,
            representation=(
                "STRUCTURED_LEGAL_XML"
                if "content" in record_id
                else "CELLAR_RDF_METADATA"
            ),
        )
        for record_id in ids
    ]


def test_metadata_only_evidence_view_is_human_readable_and_closed():
    change=source_change("metadata_changed")
    result=build_operational_result(EVENT,change)
    card=build_feed_card(result)

    view=build_evidence_view(
        card,result,
        provenance_records=records_for(change),
        expected_language="ENG",
    )

    assert view["state"] == "CLOSED"
    assert view["unresolved_refs"] == []
    assert view["title"] == "Evidence / Why this is shown"
    labels=[item["label"] for item in view["items"]]
    assert any("Publications Office UPDATE notification" in label for label in labels)
    assert any("Metadata-only comparison" in label for label in labels)
    assert any("CELLAR STRUCTURED_LEGAL_XML — CELEX:32026R0001 (ENG)" in label for label in labels)

    comparison=next(item for item in view["items"] if item["kind"] == "SOURCE_COMPARISON")
    assert comparison["evidence_character"] == "SOURCE_ONLY"
    assert "does not establish a legal-text mutation" in comparison["does_not_establish"]


def test_missing_record_stays_explicitly_unresolved_without_friendly_guess():
    change=source_change("same")
    result=build_operational_result(EVENT,change)
    card=build_feed_card(result)
    records=records_for(change)[:-1]
    missing=change["current"]["metadata_observation_id"]

    view=build_evidence_view(
        card,result,
        provenance_records=records,
        expected_language="ENG",
    )

    assert view["state"] == "PARTIAL"
    assert missing in view["unresolved_refs"]
    assert all(
        item["label"] != missing
        for item in view["items"]
    )


def test_tampered_source_observation_fails_closed():
    change=source_change("same")
    result=build_operational_result(EVENT,change)
    card=build_feed_card(result)
    records=records_for(change)
    records[0]["payload"]["identifier"]="CELEX:TAMPERED"

    with pytest.raises(EvidencePresentationError,match="invalid provenance record hash"):
        build_evidence_view(
            card,result,
            provenance_records=records,
            expected_language="ENG",
        )


def test_cross_celex_source_observation_is_rejected():
    change=source_change("same")
    result=build_operational_result(EVENT,change)
    card=build_feed_card(result)
    records=records_for(change)
    target=change["current"]["content_observation_id"]
    records=[
        observation(
            target,
            identifier="CELEX:39999R9999",
        ) if record["record_id"] == target else record
        for record in records
    ]

    with pytest.raises(EvidencePresentationError,match="CELEX does not match"):
        build_evidence_view(
            card,result,
            provenance_records=records,
            expected_language="ENG",
        )


def test_explicit_language_scope_rejects_cross_language_binding():
    change=source_change("same")
    result=build_operational_result(EVENT,change)
    card=build_feed_card(result)
    records=records_for(change)
    target=change["current"]["content_observation_id"]
    records=[
        observation(target,language="FRA")
        if record["record_id"] == target else record
        for record in records
    ]

    with pytest.raises(EvidencePresentationError,match="language does not match"):
        build_evidence_view(
            card,result,
            provenance_records=records,
            expected_language="ENG",
        )


def test_authentic_cause_label_requires_explicit_matching_language_scope():
    change=source_change("content_changed")
    current_content=change["current"]["content_observation_id"]
    downstream={
        "disposition":"LEGAL_CHANGE_VERIFIED",
        "verification_route":"AUTHENTIC_LEGAL_CAUSE",
        "canonical_refs":[
            {"kind":"MUTATION","entity_id":"mutation:test"},
        ],
        "evidence_refs":[current_content],
        "explanation":{
            "what_changed":"A bounded authentic amendment was verified.",
            "compared_with":"The authentic placement instruction.",
            "when_it_matters":None,
            "affected":[],
            "evidence_character":"DIRECT",
        },
        "unknowns":["Application timing is not established."],
    }
    result=build_operational_result(EVENT,change,downstream=downstream)
    card=build_feed_card(result)
    records=records_for(change)

    unscoped=build_evidence_view(
        card,result,provenance_records=records
    )
    unscoped_item=next(
        item for item in unscoped["items"]
        if item["ref"] == current_content
    )
    assert unscoped_item["evidence_character"] == "SOURCE_ONLY"
    assert "authentic-cause verification" not in unscoped_item["supports"]

    scoped=build_evidence_view(
        card,result,
        provenance_records=records,
        expected_language="ENG",
    )
    scoped_item=next(
        item for item in scoped["items"]
        if item["ref"] == current_content
    )
    assert scoped_item["evidence_character"] == "DIRECT"
    assert "authentic-cause verification" in scoped_item["supports"]


def test_card_result_cross_binding_is_rejected():
    change=source_change("same")
    result=build_operational_result(EVENT,change)
    card=build_feed_card(result)
    card=deepcopy(card)
    card["operational_result_id"]="operational-result:wrong"

    with pytest.raises(EvidencePresentationError,match="does not belong"):
        build_evidence_view(card,result)


def temporal_assertion(
    assertion_id="temporal-publication:test",
    *,
    identifier="CELEX:32026R0001",
    dimension="PUBLICATION",
    resolution_state="RESOLVED_ABSOLUTE",
    normalized_date="2026-09-20",
):
    assertion={
        "assertion_id":assertion_id,
        "subject_ref":{
            "kind":"LEGAL_ACT",
            "identifier":identifier,
            "locator":"official publication metadata",
        },
        "dimension":dimension,
        "boundary":"POINT",
        "inclusive":True,
        "trigger":{
            "kind":"ABSOLUTE_DATE",
            "date":normalized_date or "2026-09-20",
            "source_expression":"test source",
        },
        "scope":{
            "mode":"DEFAULT",
            "applies_to":["ACT:32026R0001"],
            "overrides_assertion_ids":[],
            "entity_condition":None,
        },
        "resolution_state":resolution_state,
        "evidence_state":"DIRECT",
        "source_refs":[{
            "source_type":"CELLAR",
            "identifier":identifier,
            "locator":"CELLAR_RDF_NOTICE_TREE#publication",
            "language":None,
            "role":"PUBLICATION_METADATA",
        }],
        "notes":None,
    }
    if normalized_date is not None:
        assertion["normalized_date"]=normalized_date
    return assertion


def test_matching_canonical_temporal_assertion_closes_evidence_ref():
    change=source_change("content_changed")
    assertion=temporal_assertion()
    downstream={
        "disposition":"LEGAL_CHANGE_VERIFIED",
        "verification_route":"SOURCE_DIFF",
        "canonical_refs":[
            {"kind":"MUTATION","entity_id":"mutation:test"},
            {"kind":"TEMPORAL_ASSERTION","entity_id":assertion["assertion_id"]},
        ],
        "evidence_refs":[assertion["assertion_id"]],
        "explanation":{
            "what_changed":"A legal change was verified.",
            "compared_with":"The prior source.",
            "when_it_matters":"Publication is 20 September 2026.",
            "affected":[],
            "evidence_character":"DIRECT",
        },
        "unknowns":[],
    }
    result=build_operational_result(EVENT,change,downstream=downstream)
    card=build_feed_card(result)
    view=build_evidence_view(
        card,result,
        provenance_records=records_for(change),
        temporal_assertions=[assertion],
        expected_language="ENG",
    )
    item=next(
        item for item in view["items"]
        if item["ref"] == assertion["assertion_id"]
    )
    assert view["state"] == "CLOSED"
    assert item["kind"] == "TEMPORAL_ASSERTION"
    assert item["normalized_date"] == "2026-09-20"
    assert "Publication does not establish entry into force or application" in item["does_not_establish"]


def test_temporal_object_requires_typed_canonical_ref_before_humanizing():
    change=source_change("content_changed")
    assertion=temporal_assertion()
    downstream={
        "disposition":"LEGAL_CHANGE_VERIFIED",
        "verification_route":"SOURCE_DIFF",
        "canonical_refs":[{"kind":"MUTATION","entity_id":"mutation:test"}],
        "evidence_refs":[assertion["assertion_id"]],
        "explanation":{
            "what_changed":"A legal change was verified.",
            "compared_with":"The prior source.",
            "when_it_matters":None,
            "affected":[],
            "evidence_character":"DIRECT",
        },
        "unknowns":[],
    }
    result=build_operational_result(EVENT,change,downstream=downstream)
    card=build_feed_card(result)
    view=build_evidence_view(
        card,result,
        provenance_records=records_for(change),
        temporal_assertions=[assertion],
    )
    assert assertion["assertion_id"] in view["unresolved_refs"]
    assert view["state"] == "PARTIAL"


def test_cross_celex_temporal_assertion_is_rejected():
    change=source_change("content_changed")
    assertion=temporal_assertion(identifier="CELEX:39999R9999")
    downstream={
        "disposition":"LEGAL_CHANGE_VERIFIED",
        "verification_route":"SOURCE_DIFF",
        "canonical_refs":[
            {"kind":"MUTATION","entity_id":"mutation:test"},
            {"kind":"TEMPORAL_ASSERTION","entity_id":assertion["assertion_id"]},
        ],
        "evidence_refs":[assertion["assertion_id"]],
        "explanation":{
            "what_changed":"A legal change was verified.",
            "compared_with":"The prior source.",
            "when_it_matters":None,
            "affected":[],
            "evidence_character":"DIRECT",
        },
        "unknowns":[],
    }
    result=build_operational_result(EVENT,change,downstream=downstream)
    card=build_feed_card(result)
    with pytest.raises(EvidencePresentationError,match="subject CELEX does not match"):
        build_evidence_view(
            card,result,
            provenance_records=records_for(change),
            temporal_assertions=[assertion],
        )


def test_conflicting_duplicate_temporal_assertions_fail_closed():
    first=temporal_assertion()
    second=deepcopy(first)
    second["normalized_date"]="2026-09-21"
    with pytest.raises(EvidencePresentationError,match="conflicting Temporal Assertions"):
        build_evidence_view(
            {"operational_result_id":"result","source_mode":{"refs":[]},"evidence_character":"UNRESOLVED","card_id":"card","unknowns":[]},
            {"result_id":"result","evidence_refs":[],"canonical_refs":[],"trigger":{"identifiers":[],"related_event_keys":[],"event_key":"evt","feed_action":"UPDATE"},"source_change":{"change_id":"source-change:test","classification":"UNRESOLVED"}},
            temporal_assertions=[first,second],
        )
