---
name: web-development-intelligence
description: "Use when planning, designing, building, auditing, or refining commercial websites and web applications across business strategy, UX/UI, visual craft, motion design, responsive layouts, frontend, and backend."
---

# Web Development Intelligence

A universal agent skill for professional commercial web design and engineering. It equips the agent to make autonomous, high-taste design and architectural decisions without requiring manual micro-management of every layout, button placement, card dimension, or animation curve.

## Operating Modes

Calibrate the scope of work automatically based on the user's task:

| Mode | Trigger condition | Workflow | Expected output |
|---|---|---|---|
| **`quick`** | Single component edit, button style, small animation tweak, bug fix, copy edit. | Local inspection → direct targeted implementation → verification. | Minimal diff; zero unnecessary refactoring or catalog sweeps. |
| **`standard`** | New page, substantial feature, section redesign, multi-step form, interactive widget. | Task analysis → reference search → composition → responsive implementation → audit. | Component code, responsive layouts, state handling, visual checks. |
| **`comprehensive`** | Brand-new website or web app from scratch, major full-site redesign, complex digital product. | 9-Stage Full Lifecycle: Strategy → IA → Direction → UI/UX → Motion → Dev → QA → Refine. | Architecture map, design system tokens, full page routes, verified code. |

*Override:* The user may explicitly specify `mode: quick`, `mode: standard`, or `mode: comprehensive`.

## Progressive Disclosure & Competence Routing

Do not load all reference files into context at once. Load only the specific modules demanded by the current phase:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        TASK INTAKE & TRIAGE                            │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
          ┌─────────────────────────┼─────────────────────────┐
          ▼                         ▼                         ▼
   [Strategy & IA]            [Design & Craft]         [Engineering]
   • website-strategy.md      • visual-design.md       • frontend.md
   • information-arch.md      • composition-patterns   • backend.md
   • ux-patterns.md           • section-patterns.md    • responsive-design.md
   • industry-patterns.md     • design-anti-patterns   • motion-design.md
          │                         │                         │
          └─────────────────────────┼─────────────────────────┘
                                    │
                                    ▼
                         [Verification & Delivery]
                         • quality-assurance.md
                         • design-review.md
                         • scripts/validate-design.mjs
```

### Competence Matrix

| If the task involves... | Read from `references/` | Read from `design-intelligence/` | Read from `workflows/` |
|---|---|---|---|
| Business goals, user models, lead-gen vs catalog | [website-strategy.md](references/website-strategy.md), [information-architecture.md](references/information-architecture.md) | [industry-patterns.md](design-intelligence/industry-patterns.md), [ux-patterns.md](design-intelligence/ux-patterns.md) | [new-project.md](workflows/new-project.md) |
| Layout, hierarchy, typography, colors, themes | [ui-design.md](references/ui-design.md), [visual-design.md](references/visual-design.md), [design-systems.md](references/design-systems.md) | [composition-patterns.md](design-intelligence/composition-patterns.md), [section-patterns.md](design-intelligence/section-patterns.md), [design-anti-patterns.md](design-intelligence/design-anti-patterns.md) | [new-page.md](workflows/new-page.md), [component-development.md](workflows/component-development.md) |
| Animations, transitions, gestures, scroll effects | [motion-design.md](references/motion-design.md), [scroll-interactions.md](references/scroll-interactions.md) | [motion-patterns.md](design-intelligence/motion-patterns.md) | [motion-development.md](workflows/motion-development.md) |
| Mobile adaptation, touch, fluid layout | [responsive-design.md](references/responsive-design.md) | [responsive-patterns.md](design-intelligence/responsive-patterns.md) | [quality-assurance.md](workflows/quality-assurance.md) |
| Components, state, APIs, database, auth | [frontend.md](references/frontend.md), [backend.md](references/backend.md), [security.md](references/security.md) | [ux-patterns.md](design-intelligence/ux-patterns.md) | [new-project.md](workflows/new-project.md) |
| SEO, accessibility, performance, vitals | [seo.md](references/seo.md), [accessibility.md](references/accessibility.md), [performance.md](references/performance.md) | [design-anti-patterns.md](design-intelligence/design-anti-patterns.md) | [quality-assurance.md](workflows/quality-assurance.md) |
| Auditing existing designs or legacy code | [ui-design.md](references/ui-design.md), [performance.md](references/performance.md) | [design-anti-patterns.md](design-intelligence/design-anti-patterns.md) | [design-review.md](workflows/design-review.md), [existing-project.md](workflows/existing-project.md) |

## Searching References and Libraries

Before implementing UI or motion, search the curated registry using the bundled search script:

```bash
# Search by industry and section
node scripts/search-references.mjs --industry tourism --category hero

# Search components by motion type or complexity
node scripts/search-references.mjs --category scroll-animations --complexity medium

# Search across all indexed websites, components, and animations
node scripts/search-references.mjs --query "pinned scroll cards"
```

### Supported Component & Motion Ecosystems

1. **shadcn/ui**: Core accessible primitives, forms, dialogs, data tables.
   - MCP Server: `npx -y shadcn@latest mcp`
   - Install: `npx shadcn@latest add <component>`
2. **Aceternity UI**: Hero sections, 3D cards, sticky scroll, animated backgrounds, liquid glass.
   - Registry: `https://ui.aceternity.com/registry/{name}.json`
   - Install: `npx shadcn@latest add https://ui.aceternity.com/registry/<name>.json`
