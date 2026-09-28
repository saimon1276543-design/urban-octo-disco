#!/usr/bin/env python3
"""Validate compact freshness-control records."""
from __future__ import annotations

import json
import sys
from pathlib import Path

HEALTH = {"current", "aging", "stale", "inaccessible", "contradicted", "context_limited"}
CLAIM_STATUS = {"accepted", "unverified", "conflicting", "rejected", "expired"}
UPDATE_MODES = {"targeted_refresh", "domain_refresh", "portfolio_drift_scan", "full_portfolio_review"}
UPDATE_STATUS = {"planned", "completed", "partial", "failed", "rolled_back"}
QUEUE_REASONS = {"expiry", "version_change", "deprecation", "source_conflict", "safety_change", "evidence_shift", "context_change", "integration_failure", "learner_request"}
QUEUE_STATUS = {"queued", "researching", "verified_unchanged", "updated", "blocked", "dismissed"}


def main() -> int:
    if len(sys.argv) != 3 or sys.argv[1] not in {"ledger", "queue", "run"}:
        print("Usage: validate_update_records.py <ledger|queue|run> <record.json>")
        return 1
    kind, raw_path = sys.argv[1], Path(sys.argv[2])
    try:
        data = json.loads(raw_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Update-record validation failed: {exc}")
        return 1
    errors: list[str] = []
    if not isinstance(data, dict):
        errors.append("root must be an object")
    elif kind == "ledger":
        for field in ("schema_version", "portfolio_id", "research_cutoff", "sources", "claims"):
            if field not in data:
                errors.append(f"missing required field: {field}")
        source_ids: set[str] = set()
        for index, source in enumerate(data.get("sources", [])):
            if not isinstance(source, dict):
                errors.append(f"sources[{index}] must be an object")
                continue
            source_id = source.get("source_id")
            if not isinstance(source_id, str) or not source_id.strip():
                errors.append(f"sources[{index}] has invalid source_id")
            elif source_id in source_ids:
                errors.append(f"duplicate source_id: {source_id}")
            else:
                source_ids.add(source_id)
            if source.get("health") not in HEALTH:
                errors.append(f"sources[{index}] has invalid health")
        claim_ids: set[str] = set()
        for index, claim in enumerate(data.get("claims", [])):
            if not isinstance(claim, dict):
                errors.append(f"claims[{index}] must be an object")
                continue
            claim_id = claim.get("claim_id")
            if not isinstance(claim_id, str) or not claim_id.strip() or claim_id in claim_ids:
                errors.append(f"claims[{index}] has missing or duplicate claim_id")
            else:
                claim_ids.add(claim_id)
            if not isinstance(claim.get("source_ids"), list) or not claim["source_ids"]:
                errors.append(f"claims[{index}] must cite at least one source")
            elif any(source_id not in source_ids for source_id in claim["source_ids"]):
                errors.append(f"claims[{index}] cites an unknown source_id")
            if claim.get("status") not in CLAIM_STATUS:
                errors.append(f"claims[{index}] has invalid status")
    elif kind == "queue":
        for field in ("schema_version", "portfolio_id", "items"):
            if field not in data:
                errors.append(f"missing required field: {field}")
        queue_ids: set[str] = set()
        for index, item in enumerate(data.get("items", [])):
            if not isinstance(item, dict):
                errors.append(f"items[{index}] must be an object")
                continue
            queue_id = item.get("queue_id")
            if not isinstance(queue_id, str) or not queue_id.strip() or queue_id in queue_ids:
                errors.append(f"items[{index}] has missing or duplicate queue_id")
            else:
                queue_ids.add(queue_id)
            if item.get("reason") not in QUEUE_REASONS:
                errors.append(f"items[{index}] has invalid reason")
            if item.get("status") not in QUEUE_STATUS:
                errors.append(f"items[{index}] has invalid status")
    else:
        for field in ("update_run_id", "portfolio_id", "mode", "started_at", "status", "scope", "changes"):
            if field not in data:
                errors.append(f"missing required field: {field}")
        if data.get("mode") not in UPDATE_MODES:
            errors.append("invalid update mode")
        if data.get("status") not in UPDATE_STATUS:
            errors.append("invalid update status")
        if not isinstance(data.get("scope"), list) or not data["scope"]:
            errors.append("scope must be a non-empty array")
        if not isinstance(data.get("changes"), list):
            errors.append("changes must be an array")
    if errors:
        print("Update-record validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Update-record validation passed ({kind}): {raw_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
