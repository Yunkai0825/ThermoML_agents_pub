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
- [L1] Find viscosity data blocks for water + DMSO binary system near 298.15 K → stored as L1_query_1 · validation: PASS

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: PASS

**Summary:** Two ThermoML data blocks report dynamic viscosity of the water + DMSO binary system at 298.15 K and 101 kPa. Block 1 (GLOBlit_2781::PROPblock_3, DOI 10.1016/j.jct.2006.12.012) provides 24 mole-fraction points spanning x(DMSO) = 0–1, with viscosities ranging from 0.0008901 Pa·s (pure water) to a maximum of 0.0037353 Pa·s at x(DMSO) ≈ 0.3638, decreasing to 0.001996 Pa·s for pure DMSO. Block 2 (GLOBlit_11517::PROPblock_3, DOI 10.1021/je9001027) provides 7 mass-fraction points at 298.15 K, with viscosities from 0.00089 Pa·s (pure water) to a maximum of 0.003421 Pa·s at w(DMSO) = 0.6 (corresponding to x ≈ 0.33), decreasing to 0.001966 Pa·s for pure DMSO. Both blocks consistently show a pronounced viscosity maximum in the DMSO-rich water region near x(DMSO) ≈ 0.33–0.36, attributed to strong hydrogen-bonding interactions forming structured hydration complexes. Block 1 offers the most detailed composition resolution.

**Answer:**

#### Viscosity Data for Water + DMSO Binary System near 298.15 K

Two data blocks were found in the ThermoML database containing dynamic viscosity (GLOBprop_4) measurements for the water (GLOBcomp_1) + dimethyl sulfoxide (GLOBcomp_31) binary system at 298.15 K and 101 kPa.

---

##### Block 1: GLOBlit_2781 :: PROPblock_3
- **DOI:** 10.1016/j.jct.2006.12.012
- **Title:** Density and viscosity of water + DMSO
- **Full block:** 120 data points, T = 298.15–318.15 K, x(DMSO) = 0–1
- **At 298.15 K:** 24 data points (RDP shape-preserving selection shown below), composition in **mole fraction** of DMSO

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *BLKpoint_id* | *x(DMSO)* | *η (Pa·s)* |
|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「BLKpoint_1」 | 「0」 | 「0.0008901」 |
| WM_L1#1_Table#1_Row#2 | 「BLKpoint_2」 | 「0.0238」 | 「0.0010331」 |
| WM_L1#1_Table#1_Row#3 | 「BLKpoint_3」 | 「0.0489」 | 「0.0012576」 |
| WM_L1#1_Table#1_Row#4 | 「BLKpoint_6」 | 「0.1587」 | 「0.0025493」 |
| WM_L1#1_Table#1_Row#5 | 「BLKpoint_7」 | 「0.2036」 | 「0.0030165」 |
| WM_L1#1_Table#1_Row#6 | 「BLKpoint_8」 | 「0.2379」 | 「0.0033011」 |
| WM_L1#1_Table#1_Row#7 | 「BLKpoint_9」 | 「0.2768」 | 「0.0035372」 |
| WM_L1#1_Table#1_Row#8 | 「BLKpoint_10」 | 「0.3074」 | 「0.0036564」 |
| WM_L1#1_Table#1_Row#9 | 「BLKpoint_11」 | 「0.3335」 | 「0.0037144」 |
| WM_L1#1_Table#1_Row#10 | 「BLKpoint_12」 | 「0.3638」 | 「**0.0037353**」 |
| WM_L1#1_Table#1_Row#11 | 「BLKpoint_13」 | 「0.3906」 | 「0.0037169」 |
| WM_L1#1_Table#1_Row#12 | 「BLKpoint_14」 | 「0.4412」 | 「0.0036062」 |
| WM_L1#1_Table#1_Row#13 | 「BLKpoint_15」 | 「0.5193」 | 「0.0033124」 |
| WM_L1#1_Table#1_Row#14 | 「BLKpoint_17」 | 「0.6195」 | 「0.0028832」 |
| WM_L1#1_Table#1_Row#15 | 「BLKpoint_18」 | 「0.6813」 | 「0.0026556」 |
| WM_L1#1_Table#1_Row#16 | 「BLKpoint_19」 | 「0.7595」 | 「0.0024317」 |
| WM_L1#1_Table#1_Row#17 | 「BLKpoint_21」 | 「0.8856」 | 「0.0021754」 |
| WM_L1#1_Table#1_Row#18 | 「BLKpoint_24」 | 「1」 | 「0.001996」 |

**Viscosity maximum** is observed at x(DMSO) ≈ 0.3638, where η = 0.0037353 Pa·s — several times larger than the viscosity of pure water (0.0008901 Pa·s at x = 0) and substantially above that of pure DMSO (0.001996 Pa·s at x = 1) (comparison derived by division of the inspected endpoint values above). The viscosity rises steeply from pure water, peaks in the DMSO-rich water region, then decreases gradually toward pure DMSO. This pronounced maximum is characteristic of strong hydrogen-bonding interactions between water and DMSO, where DMSO acts as a strong hydrogen-bond acceptor, forming structured hydration complexes that resist flow.

