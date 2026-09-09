# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_042456_557034_1f6a3d73\analysis_runs\run_6`

### ID Catalog
| type | global_id | name | pure_values |
|------|--------|------|-------------|
| comp | GLOBcomp_1 | water | 1.8449115e-05 |
| comp | GLOBcomp_2 | ethanol | 5.8634339e-05 |
| prop | GLOBprop_1 | massdensitykgm3 |  |
| var | GLOBvar_1 | temperaturek |  |
| var | GLOBvar_3 | pressurekpa |  |
| var | GLOBvar_2 | molefraction<ethanol> |  |
| lit | GLOBlit_220 | 10.1016/j.fluid.2004.11.019 |  |

### History
- [query_thermoml_parallel]
- [inspect_block]
- [fit_block_derived] ERROR: Constraint column 'Temperature, K' not found
- [fit_block_derived]
- [predict_from_rk]
- [list_session_files]

### Query Results
#### excess_volume_direct
**L1_query_1** — status: no_results · validation: PASS

**Summary:** A comprehensive search of the ThermoML database found that both ethanol and water are present as compounds, and excess molar volume (V^E) exists as a property for other systems, but no excess molar volume data for the ethanol + water binary system is recorded. Ethanol + water data exists for other properties — mass density, mole fraction/VLE, activity coefficient, viscosity, and vapor pressure — but not for V^E. Density data for this pair could in principle be used to derive V^E, but no direct V^E entries exist in the database.

**Answer:**

**Excess molar volume (V^E) data for ethanol + water at 298.15 K: Not found in the ThermoML database.**

A comprehensive search was conducted:

- **Compounds confirmed:** ethanol (GLOBcomp_2) and water (GLOBcomp_1) are both present in the database.
- **Property confirmed:** Excess molar volume (GLOBprop_28, m³/mol) exists in the database and is recorded for other binary and ternary systems (e.g., in DOIs 10.1007/s10765-010-0717-9 [GLOBlit_92] and 10.1016/j.fluid.2005.06.011 [GLOBlit_276]), but **none of those blocks involve ethanol or water**.
- **Ethanol + water binary data exists** for other properties — mass density (GLOBprop_1, 12 blocks), mole fraction / VLE (GLOBprop_2, 9 blocks), activity coefficient (GLOBprop_3, 4 blocks), viscosity (GLOBprop_4, 4 blocks), and vapor pressure (GLOBprop_5, 5 blocks) — but no excess molar volume blocks were found for this pair under any scope (declared or subsystem).

In summary, the ThermoML database does not contain excess molar volume (V^E) measurements for the ethanol + water binary system. Density data (GLOBprop_1) is available for this system and could, in principle, be used to derive V^E if pure-component densities are also available, but no direct V^E entries exist.

**Core claims:**
- The ThermoML database does not contain excess molar volume (V^E) measurements for the ethanol + water binary system at 298.15 K, despite both compounds and the V^E property being present in the database for other systems.
- Ethanol + water binary data exists in the database for other properties (mass density, mole fraction/VLE, activity coefficient, viscosity, vapor pressure) but not for excess molar volume.
- Density data for ethanol + water is available in the database and could in principle be used to derive V^E, but no direct V^E entries exist.

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### density_ethanol_water
**L1_query_2** — status: success · validation: PASS

**Summary:** Density data for the ethanol (GLOBcomp_2) + water (GLOBcomp_1) binary mixture at 298.15 K and ~100 kPa are available from ThermoML, primarily from GLOBlit_220 (DOI: 10.1016/j.fluid.2004.11.019), PROPblock_2, reporting mass density (GLOBprop_1, kg/m³). This block contains 54 data points at 298.15 K spanning ethanol mole fractions from 0.003 to 1.0, with density decreasing monotonically from ~995.3 kg/m³ (near-pure water) to 785.7 kg/m³ (pure ethanol). The full 54-point dataset provides sufficient composition resolution for computing excess molar volumes. The same block contains 810 total data points covering 298.15–348.15 K and 100–40,000 kPa. Twenty-two total blocks of ethanol+water binary density data near 298.15 K were found across multiple literature sources for cross-validation.

**Answer:**

#### Density Data for Ethanol + Water Binary Mixture at 298.15 K

The ThermoML database contains extensive density data for the ethanol (GLOBcomp_2) + water (GLOBcomp_1) binary system at 298.15 K and atmospheric pressure (~100 kPa), suitable for deriving excess molar volume.

##### Primary Data Source

