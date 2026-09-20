import json
from copy import deepcopy
from pathlib import Path

from jsonschema import Draft202012Validator

from needle.provenance.ledger import (
    active_records,
    compute_record_hash,
    seal_record,
    trace_claim_support,
    validate_ledger,
    verify_record_hash,
)


SCHEMA = json.loads(
    Path("schemas/provenance-record-v0.1.schema.json").read_text(encoding="utf-8")
)
FIXTURE = json.loads(
    Path("fixtures/provenance/reg794-article3-dag-v0.1.json").read_text(encoding="utf-8")
)
RECORDS = FIXTURE["records"]


def test_all_provenance_records_validate_and_hash_verify():
    validator = Draft202012Validator(SCHEMA)
    errors = []
    for record in RECORDS:
        errors.extend(
            f"{record['record_id']}: {error.message}"
            for error in validator.iter_errors(record)
        )
        assert verify_record_hash(record), record["record_id"]
    assert errors == []
    assert validate_ledger(RECORDS) == []


def test_verified_sani_atom_traces_to_immutable_authentic_bytes():
    traces = trace_claim_support(
        RECORDS,
        entity_type="CHANGE_ATOM",
        entity_id="reg794-art3-sani-duty-v0.1",
    )
    assert len(traces) == 1
    trace = traces[0]
    source = trace["source_observation"]
    support = trace["support_record"]
    assert source["record_id"] == "src-reg271-2008-eng"
    assert source["payload"]["artifact_hash"] == (
        "sha256:c61ea6c41be9c3faf418a80c2ce12fcfb1233b91557eb4157ce2435c40afe5f7"
    )
    assert support["payload"]["source_span"]["artifact_hash"] == source["payload"]["artifact_hash"]
    assert support["payload"]["source_span"]["locator"] == (
        "L_2008082EN.01000101.xml#normalized-chars:7414-7551"
    )


def test_tampering_with_historical_record_invalidates_hash():
    tampered = deepcopy(RECORDS[2])
    original_hash = tampered["record_hash"]
    tampered["payload"]["identifier"] = "CELEX:TAMPERED"
    assert tampered["record_hash"] == original_hash
    assert verify_record_hash(tampered) is False
    assert compute_record_hash(tampered) != original_hash


def test_record_hash_is_canonical_not_key_order_dependent():
    source = deepcopy(RECORDS[0])
    source.pop("record_hash")
    reordered = {
        "payload": source["payload"],
        "created_at": source["created_at"],
        "record_type": source["record_type"],
        "record_id": source["record_id"],
    }
    assert seal_record(source)["record_hash"] == seal_record(reordered)["record_hash"]


def test_correction_is_append_only_and_original_remains_queryable():
    by_id = {record["record_id"]: record for record in RECORDS}
    old = by_id["support-audit-locator-v1"]
    new = by_id["support-audit-locator-v2"]
    correction = by_id["supersede-audit-locator-v1"]

    assert verify_record_hash(old)
    assert verify_record_hash(new)
    assert old["payload"]["source_span"]["locator"] == "Article 3(3) SANI sentence"
    assert new["payload"]["source_span"]["locator"].endswith("7414-7551")
    assert correction["payload"]["superseded_record_ids"] == [old["record_id"]]
    assert correction["payload"]["replacement_record_ids"] == [new["record_id"]]


def test_forward_reference_fails_append_only_ordering():
    records = deepcopy(RECORDS)
    diff = next(r for r in records if r["record_id"] == "run-diff-article3")
    records.remove(diff)
    records.insert(0, diff)
    errors = validate_ledger(records)
    assert any("reference is not an earlier ledger record" in error for error in errors)


def test_support_artifact_hash_must_match_source_observation():
    records = deepcopy(RECORDS)
    support = next(
        r for r in records if r["record_id"] == "support-atom-sani"
    )
    support["payload"]["source_span"]["artifact_hash"] = "sha256:" + ("0" * 64)
    support["record_hash"] = compute_record_hash(support)
    errors = validate_ledger(records)
    assert any(
        "source span artifact hash does not match source observation" in error
        for error in errors
    )


def test_mutation_keeps_before_after_and_cause_as_independent_support_edges():
    traces = trace_claim_support(
        RECORDS,
        entity_type="MUTATION",
        entity_id="reg794-article3-live-verified-v0.1",
    )
    assert {trace["support_record"]["payload"]["role"] for trace in traces} == {
        "BEFORE",
        "AFTER",
        "CAUSE",
    }
    assert {
        trace["source_observation"]["record_id"] for trace in traces
    } == {
        "src-reg794-20070119-eng",
        "src-reg794-20080414-eng",
        "src-reg271-2008-eng",
    }


