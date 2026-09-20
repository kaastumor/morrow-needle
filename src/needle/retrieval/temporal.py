from __future__ import annotations

from pathlib import Path
from typing import Any

from needle.provenance.ledger import active_records
from needle.temporal.resolver import status_on_perspective
from needle.thread.composer import load_thread_sources


def _temporal_registry(
    thread: dict[str, Any],
    *,
    root: Path,
) -> tuple[dict[str, dict[str, Any]], set[str]]:
    sources = load_thread_sources(thread, root=root)

    assertions: dict[str, dict[str, Any]] = {}
    for source in sources.values():
        if source["kind"] != "TEMPORAL":
            continue
        for assertion_id, assertion in source["index"].items():
            if assertion_id in assertions:
                raise ValueError(
                    f"duplicate temporal assertion_id across Thread registry: "
                    f"{assertion_id}"
                )
            assertions[assertion_id] = assertion

    ledger = sources[thread["provenance_source_key"]]["data"]["records"]
    current = active_records(ledger, include_supersession_records=False)
    supported = {
        record["payload"]["claim_ref"]["entity_id"]
        for record in current
        if record.get("record_type") == "CLAIM_SUPPORT"
        and record["payload"]["claim_ref"]["entity_type"] == "TEMPORAL_ASSERTION"
    }
    return assertions, supported


def _abstention(
    state: str,
    *,
    reason: str,
    temporal: dict[str, Any],
    assertion_ids: list[str],
    extra: dict[str, Any] | None = None,
) -> dict[str, Any]:
    evaluation = {
        "state":state,
        "active":None,
        "dimension":temporal["dimension"],
        "valid_date":temporal["valid_date"],
        "perspective":temporal["perspective"],
        "source_cutoff_date":temporal.get("source_cutoff_date"),
        "supporting_assertion_ids":assertion_ids,
    }
    if extra:
        evaluation.update(extra)
    return {
        "decision":"ABSTAIN",
        "reason":reason,
        "evaluation":evaluation,
    }


def evaluate_entity_temporally(
    thread: dict[str, Any],
    entity: dict[str, Any],
    temporal: dict[str, Any],
    *,
    root: Path | str = Path("."),
) -> dict[str, Any]:
    """Evaluate an entity only through explicit canonical temporal references.

    Retrieval deliberately refuses to infer temporal scope from Thread event
    order, mutation dates, lineage, lexical dates or neighboring entities.
    """
    root = Path(root)
    assertion_ids = list(entity.get("temporal_assertion_refs", []))
    if not assertion_ids:
        return _abstention(
            "NO_TEMPORAL_ASSERTIONS",
            reason="NO_TEMPORAL_ASSERTIONS",
            temporal=temporal,
            assertion_ids=[],
        )

    registry, supported = _temporal_registry(thread, root=root)

    unknown = sorted(set(assertion_ids) - set(registry))
    if unknown:
        return _abstention(
            "UNKNOWN_TEMPORAL_REFERENCE",
            reason="UNKNOWN_TEMPORAL_REFERENCE",
            temporal=temporal,
            assertion_ids=assertion_ids,
            extra={"unknown_assertion_ids":unknown},
        )

    unsupported = sorted(set(assertion_ids) - supported)
    if unsupported:
        return _abstention(
            "TEMPORAL_PROVENANCE_GAP",
            reason="TEMPORAL_PROVENANCE_GAP",
            temporal=temporal,
            assertion_ids=assertion_ids,
            extra={"unsupported_assertion_ids":unsupported},
        )

    dimension = temporal["dimension"]
    relevant = [
        registry[assertion_id]
        for assertion_id in assertion_ids
        if registry[assertion_id]["dimension"] == dimension
    ]
    if not relevant:
        return _abstention(
            "TEMPORAL_NOT_ASSERTED",
            reason="TEMPORAL_NOT_ASSERTED",
            temporal=temporal,
            assertion_ids=assertion_ids,
        )

    # OFFICIAL_SOURCE_STATE_AS_OF needs publication assertions to establish
    # when supporting official sources were available. These are canonical
    # temporal facts in the Thread registry, not caller-supplied dates.
    publication = [
        assertion
        for assertion in registry.values()
        if assertion["dimension"] == "PUBLICATION"
        and assertion["assertion_id"] in supported
    ]
    resolver_assertions = relevant + (
        publication
        if temporal["perspective"] == "OFFICIAL_SOURCE_STATE_AS_OF"
        else []
    )

    subject_keys = {
        subject_key
        for assertion in relevant
        for subject_key in assertion["scope"]["applies_to"]
    }

    # Query context may supply entity/event facts required by conditional
    # temporal clauses. It may not inject official-source availability.
    context = {
        key:value
        for key, value in temporal.get("context", {}).items()
        if key != "source_available_from"
    }

    evaluation = status_on_perspective(
        resolver_assertions,
        dimension=dimension,
        subject_keys=subject_keys,
        valid_date=temporal["valid_date"],
        perspective=temporal["perspective"],
        source_cutoff_date=temporal.get("source_cutoff_date"),
        context=context,
    )
    evaluation = {
        **evaluation,
        "dimension":dimension,
        "supporting_assertion_ids":[
            assertion["assertion_id"] for assertion in relevant
        ],
        "source_availability_assertion_ids":[
            assertion["assertion_id"] for assertion in publication
        ],
    }

    state = evaluation["state"]
    reason_by_state = {
        "CONTEXT_REQUIRED":"TEMPORAL_CONTEXT_REQUIRED",
        "CONFLICTING":"TEMPORAL_CONFLICT",
        "SOURCE_AVAILABILITY_UNRESOLVED":"SOURCE_AVAILABILITY_UNRESOLVED",
        "NOT_ASSERTED_AS_OF_SOURCE_DATE":"NOT_ASSERTED_AS_OF_SOURCE_DATE",
        "SOURCE_CUTOFF_REQUIRED":"SOURCE_AVAILABILITY_UNRESOLVED",
        "NOT_ASSERTED":"TEMPORAL_NOT_ASSERTED",
    }
    if state in reason_by_state:
        return {
            "decision":"ABSTAIN",
            "reason":reason_by_state[state],
            "evaluation":evaluation,
        }

    if evaluation.get("active") is False and temporal["mode"] == "ACTIVE_ONLY":
        return {
            "decision":"ABSTAIN",
            "reason":"TEMPORAL_NOT_ACTIVE",
            "evaluation":evaluation,
        }

    return {
        "decision":"INCLUDE",
        "reason":None,
        "evaluation":evaluation,
    }
