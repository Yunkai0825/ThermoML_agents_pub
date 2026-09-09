# Working Memory

## ID Catalog
<!-- PROTECTED — never compacted. Auto-populated by catalog ops. -->
### Resolved Entities
| type | global_id | registry_id | name |
|------|--------|----|------|
| comp | GLOBcomp_952 | CAS:110-88-3 | 1,3,5-trioxane |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|
| lit | GLOBlit_3147 | 10.1016/j.jct.2009.08.015 | 2010-cib-ale-0 (mass density) |
| lit | GLOBlit_3168 | 10.1016/j.jct.2009.11.005 | 2010-cib--0 (partial molar volume) |
| lit | GLOBlit_8200 | 10.1021/je030243h | 2004-gru-has-0 (LLE temperature) |
| lit | GLOBlit_8573 | 10.1021/je050015i | 2005-alb-has-0 (VLE) |
| lit | GLOBlit_10066 | 10.1021/je301352v | 2013-cib--0 (speed of sound) |

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find all available property data for the binary system 1,3,5-trioxane + water in ThermoML → stored as L1_query_1 · validation: FLAGGED(2)

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: FLAGGED(2)

**Summary:** Six ThermoML property-data blocks were identified for the binary system 1,3,5-trioxane + water, drawn from four literature sources. Four blocks were inspected in detail; two (GLOBlit_8573::PROPblock_2 for gas-phase mole fraction and GLOBlit_10066::PROPblock_5 for speed of sound) were not inspected. (1) Mass density (GLOBprop_1, GLOBlit_3147::PROPblock_5, DOI 10.1016/j.jct.2009.08.015): 175 liquid-phase data points, T = 278.15–373.15 K, P = 101–530 kPa, molality 0.049773–0.42135 mol/kg. (2) Partial molar volume at infinite dilution (GLOBprop_84, GLOBlit_3168::PROPblock_5, DOI 10.1016/j.jct.2009.11.005): 25 liquid-phase data points at x(trioxane) = 0.0, T = 298.16–498.17 K, P = 2020–30070 kPa, values from 6.95×10⁻⁵ to 9.496×10⁻⁵ m³/mol. (3) LLE temperature (GLOBprop_20, GLOBlit_8200::PROPblock_1, DOI 10.1021/je030243h): 19 data points at P = 101.3 kPa, w(trioxane) 0.2037–0.8994, T = 301.28–321.01 K; the curve is non-monotonic with a maximum near w = 0.6159 (T = 319.53 K), consistent with an upper critical solution temperature phase diagram. (4) Vapor pressure (GLOBprop_5, GLOBlit_8573::PROPblock_1, DOI 10.1021/je050015i): 17 data points at T = 393–413.2 K, x(trioxane) 0.004–0.7619, pressures 226.8–450.1 kPa, with a pressure maximum near x(trioxane) ≈ 0.436 suggesting positive deviations from Raoult's law. (5) Gas-phase mole fraction (GLOBprop_2, GLOBlit_8573::PROPblock_2) complements the vapor pressure data but was not inspected. (6) Speed of sound (GLOBprop_8, GLOBlit_10066::PROPblock_5, DOI 10.1021/je301352v) was not inspected. No viscosity data were found for this system.

**Answer:**

#### Comprehensive Inventory of Property Data for the Binary System 1,3,5-Trioxane + Water in ThermoML

Six property data blocks were found across four literature sources, covering volumetric, phase-equilibrium, acoustic, and VLE properties. Four of the six blocks were inspected in this run; two blocks (GLOBlit_8573::PROPblock_2 and GLOBlit_10066::PROPblock_5) could not be inspected due to time constraints.

##### Block-by-Block Summary

**WM_L1#2_Table#1_(Query_L1#2_Answer):**

