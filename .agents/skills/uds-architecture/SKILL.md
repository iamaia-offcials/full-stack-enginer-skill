---
name: uds-architecture
description: "Use when choosing or reviewing application structure, module boundaries, dependency direction, logic ownership, or significant architectural decisions."
---
# Architecture and module boundaries

## Inputs
Task context, repository, nonfunctional requirements, data models, integrations, and deployment topology.

## Procedure
1. Inspect existing structure and call paths; a directory tree alone is insufficient evidence for redesign.
2. Map domain modules, APIs, owners of business rules/dependencies, and state/transaction boundaries.
3. Separate presentation, orchestration/use cases, domain invariants, and infrastructure where useful.
4. Find duplicate implementation paths, dependency cycles, leaked ORM/types, and shared mutable state.
5. For a significant choice, compare at least two reasonable options and record trade-offs in an ADR.
6. Choose the simplest sufficient structure, usually a modular monolith when an application needs backend modules and distribution has no proven benefit.
7. Define relevant architecture/import-boundary checks, migration needs, security, and observability.

## Output and verification
Provide a context/container/module diagram as useful, ownership map, contracts, decisions/ADRs, and compatible change stages. Scale artifacts to the decision. Create abstractions only for real scenarios or a clear justification; never silently break contracts.
## Core rules
Use the sibling [core workflow](../unified-development-standard/SKILL.md) once per context; reuse it if already read. Then read only relevant sections of: 03-ARCHITECTURE, 04-CODE-QUALITY, 21-DECISION-PROFILES. Apply core 00-GOVERNANCE scope. Do not recursively rediscover profiles/core or load the full corpus for a local edit. If core is unavailable, report that limitation without claiming compliance with unread rules.

