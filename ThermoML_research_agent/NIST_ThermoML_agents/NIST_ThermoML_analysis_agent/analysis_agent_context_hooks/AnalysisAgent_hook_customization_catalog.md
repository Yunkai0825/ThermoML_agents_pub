# Analysis Agent — Hook Customization Catalog

> Deviations from `general_hooks_management_helpers/` defaults.
> Version 6.0 — 2026-04-08

---

## 1. Anchor Wiring

All 8 standard anchors wired to **analysis-specific singletons**.

| Anchor | Handler | Deviations from General |
|--------|---------|------------------------|
| `ON_REASONING` | `AnalysisReasoningTokenTracker` singleton | Identical to general; no deviation |
| `ON_TOOL_RESULT` | `AnalysisToolResultCompactor` singleton | Custom compactors; uses `for_l1_data` client |
| `ON_TOOL_CALL` | `AnalysisHistoryRecorder` singleton | Empty subclass of `HistoryRecorder` |
| `ON_TOOL_ERROR` | `AnalysisStatsRecorder` singleton | Pinned config fields |
| `ON_PURPOSE_ERROR` | `AnalysisStatsRecorder` singleton | Same singleton as ON_TOOL_ERROR |
| `ON_STAGE_COMPACT` | `AnalysisStageCompactor` singleton | Budget differs from general default |
| `ON_COMPACTION` | `AnalysisInteractiveCompactor` singleton | PROTECT_TOOLS=6, domain_hint set |
| `ON_COMPACTION_STATS` | `AnalysisStatsRecorder` singleton | Same singleton |

---

## 2. Stage Compactor → `AnalysisStageCompactor`

| Aspect | General Default | Analysis Agent |
|--------|----------------|----------------|
| Base class | `StageCompactor` | `AnalysisStageCompactor(StageCompactor)` |
| Budget (tokens) | N/A (caller-supplied) | Config-pinned: `STAGE_COMPACTION_BUDGET` field in AnalysisAgentConfig |
| Config source | Passed at call time | Pinned from `AnalysisAgentConfig` at construction |

---

## 3. Tool-Result Compactor → `AnalysisToolResultCompactor`

| Aspect | General Default (`ToolResultCompactor`) | Analysis Agent |
|--------|----------------------------------------|----------------|
| Subclass | `ToolResultCompactor` (base) | `AnalysisToolResultCompactor(ToolResultCompactor)` |
| Client factory | Generic `ArgoClient()` | `AnalysisClient.for_l1_data()` — baked-in model/budget |
| Number of compactors | N/A | **12+** domain-specific compactors |
| 2-layer pipeline | Same | Deterministic schema compactor → mandatory LLM KEEP/DISCARD review |

### Compactor Registry

| Compactor Key | Deterministic projection? | Mandatory LLM review? | Notes |
|---------------|---------------------------|-----------------------|-------|
| `compact_resolve_compounds` | ✓ | — | Dict→markdown only |
| `compact_resolve_properties` | ✓ | — | Dict→markdown only |
| `compact_query_system_summary` | ✓ then LLM | ✓ | Structured extract + LLM polish |
| `compact_query_blocks` | ✓ then LLM | ✓ | Block list summary |
| `compact_inspect_block` | ✓ | — | Deterministic extraction |
| `compact_get_pure_values` | ✓ | — | Deterministic extraction |
| `compact_find_similar_compounds` | ✓ then LLM | ✓ | Similarity ranking reduction |
| `compact_fit_block` | ✓ | — | Hardcoded: BIC table, R², RMSE, coefficients, paths |
| `compact_fit_multi_system` | ✓ | — | Per-system summary aggregation |
| `compact_fit_block_by_temp` | ✓ | — | Per-isotherm coefficient table |
| `compact_fit_block_multi_prop` | ✓ | — | Multi-property coefficient table |
| `compact_compute_ideal_baseline` | ✓ | — | Curve statistics summary |
| `compact_predict_from_rk` | ✓ | — | Prediction statistics summary |

**Key pattern:** every fitting result has a deterministic numerical projection;
the subsequent LLM stage may KEEP or DISCARD it but cannot substitute a missing
compactor or silently pass through malformed output.

---

## 4. Interactive Compactor → `AnalysisInteractiveCompactor`

| Aspect | General Default | Analysis Agent |
|--------|----------------|----------------|
| `PROTECT_TOOLS` | `[]` (empty) | **6 fitting tools** — exempt from LLM compaction |
| `domain_hint` | `""` (none) | `"Redlich-Kister fitting and thermodynamic data analysis"` |
| Behavior | Compresses all tool results | **Skips** results from protected tools; compresses others |
| Prompt template | General compaction prompt | `domain_hint` injected into prompt for LLM context |

---

## 5. Working Memory → `AnalysisWorkingMemory`

| Aspect | General Default (`BaseWorkingMemory`) | Analysis Agent |
|--------|---------------------------------------|----------------|
| Superclass | `BaseWorkingMemory` (abstract) | `AnalysisWorkingMemory(WorkingMemory)` — inherits FILE-BACKED WorkingMemory but operates **in-memory** |
| Storage | Abstract | In-memory dicts (NOT file-backed despite inheritance) |
| Structured fields | None | `query_results`, `inspected_blocks`, `fit_results`, `history` |
| Auto-extraction | None | `record_tool_result()` dispatches by 8+ tool-name prefixes |
| `sync_to_disk()` | (in WorkingMemory: MCP file-backed) | Writes `working_memory.json` to session dir only when session is active |

### `record_tool_result()` dispatch map

| Tool name prefix | Storage target | Extraction logic |
|-----------------|---------------|-----------------|
| `query_thermoml` | `query_results` | DOI + summary |
| `inspect_block` | `inspected_blocks` | Full block meta + ID-catalog ingest |
| `get_pure_values` | compound entities | Merges pure values per compound |
| `align_compositions` | `composition_library` | Bridge, molar masses, translation-table refs |
| `fit_block` / `fit_block_derived` | `fit_results` | Shape-dispatched: single fit, per-isotherm sweep (`per_sweep_value`), or multi-property (`results`) |
| `fit_multi_system` | `fit_results` (per-system) | Aggregated multi-system |
| `resolve_compounds` / `resolve_properties` | ID catalog | exact typed `GLOB*` entries |

### `render()` sections

Returns a structured string with sections:
1. **ROOT / ID Catalog** — resolved compounds / properties
2. **History** — timestamped action log
3. **Query Results** — per-DOI summaries
4. **Completed Fits** — per-DOI fit quality tables
5. **Session Manifest** — session dir, open files list

---

## 6. Hooks Not Present in Analysis Agent

| Hook | Present in Query? | Present in Analysis? | Notes |
|------|-------------------|---------------------|-------|
| `L1AutoSaver` | ✓ | ✗ | No L1 sub-dispatchers in analysis |
| `thin_answer_guard` | ✓ | ✗ | Analysis has no thin-answer detection |
| `adaptive_condense` | ✓ (on search_blocks, search_system_registry) | ✗ | Analysis doesn't search directly |

---

## 7. Verdict Runner → `AnalysisVerdictRunner`

| Aspect | Query Agent | Analysis Agent |
|--------|-------------|----------------|
| Sections | 1 (Scientific Review) | **3** (Data Quality / Fit Quality / Scientific) |
| Fabrication detection | Not present | **Yes** — checks for fabricated data references |
| `answer_char_limit` | 150 words (word cap) | **4000 chars** (char cap, much larger) |
| `include_elapsed` | True | **False** |
| Prompt style | Concise scientific review | Multi-section structured scientific assessment |
