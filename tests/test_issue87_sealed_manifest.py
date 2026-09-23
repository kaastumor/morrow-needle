import json
from pathlib import Path


MANIFEST = json.loads(
    Path(
        "fixtures/value-gates/issue87-sealed-manifest-v0.1.json"
    ).read_text(encoding="utf-8")
)


def test_issue87_manifest_commits_three_external_artifacts():
    artifacts = MANIFEST["sealed_artifacts"]

    assert [item["filename"] for item in artifacts] == [
        "issue87-stage-a-packets.json",
        "issue87-stage-b-packets.json",
        "issue87-sealed-answer-key.json",
    ]
    assert all(item["repository_contains_plaintext"] is False for item in artifacts)


def test_issue87_manifest_hashes_are_sha256_hex():
    for item in MANIFEST["sealed_artifacts"]:
        digest = item["sha256"]
        assert len(digest) == 64
        int(digest, 16)


def test_issue87_preserves_external_execution_boundary():
    assert MANIFEST["status"] == "SEALED_AWAITING_INDEPENDENT_EXECUTION"
    assert "Fresh investigators" in MANIFEST["acceptance_boundary"]
    assert "Do not commit or reveal plaintext" in MANIFEST["blinding_rule"]
