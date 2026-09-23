import json
from pathlib import Path

from jsonschema import Draft202012Validator

from needle.temporal.resolver import status_on


DYNAMIC_SCHEMA = json.loads(
    Path("schemas/authoritative-dynamic-set-v0.1.schema.json").read_text(
        encoding="utf-8"
    )
)
TEMPORAL_SCHEMA = json.loads(
    Path("schemas/temporal-assertion-v0.1.schema.json").read_text(
        encoding="utf-8"
    )
)
DYNAMIC = json.loads(
    Path(
        "fixtures/dependency/dsa-vlop-vlose-authoritative-dynamic-set-v0.1.json"
    ).read_text(encoding="utf-8")
)
TEMPORAL = json.loads(
    Path(
        "fixtures/temporal/dsa-stripchat-designation-application-lag-v0.1.json"
    ).read_text(encoding="utf-8")
)


def test_dsa_dynamic_set_fixture_fits_existing_contract():
    assert list(
        Draft202012Validator(DYNAMIC_SCHEMA).iter_errors(DYNAMIC)
    ) == []


def test_temporal_assertions_fit_existing_contract():
    errors = [
        error
        for assertion in TEMPORAL["assertions"]
        for error in Draft202012Validator(TEMPORAL_SCHEMA).iter_errors(
            assertion
        )
    ]
    assert errors == []


def test_designation_and_application_start_are_distinct():
    designation = DYNAMIC["transitions"][0]
    assertions = TEMPORAL["assertions"]

    assert designation["operation"] == "ADD_MEMBER"
    assert designation["effective_from"] == "2023-12-20"

    before = status_on(
        assertions,
        dimension="APPLICATION",
        subject_keys={"service:stripchat:section5-obligations"},
        on_date="2024-01-15",
        context={"events": TEMPORAL["event_context"]},
    )
    start = status_on(
        assertions,
        dimension="APPLICATION",
        subject_keys={"service:stripchat:section5-obligations"},
        on_date="2024-04-21",
        context={"events": TEMPORAL["event_context"]},
    )

    assert before["state"] == "RESOLVED"
    assert before["active"] is False
    assert start["active"] is True


def test_termination_and_application_end_are_distinct():
    termination = DYNAMIC["transitions"][1]
    assertions = TEMPORAL["assertions"]

    assert termination["operation"] == "REMOVE_MEMBER"
    assert termination["effective_from"] == "2025-05-27"
    assert termination["after"]["membership"] == "NOT_INCLUDED"

    tail = status_on(
        assertions,
        dimension="APPLICATION",
        subject_keys={"service:stripchat:section5-obligations"},
        on_date="2025-06-01",
        context={"events": TEMPORAL["event_context"]},
    )
    ended = status_on(
        assertions,
        dimension="APPLICATION",
        subject_keys={"service:stripchat:section5-obligations"},
        on_date="2025-09-27",
        context={"events": TEMPORAL["event_context"]},
    )

    assert tail["state"] == "RESOLVED"
    assert tail["active"] is True
    assert ended["active"] is False


def test_exclusive_end_boundary_prevents_one_day_overhang():
    result = status_on(
        TEMPORAL["assertions"],
        dimension="APPLICATION",
        subject_keys={"service:stripchat:section5-obligations"},
        on_date="2025-09-27",
        context={"events": TEMPORAL["event_context"]},
    )

    assert result["end"]["date"] == "2025-09-27"
    assert result["end"]["inclusive"] is False
    assert result["active"] is False


def test_set_state_never_claims_to_own_application_date():
    encoded = json.dumps(DYNAMIC, sort_keys=True)

    assert "application_start" not in encoded
    assert "application_end" not in encoded
    assert "2024-04-21" not in encoded
    assert "2025-09-27" not in encoded
    assert "application date" in encoded.casefold()


def test_temporal_fixture_never_rewrites_set_transition_dates():
    encoded = json.dumps(TEMPORAL, sort_keys=True)

    assert "2023-12-20" in encoded
    assert "2025-05-27" in encoded
    assert TEMPORAL["expected_windows"][0]["through"] == "2024-04-20"
    assert TEMPORAL["expected_windows"][1]["through"] == "2025-09-26"


def test_dynamic_set_contract_survives_without_schema_widening():
    dependency = DYNAMIC["dependencies"][0]

    assert dependency["relation_character"] == (
        "LEGAL_EFFECT_CONDITIONED_ON_AUTHORITATIVE_SET_STATE"
    )
    assert "four months" in dependency["condition_statement"].casefold()
    assert "not itself the application boundary" in (
        dependency["condition_statement"].casefold()
    )
