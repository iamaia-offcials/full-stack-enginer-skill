# 19. AI assistant and automated coding rules

- `[AI-001] MUST` Before editing, inspect the applicable repository instructions, task path, similar behavior, owning modules, tests, and configuration. Do not guess the existing architecture or read unrelated areas by default.
- `[AI-002] MUST` For substantial changes, define a bounded plan and acceptance criteria. A small edit needs a clear outcome and verification method. Label material unknowns; hypotheses are not confirmed requirements.
- `[AI-003] MUST` Keep the diff minimal. Avoid unrelated directory moves/refactors unless correctness or security requires them.
- `[AI-004] MUST` Check new API/UI/use cases for duplicate implementation and ownership. Do not create a second owner of business logic, an equivalent design component, or an independent CD pipeline.
- `[AI-005] MUST` Report exactly which commands/tests ran and their results. Never claim everything was checked without evidence.
- `[AI-006] MUST` Do not expose credentials, disable security checks to pass CI, or perform irreversible production actions without authority and required confirmations. Existing authorization remains valid within its scope.
- `[AI-007] MUST` When behavior depends on an external API/documentation/version, verify current official sources. Use supported stable versions for newly selected dependencies; do not turn an unrelated fix into a stack upgrade.
- `[AI-008] SHOULD` Run relevant `git diff --check`, lint, type, test, and build checks according to the change and available tooling. Summarize material risks/incompatibilities and distinguish implemented from untested behavior.
- `[AI-009] SHOULD` Break large changes into stages with intermediate contract checks; do not leave a production system partially switched over.

## Execution sequence
`Inspect → Locate owner → Understand invariants → Plan → Edit minimally → Test → Review diff → Report`.

Use the scoped loading and routing rules in `26-SKILL-ORCHESTRATION.md` when coordinating profiles; this sequence does not require loading every profile or reference.

## Reviewable reporting
Provide relevant file locations, actual verification commands/results, material risks, and an applicable rollback path. Do not describe unverified production behavior as complete. For small changes, a concise report is sufficient.
