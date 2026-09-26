#!/usr/bin/env python3
"""Render a narrow harmonised-standard legal-status card.

Input is an existing Authoritative Dynamic Set record. This is a derived
product view, not a new legal-state owner and not legal-correctness automation.
"""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path
from typing import Any


def parse_date(value: str) -> date:
    return date.fromisoformat(value)


def matching_transition(
    record: dict[str, Any], standard: str, as_of: date
) -> tuple[dict[str, Any] | None, dict[str, str], dict[str, Any] | None]:
    transitions = []
    for transition in record["transitions"]:
        identifiers = transition["member"]["identifiers"]
        if not any(
            item["scheme"] == "HARMONISED_STANDARD"
            and item["value"] == standard
            for item in identifiers
        ):
            continue
        transitions.append(transition)

    if not transitions:
        raise ValueError(f"standard not found in record: {standard}")

    transitions.sort(key=lambda item: item["effective_from"])
    applicable = [
        item for item in transitions
        if parse_date(item["effective_from"]) <= as_of
    ]

    future = [
        item for item in transitions
        if parse_date(item["effective_from"]) > as_of
    ]
    next_transition = future[0] if future else None

    if applicable:
        latest = applicable[-1]
        return latest, latest["after"], next_transition

    first = transitions[0]
    return None, first["before"], next_transition


def view_state(member_state: dict[str, str]) -> tuple[str, str]:
    membership = member_state["membership"]
    status = member_state["status"]

    if membership == "NOT_INCLUDED":
        return "NOT_CITED", "NOT_AVAILABLE_VIA_THIS_OJ_REFERENCE"

    if status == "RESTRICTED":
        return "CITED_WITH_RESTRICTION", "RESTRICTED_TO_STATED_SCOPE"

    return "CITED", "AVAILABLE_WITHIN_COVERED_SCOPE"


def render_card(
    record: dict[str, Any], standard: str, as_of: date
) -> str:
    transition, state, next_transition = matching_transition(record, standard, as_of)
    oj_state, consequence = view_state(state)

    dependency = record["dependencies"][0]
    governing_rule = dependency["governing_rule"]

    lines = [
        "# Harmonised Standard Status Card",
        "",
        f"**Regime:** {governing_rule['act_id']} {governing_rule['provision']}",
        f"**Standard:** {standard}",
        f"**As of:** {as_of.isoformat()}",
        f"**OJ-reference state:** {oj_state}",
        f"**Presumption consequence:** {consequence}",
        "",
    ]

    if transition is None:
        lines += [
            "**Latest owning event:** none in this record before the query date",
            "",
            "**State basis:** pre-transition state preserved by the canonical record.",
            "",
        ]
    else:
        lines += [
            (
                "**Latest owning event:** "
                f"{transition['transition_id']} "
                f"(effective {transition['effective_from']})"
            ),
            "",
            f"**Scope / reason:** {transition['scope']['statement']}",
            "",
            "**Evidence:**",
        ]
        for source in transition["source_refs"]:
            lines.append(
                f"- {source['identifier']} — {source['locator']}"
            )
        lines.append("")

    if next_transition is not None:
        lines += [
            (
                "**Next scheduled owning event:** "
                f"{next_transition['transition_id']} "
                f"(effective {next_transition['effective_from']})"
            ),
            "",
            f"**Scheduled scope:** {next_transition['scope']['statement']}",
            "",
        ]

    lines += [
        "**Non-implications:**",
    ]
    for item in record["forbidden_inferences"]:
        lines.append(f"- {item}")

    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("record", type=Path)
    parser.add_argument("--standard", required=True)
    parser.add_argument("--as-of", required=True)
    args = parser.parse_args()

    record = json.loads(args.record.read_text(encoding="utf-8"))
    print(render_card(record, args.standard, parse_date(args.as_of)), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
