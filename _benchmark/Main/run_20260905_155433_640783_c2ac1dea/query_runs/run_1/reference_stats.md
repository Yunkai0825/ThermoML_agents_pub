# Reference Stats — query-agent

**Run started:** 2026-09-05 15:55:36
**Wall time (at last flush):** 249.7 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 7 | 39,901 | 28,333 | 8,436 | 68,234 | 9,747 | 56.2 | claudeopus46 |
| L1-worker | 32 | 335,821 | 88,413 | 22,774 | 424,234 | 13,257 | 182.1 | claudeopus46 |
| verdict | 1 | 972 | 4,518 | 1,023 | 5,490 | 5,490 | 8.7 | claudeopus46 |
| **TOTAL** | **40** | **376,694** | **121,264** | **32,233** | **497,958** | **12,448** | **247.0** | |

**Estimated tokens:** ~124,489 input + ~8,058 output = ~132,547 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 20 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 20 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_id_alignment` | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_id_alignment` | 20 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_id_alignment` | 20 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **82** | **0** | **0** | **0** | **0** | **0** | **0** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (57 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_863 |  | resolve_compound_ids, search_id_alignment |
| GLOBcomp_1676 |  | resolve_compound_ids, search_id_alignment |
| GLOBcomp_1677 |  | resolve_compound_ids, search_id_alignment |
| GLOBcomp_1993 |  | resolve_compound_ids |
| GLOBcomp_8470 |  | resolve_compound_ids |
| GLOBcomp_819 |  | resolve_compound_ids |
| GLOBcomp_1294 |  | resolve_compound_ids |
| GLOBcomp_3941 |  | resolve_compound_ids |
| GLOBcomp_3948 |  | resolve_compound_ids |
| GLOBcomp_5655 |  | resolve_compound_ids |
| GLOBcomp_5715 |  | resolve_compound_ids |
| GLOBcomp_5541 |  | resolve_compound_ids |
| GLOBcomp_6949 |  | resolve_compound_ids |
| GLOBcomp_31 |  | resolve_compound_ids |
| GLOBcomp_312 |  | resolve_compound_ids |
| GLOBcomp_1755 |  | resolve_compound_ids |
| GLOBcomp_2088 |  | resolve_compound_ids |
| GLOBcomp_4689 |  | resolve_compound_ids |
| GLOBcomp_5069 |  | resolve_compound_ids |
| GLOBcomp_5678 |  | resolve_compound_ids |
| GLOBcomp_6701 |  | resolve_compound_ids |
| GLOBcomp_1115 |  | resolve_compound_ids |
| GLOBcomp_6333 |  | resolve_compound_ids |
| GLOBcomp_7157 |  | resolve_compound_ids |
| GLOBcomp_111 |  | resolve_compound_ids |
| GLOBcomp_2888 |  | resolve_compound_ids |
| GLOBcomp_5885 |  | resolve_compound_ids |
| GLOBcomp_7279 |  | resolve_compound_ids |
| GLOBcomp_2407 |  | search_id_alignment |
| GLOBcomp_952 |  | search_id_alignment |
| GLOBcomp_1480 |  | search_id_alignment |
| GLOBcomp_1653 |  | search_id_alignment |
| GLOBcomp_996 |  | search_id_alignment |
| GLOBcomp_257 |  | search_id_alignment |
| GLOBcomp_1546 |  | search_id_alignment |
| GLOBcomp_6596 |  | search_id_alignment |
| GLOBcomp_57 |  | search_id_alignment |
| GLOBcomp_685 |  | search_id_alignment |
| GLOBcomp_1879 |  | search_id_alignment |
| GLOBcomp_25 |  | search_id_alignment |
| GLOBcomp_543 |  | search_id_alignment |
| GLOBcomp_687 |  | search_id_alignment |
| GLOBcomp_883 |  | search_id_alignment |
| GLOBcomp_1766 |  | search_id_alignment |
| GLOBcomp_2924 |  | search_id_alignment |
| GLOBcomp_4943 |  | search_id_alignment |
| GLOBcomp_7447 |  | search_id_alignment |
| GLOBcomp_8308 |  | search_id_alignment |
| GLOBcomp_861 |  | search_id_alignment |
| GLOBcomp_3215 |  | search_id_alignment |
| GLOBcomp_208 |  | search_id_alignment |
| GLOBcomp_245 |  | search_id_alignment |
| GLOBcomp_262 |  | search_id_alignment |
| GLOBcomp_1486 |  | search_id_alignment |
| GLOBcomp_2224 |  | search_id_alignment |
| GLOBcomp_7042 |  | search_id_alignment |
| GLOBcomp_1 |  | resolve_compound_ids |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 57 |
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
| 1 | 2 | `resolve_compound_ids` | limit=20, min_score=40, purpose=Find all compounds… | 790 | DISCARD ←in 1,805 | 725 | 11.1 |
| 2 | 3 | `resolve_compound_ids` | limit=20, min_score=40, purpose=Find ethylene oxid… | 562 | DISCARD ←in 1,772 | 497 | 8.9 |
| 3 | 4 | `search_id_alignment` | entity_type=compound, limit=20, purpose=Find ethyl… | 242 | KEEP ←in 283 | 242 | 4.2 |
| 4 | 5 | `search_id_alignment` | entity_type=compound, limit=20, purpose=Find triox… | 418 | KEEP ←in 1,997 | 418 | 7.0 |
| 5 | 6 | `search_id_alignment` | entity_type=compound, limit=20, purpose=Find triox… | 823 | DISCARD ←in 1,892 | 759 | 11.8 |
| 6 | 1 | `L1_query` | context=User is trying to identify wh…, id_catalog… | 3,244 | — | — | 100.1 |
| 7 | 1 | `resolve_compound_ids` | purpose=Resolve water compound ID for…, queries=wa… | 156 | KEEP ←in 216 | 156 | 3.8 |
| 8 | 2 | `search_blocks` | compound=['GLOBcomp_952', 'GLOBcomp_1'], limit=50,… | 839 | DISCARD ←in 39 | 781 | 15.5 |
| 9 | 3 | `search_blocks` | compound=['GLOBcomp_2407', 'GLOBcomp_1…, limit=50,… | 741 | DISCARD ←in 39 | 683 | 14.4 |
| 10 | 4 | `search_blocks` | compound=['GLOBcomp_1480', 'GLOBcomp_1…, limit=50,… | 756 | DISCARD ←in 39 | 698 | 13.0 |
| 11 | 2 | `L1_query` | context=User wants viscosity data for…, id_catalog… | 1,667 | — | — | 91.6 |
| | | **TOTAL (11 tools)** | | **10,238** | | **4,959** | **281.4** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 1,053 | 12,634 | 1,494 | 9.9 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,106 | 25,201 | 803 | 5.8 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,247 | 26,342 | 684 | 4.4 |
| 4 | L1-worker | claudeopus46 | 3,767 | 2,026 | 5,793 | 1,226 | 10.2 |
| 5 | L1-worker | claudeopus46 | 24,095 | 2,353 | 26,448 | 627 | 4.8 |
| 6 | L1-worker | claudeopus46 | 3,767 | 1,935 | 5,702 | 1,018 | 8.1 |
| 7 | L1-worker | claudeopus46 | 24,095 | 3,208 | 27,303 | 767 | 6.1 |
| 8 | L1-worker | claudeopus46 | 3,767 | 461 | 4,228 | 441 | 4.0 |
| 9 | L1-worker | claudeopus46 | 24,095 | 3,809 | 27,904 | 553 | 4.5 |
| 10 | L1-worker | claudeopus46 | 3,767 | 2,159 | 5,926 | 679 | 6.6 |
| 11 | L1-worker | claudeopus46 | 24,095 | 4,507 | 28,602 | 589 | 4.7 |
| 12 | L1-worker | claudeopus46 | 3,767 | 2,053 | 5,820 | 1,331 | 11.2 |
| 13 | L1-worker | claudeopus46 | 24,095 | 5,613 | 29,708 | 1,783 | 12.4 |
| 14 | L1-worker | claudeopus46 | 2,106 | 2,705 | 4,811 | 312 | 3.3 |
| 15 | L1-worker | claudeopus46 | 2,320 | 1,478 | 3,798 | 677 | 4.9 |
| 16 | L1-worker | claudeopus46 | 627 | 1,358 | 1,985 | 605 | 4.9 |
| 17 | L1-worker | claudeopus46 | 366 | 1,089 | 1,455 | 206 | 2.3 |
| 18 | L1-worker | claudeopus46 | 366 | 1,114 | 1,480 | 637 | 3.4 |
| 19 | L1-worker | claudeopus46 | 787 | 4,553 | 5,340 | 579 | 5.0 |
| 20 | L0-main | claudeopus46 | 11,581 | 8,013 | 19,594 | 2,153 | 14.8 |
| 21 | L1-worker | claudeopus46 | 24,095 | 5,206 | 29,301 | 1,023 | 7.4 |
| 22 | L1-worker | claudeopus46 | 3,767 | 374 | 4,141 | 269 | 3.7 |
| 23 | L1-worker | claudeopus46 | 24,095 | 5,659 | 29,754 | 1,086 | 7.2 |
| 24 | L1-worker | claudeopus46 | 3,767 | 549 | 4,316 | 1,000 | 8.4 |
| 25 | L1-worker | claudeopus46 | 24,095 | 6,818 | 30,913 | 868 | 6.6 |
| 26 | L1-worker | claudeopus46 | 3,767 | 515 | 4,282 | 895 | 7.0 |
| 27 | L1-worker | claudeopus46 | 24,095 | 7,918 | 32,013 | 948 | 6.9 |
| 28 | L1-worker | claudeopus46 | 3,767 | 499 | 4,266 | 906 | 6.8 |
| 29 | L1-worker | claudeopus46 | 24,095 | 9,114 | 33,209 | 832 | 6.7 |
| 30 | L1-worker | claudeopus46 | 2,106 | 2,851 | 4,957 | 92 | 1.9 |
| 31 | L1-worker | claudeopus46 | 2,320 | 963 | 3,283 | 228 | 2.5 |
| 32 | L1-worker | claudeopus46 | 627 | 843 | 1,470 | 445 | 3.7 |
| 33 | L1-worker | claudeopus46 | 366 | 869 | 1,235 | 67 | 1.9 |
| 34 | L1-worker | claudeopus46 | 787 | 2,461 | 3,248 | 598 | 4.8 |
| 35 | L0-main | claudeopus46 | 11,581 | 11,878 | 23,459 | 2,424 | 14.9 |
| 36 | L0-main | claudeopus46 | 2,320 | 2,128 | 4,448 | 548 | 3.6 |
| 37 | L0-main | claudeopus46 | 2,106 | 3,013 | 5,119 | 676 | 5.7 |
| 38 | L0-main | claudeopus46 | 366 | 1,023 | 1,389 | 509 | 4.1 |
| 39 | L0-main | claudeopus46 | 366 | 1,225 | 1,591 | 632 | 3.2 |
| 40 | verdict | claudeopus46 | 972 | 4,518 | 5,490 | 1,023 | 8.7 |

