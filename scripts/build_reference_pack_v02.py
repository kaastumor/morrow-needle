#!/usr/bin/env python3
"""Build Needle Reference Pack v0.2 from the frozen v0.1 corpus source.

v0.2 is a documentation/navigation improvement. It reuses the proven v0.1
corpus derivation functions and does not introduce new scientific data.
"""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts import build_reference_pack as v01
OUTPUT_DIR = ROOT / "release" / "needle-reference-pack-v0.2"
MANIFEST = OUTPUT_DIR / "manifest.json"
CASES = OUTPUT_DIR / "cases.jsonl"
CLASSES = OUTPUT_DIR / "classes.json"
EVIDENCE_MAP = OUTPUT_DIR / "evidence-map.json"
CATALOG = OUTPUT_DIR / "catalog.md"

PACK_VERSION = "needle-reference-pack-v0.2"
WARNING = (
    "Derived from the same frozen corpus reference as v0.1. The failure-analysis "
    "surface is method/navigation only; legal and evaluative facts remain owned by "
    "referenced evidence chains."
)
PACK_FILES = [
    "README.md",
    "failure-analysis-guide.md",
    "manifest.json",
    "cases.jsonl",
    "classes.json",
    "evidence-map.json",
    "catalog.md",
    "checksums.sha256",
]


def build_catalog(source: dict, cases: list[dict]) -> str:
    catalog = v01.build_catalog(source, cases)
    return catalog.replace(
        "# Needle Reference Pack v0.1 — Corpus Catalog",
        "# Needle Reference Pack v0.2 — Corpus Catalog",
        1,
    )


def build_manifest(source: dict, evidence_map: dict) -> dict:
    manifest = v01.build_manifest(source, evidence_map)
    manifest["pack_version"] = PACK_VERSION
    manifest["warning"] = WARNING
    manifest["failure_analysis_surface"] = {
        "guide": "failure-analysis-guide.md",
        "structured_external_failure_records": False,
        "worked_use_issue": 339,
        "worked_use_owner": (
            "docs/uses/issue339-external-failure-packet-use-2026-09-26.md"
        ),
    }
    manifest["generated_outputs"]["checksums.sha256"]["payload_files"] = 7
    manifest["generation_contract"]["builder"] = (
        "scripts/build_reference_pack_v02.py"
    )
    manifest["generation_contract"]["planned_pack_files"] = PACK_FILES
    return manifest


def main() -> None:
    source, _ = v01.load_source()
    cases = v01.sorted_cases(source)
    evidence_map = v01.build_evidence_map(source, cases)

    v01.write_jsonl(CASES, cases)
    v01.write_json(CLASSES, v01.build_classes(source, cases))
    v01.write_json(EVIDENCE_MAP, evidence_map)
    CATALOG.parent.mkdir(parents=True, exist_ok=True)
    CATALOG.write_text(
        build_catalog(source, cases),
        encoding="utf-8",
        newline="\n",
    )
    v01.write_json(MANIFEST, build_manifest(source, evidence_map))


if __name__ == "__main__":
    main()
