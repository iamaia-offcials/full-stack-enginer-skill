---
name: uds-backend
description: "Use when changing server-side business operations, HTTP APIs, integrations, authorization, or backend reliability."
---
# Backend implementation

## Inputs
Repository/stack, requirements, API contracts, business invariants, dependencies, and trust boundaries.

## Procedure
1. Locate existing use cases/handlers/services, the owner of the business invariant, and analogous behavior.
2. Define transaction boundaries, resource authorization, schema/input validation, and idempotency for repeatable operations.
3. Isolate external APIs behind adapters/typed contracts. Select timeouts, retry/backoff, and errors according to operation semantics.
4. Keep shared logic in its domain/use-case owner rather than copying it into routes, controllers, or background workers.
5. Update affected OpenAPI/DTO/event contracts and data schemas without silently breaking clients.
6. Test relevant success, rejection, concurrency, dependency-failure, and permission cases; run actual repository commands.
7. Report migrations, backward compatibility, rollback options, and failure response.

## Output and verification
Provide changed contracts/services/handlers, relevant tests and execution evidence, and material operational risks. Verify API authorization and input handling. One happy-path test is insufficient for critical operations.
## Core rules
Use the sibling [core workflow](../unified-development-standard/SKILL.md) once per context; reuse it if already read. Then read only relevant sections of: 03-ARCHITECTURE, 05-API-INTEGRATIONS, 07-SECURITY-PRIVACY. Apply core 00-GOVERNANCE scope. Do not recursively rediscover profiles/core or load the full corpus for a local edit. If core is unavailable, report that limitation without claiming compliance with unread rules.

