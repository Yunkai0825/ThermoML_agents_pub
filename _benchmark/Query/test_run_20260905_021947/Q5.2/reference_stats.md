# Reference Stats — query-agent

**Run started:** 2026-09-05 05:58:40
**Wall time (at last flush):** 261.5 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 9 | 29,806 | 65,109 | 15,618 | 94,915 | 10,546 | 90.4 | claudeopus46 |
| L1-worker | 22 | 249,796 | 96,959 | 30,887 | 346,755 | 15,761 | 190.3 | claudeopus46 |
| **TOTAL** | **31** | **279,602** | **162,068** | **46,505** | **441,670** | **14,247** | **280.7** | |

**Estimated tokens:** ~110,417 input + ~11,626 output = ~122,043 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 5 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 5 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 5 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_system_summary` | 2 | 0 | 0 | 0 | 32 | 59 | 2,584 |
| `search_system_summary` | 2 | 0 | 0 | 0 | 18 | 34 | 1,780 |
| `search_system_summary` | 2 | 0 | 0 | 0 | 15 | 28 | 2,079 |
| `search_system_summary` | 2 | 0 | 0 | 0 | 16 | 40 | 3,638 |
| **TOTAL** | **23** | **0** | **0** | **0** | **81** | **161** | **10,081** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (11 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_1 |  | resolve_compound_ids, search_system_summary |
| GLOBcomp_24 |  | resolve_compound_ids, search_system_summary |
| GLOBcomp_2199 |  | resolve_compound_ids |
| GLOBcomp_5558 |  | resolve_compound_ids |
| GLOBcomp_113 |  | resolve_compound_ids, search_system_summary |
| GLOBcomp_61 |  | resolve_compound_ids, search_system_summary |
| GLOBcomp_2 |  | resolve_compound_ids |
| GLOBcomp_378 |  | resolve_compound_ids |
| GLOBcomp_1874 |  | resolve_compound_ids |
| GLOBcomp_4802 |  | resolve_compound_ids |
| GLOBcomp_111 |  | resolve_compound_ids, search_system_summary |

#### References (47 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_5201 |  | search_system_summary |
| GLOBlit_10102 |  | search_system_summary |
| GLOBlit_8038 |  | search_system_summary |
| GLOBlit_6951 |  | search_system_summary |
| GLOBlit_1283 |  | search_system_summary |
| GLOBlit_6630 |  | search_system_summary |
| GLOBlit_11186 |  | search_system_summary |
| GLOBlit_1223 |  | search_system_summary |
| GLOBlit_8324 |  | search_system_summary |
| GLOBlit_8106 |  | search_system_summary |
| GLOBlit_11906 |  | search_system_summary |
| GLOBlit_7228 |  | search_system_summary |
| GLOBlit_6686 |  | search_system_summary |
| GLOBlit_7369 |  | search_system_summary |
| GLOBlit_3286 |  | search_system_summary |
| GLOBlit_7440 |  | search_system_summary |
| GLOBlit_9693 |  | search_system_summary |
| GLOBlit_2605 |  | search_system_summary |
| GLOBlit_8736 |  | search_system_summary |
| GLOBlit_11506 |  | search_system_summary |
| GLOBlit_8239 |  | search_system_summary |
| GLOBlit_7545 |  | search_system_summary |
| GLOBlit_9758 |  | search_system_summary |
| GLOBlit_1623 |  | search_system_summary |
| GLOBlit_2979 |  | search_system_summary |
| GLOBlit_8556 |  | search_system_summary |
| GLOBlit_10313 |  | search_system_summary |
| GLOBlit_6775 |  | search_system_summary |
| GLOBlit_2574 |  | search_system_summary |
| GLOBlit_5826 |  | search_system_summary |
| GLOBlit_3180 |  | search_system_summary |
| GLOBlit_8686 |  | search_system_summary |
| GLOBlit_2831 |  | search_system_summary |
| GLOBlit_5233 |  | search_system_summary |
| GLOBlit_5907 |  | search_system_summary |
| GLOBlit_4754 |  | search_system_summary |
| GLOBlit_11031 |  | search_system_summary |
| GLOBlit_9382 |  | search_system_summary |
| GLOBlit_721 |  | search_system_summary |
| GLOBlit_5254 |  | search_system_summary |
| GLOBlit_5843 |  | search_system_summary |
| GLOBlit_10111 |  | search_system_summary |
| GLOBlit_1753 |  | search_system_summary |
| GLOBlit_4395 |  | search_system_summary |
| GLOBlit_11775 |  | search_system_summary |
| GLOBlit_11353 |  | search_system_summary |
| GLOBlit_950 |  | search_system_summary |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 11 |
| Unique References | 47 |
| Total DOIs | 0 |
| Unique parent blocks | 0 |
| Explicit block/subsystem targets | 0 |
| Subsystem targets | 0 |
| Target-matched data points | 0 |

---

## 3. DOI & Block References

*(no DOI/block references recorded)*

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=60, purpose=Resolve compound ID… | 965 | KEEP ←in 591 | 965 | 12.6 |
| 2 | 3 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve propylene g… | 637 | KEEP ←in 544 | 637 | 9.1 |
| 3 | 4 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve diethylene … | 215 | KEEP ←in 548 | 215 | 4.7 |
| 4 | 5 | `search_system_summary` | compound=['GLOBcomp_1', 'GLOBcomp_24'], purpose=Fi… | 1,179 | KEEP ←in 1,085 | 1179 | 11.2 |
| 5 | 6 | `search_system_summary` | compound=['GLOBcomp_1', 'GLOBcomp_61'], purpose=Fi… | 1,360 | KEEP ←in 1,136 | 1360 | 15.8 |
| 6 | 7 | `search_system_summary` | compound=['GLOBcomp_1', 'GLOBcomp_111'], purpose=F… | 1,067 | KEEP ←in 1,106 | 1067 | 9.5 |
| 7 | 8 | `search_system_summary` | compound=['GLOBcomp_1', 'GLOBcomp_113'], purpose=F… | 1,297 | KEEP ←in 1,160 | 1297 | 11.1 |
| 8 | 1 | `L1_query` | context=User wants a broad overview o…, id_catalog… | 12,623 | — | — | 182.0 |
| | | **TOTAL (8 tools)** | | **19,343** | | **6,720** | **256.0** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 514 | 12,095 | 1,293 | 9.2 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,107 | 25,202 | 1,048 | 6.2 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,256 | 26,351 | 679 | 4.3 |
| 4 | L1-worker | claudeopus46 | 3,767 | 813 | 4,580 | 1,804 | 11.7 |
| 5 | L1-worker | claudeopus46 | 24,095 | 2,515 | 26,610 | 731 | 5.3 |
| 6 | L1-worker | claudeopus46 | 3,767 | 758 | 4,525 | 1,128 | 8.5 |
| 7 | L1-worker | claudeopus46 | 24,095 | 3,491 | 27,586 | 1,017 | 8.1 |
| 8 | L1-worker | claudeopus46 | 3,767 | 693 | 4,460 | 371 | 4.1 |
| 9 | L1-worker | claudeopus46 | 24,095 | 3,997 | 28,092 | 842 | 6.9 |
| 10 | L1-worker | claudeopus46 | 3,767 | 1,518 | 5,285 | 1,532 | 10.8 |
| 11 | L1-worker | claudeopus46 | 24,095 | 5,474 | 29,569 | 713 | 5.6 |
| 12 | L1-worker | claudeopus46 | 3,767 | 1,606 | 5,373 | 1,670 | 10.2 |
| 13 | L1-worker | claudeopus46 | 24,095 | 7,138 | 31,233 | 610 | 6.4 |
| 14 | L1-worker | claudeopus46 | 3,767 | 1,575 | 5,342 | 1,368 | 8.3 |
| 15 | L1-worker | claudeopus46 | 24,095 | 8,528 | 32,623 | 532 | 4.4 |
| 16 | L1-worker | claudeopus46 | 3,767 | 1,631 | 5,398 | 1,828 | 10.7 |
| 17 | L1-worker | claudeopus46 | 24,095 | 10,115 | 34,210 | 6,916 | 37.4 |
| 18 | L1-worker | claudeopus46 | 2,320 | 6,441 | 8,761 | 1,655 | 7.7 |
| 19 | L1-worker | claudeopus46 | 627 | 6,321 | 6,948 | 1,405 | 7.7 |
| 20 | L1-worker | claudeopus46 | 2,106 | 7,669 | 9,775 | 1,549 | 7.8 |
| 21 | L1-worker | claudeopus46 | 366 | 2,326 | 2,692 | 1,001 | 5.0 |
| 22 | L1-worker | claudeopus46 | 366 | 2,092 | 2,458 | 1,571 | 5.4 |
| 23 | L1-worker | claudeopus46 | 787 | 18,895 | 19,682 | 917 | 7.8 |
| 24 | L0-main | claudeopus46 | 11,581 | 27,069 | 38,650 | 6,577 | 36.9 |
| 25 | L0-main | claudeopus46 | 2,320 | 6,520 | 8,840 | 1,518 | 7.1 |
| 26 | L0-main | claudeopus46 | 2,106 | 6,866 | 8,972 | 1,319 | 9.0 |
| 27 | L0-main | claudeopus46 | 366 | 1,993 | 2,359 | 1,459 | 4.9 |
| 28 | L0-main | claudeopus46 | 366 | 1,868 | 2,234 | 2,222 | 8.5 |
| 29 | L0-main | claudeopus46 | 560 | 10,710 | 11,270 | 538 | 6.9 |
| 30 | L0-main | claudeopus46 | 560 | 8,310 | 8,870 | 677 | 6.2 |
| 31 | L0-main | claudeopus46 | 366 | 1,259 | 1,625 | 15 | 1.7 |

