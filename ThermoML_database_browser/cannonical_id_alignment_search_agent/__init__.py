"""
Canonical ID Alignment Search Agent for the ThermoML Browser.

Resolves free-text search queries into canonical IDs (comp_num_id,
prop_num_id, var_num_id, meas_num_id, lit_num_id, constr_num_id)
that the index DB can use for filtering.

Two execution paths
-------------------
**Deterministic (fast)** — ``hardcoded_search_helpers.dispatch_search()``
    Hard parser → ID workers → merge → ResolvedQuery.

**Argo Agent (LLM-driven)** — ``alignment_agent_api.alignment_agent_run()``
    Proper Argo ReAct agent with MCP tools:
    parse_smart_search → resolve_entity → validate_field →
    validate_bibliography → set_field → review_top_results →
    finalize_fields.

    Uses ``AlignmentAgentConfig(EngineConfig)``, ``AlignmentClient(ArgoClient)``,
    ``AlignmentL0Catalog(AgentToolCatalog)``, and ``agent_turn()`` loop
    from ``general_argo_engine_helpers``.

Package layout
--------------
hardcoded_search_helpers/     — deterministic helpers (no LLM)
  search_parser.py            — hard parser (deterministic first pass)
  id_workers.py               — fuzzy ID resolution workers
  dispatcher.py               — deterministic dispatch + SQL builder
  bibliography_scorer.py      — keyword-weighted title search
  validation_tools.py         — field validation against registries
  review_workers.py           — review workers for top results
alignment_agent_api.py        — public API: alignment_agent_run()
alignment_agent_argo_config.py — EngineConfig subclass
alignment_agent_argo_engine/  — ArgoClient factory
alignment_agent_toolbox/      — MCP tools + tool catalog
alignment_agent_workflows/    — L0 orchestrator + workflow markdown
"""

