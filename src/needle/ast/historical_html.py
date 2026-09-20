from __future__ import annotations

import html as html_lib
import re
from html.parser import HTMLParser
from typing import Any

from needle.ast.builder import LegalASTBuilder, normalize_compare_text


BLOCK_TAGS = {
    "p", "div", "li", "td", "th", "h1", "h2", "h3", "h4", "h5", "h6",
}
ARTICLE_RE = re.compile(r"^Article\s+(?P<label>\d+[A-Za-z]?)\b", re.IGNORECASE)
ANNEX_RE = re.compile(r"^Annex(?:\s+(?P<label>[A-Z0-9IVXLC]+))?\b", re.IGNORECASE)


class _BlockExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[dict[str, object]] = []
        self.blocks: list[tuple[str, str]] = []
        self._suppressed_depth = 0

    def handle_starttag(self, tag: str, attrs) -> None:
        tag = tag.lower()
        if tag in {"script", "style", "noscript"}:
            self._suppressed_depth += 1
            return
        if self._suppressed_depth:
            return

        if tag in BLOCK_TAGS:
            self.stack.append({"tag": tag, "parts": []})
        elif tag == "br" and self.stack:
            self.stack[-1]["parts"].append("\n")

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in {"script", "style", "noscript"}:
            self._suppressed_depth = max(0, self._suppressed_depth - 1)
            return
        if self._suppressed_depth or tag not in BLOCK_TAGS:
            return

        # Pop the matching block even if the historical HTML is slightly malformed.
        idx = None
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i]["tag"] == tag:
                idx = i
                break
        if idx is None:
            return

        block = self.stack.pop(idx)
        text = normalize_compare_text(" ".join(block["parts"]))
        if text:
            self.blocks.append((tag, text))

    def handle_data(self, data: str) -> None:
        if self._suppressed_depth or not self.stack:
            return
        # Text belongs to the innermost semantic block. Parent DIVs are fallback
        # containers and should not swallow child paragraphs.
        self.stack[-1]["parts"].append(data)


def extract_blocks(payload: bytes) -> list[tuple[str, str]]:
    text = payload.decode("utf-8", errors="replace")
    parser = _BlockExtractor()
    parser.feed(text)

    # Prefer leaf-ish semantic blocks. DIVs are useful only when the old page
    # has no paragraph/list/table/heading structure at all.
    non_div = [block for block in parser.blocks if block[0] != "div"]
    return non_div or parser.blocks


class HistoricalHTMLASTParser:
    """Conservative parser for older official HTML manifestations.

    It intentionally extracts less structure than Formex. The goal is to
    preserve text and obvious provision boundaries while making lower
    structural fidelity visible in the parse report.
    """

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
            native_kind="HTML_DOCUMENT",
            native_identifier=None,
            source_anchor=self.builder.anchor(),
            native_attributes={},
        )

    def parse(self, payload: bytes, *, native_path: str) -> dict[str, Any]:
        blocks = extract_blocks(payload)
        self.builder.visible_chars_source_estimate = sum(len(text) for _, text in blocks)

        if not blocks:
            self.builder.warnings.append("HTML parser found no visible block text")
            self.builder.declared_losses.append("No legal structure recovered")
            return self.builder.finalize(fidelity="FAILED")

        current_parent = self.root_id
        article_count = 0
        annex_count = 0
        block_count = 0
        seen_text: set[str] = set()

        for tag, raw_text in blocks:
            text = normalize_compare_text(html_lib.unescape(raw_text))
            if not text or text in seen_text:
                continue
            seen_text.add(text)

            article_match = ARTICLE_RE.match(text)
            if article_match:
                article_count += 1
                label = f"Article {article_match.group('label')}"
                current_parent = self.builder.add_node(
                    kind="ARTICLE",
                    parent_id=self.root_id,
                    native_kind=tag.upper(),
                    native_identifier=None,
                    display_label=label,
                    citation_path=label,
                    source_anchor=self.builder.anchor(native_path=native_path),
                    native_attributes={},
                )
                self.builder.add_segment(
                    node_id=current_parent,
                    role="LABEL",
                    text=label,
                    native_kind=tag.upper(),
                    source_anchor=self.builder.anchor(native_path=native_path),
                )
                remainder = text[len(article_match.group(0)):].strip(" :-—\u2013")
                if remainder:
                    self.builder.add_segment(
                        node_id=current_parent,
                        role="BODY",
                        text=remainder,
                        native_kind=tag.upper(),
                        source_anchor=self.builder.anchor(native_path=native_path),
                    )
                continue

            annex_match = ANNEX_RE.match(text)
            if annex_match and len(text) < 120:
                annex_count += 1
                label = text
                current_parent = self.builder.add_node(
                    kind="ANNEX",
                    parent_id=self.root_id,
                    native_kind=tag.upper(),
                    native_identifier=None,
                    display_label=label,
                    citation_path=label,
                    source_anchor=self.builder.anchor(native_path=native_path),
                    native_attributes={},
                )
                self.builder.add_segment(
                    node_id=current_parent,
                    role="LABEL",
                    text=label,
                    native_kind=tag.upper(),
                    source_anchor=self.builder.anchor(native_path=native_path),
                )
                continue

            block_count += 1
            kind = "TABLE_CELL" if tag in {"td", "th"} else "BLOCK"
            node_id = self.builder.add_node(
                kind=kind,
                parent_id=current_parent,
                native_kind=tag.upper(),
                native_identifier=None,
                source_anchor=self.builder.anchor(native_path=native_path),
                native_attributes={},
            )
            self.builder.add_segment(
                node_id=node_id,
                role="CELL_TEXT" if kind == "TABLE_CELL" else "BODY",
                text=text,
                native_kind=tag.upper(),
                source_anchor=self.builder.anchor(native_path=native_path),
            )

        if article_count == 0:
            self.builder.warnings.append("No article boundaries recognized in historical HTML")
        self.builder.cross_representation_checks.append(
            f"HTML_RECOVERY:articles={article_count};annexes={annex_count};blocks={block_count}"
        )

        mapped_chars = sum(len(segment["text_source"]) for segment in self.builder.segments)
        source_chars = self.builder.visible_chars_source_estimate
        unexplained = max(0, source_chars - mapped_chars)
        self.builder.set_source_text_accounting({
            "basis": "HTML_BLOCKS",
            "source_chars": source_chars,
            "accounted_chars": source_chars - unexplained,
            "unexplained_chars": unexplained,
            "unexplained_ratio": 0.0 if source_chars == 0 else unexplained / source_chars,
            "atom_count": len(blocks),
            "duplicate_claim_count": 0,
            "duplicate_claim_examples": [],
            "categories": [
                {
                    "category": "LEGAL_MAPPED",
                    "atom_count": len(blocks) if unexplained == 0 else 0,
                    "chars": source_chars - unexplained,
                    "examples": [],
                },
                {
                    "category": "UNEXPLAINED",
                    "atom_count": 0 if unexplained == 0 else 1,
                    "chars": unexplained,
                    "examples": [],
                },
            ],
        })

        fidelity = "PARTIAL_STRUCTURAL" if article_count else "TEXT_ONLY"
        return self.builder.finalize(fidelity=fidelity)
