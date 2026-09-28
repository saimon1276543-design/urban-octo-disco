# Delivery and Linking

Use this reference when the user asks for one giant syllabus, a multi-file roadmap, linked parts, an offline workspace, a hosted workspace, a database-backed plan, or continuation across sessions.

For hands-off persistence or synchronization, read `references/workspace-adapters.md` first. This file describes package structure; the adapter reference decides how the files are maintained without repeatedly involving the learner.
For persistent mutation, use the workspace manifest and conflict record schemas, and follow `references/safe-mutation.md`; do not perform a broad overwrite without a revision/checkpoint strategy.

## 1. Ask or infer the delivery mode

Support these explicit modes:

- **Single document:** one authoritative syllabus or roadmap in the requested format. Use stable global IDs and internal anchors so the document remains navigable.
- **Linked parts:** a concise index/overview plus separate branch, phase, or family files linked from the index. Keep the index authoritative for route status, IDs, and current frontier; keep detail in child files.
- **Workspace package:** an index, linked Markdown files, structured progress data, and optional diagrams/templates. Use when the user wants ongoing updates or a very large plan.

If the user does not choose, infer single document for a small request and linked parts for a very large request only when a verified adapter can maintain them or the host can automatically return a complete package. State the choice and do not make repeated manual upload/download the default.

## 2. Detect the execution environment conservatively

First inspect the available workspace and tools, following the adapter priority in `references/workspace-adapters.md`. Distinguish:

- **Local or attached filesystem:** create files only in an explicit or user-approved workspace; use relative links within that workspace and avoid assuming a desktop path.
- **Hosted or cloud filesystem:** create files in the available project/workspace and use relative links for durable navigation. If the platform provides a public or hosted artifact URL, use it only when actually available and record the URL plus access limitations.
- **No durable filesystem or linkable workspace:** return a single document or inline staged parts; do not invent URLs or claim persistence.

Never expose private absolute paths as if they were public links. A `file://` or local absolute path is useful only to the user who can access the same machine. Prefer relative links inside a delivered package. Use hosted/embedded links only when the host, URL, permissions, and persistence are verified. If no automated adapter exists, state that once and return the strongest automatically generated artifact; do not turn the user into a recurring file-transfer bridge.

## 3. Create a navigable package

For linked delivery, create:

1. `index.md` — north star, route modes, assumptions, current frontier, capacity, phase/family table, and links to all parts.
2. One file per phase, family, or branch — detailed objectives, prerequisites, evidence, and local references.
3. `progress.md` or structured progress data — completed evidence, current status, blockers, capacity observations, and review history.
4. Optional `graph.mmd` or `graph.md` — only when cross-branch dependencies benefit from a visual graph.
5. A link manifest — target paths, link type, last verification, and whether the target is local, hosted, or unavailable.
6. A workspace manifest — adapter identity, capability probe, lifecycle state, schema version, and authoritative revision.
7. A revision or conflict record when an update was based on a stale or concurrently modified workspace.

Keep stable IDs in every file. Link back to the index and sibling dependencies with relative links. If a target cannot be created or verified, record it as unresolved instead of emitting a broken link.

When updating an existing package, read its manifest and revision first, create a checkpoint or versioned draft where possible, verify every affected file/link, and leave the last known-good version authoritative if verification fails.

## 4. Single-document mode still supports navigation

For a giant syllabus, use a table of contents, stable anchors, phase/family headings, a current-frontier section, and a coverage ledger. Do not split the authoritative map merely because the content is long when the user explicitly requested one file.

## 5. Database and progress integration

Do not create a database merely because one is technically possible. Use structured JSON, CSV, SQLite, or an existing project database only when the user requests persistent tracking or the workspace already provides it. Before reading progress data, identify its schema, freshness, source, and permissions. Treat progress records as evidence with uncertainty, not as unquestionable truth.

At minimum, progress should be able to represent stable node ID, status, evidence link, last attempt, confidence, blocker, observed effort, review state, and next action. If a database is unavailable, use a plain progress file with the same conceptual fields.

## 6. Verify links before delivery

Check every generated relative link, anchor, local file, hosted URL, and embedded artifact that the environment permits you to inspect. Include a short link manifest or verification note. Never claim that a link is live, public, persistent, or accessible unless it was verified.
