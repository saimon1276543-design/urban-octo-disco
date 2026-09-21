# Portability migrations and compatibility

Use this reference when importing a portfolio between AI harnesses, schema versions, local workspaces, hosted projects, or offline packages.

## Compatibility check

Before import, compare package release identity, schema versions, required capabilities, stable-ID policy, link types, freshness context, and safety metadata. Classify the package as compatible, compatible with migration, read-only compatible, incomplete, or unsafe to import automatically.

## Migration contract

A migration record names the source and target schema versions, migration steps, affected paths or IDs, preserved fields, transformed fields, dropped fields, unresolved links, conflicts, validation result, and rollback or quarantine location. Never silently discard progress, evidence, conflicts, source claims, or revision history.

Migrate in this order: parse and validate the source manifest; preserve stable identifiers; transform schema fields; remap only adapter-specific paths and URIs; repair links by explicit mapping or flag them unresolved; validate graph and record integrity; preview conflicts; then commit only through a verified writable adapter. When no writable adapter exists, produce a migrated artifact and state that the source workspace was not changed.

## Conflict preview

Show conflicts before mutation when goals, route states, completed evidence, current revisions, safety boundaries, or freshness claims disagree. Safe metadata merges may be automatic only when both sides refer to the same stable ID and neither value is materially different. Route and goal conflicts remain unresolved until the learner or an authorized decision process chooses.

## Broken links and unsupported capabilities

For every broken link, identify the original reference, reason, possible replacement, confidence, and manual decision needed. If the target harness lacks a capability such as scheduling, persistence, browsing, or database writes, preserve the intent as a queued operation instead of claiming completion.

## Version policy

Prefer additive schema changes. For breaking changes, provide a migration script or explicit manual mapping. Keep an import revision and retain the original package fingerprint so the learner can return to the source representation.
