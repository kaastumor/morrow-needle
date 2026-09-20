#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

import requests
from jsonschema import Draft202012Validator

from needle.ast.formex import FormexASTParser
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
    ast["_probe"] = {
        "requested_celex": celex,
        "response_url": response.url,
        "payload_bytes": len(payload),
        "payload_sha256": hashlib.sha256(payload).hexdigest(),
    }
    return ast


def build_html(celex: str, payload: bytes, response: requests.Response) -> dict[str, Any]:
    import io
    import zipfile

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
        errors = validate_ast(ast, schema)
        case_report = summary(ast)
        case_report["schema_errors"] = errors
        report["cases"].append(case_report)

        ast_path = out / f"{celex}.ast.json"
        ast_path.write_text(json.dumps(ast, indent=2, ensure_ascii=False), encoding="utf-8")

        print(json.dumps(case_report, indent=2, ensure_ascii=False))
        if errors:
            failed = True

    (out / "summary.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
