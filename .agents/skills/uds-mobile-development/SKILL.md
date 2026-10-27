---
name: uds-mobile-development
description: "Use when the main task concerns Android/iOS, cross-platform apps, mobile web, or PWA behavior, including lifecycle, connectivity, permissions, device compatibility, and mobile performance."
---
# Mobile application engineering

## Scope and inputs
Distinguish native/cross-platform apps from PWA, Telegram Mini Apps, and mobile web; apply only the relevant platform branch. A simple desktop CSS edit does not need this workflow. Inputs include target OS/device matrix, client architecture/runtime, backend contracts and old-client support, distribution requirements, permissions, and connectivity UX.

## Procedure
1. Identify native, cross-platform, PWA, Mini App, or mobile-web mode; omit store gates unless distribution uses a store.
2. Inspect existing navigation, state, domain/use cases, networking, secure storage, OS adapters, and tests. Reuse business rules and keep backend secrets out of clients.
3. Check touch targets, safe areas, software keyboard, scroll/zoom, dynamic type, landscape, supported themes, and accessibility; keep system APIs behind an appropriate shared adapter.
4. Handle foreground/background lifecycle, interrupted networking, applicable offline-cache TTL, idempotent retries, and preservation of critical input across restart.
5. Verify permissions, deep links, notifications, push-token lifecycle, and privacy only for features actually used.
6. Check backend compatibility with supported old clients, additive changes/deprecation windows, contract tests, and applicable beta/staging channels.
7. Profile cold/warm start, responsiveness, scrolling, memory/battery, and networking on physical devices when available. Consider Android Baseline Profiles or iOS Instruments under current official guidance for the matching platform.
8. For distributed native/cross-platform builds, check signing, provisioning, store policy/metadata where applicable, crash monitoring, and staged rollout. For mobile web/PWA, check HTTPS and responsive behavior; installation/offline support only when needed.
9. Run applicable tests/build/device checks; identify untested devices and environment limits.

## Output and verification
Provide relevant OS/device support and UX states, test evidence, performance baseline when profiling, and a platform-specific release checklist. Check critical input, recoverability, credential storage, and API compatibility. Do not equate emulator evidence with physical-device verification or impose app-store gates on ordinary web delivery.
## Core rules
Use the sibling [core workflow](../unified-development-standard/SKILL.md) once per context; reuse it if already read. Then read only relevant sections of: 23-MOBILE-PLATFORM, 07-SECURITY-PRIVACY. Apply core 00-GOVERNANCE scope. Do not recursively rediscover profiles/core or load the full corpus for a local edit. If core is unavailable, report that limitation without claiming compliance with unread rules.

