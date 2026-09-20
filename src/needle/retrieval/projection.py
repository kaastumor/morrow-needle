from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

from needle.provenance.ledger import active_records
from needle.thread.composer import (
    PROVENANCE_ENTITY_TYPES,
    load_thread_sources,
    materialize_thread,
)


PROJECTION_VERSION = "retrieval-projection-v0.1"


def _unique(values: list[str]) -> list[str]:
    return sorted({value for value in values if value})


def normalize_provision_path(value: str) -> str:
    """Normalize common Article/paragraph spellings for retrieval only.

    This is a search adapter, not canonical provision identity.
    """
    text = " ".join(value.strip().split())
    m = re.fullmatch(
        r"(?i)article\s+([^\s(>]+)(?:\s*>\s*([^\s]+)|\(([^)]+)\))?",
        text,
    )
    if m:
        article = m.group(1)
        paragraph = m.group(2) or m.group(3)
        base = f"article {article}".casefold()
        return f"{base} > {paragraph.casefold()}" if paragraph else base

    m = re.fullmatch(
        r"(?i)article\s+([^,]+),\s*paragraph\s+([^\s]+)",
        text,
    )
    if m:
        return f"article {m.group(1).strip().casefold()} > {m.group(2).casefold()}"

    return text.casefold()


def _add_lexical(
    target: list[dict[str, str]],
    field: str,
    value: Any,
) -> None:
    if value is None:
        return
    if isinstance(value, (list, tuple, set)):
        for item in value:
            _add_lexical(target, field, item)
        return
    if not isinstance(value, (str, int, float, bool)):
        return
    text = str(value).strip()
    if not text:
        return
    item = {"field":field, "value":text}
    if item not in target:
        target.append(item)


def _support_index(
    thread: dict[str, Any],
    *,
    root: Path,
) -> dict[tuple[str, str], list[str]]:
    sources = load_thread_sources(thread, root=root)
    records = active_records(
        sources[thread["provenance_source_key"]]["data"]["records"],
        include_supersession_records=False,
    )
    result: dict[tuple[str, str], list[str]] = {}
    for record in records:
        if record.get("record_type") != "CLAIM_SUPPORT":
            continue
        claim = record["payload"]["claim_ref"]
        key = (claim["entity_type"], claim["entity_id"])
        result.setdefault(key, []).append(record["record_id"])
    return result


def _empty_document(
    *,
    thread: dict[str, Any],
    source_key: str,
    kind: str,
    entity_id: str,
    support_record_ids: list[str],
) -> dict[str, Any]:
    subject = thread["subject"]
    lexical: list[dict[str, str]] = []
    _add_lexical(lexical, "ENTITY_ID", entity_id)
    _add_lexical(lexical, "THREAD_ID", thread["thread_id"])
    _add_lexical(lexical, "ACT_ID", subject["act_id"])
    _add_lexical(lexical, "PROVISION_PATH", subject["structural_path"])
    return {
        "projection_version":PROJECTION_VERSION,
        "entity_ref":{"kind":kind, "entity_id":entity_id},
        "source_key":source_key,
        "thread_id":thread["thread_id"],
        "event_ids":[],
        "event_kinds":[],
        "act_ids":[subject["act_id"]],
        "provision_paths":[normalize_provision_path(subject["structural_path"])],
        "languages":[subject["language"]],
        "legal_effects":[],
        "dimensions":[],
        "mutation_operations":[],
        "temporal_dimensions":[],
        "lineage_scopes":[],
        "lineage_edge_types":[],
        "verification_states":[],
        "evidence_states":[],
        "lexical":lexical,
        "source_mode":{
            "support_required":True,
            "closed":bool(support_record_ids),
            "support_count":len(support_record_ids),
            "support_record_ids":sorted(support_record_ids),
        },
    }


