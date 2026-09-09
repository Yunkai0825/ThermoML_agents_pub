# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_023326_012061_3dba9dd4\analysis_runs\run_5`

### ID Catalog
| type | global_id | name | pure_values |
|------|--------|------|-------------|
| comp | GLOBcomp_1 | water | 1.8065584e-05 |
| comp | GLOBcomp_5 | propan-1-ol | 7.5157579e-05 |
| prop | GLOBprop_28 | excess molar volume, m3/mol |  |
| prop | GLOBprop_1 | massdensitykgm3 |  |
| var | GLOBvar_2 | molefraction<propan-1-ol> |  |
| constr | GLOBconstr_1 | pressurekpa |  |
| constr | GLOBconstr_2 | temperaturek |  |

### History
- [query_thermoml_parallel]
- [query_thermoml]
- [inspect_block]
- [fit_block_derived]
- [predict_from_rk]
- [list_session_files]

### Query Results
#### VE_direct
**L1_query_1** — status: no_results · validation: PASS

**Summary:** Excess molar volume (V^E, property ID GLOBprop_28, m³/mol) for the binary system water (CAS 7732-18-5) + 1-propanol (CAS 71-23-8) at 298.15 K was not found in the ThermoML database. No blocks containing excess molar volume exist for this system at any temperature. The system does have data for other properties across 50 blocks and 18 DOIs, covering 14 properties including mass density (GLOBprop_1, 12 blocks), viscosity (GLOBprop_4), activity coefficients (GLOBprop_3), and VLE compositions (GLOBprop_2). Mass density data is available (e.g., DOI: 10.1016/j.jct.2004.07.019; DOI: 10.1016/j.fluid.2015.07.012; DOI: 10.1016/j.jct.2013.11.036) from which V^E could in principle be calculated, but no pre-computed V^E values are stored.

**Answer:**

**Excess molar volume (V^E) data for water + 1-propanol at 298.15 K: Not found in the ThermoML database.**

A thorough search was conducted for excess molar volume (GLOBprop_28, m³/mol) data for the binary system water (GLOBcomp_1, CAS 7732-18-5) + 1-propanol (GLOBcomp_5, CAS 71-23-8):

- **No blocks were found** containing excess molar volume for this binary system at any temperature, using both declared and subsystem scopes.
- The property ID GLOBprop_28 ("Excess molar volume, m³/mol") was confirmed as the correct and only matching property identifier.
- The water + 1-propanol binary system **does have data** in the database for other properties — 50 blocks were found spanning 14 properties including mass density (GLOBprop_1, 12 blocks), viscosity (GLOBprop_4), activity coefficients (GLOBprop_3), and VLE compositions (GLOBprop_2), among others, across 18 DOIs.

**Note:** While excess molar volume data is not directly available, mass density data for this binary system is present (e.g., in GLOBlit_2432, DOI: 10.1016/j.jct.2004.07.019; GLOBlit_1742, DOI: 10.1016/j.fluid.2015.07.012; GLOBlit_4068, DOI: 10.1016/j.jct.2013.11.036). In principle, excess molar volumes could be calculated from density data if pure-component densities are also available, but no pre-computed V^E values are stored in the database for this system.

**Core claims:**
- No excess molar volume (V^E) data for the water + 1-propanol binary system were found in the ThermoML database at any temperature.
- The water + 1-propanol system does have data in the database for other properties, including mass density (12 blocks), viscosity, activity coefficients, and VLE compositions, spanning 18 DOIs.
- Mass density data for this binary system are available and could in principle be used to calculate excess molar volumes, but no pre-computed V^E values are stored.

*Not stored here: 3 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### density_data
**L1_query_2** — status: success · validation: PASS

**Summary:** Density data for the binary water + 1-propanol system near 298.15 K were found across 17 data blocks. The most directly useful block (GLOBlit_2979, PROPblock_9; DOI 10.1016/j.jct.2008.07.005) provides absolute mass density vs. mole fraction at 298.15 K and 98.93 kPa over x(propan-1-ol) = 0–0.2, with 14 data points ranging from 997.04 kg/m³ (x = 0) to 916.46 kg/m³ (x = 0.2). A second block (GLOBlit_555, PROPblock_8; DOI 10.1016/j.fluid.2007.07.066) gives density at 298.15 K and 101.0 kPa for three mass fractions (w = 0.05, 0.1, 0.15) with values 989.431, 983.475, and 978.117 kg/m³. A third block (GLOBlit_2432, PROPblock_3; DOI 10.1016/j.jct.2004.07.019) reports negative values (−1.0456 to −7.1764 kg/m³ at 298.15 K, 420 kPa) that likely represent density differences relative to pure water rather than absolute densities. For excess molar volume derivation, PROPblock_9 is most suitable on the water-rich side; full-range coverage (x = 0 to 1) and pure 1-propanol density would require inspection of additional blocks among the 17 found.

