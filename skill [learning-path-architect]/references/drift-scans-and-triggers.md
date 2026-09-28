# Drift Scans and Update Triggers

Use this reference for ongoing portfolios whose topics change over time.

## Trigger types

- Learner requests a current refresh.
- A new session begins after a freshness boundary.
- A volatile version or platform changes.
- A source or connector reports a change.
- A regulatory, security, safety, or ethics alert occurs.
- A scheduled review arrives.
- A bridge or integration studio exposes incompatibility.
- The learner’s role, goal, deadline, capacity, access, or region changes.

## Scan sequence

First inspect the source ledger, expiry flags, unresolved conflicts, version boundaries, and learner-context changes. Then prioritize by safety, route impact, active-frontier relevance, volatility, and evidence criticality. Research flagged claims against authoritative sources, record unchanged areas as checked, and queue inaccessible or ambiguous areas instead of silently trusting stale content.

A drift scan should answer: what changed, what did not change, which nodes are affected, which dependencies or evidence criteria move, whether the active frontier changes, what was not researched, and when to scan again.

## Capability-dependent automation

Optional workspace capabilities include `read_source_ledger`, `update_source_ledger`, `run_drift_scan`, `queue_revalidation`, `record_update_run`, `subscribe_to_changes`, `recompute_impact`, and `create_revision_diff`. Use only capabilities discovered and verified in the current environment. A schedule or subscription can trigger a review, but it does not itself prove that sources were checked or that a route was safely updated.