| *row_id* | *#* | *Property* | *GLOBprop* | *Block* | *GLOBlit* | *DOI* | *Data Points* | *T Range (K)* | *P Range (kPa)* | *Composition Range* | *Phase* |
|---|---|---|---|---|---|---|---|---|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「1」 | 「Mass density (kg/m³)」 | 「GLOBprop_1」 | 「PROPblock_5」 | 「GLOBlit_3147」 | 「10.1016/j.jct.2009.08.015」 | 「175」 | 「278.15–373.15」 | 「101–530」 | 「molality 0.049773–0.42135 mol/kg」 | 「Liquid」 |
| WM_L1#2_Table#1_Row#2 | 「2」 | 「Partial molar volume (m³/mol)」 | 「GLOBprop_84」 | 「PROPblock_5」 | 「GLOBlit_3168」 | 「10.1016/j.jct.2009.11.005」 | 「25」 | 「298.16–498.17」 | 「2020–30070」 | 「x(trioxane) = 0.0 (infinite dilution)」 | 「Liquid」 |
| WM_L1#2_Table#1_Row#3 | 「3」 | 「LLE temperature (K)」 | 「GLOBprop_20」 | 「PROPblock_1」 | 「GLOBlit_8200」 | 「10.1021/je030243h」 | 「19」 | 「301.28–321.01」 | 「101.3 (fixed)」 | 「w(trioxane): 0.2037–0.8994」 | 「Liquid mix 1+2」 |
| WM_L1#2_Table#1_Row#4 | 「4」 | 「Vapor pressure (kPa)」 | 「GLOBprop_5」 | 「PROPblock_1」 | 「GLOBlit_8573」 | 「10.1021/je050015i」 | 「17」 | 「393–413.2」 | 「226.8–450.1」 | 「x(trioxane): 0.004–0.7619」 | 「Liquid/Gas」 |
| WM_L1#2_Table#1_Row#5 | 「5」 | 「Mole fraction (gas phase)」 | 「GLOBprop_2」 | 「PROPblock_2」 | 「GLOBlit_8573」 | 「10.1021/je050015i」 | 「not inspected in this run」 | 「not inspected in this run」 | 「not inspected in this run」 | 「not inspected in this run」 | 「Gas/Liquid」 |
| WM_L1#2_Table#1_Row#6 | 「6」 | 「Speed of sound (m/s)」 | 「GLOBprop_8」 | 「PROPblock_5」 | 「GLOBlit_10066」 | 「10.1021/je301352v」 | 「not inspected in this run」 | 「not inspected in this run」 | 「not inspected in this run」 | 「not inspected in this run」 | 「Liquid」 |

##### Property Categories

**Volumetric properties (inspected):**
- **Mass density** (GLOBlit_3147::PROPblock_5): 175 data points spanning T = 278.15–373.15 K, P = 101–530 kPa, with molality of trioxane from 0.049773 to 0.42135 mol/kg. Density values range from 1.019 to 9.391 kg/m³. Representative points include density = 1.138 kg/m³ at 278.15 K / 0.049773 mol/kg and 8.415 kg/m³ at 298.15 K / 0.42135 mol/kg.
- **Partial molar volume at infinite dilution** (GLOBlit_3168::PROPblock_5): 25 data points at x(trioxane) = 0.0, spanning T = 298.16–498.17 K and P = 2020–30070 kPa. Partial molar volumes range from 6.95×10⁻⁵ to 9.496×10⁻⁵ m³/mol. At the lowest temperature (298.16 K, 15030 kPa), the value is 6.964×10⁻⁵ m³/mol; at the highest (498.16 K, 3000 kPa), it reaches 9.496×10⁻⁵ m³/mol, reflecting the expected thermal expansion.

**Phase equilibrium (inspected):**
- **Liquid-liquid equilibrium temperature** (GLOBlit_8200::PROPblock_1): 19 data points at fixed P = 101.3 kPa, with w(trioxane) from 0.2037 to 0.8994. LLE temperatures range from 301.28 to 321.01 K. The curve is non-monotonic, with the maximum near w = 0.6159 (T = 319.53 K), consistent with an upper critical solution temperature (UCST) phase diagram.
- **Vapor pressure** (GLOBlit_8573::PROPblock_1): 17 data points at T = 393–413.2 K, with x(trioxane) from 0.004 to 0.7619. Vapor pressures range from 226.8 to 450.1 kPa. At 413 K, the pressure reaches a maximum near x(trioxane) ≈ 0.436 (450.1 kPa), suggesting positive deviations from Raoult's law at intermediate compositions.

**VLE composition data (not inspected):**
- **Gas-phase mole fraction** (GLOBlit_8573::PROPblock_2): This block was not inspected in this run. It complements the vapor pressure data from the same DOI (10.1021/je050015i) and provides gas-phase composition data for the VLE.

**Acoustic property (not inspected):**
- **Speed of sound** (GLOBlit_10066::PROPblock_5): This block was not inspected in this run. It is reported in DOI 10.1021/je301352v.

##### Key Observations

- The density data (GLOBlit_3147) is the largest block with 175 points, covering both atmospheric (101 kPa) and elevated pressures (up to 530 kPa) over a wide temperature range.
- The partial molar volume data (GLOBlit_3168) provides high-pressure measurements at infinite dilution, useful for modeling solute-solvent interactions.
- The LLE data (GLOBlit_8200) maps the liquid-liquid miscibility boundary at atmospheric pressure, showing a non-monotonic UCST-type curve.
- The VLE data (GLOBlit_8573) provides paired vapor pressure and gas-phase composition measurements at elevated temperatures (393–413 K).
- No viscosity data was found for this binary system.

