#!/usr/bin/env python3
"""Validate a Learning Path Architect progress JSON file."""
from __future__ import annotations

import json
import sys
from pathlib import Path

STATUSES = {
    "locked", "available", "active", "blocked", "complete",
    "maintain", "deferred", "retired",
}
EFFORT_BANDS = {"unknown", "small", "medium", "large", "very-large"}
CONFIDENCE = {"unknown", "low", "medium", "high"}
LIFECYCLE = {"draft", "active", "paused", "under_review", "superseded", "archived", "retired"}
EVIDENCE_SOURCE = {"unknown", "self_report", "uploaded_artifact", "verified_file", "automated_test", "mentor_confirmation"}
REVIEW_STATE = {"not_due", "due", "stale", "conflicted"}
STATE_SOURCES = {"stated", "observed", "artifact", "automated", "mentor_confirmed", "unknown"}
SUPPORT_LEVELS = {"guided", "familiar_independent", "bounded_unfamiliar", "ambiguous_open_ended", "unknown"}
FAILURE_CLASSES = {"route", "prerequisite", "concept", "procedure", "transfer", "retrieval", "environment", "overload", "evidence", "one_off_shock"}
INTERVENTION_STATUS = {"proposed", "active", "effective", "ineffective", "replaced"}


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_progress.py <progress.json>")
        return 1
    path = Path(sys.argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Progress validation failed: {exc}")
        return 1

    errors: list[str] = []
    if not isinstance(data, dict):
        errors.append("root must be an object")
    else:
        for key in ("schema_version", "plan_id", "nodes"):
            if key not in data:
                errors.append(f"missing required field: {key}")
        nodes = data.get("nodes")
        if not isinstance(nodes, list):
            errors.append("nodes must be an array")
        else:
            seen: set[str] = set()
            for index, node in enumerate(nodes):
                if not isinstance(node, dict):
                    errors.append(f"nodes[{index}] must be an object")
                    continue
                node_id = node.get("node_id")
                if not isinstance(node_id, str) or not node_id.strip():
                    errors.append(f"nodes[{index}] has invalid node_id")
                elif node_id in seen:
                    errors.append(f"duplicate node_id: {node_id}")
                else:
                    seen.add(node_id)
                if node.get("status") not in STATUSES:
                    errors.append(f"nodes[{index}] has invalid status")
                if node.get("confidence", "unknown") not in CONFIDENCE:
                    errors.append(f"nodes[{index}] has invalid confidence")
                if node.get("evidence_source", "unknown") not in EVIDENCE_SOURCE:
                    errors.append(f"nodes[{index}] has invalid evidence_source")
                if "evidence_verified" in node and not isinstance(node["evidence_verified"], bool):
                    errors.append(f"nodes[{index}] evidence_verified must be boolean")
                if node.get("review_state", "not_due") not in REVIEW_STATE:
                    errors.append(f"nodes[{index}] has invalid review_state")
        capacity = data.get("capacity")
        if capacity is not None:
            if not isinstance(capacity, dict):
                errors.append("capacity must be an object")
            else:
                if capacity.get("available_effort_band", "unknown") not in EFFORT_BANDS:
                    errors.append("capacity has invalid available_effort_band")
                limit = capacity.get("parallel_branch_limit")
                if limit is not None and (not isinstance(limit, int) or limit < 1):
                    errors.append("capacity parallel_branch_limit must be a positive integer or null")
                for field in ("nominal_units", "fixed_overhead_units", "maintenance_units", "recovery_reserve_units"):
                    value = capacity.get(field)
                    if value is not None and (not isinstance(value, (int, float)) or value < 0):
                        errors.append(f"capacity {field} must be a nonnegative number or null")
                for field in ("reliability", "learning_fraction"):
                    value = capacity.get(field)
                    if value is not None and (not isinstance(value, (int, float)) or not 0 < value <= 1):
                        errors.append(f"capacity {field} must be between 0 and 1")
                throughput = capacity.get("observed_throughput_ratio")
                if throughput is not None and (not isinstance(throughput, (int, float)) or throughput <= 0):
                    errors.append("capacity observed_throughput_ratio must be positive or null")
        if data.get("lifecycle_state", "active") not in LIFECYCLE:
            errors.append("invalid lifecycle_state")
        learner_state = data.get("learner_state")
        if learner_state is not None:
            if not isinstance(learner_state, dict):
                errors.append("learner_state must be an object")
            else:
                if learner_state.get("confidence", "unknown") not in CONFIDENCE:
                    errors.append("learner_state has invalid confidence")
                if learner_state.get("evidence_source", "unknown") not in STATE_SOURCES:
                    errors.append("learner_state has invalid evidence_source")
                if learner_state.get("support_level", "unknown") not in SUPPORT_LEVELS:
                    errors.append("learner_state has invalid support_level")
                if "error_patterns" in learner_state and not isinstance(learner_state["error_patterns"], list):
                    errors.append("learner_state error_patterns must be an array")
        interventions = data.get("interventions")
        if interventions is not None:
            if not isinstance(interventions, list):
                errors.append("interventions must be an array")
            else:
                seen_interventions: set[str] = set()
                for index, intervention in enumerate(interventions):
                    if not isinstance(intervention, dict):
                        errors.append(f"interventions[{index}] must be an object")
                        continue
                    for field in ("intervention_id", "node_id", "action", "recheck_trigger"):
                        if not isinstance(intervention.get(field), str) or not intervention[field].strip():
                            errors.append(f"interventions[{index}] has invalid {field}")
                    intervention_id = intervention.get("intervention_id")
                    if isinstance(intervention_id, str) and intervention_id in seen_interventions:
                        errors.append(f"duplicate intervention_id: {intervention_id}")
                    elif isinstance(intervention_id, str):
                        seen_interventions.add(intervention_id)
                    if intervention.get("failure_class") not in FAILURE_CLASSES:
                        errors.append(f"interventions[{index}] has invalid failure_class")
                    if intervention.get("status") not in INTERVENTION_STATUS:
                        errors.append(f"interventions[{index}] has invalid status")
        history = data.get("learner_history")
        if history is not None:
            if not isinstance(history, dict):
                errors.append("learner_history must be an object")
            else:
                for field in ("recurring_error_patterns", "effective_interventions", "abandoned_methods"):
                    if field in history and not isinstance(history[field], list):
                        errors.append(f"learner_history {field} must be an array")
                if history.get("confidence", "unknown") not in CONFIDENCE:
                    errors.append("learner_history has invalid confidence")

    if errors:
        print("Progress validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Progress validation passed: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
