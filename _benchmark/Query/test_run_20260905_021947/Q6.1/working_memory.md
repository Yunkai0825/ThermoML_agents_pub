# Working Memory

## ID Catalog
<!-- PROTECTED — never compacted. Auto-populated by catalog ops. -->
### Resolved Entities
| type | global_id | registry_id | name |
|------|--------|----|------|
| comp | GLOBcomp_58 | glycerol | glycerol |
| comp | GLOBcomp_1 | water | water |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find data for the binary system propane-1,2,3-triol (glycerol) + water in ThermoML. The user wrote 'propane-1,2,4-triol' → stored as L1_query_1 · validation: PASS

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: PASS

**Summary:** The binary system glycerol (propane-1,2,3-triol, CAS 56-81-5) + water is represented in ThermoML with 36 property data blocks across 20 literature sources covering 13 distinct thermophysical properties. Properties include mass density (10 blocks), speed of sound (5 blocks), boiling temperature (5 blocks), vapor pressure (2 blocks), binary diffusion coefficient (2 blocks), and others such as viscosity, refractive index, and excess volumes. Representative mass density data from GLOBlit_4951 (Negadi, 2017) at 100 kPa span 283.15–313.15 K and water mole fractions 0–1, showing monotonic decrease from pure glycerol (1267 kg/m³ at 283.15 K) to pure water (1000 kg/m³ at 283.15 K), with density decreasing with increasing temperature at each composition (e.g., pure glycerol drops from 1267 to 1248 kg/m³ over 283.15–313.15 K). Sources span 2006–2018 and include journals such as J. Chem. Thermodynamics, J. Chem. Eng. Data, Fluid Phase Equilibria, and Thermochimica Acta. The note clarifies that propane-1,2,4-triol cannot exist since propane has only 3 carbon atoms; the intended compound is glycerol (propane-1,2,3-triol).

**Answer:**

#### Glycerol (propane-1,2,3-triol) + Water Binary System in ThermoML

**Note:** The compound "propane-1,2,4-triol" cannot exist because propane has only 3 carbon atoms. The intended compound is **glycerol (propane-1,2,3-triol, CAS 56-81-5)**.

##### System Overview

The binary system **glycerol (GLOBcomp_58) + water (GLOBcomp_1)** is well-represented in ThermoML with **36 property data blocks** across **20 literature sources**, covering **13 distinct thermophysical properties**.

##### Available Properties

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *Property* | *GLOBprop* | *# Blocks* |
|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「Mass density (kg/m³)」 | 「GLOBprop_1」 | 「10」 |
| WM_L1#1_Table#1_Row#2 | 「Speed of sound (m/s)」 | 「GLOBprop_8」 | 「5」 |
| WM_L1#1_Table#1_Row#3 | 「Boiling temperature (K)」 | 「GLOBprop_14」 | 「5」 |
| WM_L1#1_Table#1_Row#4 | 「Vapor pressure (kPa)」 | 「GLOBprop_5」 | 「2」 |
| WM_L1#1_Table#1_Row#5 | 「Binary diffusion coefficient (m²/s)」 | 「GLOBprop_29」 | 「2」 |
| WM_L1#1_Table#1_Row#6 | 「And additional properties (viscosity, refractive index, excess volumes, etc.)」 | 「—」 | 「remaining blocks」 |

##### Literature Sources (selected)

**WM_L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *DOI* | *GLOBlit_N* | *Author* | *Year* |
|---|---|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「10.1016/j.jct.2017.01.011」 | 「GLOBlit_4951」 | 「Negadi, L.」 | 「2017」 |
| WM_L1#1_Table#2_Row#2 | 「10.1016/j.jct.2018.05.016」 | 「GLOBlit_5254」 | 「Kaur, K.」 | 「2018」 |

Additional DOIs include publications in J. Chem. Thermodynamics, J. Chem. Eng. Data, Fluid Phase Equilibria, and Thermochimica Acta (2006–2018 range).

##### Representative Data: Mass Density at 100 kPa

From **GLOBlit_4951** (Negadi, 2017), **PROPblock_3** — mass density of glycerol + water as a function of temperature and water mole fraction at 100 kPa (44 data points total, 283.15–313.15 K):

