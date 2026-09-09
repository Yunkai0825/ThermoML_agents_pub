# Reference Stats — query-agent

**Run started:** 2026-08-03 11:27:08
**Wall time (at last flush):** 778.4 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 10 | 60,905 | 245,212 | 26,961 | 306,117 | 30,611 | 157.1 | claudeopus46 |
| L1-worker | 75 | 472,846 | 730,255 | 118,244 | 1,203,101 | 16,041 | 670.6 | claudeopus46 |
| **TOTAL** | **85** | **533,751** | **975,467** | **145,205** | **1,509,218** | **17,755** | **827.7** | |

**Estimated tokens:** ~377,304 input + ~36,301 output = ~413,605 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_property_ids` | 0 | 5 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 16 | 5 | 4 | 20 | 30 | 712 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 4 | 2 | 5 | 5 | 182 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 80 |
| `resolve_property_ids` | 0 | 3 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 2 | 2 | 1 | 1 | 100 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_property_ids` | 0 | 3 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 2 | 2 | 1 | 1 | 100 |
| **TOTAL** | **14** | **31** | **15** | **11** | **28** | **38** | **1,174** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_15 |  | resolve_compound_ids, search_blocks |

#### Properties (18 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_42 |  | resolve_property_ids, search_blocks |
| GLOBprop_44 |  | resolve_property_ids |
| GLOBprop_33 |  | resolve_property_ids |
| GLOBprop_1 |  | resolve_property_ids, search_blocks |
| GLOBprop_4 |  | resolve_property_ids, search_blocks |
| GLOBprop_3 | Activity coefficient | search_blocks |
| GLOBprop_28 | Excess molar volume, m3/mol | search_blocks |
| GLOBprop_7 | Refractive index (Na D-line) | search_blocks |
| GLOBprop_14 | Boiling temperature at pressure P, K | search_blocks |
| GLOBprop_2 | Mole fraction | search_blocks |
| GLOBprop_8 | Speed of sound, m/s | search_blocks |
| GLOBprop_9 | Molar heat capacity at constant pressure, J/K/mol | search_blocks |
| GLOBprop_13 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBprop_15 | Molar enthalpy of solution, kJ/mol | search_blocks |
| GLOBprop_55 | Henry's Law constant (molality scale), kPa*kg/mol | search_blocks |
| GLOBprop_58 | Azeotropic temperature, K | search_blocks |
| GLOBprop_45 | Azeotropic composition: mole fraction | search_blocks |
| GLOBprop_5 | Vapor or sublimation pressure, kPa | search_blocks |

#### References (20 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_664 |  | search_blocks |
| GLOBlit_1014 |  | search_blocks |
| GLOBlit_1333 |  | search_blocks |
| GLOBlit_1501 |  | search_blocks |
| GLOBlit_2602 |  | search_blocks |
| GLOBlit_2736 |  | search_blocks |
| GLOBlit_3240 |  | search_blocks |
| GLOBlit_3286 |  | search_blocks |
| GLOBlit_5572 |  | search_blocks |
| GLOBlit_5714 |  | search_blocks |
| GLOBlit_5904 |  | search_blocks |
| GLOBlit_7312 |  | search_blocks |
| GLOBlit_8888 |  | search_blocks |
| GLOBlit_9129 |  | search_blocks |
| GLOBlit_10006 |  | search_blocks |
| GLOBlit_10193 |  | search_blocks |
| GLOBlit_10215 |  | search_blocks |
| GLOBlit_10747 |  | search_blocks |
| GLOBlit_11018 |  | search_blocks |
| GLOBlit_11299 |  | search_blocks |

