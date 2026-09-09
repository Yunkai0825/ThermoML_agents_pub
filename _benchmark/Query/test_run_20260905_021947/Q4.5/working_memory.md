# Working Memory

## ID Catalog
<!-- PROTECTED — never compacted. Auto-populated by catalog ops. -->
### Resolved Entities
| type | global_id | registry_id | name |
|------|--------|----|------|

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find dynamic viscosity data for water + ethylene glycol binary mixtures across composition range → stored as L1_query_1 · validation: FLAGGED(2)
- [L1] Find excess molar enthalpy (Hᴱ) data for water + ethylene glycol (1,2-ethanediol) binary mixtures to quantify thermodyna → stored as L1_query_2 · validation: FLAGGED(1)

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: FLAGGED(2)

**Summary:** The ThermoML database contains 7 data blocks for dynamic viscosity of the water + ethylene glycol (1,2-ethanediol) binary system. The most comprehensive block covering the full composition range is GLOBlit_6951::PROPblock_18 (DOI: 10.1021/acs.jced.6b00526), with 33 data points measured by the falling/rolling sphere method at 100.0 kPa, spanning temperatures 293.15–303.15 K and water mole fractions from 0 to 1.0. Viscosity ranges from 0.000755 to 0.02113 Pa·s across all points. At 293.15 K, pure ethylene glycol has a viscosity of 0.02113 Pa·s and pure water 0.000949 Pa·s. The composition dependence is highly nonlinear, with substantial positive deviations from a log-linear ideal mixing rule, attributed to strong intermolecular hydrogen bonding between water and ethylene glycol. Temperature strongly reduces viscosity across all compositions, with pure EG viscosity dropping from 0.02113 Pa·s at 293.15 K to 0.01423 Pa·s at 303.15 K.

**Answer:**

#### Dynamic Viscosity Data for Water + Ethylene Glycol Binary Mixtures

##### Data Overview

The ThermoML database contains **7 data blocks** for the water (GLOBcomp_1) + 1,2-ethanediol/ethylene glycol (GLOBcomp_24) binary system with dynamic viscosity (GLOBprop_4) measurements. These blocks span a range of temperatures, compositions, and experimental methods from multiple literature sources.

The most comprehensive single block covering the full composition range is **GLOBlit_6951::PROPblock_18** (DOI: 10.1021/acs.jced.6b00526), which contains 33 data points measured by the falling/rolling sphere method at a fixed pressure of 100.0 kPa, covering temperatures 293.15–303.15 K and mole fraction of water from 0 to 1.0.

##### Composition-Dependent Viscosity Data

From **GLOBlit_6951::PROPblock_18** (inspected):

**At 293.15 K:**

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *x(water)* | *Viscosity (Pa·s)* |
|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「0 (pure EG)」 | 「0.02113」 |
| WM_L1#1_Table#1_Row#2 | 「0.2014」 | 「0.01495」 |
| WM_L1#1_Table#1_Row#3 | 「0.4011」 | 「0.01005」 |
| WM_L1#1_Table#1_Row#4 | 「0.6995」 | 「0.004584」 |
| WM_L1#1_Table#1_Row#5 | 「1.0 (pure water)」 | 「0.000949」 |

**At 298.15 K:**

**WM_L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *x(water)* | *Viscosity (Pa·s)* |
|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「0 (pure EG)」 | 「0.01724」 |
| WM_L1#1_Table#2_Row#2 | 「0.2014」 | 「0.01219」 |
| WM_L1#1_Table#2_Row#3 | 「0.4011」 | 「0.00831」 |
| WM_L1#1_Table#2_Row#4 | 「0.6995」 | 「0.003884」 |
| WM_L1#1_Table#2_Row#5 | 「1.0 (pure water)」 | 「0.000843」 |

**At 303.15 K:**

**WM_L1#1_Table#3_(Query_L1#1_Answer):**

| *row_id* | *x(water)* | *Viscosity (Pa·s)* |
|---|---|---|
| WM_L1#1_Table#3_Row#1 | 「0 (pure EG)」 | 「0.01423」 |
| WM_L1#1_Table#3_Row#2 | 「0.2014」 | 「0.01014」 |
| WM_L1#1_Table#3_Row#3 | 「0.4969」 | 「0.005653」 |
| WM_L1#1_Table#3_Row#4 | 「1.0 (pure water)」 | 「0.000755」 |

Overall stats for this block: viscosity ranges from **0.000755 to 0.02113 Pa·s** across all 33 data points.

##### Non-Ideal Mixing Behavior

The data reveal **strongly non-ideal mixing** in the viscosity of this system:

