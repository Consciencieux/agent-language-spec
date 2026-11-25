# Agent Language Spec（Agent 中文沟通规范）

专门治大模型在中文技术沟通、代码评审和任务汇报里**“不说人话”**的提示词与客户端规则仓库。

过去很多通用规范试图用一套几万字的法典管住所有模型，结果往往适得其反：规则太长会稀释注意力，而不同模型“不说人话”的病灶甚至是**完全相反**的。本仓库按三类典型模型的语言缺陷拆分为独立规则，并针对主流编程软件提供开箱即用的配置文件。

## 为什么不同模型需要不同的提示词？

主流模型在经过大量推理训练（RLVR）和偏好对齐后，通常会在最终输出时坍缩成三种截然不同的“非人感”。其他开源或闭源模型也基本可以归入这三类：

| 典型代表 | 同类常见模型特征 | “不说人话”的核心表现 | 应该选用哪份规则 |
| :--- | :--- | :--- | :--- |
| **GPT / Codex** | 偏公文、司法审计风，或爱直接倾倒工作上下文的模型 | 满篇未解释的内部代号、15–25 字孤立判断句无限连发、行号和 commit 堵在主干里、按排查顺序记流水账 | [`profiles/gpt-codex.md`](profiles/gpt-codex.md) |
| **Grok** | 偏极简压缩风，或在“冷硬电报”与“耍贫嘴”间反复横跳的模型 | 砍光连接词和主语的“电报体”、用大白话词汇硬套高密度代码状态机；一旦要求“自然”，又容易滑向网络梗和表演式口语 | [`profiles/grok.md`](profiles/grok.md) |
| **DeepSeek** | 偏戏剧化表达、重度推理自白与排版强迫症的模型 | 刻意模仿人类聊天的“伪人口语”、莫名其妙的比喻和自造黑话，以及双引号、冒号、破折号、加粗和逻辑不通的表格泛滥 | [`profiles/deepseek.md`](profiles/deepseek.md) |
| **开源与国产通用模型** | Llama、Mistral、Qwen、GLM 等开源或通用对话模型 | 英文直译腔（被动句泛滥、超长前置定语、“当谈到……时”）、国产公文申论八股腔（“随着……发展”“赋能/抓手”“综上所述”） | [`profiles/open-models.md`](profiles/open-models.md) |

> **如何判断其他模型归哪一类？**

> 如果它输出像“冷冰冰的审计纪要、看不懂内部术语”，用 `gpt-codex.md`；如果它输出像“没标点过渡的压缩补丁日志”，用 `grok.md`；如果它输出“爱打比方、满篇双引号加粗和熟络语气词”，用 `deepseek.md`。如果它输出“被动句和长定语满满的英文翻译腔”，或“一开口就是随着技术发展、赋能协同的公文八股”，用 `open-models.md`。

## 仓库目录结构

```text
agent-language-spec/
├── README.md                                  # 本说明与各客户端使用教程
├── LICENSE                                    # MIT 许可证
├── SKILL.md                                   # 通用 Agent Skill 入口（兼容各类 Skills 自动发现）
├── profiles/                                  # 按模型拆分的独立核心规则（纯正文，可直接复制）
│   ├── gpt-codex.md                           # GPT / Codex 专用规范
│   ├── grok.md                                # Grok 专用规范
│   └── deepseek.md                            # DeepSeek 专用规范
│   └── open-models.md                         # 开源与国产通用模型规范（治翻译腔与公文八股）
├── clients/                                   # 按编程软件封装好的即用配置文件
│   ├── cursor/
│   │   ├── rules/                             # Cursor .mdc 常驻规则（每次只启用一个对应模型的）
│   │   │   ├── agent-lang-gpt.mdc
│   │   │   ├── agent-lang-grok.mdc
│   │   │   └── agent-lang-deepseek.mdc
│   │   │   └── agent-lang-open-models.mdc
│   │   └── skills/
│   │       └── agent-language-spec/SKILL.md   # Cursor Skill 按需入口
│   ├── codex/
│   │   └── AGENTS.md                          # Codex CLI / IDE 开箱即用配置
│   └── deepseek-harness/
│       └── system-prompt.md                   # DeepSeek Harness / API System Prompt 模板
└── references/
    └── full-spec.md                           # 原版 27 主题完整参考手册（仅作查阅，不建议整篇常驻）
```

