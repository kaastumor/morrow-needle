from __future__ import annotations

import re
from typing import Any

# Deliberately narrow first slice: explicit English replacement commands in an
# authentic amending act. Unsupported drafting forms abstain rather than guess.
REPLACEMENT_RE = re.compile(
    r"(?P<target>(?:Article|Annex)\s+[A-Za-z0-9IVXLC().-]+(?:\s*,?\s*(?:paragraph|point|subparagraph)\s+[A-Za-z0-9().-]+)?)"
    r"\s+(?:is|are)\s+replaced\s+by\s+(?:the\s+following|the following text)",
    re.IGNORECASE,
)


def _canonical_target(raw: str) -> str:
    value = re.sub(r"\s+", " ", raw.strip()).rstrip(",")
    # Map common amendment drafting locators onto Needle citation paths.
    match = re.match(
        r"(Article\s+[A-Za-z0-9IVXLC().-]+)\s*,?\s*paragraph\s+([A-Za-z0-9().-]+)$",
        value,
        re.I,
    )
    if match:
        return f"{match.group(1)} > {match.group(2).strip('()')}"
    return value


def parse_authentic_instructions(
    text: str,
    *,
    source_id: str,
    locator: str | None = None,
) -> list[dict[str, Any]]:
    """Extract only explicit amendment commands that are safe to assert.

    The output is evidence for reconciliation, not a semantic Change Atom.
    Absence of a recognised command is NO ASSERTION.
    """
    evidence = []
    for match in REPLACEMENT_RE.finditer(text):
        evidence.append({
            "channel":"AUTHENTIC_ACT",
            "source_id":source_id,
            "operation":"REPLACE",
            "target_locator":_canonical_target(match.group("target")),
            "authority_character":"CANONICAL_LEGAL_CAUSE",
            "locator":locator,
        })
    return evidence
