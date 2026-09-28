# Safe Mutation and Conflict Handling

Use this reference whenever the skill changes a persistent roadmap, progress record, linked workspace, or database-backed plan.

## Before mutation

Read the current workspace manifest and authoritative revision. Check schema compatibility, write permission, freshness, and whether another version has changed since the last read. Identify the exact stable IDs and files/records affected. Do not perform broad destructive rewrites when a targeted update is sufficient.

## Apply changes safely

Prefer this order:

1. Transaction with rollback support.
2. Versioned draft plus verification, then authoritative pointer update.
3. Checkpointed file/database update with post-write verification.
4. Best-effort update only when the user accepts the limitation and the affected scope is small.

Make updates idempotent: rerunning the same approved operation should not duplicate nodes, links, progress events, or review records. Preserve unknown fields when the schema permits them, and migrate schema versions explicitly rather than silently dropping data.

## Verify after mutation

Check that:

- Stable IDs remain unique and unchanged unless migration is recorded.
- All expected files/records exist.
- Relative links and anchors resolve.
- Progress references point to known nodes.
- Revision and audit metadata were recorded.
- The active frontier reflects the new evidence and dependencies.
- The authoritative index points to the verified version.

If any check fails, keep the last known-good version authoritative and report the failed operation. Do not claim completion.

## Concurrent edits

Use revision IDs, modification timestamps, ETags, Git commits, database versions, or equivalent conflict signals when available. If the source changed after it was read, do not overwrite it blindly. Merge only disjoint fields with clear ownership. For conflicts involving goals, route priority, evidence, dependencies, permissions, or learner-authored content, preserve both values and create a conflict record.

A conflict record should contain the workspace/plan ID, affected stable IDs, base revision, competing revisions, automatically merged fields, unresolved fields, risk, and required decision. Ask the learner only for the unresolved decision; do not ask them to manually reconstruct the entire workspace.

## Recovery

When a mutation partially fails, stop further writes, preserve the checkpoint, report the affected operations, and restore or point back to the last verified version when the adapter supports it. If rollback is unavailable, create a recovery manifest identifying the authoritative files/records and the incomplete changes. A future adapter can reconcile this manifest without rebuilding the plan.

Explain recovery in learner language. Support requests such as “show what changed,” “undo the last update,” “restore the previous roadmap,” and “export everything.” If the current host cannot perform one of these actions, say which one is unavailable and preserve the last known-good export instead of implying that recovery happened.
