import json
from pathlib import Path

from jsonschema import Draft202012Validator


FIXTURE = json.loads(
    Path(
        "fixtures/discovery/toy-wave-roller-dynamic-standard-gateway-v0.1.json"
    ).read_text(encoding="utf-8")
)
VIEW_SCHEMA = json.loads(
    Path("schemas/dependency-ripple-view-v0.1.schema.json").read_text(
        encoding="utf-8"
    )
)


def test_local_gateway_text_and_standard_identity_remain_stable():
    gateway = FIXTURE["local_gateway"]
    standard = FIXTURE["standard_identity"]

    assert gateway["textual_mutation_at_2025_transition"] is None
    assert standard["identifier"] == "EN 71-1:2014+A1:2018"
    assert standard["identifier_changed_at_2025_transition"] is False


def test_reference_status_changes_for_same_standard_identifier():
    before, after = FIXTURE["reference_states"]

    assert before["reference"] == after["reference"]
    assert before["wave_roller_restriction"] is None
    assert after["wave_roller_restriction"]["standard_clauses"] == [
        "3.19",
        "4.15.1",
    ]
    assert after["wave_roller_restriction"]["effect"] == (
        "NO_PRESUMPTION_OF_CONFORMITY_FOR_SPECIFIED_SCOPE"
    )
    assert before["presumption_status_for_wave_roller_clauses"] != (
        after["presumption_status_for_wave_roller_clauses"]
    )


def test_upstream_change_is_not_laundered_into_local_text_mutation():
    upstream = FIXTURE["upstream_legal_change"]
    local = FIXTURE["derived_local_effect"]

    assert upstream["act_id"] == "CELEX:32025D1785"
    assert upstream["operation"] == "REPLACE"
    assert local["local_textual_mutation"] is False
    assert local["effect_state"] == "DERIVED"


def test_v0_1_relation_vocabulary_cannot_express_dynamic_gateway():
    dependency_schema = (
        VIEW_SCHEMA["$defs"]["case"]["properties"]["dependency"]["properties"]
        ["relation_character"]
    )
    required = FIXTURE["architecture_probe"]["required_honest_relation_character"]

    assert dependency_schema["const"] == (
        "DERIVED_FROM_EVIDENCED_CROSS_REFERENCE_ATOM"
    )
    assert required == "DERIVED_FROM_DYNAMIC_PUBLICATION_GATEWAY"
    assert required != dependency_schema["const"]


def test_full_v0_1_view_rejects_honest_dynamic_relation():
    h = FIXTURE["local_gateway"]["text_hash"]
    candidate = {
        "schema_version": "dependency-ripple-view-v0.1",
        "analytic_id": "discovery:toy-wave-roller-dynamic-gateway",
        "character": "DERIVED_VIEW",
        "cases": [{
            "case_id": "toy-wave-roller-dynamic-gateway",
            "language": "ENG",
            "local_provision": "Directive 2009/48/EC Article 13",
            "local_continuity": {
                "result": "IDENTICAL_CANONICAL_SUBTREE",
                "textual_mutation": None,
                "before": {"state_id": "pre", "text_hash": h, "text_length": 303},
                "after": {"state_id": "post", "text_hash": h, "text_length": 303},
            },
            "dependency": {
                "relation_character": "DERIVED_FROM_DYNAMIC_PUBLICATION_GATEWAY",
                "local_provision": "Directive 2009/48/EC Article 13",
                "upstream_target": "Implementing Decision 2023/740 > Annex > row 1",
            },
            "upstream_change": {
                "mutation_id": "toy-wave-roller-reference-restriction-2025",
                "operation": "REPLACE",
                "target": "Implementing Decision 2023/740 > Annex > row 1",
                "verification_state": "VERIFIED",
            },
            "derived_effect": {
                "atom_id": "toy-art13-wave-roller-gateway-ripple",
                "verification_state": "EVIDENCED",
                "evidence_state": "DERIVED",
                "legal_effect": "LEGAL_STATUS",
                "dimensions": ["VALIDITY_CONDITION", "CROSS_REFERENCE"],
                "statement": "Published-reference restriction narrows the Article 13 presumption.",
            },
            "evidence_anchors": [{
                "identifier": "CELEX:32025D1785",
                "locator": "Annex",
                "artifact_hash": "sha256:" + "0" * 64,
                "role": "CONTEXT",
            }],
            "non_implications": ["Do not manufacture an Article 13 textual mutation."],
        }],
        "summary": {
            "case_count": 2,
            "verified_upstream_mutation_count": 1,
            "derived_local_effect_count": 1,
            "local_textual_mutation_count": 0,
        },
        "guardrails": ["Fail closed on unsupported dependency relation types."],
    }

    errors = list(Draft202012Validator(VIEW_SCHEMA).iter_errors(candidate))
    assert errors
    assert any(
        "DERIVED_FROM_EVIDENCED_CROSS_REFERENCE_ATOM" in error.message
        for error in errors
    )


def test_discovery_hits_reopen_rule_without_adding_schema_yet():
    probe = FIXTURE["architecture_probe"]

    assert probe["result"] == "REPRESENTATIONAL_FAILURE_REOPEN_TRIGGERED"
    assert probe["new_schema_added_in_this_probe"] is False
