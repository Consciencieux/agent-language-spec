---
name: agent-language-spec
description: 按“通用规范 + 模型专项纠偏”约束 Agent 的中文技术沟通与任务汇报，消除电报体、审计短句、内部黑话、伪人口语、英文翻译腔及公文八股腔。
license: MIT
---

# Agent 中文沟通规范（Skill 入口）

1. **必须先加载并执行通用规范**：读取 `profiles/general.md`，作为所有模型共同遵守的中文沟通底线。
2. **按当前模型加载专项纠偏**：根据当前运行的模型，额外读取对应的专项增量文件（专项文件只强化通用规则的执行，不覆盖通用规范）：
   - **GPT / Codex 系列**：读取 `profiles/gpt-codex.md`
   - **Grok 系列**：读取 `profiles/grok.md`
   - **DeepSeek 系列**：读取 `profiles/deepseek.md`
   - **其他模型**：仅执行通用规范 `profiles/general.md`。
3. **需要查看完整边界条件或修订细则时**：按需查阅 `references/full-spec.md` 的相关条目，日常使用无需全文加载。
