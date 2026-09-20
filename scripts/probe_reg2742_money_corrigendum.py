#!/usr/bin/env python3
from __future__ import annotations

from html.parser import HTMLParser
import hashlib
import json
from pathlib import Path
import re

import requests

from needle.mutation.instructions import parse_authentic_corrigendum_replacements


CELEX="31990R2742R(01)"
CELLAR_URL=f"https://publications.europa.eu/resource/celex/{CELEX}"
HTML_URL=(
    "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/"
    f"?uri=CELEX:{CELEX}"
)
PDF_URL=(
    "https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/"
    f"?uri=CELEX:{CELEX}"
)


class VisibleText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts=[]
        self.hidden=0

    def handle_starttag(self, tag, attrs):
        if tag.lower() in {"script","style"}:
            self.hidden += 1

    def handle_endtag(self, tag):
        if tag.lower() in {"script","style"} and self.hidden:
            self.hidden -= 1

    def handle_data(self, data):
        if not self.hidden:
            self.parts.append(data)


def normalized_html_text(payload: bytes) -> str:
    parser=VisibleText()
    parser.feed(payload.decode("utf-8",errors="replace"))
    return " ".join(" ".join(parser.parts).split())


def fetch(url: str, *, accept: str) -> requests.Response:
    response=requests.get(
        url,
        headers={
            "Accept":accept,
            "Accept-Language":"eng",
            "User-Agent":(
                "Morrow-Needle-Money-Corrigendum-Probe/0.2 "
                "(+https://github.com/kaastumor/morrow-needle)"
            ),
        },
        timeout=120,
        allow_redirects=True,
    )
    return response


def main() -> int:
    # Important audit adversary: the historic corrigendum is not resolvable
    # through the normal Cellar CELEX route, while authoritative EUR-Lex
    # representations exist. Route availability must not become legal absence.
    cellar=fetch(CELLAR_URL,accept="application/zip;mtype=fmx4")

    html=fetch(HTML_URL,accept="text/html")
    html.raise_for_status()
    text=normalized_html_text(html.content)

    target="On page 21 in the second line of Article 4 (1):"
    if target not in text or "ECU 225" not in text or "ECU 255" not in text:
        raise AssertionError(
            "official EUR-Lex HTML does not expose expected Article 4(1) correction"
        )

    target_start=text.index(target)
    after_end=text.index("ECU 255",target_start)+len("ECU 255")
    correction_text=text[target_start:after_end]
    before_fragment="shall be ECU 225"
    after_fragment="shall be ECU 255"
    if before_fragment not in correction_text or after_fragment not in correction_text:
        raise AssertionError(correction_text)

    pdf=fetch(PDF_URL,accept="application/pdf")
    pdf.raise_for_status()
    if not pdf.content.startswith(b"%PDF"):
        raise AssertionError(
            f"official OJ PDF route returned {pdf.headers.get('content-type')}"
        )

    parsed=parse_authentic_corrigendum_replacements(
        correction_text,
        source_id=f"CELEX:{CELEX}",
        locator=(
            f"normalized-visible-text#chars:"
            f"{target_start}-{after_end}"
        ),
    )
    if len(parsed) != 1:
        raise AssertionError(
            f"authentic corrigendum parser did not resolve one replacement: {parsed}"
        )
    if parsed[0]["target_locator"] != "Article 4 > 1":
        raise AssertionError(parsed[0])

    result={
        "probe_version":"0.3",
        "celex":CELEX,
        "language":"ENG",
        "source_route_observations":{
            "cellar_celex":{
                "url":CELLAR_URL,
                "http_status":cellar.status_code,
                "available":cellar.ok,
            },
            "eurlex_html":{
                "url":HTML_URL,
                "final_url":html.url,
                "http_status":html.status_code,
                "media_type":html.headers.get("content-type"),
                "artifact_hash":"sha256:"+hashlib.sha256(html.content).hexdigest(),
            },
            "eurlex_oj_pdf":{
                "url":PDF_URL,
                "final_url":pdf.url,
                "http_status":pdf.status_code,
                "media_type":pdf.headers.get("content-type"),
                "artifact_hash":"sha256:"+hashlib.sha256(pdf.content).hexdigest(),
            },
        },
        "parsed_replacement":parsed[0],
        "correction":{
            "target":"Article 4 > 1",
            "target_source_text":target,
            "locator":(
                f"normalized-visible-text#chars:"
                f"{target_start}-{after_end}"
            ),
            "text":correction_text,
            "text_hash":hashlib.sha256(
                correction_text.encode("utf-8")
            ).hexdigest(),
            "before_fragment":before_fragment,
            "before_hash":hashlib.sha256(
                before_fragment.encode("utf-8")
            ).hexdigest(),
            "after_fragment":after_fragment,
            "after_hash":hashlib.sha256(
                after_fragment.encode("utf-8")
            ).hexdigest(),
            "numbers_removed":["225"],
            "numbers_added":["255"],
        },
        "language_scope":{
            "languages":["ENG"],
            "cross_language_equivalence_assumed":False,
        },
        "invariants":[
            "Cellar CELEX route unavailability is not legal/source absence when another official representation is available.",
            "The operative correction is English-expression scoped.",
            "Do not infer the corrected amount for non-English expressions from absence of a listed corrigendum.",
            "The current corrected base-act display is not evidence that ECU 255 was printed in the original English expression.",
        ],
    }

    if cellar.status_code != 404:
        raise AssertionError(
            "historic-route adversary changed; inspect before weakening fixture: "
            f"Cellar status={cellar.status_code}"
        )

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
