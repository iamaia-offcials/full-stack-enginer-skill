# 25. Dependencies, licenses, and supply-chain resilience

- `[DEP-001] MUST` Each new dependency has an owner, license, active support, acceptable risk profile, and a reason existing platform capabilities are insufficient.
- `[DEP-002] MUST` Use lockfiles/frozen installs. Select **officially supported stable** SDK/runtime releases and track EOL. Production beta/preview use requires a justified ADR.
- `[DEP-003] MUST` Vulnerability triage goes beyond CVE counts: establish reachability, severity, remediation deadline, and compensating controls. Do not silently ignore critical exploitable risk.
- `[DEP-004] MUST` Treat CI/CD actions and container images as privileged third-party code. Pin trusted digests/SHAs, minimize permissions, and protect registries.
- `[DEP-005] SHOULD` Use regular dependency-bot updates with CI, dependency review, and SBOMs for Standard/Critical projects where maintenance capacity supports them.
- `[DEP-006] MUST` Check licenses and obligations before distribution/commercial use. Resolve license conflicts before proceeding with affected use.

Library popularity does not prove quality or security. Building an alternative also creates maintenance cost and risk, especially for security features.

## Updates, EOL, and compatibility
- `[DEP-007] MUST` Maintain an inventory and canonical source of runtime/framework/SDK/database/container/OS/API versions in use. Before major upgrades, verify official stable releases and support/EOL.
- `[DEP-008] MUST` Review migration guides, breaking changes, and peer/runtime/OS compatibility; version numbers alone are insufficient.
- `[DEP-009] MUST` Align manifest, lockfile, CI build image, and production runtime on supported compatible versions. Verify clean/frozen installation and builds.
- `[DEP-010] SHOULD` Schedule dependency reviews and, where feasible, automated PRs (Renovate/Dependabot or equivalent). Do not auto-merge high-risk major upgrades.
- `[DEP-011] MUST` Handle urgent security fixes separately from planned upgrades, prioritizing actual exploitation and compensating controls.
- `[DEP-012] MUST` Major upgrades undergo relevant contract/CI/staging compatibility checks and rollback verification. Account for old mobile clients and database expand/migrate/contract changes where applicable.
- `[DEP-013] MUST` Do not use beta/RC/canary releases as the general production default. Exceptions need explicit rationale and controlled risk. A framework's internal canary runtime is not equivalent to independently selecting an unstable dependency.
- `[DEP-014] SHOULD` Remove temporary compatibility layers and deprecated implementations after migration, with a documented removal deadline.
- `[DEP-015] MUST` Support claims of the latest stable version with a dated official source at upgrade time. Do not hard-code current versions into a permanent standard.
