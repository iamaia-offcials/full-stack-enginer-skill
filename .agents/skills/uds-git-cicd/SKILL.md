---
name: uds-git-cicd
description: "Use when changing Git workflows, pull-request checks, CI/CD, release artifacts, environments, or deployment automation, including containers when the project uses them."
---
# Git, CI/CD, and deployment

## Inputs
Repository, hosting provider/VPS, stack, existing workflows, secrets/environments, and release policy.

## Procedure
1. Inspect main-branch protections, branches, tags, workflows, registries, and the actual deployment controller.
2. Separate CI (relevant lint/types/tests/build/security) from CD (delivery of the approved immutable artifact).
3. Choose a proportionate Git model: short feature branches, PR review, required checks, and one release source of truth.
4. Follow the chosen hosting model. If containers are justified, compare Docker/Compose and Podman/Quadlet for compatibility and team needs; verify actual Coolify/Dokploy/stack support.
5. Design least-privilege credentials, secret storage, action/image pins, locked dependencies, deployment concurrency, and atomic/serialized migrations where relevant.
6. Define environments appropriate to risk, readiness/smoke, rollback, applicable backup/restore rehearsal, and acceptable downtime.
7. Before deployment, verify authority, consequences, and required approvals, reusing existing authorization. Provide execution commands and expected success signals.

## Output and verification
Provide the relevant Git policy, CI/CD graph, container blueprint only when used, deploy/rollback runbook, and actual verification status. One chain owns CD. Workflow YAML alone does not prove a deployment occurred or succeeded.
## Core rules
Use the sibling [core workflow](../unified-development-standard/SKILL.md) once per context; reuse it if already read. Then read only relevant sections of: 13-GIT, 14-CI-CD, 15-CONTAINERS (only for containers), 22-RELEASE. Apply core 00-GOVERNANCE scope. Do not recursively rediscover profiles/core or load the full corpus for a local edit. If core is unavailable, report that limitation without claiming compliance with unread rules.

