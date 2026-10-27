# User Experience (UX) Design

Eliminate user friction, prevent dead ends, and deliver intuitive interactions.

## Core Interaction Guidelines

1. **Cognitive Load Optimization:**
   - **Hick's Law:** Increasing the number of choices logarithmically increases decision time. Break complex decisions into stepped wizards or progressive disclosure.
   - **Miller's Law & Chunking:** Group related data into 4–6 visual clusters rather than presenting monolithic blocks of text or controls.
   - **Jakob's Law:** Users spend most of their time on other sites. Honor established conventions for search bars, cart icons, user profiles, and form layouts.

2. **State Completeness Invariant:**
   Every interactive component and screen scenario must explicitly account for six operational states:
   1. **Empty State:** First-time use, no records found, or zero search results. Must provide guidance or clear creation CTA, never a blank screen.
   2. **Loading State:** Skeletons matching exact final geometry or inline spinners with `aria-busy="true"`. Prevent layout shift when data arrives.
   3. **Partial / Incomplete State:** Content partially loaded or filtered.
   4. **Ready / Populated State:** Normal ideal data representation.
   5. **Error State:** Human-readable explanation of what went wrong and an immediate recovery path (Retry, Contact Support, Reset Filters).
   6. **Offline / Degraded State:** Graceful notification when network drops, caching pending inputs locally where safe.

3. **Form Experience & Affordances:**
   - Always connect `<label>` to inputs using `htmlFor` / `id`.
   - Place labels above inputs, not as placeholders inside. Placeholders vanish upon typing, destroying memory context.
   - Provide inline validation after the user leaves the field (`onBlur`), not on the very first keystroke.
   - Error messages must explain *how to fix* the issue, not just state that it failed.
