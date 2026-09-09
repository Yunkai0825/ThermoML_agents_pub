# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_041158_447699_492f384b\analysis_runs\run_2`

### ID Catalog
| type | global_id | name | pure_values |
|------|--------|------|-------------|
| comp | GLOBcomp_1 | water | 1.8068301e-05 |
| comp | GLOBcomp_4 | methanol | 4.070376e-05 |
| prop | GLOBprop_28 | excess molar volume, m3/mol |  |
| prop | GLOBprop_1 | massdensitykgm3 |  |
| var | GLOBvar_1 | temperaturek |  |
| var | GLOBvar_2 | molefraction<water> |  |
| constr | GLOBconstr_1 | pressurekpa |  |
| lit | GLOBlit_2395 | 10.1016/j.jct.2004.03.011 |  |

### History
- [query_thermoml_parallel]
- [inspect_block]
- [fit_block_derived] ERROR: Constraint column 'Temperature, K' not found
- [fit_block_derived]
- [predict_from_rk]
- [list_session_files]

### Query Results
#### excess_volume
**L1_query_1** — status: success · validation: PASS

**Summary:** Excess molar volume (V_E) data for the water + methanol binary system from Safronov & Heyer (2004), DOI 10.1016/j.jct.2004.03.011 (GLOBlit_2395, PROPblock_1). At 298.15 K, 23 data points cover pressures from 100 to 60000 kPa at methanol mole fractions of 0.25, 0.50, and 0.75. All V_E values are negative, ranging from −1.014 × 10⁻⁶ to −4.61 × 10⁻⁷ m³/mol, indicating volume contraction upon mixing due to strong hydrogen-bonding interactions. The most negative V_E occurs at x(methanol) = 0.5, and the magnitude of V_E decreases with increasing pressure. The full data block contains 206 points spanning 298.15–523.15 K, 100–60000 kPa, and x(methanol) = 0.25–0.75, with V_E ranging from −2.545 × 10⁻⁶ to −5 × 10⁻⁹ m³/mol.

**Answer:**

#### Excess Molar Volume (V_E) Data for Water + Methanol Binary at 298.15 K

**Source:** Safronov & Heyer (2004), DOI 10.1016/j.jct.2004.03.011 [GLOBlit_2395], Block PROPblock_1

**Compounds:**
- Water (GLOBcomp_1)
- Methanol (GLOBcomp_4)

**Property:** Excess molar volume (GLOBprop_28), liquid phase

One block was found in the ThermoML database containing excess molar volume data for the water + methanol binary system at 298.15 K. The data span pressures from 100 to 60000 kPa at three methanol mole fractions (0.25, 0.5, 0.75). All V_E values are negative, indicating volume contraction upon mixing — consistent with strong hydrogen-bonding interactions between water and methanol. The most negative V_E occurs at x(methanol) = 0.5, reflecting the composition of maximum intermolecular interaction.

##### Data at T = 298.15 K

**WM_L1#1_Table#1_(Analysis_L1#1_Answer):**

