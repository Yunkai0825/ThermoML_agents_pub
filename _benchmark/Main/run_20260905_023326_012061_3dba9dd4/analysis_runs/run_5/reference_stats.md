# Reference Stats — analysis-agent

**Run started:** 2026-09-05 02:42:05
**Wall time (at last flush):** 638.7 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 23 | 369,080 | 857,564 | 38,279 | 1,226,644 | 53,332 | 307.3 | claudeopus46 |
| L1-worker | 64 | 880,749 | 379,928 | 65,249 | 1,260,677 | 19,698 | 499.3 | claudeopus46 |
| **TOTAL** | **87** | **1,249,829** | **1,237,492** | **103,528** | **2,487,321** | **28,589** | **806.6** | |

**Estimated tokens:** ~621,830 input + ~25,882 output = ~647,712 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 4 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 5 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_property_ids` | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 5 | 3 | 16 | 17 | 1,379 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 14 | 6 | 6 | 27 | 50 | 1,775 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_id_alignment` | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml_parallel` | 2 | 1 | 5 | 1 | 3 | 3 | 0 |
| `search_blocks` | 2 | 1 | 5 | 3 | 16 | 17 | 1,379 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml` | 2 | 1 | 2 | 2 | 3 | 3 | 0 |
| `list_session_files` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **21** | **20** | **23** | **15** | **65** | **90** | **4,533** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_1 |  | query_thermoml, query_thermoml_parallel, resolve_compound_ids, search_blocks |
| GLOBcomp_797 |  | resolve_compound_ids |
| GLOBcomp_1168 |  | resolve_compound_ids |
| GLOBcomp_6445 |  | resolve_compound_ids |
| GLOBcomp_241 |  | resolve_compound_ids |
| GLOBcomp_5 |  | query_thermoml, query_thermoml_parallel, resolve_compound_ids, search_blocks |

#### Properties (15 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_28 |  | resolve_property_ids, search_id_alignment |
| GLOBprop_1 | Mass density, kg/m3 | query_thermoml, query_thermoml_parallel, search_blocks |
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

#### References (34 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_555 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_590 |  | search_blocks |
| GLOBlit_2432 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_2979 |  | query_thermoml, query_thermoml_parallel, search_blocks |
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
| GLOBlit_11142 |  | query_thermoml, search_blocks |
| GLOBlit_11872 |  | search_blocks |
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

#### Measurements (27 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_134 | Mass density, kg/m3 | query_thermoml, query_thermoml_parallel, search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBmeas_153 | Mass density, kg/m3 | query_thermoml, query_thermoml_parallel, search_blocks |
| GLOBmeas_66 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_6 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_170 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_143 | Mass density, kg/m3 | search_blocks |
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
| GLOBphase_1 |  | query_thermoml, query_thermoml_parallel, search_blocks |
| GLOBphase_3 |  | search_blocks |

#### Variables (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | query_thermoml, query_thermoml_parallel, search_blocks |
| GLOBvar_5 | Mass fraction | query_thermoml_parallel, search_blocks |
| GLOBvar_3 | Pressure, kPa | query_thermoml_parallel, search_blocks |
| GLOBvar_4 | Molality, mol/kg | query_thermoml_parallel, search_blocks |
| GLOBvar_2 | Mole fraction | query_thermoml, query_thermoml_parallel, search_blocks |
| GLOBvar_32 | Initial mass fraction of solute | search_blocks |

#### Constraints (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | query_thermoml, query_thermoml_parallel, search_blocks |
| GLOBconstr_8 | Molality, mol/kg | search_blocks |
| GLOBconstr_2 | Temperature, K | query_thermoml, search_blocks |
| GLOBconstr_3 | Mole fraction | search_blocks |
| GLOBconstr_25 | Final mass fraction of solute | search_blocks |
| GLOBconstr_4 | Frequency, MHz | search_blocks |

#### Solvents (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | query_thermoml_parallel, search_blocks |
| GLOBsolvent_9 |  | search_blocks |

#### Block_Types (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | query_thermoml, query_thermoml_parallel |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 6 |
| Unique Properties | 15 |
| Unique References | 34 |
| Unique Measurements | 27 |
| Unique Phases | 2 |
| Unique Variables | 6 |
| Unique Constraints | 6 |
| Unique Solvents | 2 |
| Unique Block_Types | 1 |
| Total DOIs | 34 |
| Unique parent blocks | 57 |
| Explicit block/subsystem targets | 57 |
| Subsystem targets | 0 |
| Target-matched data points | 5,265 |

---

## 3. DOI & Block References

