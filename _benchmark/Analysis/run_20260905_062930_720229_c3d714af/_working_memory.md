# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_062930_720229_c3d714af`

### ID Catalog
| type | global_id | name | pure_values |
|------|--------|------|-------------|
| comp | GLOBcomp_1 | water | 0.0008385 |
| comp | GLOBcomp_2 | ethanol | 0.00099196 |
| prop | GLOBprop_4 | viscositypas |  |
| var | GLOBvar_1 | temperaturek |  |
| var | GLOBvar_2 | molefraction<ethanol> |  |
| constr | GLOBconstr_1 | pressurekpa |  |
| lit | GLOBlit_5201 | 10.1016/j.jct.2018.02.022 |  |
| lit | GLOBlit_11136 | 10.1021/je800150h |  |

### History
- [query_thermoml]
- [inspect_block]
- [fit_block]
- [fit_multi_system]
- [fit_multi_system]
- [predict_from_rk]
- [predict_from_rk]
- [predict_from_rk]
- [predict_from_rk]

### Query Results
#### query
**L1_query_1** — status: success · validation: FLAGGED(3)

**Summary:** Viscosity data for the ethanol + water binary liquid system were identified across multiple ThermoML datasets. The best composition-coverage dataset is from DOI 10.1016/j.jct.2018.02.022 (GLOBlit_5201, PROPblock_21), containing 100 data points at 293.15–308.15 K over the full mole fraction range x(ethanol) = 0 to 1 at 92.3 kPa. At 298.15 K, 25 data points span the entire composition range and reveal the well-known viscosity maximum near x(ethanol) ≈ 0.25, where viscosity reaches 0.0024286 Pa·s compared to 0.00089689 Pa·s for pure water and 0.0010914 Pa·s for pure ethanol. This maximum is attributed to strong hydrogen-bonding interactions creating structured molecular clusters at intermediate compositions. The best temperature-coverage dataset is from DOI 10.1021/je800150h (GLOBlit_11136, PROPblock_8), with 108 data points spanning 268.1–323.15 K at x(water) = 0.1–0.9 and 101.0 kPa, with viscosities ranging from 0.00076 to 0.007549 Pa·s. At 298.15 K and x(water) = 0.7, viscosity is 0.00235 Pa·s; the highest viscosity (0.007549 Pa·s) occurs at x(water) = 0.8 and T = 268.1 K, illustrating strong temperature dependence of the viscosity maximum.

**Answer:**

#### Viscosity Data for Ethanol + Water Binary Mixtures

##### Best Dataset: Full Composition Range at 298.15 K

**DOI:** 10.1016/j.jct.2018.02.022 [GLOBlit_5201] — PROPblock_21  
- **System:** binary ethanol (GLOBcomp_2) + water (GLOBcomp_1), liquid phase  
- **Total data points:** 100  
- **Temperature range:** 293.15–308.15 K (multiple isotherms including 298.15 K)  
- **Composition range:** x(ethanol) = 0 to 1 (full range)  
- **Pressure:** 92.3 kPa (fixed constraint)

At **T = 298.15 K**, 25 data points span the entire mole fraction range. Representative inspected values:

**WM_L1#1_Table#1_(Analysis_L1#1_Answer):**

| *row_id* | *x(ethanol)* | *Viscosity (Pa·s)* |
|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「0」 | 「0.00089689」 |
| WM_L1#1_Table#1_Row#2 | 「0.0201」 | 「0.001098」 |
| WM_L1#1_Table#1_Row#3 | 「0.1004」 | 「0.0019469」 |
| WM_L1#1_Table#1_Row#4 | 「0.1499」 | 「0.0022424」 |
| WM_L1#1_Table#1_Row#5 | 「0.1984」 | 「0.0023706」 |
| WM_L1#1_Table#1_Row#6 | 「0.2499」 | 「0.0024286」 |
| WM_L1#1_Table#1_Row#7 | 「0.3499」 | 「0.0022633」 |
| WM_L1#1_Table#1_Row#8 | 「0.399」 | 「0.0021697」 |
| WM_L1#1_Table#1_Row#9 | 「0.4989」 | 「0.0019557」 |
| WM_L1#1_Table#1_Row#10 | 「0.5495」 | 「0.0018796」 |
| WM_L1#1_Table#1_Row#11 | 「0.6067」 | 「0.0017439」 |
| WM_L1#1_Table#1_Row#12 | 「0.6956」 | 「0.0015722」 |
| WM_L1#1_Table#1_Row#13 | 「0.8475」 | 「0.0013415」 |
| WM_L1#1_Table#1_Row#14 | 「1」 | 「0.0010914」 |

**Chemistry insight:** The data clearly show the well-known viscosity maximum in the ethanol–water system. At 298.15 K, viscosity peaks near x(ethanol) ≈ 0.25 (0.0024286 Pa·s). From the inspected values, the peak-to-pure-water ratio is 0.0024286 / 0.00089689 ≈ 2.7 (computed), and the peak-to-pure-ethanol ratio is 0.0024286 / 0.0010914 ≈ 2.2 (computed). This maximum arises from strong hydrogen-bonding interactions between ethanol and water molecules, which create more structured, less mobile molecular clusters at intermediate compositions.

