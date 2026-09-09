# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_060742_675586_997fb6a3`

### History
- [query_thermoml]
- [query_thermoml]
- [query_thermoml]
- [query_thermoml]
- [fit_block_derived]
- [fit_block_derived]
- [fit_block_derived] ERROR: Constraint column 'Temperature, K' not found
- [fit_block_derived]

### Query Results
#### query
**L1_query_1** — status: no_results · validation: PASS

**Summary:** No density data were found for the ternary mixture DMF + water + methanol at 298.15 K in the ThermoML database. A progressively broadened search — ternary density at 298.15 K, ternary density at any temperature, and any ternary property for these three compounds — returned no density results. The only ternary block containing all three compounds (DOI 10.1016/j.tca.2006.02.028) reports molar enthalpy of solution of DMF at infinite dilution in binary methanol–water solvent mixtures at 298.15 K, measured by titration calorimetry. Values range from −2.32 kJ/mol in pure water to 11.95 kJ/mol in pure methanol across 13 data points. No finite-composition ternary mass density or molar volume data exist in ThermoML for this system at any temperature.

**Answer:**

**No density data found for the ternary mixture DMF + water + methanol at 298.15 K in the ThermoML database.**

A comprehensive search was conducted for ternary blocks containing all three compounds — N,N-dimethylformamide (DMF, GLOBcomp_18), water (GLOBcomp_1), and methanol (GLOBcomp_4) — with mass density (GLOBprop_1) as the property. The search was progressively broadened:

1. **Ternary density at 298.15 K** → no results  
2. **Ternary density at any temperature** → no results  
3. **Any ternary property for these three compounds** → one block found, but it is **not** density data

The only ternary block containing all three compounds is:

- **DOI:** 10.1016/j.tca.2006.02.028 (GLOBlit_5688)  
- **Block:** PROPblock_4  
- **Property:** Molar enthalpy of solution (GLOBprop_15), not density  
- **Conditions:** Temperature = 298.15 K, pressure = 1.0 kPa, DMF mole fraction = 0.0 (infinite dilution)  
- **Variable:** Solvent mole fraction of methanol (range 0–1, 13 data points)  
- **Method:** Titration calorimetry  

This block measures the enthalpy of dissolving DMF at infinite dilution in binary methanol–water solvent mixtures. For example, the molar enthalpy of solution ranges from −2.32 kJ/mol in pure water (methanol mole fraction = 0) to 11.95 kJ/mol in pure methanol (methanol mole fraction = 1), showing a monotonically increasing trend. It does not contain finite-composition ternary density data.

**Conclusion:** The ThermoML database does not contain mass density (or molar volume) data for the ternary system DMF + water + methanol at 298.15 K or any other temperature.

**Core claims:**
- A comprehensive search of the ThermoML database found no mass density or molar volume data for the ternary system N,N-dimethylformamide (DMF) + water + methanol at 298.15 K or any other temperature.
- The only ternary block containing all three compounds (DOI 10.1016/j.tca.2006.02.028) reports molar enthalpy of solution of DMF at infinite dilution in binary methanol–water solvent mixtures at 298.15 K, not density data.

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### query
**L1_query_2** — status: success · validation: PASS

**Summary:** Eleven ThermoML binary blocks contain mass density data for DMF (N,N-dimethylformamide) + water near 298.15 K. The recommended full-range dataset is GLOBlit_2834 / PROPblock_18 (DOI 10.1016/j.jct.2007.05.015), which provides 40 data points at T = 298.15 K and p = 101.0 kPa spanning x(DMF) = 0 to 1, with densities from 943.94 to 997.02 kg/m³. The density profile is non-monotonic with a maximum near x(DMF) ≈ 0.12 where the mixture density equals or slightly exceeds that of pure water (~997 kg/m³), before decreasing toward pure DMF (943.94 kg/m³). A second full-range dataset, GLOBlit_4174 / PROPblock_19 (DOI 10.1016/j.jct.2014.05.013), has fewer composition points at 298.15 K but confirms the same trend, with pure-DMF density of 943.89 kg/m³. Additional blocks from sources including GLOBlit_11030 (10.1021/je700671t), GLOBlit_2584 (10.1016/j.jct.2005.07.012), GLOBlit_3614 (10.1016/j.jct.2012.04.007), GLOBlit_1540 (10.1016/j.fluid.2014.08.026), and GLOBlit_4166 (10.1016/j.jct.2014.05.003) were also found but not individually inspected. The non-monotonic behavior reflects strong DMF–water hydrogen-bonding interactions producing volume contraction in the water-rich region.

