# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_041158_447699_492f384b\analysis_runs\run_3`

### History
- [query_thermoml_parallel]
- [fit_block_derived] ERROR: Constraint column 'Temperature, K' not found
- [fit_block_derived]
- [predict_from_rk]
- [list_session_files]

### Query Results
#### excess_volume
**L1_query_1** — status: no_results · validation: PASS

**Summary:** A thorough search of the ThermoML database for excess molar volume (V^E, GLOBprop_28) data for the binary system water + ethanol at 298.15 K found no matching blocks. The water + ethanol system exists in the database with other properties (mass density, activity coefficient, vapor pressure, etc.), and excess molar volume data exists for other water-containing and ethanol-containing binary systems, but not for the water + ethanol combination. One candidate block (GLOBlit_1014, PROPblock_1, DOI: 10.1016/j.fluid.2011.09.016) turned out to be acetonitrile + water, not ethanol + water, with 6 data points at 298.15 K and 101.0 kPa and V^E ranging from −5.81×10⁻⁷ to −4.13×10⁻⁷ m³/mol. The database does not contain excess molar volume data for water + ethanol at 298.15 K or any other temperature.

**Answer:**

#### Excess Molar Volume (V^E) Data for Water + Ethanol at 298.15 K

##### Search Summary

A thorough search of the ThermoML database was conducted for excess molar volume (GLOBprop_28) data for the binary system of water (GLOBcomp_1) + ethanol (GLOBcomp_2) at 298.15 K. **No blocks containing excess molar volume data for the water + ethanol binary system were found in the database.**

##### What was found

**Water + ethanol binary system** exists in the database with other properties (mass density, activity coefficient, vapor pressure, etc.) across multiple DOIs, but none of these blocks report excess molar volume.

**Excess molar volume data** exists in the database for other systems involving water (e.g., water + ionic liquids, water + amines, water + methanol) and for other systems involving ethanol (e.g., ethanol + various organic solvents), but not for the water + ethanol binary combination.

For example, one inspected block (GLOBlit_1014, PROPblock_1, DOI: 10.1016/j.fluid.2011.09.016) initially appeared to contain water + ethanol V^E data, but upon inspection it was confirmed to be **acetonitrile + water** (not ethanol + water), with 6 data points at 298.15 K and 101.0 kPa, with V^E ranging from −5.81×10⁻⁷ to −4.13×10⁻⁷ m³/mol.

##### Conclusion

The ThermoML database, as indexed, **does not contain excess molar volume (V^E) data for the water + ethanol binary system** at 298.15 K or any other temperature. While both compounds appear extensively in the database individually and together (for other properties like density and vapor pressure), the specific combination of this binary system with the excess molar volume property is not present in the current dataset.

**Core claims:**
- The ThermoML database, as indexed, does not contain excess molar volume (V^E) data for the water + ethanol binary system at 298.15 K or any other temperature.
- Water + ethanol binary data exist in the database for other properties (e.g., mass density, activity coefficient, vapor pressure), but not for excess molar volume.
- Excess molar volume data exist in the database for other binary systems involving water or ethanol individually, but not for the water + ethanol combination.

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### density_data
**L1_query_2** — status: success · validation: PASS

**Summary:** Density data for the water + ethanol binary mixture at 298.15 K and 100 kPa were identified in DOI 10.1016/j.fluid.2004.11.019 (GLOBlit_220, PROPblock_2). The block contains 810 total data points across multiple temperatures and pressures, with 54 composition points at exactly 298.15 K and 100 kPa spanning ethanol mole fractions from 0.003 to 1.0. Density decreases monotonically from ~995 kg/m³ (near-pure water) to 785.7 kg/m³ (pure ethanol). Representative values include 995.3 kg/m³ at x(ethanol)=0.003, 918.5 kg/m³ at 0.2502, 859.3 kg/m³ at 0.4980, and 785.7 kg/m³ at 1.000. This dataset is suitable for deriving excess molar volume, which is known to be negative for water–ethanol due to hydrogen-bonding-driven volume contraction. Among 22 candidate blocks found for binary water–ethanol density near 298.15 K, this block was selected for its dense full-range composition coverage at atmospheric pressure.

**Answer:**

#### Density Data for Water + Ethanol Binary Mixture at 298.15 K

##### Best Candidate Block

**DOI:** 10.1016/j.fluid.2004.11.019  
**Literature ID:** GLOBlit_220  
**Block:** PROPblock_2  
**Property:** Mass density (GLOBprop_1), kg/m³  
**Compounds:** Water (GLOBcomp_1) + Ethanol (GLOBcomp_2)  
**System type:** Binary  

This block contains **810 total data points** across multiple temperatures (298.15–348.15 K) and pressures (100–40000 kPa). At the target conditions of **T = 298.15 K and P = 100 kPa (≈1 atm)**, there are **54 composition points** spanning the full mole fraction range of ethanol from 0.003 to 1.0 — excellent for deriving excess molar volume.

##### Representative Data at 298.15 K, 100 kPa

**WM_L1#2_Table#1_(Analysis_L1#2_Answer):**

