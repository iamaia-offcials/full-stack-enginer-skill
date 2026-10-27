# Workflow: Motion Development & Transition Tuning

Implement fluid, performant, and accessible animations.

## Procedure

1. **Motion Justification Check:**
   - Does this motion serve feedback, spatial continuity, or explicit narrative? If not, delete it.
2. **Frequency Calibration:**
   - Check `references/motion-design.md` matrix. If triggered 100+ times/day, set duration to 0ms.
3. **Property & Easing Selection:**
   - Animate only `transform` and `opacity`.
   - Apply decelerating `ease-out` for entrances.
4. **Reduced Motion & Mobile Fallback:**
   - Wrap in `@media (prefers-reduced-motion: reduce)`.
   - Provide natural unpinned scroll on screens under 768px.
