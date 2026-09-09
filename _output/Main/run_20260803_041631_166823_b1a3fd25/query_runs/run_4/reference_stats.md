# Reference Stats — query-agent

**Run started:** 2026-08-03 04:41:28
**Wall time (at last flush):** 972.9 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 8 | 41,695 | 249,772 | 42,000 | 291,467 | 36,433 | 214.7 | claudeopus46 |
| L1-worker | 70 | 435,869 | 1,557,124 | 118,610 | 1,992,993 | 28,471 | 739.0 | claudeopus46 |
| **TOTAL** | **78** | **477,564** | **1,806,896** | **160,610** | **2,284,460** | **29,287** | **953.7** | |

**Estimated tokens:** ~571,115 input + ~40,152 output = ~611,267 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `search_blocks` | 2 | 13 | 5 | 3 | 16 | 29 | 1,601 |
| `search_blocks` | 2 | 1 | 4 | 2 | 9 | 9 | 484 |
| `search_blocks` | 2 | 1 | 3 | 1 | 3 | 3 | 171 |
| `search_blocks` | 2 | 1 | 2 | 0 | 1 | 1 | 112 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 4 | 2 | 9 | 9 | 484 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 3 | 1 | 3 | 3 | 171 |
| `search_blocks` | 2 | 1 | 2 | 0 | 1 | 1 | 112 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 6 | 1 | 5 | 2 | 3 | 7 | 677 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_property_ids` | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **20** | **21** | **28** | **11** | **45** | **62** | **3,812** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### References (19 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_663 |  | search_blocks |
| GLOBlit_2584 |  | search_blocks |
| GLOBlit_2652 |  | search_blocks |
| GLOBlit_2781 |  | search_blocks |
| GLOBlit_2842 |  | search_blocks |
| GLOBlit_2844 |  | search_blocks |
| GLOBlit_5953 |  | search_blocks |
| GLOBlit_5958 |  | search_blocks |
| GLOBlit_7713 |  | search_blocks |
| GLOBlit_9547 |  | search_blocks |
| GLOBlit_10024 |  | search_blocks |
| GLOBlit_10109 |  | search_blocks |
| GLOBlit_10215 |  | search_blocks |
| GLOBlit_10766 |  | search_blocks |
| GLOBlit_11018 |  | search_blocks |
| GLOBlit_11517 |  | search_blocks |
| GLOBlit_7523 |  | search_blocks |
| GLOBlit_9178 |  | search_blocks |
| GLOBlit_10194 |  | search_blocks |

#### Compounds (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_31 | dimethyl sulfoxide | search_blocks |
| GLOBcomp_1 | water | search_blocks |
| GLOBcomp_2043 | cetylpyridinium chloride | search_blocks |
| GLOBcomp_4537 | sodium ((4-aminophenyl)sulfonyl)(thiazol-2-yl)amide | search_blocks |
| GLOBcomp_377 | dodecyltrimethylammonium bromide | search_blocks |
| GLOBcomp_1776 | sodium [dodecanoyl(methyl)amino]acetate | search_blocks |

#### Properties (15 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_14 | Boiling temperature at pressure P, K | search_blocks |
| GLOBprop_2 | Mole fraction | search_blocks |
| GLOBprop_1 | Mass density, kg/m3 | search_blocks |
| GLOBprop_8 | Speed of sound, m/s | search_blocks |
| GLOBprop_4 | Viscosity, Pa*s | search_blocks |
| GLOBprop_9 | Molar heat capacity at constant pressure, J/K/mol | search_blocks |
| GLOBprop_64 | Apparent molar heat capacity, J/K/mol | search_blocks |
| GLOBprop_15 | Molar enthalpy of solution, kJ/mol | search_blocks |
| GLOBprop_11 | Solid-liquid equilibrium temperature, K | search_blocks |
| GLOBprop_34 | Thermal conductivity, W/m/K | search_blocks |
| GLOBprop_44 | Relative permittivity at zero frequency | search_blocks |
| GLOBprop_13 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBprop_7 | Refractive index (Na D-line) | search_blocks |
| GLOBprop_18 | Electrical conductivity, S/m | search_blocks |
| GLOBprop_28 |  | resolve_property_ids |

#### Measurements (28 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_146 | Boiling temperature at pressure P, K | search_blocks |
| GLOBmeas_150 | Mole fraction | search_blocks |
| GLOBmeas_147 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_7 | Speed of sound, m/s | search_blocks |
| GLOBmeas_141 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_140 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_31 | Molar heat capacity at constant pressure, J/K/mol | search_blocks |
| GLOBmeas_811 | Speed of sound, m/s | search_blocks |
| GLOBmeas_6 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_57 | Apparent molar heat capacity, J/K/mol | search_blocks |
| GLOBmeas_4 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_15 | Speed of sound, m/s | search_blocks |
| GLOBmeas_144 | Molar enthalpy of solution, kJ/mol | search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_130 | Solid-liquid equilibrium temperature, K | search_blocks |
| GLOBmeas_41 | Thermal conductivity, W/m/K | search_blocks |
| GLOBmeas_823 | Relative permittivity at zero frequency | search_blocks |
| GLOBmeas_1503 | Solid-liquid equilibrium temperature, K | search_blocks |
| GLOBmeas_359 | Boiling temperature at pressure P, K | search_blocks |
| GLOBmeas_145 | Mole fraction | search_blocks |
| GLOBmeas_36 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBmeas_163 | Refractive index (Na D-line) | search_blocks |
| GLOBmeas_205 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_495 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_14 | Electrical conductivity, S/m | search_blocks |
| GLOBmeas_1258 | Electrical conductivity, S/m | search_blocks |
| GLOBmeas_49 | Electrical conductivity, S/m | search_blocks |

#### Phases (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_3 |  | search_blocks |
| GLOBphase_1 |  | search_blocks |

#### Variables (8 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_2 | Mole fraction | search_blocks |
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |
| GLOBvar_3 | Pressure, kPa | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |
| GLOBvar_7 | Solvent: Mass fraction | search_blocks |
| GLOBvar_16 | Solvent: Volume fraction | search_blocks |
| GLOBvar_9 | Amount concentration (molarity), mol/dm3 | search_blocks |

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
| Unique References | 19 |
| Unique Compounds | 6 |
| Unique Properties | 15 |
| Unique Measurements | 28 |
| Unique Phases | 2 |
| Unique Variables | 8 |
| Unique Constraints | 3 |
| Unique Solvents | 2 |
| Total DOIs | 19 |
| Unique parent blocks | 33 |
| Explicit block/subsystem targets | 36 |
| Subsystem targets | 3 |
| Target-matched data points | 3,812 |

---

## 3. DOI & Block References

**Unique DOIs:** 19  |  **Parent blocks:** 33  |  **Explicit targets:** 36  |  **Subsystems:** 3  |  **Target-matched datapoints:** 2,278

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2008.09.010 | 2 | 32 | binary | search_blocks |
| 10.1016/j.jct.2005.07.012 | 1 | 96 | binary | search_blocks |
| 10.1016/j.jct.2006.01.007 | 2 | 12 | binary | search_blocks |
| 10.1016/j.jct.2006.12.012 | 2 | 240 | binary | search_blocks |
| 10.1016/j.jct.2007.06.007 | 3 | 87 | binary | search_blocks |
| 10.1016/j.jct.2007.06.010 | 2 | 308 | binary | search_blocks |
| 10.1016/j.tca.2011.08.013 | 3 | 48 | binary | search_blocks |
| 10.1016/j.tca.2011.09.009 | 1 | 1 | binary | search_blocks |
| 10.1021/acs.jced.8b00326 | 2 | 192 | binary, ternary | search_blocks |
| 10.1021/acs.jced.8b01048 | 1 | 9 | binary | search_blocks |
| 10.1021/je100287g | 1 | 96 | ternary | search_blocks |
| 10.1021/je2002607 | 1 | 5 | binary | search_blocks |
| 10.1021/je301171y | 1 | 63 | binary | search_blocks |
| 10.1021/je400149j | 3 | 373 | binary | search_blocks |
| 10.1021/je4004788 | 4 | 389 | binary, ternary | search_blocks |
| 10.1021/je400531a | 2 | 42 | binary | search_blocks |
| 10.1021/je7001013 | 2 | 145 | binary | search_blocks |
| 10.1021/je700645p | 1 | 70 | binary | search_blocks |
| 10.1021/je9001027 | 2 | 70 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2008.09.010 | PROPblock_4 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.fluid.2008.09.010 | PROPblock_5 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.jct.2005.07.012 | PROPblock_8 | declared | 96 | binary | — | search_blocks |
| 10.1016/j.jct.2006.01.007 | PROPblock_3 | declared | 6 | binary | — | search_blocks |
| 10.1016/j.jct.2006.01.007 | PROPblock_4 | declared | 6 | binary | — | search_blocks |
| 10.1016/j.jct.2006.12.012 | PROPblock_3 | declared | 120 | binary | — | search_blocks |
| 10.1016/j.jct.2006.12.012 | PROPblock_4 | declared | 120 | binary | — | search_blocks |
| 10.1016/j.jct.2007.06.007 | PROPblock_4 | declared | 7 | binary | — | search_blocks |
| 10.1016/j.jct.2007.06.007 | PROPblock_5 | declared | 40 | binary | — | search_blocks |
| 10.1016/j.jct.2007.06.007 | PROPblock_6 | declared | 40 | binary | — | search_blocks |
| 10.1016/j.jct.2007.06.010 | PROPblock_3 | declared | 216 | binary | — | search_blocks |
| 10.1016/j.jct.2007.06.010 | PROPblock_4 | declared | 92 | binary | — | search_blocks |
| 10.1016/j.tca.2011.08.013 | PROPblock_10 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.tca.2011.08.013 | PROPblock_11 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.tca.2011.08.013 | PROPblock_12 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.tca.2011.09.009 | PROPblock_1 | declared | 1 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00326 | PROPblock_3 | declared | 176 | ternary | — | search_blocks |
| 10.1021/acs.jced.8b00326 | PROPblock_3 | BLKsubsys_1 | 16 | binary | — | search_blocks |
| 10.1021/acs.jced.8b01048 | PROPblock_10 | declared | 9 | binary | — | search_blocks |
| 10.1021/je100287g | PROPblock_2 | declared | 96 | ternary | — | search_blocks |
| 10.1021/je2002607 | PROPblock_1 | declared | 5 | binary | — | search_blocks |
| 10.1021/je301171y | PROPblock_5 | declared | 63 | binary | — | search_blocks |
| 10.1021/je400149j | PROPblock_5 | declared | 363 | binary | — | search_blocks |
| 10.1021/je400149j | PROPblock_6 | declared | 8 | binary | — | search_blocks |
| 10.1021/je400149j | PROPblock_7 | declared | 2 | binary | — | search_blocks |
| 10.1021/je4004788 | PROPblock_10 | declared | 172 | ternary | — | search_blocks |
| 10.1021/je4004788 | PROPblock_10 | BLKsubsys_1 | 6 | binary | — | search_blocks |
| 10.1021/je4004788 | PROPblock_7 | declared | 205 | ternary | — | search_blocks |
| 10.1021/je4004788 | PROPblock_7 | BLKsubsys_1 | 6 | binary | — | search_blocks |
| 10.1021/je400531a | PROPblock_16 | declared | 21 | binary | — | search_blocks |
| 10.1021/je400531a | PROPblock_17 | declared | 21 | binary | — | search_blocks |
| 10.1021/je7001013 | PROPblock_10 | declared | 33 | binary | — | search_blocks |
| 10.1021/je7001013 | PROPblock_9 | declared | 112 | binary | — | search_blocks |
| 10.1021/je700645p | PROPblock_6 | declared | 70 | binary | — | search_blocks |
| 10.1021/je9001027 | PROPblock_3 | declared | 35 | binary | — | search_blocks |
| 10.1021/je9001027 | PROPblock_4 | declared | 35 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (pre-compaction)

| # | Iter | Tool | Args | Raw (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 1,359 | KEEP | 1344 | 22.3 |
| 2 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 1,247 | KEEP | 1142 | 23.4 |
| 3 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 1,349 | KEEP | 1303 | 22.6 |
| 4 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 916 | KEEP | 884 | 19.4 |
| 5 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 788 | DISCARD | 730 | 16.6 |
| 6 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 693 | DISCARD | 635 | 7.7 |
| 7 | 1 | `L1_query` | context=This is for Fe electrodeposit…, id_catalog… | 1,114 | — | — | 223.4 |
| 8 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 1,138 | KEEP | 1138 | 20.6 |
| 9 | 2 | `L1_query` | context=Binary system: water + DMSO. …, id_catalog… | 270 | — | — | 93.6 |
| 10 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 1,433 | KEEP | 1433 | 17.2 |
| 11 | 2 | `L1_query` | context=Binary system: water + DMSO. …, id_catalog… | 21,444 | — | — | 56.7 |
| 12 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 911 | KEEP | 879 | 17.7 |
| 13 | 3 | `L1_query` | context=Binary system: water + DMSO. …, id_catalog… | 8,486 | — | — | 51.6 |
| 14 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 603 | DISCARD | 545 | 13.3 |
| 15 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 1,221 | KEEP | 1159 | 28.9 |
| 16 | 3 | `L1_query` | context=Binary system: water + DMSO. …, id_catalog… | 270 | — | — | 97.4 |
| 17 | 2 | `resolve_property_ids` | limit=10, min_score=50, purpose=Find the global pr… | 251 | KEEP | 251 | 5.0 |
| 18 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 892 | DISCARD | 834 | 17.7 |
| 19 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 654 | DISCARD | 596 | 15.8 |
| 20 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 781 | DISCARD | 723 | 16.1 |
| 21 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 719 | DISCARD | 661 | 18.0 |
| 22 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 825 | DISCARD | 767 | 9.9 |
| 23 | 3 | `L1_query` | context=Binary system: water + DMSO. …, id_catalog… | 1,792 | — | — | 252.9 |
| | | **TOTAL (23 tools)** | | **49,156** | | **15,024** | **1067.8** |

---

## 5. Compaction Events

| # | Trigger | Outcome | Before (chars) | After (chars) | Saved (chars) | Saved (%) |
|--:|---------|---------|---------------:|--------------:|--------------:|----------:|
| 1 | interval=3 | skipped_by_agent | 6,151 | 6,151 | 0 | 0.0% |

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 9,605 | 1,180 | 10,785 | 1,844 | 9.0 |
| 2 | L1-worker | claudeopus46 | 20,643 | 1,675 | 22,318 | 1,588 | 11.6 |
| 3 | L1-worker | claudeopus46 | 2,065 | 19,086 | 21,151 | 1,638 | 13.7 |
| 4 | L1-worker | claudeopus46 | 20,643 | 3,565 | 24,208 | 2,109 | 9.0 |
| 5 | L1-worker | claudeopus46 | 2,065 | 6,364 | 8,429 | 1,467 | 15.8 |
| 6 | L1-worker | claudeopus46 | 2,065 | 7,471 | 9,536 | 1,565 | 14.1 |
| 7 | L1-worker | claudeopus46 | 2,065 | 2,779 | 4,844 | 1,338 | 11.6 |
| 8 | L1-worker | claudeopus46 | 2,065 | 468 | 2,533 | 1,331 | 9.0 |
| 9 | L1-worker | claudeopus46 | 2,065 | 476 | 2,541 | 1,070 | 7.3 |
| 10 | L1-worker | claudeopus46 | 20,643 | 6,384 | 27,027 | 5,680 | 31.0 |
| 11 | L1-worker | claudeopus46 | 1,356 | 3,387 | 4,743 | 829 | 5.3 |
| 12 | L1-worker | claudeopus46 | 536 | 3,267 | 3,803 | 1,437 | 7.7 |
| 13 | L1-worker | claudeopus46 | 1,323 | 13,903 | 15,226 | 3,838 | 18.7 |
| 14 | L1-worker | claudeopus46 | 298 | 4,560 | 4,858 | 3,161 | 13.7 |
| 15 | L1-worker | claudeopus46 | 1,160 | 18,856 | 20,016 | 3,196 | 15.2 |
| 16 | L1-worker | claudeopus46 | 747 | 82,270 | 83,017 | 1,015 | 10.8 |
| 17 | L0-main | claudeopus46 | 9,605 | 2,836 | 12,441 | 14,559 | 64.6 |
| 18 | L1-worker | claudeopus46 | 20,643 | 1,106 | 21,749 | 890 | 6.6 |
| 19 | L1-worker | claudeopus46 | 2,065 | 6,435 | 8,500 | 1,464 | 12.6 |
| 20 | L1-worker | claudeopus46 | 20,643 | 2,778 | 23,421 | 3,298 | 17.6 |
| 21 | L1-worker | claudeopus46 | 1,356 | 2,336 | 3,692 | 754 | 4.2 |
| 22 | L1-worker | claudeopus46 | 536 | 2,216 | 2,752 | 854 | 5.7 |
| 23 | L1-worker | claudeopus46 | 298 | 1,136 | 1,434 | 742 | 3.2 |
| 24 | L1-worker | claudeopus46 | 298 | 1,210 | 1,508 | 841 | 6.2 |
| 25 | L1-worker | claudeopus46 | 1,323 | 5,028 | 6,351 | 3,010 | 12.6 |
| 26 | L1-worker | claudeopus46 | 298 | 3,732 | 4,030 | 2,289 | 10.2 |
| 27 | L1-worker | claudeopus46 | 747 | 48,310 | 49,057 | 654 | 5.7 |
| 28 | L1-worker | claudeopus46 | 1,160 | 9,008 | 10,168 | 2,354 | 11.4 |
| 29 | L1-worker | claudeopus46 | 747 | 48,375 | 49,122 | 625 | 6.8 |
| 30 | L1-worker | claudeopus46 | 20,643 | 45,744 | 66,387 | 798 | 6.2 |
| 31 | L1-worker | claudeopus46 | 2,065 | 7,547 | 9,612 | 1,671 | 16.8 |
| 32 | L1-worker | claudeopus46 | 20,643 | 47,677 | 68,320 | 1,910 | 12.0 |
| 33 | L1-worker | claudeopus46 | 1,356 | 1,841 | 3,197 | 925 | 5.4 |
| 34 | L1-worker | claudeopus46 | 536 | 1,721 | 2,257 | 823 | 5.4 |
| 35 | L1-worker | claudeopus46 | 1,323 | 4,860 | 6,183 | 1,746 | 8.2 |
| 36 | L1-worker | claudeopus46 | 298 | 2,468 | 2,766 | 1,421 | 5.9 |
| 37 | L1-worker | claudeopus46 | 747 | 25,092 | 25,839 | 526 | 6.5 |
| 38 | L0-main | claudeopus46 | 9,605 | 70,457 | 80,062 | 2,960 | 15.0 |
| 39 | L1-worker | claudeopus46 | 20,643 | 67,270 | 87,913 | 816 | 7.1 |
| 40 | L1-worker | claudeopus46 | 2,065 | 2,871 | 4,936 | 1,105 | 9.6 |
| 41 | L1-worker | claudeopus46 | 20,643 | 68,691 | 89,334 | 1,331 | 9.9 |
| 42 | L1-worker | claudeopus46 | 1,323 | 3,980 | 5,303 | 684 | 4.6 |
| 43 | L1-worker | claudeopus46 | 536 | 1,340 | 1,876 | 865 | 5.3 |
| 44 | L1-worker | claudeopus46 | 298 | 1,406 | 1,704 | 557 | 3.6 |
| 45 | L1-worker | claudeopus46 | 1,356 | 1,460 | 2,816 | 726 | 9.6 |
| 46 | L1-worker | claudeopus46 | 747 | 11,252 | 11,999 | 630 | 6.9 |
| 47 | L1-worker | claudeopus46 | 20,643 | 75,841 | 96,484 | 843 | 9.7 |
| 48 | L1-worker | claudeopus46 | 2,065 | 520 | 2,585 | 1,678 | 12.8 |
| 49 | L1-worker | claudeopus46 | 20,643 | 76,966 | 97,609 | 1,120 | 7.8 |
| 50 | L1-worker | claudeopus46 | 2,065 | 9,589 | 11,654 | 1,961 | 16.6 |
| 51 | L1-worker | claudeopus46 | 20,643 | 78,756 | 99,399 | 2,443 | 13.1 |
| 52 | L1-worker | claudeopus46 | 1,356 | 2,161 | 3,517 | 743 | 4.8 |
| 53 | L1-worker | claudeopus46 | 536 | 2,041 | 2,577 | 1,067 | 5.3 |
| 54 | L1-worker | claudeopus46 | 1,323 | 6,047 | 7,370 | 1,889 | 9.5 |
| 55 | L1-worker | claudeopus46 | 298 | 2,611 | 2,909 | 1,426 | 8.0 |
| 56 | L1-worker | claudeopus46 | 747 | 32,147 | 32,894 | 553 | 6.5 |
| 57 | L1-worker | claudeopus46 | 20,643 | 103,286 | 123,929 | 1,324 | 9.3 |
| 58 | L1-worker | claudeopus46 | 20,643 | 105,338 | 125,981 | 14,920 | 59.0 |
| 59 | L1-worker | claudeopus46 | 2,065 | 406 | 2,471 | 490 | 4.9 |
| 60 | L1-worker | claudeopus46 | 2,065 | 498 | 2,563 | 1,348 | 9.4 |
| 61 | L1-worker | claudeopus46 | 20,643 | 106,565 | 127,208 | 10,308 | 56.0 |
| 62 | L1-worker | claudeopus46 | 2,065 | 494 | 2,559 | 1,330 | 8.5 |
| 63 | L1-worker | claudeopus46 | 2,065 | 553 | 2,618 | 1,617 | 10.1 |
| 64 | L1-worker | claudeopus46 | 20,610 | 109,551 | 130,161 | 577 | 7.6 |
| 65 | L1-worker | claudeopus46 | 20,643 | 108,798 | 129,441 | 3,151 | 17.4 |
| 66 | L1-worker | claudeopus46 | 2,065 | 453 | 2,518 | 985 | 7.0 |
| 67 | L1-worker | claudeopus46 | 2,065 | 449 | 2,514 | 960 | 9.1 |
| 68 | L1-worker | claudeopus46 | 20,643 | 111,080 | 131,723 | 760 | 8.7 |
| 69 | L1-worker | claudeopus46 | 1,356 | 891 | 2,247 | 403 | 3.1 |
| 70 | L1-worker | claudeopus46 | 536 | 771 | 1,307 | 490 | 3.2 |
| 71 | L1-worker | claudeopus46 | 1,323 | 9,288 | 10,611 | 92 | 4.2 |
| 72 | L1-worker | claudeopus46 | 298 | 814 | 1,112 | 67 | 2.3 |
| 73 | L1-worker | claudeopus46 | 747 | 9,809 | 10,556 | 494 | 4.8 |
| 74 | L0-main | claudeopus46 | 9,605 | 110,457 | 120,062 | 7,012 | 46.8 |
| 75 | L0-main | claudeopus46 | 1,356 | 6,456 | 7,812 | 1,421 | 9.6 |
| 76 | L0-main | claudeopus46 | 298 | 1,803 | 2,101 | 1,409 | 8.6 |
| 77 | L0-main | claudeopus46 | 1,323 | 48,989 | 50,312 | 6,926 | 36.1 |
| 78 | L0-main | claudeopus46 | 298 | 7,594 | 7,892 | 5,869 | 25.0 |

