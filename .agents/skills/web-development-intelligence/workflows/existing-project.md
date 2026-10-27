# Workflow: Working with Existing Projects

Preserve established architectural patterns, tokens, and components without introducing breaking changes or parallel design systems.

## Step-by-Step Procedure

### 1. Token Discovery & Design System Audit
- **Inspect CSS variables:** Scan `globals.css`, `index.css`, or `tailwind.config.js` for `--background`, `--foreground`, `--primary`, `--radius`, and font families.
- **Audit Existing Primitives:** Locate existing atomic components (`Button`, `Card`, `Input`, `Dialog`, `Sheet`).
- **Audit Motion Stack:** Identify whether the project uses `framer-motion` / `motion`, `gsap`, `tailwind-animate`, or pure CSS transitions.
- **Strict Rule:** Do NOT reinvent or replace existing core components without explicit user authorization. If a button component exists, all new screens must use that existing component.

### 2. Additive & Non-Breaking Modifications
- Keep changes strictly additive. Never break public component props, imports, or existing routing patterns.
- If implementing a new section, use the existing token variables (`var(--primary)`, `var(--radius)`, `var(--font-heading)`) rather than hardcoding new hex values or arbitrary paddings.
- If importing a component from an external registry (such as Aceternity or Magic UI), immediately refactor its classes to map onto the host project's Tailwind config and semantic color tokens.

### 3. Progressive Visual Refinement
- When tasked with "improving" or "polishing" an existing page, conduct a targeted visual review:
  - Fix broken typographic scale hierarchy.
  - Standardize inconsistent card paddings (`p-4` vs `p-8` on the same page).
  - Add missing interactive states (`hover:`, `focus-visible:`, `disabled:`).
  - Preserve all form logic, API handlers, data fetching, and analytics hooks intact.