**Answer:**

#### Binary Density Data: DMF + Water at 298.15 K

**11 binary blocks** were found in ThermoML containing both N,N-dimethylformamide (DMF, GLOBcomp_18) and water (GLOBcomp_1) with mass density (GLOBprop_1) near 298.15 K.

##### Best Full-Range Dataset: GLOBlit_2834 / PROPblock_18

**DOI:** 10.1016/j.jct.2007.05.015  
**40 data points**, all at T = 298.15 K and p = 101.0 kPa, spanning x(DMF) = 0 to 1.  
**Density range (n=40):** 943.94–997.02 kg/m³

Representative inspected rows:

**WM_L1#2_Table#1_(Analysis_L1#2_Answer):**

| *row_id* | *x(DMF)* | *ρ (kg/m³)* |
|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「0」 | 「997.02」 |
| WM_L1#2_Table#1_Row#2 | 「0.01233」 | 「996.44」 |
| WM_L1#2_Table#1_Row#3 | 「0.0266」 | 「996.21」 |
| WM_L1#2_Table#1_Row#4 | 「0.04154」 | 「996.18」 |
| WM_L1#2_Table#1_Row#5 | 「0.11728」 | 「997.02」 |
| WM_L1#2_Table#1_Row#6 | 「0.14116」 | 「996.93」 |
| WM_L1#2_Table#1_Row#7 | 「0.23003」 | 「993.87」 |
| WM_L1#2_Table#1_Row#8 | 「0.28661」 | 「990.18」 |
| WM_L1#2_Table#1_Row#9 | 「0.31385」 | 「989.17」 |
| WM_L1#2_Table#1_Row#10 | 「0.37711」 | 「984.28」 |
| WM_L1#2_Table#1_Row#11 | 「0.92495」 | 「948.01」 |
| WM_L1#2_Table#1_Row#12 | 「0.96614」 | 「946.28」 |
| WM_L1#2_Table#1_Row#13 | 「1」 | 「943.94」 |

The topology is **non-monotonic** (4 extrema), showing a density maximum near x(DMF) ≈ 0.12 where the mixture density equals or slightly exceeds that of pure water (~997 kg/m³), before decreasing toward pure DMF (943.94 kg/m³).

##### Additional Full-Range Dataset: GLOBlit_4174 / PROPblock_19

**DOI:** 10.1016/j.jct.2014.05.013  
**18 total points** across three temperatures (288.15, 298.15, 308.15 K) at p = 100.0 kPa, using mass fraction w(DMF) = 0 to 1.

At 298.15 K specifically (inspected rows):

**WM_L1#2_Table#2_(Analysis_L1#2_Answer):**

| *row_id* | *w(DMF)* | *ρ (kg/m³)* |
|---|---|---|
| WM_L1#2_Table#2_Row#1 | 「0」 | 「997」 |
| WM_L1#2_Table#2_Row#2 | 「0.4」 | 「996.99」 |
| WM_L1#2_Table#2_Row#3 | 「0.6」 | 「992.97」 |
| WM_L1#2_Table#2_Row#4 | 「0.8」 | 「977.38」 |
| WM_L1#2_Table#2_Row#5 | 「1」 | 「943.89」 |

This dataset has fewer composition points at 298.15 K but confirms the same trend.

##### Other Blocks Found (not individually inspected)

The search_blocks tool summary also returned blocks from the following sources, which may contain relevant 298.15 K data. Point counts below are per the search_blocks summary and have not been individually verified by block inspection:

