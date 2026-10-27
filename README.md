# Full Stack Engineering Skill

[English](README.md) · [Русский](docs/i18n/README.ru.md) · [Español](docs/i18n/README.es.md) · [العربية](docs/i18n/README.ar.md) · [Türkçe](docs/i18n/README.tr.md) · [简体中文](docs/i18n/README.zh-CN.md)

**A portable engineering standard for AI assistants: decision rules, explanations and examples for planning, building and maintaining software.**

The main skill, `unified-development-standard`, works on its own. It helps an agent understand a product, choose a suitable stack and implement the requested scope with relevant checks. A copy edit should remain a copy edit, not become a full audit.

## What it covers

- Product vision, business rules, first release/MVP, stack selection and complexity.
- Architecture, ownership of logic, backend, APIs and integrations.
- Validation, authorization, secrets and trusted enforcement of business invariants.
- Database constraints, transactions, indexes, migrations and recovery.
- Frontend, maintainable styles, accessibility and responsive interfaces without prescribing a brand.
- UI motion: contextual pattern selection, interruption/reversal, reduced motion, usable fallbacks and truthful progress.
- UX reference literacy: 39 supplied website studies, 12 conditional page compositions and 27 motion examples with storyboards/GIFs, selected by task and actual business model.
- Technical SEO and planning analytics/pixels before connecting services.
- Git, cost-aware CI/CD, containers when appropriate, releases and operations.
- Living documentation: update the current feature document; distinguish plans and history.

Decision pattern: **condition → decision → reason → example → verification**. Email format validation, parameterized SQL, safe rendering and authorization solve different problems; a character blacklist cannot replace them.

## Context and language

All installed instructions are in **English**. Agents should still answer in your language. The entrypoint routes to the relevant sections; it does not require reading all 30 references. One self-contained core is installed by default; 18 specialized profiles are optional. README translations stay outside the installed skill. Preserved motion artwork retains its original captions; English explanations accompany it.

The [reference guide](.agents/skills/unified-development-standard/guides/UX-REFERENCE-RESEARCH.md) explains selective CLI lookup and the [offline gallery](.agents/skills/unified-development-standard/examples/reference-atlas.html). Open the HTML locally after cloning/downloading; GitHub's file view shows source code. UX diagrams are schematics, not live-site screenshots. Supplied observation dates are not fresh verification. Edit canonical JSON records and run `scripts/reference_atlas.py --build-gallery` from the core folder to regenerate the derived gallery; use `--check-gallery` to detect drift.

English can use fewer tokens with some tokenizers, but savings depend on the text and model. Selective reading and removing duplication matter as well. [Review results](docs/REVIEW.md) distinguish measured text sizes/token counts from actual runtime behavior.

## Quick installation

Requires **Python 3.10+**, with no pip dependencies. Use `py` on Windows or `python3` on Linux/macOS if that is your interpreter command. Git is needed for cloning; alternatively use GitHub **Code → Download ZIP** and extract it.

```bash
git clone https://github.com/iamaia-offcials/full-stack-enginer-skill.git
cd full-stack-enginer-skill
python tooling/install.py --agent codex --scope user
```

The installer copies local files. It does not download dependencies, access accounts or modify `AGENTS.md`, `CLAUDE.md` or `GEMINI.md`.

To install into an existing project:

```bash
python tooling/install.py --agent codex --repo "/path/to/my-project" --dry-run
python tooling/install.py --agent codex --repo "/path/to/my-project"
```

On Windows, use a path such as `"C:/dev/my-project"`. Source and destination must not overlap: do not target this suite's own directory.

## Agent compatibility

| Tool | `--agent` | Project directory | User directory |
|---|---|---|---|
| Codex | `codex` | `.agents/skills/` | `~/.agents/skills/` |
| Claude Code | `claude` | `.claude/skills/` | `~/.claude/skills/` |
| Gemini CLI | `gemini` | `.gemini/skills/` | `~/.gemini/skills/` |
| Antigravity App / IDE | `antigravity` | `.agents/skills/` | `~/.gemini/config/skills/` |
| Antigravity CLI | `antigravity-cli` | `.agents/skills/` | `~/.gemini/antigravity-cli/skills/` |
| Other compatible agents | `generic` or `--target` | Agent-specific | Agent-specific |

Choose the command for your tool:

```bash
python tooling/install.py --agent claude --scope user
python tooling/install.py --agent gemini --repo "/path/to/my-project"
python tooling/install.py --agent antigravity --scope user
python tooling/install.py --target "/path/to/another-agent/skills"
```

Avoid installing duplicate copies in directories the same agent discovers. Gemini also supports `.agents/skills`, so a shared Codex installation may already be visible. Check your agent's skills list, then explicitly ask it to use `unified-development-standard`. Refresh discovery or start a new session if necessary. Copying files and confirming model use are separate checks.

