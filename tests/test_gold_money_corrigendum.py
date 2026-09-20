import json
from pathlib import Path

from jsonschema import Draft202012Validator

from needle.gold import compare_expectations


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


SCHEMA = load("schemas/gold-corpus-case-v0.2.schema.json")
CASE = load(
    "fixtures/gold/reg2742-money-corrigendum-language-scope-v0.1.json"
)
MUTATION = load(
    "fixtures/mutations/reg2742-art4p1-eng-money-corrigendum-v0.1.json"
)
SEMANTIC = load(
    "fixtures/semantic/reg2742-art4p1-eng-money-atom-v0.1.json"
)


def emitted_facts():
    atom=SEMANTIC["atoms"][0]
    return [
        {
            "kind":"SOURCE_MUTATION",
            "mutation_id":MUTATION["candidate_id"],
            "verification_state":MUTATION["verification_state"],
            "operation":MUTATION["operation"],
            "language":MUTATION["target"]["language"],
        },
        {
            "kind":"CHANGE_ATOM",
            "atom_id":atom["atom_id"],
            "verification_state":atom["verification_state"],
            "legal_effect":atom["claim"]["legal_effect"],
            "dimensions":atom["claim"]["dimensions"],
            "languages":atom["language_scope"]["languages"],
        },
    ]


def test_money_corrigendum_gold_case_validates():
    assert list(Draft202012Validator(SCHEMA).iter_errors(CASE)) == []


def test_money_corrigendum_facts_satisfy_gold_case():
    assert compare_expectations(
        CASE["machine_expectations"],
        emitted_facts(),
    ) == []


def test_gold_rejects_globalized_money_correction():
    false_fact={
        "kind":"CHANGE_ATOM",
        "claim_key":"REG2742_MONEY_CORRECTION_GLOBALIZED",
        "languages":["ENG","DEU","FRA"],
    }
    errors=compare_expectations(
        CASE["machine_expectations"],
        emitted_facts()+[false_fact],
    )
    assert errors == [
        "money.nonatom.globalized: forbidden fact was emitted"
    ]


def test_every_machine_expectation_has_human_assertion():
    human={
        assertion["assertion_id"]
        for bucket in CASE["expected"].values()
        for assertion in bucket
    }
    machine={
        expectation["assertion_id"]
        for expectation in CASE["machine_expectations"]
    }
    assert machine <= human
