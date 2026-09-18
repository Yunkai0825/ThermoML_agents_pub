# Alignment Agent — Workflows

Orchestrator workflow for the alignment agent's ReAct loop.

## Files

| File | Purpose |
|------|---------|
| `L0_orchestrator/orchestrator.py` | Main orchestration logic |
| `L0_orchestrator/L0_orchestrator_workflow.md` | Workflow specification (prompt / plan) |
| `__init__.py` | Package init |

## L0 Orchestrator

The L0 (layer-0) orchestrator defines the multi-step plan the agent
follows when resolving a query:

1. Parse the raw query via deterministic parser
2. Resolve entities to canonical IDs
3. Validate resolved values against the index
4. Fill search-form blocks (bibliography, chemistry, properties, etc.)
5. Review top results for relevance
6. Finalize fields and return

The workflow markdown file is loaded as part of the agent system prompt.
