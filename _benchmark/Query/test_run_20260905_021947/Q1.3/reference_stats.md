# Reference Stats — query-agent

**Run started:** 2026-09-05 05:21:40
**Wall time (at last flush):** 166.0 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 8 | 30,036 | 23,857 | 6,371 | 53,893 | 6,736 | 45.2 | claudeopus46 |
| L1-worker | 17 | 210,633 | 67,320 | 16,500 | 277,953 | 16,350 | 136.1 | claudeopus46 |
| **TOTAL** | **25** | **240,669** | **91,177** | **22,871** | **331,846** | **13,273** | **181.3** | |

**Estimated tokens:** ~82,961 input + ~5,717 output = ~88,678 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 5 | 2 | 10 | 10 | 898 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **4** | **1** | **5** | **2** | **10** | **10** | **898** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_6 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks |

#### References (10 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_2432 |  | search_blocks |
| GLOBlit_5585 |  | search_blocks |
| GLOBlit_6822 |  | search_blocks |
| GLOBlit_7474 |  | search_blocks |
| GLOBlit_8447 |  | search_blocks |
| GLOBlit_9722 |  | search_blocks |
| GLOBlit_11042 |  | search_blocks |
| GLOBlit_11130 |  | search_blocks |
| GLOBlit_11142 |  | search_blocks |
| GLOBlit_11872 |  | search_blocks |

#### Properties (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_1 | Mass density, kg/m3 | search_blocks |

#### Measurements (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks |

#### Solvents (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | search_blocks |

#### Variables (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_3 | Pressure, kPa | search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |
| GLOBvar_2 | Mole fraction | search_blocks |

#### Constraints (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | search_blocks |
| GLOBconstr_2 | Temperature, K | search_blocks |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 2 |
| Unique References | 10 |
| Unique Properties | 1 |
| Unique Measurements | 2 |
| Unique Phases | 1 |
| Unique Solvents | 1 |
| Unique Variables | 5 |
| Unique Constraints | 2 |
| Total DOIs | 10 |
| Unique parent blocks | 10 |
| Explicit block/subsystem targets | 10 |
| Subsystem targets | 0 |
| Target-matched data points | 898 |

---

## 3. DOI & Block References

