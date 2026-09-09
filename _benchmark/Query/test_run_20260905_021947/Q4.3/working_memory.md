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
- [L1] Find density or molar volume data for the ternary mixture DMF + water + methanol at 298 K → stored as L1_query_1 · validation: PASS
- [L1] Find pure component mass density of DMF (N,N-dimethylformamide) at 298.15 K → stored as L1_query_2 · validation: FLAGGED(3)
- [L1] Find pure component mass density of water at 298.15 K and pure component mass density of methanol at 298.15 K from the T → stored as L1_query_3 · validation: FLAGGED(1)
- [L1] Find excess molar volume (VE) data for binary DMF + water mixture at 298.15 K → stored as L1_query_4 · validation: FLAGGED(2)
- [L1] Find binary density data for DMF+methanol and water+methanol at 298.15 K → stored as L1_query_5 · validation: FLAGGED(2)

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: no_results · validation: PASS

**Summary:** No density, molar volume, or excess molar volume data was found in the ThermoML database for the ternary mixture of N,N-dimethylformamide (DMF) + water + methanol at 298.15 K or any nearby temperature. A broad search for ternary data blocks containing all three components across 273–373 K returned only one block (GLOBlit_5688 / PROPblock_4, DOI: 10.1016/j.tca.2006.02.028), which reports the molar enthalpy of solution of DMF at infinite dilution in methanol–water solvent mixtures at 298.15 K and 1.0 kPa, with 13 data points spanning solvent methanol mole fractions from 0 to 1 and enthalpies ranging from −2.32 kJ/mol (pure water) to 11.95 kJ/mol (pure methanol). That block contains no volumetric properties. The direct ternary volumetric measurement needed to determine the molar volume of an equimolar DMF + water + methanol mixture at 298 K is not available in the database.

**Answer:**

No density, molar volume, or excess molar volume data was found in the ThermoML database for the ternary mixture of N,N-dimethylformamide (DMF) + water + methanol at 298.15 K (or any nearby temperature).

A broad search for any data blocks containing all three components (GLOBcomp_18: DMF, GLOBcomp_1: water, GLOBcomp_4: methanol) across the temperature range 273–373 K returned only one ternary block:

- **GLOBlit_5688 / PROPblock_4** (DOI: 10.1016/j.tca.2006.02.028) — This block reports the **molar enthalpy of solution** of DMF at infinite dilution (mole fraction of DMF = 0.0) in methanol–water solvent mixtures at 298.15 K and 1.0 kPa, measured by titration calorimetry. It contains 13 data points spanning solvent mole fractions of methanol from 0 to 1. The molar enthalpy of solution ranges from −2.32 kJ/mol (pure water solvent) to 11.95 kJ/mol (pure methanol solvent), increasing monotonically with methanol content. This block contains no volumetric properties.

**In summary:** The ThermoML database does not contain the density or molar volume data needed to determine the molar volume of an equimolar DMF + water + methanol mixture at 298 K. Binary subsystem data (e.g., DMF + water, DMF + methanol, water + methanol) may exist separately and could potentially support mixing-rule estimates, but the direct ternary volumetric measurement is not available in this database.

**Core claims:**
- The ThermoML database does not contain density, molar volume, or excess molar volume data for the ternary mixture of DMF + water + methanol at 298.15 K, and therefore the data needed to directly determine the molar volume of an equimolar DMF + water + methanol mixture at 298 K is not available in that database.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#1 | 「GLOBlit_5688」 | 「PROPblock_4」 | 「GLOBcomp_4, GLOBcomp_18, GLOBcomp_1」 | 「GLOBprop_15」 | 「Molar enthalpy of solution of DMF at infinite dilution in methanol-water solvent mixtures at 298.15 K. No volumetric properties present.」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.
### L1_query_2
**L1_query_2** — status: success · validation: FLAGGED(3)

**Summary:** The ThermoML database provides mass density values for pure N,N-dimethylformamide (DMF) at 298.15 K. From DOI 10.1016/j.fluid.2004.12.004 (GLOBlit_228 / PROPblock_4), the density is 943.81 kg/m³ at 298.15 K and 101.325 kPa. From DOI 10.1007/s10765-009-0648-5 (GLOBlit_86 / PROPblock_6), the density is 943.917 kg/m³ at 298.15 K and 101.0 kPa, part of a 5-point temperature series from 288.15 K (953.442 kg/m³) to 308.15 K (934.357 kg/m³). Most reported values cluster near 943.9 kg/m³. A derived molar volume of approximately 77.4 cm³/mol was computed using the standard molar mass of DMF (73.09 g/mol, general chemical knowledge, not a database datum) and the inspected density of 943.9 kg/m³; this molar volume is a derived calculation, not a database datum. Direct ternary volumetric data for DMF + water + methanol mixtures was not found in the ThermoML database.

