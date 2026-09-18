# Query Agent — Engine Customization Catalog

> Deviations from `general_argo_engine_helpers/` defaults.
> Version 6.0 — 2026-04-08

---

## 1. ArgoClient Subclass → `QueryClient`

| Aspect | General Default (`ArgoClient`) | Query Agent Override |
|--------|-------------------------------|---------------------|
| Subclass | `ArgoClient` (dataclass) | `QueryClient(ArgoClient)` |
| Base factories inherited | `with_tier()`, `for_verdict()`, `for_compactor()`, `for_planner()` | All 4 inherited unchanged |

### Added Factory Methods (not in base)

| Factory | Model | MaxTokens | Tier Label | Purpose |
|---------|-------|-----------|------------|---------|
| `for_l0()` | `cfg.MODEL` | `cfg.MAX_TOKENS` (6000) | `"L0-main"` | L0 orchestrator |
| `for_l1()` | `cfg.L1_MODEL` | `cfg.MAX_TOKENS` (6000) | `"L1-worker"` | L1 query dispatchers |
| `for_l2()` | `cfg.L2_MODEL` | `cfg.L2_MAX_TOKENS` (2000) | `"L2-leaf"` | L2 leaf evaluators |

**Why three tiers:** Query agent uses a 3-tier hierarchy (L0→L1→L2).
L2 uses a smaller token budget (2000) because leaf evaluators produce brief summaries.

---

## 2. Import-Time `load_config()`

| Aspect | General Default | Query Agent |
|--------|----------------|-------------|
| `__init__.py` behaviour | No side effects — only exports types | Calls `load_config(AGENT_CONFIG)` at import time |

**Effect:** The moment any module imports from `query_agent_argo_engine`,
the global `EngineConfig` singleton is set to `QueryAgentConfig`.
All downstream `get_config()` calls return query-agent values.

---

## 3. Terminal UI → `QueryAgentTerminalUI`

| Aspect | General Default (`ArgoAgentTerminalUI`) | Query Agent |
|--------|----------------------------------------|-------------|
| `agent_name` | `"Argo Agent"` | `"ThermoML Query Agent"` |
| `ensure_sys_paths()` | No-op | Injects `_AGENT_DIR`, `_AGENTS_DIR`, `_WORKSPACE` into `sys.path` |
| `run_agent(question)` | `raise NotImplementedError` | Calls `orchestrator.run(question, **self.build_run_kwargs())` |
| `display_result(result)` | Generic `result.answer` | Answer + `[iterations, elapsed]` + continuation round indicator |

---

## 4. EngineConfig → `QueryAgentConfig` (53 fields total)

### 4a. Base Engine Fields (26) — values chosen by query agent

| Field | Value | Notes |
|-------|-------|-------|
| `API_URL` | `"https://apps-dev.inside.anl.gov/argoapi/api/v1/resource/chat/"` | |
| `API_USER` | `$ARGO_API_USER` or active master-browser username; blank otherwise | env-overridable; no personal fallback |
| `HEADERS` | `{"Content-Type": "application/json"}` | |
| `MODEL` | `"claudeopus46"` | L0 + L1 model |
| `VERDICT_MODEL` | `"claudeopus46"` | same as primary |
| `PLANNER_MODEL` | `"claudeopus46"` | same as primary |
| `TEMPERATURE` | `0.3` | |
| `TOP_P` | `0.9` | omitted for Claude |
| `MAX_TOKENS` | `6000` | L0 + L1 |
| `HTTP_TIMEOUT` | `600` (10 min) | |
| `MAX_TOOL_ITERATIONS` | `25` | L0 iteration cap |
| `MAX_TURN_SECONDS` | `1000` (≈17 min) | L0 wall-clock budget |
| `L2_MAX_ITERATIONS` | `6` | |
| `L2_MAX_SECONDS` | `90` | |
| `WARN_THRESHOLDS` | `[0.65, 0.85, 0.95]` | |
| `MAX_WRAP_WARNINGS` | `3` | |
| `MAX_EMPTY_WAITS` | `3` | |
| `TOOL_RESULT_CHAR_LIMIT` | `24,000` | |
| `COMPACTION_TRIGGER_CHARS` | `80,000` | |
| `SUMMARY_MAX_CHARS` | `1,000` | |
| `GUIDANCE_MAX_TOKENS` | `150` | |
| `VERDICT_TEMPERATURE` | `0.1` | |
| `VERDICT_MAX_TOKENS` | `500` | |
| `COMPACTOR_TEMPERATURE` | `0.1` | |
| `COMPACTOR_MAX_TOKENS` | `1,000` | |
| `PLANNER_TEMPERATURE` | `0.2` | |
| `PLANNER_MAX_TOKENS` | `1,000` | |

### 4b. Query-Agent-Only Extra Fields (27)

| Field | Value | Purpose |
|-------|-------|---------|
| `L1_MODEL` | `"claudeopus46"` | L1 dispatcher model |
| `L2_MODEL` | `"claudeopus46"` | L2 leaf evaluator model |
| `L2_MAX_TOKENS` | `2000` | L2 token budget |
| `REASONING_CAP` | `10,000` | Char cap on `<reasoning>` blocks |
| `SUBAGENT_MAX_TOKENS` | `700` | KEEP/DISCARD subagent budget |
| `L1_MAX_ITERATIONS` | `12` | L1 iteration cap |
| `L1_MAX_SECONDS` | `360` (6 min) | L1 wall-clock budget |
| `VERDICT_MAX_SECONDS` | `60` | Verdict time limit |
| `KEEP_RECENT_RESULTS` | `2` | Trimming exemption count |
| `MIN_COMPRESS_CHARS` | `500` | Skip compress threshold |
| `COMPRESS_SHORT_THRESHOLD` | `1,500` | Short-result threshold |
| `MAX_RETRY` | `5` | Compaction SELECT→COMPRESS→VALIDATE cycles |
| `MAX_IMMEDIATE_RETRY` | `2` | Immediate retries on VALIDATE=RETRY |
| `COMPRESS_MAX_WORDS` | `500` | Word cap in compaction prompt |
| `COMPRESS_SUMMARY_CHARS` | `800` | Summary preview chars |
| `L1_COMPACTION_INTERVAL` | `999` | > L1 iteration cap — turn-based compaction disabled; size trigger governs |
| `STAGE_COMPACT_BUDGET` | `4,000` | Stage-level compaction budget |
| `STAGE_NOTE_CHARS` | `200` | Max chars per stage note |
| `VERDICT_MAX_WORDS` | `150` | Verdict word limit |
| `SUBAGENT_CHAR_LIMIT` | `40,000` | Max raw chars to KEEP/DISCARD subagent |
| `BLOCK_CONDENSE_LIMIT` | `10,000` | Block condensation trigger |

Malformed tool-call JSON is rejected by the strict `<tool_call>` parser; it is never repaired or truncated into a call.
