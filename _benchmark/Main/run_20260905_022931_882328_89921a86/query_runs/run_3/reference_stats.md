# Reference Stats — query-agent

**Run started:** 2026-09-05 02:29:42
**Wall time (at last flush):** 454.8 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 9 | 41,617 | 75,830 | 12,997 | 117,447 | 13,049 | 86.7 | claudeopus46 |
| L1-worker | 46 | 642,587 | 368,033 | 53,286 | 1,010,620 | 21,970 | 384.5 | claudeopus46 |
| verdict | 1 | 972 | 8,407 | 1,073 | 9,379 | 9,379 | 9.6 | claudeopus46 |
| **TOTAL** | **56** | **685,176** | **452,270** | **67,356** | **1,137,446** | **20,311** | **480.8** | |

**Estimated tokens:** ~284,361 input + ~16,839 output = ~301,200 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 4 | 3 | 10 | 10 | 334 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_property_ids` | 0 | 7 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **4** | **8** | **4** | **3** | **10** | **10** | **334** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_2 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks |

#### References (10 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_2825 |  | search_blocks |
| GLOBlit_5201 |  | search_blocks |
| GLOBlit_7178 |  | search_blocks |
| GLOBlit_7448 |  | search_blocks |
| GLOBlit_7676 |  | search_blocks |
| GLOBlit_10159 |  | search_blocks |
| GLOBlit_10699 |  | search_blocks |
| GLOBlit_11005 |  | search_blocks |
| GLOBlit_11136 |  | search_blocks |
| GLOBlit_11792 |  | search_blocks |

#### Properties (7 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_4 | Viscosity, Pa*s | resolve_property_ids, search_blocks |
| GLOBprop_40 |  | resolve_property_ids |
| GLOBprop_48 |  | resolve_property_ids |
| GLOBprop_98 |  | resolve_property_ids |
| GLOBprop_45 |  | resolve_property_ids |
| GLOBprop_107 |  | resolve_property_ids |
| GLOBprop_60 |  | resolve_property_ids |

#### Measurements (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_140 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_11 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_4 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_8 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_988 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_165 | Viscosity, Pa*s | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks |

#### Variables (4 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_2 | Mole fraction | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |

#### Constraints (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | search_blocks |
| GLOBconstr_8 | Molality, mol/kg | search_blocks |
| GLOBconstr_2 | Temperature, K | search_blocks |

#### Solvents (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | search_blocks |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 2 |
| Unique References | 10 |
| Unique Properties | 7 |
| Unique Measurements | 6 |
| Unique Phases | 1 |
| Unique Variables | 4 |
| Unique Constraints | 3 |
| Unique Solvents | 1 |
| Total DOIs | 10 |
| Unique parent blocks | 10 |
| Explicit block/subsystem targets | 10 |
| Subsystem targets | 0 |
| Target-matched data points | 334 |

---

## 3. DOI & Block References

**Unique DOIs:** 10  |  **Parent blocks:** 10  |  **Explicit targets:** 10  |  **Subsystems:** 0  |  **Target-matched datapoints:** 334

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.jct.2007.05.004 | 1 | 37 | binary | search_blocks |
| 10.1016/j.jct.2018.02.022 | 1 | 100 | binary | search_blocks |
| 10.1021/acs.jced.7b00299 | 1 | 2 | binary | search_blocks |
| 10.1021/acs.jced.8b00086 | 1 | 6 | binary | search_blocks |
| 10.1021/acs.jced.8b00939 | 1 | 9 | binary | search_blocks |
| 10.1021/je4003515 | 1 | 25 | binary | search_blocks |
| 10.1021/je600565m | 1 | 17 | binary | search_blocks |
| 10.1021/je700618y | 1 | 15 | binary | search_blocks |
| 10.1021/je800150h | 1 | 108 | binary | search_blocks |
| 10.1021/je900743e | 1 | 15 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.jct.2007.05.004 | PROPblock_11 | declared | 37 | binary | — | search_blocks |
| 10.1016/j.jct.2018.02.022 | PROPblock_21 | declared | 100 | binary | — | search_blocks |
| 10.1021/acs.jced.7b00299 | PROPblock_11 | declared | 2 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00086 | PROPblock_47 | declared | 6 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00939 | PROPblock_18 | declared | 9 | binary | — | search_blocks |
| 10.1021/je4003515 | PROPblock_8 | declared | 25 | binary | — | search_blocks |
| 10.1021/je600565m | PROPblock_5 | declared | 17 | binary | — | search_blocks |
| 10.1021/je700618y | PROPblock_7 | declared | 15 | binary | — | search_blocks |
| 10.1021/je800150h | PROPblock_8 | declared | 108 | binary | — | search_blocks |
| 10.1021/je900743e | PROPblock_2 | declared | 15 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Resolve ethanol and… | 213 | KEEP ←in 278 | 213 | 4.0 |
| 2 | 4 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=20, p… | 1,258 | KEEP ←in 6,284 | 1258 | 20.0 |
| 3 | 5 | `inspect_block_table` | block_number=PROPblock_11, literature=GLOBlit_2825… | 262 | — | — | 0.0 |
| 4 | 6 | `inspect_block_table` | block_number=PROPblock_11, literature=GLOBlit_2825… | 365 | — | — | 0.1 |
| 5 | 7 | `inspect_block_table` | block_number=PROPblock_11, literature=GLOBlit_2825… | 1,214 | — | — | 0.1 |
| 6 | 8 | `inspect_block_table` | block_number=PROPblock_21, literature=GLOBlit_5201… | 1,233 | — | — | 0.2 |
| 7 | 9 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=10, p… | 1,091 | DISCARD ←in 39 | 1033 | 18.0 |
| 8 | 11 | `inspect_block_table` | block_number=GLOBlit_2825::PROPblock_11, nearest={… | 1,004 | — | — | 0.8 |
| 9 | 1 | `L1_query` | context=Property IDs: GLOBprop_4 = dy…, id_catalog… | 21,495 | — | — | 234.4 |
| 10 | 2 | `resolve_property_ids` | limit=20, min_score=40, purpose=Find property IDs … | 874 | KEEP ←in 801 | 874 | 11.2 |
| 11 | 3 | `search_id_alignment` | entity_type=property, limit=20, purpose=Find any e… | 772 | DISCARD ←in 84 | 708 | 7.2 |
| 12 | 4 | `search_id_alignment` | entity_type=property, limit=20, purpose=Find all v… | 277 | KEEP ←in 271 | 277 | 4.4 |
| 13 | 5 | `search_id_alignment` | entity_type=property, limit=30, purpose=Find all e… | 838 | KEEP ←in 627 | 838 | 6.6 |
| 14 | 7 | `inspect_block_table` | block_number=GLOBlit_5201::PROPblock_21, nearest=x… | 264 | — | — | 0.0 |
| 15 | 8 | `inspect_block_table` | block_number=GLOBlit_5201::PROPblock_21, nearest={… | 376 | — | — | 0.2 |
| 16 | 9 | `inspect_block_table` | block_number=GLOBlit_5201::PROPblock_21, nearest={… | 1,286 | — | — | 0.1 |
| 17 | 11 | `inspect_block_table` | block_number=GLOBlit_2825::PROPblock_11, nearest={… | 1,057 | — | — | 0.1 |
| 18 | 2 | `L1_query` | context=We already found dynamic visc…, id_catalog… | 6,798 | — | — | 133.8 |
| | | **TOTAL (18 tools)** | | **40,677** | | **5,201** | **441.2** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 992 | 12,573 | 1,527 | 9.5 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,304 | 25,399 | 535 | 4.9 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,352 | 26,447 | 563 | 4.1 |
| 4 | L1-worker | claudeopus46 | 3,767 | 470 | 4,237 | 375 | 3.9 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,947 | 26,042 | 996 | 7.9 |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,703 | 26,798 | 738 | 6.3 |
| 7 | L1-worker | claudeopus46 | 3,767 | 6,734 | 10,501 | 1,562 | 14.7 |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,985 | 28,080 | 1,192 | 8.7 |
| 9 | L1-worker | claudeopus46 | 24,095 | 4,682 | 28,777 | 714 | 5.2 |
| 10 | L1-worker | claudeopus46 | 24,095 | 5,397 | 29,492 | 1,213 | 9.2 |
| 11 | L1-worker | claudeopus46 | 24,095 | 6,964 | 31,059 | 988 | 7.9 |
| 12 | L1-worker | claudeopus46 | 24,095 | 8,637 | 32,732 | 1,198 | 9.9 |
| 13 | L1-worker | claudeopus46 | 3,767 | 514 | 4,281 | 1,550 | 10.2 |
| 14 | L1-worker | claudeopus46 | 24,095 | 10,132 | 34,227 | 3,661 | 26.1 |
| 15 | L1-worker | claudeopus46 | 24,095 | 18,608 | 42,703 | 3,582 | 27.6 |
| 16 | L1-worker | claudeopus46 | 24,095 | 20,095 | 44,190 | 3,383 | 24.4 |
| 17 | L1-worker | claudeopus46 | 24,062 | 26,005 | 50,067 | 3,585 | 25.2 |
| 18 | L1-worker | claudeopus46 | 2,320 | 3,716 | 6,036 | 905 | 5.9 |
| 19 | L1-worker | claudeopus46 | 2,106 | 5,141 | 7,247 | 1,469 | 8.0 |
| 20 | L1-worker | claudeopus46 | 627 | 3,596 | 4,223 | 1,107 | 8.4 |
| 21 | L1-worker | claudeopus46 | 366 | 1,342 | 1,708 | 865 | 4.3 |
| 22 | L1-worker | claudeopus46 | 366 | 1,518 | 1,884 | 1,094 | 4.7 |
| 23 | L1-worker | claudeopus46 | 366 | 2,246 | 2,612 | 1,136 | 5.3 |
| 24 | L1-worker | claudeopus46 | 787 | 21,693 | 22,480 | 709 | 7.5 |
| 25 | L0-main | claudeopus46 | 11,581 | 19,821 | 31,402 | 1,714 | 13.4 |
| 26 | L1-worker | claudeopus46 | 24,095 | 9,169 | 33,264 | 836 | 5.9 |
| 27 | L1-worker | claudeopus46 | 24,095 | 10,285 | 34,380 | 682 | 4.1 |
| 28 | L1-worker | claudeopus46 | 3,767 | 989 | 4,756 | 1,729 | 11.0 |
| 29 | L1-worker | claudeopus46 | 24,095 | 10,523 | 34,618 | 965 | 6.9 |
| 30 | L1-worker | claudeopus46 | 3,767 | 379 | 4,146 | 948 | 6.9 |
| 31 | L1-worker | claudeopus46 | 24,095 | 11,670 | 35,765 | 739 | 4.6 |
| 32 | L1-worker | claudeopus46 | 3,767 | 435 | 4,202 | 441 | 4.3 |
| 33 | L1-worker | claudeopus46 | 24,095 | 12,268 | 36,363 | 651 | 4.8 |
| 34 | L1-worker | claudeopus46 | 3,767 | 850 | 4,617 | 1,197 | 6.5 |
| 35 | L1-worker | claudeopus46 | 24,095 | 13,413 | 37,508 | 1,895 | 14.6 |
| 36 | L1-worker | claudeopus46 | 24,095 | 17,789 | 41,884 | 637 | 6.0 |
| 37 | L1-worker | claudeopus46 | 24,095 | 18,376 | 42,471 | 568 | 6.7 |
| 38 | L1-worker | claudeopus46 | 24,095 | 19,037 | 43,132 | 627 | 5.8 |
| 39 | L1-worker | claudeopus46 | 24,095 | 20,618 | 44,713 | 485 | 4.7 |
| 40 | L1-worker | claudeopus46 | 24,095 | 21,668 | 45,763 | 632 | 4.9 |
| 41 | L1-worker | claudeopus46 | 24,095 | 22,163 | 46,258 | 2,093 | 16.6 |
| 42 | L1-worker | claudeopus46 | 2,106 | 3,953 | 6,059 | 353 | 3.3 |
| 43 | L1-worker | claudeopus46 | 2,320 | 2,224 | 4,544 | 849 | 4.5 |
| 44 | L1-worker | claudeopus46 | 366 | 1,130 | 1,496 | 80 | 2.1 |
| 45 | L1-worker | claudeopus46 | 627 | 2,104 | 2,731 | 1,185 | 6.5 |
| 46 | L1-worker | claudeopus46 | 366 | 1,286 | 1,652 | 814 | 3.9 |
| 47 | L1-worker | claudeopus46 | 366 | 1,596 | 1,962 | 1,172 | 4.8 |
| 48 | L1-worker | claudeopus46 | 787 | 6,327 | 7,114 | 588 | 4.8 |
| 49 | L0-main | claudeopus46 | 11,581 | 30,646 | 42,227 | 4,472 | 30.3 |
| 50 | L0-main | claudeopus46 | 2,106 | 5,167 | 7,273 | 951 | 6.2 |
| 51 | L0-main | claudeopus46 | 2,320 | 4,343 | 6,663 | 1,106 | 8.3 |
| 52 | L0-main | claudeopus46 | 366 | 1,500 | 1,866 | 1,013 | 4.6 |
| 53 | L0-main | claudeopus46 | 366 | 1,581 | 1,947 | 1,062 | 4.7 |
| 54 | L0-main | claudeopus46 | 560 | 5,210 | 5,770 | 187 | 2.7 |
| 55 | L0-main | claudeopus46 | 1,156 | 6,570 | 7,726 | 965 | 7.0 |
| 56 | verdict | claudeopus46 | 972 | 8,407 | 9,379 | 1,073 | 9.6 |

