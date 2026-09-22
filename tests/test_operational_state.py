import json
from copy import deepcopy
from pathlib import Path

from jsonschema import Draft202012Validator

from needle.operations.state import (
    advance_baseline,
    baseline_key,
    baseline_seed_eligible,
    lookup_baseline,
    record_reobservation,
    retain_overlap_event_keys,
    validate_operational_state,
)
from needle.provenance.ledger import verify_record_hash


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


STATE=load("data/operational-pilot-state-v0.1.json")
STATE_SCHEMA=load("schemas/operational-state-v0.1.schema.json")
PROVENANCE_SCHEMA=load("schemas/provenance-record-v0.1.schema.json")


def event(
    *,
    celex="32019R0632",
    root="cellar:e26bdaad-6759-11e9-9f05-01aa75ed71a1",
    ingestion_time="2026-09-21T08:00:00+00:00",
    event_key="future-event",
):
    return {
        "event_key":event_key,
        "notification_id":event_key,
        "notification_id_basis":"RSS_GUID",
        "raw_feed_id":event_key,
        "action":"UPDATE",
        "cellar_id":root,
        "root_cellar_id":root,
        "ingestion_time":ingestion_time,
        "priority":"DAILY",
        "classes":[],
        "wemi_levels":["WORK"],
        "identifiers":[f"celex:{celex}"],
        "feed_observation":{
            "channel":"ingestion",
            "format":"RSS",
            "window_start":None,
            "window_end":None,
            "page":1,
            "entry_ordinal":0,
        },
    }


def current_baseline():
    return next(
        item for item in STATE["baselines"]
        if item["baseline_key"] == "CELEX:32019R0632|ENG"
    )


def observation(record_id):
    return next(
        record for record in STATE["source_observations"]
        if record["record_id"] == record_id
    )


def test_live_state_and_embedded_provenance_validate_without_freezing_cache_size():
    """The checked-in pilot state is mutable operational cache, not a fixture.

    Monitor cycles are expected to add baselines and immutable observations. Tests
    therefore validate invariants rather than pinning counts or historical record
    ids that a successful production run is designed to change.
    """
    assert list(
        Draft202012Validator(STATE_SCHEMA).iter_errors(STATE)
    ) == []
    assert validate_operational_state(STATE) == []
    assert STATE["baselines"]
    assert STATE["source_observations"]
    for record in STATE["source_observations"]:
        assert verify_record_hash(record)
        assert list(
            Draft202012Validator(PROVENANCE_SCHEMA).iter_errors(record)
        ) == []


def test_seed_baseline_key_is_canonical_identifier_plus_language():
    assert baseline_key("celex:32019r0632","eng") == (
        "CELEX:32019R0632|ENG"
    )


def test_cold_start_seed_cannot_retroactively_solve_prior_update():
    prior=event(
        ingestion_time="2026-09-19T08:02:40.099+02:00",
        event_key=(
            "cellar:e26bdaad-6759-11e9-9f05-01aa75ed71a1_"
            "2026-09-19T08:02:40.099+02:00"
        ),
    )
    lookup=lookup_baseline(STATE,prior)
    assert lookup["state"] == "BASELINE_NOT_PRIOR"
    assert lookup["snapshot"] is None
    assert "cannot be used retroactively" in lookup["reason"]


def test_later_event_gets_current_complete_prior_snapshot():
    later=event()
    lookup=lookup_baseline(STATE,later)
    assert lookup["state"] == "ELIGIBLE"
    current=current_baseline()
    assert lookup["snapshot"] == {
        "available":True,
        "content_hash":observation(
            current["content_observation_id"]
        )["payload"]["artifact_hash"],
        "metadata_hash":observation(
            current["metadata_observation_id"]
        )["payload"]["artifact_hash"],
        "content_observation_id":current["content_observation_id"],
        "metadata_observation_id":current["metadata_observation_id"],
    }


def test_unknown_celex_has_no_baseline():
    lookup=lookup_baseline(
        STATE,
        event(
            celex="32026R9999",
            root="cellar:new",
        ),
    )
    assert lookup["state"] == "MISSING_BASELINE"
    assert lookup["snapshot"] is None


def test_advance_baseline_appends_observations_and_moves_pointer():
    later=event()
    prior=current_baseline()
    content=deepcopy(observation(prior["content_observation_id"]))
    metadata=deepcopy(observation(prior["metadata_observation_id"]))
    content["record_id"]="src-operational-content-next"
    metadata["record_id"]="src-operational-metadata-next"
    for record in (content,metadata):
        record["created_at"]="2026-09-21T08:01:00+00:00"
        record["payload"]["observed_at"]="2026-09-21T08:01:00+00:00"
        record["record_hash"]=None
    from needle.provenance.ledger import seal_record
    content=seal_record(content)
    metadata=seal_record(metadata)
    reobservation={
        "snapshot":{
            "available":True,
            "content_hash":content["payload"]["artifact_hash"],
            "metadata_hash":metadata["payload"]["artifact_hash"],
            "content_observation_id":content["record_id"],
            "metadata_observation_id":metadata["record_id"],
        },
        "content_observation":content,
        "metadata_observation":metadata,
    }
    advanced=advance_baseline(
        STATE,later,reobservation,
        updated_at="2026-09-21T08:01:00+00:00",
        seed_character="POST_EVENT_REFRESH",
    )
    moved=next(
        item for item in advanced["baselines"]
        if item["baseline_key"] == "CELEX:32019R0632|ENG"
    )
    assert moved["content_observation_id"] == content["record_id"]
    assert moved["metadata_observation_id"] == metadata["record_id"]
    assert later["event_key"] in advanced["processed_event_keys"]
    assert observation(prior["content_observation_id"])


