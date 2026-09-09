# Reference Stats — query-agent

**Run started:** 2026-09-05 04:43:18
**Wall time (at last flush):** 214.4 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 6 | 28,320 | 16,683 | 6,890 | 45,003 | 7,500 | 40.2 | claudeopus46 |
| L1-worker | 20 | 242,262 | 81,678 | 21,775 | 323,940 | 16,197 | 156.7 | claudeopus46 |
| verdict | 1 | 972 | 4,247 | 980 | 5,219 | 5,219 | 8.2 | claudeopus46 |
| **TOTAL** | **27** | **271,554** | **102,608** | **29,645** | **374,162** | **13,857** | **205.1** | |

**Estimated tokens:** ~93,540 input + ~7,411 output = ~100,951 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_property_ids` | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 9 | 5 | 2 | 11 | 16 | 1,377 |
| `search_blocks` | 16 | 1 | 1 | 2 | 3 | 15 | 203 |
| **TOTAL** | **18** | **11** | **6** | **4** | **14** | **31** | **1,580** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Properties (10 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_28 |  | resolve_property_ids, search_blocks |
| GLOBprop_1 | Mass density, kg/m3 | search_blocks |
| GLOBprop_8 | Speed of sound, m/s | search_blocks |
| GLOBprop_4 | Viscosity, Pa*s | search_blocks |
| GLOBprop_64 | Apparent molar heat capacity, J/K/mol | search_blocks |
| GLOBprop_15 | Molar enthalpy of solution, kJ/mol | search_blocks |
| GLOBprop_34 | Thermal conductivity, W/m/K | search_blocks |
| GLOBprop_44 | Relative permittivity at zero frequency | search_blocks |
| GLOBprop_13 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBprop_7 | Refractive index (Na D-line) | search_blocks |

#### References (14 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_2584 |  | search_blocks |
| GLOBlit_2652 |  | search_blocks |
| GLOBlit_2781 |  | search_blocks |
| GLOBlit_2844 |  | search_blocks |
| GLOBlit_5958 |  | search_blocks |
| GLOBlit_7713 |  | search_blocks |
| GLOBlit_10024 |  | search_blocks |
| GLOBlit_10109 |  | search_blocks |
| GLOBlit_10766 |  | search_blocks |
| GLOBlit_11018 |  | search_blocks |
| GLOBlit_11517 |  | search_blocks |
| GLOBlit_2686 |  | search_blocks |
| GLOBlit_2863 |  | search_blocks |
| GLOBlit_8444 |  | search_blocks |

#### Compounds (17 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_31 | dimethyl sulfoxide | search_blocks |
| GLOBcomp_1 | water | search_blocks |
| GLOBcomp_264 | 1,2-dichlorobenzene | search_blocks |
| GLOBcomp_419 | 1,3-dichlorobenzene | search_blocks |
| GLOBcomp_728 | 1,2,4-trichlorobenzene | search_blocks |
| GLOBcomp_408 | 2-chlorotoluene | search_blocks |
| GLOBcomp_664 | 3-chlorotoluene | search_blocks |
| GLOBcomp_473 | 4-chlorotoluene | search_blocks |
| GLOBcomp_616 | 2-nitrotoluene | search_blocks |
| GLOBcomp_807 | 3-nitrotoluene | search_blocks |
| GLOBcomp_39 | butanone | search_blocks |
| GLOBcomp_104 | pentan-3-one | search_blocks |
| GLOBcomp_75 | pentan-2-one | search_blocks |
| GLOBcomp_101 | 4-methylpentan-2-one | search_blocks |
| GLOBcomp_87 | cyclohexanone | search_blocks |
| GLOBcomp_309 | 1,2,4-trimethylbenzene | search_blocks |
| GLOBcomp_191 | 1,3,5-trimethylbenzene | search_blocks |

#### Measurements (16 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_147 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_7 | Speed of sound, m/s | search_blocks |
| GLOBmeas_141 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_140 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_57 | Apparent molar heat capacity, J/K/mol | search_blocks |
| GLOBmeas_144 | Molar enthalpy of solution, kJ/mol | search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_41 | Thermal conductivity, W/m/K | search_blocks |
| GLOBmeas_823 | Relative permittivity at zero frequency | search_blocks |
| GLOBmeas_36 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBmeas_163 | Refractive index (Na D-line) | search_blocks |
| GLOBmeas_205 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_495 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_55 | Excess molar volume, m3/mol | search_blocks |
| GLOBmeas_29 | Excess molar volume, m3/mol | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks |

#### Variables (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_2 | Mole fraction | search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |
| GLOBvar_3 | Pressure, kPa | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |

#### Constraints (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | search_blocks |
| GLOBconstr_3 | Mole fraction | search_blocks |
| GLOBconstr_2 | Temperature, K | search_blocks |

#### Solvents (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | search_blocks |
| GLOBsolvent_8 |  | search_blocks |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Properties | 10 |
| Unique References | 14 |
| Unique Compounds | 17 |
| Unique Measurements | 16 |
| Unique Phases | 1 |
| Unique Variables | 5 |
| Unique Constraints | 3 |
| Unique Solvents | 2 |
| Total DOIs | 14 |
| Unique parent blocks | 31 |
| Explicit block/subsystem targets | 31 |
| Subsystem targets | 0 |
| Target-matched data points | 1,580 |

---

## 3. DOI & Block References

**Unique DOIs:** 14  |  **Parent blocks:** 31  |  **Explicit targets:** 31  |  **Subsystems:** 0  |  **Target-matched datapoints:** 1,580

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.jct.2005.07.012 | 1 | 96 | binary | search_blocks |
| 10.1016/j.jct.2006.01.007 | 2 | 12 | binary | search_blocks |
| 10.1016/j.jct.2006.04.005 | 8 | 119 | binary | search_blocks |
| 10.1016/j.jct.2006.12.012 | 2 | 240 | binary | search_blocks |
| 10.1016/j.jct.2007.06.010 | 2 | 308 | binary | search_blocks |
| 10.1016/j.jct.2007.08.006 | 5 | 46 | binary | search_blocks |
| 10.1016/j.tca.2011.09.009 | 1 | 1 | binary | search_blocks |
| 10.1021/acs.jced.8b01048 | 1 | 9 | binary | search_blocks |
| 10.1021/je0497294 | 2 | 38 | binary | search_blocks |
| 10.1021/je301171y | 1 | 63 | binary | search_blocks |
| 10.1021/je400149j | 1 | 363 | binary | search_blocks |
| 10.1021/je7001013 | 2 | 145 | binary | search_blocks |
| 10.1021/je700645p | 1 | 70 | binary | search_blocks |
| 10.1021/je9001027 | 2 | 70 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.jct.2005.07.012 | PROPblock_8 | declared | 96 | binary | — | search_blocks |
| 10.1016/j.jct.2006.01.007 | PROPblock_3 | declared | 6 | binary | — | search_blocks |
| 10.1016/j.jct.2006.01.007 | PROPblock_4 | declared | 6 | binary | — | search_blocks |
| 10.1016/j.jct.2006.04.005 | PROPblock_29 | declared | 15 | binary | — | search_blocks |
| 10.1016/j.jct.2006.04.005 | PROPblock_33 | declared | 15 | binary | — | search_blocks |
| 10.1016/j.jct.2006.04.005 | PROPblock_37 | declared | 15 | binary | — | search_blocks |
| 10.1016/j.jct.2006.04.005 | PROPblock_41 | declared | 14 | binary | — | search_blocks |
| 10.1016/j.jct.2006.04.005 | PROPblock_45 | declared | 15 | binary | — | search_blocks |
| 10.1016/j.jct.2006.04.005 | PROPblock_49 | declared | 15 | binary | — | search_blocks |
| 10.1016/j.jct.2006.04.005 | PROPblock_53 | declared | 15 | binary | — | search_blocks |
| 10.1016/j.jct.2006.04.005 | PROPblock_57 | declared | 15 | binary | — | search_blocks |
| 10.1016/j.jct.2006.12.012 | PROPblock_3 | declared | 120 | binary | — | search_blocks |
| 10.1016/j.jct.2006.12.012 | PROPblock_4 | declared | 120 | binary | — | search_blocks |
| 10.1016/j.jct.2007.06.010 | PROPblock_3 | declared | 216 | binary | — | search_blocks |
| 10.1016/j.jct.2007.06.010 | PROPblock_4 | declared | 92 | binary | — | search_blocks |
| 10.1016/j.jct.2007.08.006 | PROPblock_14 | declared | 9 | binary | — | search_blocks |
| 10.1016/j.jct.2007.08.006 | PROPblock_16 | declared | 9 | binary | — | search_blocks |
| 10.1016/j.jct.2007.08.006 | PROPblock_18 | declared | 9 | binary | — | search_blocks |
| 10.1016/j.jct.2007.08.006 | PROPblock_20 | declared | 10 | binary | — | search_blocks |
| 10.1016/j.jct.2007.08.006 | PROPblock_22 | declared | 9 | binary | — | search_blocks |
| 10.1016/j.tca.2011.09.009 | PROPblock_1 | declared | 1 | binary | — | search_blocks |
| 10.1021/acs.jced.8b01048 | PROPblock_10 | declared | 9 | binary | — | search_blocks |
| 10.1021/je0497294 | PROPblock_20 | declared | 19 | binary | — | search_blocks |
| 10.1021/je0497294 | PROPblock_22 | declared | 19 | binary | — | search_blocks |
| 10.1021/je301171y | PROPblock_5 | declared | 63 | binary | — | search_blocks |
| 10.1021/je400149j | PROPblock_5 | declared | 363 | binary | — | search_blocks |
| 10.1021/je7001013 | PROPblock_10 | declared | 33 | binary | — | search_blocks |
| 10.1021/je7001013 | PROPblock_9 | declared | 112 | binary | — | search_blocks |
| 10.1021/je700645p | PROPblock_6 | declared | 70 | binary | — | search_blocks |
| 10.1021/je9001027 | PROPblock_3 | declared | 35 | binary | — | search_blocks |
| 10.1021/je9001027 | PROPblock_4 | declared | 35 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_property_ids` | limit=10, min_score=50, purpose=Find the global pr… | 254 | KEEP ←in 227 | 254 | 4.6 |
| 2 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 989 | DISCARD ←in 39 | 931 | 10.7 |
| 3 | 5 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 1,042 | DISCARD ←in 39 | 984 | 19.8 |
| 4 | 6 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 1,314 | KEEP ←in 10,618 | 1115 | 19.5 |
| 5 | 7 | `search_blocks` | compound=GLOBcomp_31, limit=20, property=GLOBprop_… | 1,139 | KEEP ←in 9,632 | 1016 | 19.5 |
| 6 | 1 | `L1_query` | context=User wants composition depend…, id_catalog… | 3,432 | — | — | 172.6 |
| | | **TOTAL (6 tools)** | | **8,170** | | **4,300** | **246.7** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 861 | 12,442 | 1,418 | 8.5 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,278 | 25,373 | 662 | 4.8 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,322 | 26,417 | 585 | 6.3 |
| 4 | L1-worker | claudeopus46 | 3,767 | 413 | 4,180 | 416 | 4.1 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,960 | 26,055 | 822 | 5.5 |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,678 | 26,773 | 659 | 5.3 |
| 7 | L1-worker | claudeopus46 | 3,767 | 566 | 4,333 | 1,520 | 10.3 |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,640 | 27,735 | 843 | 5.7 |
| 9 | L1-worker | claudeopus46 | 3,767 | 449 | 4,216 | 1,394 | 10.4 |
| 10 | L1-worker | claudeopus46 | 24,095 | 5,019 | 29,114 | 869 | 6.8 |
| 11 | L1-worker | claudeopus46 | 3,767 | 11,008 | 14,775 | 1,574 | 12.8 |
| 12 | L1-worker | claudeopus46 | 24,095 | 6,745 | 30,840 | 1,437 | 9.0 |
| 13 | L1-worker | claudeopus46 | 3,767 | 10,009 | 13,776 | 1,388 | 12.8 |
| 14 | L1-worker | claudeopus46 | 24,095 | 8,288 | 32,383 | 2,937 | 19.8 |
| 15 | L1-worker | claudeopus46 | 24,095 | 13,163 | 37,258 | 3,743 | 21.4 |
| 16 | L1-worker | claudeopus46 | 2,106 | 3,301 | 5,407 | 92 | 2.1 |
| 17 | L1-worker | claudeopus46 | 366 | 869 | 1,235 | 67 | 2.0 |
| 18 | L1-worker | claudeopus46 | 2,320 | 1,902 | 4,222 | 684 | 4.4 |
| 19 | L1-worker | claudeopus46 | 627 | 1,782 | 2,409 | 811 | 5.2 |
| 20 | L1-worker | claudeopus46 | 366 | 1,121 | 1,487 | 672 | 2.8 |
| 21 | L1-worker | claudeopus46 | 787 | 5,165 | 5,952 | 600 | 5.2 |
| 22 | L0-main | claudeopus46 | 11,581 | 8,050 | 19,631 | 2,456 | 13.6 |
| 23 | L0-main | claudeopus46 | 2,320 | 2,254 | 4,574 | 730 | 4.1 |
| 24 | L0-main | claudeopus46 | 366 | 1,205 | 1,571 | 691 | 3.0 |
| 25 | L0-main | claudeopus46 | 2,106 | 2,947 | 5,053 | 817 | 7.3 |
| 26 | L0-main | claudeopus46 | 366 | 1,366 | 1,732 | 778 | 3.7 |
| 27 | verdict | claudeopus46 | 972 | 4,247 | 5,219 | 980 | 8.2 |

