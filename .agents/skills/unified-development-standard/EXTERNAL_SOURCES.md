# Primary sources and applicability limits

This is a source catalog, not a copy of the specifications or a claim that every URL has been checked. Verify current supported versions and applicability when implementing a specific change.

| Topic | Source | Scope |
|---|---|---|
| Skill format | https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx | Skill file format specification |
| Apple UI and materials | https://developer.apple.com/design/human-interface-guidelines/materials | Platform HIG and materials for controls/navigation |
| Google Material | https://m3.material.io/ | Design system and adaptive interfaces |
| Microsoft Fluent 2 | https://fluent2.microsoft.design/ | Design system and tokens |
| WCAG 2.2 | https://www.w3.org/TR/WCAG22/ | Testable accessibility standard |
| OWASP ASVS | https://asvs.owasp.org/ | Security verification; check the applicable stable version |
| GitHub Rulesets | https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets | Branch protection and checks |
| GitHub Actions Security | https://docs.github.com/en/code-security/tutorials/secure-your-organization/protect-against-threats | Least privilege and action commit pinning |
| Docker Builds | https://docs.docker.com/build/building/best-practices/ | Image build practices |
| Docker Compose | https://docs.docker.com/compose/how-tos/startup-order/ | Startup readiness |
| Podman Quadlet | https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html | systemd units |
| Podman Compose | https://docs.podman.io/en/latest/markdown/podman-compose.1.html | External Compose provider |
| OpenTelemetry | https://opentelemetry.io/docs/concepts/signals/ | Traces, metrics, and logs |
| Conventional Commits | https://www.conventionalcommits.org/en/v1.0.0/ | Commit message convention |
| SemVer | https://semver.org/ | Public API/package versioning |
| RFC 9457 | https://www.rfc-editor.org/rfc/rfc9457 | HTTP Problem Details |

Minimal/Standard/Critical profiles, a single deployment owner per target, and the suite's duplication rules are **internal engineering policies**, not universal requirements endorsed by Apple, Google, Docker, or GitHub. Use primary sources for the specific practices they document; they do not validate every custom rule or formula here.

## Specialist documentation

| Topic | Source | Purpose |
|---|---|---|
| Google Search SEO | https://developers.google.com/search/docs/fundamentals/seo-starter-guide | Crawling, indexing, and SEO scope; no ranking guarantee |
| JavaScript SEO | https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics | HTML, rendering, and indexability |
| Core Web Vitals | https://web.dev/articles/vitals | LCP/INP/CLS and field p75 |
| Next.js App Router | https://nextjs.org/docs/app | Verify routes, caching, and rendering APIs for the selected stable version |
| Android performance | https://developer.android.com/topic/performance/overview | Startup, jank, memory, and battery |
| Android Baseline Profiles | https://developer.android.com/topic/performance/baselineprofiles/overview | Android performance profiles |
| Apple performance | https://developer.apple.com/documentation/xcode/improving-your-app-s-performance | Profiling and measurement |
| GitHub dependencies | https://docs.github.com/en/code-security/dependabot | Updates and security alerts |

These URLs are starting points. Recheck relevant versions and behavior before a concrete code change.
