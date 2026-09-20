import json
from pathlib import Path

from jsonschema import Draft202012Validator

from needle.temporal.resolver import gap_between, resolve_boundary, status_on


SCHEMA = json.loads(
    Path("schemas/temporal-assertion-v0.1.schema.json").read_text(encoding="utf-8")
)
FIXTURE = json.loads(
    Path("fixtures/temporal/temporal-adversaries-v0.1.json").read_text(encoding="utf-8")
)


def _case(case_id):
    return next(case for case in FIXTURE["cases"] if case["case_id"] == case_id)


def test_all_temporal_assertions_validate():
    validator = Draft202012Validator(SCHEMA)
    errors = []
    for case in FIXTURE["cases"]:
        for assertion in case["assertions"]:
            for error in validator.iter_errors(assertion):
                errors.append(
                    f"{case['case_id']} / {assertion['assertion_id']}: {error.message}"
                )
    assert errors == []


def test_fixture_queries_resolve_without_collapsing_dimensions():
    for case in FIXTURE["cases"]:
        for query in case.get("queries", []):
            result = status_on(
                case["assertions"],
                dimension=query["dimension"],
                subject_keys=set(query["subject_keys"]),
                on_date=query["date"],
                context=query.get("context", {}),
            )
            expected = query["expected"]
            assert result["state"] == expected["state"], query["query_id"]
            assert result["active"] == expected["active"], query["query_id"]
            if "start" in expected:
                assert result["start"]["date"] == expected["start"], query["query_id"]


def test_dsa_context_required_is_not_silently_replaced_by_default():
    case = _case("dsa-scoped-and-entity-relative-application")
    result = resolve_boundary(
        case["assertions"],
        dimension="APPLICATION",
        boundary="START",
        subject_keys={"ACT:32022R2065", "ENTITY_SCOPE:32022R2065"},
        context={"entity":{"designation_class":"VLOP"}},
    )
    assert result["state"] == "CONTEXT_REQUIRED"
    assert result["date"] is None
    assert result["fallbacks"] == [
        {"assertion_id":"dsa-application-default","date":"2024-02-17"}
    ]
    assert result["missing"] == [
        {
            "assertion_id":"dsa-application-designated-provider",
            "missing":"article33_6_notification_date",
        }
    ]


def test_2025_905_text_state_can_precede_application():
    case = _case("reg2025-905-text-state-vs-application")
    keys = {
        "MUTATION_BATCH:32025R0905",
        "TARGET:32004R0794:ANNEX_I_PART_I_6.8",
    }
    text_state = status_on(
        case["assertions"],
        dimension="TEXT_STATE",
        subject_keys=keys,
        on_date="2025-07-20",
    )
    application = status_on(
        case["assertions"],
        dimension="APPLICATION",
        subject_keys=keys,
        on_date="2025-07-20",
    )
    assert text_state["active"] is True
    assert application["active"] is False
    assert application["start"]["date"] == "2025-08-13"


def test_genealogical_successor_does_not_erase_real_application_gap():
    case = _case("temporary-regime-real-gap")
    by_id = {a["assertion_id"]: a for a in case["assertions"]}
    query = case["gap_query"]
    previous = by_id[query["previous_end_assertion_id"]]["normalized_date"]
    following = by_id[query["next_start_assertion_id"]]["normalized_date"]
    result = gap_between(previous, following)
    assert result == query["expected"]
