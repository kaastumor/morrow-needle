from __future__ import annotations

import hashlib
import json
from typing import Any


class OperationalPipelineError(ValueError):
    pass


_SOURCE_ONLY_DISPOSITIONS = {
    "NO_MATERIAL_CHANGE":"NO_MATERIAL_CHANGE",
    "METADATA_ONLY":"SOURCE_METADATA_ONLY",
    "AVAILABILITY_CHANGED":"SOURCE_AVAILABILITY_CHANGED",
    "UNRESOLVED":"ABSTAIN_SOURCE_UNRESOLVED",
}

_STREAM_BY_DISPOSITION = {
    "LEGAL_CHANGE_VERIFIED":"CHANGE_FEED",
    "LEGAL_NON_IMPACT_VERIFIED":"AUDIT_FEED",
    "SOURCE_CREATED_UNANALYSED":"ABSTENTION_FEED",
    "SOURCE_CONTENT_CHANGED_UNRESOLVED":"ABSTENTION_FEED",
    "SOURCE_METADATA_ONLY":"AUDIT_FEED",
    "SOURCE_AVAILABILITY_CHANGED":"AUDIT_FEED",
    "NO_MATERIAL_CHANGE":"AUDIT_FEED",
    "ABSTAIN_SOURCE_UNRESOLVED":"ABSTENTION_FEED",
    "ABSTAIN_LEGAL_UNRESOLVED":"ABSTENTION_FEED",
}


