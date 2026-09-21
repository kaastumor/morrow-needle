from needle.operations.authentic_candidates import candidates_from_authentic_text


def event():
    return {"event_key":"evt:test","identifiers":["celex:32026R2104"]}


def test_keyed_row_instruction_is_generic_and_evidence_backed():
    text=(
        "ANNEX Annex V is amended as follows: in Part 1, Section B, in the entry "
        "for the United States, the following rows for the zones US-2.1405 and "
        "US-2.1406 are added after the row for the zone US-2.1404."
    )
    candidates=candidates_from_authentic_text(
        event(),text,source_id="CELEX:32026R2104",locator="official://artifact"
    )
    assert len(candidates)==1
    candidate=candidates[0]
    assert candidate["outcome"]=="LEGAL_CHANGE_VERIFIED"
    assert candidate["verification_route"]=="AUTHENTIC_LEGAL_CAUSE"
    assert "Annex V > Part 1 > Section B > United States" in candidate["semantic_key"]
    assert candidate["evidence_refs"]==["CELEX:32026R2104"]
    assert candidate["explanation"]["affected"]==[]


def test_same_drafting_form_is_not_celex_dispatched():
    text=(
        "Annex XIV is amended: in Part 2, Section C, in the entry for Exampleland, "
        "the following rows for the zones EX-1.1 and EX-1.2 are added after the "
        "row for the zone EX-1.0."
    )
    candidates=candidates_from_authentic_text(
        {"event_key":"evt:other","identifiers":["celex:39999R9999"]},
        text,source_id="CELEX:39999R9999"
    )
    assert len(candidates)==1
    assert "Annex XIV" in candidates[0]["semantic_key"]


def test_missing_explicit_annex_abstains():
    text=(
        "in Part 1, Section B, in the entry for the United States, the following "
        "rows for the zones US-2.1405 and US-2.1406 are added after the row for "
        "the zone US-2.1404."
    )
    assert candidates_from_authentic_text(
        event(),text,source_id="CELEX:32026R2104"
    )==[]


def test_near_match_abstains_instead_of_guessing():
    text=(
        "Annex V should contain zones US-2.1405 and US-2.1406 somewhere after "
        "US-2.1404."
    )
    assert candidates_from_authentic_text(
        event(),text,source_id="CELEX:32026R2104"
    )==[]
