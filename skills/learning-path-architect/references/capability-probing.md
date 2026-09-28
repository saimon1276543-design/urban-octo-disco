# Capability Probing

Use this reference before the first persistent read or write. The probe is a short capability check, not a request to expose secrets.

## Probe record

Record one result per candidate adapter:

| Field | Meaning |
|---|---|
| Adapter | Stable name/type, not a guessed label |
| Reachable | Whether the host can contact it |
| Authenticated | Whether credentials/session are valid |
| Read | Plan/progress read scope |
| Write | Plan/progress mutation scope |
| Persistent | Survives this session |
| Links | Relative, hosted, embedded, or none |
| Versioning | Revisions/checkpoints available |
| Transactions | Atomic multi-file/record changes available |
| Conflicts | Stale-write detection available |
| Missing operations | Exact unavailable capabilities |
| Verified at | Timestamp or session marker |

## Probe order

Run the workspace adapter hierarchy from `references/workspace-adapters.md`. Stop at the highest adapter that is reachable, authenticated, authorized for the required operation, and persistent enough for the user’s request. A read-only adapter may be useful for analysis but cannot be selected for a requested write workflow.

For MCP, discover resources and tools before calling them. Confirm resource URIs, tool schemas, authentication state, read/write scope, persistence behavior, and whether the server is local or remote. A plain URL, a connector name, or a successful health page is not proof that the required plan operations work.

For a filesystem, verify the intended workspace root, ability to create/update files, relative-link behavior, and whether the location persists across sessions. Do not assume a desktop folder exists or is visible.

For databases and project connectors, verify the schema or API endpoints, permissions, stable identifiers, transaction behavior, and update semantics. Do not inspect unrelated personal data.

## Selection result

Return a compact selection record:

- Selected adapter and why it outranked lower options.
- Required operations available.
- Required operations unavailable.
- Persistence and link assumptions.
- Mutation safety level: transactional, versioned, best-effort, or artifact-only.
- Fallback mode if a required operation fails.

If no adapter passes, descend once to the strongest artifact mode and state the limitation. Do not repeatedly ask the learner to transfer files manually.
