# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_063038_572233_a4c050bb`

### ID Catalog
| type | global_id | name | pure_values |
|------|--------|------|-------------|
| comp | GLOBcomp_1 | water | 994.05 |
| comp | GLOBcomp_2 | ethanol | 776.51 |
| prop | GLOBprop_1 | massdensitykgm3 |  |
| var | GLOBvar_2 | molefraction<water> |  |
| var | GLOBvar_1 | temperaturek |  |
| constr | GLOBconstr_1 | pressurekpa |  |

### History
- [query_thermoml]
- [inspect_block]
- [fit_block] ERROR: Requested x column 'Mole fraction of water' not found in block
- [fit_block] ERROR: No pure values given and the block's composition coverage is insufficient to ext
- [query_thermoml_parallel]
- [fit_block]
- [predict_from_rk]
- [predict_from_rk]
- [list_session_files]
- [predict_from_rk]
- [predict_from_rk]
- [query_thermoml]

### Query Results
#### query
**L1_query_1** — status: success · validation: FLAGGED(2)

**Summary:** Sixteen binary ethanol–water mass-density (GLOBprop_1) blocks were identified in the 305–315 K window. Five were inspected in detail. The strongest candidate is GLOBlit_11136 / PROPblock_9 (DOI 10.1021/je800150h): 108 data points spanning x(water) 0.1–0.9 over T = 268.1–323.15 K at 101.0 kPa, with representative densities from 774.3 kg/m³ (x(water)=0.1, 323.15 K) to 977.3 kg/m³ (x(water)=0.9, 268.1 K). The second-best is GLOBlit_10699 / PROPblock_6 (DOI 10.1021/je600565m): 18 points at x(water) 0.0998–0.9051 measured at 298.15 K and 318.15 K (101.0 kPa), with densities at 318.15 K ranging from 780.53 kg/m³ (x(water)=0.1) to 952.47 kg/m³ (x(water)=0.9). Additional candidates include GLOBlit_8050 / PROPblock_5 (DOI 10.1021/je020173z, 24 points, w(ethanol) 0.10835–0.71144, 298.15–313.15 K, 101.3 kPa), GLOBlit_11792 / PROPblock_3 (DOI 10.1021/je900743e, 15 points, w(ethanol) 0.1–0.5, 293.15–313.15 K, 101.0 kPa), and GLOBlit_7085 / PROPblock_7 (DOI 10.1021/acs.jced.6b01058, 12 points, w(ethanol) 0.04–0.16, 298.15–313.15 K, 85.0 kPa). Resolved component IDs: ethanol = GLOBcomp_2 (C₂H₆O), water = GLOBcomp_1 (H₂O). The reference to 310 K throughout is the user's query target, not a measured database temperature.

**Answer:**

#### Density Data for Binary Ethanol–Water Mixtures near 310 K

Sixteen binary ethanol–water mass density (GLOBprop_1) blocks were found in the 305–315 K temperature window. The five most useful candidates, all verified by inspection, are summarized below. The target temperature of 310 K referenced throughout is the user's query condition, not a database measurement temperature.

##### Inspected Candidates

**WM_L1#1_Table#1_(Analysis_L1#1_Answer):**

