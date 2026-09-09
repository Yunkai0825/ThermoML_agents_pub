# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_061910_229438_9cbbb4f7`

### ID Catalog
| type | global_id | name | pure_values |
|------|--------|------|-------------|
| comp | GLOBcomp_6 | propan-2-ol | 7.9211262e-05 |
| comp | GLOBcomp_1 | water | 1.8233252e-05 |
| prop | GLOBprop_1 | massdensitykgm3 |  |
| var | GLOBvar_2 | molefraction<propan-2-ol> |  |
| var | GLOBvar_1 | temperaturek |  |
| constr | GLOBconstr_1 | pressurekpa |  |
| lit | GLOBlit_11142 | 10.1021/je800158z |  |

### History
- [query_thermoml]
- [fit_block_derived] ERROR: Requested x column 'Mole fraction of propan-2-ol' not found
- [fit_block_derived]
- [fit_block_derived]
- [fit_block_derived]
- [fit_block_derived]
- [fit_block_derived]
- [predict_from_rk]
- [predict_from_rk]
- [predict_from_rk]
- [predict_from_rk]
- [inspect_block]
- [query_thermoml]

### Query Results
#### query
**L1_query_1** — status: success · validation: PASS

**Summary:** The best density dataset for binary propan-2-ol + water mixtures is GLOBlit_11142 (DOI: 10.1021/je800158z), PROPblock_4, containing 56 data points of mass density (kg/m³) in the liquid phase. It covers the full mole fraction range x(propan-2-ol) = 0 to 1 (14 compositions including 0, 0.0399, 0.1197, 0.2017, 0.28, 0.359, 0.4384, 0.5204, 0.5995, 0.6801, 0.7552, 0.8403, 0.9225, and 1), temperatures 293.15–323.15 K at 10 K intervals, and a fixed pressure of 81.5 kPa. Density ranges from 758.68 to 998.2 kg/m³, decreasing monotonically with increasing propan-2-ol mole fraction and with increasing temperature. Components are propan-2-ol (GLOBcomp_6) and water (GLOBcomp_1). Twelve total binary density blocks were found for this system; other candidates from GLOBlit_11872 (10.1021/je900966r), GLOBlit_7474 (10.1021/acs.jced.8b00160), and GLOBlit_5585 (10.1016/j.jct.2019.105880) were not individually inspected.

**Answer:**

#### Density Data for Binary Propan-2-ol + Water Mixtures

##### Best Dataset: GLOBlit_11142 (DOI: 10.1021/je800158z)

**Block: PROPblock_4** — 56 data points of mass density (kg/m³) for the binary system propan-2-ol (GLOBcomp_6) + water (GLOBcomp_1) in the liquid phase.

- **Composition range:** x(propan-2-ol) = 0 to 1 (the inspected RDP subset shows compositions at 0, 0.0399, 0.1197, 0.2017, 0.28, 0.359, 0.4384, 0.5204, 0.5995, 0.6801, 0.7552, 0.8403, 0.9225, and 1)
- **Temperature range:** 293.15–323.15 K (isotherms at 10 K intervals)
- **Pressure:** 81.5 kPa (fixed constraint)
- **Variables:** mole fraction of propan-2-ol (BLKvar_1 → GLOBvar_2), temperature (BLKvar_2 → GLOBvar_1)
- **Density range:** 758.68–998.2 kg/m³

This is the richest dataset with excellent composition coverage across the full mole fraction range and multiple isotherms. Representative data points (verbatim from inspection):

**WM_L1#1_Table#1_(Analysis_L1#1_Answer):**

| *row_id* | *x(propan-2-ol)* | *T (K)* | *ρ (kg/m³)* |
|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「0」 | 「293.15」 | 「998.2」 |
| WM_L1#1_Table#1_Row#2 | 「0」 | 「323.15」 | 「988.03」 |
| WM_L1#1_Table#1_Row#3 | 「0.2017」 | 「293.15」 | 「916.63」 |
| WM_L1#1_Table#1_Row#4 | 「0.2017」 | 「323.15」 | 「891.98」 |
| WM_L1#1_Table#1_Row#5 | 「0.5204」 | 「293.15」 | 「839.36」 |
| WM_L1#1_Table#1_Row#6 | 「0.5204」 | 「323.15」 | 「812.2」 |
| WM_L1#1_Table#1_Row#7 | 「1」 | 「293.15」 | 「785.1」 |
| WM_L1#1_Table#1_Row#8 | 「1」 | 「323.15」 | 「758.68」 |

The density decreases monotonically with increasing propan-2-ol mole fraction at each temperature, reflecting the lower density of propan-2-ol compared to water. The temperature effect is also systematic: density decreases with increasing temperature at every composition.

##### Other Available Blocks (not individually inspected in this run)

