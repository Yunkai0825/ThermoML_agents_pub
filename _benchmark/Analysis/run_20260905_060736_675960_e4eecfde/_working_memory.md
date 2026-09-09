# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_060736_675960_e4eecfde`

### ID Catalog
| type | global_id | name | pure_values |
|------|--------|------|-------------|
| comp | GLOBcomp_18 | dimethylformamide |  |
| comp | GLOBcomp_15 | acetonitrile |  |
| comp | GLOBcomp_1 | water |  |
| prop | GLOBprop_4 | viscosity, pas |  |
| meas | GLOBmeas_140 | captub:ufactor:2 |  |
| lit | GLOBlit_7481 | 10.1021/acs.jced.8b00176 |  |
| lit | GLOBlit_4124 | 10.1016/j.jct.2014.02.019 |  |
| lit | GLOBlit_2602 | 10.1016/j.jct.2005.08.009 |  |

### History
- [query_thermoml_parallel]
- [fit_multi_system]
- [fit_multi_system]
- [predict_from_rk]
- [predict_from_rk]
- [predict_from_rk]

### Query Results
#### ternary_viscosity
**L1_query_1** — status: no_results · validation: PASS

**Summary:** No viscosity data exists in the ThermoML database for the ternary system N,N-dimethylformamide (DMF) + water + acetonitrile at 298.15 K or any other temperature. The ternary combination itself is not present in the ThermoML collection for any measured property.

**Answer:**

No viscosity data was found in the ThermoML database for the ternary system N,N-dimethylformamide (DMF) + water + acetonitrile at 298.15 K or any other temperature.

Further investigation confirmed that this ternary combination (GLOBcomp_18 DMF, GLOBcomp_1 water, GLOBcomp_15 acetonitrile) does not appear in the database for any measured property — the ternary system itself is not present in the ThermoML collection.

**Core claims:**
- No viscosity data was found in the ThermoML database for the ternary system N,N-dimethylformamide (DMF) + water + acetonitrile at 298.15 K or any other temperature.
- The ternary system DMF + water + acetonitrile is not present in the ThermoML collection for any measured property.

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### binary_DMF_water
**L1_query_2** — status: success · validation: PASS

**Summary:** Composition-dependent dynamic viscosity data for the binary system N,N-dimethylformamide (DMF) + water at 298.15 K and 101.325 kPa were retrieved from the ThermoML database (DOI 10.1021/je050209y, GLOBlit_8676, PROPblock_9). Eleven data points span x(DMF) = 0.05–0.9488, measured by capillary tube / U-factor method. Viscosity values (Pa·s): 0.00131 at x=0.05, 0.001728 at x=0.1001, 0.002346 at x=0.2, 0.002491 at x=0.299, 0.002273 at x=0.3998, 0.001878 at x=0.4997, 0.001532 at x=0.5993, 0.001243 at x=0.6995, 0.001045 at x=0.8, 0.000901 at x=0.8991, 0.000843 at x=0.9488. The viscosity shows a non-monotonic dependence on composition with a single maximum near x(DMF) ≈ 0.3 (η = 0.002491 Pa·s), attributed to strong hydrogen-bonding interactions between DMF and water that create enhanced local structuring at intermediate compositions. Beyond x(DMF) ≈ 0.3, viscosity decreases steadily. Two additional datasets (DOI 10.1021/je300608v, GLOBlit_9900; GLOBlit_11207) were also identified but not inspected.

**Answer:**

#### Viscosity of Binary DMF + Water at 298.15 K

Composition-dependent dynamic viscosity data for the binary system **N,N-dimethylformamide (DMF) + water** at **298.15 K** and **101.325 kPa** were found in the ThermoML database.

##### Best Dataset: DOI 10.1021/je050209y (GLOBlit_8676, PROPblock_9)

This block provides 11 data points spanning the mole fraction range x(DMF) = 0.05–0.9488, measured by capillary tube / U-factor method:

**WM_L1#2_Table#1_(Analysis_L1#2_Answer):**

