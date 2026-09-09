# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_041134_447586_bd903d48\analysis_runs\run_1`

### ID Catalog
| type | global_id | name | pure_values |
|------|--------|------|-------------|
| comp | GLOBcomp_4 | methanol | 787.2 |
| comp | GLOBcomp_1 | water | 997.05 |
| prop | GLOBprop_1 | massdensitykgm3 |  |
| var | GLOBvar_1 | temperaturek |  |
| var | GLOBvar_2 | molefraction<water> |  |
| constr | GLOBconstr_1 | pressurekpa |  |

### History
- [query_thermoml]
- [inspect_block]
- [fit_block] ERROR: Constraint column 'Temperature, K' not found in block
- [fit_block]

### Query Results
#### query
**L1_query_1** — status: success · validation: PASS

**Summary:** Composition-dependent mass density data for the binary methanol + water system at 298.15 K and 101 kPa were identified in the ThermoML database. The best data block comes from DOI 10.1016/j.jct.2007.05.004 (Literature ID GLOBlit_2825, PROPblock_10), containing 13 data points at 298.15 K spanning the full mole-fraction range of water from 0 to 1. Density increases monotonically from 787.2 kg/m³ (pure methanol, x_water = 0) to 997.05 kg/m³ (pure water, x_water = 1), with intermediate values of 795.47 (0.049), 804.11 (0.0993), 821.73 (0.1973), 840.79 (0.2983), 860.59 (0.3985), 881.69 (0.5003), 902.96 (0.5994), 947.17 (0.7986), 969.84 (0.8999), and 982.53 kg/m³ (0.9512). The non-linear composition dependence reflects non-ideal mixing with negative excess volume due to hydrogen-bonding interactions. Nine total binary methanol + water density blocks near 298.15 K from multiple literature sources were found; the selected block was chosen for its broad composition coverage and number of data points.

**Answer:**

#### Density Data for Binary Methanol + Water Mixture at 298.15 K

A comprehensive composition-dependent mass density dataset for the binary methanol + water system at 298.15 K and atmospheric pressure (101 kPa) was found in the ThermoML database.

##### Best Data Block

**Source:** DOI 10.1016/j.jct.2007.05.004  
**Literature ID:** GLOBlit_2825  
**Block:** PROPblock_10  
**System:** Binary (methanol + water)  
**Total data points in block:** 39 (across 293.15–303.15 K); **13 points at 298.15 K** covering the full composition range (mole fraction of water from 0 to 1).

##### Density vs. Composition at 298.15 K (101 kPa)

**WM_L1#1_Table#1_(Analysis_L1#1_Answer):**

| *row_id* | *Mole fraction of water* | *Mass density (kg/m³)* |
|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「0 (pure methanol)」 | 「787.2」 |
| WM_L1#1_Table#1_Row#2 | 「0.049」 | 「795.47」 |
| WM_L1#1_Table#1_Row#3 | 「0.0993」 | 「804.11」 |
| WM_L1#1_Table#1_Row#4 | 「0.1973」 | 「821.73」 |
| WM_L1#1_Table#1_Row#5 | 「0.2983」 | 「840.79」 |
| WM_L1#1_Table#1_Row#6 | 「0.3985」 | 「860.59」 |
| WM_L1#1_Table#1_Row#7 | 「0.5003」 | 「881.69」 |
| WM_L1#1_Table#1_Row#8 | 「0.5994」 | 「902.96」 |
| WM_L1#1_Table#1_Row#9 | 「0.7986」 | 「947.17」 |
| WM_L1#1_Table#1_Row#10 | 「0.8999」 | 「969.84」 |
| WM_L1#1_Table#1_Row#11 | 「0.9512」 | 「982.53」 |
| WM_L1#1_Table#1_Row#12 | 「1 (pure water)」 | 「997.05」 |

##### Chemistry Insight

The density increases monotonically from pure methanol (787.2 kg/m³) to pure water (997.05 kg/m³) at 298.15 K. The progression is not perfectly linear with mole fraction — the curvature reflects non-ideal mixing behavior characteristic of the methanol–water system, where hydrogen-bonding interactions between the two components lead to volume contraction (negative excess volume) upon mixing.

##### Additional Blocks Found

The search returned 9 total binary methanol + water density blocks near 298.15 K from multiple literature sources. The block above (PROPblock_10 from GLOBlit_2825) was selected as the best candidate due to its broad composition coverage (full 0–1 range) and numerous data points at the target temperature.

**Core claims:**
- A composition-dependent mass density dataset for binary methanol + water at 298.15 K and 101 kPa was identified in ThermoML (DOI 10.1016/j.jct.2007.05.004, PROPblock_10), providing 13 data points spanning the full mole-fraction range of water from 0 to 1.
- At 298.15 K, the mass density increases monotonically from 787.2 kg/m³ for pure methanol to 997.05 kg/m³ for pure water.
- The density–composition relationship is not perfectly linear with mole fraction; the curvature reflects non-ideal mixing behavior attributed to hydrogen-bonding interactions that produce volume contraction (negative excess volume) upon mixing.
- Nine total binary methanol + water density blocks near 298.15 K from multiple literature sources were found; the selected block was chosen for its broad composition coverage across the full 0–1 mole-fraction range.

**Core blocks found:**

**WM_L1#1_Blocks_(Analysis_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#2 | 「GLOBlit_2825」 | 「PROPblock_10」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density measurements for binary methanol + water mixture at 298.15 K (101 kPa), 13 data points covering full mole fraction range 0–1.」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


### Inspected Blocks
- GLOBlit_2825 | 10.1016/j.jct.2007.05.004 | PROPblock_10: 39 rows; x=['mole_fraction_<water>']; y=['mass_density_kg_m3']
    - BLKprop_1 / GLOBprop_1: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_1: kind=direct; materialize_reference=False; supported=True; units=kg/m3 -> kg/m3

### Completed Fits
  - 10.1016/j.jct.2007.05.004/PROPblock_10 (water, methanol): RK order=5, R²=0.999796, RMSE=0.03885240667464569, coeffs=[-42.310758, 2.461285, 7.280933, -0.41971, -46.15381, -43.843096]
      response: direct via X = reported X | 0 reference source(s) | kg/m3 -> kg/m3
      pure refs: water=997.05, methanol=787.2 [block-edges (methanol: direct/good, water: direct/good)]
      fit_csv: $ROOT/data\10_1016_j_jct_2007_05_004_BPROPblock_10_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1016_j_jct_2007_05_004_BPROPblock_10_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_jct_2007_05_004_BPROPblock_10_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1016_j_jct_2007_05_004_BPROPblock_10_T298.1_excess.png

## Session Output Files

### data
- `$ROOT/data\10_1016_j_jct_2007_05_004_BPROPblock_10_T298.1_fit.csv` — RK fit data — 10.1016/j.jct.2007.05.004 PROPblock_10_T298.1
- `$ROOT/data\10_1016_j_jct_2007_05_004_BPROPblock_10_T298.1_excess.csv` — Excess property — 10.1016/j.jct.2007.05.004 PROPblock_10_T298.1

### plot
- `$ROOT/plots\10_1016_j_jct_2007_05_004_BPROPblock_10_T298.1_fit.png` — RK fit plot — 10.1016/j.jct.2007.05.004 PROPblock_10_T298.1
- `$ROOT/plots\10_1016_j_jct_2007_05_004_BPROPblock_10_T298.1_excess.png` — Excess plot — 10.1016/j.jct.2007.05.004 PROPblock_10_T298.1

