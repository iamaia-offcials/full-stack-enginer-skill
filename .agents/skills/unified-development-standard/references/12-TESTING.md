# 12. Testing and quality assurance (QA)

- `[TEST-001] MUST` Prioritize tests by risk. Money, access, state, deletion, external effects, and migrations require negative, boundary, and concurrency tests for the risks present.
- `[TEST-002] MUST` Select test levels by change: unit tests for business rules, integration tests for boundaries, contract tests for contracts, and E2E tests for critical flows. Do not require every level for every change or substitute screenshots for behavioral verification.
- `[TEST-003] MUST` Test error handling, replay, out-of-order events, timeouts, cancellation, races, and partial failures wherever those risks exist.
- `[TEST-004] MUST` Use reproducible test environments and deterministic fixtures. A flaky test is a CI defect to fix, not permanently ignore.
- `[TEST-005] MUST` Follow CI-001 for gate selection and frequency. Before release, verify the exact commit/artifact being released. Do not silently bypass failing mandatory checks or report unrun checks as successful.
- `[TEST-006] MUST` For changed UI flows, check supported themes/devices, affected states, and accessibility. For substantial visual changes, compare against managed baselines when infrastructure exists.
- `[TEST-007] SHOULD` Use coverage as a diagnostic signal. Do not pursue an arbitrary percentage or treat high coverage as proof of correctness.
- `[TEST-008] MUST` Test fixtures and logs must not contain production secrets or real personal data without a justified, safe process.
- `[TEST-009] SHOULD` Keep local and CI test commands aligned. Do not report a pass without execution logs.

## Test matrix (adapt to the project)
| Category | Release conditions |
|---|---|
| Business invariants | Unit test + negative case |
| Database writes / migrations | Integration tests against the target database engine |
| Authentication/roles | Resource-level negative tests |
| External provider | Fake + contract/sandbox tests, retry checks |
| UI supporting two themes | Visual, keyboard, responsive checks in both |
| Production deployment | Readiness + smoke + rollback checks |

**Evidence rule:** A test file's existence is not verification. Record execution results for the changed commit.