def _stable_digest(value: dict[str, Any]) -> str:
    payload=json.dumps(
        value,
        sort_keys=True,
        separators=(",",":"),
        ensure_ascii=False,
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()[:32]


def _observation_refs(source_change: dict[str, Any]) -> list[str]:
    refs=[source_change["change_id"]]
    for side in ("previous","current"):
        snapshot=source_change.get(side)
        if not snapshot:
            continue
        for field in (
            "content_observation_id",
            "metadata_observation_id",
        ):
            value=snapshot.get(field)
            if value:
                refs.append(value)
    return list(dict.fromkeys(refs))


def _trigger(event: dict[str, Any], source_change: dict[str, Any]) -> dict[str, Any]:
    return {
        "event_key":event["event_key"],
        "feed_action":event["action"],
        "ingestion_time":event["ingestion_time"],
        "target_cellar_id":event["cellar_id"],
        "root_cellar_id":event["root_cellar_id"],
        "identifiers":list(event.get("identifiers",[])),
        "refresh_scope":source_change["refresh_scope"],
    }


def _require_legal_change_shape(
    downstream: dict[str, Any],
) -> None:
    refs=downstream.get("canonical_refs",[])
    if not any(ref.get("kind") == "MUTATION" for ref in refs):
        raise OperationalPipelineError(
            "LEGAL_CHANGE_VERIFIED requires at least one canonical MUTATION ref"
        )
    explanation=downstream.get("explanation")
    if not explanation:
        raise OperationalPipelineError(
            "LEGAL_CHANGE_VERIFIED requires an explanation projection"
        )
    if explanation.get("evidence_character") == "UNRESOLVED":
        raise OperationalPipelineError(
            "verified legal change cannot have UNRESOLVED evidence character"
        )


def build_operational_result(
    event: dict[str, Any],
    source_change: dict[str, Any],
    *,
    downstream: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Connect feed/source state to downstream legal analysis without conflation."""
    if source_change["event_key"] != event["event_key"]:
        raise OperationalPipelineError(
            "source change does not belong to trigger feed event"
        )

    classification=source_change["classification"]
    canonical_refs=[]
    explanation=None
    unknowns=[]
    evidence_refs=[
        f"feed-event:{event['event_key']}",
        *_observation_refs(source_change),
    ]

    if downstream is None:
        if classification in _SOURCE_ONLY_DISPOSITIONS:
            disposition=_SOURCE_ONLY_DISPOSITIONS[classification]
        elif classification == "SOURCE_CREATED":
            disposition="SOURCE_CREATED_UNANALYSED"
            unknowns.append(
                "No downstream legal comparison has yet established whether the newly observed source creates or changes legal rules."
            )
        elif classification == "CONTENT_CHANGED":
            disposition="SOURCE_CONTENT_CHANGED_UNRESOLVED"
            unknowns.append(
                "Official source bytes changed, but legal mutation/non-impact analysis has not yet resolved the change."
            )
        else:
            raise OperationalPipelineError(
                f"unsupported source classification: {classification}"
            )
    else:
        requested=downstream["disposition"]
        if classification in {"NO_MATERIAL_CHANGE","METADATA_ONLY"} and requested in {
            "LEGAL_CHANGE_VERIFIED","LEGAL_NON_IMPACT_VERIFIED"
        }:
            raise OperationalPipelineError(
                f"{classification} source re-observation cannot emit {requested}"
            )
        if classification == "UNRESOLVED" and requested in {
            "LEGAL_CHANGE_VERIFIED","LEGAL_NON_IMPACT_VERIFIED"
        }:
            raise OperationalPipelineError(
                "unresolved source state cannot emit verified legal disposition"
            )
        if requested == "LEGAL_CHANGE_VERIFIED":
            _require_legal_change_shape(downstream)
        elif requested == "LEGAL_NON_IMPACT_VERIFIED":
            if not downstream.get("explanation"):
                raise OperationalPipelineError(
                    "LEGAL_NON_IMPACT_VERIFIED requires explanation"
                )
        elif requested != "ABSTAIN_LEGAL_UNRESOLVED":
            raise OperationalPipelineError(
                f"unsupported downstream disposition: {requested}"
            )

        disposition=requested
        canonical_refs=list(downstream.get("canonical_refs",[]))
        evidence_refs.extend(downstream.get("evidence_refs",[]))
        explanation=downstream.get("explanation")
        unknowns=list(downstream.get("unknowns",[]))

    stream=_STREAM_BY_DISPOSITION[disposition]
    evidence_refs=list(dict.fromkeys(evidence_refs))
    material={
        "event_key":event["event_key"],
        "source_change_id":source_change["change_id"],
        "disposition":disposition,
        "canonical_refs":canonical_refs,
        "evidence_refs":evidence_refs,
    }
    return {
        "schema_version":"operational-result-v0.1",
        "result_id":f"operational-result:{_stable_digest(material)}",
        "character":"PROCESS_RECORD",
        "trigger":_trigger(event,source_change),
        "source_change":source_change,
        "disposition":disposition,
        "stream":stream,
        "canonical_refs":canonical_refs,
        "evidence_refs":evidence_refs,
        "explanation":explanation,
        "unknowns":unknowns,
    }


def _identifier_label(result: dict[str, Any]) -> str:
    identifiers=result["trigger"]["identifiers"]
    celex=next(
        (value for value in identifiers if value.lower().startswith("celex:")),
        None,
    )
    return celex or identifiers[0] if identifiers else result["trigger"]["target_cellar_id"]


def _source_only_copy(result: dict[str, Any]) -> tuple[str,str,str]:
    label=_identifier_label(result)
    disposition=result["disposition"]
    if disposition == "NO_MATERIAL_CHANGE":
        return (
            f"No material source change for {label}",
            "An official feed event triggered re-observation, but content and metadata hashes are unchanged.",
            "Shown in the audit stream because official update hints are not silently discarded even when re-observation finds no material change.",
        )
    if disposition == "SOURCE_METADATA_ONLY":
        return (
            f"Metadata-only source update for {label}",
            "The re-observed legal content hash is unchanged while source metadata changed.",
            "Shown in the audit stream because source metadata changes are tracked separately from legal-text change.",
        )
    if disposition == "SOURCE_AVAILABILITY_CHANGED":
        return (
            f"Source availability changed for {label}",
            "The official source branch changed availability state.",
            "Shown in the audit stream because source availability is operational evidence, not legal-state truth.",
        )
    if disposition == "ABSTAIN_SOURCE_UNRESOLVED":
        return (
            f"Needle could not resolve source state for {label}",
            "The official feed event was observed, but the targeted source re-observation is insufficient to classify material source change.",
            "Shown as an abstention rather than guessing from the feed action.",
        )
    if disposition == "SOURCE_CREATED_UNANALYSED":
        return (
            f"New official source observed for {label}",
            "A source was newly observed, but no downstream legal comparison has yet established its legal effect.",
            "Shown as unresolved until legal comparison is complete.",
        )
    if disposition == "SOURCE_CONTENT_CHANGED_UNRESOLVED":
        return (
            f"Official source content changed for {label}",
            "Official source bytes changed, but Needle has not yet resolved whether the difference is a legal mutation, non-impact change or representation effect.",
            "Shown as an abstention until legal analysis closes the source-to-law gap.",
        )
    raise OperationalPipelineError(
        f"no source-only copy for disposition {disposition}"
    )


def build_feed_card(result: dict[str, Any]) -> dict[str, Any]:
    """Project one operational result into a factual public/audit card."""
    explanation=result.get("explanation")
    if result["disposition"] in {
        "LEGAL_CHANGE_VERIFIED","LEGAL_NON_IMPACT_VERIFIED","ABSTAIN_LEGAL_UNRESOLVED"
    }:
        if explanation is None:
            if result["disposition"] != "ABSTAIN_LEGAL_UNRESOLVED":
                raise OperationalPipelineError(
                    "resolved legal disposition lacks explanation"
                )
            label=_identifier_label(result)
            headline=f"Legal effect unresolved for {label}"
            what_changed=(
                "The official source changed, but Needle does not yet have enough evidence to state the legal effect."
            )
            why_visible="Shown as an abstention so unresolved legal analysis is not dropped."
            compared_with=None
            when_it_matters=None
            affected=[]
            evidence_character="UNRESOLVED"
        else:
            what_changed=explanation["what_changed"]
            compared_with=explanation["compared_with"]
            when_it_matters=explanation["when_it_matters"]
            affected=list(explanation["affected"])
            evidence_character=explanation["evidence_character"]
            label=_identifier_label(result)
            if result["disposition"] == "LEGAL_CHANGE_VERIFIED":
                headline=f"Verified legal change — {label}"
                why_visible=(
                    "Shown because source re-observation led to a verified legal mutation."
                )
            elif result["disposition"] == "LEGAL_NON_IMPACT_VERIFIED":
                headline=f"Reviewed update with no scoped legal impact — {label}"
                why_visible=(
                    "Shown in the audit stream because a reviewed official update was verified as non-impact for the scoped rule."
                )
            else:
                headline=f"Legal effect unresolved — {label}"
                why_visible=(
                    "Shown as an abstention because legal analysis remains unresolved."
                )
    else:
        headline,what_changed,why_visible=_source_only_copy(result)
        compared_with=None
        when_it_matters=None
        affected=[]
        evidence_character=(
            "UNRESOLVED"
            if result["stream"] == "ABSTENTION_FEED"
            else "SOURCE_ONLY"
        )

    material={
        "operational_result_id":result["result_id"],
        "stream":result["stream"],
        "headline":headline,
    }
    refs=list(result["evidence_refs"])
    return {
        "schema_version":"feed-card-v0.1",
        "card_id":f"feed-card:{_stable_digest(material)}",
        "character":"DERIVED_VIEW",
        "stream":result["stream"],
        "headline":headline,
        "why_visible":why_visible,
        "what_changed":what_changed,
        "compared_with":compared_with,
        "when_it_matters":when_it_matters,
        "affected":affected,
        "evidence_character":evidence_character,
        "source_mode":{
            "closed":bool(refs),
            "refs":refs,
        },
        "canonical_refs":list(result["canonical_refs"]),
        "unknowns":list(result["unknowns"]),
        "operational_result_id":result["result_id"],
    }
