#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import io
import json
from pathlib import Path
import re
import zipfile
import xml.etree.ElementTree as ET

import requests

from needle.ast.formex import FormexASTParser
from needle.ast.resolve import resolve_structural_path
from needle.mutation.diff import diff_resolved_subtree


BASE="https://publications.europa.eu/resource/celex/{celex}"
CAUSE="32023R2055"
BEFORE="02006R1907-20230806"
AFTER_CANDIDATES=[
    "02006R1907-20231201",
    "02006R1907-20240606",
    "02006R1907-20241010",
    "02006R1907-20241218",
]
ENTRY78_MARKER="Synthetic polymer microparticles"
DEPENDENCY_FRAGMENT=(
    "for which Annex XVII contains a restriction shall not be manufactured, "
    "placed on the market or used unless it complies with the conditions of "
    "that restriction"
)
CAUSE_ANCHORS={
    "annex-amendment":(
        "Annex XVII to Regulation (EC) No 1907/2006 is amended as follows"
    ),
    "entry-added":"the following entry is added",
}


def fetch_fmx4(celex: str) -> tuple[bytes, requests.Response]:
    response=requests.get(
        BASE.format(celex=celex),
        headers={
            "Accept":"application/zip;mtype=fmx4",
            "Accept-Language":"eng",
            "User-Agent":(
                "Morrow-Needle-Dependency-Ripple-Probe/0.1 "
                "(+https://github.com/kaastumor/morrow-needle)"
            ),
        },
        timeout=180,
        allow_redirects=True,
    )
    response.raise_for_status()
    return response.content,response


def normalized_visible_text(xml_bytes: bytes) -> str:
    root=ET.fromstring(xml_bytes)
    return " ".join("".join(root.itertext()).split())


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


def source_meta(celex: str, response: requests.Response, payload: bytes) -> dict:
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


def build_ast(celex: str, payload: bytes, response: requests.Response) -> dict:
    observation=f"live:{celex}:{hashlib.sha256(payload).hexdigest()[:16]}"
    return FormexASTParser(
        state_id=f"CELEX:{celex}",
        source=source_meta(celex,response,payload),
        source_observation_id=observation,
        representation_plan_id=f"{celex}:ENG:dependency-ripple",
    ).parse_zip(payload)


def subtree_state(
    ast: dict,
    structural_path: list[tuple[str,str]],
) -> dict:
    node=resolve_structural_path(ast,structural_path)
    if node is None:
        raise AssertionError(
            f"could not resolve structural path: {structural_path}"
        )
    children={}
    for candidate in ast.get("nodes",[]):
        children.setdefault(candidate.get("parent_id"),[]).append(
            candidate["node_id"]
        )
    ids=set()
    stack=[node["node_id"]]
    while stack:
        node_id=stack.pop()
        if node_id in ids:
            continue
        ids.add(node_id)
        stack.extend(children.get(node_id,[]))

    segments=sorted(
        (
            segment for segment in ast.get("segments",[])
            if segment["node_id"] in ids
            and segment.get("role") not in {"LABEL","HEADING"}
        ),
        key=lambda segment:(
            segment.get("document_order",0),
            segment.get("ordinal",0),
        ),
    )
    text=" ".join(
        segment.get("text_compare",segment.get("text_source","")).strip()
        for segment in segments
        if segment.get(
            "text_compare",segment.get("text_source","")
        ).strip()
    )
    return {
        "state_id":ast["state_id"],
        "node_id":node["node_id"],
        "text_hash":hashlib.sha256(text.encode("utf-8")).hexdigest(),
        "text_length":len(text),
        "text":text,
    }


