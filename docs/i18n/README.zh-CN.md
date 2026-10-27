# 全栈工程技能

[English](../../README.md) · [Русский](README.ru.md) · [Español](README.es.md) · [العربية](README.ar.md) · [Türkçe](README.tr.md) · [简体中文](README.zh-CN.md)

**一套可移植的 AI 助手工程规范：通过决策规则、解释和示例，支持软件的规划、开发与维护。**

核心技能 `unified-development-standard` 可独立使用。它帮助智能体理解产品、选择合适的技术栈，并在完成所请求范围的同时进行相关验证。修改文案应当只是修改文案，不应自动扩展成全面审计。

## 覆盖范围

- 产品愿景、业务规则、首个版本/MVP、技术栈选择与复杂度评估。
- 架构、逻辑归属、后端、API 与集成。
- 输入校验、授权、密钥管理，以及在可信边界内强制执行业务不变量。
- 数据库约束、事务、索引、迁移与恢复。
- 前端、可维护的样式、无障碍和响应式界面，不强制采用特定品牌风格。
- 技术 SEO，以及接入服务前的分析工具与广告像素规划。
- Git、兼顾成本的 CI/CD、按需使用容器、发布与运维。
- 持续维护的文档：更新当前功能文档，区分计划与历史。

决策模式：**条件 → 决策 → 原因 → 示例 → 验证**。邮箱格式校验、参数化 SQL、安全渲染和授权分别解决不同问题；字符黑名单不能替代这些措施。

## 上下文与语言

安装的所有指令均使用**英语**。智能体仍应使用你的语言回答。入口文件会引导智能体阅读相关章节，无需通读全部 28 份参考文件。默认只安装一个自包含的核心技能；另有 18 个可选的专门配置。README 译文不会安装到技能目录中。

某些分词器处理英语时可能消耗较少的 token，但节省程度取决于文本和模型。按需阅读和消除重复同样重要。[审查结果](../REVIEW.md)区分了实际测量的文本大小、token 数量和运行时行为。

## 快速安装

需要 **Python 3.10+**，无需安装 pip 依赖。如果你的解释器命令是 Windows 上的 `py` 或 Linux/macOS 上的 `python3`，请使用相应命令。克隆仓库需要 Git；也可以在 GitHub 中选择 **Code → Download ZIP**，然后解压。

```bash
git clone https://github.com/iamaia-offcials/full-stack-enginer-skill.git
cd full-stack-enginer-skill
python tooling/install.py --agent codex --scope user
```

安装程序只复制本地文件，不会下载依赖、访问账户，也不会修改 `AGENTS.md`、`CLAUDE.md` 或 `GEMINI.md`。

安装到现有项目：

```bash
python tooling/install.py --agent codex --repo "/path/to/my-project" --dry-run
python tooling/install.py --agent codex --repo "/path/to/my-project"
```

在 Windows 上可使用类似 `"C:/dev/my-project"` 的路径。源目录与目标目录不能重叠：不要将本套件自身的目录作为安装目标。

## 智能体兼容性

| 工具 | `--agent` | 项目级目录 | 用户级目录 |
|---|---|---|---|
| Codex | `codex` | `.agents/skills/` | `~/.agents/skills/` |
| Claude Code | `claude` | `.claude/skills/` | `~/.claude/skills/` |
| Gemini CLI | `gemini` | `.gemini/skills/` | `~/.gemini/skills/` |
| Antigravity App / IDE | `antigravity` | `.agents/skills/` | `~/.gemini/config/skills/` |
| Antigravity CLI | `antigravity-cli` | `.agents/skills/` | `~/.gemini/antigravity-cli/skills/` |
| 其他兼容智能体 | `generic` 或 `--target` | 取决于智能体 | 取决于智能体 |

选择适合所用工具的命令：

```bash
python tooling/install.py --agent claude --scope user
python tooling/install.py --agent gemini --repo "/path/to/my-project"
python tooling/install.py --agent antigravity --scope user
python tooling/install.py --target "/path/to/another-agent/skills"
```

避免在同一个智能体会扫描的多个目录中重复安装。Gemini 也支持 `.agents/skills`，因此可能已经能发现共享的 Codex 安装。检查智能体的技能列表，然后明确要求它使用 `unified-development-standard`。必要时刷新技能发现或启动新会话。文件复制成功与模型实际使用技能是两项独立的验证。

