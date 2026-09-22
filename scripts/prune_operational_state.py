#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from needle.operations.retention import retain_operational_observations


OUT = Path("artifacts/operational-cycle")


def main() -> int:
    state_path = OUT / "state.json"
    results_path = OUT / "results.json"
    report_path = OUT / "report.json"
    state = json.loads(state_path.read_text(encoding="utf-8"))
    results = json.loads(results_path.read_text(encoding="utf-8"))
    report = json.loads(report_path.read_text(encoding="utf-8"))
    before = len(state.get("source_observations", []))
    state = retain_operational_observations(
        state,
        latest_results=results,
        updated_at=state["updated_at"],
    )
    after = len(state.get("source_observations", []))
    state_path.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    report["source_observation_count_after_retention"] = after
    report["source_observation_count_pruned"] = before - after
    report["state_json_bytes_after_retention"] = len(
        json.dumps(state, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    )
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
