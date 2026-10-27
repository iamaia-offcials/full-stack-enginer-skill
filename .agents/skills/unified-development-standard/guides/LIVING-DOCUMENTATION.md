# Living documentation

**Formula:** locate the source owner → distinguish plans from current behavior → change and verify → update the canonical document → check links and contradictions. Keep one source for each fact or contract, not one file for the entire project.

## When to write

- Before a substantial feature, record its purpose, rules, and acceptance criteria in the existing task or specification. Mark future behavior explicitly; a small edit does not need a new document.
- During implementation, clarify contracts, decisions, and open questions.
- With the code, update affected descriptions in the same PR or changeset. Implementation on a branch does not mean production availability; state the release or environment when that distinction matters.
- After release, update availability and operations when they change. Mark removed features and update their links.

## One current source

**Example:** a header is documented in `docs/features/header.md`. When its menu changes, edit that file in place and replace outdated claims; do not create `header-v2.md` or `header-final.md`. If a shared component document already describes it, update that section. Existing project names and structure take precedence over this example.

Find the existing source through the README or index, names and synonyms, code, and links. It may be a file or maintained wiki. Identify the domain owner and canonical source; avoid copying API schemas into several places. Update generated documentation through its source.

| Material | Purpose |
|---|---|
| Feature documentation | Actual behavior, audience, rules, limitations, and links to code/contracts |
| Task or plan | Proposed or ongoing work, status, and a link to the current description |
| API/schema | Exact field and constraint contracts; descriptions link to these |
| ADR | Reasons for a significant decision; mark superseded decisions and link to replacements |
| Git/release notes | Change history, not a competing current specification |

User instructions, technical references, and runbooks may serve different audiences in separate documents. Separate versions are appropriate for concurrently supported product or API versions with explicit scope and status. Do not copy the whole specification after every feature to create history.

## What to describe

Include useful information only: purpose, status, roles and permissions, inputs and outputs, main flow, states and errors, invariants, significant UX/security constraints, canonical contract links, and verification. Adapt the [feature template](../templates/FEATURE_DOCUMENTATION.md); omit irrelevant fields. Do not include secrets or real sensitive payloads.

## Existing duplicates

Compare documents with code, tests, and the relevant version or environment. The newest date does not prove accuracy. Code can also contain bugs: do not automatically rewrite a business requirement to match implementation. Consolidate verified facts into the canonical document, update links, and mark earlier material as historical. Before deletion, check consumers, purpose, and authorization; ADRs and regulated records are not disposable clutter.

Check links, examples, and status clarity. A link checker cannot establish semantic accuracy; label unverified claims. Further reading: [Diátaxis](https://www.diataxis.fr/application/), [Google Cloud ADR](https://docs.cloud.google.com/architecture/architecture-decision-records).
