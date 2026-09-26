import json
from datetime import date
from pathlib import Path

from scripts.render_harmonised_standard_status import render_card


TOY = json.loads(
    Path("fixtures/dependency/toy-safety-authoritative-dynamic-set-v0.1.json").read_text(
        encoding="utf-8"
    )
)
GAR = json.loads(
    Path("fixtures/dependency/gar-en497-authoritative-dynamic-set-v0.1.json").read_text(
        encoding="utf-8"
    )
)
LVD_WITHDRAWAL = json.loads(
    Path(
        "fixtures/dependency/lvd-en60335-2-60-scheduled-withdrawal-v0.1.json"
    ).read_text(encoding="utf-8")
)


def test_toy_status_changes_from_cited_to_restricted():
    before = render_card(TOY, "EN 71-1:2014+A1:2018", date(2025, 9, 9))
    after = render_card(TOY, "EN 71-1:2014+A1:2018", date(2025, 9, 10))

    assert "**OJ-reference state:** CITED" in before
    assert "**Presumption consequence:** AVAILABLE_WITHIN_COVERED_SCOPE" in before
    assert "**OJ-reference state:** CITED_WITH_RESTRICTION" in after
    assert "**Presumption consequence:** RESTRICTED_TO_STATED_SCOPE" in after
    assert "wave rollers" in after


def test_gar_status_remains_not_cited_but_reason_changes():
    before = render_card(GAR, "EN 497:2022", date(2026, 7, 23))
    after = render_card(GAR, "EN 497:2022", date(2026, 7, 24))

    assert "**OJ-reference state:** NOT_CITED" in before
    assert "**OJ-reference state:** NOT_CITED" in after
    assert "none in this record before the query date" in before
    assert "gar-en497-formal-nonpublication-2026-07-24" in after
    assert "formally decides not to publish" in after


def test_no_presumption_does_not_become_standard_prohibition():
    card = render_card(GAR, "EN 497:2022", date(2026, 9, 26))

    assert "alternative conformity route" in card
    assert "standards organisation" in card
    assert "NOT_AVAILABLE_VIA_THIS_OJ_REFERENCE" in card


def test_card_exposes_scheduled_future_withdrawal_before_it_takes_effect():
    card = render_card(
        LVD_WITHDRAWAL,
        "EN 60335-2-60:2003",
        date(2026, 9, 26),
    )

    assert "**OJ-reference state:** CITED" in card
    assert "Next scheduled owning event" in card
    assert "effective 2027-01-18" in card
    assert "schedules withdrawal" in card


def test_card_applies_withdrawal_after_effective_date():
    card = render_card(
        LVD_WITHDRAWAL,
        "EN 60335-2-60:2003",
        date(2027, 1, 18),
    )

    assert "**OJ-reference state:** NOT_CITED" in card
    assert "**Presumption consequence:** NOT_AVAILABLE_VIA_THIS_OJ_REFERENCE" in card
    assert "lvd-en60335-2-60-withdrawal-2027-01-18" in card
