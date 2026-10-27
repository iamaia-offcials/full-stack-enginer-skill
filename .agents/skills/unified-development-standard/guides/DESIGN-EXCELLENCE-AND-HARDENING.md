# Design excellence, typography, and interface hardening

Guidance for distinctive visual craft, optical typography, anti-slop review, and resilient interface engineering. Supplements normative rules in [DS-011 through DS-013](../references/09-DESIGN-SYSTEM.md), [FE-011 and FE-012](../references/08-FRONTEND.md), and [WEB-013 through WEB-015](../references/27-WEB-ENGINEERING.md).

## Optical typography and measure

Typography communicates character and structure before text is read:

| Attribute | Recommended standard | Technical reason |
|---|---|---|
| **Body measure** | 45–75 characters per line (max 80) | Line lengths exceeding 80 characters increase tracking difficulty across returns; lines below 40 break natural phrasing. |
| **Body line-height** | Sans-serif: `1.4–1.55`; Serif: `1.5–1.65` | Serif faces with pronounced vertical ascenders/descenders require more breathing room to avoid clashing. |
| **Display headings** | Tracking: `-0.01em` to `-0.03em`; Leading: `0.95–1.1` | Large type (>48px / >3.5vw) naturally spaces letters too far apart visually. Tight tracking creates cohesive word silhouettes. |
| **Small labels / All-caps** | Tracking: `+0.04em` to `+0.08em` | Uppercase glyphs have uniform rectangular profiles and need breathing space to prevent letter blending. |
| **Headline-to-body ratio** | 4.0x–4.8x scale ratio in heroes | Top-tier editorial layouts achieve visual punch through pronounced scale contrast rather than setting every headline to extra-bold. |

## Anti-slop heuristics (avoiding AI tells)

Generic AI-generated interfaces exhibit predictable defaults that make pages feel assembled from templates rather than intentionally designed:

1. **Arbitrary word accents:** Avoid highlighting a single word in a headline with italic, neon accent color, or underline unless the brand specifically requires it.
2. **Ornamental ordinals:** Avoid numbering items (`01`, `02`, `03`) unless the content represents a genuine temporal sequence, ordered algorithm, or step-by-step workflow.
3. **Eyebrow overuse:** Avoid placing a tiny uppercase badge or tag above every single heading. Structural devices must encode semantic hierarchy, not decorative padding.
4. **Forced bento grids:** Do not force asymmetric or sequential content into symmetric square tiles or icon cards simply for layout fashion. Match container proportions to content density.
5. **Cliché color formulas:** Do not default to generic templates (e.g. violet/indigo glows on dark slate, or warm cream `#F4F1EA` with generic serif) without project-grounded rationale. Derive palettes from the product's subject matter, materials, and user context.

## Interface hardening and resilience

Designs that only work with short, ideal English strings are not production-ready:

### 1. Flexbox and grid overflow defense

Flex and grid items default to `min-width: auto`, which allows children with long unbreakable content (URLs, email addresses, file paths, code snippets) to blow out containers horizontally.

```css
/* ✅ Prevent container blowout on flexible items */
.flex-item, .grid-item {
  min-width: 0;
  min-height: 0;
}

.text-content {
  overflow-wrap: anywhere;
  word-break: break-word;
}
```

### 2. Mobile input zoom floor (16px)

iOS Safari automatically zooms the entire viewport when focusing an `<input>`, `<select>`, or `<textarea>` whose computed `font-size` is below 16px. This unexpected zoom disrupts fixed navigation bars, breaks modals, and causes horizontal layout shift.

```css
/* ✅ Ensure inputs maintain at least 16px on mobile viewports */
input, select, textarea {
  font-size: 16px; /* or clamp(16px, 1.2vw, 18px) */
}
```

### 3. Internationalization (i18n) space budgets

- Languages such as German, French, or Russian frequently expand text by **30% to 40%** relative to English.
- Avoid fixed button and container widths (e.g. `w-24`). Use content-adaptive layouts with padding (`px-4 py-2`).

### 4. Accessible form submission states

- **Do not simply disable (`disabled`) submit buttons while in-flight:** doing so removes the button from keyboard focus order, traps keyboard users, and fails to communicate why action is blocked.
- Instead, maintain focus, indicate in-flight state via `aria-busy="true"` or `aria-disabled="true"`, render an inline spinner, and announce progress via an `aria-live` region.

### 5. Hover parity on touch devices

Touchscreens have no persistent pointer hover. Never hide essential controls (edit, delete, options menu, copy button) strictly behind `:hover`. Provide always-visible or touch-operable taps for critical actions.

### 6. Viewport scaling

Never set `maximum-scale=1.0` or `user-scalable=no` in `<meta name="viewport">`. This violates WCAG 2.2 SC 1.4.4 (Resize text up to 200%) and prevents low-vision users from magnifying content.
