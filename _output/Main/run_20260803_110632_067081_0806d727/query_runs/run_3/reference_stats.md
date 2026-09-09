# Reference Stats — query-agent

**Run started:** 2026-08-03 11:10:40
**Wall time (at last flush):** 457.0 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 6 | 22,485 | 94,167 | 37,086 | 116,652 | 19,442 | 190.0 | claudeopus46 |
| L1-worker | 16 | 118,065 | 151,070 | 51,060 | 269,135 | 16,820 | 273.0 | claudeopus46 |
| **TOTAL** | **22** | **140,550** | **245,237** | **88,146** | **385,787** | **17,535** | **463.0** | |

**Estimated tokens:** ~96,446 input + ~22,036 output = ~118,482 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 5 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_property_ids` | 0 | 3 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 4 | 2 | 9 | 9 | 484 |
| `search_blocks` | 2 | 1 | 3 | 1 | 3 | 3 | 171 |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 363 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **11** | **6** | **9** | **4** | **13** | **13** | **1,018** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_241 |  | resolve_compound_ids |
| GLOBcomp_31 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_1294 |  | resolve_compound_ids |
| GLOBcomp_2408 |  | resolve_compound_ids |

#### Properties (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_42 |  | resolve_property_ids |
| GLOBprop_44 |  | resolve_property_ids, search_blocks |
| GLOBprop_33 |  | resolve_property_ids |
| GLOBprop_1 | Mass density, kg/m3 | search_blocks |
| GLOBprop_4 | Viscosity, Pa*s | search_blocks |

#### References (10 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_2584 |  | search_blocks |
| GLOBlit_2652 |  | search_blocks |
| GLOBlit_2781 |  | search_blocks |
| GLOBlit_2842 |  | search_blocks |
| GLOBlit_2844 |  | search_blocks |
| GLOBlit_5953 |  | search_blocks |
| GLOBlit_7713 |  | search_blocks |
| GLOBlit_11018 |  | search_blocks |
| GLOBlit_11517 |  | search_blocks |
| GLOBlit_10109 |  | search_blocks |

#### Measurements (10 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_147 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_141 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_6 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_495 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_140 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_4 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_205 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_823 | Relative permittivity at zero frequency | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks |

#### Variables (4 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_2 | Mole fraction | search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |

#### Constraints (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | search_blocks |
| GLOBconstr_3 | Mole fraction | search_blocks |

#### Solvents (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | search_blocks |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 5 |
| Unique Properties | 5 |
| Unique References | 10 |
| Unique Measurements | 10 |
| Unique Phases | 1 |
| Unique Variables | 4 |
| Unique Constraints | 2 |
| Unique Solvents | 1 |
| Total DOIs | 10 |
| Unique parent blocks | 13 |
| Explicit block/subsystem targets | 13 |
| Subsystem targets | 0 |
| Target-matched data points | 1,018 |

---

## 3. DOI & Block References

**Unique DOIs:** 10  |  **Parent blocks:** 13  |  **Explicit targets:** 13  |  **Subsystems:** 0  |  **Target-matched datapoints:** 1,018

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.jct.2005.07.012 | 1 | 96 | binary | search_blocks |
| 10.1016/j.jct.2006.01.007 | 1 | 6 | binary | search_blocks |
| 10.1016/j.jct.2006.12.012 | 2 | 240 | binary | search_blocks |
| 10.1016/j.jct.2007.06.007 | 1 | 40 | binary | search_blocks |
| 10.1016/j.jct.2007.06.010 | 1 | 92 | binary | search_blocks |
| 10.1016/j.tca.2011.08.013 | 2 | 32 | binary | search_blocks |
| 10.1021/acs.jced.8b01048 | 1 | 9 | binary | search_blocks |
| 10.1021/je400149j | 1 | 363 | binary | search_blocks |
| 10.1021/je700645p | 1 | 70 | binary | search_blocks |
| 10.1021/je9001027 | 2 | 70 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.jct.2005.07.012 | PROPblock_8 | declared | 96 | binary | — | search_blocks |
| 10.1016/j.jct.2006.01.007 | PROPblock_4 | declared | 6 | binary | — | search_blocks |
| 10.1016/j.jct.2006.12.012 | PROPblock_3 | declared | 120 | binary | — | search_blocks |
| 10.1016/j.jct.2006.12.012 | PROPblock_4 | declared | 120 | binary | — | search_blocks |
| 10.1016/j.jct.2007.06.007 | PROPblock_6 | declared | 40 | binary | — | search_blocks |
| 10.1016/j.jct.2007.06.010 | PROPblock_4 | declared | 92 | binary | — | search_blocks |
| 10.1016/j.tca.2011.08.013 | PROPblock_10 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.tca.2011.08.013 | PROPblock_12 | declared | 16 | binary | — | search_blocks |
| 10.1021/acs.jced.8b01048 | PROPblock_10 | declared | 9 | binary | — | search_blocks |
| 10.1021/je400149j | PROPblock_5 | declared | 363 | binary | — | search_blocks |
| 10.1021/je700645p | PROPblock_6 | declared | 70 | binary | — | search_blocks |
| 10.1021/je9001027 | PROPblock_3 | declared | 35 | binary | — | search_blocks |
| 10.1021/je9001027 | PROPblock_4 | declared | 35 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (pre-compaction)

| # | Iter | Tool | Args | Raw (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve compound ID… | 300 | KEEP | 300 | 6.4 |
| 2 | 2 | `resolve_property_ids` | limit=5, min_score=50, purpose=Resolve property ID… | 456 | KEEP | 456 | 8.8 |
| 3 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 1,227 | KEEP | 1122 | 22.5 |
| 4 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 1,444 | KEEP | 1413 | 15.8 |
| 5 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 1,240 | KEEP | 1208 | 27.4 |
| 6 | 1 | `L1_query` | context=Looking for solvent property …, id_catalog… | 270 | — | — | 279.4 |
| | | **TOTAL (6 tools)** | | **4,937** | | **4,499** | **360.3** |

---

## 5. Compaction Events

| # | Trigger | Outcome | Before (chars) | After (chars) | Saved (chars) | Saved (%) |
|--:|---------|---------|---------------:|--------------:|--------------:|----------:|
| 1 | interval=3 | skipped_by_agent | 8,035 | 8,035 | 0 | 0.0% |

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 9,605 | 978 | 10,583 | 17,317 | 80.2 |
| 2 | L1-worker | claudeopus46 | 20,643 | 1,235 | 21,878 | 994 | 6.2 |
| 3 | L1-worker | claudeopus46 | 20,643 | 2,957 | 23,600 | 15,376 | 59.6 |
| 4 | L1-worker | claudeopus46 | 2,065 | 749 | 2,814 | 586 | 5.3 |
| 5 | L1-worker | claudeopus46 | 2,065 | 669 | 2,734 | 1,085 | 8.6 |
| 6 | L1-worker | claudeopus46 | 20,643 | 3,748 | 24,391 | 11,254 | 49.3 |
| 7 | L1-worker | claudeopus46 | 2,065 | 6,411 | 8,476 | 1,433 | 13.1 |
| 8 | L1-worker | claudeopus46 | 2,065 | 7,521 | 9,586 | 1,768 | 15.3 |
| 9 | L1-worker | claudeopus46 | 2,065 | 3,849 | 5,914 | 1,658 | 16.6 |
| 10 | L1-worker | claudeopus46 | 20,610 | 9,330 | 29,940 | 381 | 5.2 |
| 11 | L1-worker | claudeopus46 | 20,643 | 8,577 | 29,220 | 4,915 | 32.6 |
| 12 | L1-worker | claudeopus46 | 1,356 | 3,508 | 4,864 | 1,001 | 6.6 |
| 13 | L1-worker | claudeopus46 | 536 | 3,388 | 3,924 | 1,030 | 7.6 |
| 14 | L1-worker | claudeopus46 | 298 | 1,383 | 1,681 | 989 | 3.9 |
| 15 | L1-worker | claudeopus46 | 1,323 | 12,101 | 13,424 | 4,220 | 18.3 |
| 16 | L1-worker | claudeopus46 | 298 | 4,942 | 5,240 | 3,384 | 14.7 |
| 17 | L1-worker | claudeopus46 | 747 | 80,702 | 81,449 | 986 | 10.1 |
| 18 | L0-main | claudeopus46 | 9,605 | 72,328 | 81,933 | 9,173 | 60.1 |
| 19 | L0-main | claudeopus46 | 1,356 | 6,036 | 7,392 | 1,351 | 7.7 |
| 20 | L0-main | claudeopus46 | 298 | 1,733 | 2,031 | 1,339 | 5.6 |
| 21 | L0-main | claudeopus46 | 1,323 | 8,125 | 9,448 | 4,299 | 22.3 |
| 22 | L0-main | claudeopus46 | 298 | 4,967 | 5,265 | 3,607 | 14.1 |

