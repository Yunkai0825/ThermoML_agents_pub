# Reference Stats — query-agent

**Run started:** 2026-08-03 11:10:40
**Wall time (at last flush):** 988.6 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 10 | 60,905 | 160,782 | 23,348 | 221,687 | 22,168 | 142.0 | claudeopus46 |
| L1-worker | 65 | 542,700 | 730,215 | 174,485 | 1,272,915 | 19,583 | 876.5 | claudeopus46 |
| **TOTAL** | **75** | **603,605** | **890,997** | **197,833** | **1,494,602** | **19,928** | **1018.5** | |

**Estimated tokens:** ~373,650 input + ~49,458 output = ~423,108 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_property_ids` | 0 | 3 | 0 | 0 | 0 | 0 | 0 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_property_ids` | 0 | 3 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 2 | 4 | 2 | 11 | 12 | 1,157 |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 28 |
| `search_blocks` | 2 | 2 | 4 | 2 | 11 | 12 | 1,157 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 4 | 2 | 11 | 11 | 1,081 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 76 |
| `resolve_property_ids` | 0 | 3 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **14** | **16** | **16** | **8** | **35** | **37** | **3,499** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_58 |  | resolve_compound_ids, search_blocks |

#### Properties (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_42 |  | resolve_property_ids |
| GLOBprop_44 |  | resolve_property_ids, search_blocks |
| GLOBprop_33 |  | resolve_property_ids |
| GLOBprop_1 | Mass density, kg/m3 | search_blocks |
| GLOBprop_4 | Viscosity, Pa*s | search_blocks |

#### References (12 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_2738 |  | search_blocks |
| GLOBlit_2979 |  | search_blocks |
| GLOBlit_4204 |  | search_blocks |
| GLOBlit_4631 |  | search_blocks |
| GLOBlit_4951 |  | search_blocks |
| GLOBlit_5201 |  | search_blocks |
| GLOBlit_5254 |  | search_blocks |
| GLOBlit_5288 |  | search_blocks |
| GLOBlit_6107 |  | search_blocks |
| GLOBlit_6811 |  | search_blocks |
| GLOBlit_9758 |  | search_blocks |
| GLOBlit_8736 |  | search_blocks |

#### Measurements (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_153 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_11 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_46 | Relative permittivity at zero frequency | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks |

#### Solvents (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | search_blocks |

#### Variables (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |
| GLOBvar_2 | Mole fraction | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |
| GLOBvar_3 | Pressure, kPa | search_blocks |

#### Constraints (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | search_blocks |
| GLOBconstr_2 | Temperature, K | search_blocks |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 2 |
| Unique Properties | 5 |
| Unique References | 12 |
| Unique Measurements | 5 |
| Unique Phases | 1 |
| Unique Solvents | 1 |
| Unique Variables | 5 |
| Unique Constraints | 2 |
| Total DOIs | 12 |
| Unique parent blocks | 13 |
| Explicit block/subsystem targets | 13 |
| Subsystem targets | 0 |
| Target-matched data points | 3,499 |

---

## 3. DOI & Block References

