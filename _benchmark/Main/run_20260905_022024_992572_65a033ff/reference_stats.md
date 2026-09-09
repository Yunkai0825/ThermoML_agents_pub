# Reference Stats — main-agent

**Run started:** 2026-09-05 02:20:25
**Wall time (at last flush):** 480.7 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 18 | 157,744 | 301,834 | 29,379 | 459,578 | 25,532 | 209.7 | claudeopus46 |
| L1-worker | 4 | 15,068 | 4,247 | 3,353 | 19,315 | 4,828 | 28.2 | claudeopus46 |
| **TOTAL** | **22** | **172,812** | **306,081** | **32,732** | **478,893** | **21,767** | **237.9** | |

**Estimated tokens:** ~119,723 input + ~8,183 output = ~127,906 total
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
| 1 | 2 | `run_query_agent` | context=The user wants specific exper…, purpose=Lo… | 13,629 | — | — | 241.2 |
| 2 | 4 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_1…, purpose=Ins… | 431 | — | — | 6.8 |
| 3 | 6 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_7481'…, purpose=Ver… | 551 | — | — | 7.4 |
| 4 | 7 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_7481'…, purpose=Che… | 575 | — | — | 8.7 |
| 5 | 10 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_7481'…, purpose=Ver… | 637 | — | — | 8.1 |
| | | **TOTAL (5 tools)** | | **15,823** | | **0** | **272.2** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 13,598 | 318 | 13,916 | 1,155 | 7.5 |
| 2 | L0-main | claudeopus46 | 13,598 | 967 | 14,565 | 1,255 | 8.1 |
| 3 | L0-main | claudeopus46 | 13,598 | 15,714 | 29,312 | 4,384 | 30.5 |
| 4 | L0-main | claudeopus46 | 13,598 | 25,450 | 39,048 | 1,466 | 12.2 |
| 5 | L1-worker | claudeopus46 | 3,767 | 1,023 | 4,790 | 618 | 5.3 |
| 6 | L0-main | claudeopus46 | 13,598 | 26,321 | 39,919 | 732 | 6.8 |
| 7 | L0-main | claudeopus46 | 13,598 | 27,148 | 40,746 | 732 | 6.9 |
| 8 | L1-worker | claudeopus46 | 3,767 | 988 | 4,755 | 857 | 7.0 |
| 9 | L0-main | claudeopus46 | 13,598 | 27,599 | 41,197 | 665 | 6.3 |
| 10 | L1-worker | claudeopus46 | 3,767 | 1,130 | 4,897 | 916 | 8.1 |
| 11 | L0-main | claudeopus46 | 13,598 | 28,595 | 42,193 | 5,250 | 28.1 |
| 12 | L0-main | claudeopus46 | 13,598 | 39,197 | 52,795 | 3,181 | 25.0 |
| 13 | L0-main | claudeopus46 | 13,598 | 40,199 | 53,797 | 650 | 6.2 |
| 14 | L1-worker | claudeopus46 | 3,767 | 1,106 | 4,873 | 962 | 7.8 |
| 15 | L0-main | claudeopus46 | 13,598 | 40,697 | 54,295 | 5,149 | 35.5 |
| 16 | L0-main | claudeopus46 | 2,106 | 4,719 | 6,825 | 273 | 2.9 |
| 17 | L0-main | claudeopus46 | 2,320 | 4,304 | 6,624 | 859 | 6.0 |
| 18 | L0-main | claudeopus46 | 366 | 813 | 1,179 | 259 | 3.3 |
| 19 | L0-main | claudeopus46 | 366 | 1,334 | 1,700 | 820 | 4.1 |
| 20 | L0-main | claudeopus46 | 560 | 5,071 | 5,631 | 185 | 2.8 |
| 21 | L0-main | claudeopus46 | 1,156 | 6,592 | 7,748 | 943 | 6.5 |
| 22 | L0-main | claudeopus46 | 1,292 | 6,796 | 8,088 | 1,421 | 11.0 |

