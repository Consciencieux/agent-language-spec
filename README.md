# Agent Language Spec（Agent 中文沟通规范）

用于纠正编程 Agent 与大模型在中文技术讨论、代码审查和任务汇报中“不说人话”的提示词仓库。采用**精简通用规范 + 模型专项纠偏**的分层结构，避免超长规则稀释注意力，也避免不同模型的纠偏指令互相冲突。

## 快速使用

| 使用环境 | 主力模型 | 直接使用的文件 |
| :--- | :--- | :--- |
| **Cursor** | Grok | [`clients/cursor/agent-lang-grok.mdc`](clients/cursor/agent-lang-grok.mdc)（放入 `.cursor/rules/`） |
| **Codex (CLI / IDE)** | GPT / Codex | [`clients/codex/AGENTS.md`](clients/codex/AGENTS.md)（放入项目根目录或 `~/.codex/`） |
| **DeepSeek Harness / API** | DeepSeek | [`clients/deepseek-harness/system-prompt.md`](clients/deepseek-harness/system-prompt.md)（填入 System Prompt） |
| **通用 Agent Skills 客户端** | 按模型切换 | 根目录 [`SKILL.md`](SKILL.md) + `profiles/` |

## 目录结构

仓库目录见 [`docs/structure.md`](docs/structure.md)。

## 文档导航

- 各客户端详细安装与避坑：[`docs/installation.md`](docs/installation.md)
- 不同模型的输出偏差观察：[`docs/model-behaviors.md`](docs/model-behaviors.md)
- 规范修改与同步方式：[`docs/maintenance.md`](docs/maintenance.md)
- 完整版 27 主题参考规范：[`references/full-spec.md`](references/full-spec.md)