| *row_id* | *x(DMF)* | *Viscosity (Pa·s)* |
|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「0.05」 | 「0.00131」 |
| WM_L1#2_Table#1_Row#2 | 「0.1001」 | 「0.001728」 |
| WM_L1#2_Table#1_Row#3 | 「0.2」 | 「0.002346」 |
| WM_L1#2_Table#1_Row#4 | 「0.299」 | 「0.002491」 |
| WM_L1#2_Table#1_Row#5 | 「0.3998」 | 「0.002273」 |
| WM_L1#2_Table#1_Row#6 | 「0.4997」 | 「0.001878」 |
| WM_L1#2_Table#1_Row#7 | 「0.5993」 | 「0.001532」 |
| WM_L1#2_Table#1_Row#8 | 「0.6995」 | 「0.001243」 |
| WM_L1#2_Table#1_Row#9 | 「0.8」 | 「0.001045」 |
| WM_L1#2_Table#1_Row#10 | 「0.8991」 | 「0.000901」 |
| WM_L1#2_Table#1_Row#11 | 「0.9488」 | 「0.000843」 |

**Conditions:** T = 298.15 K, P = 101.325 kPa (block constraints).

##### Chemical Insight

The viscosity exhibits a **non-monotonic** dependence on composition with a single maximum near **x(DMF) ≈ 0.3** (η = 0.002491 Pa·s). This is characteristic of strong intermolecular interactions (hydrogen bonding) between DMF and water, which create more structured solution networks at intermediate compositions compared to either pure component. The viscosity maximum in the water-rich region reflects the disruption of the water hydrogen-bond network by DMF molecules, leading to enhanced local structuring. Beyond x(DMF) ≈ 0.3, the viscosity decreases steadily as DMF becomes the dominant component.

##### Additional Sources

Two other datasets were also identified in the search as containing viscosity data for this binary system (not inspected in this run):
- **DOI 10.1021/je300608v** (GLOBlit_9900, PROPblock_3)
- **GLOBlit_11207**

The GLOBlit_8676 dataset offers the most complete composition coverage at this temperature.

**Core claims:**
- Composition-dependent dynamic viscosity data for the binary system N,N-dimethylformamide (DMF) + water at 298.15 K and 101.325 kPa were found in the ThermoML database (DOI 10.1021/je050209y), spanning 11 data points from x(DMF) = 0.05 to 0.9488.
- The viscosity exhibits a non-monotonic dependence on composition with a single maximum near x(DMF) ≈ 0.3 (η = 0.002491 Pa·s), attributed to strong intermolecular hydrogen-bonding interactions between DMF and water at intermediate compositions.
- Beyond x(DMF) ≈ 0.3, the viscosity decreases steadily as DMF becomes the dominant component, reaching 0.000843 Pa·s at x(DMF) = 0.9488.

**Core blocks found:**

**WM_L1#2_Blocks_(Analysis_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#2 | 「GLOBlit_8676」 | 「PROPblock_9」 | 「GLOBcomp_18, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity measurements for N,N-dimethylformamide + water binary mixture at 298.15 K across mole fraction range 0.05–0.9488.」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### binary_DMF_acetonitrile
**L1_query_3** — status: success · validation: FLAGGED(2)

**Summary:** Dynamic viscosity data for the binary system N,N-dimethylformamide (DMF) + acetonitrile at 298.15 K are reported from two ThermoML sources. The primary dataset (DOI 10.1021/acs.jced.8b00176, PROPblock_18) provides 11 mole-fraction compositions at 298.15 K and 100.0 kPa measured by falling/rolling sphere viscometer, spanning from pure acetonitrile (η = 0.00034 Pa·s at x(DMF) = 0) to pure DMF (η = 0.00081 Pa·s at x(DMF) = 1), with a smooth, monotonic, slightly concave increase. A secondary dataset (DOI 10.1016/j.jct.2014.02.019, PROPblock_6) gives five mass-fraction compositions at 298.15 K and 101.0 kPa measured by capillary viscometer, with pure-component values of 0.000342 Pa·s (acetonitrile) and 0.0007986 Pa·s (DMF). The two sources are mutually consistent. The mole-fraction dataset with 11 compositions is recommended for composition-dependent modelling.

