# Chrome DevTools and Browser Network Debugging

Use this reference for Chrome DevTools, Chrome DevTools Protocol (CDP), browser automation diagnostics, request/response interception, and enterprise crawling observability. Treat panel names and protocol domains as durable conceptual interfaces; current browser versions, protocol fields, tool APIs, and feature support remain volatile overlays requiring current verification.

## DevTools interface

### Console

Use the Console for JavaScript evaluation, runtime errors, warnings, object inspection, stack traces, source locations, and controlled reproduction. Preserve the distinction between a page's runtime context and the automation or DevTools client context. Do not paste secrets or execute untrusted commands in privileged contexts.

### Network panel

Read the request waterfall and dependency graph. Inspect URL, method, status, protocol, initiator, timing phases, headers, cookies, query parameters, request payload, response body, response headers, redirects, cache state, priority, size, compression, and connection details. Use filters and preserved logs to isolate a reproducible request sequence.

### Sources panel

Use Sources for source maps, breakpoints, conditional breakpoints, call stacks, scopes, watch expressions, async stack traces, overrides, snippets, workers, and loaded resources. Treat source maps as debugging aids rather than proof that deployed source exactly matches a repository.

### Application panel

Inspect origins, storage, cookies, local/session storage, IndexedDB, Cache Storage, service workers, manifests, background services, and storage quotas. Record cookie attributes such as domain, path, expiration, Secure, HttpOnly, and SameSite without exposing values. Use isolated profiles and approved test accounts.

### Performance panel

Use traces to reason about navigation, scripting, rendering, painting, layout, long tasks, network-to-render relationships, workers, frames, and responsiveness. Correlate trace evidence with network and runtime evidence; avoid attributing causality from a single timeline marker.

### Memory panel

Use heap snapshots, allocation instrumentation, allocation timelines, detached DOM inspection, and comparison snapshots to investigate leaks and retention. Control workload, warm-up, sampling, browser version, and test repeatability before comparing results.

### Security panel

Inspect certificate/connection information, origin security, mixed content, certificate errors, and security-related resource warnings in authorized environments. Do not weaken TLS or security controls in production to make a test pass.

### Lighthouse

Use Lighthouse for repeatable audits of performance, accessibility, best practices, and SEO-related signals. Treat scores as diagnostic measurements under a test configuration, not universal production truth. Record URL, device/network profile, browser/version, run conditions, and variability.

## Chrome DevTools Protocol

CDP domains provide a programmable control and observation surface. The most relevant durable concepts are:

| Domain | Core capability |
|---|---|
| Network | Requests, responses, headers, cookies, cache, redirects, loading, WebSockets, and network conditions |
| Fetch | Pausing, inspecting, fulfilling, or continuing selected requests |
| Runtime | JavaScript evaluation, execution contexts, exceptions, console/runtime events |
| Page | Navigation, lifecycle, frames, dialogs, screenshots, printing, and page state |
| DOM | Document tree, nodes, attributes, mutations, and inspection |
| Debugger | Scripts, breakpoints, pauses, stack traces, source maps, and debug events |
| Performance | Tracing, metrics, timeline collection, and performance evidence |

Use capability discovery and version-aware compatibility checks. Keep CDP sessions scoped, authenticated, observable, and disconnected after use.

## Intercepting, mocking, and replaying

Define a narrow interception predicate before modifying traffic. Capture method, URL, headers, cookies metadata, payload shape, response status/headers/body metadata, redirects, timing, initiator, cache state, and correlation ID. Prefer replaying sanitized fixtures or HAR files over changing live production responses. When fulfilling or mocking, record that the response was synthetic, preserve the original contract, validate schemas, and prevent mock data from entering production indexes.

Blocking should be used for controlled performance or failure experiments with an explicit allowlist, not to conceal required dependencies. Request continuation, abort, and fulfillment need timeout, retry, and cleanup behavior. Verify that interception did not create a false success by changing the application path.

## Protocols and streaming

Handle WebSockets through connection, handshake, frame, close, and error evidence. Handle Server-Sent Events through connection lifecycle, event IDs, retry behavior, content type, and incremental parsing. Handle GraphQL by recording operation name, variables shape, persisted-query behavior, response errors, batching, and transport. Handle streaming responses by preserving chunk order, framing, cancellation, backpressure, and partial-result semantics. Redact tokens, personal data, and sensitive payloads.

## Browser automation integrations

Playwright routing and request interception should use scoped routes, explicit continuation/abort/fulfill decisions, context isolation, tracing, and cleanup. Puppeteer request interception and CDP sessions should coordinate listeners to avoid double-handling and should record the browser/context/page identity. Selenium can use performance logs and CDP integration where supported; always check browser/driver compatibility and avoid assuming that one Selenium binding exposes every CDP feature.

## Browser platform behavior

Understand service workers, browser cache, cache validation, storage, CORS, CSP, preflight OPTIONS requests, credentials mode, redirects, origin, SameSite, Secure, and HttpOnly cookie behavior. Diagnose authorization failures by separating browser policy, server policy, application authentication, and automation configuration. Never advise bypassing CORS, CSP, authentication, anti-abuse controls, or access restrictions on systems the learner does not own or have permission to test.

## Enterprise debugging workflow

For browser automation and crawling, establish a reproducible fixture and authorization first. Capture a trace/HAR or equivalent bounded evidence, identify the failing stage, correlate Network, Console, Runtime, Page, Performance, and Application evidence, make the smallest reversible change, rerun with the same conditions, and record the result. Feed only validated, authorized, provenance-preserving data into cleaning, storage, indexing, or RAG pipelines.
