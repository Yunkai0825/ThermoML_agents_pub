# Main Agent — Engine Customization Catalog

> Deviations from `general_argo_engine_helpers/` defaults.
> Version 6.0 — 2026-04-08

---

## 1. ArgoClient → `MainClient`

| Aspect | General Default (`ArgoClient`) | Main Agent |
|--------|-------------------------------|------------|
| Subclass | `ArgoClient` (base) | `MainClient(ArgoClient)` |
| Factory methods | None (bare constructor) | **`for_l0()` only** — no L1 or L2 factories |
| Baked-in defaults | None | `for_l0()` sets model, max_tokens, temperature from config |
| L1 tier | (caller-supplied) | **Not present** — no L1 dispatchers |
| L2 tier | (caller-supplied) | **Not present** — no L2 searchers |

**Key deviation:** Main agent has the **simplest** client — only one factory.
Query has 3 (L0/L1/L2), Analysis has 3 (L0/L1_DATA/L1_FIT). Main has **1**.

---

## 2. Config → `MainAgentConfig`

### Base Fields (26 from `EngineConfig` — NO defaults in base)

All 26 fields from `EngineConfig` are overridden with **main-agent-specific values**.

### Main-Agent-Specific Fields (beyond the 26 base)

| Field | Value | Query Equivalent | Analysis Equivalent | Notes |
|-------|-------|-----------------|---------------------|-------|
| `MAX_TOOL_ITERATIONS` | **40** | 20 | 30 | Highest of all agents — orchestrates subagents |
| `MAX_TURN_SECONDS` | **2400** (40 min) | 600 | 1200 | Highest — must wait for subagent round-trips |
| `COMPACTION_INTERVAL` | **999** | 999 (`L1_COMPACTION_INTERVAL`) | 9999 | Turn-based compaction disabled everywhere — the char-size trigger governs |
| `MENU_PLANNER_MODEL` | `"claudesonnet4"` | N/A | N/A | **Unique** — used for tool-menu discovery |
| `VERDICT_MAX_TOKENS` | **3000** | 500 | 2000 | Largest — final user-facing synthesis |
| `PROTECT_TOOLS` | **`[]` (empty)** | `[]` | 6 fitting tools | No tools need protection — all are delegation |
| `SUBAGENT_MAX_TOKENS` | **700** | 700 | 500 | Compaction budget per subagent result |

### Fields NOT present (vs Query / Analysis)

| Field | In Query? | In Analysis? | In Main? | Why |
|-------|-----------|-------------|----------|-----|
| `L1_MODEL` | ✓ | ✓ | ✗ | No L1 workers |
| `L1_MAX_TOKENS` | ✓ | ✓ | ✗ | No L1 workers |
| `L2_MODEL` | ✓ | ✗ | ✗ | No L2 workers |
| `L2_MAX_TOKENS` | ✓ | ✗ | ✗ | No L2 workers |
| `L1_DATA_*` / `L1_FIT_*` | ✗ | ✓ | ✗ | No analysis sub-tiers |
| `RK_MAX_ORDER` | ✗ | ✓ | ✗ | No fitting |
| `IDEAL_BASELINE_PROPS` | ✗ | ✓ | ✗ | No fitting |
| `BLOCK_CONDENSE_LIMIT` | ✓ | ✗ | ✗ | No direct search |
| `REASONING_CAP` | ✓ | ✗ | ✗ | Not tracking reasoning budget |

---

## 3. Terminal UI

| Aspect | General Default | Main Agent |
|--------|----------------|------------|
| Class | None (agent-specific) | `MainAgentTerminalUI` |
| Deviation | N/A | Adds subagent progress display, multi-round prompts |

---

## 4. Config Loading

| Aspect | General Default | Main Agent |
|--------|----------------|------------|
| Pattern | None (caller constructs) | `load_config()` at import time → module-level `CONFIG` singleton |
| Source | N/A | `ThermoML_main_argo_config.py` → JSON / env-var merging |

Same pattern as Query and Analysis agents.

---

## 5. Three-Agent Engine Comparison

| Parameter | Query | Analysis | Main |
|-----------|-------|----------|------|
| L0 iterations | 20 | 30 | **40** |
| L0 timeout (s) | 600 | 1200 | **2400** |
| Compaction interval | 999 (L1) | 9999 | **999** (turn-based disabled — size trigger governs) |
| Client factories | 3 (L0/L1/L2) | 3 (L0/L1_DATA/L1_FIT) | **1 (L0 only)** |
| Verdict tokens | 500 | 2000 | **3000** |
| PROTECT_TOOLS | 0 | 6 | **0** |
| Domain config fields | 27 extra | ~15 extra | **~8 extra** |
| Unique fields | REASONING_CAP, BLOCK_CONDENSE_LIMIT | RK_MAX_ORDER, IDEAL_BASELINE_PROPS | **MENU_PLANNER_MODEL** |