- **GLOBlit_11030** (10.1021/je700671t) — reported as the largest dataset (per search summary)
- **GLOBlit_2584** (10.1016/j.jct.2005.07.012) — multi-temperature block
- **GLOBlit_3614** (10.1016/j.jct.2012.04.007) — narrow water-dilute composition range
- **GLOBlit_1540** (10.1016/j.fluid.2014.08.026) — partial composition range
- **GLOBlit_4166** (10.1016/j.jct.2014.05.003) — partial composition range
- Plus additional blocks (11 total found)

##### Recommendation

**GLOBlit_2834 / PROPblock_18** is the best single block for full-range binary density of DMF + water at 298.15 K: 40 points spanning x(DMF) = 0–1, all at exactly 298.15 K and 101.0 kPa. The non-monotonic density behavior (density maximum near x(DMF) ≈ 0.12) reflects strong DMF–water hydrogen-bonding interactions that produce volume contraction in the water-rich region.

**Core claims:**
- 11 binary ThermoML blocks were found containing mass density data for DMF + water near 298.15 K.
- The best full-range dataset is GLOBlit_2834 / PROPblock_18 (DOI: 10.1016/j.jct.2007.05.015), comprising 40 data points at T = 298.15 K and p = 101.0 kPa, spanning x(DMF) = 0 to 1, with a density range of 943.94–997.02 kg/m³.
- The density–composition relationship is non-monotonic, exhibiting a density maximum near x(DMF) ≈ 0.12 where the mixture density equals or slightly exceeds that of pure water (~997 kg/m³), before decreasing toward pure DMF (943.94 kg/m³).
- The non-monotonic behavior is attributed to strong DMF–water hydrogen-bonding interactions producing volume contraction in the water-rich region.
- A second full-range dataset (GLOBlit_4174 / PROPblock_19, DOI: 10.1016/j.jct.2014.05.013) with fewer composition points at 298.15 K confirms the same overall trend.

**Core blocks found:**

**WM_L1#2_Blocks_(Analysis_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#3 | 「GLOBlit_2834」 | 「PROPblock_18」 | 「GLOBcomp_18, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of DMF + water at 298.15 K and 101.0 kPa; 40 data points spanning x(DMF) = 0–1, density range 943.94–997.02 kg/m³, non-monotonic with maximum near x(DMF) ≈ 0.12.」 |
| WM_L1#2_Table#4 | 「GLOBlit_4174」 | 「PROPblock_19」 | 「GLOBcomp_18, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of DMF + water at multiple temperatures (288.15, 298.15, 308.15 K) and 100.0 kPa; 18 total points using mass fraction w(DMF) = 0–1.」 |

*Not stored here: 2 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### query
**L1_query_3** — status: success · validation: PASS

**Summary:** Binary liquid density data for dimethylformamide (DMF) + methanol at 298.15 K and 101.0 kPa, from DOI 10.1016/j.jct.2014.02.021. The dataset contains 26 points spanning the full composition range x(DMF) = 0–1. Density increases monotonically from 786.58 kg/m³ (pure methanol) to 943.974 kg/m³ (pure DMF). Nine representative points are given: x(DMF) = 0, ρ = 786.58; x = 0.1988, ρ = 843.761; x = 0.2004, ρ = 843.0; x = 0.4022, ρ = 882.138; x = 0.4054, ρ = 881.38; x = 0.5982, ρ = 909.277; x = 0.6008, ρ = 908.588; x = 0.9033, ρ = 936.655; x = 1.0, ρ = 943.974 (all ρ in kg·m⁻³). Near-duplicate compositions (e.g., x ≈ 0.20, 0.40, 0.60) from replicate measurements show differences < 1 kg/m³, indicating good reproducibility. A second data block from a different literature source covering multiple temperatures was noted but not inspected.

**Answer:**

#### Binary Density Data: DMF + Methanol at 298.15 K

**Source:** DOI 10.1016/j.jct.2014.02.021 (GLOBlit_4125), PROPblock_6  
**System:** Binary — methanol (GLOBcomp_4) + dimethylformamide (GLOBcomp_18)  
**Conditions:** T = 298.15 K (fixed), P = 101.0 kPa (fixed), liquid phase  
**Total data points:** 26 across the full composition range x(DMF) = 0–1