**Answer:**

#### Viscosity Data for Binary DMF + Acetonitrile at 298.15 K

Two ThermoML data blocks contain dynamic viscosity measurements for the binary system N,N-dimethylformamide (DMF, GLOBcomp_18) + acetonitrile (GLOBcomp_15) at 298.15 K.

##### Primary dataset — full mole fraction range

**Source:** DOI 10.1021/acs.jced.8b00176 (GLOBlit_7481, PROPblock_18)
Method: falling/rolling sphere viscometer; pressure constraint: 100.0 kPa.
The block contains 66 total data points (298.15–323.15 K); 11 points at 298.15 K span the complete mole fraction range of DMF:

**WM_L1#3_Table#1_(Analysis_L1#3_Answer):**

| *row_id* | *x(DMF)* | *η (Pa·s)* |
|---|---|---|
| WM_L1#3_Table#1_Row#1 | 「0」 | 「0.00034」 |
| WM_L1#3_Table#1_Row#2 | 「0.0989」 | 「0.0004」 |
| WM_L1#3_Table#1_Row#3 | 「0.1916」 | 「0.00044」 |
| WM_L1#3_Table#1_Row#4 | 「0.2925」 | 「0.00048」 |
| WM_L1#3_Table#1_Row#5 | 「0.3932」 | 「0.00054」 |
| WM_L1#3_Table#1_Row#6 | 「0.5029」 | 「0.00061」 |
| WM_L1#3_Table#1_Row#7 | 「0.6002」 | 「0.00065」 |
| WM_L1#3_Table#1_Row#8 | 「0.6931」 | 「0.00069」 |
| WM_L1#3_Table#1_Row#9 | 「0.7926」 | 「0.00075」 |
| WM_L1#3_Table#1_Row#10 | 「0.8996」 | 「0.00079」 |
| WM_L1#3_Table#1_Row#11 | 「1」 | 「0.00081」 |

The viscosity increases monotonically from pure acetonitrile (0.00034 Pa·s) to pure DMF (0.00081 Pa·s) — a ratio of approximately 2.4 (computed from the inspected endpoint values: 0.00081 / 0.00034 ≈ 2.38). The increase is smooth and slightly concave, consistent with the stronger intermolecular interactions (hydrogen-bond accepting and dipole–dipole) in DMF compared with acetonitrile.

##### Secondary dataset — mass fraction basis

**Source:** DOI 10.1016/j.jct.2014.02.019 (GLOBlit_4124, PROPblock_6)
Method: capillary (Ostwald/Ubbelohde) viscometer; pressure: 101.0 kPa; 20 total data points (298.15–313.15 K).
Five compositions at 298.15 K (mass fraction of DMF):

**WM_L1#3_Table#2_(Analysis_L1#3_Answer):**

| *row_id* | *w(DMF)* | *η (Pa·s)* |
|---|---|---|
| WM_L1#3_Table#2_Row#1 | 「0」 | 「0.000342」 |
| WM_L1#3_Table#2_Row#2 | 「0.25」 | 「0.0003959」 |
| WM_L1#3_Table#2_Row#3 | 「0.5」 | 「0.0005214」 |
| WM_L1#3_Table#2_Row#4 | 「0.75」 | 「0.0006465」 |
| WM_L1#3_Table#2_Row#5 | 「1」 | 「0.0007986」 |

The two datasets are mutually consistent: pure acetonitrile ≈ 0.00034 Pa·s and pure DMF ≈ 0.0008 Pa·s in both sources.

The mole-fraction dataset (PROPblock_18) is recommended for composition-dependent modelling as it covers 11 evenly spaced compositions across the full range.

