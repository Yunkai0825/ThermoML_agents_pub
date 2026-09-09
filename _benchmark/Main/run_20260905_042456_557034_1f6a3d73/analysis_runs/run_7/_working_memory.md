# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_042456_557034_1f6a3d73\analysis_runs\run_7`

### ID Catalog
| type | global_id | name | pure_values |
|------|--------|------|-------------|
| comp | GLOBcomp_15 | acetonitrile | 5.2854719e-05 |
| comp | GLOBcomp_18 | dimethylformamide | 7.7436558e-05 |
| prop | GLOBprop_28 | excess molar volume, m3/mol |  |
| prop | GLOBprop_1 | mass density, kg/m3 |  |
| prop | GLOBprop_8 | speed of sound, m/s |  |
| prop | GLOBprop_4 | viscosity, pas |  |

### History
- [query_thermoml_parallel]
- [fit_block_derived] ERROR: Constraint column 'Temperature, K' not found
- [fit_block_derived]
- [fit_block_derived]
- [predict_from_rk]
- [list_session_files]

### Query Results
#### VE_direct
**L1_query_1** — status: no_results · validation: PASS

**Summary:** No excess molar volume (VE, GLOBprop_28) data were found in the ThermoML database for the binary system acetonitrile (GLOBcomp_15) + N,N-dimethylformamide (GLOBcomp_18) at 298.15 K. However, mass density (GLOBprop_1) data covering the full composition range at 298.15 K are available from three sources (DOIs 10.1016/j.jct.2006.01.015, 10.1016/j.jct.2014.02.019, 10.1021/acs.jced.8b00176), from which VE could in principle be calculated. Representative density values at 298.15 K include 776.8 kg/m³ (pure acetonitrile) and 944.6 kg/m³ (pure DMF) from GLOBlit_2659 PROPblock_7, and 776.714 kg/m³ (pure acetonitrile) to 943.934 kg/m³ (pure DMF) from GLOBlit_7481 PROPblock_16. Speed of sound and viscosity data for this binary system are also present in the database.

**Answer:**

**Excess molar volume (VE) data for the binary system acetonitrile + N,N-dimethylformamide (DMF) at 298.15 K — ThermoML database search results:**

No excess molar volume (GLOBprop_28) data were found in the ThermoML database for the binary system acetonitrile (GLOBcomp_15) + N,N-dimethylformamide (GLOBcomp_18). The search was conducted with and without temperature constraints, and no blocks exist for this specific property–compound combination.

**Available related data for this binary system:**

The database does contain density, viscosity, and speed of sound data for the acetonitrile + DMF binary, from which excess molar volume could in principle be derived. The relevant blocks are:

**WM_L1#1_Table#1_(Analysis_L1#1_Answer):**

| *row_id* | *DOI* | *Literature ID* | *Block* | *Property* | *Data points* | *T range (K)* | *Composition variable* | *P (kPa)* |
|---|---|---|---|---|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「10.1016/j.jct.2006.01.015」 | 「GLOBlit_2659」 | 「PROPblock_7」 | 「Mass density (GLOBprop_1)」 | 「102」 | 「293.15–318.15」 | 「x(acetonitrile) 0–1」 | 「101.0」 |
| WM_L1#1_Table#1_Row#2 | 「10.1016/j.jct.2014.02.019」 | 「GLOBlit_4124」 | 「PROPblock_5」 | 「Mass density (GLOBprop_1)」 | 「20」 | 「298.15–313.15」 | 「w(DMF) 0–1」 | 「101.0」 |
| WM_L1#1_Table#1_Row#3 | 「10.1021/acs.jced.8b00176」 | 「GLOBlit_7481」 | 「PROPblock_16」 | 「Mass density (GLOBprop_1)」 | 「66」 | 「298.15–323.15」 | 「x(DMF) 0–1」 | 「100.0」 |
| WM_L1#1_Table#1_Row#4 | 「10.1021/acs.jced.8b00176」 | 「GLOBlit_7481」 | 「PROPblock_17」 | 「Speed of sound (GLOBprop_8)」 | 「66」 | 「298.15–323.15」 | 「x(DMF) 0–1」 | 「100.0」 |
| WM_L1#1_Table#1_Row#5 | 「10.1016/j.jct.2014.02.019」 | 「GLOBlit_4124」 | 「PROPblock_6」 | 「Viscosity (GLOBprop_4)」 | 「Not inspected in this run」 | 「Not inspected in this run」 | 「w(DMF)」 | 「Not inspected in this run」 |
| WM_L1#1_Table#1_Row#6 | 「10.1021/acs.jced.8b00176」 | 「GLOBlit_7481」 | 「PROPblock_18」 | 「Viscosity (GLOBprop_4)」 | 「Not inspected in this run」 | 「Not inspected in this run」 | 「x(DMF)」 | 「Not inspected in this run」 |

