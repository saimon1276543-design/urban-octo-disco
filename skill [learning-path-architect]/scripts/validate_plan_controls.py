#!/usr/bin/env python3
"""Validate compact plan-control records used for actionability and assumptions."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 3 or sys.argv[1] not in {"action", "assumptions"}:
        print("Usage: validate_plan_controls.py action|assumptions <record.json>")
        return 1
    mode, filename = sys.argv[1], sys.argv[2]
    try:
        data = json.loads(Path(filename).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Plan-control validation failed: {exc}")
        return 1

    if mode == "action":
        required = {"primary_action", "evidence", "review_trigger"}
        missing = sorted(required - set(data)) if isinstance(data, dict) else sorted(required)
        if missing:
            print(f"Plan-control validation failed: action record missing {', '.join(missing)}")
            return 1
        if not all(isinstance(data[key], str) and data[key].strip() for key in required):
            print("Plan-control validation failed: action, evidence, and review trigger must be non-empty strings")
            return 1
        parallel = data.get("optional_parallel_action")
        if parallel is not None and not isinstance(parallel, str):
            print("Plan-control validation failed: optional_parallel_action must be a string or null")
            return 1
        print(f"Plan-control validation passed: {filename}")
        return 0

    if not isinstance(data, dict) or not isinstance(data.get("assumptions"), list) or not data["assumptions"]:
        print("Plan-control validation failed: assumptions must be a non-empty array")
        return 1
    allowed_sources = {"stated", "observed", "inferred", "verified", "unknown"}
    allowed_status = {"open", "confirmed", "invalidated", "superseded"}
    for index, item in enumerate(data["assumptions"], start=1):
        if not isinstance(item, dict):
            print(f"Plan-control validation failed: assumption {index} is not an object")
            return 1
        required = {"id", "assumption", "source", "confidence", "impact_if_wrong", "validation_method", "status"}
        missing = sorted(required - set(item))
        if missing:
            print(f"Plan-control validation failed: assumption {index} missing {', '.join(missing)}")
            return 1
        if item["source"] not in allowed_sources or item["status"] not in allowed_status:
            print(f"Plan-control validation failed: assumption {index} has invalid source or status")
            return 1
        if not all(isinstance(item[key], str) and item[key].strip() for key in required - {"confidence"}):
            print(f"Plan-control validation failed: assumption {index} has empty required text")
            return 1
    print(f"Plan-control validation passed: {filename}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
