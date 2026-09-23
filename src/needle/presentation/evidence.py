from __future__ import annotations

from typing import Any, Iterable

from needle.provenance.ledger import verify_record_hash


class EvidencePresentationError(ValueError):
    pass


def _normalize_celex(value: Any) -> str | None:
    if value is None:
        return None
    normalized=str(value).strip().upper()
    if normalized.startswith("CELEX:"):
        normalized=normalized.split(":",1)[1]
    return normalized or None


def _trigger_celexes(result: dict[str, Any]) -> set[str]:
    return {
        normalized
        for value in result.get("trigger",{}).get("identifiers",[])
        for normalized in [_normalize_celex(value)]
        if normalized and str(value).lower().startswith("celex:")
    }


def _subject_label(result: dict[str, Any]) -> str:
    identifiers=result.get("trigger",{}).get("identifiers",[])
    celex=next(
        (value.split(":",1)[1] for value in identifiers if str(value).lower().startswith("celex:")),
        None,
    )
    if celex:
        return f"CELEX {celex}"
    root=result.get("trigger",{}).get("root_cellar_id")
    return f"Cellar {root}" if root else "official source"


def _source_change_copy(result: dict[str, Any]) -> tuple[str,str,str,str]:
    classification=result["source_change"]["classification"]
    subject=_subject_label(result)
    mapping={
        "NO_MATERIAL_CHANGE":(
            f"Source comparison — {subject}",
            "The observed legal content and source metadata match the prior baseline.",
            "SOURCE_ONLY",
            "This does not establish that no legal issue exists outside the observed source dimensions.",
        ),
        "METADATA_ONLY":(
            f"Metadata-only comparison — {subject}",
            "Official source metadata changed while the observed legal-content hash did not.",
            "SOURCE_ONLY",
            "A metadata update does not establish a legal-text mutation or legal-effect date.",
        ),
        "CONTENT_CHANGED":(
            f"Observed content change — {subject}",
            "Official source content differs from the eligible prior observation.",
            "SOURCE_ONLY",
            "Changed source bytes do not by themselves establish the legal mutation or its effect.",
        ),
        "AVAILABILITY_CHANGED":(
            f"Observed source availability change — {subject}",
            "Independent source observations establish a change in availability state.",
            "SOURCE_ONLY",
            "Source availability is operational evidence, not legal-state truth.",
        ),
        "SOURCE_CREATED":(
            f"Newly observed official source — {subject}",
            "The operational source layer newly observed this official resource.",
            "SOURCE_ONLY",
            "A newly observed source does not by itself establish a new legal rule.",
        ),
        "UNRESOLVED":(
            f"Unresolved source comparison — {subject}",
            "The available source observations are insufficient for a material-change conclusion.",
            "UNRESOLVED",
            "No legal or source-change conclusion should be inferred from the unresolved comparison.",
        ),
    }
    if classification not in mapping:
        raise EvidencePresentationError(
            f"unsupported source-change classification: {classification}"
        )
    return mapping[classification]


def _snapshot_roles(result: dict[str, Any]) -> dict[str,list[str]]:
    roles: dict[str,list[str]]={}
    for side,label in (("previous","prior"),("current","current")):
        snapshot=result.get("source_change",{}).get(side) or {}
        for field,kind in (
            ("content_observation_id","legal content"),
            ("metadata_observation_id","source metadata"),
        ):
            ref=snapshot.get(field)
            if ref:
                roles.setdefault(ref,[]).append(f"{label} {kind}")
    return roles


def _record_map(records: Iterable[dict[str, Any]]) -> dict[str,dict[str, Any]]:
    by_id: dict[str,dict[str, Any]]={}
    for record in records:
        record_id=record.get("record_id")
        if not record_id:
            raise EvidencePresentationError("provenance presentation record requires record_id")
        if record_id in by_id and by_id[record_id] != record:
            raise EvidencePresentationError(
                f"conflicting provenance records share record_id {record_id}"
            )
        if not verify_record_hash(record):
            raise EvidencePresentationError(
                f"invalid provenance record hash: {record_id}"
            )
        by_id[record_id]=record
    return by_id


