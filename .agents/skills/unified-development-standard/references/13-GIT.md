# 13. Git, branches, commits, and code review

- `[GIT-001] MUST` In shared production repositories, protect the main branch from accidental/force pushes and deletion; configure PRs/required checks according to risk and host capabilities. Do not impose GitHub or a separate PR for every small change on a local prototype.
- `[GIT-002] SHOULD` Prefer trunk-based development with short-lived `feat/*`, `fix/*`, `refactor/*`, `docs/*`, and `chore/*` branches. Introduce `develop`/release branches only when separate support lines are needed.
- `[GIT-003] MUST` A PR explains why, what changed, affected modules/contracts, tests, and risks. Include migrations and rollback when release risk warrants them.
- `[GIT-004] SHOULD` Use Conventional Commits and squash merges when they improve a consistent history. Apply SemVer to versioned public interfaces/packages according to the product's adopted policy.
- `[GIT-005] MUST` Run checks against the correct commit/merge context. Do not merge a PR without confirmed results for mandatory checks.
- `[GIT-006] MUST` Solo developers perform self-review and checks according to CI-001. Do not require a nonexistent second reviewer.
- `[GIT-007] MUST` Hotfixes receive minimally sufficient real checks and follow a documented emergency procedure; simply uploading to a server is insufficient.
- `[GIT-008] SHOULD` Protect release tags; changelogs/release notes connect the SHA, artifact, and changes.
- `[GIT-009] MUST` Keep secrets, customer-data dumps, secret-bearing `.env` files, and large generated artifacts out of Git. Any justified storage exception for non-secret data/artifacts must be explicit; sanitized environment examples are allowed.

## Example workflow
`Issue → feat/123-description → PR → review/checks → squash → main → release artifact → deployment`. `staging` is an environment, not necessarily a separate branch.

## PR process
1. Keep the diff focused and include relevant tests.
2. Self-review, search for duplication, and check API/database/UI impact.
3. Run required checks and applicable security checks.
4. Merge and clean up the branch automatically where configured.