**Answer:**

The ThermoML database contains multiple measurements of the mass density of pure N,N-dimethylformamide (DMF) at 298.15 K. Representative values from inspected blocks:

1. **GLOBlit_228 / PROPblock_4** (DOI: 10.1016/j.fluid.2004.12.004)
   - **943.81 kg/m³** at 298.15 K, 101.325 kPa (single data point)

2. **GLOBlit_86 / PROPblock_6** (DOI: 10.1007/s10765-009-0648-5)
   - **943.917 kg/m³** at 298.15 K, 101.0 kPa (from a 5-point temperature series spanning 288.15–308.15 K; density decreases monotonically and nearly linearly with temperature, from 953.442 kg/m³ at 288.15 K to 934.357 kg/m³ at 308.15 K)

Additional blocks from the search confirm densities at 298.15 K in the range of approximately 943.8–949 kg/m³, with most values clustering near 943.9 kg/m³.

**Molar volume estimate (derived calculation):** Using the standard reference molar mass of DMF (73.09 g/mol; this value is general chemical knowledge, not from the ThermoML database) and the inspected density of 943.9 kg/m³ (= 0.9439 g/cm³) from GLOBlit_86 / PROPblock_6, the derived molar volume is approximately 77.4 cm³/mol (computed as 73.09 ÷ 0.9439; this result is a derived calculation, not a database datum).

This pure-component molar volume can be used as one input for estimating the molar volume of a ternary DMF + water + methanol mixture via ideal mixing or excess volume corrections, though the direct ternary volumetric data is not available in the ThermoML database (as established in the prior search).

**Core claims:**
- The ThermoML database reports the mass density of pure N,N-dimethylformamide (DMF) at 298.15 K as 943.81 kg/m³ (GLOBlit_228/PROPblock_4, 101.325 kPa) and 943.917 kg/m³ (GLOBlit_86/PROPblock_6, 101.0 kPa), with most inspected values clustering near 943.9 kg/m³.
- In GLOBlit_86/PROPblock_6, DMF density decreases monotonically and nearly linearly with temperature over 288.15–308.15 K, from 953.442 kg/m³ at 288.15 K to 934.357 kg/m³ at 308.15 K.
- Direct ternary volumetric data for DMF + water + methanol mixtures were not found in the ThermoML database.
- The molar mass of DMF (73.09 g/mol) and the derived molar volume (~77.4 cm³/mol) are not database values; they are external knowledge and a derived calculation, respectively, and are flagged as UNVERIFIED against the database.

**Core blocks found:**

**WM_L1#2_Blocks_(Query_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#1 | 「GLOBlit_228」 | 「PROPblock_4」 | 「GLOBcomp_18」 | 「GLOBprop_1」 | 「Mass density of pure DMF at 298.15 K and 101.325 kPa; single data point of 943.81 kg/m³.」 |
| WM_L1#2_Table#2 | 「GLOBlit_86」 | 「PROPblock_6」 | 「GLOBcomp_18」 | 「GLOBprop_1」 | 「Mass density of pure DMF over 288.15–308.15 K at 101.0 kPa; value at 298.15 K is 943.917 kg/m³.」 |

*Not stored here: 2 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(3) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNGROUNDED_LITERAL** PROPblock_6: 73.09 (near '…ulation):** Using the standard reference molar mass of DMF (…') matches no inspected row/stat, database table, or other source of PROPblock_6
- **UNGROUNDED_LITERAL** PROPblock_6: 77.4 (near '…, the derived molar volume is approximately 77.4 cm3/mol (co…') matches no inspected row/stat, database table, or other source of PROPblock_6
- **UNGROUNDED_LITERAL** PROPblock_6: 73.09 (near '…ved molar volume is approximately 77.4 cm3/mol (computed as …') matches no inspected row/stat, database table, or other source of PROPblock_6
### L1_query_3
**L1_query_3** — status: success · validation: FLAGGED(1)

