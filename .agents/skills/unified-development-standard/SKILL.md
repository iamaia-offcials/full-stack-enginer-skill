---
name: unified-development-standard
description: "Use when planning, implementing, reviewing or maintaining a software product, especially decisions spanning business rules, architecture, security, interfaces, data and delivery."
---
# Unified Development Standard

Apply engineering decision rules to the requested scope. This core works alone; optional `uds-*` profiles add domain workflows. Paths below are relative to this file. Follow these English instructions while answering in the user's language.

## Workflow

1. Inspect relevant project instructions, existing code and current documentation. Identify the outcome, affected behavior and owner of the logic. Reuse established solutions before adding abstractions.
2. Match effort to risk. A small edit needs existing context and a relevant check, not a new product plan. For a new product, establish the target vision and first release; build foundations for confirmed constraints, not speculative features. Ask only about consequential unknowns that available evidence cannot resolve; state safe assumptions.
3. Select the relevant starting point below. Read only affected sections and follow additional links when they resolve a concrete dependency or uncertainty. Do not preload the index, all references, templates or external sources. Reuse already-read context unless it changed. An absent feature is usually not applicable, not work to add.
4. Implement within the request. Keep protected business decisions, authorization, secrets and invariants on the trusted side of the product's architecture. Client validation helps UX; it cannot enforce a server trust boundary.
5. Update the existing canonical description when behavior or contracts change. Separate current, planned and historical states; do not create competing version-suffixed feature documents.
6. Run checks proportional to the change. Report outcomes, evidence and remaining uncertainty concisely. A review alone does not authorize fixes; installing a skill does not authorize publication or production actions. Never claim unavailable tools, unread rules or unrun checks.

## Choose a starting point

| Task | Read when needed |
|---|---|
| Product, first release/MVP, stack, complexity | [Planning guide](guides/PRODUCT-AND-MVP-PLANNING.md) |
| System boundaries | [Architecture](references/03-ARCHITECTURE.md) |
| Refactoring, ownership, duplication | [Code quality](references/04-CODE-QUALITY.md) |
| Backend, APIs, integrations | [Contracts](references/05-API-INTEGRATIONS.md) |
| Database, queries, migrations | [Data](references/06-DATA-DATABASE.md) |
| Trust boundaries, access, input, privacy | [Security](references/07-SECURITY-PRIVACY.md) |
| Frontend behavior and components | [Frontend](references/08-FRONTEND.md) |
| Styles, tokens, interface system | [Design system](references/09-DESIGN-SYSTEM.md) |
| Keyboard, semantics, assistive technology | [Accessibility](references/10-ACCESSIBILITY.md) |
| Public websites, SEO, analytics/pixels | [SEO and analytics](guides/SEO-ANALYTICS-PLANNING.md) |
| Tests and regression risks | [Testing](references/12-TESTING.md) |
| Git, CI/CD, delivery | [Git](references/13-GIT.md), [CI/CD](references/14-CI-CD.md) |
| Runtime incidents or performance | [Observability](references/16-OBSERVABILITY.md), [Performance](references/17-PERFORMANCE.md) |
| Feature documentation | [Living documentation](guides/LIVING-DOCUMENTATION.md) |
| Mobile, dependencies, other domains | [Rule index](RULES_INDEX.md): select the affected domain |

For rule conflicts or exceptions, use [governance](references/00-GOVERNANCE.md). For explanations, use [decision formulas](guides/PRACTICAL-FORMULAS.md); for standards research, [primary sources](EXTERNAL_SOURCES.md). References are normative; guides explain; templates are optional starting points, not a required document set.

If a relevant profile is already loaded, follow its workflow with the needed core rules. Do not restart profile selection or load sibling profiles recursively. The core remains sufficient when no profiles are installed.
