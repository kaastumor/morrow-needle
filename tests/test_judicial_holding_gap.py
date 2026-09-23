import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker


GAP = json.loads(
    Path("fixtures/discovery/judicial-holding-gap-v0.1.json").read_text(
        encoding="utf-8"
    )
)
TEMPORAL = json.loads(
    Path("fixtures/temporal/test-achats-derogation-end-v0.2.json").read_text(
        encoding="utf-8"
    )
)
TEMPORAL_SCHEMA = json.loads(
    Path("schemas/temporal-assertion-v0.2.schema.json").read_text(
        encoding="utf-8"
    )
)
CHANGE_ATOM_SCHEMA = json.loads(
    Path("schemas/change-atom-v0.3.schema.json").read_text(encoding="utf-8")
)


def cases():
    return {item["case_id"]: item for item in GAP["cases"]}


def test_test_achats_preserves_text_state_validity_divergence():
    case = cases()["test-achats-c-236-09"]

    assert case["holding_character"] == "INVALIDITY"
    assert case["explicit_effect_date"] == "2012-12-21"
    assert case["current_text_state"]["article_5_2_still_printed"] is True
    assert case["functional_temporal_consequence"]["dimension"] == "DEROGATION"


def test_test_achats_temporal_consequence_fits_existing_temporal_v0_2():
    validator = Draft202012Validator(
        TEMPORAL_SCHEMA,
        format_checker=FormatChecker(),
    )
    errors = [
        error
        for assertion in TEMPORAL["assertions"]
        for error in validator.iter_errors(assertion)
    ]

    assert errors == []
    assertion = TEMPORAL["assertions"][0]
    assert assertion["dimension"] == "DEROGATION"
    assert assertion["boundary"] == "END"
    assert assertion["inclusive"] is False


def test_planet49_does_not_invent_judgment_date_as_application_start():
    case = cases()["planet49-c-673-17"]

    assert case["holding_character"] == "INTERPRETATION"
    assert case["explicit_effect_date"] is None
    assert "does not invent" in case["temporal_guardrail"]


def test_change_atom_cannot_own_judicial_holding_without_fake_mutation():
    source_mutations = CHANGE_ATOM_SCHEMA["properties"]["source_mutation_ids"]

    assert "source_mutation_ids" in CHANGE_ATOM_SCHEMA["required"]
    assert source_mutations["minItems"] == 1
    assert GAP["architecture_probe"]["change_atom_v0_3"]["fit"] == (
        "FAILS_CAUSAL_REQUIREMENT"
    )


def test_gap_is_direct_holding_ownership_not_temporal_failure():
    probe = GAP["architecture_probe"]

    assert probe["temporal_v0_2"]["fit"] == "CONSEQUENCE_ONLY"
    assert probe["authoritative_finding_v0_1"]["fit"] == (
        "SEMANTICALLY_WRONG_OWNER"
    )
    assert probe["result"] == "DIRECT_JUDICIAL_HOLDING_OWNER_MISSING"
    assert probe["provisional_missing_concept"] == "JUDICIAL_HOLDING"
    assert probe["new_schema_added_in_failure_commit"] is False
