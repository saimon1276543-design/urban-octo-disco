#!/usr/bin/env python3
"""Validate workspace manifest or conflict record JSON files."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ADAPTER_TYPES = {"workspace", "mcp", "project", "database", "filesystem", "hosted", "artifact", "inline"}
LIFECYCLE = {"draft", "active", "paused", "under_review", "superseded", "archived", "retired"}
RISK = {"low", "medium", "high"}
CONFLICT_STATUS = {"open", "resolved", "abandoned"}
REQUIRED_CAPABILITIES = {"read_plan", "write_plan", "read_progress", "update_progress"}


def validate_manifest(data: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["manifest root must be an object"]
    for key in ("schema_version", "workspace_id", "plan_id", "adapter", "lifecycle_state"):
        if key not in data:
            errors.append(f"manifest missing required field: {key}")
    if data.get("lifecycle_state") not in LIFECYCLE:
        errors.append("manifest has invalid lifecycle_state")
    adapter = data.get("adapter")
    if not isinstance(adapter, dict):
        errors.append("manifest adapter must be an object")
    else:
        for key in ("adapter_id", "adapter_type", "verified_at", "capabilities"):
            if key not in adapter:
                errors.append(f"manifest adapter missing required field: {key}")
        if adapter.get("adapter_type") not in ADAPTER_TYPES:
            errors.append("manifest adapter has invalid adapter_type")
        capabilities = adapter.get("capabilities")
        if not isinstance(capabilities, list):
            errors.append("manifest adapter capabilities must be an array")
        elif adapter.get("persistent") is True and not REQUIRED_CAPABILITIES.issubset(set(capabilities)):
            errors.append("persistent adapter lacks required plan/progress read-write capabilities")
    return errors


def validate_conflict(data: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["conflict root must be an object"]
    for key in ("conflict_id", "workspace_id", "plan_id", "base_revision", "affected_ids", "status"):
        if key not in data:
            errors.append(f"conflict missing required field: {key}")
    if not isinstance(data.get("affected_ids"), list) or not data.get("affected_ids"):
        errors.append("conflict affected_ids must be a non-empty array")
    if data.get("risk") is not None and data.get("risk") not in RISK:
        errors.append("conflict has invalid risk")
    if data.get("status") not in CONFLICT_STATUS:
        errors.append("conflict has invalid status")
    return errors


def main() -> int:
    if len(sys.argv) != 3 or sys.argv[1] not in {"manifest", "conflict"}:
        print("Usage: validate_workspace.py manifest|conflict <file.json>")
        return 1
    kind, filename = sys.argv[1], Path(sys.argv[2])
    try:
        data = json.loads(filename.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Workspace validation failed: {exc}")
        return 1
    errors = validate_manifest(data) if kind == "manifest" else validate_conflict(data)
    if errors:
        print("Workspace validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Workspace {kind} validation passed: {filename}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