**Chemistry note:** While excess molar volume is not directly reported in the database for this system, the three density datasets (PROPblock_7, PROPblock_5, PROPblock_16) cover 298.15 K across the full composition range and could be used to calculate VE. For example, at 298.15 K from PROPblock_7 (GLOBlit_2659), the density of pure DMF is 944.6 kg/m³ and pure acetonitrile is 776.8 kg/m³, with intermediate compositions such as x(acetonitrile) = 0.5925 giving 865.2 kg/m³. Similarly, PROPblock_16 (GLOBlit_7481) reports densities at 298.15 K ranging from 776.714 kg/m³ (pure acetonitrile) to 943.934 kg/m³ (pure DMF).

**Compound IDs:** acetonitrile = GLOBcomp_15, DMF = GLOBcomp_18
**Property ID (not found in database):** Excess molar volume = GLOBprop_28

**Core claims:**
- No excess molar volume (VE) data were found in the ThermoML database for the binary system acetonitrile + N,N-dimethylformamide at 298.15 K or any other temperature.
- The ThermoML database does contain mass density data for the acetonitrile + DMF binary system at 298.15 K across the full composition range from three independent sources (DOIs 10.1016/j.jct.2006.01.015, 10.1016/j.jct.2014.02.019, and 10.1021/acs.jced.8b00176), from which excess molar volume could in principle be calculated.
- Representative pure-component densities at 298.15 K from the available data include 776.8 kg/m³ (acetonitrile) and 944.6 kg/m³ (DMF) from one source, and 776.714 kg/m³ (acetonitrile) and 943.934 kg/m³ (DMF) from another.

**Core blocks found:**

**WM_L1#1_Blocks_(Analysis_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#2 | 「GLOBlit_2659」 | 「PROPblock_7」 | 「GLOBcomp_18, GLOBcomp_15」 | 「GLOBprop_1」 | 「Mass density for binary acetonitrile + DMF, 293.15–318.15 K, 101.0 kPa.」 |
| WM_L1#1_Table#3 | 「GLOBlit_4124」 | 「PROPblock_5」 | 「GLOBcomp_18, GLOBcomp_15」 | 「GLOBprop_1」 | 「Mass density for binary acetonitrile + DMF, 298.15–313.15 K, 101.0 kPa.」 |
| WM_L1#1_Table#4 | 「GLOBlit_7481」 | 「PROPblock_16」 | 「GLOBcomp_18, GLOBcomp_15」 | 「GLOBprop_1」 | 「Mass density for binary acetonitrile + DMF, 298.15–323.15 K, 100.0 kPa.」 |
| WM_L1#1_Table#5 | 「GLOBlit_7481」 | 「PROPblock_17」 | 「GLOBcomp_18, GLOBcomp_15」 | 「GLOBprop_8」 | 「Speed of sound for binary acetonitrile + DMF, 298.15–323.15 K, 100.0 kPa.」 |
| WM_L1#1_Table#6 | 「GLOBlit_4124」 | 「PROPblock_6」 | 「GLOBcomp_18, GLOBcomp_15」 | 「GLOBprop_4」 | 「Viscosity for binary acetonitrile + DMF.」 |
| WM_L1#1_Table#7 | 「GLOBlit_7481」 | 「PROPblock_18」 | 「GLOBcomp_18, GLOBcomp_15」 | 「GLOBprop_4」 | 「Viscosity for binary acetonitrile + DMF.」 |

*Not stored here: 4 verbatim data_inspections table(s); 6 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### density_mix
**L1_query_2** — status: success · validation: FLAGGED(2)

