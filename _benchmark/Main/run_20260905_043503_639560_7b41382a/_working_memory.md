# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_043503_639560_7b41382a`

### History
- [analysis:A1] "Find and fit excess molar enthalpy (HE) data for the binary system ethanol + wat" (734s, 22 iters, validation=PASS verdict=**Data Quality**
Multiple fit_)

### Analysis Agent Results

#### A1
**A1** — validation: PASS

**Answer:**

#### Excess Molar Enthalpy (H^E) of Ethanol + Water at 298.15 K — Redlich-Kister Analysis

##### Data Source

The best available dataset for the full-composition-range excess molar enthalpy of ethanol + water at 298.15 K comes from **GLOBlit_2574::PROPblock_4** (DOI 10.1016/j.jct.2005.06.018):

- **Data priority:** DP0 — directly measured excess molar enthalpy (Calvet calorimetry)
- **Conditions:** T = 298.15 K, P = 101.0 kPa
- **Data points used:** 12 mixture points at 298.15 K (from 27 total spanning 298.15–323.15 K)
- **Composition range:** x(ethanol) = 0.0582 to 0.900

⚠️ **Note:** The paper title in the ThermoML database references propanediols/butanediol rather than ethanol — a possible compound-mapping issue. However, the data are internally consistent and agree with an independent measurement (see Cross-validation below).

##### Measured Data at 298.15 K (all from GLOBlit_2574::PROPblock_4)

**WM_A#1_Table#1_(Main_A#1_Answer):**

| *row_id* | *x(ethanol)* | *H^E (kJ/mol)* |
|---|---|---|
| WM_A#1_Table#1_Row#1 | 「0.0582」 | 「−0.492」 |
| WM_A#1_Table#1_Row#2 | 「0.1198」 | 「−0.747」 |
| WM_A#1_Table#1_Row#3 | 「0.150」 | 「−0.770」 |
| WM_A#1_Table#1_Row#4 | 「0.1837」 | 「−0.767」 |
| WM_A#1_Table#1_Row#5 | 「0.250」 | 「−0.702」 |
| WM_A#1_Table#1_Row#6 | 「0.2981」 | 「−0.649」 |
| WM_A#1_Table#1_Row#7 | 「0.4127」 | 「−0.501」 |
| WM_A#1_Table#1_Row#8 | 「0.500」 | 「−0.391」 |
| WM_A#1_Table#1_Row#9 | 「0.607」 | 「−0.323」 |
| WM_A#1_Table#1_Row#10 | 「0.701」 | 「−0.271」 |
| WM_A#1_Table#1_Row#11 | 「0.812」 | 「−0.206」 |
| WM_A#1_Table#1_Row#12 | 「0.900」 | 「−0.148」 |

##### Redlich-Kister Fit Results (fitted to GLOBlit_2574::PROPblock_4 data above)

The excess molar enthalpy is represented as:

$$H^E = x_1 x_2 \sum_{k=0}^{n} A_k (x_1 - x_2)^k$$

where x₁ = mole fraction of ethanol and x₂ = 1 − x₁ (mole fraction of water).

**WM_A#1_Table#2_(Main_A#1_Answer):**

| *row_id* | *Parameter* | *Value* |
|---|---|---|
| WM_A#1_Table#2_Row#1 | 「**BIC-selected order**」 | 「**4**」 |
| WM_A#1_Table#2_Row#2 | 「**R²**」 | 「**0.998537**」 |
| WM_A#1_Table#2_Row#3 | 「**RMSE**」 | 「**0.00837 kJ/mol**」 |

**Redlich-Kister coefficients (kJ/mol):**

**WM_A#1_Table#3_(Main_A#1_Answer):**

| *row_id* | *k* | *A_k* |
|---|---|---|
| WM_A#1_Table#3_Row#1 | 「0」 | 「−1.60102」 |
| WM_A#1_Table#3_Row#2 | 「1」 | 「+1.73493」 |
| WM_A#1_Table#3_Row#3 | 「2」 | 「−3.19748」 |
| WM_A#1_Table#3_Row#4 | 「3」 | 「+3.11326」 |
| WM_A#1_Table#3_Row#5 | 「4」 | 「−2.36171」 |

**Model selection (BIC comparison):**

**WM_A#1_Table#4_(Main_A#1_Answer):**

