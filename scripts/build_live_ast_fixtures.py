#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import io
import json
from pathlib import Path
import zipfile
import xml.etree.ElementTree as ET
from typing import Any

import requests
from jsonschema import Draft202012Validator

from needle.ast.completeness import audit_text_witness
from needle.ast.formex import FormexASTParser, text_of
from needle.ast.historical_html import HistoricalHTMLASTParser


BASE = "https://publications.europa.eu/resource/celex/{celex}"


def fetch_zip(celex: str, language: str, mtype: str) -> tuple[bytes, requests.Response]:
    response = requests.get(
        BASE.format(celex=celex),
        headers={
            "Accept": f"application/zip;mtype={mtype}",
            "Accept-Language": language,
            "User-Agent": "Morrow-Needle-AST-Probe/0.1 (+https://github.com/kaastumor/morrow-needle)",
        },
        timeout=120,
        allow_redirects=True,
    )
    response.raise_for_status()
    return response.content, response


def observation_id(celex: str, payload: bytes) -> str:
    return f"live:{celex}:{hashlib.sha256(payload).hexdigest()[:16]}"


def source_meta(
    *,
    celex: str,
    representation_class: str,
    adapter: str,
    manifestation_uri: str,
    observation: str,
) -> dict[str, Any]:
    return {
        "source_observation_ids": [observation],
        "celex": celex,
        "eli": None,
        "work_uri": None,
        "expression_uri": None,
        "manifestation_uri": manifestation_uri,
        "language": "ENG",
        "representation_class": representation_class,
        "adapter": adapter,
        "adapter_version": "0.1",
        "canonicalization_profile": "whitespace-collapse-v0.1",
    }


def raw_formex_visible_text(payload: bytes) -> str:
    parts: list[str] = []
    with zipfile.ZipFile(io.BytesIO(payload)) as zf:
        for name in sorted(zf.namelist()):
            if not name.lower().endswith((".xml", ".frg")):
                continue
            try:
                root = ET.fromstring(zf.read(name))
            except ET.ParseError:
                continue
            value = text_of(root)
            if value:
                parts.append(value)
    return " ".join(parts)


def first_html_from_zip(payload: bytes) -> tuple[str, bytes]:
    with zipfile.ZipFile(io.BytesIO(payload)) as zf:
        names = sorted(
            name for name in zf.namelist()
            if name.lower().endswith((".html", ".htm", ".xhtml"))
        )
        if not names:
            raise RuntimeError("HTML/XHTML ZIP contains no HTML entry")
        name = names[0]
        return name, zf.read(name)


def build_formex(celex: str, payload: bytes, response: requests.Response) -> dict[str, Any]:
    obs = observation_id(celex, payload)
    parser = FormexASTParser(
        state_id=f"{celex}:ENG:live",
        source=source_meta(
            celex=celex,
            representation_class="STRUCTURED_LEGAL_XML",
            adapter="cellar-fmx4",
            manifestation_uri=response.url.removesuffix("/zip"),
            observation=obs,
        ),
        source_observation_id=obs,
        representation_plan_id=f"{celex}:ENG:live-plan",
    )
    ast = parser.parse_zip(payload)
    interesting_tags = {
        tag: count
        for tag, count in sorted(parser.tag_counts.items())
        if any(token in tag for token in ("ANNEX", "TABLE", "FORM", "TBL", "GR.", "TOC"))
    }
    ast["_probe"] = {
        "requested_celex": celex,
        "response_url": response.url,
        "payload_bytes": len(payload),
        "payload_sha256": hashlib.sha256(payload).hexdigest(),
        "source_tag_counts_interest": interesting_tags,
    }
    return ast


def build_html(celex: str, payload: bytes, response: requests.Response) -> dict[str, Any]:
    obs = observation_id(celex, payload)
    with zipfile.ZipFile(io.BytesIO(payload)) as zf:
        html_names = [
            name for name in zf.namelist()
            if name.lower().endswith((".html", ".htm", ".xhtml"))
        ]
        if not html_names:
            raise RuntimeError(f"{celex}: no HTML entry in Cellar ZIP")
        html_names.sort()
        name = html_names[0]
        body = zf.read(name)

    parser = HistoricalHTMLASTParser(
        state_id=f"{celex}:ENG:live",
        source=source_meta(
            celex=celex,
            representation_class="STRUCTURED_HTML",
            adapter="cellar-historical-html",
            manifestation_uri=response.url.removesuffix("/zip"),
            observation=obs,
        ),
        source_observation_id=obs,
        representation_plan_id=f"{celex}:ENG:live-plan",
    )
    ast = parser.parse(body, native_path=name)
    ast["_probe"] = {
        "requested_celex": celex,
        "response_url": response.url,
        "payload_bytes": len(payload),
        "payload_sha256": hashlib.sha256(payload).hexdigest(),
        "html_entry": name,
        "html_bytes": len(body),
    }
    return ast


