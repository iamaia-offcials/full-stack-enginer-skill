---
name: uds-testing
description: "Use when planning or running verification for code changes, regressions, acceptance criteria, accessibility, or release readiness."
---
# Testing and quality verification

## Inputs
Changes, acceptance criteria, risks, stack, available commands, and user scenarios.

## Procedure
1. Map acceptance criteria to proportionate test levels and priorities.
2. For critical operations, cover relevant negative cases, races, authorization, idempotency, and degraded dependencies.
3. Prefer unit/integration checks when sufficient; avoid redundant expensive e2e coverage. Smoke tests cover the key flow.
4. For affected UI, check keyboard, accessibility, supported themes/locales, actual viewport sizes, and relevant error states.
5. Run applicable repository commands when the environment is available. Mark unavailable/unrun checks NOT_RUN, never PASS.
6. Distinguish flaky tests from confirmed defects; collect evidence and assess coverage against actual risks.
7. Report a scoped PASS/BLOCKED/UNKNOWN decision with rationale and reproduction.

## Output and verification
Provide the relevant test plan and actual results, commands/versions, failures, and scoped release-gate status. No execution means no execution-based PASS; inability to run means UNKNOWN/NOT_RUN. The task does not require new themes, localization, or test infrastructure unrelated to the change.
## Core rules
Use the sibling [core workflow](../unified-development-standard/SKILL.md) once per context; reuse it if already read. Then read only relevant sections of: 12-TESTING, 22-RELEASE. Apply core 00-GOVERNANCE scope. Do not recursively rediscover profiles/core or load the full corpus for a local edit. If core is unavailable, report that limitation without claiming compliance with unread rules.

