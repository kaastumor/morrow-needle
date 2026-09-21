from __future__ import annotations

import hashlib
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
    match = re.match(r"(Article\s+[A-Za-z0-9IVXLC.-]+)\s*\(\s*([A-Za-z0-9.-]+)\s*\)$", value, re.I)
    if match:
        return f"{match.group(1)} > {match.group(2)}"
    match = re.match(r"(Article\s+[A-Za-z0-9IVXLC().-]+)\s*,?\s*paragraph\s+([A-Za-z0-9().-]+)$", value, re.I)
    if match:
        return f"{match.group(1)} > {match.group(2).strip('()')}"
    return value


def parse_authentic_instructions(text: str, *, source_id: str, locator: str | None = None, include_match_span: bool = False) -> list[dict[str, Any]]:
    """Extract only explicit amendment commands that are safe to assert."""
    evidence = []
    for match in REPLACEMENT_RE.finditer(text):
        resolved_locator = locator
        if include_match_span and locator is not None:
            resolved_locator = f"{locator}#normalized-chars:{match.start()}-{match.end()}"
        evidence.append({"channel":"AUTHENTIC_ACT","source_id":source_id,"operation":"REPLACE","target_locator":_canonical_target(match.group("target")),"authority_character":"CANONICAL_LEGAL_CAUSE","locator":resolved_locator})
    return evidence


CORRIGENDUM_TARGET_RE = re.compile(r"On\s+page\s+\d+.*?(?P<target>Article\s+[A-Za-z0-9IVXLC.-]+\s*\(\s*[A-Za-z0-9.-]+\s*\))\s*:", re.IGNORECASE)
CORRIGENDUM_FOR_READ_RE = re.compile(r"\bfor\s*:\s*(?:/\s*)*(?P<before>.*?)\s*(?:/\s*)*\bread\s*:\s*(?:/\s*)*(?P<after>.*?)(?=$|\n)", re.IGNORECASE)


def _clean_corrigendum_fragment(value: str) -> str:
    value=re.sub(r"^\s*[0-9]+(?:\.[0-9]+)?\s*(?://\s*)*", "", value)
    value=value.strip().strip(" /,;:.").strip("'\"‘’“”").strip()
    return re.sub(r"\s+", " ", value)


def parse_authentic_corrigendum_replacements(text: str, *, source_id: str, locator: str | None = None) -> list[dict[str, Any]]:
    """Parse explicit English corrigendum for/read replacement commands."""
    normalized=" ".join(text.split())
    target_match=CORRIGENDUM_TARGET_RE.search(normalized)
    if target_match is None:
        return []
    replace_match=CORRIGENDUM_FOR_READ_RE.search(normalized[target_match.end():])
    if replace_match is None:
        return []
    before=_clean_corrigendum_fragment(replace_match.group("before")); after=_clean_corrigendum_fragment(replace_match.group("after"))
    if not before or not after or before == after:
        return []
    target=_canonical_target(target_match.group("target"))
    return [{"target_locator":target,"target_source_text":target_match.group(0),"before_text":before,"after_text":after,"evidence":{"channel":"AUTHENTIC_ACT","source_id":source_id,"operation":"REPLACE","target_locator":target,"authority_character":"CANONICAL_LEGAL_CAUSE","locator":locator}}]


# Keep this intentionally specific. Expanding drafting coverage requires an
# authentic adversarial fixture; a near-match must abstain rather than guess.
KEYED_ROW_INSERT_RE = re.compile(
    r"in\s+(?P<part>Part\s+[A-Za-z0-9IVXLC.-]+)\s*,\s*"
    r"(?P<section>Section\s+[A-Za-z0-9IVXLC.-]+)\s*,\s*"
    r"in\s+the\s+entry\s+for\s+the\s+(?P<entry>[^,]+)\s*,\s*"
    r"the\s+following\s+rows\s+for\s+the\s+zones\s+"
    r"(?P<key1>[A-Z]{2}-[A-Z0-9.]+)\s+and\s+"
    r"(?P<key2>[A-Z]{2}-[A-Z0-9.]+)\s+"
    r"are\s+added\s+after\s+the\s+row\s+for\s+the\s+zone\s+"
    r"(?P<anchor>[A-Z]{2}-[A-Z0-9.]+)", re.IGNORECASE)


