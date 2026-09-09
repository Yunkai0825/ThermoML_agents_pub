# Reference Stats — main-agent

**Run started:** 2026-09-05 02:25:43
**Wall time (at last flush):** 729.7 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 11 | 62,558 | 139,988 | 26,786 | 202,546 | 18,413 | 195.9 | claudeopus46 |
| **TOTAL** | **11** | **62,558** | **139,988** | **26,786** | **202,546** | **18,413** | **195.9** | |

**Estimated tokens:** ~50,636 input + ~6,696 output = ~57,332 total
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
| 1 | 1 | `run_analysis_agent` | context=The user wants a complete Red…, purpose=Fi… | 23,804 | — | — | 537.5 |
| | | **TOTAL (1 tools)** | | **23,804** | | **0** | **537.5** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 13,598 | 412 | 14,010 | 2,016 | 12.0 |
| 2 | L0-main | claudeopus46 | 13,598 | 23,544 | 37,142 | 5,479 | 41.0 |
| 3 | L0-main | claudeopus46 | 13,598 | 34,954 | 48,552 | 6,781 | 51.4 |
| 4 | L0-main | claudeopus46 | 13,598 | 47,659 | 61,257 | 7,288 | 52.9 |
| 5 | L0-main | claudeopus46 | 2,106 | 6,069 | 8,175 | 154 | 2.6 |
| 6 | L0-main | claudeopus46 | 366 | 694 | 1,060 | 137 | 2.0 |
| 7 | L0-main | claudeopus46 | 2,320 | 5,560 | 7,880 | 1,348 | 9.6 |
| 8 | L0-main | claudeopus46 | 366 | 1,823 | 2,189 | 1,294 | 5.5 |
| 9 | L0-main | claudeopus46 | 560 | 6,042 | 6,602 | 100 | 2.2 |
| 10 | L0-main | claudeopus46 | 1,156 | 6,820 | 7,976 | 584 | 5.6 |
| 11 | L0-main | claudeopus46 | 1,292 | 6,411 | 7,703 | 1,605 | 11.1 |

