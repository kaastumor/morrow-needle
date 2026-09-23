import json
from pathlib import Path


PRIVATE_RATING = json.loads(
    Path(
        "fixtures/discovery/capri-sp-private-rating-regulatory-input-v0.1.json"
    ).read_text(encoding="utf-8")
)
NOTIFIED_BODY = json.loads(
    Path(
        "fixtures/discovery/"
        "biotrh-szutest-private-notified-body-determination-v0.1.json"
    ).read_text(encoding="utf-8")
)


def test_named_private_notified_body_transitions_are_pinned():
    determination = NOTIFIED_BODY["private_determination"]
    transitions = determination["transitions"]

    assert determination["originator"]["name"] == (
        "SZUTEST Uygunluk Değerlendirme A.Ş."
    )
    assert determination["originator"]["notified_body_number"] == "2195"
    assert transitions[0] == {
        "date": "2023-03-23",
        "operation": "SUSPEND_CERTIFICATE",
        "before": "ACTIVE",
        "after": "SUSPENDED",
        "direct_source_statement": (
            "The manufacturer was informed by Notified Body SZUTEST, NB 2195, "
            "about suspension of the CE certificate."
        ),
    }
    assert transitions[1]["date"] == "2023-05-02"
    assert transitions[1]["operation"] == "WITHDRAW_CERTIFICATE"
    assert transitions[1]["after"] == "WITHDRAWN"


def test_private_decision_and_public_authority_action_remain_distinct():
    downstream = NOTIFIED_BODY["observed_downstream_effect"]

    assert "later regulatory action is distinct" in (
        downstream["field_safety_action"].casefold()
    )
    assert "appealed" in downstream["appeal"].casefold()
    assert "do not collapse" in downstream["guardrail"].casefold()


def test_two_domains_confirm_recognition_relationship_pattern():
    comparison = NOTIFIED_BODY["comparison_to_private_rating"]

    assert comparison["result"] == (
        "LEGALLY_RECOGNIZED_PRIVATE_DETERMINATION_PATTERN_CONFIRMED"
    )
    assert (
        "private source provenance must remain private rather than being "
        "relabelled official"
        in comparison["shared_shape"]
    )
    assert PRIVATE_RATING["architecture_probe"]["result"] == (
        "LEGALLY_RECOGNIZED_PRIVATE_ORIGIN_GAP_PINNED"
    )


def test_second_case_earns_repair_without_choosing_schema_yet():
    probe = NOTIFIED_BODY["architecture_probe"]

    assert probe["result"] == "SECOND_ORTHOGONAL_CASE_JUSTIFIES_REPAIR"
    assert probe["new_schema_added_in_this_probe"] is False
    assert probe["private_authority_as_other_official"] == (
        "REJECTED_AS_FALSE_PROVENANCE"
    )
    assert "separate source origin from legal recognition" in (
        probe["recommended_architecture_direction"]
    )
