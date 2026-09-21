from __future__ import annotations

import hashlib
import json
from datetime import date, datetime, timedelta
from typing import Any, Iterable


class OperationalLegalAnalysisError(ValueError):
    pass


RELEVANCE_DIMENSIONS={
    "PUBLICATION","ENTRY_INTO_FORCE","APPLICATION_START","APPLICATION_END",
    "TRANSITION_BOUNDARY","DEADLINE","PROCEDURAL_MILESTONE","ENTITY_SPECIFIC_TRIGGER",
}

_TEMPORAL_RELEVANCE = {
    ("PUBLICATION", "POINT"): "PUBLICATION",
    ("PUBLICATION", "START"): "PUBLICATION",
    ("LEGAL_FORCE", "START"): "ENTRY_INTO_FORCE",
    ("APPLICATION", "START"): "APPLICATION_START",
    ("APPLICATION", "END"): "APPLICATION_END",
    ("TRANSITION", "POINT"): "TRANSITION_BOUNDARY",
    ("TRANSITION", "START"): "TRANSITION_BOUNDARY",
    ("TRANSITION", "END"): "TRANSITION_BOUNDARY",
    ("DEADLINE", "POINT"): "DEADLINE",
    ("DEADLINE", "END"): "DEADLINE",
}


def _digest(value: Any) -> str:
    payload=json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()[:32]


def should_attempt_legal_analysis(*, relevance: str, source_change: dict[str, Any]) -> bool:
    if relevance != "LEGAL_RESOURCE_CANDIDATE": return False
    classification=source_change.get("classification")
    if classification == "CONTENT_CHANGED": return True
    if classification != "UNRESOLVED": return False
    basis=set(source_change.get("classification_basis",[]))
    return "MISSING_BASELINE" in basis and "MISSING_OBSERVATION" not in basis


def _semantic_key(candidate: dict[str, Any]) -> str:
    key=candidate.get("semantic_key")
    if not key: raise OperationalLegalAnalysisError("legal-analysis candidate requires semantic_key")
    return str(key)


def collapse_evidence_candidates(candidates: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, dict[str, Any]]={}
    for raw in candidates:
        candidate=dict(raw); key=_semantic_key(candidate); occurrences=list(candidate.pop("evidence_occurrences",[]))
        if key not in grouped:
            candidate["evidence_occurrences"]=[]; grouped[key]=candidate
        else:
            left={k:v for k,v in grouped[key].items() if k != "evidence_occurrences"}
            right={k:v for k,v in candidate.items() if k != "evidence_occurrences"}
            if left != right: raise OperationalLegalAnalysisError(f"conflicting canonical candidates share semantic_key {key}")
        existing=grouped[key]["evidence_occurrences"]
        for occurrence in occurrences:
            if occurrence not in existing: existing.append(occurrence)
    return [grouped[key] for key in sorted(grouped)]


def derive_operational_relevance(
    legal_analysis: dict[str, Any], *, temporal_assertions: Iterable[dict[str, Any]],
    window_start: str, window_end: str,
) -> dict[str, Any]:
    """Project already-bound canonical temporal truth into operational relevance.

    Callers must supply only assertions canonically bound to the gated legal analysis;
    this function never discovers, guesses, or cross-binds legal subjects. The window is
    half-open [start, end), matching polling semantics.
    """
    identity=legal_analysis.get("analysis_identity")
    if legal_analysis.get("disposition") != "LEGAL_CHANGE_VERIFIED" or not identity:
        raise OperationalLegalAnalysisError("operational relevance requires a verified legal analysis with analysis_identity")
    start=date.fromisoformat(window_start); end=date.fromisoformat(window_end)
    if end <= start: raise OperationalLegalAnalysisError("operational relevance window_end must be after window_start")

    assertions=list(temporal_assertions)
    if not assertions:
        return {"state":"UNRESOLVED","assertion_refs":[],"legal_analysis_identity":identity}
    if any(a.get("resolution_state") == "CONFLICTING" for a in assertions):
        return {"state":"CONFLICTING","assertion_refs":[a["assertion_id"] for a in assertions],"legal_analysis_identity":identity}
    if any(a.get("resolution_state") == "CONTEXT_REQUIRED" for a in assertions):
        return {"state":"CONTEXT_REQUIRED","assertion_refs":[a["assertion_id"] for a in assertions if a.get("resolution_state") == "CONTEXT_REQUIRED"],"legal_analysis_identity":identity}

    resolved=[]
    for assertion in assertions:
        dimension=_TEMPORAL_RELEVANCE.get((assertion.get("dimension"),assertion.get("boundary")))
        value=assertion.get("normalized_date")
        if dimension and assertion.get("resolution_state") == "RESOLVED_ABSOLUTE" and value:
            resolved.append((date.fromisoformat(value),dimension,assertion["assertion_id"]))
    current=[item for item in resolved if start <= item[0] < end]
    if len(current) == 1:
        when,dimension,ref=current[0]
        return {"state":"CURRENT_RELEVANT","assertion_refs":[ref],"legal_analysis_identity":identity,"relevance_dimension":dimension,"relevant_at":when.isoformat()}
    if len(current) > 1:
        # Multiple simultaneous legal relevance events are true, but v0.1 has no
        # precedence rule for choosing the public feed reason. Do not invent one.
        return {"state":"CONFLICTING","assertion_refs":[item[2] for item in current],"legal_analysis_identity":identity}
    if resolved and all(item[0] < start for item in resolved):
        return {"state":"HISTORICAL_NOT_CURRENT","assertion_refs":[item[2] for item in resolved],"legal_analysis_identity":identity}
    return {"state":"UNRESOLVED","assertion_refs":[item[2] for item in resolved],"legal_analysis_identity":identity}


