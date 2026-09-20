import json
from copy import deepcopy
from pathlib import Path

from jsonschema import Draft202012Validator

from needle.operations.state import (
    advance_baseline,
    baseline_key,
    lookup_baseline,
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


def test_seed_state_and_embedded_provenance_validate():
    assert list(
        Draft202012Validator(STATE_SCHEMA).iter_errors(STATE)
    ) == []
    assert validate_operational_state(STATE) == []
    assert len(STATE["baselines"]) == 3
    assert len(STATE["source_observations"]) == 6
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


def test_later_event_gets_complete_prior_snapshot():
    later=event()
    lookup=lookup_baseline(STATE,later)
    assert lookup["state"] == "ELIGIBLE"
    assert lookup["snapshot"] == {
        "available":True,
        "content_hash":(
            "sha256:b2f4fc192ebe69d743c9ee15f1d576b8"
            "ad87bd83d5de19b3373c8eba4d13d020"
        ),
        "metadata_hash":(
            "sha256:b4ef3683299a2970dae23573ae652ce625"
            "f17a0ffad65252ae351bbf2c239c51"
        ),
        "content_observation_id":(
            "src-operational-content-0204a83622f5602f2eefb29ca9f8cd6c"
        ),
        "metadata_observation_id":(
            "src-operational-metadata-b9ce44d3eb856b5cb789413f9557e293"
        ),
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
    content=deepcopy(next(
        record for record in STATE["source_observations"]
        if record["record_id"].startswith("src-operational-content-0204")
    ))
    metadata=deepcopy(next(
        record for record in STATE["source_observations"]
        if record["record_id"].startswith("src-operational-metadata-b9ce")
    ))
    content["record_id"]="src-operational-content-next"
    metadata["record_id"]="src-operational-metadata-next"
    for record in (content,metadata):
        record["created_at"]="2026-09-21T08:01:00+00:00"
        record["payload"]["observed_at"]="2026-09-21T08:01:00+00:00"
        # Re-seal after changing immutable observation metadata.
        record.pop("record_hash",None)
    from needle.provenance.ledger import seal_record
    content=seal_record(content)
    metadata=seal_record(metadata)

    reobservation={
        "state":"OBSERVED",
        "content_observation":content,
        "metadata_observation":metadata,
        "snapshot":{
            "available":True,
            "content_hash":content["payload"]["artifact_hash"],
            "metadata_hash":metadata["payload"]["artifact_hash"],
            "content_observation_id":content["record_id"],
            "metadata_observation_id":metadata["record_id"],
        },
    }
    advanced=advance_baseline(
        STATE,
        later,
        reobservation,
        updated_at="2026-09-21T08:01:01+00:00",
        seed_character="POST_EVENT_REFRESH",
    )
    assert len(advanced["source_observations"]) == 8
    assert len(advanced["baselines"]) == 3
    current=next(
        item for item in advanced["baselines"]
        if item["baseline_key"] == "CELEX:32019R0632|ENG"
    )
    assert current["content_observation_id"] == content["record_id"]
    assert current["metadata_observation_id"] == metadata["record_id"]
    assert current["seed_character"] == "POST_EVENT_REFRESH"
    assert later["event_key"] in advanced["processed_event_keys"]
    # Prior observation records remain append-only.
    assert any(
        record["record_id"]
        == "src-operational-content-0204a83622f5602f2eefb29ca9f8cd6c"
        for record in advanced["source_observations"]
    )
    assert validate_operational_state(advanced) == []


def test_advance_is_idempotent_for_same_event_and_observations():
    later=event()
    content=next(
        record for record in STATE["source_observations"]
        if record["record_id"].startswith("src-operational-content-0204")
    )
    metadata=next(
        record for record in STATE["source_observations"]
        if record["record_id"].startswith("src-operational-metadata-b9ce")
    )
    reobservation={
        "state":"OBSERVED",
        "content_observation":content,
        "metadata_observation":metadata,
        "snapshot":{
            "available":True,
            "content_hash":content["payload"]["artifact_hash"],
            "metadata_hash":metadata["payload"]["artifact_hash"],
            "content_observation_id":content["record_id"],
            "metadata_observation_id":metadata["record_id"],
        },
    }
    once=advance_baseline(
        STATE,later,reobservation,
        updated_at="2026-09-21T08:02:00+00:00",
        seed_character="POST_EVENT_REFRESH",
    )
    twice=advance_baseline(
        once,later,reobservation,
        updated_at="2026-09-21T08:02:00+00:00",
        seed_character="POST_EVENT_REFRESH",
    )
    assert twice == once
