import json
from pathlib import Path

from jsonschema import Draft202012Validator
import pytest

from needle.mutation.instructions import (
    candidate_from_authentic_instruction,
    parse_authentic_keyed_row_insertions,
)


SCHEMA=json.loads(
    Path("schemas/mutation-candidate-v0.3.schema.json").read_text(
        encoding="utf-8"
    )
)

INSTRUCTION=(
    "in Part 1, Section B, in the entry for the United States, "
    "the following rows for the zones US-2.1405 and US-2.1406 "
    "are added after the row for the zone US-2.1404:"
)


def parse():
    return parse_authentic_keyed_row_insertions(
        INSTRUCTION,
        source_id="CELEX:32026R2104",
        parent_locator="Annex V",
        locator=(
            "L_202602104EN.000101.fmx.xml"
            "#normalized-chars:5833-5994"
        ),
    )


def test_explicit_keyed_row_insertion_is_parsed_source_natively():
    result=parse()
    assert len(result) == 1
    instruction=result[0]
    assert instruction["operation"] == "INSERT"
    assert instruction["inserted_keys"] == [
        "US-2.1405","US-2.1406"
    ]
    assert instruction["placement_anchor"] == "US-2.1404"
    assert instruction["target_locator"] == (
        "Annex V > Part 1 > Section B > United States > "
        "rows US-2.1405, US-2.1406"
    )
    assert instruction["evidence"]["authority_character"] == (
        "CANONICAL_LEGAL_CAUSE"
    )


def test_authentic_instruction_creates_verified_v03_mutation_without_state_snapshot():
    candidate=candidate_from_authentic_instruction(
        parse()[0],
        kind="TABLE_ROW_SET",
        language="ENG",
        candidate_id="reg2104-annexv-us-zones-1405-1406-v0.1",
    )
    assert candidate["candidate_origin"] == "AUTHENTIC_INSTRUCTION"
    assert candidate["alignment_basis"] == "SOURCE_NATIVE_IDENTIFIER"
    assert candidate["reconciliation_state"] == "AUTHENTIC_CAUSE_ONLY"
    assert candidate["verification_state"] == "VERIFIED"
    assert candidate["before"] is None
    assert candidate["after"] is None
    assert candidate["supporting_evidence"] == [
        parse()[0]["evidence"]
    ]
    assert list(
        Draft202012Validator(SCHEMA).iter_errors(candidate)
    ) == []


def test_ambiguous_table_amendment_does_not_create_insertion():
    assert parse_authentic_keyed_row_insertions(
        "Annex V is amended as follows.",
        source_id="CELEX:32026R2104",
        parent_locator="Annex V",
    ) == []


def test_missing_placement_anchor_does_not_create_insertion():
    assert parse_authentic_keyed_row_insertions(
        (
            "in Part 1, Section B, in the entry for the United States, "
            "the zones US-2.1405 and US-2.1406 are added."
        ),
        source_id="CELEX:32026R2104",
        parent_locator="Annex V",
    ) == []


def test_candidate_builder_rejects_non_authentic_evidence():
    instruction=parse()[0]
    instruction["evidence"]["channel"]="CONSOLIDATED_CHECKPOINT"
    with pytest.raises(ValueError,match="AUTHENTIC_ACT"):
        candidate_from_authentic_instruction(
            instruction,
            kind="TABLE_ROW_SET",
            language="ENG",
        )


def test_schema_rejects_fake_after_state_on_authentic_only_candidate():
    candidate=candidate_from_authentic_instruction(
        parse()[0],
        kind="TABLE_ROW_SET",
        language="ENG",
    )
    candidate["after"]={
        "state_id":"fabricated-after",
        "node_id":"row-us-2-1405",
        "text_hash":"a"*64,
        "text_length":10,
    }
    assert list(
        Draft202012Validator(SCHEMA).iter_errors(candidate)
    )


def test_schema_rejects_false_diff_origin_on_authentic_only_candidate():
    candidate=candidate_from_authentic_instruction(
        parse()[0],
        kind="TABLE_ROW_SET",
        language="ENG",
    )
    candidate["candidate_origin"]="DETERMINISTIC_DIFF"
    assert list(
        Draft202012Validator(SCHEMA).iter_errors(candidate)
    )


def test_schema_rejects_unverified_authentic_only_candidate():
    candidate=candidate_from_authentic_instruction(
        parse()[0],
        kind="TABLE_ROW_SET",
        language="ENG",
    )
    candidate["verification_state"]="UNVERIFIED"
    assert list(
        Draft202012Validator(SCHEMA).iter_errors(candidate)
    )
