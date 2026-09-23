import json
from pathlib import Path


FIXTURE = json.loads(
    Path(
        "fixtures/discovery/"
        "reach-art33-nhexane-authoritative-set-membership-v0.1.json"
    ).read_text(encoding="utf-8")
)
SOURCE_CHANGE_SCHEMA = json.loads(
    Path("schemas/source-change-v0.1.schema.json").read_text(encoding="utf-8")
)
MUTATION_SCHEMA = json.loads(
    Path("schemas/mutation-candidate-v0.2.schema.json").read_text(
        encoding="utf-8"
    )
)
CHANGE_ATOM_SCHEMA = json.loads(
    Path("schemas/change-atom-v0.3.schema.json").read_text(encoding="utf-8")
)


def test_candidate_list_membership_changes_without_local_rule_mutation():
    rule = FIXTURE["governing_rule"]
    event = FIXTURE["membership_event"]
    effect = FIXTURE["derived_effect"]

    assert rule["provision"] == "Article 33"
    assert rule["textual_mutation_at_membership_event"] is None
    assert event["before"] == "NOT_INCLUDED"
    assert event["after"] == "INCLUDED"
    assert event["effective_date"] == "2026-02-04"
    assert effect["local_textual_mutation"] is False


def test_member_identity_is_stable_across_membership_transition():
    member = FIXTURE["member"]

    assert member["name"] == "n-hexane"
    assert member["ec_number"] == "203-777-6"
    assert member["cas_number"] == "110-54-3"
    assert member["identity_changed_at_event"] is False


def test_second_case_generalises_beyond_publication_gateway():
    comparison = FIXTURE["comparison_to_toy_case"]

    assert comparison["result"] == "DYNAMIC_PUBLICATION_GATEWAY_TOO_NARROW"
    assert "unchanged governing provision" in comparison["shared_shape"]
    assert "stable member identity" in comparison["shared_shape"]
    assert (
        "authoritative external set or status surface"
        in comparison["shared_shape"]
    )


def test_cellar_source_change_contract_cannot_own_echa_membership_state():
    required = set(SOURCE_CHANGE_SCHEMA["required"])
    target_enum = (
        SOURCE_CHANGE_SCHEMA["properties"]["refresh_scope"]["enum"]
    )

    assert "target_cellar_id" in required
    assert "root_cellar_id" in required
    assert all("ECHA" not in value for value in target_enum)
    assert FIXTURE["architecture_probe"]["source_change_v0_1_fit"] == (
        "FAILS_SOURCE_SCOPE"
    )


def test_mutation_evidence_has_no_authoritative_agency_register_channel():
    channels = (
        MUTATION_SCHEMA["$defs"]["evidence_ref"]["properties"]["channel"]["enum"]
    )

    assert "AUTHORITATIVE_OFFICIAL_REGISTER" not in channels
    assert "AUTHENTIC_AGENCY_LIST" not in channels
    assert FIXTURE["architecture_probe"]["mutation_candidate_v0_2_fit"] == (
        "FAILS_EVIDENCE_SEMANTICS"
    )


def test_change_atom_v0_3_requires_textual_mutation_cause():
    required = set(CHANGE_ATOM_SCHEMA["required"])
    source_mutation = CHANGE_ATOM_SCHEMA["properties"]["source_mutation_ids"]

    assert "source_mutation_ids" in required
    assert source_mutation["minItems"] == 1
    assert FIXTURE["architecture_probe"]["change_atom_v0_3_direct_fit"] == (
        "FAILS_TEXTUAL_MUTATION_CAUSE_REQUIREMENT"
    )


def test_architecture_probe_stops_before_patchwork():
    probe = FIXTURE["architecture_probe"]

    assert probe["required_concept"] == "AUTHORITATIVE_DYNAMIC_SET_TRANSITION"
    assert probe["dependency_character"] == (
        "DERIVED_FROM_AUTHORITATIVE_SET_STATE"
    )
    assert probe["decision"] == (
        "DO_NOT_PATCH_EXISTING_ENUMS; DEFINE_CAUSAL_OWNERSHIP_FIRST"
    )
