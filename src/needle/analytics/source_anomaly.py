from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class SourceAnomalyError(ValueError):
    pass


def _read_json(root: Path, path: str) -> dict[str, Any]:
    return json.loads((root / path).read_text(encoding="utf-8"))


def _evidence(
    fixture: dict[str, Any],
    fixture_path: str,
) -> dict[str, Any]:
    observation=fixture.get("source_observation", {})
    artifact_hash=observation.get("artifact_hash")
    if not artifact_hash:
        raise SourceAnomalyError(
            f"{fixture_path}: source anomaly evidence lacks immutable artifact hash"
        )
    return {
        "fixture_path":fixture_path,
        "fixture_id":fixture["fixture_id"],
        "artifact_hash":artifact_hash,
    }


def _route_fallback_card(
    fixture: dict[str, Any],
    fixture_path: str,
) -> dict[str, Any]:
    route=fixture["source_route_observation"]
    observation=fixture["source_observation"]
    status=route.get("observed_http_status")
    if status is None or status < 400:
        raise SourceAnomalyError(
            f"{fixture_path}: route fallback anomaly requires failed preferred route"
        )
    if route.get("inference") != "ROUTE_UNAVAILABLE_NOT_SOURCE_ABSENT":
        raise SourceAnomalyError(
            f"{fixture_path}: unexpected route-fallback semantics"
        )

    fallbacks=[{
        "source_system":"EUR_LEX",
        "representation_class":observation["representation_class"],
        "resource_uri":observation["resource_uri"],
        "artifact_hash":observation["artifact_hash"],
    }]
    pdf=observation.get("corroborating_pdf")
    if pdf:
        fallbacks.append({
            "source_system":"OFFICIAL_JOURNAL",
            "representation_class":"OFFICIAL_PDF",
            "resource_uri":pdf["resource_uri"],
            "artifact_hash":pdf["artifact_hash"],
        })

    return {
        "anomaly_id":f"{fixture['fixture_id']}:route-fallback",
        "kind":"ROUTE_FALLBACK",
        "subject_identifier":fixture.get("corrigendum") or fixture.get("target_act"),
        "language":fixture.get("language"),
        "semantics":"ROUTE_UNAVAILABLE_NOT_SOURCE_ABSENT",
        "legal_mutation_inference":"NONE_FROM_SOURCE_ANOMALY_ALONE",
        "facts":{
            "preferred_route":{
                "source_system":"CELLAR",
                "resource_uri":route["preferred_cellar_celex_uri"],
                "observed_at":fixture.get("observed_at"),
                "http_status":status,
                "available":False,
            },
            "authoritative_fallbacks":fallbacks,
            "pinned_legal_evidence_available":True,
        },
        "evidence":_evidence(fixture,fixture_path),
        "non_implications":[
            "The legal source is not absent merely because the preferred route failed.",
            "The route failure is not a legal mutation.",
            "Fallback representations do not change the identity of the underlying legal resource.",
        ],
    }


def _source_internal_conflict_card(
    fixture: dict[str, Any],
    fixture_path: str,
) -> dict[str, Any]:
    conflict=fixture["source_internal_identifier_disagreement"]
    if conflict.get("conflict_state") != "SOURCE_INTERNAL_CONFLICT":
        raise SourceAnomalyError(
            f"{fixture_path}: identifier disagreement is not marked as conflict"
        )
    if (
        conflict.get("semantics")
        != "PRESERVE_LITERAL_AND_RESOLVE_CANONICAL_SEPARATELY"
    ):
        raise SourceAnomalyError(
            f"{fixture_path}: source-internal conflict semantics changed"
        )

    evidence=fixture["evidence"]
    literal=conflict["literal_article16"]
    canonical=conflict["resolved_canonical_predecessor"]
    if literal == canonical:
        raise SourceAnomalyError(
            f"{fixture_path}: source-internal conflict values unexpectedly equal"
        )
    support=evidence["canonical_predecessor_support"]
    if not support:
        raise SourceAnomalyError(
            f"{fixture_path}: canonical resolution lacks independent support"
        )

    return {
        "anomaly_id":f"{fixture['fixture_id']}:source-internal-conflict",
        "kind":"SOURCE_INTERNAL_CONFLICT",
        "subject_identifier":fixture["act"],
        "language":fixture.get("language"),
        "semantics":"PRESERVE_LITERAL_AND_RESOLVE_CANONICAL_SEPARATELY",
        "legal_mutation_inference":"NONE_FROM_SOURCE_ANOMALY_ALONE",
        "facts":{
            "literal":{
                "locator":evidence["repeal_clause"]["locator"],
                "value":literal,
            },
            "canonical_resolution":{
                "value":canonical,
                "independent_support":[
                    {"location":key, "value":value}
                    for key,value in sorted(support.items())
                ],
            },
            "conflict_state":"SOURCE_INTERNAL_CONFLICT",
        },
        "evidence":_evidence(fixture,fixture_path),
        "non_implications":[
            "Canonical resolution does not rewrite the authentic literal source text.",
            "The identifier disagreement alone does not establish a legal defect.",
            "Literal disagreement does not create a textual mutation in the regulated provision.",
        ],
    }


