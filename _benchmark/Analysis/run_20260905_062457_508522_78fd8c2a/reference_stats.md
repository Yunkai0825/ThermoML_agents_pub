# Reference Stats — analysis-agent

**Run started:** 2026-09-05 06:24:57
**Wall time (at last flush):** 1,289.4 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 36 | 639,662 | 1,468,474 | 87,454 | 2,108,136 | 58,559 | 571.0 | claudeopus46 |
| L1-worker | 54 | 740,410 | 651,604 | 108,653 | 1,392,014 | 25,778 | 744.0 | claudeopus46 |
| **TOTAL** | **90** | **1,380,072** | **2,120,078** | **196,107** | **3,500,150** | **38,890** | **1315.0** | |

**Estimated tokens:** ~875,037 input + ~49,026 output = ~924,063 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 9 | 5 | 2 | 12 | 19 | 1,425 |
| `search_system_registry` | 2 | 9 | 5 | 2 | 12 | 19 | 1,425 |
| `search_blocks` | 2 | 9 | 5 | 2 | 12 | 19 | 1,425 |
| `search_blocks` | 2 | 3 | 2 | 1 | 1 | 3 | 48 |
| `search_blocks` | 2 | 1 | 3 | 0 | 1 | 1 | 1 |
| `search_blocks` | 4 | 1 | 2 | 2 | 1 | 3 | 148 |
| `search_system_summary` | 2 | 0 | 0 | 0 | 12 | 19 | 1,425 |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 363 |
| `query_thermoml` | 2 | 6 | 4 | 2 | 8 | 13 | 1,077 |
| `resolve_property_ids` | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 63 |
| `search_blocks` | 2 | 1 | 2 | 0 | 1 | 1 | 112 |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 33 |
| `search_blocks` | 5 | 2 | 2 | 1 | 1 | 16 | 441 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml` | 5 | 3 | 3 | 1 | 2 | 17 | 296 |
| **TOTAL** | **38** | **48** | **39** | **16** | **66** | **133** | **8,282** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (7 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_31 |  | query_thermoml, resolve_compound_ids, search_blocks, search_system_registry, search_system_summary |
| GLOBcomp_1 |  | query_thermoml, resolve_compound_ids, search_blocks, search_system_registry, search_system_summary |
| GLOBcomp_179 | 1-ethyl-3-methylimidazolium acetate | search_blocks |
| GLOBcomp_1455 | choline acetate | search_blocks |
| GLOBcomp_1294 | diethyl sulfoxide | query_thermoml, search_blocks |
| GLOBcomp_2145 | dipropyl sulfoxide | query_thermoml, search_blocks |
| GLOBcomp_7698 | 2,2'-sulfinylbispropane | query_thermoml, search_blocks |

#### References (12 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_2584 |  | query_thermoml, search_blocks, search_system_registry, search_system_summary |
| GLOBlit_2652 |  | query_thermoml, search_blocks, search_system_registry, search_system_summary |
| GLOBlit_2781 |  | query_thermoml, search_blocks, search_system_registry, search_system_summary |
| GLOBlit_2844 |  | query_thermoml, search_blocks, search_system_registry, search_system_summary |
| GLOBlit_5953 |  | query_thermoml, search_blocks, search_system_registry, search_system_summary |
| GLOBlit_5958 |  | query_thermoml, search_blocks, search_system_registry, search_system_summary |
| GLOBlit_7713 |  | query_thermoml, search_blocks, search_system_registry, search_system_summary |
| GLOBlit_10024 |  | query_thermoml, search_blocks, search_system_registry, search_system_summary |
| GLOBlit_10109 |  | query_thermoml, search_blocks, search_system_registry, search_system_summary |
| GLOBlit_10766 |  | query_thermoml, search_blocks, search_system_registry, search_system_summary |
| GLOBlit_11018 |  | search_blocks, search_system_registry, search_system_summary |
| GLOBlit_11517 |  | search_blocks, search_system_registry, search_system_summary |

#### Properties (9 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_1 | Mass density, kg/m3 | query_thermoml, search_blocks, search_system_registry |
| GLOBprop_8 | Speed of sound, m/s | query_thermoml, search_blocks, search_system_registry |
| GLOBprop_4 | Viscosity, Pa*s | query_thermoml, search_blocks, search_system_registry |
| GLOBprop_64 | Apparent molar heat capacity, J/K/mol | query_thermoml, search_blocks, search_system_registry |
| GLOBprop_15 | Molar enthalpy of solution, kJ/mol | query_thermoml, search_blocks, search_system_registry |
| GLOBprop_34 | Thermal conductivity, W/m/K | query_thermoml, resolve_property_ids, search_blocks, search_system_registry |
| GLOBprop_44 | Relative permittivity at zero frequency | query_thermoml, search_blocks, search_system_registry |
| GLOBprop_13 | Surface tension liquid-gas, N/m | query_thermoml, search_blocks, search_system_registry |
| GLOBprop_7 | Refractive index (Na D-line) | query_thermoml, search_blocks, search_system_registry |

#### Measurements (18 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_147 | Mass density, kg/m3 | query_thermoml, search_blocks, search_system_registry |
| GLOBmeas_7 | Speed of sound, m/s | query_thermoml, search_blocks, search_system_registry |
| GLOBmeas_141 | Mass density, kg/m3 | query_thermoml, search_blocks, search_system_registry |
| GLOBmeas_140 | Viscosity, Pa*s | query_thermoml, search_blocks, search_system_registry |
| GLOBmeas_134 | Mass density, kg/m3 | query_thermoml, search_blocks, search_system_registry |
| GLOBmeas_57 | Apparent molar heat capacity, J/K/mol | query_thermoml, search_blocks, search_system_registry |
| GLOBmeas_4 | Viscosity, Pa*s | query_thermoml, search_blocks, search_system_registry |
| GLOBmeas_15 | Speed of sound, m/s | query_thermoml, search_blocks, search_system_registry |
| GLOBmeas_6 | Mass density, kg/m3 | query_thermoml, search_blocks, search_system_registry |
| GLOBmeas_144 | Molar enthalpy of solution, kJ/mol | query_thermoml, search_blocks, search_system_registry |
| GLOBmeas_2 | Mass density, kg/m3 | query_thermoml, search_blocks, search_system_registry |
| GLOBmeas_41 | Thermal conductivity, W/m/K | query_thermoml, search_blocks, search_system_registry |
| GLOBmeas_823 | Relative permittivity at zero frequency | query_thermoml, search_blocks, search_system_registry |
| GLOBmeas_36 | Surface tension liquid-gas, N/m | query_thermoml, search_blocks, search_system_registry |
| GLOBmeas_163 | Refractive index (Na D-line) | query_thermoml, search_blocks, search_system_registry |
| GLOBmeas_205 | Viscosity, Pa*s | search_blocks, search_system_registry |
| GLOBmeas_495 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_714 | Surface tension liquid-gas, N/m | query_thermoml, search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | query_thermoml, search_blocks, search_system_registry |

#### Variables (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | query_thermoml, search_blocks, search_system_registry |
| GLOBvar_2 | Mole fraction | query_thermoml, search_blocks, search_system_registry |
| GLOBvar_4 | Molality, mol/kg | query_thermoml, search_blocks, search_system_registry |
| GLOBvar_3 | Pressure, kPa | query_thermoml, search_blocks, search_system_registry |
| GLOBvar_5 | Mass fraction | query_thermoml, search_blocks, search_system_registry |

#### Constraints (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | query_thermoml, search_blocks, search_system_registry |
| GLOBconstr_3 | Mole fraction | query_thermoml, search_blocks, search_system_registry |

#### Solvents (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | query_thermoml, search_blocks, search_system_registry |
| GLOBsolvent_8 |  | query_thermoml, search_blocks, search_system_registry |

#### Block_Types (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | query_thermoml, search_system_registry |
| GLOBblocktype_2 |  | query_thermoml |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 7 |
| Unique References | 12 |
| Unique Properties | 9 |
| Unique Measurements | 18 |
| Unique Phases | 1 |
| Unique Variables | 5 |
| Unique Constraints | 2 |
| Unique Solvents | 2 |
| Unique Block_Types | 2 |
| Total DOIs | 12 |
| Unique parent blocks | 35 |
| Explicit block/subsystem targets | 35 |
| Subsystem targets | 0 |
| Target-matched data points | 7,065 |

---

## 3. DOI & Block References

**Unique DOIs:** 12  |  **Parent blocks:** 35  |  **Explicit targets:** 35  |  **Subsystems:** 0  |  **Target-matched datapoints:** 1,860

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.jct.2005.07.012 | 1 | 96 | binary | query_thermoml, search_blocks, search_system_registry |
| 10.1016/j.jct.2006.01.007 | 2 | 12 | binary | query_thermoml, search_blocks, search_system_registry |
| 10.1016/j.jct.2006.12.012 | 2 | 240 | binary | query_thermoml, search_blocks, search_system_registry |
| 10.1016/j.jct.2007.06.010 | 2 | 308 | binary | query_thermoml, search_blocks, search_system_registry |
| 10.1016/j.tca.2011.08.013 | 3 | 48 | binary | query_thermoml, search_blocks, search_system_registry |
| 10.1016/j.tca.2011.09.009 | 1 | 1 | binary | query_thermoml, search_blocks, search_system_registry |
| 10.1021/acs.jced.8b01048 | 3 | 148 | binary, ternary | query_thermoml, search_blocks, search_system_registry |
| 10.1021/je301171y | 1 | 63 | binary | query_thermoml, search_blocks, search_system_registry |
| 10.1021/je400149j | 1 | 363 | binary | query_thermoml, search_blocks, search_system_registry |
| 10.1021/je7001013 | 16 | 441 | binary, unary | query_thermoml, search_blocks, search_system_registry |
| 10.1021/je700645p | 1 | 70 | binary | search_blocks, search_system_registry |
| 10.1021/je9001027 | 2 | 70 | binary | search_blocks, search_system_registry |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.jct.2005.07.012 | PROPblock_8 | declared | 96 | binary | 2 | query_thermoml, search_blocks, search_system_registry |
| 10.1016/j.jct.2006.01.007 | PROPblock_3 | declared | 6 | binary | 2 | query_thermoml, search_blocks, search_system_registry |
| 10.1016/j.jct.2006.01.007 | PROPblock_4 | declared | 6 | binary | 2 | query_thermoml, search_blocks, search_system_registry |
| 10.1016/j.jct.2006.12.012 | PROPblock_3 | declared | 120 | binary | 2 | query_thermoml, search_blocks, search_system_registry |
| 10.1016/j.jct.2006.12.012 | PROPblock_4 | declared | 120 | binary | 2 | query_thermoml, search_blocks, search_system_registry |
| 10.1016/j.jct.2007.06.010 | PROPblock_3 | declared | 216 | binary | 2 | query_thermoml, search_blocks, search_system_registry |
| 10.1016/j.jct.2007.06.010 | PROPblock_4 | declared | 92 | binary | 2 | query_thermoml, search_blocks, search_system_registry |
| 10.1016/j.tca.2011.08.013 | PROPblock_10 | declared | 16 | binary | 2 | query_thermoml, search_blocks, search_system_registry |
| 10.1016/j.tca.2011.08.013 | PROPblock_11 | declared | 16 | binary | 2 | query_thermoml, search_blocks, search_system_registry |
| 10.1016/j.tca.2011.08.013 | PROPblock_12 | declared | 16 | binary | 2 | query_thermoml, search_blocks, search_system_registry |
| 10.1016/j.tca.2011.09.009 | PROPblock_1 | declared | 1 | binary | 2 | query_thermoml, search_blocks, search_system_registry |
| 10.1021/acs.jced.8b01048 | PROPblock_10 | declared | 9 | binary | 2 | query_thermoml, search_blocks, search_system_registry |
| 10.1021/acs.jced.8b01048 | PROPblock_3 | declared | 108 | ternary | — | search_blocks |
| 10.1021/acs.jced.8b01048 | PROPblock_4 | declared | 31 | ternary | — | search_blocks |
| 10.1021/je301171y | PROPblock_5 | declared | 63 | binary | 2 | query_thermoml, search_blocks, search_system_registry |
| 10.1021/je400149j | PROPblock_5 | declared | 363 | binary | 2 | query_thermoml, search_blocks, search_system_registry |
| 10.1021/je7001013 | PROPblock_1 | declared | 7 | unary | 1 | query_thermoml, search_blocks |
| 10.1021/je7001013 | PROPblock_10 | declared | 33 | binary | 2 | query_thermoml, search_blocks, search_system_registry |
| 10.1021/je7001013 | PROPblock_11 | declared | 56 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je7001013 | PROPblock_12 | declared | 30 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je7001013 | PROPblock_13 | declared | 63 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je7001013 | PROPblock_14 | declared | 30 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je7001013 | PROPblock_15 | declared | 53 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je7001013 | PROPblock_16 | declared | 24 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je7001013 | PROPblock_2 | declared | 3 | unary | 1 | query_thermoml, search_blocks |
| 10.1021/je7001013 | PROPblock_3 | declared | 7 | unary | 1 | query_thermoml, search_blocks |
| 10.1021/je7001013 | PROPblock_4 | declared | 3 | unary | 1 | query_thermoml, search_blocks |
| 10.1021/je7001013 | PROPblock_5 | declared | 7 | unary | 1 | query_thermoml, search_blocks |
| 10.1021/je7001013 | PROPblock_6 | declared | 3 | unary | 1 | query_thermoml, search_blocks |
| 10.1021/je7001013 | PROPblock_7 | declared | 7 | unary | 1 | query_thermoml, search_blocks |
| 10.1021/je7001013 | PROPblock_8 | declared | 3 | unary | 1 | query_thermoml, search_blocks |
| 10.1021/je7001013 | PROPblock_9 | declared | 112 | binary | 2 | query_thermoml, search_blocks, search_system_registry |
| 10.1021/je700645p | PROPblock_6 | declared | 70 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je9001027 | PROPblock_3 | declared | 35 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je9001027 | PROPblock_4 | declared | 35 | binary | 2 | search_blocks, search_system_registry |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `query_thermoml_parallel` | queries=[{'label': 'density', 'purpos… | 209 | — | — | 0.0 |
| 2 | 3 | `query_thermoml_parallel` | queries=[{'label': 'density_dmso_wate… | 132 | — | — | 0.0 |
| 3 | 4 | `query_thermoml_parallel` | queries=[{'label': 'density_dmso_wate… | 132 | — | — | 0.1 |
| 4 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve DMSO and wa… | 200 | KEEP ←in 295 | 200 | 3.9 |
| 5 | 4 | `search_blocks` | compound=['GLOBcomp_31', 'GLOBcomp_1'], limit=50, … | 1,264 | KEEP ←in 12,628 | 1249 | 16.2 |
| 6 | 5 | `search_system_registry` | compound=['GLOBcomp_31', 'GLOBcomp_1'], limit=50, … | 1,176 | KEEP ←in 3,070 | 996 | 16.2 |
| 7 | 6 | `search_blocks` | compound=['GLOBcomp_31', 'GLOBcomp_1'], limit=50, … | 1,212 | KEEP ←in 12,628 | 1197 | 14.1 |
| 8 | 7 | `search_blocks` | compound=['GLOBcomp_31', 'GLOBcomp_1'], limit=50, … | 1,122 | KEEP ←in 5,878 | 1122 | 15.5 |
| 9 | 8 | `search_blocks` | compound=['GLOBcomp_31', 'GLOBcomp_1'], limit=50, … | 1,033 | KEEP ←in 1,762 | 1033 | 11.7 |
| 10 | 9 | `search_blocks` | compound=['GLOBcomp_31', 'GLOBcomp_1'], literature… | 916 | KEEP ←in 7,913 | 901 | 15.7 |
| 11 | 10 | `search_system_summary` | compound=['GLOBcomp_31', 'GLOBcomp_1'], purpose=Co… | 1,270 | KEEP ←in 1,070 | 1270 | 19.5 |
| 12 | 11 | `search_blocks` | compound=['GLOBcomp_31', 'GLOBcomp_1'], limit=10, … | 1,210 | KEEP ←in 3,380 | 1194 | 17.8 |
| 13 | 5 | `query_thermoml` | instruction=Search for binary mixture dat…, purpos… | 85,458 | — | — | 402.3 |
| 14 | 8 | `inspect_block` | block_number=PROPblock_8, doi=10.1016/j.jct.2005.0… | 1,383 | — | — | 0.1 |
| 15 | 12 | `inspect_block` | block_number=PROPblock_3, doi=10.1016/j.jct.2006.1… | 1,379 | — | — | 0.1 |
| 16 | 16 | `inspect_block` | block_number=PROPblock_5, doi=10.1021/je400149j, p… | 1,522 | — | — | 0.1 |
| 17 | 20 | `inspect_block` | block_number=PROPblock_3, doi=10.1016/j.jct.2007.0… | 1,534 | — | — | 0.1 |
| 18 | 24 | `inspect_block` | block_number=PROPblock_11, doi=10.1016/j.tca.2011.… | 1,430 | — | — | 0.4 |
| 19 | 2 | `resolve_property_ids` | limit=5, min_score=50, purpose=Resolve thermal con… | 239 | KEEP ←in 226 | 239 | 5.1 |
| 20 | 3 | `search_blocks` | compound=['GLOBcomp_31', 'GLOBcomp_1'], limit=50, … | 1,265 | KEEP ←in 2,121 | 1249 | 14.1 |
| 21 | 4 | `search_blocks` | compound=['GLOBcomp_31', 'GLOBcomp_1'], limit=50, … | 1,285 | KEEP ←in 2,393 | 1269 | 18.8 |
| 22 | 5 | `search_blocks` | compound=['GLOBcomp_31', 'GLOBcomp_1'], limit=50, … | 1,131 | KEEP ←in 2,265 | 1115 | 18.4 |
| 23 | 6 | `search_blocks` | limit=50, literature=GLOBlit_10766, purpose=Find a… | 990 | KEEP ←in 9,688 | 990 | 12.7 |
| 24 | 8 | `inspect_block_table` | block_number=PROPblock_5, literature=GLOBlit_10024… | 1,636 | — | — | 0.2 |
| 25 | 10 | `inspect_block_table` | block_number=PROPblock_9, literature=GLOBlit_10766… | 2,773 | — | — | 0.2 |
| 26 | 11 | `inspect_block_table` | block_number=PROPblock_10, literature=GLOBlit_1076… | 1,659 | — | — | 0.2 |
| 27 | 25 | `query_thermoml` | instruction=Search for binary mixture blo…, purpos… | 112,628 | — | — | 325.2 |
| | | **TOTAL (27 tools)** | | **226,188** | | **14,024** | **928.7** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 22,518 | 436 | 22,954 | 3,644 | 15.9 |
| 2 | L0-main | claudeopus46 | 22,518 | 2,385 | 24,903 | 3,543 | 11.5 |
| 3 | L0-main | claudeopus46 | 22,518 | 1,217 | 23,735 | 3,532 | 12.9 |
| 4 | L0-main | claudeopus46 | 22,518 | 1,647 | 24,165 | 3,329 | 11.4 |
| 5 | L0-main | claudeopus46 | 22,518 | 2,059 | 24,577 | 957 | 7.0 |
| 6 | L1-worker | claudeopus46 | 24,095 | 1,091 | 25,186 | 674 | 6.2 |
| 7 | L1-worker | claudeopus46 | 24,095 | 2,161 | 26,256 | 549 | 4.4 |
| 8 | L1-worker | claudeopus46 | 3,767 | 462 | 4,229 | 332 | 3.7 |
| 9 | L1-worker | claudeopus46 | 24,095 | 1,719 | 25,814 | 1,771 | 11.1 |
| 10 | L1-worker | claudeopus46 | 24,095 | 2,437 | 26,532 | 740 | 4.8 |
| 11 | L1-worker | claudeopus46 | 3,767 | 13,206 | 16,973 | 1,560 | 15.5 |
| 12 | L1-worker | claudeopus46 | 24,095 | 3,663 | 27,758 | 1,138 | 9.2 |
| 13 | L1-worker | claudeopus46 | 3,767 | 3,559 | 7,326 | 1,606 | 12.7 |
| 14 | L1-worker | claudeopus46 | 24,095 | 5,223 | 29,318 | 3,126 | 20.6 |
| 15 | L1-worker | claudeopus46 | 3,767 | 13,092 | 16,859 | 1,465 | 13.4 |
| 16 | L1-worker | claudeopus46 | 24,095 | 6,877 | 30,972 | 3,012 | 19.4 |
| 17 | L1-worker | claudeopus46 | 3,767 | 6,428 | 10,195 | 1,719 | 15.3 |
| 18 | L1-worker | claudeopus46 | 24,095 | 8,402 | 32,497 | 1,278 | 10.2 |
| 19 | L1-worker | claudeopus46 | 3,767 | 2,189 | 5,956 | 1,454 | 11.5 |
| 20 | L1-worker | claudeopus46 | 24,095 | 9,825 | 33,920 | 842 | 6.7 |
| 21 | L1-worker | claudeopus46 | 3,767 | 8,316 | 12,083 | 1,729 | 14.9 |
| 22 | L1-worker | claudeopus46 | 24,095 | 11,155 | 35,250 | 2,151 | 16.6 |
| 23 | L1-worker | claudeopus46 | 3,767 | 1,519 | 5,286 | 1,881 | 12.5 |
| 24 | L1-worker | claudeopus46 | 24,095 | 12,831 | 36,926 | 983 | 8.8 |
| 25 | L1-worker | claudeopus46 | 3,767 | 3,895 | 7,662 | 1,851 | 17.2 |
| 26 | L1-worker | claudeopus46 | 24,095 | 14,533 | 38,628 | 6,910 | 41.4 |
| 27 | L1-worker | claudeopus46 | 24,062 | 25,876 | 49,938 | 5,666 | 39.9 |
| 28 | L1-worker | claudeopus46 | 24,062 | 29,885 | 53,947 | 4,482 | 28.1 |
| 29 | L1-worker | claudeopus46 | 2,320 | 7,180 | 9,500 | 810 | 7.2 |
| 30 | L1-worker | claudeopus46 | 366 | 1,247 | 1,613 | 775 | 3.4 |
| 31 | L1-worker | claudeopus46 | 627 | 7,060 | 7,687 | 1,552 | 12.8 |
| 32 | L1-worker | claudeopus46 | 2,106 | 8,392 | 10,498 | 3,900 | 15.2 |
| 33 | L1-worker | claudeopus46 | 366 | 4,677 | 5,043 | 3,050 | 13.7 |
| 34 | L1-worker | claudeopus46 | 787 | 92,038 | 92,825 | 863 | 10.3 |
| 35 | L0-main | claudeopus46 | 22,518 | 41,273 | 63,791 | 1,756 | 14.7 |
| 36 | L0-main | claudeopus46 | 22,518 | 42,069 | 64,587 | 893 | 12.6 |
| 37 | L0-main | claudeopus46 | 22,518 | 42,863 | 65,381 | 705 | 5.0 |
| 38 | L0-main | claudeopus46 | 22,518 | 44,541 | 67,059 | 1,201 | 9.7 |
| 39 | L0-main | claudeopus46 | 22,518 | 45,290 | 67,808 | 660 | 5.1 |
| 40 | L0-main | claudeopus46 | 22,518 | 46,002 | 68,520 | 597 | 5.5 |
| 41 | L0-main | claudeopus46 | 22,518 | 46,716 | 69,234 | 628 | 6.1 |
| 42 | L0-main | claudeopus46 | 22,518 | 47,999 | 70,517 | 1,091 | 9.8 |
| 43 | L0-main | claudeopus46 | 22,518 | 48,738 | 71,256 | 747 | 5.3 |
| 44 | L0-main | claudeopus46 | 22,518 | 49,491 | 72,009 | 724 | 5.3 |
| 45 | L0-main | claudeopus46 | 22,518 | 50,264 | 72,782 | 712 | 5.1 |
| 46 | L0-main | claudeopus46 | 22,518 | 51,680 | 74,198 | 1,007 | 8.8 |
| 47 | L0-main | claudeopus46 | 22,518 | 52,496 | 75,014 | 614 | 21.8 |
| 48 | L0-main | claudeopus46 | 22,518 | 53,212 | 75,730 | 692 | 5.7 |
| 49 | L0-main | claudeopus46 | 22,518 | 54,002 | 76,520 | 612 | 4.8 |
| 50 | L0-main | claudeopus46 | 22,518 | 55,495 | 78,013 | 1,140 | 12.9 |
| 51 | L0-main | claudeopus46 | 22,518 | 56,313 | 78,831 | 685 | 5.5 |
| 52 | L0-main | claudeopus46 | 22,518 | 57,002 | 79,520 | 681 | 5.9 |
| 53 | L0-main | claudeopus46 | 22,518 | 57,707 | 80,225 | 628 | 5.0 |
| 54 | L0-main | claudeopus46 | 22,518 | 58,989 | 81,507 | 1,287 | 10.2 |
| 55 | L1-worker | claudeopus46 | 24,095 | 1,011 | 25,106 | 890 | 6.2 |
| 56 | L1-worker | claudeopus46 | 24,095 | 2,022 | 26,117 | 571 | 4.1 |
| 57 | L1-worker | claudeopus46 | 3,767 | 379 | 4,146 | 368 | 4.3 |
| 58 | L1-worker | claudeopus46 | 24,095 | 1,725 | 25,820 | 1,179 | 7.6 |
| 59 | L1-worker | claudeopus46 | 3,767 | 2,517 | 6,284 | 1,485 | 13.6 |
| 60 | L1-worker | claudeopus46 | 24,095 | 3,370 | 27,465 | 830 | 13.9 |
| 61 | L1-worker | claudeopus46 | 3,767 | 2,777 | 6,544 | 1,534 | 12.5 |
| 62 | L1-worker | claudeopus46 | 24,095 | 5,055 | 29,150 | 716 | 5.1 |
| 63 | L1-worker | claudeopus46 | 3,767 | 2,663 | 6,430 | 1,452 | 12.1 |
| 64 | L1-worker | claudeopus46 | 24,095 | 6,552 | 30,647 | 960 | 7.6 |
| 65 | L1-worker | claudeopus46 | 3,767 | 10,015 | 13,782 | 1,539 | 12.3 |
| 66 | L1-worker | claudeopus46 | 24,095 | 7,788 | 31,883 | 4,813 | 27.4 |
| 67 | L1-worker | claudeopus46 | 24,095 | 17,411 | 41,506 | 1,157 | 9.7 |
| 68 | L1-worker | claudeopus46 | 24,095 | 19,387 | 43,482 | 515 | 5.8 |
| 69 | L1-worker | claudeopus46 | 24,095 | 20,356 | 44,451 | 534 | 3.8 |
| 70 | L1-worker | claudeopus46 | 24,095 | 22,625 | 46,720 | 620 | 7.6 |
| 71 | L1-worker | claudeopus46 | 24,095 | 24,663 | 48,758 | 6,851 | 45.0 |
| 72 | L1-worker | claudeopus46 | 24,062 | 34,432 | 58,494 | 4,284 | 28.1 |
| 73 | L1-worker | claudeopus46 | 24,062 | 36,345 | 60,407 | 4,371 | 26.8 |
| 74 | L1-worker | claudeopus46 | 2,320 | 4,912 | 7,232 | 1,626 | 12.4 |
| 75 | L1-worker | claudeopus46 | 627 | 4,792 | 5,419 | 1,427 | 12.4 |
| 76 | L1-worker | claudeopus46 | 366 | 2,063 | 2,429 | 1,581 | 6.4 |
| 77 | L1-worker | claudeopus46 | 2,106 | 6,044 | 8,150 | 6,053 | 23.5 |
| 78 | L1-worker | claudeopus46 | 366 | 6,830 | 7,196 | 4,689 | 20.4 |
| 79 | L1-worker | claudeopus46 | 787 | 96,932 | 97,719 | 739 | 8.7 |
| 80 | L0-main | claudeopus46 | 22,518 | 106,633 | 129,151 | 12,132 | 84.5 |
| 81 | L0-main | claudeopus46 | 22,518 | 124,995 | 147,513 | 12,344 | 83.7 |
| 82 | L0-main | claudeopus46 | 22,518 | 143,514 | 166,032 | 12,011 | 79.2 |
| 83 | L0-main | claudeopus46 | 2,106 | 13,312 | 15,418 | 1,448 | 9.4 |
| 84 | L0-main | claudeopus46 | 366 | 1,971 | 2,337 | 1,632 | 7.2 |
| 85 | L0-main | claudeopus46 | 2,320 | 12,761 | 15,081 | 2,536 | 18.2 |
| 86 | L0-main | claudeopus46 | 366 | 2,973 | 3,339 | 2,461 | 6.7 |
| 87 | L0-main | claudeopus46 | 560 | 16,572 | 17,132 | 1,020 | 7.0 |
| 88 | L0-main | claudeopus46 | 1,156 | 24,770 | 25,926 | 4,597 | 25.1 |
| 89 | L0-main | claudeopus46 | 366 | 5,290 | 5,656 | 4,079 | 16.2 |
| 90 | L0-main | claudeopus46 | 1,918 | 5,797 | 7,715 | 1,129 | 10.3 |

