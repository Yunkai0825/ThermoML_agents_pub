# Working Memory

## ID Catalog
<!-- PROTECTED — never compacted. Auto-populated by catalog ops. -->
### Resolved Entities
| type | global_id | registry_id | name |
|------|--------|----|------|
| comp | GLOBcomp_2407 | oxirane | oxirane |
| comp | GLOBcomp_952 | 1,3,5-trioxane | 1,3,5-trioxane |
| comp | GLOBcomp_1480 | 2,4,6-trimethyl-1,3,5-trioxane | 2,4,6-trimethyl-1,3,5-trioxane |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Search for compounds matching 'ethylene trioxide', '1,3,5-trioxane', 'trioxane', 'trioxolane', or 'ethylene oxide' in Th → stored as L1_query_1 · validation: PASS
- [L1] Find viscosity data blocks for 1,3,5-trioxane + water and oxirane + water binary systems → stored as L1_query_2 · validation: PASS

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: PASS

**Summary:** No compound named "ethylene trioxide" exists in the ThermoML database. The closest matches found are oxirane (ethylene oxide, GLOBcomp_2407, C₂H₄O, SMILES C1CO1), 1,3,5-trioxane (GLOBcomp_952, C₃H₆O₃, SMILES C1OCOCO1), and 2,4,6-trimethyl-1,3,5-trioxane (GLOBcomp_1480, C₆H₁₂O₃). Trioxolane (1,2,4-trioxolane / ozonide class) is also not present. "Ethylene trioxide" is not a standard IUPAC name; the most plausible candidate if "trioxide" refers to three ring oxygens is 1,3,5-trioxane (GLOBcomp_952). Oxirane (GLOBcomp_2407) contains only one oxygen and would not match "trioxide."

**Answer:**

The ThermoML database was searched for compounds matching "ethylene trioxide," "trioxane," "trioxolane," and "ethylene oxide." Here are the results:

**Compounds found:**

**WM_L1_Q1_Table#1_(Query_L1_Q1_Answer):**

| *row_id* | *Global ID* | *Name* | *Molecular Formula* | *SMILES* |
|---|---|---|---|---|
| WM_L1_Q1_Table#1_Row#1 | 「GLOBcomp_2407」 | 「oxirane (ethylene oxide)」 | 「C₂H₄O」 | 「C1CO1」 |
| WM_L1_Q1_Table#1_Row#2 | 「GLOBcomp_952」 | 「1,3,5-trioxane」 | 「C₃H₆O₃」 | 「C1OCOCO1」 |
| WM_L1_Q1_Table#1_Row#3 | 「GLOBcomp_1480」 | 「2,4,6-trimethyl-1,3,5-trioxane」 | 「C₆H₁₂O₃」 | 「CC1OC(C)OC(C)O1」 |

**Compounds not found:**
- **"Ethylene trioxide"** — No compound with this exact name exists in the ThermoML database.
- **Trioxolane** (1,2,4-trioxolane / ozonide class) — Not present in the database.

**Chemical context:**
- "Ethylene trioxide" is not a standard IUPAC name. It could potentially refer to **1,3,5-trioxane** (GLOBcomp_952), which is the cyclic trimer of formaldehyde (C₃H₆O₃), or less likely to ethylene oxide (oxirane, GLOBcomp_2407, C₂H₄O). The name "ethylene trioxide" does not correspond to any single well-established compound in standard chemical nomenclature or in the ThermoML database.
- **1,3,5-trioxane** (GLOBcomp_952) is the most plausible candidate if "trioxide" refers to the three oxygen atoms in the ring structure.
- **Oxirane / ethylene oxide** (GLOBcomp_2407) is a simple three-membered epoxide ring with only one oxygen, so it would not match "trioxide."

**Core claims:**
- No compound named "ethylene trioxide" exists in the ThermoML database; the name is not a standard IUPAC designation and does not correspond to any single well-established compound in standard chemical nomenclature.
- The closest plausible match in the ThermoML database is 1,3,5-trioxane (GLOBcomp_952, C₃H₆O₃), which contains three oxygen atoms in its ring structure.
- Oxirane (ethylene oxide, GLOBcomp_2407, C₂H₄O) is present in the database but contains only one oxygen atom and would not match a "trioxide" designation.
- Trioxolane (1,2,4-trioxolane / ozonide class) is not present in the ThermoML database.

*Not stored here: 3 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.
### L1_query_2
**L1_query_2** — status: no_results · validation: PASS

**Summary:** No viscosity data were found in the ThermoML database for any of the candidate binary systems: 1,3,5-trioxane (GLOBcomp_952) + water (GLOBcomp_1), oxirane/ethylene oxide (GLOBcomp_2407) + water (GLOBcomp_1), and 2,4,6-trimethyl-1,3,5-trioxane (GLOBcomp_1480) + water (GLOBcomp_1). Searches covered both dynamic viscosity (GLOBprop_4) and kinematic viscosity (GLOBprop_40) for declared binary systems, and all returned zero results.

**Answer:**

No viscosity data were found in the ThermoML database for any of the candidate binary systems:

1. **1,3,5-trioxane (GLOBcomp_952) + water (GLOBcomp_1)** — No dynamic viscosity (GLOBprop_4) or kinematic viscosity (GLOBprop_40) data blocks exist for this binary system.

2. **Oxirane / ethylene oxide (GLOBcomp_2407) + water (GLOBcomp_1)** — No viscosity data blocks found for this binary system either.

3. **2,4,6-trimethyl-1,3,5-trioxane (GLOBcomp_1480) + water (GLOBcomp_1)** — Also no viscosity data blocks found.

All three searches were conducted for declared binary systems with both dynamic and kinematic viscosity properties, and all returned zero results. The ThermoML database does not contain viscosity measurements for any of these aqueous binary systems involving trioxane-type compounds or oxirane.

**Core claims:**
- No dynamic viscosity or kinematic viscosity data were found in the ThermoML database for the binary systems 1,3,5-trioxane + water, oxirane (ethylene oxide) + water, or 2,4,6-trimethyl-1,3,5-trioxane + water.

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