##### Representative Data Points (9 of 26, shape-preserving RDP subset)

**WM_L1#3_Table#1_(Analysis_L1#3_Answer):**

| *row_id* | *x(DMF)* | *ρ / kg·m⁻³* |
|---|---|---|
| WM_L1#3_Table#1_Row#1 | 「0」 | 「786.58」 |
| WM_L1#3_Table#1_Row#2 | 「0.1988」 | 「843.761」 |
| WM_L1#3_Table#1_Row#3 | 「0.2004」 | 「843.0」 |
| WM_L1#3_Table#1_Row#4 | 「0.4022」 | 「882.138」 |
| WM_L1#3_Table#1_Row#5 | 「0.4054」 | 「881.38」 |
| WM_L1#3_Table#1_Row#6 | 「0.5982」 | 「909.277」 |
| WM_L1#3_Table#1_Row#7 | 「0.6008」 | 「908.588」 |
| WM_L1#3_Table#1_Row#8 | 「0.9033」 | 「936.655」 |
| WM_L1#3_Table#1_Row#9 | 「1.0」 | 「943.974」 |

**Statistics (full 26-point block):**  
- x(DMF): 0–1  
- ρ: 786.58–943.974 kg/m³

**Chemistry insight:** The density increases monotonically from pure methanol (786.58 kg/m³) to pure DMF (943.974 kg/m³) at 298.15 K. The block includes duplicate/near-duplicate compositions (e.g., x ≈ 0.20, x ≈ 0.40, x ≈ 0.60), likely from replicate measurements, showing good reproducibility (differences < 1 kg/m³). The full block contains 26 points providing dense coverage of the composition range.

A second block (PROPblock_8, GLOBlit_10930) also contains DMF + methanol density data over multiple temperatures, if additional data are needed (not inspected in this run).

**Core claims:**
- For the binary system dimethylformamide (DMF) + methanol at 298.15 K and 101.0 kPa (liquid phase), 26 density data points spanning the full composition range x(DMF) = 0–1 are available from DOI 10.1016/j.jct.2014.02.021.
- The density increases monotonically from pure methanol (786.58 kg·m⁻³) to pure DMF (943.974 kg·m⁻³) at 298.15 K.
- Near-duplicate compositions (e.g., x(DMF) ≈ 0.20, ≈ 0.40, ≈ 0.60) from replicate measurements show good reproducibility, with density differences less than 1 kg·m⁻³.

**Core blocks found:**

**WM_L1#3_Blocks_(Analysis_L1#3_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#3_Table#2 | 「GLOBlit_4125」 | 「PROPblock_6」 | 「GLOBcomp_4, GLOBcomp_18」 | 「GLOBprop_1」 | 「Mass density measurements for methanol + dimethylformamide at 298.15 K and 101.0 kPa across the full composition range (26 data points, x(DMF) = 0–1).」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### query
**L1_query_4** — status: success · validation: PASS

**Summary:** Binary density data for water (GLOBcomp_1) + methanol (GLOBcomp_4) at 298.15 K and 101 kPa were found in GLOBlit_2825 (DOI 10.1016/j.jct.2007.05.004, PROPblock_10). The dataset contains 13 liquid-phase mass density (GLOBprop_1) points spanning the full water mole fraction range: 0 (787.2 kg/m³) to 1 (997.05 kg/m³). Representative values include x(water) = 0.2983 / 840.79 kg/m³, 0.5003 / 881.69 kg/m³, and 0.7986 / 947.17 kg/m³. Density increases monotonically but slightly nonlinearly with water content, consistent with the known positive excess volume of the water–methanol system. Additional overlapping datasets at 298.15 K exist in GLOBlit_8424 (DOI 10.1021/je049691v, PROPblock_3) and GLOBlit_10866 (DOI 10.1021/je700300y, PROPblock_6) but were not inspected.

**Answer:**

