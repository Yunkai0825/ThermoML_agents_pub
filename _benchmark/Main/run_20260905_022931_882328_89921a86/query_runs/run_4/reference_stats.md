# Reference Stats — query-agent

**Run started:** 2026-09-05 02:29:42
**Wall time (at last flush):** 366.2 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 9 | 41,617 | 67,201 | 14,207 | 108,818 | 12,090 | 89.3 | claudeopus46 |
| L1-worker | 34 | 444,995 | 196,154 | 40,470 | 641,149 | 18,857 | 277.8 | claudeopus46 |
| verdict | 1 | 972 | 6,990 | 1,133 | 7,962 | 7,962 | 10.5 | claudeopus46 |
| **TOTAL** | **44** | **487,584** | **270,345** | **55,810** | **757,929** | **17,225** | **377.6** | |

**Estimated tokens:** ~189,482 input + ~13,952 output = ~203,434 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 4 | 1 | 4 | 4 | 76 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_property_ids` | 0 | 9 | 0 | 0 | 0 | 0 | 0 |
| `search_id_alignment` | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| `search_id_alignment` | 0 | 4 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **4** | **15** | **4** | **1** | **4** | **4** | **76** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_4 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks |

#### References (4 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_2825 |  | search_blocks |
| GLOBlit_5533 |  | search_blocks |
| GLOBlit_8869 |  | search_blocks |
| GLOBlit_9571 |  | search_blocks |

#### Properties (13 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_4 | Viscosity, Pa*s | resolve_property_ids, search_blocks, search_id_alignment |
| GLOBprop_40 |  | resolve_property_ids |
| GLOBprop_48 |  | resolve_property_ids |
| GLOBprop_98 |  | resolve_property_ids |
| GLOBprop_45 |  | resolve_property_ids |
| GLOBprop_107 |  | resolve_property_ids |
| GLOBprop_60 |  | resolve_property_ids |
| GLOBprop_3 |  | resolve_property_ids |
| GLOBprop_73 |  | resolve_property_ids |
| GLOBprop_17 |  | search_id_alignment |
| GLOBprop_28 |  | search_id_alignment |
| GLOBprop_85 |  | search_id_alignment |
| GLOBprop_97 |  | search_id_alignment |

#### Measurements (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_140 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_8 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_271 | Viscosity, Pa*s | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks |

#### Variables (4 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_2 | Mole fraction | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |
| GLOBvar_18 | Volume fraction | search_blocks |

#### Constraints (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | search_blocks |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 2 |
| Unique References | 4 |
| Unique Properties | 13 |
| Unique Measurements | 3 |
| Unique Phases | 1 |
| Unique Variables | 4 |
| Unique Constraints | 1 |
| Total DOIs | 4 |
| Unique parent blocks | 4 |
| Explicit block/subsystem targets | 4 |
| Subsystem targets | 0 |
| Target-matched data points | 76 |

---

## 3. DOI & Block References

**Unique DOIs:** 4  |  **Parent blocks:** 4  |  **Explicit targets:** 4  |  **Subsystems:** 0  |  **Target-matched datapoints:** 76

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.jct.2007.05.004 | 1 | 39 | binary | search_blocks |
| 10.1016/j.jct.2019.05.013 | 1 | 12 | binary | search_blocks |
| 10.1021/je0600810 | 1 | 9 | binary | search_blocks |
| 10.1021/je2003622 | 1 | 16 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.jct.2007.05.004 | PROPblock_9 | declared | 39 | binary | — | search_blocks |
| 10.1016/j.jct.2019.05.013 | PROPblock_3 | declared | 12 | binary | — | search_blocks |
| 10.1021/je0600810 | PROPblock_3 | declared | 9 | binary | — | search_blocks |
| 10.1021/je2003622 | PROPblock_1 | declared | 16 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve compound ID… | 175 | KEEP ←in 277 | 175 | 4.1 |
| 2 | 4 | `search_blocks` | compound=['GLOBcomp_4', 'GLOBcomp_1'], limit=20, p… | 1,117 | KEEP ←in 8,146 | 1102 | 22.6 |
| 3 | 5 | `inspect_block_table` | block_number=GLOBlit_2825::PROPblock_9, nearest=x(… | 270 | — | — | 0.1 |
| 4 | 6 | `inspect_block_table` | block_number=GLOBlit_2825::PROPblock_9, nearest={'… | 365 | — | — | 0.1 |
| 5 | 7 | `inspect_block_table` | block_number=GLOBlit_2825::PROPblock_9, nearest={'… | 1,269 | — | — | 0.1 |
| 6 | 1 | `L1_query` | context=Looking for dynamic viscosity…, id_catalog… | 28,868 | — | — | 164.0 |
| 7 | 2 | `resolve_property_ids` | limit=20, min_score=40, purpose=Find property IDs … | 943 | DISCARD ←in 982 | 878 | 10.2 |
| 8 | 3 | `search_id_alignment` | entity_type=property, limit=20, purpose=Find any v… | 741 | KEEP ←in 277 | 741 | 9.5 |
| 9 | 4 | `search_id_alignment` | entity_type=property, limit=20, purpose=Find any e… | 631 | KEEP ←in 627 | 631 | 6.0 |
| 10 | 5 | `search_blocks` | compound=['GLOBcomp_4', 'GLOBcomp_1'], limit=10, p… | 731 | DISCARD ←in 39 | 673 | 12.8 |
| 11 | 2 | `L1_query` | context=Already found dynamic viscosi…, id_catalog… | 3,356 | — | — | 111.9 |
| | | **TOTAL (11 tools)** | | **38,466** | | **4,200** | **341.4** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 901 | 12,482 | 1,516 | 9.4 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,347 | 25,442 | 540 | 4.6 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,354 | 26,449 | 522 | 3.7 |
| 4 | L1-worker | claudeopus46 | 3,767 | 427 | 4,194 | 305 | 4.0 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,950 | 26,045 | 924 | 8.4 |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,679 | 26,774 | 700 | 4.7 |
| 7 | L1-worker | claudeopus46 | 3,767 | 8,603 | 12,370 | 1,662 | 15.3 |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,760 | 27,855 | 1,072 | 8.9 |
| 9 | L1-worker | claudeopus46 | 24,095 | 4,402 | 28,497 | 697 | 6.1 |
| 10 | L1-worker | claudeopus46 | 24,095 | 5,099 | 29,194 | 836 | 7.0 |
| 11 | L1-worker | claudeopus46 | 24,095 | 6,686 | 30,781 | 2,291 | 18.1 |
| 12 | L1-worker | claudeopus46 | 24,095 | 11,576 | 35,671 | 4,596 | 28.3 |
| 13 | L1-worker | claudeopus46 | 24,095 | 18,362 | 42,457 | 4,005 | 24.4 |
| 14 | L1-worker | claudeopus46 | 2,320 | 2,187 | 4,507 | 825 | 5.3 |
| 15 | L1-worker | claudeopus46 | 627 | 2,067 | 2,694 | 855 | 5.3 |
| 16 | L1-worker | claudeopus46 | 2,106 | 3,655 | 5,761 | 1,811 | 8.1 |
| 17 | L1-worker | claudeopus46 | 366 | 1,262 | 1,628 | 790 | 3.5 |
| 18 | L1-worker | claudeopus46 | 366 | 2,588 | 2,954 | 1,332 | 5.5 |
| 19 | L1-worker | claudeopus46 | 787 | 29,170 | 29,957 | 640 | 7.0 |
| 20 | L0-main | claudeopus46 | 11,581 | 16,723 | 28,304 | 2,522 | 18.4 |
| 21 | L1-worker | claudeopus46 | 24,095 | 7,205 | 31,300 | 976 | 6.1 |
| 22 | L1-worker | claudeopus46 | 24,095 | 8,366 | 32,461 | 740 | 4.4 |
| 23 | L1-worker | claudeopus46 | 3,767 | 1,212 | 4,979 | 1,437 | 9.4 |
| 24 | L1-worker | claudeopus46 | 24,095 | 8,641 | 32,736 | 958 | 7.0 |
| 25 | L1-worker | claudeopus46 | 3,767 | 526 | 4,293 | 1,390 | 9.1 |
| 26 | L1-worker | claudeopus46 | 24,095 | 9,734 | 33,829 | 849 | 11.5 |
| 27 | L1-worker | claudeopus46 | 3,767 | 830 | 4,597 | 1,000 | 5.8 |
| 28 | L1-worker | claudeopus46 | 24,095 | 10,774 | 34,869 | 1,061 | 7.0 |
| 29 | L1-worker | claudeopus46 | 3,767 | 512 | 4,279 | 857 | 6.5 |
| 30 | L1-worker | claudeopus46 | 24,095 | 11,929 | 36,024 | 2,096 | 12.7 |
| 31 | L1-worker | claudeopus46 | 24,095 | 15,991 | 40,086 | 2,371 | 13.1 |
| 32 | L1-worker | claudeopus46 | 2,106 | 3,368 | 5,474 | 92 | 2.0 |
| 33 | L1-worker | claudeopus46 | 627 | 1,532 | 2,159 | 846 | 3.7 |
| 34 | L1-worker | claudeopus46 | 366 | 869 | 1,235 | 67 | 2.2 |
| 35 | L1-worker | claudeopus46 | 2,320 | 1,652 | 3,972 | 807 | 4.7 |
| 36 | L1-worker | claudeopus46 | 787 | 4,839 | 5,626 | 520 | 4.4 |
| 37 | L0-main | claudeopus46 | 11,581 | 23,918 | 35,499 | 4,399 | 27.2 |
| 38 | L0-main | claudeopus46 | 2,320 | 4,091 | 6,411 | 1,087 | 6.2 |
| 39 | L0-main | claudeopus46 | 2,106 | 4,824 | 6,930 | 997 | 6.6 |
| 40 | L0-main | claudeopus46 | 366 | 1,562 | 1,928 | 1,043 | 4.3 |
| 41 | L0-main | claudeopus46 | 366 | 1,546 | 1,912 | 967 | 4.3 |
| 42 | L0-main | claudeopus46 | 560 | 5,414 | 5,974 | 341 | 3.3 |
| 43 | L0-main | claudeopus46 | 1,156 | 8,222 | 9,378 | 1,335 | 9.6 |
| 44 | verdict | claudeopus46 | 972 | 6,990 | 7,962 | 1,133 | 10.5 |