**Answer:**

**Density data for the binary water + 1-propanol system near 298.15 K**

A search for mass density (GLOBprop_1) of the binary system water (GLOBcomp_1) + 1-propanol (GLOBcomp_5) near 298.15 K returned **17 data blocks** across multiple literature sources. Below are three representative inspected blocks:

---

##### Block 1 — Mole fraction basis (most directly useful for V^E)

**DOI:** 10.1016/j.jct.2008.07.005 | **GLOBlit_2979 :: PROPblock_9**
- Full block: T = 283.15–308.15 K, x(propan-1-ol) = 0–0.2, p = 98.93 kPa, 96 data points
- At 298.15 K (16 points):

**WM_L1#2_Table#1_(Analysis_L1#2_Answer):**

| *row_id* | *x(propan-1-ol)* | *ρ (kg/m³)* |
|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「0」 | 「997.04」 |
| WM_L1#2_Table#1_Row#2 | 「0.002」 | 「995.4」 |
| WM_L1#2_Table#1_Row#3 | 「0.009」 | 「991.66」 |
| WM_L1#2_Table#1_Row#4 | 「0.02」 | 「986.54」 |
| WM_L1#2_Table#1_Row#5 | 「0.03」 | 「982.56」 |
| WM_L1#2_Table#1_Row#6 | 「0.05」 | 「975.49」 |
| WM_L1#2_Table#1_Row#7 | 「0.065」 | 「969.94」 |
| WM_L1#2_Table#1_Row#8 | 「0.08」 | 「963.72」 |
| WM_L1#2_Table#1_Row#9 | 「0.1」 | 「954.91」 |
| WM_L1#2_Table#1_Row#10 | 「0.13」 | 「941.96」 |
| WM_L1#2_Table#1_Row#11 | 「0.15」 | 「934.12」 |
| WM_L1#2_Table#1_Row#12 | 「0.17」 | 「926.68」 |
| WM_L1#2_Table#1_Row#13 | 「0.1856」 | 「921.23」 |
| WM_L1#2_Table#1_Row#14 | 「0.2」 | 「916.46」 |

This block covers the water-rich side (x = 0 to 0.2) and is directly suitable for V^E calculation in that range, using V^E = (x₁M₁ + x₂M₂)/ρ_mix − x₁M₁/ρ₁ − x₂M₂/ρ₂.

---

##### Block 2 — Mass fraction basis (narrow range)

**DOI:** 10.1016/j.fluid.2007.07.066 | **GLOBlit_555 :: PROPblock_8**
- Full block: T = 283.15–303.15 K, w(propan-1-ol) = 0.05–0.15, p = 101.0 kPa, 15 data points
- At 298.15 K (3 points):

**WM_L1#2_Table#2_(Analysis_L1#2_Answer):**

| *row_id* | *w(propan-1-ol)* | *ρ (kg/m³)* |
|---|---|---|
| WM_L1#2_Table#2_Row#1 | 「0.05」 | 「989.431」 |
| WM_L1#2_Table#2_Row#2 | 「0.1」 | 「983.475」 |
| WM_L1#2_Table#2_Row#3 | 「0.15」 | 「978.117」 |

Covers a narrow water-rich composition window in mass fraction; convertible to mole fraction for V^E derivation.

---

##### Block 3 — Apparent/excess quantity (not absolute density)

**DOI:** 10.1016/j.jct.2004.07.019 | **GLOBlit_2432 :: PROPblock_3**
- Full block: T = 298.15–573.15 K, b(propan-1-ol) = 0.0943–0.84695 mol/kg, p = 420–30310 kPa, 456 data points
- At 298.15 K, p = 420 kPa (5 points shown):

**WM_L1#2_Table#3_(Analysis_L1#2_Answer):**

