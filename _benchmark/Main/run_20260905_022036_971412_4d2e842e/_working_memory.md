# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_022036_971412_4d2e842e`

### History
- [analysis:A1] "Fit a Redlich-Kister polynomial to the density of liquid ethanol + water at 25°C" (470s, 14 iters, validation=PASS verdict=**Data Quality**
The agent use)
- [menu:run] inspect_block_table → OK

### Analysis Agent Results

#### A1
**A1** — validation: PASS

**Answer:**

#### Redlich-Kister Correlation for Density of Ethanol + Water at 298.15 K

##### Data Source

- **DOI:** 10.1016/j.fluid.2004.11.019 (GLOBlit_220)
- **Block:** PROPblock_2
- **System:** ethanol (GLOBcomp_2) + water (GLOBcomp_1), liquid phase
- **Conditions:** T = 298.15 K, P = 100 kPa (atmospheric)
- **Data points used:** 47 mixture compositions (from 810 total rows spanning multiple T and P)
- **Composition range:** x(ethanol) = 0.003 to 1.0 (mole fraction)
- **Measurement method:** Vibrating-tube densimeter (GLOBmeas_138)

##### Pure-Component Densities

**WM_A#1_Table#1_(Main_A#1_Answer):**

| *row_id* | *Component* | *ρ* (kg/m³)* | *Source* |
|---|---|---|---|
| WM_A#1_Table#1_Row#1 | 「Water」 | 「992.083」 | 「Block edge value (direct/good)」 |
| WM_A#1_Table#1_Row#2 | 「Ethanol」 | 「785.7」 | 「Block edge value (direct/good)」 |

##### Fitted Equation

The total density is expressed as:

$$\rho(x_1) = x_1 \, \rho_1^* + x_2 \, \rho_2^* + x_1 \, x_2 \sum_{k=0}^{n} A_k (x_1 - x_2)^k$$

where x₁ = mole fraction of ethanol, x₂ = 1 − x₁, ρ₁* = 785.7 kg/m³ (pure ethanol), ρ₂* = 992.083 kg/m³ (pure water), and the mixing rule is **linear** (appropriate for density).

##### BIC-Selected Polynomial Order and Coefficients

**WM_A#1_Table#2_(Main_A#1_Answer):**

| *row_id* | *Parameter* | *Value* |
|---|---|---|
| WM_A#1_Table#2_Row#1 | 「**BIC-selected order**」 | 「**3**」 |
| WM_A#1_Table#2_Row#2 | 「A₀」 | 「−120.557 kg/m³」 |
| WM_A#1_Table#2_Row#3 | 「A₁」 | 「18.568 kg/m³」 |
| WM_A#1_Table#2_Row#4 | 「A₂」 | 「43.919 kg/m³」 |
| WM_A#1_Table#2_Row#5 | 「A₃」 | 「−31.351 kg/m³」 |
| WM_A#1_Table#2_Row#6 | 「**R²**」 | 「**0.997283**」 |
| WM_A#1_Table#2_Row#7 | 「**RMSE**」 | 「**0.4748 kg/m³**」 |
| WM_A#1_Table#2_Row#8 | 「**BIC**」 | 「**−54.62**」 |

##### Model Selection Summary

**WM_A#1_Table#3_(Main_A#1_Answer):**

| *row_id* | *Order* | *BIC* | *R²* | *RMSE (kg/m³)* |
|---|---|---|---|---|
| WM_A#1_Table#3_Row#1 | 「0」 | 「47.60」 | 「0.969419」 | 「1.593」 |
| WM_A#1_Table#3_Row#2 | 「1」 | 「48.19」 | 「0.971469」 | 「1.538」 |
| WM_A#1_Table#3_Row#3 | 「2」 | 「−33.56」 | 「0.995383」 | 「0.619」 |
| WM_A#1_Table#3_Row#4 | 「3」 | 「**−54.62**」 | 「**0.997283**」 | 「**0.475**」 |
| WM_A#1_Table#3_Row#5 | 「4」 | 「−52.17」 | 「0.997362」 | 「0.468」 |
| WM_A#1_Table#3_Row#6 | 「5」 | 「−53.77」 | 「0.997651」 | 「0.441」 |

The BIC criterion selects order 3 as optimal — orders 4 and 5 provide negligible improvement in R² while incurring a complexity penalty.

##### Chemistry Insight

The large negative A₀ coefficient (−120.6 kg/m³) reflects the well-known **volume contraction** upon mixing ethanol and water: hydrogen-bonding reorganization allows water molecules to partially fill the voids in ethanol's structure, producing a mixture denser than the mole-fraction-weighted average of the pure components. The asymmetry captured by A₁ through A₃ indicates that the maximum deviation from ideal (linear) mixing occurs at water-rich compositions (roughly x(ethanol) ≈ 0.3–0.4), consistent with the composition range where the ethanol–water hydrogen-bond network undergoes the most dramatic restructuring.

