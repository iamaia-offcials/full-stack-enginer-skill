# Web Accessibility (A11Y) & Inclusive Design

Guarantee equal access across keyboard navigation, screen readers, touch, and assistive technologies conforming to WCAG 2.2 AA.

## Essential Accessibility Standards

1. **Keyboard Operability:**
   - All interactive controls must be operable via Tab, Enter, Space, and Arrow keys.
   - Visible focus indicators (`:focus-visible`) must never be suppressed with `outline: none` without providing a high-contrast replacement.
   - Manage focus trap and restoration inside modal dialogs and slide-out drawers.

2. **Color Contrast (WCAG 1.4.3 & 1.4.11):**
   - Normal text: minimum **4.5:1** contrast ratio against its background.
   - Large text (>=18pt or 14pt bold): minimum **3.0:1**.
   - Interactive boundaries and focus rings: minimum **3.0:1**.
   - Never rely on color alone to convey status or errors; pair with icons or explicit text.

3. **Reduced Motion (WCAG 2.3.3):**
   - Wrap non-essential animations in `@media (prefers-reduced-motion: reduce)`.
   - Provide instant state rendering or subtle opacity fades when reduced motion is requested.
