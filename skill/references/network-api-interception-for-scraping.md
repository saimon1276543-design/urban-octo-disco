# Network API Interception for Scraping

Use this reference when the learner wants to discover, observe, capture, replay, mock, or extract data from browser network APIs for an authorized scraping or testing workflow. Treat protocol names and browser concepts as durable; verify current library methods, browser support, and site rules before implementation.

## Definition

**Network API interception** is the controlled observation or handling of requests and responses made by an application. It is useful when the visible page is only a presentation layer and the data arrives through XHR, `fetch`, GraphQL, WebSocket, Server-Sent Events, or another browser-managed channel.

Interception can mean:

- **Observe:** record request and response metadata without changing traffic.
- **Capture:** preserve selected response bodies or structured payloads as sanitized evidence.
- **Replay:** run the same request against a fixture or authorized endpoint.
- **Fulfill/mock:** return a synthetic response for testing.
- **Block/continue:** deliberately stop or allow a request in a controlled experiment.
- **Transform:** parse or normalize captured data after acquisition; do not silently alter source evidence.

## First decision: use the least complex acquisition method

Prefer, in order:

1. An authorized public or private API.
2. An official export, feed, or data download.
3. Direct HTTP requests when the endpoint and authorization are clear.
4. Browser network observation when rendering, session state, client-generated parameters, or interaction is genuinely required.
5. Browser automation for interaction and extraction only when simpler methods cannot satisfy the task.

Do not treat interception as permission to bypass authentication, access controls, rate limits, CAPTCHAs, paywalls, anti-abuse mechanisms, or terms that prohibit the activity.

## Conceptual request lifecycle

```text
page action → browser context → service worker/cache → request
           → redirect/auth/preflight → server response
           → stream/WebSocket events → application state → rendered view
```

A scraper should identify which stage contains the desired data. The rendered DOM may be incomplete, while the response body may contain structured records. Conversely, a response may be encrypted, abbreviated, paginated, or useless without the application’s subsequent requests.

## What to record

For every selected request, record a correlation ID and, where authorized:

- Method, URL pattern, origin, and resource type.
- Query and path parameters with secrets removed.
- Request payload shape, operation name, or GraphQL variables shape.
- Status, response headers, content type, and body schema.
- Redirect chain, initiator, timing, cache state, and retry behavior.
- Pagination cursor, page size, continuation token metadata, or offset.
- WebSocket handshake and frame type, or SSE event ID and retry behavior.
- Browser context, page, fixture, timestamp, and tool/version.

Never store raw cookies, bearer tokens, passwords, personal data, or unnecessary session state in source code, HAR files, logs, or generated knowledge indexes.

## Browser/tool surfaces

| Surface | Best use | Main caution |
|---|---|---|
| DevTools Network | Discover request sequence and inspect payloads | Manual observations are not automatically reproducible |
| CDP Network | Observe browser requests and responses | Check browser/protocol version and scope the session |
| CDP Fetch | Pause, continue, abort, or fulfill selected requests | A synthetic response can create a false success |
| Playwright routing | Isolated contexts, fixtures, request handling | Use narrow predicates and always continue or fulfill deliberately |
| Puppeteer interception/CDP | Chromium-focused instrumentation | Coordinate listeners to avoid double-handling |
| Selenium logs/CDP | Existing WebDriver/Grid environments | Feature support varies by binding and driver |
| HAR/trace replay | Deterministic offline testing | Sanitize secrets and mark responses as recorded fixtures |

## Discovery workflow

1. Confirm authorization, scope, retention, and rate limits.
2. Use a clean or isolated browser context and a representative fixture.
3. Record the user action that triggers the data request.
4. Filter requests by method, resource type, URL, operation name, or response type.
5. Identify the minimum request sequence needed to obtain the target data.
6. Determine whether direct HTTP reproduction is reliable and permitted.
7. Capture a sanitized fixture or bounded sample.
8. Write a parser and schema test against the fixture.
9. Run the authorized acquisition with budgets, retries, checkpoints, and cleanup.
10. Preserve provenance from source request to parsed record and downstream index.

## Common API patterns

### XHR and fetch

Inspect request method, query/body parameters, pagination, response schema, and error envelopes. Do not assume that a visible button maps to one request; record dependent calls and client-side joins.

### GraphQL

Record operation name, variables shape, endpoint, persisted-query behavior, batching, aliases, pagination, and response errors. Keep the query and variables separate from secrets. A GraphQL response may contain partial data alongside errors.

### WebSocket

Capture the handshake, authentication metadata without secret values, subscription or command shape, frame direction, event type, sequence, close code, and reconnection behavior. Preserve ordering and distinguish commands from server events.

### Server-Sent Events

Record the connection lifecycle, content type, event IDs, retry timing, `Last-Event-ID` behavior, event framing, and incremental parsing. A final page snapshot may omit events received earlier.

### Service workers and cache

Check whether the service worker fulfills, transforms, caches, or delays the request. Compare a controlled context with cache disabled or a fresh profile only when permitted. Do not disable security controls on a production system merely to make extraction work.

## Reliability and data quality

Use bounded navigation, timeout budgets, retries, circuit breakers, concurrency limits, pagination checkpoints, schema-drift alarms, duplicate detection, content hashes, and deterministic fixture tests. Preserve raw authorized evidence separately from cleaned records. Track extraction coverage, missing pages, parse failures, freshness, and deletion or correction propagation.

When an interception rule is changed, rerun the same fixture and compare request count, response schema, extracted records, and error behavior. Verify that mocks, blocked calls, cache effects, or altered headers did not create a false success.

## Safety and authorization boundary

This reference supports authorized data collection, debugging, testing, research, and interoperability work. It does not support credential theft, session hijacking, access-control bypass, CAPTCHA or anti-bot evasion, covert surveillance, abusive crawling, paywall circumvention, privacy-invasive collection, or scraping systems without permission. When authorization is uncertain, stop at conceptual explanation or use a local fixture that the learner owns.

## Evidence for a scraping project

A credible project should submit:

- Scope and authorization statement.
- Sanitized request/response sample or HAR/trace.
- Acquisition method and reason simpler methods were rejected.
- Parser and schema tests.
- Pagination, retry, and rate-limit behavior.
- Provenance and redaction policy.
- Coverage and failure report.
- Demonstration on a fixture or authorized target.

A captured request proves that a request occurred. It does not by itself prove permission, complete coverage, extraction accuracy, production reliability, or long-term maintainability.
