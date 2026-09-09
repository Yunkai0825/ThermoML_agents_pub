# Reference Stats — query-agent

**Run started:** 2026-09-05 05:02:27
**Wall time (at last flush):** 655.3 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 10 | 41,983 | 124,752 | 28,026 | 166,735 | 16,673 | 169.9 | claudeopus46 |
| L1-worker | 40 | 538,706 | 430,515 | 69,451 | 969,221 | 24,230 | 499.8 | claudeopus46 |
| verdict | 1 | 972 | 13,291 | 1,104 | 14,263 | 14,263 | 10.3 | claudeopus46 |
| **TOTAL** | **51** | **581,661** | **568,558** | **98,581** | **1,150,219** | **22,553** | **680.0** | |

**Estimated tokens:** ~287,554 input + ~24,645 output = ~312,199 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 5 | 3 | 16 | 17 | 1,379 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 5 | 3 | 16 | 17 | 1,379 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 5 | 3 | 16 | 17 | 1,379 |
| `search_system_registry` | 2 | 1 | 5 | 2 | 13 | 14 | 1,346 |
| **TOTAL** | **10** | **4** | **20** | **11** | **61** | **65** | **5,483** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks, search_system_registry |
| GLOBcomp_5 |  | resolve_compound_ids, search_blocks, search_system_registry |

#### References (16 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_555 |  | search_blocks, search_system_registry |
| GLOBlit_590 |  | search_blocks, search_system_registry |
| GLOBlit_2432 |  | search_blocks, search_system_registry |
| GLOBlit_2979 |  | search_blocks, search_system_registry |
| GLOBlit_4068 |  | search_blocks, search_system_registry |
| GLOBlit_4415 |  | search_blocks, search_system_registry |
| GLOBlit_5585 |  | search_blocks, search_system_registry |
| GLOBlit_7085 |  | search_blocks, search_system_registry |
| GLOBlit_7178 |  | search_blocks, search_system_registry |
| GLOBlit_8254 |  | search_blocks, search_system_registry |
| GLOBlit_8447 |  | search_blocks |
| GLOBlit_8888 |  | search_blocks |
| GLOBlit_10159 |  | search_blocks, search_system_registry |
| GLOBlit_11042 |  | search_blocks |
| GLOBlit_11142 |  | search_blocks, search_system_registry |
| GLOBlit_11872 |  | search_blocks, search_system_registry |

#### Properties (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_1 | Mass density, kg/m3 | search_blocks, search_system_registry |

#### Measurements (7 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_153 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_66 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_6 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_170 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_143 | Mass density, kg/m3 | search_blocks, search_system_registry |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks, search_system_registry |

#### Variables (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | search_blocks, search_system_registry |
| GLOBvar_5 | Mass fraction | search_blocks, search_system_registry |
| GLOBvar_3 | Pressure, kPa | search_blocks, search_system_registry |
| GLOBvar_4 | Molality, mol/kg | search_blocks, search_system_registry |
| GLOBvar_2 | Mole fraction | search_blocks, search_system_registry |

#### Constraints (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | search_blocks, search_system_registry |
| GLOBconstr_8 | Molality, mol/kg | search_blocks, search_system_registry |
| GLOBconstr_2 | Temperature, K | search_blocks |

#### Solvents (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | search_blocks, search_system_registry |
| GLOBsolvent_9 |  | search_blocks |

#### Block_Types (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | search_system_registry |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 2 |
| Unique References | 16 |
| Unique Properties | 1 |
| Unique Measurements | 7 |
| Unique Phases | 1 |
| Unique Variables | 5 |
| Unique Constraints | 3 |
| Unique Solvents | 2 |
| Unique Block_Types | 1 |
| Total DOIs | 16 |
| Unique parent blocks | 17 |
| Explicit block/subsystem targets | 17 |
| Subsystem targets | 0 |
| Target-matched data points | 5,483 |

---

## 3. DOI & Block References

