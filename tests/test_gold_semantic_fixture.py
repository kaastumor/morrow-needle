import json
from pathlib import Path

from needle.gold import compare_expectations


CASE = json.loads(
    Path("fixtures/gold/reg794-article3-semantic-atoms-v0.1.json").read_text(
        encoding="utf-8"
    )
)
SEMANTIC = json.loads(
    Path("fixtures/semantic/reg794-article3-atoms-v0.1.json").read_text(
        encoding="utf-8"
    )
)
TEMPORAL = json.loads(
    Path("fixtures/temporal/reg794-article3-sani-v0.1.json").read_text(
        encoding="utf-8"
    )
)


def emitted_facts():
    facts = [
        {
            "kind":"SOURCE_MUTATION",
            "mutation_id":SEMANTIC["source_mutation"]["mutation_id"],
            "verification_state":SEMANTIC["source_mutation"]["verification_state"],
        }
    ]
    for atom in SEMANTIC["atoms"]:
        facts.append({
            "kind":"CHANGE_ATOM",
            "atom_id":atom["atom_id"],
            "legal_effect":atom["claim"]["legal_effect"],
            "verification_state":atom["verification_state"],
            "relations":atom["relations"],
            "temporal_assertion_refs":atom["temporal_assertion_refs"],
        })
    return facts


def test_semantic_decomposition_satisfies_gold_expectations():
    assert compare_expectations(CASE["machine_expectations"], emitted_facts()) == []


def test_gold_contract_rejects_false_all_correspondence_sani_atom():
    false_fact = {
        "kind":"CHANGE_ATOM",
        "atom_id":"bad-globalized-sani",
        "legal_effect":"DUTY",
        "verification_state":"VERIFIED",
        "claim_key":"ALL_CORRESPONDENCE_VIA_SANI",
    }
    errors = compare_expectations(
        CASE["machine_expectations"],
        emitted_facts() + [false_fact],
    )
    assert errors == [
        "nonatom.all-correspondence-sani: forbidden fact was emitted"
    ]


def test_sani_temporal_reference_exists_in_canonical_temporal_fixture():
    refs = {
        assertion["assertion_id"] for assertion in TEMPORAL["assertions"]
    }
    sani = next(
        atom for atom in SEMANTIC["atoms"]
        if atom["atom_id"] == "reg794-art3-sani-duty-v0.1"
    )
    assert set(sani["temporal_assertion_refs"]) <= refs
