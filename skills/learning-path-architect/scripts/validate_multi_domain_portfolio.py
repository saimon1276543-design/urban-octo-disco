#!/usr/bin/env python3
"""Validate a compact multi-domain portfolio manifest."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROUTE_STATES = {"primary", "supporting", "parallel", "sequenced", "deferred", "exploratory", "retired"}
VOLATILITY = {"durable", "medium_term", "volatile", "unknown"}


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_multi_domain_portfolio.py <portfolio.json>")
        return 1
    path = Path(sys.argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Portfolio validation failed: {exc}")
        return 1
    errors: list[str] = []
    if not isinstance(data, dict):
        errors.append("root must be an object")
    else:
        for field in ("schema_version", "portfolio_id", "north_star", "domains", "shared_foundations", "bridges", "active_frontier"):
            if field not in data:
                errors.append(f"missing required field: {field}")
        domains = data.get("domains")
        domain_ids: set[str] = set()
        if not isinstance(domains, list) or not domains:
            errors.append("domains must be a non-empty array")
        else:
            for index, domain in enumerate(domains):
                if not isinstance(domain, dict):
                    errors.append(f"domains[{index}] must be an object")
                    continue
                for field in ("domain_id", "name", "outcome", "target_level", "route_state"):
                    if not isinstance(domain.get(field), str) or not domain[field].strip():
                        errors.append(f"domains[{index}] has invalid {field}")
                domain_id = domain.get("domain_id")
                if isinstance(domain_id, str):
                    if domain_id in domain_ids:
                        errors.append(f"duplicate domain_id: {domain_id}")
                    domain_ids.add(domain_id)
                if domain.get("route_state") not in ROUTE_STATES:
                    errors.append(f"domains[{index}] has invalid route_state")
                if domain.get("volatility", "unknown") not in VOLATILITY:
                    errors.append(f"domains[{index}] has invalid volatility")
        bridges = data.get("bridges")
        if not isinstance(bridges, list):
            errors.append("bridges must be an array")
        else:
            bridge_ids: set[str] = set()
            for index, bridge in enumerate(bridges):
                if not isinstance(bridge, dict):
                    errors.append(f"bridges[{index}] must be an object")
                    continue
                for field in ("bridge_id", "name", "outcome"):
                    if not isinstance(bridge.get(field), str) or not bridge[field].strip():
                        errors.append(f"bridges[{index}] has invalid {field}")
                if not isinstance(bridge.get("domains"), list) or len(bridge["domains"]) < 2:
                    errors.append(f"bridges[{index}] must serve at least two domains")
                bridge_id = bridge.get("bridge_id")
                if isinstance(bridge_id, str):
                    if bridge_id in bridge_ids:
                        errors.append(f"duplicate bridge_id: {bridge_id}")
                    bridge_ids.add(bridge_id)
        if not isinstance(data.get("active_frontier"), list):
            errors.append("active_frontier must be an array")
        limit = data.get("parallel_limit")
        if limit is not None and (not isinstance(limit, int) or limit < 1):
            errors.append("parallel_limit must be a positive integer or null")
    if errors:
        print("Portfolio validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Portfolio validation passed: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
