# 28. Motion design and interaction transitions

Apply when motion is introduced, changed or reviewed. Existing product language and task scope determine expression; no animation is a valid choice. These are engineering rules, not one visual style or mandatory library.

## Purpose and ownership

- `[MOT-001] MUST` Give intentional motion a purpose: feedback, continuity, hierarchy, spatial relationship, progress, or explicitly scoped decorative storytelling. Omit movement that adds no useful value.
- `[MOT-002] MUST` Inspect and reuse existing motion primitives, tokens and component owners. Do not duplicate a component or curve for the same semantic role.
- `[MOT-003] SHOULD` Keep a small semantic scale for duration, easing, travel and spring presets. Explain local exceptions; example milliseconds are not industry requirements.
- `[MOT-004] MUST` Make stateful transitions interruptible or safely cancellable. Rapid actions must converge on the latest valid requested UI state, subject to domain constraints, without stale completion callbacks, stranded overlays or lost focus.
- `[MOT-005] MUST` Preserve semantics, reading order, focus and operability throughout a transition. Off-screen or exiting live elements must not remain unintentionally interactive or focusable; duplicate transition visuals must not create duplicate accessible controls.
- `[MOT-006] MUST` Implement A11Y-007 for the changed transition: suppress nonessential spatial motion/parallax/choreography under reduced motion and preserve the destination state through instant rendering or a suitable restrained alternative.
- `[MOT-007] MUST` Apply A11Y-004 to animated states. Expose validation, success/error and meaningful progress through persistent text/semantics; avoid announcing every interpolated numeric frame.
- `[MOT-008] MUST` Check applicable flashing, autoplay and auto-update criteria under A11Y-007. Interaction animation SC 2.3.3 is AAA; pause/stop/hide SC 2.2.2 is A with specific conditions. Reduced-motion support alone proves neither conformance nor a complete accessibility audit.

## Implementation and state

- `[MOT-009] SHOULD` Prefer transform/opacity for frequent web movement/fades. Layout, masks and paint-heavy effects are allowed when justified and measured under PERF-001/OPT-*. Compositor-friendly properties do not guarantee smoothness.
- `[MOT-010] MUST` Give immediate feedback and keep essential actions available. Do not gate navigation, data mutation or request completion on an animation timer or transition event; guard duplicate business operations separately.
- `[MOT-011] MUST` Follow actual navigation, origin and gesture semantics, accounting for writing direction where relevant. A shared-element effect requires recognizable entity continuity, not merely similar shapes.
- `[MOT-012] SHOULD` Tune travel, duration and easing to distance, scale, repetition, density, input method and supported devices. Frequent work usually needs less visual intensity; departure need not mirror arrival.
- `[MOT-013] SHOULD` Reserve large zooms, parallax, bounce, perpetual motion and expressive sequences for justified contexts. Do not hijack scrolling or replay entrances on routine updates without a reason.
- `[MOT-014] MUST` Handle reversal, mount/unmount, route changes and relevant resize/preference changes. Clean up animation objects, observers, listeners and timers; reject stale callbacks and handle cancellation of awaited animation promises.
- `[MOT-015] SHOULD` Use CSS for simple self-contained states and existing primitives/libraries for advanced needs. Choose WAAPI, shared-layout tooling or native platform animation only when its control/gesture/sequence capabilities justify the cost. A hover fade does not justify a new package.
- `[MOT-016] MUST` Animate explicit properties instead of a global `transition: all` policy. Keep motion with its canonical component and compose transforms deliberately when multiple systems affect one element.
- `[MOT-017] SHOULD` Bound total choreography/stagger time. Large lists and search results must remain available without waiting for sequential entrances; do not delay essential content behind an observer or JavaScript enhancement.
- `[MOT-018] MUST` Derive loading, completion, errors and counts from real application state. Show determinate progress only from a meaningful measurement; do not invent percentages, simulate success or use visual duration as operation truth.

## Verification and documentation

- `[MOT-019] MUST` Verify significant transitions in representative supported browsers/device classes; use relevant PERF-001/OPT-* measurements for performance-sensitive effects. Include mobile when targeted, record untested targets, and distinguish browser emulation from real-device evidence. Never invent FPS or visual-check results.
- `[MOT-020] SHOULD` Profile continuous effects, blur/filter/backdrop-filter, large shadows and excessive compositing layers when used. Apply `will-change` selectively for a demonstrated need, not to every element permanently.
- `[MOT-021] MUST` Keep controls, meaningful content and dismissal usable when animation is absent, cancelled, paused or disabled. Gesture-driven actions need an operable non-gesture alternative where required.
- `[MOT-022] SHOULD` Verify support for the exact View Transitions/scroll-driven features used. Keep ordinary navigation and rendering as the usable fallback; optional animation APIs must not become functional dependencies.
- `[MOT-023] SHOULD` Prefer semantic roles such as `menu-enter`, `dialog-exit` or `tab-indicator` over unrelated page-specific animation names. Share by meaning rather than forcing one preset on every interaction.
- `[MOT-024] MUST` For a new complex pattern, update its existing component/feature specification with trigger, purpose, from/to states, properties/model, cancellation, reduced-motion/fallback behavior and relevant evidence. A trivial edit does not need a separate motion document.

For decision formulas, vocabulary, contextual examples and engineering choices, read the relevant part of the [motion guide](../guides/MOTION-DECISIONS.md). A11Y owns general accessibility, DS-009 visual suitability, and PERF/OPT performance evidence; this section specifies their motion application.
