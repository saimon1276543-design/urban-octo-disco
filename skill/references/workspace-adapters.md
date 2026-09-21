# Workspace Adapter Hierarchy

Use this reference whenever the plan must be created, updated, linked, persisted, synchronized, or driven by progress across sessions. The objective is to avoid repetitive manual file handling. Select the highest verified adapter available in this order:

For the detailed portable contract, capability probe, and safe mutation protocol, read `references/workspace-contract.md`, `references/capability-probing.md`, and `references/safe-mutation.md` before persistent mutation.

1. **Existing verified learning workspace** — use an already connected workspace that exposes the plan, progress, and link operations.
2. **Connected MCP server** — use an authenticated MCP server exposing files, database/progress resources, and write/update tools.
3. **Existing project or database connector** — use a verified project API, database connector, Git integration, cloud drive connector, or equivalent.
4. **Local or attached filesystem** — create and update files in an explicitly accessible workspace, using relative links.
5. **Hosted file or project workspace** — use an existing verified hosted project, artifact store, or persistent workspace.
6. **Automatically generated downloadable multi-file package** — generate the complete package as an artifact when no persistent adapter exists but the host can create and return files. Treat this as a delivery artifact, not as a recurring manual upload/download workflow.
7. **Single document** — create one navigable authoritative document when multi-file output is not useful or the user requests it.
8. **Inline staged response** — use only when the host cannot create or return files.

## Adapter selection rules

- Detect capabilities; never infer them from the model or skill name.
- Prefer an existing adapter over creating a new storage system.
- Prefer a persistent adapter over a transient artifact.
- Prefer machine-readable progress and verified update operations over repeatedly asking the learner to re-upload files.
- If the user explicitly requests a lower mode, honor that request even when a higher mode exists.
- If the highest available mode cannot perform a required operation, descend to the next mode and record exactly what is unavailable.
- Do not present manual upload/download as the normal operating procedure. Do not repeatedly ask the user to copy files between systems when an adapter is unavailable; instead, state the limitation and use the strongest automated fallback available.
- Do not create or recommend a new MCP server, database, connector, or public endpoint without the required execution capability, credentials, permissions, or user approval. Explain what connector would be needed, but do not pretend it exists.
- Treat lifecycle state explicitly: draft, active, paused, under review, superseded, archived, or retired. Preserve stable IDs and completed evidence across lifecycle changes.
- Prefer idempotent, checkpointed, versioned mutations. If the adapter cannot provide transactions or rollback, use a verified versioned draft where possible and report the weaker safety level.
- Keep update logic host-neutral. In an online environment, verify current sources and record the research cutoff. In an offline environment, use cached or bundled records only as explicitly dated evidence, queue volatile claims for later revalidation, and never claim current web verification.
- When moving between AI harnesses, import the manifest, source/claim ledger, revalidation queue, update history, schemas, stable IDs, progress, revisions, links, and conflicts. Remap only adapter-specific paths or URIs.

## Capability contract

Treat adapters as implementations of these conceptual operations:

| Operation | Purpose |
|---|---|
| `read_plan` | Read the authoritative index and relevant detail files. |
| `write_plan` | Create or update plan files while preserving stable IDs. |
| `read_progress` | Read progress state, evidence, blockers, and review history. |
| `update_progress` | Record verified learner evidence and status changes. |
| `list_nodes` | Enumerate nodes, dependencies, and current states. |
| `recompute_frontier` | Determine what is unlocked and actionable now. |
| `verify_links` | Check relative paths, anchors, hosted URLs, and artifact references. |
| `record_review` | Store capacity observations, replanning decisions, and route changes. |
| `read_source_ledger` | Read source, claim, version, context, and freshness metadata. |
| `update_source_ledger` | Persist verified source and claim changes. |
| `run_drift_scan` | Identify expired, changed, conflicting, or context-limited scopes. |
| `queue_revalidation` | Prioritize scopes that require future research. |
| `record_update_run` | Store update cutoff, scope, changes, unchanged areas, and status. |
| `recompute_impact` | Traverse affected dependencies, bridges, evidence, and frontier. |
| `create_revision_diff` | Produce a stable-ID update diff before mutation. |

An adapter may expose these through MCP tools/resources, filesystem operations, project APIs, SQL, or another verified mechanism. Map the available operations before relying on them. If an operation is absent, do not simulate persistence by claiming that an in-memory change was saved.

Use `templates/workspace-manifest.schema.json` to record adapter identity, capabilities, persistence, lifecycle, and current revision. Use `templates/conflict-record.schema.json` when concurrent edits cannot be safely merged.

## MCP-specific guidance

For an MCP connection, discover the server’s available resources and tools before using it. Confirm authentication, read/write scope, resource URIs, persistence behavior, and whether the server is local or remote. A URL is not sufficient by itself: it must point to a compatible, reachable, authenticated MCP endpoint. Use resource reads for plan/progress data and tools for mutations when the host exposes both.

## Failure and handoff behavior

If no persistent adapter is available, finish the requested work using the strongest available artifact mode and state the limitation once. Do not turn the learner into the synchronization mechanism. Preserve stable IDs, include a progress schema and link manifest when relevant, and make the package ready for an automated adapter later.
