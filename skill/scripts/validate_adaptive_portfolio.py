#!/usr/bin/env python3
"""Validate adaptive portfolio records and structured output evaluations."""
from __future__ import annotations

import json
import sys
from pathlib import Path

STATES = {"unfamiliar", "exposed", "guided", "practiced", "transferable", "retained", "maintained", "stale", "contradicted"}
EXPERIMENT_STATES = {"proposed", "running", "continue", "revise", "stop", "revert"}
MIGRATION_STATES = {"preview", "ready", "committed", "quarantined", "rolled_back"}
EVALUATION_RESULTS = {"pass", "revise", "blocked", "unavailable"}


def load(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(kind: str, data: object) -> list[str]:
    if not isinstance(data, dict):
        return ["root must be an object"]
    errors: list[str] = []
    if kind == "state":
        for key in ("schema_version", "node_id", "state", "context", "evidence_date", "confidence"):
            if key not in data:
                errors.append(f"missing required field: {key}")
        if data.get("state") not in STATES:
            errors.append("invalid capability state")
    elif kind == "experiment":
        for key in ("schema_version", "experiment_id", "hypothesis", "change", "boundary", "success_evidence", "failure_signal", "decision_state"):
            if key not in data:
                errors.append(f"missing required field: {key}")
        if data.get("decision_state") not in EXPERIMENT_STATES:
            errors.append("invalid experiment decision_state")
    elif kind == "migration":
        for key in ("schema_version", "migration_id", "source_version", "target_version", "status", "preserved_ids", "affected_paths", "conflicts"):
            if key not in data:
                errors.append(f"missing required field: {key}")
        if data.get("status") not in MIGRATION_STATES:
            errors.append("invalid migration status")
    elif kind == "evaluation":
        for key in ("schema_version", "case_id", "evaluation_mode", "result", "dimensions"):
            if key not in data:
                errors.append(f"missing required field: {key}")
        if data.get("result") not in EVALUATION_RESULTS:
            errors.append("invalid evaluation result")
        dimensions = data.get("dimensions")
        if not isinstance(dimensions, dict):
            errors.append("dimensions must be an object")
        else:
            for name, score in dimensions.items():
                if score not in {0, 1, 2, "unavailable"}:
                    errors.append(f"invalid score for dimension {name}")
    else:
        errors.append(f"unknown record kind: {kind}")
    return errors


def main() -> int:
    if len(sys.argv) != 3 or sys.argv[1] not in {"state", "experiment", "migration", "evaluation"}:
        print("Usage: validate_adaptive_portfolio.py state|experiment|migration|evaluation <record.json>")
        return 1
    kind, path = sys.argv[1], Path(sys.argv[2])
    try:
        errors = validate(kind, load(path))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Adaptive portfolio validation failed: {exc}")
        return 1
    if errors:
        print("Adaptive portfolio validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Adaptive portfolio validation passed ({kind}): {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
