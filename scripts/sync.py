#!/usr/bin/env python3
"""Zero-dependency sync script to build self-contained client prompts from profiles/."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
PROFILES = ROOT / "profiles"

TARGETS = [
    {
        "client_path": ROOT / "clients" / "cursor" / "agent-lang-grok.mdc",
        "delta": PROFILES / "grok.md",
        "header": (
            "---\n"
            "description: 约束 Grok 在 Cursor 中的中文沟通与任务汇报（自动同步自 profiles/general.md + profiles/grok.md）\n"
            "alwaysApply: true\n"
            "---\n\n"
        ),
    },
    {
        "client_path": ROOT / "clients" / "codex" / "AGENTS.md",
        "delta": PROFILES / "gpt-codex.md",
        "header": (
            "# AGENTS.md（Codex 中文沟通规范）\n\n"
            "> 本文件由 `scripts/sync.py` 自动合并 `profiles/general.md` 与 `profiles/gpt-codex.md` 生成。\n\n"
        ),
    },
    {
        "client_path": ROOT / "clients" / "deepseek-harness" / "system-prompt.md",
        "delta": PROFILES / "deepseek.md",
        "header": (
            "<!-- 本文件由 scripts/sync.py 自动合并 profiles/general.md 与 profiles/deepseek.md 生成 -->\n\n"
        ),
    },
]


def render(target: dict) -> str:
    general = (PROFILES / "general.md").read_text(encoding="utf-8").strip()
    delta = target["delta"].read_text(encoding="utf-8").strip()
    return f"{target['header']}{general}\n\n{delta}\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync profiles/ into clients/.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Verify clients/ files match profiles/ without modifying them.",
    )
    args = parser.parse_args()

    out_of_sync = []
    for target in TARGETS:
        expected = render(target)
        path: Path = target["client_path"]
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current != expected:
            if args.check:
                out_of_sync.append(path.relative_to(ROOT))
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(expected, encoding="utf-8", newline="\n")
                print(f"Synced {path.relative_to(ROOT)}")

    if args.check and out_of_sync:
        for rel in out_of_sync:
            print(f"Out of sync: {rel}", file=sys.stderr)
        print("Run `python3 scripts/sync.py` to update client files.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
