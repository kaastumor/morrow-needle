import json
from pathlib import Path

from needle.identity.resolver import TypedIdentifierGraph
from needle.multilingual.mutations import (
    correction_chain_for_language,
    events_for_language,
)
from needle.procedure.resolver import state_as_of
from needle.provenance.ledger import active_records
from needle.temporal.resolver import gap_between
from needle.thread.composer import resolve_thread_references, source_mode_gaps
from needle.updates.classify import classify_source_change


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


LINEAGE_GAP = load(
    "fixtures/lineage/reg2021-1232-to-reg2026-1881-gap-v0.1.json"
)
LINEAGE_SPLIT = load(
    "fixtures/lineage/dir69-335-to-dir2008-7-split-v0.1.json"
)
CORR = load(
    "fixtures/multilingual/reg794-2004-corrigenda-language-scope-v0.1.json"
)
MONEY_CORR = load(
    "fixtures/multilingual/reg2742-1990-english-money-corrigendum-v0.1.json"
)
BACKPROJECTION = load(
    "fixtures/multilingual/reg794-2004-consolidation-backprojection-v0.1.json"
)
IDENTITY = load("fixtures/identity/eu-identifier-adversaries-v0.1.json")
PROCEDURE = load("fixtures/procedure/procedure-state-adversaries-v0.1.json")
SOURCE_CHANGE = load("fixtures/updates/source-change-adversaries-v0.1.json")
AST_ACCOUNTING = load("fixtures/ast/source-accounting-closed-v0.2.json")
LEDGER = load("fixtures/provenance/reg794-article3-dag-v0.1.json")
THREAD = load("fixtures/thread/reg794-article3-thread-v0.1.json")
GOLD_THREAD = load("fixtures/gold/reg794-article3-thread-v0.1.json")

SEMANTIC_FIXTURES = [
    load("fixtures/semantic/reg794-article3-atoms-v0.1.json"),
    load("fixtures/semantic/reg794-article3-2025-atoms-v0.1.json"),
]
TEMPORAL_FIXTURES = [
    load("fixtures/temporal/reg794-article3-original-v0.1.json"),
    load("fixtures/temporal/reg794-article3-sani-v0.1.json"),
    load("fixtures/temporal/reg794-article3-2025-v0.1.json"),
]


def _procedure_case(case_id):
    return next(case for case in PROCEDURE["cases"] if case["case_id"] == case_id)


def test_audit_lineage_genealogy_does_not_erase_temporal_gap():
    result = gap_between(
        LINEAGE_GAP["source_regime"]["application_end"],
        LINEAGE_GAP["target_regime"]["application_start"],
    )
    assert result == {
        "state":"GAP",
        "start":"2026-04-04",
        "end":"2026-07-30",
    }
    assert result["start"] == LINEAGE_GAP["edge"]["gap"]["start"]
    assert result["end"] == LINEAGE_GAP["edge"]["gap"]["end"]
    assert LINEAGE_GAP["edge"]["applicability_continuity"] == "GAPPED"


def test_audit_structural_split_does_not_claim_whole_rule_identity():
    assert LINEAGE_SPLIT["expected_lineage"]["cardinality"] == "ONE_TO_MANY"
    assert len(LINEAGE_SPLIT["expected_lineage"]["edges"]) == 2
    assertions = " ".join(LINEAGE_SPLIT["assertions"]).casefold()
    assert "does not by itself prove" in assertions
    assert "separately asserted" in assertions


def test_audit_language_scope_survives_correction_chain():
    eng = events_for_language(CORR["events"], "ENG")
    fra = events_for_language(CORR["events"], "FRA")
    pol = events_for_language(CORR["events"], "POL")

    assert [event["event_id"] for event in eng] == [
        "corr-2005-01-28-group-a",
        "corr-2005-05-25-correct-placement",
    ]
    assert [event["event_id"] for event in fra] == [
        "corr-2005-01-28-group-b",
        "corr-2005-05-25-correct-placement",
    ]
    assert pol == []

    eng_chain = correction_chain_for_language(CORR["events"], "ENG")
    fra_chain = correction_chain_for_language(CORR["events"], "FRA")
    assert eng_chain[-1]["corrects_event_ids"] == [
        "corr-2005-01-28-group-a"
    ]
    assert fra_chain[-1]["corrects_event_ids"] == [
        "corr-2005-01-28-group-b"
    ]


