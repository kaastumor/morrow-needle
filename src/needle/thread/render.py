from __future__ import annotations

from pathlib import Path
from typing import Any

from needle.provenance.ledger import active_records
from needle.thread.composer import (
    PROVENANCE_ENTITY_TYPES,
    load_thread_sources,
    materialize_thread,
)


def _ref(kind: str, entity_id: str) -> dict[str, str]:
    return {"kind":kind, "entity_id":entity_id}


def _entity_index(materialized: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        ref["entity_id"]:ref["entity"]
        for event in materialized["events"]
        for ref in event["refs"]
    }


def _support_index(
    thread: dict[str, Any],
    *,
    root: Path | str,
) -> dict[tuple[str, str], list[dict[str, Any]]]:
    sources = load_thread_sources(thread, root=root)
    records = active_records(
        sources[thread["provenance_source_key"]]["data"]["records"]
    )
    result: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for record in records:
        if record.get("record_type") != "CLAIM_SUPPORT":
            continue
        payload = record["payload"]
        claim = payload["claim_ref"]
        result.setdefault(
            (claim["entity_type"], claim["entity_id"]),
            [],
        ).append({
            "support_record_id":record["record_id"],
            "source_observation_id":payload["source_observation_id"],
            "role":payload["role"],
            "evidence_state":payload["evidence_state"],
            "locator":payload["source_span"]["locator"],
        })
    return result


def _evidence_for_refs(
    refs: list[dict[str, str]],
    support: dict[tuple[str, str], list[dict[str, Any]]],
) -> list[dict[str, Any]]:
    evidence = []
    seen = set()
    for ref in refs:
        entity_type = PROVENANCE_ENTITY_TYPES.get(ref["kind"])
        if entity_type is None:
            continue
        for item in support.get((entity_type, ref["entity_id"]), []):
            key = item["support_record_id"]
            if key in seen:
                continue
            seen.add(key)
            evidence.append(item)
    return evidence


def _item(
    *,
    text: str,
    refs: list[dict[str, str]],
    support: dict[tuple[str, str], list[dict[str, Any]]],
    character: str = "FACTUAL",
    event_id: str | None = None,
) -> dict[str, Any]:
    return {
        "text":text,
        "character":character,
        "event_id":event_id,
        "refs":refs,
        "evidence":_evidence_for_refs(refs, support),
    }