## 各软件安装与使用教程

### 1. Cursor

Cursor 支持通过 `.cursor/rules/*.mdc` 常驻注入规则，也支持通过 `.cursor/skills/` 按需加载。

**方式 A：使用 `.mdc` 常驻规则（推荐，日常对话和改代码稳定生效）**

1. 根据你平时在 Cursor 里最常用的模型，从 `clients/cursor/rules/` 中**只挑选对应的那一个文件**，复制到你项目的 `.cursor/rules/` 目录下：
   - 常用 GPT 系列：复制 `clients/cursor/rules/agent-lang-gpt.mdc`
   - 常用 Grok 系列：复制 `clients/cursor/rules/agent-lang-grok.mdc`
   - 常用 DeepSeek 系列：复制 `clients/cursor/rules/agent-lang-deepseek.mdc`
   - 常用 Llama / Mistral / Qwen / GLM 等模型：复制 `clients/cursor/rules/agent-lang-open-models.mdc`
2. 文件头已配置 `alwaysApply: true`，打开 Cursor 的 **Settings → Rules** 确认该规则已处于启用状态，新建会话即可生效。

> **避坑提示**：不要把三个模型的 `.mdc` 文件同时放进 `.cursor/rules/` 并全部开启 `alwaysApply: true`。它们针对不同模型的反向纠偏指令会互相冲突，而且会白白占用三倍上下文。如果你经常切换模型，可以在 Cursor 中将其中两条改为 `Manual`（手动 `@` 引用），只保留主力模型那一条为 `Always`。

**方式 B：作为 Skill 使用**

如果你希望由 Agent 按需加载，可将 `clients/cursor/skills/agent-language-spec/` 整个目录复制到项目的 `.cursor/skills/`（或全局 `~/.cursor/skills/`）中，同时把 `profiles/` 目录一并放入以便模型按模型名称读取对应规则。

---

### 2. Codex（OpenAI Codex CLI / IDE）

Codex 默认会自动读取项目根目录以及用户主目录下的 `AGENTS.md`。

- **单项目生效**：直接将 `clients/codex/AGENTS.md` 复制到你的代码仓库根目录（如果项目里已经有 `AGENTS.md`，把里面的正文追加到原有文件末尾即可）。
- **全局生效**：复制到 `~/.codex/AGENTS.md`，这样你在任何目录下启动 Codex 都会自动遵循汇报规范。

---

### 3. DeepSeek Harness / 各类 API 客户端

DeepSeek 系列的“伪人口语”和“排版强迫症”必须靠 System Prompt 在对话最前端强力压制。

- **DeepSeek Harness**：将 `clients/deepseek-harness/system-prompt.md` 的内容完整复制到你的 Harness 系统提示词（System Prompt）配置项中，或者在仓库配置里将其挂载为最高优先级系统指令。
- **ChatBox / Cherry Studio / OpenWebUI / 第三方客户端**：新建或编辑助手预设，将 `profiles/deepseek.md` 全文粘贴到 **System Prompt（系统提示词）** 中即可。若你搭配的是长思维链推理模式（如 R1），该规则会直接约束最终输出区，不会干扰 `<think>` 内部的正常逻辑推演。

---

### 4. Claude Code / Windsurf / Cline / Trae / OpenCode 等通用客户端

- **Claude Code**：如果你在使用 Claude 时仍然希望收紧汇报结构，可将 `profiles/gpt-codex.md` 的核心段落追加到项目的 `CLAUDE.md`，或将本仓库作为 Skill 挂载到 `.claude/skills/agent-language-spec/`。
- **Windsurf**：将对应模型的 `profiles/*.md` 内容放入项目根目录的 `.windsurfrules`（或 `.windsurf/rules/`）。
- **Cline / Roo Code**：将对应模型的 `profiles/*.md` 内容放入项目根目录的 `.clinerules`。
- **支持 `SKILL.md` 标准的工具（如 Trae、OpenCode 等）**：直接引用本仓库根目录的 `SKILL.md` 及 `profiles/` 文件夹即可。

## 维护说明

- 日常调整某类模型的约束时，直接修改 `profiles/` 下的对应文件，并同步更新 `clients/` 下对应的封装文件即可，仓库不再依赖复杂的构建或同步脚本。
- `references/full-spec.md` 保留了初版的全部 27 项细则，适合在需要进一步细化某项条款时翻阅参考。
