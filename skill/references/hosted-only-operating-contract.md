# Hosted-only operating contract

Use this reference when the learner asks for capstones, evaluation, progress tracking, persistence, reminders, local files, Freeplane updates, or future review.

## Capability boundary

In a normal hosted session, the skill can design a route, assign a task, inspect material supplied in the session, produce structured records, and create downloadable proposed updates. It cannot silently watch offline work, access an arbitrary local folder, maintain permanent background state, send future reminders, control a running Freeplane application, or prove mastery without supplied evidence.

State the boundary in user language. Say “I can create a downloadable review record now; automatic resurfacing later needs you to bring that record back or connect a verified local system.”

## Evidence boundary

Use one of these labels for every meaningful progress claim:

- `unknown`: no sufficient evidence.
- `self_reported`: the learner reported completion.
- `submitted`: an artifact or answer was supplied.
- `reviewed`: the supplied material was examined.
- `tool_checked`: a deterministic check confirmed a limited property.
- `transfer_tested`: the capability worked in a new situation.
- `retention_checked`: it worked after a time gap.

Never convert “planned,” “read,” or “self_reported” into mastery.

## Hosted submission workflow

When assigning work in a hosted environment:

1. State exactly what to submit in the next session: text, code, map, image, document, test output, or explanation.
2. Define the evidence requirement and the file or answer needed.
3. Tell the learner what the skill will inspect and what it cannot verify.
4. When the learner submits material, list what was actually received.
5. Mark missing, unreadable, unsupported, or unexamined items explicitly.
6. Save the result as a portable Markdown or JSON record when requested.

## Large submissions

Do not claim that every file was considered merely because a summary or retrieval step was used. Inventory the supplied material, divide it into bounded evidence units, inspect the units relevant to each rubric item, preserve source references, and report what was not examined.

## Current action

For a large plan, show the complete portfolio index separately from the current action. The current action must contain one task, expected time, required input, expected output, evidence to submit, and the next decision.

## Future integrations

Describe local databases, project-folder access, multi-agent evaluation, sandbox execution, time trackers, automatic roadmap insertion, and Freeplane plugins as future layers unless the current host explicitly verifies them. A downloadable file is not proof of permanent storage or live synchronization.
