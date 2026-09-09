# Reference Stats — query-agent

**Run started:** 2026-09-05 05:26:04
**Wall time (at last flush):** 589.3 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 10 | 41,983 | 109,020 | 22,248 | 151,003 | 15,100 | 132.1 | claudeopus46 |
| L1-worker | 47 | 603,126 | 414,605 | 70,967 | 1,017,731 | 21,653 | 488.7 | claudeopus46 |
| **TOTAL** | **57** | **645,109** | **523,625** | **93,215** | **1,168,734** | **20,504** | **620.8** | |

**Estimated tokens:** ~292,183 input + ~23,303 output = ~315,486 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 2 | 3 | 2 | 2 | 2 | 4 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 8 | 2 | 2 | 5 | 9 | 449 |
| `search_blocks` | 2 | 8 | 2 | 2 | 5 | 9 | 449 |
| `search_blocks` | 2 | 1 | 2 | 0 | 1 | 1 | 77 |
| `search_blocks` | 2 | 1 | 1 | 2 | 1 | 1 | 9 |
| `search_blocks` | 2 | 8 | 2 | 2 | 5 | 9 | 449 |
| `search_blocks` | 2 | 2 | 2 | 0 | 1 | 2 | 206 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **18** | **30** | **14** | **10** | **20** | **33** | **1,643** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (4 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_14 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_8 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_12 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_2 |  | resolve_compound_ids, search_blocks |

#### References (7 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_6057 |  | search_blocks |
| GLOBlit_6268 |  | search_blocks |
| GLOBlit_294 |  | search_blocks |
| GLOBlit_2800 |  | search_blocks |
| GLOBlit_8445 |  | search_blocks |
| GLOBlit_10821 |  | search_blocks |
| GLOBlit_11449 |  | search_blocks |

#### Properties (9 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_17 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBprop_15 | Molar enthalpy of solution, kJ/mol | search_blocks |
| GLOBprop_28 | Excess molar volume, m3/mol | search_blocks |
| GLOBprop_7 | Refractive index (Na D-line) | search_blocks |
| GLOBprop_8 | Speed of sound, m/s | search_blocks |
| GLOBprop_1 | Mass density, kg/m3 | search_blocks |
| GLOBprop_29 | Binary diffusion coefficient, m2/s | search_blocks |
| GLOBprop_13 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBprop_4 | Viscosity, Pa*s | search_blocks |

#### Measurements (11 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_13 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_25 | Molar enthalpy of solution, kJ/mol | search_blocks |
| GLOBmeas_12 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_29 | Excess molar volume, m3/mol | search_blocks |
| GLOBmeas_3 | Refractive index (Na D-line) | search_blocks |
| GLOBmeas_7 | Speed of sound, m/s | search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_38 | Binary diffusion coefficient, m2/s | search_blocks |
| GLOBmeas_342 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBmeas_284 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_147 | Mass density, kg/m3 | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks |

#### Variables (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_2 | Mole fraction | search_blocks |
| GLOBvar_3 | Pressure, kPa | search_blocks |
| GLOBvar_1 | Temperature, K | search_blocks |

#### Constraints (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_2 | Temperature, K | search_blocks |
| GLOBconstr_1 | Pressure, kPa | search_blocks |

#### Solvents (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_13 |  | search_blocks |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 4 |
| Unique References | 7 |
| Unique Properties | 9 |
| Unique Measurements | 11 |
| Unique Phases | 1 |
| Unique Variables | 3 |
| Unique Constraints | 2 |
| Unique Solvents | 1 |
| Total DOIs | 7 |
| Unique parent blocks | 11 |
| Explicit block/subsystem targets | 11 |
| Subsystem targets | 0 |
| Target-matched data points | 1,643 |

---

## 3. DOI & Block References

**Unique DOIs:** 7  |  **Parent blocks:** 11  |  **Explicit targets:** 11  |  **Subsystems:** 0  |  **Target-matched datapoints:** 453

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2005.08.001 | 2 | 40 | binary | search_blocks |
| 10.1016/j.jct.2007.02.008 | 3 | 117 | binary | search_blocks |
| 10.1016/j.tca.2013.01.028 | 1 | 3 | binary | search_blocks |
| 10.1016/j.tca.2015.09.022 | 1 | 1 | binary | search_blocks |
| 10.1021/je0497303 | 1 | 9 | binary | search_blocks |
| 10.1021/je700215z | 1 | 77 | binary | search_blocks |
| 10.1021/je800925v | 2 | 206 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2005.08.001 | PROPblock_5 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.fluid.2005.08.001 | PROPblock_6 | declared | 23 | binary | — | search_blocks |
| 10.1016/j.jct.2007.02.008 | PROPblock_22 | declared | 39 | binary | — | search_blocks |
| 10.1016/j.jct.2007.02.008 | PROPblock_23 | declared | 39 | binary | — | search_blocks |
| 10.1016/j.jct.2007.02.008 | PROPblock_24 | declared | 39 | binary | — | search_blocks |
| 10.1016/j.tca.2013.01.028 | PROPblock_1 | declared | 3 | binary | — | search_blocks |
| 10.1016/j.tca.2015.09.022 | PROPblock_7 | declared | 1 | binary | — | search_blocks |
| 10.1021/je0497303 | PROPblock_8 | declared | 9 | binary | — | search_blocks |
| 10.1021/je700215z | PROPblock_5 | declared | 77 | binary | — | search_blocks |
| 10.1021/je800925v | PROPblock_10 | declared | 103 | binary | — | search_blocks |
| 10.1021/je800925v | PROPblock_9 | declared | 103 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Resolve benzene and… | 192 | KEEP ←in 294 | 192 | 4.8 |
| 2 | 4 | `search_blocks` | compound=['GLOBcomp_14', 'GLOBcomp_8'], limit=50, … | 1,408 | KEEP ←in 3,413 | 1408 | 15.3 |
| 3 | 5 | `inspect_block_table` | block_number=GLOBlit_6057::PROPblock_1, purpose=In… | 988 | — | — | 0.2 |
| 4 | 7 | `inspect_block_table` | block_number=GLOBlit_6268::PROPblock_7, purpose=Gr… | 644 | — | — | 0.1 |
| 5 | 1 | `L1_query` | instruction=Search for binary mixture dat…, purpos… | 18,156 | — | — | 139.0 |
| 6 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve hexane and … | 218 | KEEP ←in 287 | 218 | 4.0 |
| 7 | 4 | `search_blocks` | compound=['GLOBcomp_12', 'GLOBcomp_2'], limit=50, … | 1,388 | KEEP ←in 5,780 | 1388 | 19.1 |
| 8 | 5 | `search_blocks` | compound=['GLOBcomp_12', 'GLOBcomp_2'], limit=50, … | 1,265 | KEEP ←in 5,780 | 1265 | 23.8 |
| 9 | 6 | `search_blocks` | compound=['GLOBcomp_12', 'GLOBcomp_2'], limit=10, … | 1,038 | KEEP ←in 2,398 | 1022 | 9.7 |
| 10 | 7 | `search_blocks` | compound=['GLOBcomp_12', 'GLOBcomp_2'], literature… | 828 | KEEP ←in 1,681 | 813 | 9.0 |
| 11 | 8 | `search_blocks` | compound=['GLOBcomp_12', 'GLOBcomp_2'], limit=50, … | 1,064 | KEEP ←in 5,780 | 1030 | 16.8 |
| 12 | 9 | `search_blocks` | compound=['GLOBcomp_12', 'GLOBcomp_2'], literature… | 970 | KEEP ←in 3,843 | 970 | 10.7 |
| 13 | 10 | `inspect_block_table` | block_number=PROPblock_5, literature=GLOBlit_294, … | 1,408 | — | — | 0.1 |
| 14 | 11 | `inspect_block_table` | block_number=PROPblock_6, literature=GLOBlit_294, … | 1,347 | — | — | 0.1 |
| 15 | 12 | `inspect_block_table` | block_number=PROPblock_8, literature=GLOBlit_8445,… | 1,200 | — | — | 0.1 |
| 16 | 2 | `L1_query` | context=This is for comparing hexane+…, id_catalog… | 67,518 | — | — | 328.1 |
| | | **TOTAL (16 tools)** | | **99,632** | | **8,306** | **580.9** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 705 | 12,286 | 1,497 | 9.6 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,185 | 25,280 | 667 | 5.4 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,200 | 26,295 | 512 | 3.9 |
| 4 | L1-worker | claudeopus46 | 3,767 | 451 | 4,218 | 377 | 4.0 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,787 | 25,882 | 815 | 6.3 |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,502 | 26,597 | 598 | 5.0 |
| 7 | L1-worker | claudeopus46 | 3,767 | 3,842 | 7,609 | 1,657 | 14.4 |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,879 | 27,974 | 809 | 6.7 |
| 9 | L1-worker | claudeopus46 | 24,095 | 5,242 | 29,337 | 2,234 | 14.8 |
| 10 | L1-worker | claudeopus46 | 24,095 | 9,893 | 33,988 | 572 | 5.4 |
| 11 | L1-worker | claudeopus46 | 24,095 | 10,809 | 34,904 | 2,383 | 16.6 |
| 12 | L1-worker | claudeopus46 | 24,095 | 15,819 | 39,914 | 4,492 | 27.2 |
| 13 | L1-worker | claudeopus46 | 2,106 | 3,855 | 5,961 | 734 | 4.7 |
| 14 | L1-worker | claudeopus46 | 2,320 | 2,549 | 4,869 | 882 | 5.7 |
| 15 | L1-worker | claudeopus46 | 627 | 2,429 | 3,056 | 945 | 6.3 |
| 16 | L1-worker | claudeopus46 | 366 | 1,511 | 1,877 | 558 | 3.2 |
| 17 | L1-worker | claudeopus46 | 366 | 1,319 | 1,685 | 842 | 3.9 |
| 18 | L1-worker | claudeopus46 | 366 | 1,356 | 1,722 | 932 | 4.4 |
| 19 | L1-worker | claudeopus46 | 1,228 | 4,917 | 6,145 | 756 | 3.9 |
| 20 | L1-worker | claudeopus46 | 366 | 1,533 | 1,899 | 610 | 3.5 |
| 21 | L1-worker | claudeopus46 | 787 | 18,700 | 19,487 | 547 | 6.4 |
| 22 | L0-main | claudeopus46 | 11,581 | 15,258 | 26,839 | 1,762 | 13.6 |
| 23 | L1-worker | claudeopus46 | 24,095 | 7,491 | 31,586 | 568 | 5.3 |
| 24 | L1-worker | claudeopus46 | 24,095 | 8,536 | 32,631 | 562 | 4.0 |
| 25 | L1-worker | claudeopus46 | 3,767 | 475 | 4,242 | 400 | 3.9 |
| 26 | L1-worker | claudeopus46 | 24,095 | 8,133 | 32,228 | 803 | 6.4 |
| 27 | L1-worker | claudeopus46 | 24,095 | 8,832 | 32,927 | 631 | 4.8 |
| 28 | L1-worker | claudeopus46 | 3,767 | 6,256 | 10,023 | 1,650 | 13.1 |
| 29 | L1-worker | claudeopus46 | 24,095 | 10,177 | 34,272 | 1,545 | 10.6 |
| 30 | L1-worker | claudeopus46 | 3,767 | 6,243 | 10,010 | 1,523 | 18.5 |
| 31 | L1-worker | claudeopus46 | 24,095 | 11,906 | 36,001 | 1,449 | 14.1 |
| 32 | L1-worker | claudeopus46 | 3,767 | 2,825 | 6,592 | 1,370 | 9.6 |
| 33 | L1-worker | claudeopus46 | 24,095 | 13,296 | 37,391 | 1,841 | 11.9 |
| 34 | L1-worker | claudeopus46 | 3,767 | 2,111 | 5,878 | 1,044 | 8.7 |
| 35 | L1-worker | claudeopus46 | 24,095 | 14,470 | 38,565 | 1,974 | 13.2 |
| 36 | L1-worker | claudeopus46 | 3,767 | 6,263 | 10,030 | 1,593 | 13.6 |
| 37 | L1-worker | claudeopus46 | 24,095 | 15,936 | 40,031 | 1,727 | 12.0 |
| 38 | L1-worker | claudeopus46 | 3,767 | 4,248 | 8,015 | 1,206 | 10.2 |
| 39 | L1-worker | claudeopus46 | 24,095 | 17,229 | 41,324 | 2,547 | 16.7 |
| 40 | L1-worker | claudeopus46 | 24,095 | 19,098 | 43,193 | 722 | 6.3 |
| 41 | L1-worker | claudeopus46 | 24,095 | 20,796 | 44,891 | 2,595 | 18.0 |
| 42 | L1-worker | claudeopus46 | 24,062 | 16,326 | 40,388 | 5,561 | 34.1 |
| 43 | L1-worker | claudeopus46 | 24,062 | 24,510 | 48,572 | 5,826 | 34.2 |
| 44 | L1-worker | claudeopus46 | 2,320 | 6,441 | 8,761 | 1,618 | 9.7 |
| 45 | L1-worker | claudeopus46 | 627 | 6,321 | 6,948 | 1,751 | 13.1 |
| 46 | L1-worker | claudeopus46 | 366 | 2,055 | 2,421 | 1,563 | 5.5 |
| 47 | L1-worker | claudeopus46 | 2,106 | 8,285 | 10,391 | 3,977 | 17.5 |
| 48 | L1-worker | claudeopus46 | 366 | 4,754 | 5,120 | 2,287 | 11.1 |
| 49 | L1-worker | claudeopus46 | 787 | 65,814 | 66,601 | 712 | 10.9 |
| 50 | L0-main | claudeopus46 | 11,581 | 53,383 | 64,964 | 5,101 | 39.7 |
| 51 | L0-main | claudeopus46 | 2,320 | 4,214 | 6,534 | 1,386 | 7.7 |
| 52 | L0-main | claudeopus46 | 2,106 | 4,751 | 6,857 | 1,732 | 9.3 |
| 53 | L0-main | claudeopus46 | 366 | 1,861 | 2,227 | 1,337 | 4.7 |
| 54 | L0-main | claudeopus46 | 366 | 2,281 | 2,647 | 1,723 | 7.3 |
| 55 | L0-main | claudeopus46 | 560 | 7,533 | 8,093 | 936 | 6.2 |
| 56 | L0-main | claudeopus46 | 1,156 | 14,887 | 16,043 | 3,454 | 19.0 |
| 57 | L0-main | claudeopus46 | 366 | 4,147 | 4,513 | 3,320 | 15.0 |

