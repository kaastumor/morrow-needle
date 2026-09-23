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