| *row_id* | *Order* | *BIC* | *R²* | *RMSE (kJ/mol)* |
|---|---|---|---|---|
| WM_A#1_Table#4_Row#1 | 「0」 | 「−27.01」 | 「−0.789」 | 「0.2926」 |
| WM_A#1_Table#4_Row#2 | 「1」 | 「−39.32」 | 「0.479」 | 「0.1579」 |
| WM_A#1_Table#4_Row#3 | 「2」 | 「−64.66」 | 「0.949」 | 「0.0496」 |
| WM_A#1_Table#4_Row#4 | 「3」 | 「−87.76」 | 「0.994」 | 「0.0171」 |
| WM_A#1_Table#4_Row#5 | 「**4**」 | 「**−102.38**」 | 「**0.999**」 | 「**0.0084**」 |
| WM_A#1_Table#4_Row#6 | 「5」 | 「−99.95」 | 「0.999」 | 「0.0083」 |

Order 4 is selected by BIC (lowest value, −102.38). Adding a 5th coefficient does not improve the fit enough to justify the additional parameter.

##### Key Findings

1. **Sign of H^E — Exothermic mixing:** H^E is **negative across the entire composition range** (0 < x(ethanol) < 1). Mixing ethanol and water at 298.15 K always **releases heat**.

2. **Maximum magnitude:** The RK fit predicts (via `predict_from_rk`, tool-returned value: max |excess| = −0.773521 kJ/mol) a minimum H^E of approximately **−0.774 kJ/mol**. The measured minimum in GLOBlit_2574::PROPblock_4 is −0.770 kJ/mol at x(ethanol) = 0.150. The minimum occurs in the **water-rich region** near x(ethanol) ≈ 0.15.

3. **Asymmetry:** The H^E curve is strongly asymmetric — the minimum is shifted far toward the water-rich side. The large positive A₁ coefficient (+1.73493) and the significant higher-order terms (A₂ through A₄) quantify this asymmetry. At x(ethanol) = 0.500, the RK fit predicts (via `predict_from_rk`) H^E ≈ −0.400 kJ/mol, only about half the magnitude of the minimum.

4. **Cross-validation with GLOBlit_6377::PROPblock_1:** An independent measurement from a different laboratory (**GLOBlit_6377::PROPblock_1**, DOI 10.1016/j.tca.2017.05.023) reports H^E = −0.70659 kJ/mol at x(ethanol) = 0.102 and 298.15 K. This is consistent with the fitted curve from GLOBlit_2574::PROPblock_4 — the nearest measured point in GLOBlit_2574::PROPblock_4 is x(ethanol) = 0.1198 with H^E = −0.747 kJ/mol, and the trend of increasing |H^E| from x = 0.0582 to 0.150 in GLOBlit_2574::PROPblock_4 supports the GLOBlit_6377 value falling between those measurements.

##### Molecular Interpretation

The strongly exothermic and asymmetric H^E curve reflects the complex interplay of hydrogen-bonding interactions in ethanol–water mixtures:

- **Water-rich region (x_ethanol < 0.15):** Adding small amounts of ethanol to water is highly exothermic because ethanol molecules can be accommodated into the water hydrogen-bond network, forming strong O–H···O hydrogen bonds between ethanol's hydroxyl group and surrounding water molecules. The ethanol alkyl group can be partially enclosed in clathrate-like water cages, releasing energy as the water restructures.

- **Near the minimum (x_ethanol ≈ 0.15):** The maximum heat release occurs where the water network can still maintain extensive hydrogen bonding while maximally interacting with ethanol hydroxyl groups.

- **Ethanol-rich region (x_ethanol > 0.5):** As ethanol becomes the majority component, the weaker ethanol–ethanol hydrogen-bond network is progressively disrupted by water, but the energetic gain from forming ethanol–water hydrogen bonds is partially offset by the loss of ethanol–ethanol interactions. The magnitude of H^E decreases steadily.

- **The asymmetry** (minimum shifted toward water-rich compositions) arises because water's three-dimensional hydrogen-bond network has a much higher cohesive energy density than ethanol's chain-like hydrogen bonding, so the energetic perturbation is greatest when a few ethanol molecules are inserted into the water-dominated structure.

##### Output Files

- **Fit data CSV:** `10_1016_j_jct_2005_06_018_BPROPblock_4_T298.1_fit.csv`
- **Excess property CSV:** `10_1016_j_jct_2005_06_018_BPROPblock_4_T298.1_excess.csv`
- **Fit plot:** `10_1016_j_jct_2005_06_018_BPROPblock_4_T298.1_fit.png`
- **Excess property plot:** `10_1016_j_jct_2005_06_018_BPROPblock_4_T298.1_excess.png`

