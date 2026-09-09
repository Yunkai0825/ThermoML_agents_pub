# Reference Stats — analysis-agent

**Run started:** 2026-09-05 04:21:00
**Wall time (at last flush):** 477.0 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 23 | 369,080 | 440,757 | 32,349 | 809,837 | 35,210 | 254.7 | claudeopus46 |
| L1-worker | 43 | 556,809 | 209,504 | 44,801 | 766,313 | 17,821 | 334.5 | claudeopus46 |
| **TOTAL** | **66** | **925,889** | **650,261** | **77,150** | **1,576,150** | **23,881** | **589.2** | |

**Estimated tokens:** ~394,037 input + ~19,287 output = ~413,324 total
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
| `search_blocks` | 2 | 1 | 5 | 3 | 16 | 17 | 1,379 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 7 | 1 | 2 | 2 | 6 | 6 | 250 |
| `search_blocks` | 2 | 14 | 6 | 6 | 27 | 50 | 1,775 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml_parallel` | 2 | 1 | 1 | 2 | 1 | 1 | 0 |
| `list_session_files` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **17** | **18** | **14** | **13** | **50** | **74** | **3,404** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (8 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_1 |  | query_thermoml_parallel, resolve_compound_ids, search_blocks |
| GLOBcomp_5 |  | query_thermoml_parallel, resolve_compound_ids, search_blocks |
| GLOBcomp_482 | 1-butyl-3-methylimidazolium nitrate | search_blocks |
| GLOBcomp_299 | 3-methylbutyl ethanoate | search_blocks |
| GLOBcomp_2754 | 1-methylimidazolium acetate | search_blocks |
| GLOBcomp_268 | 2-pyrrolidinone | search_blocks |
| GLOBcomp_133 | formamide | search_blocks |
| GLOBcomp_56 | 1-hexyl-3-methylimidazolium bis[(trifluoromethyl)sulfonyl]imide | search_blocks |

#### Properties (15 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_28 |  | resolve_property_ids, search_blocks |
| GLOBprop_1 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBprop_3 | Activity coefficient | search_blocks |
| GLOBprop_8 | Speed of sound, m/s | search_blocks |
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

#### References (40 unique)

| ID | Name | Source tools |
|---:|------|-------------|
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
| GLOBlit_11042 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_11142 |  | search_blocks |
| GLOBlit_11872 |  | search_blocks |
| GLOBlit_3116 |  | search_blocks |
| GLOBlit_3325 |  | search_blocks |
| GLOBlit_3540 |  | search_blocks |
| GLOBlit_5836 |  | search_blocks |
| GLOBlit_6063 |  | search_blocks |
| GLOBlit_8993 |  | search_blocks |
| GLOBlit_299 |  | search_blocks |
| GLOBlit_766 |  | search_blocks |
| GLOBlit_970 |  | search_blocks |
| GLOBlit_996 |  | search_blocks |
| GLOBlit_1742 |  | search_blocks |
| GLOBlit_2060 |  | search_blocks |
| GLOBlit_2092 |  | search_blocks |
| GLOBlit_3518 |  | search_blocks |
| GLOBlit_3796 |  | search_blocks |
| GLOBlit_4843 |  | search_blocks |
| GLOBlit_5053 |  | search_blocks |
| GLOBlit_5059 |  | search_blocks |
| GLOBlit_5124 |  | search_blocks |
| GLOBlit_6268 |  | search_blocks |
| GLOBlit_6460 |  | search_blocks |
| GLOBlit_6553 |  | search_blocks |
| GLOBlit_7483 |  | search_blocks |
| GLOBlit_7818 |  | search_blocks |

#### Measurements (29 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_134 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_153 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_66 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_6 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_170 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_143 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_29 | Excess molar volume, m3/mol | search_blocks |
| GLOBmeas_55 | Excess molar volume, m3/mol | search_blocks |
| GLOBmeas_543 | Activity coefficient | search_blocks |
| GLOBmeas_1045 | Activity coefficient | search_blocks |
| GLOBmeas_1042 | Activity coefficient | search_blocks |
| GLOBmeas_7 | Speed of sound, m/s | search_blocks |
| GLOBmeas_922 | Binary diffusion coefficient, m2/s | search_blocks |
| GLOBmeas_933 | Binary diffusion coefficient, m2/s | search_blocks |
| GLOBmeas_1 | Mole fraction | search_blocks |
| GLOBmeas_133 | Vapor or sublimation pressure, kPa | search_blocks |
| GLOBmeas_4 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_5 | Boiling temperature at pressure P, K | search_blocks |
| GLOBmeas_39 | Azeotropic composition: mole fraction | search_blocks |
| GLOBmeas_13 | Molar enthalpy of dilution, kJ/mol | search_blocks |
| GLOBmeas_10 | Mole fraction | search_blocks |
| GLOBmeas_14 | Electrical conductivity, S/m | search_blocks |
| GLOBmeas_137 | Boiling temperature at pressure P, K | search_blocks |
| GLOBmeas_8 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_18 | Speed of sound, m/s | search_blocks |
| GLOBmeas_25 | Molar enthalpy of solution, kJ/mol | search_blocks |
| GLOBmeas_144 | Molar enthalpy of solution, kJ/mol | search_blocks |
| GLOBmeas_3 | Refractive index (Na D-line) | search_blocks |

#### Phases (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | query_thermoml_parallel, search_blocks |
| GLOBphase_3 |  | search_blocks |

#### Variables (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |
| GLOBvar_3 | Pressure, kPa | search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |
| GLOBvar_2 | Mole fraction | query_thermoml_parallel, search_blocks |
| GLOBvar_32 | Initial mass fraction of solute | search_blocks |

#### Constraints (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | query_thermoml_parallel, search_blocks |
| GLOBconstr_8 | Molality, mol/kg | search_blocks |
| GLOBconstr_2 | Temperature, K | query_thermoml_parallel, search_blocks |
| GLOBconstr_3 | Mole fraction | search_blocks |
| GLOBconstr_25 | Final mass fraction of solute | search_blocks |
| GLOBconstr_4 | Frequency, MHz | search_blocks |

#### Solvents (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | search_blocks |
| GLOBsolvent_9 |  | search_blocks |

#### Block_Types (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | query_thermoml_parallel |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 8 |
| Unique Properties | 15 |
| Unique References | 40 |
| Unique Measurements | 29 |
| Unique Phases | 2 |
| Unique Variables | 6 |
| Unique Constraints | 6 |
| Unique Solvents | 2 |
| Unique Block_Types | 1 |
| Total DOIs | 40 |
| Unique parent blocks | 63 |
| Explicit block/subsystem targets | 63 |
| Subsystem targets | 0 |
| Target-matched data points | 3,417 |

---

## 3. DOI & Block References

**Unique DOIs:** 40  |  **Parent blocks:** 63  |  **Explicit targets:** 63  |  **Subsystems:** 0  |  **Target-matched datapoints:** 2,549

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2005.08.018 | 3 | 14 | binary | search_blocks |
| 10.1016/j.fluid.2007.07.066 | 2 | 30 | binary | search_blocks |
| 10.1016/j.fluid.2008.01.004 | 2 | 30 | binary | search_blocks |
| 10.1016/j.fluid.2009.12.009 | 2 | 16 | binary | search_blocks |
| 10.1016/j.fluid.2011.05.016 | 1 | 12 | binary | search_blocks |
| 10.1016/j.fluid.2011.08.009 | 1 | 28 | binary | search_blocks |
| 10.1016/j.fluid.2015.07.012 | 2 | 168 | binary | search_blocks |
| 10.1016/j.fluid.2017.05.012 | 4 | 34 | binary | search_blocks |
| 10.1016/j.fluid.2017.09.005 | 2 | 144 | binary | search_blocks |
| 10.1016/j.jct.2004.07.019 | 1 | 456 | binary | search_blocks |
| 10.1016/j.jct.2008.07.005 | 1 | 96 | binary | search_blocks |
| 10.1016/j.jct.2009.06.023 | 1 | 88 | binary | search_blocks |
| 10.1016/j.jct.2010.12.009 | 1 | 60 | binary | search_blocks |
| 10.1016/j.jct.2011.12.018 | 1 | 22 | binary | search_blocks |
| 10.1016/j.jct.2012.01.013 | 1 | 45 | binary | search_blocks |
| 10.1016/j.jct.2012.12.019 | 2 | 74 | binary | search_blocks |
| 10.1016/j.jct.2013.11.036 | 2 | 203 | binary | search_blocks |
| 10.1016/j.jct.2015.06.024 | 2 | 80 | binary | search_blocks |
| 10.1016/j.jct.2016.10.001 | 2 | 36 | binary | search_blocks |
| 10.1016/j.jct.2017.06.014 | 2 | 42 | binary | search_blocks |
| 10.1016/j.jct.2017.07.003 | 1 | 36 | binary | search_blocks |
| 10.1016/j.jct.2017.10.005 | 2 | 10 | binary | search_blocks |
| 10.1016/j.jct.2019.105880 | 3 | 48 | binary | search_blocks |
| 10.1016/j.tca.2009.03.014 | 1 | 14 | binary | search_blocks |
| 10.1016/j.tca.2013.02.010 | 1 | 22 | binary | search_blocks |
| 10.1016/j.tca.2015.09.022 | 1 | 1 | binary | search_blocks |
| 10.1016/j.tca.2018.09.022 | 1 | 1 | binary | search_blocks |
| 10.1021/acs.jced.5b00200 | 1 | 1 | binary | search_blocks |
| 10.1021/acs.jced.6b01058 | 1 | 12 | binary | search_blocks |
| 10.1021/acs.jced.7b00299 | 3 | 5 | binary | search_blocks |
| 10.1021/acs.jced.8b00181 | 2 | 10 | binary | search_blocks |
| 10.1021/acs.jced.9b00102 | 3 | 166 | binary | search_blocks |
| 10.1021/je034101z | 1 | 380 | binary | search_blocks |
| 10.1021/je049738c | 1 | 8 | binary | search_blocks |
| 10.1021/je0601098 | 1 | 12 | binary | search_blocks |
| 10.1021/je060307z | 1 | 21 | binary | search_blocks |
| 10.1021/je4003515 | 1 | 25 | binary | search_blocks |
| 10.1021/je700700f | 1 | 13 | binary | query_thermoml_parallel, search_blocks |
| 10.1021/je800158z | 1 | 56 | binary | search_blocks |
| 10.1021/je900966r | 1 | 30 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2005.08.018 | PROPblock_7 | declared | 3 | binary | — | search_blocks |
| 10.1016/j.fluid.2005.08.018 | PROPblock_8 | declared | 7 | binary | — | search_blocks |
| 10.1016/j.fluid.2005.08.018 | PROPblock_9 | declared | 4 | binary | — | search_blocks |
| 10.1016/j.fluid.2007.07.066 | PROPblock_7 | declared | 15 | binary | — | search_blocks |
| 10.1016/j.fluid.2007.07.066 | PROPblock_8 | declared | 15 | binary | — | search_blocks |
| 10.1016/j.fluid.2008.01.004 | PROPblock_4 | declared | 15 | binary | — | search_blocks |
| 10.1016/j.fluid.2008.01.004 | PROPblock_5 | declared | 15 | binary | — | search_blocks |
| 10.1016/j.fluid.2009.12.009 | PROPblock_7 | declared | 8 | binary | — | search_blocks |
| 10.1016/j.fluid.2009.12.009 | PROPblock_8 | declared | 8 | binary | — | search_blocks |
| 10.1016/j.fluid.2011.05.016 | PROPblock_1 | declared | 12 | binary | — | search_blocks |
| 10.1016/j.fluid.2011.08.009 | PROPblock_6 | declared | 28 | binary | — | search_blocks |
| 10.1016/j.fluid.2015.07.012 | PROPblock_5 | declared | 84 | binary | — | search_blocks |
| 10.1016/j.fluid.2015.07.012 | PROPblock_6 | declared | 84 | binary | — | search_blocks |
| 10.1016/j.fluid.2017.05.012 | PROPblock_4 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.fluid.2017.05.012 | PROPblock_5 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.fluid.2017.05.012 | PROPblock_6 | declared | 1 | binary | — | search_blocks |
| 10.1016/j.fluid.2017.05.012 | PROPblock_7 | declared | 1 | binary | — | search_blocks |
| 10.1016/j.fluid.2017.09.005 | PROPblock_5 | declared | 72 | binary | — | search_blocks |
| 10.1016/j.fluid.2017.09.005 | PROPblock_6 | declared | 72 | binary | — | search_blocks |
| 10.1016/j.jct.2004.07.019 | PROPblock_3 | declared | 456 | binary | — | search_blocks |
| 10.1016/j.jct.2008.07.005 | PROPblock_9 | declared | 96 | binary | — | search_blocks |
| 10.1016/j.jct.2009.06.023 | PROPblock_14 | declared | 88 | binary | — | search_blocks |
| 10.1016/j.jct.2010.12.009 | PROPblock_20 | declared | 60 | binary | — | search_blocks |
| 10.1016/j.jct.2011.12.018 | PROPblock_1 | declared | 22 | binary | — | search_blocks |
| 10.1016/j.jct.2012.01.013 | PROPblock_23 | declared | 45 | binary | — | search_blocks |
| 10.1016/j.jct.2012.12.019 | PROPblock_2 | declared | 37 | binary | — | search_blocks |
| 10.1016/j.jct.2012.12.019 | PROPblock_3 | declared | 37 | binary | — | search_blocks |
| 10.1016/j.jct.2013.11.036 | PROPblock_1 | declared | 174 | binary | — | search_blocks |
| 10.1016/j.jct.2013.11.036 | PROPblock_2 | declared | 29 | binary | — | search_blocks |
| 10.1016/j.jct.2015.06.024 | PROPblock_5 | declared | 40 | binary | — | search_blocks |
| 10.1016/j.jct.2015.06.024 | PROPblock_6 | declared | 40 | binary | — | search_blocks |
| 10.1016/j.jct.2016.10.001 | PROPblock_7 | declared | 18 | binary | — | search_blocks |
| 10.1016/j.jct.2016.10.001 | PROPblock_8 | declared | 18 | binary | — | search_blocks |
| 10.1016/j.jct.2017.06.014 | PROPblock_3 | declared | 21 | binary | — | search_blocks |
| 10.1016/j.jct.2017.06.014 | PROPblock_4 | declared | 21 | binary | — | search_blocks |
| 10.1016/j.jct.2017.07.003 | PROPblock_6 | declared | 36 | binary | — | search_blocks |
| 10.1016/j.jct.2017.10.005 | PROPblock_13 | declared | 5 | binary | — | search_blocks |
| 10.1016/j.jct.2017.10.005 | PROPblock_14 | declared | 5 | binary | — | search_blocks |
| 10.1016/j.jct.2019.105880 | PROPblock_7 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.jct.2019.105880 | PROPblock_8 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.jct.2019.105880 | PROPblock_9 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.tca.2009.03.014 | PROPblock_16 | declared | 14 | binary | — | search_blocks |
| 10.1016/j.tca.2013.02.010 | PROPblock_7 | declared | 22 | binary | — | search_blocks |
| 10.1016/j.tca.2015.09.022 | PROPblock_43 | declared | 1 | binary | — | search_blocks |
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
| 10.1021/je034101z | PROPblock_6 | declared | 380 | binary | — | search_blocks |
| 10.1021/je049738c | PROPblock_26 | declared | 8 | binary | — | search_blocks |
| 10.1021/je0601098 | PROPblock_22 | declared | 12 | binary | — | search_blocks |
| 10.1021/je060307z | PROPblock_7 | declared | 21 | binary | — | search_blocks |
| 10.1021/je4003515 | PROPblock_10 | declared | 25 | binary | — | search_blocks |
| 10.1021/je700700f | PROPblock_14 | declared | 13 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1021/je800158z | PROPblock_3 | declared | 56 | binary | — | search_blocks |
| 10.1021/je900966r | PROPblock_4 | declared | 30 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 1 | `query_thermoml_parallel` | queries=[{'label': 'direct_VE', 'purp… | 132 | — | — | 0.0 |
| 2 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve compound ID… | 203 | KEEP ←in 283 | 203 | 4.0 |
| 3 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve compound ID… | 210 | KEEP ←in 283 | 210 | 4.6 |
| 4 | 3 | `resolve_property_ids` | limit=10, min_score=50, purpose=Find the global pr… | 132 | KEEP ←in 227 | 132 | 7.3 |
| 5 | 5 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_5'], limit=50, p… | 976 | DISCARD ←in 39 | 918 | 11.1 |
| 6 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_5'], limit=50, p… | 616 | KEEP ←in 11,346 | 600 | 23.2 |
| 7 | 5 | `inspect_block_table` | block_number=PROPblock_14, literature=GLOBlit_1104… | 352 | — | — | 0.3 |
| 8 | 6 | `inspect_block_table` | block_number=PROPblock_14, literature=GLOBlit_1104… | 1,195 | — | — | 0.1 |
| 9 | 6 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_5'], limit=50, p… | 1,024 | DISCARD ←in 39 | 966 | 18.7 |
| 10 | 7 | `search_blocks` | compound=['GLOBcomp_5'], limit=20, property=GLOBpr… | 1,294 | KEEP ←in 8,762 | 1279 | 20.4 |
| 11 | 8 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_5'], limit=50, p… | 703 | KEEP ←in 31,749 | 627 | 21.8 |
| 12 | 9 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_5'], limit=20, p… | 697 | DISCARD ←in 39 | 639 | 15.0 |
| 13 | 2 | `query_thermoml_parallel` | queries=[{'label': 'direct_VE', 'purp… | 17,501 | — | — | 221.7 |
| 14 | 6 | `inspect_block` | block_number=PROPblock_14, doi=10.1021/je700700f, … | 1,367 | — | — | 0.1 |
| 15 | 10 | `fit_block_derived` | block_number=PROPblock_14, composition_hint=mole_f… | 957 | — | — | 1.8 |
| 16 | 12 | `predict_from_rk` | coeffs=[-2.58261e-06, 6.379e-07, -7.…, mixing_rule… | 210 | — | — | 0.0 |
| 17 | 13 | `list_session_files` |  | 1,561 | — | — | 0.1 |
| | | **TOTAL (17 tools)** | | **29,130** | | **5,574** | **350.2** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 22,518 | 733 | 23,251 | 1,570 | 10.3 |
| 2 | L0-main | claudeopus46 | 22,518 | 1,198 | 23,716 | 1,336 | 8.6 |
| 3 | L1-worker | claudeopus46 | 24,095 | 919 | 25,014 | 597 | 4.6 |
| 4 | L1-worker | claudeopus46 | 24,095 | 988 | 25,083 | 617 | 4.8 |
| 5 | L1-worker | claudeopus46 | 24,095 | 2,006 | 26,101 | 535 | 4.0 |
| 6 | L1-worker | claudeopus46 | 24,095 | 1,937 | 26,032 | 549 | 4.2 |
| 7 | L1-worker | claudeopus46 | 3,767 | 442 | 4,209 | 370 | 3.9 |
| 8 | L1-worker | claudeopus46 | 3,767 | 442 | 4,209 | 377 | 4.4 |
| 9 | L1-worker | claudeopus46 | 24,095 | 1,621 | 25,716 | 563 | 4.7 |
| 10 | L1-worker | claudeopus46 | 24,095 | 1,573 | 25,668 | 854 | 7.0 |
| 11 | L1-worker | claudeopus46 | 3,767 | 408 | 4,175 | 297 | 3.6 |
| 12 | L1-worker | claudeopus46 | 3,767 | 710 | 4,477 | 294 | 3.5 |
| 13 | L1-worker | claudeopus46 | 24,095 | 2,278 | 26,373 | 764 | 5.1 |
| 14 | L1-worker | claudeopus46 | 24,095 | 2,037 | 26,132 | 923 | 6.8 |
| 15 | L1-worker | claudeopus46 | 24,095 | 2,787 | 26,882 | 706 | 5.1 |
| 16 | L1-worker | claudeopus46 | 3,767 | 598 | 4,365 | 1,307 | 10.7 |
| 17 | L1-worker | claudeopus46 | 3,767 | 11,867 | 15,634 | 1,942 | 16.0 |
| 18 | L1-worker | claudeopus46 | 24,095 | 3,751 | 27,846 | 875 | 7.4 |
| 19 | L1-worker | claudeopus46 | 24,095 | 2,889 | 26,984 | 1,568 | 11.1 |
| 20 | L1-worker | claudeopus46 | 24,095 | 3,642 | 27,737 | 755 | 6.1 |
| 21 | L1-worker | claudeopus46 | 3,767 | 505 | 4,272 | 1,370 | 9.7 |
| 22 | L1-worker | claudeopus46 | 24,095 | 5,149 | 29,244 | 836 | 6.7 |
| 23 | L1-worker | claudeopus46 | 24,095 | 5,194 | 29,289 | 1,582 | 16.7 |
| 24 | L1-worker | claudeopus46 | 3,767 | 9,148 | 12,915 | 1,555 | 13.7 |
| 25 | L1-worker | claudeopus46 | 24,095 | 9,504 | 33,599 | 2,994 | 19.8 |
| 26 | L1-worker | claudeopus46 | 24,095 | 6,856 | 30,951 | 802 | 6.3 |
| 27 | L1-worker | claudeopus46 | 24,095 | 14,948 | 39,043 | 2,247 | 14.1 |
| 28 | L1-worker | claudeopus46 | 2,320 | 1,680 | 4,000 | 638 | 4.2 |
| 29 | L1-worker | claudeopus46 | 2,106 | 2,720 | 4,826 | 963 | 5.8 |
| 30 | L1-worker | claudeopus46 | 627 | 1,560 | 2,187 | 816 | 5.9 |
| 31 | L1-worker | claudeopus46 | 366 | 1,075 | 1,441 | 603 | 3.4 |
| 32 | L1-worker | claudeopus46 | 366 | 1,740 | 2,106 | 596 | 3.4 |
| 33 | L1-worker | claudeopus46 | 3,767 | 32,097 | 35,864 | 1,660 | 14.9 |
| 34 | L1-worker | claudeopus46 | 787 | 10,854 | 11,641 | 662 | 7.4 |
| 35 | L1-worker | claudeopus46 | 24,095 | 7,945 | 32,040 | 1,560 | 11.1 |
| 36 | L1-worker | claudeopus46 | 3,767 | 484 | 4,251 | 899 | 7.4 |
| 37 | L1-worker | claudeopus46 | 24,095 | 9,105 | 33,200 | 2,269 | 15.5 |
| 38 | L1-worker | claudeopus46 | 24,095 | 14,457 | 38,552 | 2,917 | 19.3 |
| 39 | L1-worker | claudeopus46 | 24,095 | 19,319 | 43,414 | 2,650 | 13.5 |
| 40 | L1-worker | claudeopus46 | 2,106 | 2,950 | 5,056 | 308 | 2.9 |
| 41 | L1-worker | claudeopus46 | 2,320 | 1,841 | 4,161 | 532 | 3.3 |
| 42 | L1-worker | claudeopus46 | 627 | 1,721 | 2,348 | 871 | 5.2 |
| 43 | L1-worker | claudeopus46 | 366 | 1,085 | 1,451 | 202 | 2.4 |
| 44 | L1-worker | claudeopus46 | 366 | 1,282 | 1,648 | 858 | 3.7 |
| 45 | L1-worker | claudeopus46 | 787 | 5,390 | 6,177 | 518 | 5.2 |
| 46 | L0-main | claudeopus46 | 22,518 | 22,007 | 44,525 | 924 | 12.6 |
| 47 | L0-main | claudeopus46 | 22,518 | 23,040 | 45,558 | 529 | 4.3 |
| 48 | L0-main | claudeopus46 | 22,518 | 23,682 | 46,200 | 561 | 3.7 |
| 49 | L0-main | claudeopus46 | 22,518 | 24,421 | 46,939 | 597 | 4.0 |
| 50 | L0-main | claudeopus46 | 22,518 | 25,081 | 47,599 | 1,009 | 10.6 |
| 51 | L0-main | claudeopus46 | 22,518 | 25,829 | 48,347 | 792 | 5.6 |
| 52 | L0-main | claudeopus46 | 22,518 | 26,547 | 49,065 | 744 | 5.2 |
| 53 | L0-main | claudeopus46 | 22,518 | 27,274 | 49,792 | 676 | 4.4 |
| 54 | L0-main | claudeopus46 | 22,518 | 28,924 | 51,442 | 1,335 | 10.9 |
| 55 | L0-main | claudeopus46 | 22,518 | 29,727 | 52,245 | 814 | 5.5 |
| 56 | L0-main | claudeopus46 | 22,518 | 29,914 | 52,432 | 2,483 | 18.1 |
| 57 | L0-main | claudeopus46 | 22,518 | 31,785 | 54,303 | 6,168 | 45.7 |
| 58 | L0-main | claudeopus46 | 22,518 | 44,142 | 66,660 | 4,414 | 34.9 |
| 59 | L0-main | claudeopus46 | 22,518 | 52,166 | 74,684 | 4,009 | 31.3 |
| 60 | L0-main | claudeopus46 | 2,106 | 4,264 | 6,370 | 147 | 2.6 |
| 61 | L0-main | claudeopus46 | 366 | 670 | 1,036 | 188 | 2.4 |
| 62 | L0-main | claudeopus46 | 2,320 | 3,432 | 5,752 | 1,154 | 9.5 |
| 63 | L0-main | claudeopus46 | 366 | 1,591 | 1,957 | 1,109 | 5.4 |
| 64 | L0-main | claudeopus46 | 560 | 3,946 | 4,506 | 99 | 2.5 |
| 65 | L0-main | claudeopus46 | 1,156 | 4,703 | 5,859 | 551 | 5.5 |
| 66 | L0-main | claudeopus46 | 1,918 | 5,681 | 7,599 | 1,140 | 11.1 |

