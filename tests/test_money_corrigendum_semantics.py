import json
from copy import deepcopy
from pathlib import Path

from jsonschema import Draft202012Validator

from needle.mutation.instructions import parse_authentic_corrigendum_replacements
from needle.mutation.reconcile import reconcile_candidate
from needle.semantic.adversary import validate_atom


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


SOURCE = load("fixtures/audit/reg2742-money-corrigendum-source-v0.1.json")
MUTATION = load(
    "fixtures/mutations/reg2742-art4p1-eng-money-corrigendum-v0.1.json"
)
SEMANTIC = load(
    "fixtures/semantic/reg2742-art4p1-eng-money-atom-v0.1.json"
)
LANGUAGE_EVENT = load(
    "fixtures/multilingual/reg2742-1990-english-money-corrigendum-v0.1.json"
)
MUTATION_SCHEMA = load("schemas/mutation-candidate-v0.2.schema.json")
ATOM_SCHEMA = load("schemas/change-atom-v0.3.schema.json")


def test_money_corrigendum_mutation_validates_v02_without_fake_checkpoints():
    assert list(
        Draft202012Validator(MUTATION_SCHEMA).iter_errors(MUTATION)
    ) == []
    assert MUTATION["verification_state"] == "VERIFIED"
    assert MUTATION["before"] is None
    assert MUTATION["after"] is None
    assert MUTATION["feature_deltas"]["numbers_removed"] == ["225"]
    assert MUTATION["feature_deltas"]["numbers_added"] == ["255"]


def test_authentic_corrigendum_instruction_reconciles_to_verified_mutation():
    parsed = parse_authentic_corrigendum_replacements(
        SOURCE["correction"]["text"],
        source_id=SOURCE["corrigendum"],
        locator=SOURCE["correction"]["locator"],
    )
    assert len(parsed) == 1

    candidate = deepcopy(MUTATION)
    candidate["supporting_evidence"] = []
    candidate["reconciliation_state"] = "DIFF_ONLY"
    candidate["verification_state"] = "UNVERIFIED"

    result = reconcile_candidate(candidate, [parsed[0]["evidence"]])
    assert result["verification_state"] == "VERIFIED"
    assert result["reconciliation_state"] == "CORROBORATED"
    assert result["supporting_evidence"] == MUTATION["supporting_evidence"]


def test_money_change_atom_validates_and_keeps_expression_scope():
    atom = SEMANTIC["atoms"][0]
    assert list(Draft202012Validator(ATOM_SCHEMA).iter_errors(atom)) == []

    errors = validate_atom(
        atom,
        mutations={
            MUTATION["candidate_id"]:{
                "mutation_id":MUTATION["candidate_id"],
                "verification_state":MUTATION["verification_state"],
                "operation":MUTATION["operation"],
                "target":MUTATION["target"]["citation_path"],
            }
        },
        source_span_registry=SEMANTIC["source_span_registry"],
        temporal_assertions={},
    )
    assert errors == []
    assert atom["claim"]["dimensions"] == ["MONEY"]
    assert atom["language_scope"] == {
        "languages":["ENG"],
        "cross_language_equivalence_assumed":False,
    }


def test_change_atom_scope_matches_official_corrigendum_expression_scope():
    official_scope = LANGUAGE_EVENT["events"][0]["expression_scope"]
    atom_scope = SEMANTIC["atoms"][0]["language_scope"]
    assert official_scope["languages"] == atom_scope["languages"] == ["ENG"]
    assert official_scope["nonlisted_semantics"] == "NO_ASSERTION"
    assert atom_scope["cross_language_equivalence_assumed"] is False


def test_globalizing_english_money_atom_is_rejected():
    atom = deepcopy(SEMANTIC["atoms"][0])
    atom["language_scope"]["languages"] = ["ENG","DEU","FRA"]

    errors = validate_atom(
        atom,
        mutations={
            MUTATION["candidate_id"]:{
                "verification_state":"VERIFIED"
            }
        },
        source_span_registry=SEMANTIC["source_span_registry"],
        temporal_assertions={},
    )
    assert errors == [
        "VERIFIED atom claims language without source-span evidence: DEU",
        "VERIFIED atom claims language without source-span evidence: FRA",
    ]


def test_relabelling_provision_reference_language_is_rejected():
    atom = deepcopy(SEMANTIC["atoms"][0])
    atom["provision_refs"][0]["language"] = "DEU"

    errors = validate_atom(
        atom,
        mutations={
            MUTATION["candidate_id"]:{
                "verification_state":"VERIFIED"
            }
        },
        source_span_registry=SEMANTIC["source_span_registry"],
        temporal_assertions={},
    )
    assert errors == [
        "provision reference language outside atom language scope: DEU"
    ]


def test_current_corrected_display_is_not_used_as_original_printed_state():
    notes = MUTATION["notes"].casefold()
    invariants = " ".join(SOURCE["invariants"]).casefold()
    assert "no historical consolidated before/after checkpoint is invented" in notes
    assert "current corrected display is not evidence" in invariants
