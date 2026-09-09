# Main Agent — Toolbox Customization Catalog

> Deviations from `general_tool_management_helpers/` defaults.
> Version 6.0 — 2026-04-08

---

## 1. L0 Tool Catalog → `MainCatalog`

| Aspect | General Default (`AgentToolCatalog`) | Main Agent |
|--------|-------------------------------------|------------|
| Subclass | `AgentToolCatalog` (base) | `MainCatalog(AgentToolCatalog)` |
| `pipeline_label` | `""` (unset) | `"main"` |
| `PROTECT_TOOLS` | N/A | **`[]` (empty)** — all tools are delegation, none need protection |
| Tool count | N/A | **5 tools** (smallest of all agents) |

---

## 2. Registered Tools (5 total)

| Tool | Group | Compactor | Notes |
|------|-------|-----------|-------|
| `run_query_agent` | `subagent_delegation` | `compact_query_result` | Delegates full query to Query Agent |
| `run_analysis_agent` | `subagent_delegation` | `compact_analysis_result` | Delegates full analysis to Analysis Agent |
| `run_parallel_subagents` | `parallel_delegation` | internal agentic batch compaction (auto two-stage when oversized) | ThreadPoolExecutor → multiple subagent calls |
| `browse_subagent_tools` | `tool_menu` | — (`skip_compactor=True`) | LLM-powered tool discovery |
| `run_subagent_tool` | `tool_menu` | cross-agent compaction routing | Execute any tool from any subagent |

---

## 3. Key Deviation from Other Agent Tool Models

| Aspect | Query Agent | Analysis Agent | Main Agent |
|--------|-------------|----------------|------------|
| L0 tool count | 8 memory + 1 dispatch | 10+ domain | **5 delegation + menu** |
| Tool nature | Memory/dispatch | Domain-specific | **Pure delegation** |
| Direct DB access | Via L2 workers | Via query agent | **Never** |
| Tier catalogs | 3-tier (L0/L1/L2) | 1 tier | **1 tier** |
| PROTECT_TOOLS | 0 | 6 | **0** |

Main agent does **no direct work** — every substantive action goes through a subagent.

---

## 4. Subagent Delegation Tools (main-specific)

### `run_query_agent`

| Parameter | Type | Purpose |
|-----------|------|---------|
| `question` | str | The query to pass to the Query Agent |
| `context` | str (optional) | Additional context from conversation |

Calls `QueryAgent.run(question, context)` synchronously. Result is compacted
by `compact_query_result` before returning to the main agent's context window.

### `run_analysis_agent`

| Parameter | Type | Purpose |
|-----------|------|---------|
| `question` | str | The analysis task to pass to the Analysis Agent |
| `context` | str (optional) | Additional context (e.g., prior query results) |

Calls `AnalysisAgent.run(question, context)` synchronously. Result compacted
by `compact_analysis_result`.

### `run_parallel_subagents`

| Parameter | Type | Purpose |
|-----------|------|---------|
| `tasks` | list[dict] | Native array of `{agent, label, question, purpose, context}` objects; all fields required |

Uses `ThreadPoolExecutor` to dispatch multiple subagent calls in parallel.
The raw batch dict `{n_tasks, results}` is recorded verbatim in working
memory; the orchestrator context receives agentically compacted markdown
(one `[label]` section per task) produced by `MainToolResultCompactor.call`
over the full JSON payload, briefed with each task's original purpose and
question. If the compaction LLM fails, a deterministic per-task snapshot is
returned instead — completed subagent work is never destroyed.

---

## 5. Tool Menu System (entirely main-specific)

### `browse_subagent_tools`

| Aspect | Detail |
|--------|--------|
| Purpose | Discover tools available in query/analysis agents without calling them |
| Planner model | `CONFIG.MENU_PLANNER_MODEL` (`claudesonnet4`) |
| How it works | Loads tool catalogs from both subagents → LLM planner selects relevant tools for the user's question |
| Returns | Ranked list of tool names + descriptions + which agent owns them |

### `run_subagent_tool`

| Parameter | Type | Purpose |
|-----------|------|---------|
| `agent` | str | `"query"` or `"analysis"` |
| `tool_name` | str | The specific tool to call (from browse results) |
| `parameters` | dict | Tool-specific parameters |

Calls the specified tool in the target agent's context. Result goes through
**cross-agent compaction routing** — uses the target agent's compactor
(not main agent's) to ensure domain-appropriate compression.

---

## 6. Compactors (2 main-specific + 1 aggregation)

| Compactor | Input | Output |
|-----------|-------|--------|
| `compact_query_result` | Full query agent result | Question + Top DOIs/compounds + answer summary |
| `compact_analysis_result` | Full analysis agent result (incl. fit_results) | Question + fit quality summary + key coefficients + verdict excerpt |
| batch compaction (inside `run_parallel_subagents`) | Batch of task results | Single-pass agentic per-`[label]` report; oversized batches return a compaction **anchor** instead |

**No hardcoded compactors** — all are LLM-based because subagent outputs
are free-form text, not structured data. Uses `MainClient.for_l0()` for
compaction calls (highest-tier model).

**Two-stage path for oversized batches (automated):** when the batch
JSON exceeds the single-pass limit, `run_parallel_subagents` runs an
internal loop — a philosophy hook to the orchestrator's model tier
(numbered result sizes + producing arguments; hook replies select
`TARGET` results and the philosophy; malformed replies get up to two
correction rounds; deterministic default derived from task purposes if
unavailable), agentic compaction of the targeted tasks under that
philosophy (untargeted tasks pass as complete child-authored claims),
then an agentic consolidation pass. Fallbacks are whole-field digests
(complete `core_claims`, verdicts, file lists) — never character
truncation. The philosophy, targets, and per-task reports are recorded
in working memory.

---

## 7. No Dynamic Tool Registration

| Aspect | Query Agent | Analysis Agent | Main Agent |
|--------|-------------|----------------|------------|
| Runtime tools | `L1_query` via `L1AutoSaver` | `list_session_files` | **None** |
| Dynamic pattern | Wrapper tool on first L1 dispatch | Added by orchestrator | **Static catalog only** |

Main agent's 5 tools are all registered at catalog construction time and never change.