**Unique DOIs:** 16  |  **Parent blocks:** 17  |  **Explicit targets:** 17  |  **Subsystems:** 0  |  **Target-matched datapoints:** 1,379

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2007.07.066 | 1 | 15 | binary | search_blocks, search_system_registry |
| 10.1016/j.fluid.2008.01.004 | 1 | 15 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2004.07.019 | 1 | 456 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2008.07.005 | 1 | 96 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2013.11.036 | 2 | 203 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2015.06.024 | 1 | 40 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2019.105880 | 1 | 16 | binary | search_blocks, search_system_registry |
| 10.1021/acs.jced.6b01058 | 1 | 12 | binary | search_blocks, search_system_registry |
| 10.1021/acs.jced.7b00299 | 1 | 2 | binary | search_blocks, search_system_registry |
| 10.1021/je034101z | 1 | 380 | binary | search_blocks, search_system_registry |
| 10.1021/je049738c | 1 | 8 | binary | search_blocks |
| 10.1021/je0601098 | 1 | 12 | binary | search_blocks |
| 10.1021/je4003515 | 1 | 25 | binary | search_blocks, search_system_registry |
| 10.1021/je700700f | 1 | 13 | binary | search_blocks |
| 10.1021/je800158z | 1 | 56 | binary | search_blocks, search_system_registry |
| 10.1021/je900966r | 1 | 30 | binary | search_blocks, search_system_registry |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2007.07.066 | PROPblock_8 | declared | 15 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2008.01.004 | PROPblock_5 | declared | 15 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2004.07.019 | PROPblock_3 | declared | 456 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2008.07.005 | PROPblock_9 | declared | 96 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2013.11.036 | PROPblock_1 | declared | 174 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2013.11.036 | PROPblock_2 | declared | 29 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2015.06.024 | PROPblock_5 | declared | 40 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2019.105880 | PROPblock_7 | declared | 16 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.6b01058 | PROPblock_8 | declared | 12 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.7b00299 | PROPblock_13 | declared | 2 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je034101z | PROPblock_6 | declared | 380 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je049738c | PROPblock_26 | declared | 8 | binary | — | search_blocks |
| 10.1021/je0601098 | PROPblock_22 | declared | 12 | binary | — | search_blocks |
| 10.1021/je4003515 | PROPblock_10 | declared | 25 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je700700f | PROPblock_14 | declared | 13 | binary | — | search_blocks |
| 10.1021/je800158z | PROPblock_3 | declared | 56 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je900966r | PROPblock_4 | declared | 30 | binary | 2 | search_blocks, search_system_registry |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve compound ID… | 198 | KEEP ←in 283 | 198 | 4.8 |
| 2 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_5'], limit=50, p… | 784 | KEEP ←in 11,346 | 766 | 21.7 |
| 3 | 5 | `inspect_block_table` | block_number=PROPblock_8, literature=GLOBlit_555, … | 249 | — | — | 0.1 |
| 4 | 6 | `inspect_block_table` | block_number=PROPblock_8, literature=GLOBlit_555, … | 379 | — | — | 0.2 |
| 5 | 7 | `inspect_block_table` | block_number=PROPblock_8, literature=GLOBlit_555, … | 980 | — | — | 0.1 |
| 6 | 8 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_5'], limit=50, p… | 1,179 | KEEP ←in 11,346 | 1164 | 20.8 |
| 7 | 9 | `inspect_block_table` | block_number=PROPblock_9, literature=GLOBlit_2979,… | 1,118 | — | — | 0.1 |
| 8 | 1 | `L1_query` | context=User wants to know what densi…, id_catalog… | 28,253 | — | — | 257.0 |
| 9 | 1 | `inspect_block_table` | block_number=PROPblock_5, literature=GLOBlit_590, … | 249 | — | — | 0.0 |
| 10 | 2 | `inspect_block_table` | block_number=PROPblock_5, literature=GLOBlit_590, … | 379 | — | — | 0.2 |
| 11 | 3 | `inspect_block_table` | block_number=PROPblock_5, literature=GLOBlit_590, … | 1,125 | — | — | 0.2 |
| 12 | 5 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_5'], limit=50, p… | 1,186 | KEEP ←in 11,346 | 1186 | 22.7 |
| 13 | 6 | `search_system_registry` | compound=['GLOBcomp_1', 'GLOBcomp_5'], limit=50, p… | 1,214 | KEEP ←in 2,231 | 1019 | 17.9 |
| 14 | 2 | `L1_query` | context=Previous search found 17 bloc…, id_catalog… | 82,686 | — | — | 227.7 |
| | | **TOTAL (14 tools)** | | **119,979** | | **4,333** | **573.5** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 1,037 | 12,618 | 1,220 | 8.3 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,240 | 25,335 | 564 | 4.9 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,258 | 26,353 | 545 | 4.3 |
| 4 | L1-worker | claudeopus46 | 3,767 | 442 | 4,209 | 376 | 4.7 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,867 | 25,962 | 749 | 6.1 |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,560 | 26,655 | 659 | 5.5 |
| 7 | L1-worker | claudeopus46 | 3,767 | 11,815 | 15,582 | 1,699 | 15.0 |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,323 | 27,418 | 2,764 | 18.7 |
| 9 | L1-worker | claudeopus46 | 24,095 | 3,951 | 28,046 | 707 | 6.3 |
| 10 | L1-worker | claudeopus46 | 24,095 | 4,655 | 28,750 | 1,439 | 10.3 |
| 11 | L1-worker | claudeopus46 | 24,095 | 5,982 | 30,077 | 1,333 | 11.1 |
| 12 | L1-worker | claudeopus46 | 3,767 | 11,800 | 15,567 | 1,495 | 15.0 |
| 13 | L1-worker | claudeopus46 | 24,095 | 7,592 | 31,687 | 1,093 | 8.8 |
| 14 | L1-worker | claudeopus46 | 24,095 | 9,089 | 33,184 | 4,910 | 35.4 |
| 15 | L1-worker | claudeopus46 | 24,095 | 21,125 | 45,220 | 6,373 | 43.8 |
| 16 | L1-worker | claudeopus46 | 24,095 | 30,815 | 54,910 | 3,749 | 28.4 |
| 17 | L1-worker | claudeopus46 | 2,320 | 4,100 | 6,420 | 1,018 | 7.8 |
| 18 | L1-worker | claudeopus46 | 627 | 3,980 | 4,607 | 1,348 | 9.9 |
| 19 | L1-worker | claudeopus46 | 2,106 | 5,461 | 7,567 | 1,961 | 10.1 |
| 20 | L1-worker | claudeopus46 | 366 | 1,455 | 1,821 | 983 | 4.6 |
| 21 | L1-worker | claudeopus46 | 366 | 1,759 | 2,125 | 1,335 | 5.6 |
| 22 | L1-worker | claudeopus46 | 366 | 2,738 | 3,104 | 1,174 | 5.6 |
| 23 | L1-worker | claudeopus46 | 787 | 28,242 | 29,029 | 634 | 7.2 |
| 24 | L0-main | claudeopus46 | 11,581 | 21,959 | 33,540 | 1,923 | 15.7 |
| 25 | L1-worker | claudeopus46 | 24,095 | 9,603 | 33,698 | 802 | 8.0 |
| 26 | L1-worker | claudeopus46 | 24,095 | 10,200 | 34,295 | 685 | 4.8 |
| 27 | L1-worker | claudeopus46 | 24,095 | 10,929 | 35,024 | 733 | 12.5 |
| 28 | L1-worker | claudeopus46 | 24,095 | 12,369 | 36,464 | 811 | 7.3 |
| 29 | L1-worker | claudeopus46 | 24,095 | 13,134 | 37,229 | 650 | 5.9 |
| 30 | L1-worker | claudeopus46 | 3,767 | 11,839 | 15,606 | 1,555 | 15.3 |
| 31 | L1-worker | claudeopus46 | 24,095 | 14,272 | 38,367 | 972 | 7.4 |
| 32 | L1-worker | claudeopus46 | 3,767 | 2,765 | 6,532 | 1,685 | 12.8 |
| 33 | L1-worker | claudeopus46 | 24,095 | 15,844 | 39,939 | 5,027 | 33.9 |
| 34 | L1-worker | claudeopus46 | 24,095 | 26,883 | 50,978 | 5,496 | 38.1 |
| 35 | L1-worker | claudeopus46 | 24,095 | 36,068 | 60,163 | 3,686 | 28.2 |
| 36 | L1-worker | claudeopus46 | 2,320 | 2,914 | 5,234 | 588 | 5.1 |
| 37 | L1-worker | claudeopus46 | 627 | 2,794 | 3,421 | 754 | 6.4 |
| 38 | L1-worker | claudeopus46 | 366 | 1,025 | 1,391 | 558 | 3.1 |
| 39 | L1-worker | claudeopus46 | 366 | 1,165 | 1,531 | 741 | 4.3 |
| 40 | L1-worker | claudeopus46 | 2,106 | 4,640 | 6,746 | 4,040 | 16.2 |
| 41 | L1-worker | claudeopus46 | 366 | 4,817 | 5,183 | 3,245 | 13.9 |
| 42 | L1-worker | claudeopus46 | 787 | 83,005 | 83,792 | 515 | 7.5 |
| 43 | L0-main | claudeopus46 | 11,581 | 52,243 | 63,824 | 8,009 | 57.3 |
| 44 | L0-main | claudeopus46 | 2,320 | 5,589 | 7,909 | 1,045 | 7.2 |
| 45 | L0-main | claudeopus46 | 366 | 1,520 | 1,886 | 1,001 | 3.7 |
| 46 | L0-main | claudeopus46 | 2,106 | 6,458 | 8,564 | 1,794 | 11.3 |
| 47 | L0-main | claudeopus46 | 366 | 2,343 | 2,709 | 2,809 | 10.4 |
| 48 | L0-main | claudeopus46 | 560 | 9,355 | 9,915 | 747 | 6.1 |
| 49 | L0-main | claudeopus46 | 1,156 | 18,429 | 19,585 | 5,126 | 28.9 |
| 50 | L0-main | claudeopus46 | 366 | 5,819 | 6,185 | 4,352 | 21.0 |
| 51 | verdict | claudeopus46 | 972 | 13,291 | 14,263 | 1,104 | 10.3 |

