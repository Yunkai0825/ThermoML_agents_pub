# ThermoML Agent Framework

> Card-based agentic platform for exploring the NIST ThermoML Archive  
> (v2020-09-30 — 11,923 papers · ~2.7 M source rows · 110 property IDs · 8,526 compounds)

For setup and everyday use, start with the [workspace README](../README.md) and
[usage guide](../docs/USAGE.md). This document describes the agent internals.
The bundled databases contain NIST/TRC ThermoML Archive data; the citations NIST
requests are listed in the workspace README's
[license, data source, and citation](../README.md#license-data-source-and-citation)
section.

## Three-Agent Architecture

The platform uses three cooperating agents that share a common engine:

| Agent | Location | Role |
|-------|----------|------|
| **Main** | `NIST_ThermoML_agents/_NIST_ThermoML_main_agent/` | L0 orchestrator — routes user questions to the appropriate sub-agent |
| **Query** | `NIST_ThermoML_agents/NIST_ThermoML_query_agent/` | Card-based data retrieval (search, filter, extract) |
| **Analysis** | `NIST_ThermoML_agents/NIST_ThermoML_analysis_agent/` | Statistical & comparative analysis of retrieved data |

A stub exists for a future **Editing** agent (`NIST_ThermoML_agents/NIST_ThermoML_editing_agent(stub)/`).

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

L1 → { T_id , T_blk , T_sim , T_rank , L2_comp , L2_meas , L2_ref , L2_prop }
                                                               L1 query worker · shell 2
│ T_id   = { resolve_ids , resolve_compound_ids , resolve_property_ids ,
│            resolve_measurement_ids , resolve_reference_ids , search_id_alignment }
│ T_blk  = { search_blocks , block_search_adv , search_system_registry ,
│            search_system_summary }
│ T_sim  = { search_similar_compounds }      T_rank = { screen_property_systems }
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

## Top-Level Directory Map

```
ThermoML_research_agent/
├── NIST_ThermoML_agents/           # Agent code (main, query, analysis, shared engine)
├── card_databases_storage/         # Pre-built card databases (JSON + SQLite) + ID_architecture.md
├── card_db_search_tools/           # Search-tool implementations (component, measurement, property, DOI, block)
├── specialized_tools_pipelines/    # Deterministic multi-stage pipelines (property screening & ranking)
├── ThermoML_card_json_to_md_compactors/  # JSON→Markdown compactors for token-efficient output
├── ThermoML_raw_json_to_card_db_parsers/ # Raw JSON/SQLite→card-JSON parsers + id_schema.py (ID grammar)
├── ThermoML.v2020-09-30.db/        # Raw NIST archive + raw-DB docs
├── __tmp__/                       # Archived scratch work and publication audits
├── run_debug_benchmark.py          # Batch debug-prompt benchmark runner (main → query → analysis)
├── MASTER_ARCHITECTURE.md          # Full system architecture reference
└── README.md                       # ← this file
```

Scratch and concluded campaign artifacts live in `__tmp__/` here or at the
workspace root.

Output locations are declared directly in the agent configs, benchmark runners,
and diagnostic scripts, relative to their source files:

- `../_benchmark/{Main,Query,Analysis}/` holds benchmark campaigns and sessions.
- `../_output/{Main,Query,Analysis}/` holds persistent freeform sessions and diagnostics shared by all visitors.
- Existing Main sessions directly under `../_output/` remain available in the browser.

These paths do not depend on the current working directory. Explicit `session_dir`
and runner `--output` arguments are still supported.

---

## Quick Start

Install dependencies from this project directory with
`python -m pip install -r requirements.txt` (or `requirements-dev.txt` for tests).
Set `ARGO_API_USER` to your Argo username for live agent calls; the benchmark
launcher preserves your environment rather than selecting a personal account.

### Run the test suites

```bash
# Live agent prompt suites (per agent; requires Argo access)
python -m NIST_ThermoML_agents._NIST_ThermoML_main_agent._DEBUG_script.run_tests          # all main-agent prompts
python -m NIST_ThermoML_agents.NIST_ThermoML_query_agent._DEBUG_script.run_tests 1.1 2.1  # specific query prompts
python -m NIST_ThermoML_agents.NIST_ThermoML_analysis_agent._DEBUG_script.run_tests --section 2

# Combined benchmark (configured prompt cohorts, three agents, ../_benchmark)
python run_debug_benchmark.py --offline # imports/config/output plan; no network or credentials
python run_debug_benchmark.py          # preflight only — health-check + run plan, no launches
python run_debug_benchmark.py --go     # launch; add --resume <TS> to continue an interrupted test_run

# Deterministic regression suites (no LLM)
python -m pytest card_db_search_tools/DEBUG_tools_scripts -q
python -m pytest specialized_tools_pipelines/property_screening_ranking_tool/tests -q
```

The combined launcher has an explicit Main filter; its 17 listed IDs currently
match 16 cases. Query and Analysis use all current prompts. See the
[benchmark guide](../docs/BENCHMARKS.md) for exact selection and resume behavior.

### Launch the browser app

The browser is in the sibling `../ThermoML_database_browser/` folder.

```bash
# From the containing workspace (starts the server and opens your browser)
python launch_thermoml_browser.py

# Or from this project directory
python ../launch_thermoml_browser.py
```

---

## Further Reading

- [MASTER_ARCHITECTURE.md](MASTER_ARCHITECTURE.md) — card schemas, data flow, full system design
- [card_databases_storage/ID_architecture.md](card_databases_storage/ID_architecture.md) — the strict identifier grammar (GLOB*/DOI*/BLK* scopes)
- [NIST_ThermoML_agents/ARCHITECTURE.md](NIST_ThermoML_agents/ARCHITECTURE.md) — agent-layer architecture
- [specialized_tools_pipelines/property_screening_ranking_tool/README.md](specialized_tools_pipelines/property_screening_ranking_tool/README.md) — deterministic screening & ranking pipeline
- [ThermoML_database_browser/README.md](../ThermoML_database_browser/README.md) — browser app docs
