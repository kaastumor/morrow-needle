import copy
import json
from pathlib import Path

import pytest

from scripts.validate_adversarial_corpus import CorpusValidationError, validate


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "corpus" / "index-v0.1.json"


def load_index():
    return json.loads(INDEX.read_text(encoding="utf-8"))


def test_public_adversarial_corpus_is_valid():
    validate(load_index(), ROOT)


def test_duplicate_case_ids_fail_closed():
    data = load_index()
    duplicate = copy.deepcopy(data["cases"][0])
    data["cases"].append(duplicate)
    data["case_count"] += 1

    with pytest.raises(CorpusValidationError, match="duplicate case id"):
        validate(data, ROOT)


def test_public_case_cannot_be_marked_blind_reusable():
    data = load_index()
    data["cases"][0]["exposure"]["blind_reuse"] = True

    with pytest.raises(CorpusValidationError, match="blind_reuse=false"):
        validate(data, ROOT)


def test_missing_artifact_path_fails_closed():
    data = load_index()
    data["cases"][0]["evidence_refs"].append("path:fixtures/does-not-exist.json")

    with pytest.raises(CorpusValidationError, match="missing referenced path"):
        validate(data, ROOT)


def test_case_must_reference_its_provenance_issue():
    data = load_index()
    issue = data["cases"][0]["provenance"]["issue"]
    data["cases"][0]["evidence_refs"].remove(f"issue:{issue}")

    with pytest.raises(CorpusValidationError, match="must include issue"):
        validate(data, ROOT)


def test_artifact_path_cannot_escape_repository():
    data = load_index()
    data["cases"][0]["evidence_refs"].append("path:../outside.json")

    with pytest.raises(CorpusValidationError, match="stay inside repository"):
        validate(data, ROOT)
