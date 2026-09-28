# Enterprise Crawling, Browser Automation, and Indexing

Use this reference for enterprise scraping/crawling, Selenium, Puppeteer, Playwright, browser agents, parsing, cleaning, storage, indexing, search, ranking, and RAG ingestion.

## Acquisition decision

Prefer an authorized API, feed, export, or direct HTTP parser. Use Selenium/WebDriver for established cross-browser/Grid environments, Puppeteer/CDP for Chromium-focused instrumentation and network control, and Playwright for isolated contexts, reliable locators, cross-browser workflows, testing, and extraction. Use browser automation only when rendering or interaction is genuinely required.

## Pipeline

Design: scope and authorization → frontier and scheduler → acquisition → parse → clean/normalize → enrich and deduplicate → store raw and derived records → index lexical/vector/graph/time-aware views → retrieve/rank/rerank → monitor freshness, drift, access, and deletion.

Cover canonical URLs, politeness, rate/concurrency budgets, retries, checkpoints, pagination, infinite scroll, frames, shadow DOM, lazy loading, XHR/fetch/GraphQL capture, structured data, PDF/office/media parsing, OCR/transcription where authorized, content hashes, provenance, language, chunk metadata, permissions, versions, and deletion propagation.

## Browser reliability

Use isolated contexts, semantic locators, explicit waits, bounded navigation, timeout budgets, retries, circuit breakers, browser resource limits, tracing, screenshots/HAR where appropriate, fixture pages, parser tests, schema-drift alarms, and deterministic replay. Keep cookies, tokens, and storage state in secret management, never in source or artifacts.

For browser network debugging, load `references/chrome-devtools-and-network-debugging.md`. Use the DevTools Network, Sources, Application, Performance, Memory, Console, Security, and Lighthouse surfaces to correlate requests, runtime behavior, storage, traces, memory, security state, and audit conditions. Use CDP Network, Fetch, Runtime, Page, DOM, Debugger, and Performance domains for programmable diagnostics, with capability/version checks and scoped sessions.

Capture request and response method, URL, headers, cookie metadata, payload shape, status, response metadata, redirects, timing, initiator, cache state, WebSocket/SSE/GraphQL/streaming events, and correlation IDs. Use narrow predicates for interception, blocking, mocking, fulfillment, and replay; mark synthetic responses, sanitize HAR/fixtures, and prevent test data from entering production indexes. Integrate Playwright routing, Puppeteer interception/CDP sessions, and Selenium performance logs/CDP where supported.

Diagnose service workers, browser cache, CORS, CSP, preflight requests, redirects, authentication, session state, and secure cookies by separating browser policy from server policy and automation configuration. Preserve authorization, least privilege, secret redaction, reproducibility, and cleanup.

## Enterprise operations

Use queues, distributed workers, backpressure, partitioning, observability, cost controls, storage tiers, disaster recovery, and service-level objectives. Preserve raw evidence and transformation lineage. Measure coverage, freshness, duplicate rate, extraction accuracy, index quality, latency, cost, and recovery behavior.

Do not teach credential theft, CAPTCHA bypass, stealth evasion, access-control bypass, abusive crawling, paywall circumvention, stalking, doxxing, or collection without authorization. For authenticated sources, require explicit permission, least privilege, audit logs, minimization, retention, and deletion policies.
