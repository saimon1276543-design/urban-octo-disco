# Decision Provenance and Query Modes

## Decision provenance

For each material route decision record the decision, alternatives considered, evidence or assumption used, affected IDs, accepted trade-off, uncertainty, reversal condition, and review trigger. Link to stable graph IDs, source claims, tracker observations, diagnostics, or learner statements. Provide concise rationale, not hidden chain-of-thought.

## Query modes

Answer portfolio questions from the smallest relevant graph slice. Supported queries include: what should I do today; why is this prerequisite here; what changed; what can I skip; which domain is the bottleneck; what happens if I add/remove a domain; which foundations are shared; what is stale; which alternatives remain; what evidence unlocks the next bridge; what is the smallest safe project; and what can I do offline.

For each query, expose the answer, affected IDs, assumptions, evidence or source basis, next action, and relevant uncertainty. Do not regenerate the full portfolio for a local query unless the query exposes a global inconsistency.