def validate_ast(ast: dict[str, Any], schema: dict[str, Any]) -> list[str]:
    material = dict(ast)
    material.pop("_probe", None)
    validator = Draft202012Validator(schema)
    return [
        error.message
        for error in sorted(validator.iter_errors(material), key=lambda e: list(e.absolute_path))
    ]


def summary(ast: dict[str, Any]) -> dict[str, Any]:
    kinds: dict[str, int] = {}
    for node in ast["nodes"]:
        kinds[node["kind"]] = kinds.get(node["kind"], 0) + 1
    return {
        "state_id": ast["state_id"],
        "fidelity": ast["parse_report"]["fidelity"],
        "completeness": ast["completeness"]["state"],
        "nodes": len(ast["nodes"]),
        "segments": len(ast["segments"]),
        "references": len(ast["references"]),
        "annotations": len(ast["annotations"]),
        "node_kinds": dict(sorted(kinds.items())),
        "visible_chars_source_estimate": ast["parse_report"]["visible_chars_source_estimate"],
        "visible_chars_mapped": ast["parse_report"]["visible_chars_mapped"],
        "unknown_native_kinds": ast["parse_report"]["unknown_native_kinds"][:40],
        "warnings": ast["parse_report"]["warnings"][:20],
        "known_gaps": ast["completeness"]["known_gaps"][:20],
        "probe": ast.get("_probe", {}),
    }


LIVE_EXPECTATIONS = {
    "32004R0794": {
        "articles_min": 13,
        "paragraphs_min": 70,
        "recitals_min": 15,
        "annexes_min": 5,
        "annotations_min": 0,
        "unknown_native_exact": 0,
        "source_text_unexplained_exact": 0,
        "duplicate_claims_exact": 0,
        "mapped_not_above_source": True,
        "known_gap_contains": "raster assets",
    },
    "31958R0001": {
        "articles_exact": 8,
        "source_text_unexplained_exact": 0,
        "duplicate_claims_exact": 0,
        "mapped_equals_source": True,
        "warnings_exact": 0,
    },
    "02004R0794-20250813": {
        "articles_min": 15,
        "paragraphs_min": 80,
        "annexes_min": 8,
        "tables_min": 190,
        "table_cells_min": 1000,
        "footnotes_min": 700,
        "source_resolved_eli_refs_min": 20,
        "annotations_exact": 48,
        "unknown_native_exact": 0,
        "source_text_unexplained_exact": 0,
        "duplicate_claims_exact": 0,
        "mapped_not_above_source": True,
    },
}


