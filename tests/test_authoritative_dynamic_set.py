import json
from pathlib import Path

from jsonschema import Draft202012Validator


SCHEMA = json.loads(
    Path("schemas/authoritative-dynamic-set-v0.1.schema.json").read_text(
        encoding="utf-8"
    )
)
TOY = json.loads(
    Path(
        "fixtures/dependency/"
        "toy-safety-authoritative-dynamic-set-v0.1.json"
    ).read_text(encoding="utf-8")
)
REACH = json.loads(
    Path(
        "fixtures/dependency/"
        "reach-candidate-list-authoritative-dynamic-set-v0.1.json"
    ).read_text(encoding="utf-8")
)
GAR = json.loads(
    Path(
        "fixtures/dependency/"
        "gar-en497-authoritative-dynamic-set-v0.1.json"
    ).read_text(encoding="utf-8")
)
LVD_WITHDRAWAL = json.loads(
    Path(
        "fixtures/dependency/"
        "lvd-en60335-2-60-scheduled-withdrawal-v0.1.json"
    ).read_text(encoding="utf-8")
)
MACHINERY_RESTRICTION = json.loads(
    Path(
        "fixtures/dependency/"
        "machinery-en50434-restriction-v0.1.json"
    ).read_text(encoding="utf-8")
)
LVD_NONPUBLICATION = json.loads(
    Path(
        "fixtures/dependency/"
        "lvd-en60335-2-14-nonpublication-v0.1.json"
    ).read_text(encoding="utf-8")
)


def validate(document):
    return list(Draft202012Validator(SCHEMA).iter_errors(document))


def test_three_orthogonal_cases_fit_same_canonical_contract():
    assert validate(TOY) == []
    assert validate(REACH) == []
    assert validate(GAR) == []
    assert validate(LVD_WITHDRAWAL) == []
    assert validate(MACHINERY_RESTRICTION) == []
    assert validate(LVD_NONPUBLICATION) == []
    assert (
        TOY["set_character"]
        == REACH["set_character"]
        == GAR["set_character"]
        == LVD_WITHDRAWAL["set_character"]
        == MACHINERY_RESTRICTION["set_character"]
        == LVD_NONPUBLICATION["set_character"]
        == "AUTHORITATIVE_DYNAMIC_SET"
    )


def test_contract_keeps_authority_surface_explicit():
    assert TOY["publication_surface"]["surface_type"] == "OFFICIAL_JOURNAL"
    assert REACH["publication_surface"]["surface_type"] == (
        "OFFICIAL_AUTHORITY_WEBSITE"
    )
    assert TOY["authority"]["authority_type"] == "EU_INSTITUTION"
    assert REACH["authority"]["authority_type"] == "EU_AGENCY"


def test_same_dependency_character_covers_two_different_legal_mechanisms():
    toy_dependency = TOY["dependencies"][0]
    reach_dependency = REACH["dependencies"][0]

    expected = "LEGAL_EFFECT_CONDITIONED_ON_AUTHORITATIVE_SET_STATE"
    assert toy_dependency["relation_character"] == expected
    assert reach_dependency["relation_character"] == expected

    assert toy_dependency["governing_rule"]["provision"] == "Article 13"
    assert reach_dependency["governing_rule"]["provision"] == "Article 33"


def test_toy_case_is_status_restriction_not_member_replacement():
    transition = TOY["transitions"][0]

    assert transition["operation"] == "RESTRICT_MEMBER"
    assert transition["member"]["identifiers"] == [
        {
            "scheme": "HARMONISED_STANDARD",
            "value": "EN 71-1:2014+A1:2018",
        }
    ]
    assert transition["before"]["membership"] == "INCLUDED"
    assert transition["after"]["membership"] == "INCLUDED"
    assert transition["after"]["status"] == "RESTRICTED"
    assert transition["scope"]["character"] == "PARTIAL_MEMBER"


