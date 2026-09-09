# Reference Stats — analysis-agent

**Run started:** 2026-09-05 06:07:18
**Wall time (at last flush):** 464.6 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 22 | 346,562 | 514,792 | 32,659 | 861,354 | 39,152 | 234.6 | claudeopus46 |
| L1-worker | 21 | 303,612 | 206,875 | 37,142 | 510,487 | 24,308 | 243.6 | claudeopus46 |
| **TOTAL** | **43** | **650,174** | **721,667** | **69,801** | **1,371,841** | **31,903** | **478.2** | |

**Estimated tokens:** ~342,960 input + ~17,450 output = ~360,410 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `query_thermoml` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 4 | 3 | 10 | 10 | 334 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml` | 2 | 1 | 4 | 3 | 7 | 7 | 50 |
| **TOTAL** | **6** | **2** | **8** | **6** | **17** | **17** | **384** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_2 |  | query_thermoml, resolve_compound_ids, search_blocks |
| GLOBcomp_1 |  | query_thermoml, resolve_compound_ids, search_blocks |

#### References (10 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_2825 |  | query_thermoml, search_blocks |
| GLOBlit_5201 |  | query_thermoml, search_blocks |
| GLOBlit_7178 |  | query_thermoml, search_blocks |
| GLOBlit_7448 |  | query_thermoml, search_blocks |
| GLOBlit_7676 |  | query_thermoml, search_blocks |
| GLOBlit_10159 |  | query_thermoml, search_blocks |
| GLOBlit_10699 |  | query_thermoml, search_blocks |
| GLOBlit_11005 |  | search_blocks |
| GLOBlit_11136 |  | search_blocks |
| GLOBlit_11792 |  | search_blocks |

#### Properties (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_4 | Viscosity, Pa*s | query_thermoml, search_blocks |

#### Measurements (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_140 | Viscosity, Pa*s | query_thermoml, search_blocks |
| GLOBmeas_11 | Viscosity, Pa*s | query_thermoml, search_blocks |
| GLOBmeas_4 | Viscosity, Pa*s | query_thermoml, search_blocks |
| GLOBmeas_8 | Viscosity, Pa*s | query_thermoml, search_blocks |
| GLOBmeas_988 | Viscosity, Pa*s | query_thermoml, search_blocks |
| GLOBmeas_165 | Viscosity, Pa*s | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | query_thermoml, search_blocks |

#### Variables (4 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | query_thermoml, search_blocks |
| GLOBvar_2 | Mole fraction | query_thermoml, search_blocks |
| GLOBvar_5 | Mass fraction | query_thermoml, search_blocks |
| GLOBvar_4 | Molality, mol/kg | query_thermoml, search_blocks |

#### Constraints (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | query_thermoml, search_blocks |
| GLOBconstr_8 | Molality, mol/kg | query_thermoml, search_blocks |
| GLOBconstr_2 | Temperature, K | query_thermoml, search_blocks |

#### Solvents (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | query_thermoml, search_blocks |

#### Block_Types (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | query_thermoml |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 2 |
| Unique References | 10 |
| Unique Properties | 1 |
| Unique Measurements | 6 |
| Unique Phases | 1 |
| Unique Variables | 4 |
| Unique Constraints | 3 |
| Unique Solvents | 1 |
| Unique Block_Types | 1 |
| Total DOIs | 10 |
| Unique parent blocks | 10 |
| Explicit block/subsystem targets | 10 |
| Subsystem targets | 0 |
| Target-matched data points | 530 |

---

## 3. DOI & Block References

**Unique DOIs:** 10  |  **Parent blocks:** 10  |  **Explicit targets:** 10  |  **Subsystems:** 0  |  **Target-matched datapoints:** 334

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.jct.2007.05.004 | 1 | 37 | binary | query_thermoml, search_blocks |
| 10.1016/j.jct.2018.02.022 | 1 | 100 | binary | query_thermoml, search_blocks |
| 10.1021/acs.jced.7b00299 | 1 | 2 | binary | query_thermoml, search_blocks |
| 10.1021/acs.jced.8b00086 | 1 | 6 | binary | query_thermoml, search_blocks |
| 10.1021/acs.jced.8b00939 | 1 | 9 | binary | query_thermoml, search_blocks |
| 10.1021/je4003515 | 1 | 25 | binary | query_thermoml, search_blocks |
| 10.1021/je600565m | 1 | 17 | binary | query_thermoml, search_blocks |
| 10.1021/je700618y | 1 | 15 | binary | search_blocks |
| 10.1021/je800150h | 1 | 108 | binary | search_blocks |
| 10.1021/je900743e | 1 | 15 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.jct.2007.05.004 | PROPblock_11 | declared | 37 | binary | 2 | query_thermoml, search_blocks |
| 10.1016/j.jct.2018.02.022 | PROPblock_21 | declared | 100 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/acs.jced.7b00299 | PROPblock_11 | declared | 2 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/acs.jced.8b00086 | PROPblock_47 | declared | 6 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/acs.jced.8b00939 | PROPblock_18 | declared | 9 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je4003515 | PROPblock_8 | declared | 25 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je600565m | PROPblock_5 | declared | 17 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je700618y | PROPblock_7 | declared | 15 | binary | — | search_blocks |
| 10.1021/je800150h | PROPblock_8 | declared | 108 | binary | — | search_blocks |
| 10.1021/je900743e | PROPblock_2 | declared | 15 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 1 | `query_thermoml` | id_catalog=[{'id': 'GLOBprop_4', 'type':…, instruc… | 198 | — | — | 0.0 |
| 2 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve ethanol and… | 198 | KEEP ←in 276 | 198 | 4.6 |
| 3 | 4 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=50, p… | 1,242 | KEEP ←in 6,284 | 1242 | 21.3 |
| 4 | 6 | `inspect_block_table` | block_number=PROPblock_11, literature=GLOBlit_2825… | 261 | — | — | 0.0 |
| 5 | 7 | `inspect_block_table` | block_number=PROPblock_11, literature=GLOBlit_2825… | 365 | — | — | 0.5 |
| 6 | 8 | `inspect_block_table` | block_number=PROPblock_11, literature=GLOBlit_2825… | 1,124 | — | — | 0.1 |
| 7 | 9 | `inspect_block_table` | block_number=PROPblock_21, literature=GLOBlit_5201… | 1,137 | — | — | 0.5 |
| 8 | 10 | `inspect_block_table` | block_number=PROPblock_18, literature=GLOBlit_7676… | 1,190 | — | — | 0.1 |
| 9 | 2 | `query_thermoml` | instruction=Search for blocks containing …, purpos… | 54,901 | — | — | 226.9 |
| 10 | 5 | `inspect_block` | block_number=PROPblock_11, doi=10.1016/j.jct.2007.… | 1,338 | — | — | 0.1 |
| 11 | 9 | `fit_multi_system` | purpose=Fit Redlich-Kister polynomial…, systems=[{… | 534 | — | — | 0.2 |
| 12 | 13 | `fit_multi_system` | purpose=Fit Redlich-Kister polynomial…, systems=[{… | 1,187 | — | — | 3.0 |
| | | **TOTAL (12 tools)** | | **63,675** | | **1,440** | **257.3** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 22,518 | 439 | 22,957 | 994 | 7.7 |
| 2 | L0-main | claudeopus46 | 22,518 | 895 | 23,413 | 731 | 5.4 |
| 3 | L1-worker | claudeopus46 | 24,095 | 949 | 25,044 | 622 | 5.0 |
| 4 | L1-worker | claudeopus46 | 24,095 | 1,990 | 26,085 | 556 | 4.2 |
| 5 | L1-worker | claudeopus46 | 3,767 | 435 | 4,202 | 332 | 3.6 |
| 6 | L1-worker | claudeopus46 | 24,095 | 1,575 | 25,670 | 889 | 6.3 |
| 7 | L1-worker | claudeopus46 | 24,095 | 2,290 | 26,385 | 664 | 5.2 |
| 8 | L1-worker | claudeopus46 | 3,767 | 6,748 | 10,515 | 1,546 | 13.9 |
| 9 | L1-worker | claudeopus46 | 24,095 | 3,480 | 27,575 | 4,941 | 30.8 |
| 10 | L1-worker | claudeopus46 | 24,095 | 11,839 | 35,934 | 1,266 | 10.9 |
| 11 | L1-worker | claudeopus46 | 24,095 | 12,497 | 36,592 | 572 | 6.1 |
| 12 | L1-worker | claudeopus46 | 24,095 | 13,167 | 37,262 | 953 | 7.3 |
| 13 | L1-worker | claudeopus46 | 24,095 | 14,602 | 38,697 | 1,704 | 13.6 |
| 14 | L1-worker | claudeopus46 | 24,095 | 16,094 | 40,189 | 650 | 5.9 |
| 15 | L1-worker | claudeopus46 | 24,095 | 17,615 | 41,710 | 4,280 | 28.6 |
| 16 | L1-worker | claudeopus46 | 24,095 | 28,192 | 52,287 | 6,308 | 40.2 |
| 17 | L1-worker | claudeopus46 | 2,320 | 4,664 | 6,984 | 1,475 | 9.2 |
| 18 | L1-worker | claudeopus46 | 627 | 4,544 | 5,171 | 1,311 | 9.6 |
| 19 | L1-worker | claudeopus46 | 2,106 | 5,734 | 7,840 | 3,501 | 14.6 |
| 20 | L1-worker | claudeopus46 | 366 | 1,912 | 2,278 | 1,425 | 5.8 |
| 21 | L1-worker | claudeopus46 | 366 | 1,722 | 2,088 | 1,298 | 5.4 |
| 22 | L1-worker | claudeopus46 | 366 | 4,278 | 4,644 | 2,132 | 9.5 |
| 23 | L1-worker | claudeopus46 | 787 | 52,548 | 53,335 | 717 | 7.9 |
| 24 | L0-main | claudeopus46 | 22,518 | 31,366 | 53,884 | 1,242 | 11.5 |
| 25 | L0-main | claudeopus46 | 22,518 | 32,202 | 54,720 | 577 | 5.9 |
| 26 | L0-main | claudeopus46 | 22,518 | 32,894 | 55,412 | 480 | 4.0 |
| 27 | L0-main | claudeopus46 | 22,518 | 34,377 | 56,895 | 1,583 | 12.7 |
| 28 | L0-main | claudeopus46 | 22,518 | 35,125 | 57,643 | 1,484 | 9.8 |
| 29 | L0-main | claudeopus46 | 22,518 | 35,783 | 58,301 | 1,186 | 8.1 |
| 30 | L0-main | claudeopus46 | 22,518 | 36,458 | 58,976 | 1,414 | 10.2 |
| 31 | L0-main | claudeopus46 | 22,518 | 36,371 | 58,889 | 1,061 | 7.6 |
| 32 | L0-main | claudeopus46 | 22,518 | 36,995 | 59,513 | 1,111 | 7.3 |
| 33 | L0-main | claudeopus46 | 22,518 | 37,592 | 60,110 | 1,370 | 9.9 |
| 34 | L0-main | claudeopus46 | 22,518 | 38,249 | 60,767 | 1,085 | 7.8 |
| 35 | L0-main | claudeopus46 | 22,518 | 41,405 | 63,923 | 5,949 | 40.0 |
| 36 | L0-main | claudeopus46 | 22,518 | 52,364 | 74,882 | 6,754 | 47.2 |
| 37 | L0-main | claudeopus46 | 2,106 | 5,763 | 7,869 | 275 | 2.9 |
| 38 | L0-main | claudeopus46 | 366 | 798 | 1,164 | 261 | 2.6 |
| 39 | L0-main | claudeopus46 | 2,320 | 5,209 | 7,529 | 1,472 | 8.6 |
| 40 | L0-main | claudeopus46 | 366 | 1,909 | 2,275 | 1,422 | 5.3 |
| 41 | L0-main | claudeopus46 | 560 | 6,017 | 6,577 | 187 | 2.5 |
| 42 | L0-main | claudeopus46 | 1,156 | 7,475 | 8,631 | 921 | 7.2 |
| 43 | L0-main | claudeopus46 | 1,918 | 5,106 | 7,024 | 1,100 | 10.4 |

