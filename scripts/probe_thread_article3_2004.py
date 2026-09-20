#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import io
import json
from pathlib import Path
import zipfile
import xml.etree.ElementTree as ET

import requests

from needle.ast.formex import FormexASTParser
from needle.ast.resolve import resolve_structural_path


BASE = "https://publications.europa.eu/resource/celex/{celex}"
AUTHENTIC = "32004R0794"
INITIAL = "02004R0794-20040520"
SENTENCES = {
    "entry-into-force": (
        "This Regulation shall enter into force on the twentieth day following "
        "that of its publication in the Official Journal of the European Union."
    ),
    "chapter-ii-application": (
        "Chapter II shall apply only to those notifications transmitted to the "
        "Commission more than five months after the entry into force of this Regulation."
    ),
    "paper-until-2005": (
        "Until 31 December 2005 notifications shall be transmitted by the Member State "
        "on paper."
    ),
    "electronic-from-2006": (
        "With effect from 1 January 2006 notifications shall be transmitted "
        "electronically, unless otherwise agreed by the Commission and the notifying "
        "Member State."
    ),
    "correspondence-from-2006": (
        "All correspondence in connection with a notification which has been submitted "
        "after 1 January 2006 shall be transmitted electronically."
    ),
}


def fetch_fmx4(celex: str) -> tuple[bytes, requests.Response]:
    response = requests.get(
        BASE.format(celex=celex),
        headers={
            "Accept":"application/zip;mtype=fmx4",
            "Accept-Language":"eng",
            "User-Agent":(
                "Morrow-Needle-Thread-2004-Probe/0.1 "
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


def source_meta(celex: str,response: requests.Response,payload: bytes) -> dict:
    digest=hashlib.sha256(payload).hexdigest()
    observation=f"live:{celex}:{digest[:16]}"
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


def build_ast(celex: str,payload: bytes,response: requests.Response) -> dict:
    digest=hashlib.sha256(payload).hexdigest()
    return FormexASTParser(
        state_id=f"CELEX:{celex}",
        source=source_meta(celex,response,payload),
        source_observation_id=f"live:{celex}:{digest[:16]}",
        representation_plan_id=f"{celex}:ENG:thread-2004",
    ).parse_zip(payload)


def subtree_state(ast: dict, structural_path: list[tuple[str,str]]) -> dict:
    node=resolve_structural_path(ast,structural_path)
    if node is None:
        raise AssertionError(f"could not resolve structural path: {structural_path}")

    children={}
    for candidate in ast.get("nodes",[]):
        children.setdefault(candidate.get("parent_id"),[]).append(candidate["node_id"])
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
        if segment.get("text_compare",segment.get("text_source","")).strip()
    )
    return {
        "state_id":ast["state_id"],
        "node_id":node["node_id"],
        "text_hash":hashlib.sha256(text.encode("utf-8")).hexdigest(),
        "text_length":len(text),
    }


def publication_date_metadata(payload: bytes) -> dict:
    candidates=[]
    date_patterns=("20040430","2004-04-30","30.04.2004","30/04/2004")
    with zipfile.ZipFile(io.BytesIO(payload)) as zf:
        for name in sorted(zf.namelist()):
            if not name.lower().endswith((".xml",".frg")):
                continue
            raw=zf.read(name).decode("utf-8",errors="replace")
            try:
                root=ET.fromstring(raw)
            except ET.ParseError:
                continue
            for element in root.iter():
                tag=element.tag.rsplit("}",1)[-1].upper()
                text=" ".join("".join(element.itertext()).split())
                attrs={str(k):str(v) for k,v in element.attrib.items()}
                material=" ".join([tag,text,*attrs.keys(),*attrs.values()])
                if "2004" not in material:
                    continue
                if not any(token in material for token in date_patterns):
                    continue
                candidates.append({
                    "source_file":name,
                    "tag":tag,
                    "attributes":attrs,
                    "text":text[:300],
                })
    exact=[
        candidate for candidate in candidates
        if candidate["tag"]=="DATE"
        and candidate["attributes"].get("ISO")=="20040430"
        and candidate["text"]=="20040430"
    ]
    if len(exact)!=1:
        raise AssertionError(
            "expected one source-native publication DATE[ISO=20040430], "
            f"got {len(exact)}"
        )
    candidate=exact[0]
    return {
        "normalized_date":"2004-04-30",
        "source_file":candidate["source_file"],
        "locator":(
            f"{candidate['source_file']}#DATE[ISO=20040430]"
        ),
        "source_text":"20040430",
        "text_hash":hashlib.sha256(b"20040430").hexdigest(),
        "tag":candidate["tag"],
        "attributes":candidate["attributes"],
    }


def locate_sentences(payload: bytes) -> dict:
    matches={key:[] for key in SENTENCES}
    with zipfile.ZipFile(io.BytesIO(payload)) as zf:
        for name in sorted(zf.namelist()):
            if not name.lower().endswith((".xml",".frg")):
                continue
            try:
                text=normalized_visible_text(zf.read(name))
            except ET.ParseError:
                continue
            for key,sentence in SENTENCES.items():
                start=text.find(sentence)
                while start >= 0:
                    matches[key].append({
                        "identifier":f"CELEX:{AUTHENTIC}",
                        "source_file":name,
                        "locator":f"{name}#normalized-chars:{start}-{start+len(sentence)}",
                        "language":"ENG",
                        "text":sentence,
                        "text_hash":hashlib.sha256(sentence.encode("utf-8")).hexdigest(),
                    })
                    start=text.find(sentence,start+1)
    for key,found in matches.items():
        if len(found)!=1:
            raise AssertionError(
                f"{key}: expected one authentic sentence, got {len(found)}"
            )
    return {key:found[0] for key,found in matches.items()}


def main() -> int:
    authentic_payload,authentic_response=fetch_fmx4(AUTHENTIC)
    initial_payload,initial_response=fetch_fmx4(INITIAL)

    authentic_ast=build_ast(AUTHENTIC,authentic_payload,authentic_response)
    initial_ast=build_ast(INITIAL,initial_payload,initial_response)

    path=[("ARTICLE","3")]
    authentic_state=subtree_state(authentic_ast,path)
    initial_state=subtree_state(initial_ast,path)
    spans=locate_sentences(authentic_payload)
    publication_metadata=publication_date_metadata(authentic_payload)

    if authentic_state["text_hash"] != initial_state["text_hash"]:
        raise AssertionError(
            "authentic Article 3 and initial consolidated checkpoint differ"
        )

    result={
        "probe_version":"0.1",
        "authentic":{
            "celex":AUTHENTIC,
            "payload_sha256":hashlib.sha256(authentic_payload).hexdigest(),
            "final_url":authentic_response.url,
            "article3":authentic_state,
        },
        "initial_checkpoint":{
            "celex":INITIAL,
            "payload_sha256":hashlib.sha256(initial_payload).hexdigest(),
            "final_url":initial_response.url,
            "article3":initial_state,
        },
        "comparison":{
            "article3_text_equal":True,
            "basis":"EXACT_CANONICAL_AST_SUBTREE_HASH",
            "lineage_inference":False,
        },
        "source_spans":spans,
        "publication_metadata":publication_metadata,
        "temporal_boundaries":{
            "publication_date":"2004-04-30",
            "entry_into_force_expression":(
                "twentieth day following publication"
            ),
            "chapter_ii_application_expression":(
                "more than five months after entry into force"
            ),
            "chapter_ii_application_boundary_inclusive":False,
            "paper_rule_end":"2005-12-31",
            "electronic_notification_start":"2006-01-01",
            "electronic_correspondence_scope_start":"EVENT_CONDITIONED",
        },
    }
    out=Path("artifacts/thread-2004/article3-2004.json")
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding="utf-8")
    print(json.dumps(result,indent=2,ensure_ascii=False))
    return 0


if __name__=="__main__":
    raise SystemExit(main())
