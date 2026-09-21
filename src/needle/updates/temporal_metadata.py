from __future__ import annotations

from datetime import date
import hashlib
import json
from typing import Any
import xml.etree.ElementTree as ET


CDM_NAMESPACE="http://publications.europa.eu/ontology/cdm#"
PUBLICATION_PROPERTIES=(
    "official-journal-act_date_publication",
    "date_publication",
)


def _digest(value: Any) -> str:
    payload=json.dumps(
        value,sort_keys=True,separators=(",",":"),ensure_ascii=False
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()[:24]


def _tag_parts(tag: str) -> tuple[str | None,str]:
    if tag.startswith("{") and "}" in tag:
        namespace,local=tag[1:].split("}",1)
        return namespace,local
    return None,tag


def _date_literal(value: str) -> str | None:
    value=value.strip()
    try:
        parsed=date.fromisoformat(value)
    except ValueError:
        return None
    if parsed.isoformat() != value:
        return None
    return value


def extract_cellar_publication_metadata(
    payload: bytes,
    *,
    identifier: str,
    evidence_ref: str,
) -> dict[str, Any]:
    """Project explicit Cellar CDM publication properties into P0-E shape.

    Only source properties whose semantics explicitly say publication are
    eligible. Document dates, source-system creation/modification timestamps,
    legacy creation dates, annotations and arbitrary date-looking literals are
    intentionally ignored.

    The returned temporal assertion has stable legal-fact identity; the
    immutable Source Observation supplying the RDF bytes is carried separately
    in evidence_refs so repeated observations do not create new temporal truth.
    """
    try:
        root=ET.fromstring(payload)
    except (ET.ParseError,ValueError):
        return {
            "state":"UNRESOLVED",
            "assertion":None,
            "evidence_refs":[evidence_ref],
            "occurrences":[],
            "unknowns":[
                "Cellar RDF tree notice could not be parsed; publication time "
                "was not inferred from other source timestamps."
            ],
        }

    occurrences=[]
    invalid=[]
    for element in root.iter():
        namespace,local=_tag_parts(element.tag)
        if namespace != CDM_NAMESPACE or local not in PUBLICATION_PROPERTIES:
            continue
        raw=" ".join("".join(element.itertext()).split())
        normalized=_date_literal(raw)
        item={
            "property":local,
            "raw_value":raw,
            "normalized_date":normalized,
        }
        occurrences.append(item)
        if normalized is None:
            invalid.append(item)

    if not occurrences:
        return {
            "state":"NOT_ASSERTED",
            "assertion":None,
            "evidence_refs":[evidence_ref],
            "occurrences":[],
            "unknowns":[
                "No explicit Cellar CDM publication-date property was present "
                "in the observed tree notice."
            ],
        }

    if invalid:
        return {
            "state":"UNRESOLVED",
            "assertion":None,
            "evidence_refs":[evidence_ref],
            "occurrences":occurrences,
            "unknowns":[
                "An explicit Cellar publication-date property had a value that "
                "was not an exact ISO calendar date; no date was normalized."
            ],
        }

    values={item["normalized_date"] for item in occurrences}
    if len(values) != 1:
        return {
            "state":"CONFLICTING",
            "assertion":None,
            "evidence_refs":[evidence_ref],
            "occurrences":occurrences,
            "unknowns":[
                "Explicit Cellar publication-date properties disagree; "
                "automatic publication-time selection is forbidden."
            ],
        }

    publication_date=next(iter(values))
    properties=sorted({item["property"] for item in occurrences})
    canonical_property=(
        "official-journal-act_date_publication"
        if "official-journal-act_date_publication" in properties
        else "date_publication"
    )
    normalized_identifier=identifier.upper()
    if not normalized_identifier.startswith("CELEX:"):
        normalized_identifier=f"CELEX:{normalized_identifier}"
    celex=normalized_identifier.split(":",1)[1]

    assertion={
        "assertion_id":"temporal-publication:"+_digest({
            "identifier":normalized_identifier,
            "date":publication_date,
        }),
        "subject_ref":{
            "kind":"LEGAL_ACT",
            "identifier":normalized_identifier,
            "locator":"official publication metadata",
        },
        "dimension":"PUBLICATION",
        "boundary":"POINT",
        "inclusive":True,
        "trigger":{
            "kind":"ABSOLUTE_DATE",
            "date":publication_date,
            "source_expression":"Cellar CDM "+canonical_property,
        },
        "normalized_date":publication_date,
        "scope":{
            "mode":"DEFAULT",
            "applies_to":[f"ACT:{celex}"],
            "overrides_assertion_ids":[],
            "entity_condition":None,
        },
        "resolution_state":"RESOLVED_ABSOLUTE",
        "evidence_state":"DIRECT",
        "source_refs":[{
            "source_type":"CELLAR",
            "identifier":normalized_identifier,
            "locator":"CELLAR_RDF_NOTICE_TREE#cdm:"+canonical_property,
            "language":None,
            "role":"PUBLICATION_METADATA",
        }],
        "notes":(
            "Publication is projected only from explicit CDM publication "
            "properties. Repeated identical occurrences are representation "
            "duplication, not independent evidence."
        ),
    }
    return {
        "state":"RESOLVED",
        "assertion":assertion,
        "evidence_refs":[evidence_ref],
        "occurrences":occurrences,
        "source_properties":properties,
        "unknowns":[],
    }
