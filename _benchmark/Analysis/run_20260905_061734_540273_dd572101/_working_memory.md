# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_061734_540273_dd572101`

### History
- [query_thermoml]
- [fit_block] ERROR: Constraint column 'Temperature, K' not found in block
- [fit_block]
- [compute_ideal_baseline]
- [predict_from_rk]
- [list_session_files]

### Query Results
#### query
**L1_query_1** — status: success · validation: PASS

**Summary:** Speed of sound data for binary ethanol + water mixtures near 298.15 K were found in three fully inspected ThermoML data blocks. PROPblock_20 (GLOBlit_5201, DOI: 10.1016/j.jct.2018.02.022) is the most comprehensive, with 152 data points spanning the full mole-fraction range (x(ethanol) = 0–1) at 293.15–308.15 K and 92.3 kPa, with speed of sound ranging from 1109.59 to 1625.74 m/s; at 298.15 K representative values include 1496.99 m/s (pure water), 1618.97 m/s (x = 0.0997), and 1143.50 m/s (pure ethanol), showing the well-known maximum near x ≈ 0.1. PROPblock_8 (GLOBlit_4415, DOI: 10.1016/j.jct.2015.06.024) provides 40 points in the dilute ethanol regime (molality 0.02159–0.21882 mol/kg) at 288.15–308.15 K and 84.5 kPa, with speed of sound 1467.43–1525.49 m/s. PROPblock_19 (GLOBlit_8888, DOI: 10.1021/je0601098) gives 12 isothermal points at exactly 298.15 K and 101.0 kPa on the ethanol-rich side (water molality 0–1.01891 mol/kg in ethanol), with speed of sound 1142.1–1160.1 m/s increasing monotonically with water content. A fourth block was identified but not fully inspected.

**Answer:**

#### Speed of Sound Data for Binary Ethanol + Water Mixtures near 298.15 K

Four data blocks were found in the ThermoML database containing speed of sound measurements for binary ethanol (GLOBcomp_2) + water (GLOBcomp_1) mixtures at or near 298.15 K. Three were fully inspected:

##### 1. PROPblock_20 — GLOBlit_5201 (DOI: 10.1016/j.jct.2018.02.022)
- **Data points:** 152
- **Composition variable:** Mole fraction of ethanol, range 0–1 (full binary range including pure endpoints)
- **Temperature range:** 293.15–308.15 K
- **Pressure:** 92.3 kPa (fixed constraint)
- **Speed of sound range:** 1109.59–1625.74 m/s

This is the most comprehensive dataset, spanning the entire composition range at four temperatures. At 298.15 K, representative inspected values include:
- x(ethanol) = 0: 1496.99 m/s (pure water)
- x(ethanol) = 0.0997: 1618.97 m/s
- x(ethanol) = 0.1497: 1600.11 m/s
- x(ethanol) = 0.3507: 1426.17 m/s
- x(ethanol) = 0.5002: 1337.91 m/s
- x(ethanol) = 1: 1143.50 m/s (pure ethanol)

The data show the well-known speed-of-sound maximum in the water-rich region (near x ≈ 0.1) before decreasing through the ethanol-rich side.

##### 2. PROPblock_8 — GLOBlit_4415 (DOI: 10.1016/j.jct.2015.06.024)
- **Data points:** 40
- **Composition variable:** Molality of ethanol (solvent: water), range 0.02159–0.21882 mol/kg
- **Temperature range:** 288.15–308.15 K
- **Pressure:** 84.5 kPa (fixed constraint)
- **Speed of sound range:** 1467.43–1525.49 m/s

This dataset covers only the dilute ethanol regime but spans a broader temperature window. At 298.15 K, inspected values include:
- m = 0.02159 mol/kg: 1497.50 m/s
- m = 0.08646 mol/kg: 1499.71 m/s
- m = 0.21882 mol/kg: 1503.85 m/s

##### 3. PROPblock_19 — GLOBlit_8888 (DOI: 10.1021/je0601098)
- **Data points:** 12
- **Composition variable:** Molality of water (in ethanol as solvent), range 0–1.01891 mol/kg
- **Temperature:** 298.15 K (fixed constraint, exactly at target temperature)
- **Pressure:** 101.0 kPa (fixed constraint)
- **Speed of sound range:** 1142.1–1160.1 m/s

