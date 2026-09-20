#!/usr/bin/env python3
from __future__ import annotations

import hashlib
from html.parser import HTMLParser
import io
import json
from pathlib import Path
import zipfile
import xml.etree.ElementTree as ET

import requests

from needle.ast.formex import FormexASTParser
from needle.mutation.diff import diff_resolved_subtree
from needle.mutation.instructions import parse_authentic_instructions
from needle.mutation.reconcile import reconcile_candidate


BASE = "https://publications.europa.eu/resource/celex/{celex}"
CAUSE = "32025R0905"
CORRIGENDUM = "32025R0905R(01)"
CORRIGENDUM_HTML = (
    "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/"
    "?uri=CELEX%3A32025R0905R%2801%29"
)
BEFORE = "02004R0794-20161222"
AFTER = "02004R0794-20250703"
TARGET = "Article 3 > 3"
SENTENCES = {
    "amendment-instruction": (
        "Article 3, paragraph 3 is replaced by the following"
    ),
    "notification-channel": (
        "Notifications shall be sent electronically, via the electronic "
        "application designated by the Commission."
    ),
    "correspondence-channel": (
        "All correspondence in connection with a notification shall be sent "
        "electronically via the secured electronic system designated by the Commission."
    ),
    "entry-into-force": (
        "This Regulation shall enter into force on the twentieth day following "
        "that of its publication in the Official Journal of the European Union."
    ),
}


def fetch_fmx4(celex: str) -> tuple[bytes, requests.Response]:
    response = requests.get(
        BASE.format(celex=celex),
        headers={
            "Accept":"application/zip;mtype=fmx4",
            "Accept-Language":"eng",
            "User-Agent":(
                "Morrow-Needle-Thread-2025-Probe/0.1 "
                "(+https://github.com/kaastumor/morrow-needle)"
            ),
        },
        timeout=120,
        allow_redirects=True,
    )
    response.raise_for_status()
    return response.content,response


def normalized_visible_text(xml_bytes: bytes) -> str:
    root=ET.fromstring(xml_bytes)
    return " ".join("".join(root.itertext()).split())


