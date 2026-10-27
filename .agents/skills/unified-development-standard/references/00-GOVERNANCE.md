# 00. Governance, scope, and exceptions

## Requirement levels and precedence
- `[GOV-001] MUST` For a new system or significant architectural change, record goals, stack, risks, environments, and owner in the existing profile/README. Create a separate PROJECT_PROFILE.md only when useful. Use existing context for a local change.
- `[GOV-002] MUST` Environment and user instructions define the task and authority; this standard does not expand them. Account for applicable contractual/legal constraints and report conflicts. Project decisions take precedence over this standard's recommended alternatives. References define rules; guides explain them; templates/examples illustrate them.
- `[GOV-003] MUST` Record departures from applicable mandatory rules with a reason, risk, mitigation, and owner. Use an ADR for significant architectural or hard-to-reverse decisions. Do not treat N/A as an exception or claim unverified compliance.
- `[GOV-004] MUST` Do not claim WCAG/ASVS/ISO compliance merely because a document exists: establish the scope and verify its requirements.
- `[GOV-005] MUST` When reporting rule coverage, give a reason for `N/A`. Conditional requirements do not become mandatory when the relevant functionality is absent; ordinary tasks do not need a full coverage table.
- `[GOV-006] SHOULD` Maintain one canonical standard. Pin its version in repositories through a submodule, template, path, or documented synchronization process; avoid editing divergent local copies.
- `[GOV-007] SHOULD` Review affected rules when risks change, after incidents, and at the agreed interval. Check tool support at the time of work; do not initiate an unrequested upgrade of the whole stack.

## Profiles
- **Minimal**: landing page/prototype without sensitive data — minimal architecture, checks for critical functions, linting where supported, validation according to CI-001, and safe deployment when deployed.
- **Standard (default)**: databases, authentication, integrations, real users — clear module boundaries, CI, migrations, authorization, backups, and monitoring for the capabilities present.
- **Critical**: payments, sensitive data, or high availability — stronger concurrency tests, security review, staged rollout, recovery rehearsal, and measured SLOs as applicable.

## Maintaining rules
- Rule IDs are permanent. Record semantic changes, rationale, and impact in the existing change record (PR/Git history or maintained changelog). Update a policy version when the project tracks one; do not create competing versioned documents.
- `MUST` requires evidence: configuration, test, linter output, screenshot/manual verification record, or audit record. Declarations alone are not evidence.
- `SHOULD` allows a documented rationale in the profile/PR without a large ADR.
- Where iOS, Android, and Web prescribe different UX, handle platform requirements in adapters while keeping shared semantics consistent.

## Exception format
`rule_id | project | reason | alternatives | risk | mitigation | owner | expiry/review | confirmation`.
