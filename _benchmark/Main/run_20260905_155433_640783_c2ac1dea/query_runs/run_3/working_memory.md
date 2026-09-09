# Working Memory

## ID Catalog
<!-- PROTECTED — never compacted. Auto-populated by catalog ops. -->
### Resolved Entities
| type | global_id | registry_id | name |
|------|--------|----|------|
| comp | GLOBcomp_1 | water | water |
| comp | GLOBcomp_2 | ethanol | ethanol |
| comp | GLOBcomp_4 | methanol | methanol |
| comp | GLOBcomp_6 | propan-2-ol | propan-2-ol |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find pure-component viscosity data for 1,3,5-trioxane → stored as L1_query_1 · validation: PASS
- [L1] Find viscosity data for 1,3,5-trioxane in any binary mixture system → stored as L1_query_2 · validation: PASS

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: no_results · validation: PASS

**Summary:** No pure-component (unary) viscosity data—neither dynamic viscosity (GLOBprop_4) nor kinematic viscosity (GLOBprop_40)—was found for 1,3,5-trioxane (GLOBcomp_952) in the ThermoML database. In fact, no pure-component data blocks of any kind were found for this compound. Any viscosity data involving 1,3,5-trioxane in the database would exist only in mixture (binary, ternary, etc.) systems.

**Answer:**

No pure-component (unary) viscosity data was found for 1,3,5-trioxane (GLOBcomp_952) in the ThermoML database. Specifically:

- **Dynamic viscosity (GLOBprop_4):** No unary blocks found for 1,3,5-trioxane.
- **Kinematic viscosity (GLOBprop_40):** No unary blocks found for 1,3,5-trioxane.
- **Any property in unary systems:** No pure-component data blocks of any kind were found for 1,3,5-trioxane.

The ThermoML database does not contain any pure-component property data for 1,3,5-trioxane. If viscosity data involving this compound exists in the database, it would only be found in mixture (binary, ternary, etc.) systems where 1,3,5-trioxane is one of the components.

**Core claims:**
- No pure-component (unary) viscosity data—neither dynamic viscosity nor kinematic viscosity—was found for 1,3,5-trioxane in the ThermoML database.
- No pure-component data blocks of any kind were found for 1,3,5-trioxane in the ThermoML database.
- Any viscosity data for 1,3,5-trioxane in the database, if it exists, would only appear in mixture (binary, ternary, etc.) systems.

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.
### L1_query_2
**L1_query_2** — status: no_results · validation: PASS

**Summary:** No viscosity data — neither dynamic viscosity (GLOBprop_4) nor kinematic viscosity (GLOBprop_40) — was found for 1,3,5-trioxane (GLOBcomp_952) in any binary mixture system in the ThermoML database. The database does contain 9 binary-mixture data blocks for 1,3,5-trioxane across 5 publications, covering mass density, partial molar volume, liquid–liquid equilibrium temperature, solid–liquid equilibrium mole fraction, and vapor pressure/VLE mole fraction, with co-components including water (GLOBcomp_1), GLOBcomp_4, GLOBcomp_2, and GLOBcomp_6.

**Answer:**

No viscosity data — neither dynamic viscosity (GLOBprop_4) nor kinematic viscosity (GLOBprop_40) — was found for 1,3,5-trioxane (GLOBcomp_952) in any binary mixture system in the ThermoML database.

However, the database does contain **9 binary-mixture data blocks** for 1,3,5-trioxane across 5 publications, covering the following properties and co-components:

**WM_L1_Q2_Table#1_(Query_L1_Q2_Answer):**

