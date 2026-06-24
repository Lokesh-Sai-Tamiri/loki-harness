#!/usr/bin/env python3
"""Loki-Harness git guardrail: block destructive commands before they run.
Exit code 2 blocks the tool call and surfaces the message to Claude."""
import json, sys, re

try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)

cmd = (data.get("tool_input") or {}).get("command") or ""

dangerous = [
    r"git\s+push\s+[^|;&]*(--force\b|-f\b)",   # force push
    r"git\s+push\s+[^|;&]*\+",                  # force push via refspec +
    r"git\s+reset\s+--hard",                    # discard work
    r"git\s+clean\s+-[a-zA-Z]*f",               # delete untracked
    r"git\s+branch\s+-D\s+(main|master)\b",     # nuke trunk
    r"git\s+checkout\s+--\s+\.",                # wipe local changes
    r"\brm\s+-rf?\s+(/|~|\*|\.)(\s|$)",         # catastrophic rm
]
for p in dangerous:
    if re.search(p, cmd):
        sys.stderr.write(
            "Loki-Harness blocked a destructive command: " + cmd + "\n"
            "This guardrail prevents irreversible loss. If you truly intend it, run it yourself outside the harness."
        )
        sys.exit(2)
sys.exit(0)