| *row_id* | *BLKpoint_id* | *x(ethanol)* | *ρ (kg/m³)* |
|---|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「BLKpoint_1」 | 「0.003」 | 「995.3」 |
| WM_L1#2_Table#1_Row#2 | 「BLKpoint_6」 | 「0.0184」 | 「988.4」 |
| WM_L1#2_Table#1_Row#3 | 「BLKpoint_7」 | 「0.0219」 | 「987.6」 |
| WM_L1#2_Table#1_Row#4 | 「BLKpoint_9」 | 「0.0279」 | 「984.7」 |
| WM_L1#2_Table#1_Row#5 | 「BLKpoint_10」 | 「0.0315」 | 「984.0」 |
| WM_L1#2_Table#1_Row#6 | 「BLKpoint_11」 | 「0.0366」 | 「981.6」 |
| WM_L1#2_Table#1_Row#7 | 「BLKpoint_14」 | 「0.0483」 | 「977.5」 |
| WM_L1#2_Table#1_Row#8 | 「BLKpoint_15」 | 「0.0516」 | 「977.1」 |
| WM_L1#2_Table#1_Row#9 | 「BLKpoint_21」 | 「0.0801」 | 「968.6」 |
| WM_L1#2_Table#1_Row#10 | 「BLKpoint_24」 | 「0.0926」 | 「965.6」 |
| WM_L1#2_Table#1_Row#11 | 「BLKpoint_29」 | 「0.1296」 | 「954.9」 |
| WM_L1#2_Table#1_Row#12 | 「BLKpoint_38」 | 「0.2502」 | 「918.5」 |
| WM_L1#2_Table#1_Row#13 | 「BLKpoint_40」 | 「0.3009」 | 「904.5」 |
| WM_L1#2_Table#1_Row#14 | 「BLKpoint_41」 | 「0.3500」 | 「891.9」 |
| WM_L1#2_Table#1_Row#15 | 「BLKpoint_43」 | 「0.4501」 | 「868.8」 |
| WM_L1#2_Table#1_Row#16 | 「BLKpoint_44」 | 「0.4980」 | 「859.3」 |
| WM_L1#2_Table#1_Row#17 | 「BLKpoint_45」 | 「0.5501」 | 「849.5」 |
| WM_L1#2_Table#1_Row#18 | 「BLKpoint_47」 | 「0.6489」 | 「832.7」 |
| WM_L1#2_Table#1_Row#19 | 「BLKpoint_48」 | 「0.6967」 | 「825.2」 |
| WM_L1#2_Table#1_Row#20 | 「BLKpoint_51」 | 「0.8484」 | 「804.4」 |
| WM_L1#2_Table#1_Row#21 | 「BLKpoint_54」 | 「1.000」 | 「785.7」 |

(Shape-preserving RDP sampling of the 54 matched rows at these conditions; the full block contains additional intermediate compositions.)

##### Chemistry Note

The density decreases monotonically from near-pure water (~995 kg/m³) to pure ethanol (~786 kg/m³). To derive excess molar volume (V^E), one would compute V_mix = (x₁M₁ + x₂M₂)/ρ_mix and subtract the ideal volume V_ideal = x₁V₁* + x₂V₂*, where V_i* = Mᵢ/ρᵢ*. The water–ethanol system is well known for exhibiting negative excess molar volumes (volume contraction upon mixing), reflecting strong hydrogen-bonding interactions between water and ethanol molecules.

##### Search Overview

A total of **22 blocks** of mass density data were found for binary water–ethanol systems near 298.15 K (the search used a temperature window up to 300 K). The GLOBlit_220::PROPblock_2 block stands out for its 54 atmospheric-pressure composition points at exactly 298.15 K, providing dense coverage across the full mole fraction range — ideal for accurate V^E derivation.

**Core claims:**
- A ThermoML block (DOI 10.1016/j.fluid.2004.11.019, GLOBlit_220, PROPblock_2) provides mass density data for the water + ethanol binary system with 54 composition points at T = 298.15 K and P = 100 kPa, spanning ethanol mole fractions from 0.003 to 1.0.
- At 298.15 K and 100 kPa, the measured density decreases monotonically from approximately 995 kg/m³ near pure water to approximately 786 kg/m³ for pure ethanol.
- The water–ethanol system is well known for exhibiting negative excess molar volumes (volume contraction upon mixing), attributed to strong hydrogen-bonding interactions between water and ethanol molecules.
- Among 22 blocks of mass density data found for binary water–ethanol systems near 298.15 K, the selected block provides the densest atmospheric-pressure composition coverage across the full mole fraction range.

**Core blocks found:**

**WM_L1#2_Blocks_(Analysis_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#2 | 「GLOBlit_220」 | 「PROPblock_2」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density data for water + ethanol binary mixture at 298.15–348.15 K and 100–40000 kPa; 810 total data points with 54 composition points at 298.15 K and 100 kPa spanning x(ethanol) = 0.003 to 1.0.」 |

*Not stored here: 2 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


### Completed Fits
  - 10.1016/j.fluid.2004.11.019/PROPblock_2 (ethanol, water): RK order=5, R²=0.979248, RMSE=4.208680076125661e-08, coeffs=[-5e-06, 3e-06, -1e-06, -5e-06, -3e-06, 9e-06]
      response: direct via X = reported X | 0 reference source(s) | kg/m3 -> kg/m3
      route: measured-derived (density_to_molar_volume, exact pointwise) via density_to_molar_volume
      pure refs: ethanol=5.86343e-05, water=1.84491e-05 [block-edges of derived data (water: direct/good, ethanol: direct/good)]
      fit_csv: $ROOT/data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_excess.png

## Session Output Files

### data
- `$ROOT/data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_fit.csv` — RK fit data — 10.1016/j.fluid.2004.11.019 PROPblock_2_T298.1
- `$ROOT/data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_excess.csv` — Excess property — 10.1016/j.fluid.2004.11.019 PROPblock_2_T298.1

### plot
- `$ROOT/plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_fit.png` — RK fit plot — 10.1016/j.fluid.2004.11.019 PROPblock_2_T298.1
- `$ROOT/plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_excess.png` — Excess plot — 10.1016/j.fluid.2004.11.019 PROPblock_2_T298.1