#### Measurements (19 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_289 | Activity coefficient | search_blocks |
| GLOBmeas_29 | Excess molar volume, m3/mol | search_blocks |
| GLOBmeas_3 | Refractive index (Na D-line) | search_blocks |
| GLOBmeas_5 | Boiling temperature at pressure P, K | search_blocks |
| GLOBmeas_1 | Mole fraction | search_blocks |
| GLOBmeas_140 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_147 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_311 | Speed of sound, m/s | search_blocks |
| GLOBmeas_167 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_17 | Molar heat capacity at constant pressure, J/K/mol | search_blocks |
| GLOBmeas_19 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBmeas_144 | Molar enthalpy of solution, kJ/mol | search_blocks |
| GLOBmeas_967 | Boiling temperature at pressure P, K | search_blocks |
| GLOBmeas_15 | Speed of sound, m/s | search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_39 | Azeotropic temperature, K | search_blocks |
| GLOBmeas_53 | Relative permittivity at various frequencies | search_blocks |
| GLOBmeas_138 | Mass density, kg/m3 | search_blocks |

#### Phases (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks |
| GLOBphase_3 |  | search_blocks |

#### Constraints (4 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_2 | Temperature, K | search_blocks |
| GLOBconstr_3 | Mole fraction | search_blocks |
| GLOBconstr_1 | Pressure, kPa | search_blocks |
| GLOBconstr_4 | Frequency, MHz | search_blocks |

#### Variables (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_2 | Mole fraction | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |
| GLOBvar_3 | Pressure, kPa | search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |

#### Solvents (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | search_blocks |
| GLOBsolvent_5 |  | search_blocks |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 2 |
| Unique Properties | 18 |
| Unique References | 20 |
| Unique Measurements | 19 |
| Unique Phases | 2 |
| Unique Constraints | 4 |
| Unique Variables | 5 |
| Unique Solvents | 2 |
| Total DOIs | 20 |
| Unique parent blocks | 30 |
| Explicit block/subsystem targets | 30 |
| Subsystem targets | 0 |
| Target-matched data points | 1,174 |

---

## 3. DOI & Block References