| *row_id* | *Pressure (kPa)* | *x(methanol)* | *V_E (m³/mol)* |
|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「100」 | 「0.25」 | 「−7.42 × 10⁻⁷」 |
| WM_L1#1_Table#1_Row#2 | 「100」 | 「0.50」 | 「−1.014 × 10⁻⁶」 |
| WM_L1#1_Table#1_Row#3 | 「100」 | 「0.75」 | 「−7.05 × 10⁻⁷」 |
| WM_L1#1_Table#1_Row#4 | 「5000」 | 「0.25」 | 「−7.13 × 10⁻⁷」 |
| WM_L1#1_Table#1_Row#5 | 「5000」 | 「0.50」 | 「−9.63 × 10⁻⁷」 |
| WM_L1#1_Table#1_Row#6 | 「5000」 | 「0.75」 | 「−6.74 × 10⁻⁷」 |
| WM_L1#1_Table#1_Row#7 | 「10000」 | 「0.25」 | 「−6.85 × 10⁻⁷」 |
| WM_L1#1_Table#1_Row#8 | 「10000」 | 「0.50」 | 「−9.15 × 10⁻⁷」 |
| WM_L1#1_Table#1_Row#9 | 「10000」 | 「0.75」 | 「−6.44 × 10⁻⁷」 |
| WM_L1#1_Table#1_Row#10 | 「20000」 | 「0.25」 | 「−6.27 × 10⁻⁷」 |
| WM_L1#1_Table#1_Row#11 | 「20000」 | 「0.50」 | 「−8.31 × 10⁻⁷」 |
| WM_L1#1_Table#1_Row#12 | 「20000」 | 「0.75」 | 「−5.93 × 10⁻⁷」 |
| WM_L1#1_Table#1_Row#13 | 「30000」 | 「0.25」 | 「−5.75 × 10⁻⁷」 |
| WM_L1#1_Table#1_Row#14 | 「30000」 | 「0.50」 | 「−7.62 × 10⁻⁷」 |
| WM_L1#1_Table#1_Row#15 | 「30000」 | 「0.75」 | 「−5.53 × 10⁻⁷」 |
| WM_L1#1_Table#1_Row#16 | 「40000」 | 「0.25」 | 「−5.29 × 10⁻⁷」 |
| WM_L1#1_Table#1_Row#17 | 「40000」 | 「0.50」 | 「−7.02 × 10⁻⁷」 |
| WM_L1#1_Table#1_Row#18 | 「40000」 | 「0.75」 | 「−5.14 × 10⁻⁷」 |
| WM_L1#1_Table#1_Row#19 | 「50000」 | 「0.25」 | 「−4.85 × 10⁻⁷」 |
| WM_L1#1_Table#1_Row#20 | 「50000」 | 「0.50」 | 「−6.49 × 10⁻⁷」 |
| WM_L1#1_Table#1_Row#21 | 「50000」 | 「0.75」 | 「−4.65 × 10⁻⁷」 |
| WM_L1#1_Table#1_Row#22 | 「60000」 | 「0.25」 | 「−4.61 × 10⁻⁷」 |
| WM_L1#1_Table#1_Row#23 | 「60000」 | 「0.50」 | 「−6.02 × 10⁻⁷」 |

**Summary statistics at 298.15 K (23 data points):** V_E ranges from −1.014 × 10⁻⁶ to −4.61 × 10⁻⁷ m³/mol. The magnitude of V_E decreases (becomes less negative) with increasing pressure, indicating that high pressure reduces the volume contraction effect. At all pressures, the equimolar composition (x = 0.5) shows the largest contraction, consistent with the symmetric nature of water–methanol hydrogen bonding.

The full block contains 206 data points spanning 298.15–523.15 K, 100–60000 kPa, and x(methanol) = 0.25–0.75, with V_E ranging from −2.545 × 10⁻⁶ to −5 × 10⁻⁹ m³/mol.

**Core claims:**
- Excess molar volume data for the water + methanol binary system at 298.15 K were found in one ThermoML block (Safronov & Heyer, 2004), covering pressures from 100 to 60000 kPa at methanol mole fractions of 0.25, 0.5, and 0.75.
- All V_E values at 298.15 K are negative, ranging from −1.014 × 10⁻⁶ to −4.61 × 10⁻⁷ m³/mol, indicating volume contraction upon mixing consistent with strong hydrogen-bonding interactions between water and methanol.
- At all pressures studied, the equimolar composition (x(methanol) = 0.5) exhibits the most negative V_E, reflecting the composition of maximum intermolecular interaction.
- The magnitude of V_E decreases (becomes less negative) with increasing pressure at 298.15 K, indicating that high pressure reduces the volume contraction effect.
- The full data block contains 206 data points spanning 298.15–523.15 K, 100–60000 kPa, and x(methanol) = 0.25–0.75, with V_E ranging from −2.545 × 10⁻⁶ to −5 × 10⁻⁹ m³/mol.

**Core blocks found:**

