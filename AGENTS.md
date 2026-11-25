# 规范维护与同步说明

本仓库采用**单源维护 + 零依赖同步**的结构，避免手动复制导致的规则漂移：

- **公共规则修改**：编辑 `profiles/general.md`。所有模型都应遵守的语法、事实准确性、去翻译腔、去八股等条款统一放在这里。
- **模型专项调整**：编辑 `profiles/gpt-codex.md`、`profiles/grok.md` 或 `profiles/deepseek.md`。只维护该模型需要额外强调的偏差及具体纠偏示例；所有模型都应遵守的规则放在通用规范中，不重复抄写。

## 同步客户端产物

修改 `profiles/` 下的任意文件后，在仓库根目录运行：

```bash
python3 scripts/sync.py
```

脚本会自动把 `profiles/general.md` 与对应专项文件合并写入 `clients/` 下的即用文件。提交前可运行检查模式确认无遗漏：

```bash
python3 scripts/sync.py --check
```
