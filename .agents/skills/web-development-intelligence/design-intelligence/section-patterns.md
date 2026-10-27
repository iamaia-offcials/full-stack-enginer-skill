# Section Patterns & Component Blueprints

Detailed architecture and design criteria for primary page sections.

## Key Section Blueprints

1. **Hero Section Archetypes:**
   - **The Product In Action:** Punchy value proposition on the left (50%), interactive live app mockup or 3D product showcase on the right (50%).
   - **The Editorial Statement:** Massive typography (72px+ / 5vw+) centered or left-aligned, tight tracking (-0.02em), cinematic background photography or subtle canvas animation.
   - **The Interactive Hook:** Hero featuring an immediate interactive calculation, selector, or demo (e.g. "Select your destination" for travel/eSIM; "Calculate your savings" for fintech).

2. **Feature & Capability Sections:**
   - **The Narrative Walkthrough:** Alternating left-right blocks pairing short copy with interactive demonstrations or videos.
   - **The Tabbed Workflow:** Segmented controller switching views of real product interfaces with smooth crossfades.
   - **The Comparison Matrix:** Clean tabular layout contrasting current painful alternatives against the streamlined modern solution.

3. **Social Proof & Evidence Blocks:**
   - **Logo Wall:** Monochrome, visually balanced logos (normalized to equal optical surface area, not uniform bounding pixel boxes).
   - **High-Impact Testimonials:** Real client photographs, verified company names, specific metrics achieved ("Reduced turnaround by 42%"), avoid generic platitudes.
   - **Live Metric Counters:** Big numbers with concise explanatory captions.

4. **Actionable FAQ & Risk Reversal:**
   - Accordion-based layout with clean semantic disclosure (`<details>` / accessible ARIA).
   - Direct, transparent answers addressing the top five purchase objections.