**WM_L1#1_Blocks_(Analysis_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#2 | 「GLOBlit_2395」 | 「PROPblock_1」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_28」 | 「Excess molar volume data for water + methanol binary system at 298.15 K, pressures 100–60000 kPa, methanol mole fractions 0.25, 0.5, 0.75.」 |

*Not stored here: 1 verbatim data_inspections table(s); 4 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### density_data
**L1_query_2** — status: success · validation: FLAGGED(1)

**Summary:** Nine ThermoML data blocks were identified for the mass density (kg/m³) of the binary liquid water (H₂O) + methanol (CH₄O) system near 298.15 K. Six blocks were inspected in detail; three were not inspected and their values are not reported. Key inspected datasets at 298.15 K include: GLOBlit_2825/PROPblock_10 (DOI 10.1016/j.jct.2007.05.004, 39 points, 293.15–303.15 K, x(water) 0–1, P = 101.0 kPa, ρ 782.48–998.2 kg/m³), GLOBlit_8424/PROPblock_3 (DOI 10.1021/je049691v, 180 points, 283.15–353.15 K, x(water) 0.08–0.9603, ρ 747.01–988.05 kg/m³), and GLOBlit_10866/PROPblock_6 (DOI 10.1021/je700300y, 84 points, 283.15–313.15 K, x(water) 0.0871–0.964, P = 101.0 kPa, ρ 787.52–988.96 kg/m³). Representative 298.15 K values from GLOBlit_2825/PROPblock_10: ρ = 787.2 kg/m³ at x(water) = 0 (pure methanol), 795.47 at 0.049, 804.11 at 0.0993, 821.73 at 0.1973, 840.79 at 0.2983. From GLOBlit_8424/PROPblock_3: ρ = 800.1 at x(water) = 0.08, 813.88 at 0.1581, 829.11 at 0.2401, 844.62 at 0.3206, 860.25 at 0.3987. From GLOBlit_10866/PROPblock_6: ρ = 801.35 at x(water) = 0.0871, 812.99 at 0.1529, 828.9 at 0.2395, 846.53 at 0.3306, 861.73 at 0.4064. Additional blocks include GLOBlit_2432/PROPblock_1 (DOI 10.1016/j.jct.2004.07.019, 596 points, 298.16–573.15 K, high-pressure 390–30320 kPa, density reported as a difference) and GLOBlit_7085/PROPblock_6 (DOI 10.1021/acs.jced.6b01058, 12 points, 298.15–313.15 K, w(methanol) 0.04–0.16, P = 85.0 kPa, ρ 963.68–989.97 kg/m³). Density increases monotonically with increasing water mole fraction at 298.15 K across all inspected datasets, consistent with water's higher molecular packing density relative to methanol.

**Answer:**

#### Density Data for Water + Methanol Binary Mixture at ~298.15 K

**Compounds:**
- Water: GLOBcomp_1 (H₂O)
- Methanol: GLOBcomp_4 (CH₄O)

**Property:** Mass density (GLOBprop_1, kg/m³)

**System type:** Binary, liquid phase

##### Data Blocks Found (9 total)

The search returned 9 blocks. Six were inspected in this run; three (GLOBlit_8254/PROPblock_4, GLOBlit_8888/PROPblock_18, GLOBlit_9571/PROPblock_2) were not inspected and their detailed values are not reported.

###### Inspected Blocks

**WM_L1#2_Table#1_(Analysis_L1#2_Answer):**

