# Package review and verification

Current review: **2026-10-27**. Scope: the English instructions, public documentation, installer, validation and distribution. This is the current evidence record, not a second product description. No application or production environment was audited.

## Changes and findings resolved

| Area | Finding | Resolution |
|---|---|---|
| Canonical content | Duplicate catalogs, legacy copies and versioned descriptions increased context and drift | One core entrypoint, canonical references with stable IDs, optional profiles, one primary README with translations |
| Language | Agent-facing content was mostly Russian | All 73 installed Markdown files are English, including descriptions, references, guides, templates and profiles; agents still answer in the user's language |
| Loading | Broad audit wording and ambiguous routing could cause full-corpus reads | Direct task links, relevant sections only, reuse already-read core, no recursive profile discovery; optional templates are not mandatory documents |
| Scope | Some workflows implied backend, containers, themes, localization or a new MVP regardless of need | Apply the relevant architecture and capabilities only; distinguish a first release from hypothesis-testing MVP work |
| CI policy | Local/manual allowance conflicted with separate mandatory pipeline wording | CI-001 governs cadence and exceptions; still verify the exact release commit/artifact |
| Input security | Format checks could be mistaken for injection or access protection | Separate format/length validation, parameterized SQL, context-safe output, and action/object authorization |
| Documentation | Existing product documents and current versus planned behavior needed clearer ownership | Update the canonical document in place, label history/plans, and record rule changes in existing change history |
| Examples | Broken profile table and a two-theme example could imply required features | Repaired the table; examples are conditional and illustrative |
| Distribution | Documentation languages must not inflate installed context | English core ZIP excludes all public README translations; repository archive includes them |
| Installation | Updates must preserve user edits and older copies | Managed hashes, refusal on modified/added files, explicit legacy adoption, retained backups, snapshot recheck and ordinary-error rollback |

The 280 rule IDs and their MUST/SHOULD/MAY levels match the pre-translation snapshot, in the same order within each reference. Conditions and wording were clarified; retaining IDs is not a claim that semantics are entirely unchanged.

## Context measurement

Measured with **tiktoken 0.14.0**, encoding **o200k_base**, against the local snapshot immediately before the English revision. Both snapshots were normalized from CRLF to LF before tokenization; each file was tokenized separately and totals were summed. Description measurements include the quoted description values, excluding names, wrapper schemas and runtime messages.

| Content | Before | After | Token reduction |
|---|---:|---:|---:|
| All 73 skill Markdown files | 41,872 | 34,200 | 18.3% |
| All 19 SKILL.md entrypoints | 11,366 | 8,816 | 22.4% |
| Core entrypoint alone | 903 | 857 | 5.1% |
| All 19 discovery descriptions | 987 | 557 | 43.6% |

The core description alone is 30 tokens under the same method. On-disk skill Markdown totals 166,791 bytes. README translations are excluded. The tokenizer was used only for this measurement; it is **not** an installer dependency.

These are combined translation/editing results, not an isolated language experiment or a benchmark of Gemini/Claude tokenizers. The full corpus is not intended to be loaded for every task. Actual context use depends on discovery metadata, selected references, repeated reads, tool output and the runtime. A smaller file does not prove better behavior, and these percentages do not predict session cost.

## Behavioral evaluation

An independent agent read the English core once and reused it for six bounded instruction-following scenarios. It selected only relevant profiles/references and reported no remaining conflict affecting those outcomes:

| Scenario | Observed decision from the instructions |
|---|---|
| Private-app button text change | Change the owner component/message and check relevant layout/accessibility; no SEO, backend, new theme or full product plan |
| Static public landing with an unknown future pixel | Apply relevant public-page SEO; leave the provider undecided; no invented ID, SDK or tracking traffic |
| CRM email field with PostgreSQL | Keep format/length, server authorization, SQL parameters and output safety separate; migration only if the schema actually changes |
| Solo first release with possible teams later | Mark teams as hypothetical and assess ownership/migration consequences; no automatic multitenancy or role builder |
| Header change with current header.md and an old plan | Update the current canonical document and distinguish historical plans; no header-v2.md |
| Audit without a repair request | Inspect and report evidence within scope; no fixes, publication or production changes |

This was a reasoning/behavioral review, **not** application implementation, blinded statistical evaluation, or a live run across supported agents. It does not establish a pass rate for future tasks. Repeat the [evaluation scenarios](../tooling/EVALUATION_GUIDE.md) in the target runtime when assessing real behavior.

## Executed checks

Environment: **Windows, Python 3.14**.

- `python tooling/validate_suite.py`: PASS, zero metadata/link/rule-ID errors.
- `python -m unittest discover -s tests -v`: 27 tests; 26 passed, one skipped because this host cannot create the generic test symlink. The separate Windows junction refusal test passed.
- Installer tests cover destinations and core dependencies, dry-run/no-op, preservation of local edits and added files, legacy adoption, source overlap, plan/apply changes, backups and rollback.
- Package tests cover reproducibility, a single skill manifest, included license/guides, excluded README translations, file limits and archive integrity.
- All five README translations preserve the eight executable Bash blocks from English, in order. Language navigation and local links pass validation. Arabic uses RTL prose with LTR command blocks. These checks are not independent native-speaker certification or a rendered-GitHub visual test.
- Source comparison: 73 skill Markdown files before and after; 280 rule IDs/levels retained; no remaining Cyrillic, Arabic or Chinese prose in the installed skill files. The instruction files were also reviewed for English meaning, not just script detection.

## Limits

Python 3.10 and Linux/macOS were not executed in this review. Installation paths and cloud-import instructions were checked against the official sources linked in the [README](../README.md), not by signing into every agent/account. No claim is made that every external standards URL was revalidated during translation.

Skills provide instructions, not runtime tools or account access. Static checks and bounded scenario reviews do not prove application security, legal compliance, search rankings or correctness in every model. Publication to GitHub and cloud installation are separate actions; this review does not claim they occurred.