3. **Magic UI**: Animated landing components, interactive text, marquee, particles.
   - MCP Server: `npx -y @magicuidesign/mcp@latest`
   - Registry: `https://magicui.design/r/{name}.json`
4. **React Bits**: Text animations, creative backgrounds, interactive cursor, WebGL shaders.
   - Registry: `https://reactbits.dev/r/{name}.json`
   - Install: `npx shadcn@latest add @react-bits/<ComponentName>-TS-TW`
5. **Motion Primitives**: Fluid layout morphs, gesture cards, animated accordions, popovers.
   - Registry: `https://motion-primitives.com/c/{name}.json`
6. **GSAP & ScrollTrigger**: Complex timeline sequencing, pinned scrollytelling, SplitText, Flip. All plugins are 100% free (`npm i gsap @gsap/react`).
7. **Motion (formerly Framer Motion)**: Declarative springs, AnimatePresence, shared element transitions.
8. **Codrops & Three.js**: WebGL shaders, camera transitions, 3D product visualizers (used selectively).

*Rule of thumb:* Never assemble an incoherent patchwork. Adapt library components into a unified token system (shared spacing, radius, colors, and motion physics).

## Core Design Principles

1. **Grounded in Subject Matter:** Derive the visual language from the client's industry, materials, and users. A luxury perfume boutique must look completely different from an industrial equipment catalog.
2. **Optical Typography:** 
   - Body measure: 45–75 characters per line (max 80).
   - Display headings: tighter tracking (`-0.01em` to `-0.03em`) and tight leading (`0.95` to `1.1`).
   - Small labels: slight tracking expansion (`+0.04em` to `+0.08em`).
   - Scale contrast: prioritize size ratios (4.0x–4.8x between hero headline and body) over heavy font weights.
3. **Anti-Slop (No AI Tells):**
   - No arbitrary single-word italic/neon accents in headlines.
   - No decorative numbers (`01`, `02`, `03`) unless there is a genuine chronological or procedural sequence.
   - No redundant uppercase eyebrow badges above every heading.
   - No forced symmetric 3-column bento grids on unequal data.
   - No default cliché palettes (violet-glow on dark slate, or warm cream `#F4F1EA` with generic serif) without brief justification.
4. **Resilient Hardening:**
   - Mobile input zoom floor: `font-size: 16px` minimum on inputs, selects, and textareas to prevent iOS Safari auto-zoom.
   - Container blowout protection: `min-width: 0` on flex/grid items with `overflow-wrap: anywhere`.
   - Never disable submit buttons during submission in ways that drop keyboard focus; use `aria-busy="true"` and visible spinners.
   - Never gate essential functionality exclusively behind pointer `:hover`.
   - Never disable viewport scaling (`maximum-scale=1.0` or `user-scalable=no` violates WCAG 1.4.4).
   - Sanitize user microcopy: never expose raw database errors or stack traces.
5. **Calibrated Motion:**
   - 100+ times/day interactions (shortcuts, command palette) = **0ms (instant)**.
   - Frequent routine navigation = `<=150ms`.
   - Contextual overlays (modals, sheets) = `150–250ms`.
   - Entrances use decelerating **`ease-out`**. Never use `ease-in` for entrances.
   - Spring physics for direct touch manipulation with near-critical damping (`dampingRatio: 0.8–1.0`).
   - In GSAP ScrollTrigger, **higher numbers refresh first** (`refreshPriority`).

## The 9-Stage Standard Workflow

When working in `comprehensive` mode:

1. **Business Understanding:** Identify business model, target audience, primary user conversion action, and trust requirements.
2. **Information Architecture:** Map pages, navigation, reading hierarchy, and user decision pathways.
3. **Reference Research:** Query [libraries/](libraries/) for 2–3 relevant industry benchmarks and component patterns; examine live demos where helpful.
4. **Design Direction:** Select visual tone, font pairing, color roles, spacing scale, and radius system.
5. **UI/UX Composition:** Build structured layouts block-by-block based on user questions, not static templates.
6. **Motion Design:** Define purposeful transitions, gestures, scroll behaviors, and reduced-motion fallbacks.
7. **Frontend & Backend Implementation:** Code components cleanly using modern TypeScript, CSS tokens, and robust server invariants.
8. **Quality Assurance:** Validate across the viewport matrix (360px, 390px, 768px, 1024px, 1440px), verify keyboard accessibility, check contrast, and test build.
9. **Refinement:** Polish alignment, microcopy, error states, and responsive edge cases.

## Automated Verification

Run design and catalog validation tools before claiming completion:

```bash
# Validate component and animation registry schema
node scripts/validate-catalog.mjs

# Lint markup and styles for optical typography and hardening defects
node scripts/validate-design.mjs <file-or-directory>
```

## Completion Criteria

A task is complete only when:
- The implementation fulfills the user's specific business and functional requirements.
- Responsive layouts work seamlessly across mobile (390px), tablet (768px), and desktop (1440px) without horizontal overflow.
- Forms enforce 16px input floors, accessible submission states, and error handling.
- Motion obeys frequency rules, reduced-motion preferences, and uses compositor-friendly properties.
- Code compiles, lints cleanly, and passes automated verification.