def test_audit_operational_money_corrigendum_is_expression_scoped():
    assert [
        event["event_id"]
        for event in events_for_language(MONEY_CORR["events"], "ENG")
    ] == ["corr-1990-10-06-en-article4-money"]
    assert events_for_language(MONEY_CORR["events"], "DEU") == []
    operation = MONEY_CORR["events"][0]["operations"][0]
    assert operation["before_text"] == "ECU 225"
    assert operation["after_text"] == "ECU 255"


def test_audit_current_consolidation_does_not_rewrite_source_history():
    label_date = BACKPROJECTION["text_state_label_date"]
    later_sources = [
        source
        for expression in BACKPROJECTION["observed_expressions"]
        for source in expression["supporting_later_sources"]
    ]
    assert later_sources
    assert all(source["source_date"] > label_date for source in later_sources)

    english_as_of_february = events_for_language(
        CORR["events"],
        "ENG",
        source_cutoff_date="2005-02-01",
    )
    assert [event["event_id"] for event in english_as_of_february] == [
        "corr-2005-01-28-group-a"
    ]


def test_audit_identifier_equivalence_stops_at_identity_level_boundaries():
    graph = TypedIdentifierGraph(IDENTITY)
    equivalents = {
        node["node_id"] for node in graph.equivalents("r794-celex")
    }
    assert equivalents == {
        "r794-celex",
        "r794-eli",
        "r794-cellar-work",
    }
    assert "r794-eng-expression" not in equivalents
    assert "r794-eng-fmx4" not in equivalents
    assert "r794-consolidated-celex" not in equivalents
    assert "r794-corr-celex" not in equivalents


def test_audit_procedure_adoption_publication_and_scrutiny_remain_orthogonal():
    case = _procedure_case("esrs-delegated-act")
    state = state_as_of(
        case["events"],
        procedure_id=case["procedure_id"],
        on_date="2023-08-15",
    )
    dimensions = state["dimensions"]
    assert dimensions["FORMAL_ACT_ADOPTION"] == "ADOPTED"
    assert dimensions["DELEGATED_SCRUTINY"] == "OPEN"
    assert dimensions["FINAL_ACT_PUBLICATION"] == "NOT_PUBLISHED"
    assert dimensions["PROCEDURE_OUTCOME"] == "PENDING"


def test_audit_feed_action_is_hint_not_source_change_truth():
    event = SOURCE_CHANGE["event"]
    before = SOURCE_CHANGE["snapshots"]["before"]
    for key, expected in SOURCE_CHANGE["expected"].items():
        actual = classify_source_change(
            action=event["action"],
            previous=before,
            current=SOURCE_CHANGE["snapshots"][key],
        )
        assert actual == expected


def test_audit_zero_unexplained_ast_text_is_not_full_structural_by_itself():
    for case in AST_ACCOUNTING["cases"]:
        assert case["unexplained_chars"] == 0
        assert case["duplicate_claim_count"] == 0
        if case["unknown_native_kinds"]:
            assert case["fidelity"] != "FULL_STRUCTURAL"


def test_audit_superseded_provenance_disappears_only_from_current_view():
    all_ids = {record["record_id"] for record in LEDGER["records"]}
    current_ids = {
        record["record_id"]
        for record in active_records(
            LEDGER["records"],
            include_supersession_records=False,
        )
    }
    assert "support-audit-locator-v1" in all_ids
    assert "support-audit-locator-v1" not in current_ids
    assert "support-audit-locator-v2" in current_ids


def test_audit_all_change_atom_temporal_refs_resolve_canonically():
    temporal_ids = {
        assertion["assertion_id"]
        for fixture in TEMPORAL_FIXTURES
        for assertion in fixture["assertions"]
    }
    refs = {
        ref
        for fixture in SEMANTIC_FIXTURES
        for atom in fixture["atoms"]
        for ref in atom.get("temporal_assertion_refs", [])
    }
    assert refs
    assert refs <= temporal_ids


def test_audit_thread_reference_graph_resolves_and_source_mode_closes():
    resolved, errors = resolve_thread_references(THREAD)
    assert errors == []
    assert resolved
    assert source_mode_gaps(THREAD) == []


def test_audit_gold_machine_assertions_all_have_human_assertions():
    human_ids = {
        assertion["assertion_id"]
        for bucket in GOLD_THREAD["expected"].values()
        for assertion in bucket
    }
    machine_ids = {
        assertion["assertion_id"]
        for assertion in GOLD_THREAD["machine_expectations"]
    }
    assert machine_ids <= human_ids
