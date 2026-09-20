from __future__ import annotations

import hashlib
import re
from collections import defaultdict
from typing import Any


def normalize_compare_text(text: str) -> str:
    """Minimal canonicalization for deterministic comparison.

    Only collapses Unicode whitespace. It deliberately preserves punctuation,
    casing, numbers, dates, modal verbs, and visible legal labels.
    """
    return re.sub(r"\s+", " ", text).strip()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


class LegalASTBuilder:
    def __init__(
        self,
        *,
        state_id: str,
        source: dict[str, Any],
        source_observation_id: str,
        completeness_state: str = "UNKNOWN_COMPLETENESS",
        representation_plan_id: str | None = None,
    ) -> None:
        self.state_id = state_id
        self.source = source
        self.source_observation_id = source_observation_id
        self.nodes: list[dict[str, Any]] = []
        self.segments: list[dict[str, Any]] = []
        self.references: list[dict[str, Any]] = []
        self.annotations: list[dict[str, Any]] = []
        self.warnings: list[str] = []
        self.declared_losses: list[str] = []
        self.unknown_native_kinds: set[str] = set()
        self.unassembled_fragments = 0
        self._node_counter = 0
        self._segment_counter = 0
        self._reference_counter = 0
        self._annotation_counter = 0
        self._document_order = 0
        self._sibling_counts: dict[str | None, int] = defaultdict(int)
        self._segment_counts: dict[str, int] = defaultdict(int)
        self.visible_chars_source_estimate = 0
        self.completeness_state = completeness_state
        self.representation_plan_id = representation_plan_id
        self.known_gaps: list[str] = []
        self.cross_representation_checks: list[str] = []

    def anchor(
        self,
        *,
        native_path: str | None = None,
        native_identifier: str | None = None,
        item_uri: str | None = None,
        char_start: int | None = None,
        char_end: int | None = None,
    ) -> dict[str, Any]:
        return {
            "source_observation_id": self.source_observation_id,
            "item_uri": item_uri,
            "native_path": native_path,
            "native_identifier": native_identifier,
            "char_start": char_start,
            "char_end": char_end,
        }

    def add_node(
        self,
        *,
        kind: str,
        parent_id: str | None,
        native_kind: str | None,
        native_identifier: str | None,
        source_anchor: dict[str, Any],
        display_label: str | None = None,
        citation_path: str | None = None,
        eli_subdivision_uri: str | None = None,
        presence_state: str = "PRESENT",
        native_attributes: dict[str, Any] | None = None,
        table_coordinates: dict[str, Any] | None = None,
    ) -> str:
        self._node_counter += 1
        self._document_order += 1
        node_id = f"{self.state_id}:n{self._node_counter:06d}"
        ordinal = self._sibling_counts[parent_id]
        self._sibling_counts[parent_id] += 1
        self.nodes.append(
            {
                "node_id": node_id,
                "parent_id": parent_id,
                "kind": kind,
                "native_kind": native_kind,
                "native_identifier": native_identifier,
                "ordinal": ordinal,
                "document_order": self._document_order,
                "display_label": display_label,
                "citation_path": citation_path,
                "eli_subdivision_uri": eli_subdivision_uri,
                "presence_state": presence_state,
                "table_coordinates": table_coordinates,
                "native_attributes": native_attributes or {},
                "source_anchor": source_anchor,
            }
        )
        return node_id

    def add_segment(
        self,
        *,
        node_id: str,
        role: str,
        text: str,
        source_anchor: dict[str, Any],
        native_kind: str | None = None,
    ) -> str | None:
        source_text = normalize_compare_text(text)
        if not source_text:
            return None
        compare_text = normalize_compare_text(source_text)
        self._segment_counter += 1
        self._document_order += 1
        segment_id = f"{self.state_id}:s{self._segment_counter:06d}"
        ordinal = self._segment_counts[node_id]
        self._segment_counts[node_id] += 1
        self.segments.append(
            {
                "segment_id": segment_id,
                "node_id": node_id,
                "ordinal": ordinal,
                "document_order": self._document_order,
                "role": role,
                "native_kind": native_kind,
                "text_source": source_text,
                "text_compare": compare_text,
                "source_hash": sha256_text(source_text),
                "compare_hash": sha256_text(compare_text),
                "source_anchor": source_anchor,
            }
        )
        return segment_id

    def add_reference(
        self,
        *,
        segment_id: str,
        kind: str,
        display_text: str,
        source_anchor: dict[str, Any],
        source_target_uri: str | None = None,
        resolved_identifiers: dict[str, Any] | None = None,
        resolution_state: str = "UNRESOLVED",
    ) -> str:
        self._reference_counter += 1
        reference_id = f"{self.state_id}:r{self._reference_counter:06d}"
        self.references.append(
            {
                "reference_id": reference_id,
                "segment_id": segment_id,
                "kind": kind,
                "display_text": display_text,
                "source_target_uri": source_target_uri,
                "resolved_identifiers": resolved_identifiers or {},
                "resolution_state": resolution_state,
                "source_anchor": source_anchor,
            }
        )
        return reference_id

    def add_annotation(
        self,
        *,
        kind: str,
        source_anchor: dict[str, Any],
        data: dict[str, Any],
        target_node_ids: list[str] | None = None,
        target_segment_ids: list[str] | None = None,
        end_source_anchor: dict[str, Any] | None = None,
    ) -> str:
        self._annotation_counter += 1
        annotation_id = f"{self.state_id}:a{self._annotation_counter:06d}"
        self.annotations.append(
            {
                "annotation_id": annotation_id,
                "kind": kind,
                "source_anchor": source_anchor,
                "end_source_anchor": end_source_anchor,
                "target_node_ids": target_node_ids or [],
                "target_segment_ids": target_segment_ids or [],
                "data": data,
            }
        )
        return annotation_id

    def finalize(self, *, fidelity: str) -> dict[str, Any]:
        visible_chars_mapped = sum(len(s["text_source"]) for s in self.segments)
        return {
            "ast_version": "0.1",
            "state_id": self.state_id,
            "source": self.source,
            "nodes": self.nodes,
            "segments": self.segments,
            "references": self.references,
            "annotations": self.annotations,
            "parse_report": {
                "fidelity": fidelity,
                "visible_chars_source_estimate": self.visible_chars_source_estimate,
                "visible_chars_mapped": visible_chars_mapped,
                "unknown_native_kinds": sorted(self.unknown_native_kinds),
                "unresolved_references": sum(
                    1 for r in self.references if r["resolution_state"] == "UNRESOLVED"
                ),
                "unassembled_fragments": self.unassembled_fragments,
                "warnings": self.warnings,
                "declared_losses": self.declared_losses,
            },
            "completeness": {
                "state": self.completeness_state,
                "representation_plan_id": self.representation_plan_id,
                "known_gaps": self.known_gaps,
                "cross_representation_checks": self.cross_representation_checks,
            },
        }
