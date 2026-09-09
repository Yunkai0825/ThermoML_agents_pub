# Reference Stats — main-agent

**Run started:** 2026-08-15 19:42:52
**Wall time (at last flush):** 255.0 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 11 | 62,558 | 51,412 | 13,352 | 113,970 | 10,360 | 100.9 | claudeopus46 |
| **TOTAL** | **11** | **62,558** | **51,412** | **13,352** | **113,970** | **10,360** | **100.9** | |

**Estimated tokens:** ~28,492 input + ~3,338 output = ~31,830 total
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
| 1 | 2 | `run_query_agent` | context=The user wants to know what s…, purpose=Lo… | 10,477 | — | — | 157.9 |
| | | **TOTAL (1 tools)** | | **10,477** | | **0** | **157.9** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 13,598 | 331 | 13,929 | 1,324 | 8.9 |
| 2 | L0-main | claudeopus46 | 13,598 | 1,042 | 14,640 | 1,272 | 7.4 |
| 3 | L0-main | claudeopus46 | 13,598 | 13,030 | 26,628 | 3,493 | 21.6 |
| 4 | L0-main | claudeopus46 | 13,598 | 19,145 | 32,743 | 3,702 | 21.0 |
| 5 | L0-main | claudeopus46 | 2,106 | 2,950 | 5,056 | 146 | 2.4 |
| 6 | L0-main | claudeopus46 | 2,320 | 2,522 | 4,842 | 671 | 4.3 |
| 7 | L0-main | claudeopus46 | 366 | 686 | 1,052 | 187 | 2.2 |
| 8 | L0-main | claudeopus46 | 366 | 1,146 | 1,512 | 632 | 15.7 |
| 9 | L0-main | claudeopus46 | 560 | 2,996 | 3,556 | 98 | 2.1 |
| 10 | L0-main | claudeopus46 | 1,156 | 3,698 | 4,854 | 403 | 3.8 |
| 11 | L0-main | claudeopus46 | 1,292 | 3,866 | 5,158 | 1,424 | 11.5 |