---

##### Block 2: GLOBlit_11517 :: PROPblock_3
- **DOI:** 10.1021/je9001027
- **Title:** Densities and Viscosities of RbBr in DMSO+Water
- **Full block:** 35 data points, T = 298.15–318.15 K, w(DMSO) = 0–1
- **At 298.15 K:** 7 data points, composition in **mass fraction** of DMSO

**WM_L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *BLKpoint_id* | *w(DMSO)* | *η (Pa·s)* |
|---|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「BLKpoint_1」 | 「0」 | 「0.00089」 |
| WM_L1#1_Table#2_Row#2 | 「BLKpoint_2」 | 「0.2」 | 「0.00134」 |
| WM_L1#1_Table#2_Row#3 | 「BLKpoint_3」 | 「0.4」 | 「0.002221」 |
| WM_L1#1_Table#2_Row#4 | 「BLKpoint_4」 | 「0.5」 | 「0.0028073」 |
| WM_L1#1_Table#2_Row#5 | 「BLKpoint_5」 | 「0.6」 | 「**0.003421**」 |
| WM_L1#1_Table#2_Row#6 | 「BLKpoint_6」 | 「0.7」 | 「0.0023568」 |
| WM_L1#1_Table#2_Row#7 | 「BLKpoint_7」 | 「1」 | 「0.001966」 |

This coarser dataset also shows the viscosity maximum, here at w(DMSO) = 0.6 (η = 0.003421 Pa·s). A mass fraction of 0.6 DMSO corresponds to a mole fraction of approximately 0.33, consistent with the maximum location found in Block 1.

---

##### Summary

**WM_L1#1_Table#3_(Query_L1#1_Answer):**

| *row_id* | *Feature* | *Block 1 (GLOBlit_2781)* | *Block 2 (GLOBlit_11517)* |
|---|---|---|---|
| WM_L1#1_Table#3_Row#1 | 「DOI」 | 「10.1016/j.jct.2006.12.012」 | 「10.1021/je9001027」 |
| WM_L1#1_Table#3_Row#2 | 「Composition variable」 | 「Mole fraction」 | 「Mass fraction」 |
| WM_L1#1_Table#3_Row#3 | 「Points at 298.15 K」 | 「24」 | 「7」 |
| WM_L1#1_Table#3_Row#4 | 「η range at 298.15 K」 | 「0.0008901–0.0037353 Pa·s」 | 「0.00089–0.003421 Pa·s」 |
| WM_L1#1_Table#3_Row#5 | 「Viscosity maximum location」 | 「x(DMSO) ≈ 0.36」 | 「w(DMSO) ≈ 0.6 (~x ≈ 0.33)」 |
| WM_L1#1_Table#3_Row#6 | 「Maximum η value」 | 「0.0037353 Pa·s」 | 「0.003421 Pa·s」 |

Block 1 (GLOBlit_2781::PROPblock_3) provides the most detailed composition-dependent viscosity data with 24 mole-fraction points at 298.15 K, clearly resolving the viscosity maximum near x(DMSO) ≈ 0.33–0.36.

**Core claims:**
- Two ThermoML data blocks provide dynamic viscosity measurements for the water + DMSO binary system at 298.15 K and 101 kPa: GLOBlit_2781::PROPblock_3 (DOI 10.1016/j.jct.2006.12.012, 24 mole-fraction points) and GLOBlit_11517::PROPblock_3 (DOI 10.1021/je9001027, 7 mass-fraction points).
- A pronounced viscosity maximum is observed at 298.15 K: in Block 1 at x(DMSO) ≈ 0.3638 with η = 0.0037353 Pa·s, and in Block 2 at w(DMSO) = 0.6 (approximately x ≈ 0.33) with η = 0.003421 Pa·s.
- The maximum viscosity is several times larger than the viscosity of pure water (0.0008901 Pa·s) and substantially above that of pure DMSO (0.001996 Pa·s), as reported in Block 1 at 298.15 K.
- The pronounced viscosity maximum is attributed to strong hydrogen-bonding interactions between water and DMSO, where DMSO acts as a strong hydrogen-bond acceptor forming structured hydration complexes that resist flow.
- Block 1 (GLOBlit_2781::PROPblock_3) provides the most detailed composition-dependent viscosity data, with 24 mole-fraction points at 298.15 K clearly resolving the viscosity maximum near x(DMSO) ≈ 0.33–0.36.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#4 | 「GLOBlit_2781」 | 「PROPblock_3」 | 「GLOBcomp_31, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of water + DMSO binary system; 24 mole-fraction points at 298.15 K (full block 298.15–318.15 K), viscosity maximum at x(DMSO) ≈ 0.36 with η = 0.0037353 Pa·s.」 |
| WM_L1#1_Table#5 | 「GLOBlit_11517」 | 「PROPblock_3」 | 「GLOBcomp_31, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of water + DMSO binary system; 7 mass-fraction points at 298.15 K (full block 298.15–318.15 K), viscosity maximum at w(DMSO) ≈ 0.6 with η = 0.003421 Pa·s.」 |

*Not stored here: 2 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