The search found 12 total binary density blocks for this system. Additional candidates identified in the search include:

**WM_L1#1_Table#2_(Analysis_L1#1_Answer):**

| *row_id* | *Literature* | *DOI* | *Notes* |
|---|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「GLOBlit_11872」 | 「10.1021/je900966r」 | 「Multiple temperatures and compositions; not inspected — point count not verified」 |
| WM_L1#1_Table#2_Row#2 | 「GLOBlit_7474」 | 「10.1021/acs.jced.8b00160」 | 「Multiple temperatures and compositions; not inspected — point count not verified」 |
| WM_L1#1_Table#2_Row#3 | 「GLOBlit_5585」 | 「10.1016/j.jct.2019.105880」 | 「Multiple temperatures and compositions; not inspected — point count not verified」 |

The search also identified additional large datasets that appear to be high-pressure studies at fixed composition, making them less suitable for composition-dependent analysis at ambient conditions. These were not individually inspected.

**Recommendation:** GLOBlit_11142, PROPblock_4 provides the best combination of composition coverage (spanning x = 0–1 with 56 data points across multiple compositions) and temperature variation (293.15 to 323.15 K), making it ideal for studying the composition and temperature dependence of density in propan-2-ol + water binary mixtures.

**Core claims:**
- The richest identified density dataset for binary propan-2-ol + water mixtures is GLOBlit_11142 (DOI: 10.1021/je800158z), PROPblock_4, containing 56 data points of liquid-phase mass density spanning x(propan-2-ol) = 0 to 1, temperatures 293.15–323.15 K, and a fixed pressure of 81.5 kPa, with densities ranging from 758.68 to 998.2 kg/m³.
- Within this dataset, density decreases monotonically with increasing propan-2-ol mole fraction at each temperature and decreases with increasing temperature at every composition.
- Twelve total binary density blocks for propan-2-ol + water were found in the search, but only PROPblock_4 of GLOBlit_11142 was fully inspected; the remaining candidates were not individually verified for point count or suitability.

**Core blocks found:**

**WM_L1#1_Blocks_(Analysis_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#3 | 「GLOBlit_11142」 | 「PROPblock_4」 | 「GLOBcomp_6, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density measurements for binary propan-2-ol + water mixtures; 56 data points spanning x(propan-2-ol) = 0 to 1 at temperatures 293.15–323.15 K and 81.5 kPa.」 |

*Not stored here: 2 verbatim data_inspections table(s); 6 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### query
**L1_query_2** — status: success · validation: PASS

**Summary:** In PROPblock_4 from GLOBlit_11142 (DOI 10.1021/je800158z), both 303.15 K and 313.15 K are confirmed as actual data points. At mole fraction 0 (pure water) and a fixed pressure constraint of 81.5 kPa, the mass density is 995.64 kg/m³ at 303.15 K and 992.21 kg/m³ at 313.15 K. The block contains 56 data points total, covering mole fractions 0–1 (propan-2-ol in water), temperatures 293.15–323.15 K, and mass densities spanning 758.68–998.2 kg/m³.

**Answer:**

Inspection of PROPblock_4 from GLOBlit_11142 (DOI 10.1021/je800158z) confirms that both 303.15 K and 313.15 K are actual data points in the block.

**Temperature 303.15 K** — exact match confirmed:

**WM_L1#2_Table#1_(Analysis_L1#2_Answer):**

| *row_id* | *BLKpoint_id* | *mole_fraction (propan-2-ol)* | *temperature_k* | *pressure_kpa* | *mass_density_kg_m3* |
|---|---|---|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「BLKpoint_2」 | 「0」 | 「303.15」 | 「81.5」 | 「995.64」 |

**Temperature 313.15 K** — exact match confirmed:

**WM_L1#2_Table#2_(Analysis_L1#2_Answer):**

| *row_id* | *BLKpoint_id* | *mole_fraction (propan-2-ol)* | *temperature_k* | *pressure_kpa* | *mass_density_kg_m3* |
|---|---|---|---|---|---|
| WM_L1#2_Table#2_Row#1 | 「BLKpoint_3」 | 「0」 | 「313.15」 | 「81.5」 | 「992.21」 |

Both rows shown are at mole fraction 0 (pure water end), with a fixed constraint of pressure = 81.5 kPa. The block contains 56 data points total covering the full composition range (mole fraction 0–1) and temperature range 293.15–323.15 K, with mass density spanning 758.68–998.2 kg/m³.

**Core claims:**
- PROPblock_4 from GLOBlit_11142 (DOI 10.1021/je800158z) contains exact data points at both 303.15 K and 313.15 K, confirmed at mole fraction 0 (pure water) and pressure 81.5 kPa, with mass densities of 995.64 kg/m³ and 992.21 kg/m³ respectively.
- The block contains 56 data points total covering mole fractions 0–1 and temperatures 293.15–323.15 K, with mass density spanning 758.68–998.2 kg/m³.

