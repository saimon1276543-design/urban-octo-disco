#!/usr/bin/env python3
"""Compare structured evaluation records across two skill revisions."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def score(record: dict) -> int:
    total = 0
    for value in record.get("dimensions", {}).values():
        if isinstance(value, int):
            total += value
    return total


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("baseline", type=Path)
    parser.add_argument("candidate", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    baseline = json.loads(args.baseline.read_text(encoding="utf-8"))
    candidate = json.loads(args.candidate.read_text(encoding="utf-8"))
    base_score, candidate_score = score(baseline), score(candidate)
    output = {
        "schema_version": "1.0",
        "case_id": candidate.get("case_id", baseline.get("case_id")),
        "baseline_result": baseline.get("result"),
        "candidate_result": candidate.get("result"),
        "baseline_score": base_score,
        "candidate_score": candidate_score,
        "score_delta": candidate_score - base_score,
        "changed_dimensions": sorted(set(baseline.get("dimensions", {})) | set(candidate.get("dimensions", {}))),
        "interpretation": "structural comparison only; not proof of learner outcomes"
    }
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(f"Benchmark comparison written: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
