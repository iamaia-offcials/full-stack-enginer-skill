# 10. Interface accessibility (a11y)

**Default web target:** WCAG 2.2 AA with a documented verification scope. WCAG is a testable standard; AA does not mean every requirement can be checked automatically.

- `[A11Y-001] MUST` Meet contrast ratios of at least 4.5:1 for normal text and 3:1 for large text. Meaningful non-text controls and state indicators generally require 3:1, subject to the standard's defined exceptions.
- `[A11Y-002] MUST` Make functionality keyboard-accessible: visible focus, logical tab order, dialog management, and no keyboard traps. A modal may contain focus while open, but users must be able to dismiss or complete it using the keyboard.
- `[A11Y-003] MUST` Provide field labels/instructions, associate errors with fields, expose meaningful messages to assistive technologies, and give controls distinguishable accessible names.
- `[A11Y-004] MUST` Do not convey information solely through color, animation, or sound. Provide textual/semantic alternatives for loading, progress, and status.
- `[A11Y-005] MUST` Support web text resizing to 200% without loss of content/functionality, orientation changes, and reflow according to applicable WCAG criteria.
- `[A11Y-006] MUST` For WCAG 2.2 AA, targets are at least 24×24 CSS px **subject to the defined exceptions**. As a UX guideline, primary mobile controls are typically 44–48 CSS px or larger.
- `[A11Y-007] MUST` Respect `prefers-reduced-motion`, prevent/limit hazardous flashes, and provide controls for automatically updating content.
- `[A11Y-008] MUST` For affected scenarios, combine available automated checks with manual keyboard, zoom, and supported-theme checks. Use screen-reader checks for substantial interactive scenarios. An automated score does not prove WCAG compliance.
- `[A11Y-009] SHOULD` Prefer native semantic elements to div-based imitations of buttons/controls. Use ARIA only when HTML semantics are insufficient.

## Requirement boundaries
Apple's iOS touch-target recommendations generally use **pt**, while Android uses **dp**. Neither unit is equivalent to CSS px, and these recommendations are not WCAG requirements. Distinguish formal WCAG limits from the team's more generous usability targets.