上述路径已于 2026-10-27 对照官方文档检查：[Codex](https://learn.chatgpt.com/docs/build-skills)、[Claude Code](https://code.claude.com/docs/en/skills)、[Gemini CLI](https://geminicli.com/docs/cli/skills/)、[Antigravity](https://antigravity.google/docs/skills)。接口可能变化；这里并不声称已在每个平台上完成实际运行验证。

### Lovable 与云端界面

在 Lovable 中，选择 **Workspace settings → Skills → Add → Import from GitHub**，然后选择[核心技能文件夹](https://github.com/iamaia-offcials/full-stack-enginer-skill/tree/main/.agents/skills/unified-development-standard)。根据 [Lovable 官方文档](https://docs.lovable.dev/features/skills)，此操作需要工作区所有者或管理员权限。也可以选择 **Upload ZIP**。

构建可移植压缩包：

```bash
python tooling/package.py
```

输出为 `dist/unified-development-standard.zip`，其中包含入口文件、参考规则、指南、示例和许可证。请导入完整包；仅导入 `SKILL.md` 不够。安装到 Claude Code 不会将技能安装到 Claude 云端账户；请使用该账户支持的导入方式。本安装程序不管理云端账户。

如果智能体能访问文件但没有原生技能支持，可以要求它阅读核心 `SKILL.md` 和相关链接章节。如果既无法访问文件，也不支持导入，则需要在聊天中提供指令；这不属于自动安装。兼容性取决于运行环境，而不仅是模型名称。

## 让 AI 帮你安装

将以下请求交给具备终端和文件访问能力的智能体：

> 从 https://github.com/iamaia-offcials/full-stack-enginer-skill.git 安装工程技能。阅读其 README 和安装程序。根据当前工具和请求的安装范围选择技能目录；若未指定范围，则使用当前项目。先执行 dry run，再安装，不修改现有项目指令文件，也不覆盖本地编辑。验证安装后的 SKILL.md 和参考文件，并单独报告智能体是否能发现该技能。如果无法通过文件系统安装，则使用文档中的导入方式，或说明具体限制。

云端界面请使用上面的 GitHub/ZIP 导入方式。只有聊天界面不代表具备 Python 终端。

## 可选专门配置

核心技能已覆盖所有领域。只有在独立的专门工作流程有帮助时，才安装对应配置。安装程序始终会包含它们依赖的核心技能。

```bash
python tooling/install.py --list
python tooling/install.py --agent codex --scope user --skills uds-security,uds-backend
python tooling/install.py --agent codex --scope user --skills all
```

可选配置：`uds-product-discovery`、`uds-requirements-planning`、`uds-architecture`、`uds-design-system`、`uds-frontend`、`uds-web-development`、`uds-technical-seo`、`uds-backend`、`uds-data`、`uds-mobile-development`、`uds-performance-optimization`、`uds-dependency-upgrades`、`uds-code-review`、`uds-testing`、`uds-security`、`uds-git-cicd`、`uds-operations`、`uds-project-audit`。

## 使用示例

> 使用 unified-development-standard。规划一个客户门户：明确产品愿景和业务规则，划定首个版本范围，评估未来的员工团队和支付功能，并选择技术栈。说明哪些基础设计现在就有依据，哪些工作可以推迟。

> 使用 unified-development-standard。为现有 CRM 添加邮箱字段。复用现有组件和契约，检查服务端校验与权限，更新当前功能文档，并运行相关验证。

## 更新、恢复与卸载

在本地仓库中拉取更新，然后使用相同的智能体、安装范围和技能选择重新安装：

```bash
git pull --ff-only
python tooling/install.py --agent codex --scope user --update --dry-run
python tooling/install.py --agent codex --scope user --update
```

如果安装了专门配置，更新时也要保留相同的 `--skills` 选择。安装程序记录文件哈希；发现本地修改或新增文件时会停止。更新前请先保留并协调这些改动。若要接管没有清单文件的旧安装，请先审查其文件，再明确执行：

```bash
python tooling/install.py --agent codex --scope user --update --adopt-existing --dry-run
python tooling/install.py --agent codex --scope user --update --adopt-existing
```

`--adopt-existing` 会替换匹配的技能文件夹，并将旧文件保存在与 `skills/` 同级的 `.uds-backups/` 中。它不会绕过对已修改的受管安装的保护。普通替换失败会触发回滚；进程中断或断电后，应从备份恢复。手动恢复前，先保留当前文件夹，再将选定备份恢复到原技能名称对应的目录。

卸载时，仅删除选定的已安装技能文件夹。删除核心技能会导致依赖它的专门配置失效。云端技能必须通过各自的设置删除。不要删除无关技能。

安装程序明确拒绝符号链接、目录联接和重解析路径。如果崩溃后遗留 `.uds-install.lock`，先确认没有安装程序正在运行，然后只删除该锁文件。

## 仓库结构与验证

```text
README.md                       英文主说明与安装指南
LICENSE                         MIT 许可证
.agents/skills/
  unified-development-standard/ 核心、规则、指南、模板与示例
  uds-*/SKILL.md                 可选领域工作流程
docs/i18n/                      公开 README 的译文
docs/REVIEW.md                   当前审查证据与限制
tooling/                        安装、打包、验证与评估工具
tests/                          文件系统与安装包回归测试
```

```bash
python tooling/validate_suite.py
python -m unittest discover -s tests -v
python tooling/package.py
```

这些检查覆盖元数据、本地链接、规则 ID、安装、更新保护和压缩包可移植性。它们不能证明所有智能体都能正确使用技能，也不能证明应用的安全性。详见[审查结果](../REVIEW.md)和[行为评估指南](../../tooling/EVALUATION_GUIDE.md)。

贡献时，请编辑规范规则的唯一维护来源，保留规则 ID，并提供有帮助的推理和示例。行为变更应附带可复现的场景。文档应在原处更新。README 译文应与英语版保持一致；不要按语言翻译或复制已安装的技能。

## 许可证与限制

采用 [MIT 许可证](../../LICENSE)。链接的第三方文档保留各自的条款。引用标准或公司不代表获得认证或背书。

该技能不保证应用安全、搜索排名、法律合规，也不保证未来无需迁移；这些都需要针对项目进行验证。它不会授予工具、账户，也不会授予发布或操作生产系统的权限。
