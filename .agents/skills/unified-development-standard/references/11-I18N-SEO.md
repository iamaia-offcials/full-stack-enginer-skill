# 11. Internationalization, localization, SEO, and content

- `[I18N-001] MUST` When localization is required or a future need is justified, use one message/translation source; do not copy the same translation into unrelated locations. Do not impose an i18n framework on a single-language site without that need.
- `[I18N-002] MUST` Format dates, times, prices, numbers, and units for the locale and time zone. Translation must not alter the authoritative business amount.
- `[I18N-003] MUST` Account for Unicode and normalization in user input/search. Add case folding, transliteration, diacritic handling, or typo tolerance only when needed, controlling false matches.
- `[I18N-004] MUST` Test UI with long strings, supported RTL layouts, varying text formats, and missing translations where localization exists. Define predictable fallbacks.
- `[I18N-005] MUST` For indexable public sites, provide correct semantics, canonical URLs, sitemap/robots as needed, indexability checks, hreflang for localized equivalents, and valid metadata.
- `[I18N-006] MUST` Prevent indexing of personal/private pages; keep private APIs and tokens out of search-engine caches.
- `[I18N-007] SHOULD` Choose SSR/SSG/ISR according to SEO and content freshness needs. Meta tags do not compensate for poor structure, performance, or missing content.
- `[I18N-008] SHOULD` Document the content model, translation ownership, keys, missing-key failure/fallback policy, and editorial review of important pages.
- `[I18N-009] MUST` Language switching preserves transactional state and navigation, and correctly encodes localized URLs.

## Verification
For each supported locale, check routes, metadata, language switching, currency/date formatting, accessibility, long text, canonical/hreflang, and RTL where supported.

## Technical SEO for indexable web pages (supplements I18N-005–007)
- `[SEO-001] MUST` Before optimizing, map indexable URLs and exclude private/personal routes. Technical SEO does not apply to private APIs or non-indexable Mini App screens.
- `[SEO-002] MUST` An indexable route returns correct HTTP statuses and primary content accessible to crawlers. Fix soft 404s and errors disguised as `200` responses.
- `[SEO-003] MUST` Generate `title`, `meta description`, canonical, and robots directives from one route/content source of truth, with no contradictions between server HTML and client state.
- `[SEO-004] MUST` Do not treat `robots.txt` as a security control. Protect private content with authorization and appropriate HTTP controls.
- `[SEO-005] MUST` Sitemaps contain only current target canonical URLs, excluding 3xx/4xx/5xx/`noindex` URLs and duplicates. Synchronize updates with content.
- `[SEO-006] MUST` For multilingual content, keep `hreflang` consistent across existing indexable equivalents; construct correct language/locale URLs and avoid unsuitable canonical/redirect targets.
- `[SEO-007] SHOULD` Use valid structured data only when the search platform supports its type and it describes content actually visible to users. Do not promise rich results.
- `[SEO-008] MUST` Important internal links use ordinary `href` attributes and point to canonical routes. Verify server-rendered/prerendered content in HTML and/or through a real crawler, not solely in a developer's browser.
- `[SEO-009] MUST` URL/domain migrations include redirect mappings, canonical/hreflang/sitemap checks, 404 monitoring, and a plan for indexing consequences.
- `[SEO-010] SHOULD` Record observed SEO evidence: sampled URLs, requests, returned HTTP/HTML, and logs/Search Console data when available. Local linting does not prove indexing.
- `[SEO-011] MUST` SEO must preserve UX and accessibility. Do not covertly serve materially different content to crawlers and real users (cloaking).

For planning SEO, measurement, and integrations, see [SEO and analytics](../guides/SEO-ANALYTICS-PLANNING.md).