def _source_observation_item(
    ref: str,
    record: dict[str, Any],
    *,
    result: dict[str, Any],
    roles: list[str],
    expected_language: str | None,
) -> dict[str, Any]:
    payload=record["payload"]
    source_celex=_normalize_celex(payload.get("identifier"))
    trigger_celexes=_trigger_celexes(result)
    if source_celex and trigger_celexes and source_celex not in trigger_celexes:
        raise EvidencePresentationError(
            f"{ref}: Source Observation CELEX does not match operational trigger"
        )

    language=payload.get("language")
    if (
        expected_language is not None
        and language is not None
        and str(language).upper() != expected_language.upper()
    ):
        raise EvidencePresentationError(
            f"{ref}: Source Observation language does not match presentation scope"
        )

    identifier=payload.get("identifier") or _subject_label(result)
    source_type=payload.get("source_type") or "official"
    representation=payload.get("representation_class") or "source representation"
    role_text=", ".join(roles) if roles else "referenced official evidence"

    legal_cause=(
        result.get("verification_route") == "AUTHENTIC_LEGAL_CAUSE"
        and "current legal content" in roles
        and expected_language is not None
    )
    supports=(
        "Official legal content used by the authentic-cause verification route; "
        + f"this record is also the {role_text}."
        if legal_cause
        else f"Immutable official observation used as {role_text}."
    )
    does_not=(
        "This source observation alone does not establish application timing, affected entities, "
        "or semantic legal effect."
    )
    return {
        "ref":ref,
        "kind":"OFFICIAL_SOURCE_OBSERVATION",
        "label":f"{source_type} {representation} — {identifier}"
            + (f" ({language})" if language else ""),
        "supports":supports,
        "does_not_establish":does_not,
        "evidence_character":"DIRECT" if legal_cause else "SOURCE_ONLY",
        "official_uri":payload.get("resource_uri")
            or (payload.get("retrieval") or {}).get("final_uri"),
        "language":language,
        "audit_id":ref,
    }


def _claim_support_item(
    ref: str,
    record: dict[str, Any],
    *,
    by_id: dict[str,dict[str, Any]],
) -> dict[str, Any] | None:
    payload=record["payload"]
    source=by_id.get(payload.get("source_observation_id"))
    if not source or source.get("record_type") != "SOURCE_OBSERVATION":
        return None
    claim=payload["claim_ref"]
    source_payload=source["payload"]
    locator=payload["source_span"]["locator"]
    return {
        "ref":ref,
        "kind":"CLAIM_SUPPORT",
        "label":(
            f"{payload['role'].replace('_',' ').title()} evidence for "
            f"{claim['entity_type'].replace('_',' ').title()}"
        ),
        "supports":(
            f"{payload['evidence_state']} support for the referenced canonical claim "
            f"at {locator}."
        ),
        "does_not_establish":(
            "The presentation does not extend the claim beyond the canonical entity and source span."
        ),
        "evidence_character":payload["evidence_state"],
        "official_uri":source_payload.get("resource_uri")
            or (source_payload.get("retrieval") or {}).get("final_uri"),
        "language":payload["source_span"].get("language"),
        "audit_id":ref,
    }


def _temporal_assertion_map(
    assertions: Iterable[dict[str, Any]],
) -> dict[str,dict[str, Any]]:
    by_id: dict[str,dict[str, Any]]={}
    for assertion in assertions:
        assertion_id=assertion.get("assertion_id")
        if not assertion_id:
            raise EvidencePresentationError(
                "temporal presentation object requires assertion_id"
            )
        if assertion_id in by_id and by_id[assertion_id] != assertion:
            raise EvidencePresentationError(
                f"conflicting Temporal Assertions share assertion_id {assertion_id}"
            )
        by_id[assertion_id]=assertion
    return by_id


def _temporal_assertion_item(
    ref: str,
    assertion: dict[str, Any],
    *,
    result: dict[str, Any],
) -> dict[str, Any]:
    subject=assertion.get("subject_ref") or {}
    subject_identifier=subject.get("identifier")
    subject_celex=_normalize_celex(subject_identifier)
    trigger_celexes=_trigger_celexes(result)
    if (
        subject.get("kind") == "LEGAL_ACT"
        and subject_celex
        and trigger_celexes
        and subject_celex not in trigger_celexes
    ):
        raise EvidencePresentationError(
            f"{ref}: Temporal Assertion subject CELEX does not match operational trigger"
        )

    dimension=str(assertion.get("dimension") or "temporal").upper()
    boundary=str(assertion.get("boundary") or "boundary").upper()
    resolution=str(assertion.get("resolution_state") or "UNRESOLVED")
    evidence_state=str(assertion.get("evidence_state") or "UNRESOLVED")
    normalized_date=assertion.get("normalized_date")

    if resolution == "RESOLVED_ABSOLUTE" and normalized_date:
        supports=(
            f"{evidence_state} temporal evidence establishes the {dimension} "
            f"{boundary.lower()} for {subject_identifier or _subject_label(result)} "
            f"on {normalized_date}."
        )
    else:
        supports=(
            f"The canonical Temporal Assertion records the {dimension} "
            f"{boundary.lower()} for {subject_identifier or _subject_label(result)} "
            f"as {resolution}; no stronger temporal conclusion is presented."
        )

    does_not_by_dimension={
        "PUBLICATION":"Publication does not establish entry into force or application.",
        "LEGAL_FORCE":"Entry into force does not by itself establish when the rule applies.",
        "APPLICATION":"Application timing does not by itself establish publication, legal force, or text-state timing.",
        "TEXT_STATE":"Text-state timing does not by itself establish legal force or application.",
        "TRANSITION":"A transition boundary does not by itself establish every affected entity's application state.",
        "DEROGATION":"A derogation boundary does not establish broader application outside its evidenced scope.",
        "DEADLINE":"A deadline is not an application-start or entry-into-force date.",
    }
    source_languages={
        item.get("language")
        for item in assertion.get("source_refs",[])
        if item.get("language") is not None
    }
    language=next(iter(source_languages)) if len(source_languages) == 1 else None
    return {
        "ref":ref,
        "kind":"TEMPORAL_ASSERTION",
        "label":(
            f"{dimension.replace('_',' ').title()} — "
            f"{subject_identifier or _subject_label(result)}"
            + (f" · {normalized_date}" if normalized_date else f" · {resolution}")
        ),
        "supports":supports,
        "does_not_establish":does_not_by_dimension.get(
            dimension,
            "This temporal assertion establishes only its named dimension, scope, and resolution state.",
        ),
        "evidence_character":evidence_state,
        "official_uri":None,
        "language":language,
        "audit_id":ref,
        "dimension":dimension,
        "boundary":boundary,
        "resolution_state":resolution,
        "normalized_date":normalized_date,
    }


