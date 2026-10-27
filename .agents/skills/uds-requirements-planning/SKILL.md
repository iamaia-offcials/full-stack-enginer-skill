---
name: uds-requirements-planning
description: "Use when defining requirements, acceptance criteria, feature scope, estimates, roadmaps, sprint work, or a first release/MVP; not for a trivial isolated edit."
---
# Requirements and planning

## Inputs
Goal, constraints, known decisions, risks, stakeholders, and expected user scenarios.

## Procedure
1. Define in-scope, out-of-scope, assumptions, and dependencies. Do not invent missing requirements.
2. Describe main roles/use cases and their necessary UX, data, and security behavior.
3. Separate functional requirements from relevant nonfunctional requirements: response time, recovery, security, accessibility, and scale.
4. For product/release planning, describe the known vision and future capability map, separating facts from hypotheses. Define the first release or an MVP when hypothesis validation is the goal, using complete vertical scenarios. Detail that scope's business rules and future dependencies/risks affecting foundations. Use core `guides/PRODUCT-AND-MVP-PLANNING.md` when relevant and available; a feature task does not require a new MVP.
5. Break work down by outcomes with testable Given/When/Then or equivalent acceptance criteria.
6. Define proportionate Ready/Done criteria and dependencies; estimate uncertainty separately from effort.
7. When planning a website, establish whether search traffic and future measurement matter. If relevant, use core `guides/SEO-ANALYTICS-PLANNING.md`; record assumptions, required events, and possible integrations without inventing providers or IDs.
8. Check relevant empty/error states, roles/permissions, supported locales, operations, and migrations.

Document product/substantial-feature requirements before implementation. Update the existing canonical document in place as behavior changes, separating plans from implemented behavior. Use core `guides/LIVING-DOCUMENTATION.md` when available.

## Output and verification
Provide a proportionate spec/PRD with goals, scope, user stories, acceptance criteria, relevant NFRs, phases/MVP only when applicable, dependencies, and risks. Estimates are not guarantees; requirements must be testable.

Use current sources and available research tools when validating hypotheses. Markdown/issues/ADRs are sufficient; a paid planning service is not required. Preserve user requirements instead of replacing them with another skill's template, and do not invent deadlines.
## Core rules
Use the sibling [core workflow](../unified-development-standard/SKILL.md) once per context; reuse it if already read. Then read only relevant sections of: 01-PRODUCT-DISCOVERY, 02-REQUIREMENTS, 21-DECISION-PROFILES. Apply core 00-GOVERNANCE scope. Do not recursively rediscover profiles/core or load the full corpus for a local edit. If core is unavailable, report that limitation without claiming compliance with unread rules.