**Unique DOIs:** 10  |  **Parent blocks:** 10  |  **Explicit targets:** 10  |  **Subsystems:** 0  |  **Target-matched datapoints:** 898

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.jct.2004.07.019 | 1 | 529 | binary | search_blocks |
| 10.1016/j.jct.2019.105880 | 1 | 12 | binary | search_blocks |
| 10.1021/acs.jced.6b00019 | 1 | 6 | binary | search_blocks |
| 10.1021/acs.jced.8b00160 | 1 | 18 | binary | search_blocks |
| 10.1021/je049738c | 1 | 8 | binary | search_blocks |
| 10.1021/je201010s | 1 | 17 | binary | search_blocks |
| 10.1021/je700700f | 1 | 13 | binary | search_blocks |
| 10.1021/je8001305 | 1 | 209 | binary | search_blocks |
| 10.1021/je800158z | 1 | 56 | binary | search_blocks |
| 10.1021/je900966r | 1 | 30 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.jct.2004.07.019 | PROPblock_4 | declared | 529 | binary | — | search_blocks |
| 10.1016/j.jct.2019.105880 | PROPblock_10 | declared | 12 | binary | — | search_blocks |
| 10.1021/acs.jced.6b00019 | PROPblock_13 | declared | 6 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00160 | PROPblock_15 | declared | 18 | binary | — | search_blocks |
| 10.1021/je049738c | PROPblock_28 | declared | 8 | binary | — | search_blocks |
| 10.1021/je201010s | PROPblock_8 | declared | 17 | binary | — | search_blocks |
| 10.1021/je700700f | PROPblock_17 | declared | 13 | binary | — | search_blocks |
| 10.1021/je8001305 | PROPblock_1 | declared | 209 | binary | — | search_blocks |
| 10.1021/je800158z | PROPblock_4 | declared | 56 | binary | — | search_blocks |
| 10.1021/je900966r | PROPblock_6 | declared | 30 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve compound ID… | 183 | KEEP ←in 285 | 183 | 4.0 |
| 2 | 4 | `search_blocks` | compound=['GLOBcomp_6', 'GLOBcomp_1'], limit=20, p… | 2,159 | KEEP ←in 6,532 | 2159 | 38.4 |
| 3 | 5 | `inspect_block_table` | block_number=PROPblock_17, literature=GLOBlit_1104… | 259 | — | — | 0.1 |
| 4 | 6 | `inspect_block_table` | block_number=PROPblock_17, literature=GLOBlit_1104… | 369 | — | — | 0.1 |
| 5 | 7 | `inspect_block_table` | block_number=PROPblock_17, literature=GLOBlit_1104… | 1,069 | — | — | 0.1 |
| 6 | 1 | `L1_query` | instruction=Search for mass density (GLOB…, purpos… | 10,398 | — | — | 127.7 |
| | | **TOTAL (6 tools)** | | **14,437** | | **2,342** | **170.4** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 580 | 12,161 | 1,285 | 9.6 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,185 | 25,280 | 698 | 5.8 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,249 | 26,344 | 548 | 3.9 |
| 4 | L1-worker | claudeopus46 | 3,767 | 460 | 4,227 | 349 | 3.9 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,797 | 25,892 | 1,197 | 8.2 |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,555 | 26,650 | 775 | 9.2 |
| 7 | L1-worker | claudeopus46 | 3,767 | 7,069 | 10,836 | 1,490 | 15.1 |
| 8 | L1-worker | claudeopus46 | 3,767 | 7,371 | 11,138 | 2,615 | 22.5 |
| 9 | L1-worker | claudeopus46 | 24,095 | 4,704 | 28,799 | 1,281 | 12.7 |
| 10 | L1-worker | claudeopus46 | 24,095 | 5,393 | 29,488 | 794 | 7.6 |
| 11 | L1-worker | claudeopus46 | 24,095 | 6,099 | 30,194 | 778 | 5.8 |
| 12 | L1-worker | claudeopus46 | 24,095 | 7,549 | 31,644 | 1,827 | 12.8 |
| 13 | L1-worker | claudeopus46 | 2,106 | 3,264 | 5,370 | 635 | 4.0 |
| 14 | L1-worker | claudeopus46 | 627 | 1,838 | 2,465 | 665 | 4.8 |
| 15 | L1-worker | claudeopus46 | 2,320 | 1,958 | 4,278 | 858 | 4.9 |
| 16 | L1-worker | claudeopus46 | 366 | 1,412 | 1,778 | 453 | 3.2 |
| 17 | L1-worker | claudeopus46 | 366 | 1,295 | 1,661 | 818 | 3.9 |
| 18 | L1-worker | claudeopus46 | 787 | 11,122 | 11,909 | 719 | 7.8 |
| 19 | L0-main | claudeopus46 | 11,581 | 10,913 | 22,494 | 1,793 | 12.8 |
| 20 | L0-main | claudeopus46 | 2,320 | 1,961 | 4,281 | 827 | 4.6 |
| 21 | L0-main | claudeopus46 | 2,106 | 2,373 | 4,479 | 550 | 4.9 |
| 22 | L0-main | claudeopus46 | 366 | 1,099 | 1,465 | 591 | 3.0 |
| 23 | L0-main | claudeopus46 | 366 | 1,302 | 1,668 | 783 | 3.7 |
| 24 | L0-main | claudeopus46 | 560 | 2,436 | 2,996 | 93 | 2.4 |
| 25 | L0-main | claudeopus46 | 1,156 | 3,193 | 4,349 | 449 | 4.2 |