def test_reach_case_is_membership_addition_not_statutory_mutation():
    transition = REACH["transitions"][0]

    assert transition["operation"] == "ADD_MEMBER"
    assert transition["before"]["membership"] == "NOT_INCLUDED"
    assert transition["after"]["membership"] == "INCLUDED"
    assert transition["effective_from"] == "2026-02-04"
    assert transition["scope"]["character"] == "FULL_MEMBER"


def test_direct_set_state_and_derived_local_effect_remain_separable():
    for document in (TOY, REACH):
        assert document["transitions"][0]["evidence_state"] == "DIRECT"
        assert document["dependencies"][0]["evidence_state"] == "DIRECT"
        encoded = json.dumps(document, sort_keys=True)
        assert "local_textual_mutation" not in encoded
        assert "source_mutation_ids" not in encoded
        assert "derived_effect" not in encoded


def test_contract_does_not_become_generic_dependency_graph():
    allowed = set(SCHEMA["properties"])
    assert "nodes" not in allowed
    assert "edges" not in allowed
    assert "graph" not in allowed
    assert "transitions" in allowed
    assert "dependencies" in allowed


def test_operation_specific_constraints_reject_false_addition():
    bad = json.loads(json.dumps(REACH))
    bad["transitions"][0]["before"]["membership"] = "INCLUDED"

    errors = validate(bad)
    assert errors
    assert any(
        error.validator == "const" and error.validator_value == "NOT_INCLUDED"
        for error in errors
    )


def test_operation_specific_constraints_reject_false_restriction():
    bad = json.loads(json.dumps(TOY))
    bad["transitions"][0]["after"]["membership"] = "NOT_INCLUDED"

    errors = validate(bad)
    assert errors
    assert any(
        error.validator == "const" and error.validator_value == "INCLUDED"
        for error in errors
    )


def test_gar_case_preserves_formal_nonpublication_without_fake_membership():
    transition = GAR["transitions"][0]

    assert transition["operation"] == "STATUS_CHANGE"
    assert transition["member"]["identifiers"] == [
        {"scheme": "HARMONISED_STANDARD", "value": "EN 497:2022"}
    ]
    assert transition["before"]["membership"] == "NOT_INCLUDED"
    assert transition["after"]["membership"] == "NOT_INCLUDED"
    assert transition["effective_from"] == "2026-07-24"
    assert "does not acquire Article 13 presumption-of-conformity status" in (
        transition["scope"]["statement"]
    )


def test_gar_case_does_not_infer_standard_is_forbidden():
    forbidden = GAR["forbidden_inferences"]

    assert any("alternative conformity route" in item for item in forbidden)
    assert any("standards organisation" in item for item in forbidden)


def test_lvd_case_preserves_future_withdrawal_effective_date():
    transition = LVD_WITHDRAWAL["transitions"][0]

    assert transition["operation"] == "REMOVE_MEMBER"
    assert transition["before"]["membership"] == "INCLUDED"
    assert transition["after"]["membership"] == "NOT_INCLUDED"
    assert transition["after"]["status"] == "WITHDRAWN"
    assert transition["effective_from"] == "2027-01-18"


def test_machinery_case_preserves_scoped_restriction():
    transition = MACHINERY_RESTRICTION["transitions"][0]

    assert transition["operation"] == "RESTRICT_MEMBER"
    assert transition["before"]["membership"] == "INCLUDED"
    assert transition["after"]["membership"] == "INCLUDED"
    assert transition["after"]["status"] == "RESTRICTED"
    assert transition["effective_from"] == "2026-01-13"
    assert transition["scope"]["character"] == "PARTIAL_MEMBER"
    assert "300" in transition["scope"]["statement"]


def test_lvd_nonpublication_keeps_nonmembership_but_changes_owning_reason():
    transition = LVD_NONPUBLICATION["transitions"][0]

    assert transition["operation"] == "STATUS_CHANGE"
    assert transition["before"]["membership"] == "NOT_INCLUDED"
    assert transition["after"]["membership"] == "NOT_INCLUDED"
    assert transition["effective_from"] == "2025-07-18"
    assert "already not been included" in transition["scope"]["statement"]
