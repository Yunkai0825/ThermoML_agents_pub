# Reference Stats — query-agent

**Run started:** 2026-09-05 06:02:59
**Wall time (at last flush):** 219.3 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 8 | 30,036 | 44,248 | 9,000 | 74,284 | 9,285 | 61.8 | claudeopus46 |
| L1-worker | 18 | 234,728 | 138,727 | 19,699 | 373,455 | 20,747 | 173.4 | claudeopus46 |
| **TOTAL** | **26** | **264,764** | **182,975** | **28,699** | **447,739** | **17,220** | **235.2** | |

**Estimated tokens:** ~111,934 input + ~7,174 output = ~119,108 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 6 | 3 | 14 | 14 | 534 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **4** | **1** | **6** | **3** | **14** | **14** | **534** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_2 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks |

#### References (14 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_1742 |  | search_blocks |
| GLOBlit_2092 |  | search_blocks |
| GLOBlit_2825 |  | search_blocks |
| GLOBlit_5201 |  | search_blocks |
| GLOBlit_7178 |  | search_blocks |
| GLOBlit_7448 |  | search_blocks |
| GLOBlit_7676 |  | search_blocks |
| GLOBlit_8949 |  | search_blocks |
| GLOBlit_10159 |  | search_blocks |
| GLOBlit_10699 |  | search_blocks |
| GLOBlit_11005 |  | search_blocks |
| GLOBlit_11136 |  | search_blocks |
| GLOBlit_11459 |  | search_blocks |
| GLOBlit_11792 |  | search_blocks |

#### Properties (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_4 | Viscosity, Pa*s | search_blocks |

#### Measurements (8 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_4 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_140 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_11 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_8 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_205 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_988 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_165 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_142 | Viscosity, Pa*s | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks |

#### Variables (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_3 | Pressure, kPa | search_blocks |
| GLOBvar_2 | Mole fraction | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |
| GLOBvar_18 | Volume fraction | search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |

#### Constraints (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | search_blocks |
| GLOBconstr_8 | Molality, mol/kg | search_blocks |
| GLOBconstr_2 | Temperature, K | search_blocks |

#### Solvents (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | search_blocks |
| GLOBsolvent_2 |  | search_blocks |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 2 |
| Unique References | 14 |
| Unique Properties | 1 |
| Unique Measurements | 8 |
| Unique Phases | 1 |
| Unique Variables | 6 |
| Unique Constraints | 3 |
| Unique Solvents | 2 |
| Total DOIs | 14 |
| Unique parent blocks | 14 |
| Explicit block/subsystem targets | 14 |
| Subsystem targets | 0 |
| Target-matched data points | 534 |

---

## 3. DOI & Block References