**Core claims:**
- At 298.15 K and approximately 100 kPa, the dynamic viscosity of the binary DMF + acetonitrile system increases monotonically from pure acetonitrile (0.00034 Pa·s) to pure DMF (0.00081 Pa·s) across 11 mole-fraction compositions spanning the full range (DOI 10.1021/acs.jced.8b00176).
- A second dataset (DOI 10.1016/j.jct.2014.02.019) reports viscosity on a mass-fraction basis at 298.15 K for five compositions, with pure-component values (acetonitrile 0.000342 Pa·s, DMF 0.0007986 Pa·s) mutually consistent with the first dataset.
- The mole-fraction dataset (11 compositions) is recommended for composition-dependent modelling over the mass-fraction dataset (5 compositions) due to its finer and more evenly spaced coverage.

**Core blocks found:**

**WM_L1#3_Blocks_(Analysis_L1#3_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#3_Table#3 | 「GLOBlit_7481」 | 「PROPblock_18」 | 「GLOBcomp_18, GLOBcomp_15」 | 「GLOBprop_4」 | 「Dynamic viscosity of binary N,N-dimethylformamide + acetonitrile at 298.15 K across 11 mole fractions (0–1), measured by falling/rolling sphere viscometer at 100.0 kPa.」 |
| WM_L1#3_Table#4 | 「GLOBlit_4124」 | 「PROPblock_6」 | 「GLOBcomp_18, GLOBcomp_15」 | 「GLOBprop_4」 | 「Dynamic viscosity of binary N,N-dimethylformamide + acetonitrile at 298.15 K at 5 mass fractions, measured by capillary viscometer at 101.0 kPa.」 |

*Not stored here: 2 verbatim data_inspections table(s); 5 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(2) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNGROUNDED_LITERAL** PROPblock_18: 2.4 (near '…Pa·s) to pure DMF (0.00081 Pa·s) — a ratio of approximately …') matches no inspected row/stat, database table, or other source of PROPblock_18
- **UNGROUNDED_LITERAL** PROPblock_18: 2.38 (near '…ted from the inspected endpoint values: 0.00081 / 0.00034 ≈ …') matches no inspected row/stat, database table, or other source of PROPblock_18


#### binary_water_acetonitrile
**L1_query_4** — status: success · validation: PASS

**Summary:** Dynamic viscosity data for the binary system water + acetonitrile at 298.15 K and 101.0 kPa were found in a single ThermoML data block (DOI 10.1016/j.jct.2005.08.009, GLOBlit_2602, PROPblock_3), measured by capillary tube with U-factor (GLOBmeas_140). The block contains 16 composition points spanning the full mole fraction range of acetonitrile (0 to 1). Viscosity exhibits a maximum near x(acetonitrile) ≈ 0.05 (0.0009849 Pa·s), exceeding that of pure water (0.0008901 Pa·s), attributed to strong water–acetonitrile hydrogen-bonding interactions. Beyond this maximum, viscosity decreases monotonically to pure acetonitrile (0.0003417 Pa·s). The overall viscosity range is 0.0003417–0.0009849 Pa·s.

**Answer:**

#### Viscosity Data for Binary Water + Acetonitrile at 298.15 K

A single data block was found in the ThermoML database:

**Source:** DOI 10.1016/j.jct.2005.08.009 (GLOBlit_2602, PROPblock_3)  
**Property:** Dynamic viscosity (Pa·s), liquid phase  
**Method:** Capillary tube with U-factor (GLOBmeas_140)  
**Constraint:** Pressure = 101.0 kPa  
**System:** Binary — water (GLOBcomp_1) + acetonitrile (GLOBcomp_15)

The block contains 16 composition points at 298.15 K spanning the full mole fraction range of acetonitrile (0 to 1). The following shape-preserving subset was returned by inspection:

**WM_L1#4_Table#1_(Analysis_L1#4_Answer):**

