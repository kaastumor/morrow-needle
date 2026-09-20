import json
import re
from copy import deepcopy
from pathlib import Path

from jsonschema import Draft202012Validator
import pytest

from needle.analytics.source_anomaly import (
    SourceAnomalyError,
    build_source_anomaly_view,
    render_source_anomaly_text,
)


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


COMPOSITION = load(
    "fixtures/analytics/source-anomaly-first-cohort-v0.1.json"
)
COMPOSITION_SCHEMA = load(
    "schemas/source-anomaly-composition-v0.1.schema.json"
)
VIEW_SCHEMA = load("schemas/source-anomaly-view-v0.1.schema.json")


def by_kind(view):
    return {card["kind"]:card for card in view["cards"]}


def _materialize_inputs(tmp_path, composition=COMPOSITION):
    for fixture_path in composition["evidence_fixture_paths"]:
        source=Path(fixture_path)
        target=tmp_path / fixture_path
        target.parent.mkdir(parents=True,exist_ok=True)
        target.write_text(source.read_text(encoding="utf-8"),encoding="utf-8")


def test_source_anomaly_composition_is_reference_only_and_valid():
    assert list(
        Draft202012Validator(COMPOSITION_SCHEMA).iter_errors(COMPOSITION)
    ) == []
    encoded=json.dumps(COMPOSITION,sort_keys=True)
    assert "sha256:" not in encoded
    assert "http_status" not in encoded
    assert re.search(r"https?://",encoded) is None


def test_first_source_anomaly_view_is_schema_valid_and_categorical():
    view=build_source_anomaly_view(COMPOSITION)
    assert list(Draft202012Validator(VIEW_SCHEMA).iter_errors(view)) == []
    assert view["character"] == "DERIVED_VIEW"
    assert view["summary"] == {
        "card_count":3,
        "kind_counts":{
            "REPRESENTATION_DUPLICATION":1,
            "ROUTE_FALLBACK":1,
            "SOURCE_INTERNAL_CONFLICT":1,
        },
    }
    assert set(by_kind(view)) == {
        "ROUTE_FALLBACK",
        "SOURCE_INTERNAL_CONFLICT",
        "REPRESENTATION_DUPLICATION",
    }


def test_route_failure_is_not_rendered_as_source_or_law_absence():
    card=by_kind(build_source_anomaly_view(COMPOSITION))["ROUTE_FALLBACK"]
    assert card["subject_identifier"] == "CELEX:31990R2742R(01)"
    assert card["semantics"] == "ROUTE_UNAVAILABLE_NOT_SOURCE_ABSENT"
    assert card["facts"]["preferred_route"]["http_status"] == 404
    assert card["facts"]["preferred_route"]["available"] is False
    assert card["facts"]["pinned_legal_evidence_available"] is True
    assert len(card["facts"]["authoritative_fallbacks"]) == 2
    assert {
        item["source_system"]
        for item in card["facts"]["authoritative_fallbacks"]
    } == {"EUR_LEX","OFFICIAL_JOURNAL"}
    assert card["legal_mutation_inference"] == (
        "NONE_FROM_SOURCE_ANOMALY_ALONE"
    )


def test_internal_identifier_conflict_preserves_literal_and_canonical_values():
    card=by_kind(
        build_source_anomaly_view(COMPOSITION)
    )["SOURCE_INTERNAL_CONFLICT"]
    assert card["subject_identifier"] == "CELEX:32008L0007"
    assert card["facts"]["literal"] == {
        "locator":"Article 16",
        "value":"69/355/EEC",
    }
    assert card["facts"]["canonical_resolution"]["value"] == "69/335/EEC"
    assert len(
        card["facts"]["canonical_resolution"]["independent_support"]
    ) == 3
    assert card["semantics"] == (
        "PRESERVE_LITERAL_AND_RESOLVE_CANONICAL_SEPARATELY"
    )


def test_duplicate_representation_has_one_evidentiary_value_not_two():
    card=by_kind(
        build_source_anomaly_view(COMPOSITION)
    )["REPRESENTATION_DUPLICATION"]
    facts=card["facts"]
    assert card["subject_identifier"] == "CELEX:32025R0905"
    assert facts["semantic_key"] == "PUBLICATION_DATE"
    assert facts["normalized_value"] == "2025-06-13"
    assert facts["occurrence_count"] == 2
    assert facts["unique_evidence_value_count"] == 1
    assert facts["canonical_occurrence_locator"] in facts[
        "occurrence_locators"
    ]
    assert len(facts["occurrence_locators"]) == 2


def test_conflicting_duplicate_values_fail_closed(tmp_path):
    composition=deepcopy(COMPOSITION)
    _materialize_inputs(tmp_path,composition)

    path=(
        tmp_path
        / "fixtures/audit/reg905-2025-formex-publication-duplication-v0.1.json"
    )
    duplicate=json.loads(path.read_text(encoding="utf-8"))
    duplicate["representation_duplication"]["unique_evidence_value_count"]=2
    path.write_text(json.dumps(duplicate),encoding="utf-8")

    with pytest.raises(
        SourceAnomalyError,
        match="conflicting evidence values",
    ):
        build_source_anomaly_view(composition,root=tmp_path)


def test_selected_fixture_without_supported_anomaly_shape_fails_closed(tmp_path):
    composition=deepcopy(COMPOSITION)
    composition["evidence_fixture_paths"]=["fixtures/audit/empty.json"]
    path=tmp_path / "fixtures/audit/empty.json"
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(
        json.dumps({
            "fixture_id":"empty-audit",
            "source_observation":{
                "artifact_hash":"sha256:"+"a"*64
            },
        }),
        encoding="utf-8",
    )
    with pytest.raises(
        SourceAnomalyError,
        match="no supported source-anomaly shape",
    ):
        build_source_anomaly_view(composition,root=tmp_path)


def test_public_render_is_factual_and_keeps_source_vs_legal_state_separate():
    text=render_source_anomaly_text(
        build_source_anomaly_view(COMPOSITION)
    )
    assert "HTTP 404" in text
    assert "69/355/EEC" in text
    assert "69/335/EEC" in text
    assert "duplicates are not counted as corroboration" in text
    assert "Source anomalies alone emit no legal-mutation inference" in text
    assert "Endpoint availability is source state, not legal state" in text


def test_all_cards_retain_immutable_evidence_anchor():
    view=build_source_anomaly_view(COMPOSITION)
    for card in view["cards"]:
        assert card["evidence"]["fixture_path"].startswith("fixtures/audit/")
        assert card["evidence"]["fixture_id"]
        assert card["evidence"]["artifact_hash"].startswith("sha256:")
        assert len(card["evidence"]["artifact_hash"]) == 71
