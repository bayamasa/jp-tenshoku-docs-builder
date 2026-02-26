#!/usr/bin/env python3
"""PreToolUse hook: 個人情報を含むパスへの操作をブロックする."""

import json
import sys

BLOCKED_PATHS = [
    ".personal/credential.yaml",
    "output/",
]


def _find_blocked(text: str) -> str | None:
    for p in BLOCKED_PATHS:
        if p in text:
            return p
    return None


def _block(matched_path: str) -> None:
    result = {
        "decision": "block",
        "reason": (
            f"{matched_path} には個人の機密情報が含まれている可能性があります。"
            f"このファイルへのアクセスはブロックされました。"
        ),
    }
    print(json.dumps(result))
    sys.exit(2)


BASH_ALLOW_PREFIXES = [
    "make build-",
    "mkdir ",
]


def main() -> None:
    raw = sys.stdin.read()
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        sys.exit(0)

    tool_name = data.get("tool_name", "")
    tool_input = data.get("tool_input", {})

    # Bash: ホワイトリストのコマンドは許可
    if tool_name == "Bash":
        command = tool_input.get("command", "")
        if any(command.startswith(prefix) for prefix in BASH_ALLOW_PREFIXES):
            sys.exit(0)

    # tool_input の全値を検査
    for value in tool_input.values():
        if isinstance(value, str):
            matched = _find_blocked(value)
            if matched:
                _block(matched)

    sys.exit(0)


if __name__ == "__main__":
    main()