def benchmark_errors(celex: str, ast: dict[str, Any]) -> list[str]:
    expected = LIVE_EXPECTATIONS.get(celex, {})
    kinds: dict[str, int] = {}
    for node in ast["nodes"]:
        kinds[node["kind"]] = kinds.get(node["kind"], 0) + 1

    errors: list[str] = []
    checks = {
        "articles": kinds.get("ARTICLE", 0),
        "paragraphs": kinds.get("PARAGRAPH", 0),
        "recitals": kinds.get("RECITAL", 0),
        "annexes": kinds.get("ANNEX", 0),
        "tables": kinds.get("TABLE", 0),
        "table_cells": kinds.get("TABLE_CELL", 0),
        "footnotes": kinds.get("FOOTNOTE", 0),
    }

    for name in ("articles", "paragraphs", "recitals", "annexes", "tables", "table_cells", "footnotes"):
        minimum = expected.get(f"{name}_min")
        exact = expected.get(f"{name}_exact")
        actual = checks[name]
        if minimum is not None and actual < minimum:
            errors.append(f"{name}: expected >= {minimum}, got {actual}")
        if exact is not None and actual != exact:
            errors.append(f"{name}: expected {exact}, got {actual}")

    unknown_exact = expected.get("unknown_native_exact")
    if unknown_exact is not None:
        actual_unknown = len(ast["parse_report"]["unknown_native_kinds"])
        if actual_unknown != unknown_exact:
            errors.append(
                f"unknown native kinds: expected {unknown_exact}, got "
                f"{actual_unknown}: {ast['parse_report']['unknown_native_kinds']}"
            )

    accounting = ast["parse_report"]["source_text_accounting"]
    unexplained_exact = expected.get("source_text_unexplained_exact")
    if unexplained_exact is not None and accounting["unexplained_chars"] != unexplained_exact:
        errors.append(
            f"unexplained source chars: expected {unexplained_exact}, "
            f"got {accounting['unexplained_chars']}"
        )
    duplicate_exact = expected.get("duplicate_claims_exact")
    if duplicate_exact is not None and accounting["duplicate_claim_count"] != duplicate_exact:
        errors.append(
            f"duplicate source claims: expected {duplicate_exact}, "
            f"got {accounting['duplicate_claim_count']}"
        )

    eli_min = expected.get("source_resolved_eli_refs_min")
    if eli_min is not None:
        actual_eli = sum(
            1
            for ref in ast["references"]
            if ref.get("source_target_uri", "").startswith("http://data.europa.eu/eli/")
            and ref.get("resolution_state") == "SOURCE_RESOLVED"
        )
        if actual_eli < eli_min:
            errors.append(
                f"source-resolved ELI references: expected >= {eli_min}, got {actual_eli}"
            )

    annotations = len(ast["annotations"])
    if "annotations_min" in expected and annotations < expected["annotations_min"]:
        errors.append(f"annotations: expected >= {expected['annotations_min']}, got {annotations}")
    if "annotations_exact" in expected and annotations != expected["annotations_exact"]:
        errors.append(f"annotations: expected {expected['annotations_exact']}, got {annotations}")

    source_chars = ast["parse_report"]["visible_chars_source_estimate"]
    mapped_chars = ast["parse_report"]["visible_chars_mapped"]
    if expected.get("mapped_not_above_source") and source_chars is not None and mapped_chars is not None:
        if mapped_chars > source_chars:
            errors.append(f"mapped chars exceed source estimate: {mapped_chars} > {source_chars}")
    if expected.get("mapped_equals_source") and source_chars != mapped_chars:
        errors.append(f"expected full visible-text recovery: {mapped_chars} != {source_chars}")

    warnings_exact = expected.get("warnings_exact")
    if warnings_exact is not None and len(ast["parse_report"]["warnings"]) != warnings_exact:
        errors.append(
            f"warnings: expected {warnings_exact}, got {len(ast['parse_report']['warnings'])}"
        )

    gap_needle = expected.get("known_gap_contains")
    if gap_needle and not any(
        gap_needle in gap.lower() for gap in ast["completeness"]["known_gaps"]
    ):
        errors.append(f"expected known gap containing {gap_needle!r}")

    return errors


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="artifacts/live-ast")
    ap.add_argument("--schema", default="schemas/legal-ast-v0.1.schema.json")
    args = ap.parse_args()

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    schema = json.loads(Path(args.schema).read_text(encoding="utf-8"))

    cases: list[tuple[str, str]] = [
        ("32004R0794", "fmx4"),
        ("31958R0001", "html"),
        ("02004R0794-20250813", "fmx4"),
    ]

    report = {"ast_version": "0.1", "cases": []}
    failed = False

    for celex, mtype in cases:
        payload, response = fetch_zip(celex, "eng", mtype)
        ast = (
            build_formex(celex, payload, response)
            if mtype == "fmx4"
            else build_html(celex, payload, response)
        )

        if celex == "32004R0794":
            witness_zip, witness_response = fetch_zip(celex, "eng", "xhtml")
            witness_name, witness_html = first_html_from_zip(witness_zip)
            raw_formex_text = raw_formex_visible_text(payload)
            raw_formex_proxy = {
                "segments": [{"text_compare": raw_formex_text}]
            }
            ast["_probe"]["xhtml_witness"] = {
                "response_url": witness_response.url,
                "entry_name": witness_name,
                "payload_bytes": len(witness_zip),
                "html_bytes": len(witness_html),
                "ast_vs_xhtml": audit_text_witness(ast, witness_html),
                "raw_formex_vs_xhtml": audit_text_witness(
                    raw_formex_proxy,
                    witness_html,
                ),
                "ast_mapping_ratio_of_raw_formex_chars": (
                    None if not raw_formex_text
                    else round(
                        ast["parse_report"]["visible_chars_mapped"] / len(raw_formex_text),
                        6,
                    )
                ),
            }

        errors = validate_ast(ast, schema)
        benchmark = benchmark_errors(celex, ast)
        case_report = summary(ast)
        case_report["schema_errors"] = errors
        case_report["benchmark_errors"] = benchmark
        report["cases"].append(case_report)

        ast_path = out / f"{celex}.ast.json"
        ast_path.write_text(json.dumps(ast, indent=2, ensure_ascii=False), encoding="utf-8")

        print(json.dumps(case_report, indent=2, ensure_ascii=False))
        if errors or benchmark:
            failed = True

    (out / "summary.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