| *row_id* | *b(propan-1-ol) (mol/kg)* | *"mass_density" (kg/m³)* |
|---|---|---|
| WM_L1#2_Table#3_Row#1 | 「0.10076」 | 「−1.0456」 |
| WM_L1#2_Table#3_Row#2 | 「0.21222」 | 「−2.149」 |
| WM_L1#2_Table#3_Row#3 | 「0.35404」 | 「−3.4984」 |
| WM_L1#2_Table#3_Row#4 | 「0.53097」 | 「−5.0885」 |
| WM_L1#2_Table#3_Row#5 | 「0.77737」 | 「−7.1764」 |

**Caution:** The negative values (full block range: −20.1904 to −1.0433) indicate this block likely records a **density difference** (Δρ relative to pure water) or an apparent/excess quantity rather than absolute mass density. This should be verified before using for V^E derivation.

---

**Summary for V^E derivation:**
- **PROPblock_9** (GLOBlit_2979) is the most directly useful block, providing absolute density vs. mole fraction at 298.15 K over x = 0–0.2.
- The remaining blocks among the 17 found may extend the composition range; further inspection of those blocks would be needed for full-range (x = 0 to 1) V^E coverage.
- For V^E calculation, pure-component densities are also needed: the pure water density at 298.15 K is available from PROPblock_9 (ρ = 997.04 kg/m³ at x = 0); pure 1-propanol density would need to be sourced from a unary block or from blocks covering x → 1.

**Core claims:**
- A search for mass density of the binary water + 1-propanol system near 298.15 K returned 17 data blocks across multiple literature sources.
- The most directly useful block for excess molar volume (V^E) derivation is PROPblock_9 (GLOBlit_2979, DOI 10.1016/j.jct.2008.07.005), which provides absolute density vs. mole fraction at 298.15 K over x(propan-1-ol) = 0 to 0.2, with density decreasing from 997.04 kg/m³ at x = 0 to 916.46 kg/m³ at x = 0.2.
- PROPblock_3 (GLOBlit_2432, DOI 10.1016/j.jct.2004.07.019) reports negative 'mass density' values (range −20.1904 to −1.0433 kg/m³), indicating it likely records a density difference relative to pure water or an apparent/excess quantity rather than absolute mass density, and should be verified before use in V^E derivation.
- The inspected blocks cover only the water-rich composition range (x = 0 to 0.2); full-range V^E coverage (x = 0 to 1) would require inspection of additional blocks among the 17 found and a source for pure 1-propanol density at 298.15 K.

**Core blocks found:**

**WM_L1#2_Blocks_(Analysis_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#4 | 「GLOBlit_2979」 | 「PROPblock_9」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density for water + 1-propanol binary system. T = 283.15–308.15 K, x(propan-1-ol) = 0–0.2, p = 98.93 kPa, 96 data points. Most directly useful block for V^E derivation at 298.15 K.」 |
| WM_L1#2_Table#5 | 「GLOBlit_555」 | 「PROPblock_8」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density for water + 1-propanol binary system. T = 283.15–303.15 K, w(propan-1-ol) = 0.05–0.15, p = 101.0 kPa, 15 data points. Narrow water-rich composition window in mass fraction.」 |
| WM_L1#2_Table#6 | 「GLOBlit_2432」 | 「PROPblock_3」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density (likely density difference) for water + 1-propanol binary system. T = 298.15–573.15 K, b(propan-1-ol) = 0.0943–0.84695 mol/kg, p = 420–30310 kPa, 456 data points. Negative values suggest Δρ rather than absolute density.」 |

*Not stored here: 3 verbatim data_inspections table(s); 2 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### query
**L1_query_3** — status: success · validation: PASS

**Summary:** Mass density data for the water + 1-propanol binary system at 298.15 K across the full composition range are best provided by PROPblock_14 (GLOBlit_11042, DOI 10.1021/je700700f). This block contains 13 data points at T = 298.15 K and P = 101.0 kPa, with mole fraction of propan-1-ol ranging from 0 to 1. Density decreases monotonically from 997.2 kg/m³ (pure water, x = 0) to 799.6 kg/m³ (pure propan-1-ol, x = 1), with the steepest decrease on the water-rich side, consistent with non-ideal mixing. In the propanol-rich region (x > 0.6) the density decrease is nearly linear. PROPblock_3 (GLOBlit_11142, DOI 10.1021/je800158z) was considered but has no data at exactly 298.15 K (nearest temperatures 293.15 K and 303.15 K). PROPblock_9 (GLOBlit_2979, DOI 10.1016/j.jct.2008.07.005) only covers x = 0 to 0.2 and cannot provide full-range coverage. PROPblock_14 is recommended for deriving excess molar volume V^E at 298.15 K because it supplies both pure-component endpoints and 11 intermediate compositions spanning the entire mole-fraction range.

