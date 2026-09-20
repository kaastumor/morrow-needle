from __future__ import annotations

import hashlib
import re
from typing import Any


DETERMINISTIC_EFFECT_PATTERNS = {
    "DUTY": [r"\bshall\b", r"\bmust\b"],
    "PROHIBITION": [r"\bshall\s+not\b", r"\bmust\s+not\b", r"\bprohibited\b"],
    "PERMISSION": [r"\bmay\b"],
    "POWER": [r"\bmay\b"],
    "RIGHT": [r"\bright\b", r"\bentitled\b"],
    "DEFINITION": [r"\bmeans\b", r"\bshall\s+mean\b"],
    "LEGAL_STATUS": [
        r"\bshall\s+not\s+be\s+considered\b",
        r"\bshall\s+be\s+considered\b",
        r"\bdeemed\b",
    ],
}


def _normalise(value: str) -> str:
    return " ".join(value.split()).strip().lower()


def validate_atom(
    atom: dict[str, Any],
    *,
    mutations: dict[str, dict[str, Any]],
    source_span_registry: dict[str, dict[str, Any]],
    temporal_assertions: dict[str, dict[str, Any]],
    procedure_state_refs: set[str] | None = None,
) -> list[str]:
    """Deterministic adversary checks for Change Atom v0.3.

    This does not prove legal interpretation generally. It enforces hard
    provenance boundaries around claims eligible for VERIFIED publication.
    """
    errors: list[str] = []
    procedure_state_refs = procedure_state_refs or set()

    mutation_records = []
    for mutation_id in atom.get("source_mutation_ids", []):
        mutation = mutations.get(mutation_id)
        if mutation is None:
            errors.append(f"unknown source mutation: {mutation_id}")
            continue
        mutation_records.append(mutation)
        if atom.get("verification_state") == "VERIFIED":
            if mutation.get("verification_state") != "VERIFIED":
                errors.append(
                    f"VERIFIED atom depends on unverified mutation: {mutation_id}"
                )

    span_texts: dict[str, str] = {}
    for span in atom.get("source_spans", []):
        span_id = span["span_id"]
        registered = source_span_registry.get(span_id)
        if registered is None:
            errors.append(f"unknown source span: {span_id}")
            continue
        text = registered.get("text", "")
        digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
        if digest != span["text_hash"]:
            errors.append(f"source span hash mismatch: {span_id}")
        if registered.get("identifier") != span["identifier"]:
            errors.append(f"source span identifier mismatch: {span_id}")
        if registered.get("language") != span["language"]:
            errors.append(f"source span language mismatch: {span_id}")
        if registered.get("locator") and registered.get("locator") != span["locator"]:
            errors.append(f"source span locator mismatch: {span_id}")
        if registered.get("artifact_hash") and registered.get("artifact_hash") != span["artifact_hash"]:
            errors.append(f"source span artifact hash mismatch: {span_id}")
        span_texts[span_id] = text

    referenced_span_ids = {span["span_id"] for span in atom.get("source_spans", [])}
    for entity in atom.get("affected_entities", []):
        missing = set(entity.get("source_span_ids", [])) - referenced_span_ids
        if missing:
            errors.append(
                "affected entity references non-atom source spans: "
                + ", ".join(sorted(missing))
            )

    for temporal_id in atom.get("temporal_assertion_refs", []):
        if temporal_id not in temporal_assertions:
            errors.append(f"unknown temporal assertion: {temporal_id}")

    for procedure_id in atom.get("procedure_state_refs", []):
        if procedure_id not in procedure_state_refs:
            errors.append(f"unknown procedure state reference: {procedure_id}")

    if atom.get("verification_state") != "VERIFIED":
        return errors

    basis = atom.get("semantic_basis", {})
    method = basis.get("classification_method")
    searchable = _normalise(" ".join(span_texts.values()))

    for term in basis.get("trigger_terms", []):
        if _normalise(term) not in searchable:
            errors.append(f"unsupported semantic trigger term: {term!r}")
    for term in basis.get("qualifier_terms", []):
        if _normalise(term) not in searchable:
            errors.append(f"unsupported qualifier term: {term!r}")

    if method == "DETERMINISTIC_LEGAL_LANGUAGE":
        effect = atom.get("claim", {}).get("legal_effect")
        patterns = DETERMINISTIC_EFFECT_PATTERNS.get(effect)
        basis_text = _normalise(" ".join(basis.get("trigger_terms", [])))
        if patterns is None and effect not in {"NONE"}:
            errors.append(
                f"no deterministic verification rule for legal effect: {effect}"
            )
        elif patterns and not any(
            re.search(pattern, basis_text, flags=re.IGNORECASE)
            for pattern in patterns
        ):
            errors.append(
                f"deterministic basis does not support legal effect {effect}"
            )

    if not any(
        span.get("role") == "SEMANTIC_CLAIM"
        for span in atom.get("source_spans", [])
    ):
        errors.append("VERIFIED atom requires a SEMANTIC_CLAIM source span")

    return errors



def validate_atom_set(atoms: list[dict[str, Any]]) -> list[str]:
    """Validate cross-atom graph integrity independently of atom semantics."""
    errors: list[str] = []
    ids = [atom.get("atom_id") for atom in atoms]
    duplicates = sorted({atom_id for atom_id in ids if ids.count(atom_id) > 1})
    for atom_id in duplicates:
        errors.append(f"duplicate atom_id: {atom_id}")

    by_id = {atom["atom_id"]: atom for atom in atoms if atom.get("atom_id")}
    for atom in atoms:
        source_id = atom.get("atom_id")
        source_languages = set(atom.get("language_scope", {}).get("languages", []))
        for relation in atom.get("relations", []):
            target_id = relation["target_atom_id"]
            if target_id == source_id:
                errors.append(f"self-referential atom relation: {source_id}")
                continue
            target = by_id.get(target_id)
            if target is None:
                errors.append(
                    f"unknown relation target from {source_id}: {target_id}"
                )
                continue
            target_languages = set(
                target.get("language_scope", {}).get("languages", [])
            )
            if source_languages and target_languages and not (
                source_languages & target_languages
            ):
                errors.append(
                    f"relation has disjoint language scopes: "
                    f"{source_id} -> {target_id}"
                )
            if atom.get("verification_state") == "VERIFIED":
                if target.get("verification_state") not in {
                    "VERIFIED",
                    "EVIDENCED",
                }:
                    errors.append(
                        f"VERIFIED atom relation targets unsupported atom: "
                        f"{source_id} -> {target_id}"
                    )
    return errors