**Summary:** In the ThermoML database at 298.15 K and 101.325 kPa, the pure-component liquid mass densities are: water (GLOBcomp_1) at 997.06 kg/m³ (GLOBlit_306 / PROPblock_6, DOI 10.1016/j.fluid.2005.09.009), and methanol (GLOBcomp_4) at 786.531 kg/m³ (GLOBlit_57 / PROPblock_1, DOI 10.1007/s10765-008-0395-z). Cross-checked database entries show water density in the 997.04–997.06 kg/m³ range and methanol density in the 786.4–786.63 kg/m³ range. Together with a previously established DMF density (from GLOBlit_86 / PROPblock_6, not re-inspected in this run), these three pure-component densities are intended for an ideal-mixing estimate of the molar volume of an equimolar DMF + water + methanol mixture at 298 K. The methanol value 786.531 kg/m³ was initially misattributed to PROPblock_6 but correctly belongs to GLOBlit_57::PROPblock_1.

**Answer:**

The ThermoML database provides the following pure-component mass density values at 298.15 K and 101.325 kPa:

**Water (GLOBcomp_1):**
- **997.06 kg/m³** at 298.15 K, 101.325 kPa
- Source: GLOBlit_306 / PROPblock_6 (DOI: 10.1016/j.fluid.2005.09.009), liquid phase, single data point
- This value is consistent across multiple independent blocks in the database (997.04–997.06 kg/m³ range observed in search results).

**Methanol (GLOBcomp_4):**
- **786.531 kg/m³** at 298.15 K, 101.325 kPa
- Source: GLOBlit_57 / PROPblock_1 (DOI: 10.1007/s10765-008-0395-z), liquid phase, single data point
- This value is consistent with other blocks in the database reporting methanol density at 298.15 K (786.4–786.63 kg/m³ range observed in search results).

These values, together with the previously established DMF density (from prior working memory result L1_query_2, GLOBlit_86 / PROPblock_6, not re-inspected in this run), provide the three pure-component densities needed for an ideal mixing estimate of the molar volume of an equimolar DMF + water + methanol mixture at 298 K.

**Core claims:**
- At 298.15 K and 101.325 kPa, the ThermoML database reports a pure-component liquid mass density of 997.06 kg/m³ for water (GLOBlit_306 / PROPblock_6), consistent with other database blocks in the 997.04–997.06 kg/m³ range.
- At 298.15 K and 101.325 kPa, the ThermoML database reports a pure-component liquid mass density of 786.531 kg/m³ for methanol (GLOBlit_57 / PROPblock_1), consistent with other database blocks in the 786.4–786.63 kg/m³ range.
- The methanol density value of 786.531 kg/m³ was initially misattributed to PROPblock_6 but was corrected to GLOBlit_57 / PROPblock_1 based on inspection during this run.
- These pure-component densities, together with a previously established DMF density not re-inspected in this run, are intended for an ideal mixing estimate of the molar volume of an equimolar DMF + water + methanol mixture at 298 K.

**Core blocks found:**

**WM_L1#3_Blocks_(Query_L1#3_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#3_Table#1 | 「GLOBlit_306」 | 「PROPblock_6」 | 「GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of pure water at 298.15 K and 101.325 kPa, reporting 997.06 kg/m³.」 |
| WM_L1#3_Table#2 | 「GLOBlit_57」 | 「PROPblock_1」 | 「GLOBcomp_4」 | 「GLOBprop_1」 | 「Mass density of pure methanol at 298.15 K and 101.325 kPa, reporting 786.531 kg/m³.」 |

*Not stored here: 2 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(1) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **MISATTRIBUTED_VALUE** PROPblock_6: 786.531 does not belong to PROPblock_6; it matches only GLOBlit_57::PROPblock_1 (inspected this run)
### L1_query_4
**L1_query_4** — status: partial · validation: FLAGGED(2)

