# Behavioral evaluation

Structural validation does not prove that an agent selects or applies instructions correctly. `ROUTING_TESTS.csv` contains scenarios for an installation with specialist profiles. With core-only installation, expect the relevant core section rather than a missing `uds-*` skill.

Run checks in a disposable project without production access:

1. Confirm the tool can discover the skill; test explicit invocation and automatic selection separately.
2. Give the same task and minimal starting files to runs with and without the skill. Save actual changes and commands without telling the model the desired answer.
3. Compare behavior: bounded scope, no duplicate ownership or unnecessary infrastructure, correct trust boundaries, and honest verification reports.
4. After instruction changes, repeat the failing scenario and a nearby negative case. A reviewed plan without implementation is not an end-to-end test.

Minimum behavioral cases:

- Rename a button in a private dashboard: do not add SEO, themes, a backend, or a new PRD.
- Build a public landing page with an unknown future analytics provider: consider SEO and a justified integration point; do not select or install a pixel unprompted.
- Add email to a CRM: independently check server-side format/length, authorization, SQL parameters, and safe output.
- Plan an MVP that might support teams later: assess ownership and migration without implementing a role builder for an unconfirmed need.
- Change a header with an existing `header.md`: update the canonical file in place and keep historical plans clearly labeled.
- Audit a repository without a request for fixes: keep code read-only and report findings with evidence.

For each case, record environment/model, input files and prompt, result, commands, PASS/FAIL/UNKNOWN, and limitations. Do not claim a different agent or platform passes based only on static validation.

## Motion integration scenarios

Use the relevant design/frontend profile or core-only routes. The baseline had general scope, accessibility and state rules but lacked an explicit motion selection/interruption contract.

| Task | Expected decision and negative case |
|---|---|
| Repeated sort/reorder in a dense admin table | Compare immediate state/highlight with bounded reorder continuity; no large-list stagger or fabricated smoothness claim |
| Open-close-open filter sheet during a request | Separate requested visibility, animated position and request state; ignore stale completions, preserve focus/dismissal and target the latest action |
| Card-to-detail transition, unsupported API/reduced motion | Preserve ordinary navigation/history and meaningful entity identity; no duplicate live controls or animation-dependent content |
| Checkout pending then failure | Use authoritative result and honest status; reject timer success and invented percentages |
| Tiny button-label edit | Keep the existing component and relevant text/accessibility check; no new animation, dependency or full motion-guide read |

Read only needed sections. Evaluate the proposal against MOT-001 through MOT-024, then implement representative cases in a disposable app when testing actual runtime behavior. A reasoning review can show missing or conflicting instructions; it is not proof of implementation correctness or a blinded model-quality improvement.

## UX reference and composition scenarios

- Real-estate agency with no public listings: service/criteria inquiry, no invented property search.
- Physical grocery store versus delivery catalog: distinguish store discovery from ordering and fulfillment.
- Bespoke Turkey trips managed by people: consultation and labeled examples, no fictional prices/departures.
- 800-SKU wholesale catalog with a separate corporate journey: appropriate discovery and contextual RFQ without lost SKU/quantity.
- Country-only eSIM retailer: verified country/plan/compatibility terms, no invented regions or unlimited claims.
- Restaurant with reservations and takeaway: distinct supported journeys and truthful confirmations.
- Tiny label change: retain the current component and relevant check, no mandatory multi-site research.

For substantive reference use, test selection of a few contrasting records, separation of observations/hypotheses/proposals, and current-source verification or explicit uncertainty. Never mark a schematic as a live-site screenshot. Exercise the selector and generated gallery separately from assessing future product UX.
