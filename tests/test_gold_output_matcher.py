from needle.gold import compare_expectations


def test_partial_present_match_allows_extra_provenance():
    expectations = [{
        "assertion_id": "lineage.old7.new4",
        "outcome": "PRESENT",
        "match": {"kind": "STRUCTURAL_LINEAGE", "source": "old:7", "target": "new:4"},
    }]
    emitted = [{
        "kind": "STRUCTURAL_LINEAGE", "source": "old:7", "target": "new:4",
        "confidence": "HIGH", "evidence": ["official-correlation-table"],
    }]
    assert compare_expectations(expectations, emitted) == []


def test_missing_required_fact_fails():
    expectations = [{"assertion_id": "required", "outcome": "PRESENT", "match": {"kind": "MOVE"}}]
    assert compare_expectations(expectations, []) == ["required: required fact was not emitted"]


def test_forbidden_inference_fails_when_emitted():
    expectations = [{
        "assertion_id": "no.rule.continuity",
        "outcome": "ABSENT",
        "match": {"kind": "RULE_LINEAGE", "status": "ASSERTED"},
    }]
    emitted = [{"kind": "RULE_LINEAGE", "status": "ASSERTED", "source": "old:7", "target": "new:7"}]
    assert compare_expectations(expectations, emitted) == ["no.rule.continuity: forbidden fact was emitted"]


def test_forbidden_inference_passes_when_absent():
    expectations = [{
        "assertion_id": "no.rule.continuity",
        "outcome": "ABSENT",
        "match": {"kind": "RULE_LINEAGE", "status": "ASSERTED"},
    }]
    emitted = [{"kind": "STRUCTURAL_LINEAGE", "status": "ASSERTED"}]
    assert compare_expectations(expectations, emitted) == []


def test_nested_partial_match():
    expectations = [{
        "assertion_id": "nested",
        "outcome": "PRESENT",
        "match": {"provenance": {"authority": "EUR_LEX"}},
    }]
    emitted = [{"provenance": {"authority": "EUR_LEX", "celex": "32006R1184"}}]
    assert compare_expectations(expectations, emitted) == []
