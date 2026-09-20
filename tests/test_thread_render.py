import json
from pathlib import Path

from needle.thread.render import render_article3_preview, render_preview_text


THREAD = json.loads(
    Path("fixtures/thread/reg794-article3-thread-v0.1.json").read_text(
        encoding="utf-8"
    )
)


def preview():
    return render_article3_preview(THREAD)


def test_public_preview_requires_and_reports_closed_source_mode():
    result = preview()
    assert result["source_mode"] == {"closed":True, "gap_count":0}


def test_public_preview_contains_all_three_requested_layers():
    result = preview()
    assert set(result["layers"]) == {"3_seconds", "30_seconds", "3_minutes"}
    assert result["layers"]["3_seconds"]["text"]
    assert len(result["layers"]["30_seconds"]) >= 4
    assert len(result["layers"]["3_minutes"]) >= 7


def test_every_substantive_preview_item_has_refs_and_provenance_evidence():
    result = preview()
    items = [
        result["layers"]["3_seconds"],
        *result["layers"]["30_seconds"],
        *result["layers"]["3_minutes"],
    ]
    for item in items:
        assert item["refs"], item["text"]
        assert item["evidence"], item["text"]
        assert all(evidence["support_record_id"] for evidence in item["evidence"])
        assert all(evidence["source_observation_id"] for evidence in item["evidence"])
        assert all(evidence["locator"] for evidence in item["evidence"])


def test_public_preview_preserves_sani_pki_scope_separation():
    result = preview()
    second = result["layers"]["30_seconds"][1]
    assert "SANI" in second["text"]
    assert "Public Key Infrastructure (PKI)" in second["text"]
    assert {
        ref["entity_id"] for ref in second["refs"]
    } == {
        "reg794-art3-sani-duty-v0.1",
        "reg794-art3-pki-correspondence-duty-v0.1",
    }


def test_public_preview_calls_2025_paragraph4_effect_derived_not_textual():
    result = preview()
    item = result["layers"]["30_seconds"][4]
    assert item["character"] == "DERIVED_WITH_NEGATIVE_TEXTUAL_CHECK"
    assert "was not textually changed in 2025" in item["text"]
    assert {
        ref["kind"] for ref in item["refs"]
    } == {"CHANGE_ATOM", "THREAD_EVIDENCE"}


def test_public_preview_keeps_corrigendum_out_of_article3_mutation_timeline():
    result = preview()
    item = result["layers"]["3_minutes"][-1]
    assert item["event_id"] == "corrigendum-review-2026"
    assert "excluded from the Article 3 mutation timeline" in item["text"]
    assert item["refs"] == [{
        "kind":"THREAD_EVIDENCE",
        "entity_id":"reg794-article3-corrigendum-scope-v0.1",
    }]


def test_plain_text_preview_is_generated_from_public_json():
    result = preview()
    text = render_preview_text(result)
    assert "3 seconds" in text
    assert "30 seconds" in text
    assert "3 minutes" in text
    assert result["layers"]["3_seconds"]["text"] in text
    assert "Source Mode closed" in text
