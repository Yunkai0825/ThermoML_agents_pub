# Reference Stats — main-agent

**Run started:** 2026-09-05 04:20:35
**Wall time (at last flush):** 780.4 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 30 | 254,923 | 966,333 | 61,618 | 1,221,256 | 40,708 | 438.7 | claudeopus46 |
| L1-worker | 11 | 41,437 | 14,710 | 13,027 | 56,147 | 5,104 | 98.4 | claudeopus46 |
| **TOTAL** | **41** | **296,360** | **981,043** | **74,645** | **1,277,403** | **31,156** | **537.1** | |

**Estimated tokens:** ~319,350 input + ~18,661 output = ~338,011 total
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
| 1 | 1 | `run_parallel_subagents` | tasks=[{'agent': 'query', 'label': … | 1,284 | — | — | 297.1 |
| 2 | 3 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_1…, purpose=Ins… | 1,056 | — | — | 9.4 |
| 3 | 4 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_1…, purpose=Ins… | 496 | — | — | 5.3 |
| 4 | 5 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_1…, purpose=Ins… | 857 | — | — | 9.6 |
| 5 | 6 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_2…, purpose=Ins… | 987 | — | — | 10.6 |
| 6 | 7 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_1…, purpose=Ins… | 797 | — | — | 8.4 |
| 7 | 8 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_1…, purpose=Ins… | 1,051 | — | — | 9.6 |
| 8 | 11 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_11337…, purpose=Gro… | 868 | — | — | 10.6 |
| 9 | 12 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_7481'…, purpose=Ins… | 558 | — | — | 8.2 |
| 10 | 13 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_7481'…, purpose=Ins… | 837 | — | — | 9.2 |
| 11 | 14 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_5201'…, purpose=Ins… | 961 | — | — | 10.3 |
| 12 | 16 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_6951'…, purpose=Ins… | 1,027 | — | — | 9.2 |
| | | **TOTAL (12 tools)** | | **10,779** | | **0** | **397.5** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 13,598 | 441 | 14,039 | 2,644 | 12.5 |
| 2 | L0-main | claudeopus46 | 161 | 2,559 | 2,720 | 431 | 4.2 |
| 3 | L0-main | claudeopus46 | 3,766 | 12,558 | 16,324 | 1,146 | 10.1 |
| 4 | L0-main | claudeopus46 | 3,766 | 17,763 | 21,529 | 1,278 | 12.0 |
| 5 | L0-main | claudeopus46 | 3,766 | 23,792 | 27,558 | 1,276 | 13.4 |
| 6 | L0-main | claudeopus46 | 3,766 | 4,261 | 8,027 | 1,223 | 10.5 |
| 7 | L0-main | claudeopus46 | 13,598 | 21,146 | 34,744 | 14,129 | 94.6 |
| 8 | L0-main | claudeopus46 | 13,598 | 37,836 | 51,434 | 1,029 | 8.5 |
| 9 | L1-worker | claudeopus46 | 3,767 | 1,532 | 5,299 | 1,310 | 9.3 |
| 10 | L0-main | claudeopus46 | 13,598 | 39,324 | 52,922 | 729 | 6.7 |
| 11 | L1-worker | claudeopus46 | 3,767 | 539 | 4,306 | 688 | 5.0 |
| 12 | L0-main | claudeopus46 | 13,598 | 40,303 | 53,901 | 727 | 6.4 |
| 13 | L1-worker | claudeopus46 | 3,767 | 1,561 | 5,328 | 1,192 | 9.4 |
| 14 | L0-main | claudeopus46 | 13,598 | 41,594 | 55,192 | 561 | 5.7 |
| 15 | L1-worker | claudeopus46 | 3,767 | 1,921 | 5,688 | 1,352 | 10.4 |
| 16 | L0-main | claudeopus46 | 13,598 | 42,977 | 56,575 | 573 | 6.0 |
| 17 | L1-worker | claudeopus46 | 3,767 | 561 | 4,328 | 1,283 | 8.3 |
| 18 | L0-main | claudeopus46 | 13,598 | 44,234 | 57,832 | 506 | 5.4 |
| 19 | L1-worker | claudeopus46 | 3,767 | 1,563 | 5,330 | 1,284 | 9.4 |
| 20 | L0-main | claudeopus46 | 13,598 | 45,603 | 59,201 | 12,037 | 77.5 |
| 21 | L0-main | claudeopus46 | 13,598 | 62,223 | 75,821 | 1,385 | 11.5 |
| 22 | L0-main | claudeopus46 | 13,598 | 63,096 | 76,694 | 415 | 5.2 |
| 23 | L1-worker | claudeopus46 | 3,767 | 1,478 | 5,245 | 1,246 | 10.4 |
| 24 | L0-main | claudeopus46 | 13,598 | 63,848 | 77,446 | 448 | 5.5 |
| 25 | L1-worker | claudeopus46 | 3,767 | 514 | 4,281 | 947 | 8.0 |
| 26 | L0-main | claudeopus46 | 13,598 | 64,764 | 78,362 | 506 | 6.2 |
| 27 | L1-worker | claudeopus46 | 3,767 | 1,565 | 5,332 | 1,089 | 9.0 |
| 28 | L0-main | claudeopus46 | 13,598 | 65,952 | 79,550 | 506 | 6.1 |
| 29 | L1-worker | claudeopus46 | 3,767 | 1,913 | 5,680 | 1,376 | 10.2 |
| 30 | L0-main | claudeopus46 | 13,598 | 67,261 | 80,859 | 478 | 5.2 |
| 31 | L0-main | claudeopus46 | 13,598 | 68,321 | 81,919 | 690 | 5.3 |
| 32 | L1-worker | claudeopus46 | 3,767 | 1,563 | 5,330 | 1,260 | 9.0 |
| 33 | L0-main | claudeopus46 | 13,598 | 68,814 | 82,412 | 9,650 | 62.3 |
| 34 | L0-main | claudeopus46 | 2,106 | 12,756 | 14,862 | 508 | 4.1 |
| 35 | L0-main | claudeopus46 | 366 | 1,048 | 1,414 | 708 | 4.1 |
| 36 | L0-main | claudeopus46 | 2,320 | 12,218 | 14,538 | 1,495 | 11.5 |
| 37 | L0-main | claudeopus46 | 366 | 1,970 | 2,336 | 1,436 | 4.4 |
| 38 | L0-main | claudeopus46 | 560 | 13,552 | 14,112 | 352 | 3.4 |
| 39 | L0-main | claudeopus46 | 1,156 | 16,418 | 17,574 | 1,744 | 11.7 |
| 40 | L0-main | claudeopus46 | 366 | 2,437 | 2,803 | 1,492 | 5.7 |
| 41 | L0-main | claudeopus46 | 1,292 | 7,264 | 8,556 | 1,516 | 13.0 |