##### Second Largest Dataset: Wide Temperature Range

**DOI:** 10.1021/je800150h [GLOBlit_11136] — PROPblock_8  
- **Total data points:** 108  
- **Temperature range:** 268.1–323.15 K (much wider T coverage)  
- **Composition range:** x(water) = 0.1–0.9 (note: composition variable is mole fraction of water)  
- **Pressure:** 101.0 kPa (fixed constraint)  
- **Viscosity range:** 0.00076–0.007549 Pa·s

This block covers multiple compositions at multiple temperatures. At 298.15 K, an inspected data point at x(water) = 0.7 gives viscosity = 0.00235 Pa·s. The highest viscosity in the block (0.007549 Pa·s) occurs at x(water) = 0.8 and T = 268.1 K, illustrating the strong temperature dependence of the viscosity maximum. This dataset is particularly valuable for studying the temperature dependence of the viscosity–composition relationship across a range of 323.15 − 268.1 = 55.05 K (computed from the inspected temperature bounds).

##### Summary of All Found Blocks

The initial search returned a total of 14 viscosity blocks (from the search_blocks discovery query) for the ethanol + water binary system, all in the liquid phase. The two datasets above offer the best combination of composition coverage (GLOBlit_5201, full x range at 298.15 K) and temperature coverage (GLOBlit_11136, 268.1–323.15 K across x(water) = 0.1–0.9) for studying composition-dependent dynamic viscosity at and around 298.15 K.

**Core claims:**
- At 298.15 K and 92.3 kPa, liquid-phase dynamic viscosity data for ethanol + water spanning x(ethanol) = 0 to 1 (25 data points, DOI 10.1016/j.jct.2018.02.022) show a well-known viscosity maximum near x(ethanol) ≈ 0.25, with a peak value of 0.0024286 Pa·s compared to 0.00089689 Pa·s for pure water and 0.0010914 Pa·s for pure ethanol.
- The viscosity maximum in ethanol–water mixtures is attributed to strong hydrogen-bonding interactions between ethanol and water molecules, creating more structured, less mobile molecular clusters at intermediate compositions.
- A second dataset (DOI 10.1021/je800150h) provides 108 data points covering a wider temperature range of 268.1–323.15 K at x(water) = 0.1–0.9 and 101.0 kPa, with viscosities spanning 0.00076–0.007549 Pa·s; the highest viscosity (0.007549 Pa·s) occurs at x(water) = 0.8 and T = 268.1 K, illustrating strong temperature dependence of the viscosity maximum.

**Core blocks found:**

**WM_L1#1_Blocks_(Analysis_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#2 | 「GLOBlit_5201」 | 「PROPblock_21」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of ethanol + water binary mixture, liquid phase. 100 data points, T = 293.15–308.15 K (including 298.15 K), x(ethanol) = 0–1 (full range), P = 92.3 kPa.」 |
| WM_L1#1_Table#3 | 「GLOBlit_11136」 | 「PROPblock_8」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of ethanol + water binary mixture, liquid phase. 108 data points, T = 268.1–323.15 K, x(water) = 0.1–0.9, P = 101.0 kPa.」 |

*Not stored here: 2 verbatim data_inspections table(s); 5 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(3) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNINSPECTED_VALUE** PROPblock_21: 2.7 exists in PROPblock_21's database table but was never shown in an inspection of this run
- **UNGROUNDED_LITERAL** PROPblock_8: 55.05 (near '…composition relationship across a range of 323.15 - 268.1 = …') matches no inspected row/stat, database table, or other source of PROPblock_8
- **UNGROUNDED_LITERAL** PROPblock_8: 14 (near '…of All Found Blocks  The initial search returned a total of …') matches no inspected row/stat, database table, or other source of PROPblock_8


### Inspected Blocks
- GLOBlit_5201 | 10.1016/j.jct.2018.02.022 | PROPblock_21: 100 rows; x=['mole_fraction_<ethanol>']; y=['viscosity_pa_s']
    - BLKprop_1 / GLOBprop_4: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_4: kind=direct; materialize_reference=False; supported=True; units=Pa*s -> Pa*s