**Answer:**

#### Mass Density Data for Water + 1-Propanol Binary System at 298.15 K — Full Composition Range

##### Best Block: PROPblock_14 (GLOBlit_11042)
**DOI:** 10.1021/je700700f  
**System:** propan-1-ol + water (binary)  
**Conditions:** T = 298.15 K, P = 101.0 kPa  
**Composition variable:** mole fraction of propan-1-ol  
**Coverage:** x = 0 to 1 (full range), 13 data points  

All 13 data points at 298.15 K:

**WM_L1#3_Table#1_(Analysis_L1#3_Answer):**

| *row_id* | *BLKpoint_id* | *x(propan-1-ol)* | *ρ (kg/m³)* |
|---|---|---|---|
| WM_L1#3_Table#1_Row#1 | 「BLKpoint_1」 | 「0」 | 「997.2」 |
| WM_L1#3_Table#1_Row#2 | 「BLKpoint_2」 | 「0.0504」 | 「975.1」 |
| WM_L1#3_Table#1_Row#3 | 「BLKpoint_3」 | 「0.0993」 | 「953.3」 |
| WM_L1#3_Table#1_Row#4 | 「BLKpoint_4」 | 「0.1986」 | 「914.9」 |
| WM_L1#3_Table#1_Row#5 | 「BLKpoint_5」 | 「0.2979」 | 「887.2」 |
| WM_L1#3_Table#1_Row#6 | 「BLKpoint_6」 | 「0.3949」 | 「866.9」 |
| WM_L1#3_Table#1_Row#7 | 「BLKpoint_7」 | 「0.4955」 | 「850.3」 |
| WM_L1#3_Table#1_Row#8 | 「BLKpoint_8」 | 「0.5953」 | 「836.9」 |
| WM_L1#3_Table#1_Row#9 | 「BLKpoint_9」 | 「0.6995」 | 「825.6」 |
| WM_L1#3_Table#1_Row#10 | 「BLKpoint_10」 | 「0.7969」 | 「816.3」 |
| WM_L1#3_Table#1_Row#11 | 「BLKpoint_11」 | 「0.8983」 | 「807.7」 |
| WM_L1#3_Table#1_Row#12 | 「BLKpoint_12」 | 「0.9518」 | 「803.5」 |
| WM_L1#3_Table#1_Row#13 | 「BLKpoint_13」 | 「1」 | 「799.6」 |

The density decreases monotonically from 997.2 kg/m³ (pure water) to 799.6 kg/m³ (pure propan-1-ol). The decrease is steepest at low propan-1-ol concentrations (water-rich side), consistent with the known non-ideal mixing behavior of this system. In the propanol-rich region (x > 0.6), the density decrease is nearly linear (R² = 0.9985).

##### Other Block Considered: PROPblock_3 (GLOBlit_11142)
**DOI:** 10.1021/je800158z  
**Coverage:** x = 0 to 1, 56 total points across T = 293.15–323.15 K at P = 81.5 kPa  
**However:** This block has **no data at exactly 298.15 K**. The nearest temperatures are 293.15 K and 303.15 K, so it cannot be used directly for a 298.15 K analysis without interpolation.

##### Previously Found Block: PROPblock_9 (GLOBlit_2979)
**DOI:** 10.1016/j.jct.2008.07.005  
**Coverage:** x = 0 to 0.2, 96 total points across T = 283.15–308.15 K at P = 98.93 kPa  
This block only covers the water-rich region. At 298.15 K, it includes points at x = 0 (ρ = 997.04 kg/m³), x = 0.13 (ρ = 941.96 kg/m³), and x = 0.2 (ρ = 916.46 kg/m³), among others. It does not extend beyond x = 0.2 and therefore cannot provide full-range coverage.