**DOI:** 10.1016/j.fluid.2004.11.019  
**Literature ID:** GLOBlit_220  
**Block:** PROPblock_2  
**Property:** Mass density (GLOBprop_1), kg/m³  
**Total data points at 298.15 K, 100 kPa:** 54 points spanning the full composition range (ethanol mole fraction 0.003 to 1.0)

##### Representative Data Points (298.15 K, 100 kPa)

**WM_L1#2_Table#1_(Analysis_L1#2_Answer):**

| *row_id* | *Ethanol mole fraction* | *Mass density (kg/m³)* |
|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「0.003」 | 「995.3」 |
| WM_L1#2_Table#1_Row#2 | 「0.0184」 | 「988.4」 |
| WM_L1#2_Table#1_Row#3 | 「0.0279」 | 「984.7」 |
| WM_L1#2_Table#1_Row#4 | 「0.0483」 | 「977.5」 |
| WM_L1#2_Table#1_Row#5 | 「0.0801」 | 「968.6」 |
| WM_L1#2_Table#1_Row#6 | 「0.1296」 | 「954.9」 |
| WM_L1#2_Table#1_Row#7 | 「0.2502」 | 「918.5」 |
| WM_L1#2_Table#1_Row#8 | 「0.3009」 | 「904.5」 |
| WM_L1#2_Table#1_Row#9 | 「0.35」 | 「891.9」 |
| WM_L1#2_Table#1_Row#10 | 「0.4501」 | 「868.8」 |
| WM_L1#2_Table#1_Row#11 | 「0.498」 | 「859.3」 |
| WM_L1#2_Table#1_Row#12 | 「0.5501」 | 「849.5」 |
| WM_L1#2_Table#1_Row#13 | 「0.6489」 | 「832.7」 |
| WM_L1#2_Table#1_Row#14 | 「0.6967」 | 「825.2」 |
| WM_L1#2_Table#1_Row#15 | 「0.8484」 | 「804.4」 |
| WM_L1#2_Table#1_Row#16 | 「1.0」 | 「785.7」 |

The density decreases monotonically from near-pure water (~995.3 kg/m³) to pure ethanol (785.7 kg/m³). The full 54-point dataset at this isotherm provides excellent composition resolution for computing excess molar volumes via V^E = V_mix − Σ x_i V_i*, where pure component molar volumes can be obtained from the endpoint densities (x_ethanol = 0 and x_ethanol = 1).

##### Additional Data Availability

The search returned **22 total blocks** of ethanol+water binary density data near 298.15 K across multiple literature sources, so additional datasets are available for cross-validation if needed. The block above (GLOBlit_220::PROPblock_2) contains 810 total data points spanning 298.15–348.15 K and pressures from 100 to 40,000 kPa, making it also useful for temperature- and pressure-dependent studies.

##### Key Identifiers
- **Ethanol:** GLOBcomp_2 (C₂H₆O, CCO)
- **Water:** GLOBcomp_1 (H₂O)
- **Mass density:** GLOBprop_1 (kg/m³)
- **Literature:** GLOBlit_220 (DOI: 10.1016/j.fluid.2004.11.019)
- **Block:** PROPblock_2

**Core claims:**
- The ThermoML database contains 54 density data points for the ethanol + water binary system at 298.15 K and ~100 kPa, spanning ethanol mole fractions from 0.003 to 1.0, sourced from DOI 10.1016/j.fluid.2004.11.019.
- Mass density decreases monotonically from ~995.3 kg/m³ near pure water to 785.7 kg/m³ for pure ethanol at 298.15 K and 100 kPa.
- The 54-point dataset provides sufficient composition resolution for computing excess molar volumes via V^E = V_mix − Σ x_i V_i*, using pure component molar volumes from the endpoint densities.
- 22 total blocks of ethanol + water binary density data near 298.15 K are available across multiple literature sources for cross-validation.

**Core blocks found:**

**WM_L1#2_Blocks_(Analysis_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#2 | 「GLOBlit_220」 | 「PROPblock_2」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density (kg/m³) of ethanol + water binary mixture; 54 data points at 298.15 K and 100 kPa spanning ethanol mole fraction 0.003 to 1.0; 810 total points across 298.15–348.15 K and 100–40000 kPa.」 |

*Not stored here: 1 verbatim data_inspections table(s); 4 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


### Inspected Blocks
- GLOBlit_220 | 10.1016/j.fluid.2004.11.019 | PROPblock_2: 810 rows; x=['mole_fraction_<ethanol>']; y=['mass_density_kg_m3']
    - BLKprop_1 / GLOBprop_1: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_1: kind=direct; materialize_reference=False; supported=True; units=kg/m3 -> kg/m3

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

