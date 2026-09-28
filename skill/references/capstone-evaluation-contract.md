# Capstone evaluation contracts

Phase 0 defines the records that later phases will use. It does not yet run an LLM swarm, execute project code, or modify Freeplane automatically.

## Roles

- `learning-path-architect` creates the assignment, rubric, evidence checklist, and review policy.
- The local bridge reads only explicitly authorized project roots.
- The evaluator examines submitted evidence and returns structured findings.
- The database keeps history, mistakes, reviews, and revisions.
- Freeplane shows concise summaries and links to the detailed records.

## Evidence rule

The system must not say that a capability was mastered merely because an assignment was created or a file exists. Every evaluation must state what was actually supplied, what was checked, and what remains unknown.

Use the evidence states from `evaluation-result.schema.json`:

- `unknown`: no sufficient evidence was supplied.
- `self_reported`: the learner reported completion.
- `submitted`: an artifact or answer was supplied.
- `tool_checked`: an allowlisted deterministic check confirmed a property.
- `llm_reviewed`: an LLM reviewed supplied evidence.
- `transfer_tested`: the capability worked in a new situation.
- `retention_checked`: the capability was checked after time had passed.

## Context-window rule

A large project is never placed blindly into one LLM request. The bridge first inventories files, creates bounded evidence references, runs deterministic checks, and sends only the relevant work unit to each evaluator. Specialist results are combined with structured references and disagreements are preserved.

The original files remain the source material. Extracted summaries are convenience records and must include their source file hashes.

## Permission rule

“Full access to the project” means access to the project folder that the learner explicitly authorizes. It does not mean unrestricted access to the entire computer.

The default policy should:

- Read only authorized roots.
- Keep secrets out of project submissions.
- Disable network access during code checks.
- Run only allowlisted commands.
- Use copies or read-only checkouts.
- Create a draft evaluation before changing official records.
- Require confirmation before updating Freeplane or running project code.
- Preserve a revision before every official write.

## Review and roadmap rule

A recurring mistake becomes a compact review record, not a duplicate copy of the original capstone. When due, the system can insert a linked review item into the progress view or review queue. It must preserve the original capability node, stable ID, evidence history, and link to the originating evaluation.

If available time is known, use it to choose a full review, a smaller corrective task, or a later slot. If available time is unknown, use a labeled default estimate or ask for a manual value. Never silently discard a due review because the current session is short.

## Freeplane rule

The authoritative dependency map and the visual progress view are separate concepts. A capability may visually move from planned to active to transfer-tested without breaking its original prerequisite relationships. Early implementations should propose map changes and allow approval; later UI work may make the approval flow more elegant.

## Contract files

- `templates/capstone.schema.json`
- `templates/submission-manifest.schema.json`
- `templates/evaluation-result.schema.json`
- `templates/mistake-memory.schema.json`
- `templates/review-event.schema.json`
- `templates/permission-policy.schema.json`
