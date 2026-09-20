from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from needle.identity.resolver import TypedIdentifierGraph


DEFAULT_CONFIG = Path("fixtures/retrieval/index-sources-v0.1.json")


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def equivalent_act_identifiers(
    act_id: str,
    *,
    root: Path | str = Path("."),
    config_path: Path | str = DEFAULT_CONFIG,
) -> list[dict[str, Any]]:
    """Resolve legal-resource identifier equivalents for retrieval enrichment.

    Only the identity graph's explicit SAME_LEGAL_RESOURCE closure is used.
    Retrieval never promotes hierarchy/relationship edges into aliases.
    """
    root = Path(root)
    config_file = root / Path(config_path)
    if not config_file.exists():
        return []

    if ":" not in act_id:
        return []
    scheme, value = act_id.split(":", 1)

    config = _load_json(config_file)
    aliases: dict[tuple[str, str], dict[str, Any]] = {}

    for graph_path in config.get("identity_graph_paths", []):
        graph = TypedIdentifierGraph(_load_json(root / graph_path))
        node = graph.find(scheme, value)
        if node is None:
            continue
        for equivalent in graph.equivalents(node["node_id"]):
            key = (equivalent["scheme"], equivalent["value"])
            previous = aliases.get(key)
            if previous is not None and (
                previous["identity_level"] != equivalent["identity_level"]
                or previous["resource_kind"] != equivalent["resource_kind"]
            ):
                raise ValueError(
                    "conflicting identifier enrichment for "
                    f"{equivalent['scheme']}:{equivalent['value']}"
                )
            aliases[key] = {
                "scheme":equivalent["scheme"],
                "value":equivalent["value"],
                "node_id":equivalent["node_id"],
                "identity_level":equivalent["identity_level"],
                "resource_kind":equivalent["resource_kind"],
            }

    return sorted(
        aliases.values(),
        key=lambda item:(item["scheme"], item["value"]),
    )
