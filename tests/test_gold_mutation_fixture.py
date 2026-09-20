import json
from pathlib import Path

from needle.gold import compare_expectations


CASE = json.loads(
    Path("fixtures/gold/reg794-article3-verified-mutation-v0.1.json").read_text(
        encoding="utf-8"
    )
)
LIVE = json.loads(
    Path("fixtures/mutations/reg794-article3-live-verified-v0.1.json").read_text(
        encoding="utf-8"
    )
)


def emitted_facts():
    result = LIVE["result"]
    instruction = LIVE["authentic_amending_act"]["instruction"]
    return [
        {
            "kind":"TEXTUAL_MUTATION",
            "operation":instruction["operation"],
            "target":instruction["target_locator"],
            "language":LIVE["language"],
            "reconciliation_state":result["reconciliation_state"],
            "verification_state":result["verification_state"],
            "authentic_cause":"CELEX:" + LIVE["authentic_amending_act"]["celex"],
            "source_mutation":LIVE["case_id"],
            "before_hash":LIVE["before_checkpoint"]["article3"]["text_hash"],
            "after_hash":LIVE["after_checkpoint"]["article3"]["text_hash"],
        }
    ]


def test_live_verified_mutation_satisfies_gold_contract():
    assert compare_expectations(CASE["machine_expectations"], emitted_facts()) == []


def test_gold_contract_would_reject_premature_semantic_atom():
    emitted = emitted_facts() + [
        {
            "kind":"CHANGE_ATOM",
            "source_mutation":"reg794-article3-live-verified-v0.1",
            "legal_effect":"DUTY",
        }
    ]
    errors = compare_expectations(CASE["machine_expectations"], emitted)
    assert errors == [
        "nonatom.semantic-effect: forbidden fact was emitted"
    ]
