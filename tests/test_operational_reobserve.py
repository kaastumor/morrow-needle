import json
from pathlib import Path

from jsonschema import Draft202012Validator

from needle.provenance.ledger import verify_record_hash
from needle.updates.reobserve import reobserve_event


PROVENANCE_SCHEMA=json.loads(
    Path("schemas/provenance-record-v0.1.schema.json").read_text(
        encoding="utf-8"
    )
)


def publication_notice(date_value="2025-06-13"):
    return (
        '<rdf:RDF '
        'xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" '
        'xmlns:cdm="http://publications.europa.eu/ontology/cdm#">'
        '<rdf:Description>'
        '<cdm:date_document '
        'rdf:datatype="http://www.w3.org/2001/XMLSchema#date">'
        '2025-06-12</cdm:date_document>'
        '<cdm:official-journal-act_date_publication '
        'rdf:datatype="http://www.w3.org/2001/XMLSchema#date">'
        f'{date_value}</cdm:official-journal-act_date_publication>'
        '</rdf:Description></rdf:RDF>'
    ).encode("utf-8")


class FakeResponse:
    def __init__(self, status, content, *, url, content_type):
        self.status_code=status
        self.content=content
        self.url=url
        self.headers={"Content-Type":content_type}


class FakeSession:
    def __init__(self, responses):
        self.responses=list(responses)
        self.calls=[]

    def get(self, url, *, headers, timeout, allow_redirects):
        self.calls.append({
            "url":url,
            "headers":dict(headers),
            "timeout":timeout,
            "allow_redirects":allow_redirects,
        })
        return self.responses.pop(0)


def event(identifiers=None):
    return {
        "event_key":"cellar:test_2026-09-20T20:00:00+00:00",
        "notification_id":"n1",
        "notification_id_basis":"RSS_GUID",
        "raw_feed_id":"n1",
        "action":"UPDATE",
        "cellar_id":"cellar:test",
        "root_cellar_id":"cellar:test",
        "ingestion_time":"2026-09-20T20:00:00+00:00",
        "priority":"DAILY",
        "classes":[],
        "wemi_levels":["WORK"],
        "identifiers":identifiers or ["celex:32025R0905"],
        "feed_observation":{
            "channel":"ingestion",
            "format":"RSS",
            "window_start":None,
            "window_end":None,
            "page":1,
            "entry_ordinal":0,
        },
    }


def test_reobserver_emits_sealed_provenance_records_and_snapshot():
    session=FakeSession([
        FakeResponse(
            200,b"<rdf>metadata</rdf>",
            url="https://example.invalid/meta",
            content_type="application/rdf+xml",
        ),
        FakeResponse(
            200,b"PK\x03\x04FORMEX",
            url="https://example.invalid/fmx4",
            content_type="application/zip",
        ),
    ])
    result=reobserve_event(
        event(),
        observed_at="2026-09-20T20:10:00+00:00",
        session=session,
    )

    assert result["state"] == "OBSERVED"
    assert result["celex"] == "32025R0905"
    assert result["selected_representation"] == {
        "accept":"application/zip;mtype=fmx4",
        "representation_class":"STRUCTURED_LEGAL_XML",
    }
    assert result["snapshot"]["available"] is True
    assert result["snapshot"]["content_hash"].startswith("sha256:")
    assert result["snapshot"]["metadata_hash"].startswith("sha256:")

    for key in ("content_observation","metadata_observation"):
        record=result[key]
        assert verify_record_hash(record)
        assert list(
            Draft202012Validator(PROVENANCE_SCHEMA).iter_errors(record)
        ) == []
        assert record["record_type"] == "SOURCE_OBSERVATION"


def test_reobserver_falls_back_from_unavailable_formex_to_xhtml():
    session=FakeSession([
        FakeResponse(
            200,b"<rdf>metadata</rdf>",
            url="https://example.invalid/meta",
            content_type="application/rdf+xml",
        ),
        FakeResponse(
            406,b"",
            url="https://example.invalid/fmx4",
            content_type="text/plain",
        ),
        FakeResponse(
            200,b"PK\x03\x04XHTML",
            url="https://example.invalid/xhtml",
            content_type="application/zip",
        ),
    ])
    result=reobserve_event(
        event(),
        observed_at="2026-09-20T20:10:00+00:00",
        session=session,
    )
    assert result["state"] == "OBSERVED"
    assert result["selected_representation"]["representation_class"] == (
        "STRUCTURED_XHTML"
    )
    assert [call["headers"]["Accept"] for call in session.calls] == [
        "application/rdf+xml;notice=tree",
        "application/zip;mtype=fmx4",
        "application/zip;mtype=xhtml",
    ]


