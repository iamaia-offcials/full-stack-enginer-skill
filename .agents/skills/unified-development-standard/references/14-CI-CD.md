# 14. CI/CD, software supply chain, and release artifacts

- `[CI-001] MUST` Set a risk-proportionate policy: run relevant fast lint/types/tests/build and secret checks on changes/before merge; run heavier integration/security/contract checks according to risk and before release. Infrequent low-risk changes may use a documented local or manual process that checks the exact release commit. Monthly runs do not replace pre-release checks. Save resources through caching, cancelling obsolete runs, and correct filters without skipping critical gates.
- `[CI-002] MUST` Give workflow tokens minimal `permissions`; keep secrets away from untrusted PR code. Do not use `pull_request_target` to run an untrusted checkout with privileges.
- `[CI-003] MUST` Pin external actions to full commit SHAs or follow a documented internal trusted-source/dependency policy; update pins under control. Example version values are not verified SHAs.
- `[CI-004] MUST` Link each release to its commit SHA and immutable artifact identifier/image **digest**. Verify source provenance and promote the built artifact to production without an undisclosed rebuild.
- `[CI-005] MUST` One chain owns CD: Actions calls the platform, or the platform subscribes to an approved registry image; **both must not independently** change the host.
- `[CI-006] MUST` Separate `build` and `deploy` permissions. Expose production secrets only to the production job/environment; prefer OIDC over long-lived keys where available.
- `[CI-007] MUST` Serialize deployments and applicable migrations per environment. Check health/readiness and smoke flows after deployment; on failure, use bounded rollback or an operational response.
- `[CI-008] SHOULD` Use container/dependency scans, license policy, SBOMs, and provenance attestations for elevated risk. Triage results instead of merely generating noise.
- `[CI-009] MUST` Use supported workflow/action/runtime versions. A floating `latest` is not the production source of truth.
- `[CI-010] MUST` Do not treat staging or rolling updates as unconditional zero-downtime guarantees. Check topology, proxies, stateful jobs, and sessions.

## Example container release pipeline
1. PR CI → checks.
2. Merge to main → commit-scoped build → registry digest.
3. Deployment control → pinned digest, environment secrets, migration lock → health/smoke.
4. Release note/update deployment manifest → observe; on failure, roll back **code** and assess data separately.

## Adoption by readiness
Minimal: checks under CI-001. Standard: reproducible artifacts and environment separation. Critical: stronger verification and release controls according to actual risk. Artifact format follows the platform; containers are optional.

## Workflow example
See `examples/github-actions-ci.node.template.yml`: a **template, not a ready-to-run workflow**. Replace SHA placeholders, commands, and versions using the project and verified sources.

For task-specific patterns and examples, read the relevant section of [practical formulas](../guides/PRACTICAL-FORMULAS.md).
