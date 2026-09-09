# Reference Stats — main-agent

**Run started:** 2026-08-03 04:16:31
**Wall time (at last flush):** 2,895.6 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 20 | 141,048 | 305,431 | 91,329 | 446,479 | 22,323 | 488.1 | claudeopus46 |
| L0-menu-planner | 1 | 831 | 1,515 | 4,350 | 2,346 | 2,346 | 20.9 | claudesonnet46 |
| L1-worker | 11 | 22,715 | 9,594 | 8,007 | 32,309 | 2,937 | 78.7 | claudeopus46 |
| **TOTAL** | **32** | **164,594** | **316,540** | **103,686** | **481,134** | **15,035** | **587.7** | |

**Estimated tokens:** ~120,283 input + ~25,921 output = ~146,204 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `run_parallel_subagents` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `run_parallel_subagents` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **0** | **0** | **0** | **0** | **0** | **0** | **0** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

*(no entity references recorded)*

---

## 3. DOI & Block References

*(no DOI/block references recorded)*

---

## 4. Tool Results (pre-compaction)

| # | Iter | Tool | Args | Raw (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `browse_subagent_tools` | purpose=Find water-based solvent syst…, tasks=Sear… | 4,350 | — | — | 48.0 |
| 2 | 5 | `run_subagent_tool` | kwargs={'queries': ['water', 'iron(I…, purpose=Res… | 929 | — | — | 12.6 |
| 3 | 5 | `run_subagent_tool` | kwargs={'queries': ['viscosity', 'de…, purpose=Res… | 764 | — | — | 7.0 |
| 4 | 6 | `run_subagent_tool` | kwargs={'queries': ['iron(II) chlori…, purpose=Res… | 865 | — | — | 17.0 |
| 5 | 7 | `run_subagent_tool` | kwargs={'queries': ['ethanol']}, purpose=Resolve e… | 246 | — | — | 4.2 |
| 6 | 7 | `run_subagent_tool` | kwargs={'queries': ['methanol']}, purpose=Resolve … | 246 | — | — | 6.6 |
| 7 | 7 | `run_subagent_tool` | kwargs={'queries': ['ethylene glycol…, purpose=Res… | 312 | — | — | 6.1 |
| 8 | 7 | `run_subagent_tool` | kwargs={'queries': ['glycerol']}, purpose=Resolve … | 174 | — | — | 4.1 |
| 9 | 7 | `run_subagent_tool` | kwargs={'queries': ['dimethyl sulfox…, purpose=Res… | 291 | — | — | 4.8 |
| 10 | 7 | `run_subagent_tool` | kwargs={'queries': ['acetonitrile']}, purpose=Reso… | 193 | — | — | 3.8 |
| 11 | 7 | `run_subagent_tool` | kwargs={'queries': ['2-propanol']}, purpose=Resolv… | 243 | — | — | 5.3 |
| 12 | 7 | `run_subagent_tool` | kwargs={'queries': ['iron(II) chlori…, purpose=Res… | 584 | — | — | 9.4 |
| 13 | 8 | `run_parallel_subagents` | tasks=[{'agent': 'query', 'label': … | 298 | — | — | 1094.6 |
| 14 | 9 | `run_parallel_subagents` | tasks=[{'agent': 'query', 'label': … | 298 | — | — | 1207.5 |
| | | **TOTAL (14 tools)** | | **9,793** | | **0** | **2431.0** |

---

## 5. Compaction Events

| # | Trigger | Outcome | Before (chars) | After (chars) | Saved (chars) | Saved (%) |
|--:|---------|---------|---------------:|--------------:|--------------:|----------:|
| 1 | interval=2 | skipped_by_agent | 5,728 | 5,728 | 0 | 0.0% |
| 2 | interval=2 | skipped_by_agent | 11,281 | 11,281 | 0 | 0.0% |
| 3 | interval=2 | skipped_by_agent | 14,310 | 14,310 | 0 | 0.0% |

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 10,215 | 562 | 10,777 | 2,308 | 13.2 |
| 2 | L0-main | claudeopus46 | 10,215 | 1,676 | 11,891 | 16,951 | 70.7 |
| 3 | L0-menu-planner | claudesonnet46 | 831 | 1,515 | 2,346 | 4,350 | 20.9 |
| 4 | L0-main | claudeopus46 | 10,182 | 6,810 | 16,992 | 573 | 5.3 |
| 5 | L0-main | claudeopus46 | 10,215 | 6,053 | 16,268 | 16,507 | 75.5 |
| 6 | L0-main | claudeopus46 | 10,215 | 9,479 | 19,694 | 2,207 | 13.7 |
| 7 | L0-main | claudeopus46 | 10,215 | 12,299 | 22,514 | 1,502 | 9.6 |
| 8 | L1-worker | claudeopus46 | 2,065 | 1,247 | 3,312 | 1,563 | 11.9 |
| 9 | L1-worker | claudeopus46 | 2,065 | 1,457 | 3,522 | 1,046 | 6.9 |
| 10 | L0-main | claudeopus46 | 2,064 | 2,038 | 4,102 | 1,542 | 11.7 |
| 11 | L0-main | claudeopus46 | 10,215 | 10,228 | 20,443 | 1,202 | 7.8 |
| 12 | L1-worker | claudeopus46 | 2,065 | 2,239 | 4,304 | 1,564 | 16.6 |
| 13 | L0-main | claudeopus46 | 10,182 | 12,582 | 22,764 | 559 | 4.8 |
| 14 | L0-main | claudeopus46 | 10,215 | 11,823 | 22,038 | 2,329 | 9.8 |
| 15 | L1-worker | claudeopus46 | 2,065 | 349 | 2,414 | 368 | 4.0 |
| 16 | L1-worker | claudeopus46 | 2,065 | 350 | 2,415 | 369 | 6.6 |
| 17 | L1-worker | claudeopus46 | 2,065 | 375 | 2,440 | 602 | 6.0 |
| 18 | L1-worker | claudeopus46 | 2,065 | 359 | 2,424 | 297 | 4.1 |
| 19 | L1-worker | claudeopus46 | 2,065 | 374 | 2,439 | 476 | 4.8 |
| 20 | L1-worker | claudeopus46 | 2,065 | 366 | 2,431 | 322 | 3.7 |
| 21 | L1-worker | claudeopus46 | 2,065 | 362 | 2,427 | 489 | 5.2 |
| 22 | L1-worker | claudeopus46 | 2,065 | 2,116 | 4,181 | 911 | 8.9 |
| 23 | L0-main | claudeopus46 | 2,064 | 2,873 | 4,937 | 1,089 | 10.4 |
| 24 | L0-main | claudeopus46 | 10,215 | 14,295 | 24,510 | 3,157 | 18.2 |
| 25 | L0-main | claudeopus46 | 10,182 | 36,808 | 46,990 | 471 | 6.0 |
| 26 | L0-main | claudeopus46 | 10,215 | 36,049 | 46,264 | 2,434 | 15.6 |
| 27 | L0-main | claudeopus46 | 10,215 | 59,731 | 69,946 | 17,435 | 103.5 |
| 28 | L0-main | claudeopus46 | 1,356 | 16,219 | 17,575 | 2,385 | 18.5 |
| 29 | L0-main | claudeopus46 | 298 | 2,767 | 3,065 | 2,373 | 6.9 |
| 30 | L0-main | claudeopus46 | 1,323 | 46,395 | 47,718 | 7,693 | 39.4 |
| 31 | L0-main | claudeopus46 | 298 | 8,216 | 8,514 | 7,009 | 35.1 |
| 32 | L0-main | claudeopus46 | 949 | 8,528 | 9,477 | 1,603 | 12.4 |

