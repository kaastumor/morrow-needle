#!/usr/bin/env python3
"""Validate Morrow // Needle Gold Corpus fixtures.

JSON Schema checks shape; these checks enforce corpus invariants that JSON Schema
cannot conveniently express (referential integrity, globally unique assertion IDs,
and evidence/verification discipline).
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

EXPECTED_BUCKETS = (
    "document_relationships",
    "provision_alignments",
    "textual_mutations",
    "change_atoms",
    "non_atoms",
    "temporal_assertions",
)


def semantic_errors(case: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    sources = case.get("official_sources", [])
    source_ids = [source.get("source_id") for source in sources]
    if len(source_ids) != len(set(source_ids)):
        errors.append("official source_id values must be unique")
    known_sources = set(source_ids)

    seen_assertions: set[str] = set()
    all_assertions: list[dict[str, Any]] = []
    expected = case.get("expected", {})
    for bucket in EXPECTED_BUCKETS:
        for assertion in expected.get(bucket, []):
            all_assertions.append(assertion)
            assertion_id = assertion.get("assertion_id")
            if assertion_id in seen_assertions:
                errors.append(f"duplicate assertion_id: {assertion_id}")
            seen_assertions.add(assertion_id)

            evidence = assertion.get("evidence_source_ids", [])
            unknown = sorted(set(evidence) - known_sources)
            if unknown:
                errors.append(
                    f"{assertion_id}: unknown evidence_source_ids: {', '.join(unknown)}"
                )
            if assertion.get("status") in {"ASSERTED", "FORBIDDEN_INFERENCE"} and not evidence:
                errors.append(f"{assertion_id}: {assertion.get('status')} requires official evidence")

    verification = case.get("verification", {})
    if verification.get("state") == "VERIFIED":
        if not verification.get("verified_by"):
            errors.append("VERIFIED cases require at least one verified_by entry")
        unsettled = [
            a.get("assertion_id")
            for a in all_assertions
            if a.get("status") in {"CANDIDATE", "UNRESOLVED"}
        ]
        if unsettled:
            errors.append("VERIFIED case contains unsettled assertions: " + ", ".join(unsettled))

    return errors


def validate_case(case_path: Path, schema: dict[str, Any]) -> list[str]:
    case = json.loads(case_path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    errors = [
        f"schema: {error.message}"
        for error in sorted(validator.iter_errors(case), key=lambda e: list(e.absolute_path))
    ]
    errors.extend(f"semantic: {error}" for error in semantic_errors(case))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--schema", type=Path, default=Path("schemas/gold-corpus-case-v0.1.schema.json"))
    parser.add_argument("--fixtures", type=Path, default=Path("fixtures/gold"))
    args = parser.parse_args()

    schema = json.loads(args.schema.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    fixtures = sorted(args.fixtures.glob("*.json"))
    if not fixtures:
        print("ERROR: Gold Corpus contains no fixtures")
        return 1

    failed = False
    for fixture in fixtures:
        errors = validate_case(fixture, schema)
        if errors:
            failed = True
            print(f"FAIL {fixture}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"PASS {fixture}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
