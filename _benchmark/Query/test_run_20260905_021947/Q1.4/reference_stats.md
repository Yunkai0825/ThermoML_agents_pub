# Reference Stats — query-agent

**Run started:** 2026-09-05 05:21:46
**Wall time (at last flush):** 197.6 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 11 | 32,312 | 38,238 | 7,917 | 70,550 | 6,413 | 57.0 | claudeopus46 |
| L1-worker | 21 | 307,013 | 93,124 | 19,703 | 400,137 | 19,054 | 153.2 | claudeopus46 |
| **TOTAL** | **32** | **339,325** | **131,362** | **27,620** | **470,687** | **14,708** | **210.2** | |

**Estimated tokens:** ~117,671 input + ~6,905 output = ~124,576 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_property_ids` | 0 | 9 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 1 | 2 | 1 | 1 | 141 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **4** | **10** | **1** | **2** | **1** | **1** | **141** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_107 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks |

#### Properties (9 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_3 |  | resolve_property_ids |
| GLOBprop_56 |  | resolve_property_ids, search_blocks |
| GLOBprop_73 |  | resolve_property_ids |
| GLOBprop_38 |  | resolve_property_ids |
| GLOBprop_89 |  | resolve_property_ids |
| GLOBprop_94 |  | resolve_property_ids |
| GLOBprop_71 |  | resolve_property_ids |
| GLOBprop_95 |  | resolve_property_ids |
| GLOBprop_33 |  | resolve_property_ids |

#### References (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_1540 |  | search_blocks |

#### Measurements (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_185 | Mean ionic activity coefficient | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks |

#### Solvents (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | search_blocks |

#### Variables (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_4 | Molality, mol/kg | search_blocks |

#### Constraints (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_2 | Temperature, K | search_blocks |
| GLOBconstr_1 | Pressure, kPa | search_blocks |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 2 |
| Unique Properties | 9 |
| Unique References | 1 |
| Unique Measurements | 1 |
| Unique Phases | 1 |
| Unique Solvents | 1 |
| Unique Variables | 1 |
| Unique Constraints | 2 |
| Total DOIs | 1 |
| Unique parent blocks | 1 |
| Explicit block/subsystem targets | 1 |
| Subsystem targets | 0 |
| Target-matched data points | 141 |

---

## 3. DOI & Block References

**Unique DOIs:** 1  |  **Parent blocks:** 1  |  **Explicit targets:** 1  |  **Subsystems:** 0  |  **Target-matched datapoints:** 141

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2014.08.026 | 1 | 141 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2014.08.026 | PROPblock_13 | declared | 141 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve compound ID… | 213 | KEEP ←in 296 | 213 | 4.5 |
| 2 | 3 | `resolve_property_ids` | limit=10, min_score=50, purpose=Find property IDs … | 231 | KEEP ←in 965 | 231 | 4.3 |
| 3 | 5 | `search_blocks` | compound=['GLOBcomp_107', 'GLOBcomp_1'], limit=50,… | 1,230 | KEEP ←in 1,949 | 1215 | 13.0 |
| 4 | 6 | `inspect_block_table` | block_number=PROPblock_13, literature=GLOBlit_1540… | 412 | — | — | 0.1 |
| 5 | 7 | `inspect_block_table` | block_number=PROPblock_13, literature=GLOBlit_1540… | 321 | — | — | 0.0 |
| 6 | 8 | `inspect_block_table` | block_number=PROPblock_13, literature=GLOBlit_1540… | 422 | — | — | 1.4 |
| 7 | 9 | `inspect_block_table` | block_number=PROPblock_13, literature=GLOBlit_1540… | 1,232 | — | — | 0.1 |
| 8 | 10 | `inspect_block_table` | block_number=PROPblock_13, literature=GLOBlit_1540… | 1,304 | — | — | 0.1 |
| 9 | 1 | `L1_query` | instruction=Search for activity coefficie…, purpos… | 13,512 | — | — | 145.9 |
| | | **TOTAL (9 tools)** | | **18,877** | | **1,659** | **169.4** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 579 | 12,160 | 1,268 | 8.8 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,213 | 25,308 | 603 | 5.2 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,235 | 26,330 | 560 | 3.9 |
| 4 | L1-worker | claudeopus46 | 3,767 | 453 | 4,220 | 341 | 4.1 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,877 | 25,972 | 747 | 5.7 |
| 6 | L1-worker | claudeopus46 | 3,767 | 1,173 | 4,940 | 432 | 4.2 |
| 7 | L1-worker | claudeopus46 | 24,095 | 2,425 | 26,520 | 993 | 9.2 |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,215 | 27,310 | 714 | 5.2 |
| 9 | L1-worker | claudeopus46 | 3,767 | 2,481 | 6,248 | 1,590 | 12.4 |
| 10 | L1-worker | claudeopus46 | 24,095 | 4,445 | 28,540 | 987 | 7.4 |
| 11 | L1-worker | claudeopus46 | 24,095 | 5,267 | 29,362 | 759 | 10.8 |
| 12 | L1-worker | claudeopus46 | 24,095 | 5,924 | 30,019 | 639 | 6.0 |
| 13 | L1-worker | claudeopus46 | 24,095 | 6,670 | 30,765 | 689 | 6.9 |
| 14 | L1-worker | claudeopus46 | 24,095 | 8,237 | 32,332 | 675 | 5.8 |
| 15 | L1-worker | claudeopus46 | 24,095 | 9,873 | 33,968 | 2,109 | 15.8 |
| 16 | L1-worker | claudeopus46 | 24,095 | 14,330 | 38,425 | 3,595 | 21.4 |
| 17 | L1-worker | claudeopus46 | 2,320 | 2,208 | 4,528 | 771 | 5.1 |
| 18 | L1-worker | claudeopus46 | 627 | 2,088 | 2,715 | 676 | 5.3 |
| 19 | L1-worker | claudeopus46 | 2,106 | 3,542 | 5,648 | 926 | 5.3 |
| 20 | L1-worker | claudeopus46 | 366 | 1,208 | 1,574 | 731 | 3.7 |
| 21 | L1-worker | claudeopus46 | 366 | 1,703 | 2,069 | 666 | 3.9 |
| 22 | L1-worker | claudeopus46 | 787 | 12,557 | 13,344 | 500 | 5.9 |
| 23 | L0-main | claudeopus46 | 11,581 | 13,802 | 25,383 | 2,389 | 17.2 |
| 24 | L0-main | claudeopus46 | 2,320 | 2,325 | 4,645 | 800 | 4.4 |
| 25 | L0-main | claudeopus46 | 2,106 | 2,736 | 4,842 | 639 | 5.0 |
| 26 | L0-main | claudeopus46 | 366 | 1,275 | 1,641 | 761 | 3.6 |
| 27 | L0-main | claudeopus46 | 366 | 1,188 | 1,554 | 708 | 3.3 |
| 28 | L0-main | claudeopus46 | 560 | 2,800 | 3,360 | 73 | 2.3 |
| 29 | L0-main | claudeopus46 | 1,156 | 3,579 | 4,735 | 570 | 4.8 |
| 30 | L0-main | claudeopus46 | 560 | 3,259 | 3,819 | 53 | 2.1 |
| 31 | L0-main | claudeopus46 | 560 | 2,631 | 3,191 | 77 | 2.2 |
| 32 | L0-main | claudeopus46 | 1,156 | 4,064 | 5,220 | 579 | 3.3 |

