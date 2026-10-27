# 05. APIs, contracts, queues, and external integrations

- `[API-001] MUST` HTTP APIs have stable input/output schemas and semantically correct methods/statuses. Prefer a supported OpenAPI version for external REST APIs.
- `[API-002] MUST` Validate incoming data at trust boundaries: HTTP, webhooks, queues, and third-party APIs. The server independently enforces permissions and business invariants.
- `[API-003] SHOULD` Use machine-readable error codes and a consistent format, such as HTTP Problem Details (RFC 9457) where appropriate. Do not expose stacks, secrets, SQL, or sensitive context.
- `[API-004] MUST` Define list size limits, pagination, ordering, filters, time limits, and predictable invalid-input behavior.
- `[API-005] MUST` Public contract breaks require versioning/a migration window, changelog, consumer monitoring, and a transition plan. Do not introduce silent breaking changes.
- `[API-006] MUST` Protect repeatable operations with side effects using idempotency keys, unique constraints, or state transitions. Define key scope, TTL/retention, and replay semantics.
- `[API-007] MUST` External calls have timeouts, status/schema validation, and normalized errors. Retry only classified transient failures, with backoff/jitter and an assessment of replay safety.
- `[API-008] MUST` Verify webhook provider authenticity, prevent replay, deduplicate events, and handle out-of-order delivery.
- `[API-009] SHOULD` Design workers/jobs for at-least-once delivery: deduplication, timeout, retries/dead-letter handling or manual failure resolution.
- `[API-010] SHOULD` Consider a transactional outbox when a database change and external effect must be coordinated atomically. Two independent writes are not atomic.
- `[API-011] MUST` Keep integration secrets out of frontend bundles, logs, URLs, and exception responses.

## Typical boundary
`HTTP/webhook → DTO validation → application use case → module contract / provider adapter → normalized result`. SDK structures stay inside the adapter.

## Delivery semantics
An HTTP timeout **does not prove** that the provider did not execute the operation. Check status using the correlation/idempotency key first, then retry safely. If status lookup is unavailable, use the provider's documented replay/reconciliation mechanism; do not assume the operation failed.
