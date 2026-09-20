#!/usr/bin/env python3
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
import pathlib
from typing import Dict, Any

import requests
import xml.etree.ElementTree as ET
from collections import Counter
import io
import zipfile
import re

# Official Cellar dissemination resource endpoint documented by the Publications Office.
BASE = "https://publications.europa.eu/resource/celex/{celex}"
SPARQL_ENDPOINT = "https://publications.europa.eu/webapi/rdf/sparql"

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
        "name": "xhtml_zip_eng",
        "headers": {
            "Accept": "application/zip;mtype=xhtml",
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
        "name": "html_zip_eng",
        "headers": {
            "Accept": "application/zip;mtype=html",
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

        relation_examples = []
        for relation in root.iter():
            if _local(relation.tag) == "EXPRESSION_MANIFESTED_BY_MANIFESTATION":
                relation_examples.append(
                    ET.tostring(relation, encoding="unicode")[:5000]
                )
                if len(relation_examples) >= 3:
                    break
        result["manifestation_relation_examples"] = relation_examples

    return result

def inspect_zip_payload(body: bytes) -> Dict[str, Any]:
    result = {
        "entry_count": 0,
        "xml_like_entries": 0,
        "clg_mdfo_occurrences": 0,
        "clg_mdfc_occurrences": 0,
        "modification_examples": [],
        "entry_names_sample": [],
        "extension_counts": {},
        "xml_entries": [],
        "image_reference_examples": [],
        "html_entries": [],
    }
    try:
        with zipfile.ZipFile(io.BytesIO(body)) as zf:
            names = zf.namelist()
            result["entry_count"] = len(names)
            result["entry_names_sample"] = names[:50]

            extension_counts = Counter()
            for name in names:
                suffix = pathlib.PurePosixPath(name).suffix.lower() or "<none>"
                extension_counts[suffix] += 1
            result["extension_counts"] = dict(sorted(extension_counts.items()))

            for name in names:
                lower = name.lower()
                if lower.endswith((".html", ".xhtml", ".htm")):
                    try:
                        data = zf.read(name)
                    except Exception:
                        data = b""
                    html_text = data.decode("utf-8", errors="replace")
                    visible_html = re.sub(r"<script\\b.*?</script>", " ", html_text, flags=re.I | re.S)
                    visible_html = re.sub(r"<style\\b.*?</style>", " ", visible_html, flags=re.I | re.S)
                    visible_html = re.sub(r"<[^>]+>", " ", visible_html)
                    visible_html = re.sub(r"\\s+", " ", visible_html).strip()
                    img_tags = re.findall(r"<img\\b[^>]*>", html_text, flags=re.I)
                    srcs = []
                    for tag in img_tags[:500]:
                        m = re.search(r'\\bsrc=["\\\']([^"\\\']+)', tag, flags=re.I)
                        if m:
                            srcs.append(m.group(1)[:300])
                    result["html_entries"].append({
                        "name": name,
                        "bytes": len(data),
                        "visible_text_chars_estimate": len(visible_html),
                        "img_tag_count": len(img_tags),
                        "data_image_count": sum(1 for src in srcs if src.lower().startswith("data:image")),
                        "image_src_sample": srcs[:20],
                    })

                if not lower.endswith((".xml", ".frg")):
                    continue
                result["xml_like_entries"] += 1
                try:
                    data = zf.read(name)
                except Exception:
                    continue

                text = data.decode("utf-8", errors="replace")
                visible = re.sub(r"<\\?.*?\\?>", "", text, flags=re.S)
                visible = re.sub(r"<[^>]+>", " ", visible)
                visible = re.sub(r"\\s+", " ", visible).strip()
                refs = sorted(set(re.findall(r"[^\\\"'<>\\s]+\\.(?:tif|tiff|png|jpg|jpeg|gif)", text, flags=re.I)))

                result["xml_entries"].append({
                    "name": name,
                    "bytes": len(data),
                    "visible_text_chars_estimate": len(visible),
                    "image_reference_count": len(refs),
                    "image_references_sample": refs[:20],
                })
                for ref in refs:
                    if len(result["image_reference_examples"]) >= 30:
                        break
                    result["image_reference_examples"].append({"entry": name, "reference": ref})

                open_count = data.count(b"CLG.MDFO")
                close_count = data.count(b"CLG.MDFC")
                result["clg_mdfo_occurrences"] += open_count
                result["clg_mdfc_occurrences"] += close_count

                if open_count and len(result["modification_examples"]) < 12:
                    cursor = 0
                    while len(result["modification_examples"]) < 12:
                        idx = text.find("CLG.MDFO", cursor)
                        if idx < 0:
                            break
                        start = max(0, idx - 120)
                        end = min(len(text), idx + 1800)
                        result["modification_examples"].append({
                            "entry": name,
                            "context": text[start:end],
                        })
                        cursor = idx + len("CLG.MDFO")
    except Exception as exc:
        result["zip_parse_error"] = f"{type(exc).__name__}: {exc}"
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

    if r.status_code == 200 and ("zip" in content_type or body.startswith(b"PK")):
        summary["zip_structure"] = inspect_zip_payload(body)

    return summary

REPRESENTATION_PREFERENCE = [
    ("fmx4", "STRUCTURED_LEGAL_XML"),
    ("xhtml", "STRUCTURED_XHTML"),
    ("html", "STRUCTURED_HTML"),
    ("pdfa2a", "PDF_TEXT"),
    ("pdfa1a", "PDF_TEXT"),
    ("pdfa1b", "PDF_TEXT"),
    ("pdf", "PDF_TEXT"),
]

def select_sparql_representation(rows):
    """Select a manifestation, never an arbitrary item.

    The knowledge graph may expose one or more Item URIs for a manifestation.
    Those Items are not assumed to equal every internal stream exposed by
    Cellar's publication-list endpoint.
    """
    by_format = {}
    for row in rows:
        fmt = (row.get("format") or "").lower()
        manif = row.get("manif")
        if not fmt or not manif:
            continue
        key = (fmt, manif)
        entry = by_format.setdefault(key, {
            "format": fmt,
            "manifestation_uri": manif,
            "expression_uri": row.get("expr"),
            "work_uri": row.get("work"),
            "language": row.get("langCode"),
            "item_uris": [],
        })
        item = row.get("item")
        if item and item not in entry["item_uris"]:
            entry["item_uris"].append(item)

    for wanted, quality in REPRESENTATION_PREFERENCE:
        candidates = [
            entry for (fmt, _), entry in by_format.items()
            if fmt == wanted
        ]
        if not candidates:
            continue
        candidates.sort(key=lambda x: x["manifestation_uri"])
        selected = candidates[0]
        return {
            **selected,
            "representation_class": quality,
            "selection_basis": "SPARQL_MANIFESTATION_INVENTORY",
            "collection_list_accept": f"application/list;mtype={wanted}",
            "collection_zip_accept": f"application/zip;mtype={wanted}",
            "internal_stream_count": None,
            "internal_stream_count_basis": "NOT_YET_PROBED",
        }

    return None

def sparql_inventory(celex: str, language: str = "ENG") -> Dict[str, Any]:
    query = f"""
PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX purl: <http://purl.org/dc/elements/1.1/>

SELECT DISTINCT ?work ?expr ?manif ?langCode (str(?format) AS ?format) ?item
WHERE {{
  ?work owl:sameAs <http://publications.europa.eu/resource/celex/{celex}> .
  ?expr cdm:expression_belongs_to_work ?work ;
        cdm:expression_uses_language ?lang .
  ?lang purl:identifier ?langCode .
  ?manif cdm:manifestation_manifests_expression ?expr ;
         cdm:manifestation_type ?format .
  ?item cdm:item_belongs_to_manifestation ?manif .
  FILTER(str(?langCode)="{language}")
}}
ORDER BY ?format ?manif ?item
LIMIT 5000
"""
    try:
        r = requests.get(
            SPARQL_ENDPOINT,
            params={"query": query, "format": "application/sparql-results+json"},
            headers={
                "Accept": "application/sparql-results+json",
                "User-Agent": "Morrow-Needle-Source-Probe/0.1 (+https://github.com/kaastumor/morrow-needle)",
            },
            timeout=90,
        )
        result = {
            "status": r.status_code,
            "content_type": r.headers.get("content-type"),
            "bytes": len(r.content),
            "sha256": hashlib.sha256(r.content).hexdigest(),
        }
        if r.status_code == 200:
            payload = r.json()
            rows = []
            for binding in payload.get("results", {}).get("bindings", []):
                rows.append({
                    key: value.get("value")
                    for key, value in binding.items()
                })
            result["row_count"] = len(rows)
            result["rows"] = rows
            formats = sorted({row.get("format") for row in rows if row.get("format")})
            result["formats"] = formats
            result["manifestation_count"] = len({row.get("manif") for row in rows if row.get("manif")})
            result["item_count"] = len({row.get("item") for row in rows if row.get("item")})
            result["selected_representation"] = select_sparql_representation(rows)
        else:
            result["head"] = r.text[:1000]
        return result
    except Exception as exc:
        return {"error": type(exc).__name__, "message": str(exc)}

def run_probe(celex: str) -> Dict[str, Any]:
    url = BASE.format(celex=celex)
    record: Dict[str, Any] = {
        "celex": celex,
        "resource_url": url,
        "observed_at": datetime.now(timezone.utc).isoformat(),
        "sparql_inventory_eng": sparql_inventory(celex, "ENG"),
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
