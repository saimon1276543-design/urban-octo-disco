# Portable Workspace Contract

Use this reference when a plan must persist, synchronize, or move between Manus and another AI harness. The contract separates planning behavior from storage technology. A filesystem, MCP server, database, Git repository, project API, or cloud connector may implement it.

## Workspace identity

A workspace should expose a stable `workspace_id`, `plan_id`, `schema_version`, `adapter_id`, `adapter_type`, `lifecycle_state`, and `last_verified` value. The authoritative plan/index must identify its current revision and the progress record it uses.

Supported lifecycle states are **draft**, **active**, **paused**, **under review**, **superseded**, **archived**, and **retired**. Revisions preserve stable node IDs and completed evidence unless a revision record explicitly explains a migration.

## Capability contract

Adapters advertise capabilities rather than making the skill guess:

| Capability | Meaning |
|---|---|
| `read_plan` | Read the authoritative index and relevant detail. |
| `write_plan` | Create or update plan content. |
| `read_progress` | Read progress, evidence, blockers, and reviews. |
| `update_progress` | Persist progress changes. |
| `list_nodes` | Enumerate nodes and statuses. |
| `recompute_frontier` | Calculate currently unlocked actions. |
| `verify_links` | Check links and artifact targets. |
| `record_review` | Persist capacity and replanning decisions. |
| `read_source_ledger` | Read current source, claim, version, context, and freshness records. |
| `update_source_ledger` | Add or revise verified source and claim metadata. |
| `run_drift_scan` | Compare expiry, version, source, and context signals and return flagged scopes. |
| `queue_revalidation` | Add affected sources or nodes to a prioritized revalidation queue. |
| `record_update_run` | Persist update scope, cutoff, changes, unchanged areas, status, and next trigger. |
| `recompute_impact` | Traverse affected dependencies, bridges, evidence, and active-frontier implications. |
| `create_revision_diff` | Produce a stable-ID diff for accepted, rejected, conflicting, and unresolved changes. |
| `versioning` | Read revision IDs and history. |
| `checkpoint` | Create a recoverable pre-change checkpoint. |
| `transactions` | Apply a multi-record change atomically. |
| `conflict_detection` | Detect stale or concurrently modified content. |
| `subscriptions` | Notify the host when resources change. |

The skill may use only capabilities that were discovered and verified in the current environment. Missing capabilities must be recorded as unavailable; they must not be simulated by claiming that a change was saved.

## Mutation protocol

For a persistent update:

1. Read the current manifest, plan revision, and relevant progress records.
2. Confirm write scope and freshness.
3. Create a checkpoint or versioned draft when supported.
4. Compute a stable-ID revision diff.
5. Detect stale revisions or concurrent modifications.
6. Apply an idempotent transaction, or write and verify a new version before changing the authoritative pointer.
7. Verify files, records, links, and schema versions.
8. Record the review, revision, adapter, and verification result.

If verification fails, preserve the previous authoritative version and report the failed operation. Never silently leave a multi-file plan half updated.

## Conflict policy

Never overwrite learner edits silently. If a version conflict is detected, attempt a field-level merge only for non-conflicting metadata. Preserve conflicting values, identify affected stable IDs, and produce a conflict record. Ask the learner for a choice only when the conflict changes goals, evidence, dependencies, permissions, or the authoritative route.

## Portability mapping

- **MCP:** resources expose plan/progress data; tools perform verified mutations; server capabilities and permissions must be discovered.
- **Filesystem:** files and relative links implement plan reads/writes; versioned copies can implement checkpoints.
- **Database:** tables or documents implement nodes, progress, revisions, and reviews; transactions should be used when available.
- **Git/project API:** commits or revisions implement checkpoints and history; branches or pull requests may represent proposed plan updates.
- **Cloud/project workspace:** hosted files and APIs implement resources and mutations; URLs must be verified and access-scoped.
- **Artifact-only host:** generated package is portable but not persistent; include schemas and manifest for later import.
- **Offline host:** use cached or bundled source records with explicit as-of dates, mark volatile claims unverified or stale, and queue revalidation; never claim current web verification.
- **Other AI harness:** map host features to the conceptual operations, preserve stable IDs and schemas, and keep provider-specific URIs or credentials in adapter metadata only.

Do not require a particular transport. Require the contract, capability verification, stable IDs, and honest persistence claims.
