import json
from pathlib import Path

from jsonschema import Draft202012Validator


OBS_SCHEMA = json.loads(
    Path("schemas/authoritative-metric-observation-v0.1.schema.json").read_text(
        encoding="utf-8"
    )
)
EVAL_SCHEMA = json.loads(
    Path("schemas/metric-rule-evaluation-v0.1.schema.json").read_text(
        encoding="utf-8"
    )
)

OBS_PATHS = [
    "fixtures/metrics/eu-ets-tnac-2025-v0.1.json",
    "fixtures/metrics/vehicle-co2-bugatti-distance-2022-v0.1.json",
    "fixtures/metrics/vehicle-co2-bugatti-registrations-2022-v0.1.json",
]
EVAL_PATHS = [
    "fixtures/metrics/eu-ets-tnac-reserve-evaluation-2025-v0.1.json",
    "fixtures/metrics/vehicle-co2-bugatti-premium-evaluation-2022-v0.1.json",
]

OBS = {
    item["observation_id"]: item
    for item in [
        json.loads(Path(path).read_text(encoding="utf-8"))
        for path in OBS_PATHS
    ]
}
EVALS = [
    json.loads(Path(path).read_text(encoding="utf-8"))
    for path in EVAL_PATHS
]


def test_all_metric_observations_are_schema_valid():
    for observation in OBS.values():
        assert list(
            Draft202012Validator(OBS_SCHEMA).iter_errors(observation)
        ) == []


def test_all_metric_evaluations_are_schema_valid():
    for evaluation in EVALS:
        assert list(
            Draft202012Validator(EVAL_SCHEMA).iter_errors(evaluation)
        ) == []


def test_all_metric_refs_resolve_to_direct_observations():
    for evaluation in EVALS:
        for observation_id in evaluation["metric_input_refs"]:
            assert observation_id in OBS
            assert OBS[observation_id]["evidence_state"] == "DIRECT"


def test_tnac_evaluation_recomputes_from_observation():
    evaluation = next(
        item for item in EVALS if "tnac:2025" in item["evaluation_id"]
    )
    tnac = OBS["metric:eu-ets:tnac:2025"]["metric"]["value"]

    assert 833_000_000 <= tnac <= 1_096_000_000
    assert evaluation["predicate"]["result"] is True
    assert tnac - 833_000_000 == evaluation["result"]["value"]
    assert evaluation["result"]["value"] == 190_494_202
    assert evaluation["result"]["official_corroboration_refs"]


def test_bugatti_evaluation_recomputes_from_two_observations():
    evaluation = next(
        item for item in EVALS if "bugatti:2022:premium" in item["evaluation_id"]
    )
    distance = OBS[
        "metric:vehicle-co2:bugatti:2022:distance-to-target"
    ]["metric"]["value"]
    registrations = OBS[
        "metric:vehicle-co2:bugatti:2022:registrations"
    ]["metric"]["value"]

    assert distance > 0
    assert evaluation["predicate"]["result"] is True
    assert round(distance * 95 * registrations, 2) == (
        evaluation["result"]["value"]
    )
    assert evaluation["result"]["value"] == 341_046.96


def test_bugatti_exact_money_result_is_derived_not_directly_corroborated():
    evaluation = next(
        item for item in EVALS if "bugatti:2022:premium" in item["evaluation_id"]
    )

    assert evaluation["result"]["derivation_state"] == "DERIVED"
    assert evaluation["result"]["official_corroboration_refs"] == []


def test_observation_does_not_own_evaluation_result():
    for observation in OBS.values():
        encoded = json.dumps(observation, sort_keys=True)
        assert "formula_text" not in encoded
        assert "derived_result" not in encoded
        assert "owns_temporal_application" not in encoded


def test_evaluation_does_not_copy_metric_values_as_metric_truth():
    for evaluation in EVALS:
        metric_inputs = [
            item
            for item in evaluation["calculation"]["inputs"]
            if item["source_kind"] == "METRIC_OBSERVATION"
        ]
        assert metric_inputs
        for item in metric_inputs:
            assert "value" not in item
            assert item["metric_observation_id"] in OBS


def test_evaluation_refuses_temporal_ownership():
    for evaluation in EVALS:
        assert evaluation["owns_temporal_application"] is False
        assert evaluation["evidence_state"] == "DERIVED"


def test_contract_does_not_embed_executable_expression_language():
    encoded = json.dumps(EVAL_SCHEMA, sort_keys=True).casefold()

    assert '"code"' not in encoded
    assert "expression_ast" not in encoded
    assert "eval(" not in encoded
    assert EVAL_SCHEMA["properties"]["evaluation_method"]["const"] == (
        "PINNED_DETERMINISTIC_ARITHMETIC"
    )
