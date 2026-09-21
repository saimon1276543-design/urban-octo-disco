# Assumption and Plan-Fragility Ledger

Use this reference for complex, long-horizon, time-sensitive, or adaptive plans. Record assumptions that could change the route rather than listing every minor uncertainty.

## Ledger

| Assumption ID | Assumption | Source | Confidence | If wrong, what changes? | Validation method | Review trigger | Status |
|---|---|---|---|---|---|---|---|
| A1 | {{}} | stated / observed / inferred / verified / unknown | low / medium / high | {{}} | {{}} | {{}} | open / confirmed / invalidated / superseded |

## Fragility ranking

Rank assumptions by consequence and uncertainty:

- **High fragility:** if wrong, it changes the north star, primary route, safety boundary, or critical path.
- **Medium fragility:** if wrong, it changes sequencing, scope, concurrency, or evidence requirements.
- **Low fragility:** if wrong, it changes an example, tool choice, or optional extension without harming the core route.

Validate high-fragility assumptions first. Do not spend research or intake effort on low-fragility details that do not change the next decision.

## Source labels

Use **stated** for what the learner explicitly supplied, **observed** for tracker or performance evidence, **inferred** for a conservative interpretation, **verified** for an externally or workspace-confirmed fact, and **unknown** when no basis exists. Never silently convert unknown into confirmed.

## Update rule

At review, retain the historical assumption and append the new status or revision reason. State what stayed stable, what changed, and what action follows. A plan should be simplified or narrowed when a high-fragility assumption fails; do not hide fragility by adding more topics.
