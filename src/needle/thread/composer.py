from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from needle.provenance.ledger import active_records, validate_ledger


REF_SOURCE_KINDS = {
    "THREAD_EVIDENCE":{"BASELINE_EVIDENCE","CONTINUITY","RELATED_SOURCE"},
    "MUTATION":{"MUTATION"},
    "CHANGE_ATOM":{"SEMANTIC"},
    "TEMPORAL_ASSERTION":{"TEMPORAL"},
    "LINEAGE_EDGE":{"LINEAGE"},
    "PROVENANCE_CLAIM":{"PROVENANCE"},
}

PROVENANCE_ENTITY_TYPES = {
    "THREAD_EVIDENCE":"OTHER",
    "MUTATION":"MUTATION",
    "CHANGE_ATOM":"CHANGE_ATOM",
    "TEMPORAL_ASSERTION":"TEMPORAL_ASSERTION",
    "LINEAGE_EDGE":"OTHER",
}


def _read_json(root: Path, path: str) -> dict[str, Any]:
    return json.loads((root / path).read_text(encoding="utf-8"))


def _index_fixture(kind: str, data: dict[str, Any]) -> dict[str, Any]:
    if kind in {"BASELINE_EVIDENCE","CONTINUITY","RELATED_SOURCE"}:
        return {data["fixture_id"]:data}
    if kind == "MUTATION":
        return {data["mutation_id"]:data}
    if kind == "SEMANTIC":
        return {atom["atom_id"]:atom for atom in data.get("atoms", [])}
    if kind == "TEMPORAL":
        return {
            assertion["assertion_id"]:assertion
            for assertion in data.get("assertions", [])
        }
    if kind == "LINEAGE":
        return {edge["edge_id"]:edge for edge in data.get("edges", [])}
    if kind == "PROVENANCE":
        return {
            record["record_id"]:record
            for record in data.get("records", [])
        }
    raise ValueError(f"unsupported Thread source kind: {kind}")


def load_thread_sources(
    thread: dict[str, Any],
    *,
    root: Path | str = Path("."),
) -> dict[str, dict[str, Any]]:
    root = Path(root)
    result: dict[str, dict[str, Any]] = {}
    for source_key, source in thread["source_registry"].items():
        data = _read_json(root, source["fixture_path"])
        result[source_key] = {
            "kind":source["kind"],
            "fixture_path":source["fixture_path"],
            "data":data,
            "index":_index_fixture(source["kind"], data),
        }
    return result


def resolve_thread_references(
    thread: dict[str, Any],
    *,
    root: Path | str = Path("."),
) -> tuple[list[dict[str, Any]], list[str]]:
    sources = load_thread_sources(thread, root=root)
    resolved: list[dict[str, Any]] = []
    errors: list[str] = []
    event_ids: set[str] = set()

    for event in thread["events"]:
        event_id = event["event_id"]
        if event_id in event_ids:
            errors.append(f"duplicate Thread event_id: {event_id}")
        event_ids.add(event_id)

        resolved_refs = []
        for ref in event["refs"]:
            source_key = ref["source_key"]
            source = sources.get(source_key)
            if source is None:
                errors.append(
                    f"{event_id}: unknown Thread source_key: {source_key}"
                )
                continue

            allowed = REF_SOURCE_KINDS[ref["kind"]]
            if source["kind"] not in allowed:
                errors.append(
                    f"{event_id}: {ref['kind']} cannot resolve from "
                    f"{source['kind']} source {source_key}"
                )
                continue

            entity = source["index"].get(ref["entity_id"])
            if entity is None:
                errors.append(
                    f"{event_id}: unresolved {ref['kind']} "
                    f"{ref['entity_id']} in {source_key}"
                )
                continue

            resolved_refs.append({**ref, "entity":entity})

        resolved.append({
            "event_id":event_id,
            "event_kind":event["event_kind"],
            "refs":resolved_refs,
        })

    lineage_sources = [
        source for source in sources.values()
        if source["kind"] == "LINEAGE"
    ]
    lineage_index = {
        entity_id:entity
        for source in lineage_sources
        for entity_id, entity in source["index"].items()
    }
    for edge_id in thread["lineage_edge_ids"]:
        if edge_id not in lineage_index:
            errors.append(f"unresolved Thread lineage edge: {edge_id}")

    provenance_key = thread["provenance_source_key"]
    provenance = sources.get(provenance_key)
    if provenance is None:
        errors.append(
            f"unknown provenance_source_key: {provenance_key}"
        )
    elif provenance["kind"] != "PROVENANCE":
        errors.append(
            f"provenance_source_key must reference PROVENANCE, "
            f"got {provenance['kind']}"
        )
    else:
        ledger_errors = validate_ledger(provenance["data"]["records"])
        errors.extend(f"provenance ledger: {error}" for error in ledger_errors)

    return resolved, errors


