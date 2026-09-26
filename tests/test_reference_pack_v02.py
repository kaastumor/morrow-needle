import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from scripts import build_reference_pack_v02 as builder
from scripts.validate_reference_pack_v02 import (
    GENERATED_FILES,
    PACK_DIR_REL,
    ReferencePackV02ValidationError,
    validate_pack,
)


ROOT = Path(__file__).resolve().parents[1]
V01_DIR = ROOT / "release" / "needle-reference-pack-v0.1"
V02_DIR = ROOT / PACK_DIR_REL


def v01_bytes():
    return {
        path.name: path.read_bytes()
        for path in V01_DIR.iterdir()
        if path.is_file()
    }


def generated_v02_bytes():
    return {name: (V02_DIR / name).read_bytes() for name in GENERATED_FILES}


def test_reference_pack_v02_is_valid():
    result = validate_pack(ROOT)
    assert result == {
        "cases": 81,
        "trap_classes": 26,
        "issue_owners": 54,
        "path_owners": 32,
        "payload_files": 7,
    }


def test_v02_builder_is_stable_and_v01_remains_byte_identical():
    before_v01 = v01_bytes()
    before_v02 = generated_v02_bytes()

    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "build_reference_pack_v02.py")],
        cwd=ROOT,
        check=True,
    )
    after_first_v01 = v01_bytes()
    after_first_v02 = generated_v02_bytes()

    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "build_reference_pack_v02.py")],
        cwd=ROOT,
        check=True,
    )
    after_second_v01 = v01_bytes()
    after_second_v02 = generated_v02_bytes()

    assert before_v01 == after_first_v01 == after_second_v01
    assert before_v02 == after_first_v02 == after_second_v02
    validate_pack(ROOT)


def test_v02_guide_exposes_failure_analysis_contract():
    guide = (V02_DIR / "failure-analysis-guide.md").read_text(encoding="utf-8")
    assert "NO_EXISTING_CLASS_MATCH" in guide
    assert "Omit rather than synthesize." in guide
    assert "issue339-external-failure-packet-use-2026-09-26.md" in guide
    assert "PASS/FAIL" in guide


def test_v02_membership_fails_closed_on_unearned_packet_file(tmp_path):
    (tmp_path / "corpus").mkdir()
    shutil.copy2(
        ROOT / "corpus" / "index-v0.1.json",
        tmp_path / "corpus" / "index-v0.1.json",
    )
    release_dir = tmp_path / "release"
    release_dir.mkdir()
    shutil.copytree(V01_DIR, release_dir / "needle-reference-pack-v0.1")
    shutil.copytree(V02_DIR, release_dir / "needle-reference-pack-v0.2")

    target = release_dir / "needle-reference-pack-v0.2"
    (target / "analysis-packets.jsonl").write_text(
        "{}\n",
        encoding="utf-8",
        newline="\n",
    )

    with pytest.raises(
        ReferencePackV02ValidationError,
        match="file membership mismatch",
    ):
        validate_pack(
            tmp_path,
            run_canonical_validation=False,
        )