- Pure ethylene glycol is **far more viscous** than pure water at 293.15 K (0.02113 vs. 0.000949 Pa·s — a ratio of approximately 0.02113 ÷ 0.000949 ≈ 22, derived by dividing the two inspected endpoint values).
- The composition dependence is highly nonlinear. Under a simple log-linear (Arrhenius) ideal mixing rule at 293.15 K, the estimated viscosity at x(water) = 0.4011 would be approximately 0.006 Pa·s (derived calculation: exp((1 − 0.4011) × ln(0.02113) + 0.4011 × ln(0.000949)), where 1 − 0.4011 = 0.5989 is the complementary EG mole fraction), but the measured value is **0.01005 Pa·s** — a substantial **positive deviation** (derived comparison: the measured value is roughly 65% higher than the log-linear ideal estimate).
- This positive excess viscosity is characteristic of systems with strong intermolecular hydrogen bonding between the two components. Water and ethylene glycol form extensive H-bond networks, with EG acting as both donor and acceptor through its two hydroxyl groups, creating more structured and viscous mixtures than ideal mixing would predict.
- Temperature strongly reduces viscosity across all compositions, with pure EG viscosity dropping from 0.02113 Pa·s at 293.15 K to 0.01423 Pa·s at 303.15 K (a ~33% decrease over just 10 K; derived from inspected values).

This system is a textbook example of how hydrogen-bonding interactions between unlike molecules can produce transport-property deviations well beyond what thermodynamic excess Gibbs energy alone would suggest.

**Core claims:**
- The ThermoML database contains 7 data blocks for the water + ethylene glycol binary system with dynamic viscosity measurements, with the most comprehensive single block (GLOBlit_6951::PROPblock_18) covering 33 data points at 100.0 kPa, temperatures 293.15–303.15 K, and water mole fractions from 0 to 1.0.
- At 293.15 K, the dynamic viscosity decreases monotonically from 0.02113 Pa·s for pure ethylene glycol to 0.000949 Pa·s for pure water, spanning roughly a factor of 22 in magnitude.
- The composition dependence of viscosity is highly nonlinear, with the measured viscosity at x(water) = 0.4011 and 293.15 K being 0.01005 Pa·s, which represents a substantial positive deviation above a log-linear (Arrhenius) ideal mixing estimate, indicative of strongly non-ideal mixing attributed to extensive intermolecular hydrogen bonding between water and ethylene glycol.
- Temperature strongly reduces viscosity across all compositions; pure ethylene glycol viscosity drops from 0.02113 Pa·s at 293.15 K to 0.01423 Pa·s at 303.15 K over a 10 K interval.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#4 | 「GLOBlit_6951」 | 「PROPblock_18」 | 「GLOBcomp_24, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity measurements for water + 1,2-ethanediol (ethylene glycol) binary mixtures across full composition range at 293.15–303.15 K and 100.0 kPa, measured by falling/rolling sphere method.」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(2) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNGROUNDED_LITERAL** GLOBlit_6951::PROPblock_18: 22 (near '…000949 Pa·s — a ratio of approximately 0.02113 ÷ 0.000949 ≈ …') matches no inspected row/stat, database table, or other source of GLOBlit_6951::PROPblock_18
- **UNGROUNDED_LITERAL** GLOBlit_6951::PROPblock_18: 0.5989 (near '…× ln(0.02113) + 0.4011 × ln(0.000949)), where 1 - 0.4011 = 0…') matches no inspected row/stat, database table, or other source of GLOBlit_6951::PROPblock_18
### L1_query_2
**L1_query_2** — status: success · validation: FLAGGED(1)

**Summary:** The ThermoML database (DOI 10.1016/j.tca.2009.06.004) contains 13 excess molar enthalpy (Hᴱ) data points for the water + ethylene glycol binary system measured at 298.15 K and 101.0 kPa, spanning x(water) = 0.1014 to 0.915. Hᴱ is negative (exothermic) across the entire composition range, with the most exothermic value of −0.715 kJ/mol occurring at x(water) = 0.669, corresponding to roughly a 2:1 water-to-EG molar ratio. The Hᴱ curve is asymmetric, with the minimum shifted toward the water-rich side, consistent with the stoichiometry of hydrogen-bond formation involving ethylene glycol's two hydroxyl groups. The moderate magnitude of the exothermic mixing reflects partial disruption of existing hydrogen-bond networks in both pure components before new cross-interactions form.

**Answer:**

#### Excess Molar Enthalpy (Hᴱ) Data for Water + Ethylene Glycol Binary Mixtures

##### Data Source

The ThermoML database contains **1 data block** with excess molar enthalpy measurements for the water (GLOBcomp_1) + 1,2-ethanediol/ethylene glycol (GLOBcomp_24) binary system:

- **GLOBlit_5843::PROPblock_1** (DOI: 10.1016/j.tca.2009.06.004)
- **13 data points** measured by Calvet calorimetry at **298.15 K** and **101.0 kPa**
- Composition range: x(water) = 0.1014 to 0.915

