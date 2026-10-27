---
name: uds-dependency-upgrades
description: "Use when upgrading dependencies, frameworks, runtimes, SDKs, databases, operating systems, containers, or external APIs, including CVEs, EOL, and major-version compatibility changes."
---
# Dependency and compatibility upgrades

## Scope and inputs
Use for version/support changes, not every code edit. Inspect manifests, lockfiles, runtime versions, package manager, support matrix, deployment target, CI commands, release history, and affected API consumers.

## Procedure
1. Inventory affected direct/transitive dependencies, runtime, build toolchain, CI images, OS/database/API/SDK versions, and their canonical source.
2. Check official supported stable releases, EOL, advisories, and platform support as of the task date. Do not rely on remembered versions or select production prereleases without an explicit decision.
3. Review release notes, migration guides, breaking APIs, deprecated configuration, types/plugins, and consumer/server compatibility.
4. Separate safe patch/minor updates from risky majors and urgent security fixes from scheduled work. Avoid unreviewed mass upgrades.
5. Make the smallest manifest/lockfile/configuration patch within the repository workflow. Keep strict checks enabled.
6. Run relevant clean/reproducible install, lint/types/tests/build, migration-compatibility, and staging smoke checks according to risk; account for supported old mobile clients.
7. For database/infrastructure changes, plan applicable expand-migrate-contract steps, backups, and rollback. Do not promise reversibility for destructive migrations.
8. Record before/after versions, support status, conflicts, failed checks, rollout/rollback, and production observation needs.
9. Remove deprecated code and temporary compatibility layers after safe migration, with a bounded lifetime.

## Output and verification
Update the existing upgrade plan or create UPGRADE_PLAN.md when needed. Include scoped inventory/risk, diff/lockfile, compatibility, actual install/build/test results, and rollout/mitigation. Supported stable versions, a consistent lockfile, addressed breaking changes, and verification evidence are the completion criteria. Claim latest only after checking dated official sources.
## Core rules
Use the sibling [core workflow](../unified-development-standard/SKILL.md) once per context; reuse it if already read. Then read only relevant sections of: 25-DEPENDENCIES, 12-TESTING, 22-RELEASE. Apply core 00-GOVERNANCE scope. Do not recursively rediscover profiles/core or load the full corpus for a local edit. If core is unavailable, report that limitation without claiming compliance with unread rules.

