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
- [L1] Find blocks with excess molar volume (VE) data for water + DMSO near 298.15 K → stored as L1_query_1 · validation: PASS

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: no_results · validation: PASS

**Summary:** No excess molar volume (VE, GLOBprop_28) data exists in the ThermoML database for the binary system water (GLOBcomp_1) + DMSO (GLOBcomp_31). VE data for DMSO paired with other compounds (15 blocks) confirms the property ID is correct, but none involve water. For water + DMSO in the 290–310 K range, 16 blocks across 9 DOIs cover other properties: mass density (GLOBprop_1, 7 blocks), viscosity (GLOBprop_4, 2 blocks), speed of sound (GLOBprop_8, 1 block), apparent molar heat capacity (GLOBprop_64, 1 block), molar enthalpy of solution (GLOBprop_15, 1 block), thermal conductivity (GLOBprop_34, 1 block), and relative permittivity (GLOBprop_44). The available density data could in principle be used to compute VE if pure-component molar volumes are known, but no VE values are directly reported.

**Answer:**

**Excess molar volume (VE) data for water + DMSO: not found in the ThermoML database.**

A thorough search was conducted:

1. **Property ID confirmed:** Excess molar volume is GLOBprop_28 (m³/mol, VolumetricProp group).

2. **Direct VE search for water (GLOBcomp_1) + DMSO (GLOBcomp_31):** Zero blocks found — no excess molar volume data exists for this binary pair in the database, regardless of temperature range or system scope.

3. **VE data for DMSO with other solvents:** 15 VE blocks exist for DMSO paired with other compounds (e.g., GLOBcomp_264, GLOBcomp_419, GLOBcomp_728, etc.), primarily from DOI 10.1016/j.jct.2006.04.005 (GLOBlit_2686). These confirm the property ID is correct and VE data is catalogued for DMSO — just not with water.

4. **Available data for water + DMSO (searched in the 290–310 K range):** 16 blocks across 9 DOIs were found covering other properties:
   - **Mass density** (GLOBprop_1): 7 blocks — e.g., GLOBlit_2584/PROPblock_8, GLOBlit_2652/PROPblock_4, GLOBlit_2781/PROPblock_4, GLOBlit_2844/PROPblock_4, GLOBlit_7713/PROPblock_10, GLOBlit_11018/PROPblock_6, GLOBlit_11517/PROPblock_4
   - **Viscosity** (GLOBprop_4): 2 blocks
   - **Speed of sound** (GLOBprop_8): 1 block
   - **Apparent molar heat capacity** (GLOBprop_64): 1 block
   - **Molar enthalpy of solution** (GLOBprop_15): 1 block
   - **Thermal conductivity** (GLOBprop_34): 1 block
   - **Relative permittivity** (GLOBprop_44): available

**Chemistry note:** While VE is not directly available, the density data blocks listed above for this binary system could, in principle, be used to compute VE if pure-component molar volumes are known, since VE = Vmix − Σ xi·Vi*. No specific data values from these density blocks were inspected in this search.

**Core claims:**
- No excess molar volume (VE) data for the water + DMSO binary system exists in the ThermoML database, despite VE data being available for DMSO paired with other solvents and despite multiple other properties (mass density, viscosity, speed of sound, apparent molar heat capacity, molar enthalpy of solution, thermal conductivity, relative permittivity) being catalogued for water + DMSO.
- Mass density data for water + DMSO are available in the database (7 blocks across multiple literature sources in the 290–310 K range), which could in principle be used to compute VE if pure-component molar volumes are known, but no such computation was performed.

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


