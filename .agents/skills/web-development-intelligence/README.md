# Web Development Intelligence Agent Skill

> Universal Agent Skill for end-to-end commercial web development, design engineering, and architectural intelligence. Compatible with the [Agent Skills Standard](https://agentskills.io/specification).

---

## 1. Overview & Core Philosophy

Small businesses and modern engineering teams frequently face a common bottleneck: **they lack a dedicated senior web designer**. When an AI is asked to build a web page or application, it often generates generic, cookie-cutter templates ("AI slop") — standard 3-column feature grids, centered purple buttons, raw generic colors, and unconsidered spacing — requiring developers to micro-manage every padding, font size, and layout decision.

**Web Development Intelligence** solves this problem by embedding deep, autonomous design-engineering intelligence directly into the AI agent. The agent makes professional, context-driven aesthetic, UX, and architectural decisions automatically while respecting existing codebases and design systems.

### Core Tenet: Design, Don't Assemble
The agent does **not** blindly copy-paste components (`"find card -> paste card -> find button -> paste button"`). Instead, it follows a 9-stage engineering workflow:
1. **Understand Business Intent & Audience**
2. **Information Architecture & User Journeys**
3. **Reference Research & Competitive Analysis**
4. **Design Direction & Token Hierarchy**
5. **UI/UX Composition (Desktop, Tablet, Mobile)**
6. **Motion Choreography & Spring Physics**
7. **Production Implementation (Accessible, Semantic, Performant)**
8. **Automated & Visual Quality Assurance**
9. **Refinement & Hardening**

---

## 2. Directory Architecture & Progressive Disclosure

The skill is engineered with a strict **Progressive Disclosure** architecture. The root `SKILL.md` is compact (< 500 lines) and acts as an executive controller. Detailed domain competencies are loaded on-demand from dedicated modular subdirectories:

```
web-development-intelligence/
├── SKILL.md                          # Executive orchestrator & routing manifest
├── README.md                         # Suite documentation & usage manual
├── references/                       # Domain engineering standards
│   ├── website-strategy.md           # Business goals, KPIs, conversion funnels
│   ├── information-architecture.md   # Site structures, mental models, navigation
│   ├── ux-design.md                  # Heuristics, cognitive load, interaction design
│   ├── ui-design.md                  # Controls, forms, states, affordances
│   ├── visual-design.md              # Typographic scales, optical alignment, colors
│   ├── design-systems.md             # Token architectures, Radix/shadcn foundations
│   ├── content-design.md             # UX writing, active CTAs, microcopy, error states
│   ├── responsive-design.md          # Multi-device layouts, fluid typography, iOS fixes
│   ├── motion-design.md              # Spring physics, choreographies, reduced-motion
│   ├── scroll-interactions.md        # GSAP ScrollTrigger, pinned reveals, scrollytelling
│   ├── frontend.md                   # Semantic HTML5, CSS/Tailwind, hydration, Next/Vite
│   ├── backend.md                    # REST/GraphQL, server actions, validations (Zod)
│   ├── seo.md                        # Meta tags, OpenGraph, JSON-LD Schema.org, sitemaps
│   ├── accessibility.md              # WCAG 2.2 AA/AAA, ARIA patterns, focus management
│   ├── performance.md                # Core Web Vitals (LCP, INP, CLS), bundles, lazy-load
│   └── security.md                   # OWASP Top 10, CSP, CSRF, sanitized inputs
├── design-intelligence/              # High-taste design heuristics & rules
│   ├── design-principles.md          # 10 core principles (Hierarchy, contrast, restraint)
│   ├── composition-patterns.md       # Asymmetric, editorial, bento, split, layered grids
│   ├── section-patterns.md           # Hero, pricing, feature, testimonial, CTA patterns
│   ├── ux-patterns.md                # Multi-step forms, search filters, modal drawers
│   ├── industry-patterns.md          # Sector-specific rules (Restaurant, B2B, Real Estate...)
│   ├── motion-patterns.md            # Entrances, cards, hover, pin-scroll, parallax
│   ├── responsive-patterns.md        # Mobile unpinning, drawer fallbacks, touch targets
│   └── design-anti-patterns.md       # 62 Anti-Slop / AI-tell rules & prevention guide
├── libraries/                        # Component registries, MCP configs & catalogs
│   ├── sources.json                  # Source library metadata (Aceternity, Magic UI, etc.)
│   ├── components.json               # Indexed production components with registry URLs
│   ├── animations.json               # Indexed GSAP & Motion animation patterns
│   ├── layouts.json                  # Curated responsive layout archetypes
│   ├── websites.json                 # Curated live design case studies & benchmarks
│   └── registry-config.md            # MCP integration specs & Open Registry installation
├── case-studies/                     # Detailed real-world sector case studies
│   ├── restaurants.md                # Menu-first, reservation funnels, ambience
│   ├── ecommerce.md                  # High-intent catalogs, trust badges, checkout
│   ├── real-estate.md                # Lead-generation without catalog, valuation funnels
│   ├── tourism.md                    # Cinematic parallax, experiential storytelling
│   ├── catalogs.md                   # B2B wholesale, RFQ, spec sheets, bulk orders
│   ├── esim.md                       # Destination search, bundle comparison, zero-confusion
│   └── corporate-websites.md         # B2B credibility, case studies, enterprise compliance
├── workflows/                        # Step-by-step operational workflows
│   ├── new-project.md                # 9-stage complete project lifecycle
│   ├── existing-project.md           # Respecting existing tokens & incremental adoption
│   ├── redesign.md                   # Visual audit, heuristic evaluation, modernisation
│   ├── new-page.md                   # Adding pages to existing design systems
│   ├── component-development.md      # Atomic component design & accessible states
│   ├── motion-development.md         # Motion choreography & performance budgeting
│   ├── design-review.md              # 10-point visual design review rubric
│   └── quality-assurance.md          # Cross-browser, responsive & technical audit
├── scripts/                          # Automated tooling & validation CLI
│   ├── search-references.mjs         # Multi-criteria catalog search utility
│   ├── validate-catalog.mjs          # JSON schema & link integrity validator
│   ├── validate-design.mjs           # Automated code scanner for design anti-patterns
│   └── update-references.mjs         # Knowledge ingestion & catalog updater
└── tests/                            # Comprehensive validation suite
    └── test_scenarios.mjs            # Tests for Scenarios A, B, C, D, E
```

---

## 3. Operational Modes

The skill automatically adapts its execution depth to the scale of the request:

| Mode | Trigger Criteria | Scope & Workflow |
| :--- | :--- | :--- |
| **`quick`** | Minor bugfixes, single component tweaks, simple CSS styling, adding a basic modal animation | Skips deep research and IA; executes directly using existing design tokens; validates locally. |
| **`standard`** | Creating a new section, building a dedicated page, integrating a complex interactive component | Formulates page IA, inspects relevant reference patterns, applies responsive composition, verifies cross-device behavior. |
| **`comprehensive`** | Building a new web application, complete site redesign, implementing full motion story | Full 9-stage lifecycle: strategy, IA, reference research, token architecture, UI/UX, motion, development, QA audit. |

---

## 4. Connected Component & Motion Libraries

All component libraries conform to the **Open Registry Standard** (`components.json`), installable directly into modern React/Next.js/Vite projects via `npx shadcn@latest add <registry-url>`:

| Library | Focus & Specialty | License / Access |
| :--- | :--- | :--- |
| **[shadcn/ui](https://ui.shadcn.com/)** | Accessible core primitives, Radix UI foundations, forms, tables, dialogs, drawers | MIT (Free) |
| **[Aceternity UI](https://ui.aceternity.com/)** | Hero sections, 3D cards, sticky scroll reveal, parallax, animated backgrounds | MIT / Free tier |
| **[Magic UI](https://magicui.design/)** | High-conversion marketing UI, animated borders, marquee, dock, bento grids | MIT (Free core) |
| **[React Bits](https://reactbits.dev/)** | Text animations, WebGL canvas effects, interactive cursor particles, creative cards | MIT (Free) |
| **[Motion Primitives](https://motion-primitives.com/)** | Gestures, smooth accordion expansions, animated dialogs, subtle micro-interactions | MIT (Free) |
| **[GSAP 3](https://gsap.com/)** | ScrollTrigger, timelines, pinned scrollytelling, horizontal scroll reels, Flip plugin | Standard GreenSock License |
| **[Motion](https://motion.dev/)** | Spring physics, layout animations, exit transitions (`AnimatePresence`) | MIT (Free) |
| **[Codrops](https://tympanus.net/codrops/)** | Experimental interactions, WebGL shaders, creative page transitions | Reference / Open source |
| **[Three.js](https://threejs.org/)** | WebGL 3D scenes, 3D product configurations (used selectively when justified) | MIT (Free) |

---

## 5. MCP (Model Context Protocol) Integration

The skill is built to interface directly with MCP servers when active in the client environment:

### `shadcn` MCP Server
```json
{
  "mcpServers": {
    "shadcn": {
      "command": "npx",
      "args": ["-y", "shadcn@latest", "mcp"]
    }
  }
}
```
*Capabilities:* Automated component discovery, installation, and dependency resolution.

### `Magic UI` MCP Server
```json
{
  "mcpServers": {
    "magicui": {
      "command": "npx",
      "args": ["-y", "@magicuidesign/mcp@latest"]
    }
  }
}
```
*Capabilities:* Instant marketing component injection and configuration.

### `Playwright` / Chrome DevTools MCP
When available, the agent uses automated browser tooling to inspect live demos, verify scroll triggers, take multi-viewport screenshots (360px, 390px, 768px, 1024px, 1440px), and validate Core Web Vitals.

---

## 6. CLI Tooling & Scripts

The skill includes 4 standalone Node.js utilities in `scripts/`:

### 1. Reference Search Utility
```bash
# Search by category
node scripts/search-references.mjs --category hero

# Multi-criteria search
node scripts/search-references.mjs --industry tourism --complexity medium

# Free-text keyword query
node scripts/search-references.mjs --query "sticky scroll"
```

### 2. Catalog Integrity Validator
```bash
node scripts/validate-catalog.mjs
```
Checks JSON syntax, required fields, and URL structures across all libraries.

### 3. Design Anti-Pattern Scanner
```bash
node scripts/validate-design.mjs src/components
```
Detects AI-tells: generic colors (`#3b82f6`), missing `min-width: 0`, iOS Safari font size zoom hazards (`font-size < 16px`), missing `prefers-reduced-motion`, and unbounded scroll pins.

### 4. Knowledge Ingestion Updater
```bash
node scripts/update-references.mjs --type component --file path/to/new-entry.json
```
Enables continuous knowledge accumulation as new patterns and components are validated.

---

## 7. Anti-Slop / Design Heuristics (Extract)

The agent strictly enforces **62 Anti-Slop Rules** documented in `design-intelligence/design-anti-patterns.md`:
1. **No Generic Colors**: Never use default raw blues (`#0000ff`, `#3b82f6`) or harsh black text on pure white. Use tailored HSL scales with warm or cool tinted darks.
2. **No Monotonous Centered Layouts**: Break the `Centered Title -> Centered Subtitle -> 3 Centered Cards` monotony using asymmetric editorial grids, bento hierarchies, or split columns.
3. **No Unpinned Mobile Traps**: Any pinned desktop scroll experience (`ScrollTrigger`) must unpin below 768px into natural vertical flow.
4. **Mobile Input 16px Floor**: Never render inputs below 16px on mobile to prevent iOS Safari auto-zoom from breaking viewport framing.
5. **Spring Physics Over Linear Transitions**: Never use linear or abrupt easing on interactive UI elements. Use high-tension damped springs (`damping: 24, stiffness: 260`).
6. **Accessible Motion**: Always wrap continuous or large-scale motion in `@media (prefers-reduced-motion: reduce)`.

---

## 8. License & Standard Compliance

- Conforms strictly to the [Agent Skills Standard v1.0](https://agentskills.io/specification).
- Released under the MIT License.