def locate_unique(
    payload: bytes,
    *,
    identifier: str,
    phrase: str,
) -> dict:
    matches=[]
    with zipfile.ZipFile(io.BytesIO(payload)) as zf:
        for name in sorted(zf.namelist()):
            if not name.lower().endswith((".xml",".frg")):
                continue
            try:
                text=normalized_visible_text(zf.read(name))
            except ET.ParseError:
                continue
            start=text.find(phrase)
            while start >= 0:
                matches.append({
                    "identifier":identifier,
                    "source_file":name,
                    "locator":(
                        f"{name}#normalized-chars:"
                        f"{start}-{start+len(phrase)}"
                    ),
                    "language":"ENG",
                    "text":phrase,
                    "text_hash":hashlib.sha256(
                        phrase.encode("utf-8")
                    ).hexdigest(),
                })
                start=text.find(phrase,start+1)
    if len(matches)!=1:
        raise AssertionError(
            f"{identifier}: expected one occurrence of {phrase!r}, "
            f"got {len(matches)}"
        )
    return matches[0]


def locate_unique_regex(
    payload: bytes,
    *,
    identifier: str,
    pattern: str,
) -> dict:
    regex=re.compile(pattern)
    matches=[]
    with zipfile.ZipFile(io.BytesIO(payload)) as zf:
        for name in sorted(zf.namelist()):
            if not name.lower().endswith((".xml",".frg")):
                continue
            try:
                text=normalized_visible_text(zf.read(name))
            except ET.ParseError:
                continue
            for match in regex.finditer(text):
                matched=match.group(0)
                matches.append({
                    "identifier":identifier,
                    "source_file":name,
                    "locator":(
                        f"{name}#normalized-chars:"
                        f"{match.start()}-{match.end()}"
                    ),
                    "language":"ENG",
                    "text":matched,
                    "text_hash":hashlib.sha256(
                        matched.encode("utf-8")
                    ).hexdigest(),
                })
    if len(matches)!=1:
        raise AssertionError(
            f"{identifier}: expected one regex match for {pattern!r}, "
            f"got {len(matches)}"
        )
    return matches[0]


def earliest_after_checkpoint() -> tuple[str,bytes,requests.Response]:
    observed=[]
    for celex in AFTER_CANDIDATES:
        payload,response=fetch_fmx4(celex)
        present=ENTRY78_MARKER in all_visible_text(payload)
        observed.append({
            "celex":celex,
            "artifact_hash":"sha256:"+hashlib.sha256(payload).hexdigest(),
            "contains_entry_78":present,
        })
        if present:
            return celex,payload,response,observed
    raise AssertionError(
        "none of the post-amendment consolidated checkpoints contains "
        f"{ENTRY78_MARKER!r}: {observed}"
    )


