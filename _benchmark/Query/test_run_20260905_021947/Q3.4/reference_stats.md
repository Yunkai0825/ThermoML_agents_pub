# Reference Stats — query-agent

**Run started:** 2026-09-05 05:35:35
**Wall time (at last flush):** 1,093.9 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 12 | 65,339 | 138,237 | 17,045 | 203,576 | 16,964 | 111.1 | claudeopus46 |
| L1-worker | 91 | 1,272,453 | 1,373,558 | 157,023 | 2,646,011 | 29,077 | 1057.1 | claudeopus46 |
| **TOTAL** | **103** | **1,337,792** | **1,511,795** | **174,068** | **2,849,587** | **27,665** | **1168.2** | |

**Estimated tokens:** ~712,396 input + ~43,517 output = ~755,913 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 11 | 4 | 4 | 29 | 50 | 3,112 |
| `search_system_registry` | 2 | 18 | 7 | 6 | 58 | 100 | 4,354 |
| `search_blocks` | 2 | 2 | 3 | 1 | 1 | 4 | 326 |
| `search_blocks` | 2 | 4 | 2 | 1 | 1 | 4 | 34 |
| `search_blocks` | 2 | 3 | 2 | 2 | 1 | 3 | 496 |
| `search_system_registry` | 2 | 18 | 7 | 6 | 58 | 100 | 4,354 |
| `search_blocks` | 2 | 3 | 3 | 2 | 1 | 3 | 5 |
| `search_blocks` | 2 | 3 | 1 | 2 | 1 | 3 | 18 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 3 | 7 | 3 | 1 | 1 | 17 | 151 |
| `search_blocks` | 3 | 4 | 3 | 1 | 1 | 7 | 111 |
| `search_blocks` | 3 | 1 | 2 | 1 | 1 | 1 | 39 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 3 | 7 | 3 | 1 | 1 | 17 | 151 |
| `search_blocks` | 3 | 4 | 3 | 1 | 1 | 7 | 111 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 3 | 7 | 3 | 1 | 1 | 17 | 151 |
| `search_blocks` | 3 | 4 | 3 | 1 | 1 | 7 | 111 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **39** | **96** | **49** | **31** | **157** | **340** | **13,524** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_2 |  | resolve_compound_ids, search_blocks, search_system_registry |
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks, search_system_registry |
| GLOBcomp_154 | propan-1,3-diol | search_blocks |

#### References (58 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_220 |  | search_blocks, search_system_registry |
| GLOBlit_299 |  | search_blocks, search_system_registry |
| GLOBlit_384 |  | search_blocks, search_system_registry |
| GLOBlit_528 |  | search_blocks, search_system_registry |
| GLOBlit_742 |  | search_blocks, search_system_registry |
| GLOBlit_757 |  | search_blocks, search_system_registry |
| GLOBlit_977 |  | search_blocks, search_system_registry |
| GLOBlit_1184 |  | search_blocks, search_system_registry |
| GLOBlit_1197 |  | search_blocks, search_system_registry |
| GLOBlit_1289 |  | search_blocks, search_system_registry |
| GLOBlit_1482 |  | search_blocks, search_system_registry |
| GLOBlit_1483 |  | search_blocks, search_system_registry |
| GLOBlit_1518 |  | search_blocks, search_system_registry |
| GLOBlit_1742 |  | search_blocks, search_system_registry |
| GLOBlit_1971 |  | search_blocks, search_system_registry |
| GLOBlit_2035 |  | search_blocks, search_system_registry |
| GLOBlit_2092 |  | search_blocks, search_system_registry |
| GLOBlit_2220 |  | search_blocks, search_system_registry |
| GLOBlit_2300 |  | search_blocks, search_system_registry |
| GLOBlit_2432 |  | search_blocks, search_system_registry |
| GLOBlit_2574 |  | search_blocks, search_system_registry |
| GLOBlit_2732 |  | search_blocks, search_system_registry |
| GLOBlit_2825 |  | search_blocks, search_system_registry |
| GLOBlit_3475 |  | search_blocks, search_system_registry |
| GLOBlit_3697 |  | search_blocks, search_system_registry |
| GLOBlit_3971 |  | search_blocks, search_system_registry |
| GLOBlit_4181 |  | search_blocks, search_system_registry |
| GLOBlit_4415 |  | search_blocks, search_system_registry |
| GLOBlit_5073 |  | search_blocks, search_system_registry |
| GLOBlit_5201 |  | search_blocks, search_system_registry |
| GLOBlit_5473 |  | search_system_registry |
| GLOBlit_6377 |  | search_system_registry |
| GLOBlit_6628 |  | search_system_registry |
| GLOBlit_6866 |  | search_system_registry |
| GLOBlit_6996 |  | search_system_registry |
| GLOBlit_7085 |  | search_system_registry |
| GLOBlit_7178 |  | search_blocks, search_system_registry |
| GLOBlit_7337 |  | search_system_registry |
| GLOBlit_7425 |  | search_system_registry |
| GLOBlit_7448 |  | search_blocks, search_system_registry |
| GLOBlit_7483 |  | search_system_registry |
| GLOBlit_7629 |  | search_system_registry |
| GLOBlit_7676 |  | search_system_registry |
| GLOBlit_7748 |  | search_system_registry |
| GLOBlit_7794 |  | search_system_registry |
| GLOBlit_8050 |  | search_system_registry |
| GLOBlit_8151 |  | search_system_registry |
| GLOBlit_8381 |  | search_system_registry |
| GLOBlit_8445 |  | search_system_registry |
| GLOBlit_8511 |  | search_system_registry |
| GLOBlit_8830 |  | search_system_registry |
| GLOBlit_8888 |  | search_system_registry |
| GLOBlit_8949 |  | search_system_registry |
| GLOBlit_9006 |  | search_system_registry |
| GLOBlit_9599 |  | search_system_registry |
| GLOBlit_9630 |  | search_system_registry |
| GLOBlit_9693 |  | search_system_registry |
| GLOBlit_9930 |  | search_system_registry |

