from __future__ import annotations

import hashlib
import re
from typing import Any

from needle.mutation.instructions import (
    candidate_from_authentic_instruction,
    parse_authentic_keyed_row_insertions,
)


_ANNEX_AMENDMENT_RE = re.compile(
    r"\bAnnex\s+(?P<annex>[IVXLC]+)\b\s+is\s+amended"
    r"(?:\s+as\s+follows)?\s*:",
    re.IGNORECASE,
)


def _nearest_amended_annex(
    text: str,
    instruction_start: int,
) -> str | None:
    """Resolve only an explicit preceding Annex amendment heading.

    A bare Annex mention is contextual prose, not an authentic amendment
    command. Requiring the local "is amended" heading prevents quoted,
    explanatory, or recital-like text from being promoted merely because an
    amendment-shaped sentence appears later in the same flattened document.
    """
    matches=list(
        _ANNEX_AMENDMENT_RE.finditer(text,0,instruction_start)
    )
    if not matches:
        return None
    return f"Annex {matches[-1].group('annex').upper()}"


def _semantic_mutation_id(*, source_id: str, language: str, operation: str, target: str) -> str:
    """Identity for the legal mutation, excluding observation-local provenance."""
    material="|".join([source_id, language.lower(), operation, target])
    return f"authentic-mutation:{hashlib.sha256(material.encode('utf-8')).hexdigest()[:20]}"


def candidates_from_authentic_text(
    event: dict[str, Any],
    text: str,
    *,
    source_id: str,
    locator: str | None = None,
    language: str = "eng",
    evidence_ref: str | None = None,
) -> list[dict[str, Any]]:
    """Produce bounded operational candidates from explicit authentic commands.

    ``source_id`` is the stable legal-source identity (for example CELEX), while
    ``evidence_ref`` may point at the immutable observation that supplied these
    bytes. Keeping those identities separate makes repeated observations
    idempotent without sacrificing provenance. Parser families are drafting-
    pattern capabilities, never CELEX dispatch. Unsupported forms return no
    candidate and therefore preserve abstention.
    """
    normalized=" ".join(text.split())
    provisional=parse_authentic_keyed_row_insertions(
        normalized,
        source_id=source_id,
        parent_locator="__UNRESOLVED_ANNEX__",
        locator=locator,
    )
    output=[]
    search_from=0
    for item in provisional:
        instruction=item["instruction_text"]
        start=normalized.find(instruction, search_from)
        if start < 0:
            continue
        search_from=start+len(instruction)
        annex=_nearest_amended_annex(normalized,start)
        if annex is None:
            continue
        parsed=parse_authentic_keyed_row_insertions(
            instruction,
            source_id=source_id,
            parent_locator=annex,
            locator=locator,
        )
        if len(parsed) != 1:
            continue
        canonical=parsed[0]
        mutation=candidate_from_authentic_instruction(
            canonical,
            kind="TABLE_ROWS",
            language=language,
            candidate_id=_semantic_mutation_id(
                source_id=source_id,
                language=language,
                operation=canonical["operation"],
                target=canonical["target_locator"],
            ),
        )
        semantic_key=(
            f"{source_id}|{language.lower()}|{mutation['operation']}|"
            f"{mutation['target']['citation_path']}|"
            f"{','.join(canonical.get('inserted_keys',[]))}"
        )
        output.append({
            "semantic_key":semantic_key,
            "outcome":"LEGAL_CHANGE_VERIFIED",
            "verification_route":"AUTHENTIC_LEGAL_CAUSE",
            "canonical_refs":[{
                "kind":"MUTATION",
                "entity_id":mutation["candidate_id"],
            }],
            "evidence_refs":[evidence_ref or source_id],
            "evidence_occurrences":[{
                "locator":locator,
                "instruction_text":canonical["instruction_text"],
            }],
            "explanation":{
                "what_changed":(
                    f"{mutation['target']['citation_path']}: "
                    f"{canonical['instruction_text']}"
                ),
                "compared_with":(
                    "The placement anchor named by the authentic amendment; "
                    "no source-state comparator is implied."
                ),
                "when_it_matters":(
                    "Legal change is verified from the authentic amendment; "
                    "temporal applicability requires canonical temporal analysis."
                ),
                "affected":[],
                "evidence_character":"DIRECT",
            },
            "unknowns":[
                "Affected entities are not inferred from drafting text by the operational adapter.",
                "Temporal applicability is not inferred by the operational adapter.",
            ],
        })
    return output


