# 27. Code-first website and web application engineering

**Scope:** public websites, web applications, catalogs, dashboards, PWAs, and Mini Apps. Native Android/iOS specifics are in `23-MOBILE-PLATFORM.md`. SEO applies only to routes intended for indexing.

- `[WEB-001] MUST` For each affected route, define purpose, access level, expected HTTP status, rendering strategy, and cache/privacy policy. Do not mechanically apply one strategy everywhere.
- `[WEB-002] MUST` Keep server secrets and privileged keys out of client bundles, HTML, browser storage, and telemetry. Distinguish public client IDs and user-session tokens from server secrets; choose session storage/lifecycle for the protocol and threat model, including XSS/CSRF.
- `[WEB-003] MUST` Mobile-first and desktop layouts share domain behavior and design tokens. Layout differences do not justify copied business logic or API clients.
- `[WEB-004] MUST` Critical routes support deep links, back/forward, reload, direct navigation, and correct `404` and `401/403` handling under the existing security model.
- `[WEB-005] MUST` Forms have accessible labels, clear validation, and error handling. When sending data to a trusted service, the server independently validates it and checks permissions/replays. Do not create a backend for a local client-only tool without need.
- `[WEB-006] SHOULD` Use feature detection and progressive enhancement for target browsers. Add heavy polyfills only for supported traffic or explicit requirements.
- `[WEB-007] MUST` Mobile layouts account for available viewport space, safe areas, software keyboards, zoom/reflow, orientation, touch, and long strings in supported locales.
- `[WEB-008] SHOULD` Add PWA/offline support, push, and service workers only for user needs, with controls for stale assets, private-data caching, and safe updates.
- `[WEB-009] MUST` When changing SSR/SSG/ISR/CSR, check indexability, personalized caching, data freshness, and error statuses using the current framework version's APIs.
- `[WEB-010] MUST` Before release, verify the production build and smoke critical flows at mobile and desktop widths. State the browsers actually tested.
- `[WEB-011] SHOULD` Use shared UI primitives for important components. Variants express meaning rather than dozens of independent boolean switches.
- `[WEB-012] SHOULD` For unreliable networks, use abort/timeouts/bounded retries and explicit recoverable states instead of endless spinners or uncontrolled polling.

## Notes
- Responsive design uses structure, components, states, and checks appropriate to available space; it does not imply a separate mobile-browser project.
- Choose rendering per route: public pages may need accessible HTML, while private dashboards have different requirements.
- Define compatibility and browser support in `PROJECT_PROFILE.md`; do not invent a promise to support every browser.

For early SEO, measurement, and integration planning, see [SEO and analytics](../guides/SEO-ANALYTICS-PLANNING.md).
