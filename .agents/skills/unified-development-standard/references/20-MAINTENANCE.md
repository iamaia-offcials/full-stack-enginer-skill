# 20. Maintenance, technical debt, updates, and incidents

- `[MAIN-001] MUST` Maintain supported stable runtimes/frameworks/base images. Track EOL and security advisories; verify updates with CI, compatibility, and rollback checks.
- `[MAIN-002] MUST` Track technical debt with its impact, risk, owner, plan/deadline or acceptance rationale. Deferred work needs visible status.
- `[MAIN-003] SHOULD` Remove feature flags and temporary adapters after migrations; retire obsolete endpoints according to compatibility policy.
- `[MAIN-004] MUST` Close critical incidents with a blameless postmortem: timeline, impact, root cause/contributing factors, concrete actions, and owners.
- `[MAIN-005] MUST` Update dependencies with lockfiles, changelog review, and tests. Avoid uncontrolled auto-updates of production packages or containers.
- `[MAIN-006] SHOULD` Periodically audit architectural cycles, copied business rules, duplicate UI, obsolete configuration, and secrets; track technical-debt reduction.
- `[MAIN-007] MUST` Recheck applicable backup/restore, certificates, secrets, permissions, and vulnerabilities. Initial setup is not permanent evidence of correctness.
- `[MAIN-008] SHOULD` Improve the shared standard from recurring issues, with a changelog and controlled adoption across existing repositories.

## Example cadence; adapt to risk
- Each PR: code/design/security review as applicable.
- Weekly/per release: dependency triage, failed jobs, alerts, error budget.
- Monthly: restore spot-check, open technical debt, configuration freshness.
- Every six months: review the standard version, practices, tools, and threats.
