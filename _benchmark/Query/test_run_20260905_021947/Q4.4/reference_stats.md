# Reference Stats — query-agent

**Run started:** 2026-09-05 05:46:34
**Wall time (at last flush):** 742.7 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 11 | 53,564 | 163,814 | 20,093 | 217,378 | 19,761 | 131.5 | claudeopus46 |
| L1-worker | 53 | 741,073 | 614,485 | 86,697 | 1,355,558 | 25,576 | 658.5 | claudeopus46 |
| **TOTAL** | **64** | **794,637** | **778,299** | **106,790** | **1,572,936** | **24,577** | **790.0** | |

**Estimated tokens:** ~393,234 input + ~26,697 output = ~419,931 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 3 | 2 | 5 | 5 | 193 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 3 | 1 | 3 | 3 | 171 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 10 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 2 | 1 | 3 | 3 | 204 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **19** | **3** | **8** | **4** | **11** | **11** | **568** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (13 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_18 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_31 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_47 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_1061 |  | resolve_compound_ids |
| GLOBcomp_268 |  | resolve_compound_ids |
| GLOBcomp_3089 |  | resolve_compound_ids |
| GLOBcomp_3210 |  | resolve_compound_ids |
| GLOBcomp_3578 |  | resolve_compound_ids |
| GLOBcomp_2105 |  | resolve_compound_ids |
| GLOBcomp_3079 |  | resolve_compound_ids |
| GLOBcomp_4410 |  | resolve_compound_ids |
| GLOBcomp_4541 |  | resolve_compound_ids |

#### References (11 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_8676 |  | search_blocks |
| GLOBlit_9342 |  | search_blocks |
| GLOBlit_9900 |  | search_blocks |
| GLOBlit_11030 |  | search_blocks |
| GLOBlit_11207 |  | search_blocks |
| GLOBlit_2781 |  | search_blocks |
| GLOBlit_5953 |  | search_blocks |
| GLOBlit_11517 |  | search_blocks |
| GLOBlit_8238 |  | search_blocks |
| GLOBlit_8242 |  | search_blocks |
| GLOBlit_9372 |  | search_blocks |

#### Properties (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_4 | Viscosity, Pa*s | search_blocks |

#### Measurements (4 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_140 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_4 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_205 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_142 | Viscosity, Pa*s | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks |

#### Variables (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_2 | Mole fraction | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |
| GLOBvar_1 | Temperature, K | search_blocks |

#### Constraints (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_2 | Temperature, K | search_blocks |
| GLOBconstr_1 | Pressure, kPa | search_blocks |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 13 |
| Unique References | 11 |
| Unique Properties | 1 |
| Unique Measurements | 4 |
| Unique Phases | 1 |
| Unique Variables | 3 |
| Unique Constraints | 2 |
| Total DOIs | 11 |
| Unique parent blocks | 11 |
| Explicit block/subsystem targets | 11 |
| Subsystem targets | 0 |
| Target-matched data points | 568 |

---

## 3. DOI & Block References

**Unique DOIs:** 11  |  **Parent blocks:** 11  |  **Explicit targets:** 11  |  **Subsystems:** 0  |  **Target-matched datapoints:** 568

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.jct.2006.12.012 | 1 | 120 | binary | search_blocks |
| 10.1016/j.tca.2011.08.013 | 1 | 16 | binary | search_blocks |
| 10.1021/je034073k | 1 | 65 | binary | search_blocks |
| 10.1021/je0340809 | 1 | 95 | binary | search_blocks |
| 10.1021/je050209y | 1 | 11 | binary | search_blocks |
| 10.1021/je1008813 | 1 | 16 | binary | search_blocks |
| 10.1021/je100967k | 1 | 44 | binary | search_blocks |
| 10.1021/je300608v | 1 | 60 | binary | search_blocks |
| 10.1021/je700671t | 1 | 98 | binary | search_blocks |
| 10.1021/je800330d | 1 | 8 | binary | search_blocks |
| 10.1021/je9001027 | 1 | 35 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.jct.2006.12.012 | PROPblock_3 | declared | 120 | binary | — | search_blocks |
| 10.1016/j.tca.2011.08.013 | PROPblock_10 | declared | 16 | binary | — | search_blocks |
| 10.1021/je034073k | PROPblock_3 | declared | 65 | binary | — | search_blocks |
| 10.1021/je0340809 | PROPblock_17 | declared | 95 | binary | — | search_blocks |
| 10.1021/je050209y | PROPblock_9 | declared | 11 | binary | — | search_blocks |
| 10.1021/je1008813 | PROPblock_3 | declared | 16 | binary | — | search_blocks |
| 10.1021/je100967k | PROPblock_17 | declared | 44 | binary | — | search_blocks |
| 10.1021/je300608v | PROPblock_3 | declared | 60 | binary | — | search_blocks |
| 10.1021/je700671t | PROPblock_3 | declared | 98 | binary | — | search_blocks |
| 10.1021/je800330d | PROPblock_3 | declared | 8 | binary | — | search_blocks |
| 10.1021/je9001027 | PROPblock_3 | declared | 35 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve DMF and wat… | 206 | KEEP ←in 295 | 206 | 3.8 |
| 2 | 3 | `search_blocks` | compound=['GLOBcomp_18', 'GLOBcomp_1'], limit=50, … | 1,293 | KEEP ←in 7,112 | 1293 | 20.9 |
| 3 | 4 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_11030… | 372 | — | — | 0.1 |
| 4 | 5 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_11030… | 312 | — | — | 0.0 |
| 5 | 6 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_11030… | 377 | — | — | 0.1 |
| 6 | 7 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_11030… | 378 | — | — | 0.1 |
| 7 | 8 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_11030… | 1,271 | — | — | 0.1 |
| 8 | 1 | `L1_query` | context=User wants to find DMF substi…, id_catalog… | 37,839 | — | — | 210.0 |
| 9 | 2 | `resolve_compound_ids` | limit=10, min_score=50, purpose=Resolve DMSO compo… | 274 | KEEP ←in 239 | 274 | 4.4 |
| 10 | 3 | `search_blocks` | compound=['GLOBcomp_31', 'GLOBcomp_1'], limit=50, … | 1,450 | KEEP ←in 7,090 | 1450 | 22.3 |
| 11 | 4 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_2781,… | 261 | — | — | 0.0 |
| 12 | 5 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_2781,… | 384 | — | — | 0.2 |
| 13 | 6 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_2781,… | 1,311 | — | — | 0.2 |
| 14 | 2 | `L1_query` | context=User is looking for DMF subst…, id_catalog… | 25,401 | — | — | 185.6 |
| 15 | 2 | `resolve_compound_ids` | limit=10, min_score=50, purpose=Resolve NMP compou… | 217 | KEEP ←in 1,125 | 217 | 5.5 |
| 16 | 3 | `search_blocks` | compound=['GLOBcomp_47', 'GLOBcomp_1'], limit=50, … | 1,307 | KEEP ←in 7,956 | 1307 | 23.6 |
| 17 | 4 | `inspect_block_table` | block_number=PROPblock_17, literature=GLOBlit_8242… | 256 | — | — | 0.0 |
| 18 | 5 | `inspect_block_table` | block_number=PROPblock_17, literature=GLOBlit_8242… | 377 | — | — | 0.2 |
| 19 | 6 | `inspect_block_table` | block_number=PROPblock_17, literature=GLOBlit_8242… | 1,241 | — | — | 0.4 |
| 20 | 3 | `L1_query` | context=User is looking for DMF subst…, id_catalog… | 29,623 | — | — | 224.9 |
| | | **TOTAL (20 tools)** | | **104,150** | | **4,747** | **702.4** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 589 | 12,170 | 1,731 | 11.0 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,047 | 25,142 | 633 | 4.8 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,068 | 26,163 | 571 | 4.3 |
| 4 | L1-worker | claudeopus46 | 3,767 | 446 | 4,213 | 338 | 3.7 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,701 | 25,796 | 788 | 5.8 |
| 6 | L1-worker | claudeopus46 | 3,767 | 7,568 | 11,335 | 1,627 | 14.0 |
| 7 | L1-worker | claudeopus46 | 24,095 | 3,319 | 27,414 | 969 | 7.6 |
| 8 | L1-worker | claudeopus46 | 24,095 | 4,071 | 28,166 | 865 | 6.7 |
| 9 | L1-worker | claudeopus46 | 24,095 | 4,777 | 28,872 | 644 | 6.5 |
| 10 | L1-worker | claudeopus46 | 24,095 | 5,501 | 29,596 | 995 | 7.5 |
| 11 | L1-worker | claudeopus46 | 24,095 | 6,235 | 30,330 | 1,290 | 10.1 |
| 12 | L1-worker | claudeopus46 | 24,095 | 7,864 | 31,959 | 3,241 | 26.5 |
| 13 | L1-worker | claudeopus46 | 24,095 | 17,025 | 41,120 | 4,972 | 35.4 |
| 14 | L1-worker | claudeopus46 | 24,095 | 27,439 | 51,534 | 5,506 | 39.9 |
| 15 | L1-worker | claudeopus46 | 627 | 3,868 | 4,495 | 988 | 8.3 |
| 16 | L1-worker | claudeopus46 | 2,106 | 5,156 | 7,262 | 2,158 | 10.6 |
| 17 | L1-worker | claudeopus46 | 2,320 | 3,988 | 6,308 | 1,285 | 13.8 |
| 18 | L1-worker | claudeopus46 | 366 | 2,935 | 3,301 | 1,580 | 6.6 |
| 19 | L1-worker | claudeopus46 | 366 | 1,722 | 2,088 | 1,235 | 4.7 |
| 20 | L1-worker | claudeopus46 | 787 | 39,197 | 39,984 | 890 | 9.0 |
| 21 | L0-main | claudeopus46 | 11,581 | 22,989 | 34,570 | 1,602 | 13.3 |
| 22 | L1-worker | claudeopus46 | 24,095 | 9,347 | 33,442 | 592 | 6.3 |
| 23 | L1-worker | claudeopus46 | 24,095 | 10,346 | 34,441 | 560 | 4.6 |
| 24 | L1-worker | claudeopus46 | 3,767 | 381 | 4,148 | 390 | 4.2 |
| 25 | L1-worker | claudeopus46 | 24,095 | 10,068 | 34,163 | 722 | 7.0 |
| 26 | L1-worker | claudeopus46 | 3,767 | 7,568 | 11,335 | 1,686 | 16.0 |
| 27 | L1-worker | claudeopus46 | 24,095 | 11,813 | 35,908 | 815 | 9.9 |
| 28 | L1-worker | claudeopus46 | 24,095 | 12,441 | 36,536 | 607 | 5.7 |
| 29 | L1-worker | claudeopus46 | 24,095 | 13,162 | 37,257 | 741 | 6.6 |
| 30 | L1-worker | claudeopus46 | 24,095 | 14,869 | 38,964 | 3,570 | 25.3 |
| 31 | L1-worker | claudeopus46 | 24,095 | 24,529 | 48,624 | 4,781 | 37.3 |
| 32 | L1-worker | claudeopus46 | 24,095 | 35,473 | 59,568 | 4,563 | 33.8 |
| 33 | L1-worker | claudeopus46 | 2,106 | 4,810 | 6,916 | 1,256 | 6.8 |
| 34 | L1-worker | claudeopus46 | 2,320 | 3,362 | 5,682 | 1,110 | 6.9 |
| 35 | L1-worker | claudeopus46 | 627 | 3,242 | 3,869 | 947 | 7.1 |
| 36 | L1-worker | claudeopus46 | 366 | 1,547 | 1,913 | 1,065 | 4.0 |
| 37 | L1-worker | claudeopus46 | 366 | 2,033 | 2,399 | 902 | 4.4 |
| 38 | L1-worker | claudeopus46 | 787 | 26,101 | 26,888 | 741 | 8.4 |
| 39 | L0-main | claudeopus46 | 11,581 | 40,747 | 52,328 | 1,564 | 14.4 |
| 40 | L1-worker | claudeopus46 | 24,095 | 16,145 | 40,240 | 671 | 7.4 |
| 41 | L1-worker | claudeopus46 | 24,095 | 17,221 | 41,316 | 596 | 4.6 |
| 42 | L1-worker | claudeopus46 | 3,767 | 1,303 | 5,070 | 453 | 4.7 |
| 43 | L1-worker | claudeopus46 | 24,095 | 16,783 | 40,878 | 598 | 5.5 |
| 44 | L1-worker | claudeopus46 | 3,767 | 8,356 | 12,123 | 1,766 | 16.3 |
| 45 | L1-worker | claudeopus46 | 24,095 | 18,414 | 42,509 | 1,162 | 12.3 |
| 46 | L1-worker | claudeopus46 | 24,095 | 19,046 | 43,141 | 660 | 5.3 |
| 47 | L1-worker | claudeopus46 | 24,095 | 19,768 | 43,863 | 1,064 | 8.9 |
| 48 | L1-worker | claudeopus46 | 24,095 | 21,406 | 45,501 | 4,733 | 36.0 |
| 49 | L1-worker | claudeopus46 | 24,095 | 32,134 | 56,229 | 6,032 | 43.6 |
| 50 | L1-worker | claudeopus46 | 24,095 | 43,952 | 68,047 | 6,611 | 44.8 |
| 51 | L1-worker | claudeopus46 | 2,106 | 9,128 | 11,234 | 1,700 | 9.1 |
| 52 | L1-worker | claudeopus46 | 2,320 | 7,637 | 9,957 | 1,010 | 9.7 |
| 53 | L1-worker | claudeopus46 | 627 | 7,517 | 8,144 | 986 | 10.7 |
| 54 | L1-worker | claudeopus46 | 366 | 2,477 | 2,843 | 989 | 4.4 |
| 55 | L1-worker | claudeopus46 | 366 | 1,447 | 1,813 | 965 | 4.2 |
| 56 | L1-worker | claudeopus46 | 787 | 34,732 | 35,519 | 1,078 | 10.9 |
| 57 | L0-main | claudeopus46 | 11,581 | 65,342 | 76,923 | 6,537 | 45.7 |
| 58 | L0-main | claudeopus46 | 2,106 | 6,320 | 8,426 | 1,005 | 6.7 |
| 59 | L0-main | claudeopus46 | 2,320 | 5,899 | 8,219 | 1,765 | 10.9 |
| 60 | L0-main | claudeopus46 | 366 | 1,554 | 1,920 | 1,152 | 5.0 |
| 61 | L0-main | claudeopus46 | 366 | 2,240 | 2,606 | 1,706 | 7.1 |
| 62 | L0-main | claudeopus46 | 560 | 6,938 | 7,498 | 257 | 2.6 |
| 63 | L0-main | claudeopus46 | 1,156 | 9,110 | 10,266 | 1,393 | 9.1 |
| 64 | L0-main | claudeopus46 | 366 | 2,086 | 2,452 | 1,381 | 5.7 |