**Summary:** No excess molar volume (VE) data for binary DMF + water exists in the ThermoML database at any temperature. Binary mass density data at 298.15 K are available from GLOBlit_11030 / PROPblock_4 (DOI: 10.1021/je700671t), comprising 14 data points spanning x_DMF = 0 to 1 at 101.0 kPa. Reported densities (kg/m³) at 298.15 K: x_DMF = 0, 997.04; 0.02, 996.39; 0.04, 996.31; 0.06, 996.53; 0.08, 996.80; 0.10, 997.03; 0.20, 996.13; 0.30, 991.40; 0.398, 984.18; 0.498, 976.64; 0.599, 968.96; 0.697, 961.92; 0.798, 955.63; 1.0, 944.60. At low DMF mole fractions (0 to ~0.10), density remains nearly constant at ~997 kg/m³ with a slight local minimum near x_DMF = 0.04, indicative of strong DMF–water hydrogen bonding and volume contraction (negative VE). Beyond x_DMF ≈ 0.2, density decreases monotonically toward pure DMF. No data point at exactly x_DMF = 0.333 was inspected; the nearest compositions are x_DMF = 0.300 (991.40 kg/m³) and x_DMF = 0.398 (984.18 kg/m³). Additional binary density blocks from GLOBlit_2584, GLOBlit_9855, and GLOBlit_4174 were identified but not inspected.

**Answer:**

#### Excess Molar Volume Data for Binary DMF + Water at 298.15 K

##### Direct VE Data: Not Available
No excess molar volume (GLOBprop_28) data exists in the ThermoML database for the binary DMF (GLOBcomp_18) + water (GLOBcomp_1) system at any temperature (searched 273–373 K). Zero blocks were returned.

##### Binary Density Data: Available
Mass density data for the binary DMF + water system at 298.15 K is available and could be used to derive excess molar volumes. The most comprehensive dataset is:

**GLOBlit_11030 / PROPblock_4** (DOI: 10.1021/je700671t)
- 210 total data points, 14 at 298.15 K, covering the full composition range (x_DMF = 0 to 1) at 101.0 kPa

Full 298.15 K isotherm (all 14 matched rows, from inspection INSP_3731e85c0b92):

**WM_L1#4_Table#1_(Query_L1#4_Answer):**

| *row_id* | *x_DMF* | *ρ (kg/m³)* |
|---|---|---|
| WM_L1#4_Table#1_Row#1 | 「0」 | 「997.04」 |
| WM_L1#4_Table#1_Row#2 | 「0.02」 | 「996.39」 |
| WM_L1#4_Table#1_Row#3 | 「0.04」 | 「996.31」 |
| WM_L1#4_Table#1_Row#4 | 「0.06」 | 「996.53」 |
| WM_L1#4_Table#1_Row#5 | 「0.08」 | 「996.80」 |
| WM_L1#4_Table#1_Row#6 | 「0.10」 | 「997.03」 |
| WM_L1#4_Table#1_Row#7 | 「0.20」 | 「996.13」 |
| WM_L1#4_Table#1_Row#8 | 「0.30」 | 「991.40」 |
| WM_L1#4_Table#1_Row#9 | 「0.398」 | 「984.18」 |
| WM_L1#4_Table#1_Row#10 | 「0.498」 | 「976.64」 |
| WM_L1#4_Table#1_Row#11 | 「0.599」 | 「968.96」 |
| WM_L1#4_Table#1_Row#12 | 「0.697」 | 「961.92」 |
| WM_L1#4_Table#1_Row#13 | 「0.798」 | 「955.63」 |
| WM_L1#4_Table#1_Row#14 | 「1.0」 | 「944.60」 |

**Nearest compositions to x_DMF = 0.333:** No data point at exactly x_DMF = 0.333 was inspected in this run. The two nearest inspected compositions are x_DMF = 0.300 (ρ = 991.40 kg/m³) and x_DMF = 0.398 (ρ = 984.18 kg/m³). A targeted nearest-value inspection was not completed due to the iteration limit.

##### Chemistry Insight
The density profile reveals notable non-ideal mixing behavior. At low DMF concentrations (x_DMF = 0 to ~0.10), the mixture density remains nearly constant at ~997 kg/m³ — essentially unchanged from pure water — and even shows a slight local minimum near x_DMF = 0.04 (996.31 kg/m³) followed by a recovery to 997.03 kg/m³ at x_DMF = 0.10. This plateau region is characteristic of strong DMF–water hydrogen bonding interactions that produce volume contraction (negative VE), partially offsetting the expected density decrease from adding the lighter DMF component. Beyond x_DMF ≈ 0.2, density decreases monotonically toward pure DMF (944.60 kg/m³).

To derive VE from these density data, one would need the pure-component molar masses (not stored in the ThermoML database) and apply the standard relation VE = V_mix − Σ(x_i · V_i*), where V_mix = Σ(x_i · M_i)/ρ_mix and V_i* = M_i/ρ_i*. The pure-component densities at 298.15 K from this same block are: ρ_water = 997.04 kg/m³ (x_DMF = 0) and ρ_DMF = 944.60 kg/m³ (x_DMF = 1).