def _project_change_atom(doc: dict[str, Any], entity: dict[str, Any]) -> None:
    doc["act_ids"] = _unique(doc["act_ids"] + [entity["act_id"]])
    doc["provision_paths"] = _unique(
        doc["provision_paths"]
        + [
            normalize_provision_path(ref["citation_path"])
            for ref in entity.get("provision_refs", [])
        ]
    )
    doc["languages"] = _unique(
        doc["languages"] + entity.get("language_scope", {}).get("languages", [])
    )
    claim = entity["claim"]
    doc["legal_effects"] = [claim["legal_effect"]]
    doc["dimensions"] = _unique(claim.get("dimensions", []))
    doc["verification_states"] = [entity["verification_state"]]
    doc["evidence_states"] = [entity["evidence_state"]]

    for field in ("statement", "subject", "action", "object"):
        _add_lexical(doc["lexical"], "CLAIM", claim.get(field))
    semantic = entity.get("semantic_basis", {})
    _add_lexical(doc["lexical"], "TRIGGER_TERM", semantic.get("trigger_terms", []))
    _add_lexical(
        doc["lexical"], "QUALIFIER_TERM", semantic.get("qualifier_terms", [])
    )
    for relation in entity.get("relations", []):
        _add_lexical(doc["lexical"], "RELATED_ENTITY_ID", relation["target_atom_id"])


def _project_mutation(doc: dict[str, Any], entity: dict[str, Any]) -> None:
    language = entity.get("language")
    if language:
        doc["languages"] = _unique(doc["languages"] + [language])

    target = entity.get("target")
    instruction = entity.get("authentic_amending_act", {}).get("instruction", {})
    if not target:
        target = instruction.get("target_locator")
    if target:
        doc["provision_paths"] = _unique(
            doc["provision_paths"] + [normalize_provision_path(target)]
        )
        _add_lexical(doc["lexical"], "PROVISION_PATH", target)

    operation = entity.get("result", {}).get("operation") or instruction.get("operation")
    if operation:
        doc["mutation_operations"] = [operation]
        _add_lexical(doc["lexical"], "MUTATION_OPERATION", operation)

    verification = entity.get("result", {}).get("verification_state")
    if verification:
        doc["verification_states"] = [verification]

    for container in (
        entity.get("authentic_amending_act", {}),
        entity.get("authentic_cause", {}),
        entity.get("before_checkpoint", {}),
        entity.get("after_checkpoint", {}),
        entity.get("before", {}),
        entity.get("after", {}),
    ):
        _add_lexical(doc["lexical"], "SOURCE_IDENTIFIER", container.get("celex"))
    _add_lexical(doc["lexical"], "CASE_ID", entity.get("case_id"))


def _project_temporal(doc: dict[str, Any], entity: dict[str, Any]) -> None:
    doc["temporal_dimensions"] = [entity["dimension"]]
    doc["evidence_states"] = [entity["evidence_state"]]
    doc["verification_states"] = [entity["resolution_state"]]

    subject = entity.get("subject_ref", {})
    _add_lexical(doc["lexical"], "SUBJECT_IDENTIFIER", subject.get("identifier"))
    locator = subject.get("locator")
    if locator:
        doc["provision_paths"] = _unique(
            doc["provision_paths"] + [normalize_provision_path(locator)]
        )
        _add_lexical(doc["lexical"], "PROVISION_PATH", locator)

    trigger = entity.get("trigger", {})
    _add_lexical(doc["lexical"], "SOURCE_EXPRESSION", trigger.get("source_expression"))
    _add_lexical(doc["lexical"], "DATE", entity.get("normalized_date"))
    _add_lexical(doc["lexical"], "NOTES", entity.get("notes"))
    for source in entity.get("source_refs", []):
        _add_lexical(doc["lexical"], "SOURCE_IDENTIFIER", source.get("identifier"))


def _project_lineage(doc: dict[str, Any], entity: dict[str, Any]) -> None:
    doc["lineage_scopes"] = [entity["assertion_scope"]]
    doc["lineage_edge_types"] = [entity["edge_type"]]
    doc["evidence_states"] = [entity["evidence_state"]]
    doc["verification_states"] = [entity["claim_status"]]
    _add_lexical(doc["lexical"], "LINEAGE_EDGE_TYPE", entity["edge_type"])
    _add_lexical(doc["lexical"], "NOTES", entity.get("notes"))

    for ref in entity.get("sources", []) + entity.get("targets", []):
        doc["act_ids"] = _unique(doc["act_ids"] + [ref.get("act_id", "")])
        doc["provision_paths"] = _unique(
            doc["provision_paths"]
            + [normalize_provision_path(ref["structural_path"])]
        )
        if ref.get("language"):
            doc["languages"] = _unique(doc["languages"] + [ref["language"]])
        _add_lexical(doc["lexical"], "PROVISION_PATH", ref["structural_path"])

    anchor = entity.get("rule_anchor") or {}
    _add_lexical(doc["lexical"], "RULE_ID", anchor.get("rule_id"))
    _add_lexical(doc["lexical"], "RULE_STATEMENT", anchor.get("statement"))
    confidence = entity.get("confidence", {})
    _add_lexical(doc["lexical"], "EVIDENCE_RATIONALE", confidence.get("rationale"))


