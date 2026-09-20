from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class DependencyRippleError(ValueError):
    pass


def _read_json(root: Path, path: str) -> dict[str, Any]:
    return json.loads((root / path).read_text(encoding="utf-8"))


def _continuity_state(
    fixture: dict[str, Any],
    continuity: dict[str, Any],
    *,
    side: str,
) -> dict[str, Any]:
    state=dict(continuity[side])
    if "state_id" not in state:
        transition=fixture.get("transition", {})
        state["state_id"]=transition.get(side)
    if not state.get("state_id"):
        raise DependencyRippleError(
            f"continuity {side} state lacks state_id"
        )
    state.setdefault("node_id",None)

    if "artifact_hash" not in state:
        observations=fixture.get("source_observations", {})
        observation=observations.get(side, {})
        state["artifact_hash"]=observation.get("artifact_hash")
    state.setdefault("artifact_hash",None)

    return {
        "state_id":state["state_id"],
        "node_id":state.get("node_id"),
        "text_hash":state["text_hash"],
        "text_length":state["text_length"],
        "artifact_hash":state.get("artifact_hash"),
    }


def _normalise_continuity(
    fixture: dict[str, Any],
    object_key: str,
) -> dict[str, Any]:
    continuity=fixture.get(object_key)
    if not isinstance(continuity,dict):
        raise DependencyRippleError(
            f"continuity object not found: {object_key}"
        )

    result=(
        continuity.get("continuity_result")
        or continuity.get("result")
    )
    if result != "IDENTICAL_CANONICAL_SUBTREE":
        raise DependencyRippleError(
            f"local provision is not canonically unchanged: {result}"
        )
    if continuity.get("textual_mutation") is not None:
        raise DependencyRippleError(
            "dependency ripple requires no local textual mutation"
        )

    before=_continuity_state(
        fixture,continuity,side="before"
    )
    after=_continuity_state(
        fixture,continuity,side="after"
    )
    if before["text_hash"] != after["text_hash"]:
        raise DependencyRippleError(
            "local continuity hashes differ"
        )
    if before["text_length"] != after["text_length"]:
        raise DependencyRippleError(
            "local continuity lengths differ"
        )

    return {
        "result":"IDENTICAL_CANONICAL_SUBTREE",
        "textual_mutation":None,
        "before":before,
        "after":after,
    }


def _normalise_mutation(
    mutation: dict[str, Any],
) -> dict[str, Any]:
    mutation_id=mutation.get("mutation_id") or mutation.get("candidate_id")
    result=mutation.get("result", {})
    operation=mutation.get("operation") or result.get("operation")
    verification=(
        mutation.get("verification_state")
        or result.get("verification_state")
    )
    target=mutation.get("target")
    if isinstance(target,dict):
        target=target.get("citation_path")

    if not mutation_id or not operation or not target:
        raise DependencyRippleError(
            "upstream mutation lacks canonical identity/operation/target"
        )
    if verification != "VERIFIED":
        raise DependencyRippleError(
            f"upstream mutation is not VERIFIED: {mutation_id}"
        )

    return {
        "mutation_id":mutation_id,
        "operation":operation,
        "target":target,
        "verification_state":"VERIFIED",
    }


def _find_atom(
    semantic: dict[str, Any],
    atom_id: str,
) -> dict[str, Any]:
    matches=[
        atom for atom in semantic.get("atoms", [])
        if atom.get("atom_id") == atom_id
    ]
    if len(matches) != 1:
        raise DependencyRippleError(
            f"expected one Change Atom {atom_id}, got {len(matches)}"
        )
    return matches[0]


def _derived_effect(
    atom: dict[str, Any],
    *,
    mutation: dict[str, Any],
) -> tuple[str,str,dict[str, Any],list[dict[str, Any]]]:
    if atom.get("verification_state") != "EVIDENCED":
        raise DependencyRippleError(
            "dependency-ripple atom must be EVIDENCED, not direct VERIFIED truth"
        )
    if atom.get("evidence_state") != "DERIVED":
        raise DependencyRippleError(
            "dependency-ripple atom must have DERIVED evidence_state"
        )
    dimensions=atom.get("claim",{}).get("dimensions",[])
    if "CROSS_REFERENCE" not in dimensions:
        raise DependencyRippleError(
            "dependency-ripple atom lacks CROSS_REFERENCE dimension"
        )
    if mutation["mutation_id"] not in atom.get("source_mutation_ids",[]):
        raise DependencyRippleError(
            "derived atom does not reference selected upstream mutation"
        )

    refs=atom.get("provision_refs",[])
    if len(refs) != 1:
        raise DependencyRippleError(
            "dependency-ripple v0.1 requires one local provision reference"
        )
    local=refs[0]["citation_path"]
    if local == mutation["target"]:
        raise DependencyRippleError(
            "local provision equals upstream mutation target; not a silent dependency ripple"
        )

    languages=atom.get("language_scope",{}).get("languages",[])
    if len(languages) != 1:
        raise DependencyRippleError(
            "dependency-ripple v0.1 requires one explicit expression language"
        )

    effect={
        "atom_id":atom["atom_id"],
        "verification_state":"EVIDENCED",
        "evidence_state":"DERIVED",
        "legal_effect":atom["claim"]["legal_effect"],
        "dimensions":list(dimensions),
        "statement":atom["claim"]["statement"],
    }

    anchors=[
        {
            "identifier":span["identifier"],
            "locator":span["locator"],
            "artifact_hash":span["artifact_hash"],
            "role":span["role"],
        }
        for span in atom.get("source_spans",[])
    ]
    if not anchors:
        raise DependencyRippleError(
            "dependency-ripple atom has no evidence anchors"
        )

    return local,languages[0],effect,anchors