#### Binary Density Data: Water + Methanol at 298.15 K

A full-composition-range dataset for the binary system **water (GLOBcomp_1) + methanol (GLOBcomp_4)** with **mass density (GLOBprop_1)** at **298.15 K** and **101 kPa** was found in:

**Source:** DOI 10.1016/j.jct.2007.05.004 (GLOBlit_2825, PROPblock_10)

The block contains 13 data points at exactly 298.15 K spanning the full mole fraction range of water from 0 (pure methanol) to 1 (pure water). Here are 12 representative points (RDP-simplified from 13):

**WM_L1#4_Table#1_(Analysis_L1#4_Answer):**

| *row_id* | *Mole fraction of water* | *Mass density (kg/m³)* |
|---|---|---|
| WM_L1#4_Table#1_Row#1 | 「0」 | 「787.2」 |
| WM_L1#4_Table#1_Row#2 | 「0.049」 | 「795.47」 |
| WM_L1#4_Table#1_Row#3 | 「0.0993」 | 「804.11」 |
| WM_L1#4_Table#1_Row#4 | 「0.1973」 | 「821.73」 |
| WM_L1#4_Table#1_Row#5 | 「0.2983」 | 「840.79」 |
| WM_L1#4_Table#1_Row#6 | 「0.3985」 | 「860.59」 |
| WM_L1#4_Table#1_Row#7 | 「0.5003」 | 「881.69」 |
| WM_L1#4_Table#1_Row#8 | 「0.5994」 | 「902.96」 |
| WM_L1#4_Table#1_Row#9 | 「0.7986」 | 「947.17」 |
| WM_L1#4_Table#1_Row#10 | 「0.8999」 | 「969.84」 |
| WM_L1#4_Table#1_Row#11 | 「0.9512」 | 「982.53」 |
| WM_L1#4_Table#1_Row#12 | 「1」 | 「997.05」 |

**Conditions:** T = 298.15 K, P = 101.0 kPa (block constraint), liquid phase.

**Chemistry insight:** The density increases monotonically from pure methanol (787.2 kg/m³) to pure water (997.05 kg/m³) as the water mole fraction increases. The relationship is slightly nonlinear — at x(water) = 0.5003, the density is 881.69 kg/m³, which is slightly below the midpoint of the two pure-component densities (derived by arithmetic average of the inspected endpoint values 787.2 and 997.05), consistent with the known positive excess volume of the water–methanol system.

Additional blocks with overlapping coverage at 298.15 K were also found, including GLOBlit_8424 (PROPblock_3, DOI 10.1021/je049691v) and GLOBlit_10866 (PROPblock_6, DOI 10.1021/je700300y), which could serve as cross-validation sources (not inspected in this run).

**Core claims:**
- A full-composition-range dataset for the binary system water + methanol at 298.15 K and 101.0 kPa (liquid phase) was found in DOI 10.1016/j.jct.2007.05.004, containing 13 data points spanning water mole fractions from 0 (pure methanol) to 1 (pure water).
- Mass density increases monotonically from 787.2 kg/m³ for pure methanol to 997.05 kg/m³ for pure water as the water mole fraction increases, with a slightly nonlinear relationship.
- At x(water) = 0.5003, the measured density is 881.69 kg/m³, which is slightly below the arithmetic average of the two pure-component endpoint densities, consistent with the known positive excess volume of the water–methanol system.

**Core blocks found:**

**WM_L1#4_Blocks_(Analysis_L1#4_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#4_Table#2 | 「GLOBlit_2825」 | 「PROPblock_10」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of water + methanol at 298.15 K and 101 kPa, 13 data points spanning full mole fraction range (0 to 1).」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


