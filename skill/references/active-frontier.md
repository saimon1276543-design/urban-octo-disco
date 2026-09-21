# Active Frontier and Branch Handoff Protocol

Use this protocol for large integrated roadmaps with several goal families. Its purpose is to convert a portfolio architecture into an executable next step without forcing every branch into a single linear sequence.

For detailed capacity and review decisions, read `references/capacity-and-replanning.md`; this protocol identifies the frontier, while that reference calibrates whether the learner can sustainably carry it.

## Active frontier

After constructing the dependency graph, identify the **active frontier**: the smallest set of currently unlocked nodes that the learner can begin or continue based on demonstrated prerequisites, constraints, and route state.

For each frontier node, record:

| Node | Family | Why unlocked | Required support or setup | Evidence needed to advance | Next handoff |
|---|---|---|---|---|---|
| {{Node ID}} | {{Family}} | {{Prerequisite evidence}} | {{Tool, reference, supervision, or setup}} | {{Exit criterion}} | {{Downstream node or branch}} |

The frontier is not a schedule and does not imply that the learner should work on every unlocked node simultaneously. Select one primary active node and, only when useful, one parallel maintenance or exploration node.

## Branch handoff rules

A family may hand off to another family when it produces one of the following:

- a prerequisite artifact, such as a working program, dataset, schema, or environment;
- a demonstrated transferable capability;
- an operational setup that removes a bottleneck;
- evidence that a branch is ready for bounded unfamiliar work; or
- a decision that selects one alternative route.

Name the handoff explicitly. Do not treat exposure to a topic as handoff evidence.

## Switching and concurrency

Keep concurrency limited by the learner’s stated constraints and cognitive context. If no preference is supplied, favor one primary branch plus at most one genuinely parallel branch whose switching cost is low and whose practice reinforces the primary route. Do not invent a weekly timetable. State only the switching rule, such as “continue the primary branch until its exit criterion is met, then activate the dependent family.”

## Frontier updates

Recompute the frontier when:

- a milestone is passed or fails;
- a prerequisite is skipped after diagnostic evidence;
- a tool, deadline, or target context changes;
- a branch is deferred, completed, or abandoned; or
- new research changes a dependency, tool choice, or safety boundary.
- observed throughput, interruption, cognitive load, maintenance burden, or recovery reserve changes materially;
- a periodic review trigger is reached, such as two completed cycles, a phase exit, or repeated exposure of the same blocker.

When a milestone fails, remove only the blocked downstream nodes from the active frontier and expose the smallest prerequisite to remediate. When a branch is deferred, do not let its descendants appear actionable.

At a review, do not only recompute available nodes. Reclassify each active family as advance, remediate, maintain, narrow, defer, replace, retire, split, or pause. Record the reason and route impact, then expose one primary action and at most the learner’s feasible parallel maintenance/exploration branches.

## Delivery rule

For very large requests, place the active frontier immediately after the portfolio architecture and starting point. The learner should be able to answer: **What can I begin now, why can I begin it, what evidence unlocks the next handoff, and which branches are intentionally not active yet?**
