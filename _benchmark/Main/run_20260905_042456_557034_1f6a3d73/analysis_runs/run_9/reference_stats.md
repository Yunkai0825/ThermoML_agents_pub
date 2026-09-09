# Reference Stats — analysis-agent

**Run started:** 2026-09-05 04:45:27
**Wall time (at last flush):** 201.8 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 19 | 279,008 | 86,455 | 28,265 | 365,463 | 19,234 | 204.3 | claudeopus46 |
| **TOTAL** | **19** | **279,008** | **86,455** | **28,265** | **365,463** | **19,234** | **204.3** | |

**Estimated tokens:** ~91,365 input + ~7,066 output = ~98,431 total
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
| 1 | 4 | `predict_from_rk` | coeffs=[-3.982385645518985e-06, -1.5…, n_points=20… | 207 | — | — | 0.0 |
| 2 | 6 | `predict_from_rk` | coeffs=[-3.982385645518985e-06, -1.5…, mixing_rule… | 207 | — | — | 0.0 |
| 3 | 7 | `compute_ideal_baseline` | mixing_rule=linear, n_points=13, property_type=mol… | 139 | — | — | 0.0 |
| 4 | 8 | `predict_from_rk` | coeffs=[-3.982385645518985e-06, -1.5…, mixing_rule… | 206 | — | — | 0.0 |
| 5 | 9 | `list_session_files` |  | 211 | — | — | 0.1 |
| | | **TOTAL (5 tools)** | | **970** | | **0** | **0.1** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 22,518 | 975 | 23,493 | 1,174 | 7.5 |
| 2 | L0-main | claudeopus46 | 22,518 | 1,673 | 24,191 | 802 | 5.2 |
| 3 | L0-main | claudeopus46 | 22,518 | 2,338 | 24,856 | 974 | 6.1 |
| 4 | L0-main | claudeopus46 | 22,518 | 3,161 | 25,679 | 929 | 6.3 |
| 5 | L0-main | claudeopus46 | 22,518 | 2,736 | 25,254 | 2,457 | 16.6 |
| 6 | L0-main | claudeopus46 | 22,518 | 3,550 | 26,068 | 1,060 | 10.1 |
| 7 | L0-main | claudeopus46 | 22,518 | 3,735 | 26,253 | 1,975 | 15.4 |
| 8 | L0-main | claudeopus46 | 22,518 | 4,315 | 26,833 | 2,514 | 20.0 |
| 9 | L0-main | claudeopus46 | 22,518 | 4,878 | 27,396 | 994 | 7.8 |
| 10 | L0-main | claudeopus46 | 22,518 | 5,385 | 27,903 | 5,544 | 39.7 |
| 11 | L0-main | claudeopus46 | 22,518 | 13,054 | 35,572 | 3,378 | 21.5 |
| 12 | L0-main | claudeopus46 | 22,518 | 18,548 | 41,066 | 2,491 | 13.7 |
| 13 | L0-main | claudeopus46 | 2,106 | 3,910 | 6,016 | 112 | 2.8 |
| 14 | L0-main | claudeopus46 | 366 | 635 | 1,001 | 116 | 2.3 |
| 15 | L0-main | claudeopus46 | 2,320 | 2,836 | 5,156 | 1,085 | 6.4 |
| 16 | L0-main | claudeopus46 | 366 | 1,522 | 1,888 | 1,040 | 4.8 |
| 17 | L0-main | claudeopus46 | 560 | 3,336 | 3,896 | 70 | 3.1 |
| 18 | L0-main | claudeopus46 | 1,156 | 4,135 | 5,291 | 509 | 6.2 |
| 19 | L0-main | claudeopus46 | 1,918 | 5,733 | 7,651 | 1,041 | 8.8 |

