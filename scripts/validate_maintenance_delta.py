#!/usr/bin/env python3
"""Structural and semantic validation for Candidate A maintenance-delta v0.1.

This validator deliberately does not decide legal correctness, source authority,
repair substance, comparability, or product value.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "maintenance-delta-v0.1.schema.json"
DEFAULT_FIXTURE_GLOB = "fixtures/mvp/maintenance-delta/*.json"

SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
SCHEMA_VALIDATOR = Draft202012Validator(SCHEMA)


def schema_errors(record: dict[str, Any]) -> list[str]:
    return [
        f"{'.'.join(str(part) for part in error.path) or '<root>'}: {error.message}"
        for error in sorted(SCHEMA_VALIDATOR.iter_errors(record), key=lambda e: list(e.path))
    ]


def semantic_errors(record: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    units = record.get("delta_units", [])
    ids = [unit.get("id") for unit in units]
    if len(ids) != len(set(ids)):
        errors.append("delta_units must have unique ids")

    for unit in units:
        unit_id = unit.get("id", "<unknown>")
        refs = unit.get("affected_contract_refs", [])
        risks = set(unit.get("risk", []))

        if not refs and "NO_KNOWN_SCORE_IMPACT" not in risks:
            errors.append(
                f"{unit_id}: empty affected_contract_refs requires NO_KNOWN_SCORE_IMPACT"
            )

        if "NO_KNOWN_SCORE_IMPACT" in risks and len(risks) > 1:
            errors.append(
                f"{unit_id}: NO_KNOWN_SCORE_IMPACT cannot be combined with another risk"
            )

        if unit.get("kind") == "LEGAL_PROPOSITION":
            if "evidence" not in unit:
                errors.append(f"{unit_id}: LEGAL_PROPOSITION requires evidence")
            if "governing_time" not in unit:
                errors.append(f"{unit_id}: LEGAL_PROPOSITION requires governing_time")

        governing_time = unit.get("governing_time")
        if governing_time:
            kind = governing_time.get("kind")
            if kind in {"LAW_AS_OF", "CONTROLLING_EVENT_DATE", "EFFECTIVE_PERIOD"}:
                if not governing_time.get("value_or_ref"):
                    errors.append(
                        f"{unit_id}: governing_time {kind} requires value_or_ref"
                    )

    subject = record.get("subject", {})
    repair = record.get("repair", {})
    change_status = record.get("change_status")

    if change_status == "ADOPTED_BY_OWNER" and not subject.get("candidate_contract_ref"):
        errors.append(
            "ADOPTED_BY_OWNER requires subject.candidate_contract_ref"
        )

    repair_status = repair.get("status")
    actions = repair.get("actions", [])

    if repair_status == "ACCEPTED":
        if not subject.get("candidate_contract_ref"):
            errors.append("accepted repair requires subject.candidate_contract_ref")
        if change_status != "ADOPTED_BY_OWNER":
            errors.append("accepted repair requires change_status ADOPTED_BY_OWNER")
        if not actions:
            errors.append("accepted repair requires at least one repair action")

    if repair_status in {"PROPOSED", "PARTIAL"} and not actions:
        errors.append(f"{repair_status} repair requires at least one repair action")

    if repair_status == "NOT_REQUIRED" and actions:
        errors.append("NOT_REQUIRED repair must not contain repair actions")

    unresolved_evidence = any(
        unit.get("evidence", {}).get("status") == "UNRESOLVED"
        for unit in units
    )
    if unresolved_evidence and repair_status == "ACCEPTED":
        adjudication = record.get("adjudication", {})
        if adjudication.get("status") != "ACCEPTED":
            errors.append(
                "accepted repair with unresolved evidence requires accepted adjudication"
            )

    result_impact = record.get("result_impact", {})
    if (
        result_impact.get("comparability") in {"NOT_COMPARABLE", "UNKNOWN"}
        and result_impact.get("existing_outputs_action") == "NONE"
    ):
        errors.append(
            "NOT_COMPARABLE/UNKNOWN result impact cannot use existing_outputs_action NONE"
        )

    return errors


def validate_record(record: dict[str, Any]) -> list[str]:
    return schema_errors(record) + semantic_errors(record)


def validate_path(path: Path) -> list[str]:
    try:
        record = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{path}: unable to load JSON: {exc}"]

    return [f"{path}: {error}" for error in validate_record(record)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", type=Path)
    args = parser.parse_args()

    paths = args.paths or sorted(ROOT.glob(DEFAULT_FIXTURE_GLOB))
    if not paths:
        print("No maintenance-delta fixtures found.")
        return 1

    errors: list[str] = []
    for path in paths:
        errors.extend(validate_path(path))

    if errors:
        for error in errors:
            print(error)
        return 1

    print(f"Validated {len(paths)} maintenance-delta record(s): 0 errors")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
