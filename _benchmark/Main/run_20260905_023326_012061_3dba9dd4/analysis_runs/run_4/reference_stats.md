# Reference Stats — analysis-agent

**Run started:** 2026-09-05 02:33:37
**Wall time (at last flush):** 821.5 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 45 | 864,080 | 4,367,889 | 62,586 | 5,231,969 | 116,265 | 537.9 | claudeopus46 |
| L1-worker | 44 | 601,166 | 415,676 | 57,545 | 1,016,842 | 23,110 | 416.9 | claudeopus46 |
| **TOTAL** | **89** | **1,465,246** | **4,783,565** | **120,131** | **6,248,811** | **70,211** | **954.8** | |

**Estimated tokens:** ~1,562,202 input + ~30,032 output = ~1,592,234 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_property_ids` | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 5 | 4 | 22 | 22 | 2,417 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 5 | 4 | 22 | 22 | 2,417 |
| `search_blocks` | 2 | 11 | 4 | 4 | 29 | 50 | 3,112 |
| `search_system_registry` | 2 | 1 | 5 | 3 | 17 | 17 | 2,366 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml_parallel` | 2 | 1 | 5 | 3 | 17 | 17 | 747 |
| `fit_block_derived` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `list_session_files` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **16** | **16** | **24** | **18** | **107** | **128** | **11,059** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_1 |  | query_thermoml_parallel, resolve_compound_ids, search_blocks, search_system_registry |
| GLOBcomp_2 |  | query_thermoml_parallel, resolve_compound_ids, search_blocks, search_system_registry |
| GLOBcomp_5494 |  | resolve_compound_ids |

#### Properties (12 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_28 |  | resolve_property_ids |
| GLOBprop_1 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBprop_3 | Activity coefficient | search_blocks |
| GLOBprop_5 | Vapor or sublimation pressure, kPa | search_blocks |
| GLOBprop_17 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBprop_14 | Boiling temperature at pressure P, K | search_blocks |
| GLOBprop_2 | Mole fraction | search_blocks |
| GLOBprop_4 | Viscosity, Pa*s | search_blocks |
| GLOBprop_44 | Relative permittivity at zero frequency | search_blocks |
| GLOBprop_58 | Azeotropic temperature, K | search_blocks |
| GLOBprop_45 | Azeotropic composition: mole fraction | search_blocks |
| GLOBprop_8 | Speed of sound, m/s | search_blocks |

#### References (45 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_220 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_1483 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_2432 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_2825 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_3475 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_4415 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_5201 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_5473 |  | search_blocks |
| GLOBlit_7085 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_7178 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_7448 |  | search_blocks |
| GLOBlit_7676 |  | search_blocks |
| GLOBlit_8050 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_8888 |  | search_blocks |
| GLOBlit_9006 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_10159 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_10699 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_10866 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_11005 |  | search_blocks |
| GLOBlit_11136 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_11504 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_11792 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_299 |  | search_blocks |
| GLOBlit_384 |  | search_blocks |
| GLOBlit_528 |  | search_blocks |
| GLOBlit_742 |  | search_blocks |
| GLOBlit_757 |  | search_blocks |
| GLOBlit_977 |  | search_blocks |
| GLOBlit_1184 |  | search_blocks |
| GLOBlit_1197 |  | search_blocks |
| GLOBlit_1289 |  | search_blocks |
| GLOBlit_1482 |  | search_blocks |
| GLOBlit_1518 |  | search_blocks |
| GLOBlit_1742 |  | search_blocks |
| GLOBlit_1971 |  | search_blocks |
| GLOBlit_2035 |  | search_blocks |
| GLOBlit_2092 |  | search_blocks |
| GLOBlit_2220 |  | search_blocks |
| GLOBlit_2300 |  | search_blocks |
| GLOBlit_2574 |  | search_blocks |
| GLOBlit_2732 |  | search_blocks |
| GLOBlit_3697 |  | search_blocks |
| GLOBlit_3971 |  | search_blocks |
| GLOBlit_4181 |  | search_blocks |
| GLOBlit_5073 |  | search_blocks |

