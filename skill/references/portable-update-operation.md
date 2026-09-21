# Portable Update Operation

Keep the learning-path logic independent of Manus or any specific AI harness. A host only needs to map its available operations to the portable contract; it must not be assumed to provide browsing, persistence, scheduling, MCP, databases, or background execution.

## Environment profiles

| Environment | Best available behavior | Freshness limitation |
|---|---|---|
| Online AI host with web access | Research current sources, update ledger, produce revision diff | Requires explicit source verification; no persistence unless exposed |
| Online host with verified workspace/MCP/API | Read/write plans, ledgers, progress, checkpoints, and update runs | Use only discovered capabilities and permissions |
| Offline local filesystem | Use bundled references, cached source ledger, local files, and queued revalidation | Cannot claim current web facts; mark claims offline/unverified |
| Offline host with local source archive | Search and cite the archive with archive date/context | Freshness is bounded by archive date; queue external recheck |
| Hosted artifact-only environment | Generate portable Markdown/JSON package with manifest and update report | Not persistent unless the host confirms storage and retrieval |
| Chat-only harness | Return staged text or downloadable package if supported | No saved state or monitoring claim |

## Portability rules

Use plain Markdown, JSON, relative links, stable IDs, ISO dates, explicit schemas, and host-neutral operation names. Keep provider-specific URIs, credentials, tool names, and paths in adapter metadata rather than in the learning graph. On import, remap only adapter-specific references; preserve stable IDs, source IDs, revision history, progress, conflicts, freshness states, and queued revalidation.

## Offline behavior

If offline, do not fabricate current claims. Use the last verified ledger and label each affected claim current-as-of, aging, stale, inaccessible, or offline-unverified. Continue with stable conceptual architecture and queue the volatile or safety-sensitive claims for online revalidation. For high-consequence domains, do not turn cached information into current authorization or practice guidance.

## Online behavior

If online, research only the scope required by the update mode, prefer authoritative sources, record the cutoff and context, and preserve unchanged areas. A web browser or search tool is not itself a persistent workspace. A remote URL or MCP endpoint is not itself a verified update channel.

## Capability mapping

Map host features to conceptual operations such as read plan, write plan, read source ledger, run drift scan, queue revalidation, record update run, recompute impact, create revision diff, checkpoint, verify links, and subscribe to changes. If an operation is unavailable, use the strongest fallback and record the missing capability. Never let portability reduce honesty about what was actually read, changed, saved, or scheduled.
