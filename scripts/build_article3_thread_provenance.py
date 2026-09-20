#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from needle.provenance.ledger import seal_record, validate_ledger


LEDGER_PATH = Path("fixtures/provenance/reg794-article3-dag-v0.1.json")
BASELINE_PATH = Path("fixtures/thread/reg794-article3-baseline-v0.1.json")
ORIGINAL_TEMPORAL_PATH = Path("fixtures/temporal/reg794-article3-original-v0.1.json")
TEMPORAL_2008_PATH = Path("fixtures/temporal/reg794-article3-sani-v0.1.json")
LINEAGE_PATH = Path("fixtures/lineage/reg794-article3-thread-lineage-v0.1.json")
P4_PATH = Path("fixtures/thread/reg794-article3-p4-continuity-v0.1.json")
CORR_PATH = Path("fixtures/thread/reg794-article3-corrigendum-scope-v0.1.json")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sha(value: str) -> str:
    return value if value.startswith("sha256:") else "sha256:" + value


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--out",
        default="artifacts/thread-provenance/reg794-article3-dag-v0.1.json",
    )
    args = ap.parse_args()

    ledger = load(LEDGER_PATH)
    baseline = load(BASELINE_PATH)
    temporal = load(ORIGINAL_TEMPORAL_PATH)
    temporal_2008 = load(TEMPORAL_2008_PATH)
    lineage = load(LINEAGE_PATH)
    p4 = load(P4_PATH)
    corrigendum = load(CORR_PATH)

    records = ledger["records"]
    by_id = {record["record_id"]:record for record in records}

    def append(record: dict[str, Any]) -> None:
        sealed = seal_record(record)
        prior = by_id.get(sealed["record_id"])
        if prior is not None:
            if prior != sealed:
                raise AssertionError(
                    f"existing provenance record differs: {sealed['record_id']}"
                )
            return
        records.append(sealed)
        by_id[sealed["record_id"]] = sealed

    # New immutable official observations required by the complete Thread.
    append({
        "record_id":"src-reg794-2004-eng",
        "record_type":"SOURCE_OBSERVATION",
        "created_at":"2026-09-20T17:11:00Z",
        "payload":{
            "source_type":"CELLAR",
            "identifier":"CELEX:32004R0794",
            "resource_uri":"https://publications.europa.eu/resource/celex/32004R0794",
            "language":"ENG",
            "representation_class":"STRUCTURED_LEGAL_XML",
            "observed_at":"2026-09-20T17:04:30Z",
            "artifact_hash":baseline["authentic_source"]["artifact_hash"],
            "retrieval":{
                "final_uri":(
                    "http://publications.europa.eu/resource/cellar/"
                    "26f403d1-7656-4c91-9726-c08d466ff8bd.0006.05/zip"
                ),
                "media_type":"application/zip;mtype=fmx4",
                "http_status":200,
            },
        },
    })
    append({
        "record_id":"src-reg794-20040520-eng",
        "record_type":"SOURCE_OBSERVATION",
        "created_at":"2026-09-20T17:11:01Z",
        "payload":{
            "source_type":"CELLAR",
            "identifier":"CELEX:02004R0794-20040520",
            "resource_uri":"https://publications.europa.eu/resource/celex/02004R0794-20040520",
            "language":"ENG",
            "representation_class":"STRUCTURED_LEGAL_XML",
            "observed_at":"2026-09-20T17:04:30Z",
            "artifact_hash":baseline["initial_consolidated_checkpoint"]["artifact_hash"],
            "retrieval":{
                "final_uri":(
                    "http://publications.europa.eu/resource/cellar/"
                    "a18ae2f9-d2ea-44e3-bdc0-11cca6a10034.0004.02/zip"
                ),
                "media_type":"application/zip;mtype=fmx4",
                "http_status":200,
            },
        },
    })
    observation = corrigendum["verified_observation"]
    append({
        "record_id":"src-reg905-2025-corrigendum-eng",
        "record_type":"SOURCE_OBSERVATION",
        "created_at":"2026-09-20T17:11:02Z",
        "payload":{
            "source_type":"ELI",
            "identifier":"CELEX:32025R0905R(01)",
            "resource_uri":observation["resource_uri"],
            "language":"ENG",
            "representation_class":observation["representation_class"],
            "observed_at":observation["observed_at"],
            "artifact_hash":observation["artifact_hash"],
            "retrieval":{
                "final_uri":observation["final_uri"],
                "media_type":observation["media_type"],
                "http_status":observation["http_status"],
            },
        },
    })

    # Baseline equality is evidence, not a fabricated mutation.
    append({
        "record_id":"run-thread-baseline-2004",
        "record_type":"DERIVATION_RUN",
        "created_at":"2026-09-20T17:11:03Z",
        "payload":{
            "derivation_kind":"OTHER",
            "execution_character":"DETERMINISTIC",
            "implementation":{
                "name":"needle.thread.baseline",
                "version":"thread-v0.1",
                "config_hash":None,
            },
            "input_record_ids":[
                "src-reg794-2004-eng",
                "src-reg794-20040520-eng",
            ],
            "output_entity_refs":[{
                "entity_type":"OTHER",
                "entity_id":baseline["fixture_id"],
            }],
            "executed_at":"2026-09-20T17:04:30Z",
        },
    })
    baseline_text_hash = sha(baseline["authentic_source"]["article3"]["text_hash"])
    append({
        "record_id":"support-thread-baseline-authentic",
        "record_type":"CLAIM_SUPPORT",
        "created_at":"2026-09-20T17:11:04Z",
        "payload":{
            "claim_ref":{"entity_type":"OTHER","entity_id":baseline["fixture_id"]},
            "source_observation_id":"src-reg794-2004-eng",
            "source_span":{
                "locator":"Article 3 subtree",
                "language":"ENG",
                "text_hash":baseline_text_hash,
                "artifact_hash":baseline["authentic_source"]["artifact_hash"],
            },
            "role":"CONTEXT",
            "evidence_state":"DIRECT",
            "derivation_record_id":"run-thread-baseline-2004",
        },
    })
    append({
        "record_id":"support-thread-baseline-checkpoint",
        "record_type":"CLAIM_SUPPORT",
        "created_at":"2026-09-20T17:11:05Z",
        "payload":{
            "claim_ref":{"entity_type":"OTHER","entity_id":baseline["fixture_id"]},
            "source_observation_id":"src-reg794-20040520-eng",
            "source_span":{
                "locator":"Article 3 subtree",
                "language":"ENG",
                "text_hash":sha(
                    baseline["initial_consolidated_checkpoint"]["article3"]["text_hash"]
                ),
                "artifact_hash":baseline["initial_consolidated_checkpoint"]["artifact_hash"],
            },
            "role":"CORROBORATION",
            "evidence_state":"DIRECT",
            "derivation_record_id":"run-thread-baseline-2004",
        },
    })

    temporal_by_id = {
        assertion["assertion_id"]:assertion
        for assertion in temporal["assertions"]
    }
    pub = baseline["source_spans"]["publication-date-oj"]
    entry = baseline["source_spans"]["entry-into-force"]
    chapter = baseline["source_spans"]["chapter-ii-application"]

    append({
        "record_id":"run-temporal-original-entry-force",
        "record_type":"DERIVATION_RUN",
        "created_at":"2026-09-20T17:11:06Z",
        "payload":{
            "derivation_kind":"TEMPORAL_RESOLVE",
            "execution_character":"DETERMINISTIC",
            "implementation":{
                "name":"needle.temporal",
                "version":"temporal-v0.1",
                "config_hash":None,
            },
            "input_record_ids":["src-reg794-2004-eng"],
            "output_entity_refs":[{
                "entity_type":"TEMPORAL_ASSERTION",
                "entity_id":"reg794-2004-entry-into-force",
            }],
            "executed_at":"2026-09-20T17:04:30Z",
        },
    })
    for record_id, span, role in (
        ("support-temporal-original-publication-date", pub, "CONTEXT"),
        ("support-temporal-original-entry-force-clause", entry, "TEMPORAL"),
    ):
        append({
            "record_id":record_id,
            "record_type":"CLAIM_SUPPORT",
            "created_at":(
                "2026-09-20T17:11:07Z"
                if role == "CONTEXT"
                else "2026-09-20T17:11:08Z"
            ),
            "payload":{
                "claim_ref":{
                    "entity_type":"TEMPORAL_ASSERTION",
                    "entity_id":"reg794-2004-entry-into-force",
                },
                "source_observation_id":"src-reg794-2004-eng",
                "source_span":{
                    "locator":span["locator"],
                    "language":"ENG",
                    "text_hash":sha(span["text_hash"]),
                    "artifact_hash":baseline["authentic_source"]["artifact_hash"],
                },
                "role":role,
                "evidence_state":"DIRECT",
                "derivation_record_id":"run-temporal-original-entry-force",
            },
        })

    append({
        "record_id":"run-temporal-original-chapter2",
        "record_type":"DERIVATION_RUN",
        "created_at":"2026-09-20T17:11:09Z",
        "payload":{
            "derivation_kind":"TEMPORAL_RESOLVE",
            "execution_character":"DETERMINISTIC",
            "implementation":{
                "name":"needle.temporal",
                "version":"temporal-v0.1",
                "config_hash":None,
            },
            "input_record_ids":[
                "src-reg794-2004-eng",
                "support-temporal-original-publication-date",
                "support-temporal-original-entry-force-clause",
            ],
            "output_entity_refs":[{
                "entity_type":"TEMPORAL_ASSERTION",
                "entity_id":"reg794-2004-chapter2-application-threshold",
            }],
            "executed_at":"2026-09-20T17:04:30Z",
        },
    })
    append({
        "record_id":"support-temporal-original-chapter2",
        "record_type":"CLAIM_SUPPORT",
        "created_at":"2026-09-20T17:11:10Z",
        "payload":{
            "claim_ref":{
                "entity_type":"TEMPORAL_ASSERTION",
                "entity_id":"reg794-2004-chapter2-application-threshold",
            },
            "source_observation_id":"src-reg794-2004-eng",
            "source_span":{
                "locator":chapter["locator"],
                "language":"ENG",
                "text_hash":sha(chapter["text_hash"]),
                "artifact_hash":baseline["authentic_source"]["artifact_hash"],
            },
            "role":"TEMPORAL",
            "evidence_state":"DIRECT",
            "derivation_record_id":"run-temporal-original-chapter2",
        },
    })

    article3_temporal_ids = [
        "reg794-art3-original-paper-notification-end",
        "reg794-art3-original-electronic-notification-start",
        "reg794-art3-original-electronic-correspondence-trigger",
    ]
    append({
        "record_id":"run-temporal-original-article3",
        "record_type":"DERIVATION_RUN",
        "created_at":"2026-09-20T17:11:11Z",
        "payload":{
            "derivation_kind":"TEMPORAL_RESOLVE",
            "execution_character":"DETERMINISTIC",
            "implementation":{
                "name":"needle.temporal",
                "version":"temporal-v0.1",
                "config_hash":None,
            },
            "input_record_ids":["src-reg794-2004-eng"],
            "output_entity_refs":[
                {"entity_type":"TEMPORAL_ASSERTION","entity_id":assertion_id}
                for assertion_id in article3_temporal_ids
            ],
            "executed_at":"2026-09-20T17:04:30Z",
        },
    })
    temporal_supports = [
        (
            "support-temporal-original-paper-end",
            "reg794-art3-original-paper-notification-end",
            baseline["source_spans"]["paper-until-2005"],
            "2026-09-20T17:11:12Z",
        ),
        (
            "support-temporal-original-electronic-notification",
            "reg794-art3-original-electronic-notification-start",
            baseline["source_spans"]["electronic-from-2006"],
            "2026-09-20T17:11:13Z",
        ),
        (
            "support-temporal-original-electronic-correspondence",
            "reg794-art3-original-electronic-correspondence-trigger",
            baseline["source_spans"]["correspondence-from-2006"],
            "2026-09-20T17:11:14Z",
        ),
    ]
    for record_id, assertion_id, span, created_at in temporal_supports:
        append({
            "record_id":record_id,
            "record_type":"CLAIM_SUPPORT",
            "created_at":created_at,
            "payload":{
                "claim_ref":{
                    "entity_type":"TEMPORAL_ASSERTION",
                    "entity_id":assertion_id,
                },
                "source_observation_id":"src-reg794-2004-eng",
                "source_span":{
                    "locator":span["locator"],
                    "language":"ENG",
                    "text_hash":sha(span["text_hash"]),
                    "artifact_hash":baseline["authentic_source"]["artifact_hash"],
                },
                "role":"TEMPORAL",
                "evidence_state":"DIRECT",
                "derivation_record_id":"run-temporal-original-article3",
            },
        })

    # Canonical official publication point for source-as-of retrieval.
    append({
        "record_id":"run-temporal-reg271-2008-publication",
        "record_type":"DERIVATION_RUN",
        "created_at":"2026-09-20T17:48:00Z",
        "payload":{
            "derivation_kind":"TEMPORAL_RESOLVE",
            "execution_character":"DETERMINISTIC",
            "implementation":{
                "name":"needle.temporal",
                "version":"temporal-v0.1",
                "config_hash":None,
            },
            "input_record_ids":["src-reg271-2008-eng"],
            "output_entity_refs":[{
                "entity_type":"TEMPORAL_ASSERTION",
                "entity_id":"reg271-2008-publication",
            }],
            "executed_at":"2026-09-20T17:33:14Z",
        },
    })
    append({
        "record_id":"support-temporal-reg271-publication-point",
        "record_type":"CLAIM_SUPPORT",
        "created_at":"2026-09-20T17:48:01Z",
        "payload":{
            "claim_ref":{
                "entity_type":"TEMPORAL_ASSERTION",
                "entity_id":"reg271-2008-publication",
            },
            "source_observation_id":"src-reg271-2008-eng",
            "source_span":{
                "locator":"L_2008082EN.01000101.doc.xml#DATE[ISO=20080325]",
                "language":"ENG",
                "text_hash":"sha256:280f989c59b0e7feb1d7b9f0fba9daba12ba855deb20bad7835a3d73708b1302",
                "artifact_hash":"sha256:c61ea6c41be9c3faf418a80c2ce12fcfb1233b91557eb4157ce2435c40afe5f7",
            },
            "role":"TEMPORAL",
            "evidence_state":"DIRECT",
            "derivation_record_id":"run-temporal-reg271-2008-publication",
        },
    })

    # Complete the 2008 channel lifecycle before time-aware retrieval.
    append({
        "record_id":"run-temporal-reg271-2008-entry-force",
        "record_type":"DERIVATION_RUN",
        "created_at":"2026-09-20T17:37:00Z",
        "payload":{
            "derivation_kind":"TEMPORAL_RESOLVE",
            "execution_character":"DETERMINISTIC",
            "implementation":{
                "name":"needle.temporal",
                "version":"temporal-v0.1",
                "config_hash":None,
            },
            "input_record_ids":["src-reg271-2008-eng"],
            "output_entity_refs":[{
                "entity_type":"TEMPORAL_ASSERTION",
                "entity_id":"reg271-2008-entry-into-force",
            }],
            "executed_at":"2026-09-20T17:33:14Z",
        },
    })
    for record_id, locator, text_hash, role, created_at in [
        (
            "support-temporal-reg271-publication",
            "L_2008082EN.01000101.doc.xml#DATE[ISO=20080325]",
            "280f989c59b0e7feb1d7b9f0fba9daba12ba855deb20bad7835a3d73708b1302",
            "CONTEXT",
            "2026-09-20T17:37:01Z",
        ),
        (
            "support-temporal-reg271-entry-clause",
            "L_2008082EN.01000101.xml#normalized-chars:11427-11554",
            "54d5a5d17e73703f7db092dec7d536193a9946b6d0b56707b0e1aa3acc26f67a",
            "TEMPORAL",
            "2026-09-20T17:37:02Z",
        ),
    ]:
        append({
            "record_id":record_id,
            "record_type":"CLAIM_SUPPORT",
            "created_at":created_at,
            "payload":{
                "claim_ref":{
                    "entity_type":"TEMPORAL_ASSERTION",
                    "entity_id":"reg271-2008-entry-into-force",
                },
                "source_observation_id":"src-reg271-2008-eng",
                "source_span":{
                    "locator":locator,
                    "language":"ENG",
                    "text_hash":sha(text_hash),
                    "artifact_hash":"sha256:c61ea6c41be9c3faf418a80c2ce12fcfb1233b91557eb4157ce2435c40afe5f7",
                },
                "role":role,
                "evidence_state":"DIRECT",
                "derivation_record_id":"run-temporal-reg271-2008-entry-force",
            },
        })

    append({
        "record_id":"run-temporal-article3-2008-unqualified",
        "record_type":"DERIVATION_RUN",
        "created_at":"2026-09-20T17:37:03Z",
        "payload":{
            "derivation_kind":"TEMPORAL_RESOLVE",
            "execution_character":"DETERMINISTIC",
            "implementation":{
                "name":"needle.temporal",
                "version":"temporal-v0.1",
                "config_hash":None,
            },
            "input_record_ids":[
                "support-temporal-reg271-publication",
                "support-temporal-reg271-entry-clause",
                "run-reconcile-article3",
            ],
            "output_entity_refs":[{
                "entity_type":"TEMPORAL_ASSERTION",
                "entity_id":"reg794-art3-2008-unqualified-rules-application-start",
            }],
            "executed_at":"2026-09-20T17:33:14Z",
        },
    })
    for record_id, locator, text_hash, role, created_at in [
        (
            "support-temporal-article3-2008-unqualified-entry",
            "L_2008082EN.01000101.xml#normalized-chars:11427-11554",
            "54d5a5d17e73703f7db092dec7d536193a9946b6d0b56707b0e1aa3acc26f67a",
            "TEMPORAL",
            "2026-09-20T17:37:04Z",
        ),
        (
            "support-temporal-article3-2008-pki-context",
            "L_2008082EN.01000101.xml#normalized-chars:7551-7702",
            "d248b91594760dc2970219153a93862d574eaf13ad6c38c08204f8ec380e4a6d",
            "CONTEXT",
            "2026-09-20T17:37:05Z",
        ),
        (
            "support-temporal-article3-2008-alt-context",
            "L_2008082EN.01000101.xml#normalized-chars:7704-7983",
            "c7fc733a71948a5bd1b40fc83e6e0ba18f073803adaa8bd97bbc73a2f55cdb26",
            "CONTEXT",
            "2026-09-20T17:37:06Z",
        ),
        (
            "support-temporal-article3-2008-invalid-context",
            "L_2008082EN.01000101.xml#normalized-chars:7983-8261",
            "89db2848597405bd3fe6661af754001e96e292a97bb90d23c0d203095d67e5cd",
            "CONTEXT",
            "2026-09-20T17:37:07Z",
        ),
    ]:
        append({
            "record_id":record_id,
            "record_type":"CLAIM_SUPPORT",
            "created_at":created_at,
            "payload":{
                "claim_ref":{
                    "entity_type":"TEMPORAL_ASSERTION",
                    "entity_id":"reg794-art3-2008-unqualified-rules-application-start",
                },
                "source_observation_id":"src-reg271-2008-eng",
                "source_span":{
                    "locator":locator,
                    "language":"ENG",
                    "text_hash":sha(text_hash),
                    "artifact_hash":"sha256:c61ea6c41be9c3faf418a80c2ce12fcfb1233b91557eb4157ce2435c40afe5f7",
                },
                "role":role,
                "evidence_state":"DIRECT",
                "derivation_record_id":"run-temporal-article3-2008-unqualified",
            },
        })

    append({
        "record_id":"run-temporal-reg905-2025-publication",
        "record_type":"DERIVATION_RUN",
        "created_at":"2026-09-20T17:50:00Z",
        "payload":{
            "derivation_kind":"TEMPORAL_RESOLVE",
            "execution_character":"DETERMINISTIC",
            "implementation":{
                "name":"needle.temporal",
                "version":"temporal-v0.1",
                "config_hash":None,
            },
            "input_record_ids":["src-reg905-2025-eng"],
            "output_entity_refs":[{
                "entity_type":"TEMPORAL_ASSERTION",
                "entity_id":"reg905-2025-publication",
            }],
            "executed_at":"2026-09-20T17:49:00Z",
        },
    })
    append({
        "record_id":"support-temporal-reg905-publication-point",
        "record_type":"CLAIM_SUPPORT",
        "created_at":"2026-09-20T17:50:01Z",
        "payload":{
            "claim_ref":{
                "entity_type":"TEMPORAL_ASSERTION",
                "entity_id":"reg905-2025-publication",
            },
            "source_observation_id":"src-reg905-2025-eng",
            "source_span":{
                "locator":"L_202500905EN.doc.fmx.xml#DATE[ISO=20250613]",
                "language":"ENG",
                "text_hash":"sha256:24cac975ccb4483a85feccc1a2e2a57a618dcaab6729e967a91f5c0e29a268aa",
                "artifact_hash":"sha256:91bc8da880879ef9e02ccd7c3bdae09d8b21f496d839d7418bd0a0b088976ff8",
            },
            "role":"TEMPORAL",
            "evidence_state":"DIRECT",
            "derivation_record_id":"run-temporal-reg905-2025-publication",
        },
    })

    append({
        "record_id":"run-temporal-article3-legacy-channel-end",
        "record_type":"DERIVATION_RUN",
        "created_at":"2026-09-20T17:37:08Z",
        "payload":{
            "derivation_kind":"TEMPORAL_RESOLVE",
            "execution_character":"DETERMINISTIC",
            "implementation":{
                "name":"needle.temporal",
                "version":"temporal-v0.1",
                "config_hash":None,
            },
            "input_record_ids":[
                "src-reg905-2025-eng",
                "run-reconcile-article3-p3-2025",
                "run-temporal-article3-p3-2025",
            ],
            "output_entity_refs":[{
                "entity_type":"TEMPORAL_ASSERTION",
                "entity_id":"reg794-art3-p3-legacy-channels-application-end",
            }],
            "executed_at":"2026-09-20T17:23:20Z",
        },
    })
    for record_id, locator, text_hash, role, created_at in [
        (
            "support-temporal-article3-legacy-channel-end-cause",
            "L_202500905EN.000101.fmx.xml#normalized-chars:10410-10461",
            "4b0aea16593c10154d2e827d3979fbe1f1066dab929f69923fd522de1180a80e",
            "CAUSE",
            "2026-09-20T17:37:09Z",
        ),
        (
            "support-temporal-article3-legacy-channel-end-time",
            "L_202500905EN.000101.fmx.xml#normalized-chars:13176-13316",
            "7521c32a90f5ee981042548d552a96206956fd9a1b9c292a5454ee68610371f8",
            "TEMPORAL",
            "2026-09-20T17:37:10Z",
        ),
    ]:
        append({
            "record_id":record_id,
            "record_type":"CLAIM_SUPPORT",
            "created_at":created_at,
            "payload":{
                "claim_ref":{
                    "entity_type":"TEMPORAL_ASSERTION",
                    "entity_id":"reg794-art3-p3-legacy-channels-application-end",
                },
                "source_observation_id":"src-reg905-2025-eng",
                "source_span":{
                    "locator":locator,
                    "language":"ENG",
                    "text_hash":sha(text_hash),
                    "artifact_hash":"sha256:91bc8da880879ef9e02ccd7c3bdae09d8b21f496d839d7418bd0a0b088976ff8",
                },
                "role":role,
                "evidence_state":"DIRECT",
                "derivation_record_id":"run-temporal-article3-legacy-channel-end",
            },
        })

    lineage_by_id = {edge["edge_id"]:edge for edge in lineage["edges"]}

    def lineage_run(
        *,
        run_id: str,
        edge_id: str,
        inputs: list[str],
        execution_character: str,
        created_at: str,
    ) -> None:
        append({
            "record_id":run_id,
            "record_type":"DERIVATION_RUN",
            "created_at":created_at,
            "payload":{
                "derivation_kind":"OTHER",
                "execution_character":execution_character,
                "implementation":{
                    "name":"needle.thread.lineage",
                    "version":"provision-lineage-v0.5",
                    "config_hash":None,
                },
                "input_record_ids":inputs,
                "output_entity_refs":[{
                    "entity_type":"OTHER",
                    "entity_id":edge_id,
                }],
                "executed_at":"2026-09-20T16:34:27Z",
            },
        })

    lineage_run(
        run_id="run-lineage-article3-2008-structural",
        edge_id="reg794-art3-pre2008-replaced-by-2008",
        inputs=[
            "support-mutation-before-checkpoint",
            "support-mutation-after-checkpoint",
            "support-mutation-authentic-cause",
        ],
        execution_character="DETERMINISTIC",
        created_at="2026-09-20T17:11:15Z",
    )
    for record_id, source_id, locator, text_hash, artifact_hash, role, created_at in [
        (
            "support-lineage-article3-2008-cause",
            "src-reg271-2008-eng",
            "L_2008082EN.01000101.xml#normalized-chars:6924-6962",
            "b0b7d3453e67ae9419cd44af197fea25c77526d3d60a64e4e2df2198a731a8f8",
            "sha256:c61ea6c41be9c3faf418a80c2ce12fcfb1233b91557eb4157ce2435c40afe5f7",
            "CAUSE",
            "2026-09-20T17:11:16Z",
        ),
        (
            "support-lineage-article3-2008-before",
            "src-reg794-20070119-eng",
            "Article 3 subtree",
            "d2fed56ff253de5abde15990eb87fe2bcfc65865496249849814553f485311d4",
            "sha256:8d71b04b69b7b757e056c926f20676a355fe2bc5af22407858755efb256eb151",
            "BEFORE",
            "2026-09-20T17:11:17Z",
        ),
        (
            "support-lineage-article3-2008-after",
            "src-reg794-20080414-eng",
            "Article 3 subtree",
            "f36b625716e97e83be29fd99d3be128a2fe6b872cfa78c8df8f6f1b6fa2dbab9",
            "sha256:ccf4e4e92d8191fb22685b0ac9062ef64a816a39c81455f445052a4ad03a68f1",
            "AFTER",
            "2026-09-20T17:11:18Z",
        ),
    ]:
        append({
            "record_id":record_id,
            "record_type":"CLAIM_SUPPORT",
            "created_at":created_at,
            "payload":{
                "claim_ref":{
                    "entity_type":"OTHER",
                    "entity_id":"reg794-art3-pre2008-replaced-by-2008",
                },
                "source_observation_id":source_id,
                "source_span":{
                    "locator":locator,
                    "language":"ENG",
                    "text_hash":sha(text_hash),
                    "artifact_hash":artifact_hash,
                },
                "role":role,
                "evidence_state":"DIRECT",
                "derivation_record_id":"run-lineage-article3-2008-structural",
            },
        })

    lineage_run(
        run_id="run-lineage-article3-p3-2025-structural",
        edge_id="reg794-art3-p3-pre2025-replaced-by-2025",
        inputs=[
            "support-mutation-2025-before",
            "support-mutation-2025-after",
            "support-mutation-2025-cause",
        ],
        execution_character="DETERMINISTIC",
        created_at="2026-09-20T17:11:19Z",
    )
    for record_id, source_id, locator, text_hash, artifact_hash, role, created_at in [
        (
            "support-lineage-article3-p3-2025-cause",
            "src-reg905-2025-eng",
            "L_202500905EN.000101.fmx.xml#normalized-chars:10410-10461",
            "4b0aea16593c10154d2e827d3979fbe1f1066dab929f69923fd522de1180a80e",
            "sha256:91bc8da880879ef9e02ccd7c3bdae09d8b21f496d839d7418bd0a0b088976ff8",
            "CAUSE",
            "2026-09-20T17:11:20Z",
        ),
        (
            "support-lineage-article3-p3-2025-before",
            "src-reg794-20161222-eng",
            "Article 3 > 3 subtree",
            "2fad3273b6ddb7eead8595e94165d02a30f4a149e67dc106a9c3df220b081452",
            "sha256:5aed9f446884f30786a1d96bfe090122dbabfbc6c281059f572377b0c1cc7d6b",
            "BEFORE",
            "2026-09-20T17:11:21Z",
        ),
        (
            "support-lineage-article3-p3-2025-after",
            "src-reg794-20250703-eng",
            "Article 3 > 3 subtree",
            "144a32004977b741ffa02847cffb05c981388243c6dab54e749ee0e71152ec19",
            "sha256:d9a6ae56974c463fec60fd7fb12ee9d49fc4ae8fda226df06ee384463c259ab2",
            "AFTER",
            "2026-09-20T17:11:22Z",
        ),
    ]:
        append({
            "record_id":record_id,
            "record_type":"CLAIM_SUPPORT",
            "created_at":created_at,
            "payload":{
                "claim_ref":{
                    "entity_type":"OTHER",
                    "entity_id":"reg794-art3-p3-pre2025-replaced-by-2025",
                },
                "source_observation_id":source_id,
                "source_span":{
                    "locator":locator,
                    "language":"ENG",
                    "text_hash":sha(text_hash),
                    "artifact_hash":artifact_hash,
                },
                "role":role,
                "evidence_state":"DIRECT",
                "derivation_record_id":"run-lineage-article3-p3-2025-structural",
            },
        })

    lineage_run(
        run_id="run-lineage-article3-parent-2025",
        edge_id="reg794-art3-parent-continues-through-2025-p3-replacement",
        inputs=["support-mutation-2025-cause"],
        execution_character="DETERMINISTIC",
        created_at="2026-09-20T17:11:23Z",
    )
    append({
        "record_id":"support-lineage-article3-parent-2025",
        "record_type":"CLAIM_SUPPORT",
        "created_at":"2026-09-20T17:11:24Z",
        "payload":{
            "claim_ref":{
                "entity_type":"OTHER",
                "entity_id":"reg794-art3-parent-continues-through-2025-p3-replacement",
            },
            "source_observation_id":"src-reg905-2025-eng",
            "source_span":{
                "locator":"L_202500905EN.000101.fmx.xml#normalized-chars:10410-10461",
                "language":"ENG",
                "text_hash":sha(
                    "4b0aea16593c10154d2e827d3979fbe1f1066dab929f69923fd522de1180a80e"
                ),
                "artifact_hash":"sha256:91bc8da880879ef9e02ccd7c3bdae09d8b21f496d839d7418bd0a0b088976ff8",
            },
            "role":"CONTEXT",
            "evidence_state":"DERIVED",
            "derivation_record_id":"run-lineage-article3-parent-2025",
        },
    })

    rule_lineage_specs = [
        {
            "run_id":"run-rule-lineage-notification-2008-2025",
            "edge_id":"reg794-art3-notification-channel-rule-2008-to-2025",
            "inputs":[
                "support-atom-sani",
                "support-atom-2025-notification-channel",
            ],
            "supports":[
                (
                    "support-rule-lineage-notification-2008",
                    "src-reg271-2008-eng",
                    "L_2008082EN.01000101.xml#normalized-chars:7414-7551",
                    "e4be9c1a527f6ef3ec8f4214aae06b58d86477e015651327e71ca83d45aa3d8a",
                    "sha256:c61ea6c41be9c3faf418a80c2ce12fcfb1233b91557eb4157ce2435c40afe5f7",
                ),
                (
                    "support-rule-lineage-notification-2025",
                    "src-reg905-2025-eng",
                    "L_202500905EN.000101.fmx.xml#normalized-chars:10464-10568",
                    "fd6c5bf4d5162189448d1184a230eb81845282acb33d1a344f3aeab6ee6f0e56",
                    "sha256:91bc8da880879ef9e02ccd7c3bdae09d8b21f496d839d7418bd0a0b088976ff8",
                ),
            ],
        },
        {
            "run_id":"run-rule-lineage-correspondence-2008-2025",
            "edge_id":"reg794-art3-correspondence-channel-rule-2008-to-2025",
            "inputs":[
                "support-atom-pki-correspondence",
                "support-atom-2025-correspondence-channel",
            ],
            "supports":[
                (
                    "support-rule-lineage-correspondence-2008",
                    "src-reg271-2008-eng",
                    "L_2008082EN.01000101.xml#normalized-chars:7551-7702",
                    "d248b91594760dc2970219153a93862d574eaf13ad6c38c08204f8ec380e4a6d",
                    "sha256:c61ea6c41be9c3faf418a80c2ce12fcfb1233b91557eb4157ce2435c40afe5f7",
                ),
                (
                    "support-rule-lineage-correspondence-2025",
                    "src-reg905-2025-eng",
                    "L_202500905EN.000101.fmx.xml#normalized-chars:10568-10713",
                    "c55852f95e0a890d02f22ca83e4430861b63e35cadd1f96710e68037a2c81ca5",
                    "sha256:91bc8da880879ef9e02ccd7c3bdae09d8b21f496d839d7418bd0a0b088976ff8",
                ),
            ],
        },
    ]
    created_index = 25
    for spec in rule_lineage_specs:
        lineage_run(
            run_id=spec["run_id"],
            edge_id=spec["edge_id"],
            inputs=spec["inputs"],
            execution_character="MODEL",
            created_at=f"2026-09-20T17:11:{created_index:02d}Z",
        )
        created_index += 1
        for record_id, source_id, locator, text_hash, artifact_hash in spec["supports"]:
            append({
                "record_id":record_id,
                "record_type":"CLAIM_SUPPORT",
                "created_at":f"2026-09-20T17:11:{created_index:02d}Z",
                "payload":{
                    "claim_ref":{
                        "entity_type":"OTHER",
                        "entity_id":spec["edge_id"],
                    },
                    "source_observation_id":source_id,
                    "source_span":{
                        "locator":locator,
                        "language":"ENG",
                        "text_hash":sha(text_hash),
                        "artifact_hash":artifact_hash,
                    },
                    "role":"CONTEXT",
                    "evidence_state":"INTERPRETIVE",
                    "derivation_record_id":spec["run_id"],
                },
            })
            created_index += 1

    append({
        "record_id":"run-thread-p4-continuity-2025",
        "record_type":"DERIVATION_RUN",
        "created_at":"2026-09-20T17:11:31Z",
        "payload":{
            "derivation_kind":"DIFF",
            "execution_character":"DETERMINISTIC",
            "implementation":{
                "name":"needle.mutation.diff.diff_resolved_subtree",
                "version":"mutation-v0.2",
                "config_hash":None,
            },
            "input_record_ids":[
                "run-normalize-2025-before",
                "run-normalize-2025-after",
            ],
            "output_entity_refs":[{
                "entity_type":"OTHER",
                "entity_id":p4["fixture_id"],
            }],
            "executed_at":"2026-09-20T16:50:42Z",
        },
    })
    for record_id, source_id, state, artifact_hash, role, created_at in [
        (
            "support-thread-p4-continuity-before",
            "src-reg794-20161222-eng",
            p4["paragraph4"]["before"],
            p4["paragraph4"]["before"]["artifact_hash"],
            "BEFORE",
            "2026-09-20T17:11:32Z",
        ),
        (
            "support-thread-p4-continuity-after",
            "src-reg794-20250703-eng",
            p4["paragraph4"]["after"],
            p4["paragraph4"]["after"]["artifact_hash"],
            "AFTER",
            "2026-09-20T17:11:33Z",
        ),
    ]:
        append({
            "record_id":record_id,
            "record_type":"CLAIM_SUPPORT",
            "created_at":created_at,
            "payload":{
                "claim_ref":{"entity_type":"OTHER","entity_id":p4["fixture_id"]},
                "source_observation_id":source_id,
                "source_span":{
                    "locator":"Article 3 > 4 subtree",
                    "language":"ENG",
                    "text_hash":sha(state["text_hash"]),
                    "artifact_hash":artifact_hash,
                },
                "role":role,
                "evidence_state":"DIRECT",
                "derivation_record_id":"run-thread-p4-continuity-2025",
            },
        })

    append({
        "record_id":"run-thread-corrigendum-scope-2026",
        "record_type":"DERIVATION_RUN",
        "created_at":"2026-09-20T17:11:34Z",
        "payload":{
            "derivation_kind":"OTHER",
            "execution_character":"DETERMINISTIC",
            "implementation":{
                "name":"needle.thread.corrigendum_scope",
                "version":"thread-v0.1",
                "config_hash":None,
            },
            "input_record_ids":["src-reg905-2025-corrigendum-eng"],
            "output_entity_refs":[{
                "entity_type":"OTHER",
                "entity_id":corrigendum["fixture_id"],
            }],
            "executed_at":observation["observed_at"],
        },
    })
    append({
        "record_id":"support-thread-corrigendum-scope-2026",
        "record_type":"CLAIM_SUPPORT",
        "created_at":"2026-09-20T17:11:35Z",
        "payload":{
            "claim_ref":{
                "entity_type":"OTHER",
                "entity_id":corrigendum["fixture_id"],
            },
            "source_observation_id":"src-reg905-2025-corrigendum-eng",
            "source_span":{
                "locator":observation["target_span"]["locator"],
                "language":"ENG",
                "text_hash":sha(observation["target_span"]["text_hash"]),
                "artifact_hash":observation["artifact_hash"],
            },
            "role":"CONTEXT",
            "evidence_state":"DIRECT",
            "derivation_record_id":"run-thread-corrigendum-scope-2026",
        },
    })

    errors = validate_ledger(records)
    if errors:
        raise AssertionError(
            "generated provenance ledger is invalid:\n" + "\n".join(errors)
        )

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        json.dumps(ledger, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "record_count":len(records),
        "new_record_count":len(records) - len(load(LEDGER_PATH)["records"]),
        "output":str(out),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