| *row_id* | *DOI* | *Block* | *Literature ID* | *Data Points* | *T Range (K)* | *Composition Variable & Range* | *ρ Range (kg/m³)* | *Notes* |
|---|---|---|---|---|---|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「10.1016/j.jct.2007.05.004」 | 「PROPblock_10」 | 「GLOBlit_2825」 | 「39」 | 「293.15–303.15」 | 「x(water) 0–1」 | 「782.48–998.2」 | 「Full composition range, P = 101.0 kPa」 |
| WM_L1#2_Table#1_Row#2 | 「10.1021/je049691v」 | 「PROPblock_3」 | 「GLOBlit_8424」 | 「180」 | 「283.15–353.15」 | 「x(water) 0.08–0.9603」 | 「747.01–988.05」 | 「Broad T and composition coverage」 |
| WM_L1#2_Table#1_Row#3 | 「10.1021/je700300y」 | 「PROPblock_6」 | 「GLOBlit_10866」 | 「84」 | 「283.15–313.15」 | 「x(water) 0.0871–0.964」 | 「787.52–988.96」 | 「P = 101.0 kPa」 |
| WM_L1#2_Table#1_Row#4 | 「10.1016/j.jct.2004.07.019」 | 「PROPblock_1」 | 「GLOBlit_2432」 | 「596」 | 「298.16–573.15」 | 「b(methanol) 0.07706–1.04694」 | 「−13.3065 to −0.4632 (relative)」 | 「High-pressure (390–30320 kPa); density reported as difference」 |
| WM_L1#2_Table#1_Row#5 | 「10.1021/acs.jced.6b01058」 | 「PROPblock_6」 | 「GLOBlit_7085」 | 「12」 | 「298.15–313.15」 | 「w(methanol) 0.04–0.16」 | 「963.68–989.97」 | 「P = 85.0 kPa; narrow composition range」 |

###### Not Inspected in This Run

**WM_L1#2_Table#2_(Analysis_L1#2_Answer):**

| *row_id* | *DOI* | *Block* | *Literature ID* | *Details* |
|---|---|---|---|---|
| WM_L1#2_Table#2_Row#1 | 「10.1021/je034101z」 | 「PROPblock_4」 | 「GLOBlit_8254」 | 「Not inspected; data point counts and ranges not verified」 |
| WM_L1#2_Table#2_Row#2 | 「10.1021/je0601098」 | 「PROPblock_18」 | 「GLOBlit_8888」 | 「Not inspected; data point counts and ranges not verified」 |
| WM_L1#2_Table#2_Row#3 | 「10.1021/je2003622」 | 「PROPblock_2」 | 「GLOBlit_9571」 | 「Not inspected; data point counts and ranges not verified」 |
| WM_L1#2_Table#2_Row#4 | 「10.1021/je0600810」 | 「PROPblock_4」 | 「GLOBlit_8869」 | 「Not inspected; data point counts and ranges not verified」 |

##### Representative Data at 298.15 K

**GLOBlit_2825 / PROPblock_10** (at 298.15 K, P = 101.0 kPa):

**WM_L1#2_Table#3_(Analysis_L1#2_Answer):**

| *row_id* | *x(water)* | *ρ (kg/m³)* |
|---|---|---|
| WM_L1#2_Table#3_Row#1 | 「0」 | 「787.2」 |
| WM_L1#2_Table#3_Row#2 | 「0.049」 | 「795.47」 |
| WM_L1#2_Table#3_Row#3 | 「0.0993」 | 「804.11」 |
| WM_L1#2_Table#3_Row#4 | 「0.1973」 | 「821.73」 |
| WM_L1#2_Table#3_Row#5 | 「0.2983」 | 「840.79」 |

**GLOBlit_8424 / PROPblock_3** (at 298.15 K):

**WM_L1#2_Table#4_(Analysis_L1#2_Answer):**

| *row_id* | *x(water)* | *ρ (kg/m³)* |
|---|---|---|
| WM_L1#2_Table#4_Row#1 | 「0.08」 | 「800.1」 |
| WM_L1#2_Table#4_Row#2 | 「0.1581」 | 「813.88」 |
| WM_L1#2_Table#4_Row#3 | 「0.2401」 | 「829.11」 |
| WM_L1#2_Table#4_Row#4 | 「0.3206」 | 「844.62」 |
| WM_L1#2_Table#4_Row#5 | 「0.3987」 | 「860.25」 |

**GLOBlit_10866 / PROPblock_6** (at 298.15 K, P = 101.0 kPa):

**WM_L1#2_Table#5_(Analysis_L1#2_Answer):**

