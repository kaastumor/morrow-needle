from __future__ import annotations

import hashlib
import json
from typing import Any, Iterable


class OperationalLegalAnalysisError(ValueError):
    pass


def _digest(value: Any) -> str:
    payload=json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()[:32]


def _semantic_key(candidate: dict[str, Any]) -> str:
    """Identity supplied by canonical analysis, never by representation occurrence."""
    key=candidate.get("semantic_key")
    if not key:
        raise OperationalLegalAnalysisError("legal-analysis candidate requires semantic_key")
    return str(key)


def collapse_evidence_candidates(candidates: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    """Collapse duplicate representations while retaining every evidence occurrence.

    A semantic key is produced by the canonical parser/mutation service. This adapter
    deliberately does not derive semantic identity from CELEX ids, locators or text
    similarity: doing so here would create a second legal truth model.
    """
    grouped: dict[str, dict[str, Any]]={}
    for raw in candidates:
        candidate=dict(raw)
        key=_semantic_key(candidate)
        occurrences=list(candidate.pop("evidence_occurrences",[]))
        if key not in grouped:
            candidate["evidence_occurrences"]=[]
            grouped[key]=candidate
        else:
            left={k:v for k,v in grouped[key].items() if k != "evidence_occurrences"}
            right={k:v for k,v in candidate.items() if k != "evidence_occurrences"}
            if left != right:
                raise OperationalLegalAnalysisError(
                    f"conflicting canonical candidates share semantic_key {key}"
                )
        existing=grouped[key]["evidence_occurrences"]
        for occurrence in occurrences:
            if occurrence not in existing:
                existing.append(occurrence)
    return [grouped[key] for key in sorted(grouped)]


def analyze_operational_legal(
    event: dict[str, Any],
    source_change: dict[str, Any],
    *,
    candidates: Iterable[dict[str, Any]],
) -> dict[str, Any]:
    """Return the bounded downstream outcome consumed by operations.pipeline.

    `candidates` are canonical analyzer outputs. The adapter arbitrates them; it
    does not parse legislation itself. That keeps the recurring monitor generic
    and prevents case-specific CELEX dispatch from becoming production logic.
    """
    if source_change.get("event_key") != event.get("event_key"):
        raise OperationalLegalAnalysisError("source change does not belong to event")

    collapsed=collapse_evidence_candidates(candidates)
    verified=[c for c in collapsed if c.get("outcome") == "LEGAL_CHANGE_VERIFIED"]
    non_impact=[c for c in collapsed if c.get("outcome") == "LEGAL_NON_IMPACT_VERIFIED"]

    if verified and non_impact:
        return {
            "disposition":"ABSTAIN_LEGAL_UNRESOLVED",
            "verification_route":None,
            "canonical_refs":[],
            "evidence_refs":sorted({ref for c in collapsed for ref in c.get("evidence_refs",[])}),
            "explanation":None,
            "unknowns":["Canonical analyzers produced conflicting verified-change and verified-non-impact outcomes for the same operational event."],
        }
    if len(verified) > 1:
        return {
            "disposition":"ABSTAIN_LEGAL_UNRESOLVED",
            "verification_route":None,
            "canonical_refs":[],
            "evidence_refs":sorted({ref for c in verified for ref in c.get("evidence_refs",[])}),
            "explanation":None,
            "unknowns":["More than one distinct verified legal mutation candidate remains after representation deduplication; automatic selection is forbidden."],
        }

    chosen=verified[0] if verified else (non_impact[0] if len(non_impact) == 1 else None)
    if chosen is None:
        return {
            "disposition":"ABSTAIN_LEGAL_UNRESOLVED",
            "verification_route":None,
            "canonical_refs":[],
            "evidence_refs":sorted({ref for c in collapsed for ref in c.get("evidence_refs",[])}),
            "explanation":None,
            "unknowns":["No unique evidence-backed legal outcome was established by canonical analyzers."],
        }

    route=chosen.get("verification_route")
    if route not in {"AUTHENTIC_LEGAL_CAUSE","SOURCE_DIFF"}:
        raise OperationalLegalAnalysisError("verified legal outcome requires an allowed verification_route")
    result={
        "disposition":chosen["outcome"],
        "verification_route":route,
        "canonical_refs":list(chosen.get("canonical_refs",[])),
        "evidence_refs":list(dict.fromkeys(chosen.get("evidence_refs",[]))),
        "explanation":chosen.get("explanation"),
        "unknowns":list(chosen.get("unknowns",[])),
    }
    # Deterministic audit identity is intentionally not consumed as canonical truth.
    result["analysis_identity"]="operational-legal-analysis:"+_digest({
        "event_key":event["event_key"],
        "source_change_id":source_change.get("change_id"),
        "semantic_key":chosen["semantic_key"],
        "outcome":chosen["outcome"],
        "verification_route":route,
    })
    return result
