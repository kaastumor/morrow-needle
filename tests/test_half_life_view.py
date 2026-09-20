import json
import re
from copy import deepcopy
from pathlib import Path

from jsonschema import Draft202012Validator
import pytest

from needle.analytics.half_life import (
    HalfLifeError,
    build_half_life_view,
    render_half_life_text,
)


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


COMPOSITION = load("fixtures/analytics/eprivacy-half-life-v0.1.json")
COMPOSITION_SCHEMA = load("schemas/half-life-composition-v0.1.schema.json")
VIEW_SCHEMA = load("schemas/half-life-view-v0.1.schema.json")


def test_half_life_composition_is_reference_only_and_schema_valid():
    assert list(
        Draft202012Validator(COMPOSITION_SCHEMA).iter_errors(COMPOSITION)
    ) == []
    encoded=json.dumps(COMPOSITION,sort_keys=True)
    assert re.search(r"\b\d{4}-\d{2}-\d{2}\b",encoded) is None
    for forbidden in (
        "application_start",
        "application_end",
        "gap_start",
        "gap_end",
        "duration_days",
    ):
        assert f'"{forbidden}"' not in encoded


def test_eprivacy_half_life_view_is_derived_and_schema_valid():
    view=build_half_life_view(COMPOSITION)
    assert list(Draft202012Validator(VIEW_SCHEMA).iter_errors(view)) == []
    assert view["character"] == "DERIVED_VIEW"
    assert view["summary"] == {
        "original_planned_days":1098,
        "first_regime_actual_days":1706,
        "extension_added_days":608,
        "successor_days":613,
        "total_applicable_days":2319,
        "calendar_span_days":2437,
        "non_applicable_days":118,
        "first_regime_duration_ratio":1.5537,
    }


def test_every_displayed_boundary_retains_temporal_assertion_identity():
    view=build_half_life_view(COMPOSITION)
    source_ids=set(view["sources"]["temporal_assertion_ids"])
    for interval in [view["original_plan"], *view["episodes"]]:
        for boundary in ("start","end"):
            assert interval[boundary]["assertion_id"] in source_ids
    for gap in view["gaps"]:
        assert gap["previous_end_assertion_id"] in source_ids
        assert gap["next_start_assertion_id"] in source_ids


def test_extension_is_derived_from_explicit_temporal_override():
    view=build_half_life_view(COMPOSITION)
    assert view["extensions"] == [{
        "regime_id":"REGIME:2021R1232_AS_EXTENDED",
        "previous_end":"2024-08-03",
        "new_end":"2026-04-03",
        "added_days":608,
        "supersedes_assertion_id":"eprivacy-2021-original-application-end",
        "extension_assertion_id":"eprivacy-2021-extended-application-end",
    }]


def test_gap_is_visible_not_smoothed_into_genealogical_continuity():
    view=build_half_life_view(COMPOSITION)
    assert view["gaps"] == [{
        "from_regime_id":"REGIME:2021R1232_AS_EXTENDED",
        "to_regime_id":"REGIME:2026R1881",
        "start":"2026-04-04",
        "end":"2026-07-30",
        "duration_days":118,
        "previous_end_assertion_id":"eprivacy-2021-extended-application-end",
        "next_start_assertion_id":"eprivacy-2026-application-start",
    }]


def test_half_life_refuses_discovery_era_lineage_with_embedded_dates():
    bad=deepcopy(COMPOSITION)
    bad["lineage_fixture_path"] = (
        "fixtures/lineage/reg2021-1232-to-reg2026-1881-gap-v0.1.json"
    )
    with pytest.raises(HalfLifeError,match="regime-lineage-v0.2"):
        build_half_life_view(bad)


def test_half_life_refuses_unknown_temporal_reference():
    bad=deepcopy(COMPOSITION)
    bad["original_regime"]["end_assertion_ids"][-1]="invented-end"
    with pytest.raises(HalfLifeError,match="unknown temporal assertion"):
        build_half_life_view(bad)


def test_half_life_refuses_wrong_temporal_dimension():
    bad=deepcopy(COMPOSITION)
    bad["original_regime"]["application_start_assertion_id"]="eprivacy-2021-publication"
    with pytest.raises(HalfLifeError,match="requires APPLICATION"):
        build_half_life_view(bad)


def test_render_is_factual_and_exposes_evidence_model():
    text=render_half_life_text(build_half_life_view(COMPOSITION))
    assert "originally planned for 1,098 days" in text
    assert "extended by 608 days" in text
    assert "118-day gap" in text
    assert "canonical Temporal Assertion ID" in text
    assert "genealogy only" in text
    assert "temporary was abused" not in text.casefold()
    assert "should have expired" not in text.casefold()


def test_half_life_does_not_assert_rule_level_continuity():
    view=build_half_life_view(COMPOSITION)
    combined=" ".join(view["guardrails"] + view["unknowns"]).casefold()
    assert "no proposition-level rule continuity" in combined
    assert "proposition-by-proposition continuity" in combined



