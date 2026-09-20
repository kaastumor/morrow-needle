#!/usr/bin/env python3
from __future__ import annotations

from html.parser import HTMLParser
import hashlib
import json
from pathlib import Path

import requests


CELEX = "32025R0905R(01)"
ELI = (
    "https://data.europa.eu/eli/reg_impl/2025/905/"
    "corrigendum/2026-07-17/oj"
)
EXPECTED_TARGET = "in the amendment to Article 4(1), second sentence"


class _VisibleHTML(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        self.parts.append(data)


def main() -> int:
    result = {
        "probe_version":"0.1",
        "identifier":CELEX,
        "eli":ELI,
        "classification":"AVAILABILITY_UNRESOLVED",
        "legal_contradiction":False,
    }

    try:
        response = requests.get(
            ELI,
            headers={
                "Accept":"text/html",
                "Accept-Language":"en",
                "User-Agent":(
                    "Morrow-Needle-Corrigendum-Availability-Probe/0.1 "
                    "(+https://github.com/kaastumor/morrow-needle)"
                ),
            },
            timeout=120,
            allow_redirects=True,
        )
        result["http_status"] = response.status_code
        result["final_url"] = response.url
        result["media_type"] = (
            response.headers.get("Content-Type","").split(";",1)[0].lower()
        )
        result["payload_sha256"] = hashlib.sha256(response.content).hexdigest()

        if response.ok and result["media_type"] in {
            "text/html",
            "application/xhtml+xml",
        }:
            parser = _VisibleHTML()
            parser.feed(response.text)
            visible = " ".join(" ".join(parser.parts).split())
            result["requested_identifier_present"] = CELEX in visible
            result["interstitial_detected"] = (
                "verify that you're not a robot" in visible.lower()
            )
            result["target_occurrences"] = visible.count(EXPECTED_TARGET)
            result["article3_occurrences"] = visible.count("Article 3")

            if (
                result["requested_identifier_present"]
                and not result["interstitial_detected"]
            ):
                if result["target_occurrences"] != 1:
                    result["classification"] = "CONTENT_CONTRACT_CONFLICT"
                    result["legal_contradiction"] = True
                elif result["article3_occurrences"] != 0:
                    result["classification"] = "CONTENT_CONTRACT_CONFLICT"
                    result["legal_contradiction"] = True
                else:
                    result["classification"] = "AVAILABLE_VERIFIED"
    except requests.RequestException as exc:
        result["retrieval_error"] = type(exc).__name__

    out = Path("artifacts/thread-corrigendum/corrigendum-availability.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        json.dumps(result, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))

    # Network/interstitial availability is an observation, not a legal
    # contradiction. Only retrieved official content that conflicts with the
    # pinned provision-scoped contract fails this probe.
    return 1 if result["legal_contradiction"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