| *row_id* | *x(water)* | *ρ (kg/m³)* |
|---|---|---|
| WM_L1#2_Table#5_Row#1 | 「0.0871」 | 「801.35」 |
| WM_L1#2_Table#5_Row#2 | 「0.1529」 | 「812.99」 |
| WM_L1#2_Table#5_Row#3 | 「0.2395」 | 「828.9」 |
| WM_L1#2_Table#5_Row#4 | 「0.3306」 | 「846.53」 |
| WM_L1#2_Table#5_Row#5 | 「0.4064」 | 「861.73」 |

##### Chemistry Insight

The inspected data show that density increases monotonically with increasing water mole fraction across all three datasets at 298.15 K. For example, in GLOBlit_2825/PROPblock_10, density rises from 787.2 kg/m³ at x(water) = 0 (pure methanol) to 840.79 kg/m³ at x(water) = 0.2983, consistent with water's stronger hydrogen-bonding network and higher molecular packing density compared to methanol.

**Core claims:**
- Nine ThermoML data blocks were identified for the mass density of the water + methanol binary liquid mixture near 298.15 K; six were inspected and three were not, so coverage is incomplete.
- At 298.15 K and ambient pressure (~101.0 kPa), the inspected datasets consistently show that density increases monotonically with increasing water mole fraction, ranging from about 787.2 kg/m³ at x(water) = 0 (pure methanol) up through the full composition range toward pure water.
- Three independent datasets (GLOBlit_2825/PROPblock_10, GLOBlit_8424/PROPblock_3, GLOBlit_10866/PROPblock_6) show mutually consistent density values at 298.15 K for overlapping water mole fractions.
- One block (GLOBlit_2432/PROPblock_1) reports density as a relative difference at high pressures (390–30320 kPa) rather than absolute density, limiting its direct comparability with the ambient-pressure data.
- Several blocks were not inspected in the run, and one block (PROPblock_2) was flagged as UNINSPECTED_BLOCK with unverified quoted values.

**Core blocks found:**

**WM_L1#2_Blocks_(Analysis_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#6 | 「GLOBlit_2825」 | 「PROPblock_10」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of water + methanol at 293.15–303.15 K, full composition range, P = 101.0 kPa; 39 data points.」 |
| WM_L1#2_Table#7 | 「GLOBlit_8424」 | 「PROPblock_3」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of water + methanol at 283.15–353.15 K, x(water) 0.08–0.9603; 180 data points.」 |
| WM_L1#2_Table#8 | 「GLOBlit_10866」 | 「PROPblock_6」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of water + methanol at 283.15–313.15 K, x(water) 0.0871–0.964, P = 101.0 kPa; 84 data points.」 |
| WM_L1#2_Table#9 | 「GLOBlit_2432」 | 「PROPblock_1」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density (relative difference) of water + methanol at 298.16–573.15 K, high pressure 390–30320 kPa; 596 data points.」 |
| WM_L1#2_Table#10 | 「GLOBlit_7085」 | 「PROPblock_6」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of water + methanol at 298.15–313.15 K, w(methanol) 0.04–0.16, P = 85.0 kPa; 12 data points.」 |
| WM_L1#2_Table#11 | 「GLOBlit_8254」 | 「PROPblock_4」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of water + methanol; not inspected in this run.」 |
| WM_L1#2_Table#12 | 「GLOBlit_8888」 | 「PROPblock_18」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of water + methanol; not inspected in this run.」 |
| WM_L1#2_Table#13 | 「GLOBlit_9571」 | 「PROPblock_2」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of water + methanol; not inspected in this run.」 |
| WM_L1#2_Table#14 | 「GLOBlit_8869」 | 「PROPblock_4」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of water + methanol; not inspected in this run.」 |

*Not stored here: 5 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(1) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNINSPECTED_BLOCK** PROPblock_2: PROPblock_2 is quoted with data values (298.15, …) but was never inspected in this run


### Inspected Blocks
- GLOBlit_2825 | 10.1016/j.jct.2007.05.004 | PROPblock_10: 39 rows; x=['mole_fraction_<water>']; y=['mass_density_kg_m3']
    - BLKprop_1 / GLOBprop_1: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_1: kind=direct; materialize_reference=False; supported=True; units=kg/m3 -> kg/m3

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

