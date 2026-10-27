# Motion Design & Transition Physics

Bring digital interfaces to life with purposeful, physics-informed animation that clarifies spatial relationships.

## Frequency-to-Motion Decision Matrix

| Interaction Frequency | Motion Policy | Target Duration | Easing / Physics |
|---|---|---|---|
| **100+ times/day** (Shortcuts, command bar) | **Zero animation (0ms)** | Instant | No motion. Animation here breeds user fatigue. |
| **Tens of times/day** (List items, dropdowns) | **Micro-motion** | 100–140ms | `cubic-bezier(0.16, 1, 0.3, 1)` |
| **Occasional** (Modals, sheets, drawers) | **Standard transition** | 150–220ms | Decelerating `ease-out` or near-critically damped spring |
| **Rare / Narrative** (Onboarding, celebration) | **Authored choreography** | 300–600ms | Staggered sequence, custom spring |

## Directional Easing Rules

- **Entrances:** Always use decelerating **`ease-out`** (`cubic-bezier(0.16, 1, 0.3, 1)`). Immediate visual feedback upon trigger, gently settling at rest. **Never use `ease-in` for entrances.**
- **Exits:** Fast `ease-in` or quick `ease-out` (departure can be 20–30% faster than arrival).
- **On-Screen Relocations:** `ease-in-out` (`cubic-bezier(0.65, 0, 0.35, 1)`).

## Spring Physics Parameters

- **Apple Response/Damping:**
  - `response`: duration equivalent (`0.3s` for snappy controls, `0.5s` for sheets).
  - `dampingRatio` (ζ): `1.0` = critically damped (zero bounce); `0.75–0.85` = smooth organic settling; `< 0.6` = underdamped (avoid on productive UI).

## Accessibility & Reduced Motion

- **`prefers-reduced-motion` Mandate:** Every motion system must respect the operating system's reduced motion setting.
  ```css
  @media (prefers-reduced-motion: reduce) {
    *, ::before, ::after {
      animation-duration: 0.01ms !important;
      animation-iteration-count: 1 !important;
      transition-duration: 0.01ms !important;
      scroll-behavior: auto !important;
    }
  }
  ```
- In JavaScript (Motion / GSAP): check `window.matchMedia('(prefers-reduced-motion: reduce)').matches` and swap out spatial translation animations for subtle opacity fades or instantaneous state changes.