**Unique DOIs:** 34  |  **Parent blocks:** 57  |  **Explicit targets:** 57  |  **Subsystems:** 0  |  **Target-matched datapoints:** 2,299

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2005.08.018 | 3 | 14 | binary | search_blocks |
| 10.1016/j.fluid.2007.07.066 | 2 | 30 | binary | query_thermoml_parallel, search_blocks |
| 10.1016/j.fluid.2008.01.004 | 2 | 30 | binary | search_blocks |
| 10.1016/j.fluid.2009.12.009 | 2 | 16 | binary | search_blocks |
| 10.1016/j.fluid.2011.05.016 | 1 | 12 | binary | search_blocks |
| 10.1016/j.fluid.2011.08.009 | 1 | 28 | binary | search_blocks |
| 10.1016/j.fluid.2015.07.012 | 2 | 168 | binary | search_blocks |
| 10.1016/j.fluid.2017.05.012 | 4 | 34 | binary | search_blocks |
| 10.1016/j.fluid.2017.09.005 | 2 | 144 | binary | search_blocks |
| 10.1016/j.jct.2004.07.019 | 1 | 456 | binary | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2008.07.005 | 1 | 96 | binary | query_thermoml, query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2011.12.018 | 1 | 22 | binary | search_blocks |
| 10.1016/j.jct.2012.12.019 | 2 | 74 | binary | search_blocks |
| 10.1016/j.jct.2013.11.036 | 2 | 203 | binary | search_blocks |
| 10.1016/j.jct.2015.06.024 | 2 | 80 | binary | search_blocks |
| 10.1016/j.jct.2016.10.001 | 2 | 36 | binary | search_blocks |
| 10.1016/j.jct.2017.06.014 | 2 | 42 | binary | search_blocks |
| 10.1016/j.jct.2017.07.003 | 1 | 36 | binary | search_blocks |
| 10.1016/j.jct.2017.10.005 | 2 | 10 | binary | search_blocks |
| 10.1016/j.jct.2019.105880 | 3 | 48 | binary | search_blocks |
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
| 10.1021/je4003515 | 1 | 25 | binary | search_blocks |
| 10.1021/je700700f | 1 | 13 | binary | query_thermoml, search_blocks |
| 10.1021/je800158z | 1 | 56 | binary | query_thermoml, search_blocks |
| 10.1021/je900966r | 1 | 30 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2005.08.018 | PROPblock_7 | declared | 3 | binary | — | search_blocks |
| 10.1016/j.fluid.2005.08.018 | PROPblock_8 | declared | 7 | binary | — | search_blocks |
| 10.1016/j.fluid.2005.08.018 | PROPblock_9 | declared | 4 | binary | — | search_blocks |
| 10.1016/j.fluid.2007.07.066 | PROPblock_7 | declared | 15 | binary | — | search_blocks |
| 10.1016/j.fluid.2007.07.066 | PROPblock_8 | declared | 15 | binary | 2 | query_thermoml_parallel, search_blocks |
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
| 10.1016/j.jct.2004.07.019 | PROPblock_3 | declared | 456 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2008.07.005 | PROPblock_9 | declared | 96 | binary | 2 | query_thermoml, query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2011.12.018 | PROPblock_1 | declared | 22 | binary | — | search_blocks |
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
| 10.1021/je4003515 | PROPblock_10 | declared | 25 | binary | — | search_blocks |
| 10.1021/je700700f | PROPblock_14 | declared | 13 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je800158z | PROPblock_3 | declared | 56 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je900966r | PROPblock_4 | declared | 30 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 1 | `query_thermoml_parallel` | queries=[{'label': 'VE_direct', 'purp… | 218 | — | — | 0.0 |
| 2 | 2 | `query_thermoml_parallel` | queries=[{'label': 'VE_direct', 'purp… | 253 | — | — | 0.0 |
| 3 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve water and 1… | 569 | KEEP ←in 428 | 569 | 9.8 |
| 4 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve compound ID… | 548 | KEEP ←in 496 | 548 | 9.1 |
| 5 | 3 | `resolve_compound_ids` | limit=10, min_score=50, purpose=Resolve 1-propanol… | 202 | KEEP ←in 227 | 202 | 3.9 |
| 6 | 3 | `resolve_compound_ids` | limit=10, min_score=50, purpose=Find GLOBcomp ID f… | 267 | KEEP ←in 227 | 267 | 5.0 |
| 7 | 4 | `resolve_property_ids` | limit=10, min_score=50, purpose=Find GLOBprop ID f… | 200 | KEEP ←in 227 | 200 | 3.6 |
| 8 | 6 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_5'], limit=50, p… | 918 | DISCARD ←in 39 | 860 | 8.5 |
| 9 | 5 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_5'], limit=50, p… | 1,200 | KEEP ←in 11,346 | 1185 | 20.6 |
| 10 | 7 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_5'], limit=50, p… | 1,044 | DISCARD ←in 39 | 986 | 18.9 |
| 11 | 7 | `inspect_block_table` | block_number=PROPblock_9, literature=GLOBlit_2979,… | 249 | — | — | 0.1 |
| 12 | 8 | `inspect_block_table` | block_number=PROPblock_9, literature=GLOBlit_2979,… | 377 | — | — | 0.2 |
| 13 | 9 | `inspect_block_table` | block_number=PROPblock_9, literature=GLOBlit_2979,… | 1,598 | — | — | 0.1 |
| 14 | 8 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_5'], limit=50, p… | 768 | KEEP ←in 31,749 | 632 | 21.1 |
| 15 | 10 | `inspect_block_table` | block_number=PROPblock_8, literature=GLOBlit_555, … | 883 | — | — | 0.2 |
| 16 | 9 | `search_id_alignment` | entity_type=property, limit=20, purpose=Find alter… | 310 | KEEP ←in 289 | 310 | 4.5 |
| 17 | 11 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_2432,… | 957 | — | — | 0.1 |
| 18 | 3 | `query_thermoml_parallel` | queries=[{'label': 'VE_direct', 'purp… | 38,620 | — | — | 174.1 |
| 19 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_5'], limit=50, p… | 423 | KEEP ←in 11,346 | 391 | 20.0 |
| 20 | 3 | `inspect_block_table` | block_number=PROPblock_14, literature=GLOBlit_1104… | 1,195 | — | — | 0.2 |
| 21 | 4 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_11142… | 259 | — | — | 0.0 |
| 22 | 5 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_11142… | 372 | — | — | 0.1 |
| 23 | 6 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_11142… | 373 | — | — | 0.1 |
| 24 | 7 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_11142… | 944 | — | — | 0.1 |
| 25 | 8 | `inspect_block_table` | block_number=PROPblock_14, literature=GLOBlit_1104… | 962 | — | — | 0.1 |
| 26 | 9 | `inspect_block_table` | block_number=PROPblock_14, literature=GLOBlit_1104… | 1,157 | — | — | 0.1 |
| 27 | 11 | `inspect_block_table` | block_number=PROPblock_9, literature=GLOBlit_2979,… | 1,629 | — | — | 0.2 |
| 28 | 4 | `query_thermoml` | context=Previously found 17 density b…, id_catalog… | 32,146 | — | — | 157.4 |
| 29 | 7 | `inspect_block` | block_number=PROPblock_14, doi=10.1021/je700700f, … | 1,367 | — | — | 0.1 |
| 30 | 11 | `fit_block_derived` | block_number=PROPblock_14, composition_hint=mole_f… | 957 | — | — | 1.7 |
| 31 | 12 | `predict_from_rk` | coeffs=[-2.58261e-06, 6.379e-07, -7.…, n_points=10… | 210 | — | — | 0.1 |
| 32 | 13 | `list_session_files` |  | 1,561 | — | — | 0.0 |
| | | **TOTAL (32 tools)** | | **92,736** | | **6,150** | **460.0** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 22,518 | 661 | 23,179 | 2,147 | 12.3 |
| 2 | L0-main | claudeopus46 | 22,518 | 1,203 | 23,721 | 1,555 | 8.8 |
| 3 | L0-main | claudeopus46 | 22,518 | 1,726 | 24,244 | 1,402 | 9.0 |
| 4 | L1-worker | claudeopus46 | 24,095 | 948 | 25,043 | 668 | 5.5 |
| 5 | L1-worker | claudeopus46 | 24,095 | 962 | 25,057 | 777 | 5.9 |
| 6 | L1-worker | claudeopus46 | 24,095 | 1,990 | 26,085 | 578 | 4.0 |
| 7 | L1-worker | claudeopus46 | 24,095 | 2,028 | 26,123 | 583 | 4.3 |
| 8 | L1-worker | claudeopus46 | 3,767 | 593 | 4,360 | 917 | 8.4 |
| 9 | L1-worker | claudeopus46 | 3,767 | 685 | 4,452 | 964 | 8.0 |
| 10 | L1-worker | claudeopus46 | 24,095 | 1,966 | 26,061 | 500 | 4.1 |
| 11 | L1-worker | claudeopus46 | 24,095 | 1,940 | 26,035 | 545 | 4.7 |
| 12 | L1-worker | claudeopus46 | 3,767 | 388 | 4,155 | 319 | 3.7 |
| 13 | L1-worker | claudeopus46 | 3,767 | 371 | 4,138 | 516 | 4.5 |
| 14 | L1-worker | claudeopus46 | 24,095 | 2,464 | 26,559 | 632 | 4.8 |
| 15 | L1-worker | claudeopus46 | 24,095 | 2,416 | 26,511 | 861 | 7.0 |
| 16 | L1-worker | claudeopus46 | 3,767 | 403 | 4,170 | 304 | 3.4 |
| 17 | L1-worker | claudeopus46 | 24,095 | 3,147 | 27,242 | 649 | 4.9 |
| 18 | L1-worker | claudeopus46 | 24,095 | 2,926 | 27,021 | 876 | 7.2 |
| 19 | L1-worker | claudeopus46 | 24,095 | 3,682 | 27,777 | 703 | 5.1 |
| 20 | L1-worker | claudeopus46 | 3,767 | 607 | 4,374 | 1,107 | 8.1 |
| 21 | L1-worker | claudeopus46 | 3,767 | 11,833 | 15,600 | 1,557 | 15.0 |
| 22 | L1-worker | claudeopus46 | 24,095 | 4,576 | 28,671 | 884 | 6.5 |
| 23 | L1-worker | claudeopus46 | 24,095 | 4,314 | 28,409 | 3,435 | 23.0 |
| 24 | L1-worker | claudeopus46 | 3,767 | 476 | 4,243 | 1,522 | 10.7 |
| 25 | L1-worker | claudeopus46 | 24,095 | 5,992 | 30,087 | 847 | 6.6 |
| 26 | L1-worker | claudeopus46 | 24,095 | 10,837 | 34,932 | 1,184 | 10.3 |
| 27 | L1-worker | claudeopus46 | 24,095 | 11,512 | 35,607 | 588 | 5.0 |
| 28 | L1-worker | claudeopus46 | 24,095 | 12,207 | 36,302 | 612 | 6.1 |
| 29 | L1-worker | claudeopus46 | 3,767 | 32,122 | 35,889 | 1,669 | 13.8 |
| 30 | L1-worker | claudeopus46 | 24,095 | 14,125 | 38,220 | 845 | 9.8 |
| 31 | L1-worker | claudeopus46 | 24,095 | 7,127 | 31,222 | 902 | 6.3 |
| 32 | L1-worker | claudeopus46 | 3,767 | 504 | 4,271 | 495 | 4.3 |
| 33 | L1-worker | claudeopus46 | 24,095 | 15,336 | 39,431 | 1,056 | 9.3 |
| 34 | L1-worker | claudeopus46 | 24,095 | 7,831 | 31,926 | 2,538 | 15.9 |
| 35 | L1-worker | claudeopus46 | 2,106 | 2,575 | 4,681 | 308 | 2.9 |
| 36 | L1-worker | claudeopus46 | 2,320 | 1,492 | 3,812 | 546 | 3.4 |
| 37 | L1-worker | claudeopus46 | 627 | 1,372 | 1,999 | 762 | 5.1 |
| 38 | L1-worker | claudeopus46 | 366 | 1,085 | 1,451 | 202 | 2.2 |
| 39 | L1-worker | claudeopus46 | 366 | 1,173 | 1,539 | 749 | 4.0 |
| 40 | L1-worker | claudeopus46 | 366 | 983 | 1,349 | 511 | 7.3 |
| 41 | L1-worker | claudeopus46 | 24,095 | 16,641 | 40,736 | 2,854 | 24.6 |
| 42 | L1-worker | claudeopus46 | 787 | 4,548 | 5,335 | 481 | 4.8 |
| 43 | L1-worker | claudeopus46 | 2,320 | 2,985 | 5,305 | 1,073 | 7.4 |
| 44 | L1-worker | claudeopus46 | 627 | 2,865 | 3,492 | 1,059 | 7.9 |
| 45 | L1-worker | claudeopus46 | 2,106 | 4,054 | 6,160 | 1,649 | 8.3 |
| 46 | L1-worker | claudeopus46 | 366 | 1,510 | 1,876 | 1,033 | 4.3 |
| 47 | L1-worker | claudeopus46 | 366 | 2,426 | 2,792 | 1,269 | 6.0 |
| 48 | L1-worker | claudeopus46 | 787 | 26,201 | 26,988 | 703 | 8.7 |
| 49 | L0-main | claudeopus46 | 22,518 | 37,848 | 60,366 | 2,640 | 26.6 |
| 50 | L1-worker | claudeopus46 | 24,095 | 2,202 | 26,297 | 907 | 6.1 |
| 51 | L1-worker | claudeopus46 | 24,095 | 2,917 | 27,012 | 560 | 4.2 |
| 52 | L1-worker | claudeopus46 | 3,767 | 11,793 | 15,560 | 1,778 | 14.5 |
| 53 | L1-worker | claudeopus46 | 24,095 | 3,287 | 27,382 | 980 | 7.6 |
| 54 | L1-worker | claudeopus46 | 24,095 | 4,867 | 28,962 | 1,384 | 11.4 |
| 55 | L1-worker | claudeopus46 | 24,095 | 5,509 | 29,604 | 549 | 4.8 |
| 56 | L1-worker | claudeopus46 | 24,095 | 6,157 | 30,252 | 691 | 6.1 |
| 57 | L1-worker | claudeopus46 | 24,095 | 6,870 | 30,965 | 960 | 7.1 |
| 58 | L1-worker | claudeopus46 | 24,095 | 8,203 | 32,298 | 1,639 | 12.8 |
| 59 | L1-worker | claudeopus46 | 24,095 | 9,644 | 33,739 | 863 | 8.2 |
| 60 | L1-worker | claudeopus46 | 24,095 | 11,108 | 35,203 | 2,001 | 16.5 |
| 61 | L1-worker | claudeopus46 | 24,095 | 15,593 | 39,688 | 1,312 | 10.1 |
| 62 | L1-worker | claudeopus46 | 24,095 | 17,548 | 41,643 | 2,409 | 20.0 |
| 63 | L1-worker | claudeopus46 | 2,320 | 2,540 | 4,860 | 1,125 | 6.6 |
| 64 | L1-worker | claudeopus46 | 627 | 2,420 | 3,047 | 1,062 | 6.6 |
| 65 | L1-worker | claudeopus46 | 2,106 | 4,863 | 6,969 | 1,642 | 9.1 |
| 66 | L1-worker | claudeopus46 | 366 | 1,562 | 1,928 | 1,080 | 4.3 |
| 67 | L1-worker | claudeopus46 | 366 | 2,419 | 2,785 | 951 | 4.7 |
| 68 | L1-worker | claudeopus46 | 787 | 24,208 | 24,995 | 524 | 5.5 |
| 69 | L0-main | claudeopus46 | 22,518 | 57,876 | 80,394 | 908 | 10.3 |
| 70 | L0-main | claudeopus46 | 22,518 | 58,583 | 81,101 | 602 | 5.0 |
| 71 | L0-main | claudeopus46 | 22,518 | 59,293 | 81,811 | 586 | 5.3 |
| 72 | L0-main | claudeopus46 | 22,518 | 60,824 | 83,342 | 1,215 | 14.3 |
| 73 | L0-main | claudeopus46 | 22,518 | 61,583 | 84,101 | 752 | 5.9 |
| 74 | L0-main | claudeopus46 | 22,518 | 62,257 | 84,775 | 816 | 7.1 |
| 75 | L0-main | claudeopus46 | 22,518 | 63,070 | 85,588 | 711 | 5.0 |
| 76 | L0-main | claudeopus46 | 22,518 | 64,625 | 87,143 | 1,245 | 9.1 |
| 77 | L0-main | claudeopus46 | 22,518 | 65,219 | 87,737 | 2,449 | 18.8 |
| 78 | L0-main | claudeopus46 | 22,518 | 67,089 | 89,607 | 8,697 | 62.2 |
| 79 | L0-main | claudeopus46 | 22,518 | 81,192 | 103,710 | 4,484 | 40.5 |
| 80 | L0-main | claudeopus46 | 22,518 | 89,584 | 112,102 | 3,447 | 30.5 |
| 81 | L0-main | claudeopus46 | 2,106 | 4,336 | 6,442 | 147 | 2.5 |
| 82 | L0-main | claudeopus46 | 366 | 670 | 1,036 | 188 | 2.6 |
| 83 | L0-main | claudeopus46 | 2,320 | 3,576 | 5,896 | 1,360 | 9.4 |
| 84 | L0-main | claudeopus46 | 366 | 1,797 | 2,163 | 1,310 | 5.2 |
| 85 | L0-main | claudeopus46 | 560 | 4,090 | 4,650 | 93 | 2.1 |
| 86 | L0-main | claudeopus46 | 1,156 | 4,847 | 6,003 | 446 | 4.8 |
| 87 | L0-main | claudeopus46 | 1,918 | 5,615 | 7,533 | 1,079 | 10.0 |