#### Properties (18 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_1 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBprop_3 | Activity coefficient | search_blocks, search_system_registry |
| GLOBprop_5 | Vapor or sublimation pressure, kPa | search_blocks, search_system_registry |
| GLOBprop_17 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks, search_system_registry |
| GLOBprop_14 | Boiling temperature at pressure P, K | search_blocks, search_system_registry |
| GLOBprop_2 | Mole fraction | search_blocks, search_system_registry |
| GLOBprop_4 | Viscosity, Pa*s | search_blocks, search_system_registry |
| GLOBprop_44 | Relative permittivity at zero frequency | search_blocks, search_system_registry |
| GLOBprop_58 | Azeotropic temperature, K | search_blocks, search_system_registry |
| GLOBprop_45 | Azeotropic composition: mole fraction | search_blocks, search_system_registry |
| GLOBprop_8 | Speed of sound, m/s | search_blocks, search_system_registry |
| GLOBprop_13 | Surface tension liquid-gas, N/m | search_blocks, search_system_registry |
| GLOBprop_62 | Azeotropic pressure, kPa | search_system_registry |
| GLOBprop_7 | Refractive index (Na D-line) | search_blocks, search_system_registry |
| GLOBprop_18 | Electrical conductivity, S/m | search_system_registry |
| GLOBprop_34 | Thermal conductivity, W/m/K | search_system_registry |
| GLOBprop_27 | Henry's Law constant (mole fraction scale), kPa | search_system_registry |
| GLOBprop_29 | Binary diffusion coefficient, m2/s | search_system_registry |

#### Measurements (45 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_138 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_543 | Activity coefficient | search_blocks, search_system_registry |
| GLOBmeas_1045 | Activity coefficient | search_blocks, search_system_registry |
| GLOBmeas_1042 | Activity coefficient | search_blocks, search_system_registry |
| GLOBmeas_133 | Vapor or sublimation pressure, kPa | search_blocks, search_system_registry |
| GLOBmeas_13 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks, search_system_registry |
| GLOBmeas_5 | Boiling temperature at pressure P, K | search_blocks, search_system_registry |
| GLOBmeas_1362 | Boiling temperature at pressure P, K | search_blocks, search_system_registry |
| GLOBmeas_2137 | Boiling temperature at pressure P, K | search_blocks, search_system_registry |
| GLOBmeas_131 | Mole fraction | search_blocks, search_system_registry |
| GLOBmeas_1 | Mole fraction | search_blocks, search_system_registry |
| GLOBmeas_10 | Mole fraction | search_blocks, search_system_registry |
| GLOBmeas_664 | Vapor or sublimation pressure, kPa | search_blocks, search_system_registry |
| GLOBmeas_12 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks, search_system_registry |
| GLOBmeas_66 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_4 | Viscosity, Pa*s | search_blocks, search_system_registry |
| GLOBmeas_1153 | Activity coefficient | search_blocks, search_system_registry |
| GLOBmeas_1355 | Boiling temperature at pressure P, K | search_blocks, search_system_registry |
| GLOBmeas_169 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks, search_system_registry |
| GLOBmeas_161 | Vapor or sublimation pressure, kPa | search_blocks, search_system_registry |
| GLOBmeas_1497 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_140 | Viscosity, Pa*s | search_blocks, search_system_registry |
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_53 | Relative permittivity at zero frequency | search_blocks, search_system_registry |
| GLOBmeas_39 | Azeotropic temperature, K | search_blocks, search_system_registry |
| GLOBmeas_7 | Speed of sound, m/s | search_blocks, search_system_registry |
| GLOBmeas_24 | Mole fraction | search_blocks, search_system_registry |
| GLOBmeas_18 | Speed of sound, m/s | search_blocks, search_system_registry |
| GLOBmeas_11 | Viscosity, Pa*s | search_blocks, search_system_registry |
| GLOBmeas_36 | Surface tension liquid-gas, N/m | search_system_registry |
| GLOBmeas_3 | Refractive index (Na D-line) | search_blocks, search_system_registry |
| GLOBmeas_8 | Viscosity, Pa*s | search_blocks, search_system_registry |
| GLOBmeas_19 | Surface tension liquid-gas, N/m | search_blocks, search_system_registry |
| GLOBmeas_14 | Electrical conductivity, S/m | search_system_registry |
| GLOBmeas_193 | Thermal conductivity, W/m/K | search_system_registry |
| GLOBmeas_163 | Refractive index (Na D-line) | search_system_registry |
| GLOBmeas_236 | Mass density, kg/m3 | search_system_registry |
| GLOBmeas_145 | Mole fraction | search_system_registry |
| GLOBmeas_38 | Binary diffusion coefficient, m2/s | search_system_registry |
| GLOBmeas_276 | Vapor or sublimation pressure, kPa | search_system_registry |
| GLOBmeas_150 | Mole fraction | search_system_registry |
| GLOBmeas_15 | Speed of sound, m/s | search_system_registry |
| GLOBmeas_205 | Viscosity, Pa*s | search_system_registry |
| GLOBmeas_155 | Boiling temperature at pressure P, K | search_system_registry |

#### Phases (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks, search_system_registry |
| GLOBphase_3 |  | search_blocks, search_system_registry |
| GLOBphase_10 |  | search_blocks, search_system_registry |

