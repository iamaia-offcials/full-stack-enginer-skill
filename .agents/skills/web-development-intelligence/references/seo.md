# Technical Search Engine Optimization (SEO)

Ensure indexable public routes are fully discovered, parsed, and understood by search engine crawlers.

## SEO Checklist & Implementation

1. **Rendering & Indexability:**
   - Public pages intended for organic search must deliver semantic HTML directly in the initial server response (SSR or SSG). Do not hide indexable text behind client-side JavaScript execution.
2. **Metadata & Open Graph:**
   - Unique, descriptive `<title>` tag (50–60 characters).
   - Compelling `<meta name="description">` (120–155 characters).
   - Complete Open Graph tags (`og:title`, `og:description`, `og:image`, `og:url`) with 1200x630px high-resolution preview images.
3. **Structured Data (JSON-LD):**
   - Implement Schema.org structured data: `Organization`, `WebSite`, `Product`, `LocalBusiness`, `FAQPage`, or `Article`.
4. **Canonical & Internationalization:**
   - Explicit `<link rel="canonical">` to prevent duplicate content penalties.
   - Proper `hreflang` attributes on localized public domains.
