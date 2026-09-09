# Reference Stats — query-agent

**Run started:** 2026-09-05 05:21:34
**Wall time (at last flush):** 291.0 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 9 | 30,402 | 61,105 | 16,792 | 91,507 | 10,167 | 96.2 | claudeopus46 |
| L1-worker | 23 | 355,137 | 192,224 | 31,042 | 547,361 | 23,798 | 215.6 | claudeopus46 |
| **TOTAL** | **32** | **385,539** | **253,329** | **47,834** | **638,868** | **19,964** | **311.8** | |

**Estimated tokens:** ~159,717 input + ~11,958 output = ~171,675 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 8 | 2 | 2 | 5 | 9 | 449 |
| `search_system_registry` | 2 | 5 | 2 | 1 | 3 | 6 | 400 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **7** | **13** | **4** | **3** | **8** | **15** | **849** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_12 |  | resolve_compound_ids, search_blocks, search_system_registry |
| GLOBcomp_2 |  | resolve_compound_ids, search_blocks, search_system_registry |
| GLOBcomp_5494 |  | resolve_compound_ids |

#### References (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_294 |  | search_blocks |
| GLOBlit_2800 |  | search_blocks, search_system_registry |
| GLOBlit_8445 |  | search_blocks |
| GLOBlit_10821 |  | search_blocks, search_system_registry |
| GLOBlit_11449 |  | search_blocks, search_system_registry |

#### Properties (8 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_17 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBprop_28 | Excess molar volume, m3/mol | search_blocks |
| GLOBprop_7 | Refractive index (Na D-line) | search_blocks, search_system_registry |
| GLOBprop_8 | Speed of sound, m/s | search_blocks, search_system_registry |
| GLOBprop_1 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBprop_29 | Binary diffusion coefficient, m2/s | search_blocks |
| GLOBprop_13 | Surface tension liquid-gas, N/m | search_blocks, search_system_registry |
| GLOBprop_4 | Viscosity, Pa*s | search_blocks, search_system_registry |

#### Measurements (9 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_12 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_29 | Excess molar volume, m3/mol | search_blocks |
| GLOBmeas_3 | Refractive index (Na D-line) | search_blocks, search_system_registry |
| GLOBmeas_7 | Speed of sound, m/s | search_blocks, search_system_registry |
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_38 | Binary diffusion coefficient, m2/s | search_blocks |
| GLOBmeas_342 | Surface tension liquid-gas, N/m | search_blocks, search_system_registry |
| GLOBmeas_284 | Viscosity, Pa*s | search_blocks, search_system_registry |
| GLOBmeas_147 | Mass density, kg/m3 | search_blocks, search_system_registry |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks, search_system_registry |

#### Variables (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_2 | Mole fraction | search_blocks, search_system_registry |
| GLOBvar_1 | Temperature, K | search_blocks, search_system_registry |

#### Constraints (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_2 | Temperature, K | search_blocks |
| GLOBconstr_1 | Pressure, kPa | search_blocks, search_system_registry |

#### Block_Types (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | search_system_registry |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 3 |
| Unique References | 5 |
| Unique Properties | 8 |
| Unique Measurements | 9 |
| Unique Phases | 1 |
| Unique Variables | 2 |
| Unique Constraints | 2 |
| Unique Block_Types | 1 |
| Total DOIs | 5 |
| Unique parent blocks | 9 |
| Explicit block/subsystem targets | 9 |
| Subsystem targets | 0 |
| Target-matched data points | 849 |

---

## 3. DOI & Block References

