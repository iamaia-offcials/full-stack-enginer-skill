# Design Anti-Patterns & AI Slop Registry

A definitive checklist of unconsidered defaults, AI tells, and interface defects to detect and eliminate.

## The Anti-Slop Registry

1. **Typography & Hierarchy Defects:**
   - ❌ *Single-Word Italic/Color Accent:* Randomly making one word in a headline neon purple or italic without brand rationale.
   - ❌ *Ornamental Ordinals:* Adding `01 / 02 / 03` numbered badges on feature cards that are not an ordered sequence.
   - ❌ *Eyebrow Clutter:* Sticking an all-caps, letterspaced tag (`FEATURES`, `ABOUT US`, `TESTIMONIALS`) above every single heading.
   - ❌ *Unreadable Line Measure:* Body text stretching across the full screen width (>100 characters).

2. **Color & Material Clichés:**
   - ❌ *Default AI Dark Mode:* Violet/indigo neon radial gradients on a generic `#0f172a` slate background.
   - ❌ *Default AI Light Mode:* Warm cream `#F4F1EA` with generic serif headings on modern digital software.
   - ❌ *Faux Glassmorphism:* Translucent cards with `backdrop-filter: blur(12px)` placed over complex text, destroying legibility.

3. **Layout & Structural Tells:**
   - ❌ *Forced Bento:* Placing three equal features in a forced bento grid where one box has 2 words and another has 50.
   - ❌ *Fake Product Chrome:* Surrounding screenshots with fake browser title bars (red/yellow/green dots) when unnecessary.
   - ❌ *Vague Slogan Copy:* "Supercharge your workflow", "Revolutionize your productivity", "The all-in-one platform for tomorrow".

4. **Technical & Accessibility Bugs:**
   - ❌ *iOS Safari Input Zoom:* Font size < 16px on form inputs, causing viewport jump.
   - ❌ *Disabled Submit Trap:* Setting `disabled` on form submit buttons during async requests, stripping focus and trapping keyboard users.
   - ❌ *Hover-Only Actions:* Hiding delete, edit, or menu triggers strictly behind `:hover`, rendering them inaccessible on touchscreens.
   - ❌ *Locked Viewports:* Setting `maximum-scale=1.0` or `user-scalable=no` (WCAG 1.4.4 violation).
   - ❌ *Ease-In Entrances:* Applying `ease-in` to modals or dropdowns, making them feel slow and laggy.