**Unique DOIs:** 12  |  **Parent blocks:** 13  |  **Explicit targets:** 13  |  **Subsystems:** 0  |  **Target-matched datapoints:** 1,185

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.jct.2006.08.009 | 1 | 99 | binary | search_blocks |
| 10.1016/j.jct.2008.07.005 | 1 | 96 | binary | search_blocks |
| 10.1016/j.jct.2014.06.031 | 1 | 85 | binary | search_blocks |
| 10.1016/j.jct.2016.02.026 | 1 | 7 | binary | search_blocks |
| 10.1016/j.jct.2017.01.011 | 1 | 44 | binary | search_blocks |
| 10.1016/j.jct.2018.02.022 | 2 | 212 | binary | search_blocks |
| 10.1016/j.jct.2018.05.016 | 1 | 16 | binary | search_blocks |
| 10.1016/j.jct.2018.07.015 | 1 | 20 | binary | search_blocks |
| 10.1016/j.tca.2013.07.012 | 1 | 296 | binary | search_blocks |
| 10.1021/acs.jced.5b01080 | 1 | 175 | binary | search_blocks |
| 10.1021/je050353j | 1 | 28 | binary | search_blocks |
| 10.1021/je201184b | 1 | 107 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.jct.2006.08.009 | PROPblock_6 | declared | 99 | binary | — | search_blocks |
| 10.1016/j.jct.2008.07.005 | PROPblock_8 | declared | 96 | binary | — | search_blocks |
| 10.1016/j.jct.2014.06.031 | PROPblock_5 | declared | 85 | binary | — | search_blocks |
| 10.1016/j.jct.2016.02.026 | PROPblock_17 | declared | 7 | binary | — | search_blocks |
| 10.1016/j.jct.2017.01.011 | PROPblock_3 | declared | 44 | binary | — | search_blocks |
| 10.1016/j.jct.2018.02.022 | PROPblock_31 | declared | 136 | binary | — | search_blocks |
| 10.1016/j.jct.2018.02.022 | PROPblock_33 | declared | 76 | binary | — | search_blocks |
| 10.1016/j.jct.2018.05.016 | PROPblock_9 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.jct.2018.07.015 | PROPblock_1 | declared | 20 | binary | — | search_blocks |
| 10.1016/j.tca.2013.07.012 | PROPblock_3 | declared | 296 | binary | — | search_blocks |
| 10.1021/acs.jced.5b01080 | PROPblock_15 | declared | 175 | binary | — | search_blocks |
| 10.1021/je050353j | PROPblock_4 | declared | 28 | binary | — | search_blocks |
| 10.1021/je201184b | PROPblock_6 | declared | 107 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (pre-compaction)

| # | Iter | Tool | Args | Raw (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve global comp… | 329 | KEEP | 329 | 6.4 |
| 2 | 2 | `resolve_property_ids` | limit=10, min_score=50, purpose=Find property ID f… | 417 | KEEP | 417 | 6.7 |
| 3 | 1 | `L1_query` | context=Looking for solvent property …, id_catalog… | 414 | — | — | 218.3 |
| 4 | 1 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve global comp… | 320 | KEEP | 320 | 5.5 |
| 5 | 2 | `L1_query` | context=Need to identify these compou…, id_catalog… | 1,634 | — | — | 28.0 |
| 6 | 3 | `resolve_property_ids` | limit=10, min_score=50, purpose=Find the GLOBprop … | 386 | KEEP | 386 | 6.2 |
| 7 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 1,197 | KEEP | 1107 | 26.9 |
| 8 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 1,045 | KEEP | 1015 | 12.2 |
| 9 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 1,231 | KEEP | 1141 | 23.0 |
| 10 | 3 | `L1_query` | context=Binary mixture search for wat…, id_catalog… | 420 | — | — | 354.5 |
| 11 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 1,188 | KEEP | 1158 | 24.3 |
| 12 | 4 | `L1_query` | context=Looking for density data in w…, id_catalog… | 270 | — | — | 133.9 |
| 13 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 1,215 | KEEP | 1185 | 21.1 |
| 14 | 5 | `L1_query` | context=Binary water+glycerol mixture…, id_catalog… | 9,460 | — | — | 62.4 |
| 15 | 3 | `resolve_property_ids` | limit=10, min_score=50, purpose=Find GLOBprop_N ID… | 451 | KEEP | 451 | 6.8 |
| 16 | 5 | `L1_query` | context=Binary water+glycerol mixture…, id_catalog… | 1,984 | — | — | 59.4 |
| | | **TOTAL (16 tools)** | | **21,961** | | **7,509** | **995.6** |

---

## 5. Compaction Events

