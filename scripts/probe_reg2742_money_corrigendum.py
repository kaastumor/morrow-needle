#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import io
import json
from pathlib import Path
import zipfile
import xml.etree.ElementTree as ET

import requests


CELEX="31990R2742R(01)"
BASE="https://publications.europa.eu/resource/celex/{celex}"


def normalized_visible_text(data: bytes) -> str:
    root=ET.fromstring(data)
    return " ".join("".join(root.itertext()).split())


def main() -> int:
    response=requests.get(
        BASE.format(celex=CELEX),
        headers={
            "Accept":"application/zip;mtype=fmx4",
            "Accept-Language":"eng",
            "User-Agent":(
                "Morrow-Needle-Money-Corrigendum-Probe/0.1 "
                "(+https://github.com/kaastumor/morrow-needle)"
            ),
        },
        timeout=120,
        allow_redirects=True,
    )
    response.raise_for_status()
    payload=response.content
    hits=[]
    with zipfile.ZipFile(io.BytesIO(payload)) as zf:
        for name in sorted(zf.namelist()):
            if not name.lower().endswith((".xml",".frg")):
                continue
            try:
                text=normalized_visible_text(zf.read(name))
            except ET.ParseError:
                continue
            if "ECU 225" not in text and "ECU 255" not in text:
                continue
            positions=[
                pos for needle in ("ECU 225","ECU 255")
                for pos in [text.find(needle)]
                if pos >= 0
            ]
            start=max(0,min(positions)-300)
            end=min(len(text),max(positions)+500)
            snippet=text[start:end]
            hits.append({
                "source_file":name,
                "normalized_text_length":len(text),
                "snippet_start":start,
                "snippet_end":end,
                "snippet":snippet,
                "snippet_hash":hashlib.sha256(
                    snippet.encode("utf-8")
                ).hexdigest(),
            })

    if not hits:
        raise AssertionError(
            "authentic English corrigendum did not expose ECU 225/255 in FMX4"
        )

    result={
        "probe_version":"0.1",
        "celex":CELEX,
        "language":"ENG",
        "artifact_hash":"sha256:"+hashlib.sha256(payload).hexdigest(),
        "final_url":response.url,
        "hits":hits,
    }
    out=Path("artifacts/audit/reg2742-money-corrigendum-inspection.json")
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(
        json.dumps(result,indent=2,ensure_ascii=False)+"\n",
        encoding="utf-8",
    )
    print(json.dumps(result,indent=2,ensure_ascii=False))
    return 0


if __name__=="__main__":
    raise SystemExit(main())
