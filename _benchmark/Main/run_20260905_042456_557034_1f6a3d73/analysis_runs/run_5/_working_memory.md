# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_042456_557034_1f6a3d73\analysis_runs\run_5`

### ID Catalog
| type | global_id | name | pure_values |
|------|--------|------|-------------|
| comp | GLOBcomp_4 | methanol | 4.070376e-05 |
| comp | GLOBcomp_1 | water | 1.8068301e-05 |
| prop | GLOBprop_1 | mass density, kg/m3 |  |
| lit | GLOBlit_2825 | 10.1016/j.jct.2007.05.004 |  |
| lit | GLOBlit_8424 | 10.1021/je049691v |  |
| lit | GLOBlit_8254 | 10.1021/je034101z |  |
| lit | GLOBlit_7085 | 10.1021/acs.jced.6b01058 |  |
| lit | GLOBlit_2432 | 10.1016/j.jct.2004.07.019 |  |

### History
- [query_thermoml_parallel]
- [fit_block_derived] ERROR: Unknown transform 'density_to_excess_volume'. Available: ['density_to_molar_volu
- [fit_block_derived] ERROR: Constraint column 'Temperature, K' not found
- [fit_block_derived]
- [predict_from_rk]
- [list_session_files]

### Query Results
#### excess_volume
**L1_query_1** — status: success · validation: PASS

**Summary:** Excess molar volume (V^E) data for methanol + water at 298.15 K and 100 kPa were found in the ThermoML database from DOI 10.1016/j.jct.2004.03.011 (GLOBlit_2395, PROPblock_1, GLOBprop_28, liquid phase). At methanol mole fractions of 0.25, 0.50, and 0.75, V^E values are −7.42 × 10⁻⁷, −1.014 × 10⁻⁶, and −7.05 × 10⁻⁷ m³/mol, respectively. All values are negative, with the most negative at x = 0.50 (≈ −1.014 cm³/mol), indicating maximum volume contraction near equimolar composition due to strong hydrogen-bonding interactions. The full data block contains 206 points spanning 298.15–523.15 K, 100–60,000 kPa, and methanol mole fractions of 0.25, 0.50, and 0.75, with V^E ranging from −2.545 × 10⁻⁶ to −5 × 10⁻⁹ m³/mol across all conditions.

**Answer:**

#### Excess Molar Volume (V^E) Data for Methanol + Water at 298.15 K and Atmospheric Pressure

One data block was found in the ThermoML database containing excess molar volume measurements for the binary system methanol (CH₃OH) + water (H₂O) at 298.15 K and atmospheric pressure (100 kPa):

**Source:** DOI 10.1016/j.jct.2004.03.011 (GLOBlit_2395), PROPblock_1

**Property:** Excess molar volume (GLOBprop_28), liquid phase

**Data at T = 298.15 K, P = 100 kPa:**

**WM_L1#1_Table#1_(Analysis_L1#1_Answer):**

| *row_id* | *Mole fraction of methanol (x)* | *V^E (m³/mol)* |
|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「0.25」 | 「−7.42 × 10⁻⁷」 |
| WM_L1#1_Table#1_Row#2 | 「0.50」 | 「−1.014 × 10⁻⁶」 |
| WM_L1#1_Table#1_Row#3 | 「0.75」 | 「−7.05 × 10⁻⁷」 |

All three values are negative, which is characteristic of the methanol–water system. The most negative excess molar volume occurs at x(methanol) = 0.50 (V^E = −1.014 × 10⁻⁶ m³/mol ≈ −1.014 cm³/mol), indicating maximum volume contraction near the equimolar composition. This behavior reflects strong hydrogen-bonding interactions between methanol and water molecules that lead to a more efficient molecular packing compared to the ideal mixture.

The full block contains 206 data points spanning temperatures from 298.15 K to 523.15 K, pressures from 100 kPa to 60,000 kPa, and methanol mole fractions of 0.25, 0.50, and 0.75, with V^E values ranging from −2.545 × 10⁻⁶ to −5 × 10⁻⁹ m³/mol across all conditions.

**Core claims:**
- One ThermoML data block (DOI 10.1016/j.jct.2004.03.011, PROPblock_1) reports excess molar volume (V^E) for methanol + water in the liquid phase at 298.15 K and 100 kPa at three methanol mole fractions: V^E = −7.42 × 10⁻⁷ m³/mol at x = 0.25, V^E = −1.014 × 10⁻⁶ m³/mol at x = 0.50, and V^E = −7.05 × 10⁻⁷ m³/mol at x = 0.75.
- All three excess molar volume values are negative, with the most negative value occurring at x(methanol) = 0.50, indicating maximum volume contraction near the equimolar composition.
- The full data block contains 206 data points spanning temperatures from 298.15 K to 523.15 K, pressures from 100 kPa to 60,000 kPa, and methanol mole fractions of 0.25, 0.50, and 0.75, with V^E values ranging from −2.545 × 10⁻⁶ to −5 × 10⁻⁹ m³/mol across all conditions.

**Core blocks found:**

**WM_L1#1_Blocks_(Analysis_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#2 | 「GLOBlit_2395」 | 「PROPblock_1」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_28」 | 「Excess molar volume for methanol + water at 298.15 K and 100 kPa.」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### density_data
**L1_query_2** — status: success · validation: FLAGGED(1)

**Summary:** Density data for the methanol (GLOBcomp_4, CAS 67-56-1) + water (GLOBcomp_1, CAS 7732-18-5) binary mixture at 298.15 K and 101.0 kPa are reported from DOI 10.1016/j.jct.2007.05.004 (GLOBlit_2825, PROPblock_10). The dataset contains 13 mass density (GLOBprop_1, kg/m³) values spanning the full mole fraction range of water: 0 (787.2), 0.049 (795.47), 0.0993 (804.11), 0.1973 (821.73), 0.2983 (840.79), 0.3985 (860.59), 0.5003 (881.69), 0.5994 (902.96), 0.6997 (925.21), 0.7986 (947.17), 0.8999 (969.84), 0.9512 (982.53), and 1 (997.05). Density increases monotonically from pure methanol to pure water. The non-linear density–composition relationship reflects the well-known negative excess molar volumes arising from strong hydrogen-bonding interactions. Additional datasets potentially containing 298.15 K data were identified but not numerically inspected: DOI 10.1021/je049691v (GLOBlit_8424, PROPblock_3), DOI 10.1021/je034101z (GLOBlit_8254, PROPblock_4), DOI 10.1021/acs.jced.6b01058 (GLOBlit_7085, PROPblock_6), and DOI 10.1016/j.jct.2004.07.019 (GLOBlit_2432, PROPblock_1).

**Answer:**

#### Density Data for Methanol + Water Binary Mixture at 298.15 K

##### Best Dataset: Full Composition Coverage

**Source:** DOI 10.1016/j.jct.2007.05.004 (GLOBlit_2825, PROPblock_10)

This block contains 13 data points at exactly 298.15 K and 101.0 kPa, spanning the full mole fraction range of water from 0 (pure methanol) to 1 (pure water). The composition variable is mole fraction of water (BLKvar_2).

**WM_L1#2_Table#1_(Analysis_L1#2_Answer):**

| *row_id* | *Mole fraction water* | *Mass density (kg/m³)* |
|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「0」 | 「787.2」 |
| WM_L1#2_Table#1_Row#2 | 「0.049」 | 「795.47」 |
| WM_L1#2_Table#1_Row#3 | 「0.0993」 | 「804.11」 |
| WM_L1#2_Table#1_Row#4 | 「0.1973」 | 「821.73」 |
| WM_L1#2_Table#1_Row#5 | 「0.2983」 | 「840.79」 |
| WM_L1#2_Table#1_Row#6 | 「0.3985」 | 「860.59」 |
| WM_L1#2_Table#1_Row#7 | 「0.5003」 | 「881.69」 |
| WM_L1#2_Table#1_Row#8 | 「0.5994」 | 「902.96」 |
| WM_L1#2_Table#1_Row#9 | 「0.6997」 | 「925.21」 |
| WM_L1#2_Table#1_Row#10 | 「0.7986」 | 「947.17」 |
| WM_L1#2_Table#1_Row#11 | 「0.8999」 | 「969.84」 |
| WM_L1#2_Table#1_Row#12 | 「0.9512」 | 「982.53」 |
| WM_L1#2_Table#1_Row#13 | 「1」 | 「997.05」 |

(All 13 matched rows at 298.15 K shown.)

##### Additional Datasets Available

Several other blocks also contain methanol + water density data with temperature ranges that may include 298.15 K. These were identified in the registry search but their individual data rows were not inspected in this run, so no specific numerical details are quoted for them:

- DOI 10.1021/je049691v (GLOBlit_8424, PROPblock_3) — multi-temperature dataset with broad composition coverage
- DOI 10.1021/je034101z (GLOBlit_8254, PROPblock_4) — multi-temperature, variable-pressure dataset
- DOI 10.1021/acs.jced.6b01058 (GLOBlit_7085, PROPblock_6) — narrow mass fraction range
- DOI 10.1016/j.jct.2004.07.019 (GLOBlit_2432, PROPblock_1) — relative density, variable pressure

##### Compound IDs
- **Methanol:** GLOBcomp_4 (CH₄O, CAS 67-56-1)
- **Water:** GLOBcomp_1 (H₂O, CAS 7732-18-5)
- **Property:** Mass density (GLOBprop_1, kg/m³)

##### Chemistry Note
The GLOBlit_2825 dataset is ideal for deriving excess molar volume (V^E) at 298.15 K because it covers the complete composition range at constant atmospheric pressure. The density increases monotonically from 787.2 kg/m³ (pure methanol) to 997.05 kg/m³ (pure water). The methanol–water system is well known for exhibiting negative excess molar volumes across the entire composition range, reflecting strong hydrogen-bonding interactions and efficient molecular packing between the two components. The non-linear density–composition relationship visible in these data (the density does not follow a simple linear mixing rule) is the signature of this non-ideal volumetric behavior.

**Core claims:**
- At 298.15 K and 101.0 kPa, the mass density of the methanol + water binary mixture increases monotonically from 787.2 kg/m³ (pure methanol, mole fraction water = 0) to 997.05 kg/m³ (pure water, mole fraction water = 1), based on 13 data points spanning the full composition range from DOI 10.1016/j.jct.2007.05.004.
- The density–composition relationship is non-linear, indicating non-ideal volumetric mixing behavior consistent with the known negative excess molar volumes of the methanol–water system attributed to strong hydrogen-bonding interactions.
- Several additional datasets from other sources may contain methanol + water density data at 298.15 K, but their individual data rows were not inspected and no numerical values are quoted for them.

**Core blocks found:**

**WM_L1#2_Blocks_(Analysis_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#2 | 「GLOBlit_2825」 | 「PROPblock_10」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of methanol + water at 298.15 K and 101.0 kPa across full mole fraction range, 13 data points.」 |
| WM_L1#2_Table#3 | 「GLOBlit_8424」 | 「PROPblock_3」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of methanol + water, multi-temperature dataset with broad composition coverage.」 |
| WM_L1#2_Table#4 | 「GLOBlit_8254」 | 「PROPblock_4」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of methanol + water, multi-temperature variable-pressure dataset.」 |
| WM_L1#2_Table#5 | 「GLOBlit_7085」 | 「PROPblock_6」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of methanol + water, narrow mass fraction range.」 |
| WM_L1#2_Table#6 | 「GLOBlit_2432」 | 「PROPblock_1」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Relative density of methanol + water, variable pressure.」 |

*Not stored here: 3 verbatim data_inspections table(s); 8 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(1) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNINSPECTED_BLOCK** PROPblock_1: PROPblock_1 is quoted with data values (67, 7732, 298.15, 787.2, …) but was never inspected in this run


### Completed Fits
  - 10.1016/j.jct.2007.05.004/PROPblock_10 (water, methanol): RK order=5, R²=0.999995, RMSE=6.883050222977911e-10, coeffs=[-4e-06, -0.0, 0.0, 0.0, 1e-06, 1e-06]
      response: direct via X = reported X | 0 reference source(s) | kg/m3 -> kg/m3
      route: measured-derived (density_to_molar_volume, exact pointwise) via density_to_molar_volume
      pure refs: water=1.80683e-05, methanol=4.07038e-05 [block-edges of derived data (methanol: direct/good, water: direct/good)]
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