#### Measurements (33 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_138 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBmeas_66 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBmeas_2 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBmeas_134 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBmeas_236 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBmeas_203 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBmeas_212 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBmeas_141 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBmeas_6 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBmeas_543 | Activity coefficient | search_blocks |
| GLOBmeas_1045 | Activity coefficient | search_blocks |
| GLOBmeas_1042 | Activity coefficient | search_blocks |
| GLOBmeas_133 | Vapor or sublimation pressure, kPa | search_blocks |
| GLOBmeas_13 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_5 | Boiling temperature at pressure P, K | search_blocks |
| GLOBmeas_1362 | Boiling temperature at pressure P, K | search_blocks |
| GLOBmeas_2137 | Boiling temperature at pressure P, K | search_blocks |
| GLOBmeas_131 | Mole fraction | search_blocks |
| GLOBmeas_1 | Mole fraction | search_blocks |
| GLOBmeas_10 | Mole fraction | search_blocks |
| GLOBmeas_664 | Vapor or sublimation pressure, kPa | search_blocks |
| GLOBmeas_12 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_4 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_1153 | Activity coefficient | search_blocks |
| GLOBmeas_1355 | Boiling temperature at pressure P, K | search_blocks |
| GLOBmeas_169 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_161 | Vapor or sublimation pressure, kPa | search_blocks |
| GLOBmeas_1497 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_140 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_53 | Relative permittivity at zero frequency | search_blocks |
| GLOBmeas_39 | Azeotropic temperature, K | search_blocks |
| GLOBmeas_7 | Speed of sound, m/s | search_blocks |
| GLOBmeas_24 | Mole fraction | search_blocks |

#### Phases (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBphase_3 |  | search_blocks |
| GLOBphase_10 |  | search_blocks |

#### Variables (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBvar_3 | Pressure, kPa | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBvar_2 | Mole fraction | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBvar_4 | Molality, mol/kg | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBvar_5 | Mass fraction | query_thermoml_parallel, search_blocks, search_system_registry |

#### Solvents (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBsolvent_2 |  | search_blocks |

#### Constraints (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBconstr_2 | Temperature, K | search_blocks |
| GLOBconstr_8 | Molality, mol/kg | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBconstr_22 | Volume fraction | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBconstr_3 | Mole fraction | search_blocks |
| GLOBconstr_4 | Frequency, MHz | search_blocks |

#### Block_Types (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | query_thermoml_parallel, search_system_registry |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 3 |
| Unique Properties | 12 |
| Unique References | 45 |
| Unique Measurements | 33 |
| Unique Phases | 3 |
| Unique Variables | 5 |
| Unique Solvents | 2 |
| Unique Constraints | 6 |
| Unique Block_Types | 1 |
| Total DOIs | 45 |
| Unique parent blocks | 66 |
| Explicit block/subsystem targets | 66 |
| Subsystem targets | 0 |
| Target-matched data points | 12,678 |

---

## 3. DOI & Block References

