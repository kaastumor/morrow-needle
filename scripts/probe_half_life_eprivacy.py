#!/usr/bin/env python3
from __future__ import annotations

from datetime import date
import hashlib
import io
import json
from pathlib import Path
import zipfile
import xml.etree.ElementTree as ET

import requests


BASE = "https://publications.europa.eu/resource/celex/{celex}"

ACTS = {
    "32021R1232":{
        "publication_iso":"20210730",
        "sentences":{
            "entry_into_force":(
                "This Regulation shall enter into force on the third day following "
                "that of its publication in the Official Journal of the European Union."
            ),
            "original_application_end":"It shall apply until 3 August 2024.",
        },
    },
    "32024R1307":{
        "publication_iso":"20240514",
        "sentences":{
            "extended_application_end":"It shall apply until 3 April 2026.",
        },
    },
    "32026R1881":{
        "publication_iso":"20260728",
        "sentences":{
            "entry_into_force":(
                "This Regulation shall enter into force on the third day following "
                "that of its publication in the Official Journal of the European Union."
            ),
            "successor_application_end":"It shall apply until 3 April 2028.",
            "predecessor_expired":"Regulation (EU) 2021/1232 has expired.",
        },
    },
}


def fetch_fmx4(celex: str) -> tuple[bytes, requests.Response]:
    response=requests.get(
        BASE.format(celex=celex),
        headers={
            "Accept":"application/zip;mtype=fmx4",
            "Accept-Language":"eng",
            "User-Agent":(
                "Morrow-Needle-Half-Life-Probe/0.1 "
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


def publication_metadata(payload: bytes, expected_iso: str) -> dict:
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
                if element.tag.rsplit("}",1)[-1].upper() != "DATE":
                    continue
                iso=element.attrib.get("ISO")
                text=" ".join("".join(element.itertext()).split())
                if iso==expected_iso and text==expected_iso:
                    matches.append({
                        "source_file":name,
                        "locator":f"{name}#DATE[ISO={expected_iso}]",
                        "text":text,
                        "text_hash":hashlib.sha256(text.encode("utf-8")).hexdigest(),
                    })
    if not matches:
        raise AssertionError(
            f"no source-native publication DATE[ISO={expected_iso}]"
        )
    signatures={(m["text"],m["text_hash"]) for m in matches}
    if len(signatures)!=1:
        raise AssertionError(
            f"conflicting publication metadata for {expected_iso}: {matches}"
        )
    matches=sorted(matches,key=lambda item:item["locator"])
    return {
        "normalized_date":(
            f"{expected_iso[:4]}-{expected_iso[4:6]}-{expected_iso[6:]}"
        ),
        "occurrence_count":len(matches),
        "canonical_occurrence":matches[0],
        "occurrences":matches,
    }


def locate_sentences(payload: bytes, expected: dict[str,str]) -> dict:
    found={key:[] for key in expected}
    with zipfile.ZipFile(io.BytesIO(payload)) as zf:
        for name in sorted(zf.namelist()):
            if not name.lower().endswith((".xml",".frg")):
                continue
            try:
                text=normalized_visible_text(zf.read(name))
            except ET.ParseError:
                continue
            for key,sentence in expected.items():
                pos=text.find(sentence)
                while pos >= 0:
                    found[key].append({
                        "source_file":name,
                        "locator":f"{name}#normalized-chars:{pos}-{pos+len(sentence)}",
                        "text":sentence,
                        "text_hash":hashlib.sha256(
                            sentence.encode("utf-8")
                        ).hexdigest(),
                    })
                    pos=text.find(sentence,pos+1)

    result={}
    for key,matches in found.items():
        if not matches:
            raise AssertionError(f"{key}: expected at least one authentic match")
        signatures={(m["text"],m["text_hash"]) for m in matches}
        if len(signatures)!=1:
            raise AssertionError(f"{key}: conflicting authentic matches: {matches}")
        matches=sorted(matches,key=lambda item:item["locator"])
        result[key]={
            "occurrence_count":len(matches),
            "canonical_occurrence":matches[0],
            "occurrences":matches,
        }
    return result


def inclusive_days(start: str, end: str) -> int:
    return (date.fromisoformat(end)-date.fromisoformat(start)).days+1


def main() -> int:
    observations={}
    for celex,contract in ACTS.items():
        payload,response=fetch_fmx4(celex)
        observations[celex]={
            "celex":celex,
            "artifact_hash":"sha256:"+hashlib.sha256(payload).hexdigest(),
            "final_url":response.url,
            "publication_metadata":publication_metadata(
                payload,contract["publication_iso"]
            ),
            "source_spans":locate_sentences(
                payload,contract["sentences"]
            ),
        }

    original_start="2021-08-02"
    original_planned_end="2024-08-03"
    extended_end="2026-04-03"
    gap_start="2026-04-04"
    gap_end="2026-07-30"
    successor_start="2026-07-31"
    successor_end="2028-04-03"

    metrics={
        "original_application_start":original_start,
        "original_planned_end":original_planned_end,
        "original_planned_days":inclusive_days(
            original_start,original_planned_end
        ),
        "extended_first_regime_end":extended_end,
        "extended_first_regime_days":inclusive_days(
            original_start,extended_end
        ),
        "extension_added_days":(
            date.fromisoformat(extended_end)
            - date.fromisoformat(original_planned_end)
        ).days,
        "gap_start":gap_start,
        "gap_end":gap_end,
        "gap_days":inclusive_days(gap_start,gap_end),
        "successor_application_start":successor_start,
        "successor_application_end":successor_end,
        "successor_days":inclusive_days(successor_start,successor_end),
    }
    metrics["total_applicable_days_through_successor_end"]=(
        metrics["extended_first_regime_days"]+metrics["successor_days"]
    )
    metrics["calendar_span_days"]=inclusive_days(
        original_start,successor_end
    )
    metrics["non_applicable_days_in_span"]=(
        metrics["calendar_span_days"]
        - metrics["total_applicable_days_through_successor_end"]
    )

    if metrics["original_planned_days"] != 1098:
        raise AssertionError(metrics)
    if metrics["extension_added_days"] != 608:
        raise AssertionError(metrics)
    if metrics["gap_days"] != 118:
        raise AssertionError(metrics)
    if metrics["successor_days"] != 613:
        raise AssertionError(metrics)
    if metrics["non_applicable_days_in_span"] != 118:
        raise AssertionError(metrics)

    result={
        "probe_version":"0.1",
        "concept":"HALF_LIFE",
        "topic":"temporary ePrivacy derogation for voluntary online child sexual abuse detection",
        "observations":observations,
        "metrics":metrics,
        "interpretation_guardrails":[
            "Temporary is a legal/source characterization, not an evaluative criticism.",
            "The 2026 act is a successor temporary derogation; the 118-day gap is preserved.",
            "Genealogical relation does not imply uninterrupted applicability.",
            "No proposition-by-proposition rule continuity is asserted by this probe.",
            "Derived durations are analytics over evidenced dates, not new legal-state facts.",
        ],
    }

    out=Path("artifacts/discovery/half-life-eprivacy-v0.1.json")
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(
        json.dumps(result,indent=2,ensure_ascii=False)+"\n",
        encoding="utf-8",
    )
    print(json.dumps(result,indent=2,ensure_ascii=False))
    return 0


if __name__=="__main__":
    raise SystemExit(main())