#### Variables (7 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | search_blocks, search_system_registry |
| GLOBvar_3 | Pressure, kPa | search_blocks, search_system_registry |
| GLOBvar_2 | Mole fraction | search_blocks, search_system_registry |
| GLOBvar_4 | Molality, mol/kg | search_blocks, search_system_registry |
| GLOBvar_5 | Mass fraction | search_blocks, search_system_registry |
| GLOBvar_15 | Mass ratio of solute to solvent | search_system_registry |
| GLOBvar_18 | Volume fraction | search_system_registry |

#### Constraints (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_3 | Mole fraction | search_blocks, search_system_registry |
| GLOBconstr_2 | Temperature, K | search_blocks, search_system_registry |
| GLOBconstr_1 | Pressure, kPa | search_blocks, search_system_registry |
| GLOBconstr_4 | Frequency, MHz | search_blocks, search_system_registry |
| GLOBconstr_5 | Mass fraction | search_system_registry |
| GLOBconstr_8 | Molality, mol/kg | search_blocks, search_system_registry |

#### Solvents (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | search_blocks, search_system_registry |
| GLOBsolvent_2 |  | search_system_registry |

#### Block_Types (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | search_system_registry |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 3 |
| Unique References | 58 |
| Unique Properties | 18 |
| Unique Measurements | 45 |
| Unique Phases | 3 |
| Unique Variables | 7 |
| Unique Constraints | 6 |
| Unique Solvents | 2 |
| Unique Block_Types | 1 |
| Total DOIs | 58 |
| Unique parent blocks | 113 |
| Explicit block/subsystem targets | 113 |
| Subsystem targets | 0 |
| Target-matched data points | 13,524 |

---

## 3. DOI & Block References

