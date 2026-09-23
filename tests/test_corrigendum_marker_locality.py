import json
from collections import defaultdict
from pathlib import Path


FIXTURE=json.loads(
    Path("fixtures/audit/reg794-2025-corrigendum-marker-locality-v0.1.json").read_text(
        encoding="utf-8"
    )
)


def test_same_corrigendum_has_different_expression_local_markers():
    target="CELEX:32025R0905R(01)"
    markers={
        item["marker"]
        for item in FIXTURE["observations"]
        if item["corrigendum_identifier"] == target
    }
    assert markers == {"C2","C4","C5","C6"}


def test_same_marker_can_point_to_different_corrigenda():
    by_marker=defaultdict(set)
    for item in FIXTURE["observations"]:
        by_marker[item["marker"]].add(item["corrigendum_identifier"])

    assert "C4" in by_marker
    assert "CELEX:32025R0905R(01)" in by_marker["C4"]
    assert "CORRIGENDUM:REG271-2008:2009-11-17" in by_marker["C4"]
    assert len(by_marker["C4"]) >= 2


def test_cross_expression_identity_uses_official_source_identity_not_marker():
    finding=FIXTURE["finding"]
    assert finding["marker_semantics"] == "EXPRESSION_LOCAL_PRESENTATION_ORDINAL"
    assert (
        finding["canonical_cross_expression_key"]
        == "OFFICIAL_CORRIGENDUM_IDENTITY_OR_SOURCE_RELATIONSHIP"
    )


def test_fixture_records_preventive_regression_not_known_code_defect():
    assert FIXTURE["finding"]["current_code_defect_observed"] is False
    assert (
        FIXTURE["finding"]["disposition"]
        == "PREVENTIVE_SOURCE_REPRESENTATION_REGRESSION"
    )


def test_marker_only_cross_language_join_is_explicitly_forbidden():
    forbidden=" ".join(FIXTURE["forbidden_inferences"])
    assert "same corrigendum as C4 in every other language" in forbidden
    assert "C-label alone is sufficient evidence" in forbidden
    assert "replace CELEX, ELI, OJ citation" in forbidden
