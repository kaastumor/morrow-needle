#!/usr/bin/env python3
"""Validate the frozen Needle Reference Pack and its deterministic checksums."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from scripts import build_reference_pack as builder
from scripts.validate_adversarial_corpus import (
    CorpusValidationError,
    validate as validate_corpus,
)

ROOT = Path(__file__).resolve().parents[1]
PACK_DIR_REL = Path("release") / "needle-reference-pack-v0.1"
PAYLOAD_FILES = sorted(
    [
        "README.md",
        "manifest.json",
        "cases.jsonl",
        "classes.json",
        "evidence-map.json",
        "catalog.md",
    ]
)
GENERATED_FILES = [
    "manifest.json",
    "cases.jsonl",
    "classes.json",
    "evidence-map.json",
    "catalog.md",
]


class ReferencePackValidationError(ValueError):
    pass


def fail(message: str) -> None:
    raise ReferencePackValidationError(message)


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
        cases = builder.sorted_cases(source)
        classes = builder.build_classes(source, cases)
        evidence_map = builder.build_evidence_map(source, cases)
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
    source_path = root / "corpus" / "index-v0.1.json"
    pack_dir = root / PACK_DIR_REL

    if not source_path.is_file():
        fail("missing canonical corpus index")
    raw = source_path.read_bytes()
    if builder.git_blob_sha(raw) != builder.INDEX_BLOB:
        fail("canonical source blob does not match frozen Reference Pack identity")

    source = json.loads(raw)
    if source.get("status") != "CANONICAL_REFERENCE":
        fail("canonical corpus is not in CANONICAL_REFERENCE state")
    if len(source.get("cases", [])) != builder.EXPECTED_CASES:
        fail("Reference Pack requires exactly 81 canonical cases")
    if len(source.get("trap_classes", {})) != builder.EXPECTED_CLASSES:
        fail("Reference Pack requires exactly 26 canonical trap classes")

    if run_canonical_validation:
        try:
            validate_corpus(source, root)
        except CorpusValidationError as exc:
            fail(f"canonical corpus validation failed: {exc}")

    case_ids = [case.get("id") for case in source["cases"]]
    if len(set(case_ids)) != builder.EXPECTED_CASES:
        fail("case IDs are not unique")

    class_ids = set(source["trap_classes"])
    used_classes: set[str] = set()
    for case in source["cases"]:
        refs = set(case.get("trap_classes", []))
        unknown = refs - class_ids
        if unknown:
            fail(f"case {case.get('id')} references unknown trap classes: {sorted(unknown)}")
        used_classes.update(refs)
        exposure = case.get("exposure", {})
        if exposure.get("blind_reuse") is not False:
            fail(f"case {case.get('id')} must remain blind_reuse=false")
        if exposure.get("future_use") != "REGRESSION_ONLY":
            fail(f"case {case.get('id')} must remain REGRESSION_ONLY")
    if used_classes != class_ids:
        fail("every canonical trap class must remain represented")

    if not pack_dir.is_dir():
        fail("missing Reference Pack directory")
    expected_members = set(builder.PACK_FILES)
    actual_members = {path.name for path in pack_dir.iterdir() if path.is_file()}
    if require_checksums:
        if actual_members != expected_members:
            fail(
                "Reference Pack file membership mismatch: "
                f"expected {sorted(expected_members)}, got {sorted(actual_members)}"
            )
    else:
        allowed = expected_members - {"checksums.sha256"}
        if actual_members not in (allowed, expected_members):
            fail("Reference Pack file membership mismatch before checksum generation")

    expected_texts = expected_generated_texts(source)
    for name in GENERATED_FILES:
        path = pack_dir / name
        if not path.is_file():
            fail(f"missing generated pack file: {name}")
        actual = path.read_text(encoding="utf-8")
        if actual != expected_texts[name]:
            fail(f"generated pack file drift: {name}")

    readme = pack_dir / "README.md"
    if not readme.is_file():
        fail("missing Reference Pack README")
    readme_text = readme.read_text(encoding="utf-8")
    for required in (
        "REGRESSION_ONLY",
        "SURFACED_TRAP_ADJUDICATION",
        "LATENT_TRAP_DETECTION",
        "NO DIAGNOSTIC VALUE DEMONSTRATED / SIMPLIFY",
    ):
        if required not in readme_text:
            fail(f"README missing required safe-use statement: {required}")

    evidence_map = json.loads((pack_dir / "evidence-map.json").read_text(encoding="utf-8"))
    if evidence_map["counts"]["issue_owners"] != builder.EXPECTED_ISSUE_OWNERS:
        fail("evidence map must contain exactly 54 issue owners")
    if evidence_map["counts"]["path_owners"] != builder.EXPECTED_PATH_OWNERS:
        fail("evidence map must contain exactly 32 repository-path owners")
    if len(evidence_map["case_links"]) != builder.EXPECTED_CASES:
        fail("evidence map must cover all 81 cases")

    if require_checksums:
        checksum_path = pack_dir / "checksums.sha256"
        if not checksum_path.is_file():
            fail("missing checksums.sha256")
        expected_checksums = render_checksums(root)
        actual_checksums = checksum_path.read_text(encoding="utf-8")
        if actual_checksums != expected_checksums:
            fail("checksums.sha256 does not match pack payload bytes")

    return {
        "cases": builder.EXPECTED_CASES,
        "trap_classes": builder.EXPECTED_CLASSES,
        "issue_owners": builder.EXPECTED_ISSUE_OWNERS,
        "path_owners": builder.EXPECTED_PATH_OWNERS,
        "payload_files": len(PAYLOAD_FILES),
    }


def write_checksums(root: Path = ROOT) -> None:
    validate_pack(root, require_checksums=False)
    checksum_path = root / PACK_DIR_REL / "checksums.sha256"
    checksum_path.write_text(render_checksums(root), encoding="utf-8", newline="\n")
    validate_pack(root, require_checksums=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write-checksums",
        action="store_true",
        help="validate payload files, rewrite deterministic checksums, then validate again",
    )
    args = parser.parse_args()

    if args.write_checksums:
        write_checksums(ROOT)
    result = validate_pack(ROOT)
    print(
        "REFERENCE_PACK_VALID "
        f"cases={result['cases']} classes={result['trap_classes']} "
        f"issue_owners={result['issue_owners']} path_owners={result['path_owners']}"
    )


if __name__ == "__main__":
    main()
