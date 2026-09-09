# Reference Stats — query-agent

**Run started:** 2026-09-05 05:37:26
**Wall time (at last flush):** 915.8 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 11 | 64,779 | 175,650 | 16,074 | 240,429 | 21,857 | 111.8 | claudeopus46 |
| L1-worker | 89 | 1,201,462 | 983,734 | 105,243 | 2,185,196 | 24,552 | 813.5 | claudeopus46 |
| **TOTAL** | **100** | **1,266,241** | **1,159,384** | **121,317** | **2,425,625** | **24,256** | **925.3** | |

**Estimated tokens:** ~606,406 input + ~30,329 output = ~636,735 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 3 | 2 | 2 | 2 | 429 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 3 | 2 | 5 | 6 | 144 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 3 | 2 | 5 | 6 | 144 |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 27 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_system_registry` | 3 | 1 | 1 | 2 | 1 | 1 | 3 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 14 | 6 | 6 | 27 | 50 | 1,775 |
| `search_blocks` | 50 | 1 | 4 | 2 | 41 | 50 | 1,704 |
| `search_blocks` | 3 | 1 | 1 | 2 | 1 | 1 | 59 |
| `search_blocks` | 3 | 1 | 1 | 2 | 1 | 1 | 3 |
| `search_system_registry` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **74** | **22** | **24** | **21** | **84** | **118** | **4,288** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (52 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_4 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks, search_system_registry |
| GLOBcomp_2 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_5 |  | resolve_compound_ids, search_blocks, search_system_registry |
| GLOBcomp_35 | acetic acid | search_blocks, search_system_registry |
| GLOBcomp_64 | 1-ethyl-3-methylimidazolium bis((trifluoromethyl)sulfonyl)imide | search_blocks |
| GLOBcomp_55 | 1-butyl-3-methylimidazolium hexafluorophosphate | search_blocks |
| GLOBcomp_69 | oct-1-ene | search_blocks |
| GLOBcomp_686 | ethyl 3-oxobutanoate | search_blocks |
| GLOBcomp_21 | decane | search_blocks |
| GLOBcomp_48 | 2-methoxy-2-methylpropane | search_blocks |
| GLOBcomp_37 | 2,2,4-trimethylpentane | search_blocks |
| GLOBcomp_535 | pyrrole | search_blocks |
| GLOBcomp_115 | propyl ethanoate | search_blocks |
| GLOBcomp_240 | ethyl methanoate | search_blocks |
| GLOBcomp_295 | tributyl phosphate | search_blocks |
| GLOBcomp_301 | 1-butyl-4-methylpyridinium tetrafluoroborate | search_blocks |
| GLOBcomp_70 | dibutyl ether | search_blocks |
| GLOBcomp_271 | benzaldehyde | search_blocks |
| GLOBcomp_178 | cyclohexanol | search_blocks |
| GLOBcomp_1054 | diethyl ethanedioate | search_blocks |
| GLOBcomp_11 | heptane | search_blocks |
| GLOBcomp_39 | butanone | search_blocks |
| GLOBcomp_202 | triethylamine | search_blocks |
| GLOBcomp_170 | nitrobenzene | search_blocks |
| GLOBcomp_14 | benzene | search_blocks |
| GLOBcomp_8 | toluene | search_blocks |
| GLOBcomp_1789 | (-)-fenchone | search_blocks |
| GLOBcomp_826 | 1-butyl-1-methylpyrrolidinium tetracyanoborate | search_blocks |
| GLOBcomp_877 | 1-hexylpyridinium bis(trifluromethylsulfonyl)imide | search_blocks |
| GLOBcomp_189 | 2-butoxyethan-1-ol | search_blocks |
| GLOBcomp_13 | cyclohexane | search_blocks |
| GLOBcomp_42 | methylcyclohexane | search_blocks |
| GLOBcomp_413 | ethane-1,2-diamine | search_blocks |
| GLOBcomp_1000 | methyl 2-hydroxypropanoate | search_blocks |
| GLOBcomp_390 | DL-ethyl lactate | search_blocks |
| GLOBcomp_327 | 1-methylimidazole | search_blocks |
| GLOBcomp_7670 | ethyl 2-methylpropanoate | search_blocks |
| GLOBcomp_101 | 4-methylpentan-2-one | search_blocks |
| GLOBcomp_10 | ethyl acetate | search_blocks |
| GLOBcomp_6 | propan-2-ol | search_blocks |
| GLOBcomp_25 | 1,4-dioxane | search_blocks |
| GLOBcomp_345 | methyl methanoate | search_blocks |
| GLOBcomp_683 | 1,3-propanediamine | search_blocks |
| GLOBcomp_1270 | 1,2-propanediamine | search_blocks |
| GLOBcomp_31 | dimethyl sulfoxide | search_blocks |
| GLOBcomp_265 | 2,2,2-trifluoroethanol | search_blocks |
| GLOBcomp_1526 | trimethyl orthophosphate | search_blocks |
| GLOBcomp_268 | 2-pyrrolidinone | search_blocks |
| GLOBcomp_133 | formamide | search_blocks |
| GLOBcomp_9 | acetone | search_blocks |
| GLOBcomp_17 | octane | search_blocks |

#### References (74 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_2520 |  | search_blocks |
| GLOBlit_5688 |  | search_blocks |
| GLOBlit_528 |  | search_blocks |
| GLOBlit_1482 |  | search_blocks |
| GLOBlit_2574 |  | search_blocks |
| GLOBlit_4181 |  | search_blocks |
| GLOBlit_6377 |  | search_blocks |
| GLOBlit_1766 |  | search_blocks, search_system_registry |
| GLOBlit_299 |  | search_blocks |
| GLOBlit_555 |  | search_blocks |
| GLOBlit_590 |  | search_blocks |
| GLOBlit_766 |  | search_blocks |
| GLOBlit_970 |  | search_blocks |
| GLOBlit_996 |  | search_blocks |
| GLOBlit_1742 |  | search_blocks |
| GLOBlit_2060 |  | search_blocks |
| GLOBlit_2092 |  | search_blocks |
| GLOBlit_2432 |  | search_blocks |
| GLOBlit_2979 |  | search_blocks |
| GLOBlit_3518 |  | search_blocks |
| GLOBlit_3796 |  | search_blocks |
| GLOBlit_4068 |  | search_blocks |
| GLOBlit_4415 |  | search_blocks |
| GLOBlit_4843 |  | search_blocks |
| GLOBlit_5053 |  | search_blocks |
| GLOBlit_5059 |  | search_blocks |
| GLOBlit_5124 |  | search_blocks |
| GLOBlit_5585 |  | search_blocks |
| GLOBlit_6268 |  | search_blocks |
| GLOBlit_6460 |  | search_blocks |
| GLOBlit_6553 |  | search_blocks |
| GLOBlit_7085 |  | search_blocks |
| GLOBlit_7178 |  | search_blocks |
| GLOBlit_7483 |  | search_blocks |
| GLOBlit_7818 |  | search_blocks |
| GLOBlit_524 |  | search_blocks |
| GLOBlit_553 |  | search_blocks |
| GLOBlit_617 |  | search_blocks |
| GLOBlit_637 |  | search_blocks |
| GLOBlit_1128 |  | search_blocks |
| GLOBlit_1354 |  | search_blocks |
| GLOBlit_1537 |  | search_blocks |
| GLOBlit_2543 |  | search_blocks |
| GLOBlit_2731 |  | search_blocks |
| GLOBlit_2929 |  | search_blocks |
| GLOBlit_3040 |  | search_blocks |
| GLOBlit_3118 |  | search_blocks |
| GLOBlit_3393 |  | search_blocks |
| GLOBlit_3581 |  | search_blocks |
| GLOBlit_3900 |  | search_blocks |
| GLOBlit_3931 |  | search_blocks |
| GLOBlit_4002 |  | search_blocks |
| GLOBlit_4238 |  | search_blocks |
| GLOBlit_4299 |  | search_blocks |
| GLOBlit_4376 |  | search_blocks |
| GLOBlit_4402 |  | search_blocks |
| GLOBlit_4414 |  | search_blocks |
| GLOBlit_4783 |  | search_blocks |
| GLOBlit_4847 |  | search_blocks |
| GLOBlit_4940 |  | search_blocks |
| GLOBlit_5286 |  | search_blocks |
| GLOBlit_5405 |  | search_blocks |
| GLOBlit_5589 |  | search_blocks |
| GLOBlit_5601 |  | search_blocks |
| GLOBlit_5627 |  | search_blocks |
| GLOBlit_5642 |  | search_blocks |
| GLOBlit_5675 |  | search_blocks |
| GLOBlit_5720 |  | search_blocks |
| GLOBlit_5731 |  | search_blocks |
| GLOBlit_5750 |  | search_blocks |
| GLOBlit_5779 |  | search_blocks |
| GLOBlit_5836 |  | search_blocks |
| GLOBlit_6063 |  | search_blocks |
| GLOBlit_8042 |  | search_blocks |

#### Properties (15 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_17 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks, search_system_registry |
| GLOBprop_3 | Activity coefficient | search_blocks |
| GLOBprop_8 | Speed of sound, m/s | search_blocks |
| GLOBprop_1 | Mass density, kg/m3 | search_blocks |
| GLOBprop_29 | Binary diffusion coefficient, m2/s | search_blocks |
| GLOBprop_2 | Mole fraction | search_blocks |
| GLOBprop_5 | Vapor or sublimation pressure, kPa | search_blocks |
| GLOBprop_4 | Viscosity, Pa*s | search_blocks |
| GLOBprop_14 | Boiling temperature at pressure P, K | search_blocks |
| GLOBprop_45 | Azeotropic composition: mole fraction | search_blocks |
| GLOBprop_58 | Azeotropic temperature, K | search_blocks |
| GLOBprop_46 | Molar enthalpy of dilution, kJ/mol | search_blocks |
| GLOBprop_18 | Electrical conductivity, S/m | search_blocks |
| GLOBprop_15 | Molar enthalpy of solution, kJ/mol | search_blocks |
| GLOBprop_7 | Refractive index (Na D-line) | search_blocks |

#### Measurements (34 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_224 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_25 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_13 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_12 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks, search_system_registry |
| GLOBmeas_169 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_543 | Activity coefficient | search_blocks |
| GLOBmeas_1045 | Activity coefficient | search_blocks |
| GLOBmeas_1042 | Activity coefficient | search_blocks |
| GLOBmeas_7 | Speed of sound, m/s | search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_922 | Binary diffusion coefficient, m2/s | search_blocks |
| GLOBmeas_933 | Binary diffusion coefficient, m2/s | search_blocks |
| GLOBmeas_1 | Mole fraction | search_blocks |
| GLOBmeas_133 | Vapor or sublimation pressure, kPa | search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_4 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_5 | Boiling temperature at pressure P, K | search_blocks |
| GLOBmeas_39 | Azeotropic composition: mole fraction | search_blocks |
| GLOBmeas_153 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_10 | Mole fraction | search_blocks |
| GLOBmeas_66 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_6 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_14 | Electrical conductivity, S/m | search_blocks |
| GLOBmeas_137 | Boiling temperature at pressure P, K | search_blocks |
| GLOBmeas_8 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_18 | Speed of sound, m/s | search_blocks |
| GLOBmeas_144 | Molar enthalpy of solution, kJ/mol | search_blocks |
| GLOBmeas_3 | Refractive index (Na D-line) | search_blocks |
| GLOBmeas_44 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_262 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_657 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_747 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_78 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_34 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |

#### Phases (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks, search_system_registry |
| GLOBphase_3 |  | search_blocks |

#### Variables (7 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_3 | Pressure, kPa | search_blocks |
| GLOBvar_2 | Mole fraction | search_blocks, search_system_registry |
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |
| GLOBvar_32 | Initial mass fraction of solute | search_blocks |
| GLOBvar_8 | Solvent: Mole fraction | search_blocks |

#### Constraints (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_2 | Temperature, K | search_blocks, search_system_registry |
| GLOBconstr_1 | Pressure, kPa | search_blocks, search_system_registry |
| GLOBconstr_3 | Mole fraction | search_blocks |
| GLOBconstr_25 | Final mass fraction of solute | search_blocks |
| GLOBconstr_4 | Frequency, MHz | search_blocks |
| GLOBconstr_8 | Molality, mol/kg | search_blocks |

#### Block_Types (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_3 |  | search_system_registry |

#### Solvents (4 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | search_blocks |
| GLOBsolvent_9 |  | search_blocks |
| GLOBsolvent_146 |  | search_blocks |
| GLOBsolvent_6 |  | search_blocks |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 52 |
| Unique References | 74 |
| Unique Properties | 15 |
| Unique Measurements | 34 |
| Unique Phases | 2 |
| Unique Variables | 7 |
| Unique Constraints | 6 |
| Unique Block_Types | 1 |
| Unique Solvents | 4 |
| Total DOIs | 74 |
| Unique parent blocks | 108 |
| Explicit block/subsystem targets | 109 |
| Subsystem targets | 1 |
| Target-matched data points | 4,288 |

---

## 3. DOI & Block References

**Unique DOIs:** 74  |  **Parent blocks:** 108  |  **Explicit targets:** 109  |  **Subsystems:** 1  |  **Target-matched datapoints:** 4,055

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2005.08.018 | 3 | 14 | binary | search_blocks |
| 10.1016/j.fluid.2007.06.001 | 1 | 8 | binary | search_blocks |
| 10.1016/j.fluid.2007.06.007 | 3 | 62 | binary | search_blocks |
| 10.1016/j.fluid.2007.07.063 | 1 | 9 | binary | search_blocks |
| 10.1016/j.fluid.2007.07.066 | 2 | 30 | binary | search_blocks |
| 10.1016/j.fluid.2008.01.004 | 2 | 30 | binary | search_blocks |
| 10.1016/j.fluid.2008.03.012 | 1 | 78 | binary | search_blocks |
| 10.1016/j.fluid.2008.06.011 | 2 | 61 | binary, ternary | search_blocks |
| 10.1016/j.fluid.2009.12.009 | 2 | 16 | binary | search_blocks |
| 10.1016/j.fluid.2011.05.016 | 1 | 12 | binary | search_blocks |
| 10.1016/j.fluid.2011.08.009 | 1 | 28 | binary | search_blocks |
| 10.1016/j.fluid.2012.06.031 | 1 | 13 | binary | search_blocks |
| 10.1016/j.fluid.2013.10.029 | 1 | 34 | binary | search_blocks |
| 10.1016/j.fluid.2014.05.031 | 1 | 56 | binary | search_blocks |
| 10.1016/j.fluid.2014.08.022 | 2 | 43 | binary | search_blocks |
| 10.1016/j.fluid.2015.07.012 | 2 | 168 | binary | search_blocks |
| 10.1016/j.fluid.2015.07.053 | 2 | 62 | binary, ternary | search_blocks, search_system_registry |
| 10.1016/j.fluid.2017.05.012 | 4 | 34 | binary | search_blocks |
| 10.1016/j.fluid.2017.09.005 | 2 | 144 | binary | search_blocks |
| 10.1016/j.jct.2004.07.019 | 1 | 456 | binary | search_blocks |
| 10.1016/j.jct.2005.03.012 | 1 | 416 | binary | search_blocks |
| 10.1016/j.jct.2005.04.015 | 1 | 56 | binary | search_blocks |
| 10.1016/j.jct.2005.06.018 | 1 | 27 | binary | search_blocks |
| 10.1016/j.jct.2006.08.001 | 1 | 16 | binary | search_blocks |
| 10.1016/j.jct.2008.02.019 | 1 | 33 | binary | search_blocks |
| 10.1016/j.jct.2008.07.005 | 1 | 96 | binary | search_blocks |
| 10.1016/j.jct.2008.12.004 | 1 | 21 | binary | search_blocks |
| 10.1016/j.jct.2009.07.001 | 1 | 21 | binary | search_blocks |
| 10.1016/j.jct.2011.05.014 | 1 | 12 | binary | search_blocks |
| 10.1016/j.jct.2011.12.018 | 1 | 22 | binary | search_blocks |
| 10.1016/j.jct.2012.02.037 | 1 | 11 | binary | search_blocks |
| 10.1016/j.jct.2012.12.019 | 2 | 74 | binary | search_blocks |
| 10.1016/j.jct.2013.05.024 | 1 | 76 | binary | search_blocks |
| 10.1016/j.jct.2013.06.018 | 1 | 16 | binary | search_blocks |
| 10.1016/j.jct.2013.09.026 | 1 | 57 | ternary | search_blocks |
| 10.1016/j.jct.2013.11.036 | 2 | 203 | binary | search_blocks |
| 10.1016/j.jct.2014.05.020 | 1 | 30 | binary | search_blocks |
| 10.1016/j.jct.2014.09.001 | 1 | 10 | binary | search_blocks |
| 10.1016/j.jct.2015.01.003 | 2 | 76 | binary | search_blocks |
| 10.1016/j.jct.2015.04.034 | 1 | 44 | binary | search_blocks |
| 10.1016/j.jct.2015.06.004 | 1 | 39 | binary | search_blocks |
| 10.1016/j.jct.2015.06.023 | 1 | 15 | binary | search_blocks |
| 10.1016/j.jct.2015.06.024 | 2 | 80 | binary | search_blocks |
| 10.1016/j.jct.2016.08.003 | 1 | 9 | binary | search_blocks |
| 10.1016/j.jct.2016.10.001 | 2 | 36 | binary | search_blocks |
| 10.1016/j.jct.2016.10.005 | 2 | 74 | binary | search_blocks |
| 10.1016/j.jct.2016.12.036 | 1 | 9 | binary | search_blocks |
| 10.1016/j.jct.2017.06.014 | 2 | 42 | binary | search_blocks |
| 10.1016/j.jct.2017.07.003 | 1 | 36 | binary | search_blocks |
| 10.1016/j.jct.2017.10.005 | 2 | 10 | binary | search_blocks |
| 10.1016/j.jct.2018.07.013 | 2 | 22 | binary | search_blocks |
| 10.1016/j.jct.2018.12.019 | 1 | 13 | binary | search_blocks |
| 10.1016/j.jct.2019.105880 | 3 | 48 | binary | search_blocks |
| 10.1016/j.jct.2019.105884 | 1 | 22 | binary | search_blocks |
| 10.1016/j.tca.2004.09.012 | 1 | 10 | binary | search_blocks |
| 10.1016/j.tca.2005.03.009 | 1 | 27 | binary | search_blocks |
| 10.1016/j.tca.2005.06.011 | 2 | 60 | binary, ternary | search_blocks |
| 10.1016/j.tca.2005.11.041 | 1 | 57 | binary | search_blocks |
| 10.1016/j.tca.2006.02.028 | 1 | 13 | binary | search_blocks |
| 10.1016/j.tca.2006.08.006 | 2 | 380 | binary | search_blocks |
| 10.1016/j.tca.2006.10.025 | 1 | 17 | binary | search_blocks |
| 10.1016/j.tca.2007.04.012 | 1 | 25 | binary | search_blocks |
| 10.1016/j.tca.2008.02.015 | 1 | 18 | binary | search_blocks |
| 10.1016/j.tca.2009.03.014 | 1 | 14 | binary | search_blocks |
| 10.1016/j.tca.2013.02.010 | 1 | 44 | binary | search_blocks |
| 10.1016/j.tca.2015.09.022 | 1 | 1 | binary | search_blocks |
| 10.1016/j.tca.2017.05.023 | 1 | 1 | binary | search_blocks |
| 10.1016/j.tca.2018.09.022 | 1 | 1 | binary | search_blocks |
| 10.1021/acs.jced.5b00200 | 1 | 1 | binary | search_blocks |
| 10.1021/acs.jced.6b01058 | 1 | 12 | binary | search_blocks |
| 10.1021/acs.jced.7b00299 | 3 | 5 | binary | search_blocks |
| 10.1021/acs.jced.8b00181 | 2 | 10 | binary | search_blocks |
| 10.1021/acs.jced.9b00102 | 3 | 166 | binary | search_blocks |
| 10.1021/je020149l | 3 | 63 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2005.08.018 | PROPblock_7 | declared | 3 | binary | — | search_blocks |
| 10.1016/j.fluid.2005.08.018 | PROPblock_8 | declared | 7 | binary | — | search_blocks |
| 10.1016/j.fluid.2005.08.018 | PROPblock_9 | declared | 4 | binary | — | search_blocks |
| 10.1016/j.fluid.2007.06.001 | PROPblock_15 | declared | 8 | binary | — | search_blocks |
| 10.1016/j.fluid.2007.06.007 | PROPblock_1 | declared | 15 | binary | — | search_blocks |
| 10.1016/j.fluid.2007.06.007 | PROPblock_2 | declared | 15 | binary | — | search_blocks |
| 10.1016/j.fluid.2007.06.007 | PROPblock_6 | declared | 32 | binary | — | search_blocks |
| 10.1016/j.fluid.2007.07.063 | PROPblock_7 | declared | 9 | binary | — | search_blocks |
| 10.1016/j.fluid.2007.07.066 | PROPblock_7 | declared | 15 | binary | — | search_blocks |
| 10.1016/j.fluid.2007.07.066 | PROPblock_8 | declared | 15 | binary | — | search_blocks |
| 10.1016/j.fluid.2008.01.004 | PROPblock_4 | declared | 15 | binary | — | search_blocks |
| 10.1016/j.fluid.2008.01.004 | PROPblock_5 | declared | 15 | binary | — | search_blocks |
| 10.1016/j.fluid.2008.03.012 | PROPblock_4 | declared | 78 | binary | — | search_blocks |
| 10.1016/j.fluid.2008.06.011 | PROPblock_1 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.fluid.2008.06.011 | PROPblock_2 | declared | 44 | ternary | — | search_blocks |
| 10.1016/j.fluid.2009.12.009 | PROPblock_7 | declared | 8 | binary | — | search_blocks |
| 10.1016/j.fluid.2009.12.009 | PROPblock_8 | declared | 8 | binary | — | search_blocks |
| 10.1016/j.fluid.2011.05.016 | PROPblock_1 | declared | 12 | binary | — | search_blocks |
| 10.1016/j.fluid.2011.08.009 | PROPblock_6 | declared | 28 | binary | — | search_blocks |
| 10.1016/j.fluid.2012.06.031 | PROPblock_9 | declared | 13 | binary | — | search_blocks |
| 10.1016/j.fluid.2013.10.029 | PROPblock_14 | declared | 34 | binary | — | search_blocks |
| 10.1016/j.fluid.2014.05.031 | PROPblock_4 | declared | 56 | binary | — | search_blocks |
| 10.1016/j.fluid.2014.08.022 | PROPblock_1 | declared | 22 | binary | — | search_blocks |
| 10.1016/j.fluid.2014.08.022 | PROPblock_3 | declared | 21 | binary | — | search_blocks |
| 10.1016/j.fluid.2015.07.012 | PROPblock_5 | declared | 84 | binary | — | search_blocks |
| 10.1016/j.fluid.2015.07.012 | PROPblock_6 | declared | 84 | binary | — | search_blocks |
| 10.1016/j.fluid.2015.07.053 | PROPblock_1 | declared | 59 | ternary | — | search_blocks |
| 10.1016/j.fluid.2015.07.053 | PROPblock_1 | BLKsubsys_1 | 3 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2017.05.012 | PROPblock_4 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.fluid.2017.05.012 | PROPblock_5 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.fluid.2017.05.012 | PROPblock_6 | declared | 1 | binary | — | search_blocks |
| 10.1016/j.fluid.2017.05.012 | PROPblock_7 | declared | 1 | binary | — | search_blocks |
| 10.1016/j.fluid.2017.09.005 | PROPblock_5 | declared | 72 | binary | — | search_blocks |
| 10.1016/j.fluid.2017.09.005 | PROPblock_6 | declared | 72 | binary | — | search_blocks |
| 10.1016/j.jct.2004.07.019 | PROPblock_3 | declared | 456 | binary | — | search_blocks |
| 10.1016/j.jct.2005.03.012 | PROPblock_3 | declared | 416 | binary | — | search_blocks |
| 10.1016/j.jct.2005.04.015 | PROPblock_1 | declared | 56 | binary | — | search_blocks |
| 10.1016/j.jct.2005.06.018 | PROPblock_4 | declared | 27 | binary | — | search_blocks |
| 10.1016/j.jct.2006.08.001 | PROPblock_3 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.jct.2008.02.019 | PROPblock_9 | declared | 33 | binary | — | search_blocks |
| 10.1016/j.jct.2008.07.005 | PROPblock_9 | declared | 96 | binary | — | search_blocks |
| 10.1016/j.jct.2008.12.004 | PROPblock_3 | declared | 21 | binary | — | search_blocks |
| 10.1016/j.jct.2009.07.001 | PROPblock_2 | declared | 21 | binary | — | search_blocks |
| 10.1016/j.jct.2011.05.014 | PROPblock_3 | declared | 12 | binary | — | search_blocks |
| 10.1016/j.jct.2011.12.018 | PROPblock_1 | declared | 22 | binary | — | search_blocks |
| 10.1016/j.jct.2012.02.037 | PROPblock_16 | declared | 11 | binary | — | search_blocks |
| 10.1016/j.jct.2012.12.019 | PROPblock_2 | declared | 37 | binary | — | search_blocks |
| 10.1016/j.jct.2012.12.019 | PROPblock_3 | declared | 37 | binary | — | search_blocks |
| 10.1016/j.jct.2013.05.024 | PROPblock_4 | declared | 76 | binary | — | search_blocks |
| 10.1016/j.jct.2013.06.018 | PROPblock_1 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.jct.2013.09.026 | PROPblock_4 | declared | 57 | ternary | — | search_blocks |
| 10.1016/j.jct.2013.11.036 | PROPblock_1 | declared | 174 | binary | — | search_blocks |
| 10.1016/j.jct.2013.11.036 | PROPblock_2 | declared | 29 | binary | — | search_blocks |
| 10.1016/j.jct.2014.05.020 | PROPblock_1 | declared | 30 | binary | — | search_blocks |
| 10.1016/j.jct.2014.09.001 | PROPblock_14 | declared | 10 | binary | — | search_blocks |
| 10.1016/j.jct.2015.01.003 | PROPblock_1 | declared | 38 | binary | — | search_blocks |
| 10.1016/j.jct.2015.01.003 | PROPblock_2 | declared | 38 | binary | — | search_blocks |
| 10.1016/j.jct.2015.04.034 | PROPblock_4 | declared | 44 | binary | — | search_blocks |
| 10.1016/j.jct.2015.06.004 | PROPblock_25 | declared | 39 | binary | — | search_blocks |
| 10.1016/j.jct.2015.06.023 | PROPblock_6 | declared | 15 | binary | — | search_blocks |
| 10.1016/j.jct.2015.06.024 | PROPblock_5 | declared | 40 | binary | — | search_blocks |
| 10.1016/j.jct.2015.06.024 | PROPblock_6 | declared | 40 | binary | — | search_blocks |
| 10.1016/j.jct.2016.08.003 | PROPblock_17 | declared | 9 | binary | — | search_blocks |
| 10.1016/j.jct.2016.10.001 | PROPblock_7 | declared | 18 | binary | — | search_blocks |
| 10.1016/j.jct.2016.10.001 | PROPblock_8 | declared | 18 | binary | — | search_blocks |
| 10.1016/j.jct.2016.10.005 | PROPblock_1 | declared | 37 | binary | — | search_blocks |
| 10.1016/j.jct.2016.10.005 | PROPblock_2 | declared | 37 | binary | — | search_blocks |
| 10.1016/j.jct.2016.12.036 | PROPblock_24 | declared | 9 | binary | — | search_blocks |
| 10.1016/j.jct.2017.06.014 | PROPblock_3 | declared | 21 | binary | — | search_blocks |
| 10.1016/j.jct.2017.06.014 | PROPblock_4 | declared | 21 | binary | — | search_blocks |
| 10.1016/j.jct.2017.07.003 | PROPblock_6 | declared | 36 | binary | — | search_blocks |
| 10.1016/j.jct.2017.10.005 | PROPblock_13 | declared | 5 | binary | — | search_blocks |
| 10.1016/j.jct.2017.10.005 | PROPblock_14 | declared | 5 | binary | — | search_blocks |
| 10.1016/j.jct.2018.07.013 | PROPblock_21 | declared | 11 | binary | — | search_blocks |
| 10.1016/j.jct.2018.07.013 | PROPblock_33 | declared | 11 | binary | — | search_blocks |
| 10.1016/j.jct.2018.12.019 | PROPblock_19 | declared | 13 | binary | — | search_blocks |
| 10.1016/j.jct.2019.105880 | PROPblock_7 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.jct.2019.105880 | PROPblock_8 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.jct.2019.105880 | PROPblock_9 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.jct.2019.105884 | PROPblock_24 | declared | 22 | binary | — | search_blocks |
| 10.1016/j.tca.2004.09.012 | PROPblock_10 | declared | 10 | binary | — | search_blocks |
| 10.1016/j.tca.2005.03.009 | PROPblock_3 | declared | 27 | binary | — | search_blocks |
| 10.1016/j.tca.2005.06.011 | PROPblock_1 | declared | 3 | binary | — | search_blocks |
| 10.1016/j.tca.2005.06.011 | PROPblock_2 | declared | 57 | ternary | — | search_blocks |
| 10.1016/j.tca.2005.11.041 | PROPblock_1 | declared | 57 | binary | — | search_blocks |
| 10.1016/j.tca.2006.02.028 | PROPblock_1 | declared | 13 | binary | — | search_blocks |
| 10.1016/j.tca.2006.08.006 | PROPblock_13 | declared | 185 | binary | — | search_blocks |
| 10.1016/j.tca.2006.08.006 | PROPblock_15 | declared | 195 | binary | — | search_blocks |
| 10.1016/j.tca.2006.10.025 | PROPblock_22 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.tca.2007.04.012 | PROPblock_12 | declared | 25 | binary | — | search_blocks |
| 10.1016/j.tca.2008.02.015 | PROPblock_3 | declared | 18 | binary | — | search_blocks |
| 10.1016/j.tca.2009.03.014 | PROPblock_14 | declared | 14 | binary | — | search_blocks |
| 10.1016/j.tca.2013.02.010 | PROPblock_8 | declared | 44 | binary | — | search_blocks |
| 10.1016/j.tca.2015.09.022 | PROPblock_43 | declared | 1 | binary | — | search_blocks |
| 10.1016/j.tca.2017.05.023 | PROPblock_1 | declared | 1 | binary | — | search_blocks |
| 10.1016/j.tca.2018.09.022 | PROPblock_5 | declared | 1 | binary | — | search_blocks |
| 10.1021/acs.jced.5b00200 | PROPblock_19 | declared | 1 | binary | — | search_blocks |
| 10.1021/acs.jced.6b01058 | PROPblock_8 | declared | 12 | binary | — | search_blocks |
| 10.1021/acs.jced.7b00299 | PROPblock_13 | declared | 2 | binary | — | search_blocks |
| 10.1021/acs.jced.7b00299 | PROPblock_14 | declared | 2 | binary | — | search_blocks |
| 10.1021/acs.jced.7b00299 | PROPblock_15 | declared | 1 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00181 | PROPblock_8 | declared | 5 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00181 | PROPblock_9 | declared | 5 | binary | — | search_blocks |
| 10.1021/acs.jced.9b00102 | PROPblock_11 | declared | 60 | binary | — | search_blocks |
| 10.1021/acs.jced.9b00102 | PROPblock_12 | declared | 60 | binary | — | search_blocks |
| 10.1021/acs.jced.9b00102 | PROPblock_13 | declared | 46 | binary | — | search_blocks |
| 10.1021/je020149l | PROPblock_10 | declared | 21 | binary | — | search_blocks |
| 10.1021/je020149l | PROPblock_11 | declared | 20 | binary | — | search_blocks |
| 10.1021/je020149l | PROPblock_12 | declared | 22 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Resolve methanol an… | 171 | KEEP ←in 277 | 171 | 3.8 |
| 2 | 3 | `search_blocks` | compound=['GLOBcomp_4', 'GLOBcomp_1'], limit=20, p… | 1,164 | KEEP ←in 4,068 | 1164 | 18.7 |
| 3 | 4 | `inspect_block_table` | block_number=GLOBlit_5688::PROPblock_1, purpose=Ge… | 1,381 | — | — | 0.1 |
| 4 | 5 | `inspect_block_table` | block_number=GLOBlit_2520::PROPblock_3, nearest=mo… | 265 | — | — | 0.0 |
| 5 | 6 | `inspect_block_table` | block_number=GLOBlit_2520::PROPblock_3, nearest={'… | 415 | — | — | 0.2 |
| 6 | 7 | `inspect_block_table` | block_number=GLOBlit_2520::PROPblock_3, nearest={'… | 1,012 | — | — | 0.1 |
| 7 | 1 | `L1_query` | context=Investigating nonideality tre…, id_catalog… | 21,186 | — | — | 126.6 |
| 8 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve ethanol to … | 208 | KEEP ←in 222 | 208 | 5.4 |
| 9 | 3 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=50, p… | 373 | KEEP ←in 8,333 | 373 | 15.4 |
| 10 | 4 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_528, … | 1,588 | — | — | 0.1 |
| 11 | 5 | `inspect_block_table` | block_number=PROPblock_2, literature=GLOBlit_528, … | 1,529 | — | — | 0.3 |
| 12 | 6 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_2574,… | 1,558 | — | — | 0.1 |
| 13 | 7 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=20, p… | 621 | KEEP ←in 8,333 | 621 | 23.5 |
| 14 | 8 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], literature=… | 893 | KEEP ←in 2,171 | 878 | 9.6 |
| 15 | 9 | `inspect_block_table` | block_number=PROPblock_4, literature=GLOBlit_2574,… | 1,512 | — | — | 1.2 |
| 16 | 12 | `inspect_block_table` | block_number=GLOBlit_5688::PROPblock_1, nearest={'… | 1,044 | — | — | 0.1 |
| 17 | 2 | `L1_query` | context=Building a comparison of Hᴱ a…, id_catalog… | 37,745 | — | — | 263.0 |
| 18 | 1 | `resolve_compound_ids` | limit=10, min_score=50, purpose=Resolve 1-propanol… | 255 | KEEP ←in 227 | 255 | 4.9 |
| 19 | 3 | `search_blocks` | compound=['GLOBcomp_5', 'GLOBcomp_1'], limit=20, p… | 950 | DISCARD ←in 39 | 892 | 16.3 |
| 20 | 4 | `search_blocks` | compound=['GLOBcomp_5', 'GLOBcomp_1'], limit=50, p… | 967 | DISCARD ←in 39 | 909 | 16.1 |
| 21 | 5 | `search_system_registry` | compound=['GLOBcomp_5', 'GLOBcomp_1'], limit=20, p… | 707 | KEEP ←in 683 | 677 | 11.0 |
| 22 | 6 | `inspect_block_table` | BLKsubsys_id=BLKsubsys_1, block_number=PROPblock_1… | 970 | — | — | 0.2 |
| 23 | 3 | `L1_query` | context=Building a chain-length trend…, id_catalog… | 383 | — | — | 166.4 |
| 24 | 2 | `resolve_compound_ids` | limit=10, min_score=50, purpose=Resolve 1-propanol… | 253 | KEEP ←in 227 | 253 | 4.9 |
| 25 | 3 | `search_blocks` | compound=['GLOBcomp_5', 'GLOBcomp_1'], limit=20, p… | 960 | DISCARD ←in 39 | 902 | 10.5 |
| 26 | 4 | `search_blocks` | compound=['GLOBcomp_5', 'GLOBcomp_1'], limit=50, p… | 596 | KEEP ←in 31,749 | 563 | 16.6 |
| 27 | 5 | `search_blocks` | compound=GLOBcomp_5, limit=50, property=GLOBprop_1… | 1,263 | KEEP ←in 34,310 | 1159 | 18.8 |
| 28 | 6 | `search_blocks` | compound=['GLOBcomp_5', 'GLOBcomp_1'], limit=50, p… | 915 | KEEP ←in 3,038 | 885 | 22.6 |
| 29 | 7 | `search_blocks` | compound=['GLOBcomp_5', 'GLOBcomp_1'], limit=50, p… | 886 | KEEP ←in 815 | 856 | 10.9 |
| 30 | 8 | `search_system_registry` | compound=['GLOBcomp_5', 'GLOBcomp_1'], limit=100, … | 383 | KEEP ←in 39 | 383 | 11.9 |
| 31 | 10 | `inspect_block_table` | block_number=GLOBlit_1766::PROPblock_1, purpose=In… | 3,154 | — | — | 0.1 |
| 32 | 11 | `inspect_block_table` | block_number=GLOBlit_5688::PROPblock_1, purpose=Gr… | 1,381 | — | — | 0.1 |
| 33 | 4 | `L1_query` | context=Comparing nonideality of alco…, id_catalog… | 19,054 | — | — | 256.2 |
| | | **TOTAL (33 tools)** | | **105,742** | | **11,149** | **1035.7** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 547 | 12,128 | 1,673 | 10.4 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,055 | 25,150 | 657 | 4.9 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,073 | 26,168 | 541 | 4.0 |
| 4 | L1-worker | claudeopus46 | 3,767 | 438 | 4,205 | 352 | 3.7 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,656 | 25,751 | 740 | 5.8 |
| 6 | L1-worker | claudeopus46 | 3,767 | 4,481 | 8,248 | 1,360 | 12.1 |
| 7 | L1-worker | claudeopus46 | 24,095 | 3,164 | 27,259 | 885 | 6.7 |
| 8 | L1-worker | claudeopus46 | 24,095 | 4,820 | 28,915 | 858 | 8.1 |
| 9 | L1-worker | claudeopus46 | 24,095 | 5,495 | 29,590 | 535 | 5.1 |
| 10 | L1-worker | claudeopus46 | 24,095 | 6,174 | 30,269 | 641 | 5.3 |
| 11 | L1-worker | claudeopus46 | 24,095 | 7,484 | 31,579 | 2,413 | 18.2 |
| 12 | L1-worker | claudeopus46 | 24,095 | 12,760 | 36,855 | 3,312 | 23.4 |
| 13 | L1-worker | claudeopus46 | 627 | 2,502 | 3,129 | 864 | 5.6 |
| 14 | L1-worker | claudeopus46 | 2,106 | 3,798 | 5,904 | 1,037 | 5.7 |
| 15 | L1-worker | claudeopus46 | 2,320 | 2,622 | 4,942 | 1,094 | 6.1 |
| 16 | L1-worker | claudeopus46 | 366 | 1,814 | 2,180 | 811 | 4.4 |
| 17 | L1-worker | claudeopus46 | 366 | 1,531 | 1,897 | 1,054 | 4.2 |
| 18 | L1-worker | claudeopus46 | 1,228 | 5,189 | 6,417 | 809 | 4.9 |
| 19 | L1-worker | claudeopus46 | 787 | 18,984 | 19,771 | 386 | 5.3 |
| 20 | L0-main | claudeopus46 | 11,581 | 16,874 | 28,455 | 1,561 | 13.0 |
| 21 | L1-worker | claudeopus46 | 24,095 | 7,525 | 31,620 | 586 | 5.4 |
| 22 | L1-worker | claudeopus46 | 24,095 | 8,532 | 32,627 | 539 | 4.3 |
| 23 | L1-worker | claudeopus46 | 3,767 | 384 | 4,151 | 372 | 4.8 |
| 24 | L1-worker | claudeopus46 | 24,095 | 8,172 | 32,267 | 674 | 5.4 |
| 25 | L1-worker | claudeopus46 | 3,767 | 8,735 | 12,502 | 1,488 | 14.2 |
| 26 | L1-worker | claudeopus46 | 24,095 | 8,860 | 32,955 | 858 | 6.9 |
| 27 | L1-worker | claudeopus46 | 24,095 | 10,823 | 34,918 | 826 | 6.7 |
| 28 | L1-worker | claudeopus46 | 24,095 | 12,688 | 36,783 | 810 | 6.8 |
| 29 | L1-worker | claudeopus46 | 24,095 | 14,568 | 38,663 | 2,362 | 17.1 |
| 30 | L1-worker | claudeopus46 | 3,767 | 8,782 | 12,549 | 1,700 | 17.9 |
| 31 | L1-worker | claudeopus46 | 24,095 | 15,592 | 39,687 | 1,235 | 9.5 |
| 32 | L1-worker | claudeopus46 | 3,767 | 2,585 | 6,352 | 1,204 | 9.5 |
| 33 | L1-worker | claudeopus46 | 24,095 | 16,871 | 40,966 | 600 | 6.8 |
| 34 | L1-worker | claudeopus46 | 24,095 | 18,679 | 42,774 | 3,714 | 26.6 |
| 35 | L1-worker | claudeopus46 | 24,095 | 27,771 | 51,866 | 4,033 | 29.9 |
| 36 | L1-worker | claudeopus46 | 24,095 | 35,596 | 59,691 | 861 | 7.4 |
| 37 | L1-worker | claudeopus46 | 24,062 | 30,488 | 54,550 | 2,818 | 22.2 |
| 38 | L1-worker | claudeopus46 | 24,062 | 33,149 | 57,211 | 2,552 | 20.9 |
| 39 | L1-worker | claudeopus46 | 2,320 | 3,213 | 5,533 | 1,147 | 8.8 |
| 40 | L1-worker | claudeopus46 | 2,106 | 4,670 | 6,776 | 1,802 | 9.9 |
| 41 | L1-worker | claudeopus46 | 627 | 3,093 | 3,720 | 1,009 | 12.8 |
| 42 | L1-worker | claudeopus46 | 366 | 1,584 | 1,950 | 1,107 | 4.9 |
| 43 | L1-worker | claudeopus46 | 366 | 2,579 | 2,945 | 1,067 | 5.8 |
| 44 | L1-worker | claudeopus46 | 1,228 | 6,474 | 7,702 | 1,059 | 5.3 |
| 45 | L1-worker | claudeopus46 | 787 | 25,991 | 26,778 | 615 | 7.3 |
| 46 | L0-main | claudeopus46 | 11,581 | 39,881 | 51,462 | 1,575 | 15.1 |
| 47 | L1-worker | claudeopus46 | 24,095 | 14,655 | 38,750 | 686 | 6.2 |
| 48 | L1-worker | claudeopus46 | 3,767 | 396 | 4,163 | 393 | 3.8 |
| 49 | L1-worker | claudeopus46 | 24,095 | 15,170 | 39,265 | 790 | 6.3 |
| 50 | L1-worker | claudeopus46 | 24,095 | 15,905 | 40,000 | 611 | 5.1 |
| 51 | L1-worker | claudeopus46 | 3,767 | 549 | 4,316 | 1,405 | 10.7 |
| 52 | L1-worker | claudeopus46 | 24,095 | 16,796 | 40,891 | 774 | 5.6 |
| 53 | L1-worker | claudeopus46 | 3,767 | 528 | 4,295 | 1,655 | 11.5 |
| 54 | L1-worker | claudeopus46 | 24,095 | 18,096 | 42,191 | 827 | 6.5 |
| 55 | L1-worker | claudeopus46 | 3,767 | 1,114 | 4,881 | 1,046 | 8.5 |
| 56 | L1-worker | claudeopus46 | 24,095 | 19,151 | 43,246 | 828 | 10.9 |
| 57 | L1-worker | claudeopus46 | 24,095 | 20,499 | 44,594 | 2,522 | 17.3 |
| 58 | L1-worker | claudeopus46 | 24,095 | 26,183 | 50,278 | 4,367 | 30.9 |
| 59 | L1-worker | claudeopus46 | 24,095 | 32,798 | 56,893 | 2,805 | 14.7 |
| 60 | L1-worker | claudeopus46 | 2,106 | 3,154 | 5,260 | 527 | 4.3 |
| 61 | L1-worker | claudeopus46 | 2,320 | 1,527 | 3,847 | 727 | 4.6 |
| 62 | L1-worker | claudeopus46 | 627 | 1,407 | 2,034 | 780 | 5.2 |
| 63 | L1-worker | claudeopus46 | 366 | 1,304 | 1,670 | 425 | 2.9 |
| 64 | L1-worker | claudeopus46 | 366 | 1,164 | 1,530 | 696 | 3.2 |
| 65 | L1-worker | claudeopus46 | 1,228 | 4,057 | 5,285 | 547 | 4.2 |
| 66 | L0-main | claudeopus46 | 11,581 | 40,684 | 52,265 | 1,415 | 11.0 |
| 67 | L1-worker | claudeopus46 | 24,095 | 14,600 | 38,695 | 625 | 5.9 |
| 68 | L1-worker | claudeopus46 | 24,095 | 15,626 | 39,721 | 572 | 4.5 |
| 69 | L1-worker | claudeopus46 | 3,767 | 373 | 4,140 | 440 | 4.4 |
| 70 | L1-worker | claudeopus46 | 24,095 | 15,315 | 39,410 | 784 | 6.2 |
| 71 | L1-worker | claudeopus46 | 3,767 | 508 | 4,275 | 1,575 | 10.1 |
| 72 | L1-worker | claudeopus46 | 24,095 | 16,617 | 40,712 | 808 | 6.3 |
| 73 | L1-worker | claudeopus46 | 3,767 | 32,149 | 35,916 | 1,843 | 14.7 |
| 74 | L1-worker | claudeopus46 | 24,095 | 17,568 | 41,663 | 1,392 | 9.5 |
| 75 | L1-worker | claudeopus46 | 3,767 | 34,683 | 38,450 | 1,526 | 15.5 |
| 76 | L1-worker | claudeopus46 | 24,095 | 19,199 | 43,294 | 1,047 | 7.7 |
| 77 | L1-worker | claudeopus46 | 3,767 | 3,428 | 7,195 | 1,791 | 17.0 |
| 78 | L1-worker | claudeopus46 | 24,095 | 20,472 | 44,567 | 1,467 | 10.6 |
| 79 | L1-worker | claudeopus46 | 3,767 | 1,238 | 5,005 | 1,232 | 8.3 |
| 80 | L1-worker | claudeopus46 | 24,095 | 21,806 | 45,901 | 1,626 | 11.3 |
| 81 | L1-worker | claudeopus46 | 3,767 | 548 | 4,315 | 600 | 5.7 |
| 82 | L1-worker | claudeopus46 | 24,095 | 22,587 | 46,682 | 1,732 | 13.2 |
| 83 | L1-worker | claudeopus46 | 24,095 | 26,738 | 50,833 | 1,359 | 10.0 |
| 84 | L1-worker | claudeopus46 | 24,095 | 30,248 | 54,343 | 977 | 11.1 |
| 85 | L1-worker | claudeopus46 | 24,095 | 31,996 | 56,091 | 1,420 | 13.6 |
| 86 | L1-worker | claudeopus46 | 24,062 | 22,575 | 46,637 | 1,633 | 14.7 |
| 87 | L1-worker | claudeopus46 | 24,062 | 24,163 | 48,225 | 1,430 | 15.3 |
| 88 | L1-worker | claudeopus46 | 2,106 | 3,133 | 5,239 | 92 | 2.3 |
| 89 | L1-worker | claudeopus46 | 366 | 869 | 1,235 | 67 | 1.9 |
| 90 | L1-worker | claudeopus46 | 627 | 1,441 | 2,068 | 1,075 | 5.3 |
| 91 | L1-worker | claudeopus46 | 2,320 | 1,561 | 3,881 | 962 | 6.2 |
| 92 | L1-worker | claudeopus46 | 366 | 1,399 | 1,765 | 922 | 4.7 |
| 93 | L1-worker | claudeopus46 | 787 | 4,997 | 5,784 | 448 | 4.5 |
| 94 | L0-main | claudeopus46 | 11,581 | 53,833 | 65,414 | 4,902 | 31.8 |
| 95 | L0-main | claudeopus46 | 2,320 | 4,359 | 6,679 | 1,026 | 5.9 |
| 96 | L0-main | claudeopus46 | 2,106 | 4,738 | 6,844 | 933 | 7.4 |
| 97 | L0-main | claudeopus46 | 366 | 1,501 | 1,867 | 982 | 4.3 |
| 98 | L0-main | claudeopus46 | 366 | 1,482 | 1,848 | 1,027 | 4.2 |
| 99 | L0-main | claudeopus46 | 560 | 5,126 | 5,686 | 185 | 2.5 |
| 100 | L0-main | claudeopus46 | 1,156 | 6,625 | 7,781 | 795 | 6.2 |

