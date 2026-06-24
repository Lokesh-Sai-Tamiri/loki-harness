# Loki-Harness

A generic, install-anywhere [Claude Code](https://code.claude.com) harness. One repo → one plugin → install once → cached globally → every project gets it. No brand, no per-repo cloning.

Type `/go` once at the start of a session. From then on, every prompt you send is routed through a gated, model-tiered multi-agent pipeline that turns a rough prompt into researched, grilled, plan-hardened, test-verified output — with always-on engineering discipline running underneath no matter what.

## Install (CLI only)

```bash
# In the Claude Code CLI (not Desktop/web — /plugin is CLI-only):
/plugin marketplace add <your-github-username>/loki-harness
/plugin install loki-harness@loki-harness
/reload-plugins
```

Installs globally and is available in every project. Requires Node.js ≥ 18 and a current Claude Code (run `/doctor` to check).

## Use

```
/go            # engage the harness for the rest of this session
<your prompt>  # routed automatically from here on
```

`/go` is a per-session toggle: a SessionStart hook resets it each new session, so you type it once per session. The first `/go` in a fresh repo also bootstraps it — see below.

## How it works

Three layers, by design:

1. **Always-on (deterministic, via hooks)** — fire every session regardless of `/go`:
   - SessionStart injects the four Karpathy principles into context.
   - PreToolUse blocks dangerous git operations (force-push, hard reset, etc.).
   - Stop runs the project's configured test command as a verification gate.
2. **The pipeline (engaged by `/go`)** — a UserPromptSubmit hook routes each prompt through the agents below.
3. **Skills (model-invoked)** — the agents reach for these on demand; specialized stack skills are pulled from the marketplace on first run, with your per-item approval.

### Flow (deep path)

```
/go → Classifier → Research → Interview → Planner ⇄ Adversary (cap 3)
    → Task-splitter → per task [ Context-assembler → Implementer ⇄ tests ]
    → Adversary (final whole-diff review) → handoff
```

Trivial prompts skip the pipeline and are answered directly. Standard prompts skip the interview grill and the Planner⇄Adversary mesh.

### Agents (8)

| Agent | Model | Job |
|---|---|---|
| Classifier | Haiku | Sizes each prompt (trivial/standard/deep); picks path + model tier |
| Research | Haiku | Codebase deep-dive + web; writes findings to file, returns a distilled summary |
| Interview | Sonnet | Grills until intent and edge cases are clear; writes answers into context |
| Planner | Sonnet (Opus on deep) | Drafts the solution as a spec with verifiable success criteria + failing tests |
| Adversary | Opus | Assumes the plan is wrong; produces concrete gap artifacts; also the final whole-diff review |
| Task-splitter | Sonnet | Approved plan → ordered, independently-shippable tasks (vertical slices) |
| Context-assembler | Haiku | Per task: pulls the right skills/patterns into the implementer's brief |
| Implementer | Sonnet (Opus on hard) | Writes one task under the Ponytail ladder + Simplicity/Surgical; runs tests |

### Skills (7, generic, zero-install)

`caveman` · `ponytail` · `tdd` · `diagnose` · `handoff` · `frontend-design` · `backend-design`

### Model tiers

Haiku = triage / research / assembly. Sonnet = interview / plan / build. Opus = adversary / architecture / hard work. The Classifier and the router set the tier per prompt; each agent also pins its default model in frontmatter.

## First-run bootstrap

The first `/go` in a repo with no `.claude/loki-harness/config.json`:

1. Reads the codebase and infers the stack.
2. Writes per-project config (test command, conventions) and a CONTEXT map into `.claude/loki-harness/`.
3. Recommends any specialized stack skills, showing each with its source.
4. Installs only the ones **you approve, one at a time**, then reloads.

Loop exit is grounded (tests pass / zero surviving adversary findings / cap of 3 rounds), never a self-reported confidence number.

## Honest limits

- **CLI only.** `/plugin` and installs don't exist in Claude Code Desktop/web.
- **Installing third-party skills runs code with your privileges** and isn't vetted by Anthropic — that's why the bootstrap installs only what you approve per item, from sources you see.
- **Skills are probabilistic.** The hooks are the only guaranteed steps; agent stages are a strong nudge.
- **Validate the hooks against your version.** Hook JSON formats can shift between Claude Code versions. After install run `/doctor` and `/reload-plugins`; if a hook doesn't fire, check `hooks/hooks.json` against your version's hooks reference.

## License

MIT. Bundled disciplines adapt open work: the Karpathy principles (forrestchang/andrej-karpathy-skills), the Ponytail ladder (DietrichGebert/ponytail), Caveman, and the grill/PRD/TDD patterns (mattpocock/skills). See each upstream for its license.