**Unique DOIs:** 14  |  **Parent blocks:** 14  |  **Explicit targets:** 14  |  **Subsystems:** 0  |  **Target-matched datapoints:** 534

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2015.07.012 | 1 | 84 | binary | search_blocks |
| 10.1016/j.fluid.2017.09.005 | 1 | 72 | binary | search_blocks |
| 10.1016/j.jct.2007.05.004 | 1 | 37 | binary | search_blocks |
| 10.1016/j.jct.2018.02.022 | 1 | 100 | binary | search_blocks |
| 10.1021/acs.jced.7b00299 | 1 | 2 | binary | search_blocks |
| 10.1021/acs.jced.8b00086 | 1 | 6 | binary | search_blocks |
| 10.1021/acs.jced.8b00939 | 1 | 9 | binary | search_blocks |
| 10.1021/je060219e | 1 | 26 | binary | search_blocks |
| 10.1021/je4003515 | 1 | 25 | binary | search_blocks |
| 10.1021/je600565m | 1 | 17 | binary | search_blocks |
| 10.1021/je700618y | 1 | 15 | binary | search_blocks |
| 10.1021/je800150h | 1 | 108 | binary | search_blocks |
| 10.1021/je800942u | 1 | 18 | binary | search_blocks |
| 10.1021/je900743e | 1 | 15 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2015.07.012 | PROPblock_4 | declared | 84 | binary | — | search_blocks |
| 10.1016/j.fluid.2017.09.005 | PROPblock_4 | declared | 72 | binary | — | search_blocks |
| 10.1016/j.jct.2007.05.004 | PROPblock_11 | declared | 37 | binary | — | search_blocks |
| 10.1016/j.jct.2018.02.022 | PROPblock_21 | declared | 100 | binary | — | search_blocks |
| 10.1021/acs.jced.7b00299 | PROPblock_11 | declared | 2 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00086 | PROPblock_47 | declared | 6 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00939 | PROPblock_18 | declared | 9 | binary | — | search_blocks |
| 10.1021/je060219e | PROPblock_1 | declared | 26 | binary | — | search_blocks |
| 10.1021/je4003515 | PROPblock_8 | declared | 25 | binary | — | search_blocks |
| 10.1021/je600565m | PROPblock_5 | declared | 17 | binary | — | search_blocks |
| 10.1021/je700618y | PROPblock_7 | declared | 15 | binary | — | search_blocks |
| 10.1021/je800150h | PROPblock_8 | declared | 108 | binary | — | search_blocks |
| 10.1021/je800942u | PROPblock_5 | declared | 18 | binary | — | search_blocks |
| 10.1021/je900743e | PROPblock_2 | declared | 15 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Resolve ethanol and… | 222 | KEEP ←in 278 | 222 | 6.9 |
| 2 | 3 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=50, p… | 1,260 | KEEP ←in 8,844 | 1242 | 20.9 |
| 3 | 5 | `inspect_block_table` | block_number=PROPblock_4, literature=GLOBlit_2092,… | 2,405 | — | — | 0.1 |
| 4 | 6 | `inspect_block_table` | block_number=PROPblock_4, literature=GLOBlit_1742,… | 2,697 | — | — | 0.1 |
| 5 | 7 | `inspect_block_table` | block_number=PROPblock_11, literature=GLOBlit_2825… | 1,568 | — | — | 0.1 |
| 6 | 1 | `L1_query` | context=User is asking for viscosity …, id_catalog… | 45,786 | — | — | 165.9 |
| | | **TOTAL (6 tools)** | | **53,938** | | **1,464** | **194.0** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 523 | 12,104 | 1,451 | 8.6 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,048 | 25,143 | 864 | 6.6 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,063 | 26,158 | 540 | 5.0 |
| 4 | L1-worker | claudeopus46 | 3,767 | 437 | 4,204 | 209 | 3.1 |
| 5 | L1-worker | claudeopus46 | 3,767 | 739 | 4,506 | 398 | 3.6 |
| 6 | L1-worker | claudeopus46 | 24,095 | 1,689 | 25,784 | 776 | 7.2 |
| 7 | L1-worker | claudeopus46 | 3,767 | 9,244 | 13,011 | 1,534 | 14.7 |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,326 | 27,421 | 2,437 | 17.3 |
| 9 | L1-worker | claudeopus46 | 24,095 | 8,136 | 32,231 | 1,016 | 8.6 |
| 10 | L1-worker | claudeopus46 | 24,095 | 10,880 | 34,975 | 730 | 8.9 |
| 11 | L1-worker | claudeopus46 | 24,095 | 13,865 | 37,960 | 529 | 7.1 |
| 12 | L1-worker | claudeopus46 | 24,095 | 15,723 | 39,818 | 2,276 | 21.0 |
| 13 | L1-worker | claudeopus46 | 24,095 | 22,467 | 46,562 | 3,570 | 32.8 |
| 14 | L1-worker | claudeopus46 | 2,320 | 5,239 | 7,559 | 710 | 6.1 |
| 15 | L1-worker | claudeopus46 | 627 | 5,119 | 5,746 | 695 | 7.2 |
| 16 | L1-worker | claudeopus46 | 2,106 | 6,408 | 8,514 | 1,497 | 8.9 |
| 17 | L1-worker | claudeopus46 | 366 | 1,147 | 1,513 | 313 | 2.8 |
| 18 | L1-worker | claudeopus46 | 366 | 2,274 | 2,640 | 788 | 4.0 |
| 19 | L1-worker | claudeopus46 | 787 | 28,923 | 29,710 | 817 | 8.5 |
| 20 | L0-main | claudeopus46 | 11,581 | 26,083 | 37,664 | 2,600 | 23.1 |
| 21 | L0-main | claudeopus46 | 2,106 | 2,916 | 5,022 | 776 | 4.9 |
| 22 | L0-main | claudeopus46 | 2,320 | 2,561 | 4,881 | 932 | 5.2 |
| 23 | L0-main | claudeopus46 | 366 | 1,407 | 1,773 | 883 | 4.0 |
| 24 | L0-main | claudeopus46 | 366 | 1,325 | 1,691 | 923 | 4.5 |
| 25 | L0-main | claudeopus46 | 560 | 3,619 | 4,179 | 276 | 2.8 |
| 26 | L0-main | claudeopus46 | 1,156 | 5,814 | 6,970 | 1,159 | 8.7 |

