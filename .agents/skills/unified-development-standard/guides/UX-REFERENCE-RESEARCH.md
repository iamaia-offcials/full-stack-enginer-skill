# UX references: learn decisions, adapt to the product

Read when selecting page architecture, comparing references or designing a substantial new journey. [UXR rules](../references/29-UX-REFERENCE-RESEARCH.md) are normative. Existing components and project constraints remain the starting point. Do not turn a text correction into a research program.

## Formula: need → operation → information → composition → test

1. Establish the audience's task, urgency and uncertainty from project evidence.
2. Determine what the business can actually complete online, through a manager or in person. Map this **per journey**: a company may combine several models.
3. Inventory available content and its owner: products, availability, prices, locations, service scope, real proof, terms and next steps. Label unknowns rather than filling them with plausible inventions.
4. Map each candidate block to `user question | reliable content | real action | prerequisite | owner`. Omit it when its purpose or evidence is missing.
5. Order by task-critical prerequisites, acquisition intent and risk before acting. Place relevant proof near the uncertainty it addresses. Do not infer above-the-fold position from scraped text or prescribe one scanning pattern to every page.
6. For a consequential uncertain page, compare genuinely different journeys/compositions and explain tradeoffs. Choose the simplest justified structure, using the established design system.
7. Verify a representative task and changed states. Record what was observed, assumed and still untested; revise with evidence.

### Offer model determines the legitimate action

| Confirmed facts | Appropriate path | Avoid |
|---|---|---|
| Selectable items, verified prices and availability; purchase is supported | Browse/search → relevant comparison → detail/terms → checkout | A contact form disguised as checkout or invented stock |
| Real products/specifications, negotiated price/terms | Catalog → shortlist/specification → contextual RFQ → manager | Fake instant prices or losing SKU/quantity context in a generic form |
| Bespoke service, no fixed inventory | Service fit/examples → actual process/proof → requirements/inquiry | Fictional bookable products, departures or property listings |
| Sales only at physical locations | Assortment/inspiration → location/hours → directions/contact | A cart or delivery promise the business cannot fulfill |
| Both direct and assisted offers | Clearly labeled purchase and consultation paths | Combining request and payment under one misleading CTA |
| Corporate story and independent catalog tasks | Clear navigation/cross-links and context transfer | An isolated catalog or a new subdomain for aesthetic reasons alone |

Priority is qualitative: `task necessity + uncertainty before action + acquisition intent + error cost`. It is a discussion aid, not a calibrated conversion score. Surface search only when searchable inventory exists and the task benefits. A sticky action is a hypothesis to test against small viewports, zoom, keyboard and safe areas, not a requirement.

### Three compositions, not three visual skins

- **Advisor-first:** clarify service/fit, then process and credible evidence, then a useful brief. Appropriate when scope depends on conversation or trust barriers dominate.
- **Explorer-first:** help users find/compare real options, then detail/terms and the supported next action. Appropriate when a meaningful assortment exists.
- **Split-path:** expose distinct tasks early, such as a company introduction versus catalog/RFQ, or reservation versus takeaway. Keep boundaries clear and allow relevant cross-navigation.

Different colors do not make structures materially different. Do not randomize section order for novelty or manufacture multiple concepts for an already agreed small change. Route/subdomain choices also depend on ownership, update cadence, authentication, SEO and attribution; use their existing rules where applicable.

## Contextual contrasts and task checks

| Situation | Useful structure or comparison | Verify |
|---|---|---|
| Real-estate agency with no public listings | Service/area expertise and a qualified client brief; compare advisor-led versus buy/rent/sell entry points | A visitor can state criteria and understand what happens next; no fictional property search |
| Physical grocery versus online delivery | Store discovery/hours/assortment versus service area, real categories and fulfillment | Find the right store or confirm delivery availability; do not conflate these tasks |
| Tailor-made Turkey travel | Destination inspiration and planning process versus a preferences-first inquiry; mark sample itineraries as examples | Understand consultation, inclusions and next steps without invented dates/prices |
| Wholesale catalog with a separate company site | Taxonomy/specifications and contextual RFQ; retain clear company/catalog navigation | Find a relevant SKU/specification and send its context, quantity and requirements |
| Country-only eSIM plans | Verified country coverage, device compatibility, activation/validity and actual terms | Choose a supported plan; no invented regions, unlimited data or recurring-fee claims |
| Restaurant reservations plus takeaway | Distinct visit and order journeys with relevant menu, location and timing | Book the intended visit or find supported ordering without confusing confirmations |

