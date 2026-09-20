from __future__ import annotations

from collections import Counter, defaultdict
import xml.etree.ElementTree as ET
from typing import Any, Callable

from needle.ast.builder import normalize_compare_text


ACCOUNTING_CATEGORIES = (
    "LEGAL_MAPPED",
    "SOURCE_METADATA",
    "PUBLICATION_NAVIGATION",
    "PROVENANCE_ONLY",
    "OPAQUE_OR_EMBEDDED",
    "DUPLICATE_FRAGMENT",
    "UNEXPLAINED",
)


class XMLTextLedger:
    """Account once for each normalized visible XML text atom.

    An atom is one element.text or child.tail slot after whitespace
    normalization. The ledger measures parser disposition without inventing
    legal meaning.
    """

    def __init__(self, root: ET.Element, *, source_entry: str) -> None:
        self.source_entry = source_entry
        self.atoms: dict[str, dict[str, Any]] = {}
        self._subtree_atoms: dict[int, tuple[str, ...]] = {}
        self._element_text_atom: dict[int, str] = {}
        self._child_tail_atom: dict[int, str] = {}
        self._duplicate_claims: list[dict[str, Any]] = []
        self._build(root)

    @staticmethod
    def _local(tag: str) -> str:
        return tag.rsplit("}", 1)[-1].upper()

    def _add_atom(
        self,
        *,
        atom_id: str,
        text: str | None,
        locator: str,
        native_tags: tuple[str, ...],
    ) -> str | None:
        value = normalize_compare_text(text or "")
        if not value:
            return None
        self.atoms[atom_id] = {
            "atom_id": atom_id,
            "text": value,
            "chars": len(value),
            "locator": locator,
            "native_tags": native_tags,
            "category": None,
            "reason": None,
        }
        return atom_id

    def _build(self, root: ET.Element) -> None:
        def walk(
            element: ET.Element,
            *,
            path: str,
            ancestry: tuple[str, ...],
        ) -> list[str]:
            tag = self._local(element.tag)
            tags = ancestry + (tag,)
            owned: list[str] = []

            text_id = f"{self.source_entry}:{path}#text"
            added = self._add_atom(
                atom_id=text_id,
                text=element.text,
                locator=f"{path}#text",
                native_tags=tags,
            )
            if added:
                self._element_text_atom[id(element)] = added
                owned.append(added)

            sibling_counts: Counter[str] = Counter()
            for child in list(element):
                child_tag = self._local(child.tag)
                index = sibling_counts[child_tag]
                sibling_counts[child_tag] += 1
                child_path = f"{path}/{child_tag}[{index}]"
                owned.extend(
                    walk(
                        child,
                        path=child_path,
                        ancestry=tags,
                    )
                )

                # A child's tail belongs to the containing parent flow, not to
                # the child's subtree text returned by Element.itertext().
                tail_id = f"{self.source_entry}:{child_path}#tail"
                tail = self._add_atom(
                    atom_id=tail_id,
                    text=child.tail,
                    locator=f"{child_path}#tail",
                    native_tags=tags,
                )
                if tail:
                    self._child_tail_atom[id(child)] = tail
                    owned.append(tail)

            self._subtree_atoms[id(element)] = tuple(owned)
            return owned

        root_tag = self._local(root.tag)
        walk(root, path=f"/{root_tag}[0]", ancestry=())

    def _claim_atom(self, atom_id: str, *, category: str, reason: str) -> None:
        if category not in ACCOUNTING_CATEGORIES:
            raise ValueError(f"unknown source-text accounting category: {category}")
        atom = self.atoms.get(atom_id)
        if atom is None:
            return
        if atom["category"] is not None:
            self._duplicate_claims.append(
                {
                    "atom_id": atom_id,
                    "locator": atom["locator"],
                    "first_category": atom["category"],
                    "second_category": category,
                    "text_prefix": atom["text"][:180],
                }
            )
            return
        atom["category"] = category
        atom["reason"] = reason

    def claim_element_text(
        self,
        element: ET.Element,
        *,
        category: str,
        reason: str,
    ) -> None:
        atom_id = self._element_text_atom.get(id(element))
        if atom_id:
            self._claim_atom(atom_id, category=category, reason=reason)

    def claim_subtree(
        self,
        element: ET.Element,
        *,
        category: str,
        reason: str,
    ) -> None:
        for atom_id in self._subtree_atoms.get(id(element), ()):
            self._claim_atom(atom_id, category=category, reason=reason)

    def subtree_claim_counts(self, element: ET.Element) -> tuple[int, int]:
        claimed = unclaimed = 0
        for atom_id in self._subtree_atoms.get(id(element), ()):
            atom = self.atoms.get(atom_id)
            if atom is None:
                continue
            if atom["category"] is None:
                unclaimed += 1
            else:
                claimed += 1
        return claimed, unclaimed

    def subtree_has_unclaimed(self, element: ET.Element) -> bool:
        return self.subtree_claim_counts(element)[1] > 0

    def claim_child_tail(
        self,
        child: ET.Element,
        *,
        category: str,
        reason: str,
    ) -> None:
        atom_id = self._child_tail_atom.get(id(child))
        if atom_id:
            self._claim_atom(atom_id, category=category, reason=reason)

    def classify_unclaimed(
        self,
        classifier: Callable[[dict[str, Any]], tuple[str, str]],
    ) -> None:
        for atom in self.atoms.values():
            if atom["category"] is not None:
                continue
            category, reason = classifier(atom)
            self._claim_atom(
                atom["atom_id"],
                category=category,
                reason=reason,
            )

    def report(self, *, examples_per_category: int = 8) -> dict[str, Any]:
        grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for atom in self.atoms.values():
            category = atom["category"] or "UNEXPLAINED"
            grouped[category].append(atom)

        categories = []
        for category in ACCOUNTING_CATEGORIES:
            atoms = grouped.get(category, [])
            chars = sum(atom["chars"] for atom in atoms)
            categories.append(
                {
                    "category": category,
                    "atom_count": len(atoms),
                    "chars": chars,
                    "examples": [
                        {
                            "locator": atom["locator"],
                            "native_tags": list(atom["native_tags"]),
                            "reason": atom["reason"],
                            "text_prefix": atom["text"][:220],
                        }
                        for atom in atoms[:examples_per_category]
                    ],
                }
            )

        source_chars = sum(atom["chars"] for atom in self.atoms.values())
        unexplained_atoms = [
            atom
            for atom in self.atoms.values()
            if (atom["category"] or "UNEXPLAINED") == "UNEXPLAINED"
        ]
        unexplained = sum(atom["chars"] for atom in unexplained_atoms)

        shape_stats: dict[str, dict[str, Any]] = {}
        for atom in unexplained_atoms:
            slot = "tail" if atom["locator"].endswith("#tail") else "text"
            shape = "/".join(atom["native_tags"]) + f"#{slot}"
            stat = shape_stats.setdefault(
                shape,
                {"shape": shape, "atom_count": 0, "chars": 0, "examples": []},
            )
            stat["atom_count"] += 1
            stat["chars"] += atom["chars"]
            if len(stat["examples"]) < 4:
                stat["examples"].append(
                    {
                        "locator": atom["locator"],
                        "text_prefix": atom["text"][:220],
                    }
                )

        unexplained_shapes = sorted(
            shape_stats.values(),
            key=lambda item: (-item["chars"], -item["atom_count"], item["shape"]),
        )[:30]

        return {
            "basis": "XML_TEXT_ATOMS",
            "source_entry": self.source_entry,
            "source_chars": source_chars,
            "accounted_chars": source_chars - unexplained,
            "unexplained_chars": unexplained,
            "unexplained_ratio": 0.0 if source_chars == 0 else unexplained / source_chars,
            "atom_count": len(self.atoms),
            "duplicate_claim_count": len(self._duplicate_claims),
            "duplicate_claim_examples": self._duplicate_claims[:12],
            "unexplained_shapes": unexplained_shapes,
            "categories": categories,
        }