**Unique DOIs:** 45  |  **Parent blocks:** 66  |  **Explicit targets:** 66  |  **Subsystems:** 0  |  **Target-matched datapoints:** 3,867

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2004.11.019 | 1 | 810 | binary | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1016/j.fluid.2005.08.018 | 3 | 13 | binary | search_blocks |
| 10.1016/j.fluid.2006.04.017 | 1 | 28 | binary | search_blocks |
| 10.1016/j.fluid.2007.06.007 | 2 | 30 | binary | search_blocks |
| 10.1016/j.fluid.2009.10.002 | 2 | 10 | binary | search_blocks |
| 10.1016/j.fluid.2009.11.014 | 2 | 36 | binary | search_blocks |
| 10.1016/j.fluid.2011.06.009 | 2 | 90 | binary | search_blocks |
| 10.1016/j.fluid.2012.11.026 | 2 | 48 | binary | search_blocks |
| 10.1016/j.fluid.2012.12.014 | 2 | 152 | binary | search_blocks |
| 10.1016/j.fluid.2013.07.001 | 1 | 42 | binary | search_blocks |
| 10.1016/j.fluid.2014.05.031 | 1 | 56 | binary | search_blocks |
| 10.1016/j.fluid.2014.05.032 | 1 | 140 | binary | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1016/j.fluid.2014.07.022 | 2 | 14 | binary | search_blocks |
| 10.1016/j.fluid.2015.07.012 | 2 | 168 | binary | search_blocks |
| 10.1016/j.fluid.2016.08.030 | 1 | 4 | binary | search_blocks |
| 10.1016/j.fluid.2017.03.010 | 2 | 34 | binary | search_blocks |
| 10.1016/j.fluid.2017.09.005 | 2 | 144 | binary | search_blocks |
| 10.1016/j.fluid.2018.07.014 | 1 | 17 | binary | search_blocks |
| 10.1016/j.fluid.2019.03.019 | 2 | 32 | binary | search_blocks |
| 10.1016/j.jct.2004.07.019 | 1 | 565 | binary | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1016/j.jct.2005.06.018 | 1 | 27 | binary | search_blocks |
| 10.1016/j.jct.2006.08.002 | 4 | 326 | binary | search_blocks |
| 10.1016/j.jct.2007.05.004 | 2 | 74 | binary | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1016/j.jct.2011.10.009 | 1 | 70 | binary | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1016/j.jct.2012.08.009 | 1 | 14 | binary | search_blocks |
| 10.1016/j.jct.2013.08.020 | 4 | 34 | binary | search_blocks |
| 10.1016/j.jct.2014.05.020 | 1 | 30 | binary | search_blocks |
| 10.1016/j.jct.2015.06.024 | 2 | 80 | binary | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1016/j.jct.2017.07.021 | 1 | 24 | binary | search_blocks |
| 10.1016/j.jct.2018.02.022 | 1 | 244 | binary | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1016/j.jct.2019.02.027 | 1 | 9 | binary | search_blocks |
| 10.1021/acs.jced.6b01058 | 1 | 12 | binary | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1021/acs.jced.7b00299 | 1 | 2 | binary | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00086 | 1 | 6 | binary | search_blocks |
| 10.1021/acs.jced.8b00939 | 1 | 9 | binary | search_blocks |
| 10.1021/je020173z | 1 | 24 | binary | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1021/je0601098 | 1 | 12 | binary | search_blocks |
| 10.1021/je060335h | 1 | 164 | binary | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1021/je4003515 | 1 | 23 | binary | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1021/je600565m | 1 | 18 | binary | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1021/je700300y | 1 | 84 | binary | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1021/je700618y | 1 | 15 | binary | search_blocks |
| 10.1021/je800150h | 1 | 108 | binary | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1021/je900064e | 1 | 10 | binary | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1021/je900743e | 1 | 15 | binary | query_thermoml_parallel, search_blocks, search_system_registry |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2004.11.019 | PROPblock_2 | declared | 810 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1016/j.fluid.2005.08.018 | PROPblock_4 | declared | 2 | binary | — | search_blocks |
| 10.1016/j.fluid.2005.08.018 | PROPblock_5 | declared | 7 | binary | — | search_blocks |
| 10.1016/j.fluid.2005.08.018 | PROPblock_6 | declared | 4 | binary | — | search_blocks |
| 10.1016/j.fluid.2006.04.017 | PROPblock_3 | declared | 28 | binary | — | search_blocks |
| 10.1016/j.fluid.2007.06.007 | PROPblock_1 | declared | 15 | binary | — | search_blocks |
| 10.1016/j.fluid.2007.06.007 | PROPblock_2 | declared | 15 | binary | — | search_blocks |
| 10.1016/j.fluid.2009.10.002 | PROPblock_17 | declared | 5 | binary | — | search_blocks |
| 10.1016/j.fluid.2009.10.002 | PROPblock_18 | declared | 5 | binary | — | search_blocks |
| 10.1016/j.fluid.2009.11.014 | PROPblock_2 | declared | 18 | binary | — | search_blocks |
| 10.1016/j.fluid.2009.11.014 | PROPblock_3 | declared | 18 | binary | — | search_blocks |
| 10.1016/j.fluid.2011.06.009 | PROPblock_1 | declared | 45 | binary | — | search_blocks |
| 10.1016/j.fluid.2011.06.009 | PROPblock_2 | declared | 45 | binary | — | search_blocks |
| 10.1016/j.fluid.2012.11.026 | PROPblock_4 | declared | 24 | binary | — | search_blocks |
| 10.1016/j.fluid.2012.11.026 | PROPblock_5 | declared | 24 | binary | — | search_blocks |
| 10.1016/j.fluid.2012.12.014 | PROPblock_2 | declared | 76 | binary | — | search_blocks |
| 10.1016/j.fluid.2012.12.014 | PROPblock_3 | declared | 76 | binary | — | search_blocks |
| 10.1016/j.fluid.2013.07.001 | PROPblock_6 | declared | 42 | binary | — | search_blocks |
| 10.1016/j.fluid.2014.05.031 | PROPblock_4 | declared | 56 | binary | — | search_blocks |
| 10.1016/j.fluid.2014.05.032 | PROPblock_1 | declared | 140 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1016/j.fluid.2014.07.022 | PROPblock_1 | declared | 7 | binary | — | search_blocks |
| 10.1016/j.fluid.2014.07.022 | PROPblock_2 | declared | 7 | binary | — | search_blocks |
| 10.1016/j.fluid.2015.07.012 | PROPblock_3 | declared | 84 | binary | — | search_blocks |
| 10.1016/j.fluid.2015.07.012 | PROPblock_4 | declared | 84 | binary | — | search_blocks |
| 10.1016/j.fluid.2016.08.030 | PROPblock_1 | declared | 4 | binary | — | search_blocks |
| 10.1016/j.fluid.2017.03.010 | PROPblock_7 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.fluid.2017.03.010 | PROPblock_8 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.fluid.2017.09.005 | PROPblock_3 | declared | 72 | binary | — | search_blocks |
| 10.1016/j.fluid.2017.09.005 | PROPblock_4 | declared | 72 | binary | — | search_blocks |
| 10.1016/j.fluid.2018.07.014 | PROPblock_4 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.fluid.2019.03.019 | PROPblock_8 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.fluid.2019.03.019 | PROPblock_9 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.jct.2004.07.019 | PROPblock_2 | declared | 565 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1016/j.jct.2005.06.018 | PROPblock_4 | declared | 27 | binary | — | search_blocks |
| 10.1016/j.jct.2006.08.002 | PROPblock_1 | declared | 25 | binary | — | search_blocks |
| 10.1016/j.jct.2006.08.002 | PROPblock_2 | declared | 19 | binary | — | search_blocks |
| 10.1016/j.jct.2006.08.002 | PROPblock_3 | declared | 4 | binary | — | search_blocks |
| 10.1016/j.jct.2006.08.002 | PROPblock_4 | declared | 278 | binary | — | search_blocks |
| 10.1016/j.jct.2007.05.004 | PROPblock_11 | declared | 37 | binary | — | search_blocks |
| 10.1016/j.jct.2007.05.004 | PROPblock_12 | declared | 37 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1016/j.jct.2011.10.009 | PROPblock_3 | declared | 70 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1016/j.jct.2012.08.009 | PROPblock_18 | declared | 14 | binary | — | search_blocks |
| 10.1016/j.jct.2013.08.020 | PROPblock_10 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.jct.2013.08.020 | PROPblock_11 | declared | 1 | binary | — | search_blocks |
| 10.1016/j.jct.2013.08.020 | PROPblock_12 | declared | 1 | binary | — | search_blocks |
| 10.1016/j.jct.2013.08.020 | PROPblock_9 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.jct.2014.05.020 | PROPblock_1 | declared | 30 | binary | — | search_blocks |
| 10.1016/j.jct.2015.06.024 | PROPblock_7 | declared | 40 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1016/j.jct.2015.06.024 | PROPblock_8 | declared | 40 | binary | — | search_blocks |
| 10.1016/j.jct.2017.07.021 | PROPblock_3 | declared | 24 | binary | — | search_blocks |
| 10.1016/j.jct.2018.02.022 | PROPblock_19 | declared | 244 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1016/j.jct.2019.02.027 | PROPblock_21 | declared | 9 | binary | — | search_blocks |
| 10.1021/acs.jced.6b01058 | PROPblock_7 | declared | 12 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1021/acs.jced.7b00299 | PROPblock_10 | declared | 2 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00086 | PROPblock_46 | declared | 6 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00939 | PROPblock_17 | declared | 9 | binary | — | search_blocks |
| 10.1021/je020173z | PROPblock_5 | declared | 24 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1021/je0601098 | PROPblock_20 | declared | 12 | binary | — | search_blocks |
| 10.1021/je060335h | PROPblock_1 | declared | 164 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1021/je4003515 | PROPblock_7 | declared | 23 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1021/je600565m | PROPblock_6 | declared | 18 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1021/je700300y | PROPblock_7 | declared | 84 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1021/je700618y | PROPblock_9 | declared | 15 | binary | — | search_blocks |
| 10.1021/je800150h | PROPblock_9 | declared | 108 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1021/je900064e | PROPblock_6 | declared | 10 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1021/je900743e | PROPblock_3 | declared | 15 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 1 | `query_thermoml_parallel` | queries=[{'label': 'VE_direct', 'purp… | 224 | — | — | 0.0 |
| 2 | 2 | `query_thermoml_parallel` | queries=[{'label': 'VE_direct', 'purp… | 253 | — | — | 0.1 |
| 3 | 3 | `query_thermoml_parallel` | queries=[{'label': 'VE_direct', 'purp… | 152 | — | — | 0.0 |
| 4 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve water and e… | 307 | KEEP ←in 351 | 307 | 6.2 |
| 5 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve water and e… | 270 | KEEP ←in 351 | 270 | 5.7 |
| 6 | 4 | `resolve_property_ids` | limit=10, min_score=60, purpose=Find excess molar … | 256 | KEEP ←in 227 | 256 | 4.5 |
| 7 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=50, p… | 303 | KEEP ←in 14,080 | 303 | 17.0 |
| 8 | 6 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=50, p… | 1,076 | DISCARD ←in 39 | 1018 | 10.2 |
| 9 | 5 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=30, p… | 677 | KEEP ←in 14,080 | 659 | 16.3 |
| 10 | 7 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=50, p… | 1,412 | KEEP ←in 30,867 | 1250 | 15.9 |
| 11 | 6 | `search_system_registry` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=50, p… | 1,355 | KEEP ←in 2,557 | 1095 | 10.6 |
| 12 | 8 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=20, p… | 725 | DISCARD ←in 39 | 667 | 16.9 |
| 13 | 8 | `inspect_block_table` | block_number=GLOBlit_220::PROPblock_2, purpose=Ins… | 369 | — | — | 0.2 |
| 14 | 9 | `inspect_block_table` | block_number=GLOBlit_220::PROPblock_2, purpose=Gro… | 2,089 | — | — | 0.1 |
| 15 | 10 | `inspect_block_table` | block_number=GLOBlit_2432::PROPblock_2, purpose=Gr… | 4,539 | — | — | 0.2 |
| 16 | 11 | `inspect_block_table` | block_number=GLOBlit_5201::PROPblock_19, purpose=I… | 1,805 | — | — | 0.2 |
| 17 | 4 | `query_thermoml_parallel` | queries=[{'label': 'VE_direct', 'purp… | 163,237 | — | — | 278.3 |
| 18 | 7 | `inspect_block` | block_number=PROPblock_1, doi=10.1021/je060335h, p… | 1,359 | — | — | 0.1 |
| 19 | 9 | `fit_block_derived` | block_number=PROPblock_1, composition_hint=mole_fr… | 208 | — | — | 0.1 |
| 20 | 13 | `fit_block_derived` | block_number=PROPblock_1, composition_hint=mole_fr… | 301 | — | — | 0.0 |
| 21 | 16 | `fit_block_derived` | block_number=PROPblock_1, composition_hint=mole_fr… | 230 | — | — | 0.1 |
| 22 | 17 | `fit_block_derived` | block_number=PROPblock_1, composition_hint=mole_fr… | 954 | — | — | 1.8 |
| 23 | 18 | `predict_from_rk` | coeffs=[-4.64231e-06, 1.53527e-06, -…, n_points=10… | 205 | — | — | 0.1 |
| 24 | 19 | `fit_block_derived` | block_number=PROPblock_19, composition_hint=mole_f… | 961 | — | — | 1.9 |
| 25 | 20 | `predict_from_rk` | coeffs=[-3.38039e-06, 2.37917e-06, -…, mixing_rule… | 206 | — | — | 0.1 |
| 26 | 21 | `list_session_files` |  | 3,077 | — | — | 0.0 |
| 27 | 23 | `inspect_block` | block_number=PROPblock_1, doi=10.1021/je060335h, p… | 1,359 | — | — | 0.1 |
| 28 | 25 | `inspect_block` | block_number=PROPblock_1, doi=10.1021/je060335h, p… | 1,359 | — | — | 0.1 |
| | | **TOTAL (28 tools)** | | **189,268** | | **5,825** | **386.8** |

---

## 5. Compaction Events

| # | Trigger | Outcome | Before (chars) | After (chars) | Saved (chars) | Saved (%) |
|--:|---------|---------|---------------:|--------------:|--------------:|----------:|
| 1 | chars=98928>80000 | skipped_by_agent | 98,928 | 98,928 | 0 | 0.0% |
| 2 | chars=101375>80000 | skipped_by_agent | 101,375 | 101,375 | 0 | 0.0% |
| 3 | chars=102316>80000 | skipped_by_agent | 102,316 | 102,316 | 0 | 0.0% |
| 4 | chars=104215>80000 | skipped_by_agent | 104,215 | 104,215 | 0 | 0.0% |
| 5 | chars=105555>80000 | skipped_by_agent | 105,555 | 105,555 | 0 | 0.0% |
| 6 | chars=106856>80000 | skipped_by_agent | 106,856 | 106,856 | 0 | 0.0% |
| 7 | chars=107460>80000 | skipped_by_agent | 107,460 | 107,460 | 0 | 0.0% |
| 8 | chars=108829>80000 | skipped_by_agent | 108,829 | 108,829 | 0 | 0.0% |
| 9 | chars=109350>80000 | skipped_by_agent | 109,350 | 109,350 | 0 | 0.0% |
| 10 | chars=112704>80000 | skipped_by_agent | 112,704 | 112,704 | 0 | 0.0% |
| 11 | chars=128578>80000 | skipped_by_agent | 128,578 | 128,578 | 0 | 0.0% |
| 12 | chars=141008>80000 | skipped_by_agent | 141,008 | 141,008 | 0 | 0.0% |

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 22,518 | 649 | 23,167 | 2,137 | 12.7 |
| 2 | L0-main | claudeopus46 | 22,518 | 1,196 | 23,714 | 1,586 | 9.3 |
| 3 | L0-main | claudeopus46 | 22,518 | 1,728 | 24,246 | 1,859 | 9.8 |
| 4 | L0-main | claudeopus46 | 22,518 | 2,171 | 24,689 | 1,484 | 9.7 |
| 5 | L1-worker | claudeopus46 | 24,095 | 897 | 24,992 | 649 | 5.1 |
| 6 | L1-worker | claudeopus46 | 24,095 | 863 | 24,958 | 824 | 6.3 |
| 7 | L1-worker | claudeopus46 | 24,095 | 1,930 | 26,025 | 548 | 4.1 |
| 8 | L1-worker | claudeopus46 | 24,095 | 1,896 | 25,991 | 532 | 4.2 |
| 9 | L1-worker | claudeopus46 | 3,767 | 510 | 4,277 | 468 | 5.2 |
| 10 | L1-worker | claudeopus46 | 3,767 | 510 | 4,277 | 431 | 4.9 |
| 11 | L1-worker | claudeopus46 | 24,095 | 1,632 | 25,727 | 821 | 6.7 |
| 12 | L1-worker | claudeopus46 | 24,095 | 1,545 | 25,640 | 808 | 6.6 |
| 13 | L1-worker | claudeopus46 | 24,095 | 2,334 | 26,429 | 684 | 4.8 |
| 14 | L1-worker | claudeopus46 | 24,095 | 2,286 | 26,381 | 516 | 4.5 |
| 15 | L1-worker | claudeopus46 | 3,767 | 381 | 4,148 | 388 | 4.3 |
| 16 | L1-worker | claudeopus46 | 24,095 | 2,431 | 26,526 | 808 | 6.0 |
| 17 | L1-worker | claudeopus46 | 24,095 | 3,175 | 27,270 | 656 | 5.0 |
| 18 | L1-worker | claudeopus46 | 3,767 | 14,542 | 18,309 | 1,767 | 16.0 |
| 19 | L1-worker | claudeopus46 | 3,767 | 598 | 4,365 | 1,231 | 9.7 |
| 20 | L1-worker | claudeopus46 | 24,095 | 2,607 | 26,702 | 1,323 | 9.3 |
| 21 | L1-worker | claudeopus46 | 24,095 | 4,194 | 28,289 | 842 | 6.0 |
| 22 | L1-worker | claudeopus46 | 3,767 | 14,569 | 18,336 | 1,660 | 15.5 |
| 23 | L1-worker | claudeopus46 | 3,767 | 31,260 | 35,027 | 1,981 | 13.9 |
| 24 | L1-worker | claudeopus46 | 24,095 | 3,625 | 27,720 | 1,189 | 8.9 |
| 25 | L1-worker | claudeopus46 | 24,095 | 5,957 | 30,052 | 1,656 | 11.1 |
| 26 | L1-worker | claudeopus46 | 3,767 | 3,050 | 6,817 | 1,341 | 10.1 |
| 27 | L1-worker | claudeopus46 | 3,767 | 454 | 4,221 | 945 | 7.8 |
| 28 | L1-worker | claudeopus46 | 24,095 | 5,345 | 29,440 | 3,032 | 19.2 |
| 29 | L1-worker | claudeopus46 | 24,095 | 7,081 | 31,176 | 1,742 | 11.7 |
| 30 | L1-worker | claudeopus46 | 2,106 | 2,284 | 4,390 | 92 | 2.0 |
| 31 | L1-worker | claudeopus46 | 2,320 | 1,300 | 3,620 | 488 | 3.6 |
| 32 | L1-worker | claudeopus46 | 627 | 1,180 | 1,807 | 614 | 3.9 |
| 33 | L1-worker | claudeopus46 | 366 | 869 | 1,235 | 67 | 2.0 |
| 34 | L1-worker | claudeopus46 | 24,095 | 12,461 | 36,556 | 1,572 | 11.7 |
| 35 | L1-worker | claudeopus46 | 366 | 925 | 1,291 | 458 | 2.6 |
| 36 | L1-worker | claudeopus46 | 787 | 3,547 | 4,334 | 436 | 4.3 |
| 37 | L1-worker | claudeopus46 | 24,095 | 13,164 | 37,259 | 596 | 5.6 |
| 38 | L1-worker | claudeopus46 | 24,095 | 15,552 | 39,647 | 575 | 7.1 |
| 39 | L1-worker | claudeopus46 | 24,095 | 20,397 | 44,492 | 937 | 12.4 |
| 40 | L1-worker | claudeopus46 | 24,095 | 22,597 | 46,692 | 3,105 | 25.3 |
| 41 | L1-worker | claudeopus46 | 24,062 | 32,865 | 56,927 | 3,779 | 28.7 |
| 42 | L1-worker | claudeopus46 | 24,062 | 36,677 | 60,739 | 3,657 | 26.4 |
| 43 | L1-worker | claudeopus46 | 627 | 5,569 | 6,196 | 1,136 | 9.1 |
| 44 | L1-worker | claudeopus46 | 2,320 | 5,689 | 8,009 | 1,380 | 10.4 |
| 45 | L1-worker | claudeopus46 | 366 | 1,817 | 2,183 | 1,330 | 5.4 |
| 46 | L1-worker | claudeopus46 | 2,106 | 6,707 | 8,813 | 5,408 | 21.5 |
| 47 | L1-worker | claudeopus46 | 366 | 6,185 | 6,551 | 4,296 | 17.6 |
| 48 | L1-worker | claudeopus46 | 787 | 112,219 | 113,006 | 777 | 10.4 |
| 49 | L0-main | claudeopus46 | 22,485 | 114,022 | 136,507 | 471 | 7.2 |
| 50 | L0-main | claudeopus46 | 22,518 | 113,263 | 135,781 | 1,680 | 16.0 |
| 51 | L0-main | claudeopus46 | 22,518 | 114,043 | 136,561 | 926 | 7.8 |
| 52 | L0-main | claudeopus46 | 22,518 | 114,816 | 137,334 | 1,055 | 7.6 |
| 53 | L0-main | claudeopus46 | 22,485 | 117,045 | 139,530 | 373 | 5.0 |
| 54 | L0-main | claudeopus46 | 22,518 | 116,284 | 138,802 | 1,580 | 15.6 |
| 55 | L0-main | claudeopus46 | 22,518 | 117,065 | 139,583 | 768 | 7.4 |
| 56 | L0-main | claudeopus46 | 22,485 | 118,146 | 140,631 | 473 | 5.8 |
| 57 | L0-main | claudeopus46 | 22,518 | 117,385 | 139,903 | 934 | 8.8 |
| 58 | L0-main | claudeopus46 | 22,518 | 118,113 | 140,631 | 1,013 | 8.5 |
| 59 | L0-main | claudeopus46 | 22,518 | 118,837 | 141,355 | 837 | 6.9 |
| 60 | L0-main | claudeopus46 | 22,518 | 119,612 | 142,130 | 832 | 7.3 |
| 61 | L0-main | claudeopus46 | 22,485 | 120,146 | 142,631 | 572 | 6.9 |
| 62 | L0-main | claudeopus46 | 22,518 | 119,384 | 141,902 | 716 | 7.6 |
| 63 | L0-main | claudeopus46 | 22,518 | 120,084 | 142,602 | 794 | 6.1 |
| 64 | L0-main | claudeopus46 | 22,518 | 120,836 | 143,354 | 849 | 6.5 |
| 65 | L0-main | claudeopus46 | 22,485 | 121,635 | 144,120 | 521 | 9.4 |
| 66 | L0-main | claudeopus46 | 22,518 | 120,873 | 143,391 | 930 | 17.2 |
| 67 | L0-main | claudeopus46 | 22,485 | 124,318 | 146,803 | 432 | 5.7 |
| 68 | L0-main | claudeopus46 | 22,518 | 123,556 | 146,074 | 1,532 | 12.2 |
| 69 | L0-main | claudeopus46 | 22,485 | 124,967 | 147,452 | 499 | 6.6 |
| 70 | L0-main | claudeopus46 | 22,518 | 124,205 | 146,723 | 1,644 | 12.6 |
| 71 | L0-main | claudeopus46 | 22,485 | 127,743 | 150,228 | 399 | 7.2 |
| 72 | L0-main | claudeopus46 | 22,518 | 126,981 | 149,499 | 1,724 | 13.3 |
| 73 | L0-main | claudeopus46 | 22,485 | 128,309 | 150,794 | 397 | 7.5 |
| 74 | L0-main | claudeopus46 | 22,518 | 127,547 | 150,065 | 2,705 | 21.4 |
| 75 | L0-main | claudeopus46 | 22,485 | 131,711 | 154,196 | 493 | 6.7 |
| 76 | L0-main | claudeopus46 | 22,518 | 130,949 | 153,467 | 9,034 | 65.3 |
| 77 | L0-main | claudeopus46 | 22,518 | 145,069 | 167,587 | 2,187 | 18.6 |
| 78 | L0-main | claudeopus46 | 22,485 | 147,988 | 170,473 | 493 | 7.3 |
| 79 | L0-main | claudeopus46 | 22,518 | 147,226 | 169,744 | 5,317 | 42.6 |
| 80 | L0-main | claudeopus46 | 22,518 | 157,958 | 180,476 | 2,133 | 19.6 |
| 81 | L0-main | claudeopus46 | 22,485 | 160,821 | 183,306 | 474 | 7.2 |
| 82 | L0-main | claudeopus46 | 22,518 | 160,059 | 182,577 | 5,744 | 43.4 |
| 83 | L0-main | claudeopus46 | 2,106 | 10,264 | 12,370 | 266 | 3.3 |
| 84 | L0-main | claudeopus46 | 366 | 789 | 1,155 | 252 | 2.9 |
| 85 | L0-main | claudeopus46 | 2,320 | 9,516 | 11,836 | 1,091 | 10.5 |
| 86 | L0-main | claudeopus46 | 366 | 1,528 | 1,894 | 1,023 | 4.0 |
| 87 | L0-main | claudeopus46 | 560 | 10,315 | 10,875 | 178 | 2.3 |
| 88 | L0-main | claudeopus46 | 1,156 | 11,765 | 12,921 | 1,040 | 8.1 |
| 89 | L0-main | claudeopus46 | 1,918 | 6,972 | 8,890 | 1,139 | 10.5 |