##### Additional Binary DMF+Water Density Blocks at 298.15 K
The registry search identified additional blocks, but these were not individually inspected in this run, so only registry-level metadata (not data values) can be reported:
- GLOBlit_2584 / PROPblock_9 (DOI: 10.1016/j.jct.2005.07.012) — not inspected in this run
- GLOBlit_9855 / PROPblock_3 (DOI: 10.1021/je300358u) — not inspected in this run
- GLOBlit_4174 / PROPblock_19 (DOI: 10.1016/j.jct.2014.05.013) — not inspected in this run

These blocks could serve as cross-checks if inspected.

**Core claims:**
- No excess molar volume (VE) data for binary DMF + water exists in the ThermoML database at any temperature searched (273–373 K).
- Mass density data for binary DMF + water at 298.15 K are available from GLOBlit_11030 / PROPblock_4 (DOI: 10.1021/je300358u), comprising 14 data points spanning x_DMF = 0 to 1 at 101.0 kPa, with pure-component densities of 997.04 kg/m³ (water) and 944.60 kg/m³ (DMF).
- At low DMF mole fractions (x_DMF = 0 to ~0.10), the mixture density remains nearly constant at ~997 kg/m³ with a slight local minimum near x_DMF = 0.04 (996.31 kg/m³), indicative of non-ideal mixing and strong DMF–water hydrogen bonding interactions that produce volume contraction.
- Beyond x_DMF ≈ 0.2, density decreases monotonically toward pure DMF (944.60 kg/m³).
- No data point at exactly x_DMF = 0.333 was inspected; the two nearest inspected compositions are x_DMF = 0.300 (ρ = 991.40 kg/m³) and x_DMF = 0.398 (ρ = 984.18 kg/m³), and a targeted nearest-value inspection was not completed due to the iteration limit.
- Excess molar volumes could in principle be derived from the available density data using pure-component molar masses and the standard relation, but this derivation was not performed within the answer.

**Core blocks found:**

**WM_L1#4_Blocks_(Query_L1#4_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#4_Table#2 | 「GLOBlit_11030」 | 「PROPblock_4」 | 「GLOBcomp_18, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density data for binary DMF + water at 298.15 K covering x_DMF = 0 to 1 (14 points at 298.15 K, 101.0 kPa). No direct excess molar volume data found; density data can be used to derive VE.」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(2) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNINSPECTED_VALUE** PROPblock_4: 0.333 exists in PROPblock_4's database table but was never shown in an inspection of this run
- **UNINSPECTED_VALUE** PROPblock_4: 0.333 exists in PROPblock_4's database table but was never shown in an inspection of this run
### L1_query_5
**L1_query_5** — status: success · validation: FLAGGED(2)

**Summary:** Binary density data at 298.15 K and 101.0 kPa were retrieved for two systems. For DMF + methanol (GLOBlit_4125 / PROPblock_6, DOI 10.1016/j.jct.2014.02.021), 26 data points span x_DMF = 0 to 1 with density increasing monotonically from 786.58 kg/m³ (pure methanol) to 943.974 kg/m³ (pure DMF); near-equimolar density at x_DMF = 0.5002 is 894.978 kg/m³. Duplicate compositions (e.g., x_DMF = 0.1988/0.2004 and 0.4022/0.4054) show reproducibility within ~1 kg/m³. For water + methanol (GLOBlit_2825 / PROPblock_10, DOI 10.1016/j.jct.2007.05.004), 13 data points span x_water = 0 to 1 with density increasing from 787.2 kg/m³ (pure methanol) to 997.05 kg/m³ (pure water); at x_water = 0.5003 the density is 881.69 kg/m³. The two independent pure methanol endpoints (786.58 and 787.2 kg/m³) agree within ~0.6 kg/m³, confirming cross-source consistency. Excess molar volume data for these two binary systems was not searched in this run. Additional candidate blocks were identified for both systems but were not inspected.

**Answer:**

#### Binary Density Data for DMF+Methanol and Water+Methanol at 298.15 K

##### 1. DMF + Methanol Binary System

**GLOBlit_4125 / PROPblock_6** (DOI: 10.1016/j.jct.2014.02.021)
- 26 data points at 298.15 K and 101.0 kPa, covering the full composition range (x_DMF = 0 to 1)
- Density increases monotonically from pure methanol to pure DMF