def _project_thread_evidence(doc: dict[str, Any], entity: dict[str, Any]) -> None:
    _add_lexical(doc["lexical"], "PURPOSE", entity.get("purpose"))

    subject = entity.get("subject", {})
    if subject:
        _add_lexical(doc["lexical"], "ACT_ID", subject.get("act_id"))
        path = subject.get("structural_path")
        if path:
            doc["provision_paths"] = _unique(
                doc["provision_paths"] + [normalize_provision_path(path)]
            )
            _add_lexical(doc["lexical"], "PROVISION_PATH", path)
        if subject.get("language"):
            doc["languages"] = _unique(doc["languages"] + [subject["language"]])

    paragraph4 = entity.get("paragraph4", {})
    if paragraph4.get("structural_path"):
        path = paragraph4["structural_path"]
        doc["provision_paths"] = _unique(
            doc["provision_paths"] + [normalize_provision_path(path)]
        )
        _add_lexical(doc["lexical"], "PROVISION_PATH", path)

    correction_target = entity.get("correction_target", {})
    _add_lexical(
        doc["lexical"], "PROVISION_PATH", correction_target.get("base_act_path")
    )
    semantic = entity.get("semantic_result", {})
    _add_lexical(doc["lexical"], "EXPLANATION", semantic.get("explanation"))
    scope = entity.get("thread_scope_result", {})
    _add_lexical(doc["lexical"], "CLASSIFICATION", scope.get("classification"))
    _add_lexical(doc["lexical"], "RATIONALE", scope.get("rationale"))
    _add_lexical(doc["lexical"], "FORBIDDEN_INFERENCE", entity.get("forbidden_inferences", []))


def _project_entity(
    *,
    thread: dict[str, Any],
    source_key: str,
    kind: str,
    entity_id: str,
    entity: dict[str, Any],
    support_record_ids: list[str],
) -> dict[str, Any]:
    doc = _empty_document(
        thread=thread,
        source_key=source_key,
        kind=kind,
        entity_id=entity_id,
        support_record_ids=support_record_ids,
    )
    if kind == "CHANGE_ATOM":
        _project_change_atom(doc, entity)
    elif kind == "MUTATION":
        _project_mutation(doc, entity)
    elif kind == "TEMPORAL_ASSERTION":
        _project_temporal(doc, entity)
    elif kind == "LINEAGE_EDGE":
        _project_lineage(doc, entity)
    elif kind == "THREAD_EVIDENCE":
        _project_thread_evidence(doc, entity)
    else:
        raise ValueError(f"unsupported retrieval entity kind: {kind}")
    return doc