| *row_id* | *x(acetonitrile)* | *η (Pa·s)* |
|---|---|---|
| WM_L1#4_Table#1_Row#1 | 「0」 | 「0.0008901」 |
| WM_L1#4_Table#1_Row#2 | 「0.051」 | 「0.0009849」 |
| WM_L1#4_Table#1_Row#3 | 「0.1169」 | 「0.0009567」 |
| WM_L1#4_Table#1_Row#4 | 「0.1971」 | 「0.0008743」 |
| WM_L1#4_Table#1_Row#5 | 「0.4417」 | 「0.0006061」 |
| WM_L1#4_Table#1_Row#6 | 「0.5204」 | 「0.0005387」 |
| WM_L1#4_Table#1_Row#7 | 「0.6012」 | 「0.0004802」 |
| WM_L1#4_Table#1_Row#8 | 「0.6671」 | 「0.0004415」 |
| WM_L1#4_Table#1_Row#9 | 「0.7398」 | 「0.0004064」 |
| WM_L1#4_Table#1_Row#10 | 「0.8253」 | 「0.0003722」 |
| WM_L1#4_Table#1_Row#11 | 「0.886」 | 「0.0003561」 |
| WM_L1#4_Table#1_Row#12 | 「0.9389」 | 「0.0003478」 |
| WM_L1#4_Table#1_Row#13 | 「1.0」 | 「0.0003417」 |

**Chemical insight:** The viscosity shows a notable maximum near x(acetonitrile) ≈ 0.05 (η = 0.0009849 Pa·s), which exceeds the viscosity of pure water (0.0008901 Pa·s). This is characteristic of strong water–acetonitrile intermolecular interactions (hydrogen bonding between water and the nitrile group) at low acetonitrile concentrations, which enhance the local structure and resist flow. Beyond this maximum, viscosity decreases monotonically toward pure acetonitrile (0.0003417 Pa·s), which is considerably less viscous than water. The overall viscosity range at 298.15 K spans 0.0003417–0.0009849 Pa·s across 16 data points.

**Core claims:**
- A single ThermoML data block (DOI 10.1016/j.jct.2005.08.009) reports dynamic viscosity of the binary water + acetonitrile system in the liquid phase at 298.15 K and 101.0 kPa, spanning 16 composition points from x(acetonitrile) = 0 to 1.
- The viscosity exhibits a maximum near x(acetonitrile) ≈ 0.05 (η = 0.0009849 Pa·s), exceeding the pure-water value of 0.0008901 Pa·s, attributed to strong water–acetonitrile hydrogen-bonding interactions that enhance local structure at low acetonitrile concentrations.
- Beyond the maximum, viscosity decreases monotonically with increasing acetonitrile mole fraction, reaching 0.0003417 Pa·s for pure acetonitrile, giving an overall range of 0.0003417–0.0009849 Pa·s across the composition span.

**Core blocks found:**

**WM_L1#4_Blocks_(Analysis_L1#4_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#4_Table#2 | 「GLOBlit_2602」 | 「PROPblock_3」 | 「GLOBcomp_15, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity measurements for binary water + acetonitrile at 298.15 K across the full mole fraction range (16 composition points), measured by capillary tube method at 101.0 kPa.」 |

*Not stored here: 1 verbatim data_inspections table(s); 5 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


