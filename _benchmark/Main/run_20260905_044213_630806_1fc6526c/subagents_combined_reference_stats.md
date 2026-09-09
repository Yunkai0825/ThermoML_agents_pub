# Combined Subagent Stats


## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| L0-main | 6 | 28,320 | 16,683 | 6,890 | 45,003 | 7,500 | 40.2 | claudeopus46 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| L1-worker | 20 | 242,262 | 81,678 | 21,775 | 323,940 | 16,197 | 156.7 | claudeopus46 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| verdict | 1 | 972 | 4,247 | 980 | 5,219 | 5,219 | 8.2 | claudeopus46 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| L0-main | 8 | 30,036 | 42,479 | 9,616 | 72,515 | 9,064 | 65.0 | claudeopus46 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| L1-worker | 17 | 227,560 | 113,134 | 25,300 | 340,694 | 20,040 | 188.2 | claudeopus46 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| verdict | 1 | 972 | 6,494 | 1,163 | 7,466 | 7,466 | 10.1 | claudeopus46 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| L0-main | 8 | 30,036 | 26,587 | 7,710 | 56,623 | 7,077 | 47.0 | claudeopus46 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| L1-worker | 32 | 389,040 | 209,734 | 35,033 | 598,774 | 18,711 | 269.2 | claudeopus46 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| verdict | 1 | 972 | 4,778 | 1,102 | 5,750 | 5,750 | 9.4 | claudeopus46 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| **TOTAL** | **94** | **950,170** | **505,814** | **109,569** | **1,455,984** | **97,024** | **794.0** |  |  |


### 2a. Raw Tool-Return Counters

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `resolve_property_ids` | 0 | 1 | 0 | 0 | 0 | 0 | 0 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| `search_blocks` | 2 | 9 | 5 | 2 | 11 | 16 | 1,377 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| `search_blocks` | 16 | 1 | 1 | 2 | 3 | 15 | 203 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| `search_blocks` | 2 | 1 | 3 | 1 | 2 | 2 | 155 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| `resolve_compound_ids` | 20 | 0 | 0 | 0 | 0 | 0 | 0 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| `resolve_property_ids` | 0 | 11 | 0 | 0 | 0 | 0 | 0 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| `search_blocks` | 50 | 1 | 2 | 2 | 13 | 50 | 933 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| `resolve_compound_ids` | 1 | 0 | 0 | 0 | 0 | 0 | 0 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| `search_system_summary` | 2 | 0 | 0 | 0 | 16 | 29 | 1,601 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| `resolve_property_ids` | 0 | 20 | 0 | 0 | 0 | 0 | 0 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| `search_blocks` | 2 | 1 | 3 | 0 | 1 | 1 | 1 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| **TOTAL** | **95** | **45** | **14** | **7** | **46** | **113** | **4,270** |  |


### 2b. Agent-Condensed Data Complexity

| Metric | Count | Source |
| --- | --- | --- |
| Unique Properties | 10 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| Unique References | 14 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| Unique Compounds | 17 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| Unique Measurements | 16 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| Unique Phases | 1 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| Unique Variables | 5 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| Unique Constraints | 3 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| Unique Solvents | 2 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| Unique parent blocks | 31 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| Explicit block/subsystem targets | 31 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| Subsystem targets | 0 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| Target-matched data points | 1,580 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| GLOBlit_2781 |  | search_blocks |
| GLOBlit_11517 |  | search_blocks |
| GLOBcomp_31 | dimethyl sulfoxide | search_blocks |
| GLOBcomp_1 | water | search_blocks |
| GLOBprop_4 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_140 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_205 | Viscosity, Pa*s | search_blocks |
| GLOBphase_1 |  | search_blocks |
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_2 | Mole fraction | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |
| GLOBconstr_1 | Pressure, kPa | search_blocks |
| Unique References | 2 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| Unique Compounds | 2 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| Unique Properties | 1 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| Unique Measurements | 2 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| Unique Phases | 1 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| Unique Variables | 3 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| Unique Constraints | 1 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| Unique parent blocks | 2 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| Explicit block/subsystem targets | 2 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| Subsystem targets | 0 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| Target-matched data points | 155 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
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
| GLOBmeas_13 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_254 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_262 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_769 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_12 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_200 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_169 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_144 | Molar enthalpy of solution, kJ/mol | search_blocks |
| GLOBphase_1 |  | search_blocks |
| GLOBvar_2 | Mole fraction | search_blocks |
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |
| GLOBvar_3 | Pressure, kPa | search_blocks |
| GLOBconstr_2 | Temperature, K | search_blocks |
| GLOBconstr_1 | Pressure, kPa | search_blocks |
| GLOBsolvent_8 |  | search_blocks |
| Unique Compounds | 69 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| Unique Properties | 23 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| Unique References | 29 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| Unique Measurements | 8 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| Unique Phases | 1 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| Unique Variables | 4 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| Unique Constraints | 2 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| Unique Solvents | 1 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| Unique parent blocks | 51 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| Explicit block/subsystem targets | 51 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| Subsystem targets | 0 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| Target-matched data points | 934 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| **TOTAL** | **3,054** |  |


