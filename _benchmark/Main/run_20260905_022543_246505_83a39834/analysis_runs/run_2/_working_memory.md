# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_022543_246505_83a39834\analysis_runs\run_2`

### ID Catalog
| type | global_id | name | pure_values |
|------|--------|------|-------------|
| comp | GLOBcomp_4 | methanol | 4.070376e-05 |
| comp | GLOBcomp_1 | water | 1.8068301e-05 |
| prop | GLOBprop_1 | massdensitykgm3 |  |
| var | GLOBvar_1 | temperaturek |  |
| var | GLOBvar_2 | molefraction<water> |  |
| constr | GLOBconstr_1 | pressurekpa |  |

### History
- [query_thermoml]
- [inspect_block]
- [fit_block_derived] ERROR: Requested x column 'Mole fraction of water' not found
- [fit_block_derived]
- [list_session_files]

### Query Results
#### query
**L1_query_1** — status: success · validation: PASS

**Summary:** Nine mass-density data blocks were found for the methanol (GLOBcomp_4) + water (GLOBcomp_1) binary system in the 295–302 K window. The best block for Redlich-Kister fitting of excess molar volume at 25 °C is GLOBlit_2825 / PROPblock_10 (DOI: 10.1016/j.jct.2007.05.004), which provides 13 density points at exactly 298.15 K and 101.0 kPa spanning the full mole-fraction range x(water) = 0 to 1, including pure-component endpoints (ρ_methanol = 787.2 kg·m⁻³; ρ_water = 997.05 kg·m⁻³). Twelve of the 13 points were tabulated with x(water) values of 0, 0.049, 0.0993, 0.1973, 0.2983, 0.3985, 0.5003, 0.5994, 0.7986, 0.8999, 0.9512, and 1, plus one additional composition near x(water) ≈ 0.6997. The second-best block is GLOBlit_8424 / PROPblock_3 (DOI: 10.1021/je049691v), offering 12 evenly spaced points at 298.15 K from x(water) = 0.08 to 0.9603 but lacking pure-component endpoints. Other blocks from GLOBlit_2432, GLOBlit_7085, GLOBlit_8254, GLOBlit_8869, and GLOBlit_10866 were identified but are less suitable due to high-pressure conditions, narrow composition ranges, or different temperature ranges. The methanol + water system exhibits negative excess molar volume (volume contraction on mixing) consistent with strong hydrogen-bonding interactions.

**Answer:**

#### Density Data for Methanol + Water Binary at ~298.15 K

Nine mass density (GLOBprop_1) data blocks were found for the methanol (GLOBcomp_4) + water (GLOBcomp_1) binary system in the 295–302 K temperature window. The two most suitable blocks for Redlich-Kister fitting of excess molar volume at 25 °C are detailed below.

---

##### Best Block: GLOBlit_2825 / PROPblock_10
**DOI:** 10.1016/j.jct.2007.05.004  
**Full composition range** x(water) = 0 to 1 | **13 points at 298.15 K** | P = 101.0 kPa (fixed)  
Full block: 39 points, T = 293.15–303.15 K

**WM_L1#1_Table#1_(Analysis_L1#1_Answer):**

| *row_id* | *BLKpoint_id* | *T (K)* | *x(water)* | *ρ (kg·m⁻³)* |
|---|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「BLKpoint_14」 | 「298.15」 | 「0」 | 「787.2」 |
| WM_L1#1_Table#1_Row#2 | 「BLKpoint_15」 | 「298.15」 | 「0.049」 | 「795.47」 |
| WM_L1#1_Table#1_Row#3 | 「BLKpoint_16」 | 「298.15」 | 「0.0993」 | 「804.11」 |
| WM_L1#1_Table#1_Row#4 | 「BLKpoint_17」 | 「298.15」 | 「0.1973」 | 「821.73」 |
| WM_L1#1_Table#1_Row#5 | 「BLKpoint_18」 | 「298.15」 | 「0.2983」 | 「840.79」 |
| WM_L1#1_Table#1_Row#6 | 「BLKpoint_19」 | 「298.15」 | 「0.3985」 | 「860.59」 |
| WM_L1#1_Table#1_Row#7 | 「BLKpoint_20」 | 「298.15」 | 「0.5003」 | 「881.69」 |
| WM_L1#1_Table#1_Row#8 | 「BLKpoint_21」 | 「298.15」 | 「0.5994」 | 「902.96」 |
| WM_L1#1_Table#1_Row#9 | 「BLKpoint_23」 | 「298.15」 | 「0.7986」 | 「947.17」 |
| WM_L1#1_Table#1_Row#10 | 「BLKpoint_24」 | 「298.15」 | 「0.8999」 | 「969.84」 |
| WM_L1#1_Table#1_Row#11 | 「BLKpoint_25」 | 「298.15」 | 「0.9512」 | 「982.53」 |
| WM_L1#1_Table#1_Row#12 | 「BLKpoint_26」 | 「298.15」 | 「1」 | 「997.05」 |

*(12 of 13 matched rows shown by RDP shape-preserving selection; one row near x(water) ≈ 0.6997 at 298.15 K was omitted by the display algorithm — the block contains a composition at 0.6997 as confirmed by nearest-value inspection.)*

This block is ideal for Redlich-Kister fitting because it includes both pure-component endpoints (x = 0 and x = 1), enabling direct calculation of V^E without external reference densities.

---

##### Second-Best Block: GLOBlit_8424 / PROPblock_3
**DOI:** 10.1021/je049691v  
**Composition range** x(water) = 0.08 to 0.9603 | **12 points at 298.15 K** | No explicit pressure constraint  
Full block: 180 points, T = 283.15–353.15 K

