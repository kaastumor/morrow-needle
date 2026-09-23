import json
from pathlib import Path

from jsonschema import Draft202012Validator

from needle.temporal.resolver import gap_between


TEMPORAL=json.loads(
    Path("fixtures/temporal/aggregateeu-regime-transition-v0.1.json").read_text(
        encoding="utf-8"
    )
)
LINEAGE=json.loads(
    Path("fixtures/lineage/reg2022-2576-to-reg2024-1789-aggregateeu-v0.1.json").read_text(
        encoding="utf-8"
    )
)
OPERATIONAL=json.loads(
    Path("fixtures/discovery/aggregateeu-operational-afterlife-v0.1.json").read_text(
        encoding="utf-8"
    )
)
TEMPORAL_SCHEMA=json.loads(
    Path("schemas/temporal-assertion-v0.1.schema.json").read_text(encoding="utf-8")
)
LINEAGE_SCHEMA=json.loads(
    Path("schemas/regime-lineage-v0.2.schema.json").read_text(encoding="utf-8")
)


def temporal_index():
    return {item["assertion_id"]:item for item in TEMPORAL["assertions"]}


def operational_index():
    return {
        item["observation_id"]:item
        for item in OPERATIONAL["operational_observations"]
    }


def test_existing_temporal_and_regime_lineage_contracts_represent_case():
    temporal_errors=[
        error.message
        for assertion in TEMPORAL["assertions"]
        for error in Draft202012Validator(TEMPORAL_SCHEMA).iter_errors(assertion)
    ]
    lineage_errors=list(Draft202012Validator(LINEAGE_SCHEMA).iter_errors(LINEAGE))
    assert temporal_errors == []
    assert lineage_errors == []


def test_genealogy_is_direct_and_does_not_own_dates():
    assert LINEAGE["relation_type"] == "SUPERSEDED_BY"
    assert LINEAGE["genealogical_evidence_state"] == "DIRECT"
    encoded=json.dumps(LINEAGE,sort_keys=True)
    assert "2024-12-31" not in encoded
    assert "2025-01-01" not in encoded
    assert "2024-08-04" not in encoded


def test_temporary_and_permanent_substantive_regimes_have_no_calendar_gap():
    temporal=temporal_index()
    end=temporal["aggregateeu-crisis-application-end"]
    start=temporal["aggregateeu-permanent-application-start"]

    assert gap_between(
        end["normalized_date"],
        start["normalized_date"],
        previous_end_inclusive=end["inclusive"],
        next_start_inclusive=start["inclusive"],
    ) == {"state":"NO_GAP","start":None,"end":None}


def test_preparatory_transition_overlaps_temporary_regime_without_becoming_application():
    temporal=temporal_index()
    prep=temporal["aggregateeu-permanent-preparatory-transition-start"]
    temp_end=temporal["aggregateeu-crisis-application-end"]
    permanent_start=temporal["aggregateeu-permanent-application-start"]

    assert prep["dimension"] == "TRANSITION"
    assert permanent_start["dimension"] == "APPLICATION"
    assert prep["normalized_date"] < temp_end["normalized_date"]
    assert prep["normalized_date"] < permanent_start["normalized_date"]
    assert permanent_start["normalized_date"] > temp_end["normalized_date"]


def test_aggregateeu_brand_survives_into_successor_legal_basis():
    observations=operational_index()
    terms=observations["aggregateeu-terms-2025-03-07"]
    round2=observations["aggregateeu-midterm-round-2025-03-26"]

    assert terms["visible_service_name"] == "AggregateEU"
    assert "2024/1789" in terms["legal_basis"]
    assert round2["visible_service_name"] == "AggregateEU"
    assert "Permanent" in round2["legal_basis"]


def test_platform_shell_is_not_promoted_to_legal_regime_identity():
    observations=operational_index()
    platform=observations["energy-raw-materials-platform-launch-2025-07-02"]

    assert platform["visible_service_name"] == "EU Energy and Raw Materials Platform"
    assert OPERATIONAL["finding"]["platform_shell_continuity"] == "NOT_SAME_IDENTITY"


def test_same_visible_service_does_not_mean_same_legal_regime():
    finding=OPERATIONAL["finding"]
    assert finding["legal_regime_genealogy"] == "DIRECT_TEMPORARY_TO_PERMANENT"
    assert finding["legal_application_continuity"] == "CONTIGUOUS"
    assert finding["service_brand_continuity"] == (
        "AGGREGATEEU_SURVIVES_LEGAL_BASIS_CHANGE"
    )
    forbidden=" ".join(OPERATIONAL["forbidden_inferences"])
    assert "brand name was unchanged" in forbidden
    assert "continuous visible service proves one continuous legal instrument" in forbidden.lower()


def test_discovery_does_not_require_new_regime_lineage_schema():
    assert LINEAGE["schema_version"] == "regime-lineage-v0.2"
    assert TEMPORAL["status"] == "DISCOVERY_CANONICAL_CANDIDATE"
