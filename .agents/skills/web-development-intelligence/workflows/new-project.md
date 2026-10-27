# Workflow: Green-Field Project (From Scratch)

Full 9-stage engineering workflow for creating a new commercial website or web application.

## Sequence of Execution

1. **Stage 1: Business Understanding & Qualification**
   - Identify commercial model: Lead generation, E-commerce, Local hospitality, B2B wholesale, or Digital utility.
   - Define the single primary conversion action (e.g. table reservation, quote request, purchase).
   - Determine target audience expectations and trust barriers.

2. **Stage 2: Information Architecture & Sitemaps**
   - Map route hierarchy (Home, About, Services, Case Studies, Contact/Booking).
   - Design navigation layout (Sticky minimal navbar, mobile drawer).
   - Establish content hierarchy using the Inverted Pyramid model.

3. **Stage 3: Reference & Benchmark Research**
   - Run `node scripts/search-references.mjs --industry <industry> --category hero`.
   - Study 2–3 award-winning benchmarks from `libraries/websites.json`.
   - Identify applicable components from `libraries/components.json`.

4. **Stage 4: Design Direction & Token Definition**
   - Choose typeface pairing (e.g. Serif display + Clean geometric sans body).
   - Define color roles: `--background`, `--surface`, `--text-primary`, `--text-muted`, `--accent-primary`.
   - Establish spacing scale (4px, 8px, 16px, 24px, 32px, 64px, 96px).

5. **Stage 5: UI/UX Composition & Section Construction**
   - Assemble page sections block-by-block based on user decision triggers.
   - Apply anti-slop rules: no decorative numbering, no single-word neon italics, no generic slogan titles.

6. **Stage 6: Motion Design & Choreography**
   - Apply frequency rules: 0ms for frequent shortcuts; 100–150ms for routine navigation; 150–220ms ease-out for modals/drawers.
   - Configure GSAP ScrollTrigger or Motion springs with proper mobile unpinning.

7. **Stage 7: Production Implementation**
   - Implement clean TypeScript components with semantic HTML.
   - Enforce 16px mobile input floor and `min-width: 0` overflow defenses.

8. **Stage 8: Quality Assurance & Multi-Viewport Verification**
   - Smoke test critical flows at 360px, 390px, 768px, 1024px, 1440px.
   - Verify keyboard operability, focus rings, and screen-reader labels.
   - Check Core Web Vitals (LCP, INP, CLS).

9. **Stage 9: Polish & Refinement**
   - Run `node scripts/validate-design.mjs` to catch any remaining layout or contrast defects.