Inspected data points at 298.15 K (9 of 26 shown via RDP, inspection INSP_428715c8042d):

**WM_L1#5_Table#1_(Query_L1#5_Answer):**

| *row_id* | *x_DMF* | *ρ (kg/m³)* |
|---|---|---|
| WM_L1#5_Table#1_Row#1 | 「0」 | 「786.58」 |
| WM_L1#5_Table#1_Row#2 | 「0.1988」 | 「843.761」 |
| WM_L1#5_Table#1_Row#3 | 「0.2004」 | 「843.0」 |
| WM_L1#5_Table#1_Row#4 | 「0.4022」 | 「882.138」 |
| WM_L1#5_Table#1_Row#5 | 「0.4054」 | 「881.38」 |
| WM_L1#5_Table#1_Row#6 | 「0.5982」 | 「909.277」 |
| WM_L1#5_Table#1_Row#7 | 「0.6008」 | 「908.588」 |
| WM_L1#5_Table#1_Row#8 | 「0.9033」 | 「936.655」 |
| WM_L1#5_Table#1_Row#9 | 「1.0」 | 「943.974」 |

**Nearest composition to equimolar (x_DMF = 0.5):** A targeted nearest-value inspection (INSP_2a46f0d6e4fd) found no row at exactly x_DMF = 0.5. The nearest row is at x_DMF = 0.5002 (ρ = 894.978 kg/m³), with the nearest row below at x_DMF = 0.4986. The bracket confirms the block contains data very close to equimolar.

Stats (full block, n=26): x_DMF 0–1; ρ 786.58–943.974 kg/m³.

A second block was also identified in the search: **GLOBlit_10930 / PROPblock_8** (DOI: 10.1021/je700430g), but it was not inspected in this run and no data values from it can be reported.

---

##### 2. Water + Methanol Binary System

**GLOBlit_2825 / PROPblock_10** (DOI: 10.1016/j.jct.2007.05.004)
- 13 data points at 298.15 K and 101.0 kPa, covering the full composition range (x_water = 0 to 1)
- Density increases monotonically from pure methanol to pure water

Inspected data points at 298.15 K (12 of 13 shown, inspection INSP_5d31e929df24):

**WM_L1#5_Table#2_(Query_L1#5_Answer):**

| *row_id* | *x_water* | *ρ (kg/m³)* |
|---|---|---|
| WM_L1#5_Table#2_Row#1 | 「0」 | 「787.2」 |
| WM_L1#5_Table#2_Row#2 | 「0.049」 | 「795.47」 |
| WM_L1#5_Table#2_Row#3 | 「0.0993」 | 「804.11」 |
| WM_L1#5_Table#2_Row#4 | 「0.1973」 | 「821.73」 |
| WM_L1#5_Table#2_Row#5 | 「0.2983」 | 「840.79」 |
| WM_L1#5_Table#2_Row#6 | 「0.3985」 | 「860.59」 |
| WM_L1#5_Table#2_Row#7 | 「0.5003」 | 「881.69」 |
| WM_L1#5_Table#2_Row#8 | 「0.5994」 | 「902.96」 |
| WM_L1#5_Table#2_Row#9 | 「0.7986」 | 「947.17」 |
| WM_L1#5_Table#2_Row#10 | 「0.8999」 | 「969.84」 |
| WM_L1#5_Table#2_Row#11 | 「0.9512」 | 「982.53」 |
| WM_L1#5_Table#2_Row#12 | 「1.0」 | 「997.05」 |

**Near-equimolar composition:** At x_water = 0.5003, the density is 881.69 kg/m³. The corresponding methanol mole fraction of approximately 0.4997 is derived by simple arithmetic (1 − 0.5003), not a database datum.

Stats (matched at 298.15 K, n=13): x_water 0–1; ρ 787.2–997.05 kg/m³.

Several additional water+methanol density blocks were identified in the search (GLOBlit_2432, GLOBlit_8424, GLOBlit_10866, GLOBlit_7085, GLOBlit_8888, GLOBlit_8869, GLOBlit_9571) but were not inspected in this run.

---

##### Chemistry Insight

Both binary systems show monotonically increasing density from pure methanol toward the heavier component (DMF or water), but the curvature differs:

