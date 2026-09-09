# Reference Stats — main-agent

**Run started:** 2026-09-05 04:35:03
**Wall time (at last flush):** 983.8 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 11 | 62,558 | 161,927 | 31,289 | 224,485 | 20,407 | 217.2 | claudeopus46 |
| **TOTAL** | **11** | **62,558** | **161,927** | **31,289** | **224,485** | **20,407** | **217.2** | |

**Estimated tokens:** ~56,121 input + ~7,822 output = ~63,943 total
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
| 1 | 1 | `run_analysis_agent` | context=The user wants to know if mix…, purpose=De… | 43,435 | — | — | 770.8 |
| | | **TOTAL (1 tools)** | | **43,435** | | **0** | **770.8** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 13,598 | 375 | 13,973 | 1,979 | 12.0 |
| 2 | L0-main | claudeopus46 | 13,598 | 29,608 | 43,206 | 6,737 | 47.4 |
| 3 | L0-main | claudeopus46 | 13,598 | 39,960 | 53,558 | 7,962 | 57.4 |
| 4 | L0-main | claudeopus46 | 13,598 | 50,601 | 64,199 | 8,294 | 56.4 |
| 5 | L0-main | claudeopus46 | 2,106 | 7,623 | 9,729 | 273 | 2.7 |
| 6 | L0-main | claudeopus46 | 366 | 813 | 1,179 | 367 | 3.0 |
| 7 | L0-main | claudeopus46 | 2,320 | 7,151 | 9,471 | 1,568 | 10.1 |
| 8 | L0-main | claudeopus46 | 366 | 2,043 | 2,409 | 1,509 | 4.9 |
| 9 | L0-main | claudeopus46 | 560 | 7,918 | 8,478 | 185 | 2.9 |
| 10 | L0-main | claudeopus46 | 1,156 | 9,461 | 10,617 | 844 | 8.0 |
| 11 | L0-main | claudeopus46 | 1,292 | 6,374 | 7,666 | 1,571 | 12.4 |

