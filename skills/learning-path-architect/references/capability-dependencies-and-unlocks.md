# Capability Dependencies and Unlocks

Use this reference to decide what can start, what must wait, and what evidence activates a route.

## Edge types

Use hard prerequisite, soft prerequisite, alternative prerequisite, reinforcement loop, shared foundation, bridge competency, maintenance dependency, operational dependency, and safety/authorization gate. Keep learning dependencies separate from deployment dependencies.

## Unlock rules

Unlocks are partial and contextual. A small local task can become active before production, clinical, or independent capability. An unlock record should state the capability, context, evidence required, evidence present, remaining gap, confidence, and next recheck.

Examples: a learner who can parse a fixture may begin a bounded crawler task but not an enterprise distributed crawler; an EEG decoder may unlock offline evaluation but not clinical use; an MCP server tested locally may unlock integration testing but not public exposure.

## Parallelism and bottlenecks

Identify high-leverage bottlenecks, but avoid making every path linear. Parallel work is justified only after checking conceptual prerequisites, setup burden, switching cost, feedback latency, resource constraints, safety, and minimum continuity. A bridge must serve at least two families, change a real route, have an observable outcome, and remain bounded.

When evidence is missing, choose a reversible pilot rather than silently assuming readiness. Preserve deferred routes and explain the condition that would activate them.
