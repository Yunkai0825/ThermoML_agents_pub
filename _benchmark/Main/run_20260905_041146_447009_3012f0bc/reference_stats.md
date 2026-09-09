# Reference Stats — main-agent

**Run started:** 2026-09-05 04:11:46
**Wall time (at last flush):** 716.3 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 28 | 270,660 | 876,011 | 48,034 | 1,146,671 | 40,952 | 352.9 | claudeopus46 |
| L1-worker | 12 | 45,204 | 15,710 | 14,091 | 60,914 | 5,076 | 110.2 | claudeopus46 |
| **TOTAL** | **40** | **315,864** | **891,721** | **62,125** | **1,207,585** | **30,189** | **463.1** | |

**Estimated tokens:** ~301,896 input + ~15,531 output = ~317,427 total
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
| 1 | 1 | `run_parallel_subagents` | tasks=[{'agent': 'query', 'label': … | 832 | KEEP ←in 46,444 | 832 | 267.7 |
| 2 | 4 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_9…, purpose=Ins… | 748 | — | — | 9.6 |
| 3 | 5 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_9…, purpose=Ins… | 671 | — | — | 7.9 |
| 4 | 6 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_9…, purpose=Ins… | 1,070 | — | — | 10.7 |
| 5 | 7 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_1…, purpose=Ins… | 898 | — | — | 9.6 |
| 6 | 8 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_2…, purpose=Ins… | 1,100 | — | — | 12.3 |
| 7 | 9 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_3…, purpose=Ins… | 530 | — | — | 6.7 |
| 8 | 10 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_1…, purpose=Ins… | 737 | — | — | 7.2 |
| 9 | 13 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_2825'…, purpose=Ins… | 1,076 | — | — | 12.2 |
| 10 | 14 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_2825'…, purpose=Gro… | 961 | — | — | 9.7 |
| 11 | 15 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_5201'…, purpose=Ins… | 1,147 | — | — | 11.4 |
| 12 | 17 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_8869'…, purpose=Ins… | 752 | — | — | 7.8 |
| 13 | 18 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_9571'…, purpose=Ins… | 647 | — | — | 7.9 |
| | | **TOTAL (13 tools)** | | **11,169** | | **832** | **380.7** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 13,598 | 401 | 13,999 | 1,822 | 9.6 |
| 2 | L0-main | claudeopus46 | 3,766 | 47,732 | 51,498 | 1,342 | 12.5 |
| 3 | L0-main | claudeopus46 | 13,598 | 16,695 | 30,293 | 7,069 | 47.2 |
| 4 | L0-main | claudeopus46 | 13,598 | 28,174 | 41,772 | 884 | 8.2 |
| 5 | L0-main | claudeopus46 | 13,598 | 29,010 | 42,608 | 626 | 5.8 |
| 6 | L1-worker | claudeopus46 | 3,767 | 557 | 4,324 | 1,210 | 9.5 |
| 7 | L0-main | claudeopus46 | 13,598 | 29,745 | 43,343 | 738 | 6.9 |
| 8 | L1-worker | claudeopus46 | 3,767 | 517 | 4,284 | 1,095 | 7.8 |
| 9 | L0-main | claudeopus46 | 13,598 | 30,789 | 44,387 | 585 | 5.4 |
| 10 | L1-worker | claudeopus46 | 3,767 | 1,656 | 5,423 | 1,409 | 10.6 |
| 11 | L0-main | claudeopus46 | 13,598 | 32,170 | 45,768 | 755 | 6.8 |
| 12 | L1-worker | claudeopus46 | 3,767 | 1,601 | 5,368 | 1,099 | 9.4 |
| 13 | L0-main | claudeopus46 | 13,598 | 33,447 | 47,045 | 430 | 5.2 |
| 14 | L1-worker | claudeopus46 | 3,767 | 1,777 | 5,544 | 1,543 | 12.0 |
| 15 | L0-main | claudeopus46 | 13,598 | 34,833 | 48,431 | 446 | 5.4 |
| 16 | L1-worker | claudeopus46 | 3,767 | 1,094 | 4,861 | 815 | 6.6 |
| 17 | L0-main | claudeopus46 | 13,598 | 35,676 | 49,274 | 404 | 5.0 |
| 18 | L1-worker | claudeopus46 | 3,767 | 1,171 | 4,938 | 898 | 7.0 |
| 19 | L0-main | claudeopus46 | 13,598 | 36,680 | 50,278 | 10,394 | 73.6 |
| 20 | L0-main | claudeopus46 | 13,598 | 52,338 | 65,936 | 832 | 7.7 |
| 21 | L0-main | claudeopus46 | 13,598 | 53,149 | 66,747 | 540 | 6.0 |
| 22 | L1-worker | claudeopus46 | 3,767 | 1,656 | 5,423 | 1,433 | 11.7 |
| 23 | L0-main | claudeopus46 | 13,598 | 54,177 | 67,775 | 438 | 4.7 |
| 24 | L1-worker | claudeopus46 | 3,767 | 1,555 | 5,322 | 1,183 | 9.4 |
| 25 | L0-main | claudeopus46 | 13,598 | 55,440 | 69,038 | 492 | 5.0 |
| 26 | L1-worker | claudeopus46 | 3,767 | 1,810 | 5,577 | 1,531 | 11.1 |
| 27 | L0-main | claudeopus46 | 13,598 | 56,902 | 70,500 | 387 | 4.5 |
| 28 | L0-main | claudeopus46 | 13,598 | 57,926 | 71,524 | 563 | 6.3 |
| 29 | L1-worker | claudeopus46 | 3,767 | 1,113 | 4,880 | 988 | 7.5 |
| 30 | L0-main | claudeopus46 | 13,598 | 58,129 | 71,727 | 449 | 5.5 |
| 31 | L1-worker | claudeopus46 | 3,767 | 1,203 | 4,970 | 887 | 7.6 |
| 32 | L0-main | claudeopus46 | 13,598 | 59,056 | 72,654 | 8,871 | 62.1 |
| 33 | L0-main | claudeopus46 | 2,106 | 13,804 | 15,910 | 619 | 4.6 |
| 34 | L0-main | claudeopus46 | 2,320 | 13,306 | 15,626 | 1,183 | 9.2 |
| 35 | L0-main | claudeopus46 | 366 | 1,159 | 1,525 | 872 | 4.7 |
| 36 | L0-main | claudeopus46 | 366 | 1,658 | 2,024 | 1,134 | 4.7 |
| 37 | L0-main | claudeopus46 | 560 | 14,917 | 15,477 | 429 | 4.0 |
| 38 | L0-main | claudeopus46 | 1,156 | 18,381 | 19,537 | 2,259 | 13.0 |
| 39 | L0-main | claudeopus46 | 366 | 2,952 | 3,318 | 1,949 | 7.7 |
| 40 | L0-main | claudeopus46 | 1,292 | 7,365 | 8,657 | 1,522 | 11.6 |

