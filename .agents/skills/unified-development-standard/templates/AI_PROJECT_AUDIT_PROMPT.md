# Prompt for an evidence-based project audit

Audit THIS repository using `unified-development-standard/RULES_INDEX.md` and applicable `references/*.md`.

1. Read the project instructions and entry points first: existing `AGENTS.md`, README, profile, and architecture index. Identify the requested audit scope and follow relevant links. Inspect ADRs, workflows, containers, migrations, UI tokens/themes, test configuration, and deployment/recovery runbooks only where relevant. Do not assume unseen components exist.
2. Identify the risk profile, actual technology, and inapplicable sections (N/A with a reason). Do not require databases, mobile support, or SEO where absent.
3. For each applicable MUST within the audit scope, record `Rule ID | PASS/FAIL/PARTIAL/UNKNOWN/N/A | evidence | concrete risk | remedy | priority`. Evidence may be `path:line`, a command and log, or a precisely named setting. If coverage is incomplete, state the unreviewed scope.
4. Investigate duplicate domain logic, competing API clients, overlapping business rules and UI components/tokens, module API bypasses, dependency cycles, and environment/CI/deployment conflicts. Similar-looking code is not a duplicate until its meaning is compared.
5. Check actual API, transaction, migration, authentication, authorization, idempotency, trust-boundary, and queue flows where present. Middleware alone does not prove security.
6. Inspect applicable UI routes for supported themes, contrast against actual backgrounds, keyboard/focus, responsiveness, localization, SEO, and performance. Identify checks requiring a browser or manual interaction.
7. Assess relevant Git rulesets, required checks, workflow privileges, supply chain, artifact pinning, deployment ownership, ingress, backups, and restore drills. Mark inaccessible remote settings or server behavior UNKNOWN.
8. Prioritize by demonstrated impact and likelihood: urgent exploitable security issues, data loss, or immediate production failure first; then material correctness, architecture, test coverage, and accessibility gaps; then maintenance improvements. Do not assign P0 solely because a finding belongs to security.
9. Keep the audit read-only unless fixes were requested. Do not report predictions as observed test results.

Update the existing canonical audit report. Use `docs/PROJECT_AUDIT.md` only if no project location exists and a saved report is requested. Include a concise summary, applicable-rule matrix, main findings, staged remedies, evidence, unknowns, and actual verification commands. All claims must be checkable. A focused audit does not require a repository-wide document bundle.
