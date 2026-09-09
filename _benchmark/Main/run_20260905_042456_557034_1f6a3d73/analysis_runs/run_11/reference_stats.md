# Reference Stats — analysis-agent

**Run started:** 2026-09-05 04:48:49
**Wall time (at last flush):** 294.3 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 18 | 256,490 | 113,427 | 39,729 | 369,917 | 20,550 | 295.3 | claudeopus46 |
| **TOTAL** | **18** | **256,490** | **113,427** | **39,729** | **369,917** | **20,550** | **295.3** | |

**Estimated tokens:** ~92,479 input + ~9,932 output = ~102,411 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `list_session_files` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **0** | **0** | **0** | **0** | **0** | **0** | **0** |

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
| 1 | 4 | `predict_from_rk` | coeffs=[-1.1303359340037732e-06, -7.…, mixing_rule… | 207 | — | — | 0.0 |
| 2 | 5 | `list_session_files` |  | 212 | — | — | 0.0 |
| 3 | 6 | `predict_from_rk` | coeffs=[-1.1303359340037732e-06, -7.…, mixing_rule… | 206 | — | — | 0.0 |
| 4 | 7 | `predict_from_rk` | coeffs=[-1.1303359340037732e-06, -7.…, mixing_rule… | 207 | — | — | 0.0 |
| | | **TOTAL (4 tools)** | | **832** | | **0** | **0.0** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 22,518 | 979 | 23,497 | 1,527 | 10.3 |
| 2 | L0-main | claudeopus46 | 22,518 | 2,405 | 24,923 | 692 | 4.2 |
| 3 | L0-main | claudeopus46 | 22,518 | 3,103 | 25,621 | 803 | 4.8 |
| 4 | L0-main | claudeopus46 | 22,518 | 3,808 | 26,326 | 839 | 6.5 |
| 5 | L0-main | claudeopus46 | 22,518 | 2,413 | 24,931 | 1,356 | 11.6 |
| 6 | L0-main | claudeopus46 | 22,518 | 2,958 | 25,476 | 3,650 | 24.9 |
| 7 | L0-main | claudeopus46 | 22,518 | 3,628 | 26,146 | 4,384 | 29.7 |
| 8 | L0-main | claudeopus46 | 22,518 | 4,223 | 26,741 | 10,783 | 74.2 |
| 9 | L0-main | claudeopus46 | 22,518 | 15,406 | 37,924 | 2,789 | 27.4 |
| 10 | L0-main | claudeopus46 | 22,518 | 21,157 | 43,675 | 4,455 | 34.5 |
| 11 | L0-main | claudeopus46 | 22,518 | 28,586 | 51,104 | 4,249 | 33.4 |
| 12 | L0-main | claudeopus46 | 2,106 | 4,619 | 6,725 | 111 | 2.6 |
| 13 | L0-main | claudeopus46 | 366 | 634 | 1,000 | 115 | 2.0 |
| 14 | L0-main | claudeopus46 | 2,320 | 3,542 | 5,862 | 1,186 | 7.0 |
| 15 | L0-main | claudeopus46 | 366 | 1,623 | 1,989 | 1,141 | 4.2 |
| 16 | L0-main | claudeopus46 | 560 | 4,041 | 4,601 | 65 | 2.3 |
| 17 | L0-main | claudeopus46 | 1,156 | 4,856 | 6,012 | 473 | 5.7 |
| 18 | L0-main | claudeopus46 | 1,918 | 5,446 | 7,364 | 1,111 | 10.0 |

