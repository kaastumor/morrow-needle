from __future__ import annotations

import io
import zipfile
import xml.etree.ElementTree as ET
from collections import Counter
from typing import Any

from needle.ast.accounting import XMLTextLedger, aggregate_accounting_reports
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
    "CONS.ANNEX": "ANNEX",
    "APPENDIX": "APPENDIX",
    "FORM": "FORM",
    "FOOTNOTE": "FOOTNOTE",
    "NOTE": "FOOTNOTE",
    "LIST": "LIST",
    "ITEM": "LIST_ITEM",
    "TABLE": "TABLE",
    "TBL": "TABLE",
    "ROW": "TABLE_ROW",
    "CELL": "TABLE_CELL",
    "CONSID": "RECITAL",
    "RECITAL": "RECITAL",
    "PREAMBLE": "PREAMBLE",
    "ENACTING.TERMS": "ENACTING_TERMS",
    "ENACTING-TERMS": "ENACTING_TERMS",
    "FINAL": "SIGNATURE",
    "SIGNATURE": "SIGNATURE",
}

LABEL_TAGS = {
    "TI.ART", "NO.ART", "NO.ARTICLE", "NO.PARAG", "NO.P", "NO.PNT",
    "NO.POINT", "NO.EL", "NO.DASH", "NO.ITEM", "NO.ANNEX", "NUM",
}
HEADING_TAGS = {
    "STI.ART", "TI.CHAP", "TI.SECTION", "TI.SUBSECTION", "TI.PART",
    "TI.TITLE", "TI.ANNEX", "TITLE", "STITLE", "GR.TITLE", "HD", "HT",
}
OPAQUE_MEDIA_TAGS = {"INCL.ELEMENT", "FIGURE", "IMAGE", "IMG", "GRAPHIC"}
KNOWN_TEXT_WRAPPERS = {
    "P", "TXT", "DEFINITION", "VISA", "PREAMBLE.INIT", "PREAMBLE.FINAL",
    "REF.DOC", "REF.DOC.OJ", "LINK", "DATE", "PLACE", "NAME", "QUOT.START",
    "QUOT.END", "FORMULA", "MATH", "EXPR",
}

SOURCE_METADATA_TAGS = {
    "BIB.DOC", "BIB.INSTANCE", "BIB.INSTANCE.CONS", "NO.CELEX",
}
PUBLICATION_NAVIGATION_TAGS = {
    "CONTENTS", "TOC", "ITEM.REF",
}
PROVENANCE_ONLY_TAGS = {
    "GR.ANNOTATION", "GR.CORRIG", "GR.MOD.ACT", "GR.NOTES",
}


def local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].upper()


def text_of(element: ET.Element) -> str:
    return normalize_compare_text("".join(element.itertext()))


def _native_identifier(element: ET.Element) -> str | None:
    for key in ("IDENTIFIER", "ID", "ITEM.ID"):
        if key in element.attrib:
            return element.attrib[key]
    return None


def _label_and_heading(
    element: ET.Element,
) -> tuple[str | None, str | None, ET.Element | None, ET.Element | None]:
    label = None
    heading = None
    label_element = None
    heading_element = None
    for child in list(element):
        tag = local(child.tag)
        value = text_of(child)
        if not value:
            continue
        if tag in LABEL_TAGS and label is None:
            label = value
            label_element = child
        elif tag in HEADING_TAGS and heading is None:
            heading = value
            heading_element = child
    return label, heading, label_element, heading_element


def _classify_unclaimed_atom(atom: dict[str, Any]) -> tuple[str, str]:
    tags = set(atom.get("native_tags", ()))
    if tags & OPAQUE_MEDIA_TAGS:
        return "OPAQUE_OR_EMBEDDED", "text belongs to opaque/embedded source object"
    if tags & SOURCE_METADATA_TAGS:
        return "SOURCE_METADATA", "source-native bibliographic/identity metadata"
    if tags & PUBLICATION_NAVIGATION_TAGS:
        return "PUBLICATION_NAVIGATION", "source-native contents/navigation material"
    if tags & PROVENANCE_ONLY_TAGS:
        return "PROVENANCE_ONLY", "source-native consolidation/provenance material"
    return "UNEXPLAINED", "no canonical parser disposition assigned"


