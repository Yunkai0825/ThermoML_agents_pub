# general_subagent_delegation_helpers — Shared Subagent Delegation Patterns

Reusable primitives for any agent that delegates work to another
agent's public API.  Extracted from the main agent's
`subagent_delegation_tools.py` so that both the **Main Agent** and the
**Analysis Agent** (and any future agent) share identical session
nesting, question enrichment, result extraction, parallel dispatch,
and tracking-file combination logic.

---

## Dependency Injection Pattern

`SubagentSessionManager` takes a `get_session` callable (zero-arg →
`SessionManager | None`) so this package **never imports agent-specific
code**.  The caller supplies its own hook catalog's session accessor:

```python
from ...general_db_query_engine.general_subagent_delegation_helpers import (
    SubagentSessionManager,
)
_sessions = SubagentSessionManager(
    get_session=lambda: hook_catalog.session_manager  # injected
)
```

---

## Public Exports

All symbols are re-exported from `__init__.py` except
`write_subagent_result_md`, which `extract_run_result` calls internally.

| Symbol | Module | Signature | Purpose |
|--------|--------|-----------|---------|
| `SubagentSessionManager` | `_session_nesting.py` | `(get_session: Callable[[], SessionManager \| None])` | Thread-safe nested session dirs (`<parent>/<agent>_runs/run_<N>/`) |
| `preserve_active_session` | `_session_nesting.py` | context manager | Saves/restores the active-session `ContextVar` around a child run so combined roll-ups land at the parent session root |
| `build_full_question` | `_question_builder.py` | `(question, purpose="", tasks="", context="") -> str` | Injects `[Purpose:]`, `[Tasks:]`, `[Context:]` markers |
| `extract_run_result` | `_result_extractor.py` | `(result, agent_type, question, session_dir, *, extra=None) -> dict` | Exact flat dict from a query/analysis `RunResult` |
| `write_subagent_result_md` | `_result_extractor.py` | `(session_dir, result_dict) -> None` | Writes `result.md` into a child session dir (skipped if the child already wrote one) |
| `dispatch_parallel` | `_parallel_dispatch.py` | `(tasks, runner_fn, *, max_workers=3, ...) -> dict` | Native task-array dispatch with label management, `copy_context` isolation, error capture, and ordered results |
| `merge_subagent_tracking` | `_tracking_combiner.py` | `(main_dir, subagent_dir, agent_type, label="") -> None` | Parses + merges `reference_stats.md`, `run_history.md`, `reasoning_tokens_stripped.md` with `label (query_runs/run_N)` source tagging |

---

## Module Details

### `_session_nesting.py` — `SubagentSessionManager` + `preserve_active_session`

Thread-safe manager that creates nested subdirectories inside a parent
agent's active session so that each subagent run's output is co-located.

- `get_subagent_session_dir(agent_type)` → `Path | None`
- `get_parent_session_dir()` → `Path | None`

`preserve_active_session()` must wrap every same-thread child-runner call:
child runs set the active-session `ContextVar` for their own hooks, and
without the save/restore the parent's post-run roll-ups would be written
inside the child's directory.

### `_question_builder.py` — `build_full_question()`

Prepends / appends structured markers to a question string before
dispatching it to a subagent.

### `_result_extractor.py` — `extract_run_result()` + `write_subagent_result_md()`

Extracts a standardised flat dict (`answer`, `iterations`,
`elapsed_seconds`, `tool_count`, `timed_out`, `agent`, …) from any
`RunResult`-like object returned by an agent's public API, and persists
a `result.md` into child session dirs that did not write their own.

### `_parallel_dispatch.py` — `dispatch_parallel()`

Wraps `ThreadPoolExecutor` with task-array validation, per-task kwargs
extraction, error capture, and ordered result collection. Each task runs
under `contextvars.copy_context()` so nested session/config registries
never leak across workers. Returns `{"n_tasks": N, "results": [...]}`;
a failed task becomes `{"label", "error", "agent"}` in place.

### `_tracking_combiner.py` — `merge_subagent_tracking()`

Parses markdown tables from subagent tracking files, adds a **Source**
column to every data row, and writes/updates combined files in the
parent's session directory.  Also includes generic table-parsing helpers
(`_extract_tables`, `_recompute_total`, `_render_table`).

---

## Consumers

| Agent | Module | Imports |
|-------|--------|---------|
| Main Agent | `main_agent_toobox/subagent_delegation_tools.py` | All 5 exports |
| Analysis Agent | `analysis_agent_toolbox/sibling_agent_delegation_tools/query_agent_tool.py` | All 5 exports |
