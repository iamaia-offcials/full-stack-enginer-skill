# 04. Code quality, DRY, types, dependencies, and refactoring

- `[CODE-001] MUST` Before writing a function/service/component, search for equivalents by terminology, routes, usage, types, and tests. One business rule has one canonical implementation.
- `[CODE-002] MUST` Distinguish DRY from abstracting similar-looking lines. Semantically different rules can remain independent. Boundary shape validation and domain invariants are not harmful duplication.
- `[CODE-003] MUST` Do not keep active `old/new/final/v2` implementations of the same behavior without a bounded migration plan and removal deadline.
- `[CODE-004] MUST` Use domain-specific names, explicit inputs/outputs, predictable errors, minimal side effects, and clear transaction boundaries.
- `[CODE-005] MUST` Use formatting, linting, and type checks/static analysis where supported by the language/stack; their execution and CI requirements follow CI-001. Do not hide errors behind broad `ignore`, `any`, `as unknown as`, or disabled rules without a reason.
- `[CODE-006] SHOULD` Keep functions small and coherent. Long functions/modules prompt investigation, not mechanical line limits.
- `[CODE-007] MUST` Assess each new runtime dependency for maintenance, licensing, security, size, alternatives, and migration cost; commit its lockfile where supported.
- `[CODE-008] MUST` Refactoring changes observable behavior only when the task requires it. Protect critical logic with contract/characterization tests before refactoring.
- `[CODE-009] SHOULD` Remove unused exports, flags, and comments that repeat the code. Avoid parallel configuration in `.env`, YAML, and constants without explicit generation.
- `[CODE-010] MUST` Values with units (money, intervals, sizes) have unambiguous semantics. Represent money as integer minor units or decimals with defined rounding.

## AI rule
Do not satisfy a request by copying an existing use case into a new folder. First inspect `rg -n` results, imports, tests, and ownership. Include findings in the PR or summary when duplication is a real risk.

## Review checklist
No copied logic, cyclic imports, or hidden global state; correct error contract; edge-case tests; justified dependencies; only necessary modules changed.
