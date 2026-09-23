#!/usr/bin/env python3
"""Validate the public Morrow // Needle adversarial corpus index."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROLE_VALUES = {"DERIVATION", "EVALUATION"}
EXPOSURE_VALUES = {
    "PUBLIC_FROM_DISCOVERY",
    "REVEALED_AFTER_SEALED_EVALUATION",
}
FUTURE_USE_VALUES = {"REGRESSION_ONLY"}


class CorpusValidationError(ValueError):
    pass


def _fail(message: str) -> None:
    raise CorpusValidationError(message)


def validate(data: dict, repo_root: Path) -> None:
    if data.get("schema_version") != "adversarial-corpus-index-v0.1":
        _fail("unexpected schema_version")

    trap_classes = data.get("trap_classes")
    if not isinstance(trap_classes, dict) or not trap_classes:
        _fail("trap_classes must be a non-empty object")

    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        _fail("cases must be a non-empty list")

    if data.get("case_count") != len(cases):
        _fail("case_count does not match cases length")

    seen_ids: set[str] = set()
    used_trap_classes: set[str] = set()

    for position, case in enumerate(cases):
        label = f"cases[{position}]"

        required = {
            "id",
            "title",
            "domain",
            "jurisdiction",
            "trap_classes",
            "provenance",
            "exposure",
            "decisive_trap",
            "evidence_refs",
        }
        missing = sorted(required - case.keys())
        if missing:
            _fail(f"{label} missing required keys: {', '.join(missing)}")

        case_id = case["id"]
        if not isinstance(case_id, str) or not case_id.strip():
            _fail(f"{label}.id must be a non-empty string")
        if case_id in seen_ids:
            _fail(f"duplicate case id: {case_id}")
        seen_ids.add(case_id)

        classes = case["trap_classes"]
        if not isinstance(classes, list) or not classes:
            _fail(f"{case_id}: trap_classes must be a non-empty list")
        unknown = sorted(set(classes) - set(trap_classes))
        if unknown:
            _fail(f"{case_id}: unknown trap classes: {', '.join(unknown)}")
        used_trap_classes.update(classes)

        provenance = case["provenance"]
        if provenance.get("role") not in ROLE_VALUES:
            _fail(f"{case_id}: invalid provenance role")
        issue = provenance.get("issue")
        if not isinstance(issue, int) or issue <= 0:
            _fail(f"{case_id}: provenance issue must be a positive integer")

        exposure = case["exposure"]
        if exposure.get("status") not in EXPOSURE_VALUES:
            _fail(f"{case_id}: invalid exposure status")
        if exposure.get("future_use") not in FUTURE_USE_VALUES:
            _fail(f"{case_id}: invalid future_use")
        if exposure.get("blind_reuse") is not False:
            _fail(f"{case_id}: public/revealed v0.1 cases must set blind_reuse=false")

        if provenance["role"] == "DERIVATION" and exposure["status"] != "PUBLIC_FROM_DISCOVERY":
            _fail(f"{case_id}: derivation case must be PUBLIC_FROM_DISCOVERY")
        if provenance["role"] == "EVALUATION" and exposure["status"] != "REVEALED_AFTER_SEALED_EVALUATION":
            _fail(f"{case_id}: evaluation case must be REVEALED_AFTER_SEALED_EVALUATION")

        refs = case["evidence_refs"]
        if not isinstance(refs, list) or not refs:
            _fail(f"{case_id}: evidence_refs must be a non-empty list")

        expected_issue_ref = f"issue:{issue}"
        if expected_issue_ref not in refs:
            _fail(f"{case_id}: evidence_refs must include {expected_issue_ref}")

        for ref in refs:
            if not isinstance(ref, str) or ":" not in ref:
                _fail(f"{case_id}: malformed evidence ref {ref!r}")
            kind, value = ref.split(":", 1)
            if kind == "path":
                relative = Path(value)
                if relative.is_absolute() or ".." in relative.parts:
                    _fail(f"{case_id}: artifact path must stay inside repository")
                target = repo_root / relative
                if not target.is_file():
                    _fail(f"{case_id}: missing referenced path {value}")
            elif kind == "issue":
                try:
                    issue_ref = int(value)
                except ValueError as exc:
                    raise CorpusValidationError(
                        f"{case_id}: invalid issue ref {ref!r}"
                    ) from exc
                if issue_ref <= 0:
                    _fail(f"{case_id}: issue ref must be positive")
            else:
                _fail(f"{case_id}: unsupported evidence ref kind {kind!r}")

    unused_trap_classes = sorted(set(trap_classes) - used_trap_classes)
    if unused_trap_classes:
        _fail(
            "trap classes without cases: " + ", ".join(unused_trap_classes)
        )


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    index_path = repo_root / "corpus" / "index-v0.1.json"
    try:
        data = json.loads(index_path.read_text(encoding="utf-8"))
        validate(data, repo_root)
    except (OSError, json.JSONDecodeError, CorpusValidationError) as exc:
        print(f"adversarial corpus validation failed: {exc}", file=sys.stderr)
        return 1

    print(f"adversarial corpus validation passed: {data['case_count']} cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
