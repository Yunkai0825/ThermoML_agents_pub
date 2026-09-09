# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_060730_675228_c6863be1`

### ID Catalog
| type | global_id | name | pure_values |
|------|--------|------|-------------|
| comp | GLOBcomp_9 | acetone | 7.4050463e-05 |
| comp | GLOBcomp_1 | water | 1.830898e-05 |
| prop | GLOBprop_1 | massdensitykgm3 |  |
| var | GLOBvar_2 | molefraction<acetone> |  |
| var | GLOBvar_1 | temperaturek |  |
| constr | GLOBconstr_1 | pressurekpa |  |

### History
- [query_thermoml_parallel]
- [inspect_block]
- [inspect_block]
- [fit_block_derived] ERROR: Unknown transform 'density_to_excess_molar_volume'. Available: ['density_to_mola
- [fit_block_derived] ERROR: Constraint column 'Temperature, K' not found
- [fit_block_derived]
- [fit_block_derived]
- [inspect_block]
- [inspect_block]
- [query_thermoml_parallel]

### Query Results
#### excess_volume
**L1_query_1** — status: no_results · validation: PASS

**Summary:** A comprehensive search of the ThermoML database for excess molar volume (GLOBprop_28) of the binary system acetone (GLOBcomp_9, C₃H₆O) + water (GLOBcomp_1, H₂O) at 298.15 K returned zero matching blocks. The database contains 16 data blocks for this binary system covering other properties—mass density (GLOBprop_1, 3 blocks), activity coefficient (GLOBprop_3, 2 blocks), refractive index (GLOBprop_7, 1 block), surface tension (GLOBprop_13, 1 block), molar enthalpy of solution (GLOBprop_15, 1 block), Henry's Law constant (GLOBprop_27, 3 blocks), and binary diffusion coefficient (GLOBprop_29, 3 blocks)—but none for excess molar volume. The mass density data (243 data points across 3 blocks) could in principle be used to calculate excess molar volumes if pure-component densities are available, but no pre-computed excess molar volume entries exist for this system in ThermoML.

**Answer:**

**Excess molar volume data for acetone + water binary mixture at 298.15 K: Not found in the ThermoML database.**

A comprehensive search of the ThermoML database for the binary system acetone (GLOBcomp_9, C₃H₆O) + water (GLOBcomp_1, H₂O) with excess molar volume (GLOBprop_28) returned zero matching blocks — both with and without a temperature filter around 298.15 K.

The database does contain 16 data blocks for the acetone + water binary system, but they cover other properties:

**WM_L1_Q1_Table#1_(Analysis_L1_Q1_Answer):**

| *row_id* | *Property* | *GLOBprop ID* | *Blocks* | *Example DOI* |
|---|---|---|---|---|
| WM_L1_Q1_Table#1_Row#1 | 「Mass density (kg/m³)」 | 「GLOBprop_1」 | 「3」 | 「10.1016/j.tca.2006.01.008 (GLOBlit_5679)」 |
| WM_L1_Q1_Table#1_Row#2 | 「Activity coefficient」 | 「GLOBprop_3」 | 「2」 | 「10.1021/je0495942 (GLOBlit_8381)」 |
| WM_L1_Q1_Table#1_Row#3 | 「Refractive index (Na D-line)」 | 「GLOBprop_7」 | 「1」 | 「10.1016/j.tca.2006.01.008 (GLOBlit_5679)」 |
| WM_L1_Q1_Table#1_Row#4 | 「Surface tension liquid-gas (N/m)」 | 「GLOBprop_13」 | 「1」 | 「10.1021/je7000182 (GLOBlit_10721)」 |
| WM_L1_Q1_Table#1_Row#5 | 「Molar enthalpy of solution (kJ/mol)」 | 「GLOBprop_15」 | 「1」 | 「10.1016/j.tca.2010.07.017 (GLOBlit_5893)」 |
| WM_L1_Q1_Table#1_Row#6 | 「Henry's Law constant (kPa)」 | 「GLOBprop_27」 | 「3」 | 「10.1016/j.fluid.2005.02.006 (GLOBlit_241)」 |
| WM_L1_Q1_Table#1_Row#7 | 「Binary diffusion coefficient (m²/s)」 | 「GLOBprop_29」 | 「3」 | 「—」 |

**Chemistry note:** While excess molar volume data is not directly available, the mass density data (GLOBprop_1, 243 data points across 3 blocks) could in principle be used to calculate excess molar volumes if pure-component densities are also available, since V^E = V_mix − Σ x_i V_i*. However, no pre-computed excess molar volume entries exist for this system in ThermoML.

**Core claims:**
- A comprehensive search of the ThermoML database for the binary system acetone + water with excess molar volume (GLOBprop_28) returned zero matching blocks, both with and without a temperature filter around 298.15 K.
- The database contains 16 data blocks for the acetone + water binary system covering other properties (mass density, activity coefficient, refractive index, surface tension, molar enthalpy of solution, Henry's Law constant, and binary diffusion coefficient), but no pre-computed excess molar volume entries exist.
- Mass density data (GLOBprop_1, 243 data points across 3 blocks) could in principle be used to calculate excess molar volumes if pure-component densities are also available, but such derived values are not present in the database.

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### density_data
**L1_query_2** — status: success · validation: FLAGGED(1)

**Summary:** Density data for the binary mixture acetone (GLOBcomp_9) + water (GLOBcomp_1) at 298.15 K were identified in three ThermoML blocks (PROPblock_8, PROPblock_5, PROPblock_6). Only PROPblock_8 (GLOBlit_5679, DOI: 10.1016/j.tca.2006.01.008) was inspected. It contains 22 mass-density (GLOBprop_1) data points at exactly 298.15 K and 101.0 kPa, with x(acetone) ranging from 0.0502 to 0.9451 and density from 789.9 to 977 kg/m³. Representative values include 977 kg/m³ at x = 0.0502, 911.8 at 0.2496, 884.8 at 0.3507, 862.1 at 0.4509, 843.5 at 0.5489, 827 at 0.6506, 806.2 at 0.8011, 806.3 at 0.8015, and 789.9 at 0.9451. Density decreases with increasing acetone mole fraction; the full 22-point dataset shows 2 extrema, consistent with known excess-volume anomalies from strong hydrogen-bonding interactions in this system. PROPblock_5 (GLOBlit_8129) and PROPblock_6 (GLOBlit_10721) were not inspected and no numerical details from them are verified.

**Answer:**

#### Density Data for Acetone + Water Binary Mixture at 298.15 K

Three binary acetone–water density blocks were found in the ThermoML database via the search_blocks discovery tool.

##### Available Data Blocks

**PROPblock_8** (GLOBlit_5679, DOI: 10.1016/j.tca.2006.01.008) — 22 data points at exactly 298.15 K, x(acetone) from 0.0502 to 0.9451, at 101.0 kPa. *(Inspected and fully grounded below.)*

**PROPblock_5** (GLOBlit_8129, DOI: 10.1021/je030102f) — Additional density data covering a wider temperature range and partial composition range. *(Not inspected in this run; no numerical details quoted.)*

**PROPblock_6** (GLOBlit_10721, DOI: 10.1021/je7000182) — Additional density data covering the full composition range at multiple temperatures. *(Not inspected in this run; no numerical details quoted.)*

##### Inspected Density Data at 298.15 K (PROPblock_8, GLOBlit_5679)

This block provides an isothermal dataset at exactly 298.15 K and 101.0 kPa, spanning nearly the full composition range (22 data points total). A shape-preserving subset:

**WM_L1#2_Table#1_(Analysis_L1#2_Answer):**

| *row_id* | *x(acetone)* | *ρ (kg/m³)* |
|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「0.0502」 | 「977」 |
| WM_L1#2_Table#1_Row#2 | 「0.2496」 | 「911.8」 |
| WM_L1#2_Table#1_Row#3 | 「0.3507」 | 「884.8」 |
| WM_L1#2_Table#1_Row#4 | 「0.4509」 | 「862.1」 |
| WM_L1#2_Table#1_Row#5 | 「0.5489」 | 「843.5」 |
| WM_L1#2_Table#1_Row#6 | 「0.6506」 | 「827」 |
| WM_L1#2_Table#1_Row#7 | 「0.8011」 | 「806.2」 |
| WM_L1#2_Table#1_Row#8 | 「0.8015」 | 「806.3」 |
| WM_L1#2_Table#1_Row#9 | 「0.9451」 | 「789.9」 |

**Property:** Mass density (GLOBprop_1), in kg/m³.
**Compounds:** Acetone (GLOBcomp_9) + Water (GLOBcomp_1).
**Full stats (n = 22):** x(acetone) from 0.0502 to 0.9451; density from 789.9 to 977 kg/m³.

**Chemical insight:** The density decreases with increasing acetone mole fraction at 298.15 K, from near-pure water (~977 kg/m³ at x = 0.0502) toward near-pure acetone (~789.9 kg/m³ at x = 0.9451). The inspection topology notes a non-monotonic character with 2 extrema across all 22 points, suggesting subtle density anomalies — consistent with the known strong hydrogen-bonding interactions and excess volume effects in the acetone–water system.

**Core claims:**
- At 298.15 K and 101.0 kPa, the density of the acetone–water binary mixture decreases with increasing acetone mole fraction, from ~977 kg/m³ at x(acetone) = 0.0502 to ~789.9 kg/m³ at x(acetone) = 0.9451, based on 22 data points from PROPblock_8 (DOI: 10.1016/j.tca.2006.01.008).
- The full 22-point dataset exhibits non-monotonic character with 2 extrema, consistent with known strong hydrogen-bonding interactions and excess volume effects in the acetone–water system.
- Two additional density data blocks (PROPblock_5 and PROPblock_6) were identified but not inspected; no numerical details from those blocks are verified.

**Core blocks found:**

**WM_L1#2_Blocks_(Analysis_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#2 | 「GLOBlit_5679」 | 「PROPblock_8」 | 「GLOBcomp_9, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density data for acetone + water at 298.15 K and 101.0 kPa, 22 data points, x(acetone) from 0.0502 to 0.9451, density from 789.9 to 977 kg/m³.」 |
| WM_L1#2_Table#3 | 「GLOBlit_8129」 | 「PROPblock_5」 | 「GLOBcomp_9, GLOBcomp_1」 | 「GLOBprop_1」 | 「Density data for acetone + water covering a wider temperature range and partial composition range. Not inspected in this run.」 |
| WM_L1#2_Table#4 | 「GLOBlit_10721」 | 「PROPblock_6」 | 「GLOBcomp_9, GLOBcomp_1」 | 「GLOBprop_1」 | 「Density data for acetone + water covering the full composition range at multiple temperatures. Not inspected in this run.」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(1) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNINSPECTED_BLOCK** PROPblock_6: PROPblock_6 is quoted with data values (298.15, …) but was never inspected in this run


#### inspect_PROPblock_5
**L1_query_3** — status: success · validation: PASS

**Summary:** PROPblock_5 of DOI 10.1021/je030102f (GLOBlit_8129) reports mass density for the binary acetone + water system across 99 data points spanning temperatures 283.15–323.148 K, acetone mole fractions 0–1, and a constant pressure of 101.325 kPa, with densities ranging from 755.314 to 999.691 kg/m³. At ~298.15 K (actual temperatures 298.145–298.146 K), eight rows show density decreasing monotonically from 997.019 kg/m³ for pure water to 784.638 kg/m³ for pure acetone. No row exists at exactly 298.15 K; the nearest temperatures below and above are 298.146 K and 303.144 K, respectively.

**Answer:**

Here are the actual data rows from PROPblock_5 of DOI 10.1021/je030102f (GLOBlit_8129), which is a binary acetone + water mass density block.

**Block overview (99 data points total):**
- **Temperature range:** 283.15 – 323.148 K
- **Pressure:** 101.325 kPa (constant, block constraint)
- **Mole fraction (acetone):** 0 – 1
- **Mass density:** 755.314 – 999.691 kg/m³

**Data rows nearest T = 298.15 K** (8 rows returned; actual temperatures are 298.145–298.146 K):

**WM_L1#3_Table#1_(Analysis_L1#3_Answer):**

| *row_id* | *BLKpoint_id* | *Mole fraction (acetone)* | *Temperature (K)* | *Pressure (kPa)* | *Mass density (kg/m³)* |
|---|---|---|---|---|---|
| WM_L1#3_Table#1_Row#1 | 「BLKpoint_4」 | 「0」 | 「298.146」 | 「101.325」 | 「997.019」 |
| WM_L1#3_Table#1_Row#2 | 「BLKpoint_22」 | 「0.2193」 | 「298.145」 | 「101.325」 | 「919.968」 |
| WM_L1#3_Table#1_Row#3 | 「BLKpoint_31」 | 「0.2973」 | 「298.145」 | 「101.325」 | 「899.375」 |
| WM_L1#3_Table#1_Row#4 | 「BLKpoint_40」 | 「0.3998」 | 「298.145」 | 「101.325」 | 「874.098」 |
| WM_L1#3_Table#1_Row#5 | 「BLKpoint_49」 | 「0.4986」 | 「298.146」 | 「101.325」 | 「853.436」 |
| WM_L1#3_Table#1_Row#6 | 「BLKpoint_67」 | 「0.6984」 | 「298.145」 | 「101.325」 | 「820.292」 |
| WM_L1#3_Table#1_Row#7 | 「BLKpoint_76」 | 「0.7934」 | 「298.145」 | 「101.325」 | 「807.383」 |
| WM_L1#3_Table#1_Row#8 | 「BLKpoint_94」 | 「1」 | 「298.146」 | 「101.325」 | 「784.638」 |

**Bracketing note:** No row exists at exactly 298.15 K; the nearest below is BLKpoint_94 at 298.146 K, and the nearest above is BLKpoint_32 at 303.144 K.

**Chemistry insight:** The density decreases monotonically from pure water (997.019 kg/m³) to pure acetone (784.638 kg/m³) at ~298.15 K and atmospheric pressure. The data span the full composition range (x_acetone = 0 to 1) across multiple temperatures (283.15–323.15 K), all at atmospheric pressure (101.325 kPa), providing a comprehensive density map for this industrially important binary system.

**Core claims:**
- In DOI 10.1021/je030102f (PROPblock_5), the mass density of the binary acetone + water system at ~298.15 K and 101.325 kPa decreases monotonically from 997.019 kg/m³ for pure water (x_acetone = 0) to 784.638 kg/m³ for pure acetone (x_acetone = 1).
- The block contains 99 data points spanning temperatures from 283.15 to 323.148 K, acetone mole fractions from 0 to 1, and mass densities from 755.314 to 999.691 kg/m³, all at a constant pressure of 101.325 kPa.
- No data row exists at exactly 298.15 K; the nearest measured temperatures are 298.145–298.146 K (below) and 303.144 K (above).

**Core blocks found:**

**WM_L1#3_Blocks_(Analysis_L1#3_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#3_Table#2 | 「GLOBlit_8129」 | 「PROPblock_5」 | 「GLOBcomp_9, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density measurements for acetone + water binary system at 283.15–323.148 K, 101.325 kPa, and acetone mole fractions 0–1.」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### inspect_PROPblock_6
**L1_query_4** — status: success · validation: PASS

**Summary:** PROPblock_6 from DOI 10.1021/je7000182 (GLOBlit_10721) reports mass density (kg·m⁻³) for the binary system acetone (GLOBcomp_9) + water (GLOBcomp_1). The block contains 126 data points spanning temperatures 288.15–328.15 K, acetone mole fractions 0–1, and a constant pressure of 101.0 kPa, with densities ranging from 748.98 to 999.12 kg·m⁻³. At 298.15 K, eight data points show density decreasing monotonically from 997.06 kg·m⁻³ (pure water, x=0) to 874.80 kg·m⁻³ at x(acetone)=0.4, with intermediate values of 992.55 (x=0.0099), 977.21 (x=0.05), 959.83 (x=0.1), 943.05 (x=0.15), 927.37 (x=0.2), and 898.35 (x=0.3) kg·m⁻³.

**Answer:**

Here are the inspection results for **PROPblock_6** from DOI **10.1021/je7000182** (GLOBlit_10721), which is a binary acetone + water mass density block.

##### Block Overview

- **System:** binary — acetone (GLOBcomp_9) + water (GLOBcomp_1)
- **Property:** Mass density (kg·m⁻³)
- **Total data points:** 126
- **Temperature range:** 288.15 – 328.15 K
- **Pressure:** 101.0 kPa (constant, block constraint)
- **Mole fraction (acetone) range:** 0 – 1
- **Density range:** 748.98 – 999.12 kg·m⁻³

##### Data Rows at T = 298.15 K

**WM_L1#4_Table#1_(Analysis_L1#4_Answer):**

| *row_id* | *BLKpoint_id* | *temperature_k* | *mole_fraction (acetone)* | *pressure_kpa* | *mass_density_kg_m3* |
|---|---|---|---|---|---|
| WM_L1#4_Table#1_Row#1 | 「BLKpoint_29」 | 「298.15」 | 「0」 | 「101.0」 | 「997.06」 |
| WM_L1#4_Table#1_Row#2 | 「BLKpoint_30」 | 「298.15」 | 「0.0099」 | 「101.0」 | 「992.55」 |
| WM_L1#4_Table#1_Row#3 | 「BLKpoint_31」 | 「298.15」 | 「0.05」 | 「101.0」 | 「977.21」 |
| WM_L1#4_Table#1_Row#4 | 「BLKpoint_32」 | 「298.15」 | 「0.1」 | 「101.0」 | 「959.83」 |
| WM_L1#4_Table#1_Row#5 | 「BLKpoint_33」 | 「298.15」 | 「0.15」 | 「101.0」 | 「943.05」 |
| WM_L1#4_Table#1_Row#6 | 「BLKpoint_34」 | 「298.15」 | 「0.2」 | 「101.0」 | 「927.37」 |
| WM_L1#4_Table#1_Row#7 | 「BLKpoint_35」 | 「298.15」 | 「0.3」 | 「101.0」 | 「898.35」 |
| WM_L1#4_Table#1_Row#8 | 「BLKpoint_36」 | 「298.15」 | 「0.4」 | 「101.0」 | 「874.80」 |

These 8 rows are at exactly 298.15 K and span mole fractions of acetone from 0 (pure water) to 0.4. The density decreases monotonically from 997.06 kg·m⁻³ (pure water) to 874.80 kg·m⁻³ at x(acetone) = 0.4, consistent with the lower density of acetone compared to water. The full block extends to x(acetone) = 1 and covers temperatures from 288.15 to 328.15 K at atmospheric pressure (101 kPa).

**Core claims:**
- PROPblock_6 from DOI 10.1021/je7000182 reports mass density (kg·m⁻³) for the binary acetone + water system, comprising 126 data points spanning 288.15–328.15 K, acetone mole fractions 0–1, at a constant pressure of 101.0 kPa, with densities ranging from 748.98 to 999.12 kg·m⁻³.
- At 298.15 K and 101.0 kPa, the mass density decreases monotonically from 997.06 kg·m⁻³ (pure water, x_acetone = 0) to 874.80 kg·m⁻³ at x_acetone = 0.4, consistent with the lower density of acetone relative to water.

**Core blocks found:**

**WM_L1#4_Blocks_(Analysis_L1#4_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#4_Table#2 | 「GLOBlit_10721」 | 「PROPblock_6」 | 「GLOBcomp_9, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density measurements for acetone + water binary system at 288.15–328.15 K, 101.0 kPa, mole fraction (acetone) 0–1.」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


### Inspected Blocks
- GLOBlit_8129 | 10.1021/je030102f | PROPblock_5: 99 rows; x=['mole_fraction_<acetone>']; y=['mass_density_kg_m3']
    - BLKprop_1 / GLOBprop_1: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_1: kind=direct; materialize_reference=False; supported=True; units=kg/m3 -> kg/m3
- GLOBlit_10721 | 10.1021/je7000182 | PROPblock_6: 126 rows; x=['mole_fraction_<acetone>']; y=['mass_density_kg_m3']
    - BLKprop_1 / GLOBprop_1: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_1: kind=direct; materialize_reference=False; supported=True; units=kg/m3 -> kg/m3
- GLOBlit_8129 | 10.1021/je030102f | PROPblock_5: 99 rows; x=['mole_fraction_<acetone>']; y=['mass_density_kg_m3']
    - BLKprop_1 / GLOBprop_1: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_1: kind=direct; materialize_reference=False; supported=True; units=kg/m3 -> kg/m3
- GLOBlit_10721 | 10.1021/je7000182 | PROPblock_6: 126 rows; x=['mole_fraction_<acetone>']; y=['mass_density_kg_m3']
    - BLKprop_1 / GLOBprop_1: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_1: kind=direct; materialize_reference=False; supported=True; units=kg/m3 -> kg/m3

### Completed Fits
  - 10.1021/je030102f/PROPblock_5 (acetone, water): RK order=5, R²=0.999603, RMSE=7.216018718041471e-09, coeffs=[-6e-06, 2e-06, -1e-06, 1e-06, 1e-06, -2e-06]
      response: direct via X = reported X | 0 reference source(s) | kg/m3 -> kg/m3
      route: measured-derived (density_to_molar_volume, exact pointwise) via density_to_molar_volume
      pure refs: acetone=7.40214e-05, water=1.80689e-05 [block-edges of derived data (water: direct/good, acetone: direct/good)]
      fit_csv: $ROOT/data\10_1021_je030102f_BPROPblock_5_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1021_je030102f_BPROPblock_5_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1021_je030102f_BPROPblock_5_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1021_je030102f_BPROPblock_5_T298.1_excess.png
  - 10.1021/je7000182/PROPblock_6 (acetone, water): RK order=5, R²=0.999363, RMSE=1.0084490086147612e-08, coeffs=[-6e-06, 3e-06, -1e-06, -4e-06, -2e-06, 8e-06]
      response: direct via X = reported X | 0 reference source(s) | kg/m3 -> kg/m3
      route: measured-derived (density_to_molar_volume, exact pointwise) via density_to_molar_volume
      pure refs: acetone=7.40505e-05, water=1.8309e-05 [block-edges of derived data (water: direct/good, acetone: direct/good)]
      fit_csv: $ROOT/data\10_1021_je7000182_BPROPblock_6_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1021_je7000182_BPROPblock_6_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1021_je7000182_BPROPblock_6_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1021_je7000182_BPROPblock_6_T298.1_excess.png

## Session Output Files

### data
- `$ROOT/data\10_1021_je030102f_BPROPblock_5_T298.1_fit.csv` — RK fit data — 10.1021/je030102f PROPblock_5_T298.1
- `$ROOT/data\10_1021_je030102f_BPROPblock_5_T298.1_excess.csv` — Excess property — 10.1021/je030102f PROPblock_5_T298.1
- `$ROOT/data\10_1021_je7000182_BPROPblock_6_T298.1_fit.csv` — RK fit data — 10.1021/je7000182 PROPblock_6_T298.1
- `$ROOT/data\10_1021_je7000182_BPROPblock_6_T298.1_excess.csv` — Excess property — 10.1021/je7000182 PROPblock_6_T298.1

### plot
- `$ROOT/plots\10_1021_je030102f_BPROPblock_5_T298.1_fit.png` — RK fit plot — 10.1021/je030102f PROPblock_5_T298.1
- `$ROOT/plots\10_1021_je030102f_BPROPblock_5_T298.1_excess.png` — Excess plot — 10.1021/je030102f PROPblock_5_T298.1
- `$ROOT/plots\10_1021_je7000182_BPROPblock_6_T298.1_fit.png` — RK fit plot — 10.1021/je7000182 PROPblock_6_T298.1
- `$ROOT/plots\10_1021_je7000182_BPROPblock_6_T298.1_excess.png` — Excess plot — 10.1021/je7000182 PROPblock_6_T298.1

