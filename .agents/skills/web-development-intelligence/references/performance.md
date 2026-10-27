# Performance Optimization & Core Web Vitals

Engineer blazing-fast web experiences meeting Core Web Vitals (CWV) thresholds on real mobile devices.

## Core Web Vitals Targets

- **Largest Contentful Paint (LCP):** `<= 2.5s` at 75th percentile. Preload hero images, optimize fonts, eliminate render-blocking CSS.
- **Interaction to Next Paint (INP):** `<= 200ms`. Keep main-thread tasks under 50ms, defer non-critical JS, avoid layout thrashing.
- **Cumulative Layout Shift (CLS):** `<= 0.1`. Reserve explicit `width` and `height` (or aspect-ratio) on images and video embeds.

## Rendering Pipeline Discipline

1. **Animate Composite-Only Properties:**
   - Stick to `transform` and `opacity`. Animating `width`, `height`, `margin`, `padding`, `top`, `left` triggers reflow and repaint on every frame.
2. **Selective `will-change`:**
   - Apply `will-change: transform` only immediately before animation starts, and remove it upon completion. Permanent application on dozens of elements wastes GPU memory.
