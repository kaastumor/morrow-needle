import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

from needle.temporal.resolver_v0_2 import status_at


FIXTURE = json.loads(
    Path("fixtures/value-gates/issue86-core-probes-v0.1.json").read_text(
        encoding="utf-8"
    )
)
TEMPORAL_SCHEMA = json.loads(
    Path("schemas/temporal-assertion-v0.2.schema.json").read_text(
        encoding="utf-8"
    )
)
LANGUAGE_SCHEMA = json.loads(
    Path("schemas/language-scoped-mutation-v0.1.schema.json").read_text(
        encoding="utf-8"
    )
)
JUDICIAL_SCHEMA = json.loads(
    Path("schemas/judicial-holding-v0.1.schema.json").read_text(
        encoding="utf-8"
    )
)


def validate(schema, document):
    return list(
        Draft202012Validator(
            schema,
            format_checker=FormatChecker(),
        ).iter_errors(document)
    )


def test_common_charger_temporal_assertions_validate():
    assertions = FIXTURE["common_charger"]["assertions"]
    assert all(validate(TEMPORAL_SCHEMA, item) == [] for item in assertions)


def test_common_charger_core_answers_repeated_date_scope_queries():
    data = FIXTURE["common_charger"]

    for query in data["queries"]:
        result = status_at(
            data["assertions"],
            dimension="APPLICATION",
            subject_keys={query["subject_key"]},
            precision="DATE",
            at_value=query["date"],
        )
        assert result["state"] == "RESOLVED", query["query_id"]
        assert result["active"] is query["expected_active"], query["query_id"]


def test_dutch_ai_corrigendum_fits_existing_language_scoped_contract():
    mutation = FIXTURE["dutch_ai_act_corrigendum"]

    assert validate(LANGUAGE_SCHEMA, mutation) == []
    assert mutation["expression_scope"]["languages"] == ["NLD"]
    assert mutation["expression_scope"]["nonlisted_semantics"] == "NO_ASSERTION"
    operation = mutation["operations"][0]
    assert "vallen onder het toepassingsgebied" in operation["before_text"]
    assert "vallen niet onder het toepassingsgebied" in operation["after_text"]


def test_schrems_privacy_shield_invalidity_fits_judicial_v0_1():
    holding = FIXTURE["schrems_ii"]["privacy_shield_invalidity"]

    assert validate(JUDICIAL_SCHEMA, holding) == []
    assert holding["holding_type"] == "INVALIDITY"


def test_schrems_positive_validity_exposes_real_judicial_v0_1_gap():
    holding = FIXTURE["schrems_ii"]["scc_positive_validity_candidate"]
    errors = validate(JUDICIAL_SCHEMA, holding)

    assert holding["holding_type"] == "VALIDITY"
    assert errors
    assert "VALIDITY" not in JUDICIAL_SCHEMA["properties"]["holding_type"]["enum"]


def test_gate_does_not_patch_judicial_schema_to_make_core_win():
    allowed = JUDICIAL_SCHEMA["properties"]["holding_type"]["enum"]

    assert allowed == ["INVALIDITY", "INTERPRETATION"]
