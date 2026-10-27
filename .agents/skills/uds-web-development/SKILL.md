---
name: uds-web-development
description: "Use when building or maintaining website or web-application routes, pages, forms, browser behavior, rendering, responsive layouts, or required PWA and Mini App features."
---
# Code-first web engineering

## Scope and inputs
Web and mobile-browser layouts share architecture and components; separate applications need a demonstrated reason. Distinguish mobile web from native Android/iOS. Inputs include repository/routes, target browsers/devices, project profile, indexing, authentication, supported locales, content, design tokens, and API requirements.

## Procedure
1. Identify public indexable site, private dashboard, Mini App, or PWA; separate SEO, offline, authentication, and mobile constraints.
2. Inspect owning routes/layouts, shared UI/hooks, server functions, networking, HTTP caching, and tokens. Reuse equivalent behavior.
3. Choose rendering per affected route (SSG/SSR/CSR, caching/dynamic behavior) using the installed framework's supported APIs. Interactivity alone does not require the entire system to use CSR.
4. Design responsive/mobile-first layouts for content width, keyboard, orientation, safe areas, touch, reduced motion, text scaling, and long strings in supported locales.
5. Handle applicable error/empty/loading/partial/retry states with semantic structure, labels, and focus. Keep server secrets and trusted authorization on the trusted side; local-only tools do not automatically need a backend.
6. During site planning, establish organic-search intent and future analytics/pixels. Record uncertainty before consequential decisions. Apply SEO early to indexable pages and N/A to private routes. Read core `guides/SEO-ANALYTICS-PLANNING.md` when relevant and available; configure providers only within the task.
7. Minimize client JavaScript, waterfalls, layout shifts, and incompatible APIs; use progressive enhancement/feature detection where appropriate.
8. Verify target browsers/devices and the production build. Run relevant unit/integration/e2e checks for risky scenarios and report environment limits.

## Output and verification
Provide a minimal diff, relevant route/render decisions, reused components, actual browser/responsive checks, command results, and open risks. Verify shared business behavior, HTTP statuses, keyboard/touch, key routes, console errors in tested scenarios, and documented browser support. New themes, locales, offline capability, or analytics are not automatic requirements.
## Core rules
Use the sibling [core workflow](../unified-development-standard/SKILL.md) once per context; reuse it if already read. Then read only relevant sections of: 08-FRONTEND, 09-DESIGN-SYSTEM, 10-ACCESSIBILITY, 11-I18N-SEO (when applicable), 27-WEB-ENGINEERING. Apply core 00-GOVERNANCE scope. Do not recursively rediscover profiles/core or load the full corpus for a local edit. If core is unavailable, report that limitation without claiming compliance with unread rules.