| *row_id* | *DOI* | *Block* | *GLOBlit* | *Total Points* | *T range (K)* | *Composition range* | *ρ range (kg/m³)* | *Pressure (kPa)* | *Comp. variable* |
|---|---|---|---|---|---|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「10.1021/je600565m」 | 「PROPblock_6」 | 「GLOBlit_10699」 | 「18」 | 「298.15–318.15」 | 「x(water) 0.0998–0.9051」 | 「780.53–965.51」 | 「101.0」 | 「GLOBvar_2 (mole fraction)」 |
| WM_L1#1_Table#1_Row#2 | 「10.1021/je800150h」 | 「PROPblock_9」 | 「GLOBlit_11136」 | 「108」 | 「268.1–323.15」 | 「x(water) 0.1–0.9」 | 「774.3–977.3」 | 「101.0」 | 「GLOBvar_2 (mole fraction)」 |
| WM_L1#1_Table#1_Row#3 | 「10.1021/je020173z」 | 「PROPblock_5」 | 「GLOBlit_8050」 | 「24」 | 「298.15–313.15」 | 「w(ethanol) 0.10835–0.71144」 | 「848.29–979.29」 | 「101.3」 | 「GLOBvar_5 (mass fraction)」 |
| WM_L1#1_Table#1_Row#4 | 「10.1021/je900743e」 | 「PROPblock_3」 | 「GLOBlit_11792」 | 「15」 | 「293.15–313.15」 | 「w(ethanol) 0.1–0.5」 | 「897.6–981.8」 | 「101.0」 | 「GLOBvar_5 (mass fraction)」 |
| WM_L1#1_Table#1_Row#5 | 「10.1021/acs.jced.6b01058」 | 「PROPblock_7」 | 「GLOBlit_7085」 | 「12」 | 「298.15–313.15」 | 「w(ethanol) 0.04–0.16」 | 「966.4–990.13」 | 「85.0」 | 「GLOBvar_5 (mass fraction)」 |

##### Best Picks for Wide Composition Coverage

1. **GLOBlit_11136 / PROPblock_9** (DOI: 10.1021/je800150h) — **Largest dataset with wide composition**: 108 data points spanning x(water) 0.1–0.9 across T = 268.1–323.15 K at 101.0 kPa. This block covers nearly the full composition range and a broad temperature window that brackets the user's target of 310 K. Representative inspected points at the temperature extremes:
   - x(water) = 0.1: ρ = 824.9 kg/m³ (268.1 K) to 774.3 kg/m³ (323.15 K)
   - x(water) = 0.9: ρ = 977.3 kg/m³ (268.1 K) to 942 kg/m³ (323.15 K)

2. **GLOBlit_10699 / PROPblock_6** (DOI: 10.1021/je600565m) — **Widest mole-fraction range at two temperatures**: 18 points at x(water) 0.0998–0.9051, measured at 298.15 K and 318.15 K (101.0 kPa). The 318.15 K isotherm is the closer of the two to the user's target of 310 K. Representative inspected points at 318.15 K:
   - x(water) = 0.1: ρ = 780.53 kg/m³
   - x(water) = 0.5003: ρ = 840.31 kg/m³
   - x(water) = 0.9: ρ = 952.47 kg/m³

3. **GLOBlit_8050 / PROPblock_5** (DOI: 10.1021/je020173z) — **Wide mass-fraction range**: 24 points with w(ethanol) 0.10835–0.71144 at 298.15 K and 313.15 K (101.3 kPa). At 313.15 K:
   - w(ethanol) = 0.16716: ρ = 964.04 kg/m³
   - w(ethanol) = 0.44202: ρ = 911.19 kg/m³
   - w(ethanol) = 0.71144: ρ = 848.29 kg/m³

4. **GLOBlit_11792 / PROPblock_3** (DOI: 10.1021/je900743e) — 15 points at w(ethanol) 0.1–0.5 across 293.15–313.15 K (101.0 kPa). At 313.15 K:
   - w(ethanol) = 0.1: ρ = 974.6 kg/m³
   - w(ethanol) = 0.5: ρ = 897.6 kg/m³

5. **GLOBlit_7085 / PROPblock_7** (DOI: 10.1021/acs.jced.6b01058) — 12 points but narrow composition (w(ethanol) 0.04–0.16) at 298.15–313.15 K. Note: measured at 85.0 kPa rather than atmospheric pressure. At 308.15 K:
   - w(ethanol) = 0.04: ρ = 987.24 kg/m³
   - w(ethanol) = 0.16: ρ = 968.6 kg/m³

##### Resolved IDs
- Ethanol: GLOBcomp_2 (C₂H₆O)
- Water: GLOBcomp_1 (H₂O)
- Mass density: GLOBprop_1

