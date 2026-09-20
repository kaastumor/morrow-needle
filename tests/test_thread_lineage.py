import json
from pathlib import Path

from jsonschema import Draft202012Validator


SCHEMA = json.loads(
    Path("schemas/provision-lineage-v0.5.schema.json").read_text(encoding="utf-8")
)
FIXTURE = json.loads(
    Path("fixtures/lineage/reg794-article3-thread-lineage-v0.1.json").read_text(
        encoding="utf-8"
    )
)


def test_thread_lineage_edges_validate_against_frozen_v05_contract():
    validator = Draft202012Validator(SCHEMA)
    errors = []
    for edge in FIXTURE["edges"]:
        errors.extend(
            f"{edge['edge_id']}: {error.message}"
            for error in validator.iter_errors(edge)
        )
    assert errors == []


def test_structural_and_rule_lineage_are_separate_claims():
    structural = [
        edge for edge in FIXTURE["edges"]
        if edge["assertion_scope"] == "STRUCTURAL_LINEAGE"
    ]
    rules = [
        edge for edge in FIXTURE["edges"]
        if edge["assertion_scope"] == "RULE_LINEAGE"
    ]
    assert structural
    assert rules
    assert all(edge["rule_anchor"] is None for edge in structural)
    assert all(edge["rule_anchor"] for edge in rules)


def test_2008_and_2025_replacements_are_structurally_asserted_from_authentic_acts():
    by_id = {edge["edge_id"]: edge for edge in FIXTURE["edges"]}
    for edge_id in (
        "reg794-art3-pre2008-replaced-by-2008",
        "reg794-art3-p3-pre2025-replaced-by-2025",
    ):
        edge = by_id[edge_id]
        assert edge["claim_status"] == "ASSERTED"
        assert edge["edge_type"] == "REPLACED_BY"
        assert "OFFICIAL_AMENDMENT_INSTRUCTION" in edge["evidence_basis"]
        assert edge["confidence"]["conflict_state"] == "NO_KNOWN_CONFLICT"


def test_rule_continuity_does_not_claim_technical_system_identity():
    rule_edges = [
        edge for edge in FIXTURE["edges"]
        if edge["assertion_scope"] == "RULE_LINEAGE"
    ]
    assert {edge["confidence"]["level"] for edge in rule_edges} == {"MEDIUM"}
    assert {edge["evidence_state"] for edge in rule_edges} == {"INTERPRETIVE"}
    notes = " ".join(edge["notes"] for edge in rule_edges)
    assert "technically identical" in notes


def test_temporal_overreach_is_explicitly_forbidden():
    assert any(
        "SANI-specific 1 July 2008 qualifier" in inference
        for inference in FIXTURE["forbidden_inferences"]
    )
