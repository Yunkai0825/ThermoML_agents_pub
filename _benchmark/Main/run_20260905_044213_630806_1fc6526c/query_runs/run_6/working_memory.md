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
- [L1] Find blocks with excess molar enthalpy (HE) data for water + DMSO near 298.15 K → stored as L1_query_1 · validation: FLAGGED(1)

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: no_results · validation: FLAGGED(1)

**Summary:** A search of the ThermoML database for excess molar enthalpy (HE) data for the binary system water + dimethyl sulfoxide (DMSO) found no blocks containing this specific property for this compound pair. The water + DMSO system is represented by 29 property blocks across 16 papers (1,601 data points), but the available properties cover mass density, speed of sound, viscosity, solid-liquid equilibrium temperature, boiling temperature, mole fraction, molar heat capacity, apparent molar heat capacity, molar enthalpy of solution, and thermal conductivity — none of which is the excess molar enthalpy of mixing. The closest related measurement is a molar enthalpy of solution block (dissolution of water into DMSO at very low concentration) from DOI 10.1016/j.tca.2011.09.009 at 298.15 K, which is distinct from composition-dependent HE data. No HE vs. mole fraction curves for this system near 298.15 K are available in the ThermoML holdings searched.

**Answer:**

#### Excess Molar Enthalpy (HE) Data for Water + DMSO near 298.15 K

##### Summary

A thorough search of the ThermoML database for **excess molar enthalpy (HE, GLOBprop_17)** data for the binary system **water (GLOBcomp_1) + dimethyl sulfoxide (GLOBcomp_31)** found **no blocks** containing this specific property for this compound pair. This was confirmed across multiple search strategies including declared binary scope, subsystem scope, and broad unfiltered searches.

##### What Was Found

The water + DMSO binary system is well-represented in the database with **29 property blocks across 16 papers (1,601 data points)** spanning T = 253.15–393.15 K. However, the available properties are:

**WM_L1_Q1_Table#1_(Query_L1_Q1_Answer):**

| *row_id* | *Property* | *Number of Blocks* |
|---|---|---|
| WM_L1_Q1_Table#1_Row#1 | 「Mass density (kg/m³)」 | 「9」 |
| WM_L1_Q1_Table#1_Row#2 | 「Speed of sound (m/s)」 | 「3」 |
| WM_L1_Q1_Table#1_Row#3 | 「Viscosity (Pa·s)」 | 「3」 |
| WM_L1_Q1_Table#1_Row#4 | 「Solid-liquid equilibrium temperature (K)」 | 「3」 |
| WM_L1_Q1_Table#1_Row#5 | 「Boiling temperature at pressure P (K)」 | 「2」 |
| WM_L1_Q1_Table#1_Row#6 | 「Mole fraction」 | 「2」 |
| WM_L1_Q1_Table#1_Row#7 | 「Molar heat capacity at constant pressure (J/K/mol)」 | 「1」 |
| WM_L1_Q1_Table#1_Row#8 | 「Apparent molar heat capacity (J/K/mol)」 | 「1」 |
| WM_L1_Q1_Table#1_Row#9 | 「Molar enthalpy of solution (kJ/mol)」 | 「1」 |
| WM_L1_Q1_Table#1_Row#10 | 「Thermal conductivity (W/m/K)」 | 「1」 |

##### Closest Related Data

The closest enthalpy-related measurement found is a **molar enthalpy of solution (GLOBprop_15)** block:

- **Literature:** GLOBlit_5958, DOI: 10.1016/j.tca.2011.09.009
- **Block:** PROPblock_1
- **System:** Water (solute) dissolved in DMSO (solvent)
- **Method:** Isoperibol calorimetry (GLOBmeas_144)
- **Data points:** 1
- **Conditions:** 298.15 K, 101.0 kPa (per search_blocks result; *not inspected at row level in this run*)

This is an enthalpy of solution measurement (dissolution of water into DMSO at very low concentration), which is related to but distinct from the excess molar enthalpy of mixing across the full composition range.

##### Conclusion

**No composition-dependent excess molar enthalpy (HE) data for water + DMSO is available in the ThermoML database.** The database does not contain HE vs. mole fraction curves for this system near 298.15 K. The well-known strongly exothermic mixing behavior of water + DMSO (with an HE minimum near x(DMSO) ≈ 0.3–0.4) is documented in the broader literature but is not captured in the ThermoML holdings searched here.

**Core claims:**
- No composition-dependent excess molar enthalpy (HE) data for the binary system water + dimethyl sulfoxide (DMSO) is available in the ThermoML database near 298.15 K.
- The water + DMSO system is represented in the ThermoML database by 29 property blocks across 16 papers (1,601 data points, T = 253.15–393.15 K), but these cover other properties such as mass density, speed of sound, viscosity, and solid-liquid equilibrium temperature, not excess molar enthalpy.
- The closest enthalpy-related measurement found is a molar enthalpy of solution block (GLOBprop_15, GLOBlit_5958, DOI: 10.1016/j.tca.2011.09.009) for water dissolved in DMSO at 298.15 K, which is related to but distinct from excess molar enthalpy of mixing across the full composition range.
- The specific conditions and data values quoted for the molar enthalpy of solution block were not verified by direct data inspection and carry an UNVERIFIED flag.

**Validation (final in-session gate):** FLAGGED(1) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNINSPECTED_BLOCK** PROPblock_1: PROPblock_1 is quoted with data values (298.15, 101.0, 298.15, 0.3, …) but was never inspected in this run


