#!/usr/bin/env python3
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any

import requests
import xml.etree.ElementTree as ET
from collections import Counter

# Official Cellar dissemination resource endpoint documented by the Publications Office.
BASE = "https://publications.europa.eu/resource/celex/{celex}"

PROBES = [
    {
        "name": "rdf_tree_notice",
        "headers": {"Accept": "application/rdf+xml;notice=tree"},
        "params": {},
    },
    {
        "name": "xml_branch_notice_eng",
        "headers": {
            "Accept": "application/xml;notice=branch",
            "Accept-Language": "eng",
        },
        "params": {"language": "eng"},
    },
    {
        "name": "fmx4_list_eng",
        "headers": {
            "Accept": "application/list;mtype=fmx4",
            "Accept-Language": "eng",
        },
        "params": {},
    },
    {
        "name": "fmx4_zip_eng",
        "headers": {
            "Accept": "application/zip;mtype=fmx4",
            "Accept-Language": "eng",
        },
        "params": {},
    },
    {
        "name": "xhtml_list_eng",
        "headers": {
            "Accept": "application/list;mtype=xhtml",
            "Accept-Language": "eng",
        },
        "params": {},
    },
    {
        "name": "html_list_eng",
        "headers": {
            "Accept": "application/list;mtype=html",
            "Accept-Language": "eng",
        },
        "params": {},
    },
    {
        "name": "legacy_xml_type_fmx4_eng",
        "headers": {
            "Accept": "application/xml;type=fmx4",
            "Accept-Language": "eng",
        },
        "params": {},
    },
]

def _local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]

def _child_values(node, child_tag: str):
    values = []
    for child in list(node):
        if _local(child.tag) != child_tag:
            continue
        for descendant in child.iter():
            if _local(descendant.tag) == "VALUE":
                value = (descendant.text or "").strip()
                if value and value not in values:
                    values.append(value)
    return values

def _first_uri(node):
    for child in list(node):
        if _local(child.tag) != "URI":
            continue
        for descendant in child.iter():
            if _local(descendant.tag) == "VALUE":
                value = (descendant.text or "").strip()
                if value:
                    return value
    return None

def extract_branch_manifestations(root):
    inventory = []
    seen = set()

    for relation in root.iter():
        if _local(relation.tag) != "EXPRESSION_MANIFESTED_BY_MANIFESTATION":
            continue
        for manifestation in relation.iter():
            if _local(manifestation.tag) != "MANIFESTATION":
                continue

            uri = _first_uri(manifestation)
            types = _child_values(manifestation, "MANIFESTATION_TYPE")

            # Some notices encode manifestation type in embedded metadata.
            if not types:
                for candidate in manifestation.iter():
                    if _local(candidate.tag) == "MANIFESTATION_TYPE":
                        for descendant in candidate.iter():
                            if _local(descendant.tag) == "VALUE":
                                value = (descendant.text or "").strip()
                                if value and value not in types:
                                    types.append(value)

            key = (uri, tuple(types))
            if key in seen:
                continue
            seen.add(key)

            inventory.append({
                "uri": uri,
                "types": types,
            })

    return inventory

def choose_representation(inventory):
    preference = [
        ("fmx4", "STRUCTURED_LEGAL_XML"),
        ("xhtml", "STRUCTURED_XHTML"),
        ("html", "STRUCTURED_HTML"),
        ("pdfa2a", "PDF_TEXT"),
        ("pdfa1a", "PDF_TEXT"),
        ("pdf", "PDF_TEXT"),
    ]
    normalized = []
    for item in inventory:
        for value in item.get("types", []):
            normalized.append((value.lower(), item))

    for wanted, quality in preference:
        for typ, item in normalized:
            if typ == wanted:
                return {
                    "manifestation_type": wanted,
                    "representation_class": quality,
                    "manifestation_uri": item.get("uri"),
                }
    return None

def summarize_xml(body: bytes) -> Dict[str, Any]:
    try:
        root = ET.fromstring(body)
    except Exception as exc:
        return {"parse_error": f"{type(exc).__name__}: {exc}"}

    counts = Counter(_local(el.tag) for el in root.iter())

    manifestations = []
    for node in root.iter():
        if _local(node.tag).upper() != "MANIFESTATION":
            continue
        fields = {}
        for child in node.iter():
            name = _local(child.tag)
            text = (child.text or "").strip()
            if text and len(text) <= 500:
                fields.setdefault(name, [])
                if text not in fields[name] and len(fields[name]) < 10:
                    fields[name].append(text)
        manifestations.append(fields)
        if len(manifestations) >= 30:
            break

    result = {
        "root_tag": _local(root.tag),
        "top_tag_counts": counts.most_common(40),
        "manifestation_count_sampled": len(manifestations),
        "manifestations": manifestations,
    }

    if _local(root.tag) == "NOTICE":
        branch_inventory = extract_branch_manifestations(root)
        result["branch_manifestation_inventory"] = branch_inventory
        result["selected_representation"] = choose_representation(branch_inventory)

    return result

def summarize_response(r: requests.Response) -> Dict[str, Any]:
    body = r.content
    content_type = (r.headers.get("content-type") or "").lower()
    if "zip" in content_type or body.startswith(b"PK"):
        text_head = "<binary zip payload>"
    else:
        text_head = body[:500].decode("utf-8", errors="replace").replace("\n", " ")
    summary = {
        "status": r.status_code,
        "content_type": r.headers.get("content-type"),
        "content_length_header": r.headers.get("content-length"),
        "bytes": len(body),
        "sha256": hashlib.sha256(body).hexdigest(),
        "final_url": r.url,
        "redirect_chain": [
            {
                "status": h.status_code,
                "url": h.url,
                "location": h.headers.get("location"),
            }
            for h in r.history
        ],
        "head": text_head,
    }

    if r.status_code == 200 and ("xml" in content_type or body.lstrip().startswith(b"<?xml")):
        summary["xml_structure"] = summarize_xml(body)

    return summary

def run_probe(celex: str) -> Dict[str, Any]:
    url = BASE.format(celex=celex)
    record: Dict[str, Any] = {
        "celex": celex,
        "resource_url": url,
        "observed_at": datetime.now(timezone.utc).isoformat(),
        "probes": {},
    }

    for probe in PROBES:
        try:
            r = requests.get(
                url,
                headers={
                    **probe["headers"],
                    "User-Agent": "Morrow-Needle-Source-Probe/0.1 (+https://github.com/kaastumor/morrow-needle)",
                },
                params=probe["params"],
                timeout=60,
                allow_redirects=True,
            )
            record["probes"][probe["name"]] = summarize_response(r)
        except Exception as exc:
            record["probes"][probe["name"]] = {
                "error": type(exc).__name__,
                "message": str(exc),
            }

    return record

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("celex", nargs="+")
    ap.add_argument("--out", default="artifacts/cellar-probe.json")
    args = ap.parse_args()

    payload = {
        "probe_version": "0.1",
        "source": "Cellar dissemination API",
        "official_documentation": "https://op.europa.eu/en/web/cellar/cellar-data/metadata/metadata-notices",
        "results": [run_probe(c) for c in args.celex],
    }

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    print(json.dumps(payload, indent=2, ensure_ascii=False))

    # Foundation-level failure only if Cellar cannot resolve the CELEX work at all.
    failed = []
    for result in payload["results"]:
        tree = result["probes"].get("rdf_tree_notice", {})
        if tree.get("status") != 200:
            failed.append(result["celex"])

    if failed:
        print(f"ERROR: Cellar tree notice failed for: {', '.join(failed)}")
        return 1

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