def derive_feed_event_relevance(
    legal_analysis: dict[str, Any],
    *,
    temporal_assertions: Iterable[dict[str, Any]],
    ingestion_time: str,
) -> dict[str, Any]:
    """Relate day-granular legal timing to one newly processed feed event.

    The source feed timestamp establishes operational novelty only. It is never
    substituted for a legal publication/application timestamp. The event's own
    explicit offset determines its source-calendar day; canonical legal dates
    are then evaluated against that one-day interval.

    This deliberately accepts a conservative false negative for delayed feed
    delivery: an older publication date is historical even if Needle first sees
    the source later.
    """
    try:
        observed=datetime.fromisoformat(
            ingestion_time.replace("Z","+00:00")
        )
    except ValueError as exc:
        raise OperationalLegalAnalysisError(
            "feed-event ingestion_time must be ISO 8601"
        ) from exc
    if observed.tzinfo is None or observed.utcoffset() is None:
        raise OperationalLegalAnalysisError(
            "feed-event ingestion_time must be offset-aware"
        )
    event_day=observed.date()
    result=derive_operational_relevance(
        legal_analysis,
        temporal_assertions=temporal_assertions,
        window_start=event_day.isoformat(),
        window_end=(event_day+timedelta(days=1)).isoformat(),
    )
    return {
        **result,
        "novelty_basis":"OFFICIAL_FEED_EVENT_DAY",
        "event_day":event_day.isoformat(),
        "temporal_precision":"DAY",
    }


def apply_operational_recency_gate(legal_analysis: dict[str, Any], *, recency: dict[str, Any] | None) -> dict[str, Any]:
    """Gate CHANGE_FEED eligibility with a typed, separately evidenced relevance event."""
    if legal_analysis.get("disposition") != "LEGAL_CHANGE_VERIFIED": return legal_analysis
    analysis_identity=legal_analysis.get("analysis_identity")
    if not analysis_identity: raise OperationalLegalAnalysisError("verified legal analysis requires analysis_identity before recency gating")

    dimension=None; relevant_at=None; recency_evidence_refs=[]
    if recency is None:
        state="UNRESOLVED"; assertion_refs=[]
    else:
        state=recency.get("state"); assertion_refs=list(recency.get("assertion_refs",[]))
        recency_evidence_refs=list(recency.get("evidence_refs",[]))
        if recency.get("legal_analysis_identity") != analysis_identity:
            raise OperationalLegalAnalysisError("operational recency evidence must bind to the gated legal_analysis_identity")
        dimension=recency.get("relevance_dimension"); relevant_at=recency.get("relevant_at")

    if state == "CURRENT_RELEVANT":
        if not assertion_refs: raise OperationalLegalAnalysisError("CURRENT_RELEVANT recency requires canonical temporal/procedural assertion_refs")
        if dimension not in RELEVANCE_DIMENSIONS:
            raise OperationalLegalAnalysisError("CURRENT_RELEVANT recency requires an allowed relevance_dimension")
        if not relevant_at:
            raise OperationalLegalAnalysisError("CURRENT_RELEVANT recency requires an evidenced relevant_at value")
        result=dict(legal_analysis)
        result["evidence_refs"]=list(dict.fromkeys([
            *result.get("evidence_refs",[]),
            *assertion_refs,
            *recency_evidence_refs,
        ]))
        canonical_refs=list(result.get("canonical_refs",[]))
        for ref in assertion_refs:
            temporal_ref={"kind":"TEMPORAL_ASSERTION","entity_id":ref}
            if temporal_ref not in canonical_refs:
                canonical_refs.append(temporal_ref)
        result["canonical_refs"]=canonical_refs
        result["recency"]={
            "state":state,
            "assertion_refs":assertion_refs,
            "legal_analysis_identity":analysis_identity,
            "relevance_dimension":dimension,
            "relevant_at":relevant_at,
            **({
                "novelty_basis":recency["novelty_basis"],
                "event_day":recency.get("event_day"),
                "temporal_precision":recency.get("temporal_precision"),
            } if recency and recency.get("novelty_basis") else {}),
        }
        return result

    if state not in {"HISTORICAL_NOT_CURRENT","UNRESOLVED","CONTEXT_REQUIRED","CONFLICTING"}:
        raise OperationalLegalAnalysisError(f"unsupported operational recency state: {state}")
    if state == "HISTORICAL_NOT_CURRENT" and not assertion_refs:
        raise OperationalLegalAnalysisError("HISTORICAL_NOT_CURRENT recency requires canonical temporal/procedural assertion_refs")
    reason={
        "HISTORICAL_NOT_CURRENT":"The legal mutation is verified, but canonical temporal/procedural evidence establishes that it is historical rather than newly relevant to this feed window.",
        "UNRESOLVED":"The legal mutation is verified, but Needle lacks canonical temporal/procedural evidence that it is newly relevant to this feed window.",
        "CONTEXT_REQUIRED":"The legal mutation is verified, but operational recency depends on unresolved legal context.",
        "CONFLICTING":"The legal mutation is verified, but canonical temporal/procedural evidence conflicts on operational recency.",
    }[state]
    canonical_refs=list(legal_analysis.get("canonical_refs",[]))
    for ref in assertion_refs:
        temporal_ref={"kind":"TEMPORAL_ASSERTION","entity_id":ref}
        if temporal_ref not in canonical_refs:
            canonical_refs.append(temporal_ref)
    return {
        "disposition":"ABSTAIN_LEGAL_UNRESOLVED",
        "verification_route":legal_analysis.get("verification_route"),
        "canonical_refs":canonical_refs,
        "evidence_refs":list(dict.fromkeys([
            *legal_analysis.get("evidence_refs",[]),
            *assertion_refs,
            *recency_evidence_refs,
        ])),
        "explanation":None,
        "unknowns":[*legal_analysis.get("unknowns",[]),reason],
        "analysis_identity":analysis_identity,
        "recency":{
            "state":state,
            "assertion_refs":assertion_refs,
            "legal_analysis_identity":analysis_identity,
            **({
                "novelty_basis":recency["novelty_basis"],
                "event_day":recency.get("event_day"),
                "temporal_precision":recency.get("temporal_precision"),
            } if recency and recency.get("novelty_basis") else {}),
        },
    }


