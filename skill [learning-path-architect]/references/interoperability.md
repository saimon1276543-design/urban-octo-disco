# Cross-Harness Interoperability

Keep the learning-path logic independent of the AI host. Different harnesses may expose the same workspace through different transports.

| Harness capability | Contract implementation | Persistence claim |
|---|---|---|
| MCP resources and tools | Resources for plan/progress reads; tools for verified writes and recomputation | Persistent only if the server documents and passes the persistence probe |
| Local filesystem | Markdown/JSON/SQLite files and relative links | Persistent only if the workspace survives the session |
| Git or project API | Revisions/commits for checkpoints; files or API records for plan state | Persistent when the repository/project is reachable and writes verify |
| Cloud/project connector | Hosted files, records, URLs, and APIs | Persistent only with verified access and storage behavior |
| REST/function-calling connector | Explicit read/write endpoints implementing the contract | Persistent according to the connector’s documented storage |
| Artifact-only host | Generated single document or multi-file package | Not persistent; ready for later import |
| Chat-only host | Inline staged response | Not persistent; no external state claim |
| Offline local host | Cached source ledger, local Markdown/JSON, queued revalidation | Current claims unavailable unless supported by a dated local archive |

Transport is not capability. An MCP connection may be read-only; a filesystem may be temporary; a hosted URL may require authentication; a database may lack safe transactions. Probe the required operations and report the actual result.

When moving a workspace between harnesses, import the manifest, schemas, stable IDs, progress, revision history, link manifest, and unresolved conflicts. The new harness should remap only adapter-specific paths or URIs and should not rewrite the learning graph without a revision record.

For update-aware portability, also import the source/claim ledger, update-run history, revalidation queue, research cutoff, source health, conflict records, and next scan triggers. A different AI harness may perform the same update protocol using web search, local archives, MCP, APIs, databases, Git, or artifact output; the protocol must not depend on a specific provider. An offline harness may continue stable planning and use cached evidence, but it must label volatile claims as dated or unverified and queue online revalidation.
