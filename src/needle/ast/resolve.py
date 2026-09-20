from __future__ import annotations

import re
from typing import Any, Iterable


PREFIXES = {
    "ARTICLE": ("article",),
    "PARAGRAPH": ("paragraph", "para"),
    "SUBPARAGRAPH": ("subparagraph",),
    "POINT": ("point",),
    "ANNEX": ("annex",),
    "CHAPTER": ("chapter",),
    "SECTION": ("section",),
    "PART": ("part",),
}


def normalize_structural_label(kind: str, value: str | None) -> str | None:
    """Normalize a label for legal addressing, not source-text comparison.

    This deliberately strips only addressing decoration: structural type
    prefixes, surrounding whitespace and terminal citation punctuation.
    It must never be used to normalize the legal text itself.
    """
    if value is None:
        return None
    text = re.sub(r"\s+", " ", value).strip()
    if not text:
        return None

    lowered = text.lower()
    for prefix in PREFIXES.get(kind.upper(), ()):
        if lowered == prefix:
            text = ""
            break
        marker = prefix + " "
        if lowered.startswith(marker):
            text = text[len(marker):].strip()
            break

    # Native labels commonly carry "." or ":" as visual punctuation.
    text = re.sub(r"[\s.:;]+$", "", text).strip()
    # Parenthesised subdivision numbers and bare numbers are same address key.
    if re.fullmatch(r"\([A-Za-z0-9IVXLCivxlc-]+\)", text):
        text = text[1:-1]
    return text.casefold() or None


def _candidate_labels(node: dict[str, Any]) -> set[str]:
    values = []
    if node.get("display_label"):
        values.append(node["display_label"])
    citation = node.get("citation_path")
    if citation:
        values.append(citation.rsplit(" > ", 1)[-1])
    if node.get("native_identifier"):
        values.append(node["native_identifier"])

    result = set()
    for value in values:
        normalized = normalize_structural_label(node["kind"], value)
        if normalized:
            result.add(normalized)
    return result


def resolve_structural_path(
    ast: dict[str, Any],
    path: Iterable[tuple[str, str]],
) -> dict[str, Any] | None:
    """Resolve a kind/label path through canonical parent links.

    Example:
        [("ARTICLE", "3"), ("PARAGRAPH", "3")]

    Returns None on no match *or ambiguity*. Callers fail closed.
    """
    nodes = ast.get("nodes", [])
    by_parent: dict[str | None, list[dict[str, Any]]] = {}
    for node in nodes:
        by_parent.setdefault(node.get("parent_id"), []).append(node)

    parents: list[str | None] = [None]
    selected: dict[str, Any] | None = None

    # DOCUMENT can sit above the first requested legal node. Search all nodes
    # for the first path component, then require exact parent-child descent.
    for index, (kind, label) in enumerate(path):
        wanted_kind = kind.upper()
        wanted_label = normalize_structural_label(wanted_kind, label)
        if wanted_label is None:
            return None

        if index == 0:
            candidates = [
                node for node in nodes
                if node.get("kind") == wanted_kind
                and wanted_label in _candidate_labels(node)
            ]
        else:
            parent_ids = {selected["node_id"]} if selected else set()
            candidates = [
                node
                for parent_id in parent_ids
                for node in by_parent.get(parent_id, [])
                if node.get("kind") == wanted_kind
                and wanted_label in _candidate_labels(node)
            ]

        if len(candidates) != 1:
            return None
        selected = candidates[0]

    return selected
