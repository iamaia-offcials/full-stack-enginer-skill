# 08. Frontend and interface architecture

- `[FE-001] MUST` Separate routes/layouts, presentation, server/client state, fetching, DTO construction, and domain rules. Do not make the UI a second backend.
- `[FE-002] MUST` Reuse UI components and patterns: **one canonical component per shared purpose**, with explicit variants/props rather than page-specific clones.
- `[FE-003] MUST` Handle loading, empty, ready, partial, error, and offline/degraded states for each screen scenario where applicable. Error boundaries do not replace scenario-level error handling.
- `[FE-004] MUST` A trusted authority enforces protected actions, permissions, prices, and server-side business invariants. Client checks improve UX and do not replace authorization. Local/offline calculations are valid within an explicitly defined trust boundary.
- `[FE-005] SHOULD` Centralize the network client, error handling, caching/invalidation, and retry policy. Do not create an HTTP client for each component.
- `[FE-006] MUST` Verify responsive behavior against real widths and content: mobile, tablet, desktop, zoom, landscape, safe areas, and long translations where supported.
- `[FE-007] MUST` Preserve keyboard access, focus, semantic HTML, labels, form errors, and reading order throughout interactions.
- `[FE-008] SHOULD` Avoid uncontrolled effects, listeners, and duplicate subscriptions. Cancel/clean up resources and prevent asynchronous fetch races.
- `[FE-009] SHOULD` Choose SSR/SSG/CSR based on need, SEO, personal data, and latency. Do not default to an entirely client-rendered application without analysis.
- `[FE-010] MUST` Review payload/JavaScript size, images, rendering, and routes before performance-sensitive changes.

## Composition principle
`Page → layout + feature components → shared UI primitives`. `features/catalog/` can own catalog state; `components/ui/` knows nothing about pricing plans or orders.

## Acceptable repetition
Semantically different cards may compose shared primitives. Avoid a universal component with dozens of boolean props.

For practical patterns, read the relevant section of [decision formulas](../guides/PRACTICAL-FORMULAS.md).
