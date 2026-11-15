# Agent Communication

完整的 Agent 中文沟通规范。用于解释、判断、技术讨论、进度与交付说明，同时规定成文动作和输出前审核。

## 使用

完整读取 `SKILL.md`。所有执行规则均在正文中，包括用词、命名、中英使用、主语、谓语、搭配、修饰、名词化、句间承接、解释、数字、修辞、否定、重复、篇章、标题、格式、语言反馈和审核。没有需要另外加载的示例库。

正文包含 27 个主题与 26 项输出前审核要求。规则依照具体的适用条件要求删除、恢复、调整或重写文字；审核直接处理当前稿，结束于实际修正。

## 安装到 Cursor

使用 `agent-communication-complete-cursor.zip`，将其中的 `.cursor/` 目录合并到项目根目录。

- `.cursor/rules/agent-communication.mdc` 设为 `alwaysApply: true`，包含完整正文。
- `.cursor/skills/agent-communication/SKILL.md` 提供同内容的 Skill 入口，以及来源和许可证文件。

已有安装时，替换同名规则，并用新目录整体替换旧的 `agent-communication` Skill 目录。旧版 `references/examples.md` 和旧版自定义 User Rules 文字不继续使用。新建会话后在规则设置中确认该规则已启用。

规则直接携带全文，没有依赖模型自行打开的外部规则链接。Skill 与规则来自同一份正文；正文已在当前上下文完整出现时，入口要求直接执行。

Cursor 官方机制说明：

- `https://cursor.com/docs/rules`
- `https://cursor.com/docs/skills`

## 安装到其他兼容客户端

解压 `agent-communication-complete-skill.zip`，将 `agent-communication/` 整个目录放入该客户端支持的 Skills 目录，并通过客户端实际提供的方式激活。跨会话的常驻投递采用该客户端的规则设置；独立 Skill 包本身只提供规范及其入口。

## 维护

修改 `SKILL.md` 时，以它作为正文来源，同步生成 Cursor 规则：删除 YAML 头，添加 `description` 与 `alwaysApply: true` 的规则头，其余正文保持逐字一致。保留 `LICENSE` 和 `SOURCES.md`。

针对模型效果，本包尚未进行 Grok 或 DeepSeek 的实际运行对照。此次交付完成的是规范重写与安装文件校验。