##### Recommendation
**PROPblock_14 (GLOBlit_11042)** is the ideal block for deriving excess molar volume V^E at 298.15 K. It provides both pure-component endpoints (x = 0 and x = 1) needed for V₁* and V₂*, plus 11 intermediate compositions spanning the full range. This is a significant improvement over PROPblock_9 (GLOBlit_2979), which only covers x = 0 to 0.2.

**Core claims:**
- PROPblock_14 (GLOBlit_11042, DOI 10.1021/je700700f) provides mass density data for the water + 1-propanol binary system at 298.15 K and 101.0 kPa over the full composition range (mole fraction of propan-1-ol from 0 to 1), comprising 13 data points.
- The density decreases monotonically from 997.2 kg/m³ (pure water, x = 0) to 799.6 kg/m³ (pure propan-1-ol, x = 1), with the steepest decrease on the water-rich side, consistent with known non-ideal mixing behavior.
- PROPblock_3 (GLOBlit_11142, DOI 10.1021/je800158z) covers x = 0 to 1 but has no data at exactly 298.15 K (nearest temperatures are 293.15 K and 303.15 K), so it cannot be used directly without interpolation.
- PROPblock_9 (GLOBlit_2979, DOI 10.1016/j.jct.2008.07.005) includes data at 298.15 K but only covers the water-rich region (x = 0 to 0.2) and cannot provide full-range coverage.
- PROPblock_14 is recommended as the ideal block for deriving excess molar volume V^E at 298.15 K because it provides both pure-component endpoints and 11 intermediate compositions spanning the full range.

**Core blocks found:**

**WM_L1#3_Blocks_(Analysis_L1#3_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#3_Table#2 | 「GLOBlit_11042」 | 「PROPblock_14」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density for water + propan-1-ol at 298.15 K, full mole fraction range x=0 to 1, 13 data points, P=101.0 kPa.」 |
| WM_L1#3_Table#3 | 「GLOBlit_11142」 | 「PROPblock_3」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density for water + propan-1-ol, full mole fraction range x=0 to 1, 56 points across T=293.15–323.15 K at P=81.5 kPa. No data at exactly 298.15 K.」 |
| WM_L1#3_Table#4 | 「GLOBlit_2979」 | 「PROPblock_9」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density for water + propan-1-ol, x=0 to 0.2 only, 96 points across T=283.15–308.15 K at P=98.93 kPa.」 |

*Not stored here: 5 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


### Inspected Blocks
- GLOBlit_11042 | 10.1021/je700700f | PROPblock_14: 13 rows; x=['mole_fraction_<propan-1-ol>']; y=['mass_density_kg_m3']
    - BLKprop_1 / GLOBprop_1: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_1: kind=direct; materialize_reference=False; supported=True; units=kg/m3 -> kg/m3

### Completed Fits
  - 10.1021/je700700f/PROPblock_14 (propan-1-ol, water): RK order=5, R²=0.999276, RMSE=4.602814010602905e-09, coeffs=[-3e-06, 1e-06, -1e-06, 0.0, -2e-06, 2e-06]
      response: direct via X = reported X | 0 reference source(s) | kg/m3 -> kg/m3
      route: measured-derived (density_to_molar_volume, exact pointwise) via density_to_molar_volume
      pure refs: propan-1-ol=7.51576e-05, water=1.80656e-05 [block-edges of derived data (water: direct/good, propan-1-ol: direct/good)]
      fit_csv: $ROOT/data\10_1021_je700700f_BPROPblock_14_fit.csv
      excess_csv: $ROOT/data\10_1021_je700700f_BPROPblock_14_excess.csv
      fit_plot: $ROOT/plots\10_1021_je700700f_BPROPblock_14_fit.png
      excess_plot: $ROOT/plots\10_1021_je700700f_BPROPblock_14_excess.png

## Session Output Files

### data
- `$ROOT/data\10_1021_je700700f_BPROPblock_14_fit.csv` — RK fit data — 10.1021/je700700f PROPblock_14
- `$ROOT/data\10_1021_je700700f_BPROPblock_14_excess.csv` — Excess property — 10.1021/je700700f PROPblock_14

### plot
- `$ROOT/plots\10_1021_je700700f_BPROPblock_14_fit.png` — RK fit plot — 10.1021/je700700f PROPblock_14
- `$ROOT/plots\10_1021_je700700f_BPROPblock_14_excess.png` — Excess plot — 10.1021/je700700f PROPblock_14

