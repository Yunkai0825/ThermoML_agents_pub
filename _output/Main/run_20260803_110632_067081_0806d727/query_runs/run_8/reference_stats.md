# Reference Stats — query-agent

**Run started:** 2026-08-03 11:31:47
**Wall time (at last flush):** 1,034.4 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 8 | 41,695 | 245,861 | 38,131 | 287,556 | 35,944 | 205.7 | claudeopus46 |
| L1-worker | 61 | 462,662 | 1,031,689 | 138,915 | 1,494,351 | 24,497 | 830.5 | claudeopus46 |
| **TOTAL** | **69** | **504,357** | **1,277,550** | **177,046** | **1,781,907** | **25,824** | **1036.2** | |

**Estimated tokens:** ~445,476 input + ~44,261 output = ~489,737 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 10 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_property_ids` | 0 | 6 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 15 | 5 | 5 | 18 | 34 | 1,780 |
| `search_blocks` | 2 | 1 | 3 | 2 | 4 | 4 | 264 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 4 | 3 | 10 | 10 | 611 |
| `search_system_registry` | 2 | 1 | 4 | 3 | 10 | 10 | 611 |
| `search_blocks` | 2 | 1 | 4 | 2 | 7 | 7 | 493 |
| `search_blocks` | 2 | 1 | 4 | 3 | 10 | 10 | 611 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 28 |
| `search_blocks` | 2 | 1 | 4 | 3 | 10 | 10 | 611 |
| `search_system_registry` | 2 | 1 | 4 | 3 | 10 | 10 | 611 |
| `search_blocks` | 2 | 1 | 4 | 3 | 10 | 10 | 611 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **30** | **30** | **38** | **28** | **90** | **106** | **6,231** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (10 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks, search_system_registry |
| GLOBcomp_61 |  | resolve_compound_ids, search_blocks, search_system_registry |
| GLOBcomp_2199 |  | resolve_compound_ids |
| GLOBcomp_5558 |  | resolve_compound_ids |
| GLOBcomp_113 |  | resolve_compound_ids |
| GLOBcomp_111 |  | resolve_compound_ids |
| GLOBcomp_251 |  | resolve_compound_ids |
| GLOBcomp_1741 |  | resolve_compound_ids |
| GLOBcomp_5309 |  | resolve_compound_ids |
| GLOBcomp_167 |  | resolve_compound_ids |

#### Properties (18 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_1 |  | resolve_property_ids, search_blocks, search_system_registry |
| GLOBprop_4 |  | resolve_property_ids, search_blocks |
| GLOBprop_40 |  | resolve_property_ids |
| GLOBprop_42 |  | resolve_property_ids |
| GLOBprop_44 |  | resolve_property_ids, search_blocks |
| GLOBprop_33 |  | resolve_property_ids |
| GLOBprop_28 | Excess molar volume, m3/mol | search_blocks |
| GLOBprop_85 | Excess molar heat capacity, J/K/mol | search_blocks |
| GLOBprop_13 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBprop_17 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBprop_84 | Partial molar volume, m3/mol | search_blocks |
| GLOBprop_8 | Speed of sound, m/s | search_blocks |
| GLOBprop_9 | Molar heat capacity at constant pressure, J/K/mol | search_blocks |
| GLOBprop_34 | Thermal conductivity, W/m/K | search_blocks |
| GLOBprop_11 | Solid-liquid equilibrium temperature, K | search_blocks |
| GLOBprop_7 | Refractive index (Na D-line) | search_blocks |
| GLOBprop_5 | Vapor or sublimation pressure, kPa | search_blocks |
| GLOBprop_74 | Specific volume, m3/kg | search_blocks |

#### References (18 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_1283 |  | search_blocks |
| GLOBlit_1623 |  | search_blocks, search_system_registry |
| GLOBlit_2574 |  | search_blocks |
| GLOBlit_2605 |  | search_blocks |
| GLOBlit_2831 |  | search_blocks, search_system_registry |
| GLOBlit_2979 |  | search_blocks, search_system_registry |
| GLOBlit_3180 |  | search_blocks, search_system_registry |
| GLOBlit_5233 |  | search_blocks, search_system_registry |
| GLOBlit_5826 |  | search_blocks |
| GLOBlit_5907 |  | search_blocks |
| GLOBlit_6775 |  | search_blocks, search_system_registry |
| GLOBlit_7545 |  | search_blocks, search_system_registry |
| GLOBlit_8239 |  | search_blocks, search_system_registry |
| GLOBlit_8556 |  | search_blocks, search_system_registry |
| GLOBlit_8686 |  | search_blocks |
| GLOBlit_9758 |  | search_blocks, search_system_registry |
| GLOBlit_10313 |  | search_blocks |
| GLOBlit_11906 |  | search_blocks |

#### Measurements (25 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_29 | Excess molar volume, m3/mol | search_blocks |
| GLOBmeas_9 | Excess molar heat capacity, J/K/mol | search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_192 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBmeas_169 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_1187 | Partial molar volume, m3/mol | search_blocks |
| GLOBmeas_7 | Speed of sound, m/s | search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_153 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_6 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_132 | Molar heat capacity at constant pressure, J/K/mol | search_blocks |
| GLOBmeas_193 | Thermal conductivity, W/m/K | search_blocks |
| GLOBmeas_33 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_17 | Molar heat capacity at constant pressure, J/K/mol | search_blocks |
| GLOBmeas_130 | Solid-liquid equilibrium temperature, K | search_blocks |
| GLOBmeas_20 | Speed of sound, m/s | search_blocks |
| GLOBmeas_11 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_3 | Refractive index (Na D-line) | search_blocks |
| GLOBmeas_4 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_194 | Speed of sound, m/s | search_blocks |
| GLOBmeas_141 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_41 | Thermal conductivity, W/m/K | search_blocks |
| GLOBmeas_1716 | Relative permittivity at zero frequency | search_blocks |
| GLOBmeas_171 | Vapor or sublimation pressure, kPa | search_blocks |
| GLOBmeas_65 | Specific volume, m3/kg | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks, search_system_registry |

#### Variables (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | search_blocks, search_system_registry |
| GLOBvar_2 | Mole fraction | search_blocks, search_system_registry |
| GLOBvar_3 | Pressure, kPa | search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks, search_system_registry |
| GLOBvar_5 | Mass fraction | search_blocks, search_system_registry |

#### Constraints (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | search_blocks, search_system_registry |
| GLOBconstr_3 | Mole fraction | search_blocks |
| GLOBconstr_2 | Temperature, K | search_blocks, search_system_registry |
| GLOBconstr_5 | Mass fraction | search_blocks, search_system_registry |
| GLOBconstr_22 | Volume fraction | search_blocks |

#### Solvents (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_23 |  | search_blocks, search_system_registry |
| GLOBsolvent_1 |  | search_blocks, search_system_registry |

#### Block_Types (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | search_system_registry |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 10 |
| Unique Properties | 18 |
| Unique References | 18 |
| Unique Measurements | 25 |
| Unique Phases | 1 |
| Unique Variables | 5 |
| Unique Constraints | 5 |
| Unique Solvents | 2 |
| Unique Block_Types | 1 |
| Total DOIs | 18 |
| Unique parent blocks | 34 |
| Explicit block/subsystem targets | 34 |
| Subsystem targets | 0 |
| Target-matched data points | 6,231 |

---

## 3. DOI & Block References

**Unique DOIs:** 18  |  **Parent blocks:** 34  |  **Explicit targets:** 34  |  **Subsystems:** 0  |  **Target-matched datapoints:** 1,780

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2013.06.041 | 2 | 185 | binary | search_blocks |
| 10.1016/j.fluid.2014.12.040 | 2 | 168 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2005.06.018 | 1 | 36 | binary | search_blocks |
| 10.1016/j.jct.2005.08.015 | 1 | 33 | binary | search_blocks |
| 10.1016/j.jct.2007.05.010 | 2 | 16 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2008.07.005 | 1 | 96 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2009.11.018 | 2 | 28 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2018.04.007 | 4 | 16 | binary | search_blocks, search_system_registry |
| 10.1016/j.tca.2009.01.008 | 1 | 30 | binary | search_blocks |
| 10.1016/j.tca.2010.10.012 | 1 | 5 | binary | search_blocks |
| 10.1021/acs.jced.5b00964 | 2 | 39 | binary | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00403 | 3 | 291 | binary | search_blocks, search_system_registry |
| 10.1021/je0340755 | 3 | 375 | binary | search_blocks, search_system_registry |
| 10.1021/je049960h | 3 | 84 | binary | search_blocks, search_system_registry |
| 10.1021/je050237g | 1 | 28 | binary | search_blocks |
| 10.1021/je201184b | 2 | 212 | binary | search_blocks, search_system_registry |
| 10.1021/je4009014 | 1 | 73 | binary | search_blocks |
| 10.1021/je9010568 | 2 | 65 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2013.06.041 | PROPblock_13 | declared | 100 | binary | — | search_blocks |
| 10.1016/j.fluid.2013.06.041 | PROPblock_14 | declared | 85 | binary | — | search_blocks |
| 10.1016/j.fluid.2014.12.040 | PROPblock_10 | declared | 84 | binary | — | search_blocks |
| 10.1016/j.fluid.2014.12.040 | PROPblock_9 | declared | 84 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2005.06.018 | PROPblock_1 | declared | 36 | binary | — | search_blocks |
| 10.1016/j.jct.2005.08.015 | PROPblock_2 | declared | 33 | binary | — | search_blocks |
| 10.1016/j.jct.2007.05.010 | PROPblock_11 | declared | 8 | binary | — | search_blocks |
| 10.1016/j.jct.2007.05.010 | PROPblock_12 | declared | 8 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2008.07.005 | PROPblock_6 | declared | 96 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2009.11.018 | PROPblock_5 | declared | 14 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2009.11.018 | PROPblock_6 | declared | 14 | binary | — | search_blocks |
| 10.1016/j.jct.2018.04.007 | PROPblock_1 | declared | 4 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2018.04.007 | PROPblock_2 | declared | 4 | binary | — | search_blocks |
| 10.1016/j.jct.2018.04.007 | PROPblock_3 | declared | 4 | binary | — | search_blocks |
| 10.1016/j.jct.2018.04.007 | PROPblock_4 | declared | 4 | binary | — | search_blocks |
| 10.1016/j.tca.2009.01.008 | PROPblock_9 | declared | 30 | binary | — | search_blocks |
| 10.1016/j.tca.2010.10.012 | PROPblock_2 | declared | 5 | binary | — | search_blocks |
| 10.1021/acs.jced.5b00964 | PROPblock_15 | declared | 36 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.5b00964 | PROPblock_16 | declared | 3 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00403 | PROPblock_13 | declared | 105 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00403 | PROPblock_14 | declared | 105 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00403 | PROPblock_15 | declared | 81 | binary | — | search_blocks |
| 10.1021/je0340755 | PROPblock_28 | declared | 125 | binary | — | search_blocks |
| 10.1021/je0340755 | PROPblock_29 | declared | 125 | binary | — | search_blocks |
| 10.1021/je0340755 | PROPblock_30 | declared | 125 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je049960h | PROPblock_10 | declared | 21 | binary | — | search_blocks |
| 10.1021/je049960h | PROPblock_11 | declared | 30 | binary | — | search_blocks |
| 10.1021/je049960h | PROPblock_12 | declared | 33 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je050237g | PROPblock_1 | declared | 28 | binary | — | search_blocks |
| 10.1021/je201184b | PROPblock_1 | declared | 106 | binary | — | search_blocks |
| 10.1021/je201184b | PROPblock_2 | declared | 106 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je4009014 | PROPblock_5 | declared | 73 | binary | — | search_blocks |
| 10.1021/je9010568 | PROPblock_7 | declared | 44 | binary | — | search_blocks |
| 10.1021/je9010568 | PROPblock_8 | declared | 21 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (pre-compaction)

| # | Iter | Tool | Args | Raw (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=10, min_score=50, purpose=Resolve compound I… | 242 | KEEP | 242 | 5.6 |
| 2 | 2 | `resolve_property_ids` | limit=10, min_score=50, purpose=Resolve property I… | 726 | KEEP | 726 | 6.8 |
| 3 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_61'], limit=50, … | 701 | KEEP | 686 | 21.6 |
| 4 | 1 | `L1_query` | context=Looking for solvent property …, id_catalog… | 11,420 | — | — | 197.5 |
| 5 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_61'], limit=50, … | 1,366 | KEEP | 1366 | 23.3 |
| 6 | 2 | `L1_query` | context=Previous query found 4 blocks…, id_catalog… | 270 | — | — | 72.9 |
| 7 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_61'], limit=50, … | 1,091 | KEEP | 1091 | 15.2 |
| 8 | 3 | `search_system_registry` | compound=['GLOBcomp_1', 'GLOBcomp_61'], limit=20, … | 1,140 | KEEP | 1140 | 23.3 |
| 9 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_61'], limit=10, … | 557 | KEEP | 542 | 22.8 |
| 10 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_61'], limit=10, … | 345 | KEEP | 330 | 22.1 |
| 11 | 2 | `L1_query` | context=Previous query found 10 block…, id_catalog… | 204 | — | — | 334.3 |
| 12 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_61'], limit=50, … | 782 | DISCARD | 724 | 15.8 |
| 13 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_61'], limit=50, … | 766 | KEEP | 736 | 11.2 |
| 14 | 2 | `L1_query` | context=Previous query found 1 block …, id_catalog… | 9,183 | — | — | 70.9 |
| 15 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_61'], limit=50, … | 1,179 | KEEP | 1104 | 22.9 |
| 16 | 2 | `search_system_registry` | compound=['GLOBcomp_1', 'GLOBcomp_61'], limit=20, … | 1,060 | KEEP | 970 | 24.2 |
| 17 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_61'], limit=10, … | 1,044 | KEEP | 1044 | 22.1 |
| 18 | 3 | `L1_query` | context=Previous query found 10 densi…, id_catalog… | 270 | — | — | 169.3 |
| | | **TOTAL (18 tools)** | | **32,346** | | **10,701** | **1081.8** |

---

## 5. Compaction Events

| # | Trigger | Outcome | Before (chars) | After (chars) | Saved (chars) | Saved (%) |
|--:|---------|---------|---------------:|--------------:|--------------:|----------:|
| 1 | interval=3 | skipped_by_agent | 5,033 | 5,033 | 0 | 0.0% |
| 2 | interval=3 | skipped_by_agent | 5,231 | 5,231 | 0 | 0.0% |
| 3 | interval=3 | skipped_by_agent | 5,645 | 5,645 | 0 | 0.0% |

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 9,605 | 999 | 10,604 | 2,092 | 10.8 |
| 2 | L1-worker | claudeopus46 | 20,643 | 1,439 | 22,082 | 1,115 | 5.9 |
| 3 | L1-worker | claudeopus46 | 20,643 | 3,282 | 23,925 | 15,208 | 58.4 |
| 4 | L1-worker | claudeopus46 | 2,065 | 1,219 | 3,284 | 507 | 5.1 |
| 5 | L1-worker | claudeopus46 | 2,065 | 949 | 3,014 | 1,091 | 6.6 |
| 6 | L1-worker | claudeopus46 | 20,643 | 4,275 | 24,918 | 13,508 | 54.0 |
| 7 | L1-worker | claudeopus46 | 2,065 | 22,615 | 24,680 | 1,695 | 13.2 |
| 8 | L1-worker | claudeopus46 | 20,610 | 6,328 | 26,938 | 599 | 4.9 |
| 9 | L1-worker | claudeopus46 | 20,643 | 5,575 | 26,218 | 2,898 | 18.2 |
| 10 | L1-worker | claudeopus46 | 1,356 | 2,431 | 3,787 | 797 | 4.1 |
| 11 | L1-worker | claudeopus46 | 536 | 2,311 | 2,847 | 972 | 5.5 |
| 12 | L1-worker | claudeopus46 | 1,323 | 7,412 | 8,735 | 1,255 | 7.6 |
| 13 | L1-worker | claudeopus46 | 298 | 1,977 | 2,275 | 943 | 5.3 |
| 14 | L1-worker | claudeopus46 | 747 | 17,303 | 18,050 | 718 | 7.5 |
| 15 | L0-main | claudeopus46 | 9,605 | 25,134 | 34,739 | 14,539 | 67.4 |
| 16 | L1-worker | claudeopus46 | 20,643 | 13,405 | 34,048 | 773 | 6.4 |
| 17 | L1-worker | claudeopus46 | 2,065 | 8,632 | 10,697 | 1,721 | 15.0 |
| 18 | L1-worker | claudeopus46 | 20,643 | 15,265 | 35,908 | 3,655 | 17.8 |
| 19 | L1-worker | claudeopus46 | 1,356 | 3,121 | 4,477 | 960 | 6.8 |
| 20 | L1-worker | claudeopus46 | 536 | 3,001 | 3,537 | 1,079 | 7.1 |
| 21 | L1-worker | claudeopus46 | 1,323 | 6,307 | 7,630 | 2,126 | 9.4 |
| 22 | L1-worker | claudeopus46 | 298 | 2,848 | 3,146 | 1,702 | 7.7 |
| 23 | L1-worker | claudeopus46 | 747 | 33,570 | 34,317 | 583 | 6.9 |
| 24 | L1-worker | claudeopus46 | 20,643 | 42,234 | 62,877 | 798 | 6.2 |
| 25 | L1-worker | claudeopus46 | 2,065 | 7,143 | 9,208 | 1,641 | 14.4 |
| 26 | L1-worker | claudeopus46 | 20,643 | 43,801 | 64,444 | 1,127 | 8.7 |
| 27 | L1-worker | claudeopus46 | 20,643 | 45,549 | 66,192 | 12,587 | 65.1 |
| 28 | L1-worker | claudeopus46 | 2,065 | 9,005 | 11,070 | 1,589 | 15.1 |
| 29 | L1-worker | claudeopus46 | 20,610 | 47,414 | 68,024 | 618 | 9.0 |
| 30 | L1-worker | claudeopus46 | 20,643 | 46,661 | 67,304 | 13,426 | 68.1 |
| 31 | L1-worker | claudeopus46 | 2,065 | 5,197 | 7,262 | 1,878 | 14.6 |
| 32 | L1-worker | claudeopus46 | 2,065 | 7,101 | 9,166 | 1,728 | 13.4 |
| 33 | L1-worker | claudeopus46 | 20,643 | 48,410 | 69,053 | 6,814 | 42.9 |
| 34 | L1-worker | claudeopus46 | 1,356 | 3,195 | 4,551 | 975 | 6.1 |
| 35 | L1-worker | claudeopus46 | 536 | 3,075 | 3,611 | 1,282 | 8.8 |
| 36 | L1-worker | claudeopus46 | 298 | 1,357 | 1,655 | 963 | 4.4 |
| 37 | L1-worker | claudeopus46 | 1,323 | 9,925 | 11,248 | 2,957 | 16.7 |
| 38 | L1-worker | claudeopus46 | 298 | 3,679 | 3,977 | 2,516 | 11.5 |
| 39 | L1-worker | claudeopus46 | 747 | 54,672 | 55,419 | 582 | 8.1 |
| 40 | L1-worker | claudeopus46 | 1,160 | 14,060 | 15,220 | 2,751 | 13.0 |
| 41 | L1-worker | claudeopus46 | 20,643 | 42,296 | 62,939 | 1,126 | 8.3 |
| 42 | L1-worker | claudeopus46 | 2,065 | 516 | 2,581 | 1,145 | 8.2 |
| 43 | L1-worker | claudeopus46 | 2,065 | 3,074 | 5,139 | 1,014 | 10.6 |
| 44 | L1-worker | claudeopus46 | 20,643 | 44,526 | 65,169 | 2,265 | 14.6 |
| 45 | L1-worker | claudeopus46 | 536 | 1,500 | 2,036 | 701 | 4.3 |
| 46 | L1-worker | claudeopus46 | 1,356 | 1,620 | 2,976 | 717 | 4.8 |
| 47 | L1-worker | claudeopus46 | 1,323 | 5,480 | 6,803 | 681 | 9.0 |
| 48 | L1-worker | claudeopus46 | 298 | 1,403 | 1,701 | 554 | 5.0 |
| 49 | L1-worker | claudeopus46 | 747 | 13,165 | 13,912 | 554 | 6.3 |
| 50 | L0-main | claudeopus46 | 9,605 | 65,367 | 74,972 | 2,176 | 19.0 |
| 51 | L1-worker | claudeopus46 | 20,643 | 51,495 | 72,138 | 787 | 6.9 |
| 52 | L1-worker | claudeopus46 | 2,065 | 7,099 | 9,164 | 1,604 | 15.0 |
| 53 | L1-worker | claudeopus46 | 20,643 | 53,183 | 73,826 | 850 | 7.3 |
| 54 | L1-worker | claudeopus46 | 2,065 | 9,002 | 11,067 | 1,677 | 16.5 |
| 55 | L1-worker | claudeopus46 | 20,643 | 54,774 | 75,417 | 2,638 | 18.1 |
| 56 | L1-worker | claudeopus46 | 2,065 | 7,134 | 9,199 | 1,603 | 13.8 |
| 57 | L1-worker | claudeopus46 | 20,610 | 57,141 | 77,751 | 419 | 4.5 |
| 58 | L1-worker | claudeopus46 | 20,643 | 56,388 | 77,031 | 4,812 | 31.5 |
| 59 | L1-worker | claudeopus46 | 1,356 | 2,996 | 4,352 | 887 | 6.1 |
| 60 | L1-worker | claudeopus46 | 536 | 2,876 | 3,412 | 825 | 6.2 |
| 61 | L1-worker | claudeopus46 | 298 | 1,181 | 1,479 | 812 | 3.7 |
| 62 | L1-worker | claudeopus46 | 1,323 | 9,055 | 10,378 | 2,293 | 11.7 |
| 63 | L1-worker | claudeopus46 | 298 | 3,015 | 3,313 | 1,911 | 9.7 |
| 64 | L1-worker | claudeopus46 | 747 | 47,027 | 47,774 | 903 | 8.9 |
| 65 | L0-main | claudeopus46 | 9,605 | 105,820 | 115,425 | 5,391 | 38.6 |
| 66 | L0-main | claudeopus46 | 1,356 | 5,522 | 6,878 | 1,830 | 11.4 |
| 67 | L0-main | claudeopus46 | 298 | 2,212 | 2,510 | 1,818 | 5.6 |
| 68 | L0-main | claudeopus46 | 1,323 | 34,543 | 35,866 | 5,596 | 31.5 |
| 69 | L0-main | claudeopus46 | 298 | 6,264 | 6,562 | 4,689 | 21.4 |

