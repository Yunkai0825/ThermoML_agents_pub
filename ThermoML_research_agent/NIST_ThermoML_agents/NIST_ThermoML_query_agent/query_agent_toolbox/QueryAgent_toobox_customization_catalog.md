# Query Agent — Toolbox Customization Catalog

> Deviations from `general_tool_management_helpers/` defaults.
> Version 6.0 — 2026-04-08

---

## 1. L0 Tool Catalog → `QueryL0Catalog`

| Aspect | General Default (`AgentToolCatalog`) | Query Agent Override |
|--------|-------------------------------------|---------------------|
| Subclass | `AgentToolCatalog` (base) | `QueryL0Catalog(AgentToolCatalog)` |
| `pipeline_label` | `""` (unset) | `"query"` |
| `PROTECT_TOOLS` | N/A | None — no tools protected from compaction |

### L0 Registered Tools (8 memory tools)

| Tool | Group | `skip_compactor` | `skip_subagent` | Notes |
|------|-------|-------------------|------------------|-------|
| `memory_read` | `memory` | ✓ | ✓ | All memory tools return strings |
| `memory_append_history` | `memory` | ✓ | ✓ | — never need compaction |
| `memory_add_result` | `memory` | ✓ | ✓ | |
| `memory_catalog_add` | `memory` | ✓ | ✓ | |
| `memory_catalog_remove` | `memory` | ✓ | ✓ | |
| `memory_catalog_list` | `memory` | ✓ | ✓ | |
| `memory_compact` | `memory` | ✓ | ✓ | |
| `memory_reset` | `memory` | ✓ | ✓ | |

**Dynamic registration:** `L1_query` is added at runtime in `orchestrator.py`,
wrapped by `L1AutoSaver` for auto-save to working memory.

**Why only memory tools at L0:** The query agent's L0 orchestrator manages
memory and dispatches L1 workers. All database search tools live at L1/L2.

---

## 2. L1 Tool Catalog → `QueryL1Catalog`

| Aspect | Value |
|--------|-------|
| `pipeline_label` | `"query"` |
| `client_factory` | `QueryClient.for_l1()` (singleton) |

### L1 Registered Tools (16)

| Tool | Group | Compactor | `skip_subagent` | Notes |
|------|-------|-----------|------------------|-------|
| `resolve_ids` | `id_resolution` | `compact_resolve_ids` | — | |
| `resolve_compound_ids` | `id_resolution` | `compact_resolve_compound_ids` | — | |
| `resolve_property_ids` | `id_resolution` | `compact_resolve_property_ids` | — | |
| `resolve_measurement_ids` | `id_resolution` | `compact_resolve_measurement_ids` | — | |
| `resolve_reference_ids` | `id_resolution` | `compact_resolve_reference_ids` | — | |
| `search_id_alignment` | `id_resolution` | `compact_search_id_alignment` | — | |
| `search_blocks` | `block_search` | `compact_search_blocks` | — | `adaptive_condense=True` |
| `block_search_adv` | `block_search` | `compact_block_search_adv` | — | Flat exact-row/role-aware advanced search |
| `inspect_block_table` | `block_search` | `compact_inspect_block_table` | ✓ | Verbatim grounding table |
| `search_system_registry` | `block_search` | `compact_search_system_registry` | — | `adaptive_condense=True` |
| `search_system_summary` | `block_search` | `compact_search_system_summary` | — | |
| `search_similar_compounds` | `compound_similarity` | `compact_search_similar_compounds` | — | |
| `L2_comp_eval` | `L2_subagents` | — | ✓ | skip_compactor=True |
| `L2_meas_eval` | `L2_subagents` | — | ✓ | skip_compactor=True |
| `L2_ref_eval` | `L2_subagents` | — | ✓ | skip_compactor=True |
| `L2_prop_eval` | `L2_subagents` | — | ✓ | skip_compactor=True |

**Compactor source:** L1 filters the shared 29-entry catalog to the 12 compacted
tools it actually exposes; the four L2 dispatchers bypass both compaction
layers.

**Custom hook:** `_on_raw_result` logs DOI/block + entity references
via `query_stats_recorder` — not in base class.

---

## 3. L2 Tool Catalogs (4 lightweight catalogs)

| Catalog | `pipeline_label` | Tools | Compaction |
|---------|-------------------|-------|------------|
| `L2CompCatalog` | `"query-l2-comp"` | `search_comp_from_block`, `search_compound_dk`, `search_compound_indiv` | All `skip_compactor=True, skip_subagent=True` |
| `L2MeasCatalog` | `"query-l2-meas"` | `search_meas_from_block`, `search_measurement_dk`, `search_measurement_indiv` | All skip |
| `L2RefCatalog` | `"query-l2-ref"` | `search_reference_from_block`, `search_references` | All skip |
| `L2PropCatalog` | `"query-l2-prop"` | `search_prop_dk_from_block`, `search_property_dk` | All skip |

**Why skip compaction at L2:** L2 tools are raw callables passed to
`agent_turn()`. The L2 agent interprets results within its small token
budget (2000 tokens). No compaction pipeline needed.

---

## 4. Key Deviations from Base Pattern

| Base Pattern | Query Agent Deviation | Why |
|-------------|----------------------|-----|
| Single tool catalog per agent | **3-tier catalogs** (L0 + L1 + 4×L2) | Matches 3-tier ReAct hierarchy |
| Compaction on all tools | L0 memory tools skip entirely; L2 tools skip entirely | Memory returns strings; L2 is self-contained |
| Static tool registration | `L1_query` registered dynamically at runtime | Wrapped by `L1AutoSaver` for auto-memory-save |
| Base `compact_tool_result` only | L1 uses full 2-layer pipeline (hardcoded + agentic) | L1 search results need both dict→markdown and KEEP/DISCARD triage |
