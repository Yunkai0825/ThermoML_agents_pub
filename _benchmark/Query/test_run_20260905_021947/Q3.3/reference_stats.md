# Reference Stats — query-agent

**Run started:** 2026-09-05 05:35:29
**Wall time (at last flush):** 993.9 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 11 | 52,968 | 41,883 | 14,612 | 94,851 | 8,622 | 94.3 | claudeopus46 |
| L1-worker | 70 | 826,256 | 495,260 | 143,256 | 1,321,516 | 18,878 | 908.0 | claudeopus46 |
| **TOTAL** | **81** | **879,224** | **537,143** | **157,868** | **1,416,367** | **17,486** | **1002.3** | |

**Estimated tokens:** ~354,091 input + ~39,467 output = ~393,558 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_system_registry` | 2 | 17 | 6 | 5 | 39 | 71 | 2,967 |
| `search_blocks` | 2 | 17 | 6 | 5 | 39 | 71 | 2,967 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 8 | 5 | 1 | 11 | 20 | 2,112 |
| `search_blocks` | 2 | 3 | 1 | 2 | 1 | 3 | 39 |
| `search_blocks` | 2 | 2 | 1 | 2 | 1 | 2 | 38 |
| `search_blocks` | 2 | 2 | 1 | 1 | 1 | 2 | 46 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_system_registry` | 2 | 17 | 6 | 5 | 39 | 71 | 2,967 |
| `search_blocks` | 2 | 14 | 6 | 5 | 27 | 50 | 2,504 |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 12 |
| `search_blocks` | 2 | 1 | 2 | 2 | 1 | 1 | 12 |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 12 |
| `search_blocks` | 2 | 1 | 1 | 1 | 1 | 1 | 17 |
| `search_blocks` | 2 | 1 | 1 | 1 | 1 | 1 | 17 |
| `search_blocks` | 2 | 1 | 1 | 0 | 1 | 1 | 1 |
| `search_blocks` | 2 | 1 | 1 | 0 | 1 | 1 | 1 |
| `search_blocks` | 2 | 1 | 1 | 1 | 1 | 1 | 18 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 14 | 6 | 5 | 27 | 50 | 2,504 |
| `search_system_registry` | 2 | 17 | 6 | 5 | 39 | 71 | 2,967 |
| `search_blocks` | 2 | 14 | 6 | 5 | 27 | 50 | 2,504 |
| `search_blocks` | 2 | 1 | 3 | 0 | 1 | 1 | 209 |
| **TOTAL** | **46** | **134** | **64** | **48** | **260** | **470** | **21,914** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_6 |  | resolve_compound_ids, search_blocks, search_system_registry |
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks, search_system_registry |

