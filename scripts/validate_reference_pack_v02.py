#!/usr/bin/env python3
"""Validate Needle Reference Pack v0.2 and preserve the frozen v0.1 release."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts import build_reference_pack as v01_builder
from scripts import build_reference_pack_v02 as builder
from scripts.validate_reference_pack import (
    ReferencePackValidationError,
    validate_pack as validate_v01,
)


PACK_DIR_REL = Path("release") / "needle-reference-pack-v0.2"
PAYLOAD_FILES = sorted(
    [
        "README.md",
        "manifest.json",
        "cases.jsonl",
        "classes.json",
        "evidence-map.json",
        "catalog.md",
        "failure-analysis-guide.md",
    ]
)
GENERATED_FILES = [
    "manifest.json",
    "cases.jsonl",
    "classes.json",
    "evidence-map.json",
    "catalog.md",
]


class ReferencePackV02ValidationError(ValueError):
    pass


def fail(message: str) -> None:
    raise ReferencePackV02ValidationError(message)


def render_json(value: object) -> str:
    return json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def render_jsonl(rows: list[dict]) -> str:
    return "".join(
        json.dumps(
            row,
            sort_keys=True,
            ensure_ascii=False,
            separators=(",", ":"),
        )
        + "\n"
        for row in rows
    )


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def expected_generated_texts(source: dict) -> dict[str, str]:
    try:
        cases = v01_builder.sorted_cases(source)
        classes = v01_builder.build_classes(source, cases)
        evidence_map = v01_builder.build_evidence_map(source, cases)
        manifest = builder.build_manifest(source, evidence_map)
        catalog = builder.build_catalog(source, cases)
    except SystemExit as exc:
        fail(str(exc))

    return {
        "cases.jsonl": render_jsonl(cases),
        "classes.json": render_json(classes),
        "evidence-map.json": render_json(evidence_map),
        "catalog.md": catalog,
        "manifest.json": render_json(manifest),
    }


def render_checksums(root: Path) -> str:
    pack_dir = root / PACK_DIR_REL
    return "".join(
        f"{sha256_file(pack_dir / name)}  {name}\n"
        for name in PAYLOAD_FILES
    )


def validate_pack(
    root: Path = ROOT,
    *,
    require_checksums: bool = True,
    run_canonical_validation: bool = True,
) -> dict[str, int]:
    try:
        validate_v01(
            root,
            run_canonical_validation=run_canonical_validation,
        )
    except ReferencePackValidationError as exc:
        fail(f"frozen v0.1 release validation failed: {exc}")

    source_path = root / "corpus" / "index-v0.1.json"
    raw = source_path.read_bytes()
    if v01_builder.git_blob_sha(raw) != v01_builder.INDEX_BLOB:
        fail("canonical source blob does not match frozen Reference Pack identity")
    source = json.loads(raw)

    pack_dir = root / PACK_DIR_REL
    if not pack_dir.is_dir():
        fail("missing Reference Pack v0.2 directory")

    expected_members = set(builder.PACK_FILES)
    actual_members = {path.name for path in pack_dir.iterdir() if path.is_file()}
    if require_checksums:
        if actual_members != expected_members:
            fail(
                "Reference Pack v0.2 file membership mismatch: "
                f"expected {sorted(expected_members)}, got {sorted(actual_members)}"
            )
    else:
        allowed = expected_members - {"checksums.sha256"}
        if actual_members not in (allowed, expected_members):
            fail("Reference Pack v0.2 membership mismatch before checksum generation")

    expected_texts = expected_generated_texts(source)
    for name in GENERATED_FILES:
        path = pack_dir / name
        if not path.is_file():
            fail(f"missing generated v0.2 pack file: {name}")
        if path.read_text(encoding="utf-8") != expected_texts[name]:
            fail(f"generated v0.2 pack file drift: {name}")

    readme_text = (pack_dir / "README.md").read_text(encoding="utf-8")
    for required in (
        "NO_EXISTING_CLASS_MATCH",
        "SURFACED_TRAP_ADJUDICATION",
        "LATENT_TRAP_DETECTION",
        "publicly inspectable/reference material",
        "not openly licensed reusable material",
        "Issue #214",
        "Issue #327",
        "Issue #339",
    ):
        if required not in readme_text:
            fail(f"v0.2 README missing required safe-use statement: {required}")

    guide_text = (pack_dir / "failure-analysis-guide.md").read_text(
        encoding="utf-8"
    )
    for required in (
        "NO_EXISTING_CLASS_MATCH",
        "Omit rather than synthesize.",
        "docs/uses/issue339-external-failure-packet-use-2026-09-26.md",
        "PASS/FAIL",
        "publicly inspectable/reference material",
        "not as openly licensed reusable material",
    ):
        if required not in guide_text:
            fail(f"failure-analysis guide missing required contract: {required}")

    evidence_map = json.loads(
        (pack_dir / "evidence-map.json").read_text(encoding="utf-8")
    )
    if evidence_map["counts"]["issue_owners"] != v01_builder.EXPECTED_ISSUE_OWNERS:
        fail("v0.2 evidence map must contain exactly 54 issue owners")
    if evidence_map["counts"]["path_owners"] != v01_builder.EXPECTED_PATH_OWNERS:
        fail("v0.2 evidence map must contain exactly 32 repository-path owners")
    if len(evidence_map["case_links"]) != v01_builder.EXPECTED_CASES:
        fail("v0.2 evidence map must cover all 81 frozen cases")

    manifest = json.loads(
        (pack_dir / "manifest.json").read_text(encoding="utf-8")
    )
    surface = manifest.get("failure_analysis_surface", {})
    if surface.get("guide") != "failure-analysis-guide.md":
        fail("v0.2 manifest must expose the failure-analysis guide")
    if surface.get("structured_external_failure_records") is not False:
        fail("v0.2 must not claim structured external failure records")
    if surface.get("worked_use_issue") != 339:
        fail("v0.2 manifest must point to the accepted #339 worked use")

    if require_checksums:
        checksum_path = pack_dir / "checksums.sha256"
        if not checksum_path.is_file():
            fail("missing v0.2 checksums.sha256")
        if checksum_path.read_text(encoding="utf-8") != render_checksums(root):
            fail("v0.2 checksums.sha256 does not match payload bytes")

    return {
        "cases": v01_builder.EXPECTED_CASES,
        "trap_classes": v01_builder.EXPECTED_CLASSES,
        "issue_owners": v01_builder.EXPECTED_ISSUE_OWNERS,
        "path_owners": v01_builder.EXPECTED_PATH_OWNERS,
        "payload_files": len(PAYLOAD_FILES),
    }


def write_checksums(root: Path = ROOT) -> None:
    validate_pack(root, require_checksums=False)
    checksum_path = root / PACK_DIR_REL / "checksums.sha256"
    checksum_path.write_text(
        render_checksums(root),
        encoding="utf-8",
        newline="\n",
    )
    validate_pack(root, require_checksums=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write-checksums",
        action="store_true",
        help="validate v0.2 payloads, rewrite deterministic checksums, then validate",
    )
    args = parser.parse_args()

    if args.write_checksums:
        write_checksums(ROOT)
    result = validate_pack(ROOT)
    print(
        "REFERENCE_PACK_V02_VALID "
        f"cases={result['cases']} classes={result['trap_classes']} "
        f"issue_owners={result['issue_owners']} "
        f"path_owners={result['path_owners']}"
    )


if __name__ == "__main__":
    main()
