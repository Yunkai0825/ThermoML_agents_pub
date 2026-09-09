# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_023326_012061_3dba9dd4\analysis_runs\run_3`

### ID Catalog
| type | global_id | name | pure_values |
|------|--------|------|-------------|
| comp | GLOBcomp_1 | water | 1.8068301e-05 |
| comp | GLOBcomp_4 | methanol | 4.070376e-05 |
| prop | GLOBprop_1 | massdensitykgm3 |  |
| var | GLOBvar_1 | temperaturek |  |
| var | GLOBvar_2 | molefraction<water> |  |
| constr | GLOBconstr_1 | pressurekpa |  |

### History
- [query_thermoml_parallel]
- [fit_block_derived] ERROR: Constraint column 'Temperature, K' not found
- [inspect_block]
- [fit_block_derived]
- [predict_from_rk]
- [list_session_files]

### Query Results
#### direct_VE
**L1_query_1** — status: success · validation: PASS

**Summary:** Excess molar volume (V^E) data for the water + methanol binary liquid system at 298.15 K were found in one ThermoML data block (DOI 10.1016/j.jct.2004.03.011, GLOBlit_2395, PROPblock_1, GLOBprop_28). At 298.15 K, 23 data points span 8 pressures (100–60000 kPa) and 3 methanol mole fractions (0.25, 0.50, 0.75). All V^E values are negative, ranging from −1.014 × 10⁻⁶ to −4.61 × 10⁻⁷ m³/mol, indicating volume contraction upon mixing due to strong hydrogen-bonding interactions. The most negative value, −1.014 × 10⁻⁶ m³/mol (≈ −1.014 cm³/mol), occurs at x(methanol) = 0.50 and 100 kPa. As pressure increases, V^E becomes less negative, reflecting reduced relative contraction as pure-component liquids are already more compressed at elevated pressures. Only three compositions were measured, so the full composition dependence is not captured. No additional ThermoML blocks with excess molar volume for this binary at 298.15 K were found.

**Answer:**

**Excess Molar Volume (V^E) Data for Water + Methanol Binary at 298.15 K**

One data block was found in the ThermoML database:

- **Source:** DOI 10.1016/j.jct.2004.03.011 (GLOBlit_2395)
- **Block:** PROPblock_1
- **Property:** Excess molar volume (GLOBprop_28), units: m³/mol
- **System:** Binary — water (GLOBcomp_1) + methanol (GLOBcomp_4), liquid phase
- **Total data points in block:** 206 (temperatures 298.15–523.15 K, pressures 100–60000 kPa, x(methanol) = 0.25, 0.5, 0.75)

At **T = 298.15 K**, 23 data points are available across 8 pressures and 3 methanol mole fractions:

**WM_L1#1_Table#1_(Analysis_L1#1_Answer):**

| *row_id* | *Pressure (kPa)* | *x(methanol)* | *V^E (m³/mol)* |
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

**Key observations:**
- All V^E values are **negative**, indicating volume contraction upon mixing — consistent with strong hydrogen-bonding interactions between water and methanol molecules that lead to more efficient molecular packing than in the pure components.
- The most negative V^E at 298.15 K occurs at **x(methanol) = 0.50** and **100 kPa**: −1.014 × 10⁻⁶ m³/mol (≈ −1.014 cm³/mol), reflecting maximum intermolecular interaction at equimolar composition.
- As pressure increases from 100 to 60000 kPa, the magnitude of V^E decreases (becomes less negative), indicating that high pressure reduces the relative contraction effect — the pure-component liquids are already more compressed at elevated pressures, diminishing the additional packing efficiency gained upon mixing.
- The range of V^E across all 23 points at 298.15 K is −1.014 × 10⁻⁶ to −4.61 × 10⁻⁷ m³/mol.

Note: The data in this block were measured at only three compositions (x = 0.25, 0.50, 0.75), so the full composition dependence of V^E is not captured. No additional blocks with excess molar volume for this binary system at 298.15 K were found in the database.

**Core claims:**
- ThermoML data (DOI 10.1016/j.jct.2004.03.011) provide 23 excess molar volume (V^E) data points for the water + methanol binary liquid system at 298.15 K, spanning pressures 100–60000 kPa and methanol mole fractions 0.25, 0.50, and 0.75.
- All V^E values at 298.15 K are negative, indicating volume contraction upon mixing consistent with strong hydrogen-bonding interactions between water and methanol.
- The most negative V^E at 298.15 K occurs at x(methanol) = 0.50 and 100 kPa: −1.014 × 10⁻⁶ m³/mol.
- As pressure increases from 100 to 60000 kPa at 298.15 K, the magnitude of V^E decreases (becomes less negative), indicating that high pressure reduces the relative volume contraction effect upon mixing.
- The data cover only three compositions (x = 0.25, 0.50, 0.75), so the full composition dependence of V^E is not captured.

**Core blocks found:**

