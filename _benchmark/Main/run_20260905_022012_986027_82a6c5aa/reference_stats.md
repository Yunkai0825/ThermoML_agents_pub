# Reference Stats — main-agent

**Run started:** 2026-09-05 02:20:13
**Wall time (at last flush):** 257.9 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 10 | 48,960 | 29,981 | 8,092 | 78,941 | 7,894 | 58.8 | claudeopus46 |
| **TOTAL** | **10** | **48,960** | **29,981** | **8,092** | **78,941** | **7,894** | **58.8** | |

**Estimated tokens:** ~19,735 input + ~2,023 output = ~21,758 total
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
| 1 | 2 | `run_query_agent` | context=The user wants the experiment…, purpose=Re… | 11,227 | — | — | 202.5 |
| | | **TOTAL (1 tools)** | | **11,227** | | **0** | **202.5** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 13,598 | 298 | 13,896 | 1,345 | 8.4 |
| 2 | L0-main | claudeopus46 | 13,598 | 982 | 14,580 | 1,164 | 7.6 |
| 3 | L0-main | claudeopus46 | 13,598 | 13,655 | 27,253 | 1,696 | 12.0 |
| 4 | L0-main | claudeopus46 | 2,106 | 2,259 | 4,365 | 153 | 2.4 |
| 5 | L0-main | claudeopus46 | 2,320 | 1,864 | 4,184 | 853 | 4.8 |
| 6 | L0-main | claudeopus46 | 366 | 693 | 1,059 | 220 | 2.4 |
| 7 | L0-main | claudeopus46 | 366 | 1,328 | 1,694 | 809 | 3.7 |
| 8 | L0-main | claudeopus46 | 560 | 2,371 | 2,931 | 99 | 2.3 |
| 9 | L0-main | claudeopus46 | 1,156 | 3,124 | 4,280 | 468 | 3.9 |
| 10 | L0-main | claudeopus46 | 1,292 | 3,407 | 4,699 | 1,285 | 11.3 |

