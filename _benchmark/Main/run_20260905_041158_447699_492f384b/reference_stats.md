# Reference Stats — main-agent

**Run started:** 2026-09-05 04:11:58
**Wall time (at last flush):** 1,699.1 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 30 | 264,755 | 1,054,062 | 74,587 | 1,318,817 | 43,960 | 578.9 | claudeopus46 |
| L0-menu-planner | 2 | 2,026 | 2,838 | 4,335 | 4,864 | 2,432 | 25.1 | claudesonnet46 |
| L1-subagent | 4 | 15,080 | 2,254 | 5,933 | 17,334 | 4,333 | 48.3 | claudeopus46 |
| L1-worker | 4 | 15,068 | 8,998 | 5,627 | 24,066 | 6,016 | 42.7 | claudeopus46 |
| **TOTAL** | **40** | **296,929** | **1,068,152** | **90,482** | **1,365,081** | **34,127** | **695.0** | |

**Estimated tokens:** ~341,270 input + ~22,620 output = ~363,890 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

*(no raw counter data recorded)*

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

*(no entity references recorded)*

---

## 3. DOI & Block References

*(no DOI/block references recorded)*

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 1 | `run_parallel_subagents` | tasks=[{'agent': 'analysis', 'label… | 1,380 | — | — | 1049.8 |
| 2 | 3 | `browse_subagent_tools` | purpose=Find the mole fraction at whi…, tasks=Insp… | 2,213 | — | — | 12.7 |
| 3 | 5 | `browse_subagent_tools` | purpose=Predict excess molar volume f…, tasks=1. P… | 2,122 | — | — | 12.7 |
| 4 | 7 | `run_subagent_tool` | kwargs={'coeffs': [-4.98776535626797…, purpose=Pre… | 969 | — | — | 23.2 |
| 5 | 9 | `run_subagent_tool` | kwargs={'coeffs': [-4.98776535626797…, purpose=Pre… | 911 | — | — | 25.8 |
| 6 | 12 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_1…, purpose=Ins… | 971 | — | — | 10.7 |
| 7 | 13 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_2…, purpose=Ins… | 911 | — | — | 12.1 |
| 8 | 15 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_1…, purpose=Gro… | 1,091 | — | — | 11.3 |
| 9 | 17 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_1…, purpose=Gro… | 970 | — | — | 9.5 |
| | | **TOTAL (9 tools)** | | **11,538** | | **0** | **1167.8** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 13,598 | 400 | 13,998 | 2,562 | 12.1 |
| 2 | L0-main | claudeopus46 | 161 | 2,755 | 2,916 | 387 | 4.4 |
| 3 | L0-main | claudeopus46 | 3,766 | 38,465 | 42,231 | 1,102 | 12.6 |
| 4 | L0-main | claudeopus46 | 3,766 | 33,633 | 37,399 | 1,357 | 11.7 |
| 5 | L0-main | claudeopus46 | 3,766 | 6,806 | 10,572 | 1,159 | 13.6 |
| 6 | L0-main | claudeopus46 | 13,598 | 34,127 | 47,725 | 4,267 | 28.0 |
| 7 | L0-main | claudeopus46 | 13,598 | 35,046 | 48,644 | 746 | 7.9 |
| 8 | L0-menu-planner | claudesonnet46 | 1,013 | 1,419 | 2,432 | 2,213 | 12.6 |
| 9 | L0-main | claudeopus46 | 13,598 | 37,177 | 50,775 | 1,232 | 8.9 |
| 10 | L0-main | claudeopus46 | 13,598 | 38,060 | 51,658 | 1,351 | 11.4 |
| 11 | L0-menu-planner | claudesonnet46 | 1,013 | 1,419 | 2,432 | 2,122 | 12.5 |
| 12 | L0-main | claudeopus46 | 13,598 | 40,006 | 53,604 | 2,265 | 18.7 |
| 13 | L0-main | claudeopus46 | 13,598 | 40,891 | 54,489 | 1,566 | 14.3 |
| 14 | L1-subagent | claudeopus46 | 3,770 | 405 | 4,175 | 1,421 | 11.6 |
| 15 | L1-subagent | claudeopus46 | 3,770 | 707 | 4,477 | 1,445 | 11.5 |
| 16 | L0-main | claudeopus46 | 13,598 | 41,766 | 55,364 | 8,124 | 61.8 |
| 17 | L0-main | claudeopus46 | 13,598 | 42,575 | 56,173 | 1,644 | 13.8 |
| 18 | L1-subagent | claudeopus46 | 3,770 | 415 | 4,185 | 1,625 | 13.2 |
| 19 | L1-subagent | claudeopus46 | 3,770 | 727 | 4,497 | 1,442 | 12.0 |
| 20 | L0-main | claudeopus46 | 13,598 | 43,444 | 57,042 | 9,827 | 78.3 |
| 21 | L0-main | claudeopus46 | 13,598 | 53,671 | 67,269 | 6,428 | 49.5 |
| 22 | L0-main | claudeopus46 | 13,598 | 64,142 | 77,740 | 665 | 12.4 |
| 23 | L1-worker | claudeopus46 | 3,767 | 1,613 | 5,380 | 1,322 | 10.3 |
| 24 | L0-main | claudeopus46 | 13,598 | 65,493 | 79,091 | 403 | 4.9 |
| 25 | L1-worker | claudeopus46 | 3,767 | 4,379 | 8,146 | 1,488 | 11.9 |
| 26 | L0-main | claudeopus46 | 13,598 | 66,694 | 80,292 | 233 | 3.7 |
| 27 | L0-main | claudeopus46 | 13,598 | 67,558 | 81,156 | 555 | 5.8 |
| 28 | L1-worker | claudeopus46 | 3,767 | 1,372 | 5,139 | 1,477 | 11.2 |
| 29 | L0-main | claudeopus46 | 13,598 | 68,270 | 81,868 | 8,460 | 63.2 |
| 30 | L0-main | claudeopus46 | 13,598 | 81,524 | 95,122 | 1,499 | 12.6 |
| 31 | L1-worker | claudeopus46 | 3,767 | 1,634 | 5,401 | 1,340 | 9.3 |
| 32 | L0-main | claudeopus46 | 13,598 | 83,089 | 96,687 | 8,448 | 64.2 |
| 33 | L0-main | claudeopus46 | 2,106 | 12,813 | 14,919 | 509 | 4.4 |
| 34 | L0-main | claudeopus46 | 366 | 1,049 | 1,415 | 813 | 4.0 |
| 35 | L0-main | claudeopus46 | 2,320 | 12,316 | 14,636 | 1,675 | 14.4 |
| 36 | L0-main | claudeopus46 | 366 | 2,150 | 2,516 | 1,621 | 4.9 |
| 37 | L0-main | claudeopus46 | 560 | 13,755 | 14,315 | 353 | 3.5 |
| 38 | L0-main | claudeopus46 | 1,156 | 16,449 | 17,605 | 2,069 | 14.5 |
| 39 | L0-main | claudeopus46 | 366 | 2,762 | 3,128 | 1,817 | 7.0 |
| 40 | L0-main | claudeopus46 | 1,292 | 7,176 | 8,468 | 1,450 | 12.4 |