| *row_id* | *#* | *Literature* | *Block* | *Property* | *Co-compound* |
|---|---|---|---|---|---|
| WM_L1_Q2_Table#1_Row#1 | 「1」 | 「GLOBlit_3147 (10.1016/j.jct.2009.08.015)」 | 「PROPblock_5」 | 「Mass density (GLOBprop_1)」 | 「GLOBcomp_1」 |
| WM_L1_Q2_Table#1_Row#2 | 「2」 | 「GLOBlit_3168 (10.1016/j.jct.2009.11.005)」 | 「PROPblock_5」 | 「Partial molar volume (GLOBprop_84)」 | 「GLOBcomp_1」 |
| WM_L1_Q2_Table#1_Row#3 | 「3」 | 「GLOBlit_8200 (10.1021/je030243h)」 | 「PROPblock_1」 | 「LLE temperature (GLOBprop_20)」 | 「GLOBcomp_1」 |
| WM_L1_Q2_Table#1_Row#4 | 「4」 | 「GLOBlit_8564 (10.1021/je049978s)」 | 「PROPblock_1」 | 「Mole fraction (GLOBprop_2) — SLE」 | 「GLOBcomp_4」 |
| WM_L1_Q2_Table#1_Row#5 | 「5」 | 「GLOBlit_8564 (10.1021/je049978s)」 | 「PROPblock_2」 | 「Mole fraction (GLOBprop_2) — SLE」 | 「GLOBcomp_2」 |
| WM_L1_Q2_Table#1_Row#6 | 「6」 | 「GLOBlit_8564 (10.1021/je049978s)」 | 「PROPblock_3」 | 「Mole fraction (GLOBprop_2) — SLE」 | 「GLOBcomp_6」 |
| WM_L1_Q2_Table#1_Row#7 | 「7」 | 「GLOBlit_8573 (10.1021/je050015i)」 | 「PROPblock_1」 | 「Vapor pressure (GLOBprop_5)」 | 「GLOBcomp_1」 |
| WM_L1_Q2_Table#1_Row#8 | 「8–9」 | 「GLOBlit_8573 (10.1021/je050015i)」 | 「PROPblock_2」 | 「Mole fraction (GLOBprop_2)」 | 「GLOBcomp_1」 |

**Summary of available binary data for 1,3,5-trioxane:**
- **Mass density** — with GLOBcomp_1 (water)
- **Partial molar volume** — with GLOBcomp_1 (water)
- **Liquid–liquid equilibrium (LLE) temperature** — with GLOBcomp_1 (water)
- **Solid–liquid equilibrium (SLE) mole fraction** — with GLOBcomp_4, GLOBcomp_2, and GLOBcomp_6
- **Vapor pressure / VLE mole fraction** — with GLOBcomp_1 (water)

No dynamic viscosity (GLOBprop_4) or kinematic viscosity (GLOBprop_40) measurements are available for 1,3,5-trioxane in any binary system in the ThermoML database.

**Core claims:**
- No viscosity data — neither dynamic viscosity nor kinematic viscosity — was found for 1,3,5-trioxane in any binary mixture system in the ThermoML database.
- The ThermoML database does contain 9 binary-mixture data blocks for 1,3,5-trioxane across 5 publications, covering mass density, partial molar volume, liquid–liquid equilibrium temperature, solid–liquid equilibrium mole fraction, and vapor pressure/VLE mole fraction, with co-components including water and several other compounds.

**Core blocks found:**

**WM_L1_Q2_Blocks_(Query_L1_Q2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1_Q2_Table#2 | 「GLOBlit_3147」 | 「PROPblock_5」 | 「GLOBcomp_952, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density for 1,3,5-trioxane + water binary system.」 |
| WM_L1_Q2_Table#3 | 「GLOBlit_3168」 | 「PROPblock_5」 | 「GLOBcomp_952, GLOBcomp_1」 | 「GLOBprop_84」 | 「Partial molar volume for 1,3,5-trioxane + water binary system.」 |
| WM_L1_Q2_Table#4 | 「GLOBlit_8200」 | 「PROPblock_1」 | 「GLOBcomp_952, GLOBcomp_1」 | 「GLOBprop_20」 | 「LLE temperature for 1,3,5-trioxane + water binary system.」 |
| WM_L1_Q2_Table#5 | 「GLOBlit_8564」 | 「PROPblock_1」 | 「GLOBcomp_4, GLOBcomp_952」 | 「GLOBprop_2」 | 「SLE mole fraction for 1,3,5-trioxane + GLOBcomp_4 binary system.」 |
| WM_L1_Q2_Table#6 | 「GLOBlit_8564」 | 「PROPblock_2」 | 「GLOBcomp_2, GLOBcomp_952」 | 「GLOBprop_2」 | 「SLE mole fraction for 1,3,5-trioxane + GLOBcomp_2 binary system.」 |
| WM_L1_Q2_Table#7 | 「GLOBlit_8564」 | 「PROPblock_3」 | 「GLOBcomp_6, GLOBcomp_952」 | 「GLOBprop_2」 | 「SLE mole fraction for 1,3,5-trioxane + GLOBcomp_6 binary system.」 |
| WM_L1_Q2_Table#8 | 「GLOBlit_8573」 | 「PROPblock_1」 | 「GLOBcomp_952, GLOBcomp_1」 | 「GLOBprop_5」 | 「Vapor pressure for 1,3,5-trioxane + water binary system.」 |
| WM_L1_Q2_Table#9 | 「GLOBlit_8573」 | 「PROPblock_2」 | 「GLOBcomp_952, GLOBcomp_1」 | 「GLOBprop_2」 | 「VLE mole fraction for 1,3,5-trioxane + water binary system.」 |

*Not stored here: 4 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


