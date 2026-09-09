# query_agent_context_hooks

All runtime context hooks for the ThermoML Query Agent.
Single entry point: `hook_catalog.py` (re-exported via `__init__.py`).

## Five Hook Categories

| Sub-package | Key Exports | Purpose |
|-------------|-------------|---------|
| `compactor_hooks/` | `QueryStageCompactor`, `QueryToolResultCompactor`, `ToolResult`, `COMPACTOR_CATALOG`, `COMPACTOR_REGISTRY` | Stage-level + per-tool-result compaction |
| `interactive_hooks/` | `QueryInteractiveCompactor` | LLM-driven 3-step context compaction (SELECT → COMPRESS → VALIDATE) |
| `memory_hooks/` | `QueryWorkingMemory`, `init_working_memory`, `make_wm_loader`, `L1AutoSaver` | Agent working memory lifecycle |
| `tracking_hooks/` | `QueryHistoryRecorder`, `QueryStatsRecorder`, `QueryTimeBudgetTracker` | Observability — history log, entity stats, time budget |
| `verdict_hooks/` | `QueryVerdictRunner`, `run_verdict`, `save_final_context` | Post-job scientific quality review |

## Usage

```python
from .hook_catalog import QueryInteractiveCompactor
from .hook_catalog import query_history_recorder
from .hook_catalog import run_verdict, save_final_context
from .hook_catalog import QueryWorkingMemory, init_working_memory
```

Each sub-package wraps a shared base class from `general_context_hooks/`
or `general_memory_management_tools_hooks_helpers/` with query-agent-specific
configuration.