**Unique DOIs:** 20  |  **Parent blocks:** 30  |  **Explicit targets:** 30  |  **Subsystems:** 0  |  **Target-matched datapoints:** 712

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2008.09.011 | 2 | 3 | binary | search_blocks |
| 10.1016/j.fluid.2011.09.016 | 1 | 6 | binary | search_blocks |
| 10.1016/j.fluid.2013.09.028 | 1 | 2 | binary | search_blocks |
| 10.1016/j.fluid.2014.06.025 | 2 | 18 | binary | search_blocks |
| 10.1016/j.jct.2005.08.009 | 2 | 155 | binary | search_blocks |
| 10.1016/j.jct.2006.08.007 | 2 | 20 | binary | search_blocks |
| 10.1016/j.jct.2010.04.019 | 1 | 116 | binary | search_blocks |
| 10.1016/j.jct.2010.09.003 | 1 | 57 | binary | search_blocks |
| 10.1016/j.jct.2019.07.006 | 2 | 28 | binary | search_blocks |
| 10.1016/j.tca.2006.06.021 | 1 | 1 | binary | search_blocks |
| 10.1016/j.tca.2010.09.013 | 1 | 1 | binary | search_blocks |
| 10.1021/acs.jced.7b00755 | 2 | 10 | binary | search_blocks |
| 10.1021/je0601098 | 2 | 26 | binary | search_blocks |
| 10.1021/je1001329 | 1 | 12 | binary | search_blocks |
| 10.1021/je3010535 | 1 | 7 | binary | search_blocks |
| 10.1021/je400473z | 1 | 9 | binary | search_blocks |
| 10.1021/je400531a | 4 | 44 | binary | search_blocks |
| 10.1021/je700055p | 1 | 100 | binary | search_blocks |
| 10.1021/je700645p | 1 | 75 | binary | search_blocks |
| 10.1021/je800557h | 1 | 22 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2008.09.011 | PROPblock_1 | declared | 2 | binary | — | search_blocks |
| 10.1016/j.fluid.2008.09.011 | PROPblock_2 | declared | 1 | binary | — | search_blocks |
| 10.1016/j.fluid.2011.09.016 | PROPblock_1 | declared | 6 | binary | — | search_blocks |
| 10.1016/j.fluid.2013.09.028 | PROPblock_19 | declared | 2 | binary | — | search_blocks |
| 10.1016/j.fluid.2014.06.025 | PROPblock_1 | declared | 9 | binary | — | search_blocks |
| 10.1016/j.fluid.2014.06.025 | PROPblock_2 | declared | 9 | binary | — | search_blocks |
| 10.1016/j.jct.2005.08.009 | PROPblock_3 | declared | 80 | binary | — | search_blocks |
| 10.1016/j.jct.2005.08.009 | PROPblock_4 | declared | 75 | binary | — | search_blocks |
| 10.1016/j.jct.2006.08.007 | PROPblock_5 | declared | 10 | binary | — | search_blocks |
| 10.1016/j.jct.2006.08.007 | PROPblock_6 | declared | 10 | binary | — | search_blocks |
| 10.1016/j.jct.2010.04.019 | PROPblock_1 | declared | 116 | binary | — | search_blocks |
| 10.1016/j.jct.2010.09.003 | PROPblock_6 | declared | 57 | binary | — | search_blocks |
| 10.1016/j.jct.2019.07.006 | PROPblock_3 | declared | 14 | binary | — | search_blocks |
| 10.1016/j.jct.2019.07.006 | PROPblock_4 | declared | 14 | binary | — | search_blocks |
| 10.1016/j.tca.2006.06.021 | PROPblock_1 | declared | 1 | binary | — | search_blocks |
| 10.1016/j.tca.2010.09.013 | PROPblock_2 | declared | 1 | binary | — | search_blocks |
| 10.1021/acs.jced.7b00755 | PROPblock_4 | declared | 5 | binary | — | search_blocks |
| 10.1021/acs.jced.7b00755 | PROPblock_5 | declared | 5 | binary | — | search_blocks |
| 10.1021/je0601098 | PROPblock_25 | declared | 13 | binary | — | search_blocks |
| 10.1021/je0601098 | PROPblock_26 | declared | 13 | binary | — | search_blocks |
| 10.1021/je1001329 | PROPblock_4 | declared | 12 | binary | — | search_blocks |
| 10.1021/je3010535 | PROPblock_13 | declared | 7 | binary | — | search_blocks |
| 10.1021/je400473z | PROPblock_1 | declared | 9 | binary | — | search_blocks |
| 10.1021/je400531a | PROPblock_10 | declared | 21 | binary | — | search_blocks |
| 10.1021/je400531a | PROPblock_11 | declared | 21 | binary | — | search_blocks |
| 10.1021/je400531a | PROPblock_12 | declared | 1 | binary | — | search_blocks |
| 10.1021/je400531a | PROPblock_13 | declared | 1 | binary | — | search_blocks |
| 10.1021/je700055p | PROPblock_2 | declared | 100 | binary | — | search_blocks |
| 10.1021/je700645p | PROPblock_5 | declared | 75 | binary | — | search_blocks |
| 10.1021/je800557h | PROPblock_5 | declared | 22 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (pre-compaction)

