from __future__ import annotations

import re
from typing import Any

from needle.mutation.instructions import (
    candidate_from_authentic_instruction,
    parse_authentic_keyed_row_insertions,
)


_ANNEX_RE = re.compile(r"\bAnnex\s+([IVXLC]+)\b", re.IGNORECASE)


def _nearest_annex(text: str, instruction_start: int) -> str | None:
    """Resolve an explicit preceding Annex label; never guess one.

    This is deliberately a source-local structural aid, not legal identity.
    If the authentic text does not expose an Annex label before the command,
    the producer abstains from this parser family.
    """
    matches=list(_ANNEX_RE.finditer(text, 0, instruction_start))
    if not matches:
        return None
    return f"Annex {matches[-1].group(1).upper()}"


def candidates_from_authentic_text(
    event: dict[str, Any],
    text: str,
    *,
    source_id: str,
    locator: str | None = None,
) -> list[dict[str, Any]]:
    """Produce bounded operational candidates from explicit authentic commands.

    Parser families are drafting-pattern capabilities, never CELEX dispatch.
    Unsupported forms return no candidate and therefore preserve abstention.
    """
    normalized=" ".join(text.split())
    # The keyed-row parser needs a parent locator. Discover candidate commands
    # first with a sentinel, then require an explicit Annex in preceding source.
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
        annex=_nearest_annex(normalized,start)
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
            language="eng",
        )
        semantic_key=(
            f"{source_id}|{mutation['operation']}|"
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
            "evidence_refs":[source_id],
            "evidence_occurrences":[{
                "locator":locator,
                "instruction_text":canonical["instruction_text"],
            }],
            "explanation":{
                "what_changed":canonical["instruction_text"],
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
