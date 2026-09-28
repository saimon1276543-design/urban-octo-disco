#!/usr/bin/env python3
"""Validate a compact learner-state and intervention record."""
from __future__ import annotations

import json
import sys
from pathlib import Path

FAILURES = {"route", "prerequisite", "concept", "procedure", "transfer", "retrieval", "environment", "overload", "evidence", "one_off_shock"}
DECISIONS = {"advance", "reinforce", "remediate", "maintain", "narrow", "re-diagnose"}


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_adaptive_records.py <record.json>")
        return 1
    path = Path(sys.argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Adaptive-record validation failed: {exc}")
        return 1
    required = {"plan_id", "node_id", "capability_estimate", "error_pattern", "next_diagnostic", "failure_class", "smallest_intervention", "expected_signal", "recheck_trigger", "decision"}
    if not isinstance(data, dict):
        print("Adaptive-record validation failed: root must be an object")
        return 1
    missing = sorted(required - set(data))
    if missing:
        print(f"Adaptive-record validation failed: missing {', '.join(missing)}")
        return 1
    for field in required - {"failure_class", "decision"}:
        if not isinstance(data[field], str) or not data[field].strip():
            print(f"Adaptive-record validation failed: {field} must be a non-empty string")
            return 1
    if data["failure_class"] not in FAILURES:
        print("Adaptive-record validation failed: invalid failure_class")
        return 1
    if data["decision"] not in DECISIONS:
        print("Adaptive-record validation failed: invalid decision")
        return 1
    print(f"Adaptive-record validation passed: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
