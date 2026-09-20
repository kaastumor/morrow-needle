import json
from pathlib import Path

from jsonschema import Draft202012Validator

from needle.retrieval.projection import build_thread_projection, _support_index
from needle.retrieval.search import search_thread


QUERY_SCHEMA = json.loads(
    Path("schemas/retrieval-query-v0.1.schema.json").read_text(encoding="utf-8")
)
RESPONSE_SCHEMA = json.loads(
    Path("schemas/retrieval-response-v0.1.schema.json").read_text(encoding="utf-8")
)
THREAD = json.loads(
    Path("fixtures/thread/reg794-article3-thread-v0.1.json").read_text(
        encoding="utf-8"
    )
)


def query(
    query_id,
    *,
    text_terms=None,
    text_mode="ALL",
    filters=None,
    temporal=None,
):
    result = {
        "schema_version":"retrieval-query-v0.1",
        "query_id":query_id,
        "text_terms":text_terms or [],
        "text_mode":text_mode,
        "filters":filters or {},
    }
    if temporal is not None:
        result["temporal"] = temporal
    return result


def ids(response):
    return [result["entity_ref"]["entity_id"] for result in response["results"]]


def kinds(response):
    return [result["entity_ref"]["kind"] for result in response["results"]]


def test_retrieval_queries_and_responses_validate():
    cases = [
        query("sani", text_terms=["SANI"]),
        query(
            "duties",
            filters={
                "entity_kinds":["CHANGE_ATOM"],
                "legal_effects":["DUTY"],
                "dimensions":["DIGITAL_CHANNEL"],
                "source_mode_closed":True,
            },
        ),
        query(
            "paragraph4",
            filters={
                "provision_path_prefixes":["Article 3(4)"],
                "event_ids":["paragraph4-cross-reference-ripple-2025"],
            },
        ),
    ]
    qv = Draft202012Validator(QUERY_SCHEMA)
    rv = Draft202012Validator(RESPONSE_SCHEMA)
    for case in cases:
        assert list(qv.iter_errors(case)) == []
        response = search_thread(THREAD, case)
        assert list(rv.iter_errors(response)) == []


def test_projection_is_rebuildable_and_contains_no_hydrated_canonical_payloads():
    first = build_thread_projection(THREAD)
    second = build_thread_projection(THREAD)
    assert first["projection_fingerprint"] == second["projection_fingerprint"]
    assert first["documents"] == second["documents"]
    assert all("canonical_entity" not in doc for doc in first["documents"])
    assert all(doc["source_mode"]["closed"] for doc in first["documents"])


def test_sani_lexical_search_prefers_the_actual_sani_atom():
    response = search_thread(THREAD, query("sani", text_terms=["SANI"]))
    assert response["results"][0]["entity_ref"] == {
        "kind":"CHANGE_ATOM",
        "entity_id":"reg794-art3-sani-duty-v0.1",
    }
    assert "reg794-art3-pki-correspondence-duty-v0.1" not in ids(response)
    assert any(
        reason["kind"] == "LEXICAL_MATCH"
        and reason["query_value"] == "SANI"
        and reason["field"] == "CLAIM"
        for reason in response["results"][0]["match_reasons"]
    )


def test_structured_digital_channel_duty_filter_returns_only_change_atom_duties():
    response = search_thread(
        THREAD,
        query(
            "digital-channel-duties",
            filters={
                "entity_kinds":["CHANGE_ATOM"],
                "legal_effects":["DUTY"],
                "dimensions":["DIGITAL_CHANNEL"],
                "source_mode_closed":True,
            },
        ),
    )
    assert set(ids(response)) == {
        "reg794-art3-sani-duty-v0.1",
        "reg794-art3-pki-correspondence-duty-v0.1",
        "reg794-art3-2025-notification-channel-duty-v0.1",
        "reg794-art3-2025-correspondence-channel-duty-v0.1",
    }
    assert set(kinds(response)) == {"CHANGE_ATOM"}


def test_article3_4_2025_search_returns_derived_effect_but_no_mutation():
    response = search_thread(
        THREAD,
        query(
            "article3-4-2025",
            filters={
                "provision_path_prefixes":["Article 3(4)"],
                "event_ids":["paragraph4-cross-reference-ripple-2025"],
                "source_mode_closed":True,
            },
        ),
    )
    assert "reg794-art3-2025-crossref-exception-ripple-v0.1" in ids(response)
    assert "reg794-article3-p4-2025-continuity-v0.1" in ids(response)
    assert "MUTATION" not in kinds(response)