**GLOBlit_11136 / PROPblock_9** is the strongest overall candidate, offering 108 data points across x(water) 0.1–0.9 and a temperature range (268.1–323.15 K) that densely brackets the user's query target. **GLOBlit_10699 / PROPblock_6** provides the widest single-isotherm composition sweep (x(water) 0.0998–0.9051) but at only two temperatures (298.15 K and 318.15 K).

**Core claims:**
- Sixteen binary ethanol–water mass density data blocks were found in the ThermoML database within the 305–315 K temperature window, and five were inspected in detail.
- GLOBlit_11136 / PROPblock_9 (DOI: 10.1021/je800150h) is the strongest overall candidate, offering 108 data points across x(water) 0.1–0.9 and T = 268.1–323.15 K at 101.0 kPa, densely bracketing the query target of 310 K.
- GLOBlit_10699 / PROPblock_6 (DOI: 10.1021/je600565m) provides the widest single-isotherm composition sweep (x(water) 0.0998–0.9051) but at only two temperatures (298.15 K and 318.15 K) at 101.0 kPa.
- GLOBlit_8050 / PROPblock_5 (DOI: 10.1021/je020173z) covers w(ethanol) 0.10835–0.71144 at 298.15 K and 313.15 K (101.3 kPa), with 24 data points.
- GLOBlit_11792 / PROPblock_3 (DOI: 10.1021/je900743e) covers w(ethanol) 0.1–0.5 across 293.15–313.15 K (101.0 kPa), with 15 data points.
- GLOBlit_7085 / PROPblock_7 (DOI: 10.1021/acs.jced.6b01058) covers only a narrow composition range (w(ethanol) 0.04–0.16) and was measured at 85.0 kPa rather than atmospheric pressure.
- No dataset contains measurements exactly at 310 K; the value 310 K is the user's query target, not a database measurement temperature, and this is flagged as UNGROUNDED_LITERAL for both PROPblock_9 and PROPblock_6.

**Core blocks found:**

**WM_L1#1_Blocks_(Analysis_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#2 | 「GLOBlit_11136」 | 「PROPblock_9」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of binary ethanol–water mixture; 108 points, T = 268.1–323.15 K, x(water) 0.1–0.9, 101.0 kPa.」 |
| WM_L1#1_Table#3 | 「GLOBlit_10699」 | 「PROPblock_6」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of binary ethanol–water mixture; 18 points, T = 298.15–318.15 K, x(water) 0.0998–0.9051, 101.0 kPa.」 |
| WM_L1#1_Table#4 | 「GLOBlit_8050」 | 「PROPblock_5」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of binary ethanol–water mixture; 24 points, T = 298.15–313.15 K, w(ethanol) 0.10835–0.71144, 101.3 kPa.」 |
| WM_L1#1_Table#5 | 「GLOBlit_11792」 | 「PROPblock_3」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of binary ethanol–water mixture; 15 points, T = 293.15–313.15 K, w(ethanol) 0.1–0.5, 101.0 kPa.」 |
| WM_L1#1_Table#6 | 「GLOBlit_7085」 | 「PROPblock_7」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of binary ethanol–water mixture; 12 points, T = 298.15–313.15 K, w(ethanol) 0.04–0.16, 85.0 kPa.」 |