**Core claims:**
- The excess molar enthalpy of ethanol + water at 298.15 K and 101.0 kPa is negative across the entire composition range (0 < x(ethanol) < 1), indicating exothermic mixing.
- The H^E curve is strongly asymmetric, with the minimum (maximum exothermic effect) located in the water-rich region near x(ethanol) ≈ 0.15; the measured minimum is −0.770 kJ/mol at x(ethanol) = 0.150, and the Redlich-Kister fit predicts a minimum of approximately −0.774 kJ/mol.
- A 4th-order Redlich-Kister polynomial was selected by BIC (BIC = −102.38) to fit 12 data points from GLOBlit_2574::PROPblock_4, yielding R² = 0.998537 and RMSE = 0.00837 kJ/mol, with coefficients A₀ = −1.60102, A₁ = +1.73493, A₂ = −3.19748, A₃ = +3.11326, A₄ = −2.36171 (all in kJ/mol).
- An independent measurement from GLOBlit_6377::PROPblock_1 (H^E = −0.70659 kJ/mol at x(ethanol) = 0.102, 298.15 K) is consistent with the fitted curve from the primary dataset, providing cross-validation.
- A possible compound-mapping issue exists: the paper title in the ThermoML database references propanediols/butanediol rather than ethanol, though the data are internally consistent and agree with the independent cross-validation measurement.

**Sources:**

**WM_A#1_Table#5_(Main_A#1_Sources):**

| *row_id* | *lit_num_id* | *block* | *doi* | *BLKsubsys_id* | *description* |
|---|---|---|---|---|---|
| WM_A#1_Table#5_Row#1 | 「GLOBlit_2574」 | 「PROPblock_4」 | 「10.1016/j.jct.2005.06.018」 | 「—」 | 「Primary data source providing 27 excess molar enthalpy measurements for ethanol + water (12 at 298.15 K) via Calvet calorimetry across x(ethanol) = 0.033–0.968 at 101.0 kPa. These data were used for the 4th-order Redlich-Kister fit (R² = 0.999, RMSE = 0.0084 kJ/mol) with minimum H^E ≈ −0.77 kJ/mol near x(ethanol) ≈ 0.15.」 |
| WM_A#1_Table#5_Row#2 | 「GLOBlit_6377」 | 「PROPblock_1」 | 「10.1016/j.tca.2017.05.023」 | 「—」 | 「Independent cross-validation point: a single flow-calorimetry measurement of H^E = −0.70659 kJ/mol at x(ethanol) = 0.102 and 298.15 K for ethanol + water, consistent with the fitted curve from the primary dataset.」 |

**Fit results:**

**WM_A#1_Table#6_(Main_A#1_FitResults):**

| *row_id* | *lit_num_id* | *block* | *property* | *rk_order* | *rk_coeffs* | *r_squared* | *rmse* | *n_points* | *T_K* | *mixing_rule* |
|---|---|---|---|---|---|---|---|---|---|---|
| WM_A#1_Table#6_Row#1 | 「GLOBlit_2574」 | 「PROPblock_4」 | 「GLOBprop_17」 | 「4」 | 「-1.6010234710917044, 1.7349306238447832, -3.197479901103324, 3.1132645013310305, -2.3617072865602253」 | 「0.998537」 | 「0.008367192167912752」 | 「12」 | 「298.15」 | 「declared_excess_no_baseline」 |

*Not stored here: 5 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


**Verdict:** **Data Quality**
Multiple fit_block attempts mostly failed (289–420 char responses suggest errors), with only one returning 882 chars — likely the successful fit. The predict_from_rk calls also mostly failed. The agent quotes 12 measured data points, but these cannot be verified against tool results since the trace shows only response sizes, not content. The DOI metadata mismatch (propanediols paper cited for ethanol+water) is a significant red flag suggesting possible compound misidentification. Composition basis appears to be mole fraction. No composition_conversion issues flagged.

**Fit Quality**
Order-4 RK with R²=0.999 and RMSE=0.0084 kJ/mol is reasonable for 12 points, though BIC selection from 5→4 shows marginal improvement. The fit quality seems acceptable if the underlying data are correct.

**Scientific Verdict**
The DOI mismatch (propanediols vs. ethanol+water) critically undermines confidence — the data may belong to a different system entirely. Known literature values for ethanol+water H^E at 298.15 K show minima near −0.8 kJ/mol around x≈0.3, not x≈0.15. **CONDITIONAL PASS** pending DOI/compound verification; results should be treated cautiously.
**Session:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_043503_639560_7b41382a\analysis_runs\run_8`
