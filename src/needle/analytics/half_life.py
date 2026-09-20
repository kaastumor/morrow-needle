from __future__ import annotations

from datetime import date
import json
from pathlib import Path
from typing import Any

from needle.temporal.resolver import gap_between


class HalfLifeError(ValueError):
    pass


def _read_json(root: Path, path: str) -> dict[str, Any]:
    return json.loads((root / path).read_text(encoding="utf-8"))


def _inclusive_days(start: str, end: str) -> int:
    return (date.fromisoformat(end) - date.fromisoformat(start)).days + 1


def _effective_start(boundary: dict[str, Any]) -> date:
    value=date.fromisoformat(boundary["date"])
    return value if boundary["inclusive"] else value.fromordinal(value.toordinal()+1)


def _effective_end(boundary: dict[str, Any]) -> date:
    value=date.fromisoformat(boundary["date"])
    return value if boundary["inclusive"] else value.fromordinal(value.toordinal()-1)


def _interval_days(start: dict[str, Any], end: dict[str, Any]) -> int:
    first=_effective_start(start)
    last=_effective_end(end)
    if last < first:
        raise HalfLifeError("temporal interval has no applicable calendar days")
    return (last-first).days+1


def _assertion(
    registry: dict[str, dict[str, Any]],
    assertion_id: str,
    *,
    boundary: str,
    regime_id: str,
) -> dict[str, Any]:
    assertion = registry.get(assertion_id)
    if assertion is None:
        raise HalfLifeError(f"unknown temporal assertion: {assertion_id}")
    if assertion.get("dimension") != "APPLICATION":
        raise HalfLifeError(
            f"{assertion_id}: Half-Life requires APPLICATION, "
            f"got {assertion.get('dimension')}"
        )
    if assertion.get("boundary") != boundary:
        raise HalfLifeError(
            f"{assertion_id}: expected {boundary} boundary, "
            f"got {assertion.get('boundary')}"
        )
    if regime_id not in assertion.get("scope", {}).get("applies_to", []):
        raise HalfLifeError(
            f"{assertion_id}: does not apply to declared regime {regime_id}"
        )
    if assertion.get("resolution_state") not in {
        "RESOLVED_ABSOLUTE",
        "RESOLVED_RELATIVE",
    }:
        raise HalfLifeError(
            f"{assertion_id}: unresolved temporal boundary "
            f"{assertion.get('resolution_state')}"
        )
    if not assertion.get("normalized_date"):
        raise HalfLifeError(f"{assertion_id}: missing normalized_date")
    return assertion


def _end_history(
    registry: dict[str, dict[str, Any]],
    regime: dict[str, Any],
) -> list[dict[str, Any]]:
    result = [
        _assertion(
            registry,
            assertion_id,
            boundary="END",
            regime_id=regime["regime_id"],
        )
        for assertion_id in regime["end_assertion_ids"]
    ]
    previous = result[0]
    for current in result[1:]:
        overrides=set(
            current.get("scope", {}).get("overrides_assertion_ids", [])
        )
        if previous["assertion_id"] not in overrides:
            raise HalfLifeError(
                f"{current['assertion_id']}: extension history does not "
                f"explicitly override prior end {previous['assertion_id']}"
            )
        if date.fromisoformat(current["normalized_date"]) <= date.fromisoformat(
            previous["normalized_date"]
        ):
            raise HalfLifeError(
                f"{current['assertion_id']}: Half-Life extension must move "
                "the regime end later"
            )
        previous=current
    return result


def _boundary_view(assertion: dict[str, Any]) -> dict[str, Any]:
    return {
        "date":assertion["normalized_date"],
        "assertion_id":assertion["assertion_id"],
        "inclusive":bool(assertion.get("inclusive", True)),
        "resolution_state":assertion["resolution_state"],
        "evidence_state":assertion["evidence_state"],
        "source_refs":[dict(item) for item in assertion.get("source_refs", [])],
    }


def _interval(
    *,
    regime_id: str,
    start: dict[str, Any],
    end: dict[str, Any],
) -> dict[str, Any]:
    start_view=_boundary_view(start)
    end_view=_boundary_view(end)
    return {
        "regime_id":regime_id,
        "start":start_view,
        "end":end_view,
        "duration_days":_interval_days(start_view,end_view),
    }


