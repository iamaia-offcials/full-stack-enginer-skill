---
name: uds-project-audit
description: "Use when a broad technical audit of an existing repository is requested across architecture, duplication, security, UI, testing, or deployment; not for a small isolated fix."
---
# Repository audit

## Inputs
Available files and commit hash, requirements/project profile, CI configuration, and actual test/environment access.

## Procedure
1. Record scope: commit, packages, and environments. Audits are read-only unless fixes are also requested/authorized.
2. Inspect applicable owners, duplicated logic, domain boundaries, APIs, database, UI tokens/supported themes, authorization, and supply chain within the accessible scope.
3. Select relevant core reference rules; mark nonapplicable controls N/A with reasons. A broad audit still does not require unrelated workflows.
4. For each defect, give file/line or command evidence, severity, impact, and recommended action.
5. Run safe available checks and retain actual output/time/context; state unavailable checks separately.
6. Distinguish quick wins, architectural violations, release blockers, and dependencies. Repository evidence is different from speculative idea evaluation.
7. Produce a remediation backlog and PASS/FAIL/UNKNOWN/N/A for assessed rules. Missing evidence means UNKNOWN.

## Output and verification
Provide a traceable report, findings/evidence, bounded rule coverage, P0/P1/P2 remediation priorities, and unexamined areas. AGENTS.md or test-file existence alone cannot prove compliance. A scoped audit is not certification of the entire project.
## Core rules
Use the sibling [core workflow](../unified-development-standard/SKILL.md) once per context; reuse it if already read. Then read only relevant sections of: 19-AI-EXECUTION, 26-SKILL-ORCHESTRATION, plus domain references selected by audit scope. Apply core 00-GOVERNANCE scope. Do not recursively rediscover profiles/core or load the full corpus for a local edit. If core is unavailable, report that limitation without claiming compliance with unread rules.

