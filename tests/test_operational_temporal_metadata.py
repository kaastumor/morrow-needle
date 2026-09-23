import json
from pathlib import Path

from jsonschema import Draft202012Validator

from needle.updates.temporal_metadata import (
    extract_cellar_entry_into_force_metadata,
    extract_cellar_publication_metadata,
)


TEMPORAL_SCHEMA=json.loads(
    Path("schemas/temporal-assertion-v0.1.schema.json").read_text(
        encoding="utf-8"
    )
)

RDF_OPEN=(
    '<rdf:RDF '
    'xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" '
    'xmlns:cdm="http://publications.europa.eu/ontology/cdm#" '
    'xmlns:cmr="http://publications.europa.eu/ontology/cdm/cmr#">'
    '<rdf:Description rdf:about="http://publications.europa.eu/resource/oj/L_202602104">'
)
RDF_CLOSE='</rdf:Description></rdf:RDF>'


def notice(*elements):
    return (RDF_OPEN+"".join(elements)+RDF_CLOSE).encode("utf-8")


def cdm(tag,value):
    return (
        f'<cdm:{tag} '
        'rdf:datatype="http://www.w3.org/2001/XMLSchema#date">'
        f'{value}</cdm:{tag}>'
    )


def test_explicit_publication_properties_resolve_and_ignore_other_dates():
    payload=notice(
        cdm("date_document","2026-09-17"),
        cdm("work_date_document","2026-09-17"),
        cdm("official-journal-act_date_publication","2026-09-18"),
        cdm("date_publication","2026-09-18"),
        cdm("date_creation_legacy","2026-09-18"),
        '<cmr:creationDate '
        'rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">'
        '2026-09-18T02:37:27.225+02:00</cmr:creationDate>',
        '<cmr:lastModificationDate '
        'rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">'
        '2026-09-21T23:00:00+02:00</cmr:lastModificationDate>',
    )
    result=extract_cellar_publication_metadata(
        payload,
        identifier="CELEX:32026R2104",
        evidence_ref="src-metadata:2104",
    )
    assert result["state"]=="RESOLVED"
    assert result["evidence_refs"]==["src-metadata:2104"]
    assert result["source_properties"]==[
        "date_publication",
        "official-journal-act_date_publication",
    ]
    assertion=result["assertion"]
    assert assertion["normalized_date"]=="2026-09-18"
    assert assertion["dimension"]=="PUBLICATION"
    assert assertion["boundary"]=="POINT"
    assert assertion["scope"]["applies_to"]==["ACT:32026R2104"]
    assert assertion["trigger"]["source_expression"]==(
        "Cellar CDM official-journal-act_date_publication"
    )
    assert list(
        Draft202012Validator(TEMPORAL_SCHEMA).iter_errors(assertion)
    )==[]


def test_duplicate_identical_publication_occurrences_are_representation_duplication():
    result=extract_cellar_publication_metadata(
        notice(
            cdm("official-journal-act_date_publication","2026-09-18"),
            cdm("official-journal-act_date_publication","2026-09-18"),
            cdm("date_publication","2026-09-18"),
        ),
        identifier="32026R2104",
        evidence_ref="src-metadata:duplicate",
    )
    assert result["state"]=="RESOLVED"
    assert len(result["occurrences"])==3
    assert result["assertion"]["normalized_date"]=="2026-09-18"


def test_conflicting_explicit_publication_properties_fail_closed():
    result=extract_cellar_publication_metadata(
        notice(
            cdm("official-journal-act_date_publication","2026-09-18"),
            cdm("date_publication","2026-09-19"),
        ),
        identifier="CELEX:32026R2104",
        evidence_ref="src-metadata:conflict",
    )
    assert result["state"]=="CONFLICTING"
    assert result["assertion"] is None
    assert "disagree" in result["unknowns"][0]


def test_generic_date_publication_is_accepted_when_oj_specific_property_absent():
    result=extract_cellar_publication_metadata(
        notice(cdm("date_publication","2025-06-13")),
        identifier="CELEX:32025R0905",
        evidence_ref="src-metadata:905",
    )
    assert result["state"]=="RESOLVED"
    assert result["assertion"]["normalized_date"]=="2025-06-13"
    assert result["assertion"]["source_refs"][0]["locator"].endswith(
        "cdm:date_publication"
    )