**WM_L1#1_Blocks_(Analysis_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#2 | 「GLOBlit_2395」 | 「PROPblock_1」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_28」 | 「Excess molar volume for water + methanol binary system at 298.15–523.15 K and 100–60000 kPa.」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### density_data
**L1_query_2** — status: success · validation: PASS

**Summary:** Nine ThermoML blocks were found for binary water (GLOBcomp_1, CAS 7732-18-5) + methanol (GLOBcomp_4, CAS 67-56-1) mass density (GLOBprop_1, kg/m³) near 298.15 K. Four blocks were inspected in detail. GLOBlit_2825 / PROPblock_10 (DOI 10.1016/j.jct.2007.05.004) is the best ambient-pressure source, with 39 data points spanning T = 293.15–303.15 K, P = 101.0 kPa, and the full composition range x(water) = 0–1, giving absolute densities from 787.2 kg/m³ (pure methanol) to 998.2 kg/m³ (pure water). Representative values at exactly 298.15 K include x(water) = 0 → 787.2 kg/m³, 0.049 → 795.47, 0.0993 → 804.11, 0.1973 → 821.73, and 0.2983 → 840.79 kg/m³. GLOBlit_7085 / PROPblock_6 (DOI 10.1021/acs.jced.6b01058) provides 12 points at P = 85.0 kPa but only for dilute methanol (w = 0.04–0.16), with 298.15 K densities of 989.97, 982.92, and 969.42 kg/m³. GLOBlit_2432 / PROPblock_1 (DOI 10.1016/j.jct.2004.07.019) contains 596 high-pressure points reporting density deviations rather than absolute values. GLOBlit_8254 / PROPblock_4 (DOI 10.1021/je034101z) has 401 high-pressure points with absolute densities spanning 762.2–966 kg/m³. Five additional blocks were identified but not inspected.

**Answer:**

#### Binary Water + Methanol Density Data near 298.15 K

**Compounds:**
- Water (H₂O): GLOBcomp_1 (CAS 7732-18-5)
- Methanol (CH₄O): GLOBcomp_4 (CAS 67-56-1)

**Property:** Mass density (GLOBprop_1), units: kg/m³

**System type:** Binary

A total of **9 blocks** were found in the ThermoML database for binary water + methanol mass density near 298.15 K. Four key blocks were inspected in detail:

---

##### Block 1 — GLOBlit_2432 / PROPblock_1
**DOI:** 10.1016/j.jct.2004.07.019
- **596 data points** total; T range: 298.16–573.15 K; P range: 390–30320 kPa
- Composition variable: molality of methanol (0.07706–1.04694 mol/kg)
- Density values are **deviations** (−13.3065 to −0.4632 kg/m³), not absolute densities
- **High-pressure data** — not ambient-condition measurements
- Representative rows nearest 298.15 K (all at 298.16 K, 14450 kPa):

**WM_L1#2_Table#1_(Analysis_L1#2_Answer):**

| *row_id* | *molality (methanol)* | *ρ (kg/m³, deviation)* |
|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「0.10243」 | 「−0.6308」 |
| WM_L1#2_Table#1_Row#2 | 「0.19833」 | 「−1.2112」 |
| WM_L1#2_Table#1_Row#3 | 「0.35111」 | 「−2.1094」 |
| WM_L1#2_Table#1_Row#4 | 「0.52912」 | 「−3.1426」 |
| WM_L1#2_Table#1_Row#5 | 「0.74847」 | 「−4.3834」 |

---

##### Block 2 — GLOBlit_2825 / PROPblock_10 ⭐ Best candidate
**DOI:** 10.1016/j.jct.2007.05.004
- **39 data points**; T range: 293.15–303.15 K; P = 101.0 kPa (ambient)
- Composition variable: mole fraction of water (0–1) — **full composition range**
- Absolute density: 782.48–998.2 kg/m³
- Representative rows at exactly 298.15 K:

**WM_L1#2_Table#2_(Analysis_L1#2_Answer):**

| *row_id* | *x(water)* | *ρ (kg/m³)* |
|---|---|---|
| WM_L1#2_Table#2_Row#1 | 「0」 | 「787.2」 |
| WM_L1#2_Table#2_Row#2 | 「0.049」 | 「795.47」 |
| WM_L1#2_Table#2_Row#3 | 「0.0993」 | 「804.11」 |
| WM_L1#2_Table#2_Row#4 | 「0.1973」 | 「821.73」 |
| WM_L1#2_Table#2_Row#5 | 「0.2983」 | 「840.79」 |

This block provides the broadest composition coverage at ambient pressure and includes exact 298.15 K data, making it the best source for mixture density across the full composition range.

---

##### Block 3 — GLOBlit_7085 / PROPblock_6
**DOI:** 10.1021/acs.jced.6b01058
- **12 data points**; T range: 298.15–313.15 K; P = 85.0 kPa
- Composition variable: mass fraction of methanol (0.04–0.16) — **dilute methanol only**
- Absolute density: 963.68–989.97 kg/m³
- Rows at exactly 298.15 K:

