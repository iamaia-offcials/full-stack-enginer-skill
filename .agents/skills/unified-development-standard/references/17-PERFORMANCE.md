# 17. Performance, reliability, resources, and scaling

- `[PERF-001] MUST` Define user and technical goals before optimizing; measure a baseline and repeat measurements after the change.
- `[PERF-002] MUST` For public websites, check current Core Web Vitals (LCP, INP, CLS) and critical-screen performance. Verify thresholds in current documentation rather than embedding permanent numeric limits.
- `[PERF-003] SHOULD` Optimize heavy images, fonts, code splitting, HTTP caching, client-state work, and network waterfalls. A skeleton loader alone does not fix slow-response UX.
- `[PERF-004] MUST` For backends, bound inputs, request duration, expensive operations, connection pools, and concurrency. Set timeouts on all external interactions.
- `[PERF-005] SHOULD` Define cache TTL/invalidation, acceptable staleness, and protection for personalized data. **A cache is not the source of truth**.
- `[PERF-006] SHOULD` Before scaling horizontally, optimize queries/indexes and run load/soak tests using actual scenarios.
- `[PERF-007] MUST` Handle overload and partial failure for important operations: rate limits/backpressure, graceful degradation, queue policies, and circuit breakers where needed.
- `[PERF-008] SHOULD` Introduce SLOs/error budgets when live traffic and measurement are available. Distinguish contractual SLAs from internal SLOs.

## Performance budget
Record relevant metrics in `PROJECT_PROFILE.md`: mobile web UX, p95 API latency, error rate, bundle budget, image sizes, and database query time. Select values for the audience, devices, and workload; irrelevant metrics are N/A.

## Measurable profiling and regressions
- `[OPT-001] MUST` Every performance change has a metric, reproduction scenario, and baseline with recorded conditions (device type, network, cold/warm cache, release build).
- `[OPT-002] MUST` Obtain bottleneck evidence before changing code: trace, waterfall, SQL execution plan, CPU/heap profile, or another relevant source. Label guesses as hypotheses.
- `[OPT-003] MUST` Distinguish Lighthouse lab data from field/RUM data. Evaluate field LCP, INP, and CLS using the current p75 method, separating mobile/desktop where data exists.
- `[OPT-004] SHOULD` Set scenario-specific budgets for bundles, images, third-party scripts, p95 API latency, database queries, and app startup; record thresholds in the project profile.
- `[OPT-005] MUST` Compare equivalent before/after conditions. One random run does not prove improvement for the entire audience.
- `[OPT-006] MUST` Optimization must preserve authorization, consistency, functionality, and accessibility. Test changed scenarios.
- `[OPT-007] SHOULD` Rank issues by user impact, frequency, and cost to fix. Do not replace profiling with an uninformed architecture rewrite.
- `[OPT-008] SHOULD` For mobile clients, separately measure startup, frame jank, main-thread stalls, memory, and battery using official platform tools.
- `[OPT-009] MUST` Document the budget and post-release verification, especially for high-risk cache, query, and database-schema changes.