**Unique DOIs:** 5  |  **Parent blocks:** 9  |  **Explicit targets:** 9  |  **Subsystems:** 0  |  **Target-matched datapoints:** 449

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2005.08.001 | 2 | 40 | binary | search_blocks |
| 10.1016/j.jct.2007.02.008 | 3 | 117 | binary | search_blocks, search_system_registry |
| 10.1021/je0497303 | 1 | 9 | binary | search_blocks |
| 10.1021/je700215z | 1 | 77 | binary | search_blocks, search_system_registry |
| 10.1021/je800925v | 2 | 206 | binary | search_blocks, search_system_registry |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2005.08.001 | PROPblock_5 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.fluid.2005.08.001 | PROPblock_6 | declared | 23 | binary | — | search_blocks |
| 10.1016/j.jct.2007.02.008 | PROPblock_22 | declared | 39 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2007.02.008 | PROPblock_23 | declared | 39 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2007.02.008 | PROPblock_24 | declared | 39 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je0497303 | PROPblock_8 | declared | 9 | binary | — | search_blocks |
| 10.1021/je700215z | PROPblock_5 | declared | 77 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je800925v | PROPblock_10 | declared | 103 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je800925v | PROPblock_9 | declared | 103 | binary | 2 | search_blocks, search_system_registry |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve hexane and … | 275 | KEEP ←in 360 | 275 | 5.2 |
| 2 | 4 | `search_blocks` | compound=['GLOBcomp_12', 'GLOBcomp_2'], limit=50, … | 1,032 | KEEP ←in 5,780 | 959 | 16.3 |
| 3 | 5 | `search_system_registry` | compound=['GLOBcomp_12', 'GLOBcomp_2'], limit=50, … | 1,355 | KEEP ←in 4,751 | 1355 | 14.0 |
| 4 | 6 | `inspect_block_table` | block_number=PROPblock_5, literature=GLOBlit_294, … | 252 | — | — | 0.0 |
| 5 | 7 | `inspect_block_table` | block_number=PROPblock_5, literature=GLOBlit_294, … | 420 | — | — | 0.1 |
| 6 | 8 | `inspect_block_table` | block_number=PROPblock_5, literature=GLOBlit_294, … | 1,147 | — | — | 0.2 |
| 7 | 9 | `inspect_block_table` | block_number=PROPblock_6, literature=GLOBlit_294, … | 1,077 | — | — | 0.1 |
| 8 | 10 | `inspect_block_table` | block_number=PROPblock_22, literature=GLOBlit_2800… | 1,149 | — | — | 0.2 |
| 9 | 11 | `inspect_block_table` | block_number=PROPblock_23, literature=GLOBlit_2800… | 1,110 | — | — | 0.1 |
| 10 | 12 | `inspect_block_table` | block_number=PROPblock_24, literature=GLOBlit_2800… | 1,116 | — | — | 0.1 |
| 11 | 1 | `L1_query` | instruction=Search for the binary mixture…, purpos… | 55,803 | — | — | 207.2 |
| | | **TOTAL (11 tools)** | | **64,736** | | **2,589** | **243.5** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 578 | 12,159 | 1,182 | 7.9 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,041 | 25,136 | 567 | 4.6 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,076 | 26,171 | 598 | 4.3 |
| 4 | L1-worker | claudeopus46 | 3,767 | 521 | 4,288 | 559 | 4.4 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,792 | 25,887 | 778 | 6.1 |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,506 | 26,601 | 673 | 5.2 |
| 7 | L1-worker | claudeopus46 | 3,767 | 6,213 | 9,980 | 1,683 | 12.8 |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,515 | 27,610 | 1,261 | 9.1 |
| 9 | L1-worker | claudeopus46 | 3,767 | 5,227 | 8,994 | 1,631 | 13.5 |
| 10 | L1-worker | claudeopus46 | 24,095 | 5,249 | 29,344 | 1,886 | 12.2 |
| 11 | L1-worker | claudeopus46 | 24,095 | 5,984 | 30,079 | 608 | 6.2 |
| 12 | L1-worker | claudeopus46 | 24,095 | 6,702 | 30,797 | 633 | 6.6 |
| 13 | L1-worker | claudeopus46 | 24,095 | 8,194 | 32,289 | 789 | 7.3 |
| 14 | L1-worker | claudeopus46 | 24,095 | 9,685 | 33,780 | 1,058 | 8.1 |
| 15 | L1-worker | claudeopus46 | 24,095 | 11,305 | 35,400 | 841 | 5.6 |
| 16 | L1-worker | claudeopus46 | 24,095 | 12,752 | 36,847 | 866 | 7.1 |
| 17 | L1-worker | claudeopus46 | 24,062 | 13,973 | 38,035 | 3,559 | 26.3 |
| 18 | L1-worker | claudeopus46 | 24,062 | 19,038 | 43,100 | 3,567 | 25.2 |
| 19 | L1-worker | claudeopus46 | 2,320 | 4,722 | 7,042 | 1,189 | 7.9 |
| 20 | L1-worker | claudeopus46 | 627 | 4,602 | 5,229 | 1,008 | 8.7 |
| 21 | L1-worker | claudeopus46 | 2,106 | 5,884 | 7,990 | 3,077 | 12.0 |
| 22 | L1-worker | claudeopus46 | 366 | 1,626 | 1,992 | 1,144 | 4.2 |
| 23 | L1-worker | claudeopus46 | 366 | 3,854 | 4,220 | 2,202 | 8.1 |
| 24 | L1-worker | claudeopus46 | 787 | 55,763 | 56,550 | 865 | 10.1 |
| 25 | L0-main | claudeopus46 | 11,581 | 29,617 | 41,198 | 3,399 | 27.6 |
| 26 | L0-main | claudeopus46 | 2,320 | 3,231 | 5,551 | 1,292 | 8.7 |
| 27 | L0-main | claudeopus46 | 2,106 | 3,641 | 5,747 | 1,484 | 8.8 |
| 28 | L0-main | claudeopus46 | 366 | 1,767 | 2,133 | 1,248 | 5.1 |
| 29 | L0-main | claudeopus46 | 366 | 2,033 | 2,399 | 1,896 | 7.3 |
| 30 | L0-main | claudeopus46 | 560 | 5,699 | 6,259 | 686 | 4.7 |
| 31 | L0-main | claudeopus46 | 1,156 | 10,993 | 12,149 | 2,853 | 16.2 |
| 32 | L0-main | claudeopus46 | 366 | 3,546 | 3,912 | 2,752 | 9.9 |

