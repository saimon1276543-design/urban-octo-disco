# Hosted LLM Reliability Matrix

Use this reference before promising that a hosted LLM environment will remember, schedule, synchronize, or continuously operate a learning workspace.

## Reliability levels

| Level | What is verified | What the skill may promise |
|---|---|---|
| 0 — Conversation only | The model can answer, but no durable file or tool is verified | “I can help now; nothing is assumed saved.” |
| 1 — Session files | Files can be created and read during the current task | “I created files for this session.” |
| 2 — Exportable workspace | Files can be packaged and downloaded | “You can download and keep this workspace.” |
| 3 — Persistent workspace | The same workspace can be reopened after a later session | “The workspace is saved here.” |
| 4 — Verified automation | A scheduler runs a task and stores its result reliably | “Discoverer runs on this schedule.” |
| 5 — Verified integration | An authenticated adapter or MCP endpoint has tested read/write operations | “The LLM can read and update this connected workspace.” |

Do not infer a higher level from a lower level. A chat that can create a ZIP is not automatically a persistent database. A URL is not automatically an authenticated MCP server. A scheduled instruction is not proof that a background job ran.

## What can be reliable in hosted environments

Hosted environments are usually reliable for the current conversation, generating documents, transforming supplied files, running bounded validation, and creating a downloadable export. They can be reliable for persistence or scheduling only when the host explicitly exposes those features and a read-back test confirms them.

They are not safe to treat as a personal always-on computer by default. Sessions can expire, file locations can change, quotas can apply, scheduled runs can be unavailable, and the model may not see prior files unless they are attached or stored in a verified workspace.

## Safe operating rule

At the start of each substantial operation, report the current reliability level in plain language. Before a destructive update, create a versioned export or checkpoint. After an update, read the changed files back and verify them. If verification fails, keep the old version and report that the update was not confirmed.

## Discoverer implication

Weekly, six-month, and yearly review schedules are design targets until a real scheduler and persistent result store are verified. Without them, maintain a due-review queue and run Discoverer when the learner requests it or when a supported host event triggers it.

## Migration implication

Design every hosted result to be portable: stable IDs, relative links, dates, source records, schemas, revision records, and a complete export. This makes hosted work useful even when the host itself is temporary.

## User-facing status

Prefer one of these short statements:

- “This is prepared in the current session; download it if you want to keep it.”
- “The workspace was exported and is ready to move to another environment.”
- “The host confirmed that this workspace can be reopened later.”
- “Automatic Discoverer scheduling is not verified here, so I recorded the next review instead of claiming it ran.”