def _representation_duplication_card(
    fixture: dict[str, Any],
    fixture_path: str,
) -> dict[str, Any]:
    duplicate=fixture["representation_duplication"]
    occurrences=duplicate.get("occurrences", [])
    if len(occurrences) < 2:
        raise SourceAnomalyError(
            f"{fixture_path}: representation duplication requires multiple occurrences"
        )
    if duplicate.get("unique_evidence_value_count") != 1:
        raise SourceAnomalyError(
            f"{fixture_path}: duplicate representation has conflicting evidence values"
        )
    if (
        duplicate.get("semantics")
        != "REPRESENTATION_DUPLICATION_NOT_CORROBORATION"
    ):
        raise SourceAnomalyError(
            f"{fixture_path}: representation-duplication semantics changed"
        )
    canonical=duplicate["canonical_occurrence_locator"]
    locators=[item["locator"] for item in occurrences]
    if canonical not in locators:
        raise SourceAnomalyError(
            f"{fixture_path}: canonical occurrence is not one of observed duplicates"
        )

    return {
        "anomaly_id":f"{fixture['fixture_id']}:representation-duplication",
        "kind":"REPRESENTATION_DUPLICATION",
        "subject_identifier":fixture["subject_identifier"],
        "language":fixture.get("language"),
        "semantics":"REPRESENTATION_DUPLICATION_NOT_CORROBORATION",
        "legal_mutation_inference":"NONE_FROM_SOURCE_ANOMALY_ALONE",
        "facts":{
            "semantic_key":duplicate["semantic_key"],
            "normalized_value":duplicate["normalized_value"],
            "source_native_value":duplicate["source_native_value"],
            "occurrence_count":len(occurrences),
            "unique_evidence_value_count":1,
            "canonical_occurrence_locator":canonical,
            "occurrence_locators":locators,
            "text_hash":duplicate["text_hash"],
        },
        "evidence":_evidence(fixture,fixture_path),
        "non_implications":[
            "Repeated identical metadata is not independent corroboration.",
            "Duplicate occurrences do not multiply evidentiary weight.",
            "Selecting one deterministic citation locator does not erase the other observed occurrence.",
            "Representation duplication is not a legal mutation.",
        ],
    }


def build_source_anomaly_view(
    composition: dict[str, Any],
    *,
    root: Path | str = Path("."),
) -> dict[str, Any]:
    """Build categorical source-anomaly cards from pinned audit evidence."""
    root=Path(root)
    if composition.get("composition_character") != "REFERENCE_ONLY":
        raise SourceAnomalyError(
            "Source Anomaly composition must be REFERENCE_ONLY"
        )

    cards=[]
    for fixture_path in composition["evidence_fixture_paths"]:
        fixture=_read_json(root,fixture_path)
        matched=False

        if "source_route_observation" in fixture:
            cards.append(_route_fallback_card(fixture,fixture_path))
            matched=True
        if "source_internal_identifier_disagreement" in fixture:
            cards.append(
                _source_internal_conflict_card(fixture,fixture_path)
            )
            matched=True
        if "representation_duplication" in fixture:
            cards.append(
                _representation_duplication_card(fixture,fixture_path)
            )
            matched=True

        if not matched:
            raise SourceAnomalyError(
                f"{fixture_path}: no supported source-anomaly shape"
            )

    cards.sort(key=lambda card:(card["kind"],card["anomaly_id"]))
    kind_counts={}
    for card in cards:
        kind_counts[card["kind"]]=kind_counts.get(card["kind"],0)+1

    return {
        "schema_version":"source-anomaly-view-v0.1",
        "analytic_id":composition["analytic_id"],
        "character":"DERIVED_VIEW",
        "cards":cards,
        "summary":{
            "card_count":len(cards),
            "kind_counts":dict(sorted(kind_counts.items())),
        },
        "guardrails":list(composition["guardrails"]),
    }


def render_source_anomaly_text(view: dict[str, Any]) -> str:
    lines=[
        "Morrow // Needle — Source Anomaly",
        "",
        "3 seconds",
        (
            f"{view['summary']['card_count']} pinned source-layer anomalies are "
            "visible without treating source infrastructure oddities as legal changes."
        ),
        "",
        "30 seconds",
    ]
    for card in view["cards"]:
        if card["kind"] == "ROUTE_FALLBACK":
            preferred=card["facts"]["preferred_route"]
            lines.append(
                f"- {card['subject_identifier']}: preferred "
                f"{preferred['source_system']} route was observed returning HTTP "
                f"{preferred['http_status']}"
                + (
                    f" at {preferred['observed_at']}"
                    if preferred.get("observed_at") else ""
                )
                + ", while "
                f"{len(card['facts']['authoritative_fallbacks'])} pinned "
                "authoritative fallback representation(s) remained available."
            )
        elif card["kind"] == "SOURCE_INTERNAL_CONFLICT":
            facts=card["facts"]
            lines.append(
                f"- {card['subject_identifier']}: authentic source text prints "
                f"{facts['literal']['value']}, while independent in-act evidence "
                f"supports canonical resolution to "
                f"{facts['canonical_resolution']['value']}; both are preserved."
            )
        elif card["kind"] == "REPRESENTATION_DUPLICATION":
            facts=card["facts"]
            lines.append(
                f"- {card['subject_identifier']}: {facts['semantic_key']} occurs "
                f"{facts['occurrence_count']} times across one representation "
                "with one unique evidentiary value; duplicates are not counted "
                "as corroboration."
            )

    lines.extend([
        "",
        "Evidence model",
        "- Cards are derived from pinned audit/source observations.",
        "- Source anomalies alone emit no legal-mutation inference.",
        "- Literal official text remains immutable even when canonical identity resolution differs.",
        "- Endpoint availability is source state, not legal state.",
    ])
    return "\n".join(lines)+"\n"
