# 22. Release gates and checklist

Apply gates to the release and platform in scope. Database, container, infrastructure, theme, and locale checks apply only where those capabilities exist or are required; record N/A where useful.

- `[REL-001] MUST` Identify the release candidate by source commit, immutable artifact version/digest, commit-linked changelog, and any migration/configuration changes.
- `[REL-002] MUST` All applicable mandatory CI gates pass; record exceptions and the responsible person's approval. Unrun checks are not successful checks.
- `[REL-003] MUST` Verify applicable environment secrets, permissions, ingress/TLS, firewall, volumes/backups, and that no second independent auto-deploy controller exists.
- `[REL-004] MUST` For data changes, apply compatible migrations under a lock, prepare code rollback, and address irreversible data consequences separately.
- `[REL-005] MUST` At deployment, verify readiness, a key smoke flow, errors/logs/metrics, and the deployed version. Stop promotion and respond on failure.
- `[REL-006] MUST` After a release/incident, update operational documentation when affected and remediate recurring defects discovered.
- `[REL-007] SHOULD` Limit the blast radius of high-risk rollouts with staged releases, feature flags, canaries, or maintenance windows where the technology and business support them.

## Before merge
- [ ] Current acceptance criteria are met.
- [ ] No duplicated logic, uncontrolled CSS, or second equivalent API client was introduced.
- [ ] Relevant types, lint, architecture, unit/integration/contract/e2e checks ran according to risk.
- [ ] Changed UI was checked for accessibility, supported themes/locales, and responsive behavior.
- [ ] Affected operations have authorization/retry/database-race checks where applicable.
- [ ] Affected documentation, API schemas, migrations, and ADRs are current.

## Before production
- [ ] Artifact version/digest is pinned, required CI passed, and deployment has one owner.
- [ ] Applicable environment secrets, backups, and pre-release baseline are verified.
- [ ] Expand migrations remain compatible with the old application during rollback.
- [ ] Rollout and smoke checks are prepared, with an owner and incident contact/channel.

## After production
- [ ] The actual endpoint/application responds and key user scenarios work.
- [ ] Relevant error rates, p95 latency, and background jobs are observed.
- [ ] Version and outcome are recorded, with a verifiable rollback path.