#### References (39 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_378 |  | search_blocks, search_system_registry |
| GLOBlit_1311 |  | search_blocks, search_system_registry |
| GLOBlit_1423 |  | search_blocks, search_system_registry |
| GLOBlit_1801 |  | search_blocks, search_system_registry |
| GLOBlit_1827 |  | search_blocks, search_system_registry |
| GLOBlit_1910 |  | search_blocks, search_system_registry |
| GLOBlit_2096 |  | search_blocks, search_system_registry |
| GLOBlit_2432 |  | search_blocks, search_system_registry |
| GLOBlit_2687 |  | search_blocks, search_system_registry |
| GLOBlit_2892 |  | search_blocks, search_system_registry |
| GLOBlit_4843 |  | search_blocks, search_system_registry |
| GLOBlit_4959 |  | search_blocks, search_system_registry |
| GLOBlit_5240 |  | search_blocks, search_system_registry |
| GLOBlit_5585 |  | search_blocks, search_system_registry |
| GLOBlit_6409 |  | search_blocks, search_system_registry |
| GLOBlit_6553 |  | search_blocks, search_system_registry |
| GLOBlit_6822 |  | search_blocks, search_system_registry |
| GLOBlit_7238 |  | search_blocks, search_system_registry |
| GLOBlit_7312 |  | search_blocks, search_system_registry |
| GLOBlit_7474 |  | search_blocks, search_system_registry |
| GLOBlit_7483 |  | search_blocks, search_system_registry |
| GLOBlit_7500 |  | search_blocks, search_system_registry |
| GLOBlit_7596 |  | search_blocks, search_system_registry |
| GLOBlit_7629 |  | search_blocks, search_system_registry |
| GLOBlit_7665 |  | search_blocks, search_system_registry |
| GLOBlit_7735 |  | search_blocks, search_system_registry |
| GLOBlit_8447 |  | search_blocks, search_system_registry |
| GLOBlit_8629 |  | search_blocks, search_system_registry |
| GLOBlit_9129 |  | search_blocks, search_system_registry |
| GLOBlit_9722 |  | search_blocks, search_system_registry |
| GLOBlit_10006 |  | search_blocks, search_system_registry |
| GLOBlit_10701 |  | search_blocks, search_system_registry |
| GLOBlit_10907 |  | search_blocks, search_system_registry |
| GLOBlit_10926 |  | search_blocks, search_system_registry |
| GLOBlit_11042 |  | search_blocks, search_system_registry |
| GLOBlit_11130 |  | search_blocks, search_system_registry |
| GLOBlit_11142 |  | search_blocks, search_system_registry |
| GLOBlit_11513 |  | search_blocks, search_system_registry |
| GLOBlit_11872 |  | search_blocks, search_system_registry |

#### Block_Types (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | search_system_registry |

#### Variables (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_3 | Pressure, kPa | search_blocks, search_system_registry |
| GLOBvar_2 | Mole fraction | search_blocks, search_system_registry |
| GLOBvar_1 | Temperature, K | search_blocks, search_system_registry |
| GLOBvar_5 | Mass fraction | search_blocks, search_system_registry |
| GLOBvar_4 | Molality, mol/kg | search_blocks, search_system_registry |
| GLOBvar_15 | Mass ratio of solute to solvent | search_blocks, search_system_registry |

#### Phases (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks, search_system_registry |
| GLOBphase_3 |  | search_blocks, search_system_registry |

#### Properties (17 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_14 | Boiling temperature at pressure P, K | search_blocks, search_system_registry |
| GLOBprop_1 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBprop_9 | Molar heat capacity at constant pressure, J/K/mol | search_blocks, search_system_registry |
| GLOBprop_2 | Mole fraction | search_blocks, search_system_registry |
| GLOBprop_58 | Azeotropic temperature, K | search_blocks, search_system_registry |
| GLOBprop_45 | Azeotropic composition: mole fraction | search_blocks, search_system_registry |
| GLOBprop_13 | Surface tension liquid-gas, N/m | search_blocks, search_system_registry |
| GLOBprop_17 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks, search_system_registry |
| GLOBprop_8 | Speed of sound, m/s | search_blocks, search_system_registry |
| GLOBprop_4 | Viscosity, Pa*s | search_blocks, search_system_registry |
| GLOBprop_18 | Electrical conductivity, S/m | search_blocks, search_system_registry |
| GLOBprop_7 | Refractive index (Na D-line) | search_blocks, search_system_registry |
| GLOBprop_5 | Vapor or sublimation pressure, kPa | search_blocks, search_system_registry |
| GLOBprop_63 | Heat capacity at constant pressure per volume, J/K/m3 | search_blocks, search_system_registry |
| GLOBprop_55 | Henry's Law constant (molality scale), kPa*kg/mol | search_blocks, search_system_registry |
| GLOBprop_3 | Activity coefficient | search_blocks, search_system_registry |
| GLOBprop_32 | Amount concentration (molarity), mol/dm3 | search_blocks, search_system_registry |

