# Reference Stats — analysis-agent

**Run started:** 2026-09-05 04:45:27
**Wall time (at last flush):** 211.9 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 16 | 254,774 | 61,415 | 29,448 | 316,189 | 19,761 | 211.6 | claudeopus46 |
| **TOTAL** | **16** | **254,774** | **61,415** | **29,448** | **316,189** | **19,761** | **211.6** | |

**Estimated tokens:** ~79,047 input + ~7,362 output = ~86,409 total
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
| 1 | 3 | `predict_from_rk` | coeffs=[-4.987765356267973e-06, 2.71…, mixing_rule… | 206 | — | — | 0.5 |
| 2 | 4 | `list_session_files` |  | 212 | — | — | 0.0 |
| 3 | 5 | `predict_from_rk` | coeffs=[-4.987765356267973e-06, 2.71…, mixing_rule… | 205 | — | — | 0.1 |
| 4 | 6 | `predict_from_rk` | coeffs=[-4.987765356267973e-06, 2.71…, n_points=5,… | 204 | — | — | 0.0 |
| 5 | 7 | `predict_from_rk` | coeffs=[-4.987765356267973e-06, 2.71…, n_points=10… | 177 | — | — | 0.2 |
| 6 | 8 | `predict_from_rk` | coeffs=[4.987765356267973e-06, -2.71…, n_points=10… | 188 | — | — | 0.2 |
| | | **TOTAL (6 tools)** | | **1,192** | | **0** | **1.0** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 22,518 | 1,004 | 23,522 | 898 | 6.6 |
| 2 | L0-main | claudeopus46 | 22,518 | 2,287 | 24,805 | 1,648 | 9.3 |
| 3 | L0-main | claudeopus46 | 22,518 | 3,039 | 25,557 | 807 | 5.4 |
| 4 | L0-main | claudeopus46 | 22,518 | 2,140 | 24,658 | 1,968 | 14.6 |
| 5 | L0-main | claudeopus46 | 22,518 | 2,677 | 25,195 | 2,206 | 14.3 |
| 6 | L0-main | claudeopus46 | 22,518 | 3,278 | 25,796 | 2,425 | 18.8 |
| 7 | L0-main | claudeopus46 | 22,518 | 3,872 | 26,390 | 3,486 | 24.6 |
| 8 | L0-main | claudeopus46 | 22,518 | 4,421 | 26,939 | 7,003 | 50.0 |
| 9 | L0-main | claudeopus46 | 22,518 | 5,053 | 27,571 | 1,585 | 15.9 |
| 10 | L0-main | claudeopus46 | 22,518 | 8,960 | 31,478 | 2,614 | 16.5 |
| 11 | L0-main | claudeopus46 | 22,518 | 13,917 | 36,435 | 2,177 | 13.4 |
| 12 | L0-main | claudeopus46 | 2,106 | 2,968 | 5,074 | 31 | 1.7 |
| 13 | L0-main | claudeopus46 | 366 | 554 | 920 | 14 | 2.4 |
| 14 | L0-main | claudeopus46 | 2,320 | 1,866 | 4,186 | 799 | 5.1 |
| 15 | L0-main | claudeopus46 | 366 | 1,236 | 1,602 | 764 | 3.5 |
| 16 | L0-main | claudeopus46 | 1,918 | 4,143 | 6,061 | 1,023 | 9.5 |

