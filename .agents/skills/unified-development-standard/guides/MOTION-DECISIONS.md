# Contextual motion decisions

Read for motion selection or implementation, not for every frontend edit. Adapted from the supplied Motion Atlas 3.0 decision material and its earlier scenario library. The [MOT rules](../references/28-MOTION-DESIGN.md) are normative; this guide explains them. Examples are not a required brand identity or production certification.

## Decision formula

**Goal and event → before/after/error/cancel states → constraints → viable alternatives → project-specific choice → implementation → evidence.**

Establish user goal, repetition, spatial/entity relationship, content density, input method, target devices, accessibility, performance and existing product character. Use available project evidence; do not ask a questionnaire for a small known interaction. If no useful change needs emphasis, render the state directly.

Correctness, access/focus, reduced-motion behavior, truthful feedback, input availability and usable API fallbacks are gates. Reject an option violating one before comparing aesthetic benefit. A favorable score never compensates for a failed gate.

For a consequential or ambiguous choice, compare two or three viable options, including no motion. For a familiar minor transition, reuse the existing pattern without a formal scoring exercise. Optional reasoning shorthand:

`utility = continuity + feedback + spatial clarity + useful hierarchy − distraction − sensory/cognitive load − implementation/runtime cost`.

The Atlas illustrates this as `U = 2C + 2F + S + H − 2D − 2K − R` with subjective 0–5 ratings. These weights are illustrative, configurable and unvalidated; do not treat a numerical winner as policy or scientific proof. In most tasks, a short comparison with reasons is clearer.

Useful relationships, not fixed equations:

- Greater repetition/density usually calls for less travel, emphasis and delay.
- Duration depends on travel, scale, content, device and product rhythm; there is no universal 250 ms rule.
- Direct manipulation should follow real input/velocity; interruption should retarget from the current rendered position where appropriate.
- Network uncertainty requires honest pending state and a recovery path; animation cannot establish successful completion.
- A new user action targets the latest intended state instead of queuing obsolete transitions. Preserve domain constraints and duplicate-request protection separately.

## Vocabulary: keep the axes separate

| Axis | Terms | Decision it answers |
|---|---|---|
| Trigger | press, focus, hover, drag, scroll, state change | What starts or controls the transition? Touch has no dependable hover. |
| Visual effect | fade/crossfade, slide, scale, reveal, highlight, shared element | What relationship should the user perceive? |
| Technique/model | tween/easing, spring, keyframes, FLIP | How is the movement calculated or coordinated? |
| Implementation | CSS, WAAPI, existing library, View Transitions, native framework | What project-supported mechanism provides the needed control? |

A spring is a displacement/velocity/damping model, not a visual style. Easing maps elapsed time to progress: decelerating entry and accelerating exit can serve different purposes; linear progress is appropriate for some continuous indicators. Avoid mandatory curve families across unrelated products.

FLIP means measure **First**, apply and measure **Last**, **Invert** the difference with a transform, then **Play** back to the final position. Control layout reads/writes and preserve stable entity keys. It is a technique to evaluate, not proof that layout work or text distortion disappears.

## Context changes the answer

| Task | Reasonable comparison | Why / rejection criterion |
|---|---|---|
| Dense admin table repeatedly sorted | Instant reorder + sort state; short highlight; FLIP for a small visible set | Scanning and responsiveness dominate. Reject long stagger, animated hundreds of rows or lost row focus. |
| Touch filter sheet | Existing sheet primitive + directional slide; restrained fade; immediate state | A meaningful screen edge can justify travel. Preserve close button/keyboard path, background inertness as applicable and focus restoration. |
| Product card to details | Shared entity transition; short fade; ordinary navigation | Continuity may help if it is the same object. Reject unsupported or inaccessible enhancement; fallback must retain navigation/history. |
| Save/payment result | Immediate semantic pending/result; optional local emphasis | Result comes from authoritative operation state. Reject timer-based success, fake percentages and celebration before confirmation. |
| Small menu or tabs | Existing component transition; fade/indicator; instant | Clarify disclosure/selection without delaying access. Keep one intended interactive view and selected semantics. |
| Marketing section or onboarding | Bounded reveal/choreography; static content | Rare storytelling may justify expression. Preserve initial content, usable scrolling and reduced-motion behavior; avoid copying another product's look. |
| Counters/charts/live data | Final value + stable label; brief highlight; selective interpolation | Keep numbers legible and announcements meaningful; avoid a live-region update for each animation frame. |

