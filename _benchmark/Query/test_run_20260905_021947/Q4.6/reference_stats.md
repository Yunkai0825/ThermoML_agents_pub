# Reference Stats — query-agent

**Run started:** 2026-09-05 05:52:58
**Wall time (at last flush):** 830.2 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 11 | 53,564 | 171,165 | 23,908 | 224,729 | 20,429 | 156.8 | claudeopus46 |
| L1-worker | 66 | 865,725 | 734,524 | 101,245 | 1,600,249 | 24,246 | 722.1 | claudeopus46 |
| **TOTAL** | **77** | **919,289** | **905,689** | **125,153** | **1,824,978** | **23,701** | **878.9** | |

**Estimated tokens:** ~456,244 input + ~31,288 output = ~487,532 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 5 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 4 | 1 | 4 | 4 | 76 |
| `search_blocks` | 2 | 1 | 5 | 3 | 10 | 10 | 345 |
| `search_blocks` | 2 | 1 | 4 | 3 | 4 | 4 | 51 |
| `search_blocks` | 2 | 1 | 3 | 2 | 2 | 2 | 25 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 5 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 3 | 1 | 3 | 3 | 171 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 76 |
| `search_blocks` | 2 | 1 | 3 | 2 | 7 | 7 | 302 |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 56 |
| `search_blocks` | 2 | 1 | 3 | 2 | 5 | 5 | 193 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **29** | **9** | **29** | **16** | **37** | **37** | **1,295** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (11 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_4 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_2 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_5 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_6 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_31 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_9 |  | resolve_compound_ids |
| GLOBcomp_58 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_24 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_133 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_18 |  | resolve_compound_ids, search_blocks |

#### References (30 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_2825 |  | search_blocks |
| GLOBlit_5533 |  | search_blocks |
| GLOBlit_8869 |  | search_blocks |
| GLOBlit_9571 |  | search_blocks |
| GLOBlit_5201 |  | search_blocks |
| GLOBlit_7178 |  | search_blocks |
| GLOBlit_7448 |  | search_blocks |
| GLOBlit_7676 |  | search_blocks |
| GLOBlit_8949 |  | search_blocks |
| GLOBlit_10159 |  | search_blocks |
| GLOBlit_10699 |  | search_blocks |
| GLOBlit_11005 |  | search_blocks |
| GLOBlit_11136 |  | search_blocks |
| GLOBlit_5585 |  | search_blocks |
| GLOBlit_11042 |  | search_blocks |
| GLOBlit_2781 |  | search_blocks |
| GLOBlit_5953 |  | search_blocks |
| GLOBlit_11517 |  | search_blocks |
| GLOBlit_2656 |  | search_blocks |
| GLOBlit_6951 |  | search_blocks |
| GLOBlit_8038 |  | search_blocks |
| GLOBlit_8106 |  | search_blocks |
| GLOBlit_11186 |  | search_blocks |
| GLOBlit_11506 |  | search_blocks |
| GLOBlit_10965 |  | search_blocks |
| GLOBlit_8676 |  | search_blocks |
| GLOBlit_9342 |  | search_blocks |
| GLOBlit_9900 |  | search_blocks |
| GLOBlit_11030 |  | search_blocks |
| GLOBlit_11207 |  | search_blocks |

#### Properties (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_4 | Viscosity, Pa*s | search_blocks |

#### Measurements (10 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_140 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_8 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_271 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_11 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_4 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_205 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_988 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_165 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_227 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_142 | Viscosity, Pa*s | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks |

#### Variables (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_2 | Mole fraction | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |
| GLOBvar_18 | Volume fraction | search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |

#### Constraints (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | search_blocks |
| GLOBconstr_8 | Molality, mol/kg | search_blocks |
| GLOBconstr_2 | Temperature, K | search_blocks |

#### Solvents (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | search_blocks |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 11 |
| Unique References | 30 |
| Unique Properties | 1 |
| Unique Measurements | 10 |
| Unique Phases | 1 |
| Unique Variables | 5 |
| Unique Constraints | 3 |
| Unique Solvents | 1 |
| Total DOIs | 30 |
| Unique parent blocks | 37 |
| Explicit block/subsystem targets | 37 |
| Subsystem targets | 0 |
| Target-matched data points | 1,295 |

---

## 3. DOI & Block References

**Unique DOIs:** 30  |  **Parent blocks:** 37  |  **Explicit targets:** 37  |  **Subsystems:** 0  |  **Target-matched datapoints:** 1,295

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.jct.2006.01.011 | 1 | 10 | binary | search_blocks |
| 10.1016/j.jct.2006.12.012 | 1 | 120 | binary | search_blocks |
| 10.1016/j.jct.2007.05.004 | 2 | 76 | binary | search_blocks |
| 10.1016/j.jct.2018.02.022 | 3 | 260 | binary | search_blocks |
| 10.1016/j.jct.2019.05.013 | 1 | 12 | binary | search_blocks |
| 10.1016/j.jct.2019.105880 | 2 | 28 | binary | search_blocks |
| 10.1016/j.tca.2011.08.013 | 1 | 16 | binary | search_blocks |
| 10.1021/acs.jced.6b00526 | 1 | 33 | binary | search_blocks |
| 10.1021/acs.jced.7b00299 | 2 | 4 | binary | search_blocks |
| 10.1021/acs.jced.8b00086 | 1 | 6 | binary | search_blocks |
| 10.1021/acs.jced.8b00939 | 1 | 9 | binary | search_blocks |
| 10.1021/je020140j | 1 | 77 | binary | search_blocks |
| 10.1021/je025610o | 1 | 30 | binary | search_blocks |
| 10.1021/je050209y | 1 | 11 | binary | search_blocks |
| 10.1021/je0600810 | 1 | 9 | binary | search_blocks |
| 10.1021/je060219e | 1 | 26 | binary | search_blocks |
| 10.1021/je1008813 | 1 | 16 | binary | search_blocks |
| 10.1021/je2003622 | 1 | 16 | binary | search_blocks |
| 10.1021/je300608v | 1 | 60 | binary | search_blocks |
| 10.1021/je4003515 | 2 | 45 | binary | search_blocks |
| 10.1021/je600565m | 1 | 17 | binary | search_blocks |
| 10.1021/je700517f | 1 | 56 | binary | search_blocks |
| 10.1021/je700618y | 1 | 15 | binary | search_blocks |
| 10.1021/je700671t | 1 | 98 | binary | search_blocks |
| 10.1021/je700700f | 2 | 26 | binary | search_blocks |
| 10.1021/je800150h | 1 | 108 | binary | search_blocks |
| 10.1021/je800271e | 1 | 52 | binary | search_blocks |
| 10.1021/je800330d | 1 | 8 | binary | search_blocks |
| 10.1021/je9000697 | 1 | 16 | binary | search_blocks |
| 10.1021/je9001027 | 1 | 35 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.jct.2006.01.011 | PROPblock_13 | declared | 10 | binary | — | search_blocks |
| 10.1016/j.jct.2006.12.012 | PROPblock_3 | declared | 120 | binary | — | search_blocks |
| 10.1016/j.jct.2007.05.004 | PROPblock_11 | declared | 37 | binary | — | search_blocks |
| 10.1016/j.jct.2007.05.004 | PROPblock_9 | declared | 39 | binary | — | search_blocks |
| 10.1016/j.jct.2018.02.022 | PROPblock_21 | declared | 100 | binary | — | search_blocks |
| 10.1016/j.jct.2018.02.022 | PROPblock_24 | declared | 84 | binary | — | search_blocks |
| 10.1016/j.jct.2018.02.022 | PROPblock_33 | declared | 76 | binary | — | search_blocks |
| 10.1016/j.jct.2019.05.013 | PROPblock_3 | declared | 12 | binary | — | search_blocks |
| 10.1016/j.jct.2019.105880 | PROPblock_12 | declared | 12 | binary | — | search_blocks |
| 10.1016/j.jct.2019.105880 | PROPblock_8 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.tca.2011.08.013 | PROPblock_10 | declared | 16 | binary | — | search_blocks |
| 10.1021/acs.jced.6b00526 | PROPblock_18 | declared | 33 | binary | — | search_blocks |
| 10.1021/acs.jced.7b00299 | PROPblock_11 | declared | 2 | binary | — | search_blocks |
| 10.1021/acs.jced.7b00299 | PROPblock_14 | declared | 2 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00086 | PROPblock_47 | declared | 6 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00939 | PROPblock_18 | declared | 9 | binary | — | search_blocks |
| 10.1021/je020140j | PROPblock_5 | declared | 77 | binary | — | search_blocks |
| 10.1021/je025610o | PROPblock_5 | declared | 30 | binary | — | search_blocks |
| 10.1021/je050209y | PROPblock_9 | declared | 11 | binary | — | search_blocks |
| 10.1021/je0600810 | PROPblock_3 | declared | 9 | binary | — | search_blocks |
| 10.1021/je060219e | PROPblock_1 | declared | 26 | binary | — | search_blocks |
| 10.1021/je1008813 | PROPblock_3 | declared | 16 | binary | — | search_blocks |
| 10.1021/je2003622 | PROPblock_1 | declared | 16 | binary | — | search_blocks |
| 10.1021/je300608v | PROPblock_3 | declared | 60 | binary | — | search_blocks |
| 10.1021/je4003515 | PROPblock_11 | declared | 20 | binary | — | search_blocks |
| 10.1021/je4003515 | PROPblock_8 | declared | 25 | binary | — | search_blocks |
| 10.1021/je600565m | PROPblock_5 | declared | 17 | binary | — | search_blocks |
| 10.1021/je700517f | PROPblock_7 | declared | 56 | binary | — | search_blocks |
| 10.1021/je700618y | PROPblock_7 | declared | 15 | binary | — | search_blocks |
| 10.1021/je700671t | PROPblock_3 | declared | 98 | binary | — | search_blocks |
| 10.1021/je700700f | PROPblock_12 | declared | 13 | binary | — | search_blocks |
| 10.1021/je700700f | PROPblock_15 | declared | 13 | binary | — | search_blocks |
| 10.1021/je800150h | PROPblock_8 | declared | 108 | binary | — | search_blocks |
| 10.1021/je800271e | PROPblock_4 | declared | 52 | binary | — | search_blocks |
| 10.1021/je800330d | PROPblock_3 | declared | 8 | binary | — | search_blocks |
| 10.1021/je9000697 | PROPblock_1 | declared | 16 | binary | — | search_blocks |
| 10.1021/je9001027 | PROPblock_3 | declared | 35 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Resolve compound ID… | 346 | KEEP ←in 475 | 346 | 4.5 |
| 2 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_4'], limit=10, p… | 1,239 | KEEP ←in 8,146 | 1224 | 19.3 |
| 3 | 6 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=10, p… | 1,208 | KEEP ←in 6,290 | 1177 | 19.6 |
| 4 | 7 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_5'], limit=10, p… | 1,091 | KEEP ←in 7,421 | 1091 | 15.7 |
| 5 | 8 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_6'], limit=10, p… | 1,108 | KEEP ←in 3,909 | 1092 | 22.9 |
| 6 | 9 | `inspect_block_table` | block_number=PROPblock_9, literature=GLOBlit_2825,… | 348 | — | — | 0.1 |
| 7 | 10 | `inspect_block_table` | block_number=PROPblock_9, literature=GLOBlit_2825,… | 1,507 | — | — | 0.1 |
| 8 | 11 | `inspect_block_table` | block_number=PROPblock_11, literature=GLOBlit_2825… | 1,414 | — | — | 1.0 |
| 9 | 12 | `inspect_block_table` | block_number=PROPblock_12, literature=GLOBlit_1104… | 1,392 | — | — | 0.1 |
| 10 | 1 | `L1_query` | context=User wants to understand how …, id_catalog… | 41,797 | — | — | 259.3 |
| 11 | 1 | `inspect_block_table` | block_number=PROPblock_15, literature=GLOBlit_1104… | 1,331 | — | — | 0.1 |
| 12 | 4 | `inspect_block_table` | block_number=PROPblock_12, literature=GLOBlit_1104… | 1,382 | — | — | 0.2 |
| 13 | 2 | `L1_query` | context=PROPblock_15 was identified b…, id_catalog… | 21,173 | — | — | 98.3 |
| 14 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve compound ID… | 705 | KEEP ←in 514 | 705 | 8.7 |
| 15 | 3 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve DMF compoun… | 220 | KEEP ←in 239 | 220 | 4.9 |
| 16 | 5 | `search_blocks` | compound=['GLOBcomp_31', 'GLOBcomp_1'], limit=10, … | 820 | KEEP ←in 7,090 | 820 | 15.3 |
| 17 | 7 | `search_blocks` | compound=['GLOBcomp_9', 'GLOBcomp_1'], limit=10, p… | 1,078 | DISCARD ←in 39 | 1020 | 18.0 |
| 18 | 8 | `search_blocks` | compound=['GLOBcomp_58', 'GLOBcomp_1'], limit=10, … | 1,150 | KEEP ←in 2,330 | 1135 | 12.8 |
| 19 | 9 | `search_blocks` | compound=['GLOBcomp_24', 'GLOBcomp_1'], limit=10, … | 1,267 | KEEP ←in 9,915 | 1237 | 15.1 |
| 20 | 10 | `search_blocks` | compound=['GLOBcomp_133', 'GLOBcomp_1'], limit=10,… | 1,121 | KEEP ←in 2,328 | 1105 | 13.5 |
| 21 | 11 | `search_blocks` | compound=['GLOBcomp_18', 'GLOBcomp_1'], limit=10, … | 642 | KEEP ←in 7,112 | 642 | 14.2 |
| 22 | 12 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_2781,… | 367 | — | — | 0.1 |
| 23 | 3 | `L1_query` | context=Already have alcohol-water vi…, id_catalog… | 305 | — | — | 328.5 |
| | | **TOTAL (23 tools)** | | **83,011** | | **11,814** | **872.3** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 644 | 12,225 | 2,146 | 15.7 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,301 | 25,396 | 919 | 6.2 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,386 | 26,481 | 699 | 4.3 |
| 4 | L1-worker | claudeopus46 | 3,767 | 679 | 4,446 | 490 | 4.4 |
| 5 | L1-worker | claudeopus46 | 24,095 | 2,131 | 26,226 | 1,080 | 7.7 |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,944 | 27,039 | 764 | 5.2 |
| 7 | L1-worker | claudeopus46 | 3,767 | 8,602 | 12,369 | 1,588 | 14.2 |
| 8 | L1-worker | claudeopus46 | 24,095 | 4,170 | 28,265 | 802 | 6.8 |
| 9 | L1-worker | claudeopus46 | 24,095 | 4,932 | 29,027 | 644 | 4.9 |
| 10 | L1-worker | claudeopus46 | 3,767 | 6,734 | 10,501 | 1,593 | 13.7 |
| 11 | L1-worker | claudeopus46 | 24,095 | 6,136 | 30,231 | 696 | 5.3 |
| 12 | L1-worker | claudeopus46 | 3,767 | 7,864 | 11,631 | 1,750 | 15.2 |
| 13 | L1-worker | claudeopus46 | 24,095 | 7,562 | 31,657 | 751 | 6.7 |
| 14 | L1-worker | claudeopus46 | 3,767 | 4,369 | 8,136 | 1,533 | 16.1 |
| 15 | L1-worker | claudeopus46 | 24,095 | 9,012 | 33,107 | 1,435 | 12.2 |
| 16 | L1-worker | claudeopus46 | 24,095 | 9,824 | 33,919 | 662 | 6.2 |
| 17 | L1-worker | claudeopus46 | 24,095 | 11,714 | 35,809 | 1,026 | 7.8 |
| 18 | L1-worker | claudeopus46 | 24,095 | 13,551 | 37,646 | 714 | 6.1 |
| 19 | L1-worker | claudeopus46 | 24,062 | 15,037 | 39,099 | 5,361 | 33.3 |
| 20 | L1-worker | claudeopus46 | 24,062 | 18,272 | 42,334 | 5,047 | 32.7 |
| 21 | L1-worker | claudeopus46 | 2,320 | 6,315 | 8,635 | 971 | 6.8 |
| 22 | L1-worker | claudeopus46 | 366 | 1,408 | 1,774 | 931 | 4.1 |
| 23 | L1-worker | claudeopus46 | 627 | 6,195 | 6,822 | 1,430 | 11.5 |
| 24 | L1-worker | claudeopus46 | 2,106 | 7,737 | 9,843 | 2,854 | 12.3 |
| 25 | L1-worker | claudeopus46 | 366 | 3,631 | 3,997 | 1,731 | 7.0 |
| 26 | L1-worker | claudeopus46 | 787 | 38,924 | 39,711 | 746 | 7.4 |
| 27 | L0-main | claudeopus46 | 11,581 | 31,371 | 42,952 | 1,727 | 14.6 |
| 28 | L1-worker | claudeopus46 | 24,095 | 12,433 | 36,528 | 645 | 5.0 |
| 29 | L1-worker | claudeopus46 | 24,095 | 14,026 | 38,121 | 2,181 | 19.0 |
| 30 | L1-worker | claudeopus46 | 24,095 | 19,505 | 43,600 | 2,658 | 21.6 |
| 31 | L1-worker | claudeopus46 | 24,095 | 25,399 | 49,494 | 797 | 7.3 |
| 32 | L1-worker | claudeopus46 | 24,095 | 27,081 | 51,176 | 2,105 | 18.4 |
| 33 | L1-worker | claudeopus46 | 627 | 2,619 | 3,246 | 780 | 5.9 |
| 34 | L1-worker | claudeopus46 | 2,320 | 2,739 | 5,059 | 882 | 6.2 |
| 35 | L1-worker | claudeopus46 | 2,106 | 4,140 | 6,246 | 1,233 | 7.2 |
| 36 | L1-worker | claudeopus46 | 366 | 1,191 | 1,557 | 768 | 3.7 |
| 37 | L1-worker | claudeopus46 | 366 | 1,319 | 1,685 | 847 | 3.9 |
| 38 | L1-worker | claudeopus46 | 366 | 2,010 | 2,376 | 760 | 5.0 |
| 39 | L1-worker | claudeopus46 | 1,228 | 5,481 | 6,709 | 760 | 4.6 |
| 40 | L1-worker | claudeopus46 | 787 | 18,324 | 19,111 | 748 | 7.1 |
| 41 | L0-main | claudeopus46 | 11,581 | 47,279 | 58,860 | 2,296 | 17.5 |
| 42 | L1-worker | claudeopus46 | 24,095 | 18,800 | 42,895 | 811 | 6.2 |
| 43 | L1-worker | claudeopus46 | 24,095 | 19,990 | 44,085 | 769 | 4.9 |
| 44 | L1-worker | claudeopus46 | 3,767 | 770 | 4,537 | 1,050 | 8.5 |
| 45 | L1-worker | claudeopus46 | 24,095 | 19,989 | 44,084 | 591 | 5.1 |
| 46 | L1-worker | claudeopus46 | 3,767 | 376 | 4,143 | 366 | 4.1 |
| 47 | L1-worker | claudeopus46 | 24,095 | 20,534 | 44,629 | 2,334 | 16.0 |
| 48 | L1-worker | claudeopus46 | 24,095 | 21,355 | 45,450 | 678 | 5.4 |
| 49 | L1-worker | claudeopus46 | 3,767 | 7,534 | 11,301 | 1,633 | 14.8 |
| 50 | L1-worker | claudeopus46 | 24,095 | 22,149 | 46,244 | 826 | 6.3 |
| 51 | L1-worker | claudeopus46 | 24,095 | 22,946 | 47,041 | 724 | 5.2 |
| 52 | L1-worker | claudeopus46 | 3,767 | 528 | 4,295 | 1,474 | 10.6 |
| 53 | L1-worker | claudeopus46 | 24,095 | 24,044 | 48,139 | 732 | 6.3 |
| 54 | L1-worker | claudeopus46 | 3,767 | 2,751 | 6,518 | 1,501 | 12.3 |
| 55 | L1-worker | claudeopus46 | 24,095 | 25,532 | 49,627 | 879 | 6.3 |
| 56 | L1-worker | claudeopus46 | 3,767 | 10,367 | 14,134 | 1,544 | 14.3 |
| 57 | L1-worker | claudeopus46 | 24,095 | 27,220 | 51,315 | 1,154 | 8.5 |
| 58 | L1-worker | claudeopus46 | 3,767 | 2,767 | 6,534 | 1,545 | 12.6 |
| 59 | L1-worker | claudeopus46 | 24,095 | 28,736 | 52,831 | 1,277 | 9.5 |
| 60 | L1-worker | claudeopus46 | 3,767 | 7,590 | 11,357 | 1,520 | 13.7 |
| 61 | L1-worker | claudeopus46 | 24,095 | 29,798 | 53,893 | 1,753 | 13.2 |
| 62 | L1-worker | claudeopus46 | 24,062 | 13,578 | 37,640 | 6,751 | 46.5 |
| 63 | L1-worker | claudeopus46 | 24,062 | 17,382 | 41,444 | 6,396 | 43.7 |
| 64 | L1-worker | claudeopus46 | 627 | 9,308 | 9,935 | 1,661 | 15.2 |
| 65 | L1-worker | claudeopus46 | 2,106 | 11,563 | 13,669 | 3,323 | 15.7 |
| 66 | L1-worker | claudeopus46 | 2,320 | 9,428 | 11,748 | 1,545 | 16.1 |
| 67 | L1-worker | claudeopus46 | 366 | 1,982 | 2,348 | 1,467 | 4.2 |
| 68 | L1-worker | claudeopus46 | 366 | 4,100 | 4,466 | 2,773 | 11.9 |
| 69 | L1-worker | claudeopus46 | 1,228 | 15,710 | 16,938 | 2,787 | 12.0 |
| 70 | L0-main | claudeopus46 | 11,581 | 48,156 | 59,737 | 8,393 | 54.4 |
| 71 | L0-main | claudeopus46 | 2,106 | 8,391 | 10,497 | 1,132 | 8.9 |
| 72 | L0-main | claudeopus46 | 2,320 | 7,915 | 10,235 | 1,510 | 10.1 |
| 73 | L0-main | claudeopus46 | 366 | 1,681 | 2,047 | 1,444 | 6.1 |
| 74 | L0-main | claudeopus46 | 366 | 1,985 | 2,351 | 1,461 | 5.5 |
| 75 | L0-main | claudeopus46 | 560 | 9,209 | 9,769 | 232 | 3.4 |
| 76 | L0-main | claudeopus46 | 1,156 | 12,029 | 13,185 | 1,812 | 13.7 |
| 77 | L0-main | claudeopus46 | 366 | 2,505 | 2,871 | 1,755 | 6.9 |

