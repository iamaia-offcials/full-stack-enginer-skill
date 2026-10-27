# 02. Functional/nonfunctional requirements and task design

- `[REQ-001] MUST` Record expected behavior and how to verify it. For substantial features, include actor/trigger, data, preconditions/postconditions, business invariants, negative cases, and security. For a small change, use concise criteria in the existing task.
- `[REQ-002] MUST` A data-changing requirement identifies the record owner, source of truth, important invariants, and behavior on repeated execution.
- `[REQ-003] MUST` Record applicable nonfunctional targets: performance, accessibility, SEO, internationalization, privacy, availability, latency, RPO/RTO, and resource budgets.
- `[REQ-004] MUST` When public behavior changes, assess existing clients, data/contract compatibility, feature flags, and migrations.
- `[REQ-005] SHOULD` For stateful scenarios, describe transitions: allowed/forbidden, actor, conditions, and atomic changes.
- `[REQ-006] SHOULD` Split tasks vertically by useful scenario rather than completing all DTOs and then all services without a working outcome.
- `[REQ-007] MUST` Done means implemented behavior, tests for critical rules, updated documentation, and passing applicable quality gates. A visually opened UI is insufficient.

## Acceptance criteria example
`Given` an authenticated user owns object X. `When` they submit a valid update to X. `Then` only X changes and the contractual result is returned; replay causes no unintended side effects; another user is denied without leaking details.

## Definition of Ready
Priority, scope, reproducible conditions, and required contracts are available.

## Definition of Done
Expected behavior works without new duplication; affected risks are checked and changed contracts/docs updated. Apply type, authorization, concurrency, and rollback checks according to the change. Explicitly report checks not run instead of marking them PASS.

For practical patterns, read the relevant section of [decision formulas](../guides/PRACTICAL-FORMULAS.md).

For planning SEO, measurement, and integrations, see [SEO and analytics](../guides/SEO-ANALYTICS-PLANNING.md).

For product, MVP, and architectural foundations, see [product and MVP planning](../guides/PRODUCT-AND-MVP-PLANNING.md).