| # | Trigger | Outcome | Before (chars) | After (chars) | Saved (chars) | Saved (%) |
|--:|---------|---------|---------------:|--------------:|--------------:|----------:|
| 1 | interval=3 | skipped_by_agent | 5,201 | 5,201 | 0 | 0.0% |
| 2 | interval=3 | skipped_by_agent | 2,687 | 2,687 | 0 | 0.0% |

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 9,605 | 965 | 10,570 | 1,768 | 10.5 |
| 2 | L1-worker | claudeopus46 | 20,643 | 1,259 | 21,902 | 1,026 | 7.0 |
| 3 | L1-worker | claudeopus46 | 20,643 | 3,013 | 23,656 | 13,821 | 54.1 |
| 4 | L1-worker | claudeopus46 | 2,065 | 476 | 2,541 | 537 | 5.4 |
| 5 | L1-worker | claudeopus46 | 2,065 | 680 | 2,745 | 1,062 | 6.6 |
| 6 | L1-worker | claudeopus46 | 20,643 | 3,754 | 24,397 | 9,705 | 45.0 |
| 7 | L1-worker | claudeopus46 | 20,643 | 14,080 | 34,723 | 3,671 | 18.0 |
| 8 | L1-worker | claudeopus46 | 1,356 | 3,486 | 4,842 | 835 | 4.9 |
| 9 | L1-worker | claudeopus46 | 536 | 3,366 | 3,902 | 796 | 5.4 |
| 10 | L1-worker | claudeopus46 | 1,323 | 6,968 | 8,291 | 8,059 | 29.8 |
| 11 | L1-worker | claudeopus46 | 298 | 8,781 | 9,079 | 6,678 | 25.7 |
| 12 | L1-worker | claudeopus46 | 1,160 | 16,917 | 18,077 | 6,638 | 24.8 |
| 13 | L0-main | claudeopus46 | 9,605 | 1,914 | 11,519 | 964 | 7.1 |
| 14 | L1-worker | claudeopus46 | 20,643 | 894 | 21,537 | 587 | 5.3 |
| 15 | L1-worker | claudeopus46 | 2,065 | 501 | 2,566 | 555 | 5.3 |
| 16 | L1-worker | claudeopus46 | 20,643 | 1,685 | 22,328 | 713 | 5.6 |
| 17 | L1-worker | claudeopus46 | 1,323 | 2,282 | 3,605 | 234 | 3.2 |
| 18 | L1-worker | claudeopus46 | 536 | 573 | 1,109 | 248 | 3.5 |
| 19 | L1-worker | claudeopus46 | 1,356 | 693 | 2,049 | 418 | 3.8 |
| 20 | L1-worker | claudeopus46 | 298 | 956 | 1,254 | 154 | 3.0 |
| 21 | L1-worker | claudeopus46 | 747 | 2,932 | 3,679 | 365 | 4.1 |
| 22 | L0-main | claudeopus46 | 9,605 | 5,863 | 15,468 | 2,013 | 16.3 |
| 23 | L1-worker | claudeopus46 | 20,643 | 3,430 | 24,073 | 1,241 | 7.9 |
| 24 | L1-worker | claudeopus46 | 20,643 | 5,399 | 26,042 | 14,392 | 57.4 |
| 25 | L1-worker | claudeopus46 | 20,643 | 6,613 | 27,256 | 13,870 | 54.6 |
| 26 | L1-worker | claudeopus46 | 2,065 | 675 | 2,740 | 966 | 6.0 |
| 27 | L1-worker | claudeopus46 | 2,065 | 8,485 | 10,550 | 1,744 | 14.8 |
| 28 | L1-worker | claudeopus46 | 20,610 | 8,267 | 28,877 | 475 | 4.8 |
| 29 | L1-worker | claudeopus46 | 20,643 | 7,514 | 28,157 | 8,016 | 39.8 |
| 30 | L1-worker | claudeopus46 | 2,065 | 3,039 | 5,104 | 1,435 | 11.7 |
| 31 | L1-worker | claudeopus46 | 2,065 | 8,488 | 10,553 | 1,672 | 14.2 |
| 32 | L1-worker | claudeopus46 | 20,643 | 10,603 | 31,246 | 7,249 | 41.0 |
| 33 | L1-worker | claudeopus46 | 20,643 | 18,601 | 39,244 | 3,875 | 17.3 |
| 34 | L1-worker | claudeopus46 | 1,356 | 4,006 | 5,362 | 1,632 | 8.2 |
| 35 | L1-worker | claudeopus46 | 536 | 3,886 | 4,422 | 1,141 | 8.2 |
| 36 | L1-worker | claudeopus46 | 298 | 2,014 | 2,312 | 1,620 | 5.5 |
| 37 | L1-worker | claudeopus46 | 1,323 | 13,784 | 15,107 | 5,015 | 21.9 |
| 38 | L1-worker | claudeopus46 | 298 | 5,737 | 6,035 | 4,165 | 19.8 |
| 39 | L1-worker | claudeopus46 | 1,160 | 20,083 | 21,243 | 4,167 | 19.6 |
| 40 | L0-main | claudeopus46 | 9,605 | 6,915 | 16,520 | 1,350 | 10.3 |
| 41 | L1-worker | claudeopus46 | 20,643 | 2,966 | 23,609 | 854 | 6.4 |
| 42 | L1-worker | claudeopus46 | 20,643 | 4,441 | 25,084 | 14,106 | 49.4 |
| 43 | L1-worker | claudeopus46 | 2,065 | 7,924 | 9,989 | 1,752 | 14.8 |
| 44 | L1-worker | claudeopus46 | 20,643 | 5,602 | 26,245 | 3,913 | 22.3 |
| 45 | L1-worker | claudeopus46 | 1,356 | 2,481 | 3,837 | 882 | 4.7 |
| 46 | L1-worker | claudeopus46 | 536 | 2,361 | 2,897 | 725 | 5.2 |
| 47 | L1-worker | claudeopus46 | 1,323 | 5,636 | 6,959 | 2,715 | 12.0 |
| 48 | L1-worker | claudeopus46 | 298 | 3,437 | 3,735 | 2,093 | 9.3 |
| 49 | L1-worker | claudeopus46 | 747 | 43,567 | 44,314 | 898 | 9.4 |
| 50 | L0-main | claudeopus46 | 9,605 | 47,141 | 56,746 | 2,057 | 12.0 |
| 51 | L1-worker | claudeopus46 | 20,643 | 42,229 | 62,872 | 1,080 | 10.1 |
| 52 | L1-worker | claudeopus46 | 2,065 | 2,919 | 4,984 | 1,695 | 12.3 |
| 53 | L1-worker | claudeopus46 | 20,643 | 43,942 | 64,585 | 2,277 | 14.4 |
| 54 | L1-worker | claudeopus46 | 1,323 | 4,842 | 6,165 | 618 | 4.3 |
| 55 | L1-worker | claudeopus46 | 1,356 | 1,849 | 3,205 | 868 | 4.9 |
| 56 | L1-worker | claudeopus46 | 536 | 1,729 | 2,265 | 797 | 5.3 |
| 57 | L1-worker | claudeopus46 | 298 | 1,340 | 1,638 | 491 | 3.5 |
| 58 | L1-worker | claudeopus46 | 747 | 13,039 | 13,786 | 819 | 8.5 |
| 59 | L1-worker | claudeopus46 | 20,643 | 51,845 | 72,488 | 665 | 6.9 |
| 60 | L1-worker | claudeopus46 | 20,643 | 53,131 | 73,774 | 1,065 | 6.4 |
| 61 | L1-worker | claudeopus46 | 20,643 | 53,826 | 74,469 | 586 | 3.5 |
| 62 | L1-worker | claudeopus46 | 2,065 | 650 | 2,715 | 1,030 | 6.6 |
| 63 | L1-worker | claudeopus46 | 20,610 | 54,569 | 75,179 | 526 | 4.4 |
| 64 | L1-worker | claudeopus46 | 20,643 | 53,816 | 74,459 | 2,097 | 14.2 |
| 65 | L1-worker | claudeopus46 | 20,643 | 56,488 | 77,131 | 1,025 | 4.6 |
| 66 | L1-worker | claudeopus46 | 1,323 | 4,235 | 5,558 | 92 | 2.2 |
| 67 | L1-worker | claudeopus46 | 1,356 | 933 | 2,289 | 474 | 4.0 |
| 68 | L1-worker | claudeopus46 | 536 | 813 | 1,349 | 570 | 4.1 |
| 69 | L1-worker | claudeopus46 | 298 | 814 | 1,112 | 67 | 2.1 |
| 70 | L1-worker | claudeopus46 | 747 | 4,871 | 5,618 | 928 | 7.5 |
| 71 | L0-main | claudeopus46 | 9,605 | 60,309 | 69,914 | 4,727 | 33.0 |
| 72 | L0-main | claudeopus46 | 1,356 | 4,858 | 6,214 | 1,219 | 7.4 |
| 73 | L0-main | claudeopus46 | 298 | 1,601 | 1,899 | 1,207 | 4.1 |
| 74 | L0-main | claudeopus46 | 1,323 | 26,194 | 27,517 | 4,354 | 25.8 |
| 75 | L0-main | claudeopus46 | 298 | 5,022 | 5,320 | 3,689 | 15.5 |

