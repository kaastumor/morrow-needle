#!/usr/bin/env python3
"""Build the derived Needle Reference Pack from the canonical corpus index.

The pack is a reference/use surface only. Legal facts remain owned by the
evidence chains referenced from corpus/index-v0.1.json.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "corpus" / "index-v0.1.json"
OUTPUT_DIR = ROOT / "release" / "needle-reference-pack-v0.1"
MANIFEST = OUTPUT_DIR / "manifest.json"

PACK_VERSION = "needle-reference-pack-v0.1"
REFERENCE_NAME = "NEEDLE_CORPUS_REFERENCE_2026-09-25"
REFERENCE_COMMIT = "c3416514e054e8c3c61ca4d42c4534eca21e1cc5"
INDEX_BLOB = "ecaab3f59fe118b71d2cafa19f05363a65ae49a1"
EXPECTED_CASES = 81
EXPECTED_CLASSES = 26

PACK_FILES = [
    "README.md",
    "manifest.json",
    "cases.jsonl",
    "classes.json",
    "evidence-map.json",
    "catalog.md",
    "checksums.sha256",
]


def git_blob_sha(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def load_source() -> tuple[dict, bytes]:
    raw = SOURCE.read_bytes()
    if git_blob_sha(raw) != INDEX_BLOB:
        raise SystemExit("canonical corpus index blob does not match frozen reference")
    data = json.loads(raw)
    if data.get("status") != "CANONICAL_REFERENCE":
        raise SystemExit("corpus index is not CANONICAL_REFERENCE")
    if len(data.get("cases", [])) != EXPECTED_CASES:
        raise SystemExit("frozen case count changed")
    if len(data.get("trap_classes", {})) != EXPECTED_CLASSES:
        raise SystemExit("frozen trap-class count changed")
    return data, raw


def build_manifest(source: dict) -> dict:
    exposures = {
        (
            case.get("exposure", {}).get("status"),
            case.get("exposure", {}).get("blind_reuse"),
            case.get("exposure", {}).get("future_use"),
        )
        for case in source["cases"]
    }
    expected_exposure = {("PUBLIC_FROM_DISCOVERY", False, "REGRESSION_ONLY"),
                         ("PUBLIC_AFTER_EVALUATION", False, "REGRESSION_ONLY")}
    if not exposures or not exposures.issubset(expected_exposure):
        raise SystemExit("unexpected exposure/reuse state in frozen corpus")

    return {
        "pack_version": PACK_VERSION,
        "artifact_role": "DERIVED_REFERENCE_LAYER",
        "warning": (
            "Generated from corpus/index-v0.1.json. Do not edit this pack as legal "
            "truth; legal facts remain owned by referenced evidence chains."
        ),
        "source": {
            "reference_name": REFERENCE_NAME,
            "reference_commit": REFERENCE_COMMIT,
            "index_path": "corpus/index-v0.1.json",
            "index_blob_sha1": INDEX_BLOB,
            "schema_version": source["schema_version"],
            "status": source["status"],
        },
        "counts": {
            "cases": len(source["cases"]),
            "trap_classes": len(source["trap_classes"]),
        },
        "exposure_policy": {
            "all_cases_exposed": True,
            "blind_reuse": False,
            "future_use": "REGRESSION_ONLY",
            "fresh_blind_validation": (
                "Requires a new independently selected and sealed case."
            ),
        },
        "generation_contract": {
            "builder": "scripts/build_reference_pack.py",
            "runtime": "Python standard library only",
            "canonical_membership_owner": "corpus/index-v0.1.json",
            "determinism": (
                "UTF-8, LF text, JSON keys sorted where object order is not semantic, "
                "stable source-derived ordering, no timestamps or environment data."
            ),
            "network_required": False,
            "planned_pack_files": PACK_FILES,
        },
    }


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    path.write_text(text, encoding="utf-8", newline="\n")


def main() -> None:
    source, _ = load_source()
    write_json(MANIFEST, build_manifest(source))


if __name__ == "__main__":
    main()