#### Measurements (25 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_171 | Boiling temperature at pressure P, K | search_blocks, search_system_registry |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_12 | Molar heat capacity at constant pressure, J/K/mol | search_blocks, search_system_registry |
| GLOBmeas_5 | Boiling temperature at pressure P, K | search_blocks, search_system_registry |
| GLOBmeas_1 | Mole fraction | search_blocks, search_system_registry |
| GLOBmeas_39 | Azeotropic temperature, K | search_blocks, search_system_registry |
| GLOBmeas_192 | Surface tension liquid-gas, N/m | search_blocks, search_system_registry |
| GLOBmeas_18 | Speed of sound, m/s | search_blocks, search_system_registry |
| GLOBmeas_8 | Viscosity, Pa*s | search_blocks, search_system_registry |
| GLOBmeas_132 | Boiling temperature at pressure P, K | search_blocks, search_system_registry |
| GLOBmeas_14 | Electrical conductivity, S/m | search_blocks, search_system_registry |
| GLOBmeas_3 | Refractive index (Na D-line) | search_blocks, search_system_registry |
| GLOBmeas_137 | Boiling temperature at pressure P, K | search_blocks, search_system_registry |
| GLOBmeas_967 | Boiling temperature at pressure P, K | search_blocks, search_system_registry |
| GLOBmeas_297 | Mole fraction | search_blocks, search_system_registry |
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_146 | Vapor or sublimation pressure, kPa | search_blocks, search_system_registry |
| GLOBmeas_145 | Mole fraction | search_blocks, search_system_registry |
| GLOBmeas_19 | Surface tension liquid-gas, N/m | search_blocks, search_system_registry |
| GLOBmeas_1043 | Activity coefficient | search_blocks, search_system_registry |
| GLOBmeas_1366 | Activity coefficient | search_blocks, search_system_registry |
| GLOBmeas_866 | Activity coefficient | search_blocks, search_system_registry |
| GLOBmeas_155 | Boiling temperature at pressure P, K | search_blocks, search_system_registry |
| GLOBmeas_4 | Viscosity, Pa*s | search_blocks, search_system_registry |
| GLOBmeas_189 | Mole fraction | search_blocks, search_system_registry |

#### Constraints (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | search_blocks, search_system_registry |
| GLOBconstr_4 | Frequency, MHz | search_blocks, search_system_registry |
| GLOBconstr_5 | Mass fraction | search_blocks, search_system_registry |
| GLOBconstr_2 | Temperature, K | search_blocks, search_system_registry |
| GLOBconstr_3 | Mole fraction | search_blocks, search_system_registry |

#### Solvents (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | search_blocks, search_system_registry |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 2 |
| Unique References | 39 |
| Unique Block_Types | 1 |
| Unique Variables | 6 |
| Unique Phases | 2 |
| Unique Properties | 17 |
| Unique Measurements | 25 |
| Unique Constraints | 5 |
| Unique Solvents | 1 |
| Total DOIs | 39 |
| Unique parent blocks | 71 |
| Explicit block/subsystem targets | 71 |
| Subsystem targets | 0 |
| Target-matched data points | 21,914 |

---

## 3. DOI & Block References

