# Product, MVP, and foundation planning

Use for a new product, major initiative, or substantial architecture revision. Scale artifacts to the task and risk: a small landing page or bug fix does not need a full product program. Mapping future capabilities does not authorize implementing or specifying all of them in detail.

## Formula and detail

**Formula:** user problem and value → product vision and boundaries → capabilities, business rules, and journeys → confirmed facts and hypotheses → MVP as a complete testable flow → future impact on foundations → architecture and stack → stages, validation, and revision. Iterate when research or a prototype changes an earlier decision.

1. **Product vision:** audience, problem, value, useful outcome, business goals, constraints, success criteria, and unproven assumptions. Use facts from the request and project. Ask only questions that materially affect a decision and cannot be reliably inferred. A brief working-backwards or PRFAQ exercise can help; a corporate document is not required for every project.
2. **Known capability map:** roles and tasks, end-to-end journeys, key business objects and owners, lifecycle and permissions, integrations, data, known monetization, and applicable web/SEO/analytics concerns. Label confirmed, expected, hypothetical, and unknown items. Do not present ideas as approved scope. Show important dependencies and exclusions.
3. **Detailed MVP or first release:** for selected flows, specify preconditions/postconditions, inputs, rules and exceptions, roles and object-level authorization, states and transitions, invariants, sources of truth, integrations/errors/retries, acceptance criteria, and applicable nonfunctional requirements: security, privacy, accessibility, SEO/measurement, performance, operations, and recovery. An MVP handling real data still needs appropriate safeguards. For later features, outline the boundaries and invariants that affect present decisions; detail them early only to investigate a material risk or dependency.
4. **Release slices:** journey/story map → smallest complete, safe vertical flow that tests a named hypothesis and metric → next stage based on dependencies → ideas awaiting validation. An MVP is not mandatory for every project: when requirements are known or a full launch is required, define the first release accordingly. An MVP is not the same as a prototype and does not automatically prove demand.
5. **Learning plan:** question, method, available data sources, decision criterion, and owner. Do not invent interviews, metrics, or market evidence. Revise the map and priorities after validation. Do not promise an immutable plan or zero future rework.

## Foundations for future capabilities

**Decision formula:** likelihood of the future scenario + cost/risk of changing later + preparation cost now + uncertainty + maintenance cost → choose `implement now / preserve a boundary / defer / investigate`. This is qualitative reasoning, not arithmetic certainty. Record the rationale and review trigger. Investigate difficult-to-change decisions early: access and data ownership, identifiers, API commitments and customer data, payment/legal obligations, migrations, data residency, and platform constraints. Do not classify every future choice as irreversible.

| Future capability | Check before the MVP when relevant | Foundation if the risk is confirmed | Avoid without a demonstrated need |
|---|---|---|---|
| Teams and roles | Individual or organization ownership; who gains access; data migration | Consistent ownership and server authorization; a migration path based on known rules | A complete role builder or multitenant platform for a hypothesis |
| Payments | Expected pricing, provider, refunds, currencies, regulatory constraints, and risk | Exact monetary representation without binary floating point, price ownership, order transitions; provider validation before contracts | Connecting a payment service or storing payment data prematurely |
| Languages and SEO | Actual markets, localizable content, URLs, and search pages | Separate strings/content and define URL policy; plan translation and migration when justified | Translating into every possible language or adding hreflang without corresponding pages |
| Analytics and pixels | Goals, events, possible recipients, privacy, and consent | Event ownership and a safe integration point if useful at the current scope | Tags without a defined provider and applicable authorization/consent, or a custom event platform |
| Growth and integrations | Expected load and volume, external limits, migration cost | Clear boundaries and measurements, query-driven indexes, migrations, and recovery proportional to risk | Microservices, queues, or sharding solely for hypothetical growth |

**Example:** if near-term support for multiple teams is confirmed, the MVP can define record ownership and enforce it on the server from the start. Owner type and migration path depend on the confirmed rules. If teams are only an idea, record the risk and a possible migration path without inventing an organization model. In either case, evaluate cost and verify the permissions required by the current flow. Preparation does not guarantee that migration will never be needed.

## Stack, complexity, and reversibility

Start with current and confirmed future constraints: user platforms; data/transaction model and migrations; trust boundaries and personal data; integrations; indexing/rendering; response time, availability, and recovery; team skills; budget, maintenance cost, and support lifetimes. Keep the existing stack unless there is a reason to change it. When a stack decision is needed, compare two or three suitable options: eliminate those violating requirements, then assess tradeoffs and risks. Use a bounded spike with a success criterion for substantial uncertainty; do not present it as production-ready. Record significant, difficult-to-reverse decisions in an ADR: context, alternatives, reasons, consequences, and review conditions. Decisions can be reversed with migration costs accounted for. Verify versions and compatibility against current official documentation.

Assess complexity through working flows, rules and states, integrations, data sensitivity and migration, failure impact, user volume, operational requirements, and unknowns. Record evidence, risks, and validation for relevant factors. Give rough time ranges only with assumptions and uncertainty; screen count is not a system estimate.

## Deliverables and starting work

For a new initiative, capture the product map, facts/hypotheses, roles/flows and key invariants, first-release slice and later capabilities, dependencies and risks, foundation decisions, stack rationale, and validation plan at an appropriate level of detail. Use existing project documents or one concise plan where sufficient; do not create an empty document bundle.

Resolve critical unknowns affecting security, permissions, irreversible actions, or costly foundations before dependent implementation, or choose a safe bounded option. Style preferences, optional providers, and distant ideas should not block independent work. Do not invent user approval or perform unauthorized deployments or external changes.

Decision matrix: `future capability | status/source | first-release impact and constraints | change risk/cost | decision now | deferred work | review trigger | owner`. Later features remain provisional; first-release requirements must be testable. For releases involving money or sensitive data, include relevant security review and risk-based verification.

## Sources and applicability

- [AWS: Working Backwards and customer needs](https://docs.aws.amazon.com/pt_br/wellarchitected/latest/devops-guidance/oa.ti.6-prioritize-customer-needs-to-deliver-optimal-business-outcomes.html): articulate value before the technical solution.
- [Atlassian: story mapping](https://www.atlassian.com/agile/product-management/story-mapping): user journeys and release slices; [MVP and hypothesis testing](https://www.atlassian.com/agile/product-management/product-market-fit).
- [AWS: reversible and difficult-to-reverse decisions](https://docs.aws.amazon.com/wellarchitected/2024-06-27/framework/the-review-process.html); [Microsoft: design for evolution](https://learn.microsoft.com/en-us/azure/architecture/guide/design-principles/design-for-evolution).

These illustrate approaches; they do not establish that all large companies follow one process or endorse this suite's custom rules. Do not copy enterprise infrastructure into every project.
