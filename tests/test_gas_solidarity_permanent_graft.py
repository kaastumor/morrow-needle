import json
from datetime import date, timedelta
from pathlib import Path


FIXTURE = json.loads(
    Path(
        "fixtures/lineage/reg2022-2576-solidarity-to-reg2017-1938-art13-v0.1.json"
    ).read_text(encoding="utf-8")
)


def test_direct_genealogy_targets_the_amended_2017_host():
    assert FIXTURE["genealogy"]["genealogical_evidence_state"] == "DIRECT"
    assert FIXTURE["genealogy"]["classification"] == "PERMANENT_GRAFT_WITH_MUTATION"
    assert FIXTURE["amending_instrument"]["act_id"] == "CELEX:32024R1789"
    assert FIXTURE["permanent_target"]["act_id"] == "CELEX:32017R1938"
    assert "Article 13(8a)-(8c)" in FIXTURE["permanent_target"]["provision"]


def test_crisis_and_permanent_rules_have_a_contiguous_eu_level_handoff():
    handoff = FIXTURE["handoff"]
    temporary_end = date.fromisoformat(handoff["temporary_last_day"])
    permanent_start = date.fromisoformat(handoff["permanent_first_day"])

    assert permanent_start == temporary_end + timedelta(days=1)
    assert handoff["calendar_gap"] is False


def test_core_mechanism_survives_the_graft():
    preserved = {item["rule"]: item for item in FIXTURE["preserved_core"]}

    assert set(preserved) == {
        "default-trigger",
        "compensation-categories",
        "market-price-benchmark",
        "solidarity-request-payload",
    }
    assert all(
        item["continuity"] == "DIRECT_CORE_CONTINUITY"
        for item in preserved.values()
    )
    assert preserved["compensation-categories"]["temporary"] == (
        preserved["compensation-categories"]["permanent"]
    )


def test_permanent_graft_is_not_a_verbatim_copy():
    mutations = {
        item["mutation"]: item for item in FIXTURE["substantive_mutations"]
    }

    assert mutations["request-lead-time"]["temporary"].startswith("At least 72")
    assert mutations["request-lead-time"]["permanent"].startswith("At least 48")
    assert mutations["response-window"]["temporary"] == "Response within 24 hours."
    assert mutations["response-window"]["permanent"] == (
        "Response effective within 18 hours."
    )
    assert mutations["indirect-cost-cap"]["effect"] == (
        "COMPENSATION_CONTROL_CHANGED"
    )
    assert mutations["ex-post-compensation-control"]["effect"] == (
        "NEW_PERMANENT_CONTROL_LAYER"
    )


def test_amending_instrument_is_not_laundered_into_current_rule_identity():
    target_note = FIXTURE["permanent_target"]["identity_note"]
    forbidden = " ".join(
        FIXTURE["architecture_result"]["forbidden_shortcuts"]
    ).lower()

    assert "canonically located" in target_note
    assert "amending instrument" in target_note
    assert "2024/1789 article 84" in forbidden
    assert "2017/1938 article 13" in forbidden


def test_discovery_requires_no_new_schema():
    result = FIXTURE["architecture_result"]

    assert result["decision"] == "SURVIVES"
    assert result["new_schema_required"] is False
    assert "genealogy" in result["statement"].lower()
    assert len(FIXTURE["substantive_mutations"]) >= 1
