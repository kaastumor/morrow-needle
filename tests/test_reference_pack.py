import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from scripts import build_reference_pack as builder
from scripts.validate_reference_pack import (
    GENERATED_FILES,
    PACK_DIR_REL,
    ReferencePackValidationError,
    validate_pack,
)


ROOT = Path(__file__).resolve().parents[1]
PACK_DIR = ROOT / PACK_DIR_REL


def generated_bytes():
    return {name: (PACK_DIR / name).read_bytes() for name in GENERATED_FILES}


def test_reference_pack_is_valid():
    result = validate_pack(ROOT)
    assert result == {
        "cases": 81,
        "trap_classes": 26,
        "issue_owners": 54,
        "path_owners": 32,
        "payload_files": 6,
    }


def test_reference_pack_builder_is_byte_stable():
    before = generated_bytes()

    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "build_reference_pack.py")],
        cwd=ROOT,
        check=True,
    )
    after_first = generated_bytes()

    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "build_reference_pack.py")],
        cwd=ROOT,
        check=True,
    )
    after_second = generated_bytes()

    assert before == after_first == after_second


def test_reference_pack_fails_closed_on_generated_case_drift(tmp_path):
    (tmp_path / "corpus").mkdir()
    shutil.copy2(
        ROOT / "corpus" / "index-v0.1.json",
        tmp_path / "corpus" / "index-v0.1.json",
    )
    target_pack = tmp_path / PACK_DIR_REL
    target_pack.parent.mkdir(parents=True)
    shutil.copytree(PACK_DIR, target_pack)

    cases_path = target_pack / "cases.jsonl"
    cases_path.write_text(
        cases_path.read_text(encoding="utf-8").replace(
            '"future_use":"REGRESSION_ONLY"',
            '"future_use":"FRESH"',
            1,
        ),
        encoding="utf-8",
        newline="\n",
    )

    with pytest.raises(ReferencePackValidationError, match="generated pack file drift"):
        validate_pack(
            tmp_path,
            run_canonical_validation=False,
        )


def test_pack_membership_fails_closed_on_extra_file(tmp_path):
    (tmp_path / "corpus").mkdir()
    shutil.copy2(
        ROOT / "corpus" / "index-v0.1.json",
        tmp_path / "corpus" / "index-v0.1.json",
    )
    target_pack = tmp_path / PACK_DIR_REL
    target_pack.parent.mkdir(parents=True)
    shutil.copytree(PACK_DIR, target_pack)
    (target_pack / "unexpected.txt").write_text("unexpected\n", encoding="utf-8")

    with pytest.raises(ReferencePackValidationError, match="file membership mismatch"):
        validate_pack(
            tmp_path,
            run_canonical_validation=False,
        )
