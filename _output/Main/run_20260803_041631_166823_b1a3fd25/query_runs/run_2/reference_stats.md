# Reference Stats — query-agent

**Run started:** 2026-08-03 04:22:52
**Wall time (at last flush):** 1,094.1 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 6 | 22,485 | 325,740 | 36,287 | 348,225 | 58,037 | 173.4 | claudeopus46 |
| L1-worker | 56 | 348,285 | 3,004,684 | 153,366 | 3,352,969 | 59,874 | 883.4 | claudeopus46 |
| **TOTAL** | **62** | **370,770** | **3,330,424** | **189,653** | **3,701,194** | **59,696** | **1056.8** | |

**Estimated tokens:** ~925,298 input + ~47,413 output = ~972,711 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `search_blocks` | 2 | 1 | 6 | 3 | 14 | 14 | 534 |
| `search_blocks` | 2 | 1 | 6 | 5 | 27 | 29 | 2,895 |
| `search_blocks` | 2 | 1 | 2 | 2 | 3 | 3 | 18 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 1 | 3 | 1 | 1 | 6 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 5 | 1 | 6 | 6 | 232 |
| `search_blocks` | 2 | 1 | 7 | 3 | 17 | 18 | 1,610 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 3 | 1 | 2 | 2 | 240 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 5 | 1 | 6 | 6 | 232 |
| `search_blocks` | 2 | 1 | 7 | 3 | 17 | 18 | 1,610 |
| `search_blocks` | 2 | 1 | 3 | 1 | 2 | 2 | 240 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 3 | 2 | 7 | 7 | 302 |
| `search_blocks` | 2 | 1 | 4 | 3 | 16 | 16 | 908 |
| `search_blocks` | 2 | 1 | 3 | 1 | 4 | 4 | 125 |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 135 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_system_summary` | 2 | 0 | 0 | 0 | 16 | 29 | 1,601 |
| `search_blocks` | 2 | 2 | 4 | 2 | 9 | 12 | 655 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **32** | **16** | **61** | **32** | **148** | **168** | **11,343** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### References (77 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_1742 |  | search_blocks |
| GLOBlit_2092 |  | search_blocks |
| GLOBlit_2825 |  | search_blocks |
| GLOBlit_5201 |  | search_blocks |
| GLOBlit_7178 |  | search_blocks |
| GLOBlit_7448 |  | search_blocks |
| GLOBlit_7676 |  | search_blocks |
| GLOBlit_8949 |  | search_blocks |
| GLOBlit_10159 |  | search_blocks |
| GLOBlit_10699 |  | search_blocks |
| GLOBlit_11005 |  | search_blocks |
| GLOBlit_11136 |  | search_blocks |
| GLOBlit_11459 |  | search_blocks |
| GLOBlit_11792 |  | search_blocks |
| GLOBlit_220 |  | search_blocks |
| GLOBlit_1483 |  | search_blocks |
| GLOBlit_2432 |  | search_blocks |
| GLOBlit_2732 |  | search_blocks |
| GLOBlit_3475 |  | search_blocks |
| GLOBlit_4415 |  | search_blocks |
| GLOBlit_5473 |  | search_blocks |
| GLOBlit_7085 |  | search_blocks |
| GLOBlit_7629 |  | search_blocks |
| GLOBlit_8050 |  | search_blocks |
| GLOBlit_8888 |  | search_blocks |
| GLOBlit_9006 |  | search_blocks |
| GLOBlit_10866 |  | search_blocks |
| GLOBlit_11504 |  | search_blocks |
| GLOBlit_6628 |  | search_blocks |
| GLOBlit_7794 |  | search_blocks |
| GLOBlit_7483 |  | search_blocks |
| GLOBlit_5533 |  | search_blocks |
| GLOBlit_8869 |  | search_blocks |
| GLOBlit_9571 |  | search_blocks |
| GLOBlit_385 |  | search_blocks |
| GLOBlit_462 |  | search_blocks |
| GLOBlit_895 |  | search_blocks |
| GLOBlit_8155 |  | search_blocks |
| GLOBlit_8254 |  | search_blocks |
| GLOBlit_8424 |  | search_blocks |
| GLOBlit_2395 |  | search_blocks |
| GLOBlit_2656 |  | search_blocks |
| GLOBlit_6951 |  | search_blocks |
| GLOBlit_8038 |  | search_blocks |
| GLOBlit_8106 |  | search_blocks |
| GLOBlit_11186 |  | search_blocks |
| GLOBlit_11506 |  | search_blocks |
| GLOBlit_1223 |  | search_blocks |
| GLOBlit_2268 |  | search_blocks |
| GLOBlit_2831 |  | search_blocks |
| GLOBlit_5254 |  | search_blocks |
| GLOBlit_5274 |  | search_blocks |
| GLOBlit_6630 |  | search_blocks |
| GLOBlit_6686 |  | search_blocks |
| GLOBlit_7228 |  | search_blocks |
| GLOBlit_7440 |  | search_blocks |
| GLOBlit_10102 |  | search_blocks |
| GLOBlit_3286 |  | search_blocks |
| GLOBlit_4021 |  | search_blocks |
| GLOBlit_8553 |  | search_blocks |
| GLOBlit_1283 |  | search_blocks |
| GLOBlit_10109 |  | search_system_summary |
| GLOBlit_2844 |  | search_blocks, search_system_summary |
| GLOBlit_2781 |  | search_blocks, search_system_summary |
| GLOBlit_10766 |  | search_system_summary |
| GLOBlit_2584 |  | search_blocks, search_system_summary |
| GLOBlit_2842 |  | search_blocks, search_system_summary |
| GLOBlit_11018 |  | search_blocks, search_system_summary |
| GLOBlit_11517 |  | search_blocks, search_system_summary |
| GLOBlit_10024 |  | search_system_summary |
| GLOBlit_5953 |  | search_blocks, search_system_summary |
| GLOBlit_10215 |  | search_system_summary |
| GLOBlit_663 |  | search_system_summary |
| GLOBlit_2652 |  | search_blocks, search_system_summary |
| GLOBlit_7713 |  | search_blocks, search_system_summary |
| GLOBlit_9547 |  | search_system_summary |
| GLOBlit_5958 |  | search_system_summary |

#### Compounds (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_2 | ethanol | search_blocks |
| GLOBcomp_1 | water | search_blocks, search_system_summary |
| GLOBcomp_4 | methanol | search_blocks |
| GLOBcomp_24 | 1,2-ethanediol | search_blocks |
| GLOBcomp_31 |  | search_blocks, search_system_summary |

#### Properties (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_4 | Viscosity, Pa*s | search_blocks |
| GLOBprop_1 | Mass density, kg/m3 | search_blocks |
| GLOBprop_13 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBprop_18 | Electrical conductivity, S/m | search_blocks |
| GLOBprop_28 | Excess molar volume, m3/mol | search_blocks |

#### Measurements (36 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_4 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_140 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_11 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_8 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_205 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_988 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_165 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_142 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_138 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_66 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_1497 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_236 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_203 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_212 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_153 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_141 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_6 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_36 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBmeas_19 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBmeas_14 | Electrical conductivity, S/m | search_blocks |
| GLOBmeas_2135 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_271 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_1494 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_170 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_280 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_29 | Excess molar volume, m3/mol | search_blocks |
| GLOBmeas_207 | Excess molar volume, m3/mol | search_blocks |
| GLOBmeas_227 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_143 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_184 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_192 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBmeas_569 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBmeas_147 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_495 | Mass density, kg/m3 | search_blocks |

#### Phases (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks |
| GLOBphase_3 |  | search_blocks |
| GLOBphase_10 |  | search_blocks |

#### Variables (7 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_3 | Pressure, kPa | search_blocks |
| GLOBvar_2 | Mole fraction | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |
| GLOBvar_18 | Volume fraction | search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |
| GLOBvar_15 | Mass ratio of solute to solvent | search_blocks |

#### Constraints (7 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | search_blocks |
| GLOBconstr_8 | Molality, mol/kg | search_blocks |
| GLOBconstr_2 | Temperature, K | search_blocks |
| GLOBconstr_3 | Mole fraction | search_blocks |
| GLOBconstr_22 | Volume fraction | search_blocks |
| GLOBconstr_5 | Mass fraction | search_blocks |
| GLOBconstr_4 | Frequency, MHz | search_blocks |

#### Solvents (4 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | search_blocks |
| GLOBsolvent_2 |  | search_blocks |
| GLOBsolvent_3 |  | search_blocks |
| GLOBsolvent_12 |  | search_blocks |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique References | 77 |
| Unique Compounds | 5 |
| Unique Properties | 5 |
| Unique Measurements | 36 |
| Unique Phases | 3 |
| Unique Variables | 7 |
| Unique Constraints | 7 |
| Unique Solvents | 4 |
| Total DOIs | 70 |
| Unique parent blocks | 113 |
| Explicit block/subsystem targets | 113 |
| Subsystem targets | 0 |
| Target-matched data points | 9,742 |

---

## 3. DOI & Block References

**Unique DOIs:** 70  |  **Parent blocks:** 113  |  **Explicit targets:** 113  |  **Subsystems:** 0  |  **Target-matched datapoints:** 7,660

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2004.11.019 | 1 | 810 | binary | search_blocks |
| 10.1016/j.fluid.2006.05.007 | 1 | 45 | binary | search_blocks |
| 10.1016/j.fluid.2006.12.005 | 2 | 10 | binary | search_blocks |
| 10.1016/j.fluid.2010.10.005 | 2 | 68 | binary | search_blocks |
| 10.1016/j.fluid.2013.01.025 | 1 | 85 | binary | search_blocks |
| 10.1016/j.fluid.2013.06.041 | 1 | 135 | binary | search_blocks |
| 10.1016/j.fluid.2014.05.032 | 1 | 140 | binary | search_blocks |
| 10.1016/j.fluid.2015.07.012 | 4 | 332 | binary | search_blocks |
| 10.1016/j.fluid.2017.09.005 | 4 | 288 | binary | search_blocks |
| 10.1016/j.fluid.2018.11.035 | 1 | 6 | binary | search_blocks |
| 10.1016/j.jct.2004.03.011 | 1 | 206 | binary | search_blocks |
| 10.1016/j.jct.2004.07.019 | 2 | 1,161 | binary | search_blocks |
| 10.1016/j.jct.2005.07.012 | 1 | 96 | binary | search_blocks |
| 10.1016/j.jct.2006.01.007 | 1 | 6 | binary | search_blocks |
| 10.1016/j.jct.2006.01.011 | 2 | 20 | binary | search_blocks |
| 10.1016/j.jct.2006.08.002 | 3 | 301 | binary | search_blocks |
| 10.1016/j.jct.2006.12.012 | 2 | 240 | binary | search_blocks |
| 10.1016/j.jct.2007.05.004 | 4 | 152 | binary | search_blocks |
| 10.1016/j.jct.2007.05.010 | 1 | 10 | binary | search_blocks |
| 10.1016/j.jct.2007.06.007 | 1 | 40 | binary | search_blocks |
| 10.1016/j.jct.2007.06.010 | 1 | 92 | binary | search_blocks |
| 10.1016/j.jct.2010.09.003 | 1 | 54 | binary | search_blocks |
| 10.1016/j.jct.2011.10.009 | 1 | 70 | binary | search_blocks |
| 10.1016/j.jct.2013.10.010 | 1 | 4 | binary | search_blocks |
| 10.1016/j.jct.2015.06.024 | 1 | 40 | binary | search_blocks |
| 10.1016/j.jct.2018.02.022 | 4 | 652 | binary | search_blocks |
| 10.1016/j.jct.2018.05.016 | 1 | 12 | binary | search_blocks |
| 10.1016/j.jct.2018.06.021 | 1 | 15 | binary | search_blocks |
| 10.1016/j.jct.2019.02.027 | 1 | 9 | binary | search_blocks |
| 10.1016/j.jct.2019.05.013 | 2 | 24 | binary | search_blocks |
| 10.1016/j.tca.2011.08.013 | 2 | 32 | binary | search_blocks |
| 10.1021/acs.jced.5b00485 | 1 | 2 | binary | search_blocks |
| 10.1021/acs.jced.5b00498 | 1 | 70 | binary | search_blocks |
| 10.1021/acs.jced.5b00662 | 1 | 30 | binary | search_blocks |
| 10.1021/acs.jced.6b00526 | 2 | 166 | binary | search_blocks |
| 10.1021/acs.jced.6b01058 | 2 | 24 | binary | search_blocks |
| 10.1021/acs.jced.7b00299 | 2 | 4 | binary | search_blocks |
| 10.1021/acs.jced.7b00501 | 1 | 32 | binary | search_blocks |
| 10.1021/acs.jced.8b00058 | 1 | 20 | binary | search_blocks |
| 10.1021/acs.jced.8b00086 | 3 | 18 | binary | search_blocks |
| 10.1021/acs.jced.8b00181 | 1 | 6 | binary | search_blocks |
| 10.1021/acs.jced.8b00723 | 2 | 6 | binary | search_blocks |
| 10.1021/acs.jced.8b00939 | 2 | 18 | binary | search_blocks |
| 10.1021/acs.jced.8b01048 | 1 | 9 | binary | search_blocks |
| 10.1021/acs.jced.9b00026 | 1 | 10 | binary | search_blocks |
| 10.1021/je020140j | 2 | 154 | binary | search_blocks |
| 10.1021/je020173z | 1 | 24 | binary | search_blocks |
| 10.1021/je025610o | 2 | 60 | binary | search_blocks |
| 10.1021/je0301500 | 1 | 5 | binary | search_blocks |
| 10.1021/je034101z | 1 | 401 | binary | search_blocks |
| 10.1021/je049691v | 1 | 180 | binary | search_blocks |
| 10.1021/je049955d | 1 | 15 | binary | search_blocks |
| 10.1021/je0600810 | 2 | 18 | binary | search_blocks |
| 10.1021/je0601098 | 2 | 24 | binary | search_blocks |
| 10.1021/je060219e | 1 | 26 | binary | search_blocks |
| 10.1021/je060335h | 1 | 164 | binary | search_blocks |
| 10.1021/je2003622 | 2 | 32 | binary | search_blocks |
| 10.1021/je4001203 | 1 | 138 | binary | search_blocks |
| 10.1021/je4003515 | 2 | 48 | binary | search_blocks |
| 10.1021/je600565m | 2 | 35 | binary | search_blocks |
| 10.1021/je700300y | 2 | 168 | binary | search_blocks |
| 10.1021/je700618y | 2 | 30 | binary | search_blocks |
| 10.1021/je700645p | 1 | 70 | binary | search_blocks |
| 10.1021/je800150h | 2 | 216 | binary | search_blocks |
| 10.1021/je800271e | 2 | 104 | binary | search_blocks |
| 10.1021/je800942u | 2 | 36 | binary | search_blocks |
| 10.1021/je900064e | 1 | 10 | binary | search_blocks |
| 10.1021/je9000697 | 2 | 32 | binary | search_blocks |
| 10.1021/je9001027 | 2 | 70 | binary | search_blocks |
| 10.1021/je900743e | 2 | 30 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2004.11.019 | PROPblock_2 | declared | 810 | binary | — | search_blocks |
| 10.1016/j.fluid.2006.05.007 | PROPblock_1 | declared | 45 | binary | — | search_blocks |
| 10.1016/j.fluid.2006.12.005 | PROPblock_3 | declared | 8 | binary | — | search_blocks |
| 10.1016/j.fluid.2006.12.005 | PROPblock_4 | declared | 2 | binary | — | search_blocks |
| 10.1016/j.fluid.2010.10.005 | PROPblock_1 | declared | 34 | binary | — | search_blocks |
| 10.1016/j.fluid.2010.10.005 | PROPblock_2 | declared | 34 | binary | — | search_blocks |
| 10.1016/j.fluid.2013.01.025 | PROPblock_2 | declared | 85 | binary | — | search_blocks |
| 10.1016/j.fluid.2013.06.041 | PROPblock_11 | declared | 135 | binary | — | search_blocks |
| 10.1016/j.fluid.2014.05.032 | PROPblock_1 | declared | 140 | binary | — | search_blocks |
| 10.1016/j.fluid.2015.07.012 | PROPblock_1 | declared | 80 | binary | — | search_blocks |
| 10.1016/j.fluid.2015.07.012 | PROPblock_2 | declared | 84 | binary | — | search_blocks |
| 10.1016/j.fluid.2015.07.012 | PROPblock_3 | declared | 84 | binary | — | search_blocks |
| 10.1016/j.fluid.2015.07.012 | PROPblock_4 | declared | 84 | binary | — | search_blocks |
| 10.1016/j.fluid.2017.09.005 | PROPblock_1 | declared | 72 | binary | — | search_blocks |
| 10.1016/j.fluid.2017.09.005 | PROPblock_2 | declared | 72 | binary | — | search_blocks |
| 10.1016/j.fluid.2017.09.005 | PROPblock_3 | declared | 72 | binary | — | search_blocks |
| 10.1016/j.fluid.2017.09.005 | PROPblock_4 | declared | 72 | binary | — | search_blocks |
| 10.1016/j.fluid.2018.11.035 | PROPblock_2 | declared | 6 | binary | — | search_blocks |
| 10.1016/j.jct.2004.03.011 | PROPblock_1 | declared | 206 | binary | — | search_blocks |
| 10.1016/j.jct.2004.07.019 | PROPblock_1 | declared | 596 | binary | — | search_blocks |
| 10.1016/j.jct.2004.07.019 | PROPblock_2 | declared | 565 | binary | — | search_blocks |
| 10.1016/j.jct.2005.07.012 | PROPblock_8 | declared | 96 | binary | — | search_blocks |
| 10.1016/j.jct.2006.01.007 | PROPblock_4 | declared | 6 | binary | — | search_blocks |
| 10.1016/j.jct.2006.01.011 | PROPblock_12 | declared | 10 | binary | — | search_blocks |
| 10.1016/j.jct.2006.01.011 | PROPblock_13 | declared | 10 | binary | — | search_blocks |
| 10.1016/j.jct.2006.08.002 | PROPblock_2 | declared | 19 | binary | — | search_blocks |
| 10.1016/j.jct.2006.08.002 | PROPblock_3 | declared | 4 | binary | — | search_blocks |
| 10.1016/j.jct.2006.08.002 | PROPblock_4 | declared | 278 | binary | — | search_blocks |
| 10.1016/j.jct.2006.12.012 | PROPblock_3 | declared | 120 | binary | — | search_blocks |
| 10.1016/j.jct.2006.12.012 | PROPblock_4 | declared | 120 | binary | — | search_blocks |
| 10.1016/j.jct.2007.05.004 | PROPblock_10 | declared | 39 | binary | — | search_blocks |
| 10.1016/j.jct.2007.05.004 | PROPblock_11 | declared | 37 | binary | — | search_blocks |
| 10.1016/j.jct.2007.05.004 | PROPblock_12 | declared | 37 | binary | — | search_blocks |
| 10.1016/j.jct.2007.05.004 | PROPblock_9 | declared | 39 | binary | — | search_blocks |
| 10.1016/j.jct.2007.05.010 | PROPblock_10 | declared | 10 | binary | — | search_blocks |
| 10.1016/j.jct.2007.06.007 | PROPblock_6 | declared | 40 | binary | — | search_blocks |
| 10.1016/j.jct.2007.06.010 | PROPblock_4 | declared | 92 | binary | — | search_blocks |
| 10.1016/j.jct.2010.09.003 | PROPblock_4 | declared | 54 | binary | — | search_blocks |
| 10.1016/j.jct.2011.10.009 | PROPblock_3 | declared | 70 | binary | — | search_blocks |
| 10.1016/j.jct.2013.10.010 | PROPblock_2 | declared | 4 | binary | — | search_blocks |
| 10.1016/j.jct.2015.06.024 | PROPblock_7 | declared | 40 | binary | — | search_blocks |
| 10.1016/j.jct.2018.02.022 | PROPblock_19 | declared | 244 | binary | — | search_blocks |
| 10.1016/j.jct.2018.02.022 | PROPblock_21 | declared | 100 | binary | — | search_blocks |
| 10.1016/j.jct.2018.02.022 | PROPblock_22 | declared | 224 | binary | — | search_blocks |
| 10.1016/j.jct.2018.02.022 | PROPblock_24 | declared | 84 | binary | — | search_blocks |
| 10.1016/j.jct.2018.05.016 | PROPblock_7 | declared | 12 | binary | — | search_blocks |
| 10.1016/j.jct.2018.06.021 | PROPblock_10 | declared | 15 | binary | — | search_blocks |
| 10.1016/j.jct.2019.02.027 | PROPblock_21 | declared | 9 | binary | — | search_blocks |
| 10.1016/j.jct.2019.05.013 | PROPblock_2 | declared | 12 | binary | — | search_blocks |
| 10.1016/j.jct.2019.05.013 | PROPblock_3 | declared | 12 | binary | — | search_blocks |
| 10.1016/j.tca.2011.08.013 | PROPblock_10 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.tca.2011.08.013 | PROPblock_12 | declared | 16 | binary | — | search_blocks |
| 10.1021/acs.jced.5b00485 | PROPblock_8 | declared | 2 | binary | — | search_blocks |
| 10.1021/acs.jced.5b00498 | PROPblock_1 | declared | 70 | binary | — | search_blocks |
| 10.1021/acs.jced.5b00662 | PROPblock_55 | declared | 30 | binary | — | search_blocks |
| 10.1021/acs.jced.6b00526 | PROPblock_16 | declared | 133 | binary | — | search_blocks |
| 10.1021/acs.jced.6b00526 | PROPblock_18 | declared | 33 | binary | — | search_blocks |
| 10.1021/acs.jced.6b01058 | PROPblock_6 | declared | 12 | binary | — | search_blocks |
| 10.1021/acs.jced.6b01058 | PROPblock_7 | declared | 12 | binary | — | search_blocks |
| 10.1021/acs.jced.7b00299 | PROPblock_10 | declared | 2 | binary | — | search_blocks |
| 10.1021/acs.jced.7b00299 | PROPblock_11 | declared | 2 | binary | — | search_blocks |
| 10.1021/acs.jced.7b00501 | PROPblock_9 | declared | 32 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00058 | PROPblock_9 | declared | 20 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00086 | PROPblock_46 | declared | 6 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00086 | PROPblock_47 | declared | 6 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00086 | PROPblock_48 | declared | 6 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00181 | PROPblock_11 | declared | 6 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00723 | PROPblock_10 | declared | 3 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00723 | PROPblock_12 | declared | 3 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00939 | PROPblock_17 | declared | 9 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00939 | PROPblock_18 | declared | 9 | binary | — | search_blocks |
| 10.1021/acs.jced.8b01048 | PROPblock_10 | declared | 9 | binary | — | search_blocks |
| 10.1021/acs.jced.9b00026 | PROPblock_16 | declared | 10 | binary | — | search_blocks |
| 10.1021/je020140j | PROPblock_4 | declared | 77 | binary | — | search_blocks |
| 10.1021/je020140j | PROPblock_5 | declared | 77 | binary | — | search_blocks |
| 10.1021/je020173z | PROPblock_5 | declared | 24 | binary | — | search_blocks |
| 10.1021/je025610o | PROPblock_5 | declared | 30 | binary | — | search_blocks |
| 10.1021/je025610o | PROPblock_6 | declared | 30 | binary | — | search_blocks |
| 10.1021/je0301500 | PROPblock_13 | declared | 5 | binary | — | search_blocks |
| 10.1021/je034101z | PROPblock_4 | declared | 401 | binary | — | search_blocks |
| 10.1021/je049691v | PROPblock_3 | declared | 180 | binary | — | search_blocks |
| 10.1021/je049955d | PROPblock_16 | declared | 15 | binary | — | search_blocks |
| 10.1021/je0600810 | PROPblock_3 | declared | 9 | binary | — | search_blocks |
| 10.1021/je0600810 | PROPblock_4 | declared | 9 | binary | — | search_blocks |
| 10.1021/je0601098 | PROPblock_18 | declared | 12 | binary | — | search_blocks |
| 10.1021/je0601098 | PROPblock_20 | declared | 12 | binary | — | search_blocks |
| 10.1021/je060219e | PROPblock_1 | declared | 26 | binary | — | search_blocks |
| 10.1021/je060335h | PROPblock_1 | declared | 164 | binary | — | search_blocks |
| 10.1021/je2003622 | PROPblock_1 | declared | 16 | binary | — | search_blocks |
| 10.1021/je2003622 | PROPblock_2 | declared | 16 | binary | — | search_blocks |
| 10.1021/je4001203 | PROPblock_1 | declared | 138 | binary | — | search_blocks |
| 10.1021/je4003515 | PROPblock_7 | declared | 23 | binary | — | search_blocks |
| 10.1021/je4003515 | PROPblock_8 | declared | 25 | binary | — | search_blocks |
| 10.1021/je600565m | PROPblock_5 | declared | 17 | binary | — | search_blocks |
| 10.1021/je600565m | PROPblock_6 | declared | 18 | binary | — | search_blocks |
| 10.1021/je700300y | PROPblock_6 | declared | 84 | binary | — | search_blocks |
| 10.1021/je700300y | PROPblock_7 | declared | 84 | binary | — | search_blocks |
| 10.1021/je700618y | PROPblock_7 | declared | 15 | binary | — | search_blocks |
| 10.1021/je700618y | PROPblock_9 | declared | 15 | binary | — | search_blocks |
| 10.1021/je700645p | PROPblock_6 | declared | 70 | binary | — | search_blocks |
| 10.1021/je800150h | PROPblock_8 | declared | 108 | binary | — | search_blocks |
| 10.1021/je800150h | PROPblock_9 | declared | 108 | binary | — | search_blocks |
| 10.1021/je800271e | PROPblock_3 | declared | 52 | binary | — | search_blocks |
| 10.1021/je800271e | PROPblock_4 | declared | 52 | binary | — | search_blocks |
| 10.1021/je800942u | PROPblock_5 | declared | 18 | binary | — | search_blocks |
| 10.1021/je800942u | PROPblock_6 | declared | 18 | binary | — | search_blocks |
| 10.1021/je900064e | PROPblock_6 | declared | 10 | binary | — | search_blocks |
| 10.1021/je9000697 | PROPblock_1 | declared | 16 | binary | — | search_blocks |
| 10.1021/je9000697 | PROPblock_2 | declared | 16 | binary | — | search_blocks |
| 10.1021/je9001027 | PROPblock_3 | declared | 35 | binary | — | search_blocks |
| 10.1021/je9001027 | PROPblock_4 | declared | 35 | binary | — | search_blocks |
| 10.1021/je900743e | PROPblock_2 | declared | 15 | binary | — | search_blocks |
| 10.1021/je900743e | PROPblock_3 | declared | 15 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (pre-compaction)

| # | Iter | Tool | Args | Raw (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=50, p… | 1,184 | KEEP | 1079 | 14.4 |
| 2 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=50, p… | 1,208 | KEEP | 1119 | 15.7 |
| 3 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=50, p… | 1,091 | KEEP | 1046 | 14.2 |
| 4 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=50, p… | 857 | DISCARD | 799 | 19.7 |
| 5 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=50, p… | 1,136 | KEEP | 1106 | 10.5 |
| 6 | 1 | `L1_query` | context=Looking for electrodeposition…, id_catalog… | 271 | — | — | 155.6 |
| 7 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_4'], limit=50, p… | 1,244 | KEEP | 1154 | 21.5 |
| 8 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_4'], limit=50, p… | 1,271 | KEEP | 1170 | 21.2 |
| 9 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_4'], limit=50, p… | 748 | DISCARD | 690 | 15.7 |
| 10 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_4'], limit=50, p… | 1,014 | KEEP | 1014 | 15.6 |
| 11 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_4'], limit=50, p… | 629 | DISCARD | 571 | 15.8 |
| 12 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_4'], limit=10, p… | 1,335 | KEEP | 1245 | 21.3 |
| 13 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_4'], limit=20, p… | 1,361 | KEEP | 1245 | 15.3 |
| 14 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_4'], limit=10, p… | 977 | KEEP | 948 | 21.9 |
| 15 | 1 | `L1_query` | context=Looking for electrodeposition…, id_catalog… | 270 | — | — | 337.0 |
| 16 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_24'], limit=50, … | 1,375 | KEEP | 1266 | 20.7 |
| 17 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_24'], limit=50, … | 1,195 | KEEP | 1104 | 15.3 |
| 18 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_24'], limit=50, … | 1,366 | KEEP | 1366 | 22.3 |
| 19 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_24'], limit=50, … | 1,166 | KEEP | 1136 | 20.8 |
| 20 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_24'], limit=50, … | 807 | DISCARD | 749 | 9.5 |
| 21 | 1 | `L1_query` | context=Looking for electrodeposition…, id_catalog… | 270 | — | — | 180.6 |
| 22 | 2 | `search_system_summary` | compound=['GLOBcomp_1', 'GLOBcomp_31'], purpose=Fi… | 1,333 | KEEP | 1315 | 18.8 |
| 23 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 1,263 | KEEP | 1169 | 22.1 |
| 24 | 1 | `L1_query` | context=Looking for electrodeposition…, id_catalog… | 419 | — | — | 262.4 |
| | | **TOTAL (24 tools)** | | **23,790** | | **21,291** | **1287.9** |

---

## 5. Compaction Events

| # | Trigger | Outcome | Before (chars) | After (chars) | Saved (chars) | Saved (%) |
|--:|---------|---------|---------------:|--------------:|--------------:|----------:|
| 1 | interval=3 | skipped_by_agent | 10,459 | 10,459 | 0 | 0.0% |
| 2 | interval=3 | skipped_by_agent | 5,123 | 5,123 | 0 | 0.0% |

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 9,605 | 1,559 | 11,164 | 14,837 | 57.3 |
| 2 | L1-worker | claudeopus46 | 20,643 | 1,411 | 22,054 | 2,174 | 8.8 |
| 3 | L1-worker | claudeopus46 | 2,065 | 9,225 | 11,290 | 1,431 | 13.6 |
| 4 | L1-worker | claudeopus46 | 2,065 | 18,905 | 20,970 | 1,416 | 14.6 |
| 5 | L1-worker | claudeopus46 | 2,065 | 4,934 | 6,999 | 1,581 | 13.6 |
| 6 | L1-worker | claudeopus46 | 2,065 | 466 | 2,531 | 1,272 | 11.4 |
| 7 | L1-worker | claudeopus46 | 2,065 | 2,285 | 4,350 | 1,496 | 10.0 |
| 8 | L1-worker | claudeopus46 | 20,643 | 4,181 | 24,824 | 3,168 | 17.3 |
| 9 | L1-worker | claudeopus46 | 536 | 2,469 | 3,005 | 804 | 4.9 |
| 10 | L1-worker | claudeopus46 | 1,356 | 2,589 | 3,945 | 1,034 | 5.4 |
| 11 | L1-worker | claudeopus46 | 1,323 | 11,545 | 12,868 | 5,671 | 25.4 |
| 12 | L1-worker | claudeopus46 | 298 | 6,393 | 6,691 | 4,640 | 19.5 |
| 13 | L1-worker | claudeopus46 | 747 | 112,401 | 113,148 | 832 | 7.8 |
| 14 | L1-worker | claudeopus46 | 20,643 | 103,902 | 124,545 | 2,162 | 13.0 |
| 15 | L1-worker | claudeopus46 | 20,643 | 107,113 | 127,756 | 13,147 | 56.7 |
| 16 | L1-worker | claudeopus46 | 2,065 | 8,746 | 10,811 | 1,537 | 13.4 |
| 17 | L1-worker | claudeopus46 | 2,065 | 11,955 | 14,020 | 1,503 | 13.6 |
| 18 | L1-worker | claudeopus46 | 2,065 | 466 | 2,531 | 1,150 | 7.5 |
| 19 | L1-worker | claudeopus46 | 2,065 | 6,643 | 8,708 | 1,611 | 14.9 |
| 20 | L1-worker | claudeopus46 | 2,065 | 482 | 2,547 | 1,030 | 7.6 |
| 21 | L1-worker | claudeopus46 | 20,643 | 108,843 | 129,486 | 5,533 | 26.1 |
| 22 | L1-worker | claudeopus46 | 2,065 | 8,785 | 10,850 | 1,555 | 13.3 |
| 23 | L1-worker | claudeopus46 | 2,065 | 11,989 | 14,054 | 1,558 | 14.5 |
| 24 | L1-worker | claudeopus46 | 2,065 | 6,682 | 8,747 | 1,607 | 14.6 |
| 25 | L1-worker | claudeopus46 | 20,610 | 114,244 | 134,854 | 524 | 6.8 |
| 26 | L1-worker | claudeopus46 | 20,643 | 113,617 | 134,260 | 5,268 | 32.1 |
| 27 | L1-worker | claudeopus46 | 1,356 | 4,911 | 6,267 | 1,012 | 5.6 |
| 28 | L1-worker | claudeopus46 | 536 | 4,791 | 5,327 | 826 | 8.2 |
| 29 | L1-worker | claudeopus46 | 298 | 1,394 | 1,692 | 1,000 | 6.0 |
| 30 | L1-worker | claudeopus46 | 1,323 | 19,477 | 20,800 | 5,367 | 24.1 |
| 31 | L1-worker | claudeopus46 | 298 | 6,089 | 6,387 | 4,454 | 19.4 |
| 32 | L1-worker | claudeopus46 | 747 | 111,679 | 112,426 | 860 | 8.3 |
| 33 | L1-worker | claudeopus46 | 20,643 | 197,761 | 218,404 | 2,567 | 15.5 |
| 34 | L1-worker | claudeopus46 | 2,065 | 10,331 | 12,396 | 1,676 | 13.4 |
| 35 | L1-worker | claudeopus46 | 2,065 | 11,183 | 13,248 | 1,648 | 14.4 |
| 36 | L1-worker | claudeopus46 | 2,065 | 8,048 | 10,113 | 1,661 | 14.1 |
| 37 | L1-worker | claudeopus46 | 2,065 | 2,687 | 4,752 | 1,744 | 13.2 |
| 38 | L1-worker | claudeopus46 | 2,065 | 519 | 2,584 | 1,265 | 8.8 |
| 39 | L1-worker | claudeopus46 | 20,643 | 200,499 | 221,142 | 3,664 | 24.1 |
| 40 | L1-worker | claudeopus46 | 536 | 2,795 | 3,331 | 712 | 4.6 |
| 41 | L1-worker | claudeopus46 | 1,356 | 2,915 | 4,271 | 1,006 | 5.0 |
| 42 | L1-worker | claudeopus46 | 1,323 | 12,536 | 13,859 | 5,484 | 23.7 |
| 43 | L1-worker | claudeopus46 | 298 | 6,206 | 6,504 | 4,512 | 18.9 |
| 44 | L1-worker | claudeopus46 | 747 | 104,103 | 104,850 | 820 | 8.2 |
| 45 | L1-worker | claudeopus46 | 20,643 | 290,952 | 311,595 | 1,862 | 14.0 |
| 46 | L1-worker | claudeopus46 | 20,643 | 291,902 | 312,545 | 13,560 | 64.9 |
| 47 | L1-worker | claudeopus46 | 2,065 | 1,672 | 3,737 | 1,937 | 11.3 |
| 48 | L1-worker | claudeopus46 | 20,643 | 293,281 | 313,924 | 13,131 | 62.4 |
| 49 | L1-worker | claudeopus46 | 2,065 | 8,415 | 10,480 | 1,571 | 13.8 |
| 50 | L1-worker | claudeopus46 | 20,610 | 295,966 | 316,576 | 471 | 5.9 |
| 51 | L1-worker | claudeopus46 | 20,643 | 295,213 | 315,856 | 5,252 | 30.3 |
| 52 | L1-worker | claudeopus46 | 1,356 | 4,397 | 5,753 | 1,083 | 5.9 |
| 53 | L1-worker | claudeopus46 | 536 | 4,277 | 4,813 | 819 | 6.2 |
| 54 | L1-worker | claudeopus46 | 298 | 1,465 | 1,763 | 1,071 | 3.8 |
| 55 | L1-worker | claudeopus46 | 1,323 | 10,325 | 11,648 | 3,478 | 15.9 |
| 56 | L1-worker | claudeopus46 | 298 | 4,200 | 4,498 | 2,658 | 14.3 |
| 57 | L1-worker | claudeopus46 | 1,160 | 14,424 | 15,584 | 2,491 | 12.8 |
| 58 | L0-main | claudeopus46 | 9,605 | 293,752 | 303,357 | 7,296 | 47.5 |
| 59 | L0-main | claudeopus46 | 1,356 | 7,427 | 8,783 | 1,797 | 8.7 |
| 60 | L0-main | claudeopus46 | 298 | 2,179 | 2,477 | 1,737 | 7.0 |
| 61 | L0-main | claudeopus46 | 1,323 | 14,400 | 15,723 | 5,755 | 29.8 |
| 62 | L0-main | claudeopus46 | 298 | 6,423 | 6,721 | 4,865 | 23.1 |

