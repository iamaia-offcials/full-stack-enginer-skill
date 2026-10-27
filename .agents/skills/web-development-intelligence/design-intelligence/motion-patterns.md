# Motion Patterns & Choreography Blueprints

Practical implementations of complex motion sequences across key UI scenarios.

## Motion Blueprints

1. **Coordinated Section Entrance (Stagger):**
   - Headline appears first (`y: 20 -> 0`, `opacity: 0 -> 1`, duration `180ms`, `ease-out`).
   - Supporting copy follows with a `60ms` stagger delay.
   - Action buttons and cards enter in cascade (`stagger: 0.08s`).
   - Total sequence duration capped at `400ms` so user is never waiting.

2. **Pinned Horizontal Scroll Showcase:**
   - Vertical scroll scrubs a horizontal reel of case studies or product details.
   - Pin container using GSAP ScrollTrigger:
     ```javascript
     gsap.to(".horizontal-track", {
       xPercent: -100 * (panels.length - 1),
       ease: "none",
       scrollTrigger: {
         trigger: ".pinned-wrapper",
         pin: true,
         scrub: 1,
         end: () => "+=" + track.offsetWidth
       }
     });
     ```

3. **Drawer & Sheet Gestures:**
   - Sheet follows finger 1:1 on vertical drag.
   - On release: if velocity > 500px/s or dragged past 40% height, dismiss; otherwise spring back to detent.
   - Spring: `response: 0.35s`, `dampingRatio: 0.82`.
