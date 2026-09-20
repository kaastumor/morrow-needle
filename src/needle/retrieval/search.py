from __future__ import annotations

from pathlib import Path
from typing import Any

from needle.retrieval.projection import (
    build_thread_projection,
    normalize_provision_path,
)
from needle.retrieval.temporal import evaluate_entity_temporally
from needle.thread.composer import load_thread_sources


_FILTER_FIELDS = {
    "entity_kinds":"entity_ref.kind",
    "act_ids":"act_ids",
    "languages":"languages",
    "event_ids":"event_ids",
    "event_kinds":"event_kinds",
    "legal_effects":"legal_effects",
    "dimensions":"dimensions",
    "mutation_operations":"mutation_operations",
    "temporal_dimensions":"temporal_dimensions",
    "lineage_scopes":"lineage_scopes",
    "lineage_edge_types":"lineage_edge_types",
    "verification_states":"verification_states",
    "evidence_states":"evidence_states",
}

_KIND_PRIORITY = {
    "CHANGE_ATOM":0,
    "MUTATION":1,
    "TEMPORAL_ASSERTION":2,
    "LINEAGE_EDGE":3,
    "THREAD_EVIDENCE":4,
    "THREAD":5,
}

_EXACT_FIELD_PRIORITY = {
    "ENTITY_ID":0,
    "THREAD_ID":1,
    "ACT_ID":2,
    "PROVISION_PATH":3,
    "CLAIM":4,
    "RULE_STATEMENT":5,
    "SOURCE_EXPRESSION":6,
}

_FUZZY_FIELD_PRIORITY = {
    "CLAIM":0,
    "RULE_STATEMENT":1,
    "SOURCE_EXPRESSION":2,
    "PROVISION_PATH":3,
    "SOURCE_IDENTIFIER":4,
    "QUALIFIER_TERM":5,
    "TRIGGER_TERM":6,
    "ENTITY_ID":20,
    "THREAD_ID":21,
    "ACT_ID":22,
}

_QUALITY_PRIORITY = {"EXACT":0, "PREFIX":1, "SUBSTRING":2}

_EVIDENCE_PRIORITY = {
    "DIRECT":0,
    "DERIVED":1,
    "CONTEXTUAL":2,
    "ATTRIBUTED":3,
    "INTERPRETIVE":4,
    "UNRESOLVED":5,
}

_VERIFICATION_PRIORITY = {
    "VERIFIED":0,
    "ASSERTED":1,
    "EVIDENCED":2,
    "CORROBORATED":2,
    "RESOLVED_ABSOLUTE":2,
    "RESOLVED_RELATIVE":2,
    "CONTEXT_REQUIRED":4,
    "CANDIDATE":5,
    "QUARANTINED":6,
    "REJECTED":7,
    "UNRESOLVED":8,
}


def _field_priority(field: str, quality: str) -> int:
    if quality == "EXACT":
        return _EXACT_FIELD_PRIORITY.get(field, 50)
    return _FUZZY_FIELD_PRIORITY.get(field, 50)


def _document_values(document: dict[str, Any], field: str) -> list[str]:
    if field == "entity_ref.kind":
        return [document["entity_ref"]["kind"]]
    value = document.get(field, [])
    if isinstance(value, list):
        return [str(item) for item in value]
    return [str(value)]


def _structured_reasons(
    document: dict[str, Any],
    filters: dict[str, Any],
) -> list[dict[str, Any]] | None:
    reasons: list[dict[str, Any]] = []

    for query_field, doc_field in _FILTER_FIELDS.items():
        wanted = filters.get(query_field, [])
        if not wanted:
            continue
        actual = _document_values(document, doc_field)
        matched = [value for value in wanted if value in actual]
        if not matched:
            return None
        for value in matched:
            reasons.append({
                "kind":"STRUCTURED_FILTER",
                "field":query_field,
                "query_value":value,
                "matched_values":[value],
                "match_quality":None,
            })

    wanted_paths = filters.get("provision_path_prefixes", [])
    if wanted_paths:
        actual = document["provision_paths"]
        matched_pairs = []
        for raw in wanted_paths:
            wanted = normalize_provision_path(raw)
            hits = [
                path for path in actual
                if path == wanted or path.startswith(wanted + " >")
            ]
            if hits:
                matched_pairs.append((raw, hits))
        if not matched_pairs:
            return None
        for raw, hits in matched_pairs:
            reasons.append({
                "kind":"STRUCTURED_FILTER",
                "field":"provision_path_prefixes",
                "query_value":raw,
                "matched_values":hits,
                "match_quality":None,
            })

    if "source_mode_closed" in filters:
        wanted = filters["source_mode_closed"]
        actual = document["source_mode"]["closed"]
        if actual is not wanted:
            return None
        reasons.append({
            "kind":"STRUCTURED_FILTER",
            "field":"source_mode_closed",
            "query_value":wanted,
            "matched_values":[actual],
            "match_quality":None,
        })

    return reasons


