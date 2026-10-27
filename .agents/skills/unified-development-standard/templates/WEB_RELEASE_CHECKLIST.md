# Web release checklist — [version/commit]

Profile: public website / dashboard / Mini App / PWA; target browsers/devices: ...
Adapt to the release and changed flows. Omit irrelevant checks or explain N/A; this template does not impose new release gates.

- [ ] Existing modules/components reused where appropriate; duplicate ownership checked.
- [ ] Production build and lockfile installation verified.
- [ ] Affected routes: direct navigation, back/forward, refresh, invalid URLs, HTTP statuses.
- [ ] Applicable authentication, server authorization, and secret-leak checks.
- [ ] Target devices: touch/keyboard/zoom, long translations, orientations.
- [ ] Supported themes, applicable loading/empty/error states, focus, semantic labels.
- [ ] Relevant performance target and measured evidence.
- [ ] SEO verified for indexable routes; N/A for private application routes.
- [ ] Required CI and relevant deployment/rollback evidence.

Checks: command / result / environment / NOT_RUN.
