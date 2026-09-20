import json
import re
from copy import deepcopy
from pathlib import Path

from jsonschema import Draft202012Validator
import pytest

from needle.analytics.dependency_ripple import (
    DependencyRippleError,
    build_dependency_ripple_view,
    render_dependency_ripple_text,
)


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


COMPOSITION = load(
    "fixtures/analytics/dependency-ripple-first-cohort-v0.1.json"
)
COMPOSITION_SCHEMA = load(
    "schemas/dependency-ripple-composition-v0.1.schema.json"
)
VIEW_SCHEMA = load("schemas/dependency-ripple-view-v0.1.schema.json")


def by_id(view):
    return {case["case_id"]:case for case in view["cases"]}


def materialize_case_files(tmp_path, composition):
    paths=set()
    for case in composition["cases"]:
        paths.update({
            case["continuity_fixture_path"],
            case["mutation_fixture_path"],
            case["semantic_fixture_path"],
        })
    for path in paths:
        source=Path(path)
        target=tmp_path / path
        target.parent.mkdir(parents=True,exist_ok=True)
        target.write_text(source.read_text(encoding="utf-8"),encoding="utf-8")


def test_dependency_ripple_composition_is_reference_only_and_valid():
    assert list(
        Draft202012Validator(COMPOSITION_SCHEMA).iter_errors(COMPOSITION)
    ) == []
    encoded=json.dumps(COMPOSITION,sort_keys=True)
    assert "sha256:" not in encoded
    assert re.search(r"\b\d{4}-\d{2}-\d{2}\b",encoded) is None
    assert "text_hash" not in encoded
    assert "statement" not in encoded


def test_first_legislative_xray_view_is_schema_valid():
    view=build_dependency_ripple_view(COMPOSITION)
    assert list(Draft202012Validator(VIEW_SCHEMA).iter_errors(view)) == []
    assert view["character"] == "DERIVED_VIEW"
    assert view["summary"] == {
        "case_count":2,
        "verified_upstream_mutation_count":2,
        "derived_local_effect_count":2,
        "local_textual_mutation_count":0,
    }


def test_article3_case_keeps_local_nonmutation_separate_from_upstream_replace():
    case=by_id(build_dependency_ripple_view(COMPOSITION))[
        "reg794-art3-p4-2025-channel-ripple"
    ]
    assert case["local_provision"] == "Article 3 > 4"
    assert case["local_continuity"]["before"]["text_hash"] == (
        case["local_continuity"]["after"]["text_hash"]
    )
    assert case["local_continuity"]["textual_mutation"] is None
    assert case["upstream_change"] == {
        "mutation_id":"reg794-article3-p3-2025-live-verified-v0.1",
        "operation":"REPLACE",
        "target":"Article 3 > 3",
        "verification_state":"VERIFIED",
    }
    assert case["derived_effect"]["atom_id"] == (
        "reg794-art3-2025-crossref-exception-ripple-v0.1"
    )


def test_reach_case_keeps_local_nonmutation_separate_from_annex_insert():
    case=by_id(build_dependency_ripple_view(COMPOSITION))[
        "reach-art67-annex17-entry78-ripple"
    ]
    assert case["local_provision"] == "Article 67 > 1"
    assert case["local_continuity"]["before"]["text_hash"] == (
        "72ffa37f50c709a28b4782909c438f5c82b769de702aee2f0c745729854faaee"
    )
    assert case["local_continuity"]["before"]["text_hash"] == (
        case["local_continuity"]["after"]["text_hash"]
    )
    assert case["upstream_change"] == {
        "mutation_id":"reach-annex17-entry78-2023-insert-v0.1",
        "operation":"INSERT",
        "target":"Annex XVII > entry 78",
        "verification_state":"VERIFIED",
    }
    assert "synthetic polymer microparticles" in (
        case["derived_effect"]["statement"].casefold()
    )