**Summary:** Three ThermoML datasets report mass density (kg/m³) for the binary system acetonitrile + N,N-dimethylformamide (DMF) at 298.15 K. Block GLOBlit_2659/PROPblock_7 (DOI 10.1016/j.jct.2006.01.015) provides 17 points at 101.0 kPa as a function of acetonitrile mole fraction, ranging from 944.6 kg/m³ (pure DMF) to 776.8 kg/m³ (pure acetonitrile). Block GLOBlit_4124/PROPblock_5 (DOI 10.1016/j.jct.2014.02.019) provides 5 points at 101.0 kPa as a function of DMF mass fraction, from 776.47 kg/m³ (pure acetonitrile) to 944.65 kg/m³ (pure DMF). Block GLOBlit_7481/PROPblock_16 (DOI 10.1021/acs.jced.8b00176) provides 11 points at 100.0 kPa as a function of DMF mole fraction, from 776.714 kg/m³ (pure acetonitrile) to 943.934 kg/m³ (pure DMF). Density increases monotonically from pure acetonitrile to pure DMF across all three studies. Pure-component endpoint densities show excellent mutual agreement among the three independent sources.

**Answer:**

#### Density Data for Binary Acetonitrile + N,N-Dimethylformamide (DMF) at 298.15 K

Three ThermoML data blocks contain mass density (GLOBprop_1, kg/m³) measurements for the binary system of acetonitrile (GLOBcomp_15) + N,N-dimethylformamide (GLOBcomp_18) at 298.15 K:

##### Block 1: GLOBlit_2659 / PROPblock_7
- **DOI:** 10.1016/j.jct.2006.01.015
- **Total data points:** 102 (full block T range: 293.15–318.15 K); 17 points at 298.15 K
- **Composition variable:** Mole fraction of acetonitrile
- **Pressure:** 101.0 kPa

Data at 298.15 K (inspection returned a shape-preserving subset of the 17 matched rows):

**WM_L1#2_Table#1_(Analysis_L1#2_Answer):**

| *row_id* | *x(acetonitrile)* | *ρ (kg/m³)* |
|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「0」 | 「944.6」 |
| WM_L1#2_Table#1_Row#2 | 「0.0654」 | 「937.5」 |
| WM_L1#2_Table#1_Row#3 | 「0.1912」 | 「922.9」 |
| WM_L1#2_Table#1_Row#4 | 「0.2586」 | 「914.5」 |
| WM_L1#2_Table#1_Row#5 | 「0.3204」 | 「906.3」 |
| WM_L1#2_Table#1_Row#6 | 「0.3851」 | 「897.4」 |
| WM_L1#2_Table#1_Row#7 | 「0.4596」 | 「886.5」 |
| WM_L1#2_Table#1_Row#8 | 「0.5125」 | 「878.4」 |
| WM_L1#2_Table#1_Row#9 | 「0.5925」 | 「865.2」 |
| WM_L1#2_Table#1_Row#10 | 「0.6402」 | 「856.9」 |
| WM_L1#2_Table#1_Row#11 | 「0.6899」 | 「847.8」 |
| WM_L1#2_Table#1_Row#12 | 「0.7736」 | 「831.1」 |
| WM_L1#2_Table#1_Row#13 | 「0.8522」 | 「813.9」 |
| WM_L1#2_Table#1_Row#14 | 「0.9359」 | 「793.8」 |
| WM_L1#2_Table#1_Row#15 | 「1」 | 「776.8」 |

##### Block 2: GLOBlit_4124 / PROPblock_5
- **DOI:** 10.1016/j.jct.2014.02.019
- **Total data points:** 20 (full block T range: 298.15–313.15 K); 5 points at 298.15 K
- **Composition variable:** Mass fraction of DMF
- **Pressure:** 101.0 kPa

Data at 298.15 K:

**WM_L1#2_Table#2_(Analysis_L1#2_Answer):**

| *row_id* | *w(DMF)* | *ρ (kg/m³)* |
|---|---|---|
| WM_L1#2_Table#2_Row#1 | 「0」 | 「776.47」 |
| WM_L1#2_Table#2_Row#2 | 「0.25」 | 「816.75」 |
| WM_L1#2_Table#2_Row#3 | 「0.5」 | 「856.92」 |
| WM_L1#2_Table#2_Row#4 | 「0.75」 | 「900.14」 |
| WM_L1#2_Table#2_Row#5 | 「1」 | 「944.65」 |

