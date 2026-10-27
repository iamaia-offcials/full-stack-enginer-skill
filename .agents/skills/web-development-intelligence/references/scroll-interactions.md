# Scroll Interactions, Pinning & Scrollytelling

Orchestrate compelling scroll-driven experiences while preserving user agency and document flow.

## Core Scroll Paradigms

1. **Never Hijack Native Scrolling:**
   - Do not override mouse wheel velocity or implement artificial inertia scripts that fight the operating system.
   - Pinned sections must occupy physical vertical space (`height: 300vh`) so the scrollbar remains truthful.

2. **GSAP ScrollTrigger Architecture:**
   - **`refreshPriority` Rule:** In GSAP ScrollTrigger, **higher numbers refresh first** (default 0). Set higher priority on pinning or DOM-expanding sections at the top of the page so they recalculate before lower triggers measure positions.
   - **Composite Animation:** Animate `transform` (`xPercent`, `yPercent`, `scale`, `rotation`) and `opacity`. Never animate `top`, `left`, `width`, or `height` on scroll.
   - **Mobile Unpinning:** If vertical screen space on mobile (<600px height) is insufficient to display pinned content legibly, disable pinning via `ScrollTrigger.matchMedia()` and revert to natural vertical stacking.

3. **CSS Scroll-Driven Animations (`animation-timeline: scroll()`):**
   - Prefer native CSS scroll-driven animations for simple reading progress bars and basic section fade-ins when supported, falling back gracefully to static display.
