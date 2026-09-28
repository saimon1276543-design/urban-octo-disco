# Multi-Goal Prioritization Protocol

Use this reference when several learning goals must be planned together and the user has not clearly specified how to prioritize them.

## Separate four kinds of priority

Do not collapse these into one ranking:

| Dimension | Meaning | Evidence source |
|---|---|---|
| User priority | What the learner explicitly values most | Wording, ordering, deadlines, stated consequences, explicit preferences |
| Dependency priority | What must come earlier to unlock other goals | Dependency graph and operational prerequisites |
| Leverage priority | What supports many downstream outcomes | Reuse across goal families and shared artifacts |
| Urgency or opportunity | What is time-sensitive or has a stated window | Deadline, current ecosystem, access, application, or external event |

A goal can be low in user priority but high in dependency leverage. Surface that distinction rather than silently promoting it to the main goal.

## Priority states

Use qualitative states instead of invented numerical scores unless the user provides a scoring scheme:

- **Primary:** the route should optimize for this outcome first.
- **Co-primary:** two outcomes jointly define the main route.
- **Parallel:** can progress independently after its prerequisites.
- **Sequenced extension:** should follow evidence or infrastructure from another family.
- **Deferred:** retained but intentionally postponed under current constraints.
- **Optional exploration:** meaningful but not required for the stated outcome.
- **Unresolved priority:** materially affects the architecture and requires one focused question or an explicit provisional assumption.

## Decision rule when priority is missing

First infer only from strong signals: explicit deadlines, repeated emphasis, desired end products, exclusions, or stated consequences. If no strong signal exists, do not invent a winner. Present a provisional architecture with either:

1. two or three route strategies and the trade-off of each; or
2. one focused question whose answer would change the branch ordering or minimum viable path.

Do not ask for a complete intake form when only one decision is missing.

## Priority matrix

For broad requests, use this compact table when it changes the roadmap:

| Goal family | User priority | Dependency leverage | Urgency | Feasibility under constraints | Route state | Reason |
|---|---|---|---|---|---|---|
| {{Family}} | {{Primary / Co-primary / Unknown}} | {{High / Medium / Low}} | {{High / Medium / Low}} | {{High / Medium / Low}} | {{State}} | {{Evidence or assumption}} |

## Anti-distortion rules

Do not use dependency leverage as a substitute for learner motivation. Do not use urgency to erase foundational safety or proficiency evidence. Do not use feasibility to silently delete a goal; defer it and state what remains unavailable. Do not treat topic order in a wall of text as a reliable priority signal unless the user presents it as an intentional ranking.

## Reassessment trigger

When the learner’s evidence, deadline, constraints, motivation, or target context changes, revisit the priority matrix and route states. A revision should show which family changed state and why; it should not silently reorder the entire portfolio.
