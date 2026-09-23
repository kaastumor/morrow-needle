import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker


SCHEMA = json.loads(
    Path("schemas/judicial-holding-v0.1.schema.json").read_text(
        encoding="utf-8"
    )
)
TEST_ACHATS = json.loads(
    Path("fixtures/judicial/test-achats-c236-09-v0.1.json").read_text(
        encoding="utf-8"
    )
)
PLANET49 = json.loads(
    Path("fixtures/judicial/planet49-c673-17-v0.1.json").read_text(
        encoding="utf-8"
    )
)
TEMPORAL = json.loads(
    Path("fixtures/temporal/test-achats-derogation-end-v0.2.json").read_text(
        encoding="utf-8"
    )
)


def validate(document):
    return list(
        Draft202012Validator(
            SCHEMA,
            format_checker=FormatChecker(),
        ).iter_errors(document)
    )


def test_invalidity_and_interpretation_fit_same_narrow_contract():
    assert validate(TEST_ACHATS) == []
    assert validate(PLANET49) == []
    assert TEST_ACHATS["holding_type"] == "INVALIDITY"
    assert PLANET49["holding_type"] == "INTERPRETATION"


def test_test_achats_references_existing_temporal_consequence():
    refs = TEST_ACHATS["temporal_relation"]["temporal_assertion_refs"]
    assertion_ids = {
        item["assertion_id"]
        for item in TEMPORAL["assertions"]
    }

    assert TEST_ACHATS["temporal_relation"]["character"] == (
        "EXPLICIT_TEMPORAL_CONSEQUENCE"
    )
    assert refs == ["test-achats-art5-2-derogation-end"]
    assert set(refs).issubset(assertion_ids)


def test_planet49_forbids_fabricated_valid_time_boundary():
    relation = PLANET49["temporal_relation"]

    assert relation["character"] == "NO_NEW_VALID_TIME_BOUNDARY_ASSERTED"
    assert relation["temporal_assertion_refs"] == []


def test_schema_rejects_temporal_ref_on_no_boundary_holding():
    bad = json.loads(json.dumps(PLANET49))
    bad["temporal_relation"]["temporal_assertion_refs"] = ["fake-start"]

    assert validate(bad)


def test_schema_requires_temporal_ref_when_explicit_consequence_exists():
    bad = json.loads(json.dumps(TEST_ACHATS))
    bad["temporal_relation"]["temporal_assertion_refs"] = []

    assert validate(bad)


def test_holding_does_not_absorb_mutation_or_factual_finding_contracts():
    for document in (TEST_ACHATS, PLANET49):
        encoded = json.dumps(document, sort_keys=True)

        assert "source_mutation_ids" not in encoded
        assert "finding_type" not in encoded
        assert "metric" not in encoded


def test_contract_is_not_case_law_graph_or_precedent_engine():
    encoded = json.dumps(SCHEMA, sort_keys=True).casefold()

    for forbidden in (
        "precedent_weight",
        "citation_graph",
        "court_hierarchy",
        "importance_score",
        "ratio_decidendi_model",
    ):
        assert forbidden not in encoded
