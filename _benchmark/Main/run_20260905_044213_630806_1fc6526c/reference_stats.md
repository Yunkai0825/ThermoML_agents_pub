# Reference Stats — main-agent

**Run started:** 2026-09-05 04:42:13
**Wall time (at last flush):** 707.9 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 27 | 257,062 | 510,135 | 39,702 | 767,197 | 28,414 | 283.1 | claudeopus46 |
| L0-menu-planner | 1 | 1,013 | 1,437 | 2,037 | 2,450 | 2,450 | 11.7 | claudesonnet46 |
| L1-worker | 8 | 30,136 | 9,231 | 7,297 | 39,367 | 4,920 | 60.8 | claudeopus46 |
| **TOTAL** | **36** | **288,211** | **520,803** | **49,036** | **809,014** | **22,472** | **355.6** | |

**Estimated tokens:** ~202,253 input + ~12,259 output = ~214,512 total
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
| 1 | 2 | `browse_subagent_tools` | purpose=Find thermodynamic and transp…, tasks=Sear… | 2,037 | — | — | 11.8 |
| 2 | 4 | `run_subagent_tool` | kwargs={'query': 'water', 'entity_ty…, purpose=Res… | 239 | — | — | 4.4 |
| 3 | 7 | `run_subagent_tool` | kwargs={'entity_type': 'compound', '…, purpose=Res… | 253 | — | — | 4.1 |
| 4 | 8 | `run_parallel_subagents` | tasks=[{'agent': 'query', 'label': … | 701 | KEEP ←in 34,200 | 701 | 365.2 |
| 5 | 11 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_2781'…, purpose=Ins… | 645 | — | — | 7.6 |
| 6 | 12 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_2781'…, purpose=Gro… | 971 | — | — | 10.7 |
| 7 | 13 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_11517…, purpose=Gro… | 716 | — | — | 8.9 |
| 8 | 15 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_2781'…, purpose=Gro… | 955 | — | — | 11.5 |
| 9 | 16 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_11517…, purpose=Gro… | 754 | — | — | 9.0 |
| 10 | 17 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_5958'…, purpose=Gro… | 579 | — | — | 7.4 |
| | | **TOTAL (10 tools)** | | **7,850** | | **701** | **440.6** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 13,598 | 408 | 14,006 | 1,384 | 9.3 |
| 2 | L0-main | claudeopus46 | 13,598 | 1,316 | 14,914 | 688 | 4.3 |
| 3 | L0-menu-planner | claudesonnet46 | 1,013 | 1,437 | 2,450 | 2,037 | 11.7 |
| 4 | L0-main | claudeopus46 | 13,598 | 3,134 | 16,732 | 569 | 4.1 |
| 5 | L0-main | claudeopus46 | 13,598 | 4,028 | 17,626 | 559 | 4.3 |
| 6 | L1-worker | claudeopus46 | 3,767 | 408 | 4,175 | 399 | 4.3 |
| 7 | L0-main | claudeopus46 | 13,598 | 4,073 | 17,671 | 478 | 4.1 |
| 8 | L0-main | claudeopus46 | 13,598 | 4,745 | 18,343 | 494 | 4.1 |
| 9 | L0-main | claudeopus46 | 13,598 | 5,375 | 18,973 | 509 | 3.9 |
| 10 | L1-worker | claudeopus46 | 3,767 | 440 | 4,207 | 390 | 4.0 |
| 11 | L0-main | claudeopus46 | 13,598 | 5,232 | 18,830 | 2,002 | 10.3 |
| 12 | L0-main | claudeopus46 | 3,766 | 35,680 | 39,446 | 1,465 | 13.7 |
| 13 | L0-main | claudeopus46 | 13,598 | 21,153 | 34,751 | 7,390 | 48.4 |
| 14 | L0-main | claudeopus46 | 13,598 | 33,059 | 46,657 | 684 | 6.5 |
| 15 | L0-main | claudeopus46 | 13,598 | 33,856 | 47,454 | 682 | 6.5 |
| 16 | L1-worker | claudeopus46 | 3,767 | 596 | 4,363 | 913 | 7.3 |
| 17 | L0-main | claudeopus46 | 13,598 | 34,479 | 48,077 | 510 | 5.4 |
| 18 | L1-worker | claudeopus46 | 3,767 | 2,049 | 5,816 | 1,357 | 10.6 |
| 19 | L0-main | claudeopus46 | 13,598 | 35,814 | 49,412 | 600 | 5.5 |
| 20 | L1-worker | claudeopus46 | 3,767 | 1,423 | 5,190 | 1,014 | 8.7 |
| 21 | L0-main | claudeopus46 | 13,598 | 36,882 | 50,480 | 5,790 | 38.4 |
| 22 | L0-main | claudeopus46 | 13,598 | 47,212 | 60,810 | 873 | 8.1 |
| 23 | L1-worker | claudeopus46 | 3,767 | 2,128 | 5,895 | 1,385 | 11.0 |
| 24 | L0-main | claudeopus46 | 13,598 | 48,517 | 62,115 | 557 | 5.6 |
| 25 | L1-worker | claudeopus46 | 3,767 | 1,360 | 5,127 | 1,035 | 8.3 |
| 26 | L0-main | claudeopus46 | 13,598 | 49,643 | 63,241 | 473 | 5.0 |
| 27 | L1-worker | claudeopus46 | 3,767 | 827 | 4,594 | 804 | 6.6 |
| 28 | L0-main | claudeopus46 | 13,598 | 50,578 | 64,176 | 6,066 | 41.4 |
| 29 | L0-main | claudeopus46 | 2,106 | 10,001 | 12,107 | 386 | 3.9 |
| 30 | L0-main | claudeopus46 | 366 | 926 | 1,292 | 533 | 3.4 |
| 31 | L0-main | claudeopus46 | 2,320 | 9,496 | 11,816 | 1,236 | 11.8 |
| 32 | L0-main | claudeopus46 | 366 | 1,711 | 2,077 | 1,187 | 4.6 |
| 33 | L0-main | claudeopus46 | 560 | 10,542 | 11,102 | 264 | 3.4 |
| 34 | L0-main | claudeopus46 | 1,156 | 12,714 | 13,870 | 1,529 | 10.5 |
| 35 | L0-main | claudeopus46 | 366 | 2,222 | 2,588 | 1,335 | 5.2 |
| 36 | L0-main | claudeopus46 | 1,292 | 7,339 | 8,631 | 1,459 | 11.4 |

