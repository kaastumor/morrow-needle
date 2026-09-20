import json
from pathlib import Path

from jsonschema import Draft202012Validator

from needle.gold import compare_expectations
from needle.thread.composer import emit_thread_facts


SCHEMA = json.loads(
    Path("schemas/gold-corpus-case-v0.2.schema.json").read_text(encoding="utf-8")
)
CASE = json.loads(
    Path("fixtures/gold/reg794-article3-thread-v0.1.json").read_text(
        encoding="utf-8"
    )
)
THREAD = json.loads(
    Path("fixtures/thread/reg794-article3-thread-v0.1.json").read_text(
        encoding="utf-8"
    )
)


def facts():
    return emit_thread_facts(THREAD)


def test_thread_gold_case_validates_against_v02_schema():
    assert list(Draft202012Validator(SCHEMA).iter_errors(CASE)) == []


def test_article3_thread_satisfies_gold_expectations():
    assert compare_expectations(CASE["machine_expectations"], facts()) == []


def test_gold_rejects_false_2025_paragraph4_textual_mutation():
    false_fact = {
        "kind":"THREAD_REF",
        "event_id":"paragraph4-cross-reference-ripple-2025",
        "event_kind":"DERIVED_SEMANTIC_EFFECT",
        "ref_kind":"MUTATION",
        "entity_id":"false-article3-p4-2025-mutation",
        "source_key":"mutation_2025",
        "entity":{},
    }
    errors = compare_expectations(
        CASE["machine_expectations"],
        facts() + [false_fact],
    )
    assert "nonmutation.p4-2025: forbidden fact was emitted" in errors


def test_gold_rejects_false_corrigendum_thread_mutation():
    false_fact = {
        "kind":"THREAD_REF",
        "event_id":"corrigendum-review-2026",
        "event_kind":"RELATED_SOURCE_NON_IMPACT",
        "ref_kind":"MUTATION",
        "entity_id":"false-corrigendum-article3-mutation",
        "source_key":"corrigendum_scope",
        "entity":{},
    }
    errors = compare_expectations(
        CASE["machine_expectations"],
        facts() + [false_fact],
    )
    assert "nonmutation.corrigendum-2026: forbidden fact was emitted" in errors


def test_gold_rejects_copying_sani_date_to_pki_atom():
    contaminated = []
    for fact in facts():
        if (
            fact.get("kind") == "THREAD_REF"
            and fact.get("entity_id") == "reg794-art3-pki-correspondence-duty-v0.1"
        ):
            fact = {
                **fact,
                "entity":{
                    **fact["entity"],
                    "temporal_assertion_refs":[
                        "reg794-art3-p3-sani-application-start"
                    ],
                },
            }
        contaminated.append(fact)

    errors = compare_expectations(
        CASE["machine_expectations"],
        contaminated,
    )
    assert "nonatom.pki-sani-temporal: forbidden fact was emitted" in errors
