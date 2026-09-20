import json
from datetime import date
from pathlib import Path

from needle.temporal.resolver import gap_between


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


DISCOVERY = load("fixtures/discovery/eprivacy-half-life-live-v0.1.json")
LINEAGE = load(
    "fixtures/lineage/reg2021-1232-to-reg2026-1881-gap-v0.2.json"
)
TEMPORAL = load(
    "fixtures/temporal/eprivacy-temporary-regime-v0.1.json"
)


def inclusive_days(start, end):
    return (date.fromisoformat(end)-date.fromisoformat(start)).days+1


def assertion(assertion_id):
    return next(
        item for item in TEMPORAL["assertions"]
        if item["assertion_id"] == assertion_id
    )


def canonical_metrics():
    original_start = assertion("eprivacy-2021-application-start")["normalized_date"]
    original_end = assertion(
        "eprivacy-2021-original-application-end"
    )["normalized_date"]
    extended_end = assertion(
        "eprivacy-2021-extended-application-end"
    )["normalized_date"]
    successor_start = assertion(
        "eprivacy-2026-application-start"
    )["normalized_date"]
    successor_end = assertion(
        "eprivacy-2026-application-end"
    )["normalized_date"]

    gap = gap_between(extended_end, successor_start)
    metrics = {
        "original_application_start":original_start,
        "original_planned_end":original_end,
        "original_planned_days":inclusive_days(original_start, original_end),
        "extended_first_regime_end":extended_end,
        "extended_first_regime_days":inclusive_days(original_start, extended_end),
        "extension_added_days":(
            date.fromisoformat(extended_end)-date.fromisoformat(original_end)
        ).days,
        "gap_start":gap["start"],
        "gap_end":gap["end"],
        "gap_days":inclusive_days(gap["start"], gap["end"]),
        "successor_application_start":successor_start,
        "successor_application_end":successor_end,
        "successor_days":inclusive_days(successor_start, successor_end),
    }
    metrics["total_applicable_days_through_successor_end"] = (
        metrics["extended_first_regime_days"] + metrics["successor_days"]
    )
    metrics["calendar_span_days"] = inclusive_days(original_start, successor_end)
    metrics["non_applicable_days_in_span"] = (
        metrics["calendar_span_days"]
        - metrics["total_applicable_days_through_successor_end"]
    )
    return metrics


def test_half_life_discovery_snapshot_matches_canonical_temporal_derivation():
    assert canonical_metrics() == DISCOVERY["derived_metrics"]


def test_half_life_preserves_real_gap_from_temporal_refs_only():
    metrics = canonical_metrics()
    assert metrics["gap_start"] == "2026-04-04"
    assert metrics["gap_end"] == "2026-07-30"
    assert metrics["gap_days"] == 118

    assert set(LINEAGE["temporal_assertion_refs"]) >= {
        "eprivacy-2021-extended-application-end",
        "eprivacy-2026-application-start",
    }
    encoded = json.dumps(LINEAGE)
    assert "applicability_continuity" not in encoded
    assert "application_start" not in encoded
    assert "application_end" not in encoded


def test_half_life_does_not_overclaim_rule_continuity():
    assert DISCOVERY["scope"]["proposition_continuity_asserted"] is False
    assert DISCOVERY["scope"]["temporal_genealogy_only"] is True
    assert LINEAGE["relation_type"] == "REENACTED_AS"
    assert "proposition-level rule continuity remains unresolved" in (
        LINEAGE["targets"][0]["scope_note"]
    )


def test_half_life_evidence_is_immutable_and_exactly_located():
    for act in DISCOVERY["official_evidence"].values():
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
    m = canonical_metrics()
    assert m["total_applicable_days_through_successor_end"] == 2319
    assert m["calendar_span_days"] == 2437
    assert m["non_applicable_days_in_span"] == 118
    assert m["non_applicable_days_in_span"] == m["gap_days"]


def test_half_life_guardrails_are_part_of_the_fixture():
    guardrails = " ".join(DISCOVERY["interpretation_guardrails"]).casefold()
    assert "not an evaluative criticism" in guardrails
    assert "does not imply uninterrupted applicability" in guardrails
    assert "no proposition-by-proposition rule continuity" in guardrails