def test_half_life_supports_repeated_extension_history(tmp_path):
    composition=deepcopy(COMPOSITION)
    temporal=load(composition["temporal_fixture_path"])
    lineage=load(composition["lineage_fixture_path"])

    prior=next(
        item for item in temporal["assertions"]
        if item["assertion_id"] == "eprivacy-2021-extended-application-end"
    )
    second=deepcopy(prior)
    second["assertion_id"]="test-second-extension-end"
    second["normalized_date"]="2026-06-03"
    second["trigger"]={
        "kind":"ABSOLUTE_DATE",
        "date":"2026-06-03",
        "source_expression":"test-only second extension boundary",
    }
    second["scope"]["overrides_assertion_ids"]=[
        "eprivacy-2021-extended-application-end"
    ]
    temporal["assertions"].append(second)

    composition["original_regime"]["end_assertion_ids"].append(
        "test-second-extension-end"
    )
    lineage["temporal_assertion_refs"].append("test-second-extension-end")

    temporal_path=tmp_path / composition["temporal_fixture_path"]
    lineage_path=tmp_path / composition["lineage_fixture_path"]
    temporal_path.parent.mkdir(parents=True,exist_ok=True)
    lineage_path.parent.mkdir(parents=True,exist_ok=True)
    temporal_path.write_text(json.dumps(temporal),encoding="utf-8")
    lineage_path.write_text(json.dumps(lineage),encoding="utf-8")

    view=build_half_life_view(composition,root=tmp_path)
    assert [item["added_days"] for item in view["extensions"]] == [608,61]
    assert view["summary"]["extension_added_days"] == 669
    assert view["episodes"][0]["end"]["assertion_id"] == (
        "test-second-extension-end"
    )


def test_half_life_rejects_broken_extension_override_chain(tmp_path):
    composition=deepcopy(COMPOSITION)
    temporal=load(composition["temporal_fixture_path"])
    lineage=load(composition["lineage_fixture_path"])

    prior=next(
        item for item in temporal["assertions"]
        if item["assertion_id"] == "eprivacy-2021-extended-application-end"
    )
    second=deepcopy(prior)
    second["assertion_id"]="test-broken-extension-end"
    second["normalized_date"]="2026-06-03"
    second["trigger"]={
        "kind":"ABSOLUTE_DATE",
        "date":"2026-06-03",
        "source_expression":"test-only broken extension boundary",
    }
    second["scope"]["overrides_assertion_ids"]=[
        "eprivacy-2021-original-application-end"
    ]
    temporal["assertions"].append(second)
    composition["original_regime"]["end_assertion_ids"].append(
        "test-broken-extension-end"
    )
    lineage["temporal_assertion_refs"].append("test-broken-extension-end")

    temporal_path=tmp_path / composition["temporal_fixture_path"]
    lineage_path=tmp_path / composition["lineage_fixture_path"]
    temporal_path.parent.mkdir(parents=True,exist_ok=True)
    lineage_path.parent.mkdir(parents=True,exist_ok=True)
    temporal_path.write_text(json.dumps(temporal),encoding="utf-8")
    lineage_path.write_text(json.dumps(lineage),encoding="utf-8")

    with pytest.raises(HalfLifeError,match="does not explicitly override"):
        build_half_life_view(composition,root=tmp_path)



def test_every_half_life_boundary_carries_official_source_evidence():
    view=build_half_life_view(COMPOSITION)
    for interval in [view["original_plan"], *view["episodes"]]:
        for boundary_name in ("start","end"):
            boundary=interval[boundary_name]
            assert boundary["resolution_state"].startswith("RESOLVED_")
            assert boundary["evidence_state"] in {"DIRECT","DERIVED"}
            assert boundary["source_refs"]
            assert all(ref["identifier"] for ref in boundary["source_refs"])
            assert all(ref["role"] for ref in boundary["source_refs"])


def test_half_life_genealogy_is_exposed_without_becoming_time_owner():
    view=build_half_life_view(COMPOSITION)
    assert view["genealogy"] == {
        "edge_id":"eprivacy-2021-regime-reenacted-as-2026",
        "relation_type":"REENACTED_AS",
        "evidence_state":"DIRECT",
        "source_regime_ids":["REGIME:2021R1232_AS_EXTENDED"],
        "target_regime_ids":["REGIME:2026R1881"],
    }
    encoded=json.dumps(view["genealogy"],sort_keys=True)
    assert "2026-04-03" not in encoded
    assert "2026-07-31" not in encoded


def test_half_life_view_horizon_is_not_misreported_as_final_expiry():
    view=build_half_life_view(COMPOSITION)
    horizon=view["coverage"]["view_horizon"]
    assert horizon["regime_id"] == "REGIME:2026R1881"
    assert horizon["boundary"]["date"] == "2028-04-03"
    assert horizon["boundary"]["assertion_id"] == "eprivacy-2026-application-end"
    assert view["coverage"]["terminal_outcome"] == (
        "UNRESOLVED_AFTER_VIEW_HORIZON"
    )
    assert view["coverage"]["rule_continuity"] == "NOT_ASSERTED"

    text=render_half_life_text(view)
    assert "not presented as final expiry" in text
    assert "Proposition-level rule continuity" in text