### Completed Fits
  - 10.1016/j.jct.2007.05.015/PROPblock_18 (dimethylformamide, water): RK order=5, R²=0.98872, RMSE=3.4507870522524115e-08, coeffs=[-5e-06, 2e-06, 0.0, -3e-06, -4e-06, 7e-06]
      response: direct via X = reported X | 0 reference source(s) | kg/m3 -> kg/m3
      route: measured-derived (density_to_molar_volume, exact pointwise) via density_to_molar_volume
      pure refs: dimethylformamide=7.74361e-05, water=1.84149e-05 [block-edges of derived data (water: direct/good, dimethylformamide: direct/good)]
      fit_csv: $ROOT/data\10_1016_j_jct_2007_05_015_BPROPblock_18_fit.csv
      excess_csv: $ROOT/data\10_1016_j_jct_2007_05_015_BPROPblock_18_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_jct_2007_05_015_BPROPblock_18_fit.png
      excess_plot: $ROOT/plots\10_1016_j_jct_2007_05_015_BPROPblock_18_excess.png
  - 10.1016/j.jct.2014.02.021/PROPblock_6 (dimethylformamide, methanol): RK order=1, R²=0.910862, RMSE=3.980600133620175e-08, coeffs=[-2e-06, 1e-06]
      response: direct via X = reported X | 0 reference source(s) | kg/m3 -> kg/m3
      route: measured-derived (density_to_molar_volume, exact pointwise) via density_to_molar_volume
      pure refs: dimethylformamide=7.74333e-05, methanol=4.07358e-05 [block-edges of derived data (methanol: direct/good, dimethylformamide: direct/good)]
      fit_csv: $ROOT/data\10_1016_j_jct_2014_02_021_BPROPblock_6_fit.csv
      excess_csv: $ROOT/data\10_1016_j_jct_2014_02_021_BPROPblock_6_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_jct_2014_02_021_BPROPblock_6_fit.png
      excess_plot: $ROOT/plots\10_1016_j_jct_2014_02_021_BPROPblock_6_excess.png
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
- `$ROOT/data\10_1016_j_jct_2007_05_015_BPROPblock_18_fit.csv` — RK fit data — 10.1016/j.jct.2007.05.015 PROPblock_18
- `$ROOT/data\10_1016_j_jct_2007_05_015_BPROPblock_18_excess.csv` — Excess property — 10.1016/j.jct.2007.05.015 PROPblock_18
- `$ROOT/data\10_1016_j_jct_2014_02_021_BPROPblock_6_fit.csv` — RK fit data — 10.1016/j.jct.2014.02.021 PROPblock_6
- `$ROOT/data\10_1016_j_jct_2014_02_021_BPROPblock_6_excess.csv` — Excess property — 10.1016/j.jct.2014.02.021 PROPblock_6
- `$ROOT/data\10_1016_j_jct_2007_05_004_BPROPblock_10_T298.1_fit.csv` — RK fit data — 10.1016/j.jct.2007.05.004 PROPblock_10_T298.1
- `$ROOT/data\10_1016_j_jct_2007_05_004_BPROPblock_10_T298.1_excess.csv` — Excess property — 10.1016/j.jct.2007.05.004 PROPblock_10_T298.1

### plot
- `$ROOT/plots\10_1016_j_jct_2007_05_015_BPROPblock_18_fit.png` — RK fit plot — 10.1016/j.jct.2007.05.015 PROPblock_18
- `$ROOT/plots\10_1016_j_jct_2007_05_015_BPROPblock_18_excess.png` — Excess plot — 10.1016/j.jct.2007.05.015 PROPblock_18
- `$ROOT/plots\10_1016_j_jct_2014_02_021_BPROPblock_6_fit.png` — RK fit plot — 10.1016/j.jct.2014.02.021 PROPblock_6
- `$ROOT/plots\10_1016_j_jct_2014_02_021_BPROPblock_6_excess.png` — Excess plot — 10.1016/j.jct.2014.02.021 PROPblock_6
- `$ROOT/plots\10_1016_j_jct_2007_05_004_BPROPblock_10_T298.1_fit.png` — RK fit plot — 10.1016/j.jct.2007.05.004 PROPblock_10_T298.1
- `$ROOT/plots\10_1016_j_jct_2007_05_004_BPROPblock_10_T298.1_excess.png` — Excess plot — 10.1016/j.jct.2007.05.004 PROPblock_10_T298.1

