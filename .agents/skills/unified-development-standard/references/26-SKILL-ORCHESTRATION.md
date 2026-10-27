# 26. Specialized skill orchestration

**Purpose:** connect relevant work stages without excessive context, false activation, or unverifiable chaining.

- `[SKL-001] MUST` Select a skill by task intent and expected outcome, not incidental terminology.
- `[SKL-002] MUST` Verify another skill is available before using it. A documented route does not invoke tools or grant authority.
- `[SKL-003] MUST` Normative rules live in core `references/`. Specialized workflows must not contradict or silently replace them.
- `[SKL-004] MUST` Scope workflows to the requested change. Read the core workflow once per context, then only relevant rule sections. Reuse already loaded instructions; do not recursively rediscover core/profiles or read the whole suite for a local edit. A full lifecycle applies only when the task needs it.
- `[SKL-005] MUST` Identify the basis for specialized work: existing code, requirements, design, or contracts. When missing, separate assumptions from facts.
- `[SKL-006] MUST` Produce reviewable artifacts, acceptance criteria, and actual execution evidence appropriate to the task. Do not claim a gate passed without running its required checks.
- `[SKL-007] MUST` Analysis/audit is **read-only** by default. Refactoring, deployment, and dangerous actions need authorization within the task context; an explicit request to fix issues supplies authority for scoped fixes, subject to applicable action controls.
- `[SKL-008] SHOULD` Start with the specialization matching the main intent. Add another workflow only for a real dependency (for example, UI accessibility or release verification); reuse relevant sections instead of restarting discovery.
- `[SKL-009] SHOULD` Reuse decision records and handoff artifacts across lifecycle work instead of retelling the entire project. Update canonical current documentation; label plans and historical records separately.
- `[SKL-010] SHOULD` Validate a skill suite for syntax/links, positive and negative trigger cases, and real-repository output quality.

## Responsibilities
**Core** defines normative scope and routing. A **specialized skill** provides a task procedure. **Tools** provide repository, browser, CI, profiler, or indexing operations only when actually available. **Project profiles/ADRs** define context and permitted variations. Do not copy parallel mandatory-rule catalogs into each workflow.

## Candidate gates
1. Discovery → testable hypothesis and context.
2. Requirements → constraints and acceptance criteria.
3. Architecture → ownership, dependencies, invariants.
4. Design → states, visual system, accessibility.
5. Build → minimal changes without parallel implementations.
6. Verification → actual test results.
7. Release → controlled artifact and rollback path.
8. Operations → observability and recovery.

Choose applicable gates from the task and project profile; mark others N/A where useful. A small change does not require restarting discovery, creating an MVP, or generating a full document set.

## Applicability
- Implement code-first UI/design through real components, styles, and browser checks. Design-editor subscriptions are not prerequisites.
- Route technical SEO only to public URLs intended for indexing; private web/Mini Apps are usually N/A.
- Mobile web and native applications have different platform/release gates; do not impose store publication on ordinary websites.
- Use performance workflows for a measurable problem or budget, and upgrade workflows for version/compatibility changes. Add layers and tools only for demonstrated needs.
