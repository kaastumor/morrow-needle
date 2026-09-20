from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
from typing import Any

import requests

from needle.provenance.ledger import seal_record
from needle.updates.classify import snapshot_from_observations


CELLAR_CELEX="https://publications.europa.eu/resource/celex/{celex}"

REPRESENTATIONS=(
    ("application/zip;mtype=fmx4","STRUCTURED_LEGAL_XML"),
    ("application/zip;mtype=xhtml","STRUCTURED_XHTML"),
    ("application/zip;mtype=html","STRUCTURED_HTML"),
    ("text/html","STRUCTURED_HTML"),
)


class ReobservationError(ValueError):
    pass


def celex_from_event(event: dict[str, Any]) -> str | None:
    for identifier in event.get("identifiers",[]):
        if identifier.lower().startswith("celex:"):
            return identifier.split(":",1)[1]
    return None


def _record_id(
    *,
    event_key: str,
    kind: str,
    artifact_hash: str,
    observed_at: str,
) -> str:
    material={
        "event_key":event_key,
        "kind":kind,
        "artifact_hash":artifact_hash,
        "observed_at":observed_at,
    }
    digest=hashlib.sha256(
        json.dumps(
            material,
            sort_keys=True,
            separators=(",",":"),
        ).encode("utf-8")
    ).hexdigest()[:32]
    return f"src-operational-{kind.lower()}-{digest}"


def _source_record(
    *,
    event_key: str,
    kind: str,
    identifier: str,
    resource_uri: str,
    language: str | None,
    representation_class: str,
    observed_at: str,
    response: requests.Response,
) -> dict[str, Any]:
    artifact_hash="sha256:"+hashlib.sha256(response.content).hexdigest()
    record={
        "record_id":_record_id(
            event_key=event_key,
            kind=kind,
            artifact_hash=artifact_hash,
            observed_at=observed_at,
        ),
        "record_type":"SOURCE_OBSERVATION",
        "created_at":observed_at,
        "payload":{
            "source_type":"CELLAR",
            "identifier":identifier,
            "resource_uri":resource_uri,
            "language":language,
            "representation_class":representation_class,
            "observed_at":observed_at,
            "artifact_hash":artifact_hash,
            "retrieval":{
                "final_uri":response.url,
                "media_type":response.headers.get(
                    "Content-Type","application/octet-stream"
                ).split(";",1)[0],
                "http_status":response.status_code,
            },
        },
    }
    return seal_record(record)


def _get(
    session: Any,
    url: str,
    *,
    accept: str,
    language: str | None,
) -> requests.Response:
    headers={
        "Accept":accept,
        "User-Agent":(
            "Morrow-Needle-Operational-Reobserver/0.1 "
            "(+https://github.com/kaastumor/morrow-needle)"
        ),
    }
    if language is not None:
        headers["Accept-Language"]=language
    return session.get(
        url,
        headers=headers,
        timeout=120,
        allow_redirects=True,
    )


def reobserve_event(
    event: dict[str, Any],
    *,
    observed_at: str | None = None,
    language: str = "eng",
    session: Any = requests,
) -> dict[str, Any]:
    """Targeted official re-observation for one CELEX-addressable feed event.

    Feed action remains only a hint. Returned provenance records are immutable
    observations; the caller still needs a prior snapshot to classify change.
    """
    celex=celex_from_event(event)
    if celex is None:
        return {
            "state":"UNRESOLVED_IDENTIFIER",
            "celex":None,
            "metadata_observation":None,
            "content_observation":None,
            "snapshot":None,
            "attempts":[],
            "unknowns":[
                "Feed event exposes no CELEX identifier supported by the v0.1 operational reobserver."
            ],
        }

    observed_at=observed_at or datetime.now(timezone.utc).isoformat()
    url=CELLAR_CELEX.format(celex=celex)
    identifier=f"CELEX:{celex}"

    attempts=[]
    metadata=_get(
        session,url,
        accept="application/rdf+xml;notice=tree",
        language=None,
    )
    attempts.append({
        "kind":"METADATA",
        "accept":"application/rdf+xml;notice=tree",
        "status":metadata.status_code,
        "final_uri":metadata.url,
        "media_type":metadata.headers.get("Content-Type"),
        "bytes":len(metadata.content),
    })

    metadata_record=None
    if metadata.status_code == 200 and metadata.content:
        metadata_record=_source_record(
            event_key=event["event_key"],
            kind="metadata",
            identifier=identifier,
            resource_uri=url,
            language=None,
            representation_class="CELLAR_RDF_NOTICE_TREE",
            observed_at=observed_at,
            response=metadata,
        )

    content_record=None
    selected=None
    for accept,representation_class in REPRESENTATIONS:
        response=_get(
            session,url,
            accept=accept,
            language=language,
        )
        attempts.append({
            "kind":"CONTENT",
            "accept":accept,
            "representation_class":representation_class,
            "status":response.status_code,
            "final_uri":response.url,
            "media_type":response.headers.get("Content-Type"),
            "bytes":len(response.content),
        })
        if response.status_code != 200 or not response.content:
            continue
        content_record=_source_record(
            event_key=event["event_key"],
            kind="content",
            identifier=identifier,
            resource_uri=url,
            language=language.upper(),
            representation_class=representation_class,
            observed_at=observed_at,
            response=response,
        )
        selected={
            "accept":accept,
            "representation_class":representation_class,
        }
        break

    available=metadata.status_code == 200
    if metadata_record is None and content_record is None:
        return {
            "state":"UNAVAILABLE",
            "celex":celex,
            "metadata_observation":None,
            "content_observation":None,
            "snapshot":{
                "available":False,
                "content_hash":None,
                "metadata_hash":None,
                "content_observation_id":None,
                "metadata_observation_id":None,
            },
            "attempts":attempts,
            "unknowns":[
                "No supported official representation could be re-observed."
            ],
        }

    snapshot=snapshot_from_observations(
        content_observation=content_record,
        metadata_observation=metadata_record,
        available=available,
    )
    state=(
        "OBSERVED"
        if content_record is not None and metadata_record is not None
        else "PARTIAL_OBSERVATION"
    )
    unknowns=[]
    if content_record is None:
        unknowns.append(
            "Official work metadata resolved, but no supported legal-text representation was retrieved."
        )
    if metadata_record is None:
        unknowns.append(
            "Legal-text representation was retrieved without the expected Cellar tree notice."
        )

    return {
        "state":state,
        "celex":celex,
        "metadata_observation":metadata_record,
        "content_observation":content_record,
        "snapshot":snapshot,
        "selected_representation":selected,
        "attempts":attempts,
        "unknowns":unknowns,
    }