def build_thread_projection(
    thread: dict[str, Any],
    *,
    root: Path | str = Path("."),
) -> dict[str, Any]:
    root = Path(root)
    materialized = materialize_thread(thread, root=root)
    if materialized["source_mode"]["gaps"]:
        raise ValueError("retrieval projection requires closed Thread Source Mode")

    sources = load_thread_sources(thread, root=root)
    support = _support_index(thread, root=root)
    documents: dict[tuple[str, str], dict[str, Any]] = {}

    source_kind_to_entity_kind = {
        "BASELINE_EVIDENCE":"THREAD_EVIDENCE",
        "CONTINUITY":"THREAD_EVIDENCE",
        "RELATED_SOURCE":"THREAD_EVIDENCE",
        "MUTATION":"MUTATION",
        "SEMANTIC":"CHANGE_ATOM",
        "TEMPORAL":"TEMPORAL_ASSERTION",
        "LINEAGE":"LINEAGE_EDGE",
    }

    # Index the complete canonical entity set deliberately registered by the
    # Thread. Event membership is attached separately below; helper assertions
    # remain searchable without being manufactured into timeline events.
    for source_key, source in sources.items():
        entity_kind = source_kind_to_entity_kind.get(source["kind"])
        if entity_kind is None:
            continue
        for entity_id, entity in source["index"].items():
            entity_type = PROVENANCE_ENTITY_TYPES.get(entity_kind)
            support_count = (
                len(support.get((entity_type, entity_id), []))
                if entity_type
                else 0
            )
            documents[(entity_kind, entity_id)] = _project_entity(
                thread=thread,
                source_key=source_key,
                kind=entity_kind,
                entity_id=entity_id,
                entity=entity,
                support_count=support_count,
            )

    for event in materialized["events"]:
        for ref in event["refs"]:
            key = (ref["kind"], ref["entity_id"])
            if key not in documents:
                raise ValueError(
                    f"Thread event references unprojected canonical entity: {key}"
                )
            doc = documents[key]
            doc["event_ids"] = _unique(doc["event_ids"] + [event["event_id"]])
            doc["event_kinds"] = _unique(doc["event_kinds"] + [event["event_kind"]])

    subject = thread["subject"]

    for unknown in thread.get("unknowns", []):
        unknown_id = unknown["unknown_id"]
        lexical: list[dict[str, str]] = []
        _add_lexical(lexical, "ENTITY_ID", unknown_id)
        _add_lexical(lexical, "THREAD_ID", thread["thread_id"])
        _add_lexical(lexical, "ACT_ID", subject["act_id"])
        _add_lexical(lexical, "PROVISION_PATH", subject["structural_path"])
        _add_lexical(lexical, "UNKNOWN_STATE", unknown.get("state"))
        _add_lexical(lexical, "DESCRIPTION", unknown.get("description"))
        documents[("THREAD_UNKNOWN", unknown_id)] = {
            "projection_version":PROJECTION_VERSION,
            "entity_ref":{"kind":"THREAD_UNKNOWN", "entity_id":unknown_id},
            "source_key":None,
            "thread_id":thread["thread_id"],
            "event_ids":[],
            "event_kinds":[],
            "act_ids":[subject["act_id"]],
            "provision_paths":[normalize_provision_path(subject["structural_path"])],
            "languages":[subject["language"]],
            "legal_effects":[],
            "dimensions":[],
            "mutation_operations":[],
            "temporal_dimensions":[],
            "lineage_scopes":[],
            "lineage_edge_types":[],
            "verification_states":[],
            "evidence_states":[],
            "lexical":lexical,
            "source_mode":{
                "support_required":False,
                "closed":True,
                "support_count":0,
                "support_record_ids":[],
            },
        }

    thread_lexical: list[dict[str, str]] = []
    _add_lexical(thread_lexical, "ENTITY_ID", thread["thread_id"])
    _add_lexical(thread_lexical, "THREAD_ID", thread["thread_id"])
    _add_lexical(thread_lexical, "ACT_ID", subject["act_id"])
    _add_lexical(thread_lexical, "PROVISION_PATH", subject["structural_path"])
    for child in documents.values():
        for item in child["lexical"]:
            _add_lexical(thread_lexical, f"CHILD_{item['field']}", item["value"])

    thread_doc = {
        "projection_version":PROJECTION_VERSION,
        "entity_ref":{"kind":"THREAD", "entity_id":thread["thread_id"]},
        "source_key":None,
        "thread_id":thread["thread_id"],
        "event_ids":[event["event_id"] for event in thread["events"]],
        "event_kinds":_unique([event["event_kind"] for event in thread["events"]]),
        "act_ids":[subject["act_id"]],
        "provision_paths":[normalize_provision_path(subject["structural_path"])],
        "languages":[subject["language"]],
        "legal_effects":[],
        "dimensions":[],
        "mutation_operations":[],
        "temporal_dimensions":[],
        "lineage_scopes":[],
        "lineage_edge_types":[],
        "verification_states":[],
        "evidence_states":[],
        "lexical":thread_lexical,
        "source_mode":{
            "support_required":True,
            "closed":True,
            "support_count":sum(
                doc["source_mode"]["support_count"] for doc in documents.values()
            ),
            "support_record_ids":sorted({
                record_id
                for doc in documents.values()
                for record_id in doc["source_mode"]["support_record_ids"]
            }),
        },
    }

    ordered = [thread_doc] + sorted(
        documents.values(),
        key=lambda doc: (
            doc["entity_ref"]["kind"],
            doc["entity_ref"]["entity_id"],
        ),
    )
    digest = hashlib.sha256(
        json.dumps(
            ordered,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        ).encode("utf-8")
    ).hexdigest()

    return {
        "projection_version":PROJECTION_VERSION,
        "thread_id":thread["thread_id"],
        "source_mode_closed":True,
        "projection_fingerprint":f"sha256:{digest}",
        "documents":ordered,
    }
