# Reference Stats — main-agent

**Run started:** 2026-09-05 04:24:56
**Wall time (at last flush):** 2,136.8 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 33 | 295,717 | 1,488,275 | 65,005 | 1,783,992 | 54,060 | 495.7 | claudeopus46 |
| L0-menu-planner | 2 | 2,026 | 2,839 | 2,723 | 4,865 | 2,432 | 17.0 | claudesonnet46 |
| L1-subagent | 2 | 7,540 | 1,344 | 3,105 | 8,884 | 4,442 | 25.3 | claudeopus46 |
| L1-worker | 8 | 30,136 | 39,298 | 11,746 | 69,434 | 8,679 | 98.5 | claudeopus46 |
| **TOTAL** | **45** | **335,419** | **1,531,756** | **82,579** | **1,867,175** | **41,492** | **636.5** | |

**Estimated tokens:** ~466,793 input + ~20,644 output = ~487,437 total
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
| 1 | 1 | `run_parallel_subagents` | tasks=[{'agent': 'analysis', 'label… | 2,319 | KEEP ←in 19,455 | 205 | 1053.0 |
| 2 | 3 | `browse_subagent_tools` | purpose=Find the predict_from_rk tool…, tasks=Get … | 1,150 | — | — | 7.5 |
| 3 | 5 | `browse_subagent_tools` | purpose=Find the predict_from_rk tool…, tasks=Get … | 1,573 | — | — | 9.7 |
| 4 | 7 | `run_subagent_tool` | kwargs={'coeffs': [-3.98238564551898…, purpose=Fin… | 983 | — | — | 25.7 |
| 5 | 8 | `run_parallel_subagents` | tasks=[{'agent': 'analysis', 'label… | 205 | — | — | 510.8 |
| 6 | 10 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_1…, purpose=Ins… | 1,130 | — | — | 11.2 |
| 7 | 11 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_1…, purpose=Ins… | 1,033 | — | — | 12.7 |
| 8 | 13 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_2…, purpose=Ins… | 1,060 | — | — | 13.6 |
| 9 | 14 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_7…, purpose=Gro… | 1,093 | — | — | 12.8 |
| 10 | 16 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_1…, purpose=Gro… | 850 | — | — | 13.7 |
| 11 | 17 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_1…, purpose=Gro… | 1,147 | — | — | 10.2 |
| 12 | 18 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_2…, purpose=Gro… | 711 | — | — | 14.6 |
| 13 | 19 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_7…, purpose=Gro… | 810 | — | — | 11.6 |
| | | **TOTAL (13 tools)** | | **14,064** | | **205** | **1707.1** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 13,598 | 468 | 14,066 | 2,740 | 13.0 |
| 2 | L0-main | claudeopus46 | 161 | 2,898 | 3,059 | 362 | 4.2 |
| 3 | L0-main | claudeopus46 | 3,766 | 45,778 | 49,544 | 1,233 | 12.3 |
| 4 | L0-main | claudeopus46 | 3,766 | 9,778 | 13,544 | 1,107 | 11.3 |
| 5 | L0-main | claudeopus46 | 3,766 | 10,080 | 13,846 | 2,013 | 18.7 |
| 6 | L0-main | claudeopus46 | 13,598 | 40,944 | 54,542 | 1,290 | 10.7 |
| 7 | L0-main | claudeopus46 | 13,598 | 42,062 | 55,660 | 683 | 5.5 |
| 8 | L0-menu-planner | claudesonnet46 | 1,013 | 1,355 | 2,368 | 1,150 | 7.4 |
| 9 | L0-main | claudeopus46 | 13,598 | 42,850 | 56,448 | 828 | 5.8 |
| 10 | L0-main | claudeopus46 | 13,598 | 43,712 | 57,310 | 696 | 5.1 |
| 11 | L0-menu-planner | claudesonnet46 | 1,013 | 1,484 | 2,497 | 1,573 | 9.6 |
| 12 | L0-main | claudeopus46 | 13,598 | 45,043 | 58,641 | 1,678 | 16.3 |
| 13 | L0-main | claudeopus46 | 13,598 | 45,840 | 59,438 | 1,681 | 14.6 |
| 14 | L1-subagent | claudeopus46 | 3,770 | 521 | 4,291 | 1,619 | 12.7 |
| 15 | L1-subagent | claudeopus46 | 3,770 | 823 | 4,593 | 1,486 | 12.6 |
| 16 | L0-main | claudeopus46 | 13,598 | 46,757 | 60,355 | 8,487 | 63.0 |
| 17 | L0-main | claudeopus46 | 3,766 | 22,012 | 25,778 | 1,581 | 14.1 |
| 18 | L0-main | claudeopus46 | 13,598 | 65,074 | 78,672 | 8,683 | 62.6 |
| 19 | L0-main | claudeopus46 | 13,598 | 76,320 | 89,918 | 634 | 7.0 |
| 20 | L1-worker | claudeopus46 | 3,767 | 1,651 | 5,418 | 1,461 | 11.0 |
| 21 | L0-main | claudeopus46 | 13,598 | 77,762 | 91,360 | 600 | 6.6 |
| 22 | L1-worker | claudeopus46 | 3,767 | 11,171 | 14,938 | 1,388 | 12.5 |
| 23 | L0-main | claudeopus46 | 13,598 | 79,122 | 92,720 | 454 | 5.8 |
| 24 | L0-main | claudeopus46 | 13,598 | 80,146 | 93,744 | 612 | 5.3 |
| 25 | L1-worker | claudeopus46 | 3,767 | 4,403 | 8,170 | 1,409 | 13.3 |
| 26 | L0-main | claudeopus46 | 13,598 | 80,696 | 94,294 | 551 | 6.0 |
| 27 | L1-worker | claudeopus46 | 3,767 | 2,418 | 6,185 | 1,606 | 12.4 |
| 28 | L0-main | claudeopus46 | 13,598 | 82,145 | 95,743 | 7,340 | 53.7 |
| 29 | L0-main | claudeopus46 | 13,598 | 93,923 | 107,521 | 1,239 | 11.1 |
| 30 | L1-worker | claudeopus46 | 3,767 | 11,183 | 14,950 | 1,422 | 13.5 |
| 31 | L0-main | claudeopus46 | 13,598 | 95,156 | 108,754 | 520 | 6.9 |
| 32 | L1-worker | claudeopus46 | 3,767 | 1,629 | 5,396 | 1,412 | 10.0 |
| 33 | L0-main | claudeopus46 | 13,598 | 96,674 | 110,272 | 547 | 6.4 |
| 34 | L1-worker | claudeopus46 | 3,767 | 4,445 | 8,212 | 1,754 | 14.4 |
| 35 | L0-main | claudeopus46 | 13,598 | 97,753 | 111,351 | 516 | 5.7 |
| 36 | L1-worker | claudeopus46 | 3,767 | 2,398 | 6,165 | 1,294 | 11.4 |
| 37 | L0-main | claudeopus46 | 13,598 | 98,904 | 112,502 | 8,592 | 61.6 |
| 38 | L0-main | claudeopus46 | 2,106 | 12,282 | 14,388 | 515 | 4.8 |
| 39 | L0-main | claudeopus46 | 366 | 1,055 | 1,421 | 819 | 4.5 |
| 40 | L0-main | claudeopus46 | 2,320 | 11,717 | 14,037 | 1,664 | 12.8 |
| 41 | L0-main | claudeopus46 | 366 | 2,139 | 2,505 | 1,605 | 4.9 |
| 42 | L0-main | claudeopus46 | 560 | 13,162 | 13,722 | 359 | 3.2 |
| 43 | L0-main | claudeopus46 | 1,156 | 15,893 | 17,049 | 2,013 | 13.2 |
| 44 | L0-main | claudeopus46 | 366 | 2,706 | 3,072 | 1,761 | 6.7 |
| 45 | L0-main | claudeopus46 | 1,292 | 7,424 | 8,716 | 1,602 | 12.3 |

