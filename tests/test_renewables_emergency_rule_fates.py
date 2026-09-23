import json
from pathlib import Path


FIXTURE = json.loads(
    Path(
        "fixtures/lineage/reg2022-2577-to-dir2023-2413-rule-fates-v0.1.json"
    ).read_text(encoding="utf-8")
)


def fates():
    return {item["rule_id"]: item for item in FIXTURE["rule_fates"]}


def test_one_emergency_act_has_multiple_rule_fates():
    classifications = {item["classification"] for item in FIXTURE["rule_fates"]}

    assert "PROMOTED_TO_PERMANENT" in classifications
    assert "TEMPORARY_COEXISTENCE_WITH_PERMANENT_REGIME" in classifications
    assert "TEMPORARY_BRIDGE_ALONGSIDE_PERMANENT_REGIME" in classifications
    assert "TEXTUALLY_CLOSE_PERMANENT_ANALOGUE" in classifications


def test_article_3_1_has_direct_official_promotion_evidence():
    rule = fates()["overriding-public-interest-presumption"]

    assert rule["source_anchor"].endswith("Article 3(1)")
    assert "Article 16f" in rule["target_anchor"]
    assert rule["classification"] == "PROMOTED_TO_PERMANENT"
    assert rule["genealogical_evidence_state"] == "DIRECT"
    evidence = " ".join(
        item["observation"] for item in rule["official_bridge_evidence"]
    ).lower()
    assert "declines to prolong" in evidence
    assert "prolong" in evidence
    assert "same presumption" in evidence


def test_temporary_coexistence_is_not_promoted_to_permanent_identity():
    rule = fates()["repowering-emergency-deadline"]

    assert rule["classification"] == "TEMPORARY_COEXISTENCE_WITH_PERMANENT_REGIME"
    assert rule["genealogical_evidence_state"] == "DIRECT"
    assert "Coexistence is not promotion" in rule["caution"]


def test_article_6_is_a_bounded_bridge_not_semantic_identity():
    rule = fates()["dedicated-area-environmental-derogation"]

    assert rule["classification"] == "TEMPORARY_BRIDGE_ALONGSIDE_PERMANENT_REGIME"
    evidence = " ".join(
        item["observation"] for item in rule["official_bridge_evidence"]
    ).lower()
    assert "coexist" in evidence
    assert "limited period" in evidence
    assert "not evidence" in rule["caution"]


def test_close_analogues_remain_derived_without_provision_specific_genealogy():
    indexed = fates()

    for rule_id in ("solar-permitting", "heat-pump-permitting"):
        rule = indexed[rule_id]
        assert rule["classification"] == "TEXTUALLY_CLOSE_PERMANENT_ANALOGUE"
        assert rule["genealogical_evidence_state"] == "DERIVED"
        assert "provision-specific official statement" in rule["caution"].lower()


def test_transposition_deadline_is_not_promoted_to_national_application_start():
    timing = FIXTURE["handoff_timing"]

    assert timing["red_iii_selected_permitting_transposition_deadline"] == "2024-07-01"
    assert timing["national_application_continuity"] == (
        "UNRESOLVED_WITHOUT_MEMBER_STATE_IMPLEMENTATION_EVIDENCE"
    )
    assert "not itself a national application-start" in timing["warning"]


def test_discovery_requires_no_new_schema():
    result = FIXTURE["architecture_result"]

    assert result["decision"] == "SURVIVES_WITH_PROPOSITION_LEVEL_DECOMPOSITION"
    assert result["new_schema_required"] is False
    forbidden = " ".join(result["forbidden_shortcuts"]).lower()
    assert "one successor" in forbidden
    assert "transposition deadline" in forbidden
