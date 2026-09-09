# Main Agent — Hook Customization Catalog

> Deviations from `general_hooks_management_helpers/` defaults.
> Version 6.0 — 2026-04-08

---

## 1. Anchor Wiring

All 8 standard anchors wired to **main-agent-specific singletons**.

| Anchor | Handler | Deviations from General |
|--------|---------|------------------------|
| `ON_REASONING` | `MainReasoningTokenTracker` singleton | Identical to general; no deviation |
| `ON_TOOL_RESULT` | `MainToolResultCompactor` singleton | Only 2 compactors (fewest of all agents) |
| `ON_TOOL_CALL` | `MainHistoryRecorder` singleton | Empty subclass of `HistoryRecorder` |
| `ON_TOOL_ERROR` | `MainStatsRecorder` singleton | Pinned config fields |
| `ON_PURPOSE_ERROR` | `MainStatsRecorder` singleton | Same singleton as ON_TOOL_ERROR |
| `ON_STAGE_COMPACT` | `MainStageCompactor` singleton | Budget = 5000 tokens |
| `ON_COMPACTION` | `MainInteractiveCompactor` singleton | Empty PROTECT_TOOLS, orchestration domain_hint |
| `ON_COMPACTION_STATS` | `MainStatsRecorder` singleton | Same singleton |

---

## 2. Stage Compactor → `MainStageCompactor`

| Aspect | General Default | Main Agent |
|--------|----------------|------------|
| Base class | `StageCompactor` | `MainStageCompactor(StageCompactor)` |
| Budget (tokens) | N/A (caller-supplied) | **5000** — highest of all agents |
| Config source | Passed at call time | Pinned from `MainAgentConfig` at construction |

### Budget comparison

| Agent | Stage Compaction Budget |
|-------|----------------------|
| Query | ~4000 |
| Analysis | (config-pinned, varies) |
| Main | **5000** |

Main has the largest budget because subagent results are already compacted
once — the stage compactor only needs to trim orchestration context, not raw data.

---

## 3. Tool-Result Compactor → `MainToolResultCompactor`

| Aspect | General Default (`ToolResultCompactor`) | Main Agent |
|--------|----------------------------------------|------------|
| Subclass | `ToolResultCompactor` (base) | `MainToolResultCompactor(ToolResultCompactor)` |
| Client factory | Generic `ArgoClient()` | `MainClient.for_l0()` — highest-tier model |
| Number of compactors | N/A | **2** compactors only (fewest of all agents) |
| 2-layer pipeline | Same | Deterministic schema compactor → mandatory LLM KEEP/DISCARD review |

### Compactor Registry

| Compactor Key | Deterministic schema projection | Mandatory LLM review | Notes |
|---------------|---------------------------------|----------------------|-------|
| `compact_query_result` | ✓ | ✓ | Preserves the complete query-agent answer and run metadata |
| `compact_analysis_result` | ✓ | ✓ | Preserves the complete analysis answer, verdict, and artifact catalog |

**Key pattern:** delegated results first pass an exact deterministic projection;
missing fields, oversized results, and LLM failures are contract errors rather
than triggers for truncation or pass-through.

### Compactor count comparison

| Agent | Compactors | Hardcoded | LLM-only |
|-------|-----------|-----------|----------|
| Query | 17 | ~12 | ~5 |
| Analysis | 12+ | ~10 | ~2 |
| Main | **2** | **0** | **2** |

---

## 4. Interactive Compactor → `MainInteractiveCompactor`

| Aspect | General Default | Main Agent |
|--------|----------------|------------|
| `PROTECT_TOOLS` | `[]` (empty) | **`[]` (empty)** — same as default |
| `domain_hint` | `""` (none) | `"multi-agent orchestration and scientific data synthesis"` |
| Behavior | Compresses all tool results | Same — no exceptions needed |
| Prompt template | General compaction prompt | `domain_hint` injected into prompt |

Main agent has the **simplest** interactive compactor — no protected tools,
just a domain hint for LLM context.

---

## 5. Working Memory → `MainWorkingMemory`

| Aspect | General Default (`BaseWorkingMemory`) | Main Agent |
|--------|---------------------------------------|------------|
| Superclass | `BaseWorkingMemory` (abstract) | `MainWorkingMemory(WorkingMemory)` |
| Storage | Abstract | In-memory dicts |
| Structured fields | None | `query_results`, `analysis_results`, `history` |
| Auto-extraction | None | `record_subagent_result(agent, result)` |
| `sync_to_disk()` | (in WorkingMemory: MCP file-backed) | Writes to `_output/` session dir when active |

### `record_subagent_result()` dispatch

| Agent type | Storage target | Extraction logic |
|-----------|---------------|-----------------|
| `"query"` | `query_results` | Question + DOI list + answer summary |
| `"analysis"` | `analysis_results` | Question + fit quality + key coefficients + verdict |

**Simpler** than Analysis agent's `record_tool_result()` (which dispatches
by 8+ tool-name prefixes).

### `render()` sections

Returns a structured string with sections:
1. **History** — timestamped subagent dispatch log
2. **Query Results** — per-question summaries from query agent
3. **Analysis Results** — per-question summaries from analysis agent
4. **Open Tasks** — any in-flight parallel subagent calls

---

## 6. Unique Hook: `_menu_batch_summary_hook`

| Aspect | Detail |
|--------|--------|
| Purpose | After a `browse_subagent_tools` + `run_subagent_tool` batch, summarizes which tools were browsed and what results came back |
| Trigger | Wired to `ON_TOOL_RESULT` alongside `MainToolResultCompactor` — fires only when tool is `run_subagent_tool` |
| Output | Appends a batch summary to working memory `history` |

**Unique to main agent** — neither query nor analysis has this hook.

---

## 7. Hooks Not Present in Main Agent

| Hook | Present in Query? | Present in Analysis? | Present in Main? |
|------|-------------------|---------------------|-----------------|
| `L1AutoSaver` | ✓ | ✗ | ✗ |
| `thin_answer_guard` | ✓ | ✗ | ✗ |
| `adaptive_condense` | ✓ | ✗ | ✗ |
| Fabrication detection (in verdict) | ✗ | ✓ | ✗ |
| `_menu_batch_summary_hook` | ✗ | ✗ | **✓** (unique) |

---

## 8. Verdict Runner → `MainVerdictRunner`

| Aspect | Query Agent | Analysis Agent | Main Agent |
|--------|-------------|----------------|------------|
| Sections | 1 (Scientific Review) | 3 (Data/Fit/Scientific) | **3** (Strategy/Scientific/Overall) |
| Focus | Concise scientific assessment | Fit quality assessment | **Orchestration quality + synthesis** |
| `word_cap` | 150 | N/A (uses char cap) | **200** |
| `answer_chars` | N/A | 4000 | **6000** (largest) |
| `include_elapsed` | True | False | **True** |
| Fabrication detection | ✗ | ✓ | ✗ |

### Main Verdict Sections

| Section | What It Checks |
|---------|---------------|
| **Strategy Assessment** | Were subagents dispatched efficiently? Redundant calls? Missing delegation? |
| **Scientific Quality** | Data completeness, consistency across subagent results |
| **Overall Verdict** | Synthesis quality, answer completeness, user-facing clarity |