This dataset is isothermal at exactly 298.15 K and covers the ethanol-rich side of the binary. Speed of sound increases monotonically with water molality, from 1142.1 m/s (pure ethanol) to 1160.1 m/s at 1.01891 mol/kg water.

A fourth block was also identified in the initial search but was not fully inspected.

##### Summary

For full-composition-range coverage at near-298.15 K, **PROPblock_20 (GLOBlit_5201)** is the most suitable dataset with 152 points spanning x(ethanol) = 0 to 1. For isothermal data at exactly 298.15 K on the ethanol-rich side, **PROPblock_19 (GLOBlit_8888)** provides 12 points. For dilute aqueous ethanol with temperature dependence, **PROPblock_8 (GLOBlit_4415)** offers 40 points across 288.15–308.15 K.

**Core claims:**
- Four ThermoML data blocks were identified containing speed of sound measurements for binary ethanol + water mixtures at or near 298.15 K; three were fully inspected.
- PROPblock_20 (GLOBlit_5201, DOI: 10.1016/j.jct.2018.02.022) is the most comprehensive dataset, with 152 data points spanning the full ethanol mole fraction range (0–1) at 293.15–308.15 K and 92.3 kPa, with speed of sound values ranging from 1109.59 to 1625.74 m/s.
- At 298.15 K in PROPblock_20, the data show the well-known speed-of-sound maximum in the water-rich region (near x(ethanol) ≈ 0.1), with representative values including 1496.99 m/s at x = 0 (pure water), 1618.97 m/s at x = 0.0997, and 1143.50 m/s at x = 1 (pure ethanol).
- PROPblock_8 (GLOBlit_4415, DOI: 10.1016/j.jct.2015.06.024) provides 40 data points covering only the dilute ethanol regime (molality 0.02159–0.21882 mol/kg) at 288.15–308.15 K and 84.5 kPa, with speed of sound values from 1467.43 to 1525.49 m/s.
- PROPblock_19 (GLOBlit_8888, DOI: 10.1021/je0601098) provides 12 isothermal data points at exactly 298.15 K and 101.0 kPa on the ethanol-rich side (water molality 0–1.01891 mol/kg in ethanol as solvent), with speed of sound increasing monotonically from 1142.1 m/s (pure ethanol) to 1160.1 m/s.

**Core blocks found:**

**WM_L1#1_Blocks_(Analysis_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#1 | 「GLOBlit_5201」 | 「PROPblock_20」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_8」 | 「Speed of sound for ethanol + water over full composition range (x=0–1) at 293.15–308.15 K, 152 data points.」 |
| WM_L1#1_Table#2 | 「GLOBlit_4415」 | 「PROPblock_8」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_8」 | 「Speed of sound for dilute ethanol in water (molality 0.02159–0.21882 mol/kg) at 288.15–308.15 K, 40 data points.」 |
| WM_L1#1_Table#3 | 「GLOBlit_8888」 | 「PROPblock_19」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_8」 | 「Speed of sound for water in ethanol (molality 0–1.01891 mol/kg) at exactly 298.15 K, 12 data points.」 |

*Not stored here: 3 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


### Completed Fits
  - 10.1016/j.jct.2018.02.022/PROPblock_20 (ethanol, water): RK order=4, R²=0.992788, RMSE=5.0129896042325095, coeffs=[47.720078, -241.964998, 744.598283, -1251.738975, 643.919105]
      response: direct via X = reported X | 0 reference source(s) | m/s -> m/s
      pure refs: ethanol=1147.54, water=1499.22 [block-edges (water: direct/good, ethanol: direct/good)]
      fit_csv: $ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_20_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_20_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_20_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_20_T298.1_excess.png

## Session Output Files

### data
- `$ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_20_T298.1_fit.csv` — RK fit data — 10.1016/j.jct.2018.02.022 PROPblock_20_T298.1
- `$ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_20_T298.1_excess.csv` — Excess property — 10.1016/j.jct.2018.02.022 PROPblock_20_T298.1

### plot
- `$ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_20_T298.1_fit.png` — RK fit plot — 10.1016/j.jct.2018.02.022 PROPblock_20_T298.1
- `$ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_20_T298.1_excess.png` — Excess plot — 10.1016/j.jct.2018.02.022 PROPblock_20_T298.1