def test_every_xray_case_is_evidenced_derived_cross_reference():
    view=build_dependency_ripple_view(COMPOSITION)
    for case in view["cases"]:
        effect=case["derived_effect"]
        assert effect["verification_state"] == "EVIDENCED"
        assert effect["evidence_state"] == "DERIVED"
        assert "CROSS_REFERENCE" in effect["dimensions"]
        assert case["dependency"] == {
            "relation_character":"DERIVED_FROM_EVIDENCED_CROSS_REFERENCE_ATOM",
            "local_provision":case["local_provision"],
            "upstream_target":case["upstream_change"]["target"],
        }
        assert case["local_provision"] != case["upstream_change"]["target"]
        assert case["evidence_anchors"]


def test_changed_local_hash_fails_closed(tmp_path):
    composition=deepcopy(COMPOSITION)
    materialize_case_files(tmp_path,composition)
    case=next(
        item for item in composition["cases"]
        if item["case_id"] == "reach-art67-annex17-entry78-ripple"
    )
    path=tmp_path / case["continuity_fixture_path"]
    fixture=json.loads(path.read_text(encoding="utf-8"))
    fixture["local_continuity"]["after"]["text_hash"]="0"*64
    path.write_text(json.dumps(fixture),encoding="utf-8")

    with pytest.raises(
        DependencyRippleError,
        match="local continuity hashes differ",
    ):
        build_dependency_ripple_view(composition,root=tmp_path)


def test_wrong_upstream_mutation_link_fails_closed(tmp_path):
    composition=deepcopy(COMPOSITION)
    materialize_case_files(tmp_path,composition)
    case=next(
        item for item in composition["cases"]
        if item["case_id"] == "reach-art67-annex17-entry78-ripple"
    )
    path=tmp_path / case["semantic_fixture_path"]
    semantic=json.loads(path.read_text(encoding="utf-8"))
    semantic["atoms"][0]["source_mutation_ids"]=["wrong-mutation"]
    path.write_text(json.dumps(semantic),encoding="utf-8")

    with pytest.raises(
        DependencyRippleError,
        match="does not reference selected upstream mutation",
    ):
        build_dependency_ripple_view(composition,root=tmp_path)


def test_direct_or_verified_local_effect_is_not_a_silent_ripple(tmp_path):
    composition=deepcopy(COMPOSITION)
    materialize_case_files(tmp_path,composition)
    case=next(
        item for item in composition["cases"]
        if item["case_id"] == "reach-art67-annex17-entry78-ripple"
    )
    path=tmp_path / case["semantic_fixture_path"]
    semantic=json.loads(path.read_text(encoding="utf-8"))
    semantic["atoms"][0]["verification_state"]="VERIFIED"
    semantic["atoms"][0]["evidence_state"]="DIRECT"
    path.write_text(json.dumps(semantic),encoding="utf-8")

    with pytest.raises(
        DependencyRippleError,
        match="must be EVIDENCED",
    ):
        build_dependency_ripple_view(composition,root=tmp_path)


def test_local_target_equal_to_upstream_target_is_not_silent_dependency(tmp_path):
    composition=deepcopy(COMPOSITION)
    materialize_case_files(tmp_path,composition)
    case=next(
        item for item in composition["cases"]
        if item["case_id"] == "reach-art67-annex17-entry78-ripple"
    )
    path=tmp_path / case["semantic_fixture_path"]
    semantic=json.loads(path.read_text(encoding="utf-8"))
    semantic["atoms"][0]["provision_refs"][0]["citation_path"] = (
        "Annex XVII > entry 78"
    )
    path.write_text(json.dumps(semantic),encoding="utf-8")

    with pytest.raises(
        DependencyRippleError,
        match="not a silent dependency ripple",
    ):
        build_dependency_ripple_view(composition,root=tmp_path)


def test_xray_render_explains_direct_vs_derived_evidence():
    text=render_dependency_ripple_text(
        build_dependency_ripple_view(COMPOSITION)
    )
    assert "2 evidenced cases" in text
    assert "Article 3 > 4" in text
    assert "Article 67 > 1" in text
    assert "VERIFIED" in text
    assert "EVIDENCED / DERIVED" in text
    assert "No local textual mutation is manufactured" in text
    assert "derived view" in text
