---
name: uds-code-review
description: "Use when reviewing a PR or code change, investigating duplicated logic, or performing a requested focused refactor or cleanup."
---
# Code review and duplication

## Inputs
Repository/PR diff, task, tests, architecture context, and AGENTS.md.

## Procedure
1. Bound the review to the diff, relevant dependencies, and public contracts; avoid unrelated work.
2. Find copy/paste and semantically duplicated business rules. Similar-looking code may enforce different invariants.
3. Check affected ownership, cycles, side effects, N+1 queries, authorization, and error handling.
4. Rank findings by severity and provide exact file/line evidence plus a plausible failure scenario.
5. Propose the smallest safe refactor; visual similarity alone does not justify merging components.
6. When code changes are authorized, establish the relevant contract/tests, make bounded edits, and run meaningful checks.
7. Distinguish pre-existing problems from regressions and from changes actually made.

## Output and verification
Provide findings with severity, location, evidence, and fix; identify the owner of duplicated logic. Produce a bounded patch only when requested/authorized. Review is read-only by default. Never invent line numbers or duplication claims without inspecting source.
## Core rules
Use the sibling [core workflow](../unified-development-standard/SKILL.md) once per context; reuse it if already read. Then read only relevant sections of: 03-ARCHITECTURE, 04-CODE-QUALITY, 12-TESTING. Apply core 00-GOVERNANCE scope. Do not recursively rediscover profiles/core or load the full corpus for a local edit. If core is unavailable, report that limitation without claiming compliance with unread rules.

