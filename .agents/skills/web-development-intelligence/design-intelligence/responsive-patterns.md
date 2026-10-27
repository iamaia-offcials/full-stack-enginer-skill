# Responsive Patterns & Mobile Architecture Shifts

Techniques for adapting complex desktop layouts into natural mobile experiences.

## Core Transformation Strategies

1. **Desktop Pinning to Mobile Natural Stacking:**
   - Complex 3-screen pinned desktop scrollytelling sequences must gracefully unpin on mobile devices (`max-width: 768px`).
   - In GSAP, wrap desktop triggers in `ScrollTrigger.matchMedia({ "(min-width: 769px)": () => { ... } })`.
   - On mobile, let the user scroll naturally through cards without hijacked viewport pinning.

2. **Split Screen to Stacked Sequence:**
   - 50/50 Desktop split (Sticky headline left, scrolling cards right) collapses on mobile to:
     - Short sticky category pill bar at top.
     - Vertically stacked cards underneath.

3. **Dense Data Tables to Mobile Card Sheets:**
   - Do not force horizontal scrollbars on multi-column tables if avoidable.
   - Transform rows into structured compact cards displaying primary data, with a tap to expand the full detail drawer.
