import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

from jsonschema import Draft202012Validator
import pytest

from needle.updates.cellar_feed import FeedPage, dedupe_events, parse_feed
from needle.updates.classify import (
    classify_source_change,
    refresh_scope,
    snapshot_from_observations,
)
from needle.updates.cursor import PollCursor, accept_page, begin_window


SCHEMA = json.loads(
    Path("schemas/cellar-ingestion-event-v0.1.schema.json").read_text(encoding="utf-8")
)
RSS = Path(
    "fixtures/updates/cellar-official-doc-example-7081775-v0.1.xml"
).read_bytes()


def _event(event_id, when="2026-09-20T10:00:00+00:00"):
    return {
        "notification_id":str(event_id),
        "action":"UPDATE",
        "cellar_id":f"cellar:target-{event_id}",
        "root_cellar_id":"cellar:root",
        "ingestion_time":when,
        "priority":"DAILY",
        "classes":["http://publications.europa.eu/ontology/cdm#work"],
        "wemi_levels":["WORK"],
        "identifiers":[f"celex:{event_id}"],
        "feed_observation":{
            "channel":"ingestion",
            "format":"RSS",
            "window_start":"2026-09-20T09:55:00+00:00",
            "window_end":"2026-09-20T10:05:00+00:00",
            "page":1,
            "entry_ordinal":0,
        },
    }


def _obs(record_id, artifact_hash):
    return {
        "record_id":record_id,
        "record_type":"SOURCE_OBSERVATION",
        "payload":{"artifact_hash":artifact_hash},
    }


def test_official_documented_feed_example_parses_and_validates():
    page = parse_feed(RSS)
    assert page.format == "RSS"
    assert page.page == 1
    assert page.more_entries is False
    assert len(page.events) == 1

    event = page.events[0]
    assert event["notification_id"] == "7081775"
    assert event["action"] == "UPDATE"
    assert event["cellar_id"] == (
        "cellar:ca753ae9-cf80-11e2-859e-01aa75ed71a1"
    )
    assert event["root_cellar_id"] == event["cellar_id"]
    assert event["wemi_levels"] == ["WORK"]
    assert "celex:32006D0241" in event["identifiers"]
    assert event["ingestion_time"] == "2012-06-11T09:13:58+01:00"

    assert list(Draft202012Validator(SCHEMA).iter_errors(event)) == []


def test_overlap_replay_is_idempotent_by_permanent_notification_id():
    first, seen = dedupe_events([_event("1"), _event("2")], set())
    assert [event["notification_id"] for event in first] == ["1","2"]

    replay, seen = dedupe_events(
        [_event("2"), _event("3")],
        seen,
    )
    assert [event["notification_id"] for event in replay] == ["3"]
    assert seen == {"1","2","3"}


def test_same_ingestion_timestamp_does_not_drop_distinct_events():
    same = "2026-09-20T10:00:00+00:00"
    emitted, seen = dedupe_events(
        [_event("101",same), _event("102",same)],
        set(),
    )
    assert [event["notification_id"] for event in emitted] == ["101","102"]
    assert seen == {"101","102"}


def test_cursor_advances_only_after_complete_paginated_window():
    cursor = begin_window(
        PollCursor(last_completed_end="2026-09-20T09:00:00+00:00"),
        window_start="2026-09-20T08:55:00+00:00",
        window_end="2026-09-20T10:00:00+00:00",
    )
    page1 = FeedPage(
        window_start="2026-09-20T10:55:00+02:00",
        window_end="2026-09-20T12:00:00+02:00",
        page=1,
        more_entries=True,
        format="RSS",
        events=(),
    )
    cursor = accept_page(cursor,page1)
    assert cursor.last_completed_end == "2026-09-20T09:00:00+00:00"
    assert cursor.next_page == 2
    assert cursor.active_window_end == "2026-09-20T10:00:00+00:00"

    page2 = FeedPage(
        window_start="2026-09-20T08:55:00+00:00",
        window_end="2026-09-20T10:00:00+00:00",
        page=2,
        more_entries=False,
        format="RSS",
        events=(),
    )
    cursor = accept_page(cursor,page2)
    assert cursor.last_completed_end == "2026-09-20T10:00:00+00:00"
    assert cursor.active_window_start is None
    assert cursor.next_page == 1


def test_cursor_rejects_skipped_page():
    cursor = begin_window(
        PollCursor(),
        window_start="2026-09-20T09:00:00+00:00",
        window_end="2026-09-20T10:00:00+00:00",
    )
    bad = FeedPage(
        window_start="2026-09-20T09:00:00+00:00",
        window_end="2026-09-20T10:00:00+00:00",
        page=2,
        more_entries=False,
        format="RSS",
        events=(),
    )
    with pytest.raises(ValueError,match="expected page 1"):
        accept_page(cursor,bad)


@pytest.mark.parametrize(
    ("action","previous","current","expected"),
    [
        (
            "CREATE",None,
            {"available":True,"content_hash":"c1","metadata_hash":"m1"},
            "SOURCE_CREATED",
        ),
        (
            "UPDATE",
            {"available":True,"content_hash":"c1","metadata_hash":"m1"},
            {"available":True,"content_hash":"c1","metadata_hash":"m1"},
            "NO_MATERIAL_CHANGE",
        ),
        (
            "UPDATE",
            {"available":True,"content_hash":"c1","metadata_hash":"m1"},
            {"available":True,"content_hash":"c1","metadata_hash":"m2"},
            "METADATA_ONLY",
        ),
        (
            "UPDATE",
            {"available":True,"content_hash":"c1","metadata_hash":"m1"},
            {"available":True,"content_hash":"c2","metadata_hash":"m1"},
            "CONTENT_CHANGED",
        ),
        (
            "UPDATE",
            {"available":True,"content_hash":"c1","metadata_hash":"m1"},
            {"available":False,"content_hash":"c1","metadata_hash":"m1"},
            "AVAILABILITY_CHANGED",
        ),
        (
            "DELETE",
            {"available":True,"content_hash":"c1","metadata_hash":"m1"},
            None,
            "AVAILABILITY_CHANGED",
        ),
        (
            "UPDATE",None,
            {"available":True,"content_hash":"c1","metadata_hash":"m1"},
            "UNRESOLVED",
        ),
    ],
)
def test_reobservation_not_feed_action_classifies_material_change(
    action, previous, current, expected
):
    assert classify_source_change(
        action=action,
        previous=previous,
        current=current,
    ) == expected


def test_metadata_and_content_are_separate_provenance_observations():
    content = _obs("src-content","sha256:" + ("a"*64))
    metadata = _obs("src-metadata","sha256:" + ("b"*64))
    snapshot = snapshot_from_observations(
        content_observation=content,
        metadata_observation=metadata,
        available=True,
    )
    assert snapshot == {
        "available":True,
        "content_hash":"sha256:" + ("a"*64),
        "metadata_hash":"sha256:" + ("b"*64),
        "content_observation_id":"src-content",
        "metadata_observation_id":"src-metadata",
    }


def test_refresh_scope_respects_wemi_level():
    manifestation = _event("m")
    manifestation["wemi_levels"] = ["MANIFESTATION"]
    assert refresh_scope(manifestation)["scope"] == "MANIFESTATION"

    item = _event("i")
    item["wemi_levels"] = ["ITEM"]
    assert refresh_scope(item)["scope"] == "ITEM_AND_PARENT_MANIFESTATION"

    work = _event("w")
    work["wemi_levels"] = ["WORK"]
    assert refresh_scope(work)["scope"] == "WORK"
