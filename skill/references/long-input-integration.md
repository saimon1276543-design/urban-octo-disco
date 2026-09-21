# Long-Input and Multi-Topic Integration Protocol

Use this protocol when the user provides a very long wall of text containing many topics, goals, technologies, projects, domains, constraints, or possible future interests and wants them structured together.

## Core principle

Treat the input as a **portfolio of learning intentions**, not as one undifferentiated syllabus. Preserve every meaningful requested item, but do not force every item into one linear route or pretend that every item has the same priority, target level, or dependency structure.

## Pass 1: Ingest and segment

Read the full input before designing the route. Create a private inventory of explicit topics, capabilities, artifacts, technologies, constraints, exclusions, motivational context, and uncertainty. Segment the text by meaning rather than by paragraph length. Distinguish:

| Input signal | Handling |
|---|---|
| Explicit learning goal | Preserve and assign a traceable goal ID. |
| Named topic or technology | Preserve exact wording; classify its role and relation to an outcome. |
| Desired task or artifact | Treat as evidence or application, not merely as a topic. |
| Background knowledge or experience | Use for entry diagnostics and skip conditions. |
| Constraint or preference | Carry forward if it changes route, scope, tools, or practice context. |
| Example, comparison, or inspiration | Do not silently promote it to required scope. |
| Contradiction or ambiguity | Record it for resolution or state a conservative assumption. |

If the input is too large to present fully in one response, do not omit items silently. First honor the requested delivery mode: keep one authoritative giant syllabus when the user explicitly requests one document; otherwise, if a verified workspace exists, create an index plus linked phase/family parts; otherwise divide the response into numbered parts. Preserve global IDs, internal anchors or verified relative links, and the coverage ledger in every mode.

## Pass 2: Cluster into goal families

Cluster related items into **goal families** using shared outcomes, prerequisites, artifacts, or domain context. A family may contain several subgoals. Name each family by capability rather than by a shopping list of technologies. Keep unrelated families separate even when they appear in the same paragraph.

For each family, record its primary outcome, requested items, target proficiency, current-level uncertainty, likely domain module, evidence artifact, and dependencies on shared foundations or other families.

## Pass 3: Find shared foundations and reuse points

Build one shared-foundations branch for prerequisites genuinely reused by multiple families. Do not duplicate the same foundation under every branch. Mark branch-specific adaptations separately. Identify shared tools, mathematical ideas, workflows, or transferable practices, but do not label a foundation shared merely because it is generally useful.

## Pass 4: Resolve relationships

For each family pair, classify the relationship as **Required prerequisite**, **Recommended support**, **Parallel**, **Alternative**, **Reinforcement**, **Shared artifact**, **Potential conflict**, or **Unrelated**. Explain only relationships that affect route decisions. Detect cycles and resolve them through the smallest common foundation followed by iterative reinforcement.

## Pass 5: Prioritize without erasing breadth

Separate the integrated result into:

1. **Shortest credible route:** the smallest set that reaches the primary outcome or highest-priority family.
2. **Parallel routes:** families that can progress independently after shared foundations.
3. **Sequenced extensions:** families that depend on earlier evidence or tools.
4. **Deferred or optional interests:** meaningful items retained but not required for the primary route.

If the user gives no priority, do not invent one silently. State the prioritization assumption, offer a small number of plausible route strategies, or ask one focused question only when the choice changes the entire architecture.

## Pass 6: Detect conflicts and infeasibility

Check for incompatible tools, mutually exclusive routes, contradictory constraints, duplicated outcomes, excessive breadth for the stated horizon, and proficiency targets that cannot all be reached under the supplied constraints. Preserve the goals, surface the trade-off, and identify the minimum viable route. Never solve infeasibility by silently deleting named goals.

## Pass 7: Build the integrated roadmap

Use global stable numbering and goal-family labels. Start with the shared foundation only when it unlocks multiple families; otherwise begin with the highest-priority family. Show parallel branches explicitly. Give each major family its own outcome, target level, evidence, and exit criterion. Use cross-references rather than repeating content.

For a very large request, provide a compact **portfolio architecture** before the detailed map:

| Family | Primary outcome | Target level | Shared prerequisites | Route status | Evidence artifact |
|---|---|---|---|---|---|
| {{Family}} | {{Capability}} | {{Level}} | {{Node IDs}} | {{Primary / Parallel / Deferred / Optional}} | {{Artifact or performance}} |

Then provide the detailed map in parts, preserving global IDs and the coverage ledger.

For a supplied duration or ongoing program, build two layers: a stable portfolio architecture covering the full horizon and a rolling execution layer containing the current phase, current cycle, and active frontier. Read `references/long-horizon-planning.md` for capacity, concurrency, stability classes, maintenance, and review rules. Do not turn the horizon into an invented calendar syllabus unless the user explicitly requests calendar scheduling.

## Pass 8: Coverage and delivery checks

Before delivery, verify that every meaningful explicit item has a status: mapped to a node, merged as a duplicate, classified as an alternative, retained as optional/deferred, identified as a conflict, or excluded as context/noise with a reason. Confirm that no family is lost because the response was too long. State which items are intentionally deferred and what capability remains unavailable until they are completed.

If progress data is supplied or a workspace package is requested, validate its schema and freshness, distinguish recorded evidence from self-report, and recompute the active frontier from completed, blocked, available, maintained, deferred, and retired states. Never let a stale or unverifiable progress record silently change the route.

Do not create a single giant linear syllabus merely because the input is long. Length of input increases the need for clustering, stable identifiers, portfolio-level prioritization, and staged delivery; it does not justify more granular trivia.