def render_article3_preview(
    thread: dict[str, Any],
    *,
    root: Path | str = Path("."),
) -> dict[str, Any]:
    materialized = materialize_thread(thread, root=root)
    if materialized["thread_id"] != "CELEX:32004R0794#Article3:ENG":
        raise ValueError("Article 3 preview renderer received another Thread")
    if materialized["source_mode"]["gaps"]:
        raise ValueError("public preview requires complete Source Mode closure")

    entities = _entity_index(materialized)
    support = _support_index(thread, root=root)

    sani = entities["reg794-art3-sani-duty-v0.1"]
    pki = entities["reg794-art3-pki-correspondence-duty-v0.1"]
    alt = entities["reg794-art3-alt-channel-permission-v0.1"]
    invalid = entities["reg794-art3-invalid-channel-status-v0.1"]
    n2025 = entities["reg794-art3-2025-notification-channel-duty-v0.1"]
    c2025 = entities["reg794-art3-2025-correspondence-channel-duty-v0.1"]
    ripple = entities["reg794-art3-2025-crossref-exception-ripple-v0.1"]
    corr = entities["reg794-article3-corrigendum-scope-v0.1"]

    baseline_refs = [
        _ref("THREAD_EVIDENCE","reg794-article3-baseline-v0.1"),
        _ref("TEMPORAL_ASSERTION","reg794-art3-original-paper-notification-end"),
        _ref(
            "TEMPORAL_ASSERTION",
            "reg794-art3-original-electronic-notification-start",
        ),
        _ref(
            "TEMPORAL_ASSERTION",
            "reg794-art3-original-electronic-correspondence-trigger",
        ),
    ]
    channel_2008_refs = [
        _ref("CHANGE_ATOM","reg794-art3-sani-duty-v0.1"),
        _ref("CHANGE_ATOM","reg794-art3-pki-correspondence-duty-v0.1"),
    ]
    exception_refs = [
        _ref("CHANGE_ATOM","reg794-art3-alt-channel-permission-v0.1"),
        _ref("CHANGE_ATOM","reg794-art3-invalid-channel-status-v0.1"),
    ]
    channel_2025_refs = [
        _ref("CHANGE_ATOM","reg794-art3-2025-notification-channel-duty-v0.1"),
        _ref(
            "CHANGE_ATOM",
            "reg794-art3-2025-correspondence-channel-duty-v0.1",
        ),
        _ref(
            "TEMPORAL_ASSERTION",
            "reg794-art3-p3-2025-application-start",
        ),
    ]

    three_seconds = _item(
        text=(
            "Article 3 moved State-aid notification from a staged "
            "paper/electronic regime to named SANI and PKI channels in 2008, "
            "then to Commission-designated electronic systems in 2025; "
            "agreed alternatives remain exceptional."
        ),
        refs=baseline_refs + channel_2008_refs + [
            _ref("CHANGE_ATOM","reg794-art3-alt-channel-permission-v0.1"),
            _ref("CHANGE_ATOM","reg794-art3-2025-notification-channel-duty-v0.1"),
            _ref(
                "CHANGE_ATOM",
                "reg794-art3-2025-correspondence-channel-duty-v0.1",
            ),
        ],
        support=support,
        character="SYNTHESIS",
    )

    thirty_seconds = [
        _item(
            text=(
                "The original Article 3 used a staged transmission regime: "
                "paper notifications ran through 31 December 2005; electronic "
                "notification began on 1 January 2006; and the correspondence "
                "rule depends on when the connected notification was submitted."
            ),
            refs=baseline_refs,
            support=support,
            character="SYNTHESIS",
            event_id="original-article3-state",
        ),
        _item(
            text=f"{sani['claim']['statement']} {pki['claim']['statement']}",
            refs=channel_2008_refs,
            support=support,
            event_id="article3-replacement-2008",
        ),
        _item(
            text=f"{alt['claim']['statement']} {invalid['claim']['statement']}",
            refs=exception_refs,
            support=support,
            event_id="article3-replacement-2008",
        ),
        _item(
            text=f"{n2025['claim']['statement']} {c2025['claim']['statement']}",
            refs=channel_2025_refs,
            support=support,
            event_id="article3-paragraph3-replacement-2025",
        ),
        _item(
            text=(
                ripple["claim"]["statement"]
                + " Article 3(4) itself was not textually changed in 2025."
            ),
            refs=[
                _ref(
                    "CHANGE_ATOM",
                    "reg794-art3-2025-crossref-exception-ripple-v0.1",
                ),
                _ref(
                    "THREAD_EVIDENCE",
                    "reg794-article3-p4-2025-continuity-v0.1",
                ),
            ],
            support=support,
            character="DERIVED_WITH_NEGATIVE_TEXTUAL_CHECK",
            event_id="paragraph4-cross-reference-ripple-2025",
        ),
    ]

    three_minutes = [
        _item(
            text=(
                "The authentic 2004 act and the first consolidated checkpoint "
                "contain the same canonical Article 3 subtree. This is retained "
                "as baseline state, not fabricated as a later textual mutation."
            ),
            refs=[_ref("THREAD_EVIDENCE","reg794-article3-baseline-v0.1")],
            support=support,
            event_id="original-article3-state",
        ),
        _item(
            text=(
                "The Regulation entered into force on 20 May 2004. Chapter II "
                "applies only to notifications transmitted more than five "
                "months after entry into force, so the normalized 20 October "
                "boundary is exclusive."
            ),
            refs=[
                _ref("TEMPORAL_ASSERTION","reg794-2004-entry-into-force"),
                _ref(
                    "TEMPORAL_ASSERTION",
                    "reg794-2004-chapter2-application-threshold",
                ),
            ],
            support=support,
            event_id="chapter2-application-gate",
        ),
        thirty_seconds[0],
        _item(
            text=(
                "In 2008 the whole of Article 3 was replaced. "
                + sani["claim"]["statement"]
                + " "
                + pki["claim"]["statement"]
            ),
            refs=[
                _ref("MUTATION","reg794-article3-live-verified-v0.1"),
                *channel_2008_refs,
            ],
            support=support,
            event_id="article3-replacement-2008",
        ),
        thirty_seconds[2],
        _item(
            text=(
                "In 2025 Article 3(3), rather than the whole Article, was "
                "replaced. "
                + n2025["claim"]["statement"]
                + " "
                + c2025["claim"]["statement"]
            ),
            refs=[
                _ref(
                    "MUTATION",
                    "reg794-article3-p3-2025-live-verified-v0.1",
                ),
                *channel_2025_refs[:2],
            ],
            support=support,
            event_id="article3-paragraph3-replacement-2025",
        ),
        thirty_seconds[4],
        _item(
            text=(
                "The 2026 corrigendum was reviewed and excluded from the "
                "Article 3 mutation timeline. "
                + corr["thread_scope_result"]["rationale"]
            ),
            refs=[
                _ref(
                    "THREAD_EVIDENCE",
                    "reg794-article3-corrigendum-scope-v0.1",
                )
            ],
            support=support,
            event_id="corrigendum-review-2026",
        ),
    ]

    return {
        "schema_version":"thread-public-preview-v0.1",
        "thread_id":materialized["thread_id"],
        "language":"ENG",
        "source_mode":{
            "closed":True,
            "gap_count":0,
        },
        "layers":{
            "3_seconds":three_seconds,
            "30_seconds":thirty_seconds,
            "3_minutes":three_minutes,
        },
        "scope_notes":materialized["unknowns"],
    }


def render_preview_text(preview: dict[str, Any]) -> str:
    lines = [
        "Morrow // Needle — Article 3 Thread",
        "",
        "3 seconds",
        preview["layers"]["3_seconds"]["text"],
        "",
        "30 seconds",
    ]
    for item in preview["layers"]["30_seconds"]:
        lines.append(f"- {item['text']}")
    lines.extend(["", "3 minutes"])
    for item in preview["layers"]["3_minutes"]:
        lines.append(f"- {item['text']}")
    lines.extend([
        "",
        "Scope",
        "- English expression only.",
        "- Source Mode closed: every referenced factual legal claim has active provenance support.",
        "- Interpretive rule-lineage claims do not assert technical identity between named 2008 systems and 2025 Commission-designated systems.",
    ])
    return "\n".join(lines) + "\n"