##### Block 3: GLOBlit_7481 / PROPblock_16
- **DOI:** 10.1021/acs.jced.8b00176
- **Total data points:** 66 (full block T range: 298.15–323.15 K); 11 points at 298.15 K
- **Composition variable:** Mole fraction of DMF
- **Pressure:** 100.0 kPa

Data at 298.15 K:

**WM_L1#2_Table#3_(Analysis_L1#2_Answer):**

| *row_id* | *x(DMF)* | *ρ (kg/m³)* |
|---|---|---|
| WM_L1#2_Table#3_Row#1 | 「0」 | 「776.714」 |
| WM_L1#2_Table#3_Row#2 | 「0.0989」 | 「802.565」 |
| WM_L1#2_Table#3_Row#3 | 「0.1916」 | 「826.376」 |
| WM_L1#2_Table#3_Row#4 | 「0.2925」 | 「844.614」 |
| WM_L1#2_Table#3_Row#5 | 「0.3932」 | 「865.725」 |
| WM_L1#2_Table#3_Row#6 | 「0.5029」 | 「880.889」 |
| WM_L1#2_Table#3_Row#7 | 「0.6002」 | 「895.421」 |
| WM_L1#2_Table#3_Row#8 | 「0.6931」 | 「907.546」 |
| WM_L1#2_Table#3_Row#9 | 「0.7926」 | 「922.026」 |
| WM_L1#2_Table#3_Row#10 | 「0.8996」 | 「932.676」 |
| WM_L1#2_Table#3_Row#11 | 「1」 | 「943.934」 |

**Chemistry insight:** The density increases monotonically from pure acetonitrile to pure DMF at 298.15 K across all three independent studies. The pure-component endpoint values show excellent agreement: pure acetonitrile densities are 776.8 (PROPblock_7), 776.47 (PROPblock_5), and 776.714 kg/m³ (PROPblock_16), while pure DMF densities are 944.6 (PROPblock_7), 944.65 (PROPblock_5), and 943.934 kg/m³ (PROPblock_16), confirming high measurement consistency across the three sources.

**Core claims:**
- Three independent ThermoML data blocks report mass density for the binary system acetonitrile + N,N-dimethylformamide at 298.15 K, and all three show a monotonic increase in density from pure acetonitrile to pure DMF.
- Pure acetonitrile densities at 298.15 K are 776.8 kg/m³ (DOI 10.1016/j.jct.2006.01.015), 776.47 kg/m³ (DOI 10.1016/j.jct.2014.02.019), and 776.714 kg/m³ (DOI 10.1021/acs.jced.8b00176), showing close agreement across the three sources.
- Pure DMF densities at 298.15 K are 944.6 kg/m³ (DOI 10.1016/j.jct.2006.01.015), 944.65 kg/m³ (DOI 10.1016/j.jct.2014.02.019), and 943.934 kg/m³ (DOI 10.1021/acs.jced.8b00176), also showing close agreement.
- The three blocks report data at slightly different pressures (101.0 kPa for two blocks, 100.0 kPa for one) and use different composition variables (mole fraction of acetonitrile, mass fraction of DMF, or mole fraction of DMF).
- Some quoted pure-component values carry unresolved data-provenance flags (AMBIGUOUS_VALUE, MISATTRIBUTED_VALUE), so the cross-block attribution of specific endpoint numbers should be treated with caution.

**Core blocks found:**

**WM_L1#2_Blocks_(Analysis_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#4 | 「GLOBlit_2659」 | 「PROPblock_7」 | 「GLOBcomp_18, GLOBcomp_15」 | 「GLOBprop_1」 | 「Mass density data for binary acetonitrile + N,N-dimethylformamide at 293.15–318.15 K; 17 points at 298.15 K.」 |
| WM_L1#2_Table#5 | 「GLOBlit_4124」 | 「PROPblock_5」 | 「GLOBcomp_18, GLOBcomp_15」 | 「GLOBprop_1」 | 「Mass density data for binary acetonitrile + N,N-dimethylformamide at 298.15–313.15 K; 5 points at 298.15 K.」 |
| WM_L1#2_Table#6 | 「GLOBlit_7481」 | 「PROPblock_16」 | 「GLOBcomp_18, GLOBcomp_15」 | 「GLOBprop_1」 | 「Mass density data for binary acetonitrile + N,N-dimethylformamide at 298.15–323.15 K; 11 points at 298.15 K.」 |

