"""Parse Formex consolidation modification processing instructions.

These processing instructions are official consolidation provenance. They are
useful evidence for mutation reconstruction, but consolidated texts themselves
are documentary aids and are not the canonical legal authority for a change.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import re
from typing import Iterable


_PI_RE = re.compile(r"<\?CLG\.MDF(?P<kind>[OC])\s+(?P<attrs>[^?]*?)\?>")
_ATTR_RE = re.compile(r'(?P<name>[A-Z0-9.]+)="(?P<value>[^"]*)"')


@dataclass(frozen=True)
class ModificationMarker:
    open_id: str
    close_id: str
    action: str
    level: str
    command: str
    active_doc: str
    active_loc: str
    mod_level: int
    start_offset: int
    end_offset: int
    source_entry: str | None = None

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass(frozen=True)
class ParseResult:
    markers: tuple[ModificationMarker, ...]
    unmatched_open_ids: tuple[str, ...]
    unmatched_close_ids: tuple[str, ...]

    def to_dict(self) -> dict:
        return {
            "markers": [m.to_dict() for m in self.markers],
            "unmatched_open_ids": list(self.unmatched_open_ids),
            "unmatched_close_ids": list(self.unmatched_close_ids),
        }


def _attrs(raw: str) -> dict[str, str]:
    return {m.group("name"): m.group("value") for m in _ATTR_RE.finditer(raw)}


def parse_modification_markers(text: str, *, source_entry: str | None = None) -> ParseResult:
    """Parse paired CLG.MDFO/CLG.MDFC processing instructions.

    Pairing is ID-based rather than stack-only so nested modifications remain
    explicit and malformed input fails visibly.
    """
    opens: dict[str, tuple[dict[str, str], int]] = {}
    markers: list[ModificationMarker] = []
    unmatched_close: list[str] = []

    for match in _PI_RE.finditer(text):
        attrs = _attrs(match.group("attrs"))
        kind = match.group("kind")

        if kind == "O":
            open_id = attrs.get("ID")
            close_id = attrs.get("IDREF")
            if not open_id or not close_id:
                continue
            opens[open_id] = (attrs, match.end())
            continue

        close_id = attrs.get("ID")
        open_id = attrs.get("IDREF")
        if not close_id or not open_id or open_id not in opens:
            if close_id:
                unmatched_close.append(close_id)
            continue

        open_attrs, content_start = opens.pop(open_id)
        try:
            mod_level = int(open_attrs.get("MOD.LEVEL", "0"))
        except ValueError:
            mod_level = 0

        markers.append(
            ModificationMarker(
                open_id=open_id,
                close_id=close_id,
                action=open_attrs.get("ACTION", "UNKNOWN"),
                level=open_attrs.get("LEVEL", "UNKNOWN"),
                command=open_attrs.get("COMMAND", "UNKNOWN"),
                active_doc=open_attrs.get("ACTIVE.DOC", ""),
                active_loc=open_attrs.get("ACTIVE.LOC", ""),
                mod_level=mod_level,
                start_offset=content_start,
                end_offset=match.start(),
                source_entry=source_entry,
            )
        )

    markers.sort(key=lambda m: (m.start_offset, -m.end_offset, m.mod_level))
    return ParseResult(
        markers=tuple(markers),
        unmatched_open_ids=tuple(sorted(opens)),
        unmatched_close_ids=tuple(unmatched_close),
    )


def parse_many(entries: Iterable[tuple[str, str]]) -> ParseResult:
    markers: list[ModificationMarker] = []
    unmatched_open: list[str] = []
    unmatched_close: list[str] = []

    for source_entry, text in entries:
        result = parse_modification_markers(text, source_entry=source_entry)
        markers.extend(result.markers)
        unmatched_open.extend(result.unmatched_open_ids)
        unmatched_close.extend(result.unmatched_close_ids)

    return ParseResult(
        markers=tuple(markers),
        unmatched_open_ids=tuple(unmatched_open),
        unmatched_close_ids=tuple(unmatched_close),
    )
