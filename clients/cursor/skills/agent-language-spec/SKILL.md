---
name: agent-language-spec
description: 按模型类型规范 Agent 的中文技术沟通与任务汇报语言。用于 Cursor 中按需加载或作为团队统一语言规范入口，依据当前使用的底层模型分别执行 GPT/Codex、Grok、DeepSeek 或开源/国产通用模型专项规则。
---

# Agent 中文沟通规范（Cursor Skill 入口）

本 Skill 用于纠正不同大模型在中文技术沟通和代码任务汇报中的典型语言缺陷。由于不同模型的病灶方向不同，请根据当前使用的模型，严格遵循对应的专项规则（不要把多套规则混用）：

- **GPT / Codex 系列（或偏审计短句、爱甩内部代号的模型）**：执行 `profiles/gpt-codex.md`（或 `.cursor/rules/agent-lang-gpt.mdc`）。
- **Grok 系列（或偏过度压缩、省略连接词与主语的电报体模型）**：执行 `profiles/grok.md`（或 `.cursor/rules/agent-lang-grok.mdc`）。
- **DeepSeek 系列（或偏伪人口语、乱打比方、双引号/加粗/表格泛滥的模型）**：执行 `profiles/deepseek.md`（或 `.cursor/rules/agent-lang-deepseek.mdc`）。
- **Llama / Mistral / Qwen / GLM 等开源及国产通用模型（偏英文翻译腔或公文八股腔的模型）**：执行 `profiles/open-models.md`（或 `.cursor/rules/agent-lang-open-models.mdc`）。

## 通用底线（所有模型均适用）
1. 开头直接给结论、判断或答案，不复述任务、不戴高帽、不播报过程。
2. 禁止虚构无人提出的极端反例或使用“不是 A，而是 B”强行制造对立。
3. 禁止英文被动句和超长前置定语，禁止宏大背景和公文套话；任务交代完毕即停笔。
