# Reference Stats — main-agent

**Run started:** 2026-08-15 19:29:13
**Wall time (at last flush):** 783.4 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 13 | 76,522 | 156,172 | 27,608 | 232,694 | 17,899 | 188.1 | claudeopus46 |
| L1-worker | 1 | 3,767 | 1,109 | 873 | 4,876 | 4,876 | 6.9 | claudeopus46 |
| **TOTAL** | **14** | **80,289** | **157,281** | **28,481** | **237,570** | **16,969** | **195.0** | |

**Estimated tokens:** ~59,392 input + ~7,120 output = ~66,512 total
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
| 1 | 1 | `run_analysis_agent` | context=The user wants a complete Red…, purpose=Fi… | 21,141 | — | — | 593.7 |
| 2 | 4 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_1…, purpose=Con… | 578 | — | — | 7.2 |
| | | **TOTAL (2 tools)** | | **21,719** | | **0** | **600.9** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 13,598 | 472 | 14,070 | 1,814 | 10.6 |
| 2 | L0-main | claudeopus46 | 13,598 | 22,067 | 35,665 | 3,499 | 24.8 |
| 3 | L0-main | claudeopus46 | 13,598 | 28,375 | 41,973 | 4,031 | 29.2 |
| 4 | L0-main | claudeopus46 | 13,598 | 35,027 | 48,625 | 7,918 | 52.6 |
| 5 | L1-worker | claudeopus46 | 3,767 | 1,109 | 4,876 | 873 | 6.9 |
| 6 | L0-main | claudeopus46 | 13,598 | 36,357 | 49,955 | 3,807 | 27.2 |
| 7 | L0-main | claudeopus46 | 2,106 | 5,236 | 7,342 | 373 | 3.2 |
| 8 | L0-main | claudeopus46 | 366 | 913 | 1,279 | 520 | 3.2 |
| 9 | L0-main | claudeopus46 | 2,320 | 4,667 | 6,987 | 1,035 | 7.6 |
| 10 | L0-main | claudeopus46 | 366 | 1,510 | 1,876 | 986 | 4.1 |
| 11 | L0-main | claudeopus46 | 560 | 5,700 | 6,260 | 251 | 2.6 |
| 12 | L0-main | claudeopus46 | 1,156 | 7,664 | 8,820 | 950 | 7.0 |
| 13 | L0-main | claudeopus46 | 366 | 1,643 | 2,009 | 904 | 4.6 |
| 14 | L0-main | claudeopus46 | 1,292 | 6,541 | 7,833 | 1,520 | 11.4 |

