import json
from pathlib import Path


FIXTURE=json.loads(
    Path("fixtures/audit/reg794-2025-corrigendum-backprojection-v0.1.json").read_text(
        encoding="utf-8"
    )
)
OLDER=json.loads(
    Path("fixtures/multilingual/reg794-2004-consolidation-backprojection-v0.1.json").read_text(
        encoding="utf-8"
    )
)


def observations():
    return {item["observation_id"]:item for item in FIXTURE["observations"]}


def test_2026_corrigendum_lexically_bridges_original_and_current_consolidation():
    obs=observations()
    original=obs["obs-amending-act-2025-905-original-wording"]
    correction=obs["obs-corrigendum-2026-90591"]
    current=obs["obs-current-consolidation-2025-08-13-observed-2026"]

    assert original["observed_text"] == correction["replaces_text"]
    assert current["observed_text"] == correction["corrected_text"]
    assert current["observed_text"] != original["observed_text"]
    assert "aid scheme" not in original["observed_text"]
    assert "aid scheme" in current["observed_text"]


def test_current_consolidation_label_predates_correction_source():
    obs=observations()
    correction=obs["obs-corrigendum-2026-90591"]
    current=obs["obs-current-consolidation-2025-08-13-observed-2026"]

    assert current["text_state_label_date"] == "2025-08-13"
    assert correction["source_date"] == "2026-07-17"
    assert current["text_state_label_date"] < correction["source_date"]
    assert FIXTURE["temporal_result"]["ordering"] == (
        "CONSOLIDATION_LABEL_PRECEDES_CORRIGENDUM_PUBLICATION"
    )


def test_current_ex_post_consolidation_cannot_prove_2025_source_state():
    temporal=FIXTURE["temporal_result"]

    assert (
        temporal["OFFICIAL_SOURCE_STATE_AS_OF_2025_08_13"]
        == "UNRESOLVED_FROM_CURRENT_CONSOLIDATION_ALONE"
    )
    assert "corrected wording" in temporal["EX_POST_LEGAL_EFFECT"]

    forbidden=" ".join(FIXTURE["forbidden_inferences"])
    assert "publicly visible on 2025-08-13" in forbidden
    assert "source-state-as-of archive" in forbidden


def test_case_is_independent_confirmation_not_new_corrigendum_semantics():
    assert "Independent real-world confirmation" in FIXTURE["finding"]
    assert OLDER["text_state_label_date"] == "2004-05-20"
    assert FIXTURE["temporal_result"]["consolidation_label_date"] == "2025-08-13"

    older_later_dates={
        source["source_date"]
        for expression in OLDER["observed_expressions"]
        for source in expression["supporting_later_sources"]
    }
    assert min(older_later_dates) > OLDER["text_state_label_date"]
    assert (
        FIXTURE["temporal_result"]["corrigendum_source_date"]
        > FIXTURE["temporal_result"]["consolidation_label_date"]
    )


def test_fixture_does_not_generalize_backprojection_beyond_observed_case():
    forbidden=" ".join(FIXTURE["forbidden_inferences"])
    assert "Every correction is back-projected" in forbidden
    assert FIXTURE["language"] == "ENG"
