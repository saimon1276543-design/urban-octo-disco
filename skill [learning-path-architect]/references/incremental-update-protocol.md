# Incremental Update and Impact Protocol

Use this protocol when current information, a source, tool, regulation, learner context, or bridge dependency changes.

1. Identify the changed claim, source, domain, or constraint.
2. Map it to stable source IDs, node IDs, bridge IDs, evidence checkpoints, and affected interfaces.
3. Classify the change and confidence.
4. Traverse direct and downstream dependencies; include bridge and integration interfaces.
5. Revalidate only the affected subgraph plus its interfaces and evidence criteria.
6. Recompute volatile nodes, prerequisite edges, maintenance/revalidation obligations, and active frontier where relevant.
7. Preserve unaffected foundations, completed evidence, learner history, and unchanged route decisions.
8. Produce a revision diff showing unchanged, updated, added, deprecated, deferred, and unresolved items.
9. Checkpoint and verify before promoting the new authoritative revision.

If a source is stale but no consequential claim is affected, update the ledger and queue revalidation without rebuilding the route. If an official deprecation, safety change, prerequisite shift, or evidence change affects the route, update the impacted subgraph and explain the downstream consequences.

When sources conflict, preserve both claims with region/version/date context, prefer the strongest applicable authority, mark unresolved decisions, and escalate safety, clinical, regulatory, or security conflicts. Do not silently choose a global answer.