**Core claims:**
- Six property data blocks for the binary system 1,3,5-trioxane + water were identified across four ThermoML literature sources, covering mass density, partial molar volume at infinite dilution, liquid-liquid equilibrium temperature, vapor pressure, gas-phase mole fraction, and speed of sound.
- Mass density data (GLOBlit_3147::PROPblock_5) comprises 175 data points spanning T = 278.15–373.15 K, P = 101–530 kPa, and molality of trioxane from 0.049773 to 0.42135 mol/kg in the liquid phase.
- Partial molar volume at infinite dilution (GLOBlit_3168::PROPblock_5) comprises 25 data points at x(trioxane) = 0.0, spanning T = 298.16–498.17 K and P = 2020–30070 kPa, with values from 6.95×10⁻⁵ to 9.496×10⁻⁵ m³/mol, reflecting expected thermal expansion.
- Liquid-liquid equilibrium temperature data (GLOBlit_8200::PROPblock_1) comprises 19 data points at P = 101.3 kPa, with w(trioxane) from 0.2037 to 0.8994 and LLE temperatures from 301.28 to 321.01 K; the curve is non-monotonic with a maximum near w = 0.6159 (T = 319.53 K), consistent with an upper critical solution temperature (UCST) phase diagram.
- Vapor pressure data (GLOBlit_8573::PROPblock_1) comprises 17 data points at T = 393–413.2 K and x(trioxane) from 0.004 to 0.7619, with pressures from 226.8 to 450.1 kPa; a pressure maximum near x(trioxane) ≈ 0.436 (450.1 kPa) at 413 K suggests positive deviations from Raoult's law.
- Two blocks (GLOBlit_8573::PROPblock_2 for gas-phase mole fraction and GLOBlit_10066::PROPblock_5 for speed of sound) were not inspected due to time constraints, and no viscosity data was found for this binary system.

**Core blocks found:**

**WM_L1#2_Blocks_(Query_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#2 | 「GLOBlit_3147」 | 「PROPblock_5」 | 「GLOBcomp_952, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density (kg/m³) for 1,3,5-trioxane + water; 175 points, T = 278.15–373.15 K, P = 101–530 kPa, molality 0.049773–0.42135 mol/kg.」 |
| WM_L1#2_Table#3 | 「GLOBlit_3168」 | 「PROPblock_5」 | 「GLOBcomp_952, GLOBcomp_1」 | 「GLOBprop_84」 | 「Partial molar volume at infinite dilution (m³/mol) for 1,3,5-trioxane in water; 25 points, T = 298.16–498.17 K, P = 2020–30070 kPa.」 |
| WM_L1#2_Table#4 | 「GLOBlit_8200」 | 「PROPblock_1」 | 「GLOBcomp_952, GLOBcomp_1」 | 「GLOBprop_20」 | 「Liquid-liquid equilibrium temperature (K) for 1,3,5-trioxane + water; 19 points, T = 301.28–321.01 K, P = 101.3 kPa, w(trioxane) 0.2037–0.8994.」 |
| WM_L1#2_Table#5 | 「GLOBlit_8573」 | 「PROPblock_1」 | 「GLOBcomp_952, GLOBcomp_1」 | 「GLOBprop_5」 | 「Vapor pressure (kPa) for 1,3,5-trioxane + water; 17 points, T = 393–413.2 K, P = 226.8–450.1 kPa, x(trioxane) 0.004–0.7619.」 |
| WM_L1#2_Table#6 | 「GLOBlit_8573」 | 「PROPblock_2」 | 「GLOBcomp_952, GLOBcomp_1」 | 「GLOBprop_2」 | 「Gas-phase mole fraction for 1,3,5-trioxane + water VLE; not inspected in this run.」 |
| WM_L1#2_Table#7 | 「GLOBlit_10066」 | 「PROPblock_5」 | 「GLOBcomp_952, GLOBcomp_1」 | 「GLOBprop_8」 | 「Speed of sound (m/s) for 1,3,5-trioxane + water; not inspected in this run.」 |

*Not stored here: 4 verbatim data_inspections table(s); 1 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(2) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **AMBIGUOUS_VALUE** GLOBlit_10066::PROPblock_5: 393 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean
- **AMBIGUOUS_VALUE** GLOBlit_10066::PROPblock_5: 413 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean


