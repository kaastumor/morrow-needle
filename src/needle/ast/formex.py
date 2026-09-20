from __future__ import annotations

import io
import re
import zipfile
import xml.etree.ElementTree as ET
from collections import Counter
from typing import Any

from needle.ast.builder import LegalASTBuilder, normalize_compare_text
from needle.formex.modifications import parse_modification_markers


STRUCTURAL_KINDS = {
    "ARTICLE": "ARTICLE",
    "PARAG": "PARAGRAPH",
    "PARAGRAPH": "PARAGRAPH",
    "ALINEA": "PARAGRAPH",
    "SUBPARAG": "SUBPARAGRAPH",
    "POINT": "POINT",
    "INDENT": "INDENT",
    "PART": "PART",
    "TITLE": "TITLE",
    "CHAPTER": "CHAPTER",
    "SECTION": "SECTION",
    "SUBSECTION": "SUBSECTION",
    "ANNEX": "ANNEX",
    "APPENDIX": "APPENDIX",
    "FORM": "FORM",
    "FOOTNOTE": "FOOTNOTE",
    "NOTE": "FOOTNOTE",
    "LIST": "LIST",
    "ITEM": "LIST_ITEM",
    "TABLE": "TABLE",
    "ROW": "TABLE_ROW",
    "CELL": "TABLE_CELL",
    "CONSID": "RECITAL",
    "RECITAL": "RECITAL",
    "PREAMBLE": "PREAMBLE",
    "ENACTING.TERMS": "ENACTING_TERMS",
    "ENACTING-TERMS": "ENACTING_TERMS",
    "FINAL": "SIGNATURE",
}

LABEL_TAGS = {
    "TI.ART", "NO.ART", "NO.ARTICLE", "NO.PARAG", "NO.P", "NO.PNT",
    "NO.POINT", "NO.EL", "NO.DASH", "NO.ITEM", "NO.ANNEX", "NUM",
}
HEADING_TAGS = {
    "STI.ART", "TI.CHAP", "TI.SECTION", "TI.SUBSECTION", "TI.PART",
    "TI.TITLE", "TI.ANNEX", "TITLE", "STITLE", "GR.TITLE", "HD",
}
OPAQUE_MEDIA_TAGS = {"INCL.ELEMENT", "FIGURE", "IMAGE", "IMG", "GRAPHIC"}


def local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].upper()


def text_of(element: ET.Element) -> str:
    return normalize_compare_text("".join(element.itertext()))


def _native_identifier(element: ET.Element) -> str | None:
    for key in ("IDENTIFIER", "ID", "ITEM.ID"):
        if key in element.attrib:
            return element.attrib[key]
    return None


def _label_and_heading(element: ET.Element) -> tuple[str | None, str | None]:
    label = None
    heading = None
    for child in list(element):
        tag = local(child.tag)
        value = text_of(child)
        if not value:
            continue
        if tag in LABEL_TAGS and label is None:
            label = value
        elif tag in HEADING_TAGS and heading is None:
            heading = value
    return label, heading


def _direct_text_without_structural_children(element: ET.Element) -> str:
    chunks: list[str] = []
    if element.text:
        chunks.append(element.text)

    for child in list(element):
        tag = local(child.tag)
        if tag in STRUCTURAL_KINDS or tag in LABEL_TAGS or tag in HEADING_TAGS:
            if child.tail:
                chunks.append(child.tail)
            continue
        chunks.extend(child.itertext())
        if child.tail:
            chunks.append(child.tail)

    return normalize_compare_text(" ".join(chunks))


def _reference_target(element: ET.Element) -> str | None:
    for key, value in element.attrib.items():
        upper = key.upper()
        if any(hint in upper for hint in ("URI", "HREF", "REF")):
            if value.startswith(("http://", "https://", "urn:", "CELEX:")):
                return value
    return None


def _reference_kind(target: str | None, tag: str) -> str:
    if target and "data.europa.eu/eli/" in target:
        return "EU_LEGAL_SUBDIVISION"
    if target and ("eur-lex" in target or target.startswith("CELEX:")):
        return "EU_LEGAL_ACT"
    if "NOTE" in tag:
        return "FOOTNOTE"
    return "UNRESOLVED"


