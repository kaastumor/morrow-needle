#!/usr/bin/env python3
from __future__ import annotations

from html.parser import HTMLParser
import hashlib
import json
from pathlib import Path

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
PINNED=Path("fixtures/audit/reg2742-money-corrigendum-source-v0.1.json")


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
    return requests.get(
        url,
        headers={
            "Accept":accept,
            "Accept-Language":"eng",
            "User-Agent":(
                "Morrow-Needle-Money-Corrigendum-Probe/0.4 "
                "(+https://github.com/kaastumor/morrow-needle)"
            ),
        },
        timeout=120,
        allow_redirects=True,
    )


def main() -> int:
    pinned=json.loads(PINNED.read_text(encoding="utf-8"))
    expected=pinned["correction"]

    cellar=fetch(CELLAR_URL,accept="application/zip;mtype=fmx4")
    html=fetch(HTML_URL,accept="text/html")
    pdf=fetch(PDF_URL,accept="application/pdf")

    route_observations={
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
            "artifact_hash":(
                "sha256:"+hashlib.sha256(html.content).hexdigest()
                if html.content else None
            ),
        },
        "eurlex_oj_pdf":{
            "url":PDF_URL,
            "final_url":pdf.url,
            "http_status":pdf.status_code,
            "media_type":pdf.headers.get("content-type"),
            "artifact_hash":(
                "sha256:"+hashlib.sha256(pdf.content).hexdigest()
                if pdf.content else None
            ),
        },
    }

    availability_state="AVAILABILITY_UNRESOLVED"
    parsed=[]
    live_correction=None

    if html.ok:
        text=normalized_html_text(html.content)
        target=expected["text"].split(" 1.2 //",1)[0]
        has_target=target in text
        has_before=expected["before_fragment"] in text
        has_after=expected["after_fragment"] in text

        if has_target and has_before and has_after:
            target_start=text.index(target)
            after_end=text.index(expected["after_fragment"],target_start)+len(
                expected["after_fragment"]
            )
            correction_text=text[target_start:after_end]
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
                    "official content is present but parser no longer resolves "
                    f"one replacement: {parsed}"
                )
            replacement=parsed[0]
            if replacement["target_locator"] != expected["target"]:
                raise AssertionError(
                    f"live corrigendum target changed: {replacement}"
                )
            if expected["before_fragment"] not in replacement["before_text"]:
                raise AssertionError(
                    f"live before-fragment changed: {replacement}"
                )
            if expected["after_fragment"] not in replacement["after_text"]:
                raise AssertionError(
                    f"live after-fragment changed: {replacement}"
                )
            live_correction={
                "target":replacement["target_locator"],
                "locator":(
                    f"normalized-visible-text#chars:"
                    f"{target_start}-{after_end}"
                ),
                "text":correction_text,
                "text_hash":hashlib.sha256(
                    correction_text.encode("utf-8")
                ).hexdigest(),
            }
            availability_state="AVAILABLE_VERIFIED"
        elif any((has_target,has_before,has_after)):
            # Partial appearance of the pinned legal content is more suspicious
            # than a generic interstitial: fail closed for manual inspection.
            raise AssertionError({
                "state":"PARTIAL_EXPECTED_LEGAL_CONTENT",
                "has_target":has_target,
                "has_before":has_before,
                "has_after":has_after,
                "html_status":html.status_code,
            })

    if pdf.ok and pdf.content and not pdf.content.startswith(b"%PDF"):
        raise AssertionError(
            f"official OJ PDF route returned {pdf.headers.get('content-type')}"
        )

    result={
        "probe_version":"0.4",
        "celex":CELEX,
        "language":"ENG",
        "availability_state":availability_state,
        "pinned_legal_evidence":{
            "fixture_id":pinned["fixture_id"],
            "artifact_hash":pinned["source_observation"]["artifact_hash"],
            "correction_text_hash":expected["text_hash"],
        },
        "source_route_observations":route_observations,
        "parsed_replacement":parsed[0] if parsed else None,
        "live_correction":live_correction,
        "invariants":pinned["invariants"],
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