**Unique DOIs:** 39  |  **Parent blocks:** 71  |  **Explicit targets:** 71  |  **Subsystems:** 0  |  **Target-matched datapoints:** 2,967

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2006.03.021 | 1 | 48 | binary | search_blocks, search_system_registry |
| 10.1016/j.fluid.2013.08.007 | 2 | 1,248 | binary | search_blocks, search_system_registry |
| 10.1016/j.fluid.2014.02.006 | 4 | 36 | binary | search_blocks, search_system_registry |
| 10.1016/j.fluid.2015.09.052 | 1 | 17 | binary | search_blocks, search_system_registry |
| 10.1016/j.fluid.2015.11.034 | 2 | 28 | binary | search_blocks, search_system_registry |
| 10.1016/j.fluid.2016.04.007 | 1 | 60 | binary | search_blocks, search_system_registry |
| 10.1016/j.fluid.2017.09.010 | 3 | 37 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2004.07.019 | 1 | 529 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2006.04.006 | 2 | 34 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2007.12.002 | 1 | 45 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2016.10.001 | 2 | 30 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2017.02.005 | 2 | 62 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2018.04.017 | 2 | 6 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2019.105880 | 3 | 36 | binary | search_blocks, search_system_registry |
| 10.1016/j.tca.2017.12.010 | 1 | 24 | binary | search_blocks, search_system_registry |
| 10.1021/acs.jced.5b00200 | 1 | 2 | binary | search_blocks, search_system_registry |
| 10.1021/acs.jced.6b00019 | 2 | 12 | binary | search_blocks, search_system_registry |
| 10.1021/acs.jced.7b00523 | 2 | 36 | binary | search_blocks, search_system_registry |
| 10.1021/acs.jced.7b00755 | 2 | 34 | binary | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00160 | 2 | 36 | binary | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00181 | 2 | 12 | binary | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00228 | 2 | 40 | binary | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00610 | 1 | 2 | binary | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00723 | 2 | 6 | binary | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00895 | 2 | 46 | binary | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b01116 | 2 | 22 | binary | search_blocks, search_system_registry |
| 10.1021/je049738c | 2 | 16 | binary | search_blocks, search_system_registry |
| 10.1021/je0501336 | 2 | 18 | binary | search_blocks, search_system_registry |
| 10.1021/je1001329 | 1 | 11 | binary | search_blocks, search_system_registry |
| 10.1021/je201010s | 2 | 38 | binary | search_blocks, search_system_registry |
| 10.1021/je3010535 | 1 | 4 | binary | search_blocks, search_system_registry |
| 10.1021/je600567z | 3 | 7 | binary | search_blocks, search_system_registry |
| 10.1021/je7003808 | 2 | 22 | binary | search_blocks, search_system_registry |
| 10.1021/je700418a | 1 | 1 | binary | search_blocks, search_system_registry |
| 10.1021/je700700f | 3 | 39 | binary | search_blocks, search_system_registry |
| 10.1021/je8001305 | 1 | 209 | binary | search_blocks, search_system_registry |
| 10.1021/je800158z | 1 | 56 | binary | search_blocks, search_system_registry |
| 10.1021/je9000922 | 2 | 22 | binary | search_blocks, search_system_registry |
| 10.1021/je900966r | 2 | 36 | binary | search_blocks, search_system_registry |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2006.03.021 | PROPblock_1 | declared | 48 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2013.08.007 | PROPblock_4 | declared | 1,110 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2013.08.007 | PROPblock_5 | declared | 138 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2014.02.006 | PROPblock_11 | declared | 17 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2014.02.006 | PROPblock_12 | declared | 17 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2014.02.006 | PROPblock_13 | declared | 1 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2014.02.006 | PROPblock_14 | declared | 1 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2015.09.052 | PROPblock_13 | declared | 17 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2015.11.034 | PROPblock_1 | declared | 14 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2015.11.034 | PROPblock_2 | declared | 14 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2016.04.007 | PROPblock_2 | declared | 60 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2017.09.010 | PROPblock_5 | declared | 18 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2017.09.010 | PROPblock_6 | declared | 18 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2017.09.010 | PROPblock_7 | declared | 1 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2004.07.019 | PROPblock_4 | declared | 529 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2006.04.006 | PROPblock_3 | declared | 17 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2006.04.006 | PROPblock_4 | declared | 17 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2007.12.002 | PROPblock_1 | declared | 45 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2016.10.001 | PROPblock_10 | declared | 15 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2016.10.001 | PROPblock_9 | declared | 15 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2017.02.005 | PROPblock_3 | declared | 31 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2017.02.005 | PROPblock_4 | declared | 31 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2018.04.017 | PROPblock_4 | declared | 3 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2018.04.017 | PROPblock_5 | declared | 3 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2019.105880 | PROPblock_10 | declared | 12 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2019.105880 | PROPblock_11 | declared | 12 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2019.105880 | PROPblock_12 | declared | 12 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.tca.2017.12.010 | PROPblock_7 | declared | 24 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.5b00200 | PROPblock_21 | declared | 2 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.6b00019 | PROPblock_13 | declared | 6 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.6b00019 | PROPblock_14 | declared | 6 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.7b00523 | PROPblock_3 | declared | 18 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.7b00523 | PROPblock_4 | declared | 18 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.7b00755 | PROPblock_2 | declared | 17 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.7b00755 | PROPblock_3 | declared | 17 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00160 | PROPblock_15 | declared | 18 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00160 | PROPblock_16 | declared | 18 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00181 | PROPblock_6 | declared | 6 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00181 | PROPblock_7 | declared | 6 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00228 | PROPblock_4 | declared | 20 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00228 | PROPblock_5 | declared | 20 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00610 | PROPblock_10 | declared | 2 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00723 | PROPblock_14 | declared | 3 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00723 | PROPblock_15 | declared | 3 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00895 | PROPblock_1 | declared | 23 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00895 | PROPblock_2 | declared | 23 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b01116 | PROPblock_10 | declared | 11 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b01116 | PROPblock_9 | declared | 11 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je049738c | PROPblock_27 | declared | 8 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je049738c | PROPblock_28 | declared | 8 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je0501336 | PROPblock_1 | declared | 9 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je0501336 | PROPblock_2 | declared | 9 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je1001329 | PROPblock_5 | declared | 11 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je201010s | PROPblock_7 | declared | 21 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je201010s | PROPblock_8 | declared | 17 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je3010535 | PROPblock_86 | declared | 4 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je600567z | PROPblock_1 | declared | 3 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je600567z | PROPblock_2 | declared | 1 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je600567z | PROPblock_3 | declared | 3 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je7003808 | PROPblock_1 | declared | 11 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je7003808 | PROPblock_2 | declared | 11 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je700418a | PROPblock_3 | declared | 1 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je700700f | PROPblock_15 | declared | 13 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je700700f | PROPblock_16 | declared | 13 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je700700f | PROPblock_17 | declared | 13 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je8001305 | PROPblock_1 | declared | 209 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je800158z | PROPblock_4 | declared | 56 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je9000922 | PROPblock_2 | declared | 12 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je9000922 | PROPblock_3 | declared | 10 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je900966r | PROPblock_5 | declared | 6 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je900966r | PROPblock_6 | declared | 30 | binary | 2 | search_blocks, search_system_registry |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve propan-2-ol… | 190 | KEEP ←in 285 | 190 | 5.0 |
| 2 | 3 | `search_system_registry` | compound=['GLOBcomp_6', 'GLOBcomp_1'], limit=100, … | 1,348 | KEEP ←in 10,570 | 1151 | 15.1 |
| 3 | 4 | `search_blocks` | compound=['GLOBcomp_6', 'GLOBcomp_1'], limit=71, p… | 493 | KEEP ←in 12,134 | 845 | 8.5 |
| 4 | 5 | `search_blocks` | compound=['GLOBcomp_6', 'GLOBcomp_1'], limit=20, p… | 953 | KEEP ←in 5,619 | 1330 | 15.5 |
| 5 | 6 | `search_blocks` | compound=['GLOBcomp_6', 'GLOBcomp_1'], limit=50, l… | 1,330 | KEEP ←in 3,630 | 930 | 13.4 |
| 6 | 7 | `search_blocks` | compound=['GLOBcomp_6', 'GLOBcomp_1'], limit=30, l… | 930 | KEEP ←in 3,466 | 1137 | 13.3 |
| 7 | 8 | `search_blocks` | compound=['GLOBcomp_6', 'GLOBcomp_1'], limit=30, l… | 1,137 | KEEP ←in 30,354 | 1347 | 15.4 |
| 8 | 1 | `L1_query` | context=User wants the most comprehen…, id_catalog… | 415 | — | — | 271.4 |
| 9 | 2 | `resolve_compound_ids` | limit=10, min_score=50, purpose=Resolve compound I… | 190 | KEEP ←in 285 | 190 | 4.3 |
| 10 | 3 | `search_system_registry` | compound=['GLOBcomp_1', 'GLOBcomp_6'], limit=100, … | 1,289 | KEEP ←in 10,570 | 1110 | 20.2 |
| 11 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_6'], limit=50, p… | 1,482 | KEEP ←in 1,993 | 1255 | 21.6 |
| 12 | 5 | `search_blocks` | block_number=GLOBlit_5585::PROPblock_10, compound=… | 1,270 | KEEP ←in 2,069 | 1041 | 12.4 |
| 13 | 6 | `search_blocks` | block_number=GLOBlit_5585::PROPblock_11, compound=… | 1,041 | KEEP ←in 2,041 | 1258 | 11.8 |
| 14 | 7 | `search_blocks` | block_number=GLOBlit_5585::PROPblock_12, compound=… | 1,258 | KEEP ←in 1,947 | 1363 | 11.5 |
| 15 | 8 | `search_blocks` | block_number=GLOBlit_1423::PROPblock_11, compound=… | 1,378 | KEEP ←in 1,840 | 1316 | 12.9 |
| 16 | 9 | `search_blocks` | block_number=GLOBlit_1423::PROPblock_12, compound=… | 1,316 | KEEP ←in 1,327 | 736 | 11.3 |
| 17 | 10 | `search_blocks` | block_number=GLOBlit_1423::PROPblock_13, compound=… | 736 | KEEP ←in 1,375 | 967 | 8.2 |
| 18 | 11 | `search_blocks` | block_number=GLOBlit_1423::PROPblock_14, compound=… | 967 | KEEP ←in 1,952 | 1268 | 9.6 |
| 19 | 12 | `search_blocks` | block_number=GLOBlit_2096::PROPblock_5, compound=[… | 1,268 | KEEP ←in 30,354 | 1313 | 12.0 |
| 20 | 2 | `L1_query` | context=User wants the most complete …, id_catalog… | 278 | — | — | 390.0 |
| 21 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve global IDs … | 203 | KEEP ←in 285 | 203 | 4.5 |
| 22 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_6'], limit=50, p… | 1,477 | KEEP ←in 30,354 | 1164 | 15.1 |
| 23 | 4 | `search_system_registry` | compound=['GLOBcomp_1', 'GLOBcomp_6'], limit=100, … | 1,319 | KEEP ←in 10,570 | 1137 | 22.9 |
| 24 | 5 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_6'], limit=50, p… | 1,373 | KEEP ←in 2,385 | 1077 | 21.3 |
| 25 | 6 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_6'], limit=50, l… | 1,077 | — | — | 13.2 |
| 26 | 3 | `L1_query` | context=User wants the most complete …, id_catalog… | 5,904 | — | — | 244.3 |
| | | **TOTAL (26 tools)** | | **30,622** | | **22,328** | **1204.7** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 664 | 12,245 | 1,237 | 8.0 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,132 | 25,227 | 593 | 4.9 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,169 | 26,264 | 570 | 4.4 |
| 4 | L1-worker | claudeopus46 | 3,767 | 462 | 4,229 | 387 | 4.3 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,761 | 25,856 | 904 | 6.6 |
| 6 | L1-worker | claudeopus46 | 3,767 | 11,042 | 14,809 | 1,601 | 13.6 |
| 7 | L1-worker | claudeopus46 | 24,095 | 3,476 | 27,571 | 1,056 | 11.8 |
| 8 | L1-worker | claudeopus46 | 24,095 | 4,354 | 28,449 | 1,192 | 8.5 |
| 9 | L1-worker | claudeopus46 | 3,767 | 12,534 | 16,301 | 1,626 | 14.8 |
| 10 | L1-worker | claudeopus46 | 24,095 | 5,683 | 29,778 | 2,736 | 19.2 |
| 11 | L1-worker | claudeopus46 | 3,767 | 6,254 | 10,021 | 1,698 | 13.1 |
| 12 | L1-worker | claudeopus46 | 24,095 | 7,433 | 31,528 | 3,999 | 22.3 |
| 13 | L1-worker | claudeopus46 | 3,767 | 4,234 | 8,001 | 1,531 | 12.4 |
| 14 | L1-worker | claudeopus46 | 24,095 | 8,819 | 32,914 | 2,746 | 18.2 |
| 15 | L1-worker | claudeopus46 | 3,767 | 4,009 | 7,776 | 1,647 | 15.2 |
| 16 | L1-worker | claudeopus46 | 24,095 | 10,411 | 34,506 | 5,685 | 34.4 |
| 17 | L1-worker | claudeopus46 | 2,320 | 3,319 | 5,639 | 1,298 | 6.0 |
| 18 | L1-worker | claudeopus46 | 627 | 3,199 | 3,826 | 1,244 | 9.2 |
| 19 | L1-worker | claudeopus46 | 366 | 1,735 | 2,101 | 1,248 | 6.5 |
| 20 | L1-worker | claudeopus46 | 2,106 | 4,572 | 6,678 | 5,434 | 19.1 |
| 21 | L1-worker | claudeopus46 | 366 | 6,211 | 6,577 | 4,289 | 15.1 |
| 22 | L1-worker | claudeopus46 | 1,228 | 11,626 | 12,854 | 4,258 | 16.4 |
| 23 | L0-main | claudeopus46 | 11,581 | 1,400 | 12,981 | 1,407 | 8.7 |
| 24 | L1-worker | claudeopus46 | 24,095 | 1,323 | 25,418 | 569 | 4.6 |
| 25 | L1-worker | claudeopus46 | 24,095 | 2,394 | 26,489 | 599 | 5.2 |
| 26 | L1-worker | claudeopus46 | 3,767 | 466 | 4,233 | 364 | 3.9 |
| 27 | L1-worker | claudeopus46 | 24,095 | 1,958 | 26,053 | 941 | 9.3 |
| 28 | L1-worker | claudeopus46 | 3,767 | 11,016 | 14,783 | 1,593 | 13.9 |
| 29 | L1-worker | claudeopus46 | 24,095 | 3,622 | 27,717 | 1,084 | 8.4 |
| 30 | L1-worker | claudeopus46 | 3,767 | 30,789 | 34,556 | 1,773 | 14.9 |
| 31 | L1-worker | claudeopus46 | 24,095 | 5,459 | 29,554 | 1,510 | 10.8 |
| 32 | L1-worker | claudeopus46 | 3,767 | 2,476 | 6,243 | 1,664 | 12.3 |
| 33 | L1-worker | claudeopus46 | 24,095 | 7,183 | 31,278 | 1,048 | 12.8 |
| 34 | L1-worker | claudeopus46 | 3,767 | 2,495 | 6,262 | 1,293 | 11.4 |
| 35 | L1-worker | claudeopus46 | 24,095 | 8,677 | 32,772 | 888 | 7.2 |
| 36 | L1-worker | claudeopus46 | 3,767 | 2,422 | 6,189 | 1,541 | 11.0 |
| 37 | L1-worker | claudeopus46 | 24,095 | 10,339 | 34,434 | 960 | 15.0 |
| 38 | L1-worker | claudeopus46 | 3,767 | 2,305 | 6,072 | 1,678 | 12.6 |
| 39 | L1-worker | claudeopus46 | 24,095 | 12,139 | 36,234 | 853 | 7.6 |
| 40 | L1-worker | claudeopus46 | 3,767 | 2,213 | 5,980 | 1,698 | 10.5 |
| 41 | L1-worker | claudeopus46 | 24,095 | 13,865 | 37,960 | 797 | 6.3 |
| 42 | L1-worker | claudeopus46 | 3,767 | 1,700 | 5,467 | 1,120 | 8.1 |
| 43 | L1-worker | claudeopus46 | 24,095 | 14,981 | 39,076 | 654 | 6.6 |
| 44 | L1-worker | claudeopus46 | 3,767 | 1,766 | 5,533 | 1,319 | 8.7 |
| 45 | L1-worker | claudeopus46 | 24,095 | 16,303 | 40,398 | 967 | 9.4 |
| 46 | L1-worker | claudeopus46 | 3,767 | 2,320 | 6,087 | 1,708 | 11.7 |
| 47 | L1-worker | claudeopus46 | 24,062 | 17,648 | 41,710 | 6,046 | 37.6 |
| 48 | L1-worker | claudeopus46 | 24,062 | 21,953 | 46,015 | 6,299 | 40.9 |
| 49 | L1-worker | claudeopus46 | 2,320 | 8,465 | 10,785 | 1,254 | 9.6 |
| 50 | L1-worker | claudeopus46 | 627 | 8,345 | 8,972 | 1,586 | 11.4 |
| 51 | L1-worker | claudeopus46 | 366 | 1,691 | 2,057 | 1,209 | 4.5 |
| 52 | L1-worker | claudeopus46 | 2,106 | 9,909 | 12,015 | 6,502 | 25.1 |
| 53 | L1-worker | claudeopus46 | 366 | 7,279 | 7,645 | 5,121 | 20.7 |
| 54 | L1-worker | claudeopus46 | 1,228 | 18,132 | 19,360 | 5,144 | 21.4 |
| 55 | L0-main | claudeopus46 | 11,581 | 2,157 | 13,738 | 1,402 | 9.8 |
| 56 | L1-worker | claudeopus46 | 24,095 | 1,400 | 25,495 | 546 | 4.7 |
| 57 | L1-worker | claudeopus46 | 24,095 | 2,418 | 26,513 | 536 | 3.8 |
| 58 | L1-worker | claudeopus46 | 3,767 | 443 | 4,210 | 352 | 4.0 |
| 59 | L1-worker | claudeopus46 | 24,095 | 2,034 | 26,129 | 737 | 6.0 |
| 60 | L1-worker | claudeopus46 | 3,767 | 30,761 | 34,528 | 1,651 | 14.0 |
| 61 | L1-worker | claudeopus46 | 24,095 | 3,815 | 27,910 | 866 | 6.9 |
| 62 | L1-worker | claudeopus46 | 3,767 | 11,005 | 14,772 | 1,717 | 16.2 |
| 63 | L1-worker | claudeopus46 | 24,095 | 5,514 | 29,609 | 4,967 | 30.7 |
| 64 | L1-worker | claudeopus46 | 3,767 | 30,766 | 34,533 | 1,618 | 15.4 |
| 65 | L1-worker | claudeopus46 | 24,095 | 7,309 | 31,404 | 4,373 | 26.1 |
| 66 | L1-worker | claudeopus46 | 3,767 | 2,910 | 6,677 | 1,473 | 12.9 |
| 67 | L1-worker | claudeopus46 | 24,095 | 8,832 | 32,927 | 14,282 | 71.9 |
| 68 | L1-worker | claudeopus46 | 2,106 | 4,579 | 6,685 | 233 | 2.3 |
| 69 | L1-worker | claudeopus46 | 366 | 1,010 | 1,376 | 153 | 2.7 |
| 70 | L1-worker | claudeopus46 | 2,320 | 3,058 | 5,378 | 1,170 | 5.1 |
| 71 | L1-worker | claudeopus46 | 627 | 2,938 | 3,565 | 1,388 | 6.3 |
| 72 | L1-worker | claudeopus46 | 366 | 1,607 | 1,973 | 1,120 | 3.7 |
| 73 | L1-worker | claudeopus46 | 787 | 8,793 | 9,580 | 550 | 5.9 |
| 74 | L0-main | claudeopus46 | 11,581 | 15,079 | 26,660 | 3,079 | 17.1 |
| 75 | L0-main | claudeopus46 | 2,320 | 3,249 | 5,569 | 1,059 | 4.9 |
| 76 | L0-main | claudeopus46 | 366 | 1,534 | 1,900 | 1,015 | 3.6 |
| 77 | L0-main | claudeopus46 | 2,106 | 3,745 | 5,851 | 1,350 | 17.9 |
| 78 | L0-main | claudeopus46 | 366 | 1,899 | 2,265 | 1,870 | 7.5 |
| 79 | L0-main | claudeopus46 | 560 | 5,398 | 5,958 | 462 | 3.7 |
| 80 | L0-main | claudeopus46 | 560 | 4,460 | 5,020 | 1,716 | 11.5 |
| 81 | L0-main | claudeopus46 | 366 | 2,298 | 2,664 | 15 | 1.6 |

