import json
from datetime import date
from pathlib import Path

from needle.temporal.resolver import gap_between


FIXTURE = json.loads(
    Path("fixtures/discovery/eprivacy-half-life-live-v0.1.json").read_text(
        encoding="utf-8"
    )
)
LINEAGE = json.loads(
    Path(
        "fixtures/lineage/reg2021-1232-to-reg2026-1881-gap-v0.1.json"
    ).read_text(encoding="utf-8")
)


def inclusive_days(start, end):
    return (date.fromisoformat(end)-date.fromisoformat(start)).days+1


def test_half_life_metrics_are_derived_from_evidenced_dates():
    m = FIXTURE["derived_metrics"]
    assert m["original_planned_days"] == inclusive_days(
        m["original_application_start"],
        m["original_planned_end"],
    )
    assert m["extended_first_regime_days"] == inclusive_days(
        m["original_application_start"],
        m["extended_first_regime_end"],
    )
    assert m["extension_added_days"] == (
        date.fromisoformat(m["extended_first_regime_end"])
        - date.fromisoformat(m["original_planned_end"])
    ).days
    assert m["successor_days"] == inclusive_days(
        m["successor_application_start"],
        m["successor_application_end"],
    )


def test_half_life_preserves_real_gap():
    m = FIXTURE["derived_metrics"]
    gap = gap_between(
        m["extended_first_regime_end"],
        m["successor_application_start"],
    )
    assert gap == {
        "state":"GAP",
        "start":"2026-04-04",
        "end":"2026-07-30",
    }
    assert m["gap_days"] == inclusive_days(gap["start"], gap["end"])
    assert m["gap_days"] == 118
    assert LINEAGE["edge"]["applicability_continuity"] == "GAPPED"
    assert LINEAGE["edge"]["gap"]["start"] == gap["start"]
    assert LINEAGE["edge"]["gap"]["end"] == gap["end"]


def test_half_life_does_not_overclaim_rule_continuity():
    assert FIXTURE["scope"]["proposition_continuity_asserted"] is False
    assert FIXTURE["scope"]["temporal_genealogy_only"] is True
    assert LINEAGE["status"] == (
        "TEMPORAL_GAP_LIVE_VERIFIED_RULE_LINEAGE_PENDING"
    )
    assert LINEAGE["verification_todo"] == [
        "Anchor source and target rule-level spans before asserting proposition-by-proposition continuity."
    ]


def test_half_life_evidence_is_immutable_and_exactly_located():
    for act in FIXTURE["official_evidence"].values():
        assert act["artifact_hash"].startswith("sha256:")
        assert len(act["artifact_hash"]) == 71
        for key,value in act.items():
            if key == "artifact_hash":
                continue
            if not isinstance(value, dict):
                continue
            assert value["locator"]
            assert len(value["text_hash"]) == 64


def test_half_life_calendar_span_accounts_for_only_the_gap_as_non_applicable():
    m = FIXTURE["derived_metrics"]
    assert m["total_applicable_days_through_successor_end"] == (
        m["extended_first_regime_days"] + m["successor_days"]
    )
    assert m["calendar_span_days"] == inclusive_days(
        m["original_application_start"],
        m["successor_application_end"],
    )
    assert m["non_applicable_days_in_span"] == (
        m["calendar_span_days"]
        - m["total_applicable_days_through_successor_end"]
    )
    assert m["non_applicable_days_in_span"] == m["gap_days"]


def test_half_life_guardrails_are_part_of_the_fixture():
    guardrails = " ".join(FIXTURE["interpretation_guardrails"]).casefold()
    assert "not an evaluative criticism" in guardrails
    assert "does not imply uninterrupted applicability" in guardrails
    assert "no proposition-by-proposition rule continuity" in guardrails
