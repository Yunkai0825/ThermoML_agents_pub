# Main Agent — Workflow Customization Catalog

> Deviations from `general_subagent_skill_schema_and_parser/` defaults.
> Version 6.0 — 2026-04-08

---

## 1. Orchestrator

| Aspect | General Default (`agent_turn`) | Main Agent |
|--------|-------------------------------|------------|
| Entry point | Caller invokes `agent_turn()` | `orchestrator.run()` → prepares context → calls `agent_turn()` |
| Return type | `AgentTurnResult` | `MainRunResult` (custom dataclass wrapping AgentTurnResult + orchestration metadata) |
| Multi-round | Not built-in | **Built-in** — orchestrator supports conversational follow-ups |
| Session management | None | Lightweight — output dir per run, no `init_session`/`reopen_session` (unlike Analysis) |

### `agent_turn()` parameter overrides

| Parameter | General Signature | Main Value |
|-----------|------------------|------------|
| `max_iterations` | (caller-supplied) | **40** (highest of all agents) |
| `timeout` | (caller-supplied) | **2400 s** (40 min — highest) |
| `required_tools` | `[]` | **`[]`** — no required tools (delegation is optional) |
| `compaction_interval` | (caller-supplied) | **999** (turn-based compaction disabled — size trigger governs) |
| `batch_summary_hook` | None | `_menu_batch_hook` — fires after tool-menu sequences |
| Verdict | External `VerdictRunner` | **Inline** via `MainVerdictRunner` in orchestrator |

---

## 2. Tier Structure

| Tier | Query Agent | Analysis Agent | Main Agent |
|------|-------------|----------------|------------|
| L0 | Orchestrator → dispatches to L1 | Orchestrator → calls tools directly | **Orchestrator → delegates to subagents** |
| L1 | Single dispatcher (12 iter, 360 s) | 2 specialized workers | **None** |
| L2 | 4 specialized searchers (6 iter, 90 s) | None | **None** |

Main agent is **single-tier only** — the simplest tier structure. All
substantive work goes to query/analysis agents as separate processes.

---

## 3. L0 Workflow → `main_agent_workflows/workflow.md`

### Phase Structure (4 phases)

| Phase | Name | Tools Used | Purpose |
|-------|------|-----------|---------|
| 1 | Understand | (no tools — LLM reasoning) | Parse user question, identify needed data/analyses |
| 2 | Delegate | `run_query_agent`, `run_analysis_agent`, `run_parallel_subagents` | Dispatch work to subagents |
| 3 | Synthesize | `browse_subagent_tools`, `run_subagent_tool` | Optional: fine-grained tool access for gap-filling |
| 4 | Report | (no tools — LLM synthesis) | Combine subagent results → final answer |

### Tool count: **5 delegation tools** (smallest of all agents)

| Agent | L0 Tools | Nature |
|-------|----------|--------|
| Query | 9 | Memory + dispatch |
| Analysis | 11 | Domain-specific |
| Main | **5** | **Pure delegation** |

---

## 4. No L1 Workers

Main agent has **zero L1 workers**. Unlike the query agent (which has an L1
dispatcher running sub-searches) and the analysis agent (which has an L1 query
delegation layer), the main agent dispatches subagent calls directly from L0.

Each `run_query_agent` / `run_analysis_agent` call invokes the target agent's
**full orchestrator** (not a lightweight worker). This means the main agent
sees only the final compacted result, never intermediate tool calls.

---

## 5. No L2 Workers

Main agent has **zero L2 workers**. No database access occurs at the main
agent level — all data retrieval is handled by the query agent.

---

## 6. Multi-Round Support (main-specific)

| Aspect | Query Agent | Analysis Agent | Main Agent |
|--------|-------------|----------------|------------|
| Multi-round | Not built-in | Session reopen | **Built-in conversational loop** |
| Follow-ups | External caller manages | `reopen_session()` | Orchestrator maintains `conversation_history` |
| Context carry-over | None | Via working memory file | Via `MainWorkingMemory.render()` injected into prompt |

Main orchestrator supports interactive follow-up questions by accumulating
`query_results` and `analysis_results` across turns in working memory, then
rendering the full context into each subsequent `agent_turn()` system prompt.

---

## 7. `MainRunResult` (custom return type)

```
@dataclass(frozen=True)
class MainRunResult:
    answer: str
    verdict: str
    elapsed_seconds: float
    tool_calls: int
    reasoning_tokens: int
    subagent_calls: list     # ← main-specific: [{agent, question, elapsed, tokens}]
    query_results: dict      # ← from working memory
    analysis_results: dict   # ← from working memory
```

General `AgentTurnResult` only has `answer`, `tool_calls`, `elapsed_seconds`,
`reasoning_tokens`. Main adds 3 orchestration-specific fields + verdict.

---

## 8. Parser / Workflow Rendering

| Aspect | General Default | Main Agent |
|--------|----------------|------------|
| `parse_workflow()` | From `general_subagent_skill_schema_and_parser` | **Re-exported** — no deviation |
| `render_prompt()` | From `general_subagent_skill_schema_and_parser` | **Re-exported** — no deviation |
| Workflow file format | Markdown with `[PHASE]` headers | Same |

---

## 9. Three-Agent Workflow Comparison

| Aspect | Query | Analysis | Main |
|--------|-------|----------|------|
| Tiers | 3 (L0/L1/L2) | 1 (L0 + L1 query delegation) | **1 (L0 only)** |
| L0 iterations | 20 | 30 | **40** |
| L0 timeout | 600 s | 1200 s | **2400 s** |
| Compaction interval | 999 (L1) | 9999 | **999** (turn-based disabled — size trigger governs) |
| L0 tool count | 9 | 11 | **5** |
| Tool nature | Memory + dispatch | Domain-specific | **Pure delegation** |
| Multi-round | No | Session-based | **Conversational loop** |
| Session management | No | Full (init/reopen/save) | **Lightweight (output dir)** |
| Unique workflow feature | Thin-answer guard | Required fitting tools | **Batch summary hook, tool menu** |