| # | Iter | Tool | Args | Raw (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve compound ID… | 210 | KEEP | 210 | 4.2 |
| 2 | 2 | `resolve_property_ids` | limit=5, min_score=50, purpose=Resolve property ID… | 621 | KEEP | 621 | 7.0 |
| 3 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_15'], limit=50, … | 826 | KEEP | 765 | 21.5 |
| 4 | 1 | `L1_query` | context=This is for Fe electrodeposit…, id_catalog… | 450 | — | — | 243.7 |
| 5 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Find GLOBcomp IDs f… | 203 | KEEP | 203 | 4.0 |
| 6 | 2 | `L1_query` | context=Need these IDs to then search…, id_catalog… | 1,404 | — | — | 27.2 |
| 7 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_15'], limit=50, … | 1,270 | KEEP | 1270 | 22.3 |
| 8 | 3 | `L1_query` | context=Looking for solvent property …, id_catalog… | 270 | — | — | 66.4 |
| 9 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_15'], limit=50, … | 1,208 | KEEP | 1178 | 23.6 |
| 10 | 3 | `L1_query` | context=Looking for solvent property …, id_catalog… | 9,039 | — | — | 66.8 |
| 11 | 1 | `resolve_property_ids` | limit=10, min_score=40, purpose=Find GLOBprop_N fo… | 547 | KEEP | 547 | 8.6 |
| 12 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_15'], limit=50, … | 803 | DISCARD | 745 | 7.6 |
| 13 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_15'], limit=50, … | 1,282 | KEEP | 1250 | 13.9 |
| 14 | 3 | `L1_query` | context=Looking for dielectric consta…, id_catalog… | 645 | — | — | 100.0 |
| 15 | 1 | `resolve_property_ids` | limit=10, min_score=40, purpose=Find GLOBprop_N fo… | 498 | KEEP | 498 | 7.4 |
| 16 | 4 | `L1_query` | context=Need the property ID before s…, id_catalog… | 2,373 | — | — | 31.6 |
| 17 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_15'], limit=50, … | 756 | DISCARD | 698 | 15.7 |
| 18 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_15'], limit=50, … | 1,228 | KEEP | 1196 | 14.8 |
| 19 | 5 | `L1_query` | context=Looking for dielectric consta…, id_catalog… | 11,517 | — | — | 98.4 |
| | | **TOTAL (19 tools)** | | **35,150** | | **9,181** | **784.7** |

---

## 5. Compaction Events

