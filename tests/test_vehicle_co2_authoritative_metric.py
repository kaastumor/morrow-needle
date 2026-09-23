import json
from pathlib import Path


FIXTURE = json.loads(
    Path(
        "fixtures/discovery/"
        "vehicle-co2-bugatti-authoritative-metric-v0.1.json"
    ).read_text(encoding="utf-8")
)


def metrics_by_name():
    return {
        item["metric_name"]: item
        for item in FIXTURE["official_metric_observation"]["metrics"]
    }


def test_bugatti_official_metrics_pin_positive_distance():
    metrics = metrics_by_name()

    assert metrics["number of newly registered passenger cars"]["value"] == 8
    assert metrics["average specific emissions of CO2"]["value"] == 561.375
    assert metrics["specific emissions target"]["value"] == 112.629
    assert metrics["distance to target"]["value"] == 448.746
    assert metrics["distance to target"]["value"] > 0


def test_distance_to_target_matches_official_component_values():
    metrics = metrics_by_name()
    average = metrics["average specific emissions of CO2"]["value"]
    target = metrics["specific emissions target"]["value"]
    distance = metrics["distance to target"]["value"]

    assert round(average - target, 3) == distance


def test_binding_formula_yields_pinned_derived_amount():
    inputs = FIXTURE["rule_evaluation"]["inputs"]
    result = (
        inputs["distance_to_target"]
        * inputs["eur_per_g_km"]
        * inputs["registrations"]
    )

    assert round(result, 2) == 341_046.96
    assert round(result, 2) == FIXTURE["rule_evaluation"]["derived_result"][
        "value"
    ]
    assert FIXTURE["rule_evaluation"]["derived_result"]["evidence_state"] == (
        "DERIVED_FROM_OFFICIAL_METRICS_AND_BINDING_FORMULA"
    )


def test_metric_observation_and_evaluation_are_not_collapsed():
    observation = FIXTURE["official_metric_observation"]
    evaluation = FIXTURE["rule_evaluation"]

    assert "derived_result" not in observation
    assert evaluation["predicate_result"] is True
    assert FIXTURE["architecture_probe"]["required_direct_object"] == (
        "AUTHORITATIVE_METRIC_OBSERVATION"
    )
    assert FIXTURE["architecture_probe"]["required_derived_object"] == (
        "METRIC_RULE_EVALUATION"
    )


def test_second_case_is_cross_domain_confirmation_not_set_membership():
    comparison = FIXTURE["comparison_to_tnac"]
    probe = FIXTURE["architecture_probe"]

    assert comparison["result"] == (
        "AUTHORITATIVE_METRIC_PATTERN_CONFIRMED_ACROSS_DOMAINS"
    )
    assert probe["dynamic_set_fit"] == "FAILS_CAUSAL_SHAPE"
    assert probe["decision"] == (
        "TWO_ORTHOGONAL_CASES_NOW_JUSTIFY_A_NARROW_METRIC_CAUSAL_CONTRACT"
    )


def test_no_textual_mutation_is_manufactured():
    assert FIXTURE["governing_rule"]["textual_mutation_at_metric_event"] is None