def main() -> int:
    cause_payload,cause_response=fetch_fmx4(CAUSE)
    before_payload,before_response=fetch_fmx4(BEFORE)
    after_celex,after_payload,after_response,checkpoint_scan=(
        earliest_after_checkpoint()
    )

    before_text=all_visible_text(before_payload)
    after_text=all_visible_text(after_payload)
    if ENTRY78_MARKER in before_text:
        raise AssertionError(
            "entry 78 marker already present in before checkpoint"
        )
    if ENTRY78_MARKER not in after_text:
        raise AssertionError(
            "entry 78 marker absent from selected after checkpoint"
        )

    before_ast=build_ast(BEFORE,before_payload,before_response)
    after_ast=build_ast(after_celex,after_payload,after_response)
    path=[("ARTICLE","67"),("PARAGRAPH","1")]
    before_state=subtree_state(before_ast,path)
    after_state=subtree_state(after_ast,path)

    if DEPENDENCY_FRAGMENT not in before_state["text"]:
        raise AssertionError(
            "Article 67(1) dependency on Annex XVII not found in before state"
        )
    if DEPENDENCY_FRAGMENT not in after_state["text"]:
        raise AssertionError(
            "Article 67(1) dependency on Annex XVII not found in after state"
        )
    if before_state["text_hash"] != after_state["text_hash"]:
        raise AssertionError(
            "Article 67(1) changed textually across dependency transition"
        )

    local_candidate=diff_resolved_subtree(
        before_ast,
        after_ast,
        structural_path=path,
        canonical_kind="PARAGRAPH",
        canonical_citation_path="Article 67 > 1",
        language="ENG",
    )
    if local_candidate is not None:
        raise AssertionError(
            "unchanged Article 67(1) emitted a textual mutation"
        )

    dependency_before=locate_unique(
        before_payload,
        identifier=f"CELEX:{BEFORE}",
        phrase=DEPENDENCY_FRAGMENT,
    )
    dependency_after=locate_unique(
        after_payload,
        identifier=f"CELEX:{after_celex}",
        phrase=DEPENDENCY_FRAGMENT,
    )
    cause_spans={
        key:locate_unique(
            cause_payload,
            identifier=f"CELEX:{CAUSE}",
            phrase=phrase,
        )
        for key,phrase in CAUSE_ANCHORS.items()
    }
    cause_spans["entry-78"]=locate_unique_regex(
        cause_payload,
        identifier=f"CELEX:{CAUSE}",
        pattern=r"78\.\s*Synthetic polymer microparticles",
    )
    entry_after=locate_unique(
        after_payload,
        identifier=f"CELEX:{after_celex}",
        phrase=ENTRY78_MARKER,
    )

    result={
        "probe_version":"0.1",
        "case_id":"reach-art67-annex17-entry78-ripple",
        "subject":{
            "act":"CELEX:32006R1907",
            "local_provision":"Article 67 > 1",
            "dependency_target":"Annex XVII",
            "language":"ENG",
        },
        "cause":{
            "celex":CAUSE,
            "artifact_hash":"sha256:"+hashlib.sha256(
                cause_payload
            ).hexdigest(),
            "final_url":cause_response.url,
            "source_spans":cause_spans,
        },
        "before":{
            "celex":BEFORE,
            "artifact_hash":"sha256:"+hashlib.sha256(
                before_payload
            ).hexdigest(),
            "final_url":before_response.url,
            "local_state":before_state,
            "dependency_span":dependency_before,
            "contains_entry_78":False,
        },
        "after":{
            "celex":after_celex,
            "artifact_hash":"sha256:"+hashlib.sha256(
                after_payload
            ).hexdigest(),
            "final_url":after_response.url,
            "local_state":after_state,
            "dependency_span":dependency_after,
            "entry_78_span":entry_after,
            "contains_entry_78":True,
        },
        "checkpoint_scan":checkpoint_scan,
        "local_textual_mutation":None,
        "dependency_edge":{
            "relation_type":"OPERATIVE_REFERENCE",
            "source":"CELEX:32006R1907#Article67(1)",
            "target":"CELEX:32006R1907#AnnexXVII",
            "evidence_span_before":dependency_before,
            "evidence_span_after":dependency_after,
        },
        "upstream_change":{
            "operation":"INSERT",
            "target":"Annex XVII > entry 78",
            "cause":"CELEX:32023R2055",
            "authentic_instruction_spans":cause_spans,
            "after_checkpoint_span":entry_after,
            "verification_character":"SOURCE_ASSISTED_OFFICIAL",
        },
        "derived_ripple":{
            "character":"DERIVED",
            "statement":(
                "Article 67(1) is textually unchanged, but its operative "
                "reference to Annex XVII now encompasses the newly added "
                "entry 78 subject to that entry's conditions."
            ),
            "local_mutation":False,
            "upstream_dependency_changed":True,
        },
        "negative_regressions":[
            "Do not emit a textual mutation for Article 67(1).",
            "Do not describe entry 78 as text inserted into Article 67(1).",
            "Do not treat the derived dependency ripple as direct local text evidence.",
        ],
    }

    out=Path(
        "artifacts/discovery/reach-art67-annex17-entry78-ripple-v0.1.json"
    )
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(
        json.dumps(result,indent=2,ensure_ascii=False)+"\n",
        encoding="utf-8",
    )
    print(json.dumps(result,indent=2,ensure_ascii=False))
    return 0


if __name__=="__main__":
    raise SystemExit(main())
