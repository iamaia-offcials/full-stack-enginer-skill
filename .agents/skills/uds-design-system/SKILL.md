---
name: uds-design-system
description: "Use when designing or auditing UI in code, creating design tokens or shared components, or improving visual consistency, responsive behavior, accessibility, and supported themes."
---
# Code-first UX/UI and design systems

## Inputs
Existing repository/screenshots where available, CSS/components/tokens, requirements, visual references, target devices, and supported themes. External design-editor mockups are not a prerequisite.

## Procedure
1. Inspect components, shared styles, tokens, routes, and actual UI states. Respect an established visual system.
2. Define the relevant visual contract: typography, semantic colors, spacing, radius, elevation, motion, supported themes, and responsive behavior. For motion decisions, read only relevant [MOT rules](../unified-development-standard/references/28-MOTION-DESIGN.md) and the [decision guide](../unified-development-standard/guides/MOTION-DECISIONS.md) when needed; choose by task, repetition and spatial meaning, including no motion. Reuse an established pattern for simple cases.
3. Implement working UI in HTML/CSS/TSX/components. Use a local demonstration page or existing Storybook when useful.
4. Consolidate duplicated components/CSS values by shared meaning; avoid giant components combining unrelated cases.
5. Define affected states/variants, keyboard/focus, touch, accessibility, reduced motion, loading/empty/error, and long strings in supported locales.
6. For visual audits, use browser screenshots/visual regression where available. Without browser access, analyze code and mark visual checks NOT_RUN.
7. Measure actual color-pair contrast, including overlays/blur/images; check mobile sizes and supported themes.
8. Update existing component specifications/tokens and run relevant frontend checks.

## Output and verification
Provide changed components/shared styles, relevant token/variant/state documentation, actual screenshots/check results, and remaining inconsistencies. An audit alone stays read-only unless fixes are authorized.

Do not require design-editor subscriptions, graphic sources, or spreadsheets to build UI. A specifically requested external file format is separate authorized work. New themes or locales are added only when the task requires them.
## Core rules
Use the sibling [core workflow](../unified-development-standard/SKILL.md) once per context; reuse it if already read. Then read only relevant sections of: 08-FRONTEND, 09-DESIGN-SYSTEM, 10-ACCESSIBILITY. Apply core 00-GOVERNANCE scope. Do not recursively rediscover profiles/core or load the full corpus for a local edit. If core is unavailable, report that limitation without claiming compliance with unread rules.

