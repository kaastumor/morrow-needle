import json
from pathlib import Path

from jsonschema import Draft202012Validator

from needle.temporal.resolver import resolve_boundary, status_on


TEMPORAL_SCHEMA = json.loads(
    Path("schemas/temporal-assertion-v0.1.schema.json").read_text(encoding="utf-8")
)
ORIGINAL_TEMPORAL = json.loads(
    Path("fixtures/temporal/reg794-article3-original-v0.1.json").read_text(
        encoding="utf-8"
    )
)
P4_CONTINUITY = json.loads(
    Path("fixtures/thread/reg794-article3-p4-continuity-v0.1.json").read_text(
        encoding="utf-8"
    )
)
CORRIGENDUM_SCOPE = json.loads(
    Path("fixtures/thread/reg794-article3-corrigendum-scope-v0.1.json").read_text(
        encoding="utf-8"
    )
)
SEMANTIC_2008 = json.loads(
    Path("fixtures/semantic/reg794-article3-atoms-v0.1.json").read_text(
        encoding="utf-8"
    )
)
SEMANTIC_2025 = json.loads(
    Path("fixtures/semantic/reg794-article3-2025-atoms-v0.1.json").read_text(
        encoding="utf-8"
    )
)


def test_original_article3_temporal_assertions_validate():
    validator = Draft202012Validator(TEMPORAL_SCHEMA)
    errors = []
    for assertion in ORIGINAL_TEMPORAL["assertions"]:
        errors.extend(
            f"{assertion['assertion_id']}: {error.message}"
            for error in validator.iter_errors(assertion)
        )
    assert errors == []


def test_chapter2_more_than_five_month_gate_is_exclusive():
    assertions = ORIGINAL_TEMPORAL["assertions"]
    on_boundary = status_on(
        assertions,
        dimension="APPLICATION",
        subject_keys={"REGIME:32004R0794:CHAPTER_II"},
        on_date="2004-10-20",
    )
    first_day_after = status_on(
        assertions,
        dimension="APPLICATION",
        subject_keys={"REGIME:32004R0794:CHAPTER_II"},
        on_date="2004-10-21",
    )
    assert on_boundary["start"]["date"] == "2004-10-20"
    assert on_boundary["start"]["inclusive"] is False
    assert on_boundary["active"] is False
    assert first_day_after["active"] is True


def test_original_correspondence_rule_requires_notification_date_context():
    assertions = ORIGINAL_TEMPORAL["assertions"]
    keys = {"RULE:32004R0794:ARTICLE3_4:ELECTRONIC_CORRESPONDENCE"}

    missing = resolve_boundary(
        assertions,
        dimension="APPLICATION",
        boundary="START",
        subject_keys=keys,
    )
    assert missing["state"] == "CONTEXT_REQUIRED"
    assert missing["missing"] == [{
        "assertion_id":"reg794-art3-original-electronic-correspondence-trigger",
        "missing":"notification_submission_date",
    }]

    excluded = resolve_boundary(
        assertions,
        dimension="APPLICATION",
        boundary="START",
        subject_keys=keys,
        context={"events":{"notification_submission_date":"2006-01-01"}},
    )
    assert excluded["state"] == "NOT_ASSERTED"

    included = resolve_boundary(
        assertions,
        dimension="APPLICATION",
        boundary="START",
        subject_keys=keys,
        context={"events":{"notification_submission_date":"2006-01-02"}},
    )
    assert included["state"] == "RESOLVED"
    assert included["date"] == "2006-01-02"


def test_2025_paragraph4_is_a_negative_textual_mutation_regression():
    p4 = P4_CONTINUITY["paragraph4"]
    assert p4["before"]["text_hash"] == p4["after"]["text_hash"]
    assert p4["textual_mutation"] is None
    assert P4_CONTINUITY["semantic_result"]["character"] == (
        "DERIVED_CROSS_REFERENCE_RIPPLE_ONLY"
    )


def test_paragraph4_sentence_hashes_reuse_canonical_2008_semantic_evidence():
    registry = SEMANTIC_2008["source_span_registry"]
    checks = P4_CONTINUITY["sentence_checks"]
    assert checks["alt-channel-permission"]["text_hash"] == (
        registry["span-alt-channel-permission"]["text_hash"]
    )
    assert checks["invalid-channel-status"]["text_hash"] == (
        registry["span-invalid-channel-status"]["text_hash"]
    )


def test_derived_2025_crossref_atom_does_not_claim_direct_paragraph4_change():
    ripple = next(
        atom for atom in SEMANTIC_2025["atoms"]
        if atom["atom_id"] == "reg794-art3-2025-crossref-exception-ripple-v0.1"
    )
    assert ripple["verification_state"] == "EVIDENCED"
    assert ripple["evidence_state"] == "DERIVED"
    assert ripple["provision_refs"][0]["citation_path"] == "Article 3 > 4"


def test_2026_corrigendum_is_retained_but_not_a_thread_mutation():
    assert CORRIGENDUM_SCOPE["thread_scope_result"] == {
        "article3_affected":False,
        "classification":"NO_THREAD_MUTATION",
        "rationale":(
            "The corrigendum explicitly targets the amendment of Article 4(1), "
            "not Article 3. It is relevant provenance for the 2025 amending act "
            "but does not create an Article 3 text state, mutation, Change Atom, "
            "or rule-lineage event."
        ),
    }
    assert CORRIGENDUM_SCOPE["thread_handling"]["retain_as"] == (
        "RELATED_SOURCE_NON_IMPACT"
    )
