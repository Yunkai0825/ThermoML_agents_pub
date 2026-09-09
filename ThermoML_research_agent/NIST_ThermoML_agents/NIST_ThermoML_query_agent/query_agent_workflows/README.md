# query_agent_workflows

Orchestration layer for the ThermoML Query Agent.
Three-tier architecture: L0 → L1 → L2.

## Sub-packages

| Directory | Purpose |
|-----------|---------|
| `L0_orchestrator/` | Entry point — `run()`, `QueryRunResult`, ReAct loop |
| `L1_workers/` | `l1_query_dispatcher` — spawns parallel L2 evaluators |
| `L2_leaf_evaluators/` | Single-card evaluation (search → inspect → answer) |
| `_subworkflow_md_parser/` | Parses `.md` workflow templates into structured steps |

## Tier Budget Summary

| Tier | Model | Max Iterations | Time Budget |
|------|-------|---------------|-------------|
| L0 | claudeopus46 | 25 | 600 s |
| L1 | claudeopus46 | 15 | 240 s |
| L2 | claudeopus46 | 8 | 120 s |
