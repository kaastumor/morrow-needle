import hashlib
import json
from pathlib import Path

from needle.mutation.instructions import parse_authentic_corrigendum_replacements


FIXTURE = Path("fixtures/audit/reg2742-money-corrigendum-source-v0.1.json")


def test_pinned_money_corrigendum_evidence_is_self_consistent():
    data = json.loads(FIXTURE.read_text(encoding="utf-8"))
    correction = data["correction"]

    assert hashlib.sha256(correction["text"].encode()).hexdigest() == correction["text_hash"]
    assert hashlib.sha256(correction["before_fragment"].encode()).hexdigest() == correction["before_hash"]
    assert hashlib.sha256(correction["after_fragment"].encode()).hexdigest() == correction["after_hash"]

    parsed = parse_authentic_corrigendum_replacements(
        correction["text"],
        source_id=data["corrigendum"],
        locator=correction["locator"],
    )
    assert len(parsed) == 1
    assert parsed[0]["target_locator"] == correction["target"]
    assert parsed[0]["before_text"] == correction["before_fragment"]
    assert parsed[0]["after_text"] == correction["after_fragment"]


def test_route_failure_is_observation_not_legal_absence():
    data = json.loads(FIXTURE.read_text(encoding="utf-8"))
    route = data["source_route_observation"]

    assert route["observed_http_status"] == 404
    assert route["inference"] == "ROUTE_UNAVAILABLE_NOT_SOURCE_ABSENT"
    assert data["source_observation"]["representation_class"] == "OFFICIAL_HTML"
    assert data["language_scope"]["cross_language_equivalence_assumed"] is False