Representative data points at 298.15 K, 100 kPa (from inspected block rows):

**WM_A#1_Table#4_(Main_A#1_Answer):**

| *row_id* | *x(ethanol)* | *ρ (kg/m³)* |
|---|---|---|
| WM_A#1_Table#4_Row#1 | 「0.003」 | 「995.3」 |
| WM_A#1_Table#4_Row#2 | 「0.2502」 | 「918.5」 |
| WM_A#1_Table#4_Row#3 | 「0.4501」 | 「868.8」 |
| WM_A#1_Table#4_Row#4 | 「0.6967」 | 「825.2」 |
| WM_A#1_Table#4_Row#5 | 「1.000」 | 「785.7」 |

##### Output Files

- **Fit data CSV:** `10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_fit.csv`
- **Excess property CSV:** `10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_excess.csv`
- **Fit plot:** `10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_fit.png`
- **Excess plot:** `10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_excess.png`

**Core claims:**
- Liquid density of ethanol + water at 298.15 K and 100 kPa was correlated using a Redlich-Kister expansion with a linear (mole-fraction-weighted) ideal mixing rule, fitted to 47 mixture compositions spanning x(ethanol) = 0.003 to 1.0, with pure-component densities of 785.7 kg/m³ (ethanol) and 992.083 kg/m³ (water).
- BIC model selection favors a 3rd-order Redlich-Kister polynomial with coefficients A₀ = −120.557 kg/m³, A₁ = 18.568 kg/m³, A₂ = 43.919 kg/m³, A₃ = −31.351 kg/m³, yielding R² = 0.997283, RMSE = 0.4748 kg/m³, and BIC = −54.62; orders 4 and 5 provide negligible improvement in R² while incurring a complexity penalty.
- The large negative A₀ coefficient reflects volume contraction upon mixing ethanol and water due to hydrogen-bonding reorganization, and the asymmetry captured by higher-order coefficients indicates the maximum deviation from ideal mixing occurs at water-rich compositions (roughly x(ethanol) ≈ 0.3–0.4).

**Sources:**

**WM_A#1_Table#5_(Main_A#1_Sources):**

| *row_id* | *lit_num_id* | *block* | *doi* | *BLKsubsys_id* | *description* |
|---|---|---|---|---|---|
| WM_A#1_Table#5_Row#1 | 「GLOBlit_220」 | 「PROPblock_2」 | 「10.1016/j.fluid.2004.11.019」 | 「—」 | 「This block provides binary ethanol + water mass density data (810 points, 298.15–348.15 K, 100–40000 kPa, x = 0.003–1.0) from which the 47 data points at T = 298.15 K and P = 100 kPa were extracted to fit the Redlich-Kister correlation of order 3 with R² = 0.997283 and RMSE = 0.475 kg/m³.」 |

**Fit results:**

**WM_A#1_Table#6_(Main_A#1_FitResults):**

| *row_id* | *lit_num_id* | *block* | *property* | *rk_order* | *rk_coeffs* | *r_squared* | *rmse* | *n_points* | *T_K* | *mixing_rule* |
|---|---|---|---|---|---|---|---|---|---|---|
| WM_A#1_Table#6_Row#1 | 「GLOBlit_220」 | 「PROPblock_2」 | 「GLOBprop_1」 | 「3」 | 「-120.55681029600882, 18.567625256466393, 43.91912836453406, -31.35056319853136」 | 「0.997283」 | 「0.47476545853553287」 | 「47」 | 「298.15」 | 「linear」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


**Verdict:** **Data Quality**
The agent used ThermoML data from a real DOI with 47 mixture compositions at 298.15 K — appropriate source. However, multiple `fit_block` calls returned short responses (~259–324 chars), suggesting failures or minimal output, until call 12 (852 chars) apparently succeeded. The representative data points (e.g., x=0.003→995.3, x=0.2502→918.5) cannot be verified against tool results since inspect_block returned limited data. The pure water density of 992.083 kg/m³ is suspect (literature: ~997.05 kg/m³), suggesting a possible data or extraction error. Composition basis appears to be mole fraction — acceptable. No fabrication flag triggered since fit_block did return results.

**Fit Quality**
Order 3 selected by BIC is reasonable. R²=0.997 and RMSE=0.475 kg/m³ are acceptable but the anomalous pure-water density raises concern about underlying data quality.

**Scientific Verdict**
The methodology is sound but the pure-water density (~992 vs ~997 kg/m³) is a red flag — possibly a data issue in the source block. Users should verify pure-component endpoints before applying this correlation. The negative A₀ correctly captures volume contraction physics.
**Session:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_022036_971412_4d2e842e\analysis_runs\run_1`