def _canonical_row_key(value: str) -> str:
    # A terminal full stop belongs to the sentence, not the legal row key.
    # Preserve internal dots (for example US-2.1404) while stripping only
    # source punctuation outside the identifier.
    return value.rstrip(".,;:")


def parse_authentic_keyed_row_insertions(text: str, *, source_id: str, parent_locator: str, locator: str | None = None) -> list[dict[str, Any]]:
    """Parse explicit keyed-table row insertion commands."""
    normalized=" ".join(text.split()); parsed=[]
    for match in KEYED_ROW_INSERT_RE.finditer(normalized):
        keys=[_canonical_row_key(match.group("key1")),_canonical_row_key(match.group("key2"))]
        part=" ".join(match.group("part").split()); section=" ".join(match.group("section").split()); entry=" ".join(match.group("entry").split()); anchor=_canonical_row_key(match.group("anchor"))
        target=f"{parent_locator} > {part} > {section} > {entry} > rows {keys[0]}, {keys[1]}"
        parsed.append({"operation":"INSERT","target_locator":target,"inserted_keys":keys,"placement_anchor":anchor,"instruction_text":match.group(0),"evidence":{"channel":"AUTHENTIC_ACT","source_id":source_id,"operation":"INSERT","target_locator":target,"authority_character":"CANONICAL_LEGAL_CAUSE","locator":locator}})
    return parsed


def candidate_from_authentic_instruction(instruction: dict[str, Any], *, kind: str, language: str | None, candidate_id: str | None = None) -> dict[str, Any]:
    """Create a v0.3 mutation from an explicit authentic command."""
    evidence=instruction.get("evidence")
    if not isinstance(evidence,dict): raise ValueError("authentic instruction lacks evidence")
    if evidence.get("channel") != "AUTHENTIC_ACT": raise ValueError("candidate requires AUTHENTIC_ACT evidence")
    if evidence.get("authority_character") != "CANONICAL_LEGAL_CAUSE": raise ValueError("candidate requires canonical legal cause")
    operation=instruction.get("operation")
    if operation not in {"INSERT","DELETE","REPLACE"}: raise ValueError(f"unsupported authentic-only operation: {operation}")
    target=instruction.get("target_locator")
    if not target or target != evidence.get("target_locator"): raise ValueError("instruction target must exactly match authentic evidence target")
    if evidence.get("operation") != operation: raise ValueError("instruction operation must exactly match authentic evidence")
    if candidate_id is None:
        material="|".join([evidence.get("source_id",""),operation,target,evidence.get("locator") or ""])
        candidate_id=f"authentic-mutation:{hashlib.sha256(material.encode('utf-8')).hexdigest()[:20]}"
    return {"candidate_id":candidate_id,"operation":operation,"target":{"kind":kind,"citation_path":target,"parent_citation_path":" > ".join(target.split(" > ")[:-1]) or None,"language":language},"alignment_basis":"SOURCE_NATIVE_IDENTIFIER","before":None,"after":None,"feature_deltas":{"numbers_added":[],"numbers_removed":[],"dates_added":[],"dates_removed":[],"references_added":[],"references_removed":[]},"reconciliation_state":"AUTHENTIC_CAUSE_ONLY","verification_state":"VERIFIED","supporting_evidence":[evidence],"conflicting_evidence":[],"notes":"Verified directly from an explicit authentic amendment instruction. No consolidated after-state is asserted.","candidate_origin":"AUTHENTIC_INSTRUCTION"}
