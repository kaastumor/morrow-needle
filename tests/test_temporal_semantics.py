import json
from pathlib import Path

from jsonschema import Draft202012Validator

from needle.temporal.resolver import (
    gap_between,
    resolve_boundary,
    status_on,
    status_on_perspective,
)


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


def test_retroactive_application_can_precede_entry_into_force_ex_post():
    case = _case("reg2023-2773-retroactive-application")
    application = status_on(
        case["assertions"],
        dimension="APPLICATION",
        subject_keys={"ACT:32023R2773"},
        on_date="2023-06-01",
    )
    legal_force = status_on(
        case["assertions"],
        dimension="LEGAL_FORCE",
        subject_keys={"ACT:32023R2773"},
        on_date="2023-06-01",
    )
    assert application["active"] is True
    assert legal_force["active"] is False
    # This deliberately exposes the need for query perspective: ex-post legal
    # effect is not the same question as what was enacted/knowable in June 2023.


def test_retroactive_effect_differs_by_official_source_perspective():
    case = _case("reg2023-2773-retroactive-application")
    for query in case["perspective_queries"]:
        result = status_on_perspective(
            case["assertions"],
            dimension=query["dimension"],
            subject_keys=set(query["subject_keys"]),
            valid_date=query["valid_date"],
            perspective=query["perspective"],
            source_cutoff_date=query.get("source_cutoff_date"),
            context=query.get("context", {}),
        )
        expected = query["expected"]
        assert result["state"] == expected["state"], query["query_id"]
        assert result["active"] == expected["active"], query["query_id"]


def test_official_source_perspective_is_not_claimed_human_knowledge():
    case = _case("reg2023-2773-retroactive-application")
    result = status_on_perspective(
        case["assertions"],
        dimension="APPLICATION",
        subject_keys={"ACT:32023R2773"},
        valid_date="2023-06-01",
        perspective="OFFICIAL_SOURCE_STATE_AS_OF",
        source_cutoff_date="2023-06-01",
    )
    assert result["state"] == "NOT_ASSERTED_AS_OF_SOURCE_DATE"
    assert result["active"] is None
    assert result["later_assertions"][0]["assertion_id"] == "r2773-application-start"
    assert result["later_assertions"][0]["official_source_available_from"] == "2023-12-14"


def test_transition_regime_can_overlap_new_regulation_and_end_in_layers():
    case = _case("mdr-overlapping-transition-and-partial-end")

    new_law = status_on(
        case["assertions"],
        dimension="APPLICATION",
        subject_keys={"ACT:32017R0745"},
        on_date="2022-01-01",
    )
    legacy_transition = status_on(
        case["assertions"],
        dimension="TRANSITION",
        subject_keys={"REGIME:MDR_LEGACY_DIRECTIVE_CONTINUITY"},
        on_date="2022-01-01",
    )
    assert new_law["active"] is True
    assert legacy_transition["active"] is True

    narrow_derogation = status_on(
        case["assertions"],
        dimension="DEROGATION",
        subject_keys={"REGIME:MDR_ART120_3_PLACEMENT_DEROGATION"},
        on_date="2024-06-01",
    )
    broad_transition = status_on(
        case["assertions"],
        dimension="TRANSITION",
        subject_keys={"REGIME:MDR_LEGACY_DIRECTIVE_CONTINUITY"},
        on_date="2024-06-01",
    )
    assert narrow_derogation["active"] is False
    assert broad_transition["active"] is True
