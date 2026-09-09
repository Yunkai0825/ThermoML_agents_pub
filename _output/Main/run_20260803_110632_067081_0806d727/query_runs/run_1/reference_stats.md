# Reference Stats — query-agent

**Run started:** 2026-08-03 11:10:40
**Wall time (at last flush):** 838.3 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 9 | 51,300 | 320,420 | 39,297 | 371,720 | 41,302 | 201.4 | claudeopus46 |
| L1-worker | 64 | 460,609 | 1,409,333 | 123,282 | 1,869,942 | 29,217 | 684.9 | claudeopus46 |
| **TOTAL** | **73** | **511,909** | **1,729,753** | **162,579** | **2,241,662** | **30,707** | **886.3** | |

**Estimated tokens:** ~560,415 input + ~40,644 output = ~601,059 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 5 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_property_ids` | 0 | 3 | 0 | 0 | 0 | 0 | 0 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 4 | 3 | 16 | 16 | 908 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 3 | 2 | 7 | 7 | 302 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_property_ids` | 0 | 3 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 35 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 4 | 3 | 16 | 16 | 908 |
| `search_system_registry` | 2 | 1 | 4 | 3 | 16 | 16 | 908 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **17** | **11** | **17** | **12** | **56** | **56** | **3,061** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks, search_system_registry |
| GLOBcomp_151 |  | resolve_compound_ids |
| GLOBcomp_234 |  | resolve_compound_ids |
| GLOBcomp_770 |  | resolve_compound_ids |
| GLOBcomp_863 |  | resolve_compound_ids |
| GLOBcomp_24 |  | resolve_compound_ids, search_blocks, search_system_registry |

#### Properties (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_42 |  | resolve_property_ids |
| GLOBprop_44 |  | resolve_property_ids, search_blocks |
| GLOBprop_33 |  | resolve_property_ids |
| GLOBprop_1 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBprop_4 | Viscosity, Pa*s | search_blocks |

#### References (18 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_1223 |  | search_blocks, search_system_registry |
| GLOBlit_2268 |  | search_blocks, search_system_registry |
| GLOBlit_2656 |  | search_blocks, search_system_registry |
| GLOBlit_2831 |  | search_blocks, search_system_registry |
| GLOBlit_5201 |  | search_blocks, search_system_registry |
| GLOBlit_5254 |  | search_blocks, search_system_registry |
| GLOBlit_5274 |  | search_blocks, search_system_registry |
| GLOBlit_6630 |  | search_blocks, search_system_registry |
| GLOBlit_6686 |  | search_blocks, search_system_registry |
| GLOBlit_6951 |  | search_blocks, search_system_registry |
| GLOBlit_7228 |  | search_blocks, search_system_registry |
| GLOBlit_7440 |  | search_blocks, search_system_registry |
| GLOBlit_8038 |  | search_blocks, search_system_registry |
| GLOBlit_8106 |  | search_blocks, search_system_registry |
| GLOBlit_10102 |  | search_blocks, search_system_registry |
| GLOBlit_11506 |  | search_blocks, search_system_registry |
| GLOBlit_11186 |  | search_blocks |
| GLOBlit_8736 |  | search_blocks |

#### Measurements (11 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_143 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_212 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_184 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_4 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_11 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_8 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_227 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_142 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_165 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_46 | Relative permittivity at zero frequency | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks, search_system_registry |

#### Variables (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | search_blocks, search_system_registry |
| GLOBvar_2 | Mole fraction | search_blocks, search_system_registry |
| GLOBvar_5 | Mass fraction | search_blocks, search_system_registry |
| GLOBvar_4 | Molality, mol/kg | search_blocks, search_system_registry |
| GLOBvar_3 | Pressure, kPa | search_blocks |

#### Constraints (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | search_blocks, search_system_registry |
| GLOBconstr_5 | Mass fraction | search_blocks, search_system_registry |
| GLOBconstr_2 | Temperature, K | search_blocks, search_system_registry |

