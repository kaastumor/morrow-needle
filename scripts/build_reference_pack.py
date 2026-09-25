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
CASES = OUTPUT_DIR / "cases.jsonl"
CLASSES = OUTPUT_DIR / "classes.json"

PACK_VERSION = "needle-reference-pack-v0.1"
REFERENCE_NAME = "NEEDLE_CORPUS_REFERENCE_2026-09-25"
REFERENCE_COMMIT = "c3416514e054e8c3c61ca4d42c4534eca21e1cc5"
INDEX_BLOB = "ecaab3f59fe118b71d2cafa19f05363a65ae49a1"
EXPECTED_CASES = 81
EXPECTED_CLASSES = 26
WARNING = (
    "Generated from corpus/index-v0.1.json. Do not edit this pack as legal truth; "
    "legal facts remain owned by referenced evidence chains."
)

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


def sorted_cases(source: dict) -> list[dict]:
    cases = sorted(source["cases"], key=lambda case: case["id"])
    if len({case["id"] for case in cases}) != EXPECTED_CASES:
        raise SystemExit("case IDs are not unique")
    return cases


def build_classes(source: dict, cases: list[dict]) -> dict:
    classes = []
    for class_id in sorted(source["trap_classes"]):
        case_ids = sorted(
            case["id"] for case in cases if class_id in case["trap_classes"]
        )
        if not case_ids:
            raise SystemExit(f"trap class has no case membership: {class_id}")
        classes.append(
            {
                "id": class_id,
                "definition": source["trap_classes"][class_id],
                "case_count": len(case_ids),
                "case_ids": case_ids,
            }
        )
    return {
        "artifact_role": "DERIVED_REFERENCE_LAYER",
        "warning": WARNING,
        "classes": classes,
    }


def build_manifest(source: dict) -> dict:
    exposures = {
        (
            case.get("exposure", {}).get("status"),
            case.get("exposure", {}).get("blind_reuse"),
            case.get("exposure", {}).get("future_use"),
        )
        for case in source["cases"]
    }
    expected_exposure = {
        ("PUBLIC_FROM_DISCOVERY", False, "REGRESSION_ONLY"),
        ("PUBLIC_AFTER_EVALUATION", False, "REGRESSION_ONLY"),
    }
    if not exposures or not exposures.issubset(expected_exposure):
        raise SystemExit("unexpected exposure/reuse state in frozen corpus")

    return {
        "pack_version": PACK_VERSION,
        "artifact_role": "DERIVED_REFERENCE_LAYER",
        "warning": WARNING,
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
        "generated_outputs": {
            "cases.jsonl": {"record_type": "case", "records": EXPECTED_CASES},
            "classes.json": {"record_type": "trap_class", "records": EXPECTED_CLASSES},
        },
        "generation_contract": {
            "builder": "scripts/build_reference_pack.py",
            "runtime": "Python standard library only",
            "canonical_membership_owner": "corpus/index-v0.1.json",
            "determinism": (
                "UTF-8, LF text, JSON object keys sorted, case/class IDs sorted, "
                "no timestamps or environment data."
            ),
            "network_required": False,
            "planned_pack_files": PACK_FILES,
        },
    }


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    path.write_text(text, encoding="utf-8", newline="\n")


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = "".join(
        json.dumps(
            row,
            sort_keys=True,
            ensure_ascii=False,
            separators=(",", ":"),
        )
        + "\n"
        for row in rows
    )
    path.write_text(text, encoding="utf-8", newline="\n")


def main() -> None:
    source, _ = load_source()
    cases = sorted_cases(source)
    write_jsonl(CASES, cases)
    write_json(CLASSES, build_classes(source, cases))
    write_json(MANIFEST, build_manifest(source))


if __name__ == "__main__":
    main()
