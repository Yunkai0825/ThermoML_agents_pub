# Reference Stats — analysis-agent

**Run started:** 2026-09-05 02:33:37
**Wall time (at last flush):** 507.7 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 28 | 459,518 | 1,159,744 | 42,103 | 1,619,262 | 57,830 | 327.1 | claudeopus46 |
| L1-worker | 39 | 541,708 | 216,963 | 39,227 | 758,671 | 19,453 | 296.9 | claudeopus46 |
| **TOTAL** | **67** | **1,001,226** | **1,376,707** | **81,330** | **2,377,933** | **35,491** | **624.0** | |

**Estimated tokens:** ~594,483 input + ~20,332 output = ~614,815 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 3 | 0 | 1 | 1 | 206 |
| `search_blocks` | 2 | 1 | 6 | 2 | 9 | 9 | 1,349 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 6 | 2 | 9 | 9 | 1,349 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml_parallel` | 2 | 2 | 5 | 1 | 5 | 5 | 0 |
| `list_session_files` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **8** | **5** | **20** | **5** | **24** | **24** | **2,904** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### References (10 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_2395 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_2432 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_2825 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_7085 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_8254 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_8424 |  | search_blocks |
| GLOBlit_8869 |  | search_blocks |
| GLOBlit_8888 |  | search_blocks |
| GLOBlit_9571 |  | search_blocks |
| GLOBlit_10866 |  | search_blocks |

#### Compounds (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_4 | methanol | query_thermoml_parallel, search_blocks |
| GLOBcomp_1 | water | query_thermoml_parallel, search_blocks |

#### Properties (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_28 | Excess molar volume, m3/mol | query_thermoml_parallel, search_blocks |
| GLOBprop_1 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |

#### Measurements (7 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_207 | Excess molar volume, m3/mol | query_thermoml_parallel, search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBmeas_170 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBmeas_138 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_141 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_280 | Mass density, kg/m3 | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | query_thermoml_parallel, search_blocks |

#### Variables (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | query_thermoml_parallel, search_blocks |
| GLOBvar_3 | Pressure, kPa | query_thermoml_parallel, search_blocks |
| GLOBvar_2 | Mole fraction | query_thermoml_parallel, search_blocks |
| GLOBvar_4 | Molality, mol/kg | query_thermoml_parallel, search_blocks |
| GLOBvar_5 | Mass fraction | query_thermoml_parallel, search_blocks |
| GLOBvar_18 | Volume fraction | search_blocks |

#### Solvents (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | query_thermoml_parallel, search_blocks |
| GLOBsolvent_3 |  | search_blocks |

#### Constraints (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | query_thermoml_parallel, search_blocks |
| GLOBconstr_2 | Temperature, K | search_blocks |

#### Block_Types (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | query_thermoml_parallel |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique References | 10 |
| Unique Compounds | 2 |
| Unique Properties | 2 |
| Unique Measurements | 7 |
| Unique Phases | 1 |
| Unique Variables | 6 |
| Unique Solvents | 2 |
| Unique Constraints | 2 |
| Unique Block_Types | 1 |
| Total DOIs | 10 |
| Unique parent blocks | 10 |
| Explicit block/subsystem targets | 10 |
| Subsystem targets | 0 |
| Target-matched data points | 4,158 |

---

## 3. DOI & Block References

**Unique DOIs:** 10  |  **Parent blocks:** 10  |  **Explicit targets:** 10  |  **Subsystems:** 0  |  **Target-matched datapoints:** 1,555

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.jct.2004.03.011 | 1 | 206 | binary | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2004.07.019 | 1 | 596 | binary | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2007.05.004 | 1 | 39 | binary | query_thermoml_parallel, search_blocks |
| 10.1021/acs.jced.6b01058 | 1 | 12 | binary | query_thermoml_parallel, search_blocks |
| 10.1021/je034101z | 1 | 401 | binary | query_thermoml_parallel, search_blocks |
| 10.1021/je049691v | 1 | 180 | binary | search_blocks |
| 10.1021/je0600810 | 1 | 9 | binary | search_blocks |
| 10.1021/je0601098 | 1 | 12 | binary | search_blocks |
| 10.1021/je2003622 | 1 | 16 | binary | search_blocks |
| 10.1021/je700300y | 1 | 84 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.jct.2004.03.011 | PROPblock_1 | declared | 206 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2004.07.019 | PROPblock_1 | declared | 596 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2007.05.004 | PROPblock_10 | declared | 39 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1021/acs.jced.6b01058 | PROPblock_6 | declared | 12 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1021/je034101z | PROPblock_4 | declared | 401 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1021/je049691v | PROPblock_3 | declared | 180 | binary | — | search_blocks |
| 10.1021/je0600810 | PROPblock_4 | declared | 9 | binary | — | search_blocks |
| 10.1021/je0601098 | PROPblock_18 | declared | 12 | binary | — | search_blocks |
| 10.1021/je2003622 | PROPblock_2 | declared | 16 | binary | — | search_blocks |
| 10.1021/je700300y | PROPblock_6 | declared | 84 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 1 | `query_thermoml_parallel` | queries=[{'label': 'direct_VE', 'purp… | 132 | — | — | 0.1 |
| 2 | 1 | `resolve_compound_ids` | purpose=Resolve water and methanol to…, queries=['… | 212 | KEEP ←in 277 | 212 | 4.1 |
| 3 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve global IDs … | 213 | KEEP ←in 408 | 213 | 5.2 |
| 4 | 3 | `resolve_property_ids` | limit=10, min_score=50, purpose=Resolve excess mol… | 202 | KEEP ←in 227 | 202 | 3.7 |
| 5 | 5 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_4'], limit=50, p… | 973 | KEEP ←in 3,972 | 958 | 15.2 |
| 6 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_4'], limit=50, p… | 164 | KEEP ←in 5,885 | 164 | 23.2 |
| 7 | 6 | `inspect_block_table` | block_number=GLOBlit_2395::PROPblock_1, purpose=Gr… | 375 | — | — | 0.3 |
| 8 | 7 | `inspect_block_table` | block_number=GLOBlit_2395::PROPblock_1, purpose=Gr… | 2,077 | — | — | 0.1 |
| 9 | 5 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_4'], limit=20, p… | 1,176 | KEEP ←in 5,885 | 1161 | 17.3 |
| 10 | 7 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_2432,… | 245 | — | — | 0.0 |
| 11 | 8 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_2432,… | 391 | — | — | 0.2 |
| 12 | 9 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_2432,… | 982 | — | — | 0.1 |
| 13 | 10 | `inspect_block_table` | block_number=PROPblock_10, literature=GLOBlit_2825… | 958 | — | — | 0.1 |
| 14 | 11 | `inspect_block_table` | block_number=PROPblock_6, literature=GLOBlit_7085,… | 953 | — | — | 0.2 |
| 15 | 12 | `inspect_block_table` | block_number=PROPblock_4, literature=GLOBlit_8254,… | 921 | — | — | 0.3 |
| 16 | 2 | `query_thermoml_parallel` | queries=[{'label': 'direct_VE', 'purp… | 62,286 | — | — | 180.0 |
| 17 | 7 | `fit_block_derived` | block_number=PROPblock_10, composition_hint=mole_f… | 237 | — | — | 0.1 |
| 18 | 10 | `inspect_block` | block_number=PROPblock_10, doi=10.1016/j.jct.2007.… | 1,360 | — | — | 0.3 |
| 19 | 14 | `fit_block_derived` | block_number=PROPblock_10, composition_hint=mole_f… | 954 | — | — | 1.8 |
| 20 | 16 | `predict_from_rk` | coeffs=[-3.98239e-06, -1.5386e-07, 1…, mixing_rule… | 207 | — | — | 0.1 |
| 21 | 17 | `list_session_files` |  | 1,681 | — | — | 0.0 |
| | | **TOTAL (21 tools)** | | **76,699** | | **2,910** | **252.4** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 22,518 | 717 | 23,235 | 1,731 | 11.0 |
| 2 | L0-main | claudeopus46 | 22,518 | 1,162 | 23,680 | 1,130 | 6.9 |
| 3 | L1-worker | claudeopus46 | 24,095 | 852 | 24,947 | 614 | 4.8 |
| 4 | L1-worker | claudeopus46 | 24,095 | 851 | 24,946 | 854 | 6.0 |
| 5 | L1-worker | claudeopus46 | 3,767 | 468 | 4,235 | 382 | 4.0 |
| 6 | L1-worker | claudeopus46 | 24,095 | 1,909 | 26,004 | 588 | 4.2 |
| 7 | L1-worker | claudeopus46 | 24,095 | 1,308 | 25,403 | 464 | 5.0 |
| 8 | L1-worker | claudeopus46 | 3,767 | 591 | 4,358 | 463 | 4.4 |
| 9 | L1-worker | claudeopus46 | 24,095 | 2,319 | 26,414 | 534 | 3.7 |
| 10 | L1-worker | claudeopus46 | 3,767 | 378 | 4,145 | 330 | 3.5 |
| 11 | L1-worker | claudeopus46 | 24,095 | 1,507 | 25,602 | 862 | 6.4 |
| 12 | L1-worker | claudeopus46 | 24,095 | 2,219 | 26,314 | 641 | 5.2 |
| 13 | L1-worker | claudeopus46 | 24,095 | 1,945 | 26,040 | 821 | 6.4 |
| 14 | L1-worker | claudeopus46 | 24,095 | 2,691 | 26,786 | 696 | 5.1 |
| 15 | L1-worker | claudeopus46 | 3,767 | 4,455 | 8,222 | 1,398 | 13.7 |
| 16 | L1-worker | claudeopus46 | 3,767 | 6,351 | 10,118 | 1,719 | 15.7 |
| 17 | L1-worker | claudeopus46 | 24,095 | 3,649 | 27,744 | 960 | 7.6 |
| 18 | L1-worker | claudeopus46 | 24,095 | 2,358 | 26,453 | 805 | 5.5 |
| 19 | L1-worker | claudeopus46 | 24,095 | 4,460 | 28,555 | 572 | 5.0 |
| 20 | L1-worker | claudeopus46 | 3,767 | 6,356 | 10,123 | 1,628 | 16.6 |
| 21 | L1-worker | claudeopus46 | 24,095 | 6,831 | 30,926 | 2,533 | 20.0 |
| 22 | L1-worker | claudeopus46 | 2,106 | 3,637 | 5,743 | 594 | 4.6 |
| 23 | L1-worker | claudeopus46 | 2,320 | 2,664 | 4,984 | 896 | 5.3 |
| 24 | L1-worker | claudeopus46 | 627 | 2,544 | 3,171 | 952 | 7.2 |
| 25 | L1-worker | claudeopus46 | 366 | 1,371 | 1,737 | 328 | 2.9 |
| 26 | L1-worker | claudeopus46 | 366 | 1,333 | 1,699 | 851 | 3.6 |
| 27 | L1-worker | claudeopus46 | 24,095 | 3,900 | 27,995 | 3,099 | 18.9 |
| 28 | L1-worker | claudeopus46 | 787 | 12,956 | 13,743 | 577 | 6.1 |
| 29 | L1-worker | claudeopus46 | 24,095 | 9,872 | 33,967 | 590 | 5.8 |
| 30 | L1-worker | claudeopus46 | 24,095 | 10,396 | 34,491 | 514 | 5.0 |
| 31 | L1-worker | claudeopus46 | 24,095 | 11,059 | 35,154 | 632 | 5.1 |
| 32 | L1-worker | claudeopus46 | 24,095 | 12,343 | 36,438 | 620 | 6.1 |
| 33 | L1-worker | claudeopus46 | 24,095 | 13,650 | 37,745 | 635 | 5.5 |
| 34 | L1-worker | claudeopus46 | 24,095 | 14,892 | 38,987 | 591 | 5.2 |
| 35 | L1-worker | claudeopus46 | 24,062 | 15,775 | 39,837 | 3,214 | 25.1 |
| 36 | L1-worker | claudeopus46 | 2,320 | 3,345 | 5,665 | 1,133 | 6.8 |
| 37 | L1-worker | claudeopus46 | 627 | 3,225 | 3,852 | 1,204 | 9.7 |
| 38 | L1-worker | claudeopus46 | 366 | 1,570 | 1,936 | 1,083 | 4.5 |
| 39 | L1-worker | claudeopus46 | 2,106 | 4,317 | 6,423 | 2,640 | 12.5 |
| 40 | L1-worker | claudeopus46 | 366 | 3,417 | 3,783 | 1,644 | 7.7 |
| 41 | L1-worker | claudeopus46 | 787 | 33,199 | 33,986 | 566 | 6.5 |
| 42 | L0-main | claudeopus46 | 22,518 | 54,843 | 77,361 | 2,675 | 21.5 |
| 43 | L0-main | claudeopus46 | 22,518 | 56,100 | 78,618 | 1,190 | 9.2 |
| 44 | L0-main | claudeopus46 | 22,518 | 56,891 | 79,409 | 781 | 4.5 |
| 45 | L0-main | claudeopus46 | 22,518 | 57,637 | 80,155 | 866 | 4.4 |
| 46 | L0-main | claudeopus46 | 22,518 | 58,431 | 80,949 | 769 | 5.8 |
| 47 | L0-main | claudeopus46 | 22,518 | 57,090 | 79,608 | 872 | 6.6 |
| 48 | L0-main | claudeopus46 | 22,518 | 57,898 | 80,416 | 647 | 4.8 |
| 49 | L0-main | claudeopus46 | 22,518 | 58,609 | 81,127 | 532 | 4.9 |
| 50 | L0-main | claudeopus46 | 22,518 | 60,145 | 82,663 | 1,224 | 9.0 |
| 51 | L0-main | claudeopus46 | 22,518 | 60,939 | 83,457 | 860 | 7.1 |
| 52 | L0-main | claudeopus46 | 22,518 | 61,646 | 84,164 | 876 | 5.6 |
| 53 | L0-main | claudeopus46 | 22,518 | 62,405 | 84,923 | 849 | 5.8 |
| 54 | L0-main | claudeopus46 | 22,518 | 64,243 | 86,761 | 1,791 | 15.1 |
| 55 | L0-main | claudeopus46 | 22,518 | 65,182 | 87,700 | 831 | 6.4 |
| 56 | L0-main | claudeopus46 | 22,518 | 65,342 | 87,860 | 4,834 | 35.6 |
| 57 | L0-main | claudeopus46 | 22,518 | 67,418 | 89,936 | 3,760 | 31.5 |
| 58 | L0-main | claudeopus46 | 22,518 | 75,398 | 97,916 | 4,954 | 40.5 |
| 59 | L0-main | claudeopus46 | 22,518 | 83,818 | 106,336 | 4,499 | 38.7 |
| 60 | L0-main | claudeopus46 | 2,106 | 5,643 | 7,749 | 274 | 3.0 |
| 61 | L0-main | claudeopus46 | 366 | 797 | 1,163 | 260 | 2.4 |
| 62 | L0-main | claudeopus46 | 2,320 | 4,827 | 7,147 | 1,251 | 11.3 |
| 63 | L0-main | claudeopus46 | 366 | 1,688 | 2,054 | 1,206 | 5.5 |
| 64 | L0-main | claudeopus46 | 560 | 5,634 | 6,194 | 186 | 2.9 |
| 65 | L0-main | claudeopus46 | 1,156 | 7,103 | 8,259 | 1,059 | 10.1 |
| 66 | L0-main | claudeopus46 | 366 | 1,752 | 2,118 | 1,024 | 5.0 |
| 67 | L0-main | claudeopus46 | 1,918 | 6,386 | 8,304 | 1,172 | 12.0 |

