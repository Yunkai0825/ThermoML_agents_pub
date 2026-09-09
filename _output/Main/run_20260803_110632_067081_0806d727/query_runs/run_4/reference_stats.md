# Reference Stats — query-agent

**Run started:** 2026-08-03 11:18:17
**Wall time (at last flush):** 368.8 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 6 | 22,485 | 111,419 | 18,400 | 133,904 | 22,317 | 103.9 | claudeopus46 |
| L1-worker | 16 | 118,065 | 173,562 | 50,405 | 291,627 | 18,226 | 269.3 | claudeopus46 |
| **TOTAL** | **22** | **140,550** | **284,981** | **68,805** | **425,531** | **19,342** | **373.2** | |

**Estimated tokens:** ~106,382 input + ~17,201 output = ~123,583 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_property_ids` | 0 | 3 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 4 | 2 | 13 | 13 | 574 |
| `search_blocks` | 2 | 1 | 3 | 2 | 5 | 5 | 193 |
| `search_blocks` | 2 | 2 | 1 | 3 | 2 | 2 | 8 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **8** | **7** | **8** | **7** | **20** | **20** | **775** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_18 |  | resolve_compound_ids, search_blocks |

#### Properties (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_42 |  | resolve_property_ids, search_blocks |
| GLOBprop_44 |  | resolve_property_ids, search_blocks |
| GLOBprop_33 |  | resolve_property_ids |
| GLOBprop_1 | Mass density, kg/m3 | search_blocks |
| GLOBprop_4 | Viscosity, Pa*s | search_blocks |

#### References (15 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_1540 |  | search_blocks |
| GLOBlit_2584 |  | search_blocks |
| GLOBlit_2736 |  | search_blocks |
| GLOBlit_2834 |  | search_blocks |
| GLOBlit_3614 |  | search_blocks |
| GLOBlit_4166 |  | search_blocks |
| GLOBlit_4174 |  | search_blocks |
| GLOBlit_4340 |  | search_blocks |
| GLOBlit_8676 |  | search_blocks |
| GLOBlit_8888 |  | search_blocks |
| GLOBlit_9342 |  | search_blocks |
| GLOBlit_9855 |  | search_blocks |
| GLOBlit_11030 |  | search_blocks |
| GLOBlit_9900 |  | search_blocks |
| GLOBlit_11207 |  | search_blocks |

#### Measurements (9 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_147 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_167 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_6 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_140 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_4 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_567 | Relative permittivity at various frequencies | search_blocks |
| GLOBmeas_53 | Relative permittivity at zero frequency | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks |

#### Variables (4 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_5 | Mass fraction | search_blocks |
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_2 | Mole fraction | search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |

#### Constraints (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | search_blocks |
| GLOBconstr_2 | Temperature, K | search_blocks |
| GLOBconstr_4 | Frequency, MHz | search_blocks |

#### Solvents (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_4 |  | search_blocks |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 2 |
| Unique Properties | 5 |
| Unique References | 15 |
| Unique Measurements | 9 |
| Unique Phases | 1 |
| Unique Variables | 4 |
| Unique Constraints | 3 |
| Unique Solvents | 1 |
| Total DOIs | 15 |
| Unique parent blocks | 20 |
| Explicit block/subsystem targets | 20 |
| Subsystem targets | 0 |
| Target-matched data points | 775 |

---

## 3. DOI & Block References

**Unique DOIs:** 15  |  **Parent blocks:** 20  |  **Explicit targets:** 20  |  **Subsystems:** 0  |  **Target-matched datapoints:** 775

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2014.08.026 | 2 | 9 | binary | search_blocks |
| 10.1016/j.jct.2005.07.012 | 1 | 128 | binary | search_blocks |
| 10.1016/j.jct.2006.08.007 | 1 | 9 | binary | search_blocks |
| 10.1016/j.jct.2007.05.015 | 1 | 40 | binary | search_blocks |
| 10.1016/j.jct.2012.04.007 | 1 | 55 | binary | search_blocks |
| 10.1016/j.jct.2014.05.003 | 2 | 6 | binary | search_blocks |
| 10.1016/j.jct.2014.05.013 | 1 | 18 | binary | search_blocks |
| 10.1016/j.jct.2015.03.012 | 1 | 6 | binary | search_blocks |
| 10.1021/je050209y | 2 | 22 | binary | search_blocks |
| 10.1021/je0601098 | 1 | 14 | binary | search_blocks |
| 10.1021/je1008813 | 2 | 32 | binary | search_blocks |
| 10.1021/je300358u | 1 | 60 | binary | search_blocks |
| 10.1021/je300608v | 1 | 60 | binary | search_blocks |
| 10.1021/je700671t | 2 | 308 | binary | search_blocks |
| 10.1021/je800330d | 1 | 8 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2014.08.026 | PROPblock_5 | declared | 4 | binary | — | search_blocks |
| 10.1016/j.fluid.2014.08.026 | PROPblock_6 | declared | 5 | binary | — | search_blocks |
| 10.1016/j.jct.2005.07.012 | PROPblock_9 | declared | 128 | binary | — | search_blocks |
| 10.1016/j.jct.2006.08.007 | PROPblock_2 | declared | 9 | binary | — | search_blocks |
| 10.1016/j.jct.2007.05.015 | PROPblock_18 | declared | 40 | binary | — | search_blocks |
| 10.1016/j.jct.2012.04.007 | PROPblock_3 | declared | 55 | binary | — | search_blocks |
| 10.1016/j.jct.2014.05.003 | PROPblock_1 | declared | 3 | binary | — | search_blocks |
| 10.1016/j.jct.2014.05.003 | PROPblock_2 | declared | 3 | binary | — | search_blocks |
| 10.1016/j.jct.2014.05.013 | PROPblock_19 | declared | 18 | binary | — | search_blocks |
| 10.1016/j.jct.2015.03.012 | PROPblock_2 | declared | 6 | binary | — | search_blocks |
| 10.1021/je050209y | PROPblock_10 | declared | 11 | binary | — | search_blocks |
| 10.1021/je050209y | PROPblock_9 | declared | 11 | binary | — | search_blocks |
| 10.1021/je0601098 | PROPblock_30 | declared | 14 | binary | — | search_blocks |
| 10.1021/je1008813 | PROPblock_3 | declared | 16 | binary | — | search_blocks |
| 10.1021/je1008813 | PROPblock_4 | declared | 16 | binary | — | search_blocks |
| 10.1021/je300358u | PROPblock_3 | declared | 60 | binary | — | search_blocks |
| 10.1021/je300608v | PROPblock_3 | declared | 60 | binary | — | search_blocks |
| 10.1021/je700671t | PROPblock_3 | declared | 98 | binary | — | search_blocks |
| 10.1021/je700671t | PROPblock_4 | declared | 210 | binary | — | search_blocks |
| 10.1021/je800330d | PROPblock_3 | declared | 8 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (pre-compaction)

| # | Iter | Tool | Args | Raw (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve global comp… | 335 | KEEP | 335 | 5.0 |
| 2 | 2 | `resolve_property_ids` | limit=5, min_score=50, purpose=Resolve property ID… | 446 | KEEP | 446 | 6.5 |
| 3 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_18'], limit=50, … | 1,287 | KEEP | 1182 | 25.4 |
| 4 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_18'], limit=50, … | 1,263 | KEEP | 1263 | 23.2 |
| 5 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_18'], limit=50, … | 1,088 | KEEP | 1028 | 20.3 |
| 6 | 1 | `L1_query` | context=User is designing Fe electrod…, id_catalog… | 270 | — | — | 278.9 |
| | | **TOTAL (6 tools)** | | **4,689** | | **4,254** | **359.3** |

---

## 5. Compaction Events

| # | Trigger | Outcome | Before (chars) | After (chars) | Saved (chars) | Saved (%) |
|--:|---------|---------|---------------:|--------------:|--------------:|----------:|
| 1 | interval=3 | skipped_by_agent | 7,970 | 7,970 | 0 | 0.0% |

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 9,605 | 979 | 10,584 | 1,563 | 8.4 |
| 2 | L1-worker | claudeopus46 | 20,643 | 1,350 | 21,993 | 1,070 | 6.6 |
| 3 | L1-worker | claudeopus46 | 20,643 | 3,148 | 23,791 | 14,686 | 52.3 |
| 4 | L1-worker | claudeopus46 | 2,065 | 490 | 2,555 | 562 | 4.8 |
| 5 | L1-worker | claudeopus46 | 2,065 | 669 | 2,734 | 1,031 | 6.3 |
| 6 | L1-worker | claudeopus46 | 20,643 | 3,963 | 24,606 | 9,984 | 50.8 |
| 7 | L1-worker | claudeopus46 | 2,065 | 8,667 | 10,732 | 1,588 | 16.4 |
| 8 | L1-worker | claudeopus46 | 2,065 | 7,520 | 9,585 | 1,633 | 13.6 |
| 9 | L1-worker | claudeopus46 | 2,065 | 3,890 | 5,955 | 1,496 | 11.3 |
| 10 | L1-worker | claudeopus46 | 20,610 | 9,265 | 29,875 | 471 | 5.2 |
| 11 | L1-worker | claudeopus46 | 20,643 | 8,512 | 29,155 | 3,728 | 25.7 |
| 12 | L1-worker | claudeopus46 | 536 | 3,739 | 4,275 | 981 | 7.1 |
| 13 | L1-worker | claudeopus46 | 1,356 | 3,859 | 5,215 | 1,093 | 7.2 |
| 14 | L1-worker | claudeopus46 | 298 | 1,475 | 1,773 | 1,081 | 6.8 |
| 15 | L1-worker | claudeopus46 | 1,323 | 12,254 | 13,577 | 5,620 | 24.8 |
| 16 | L1-worker | claudeopus46 | 298 | 6,342 | 6,640 | 4,607 | 19.9 |
| 17 | L1-worker | claudeopus46 | 747 | 98,419 | 99,166 | 774 | 10.5 |
| 18 | L0-main | claudeopus46 | 9,605 | 89,968 | 99,573 | 6,287 | 42.8 |
| 19 | L0-main | claudeopus46 | 1,356 | 5,876 | 7,232 | 1,458 | 9.7 |
| 20 | L0-main | claudeopus46 | 298 | 1,840 | 2,138 | 1,446 | 4.8 |
| 21 | L0-main | claudeopus46 | 1,323 | 8,081 | 9,404 | 4,007 | 22.3 |
| 22 | L0-main | claudeopus46 | 298 | 4,675 | 4,973 | 3,639 | 15.9 |

