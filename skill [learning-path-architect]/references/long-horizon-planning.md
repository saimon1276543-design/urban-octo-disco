# Long-Horizon Planning

Use this reference whenever the learner gives a duration such as days, weeks, months, years, “until I reach X,” or asks for an ongoing program. The unit is horizon-agnostic: do not assume that a year, month, or day has a fixed curriculum shape. Convert the supplied horizon into planning layers without pretending that future dates or technology details are known.

For detailed time-capacity modeling, cognitive load, observed-throughput calibration, recovery reserve, concurrency selection, and review decisions, also read `references/capacity-and-replanning.md`.

## 1. Define the north star

State one primary portfolio outcome in capability and evidence terms. Separate it from supporting outcomes, exploratory interests, and optional breadth. A north star may be a role, a durable capability, a portfolio of artifacts, a research direction, or a life/project outcome. If the user provides several outcomes, preserve them but classify them as primary, co-primary, parallel, sequenced, deferred, or unresolved.

Do not treat a technology list as a north star. Rewrite “learn Python, AWS, and React” as the capabilities those choices support, then retain the technologies as implementation choices, constraints, or alternatives.

## 2. Represent any horizon

Record the user’s horizon exactly as supplied and use relative phases rather than inventing calendar commitments:

| Layer | Purpose | Output |
|---|---|---|
| Portfolio horizon | Entire stated duration or open-ended program | North star, goal families, durable outcomes, deferred scope |
| Phase | A dependency- and evidence-defined segment | Phase outcome, active families, handoffs, exit evidence |
| Cycle | A bounded execution unit chosen by the learner or current capacity | One primary node, optional parallel node, practice loop, review trigger |
| Current frontier | What can start now | First action, support/setup, evidence to unlock the next node |

Use year/month/day labels only when the user supplies them or asks for calendar planning. Otherwise name phases by evidence, not dates. For an explicit duration, test whether the requested breadth and target levels are plausible under capacity; preserve the goals and surface trade-offs instead of silently shrinking them.

## 3. Model time capacity and concurrency

Capture capacity as layers and confidence, not false precision. Record nominal availability, reliable availability, usable learning capacity, variability, energy or attention constraints, fixed commitments, preferred session shape, maintenance load, recovery reserve, and whether the learner wants speed, depth, breadth, or sustainability. Use relative effort bands such as Small, Medium, Large, and Very large unless the user supplies a usable schedule. Read `references/capacity-and-replanning.md` for the deeper model.

Let the learner choose a concurrency preference: one active branch, one primary plus one maintenance branch, or several parallel branches. Treat parallelism as a constrained optimization choice, not as free speed. A branch may run in parallel only when its hard prerequisites are met, switching cost is acceptable, practice contexts do not conflict, and the learner’s capacity can sustain it. Show the expected trade-off: more parallel branches may shorten calendar completion for independent goals but usually increases switching overhead, slows depth, and raises review burden.

When progress data exists, use it as evidence for capacity calibration. Prefer observed completion, blocked-node frequency, retention checks, and actual effort over stated optimism. Never infer mastery from elapsed time alone.

## 4. Classify stability and revalidation

For every major node or technology, classify its planning stability:

- **Durable capability:** likely to remain useful across tools and versions, such as reasoning, algorithms, statistics, writing, systems thinking, debugging, experimentation, or domain principles.
- **Medium-term practice:** a method likely to persist but whose conventions evolve, such as software architecture, testing strategy, research methods, data modeling, or deployment practice.
- **Volatile implementation:** a framework, cloud service, library, platform version, API, certification objective, or vendor-specific workflow likely to change.

Build the long-range architecture around durable capabilities. Attach volatile implementations to the capability they serve, record the version/context used, and mark them for revalidation before the learner depends on them. Do not spend early effort mastering a volatile implementation when a durable prerequisite is still missing unless the implementation is the requested motivating project.

## 5. Replan periodically and after events

A long-horizon plan is a living dependency guide, not a promise. Recompute the portfolio when a phase exit criterion is met or missed, when the learner’s capacity changes materially, when goals or context change, when a branch is completed, abandoned, or deferred, when evidence reveals a prerequisite gap, or when a volatile tool or external requirement changes.

At each review, run the fixed collect → check evidence → calibrate → recompute → decide → explain → commit → expose sequence in `references/capacity-and-replanning.md`. Decide for every family: **continue, advance, remediate, maintain, narrow, defer, replace, retire, split, or pause**. Preserve stable IDs and completed evidence. Explain route-impacting changes, including what moved, why, and what becomes available or unavailable. Do not restart the learner merely because the future route changed.

## 6. Maintain completed capabilities

Mark completed branches as **maintain** when later goals depend on retained fluency. Use retrieval, transfer, small realistic tasks, or periodic reuse rather than repeating the full branch. If maintenance competes with a new branch, state the trade-off and let the user choose the acceptable decay risk.

## 7. Convert the architecture into action

Always expose the current active frontier separately from the long-range architecture. The learner should be able to answer: what can I do now, why is it unlocked, what evidence advances it, how many branches may I run in parallel, and when will the route be recomputed? The frontier is not a calendar schedule unless the user explicitly requests one.

## 8. Do not overstate forecasting

A multi-year plan may define dependencies, evidence, capacity assumptions, stability classes, and review triggers. It cannot guarantee that a learner will reach a level by a date, that motivation will remain constant, or that a volatile ecosystem will remain unchanged. State uncertainty where it changes the route and keep future research bounded to the next decision or revalidation trigger.
