#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import io
import json
from pathlib import Path
import zipfile
import xml.etree.ElementTree as ET

import requests

from needle.ast.formex import FormexASTParser
from needle.mutation.diff import diff_target_subtree
from needle.mutation.instructions import parse_authentic_instructions
from needle.mutation.reconcile import reconcile_candidate


BASE = "https://publications.europa.eu/resource/celex/{celex}"
EVIDENCE_FIXTURE = Path(
    "fixtures/mutations/reg794-article3-replacement-evidence-v0.1.json"
)


def fetch_fmx4(celex: str, language: str = "eng") -> tuple[bytes, requests.Response]:
    response = requests.get(
        BASE.format(celex=celex),
        headers={
            "Accept": "application/zip;mtype=fmx4",
            "Accept-Language": language,
            "User-Agent": (
                "Morrow-Needle-Authentic-Amendment-Probe/0.1 "
                "(+https://github.com/kaastumor/morrow-needle)"
            ),
        },
        timeout=120,
        allow_redirects=True,
    )
    response.raise_for_status()
    return response.content, response


def normalized_visible_text(xml_bytes: bytes) -> str:
    root = ET.fromstring(xml_bytes)
    return " ".join("".join(root.itertext()).split())


def extract_evidence(payload: bytes, celex: str) -> list[dict]:
    evidence: list[dict] = []
    with zipfile.ZipFile(io.BytesIO(payload)) as zf:
        for name in sorted(zf.namelist()):
            if not name.lower().endswith((".xml", ".frg")):
                continue
            try:
                text = normalized_visible_text(zf.read(name))
            except ET.ParseError:
                continue
            evidence.extend(
                parse_authentic_instructions(
                    text,
                    source_id=f"CELEX:{celex}",
                    locator=name,
                    include_match_span=True,
                )
            )
    return evidence


def source_meta(celex: str, response: requests.Response, payload: bytes) -> dict:
    observation = f"live:{celex}:{hashlib.sha256(payload).hexdigest()[:16]}"
    return {
        "source_observation_ids":[observation],
        "celex":celex,
        "eli":None,
        "work_uri":None,
        "expression_uri":None,
        "manifestation_uri":response.url.removesuffix("/zip"),
        "language":"ENG",
        "representation_class":"STRUCTURED_LEGAL_XML",
        "adapter":"cellar-fmx4",
        "adapter_version":"0.1",
        "canonicalization_profile":"whitespace-collapse-v0.1",
    }


def build_ast(celex: str, payload: bytes, response: requests.Response) -> dict:
    observation = f"live:{celex}:{hashlib.sha256(payload).hexdigest()[:16]}"
    parser = FormexASTParser(
        state_id=f"CELEX:{celex}",
        source=source_meta(celex, response, payload),
        source_observation_id=observation,
        representation_plan_id=f"{celex}:ENG:verification",
    )
    return parser.parse_zip(payload)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--celex", default="32008R0271")
    ap.add_argument(
        "--out",
        default="artifacts/authentic-amendment/32008R0271.json",
    )
    args = ap.parse_args()

    # 1. Retrieve and parse the authentic legal cause.
    payload, response = fetch_fmx4(args.celex)
    authentic_evidence = extract_evidence(payload, args.celex)
    article3_authentic = [
        item
        for item in authentic_evidence
        if item["operation"] == "REPLACE"
        and item["target_locator"] == "Article 3"
    ]

    # 2. Retrieve the real official before/after text states.
    before_payload, before_response = fetch_fmx4("02004R0794-20070119")
    after_payload, after_response = fetch_fmx4("02004R0794-20080414")
    before_ast = build_ast(
        "02004R0794-20070119",
        before_payload,
        before_response,
    )
    after_ast = build_ast(
        "02004R0794-20080414",
        after_payload,
        after_response,
    )

    # 3. Let the generic deterministic engine create the Article-level
    #    comparator candidate selected by official affected-subdivision metadata.
    candidate = diff_target_subtree(
        before_ast,
        after_ast,
        kind="ARTICLE",
        citation_path="Article 3",
        language="ENG",
    )
    if candidate is None:
        print("ERROR: deterministic engine found no Article 3 subtree mutation")
        return 1
    if candidate["operation"] != "REPLACE":
        print(f"ERROR: expected Article 3 REPLACE, got {candidate['operation']}")
        return 1

    # 4. Reconcile deterministic output against independent official channels
    #    plus the live authentic legal cause.
    fixture = json.loads(EVIDENCE_FIXTURE.read_text(encoding="utf-8"))
    corroborating = fixture["evidence"]
    reconciled = reconcile_candidate(
        candidate,
        corroborating + authentic_evidence,
    )

    result = {
        "probe_version":"0.2",
        "celex":args.celex,
        "official_resource":BASE.format(celex=args.celex),
        "final_url":response.url,
        "payload_bytes":len(payload),
        "payload_sha256":hashlib.sha256(payload).hexdigest(),
        "before_checkpoint":{
            "celex":"02004R0794-20070119",
            "payload_sha256":hashlib.sha256(before_payload).hexdigest(),
            "article3":candidate["before"],
        },
        "after_checkpoint":{
            "celex":"02004R0794-20080414",
            "payload_sha256":hashlib.sha256(after_payload).hexdigest(),
            "article3":candidate["after"],
        },
        "deterministic_candidate":candidate,
        "authentic_instruction_count":len(authentic_evidence),
        "article3_authentic_evidence":article3_authentic,
        "reconciled_article3":reconciled,
    }

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        json.dumps(result, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))

    if len(article3_authentic) != 1:
        print(
            "ERROR: expected exactly one authentic Article 3 replacement, "
            f"got {len(article3_authentic)}"
        )
        return 1
    if not article3_authentic[0].get("locator"):
        print("ERROR: authentic Article 3 replacement lacks source locator")
        return 1
    if candidate.get("comparison_scope") != "SUBTREE":
        print("ERROR: live candidate was not generated by subtree comparator")
        return 1
    if candidate["before"]["text_hash"] == candidate["after"]["text_hash"]:
        print("ERROR: live Article 3 checkpoint subtrees are identical")
        return 1
    if reconciled["reconciliation_state"] != "CORROBORATED":
        print("ERROR: Article 3 did not remain corroborated")
        return 1
    if reconciled["verification_state"] != "VERIFIED":
        print("ERROR: authentic legal cause did not cross VERIFIED gate")
        return 1
    if reconciled["conflicting_evidence"]:
        print("ERROR: verified Article 3 mutation has conflicting evidence")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