#### Solvents (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_12 |  | search_blocks, search_system_registry |
| GLOBsolvent_1 |  | search_blocks, search_system_registry |

#### Block_Types (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | search_system_registry |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 6 |
| Unique Properties | 5 |
| Unique References | 18 |
| Unique Measurements | 11 |
| Unique Phases | 1 |
| Unique Variables | 5 |
| Unique Constraints | 3 |
| Unique Solvents | 2 |
| Unique Block_Types | 1 |
| Total DOIs | 18 |
| Unique parent blocks | 24 |
| Explicit block/subsystem targets | 24 |
| Subsystem targets | 0 |
| Target-matched data points | 3,061 |

---

## 3. DOI & Block References

**Unique DOIs:** 18  |  **Parent blocks:** 24  |  **Explicit targets:** 24  |  **Subsystems:** 0  |  **Target-matched datapoints:** 1,245

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2013.01.025 | 1 | 85 | binary | search_blocks, search_system_registry |
| 10.1016/j.fluid.2018.11.035 | 1 | 6 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2006.01.011 | 2 | 20 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2007.05.010 | 1 | 10 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2018.02.022 | 2 | 308 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2018.05.016 | 1 | 12 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2018.06.021 | 1 | 15 | binary | search_blocks, search_system_registry |
| 10.1021/acs.jced.5b00498 | 1 | 70 | binary | search_blocks, search_system_registry |
| 10.1021/acs.jced.5b00662 | 1 | 30 | binary | search_blocks, search_system_registry |
| 10.1021/acs.jced.6b00526 | 2 | 166 | binary | search_blocks, search_system_registry |
| 10.1021/acs.jced.7b00501 | 1 | 32 | binary | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00058 | 1 | 20 | binary | search_blocks, search_system_registry |
| 10.1021/je020140j | 2 | 154 | binary | search_blocks, search_system_registry |
| 10.1021/je025610o | 2 | 60 | binary | search_blocks, search_system_registry |
| 10.1021/je050353j | 1 | 35 | binary | search_blocks |
| 10.1021/je4001203 | 1 | 138 | binary | search_blocks, search_system_registry |
| 10.1021/je800271e | 1 | 52 | binary | search_blocks |
| 10.1021/je9000697 | 2 | 32 | binary | search_blocks, search_system_registry |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2013.01.025 | PROPblock_2 | declared | 85 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2018.11.035 | PROPblock_2 | declared | 6 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2006.01.011 | PROPblock_12 | declared | 10 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2006.01.011 | PROPblock_13 | declared | 10 | binary | — | search_blocks |
| 10.1016/j.jct.2007.05.010 | PROPblock_10 | declared | 10 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2018.02.022 | PROPblock_22 | declared | 224 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2018.02.022 | PROPblock_24 | declared | 84 | binary | — | search_blocks |
| 10.1016/j.jct.2018.05.016 | PROPblock_7 | declared | 12 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2018.06.021 | PROPblock_10 | declared | 15 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.5b00498 | PROPblock_1 | declared | 70 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.5b00662 | PROPblock_55 | declared | 30 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.6b00526 | PROPblock_16 | declared | 133 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.6b00526 | PROPblock_18 | declared | 33 | binary | — | search_blocks |
| 10.1021/acs.jced.7b00501 | PROPblock_9 | declared | 32 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00058 | PROPblock_9 | declared | 20 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je020140j | PROPblock_4 | declared | 77 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je020140j | PROPblock_5 | declared | 77 | binary | — | search_blocks |
| 10.1021/je025610o | PROPblock_5 | declared | 30 | binary | — | search_blocks |
| 10.1021/je025610o | PROPblock_6 | declared | 30 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je050353j | PROPblock_3 | declared | 35 | binary | — | search_blocks |
| 10.1021/je4001203 | PROPblock_1 | declared | 138 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je800271e | PROPblock_4 | declared | 52 | binary | — | search_blocks |
| 10.1021/je9000697 | PROPblock_1 | declared | 16 | binary | — | search_blocks |
| 10.1021/je9000697 | PROPblock_2 | declared | 16 | binary | 2 | search_blocks, search_system_registry |