def _has_structural_descendant(element: ET.Element) -> bool:
    return any(
        desc is not element and local(desc.tag) in STRUCTURAL_KINDS
        for desc in element.iter()
    )


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
        self.accounting_reports: list[dict[str, Any]] = []
        self._ledger: XMLTextLedger | None = None

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
                text = raw.decode("utf-8", errors="replace")
                if "�" in text:
                    self.builder.warnings.append(f"{name}: invalid UTF-8 replaced")

                try:
                    root = ET.fromstring(text)
                except ET.ParseError as exc:
                    self.builder.warnings.append(f"{name}: XML parse error: {exc}")
                    self.builder.unassembled_fragments += 1
                    continue

                self.parsed_entries.append(name)
                self._ledger = XMLTextLedger(root, source_entry=name)

                # Treat each physical XML file as a fragment whose root may itself
                # be a legal structure (notably ANNEX). Wrapping it ensures root
                # structures and nested structures use exactly the same mapping path.
                fragment_container = ET.Element("NEEDLE.FRAGMENT")
                fragment_container.append(root)
                self._walk_structures(
                    fragment_container,
                    self.root_id,
                    native_path=name,
                    citation_stack=[],
                    capture_unstructured_text=True,
                )

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

                self._ledger.classify_unclaimed(_classify_unclaimed_atom)
                self.accounting_reports.append(self._ledger.report())
                self._ledger = None

            accounting = aggregate_accounting_reports(self.accounting_reports)
            self.builder.visible_chars_source_estimate = accounting["source_chars"]
            self.builder.set_source_text_accounting(accounting)

            if accounting["duplicate_claim_count"]:
                self.builder.warnings.append(
                    "source-text ledger recorded {} duplicate claims".format(
                        accounting["duplicate_claim_count"]
                    )
                )
            if accounting["unexplained_chars"]:
                self.builder.declared_losses.append(
                    "{} normalized source-text characters remain unexplained".format(
                        accounting["unexplained_chars"]
                    )
                )

            if len(xml_names) > 1:
                self.builder.cross_representation_checks.append(
                    f"FORMEX_FRAGMENT_SET:{len(xml_names)}_XML_ENTRIES"
                )

        fidelity = "FULL_STRUCTURAL"
        if self.builder.unassembled_fragments or self.builder.unknown_native_kinds:
            fidelity = "PARTIAL_STRUCTURAL"
        return self.builder.finalize(fidelity=fidelity)

    def _walk_structures(
        self,
        element: ET.Element,
        parent_id: str,
        *,
        native_path: str,
        citation_stack: list[str],
        capture_unstructured_text: bool,
    ) -> None:
        for child in list(element):
            tag = local(child.tag)
            self.tag_counts[tag] += 1

            if tag in LABEL_TAGS or tag in HEADING_TAGS:
                continue

            if tag in OPAQUE_MEDIA_TAGS:
                self.builder.known_gaps.append(
                    f"{native_path}: opaque media element {tag}"
                )
                if self._ledger is not None:
                    self._ledger.claim_subtree(
                        child,
                        category="OPAQUE_OR_EMBEDDED",
                        reason=f"opaque source element {tag}",
                    )
                continue

            kind = STRUCTURAL_KINDS.get(tag)
            if kind is not None:
                label, heading, label_element, heading_element = _label_and_heading(child)
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
                    if self._ledger is not None and label_element is not None:
                        self._ledger.claim_subtree(
                            label_element,
                            category="LEGAL_MAPPED",
                            reason="canonical structural label",
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
                    if self._ledger is not None and heading_element is not None:
                        self._ledger.claim_subtree(
                            heading_element,
                            category="LEGAL_MAPPED",
                            reason="canonical structural heading",
                        )

                self._emit_leaf_text(child, node_id, native_path=native_path)
                self._walk_structures(
                    child,
                    node_id,
                    native_path=native_path,
                    citation_stack=next_stack,
                    capture_unstructured_text=False,
                )
                continue

            if _has_structural_descendant(child):
                self._walk_structures(
                    child,
                    parent_id,
                    native_path=native_path,
                    citation_stack=citation_stack,
                    capture_unstructured_text=capture_unstructured_text,
                )
                continue

            if tag in SOURCE_METADATA_TAGS:
                if self._ledger is not None:
                    self._ledger.claim_subtree(
                        child,
                        category="SOURCE_METADATA",
                        reason=f"source metadata element {tag}",
                    )
                continue
            if tag in PUBLICATION_NAVIGATION_TAGS:
                if self._ledger is not None:
                    self._ledger.claim_subtree(
                        child,
                        category="PUBLICATION_NAVIGATION",
                        reason=f"publication navigation element {tag}",
                    )
                continue
            if tag in PROVENANCE_ONLY_TAGS:
                if self._ledger is not None:
                    self._ledger.claim_subtree(
                        child,
                        category="PROVENANCE_ONLY",
                        reason=f"source provenance element {tag}",
                    )
                continue

            # Text outside any mapped structural child is preserved on the current
            # canonical node. Unknown wrapper names are reported, not silently lost.
            if not capture_unstructured_text:
                continue

            value = text_of(child)
            if value:
                if tag not in KNOWN_TEXT_WRAPPERS:
                    self.builder.unknown_native_kinds.add(tag)
                segment_id = self.builder.add_segment(
                    node_id=parent_id,
                    role="INLINE_OTHER",
                    text=value,
                    native_kind=tag,
                    source_anchor=self.builder.anchor(
                        native_path=native_path,
                        native_identifier=_native_identifier(child),
                    ),
                )
                if segment_id:
                    if self._ledger is not None:
                        self._ledger.claim_subtree(
                            child,
                            category="LEGAL_MAPPED",
                            reason="top-level legal text wrapper mapped to canonical segment",
                        )
                    self._emit_references(
                        child,
                        segment_id,
                        native_path=native_path,
                    )

    def _emit_leaf_text(
        self,
        element: ET.Element,
        node_id: str,
        *,
        native_path: str,
    ) -> None:
        direct = normalize_compare_text(element.text or "")
        if direct:
            self.builder.add_segment(
                node_id=node_id,
                role="BODY",
                text=direct,
                native_kind=local(element.tag),
                source_anchor=self.builder.anchor(
                    native_path=native_path,
                    native_identifier=_native_identifier(element),
                ),
            )
            if self._ledger is not None:
                self._ledger.claim_element_text(
                    element,
                    category="LEGAL_MAPPED",
                    reason="direct text of canonical structural node",
                )

        for child in list(element):
            tag = local(child.tag)

            if tag in LABEL_TAGS or tag in HEADING_TAGS:
                continue
            if tag in STRUCTURAL_KINDS:
                continue
            if tag in OPAQUE_MEDIA_TAGS:
                self.builder.known_gaps.append(
                    f"{native_path}: opaque media element {tag}"
                )
                continue
            if _has_structural_descendant(child):
                continue

            value = text_of(child)
            if not value:
                continue
            if tag not in KNOWN_TEXT_WRAPPERS:
                self.builder.unknown_native_kinds.add(tag)

            role = "CELL_TEXT" if any(
                n["node_id"] == node_id and n["kind"] == "TABLE_CELL"
                for n in self.builder.nodes[-1:]
            ) else "BODY"

            segment_id = self.builder.add_segment(
                node_id=node_id,
                role=role,
                text=value,
                native_kind=tag,
                source_anchor=self.builder.anchor(
                    native_path=native_path,
                    native_identifier=_native_identifier(child),
                ),
            )
            if segment_id:
                if self._ledger is not None:
                    self._ledger.claim_subtree(
                        child,
                        category="LEGAL_MAPPED",
                        reason="legal leaf wrapper mapped to canonical segment",
                    )
                self._emit_references(child, segment_id, native_path=native_path)

    def _emit_references(
        self,
        element: ET.Element,
        segment_id: str,
        *,
        native_path: str,
    ) -> None:
        for desc in element.iter():
            desc_tag = local(desc.tag)
            target = _reference_target(desc)
            if not target and "REF" not in desc_tag:
                continue
            display = text_of(desc)
            if not display:
                continue
            self.builder.add_reference(
                segment_id=segment_id,
                kind=_reference_kind(target, desc_tag),
                display_text=display,
                source_target_uri=target,
                resolution_state="SOURCE_RESOLVED" if target else "UNRESOLVED",
                source_anchor=self.builder.anchor(
                    native_path=native_path,
                    native_identifier=_native_identifier(desc),
                ),
            )