**WM_L1#1_Table#3_(Query_L1#1_Answer):**

| *row_id* | *T (K)* | *x(water)* | *ρ (kg/m³)* |
|---|---|---|---|
| WM_L1#1_Table#3_Row#1 | 「283.15」 | 「0」 | 「1267」 |
| WM_L1#1_Table#3_Row#2 | 「283.15」 | 「0.4042」 | 「1236」 |
| WM_L1#1_Table#3_Row#3 | 「283.15」 | 「0.7003」 | 「1183」 |
| WM_L1#1_Table#3_Row#4 | 「283.15」 | 「0.9024」 | 「1091」 |
| WM_L1#1_Table#3_Row#5 | 「283.15」 | 「1」 | 「1000」 |
| WM_L1#1_Table#3_Row#6 | 「293.15」 | 「0」 | 「1261」 |
| WM_L1#1_Table#3_Row#7 | 「293.15」 | 「0.4042」 | 「1230」 |
| WM_L1#1_Table#3_Row#8 | 「293.15」 | 「0.7003」 | 「1177」 |
| WM_L1#1_Table#3_Row#9 | 「293.15」 | 「0.9024」 | 「1087」 |
| WM_L1#1_Table#3_Row#10 | 「293.15」 | 「1」 | 「998」 |
| WM_L1#1_Table#3_Row#11 | 「303.15」 | 「0」 | 「1255」 |
| WM_L1#1_Table#3_Row#12 | 「303.15」 | 「0.4042」 | 「1224」 |
| WM_L1#1_Table#3_Row#13 | 「303.15」 | 「0.7003」 | 「1172」 |
| WM_L1#1_Table#3_Row#14 | 「303.15」 | 「0.9024」 | 「1083」 |
| WM_L1#1_Table#3_Row#15 | 「303.15」 | 「1」 | 「996」 |
| WM_L1#1_Table#3_Row#16 | 「313.15」 | 「0」 | 「1248」 |
| WM_L1#1_Table#3_Row#17 | 「313.15」 | 「0.4042」 | 「1218」 |
| WM_L1#1_Table#3_Row#18 | 「313.15」 | 「0.7003」 | 「1166」 |
| WM_L1#1_Table#3_Row#19 | 「313.15」 | 「0.9024」 | 「1078」 |
| WM_L1#1_Table#3_Row#20 | 「313.15」 | 「1」 | 「992」 |

##### Chemical Insight

The density data show the expected monotonic decrease from pure glycerol (ρ ≈ 1267 kg/m³ at 283.15 K) to pure water (ρ ≈ 1000 kg/m³ at 283.15 K) as the water mole fraction increases. At each composition, density decreases with increasing temperature — for example, pure glycerol drops from 1267 kg/m³ at 283.15 K to 1248 kg/m³ at 313.15 K. The glycerol–water system is widely studied because glycerol is a major bio-derived polyol used as a humectant, cryoprotectant, and green solvent, and its aqueous mixtures exhibit significant hydrogen-bonding interactions that influence all transport and volumetric properties.

**Core claims:**
- The binary system glycerol (propane-1,2,3-triol, CAS 56-81-5) + water is represented in ThermoML by 36 property data blocks across 20 literature sources, covering 13 distinct thermophysical properties including mass density, speed of sound, boiling temperature, vapor pressure, and binary diffusion coefficient.
- Mass density data from GLOBlit_4951 (Negadi, 2017) at 100 kPa show a monotonic decrease from pure glycerol (ρ ≈ 1267 kg/m³ at 283.15 K) to pure water (ρ ≈ 1000 kg/m³ at 283.15 K) as water mole fraction increases.
- At each composition, density decreases with increasing temperature; for example, pure glycerol drops from 1267 kg/m³ at 283.15 K to 1248 kg/m³ at 313.15 K.
- The compound 'propane-1,2,4-triol' cannot exist because propane has only 3 carbon atoms; the intended compound is glycerol (propane-1,2,3-triol).

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#4 | 「GLOBlit_4951」 | 「PROPblock_3」 | 「GLOBcomp_58, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of glycerol + water as a function of temperature and water mole fraction at 100 kPa (283.15–313.15 K).」 |

*Not stored here: 1 verbatim data_inspections table(s); 2 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


