# Reference Stats — main-agent

**Run started:** 2026-09-05 02:33:26
**Wall time (at last flush):** 1,540.8 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 24 | 173,335 | 743,873 | 45,522 | 917,208 | 38,217 | 337.5 | claudeopus46 |
| L1-worker | 6 | 22,602 | 9,649 | 8,544 | 32,251 | 5,375 | 61.7 | claudeopus46 |
| **TOTAL** | **30** | **195,937** | **753,522** | **54,066** | **949,459** | **31,648** | **399.2** | |

**Estimated tokens:** ~237,364 input + ~13,516 output = ~250,880 total
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
| 1 | 1 | `run_parallel_subagents` | tasks=[{'agent': 'analysis', 'label… | 1,529 | — | — | 1197.3 |
| 2 | 3 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_1…, purpose=Gro… | 1,024 | — | — | 11.5 |
| 3 | 4 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_1…, purpose=Ins… | 1,081 | — | — | 10.8 |
| 4 | 5 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_1…, purpose=Ins… | 1,052 | — | — | 9.5 |
| 5 | 8 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_2825'…, purpose=Ins… | 1,029 | — | — | 10.2 |
| 6 | 9 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_9006'…, purpose=Gro… | 1,022 | — | — | 10.3 |
| 7 | 10 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_11042…, purpose=Gro… | 935 | — | — | 10.4 |
| | | **TOTAL (7 tools)** | | **7,672** | | **0** | **1260.0** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 13,598 | 400 | 13,998 | 2,413 | 11.5 |
| 2 | L0-main | claudeopus46 | 161 | 2,632 | 2,793 | 473 | 5.4 |
| 3 | L0-main | claudeopus46 | 3,766 | 37,107 | 40,873 | 1,126 | 11.3 |
| 4 | L0-main | claudeopus46 | 3,766 | 46,593 | 50,359 | 1,179 | 11.8 |
| 5 | L0-main | claudeopus46 | 3,766 | 44,455 | 48,221 | 1,039 | 11.8 |
| 6 | L0-main | claudeopus46 | 3,766 | 4,066 | 7,832 | 1,248 | 9.8 |
| 7 | L0-main | claudeopus46 | 13,598 | 35,747 | 49,345 | 7,624 | 52.2 |
| 8 | L0-main | claudeopus46 | 13,598 | 45,643 | 59,241 | 762 | 5.8 |
| 9 | L1-worker | claudeopus46 | 3,767 | 1,657 | 5,424 | 1,484 | 11.3 |
| 10 | L0-main | claudeopus46 | 13,598 | 47,086 | 60,684 | 684 | 6.5 |
| 11 | L1-worker | claudeopus46 | 3,767 | 1,823 | 5,590 | 1,544 | 10.5 |
| 12 | L0-main | claudeopus46 | 13,598 | 48,554 | 62,152 | 604 | 6.4 |
| 13 | L1-worker | claudeopus46 | 3,767 | 1,453 | 5,220 | 1,264 | 9.4 |
| 14 | L0-main | claudeopus46 | 13,598 | 49,991 | 63,589 | 9,174 | 64.9 |
| 15 | L0-main | claudeopus46 | 13,598 | 62,768 | 76,366 | 774 | 7.4 |
| 16 | L0-main | claudeopus46 | 13,598 | 63,566 | 77,164 | 435 | 4.8 |
| 17 | L1-worker | claudeopus46 | 3,767 | 1,581 | 5,348 | 1,465 | 10.1 |
| 18 | L0-main | claudeopus46 | 13,598 | 64,484 | 78,082 | 400 | 5.9 |
| 19 | L1-worker | claudeopus46 | 3,767 | 1,760 | 5,527 | 1,377 | 10.1 |
| 20 | L0-main | claudeopus46 | 13,598 | 65,791 | 79,389 | 417 | 5.7 |
| 21 | L1-worker | claudeopus46 | 3,767 | 1,375 | 5,142 | 1,410 | 10.3 |
| 22 | L0-main | claudeopus46 | 13,598 | 67,002 | 80,600 | 7,359 | 56.4 |
| 23 | L0-main | claudeopus46 | 2,106 | 10,366 | 12,472 | 500 | 3.9 |
| 24 | L0-main | claudeopus46 | 366 | 1,040 | 1,406 | 700 | 4.3 |
| 25 | L0-main | claudeopus46 | 2,320 | 9,869 | 12,189 | 1,704 | 14.0 |
| 26 | L0-main | claudeopus46 | 366 | 2,179 | 2,545 | 1,650 | 5.3 |
| 27 | L0-main | claudeopus46 | 560 | 11,195 | 11,755 | 344 | 3.3 |
| 28 | L0-main | claudeopus46 | 1,156 | 13,973 | 15,129 | 1,803 | 11.6 |
| 29 | L0-main | claudeopus46 | 366 | 2,496 | 2,862 | 1,551 | 6.3 |
| 30 | L0-main | claudeopus46 | 1,292 | 6,870 | 8,162 | 1,559 | 11.2 |

