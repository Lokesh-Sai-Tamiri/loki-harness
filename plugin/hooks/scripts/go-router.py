#!/usr/bin/env python3
"""Loki-Harness router: while /go is active this session, route each prompt through the pipeline."""
import json, sys, os

try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)

prompt = data.get("prompt") or ""

# ~ prefix = bypass the harness for this one prompt
if prompt.lstrip().startswith("~"):
    sys.exit(0)

# only engage when the session toggle is on
if not os.path.exists(".claude/loki-harness/active"):
    sys.exit(0)

# don't re-route the /go invocation itself; the command handles it
if prompt.lstrip().startswith("/go"):
    sys.exit(0)

ctx = (
    "Loki-Harness is ACTIVE. Route this request through the pipeline using the /go playbook:\n"
    "1) Classifier (haiku) -> {size, tier, skip}.\n"
    "   - trivial: answer directly, no pipeline.\n"
    "   - standard: Research -> Planner(once) -> Adversary(once) -> Task-splitter -> "
    "per task [Context-assembler -> Implementer+tests] -> Adversary final review.\n"
    "   - deep: add Interview after Research, and run Planner <-> Adversary as a mesh "
    "(exit on zero surviving findings or 3 rounds).\n"
    "2) Spawn each agent on its tier model (haiku/sonnet/opus).\n"
    "3) Pass forward distilled summaries + file paths, not raw dumps.\n"
    "Prefix a prompt with ~ to bypass the harness for that prompt."
)
print(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": ctx}}))