**WM_L1#1_Table#2_(Analysis_L1#1_Answer):**

| *row_id* | *BLKpoint_id* | *T (K)* | *x(water)* | *ρ (kg·m⁻³)* |
|---|---|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「BLKpoint_37」 | 「298.15」 | 「0.08」 | 「800.1」 |
| WM_L1#1_Table#2_Row#2 | 「BLKpoint_38」 | 「298.15」 | 「0.1581」 | 「813.88」 |
| WM_L1#1_Table#2_Row#3 | 「BLKpoint_39」 | 「298.15」 | 「0.2401」 | 「829.11」 |
| WM_L1#1_Table#2_Row#4 | 「BLKpoint_40」 | 「298.15」 | 「0.3206」 | 「844.62」 |
| WM_L1#1_Table#2_Row#5 | 「BLKpoint_41」 | 「298.15」 | 「0.3987」 | 「860.25」 |
| WM_L1#1_Table#2_Row#6 | 「BLKpoint_42」 | 「298.15」 | 「0.4799」 | 「876.94」 |
| WM_L1#1_Table#2_Row#7 | 「BLKpoint_43」 | 「298.15」 | 「0.56」 | 「894.14」 |
| WM_L1#1_Table#2_Row#8 | 「BLKpoint_44」 | 「298.15」 | 「0.6407」 | 「911.85」 |
| WM_L1#1_Table#2_Row#9 | 「BLKpoint_45」 | 「298.15」 | 「0.7201」 | 「929.54」 |
| WM_L1#1_Table#2_Row#10 | 「BLKpoint_46」 | 「298.15」 | 「0.8」 | 「947.37」 |
| WM_L1#1_Table#2_Row#11 | 「BLKpoint_47」 | 「298.15」 | 「0.8801」 | 「965.23」 |
| WM_L1#1_Table#2_Row#12 | 「BLKpoint_48」 | 「298.15」 | 「0.9603」 | 「985.01」 |

This block has evenly spaced compositions (~Δx ≈ 0.08) but lacks the pure-component endpoints, so external ρ* values for pure methanol and pure water would be needed to compute V^E.

---

##### Other Available Blocks (from search summary — not individually inspected)

The following blocks were also identified by the search but are less suitable for full-range Redlich-Kister fitting. Specific numerical details for these blocks were not individually inspected and are therefore omitted:

- **GLOBlit_2432 / PROPblock_1** (DOI: 10.1016/j.jct.2004.07.019) — High-pressure data with density reported as a deviation; not atmospheric-pressure conditions.
- **GLOBlit_7085 / PROPblock_6** (DOI: 10.1021/acs.jced.6b01058) — Narrow composition range in mass fraction of methanol.
- **GLOBlit_8254 / PROPblock_4** (DOI: 10.1021/je034101z) — High-temperature, high-pressure data at a single composition; not suitable for isothermal V^E fitting near room temperature.
- Additional blocks from GLOBlit_8869 (DOI: 10.1021/je0600810) and GLOBlit_10866 (DOI: 10.1021/je700300y) were also found but offer narrower composition coverage or different temperature ranges.

---

##### Recommendation for Redlich-Kister Fitting

**GLOBlit_2825 / PROPblock_10** is the strongest candidate: it provides 13 isothermal density points at exactly 298.15 K spanning the complete mole fraction range (0 to 1) at atmospheric pressure. The pure-component densities (ρ_methanol = 787.2 kg·m⁻³ at x(water) = 0; ρ_water = 997.05 kg·m⁻³ at x(water) = 1) are included, allowing direct computation of excess molar volume V^E = V_mix − Σ x_i V_i* at each composition without external data. The methanol + water system is well known to exhibit negative V^E (volume contraction on mixing), with a minimum in the water-rich region — consistent with strong hydrogen-bonding interactions between methanol and water.

**Core claims:**
- Nine mass density data blocks were identified for the methanol + water binary system in the 295–302 K temperature window from the ThermoML database.
- The best block for Redlich-Kister fitting of excess molar volume at 25 °C is GLOBlit_2825 / PROPblock_10 (DOI: 10.1016/j.jct.2007.05.004), which provides 13 isothermal density points at exactly 298.15 K spanning the complete mole fraction range x(water) = 0 to 1 at P = 101.0 kPa, including pure-component endpoints (ρ_methanol = 787.2 kg·m⁻³ at x(water) = 0; ρ_water = 997.05 kg·m⁻³ at x(water) = 1).
- The second-best block is GLOBlit_8424 / PROPblock_3 (DOI: 10.1021/je049691v), which provides 12 density points at 298.15 K with evenly spaced compositions (~Δx ≈ 0.08) from x(water) = 0.08 to 0.9603, but lacks pure-component endpoints, requiring external reference densities to compute excess molar volume.
- The inclusion of both pure-component endpoints in the best block enables direct calculation of V^E = V_mix − Σ x_i V_i* at each composition without external data.
- Other identified blocks are less suitable for full-range isothermal Redlich-Kister fitting due to high-pressure conditions, narrow composition ranges, or different temperature ranges; their specific numerical details were not individually inspected.

**Core blocks found:**

**WM_L1#1_Blocks_(Analysis_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#3 | 「GLOBlit_2825」 | 「PROPblock_10」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of methanol + water at 293.15–303.15 K and 101.0 kPa; 13 points at 298.15 K spanning full mole fraction range (0 to 1).」 |
| WM_L1#1_Table#4 | 「GLOBlit_8424」 | 「PROPblock_3」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of methanol + water at 283.15–353.15 K; 12 points at 298.15 K with x(water) = 0.08 to 0.9603.」 |

*Not stored here: 3 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

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

