# ThermoML Agent Framework

[Workspace setup](../README.md) · [Usage](../docs/USAGE.md) · [Data inventory](../docs/DATA.md)

The Main, Query, and Analysis agents share the engine described below.

## Three-Agent Architecture

The platform uses three cooperating agents that share a common engine:

| Agent | Location | Role |
|-------|----------|------|
| **Main** | `NIST_ThermoML_agents/_NIST_ThermoML_main_agent/` | L0 orchestrator — routes user questions to the appropriate sub-agent |
| **Query** | `NIST_ThermoML_agents/NIST_ThermoML_query_agent/` | Card-based data retrieval (search, filter, extract) |
| **Analysis** | `NIST_ThermoML_agents/NIST_ThermoML_analysis_agent/` | Statistical & comparative analysis of retrieved data |

### Shared Engine

All agents are built on the **general_db_query_engine** (`NIST_ThermoML_agents/general_db_query_engine/`), which provides:

- `general_argo_engine_helpers/` — argo loop (tool-call → LLM) execution engine
- `general_tool_management_helpers/` — tool catalog, registry, and dispatch
- `general_hooks_management_helpers/` — hook lifecycle (pre/post tool, validation, compaction)
- `general_subagent_delegation_helpers/` — shared delegation patterns (session nesting, question building, result extraction, parallel dispatch, tracking merge)
- `general_subagent_skill_schema_and_parser/` — skill definitions consumed by the LLM
- `general_db_search_tool_registry/` — search-tool discovery
- `general_text_context_marker_catalog/` — context-marker constants
- `general_ThermoML_db_csv_registry/` — CSV lookup indexes
- `general_DEBUG_test_runner_helpers/` — test harness utilities

### Entry Points

Each agent exposes a single API function that accepts a `session_dir` parameter for output tracking:

```python
from NIST_ThermoML_agents._NIST_ThermoML_main_agent.ThermoML_main_api import ThermoML_main_run
from NIST_ThermoML_agents.NIST_ThermoML_query_agent.ThermoML_query_api import ThermoML_query_run
from NIST_ThermoML_agents.NIST_ThermoML_analysis_agent.ThermoML_analysis_api import ThermoML_analysis_run
```

### Main Agent Toolbox

The main agent registers **5 tools** statically, plus a 6th (`list_session_files`) added dynamically by the orchestrator at runtime:

| Group | Tool | Purpose |
|-------|------|---------|
| Delegation | `run_query_agent` | Delegate a data-retrieval question to the query agent |
| Delegation | `run_analysis_agent` | Delegate an analysis question to the analysis agent |
| Delegation | `run_parallel_subagents` | Run query/analysis tasks in parallel; raw batch JSON is recorded in working memory, the orchestrator context receives an agentically compacted per-task report |
| Tool Menu | `browse_subagent_tools` | List tools available in a sub-agent |
| Tool Menu | `run_subagent_tool` | Execute a single sub-agent tool directly |
| Utility | `list_session_files` | List output files in the current session (added at runtime) |

Delegation logic is implemented via shared helpers in `general_subagent_delegation_helpers/` (not inline per-agent code).

### Call Hierarchy — exhaustive, down to the tools

Production-grammar view of the whole framework (`X → {…}` = X may invoke
each member; `∥` = parallel fan-out; `∘` = wrapped execution; every tool
name below is a literal `ToolEntry` registration; the funnel audit
`compaction_funnels/workflow_audits/hierarchy_audits.py` enforces this
tree on every generated workflow figure):