def test_corrigendum_is_retrievable_as_nonimpact_evidence_not_mutation():
    response = search_thread(
        THREAD,
        query(
            "corrigendum-nonimpact",
            filters={
                "entity_kinds":["THREAD_EVIDENCE"],
                "event_kinds":["RELATED_SOURCE_NON_IMPACT"],
            },
        ),
    )
    assert ids(response) == ["reg794-article3-corrigendum-scope-v0.1"]
    entity = response["results"][0]["canonical_entity"]
    assert entity["thread_scope_result"]["classification"] == "NO_THREAD_MUTATION"
    assert entity["thread_scope_result"]["article3_affected"] is False


def test_exclusive_chapter2_temporal_rule_is_searchable_without_flattening():
    response = search_thread(
        THREAD,
        query(
            "chapter2-exclusive",
            text_terms=["more than five months"],
            filters={
                "entity_kinds":["TEMPORAL_ASSERTION"],
                "temporal_dimensions":["APPLICATION"],
            },
        ),
    )
    assert ids(response) == ["reg794-2004-chapter2-application-threshold"]
    assertion = response["results"][0]["canonical_entity"]
    assert assertion["normalized_date"] == "2004-10-20"
    assert assertion["inclusive"] is False


def test_rule_lineage_filter_does_not_mix_structural_lineage():
    response = search_thread(
        THREAD,
        query(
            "rule-lineage",
            filters={
                "entity_kinds":["LINEAGE_EDGE"],
                "lineage_scopes":["RULE_LINEAGE"],
            },
        ),
    )
    assert set(ids(response)) == {
        "reg794-art3-notification-channel-rule-2008-to-2025",
        "reg794-art3-correspondence-channel-rule-2008-to-2025",
    }
    assert all(
        result["canonical_entity"]["assertion_scope"] == "RULE_LINEAGE"
        for result in response["results"]
    )


def test_exact_thread_id_search_ranks_thread_before_children():
    response = search_thread(
        THREAD,
        query("thread-id", text_terms=["CELEX:32004R0794#Article3:ENG"]),
    )
    assert response["results"][0]["entity_ref"] == {
        "kind":"THREAD",
        "entity_id":"CELEX:32004R0794#Article3:ENG",
    }
    reason = next(
        reason for reason in response["results"][0]["match_reasons"]
        if reason["kind"] == "LEXICAL_MATCH"
    )
    assert reason["match_quality"] == "EXACT"
    assert "ENTITY_ID" in reason["field"]


def test_retrieval_response_hydrates_current_canonical_entity():
    response = search_thread(
        THREAD,
        query(
            "pki-id",
            text_terms=["reg794-art3-pki-correspondence-duty-v0.1"],
            filters={"entity_kinds":["CHANGE_ATOM"]},
        ),
    )
    assert ids(response) == ["reg794-art3-pki-correspondence-duty-v0.1"]
    entity = response["results"][0]["canonical_entity"]
    assert entity["atom_id"] == "reg794-art3-pki-correspondence-duty-v0.1"
    assert entity["claim"]["object"] == "Public Key Infrastructure (PKI)"


def _application_on(date_value, *, mode="ACTIVE_ONLY", perspective="EX_POST_LEGAL_EFFECT", source_cutoff_date=None):
    temporal = {
        "dimension":"APPLICATION",
        "valid_date":date_value,
        "perspective":perspective,
        "mode":mode,
        "context":{},
    }
    if source_cutoff_date is not None:
        temporal["source_cutoff_date"] = source_cutoff_date
    return temporal


def test_temporal_retrieval_requires_explicit_perspective_and_mode():
    validator = Draft202012Validator(QUERY_SCHEMA)
    ambiguous = query(
        "ambiguous-date",
        filters={"entity_kinds":["CHANGE_ATOM"]},
    )
    ambiguous["temporal"] = {
        "dimension":"APPLICATION",
        "valid_date":"2025-07-03",
    }
    assert list(validator.iter_errors(ambiguous))

    official_without_cutoff = query(
        "official-no-cutoff",
        filters={"entity_kinds":["CHANGE_ATOM"]},
        temporal=_application_on(
            "2025-07-03",
            perspective="OFFICIAL_SOURCE_STATE_AS_OF",
        ),
    )
    assert list(validator.iter_errors(official_without_cutoff))


