# Reference Stats — query-agent

**Run started:** 2026-08-03 04:22:52
**Wall time (at last flush):** 172.7 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 5 | 22,187 | 38,106 | 11,196 | 60,293 | 12,058 | 62.6 | claudeopus46 |
| L1-worker | 13 | 76,514 | 58,343 | 16,935 | 134,857 | 10,373 | 111.0 | claudeopus46 |
| **TOTAL** | **18** | **98,701** | **96,449** | **28,131** | **195,150** | **10,841** | **173.6** | |

**Estimated tokens:** ~48,787 input + ~7,032 output = ~55,819 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 4 | 2 | 2 | 2 | 3 | 3 | 94 |
| `search_system_summary` | 4 | 0 | 0 | 0 | 3 | 3 | 94 |
| **TOTAL** | **8** | **2** | **2** | **2** | **6** | **6** | **188** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### References (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_4745 |  | search_blocks, search_system_summary |
| GLOBlit_7012 |  | search_blocks, search_system_summary |
| GLOBlit_9386 |  | search_blocks, search_system_summary |

#### Compounds (4 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_114 | sulfuric acid | search_blocks, search_system_summary |
| GLOBcomp_1586 | iron(II) sulfate | search_blocks, search_system_summary |
| GLOBcomp_1 | water | search_blocks, search_system_summary |
| GLOBcomp_112 | hydrogen chloride | search_blocks, search_system_summary |

#### Properties (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_21 | Molality, mol/kg | search_blocks |
| GLOBprop_18 | Electrical conductivity, S/m | search_blocks |

#### Measurements (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_158 | Molality, mol/kg | search_blocks |
| GLOBmeas_14 | Electrical conductivity, S/m | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks |

#### Solvents (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | search_blocks |

#### Variables (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_4 | Molality, mol/kg | search_blocks |
| GLOBvar_1 | Temperature, K | search_blocks |

#### Constraints (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | search_blocks |
| GLOBconstr_2 | Temperature, K | search_blocks |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique References | 3 |
| Unique Compounds | 4 |
| Unique Properties | 2 |
| Unique Measurements | 2 |
| Unique Phases | 1 |
| Unique Solvents | 1 |
| Unique Variables | 2 |
| Unique Constraints | 2 |
| Total DOIs | 3 |
| Unique parent blocks | 3 |
| Explicit block/subsystem targets | 3 |
| Subsystem targets | 0 |
| Target-matched data points | 94 |

---

## 3. DOI & Block References

**Unique DOIs:** 3  |  **Parent blocks:** 3  |  **Explicit targets:** 3  |  **Subsystems:** 0  |  **Target-matched datapoints:** 94

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.jct.2016.07.006 | 1 | 6 | ternary | search_blocks |
| 10.1021/acs.jced.6b00783 | 1 | 55 | ternary | search_blocks |
| 10.1021/je101012n | 1 | 33 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.jct.2016.07.006 | PROPblock_1 | declared | 6 | ternary | — | search_blocks |
| 10.1021/acs.jced.6b00783 | PROPblock_1 | declared | 55 | ternary | — | search_blocks |
| 10.1021/je101012n | PROPblock_30 | declared | 33 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (pre-compaction)

| # | Iter | Tool | Args | Raw (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 1 | `memory_catalog_add` | global_id=GLOBcomp_1, name=water, registry_id=wate… | 2 | — | — | 0.0 |
| 2 | 1 | `memory_catalog_add` | global_id=GLOBcomp_1586, name=iron(II) sulfate, re… | 2 | — | — | 0.0 |
| 3 | 1 | `memory_catalog_add` | global_id=GLOBprop_1, name=Mass density, registry_… | 2 | — | — | 0.0 |
| 4 | 1 | `memory_catalog_add` | global_id=GLOBprop_4, name=Viscosity (dynamic), re… | 2 | — | — | 0.0 |
| 5 | 1 | `memory_catalog_add` | global_id=GLOBprop_13, name=Surface tension (liqui… | 2 | — | — | 0.0 |
| 6 | 1 | `memory_catalog_add` | global_id=GLOBprop_18, name=Electrical conductivit… | 2 | — | — | 0.0 |
| 7 | 1 | `memory_catalog_add` | global_id=GLOBprop_37, name=Molar conductivity, re… | 2 | — | — | 0.0 |
| 8 | 1 | `search_blocks` | compound=['GLOBcomp_1586', 'GLOBcomp_1…, limit=50,… | 713 | DISCARD | 655 | 18.9 |
| 9 | 1 | `search_blocks` | compound=['GLOBcomp_1586', 'GLOBcomp_1…, limit=50,… | 806 | DISCARD | 748 | 11.9 |
| 10 | 1 | `search_blocks` | compound=['GLOBcomp_1586', 'GLOBcomp_1…, limit=50,… | 812 | DISCARD | 754 | 9.4 |
| 11 | 2 | `search_blocks` | compound=GLOBcomp_1586, limit=50, purpose=Find any… | 1,181 | KEEP | 1091 | 13.7 |
| 12 | 2 | `search_system_summary` | compound=GLOBcomp_1586, purpose=Check if iron(II) … | 910 | KEEP | 910 | 9.1 |
| 13 | 1 | `L1_query` | context=This is for finding transport…, id_catalog… | 9,990 | — | — | 114.1 |
| | | **TOTAL (13 tools)** | | **14,426** | | **4,158** | **177.1** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 9,605 | 1,130 | 10,735 | 3,189 | 16.5 |
| 2 | L1-worker | claudeopus46 | 20,643 | 2,090 | 22,733 | 2,153 | 9.7 |
| 3 | L1-worker | claudeopus46 | 2,065 | 443 | 2,508 | 1,590 | 9.7 |
| 4 | L1-worker | claudeopus46 | 2,065 | 450 | 2,515 | 1,722 | 11.1 |
| 5 | L1-worker | claudeopus46 | 2,065 | 455 | 2,520 | 1,292 | 8.8 |
| 6 | L1-worker | claudeopus46 | 20,643 | 5,261 | 25,904 | 994 | 6.9 |
| 7 | L1-worker | claudeopus46 | 2,065 | 7,058 | 9,123 | 1,498 | 13.0 |
| 8 | L1-worker | claudeopus46 | 2,065 | 1,258 | 3,323 | 1,390 | 8.4 |
| 9 | L1-worker | claudeopus46 | 20,643 | 8,012 | 28,655 | 2,346 | 14.3 |
| 10 | L1-worker | claudeopus46 | 536 | 1,819 | 2,355 | 663 | 4.9 |
| 11 | L1-worker | claudeopus46 | 1,356 | 1,939 | 3,295 | 894 | 5.1 |
| 12 | L1-worker | claudeopus46 | 1,323 | 9,885 | 11,208 | 862 | 6.6 |
| 13 | L1-worker | claudeopus46 | 298 | 1,584 | 1,882 | 735 | 3.8 |
| 14 | L1-worker | claudeopus46 | 747 | 18,089 | 18,836 | 796 | 8.7 |
| 15 | L0-main | claudeopus46 | 9,605 | 14,550 | 24,155 | 3,116 | 20.9 |
| 16 | L0-main | claudeopus46 | 1,356 | 2,319 | 3,675 | 669 | 4.7 |
| 17 | L0-main | claudeopus46 | 1,323 | 17,127 | 18,450 | 2,312 | 14.0 |
| 18 | L0-main | claudeopus46 | 298 | 2,980 | 3,278 | 1,910 | 6.5 |