### Completed Fits
  - DMF_acetonitrile [10.1021/acs.jced.8b00176/PROPblock_18] (dimethylformamide, acetonitrile): RK order=4, R²=0.917516, RMSE=0.007151559874569717, coeffs=[0.551336, 0.125607, -0.522683, -0.309479, 1.451546]
      response: direct via X = reported X | 0 reference source(s) | Pa*s -> Pa*s
      pure refs: dimethylformamide=0.00081, acetonitrile=0.00034 [block-edges (acetonitrile: direct/good, dimethylformamide: direct/good)]
      fit_csv: $ROOT/data\10_1021_acs_jced_8b00176_BPROPblock_18_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1021_acs_jced_8b00176_BPROPblock_18_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1021_acs_jced_8b00176_BPROPblock_18_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1021_acs_jced_8b00176_BPROPblock_18_T298.1_excess.png
  - DMF_water [10.1021/je050209y/PROPblock_9] (dimethylformamide, water): RK order=5, R²=0.999949, RMSE=0.002465528073338755, coeffs=[3.1881, -3.958298, 1.865104, 0.421852, -0.304041, -0.81553]
      response: direct via X = reported X | 0 reference source(s) | Pa*s -> Pa*s
      pure refs: dimethylformamide=0.00081, water=0.0008901 [named (matched to composition axis)]
      fit_csv: $ROOT/data\10_1021_je050209y_BPROPblock_9_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1021_je050209y_BPROPblock_9_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1021_je050209y_BPROPblock_9_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1021_je050209y_BPROPblock_9_T298.1_excess.png
  - water_acetonitrile [10.1016/j.jct.2005.08.009/PROPblock_3] (acetonitrile, water): RK order=5, R²=0.997253, RMSE=0.005202139660061691, coeffs=[0.044503, -1.167616, 0.255888, 0.25772, 1.197621, -1.769905]
      response: direct via X = reported X | 0 reference source(s) | Pa*s -> Pa*s
      pure refs: acetonitrile=0.00034175, water=0.0008901 [block-edges (water: direct/good, acetonitrile: direct/good)]
      fit_csv: $ROOT/data\10_1016_j_jct_2005_08_009_BPROPblock_3_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1016_j_jct_2005_08_009_BPROPblock_3_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_jct_2005_08_009_BPROPblock_3_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1016_j_jct_2005_08_009_BPROPblock_3_T298.1_excess.png

## Session Output Files

### data
- `$ROOT/data\10_1021_je050209y_BPROPblock_9_T298.1_fit.csv` — RK fit data — 10.1021/je050209y PROPblock_9_T298.1
- `$ROOT/data\10_1021_acs_jced_8b00176_BPROPblock_18_T298.1_fit.csv` — RK fit data — 10.1021/acs.jced.8b00176 PROPblock_18_T298.1
- `$ROOT/data\10_1016_j_jct_2005_08_009_BPROPblock_3_T298.1_fit.csv` — RK fit data — 10.1016/j.jct.2005.08.009 PROPblock_3_T298.1
- `$ROOT/data\10_1021_je050209y_BPROPblock_9_T298.1_excess.csv` — Excess property — 10.1021/je050209y PROPblock_9_T298.1
- `$ROOT/data\10_1016_j_jct_2005_08_009_BPROPblock_3_T298.1_excess.csv` — Excess property — 10.1016/j.jct.2005.08.009 PROPblock_3_T298.1
- `$ROOT/data\10_1021_acs_jced_8b00176_BPROPblock_18_T298.1_excess.csv` — Excess property — 10.1021/acs.jced.8b00176 PROPblock_18_T298.1

### plot
- `$ROOT/plots\10_1021_acs_jced_8b00176_BPROPblock_18_T298.1_fit.png` — RK fit plot — 10.1021/acs.jced.8b00176 PROPblock_18_T298.1
- `$ROOT/plots\10_1021_je050209y_BPROPblock_9_T298.1_fit.png` — RK fit plot — 10.1021/je050209y PROPblock_9_T298.1
- `$ROOT/plots\10_1016_j_jct_2005_08_009_BPROPblock_3_T298.1_fit.png` — RK fit plot — 10.1016/j.jct.2005.08.009 PROPblock_3_T298.1
- `$ROOT/plots\10_1021_je050209y_BPROPblock_9_T298.1_excess.png` — Excess plot — 10.1021/je050209y PROPblock_9_T298.1
- `$ROOT/plots\10_1021_acs_jced_8b00176_BPROPblock_18_T298.1_excess.png` — Excess plot — 10.1021/acs.jced.8b00176 PROPblock_18_T298.1
- `$ROOT/plots\10_1016_j_jct_2005_08_009_BPROPblock_3_T298.1_excess.png` — Excess plot — 10.1016/j.jct.2005.08.009 PROPblock_3_T298.1

