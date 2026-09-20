from __future__ import annotations

from dataclasses import dataclass
from typing import Any


CHANGE_STATES = {
    "SOURCE_CREATED",
    "CONTENT_CHANGED",
    "METADATA_ONLY",
    "AVAILABILITY_CHANGED",
    "NO_MATERIAL_CHANGE",
    "UNRESOLVED",
}


def classify_source_change(
    *,
    action: str,
    previous: dict[str, Any] | None,
    current: dict[str, Any] | None,
) -> str:
    """Classify verified source change after targeted re-observation.

    Feed action is only a hint. Hash/availability state decides the material
    source-observation classification.
    """
    action = action.upper()

    if action == "DELETE":
        return "AVAILABILITY_CHANGED"

    if action == "CREATE":
        if current is None:
            return "UNRESOLVED"
        if current.get("available") is False:
            return "UNRESOLVED"
        if previous is None:
            return "SOURCE_CREATED"
        # Replayed/backfilled CREATE against an existing baseline falls through
        # to hash comparison rather than being blindly emitted as new.

    if previous is None or current is None:
        return "UNRESOLVED"

    prev_available = previous.get("available")
    curr_available = current.get("available")
    if prev_available is None or curr_available is None:
        return "UNRESOLVED"
    if prev_available != curr_available:
        return "AVAILABILITY_CHANGED"

    prev_content = previous.get("content_hash")
    curr_content = current.get("content_hash")
    prev_metadata = previous.get("metadata_hash")
    curr_metadata = current.get("metadata_hash")

    if prev_content is None or curr_content is None:
        return "UNRESOLVED"
    if prev_content != curr_content:
        return "CONTENT_CHANGED"

    if prev_metadata is None or curr_metadata is None:
        return "UNRESOLVED"
    if prev_metadata != curr_metadata:
        return "METADATA_ONLY"

    return "NO_MATERIAL_CHANGE"


def refresh_scope(event: dict[str, Any]) -> dict[str, Any]:
    """Conservatively describe what branch should be re-observed."""
    levels = set(event.get("wemi_levels", []))
    cellar_id = event["cellar_id"]
    root = event["root_cellar_id"]

    if "ITEM" in levels:
        scope = "ITEM_AND_PARENT_MANIFESTATION"
    elif "MANIFESTATION" in levels:
        scope = "MANIFESTATION"
    elif "EXPRESSION" in levels:
        scope = "EXPRESSION"
    elif "WORK" in levels:
        scope = "WORK"
    else:
        scope = "TARGET_AND_ROOT"

    return {
        "scope":scope,
        "target_cellar_id":cellar_id,
        "root_cellar_id":root,
    }



def snapshot_from_observations(
    *,
    content_observation: dict[str, Any] | None,
    metadata_observation: dict[str, Any] | None,
    available: bool,
) -> dict[str, Any]:
    """Project immutable provenance observations into a comparison snapshot.

    Content and metadata remain distinct SOURCE_OBSERVATION records. This
    projection deliberately does not mutate or merge their provenance.
    """
    return {
        "available":available,
        "content_hash":(
            content_observation["payload"]["artifact_hash"]
            if content_observation is not None else None
        ),
        "metadata_hash":(
            metadata_observation["payload"]["artifact_hash"]
            if metadata_observation is not None else None
        ),
        "content_observation_id":(
            content_observation["record_id"]
            if content_observation is not None else None
        ),
        "metadata_observation_id":(
            metadata_observation["record_id"]
            if metadata_observation is not None else None
        ),
    }
