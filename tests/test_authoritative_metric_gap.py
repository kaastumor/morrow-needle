import json
from pathlib import Path


FIXTURE = json.loads(
    Path(
        "fixtures/discovery/eu-ets-tnac-authoritative-metric-v0.1.json"
    ).read_text(encoding="utf-8")
)
SOURCE_SCHEMA = json.loads(
    Path("schemas/source-observation-v0.1.schema.json").read_text(
        encoding="utf-8"
    )
)
SET_SCHEMA = json.loads(
    Path("schemas/authoritative-dynamic-set-v0.1.schema.json").read_text(
        encoding="utf-8"
    )
)
TEMPORAL_SCHEMA = json.loads(
    Path("schemas/temporal-assertion-v0.1.schema.json").read_text(
        encoding="utf-8"
    )
)
CHANGE_ATOM_SCHEMA = json.loads(
    Path("schemas/change-atom-v0.3.schema.json").read_text(encoding="utf-8")
)


def test_official_tnac_arithmetic_matches_official_result():
    evaluation = FIXTURE["rule_evaluation"]
    tnac = evaluation["inputs"]["TNAC"]
    lower = evaluation["inputs"]["lower_reference"]

    assert 833_000_000 <= tnac <= 1_096_000_000
    assert tnac - lower == 190_494_202
    assert evaluation["computed_result"] == evaluation["official_result"]
    assert evaluation["result_matches_official"] is True


def test_metric_event_does_not_mutate_governing_rule():
    assert FIXTURE["governing_rule"]["textual_mutation_at_metric_event"] is None
    assert FIXTURE["official_metric_observation"]["value"] == 1_023_494_202
    assert FIXTURE["downstream_effect"]["quantity"] == 190_494_202


def test_dynamic_set_contract_has_no_honest_scalar_metric_shape():
    transition_required = set(
        SET_SCHEMA["$defs"]["transition"]["required"]
    )

    assert "member" in transition_required
    assert "operation" in transition_required
    assert "metric_value" not in transition_required
    assert FIXTURE["architecture_probe"]["authoritative_dynamic_set_v0_1"][
        "fit"
    ] == "FAILS_CAUSAL_SHAPE"


def test_temporal_contract_owns_dates_not_metric_arithmetic():
    properties = set(TEMPORAL_SCHEMA["properties"])

    assert "normalized_date" in properties
    assert "metric_value" not in properties
    assert "formula" not in properties
    assert FIXTURE["architecture_probe"]["temporal_v0_1"]["fit"] == (
        "PARTIAL_ONLY"
    )


def test_source_observation_explicitly_does_not_supply_legal_semantics():
    inference = SOURCE_SCHEMA["properties"]["legal_mutation_inference"]

    assert inference["const"] == "NONE_FROM_ARTIFACT_OBSERVATION_ALONE"
    assert "metric_value" not in SOURCE_SCHEMA["properties"]
    assert FIXTURE["architecture_probe"]["source_observation_v0_1"]["fit"] == (
        "PARTIAL_ONLY"
    )


def test_change_atom_requires_textual_mutation_cause():
    source_mutations = CHANGE_ATOM_SCHEMA["properties"]["source_mutation_ids"]

    assert "source_mutation_ids" in CHANGE_ATOM_SCHEMA["required"]
    assert source_mutations["minItems"] == 1
    assert FIXTURE["architecture_probe"]["change_atom_v0_3"]["fit"] == (
        "FAILS_CAUSAL_REQUIREMENT"
    )


def test_failure_is_pinned_before_architecture():
    probe = FIXTURE["architecture_probe"]

    assert probe["result"] == "REPRESENTATIONAL_FAILURE_PINNED"
    assert probe["provisional_missing_concept"] == (
        "AUTHORITATIVE_METRIC_OBSERVATION_AND_RULE_EVALUATION"
    )
    assert probe["new_schema_added_in_this_probe"] is False
