# L1 Workers

Intermediate-layer agents that perform database searches and data evaluation.

## Files

| File | Purpose |
|------|---------|
| `l1_query_dispatcher.py` | `dispatch_l1_query()` — builds tool registry, launches L1 agent_turn |
| `L1_query_workflow.md` | System prompt, 11 search tools + L2 subagents, 4 phases |

## How `dispatch_l1_query` Works

```
dispatch_l1_query(purpose, instruction, id_catalog, context)
    │
    ├─ Parse L1_query_workflow.md
    ├─ Render prompt with {{purpose}}, {{instruction}}, {{id_catalog}}, {{context}}
    ├─ Build tool registry:
    │     resolve_compound_ids    → _id_alignment_search
    │     resolve_property_ids    → _id_alignment_search
    │     resolve_measurement_ids → _id_alignment_search
    │     search_blocks           → 1_block_search
    │     search_system_registry  → 2_system_registry_search
    │     search_compound_dk      → 3_compound_DK_search
    │     search_references       → 4_reference_search
    │     search_measurement_dk   → 5_meas_DK_search
    │     search_measurement_indiv → 6_meas_INDIV_search
    │     search_system_summary   → 9_system_summary_search
    │     search_similar_compounds → 10_compound_similarity_search
    │     L2_comp_eval            → l2_dispatchers.dispatch_l2_comp_eval
    │     L2_meas_eval            → l2_dispatchers.dispatch_l2_meas_eval
    │     L2_ref_eval             → l2_dispatchers.dispatch_l2_ref_eval
    │     L2_prop_eval            → l2_dispatchers.dispatch_l2_prop_eval
    │
    ├─ agent_turn(...) → answer text only
    ├─ one anchor → parallel claim + ID/metadata agents
    └─ deterministic assembly/ID validation → downstream JSON string
```

## L1 Query Workflow Phases

| Phase | Name | Tools | Purpose |
|-------|------|-------|---------|
| 1 | `resolve_ids` | resolve_*_ids | Convert human names → typed `GLOB*` IDs |
| 2 | `search_and_retrieve` | search_* tools | Query databases for matching data |
| 3 | `deep_evaluate` | L2_* subagents | Parallel L2 evaluation of individual blocks |
| 4 | `synthesize` | — | Write the complete chemistry answer text |

The L1 working agent does not construct the downstream JSON. One shared
anchor launches the claim agent and ID/metadata agent concurrently. The ID
agent emits only minimal batched `core_id_updates` and `core_blocks_found`
inputs. Two hidden registered tools, `construct_core_id_updates` and
`construct_core_blocks_found`, execute independently to validate and construct
all registry-owned names and block context. Tool errors become ReAct
observations for bounded correction. A final submit/refine review runs before
deterministic assembly inserts the untouched answer and claim list.

## Efficiency Rules (from workflow)

- For availability/overview queries: call ONLY `search_system_summary`
- For specific data: call ONLY `search_blocks`
- Do NOT call both `search_blocks` AND `search_system_registry` for the same query
- Stop searching as soon as you have enough data to answer

## Observability Hooks

Every tool call inside `dispatch_l1_query` feeds raw results to two passive
recorders (from `memory_management_MCP_tools/`):

- **`HistoryRecorder`** → `run_history.md` (chronological event log)
- **`StatsRecorder`** → `reference_stats.md` (Argo stats, entity references, DOI/block counts)

Hooks called: `log_doi_block_references()` and `log_entity_references()`
on every raw result dict.
