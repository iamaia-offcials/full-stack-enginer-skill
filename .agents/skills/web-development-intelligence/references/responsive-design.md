# Responsive & Adaptive Web Design

Design fluid, resilient interfaces across the complete device spectrum from 360px phones to 4K displays.

## Viewport Matrix & Breakpoint Strategy

| Target Class | Width Range | Layout Behavior | Key Considerations |
|---|---|---|---|
| **Mobile Small** | 360px – 389px | 1 column, compact | Minimum 44x44px touch targets, 16px font floor on inputs. |
| **Mobile Standard** | 390px – 480px | 1 column, fluid | Dynamic island/notch safe areas (`env(safe-area-inset-top)`). |
| **Tablet / Foldable** | 768px – 1023px | 2 columns, adaptive | Hybrid touch/pointer interaction, collapsible drawer navigation. |
| **Desktop Laptop** | 1024px – 1439px | 2–3 columns, bounded | Max content container 1200–1280px, mouse hover affordances. |
| **Desktop Large** | 1440px – 1920px+ | Multi-column, rich | Bounded max-width to preserve comfortable reading measure. |

## Responsive Rules & Hardening

1. **Fluid Typography with `clamp()`:**
   - `font-size: clamp(1rem, 0.9rem + 0.5vw, 1.25rem);` enables smooth scaling without jarring breakpoint jumps.
2. **Container Queries (`@container`):**
   - Style components based on their parent container's available width rather than the global window viewport. Enables truly reusable components across sidebars and main content.
3. **Touch Targets:**
   - Minimum 44x44px (WCAG 2.5.5) or 24x24px with surrounding spacing (WCAG 2.5.8 Target Size).
