#!/usr/bin/env python3
"""Validate compact portfolio decision-engine records."""
from __future__ import annotations

import json
import sys
from pathlib import Path

NODE_TYPES = {"goal", "domain", "family", "foundation", "capability", "bridge", "unit", "milestone", "evidence", "tool", "source", "project", "constraint", "decision"}
EDGE_TYPES = {"hard_prerequisite", "soft_prerequisite", "alternative", "reinforcement", "shared_foundation", "bridge", "integration_dependency", "shared_artifact", "parallel_compatible", "interference_prone", "maintenance", "revalidation", "risk_propagation", "unrelated"}
NODE_STATUS = {"required", "active", "completed", "optional", "deferred", "blocked", "stale", "deprecated", "retired"}


def load(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(str(exc)) from exc


def validate_graph(data: dict) -> list[str]:
    errors: list[str] = []
    nodes = data.get("nodes", [])
    edges = data.get("edges", [])
    if not isinstance(nodes, list) or not isinstance(edges, list):
        return ["nodes and edges must be arrays"]
    node_ids: set[str] = set()
    for index, node in enumerate(nodes):
        if not isinstance(node, dict):
            errors.append(f"nodes[{index}] must be an object")
            continue
        node_id = node.get("node_id")
        if not isinstance(node_id, str) or not node_id.strip() or node_id in node_ids:
            errors.append(f"nodes[{index}] has missing or duplicate node_id")
        else:
            node_ids.add(node_id)
        if node.get("node_type") not in NODE_TYPES:
            errors.append(f"nodes[{index}] has invalid node_type")
        if node.get("status") not in NODE_STATUS:
            errors.append(f"nodes[{index}] has invalid status")
        for ref in node.get("evidence_ids", []) + node.get("source_ids", []):
            if not isinstance(ref, str) or not ref.strip():
                errors.append(f"nodes[{index}] has an invalid reference")
    for index, edge in enumerate(edges):
        if not isinstance(edge, dict):
            errors.append(f"edges[{index}] must be an object")
            continue
        if edge.get("from") not in node_ids or edge.get("to") not in node_ids:
            errors.append(f"edges[{index}] references an unknown node")
        if edge.get("edge_type") not in EDGE_TYPES:
            errors.append(f"edges[{index}] has invalid edge_type")
        if edge.get("from") == edge.get("to") and edge.get("edge_type") == "hard_prerequisite":
            errors.append(f"edges[{index}] contains a self-prerequisite")
    return errors


def main() -> int:
    if len(sys.argv) != 3 or sys.argv[1] not in {"graph", "scenario", "provenance", "complexity"}:
        print("Usage: validate_decision_records.py <graph|scenario|provenance|complexity> <record.json>")
        return 1
    kind, raw_path = sys.argv[1], Path(sys.argv[2])
    try:
        data = load(raw_path)
    except ValueError as exc:
        print(f"Decision-record validation failed: {exc}")
        return 1
    errors: list[str] = []
    if not isinstance(data, dict):
        errors.append("root must be an object")
    elif kind == "graph":
        for field in ("schema_version", "portfolio_id", "nodes", "edges"):
            if field not in data:
                errors.append(f"missing required field: {field}")
        errors.extend(validate_graph(data))
    elif kind == "scenario":
        for field in ("scenario_id", "portfolio_id", "base_revision", "change", "status"):
            if field not in data:
                errors.append(f"missing required field: {field}")
        if data.get("status") not in {"draft", "compared", "selected", "rejected", "deferred"}:
            errors.append("invalid scenario status")
        if not isinstance(data.get("change"), dict) or not data.get("change", {}).get("field"):
            errors.append("change must include a field")
    elif kind == "provenance":
        for field in ("decision_id", "decision", "basis", "affected_ids", "uncertainty", "review_trigger"):
            if field not in data:
                errors.append(f"missing required field: {field}")
        if not isinstance(data.get("affected_ids"), list) or not data["affected_ids"]:
            errors.append("affected_ids must be non-empty")
    else:
        for field in ("budget_id", "portfolio_id", "limits", "observed"):
            if field not in data:
                errors.append(f"missing required field: {field}")
        if isinstance(data.get("limits"), dict) and isinstance(data.get("observed"), dict):
            for key, value in data["observed"].items():
                limit = data["limits"].get(key)
                if isinstance(value, (int, float)) and isinstance(limit, (int, float)) and value < 0:
                    errors.append(f"observed budget cannot be negative: {key}")
    if errors:
        print("Decision-record validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Decision-record validation passed ({kind}): {raw_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
