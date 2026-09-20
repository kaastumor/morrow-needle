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


def _source_meta(celex: str, response: requests.Response, payload: bytes) -> dict:
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
        source=_source_meta(celex, response, payload),
        source_observation_id=observation,
        representation_plan_id=f"{celex}:ENG:verification",
    )
    return parser.parse_zip(payload)


def article_subtree_state(ast: dict, citation_path: str) -> dict:
    article = next(
        node
        for node in ast["nodes"]
        if node.get("kind") == "ARTICLE"
        and node.get("citation_path") == citation_path
    )
    children: dict[str, list[str]] = {}
    for node in ast["nodes"]:
        parent = node.get("parent_id")
        if parent:
            children.setdefault(parent, []).append(node["node_id"])

    node_ids = set()
    stack = [article["node_id"]]
    while stack:
        node_id = stack.pop()
        if node_id in node_ids:
            continue
        node_ids.add(node_id)
        stack.extend(children.get(node_id, []))

    segments = sorted(
        (
            segment
            for segment in ast["segments"]
            if segment["node_id"] in node_ids
        ),
        key=lambda segment: (
            segment.get("document_order", 0),
            segment.get("ordinal", 0),
        ),
    )
    text = " ".join(
        segment.get("text_compare", segment.get("text_source", "")).strip()
        for segment in segments
        if segment.get("role") not in {"LABEL", "HEADING"}
        and segment.get("text_compare", segment.get("text_source", "")).strip()
    )
    return {
        "state_id":ast["state_id"],
        "node_id":article["node_id"],
        "text_hash":hashlib.sha256(text.encode("utf-8")).hexdigest(),
        "text_length":len(text),
    }


def article3_candidate(before_state: dict, after_state: dict) -> dict:
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
        "before":before_state,
        "after":after_state,
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
        "notes":"Live verification probe candidate built from actual consolidated Article 3 subtree hashes.",
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

    before_payload, before_response = fetch_fmx4("02004R0794-20070119")
    after_payload, after_response = fetch_fmx4("02004R0794-20080414")
    before_ast = build_ast("02004R0794-20070119", before_payload, before_response)
    after_ast = build_ast("02004R0794-20080414", after_payload, after_response)
    before_state = article_subtree_state(before_ast, "Article 3")
    after_state = article_subtree_state(after_ast, "Article 3")

    if before_state["text_hash"] == after_state["text_hash"]:
        print("ERROR: live Article 3 checkpoint subtrees are identical")
        return 1

    candidate = article3_candidate(before_state, after_state)
    reconciled = reconcile_candidate(candidate, evidence)

    result = {
        "probe_version":"0.1",
        "celex":args.celex,
        "official_resource":BASE.format(celex=args.celex),
        "final_url":response.url,
        "payload_bytes":len(payload),
        "payload_sha256":hashlib.sha256(payload).hexdigest(),
        "before_checkpoint":{
            "celex":"02004R0794-20070119",
            "payload_sha256":hashlib.sha256(before_payload).hexdigest(),
            "article3":before_state,
        },
        "after_checkpoint":{
            "celex":"02004R0794-20080414",
            "payload_sha256":hashlib.sha256(after_payload).hexdigest(),
            "article3":after_state,
        },
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
