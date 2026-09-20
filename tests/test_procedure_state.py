import json
from pathlib import Path

from jsonschema import Draft202012Validator

from needle.procedure.resolver import assert_no_collapsed_status, state_as_of


SCHEMA = json.loads(
    Path("schemas/procedure-state-event-v0.1.schema.json").read_text(encoding="utf-8")
)
FIXTURE = json.loads(
    Path("fixtures/procedure/procedure-state-adversaries-v0.1.json").read_text(encoding="utf-8")
)


def _case(case_id):
    return next(case for case in FIXTURE["cases"] if case["case_id"] == case_id)


def test_all_procedure_events_validate():
    validator = Draft202012Validator(SCHEMA)
    errors = []
    for case in FIXTURE["cases"]:
        for event in case["events"]:
            errors.extend(
                f"{case['case_id']} / {event['event_id']}: {error.message}"
                for error in validator.iter_errors(event)
            )
    assert errors == []


def test_snapshots_preserve_orthogonal_dimensions():
    for case in FIXTURE["cases"]:
        for snapshot in case["snapshots"]:
            result = state_as_of(
                case["events"],
                procedure_id=case["procedure_id"],
                on_date=snapshot["date"],
            )
            assert result["state"] == "RESOLVED", (case["case_id"], snapshot["date"])
            assert_no_collapsed_status(result)
            for dimension, expected in snapshot["expect"].items():
                assert result["dimensions"][dimension] == expected, (
                    case["case_id"], snapshot["date"], dimension
                )


def test_delegated_act_can_be_adopted_while_scrutiny_open_and_unpublished():
    case = _case("esrs-delegated-act")
    result = state_as_of(
        case["events"],
        procedure_id=case["procedure_id"],
        on_date="2023-08-15",
    )
    d = result["dimensions"]
    assert d["FORMAL_ACT_ADOPTION"] == "ADOPTED"
    assert d["DELEGATED_SCRUTINY"] == "OPEN"
    assert d["FINAL_ACT_PUBLICATION"] == "NOT_PUBLISHED"
    assert d["PROCEDURE_OUTCOME"] == "PENDING"


def test_withdrawn_is_terminal_not_pending():
    case = _case("european-private-company-withdrawn")
    result = state_as_of(
        case["events"],
        procedure_id=case["procedure_id"],
        on_date="2014-05-22",
    )
    d = result["dimensions"]
    assert d["PROCEDURE_ACTIVITY"] == "CLOSED"
    assert d["PROCEDURE_OUTCOME"] == "WITHDRAWN"
    assert d["FORMAL_ACT_ADOPTION"] == "NOT_ADOPTED"


def test_ordinary_legislative_positions_do_not_equal_final_adoption():
    case = _case("gdpr-ordinary-legislative")
    result = state_as_of(
        case["events"],
        procedure_id=case["procedure_id"],
        on_date="2016-04-15",
    )
    d = result["dimensions"]
    assert d["PARLIAMENT_POSITION"] == "SECOND_READING_POSITION_ADOPTED"
    assert d["COUNCIL_POSITION"] == "POSITION_ADOPTED"
    assert d["FORMAL_ACT_ADOPTION"] == "NOT_ADOPTED"
    assert d["FINAL_ACT_PUBLICATION"] == "NOT_PUBLISHED"


def test_implementing_act_does_not_invent_legislative_positions():
    case = _case("implementing-regulation-2023-2773")
    result = state_as_of(
        case["events"],
        procedure_id=case["procedure_id"],
        on_date="2023-12-14",
    )
    d = result["dimensions"]
    assert result["procedure_family"] == "IMPLEMENTING_ACT"
    assert d["PARLIAMENT_POSITION"] == "NONE"
    assert d["COUNCIL_POSITION"] == "NONE"
    assert d["FORMAL_ACT_ADOPTION"] == "ADOPTED"
    assert d["FINAL_ACT_PUBLICATION"] == "PUBLISHED"


def test_provisional_political_agreement_is_not_formal_adoption():
    case = _case("dsa-provisional-agreement-vs-adoption")
    result = state_as_of(
        case["events"],
        procedure_id=case["procedure_id"],
        on_date="2022-04-24",
    )
    d = result["dimensions"]
    assert d["NEGOTIATION_STATE"] == "PROVISIONAL_POLITICAL_AGREEMENT"
    assert d["PROCEDURE_OUTCOME"] == "PENDING"
    assert d["FORMAL_ACT_ADOPTION"] == "NOT_ADOPTED"
    assert d["FINAL_ACT_PUBLICATION"] == "NOT_PUBLISHED"


def test_procedure_schema_rejects_cross_dimension_and_legal_effect_leakage():
    validator = Draft202012Validator(SCHEMA)
    base = _case("gdpr-ordinary-legislative")["events"][0]

    bad_publication = {
        **base,
        "event_id":"bad-publication",
        "effects":[{"dimension":"FINAL_ACT_PUBLICATION","value":"ADOPTED"}],
    }
    assert list(validator.iter_errors(bad_publication))

    bad_legal_effect = {
        **base,
        "event_id":"bad-legal-effect",
        "effects":[{"dimension":"APPLICATION","value":"APPLICABLE"}],
    }
    assert list(validator.iter_errors(bad_legal_effect))