</details>

---

## 4. Tool Results (pre-compaction)

| # | Iter | Tool | Args | Raw (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve compound ID… | 488 | KEEP | 488 | 8.3 |
| 2 | 2 | `resolve_property_ids` | limit=10, min_score=50, purpose=Resolve property I… | 493 | KEEP | 493 | 6.9 |
| 3 | 1 | `L1_query` | context=Looking for viscosity, dielec…, id_catalog… | 415 | — | — | 212.0 |
| 4 | 1 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve global comp… | 254 | KEEP | 254 | 4.4 |
| 5 | 2 | `L1_query` | context=Need compound IDs before sear…, id_catalog… | 1,383 | — | — | 24.2 |
| 6 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_24'], limit=50, … | 1,190 | KEEP | 1100 | 24.1 |
| 7 | 3 | `L1_query` | context=Looking for density data in w…, id_catalog… | 270 | — | — | 83.4 |
| 8 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_24'], limit=50, … | 1,370 | KEEP | 1263 | 23.2 |
| 9 | 3 | `L1_query` | context=Looking for viscosity data in…, id_catalog… | 270 | — | — | 82.5 |
| 10 | 2 | `resolve_property_ids` | limit=10, min_score=40, purpose=Find the global pr… | 548 | KEEP | 548 | 7.6 |
| 11 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_24'], limit=50, … | 1,166 | KEEP | 1136 | 22.4 |
| 12 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_24'], limit=50, … | 906 | DISCARD | 848 | 19.1 |
| 13 | 3 | `L1_query` | context=Looking for dielectric consta…, id_catalog… | 10,590 | — | — | 116.9 |
| 14 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_24'], limit=50, … | 1,105 | KEEP | 1090 | 22.7 |
| 15 | 3 | `search_system_registry` | compound=['GLOBcomp_1', 'GLOBcomp_24'], limit=50, … | 1,246 | KEEP | 1020 | 10.7 |
| 16 | 4 | `L1_query` | context=Previous search found 16 tota…, id_catalog… | 270 | — | — | 131.3 |
| | | **TOTAL (16 tools)** | | **21,964** | | **8,240** | **799.7** |

---

## 5. Compaction Events