def analyze_operational_legal(event: dict[str, Any], source_change: dict[str, Any], *, candidates: Iterable[dict[str, Any]]) -> dict[str, Any]:
    if source_change.get("event_key") != event.get("event_key"): raise OperationalLegalAnalysisError("source change does not belong to event")
    collapsed=collapse_evidence_candidates(candidates)
    verified=[c for c in collapsed if c.get("outcome") == "LEGAL_CHANGE_VERIFIED"]
    non_impact=[c for c in collapsed if c.get("outcome") == "LEGAL_NON_IMPACT_VERIFIED"]
    if verified and non_impact:
        return {"disposition":"ABSTAIN_LEGAL_UNRESOLVED","verification_route":None,"canonical_refs":[],"evidence_refs":sorted({ref for c in collapsed for ref in c.get("evidence_refs",[])}),"explanation":None,"unknowns":["Canonical analyzers produced conflicting verified-change and verified-non-impact outcomes for the same operational event."]}
    if len(verified) > 1:
        return {"disposition":"ABSTAIN_LEGAL_UNRESOLVED","verification_route":None,"canonical_refs":[],"evidence_refs":sorted({ref for c in verified for ref in c.get("evidence_refs",[])}),"explanation":None,"unknowns":["More than one distinct verified legal mutation candidate remains after representation deduplication; automatic selection is forbidden."]}
    chosen=verified[0] if verified else (non_impact[0] if len(non_impact) == 1 else None)
    if chosen is None:
        return {"disposition":"ABSTAIN_LEGAL_UNRESOLVED","verification_route":None,"canonical_refs":[],"evidence_refs":sorted({ref for c in collapsed for ref in c.get("evidence_refs",[])}),"explanation":None,"unknowns":["No unique evidence-backed legal outcome was established by canonical analyzers."]}
    route=chosen.get("verification_route")
    if route not in {"AUTHENTIC_LEGAL_CAUSE","SOURCE_DIFF"}: raise OperationalLegalAnalysisError("verified legal outcome requires an allowed verification_route")
    result={"disposition":chosen["outcome"],"verification_route":route,"canonical_refs":list(chosen.get("canonical_refs",[])),"evidence_refs":list(dict.fromkeys(chosen.get("evidence_refs",[]))),"explanation":chosen.get("explanation"),"unknowns":list(chosen.get("unknowns",[]))}
    result["analysis_identity"]="operational-legal-analysis:"+_digest({"event_key":event["event_key"],"source_change_id":source_change.get("change_id"),"semantic_key":chosen["semantic_key"],"outcome":chosen["outcome"],"verification_route":route})
    return result
