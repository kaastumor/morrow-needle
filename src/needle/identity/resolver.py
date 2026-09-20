from __future__ import annotations

from collections import defaultdict, deque
from typing import Any


EQUIVALENCE_RELATIONS = {
    "SAME_LEGAL_RESOURCE":"LEGAL_RESOURCE",
    "SAME_TEXT_STATE":"TEXT_STATE",
    "SAME_EXPRESSION":"EXPRESSION",
    "SAME_MANIFESTATION":"MANIFESTATION",
}


class IdentityGraphError(ValueError):
    pass


class TypedIdentifierGraph:
    def __init__(self, graph: dict[str, Any]):
        self.graph = graph
        self.nodes = {node["node_id"]: node for node in graph["identifiers"]}
        if len(self.nodes) != len(graph["identifiers"]):
            raise IdentityGraphError("duplicate identifier node_id")

        self.relations = graph["relations"]
        self._out: dict[str, list[dict[str, Any]]] = defaultdict(list)
        self._in: dict[str, list[dict[str, Any]]] = defaultdict(list)

        for relation in self.relations:
            source = relation["from_node_id"]
            target = relation["to_node_id"]
            if source not in self.nodes or target not in self.nodes:
                raise IdentityGraphError(
                    f"relation {relation['relation_id']} references unknown node"
                )
            self._validate_relation_levels(relation)
            self._out[source].append(relation)
            self._in[target].append(relation)

    def _validate_relation_levels(self, relation: dict[str, Any]) -> None:
        relation_type = relation["relation_type"]
        source = self.nodes[relation["from_node_id"]]
        target = self.nodes[relation["to_node_id"]]

        expected_level = EQUIVALENCE_RELATIONS.get(relation_type)
        if expected_level is not None:
            if source["identity_level"] != expected_level or target["identity_level"] != expected_level:
                raise IdentityGraphError(
                    f"{relation_type} must connect two {expected_level} identifiers"
                )
            return

        allowed = {
            "EXPRESSION_OF": ({"EXPRESSION"}, {"LEGAL_RESOURCE","TEXT_STATE"}),
            "MANIFESTATION_OF": ({"MANIFESTATION"}, {"EXPRESSION"}),
            "ITEM_OF": ({"ITEM"}, {"MANIFESTATION"}),
            "TEXT_STATE_OF": ({"TEXT_STATE"}, {"LEGAL_RESOURCE"}),
            "SUBDIVISION_OF": ({"SUBDIVISION"}, {"LEGAL_RESOURCE","TEXT_STATE"}),
            "CORRIGENDUM_OF": ({"LEGAL_RESOURCE"}, {"LEGAL_RESOURCE"}),
            "DOCUMENT_IN_PROCEDURE": ({"LEGAL_RESOURCE"}, {"PROCEDURE"}),
            "RESULT_OF_PROCEDURE": ({"LEGAL_RESOURCE"}, {"PROCEDURE"}),
            "PUBLISHED_AS": ({"LEGAL_RESOURCE","TEXT_STATE"}, {"PUBLICATION_CITATION"}),
        }
        if relation_type not in allowed:
            raise IdentityGraphError(f"unsupported relation type {relation_type}")
        source_levels, target_levels = allowed[relation_type]
        if source["identity_level"] not in source_levels or target["identity_level"] not in target_levels:
            raise IdentityGraphError(
                f"{relation_type} invalid levels: {source['identity_level']} -> {target['identity_level']}"
            )

        if relation_type == "CORRIGENDUM_OF" and source["resource_kind"] != "CORRIGENDUM":
            raise IdentityGraphError("CORRIGENDUM_OF source must be a corrigendum")

    def find(self, scheme: str, value: str) -> dict[str, Any] | None:
        matches = [
            node for node in self.nodes.values()
            if node["scheme"] == scheme and node["value"] == value
        ]
        if len(matches) > 1:
            raise IdentityGraphError(f"identifier is not unique: {scheme}:{value}")
        return matches[0] if matches else None

    def equivalents(self, node_id: str) -> list[dict[str, Any]]:
        if node_id not in self.nodes:
            raise IdentityGraphError(f"unknown node {node_id}")
        level = self.nodes[node_id]["identity_level"]
        relation_type = next(
            (rel for rel, expected in EQUIVALENCE_RELATIONS.items() if expected == level),
            None,
        )
        if relation_type is None:
            return [self.nodes[node_id]]

        seen = {node_id}
        queue = deque([node_id])
        while queue:
            current = queue.popleft()
            for relation in self._out[current] + self._in[current]:
                if relation["relation_type"] != relation_type:
                    continue
                other = (
                    relation["to_node_id"]
                    if relation["from_node_id"] == current
                    else relation["from_node_id"]
                )
                if other not in seen:
                    seen.add(other)
                    queue.append(other)
        return [self.nodes[key] for key in sorted(seen)]

    def related(
        self,
        node_id: str,
        relation_type: str,
        *,
        direction: str = "out",
    ) -> list[dict[str, Any]]:
        if direction not in {"out","in"}:
            raise IdentityGraphError("direction must be 'out' or 'in'")
        relations = self._out[node_id] if direction == "out" else self._in[node_id]
        result = []
        for relation in relations:
            if relation["relation_type"] != relation_type:
                continue
            other_id = (
                relation["to_node_id"] if direction == "out"
                else relation["from_node_id"]
            )
            result.append(self.nodes[other_id])
        return result

    def same_identity(self, left_node_id: str, right_node_id: str) -> bool:
        return any(
            node["node_id"] == right_node_id
            for node in self.equivalents(left_node_id)
        )



def resolve_query(graph: TypedIdentifierGraph, query: dict[str, Any]) -> dict[str, Any]:
    """Resolve only the identity relation the caller explicitly requested."""
    node = graph.find(query["input"]["scheme"], query["input"]["value"])
    if node is None:
        return {
            "state":"NOT_FOUND",
            "query_id":query["query_id"],
            "input":query["input"],
            "results":[],
        }

    if query["mode"] == "EQUIVALENTS":
        results = graph.equivalents(node["node_id"])
    elif query["mode"] == "RELATION":
        results = graph.related(
            node["node_id"],
            query["relation_type"],
            direction=query.get("direction","out"),
        )
    else:
        raise IdentityGraphError(f"unsupported resolution mode: {query['mode']}")

    return {
        "state":"RESOLVED",
        "query_id":query["query_id"],
        "input_node":node,
        "mode":query["mode"],
        "relation_type":query.get("relation_type"),
        "results":results,
    }
