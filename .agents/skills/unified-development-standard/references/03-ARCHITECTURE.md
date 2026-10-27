# 03. System architecture and module boundaries

## Starting model
For a backend that needs module boundaries, prefer a modular monolith: `transport → application/use-cases → domain`, with `infrastructure` implementing required ports. Group by **business capability**, not product-wide `controllers/services/utils` folders. Static sites and local tools do not need a backend merely to follow this model.

- `[ARC-001] MUST` Give each entity and business rule a defined owner (bounded context/module) and known public contract. Do not modify another owner's data through a bypass.
- `[ARC-002] MUST` Keep domain logic independent of HTTP, UI, specific SDKs, databases, and platforms. Technical framework types in the domain require a justified exception.
- `[ARC-003] MUST` Avoid cyclic module dependencies. Import public contracts, not another module's internal repositories. For substantial codebases, check boundaries in CI.
- `[ARC-004] MUST` Route a request through one clear use case: authentication → validation → object authorization → business invariant → transactional changes → response mapping. Apply stages relevant to that operation; specific checks may be reordered without weakening protection.
- `[ARC-005] SHOULD` Start simply. When a backend is needed, prefer one deployable service; add separate workers only when necessary. Do not introduce CQRS, an event bus, or microservices for hypothetical future needs.
- `[ARC-006] MUST` Wrap integrations in adapters/anti-corruption layers; prevent SDK-specific models from spreading through the domain.
- `[ARC-007] MUST` Record an ADR for significant changes to boundaries, databases, deployment, major libraries, or consistency models.
- `[ARC-008] SHOULD` Centralize responsibility for configuration, logging, clocks, ID generation, and shared technical contracts. Do not turn `shared` into a miscellaneous dumping ground.

## Suggested layout
```text
src/
  modules/
    catalog/
      domain/
      application/
      infrastructure/
      transport/
      public.*
    accounts/
      ...
  app/             # composition root, server bootstrap
  shared/          # genuinely shared primitives only
  workers/         # call use cases without copying business logic
```

A small application may need only a few files, with no artificial empty directories. Matching a folder template is secondary: **a business rule should have one place to change**.

## Required change review
Who owns the rule? Does a similar implementation exist? Which way do dependencies flow? Must a consumer contract change? How will two sources of truth be avoided?

For practical patterns, read the relevant section of [decision formulas](../guides/PRACTICAL-FORMULAS.md).

For product, MVP, and architectural foundations, see [product and MVP planning](../guides/PRODUCT-AND-MVP-PLANNING.md).
