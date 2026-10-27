# Design Systems, Tokens & Theming

Establish scalable, maintainable design systems with tokens as the single source of truth.

## Semantic Token Architecture

1. **Three-Tier Token Hierarchy:**
   - **Tier 1: Global / Primitives:** Raw values (`--blue-500: #3b82f6`, `--space-4: 16px`, `--radius-md: 12px`).
   - **Tier 2: Semantic Tokens:** Purpose-bound tokens (`--surface-primary`, `--text-muted`, `--border-focus`, `--action-primary-bg`).
   - **Tier 3: Component Tokens:** Specific overrides (`--button-height`, `--card-padding`).

2. **Light & Dark Theme Parity:**
   - Never mechanically invert colors (`#000` to `#fff`). True dark mode requires lower contrast and desaturated accent colors to prevent ocular fatigue.
   - Surfaces in dark mode elevate via lighter surface steps (`#121212` ground, `#1e1e1e` surface-1, `#2a2a2a` surface-2) rather than casting black shadows.
   - Set `color-scheme: light dark` to inform the browser rendering engine and form controls.

3. **Component Contract:**
   Every design system component must document:
   - Purpose and semantic role.
   - Supported variants (e.g. `default`, `outline`, `ghost`, `danger`) and sizes (`sm`, `md`, `lg`).
   - Interactive states: `default`, `hover`, `focus-visible`, `active`, `disabled`, `loading`.
   - Accessibility ARIA attributes and keyboard behavior.
