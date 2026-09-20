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

from needle.mutation.instructions import parse_authentic_instructions
from needle.mutation.reconcile import reconcile_candidate


BASE = "https://publications.europa.eu/resource/celex/{celex}"


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


def article3_candidate() -> dict:
    return {
        "candidate_id":"reg794-art3-replace-live-verification",
        "operation":"REPLACE",
        "target":{
            "kind":"ARTICLE",
            "citation_path":"Article 3",
            "parent_citation_path":None,
            "language":"ENG",
        },
        "alignment_basis":"EXACT_CITATION_AND_KIND",
        "before":{
            "state_id":"CELEX:02004R0794-20070119",
            "node_id":"Article 3@20070119",
            "text_hash":"0" * 64,
            "text_length":0,
        },
        "after":{
            "state_id":"CELEX:02004R0794-20080414",
            "node_id":"Article 3@20080414",
            "text_hash":"1" * 64,
            "text_length":0,
        },
        "feature_deltas":{
            "numbers_added":[],"numbers_removed":[],
            "dates_added":[],"dates_removed":[],
            "references_added":[],"references_removed":[],
        },
        "reconciliation_state":"CORROBORATED",
        "verification_state":"UNVERIFIED",
        "supporting_evidence":[
            {
                "channel":"DETERMINISTIC_DIFF",
                "source_id":"02004R0794-20070119->02004R0794-20080414",
                "operation":"REPLACE",
                "target_locator":"Article 3",
                "authority_character":"DERIVED",
                "locator":None,
            },
            {
                "channel":"RELATIONSHIP_METADATA",
                "source_id":"CELEX:32004R0794",
                "operation":"REPLACE",
                "target_locator":"Article 3",
                "authority_character":"OFFICIAL_STRUCTURED_METADATA",
                "locator":"Modified by 32008R0271 / Replacement / article 3",
            },
            {
                "channel":"CONSOLIDATION_PROVENANCE",
                "source_id":"CELEX:02004R0794-20250813",
                "operation":"REPLACE",
                "target_locator":"Article 3",
                "authority_character":"DOCUMENTARY_NON_BINDING",
                "locator":"CLG.MDFO O003001M001000; ACTIVE.DOC=32008R0271",
            },
        ],
        "conflicting_evidence":[],
        "notes":"Live verification probe candidate; hashes are not used by reconciliation.",
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--celex", default="32008R0271")
    ap.add_argument("--out", default="artifacts/authentic-amendment/32008R0271.json")
    args = ap.parse_args()

    payload, response = fetch_fmx4(args.celex)
    evidence = extract_evidence(payload, args.celex)
    article3 = [
        item
        for item in evidence
        if item["operation"] == "REPLACE"
        and item["target_locator"] == "Article 3"
    ]

    candidate = article3_candidate()
    reconciled = reconcile_candidate(candidate, evidence)

    result = {
        "probe_version":"0.1",
        "celex":args.celex,
        "official_resource":BASE.format(celex=args.celex),
        "final_url":response.url,
        "payload_bytes":len(payload),
        "payload_sha256":hashlib.sha256(payload).hexdigest(),
        "authentic_instruction_count":len(evidence),
        "article3_authentic_evidence":article3,
        "reconciled_article3":reconciled,
    }

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))

    if len(article3) != 1:
        print(f"ERROR: expected exactly one authentic Article 3 replacement, got {len(article3)}")
        return 1
    if not article3[0].get("locator"):
        print("ERROR: authentic Article 3 replacement lacks source locator")
        return 1
    if reconciled["reconciliation_state"] != "CORROBORATED":
        print("ERROR: Article 3 did not remain corroborated")
        return 1
    if reconciled["verification_state"] != "VERIFIED":
        print("ERROR: authentic legal cause did not cross VERIFIED gate")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