**Unique DOIs:** 58  |  **Parent blocks:** 113  |  **Explicit targets:** 113  |  **Subsystems:** 0  |  **Target-matched datapoints:** 4,471

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2004.11.019 | 1 | 810 | binary | search_blocks, search_system_registry |
| 10.1016/j.fluid.2005.08.018 | 3 | 13 | binary | search_blocks, search_system_registry |
| 10.1016/j.fluid.2006.04.017 | 1 | 28 | binary | search_blocks, search_system_registry |
| 10.1016/j.fluid.2007.06.007 | 2 | 30 | binary | search_blocks, search_system_registry |
| 10.1016/j.fluid.2009.10.002 | 2 | 10 | binary | search_blocks, search_system_registry |
| 10.1016/j.fluid.2009.11.014 | 2 | 36 | binary | search_blocks, search_system_registry |
| 10.1016/j.fluid.2011.06.009 | 2 | 90 | binary | search_blocks, search_system_registry |
| 10.1016/j.fluid.2012.11.026 | 2 | 48 | binary | search_blocks, search_system_registry |
| 10.1016/j.fluid.2012.12.014 | 2 | 152 | binary | search_blocks, search_system_registry |
| 10.1016/j.fluid.2013.07.001 | 1 | 42 | binary | search_blocks, search_system_registry |
| 10.1016/j.fluid.2014.05.031 | 1 | 56 | binary | search_blocks, search_system_registry |
| 10.1016/j.fluid.2014.05.032 | 1 | 140 | binary | search_blocks, search_system_registry |
| 10.1016/j.fluid.2014.07.022 | 2 | 14 | binary | search_blocks, search_system_registry |
| 10.1016/j.fluid.2015.07.012 | 2 | 168 | binary | search_blocks, search_system_registry |
| 10.1016/j.fluid.2016.08.030 | 1 | 4 | binary | search_blocks, search_system_registry |
| 10.1016/j.fluid.2017.03.010 | 2 | 34 | binary | search_blocks, search_system_registry |
| 10.1016/j.fluid.2017.09.005 | 2 | 144 | binary | search_blocks, search_system_registry |
| 10.1016/j.fluid.2018.07.014 | 1 | 17 | binary | search_blocks, search_system_registry |
| 10.1016/j.fluid.2019.03.019 | 2 | 32 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2004.07.019 | 1 | 565 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2005.06.018 | 1 | 27 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2006.08.002 | 4 | 326 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2007.05.004 | 2 | 74 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2011.10.009 | 1 | 70 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2012.08.009 | 1 | 14 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2013.08.020 | 17 | 151 | binary, ternary, unary | search_blocks, search_system_registry |
| 10.1016/j.jct.2014.05.020 | 1 | 30 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2015.06.024 | 2 | 80 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2017.07.021 | 2 | 48 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2018.02.022 | 3 | 496 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2019.02.027 | 1 | 9 | binary | search_system_registry |
| 10.1016/j.tca.2017.05.023 | 1 | 1 | binary | search_system_registry |
| 10.1021/acs.jced.5b00485 | 1 | 2 | binary | search_system_registry |
| 10.1021/acs.jced.6b00197 | 2 | 30 | binary | search_system_registry |
| 10.1021/acs.jced.6b00725 | 2 | 2 | binary | search_system_registry |
| 10.1021/acs.jced.6b01058 | 1 | 12 | binary | search_system_registry |
| 10.1021/acs.jced.7b00299 | 3 | 5 | binary | search_blocks, search_system_registry |
| 10.1021/acs.jced.7b00827 | 2 | 42 | binary | search_system_registry |
| 10.1021/acs.jced.8b00005 | 1 | 10 | binary | search_system_registry |
| 10.1021/acs.jced.8b00086 | 3 | 18 | binary | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00181 | 2 | 12 | binary | search_system_registry |
| 10.1021/acs.jced.8b00723 | 2 | 6 | binary | search_system_registry |
| 10.1021/acs.jced.8b00939 | 2 | 18 | binary | search_system_registry |
| 10.1021/acs.jced.8b01147 | 1 | 68 | binary | search_system_registry |
| 10.1021/acs.jced.9b00026 | 1 | 10 | binary | search_system_registry |
| 10.1021/je020173z | 2 | 48 | binary | search_system_registry |
| 10.1021/je030146o | 1 | 12 | binary | search_system_registry |
| 10.1021/je0495942 | 2 | 2 | binary | search_system_registry |
| 10.1021/je0497303 | 1 | 6 | binary | search_system_registry |
| 10.1021/je049875+ | 1 | 5 | binary | search_system_registry |
| 10.1021/je050537y | 2 | 56 | binary | search_system_registry |
| 10.1021/je0601098 | 2 | 24 | binary | search_system_registry |
| 10.1021/je060219e | 1 | 26 | binary | search_system_registry |
| 10.1021/je060335h | 1 | 164 | binary | search_system_registry |
| 10.1021/je2005209 | 2 | 30 | binary | search_system_registry |
| 10.1021/je200655s | 2 | 32 | binary | search_system_registry |
| 10.1021/je2008704 | 2 | 42 | binary | search_system_registry |
| 10.1021/je3007138 | 2 | 30 | binary | search_system_registry |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2004.11.019 | PROPblock_2 | declared | 810 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2005.08.018 | PROPblock_4 | declared | 2 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2005.08.018 | PROPblock_5 | declared | 7 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2005.08.018 | PROPblock_6 | declared | 4 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2006.04.017 | PROPblock_3 | declared | 28 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2007.06.007 | PROPblock_1 | declared | 15 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2007.06.007 | PROPblock_2 | declared | 15 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2009.10.002 | PROPblock_17 | declared | 5 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2009.10.002 | PROPblock_18 | declared | 5 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2009.11.014 | PROPblock_2 | declared | 18 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2009.11.014 | PROPblock_3 | declared | 18 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2011.06.009 | PROPblock_1 | declared | 45 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2011.06.009 | PROPblock_2 | declared | 45 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2012.11.026 | PROPblock_4 | declared | 24 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2012.11.026 | PROPblock_5 | declared | 24 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2012.12.014 | PROPblock_2 | declared | 76 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2012.12.014 | PROPblock_3 | declared | 76 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2013.07.001 | PROPblock_6 | declared | 42 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2014.05.031 | PROPblock_4 | declared | 56 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2014.05.032 | PROPblock_1 | declared | 140 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2014.07.022 | PROPblock_1 | declared | 7 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2014.07.022 | PROPblock_2 | declared | 7 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2015.07.012 | PROPblock_3 | declared | 84 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2015.07.012 | PROPblock_4 | declared | 84 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2016.08.030 | PROPblock_1 | declared | 4 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2017.03.010 | PROPblock_7 | declared | 17 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2017.03.010 | PROPblock_8 | declared | 17 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2017.09.005 | PROPblock_3 | declared | 72 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2017.09.005 | PROPblock_4 | declared | 72 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2018.07.014 | PROPblock_4 | declared | 17 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2019.03.019 | PROPblock_8 | declared | 16 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2019.03.019 | PROPblock_9 | declared | 16 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2004.07.019 | PROPblock_2 | declared | 565 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2005.06.018 | PROPblock_4 | declared | 27 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2006.08.002 | PROPblock_1 | declared | 25 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2006.08.002 | PROPblock_2 | declared | 19 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2006.08.002 | PROPblock_3 | declared | 4 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2006.08.002 | PROPblock_4 | declared | 278 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2007.05.004 | PROPblock_11 | declared | 37 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2007.05.004 | PROPblock_12 | declared | 37 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2011.10.009 | PROPblock_3 | declared | 70 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2012.08.009 | PROPblock_18 | declared | 14 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2013.08.020 | PROPblock_1 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.jct.2013.08.020 | PROPblock_10 | declared | 16 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2013.08.020 | PROPblock_11 | declared | 1 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2013.08.020 | PROPblock_12 | declared | 1 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2013.08.020 | PROPblock_13 | declared | 18 | binary | — | search_blocks |
| 10.1016/j.jct.2013.08.020 | PROPblock_14 | declared | 18 | binary | — | search_blocks |
| 10.1016/j.jct.2013.08.020 | PROPblock_15 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.jct.2013.08.020 | PROPblock_16 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.jct.2013.08.020 | PROPblock_17 | declared | 39 | ternary | — | search_blocks |
| 10.1016/j.jct.2013.08.020 | PROPblock_2 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.jct.2013.08.020 | PROPblock_3 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.jct.2013.08.020 | PROPblock_4 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.jct.2013.08.020 | PROPblock_5 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.jct.2013.08.020 | PROPblock_6 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.jct.2013.08.020 | PROPblock_7 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.jct.2013.08.020 | PROPblock_8 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.jct.2013.08.020 | PROPblock_9 | declared | 16 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2014.05.020 | PROPblock_1 | declared | 30 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2015.06.024 | PROPblock_7 | declared | 40 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2015.06.024 | PROPblock_8 | declared | 40 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2017.07.021 | PROPblock_3 | declared | 24 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2017.07.021 | PROPblock_4 | declared | 24 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2018.02.022 | PROPblock_19 | declared | 244 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2018.02.022 | PROPblock_20 | declared | 152 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2018.02.022 | PROPblock_21 | declared | 100 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2019.02.027 | PROPblock_21 | declared | 9 | binary | 2 | search_system_registry |
| 10.1016/j.tca.2017.05.023 | PROPblock_1 | declared | 1 | binary | 2 | search_system_registry |
| 10.1021/acs.jced.5b00485 | PROPblock_8 | declared | 2 | binary | 2 | search_system_registry |
| 10.1021/acs.jced.6b00197 | PROPblock_11 | declared | 15 | binary | 2 | search_system_registry |
| 10.1021/acs.jced.6b00197 | PROPblock_12 | declared | 15 | binary | 2 | search_system_registry |
| 10.1021/acs.jced.6b00725 | PROPblock_15 | declared | 1 | binary | 2 | search_system_registry |
| 10.1021/acs.jced.6b00725 | PROPblock_16 | declared | 1 | binary | 2 | search_system_registry |
| 10.1021/acs.jced.6b01058 | PROPblock_7 | declared | 12 | binary | 2 | search_system_registry |
| 10.1021/acs.jced.7b00299 | PROPblock_10 | declared | 2 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.7b00299 | PROPblock_11 | declared | 2 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.7b00299 | PROPblock_12 | declared | 1 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.7b00827 | PROPblock_12 | declared | 21 | binary | 2 | search_system_registry |
| 10.1021/acs.jced.7b00827 | PROPblock_13 | declared | 21 | binary | 2 | search_system_registry |
| 10.1021/acs.jced.8b00005 | PROPblock_5 | declared | 10 | binary | 2 | search_system_registry |
| 10.1021/acs.jced.8b00086 | PROPblock_46 | declared | 6 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00086 | PROPblock_47 | declared | 6 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00086 | PROPblock_48 | declared | 6 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00181 | PROPblock_10 | declared | 6 | binary | 2 | search_system_registry |
| 10.1021/acs.jced.8b00181 | PROPblock_11 | declared | 6 | binary | 2 | search_system_registry |
| 10.1021/acs.jced.8b00723 | PROPblock_12 | declared | 3 | binary | 2 | search_system_registry |
| 10.1021/acs.jced.8b00723 | PROPblock_13 | declared | 3 | binary | 2 | search_system_registry |
| 10.1021/acs.jced.8b00939 | PROPblock_17 | declared | 9 | binary | 2 | search_system_registry |
| 10.1021/acs.jced.8b00939 | PROPblock_18 | declared | 9 | binary | 2 | search_system_registry |
| 10.1021/acs.jced.8b01147 | PROPblock_6 | declared | 68 | binary | 2 | search_system_registry |
| 10.1021/acs.jced.9b00026 | PROPblock_16 | declared | 10 | binary | 2 | search_system_registry |
| 10.1021/je020173z | PROPblock_4 | declared | 24 | binary | 2 | search_system_registry |
| 10.1021/je020173z | PROPblock_5 | declared | 24 | binary | 2 | search_system_registry |
| 10.1021/je030146o | PROPblock_1 | declared | 12 | binary | 2 | search_system_registry |
| 10.1021/je0495942 | PROPblock_1 | declared | 1 | binary | 2 | search_system_registry |
| 10.1021/je0495942 | PROPblock_2 | declared | 1 | binary | 2 | search_system_registry |
| 10.1021/je0497303 | PROPblock_2 | declared | 6 | binary | 2 | search_system_registry |
| 10.1021/je049875+ | PROPblock_1 | declared | 5 | binary | 2 | search_system_registry |
| 10.1021/je050537y | PROPblock_1 | declared | 28 | binary | 2 | search_system_registry |
| 10.1021/je050537y | PROPblock_2 | declared | 28 | binary | 2 | search_system_registry |
| 10.1021/je0601098 | PROPblock_19 | declared | 12 | binary | 2 | search_system_registry |
| 10.1021/je0601098 | PROPblock_20 | declared | 12 | binary | 2 | search_system_registry |
| 10.1021/je060219e | PROPblock_1 | declared | 26 | binary | 2 | search_system_registry |
| 10.1021/je060335h | PROPblock_1 | declared | 164 | binary | 2 | search_system_registry |
| 10.1021/je2005209 | PROPblock_2 | declared | 15 | binary | 2 | search_system_registry |
| 10.1021/je2005209 | PROPblock_3 | declared | 15 | binary | 2 | search_system_registry |
| 10.1021/je200655s | PROPblock_5 | declared | 16 | binary | 2 | search_system_registry |
| 10.1021/je200655s | PROPblock_6 | declared | 16 | binary | 2 | search_system_registry |
| 10.1021/je2008704 | PROPblock_4 | declared | 21 | binary | 2 | search_system_registry |
| 10.1021/je2008704 | PROPblock_5 | declared | 21 | binary | 2 | search_system_registry |
| 10.1021/je3007138 | PROPblock_2 | declared | 15 | binary | 2 | search_system_registry |
| 10.1021/je3007138 | PROPblock_3 | declared | 15 | binary | 2 | search_system_registry |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Resolve ethanol and… | 222 | KEEP ←in 278 | 222 | 5.0 |
| 2 | 3 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=50, p… | 1,280 | KEEP ←in 30,867 | 1280 | 15.5 |
| 3 | 4 | `search_system_registry` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=100, … | 820 | KEEP ←in 14,661 | 761 | 20.0 |
| 4 | 5 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=10, l… | 1,247 | KEEP ←in 7,548 | 1247 | 14.3 |
| 5 | 6 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=50, l… | 1,117 | KEEP ←in 5,798 | 1117 | 13.1 |
| 6 | 7 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=50, l… | 537 | KEEP ←in 6,383 | 537 | 7.2 |
| 7 | 8 | `search_system_registry` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=100, … | 2,614 | KEEP ←in 14,661 | 2124 | 32.0 |
| 8 | 9 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=10, l… | 851 | KEEP ←in 4,444 | 851 | 11.7 |
| 9 | 10 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=10, l… | 843 | KEEP ←in 4,650 | 843 | 9.8 |
| 10 | 12 | `inspect_block_table` | block_number=PROPblock_9, literature=GLOBlit_3971,… | 1,101 | — | — | 0.1 |
| 11 | 1 | `L1_query` | instruction=Search for papers (literature…, purpos… | 46,426 | — | — | 342.9 |
| 12 | 1 | `search_blocks` | limit=50, literature=GLOBlit_3971, purpose=Find al… | 1,115 | KEEP ←in 9,658 | 1115 | 13.0 |
| 13 | 2 | `search_blocks` | compound=GLOBcomp_154, limit=50, literature=GLOBli… | 1,050 | KEEP ←in 9,486 | 1050 | 12.5 |
| 14 | 3 | `search_blocks` | limit=10, literature=GLOBlit_3971, purpose=Find te… | 1,297 | KEEP ←in 3,835 | 1282 | 15.5 |
| 15 | 5 | `inspect_block_table` | block_number=PROPblock_17, literature=GLOBlit_3971… | 2,083 | — | — | 0.1 |
| 16 | 2 | `L1_query` | context=GLOBlit_3971 reports isobaric…, id_catalog… | 144 | — | — | 224.2 |
| 17 | 1 | `search_blocks` | limit=50, literature=GLOBlit_3971, purpose=Find al… | 1,103 | KEEP ←in 9,658 | 1103 | 13.7 |
| 18 | 2 | `search_blocks` | compound=GLOBcomp_154, limit=50, literature=GLOBli… | 1,041 | KEEP ←in 9,486 | 1041 | 11.9 |
| 19 | 4 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_3971,… | 542 | — | — | 0.1 |
| 20 | 6 | `inspect_block_table` | block_number=PROPblock_2, literature=GLOBlit_3971,… | 559 | — | — | 0.2 |
| 21 | 7 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_3971,… | 516 | — | — | 0.6 |
| 22 | 8 | `inspect_block_table` | block_number=PROPblock_4, literature=GLOBlit_3971,… | 540 | — | — | 0.2 |
| 23 | 9 | `inspect_block_table` | block_number=PROPblock_5, literature=GLOBlit_3971,… | 557 | — | — | 0.3 |
| 24 | 10 | `inspect_block_table` | block_number=PROPblock_6, literature=GLOBlit_3971,… | 514 | — | — | 0.1 |
| 25 | 11 | `inspect_block_table` | block_number=PROPblock_7, literature=GLOBlit_3971,… | 553 | — | — | 0.1 |
| 26 | 12 | `inspect_block_table` | block_number=PROPblock_8, literature=GLOBlit_3971,… | 567 | — | — | 0.1 |
| 27 | 3 | `L1_query` | context=GLOBlit_3971 is already known…, id_catalog… | 278 | — | — | 212.4 |
| 28 | 1 | `search_blocks` | limit=50, literature=GLOBlit_3971, purpose=Find al… | 1,061 | KEEP ←in 9,658 | 1061 | 19.4 |
| 29 | 2 | `search_blocks` | compound=GLOBcomp_154, limit=50, literature=GLOBli… | 1,334 | KEEP ←in 9,486 | 1334 | 12.3 |
| 30 | 4 | `inspect_block_table` | block_number=PROPblock_13, literature=GLOBlit_3971… | 1,103 | — | — | 0.2 |
| 31 | 5 | `inspect_block_table` | block_number=PROPblock_14, literature=GLOBlit_3971… | 1,042 | — | — | 0.1 |
| 32 | 6 | `inspect_block_table` | block_number=PROPblock_15, literature=GLOBlit_3971… | 1,098 | — | — | 0.6 |
| 33 | 7 | `inspect_block_table` | block_number=PROPblock_16, literature=GLOBlit_3971… | 933 | — | — | 0.1 |
| 34 | 8 | `inspect_block_table` | block_number=PROPblock_17, literature=GLOBlit_3971… | 2,083 | — | — | 0.2 |
| 35 | 9 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_3971,… | 542 | — | — | 0.1 |
| 36 | 10 | `inspect_block_table` | block_number=PROPblock_2, literature=GLOBlit_3971,… | 559 | — | — | 0.1 |
| 37 | 11 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_3971,… | 516 | — | — | 0.1 |
| 38 | 12 | `inspect_block_table` | block_number=PROPblock_7, literature=GLOBlit_3971,… | 553 | — | — | 0.1 |
| 39 | 4 | `L1_query` | context=We already know GLOBlit_3971 …, id_catalog… | 143 | — | — | 211.8 |
| | | **TOTAL (39 tools)** | | **80,484** | | **16,968** | **1221.7** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 668 | 12,249 | 1,217 | 7.9 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,069 | 25,164 | 570 | 4.7 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,090 | 26,185 | 534 | 5.4 |
| 4 | L1-worker | claudeopus46 | 3,767 | 443 | 4,210 | 404 | 4.7 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,719 | 25,814 | 869 | 6.3 |
| 6 | L1-worker | claudeopus46 | 3,767 | 31,302 | 35,069 | 1,732 | 14.4 |
| 7 | L1-worker | claudeopus46 | 24,095 | 3,343 | 27,438 | 1,228 | 8.4 |
| 8 | L1-worker | claudeopus46 | 3,767 | 15,153 | 18,920 | 2,004 | 15.3 |
| 9 | L1-worker | claudeopus46 | 24,095 | 4,566 | 28,661 | 1,034 | 8.2 |
| 10 | L1-worker | claudeopus46 | 3,767 | 7,951 | 11,718 | 1,450 | 14.1 |
| 11 | L1-worker | claudeopus46 | 24,095 | 6,227 | 30,322 | 847 | 6.4 |
| 12 | L1-worker | claudeopus46 | 3,767 | 6,194 | 9,961 | 1,408 | 12.7 |
| 13 | L1-worker | claudeopus46 | 24,095 | 7,740 | 31,835 | 1,672 | 11.4 |
| 14 | L1-worker | claudeopus46 | 3,767 | 6,764 | 10,531 | 726 | 7.0 |
| 15 | L1-worker | claudeopus46 | 24,095 | 8,692 | 32,787 | 2,438 | 14.9 |
| 16 | L1-worker | claudeopus46 | 3,767 | 15,092 | 18,859 | 1,279 | 12.3 |
| 17 | L1-worker | claudeopus46 | 3,767 | 15,394 | 19,161 | 2,436 | 18.9 |
| 18 | L1-worker | claudeopus46 | 24,095 | 11,722 | 35,817 | 767 | 7.5 |
| 19 | L1-worker | claudeopus46 | 3,767 | 4,819 | 8,586 | 1,130 | 10.8 |
| 20 | L1-worker | claudeopus46 | 24,095 | 12,955 | 37,050 | 1,047 | 7.6 |
| 21 | L1-worker | claudeopus46 | 3,767 | 5,028 | 8,795 | 1,056 | 9.5 |
| 22 | L1-worker | claudeopus46 | 24,095 | 14,114 | 38,209 | 4,322 | 26.7 |
| 23 | L1-worker | claudeopus46 | 24,095 | 21,380 | 45,475 | 927 | 8.0 |
| 24 | L1-worker | claudeopus46 | 24,062 | 22,483 | 46,545 | 3,300 | 24.9 |
| 25 | L1-worker | claudeopus46 | 24,062 | 26,381 | 50,443 | 3,475 | 26.1 |
| 26 | L1-worker | claudeopus46 | 2,320 | 4,935 | 7,255 | 1,375 | 9.2 |
| 27 | L1-worker | claudeopus46 | 627 | 4,815 | 5,442 | 1,484 | 11.9 |
| 28 | L1-worker | claudeopus46 | 366 | 1,812 | 2,178 | 1,330 | 5.0 |
| 29 | L1-worker | claudeopus46 | 2,106 | 6,125 | 8,231 | 3,521 | 14.8 |
| 30 | L1-worker | claudeopus46 | 366 | 4,298 | 4,664 | 2,784 | 11.3 |
| 31 | L1-worker | claudeopus46 | 1,228 | 10,617 | 11,845 | 1,783 | 8.8 |
| 32 | L1-worker | claudeopus46 | 787 | 48,981 | 49,768 | 656 | 7.9 |
| 33 | L0-main | claudeopus46 | 11,581 | 26,550 | 38,131 | 2,510 | 18.1 |
| 34 | L1-worker | claudeopus46 | 24,095 | 10,561 | 34,656 | 616 | 5.1 |
| 35 | L1-worker | claudeopus46 | 3,767 | 9,987 | 13,754 | 1,616 | 12.2 |
| 36 | L1-worker | claudeopus46 | 24,095 | 11,945 | 36,040 | 1,074 | 8.6 |
| 37 | L1-worker | claudeopus46 | 3,767 | 9,860 | 13,627 | 1,571 | 12.2 |
| 38 | L1-worker | claudeopus46 | 24,095 | 13,455 | 37,550 | 2,468 | 15.2 |
| 39 | L1-worker | claudeopus46 | 3,767 | 4,148 | 7,915 | 1,662 | 15.3 |
| 40 | L1-worker | claudeopus46 | 24,095 | 15,199 | 39,294 | 3,365 | 21.0 |
| 41 | L1-worker | claudeopus46 | 24,095 | 22,942 | 47,037 | 1,827 | 14.9 |
| 42 | L1-worker | claudeopus46 | 24,095 | 25,474 | 49,569 | 6,305 | 41.9 |
| 43 | L1-worker | claudeopus46 | 24,095 | 34,757 | 58,852 | 4,979 | 31.5 |
| 44 | L1-worker | claudeopus46 | 2,320 | 3,513 | 5,833 | 1,314 | 6.8 |
| 45 | L1-worker | claudeopus46 | 627 | 3,393 | 4,020 | 979 | 6.8 |
| 46 | L1-worker | claudeopus46 | 366 | 1,751 | 2,117 | 1,269 | 4.9 |
| 47 | L1-worker | claudeopus46 | 2,106 | 5,145 | 7,251 | 4,845 | 18.0 |
| 48 | L1-worker | claudeopus46 | 366 | 5,622 | 5,988 | 3,792 | 15.6 |
| 49 | L1-worker | claudeopus46 | 787 | 90,588 | 91,375 | 646 | 8.3 |
| 50 | L0-main | claudeopus46 | 11,581 | 27,069 | 38,650 | 1,473 | 10.3 |
| 51 | L1-worker | claudeopus46 | 24,095 | 10,505 | 34,600 | 662 | 5.4 |
| 52 | L1-worker | claudeopus46 | 3,767 | 9,989 | 13,756 | 1,548 | 13.4 |
| 53 | L1-worker | claudeopus46 | 24,095 | 11,876 | 35,971 | 1,125 | 8.2 |
| 54 | L1-worker | claudeopus46 | 3,767 | 9,852 | 13,619 | 1,282 | 11.5 |
| 55 | L1-worker | claudeopus46 | 24,095 | 13,391 | 37,486 | 3,541 | 22.8 |
| 56 | L1-worker | claudeopus46 | 24,095 | 21,815 | 45,910 | 1,159 | 12.2 |
| 57 | L1-worker | claudeopus46 | 24,095 | 22,708 | 46,803 | 444 | 4.3 |
| 58 | L1-worker | claudeopus46 | 24,095 | 23,624 | 47,719 | 521 | 4.2 |
| 59 | L1-worker | claudeopus46 | 24,095 | 23,744 | 47,839 | 488 | 5.3 |
| 60 | L1-worker | claudeopus46 | 24,095 | 24,551 | 48,646 | 521 | 4.5 |
| 61 | L1-worker | claudeopus46 | 24,095 | 25,325 | 49,420 | 429 | 4.1 |
| 62 | L1-worker | claudeopus46 | 24,095 | 26,125 | 50,220 | 326 | 3.6 |
| 63 | L1-worker | claudeopus46 | 24,095 | 26,880 | 50,975 | 372 | 3.7 |
| 64 | L1-worker | claudeopus46 | 24,095 | 27,728 | 51,823 | 359 | 3.9 |
| 65 | L1-worker | claudeopus46 | 24,062 | 19,190 | 43,252 | 3,739 | 25.1 |
| 66 | L1-worker | claudeopus46 | 24,062 | 23,951 | 48,013 | 3,412 | 23.2 |
| 67 | L1-worker | claudeopus46 | 627 | 5,312 | 5,939 | 1,220 | 8.8 |
| 68 | L1-worker | claudeopus46 | 2,320 | 5,432 | 7,752 | 1,264 | 9.4 |
| 69 | L1-worker | claudeopus46 | 366 | 1,701 | 2,067 | 1,214 | 5.5 |
| 70 | L1-worker | claudeopus46 | 2,106 | 7,008 | 9,114 | 4,939 | 19.5 |
| 71 | L1-worker | claudeopus46 | 366 | 5,716 | 6,082 | 3,886 | 15.6 |
| 72 | L1-worker | claudeopus46 | 1,228 | 13,241 | 14,469 | 3,923 | 15.3 |
| 73 | L0-main | claudeopus46 | 11,581 | 27,795 | 39,376 | 1,572 | 12.1 |
| 74 | L1-worker | claudeopus46 | 24,095 | 10,446 | 34,541 | 606 | 5.5 |
| 75 | L1-worker | claudeopus46 | 3,767 | 9,985 | 13,752 | 1,609 | 19.1 |
| 76 | L1-worker | claudeopus46 | 24,095 | 11,774 | 35,869 | 1,064 | 8.5 |
| 77 | L1-worker | claudeopus46 | 3,767 | 9,854 | 13,621 | 1,541 | 12.0 |
| 78 | L1-worker | claudeopus46 | 24,095 | 13,505 | 37,600 | 2,487 | 15.0 |
| 79 | L1-worker | claudeopus46 | 24,095 | 18,999 | 43,094 | 1,768 | 13.7 |
| 80 | L1-worker | claudeopus46 | 24,095 | 20,462 | 44,557 | 572 | 6.1 |
| 81 | L1-worker | claudeopus46 | 24,095 | 21,826 | 45,921 | 800 | 6.6 |
| 82 | L1-worker | claudeopus46 | 24,095 | 23,291 | 47,386 | 719 | 6.2 |
| 83 | L1-worker | claudeopus46 | 24,095 | 24,534 | 48,629 | 725 | 6.3 |
| 84 | L1-worker | claudeopus46 | 24,095 | 26,992 | 51,087 | 649 | 8.1 |
| 85 | L1-worker | claudeopus46 | 24,095 | 27,866 | 51,961 | 607 | 5.1 |
| 86 | L1-worker | claudeopus46 | 24,095 | 28,757 | 52,852 | 414 | 4.9 |
| 87 | L1-worker | claudeopus46 | 24,095 | 29,603 | 53,698 | 440 | 3.9 |
| 88 | L1-worker | claudeopus46 | 24,062 | 21,148 | 45,210 | 3,903 | 26.0 |
| 89 | L1-worker | claudeopus46 | 24,062 | 25,529 | 49,591 | 3,425 | 24.1 |
| 90 | L1-worker | claudeopus46 | 627 | 4,964 | 5,591 | 1,501 | 10.7 |
| 91 | L1-worker | claudeopus46 | 2,320 | 5,084 | 7,404 | 1,640 | 11.4 |
| 92 | L1-worker | claudeopus46 | 2,106 | 6,601 | 8,707 | 3,302 | 15.1 |
| 93 | L1-worker | claudeopus46 | 366 | 2,077 | 2,443 | 1,554 | 6.4 |
| 94 | L1-worker | claudeopus46 | 366 | 4,079 | 4,445 | 2,659 | 11.1 |
| 95 | L1-worker | claudeopus46 | 787 | 63,974 | 64,761 | 748 | 8.4 |
| 96 | L0-main | claudeopus46 | 11,581 | 28,541 | 40,122 | 2,961 | 22.7 |
| 97 | L0-main | claudeopus46 | 2,320 | 3,129 | 5,449 | 1,134 | 5.8 |
| 98 | L0-main | claudeopus46 | 2,106 | 3,629 | 5,735 | 1,365 | 8.0 |
| 99 | L0-main | claudeopus46 | 366 | 1,609 | 1,975 | 1,085 | 4.5 |
| 100 | L0-main | claudeopus46 | 366 | 1,914 | 2,280 | 1,447 | 6.0 |
| 101 | L0-main | claudeopus46 | 560 | 5,593 | 6,153 | 614 | 4.2 |
| 102 | L0-main | claudeopus46 | 560 | 4,385 | 4,945 | 384 | 3.3 |
| 103 | L0-main | claudeopus46 | 1,156 | 7,355 | 8,511 | 1,283 | 8.2 |

