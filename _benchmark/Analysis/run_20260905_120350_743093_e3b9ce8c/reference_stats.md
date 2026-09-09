# Reference Stats — analysis-agent

**Run started:** 2026-09-05 12:03:50
**Wall time (at last flush):** 1,165.5 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 45 | 841,895 | 4,555,262 | 71,483 | 5,397,157 | 119,936 | 586.8 | claudeopus46 |
| L1-worker | 118 | 1,652,653 | 804,740 | 136,369 | 2,457,393 | 20,825 | 1050.5 | claudeopus46 |
| **TOTAL** | **163** | **2,494,548** | **5,360,002** | **207,852** | **7,854,550** | **48,187** | **1637.3** | |

**Estimated tokens:** ~1,963,637 input + ~51,963 output = ~2,015,600 total
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
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 3 | 2 | 2 | 2 | 3 | 151 |
| `search_blocks` | 2 | 1 | 3 | 1 | 2 | 2 | 155 |
| `search_blocks` | 2 | 1 | 4 | 2 | 8 | 8 | 444 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_property_ids` | 0 | 10 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 13 | 5 | 3 | 16 | 29 | 1,601 |
| `search_blocks` | 2 | 1 | 4 | 2 | 8 | 8 | 444 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 21 | 1 | 1 | 2 | 6 | 20 | 379 |
| `query_thermoml_parallel` | 2 | 5 | 4 | 2 | 9 | 12 | 123 |
| `fit_block_derived` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 1 | 1 | 1 | 0 | 7 | 7 | 30 |
| `search_blocks` | 1 | 1 | 2 | 1 | 10 | 10 | 25 |
| `search_blocks` | 1 | 1 | 1 | 0 | 10 | 10 | 32 |
| `search_blocks` | 1 | 1 | 2 | 1 | 10 | 10 | 15 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml` | 2 | 2 | 2 | 0 | 3 | 3 | 0 |
| `search_blocks` | 1 | 1 | 2 | 1 | 10 | 10 | 15 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml` | 1 | 1 | 2 | 0 | 1 | 1 | 0 |
| **TOTAL** | **49** | **43** | **35** | **17** | **102** | **133** | **3,414** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (22 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_31 |  | query_thermoml, query_thermoml_parallel, resolve_compound_ids, search_blocks |
| GLOBcomp_1 |  | query_thermoml, query_thermoml_parallel, resolve_compound_ids, search_blocks |
| GLOBcomp_8 | toluene | search_blocks |
| GLOBcomp_27 | ethylbenzene | search_blocks |
| GLOBcomp_96 | chlorobenzene | search_blocks |
| GLOBcomp_197 | bromobenzene | search_blocks |
| GLOBcomp_170 | nitrobenzene | search_blocks |
| GLOBcomp_39 | butanone | search_blocks |
| GLOBcomp_101 | 4-methylpentan-2-one | search_blocks |
| GLOBcomp_87 | cyclohexanone | search_blocks |
| GLOBcomp_529 | hexanoic acid | search_blocks |
| GLOBcomp_84 | 1-ethyl-3-methylimidazolium tetrafluoroborate | search_blocks |
| GLOBcomp_25 | 1,4-dioxane | search_blocks |
| GLOBcomp_208 | 1,3-dioxolane | search_blocks |
| GLOBcomp_156 | tetrahydropyran | search_blocks |
| GLOBcomp_23 | tetrahydrofuran | search_blocks |
| GLOBcomp_180 | 1,2-dimethoxyethane | search_blocks |
| GLOBcomp_1162 | 1,2-diethoxyethane | search_blocks |
| GLOBcomp_4 | methanol | search_blocks |
| GLOBcomp_2 | ethanol | search_blocks |
| GLOBcomp_5 | propan-1-ol | search_blocks |
| GLOBcomp_7 | butan-1-ol | search_blocks |

#### References (56 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_2652 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_10766 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_2781 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_11517 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_2584 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_2844 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_5953 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_7713 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_11018 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_663 |  | search_blocks |
| GLOBlit_2842 |  | search_blocks |
| GLOBlit_5958 |  | search_blocks |
| GLOBlit_9547 |  | search_blocks |
| GLOBlit_10024 |  | search_blocks |
| GLOBlit_10109 |  | search_blocks |
| GLOBlit_10215 |  | search_blocks |
| GLOBlit_577 |  | search_blocks |
| GLOBlit_2816 |  | search_blocks |
| GLOBlit_3440 |  | search_blocks |
| GLOBlit_3810 |  | search_blocks |
| GLOBlit_5705 |  | search_blocks |
| GLOBlit_5731 |  | search_blocks |
| GLOBlit_3114 |  | search_blocks |
| GLOBlit_3840 |  | query_thermoml, search_blocks |
| GLOBlit_3869 |  | search_blocks |
| GLOBlit_4186 |  | search_blocks |
| GLOBlit_4715 |  | search_blocks |
| GLOBlit_8444 |  | search_blocks |
| GLOBlit_779 |  | search_blocks |
| GLOBlit_1246 |  | search_blocks |
| GLOBlit_2957 |  | query_thermoml, search_blocks |
| GLOBlit_3755 |  | search_blocks |
| GLOBlit_3879 |  | search_blocks |
| GLOBlit_5049 |  | search_blocks |
| GLOBlit_5058 |  | search_blocks |
| GLOBlit_5197 |  | search_blocks |
| GLOBlit_6204 |  | search_blocks |
| GLOBlit_522 |  | search_blocks |
| GLOBlit_725 |  | query_thermoml, search_blocks |
| GLOBlit_1065 |  | search_blocks |
| GLOBlit_1623 |  | search_blocks |
| GLOBlit_1671 |  | search_blocks |
| GLOBlit_1747 |  | search_blocks |
| GLOBlit_2239 |  | search_blocks |
| GLOBlit_3131 |  | search_blocks |
| GLOBlit_3286 |  | search_blocks |
| GLOBlit_3548 |  | search_blocks |
| GLOBlit_226 |  | search_blocks |
| GLOBlit_306 |  | query_thermoml, search_blocks |
| GLOBlit_560 |  | search_blocks |
| GLOBlit_604 |  | search_blocks |
| GLOBlit_645 |  | search_blocks |
| GLOBlit_1136 |  | search_blocks |
| GLOBlit_1161 |  | search_blocks |
| GLOBlit_1182 |  | search_blocks |
| GLOBlit_1204 |  | search_blocks |

#### Properties (22 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_8 | Speed of sound, m/s | query_thermoml_parallel, search_blocks |
| GLOBprop_13 | Surface tension liquid-gas, N/m | query_thermoml, query_thermoml_parallel, search_blocks |
| GLOBprop_7 | Refractive index (Na D-line) | query_thermoml, query_thermoml_parallel, search_blocks |
| GLOBprop_4 | Viscosity, Pa*s | query_thermoml_parallel, search_blocks |
| GLOBprop_1 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBprop_17 |  | resolve_property_ids, search_blocks |
| GLOBprop_22 |  | resolve_property_ids |
| GLOBprop_28 |  | resolve_property_ids |
| GLOBprop_90 |  | resolve_property_ids |
| GLOBprop_85 |  | resolve_property_ids |
| GLOBprop_97 |  | resolve_property_ids |
| GLOBprop_75 |  | resolve_property_ids |
| GLOBprop_30 |  | resolve_property_ids |
| GLOBprop_15 |  | resolve_property_ids, search_blocks |
| GLOBprop_36 |  | resolve_property_ids |
| GLOBprop_14 | Boiling temperature at pressure P, K | search_blocks |
| GLOBprop_2 | Mole fraction | search_blocks |
| GLOBprop_9 | Molar heat capacity at constant pressure, J/K/mol | search_blocks |
| GLOBprop_64 | Apparent molar heat capacity, J/K/mol | search_blocks |
| GLOBprop_11 | Solid-liquid equilibrium temperature, K | search_blocks |
| GLOBprop_34 | Thermal conductivity, W/m/K | search_blocks |
| GLOBprop_44 | Relative permittivity at zero frequency | search_blocks |

#### Measurements (38 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_7 | Speed of sound, m/s | query_thermoml_parallel, search_blocks |
| GLOBmeas_36 | Surface tension liquid-gas, N/m | query_thermoml_parallel, search_blocks |
| GLOBmeas_163 | Refractive index (Na D-line) | query_thermoml_parallel, search_blocks |
| GLOBmeas_140 | Viscosity, Pa*s | query_thermoml_parallel, search_blocks |
| GLOBmeas_205 | Viscosity, Pa*s | query_thermoml_parallel, search_blocks |
| GLOBmeas_147 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBmeas_141 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBmeas_6 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBmeas_495 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_146 | Boiling temperature at pressure P, K | search_blocks |
| GLOBmeas_150 | Mole fraction | search_blocks |
| GLOBmeas_31 | Molar heat capacity at constant pressure, J/K/mol | search_blocks |
| GLOBmeas_811 | Speed of sound, m/s | search_blocks |
| GLOBmeas_57 | Apparent molar heat capacity, J/K/mol | search_blocks |
| GLOBmeas_4 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_15 | Speed of sound, m/s | search_blocks |
| GLOBmeas_144 | Molar enthalpy of solution, kJ/mol | search_blocks |
| GLOBmeas_130 | Solid-liquid equilibrium temperature, K | search_blocks |
| GLOBmeas_41 | Thermal conductivity, W/m/K | search_blocks |
| GLOBmeas_823 | Relative permittivity at zero frequency | search_blocks |
| GLOBmeas_1503 | Solid-liquid equilibrium temperature, K | search_blocks |
| GLOBmeas_359 | Boiling temperature at pressure P, K | search_blocks |
| GLOBmeas_145 | Mole fraction | search_blocks |
| GLOBmeas_13 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_254 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_262 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_769 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_12 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_22 | Surface tension liquid-gas, N/m | query_thermoml, search_blocks |
| GLOBmeas_19 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBmeas_714 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBmeas_3 | Refractive index (Na D-line) | query_thermoml, search_blocks |
| GLOBmeas_659 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBmeas_32 | Surface tension liquid-gas, N/m | query_thermoml, search_blocks |
| GLOBmeas_192 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBmeas_2019 | Surface tension liquid-gas, N/m | search_blocks |

#### Phases (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | query_thermoml, query_thermoml_parallel, search_blocks |
| GLOBphase_3 |  | search_blocks |

#### Variables (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | query_thermoml, query_thermoml_parallel, search_blocks |
| GLOBvar_2 | Mole fraction | query_thermoml_parallel, search_blocks |
| GLOBvar_5 | Mass fraction | query_thermoml_parallel, search_blocks |
| GLOBvar_4 | Molality, mol/kg | query_thermoml_parallel, search_blocks |
| GLOBvar_3 | Pressure, kPa | query_thermoml, search_blocks |

#### Constraints (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_3 | Mole fraction | query_thermoml_parallel, search_blocks |
| GLOBconstr_1 | Pressure, kPa | query_thermoml_parallel, search_blocks |
| GLOBconstr_2 | Temperature, K | search_blocks |

#### Solvents (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | query_thermoml_parallel, search_blocks |
| GLOBsolvent_8 |  | search_blocks |

#### Block_Types (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | query_thermoml_parallel |
| GLOBblocktype_2 |  | query_thermoml |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 22 |
| Unique References | 56 |
| Unique Properties | 22 |
| Unique Measurements | 38 |
| Unique Phases | 2 |
| Unique Variables | 5 |
| Unique Constraints | 3 |
| Unique Solvents | 2 |
| Unique Block_Types | 2 |
| Total DOIs | 56 |
| Unique parent blocks | 87 |
| Explicit block/subsystem targets | 87 |
| Subsystem targets | 0 |
| Target-matched data points | 3,824 |

---

## 3. DOI & Block References

**Unique DOIs:** 56  |  **Parent blocks:** 87  |  **Explicit targets:** 87  |  **Subsystems:** 0  |  **Target-matched datapoints:** 2,082

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2004.11.025 | 1 | 1 | unary | search_blocks |
| 10.1016/j.fluid.2005.09.009 | 1 | 1 | unary | query_thermoml, search_blocks |
| 10.1016/j.fluid.2007.05.029 | 1 | 6 | unary | search_blocks |
| 10.1016/j.fluid.2007.08.008 | 1 | 1 | unary | search_blocks |
| 10.1016/j.fluid.2007.10.017 | 5 | 79 | binary | search_blocks |
| 10.1016/j.fluid.2008.02.008 | 1 | 1 | unary | search_blocks |
| 10.1016/j.fluid.2008.07.001 | 1 | 1 | unary | search_blocks |
| 10.1016/j.fluid.2008.09.010 | 2 | 32 | binary | search_blocks |
| 10.1016/j.fluid.2009.07.010 | 1 | 1 | unary | query_thermoml, search_blocks |
| 10.1016/j.fluid.2010.01.002 | 2 | 8 | unary | search_blocks |
| 10.1016/j.fluid.2012.01.014 | 1 | 3 | unary | search_blocks |
| 10.1016/j.fluid.2012.07.032 | 1 | 3 | unary | search_blocks |
| 10.1016/j.fluid.2012.09.038 | 1 | 1 | unary | search_blocks |
| 10.1016/j.fluid.2012.11.018 | 1 | 1 | unary | search_blocks |
| 10.1016/j.fluid.2012.12.022 | 1 | 1 | unary | search_blocks |
| 10.1016/j.fluid.2013.05.001 | 1 | 1 | unary | search_blocks |
| 10.1016/j.fluid.2014.12.040 | 1 | 4 | unary | search_blocks |
| 10.1016/j.fluid.2015.03.040 | 1 | 1 | unary | search_blocks |
| 10.1016/j.fluid.2015.07.022 | 1 | 1 | unary | search_blocks |
| 10.1016/j.fluid.2018.08.011 | 1 | 6 | unary | search_blocks |
| 10.1016/j.jct.2005.07.012 | 1 | 96 | binary | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2006.01.007 | 2 | 12 | binary | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2006.12.012 | 2 | 240 | binary | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2007.04.004 | 3 | 45 | binary | search_blocks |
| 10.1016/j.jct.2007.06.007 | 3 | 87 | binary | search_blocks |
| 10.1016/j.jct.2007.06.010 | 2 | 308 | binary | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2008.05.010 | 1 | 1 | unary | query_thermoml, search_blocks |
| 10.1016/j.jct.2009.06.021 | 1 | 4 | unary | search_blocks |
| 10.1016/j.jct.2009.07.018 | 1 | 6 | unary | search_blocks |
| 10.1016/j.jct.2010.09.003 | 1 | 3 | unary | search_blocks |
| 10.1016/j.jct.2011.07.018 | 1 | 66 | binary | search_blocks |
| 10.1016/j.jct.2012.01.023 | 1 | 1 | unary | search_blocks |
| 10.1016/j.jct.2012.10.022 | 1 | 5 | unary | search_blocks |
| 10.1016/j.jct.2013.01.010 | 1 | 18 | binary | search_blocks |
| 10.1016/j.jct.2013.02.021 | 1 | 5 | unary | query_thermoml, search_blocks |
| 10.1016/j.jct.2013.04.009 | 1 | 5 | unary | search_blocks |
| 10.1016/j.jct.2013.04.022 | 1 | 1 | unary | search_blocks |
| 10.1016/j.jct.2014.06.005 | 1 | 4 | unary | search_blocks |
| 10.1016/j.jct.2016.06.004 | 1 | 4 | unary | search_blocks |
| 10.1016/j.jct.2017.06.008 | 1 | 4 | unary | search_blocks |
| 10.1016/j.jct.2017.06.020 | 1 | 1 | unary | search_blocks |
| 10.1016/j.jct.2018.02.018 | 1 | 5 | unary | search_blocks |
| 10.1016/j.tca.2006.05.010 | 7 | 104 | binary, unary | search_blocks |
| 10.1016/j.tca.2006.10.025 | 4 | 69 | binary | search_blocks |
| 10.1016/j.tca.2011.08.013 | 3 | 48 | binary | query_thermoml_parallel, search_blocks |
| 10.1016/j.tca.2011.09.009 | 1 | 1 | binary | search_blocks |
| 10.1016/j.tca.2014.11.010 | 1 | 1 | unary | search_blocks |
| 10.1021/acs.jced.8b01048 | 1 | 9 | binary | query_thermoml_parallel, search_blocks |
| 10.1021/je0497294 | 1 | 1 | unary | search_blocks |
| 10.1021/je2002607 | 1 | 5 | binary | search_blocks |
| 10.1021/je301171y | 1 | 63 | binary | search_blocks |
| 10.1021/je400149j | 3 | 373 | binary | search_blocks |
| 10.1021/je400531a | 2 | 42 | binary | search_blocks |
| 10.1021/je7001013 | 3 | 152 | binary, unary | query_thermoml_parallel, search_blocks |
| 10.1021/je700645p | 2 | 70 | binary | query_thermoml_parallel, search_blocks |
| 10.1021/je9001027 | 2 | 70 | binary | query_thermoml_parallel, search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2004.11.025 | PROPblock_1 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2005.09.009 | PROPblock_5 | declared | 1 | unary | 1 | query_thermoml, search_blocks |
| 10.1016/j.fluid.2007.05.029 | PROPblock_4 | declared | 6 | unary | — | search_blocks |
| 10.1016/j.fluid.2007.08.008 | PROPblock_5 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2007.10.017 | PROPblock_13 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.fluid.2007.10.017 | PROPblock_14 | declared | 12 | binary | — | search_blocks |
| 10.1016/j.fluid.2007.10.017 | PROPblock_15 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.fluid.2007.10.017 | PROPblock_16 | declared | 18 | binary | — | search_blocks |
| 10.1016/j.fluid.2007.10.017 | PROPblock_17 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.fluid.2008.02.008 | PROPblock_37 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2008.07.001 | PROPblock_7 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2008.09.010 | PROPblock_4 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.fluid.2008.09.010 | PROPblock_5 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.fluid.2009.07.010 | PROPblock_12 | declared | 1 | unary | 1 | query_thermoml, search_blocks |
| 10.1016/j.fluid.2010.01.002 | PROPblock_17 | declared | 4 | unary | — | search_blocks |
| 10.1016/j.fluid.2010.01.002 | PROPblock_2 | declared | 4 | unary | — | search_blocks |
| 10.1016/j.fluid.2012.01.014 | PROPblock_1 | declared | 3 | unary | — | search_blocks |
| 10.1016/j.fluid.2012.07.032 | PROPblock_1 | declared | 3 | unary | — | search_blocks |
| 10.1016/j.fluid.2012.09.038 | PROPblock_6 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2012.11.018 | PROPblock_5 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2012.12.022 | PROPblock_5 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2013.05.001 | PROPblock_3 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2014.12.040 | PROPblock_6 | declared | 4 | unary | — | search_blocks |
| 10.1016/j.fluid.2015.03.040 | PROPblock_33 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2015.07.022 | PROPblock_3 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2018.08.011 | PROPblock_1 | declared | 6 | unary | — | search_blocks |
| 10.1016/j.jct.2005.07.012 | PROPblock_8 | declared | 96 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2006.01.007 | PROPblock_3 | declared | 6 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2006.01.007 | PROPblock_4 | declared | 6 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2006.12.012 | PROPblock_3 | declared | 120 | binary | — | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2006.12.012 | PROPblock_4 | declared | 120 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2007.04.004 | PROPblock_13 | declared | 15 | binary | — | search_blocks |
| 10.1016/j.jct.2007.04.004 | PROPblock_15 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.jct.2007.04.004 | PROPblock_17 | declared | 14 | binary | — | search_blocks |
| 10.1016/j.jct.2007.06.007 | PROPblock_4 | declared | 7 | binary | — | search_blocks |
| 10.1016/j.jct.2007.06.007 | PROPblock_5 | declared | 40 | binary | — | search_blocks |
| 10.1016/j.jct.2007.06.007 | PROPblock_6 | declared | 40 | binary | — | search_blocks |
| 10.1016/j.jct.2007.06.010 | PROPblock_3 | declared | 216 | binary | — | search_blocks |
| 10.1016/j.jct.2007.06.010 | PROPblock_4 | declared | 92 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2008.05.010 | PROPblock_11 | declared | 1 | unary | 1 | query_thermoml, search_blocks |
| 10.1016/j.jct.2009.06.021 | PROPblock_1 | declared | 4 | unary | — | search_blocks |
| 10.1016/j.jct.2009.07.018 | PROPblock_4 | declared | 6 | unary | — | search_blocks |
| 10.1016/j.jct.2010.09.003 | PROPblock_3 | declared | 3 | unary | — | search_blocks |
| 10.1016/j.jct.2011.07.018 | PROPblock_13 | declared | 66 | binary | — | search_blocks |
| 10.1016/j.jct.2012.01.023 | PROPblock_12 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.jct.2012.10.022 | PROPblock_6 | declared | 5 | unary | — | search_blocks |
| 10.1016/j.jct.2013.01.010 | PROPblock_12 | declared | 18 | binary | — | search_blocks |
| 10.1016/j.jct.2013.02.021 | PROPblock_1 | declared | 5 | unary | 1 | query_thermoml, search_blocks |
| 10.1016/j.jct.2013.04.009 | PROPblock_1 | declared | 5 | unary | — | search_blocks |
| 10.1016/j.jct.2013.04.022 | PROPblock_4 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.jct.2014.06.005 | PROPblock_1 | declared | 4 | unary | — | search_blocks |
| 10.1016/j.jct.2016.06.004 | PROPblock_1 | declared | 4 | unary | — | search_blocks |
| 10.1016/j.jct.2017.06.008 | PROPblock_15 | declared | 4 | unary | — | search_blocks |
| 10.1016/j.jct.2017.06.020 | PROPblock_12 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.jct.2018.02.018 | PROPblock_3 | declared | 5 | unary | — | search_blocks |
| 10.1016/j.tca.2006.05.010 | PROPblock_2 | declared | 2 | unary | — | search_blocks |
| 10.1016/j.tca.2006.05.010 | PROPblock_23 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.tca.2006.05.010 | PROPblock_25 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.tca.2006.05.010 | PROPblock_27 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.tca.2006.05.010 | PROPblock_29 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.tca.2006.05.010 | PROPblock_31 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.tca.2006.05.010 | PROPblock_33 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.tca.2006.10.025 | PROPblock_18 | declared | 18 | binary | — | search_blocks |
| 10.1016/j.tca.2006.10.025 | PROPblock_20 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.tca.2006.10.025 | PROPblock_22 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.tca.2006.10.025 | PROPblock_24 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.tca.2011.08.013 | PROPblock_10 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.tca.2011.08.013 | PROPblock_11 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.tca.2011.08.013 | PROPblock_12 | declared | 16 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1016/j.tca.2011.09.009 | PROPblock_1 | declared | 1 | binary | — | search_blocks |
| 10.1016/j.tca.2014.11.010 | PROPblock_8 | declared | 1 | unary | — | search_blocks |
| 10.1021/acs.jced.8b01048 | PROPblock_10 | declared | 9 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1021/je0497294 | PROPblock_10 | declared | 1 | unary | — | search_blocks |
| 10.1021/je2002607 | PROPblock_1 | declared | 5 | binary | — | search_blocks |
| 10.1021/je301171y | PROPblock_5 | declared | 63 | binary | — | search_blocks |
| 10.1021/je400149j | PROPblock_5 | declared | 363 | binary | — | search_blocks |
| 10.1021/je400149j | PROPblock_6 | declared | 8 | binary | — | search_blocks |
| 10.1021/je400149j | PROPblock_7 | declared | 2 | binary | — | search_blocks |
| 10.1021/je400531a | PROPblock_16 | declared | 21 | binary | — | search_blocks |
| 10.1021/je400531a | PROPblock_17 | declared | 21 | binary | — | search_blocks |
| 10.1021/je7001013 | PROPblock_1 | declared | 7 | unary | — | search_blocks |
| 10.1021/je7001013 | PROPblock_10 | declared | 33 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1021/je7001013 | PROPblock_9 | declared | 112 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1021/je700645p | PROPblock_1 | declared | 0 | — | — | query_thermoml_parallel |
| 10.1021/je700645p | PROPblock_6 | declared | 70 | binary | — | search_blocks |
| 10.1021/je9001027 | PROPblock_3 | declared | 35 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1021/je9001027 | PROPblock_4 | declared | 35 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 1 | `query_thermoml_parallel` | queries=[{'label': 'density', 'purpos… | 209 | — | — | 0.0 |
| 2 | 2 | `query_thermoml_parallel` | queries=[{'label': 'density_dmso_wate… | 132 | — | — | 0.0 |
| 3 | 3 | `query_thermoml_parallel` | queries=[{'label': 'density_dmso_wate… | 132 | — | — | 0.0 |
| 4 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve DMSO and wa… | 193 | KEEP ←in 295 | 193 | 4.2 |
| 5 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve DMSO and wa… | 200 | KEEP ←in 295 | 200 | 4.1 |
| 6 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve DMSO and wa… | 207 | KEEP ←in 295 | 207 | 4.5 |
| 7 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve DMSO and wa… | 237 | KEEP ←in 295 | 237 | 5.5 |
| 8 | 4 | `search_blocks` | compound=['GLOBcomp_31', 'GLOBcomp_1'], limit=50, … | 1,159 | DISCARD ←in 39 | 1101 | 15.8 |
| 9 | 4 | `search_blocks` | compound=['GLOBcomp_31', 'GLOBcomp_1'], limit=50, … | 1,162 | KEEP ←in 6,060 | 1162 | 19.2 |
| 10 | 4 | `search_blocks` | compound=['GLOBcomp_31', 'GLOBcomp_1'], limit=50, … | 755 | KEEP ←in 5,330 | 693 | 20.1 |
| 11 | 4 | `search_blocks` | compound=['GLOBcomp_31', 'GLOBcomp_1'], limit=50, … | 1,066 | KEEP ←in 5,142 | 1066 | 21.2 |
| 12 | 5 | `search_blocks` | compound=['GLOBcomp_31', 'GLOBcomp_1'], limit=50, … | 985 | DISCARD ←in 39 | 927 | 20.2 |
| 13 | 6 | `inspect_block_table` | block_number=GLOBlit_2652::PROPblock_3, purpose=Gr… | 1,068 | — | — | 0.2 |
| 14 | 6 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_2781,… | 367 | — | — | 0.1 |
| 15 | 7 | `inspect_block_table` | block_number=GLOBlit_10766::PROPblock_9, purpose=G… | 1,363 | — | — | 0.1 |
| 16 | 7 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_2781,… | 1,910 | — | — | 0.1 |
| 17 | 6 | `inspect_block_table` | block_number=PROPblock_8, literature=GLOBlit_2584,… | 1,975 | — | — | 0.1 |
| 18 | 8 | `inspect_block_table` | block_number=GLOBlit_10766::PROPblock_10, purpose=… | 1,422 | — | — | 0.1 |
| 19 | 7 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_2781,… | 2,480 | — | — | 0.1 |
| 20 | 6 | `resolve_property_ids` | limit=10, min_score=50, purpose=Verify GLOBprop_17… | 352 | KEEP ←in 1,179 | 352 | 5.6 |
| 21 | 8 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_11517… | 1,184 | — | — | 0.2 |
| 22 | 8 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_11018… | 557 | — | — | 0.6 |
| 23 | 7 | `search_blocks` | compound=['GLOBcomp_31', 'GLOBcomp_1'], limit=50, … | 1,212 | KEEP ←in 18,671 | 1109 | 21.4 |
| 24 | 8 | `search_blocks` | compound=['GLOBcomp_31', 'GLOBcomp_1'], limit=50, … | 849 | DISCARD ←in 39 | 791 | 10.8 |
| 25 | 9 | `search_blocks` | compound=['GLOBcomp_31', 'GLOBcomp_1'], limit=50, … | 1,213 | KEEP ←in 5,330 | 1213 | 20.4 |
| 26 | 10 | `inspect_block_table` | block_number=PROPblock_4, literature=GLOBlit_2781,… | 2,262 | — | — | 0.5 |
| 27 | 9 | `search_blocks` | compound=GLOBcomp_31, limit=20, property=GLOBprop_… | 1,073 | KEEP ←in 13,380 | 988 | 22.3 |
| 28 | 4 | `query_thermoml_parallel` | queries=[{'label': 'density_dmso_wate… | 140,571 | — | — | 256.2 |
| 29 | 7 | `fit_block_derived` | block_number=PROPblock_4, composition_hint=mole_fr… | 301 | — | — | 0.0 |
| 30 | 10 | `fit_block_derived` | block_number=PROPblock_4, composition_hint=mole_fr… | 249 | — | — | 0.1 |
| 31 | 12 | `fit_block_derived` | block_number=PROPblock_4, composition_hint=mole_fr… | 986 | — | — | 3.1 |
| 32 | 13 | `fit_multi_system` | purpose=Fit viscosity (Arrhenius), su…, systems=[{… | 1,305 | — | — | 1.9 |
| 33 | 3 | `search_blocks` | compound=GLOBcomp_31, limit=10, property=GLOBprop_… | 1,184 | KEEP ←in 8,579 | 1184 | 21.9 |
| 34 | 4 | `search_blocks` | compound=GLOBcomp_31, limit=10, property=GLOBprop_… | 1,117 | KEEP ←in 5,625 | 1102 | 19.0 |
| 35 | 5 | `search_blocks` | compound=GLOBcomp_1, limit=10, property=GLOBprop_1… | 1,171 | KEEP ←in 5,350 | 1153 | 20.8 |
| 36 | 6 | `search_blocks` | compound=GLOBcomp_1, limit=10, property=GLOBprop_7… | 1,135 | KEEP ←in 5,651 | 1120 | 16.0 |
| 37 | 8 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_3840,… | 249 | — | — | 0.0 |
| 38 | 9 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_3840,… | 305 | — | — | 0.2 |
| 39 | 10 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_3840,… | 690 | — | — | 0.1 |
| 40 | 11 | `inspect_block_table` | block_number=PROPblock_11, literature=GLOBlit_2957… | 667 | — | — | 0.1 |
| 41 | 12 | `inspect_block_table` | block_number=PROPblock_12, literature=GLOBlit_725,… | 601 | — | — | 0.2 |
| 42 | 14 | `query_thermoml` | context=Surface tension block GLOBlit…, instructio… | 19,568 | — | — | 239.8 |
| 43 | 15 | `fit_block` | block_number=PROPblock_9, doi=10.1021/je7001013, m… | 909 | — | — | 2.0 |
| 44 | 2 | `search_blocks` | compound=GLOBcomp_1, limit=10, property=GLOBprop_7… | 1,107 | KEEP ←in 5,651 | 1107 | 16.8 |
| 45 | 3 | `inspect_block_table` | block_number=PROPblock_5, literature=GLOBlit_306, … | 249 | — | — | 0.0 |
| 46 | 4 | `inspect_block_table` | block_number=PROPblock_5, literature=GLOBlit_306, … | 340 | — | — | 0.2 |
| 47 | 5 | `inspect_block_table` | block_number=PROPblock_5, literature=GLOBlit_306, … | 654 | — | — | 0.1 |
| 48 | 16 | `query_thermoml` | context=Pure DMSO refractive index is…, instructio… | 6,993 | — | — | 79.0 |
| 49 | 17 | `fit_block` | block_number=PROPblock_10, doi=10.1021/je7001013, … | 871 | — | — | 1.8 |
| 50 | 18 | `predict_from_rk` | coeffs=[-3.58116e-06, 2.06691e-06, -…, n_points=10… | 217 | — | — | 0.2 |
| 51 | 19 | `predict_from_rk` | coeffs=[3.705556, -3.859721, 2.18303…, mixing_rule… | 222 | — | — | 0.1 |
| 52 | 20 | `predict_from_rk` | coeffs=[-0.0338936, -0.00254064, -0.…, mixing_rule… | 202 | — | — | 0.1 |
| 53 | 21 | `predict_from_rk` | coeffs=[0.197127, -0.128481, 0.08421…, mixing_rule… | 194 | — | — | 0.1 |
| | | **TOTAL (53 tools)** | | **207,781** | | **15,905** | **877.2** |

---

## 5. Compaction Events

| # | Trigger | Outcome | Before (chars) | After (chars) | Saved (chars) | Saved (%) |
|--:|---------|---------|---------------:|--------------:|--------------:|----------:|
| 1 | chars=89942>80000 | skipped_by_agent | 89,942 | 89,942 | 0 | 0.0% |
| 2 | chars=91503>80000 | skipped_by_agent | 91,503 | 91,503 | 0 | 0.0% |
| 3 | chars=92849>80000 | skipped_by_agent | 92,849 | 92,849 | 0 | 0.0% |
| 4 | chars=94483>80000 | skipped_by_agent | 94,483 | 94,483 | 0 | 0.0% |
| 5 | chars=96052>80000 | skipped_by_agent | 96,052 | 96,052 | 0 | 0.0% |
| 6 | chars=106157>80000 | skipped_by_agent | 106,157 | 106,157 | 0 | 0.0% |
| 7 | chars=107423>80000 | skipped_by_agent | 107,423 | 107,423 | 0 | 0.0% |
| 8 | chars=111107>80000 | skipped_by_agent | 111,107 | 111,107 | 0 | 0.0% |
| 9 | chars=112426>80000 | skipped_by_agent | 112,426 | 112,426 | 0 | 0.0% |
| 10 | chars=112934>80000 | skipped_by_agent | 112,934 | 112,934 | 0 | 0.0% |
| 11 | chars=113485>80000 | skipped_by_agent | 113,485 | 113,485 | 0 | 0.0% |
| 12 | chars=113970>80000 | skipped_by_agent | 113,970 | 113,970 | 0 | 0.0% |
| 13 | chars=114409>80000 | skipped_by_agent | 114,409 | 114,409 | 0 | 0.0% |

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 22,518 | 390 | 22,908 | 2,968 | 14.5 |
| 2 | L0-main | claudeopus46 | 22,518 | 974 | 23,492 | 2,204 | 11.5 |
| 3 | L0-main | claudeopus46 | 22,518 | 1,358 | 23,876 | 2,338 | 11.4 |
| 4 | L0-main | claudeopus46 | 22,518 | 1,762 | 24,280 | 1,949 | 10.2 |
| 5 | L1-worker | claudeopus46 | 24,095 | 817 | 24,912 | 606 | 4.9 |
| 6 | L1-worker | claudeopus46 | 24,095 | 853 | 24,948 | 601 | 5.1 |
| 7 | L1-worker | claudeopus46 | 24,095 | 795 | 24,890 | 578 | 5.1 |
| 8 | L1-worker | claudeopus46 | 24,095 | 916 | 25,011 | 684 | 5.7 |
| 9 | L1-worker | claudeopus46 | 24,095 | 1,837 | 25,932 | 546 | 4.5 |
| 10 | L1-worker | claudeopus46 | 24,095 | 1,815 | 25,910 | 536 | 4.4 |
| 11 | L1-worker | claudeopus46 | 24,095 | 1,894 | 25,989 | 530 | 4.6 |
| 12 | L1-worker | claudeopus46 | 24,095 | 1,950 | 26,045 | 540 | 4.2 |
| 13 | L1-worker | claudeopus46 | 3,767 | 462 | 4,229 | 326 | 3.9 |
| 14 | L1-worker | claudeopus46 | 3,767 | 462 | 4,229 | 332 | 3.9 |
| 15 | L1-worker | claudeopus46 | 3,767 | 448 | 4,215 | 361 | 4.2 |
| 16 | L1-worker | claudeopus46 | 3,767 | 448 | 4,215 | 393 | 5.2 |
| 17 | L1-worker | claudeopus46 | 24,095 | 1,439 | 25,534 | 759 | 6.2 |
| 18 | L1-worker | claudeopus46 | 24,095 | 1,455 | 25,550 | 839 | 6.4 |
| 19 | L1-worker | claudeopus46 | 24,095 | 1,535 | 25,630 | 959 | 6.6 |
| 20 | L1-worker | claudeopus46 | 24,095 | 1,493 | 25,588 | 800 | 6.1 |
| 21 | L1-worker | claudeopus46 | 24,095 | 2,153 | 26,248 | 744 | 5.6 |
| 22 | L1-worker | claudeopus46 | 24,095 | 2,214 | 26,309 | 750 | 5.0 |
| 23 | L1-worker | claudeopus46 | 24,095 | 2,143 | 26,238 | 693 | 5.8 |
| 24 | L1-worker | claudeopus46 | 24,095 | 2,278 | 26,373 | 921 | 6.2 |
| 25 | L1-worker | claudeopus46 | 3,767 | 616 | 4,383 | 1,392 | 10.5 |
| 26 | L1-worker | claudeopus46 | 3,767 | 6,720 | 10,487 | 1,493 | 14.7 |
| 27 | L1-worker | claudeopus46 | 3,767 | 5,871 | 9,638 | 1,757 | 14.8 |
| 28 | L1-worker | claudeopus46 | 3,767 | 5,687 | 9,454 | 1,541 | 15.5 |
| 29 | L1-worker | claudeopus46 | 24,095 | 3,324 | 27,419 | 733 | 5.9 |
| 30 | L1-worker | claudeopus46 | 24,095 | 3,464 | 27,559 | 2,492 | 16.5 |
| 31 | L1-worker | claudeopus46 | 24,095 | 3,170 | 27,265 | 2,537 | 16.9 |
| 32 | L1-worker | claudeopus46 | 24,095 | 2,865 | 26,960 | 2,299 | 18.1 |
| 33 | L1-worker | claudeopus46 | 3,767 | 513 | 4,280 | 1,587 | 11.8 |
| 34 | L1-worker | claudeopus46 | 24,095 | 10,175 | 34,270 | 577 | 5.5 |
| 35 | L1-worker | claudeopus46 | 24,095 | 8,559 | 32,654 | 593 | 6.0 |
| 36 | L1-worker | claudeopus46 | 24,095 | 11,566 | 35,661 | 569 | 5.7 |
| 37 | L1-worker | claudeopus46 | 24,095 | 9,275 | 33,370 | 639 | 5.3 |
| 38 | L1-worker | claudeopus46 | 24,095 | 7,637 | 31,732 | 1,499 | 11.2 |
| 39 | L1-worker | claudeopus46 | 24,095 | 4,639 | 28,734 | 880 | 10.8 |
| 40 | L1-worker | claudeopus46 | 24,095 | 13,273 | 37,368 | 526 | 5.2 |
| 41 | L1-worker | claudeopus46 | 24,095 | 9,953 | 34,048 | 688 | 7.6 |
| 42 | L1-worker | claudeopus46 | 3,767 | 1,325 | 5,092 | 565 | 5.4 |
| 43 | L1-worker | claudeopus46 | 24,095 | 11,540 | 35,635 | 683 | 8.7 |
| 44 | L1-worker | claudeopus46 | 24,095 | 5,350 | 29,445 | 766 | 6.3 |
| 45 | L1-worker | claudeopus46 | 24,095 | 12,785 | 36,880 | 1,387 | 12.2 |
| 46 | L1-worker | claudeopus46 | 24,095 | 15,034 | 39,129 | 2,367 | 18.6 |
| 47 | L1-worker | claudeopus46 | 24,095 | 13,066 | 37,161 | 2,187 | 18.1 |
| 48 | L1-worker | claudeopus46 | 3,767 | 19,033 | 22,800 | 1,439 | 13.7 |
| 49 | L1-worker | claudeopus46 | 24,095 | 13,718 | 37,813 | 1,959 | 15.4 |
| 50 | L1-worker | claudeopus46 | 24,095 | 6,909 | 31,004 | 1,067 | 8.0 |
| 51 | L1-worker | claudeopus46 | 24,095 | 21,541 | 45,636 | 3,653 | 25.9 |
| 52 | L1-worker | claudeopus46 | 24,095 | 18,472 | 42,567 | 2,995 | 23.0 |
| 53 | L1-worker | claudeopus46 | 2,320 | 2,634 | 4,954 | 910 | 6.2 |
| 54 | L1-worker | claudeopus46 | 3,767 | 457 | 4,224 | 1,141 | 8.2 |
| 55 | L1-worker | claudeopus46 | 627 | 2,514 | 3,141 | 888 | 7.4 |
| 56 | L1-worker | claudeopus46 | 3,767 | 5,777 | 9,544 | 1,414 | 13.6 |
| 57 | L1-worker | claudeopus46 | 627 | 3,286 | 3,913 | 970 | 7.2 |
| 58 | L1-worker | claudeopus46 | 2,320 | 3,406 | 5,726 | 1,013 | 7.3 |
| 59 | L1-worker | claudeopus46 | 2,106 | 3,671 | 5,777 | 1,883 | 9.9 |
| 60 | L1-worker | claudeopus46 | 2,106 | 4,322 | 6,428 | 1,677 | 8.8 |
| 61 | L1-worker | claudeopus46 | 366 | 1,347 | 1,713 | 870 | 4.5 |
| 62 | L1-worker | claudeopus46 | 366 | 1,450 | 1,816 | 973 | 4.5 |
| 63 | L1-worker | claudeopus46 | 24,095 | 8,141 | 32,236 | 1,107 | 8.1 |
| 64 | L1-worker | claudeopus46 | 24,095 | 15,378 | 39,473 | 729 | 6.6 |
| 65 | L1-worker | claudeopus46 | 366 | 2,454 | 2,820 | 1,413 | 6.4 |
| 66 | L1-worker | claudeopus46 | 366 | 2,660 | 3,026 | 1,347 | 6.9 |
| 67 | L1-worker | claudeopus46 | 787 | 25,016 | 25,803 | 585 | 7.0 |
| 68 | L1-worker | claudeopus46 | 787 | 21,311 | 22,098 | 702 | 8.0 |
| 69 | L1-worker | claudeopus46 | 3,767 | 13,784 | 17,551 | 1,611 | 14.5 |
| 70 | L1-worker | claudeopus46 | 24,095 | 9,575 | 33,670 | 2,121 | 14.3 |
| 71 | L1-worker | claudeopus46 | 2,320 | 1,318 | 3,638 | 565 | 3.2 |
| 72 | L1-worker | claudeopus46 | 2,106 | 2,256 | 4,362 | 92 | 3.6 |
| 73 | L1-worker | claudeopus46 | 627 | 1,198 | 1,825 | 677 | 5.3 |
| 74 | L1-worker | claudeopus46 | 366 | 869 | 1,235 | 67 | 1.9 |
| 75 | L1-worker | claudeopus46 | 787 | 3,756 | 4,543 | 386 | 3.1 |
| 76 | L1-worker | claudeopus46 | 24,095 | 17,973 | 42,068 | 6,607 | 49.2 |
| 77 | L1-worker | claudeopus46 | 24,095 | 31,568 | 55,663 | 3,964 | 30.6 |
| 78 | L1-worker | claudeopus46 | 2,320 | 3,195 | 5,515 | 998 | 6.6 |
| 79 | L1-worker | claudeopus46 | 627 | 3,075 | 3,702 | 1,061 | 8.1 |
| 80 | L1-worker | claudeopus46 | 366 | 1,435 | 1,801 | 963 | 4.0 |
| 81 | L1-worker | claudeopus46 | 366 | 1,472 | 1,838 | 1,048 | 5.4 |
| 82 | L1-worker | claudeopus46 | 2,106 | 4,169 | 6,275 | 2,911 | 13.8 |
| 83 | L1-worker | claudeopus46 | 366 | 3,688 | 4,054 | 1,708 | 8.2 |
| 84 | L1-worker | claudeopus46 | 787 | 43,112 | 43,899 | 1,139 | 11.9 |
| 85 | L0-main | claudeopus46 | 22,485 | 114,610 | 137,095 | 457 | 6.9 |
| 86 | L0-main | claudeopus46 | 22,518 | 113,851 | 136,369 | 2,415 | 17.8 |
| 87 | L0-main | claudeopus46 | 22,518 | 114,697 | 137,215 | 1,138 | 10.2 |
| 88 | L0-main | claudeopus46 | 22,518 | 115,490 | 138,008 | 753 | 8.3 |
| 89 | L0-main | claudeopus46 | 22,485 | 116,246 | 138,731 | 492 | 5.1 |
| 90 | L0-main | claudeopus46 | 22,518 | 115,487 | 138,005 | 830 | 6.6 |
| 91 | L0-main | claudeopus46 | 22,518 | 116,188 | 138,706 | 812 | 7.8 |
| 92 | L0-main | claudeopus46 | 22,518 | 116,965 | 139,483 | 772 | 6.3 |
| 93 | L0-main | claudeopus46 | 22,485 | 117,742 | 140,227 | 591 | 6.9 |
| 94 | L0-main | claudeopus46 | 22,518 | 116,982 | 139,500 | 831 | 7.0 |
| 95 | L0-main | claudeopus46 | 22,518 | 117,675 | 140,193 | 865 | 8.3 |
| 96 | L0-main | claudeopus46 | 22,485 | 120,919 | 143,404 | 412 | 5.9 |
| 97 | L0-main | claudeopus46 | 22,518 | 120,159 | 142,677 | 1,308 | 10.5 |
| 98 | L0-main | claudeopus46 | 22,485 | 123,823 | 146,308 | 502 | 5.7 |
| 99 | L0-main | claudeopus46 | 22,518 | 123,063 | 145,581 | 2,199 | 17.0 |
| 100 | L1-worker | claudeopus46 | 24,095 | 1,253 | 25,348 | 926 | 7.0 |
| 101 | L1-worker | claudeopus46 | 24,095 | 2,328 | 26,423 | 666 | 4.1 |
| 102 | L1-worker | claudeopus46 | 24,095 | 3,069 | 27,164 | 715 | 4.7 |
| 103 | L1-worker | claudeopus46 | 3,767 | 8,972 | 12,739 | 1,412 | 12.3 |
| 104 | L1-worker | claudeopus46 | 24,095 | 3,407 | 27,502 | 751 | 5.7 |
| 105 | L1-worker | claudeopus46 | 3,767 | 6,034 | 9,801 | 1,423 | 12.6 |
| 106 | L1-worker | claudeopus46 | 24,095 | 4,898 | 28,993 | 683 | 5.6 |
| 107 | L1-worker | claudeopus46 | 3,767 | 5,765 | 9,532 | 1,596 | 13.4 |
| 108 | L1-worker | claudeopus46 | 24,095 | 6,407 | 30,502 | 678 | 5.3 |
| 109 | L1-worker | claudeopus46 | 3,767 | 6,059 | 9,826 | 1,383 | 11.4 |
| 110 | L1-worker | claudeopus46 | 24,095 | 7,882 | 31,977 | 3,633 | 25.4 |
| 111 | L1-worker | claudeopus46 | 24,095 | 16,703 | 40,798 | 1,097 | 9.2 |
| 112 | L1-worker | claudeopus46 | 24,095 | 17,368 | 41,463 | 905 | 6.3 |
| 113 | L1-worker | claudeopus46 | 24,095 | 17,980 | 42,075 | 655 | 13.4 |
| 114 | L1-worker | claudeopus46 | 24,095 | 19,038 | 43,133 | 926 | 6.8 |
| 115 | L1-worker | claudeopus46 | 24,095 | 20,082 | 44,177 | 448 | 4.3 |
| 116 | L1-worker | claudeopus46 | 24,062 | 20,711 | 44,773 | 3,128 | 20.6 |
| 117 | L1-worker | claudeopus46 | 24,062 | 25,548 | 49,610 | 2,712 | 19.6 |
| 118 | L1-worker | claudeopus46 | 627 | 3,519 | 4,146 | 915 | 6.8 |
| 119 | L1-worker | claudeopus46 | 2,106 | 5,013 | 7,119 | 1,336 | 7.4 |
| 120 | L1-worker | claudeopus46 | 2,320 | 3,639 | 5,959 | 1,232 | 8.2 |
| 121 | L1-worker | claudeopus46 | 366 | 2,113 | 2,479 | 752 | 4.4 |
| 122 | L1-worker | claudeopus46 | 366 | 1,669 | 2,035 | 1,187 | 4.4 |
| 123 | L1-worker | claudeopus46 | 787 | 21,347 | 22,134 | 619 | 7.6 |
| 124 | L0-main | claudeopus46 | 22,485 | 140,213 | 162,698 | 535 | 6.4 |
| 125 | L0-main | claudeopus46 | 22,518 | 139,451 | 161,969 | 2,184 | 20.8 |
| 126 | L0-main | claudeopus46 | 22,485 | 142,641 | 165,126 | 499 | 6.9 |
| 127 | L0-main | claudeopus46 | 22,518 | 141,879 | 164,397 | 1,814 | 14.5 |
| 128 | L1-worker | claudeopus46 | 24,095 | 952 | 25,047 | 674 | 5.4 |
| 129 | L1-worker | claudeopus46 | 24,095 | 1,627 | 25,722 | 623 | 4.6 |
| 130 | L1-worker | claudeopus46 | 3,767 | 6,063 | 9,830 | 1,426 | 12.0 |
| 131 | L1-worker | claudeopus46 | 24,095 | 2,673 | 26,768 | 768 | 6.4 |
| 132 | L1-worker | claudeopus46 | 24,095 | 3,260 | 27,355 | 537 | 4.3 |
| 133 | L1-worker | claudeopus46 | 24,095 | 3,871 | 27,966 | 851 | 7.2 |
| 134 | L1-worker | claudeopus46 | 24,095 | 4,903 | 28,998 | 736 | 7.9 |
| 135 | L1-worker | claudeopus46 | 24,095 | 7,739 | 31,834 | 1,144 | 6.8 |
| 136 | L1-worker | claudeopus46 | 24,095 | 10,983 | 35,078 | 792 | 5.2 |
| 137 | L1-worker | claudeopus46 | 2,320 | 923 | 3,243 | 435 | 3.3 |
| 138 | L1-worker | claudeopus46 | 627 | 803 | 1,430 | 493 | 3.4 |
| 139 | L1-worker | claudeopus46 | 2,106 | 1,996 | 4,102 | 423 | 3.5 |
| 140 | L1-worker | claudeopus46 | 366 | 1,200 | 1,566 | 305 | 3.0 |
| 141 | L1-worker | claudeopus46 | 787 | 7,189 | 7,976 | 476 | 5.8 |
| 142 | L0-main | claudeopus46 | 22,485 | 148,861 | 171,346 | 436 | 6.1 |
| 143 | L0-main | claudeopus46 | 22,518 | 148,228 | 170,746 | 2,030 | 25.8 |
| 144 | L0-main | claudeopus46 | 22,485 | 151,347 | 173,832 | 542 | 8.7 |
| 145 | L0-main | claudeopus46 | 22,518 | 150,585 | 173,103 | 898 | 10.2 |
| 146 | L0-main | claudeopus46 | 22,485 | 151,900 | 174,385 | 521 | 6.2 |
| 147 | L0-main | claudeopus46 | 22,518 | 151,138 | 173,656 | 1,149 | 13.0 |
| 148 | L0-main | claudeopus46 | 22,485 | 152,496 | 174,981 | 475 | 8.7 |
| 149 | L0-main | claudeopus46 | 22,518 | 151,734 | 174,252 | 680 | 8.1 |
| 150 | L0-main | claudeopus46 | 22,485 | 153,026 | 175,511 | 457 | 6.4 |
| 151 | L0-main | claudeopus46 | 22,518 | 152,264 | 174,782 | 475 | 6.9 |
| 152 | L0-main | claudeopus46 | 22,485 | 153,510 | 175,995 | 542 | 8.5 |
| 153 | L0-main | claudeopus46 | 22,518 | 152,748 | 175,266 | 6,584 | 53.3 |
| 154 | L0-main | claudeopus46 | 22,518 | 164,707 | 187,225 | 7,331 | 58.1 |
| 155 | L0-main | claudeopus46 | 22,518 | 176,612 | 199,130 | 7,505 | 58.1 |
| 156 | L0-main | claudeopus46 | 2,106 | 10,296 | 12,402 | 984 | 7.0 |
| 157 | L0-main | claudeopus46 | 366 | 1,507 | 1,873 | 988 | 6.1 |
| 158 | L0-main | claudeopus46 | 2,320 | 9,791 | 12,111 | 1,633 | 14.5 |
| 159 | L0-main | claudeopus46 | 366 | 2,070 | 2,436 | 1,552 | 5.1 |
| 160 | L0-main | claudeopus46 | 560 | 12,304 | 12,864 | 692 | 6.1 |
| 161 | L0-main | claudeopus46 | 1,156 | 17,209 | 18,365 | 3,020 | 19.2 |
| 162 | L0-main | claudeopus46 | 366 | 3,713 | 4,079 | 2,886 | 13.8 |
| 163 | L0-main | claudeopus46 | 1,918 | 6,651 | 8,569 | 1,235 | 10.4 |

