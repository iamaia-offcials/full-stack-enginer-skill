# 18. Documentation and architectural decisions

- `[DOC-001] MUST` Production documentation covers startup, configuration, architecture/modules, and applicable migrations, deployment/recovery, API contracts, and significant decisions (ADRs). Scale the document set to the system.
- `[DOC-002] MUST` Update code and documentation in the same PR when public contracts, startup, environments, or business invariants change.
- `[DOC-003] MUST` An ADR records context, choice, alternatives, consequences, date, status, and reconsideration triggers. It must not retrospectively advertise a tool.
- `[DOC-004] MUST` Document runtime variables in `.env.example` **without secret values**, including whether required and where values come from; use the platform equivalent where applicable.
- `[DOC-005] SHOULD` Keep documentation near code and check broken local links/inconsistencies in CI. Architectural decisions must not exist only in chat.
- `[DOC-006] MUST` Keep startup, test, build, lint, migration, and deploy/rollback commands consistent between README and automation where those operations exist.
- `[DOC-007] SHOULD` Short comments explain why instead of repeating an obvious line's behavior.

## Keep feature documentation current
Find the existing canonical document/section and source of facts for the feature or area. Update that document when behavior changes; clearly separate plans and unimplemented features from current behavior. Do not create a competing description for every edit. Keep history in Git/release notes and relevant ADRs; explicitly label concurrently supported product versions. When code and documentation disagree, inspect both and report the discrepancy. See [living documentation](../guides/LIVING-DOCUMENTATION.md) for wiki workflows and existing duplicates.

## Example project files
```text
README.md
AGENTS.md
PROJECT_PROFILE.md
docs/
  PRODUCT.md
  ARCHITECTURE.md
  API.md
  SECURITY.md
  OPERATIONS.md
  adr/0001-*.md
```
This is an example, not a required file list. Do not add empty documents to a static site; file existence does not replace accurate, verified content.
