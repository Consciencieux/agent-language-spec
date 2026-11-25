# 各客户端安装与使用教程

`clients/` 目录下的文件已由 `scripts/sync.py` 预先合并好“通用规范 + 对应模型专项纠偏”，每个文件都可独立运行，无需模型在对话时二次跳转读取。

## 1. Cursor（主力使用 Grok）

1. 将 `clients/cursor/agent-lang-grok.mdc` 复制到你项目的 `.cursor/rules/` 目录下。
2. 该文件已默认设置 `alwaysApply: true`，在 Cursor 的 **Settings → Rules** 中确认其已启用，新建会话即可生效。

> 如果你后续需要在 Cursor 中切换其他模型并启用对应规则，建议参考根目录 `AGENTS.md` 调整 `scripts/sync.py` 生成对应 `.mdc`，但同一时间只保持主力模型那一条为 `alwaysApply: true`，避免不同模型的反向纠偏相互打架。

## 2. Codex（OpenAI Codex CLI / IDE）

- **单项目生效**：将 `clients/codex/AGENTS.md` 复制到目标项目根目录。若该项目已有 `AGENTS.md`，把沟通规范正文追加到文末，不要覆盖原有内容。
- **全局生效**：将 `clients/codex/AGENTS.md` 复制到 `~/.codex/AGENTS.md`。

本仓库根目录的 `AGENTS.md` 是维护说明，不是要安装的沟通规范。安装时只复制 `clients/codex/AGENTS.md`。

## 3. DeepSeek Harness / 各类 API 客户端

- **DeepSeek Harness**：将 `clients/deepseek-harness/system-prompt.md` 设为系统的 System Prompt。
- **第三方聊天 / API 客户端（Cherry Studio、ChatBox、OpenWebUI 等）**：直接复制 `clients/deepseek-harness/system-prompt.md` 全文粘贴到助手的系统提示词中。如果是长思维链模式，该规则仅约束最终输出区，不会干扰思考过程。

## 4. 通用 Agent Skills 客户端（Claude Code / Trae / OpenCode 等）

直接引用仓库根目录的 `SKILL.md`，并确保 `profiles/` 目录随仓库一同保留，模型会先加载 `profiles/general.md`，再按当前模型选择对应的专项增量文件。