### Completed Fits
  - 10.1016/j.jct.2018.02.022/PROPblock_21 (ethanol, water): RK order=5, R²=0.998334, RMSE=0.00948397542567419, coeffs=[2.479754, -2.120004, 2.386992, -3.144373, 0.855239, 1.730003]
      response: direct via X = reported X | 0 reference source(s) | Pa*s -> Pa*s
      pure refs: ethanol=0.00099196, water=0.0008385 [block-edges (water: direct/good, ethanol: direct/good)]
      fit_csv: $ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_21_T303.1_fit.csv
      excess_csv: $ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_21_T303.1_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_21_T303.1_fit.png
      excess_plot: $ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_21_T303.1_excess.png
  - T=293.15K [10.1016/j.jct.2018.02.022/PROPblock_21] (ethanol, water): RK order=5, R²=0.99687, RMSE=0.014946647676868378, coeffs=[2.777909, -2.368838, 2.916612, -4.224496, 0.924678, 2.755948]
      response: direct via X = reported X | 0 reference source(s) | Pa*s -> Pa*s
      pure refs: ethanol=0.0012019, water=0.0010673 [block-edges (water: direct/good, ethanol: direct/good)]
      fit_csv: $ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_21_T293.1_fit.csv
      excess_csv: $ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_21_T293.1_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_21_T293.1_fit.png
      excess_plot: $ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_21_T293.1_excess.png
  - T=298.15K [10.1016/j.jct.2018.02.022/PROPblock_21] (ethanol, water): RK order=4, R²=0.999334, RMSE=0.006612838327445672, coeffs=[2.727996, -2.492594, 2.550047, -2.44775, 1.536444]
      response: direct via X = reported X | 0 reference source(s) | Pa*s -> Pa*s
      pure refs: ethanol=0.0010914, water=0.00089689 [block-edges (water: direct/good, ethanol: direct/good)]
      fit_csv: $ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_21_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_21_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_21_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_21_T298.1_excess.png
  - T=303.15K [10.1016/j.jct.2018.02.022/PROPblock_21] (ethanol, water): RK order=5, R²=0.998334, RMSE=0.00948397542567419, coeffs=[2.479754, -2.120004, 2.386992, -3.144373, 0.855239, 1.730003]
      response: direct via X = reported X | 0 reference source(s) | Pa*s -> Pa*s
      pure refs: ethanol=0.00099196, water=0.0008385 [block-edges (water: direct/good, ethanol: direct/good)]
      fit_csv: $ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_21_T303.1_fit.csv
      excess_csv: $ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_21_T303.1_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_21_T303.1_fit.png
      excess_plot: $ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_21_T303.1_excess.png
  - T=308.15K [10.1016/j.jct.2018.02.022/PROPblock_21] (ethanol, water): RK order=5, R²=0.997541, RMSE=0.010669590029158437, coeffs=[2.33015, -1.956282, 2.031489, -2.8161, 0.891963, 1.575202]
      response: direct via X = reported X | 0 reference source(s) | Pa*s -> Pa*s
      pure refs: ethanol=0.00090388, water=0.00075887 [block-edges (water: direct/good, ethanol: direct/good)]
      fit_csv: $ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_21_T308.1_fit.csv
      excess_csv: $ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_21_T308.1_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_21_T308.1_fit.png
      excess_plot: $ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_21_T308.1_excess.png

## Session Output Files

### data
- `$ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_21_T303.1_fit.csv` — RK fit data — 10.1016/j.jct.2018.02.022 PROPblock_21_T303.1
- `$ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_21_T303.1_excess.csv` — Excess property — 10.1016/j.jct.2018.02.022 PROPblock_21_T303.1
- `$ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_21_T308.1_fit.csv` — RK fit data — 10.1016/j.jct.2018.02.022 PROPblock_21_T308.1
- `$ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_21_T298.1_fit.csv` — RK fit data — 10.1016/j.jct.2018.02.022 PROPblock_21_T298.1
- `$ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_21_T293.1_fit.csv` — RK fit data — 10.1016/j.jct.2018.02.022 PROPblock_21_T293.1
- `$ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_21_T308.1_excess.csv` — Excess property — 10.1016/j.jct.2018.02.022 PROPblock_21_T308.1
- `$ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_21_T298.1_excess.csv` — Excess property — 10.1016/j.jct.2018.02.022 PROPblock_21_T298.1
- `$ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_21_T293.1_excess.csv` — Excess property — 10.1016/j.jct.2018.02.022 PROPblock_21_T293.1

### plot
- `$ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_21_T303.1_fit.png` — RK fit plot — 10.1016/j.jct.2018.02.022 PROPblock_21_T303.1
- `$ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_21_T303.1_excess.png` — Excess plot — 10.1016/j.jct.2018.02.022 PROPblock_21_T303.1
- `$ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_21_T298.1_fit.png` — RK fit plot — 10.1016/j.jct.2018.02.022 PROPblock_21_T298.1
- `$ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_21_T293.1_fit.png` — RK fit plot — 10.1016/j.jct.2018.02.022 PROPblock_21_T293.1
- `$ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_21_T308.1_fit.png` — RK fit plot — 10.1016/j.jct.2018.02.022 PROPblock_21_T308.1
- `$ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_21_T298.1_excess.png` — Excess plot — 10.1016/j.jct.2018.02.022 PROPblock_21_T298.1
- `$ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_21_T293.1_excess.png` — Excess plot — 10.1016/j.jct.2018.02.022 PROPblock_21_T293.1
- `$ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_21_T308.1_excess.png` — Excess plot — 10.1016/j.jct.2018.02.022 PROPblock_21_T308.1

