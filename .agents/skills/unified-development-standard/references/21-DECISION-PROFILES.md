# 21. Project types, requirement sets, and tool selection

- `[PROF-001] MUST` Select tools by product constraints, operational needs, team skills, stable support, and maintenance cost. No stack is mandatory for every project.
- `[PROF-002] SHOULD` For applications needing backend/domain modules, start with a modular monolith and one repository unless distributed systems have a demonstrated need. This does not require adding a backend to a static site or local tool.
- `[PROF-003] SHOULD` A baseline release path is GitHub → PR → Actions CI → registry/versioned artifact → deployment controller → health → rollback. Use equivalent facilities on the project's chosen platform.
- `[PROF-004] SHOULD` Choose hosting by requirements: static/CDN, managed runtime, serverless, or containers. Docker+Compose and Podman+Quadlet are options for justified single-VPS deployments, not mandatory web stacks.
- `[PROF-005] MUST` Give each application system one responsible deployment mechanism and one HTTPS ingress owner. Document architectural exceptions.
- `[PROF-006] SHOULD` Use **supported stable** versions, lockfiles, and periodic EOL/update reviews.

| Type | Typical profile | API/database | CI/CD | Operating model |
|---|---|---|---|---|
| Static site | Minimal | Add only when needed | Lint/build/link-check/deploy | CDN or simple hosting |
| Online service, catalog, CRM | Standard | Module boundaries, migrations, auth where needed | Unit/integration/security/build | Managed platform or justified Docker+Compose |
| Payment/personal-data service | Critical according to risk | Idempotency, audit trail, threat model | Stronger integration and negative tests | Controlled releases and restore drills |
| Mobile application | Standard/Critical | Separate backend contract where present | Platform build/signing/tests | Stores/release channels; containers only where relevant to backend/CI |
| Modular library | Standard | Versioned contracts | API compatibility, multi-version tests | Signed artifacts/registry as applicable |
| CLI/script | Minimal | As needed | Lint/test/package | Versioned executable; no default Docker requirement |

These are starting points. Select the profile and applicable controls from actual risk and project scope.

## Docker/Podman decision ADR
Evaluate ecosystem, Compose semantics, rootless operation, volume permissions, systemd, CI image builds, secrets, health/reboot/recovery, observability, and integration with the selected platform. Support the decision with tests, not marketing claims.

For task-specific patterns and examples, read the relevant section of [practical formulas](../guides/PRACTICAL-FORMULAS.md).

For product, MVP, and architectural-foundation planning, see [product and MVP planning](../guides/PRODUCT-AND-MVP-PLANNING.md).
