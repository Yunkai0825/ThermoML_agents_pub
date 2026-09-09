# query_agent_argo_engine

Query-agent-specific ArgoClient factories and terminal UI.

## Public API

```python
from .argo_client import QueryClient

client = QueryClient.for_l0()   # L0 orchestrator
client = QueryClient.for_l1()   # L1 worker
client = QueryClient.for_l2()   # L2 leaf evaluator
```

`QueryClient` extends `general_argo_engine_helpers.ArgoClient` with
factory methods that read budgets from `ThermoML_query_argo_config.AGENT_CONFIG`.

## Files

| File | Purpose |
|------|---------|
| `__init__.py` | Loads query config into the shared engine, re-exports `QueryClient` |
| `argo_client.py` | `QueryClient(ArgoClient)` with `for_l0`, `for_l1`, `for_l2` factories |
| `query_agent_terminal_ui.py` | `QueryTerminalUI(ArgoAgentTerminalUI)` — terminal display callbacks |