Paths were checked against official documentation on 2026-10-27: [Codex](https://learn.chatgpt.com/docs/build-skills), [Claude Code](https://code.claude.com/docs/en/skills), [Gemini CLI](https://geminicli.com/docs/cli/skills/), [Antigravity](https://antigravity.google/docs/skills). These interfaces can change; a live run in every platform is not claimed.

### Lovable and cloud interfaces

In Lovable, use **Workspace settings → Skills → Add → Import from GitHub**, then select the [core skill folder](https://github.com/iamaia-offcials/full-stack-enginer-skill/tree/main/.agents/skills/unified-development-standard). Workspace owner/admin access is required according to [Lovable's documentation](https://docs.lovable.dev/features/skills). Alternatively, use **Upload ZIP**.

Build the portable archive:

```bash
python tooling/package.py
```

The result is `dist/unified-development-standard.zip`, containing the entrypoint, references, guides, examples and license. Import the complete package: `SKILL.md` alone is insufficient. Installing into Claude Code does not install a skill into a Claude cloud account; use the account's supported import. This installer does not manage cloud accounts.

For an agent with file access but no native skills support, ask it to read the core `SKILL.md` and relevant linked sections. Without files or import support, instructions must be provided in chat; that is not automatic installation. Compatibility depends on the environment, not just the model name.

## Ask an AI to install it

Give this request to an agent with terminal and file access:

> Install the engineering skill from https://github.com/iamaia-offcials/full-stack-enginer-skill.git. Read its README and installer. Choose the skills directory for this tool and the scope requested; if unspecified, use the current project. Run a dry run, then install without changing existing project instruction files or overwriting local edits. Verify the installed SKILL.md and references, and separately report whether the agent discovers the skill. If filesystem installation is unavailable, use the documented import or explain the specific limitation.

For cloud interfaces, use the GitHub/ZIP import above. A chat interface alone does not imply a Python terminal.

## Optional profiles

The core already covers all domains. Install profiles only if separate specialized workflows are useful. The installer always includes the core dependency.

```bash
python tooling/install.py --list
python tooling/install.py --agent codex --scope user --skills uds-security,uds-backend
python tooling/install.py --agent codex --scope user --skills all
```

Profiles: `uds-product-discovery`, `uds-requirements-planning`, `uds-architecture`, `uds-design-system`, `uds-frontend`, `uds-web-development`, `uds-technical-seo`, `uds-backend`, `uds-data`, `uds-mobile-development`, `uds-performance-optimization`, `uds-dependency-upgrades`, `uds-code-review`, `uds-testing`, `uds-security`, `uds-git-cicd`, `uds-operations`, `uds-project-audit`.

## Usage examples

> Use unified-development-standard. Plan a customer portal: define the product vision and business rules, scope the first release, evaluate future staff teams and payments, and choose a stack. Explain which foundations are justified now and which work can wait.

> Use unified-development-standard. Add an email field to the existing CRM. Reuse its component and contract, check server validation and permissions, update the current feature documentation and run relevant checks.

## Updates, recovery and removal

In your repository checkout, pull changes and repeat installation with the same agent, scope and skill selection:

```bash
git pull --ff-only
python tooling/install.py --agent codex --scope user --update --dry-run
python tooling/install.py --agent codex --scope user --update
```

If you installed profiles, include the same `--skills` selection when updating. The installer records file hashes and stops on local modifications or added files. Preserve and reconcile those changes before updating. To adopt an older installation without a manifest, first review its files, then explicitly use:

```bash
python tooling/install.py --agent codex --scope user --update --adopt-existing --dry-run
python tooling/install.py --agent codex --scope user --update --adopt-existing
```

`--adopt-existing` replaces matching skill folders and preserves old files in `.uds-backups/` beside the `skills/` directory. It does not bypass protection of edited managed installations. Ordinary replacement failures trigger rollback; after a process interruption or power loss, recover from the backup. Before manual recovery, preserve the current folder, then restore the chosen backup under the original skill name.

To uninstall, remove only the selected installed skill folder. Removing core breaks profiles that depend on it. Cloud skills must be removed through their own settings. Never remove unrelated skills.

Symlinks, junctions and reparse paths are intentionally refused. If a crash leaves `.uds-install.lock`, first ensure no installer is running, then remove only that lock file.

## Repository and validation

```text
README.md                       Primary English description and installation
LICENSE                         MIT
.agents/skills/
  unified-development-standard/ Core, rules, guides, templates and examples
  uds-*/SKILL.md                 Optional domain workflows
docs/i18n/                      Translations of the public README
docs/REVIEW.md                   Current review evidence and limitations
tooling/                        Installer, packaging, validation and evaluation
tests/                          Filesystem and package regression tests
```

```bash
python tooling/validate_suite.py
python -m unittest discover -s tests -v
python tooling/package.py
```

These checks cover metadata, local links, rule IDs, installation, update protection and archive portability. They do not prove correct behavior in every agent or security of an application. See the [review](docs/REVIEW.md) and [behavioral evaluation guide](tooling/EVALUATION_GUIDE.md).

Contributions: edit the canonical rule, preserve its ID, and include useful reasoning/examples and a reproducible scenario for behavior changes. Update existing documentation in place. Keep README translations aligned with English; do not translate or duplicate the installed skill per language.

## License and limits

[MIT](LICENSE). Linked third-party documents retain their own terms. References to standards or companies imply neither certification nor endorsement.

The skill does not guarantee application security, search ranking, legal compliance or freedom from future migrations. These require project-specific verification. It grants no tools, accounts or permission to publish or operate production systems.