Choose amplitude, physics, materials, timing and visual emphasis from this product. A content brand can be expressive on a presentation page and restrained at checkout. Differences in goals justify different choices even for similar components.

## Implementation choices and pitfalls

- **CSS transitions/keyframes:** use explicit properties and semantic state classes for simple feedback. Reuse project tokens. Prefer native controls; preserve a visible focus state independent of movement. Keep decorative loops bounded or controllable as applicable.
- **WAAPI:** useful for play/reverse/cancel coordination. Clean up animation objects and catch cancellation of an awaited `finished` promise. Completion may clean up presentation but must not decide a payment result or overwrite a newer requested state.
- **Existing motion library:** reuse when already justified for gestures, layout identity or sequencing. Verify installed-version APIs and coordinate transform ownership. Do not add Motion/GSAP/Lottie/Rive simply because a recipe mentions it; asset size and maintenance count.
- **View Transitions:** progressively enhance ordinary navigation/state changes. Check the specific same-document/cross-document features used, handle failures, preserve history/focus/scroll, and distinguish visual snapshots from interactive live DOM. Do not apply ARIA to a decorative snapshot as if it were the destination control.
- **Scroll, masks, height or blur:** assess layout/paint and usability in the actual scenario. Height animation is not universally prohibited, but arbitrary huge `max-height` values can produce misleading timing. Content must remain available if JavaScript or an observer fails.
- **Native apps:** use native platform behavior and coordinate system. CSS pixel values, web easing and browser support do not define SwiftUI/Compose behavior.

Illustrative semantic tokens, to adapt rather than install globally:

```css
:root {
  --motion-feedback: 140ms;
  --motion-ease-feedback: cubic-bezier(.2, 0, 0, 1);
}
.action {
  transition: transform var(--motion-feedback) var(--motion-ease-feedback);
}
.action:active { transform: scale(.98); }
@media (prefers-reduced-motion: reduce) {
  .action { transition: none; }
  .action:active { transform: none; }
}
```

This assumes an existing semantic button and focus treatment. It does not prescribe timings or scale for every product. Reduced motion changes behavior, not just duration to 1 ms; keep state and information even if transition events no longer fire.

## Contract and checks

Add only needed fields to the current component/feature documentation: `trigger | purpose | from/to/error/cancel | properties/model/tokens | input/focus | interruption | reduced motion | unsupported-API fallback | evidence`.

For a filter sheet, visibility and request state are separate. Opening during an unfinished close retargets the presentation; a stale completion cannot hide the reopened sheet or restore focus outside it. Closing does not imply a filter request succeeded or was cancelled. Ignore or cancel obsolete requests according to the actual data contract.

Check relevant rapid repetitions/reversals, unmount and route/back navigation, content/viewport changes, keyboard and screen-reader semantics, reduced-motion changes, slow/error responses and fallback. Test only supported themes/locales/devices. A demo overlay missing focus containment, focus return, background behavior or scroll handling is a conceptual recipe until completed and verified.

For performance-sensitive effects, use equivalent before/after device, browser, build and data conditions; inspect frames, main-thread work, layout and paint, and input responsiveness where applicable. A 60 Hz display gives roughly 16.7 ms per frame and a 120 Hz display roughly 8.3 ms for **all** frame work. Transform/opacity, screenshots or attractive GIFs do not establish an FPS claim. Record unavailable checks as NOT_RUN; use [performance rules](../references/17-PERFORMANCE.md).

## Primary references and scope

- [Fluent 2 motion](https://fluent2.microsoft.design/motion): purpose, relationships, duration and choreography; its brand choices are not universal presets.
- [web.dev animation performance](https://web.dev/articles/animations-guide): rendering costs and measurement.
- [MDN View Transitions](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API) and [WAAPI](https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API): verify current feature support and control behavior.
- [WCAG 2.3.3, AAA](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html): disabling nonessential interaction motion; [2.2.2, A](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html): autoplay/auto-update conditions and exceptions. These explanatory pages support applying the normative WCAG standard, not a claim of product conformance.

Atlas previews, heuristic scores and this guide do not train model weights or replace project verification. Read a relevant example when useful; do not preload an entire gallery for every UI task.
