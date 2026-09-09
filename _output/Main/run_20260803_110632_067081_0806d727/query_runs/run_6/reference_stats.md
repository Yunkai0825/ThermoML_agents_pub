# Reference Stats — query-agent

**Run started:** 2026-08-03 11:24:38
**Wall time (at last flush):** 1,094.1 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 9 | 51,300 | 380,176 | 32,031 | 431,476 | 47,941 | 178.8 | claudeopus46 |
| L1-worker | 66 | 480,186 | 2,046,459 | 199,829 | 2,526,645 | 38,282 | 974.9 | claudeopus46 |
| **TOTAL** | **75** | **531,486** | **2,426,635** | **231,860** | **2,958,121** | **39,441** | **1153.7** | |

**Estimated tokens:** ~739,530 input + ~57,965 output = ~797,495 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_property_ids` | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 6 | 3 | 14 | 14 | 534 |
| `search_system_registry` | 2 | 1 | 6 | 3 | 14 | 14 | 534 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 6 | 5 | 27 | 29 | 2,895 |
| `search_system_registry` | 2 | 1 | 6 | 5 | 27 | 29 | 2,895 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_property_ids` | 0 | 3 | 0 | 0 | 0 | 0 | 0 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_property_ids` | 0 | 3 | 0 | 0 | 0 | 0 | 0 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **10** | **11** | **24** | **16** | **82** | **86** | **6,858** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks, search_system_registry |
| GLOBcomp_2 |  | resolve_compound_ids, search_blocks, search_system_registry |

#### Properties (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_4 |  | resolve_property_ids, search_blocks, search_system_registry |
| GLOBprop_1 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBprop_42 |  | resolve_property_ids |
| GLOBprop_44 |  | resolve_property_ids |
| GLOBprop_33 |  | resolve_property_ids |

#### References (28 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_1742 |  | search_blocks, search_system_registry |
| GLOBlit_2092 |  | search_blocks, search_system_registry |
| GLOBlit_2825 |  | search_blocks, search_system_registry |
| GLOBlit_5201 |  | search_blocks, search_system_registry |
| GLOBlit_7178 |  | search_blocks, search_system_registry |
| GLOBlit_7448 |  | search_blocks, search_system_registry |
| GLOBlit_7676 |  | search_blocks, search_system_registry |
| GLOBlit_8949 |  | search_blocks, search_system_registry |
| GLOBlit_10159 |  | search_blocks, search_system_registry |
| GLOBlit_10699 |  | search_blocks, search_system_registry |
| GLOBlit_11005 |  | search_blocks, search_system_registry |
| GLOBlit_11136 |  | search_blocks, search_system_registry |
| GLOBlit_11459 |  | search_blocks, search_system_registry |
| GLOBlit_11792 |  | search_blocks, search_system_registry |
| GLOBlit_220 |  | search_blocks, search_system_registry |
| GLOBlit_1483 |  | search_blocks, search_system_registry |
| GLOBlit_2432 |  | search_blocks, search_system_registry |
| GLOBlit_2732 |  | search_blocks, search_system_registry |
| GLOBlit_3475 |  | search_blocks, search_system_registry |
| GLOBlit_4415 |  | search_blocks, search_system_registry |
| GLOBlit_5473 |  | search_blocks, search_system_registry |
| GLOBlit_7085 |  | search_blocks, search_system_registry |
| GLOBlit_7629 |  | search_blocks, search_system_registry |
| GLOBlit_8050 |  | search_blocks, search_system_registry |
| GLOBlit_8888 |  | search_blocks, search_system_registry |
| GLOBlit_9006 |  | search_blocks, search_system_registry |
| GLOBlit_10866 |  | search_blocks, search_system_registry |
| GLOBlit_11504 |  | search_blocks, search_system_registry |

#### Measurements (19 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_4 | Viscosity, Pa*s | search_blocks, search_system_registry |
| GLOBmeas_140 | Viscosity, Pa*s | search_blocks, search_system_registry |
| GLOBmeas_11 | Viscosity, Pa*s | search_blocks, search_system_registry |
| GLOBmeas_8 | Viscosity, Pa*s | search_blocks, search_system_registry |
| GLOBmeas_205 | Viscosity, Pa*s | search_blocks, search_system_registry |
| GLOBmeas_988 | Viscosity, Pa*s | search_blocks, search_system_registry |
| GLOBmeas_165 | Viscosity, Pa*s | search_blocks, search_system_registry |
| GLOBmeas_142 | Viscosity, Pa*s | search_blocks, search_system_registry |
| GLOBmeas_138 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_66 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_1497 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_236 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_203 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_212 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_153 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_141 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_6 | Mass density, kg/m3 | search_blocks, search_system_registry |

#### Phases (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks, search_system_registry |
| GLOBphase_3 |  | search_blocks, search_system_registry |
| GLOBphase_10 |  | search_blocks, search_system_registry |

#### Variables (7 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | search_blocks, search_system_registry |
| GLOBvar_3 | Pressure, kPa | search_blocks, search_system_registry |
| GLOBvar_2 | Mole fraction | search_blocks, search_system_registry |
| GLOBvar_5 | Mass fraction | search_blocks, search_system_registry |
| GLOBvar_18 | Volume fraction | search_blocks, search_system_registry |
| GLOBvar_4 | Molality, mol/kg | search_blocks, search_system_registry |
| GLOBvar_15 | Mass ratio of solute to solvent | search_blocks, search_system_registry |

#### Constraints (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | search_blocks, search_system_registry |
| GLOBconstr_8 | Molality, mol/kg | search_blocks, search_system_registry |
| GLOBconstr_2 | Temperature, K | search_blocks, search_system_registry |
| GLOBconstr_3 | Mole fraction | search_blocks, search_system_registry |
| GLOBconstr_22 | Volume fraction | search_blocks, search_system_registry |

#### Solvents (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | search_blocks, search_system_registry |
| GLOBsolvent_2 |  | search_blocks, search_system_registry |

#### Block_Types (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | search_system_registry |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 2 |
| Unique Properties | 5 |
| Unique References | 28 |
| Unique Measurements | 19 |
| Unique Phases | 3 |
| Unique Variables | 7 |
| Unique Constraints | 5 |
| Unique Solvents | 2 |
| Unique Block_Types | 1 |
| Total DOIs | 28 |
| Unique parent blocks | 43 |
| Explicit block/subsystem targets | 43 |
| Subsystem targets | 0 |
| Target-matched data points | 6,858 |

---

## 3. DOI & Block References

**Unique DOIs:** 28  |  **Parent blocks:** 43  |  **Explicit targets:** 43  |  **Subsystems:** 0  |  **Target-matched datapoints:** 3,429

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2004.11.019 | 1 | 810 | binary | search_blocks, search_system_registry |
| 10.1016/j.fluid.2014.05.032 | 1 | 140 | binary | search_blocks, search_system_registry |
| 10.1016/j.fluid.2015.07.012 | 2 | 168 | binary | search_blocks, search_system_registry |
| 10.1016/j.fluid.2017.09.005 | 2 | 144 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2004.07.019 | 1 | 565 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2006.08.002 | 3 | 301 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2007.05.004 | 2 | 74 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2011.10.009 | 1 | 70 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2015.06.024 | 1 | 40 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2018.02.022 | 2 | 344 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2019.02.027 | 1 | 9 | binary | search_blocks, search_system_registry |
| 10.1021/acs.jced.6b01058 | 1 | 12 | binary | search_blocks, search_system_registry |
| 10.1021/acs.jced.7b00299 | 2 | 4 | binary | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00086 | 2 | 12 | binary | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00723 | 1 | 3 | binary | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00939 | 2 | 18 | binary | search_blocks, search_system_registry |
| 10.1021/je020173z | 1 | 24 | binary | search_blocks, search_system_registry |
| 10.1021/je0601098 | 1 | 12 | binary | search_blocks, search_system_registry |
| 10.1021/je060219e | 1 | 26 | binary | search_blocks, search_system_registry |
| 10.1021/je060335h | 1 | 164 | binary | search_blocks, search_system_registry |
| 10.1021/je4003515 | 2 | 48 | binary | search_blocks, search_system_registry |
| 10.1021/je600565m | 2 | 35 | binary | search_blocks, search_system_registry |
| 10.1021/je700300y | 1 | 84 | binary | search_blocks, search_system_registry |
| 10.1021/je700618y | 2 | 30 | binary | search_blocks, search_system_registry |
| 10.1021/je800150h | 2 | 216 | binary | search_blocks, search_system_registry |
| 10.1021/je800942u | 2 | 36 | binary | search_blocks, search_system_registry |
| 10.1021/je900064e | 1 | 10 | binary | search_blocks, search_system_registry |
| 10.1021/je900743e | 2 | 30 | binary | search_blocks, search_system_registry |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2004.11.019 | PROPblock_2 | declared | 810 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2014.05.032 | PROPblock_1 | declared | 140 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2015.07.012 | PROPblock_3 | declared | 84 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2015.07.012 | PROPblock_4 | declared | 84 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2017.09.005 | PROPblock_3 | declared | 72 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2017.09.005 | PROPblock_4 | declared | 72 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2004.07.019 | PROPblock_2 | declared | 565 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2006.08.002 | PROPblock_2 | declared | 19 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2006.08.002 | PROPblock_3 | declared | 4 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2006.08.002 | PROPblock_4 | declared | 278 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2007.05.004 | PROPblock_11 | declared | 37 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2007.05.004 | PROPblock_12 | declared | 37 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2011.10.009 | PROPblock_3 | declared | 70 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2015.06.024 | PROPblock_7 | declared | 40 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2018.02.022 | PROPblock_19 | declared | 244 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2018.02.022 | PROPblock_21 | declared | 100 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2019.02.027 | PROPblock_21 | declared | 9 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.6b01058 | PROPblock_7 | declared | 12 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.7b00299 | PROPblock_10 | declared | 2 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.7b00299 | PROPblock_11 | declared | 2 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00086 | PROPblock_46 | declared | 6 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00086 | PROPblock_47 | declared | 6 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00723 | PROPblock_12 | declared | 3 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00939 | PROPblock_17 | declared | 9 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00939 | PROPblock_18 | declared | 9 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je020173z | PROPblock_5 | declared | 24 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je0601098 | PROPblock_20 | declared | 12 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je060219e | PROPblock_1 | declared | 26 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je060335h | PROPblock_1 | declared | 164 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je4003515 | PROPblock_7 | declared | 23 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je4003515 | PROPblock_8 | declared | 25 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je600565m | PROPblock_5 | declared | 17 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je600565m | PROPblock_6 | declared | 18 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je700300y | PROPblock_7 | declared | 84 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je700618y | PROPblock_7 | declared | 15 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je700618y | PROPblock_9 | declared | 15 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je800150h | PROPblock_8 | declared | 108 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je800150h | PROPblock_9 | declared | 108 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je800942u | PROPblock_5 | declared | 18 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je800942u | PROPblock_6 | declared | 18 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je900064e | PROPblock_6 | declared | 10 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je900743e | PROPblock_2 | declared | 15 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je900743e | PROPblock_3 | declared | 15 | binary | 2 | search_blocks, search_system_registry |

</details>

---

## 4. Tool Results (pre-compaction)

| # | Iter | Tool | Args | Raw (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 1 | `L1_query` | context=This is for Fe electrodeposit…, id_catalog… | 416 | — | — | 216.4 |
| 2 | 1 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve compound ID… | 285 | KEEP | 285 | 4.4 |
| 3 | 2 | `L1_query` | context=Need to identify these compou…, id_catalog… | 1,286 | — | — | 23.5 |
| 4 | 3 | `resolve_property_ids` | limit=5, min_score=50, purpose=Confirm GLOBprop_4 … | 285 | KEEP | 285 | 4.0 |
| 5 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=50, p… | 1,314 | KEEP | 1209 | 24.1 |
| 6 | 4 | `search_system_registry` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=50, p… | 1,256 | KEEP | 1040 | 23.9 |
| 7 | 3 | `L1_query` | context=Looking for viscosity data in…, id_catalog… | 270 | — | — | 288.6 |
| 8 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=50, p… | 1,145 | KEEP | 1056 | 23.6 |
| 9 | 2 | `search_system_registry` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=100, … | 1,235 | KEEP | 1041 | 22.4 |
| 10 | 3 | `L1_query` | context=Looking for density data in w…, id_catalog… | 270 | — | — | 170.7 |
| 11 | 2 | `resolve_property_ids` | limit=10, min_score=40, purpose=Resolve the Thermo… | 555 | KEEP | 555 | 7.6 |
| 12 | 3 | `L1_query` | context=Looking for dielectric consta…, id_catalog… | 291 | — | — | 86.5 |
| 13 | 2 | `resolve_property_ids` | limit=10, min_score=40, purpose=Find the global pr… | 442 | KEEP | 442 | 7.2 |
| 14 | 4 | `L1_query` | context=Looking for dielectric consta…, id_catalog… | 1,211 | — | — | 140.9 |
| | | **TOTAL (14 tools)** | | **10,261** | | **5,913** | **1043.8** |

---

## 5. Compaction Events

| # | Trigger | Outcome | Before (chars) | After (chars) | Saved (chars) | Saved (%) |
|--:|---------|---------|---------------:|--------------:|--------------:|----------:|
| 1 | interval=3 | skipped_by_agent | 4,986 | 4,986 | 0 | 0.0% |

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 9,605 | 963 | 10,568 | 1,879 | 10.2 |
| 2 | L1-worker | claudeopus46 | 20,643 | 1,394 | 22,037 | 14,740 | 66.9 |
| 3 | L1-worker | claudeopus46 | 20,643 | 16,862 | 37,505 | 5,644 | 24.8 |
| 4 | L1-worker | claudeopus46 | 1,356 | 4,931 | 6,287 | 1,056 | 6.8 |
| 5 | L1-worker | claudeopus46 | 536 | 4,811 | 5,347 | 1,024 | 7.6 |
| 6 | L1-worker | claudeopus46 | 298 | 1,438 | 1,736 | 1,044 | 3.6 |
| 7 | L1-worker | claudeopus46 | 1,323 | 6,754 | 8,077 | 14,542 | 45.4 |
| 8 | L1-worker | claudeopus46 | 298 | 15,264 | 15,562 | 12,143 | 38.8 |
| 9 | L1-worker | claudeopus46 | 1,160 | 24,329 | 25,489 | 12,098 | 39.8 |
| 10 | L0-main | claudeopus46 | 9,605 | 1,922 | 11,527 | 833 | 6.8 |
| 11 | L1-worker | claudeopus46 | 20,643 | 788 | 21,431 | 598 | 4.7 |
| 12 | L1-worker | claudeopus46 | 2,065 | 484 | 2,549 | 511 | 4.4 |
| 13 | L1-worker | claudeopus46 | 20,643 | 1,545 | 22,188 | 413 | 4.7 |
| 14 | L1-worker | claudeopus46 | 1,323 | 1,980 | 3,303 | 233 | 2.8 |
| 15 | L1-worker | claudeopus46 | 536 | 422 | 958 | 246 | 2.8 |
| 16 | L1-worker | claudeopus46 | 1,356 | 542 | 1,898 | 236 | 2.9 |
| 17 | L1-worker | claudeopus46 | 298 | 955 | 1,253 | 153 | 2.2 |
| 18 | L1-worker | claudeopus46 | 747 | 2,388 | 3,135 | 358 | 4.0 |
| 19 | L0-main | claudeopus46 | 9,605 | 5,167 | 14,772 | 3,424 | 16.1 |
| 20 | L1-worker | claudeopus46 | 20,643 | 2,593 | 23,236 | 1,467 | 9.2 |
| 21 | L1-worker | claudeopus46 | 20,643 | 4,788 | 25,431 | 14,478 | 55.9 |
| 22 | L1-worker | claudeopus46 | 20,643 | 5,975 | 26,618 | 13,589 | 49.2 |
| 23 | L1-worker | claudeopus46 | 2,065 | 375 | 2,440 | 481 | 4.0 |
| 24 | L1-worker | claudeopus46 | 2,065 | 9,281 | 11,346 | 1,515 | 14.2 |
| 25 | L1-worker | claudeopus46 | 20,610 | 7,700 | 28,310 | 493 | 6.4 |
| 26 | L1-worker | claudeopus46 | 20,643 | 6,947 | 27,590 | 7,104 | 38.6 |
| 27 | L1-worker | claudeopus46 | 2,065 | 2,594 | 4,659 | 1,705 | 15.2 |
| 28 | L1-worker | claudeopus46 | 20,643 | 8,742 | 29,385 | 4,826 | 28.8 |
| 29 | L1-worker | claudeopus46 | 1,356 | 2,931 | 4,287 | 872 | 5.8 |
| 30 | L1-worker | claudeopus46 | 536 | 2,811 | 3,347 | 1,091 | 8.3 |
| 31 | L1-worker | claudeopus46 | 298 | 1,254 | 1,552 | 860 | 5.8 |
| 32 | L1-worker | claudeopus46 | 1,323 | 10,228 | 11,551 | 5,153 | 20.9 |
| 33 | L1-worker | claudeopus46 | 298 | 5,875 | 6,173 | 4,299 | 19.6 |
| 34 | L1-worker | claudeopus46 | 747 | 94,985 | 95,732 | 528 | 6.1 |
| 35 | L1-worker | claudeopus46 | 20,643 | 88,692 | 109,335 | 936 | 7.3 |
| 36 | L1-worker | claudeopus46 | 2,065 | 19,005 | 21,070 | 1,531 | 14.8 |
| 37 | L1-worker | claudeopus46 | 20,643 | 90,325 | 110,968 | 961 | 7.9 |
| 38 | L1-worker | claudeopus46 | 2,065 | 4,780 | 6,845 | 1,708 | 12.6 |
| 39 | L1-worker | claudeopus46 | 20,643 | 92,110 | 112,753 | 7,568 | 44.8 |
| 40 | L1-worker | claudeopus46 | 1,356 | 3,567 | 4,923 | 865 | 6.0 |
| 41 | L1-worker | claudeopus46 | 536 | 3,447 | 3,983 | 1,038 | 7.2 |
| 42 | L1-worker | claudeopus46 | 298 | 1,247 | 1,545 | 853 | 4.0 |
| 43 | L1-worker | claudeopus46 | 1,323 | 8,084 | 9,407 | 4,247 | 19.9 |
| 44 | L1-worker | claudeopus46 | 298 | 4,969 | 5,267 | 3,452 | 17.6 |
| 45 | L1-worker | claudeopus46 | 1,160 | 13,412 | 14,572 | 3,094 | 17.0 |
| 46 | L1-worker | claudeopus46 | 747 | 81,518 | 82,265 | 758 | 7.8 |
| 47 | L1-worker | claudeopus46 | 20,643 | 163,571 | 184,214 | 741 | 5.5 |
| 48 | L1-worker | claudeopus46 | 20,643 | 164,933 | 185,576 | 1,162 | 7.1 |
| 49 | L1-worker | claudeopus46 | 2,065 | 718 | 2,783 | 1,245 | 7.2 |
| 50 | L1-worker | claudeopus46 | 20,643 | 165,416 | 186,059 | 5,642 | 31.2 |
| 51 | L1-worker | claudeopus46 | 20,643 | 171,679 | 192,322 | 2,845 | 11.7 |
| 52 | L1-worker | claudeopus46 | 536 | 1,948 | 2,484 | 1,006 | 6.1 |
| 53 | L1-worker | claudeopus46 | 1,356 | 2,068 | 3,424 | 1,240 | 6.7 |
| 54 | L1-worker | claudeopus46 | 298 | 1,362 | 1,660 | 993 | 4.8 |
| 55 | L1-worker | claudeopus46 | 1,323 | 4,786 | 6,109 | 1,459 | 11.5 |
| 56 | L1-worker | claudeopus46 | 298 | 2,181 | 2,479 | 1,178 | 5.4 |
| 57 | L1-worker | claudeopus46 | 1,160 | 6,572 | 7,732 | 1,177 | 5.6 |
| 58 | L0-main | claudeopus46 | 9,605 | 167,950 | 177,555 | 1,676 | 11.9 |
| 59 | L1-worker | claudeopus46 | 20,643 | 163,727 | 184,370 | 714 | 7.2 |
| 60 | L1-worker | claudeopus46 | 20,643 | 165,062 | 185,705 | 14,243 | 57.7 |
| 61 | L1-worker | claudeopus46 | 2,065 | 678 | 2,743 | 905 | 7.1 |
| 62 | L1-worker | claudeopus46 | 20,643 | 165,444 | 186,087 | 6,325 | 35.7 |
| 63 | L1-worker | claudeopus46 | 20,643 | 172,390 | 193,033 | 2,262 | 8.8 |
| 64 | L1-worker | claudeopus46 | 1,323 | 4,649 | 5,972 | 756 | 5.2 |
| 65 | L1-worker | claudeopus46 | 1,356 | 1,930 | 3,286 | 1,018 | 5.5 |
| 66 | L1-worker | claudeopus46 | 536 | 1,810 | 2,346 | 1,042 | 5.7 |
| 67 | L1-worker | claudeopus46 | 298 | 1,400 | 1,698 | 1,006 | 3.9 |
| 68 | L1-worker | claudeopus46 | 298 | 1,478 | 1,776 | 629 | 5.5 |
| 69 | L1-worker | claudeopus46 | 1,160 | 5,704 | 6,864 | 628 | 3.5 |
| 70 | L1-worker | claudeopus46 | 747 | 13,831 | 14,578 | 1,102 | 9.2 |
| 71 | L0-main | claudeopus46 | 9,605 | 169,998 | 179,603 | 6,972 | 52.4 |
| 72 | L0-main | claudeopus46 | 1,356 | 7,103 | 8,459 | 1,463 | 8.2 |
| 73 | L0-main | claudeopus46 | 298 | 1,845 | 2,143 | 1,418 | 4.7 |
| 74 | L0-main | claudeopus46 | 1,323 | 16,978 | 18,301 | 7,582 | 38.2 |
| 75 | L0-main | claudeopus46 | 298 | 8,250 | 8,548 | 6,784 | 30.3 |

