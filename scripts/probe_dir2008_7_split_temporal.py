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


CELEX="32008L0007"
URL=f"https://publications.europa.eu/resource/celex/{CELEX}"


def visible_text(data: bytes) -> str:
    root=ET.fromstring(data)
    return " ".join("".join(root.itertext()).split())


def find_context(text: str, pattern: str, *, label: str, radius: int = 260):
    match=re.search(pattern,text,re.IGNORECASE)
    if not match:
        return None
    start=max(0,match.start()-radius)
    end=min(len(text),match.end()+radius)
    snippet=text[start:end]
    return {
        "label":label,
        "match_start":match.start(),
        "match_end":match.end(),
        "context_start":start,
        "context_end":end,
        "context":snippet,
        "context_hash":hashlib.sha256(snippet.encode("utf-8")).hexdigest(),
    }


def main() -> int:
    response=requests.get(
        URL,
        headers={
            "Accept":"application/zip;mtype=fmx4",
            "Accept-Language":"eng",
            "User-Agent":(
                "Morrow-Needle-Split-Temporal-Probe/0.1 "
                "(+https://github.com/kaastumor/morrow-needle)"
            ),
        },
        timeout=120,
        allow_redirects=True,
    )
    response.raise_for_status()
    payload=response.content

    patterns={
        "correlation":r"Article\s+7\(2\).*?Articles?\s+7\s+and\s+8",
        "transposition":(
            r"Articles\s+3,\s*4,\s*5,\s*7,\s*8,\s*12,\s*13\s+and\s+14"
            r".{0,180}?31\s+December\s+2008"
        ),
        "repeal":(
            r"Directive\s+69/335/EEC.{0,220}?"
            r"repealed\s+with\s+effect\s+from\s+1\s+January\s+2009"
        ),
        "application_list":(
            r"Articles\s+1,\s*2,\s*6,\s*9,\s*10\s+and\s+11"
            r"\s+shall\s+apply\s+from\s+1\s+January\s+2009"
        ),
    }

    hits={key:[] for key in patterns}
    with zipfile.ZipFile(io.BytesIO(payload)) as zf:
        for name in sorted(zf.namelist()):
            if not name.lower().endswith((".xml",".frg")):
                continue
            try:
                text=visible_text(zf.read(name))
            except ET.ParseError:
                continue
            for key,pattern in patterns.items():
                found=find_context(text,pattern,label=key)
                if found:
                    found["source_file"]=name
                    hits[key].append(found)

    missing=[key for key,items in hits.items() if not items]
    if missing:
        raise AssertionError({
            "missing":missing,
            "found_counts":{key:len(items) for key,items in hits.items()},
        })

    result={
        "probe_version":"0.1",
        "celex":CELEX,
        "artifact_hash":"sha256:"+hashlib.sha256(payload).hexdigest(),
        "final_url":response.url,
        "hits":hits,
        "invariants":[
            "Official structural correlation is separate from temporal semantics.",
            "The Article 7(2) predecessor maps structurally to both Articles 7 and 8.",
            "Articles 7 and 8 are named in the 31 December 2008 transposition deadline.",
            "The repealed predecessor Directive ends from 1 January 2009.",
            "The explicit 1 January 2009 application clause names Articles 1, 2, 6, 9, 10 and 11, not Articles 7 or 8.",
            "No application date for successor Articles 7 or 8 may be synthesized from lineage or repeal chronology."
        ],
    }
    out=Path("artifacts/audit/dir2008-7-split-temporal-inspection.json")
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(
        json.dumps(result,indent=2,ensure_ascii=False)+"\n",
        encoding="utf-8",
    )
    print(json.dumps(result,indent=2,ensure_ascii=False))
    return 0


if __name__=="__main__":
    raise SystemExit(main())
