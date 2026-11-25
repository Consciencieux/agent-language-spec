# 目录结构

```text
agent-language-spec/
├── README.md                  # 项目介绍与快速上手
├── SKILL.md                   # 通用 Agent Skill 入口
├── profiles/                  # 规则源：general.md（通用）+ 3 个模型专项增量
├── clients/                   # 同步生成的各客户端单文件规则（开箱即用）
├── docs/                      # 安装教程、模型偏差观察与维护说明
├── references/full-spec.md    # 完整 27 主题参考手册
└── scripts/sync.py            # 零依赖同步脚本（profiles -> clients）
```
