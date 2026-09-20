#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

from needle.retrieval.search import search_thread


THREAD_PATH = Path("fixtures/thread/reg794-article3-thread-v0.1.json")
QUERY_SCHEMA_PATH = Path("schemas/retrieval-query-v0.1.schema.json")
RESPONSE_SCHEMA_PATH = Path("schemas/retrieval-response-v0.1.schema.json")
OUT = Path("artifacts/retrieval/article3-retrieval-demo-v0.1.json")


def q(query_id, *, text_terms=None, filters=None, temporal=None):
    result = {
        "schema_version":"retrieval-query-v0.1",
        "query_id":query_id,
        "text_terms":text_terms or [],
        "text_mode":"ALL",
        "filters":filters or {},
    }
    if temporal is not None:
        result["temporal"] = temporal
    return result


def application_on(
    valid_date,
    *,
    mode="ACTIVE_ONLY",
    perspective="EX_POST_LEGAL_EFFECT",
    source_cutoff_date=None,
):
    result = {
        "dimension":"APPLICATION",
        "valid_date":valid_date,
        "perspective":perspective,
        "mode":mode,
        "context":{},
    }
    if source_cutoff_date is not None:
        result["source_cutoff_date"] = source_cutoff_date
    return result


def main() -> int:
    thread = json.loads(THREAD_PATH.read_text(encoding="utf-8"))
    query_schema = json.loads(QUERY_SCHEMA_PATH.read_text(encoding="utf-8"))
    response_schema = json.loads(RESPONSE_SCHEMA_PATH.read_text(encoding="utf-8"))
    qv = Draft202012Validator(query_schema)
    rv = Draft202012Validator(response_schema)

    queries = [
        q(
            "thread-by-eli",
            filters={
                "entity_kinds":["THREAD"],
                "identifiers":[{
                    "scheme":"ELI",
                    "value":"http://data.europa.eu/eli/reg/2004/794/oj",
                }],
            },
        ),
        q(
            "sani-day-before-replacement",
            text_terms=["SANI"],
            filters={"entity_kinds":["CHANGE_ATOM"]},
            temporal=application_on("2025-07-02"),
        ),
        q(
            "sani-on-replacement-day",
            text_terms=["SANI"],
            filters={"entity_kinds":["CHANGE_ATOM"]},
            temporal=application_on("2025-07-03"),
        ),
        q(
            "sani-source-state-before-2025-publication",
            text_terms=["reg794-art3-sani-duty-v0.1"],
            filters={"entity_kinds":["CHANGE_ATOM"]},
            temporal=application_on(
                "2025-07-03",
                mode="EVALUATE",
                perspective="OFFICIAL_SOURCE_STATE_AS_OF",
                source_cutoff_date="2025-06-12",
            ),
        ),
        q(
            "sani-source-state-after-2025-publication",
            text_terms=["reg794-art3-sani-duty-v0.1"],
            filters={"entity_kinds":["CHANGE_ATOM"]},
            temporal=application_on(
                "2025-07-03",
                mode="EVALUATE",
                perspective="OFFICIAL_SOURCE_STATE_AS_OF",
                source_cutoff_date="2025-06-13",
            ),
        ),
        q(
            "paragraph4-2025-derived-effect",
            filters={
                "provision_path_prefixes":["Article 3(4)"],
                "event_ids":["paragraph4-cross-reference-ripple-2025"],
                "source_mode_closed":True,
            },
        ),
        q(
            "technical-system-identity-unknown",
            text_terms=["technical identity"],
            filters={"entity_kinds":["THREAD_UNKNOWN"]},
        ),
    ]

    cases = []
    for query in queries:
        query_errors = list(qv.iter_errors(query))
        if query_errors:
            raise AssertionError(
                f"{query['query_id']} query invalid: "
                + "; ".join(error.message for error in query_errors)
            )
        response = search_thread(thread, query)
        response_errors = list(rv.iter_errors(response))
        if response_errors:
            raise AssertionError(
                f"{query['query_id']} response invalid: "
                + "; ".join(error.message for error in response_errors)
            )
        cases.append({"query":query, "response":response})

    payload = {
        "artifact_version":"article3-retrieval-demo-v0.1",
        "thread_id":thread["thread_id"],
        "character":"DERIVED_REBUILDABLE_RETRIEVAL_ARTIFACT",
        "cases":cases,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "thread_id":thread["thread_id"],
        "case_count":len(cases),
        "output":str(OUT),
        "projection_fingerprints":sorted({
            case["response"]["projection_fingerprint"]
            for case in cases
        }),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