def test_sani_is_active_day_before_2025_replacement_and_inactive_on_boundary():
    before = search_thread(
        THREAD,
        query(
            "sani-before-replacement",
            text_terms=["SANI"],
            filters={"entity_kinds":["CHANGE_ATOM"]},
            temporal=_application_on("2025-07-02"),
        ),
    )
    assert ids(before)[0] == "reg794-art3-sani-duty-v0.1"
    assert before["results"][0]["temporal_evaluation"]["active"] is True
    assert before["results"][0]["temporal_evaluation"]["supporting_assertion_ids"] == [
        "reg794-art3-p3-sani-application-start",
        "reg794-art3-p3-legacy-channels-application-end",
    ]
    assert any(
        reason["kind"] == "TEMPORAL_EVALUATION"
        for reason in before["results"][0]["match_reasons"]
    )

    boundary = search_thread(
        THREAD,
        query(
            "sani-on-replacement",
            text_terms=["SANI"],
            filters={"entity_kinds":["CHANGE_ATOM"]},
            temporal=_application_on("2025-07-03"),
        ),
    )
    assert "reg794-art3-sani-duty-v0.1" not in ids(boundary)
    abstention = next(
        item for item in boundary["abstentions"]
        if item["entity_ref"]["entity_id"] == "reg794-art3-sani-duty-v0.1"
    )
    assert abstention["reason"] == "TEMPORAL_NOT_ACTIVE"
    assert abstention["temporal_evaluation"]["active"] is False
    assert abstention["temporal_evaluation"]["end"]["inclusive"] is False


def test_2025_channel_duties_activate_on_replacement_day():
    response = search_thread(
        THREAD,
        query(
            "new-channels-on-replacement",
            filters={
                "entity_kinds":["CHANGE_ATOM"],
                "legal_effects":["DUTY"],
                "dimensions":["DIGITAL_CHANNEL"],
            },
            temporal=_application_on("2025-07-03"),
        ),
    )
    assert set(ids(response)) == {
        "reg794-art3-2025-notification-channel-duty-v0.1",
        "reg794-art3-2025-correspondence-channel-duty-v0.1",
    }
    assert all(
        result["temporal_evaluation"]["active"] is True
        for result in response["results"]
    )
    assert {
        item["entity_ref"]["entity_id"]
        for item in response["abstentions"]
        if item["reason"] == "TEMPORAL_NOT_ACTIVE"
    } >= {
        "reg794-art3-sani-duty-v0.1",
        "reg794-art3-pki-correspondence-duty-v0.1",
    }


def test_pki_is_active_before_sani_without_borrowing_sani_date():
    response = search_thread(
        THREAD,
        query(
            "spring-2008-channel-duties",
            filters={
                "entity_kinds":["CHANGE_ATOM"],
                "legal_effects":["DUTY"],
                "dimensions":["DIGITAL_CHANNEL"],
            },
            temporal=_application_on("2008-04-14"),
        ),
    )
    assert "reg794-art3-pki-correspondence-duty-v0.1" in ids(response)
    assert "reg794-art3-sani-duty-v0.1" not in ids(response)


def test_temporal_query_abstains_for_entities_without_explicit_temporal_refs():
    response = search_thread(
        THREAD,
        query(
            "mutation-date-abstain",
            filters={"entity_kinds":["MUTATION"]},
            temporal=_application_on("2025-07-03"),
        ),
    )
    assert response["results"] == []
    assert response["abstentions"]
    assert {
        item["reason"] for item in response["abstentions"]
    } == {"NO_TEMPORAL_ASSERTIONS"}


def test_temporal_evaluate_mode_retains_inactive_result_instead_of_hiding_it():
    response = search_thread(
        THREAD,
        query(
            "evaluate-sani-boundary",
            text_terms=["SANI"],
            filters={"entity_kinds":["CHANGE_ATOM"]},
            temporal=_application_on("2025-07-03", mode="EVALUATE"),
        ),
    )
    sani = next(
        result for result in response["results"]
        if result["entity_ref"]["entity_id"] == "reg794-art3-sani-duty-v0.1"
    )
    assert sani["temporal_evaluation"]["active"] is False
    assert sani["temporal_evaluation"]["state"] == "RESOLVED"


def test_retrieval_support_index_uses_current_provenance_view():
    support = _support_index(THREAD, root=Path("."))
    assert support[("OTHER", "TEST_ONLY:sani-locator-correction")] == [
        "support-audit-locator-v2"
    ]
    assert "support-audit-locator-v1" not in {
        record_id
        for record_ids in support.values()
        for record_id in record_ids
    }


def test_retrieval_result_exposes_active_support_record_ids():
    response = search_thread(
        THREAD,
        query(
            "sani-support",
            text_terms=["reg794-art3-sani-duty-v0.1"],
            filters={"entity_kinds":["CHANGE_ATOM"]},
        ),
    )
    result = response["results"][0]
    assert result["source_mode"]["closed"] is True
    assert "support-atom-sani" in result["source_mode"]["support_record_ids"]
    assert result["source_mode"]["support_count"] == len(
        result["source_mode"]["support_record_ids"]
    )
