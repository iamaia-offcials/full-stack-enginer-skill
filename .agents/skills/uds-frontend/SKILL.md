---
name: uds-frontend
description: "Use when implementing or changing frontend pages, components, forms, client state, or UI behavior within an existing application."
---
# Frontend implementation

## Inputs
Repository, task/acceptance criteria, design/tokens, API contracts, and states.

## Procedure
1. Find the owning components, hooks, tokens, routes, forms, and client state.
2. Plan the smallest diff and the owner of new logic; reuse rendering, fetching, and formatters with matching semantics.
3. Separate presentation and data fetching; respect client/server boundaries and input validation.
4. Use semantic colors, responsive layout, keyboard/focus support, existing locale conventions, and loading/empty/error states applicable to the changed behavior. If transitions/gestures change, use relevant [MOT rules](../unified-development-standard/references/28-MOTION-DESIGN.md): real state owns results; support interruption/reversal, lifecycle cleanup, reduced motion and fallback. Do not add animation for a static edit.
5. Keep server secrets and trusted authorization enforcement on the server. A client-only tool does not require a new backend unless the task needs trusted operations.
6. Update relevant tests according to risk: unit, integration, e2e, accessibility, and visual regression where infrastructure exists.
7. Run available lint/type/build/test commands as relevant and report actual results.

## Output and verification
Provide changed files, reused components, affected UI states, real verification, and known limitations. Do not silently alter API contracts or claim UX readiness without checking relevant states. Supported themes/locales define coverage; this profile does not mandate new ones.
## Core rules
Use the sibling [core workflow](../unified-development-standard/SKILL.md) once per context; reuse it if already read. Then read only relevant sections of: 08-FRONTEND, 09-DESIGN-SYSTEM, 10-ACCESSIBILITY. Apply core 00-GOVERNANCE scope. Do not recursively rediscover profiles/core or load the full corpus for a local edit. If core is unavailable, report that limitation without claiming compliance with unread rules.