| # | Trigger | Outcome | Before (chars) | After (chars) | Saved (chars) | Saved (%) |
|--:|---------|---------|---------------:|--------------:|--------------:|----------:|
| 1 | interval=3 | skipped_by_agent | 4,960 | 4,960 | 0 | 0.0% |

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 9,605 | 973 | 10,578 | 2,022 | 11.1 |
| 2 | L1-worker | claudeopus46 | 20,643 | 1,490 | 22,133 | 951 | 6.0 |
| 3 | L1-worker | claudeopus46 | 20,643 | 3,169 | 23,812 | 17,783 | 54.3 |
| 4 | L1-worker | claudeopus46 | 2,065 | 447 | 2,512 | 348 | 3.9 |
| 5 | L1-worker | claudeopus46 | 2,065 | 806 | 2,871 | 1,024 | 6.6 |
| 6 | L1-worker | claudeopus46 | 20,643 | 4,063 | 24,706 | 14,328 | 54.4 |
| 7 | L1-worker | claudeopus46 | 2,065 | 18,787 | 20,852 | 1,506 | 11.7 |
| 8 | L1-worker | claudeopus46 | 20,610 | 6,255 | 26,865 | 669 | 5.2 |
| 9 | L1-worker | claudeopus46 | 20,643 | 5,502 | 26,145 | 5,997 | 29.1 |
| 10 | L1-worker | claudeopus46 | 20,643 | 12,120 | 32,763 | 3,563 | 16.7 |
| 11 | L1-worker | claudeopus46 | 536 | 3,311 | 3,847 | 1,073 | 6.4 |
| 12 | L1-worker | claudeopus46 | 1,356 | 3,431 | 4,787 | 1,021 | 6.6 |
| 13 | L1-worker | claudeopus46 | 298 | 1,403 | 1,701 | 1,009 | 4.3 |
| 14 | L1-worker | claudeopus46 | 1,323 | 8,535 | 9,858 | 4,027 | 16.0 |
| 15 | L1-worker | claudeopus46 | 298 | 4,749 | 5,047 | 3,053 | 13.3 |
| 16 | L1-worker | claudeopus46 | 1,160 | 12,997 | 14,157 | 2,723 | 14.7 |
| 17 | L0-main | claudeopus46 | 9,605 | 2,000 | 11,605 | 889 | 6.8 |
| 18 | L1-worker | claudeopus46 | 20,643 | 808 | 21,451 | 582 | 4.8 |
| 19 | L1-worker | claudeopus46 | 20,643 | 2,011 | 22,654 | 946 | 5.5 |
| 20 | L1-worker | claudeopus46 | 2,065 | 500 | 2,565 | 409 | 3.9 |
| 21 | L1-worker | claudeopus46 | 20,643 | 2,134 | 22,777 | 394 | 3.6 |
| 22 | L1-worker | claudeopus46 | 1,323 | 2,142 | 3,465 | 234 | 2.7 |
| 23 | L1-worker | claudeopus46 | 536 | 405 | 941 | 293 | 3.0 |
| 24 | L1-worker | claudeopus46 | 1,356 | 525 | 1,881 | 310 | 3.6 |
| 25 | L1-worker | claudeopus46 | 298 | 956 | 1,254 | 154 | 2.3 |
| 26 | L1-worker | claudeopus46 | 747 | 2,648 | 3,395 | 353 | 3.8 |
| 27 | L0-main | claudeopus46 | 9,605 | 5,497 | 15,102 | 3,331 | 16.3 |
| 28 | L1-worker | claudeopus46 | 20,643 | 2,817 | 23,460 | 949 | 7.2 |
| 29 | L1-worker | claudeopus46 | 2,065 | 10,060 | 12,125 | 1,636 | 15.0 |
| 30 | L1-worker | claudeopus46 | 20,643 | 4,613 | 25,256 | 2,390 | 12.8 |
| 31 | L1-worker | claudeopus46 | 1,356 | 2,339 | 3,695 | 830 | 4.6 |
| 32 | L1-worker | claudeopus46 | 536 | 2,219 | 2,755 | 1,012 | 6.6 |
| 33 | L1-worker | claudeopus46 | 1,323 | 5,400 | 6,723 | 2,287 | 9.6 |
| 34 | L1-worker | claudeopus46 | 298 | 1,368 | 1,666 | 999 | 6.9 |
| 35 | L1-worker | claudeopus46 | 298 | 3,009 | 3,307 | 1,764 | 7.7 |
| 36 | L1-worker | claudeopus46 | 747 | 37,152 | 37,899 | 498 | 5.7 |
| 37 | L1-worker | claudeopus46 | 20,643 | 35,993 | 56,636 | 886 | 8.7 |
| 38 | L1-worker | claudeopus46 | 2,065 | 3,096 | 5,161 | 1,651 | 14.2 |
| 39 | L1-worker | claudeopus46 | 20,643 | 37,723 | 58,366 | 2,148 | 13.5 |
| 40 | L1-worker | claudeopus46 | 536 | 1,421 | 1,957 | 774 | 4.4 |
| 41 | L1-worker | claudeopus46 | 1,356 | 1,541 | 2,897 | 758 | 6.5 |
| 42 | L1-worker | claudeopus46 | 1,323 | 4,527 | 5,850 | 674 | 8.1 |
| 43 | L1-worker | claudeopus46 | 298 | 1,396 | 1,694 | 547 | 4.4 |
| 44 | L1-worker | claudeopus46 | 747 | 12,232 | 12,979 | 786 | 7.8 |
| 45 | L1-worker | claudeopus46 | 20,643 | 45,126 | 65,769 | 748 | 5.6 |
| 46 | L1-worker | claudeopus46 | 2,065 | 664 | 2,729 | 1,316 | 8.3 |
| 47 | L1-worker | claudeopus46 | 20,643 | 46,133 | 66,776 | 1,470 | 11.3 |
| 48 | L1-worker | claudeopus46 | 2,065 | 579 | 2,644 | 1,073 | 6.9 |
| 49 | L1-worker | claudeopus46 | 2,065 | 3,118 | 5,183 | 1,709 | 13.3 |
| 50 | L1-worker | claudeopus46 | 20,643 | 48,966 | 69,609 | 2,616 | 16.1 |
| 51 | L1-worker | claudeopus46 | 1,356 | 1,971 | 3,327 | 797 | 4.7 |
| 52 | L1-worker | claudeopus46 | 1,323 | 7,344 | 8,667 | 753 | 5.0 |
| 53 | L1-worker | claudeopus46 | 536 | 1,851 | 2,387 | 976 | 5.5 |
| 54 | L1-worker | claudeopus46 | 298 | 1,475 | 1,773 | 626 | 3.6 |
| 55 | L1-worker | claudeopus46 | 747 | 16,555 | 17,302 | 1,906 | 13.8 |
| 56 | L1-worker | claudeopus46 | 298 | 2,265 | 2,563 | 429 | 2.5 |
| 57 | L1-worker | claudeopus46 | 1,160 | 8,674 | 9,834 | 756 | 4.5 |
| 58 | L1-worker | claudeopus46 | 747 | 16,570 | 17,317 | 526 | 5.9 |
| 59 | L0-main | claudeopus46 | 9,605 | 49,782 | 59,387 | 1,476 | 9.8 |
| 60 | L1-worker | claudeopus46 | 20,643 | 44,909 | 65,552 | 652 | 5.1 |
| 61 | L1-worker | claudeopus46 | 2,065 | 636 | 2,701 | 1,141 | 7.2 |
| 62 | L1-worker | claudeopus46 | 20,643 | 45,854 | 66,497 | 854 | 5.7 |
| 63 | L1-worker | claudeopus46 | 536 | 863 | 1,399 | 465 | 3.2 |
| 64 | L1-worker | claudeopus46 | 1,323 | 2,911 | 4,234 | 235 | 3.4 |
| 65 | L1-worker | claudeopus46 | 1,356 | 983 | 2,339 | 520 | 3.7 |
| 66 | L1-worker | claudeopus46 | 298 | 957 | 1,255 | 155 | 2.6 |
| 67 | L1-worker | claudeopus46 | 747 | 4,165 | 4,912 | 577 | 6.6 |
| 68 | L0-main | claudeopus46 | 9,605 | 55,461 | 65,066 | 1,876 | 11.8 |
| 69 | L1-worker | claudeopus46 | 20,643 | 48,079 | 68,722 | 1,343 | 8.2 |
| 70 | L1-worker | claudeopus46 | 2,065 | 531 | 2,596 | 1,228 | 7.5 |
| 71 | L1-worker | claudeopus46 | 2,065 | 3,043 | 5,108 | 1,726 | 14.2 |
| 72 | L1-worker | claudeopus46 | 20,643 | 50,756 | 71,399 | 3,175 | 18.0 |
| 73 | L1-worker | claudeopus46 | 536 | 2,650 | 3,186 | 789 | 5.0 |
| 74 | L1-worker | claudeopus46 | 1,323 | 7,213 | 8,536 | 816 | 5.4 |
| 75 | L1-worker | claudeopus46 | 1,356 | 2,770 | 4,126 | 1,050 | 6.1 |
| 76 | L1-worker | claudeopus46 | 298 | 1,538 | 1,836 | 689 | 3.9 |
| 77 | L1-worker | claudeopus46 | 747 | 17,099 | 17,846 | 1,848 | 13.2 |
| 78 | L1-worker | claudeopus46 | 298 | 2,207 | 2,505 | 388 | 2.6 |
| 79 | L1-worker | claudeopus46 | 1,160 | 8,565 | 9,725 | 725 | 7.1 |
| 80 | L1-worker | claudeopus46 | 747 | 17,135 | 17,882 | 828 | 8.8 |
| 81 | L0-main | claudeopus46 | 9,605 | 79,308 | 88,913 | 5,498 | 36.7 |
| 82 | L0-main | claudeopus46 | 1,356 | 5,182 | 6,538 | 1,499 | 8.8 |
| 83 | L0-main | claudeopus46 | 298 | 1,881 | 2,179 | 1,487 | 5.5 |
| 84 | L0-main | claudeopus46 | 1,323 | 39,686 | 41,009 | 4,774 | 32.2 |
| 85 | L0-main | claudeopus46 | 298 | 5,442 | 5,740 | 4,109 | 18.1 |