def build_evidence_view(
    card: dict[str, Any],
    result: dict[str, Any],
    *,
    provenance_records: Iterable[dict[str, Any]] = (),
    temporal_assertions: Iterable[dict[str, Any]] = (),
    expected_language: str | None = None,
) -> dict[str, Any]:
    """Resolve an operational card into human-readable evidence presentation.

    This is a disposable projection. It does not modify canonical provenance or
    infer legal facts from record IDs. Missing records remain unresolved.
    """
    if card.get("operational_result_id") != result.get("result_id"):
        raise EvidencePresentationError(
            "feed card does not belong to supplied operational result"
        )
    refs=list((card.get("source_mode") or {}).get("refs") or [])
    if refs != list(result.get("evidence_refs") or []):
        raise EvidencePresentationError(
            "feed card evidence refs do not match operational result"
        )

    by_id=_record_map(provenance_records)
    temporal_by_id=_temporal_assertion_map(temporal_assertions)
    typed_temporal_refs={
        item["entity_id"]
        for item in result.get("canonical_refs",[])
        if item.get("kind") == "TEMPORAL_ASSERTION"
    }
    roles=_snapshot_roles(result)
    trigger=result["trigger"]
    event_refs={
        f"feed-event:{trigger['event_key']}",
        *(f"feed-event:{value}" for value in trigger.get("related_event_keys",[])),
    }
    source_change_ref=result["source_change"]["change_id"]

    items=[]
    unresolved=[]
    for ref in refs:
        if ref in event_refs:
            action=trigger["feed_action"]
            items.append({
                "ref":ref,
                "kind":"OFFICIAL_UPDATE_TRIGGER",
                "label":f"Publications Office {action} notification — {_subject_label(result)}",
                "supports":"Why Needle investigated this official source state.",
                "does_not_establish":"A feed notification does not by itself establish legal-text change, legal effect, or legal timing.",
                "evidence_character":"SOURCE_ONLY",
                "official_uri":None,
                "language":None,
                "audit_id":ref,
            })
            continue
        if ref == source_change_ref:
            label,supports,character,does_not=_source_change_copy(result)
            items.append({
                "ref":ref,
                "kind":"SOURCE_COMPARISON",
                "label":label,
                "supports":supports,
                "does_not_establish":does_not,
                "evidence_character":character,
                "official_uri":None,
                "language":expected_language,
                "audit_id":ref,
            })
            continue

        record=by_id.get(ref)
        if record is None:
            assertion=temporal_by_id.get(ref)
            if assertion is not None and ref in typed_temporal_refs:
                items.append(_temporal_assertion_item(
                    ref,assertion,result=result
                ))
            else:
                unresolved.append(ref)
            continue
        if record.get("record_type") == "SOURCE_OBSERVATION":
            items.append(_source_observation_item(
                ref,record,result=result,roles=roles.get(ref,[]),
                expected_language=expected_language,
            ))
            continue
        if record.get("record_type") == "CLAIM_SUPPORT":
            item=_claim_support_item(ref,record,by_id=by_id)
            if item is None:
                unresolved.append(ref)
            else:
                items.append(item)
            continue
        unresolved.append(ref)

    return {
        "character":"PRESENTATION_ONLY",
        "title":"Evidence / Why this is shown",
        "state":"CLOSED" if not unresolved else "PARTIAL",
        "evidence_character":card["evidence_character"],
        "verification_route":card.get("verification_route"),
        "items":items,
        "unresolved_refs":unresolved,
        "unknowns":list(card.get("unknowns",[])),
        "operational_result_id":result["result_id"],
        "card_id":card["card_id"],
    }