*Not stored here: 5 verbatim data_inspections table(s); 3 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(2) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNGROUNDED_LITERAL** PROPblock_9: 310 (near '…broad temperature window that brackets the user's target of …') matches no inspected row/stat, database table, or other source of PROPblock_9
- **UNGROUNDED_LITERAL** PROPblock_6: 310 (near '…K isotherm is the closer of the two to the user's target of …') matches no inspected row/stat, database table, or other source of PROPblock_6


#### pure_water_density_310K
**L1_query_2** — status: success · validation: PASS

**Summary:** Pure water density near 310 K was identified in the ThermoML database from DOI 10.1016/j.fluid.2010.01.002 (GLOBlit_779, PROPblock_18), measured by the vibrating tube method at atmospheric pressure (101.325 kPa). No exact data point at 310 K exists in this block; the two nearest bracketing points are 308.15 K with a mass density of 994.05 kg/m³ and 318.15 K with a mass density of 990.24 kg/m³. The closest measured point to 310 K is at 308.15 K, where the mass density of pure water is 994.05 kg/m³ with an uncertainty of ±0.04 kg/m³. Density decreases monotonically with temperature in this range.

**Answer:**

Pure water density near 310 K was found in the ThermoML database from DOI 10.1016/j.fluid.2010.01.002 (GLOBlit_779, PROPblock_18), measured by the vibrating tube method at atmospheric pressure (101.325 kPa).

There is no exact data point at 310 K in this block. The two nearest temperature points bracket 310 K:

**WM_L1#2_Table#1_(Analysis_L1#2_Answer):**

| *row_id* | *Temperature (K)* | *Pressure (kPa)* | *Mass Density (kg/m³)* |
|---|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「308.15」 | 「101.325」 | 「994.05」 |
| WM_L1#2_Table#1_Row#2 | 「318.15」 | 「101.325」 | 「990.24」 |

The closest measured point to 310 K is at **308.15 K**, where the mass density of pure water is **994.05 kg/m³** (uncertainty ±0.04 kg/m³). The density decreases monotonically with temperature in this range (near-linear, R² = 0.9909), consistent with the well-known thermal expansion behavior of liquid water above its density maximum (which occurs near 4 °C, a general physical chemistry fact, not a datum from this database).

**Source:** GLOBlit_779, DOI 10.1016/j.fluid.2010.01.002, PROPblock_18 (unary water system).

**Core claims:**
- No exact data point at 310 K was found; the two nearest bracketing points from DOI 10.1016/j.fluid.2010.01.002 are 308.15 K (mass density 994.05 kg/m³, ±0.04 kg/m³) and 318.15 K (mass density 990.24 kg/m³), both at 101.325 kPa for pure water measured by the vibrating tube method.
- The closest measured point to 310 K is at 308.15 K, where the mass density of pure water is 994.05 kg/m³ (±0.04 kg/m³) at atmospheric pressure.
- Density decreases monotonically with temperature between 308.15 K and 318.15 K, consistent with thermal expansion behavior of liquid water above its density maximum.

**Core blocks found:**

**WM_L1#2_Blocks_(Analysis_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#2 | 「GLOBlit_779」 | 「PROPblock_18」 | 「GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density measurements for pure water at atmospheric pressure (101.325 kPa) via vibrating tube method.」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### pure_ethanol_density_310K
**L1_query_3** — status: success · validation: PASS

**Summary:** Pure ethanol mass density near 310 K at atmospheric pressure (101.325 kPa) was found in DOI 10.1016/j.fluid.2005.10.022. No data point exists at exactly 310 K. The two nearest bracketing measured values are 776.51 kg/m³ at 308.15 K and 772.138 kg/m³ at 313.15 K. The closest single measured value to 310 K is 776.51 kg/m³ at 308.15 K. Density decreases monotonically with temperature in this range, so the density at exactly 310 K would lie between these two values (approximately 772–777 kg/m³), but no interpolated value is stated as a measured datum.

**Answer:**

Pure ethanol mass density near 310 K at atmospheric pressure was found in the ThermoML database in DOI 10.1016/j.fluid.2005.10.022 (GLOBlit_323, PROPblock_2).

No data point exists at exactly 310 K. The two nearest bracketing values at 101.325 kPa are:

**WM_L1#3_Table#1_(Analysis_L1#3_Answer):**

| *row_id* | *Temperature (K)* | *Mass Density (kg/m³)* |
|---|---|---|
| WM_L1#3_Table#1_Row#1 | 「308.15」 | 「776.51」 |
| WM_L1#3_Table#1_Row#2 | 「313.15」 | 「772.138」 |

The closest single value to 310 K is **776.51 kg/m³ at 308.15 K** (101.325 kPa), which is the nearest measured point below the target. Density decreases monotonically with temperature in this range, so the density at exactly 310 K would lie between these two values (approximately 772–777 kg/m³), but no interpolated value can be stated as a measured datum.

**Core claims:**
- No ThermoML data point exists at exactly 310 K for pure ethanol mass density at atmospheric pressure; the two nearest bracketing values at 101.325 kPa are 776.51 kg/m³ at 308.15 K and 772.138 kg/m³ at 313.15 K (from DOI 10.1016/j.fluid.2005.10.022), so the closest single measured value to 310 K is 776.51 kg/m³ at 308.15 K and 101.325 kPa.

**Core blocks found:**

**WM_L1#3_Blocks_(Analysis_L1#3_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#3_Table#2 | 「GLOBlit_323」 | 「PROPblock_2」 | 「GLOBcomp_2」 | 「GLOBprop_1」 | 「Mass density measurements for pure ethanol near 308–313 K at 101.325 kPa.」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### query
**L1_query_4** — status: success · validation: PASS

**Summary:** In DOI 10.1021/je800150h (GLOBlit_11136), PROPblock_9 reports mass density of binary ethanol + water mixtures at 101.0 kPa. The isotherm nearest 308.1 K is recorded at 308.15 K (the next lower isotherm is 303.15 K). At 308.15 K there are 9 data points spanning water mole fractions 0.1 to 0.9 in steps of 0.1. Density increases monotonically from 788.2 kg/m³ at x_water = 0.1 to 952.7 kg/m³ at x_water = 0.9. Intermediate values are 801.4 (0.2), 816 (0.3), 831.4 (0.4), 850.1 (0.5), 871.4 (0.6), 896.5 (0.7), and 923.8 (0.8) kg/m³. The full block contains 108 data points across 12 isotherms (268.1 K to 323.15 K) with 9 compositions each.

**Answer:**

Here are the measured data rows from PROPblock_9 of DOI 10.1021/je800150h (GLOBlit_11136) at the isotherm T = 308.15 K (the actual recorded temperature nearest to 308.1 K). This is a binary ethanol + water system at a fixed pressure of 101.0 kPa.

**WM_L1#4_Table#1_(Analysis_L1#4_Answer):**

| *row_id* | *BLKpoint_id* | *mole_fraction_<water>* | *temperature_k* | *pressure_kpa* | *mass_density_kg_m3* |
|---|---|---|---|---|---|
| WM_L1#4_Table#1_Row#1 | 「BLKpoint_9」 | 「0.1」 | 「308.15」 | 「101.0」 | 「788.2」 |
| WM_L1#4_Table#1_Row#2 | 「BLKpoint_21」 | 「0.2」 | 「308.15」 | 「101.0」 | 「801.4」 |
| WM_L1#4_Table#1_Row#3 | 「BLKpoint_33」 | 「0.3」 | 「308.15」 | 「101.0」 | 「816」 |
| WM_L1#4_Table#1_Row#4 | 「BLKpoint_45」 | 「0.4」 | 「308.15」 | 「101.0」 | 「831.4」 |
| WM_L1#4_Table#1_Row#5 | 「BLKpoint_57」 | 「0.5」 | 「308.15」 | 「101.0」 | 「850.1」 |
| WM_L1#4_Table#1_Row#6 | 「BLKpoint_69」 | 「0.6」 | 「308.15」 | 「101.0」 | 「871.4」 |
| WM_L1#4_Table#1_Row#7 | 「BLKpoint_81」 | 「0.7」 | 「308.15」 | 「101.0」 | 「896.5」 |
| WM_L1#4_Table#1_Row#8 | 「BLKpoint_93」 | 「0.8」 | 「308.15」 | 「101.0」 | 「923.8」 |
| WM_L1#4_Table#1_Row#9 | 「BLKpoint_105」 | 「0.9」 | 「308.15」 | 「101.0」 | 「952.7」 |

**Key observations:**
- The actual temperature recorded in the block is **308.15 K**, not 308.1 K. The bracketing analysis confirmed there is no row at exactly 308.1 K; the nearest below is 303.15 K and the nearest above is 308.15 K.
- There are **9 data points** at this isotherm, spanning water mole fractions from 0.1 to 0.9 in steps of 0.1.
- Density increases monotonically with water mole fraction, from **788.2 kg/m³** (x_water = 0.1, ethanol-rich) to **952.7 kg/m³** (x_water = 0.9, water-rich), consistent with the higher density of pure water relative to pure ethanol.
- The full block contains **108 data points** across temperatures from 268.1 K to 323.15 K, with 12 isotherms × 9 compositions each.

**Core claims:**
- In PROPblock_9 of DOI 10.1021/je800150h, the nearest recorded isotherm to 308.1 K is 308.15 K; no row at exactly 308.1 K exists in the block.
- At 308.15 K and 101.0 kPa for the binary ethanol + water system, there are 9 data points spanning water mole fractions from 0.1 to 0.9 in steps of 0.1.
- At 308.15 K and 101.0 kPa, the mass density increases monotonically with water mole fraction, from 788.2 kg/m³ at x_water = 0.1 to 952.7 kg/m³ at x_water = 0.9.
- The full block contains 108 data points across temperatures from 268.1 K to 323.15 K, with 12 isotherms × 9 compositions each.

**Core blocks found:**

**WM_L1#4_Blocks_(Analysis_L1#4_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#4_Table#2 | 「GLOBlit_11136」 | 「PROPblock_9」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density measurements for binary ethanol + water system at 101.0 kPa across 12 isotherms (268.1–323.15 K) and 9 water mole fractions (0.1–0.9); 108 data points total. Inspected rows at T = 308.15 K show density ranging from 788.2 to 952.7 kg/m³.」 |

*Not stored here: 2 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


### Inspected Blocks
- GLOBlit_11136 | 10.1021/je800150h | PROPblock_9: 108 rows; x=['mole_fraction_<water>']; y=['mass_density_kg_m3']
    - BLKprop_1 / GLOBprop_1: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_1: kind=direct; materialize_reference=False; supported=True; units=kg/m3 -> kg/m3

### Completed Fits
  - 10.1021/je800150h/PROPblock_9 (water, ethanol): RK order=5, R²=0.999626, RMSE=0.1584208739800725, coeffs=[-141.929336, -39.640763, 42.98294, 31.764762, -121.839727, -113.837423]
      response: direct via X = reported X | 0 reference source(s) | kg/m3 -> kg/m3
      pure refs: water=994.05, ethanol=776.51 [named (matched to composition axis)]
      fit_csv: $ROOT/data\10_1021_je800150h_BPROPblock_9_T308.1_fit.csv
      excess_csv: $ROOT/data\10_1021_je800150h_BPROPblock_9_T308.1_excess.csv
      fit_plot: $ROOT/plots\10_1021_je800150h_BPROPblock_9_T308.1_fit.png
      excess_plot: $ROOT/plots\10_1021_je800150h_BPROPblock_9_T308.1_excess.png

## Session Output Files

### data
- `$ROOT/data\10_1021_je800150h_BPROPblock_9_T308.1_fit.csv` — RK fit data — 10.1021/je800150h PROPblock_9_T308.1
- `$ROOT/data\10_1021_je800150h_BPROPblock_9_T308.1_excess.csv` — Excess property — 10.1021/je800150h PROPblock_9_T308.1

### plot
- `$ROOT/plots\10_1021_je800150h_BPROPblock_9_T308.1_fit.png` — RK fit plot — 10.1021/je800150h PROPblock_9_T308.1
- `$ROOT/plots\10_1021_je800150h_BPROPblock_9_T308.1_excess.png` — Excess plot — 10.1021/je800150h PROPblock_9_T308.1