def source_mode_gaps(
    thread: dict[str, Any],
    *,
    root: Path | str = Path("."),
) -> list[dict[str, str]]:
    sources = load_thread_sources(thread, root=root)
    provenance = sources[thread["provenance_source_key"]]["data"]["records"]
    current = active_records(
        provenance,
        include_supersession_records=False,
    )
    supported = {
        (
            record["payload"]["claim_ref"]["entity_type"],
            record["payload"]["claim_ref"]["entity_id"],
        )
        for record in current
        if record.get("record_type") == "CLAIM_SUPPORT"
    }

    gaps: list[dict[str, str]] = []
    for event in thread["events"]:
        for ref in event["refs"]:
            entity_type = PROVENANCE_ENTITY_TYPES.get(ref["kind"])
            if entity_type is None:
                continue
            key = (entity_type, ref["entity_id"])
            if key not in supported:
                gaps.append({
                    "event_id":event["event_id"],
                    "kind":ref["kind"],
                    "entity_id":ref["entity_id"],
                    "expected_provenance_entity_type":entity_type,
                })
    return gaps


def materialize_thread(
    thread: dict[str, Any],
    *,
    root: Path | str = Path("."),
) -> dict[str, Any]:
    events, errors = resolve_thread_references(thread, root=root)
    if errors:
        raise ValueError("Thread reference errors: " + "; ".join(errors))

    return {
        "schema_version":thread["schema_version"],
        "thread_id":thread["thread_id"],
        "subject":thread["subject"],
        "events":events,
        "lineage_edge_ids":thread["lineage_edge_ids"],
        "source_mode":{
            "required":thread["narrative_policy"]["source_mode"] == "REQUIRED",
            "gaps":source_mode_gaps(thread, root=root),
        },
        "unknowns":thread["unknowns"],
    }



def emit_thread_facts(
    thread: dict[str, Any],
    *,
    root: Path | str = Path("."),
) -> list[dict[str, Any]]:
    """Flatten a materialized Thread into Gold-testable partial facts.

    Facts retain canonical domain entities by reference/materialization; they do
    not become a second persistence model.
    """
    materialized = materialize_thread(thread, root=root)
    facts: list[dict[str, Any]] = []

    for event_index, event in enumerate(materialized["events"]):
        facts.append({
            "kind":"THREAD_EVENT",
            "event_index":event_index,
            "event_id":event["event_id"],
            "event_kind":event["event_kind"],
            "refs":[
                {
                    "kind":ref["kind"],
                    "entity_id":ref["entity_id"],
                }
                for ref in event["refs"]
            ],
        })
        for ref in event["refs"]:
            facts.append({
                "kind":"THREAD_REF",
                "event_index":event_index,
                "event_id":event["event_id"],
                "event_kind":event["event_kind"],
                "ref_kind":ref["kind"],
                "entity_id":ref["entity_id"],
                "source_key":ref["source_key"],
                "entity":ref["entity"],
            })

    gaps = materialized["source_mode"]["gaps"]
    facts.append({
        "kind":"THREAD_SOURCE_MODE",
        "closed":not gaps,
        "gap_count":len(gaps),
    })

    for unknown in materialized["unknowns"]:
        facts.append({
            "kind":"THREAD_UNKNOWN",
            **unknown,
        })

    return facts
