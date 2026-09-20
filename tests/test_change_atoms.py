import json
from copy import deepcopy
from pathlib import Path

from jsonschema import Draft202012Validator

from needle.semantic.adversary import validate_atom


SCHEMA = json.loads(
    Path("schemas/change-atom-v0.3.schema.json").read_text(encoding="utf-8")
)
FIXTURE = json.loads(
    Path("fixtures/semantic/reg794-article3-atoms-v0.1.json").read_text(encoding="utf-8")
)
TEMPORAL = json.loads(
    Path("fixtures/temporal/reg794-article3-sani-v0.1.json").read_text(encoding="utf-8")
)

MUTATIONS = {
    FIXTURE["source_mutation"]["mutation_id"]: FIXTURE["source_mutation"]
}
SPANS = FIXTURE["source_span_registry"]
TEMPORAL_ASSERTIONS = {
    assertion["assertion_id"]: assertion for assertion in TEMPORAL["assertions"]
}


def test_verified_atoms_validate_against_v03_schema_and_adversary():
    validator = Draft202012Validator(SCHEMA)
    for atom in FIXTURE["atoms"]:
        assert list(validator.iter_errors(atom)) == []
        assert validate_atom(
            atom,
            mutations=MUTATIONS,
            source_span_registry=SPANS,
            temporal_assertions=TEMPORAL_ASSERTIONS,
        ) == []


def test_one_verified_textual_mutation_can_support_multiple_semantic_atoms():
    atoms = FIXTURE["atoms"]
    assert len(atoms) >= 2
    assert {
        mutation_id
        for atom in atoms
        for mutation_id in atom["source_mutation_ids"]
    } == {"reg794-article3-live-verified-v0.1"}
    assert {atom["claim"]["legal_effect"] for atom in atoms} >= {
        "DUTY",
        "LEGAL_STATUS",
    }


def test_sani_atom_references_temporal_truth_instead_of_copying_status():
    sani = next(
        atom for atom in FIXTURE["atoms"]
        if atom["atom_id"] == "reg794-art3-sani-duty-v0.1"
    )
    assert sani["temporal_assertion_refs"] == [
        "reg794-art3-p3-sani-application-start"
    ]
    assert "legal_state" not in sani
    assert "force_state" not in sani
    assert "procedure_state" not in sani


def test_plausible_but_unsupported_atom_is_rejected():
    negative = FIXTURE["negative_atoms"][0]["atom"]
    errors = validate_atom(
        negative,
        mutations=MUTATIONS,
        source_span_registry=SPANS,
        temporal_assertions=TEMPORAL_ASSERTIONS,
    )
    assert "unsupported semantic trigger term: 'All correspondence'" in errors


def test_verified_atom_cannot_depend_on_unverified_textual_mutation():
    atom = deepcopy(FIXTURE["atoms"][0])
    mutations = deepcopy(MUTATIONS)
    mutations["reg794-article3-live-verified-v0.1"]["verification_state"] = "UNVERIFIED"
    errors = validate_atom(
        atom,
        mutations=mutations,
        source_span_registry=SPANS,
        temporal_assertions=TEMPORAL_ASSERTIONS,
    )
    assert any("depends on unverified mutation" in error for error in errors)


def test_source_span_hash_mismatch_blocks_verified_atom():
    atom = deepcopy(FIXTURE["atoms"][0])
    atom["source_spans"][0]["text_hash"] = "0" * 64
    errors = validate_atom(
        atom,
        mutations=MUTATIONS,
        source_span_registry=SPANS,
        temporal_assertions=TEMPORAL_ASSERTIONS,
    )
    assert any("source span hash mismatch" in error for error in errors)


def test_unknown_temporal_reference_is_rejected():
    atom = deepcopy(FIXTURE["atoms"][0])
    atom["temporal_assertion_refs"] = ["invented-temporal-state"]
    errors = validate_atom(
        atom,
        mutations=MUTATIONS,
        source_span_registry=SPANS,
        temporal_assertions=TEMPORAL_ASSERTIONS,
    )
    assert errors == ["unknown temporal assertion: invented-temporal-state"]


def test_schema_rejects_reintroduction_of_collapsed_lifecycle_state():
    atom = deepcopy(FIXTURE["atoms"][0])
    atom["legal_state"] = {
        "force_state":"IN_FORCE_NOT_APPLICABLE"
    }
    assert list(Draft202012Validator(SCHEMA).iter_errors(atom))
