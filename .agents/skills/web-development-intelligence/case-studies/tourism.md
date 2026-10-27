# Case Study: Cinematic Tourism & Destination Experiences

Architecture for immersive destination storytelling, expedition planning, and travel booking.

## Business Context & Sensory Appeal

Tourism and luxury adventure travel are defined by **wanderlust, visual wonder, and trust**.
- **Primary Conversion Actions:** Inquire about an expedition, check seasonal dates, request customized route itinerary, book private charter.
- **Core Friction Points:** Logistics anxiety (visas, gear, packing), unclear pricing breakdowns, clunky mobile itinerary viewing.

## Advanced Motion & Scroll Interactions

Immersive travel experiences leverage modern browser scroll storytelling:
- **GSAP ScrollTrigger & Parallax Storytelling:**
  - Hero image uses subtle multi-plane parallax depth (foreground terrain at 1.15x scroll rate, midground at 1.0x, background mountains at 0.7x).
  - Pinned route map canvas: Container remains pinned for `300vh` of scroll distance while route waypoint highlights step sequentially through Day 1 to Day 7.
- **Mobile Adaptation & Unpin Rules:**
  - **CRITICAL:** On mobile screens (< 768px), `ScrollTrigger` pinned canvas sections MUST be dynamically unpinned using `ScrollTrigger.matchMedia()`.
  - The pinned desktop scrollytelling transforms into a natural vertical feed with day-by-day swipeable cards or an interactive collapsible accordion. Never pin the mobile viewport when content exceeds vertical height!

## Section Sequence Blueprint

1. **Cinematic Hero:** Fullscreen video/photographic hero + Headline ("Expeditions into the Untamed Arctic") + Interactive Destination & Season Selector widget.
2. **Curated Expedition Packages:** Card grid with route maps, duration, group limit, and pricing.
3. **Scrollytelling Itinerary (ScrollTrigger Pinned Experience):** Pinned map on left syncing with scrolling day-by-day highlights on right.
4. **Transparent Inclusions & Exclusions:** Clear dual comparison ("What's Included: Expedition guides, heated tents, polar gear" vs "What's On You: International flights, personal insurance").
5. **Safety, Guides & Conservation Credentials:** Arctic rescue certifications, satellite comms, leave-no-trace pledge.
6. **Custom Expedition Inquiry & Date Booking:** Multi-step reservation request with preferred departure window.
