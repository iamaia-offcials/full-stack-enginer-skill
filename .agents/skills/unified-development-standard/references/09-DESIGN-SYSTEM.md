# 09. Design system: styles, themes, components, and responsiveness

**References:** Apple Human Interface Guidelines, Material Design 3, and Fluent 2 provide platform guidance, not universal design laws. Verify web accessibility separately against WCAG.

- `[DS-001] MUST` Find existing foundations/tokens/components and style owners. Store repeated semantic values in one place; introduce layers and separate files according to project size, not a formal template.
- `[DS-002] MUST` Use semantic color roles. If the product supports multiple themes, define correct values for each. Do not mechanically invert colors or add a theme without a need.
- `[DS-003] MUST` Document a component's purpose, variants, sizes, anatomy, spacing, responsive behavior, applicable states (`default/focus/hover/pressed/disabled/loading/error`), accessibility, and usage rules.
- `[DS-004] SHOULD` Use consistent spacing, typography, and radius scales aligned with the existing design system and requirements. Specific pixel values are not universal rules.
- `[DS-005] MUST` Check final color contrast in all supported themes and affected states/images/overlays. Apply WCAG exceptions where relevant; transparency is no substitute for measurement.
- `[DS-006] MUST` Align hierarchy, primary actions, grid, states, and labels with the user's task. Context determines the number of actions; do not impose a universal prohibition.
- `[DS-007] SHOULD` When multiple themes are needed, define System/Light/Dark behavior, persist the choice, and prevent flashes of the wrong theme. Do not add a switch for a single theme.
- `[DS-008] MUST` Review token/component changes as shared-system changes and visually test affected consumers. Check impact before changing global styles for one page.
- `[DS-009] SHOULD` Use transparency, blur, and motion according to purpose, brand, and platform requirements; verify readability, performance, and accessibility. Do not impose a visual style.
- `[DS-010] MUST` Represent local exceptions with a variant/token or documented rationale, not chaotic CSS specificity overrides and `!important`.
- `[DS-011] SHOULD` Tune optical typography: maintain comfortable body line lengths between 45–75 characters (max 80); calibrate line-height to typeface classification (1.5–1.65 for serif, 1.4–1.55 for sans-serif); apply tighter tracking (-0.01em to -0.03em) and tight leading (0.95–1.1) to large display type, while slightly opening tracking (+0.04em to +0.08em) on small all-caps labels.
- `[DS-012] MUST` Reject generic AI design clichés and unconsidered defaults: do not decorate single words in headlines with arbitrary italic/color accents; do not attach numbered ordinals (01, 02, 03) unless content is an actual ordered sequence; do not insert redundant eyebrow labels above every title; do not force bento grids on unequal data; and do not resort to cliché palettes (e.g. violet glows on dark slate, or warm cream with default serif) without subject-grounded rationale.
- `[DS-013] SHOULD` Leverage scale contrast over weight: establish distinct visual hierarchy through pronounced scale ratios between display headings and body copy (e.g. 4x+ scale ratio on prominent surfaces) paired with intentional whitespace, rather than setting every text block to bold or heavy weights.

## Tokens as a source of truth
```css
:root { --space-1:4px; --radius-md:12px; }
:root,[data-theme="light"] { color-scheme:light; --surface:#fff; --text:#17212f; }
[data-theme="dark"] { color-scheme:dark; --surface:#18212b; --text:#f5f7fa; }
.card { background:var(--surface); color:var(--text); border-radius:var(--radius-md); }
```
These values illustrate a product with two themes; they do not require adding a second theme and **do not prove WCAG compliance**. Measure actual text/background pairs, focus, validation, disabled states, and other relevant combinations against applicable criteria and exceptions.

## Page composition and references

For substantial page/journey selection, use [UXR rules](29-UX-REFERENCE-RESEARCH.md) and the [reference guide](../guides/UX-REFERENCE-RESEARCH.md). Establish supported operations and content per journey, then choose blocks by user questions rather than a niche template. The atlas provides selective English case notes, conditional compositions and motion visuals; supplied text observations are not live-site screenshots or proof of effectiveness.

## Motion decisions

For affected interactions, use [MOT rules](28-MOTION-DESIGN.md) and, when selection needs explanation, the [decision guide](../guides/MOTION-DECISIONS.md). Establish purpose, before/after states, repetition, spatial relationship and project character before choosing an effect. Preserve existing semantic motion tokens; no animation is a valid candidate. Add complex transition behavior to the current component specification rather than creating parallel motion documents. Numerical timings or Atlas scores are examples, not universal requirements.

## Visual defect audit
Check for inconsistent tokens, one-off buttons duplicating existing components, missing supported-theme variants, excessive custom CSS, inconsistent card density, too many visual accents, unreadable blur, incorrect content order, and inconsistent icon sets.

For practical patterns and anti-slop criteria, read [decision formulas](../guides/PRACTICAL-FORMULAS.md) and [design excellence and hardening](../guides/DESIGN-EXCELLENCE-AND-HARDENING.md).