def _extensions(
    *,
    regime_id: str,
    end_history: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    result=[]
    for previous,current in zip(end_history,end_history[1:]):
        result.append({
            "regime_id":regime_id,
            "previous_end":previous["normalized_date"],
            "new_end":current["normalized_date"],
            "added_days":(
                _effective_end(_boundary_view(current))
                - _effective_end(_boundary_view(previous))
            ).days,
            "supersedes_assertion_id":previous["assertion_id"],
            "extension_assertion_id":current["assertion_id"],
        })
    return result


def _validate_lineage(
    lineage: dict[str, Any],
    *,
    edge_id: str,
    original_regime_id: str,
    successor_regime_ids: list[str],
    required_temporal_refs: set[str],
) -> None:
    if lineage.get("schema_version") != "regime-lineage-v0.2":
        raise HalfLifeError(
            "Half-Life requires reference-only regime-lineage-v0.2"
        )
    if lineage.get("edge_id") != edge_id:
        raise HalfLifeError(
            f"lineage edge mismatch: expected {edge_id}, "
            f"got {lineage.get('edge_id')}"
        )
    source_ids={item["regime_id"] for item in lineage.get("sources", [])}
    target_ids={item["regime_id"] for item in lineage.get("targets", [])}
    if original_regime_id not in source_ids:
        raise HalfLifeError(
            f"lineage does not contain source regime {original_regime_id}"
        )
    missing_targets=set(successor_regime_ids)-target_ids
    if missing_targets:
        raise HalfLifeError(
            "lineage missing successor regimes: "
            + ", ".join(sorted(missing_targets))
        )
    temporal_refs=set(lineage.get("temporal_assertion_refs", []))
    missing_refs=required_temporal_refs-temporal_refs
    if missing_refs:
        raise HalfLifeError(
            "lineage missing required temporal references: "
            + ", ".join(sorted(missing_refs))
        )

    encoded=json.dumps(lineage,sort_keys=True)
    for forbidden in (
        '"application_start"',
        '"application_end"',
        '"applicability_continuity"',
        '"gap"',
    ):
        if forbidden in encoded:
            raise HalfLifeError(
                f"regime lineage contains forbidden temporal truth: {forbidden}"
            )


def build_half_life_view(
    composition: dict[str, Any],
    *,
    root: Path | str = Path("."),
) -> dict[str, Any]:
    """Build a disposable temporary-regime history view from canonical facts.

    Every date comes from referenced P0-E Temporal Assertions. The composition
    contains identifiers only; Regime Lineage supplies genealogy only.
    """
    root=Path(root)
    if composition.get("composition_character") != "REFERENCE_ONLY":
        raise HalfLifeError("Half-Life composition must be REFERENCE_ONLY")

    temporal=_read_json(root,composition["temporal_fixture_path"])
    lineage=_read_json(root,composition["lineage_fixture_path"])
    registry={
        assertion["assertion_id"]:assertion
        for assertion in temporal.get("assertions", [])
    }

    original=composition["original_regime"]
    original_id=original["regime_id"]
    original_start=_assertion(
        registry,
        original["application_start_assertion_id"],
        boundary="START",
        regime_id=original_id,
    )
    original_ends=_end_history(registry,original)

    successors=[]
    successor_ids=[]
    for item in composition["successor_regimes"]:
        regime_id=item["regime_id"]
        successor_ids.append(regime_id)
        start=_assertion(
            registry,
            item["application_start_assertion_id"],
            boundary="START",
            regime_id=regime_id,
        )
        ends=_end_history(registry,item)
        successors.append((item,start,ends))

    required_lineage_temporal_refs={
        original_ends[-1]["assertion_id"],
        successors[0][1]["assertion_id"],
    }
    _validate_lineage(
        lineage,
        edge_id=composition["lineage_edge_id"],
        original_regime_id=original_id,
        successor_regime_ids=successor_ids,
        required_temporal_refs=required_lineage_temporal_refs,
    )

    original_plan=_interval(
        regime_id=original_id,
        start=original_start,
        end=original_ends[0],
    )
    actual_first=_interval(
        regime_id=original_id,
        start=original_start,
        end=original_ends[-1],
    )

    extensions=_extensions(
        regime_id=original_id,
        end_history=original_ends,
    )

    episodes=[actual_first]
    for item,start,ends in successors:
        extensions.extend(
            _extensions(
                regime_id=item["regime_id"],
                end_history=ends,
            )
        )
        episodes.append(
            _interval(
                regime_id=item["regime_id"],
                start=start,
                end=ends[-1],
            )
        )

    gaps=[]
    for previous,following in zip(episodes,episodes[1:]):
        previous_end=previous["end"]
        next_start=following["start"]
        previous_last=_effective_end(previous_end)
        next_first=_effective_start(next_start)
        if next_first <= previous_last:
            raise HalfLifeError(
                "Half-Life v0.1 does not yet represent overlapping episodes; "
                f"{previous['regime_id']} -> {following['regime_id']}"
            )
        gap=gap_between(
            previous_end["date"],
            next_start["date"],
            previous_end_inclusive=previous_end["inclusive"],
            next_start_inclusive=next_start["inclusive"],
        )
        if gap["state"] == "GAP":
            gaps.append({
                "from_regime_id":previous["regime_id"],
                "to_regime_id":following["regime_id"],
                "start":gap["start"],
                "end":gap["end"],
                "duration_days":_inclusive_days(gap["start"],gap["end"]),
                "previous_end_assertion_id":previous_end["assertion_id"],
                "next_start_assertion_id":next_start["assertion_id"],
            })

    first_start=_effective_start(episodes[0]["start"])
    last_end=_effective_end(episodes[-1]["end"])
    total_applicable=sum(item["duration_days"] for item in episodes)
    calendar_span=(last_end-first_start).days+1
    gap_days=sum(item["duration_days"] for item in gaps)
    if calendar_span-total_applicable != gap_days:
        raise HalfLifeError(
            "episode accounting does not reconcile to calendar span"
        )

    assertion_ids=[original_start["assertion_id"]]
    assertion_ids.extend(item["assertion_id"] for item in original_ends)
    for _,start,ends in successors:
        assertion_ids.append(start["assertion_id"])
        assertion_ids.extend(item["assertion_id"] for item in ends)

    last_episode=episodes[-1]
    return {
        "schema_version":"half-life-view-v0.1",
        "analytic_id":composition["analytic_id"],
        "topic":composition["topic"],
        "character":"DERIVED_VIEW",
        "sources":{
            "temporal_assertion_ids":list(dict.fromkeys(assertion_ids)),
            "regime_lineage_edge_ids":[lineage["edge_id"]],
        },
        "genealogy":{
            "edge_id":lineage["edge_id"],
            "relation_type":lineage["relation_type"],
            "evidence_state":lineage["genealogical_evidence_state"],
            "source_regime_ids":[
                item["regime_id"] for item in lineage["sources"]
            ],
            "target_regime_ids":[
                item["regime_id"] for item in lineage["targets"]
            ],
        },
        "coverage":{
            "rule_continuity":"NOT_ASSERTED",
            "terminal_outcome":"UNRESOLVED_AFTER_VIEW_HORIZON",
            "view_horizon":{
                "regime_id":last_episode["regime_id"],
                "boundary":dict(last_episode["end"]),
            },
        },
        "original_plan":original_plan,
        "extensions":extensions,
        "episodes":episodes,
        "gaps":gaps,
        "summary":{
            "original_planned_days":original_plan["duration_days"],
            "first_regime_actual_days":actual_first["duration_days"],
            "extension_added_days":sum(
                item["added_days"] for item in extensions
            ),
            "successor_days":sum(
                item["duration_days"] for item in episodes[1:]
            ),
            "total_applicable_days":total_applicable,
            "calendar_span_days":calendar_span,
            "non_applicable_days":gap_days,
            "first_regime_duration_ratio":round(
                actual_first["duration_days"] / original_plan["duration_days"],
                4,
            ),
        },
        "guardrails":list(composition["guardrails"]),
        "unknowns":list(composition.get("unknowns", [])),
    }


def render_half_life_text(view: dict[str, Any]) -> str:
    summary=view["summary"]
    gap=view["gaps"][0] if view["gaps"] else None

    short=(
        f"The temporary regime was originally planned for "
        f"{summary['original_planned_days']:,} days"
    )
    if view["extensions"]:
        short += (
            f", then extended by {summary['extension_added_days']:,} days "
            f"across {len(view['extensions'])} evidenced extension"
            + ("s" if len(view["extensions"]) != 1 else "")
        )
    if gap:
        short += (
            f". After expiry there was a {gap['duration_days']:,}-day gap "
            "before the evidenced successor regime began"
        )
    short += "."

    lines=[
        "Morrow // Needle — Half-Life",
        "",
        "3 seconds",
        short,
        "",
        "30 seconds",
        f"- Original planned duration: {summary['original_planned_days']:,} days.",
        f"- First regime after evidenced extensions: {summary['first_regime_actual_days']:,} days.",
    ]
    for item in view["extensions"]:
        lines.append(
            f"- Extension for {item['regime_id']}: "
            f"{item['previous_end']} → {item['new_end']} "
            f"(+{item['added_days']:,} days)."
        )
    for item in view["gaps"]:
        lines.append(
            f"- Legal non-applicability gap: {item['start']} through "
            f"{item['end']} ({item['duration_days']:,} days)."
        )
    lines.extend([
        f"- Successor applicability represented in this view: "
        f"{summary['successor_days']:,} days.",
        "",
        "Evidence model",
        "- Every displayed boundary resolves to a canonical Temporal Assertion ID.",
        "- Regime lineage supplies genealogy only; it stores no application dates.",
        "- Durations and ratios are derived analytics, not canonical legal-time facts.",
        f"- Genealogy relation: {view['genealogy']['relation_type']} "
        f"({view['genealogy']['evidence_state']}).",
        "",
        "View horizon",
        (
            f"- The current view ends at "
            f"{view['coverage']['view_horizon']['boundary']['date']} for "
            f"{view['coverage']['view_horizon']['regime_id']}."
        ),
        "- This evidenced boundary is not presented as final expiry; later extension, replacement or permanent transition remains unresolved.",
        "- Proposition-level rule continuity into the successor regime is not asserted.",
        "",
        "Unknowns",
    ])
    lines.extend(f"- {item}" for item in view["unknowns"])
    return "\n".join(lines) + "\n"
