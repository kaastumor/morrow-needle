import json
from pathlib import Path

from jsonschema import Draft202012Validator

from needle.analytics.dependency_ripple import emit_dependency_ripple_facts
from needle.gold import compare_expectations


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


CASE=load("fixtures/gold/dependency-ripple-first-cohort-v0.1.json")
SCHEMA=load("schemas/gold-corpus-case-v0.2.schema.json")
COMPOSITION=load(
    "fixtures/analytics/dependency-ripple-first-cohort-v0.1.json"
)


def facts():
    return emit_dependency_ripple_facts(COMPOSITION)


def test_dependency_ripple_gold_case_validates():
    assert list(Draft202012Validator(SCHEMA).iter_errors(CASE)) == []


def test_dependency_ripple_view_satisfies_gold_expectations():
    assert compare_expectations(CASE["machine_expectations"],facts()) == []


def test_gold_rejects_manufactured_local_mutation():
    false_fact={
        "kind":"DEPENDENCY_RIPPLE",
        "case_id":"reach-art67-annex17-entry78-ripple",
        "local_textual_mutation":True,
    }
    errors=compare_expectations(
        CASE["machine_expectations"],
        facts()+[false_fact],
    )
    assert "xray.no-local-mutation: forbidden fact was emitted" in errors


def test_gold_rejects_direct_reclassification_of_derived_ripple():
    false_fact={
        "kind":"DEPENDENCY_RIPPLE",
        "case_id":"reach-art67-annex17-entry78-ripple",
        "derived_effect":{"evidence_state":"DIRECT"},
    }
    errors=compare_expectations(
        CASE["machine_expectations"],
        facts()+[false_fact],
    )
    assert "xray.no-direct-ripple: forbidden fact was emitted" in errors