**Core blocks found:**

**WM_L1#2_Blocks_(Analysis_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#3 | 「GLOBlit_11142」 | 「PROPblock_4」 | 「GLOBcomp_6, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density for propan-2-ol + water at 293.15–323.15 K and 81.5 kPa, covering mole fractions 0–1.」 |

*Not stored here: 2 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


### Inspected Blocks
- GLOBlit_11142 | 10.1021/je800158z | PROPblock_4: 56 rows; x=['mole_fraction_<propan-2-ol>']; y=['mass_density_kg_m3']
    - BLKprop_1 / GLOBprop_1: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_1: kind=direct; materialize_reference=False; supported=True; units=kg/m3 -> kg/m3

### Completed Fits
  - 10.1021/je800158z/PROPblock_4 (propan-2-ol, water): RK order=0, R²=0.093751, RMSE=6.258282381958874e-07, coeffs=[-4e-06]
      response: direct via X = reported X | 0 reference source(s) | kg/m3 -> kg/m3
      route: measured-derived (density_to_molar_volume, exact pointwise) via density_to_molar_volume
      pure refs: propan-2-ol=7.78509e-05, water=1.81328e-05 [block-edges of derived data (water: direct/good, propan-2-ol: direct/good)]
      fit_csv: $ROOT/data\10_1021_je800158z_BPROPblock_4_fit.csv
      excess_csv: $ROOT/data\10_1021_je800158z_BPROPblock_4_excess.csv
      fit_plot: $ROOT/plots\10_1021_je800158z_BPROPblock_4_fit.png
      excess_plot: $ROOT/plots\10_1021_je800158z_BPROPblock_4_excess.png
  - 10.1021/je800158z/PROPblock_4 (propan-2-ol, water): RK order=3, R²=0.997274, RMSE=1.3871206325349461e-08, coeffs=[-4e-06, 2e-06, -2e-06, 1e-06]
      response: direct via X = reported X | 0 reference source(s) | kg/m3 -> kg/m3
      route: measured-derived (density_to_molar_volume, exact pointwise) via density_to_molar_volume
      pure refs: propan-2-ol=7.65457e-05, water=1.80475e-05 [block-edges of derived data (water: direct/good, propan-2-ol: direct/good)]
      fit_csv: $ROOT/data\10_1021_je800158z_BPROPblock_4_T293.1_fit.csv
      excess_csv: $ROOT/data\10_1021_je800158z_BPROPblock_4_T293.1_excess.csv
      fit_plot: $ROOT/plots\10_1021_je800158z_BPROPblock_4_T293.1_fit.png
      excess_plot: $ROOT/plots\10_1021_je800158z_BPROPblock_4_T293.1_excess.png
  - 10.1021/je800158z/PROPblock_4 (propan-2-ol, water): RK order=3, R²=0.998842, RMSE=8.645607260862565e-09, coeffs=[-4e-06, 2e-06, -2e-06, 1e-06]
      response: direct via X = reported X | 0 reference source(s) | kg/m3 -> kg/m3
      route: measured-derived (density_to_molar_volume, exact pointwise) via density_to_molar_volume
      pure refs: propan-2-ol=7.73805e-05, water=1.80939e-05 [block-edges of derived data (water: direct/good, propan-2-ol: direct/good)]
      fit_csv: $ROOT/data\10_1021_je800158z_BPROPblock_4_T303.1_fit.csv
      excess_csv: $ROOT/data\10_1021_je800158z_BPROPblock_4_T303.1_excess.csv
      fit_plot: $ROOT/plots\10_1021_je800158z_BPROPblock_4_T303.1_fit.png
      excess_plot: $ROOT/plots\10_1021_je800158z_BPROPblock_4_T303.1_excess.png
  - 10.1021/je800158z/PROPblock_4 (propan-2-ol, water): RK order=4, R²=0.999452, RMSE=5.761057155851438e-09, coeffs=[-3e-06, 2e-06, -2e-06, 1e-06, -0.0]
      response: direct via X = reported X | 0 reference source(s) | kg/m3 -> kg/m3
      route: measured-derived (density_to_molar_volume, exact pointwise) via density_to_molar_volume
      pure refs: propan-2-ol=7.82663e-05, water=1.81564e-05 [block-edges of derived data (water: direct/good, propan-2-ol: direct/good)]
      fit_csv: $ROOT/data\10_1021_je800158z_BPROPblock_4_T313.1_fit.csv
      excess_csv: $ROOT/data\10_1021_je800158z_BPROPblock_4_T313.1_excess.csv
      fit_plot: $ROOT/plots\10_1021_je800158z_BPROPblock_4_T313.1_fit.png
      excess_plot: $ROOT/plots\10_1021_je800158z_BPROPblock_4_T313.1_excess.png
  - 10.1021/je800158z/PROPblock_4 (propan-2-ol, water): RK order=5, R²=0.999736, RMSE=3.937353814994336e-09, coeffs=[-3e-06, 2e-06, -1e-06, 0.0, -1e-06, 1e-06]
      response: direct via X = reported X | 0 reference source(s) | kg/m3 -> kg/m3
      route: measured-derived (density_to_molar_volume, exact pointwise) via density_to_molar_volume
      pure refs: propan-2-ol=7.92113e-05, water=1.82333e-05 [block-edges of derived data (water: direct/good, propan-2-ol: direct/good)]
      fit_csv: $ROOT/data\10_1021_je800158z_BPROPblock_4_T323.1_fit.csv
      excess_csv: $ROOT/data\10_1021_je800158z_BPROPblock_4_T323.1_excess.csv
      fit_plot: $ROOT/plots\10_1021_je800158z_BPROPblock_4_T323.1_fit.png
      excess_plot: $ROOT/plots\10_1021_je800158z_BPROPblock_4_T323.1_excess.png