| # | Trigger | Outcome | Before (chars) | After (chars) | Saved (chars) | Saved (%) |
|--:|---------|---------|---------------:|--------------:|--------------:|----------:|
| 1 | interval=3 | skipped_by_agent | 5,507 | 5,507 | 0 | 0.0% |
| 2 | interval=3 | skipped_by_agent | 5,250 | 5,250 | 0 | 0.0% |

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 9,605 | 979 | 10,584 | 1,417 | 8.0 |
| 2 | L1-worker | claudeopus46 | 20,643 | 1,254 | 21,897 | 1,000 | 5.9 |
| 3 | L1-worker | claudeopus46 | 20,643 | 2,982 | 23,625 | 15,932 | 62.6 |
| 4 | L1-worker | claudeopus46 | 2,065 | 645 | 2,710 | 1,004 | 7.0 |
| 5 | L1-worker | claudeopus46 | 2,065 | 646 | 2,711 | 1,083 | 6.5 |
| 6 | L1-worker | claudeopus46 | 20,643 | 3,990 | 24,633 | 11,966 | 53.1 |
| 7 | L1-worker | claudeopus46 | 20,643 | 16,577 | 37,220 | 3,706 | 15.8 |
| 8 | L1-worker | claudeopus46 | 1,356 | 3,837 | 5,193 | 907 | 5.8 |
| 9 | L1-worker | claudeopus46 | 536 | 3,717 | 4,253 | 903 | 6.4 |
| 10 | L1-worker | claudeopus46 | 298 | 1,289 | 1,587 | 867 | 3.9 |
| 11 | L1-worker | claudeopus46 | 1,323 | 7,506 | 8,829 | 5,979 | 22.5 |
| 12 | L1-worker | claudeopus46 | 298 | 6,701 | 6,999 | 4,906 | 17.8 |
| 13 | L1-worker | claudeopus46 | 1,160 | 14,925 | 16,085 | 4,789 | 18.1 |
| 14 | L0-main | claudeopus46 | 9,605 | 1,906 | 11,511 | 881 | 6.6 |
| 15 | L1-worker | claudeopus46 | 20,643 | 840 | 21,483 | 627 | 5.2 |
| 16 | L1-worker | claudeopus46 | 2,065 | 514 | 2,579 | 464 | 4.2 |
| 17 | L1-worker | claudeopus46 | 20,643 | 1,569 | 22,212 | 420 | 4.4 |
| 18 | L1-worker | claudeopus46 | 1,323 | 2,038 | 3,361 | 234 | 2.6 |
| 19 | L1-worker | claudeopus46 | 1,356 | 551 | 1,907 | 192 | 2.9 |
| 20 | L1-worker | claudeopus46 | 536 | 431 | 967 | 372 | 3.2 |
| 21 | L1-worker | claudeopus46 | 298 | 956 | 1,254 | 154 | 2.5 |
| 22 | L1-worker | claudeopus46 | 747 | 2,491 | 3,238 | 375 | 4.1 |
| 23 | L0-main | claudeopus46 | 9,605 | 5,346 | 14,951 | 3,729 | 17.2 |
| 24 | L1-worker | claudeopus46 | 20,643 | 2,882 | 23,525 | 745 | 7.4 |
| 25 | L1-worker | claudeopus46 | 2,065 | 11,226 | 13,291 | 1,615 | 14.7 |
| 26 | L1-worker | claudeopus46 | 20,643 | 4,546 | 25,189 | 3,662 | 20.7 |
| 27 | L1-worker | claudeopus46 | 1,356 | 2,466 | 3,822 | 978 | 5.2 |
| 28 | L1-worker | claudeopus46 | 536 | 2,346 | 2,882 | 820 | 6.3 |
| 29 | L1-worker | claudeopus46 | 298 | 1,360 | 1,658 | 966 | 4.0 |
| 30 | L1-worker | claudeopus46 | 1,323 | 5,454 | 6,777 | 2,622 | 11.9 |
| 31 | L1-worker | claudeopus46 | 298 | 3,344 | 3,642 | 2,240 | 9.8 |
| 32 | L1-worker | claudeopus46 | 747 | 43,286 | 44,033 | 845 | 8.6 |
| 33 | L1-worker | claudeopus46 | 20,643 | 42,293 | 62,936 | 1,091 | 7.3 |
| 34 | L1-worker | claudeopus46 | 2,065 | 10,481 | 12,546 | 1,648 | 13.1 |
| 35 | L1-worker | claudeopus46 | 20,643 | 44,208 | 64,851 | 3,398 | 20.1 |
| 36 | L1-worker | claudeopus46 | 536 | 2,934 | 3,470 | 1,256 | 6.5 |
| 37 | L1-worker | claudeopus46 | 1,356 | 3,054 | 4,410 | 1,347 | 7.3 |
| 38 | L1-worker | claudeopus46 | 298 | 1,729 | 2,027 | 1,335 | 4.4 |
| 39 | L1-worker | claudeopus46 | 1,323 | 6,352 | 7,675 | 3,233 | 12.5 |
| 40 | L1-worker | claudeopus46 | 298 | 3,955 | 4,253 | 2,512 | 11.6 |
| 41 | L1-worker | claudeopus46 | 747 | 50,551 | 51,298 | 559 | 6.5 |
| 42 | L1-worker | claudeopus46 | 20,643 | 88,121 | 108,764 | 705 | 5.3 |
| 43 | L1-worker | claudeopus46 | 20,643 | 89,447 | 110,090 | 1,085 | 6.5 |
| 44 | L1-worker | claudeopus46 | 2,065 | 679 | 2,744 | 1,194 | 7.5 |
| 45 | L1-worker | claudeopus46 | 20,643 | 89,919 | 110,562 | 3,168 | 15.5 |
| 46 | L1-worker | claudeopus46 | 2,065 | 3,380 | 5,445 | 1,562 | 13.8 |
| 47 | L1-worker | claudeopus46 | 2,065 | 570 | 2,635 | 1,345 | 12.7 |
| 48 | L1-worker | claudeopus46 | 20,610 | 93,514 | 114,124 | 500 | 5.9 |
| 49 | L1-worker | claudeopus46 | 20,643 | 92,761 | 113,404 | 2,279 | 14.4 |
| 50 | L1-worker | claudeopus46 | 1,356 | 2,126 | 3,482 | 895 | 5.3 |
| 51 | L1-worker | claudeopus46 | 1,323 | 7,835 | 9,158 | 1,004 | 7.3 |
| 52 | L1-worker | claudeopus46 | 536 | 2,006 | 2,542 | 915 | 7.7 |
| 53 | L1-worker | claudeopus46 | 298 | 1,271 | 1,569 | 902 | 3.9 |
| 54 | L1-worker | claudeopus46 | 298 | 1,726 | 2,024 | 822 | 4.2 |
| 55 | L1-worker | claudeopus46 | 747 | 16,926 | 17,673 | 594 | 7.3 |
| 56 | L0-main | claudeopus46 | 9,605 | 103,321 | 112,926 | 3,462 | 25.7 |
| 57 | L1-worker | claudeopus46 | 20,643 | 99,136 | 119,779 | 964 | 9.0 |
| 58 | L1-worker | claudeopus46 | 2,065 | 11,219 | 13,284 | 1,521 | 13.3 |
| 59 | L1-worker | claudeopus46 | 20,643 | 100,767 | 121,410 | 861 | 9.1 |
| 60 | L1-worker | claudeopus46 | 20,643 | 102,249 | 122,892 | 678 | 4.4 |
| 61 | L1-worker | claudeopus46 | 2,065 | 3,087 | 5,152 | 1,319 | 10.2 |
| 62 | L1-worker | claudeopus46 | 20,610 | 104,201 | 124,811 | 377 | 5.5 |
| 63 | L1-worker | claudeopus46 | 20,643 | 103,448 | 124,091 | 4,763 | 32.5 |
| 64 | L1-worker | claudeopus46 | 1,356 | 2,291 | 3,647 | 983 | 7.9 |
| 65 | L1-worker | claudeopus46 | 536 | 2,171 | 2,707 | 1,274 | 8.9 |
| 66 | L1-worker | claudeopus46 | 1,323 | 7,315 | 8,638 | 3,297 | 15.6 |
| 67 | L1-worker | claudeopus46 | 298 | 4,019 | 4,317 | 2,738 | 11.0 |
| 68 | L1-worker | claudeopus46 | 747 | 63,223 | 63,970 | 785 | 7.8 |
| 69 | L0-main | claudeopus46 | 9,605 | 161,993 | 171,598 | 6,915 | 49.4 |
| 70 | L0-main | claudeopus46 | 1,356 | 6,504 | 7,860 | 1,764 | 9.8 |
| 71 | L0-main | claudeopus46 | 298 | 2,146 | 2,444 | 1,714 | 5.8 |
| 72 | L0-main | claudeopus46 | 1,323 | 27,117 | 28,440 | 10,440 | 44.6 |
| 73 | L0-main | claudeopus46 | 298 | 11,108 | 11,406 | 8,975 | 34.3 |