def test_partial_observation_cannot_replace_complete_comparator_baseline():
    partial_content={
        "state":"PARTIAL_OBSERVATION",
        "snapshot":{
            "available":True,
            "content_hash":"sha256:content",
            "metadata_hash":None,
            "content_observation_id":"src-content",
            "metadata_observation_id":None,
        },
    }
    partial_metadata={
        "state":"PARTIAL_OBSERVATION",
        "snapshot":{
            "available":True,
            "content_hash":None,
            "metadata_hash":"sha256:metadata",
            "content_observation_id":None,
            "metadata_observation_id":"src-metadata",
        },
    }
    assert baseline_seed_eligible(partial_content) is False
    assert baseline_seed_eligible(partial_metadata) is False


def test_complete_observation_can_replace_comparator_baseline():
    complete={
        "state":"OBSERVED",
        "snapshot":{
            "available":True,
            "content_hash":"sha256:content",
            "metadata_hash":"sha256:metadata",
            "content_observation_id":"src-content",
            "metadata_observation_id":"src-metadata",
        },
    }
    assert baseline_seed_eligible(complete) is True


def test_partial_state_label_cannot_seed_even_if_snapshot_claims_both_ids():
    inconsistent={
        "state":"PARTIAL_OBSERVATION",
        "snapshot":{
            "available":True,
            "content_hash":"sha256:content",
            "metadata_hash":"sha256:metadata",
            "content_observation_id":"src-content",
            "metadata_observation_id":"src-metadata",
        },
    }
    assert baseline_seed_eligible(inconsistent) is False


def test_partial_reobservation_record_survives_without_moving_baseline():
    from needle.provenance.ledger import seal_record

    prior=current_baseline()
    content=deepcopy(observation(prior["content_observation_id"]))
    content["record_id"]="src-operational-partial-evidence"
    content["created_at"]="2026-09-21T08:02:00+00:00"
    content["payload"]["observed_at"]="2026-09-21T08:02:00+00:00"
    content["record_hash"]=None
    content=seal_record(content)
    partial={
        "state":"PARTIAL_OBSERVATION",
        "content_observation":content,
        "metadata_observation":None,
        "snapshot":{
            "available":True,
            "content_hash":content["payload"]["artifact_hash"],
            "metadata_hash":None,
            "content_observation_id":content["record_id"],
            "metadata_observation_id":None,
        },
    }
    recorded=record_reobservation(
        STATE,partial,updated_at="2026-09-21T08:02:00+00:00"
    )
    assert any(
        item["record_id"]==content["record_id"]
        for item in recorded["source_observations"]
    )
    assert recorded["baselines"]==STATE["baselines"]
    assert baseline_seed_eligible(partial) is False


def test_processed_event_retention_is_scoped_to_next_overlap_window():
    state=deepcopy(STATE)
    old_key="cellar:old_2026-09-21T09:50:00+00:00"
    keep_key="cellar:keep_2026-09-21T09:57:00+00:00"
    boundary_key="cellar:boundary_2026-09-21T09:55:00+00:00"
    state["processed_event_keys"]=[old_key,keep_key,boundary_key]
    events=[
        {"event_key":old_key,"ingestion_time":"2026-09-21T09:50:00+00:00"},
        {"event_key":boundary_key,"ingestion_time":"2026-09-21T09:55:00+00:00"},
        {"event_key":keep_key,"ingestion_time":"2026-09-21T09:57:00+00:00"},
    ]
    compact=retain_overlap_event_keys(
        state,events,
        window_end="2026-09-21T10:00:00+00:00",
        overlap_seconds=300,
        updated_at="2026-09-21T10:00:00+00:00",
    )
    assert compact["processed_event_keys"]==[boundary_key,keep_key]


def test_overlap_retention_does_not_add_unprocessed_event():
    state=deepcopy(STATE)
    state["processed_event_keys"]=[]
    event={
        "event_key":"cellar:new_2026-09-21T09:59:00+00:00",
        "ingestion_time":"2026-09-21T09:59:00+00:00",
    }
    compact=retain_overlap_event_keys(
        state,[event],
        window_end="2026-09-21T10:00:00+00:00",
        overlap_seconds=300,
        updated_at="2026-09-21T10:00:00+00:00",
    )
    assert compact["processed_event_keys"]==[]