## Session Output Files

### data
- `$ROOT/data\10_1021_je800158z_BPROPblock_4_fit.csv` — RK fit data — 10.1021/je800158z PROPblock_4
- `$ROOT/data\10_1021_je800158z_BPROPblock_4_excess.csv` — Excess property — 10.1021/je800158z PROPblock_4
- `$ROOT/data\10_1021_je800158z_BPROPblock_4_T293.1_fit.csv` — RK fit data — 10.1021/je800158z PROPblock_4_T293.1
- `$ROOT/data\10_1021_je800158z_BPROPblock_4_T293.1_excess.csv` — Excess property — 10.1021/je800158z PROPblock_4_T293.1
- `$ROOT/data\10_1021_je800158z_BPROPblock_4_T303.1_fit.csv` — RK fit data — 10.1021/je800158z PROPblock_4_T303.1
- `$ROOT/data\10_1021_je800158z_BPROPblock_4_T303.1_excess.csv` — Excess property — 10.1021/je800158z PROPblock_4_T303.1
- `$ROOT/data\10_1021_je800158z_BPROPblock_4_T313.1_fit.csv` — RK fit data — 10.1021/je800158z PROPblock_4_T313.1
- `$ROOT/data\10_1021_je800158z_BPROPblock_4_T313.1_excess.csv` — Excess property — 10.1021/je800158z PROPblock_4_T313.1
- `$ROOT/data\10_1021_je800158z_BPROPblock_4_T323.1_fit.csv` — RK fit data — 10.1021/je800158z PROPblock_4_T323.1
- `$ROOT/data\10_1021_je800158z_BPROPblock_4_T323.1_excess.csv` — Excess property — 10.1021/je800158z PROPblock_4_T323.1

### plot
- `$ROOT/plots\10_1021_je800158z_BPROPblock_4_fit.png` — RK fit plot — 10.1021/je800158z PROPblock_4
- `$ROOT/plots\10_1021_je800158z_BPROPblock_4_excess.png` — Excess plot — 10.1021/je800158z PROPblock_4
- `$ROOT/plots\10_1021_je800158z_BPROPblock_4_T293.1_fit.png` — RK fit plot — 10.1021/je800158z PROPblock_4_T293.1
- `$ROOT/plots\10_1021_je800158z_BPROPblock_4_T293.1_excess.png` — Excess plot — 10.1021/je800158z PROPblock_4_T293.1
- `$ROOT/plots\10_1021_je800158z_BPROPblock_4_T303.1_fit.png` — RK fit plot — 10.1021/je800158z PROPblock_4_T303.1
- `$ROOT/plots\10_1021_je800158z_BPROPblock_4_T303.1_excess.png` — Excess plot — 10.1021/je800158z PROPblock_4_T303.1
- `$ROOT/plots\10_1021_je800158z_BPROPblock_4_T313.1_fit.png` — RK fit plot — 10.1021/je800158z PROPblock_4_T313.1
- `$ROOT/plots\10_1021_je800158z_BPROPblock_4_T313.1_excess.png` — Excess plot — 10.1021/je800158z PROPblock_4_T313.1
- `$ROOT/plots\10_1021_je800158z_BPROPblock_4_T323.1_fit.png` — RK fit plot — 10.1021/je800158z PROPblock_4_T323.1
- `$ROOT/plots\10_1021_je800158z_BPROPblock_4_T323.1_excess.png` — Excess plot — 10.1021/je800158z PROPblock_4_T323.1