def _compose_authentic_delivery_candidate(
    candidates: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Group multiple explicit mutations from one authentic observation.

    This is delivery composition, not truth collapse: every canonical mutation
    ref remains separate. Grouping is allowed only when every child is a
    VERIFIED authentic-cause outcome supported by the same immutable source
    observation. Otherwise the children remain separate and the downstream
    analyzer preserves its ambiguity abstention.
    """
    if len(candidates) <= 1:
        return candidates
    if any(
        item.get("outcome") != "LEGAL_CHANGE_VERIFIED"
        or item.get("verification_route") != "AUTHENTIC_LEGAL_CAUSE"
        for item in candidates
    ):
        return candidates

    evidence_sets={
        tuple(sorted(item.get("evidence_refs",[])))
        for item in candidates
    }
    if len(evidence_sets) != 1:
        return candidates

    child_keys=sorted(item["semantic_key"] for item in candidates)
    canonical_refs=[]
    occurrences=[]
    affected=[]
    unknowns=[]
    descriptions=[]
    evidence_character="DIRECT"
    for item in sorted(candidates,key=lambda value:value["semantic_key"]):
        for ref in item.get("canonical_refs",[]):
            if ref not in canonical_refs:
                canonical_refs.append(ref)
        for occurrence in item.get("evidence_occurrences",[]):
            tagged={
                **occurrence,
                "semantic_key":item["semantic_key"],
            }
            if tagged not in occurrences:
                occurrences.append(tagged)
        explanation=item.get("explanation") or {}
        changed=explanation.get("what_changed")
        if changed and changed not in descriptions:
            descriptions.append(changed)
        for value in explanation.get("affected",[]):
            if value not in affected:
                affected.append(value)
        if explanation.get("evidence_character") != "DIRECT":
            evidence_character="MIXED"
        for value in item.get("unknowns",[]):
            if value not in unknowns:
                unknowns.append(value)

    semantic_material="\n".join(child_keys)
    semantic_key=(
        "authentic-compound:"
        +hashlib.sha256(semantic_material.encode("utf-8")).hexdigest()[:24]
    )
    unknowns.append(
        "Multiple explicit mutations from the same authentic act are grouped "
        "for operational delivery; their canonical mutation identities remain "
        "separate."
    )
    return [{
        "semantic_key":semantic_key,
        "outcome":"LEGAL_CHANGE_VERIFIED",
        "verification_route":"AUTHENTIC_LEGAL_CAUSE",
        "canonical_refs":canonical_refs,
        "evidence_refs":list(next(iter(evidence_sets))),
        "evidence_occurrences":occurrences,
        "explanation":{
            "what_changed":(
                f"{len(canonical_refs)} explicit amendments were verified in "
                "the authentic act: "+" | ".join(descriptions)
            ),
            "compared_with":(
                "Each amendment is compared with the placement anchor named "
                "by its authentic instruction; no source-state comparator is "
                "implied."
            ),
            "when_it_matters":(
                "Legal changes are verified from the authentic amendment; "
                "temporal applicability requires canonical temporal analysis."
            ),
            "affected":affected,
            "evidence_character":evidence_character,
        },
        "unknowns":unknowns,
    }]


def candidates_from_reobservation(
    event: dict[str, Any],
    reobservation: dict[str, Any],
) -> list[dict[str, Any]]:
    """Produce legal-analysis candidates from one sealed official re-observation.

    This adapter only bridges operational transport into canonical analyzers. It
    does not infer recency, applicability, affected entities, or legal effect
    from a Cellar notification. Missing deterministic analysis text or missing
    immutable content provenance yields no candidate and therefore abstention.
    """
    text=reobservation.get("analysis_text")
    celex=reobservation.get("celex")
    content_observation=reobservation.get("content_observation")
    if not text or not celex or not content_observation:
        return []
    evidence_ref=content_observation.get("record_id")
    if not evidence_ref:
        return []

    payload=content_observation.get("payload",{})
    retrieval=payload.get("retrieval",{})
    language=(
        reobservation.get("analysis_language")
        or payload.get("language")
        or "eng"
    )
    source_id=str(celex)
    if not source_id.upper().startswith("CELEX:"):
        source_id=f"CELEX:{source_id}"

    candidates=candidates_from_authentic_text(
        event,
        text,
        source_id=source_id,
        locator=retrieval.get("final_uri"),
        language=str(language).lower(),
        evidence_ref=evidence_ref,
    )
    return _compose_authentic_delivery_candidate(candidates)
