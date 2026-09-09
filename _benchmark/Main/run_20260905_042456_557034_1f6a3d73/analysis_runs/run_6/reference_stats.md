# Reference Stats — analysis-agent

**Run started:** 2026-09-05 04:25:09
**Wall time (at last flush):** 461.7 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 25 | 414,116 | 530,134 | 35,832 | 944,250 | 37,770 | 290.0 | claudeopus46 |
| L1-worker | 40 | 487,925 | 165,084 | 37,731 | 653,009 | 16,325 | 292.2 | claudeopus46 |
| **TOTAL** | **65** | **902,041** | **695,218** | **73,563** | **1,597,259** | **24,573** | **582.2** | |

**Estimated tokens:** ~399,314 input + ~18,390 output = ~417,704 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_property_ids` | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| `resolve_property_ids` | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 5 | 4 | 22 | 22 | 2,417 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 11 | 4 | 4 | 29 | 50 | 3,112 |
| `search_blocks` | 9 | 1 | 1 | 2 | 3 | 10 | 154 |
| `block_search_adv` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml_parallel` | 2 | 1 | 3 | 0 | 1 | 1 | 0 |
| `list_session_files` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **19** | **16** | **13** | **10** | **55** | **83** | **5,683** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (11 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_2 |  | query_thermoml_parallel, resolve_compound_ids, search_blocks |
| GLOBcomp_1 |  | query_thermoml_parallel, resolve_compound_ids, search_blocks |
| GLOBcomp_30 | 1,2-dimethylbenzene | search_blocks |
| GLOBcomp_8 | toluene | search_blocks |
| GLOBcomp_268 | 2-pyrrolidinone | search_blocks |
| GLOBcomp_28 | 1,4-dimethylbenzene | search_blocks |
| GLOBcomp_5 | propan-1-ol | search_blocks |
| GLOBcomp_14 | benzene | search_blocks |
| GLOBcomp_65 | butyl ethanoate | search_blocks |
| GLOBcomp_32 | 1,3-dimethylbenzene | search_blocks |
| GLOBcomp_13 | cyclohexane | search_blocks |

#### Properties (12 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_28 |  | resolve_property_ids, search_blocks |
| GLOBprop_1 |  | query_thermoml_parallel, resolve_property_ids, search_blocks |
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

#### References (48 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_220 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_1483 |  | search_blocks |
| GLOBlit_2432 |  | search_blocks |
| GLOBlit_2825 |  | search_blocks |
| GLOBlit_3475 |  | search_blocks |
| GLOBlit_4415 |  | search_blocks |
| GLOBlit_5201 |  | search_blocks |
| GLOBlit_5473 |  | search_blocks |
| GLOBlit_7085 |  | search_blocks |
| GLOBlit_7178 |  | search_blocks |
| GLOBlit_7448 |  | search_blocks |
| GLOBlit_7676 |  | search_blocks |
| GLOBlit_8050 |  | search_blocks |
| GLOBlit_8888 |  | search_blocks |
| GLOBlit_9006 |  | search_blocks |
| GLOBlit_10159 |  | search_blocks |
| GLOBlit_10699 |  | search_blocks |
| GLOBlit_10866 |  | search_blocks |
| GLOBlit_11005 |  | search_blocks |
| GLOBlit_11136 |  | search_blocks |
| GLOBlit_11504 |  | search_blocks |
| GLOBlit_11792 |  | search_blocks |
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
| GLOBlit_92 |  | search_blocks |
| GLOBlit_106 |  | search_blocks |
| GLOBlit_276 |  | search_blocks |

#### Measurements (36 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_138 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBmeas_66 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_236 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_203 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_212 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_141 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_6 | Mass density, kg/m3 | search_blocks |
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
| GLOBmeas_55 | Excess molar volume, m3/mol | search_blocks |
| GLOBmeas_346 | Excess molar volume, m3/mol | search_blocks |
| GLOBmeas_1885 | Excess molar volume, m3/mol | search_blocks |

#### Phases (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | query_thermoml_parallel, search_blocks |
| GLOBphase_3 |  | search_blocks |
| GLOBphase_10 |  | search_blocks |

#### Variables (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | query_thermoml_parallel, search_blocks |
| GLOBvar_3 | Pressure, kPa | query_thermoml_parallel, search_blocks |
| GLOBvar_2 | Mole fraction | query_thermoml_parallel, search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |

#### Solvents (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | search_blocks |
| GLOBsolvent_2 |  | search_blocks |

#### Constraints (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | search_blocks |
| GLOBconstr_2 | Temperature, K | search_blocks |
| GLOBconstr_8 | Molality, mol/kg | search_blocks |
| GLOBconstr_22 | Volume fraction | search_blocks |
| GLOBconstr_3 | Mole fraction | search_blocks |
| GLOBconstr_4 | Frequency, MHz | search_blocks |

#### Block_Types (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | query_thermoml_parallel |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 11 |
| Unique Properties | 12 |
| Unique References | 48 |
| Unique Measurements | 36 |
| Unique Phases | 3 |
| Unique Variables | 5 |
| Unique Solvents | 2 |
| Unique Constraints | 6 |
| Unique Block_Types | 1 |
| Total DOIs | 48 |
| Unique parent blocks | 76 |
| Explicit block/subsystem targets | 76 |
| Subsystem targets | 0 |
| Target-matched data points | 6,493 |

---

## 3. DOI & Block References

**Unique DOIs:** 48  |  **Parent blocks:** 76  |  **Explicit targets:** 76  |  **Subsystems:** 0  |  **Target-matched datapoints:** 4,021

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1007/s10765-010-0717-9 | 2 | 32 | ternary | search_blocks |
| 10.1007/s10765-010-0861-2 | 2 | 62 | ternary | search_blocks |
| 10.1016/j.fluid.2004.11.019 | 1 | 810 | binary | query_thermoml_parallel, search_blocks |
| 10.1016/j.fluid.2005.06.011 | 6 | 60 | binary | search_blocks |
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
| 10.1016/j.fluid.2014.05.032 | 1 | 140 | binary | search_blocks |
| 10.1016/j.fluid.2014.07.022 | 2 | 14 | binary | search_blocks |
| 10.1016/j.fluid.2015.07.012 | 2 | 168 | binary | search_blocks |
| 10.1016/j.fluid.2016.08.030 | 1 | 4 | binary | search_blocks |
| 10.1016/j.fluid.2017.03.010 | 2 | 34 | binary | search_blocks |
| 10.1016/j.fluid.2017.09.005 | 2 | 144 | binary | search_blocks |
| 10.1016/j.fluid.2018.07.014 | 1 | 17 | binary | search_blocks |
| 10.1016/j.fluid.2019.03.019 | 2 | 32 | binary | search_blocks |
| 10.1016/j.jct.2004.07.019 | 1 | 565 | binary | search_blocks |
| 10.1016/j.jct.2005.06.018 | 1 | 27 | binary | search_blocks |
| 10.1016/j.jct.2006.08.002 | 4 | 326 | binary | search_blocks |
| 10.1016/j.jct.2007.05.004 | 2 | 74 | binary | search_blocks |
| 10.1016/j.jct.2011.10.009 | 1 | 70 | binary | search_blocks |
| 10.1016/j.jct.2012.08.009 | 1 | 14 | binary | search_blocks |
| 10.1016/j.jct.2013.08.020 | 4 | 34 | binary | search_blocks |
| 10.1016/j.jct.2014.05.020 | 1 | 30 | binary | search_blocks |
| 10.1016/j.jct.2015.06.024 | 2 | 80 | binary | search_blocks |
| 10.1016/j.jct.2017.07.021 | 1 | 24 | binary | search_blocks |
| 10.1016/j.jct.2018.02.022 | 1 | 244 | binary | search_blocks |
| 10.1016/j.jct.2019.02.027 | 1 | 9 | binary | search_blocks |
| 10.1021/acs.jced.6b01058 | 1 | 12 | binary | search_blocks |
| 10.1021/acs.jced.7b00299 | 1 | 2 | binary | search_blocks |
| 10.1021/acs.jced.8b00086 | 1 | 6 | binary | search_blocks |
| 10.1021/acs.jced.8b00939 | 1 | 9 | binary | search_blocks |
| 10.1021/je020173z | 1 | 24 | binary | search_blocks |
| 10.1021/je0601098 | 1 | 12 | binary | search_blocks |
| 10.1021/je060335h | 1 | 164 | binary | search_blocks |
| 10.1021/je4003515 | 1 | 23 | binary | search_blocks |
| 10.1021/je600565m | 1 | 18 | binary | search_blocks |
| 10.1021/je700300y | 1 | 84 | binary | search_blocks |
| 10.1021/je700618y | 1 | 15 | binary | search_blocks |
| 10.1021/je800150h | 1 | 108 | binary | search_blocks |
| 10.1021/je900064e | 1 | 10 | binary | search_blocks |
| 10.1021/je900743e | 1 | 15 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1007/s10765-010-0717-9 | PROPblock_6 | declared | 15 | ternary | — | search_blocks |
| 10.1007/s10765-010-0717-9 | PROPblock_8 | declared | 17 | ternary | — | search_blocks |
| 10.1007/s10765-010-0861-2 | PROPblock_11 | declared | 31 | ternary | — | search_blocks |
| 10.1007/s10765-010-0861-2 | PROPblock_13 | declared | 31 | ternary | — | search_blocks |
| 10.1016/j.fluid.2004.11.019 | PROPblock_2 | declared | 810 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1016/j.fluid.2005.06.011 | PROPblock_16 | declared | 10 | binary | — | search_blocks |
| 10.1016/j.fluid.2005.06.011 | PROPblock_18 | declared | 9 | binary | — | search_blocks |
| 10.1016/j.fluid.2005.06.011 | PROPblock_20 | declared | 10 | binary | — | search_blocks |
| 10.1016/j.fluid.2005.06.011 | PROPblock_22 | declared | 10 | binary | — | search_blocks |
| 10.1016/j.fluid.2005.06.011 | PROPblock_24 | declared | 10 | binary | — | search_blocks |
| 10.1016/j.fluid.2005.06.011 | PROPblock_26 | declared | 11 | binary | — | search_blocks |
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
| 10.1016/j.fluid.2014.05.032 | PROPblock_1 | declared | 140 | binary | — | search_blocks |
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
| 10.1016/j.jct.2004.07.019 | PROPblock_2 | declared | 565 | binary | — | search_blocks |
| 10.1016/j.jct.2005.06.018 | PROPblock_4 | declared | 27 | binary | — | search_blocks |
| 10.1016/j.jct.2006.08.002 | PROPblock_1 | declared | 25 | binary | — | search_blocks |
| 10.1016/j.jct.2006.08.002 | PROPblock_2 | declared | 19 | binary | — | search_blocks |
| 10.1016/j.jct.2006.08.002 | PROPblock_3 | declared | 4 | binary | — | search_blocks |
| 10.1016/j.jct.2006.08.002 | PROPblock_4 | declared | 278 | binary | — | search_blocks |
| 10.1016/j.jct.2007.05.004 | PROPblock_11 | declared | 37 | binary | — | search_blocks |
| 10.1016/j.jct.2007.05.004 | PROPblock_12 | declared | 37 | binary | — | search_blocks |
| 10.1016/j.jct.2011.10.009 | PROPblock_3 | declared | 70 | binary | — | search_blocks |
| 10.1016/j.jct.2012.08.009 | PROPblock_18 | declared | 14 | binary | — | search_blocks |
| 10.1016/j.jct.2013.08.020 | PROPblock_10 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.jct.2013.08.020 | PROPblock_11 | declared | 1 | binary | — | search_blocks |
| 10.1016/j.jct.2013.08.020 | PROPblock_12 | declared | 1 | binary | — | search_blocks |
| 10.1016/j.jct.2013.08.020 | PROPblock_9 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.jct.2014.05.020 | PROPblock_1 | declared | 30 | binary | — | search_blocks |
| 10.1016/j.jct.2015.06.024 | PROPblock_7 | declared | 40 | binary | — | search_blocks |
| 10.1016/j.jct.2015.06.024 | PROPblock_8 | declared | 40 | binary | — | search_blocks |
| 10.1016/j.jct.2017.07.021 | PROPblock_3 | declared | 24 | binary | — | search_blocks |
| 10.1016/j.jct.2018.02.022 | PROPblock_19 | declared | 244 | binary | — | search_blocks |
| 10.1016/j.jct.2019.02.027 | PROPblock_21 | declared | 9 | binary | — | search_blocks |
| 10.1021/acs.jced.6b01058 | PROPblock_7 | declared | 12 | binary | — | search_blocks |
| 10.1021/acs.jced.7b00299 | PROPblock_10 | declared | 2 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00086 | PROPblock_46 | declared | 6 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00939 | PROPblock_17 | declared | 9 | binary | — | search_blocks |
| 10.1021/je020173z | PROPblock_5 | declared | 24 | binary | — | search_blocks |
| 10.1021/je0601098 | PROPblock_20 | declared | 12 | binary | — | search_blocks |
| 10.1021/je060335h | PROPblock_1 | declared | 164 | binary | — | search_blocks |
| 10.1021/je4003515 | PROPblock_7 | declared | 23 | binary | — | search_blocks |
| 10.1021/je600565m | PROPblock_6 | declared | 18 | binary | — | search_blocks |
| 10.1021/je700300y | PROPblock_7 | declared | 84 | binary | — | search_blocks |
| 10.1021/je700618y | PROPblock_9 | declared | 15 | binary | — | search_blocks |
| 10.1021/je800150h | PROPblock_9 | declared | 108 | binary | — | search_blocks |
| 10.1021/je900064e | PROPblock_6 | declared | 10 | binary | — | search_blocks |
| 10.1021/je900743e | PROPblock_3 | declared | 15 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 1 | `query_thermoml_parallel` | queries=[{'label': 'excess_volume_dir… | 132 | — | — | 0.0 |
| 2 | 1 | `resolve_compound_ids` | purpose=Find compound IDs for ethanol…, queries=['… | 195 | KEEP ←in 278 | 195 | 3.4 |
| 3 | 2 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Resolve ethanol and… | 250 | KEEP ←in 278 | 250 | 3.8 |
| 4 | 2 | `resolve_property_ids` | purpose=Find the global ID for excess…, queries=['… | 263 | KEEP ←in 227 | 263 | 4.6 |
| 5 | 3 | `resolve_property_ids` | limit=5, min_score=80, purpose=Confirm property ID… | 273 | KEEP ←in 218 | 273 | 8.3 |
| 6 | 4 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=50, p… | 996 | DISCARD ←in 39 | 938 | 16.5 |
| 7 | 5 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=50, p… | 539 | KEEP ←in 14,080 | 539 | 16.6 |
| 8 | 6 | `inspect_block_table` | block_number=PROPblock_2, literature=GLOBlit_220, … | 359 | — | — | 0.1 |
| 9 | 5 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=50, p… | 1,155 | DISCARD ←in 39 | 1097 | 20.1 |
| 10 | 7 | `inspect_block_table` | block_number=PROPblock_2, literature=GLOBlit_220, … | 1,888 | — | — | 0.1 |
| 11 | 6 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=50, p… | 978 | KEEP ←in 30,867 | 814 | 20.2 |
| 12 | 7 | `search_blocks` | limit=10, property=GLOBprop_28, purpose=Check if e… | 1,244 | KEEP ←in 6,974 | 1148 | 12.3 |
| 13 | 8 | `block_search_adv` | compounds=['REQUIRE GLOBcomp_2 AS ethan…, explanat… | 898 | DISCARD ←in 800 | 837 | 16.8 |
| 14 | 2 | `query_thermoml_parallel` | queries=[{'label': 'excess_volume_dir… | 20,635 | — | — | 172.1 |
| 15 | 5 | `inspect_block` | block_number=PROPblock_2, doi=10.1016/j.fluid.2004… | 1,374 | — | — | 0.1 |
| 16 | 9 | `fit_block_derived` | block_number=PROPblock_2, composition_hint=mole_fr… | 239 | — | — | 0.1 |
| 17 | 11 | `fit_block_derived` | block_number=PROPblock_2, composition_hint=mole_fr… | 963 | — | — | 1.8 |
| 18 | 14 | `predict_from_rk` | coeffs=[-4.98777e-06, 2.71547e-06, -…, mixing_rule… | 206 | — | — | 0.0 |
| 19 | 15 | `list_session_files` |  | 1,689 | — | — | 0.0 |
| | | **TOTAL (19 tools)** | | **34,276** | | **6,354** | **296.9** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 22,518 | 750 | 23,268 | 1,557 | 10.1 |
| 2 | L0-main | claudeopus46 | 22,518 | 1,208 | 23,726 | 1,376 | 8.8 |
| 3 | L1-worker | claudeopus46 | 24,095 | 962 | 25,057 | 691 | 5.6 |
| 4 | L1-worker | claudeopus46 | 24,095 | 852 | 24,947 | 596 | 6.4 |
| 5 | L1-worker | claudeopus46 | 3,767 | 430 | 4,197 | 324 | 3.3 |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,007 | 26,102 | 576 | 4.1 |
| 7 | L1-worker | claudeopus46 | 3,767 | 467 | 4,234 | 406 | 3.6 |
| 8 | L1-worker | claudeopus46 | 24,095 | 1,326 | 25,421 | 713 | 5.4 |
| 9 | L1-worker | claudeopus46 | 3,767 | 396 | 4,163 | 395 | 4.5 |
| 10 | L1-worker | claudeopus46 | 24,095 | 1,658 | 25,753 | 1,011 | 7.6 |
| 11 | L1-worker | claudeopus46 | 3,767 | 368 | 4,135 | 297 | 3.8 |
| 12 | L1-worker | claudeopus46 | 24,095 | 1,886 | 25,981 | 818 | 5.9 |
| 13 | L1-worker | claudeopus46 | 3,767 | 670 | 4,437 | 487 | 4.3 |
| 14 | L1-worker | claudeopus46 | 24,095 | 2,615 | 26,710 | 664 | 7.0 |
| 15 | L1-worker | claudeopus46 | 24,095 | 2,240 | 26,335 | 750 | 5.9 |
| 16 | L1-worker | claudeopus46 | 24,095 | 2,968 | 27,063 | 700 | 5.2 |
| 17 | L1-worker | claudeopus46 | 3,767 | 556 | 4,323 | 1,216 | 9.2 |
| 18 | L1-worker | claudeopus46 | 24,095 | 3,599 | 27,694 | 861 | 6.0 |
| 19 | L1-worker | claudeopus46 | 3,767 | 14,545 | 18,312 | 1,830 | 15.4 |
| 20 | L1-worker | claudeopus46 | 24,095 | 3,482 | 27,577 | 2,217 | 16.3 |
| 21 | L1-worker | claudeopus46 | 3,767 | 471 | 4,238 | 1,477 | 9.9 |
| 22 | L1-worker | claudeopus46 | 24,095 | 4,229 | 28,324 | 794 | 6.2 |
| 23 | L1-worker | claudeopus46 | 24,095 | 5,114 | 29,209 | 843 | 6.2 |
| 24 | L1-worker | claudeopus46 | 24,095 | 6,507 | 30,602 | 2,086 | 16.7 |
| 25 | L1-worker | claudeopus46 | 3,767 | 31,304 | 35,071 | 1,806 | 13.7 |
| 26 | L1-worker | claudeopus46 | 24,095 | 6,454 | 30,549 | 1,008 | 6.9 |
| 27 | L1-worker | claudeopus46 | 24,095 | 11,756 | 35,851 | 3,155 | 21.9 |
| 28 | L1-worker | claudeopus46 | 3,767 | 7,311 | 11,078 | 1,399 | 11.9 |
| 29 | L1-worker | claudeopus46 | 2,320 | 2,194 | 4,514 | 741 | 4.4 |
| 30 | L1-worker | claudeopus46 | 627 | 2,074 | 2,701 | 807 | 5.2 |
| 31 | L1-worker | claudeopus46 | 2,106 | 3,277 | 5,383 | 986 | 5.9 |
| 32 | L1-worker | claudeopus46 | 366 | 1,178 | 1,544 | 701 | 3.5 |
| 33 | L1-worker | claudeopus46 | 366 | 1,763 | 2,129 | 612 | 3.8 |
| 34 | L1-worker | claudeopus46 | 24,095 | 8,018 | 32,113 | 1,389 | 9.6 |
| 35 | L1-worker | claudeopus46 | 787 | 12,376 | 13,163 | 597 | 7.3 |
| 36 | L1-worker | claudeopus46 | 3,767 | 1,018 | 4,785 | 1,118 | 8.4 |
| 37 | L1-worker | claudeopus46 | 24,095 | 9,393 | 33,488 | 1,844 | 14.0 |
| 38 | L1-worker | claudeopus46 | 2,106 | 2,354 | 4,460 | 92 | 1.9 |
| 39 | L1-worker | claudeopus46 | 2,320 | 1,381 | 3,701 | 574 | 3.9 |
| 40 | L1-worker | claudeopus46 | 366 | 869 | 1,235 | 67 | 1.9 |
| 41 | L1-worker | claudeopus46 | 627 | 1,261 | 1,888 | 547 | 4.5 |
| 42 | L1-worker | claudeopus46 | 787 | 3,755 | 4,542 | 536 | 5.0 |
| 43 | L0-main | claudeopus46 | 22,518 | 23,630 | 46,148 | 1,108 | 11.0 |
| 44 | L0-main | claudeopus46 | 22,518 | 24,336 | 46,854 | 583 | 4.7 |
| 45 | L0-main | claudeopus46 | 22,518 | 25,016 | 47,534 | 465 | 4.0 |
| 46 | L0-main | claudeopus46 | 22,518 | 26,549 | 49,067 | 1,156 | 8.4 |
| 47 | L0-main | claudeopus46 | 22,518 | 27,264 | 49,782 | 888 | 6.8 |
| 48 | L0-main | claudeopus46 | 22,518 | 27,948 | 50,466 | 1,011 | 7.5 |
| 49 | L0-main | claudeopus46 | 22,518 | 28,756 | 51,274 | 927 | 6.6 |
| 50 | L0-main | claudeopus46 | 22,518 | 28,384 | 50,902 | 1,053 | 7.8 |
| 51 | L0-main | claudeopus46 | 22,518 | 29,068 | 51,586 | 949 | 6.9 |
| 52 | L0-main | claudeopus46 | 22,518 | 31,536 | 54,054 | 961 | 8.2 |
| 53 | L0-main | claudeopus46 | 22,518 | 32,220 | 54,738 | 776 | 5.5 |
| 54 | L0-main | claudeopus46 | 22,518 | 32,879 | 55,397 | 859 | 5.5 |
| 55 | L0-main | claudeopus46 | 22,518 | 32,842 | 55,360 | 3,168 | 36.9 |
| 56 | L0-main | claudeopus46 | 22,518 | 34,872 | 57,390 | 6,745 | 48.2 |
| 57 | L0-main | claudeopus46 | 22,518 | 44,908 | 67,426 | 4,567 | 35.6 |
| 58 | L0-main | claudeopus46 | 22,518 | 53,245 | 75,763 | 3,252 | 28.3 |
| 59 | L0-main | claudeopus46 | 2,106 | 4,230 | 6,336 | 154 | 2.4 |
| 60 | L0-main | claudeopus46 | 366 | 677 | 1,043 | 195 | 2.4 |
| 61 | L0-main | claudeopus46 | 2,320 | 3,381 | 5,701 | 1,170 | 10.2 |
| 62 | L0-main | claudeopus46 | 366 | 1,607 | 1,973 | 1,125 | 5.5 |
| 63 | L0-main | claudeopus46 | 560 | 3,902 | 4,462 | 106 | 2.2 |
| 64 | L0-main | claudeopus46 | 1,156 | 4,700 | 5,856 | 561 | 6.0 |
| 65 | L0-main | claudeopus46 | 1,918 | 6,226 | 8,144 | 1,120 | 10.5 |

