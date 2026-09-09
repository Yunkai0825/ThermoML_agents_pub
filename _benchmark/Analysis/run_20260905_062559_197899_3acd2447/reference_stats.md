# Reference Stats — analysis-agent

**Run started:** 2026-09-05 06:25:59
**Wall time (at last flush):** 1,050.9 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 36 | 639,662 | 2,308,788 | 74,160 | 2,948,450 | 81,901 | 559.5 | claudeopus46 |
| L1-worker | 103 | 1,299,321 | 505,165 | 104,523 | 1,804,486 | 17,519 | 805.2 | claudeopus46 |
| **TOTAL** | **139** | **1,938,983** | **2,813,953** | **178,683** | **4,752,936** | **34,193** | **1364.7** | |

**Estimated tokens:** ~1,188,234 input + ~44,670 output = ~1,232,904 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 1 | 2 | 1 | 1 | 13 |
| `search_blocks` | 2 | 1 | 3 | 2 | 3 | 4 | 58 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 3 | 1 | 1 | 2 | 1 | 1 | 3 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml_parallel` | 3 | 1 | 2 | 2 | 3 | 4 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 3 | 2 | 3 | 4 | 58 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 3 | 1 | 1 | 2 | 1 | 1 | 3 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 50 | 1 | 4 | 2 | 41 | 50 | 1,704 |
| `block_search_adv` | 3 | 1 | 0 | 0 | 1 | 0 | 0 |
| `query_thermoml_parallel` | 2 | 1 | 2 | 1 | 2 | 2 | 0 |
| `search_blocks` | 2 | 1 | 5 | 3 | 16 | 17 | 1,379 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml` | 2 | 1 | 1 | 2 | 1 | 1 | 0 |
| **TOTAL** | **80** | **11** | **23** | **20** | **73** | **85** | **3,218** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (52 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_5 |  | block_search_adv, query_thermoml, resolve_compound_ids, search_blocks |
| GLOBcomp_1 |  | block_search_adv, query_thermoml, query_thermoml_parallel, resolve_compound_ids, search_blocks |
| GLOBcomp_2 |  | query_thermoml_parallel, resolve_compound_ids, search_blocks |
| GLOBcomp_4 |  | query_thermoml_parallel, resolve_compound_ids, search_blocks |
| GLOBcomp_35 | acetic acid | block_search_adv, search_blocks |
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

#### References (60 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_5688 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_528 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_2574 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_6377 |  | search_blocks |
| GLOBlit_1766 |  | block_search_adv, query_thermoml_parallel, search_blocks |
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
| GLOBlit_555 |  | search_blocks |
| GLOBlit_590 |  | search_blocks |
| GLOBlit_2432 |  | search_blocks |
| GLOBlit_2979 |  | search_blocks |
| GLOBlit_4068 |  | search_blocks |
| GLOBlit_4415 |  | search_blocks |
| GLOBlit_5585 |  | search_blocks |
| GLOBlit_7085 |  | search_blocks |
| GLOBlit_7178 |  | search_blocks |
| GLOBlit_8254 |  | search_blocks |
| GLOBlit_8447 |  | search_blocks |
| GLOBlit_8888 |  | search_blocks |
| GLOBlit_10159 |  | search_blocks |
| GLOBlit_11042 |  | query_thermoml, search_blocks |
| GLOBlit_11142 |  | search_blocks |
| GLOBlit_11872 |  | search_blocks |

#### Properties (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_17 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | block_search_adv, query_thermoml_parallel, search_blocks |
| GLOBprop_1 | Mass density, kg/m3 | query_thermoml, search_blocks |

#### Measurements (18 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_25 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | query_thermoml_parallel, search_blocks |
| GLOBmeas_13 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | query_thermoml_parallel, search_blocks |
| GLOBmeas_169 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | query_thermoml_parallel, search_blocks |
| GLOBmeas_12 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_224 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_44 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_262 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_657 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_747 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_78 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_34 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | query_thermoml, search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_153 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_66 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_6 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_170 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_143 | Mass density, kg/m3 | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | block_search_adv, query_thermoml, query_thermoml_parallel, search_blocks |

#### Variables (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_2 | Mole fraction | query_thermoml, query_thermoml_parallel, search_blocks |
| GLOBvar_1 | Temperature, K | query_thermoml_parallel, search_blocks |
| GLOBvar_3 | Pressure, kPa | search_blocks |
| GLOBvar_8 | Solvent: Mole fraction | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |

#### Constraints (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_2 | Temperature, K | query_thermoml, query_thermoml_parallel, search_blocks |
| GLOBconstr_1 | Pressure, kPa | query_thermoml, query_thermoml_parallel, search_blocks |
| GLOBconstr_8 | Molality, mol/kg | search_blocks |

#### Block_Types (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | query_thermoml, query_thermoml_parallel |
| GLOBblocktype_3 |  | block_search_adv |

#### Solvents (4 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_9 |  | search_blocks |
| GLOBsolvent_146 |  | search_blocks |
| GLOBsolvent_6 |  | search_blocks |
| GLOBsolvent_1 |  | search_blocks |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 52 |
| Unique References | 60 |
| Unique Properties | 2 |
| Unique Measurements | 18 |
| Unique Phases | 1 |
| Unique Variables | 6 |
| Unique Constraints | 3 |
| Unique Block_Types | 2 |
| Unique Solvents | 4 |
| Total DOIs | 60 |
| Unique parent blocks | 72 |
| Explicit block/subsystem targets | 73 |
| Subsystem targets | 1 |
| Target-matched data points | 3,328 |

---

## 3. DOI & Block References

**Unique DOIs:** 60  |  **Parent blocks:** 72  |  **Explicit targets:** 73  |  **Subsystems:** 1  |  **Target-matched datapoints:** 3,157

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2007.06.001 | 1 | 8 | binary | search_blocks |
| 10.1016/j.fluid.2007.06.007 | 3 | 62 | binary | query_thermoml_parallel, search_blocks |
| 10.1016/j.fluid.2007.07.063 | 1 | 9 | binary | search_blocks |
| 10.1016/j.fluid.2007.07.066 | 1 | 15 | binary | search_blocks |
| 10.1016/j.fluid.2008.01.004 | 1 | 15 | binary | search_blocks |
| 10.1016/j.fluid.2008.03.012 | 1 | 78 | binary | search_blocks |
| 10.1016/j.fluid.2008.06.011 | 2 | 61 | binary, ternary | search_blocks |
| 10.1016/j.fluid.2012.06.031 | 1 | 13 | binary | search_blocks |
| 10.1016/j.fluid.2013.10.029 | 1 | 34 | binary | search_blocks |
| 10.1016/j.fluid.2014.08.022 | 2 | 43 | binary | search_blocks |
| 10.1016/j.fluid.2015.07.053 | 2 | 62 | binary, ternary | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2004.07.019 | 1 | 456 | binary | search_blocks |
| 10.1016/j.jct.2005.04.015 | 1 | 56 | binary | search_blocks |
| 10.1016/j.jct.2005.06.018 | 1 | 27 | binary | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2006.08.001 | 1 | 16 | binary | search_blocks |
| 10.1016/j.jct.2008.02.019 | 1 | 33 | binary | search_blocks |
| 10.1016/j.jct.2008.07.005 | 1 | 96 | binary | search_blocks |
| 10.1016/j.jct.2008.12.004 | 1 | 21 | binary | search_blocks |
| 10.1016/j.jct.2009.07.001 | 1 | 21 | binary | search_blocks |
| 10.1016/j.jct.2011.05.014 | 1 | 12 | binary | search_blocks |
| 10.1016/j.jct.2012.02.037 | 1 | 11 | binary | search_blocks |
| 10.1016/j.jct.2013.05.024 | 1 | 76 | binary | search_blocks |
| 10.1016/j.jct.2013.06.018 | 1 | 16 | binary | search_blocks |
| 10.1016/j.jct.2013.09.026 | 1 | 57 | ternary | search_blocks |
| 10.1016/j.jct.2013.11.036 | 2 | 203 | binary | search_blocks |
| 10.1016/j.jct.2014.09.001 | 1 | 10 | binary | search_blocks |
| 10.1016/j.jct.2015.01.003 | 2 | 76 | binary | search_blocks |
| 10.1016/j.jct.2015.04.034 | 1 | 44 | binary | search_blocks |
| 10.1016/j.jct.2015.06.004 | 1 | 39 | binary | search_blocks |
| 10.1016/j.jct.2015.06.023 | 1 | 15 | binary | search_blocks |
| 10.1016/j.jct.2015.06.024 | 1 | 40 | binary | search_blocks |
| 10.1016/j.jct.2016.08.003 | 1 | 9 | binary | search_blocks |
| 10.1016/j.jct.2016.10.005 | 2 | 74 | binary | search_blocks |
| 10.1016/j.jct.2016.12.036 | 1 | 9 | binary | search_blocks |
| 10.1016/j.jct.2018.07.013 | 2 | 22 | binary | search_blocks |
| 10.1016/j.jct.2018.12.019 | 1 | 13 | binary | search_blocks |
| 10.1016/j.jct.2019.105880 | 1 | 16 | binary | search_blocks |
| 10.1016/j.jct.2019.105884 | 1 | 22 | binary | search_blocks |
| 10.1016/j.tca.2004.09.012 | 1 | 10 | binary | search_blocks |
| 10.1016/j.tca.2005.03.009 | 1 | 27 | binary | search_blocks |
| 10.1016/j.tca.2005.06.011 | 2 | 60 | binary, ternary | search_blocks |
| 10.1016/j.tca.2005.11.041 | 1 | 57 | binary | search_blocks |
| 10.1016/j.tca.2006.02.028 | 1 | 13 | binary | query_thermoml_parallel, search_blocks |
| 10.1016/j.tca.2006.08.006 | 2 | 380 | binary | search_blocks |
| 10.1016/j.tca.2006.10.025 | 1 | 17 | binary | search_blocks |
| 10.1016/j.tca.2007.04.012 | 1 | 25 | binary | search_blocks |
| 10.1016/j.tca.2008.02.015 | 1 | 18 | binary | search_blocks |
| 10.1016/j.tca.2009.03.014 | 1 | 14 | binary | search_blocks |
| 10.1016/j.tca.2013.02.010 | 1 | 44 | binary | search_blocks |
| 10.1016/j.tca.2017.05.023 | 1 | 1 | binary | search_blocks |
| 10.1021/acs.jced.6b01058 | 1 | 12 | binary | search_blocks |
| 10.1021/acs.jced.7b00299 | 1 | 2 | binary | search_blocks |
| 10.1021/je020149l | 3 | 63 | binary | search_blocks |
| 10.1021/je034101z | 1 | 380 | binary | search_blocks |
| 10.1021/je049738c | 1 | 8 | binary | search_blocks |
| 10.1021/je0601098 | 1 | 12 | binary | search_blocks |
| 10.1021/je4003515 | 1 | 25 | binary | search_blocks |
| 10.1021/je700700f | 1 | 13 | binary | query_thermoml, search_blocks |
| 10.1021/je800158z | 1 | 56 | binary | search_blocks |
| 10.1021/je900966r | 1 | 30 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2007.06.001 | PROPblock_15 | declared | 8 | binary | — | search_blocks |
| 10.1016/j.fluid.2007.06.007 | PROPblock_1 | declared | 15 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1016/j.fluid.2007.06.007 | PROPblock_2 | declared | 15 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1016/j.fluid.2007.06.007 | PROPblock_6 | declared | 32 | binary | — | search_blocks |
| 10.1016/j.fluid.2007.07.063 | PROPblock_7 | declared | 9 | binary | — | search_blocks |
| 10.1016/j.fluid.2007.07.066 | PROPblock_8 | declared | 15 | binary | — | search_blocks |
| 10.1016/j.fluid.2008.01.004 | PROPblock_5 | declared | 15 | binary | — | search_blocks |
| 10.1016/j.fluid.2008.03.012 | PROPblock_4 | declared | 78 | binary | — | search_blocks |
| 10.1016/j.fluid.2008.06.011 | PROPblock_1 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.fluid.2008.06.011 | PROPblock_2 | declared | 44 | ternary | — | search_blocks |
| 10.1016/j.fluid.2012.06.031 | PROPblock_9 | declared | 13 | binary | — | search_blocks |
| 10.1016/j.fluid.2013.10.029 | PROPblock_14 | declared | 34 | binary | — | search_blocks |
| 10.1016/j.fluid.2014.08.022 | PROPblock_1 | declared | 22 | binary | — | search_blocks |
| 10.1016/j.fluid.2014.08.022 | PROPblock_3 | declared | 21 | binary | — | search_blocks |
| 10.1016/j.fluid.2015.07.053 | PROPblock_1 | declared | 59 | ternary | — | search_blocks |
| 10.1016/j.fluid.2015.07.053 | PROPblock_1 | BLKsubsys_1 | 3 | binary | — | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2004.07.019 | PROPblock_3 | declared | 456 | binary | — | search_blocks |
| 10.1016/j.jct.2005.04.015 | PROPblock_1 | declared | 56 | binary | — | search_blocks |
| 10.1016/j.jct.2005.06.018 | PROPblock_4 | declared | 27 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2006.08.001 | PROPblock_3 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.jct.2008.02.019 | PROPblock_9 | declared | 33 | binary | — | search_blocks |
| 10.1016/j.jct.2008.07.005 | PROPblock_9 | declared | 96 | binary | — | search_blocks |
| 10.1016/j.jct.2008.12.004 | PROPblock_3 | declared | 21 | binary | — | search_blocks |
| 10.1016/j.jct.2009.07.001 | PROPblock_2 | declared | 21 | binary | — | search_blocks |
| 10.1016/j.jct.2011.05.014 | PROPblock_3 | declared | 12 | binary | — | search_blocks |
| 10.1016/j.jct.2012.02.037 | PROPblock_16 | declared | 11 | binary | — | search_blocks |
| 10.1016/j.jct.2013.05.024 | PROPblock_4 | declared | 76 | binary | — | search_blocks |
| 10.1016/j.jct.2013.06.018 | PROPblock_1 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.jct.2013.09.026 | PROPblock_4 | declared | 57 | ternary | — | search_blocks |
| 10.1016/j.jct.2013.11.036 | PROPblock_1 | declared | 174 | binary | — | search_blocks |
| 10.1016/j.jct.2013.11.036 | PROPblock_2 | declared | 29 | binary | — | search_blocks |
| 10.1016/j.jct.2014.09.001 | PROPblock_14 | declared | 10 | binary | — | search_blocks |
| 10.1016/j.jct.2015.01.003 | PROPblock_1 | declared | 38 | binary | — | search_blocks |
| 10.1016/j.jct.2015.01.003 | PROPblock_2 | declared | 38 | binary | — | search_blocks |
| 10.1016/j.jct.2015.04.034 | PROPblock_4 | declared | 44 | binary | — | search_blocks |
| 10.1016/j.jct.2015.06.004 | PROPblock_25 | declared | 39 | binary | — | search_blocks |
| 10.1016/j.jct.2015.06.023 | PROPblock_6 | declared | 15 | binary | — | search_blocks |
| 10.1016/j.jct.2015.06.024 | PROPblock_5 | declared | 40 | binary | — | search_blocks |
| 10.1016/j.jct.2016.08.003 | PROPblock_17 | declared | 9 | binary | — | search_blocks |
| 10.1016/j.jct.2016.10.005 | PROPblock_1 | declared | 37 | binary | — | search_blocks |
| 10.1016/j.jct.2016.10.005 | PROPblock_2 | declared | 37 | binary | — | search_blocks |
| 10.1016/j.jct.2016.12.036 | PROPblock_24 | declared | 9 | binary | — | search_blocks |
| 10.1016/j.jct.2018.07.013 | PROPblock_21 | declared | 11 | binary | — | search_blocks |
| 10.1016/j.jct.2018.07.013 | PROPblock_33 | declared | 11 | binary | — | search_blocks |
| 10.1016/j.jct.2018.12.019 | PROPblock_19 | declared | 13 | binary | — | search_blocks |
| 10.1016/j.jct.2019.105880 | PROPblock_7 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.jct.2019.105884 | PROPblock_24 | declared | 22 | binary | — | search_blocks |
| 10.1016/j.tca.2004.09.012 | PROPblock_10 | declared | 10 | binary | — | search_blocks |
| 10.1016/j.tca.2005.03.009 | PROPblock_3 | declared | 27 | binary | — | search_blocks |
| 10.1016/j.tca.2005.06.011 | PROPblock_1 | declared | 3 | binary | — | search_blocks |
| 10.1016/j.tca.2005.06.011 | PROPblock_2 | declared | 57 | ternary | — | search_blocks |
| 10.1016/j.tca.2005.11.041 | PROPblock_1 | declared | 57 | binary | — | search_blocks |
| 10.1016/j.tca.2006.02.028 | PROPblock_1 | declared | 13 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1016/j.tca.2006.08.006 | PROPblock_13 | declared | 185 | binary | — | search_blocks |
| 10.1016/j.tca.2006.08.006 | PROPblock_15 | declared | 195 | binary | — | search_blocks |
| 10.1016/j.tca.2006.10.025 | PROPblock_22 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.tca.2007.04.012 | PROPblock_12 | declared | 25 | binary | — | search_blocks |
| 10.1016/j.tca.2008.02.015 | PROPblock_3 | declared | 18 | binary | — | search_blocks |
| 10.1016/j.tca.2009.03.014 | PROPblock_14 | declared | 14 | binary | — | search_blocks |
| 10.1016/j.tca.2013.02.010 | PROPblock_8 | declared | 44 | binary | — | search_blocks |
| 10.1016/j.tca.2017.05.023 | PROPblock_1 | declared | 1 | binary | — | search_blocks |
| 10.1021/acs.jced.6b01058 | PROPblock_8 | declared | 12 | binary | — | search_blocks |
| 10.1021/acs.jced.7b00299 | PROPblock_13 | declared | 2 | binary | — | search_blocks |
| 10.1021/je020149l | PROPblock_10 | declared | 21 | binary | — | search_blocks |
| 10.1021/je020149l | PROPblock_11 | declared | 20 | binary | — | search_blocks |
| 10.1021/je020149l | PROPblock_12 | declared | 22 | binary | — | search_blocks |
| 10.1021/je034101z | PROPblock_6 | declared | 380 | binary | — | search_blocks |
| 10.1021/je049738c | PROPblock_26 | declared | 8 | binary | — | search_blocks |
| 10.1021/je0601098 | PROPblock_22 | declared | 12 | binary | — | search_blocks |
| 10.1021/je4003515 | PROPblock_10 | declared | 25 | binary | — | search_blocks |
| 10.1021/je700700f | PROPblock_14 | declared | 13 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je800158z | PROPblock_3 | declared | 56 | binary | — | search_blocks |
| 10.1021/je900966r | PROPblock_4 | declared | 30 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 1 | `query_thermoml_parallel` | queries=[{'label': 'HE_methanol_water… | 209 | — | — | 0.0 |
| 2 | 2 | `query_thermoml_parallel` | queries=[{'label': 'HE_methanol_water… | 253 | — | — | 0.0 |
| 3 | 1 | `resolve_compound_ids` | purpose=Find compound IDs for 1-propa…, queries=['… | 203 | KEEP ←in 283 | 203 | 4.1 |
| 4 | 2 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Resolve ethanol and… | 209 | KEEP ←in 278 | 209 | 4.0 |
| 5 | 2 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Resolve methanol an… | 180 | KEEP ←in 277 | 180 | 4.1 |
| 6 | 3 | `search_blocks` | compound=['GLOBcomp_5', 'GLOBcomp_1'], limit=50, p… | 1,013 | DISCARD ←in 39 | 955 | 17.2 |
| 7 | 4 | `search_blocks` | compound=['GLOBcomp_4', 'GLOBcomp_1'], limit=50, p… | 1,218 | KEEP ←in 2,016 | 1203 | 13.9 |
| 8 | 4 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=50, p… | 1,057 | KEEP ←in 7,304 | 1057 | 18.8 |
| 9 | 5 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_5688,… | 1,381 | — | — | 0.3 |
| 10 | 4 | `search_blocks` | compound=['GLOBcomp_5', 'GLOBcomp_1'], limit=50, p… | 1,103 | KEEP ←in 815 | 1088 | 19.7 |
| 11 | 6 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_528, … | 1,588 | — | — | 0.1 |
| 12 | 7 | `inspect_block_table` | block_number=PROPblock_2, literature=GLOBlit_528, … | 1,529 | — | — | 0.1 |
| 13 | 5 | `inspect_block_table` | BLKsubsys_id=BLKsubsys_1, block_number=PROPblock_1… | 970 | — | — | 0.1 |
| 14 | 8 | `inspect_block_table` | block_number=PROPblock_4, literature=GLOBlit_2574,… | 1,436 | — | — | 0.1 |
| 15 | 3 | `query_thermoml_parallel` | queries=[{'label': 'HE_methanol_water… | 54,967 | — | — | 132.9 |
| 16 | 2 | `search_blocks` | compound=['GLOBcomp_5', 'GLOBcomp_1'], limit=50, p… | 913 | DISCARD ←in 39 | 855 | 12.8 |
| 17 | 2 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=50, p… | 570 | KEEP ←in 7,304 | 570 | 20.2 |
| 18 | 3 | `inspect_block_table` | block_number=PROPblock_4, literature=GLOBlit_2574,… | 247 | — | — | 0.0 |
| 19 | 3 | `search_blocks` | compound=['GLOBcomp_5', 'GLOBcomp_1'], limit=50, p… | 870 | DISCARD ←in 39 | 812 | 10.2 |
| 20 | 4 | `inspect_block_table` | block_number=PROPblock_4, literature=GLOBlit_2574,… | 392 | — | — | 0.2 |
| 21 | 5 | `inspect_block_table` | block_number=PROPblock_4, literature=GLOBlit_2574,… | 1,512 | — | — | 0.7 |
| 22 | 4 | `search_blocks` | compound=['GLOBcomp_5', 'GLOBcomp_1'], limit=50, p… | 867 | KEEP ←in 815 | 837 | 19.9 |
| 23 | 5 | `inspect_block_table` | BLKsubsys_id=BLKsubsys_1, block_number=GLOBlit_176… | 970 | — | — | 0.4 |
| 24 | 6 | `search_blocks` | compound=GLOBcomp_5, limit=50, property=GLOBprop_1… | 1,221 | KEEP ←in 34,310 | 1076 | 16.1 |
| 25 | 8 | `block_search_adv` | compound_match=all, compounds=['REQUIRE GLOBcomp_5… | 1,135 | KEEP ←in 1,390 | 1120 | 16.2 |
| 26 | 4 | `query_thermoml_parallel` | queries=[{'label': 'HE_propanol_water… | 20,434 | — | — | 203.4 |
| 27 | 7 | `fit_multi_system` | purpose=Fit Redlich-Kister polynomial…, systems=[{… | 783 | — | — | 1.7 |
| 28 | 10 | `inspect_block` | block_number=PROPblock_4, doi=10.1016/j.jct.2005.0… | 1,584 | — | — | 0.1 |
| 29 | 12 | `fit_block` | block_number=PROPblock_4, doi=10.1016/j.jct.2005.0… | 882 | — | — | 1.8 |
| 30 | 15 | `predict_from_rk` | coeffs=[-3.092541, 1.550802, -2.0271…, n_points=10… | 172 | — | — | 0.3 |
| 31 | 18 | `predict_from_rk` | coeffs=[-1.601023, 1.734931, -3.1974…, property_ty… | 171 | — | — | 0.1 |
| 32 | 2 | `search_blocks` | compound=['GLOBcomp_5', 'GLOBcomp_1'], limit=50, p… | 444 | KEEP ←in 11,346 | 412 | 22.7 |
| 33 | 3 | `inspect_block_table` | block_number=PROPblock_14, literature=GLOBlit_1104… | 247 | — | — | 0.0 |
| 34 | 4 | `inspect_block_table` | block_number=PROPblock_14, literature=GLOBlit_1104… | 369 | — | — | 0.3 |
| 35 | 5 | `inspect_block_table` | block_number=PROPblock_14, literature=GLOBlit_1104… | 1,213 | — | — | 0.4 |
| 36 | 6 | `inspect_block_table` | block_number=PROPblock_14, literature=GLOBlit_1104… | 1,124 | — | — | 0.3 |
| 37 | 7 | `inspect_block_table` | block_number=PROPblock_14, literature=GLOBlit_1104… | 1,226 | — | — | 0.1 |
| 38 | 19 | `query_thermoml` | id_catalog=[{'global_id': 'GLOBcomp_5', …, instruc… | 14,650 | — | — | 148.9 |
| 39 | 21 | `fit_block_derived` | block_number=PROPblock_14, composition_hint=mole_f… | 204 | — | — | 0.1 |
| 40 | 24 | `fit_block_derived` | block_number=PROPblock_14, composition_hint=mole_f… | 957 | — | — | 1.9 |
| | | **TOTAL (40 tools)** | | **120,473** | | **10,577** | **694.2** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 22,518 | 362 | 22,880 | 2,041 | 10.5 |
| 2 | L0-main | claudeopus46 | 22,518 | 898 | 23,416 | 2,043 | 9.4 |
| 3 | L0-main | claudeopus46 | 22,518 | 1,435 | 23,953 | 1,848 | 9.7 |
| 4 | L1-worker | claudeopus46 | 24,095 | 917 | 25,012 | 644 | 5.0 |
| 5 | L1-worker | claudeopus46 | 24,095 | 921 | 25,016 | 585 | 5.2 |
| 6 | L1-worker | claudeopus46 | 24,095 | 915 | 25,010 | 605 | 5.4 |
| 7 | L1-worker | claudeopus46 | 3,767 | 426 | 4,193 | 386 | 3.9 |
| 8 | L1-worker | claudeopus46 | 24,095 | 1,930 | 26,025 | 531 | 4.4 |
| 9 | L1-worker | claudeopus46 | 24,095 | 1,935 | 26,030 | 535 | 4.5 |
| 10 | L1-worker | claudeopus46 | 3,767 | 437 | 4,204 | 389 | 3.8 |
| 11 | L1-worker | claudeopus46 | 3,767 | 438 | 4,205 | 317 | 3.9 |
| 12 | L1-worker | claudeopus46 | 24,095 | 1,389 | 25,484 | 845 | 6.4 |
| 13 | L1-worker | claudeopus46 | 24,095 | 1,555 | 25,650 | 803 | 6.1 |
| 14 | L1-worker | claudeopus46 | 24,095 | 1,527 | 25,622 | 802 | 6.7 |
| 15 | L1-worker | claudeopus46 | 24,095 | 2,114 | 26,209 | 698 | 5.3 |
| 16 | L1-worker | claudeopus46 | 24,095 | 2,277 | 26,372 | 650 | 4.8 |
| 17 | L1-worker | claudeopus46 | 24,095 | 2,246 | 26,341 | 759 | 5.3 |
| 18 | L1-worker | claudeopus46 | 3,767 | 565 | 4,332 | 1,424 | 10.6 |
| 19 | L1-worker | claudeopus46 | 3,767 | 2,501 | 6,268 | 1,586 | 12.3 |
| 20 | L1-worker | claudeopus46 | 3,767 | 7,770 | 11,537 | 1,924 | 15.9 |
| 21 | L1-worker | claudeopus46 | 24,095 | 3,140 | 27,235 | 896 | 8.3 |
| 22 | L1-worker | claudeopus46 | 24,095 | 3,455 | 27,550 | 774 | 7.6 |
| 23 | L1-worker | claudeopus46 | 24,095 | 5,142 | 29,237 | 1,636 | 13.1 |
| 24 | L1-worker | claudeopus46 | 24,095 | 3,323 | 27,418 | 2,636 | 19.6 |
| 25 | L1-worker | claudeopus46 | 2,320 | 1,767 | 4,087 | 731 | 4.5 |
| 26 | L1-worker | claudeopus46 | 3,767 | 1,237 | 5,004 | 1,434 | 11.3 |
| 27 | L1-worker | claudeopus46 | 2,106 | 2,805 | 4,911 | 433 | 5.2 |
| 28 | L1-worker | claudeopus46 | 627 | 1,647 | 2,274 | 840 | 5.9 |
| 29 | L1-worker | claudeopus46 | 366 | 1,168 | 1,534 | 696 | 3.8 |
| 30 | L1-worker | claudeopus46 | 366 | 1,210 | 1,576 | 421 | 3.2 |
| 31 | L1-worker | claudeopus46 | 24,095 | 8,722 | 32,817 | 757 | 7.0 |
| 32 | L1-worker | claudeopus46 | 1,228 | 3,537 | 4,765 | 356 | 3.6 |
| 33 | L1-worker | claudeopus46 | 24,095 | 10,600 | 34,695 | 550 | 5.2 |
| 34 | L1-worker | claudeopus46 | 24,095 | 4,625 | 28,720 | 951 | 13.8 |
| 35 | L1-worker | claudeopus46 | 787 | 10,657 | 11,444 | 503 | 6.6 |
| 36 | L1-worker | claudeopus46 | 24,095 | 12,451 | 36,546 | 601 | 5.0 |
| 37 | L1-worker | claudeopus46 | 24,095 | 5,970 | 30,065 | 2,032 | 12.8 |
| 38 | L1-worker | claudeopus46 | 24,095 | 14,210 | 38,305 | 3,178 | 20.9 |
| 39 | L1-worker | claudeopus46 | 24,095 | 11,122 | 35,217 | 1,788 | 13.6 |
| 40 | L1-worker | claudeopus46 | 2,106 | 4,345 | 6,451 | 1,646 | 8.0 |
| 41 | L1-worker | claudeopus46 | 2,320 | 3,309 | 5,629 | 1,319 | 8.2 |
| 42 | L1-worker | claudeopus46 | 627 | 3,189 | 3,816 | 1,134 | 8.3 |
| 43 | L1-worker | claudeopus46 | 366 | 1,545 | 1,911 | 1,121 | 5.1 |
| 44 | L1-worker | claudeopus46 | 366 | 1,756 | 2,122 | 1,274 | 5.4 |
| 45 | L1-worker | claudeopus46 | 366 | 2,423 | 2,789 | 1,214 | 5.7 |
| 46 | L1-worker | claudeopus46 | 24,095 | 15,531 | 39,626 | 1,427 | 9.8 |
| 47 | L1-worker | claudeopus46 | 2,320 | 1,556 | 3,876 | 466 | 3.4 |
| 48 | L1-worker | claudeopus46 | 627 | 1,436 | 2,063 | 544 | 3.9 |
| 49 | L1-worker | claudeopus46 | 2,106 | 2,598 | 4,704 | 773 | 5.9 |
| 50 | L1-worker | claudeopus46 | 787 | 26,930 | 27,717 | 616 | 6.7 |
| 51 | L1-worker | claudeopus46 | 366 | 903 | 1,269 | 454 | 3.0 |
| 52 | L1-worker | claudeopus46 | 366 | 1,550 | 1,916 | 565 | 4.1 |
| 53 | L1-worker | claudeopus46 | 1,228 | 3,762 | 4,990 | 699 | 4.8 |
| 54 | L0-main | claudeopus46 | 22,518 | 50,647 | 73,165 | 3,923 | 27.2 |
| 55 | L1-worker | claudeopus46 | 24,095 | 1,554 | 25,649 | 840 | 6.3 |
| 56 | L1-worker | claudeopus46 | 24,095 | 1,929 | 26,024 | 852 | 6.4 |
| 57 | L1-worker | claudeopus46 | 24,095 | 2,666 | 26,761 | 646 | 6.7 |
| 58 | L1-worker | claudeopus46 | 24,095 | 2,270 | 26,365 | 732 | 7.5 |
| 59 | L1-worker | claudeopus46 | 3,767 | 582 | 4,349 | 1,298 | 9.1 |
| 60 | L1-worker | claudeopus46 | 3,767 | 7,750 | 11,517 | 1,924 | 15.2 |
| 61 | L1-worker | claudeopus46 | 24,095 | 3,207 | 27,302 | 751 | 6.2 |
| 62 | L1-worker | claudeopus46 | 24,095 | 3,168 | 27,263 | 994 | 7.7 |
| 63 | L1-worker | claudeopus46 | 3,767 | 505 | 4,272 | 1,370 | 9.6 |
| 64 | L1-worker | claudeopus46 | 24,095 | 3,809 | 27,904 | 688 | 6.8 |
| 65 | L1-worker | claudeopus46 | 24,095 | 4,421 | 28,516 | 886 | 6.3 |
| 66 | L1-worker | claudeopus46 | 24,095 | 4,522 | 28,617 | 658 | 5.2 |
| 67 | L1-worker | claudeopus46 | 3,767 | 1,218 | 4,985 | 1,203 | 8.9 |
| 68 | L1-worker | claudeopus46 | 24,095 | 6,411 | 30,506 | 2,118 | 17.7 |
| 69 | L1-worker | claudeopus46 | 24,095 | 5,695 | 29,790 | 945 | 7.9 |
| 70 | L1-worker | claudeopus46 | 2,106 | 4,299 | 6,405 | 510 | 4.4 |
| 71 | L1-worker | claudeopus46 | 627 | 2,129 | 2,756 | 1,026 | 5.9 |
| 72 | L1-worker | claudeopus46 | 2,320 | 2,249 | 4,569 | 1,009 | 6.0 |
| 73 | L1-worker | claudeopus46 | 366 | 1,287 | 1,653 | 383 | 3.1 |
| 74 | L1-worker | claudeopus46 | 366 | 1,446 | 1,812 | 943 | 4.1 |
| 75 | L1-worker | claudeopus46 | 366 | 1,437 | 1,803 | 1,013 | 4.9 |
| 76 | L1-worker | claudeopus46 | 24,095 | 7,051 | 31,146 | 1,287 | 10.7 |
| 77 | L1-worker | claudeopus46 | 787 | 12,260 | 13,047 | 681 | 7.4 |
| 78 | L1-worker | claudeopus46 | 3,767 | 34,745 | 38,512 | 1,592 | 14.6 |
| 79 | L1-worker | claudeopus46 | 24,095 | 8,672 | 32,767 | 1,799 | 14.1 |
| 80 | L1-worker | claudeopus46 | 24,095 | 9,600 | 33,695 | 1,041 | 7.3 |
| 81 | L1-worker | claudeopus46 | 3,767 | 1,578 | 5,345 | 1,546 | 12.2 |
| 82 | L1-worker | claudeopus46 | 24,095 | 10,644 | 34,739 | 2,283 | 17.6 |
| 83 | L1-worker | claudeopus46 | 24,095 | 16,038 | 40,133 | 2,372 | 16.6 |
| 84 | L1-worker | claudeopus46 | 24,095 | 21,521 | 45,616 | 1,347 | 10.2 |
| 85 | L1-worker | claudeopus46 | 2,106 | 3,153 | 5,259 | 92 | 2.1 |
| 86 | L1-worker | claudeopus46 | 2,320 | 1,478 | 3,798 | 728 | 4.1 |
| 87 | L1-worker | claudeopus46 | 627 | 1,358 | 1,985 | 794 | 4.6 |
| 88 | L1-worker | claudeopus46 | 366 | 869 | 1,235 | 67 | 2.4 |
| 89 | L1-worker | claudeopus46 | 366 | 1,165 | 1,531 | 601 | 3.2 |
| 90 | L1-worker | claudeopus46 | 787 | 4,217 | 5,004 | 528 | 4.7 |
| 91 | L0-main | claudeopus46 | 22,518 | 74,243 | 96,761 | 2,517 | 25.2 |
| 92 | L0-main | claudeopus46 | 22,518 | 75,021 | 97,539 | 1,042 | 8.4 |
| 93 | L0-main | claudeopus46 | 22,518 | 75,705 | 98,223 | 1,045 | 9.1 |
| 94 | L0-main | claudeopus46 | 22,518 | 77,467 | 99,985 | 1,323 | 10.3 |
| 95 | L0-main | claudeopus46 | 22,518 | 78,178 | 100,696 | 555 | 4.7 |
| 96 | L0-main | claudeopus46 | 22,518 | 78,836 | 101,354 | 587 | 4.1 |
| 97 | L0-main | claudeopus46 | 22,518 | 80,748 | 103,266 | 1,070 | 8.9 |
| 98 | L0-main | claudeopus46 | 22,518 | 81,605 | 104,123 | 887 | 8.1 |
| 99 | L0-main | claudeopus46 | 22,518 | 83,669 | 106,187 | 3,020 | 22.7 |
| 100 | L0-main | claudeopus46 | 22,518 | 84,488 | 107,006 | 810 | 6.2 |
| 101 | L0-main | claudeopus46 | 22,518 | 85,236 | 107,754 | 723 | 6.1 |
| 102 | L0-main | claudeopus46 | 22,518 | 85,133 | 107,651 | 728 | 7.9 |
| 103 | L0-main | claudeopus46 | 22,518 | 85,855 | 108,373 | 677 | 5.9 |
| 104 | L0-main | claudeopus46 | 22,518 | 86,572 | 109,090 | 603 | 9.8 |
| 105 | L0-main | claudeopus46 | 22,518 | 86,434 | 108,952 | 3,408 | 26.3 |
| 106 | L1-worker | claudeopus46 | 24,095 | 1,382 | 25,477 | 829 | 6.8 |
| 107 | L1-worker | claudeopus46 | 24,095 | 2,064 | 26,159 | 693 | 5.9 |
| 108 | L1-worker | claudeopus46 | 3,767 | 11,876 | 15,643 | 1,886 | 14.9 |
| 109 | L1-worker | claudeopus46 | 24,095 | 2,471 | 26,566 | 945 | 8.7 |
| 110 | L1-worker | claudeopus46 | 24,095 | 3,061 | 27,156 | 591 | 5.7 |
| 111 | L1-worker | claudeopus46 | 24,095 | 3,728 | 27,823 | 814 | 6.7 |
| 112 | L1-worker | claudeopus46 | 24,095 | 5,297 | 29,392 | 741 | 7.2 |
| 113 | L1-worker | claudeopus46 | 24,095 | 6,743 | 30,838 | 1,322 | 10.7 |
| 114 | L1-worker | claudeopus46 | 24,095 | 8,291 | 32,386 | 2,360 | 18.2 |
| 115 | L1-worker | claudeopus46 | 24,095 | 13,455 | 37,550 | 2,438 | 16.4 |
| 116 | L1-worker | claudeopus46 | 24,095 | 18,697 | 42,792 | 2,404 | 16.2 |
| 117 | L1-worker | claudeopus46 | 2,320 | 2,535 | 4,855 | 750 | 5.7 |
| 118 | L1-worker | claudeopus46 | 2,106 | 4,038 | 6,144 | 645 | 8.0 |
| 119 | L1-worker | claudeopus46 | 366 | 1,187 | 1,553 | 715 | 3.3 |
| 120 | L1-worker | claudeopus46 | 627 | 2,415 | 3,042 | 841 | 9.4 |
| 121 | L1-worker | claudeopus46 | 366 | 1,422 | 1,788 | 385 | 3.1 |
| 122 | L1-worker | claudeopus46 | 787 | 12,116 | 12,903 | 669 | 7.8 |
| 123 | L0-main | claudeopus46 | 22,518 | 100,184 | 122,702 | 2,259 | 17.7 |
| 124 | L0-main | claudeopus46 | 22,518 | 101,068 | 123,586 | 776 | 6.8 |
| 125 | L0-main | claudeopus46 | 22,518 | 101,394 | 123,912 | 1,246 | 15.6 |
| 126 | L0-main | claudeopus46 | 22,518 | 102,120 | 124,638 | 780 | 6.5 |
| 127 | L0-main | claudeopus46 | 22,518 | 102,859 | 125,377 | 742 | 7.6 |
| 128 | L0-main | claudeopus46 | 22,518 | 104,757 | 127,275 | 1,956 | 19.4 |
| 129 | L0-main | claudeopus46 | 22,518 | 105,628 | 128,146 | 10,994 | 75.6 |
| 130 | L0-main | claudeopus46 | 22,518 | 120,660 | 143,178 | 8,752 | 60.0 |
| 131 | L0-main | claudeopus46 | 22,518 | 132,445 | 154,963 | 9,069 | 62.6 |
| 132 | L0-main | claudeopus46 | 2,106 | 12,601 | 14,707 | 387 | 4.2 |
| 133 | L0-main | claudeopus46 | 366 | 910 | 1,276 | 382 | 3.3 |
| 134 | L0-main | claudeopus46 | 2,320 | 12,124 | 14,444 | 1,789 | 14.3 |
| 135 | L0-main | claudeopus46 | 366 | 2,226 | 2,592 | 1,734 | 5.5 |
| 136 | L0-main | claudeopus46 | 560 | 13,216 | 13,776 | 265 | 11.8 |
| 137 | L0-main | claudeopus46 | 1,156 | 15,353 | 16,509 | 1,558 | 11.9 |
| 138 | L0-main | claudeopus46 | 366 | 2,251 | 2,617 | 1,546 | 6.3 |
| 139 | L0-main | claudeopus46 | 1,918 | 6,460 | 8,378 | 1,075 | 9.9 |

