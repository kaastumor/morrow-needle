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
EVIDENCE_MAP = OUTPUT_DIR / "evidence-map.json"
CATALOG = OUTPUT_DIR / "catalog.md"

PACK_VERSION = "needle-reference-pack-v0.1"
REFERENCE_NAME = "NEEDLE_CORPUS_REFERENCE_2026-09-25"
REFERENCE_COMMIT = "c3416514e054e8c3c61ca4d42c4534eca21e1cc5"
INDEX_BLOB = "ecaab3f59fe118b71d2cafa19f05363a65ae49a1"
EXPECTED_CASES = 81
EXPECTED_CLASSES = 26
EXPECTED_ISSUE_OWNERS = 54
EXPECTED_PATH_OWNERS = 32
GITHUB_REPO = "kaastumor/morrow-needle"
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


def build_evidence_map(source: dict, cases: list[dict]) -> dict:
    issue_owners: dict[str, dict] = {}
    path_owners: dict[str, dict] = {}
    case_links = []

    for case in cases:
        refs = []
        for ref in case["evidence_refs"]:
            if ref.startswith("issue:"):
                raw_issue = ref.removeprefix("issue:")
                if not raw_issue.isdigit():
                    raise SystemExit(f"unresolvable issue evidence ref: {ref}")
                issue_number = int(raw_issue)
                owner_ref = f"issue:{issue_number}"
                owner = issue_owners.setdefault(
                    owner_ref,
                    {
                        "ref": owner_ref,
                        "issue": issue_number,
                        "url": f"https://github.com/{GITHUB_REPO}/issues/{issue_number}",
                        "case_ids": [],
                    },
                )
                owner["case_ids"].append(case["id"])
                refs.append(owner_ref)
            elif ref.startswith("path:"):
                path = ref.removeprefix("path:")
                if not path or path.startswith("/") or ".." in Path(path).parts:
                    raise SystemExit(f"unresolvable repository-path evidence ref: {ref}")
                owner_ref = f"path:{path}"
                owner = path_owners.setdefault(
                    owner_ref,
                    {
                        "ref": owner_ref,
                        "path": path,
                        "url": (
                            f"https://github.com/{GITHUB_REPO}/blob/"
                            f"{REFERENCE_COMMIT}/{path}"
                        ),
                        "case_ids": [],
                    },
                )
                owner["case_ids"].append(case["id"])
                refs.append(owner_ref)
            else:
                raise SystemExit(f"unsupported evidence ref: {ref}")
        case_links.append({"case_id": case["id"], "evidence_refs": refs})

    issues = sorted(issue_owners.values(), key=lambda owner: owner["issue"])
    paths = sorted(path_owners.values(), key=lambda owner: owner["path"])
    for owner in issues + paths:
        owner["case_ids"] = sorted(set(owner["case_ids"]))

    if len(issues) != EXPECTED_ISSUE_OWNERS:
        raise SystemExit("unexpected unique issue-owner count")
    if len(paths) != EXPECTED_PATH_OWNERS:
        raise SystemExit("unexpected unique repository-path-owner count")

    return {
        "artifact_role": "DERIVED_REFERENCE_LAYER",
        "warning": (
            "Navigation only. This file does not copy or reinterpret legal evidence; "
            "legal facts remain owned by the referenced evidence chains."
        ),
        "source": {
            "reference_commit": REFERENCE_COMMIT,
            "index_blob_sha1": INDEX_BLOB,
        },
        "counts": {
            "cases_with_evidence": len(case_links),
            "issue_owners": len(issues),
            "path_owners": len(paths),
        },
        "owners": {"issues": issues, "paths": paths},
        "case_links": case_links,
    }


def class_anchor(class_id: str) -> str:
    return "class-" + class_id.lower().replace("_", "-")


def build_catalog(source: dict, cases: list[dict]) -> str:
    lines = [
        "# Needle Reference Pack v0.1 — Corpus Catalog",
        "",
        (
            "> **Derived reference layer.** Generated from the frozen canonical corpus "
            "index. Do not edit this catalog as legal truth; legal facts remain owned "
            "by the referenced evidence chains."
        ),
        "",
        f"Source reference: `{REFERENCE_NAME}`  ",
        f"Reference commit: `{REFERENCE_COMMIT}`  ",
        f"Canonical index blob: `{INDEX_BLOB}`  ",
        (
            "Exposure rule: **all cases are exposed and REGRESSION_ONLY; none is "
            "fresh blind validation.**"
        ),
        "",
        "## Class index",
        "",
    ]

    for class_id in sorted(source["trap_classes"]):
        member_count = sum(
            class_id in case["trap_classes"] for case in cases
        )
        lines.extend(
            [
                f'<a id="{class_anchor(class_id)}"></a>',
                f"### `{class_id}`",
                "",
                source["trap_classes"][class_id],
                "",
                f"Case count: **{member_count}**",
                "",
            ]
        )

    lines.extend(["## Cases", ""])
    for case in cases:
        classes = ", ".join(
            f"[`{class_id}`](#{class_anchor(class_id)})"
            for class_id in case["trap_classes"]
        )
        provenance = case["provenance"]["role"]
        issue_number = case["provenance"].get("issue")
        if issue_number is not None:
            provenance += f" (issue:{issue_number})"
        exposure = case["exposure"]
        refs = ", ".join(f"`{ref}`" for ref in case["evidence_refs"])
        lines.extend(
            [
                f'<a id="case-{case["id"]}"></a>',
                f"### `{case['id']}` — {case['title']}",
                "",
                f"- **Domain:** {case['domain']}",
                f"- **Jurisdiction:** {case['jurisdiction']}",
                f"- **Trap classes:** {classes}",
                f"- **Provenance:** {provenance}",
                (
                    f"- **Exposure / reuse:** {exposure['status']}; "
                    f"blind reuse = `{str(exposure['blind_reuse']).lower()}`; "
                    f"future use = **{exposure['future_use']}**"
                ),
                f"- **Decisive trap:** {case['decisive_trap']}",
                f"- **Evidence refs:** {refs}",
                "",
            ]
        )

    return "\n".join(lines) + "\n"


def build_manifest(source: dict, evidence_map: dict) -> dict:
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
            "evidence_issue_owners": evidence_map["counts"]["issue_owners"],
            "evidence_path_owners": evidence_map["counts"]["path_owners"],
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
            "evidence-map.json": {
                "record_type": "evidence_owner_map",
                "issue_owners": evidence_map["counts"]["issue_owners"],
                "path_owners": evidence_map["counts"]["path_owners"],
            },
            "catalog.md": {
                "record_type": "human_catalog",
                "case_entries": EXPECTED_CASES,
                "class_entries": EXPECTED_CLASSES,
            },
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
    evidence_map = build_evidence_map(source, cases)
    write_jsonl(CASES, cases)
    write_json(CLASSES, build_classes(source, cases))
    write_json(EVIDENCE_MAP, evidence_map)
    CATALOG.write_text(build_catalog(source, cases), encoding="utf-8", newline="\n")
    write_json(MANIFEST, build_manifest(source, evidence_map))


if __name__ == "__main__":
    main()
