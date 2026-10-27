---
name: uds-technical-seo
description: "Use when launching, migrating, localizing, or auditing public web pages intended for search indexing, or investigating crawlability, indexability, metadata, structured data, or SEO regressions."
---
# Technical SEO for web

## Scope and inputs
Use for public websites intended to receive organic search traffic. Private applications, Mini Apps without public pages, internal dashboards, and APIs usually have no indexing requirement. Do not guarantee rankings, indexing, or traffic.

For new-site planning, assess SEO before choosing routes, rendering, and CMS. Distinguish technical foundations from promotion; use core `guides/SEO-ANALYTICS-PLANNING.md` when relevant and available.

Inputs include domain/base URL, indexable/private routes, supported locales, rendering, robots/sitemap, redirects, and available production/staging/Search Console access.

## Procedure
1. Inventory relevant URLs: indexing intent, 200/3xx/4xx/5xx statuses, trailing slashes/parameters, pagination, and filters.
2. Inspect server-response HTML and bot access to main content. If client JavaScript supplies critical indexable content, verify rendering rather than assuming it works.
3. Audit unique titles, descriptions (possible snippets, not ranking guarantees), headings, internal links with `href`, descriptive anchors, and meaningful image alt text.
4. Check canonical consistency, redirect chains, soft 404s, duplicates, robots.txt, and robots meta/X-Robots-Tag. Robots.txt does not secure confidential URLs.
5. Include only intended canonical indexable URLs in sitemaps, generated from one source of truth. A sitemap does not guarantee indexing.
6. For multilingual sites, verify separate URLs, `lang`, reciprocal `hreflang`/`x-default` where appropriate, and genuine localized-content quality.
7. Use supported structured-data types matching visible content; validate with official tools and do not promise rich results.
8. Check mobile rendering and field p75 LCP/INP/CLS, separating mobile/desktop where available. Lab measurements diagnose issues; they do not prove field performance.
9. For migrations, map URLs and appropriate 301/308 redirects, update canonicals/sitemaps/hreflang, and run regression checks.
10. Record pages/sample, commands, and results. Without index evidence such as Search Console, local HTML alone cannot establish actual index status.

## Output and verification
Update the existing SEO report or use SEO_AUDIT.md when appropriate. Provide URL inventory, evidence-backed findings, authorized source fixes, regression plan, and applicable Search Console follow-up. Target public pages must be render-accessible and not unintentionally blocked, metadata directives consistent, routing functional, and measurement sources explicit. Audits remain read-only unless fixes are authorized.
## Core rules
Use the sibling [core workflow](../unified-development-standard/SKILL.md) once per context; reuse it if already read. Then read only relevant sections of: 11-I18N-SEO, 17-PERFORMANCE, 27-WEB-ENGINEERING. Apply core 00-GOVERNANCE scope. Do not recursively rediscover profiles/core or load the full corpus for a local edit. If core is unavailable, report that limitation without claiming compliance with unread rules.