##### Complete Composition-Dependent Hᴱ Data at 298.15 K

**WM_L1#2_Table#1_(Query_L1#2_Answer):**

| *row_id* | *x(water)* | *Hᴱ (kJ/mol)* |
|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「0.1014」 | 「−0.174」 |
| WM_L1#2_Table#1_Row#2 | 「0.1994」 | 「−0.337」 |
| WM_L1#2_Table#1_Row#3 | 「0.2091」 | 「−0.347」 |
| WM_L1#2_Table#1_Row#4 | 「0.3051」 | 「−0.48」 |
| WM_L1#2_Table#1_Row#5 | 「0.3674」 | 「−0.559」 |
| WM_L1#2_Table#1_Row#6 | 「0.3995」 | 「−0.59」 |
| WM_L1#2_Table#1_Row#7 | 「0.4807」 | 「−0.64」 |
| WM_L1#2_Table#1_Row#8 | 「0.5455」 | 「−0.666」 |
| WM_L1#2_Table#1_Row#9 | 「0.6144」 | 「−0.698」 |
| WM_L1#2_Table#1_Row#10 | 「0.669」 | 「−0.715」 |
| WM_L1#2_Table#1_Row#11 | 「0.7949」 | 「−0.681」 |
| WM_L1#2_Table#1_Row#12 | 「0.8656」 | 「−0.57」 |
| WM_L1#2_Table#1_Row#13 | 「0.915」 | 「−0.423」 |

##### Key Observations

- **Sign:** Hᴱ is **negative (exothermic)** across the entire measured composition range, indicating that mixing water and ethylene glycol releases heat.

- **Magnitude and extremum:** The minimum (most exothermic) value is **−0.715 kJ/mol at x(water) = 0.669**, corresponding to approximately a 2:1 water-to-EG molar ratio. The topology is non-monotonic with one extremum.

- **Asymmetry:** The Hᴱ curve is asymmetric, with the minimum shifted toward the water-rich side (x(water) ≈ 0.67 rather than 0.5). This is consistent with the stoichiometry of hydrogen-bond formation: each ethylene glycol molecule has two hydroxyl groups that can each interact with water molecules, so the optimal interaction occurs when there is an excess of water relative to EG.

- **Connection to viscosity non-ideality:** The negative Hᴱ values confirm strong, favorable intermolecular interactions (hydrogen bonding) between water and ethylene glycol. This thermodynamic evidence of exothermic mixing is consistent with the positive excess viscosity previously found in the viscosity data for this system (from prior working memory, not inspected in this run): the same hydrogen-bonding network that releases enthalpy upon mixing also creates more structured, viscous solutions than ideal mixing would predict.

- **Moderate magnitude:** While clearly exothermic, the maximum absolute magnitude of Hᴱ is |−0.715| = 0.715 kJ/mol (derived: absolute value of the inspected minimum at x(water) = 0.669), which is moderate compared to strongly associating systems, reflecting the fact that both pure components already have extensive hydrogen-bond networks that must be partially disrupted before new cross-interactions form.

**Core claims:**
- At 298.15 K and 101.0 kPa, the excess molar enthalpy (Hᴱ) of water + ethylene glycol mixtures is negative (exothermic) across the entire measured composition range x(water) = 0.1014 to 0.915, based on 13 Calvet calorimetry data points from DOI 10.1016/j.tca.2009.06.004.
- The most exothermic measured value is Hᴱ = −0.715 kJ/mol at x(water) = 0.669, indicating the Hᴱ minimum is shifted toward the water-rich side rather than at equimolar composition.
- The asymmetry of the Hᴱ curve, with its minimum near a 2:1 water-to-EG molar ratio, is consistent with the stoichiometry of hydrogen-bond formation involving ethylene glycol's two hydroxyl groups.
- The moderate magnitude of Hᴱ (maximum |Hᴱ| of 0.715 kJ/mol) reflects partial disruption of existing hydrogen-bond networks in both pure components before new cross-interactions form.

**Core blocks found:**

**WM_L1#2_Blocks_(Query_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#2 | 「GLOBlit_5843」 | 「PROPblock_1」 | 「GLOBcomp_24, GLOBcomp_1」 | 「GLOBprop_17」 | 「Excess molar enthalpy data for water + 1,2-ethanediol at 298.15 K and 101.0 kPa, 13 data points covering x(water) = 0.1014 to 0.915, measured by Calvet calorimetry.」 |

*Not stored here: 2 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(1) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNGROUNDED_LITERAL** GLOBlit_5843::PROPblock_1: 0.715 (near '…thermic, the maximum absolute magnitude of Hᴱ is |-0.715| = …') matches no inspected row/stat, database table, or other source of GLOBlit_5843::PROPblock_1