**WM_L1#2_Table#3_(Analysis_L1#2_Answer):**

| *row_id* | *w(methanol)* | *ρ (kg/m³)* |
|---|---|---|
| WM_L1#2_Table#3_Row#1 | 「0.04」 | 「989.97」 |
| WM_L1#2_Table#3_Row#2 | 「0.08」 | 「982.92」 |
| WM_L1#2_Table#3_Row#3 | 「0.16」 | 「969.42」 |

---

##### Block 4 — GLOBlit_8254 / PROPblock_4
**DOI:** 10.1021/je034101z
- **401 data points**; T range: 287.15–417.15 K; P range: 3721–29927 kPa
- Composition variable: mole fraction of methanol (0.059–0.708)
- Absolute density: 762.2–966 kg/m³
- **High-pressure data** — not ambient conditions
- Rows nearest 298.15 K:

**WM_L1#2_Table#4_(Analysis_L1#2_Answer):**

| *row_id* | *x(methanol)* | *T (K)* | *P (kPa)* | *ρ (kg/m³)* |
|---|---|---|---|---|
| WM_L1#2_Table#4_Row#1 | 「0.352」 | 「297.15」 | 「14323」 | 「933」 |
| WM_L1#2_Table#4_Row#2 | 「0.502」 | 「297.15」 | 「20666」 | 「883.1」 |
| WM_L1#2_Table#4_Row#3 | 「0.352」 | 「298.15」 | 「15512」 | 「932.9」 |
| WM_L1#2_Table#4_Row#4 | 「0.502」 | 「298.15」 | 「21895」 | 「883」 |
| WM_L1#2_Table#4_Row#5 | 「0.352」 | 「299.15」 | 「16706」 | 「932.8」 |

---

##### Summary & Recommendation

For ambient-pressure mixture density of water + methanol across the full composition range at 298.15 K, **GLOBlit_2825 / PROPblock_10** (DOI: 10.1016/j.jct.2007.05.004) is the most suitable source. It covers x(water) = 0 to 1 at 101.0 kPa with absolute density values spanning 787.2 kg/m³ (pure methanol) to 998.2 kg/m³ (pure water). Five additional blocks (9 total found) were not inspected but may offer complementary data at other conditions. Blocks 1 and 4 are high-pressure datasets, and Block 3 covers only dilute methanol compositions.

**Core claims:**
- Nine blocks of binary water + methanol mass density data near 298.15 K were found in the ThermoML database.
- GLOBlit_2825 / PROPblock_10 (DOI: 10.1016/j.jct.2007.05.004) is identified as the most suitable source for ambient-pressure mixture density across the full composition range at 298.15 K, covering x(water) = 0 to 1 at 101.0 kPa with absolute density values spanning 787.2 kg/m³ (pure methanol) to 998.2 kg/m³ (pure water).
- GLOBlit_2432 / PROPblock_1 (DOI: 10.1016/j.jct.2004.07.019) reports density deviations rather than absolute densities and covers high-pressure conditions (390–30320 kPa), making it unsuitable for ambient-condition analysis.
- GLOBlit_7085 / PROPblock_6 (DOI: 10.1021/acs.jced.6b01058) covers only dilute methanol compositions (mass fraction 0.04–0.16) at 85.0 kPa.
- GLOBlit_8254 / PROPblock_4 (DOI: 10.1021/je034101z) is a high-pressure dataset (3721–29927 kPa) and not representative of ambient conditions.
- Five of the nine total blocks found were not inspected in detail and may offer complementary data at other conditions.

**Core blocks found:**

**WM_L1#2_Blocks_(Analysis_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#5 | 「GLOBlit_2432」 | 「PROPblock_1」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density deviations for water + methanol at high pressure; T range 298.16–573.15 K, P range 390–30320 kPa, molality of methanol 0.077–1.047 mol/kg; 596 data points.」 |
| WM_L1#2_Table#6 | 「GLOBlit_2825」 | 「PROPblock_10」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Absolute mass density for water + methanol at ambient pressure (101.0 kPa); T range 293.15–303.15 K, full composition range x(water) 0–1, density 782.48–998.2 kg/m³; 39 data points. Best candidate for ambient 298.15 K mixture density.」 |
| WM_L1#2_Table#7 | 「GLOBlit_7085」 | 「PROPblock_6」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Absolute mass density for water + methanol at 85.0 kPa; T range 298.15–313.15 K, dilute methanol mass fraction 0.04–0.16, density 963.68–989.97 kg/m³; 12 data points.」 |
| WM_L1#2_Table#8 | 「GLOBlit_8254」 | 「PROPblock_4」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Absolute mass density for water + methanol at high pressure; T range 287.15–417.15 K, P range 3721–29927 kPa, mole fraction of methanol 0.059–0.708, density 762.2–966 kg/m³; 401 data points.」 |

*Not stored here: 4 verbatim data_inspections table(s); 3 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


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