```
Main → { T_M , Q_i , A_i , ∥(Q ⊎ A) }                          Main orchestrator · shell 0
│ T_M = { run_query_agent → Q_i ,  run_analysis_agent → A_i ,
│         run_parallel_subagents → ∥(Q ⊎ A)  (internal agentic batch compaction),
│         browse_subagent_tools  (planning subagent over the hierarchical tool menu),
│         run_subagent_tool ∘ t , t ∈ T_L1 ∪ T_A^menu  (menu executes a single subagent
│                                tool under the owning agent's compaction pipeline),
│         list_session_files }
│ T_L1 (menu view) = T_id ∪ T_blk ∪ T_sim ∪ T_rank (the L1 search tools, defined below);
│ T_A^menu = { inspect_block , get_pure_values } ∪ T_fit ∪ { query_system_summary ,
│              query_blocks , find_similar_compounds } (the discovery trio is menu-only —
│              not registered in A_i's own loop)
│ memory: MainWorkingMemory (entity catalog + history, auto-recorded, re-rendered each
│         turn) ⊕ prev-prompt carry-over context (session continuity across prompts)
└ post-answer: claim ∥ id-align (tool-free) → construct_answer_summary → session ledger

Q_i → { T_mem , L1_1 … L1_k }                                  query agent L0 · shell 1
│ T_mem = { memory_read , memory_append_history , memory_add_result ,
│           memory_catalog_add , memory_catalog_remove , memory_catalog_list ,
│           memory_compact , memory_reset }
│         (session memory = working_memory.md; every L1_query payload is auto-archived
│          on return — L1AutoSaver)
└ post-answer: claim ∥ id-align → summary → return JSON

L1 → { T_id , T_blk , T_sim , L2_comp , L2_meas , L2_ref , L2_prop }
                                                               L1 query worker · shell 2
│ T_id   = { resolve_ids , resolve_compound_ids , resolve_property_ids ,
│            resolve_measurement_ids , resolve_reference_ids , search_id_alignment }
│ T_blk  = { search_blocks , block_search_adv , search_system_registry ,
│            search_system_summary }
│ T_sim  = { search_similar_compounds }
└ post-answer: claim ∥ id-align (tool-free) → core-ID validation loop
  { construct_core_blocks_found , construct_core_id_updates } → DB-hydrated payload JSON

L2_comp → { search_comp_from_block , search_compound_dk , search_compound_indiv }
L2_meas → { search_meas_from_block , search_measurement_dk , search_measurement_indiv }
L2_ref  → { search_reference_from_block , search_references }
L2_prop → { search_prop_dk_from_block , search_property_dk }
          L2 leaf evaluators · shell 3 — card-read tools run skip_subagent (only the meas
          pair has a det compactor): the evaluator's WRITTEN ANSWER is the agentic stage;
          its post-answer id-alignment runs construct_l2_compounds / construct_l2_measurements /
          construct_l2_properties / construct_l2_reference

A_i → { T_ev , T_fit , T_cust ,
        query_thermoml[_parallel]   → L1        (headless — no Q L0 shell, in-process),
        align_compositions          → L1_align  (analysis' own L1 worker),
        run_query_agent[s_parallel] → Q_j       (nested FULL query hierarchy, own session) }
                                                               analysis agent L0 · shell 1
│ T_ev   = { inspect_block , get_pure_values , list_session_files }
│ T_fit  = { fit_block , fit_block_derived , fit_multi_system ,
│            compute_ideal_baseline , predict_from_rk , propose_fitting_plan }
│ T_cust = { register_custom_block }
│ (resolve_compounds / resolve_properties / query_blocks / query_system_summary /
│  find_similar_compounds are compactor-only sub-step keys, not agent-facing tools)
│ memory: AnalysisWorkingMemory — ID catalog + auto-extraction from inspect_block /
│         get_pure_values / fit_block results (synced to _working_memory.md)
└ post-answer: claim ∥ id-align → summary / verdict → return JSON

L1_align → { search_blocks , search_system_registry , resolve_compound_ids ,
             inspect_block , get_pure_values , fit_block ,
             validate_dual_basis_block , register_estimated_bridge }
           mixed query+analysis catalog · shell 2 (same claim ∥ id-align post-answer)
```

Two invariants hold at every shell:

```
∀ shell, ∀ tool call t :   raw(t) → det(t) → kept(t) → ctx
    det  = hardcoded deterministic compactor (full | condense | ultra_condense | adaptive)
    kept = agentic KEEP/DISCARD triage subagent; skip_compactor / skip_subagent short-circuit
    side-channels: [WM] verbatim payload archive · [ID] add-only ID catalog (dedup)

∀ agentic shell S :   answer(S) → claim(S) ∥ id-align(S) → construct_*(S) → JSON(S)
    construct_* by tier: L0 → construct_answer_summary · L1 → construct_core_* · L2 → construct_l2_*
```

Memory tiers: **session memory** (Main working memory ⊕ prompt carry-over ·
query `working_memory.md` via the 8 `memory_*` tools · analysis working-memory
auto-extraction) and **transient memory** (dispatch briefs — purpose,
instruction, id_catalog, context — flowing down Main → {Q,A} → L1 → L2, plus
relay-carried ids never logged at a tool stage).

---

## Source layout and outputs

The agent project contains `NIST_ThermoML_agents`, `card_db_search_tools`,
the parsers/compactors, and the data directories.
The browser is a sibling package: `../ThermoML_results_browser`.

From this agent-project folder, freeform sessions use `../_output/{Main,Query,Analysis}`;
benchmarks use `../_benchmark/{Main,Query,Analysis}`. Components declare paths directly and
retain explicit session overrides. No user-bucket output router is required.

## Setup and validation

Use the [workspace installation guide](../docs/INSTALLATION.md),
[API examples](../docs/USAGE.md), and [offline checks](../docs/DEVELOPMENT.md).
Launch the browser with `python launch_thermoml_browser.py` from the parent
project root. [BENCHMARKS.md](../docs/BENCHMARKS.md) distinguishes live prompt
runners from offline validation.

## Further reading

- [Platform architecture](../MASTER_ARCHITECTURE.md)
- [Strict identifier grammar](card_databases_storage/ID_architecture.md)
- [Agent-layer architecture](NIST_ThermoML_agents/ARCHITECTURE.md)
- [Browser reference](../ThermoML_results_browser/README.md)