def test_current_view_hides_superseded_record_without_erasing_history():
    current = {record["record_id"] for record in active_records(RECORDS)}
    historical = {record["record_id"] for record in RECORDS}

    assert "support-audit-locator-v1" in historical
    assert "support-audit-locator-v1" not in current
    assert "support-audit-locator-v2" in current
    assert "supersede-audit-locator-v1" not in current


def test_competing_supersession_of_same_record_is_rejected():
    records = deepcopy(RECORDS)
    extra = {
        "record_id":"supersede-audit-locator-v1-again",
        "record_type":"SUPERSESSION",
        "created_at":"2026-09-20T15:20:17Z",
        "payload":{
            "character":"CORRECTION",
            "superseded_record_ids":["support-audit-locator-v1"],
            "replacement_record_ids":["support-audit-locator-v2"],
            "reason":"Conflicting duplicate correction for negative control.",
        },
    }
    records.append(seal_record(extra))
    errors = validate_ledger(records)
    assert any(
        "support-audit-locator-v1 was already superseded" in error
        for error in errors
    )


def test_retraction_can_remove_record_from_current_view_without_replacement():
    base = RECORDS[:]
    target = next(
        record for record in base
        if record["record_id"] == "support-audit-locator-v2"
    )
    retraction = seal_record({
        "record_id":"retract-audit-locator-v2",
        "record_type":"SUPERSESSION",
        "created_at":"2026-09-20T15:20:18Z",
        "payload":{
            "character":"RETRACTION",
            "superseded_record_ids":[target["record_id"]],
            "replacement_record_ids":[],
            "reason":"Test-only retraction with no replacement.",
        },
    })
    records = base + [retraction]
    assert validate_ledger(records) == []
    current = {record["record_id"] for record in active_records(records)}
    assert target["record_id"] not in current


def test_all_article3_thread_atoms_have_source_mode_support():
    atom_ids = {
        "reg794-art3-sani-duty-v0.1",
        "reg794-art3-alt-channel-permission-v0.1",
        "reg794-art3-invalid-channel-status-v0.1",
        "reg794-art3-2025-notification-channel-duty-v0.1",
        "reg794-art3-2025-correspondence-channel-duty-v0.1",
        "reg794-art3-2025-crossref-exception-ripple-v0.1",
    }
    for atom_id in atom_ids:
        traces = trace_claim_support(
            RECORDS,
            entity_type="CHANGE_ATOM",
            entity_id=atom_id,
        )
        assert traces, atom_id
        assert all(trace["source_observation"] is not None for trace in traces)
        assert all(trace["derivation_record"] is not None for trace in traces)


def test_2025_mutation_keeps_before_after_and_cause_independent():
    traces = trace_claim_support(
        RECORDS,
        entity_type="MUTATION",
        entity_id="reg794-article3-p3-2025-live-verified-v0.1",
    )
    assert {trace["support_record"]["payload"]["role"] for trace in traces} == {
        "BEFORE",
        "AFTER",
        "CAUSE",
    }
    assert {
        trace["source_observation"]["record_id"] for trace in traces
    } == {
        "src-reg794-20161222-eng",
        "src-reg794-20250703-eng",
        "src-reg905-2025-eng",
    }


def test_2025_temporal_and_cross_reference_effect_preserve_evidence_character():
    temporal = trace_claim_support(
        RECORDS,
        entity_type="TEMPORAL_ASSERTION",
        entity_id="reg794-art3-p3-2025-application-start",
    )
    assert len(temporal) == 1
    assert temporal[0]["support_record"]["payload"]["role"] == "TEMPORAL"
    assert temporal[0]["support_record"]["payload"]["source_span"]["locator"].endswith(
        "13176-13316"
    )

    ripple = trace_claim_support(
        RECORDS,
        entity_type="CHANGE_ATOM",
        entity_id="reg794-art3-2025-crossref-exception-ripple-v0.1",
    )
    assert len(ripple) == 3
    assert {
        trace["support_record"]["payload"]["evidence_state"] for trace in ripple
    } == {"DERIVED"}
    assert {
        trace["support_record"]["payload"]["role"] for trace in ripple
    } == {"SEMANTIC_CLAIM", "CONTEXT"}
