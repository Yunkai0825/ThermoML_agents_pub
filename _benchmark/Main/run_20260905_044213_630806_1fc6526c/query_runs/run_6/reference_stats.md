# Reference Stats — query-agent

**Run started:** 2026-09-05 04:43:18
**Wall time (at last flush):** 350.7 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 8 | 30,036 | 26,587 | 7,710 | 56,623 | 7,077 | 47.0 | claudeopus46 |
| L1-worker | 32 | 389,040 | 209,734 | 35,033 | 598,774 | 18,711 | 269.2 | claudeopus46 |
| verdict | 1 | 972 | 4,778 | 1,102 | 5,750 | 5,750 | 9.4 | claudeopus46 |
| **TOTAL** | **41** | **420,048** | **241,099** | **43,845** | **661,147** | **16,125** | **325.6** | |

**Estimated tokens:** ~165,286 input + ~10,961 output = ~176,247 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 20 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_property_ids` | 0 | 11 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 50 | 1 | 2 | 2 | 13 | 50 | 933 |
| `resolve_compound_ids` | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_system_summary` | 2 | 0 | 0 | 0 | 16 | 29 | 1,601 |
| `resolve_property_ids` | 0 | 20 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 3 | 0 | 1 | 1 | 1 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **75** | **33** | **5** | **2** | **30** | **80** | **2,535** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (69 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks, search_system_summary |
| GLOBcomp_31 |  | resolve_compound_ids, search_blocks, search_system_summary |
| GLOBcomp_1294 |  | resolve_compound_ids |
| GLOBcomp_2408 |  | resolve_compound_ids |
| GLOBcomp_4986 |  | resolve_compound_ids |
| GLOBcomp_5561 |  | resolve_compound_ids |
| GLOBcomp_1844 |  | resolve_compound_ids |
| GLOBcomp_3340 |  | resolve_compound_ids |
| GLOBcomp_143 |  | resolve_compound_ids |
| GLOBcomp_300 |  | resolve_compound_ids |
| GLOBcomp_1531 |  | resolve_compound_ids |
| GLOBcomp_2145 |  | resolve_compound_ids |
| GLOBcomp_4052 |  | resolve_compound_ids |
| GLOBcomp_5550 |  | resolve_compound_ids |
| GLOBcomp_1748 |  | resolve_compound_ids |
| GLOBcomp_4810 |  | resolve_compound_ids |
| GLOBcomp_6200 |  | resolve_compound_ids |
| GLOBcomp_418 |  | resolve_compound_ids |
| GLOBcomp_1718 |  | resolve_compound_ids |
| GLOBcomp_7322 |  | resolve_compound_ids |
| GLOBcomp_8 | toluene | search_blocks |
| GLOBcomp_27 | ethylbenzene | search_blocks |
| GLOBcomp_96 | chlorobenzene | search_blocks |
| GLOBcomp_197 | bromobenzene | search_blocks |
| GLOBcomp_170 | nitrobenzene | search_blocks |
| GLOBcomp_39 | butanone | search_blocks |
| GLOBcomp_101 | 4-methylpentan-2-one | search_blocks |
| GLOBcomp_87 | cyclohexanone | search_blocks |
| GLOBcomp_529 | hexanoic acid | resolve_compound_ids, search_blocks |
| GLOBcomp_84 | 1-ethyl-3-methylimidazolium tetrafluoroborate | search_blocks |
| GLOBcomp_25 | 1,4-dioxane | search_blocks |
| GLOBcomp_208 | 1,3-dioxolane | search_blocks |
| GLOBcomp_156 | tetrahydropyran | search_blocks |
| GLOBcomp_23 | tetrahydrofuran | search_blocks |
| GLOBcomp_180 | 1,2-dimethoxyethane | search_blocks |
| GLOBcomp_1162 | 1,2-diethoxyethane | search_blocks |
| GLOBcomp_4 | methanol | search_blocks |
| GLOBcomp_2 | ethanol | search_blocks |
| GLOBcomp_5 | propan-1-ol | search_blocks |
| GLOBcomp_7 | butan-1-ol | search_blocks |
| GLOBcomp_38 | hexan-1-ol | search_blocks |
| GLOBcomp_34 | octan-1-ol | search_blocks |
| GLOBcomp_59 | decan-1-ol | search_blocks |
| GLOBcomp_86 | 1,2-dichloroethane | search_blocks |
| GLOBcomp_439 | 1,1,1-trichloroethane | search_blocks |
| GLOBcomp_225 | 1,1,2,2-tetrachloroethane | search_blocks |
| GLOBcomp_235 | trichloroethene | search_blocks |
| GLOBcomp_280 | tetrachloroethene | search_blocks |
| GLOBcomp_24 | 1,2-ethanediol | search_blocks |
| GLOBcomp_111 | diethylene glycol | search_blocks |
| GLOBcomp_113 | triethylene glycol | search_blocks |
| GLOBcomp_251 | tetraethylene glycol | search_blocks |
| GLOBcomp_61 | 1,2-propanediol | search_blocks |
| GLOBcomp_2084 | hexanenitrile | search_blocks |
| GLOBcomp_1926 | heptanenitrile | search_blocks |
| GLOBcomp_2047 | octanenitrile | search_blocks |
| GLOBcomp_1860 | nonanenitrile | search_blocks |
| GLOBcomp_2351 | 1-decanenitrile | search_blocks |
| GLOBcomp_2937 | 1-decylcyanide | search_blocks |
| GLOBcomp_1994 | n-dodecanenitrile | search_blocks |
| GLOBcomp_3069 | dodecanecarbonitrile | search_blocks |
| GLOBcomp_2625 | tetradecanenitrile | search_blocks |
| GLOBcomp_186 | benzenemethanol | search_blocks |
| GLOBcomp_288 | 2-phenylethanol | search_blocks |
| GLOBcomp_1225 | 3-phenyl-1-propanol | search_blocks |
| GLOBcomp_62 | dimethyl carbonate | search_blocks |
| GLOBcomp_103 | diethyl carbonate | search_blocks |
| GLOBcomp_146 | 4-methyl-1,3-dioxolan-2-one | search_blocks |
| GLOBcomp_346 | butyltrimethylammonium bis(trifluoromethylsulfonyl)imide | search_blocks |

#### Properties (23 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_17 |  | resolve_property_ids, search_blocks |
| GLOBprop_22 |  | resolve_property_ids |
| GLOBprop_28 |  | resolve_property_ids |
| GLOBprop_90 |  | resolve_property_ids |
| GLOBprop_85 |  | resolve_property_ids |
| GLOBprop_97 |  | resolve_property_ids |
| GLOBprop_75 |  | resolve_property_ids |
| GLOBprop_30 |  | resolve_property_ids |
| GLOBprop_15 |  | resolve_property_ids, search_blocks |
| GLOBprop_36 |  | resolve_property_ids |
| GLOBprop_46 |  | resolve_property_ids |
| GLOBprop_86 |  | resolve_property_ids |
| GLOBprop_10 |  | resolve_property_ids |
| GLOBprop_110 |  | resolve_property_ids |
| GLOBprop_19 |  | resolve_property_ids |
| GLOBprop_50 |  | resolve_property_ids |
| GLOBprop_77 |  | resolve_property_ids |
| GLOBprop_104 |  | resolve_property_ids |
| GLOBprop_65 |  | resolve_property_ids |
| GLOBprop_43 |  | resolve_property_ids |
| GLOBprop_37 |  | resolve_property_ids |
| GLOBprop_59 |  | resolve_property_ids |
| GLOBprop_35 |  | resolve_property_ids |

#### References (29 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_577 |  | search_blocks |
| GLOBlit_2816 |  | search_blocks |
| GLOBlit_3440 |  | search_blocks |
| GLOBlit_3810 |  | search_blocks |
| GLOBlit_5705 |  | search_blocks |
| GLOBlit_5731 |  | search_blocks |
| GLOBlit_5763 |  | search_blocks |
| GLOBlit_8204 |  | search_blocks |
| GLOBlit_8539 |  | search_blocks |
| GLOBlit_8669 |  | search_blocks |
| GLOBlit_8790 |  | search_blocks |
| GLOBlit_8919 |  | search_blocks |
| GLOBlit_10541 |  | search_blocks |
| GLOBlit_10109 |  | search_system_summary |
| GLOBlit_2844 |  | search_system_summary |
| GLOBlit_2781 |  | search_system_summary |
| GLOBlit_10766 |  | search_system_summary |
| GLOBlit_2584 |  | search_system_summary |
| GLOBlit_2842 |  | search_system_summary |
| GLOBlit_11018 |  | search_system_summary |
| GLOBlit_11517 |  | search_system_summary |
| GLOBlit_10024 |  | search_system_summary |
| GLOBlit_5953 |  | search_system_summary |
| GLOBlit_10215 |  | search_system_summary |
| GLOBlit_663 |  | search_system_summary |
| GLOBlit_2652 |  | search_system_summary |
| GLOBlit_7713 |  | search_system_summary |
| GLOBlit_9547 |  | search_system_summary |
| GLOBlit_5958 |  | search_blocks, search_system_summary |

#### Measurements (8 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_13 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_254 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_262 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_769 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_12 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_200 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_169 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_144 | Molar enthalpy of solution, kJ/mol | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks |

#### Variables (4 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_2 | Mole fraction | search_blocks |
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |
| GLOBvar_3 | Pressure, kPa | search_blocks |

#### Constraints (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_2 | Temperature, K | search_blocks |
| GLOBconstr_1 | Pressure, kPa | search_blocks |

#### Solvents (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_8 |  | search_blocks |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 69 |
| Unique Properties | 23 |
| Unique References | 29 |
| Unique Measurements | 8 |
| Unique Phases | 1 |
| Unique Variables | 4 |
| Unique Constraints | 2 |
| Unique Solvents | 1 |
| Total DOIs | 14 |
| Unique parent blocks | 51 |
| Explicit block/subsystem targets | 51 |
| Subsystem targets | 0 |
| Target-matched data points | 934 |

---

## 3. DOI & Block References

**Unique DOIs:** 14  |  **Parent blocks:** 51  |  **Explicit targets:** 51  |  **Subsystems:** 0  |  **Target-matched datapoints:** 934

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2007.10.017 | 5 | 79 | binary | search_blocks |
| 10.1016/j.jct.2007.04.004 | 3 | 45 | binary | search_blocks |
| 10.1016/j.jct.2011.07.018 | 1 | 66 | binary | search_blocks |
| 10.1016/j.jct.2013.01.010 | 1 | 18 | binary | search_blocks |
| 10.1016/j.tca.2006.05.010 | 6 | 102 | binary | search_blocks |
| 10.1016/j.tca.2006.10.025 | 7 | 120 | binary | search_blocks |
| 10.1016/j.tca.2007.08.008 | 5 | 85 | binary | search_blocks |
| 10.1016/j.tca.2011.09.009 | 1 | 1 | binary | search_blocks |
| 10.1021/je034007i | 5 | 85 | binary | search_blocks |
| 10.1021/je0499317 | 9 | 163 | binary | search_blocks |
| 10.1021/je0501991 | 3 | 51 | binary | search_blocks |
| 10.1021/je050444g | 3 | 51 | binary | search_blocks |
| 10.1021/je0601513 | 1 | 51 | binary | search_blocks |
| 10.1021/je500696p | 1 | 17 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2007.10.017 | PROPblock_13 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.fluid.2007.10.017 | PROPblock_14 | declared | 12 | binary | — | search_blocks |
| 10.1016/j.fluid.2007.10.017 | PROPblock_15 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.fluid.2007.10.017 | PROPblock_16 | declared | 18 | binary | — | search_blocks |
| 10.1016/j.fluid.2007.10.017 | PROPblock_17 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.jct.2007.04.004 | PROPblock_13 | declared | 15 | binary | — | search_blocks |
| 10.1016/j.jct.2007.04.004 | PROPblock_15 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.jct.2007.04.004 | PROPblock_17 | declared | 14 | binary | — | search_blocks |
| 10.1016/j.jct.2011.07.018 | PROPblock_13 | declared | 66 | binary | — | search_blocks |
| 10.1016/j.jct.2013.01.010 | PROPblock_12 | declared | 18 | binary | — | search_blocks |
| 10.1016/j.tca.2006.05.010 | PROPblock_23 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.tca.2006.05.010 | PROPblock_25 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.tca.2006.05.010 | PROPblock_27 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.tca.2006.05.010 | PROPblock_29 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.tca.2006.05.010 | PROPblock_31 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.tca.2006.05.010 | PROPblock_33 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.tca.2006.10.025 | PROPblock_18 | declared | 18 | binary | — | search_blocks |
| 10.1016/j.tca.2006.10.025 | PROPblock_20 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.tca.2006.10.025 | PROPblock_22 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.tca.2006.10.025 | PROPblock_24 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.tca.2006.10.025 | PROPblock_26 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.tca.2006.10.025 | PROPblock_28 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.tca.2006.10.025 | PROPblock_30 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.tca.2007.08.008 | PROPblock_13 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.tca.2007.08.008 | PROPblock_14 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.tca.2007.08.008 | PROPblock_15 | declared | 21 | binary | — | search_blocks |
| 10.1016/j.tca.2007.08.008 | PROPblock_16 | declared | 14 | binary | — | search_blocks |
| 10.1016/j.tca.2007.08.008 | PROPblock_17 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.tca.2011.09.009 | PROPblock_1 | declared | 1 | binary | — | search_blocks |
| 10.1021/je034007i | PROPblock_10 | declared | 17 | binary | — | search_blocks |
| 10.1021/je034007i | PROPblock_11 | declared | 17 | binary | — | search_blocks |
| 10.1021/je034007i | PROPblock_7 | declared | 17 | binary | — | search_blocks |
| 10.1021/je034007i | PROPblock_8 | declared | 17 | binary | — | search_blocks |
| 10.1021/je034007i | PROPblock_9 | declared | 17 | binary | — | search_blocks |
| 10.1021/je0499317 | PROPblock_10 | declared | 15 | binary | — | search_blocks |
| 10.1021/je0499317 | PROPblock_11 | declared | 18 | binary | — | search_blocks |
| 10.1021/je0499317 | PROPblock_12 | declared | 16 | binary | — | search_blocks |
| 10.1021/je0499317 | PROPblock_13 | declared | 22 | binary | — | search_blocks |
| 10.1021/je0499317 | PROPblock_14 | declared | 20 | binary | — | search_blocks |
| 10.1021/je0499317 | PROPblock_15 | declared | 18 | binary | — | search_blocks |
| 10.1021/je0499317 | PROPblock_16 | declared | 17 | binary | — | search_blocks |
| 10.1021/je0499317 | PROPblock_17 | declared | 20 | binary | — | search_blocks |
| 10.1021/je0499317 | PROPblock_18 | declared | 17 | binary | — | search_blocks |
| 10.1021/je0501991 | PROPblock_13 | declared | 17 | binary | — | search_blocks |
| 10.1021/je0501991 | PROPblock_18 | declared | 17 | binary | — | search_blocks |
| 10.1021/je0501991 | PROPblock_23 | declared | 17 | binary | — | search_blocks |
| 10.1021/je050444g | PROPblock_18 | declared | 17 | binary | — | search_blocks |
| 10.1021/je050444g | PROPblock_23 | declared | 17 | binary | — | search_blocks |
| 10.1021/je050444g | PROPblock_28 | declared | 17 | binary | — | search_blocks |
| 10.1021/je0601513 | PROPblock_10 | declared | 51 | binary | — | search_blocks |
| 10.1021/je500696p | PROPblock_8 | declared | 17 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 970 | DISCARD ←in 39 | 912 | 17.5 |
| 2 | 3 | `resolve_compound_ids` | purpose=Verify GLOBcomp IDs for DMSO …, queries=di… | 285 | KEEP ←in 2,142 | 285 | 6.8 |
| 3 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 1,002 | DISCARD ←in 39 | 944 | 11.8 |
| 4 | 5 | `resolve_property_ids` | limit=20, min_score=40, purpose=Verify GLOBprop_17… | 377 | KEEP ←in 1,289 | 377 | 5.4 |
| 5 | 6 | `search_blocks` | compound=GLOBcomp_31, limit=50, property=GLOBprop_… | 1,752 | KEEP ←in 32,997 | 1632 | 38.8 |
| 6 | 7 | `resolve_compound_ids` | purpose=Verify if GLOBcomp_529 is wat…, queries=GL… | 197 | KEEP ←in 239 | 197 | 4.0 |
| 7 | 8 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 782 | DISCARD ←in 39 | 724 | 18.9 |
| 8 | 9 | `search_system_summary` | compound=['GLOBcomp_1', 'GLOBcomp_31'], include_re… | 1,170 | KEEP ←in 1,118 | 1170 | 15.0 |
| 9 | 10 | `resolve_property_ids` | limit=20, min_score=40, purpose=Find alternative p… | 1,041 | KEEP ←in 2,276 | 1041 | 12.4 |
| 10 | 11 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 893 | KEEP ←in 1,762 | 878 | 16.5 |
| 11 | 12 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 688 | DISCARD ←in 39 | 630 | 8.9 |
| 12 | 1 | `L1_query` | context=Looking for composition depen…, id_catalog… | 4,823 | — | — | 300.6 |
| | | **TOTAL (12 tools)** | | **13,980** | | **8,790** | **456.6** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 865 | 12,446 | 1,272 | 8.2 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,219 | 25,314 | 839 | 5.9 |
| 3 | L1-worker | claudeopus46 | 24,095 | 1,910 | 26,005 | 686 | 5.1 |
| 4 | L1-worker | claudeopus46 | 3,767 | 568 | 4,335 | 1,595 | 11.0 |
| 5 | L1-worker | claudeopus46 | 24,095 | 2,872 | 26,967 | 600 | 5.5 |
| 6 | L1-worker | claudeopus46 | 3,767 | 2,278 | 6,045 | 574 | 6.1 |
| 7 | L1-worker | claudeopus46 | 24,095 | 3,415 | 27,510 | 777 | 6.1 |
| 8 | L1-worker | claudeopus46 | 3,767 | 473 | 4,240 | 1,307 | 9.1 |
| 9 | L1-worker | claudeopus46 | 24,095 | 4,762 | 28,857 | 815 | 6.7 |
| 10 | L1-worker | claudeopus46 | 3,767 | 1,495 | 5,262 | 598 | 5.1 |
| 11 | L1-worker | claudeopus46 | 24,095 | 5,489 | 29,584 | 688 | 5.4 |
| 12 | L1-worker | claudeopus46 | 3,767 | 33,327 | 37,094 | 1,916 | 17.5 |
| 13 | L1-worker | claudeopus46 | 3,767 | 33,629 | 37,396 | 2,320 | 19.4 |
| 14 | L1-worker | claudeopus46 | 24,095 | 7,547 | 31,642 | 848 | 9.2 |
| 15 | L1-worker | claudeopus46 | 3,767 | 372 | 4,139 | 349 | 3.8 |
| 16 | L1-worker | claudeopus46 | 24,095 | 8,043 | 32,138 | 1,258 | 9.7 |
| 17 | L1-worker | claudeopus46 | 3,767 | 408 | 4,175 | 1,155 | 8.9 |
| 18 | L1-worker | claudeopus46 | 24,095 | 9,176 | 33,271 | 866 | 7.1 |
| 19 | L1-worker | claudeopus46 | 3,767 | 1,562 | 5,329 | 1,565 | 9.1 |
| 20 | L1-worker | claudeopus46 | 24,095 | 10,737 | 34,832 | 1,389 | 10.3 |
| 21 | L1-worker | claudeopus46 | 3,767 | 2,498 | 6,265 | 1,986 | 12.3 |
| 22 | L1-worker | claudeopus46 | 24,095 | 12,196 | 36,291 | 876 | 9.7 |
| 23 | L1-worker | claudeopus46 | 3,767 | 2,170 | 5,937 | 1,140 | 9.4 |
| 24 | L1-worker | claudeopus46 | 24,095 | 13,468 | 37,563 | 1,223 | 10.0 |
| 25 | L1-worker | claudeopus46 | 3,767 | 463 | 4,230 | 810 | 5.7 |
| 26 | L1-worker | claudeopus46 | 24,062 | 14,296 | 38,358 | 2,917 | 19.6 |
| 27 | L1-worker | claudeopus46 | 24,062 | 15,889 | 39,951 | 2,245 | 16.3 |
| 28 | L1-worker | claudeopus46 | 2,106 | 4,175 | 6,281 | 92 | 2.3 |
| 29 | L1-worker | claudeopus46 | 366 | 869 | 1,235 | 67 | 2.2 |
| 30 | L1-worker | claudeopus46 | 627 | 2,715 | 3,342 | 963 | 5.1 |
| 31 | L1-worker | claudeopus46 | 2,320 | 2,835 | 5,155 | 952 | 5.7 |
| 32 | L1-worker | claudeopus46 | 366 | 1,389 | 1,755 | 940 | 3.9 |
| 33 | L1-worker | claudeopus46 | 787 | 7,489 | 8,276 | 677 | 6.0 |
| 34 | L0-main | claudeopus46 | 11,581 | 11,223 | 22,804 | 2,509 | 14.6 |
| 35 | L0-main | claudeopus46 | 2,320 | 2,320 | 4,640 | 855 | 4.3 |
| 36 | L0-main | claudeopus46 | 2,106 | 3,017 | 5,123 | 723 | 5.9 |
| 37 | L0-main | claudeopus46 | 366 | 1,330 | 1,696 | 816 | 3.3 |
| 38 | L0-main | claudeopus46 | 366 | 1,272 | 1,638 | 904 | 3.9 |
| 39 | L0-main | claudeopus46 | 560 | 2,941 | 3,501 | 99 | 2.4 |
| 40 | L0-main | claudeopus46 | 1,156 | 3,619 | 4,775 | 532 | 4.4 |
| 41 | verdict | claudeopus46 | 972 | 4,778 | 5,750 | 1,102 | 9.4 |