def test_metadata_without_supported_content_is_partial_not_absence():
    session=FakeSession([
        FakeResponse(
            200,b"<rdf>metadata</rdf>",
            url="https://example.invalid/meta",
            content_type="application/rdf+xml",
        ),
        FakeResponse(406,b"",url="u1",content_type="text/plain"),
        FakeResponse(406,b"",url="u2",content_type="text/plain"),
        FakeResponse(406,b"",url="u3",content_type="text/plain"),
        FakeResponse(406,b"",url="u4",content_type="text/plain"),
    ])
    result=reobserve_event(
        event(),
        observed_at="2026-09-20T20:10:00+00:00",
        session=session,
    )
    assert result["state"] == "PARTIAL_OBSERVATION"
    assert result["snapshot"]["available"] is True
    assert result["snapshot"]["content_hash"] is None
    assert result["metadata_observation"] is not None
    assert result["content_observation"] is None
    assert "no supported legal-text representation" in (
        result["unknowns"][0].casefold()
    )


def test_no_celex_identifier_abstains_before_network_access():
    session=FakeSession([])
    result=reobserve_event(
        event(["eli:http://data.europa.eu/example"]),
        observed_at="2026-09-20T20:10:00+00:00",
        session=session,
    )
    assert result["state"] == "UNRESOLVED_IDENTIFIER"
    assert result["snapshot"] is None
    assert session.calls == []


def test_identical_reobservation_inputs_are_deterministic():
    responses=lambda: FakeSession([
        FakeResponse(
            200,b"<rdf>metadata</rdf>",
            url="https://example.invalid/meta",
            content_type="application/rdf+xml",
        ),
        FakeResponse(
            200,b"PK\x03\x04FORMEX",
            url="https://example.invalid/fmx4",
            content_type="application/zip",
        ),
    ])
    first=reobserve_event(
        event(),
        observed_at="2026-09-20T20:10:00+00:00",
        session=responses(),
    )
    second=reobserve_event(
        event(),
        observed_at="2026-09-20T20:10:00+00:00",
        session=responses(),
    )
    assert (
        first["content_observation"]["record_id"]
        == second["content_observation"]["record_id"]
    )
    assert (
        first["metadata_observation"]["record_id"]
        == second["metadata_observation"]["record_id"]
    )
    assert first["snapshot"] == second["snapshot"]


def test_reobserver_projects_publication_from_same_sealed_metadata_observation():
    session=FakeSession([
        FakeResponse(
            200,publication_notice(),
            url="https://example.invalid/meta",
            content_type="application/rdf+xml",
        ),
        FakeResponse(
            200,b"PK\x03\x04FORMEX",
            url="https://example.invalid/fmx4",
            content_type="application/zip",
        ),
    ])
    result=reobserve_event(
        event(),
        observed_at="2026-09-20T20:10:00+00:00",
        session=session,
    )
    publication=result["temporal_metadata"]["publication"]
    assert publication["state"]=="RESOLVED"
    assert publication["assertion"]["normalized_date"]=="2025-06-13"
    assert publication["assertion"]["subject_ref"]["identifier"]==(
        "CELEX:32025R0905"
    )
    assert publication["evidence_refs"]==[
        result["metadata_observation"]["record_id"]
    ]
    assert publication["assertion"]["normalized_date"] != (
        result["metadata_observation"]["payload"]["observed_at"][:10]
    )


def test_conflicting_publication_metadata_survives_as_reobservation_unknown():
    conflicting=(
        '<rdf:RDF '
        'xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" '
        'xmlns:cdm="http://publications.europa.eu/ontology/cdm#">'
        '<rdf:Description>'
        '<cdm:official-journal-act_date_publication>'
        '2025-06-13</cdm:official-journal-act_date_publication>'
        '<cdm:date_publication>'
        '2025-06-14</cdm:date_publication>'
        '</rdf:Description></rdf:RDF>'
    ).encode("utf-8")
    session=FakeSession([
        FakeResponse(
            200,conflicting,
            url="https://example.invalid/meta",
            content_type="application/rdf+xml",
        ),
        FakeResponse(
            200,b"PK\x03\x04FORMEX",
            url="https://example.invalid/fmx4",
            content_type="application/zip",
        ),
    ])
    result=reobserve_event(
        event(),
        observed_at="2026-09-20T20:10:00+00:00",
        session=session,
    )
    assert result["temporal_metadata"]["publication"]["state"]=="CONFLICTING"
    assert any("publication-date properties disagree" in item for item in result["unknowns"])


def test_content_route_success_does_not_become_false_unavailability_when_metadata_route_fails():
    session=FakeSession([
        FakeResponse(
            503,b"",
            url="https://example.invalid/meta",
            content_type="text/plain",
        ),
        FakeResponse(
            200,b"PK\x03\x04FORMEX",
            url="https://example.invalid/fmx4",
            content_type="application/zip",
        ),
    ])
    result=reobserve_event(
        event(),
        observed_at="2026-09-20T20:10:00+00:00",
        session=session,
    )
    assert result["state"]=="PARTIAL_OBSERVATION"
    assert result["metadata_observation"] is None
    assert result["content_observation"] is not None
    assert result["snapshot"]["available"] is True
    assert result["snapshot"]["content_hash"] is not None
    assert result["snapshot"]["metadata_hash"] is None
    assert any(
        "without the expected Cellar tree notice" in item
        for item in result["unknowns"]
    )
