from needle.operations.authentic_candidates import candidates_from_authentic_text, candidates_from_reobservation


def event():
    return {"event_key":"evt:test","identifiers":["celex:32026R2104"]}


def instruction_text():
    return (
        "ANNEX Annex V is amended as follows: in Part 1, Section B, in the entry "
        "for the United States, the following rows for the zones US-2.1405 and "
        "US-2.1406 are added after the row for the zone US-2.1404."
    )


def two_annex_text():
    command=(
        "in Part 1, Section B, in the entry for the United States, the following "
        "rows for the zones US-2.1405 and US-2.1406 are added after the row for "
        "the zone US-2.1404."
    )
    return "Annex V is amended as follows: "+command+" Annex XIV is amended as follows: "+command


def test_keyed_row_instruction_is_generic_and_evidence_backed():
    candidates=candidates_from_authentic_text(
        event(),instruction_text(),source_id="CELEX:32026R2104",locator="official://artifact"
    )
    assert len(candidates)==1
    candidate=candidates[0]
    assert candidate["outcome"]=="LEGAL_CHANGE_VERIFIED"
    assert candidate["verification_route"]=="AUTHENTIC_LEGAL_CAUSE"
    assert "Annex V > Part 1 > Section B > United States" in candidate["semantic_key"]
    assert candidate["evidence_refs"]==["CELEX:32026R2104"]
    assert candidate["explanation"]["affected"]==[]


def test_reobservation_changes_provenance_not_semantic_identity():
    first=candidates_from_authentic_text(
        event(),instruction_text(),source_id="CELEX:32026R2104",
        evidence_ref="src-observation:first",language="eng"
    )[0]
    second=candidates_from_authentic_text(
        event(),instruction_text(),source_id="CELEX:32026R2104",
        evidence_ref="src-observation:second",language="eng"
    )[0]
    assert first["semantic_key"] == second["semantic_key"]
    assert first["canonical_refs"] == second["canonical_refs"]
    assert first["evidence_refs"] == ["src-observation:first"]
    assert second["evidence_refs"] == ["src-observation:second"]


def test_language_is_part_of_mutation_identity_not_silently_globalized():
    english=candidates_from_authentic_text(
        event(),instruction_text(),source_id="CELEX:32026R2104",language="eng"
    )[0]
    french=candidates_from_authentic_text(
        event(),instruction_text(),source_id="CELEX:32026R2104",language="fra"
    )[0]
    assert english["semantic_key"] != french["semantic_key"]
    assert english["canonical_refs"] != french["canonical_refs"]


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


def test_reobservation_groups_multiple_explicit_mutations_without_collapsing_truth():
    granular=candidates_from_authentic_text(
        event(),
        two_annex_text(),
        source_id="CELEX:32026R2104",
        locator="official://artifact",
        evidence_ref="src-observation:one-act",
    )
    assert len(granular)==2
    assert len({
        ref["entity_id"]
        for item in granular
        for ref in item["canonical_refs"]
    })==2

    grouped=candidates_from_reobservation(
        event(),
        {
            "celex":"32026R2104",
            "analysis_language":"eng",
            "analysis_text":two_annex_text(),
            "content_observation":{
                "record_id":"src-observation:one-act",
                "payload":{
                    "language":"ENG",
                    "retrieval":{"final_uri":"official://artifact"},
                },
            },
        },
    )
    assert len(grouped)==1
    candidate=grouped[0]
    assert candidate["semantic_key"].startswith("authentic-compound:")
    assert len(candidate["canonical_refs"])==2
    assert candidate["evidence_refs"]==["src-observation:one-act"]
    assert "Annex V" in candidate["explanation"]["what_changed"]
    assert "Annex XIV" in candidate["explanation"]["what_changed"]
    assert any(
        "canonical mutation identities remain separate" in item
        for item in candidate["unknowns"]
    )