These contrasts are conditional reasoning examples, not current assertions about a named company's operations. Product details come from the target project's authoritative data.

## Selective atlas use

The supplied library contains **39 cases across six sectors**, **12 scenario comparisons** and **27 motion examples**. Canonical English records live in `assets/ux/` and `assets/motion/`; they are examples, not more mandatory rules. Use the bundled selector without loading the datasets into model context:

```bash
python scripts/reference_atlas.py --kind ux --niche tourism --limit 3
python scripts/reference_atlas.py --kind ux --id RW-020
python scripts/reference_atlas.py --kind scenario --id UX-S07
python scripts/reference_atlas.py --kind motion --id bottom-sheet
```

Paths are relative to the installed core folder. Use `--help` for filters. Without Python, locate the required ID in the relevant JSON file and read only that record. For motion, inspect a selected storyboard/GIF only when useful and supported. Use the [motion guide](MOTION-DECISIONS.md) for implementation decisions; educational overlays and simulated request states are not certified production components.

The [offline gallery](../examples/reference-atlas.html) is a generated human browsing aid using the same canonical data. Do not read its full HTML as skill instructions. Its UX miniatures are **original schematic diagrams**, not screenshots of the named websites; motion media are educational examples, not FPS evidence. Edit the canonical data and rebuild the gallery instead of maintaining parallel case descriptions.

## Evidence and visual literacy

The original source labels 36 cases primary text observations and three secondary review leads, dated 2026-10-27. These labels/dates are retained as supplied provenance, **not independently revalidated here**. All 39 have `visual_status: not-captured`; there are no live-site screenshots in that source package. Gallery previews depict the atlas interface, not the external companies.

Keep these labels separate:

- **Text-observed:** source-page content noted using text retrieval; no reliable pixel position or mobile behavior.
- **Visible:** an actual browser/screenshot observation tied to URL, date, viewport and state.
- **Hypothesis:** an analyst's explanation; a site owner has not necessarily confirmed the reason.
- **Proposal:** a possible adaptation to the target product.
- **Unverified:** unavailable visual, operational, accessibility, performance or outcome evidence.

When a current fact matters, revisit the relevant official page/flow with available tools. Treat secondary cards as inspection leads. Record timestamp, locale, viewport, route/state, authentication/consent conditions and errors for genuine visual research; do not label diagram viewing as a site visit. Use permitted public access and respect privacy and image rights before redistribution.

For a useful pairwise comparison, examine the dominant task, actual fulfillment, density, action labels, navigation, proof placement, comparison information and mobile affordances. Extract transferable ideas and reasons **not** to copy. Reuse principles rather than another brand's exact typography, imagery, motion, claims or content. If visual tools are unavailable, deliver a bounded content/IA proposal and mark visual checks NOT_RUN.

Use first-click/task checks or existing instrumentation to test relevant questions. Do not invent interviews, conversion gains, field performance or market evidence. Update the existing current feature/reference record; retain old evidence as clearly historical, not as a competing version.

## Primary research and limits

- [ONS: designing content for user needs](https://service-manual.ons.gov.uk/content/writing-for-users/user-needs): evidence-based needs and content sketches.
- [NN/g: text scanning patterns](https://www.nngroup.com/articles/text-scanning-patterns-eyetracking/): reading depends on task, content and layout.
- [Baymard: product listing information](https://baymard.com/research-articles/product-listing-information): comparison information in the product-list context.

These sources support specific research principles; they do not validate every custom rule, named-site observation or proposed composition in this atlas. The library expands accessible reference material; it does not train model weights or replace project verification.
