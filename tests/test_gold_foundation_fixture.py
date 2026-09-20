import json
from pathlib import Path

from needle.gold import compare_expectations

ROOT = Path(__file__).resolve().parents[1]


def test_reg26_lineage_fixture_satisfies_gold_machine_contract():
    """Exercise evidence fixture -> normalized emissions -> Gold expectations.

    This deliberately uses the established lower-level lineage fixture rather than
    hand-writing emitted facts in the test. A regression in its normalized mapping
    (for example old Article 3 -> new Article 3) therefore violates the Gold case.
    """
    lineage = json.loads((ROOT / "fixtures/lineage/reg26-to-reg1184-v0.1.json").read_text())
    gold = json.loads((ROOT / "fixtures/gold/reg26-to-reg1184-lineage-v0.1.json").read_text())

    emitted = [
        {
            "kind": "STRUCTURAL_LINEAGE",
            "source": mapping["source"],
            "target": mapping["target"],
            "status": "ASSERTED",
            "operation": mapping["classification"],
            "provenance": {"basis": "OFFICIAL_CORRELATION_TABLE"},
        }
        for mapping in lineage["mappings"]
        if mapping["source"] is not None and mapping["target"] is not None
    ]

    assert compare_expectations(gold["machine_expectations"], emitted) == []
