# 01. Product discovery

## Purpose
For a new product, establish who uses it, why, and how before choosing screens or an ORM. Test critical assumptions and define success.

- `[DISC-001] MUST` When planning a new product, identify its audience, problem, main scenarios, measurable outcome, and constraints. A short description is sufficient for a small initiative.
- `[DISC-002] MUST` Separate facts, assumptions, and open questions. Neither developers nor AI may invent disputed product rules.
- `[DISC-003] MUST` Define the first release's scope, or an MVP's scope when testing a product hypothesis: inclusions, exclusions, dependencies, and applicable constraints. An MVP is not a mandatory stage for every project.
- `[DISC-004] SHOULD` Validate important hypotheses with users/data rather than design intuition alone.
- `[DISC-005] MUST` Identify user groups with specific needs, access rights, sensitive data, irreversible actions, and retention/deletion requirements.
- `[DISC-006] SHOULD` Separate product metrics (such as completion rate) from technical metrics (p95, error rate). Server metrics do not replace interface quality measures.

## Outputs
Update the existing product document (for example, `docs/PRODUCT.md`) with key user journeys, roles, hypotheses/risks, success criteria, and first-release/MVP boundaries. Create a document only when needed. Spikes/prototypes can precede these decisions; do not present them as a finalized design.

## Readiness check
- [ ] The user problem addressed by the first release or MVP is clear.
- [ ] Each significant scenario has a starting point, successful outcome, and error cases.
- [ ] Product exclusions are recorded.
- [ ] Assumptions and legal questions are not presented as resolved.

For product, MVP, and architectural foundations, see [product and MVP planning](../guides/PRODUCT-AND-MVP-PLANNING.md).
