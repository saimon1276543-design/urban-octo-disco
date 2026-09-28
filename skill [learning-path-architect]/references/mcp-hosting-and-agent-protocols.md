# MCP Hosting and Agent-to-Agent Protocols

Use this reference for making and hosting MCP URL connections, MCP servers, interoperable agent systems, and secure protocol design.

## MCP server route

Define tools, resources, prompts, schemas, capability discovery, validation, errors, cancellation, timeouts, versioning, observability, and tests. Choose local, private-network, or public deployment based on authorization and exposure needs. For a URL endpoint, plan DNS, TLS, reverse proxy, health checks, transport/session behavior, rate limits, request-size limits, authentication, authorization, origin checks, tenant isolation, audit logs, secret management, and rollback.

Probe capabilities before mutation, use least privilege, and verify writes after execution. Record endpoint identity, server revision, request provenance, and unsupported capabilities. Current SDK syntax and transport support require current verification.

## Agent-to-agent protocol

Define identities, capabilities, message envelopes, task delegation, context transfer, routing, trust, authorization, provenance, state, retries, idempotency, version negotiation, human approval, escalation, and failure handling. Distinguish a protocol message from an authorized action. Never grant child agents more authority than the parent task permits.

## Operations

Test reachability, TLS, proxy headers, streaming, timeouts, serialization, retries, partial failures, and compatibility. Keep secrets out of prompts, logs, source control, and artifacts. Require data minimization, retention/deletion rules, and human approval for high-impact actions.
