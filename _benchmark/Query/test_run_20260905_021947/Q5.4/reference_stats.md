# Reference Stats — query-agent

**Run started:** 2026-09-05 06:00:33
**Wall time (at last flush):** 373.6 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 14 | 33,410 | 67,463 | 15,598 | 100,873 | 7,205 | 103.8 | claudeopus46 |
| L1-worker | 28 | 373,972 | 207,605 | 38,151 | 581,577 | 20,770 | 287.1 | claudeopus46 |
| **TOTAL** | **42** | **407,382** | **275,068** | **53,749** | **682,450** | **16,248** | **390.9** | |

**Estimated tokens:** ~170,612 input + ~13,437 output = ~184,049 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 10 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 10 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 10 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 9 | 1 | 3 | 2 | 12 | 16 | 924 |
| `search_blocks` | 3 | 1 | 3 | 1 | 3 | 5 | 209 |
| `search_blocks` | 1 | 1 | 2 | 0 | 1 | 1 | 1 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **43** | **3** | **8** | **3** | **16** | **22** | **1,134** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (30 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_181 |  | resolve_compound_ids |
| GLOBcomp_239 |  | resolve_compound_ids |
| GLOBcomp_792 |  | resolve_compound_ids |
| GLOBcomp_1029 |  | resolve_compound_ids |
| GLOBcomp_2012 |  | resolve_compound_ids |
| GLOBcomp_2567 |  | resolve_compound_ids |
| GLOBcomp_2947 |  | resolve_compound_ids |
| GLOBcomp_3552 |  | resolve_compound_ids |
| GLOBcomp_3627 |  | resolve_compound_ids |
| GLOBcomp_5371 |  | resolve_compound_ids |
| GLOBcomp_7 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_20 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_29 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_3075 |  | resolve_compound_ids |
| GLOBcomp_2921 |  | resolve_compound_ids |
| GLOBcomp_380 |  | resolve_compound_ids |
| GLOBcomp_3193 |  | resolve_compound_ids |
| GLOBcomp_785 |  | resolve_compound_ids |
| GLOBcomp_1269 |  | resolve_compound_ids |
| GLOBcomp_3478 |  | resolve_compound_ids |
| GLOBcomp_44 |  | resolve_compound_ids |
| GLOBcomp_3762 |  | resolve_compound_ids |
| GLOBcomp_274 | 1,3-butanediol | search_blocks |
| GLOBcomp_1145 | 2-methylheptane | search_blocks |
| GLOBcomp_13 | cyclohexane | search_blocks |
| GLOBcomp_309 | 1,2,4-trimethylbenzene | search_blocks |
| GLOBcomp_31 | dimethyl sulfoxide | search_blocks |
| GLOBcomp_580 | benzylamine | search_blocks |
| GLOBcomp_43 | dodecane | search_blocks |
| GLOBcomp_45 | hex-1-ene | search_blocks |

#### References (12 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_2451 |  | search_blocks |
| GLOBlit_2822 |  | search_blocks |
| GLOBlit_3448 |  | search_blocks |
| GLOBlit_3982 |  | search_blocks |
| GLOBlit_4104 |  | search_blocks |
| GLOBlit_4977 |  | search_blocks |
| GLOBlit_5226 |  | search_blocks |
| GLOBlit_5731 |  | search_blocks |
| GLOBlit_6198 |  | search_blocks |
| GLOBlit_8447 |  | search_blocks |
| GLOBlit_8468 |  | search_blocks |
| GLOBlit_10053 |  | search_blocks |

#### Properties (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_9 | Molar heat capacity at constant pressure, J/K/mol | search_blocks |

#### Measurements (4 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_31 | Molar heat capacity at constant pressure, J/K/mol | search_blocks |
| GLOBmeas_300 | Molar heat capacity at constant pressure, J/K/mol | search_blocks |
| GLOBmeas_12 | Molar heat capacity at constant pressure, J/K/mol | search_blocks |
| GLOBmeas_9 | Molar heat capacity at constant pressure, J/K/mol | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks |

#### Variables (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_2 | Mole fraction | search_blocks |
| GLOBvar_3 | Pressure, kPa | search_blocks |

#### Constraints (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | search_blocks |
| GLOBconstr_2 | Temperature, K | search_blocks |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 30 |
| Unique References | 12 |
| Unique Properties | 1 |
| Unique Measurements | 4 |
| Unique Phases | 1 |
| Unique Variables | 3 |
| Unique Constraints | 2 |
| Total DOIs | 12 |
| Unique parent blocks | 22 |
| Explicit block/subsystem targets | 22 |
| Subsystem targets | 0 |
| Target-matched data points | 1,134 |

---

## 3. DOI & Block References

**Unique DOIs:** 12  |  **Parent blocks:** 22  |  **Explicit targets:** 22  |  **Subsystems:** 0  |  **Target-matched datapoints:** 1,134

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.jct.2004.09.007 | 2 | 261 | binary, unary | search_blocks |
| 10.1016/j.jct.2007.04.011 | 1 | 13 | unary | search_blocks |
| 10.1016/j.jct.2011.08.012 | 2 | 132 | binary, unary | search_blocks |
| 10.1016/j.jct.2013.08.033 | 1 | 8 | unary | search_blocks |
| 10.1016/j.jct.2014.01.020 | 1 | 115 | binary | search_blocks |
| 10.1016/j.jct.2017.03.006 | 3 | 240 | binary, unary | search_blocks |
| 10.1016/j.jct.2018.03.031 | 1 | 12 | unary | search_blocks |
| 10.1016/j.tca.2006.10.025 | 2 | 20 | binary, unary | search_blocks |
| 10.1016/j.tca.2014.10.018 | 2 | 44 | binary, unary | search_blocks |
| 10.1021/je049738c | 3 | 3 | unary | search_blocks |
| 10.1021/je0497810 | 3 | 166 | binary, unary | search_blocks |
| 10.1021/je301301j | 1 | 120 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.jct.2004.09.007 | PROPblock_2 | declared | 29 | unary | — | search_blocks |
| 10.1016/j.jct.2004.09.007 | PROPblock_5 | declared | 232 | binary | — | search_blocks |
| 10.1016/j.jct.2007.04.011 | PROPblock_1 | declared | 13 | unary | — | search_blocks |
| 10.1016/j.jct.2011.08.012 | PROPblock_3 | declared | 24 | unary | — | search_blocks |
| 10.1016/j.jct.2011.08.012 | PROPblock_6 | declared | 108 | binary | — | search_blocks |
| 10.1016/j.jct.2013.08.033 | PROPblock_4 | declared | 8 | unary | — | search_blocks |
| 10.1016/j.jct.2014.01.020 | PROPblock_6 | declared | 115 | binary | — | search_blocks |
| 10.1016/j.jct.2017.03.006 | PROPblock_10 | declared | 108 | binary | — | search_blocks |
| 10.1016/j.jct.2017.03.006 | PROPblock_13 | declared | 120 | binary | — | search_blocks |
| 10.1016/j.jct.2017.03.006 | PROPblock_3 | declared | 12 | unary | — | search_blocks |
| 10.1016/j.jct.2018.03.031 | PROPblock_25 | declared | 12 | unary | — | search_blocks |
| 10.1016/j.tca.2006.10.025 | PROPblock_10 | declared | 8 | unary | — | search_blocks |
| 10.1016/j.tca.2006.10.025 | PROPblock_23 | declared | 12 | binary | — | search_blocks |
| 10.1016/j.tca.2014.10.018 | PROPblock_6 | declared | 4 | unary | — | search_blocks |
| 10.1016/j.tca.2014.10.018 | PROPblock_9 | declared | 40 | binary | — | search_blocks |
| 10.1021/je049738c | PROPblock_5 | declared | 1 | unary | — | search_blocks |
| 10.1021/je049738c | PROPblock_7 | declared | 1 | unary | — | search_blocks |
| 10.1021/je049738c | PROPblock_9 | declared | 1 | unary | — | search_blocks |
| 10.1021/je0497810 | PROPblock_12 | declared | 84 | binary | — | search_blocks |
| 10.1021/je0497810 | PROPblock_3 | declared | 4 | unary | — | search_blocks |
| 10.1021/je0497810 | PROPblock_9 | declared | 78 | binary | — | search_blocks |
| 10.1021/je301301j | PROPblock_7 | declared | 120 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=10, min_score=50, purpose=Resolve butanol is… | 846 | DISCARD ←in 983 | 781 | 13.6 |
| 2 | 3 | `resolve_compound_ids` | limit=10, min_score=50, purpose=Resolve butanol is… | 774 | KEEP ←in 967 | 774 | 10.8 |
| 3 | 4 | `resolve_compound_ids` | limit=10, min_score=50, purpose=Find tert-butanol … | 361 | KEEP ←in 1,100 | 361 | 7.4 |
| 4 | 5 | `search_blocks` | compound=['GLOBcomp_7', 'GLOBcomp_20',…, limit=50,… | 850 | DISCARD ←in 39 | 792 | 10.4 |
| 5 | 6 | `search_blocks` | compound=['GLOBcomp_7'], limit=20, property=GLOBpr… | 1,102 | KEEP ←in 10,233 | 1087 | 16.6 |
| 6 | 7 | `search_blocks` | compound=['GLOBcomp_20'], limit=20, property=GLOBp… | 1,217 | KEEP ←in 9,330 | 1217 | 21.7 |
| 7 | 8 | `search_blocks` | compound=['GLOBcomp_29'], limit=20, property=GLOBp… | 741 | KEEP ←in 1,428 | 726 | 9.0 |
| 8 | 9 | `search_blocks` | compound=['GLOBcomp_44'], limit=20, property=GLOBp… | 832 | DISCARD ←in 39 | 774 | 9.5 |
| 9 | 10 | `inspect_block_table` | block_number=PROPblock_2, literature=GLOBlit_2451,… | 1,276 | — | — | 0.1 |
| 10 | 12 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_4977,… | 1,049 | — | — | 0.1 |
| 11 | 1 | `L1_query` | context=, id_catalog=, instruction=Search for heat… | 27,007 | — | — | 278.4 |
| | | **TOTAL (11 tools)** | | **36,055** | | **6,512** | **377.6** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 510 | 12,091 | 1,154 | 7.8 |
| 2 | L1-worker | claudeopus46 | 24,095 | 964 | 25,059 | 738 | 5.8 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,036 | 26,131 | 585 | 4.2 |
| 4 | L1-worker | claudeopus46 | 3,767 | 1,151 | 4,918 | 1,605 | 13.0 |
| 5 | L1-worker | claudeopus46 | 24,095 | 2,237 | 26,332 | 718 | 5.3 |
| 6 | L1-worker | claudeopus46 | 3,767 | 1,157 | 4,924 | 1,448 | 10.3 |
| 7 | L1-worker | claudeopus46 | 24,095 | 3,263 | 27,358 | 830 | 6.2 |
| 8 | L1-worker | claudeopus46 | 3,767 | 1,249 | 5,016 | 659 | 6.9 |
| 9 | L1-worker | claudeopus46 | 24,095 | 3,995 | 28,090 | 1,044 | 6.8 |
| 10 | L1-worker | claudeopus46 | 3,767 | 478 | 4,245 | 1,368 | 9.7 |
| 11 | L1-worker | claudeopus46 | 24,095 | 5,232 | 29,327 | 718 | 6.1 |
| 12 | L1-worker | claudeopus46 | 3,767 | 10,564 | 14,331 | 1,457 | 15.5 |
| 13 | L1-worker | claudeopus46 | 24,095 | 6,666 | 30,761 | 760 | 5.9 |
| 14 | L1-worker | claudeopus46 | 3,767 | 9,639 | 13,406 | 1,581 | 14.2 |
| 15 | L1-worker | claudeopus46 | 24,095 | 8,221 | 32,316 | 761 | 5.8 |
| 16 | L1-worker | claudeopus46 | 3,767 | 1,761 | 5,528 | 1,015 | 8.3 |
| 17 | L1-worker | claudeopus46 | 24,095 | 9,309 | 33,404 | 610 | 4.7 |
| 18 | L1-worker | claudeopus46 | 3,767 | 410 | 4,177 | 1,110 | 8.2 |
| 19 | L1-worker | claudeopus46 | 24,095 | 10,489 | 34,584 | 794 | 7.2 |
| 20 | L1-worker | claudeopus46 | 24,095 | 12,088 | 36,183 | 4,029 | 29.0 |
| 21 | L1-worker | claudeopus46 | 24,095 | 22,550 | 46,645 | 1,503 | 11.5 |
| 22 | L1-worker | claudeopus46 | 24,062 | 23,734 | 47,796 | 3,904 | 28.2 |
| 23 | L1-worker | claudeopus46 | 24,062 | 26,579 | 50,641 | 3,399 | 24.6 |
| 24 | L1-worker | claudeopus46 | 2,320 | 4,372 | 6,692 | 1,044 | 7.9 |
| 25 | L1-worker | claudeopus46 | 2,106 | 5,457 | 7,563 | 1,967 | 10.3 |
| 26 | L1-worker | claudeopus46 | 627 | 4,252 | 4,879 | 1,230 | 11.9 |
| 27 | L1-worker | claudeopus46 | 366 | 1,481 | 1,847 | 999 | 4.9 |
| 28 | L1-worker | claudeopus46 | 366 | 2,744 | 3,110 | 1,584 | 6.5 |
| 29 | L1-worker | claudeopus46 | 787 | 25,527 | 26,314 | 691 | 8.2 |
| 30 | L0-main | claudeopus46 | 11,581 | 22,726 | 34,307 | 4,394 | 31.4 |
| 31 | L0-main | claudeopus46 | 2,106 | 3,878 | 5,984 | 793 | 5.9 |
| 32 | L0-main | claudeopus46 | 2,320 | 3,536 | 5,856 | 1,024 | 8.0 |
| 33 | L0-main | claudeopus46 | 366 | 1,342 | 1,708 | 1,024 | 4.8 |
| 34 | L0-main | claudeopus46 | 366 | 1,499 | 1,865 | 975 | 4.9 |
| 35 | L0-main | claudeopus46 | 560 | 4,557 | 5,117 | 179 | 2.5 |
| 36 | L0-main | claudeopus46 | 560 | 4,236 | 4,796 | 191 | 2.7 |
| 37 | L0-main | claudeopus46 | 1,156 | 6,691 | 7,847 | 1,513 | 9.1 |
| 38 | L0-main | claudeopus46 | 366 | 2,206 | 2,572 | 1,319 | 7.1 |
| 39 | L0-main | claudeopus46 | 560 | 5,630 | 6,190 | 385 | 4.2 |
| 40 | L0-main | claudeopus46 | 366 | 967 | 1,333 | 263 | 2.4 |
| 41 | L0-main | claudeopus46 | 1,156 | 7,703 | 8,859 | 1,289 | 8.1 |
| 42 | L0-main | claudeopus46 | 366 | 1,982 | 2,348 | 1,095 | 4.9 |