class FormexASTParser:
    def __init__(
        self,
        *,
        state_id: str,
        source: dict[str, Any],
        source_observation_id: str,
        representation_plan_id: str | None = None,
    ) -> None:
        self.builder = LegalASTBuilder(
            state_id=state_id,
            source=source,
            source_observation_id=source_observation_id,
            completeness_state="UNKNOWN_COMPLETENESS",
            representation_plan_id=representation_plan_id,
        )
        self.root_id = self.builder.add_node(
            kind="DOCUMENT",
            parent_id=None,
            native_kind="FORMEX_BUNDLE",
            native_identifier=None,
            source_anchor=self.builder.anchor(),
            native_attributes={},
        )
        self.parsed_entries: list[str] = []
        self.tag_counts: Counter[str] = Counter()

    def parse_zip(self, payload: bytes) -> dict[str, Any]:
        with zipfile.ZipFile(io.BytesIO(payload)) as zf:
            names = sorted(zf.namelist())
            xml_names = [n for n in names if n.lower().endswith((".xml", ".frg"))]
            raster_names = [
                n for n in names
                if n.lower().endswith((".tif", ".tiff", ".png", ".jpg", ".jpeg"))
            ]

            if raster_names:
                self.builder.known_gaps.append(
                    f"{len(raster_names)} raster assets require companion-representation completeness checks"
                )
                self.builder.cross_representation_checks.append("RASTER_ASSETS_PRESENT")

            if not xml_names:
                self.builder.warnings.append("No parseable Formex XML entries found")
                self.builder.declared_losses.append("No structured XML content parsed")
                return self.builder.finalize(fidelity="FAILED")

            for name in xml_names:
                raw = zf.read(name)
                try:
                    text = raw.decode("utf-8")
                except UnicodeDecodeError:
                    text = raw.decode("utf-8", errors="replace")
                    self.builder.warnings.append(f"{name}: invalid UTF-8 replaced")

                try:
                    root = ET.fromstring(text)
                except ET.ParseError as exc:
                    self.builder.warnings.append(f"{name}: XML parse error: {exc}")
                    self.builder.unassembled_fragments += 1
                    continue

                self.parsed_entries.append(name)
                self.builder.visible_chars_source_estimate += len(text_of(root))
                self._walk(root, self.root_id, native_path=name, citation_stack=[])

                modification_result = parse_modification_markers(text, source_entry=name)
                for marker in modification_result.markers:
                    self.builder.add_annotation(
                        kind="CONSOLIDATION_MODIFICATION",
                        source_anchor=self.builder.anchor(
                            native_path=name,
                            char_start=marker.start_offset,
                            char_end=marker.end_offset,
                        ),
                        data={
                            "open_id": marker.open_id,
                            "close_id": marker.close_id,
                            "action": marker.action,
                            "level": marker.level,
                            "command": marker.command,
                            "active_doc": marker.active_doc,
                            "active_loc": marker.active_loc,
                            "mod_level": marker.mod_level,
                            "evidence_character": "OFFICIAL_EMBEDDED_CONSOLIDATION_PROVENANCE",
                            "legal_authority_character": "DOCUMENTARY_NON_BINDING",
                        },
                    )

                if modification_result.unmatched_open_ids or modification_result.unmatched_close_ids:
                    self.builder.warnings.append(
                        f"{name}: unmatched CLG.MDF markers "
                        f"open={list(modification_result.unmatched_open_ids)} "
                        f"close={list(modification_result.unmatched_close_ids)}"
                    )

            if len(xml_names) > 1:
                self.builder.cross_representation_checks.append(
                    f"FORMEX_FRAGMENT_SET:{len(xml_names)}_XML_ENTRIES"
                )

        fidelity = "FULL_STRUCTURAL"
        if self.builder.unassembled_fragments or self.builder.unknown_native_kinds:
            fidelity = "PARTIAL_STRUCTURAL"
        return self.builder.finalize(fidelity=fidelity)

    def _walk(
        self,
        element: ET.Element,
        parent_id: str,
        *,
        native_path: str,
        citation_stack: list[str],
    ) -> None:
        for child in list(element):
            tag = local(child.tag)
            self.tag_counts[tag] += 1
            kind = STRUCTURAL_KINDS.get(tag)

            if kind is not None:
                label, heading = _label_and_heading(child)
                native_id = _native_identifier(child)
                citation_piece = label or native_id
                next_stack = citation_stack + ([citation_piece] if citation_piece else [])

                node_id = self.builder.add_node(
                    kind=kind,
                    parent_id=parent_id,
                    native_kind=tag,
                    native_identifier=native_id,
                    source_anchor=self.builder.anchor(
                        native_path=native_path,
                        native_identifier=native_id,
                    ),
                    display_label=label,
                    citation_path=" > ".join(next_stack) if next_stack else None,
                    native_attributes=dict(child.attrib),
                )

                if label:
                    self.builder.add_segment(
                        node_id=node_id,
                        role="LABEL",
                        text=label,
                        native_kind=tag,
                        source_anchor=self.builder.anchor(
                            native_path=native_path,
                            native_identifier=native_id,
                        ),
                    )
                if heading:
                    self.builder.add_segment(
                        node_id=node_id,
                        role="HEADING",
                        text=heading,
                        native_kind=tag,
                        source_anchor=self.builder.anchor(
                            native_path=native_path,
                            native_identifier=native_id,
                        ),
                    )

                body = _direct_text_without_structural_children(child)
                body_segment = None
                if body and body not in {label, heading}:
                    role = "CELL_TEXT" if kind == "TABLE_CELL" else "BODY"
                    body_segment = self.builder.add_segment(
                        node_id=node_id,
                        role=role,
                        text=body,
                        native_kind=tag,
                        source_anchor=self.builder.anchor(
                            native_path=native_path,
                            native_identifier=native_id,
                        ),
                    )

                for desc in child.iter():
                    desc_tag = local(desc.tag)
                    target = _reference_target(desc)
                    if target or "REF" in desc_tag:
                        display = text_of(desc)
                        if not display or body_segment is None:
                            continue
                        self.builder.add_reference(
                            segment_id=body_segment,
                            kind=_reference_kind(target, desc_tag),
                            display_text=display,
                            source_target_uri=target,
                            resolution_state="SOURCE_RESOLVED" if target else "UNRESOLVED",
                            source_anchor=self.builder.anchor(
                                native_path=native_path,
                                native_identifier=_native_identifier(desc),
                            ),
                        )

                    if desc_tag in OPAQUE_MEDIA_TAGS:
                        self.builder.known_gaps.append(
                            f"{native_path}: opaque media element {desc_tag}"
                        )

                self._walk(
                    child,
                    node_id,
                    native_path=native_path,
                    citation_stack=next_stack,
                )
                continue

            if tag in OPAQUE_MEDIA_TAGS:
                self.builder.known_gaps.append(
                    f"{native_path}: opaque media element {tag}"
                )
                continue

            # Retain significant unmapped containers instead of silently dropping them.
            value = text_of(child)
            if value and len(list(child)) == 0 and len(value) > 20:
                self.builder.unknown_native_kinds.add(tag)
                node_id = self.builder.add_node(
                    kind="OTHER",
                    parent_id=parent_id,
                    native_kind=tag,
                    native_identifier=_native_identifier(child),
                    source_anchor=self.builder.anchor(
                        native_path=native_path,
                        native_identifier=_native_identifier(child),
                    ),
                    native_attributes=dict(child.attrib),
                )
                self.builder.add_segment(
                    node_id=node_id,
                    role="INLINE_OTHER",
                    text=value,
                    native_kind=tag,
                    source_anchor=self.builder.anchor(
                        native_path=native_path,
                        native_identifier=_native_identifier(child),
                    ),
                )
            else:
                self._walk(
                    child,
                    parent_id,
                    native_path=native_path,
                    citation_stack=citation_stack,
                )
