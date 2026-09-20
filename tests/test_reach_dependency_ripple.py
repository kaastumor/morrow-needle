import json
from copy import deepcopy
from pathlib import Path

from jsonschema import Draft202012Validator

from needle.semantic.adversary import validate_atom


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


DISCOVERY = load(
    "fixtures/discovery/reach-art67-annex17-entry78-ripple-v0.1.json"
)
MUTATION = load(
    "fixtures/mutations/reach-annex17-entry78-2023-insert-v0.1.json"
)
SEMANTIC = load(
    "fixtures/semantic/reach-art67-annex17-entry78-ripple-v0.1.json"
)
MUTATION_SCHEMA = load("schemas/mutation-candidate-v0.2.schema.json")
ATOM_SCHEMA = load("schemas/change-atom-v0.3.schema.json")


def test_reach_upstream_insert_is_verified_without_fabricating_local_mutation():
    assert list(
        Draft202012Validator(MUTATION_SCHEMA).iter_errors(MUTATION)
    ) == []
    assert MUTATION["operation"] == "INSERT"
    assert MUTATION["verification_state"] == "VERIFIED"
    assert MUTATION["target"]["citation_path"] == "Annex XVII > entry 78"
    assert MUTATION["before"] is None
    assert MUTATION["after"] is None
    assert {
        item["channel"] for item in MUTATION["supporting_evidence"]
    } == {"AUTHENTIC_ACT","CONSOLIDATED_CHECKPOINT"}
    assert "Article 67" not in MUTATION["target"]["citation_path"]


def test_reach_local_article67_subtree_is_exactly_unchanged():
    local = DISCOVERY["local_continuity"]
    assert local["before"]["text_hash"] == local["after"]["text_hash"]
    assert local["before"]["text_length"] == local["after"]["text_length"] == 501
    assert local["result"] == "IDENTICAL_CANONICAL_SUBTREE"
    assert local["textual_mutation"] is None


def test_reach_dependency_edge_is_explicit_and_stable_across_transition():
    dep = DISCOVERY["dependency"]
    assert dep["relation_type"] == "OPERATIVE_REFERENCE"
    assert dep["source"] == "CELEX:32006R1907#Article67(1)"
    assert dep["target"] == "CELEX:32006R1907#AnnexXVII"
    assert "Annex XVII contains a restriction" in dep["text"]
    assert dep["before_locator"] != dep["after_locator"]


def test_reach_dependency_ripple_atom_validates_as_evidenced_derived_claim():
    atom = SEMANTIC["atoms"][0]
    assert list(Draft202012Validator(ATOM_SCHEMA).iter_errors(atom)) == []
    errors = validate_atom(
        atom,
        mutations={
            MUTATION["candidate_id"]:{
                "verification_state":MUTATION["verification_state"],
                "operation":MUTATION["operation"],
                "target":MUTATION["target"]["citation_path"],
            }
        },
        source_span_registry=SEMANTIC["source_span_registry"],
        temporal_assertions={},
    )
    assert errors == []
    assert atom["verification_state"] == "EVIDENCED"
    assert atom["evidence_state"] == "DERIVED"
    assert atom["claim"]["legal_effect"] == "PROHIBITION"
    assert set(atom["claim"]["dimensions"]) == {
        "SCOPE","ANNEX","CROSS_REFERENCE"
    }


def test_reach_ripple_cannot_be_silently_promoted_to_verified():
    atom = deepcopy(SEMANTIC["atoms"][0])
    atom["verification_state"] = "VERIFIED"
    schema_errors = list(
        Draft202012Validator(ATOM_SCHEMA).iter_errors(atom)
    )
    assert schema_errors
    assert any(
        "UNRESOLVED" in error.message
        for error in schema_errors
    )


def test_reach_ripple_evidence_combines_local_dependency_and_upstream_change():
    atom = SEMANTIC["atoms"][0]
    by_id = {
        span["span_id"]:span for span in atom["source_spans"]
    }
    assert by_id["span-reach-art67-annex17-dependency"]["role"] == (
        "SEMANTIC_CLAIM"
    )
    assert by_id["span-reach-2023-entry78"]["role"] == "CONTEXT"
    assert {
        span["identifier"] for span in atom["source_spans"]
    } == {
        "CELEX:02006R1907-20230806",
        "CELEX:32023R2055",
        "CELEX:02006R1907-20231201",
    }


def test_reach_ripple_does_not_invent_temporal_or_cross_language_truth():
    atom = SEMANTIC["atoms"][0]
    assert atom["temporal_assertion_refs"] == []
    assert atom["language_scope"] == {
        "languages":["ENG"],
        "cross_language_equivalence_assumed":False,
    }
    assert atom["provision_refs"] == [{
        "provision_instance_id":None,
        "citation_path":"Article 67 > 1",
        "language":"ENG",
    }]


def test_reach_negative_regressions_forbid_local_mutation_and_direct_effect():
    forbidden = " ".join(
        item["forbidden_inference"]
        for item in SEMANTIC["negative_atoms"]
    ).casefold()
    assert "inserted or replaced text in article 67(1)" in forbidden
    assert "direct local textual change" in forbidden
    assert DISCOVERY["derived_ripple"]["local_mutation"] is False
    assert DISCOVERY["derived_ripple"]["character"] == "DERIVED"
