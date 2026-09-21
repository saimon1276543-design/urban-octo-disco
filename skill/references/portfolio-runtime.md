# Learning Portfolio Runtime

Use this reference when the portfolio must behave as one coherent, measurable, updateable system rather than a collection of disconnected plans and ledgers.

## Canonical model

Maintain one authoritative portfolio record with stable IDs for goals, domains, capabilities, dependencies, evidence, observations, capacity parameters, experiments, scenarios, source claims, freshness states, decisions, revisions, policies, safety profiles, and derived views. Markdown documents, JSON records, database rows, and hosted files are representations of this model; they must carry the same portfolio ID, revision, and stable IDs.

A runtime record should expose the minimum fields needed for safe operation: schema version, portfolio ID, revision, north star, entities, relationships, evidence, observations, capacity profile, active scenarios, freshness state, policy, safety boundaries, and last-derived metrics. Keep provider-specific locations in adapter metadata, never in the learning graph.

## Derived metrics

Compute metrics from records and report the basis and freshness of each result. Useful signals include capacity utilization, maintenance load, dependency bottleneck centrality, switching-cost exposure, evidence coverage, route leverage, freshness debt, complexity debt, sustainability risk, uncertainty concentration, and active-frontier readiness. Metrics are diagnostic signals, not grades or predictions of learner worth.

Use explicit denominators and return unknown when the record is insufficient. Do not convert unknown time, missing evidence, or unresolved safety into false precision. Show the affected stable IDs and the smallest corrective action for every material warning.

## Uncertainty propagation

Propagate uncertainty along dependency and impact edges. A fragile prerequisite makes dependent estimates less reliable; weak evidence blocks or lowers confidence in downstream unlocks; stale tools create freshness risk for dependent artifacts; unknown capacity widens calendar ranges; and unresolved safety or authorization gates restrict consequential application branches. Propagation must preserve the reason and source of uncertainty so the learner can reduce it with a diagnostic, observation, research update, or authorization check.

## Consistency repair

Run a read-only integrity scan before committing a revision. Detect duplicate IDs, dangling links, goals without closure evidence, capabilities with impossible states, missing maintenance, stale current actions, unsupported parallel edges, conflicting revisions, and scenario/view drift. Emit repair proposals with issue ID, affected IDs, proposed change, consequence, reversibility, confidence, and approval requirement. Apply only safe mechanical repairs through a verified writable adapter; keep route, goal, safety, and evidence conflicts for explicit resolution.

## Runtime cycle

Ingest or observe; validate; derive metrics; propagate uncertainty and decay; scan for defects; propose repairs; expose portfolio/phase/today views; execute or record one bounded action; record evidence and observations; recompute only affected slices; checkpoint a revision; and schedule the next review or revalidation trigger. The runtime never claims background execution unless the host exposes and confirms it.
