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


BASE = "https://publications.europa.eu/resource/celex/{celex}"
EXPECTED_SPANS = {
    "span-entry-into-force": (
        "This Regulation shall enter into force on the 20th day following its "
        "publication in the Official Journal of the European Union."
    ),
    "span-sani-duty": (
        "As from 1 July 2008, notifications shall be transmitted electronically "
        "via the web application State Aid Notification Interactive (SANI)."
    ),
    "span-pki-correspondence-duty": (
        "All correspondence in connection with a notification shall be transmitted "
        "electronically via the secured e-mail system Public Key Infrastructure (PKI)."
    ),
    "span-invalid-channel-status": (
        "In the absence of such an agreement, any notification or correspondence "
        "in connection with a notification sent to the Commission by a Member State "
        "through a communication channel other than those referred to in paragraph 3 "
        "shall not be considered as submitted to the Commission."
    ),
    "span-alt-channel-permission": (
        "In exceptional circumstances and upon the agreement of the Commission and "
        "the Member State concerned, an agreed communication channel other than those "
        "referred to in paragraph 3 may be used for submission of a notification or "
        "any correspondence in connection with a notification."
    ),
}


def fetch_fmx4(celex: str, language: str = "eng") -> tuple[bytes, requests.Response]:
    response = requests.get(
        BASE.format(celex=celex),
        headers={
            "Accept":"application/zip;mtype=fmx4",
            "Accept-Language":language,
            "User-Agent":"Morrow-Needle-Semantic-Span-Probe/0.1 (+https://github.com/kaastumor/morrow-needle)",
        },
        timeout=120,
        allow_redirects=True,
    )
    response.raise_for_status()
    return response.content, response


def normalized_visible_text(xml_bytes: bytes) -> str:
    root = ET.fromstring(xml_bytes)
    return " ".join("".join(root.itertext()).split())


def publication_date_metadata(payload: bytes) -> dict:
    matches=[]
    with zipfile.ZipFile(io.BytesIO(payload)) as zf:
        for name in sorted(zf.namelist()):
            if not name.lower().endswith((".xml",".frg")):
                continue
            try:
                root=ET.fromstring(zf.read(name))
            except ET.ParseError:
                continue
            for element in root.iter():
                tag=element.tag.rsplit("}",1)[-1].upper()
                if tag != "DATE":
                    continue
                iso=element.attrib.get("ISO")
                text=" ".join("".join(element.itertext()).split())
                if iso=="20080325" and text=="20080325":
                    matches.append({
                        "source_file":name,
                        "locator":f"{name}#DATE[ISO=20080325]",
                        "language":"ENG",
                        "text":text,
                        "text_hash":hashlib.sha256(text.encode("utf-8")).hexdigest(),
                    })
    if len(matches)!=1:
        raise AssertionError(
            "expected exactly one source-native publication DATE[ISO=20080325], "
            f"got {len(matches)}"
        )
    return {
        "normalized_date":"2008-03-25",
        **matches[0],
    }


def main() -> int:
    ap=argparse.ArgumentParser()
    ap.add_argument("--celex",default="32008R0271")
    ap.add_argument("--out",default="artifacts/semantic-source/reg794-art3-sani.json")
    args=ap.parse_args()

    payload,response=fetch_fmx4(args.celex)
    matches=[]
    with zipfile.ZipFile(io.BytesIO(payload)) as zf:
        for name in sorted(zf.namelist()):
            if not name.lower().endswith((".xml",".frg")):
                continue
            try:
                text=normalized_visible_text(zf.read(name))
            except ET.ParseError:
                continue
            for span_id, expected_text in EXPECTED_SPANS.items():
                start=text.find(expected_text)
                if start < 0:
                    continue
                end=start+len(expected_text)
                matches.append({
                    "span_id":span_id,
                    "identifier":f"CELEX:{args.celex}",
                    "source_file":name,
                    "locator":f"{name}#normalized-chars:{start}-{end}",
                    "language":"ENG",
                    "text":expected_text,
                    "text_hash":hashlib.sha256(expected_text.encode("utf-8")).hexdigest(),
                })

    publication=publication_date_metadata(payload)

    result={
        "probe_version":"0.1",
        "celex":args.celex,
        "payload_sha256":hashlib.sha256(payload).hexdigest(),
        "final_url":response.url,
        "publication_metadata":publication,
        "derived_entry_into_force":"2008-04-14",
        "matches":matches,
    }
    out=Path(args.out)
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding="utf-8")
    print(json.dumps(result,indent=2,ensure_ascii=False))

    by_id={}
    for match in matches:
        by_id.setdefault(match["span_id"],[]).append(match)
    errors=[]
    for span_id in EXPECTED_SPANS:
        count=len(by_id.get(span_id,[]))
        if count != 1:
            errors.append(f"{span_id}: expected exactly one authentic match, got {count}")
    if errors:
        for error in errors:
            print("ERROR:",error)
        return 1
    return 0


if __name__=="__main__":
    raise SystemExit(main())
