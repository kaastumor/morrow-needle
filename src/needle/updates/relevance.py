from __future__ import annotations

from typing import Any


def classify_event_relevance(event: dict[str, Any]) -> str:
    """Classify whether a Cellar notification is a legal-resource candidate.

    This is an operational routing hint, not a legal-state conclusion.
    """
    identifiers=[value.lower() for value in event.get("identifiers",[])]
    if any(value.startswith("celex:") for value in identifiers):
        return "LEGAL_RESOURCE_CANDIDATE"

    class_tails={
        value.rsplit("#",1)[-1].rsplit("/",1)[-1].lower()
        for value in event.get("classes",[])
    }
    if "signature_digital" in class_tails:
        return "SOURCE_INFRASTRUCTURE"

    if identifiers and all(
        value.startswith("oj:") and "_sig" in value
        for value in identifiers
    ):
        return "SOURCE_INFRASTRUCTURE"

    return "UNRESOLVED_RESOURCE"