def _text_match(
    lexical: list[dict[str, str]],
    term: str,
) -> dict[str, Any] | None:
    wanted = term.casefold().strip()
    hits: list[tuple[int, int, str, str, str]] = []
    for item in lexical:
        candidate = item["value"].casefold()
        if wanted not in candidate:
            continue
        if candidate == wanted:
            quality = "EXACT"
        elif candidate.startswith(wanted):
            quality = "PREFIX"
        else:
            quality = "SUBSTRING"
        hits.append((
            _QUALITY_PRIORITY[quality],
            _field_priority(item["field"], quality),
            item["field"],
            item["value"],
            quality,
        ))
    if not hits:
        return None

    hits.sort()
    best_quality = hits[0][4]
    best_field_priority = hits[0][1]
    best_hits = [
        hit for hit in hits
        if hit[4] == best_quality and hit[1] == best_field_priority
    ]
    best_fields = sorted({hit[2] for hit in best_hits})
    best_values = sorted({hit[3] for hit in best_hits})
    return {
        "kind":"LEXICAL_MATCH",
        "field":"|".join(best_fields),
        "query_value":term,
        "matched_values":best_values,
        "match_quality":best_quality,
    }


def _text_reasons(
    document: dict[str, Any],
    text_terms: list[str],
    text_mode: str,
) -> list[dict[str, Any]] | None:
    if not text_terms:
        return []
    matches = [
        _text_match(document["lexical"], term)
        for term in text_terms
    ]
    if text_mode == "ALL" and any(match is None for match in matches):
        return None
    if text_mode == "ANY" and all(match is None for match in matches):
        return None
    return [match for match in matches if match is not None]


def _hydrate(
    *,
    thread: dict[str, Any],
    sources: dict[str, dict[str, Any]],
    document: dict[str, Any],
) -> dict[str, Any]:
    ref = document["entity_ref"]
    if ref["kind"] == "THREAD":
        return thread
    source_key = document["source_key"]
    return sources[source_key]["index"][ref["entity_id"]]


def _canonical_evidence_state(entity: dict[str, Any]) -> str | None:
    return entity.get("evidence_state")


def _canonical_verification_state(entity: dict[str, Any]) -> str | None:
    return (
        entity.get("verification_state")
        or entity.get("claim_status")
        or entity.get("resolution_state")
        or entity.get("result", {}).get("verification_state")
        or entity.get("result", {}).get("reconciliation_state")
    )


def _ordering_key(result: dict[str, Any]) -> tuple[Any, ...]:
    lexical = [
        reason for reason in result["match_reasons"]
        if reason["kind"] == "LEXICAL_MATCH"
    ]
    best_quality = min(
        (_QUALITY_PRIORITY[reason["match_quality"]] for reason in lexical),
        default=9,
    )
    best_field = min(
        (
            min(
                _field_priority(field, reason["match_quality"])
                for field in reason["field"].split("|")
            )
            for reason in lexical
        ),
        default=50,
    )
    structured_count = sum(
        reason["kind"] == "STRUCTURED_FILTER"
        for reason in result["match_reasons"]
    )
    entity = result["canonical_entity"]
    evidence_state = _canonical_evidence_state(entity)
    verification_state = _canonical_verification_state(entity)
    return (
        best_quality,
        best_field,
        -structured_count,
        _EVIDENCE_PRIORITY.get(evidence_state, 9),
        _VERIFICATION_PRIORITY.get(verification_state, 9),
        _KIND_PRIORITY[result["entity_ref"]["kind"]],
        result["entity_ref"]["entity_id"],
    )


def search_thread(
    thread: dict[str, Any],
    query: dict[str, Any],
    *,
    root: Path | str = Path("."),
) -> dict[str, Any]:
    """Search one Thread projection without creating a second legal truth store.

    List filters are OR within one field and AND across fields.
    Lexical matching is deterministic case-insensitive substring matching.
    """
    root = Path(root)
    projection = build_thread_projection(thread, root=root)
    sources = load_thread_sources(thread, root=root)

    filters = query.get("filters", {})
    text_terms = query.get("text_terms", [])
    text_mode = query.get("text_mode", "ALL")

    results = []
    abstentions = []
    temporal = query.get("temporal")

    for document in projection["documents"]:
        structured = _structured_reasons(document, filters)
        if structured is None:
            continue
        lexical = _text_reasons(document, text_terms, text_mode)
        if lexical is None:
            continue

        entity = _hydrate(
            thread=thread,
            sources=sources,
            document=document,
        )
        match_reasons = structured + lexical
        temporal_evaluation = None

        if temporal is not None:
            temporal_result = evaluate_entity_temporally(
                thread,
                entity,
                temporal,
                root=root,
            )
            temporal_evaluation = temporal_result["evaluation"]
            if temporal_result["decision"] == "ABSTAIN":
                abstentions.append({
                    "entity_ref":document["entity_ref"],
                    "reason":temporal_result["reason"],
                    "temporal_evaluation":temporal_evaluation,
                })
                continue

            match_reasons = match_reasons + [{
                "kind":"TEMPORAL_EVALUATION",
                "field":f"temporal.{temporal['dimension']}",
                "query_value":temporal["valid_date"],
                "matched_values":temporal_evaluation["supporting_assertion_ids"],
                "match_quality":None,
            }]

        result = {
            "entity_ref":document["entity_ref"],
            "thread_id":document["thread_id"],
            "event_ids":document["event_ids"],
            "match_reasons":match_reasons,
            "source_mode":document["source_mode"],
            "canonical_entity":entity,
        }
        if temporal is not None:
            result["temporal_evaluation"] = temporal_evaluation
        results.append(result)

    results.sort(key=_ordering_key)
    abstentions.sort(
        key=lambda item:(
            _KIND_PRIORITY[item["entity_ref"]["kind"]],
            item["entity_ref"]["entity_id"],
        )
    )
    return {
        "schema_version":"retrieval-response-v0.1",
        "query_id":query["query_id"],
        "projection_fingerprint":projection["projection_fingerprint"],
        "results":results,
        "abstentions":abstentions,
    }