class _VisibleHTML(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts=[]

    def handle_data(self,data: str) -> None:
        self.parts.append(data)


def fetch_corrigendum_html() -> tuple[bytes,requests.Response,str]:
    response=requests.get(
        CORRIGENDUM_HTML,
        headers={
            "Accept":"text/html",
            "Accept-Language":"en",
            "User-Agent":(
                "Morrow-Needle-Thread-Corrigendum-Probe/0.1 "
                "(+https://github.com/kaastumor/morrow-needle)"
            ),
        },
        timeout=120,
        allow_redirects=True,
    )
    response.raise_for_status()
    media_type=response.headers.get("Content-Type","").split(";",1)[0].lower()
    if media_type not in {"text/html","application/xhtml+xml"}:
        raise AssertionError(f"unexpected corrigendum media type: {media_type}")
    parser=_VisibleHTML()
    parser.feed(response.text)
    return response.content,response," ".join(" ".join(parser.parts).split())


def source_meta(celex,response,payload):
    observation=f"live:{celex}:{hashlib.sha256(payload).hexdigest()[:16]}"
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


def build_ast(celex,payload,response):
    observation=f"live:{celex}:{hashlib.sha256(payload).hexdigest()[:16]}"
    return FormexASTParser(
        state_id=f"CELEX:{celex}",
        source=source_meta(celex,response,payload),
        source_observation_id=observation,
        representation_plan_id=f"{celex}:ENG:thread-2025",
    ).parse_zip(payload)


def all_visible_text(payload: bytes) -> str:
    parts=[]
    with zipfile.ZipFile(io.BytesIO(payload)) as zf:
        for name in sorted(zf.namelist()):
            if not name.lower().endswith((".xml",".frg")):
                continue
            try:
                parts.append(normalized_visible_text(zf.read(name)))
            except ET.ParseError:
                continue
    return " ".join(parts)


def authentic_evidence_and_spans(payload: bytes):
    evidence=[]
    spans={}
    with zipfile.ZipFile(io.BytesIO(payload)) as zf:
        for name in sorted(zf.namelist()):
            if not name.lower().endswith((".xml",".frg")):
                continue
            try:
                text=normalized_visible_text(zf.read(name))
            except ET.ParseError:
                continue
            evidence.extend(
                parse_authentic_instructions(
                    text,
                    source_id=f"CELEX:{CAUSE}",
                    locator=name,
                    include_match_span=True,
                )
            )
            for span_id,sentence in SENTENCES.items():
                pos=text.find(sentence)
                if pos < 0:
                    continue
                spans.setdefault(span_id,[]).append({
                    "identifier":f"CELEX:{CAUSE}",
                    "source_file":name,
                    "locator":f"{name}#normalized-chars:{pos}-{pos+len(sentence)}",
                    "language":"ENG",
                    "text":sentence,
                    "text_hash":hashlib.sha256(sentence.encode("utf-8")).hexdigest(),
                })
    return evidence,spans


def main() -> int:
    cause_payload,cause_response=fetch_fmx4(CAUSE)
    before_payload,before_response=fetch_fmx4(BEFORE)
    after_payload,after_response=fetch_fmx4(AFTER)
    # Publications Office CELEX dereferencing currently returns 404 for this
    # parenthesised corrigendum identifier. Verify against the official EUR-Lex
    # representation instead; keep the source class explicit in the artifact.
    corrigendum_payload,corrigendum_response,corrigendum_text=(
        fetch_corrigendum_html()
    )

    evidence,spans=authentic_evidence_and_spans(cause_payload)
    authentic=[
        item for item in evidence
        if item["operation"]=="REPLACE"
        and item["target_locator"]==TARGET
    ]

    before_ast=build_ast(BEFORE,before_payload,before_response)
    after_ast=build_ast(AFTER,after_payload,after_response)
    candidate=diff_resolved_subtree(
        before_ast,
        after_ast,
        structural_path=[("ARTICLE","3"),("PARAGRAPH","3")],
        canonical_kind="PARAGRAPH",
        canonical_citation_path=TARGET,
        language="ENG",
    )
    if candidate is None:
        raise AssertionError("no deterministic Article 3(3) mutation")
    if candidate["operation"]!="REPLACE":
        raise AssertionError(f"unexpected operation: {candidate['operation']}")

    corroboration=[{
        "channel":"CONSOLIDATION_PROVENANCE",
        "source_id":"CELEX:02004R0794-20250813",
        "operation":"REPLACE",
        "target_locator":TARGET,
        "authority_character":"DOCUMENTARY_NON_BINDING",
        "locator":"CLG.MDFO O011001M003000; ACTIVE.DOC=32025R0905; ACTIVE.LOC=AR:1;PT:3",
    }]
    reconciled=reconcile_candidate(candidate,corroboration+evidence)

    for span_id in SENTENCES:
        matches=spans.get(span_id,[])
        if len(matches)!=1:
            raise AssertionError(
                f"{span_id}: expected one authentic sentence, got {len(matches)}"
            )
    if len(authentic)!=1:
        raise AssertionError(
            f"expected one authentic Article 3 > 3 replacement, got {len(authentic)}"
        )
    if reconciled["verification_state"]!="VERIFIED":
        raise AssertionError("Article 3(3) did not cross VERIFIED gate")
    if reconciled["conflicting_evidence"]:
        raise AssertionError("Article 3(3) has conflicting evidence")

    corrigendum_target="in the amendment to Article 4(1), second sentence"
    if corrigendum_text.count(corrigendum_target)!=1:
        raise AssertionError(
            "corrigendum does not uniquely target Article 4(1), second sentence"
        )
    if "Article 3" in corrigendum_text:
        raise AssertionError("corrigendum unexpectedly contains an Article 3 target")

    result={
        "probe_version":"0.1",
        "cause":{
            "celex":CAUSE,
            "payload_sha256":hashlib.sha256(cause_payload).hexdigest(),
            "final_url":cause_response.url,
        },
        "before":{
            "celex":BEFORE,
            "payload_sha256":hashlib.sha256(before_payload).hexdigest(),
            "final_url":before_response.url,
            "state":candidate["before"],
        },
        "after":{
            "celex":AFTER,
            "payload_sha256":hashlib.sha256(after_payload).hexdigest(),
            "final_url":after_response.url,
            "state":candidate["after"],
        },
        "candidate":candidate,
        "authentic_instruction":authentic[0],
        "source_spans":{
            key:value[0] for key,value in spans.items()
        },
        "semantic_spans":{
            key:spans[key][0]
            for key in ("notification-channel","correspondence-channel")
        },
        "reconciled":reconciled,
        "temporal":{
            "publication_date":"2025-06-13",
            "entry_into_force":"2025-07-03",
            "article3_3_special_deferred_application":False,
            "special_2025_08_13_clause_applies_only_to":"Annex I / Part I / point 6.8",
        },
        "corrigendum_32025R0905R01":{
            "celex":CORRIGENDUM,
            "publication_date":"2026-07-17",
            "payload_sha256":hashlib.sha256(corrigendum_payload).hexdigest(),
            "final_url":corrigendum_response.url,
            "source_type":"EUR_LEX",
            "representation_class":"OFFICIAL_HTML",
            "cellar_celex_dereference":"UNAVAILABLE_404",
            "target_evidence":corrigendum_target,
            "targets":"Article 4(1), second sentence",
            "article3_effect":"NONE",
            "verification_basis":"LIVE_AUTHENTIC_CORRIGENDUM_TARGET",
        },
    }

    out=Path("artifacts/thread-2025/article3-2025.json")
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding="utf-8")
    print(json.dumps(result,indent=2,ensure_ascii=False))
    return 0


if __name__=="__main__":
    raise SystemExit(main())