- **DMF + methanol (GLOBlit_4125 / PROPblock_6):** Density increases relatively smoothly from 786.58 kg/m³ (pure methanol) to 943.974 kg/m³ (pure DMF). The duplicate measurements at similar compositions (e.g., x_DMF = 0.1988/0.2004 and 0.4022/0.4054) show good reproducibility (differences < 1 kg/m³).

- **Water + methanol (GLOBlit_2825 / PROPblock_10):** Density increases from 787.2 kg/m³ (pure methanol) to 997.05 kg/m³ (pure water). This system is well known for significant negative excess volumes due to strong hydrogen bonding between water and methanol, which would manifest as densities higher than ideal mixing predictions.

##### Excess Molar Volume Data

Excess molar volume (GLOBprop_28) data was not specifically searched for these two binary systems in this run. The prior working memory established that no VE data exists for binary DMF + water in the ThermoML database. If VE data for DMF+methanol or water+methanol is needed, a separate search would be required.

##### Pure-Component Density Cross-Check

The endpoint densities from the two binary blocks inspected in this run are mutually consistent:

**From GLOBlit_4125 / PROPblock_6 (DMF + methanol, this run):**
- Pure methanol (x_DMF = 0): 786.58 kg/m³
- Pure DMF (x_DMF = 1.0): 943.974 kg/m³

**From GLOBlit_2825 / PROPblock_10 (water + methanol, this run):**
- Pure methanol (x_water = 0): 787.2 kg/m³
- Pure water (x_water = 1.0): 997.05 kg/m³

The two independent pure methanol endpoints (786.58 and 787.2 kg/m³) agree within ~0.6 kg/m³, confirming consistency across sources.

Prior working memory queries (L1_query_2 and L1_query_3) reported pure-component densities from other blocks (GLOBlit_57 / PROPblock_1 for methanol, GLOBlit_86 / PROPblock_6 for DMF, GLOBlit_306 / PROPblock_6 for water); those values were not re-inspected in this run and are not re-quoted here — see the prior results for details.

**Core claims:**
- At 298.15 K and 101.0 kPa, the density of the DMF + methanol binary system (GLOBlit_4125 / PROPblock_6, 26 data points) increases monotonically from 786.58 kg/m³ (pure methanol, x_DMF = 0) to 943.974 kg/m³ (pure DMF, x_DMF = 1.0), with a near-equimolar value of 894.978 kg/m³ at x_DMF = 0.5002.
- At 298.15 K and 101.0 kPa, the density of the water + methanol binary system (GLOBlit_2825 / PROPblock_10, 13 data points) increases monotonically from 787.2 kg/m³ (pure methanol, x_water = 0) to 997.05 kg/m³ (pure water, x_water = 1.0), with a near-equimolar value of 881.69 kg/m³ at x_water = 0.5003.
- The two independent pure methanol density endpoints from the two binary blocks (786.58 kg/m³ from GLOBlit_4125/PROPblock_6 and 787.2 kg/m³ from GLOBlit_2825/PROPblock_10) agree within ~0.6 kg/m³, confirming cross-source consistency.
- Duplicate measurements at similar compositions in the DMF + methanol block show good reproducibility with differences less than 1 kg/m³.
- Excess molar volume data for these two binary systems was not searched for in this run, and no VE values are reported.

**Core blocks found:**

**WM_L1#5_Blocks_(Query_L1#5_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#5_Table#3 | 「GLOBlit_4125」 | 「PROPblock_6」 | 「GLOBcomp_4, GLOBcomp_18」 | 「GLOBprop_1」 | 「Composition-dependent mass density for DMF + methanol at 298.15 K and 101.0 kPa, 26 data points covering x_DMF = 0 to 1, ρ = 786.58–943.974 kg/m³.」 |
| WM_L1#5_Table#4 | 「GLOBlit_2825」 | 「PROPblock_10」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Composition-dependent mass density for water + methanol at 298.15 K and 101.0 kPa, 13 data points covering x_water = 0 to 1, ρ = 787.2–997.05 kg/m³.」 |

*Not stored here: 3 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(2) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNGROUNDED_LITERAL** PROPblock_10: 0.4997 (near '…. The corresponding methanol mole fraction of approximately …') matches no inspected row/stat, database table, or other source of PROPblock_10
- **MISATTRIBUTED_VALUE** PROPblock_10: 786.58 does not belong to PROPblock_10; it matches only GLOBlit_4125::PROPblock_6 (inspected this run)


