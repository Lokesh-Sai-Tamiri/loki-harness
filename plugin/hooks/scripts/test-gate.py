#!/usr/bin/env python3
"""Loki-Harness test gate: when finishing while the harness is active, run the project's
configured test command. If it fails, block the stop so the work isn't called done.
Exit code 2 blocks stop and feeds the reason back to Claude."""
import json, sys, os, subprocess

try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)

# prevent infinite loops: if we already blocked once for this stop, let it go
if data.get("stop_hook_active"):
    sys.exit(0)

# only when the harness is active
if not os.path.exists(".claude/loki-harness/active"):
    sys.exit(0)

cfg_path = ".claude/loki-harness/config.json"
if not os.path.exists(cfg_path):
    sys.exit(0)
try:
    cfg = json.load(open(cfg_path))
except Exception:
    sys.exit(0)

test_cmd = cfg.get("test_command")
if not test_cmd:
    sys.exit(0)  # no tests configured -> gate degrades to nothing

try:
    r = subprocess.run(test_cmd, shell=True, capture_output=True, text=True, timeout=600)
except Exception:
    sys.exit(0)

if r.returncode != 0:
    tail = (r.stdout + r.stderr)[-1500:]
    sys.stderr.write(
        "Loki-Harness test gate: the configured test command failed. "
        "Do not finish until tests pass (Goal-Driven Execution).\n"
        f"$ {test_cmd}\n{tail}"
    )
    sys.exit(2)
sys.exit(0)