def _non_implications(
    continuity_fixture: dict[str, Any],
    semantic_fixture: dict[str, Any],
) -> list[str]:
    values=[]
    values.extend(continuity_fixture.get("forbidden_inferences",[]))
    values.extend(continuity_fixture.get("negative_regressions",[]))
    values.extend(
        item["forbidden_inference"]
        for item in semantic_fixture.get("negative_atoms",[])
        if item.get("forbidden_inference")
    )
    if not values:
        values=[
            "Do not emit a local textual mutation from a derived dependency ripple."
        ]
    return list(dict.fromkeys(values))


def build_dependency_ripple_view(
    composition: dict[str, Any],
    *,
    root: Path | str = Path("."),
) -> dict[str, Any]:
    """Build Legislative X-Ray from existing mutation/semantic truth.

    The view owns no canonical mutation, semantic effect or dependency state.
    It only reconciles reference-selected evidence into a public projection.
    """
    root=Path(root)
    if composition.get("composition_character") != "REFERENCE_ONLY":
        raise DependencyRippleError(
            "dependency-ripple composition must be REFERENCE_ONLY"
        )

    cases=[]
    for spec in composition["cases"]:
        continuity_fixture=_read_json(
            root,spec["continuity_fixture_path"]
        )
        mutation_fixture=_read_json(
            root,spec["mutation_fixture_path"]
        )
        semantic_fixture=_read_json(
            root,spec["semantic_fixture_path"]
        )

        continuity=_normalise_continuity(
            continuity_fixture,
            spec["continuity_object_key"],
        )
        mutation=_normalise_mutation(mutation_fixture)
        atom=_find_atom(semantic_fixture,spec["atom_id"])
        local,language,effect,anchors=_derived_effect(
            atom,
            mutation=mutation,
        )

        cases.append({
            "case_id":spec["case_id"],
            "language":language,
            "local_provision":local,
            "local_continuity":continuity,
            "dependency":{
                "relation_character":(
                    "DERIVED_FROM_EVIDENCED_CROSS_REFERENCE_ATOM"
                ),
                "local_provision":local,
                "upstream_target":mutation["target"],
            },
            "upstream_change":mutation,
            "derived_effect":effect,
            "evidence_anchors":anchors,
            "non_implications":_non_implications(
                continuity_fixture,semantic_fixture
            ),
        })

    cases.sort(key=lambda item:item["case_id"])
    return {
        "schema_version":"dependency-ripple-view-v0.1",
        "analytic_id":composition["analytic_id"],
        "character":"DERIVED_VIEW",
        "cases":cases,
        "summary":{
            "case_count":len(cases),
            "verified_upstream_mutation_count":sum(
                item["upstream_change"]["verification_state"] == "VERIFIED"
                for item in cases
            ),
            "derived_local_effect_count":sum(
                item["derived_effect"]["evidence_state"] == "DERIVED"
                for item in cases
            ),
            "local_textual_mutation_count":0,
        },
        "guardrails":list(composition["guardrails"]),
    }


def render_dependency_ripple_text(view: dict[str, Any]) -> str:
    lines=[
        "Morrow // Needle — Legislative X-Ray",
        "",
        "3 seconds",
        (
            f"{view['summary']['case_count']} evidenced cases show legal effects "
            "changing through dependencies while the local provision text stays unchanged."
        ),
        "",
        "30 seconds",
    ]
    for case in view["cases"]:
        upstream=case["upstream_change"]
        effect=case["derived_effect"]
        lines.append(
            f"- {case['local_provision']}: local canonical text is unchanged; "
            f"{upstream['operation']} at {upstream['target']} is VERIFIED, while "
            f"the local effect is {effect['verification_state']} / "
            f"{effect['evidence_state']}. {effect['statement']}"
        )

    lines.extend([
        "",
        "Evidence model",
        "- A ripple requires identical before/after local subtree hashes.",
        "- The upstream textual mutation must be VERIFIED.",
        "- The local Change Atom must be EVIDENCED + DERIVED and explicitly CROSS_REFERENCE-scoped.",
        "- No local textual mutation is manufactured.",
        "- Legislative X-Ray is a derived view; canonical mutation and semantic truth stay in their owning contracts.",
    ])
    return "\n".join(lines)+"\n"



def emit_dependency_ripple_facts(
    composition: dict[str, Any],
    *,
    root: Path | str = Path("."),
) -> list[dict[str, Any]]:
    view=build_dependency_ripple_view(composition,root=root)
    facts=[]
    for case in view["cases"]:
        facts.append({
            "kind":"DEPENDENCY_RIPPLE",
            "case_id":case["case_id"],
            "language":case["language"],
            "local_provision":case["local_provision"],
            "local_textual_mutation":False,
            "local_continuity_result":case["local_continuity"]["result"],
            "upstream_mutation":case["upstream_change"],
            "derived_effect":case["derived_effect"],
            "dependency":case["dependency"],
        })
    facts.append({
        "kind":"DEPENDENCY_RIPPLE_SUMMARY",
        **view["summary"],
    })
    return facts
