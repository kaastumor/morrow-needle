from __future__ import annotations

from collections import defaultdict
from hashlib import sha256
import re
from typing import Any


DATE_RE = re.compile(
    r"\b(?:\d{1,2}\s+(?:January|February|March|April|May|June|July|August|"
    r"September|October|November|December)\s+\d{4}|\d{4}-\d{2}-\d{2})\b",
    re.IGNORECASE,
)
NUMBER_RE = re.compile(r"(?<![A-Za-z])\d+(?:[.,]\d+)?%?")
REFERENCE_RE = re.compile(
    r"\b(?:Article|Articles|Annex|Annexes|Regulation|Directive|Decision)\s+"
    r"(?:\([A-Z]{2,}\)\s*)?(?:No\s*)?[A-Za-z0-9/().-]+",
    re.IGNORECASE,
)


def _hash(text: str) -> str:
    return sha256(text.encode("utf-8")).hexdigest()


def _node_text(ast: dict[str, Any], node_id: str) -> str:
    segments = sorted(
        (
            segment for segment in ast.get("segments", [])
            if segment["node_id"] == node_id
        ),
        key=lambda segment: (segment.get("document_order", 0), segment.get("ordinal", 0)),
    )
    # Labels/headings are structural alignment aids; BODY/CELL/etc carry the
    # textual state being compared in this first deterministic slice.
    text_segments = [
        segment.get("text_compare", segment.get("text_source", ""))
        for segment in segments
        if segment.get("role") not in {"LABEL", "HEADING"}
    ]
    return " ".join(part.strip() for part in text_segments if part.strip())


def _index(ast: dict[str, Any]) -> dict[tuple[str, str], dict[str, Any]]:
    result = {}
    for node in ast.get("nodes", []):
        citation = node.get("citation_path")
        kind = node.get("kind")
        if not citation or not kind:
            continue
        key = (kind, citation)
        # Duplicate canonical citations are an alignment ambiguity and must
        # fail closed rather than selecting whichever node happens to be last.
        if key in result:
            result[key] = {"AMBIGUOUS": True, "key": key}
        else:
            result[key] = node
    return result


def _tokens(pattern: re.Pattern[str], text: str) -> set[str]:
    return {match.group(0) for match in pattern.finditer(text)}


def feature_deltas(before: str, after: str) -> dict[str, list[str]]:
    def delta(pattern):
        left, right = _tokens(pattern, before), _tokens(pattern, after)
        return sorted(right - left), sorted(left - right)

    numbers_added, numbers_removed = delta(NUMBER_RE)
    dates_added, dates_removed = delta(DATE_RE)
    references_added, references_removed = delta(REFERENCE_RE)
    return {
        "numbers_added":numbers_added,
        "numbers_removed":numbers_removed,
        "dates_added":dates_added,
        "dates_removed":dates_removed,
        "references_added":references_added,
        "references_removed":references_removed,
    }


def diff_same_location(
    before_ast: dict[str, Any],
    after_ast: dict[str, Any],
    *,
    language: str | None = None,
) -> list[dict[str, Any]]:
    """Generate exact-location INSERT/DELETE/REPLACE candidates.

    This is intentionally conservative. Moves, renumbering, split/merge and
    fuzzy alignment are *not* inferred here.
    """
    before_idx, after_idx = _index(before_ast), _index(after_ast)
    keys = sorted(set(before_idx) | set(after_idx))
    candidates = []

    for kind, citation in keys:
        before_node = before_idx.get((kind, citation))
        after_node = after_idx.get((kind, citation))

        if (before_node and before_node.get("AMBIGUOUS")) or (
            after_node and after_node.get("AMBIGUOUS")
        ):
            continue

        before_text = _node_text(before_ast, before_node["node_id"]) if before_node else ""
        after_text = _node_text(after_ast, after_node["node_id"]) if after_node else ""

        if before_node and after_node and before_text == after_text:
            continue

        if before_node is None:
            operation = "INSERT"
        elif after_node is None:
            operation = "DELETE"
        else:
            operation = "REPLACE"

        parent = (after_node or before_node).get("parent_id")
        parent_citation = None
        if parent:
            source_ast = after_ast if after_node else before_ast
            parent_node = next(
                (node for node in source_ast.get("nodes", []) if node["node_id"] == parent),
                None,
            )
            parent_citation = parent_node.get("citation_path") if parent_node else None

        candidate_id = sha256(
            f"{before_ast['state_id']}|{after_ast['state_id']}|{kind}|{citation}|{operation}".encode()
        ).hexdigest()[:24]

        candidates.append({
            "candidate_id":candidate_id,
            "operation":operation,
            "target":{
                "kind":kind,
                "citation_path":citation,
                "parent_citation_path":parent_citation,
                "language":language,
            },
            "alignment_basis":"EXACT_CITATION_AND_KIND",
            "before":None if not before_node else {
                "state_id":before_ast["state_id"],
                "node_id":before_node["node_id"],
                "text_hash":_hash(before_text),
                "text_length":len(before_text),
            },
            "after":None if not after_node else {
                "state_id":after_ast["state_id"],
                "node_id":after_node["node_id"],
                "text_hash":_hash(after_text),
                "text_length":len(after_text),
            },
            "feature_deltas":feature_deltas(before_text, after_text),
            "reconciliation_state":"DIFF_ONLY",
            "verification_state":"UNVERIFIED",
            "supporting_evidence":[{
                "channel":"DETERMINISTIC_DIFF",
                "source_id":f"{before_ast['state_id']}->{after_ast['state_id']}",
                "operation":operation,
                "target_locator":citation,
                "authority_character":"DERIVED",
                "locator":None,
            }],
            "conflicting_evidence":[],
            "notes":None,
        })

    return candidates