## 3. DOI & Block References

| DOI | Block | Target | Datapoints | System | nComp | Source tools | Source |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| 10.1016/j.jct.2005.07.012 | PROPblock_8 | declared | 96 | binary | — | search_blocks | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 10.1016/j.jct.2006.01.007 | PROPblock_3 | declared | 6 | binary | — | search_blocks | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 10.1016/j.jct.2006.01.007 | PROPblock_4 | declared | 6 | binary | — | search_blocks | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 10.1016/j.jct.2006.04.005 | PROPblock_29 | declared | 15 | binary | — | search_blocks | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 10.1016/j.jct.2006.04.005 | PROPblock_33 | declared | 15 | binary | — | search_blocks | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 10.1016/j.jct.2006.04.005 | PROPblock_37 | declared | 15 | binary | — | search_blocks | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 10.1016/j.jct.2006.04.005 | PROPblock_41 | declared | 14 | binary | — | search_blocks | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 10.1016/j.jct.2006.04.005 | PROPblock_45 | declared | 15 | binary | — | search_blocks | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 10.1016/j.jct.2006.04.005 | PROPblock_49 | declared | 15 | binary | — | search_blocks | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 10.1016/j.jct.2006.04.005 | PROPblock_53 | declared | 15 | binary | — | search_blocks | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 10.1016/j.jct.2006.04.005 | PROPblock_57 | declared | 15 | binary | — | search_blocks | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 10.1016/j.jct.2006.12.012 | PROPblock_3 | declared | 120 | binary | — | search_blocks | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 10.1016/j.jct.2006.12.012 | PROPblock_4 | declared | 120 | binary | — | search_blocks | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 10.1016/j.jct.2007.06.010 | PROPblock_3 | declared | 216 | binary | — | search_blocks | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 10.1016/j.jct.2007.06.010 | PROPblock_4 | declared | 92 | binary | — | search_blocks | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 10.1016/j.jct.2007.08.006 | PROPblock_14 | declared | 9 | binary | — | search_blocks | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 10.1016/j.jct.2007.08.006 | PROPblock_16 | declared | 9 | binary | — | search_blocks | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 10.1016/j.jct.2007.08.006 | PROPblock_18 | declared | 9 | binary | — | search_blocks | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 10.1016/j.jct.2007.08.006 | PROPblock_20 | declared | 10 | binary | — | search_blocks | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 10.1016/j.jct.2007.08.006 | PROPblock_22 | declared | 9 | binary | — | search_blocks | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 10.1016/j.tca.2011.09.009 | PROPblock_1 | declared | 1 | binary | — | search_blocks | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 10.1021/acs.jced.8b01048 | PROPblock_10 | declared | 9 | binary | — | search_blocks | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 10.1021/je0497294 | PROPblock_20 | declared | 19 | binary | — | search_blocks | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 10.1021/je0497294 | PROPblock_22 | declared | 19 | binary | — | search_blocks | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 10.1021/je301171y | PROPblock_5 | declared | 63 | binary | — | search_blocks | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 10.1021/je400149j | PROPblock_5 | declared | 363 | binary | — | search_blocks | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 10.1021/je7001013 | PROPblock_10 | declared | 33 | binary | — | search_blocks | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 10.1021/je7001013 | PROPblock_9 | declared | 112 | binary | — | search_blocks | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 10.1021/je700645p | PROPblock_6 | declared | 70 | binary | — | search_blocks | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 10.1021/je9001027 | PROPblock_3 | declared | 35 | binary | — | search_blocks | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 10.1021/je9001027 | PROPblock_4 | declared | 35 | binary | — | search_blocks | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 10.1016/j.jct.2006.12.012 | 1 | 120 | binary | search_blocks | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |  |  |
| 10.1021/je9001027 | 1 | 35 | binary | search_blocks | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |  |  |
| 10.1016/j.jct.2006.12.012 | PROPblock_3 | declared | 120 | binary | — | search_blocks | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| 10.1021/je9001027 | PROPblock_3 | declared | 35 | binary | — | search_blocks | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| 10.1016/j.fluid.2007.10.017 | 5 | 79 | binary | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |  |  |
| 10.1016/j.jct.2007.04.004 | 3 | 45 | binary | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |  |  |
| 10.1016/j.jct.2011.07.018 | 1 | 66 | binary | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |  |  |
| 10.1016/j.jct.2013.01.010 | 1 | 18 | binary | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |  |  |
| 10.1016/j.tca.2006.05.010 | 6 | 102 | binary | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |  |  |
| 10.1016/j.tca.2006.10.025 | 7 | 120 | binary | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |  |  |
| 10.1016/j.tca.2007.08.008 | 5 | 85 | binary | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |  |  |
| 10.1016/j.tca.2011.09.009 | 1 | 1 | binary | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |  |  |
| 10.1021/je034007i | 5 | 85 | binary | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |  |  |
| 10.1021/je0499317 | 9 | 163 | binary | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |  |  |
| 10.1021/je0501991 | 3 | 51 | binary | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |  |  |
| 10.1021/je050444g | 3 | 51 | binary | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |  |  |
| 10.1021/je0601513 | 1 | 51 | binary | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |  |  |
| 10.1021/je500696p | 1 | 17 | binary | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |  |  |
| 10.1016/j.fluid.2007.10.017 | PROPblock_13 | declared | 16 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1016/j.fluid.2007.10.017 | PROPblock_14 | declared | 12 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1016/j.fluid.2007.10.017 | PROPblock_15 | declared | 17 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1016/j.fluid.2007.10.017 | PROPblock_16 | declared | 18 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1016/j.fluid.2007.10.017 | PROPblock_17 | declared | 16 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1016/j.jct.2007.04.004 | PROPblock_13 | declared | 15 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1016/j.jct.2007.04.004 | PROPblock_15 | declared | 16 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1016/j.jct.2007.04.004 | PROPblock_17 | declared | 14 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1016/j.jct.2011.07.018 | PROPblock_13 | declared | 66 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1016/j.jct.2013.01.010 | PROPblock_12 | declared | 18 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1016/j.tca.2006.05.010 | PROPblock_23 | declared | 17 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1016/j.tca.2006.05.010 | PROPblock_25 | declared | 17 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1016/j.tca.2006.05.010 | PROPblock_27 | declared | 17 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1016/j.tca.2006.05.010 | PROPblock_29 | declared | 17 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1016/j.tca.2006.05.010 | PROPblock_31 | declared | 17 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1016/j.tca.2006.05.010 | PROPblock_33 | declared | 17 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1016/j.tca.2006.10.025 | PROPblock_18 | declared | 18 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1016/j.tca.2006.10.025 | PROPblock_20 | declared | 17 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1016/j.tca.2006.10.025 | PROPblock_22 | declared | 17 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1016/j.tca.2006.10.025 | PROPblock_24 | declared | 17 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1016/j.tca.2006.10.025 | PROPblock_26 | declared | 17 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1016/j.tca.2006.10.025 | PROPblock_28 | declared | 17 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1016/j.tca.2006.10.025 | PROPblock_30 | declared | 17 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1016/j.tca.2007.08.008 | PROPblock_13 | declared | 17 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1016/j.tca.2007.08.008 | PROPblock_14 | declared | 17 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1016/j.tca.2007.08.008 | PROPblock_15 | declared | 21 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1016/j.tca.2007.08.008 | PROPblock_16 | declared | 14 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1016/j.tca.2007.08.008 | PROPblock_17 | declared | 16 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1016/j.tca.2011.09.009 | PROPblock_1 | declared | 1 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1021/je034007i | PROPblock_10 | declared | 17 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1021/je034007i | PROPblock_11 | declared | 17 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1021/je034007i | PROPblock_7 | declared | 17 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1021/je034007i | PROPblock_8 | declared | 17 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1021/je034007i | PROPblock_9 | declared | 17 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1021/je0499317 | PROPblock_10 | declared | 15 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1021/je0499317 | PROPblock_11 | declared | 18 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1021/je0499317 | PROPblock_12 | declared | 16 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1021/je0499317 | PROPblock_13 | declared | 22 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1021/je0499317 | PROPblock_14 | declared | 20 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1021/je0499317 | PROPblock_15 | declared | 18 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1021/je0499317 | PROPblock_16 | declared | 17 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1021/je0499317 | PROPblock_17 | declared | 20 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1021/je0499317 | PROPblock_18 | declared | 17 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1021/je0501991 | PROPblock_13 | declared | 17 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1021/je0501991 | PROPblock_18 | declared | 17 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1021/je0501991 | PROPblock_23 | declared | 17 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1021/je050444g | PROPblock_18 | declared | 17 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1021/je050444g | PROPblock_23 | declared | 17 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1021/je050444g | PROPblock_28 | declared | 17 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1021/je0601513 | PROPblock_10 | declared | 51 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10.1021/je500696p | PROPblock_8 | declared | 17 | binary | — | search_blocks | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| **TOTAL** | **53** | **1,089** | **2,669** |  |  |  |  |


## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) | Source |
| ---: | ---: | --- | --- | ---: | --- | ---: | ---: | --- |
| 1 | 2 | `resolve_property_ids` | limit=10, min_score=50, purpose=Find the global pr… | 254 | KEEP ←in 227 | 254 | 4.6 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 2 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 989 | DISCARD ←in 39 | 931 | 10.7 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 3 | 5 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 1,042 | DISCARD ←in 39 | 984 | 19.8 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 4 | 6 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 1,314 | KEEP ←in 10,618 | 1115 | 19.5 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 5 | 7 | `search_blocks` | compound=GLOBcomp_31, limit=20, property=GLOBprop_… | 1,139 | KEEP ←in 9,632 | 1016 | 19.5 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 6 | 1 | `L1_query` | context=User wants composition depend…, id_catalog… | 3,432 | — | — | 172.6 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 1 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 1,252 | KEEP ←in 5,142 | 1252 | 20.7 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| 2 | 3 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_2781,… | 377 | — | — | 0.1 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| 3 | 4 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_2781,… | 1,897 | — | — | 0.3 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| 4 | 5 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_11517… | 261 | — | — | 0.0 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| 5 | 6 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_11517… | 1,171 | — | — | 0.2 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| 6 | 1 | `L1_query` | context=User wants composition depend…, id_catalog… | 23,878 | — | — | 173.4 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| 1 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 970 | DISCARD ←in 39 | 912 | 17.5 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 2 | 3 | `resolve_compound_ids` | purpose=Verify GLOBcomp IDs for DMSO …, queries=di… | 285 | KEEP ←in 2,142 | 285 | 6.8 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 3 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 1,002 | DISCARD ←in 39 | 944 | 11.8 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 4 | 5 | `resolve_property_ids` | limit=20, min_score=40, purpose=Verify GLOBprop_17… | 377 | KEEP ←in 1,289 | 377 | 5.4 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 5 | 6 | `search_blocks` | compound=GLOBcomp_31, limit=50, property=GLOBprop_… | 1,752 | KEEP ←in 32,997 | 1632 | 38.8 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 6 | 7 | `resolve_compound_ids` | purpose=Verify if GLOBcomp_529 is wat…, queries=GL… | 197 | KEEP ←in 239 | 197 | 4.0 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 7 | 8 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 782 | DISCARD ←in 39 | 724 | 18.9 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 8 | 9 | `search_system_summary` | compound=['GLOBcomp_1', 'GLOBcomp_31'], include_re… | 1,170 | KEEP ←in 1,118 | 1170 | 15.0 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 9 | 10 | `resolve_property_ids` | limit=20, min_score=40, purpose=Find alternative p… | 1,041 | KEEP ←in 2,276 | 1041 | 12.4 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10 | 11 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 893 | KEEP ←in 1,762 | 878 | 16.5 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 11 | 12 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 688 | DISCARD ←in 39 | 630 | 8.9 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 12 | 1 | `L1_query` | context=Looking for composition depen…, id_catalog… | 4,823 | — | — | 300.6 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| **TOTAL** | **124** |  |  | **50,986** |  | **14,342** | **898.0** |  |


## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) | Source |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | L0-main | claudeopus46 | 11,581 | 861 | 12,442 | 1,418 | 8.5 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,278 | 25,373 | 662 | 4.8 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,322 | 26,417 | 585 | 6.3 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 4 | L1-worker | claudeopus46 | 3,767 | 413 | 4,180 | 416 | 4.1 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,960 | 26,055 | 822 | 5.5 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,678 | 26,773 | 659 | 5.3 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 7 | L1-worker | claudeopus46 | 3,767 | 566 | 4,333 | 1,520 | 10.3 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,640 | 27,735 | 843 | 5.7 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 9 | L1-worker | claudeopus46 | 3,767 | 449 | 4,216 | 1,394 | 10.4 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 10 | L1-worker | claudeopus46 | 24,095 | 5,019 | 29,114 | 869 | 6.8 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 11 | L1-worker | claudeopus46 | 3,767 | 11,008 | 14,775 | 1,574 | 12.8 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 12 | L1-worker | claudeopus46 | 24,095 | 6,745 | 30,840 | 1,437 | 9.0 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 13 | L1-worker | claudeopus46 | 3,767 | 10,009 | 13,776 | 1,388 | 12.8 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 14 | L1-worker | claudeopus46 | 24,095 | 8,288 | 32,383 | 2,937 | 19.8 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 15 | L1-worker | claudeopus46 | 24,095 | 13,163 | 37,258 | 3,743 | 21.4 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 16 | L1-worker | claudeopus46 | 2,106 | 3,301 | 5,407 | 92 | 2.1 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 17 | L1-worker | claudeopus46 | 366 | 869 | 1,235 | 67 | 2.0 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 18 | L1-worker | claudeopus46 | 2,320 | 1,902 | 4,222 | 684 | 4.4 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 19 | L1-worker | claudeopus46 | 627 | 1,782 | 2,409 | 811 | 5.2 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 20 | L1-worker | claudeopus46 | 366 | 1,121 | 1,487 | 672 | 2.8 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 21 | L1-worker | claudeopus46 | 787 | 5,165 | 5,952 | 600 | 5.2 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 22 | L0-main | claudeopus46 | 11,581 | 8,050 | 19,631 | 2,456 | 13.6 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 23 | L0-main | claudeopus46 | 2,320 | 2,254 | 4,574 | 730 | 4.1 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 24 | L0-main | claudeopus46 | 366 | 1,205 | 1,571 | 691 | 3.0 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 25 | L0-main | claudeopus46 | 2,106 | 2,947 | 5,053 | 817 | 7.3 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 26 | L0-main | claudeopus46 | 366 | 1,366 | 1,732 | 778 | 3.7 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 27 | verdict | claudeopus46 | 972 | 4,247 | 5,219 | 980 | 8.2 | Find blocks with excess molar volume (VE) data for the binar (query_runs/run_7) |
| 1 | L0-main | claudeopus46 | 11,581 | 869 | 12,450 | 1,240 | 8.3 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,244 | 25,339 | 803 | 8.3 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| 3 | L1-worker | claudeopus46 | 24,095 | 1,974 | 26,069 | 644 | 4.4 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| 4 | L1-worker | claudeopus46 | 3,767 | 5,623 | 9,390 | 1,552 | 15.8 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| 5 | L1-worker | claudeopus46 | 24,095 | 3,185 | 27,280 | 786 | 7.1 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| 6 | L1-worker | claudeopus46 | 24,095 | 4,006 | 28,101 | 671 | 5.2 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| 7 | L1-worker | claudeopus46 | 24,095 | 6,225 | 30,320 | 1,094 | 9.3 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| 8 | L1-worker | claudeopus46 | 24,095 | 6,926 | 31,021 | 635 | 6.0 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| 9 | L1-worker | claudeopus46 | 24,095 | 8,414 | 32,509 | 3,294 | 24.8 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| 10 | L1-worker | claudeopus46 | 24,095 | 15,218 | 39,313 | 4,494 | 31.9 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| 11 | L1-worker | claudeopus46 | 24,095 | 22,734 | 46,829 | 4,606 | 33.8 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| 12 | L1-worker | claudeopus46 | 627 | 3,422 | 4,049 | 949 | 6.7 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| 13 | L1-worker | claudeopus46 | 2,106 | 4,907 | 7,013 | 1,235 | 7.0 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| 14 | L1-worker | claudeopus46 | 2,320 | 3,542 | 5,862 | 1,170 | 7.5 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| 15 | L1-worker | claudeopus46 | 366 | 2,012 | 2,378 | 757 | 4.1 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| 16 | L1-worker | claudeopus46 | 366 | 1,360 | 1,726 | 936 | 4.5 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| 17 | L1-worker | claudeopus46 | 366 | 1,607 | 1,973 | 1,125 | 5.2 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| 18 | L1-worker | claudeopus46 | 787 | 20,735 | 21,522 | 549 | 6.6 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| 19 | L0-main | claudeopus46 | 11,581 | 20,990 | 32,571 | 3,626 | 27.4 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| 20 | L0-main | claudeopus46 | 2,106 | 4,214 | 6,320 | 721 | 5.1 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| 21 | L0-main | claudeopus46 | 2,320 | 3,513 | 5,833 | 1,135 | 7.1 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| 22 | L0-main | claudeopus46 | 366 | 1,270 | 1,636 | 815 | 3.8 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| 23 | L0-main | claudeopus46 | 366 | 1,610 | 1,976 | 1,086 | 4.9 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| 24 | L0-main | claudeopus46 | 560 | 4,273 | 4,833 | 178 | 2.9 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| 25 | L0-main | claudeopus46 | 1,156 | 5,740 | 6,896 | 815 | 5.5 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| 26 | verdict | claudeopus46 | 972 | 6,494 | 7,466 | 1,163 | 10.1 | Find blocks with viscosity or dynamic viscosity data for the (query_runs/run_8) |
| 1 | L0-main | claudeopus46 | 11,581 | 865 | 12,446 | 1,272 | 8.2 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,219 | 25,314 | 839 | 5.9 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 3 | L1-worker | claudeopus46 | 24,095 | 1,910 | 26,005 | 686 | 5.1 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 4 | L1-worker | claudeopus46 | 3,767 | 568 | 4,335 | 1,595 | 11.0 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 5 | L1-worker | claudeopus46 | 24,095 | 2,872 | 26,967 | 600 | 5.5 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 6 | L1-worker | claudeopus46 | 3,767 | 2,278 | 6,045 | 574 | 6.1 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 7 | L1-worker | claudeopus46 | 24,095 | 3,415 | 27,510 | 777 | 6.1 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 8 | L1-worker | claudeopus46 | 3,767 | 473 | 4,240 | 1,307 | 9.1 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 9 | L1-worker | claudeopus46 | 24,095 | 4,762 | 28,857 | 815 | 6.7 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 10 | L1-worker | claudeopus46 | 3,767 | 1,495 | 5,262 | 598 | 5.1 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 11 | L1-worker | claudeopus46 | 24,095 | 5,489 | 29,584 | 688 | 5.4 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 12 | L1-worker | claudeopus46 | 3,767 | 33,327 | 37,094 | 1,916 | 17.5 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 13 | L1-worker | claudeopus46 | 3,767 | 33,629 | 37,396 | 2,320 | 19.4 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 14 | L1-worker | claudeopus46 | 24,095 | 7,547 | 31,642 | 848 | 9.2 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 15 | L1-worker | claudeopus46 | 3,767 | 372 | 4,139 | 349 | 3.8 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 16 | L1-worker | claudeopus46 | 24,095 | 8,043 | 32,138 | 1,258 | 9.7 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 17 | L1-worker | claudeopus46 | 3,767 | 408 | 4,175 | 1,155 | 8.9 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 18 | L1-worker | claudeopus46 | 24,095 | 9,176 | 33,271 | 866 | 7.1 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 19 | L1-worker | claudeopus46 | 3,767 | 1,562 | 5,329 | 1,565 | 9.1 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 20 | L1-worker | claudeopus46 | 24,095 | 10,737 | 34,832 | 1,389 | 10.3 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 21 | L1-worker | claudeopus46 | 3,767 | 2,498 | 6,265 | 1,986 | 12.3 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 22 | L1-worker | claudeopus46 | 24,095 | 12,196 | 36,291 | 876 | 9.7 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 23 | L1-worker | claudeopus46 | 3,767 | 2,170 | 5,937 | 1,140 | 9.4 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 24 | L1-worker | claudeopus46 | 24,095 | 13,468 | 37,563 | 1,223 | 10.0 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 25 | L1-worker | claudeopus46 | 3,767 | 463 | 4,230 | 810 | 5.7 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 26 | L1-worker | claudeopus46 | 24,062 | 14,296 | 38,358 | 2,917 | 19.6 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 27 | L1-worker | claudeopus46 | 24,062 | 15,889 | 39,951 | 2,245 | 16.3 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 28 | L1-worker | claudeopus46 | 2,106 | 4,175 | 6,281 | 92 | 2.3 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 29 | L1-worker | claudeopus46 | 366 | 869 | 1,235 | 67 | 2.2 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 30 | L1-worker | claudeopus46 | 627 | 2,715 | 3,342 | 963 | 5.1 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 31 | L1-worker | claudeopus46 | 2,320 | 2,835 | 5,155 | 952 | 5.7 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 32 | L1-worker | claudeopus46 | 366 | 1,389 | 1,755 | 940 | 3.9 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 33 | L1-worker | claudeopus46 | 787 | 7,489 | 8,276 | 677 | 6.0 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 34 | L0-main | claudeopus46 | 11,581 | 11,223 | 22,804 | 2,509 | 14.6 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 35 | L0-main | claudeopus46 | 2,320 | 2,320 | 4,640 | 855 | 4.3 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 36 | L0-main | claudeopus46 | 2,106 | 3,017 | 5,123 | 723 | 5.9 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 37 | L0-main | claudeopus46 | 366 | 1,330 | 1,696 | 816 | 3.3 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 38 | L0-main | claudeopus46 | 366 | 1,272 | 1,638 | 904 | 3.9 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 39 | L0-main | claudeopus46 | 560 | 2,941 | 3,501 | 99 | 2.4 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 40 | L0-main | claudeopus46 | 1,156 | 3,619 | 4,775 | 532 | 4.4 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| 41 | verdict | claudeopus46 | 972 | 4,778 | 5,750 | 1,102 | 9.4 | Find blocks with excess molar enthalpy (HE) data for the bin (query_runs/run_6) |
| **TOTAL** |  |  | **950,170** | **505,814** | **1,455,984** | **109,569** | **794.0** |  |
