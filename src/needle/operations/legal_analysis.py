from __future__ import annotations

import hashlib
import json
from typing import Any, Iterable


class OperationalLegalAnalysisError(ValueError):
    pass


def _digest(value: Any) -> str:
    payload=json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()[:32]


def should_attempt_legal_analysis(*, relevance: str, source_change: dict[str, Any]) -> bool:
    """Return whether the source state permits a canonical legal-analysis attempt."""
    if relevance != "LEGAL_RESOURCE_CANDIDATE":
        return False
    classification=source_change.get("classification")
    if classification == "CONTENT_CHANGED":
        return True
    if classification != "UNRESOLVED":
        return False
    basis=set(source_change.get("classification_basis",[]))
    return "MISSING_BASELINE" in basis and "MISSING_OBSERVATION" not in basis


def _semantic_key(candidate: dict[str, Any]) -> str:
    key=candidate.get("semantic_key")
    if not key:
        raise OperationalLegalAnalysisError("legal-analysis candidate requires semantic_key")
    return str(key)


def collapse_evidence_candidates(candidates: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    """Collapse duplicate representations while retaining every evidence occurrence."""
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


def apply_operational_recency_gate(
    legal_analysis: dict[str, Any],
    *,
    recency: dict[str, Any] | None,
) -> dict[str, Any]:
    """Gate CHANGE_FEED eligibility using separately-owned temporal evidence.

    Recency evidence must explicitly bind itself to this legal-analysis identity.
    Merely supplying a valid temporal assertion from the same instrument is not
    sufficient: an unrelated provision/application date must never make another
    mutation appear current.
    """
    if legal_analysis.get("disposition") != "LEGAL_CHANGE_VERIFIED":
        return legal_analysis

    analysis_identity=legal_analysis.get("analysis_identity")
    if not analysis_identity:
        raise OperationalLegalAnalysisError("verified legal analysis requires analysis_identity before recency gating")

    if recency is None:
        state="UNRESOLVED"
        assertion_refs=[]
    else:
        state=recency.get("state")
        assertion_refs=list(recency.get("assertion_refs",[]))
        bound_identity=recency.get("legal_analysis_identity")
        if bound_identity != analysis_identity:
            raise OperationalLegalAnalysisError(
                "operational recency evidence must bind to the gated legal_analysis_identity"
            )

    if state == "CURRENT_RELEVANT":
        if not assertion_refs:
            raise OperationalLegalAnalysisError(
                "CURRENT_RELEVANT recency requires canonical temporal/procedural assertion_refs"
            )
        result=dict(legal_analysis)
        result["evidence_refs"]=list(dict.fromkeys([
            *result.get("evidence_refs",[]), *assertion_refs
        ]))
        result["recency"]={"state":state,"assertion_refs":assertion_refs,"legal_analysis_identity":analysis_identity}
        return result

    if state not in {"HISTORICAL_NOT_CURRENT","UNRESOLVED","CONTEXT_REQUIRED","CONFLICTING"}:
        raise OperationalLegalAnalysisError(f"unsupported operational recency state: {state}")

    if state == "HISTORICAL_NOT_CURRENT" and not assertion_refs:
        raise OperationalLegalAnalysisError(
            "HISTORICAL_NOT_CURRENT recency requires canonical temporal/procedural assertion_refs"
        )

    reason={
        "HISTORICAL_NOT_CURRENT":"The legal mutation is verified, but canonical temporal/procedural evidence establishes that it is historical rather than newly relevant to this feed window.",
        "UNRESOLVED":"The legal mutation is verified, but Needle lacks canonical temporal/procedural evidence that it is newly relevant to this feed window.",
        "CONTEXT_REQUIRED":"The legal mutation is verified, but operational recency depends on unresolved legal context.",
        "CONFLICTING":"The legal mutation is verified, but canonical temporal/procedural evidence conflicts on operational recency.",
    }[state]
    return {
        "disposition":"ABSTAIN_LEGAL_UNRESOLVED",
        "verification_route":legal_analysis.get("verification_route"),
        "canonical_refs":list(legal_analysis.get("canonical_refs",[])),
        "evidence_refs":list(dict.fromkeys([*legal_analysis.get("evidence_refs",[]),*assertion_refs])),
        "explanation":None,
        "unknowns":[*legal_analysis.get("unknowns",[]),reason],
        "analysis_identity":analysis_identity,
        "recency":{"state":state,"assertion_refs":assertion_refs,"legal_analysis_identity":analysis_identity},
    }


def analyze_operational_legal(
    event: dict[str, Any],
    source_change: dict[str, Any],
    *,
    candidates: Iterable[dict[str, Any]],
) -> dict[str, Any]:
    """Return the bounded downstream outcome consumed by operations.pipeline."""
    if source_change.get("event_key") != event.get("event_key"):
        raise OperationalLegalAnalysisError("source change does not belong to event")

    collapsed=collapse_evidence_candidates(candidates)
    verified=[c for c in collapsed if c.get("outcome") == "LEGAL_CHANGE_VERIFIED"]
    non_impact=[c for c in collapsed if c.get("outcome") == "LEGAL_NON_IMPACT_VERIFIED"]

    if verified and non_impact:
        return {
            "disposition":"ABSTAIN_LEGAL_UNRESOLVED","verification_route":None,"canonical_refs":[],
            "evidence_refs":sorted({ref for c in collapsed for ref in c.get("evidence_refs",[])}),
            "explanation":None,
            "unknowns":["Canonical analyzers produced conflicting verified-change and verified-non-impact outcomes for the same operational event."],
        }
    if len(verified) > 1:
        return {
            "disposition":"ABSTAIN_LEGAL_UNRESOLVED","verification_route":None,"canonical_refs":[],
            "evidence_refs":sorted({ref for c in verified for ref in c.get("evidence_refs",[])}),
            "explanation":None,
            "unknowns":["More than one distinct verified legal mutation candidate remains after representation deduplication; automatic selection is forbidden."],
        }

    chosen=verified[0] if verified else (non_impact[0] if len(non_impact) == 1 else None)
    if chosen is None:
        return {
            "disposition":"ABSTAIN_LEGAL_UNRESOLVED","verification_route":None,"canonical_refs":[],
            "evidence_refs":sorted({ref for c in collapsed for ref in c.get("evidence_refs",[])}),
            "explanation":None,
            "unknowns":["No unique evidence-backed legal outcome was established by canonical analyzers."],
        }

    route=chosen.get("verification_route")
    if route not in {"AUTHENTIC_LEGAL_CAUSE","SOURCE_DIFF"}:
        raise OperationalLegalAnalysisError("verified legal outcome requires an allowed verification_route")
    result={
        "disposition":chosen["outcome"],"verification_route":route,
        "canonical_refs":list(chosen.get("canonical_refs",[])),
        "evidence_refs":list(dict.fromkeys(chosen.get("evidence_refs",[]))),
        "explanation":chosen.get("explanation"),"unknowns":list(chosen.get("unknowns",[])),
    }
    result["analysis_identity"]="operational-legal-analysis:"+_digest({
        "event_key":event["event_key"],"source_change_id":source_change.get("change_id"),
        "semantic_key":chosen["semantic_key"],"outcome":chosen["outcome"],"verification_route":route,
    })
    return result
