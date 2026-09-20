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
    # Map common Article 4 (1) corrigendum notation onto citation paths.
    match = re.match(
        r"(Article\s+[A-Za-z0-9IVXLC.-]+)\s*\(\s*([A-Za-z0-9.-]+)\s*\)$",
        value,
        re.I,
    )
    if match:
        return f"{match.group(1)} > {match.group(2)}"

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
    include_match_span: bool = False,
) -> list[dict[str, Any]]:
    """Extract only explicit amendment commands that are safe to assert.

    The output is evidence for reconciliation, not a semantic Change Atom.
    Absence of a recognised command is NO ASSERTION.
    """
    evidence = []
    for match in REPLACEMENT_RE.finditer(text):
        resolved_locator = locator
        if include_match_span and locator is not None:
            resolved_locator = (
                f"{locator}#normalized-chars:{match.start()}-{match.end()}"
            )
        evidence.append({
            "channel":"AUTHENTIC_ACT",
            "source_id":source_id,
            "operation":"REPLACE",
            "target_locator":_canonical_target(match.group("target")),
            "authority_character":"CANONICAL_LEGAL_CAUSE",
            "locator":resolved_locator,
        })
    return evidence



CORRIGENDUM_TARGET_RE = re.compile(
    r"On\s+page\s+\d+.*?(?P<target>Article\s+[A-Za-z0-9IVXLC.-]+\s*\(\s*[A-Za-z0-9.-]+\s*\))\s*:",
    re.IGNORECASE,
)
CORRIGENDUM_FOR_READ_RE = re.compile(
    r"\bfor\s*:\s*(?:/\s*)*(?P<before>.*?)"
    r"\s*(?:/\s*)*\bread\s*:\s*(?:/\s*)*(?P<after>.*?)(?=$|\n)",
    re.IGNORECASE,
)


def _clean_corrigendum_fragment(value: str) -> str:
    value=re.sub(r"^\s*[0-9]+(?:\.[0-9]+)?\s*(?://\s*)*", "", value)
    value=value.strip()
    value=value.strip(" /,;:.")
    value=value.strip("'\"‘’“”")
    value=value.strip()
    value=re.sub(r"\s+", " ", value)
    return value


def parse_authentic_corrigendum_replacements(
    text: str,
    *,
    source_id: str,
    locator: str | None = None,
) -> list[dict[str, Any]]:
    """Parse explicit English corrigendum for/read replacement commands.

    This deliberately requires a nearby Article subdivision locator. It returns
    replacement details plus a schema-compatible authentic evidence object.
    Unsupported or ambiguous corrigendum wording abstains.
    """
    normalized=" ".join(text.split())
    target_match=CORRIGENDUM_TARGET_RE.search(normalized)
    if target_match is None:
        return []

    instruction_start=target_match.end()
    instruction=normalized[instruction_start:]
    replace_match=CORRIGENDUM_FOR_READ_RE.search(instruction)
    if replace_match is None:
        return []

    before=_clean_corrigendum_fragment(replace_match.group("before"))
    after=_clean_corrigendum_fragment(replace_match.group("after"))
    if not before or not after or before == after:
        return []

    target=_canonical_target(target_match.group("target"))
    return [{
        "target_locator":target,
        "target_source_text":target_match.group(0),
        "before_text":before,
        "after_text":after,
        "evidence":{
            "channel":"AUTHENTIC_ACT",
            "source_id":source_id,
            "operation":"REPLACE",
            "target_locator":target,
            "authority_character":"CANONICAL_LEGAL_CAUSE",
            "locator":locator,
        },
    }]
