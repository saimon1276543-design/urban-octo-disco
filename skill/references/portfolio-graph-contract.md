# Portfolio Graph Contract

Use this reference when a portfolio is large enough that dependencies, bridges, evidence, tools, sources, or revisions must be queried reliably. The graph is a planning representation, not a claim that learning is mathematically solvable.

## Node types

Use stable IDs for goals, domains, families, foundations, capabilities, learning units, milestones, evidence, tools, sources, projects, constraints, and decisions. Each required goal must map to at least one capability and eventual evidence route.

## Edge types

Use only decision-relevant edges: hard prerequisite, soft prerequisite, alternative, reinforcement, shared foundation, bridge, integration dependency, shared artifact, parallel-compatible, interference-prone, maintenance, revalidation, risk propagation, or unrelated.

## Required node fields

Record outcome, target level, route state, evidence status, volatility, safety state, source IDs where current claims matter, effort/capacity attributes when scheduling matters, and stable-ID revision lineage.

## Invariants

A valid graph has no orphaned required goals, dangling prerequisite references, unexplained cycles, duplicated shared foundations, bridges serving fewer than two domains, active nodes without an action/evidence boundary, or deprecated tools remaining as the only route when replacement is required. Every route change explains its affected IDs and preserves unaffected evidence.

Run graph integrity before scenario comparison, major revision, or persistent mutation. Report defects and the smallest repair; do not silently invent nodes to make the graph pass.
