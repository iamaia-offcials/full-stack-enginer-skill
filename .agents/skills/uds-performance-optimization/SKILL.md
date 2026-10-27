---
name: uds-performance-optimization
description: "Use when a website, mobile app, backend, or database has a measurable speed, latency, CPU, memory, energy, load, or performance-budget problem."
---
# Evidence-based performance optimization

## Scope and inputs
Optimization needs a symptom, goal, or budget, not merely a technical task. Inputs include affected route/operation, user symptom, project profile, load/devices, available logs/metrics, and a safe profiling environment.

## Procedure
1. Select task-relevant success metrics and a reproduction scenario: CWV p75, TTFB, bundle KiB, API p95, query count, memory, battery, or startup.
2. Record baseline conditions: hardware/network, cold/warm cache, release/development mode, and sample size.
3. Form hypotheses from profiler/trace/EXPLAIN/waterfall/heap evidence; rank bottlenecks by impact.
4. For web, inspect server waterfalls, render critical path, images/fonts, hydration, blocking tasks, layout shifts, cache/invalidation, and offscreen work as relevant.
5. For backend/data, inspect N+1, query-plan-based indexes, pooling, timeouts, backpressure, and batching. Caches need TTL/invalidation and personal-data protection.
6. For mobile, inspect startup, frame jank, main-thread work, memory, wakeups/network/battery, and resource size with platform-appropriate tools.
7. Change one bottleneck per iteration while preserving behavior, consistency, security, and accessibility.
8. Repeat comparable measurements; check correctness, errors, and relevant regressions. State uncertainty explicitly.
9. Record metrics, commands, profiles, and trade-offs. One Lighthouse run is not field p75 or a guarantee for all users.

## Output and verification
Update the existing performance report or use PERFORMANCE_AUDIT.md when appropriate. Include bottleneck → change → comparable measurements, diff, regression evidence, and affected budget. Completion requires a baseline, evidence-supported hypothesis, comparable after measurement, working functionality, and stated measurement limits.
## Core rules
Use the sibling [core workflow](../unified-development-standard/SKILL.md) once per context; reuse it if already read. Then read only relevant sections of: 17-PERFORMANCE. Apply core 00-GOVERNANCE scope. Do not recursively rediscover profiles/core or load the full corpus for a local edit. If core is unavailable, report that limitation without claiming compliance with unread rules.