*Not stored here: 3 verbatim data_inspections table(s); 3 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(2) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **AMBIGUOUS_VALUE** PROPblock_16: 944.6 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean
- **MISATTRIBUTED_VALUE** PROPblock_5: 943.934 does not belong to PROPblock_5; it matches only GLOBlit_7481::PROPblock_16 (inspected this run)


### Completed Fits
  - 10.1016/j.jct.2006.01.015/PROPblock_7 (acetonitrile, dimethylformamide): RK order=5, R²=0.999362, RMSE=2.1877523782449646e-09, coeffs=[-1e-06, -1e-06, -0.0, 0.0, 0.0, -0.0]
      response: direct via X = reported X | 0 reference source(s) | kg/m3 -> kg/m3
      route: measured-derived (density_to_molar_volume, exact pointwise) via density_to_molar_volume
      pure refs: acetonitrile=5.28489e-05, dimethylformamide=7.7382e-05 [block-edges of derived data (dimethylformamide: direct/good, acetonitrile: direct/good)]
      fit_csv: $ROOT/data\10_1016_j_jct_2006_01_015_BPROPblock_7_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1016_j_jct_2006_01_015_BPROPblock_7_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_jct_2006_01_015_BPROPblock_7_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1016_j_jct_2006_01_015_BPROPblock_7_T298.1_excess.png
  - 10.1021/acs.jced.8b00176/PROPblock_16 (dimethylformamide, acetonitrile): RK order=1, R²=0.688065, RMSE=7.876929228732568e-08, coeffs=[-2e-06, 1e-06]
      response: direct via X = reported X | 0 reference source(s) | kg/m3 -> kg/m3
      route: measured-derived (density_to_molar_volume, exact pointwise) via density_to_molar_volume
      pure refs: dimethylformamide=7.74366e-05, acetonitrile=5.28547e-05 [block-edges of derived data (acetonitrile: direct/good, dimethylformamide: direct/good)]
      fit_csv: $ROOT/data\10_1021_acs_jced_8b00176_BPROPblock_16_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1021_acs_jced_8b00176_BPROPblock_16_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1021_acs_jced_8b00176_BPROPblock_16_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1021_acs_jced_8b00176_BPROPblock_16_T298.1_excess.png

## Session Output Files

### data
- `$ROOT/data\10_1016_j_jct_2006_01_015_BPROPblock_7_T298.1_fit.csv` — RK fit data — 10.1016/j.jct.2006.01.015 PROPblock_7_T298.1
- `$ROOT/data\10_1016_j_jct_2006_01_015_BPROPblock_7_T298.1_excess.csv` — Excess property — 10.1016/j.jct.2006.01.015 PROPblock_7_T298.1
- `$ROOT/data\10_1021_acs_jced_8b00176_BPROPblock_16_T298.1_fit.csv` — RK fit data — 10.1021/acs.jced.8b00176 PROPblock_16_T298.1
- `$ROOT/data\10_1021_acs_jced_8b00176_BPROPblock_16_T298.1_excess.csv` — Excess property — 10.1021/acs.jced.8b00176 PROPblock_16_T298.1

### plot
- `$ROOT/plots\10_1016_j_jct_2006_01_015_BPROPblock_7_T298.1_fit.png` — RK fit plot — 10.1016/j.jct.2006.01.015 PROPblock_7_T298.1
- `$ROOT/plots\10_1016_j_jct_2006_01_015_BPROPblock_7_T298.1_excess.png` — Excess plot — 10.1016/j.jct.2006.01.015 PROPblock_7_T298.1
- `$ROOT/plots\10_1021_acs_jced_8b00176_BPROPblock_16_T298.1_fit.png` — RK fit plot — 10.1021/acs.jced.8b00176 PROPblock_16_T298.1
- `$ROOT/plots\10_1021_acs_jced_8b00176_BPROPblock_16_T298.1_excess.png` — Excess plot — 10.1021/acs.jced.8b00176 PROPblock_16_T298.1