def test_document_and_source_system_dates_do_not_manufacture_publication():
    result=extract_cellar_publication_metadata(
        notice(
            cdm("date_document","2026-09-17"),
            cdm("date_creation_legacy","2026-09-18"),
            '<cmr:lastModificationDate '
            'rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">'
            '2026-09-22T01:00:00+02:00</cmr:lastModificationDate>',
        ),
        identifier="CELEX:32026R2104",
        evidence_ref="src-metadata:no-publication",
    )
    assert result["state"]=="NOT_ASSERTED"
    assert result["assertion"] is None


def test_invalid_explicit_publication_literal_does_not_fall_back_to_other_dates():
    result=extract_cellar_publication_metadata(
        notice(
            cdm("official-journal-act_date_publication","18-09-2026"),
            cdm("date_document","2026-09-17"),
        ),
        identifier="CELEX:32026R2104",
        evidence_ref="src-metadata:invalid",
    )
    assert result["state"]=="UNRESOLVED"
    assert result["assertion"] is None


def test_malformed_rdf_abstains_instead_of_scanning_date_strings():
    result=extract_cellar_publication_metadata(
        b"<rdf>2026-09-18",
        identifier="CELEX:32026R2104",
        evidence_ref="src-metadata:malformed",
    )
    assert result["state"]=="UNRESOLVED"
    assert result["assertion"] is None


def test_explicit_entry_into_force_property_projects_legal_force_start():
    payload=notice(
        cdm("official-journal-act_date_publication","2026-09-18"),
        cdm("resource_legal_date_entry-into-force","2026-09-19"),
        cdm("date_document","2026-09-17"),
    )
    result=extract_cellar_entry_into_force_metadata(
        payload,
        identifier="CELEX:32026R2104",
        evidence_ref="src-metadata:2104",
    )
    assert result["state"]=="RESOLVED"
    assert result["evidence_refs"]==["src-metadata:2104"]
    assert result["source_properties"]==[
        "resource_legal_date_entry-into-force"
    ]
    assertion=result["assertion"]
    assert assertion["normalized_date"]=="2026-09-19"
    assert assertion["dimension"]=="LEGAL_FORCE"
    assert assertion["boundary"]=="START"
    assert assertion["scope"]["applies_to"]==["ACT:32026R2104"]
    assert assertion["source_refs"][0]["role"]=="DERIVATION_INPUT"
    assert "application date" in assertion["notes"]
    assert list(
        Draft202012Validator(TEMPORAL_SCHEMA).iter_errors(assertion)
    )==[]


def test_entry_into_force_does_not_fall_back_to_publication_or_document_date():
    result=extract_cellar_entry_into_force_metadata(
        notice(
            cdm("official-journal-act_date_publication","2026-09-18"),
            cdm("date_publication","2026-09-18"),
            cdm("date_document","2026-09-17"),
        ),
        identifier="CELEX:32026R2104",
        evidence_ref="src-metadata:no-force",
    )
    assert result["state"]=="NOT_ASSERTED"
    assert result["assertion"] is None


def test_duplicate_identical_entry_into_force_occurrences_are_not_corroboration():
    result=extract_cellar_entry_into_force_metadata(
        notice(
            cdm("resource_legal_date_entry-into-force","2026-09-19"),
            cdm("resource_legal_date_entry-into-force","2026-09-19"),
        ),
        identifier="CELEX:32026R2104",
        evidence_ref="src-metadata:force-duplicate",
    )
    assert result["state"]=="RESOLVED"
    assert len(result["occurrences"])==2
    assert result["assertion"]["normalized_date"]=="2026-09-19"


def test_conflicting_entry_into_force_values_fail_closed():
    result=extract_cellar_entry_into_force_metadata(
        notice(
            cdm("resource_legal_date_entry-into-force","2026-09-19"),
            cdm("resource_legal_date_entry-into-force","2026-09-20"),
        ),
        identifier="CELEX:32026R2104",
        evidence_ref="src-metadata:force-conflict",
    )
    assert result["state"]=="CONFLICTING"
    assert result["assertion"] is None
    assert "disagree" in result["unknowns"][0]


def test_invalid_entry_into_force_literal_does_not_use_publication_arithmetic():
    result=extract_cellar_entry_into_force_metadata(
        notice(
            cdm("resource_legal_date_entry-into-force","19-09-2026"),
            cdm("official-journal-act_date_publication","2026-09-18"),
        ),
        identifier="CELEX:32026R2104",
        evidence_ref="src-metadata:force-invalid",
    )
    assert result["state"]=="UNRESOLVED"
    assert result["assertion"] is None
