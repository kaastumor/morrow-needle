from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
from typing import Any


EDGE_TO_OPERATION = {
    "RENUMBERED_TO":"RENUMBER",
    "MOVED_TO":"MOVE",
    "SPLIT_INTO":"SPLIT",
    "MERGED_INTO":"MERGE",
}


def _asserted_lineage(edge: dict[str, Any]) -> bool:
    confidence = edge.get("confidence", {})
    return (
        edge.get("claim_status") == "ASSERTED"
        and edge.get("assertion_scope") == "STRUCTURAL_LINEAGE"
        and edge.get("evidence_state") != "UNRESOLVED"
        and confidence.get("conflict_state") == "NO_KNOWN_CONFLICT"
    )


def _structural_path(ref: dict[str, Any]) -> str:
    return ref["structural_path"]


def _by_operation_and_path(
    candidates: list[dict[str, Any]],
) -> dict[tuple[str, str], dict[str, Any]]:
    return {
        (candidate["operation"], candidate["target"]["citation_path"]):candidate
        for candidate in candidates
        if candidate["operation"] in {"INSERT","DELETE"}
    }


def reclassify_with_lineage(
    candidates: list[dict[str, Any]],
    lineage_edges: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Replace matching INSERT/DELETE pairs with lineage-backed structure ops.

    Candidate or unresolved lineage never promotes structure. Those original
    INSERT/DELETE candidates remain intact.
    """
    lookup = _by_operation_and_path(candidates)
    consumed: set[str] = set()
    generated: list[dict[str, Any]] = []

    for edge in lineage_edges:
        operation = EDGE_TO_OPERATION.get(edge.get("edge_type"))
        if not operation or not _asserted_lineage(edge):
            continue

        source_paths = [_structural_path(ref) for ref in edge.get("sources", [])]
        target_paths = [_structural_path(ref) for ref in edge.get("targets", [])]

        deletes = [lookup.get(("DELETE", path)) for path in source_paths]
        inserts = [lookup.get(("INSERT", path)) for path in target_paths]
        if any(item is None for item in deletes + inserts):
            continue

        if operation in {"MOVE","RENUMBER"} and not (
            len(deletes) == 1 and len(inserts) == 1
        ):
            continue
        if operation == "SPLIT" and not (
            len(deletes) == 1 and len(inserts) >= 2
        ):
            continue
        if operation == "MERGE" and not (
            len(deletes) >= 2 and len(inserts) == 1
        ):
            continue

        consumed_ids=[c["candidate_id"] for c in deletes+inserts]
        consumed.update(consumed_ids)
        before = deletes[0]["before"] if len(deletes) == 1 else None
        after = inserts[0]["after"] if len(inserts) == 1 else None

        target_path = (
            target_paths[0]
            if len(target_paths) == 1
            else " | ".join(target_paths)
        )
        source_path = (
            source_paths[0]
            if len(source_paths) == 1
            else " | ".join(source_paths)
        )
        candidate_id=sha256(
            f"{edge['edge_id']}|{operation}|{source_path}|{target_path}".encode()
        ).hexdigest()[:24]

        evidence=[{
            "channel":"DETERMINISTIC_DIFF",
            "source_id":"lineage-reclassification",
            "operation":operation,
            "target_locator":target_path,
            "authority_character":"DERIVED",
            "locator":f"consumed {len(consumed_ids)} insert/delete candidates",
        }]
        evidence.extend({
            "channel":"RELATIONSHIP_METADATA"
                if "OFFICIAL_RELATION_METADATA" in edge.get("evidence_basis", [])
                else "AUTHENTIC_ACT"
                if "OFFICIAL_AMENDMENT_INSTRUCTION" in edge.get("evidence_basis", [])
                else "CONSOLIDATED_CHECKPOINT",
            "source_id":ref["identifier"],
            "operation":operation,
            "target_locator":target_path,
            "authority_character":"OFFICIAL_STRUCTURED_METADATA"
                if "OFFICIAL_CORRELATION_TABLE" in edge.get("evidence_basis", [])
                else "DERIVED",
            "locator":ref.get("locator"),
        } for ref in edge.get("source_refs", []))

        template=deepcopy(inserts[0] if inserts else deletes[0])
        template.update({
            "candidate_id":candidate_id,
            "operation":operation,
            "target":{
                **template["target"],
                "citation_path":target_path,
                "parent_citation_path":None,
            },
            "alignment_basis":"ASSERTED_STRUCTURAL_LINEAGE",
            "before":before,
            "after":after,
            "feature_deltas":{
                "numbers_added":[],"numbers_removed":[],
                "dates_added":[],"dates_removed":[],
                "references_added":[],"references_removed":[],
            },
            "reconciliation_state":"CORROBORATED",
            "verification_state":"UNVERIFIED",
            "supporting_evidence":evidence,
            "conflicting_evidence":[],
            "lineage_edge_ids":[edge["edge_id"]],
            "consumed_candidate_ids":consumed_ids,
            "notes":(
                f"Structural {operation} candidate requires asserted lineage; "
                "semantic rule continuity remains a separate claim."
            ),
        })
        generated.append(template)

    remaining=[
        candidate for candidate in candidates
        if candidate["candidate_id"] not in consumed
    ]
    return remaining + generated