def aggregate_accounting_reports(reports: list[dict[str, Any]]) -> dict[str, Any]:
    """Aggregate entry-level accounting without discarding examples."""
    if not reports:
        return {
            "basis": "XML_TEXT_ATOMS",
            "source_chars": 0,
            "accounted_chars": 0,
            "unexplained_chars": 0,
            "unexplained_ratio": 0.0,
            "atom_count": 0,
            "duplicate_claim_count": 0,
            "duplicate_claim_examples": [],
            "unexplained_shapes": [],
            "categories": [
                {
                    "category": category,
                    "atom_count": 0,
                    "chars": 0,
                    "examples": [],
                }
                for category in ACCOUNTING_CATEGORIES
            ],
            "entry_count": 0,
        }

    by_category: dict[str, dict[str, Any]] = {
        category: {
            "category": category,
            "atom_count": 0,
            "chars": 0,
            "examples": [],
        }
        for category in ACCOUNTING_CATEGORIES
    }
    duplicate_examples: list[dict[str, Any]] = []
    shape_totals: dict[str, dict[str, Any]] = {}

    for report in reports:
        for category_report in report["categories"]:
            target = by_category[category_report["category"]]
            target["atom_count"] += category_report["atom_count"]
            target["chars"] += category_report["chars"]
            remaining = max(0, 12 - len(target["examples"]))
            target["examples"].extend(category_report["examples"][:remaining])

        remaining = max(0, 20 - len(duplicate_examples))
        duplicate_examples.extend(report["duplicate_claim_examples"][:remaining])

        for shape in report.get("unexplained_shapes", []):
            target = shape_totals.setdefault(
                shape["shape"],
                {
                    "shape": shape["shape"],
                    "atom_count": 0,
                    "chars": 0,
                    "examples": [],
                },
            )
            target["atom_count"] += shape["atom_count"]
            target["chars"] += shape["chars"]
            remaining_examples = max(0, 6 - len(target["examples"]))
            target["examples"].extend(shape["examples"][:remaining_examples])

    source_chars = sum(report["source_chars"] for report in reports)
    unexplained = sum(report["unexplained_chars"] for report in reports)
    return {
        "basis": "XML_TEXT_ATOMS",
        "source_chars": source_chars,
        "accounted_chars": source_chars - unexplained,
        "unexplained_chars": unexplained,
        "unexplained_ratio": 0.0 if source_chars == 0 else unexplained / source_chars,
        "atom_count": sum(report["atom_count"] for report in reports),
        "duplicate_claim_count": sum(
            report["duplicate_claim_count"] for report in reports
        ),
        "duplicate_claim_examples": duplicate_examples,
        "unexplained_shapes": sorted(
            shape_totals.values(),
            key=lambda item: (-item["chars"], -item["atom_count"], item["shape"]),
        )[:40],
        "categories": [by_category[c] for c in ACCOUNTING_CATEGORIES],
        "entry_count": len(reports),
    }
