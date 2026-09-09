# Q5.1 — Tool Trace

**Prompt:** Do you have viscosity data for IPA + water?

**Summary:** 396.1s  |  4 iterations  |  3 tools

---

### Step 1: `L1_query`
- **Args:** `{"context": "...", "id_catalog": "...", "instruction": "...", "purpose": "..."}`
- **Result size:** 319 chars
- **Elapsed:** 153.6s

### Step 2: `L1_query`
- **Args:** `{"context": "...", "id_catalog": "...", "instruction": "...", "purpose": "..."}`
- **Result size:** 1,368 chars
- **Elapsed:** 29.4s

### Step 3: `L1_query`
- **Args:** `{"context": "...", "id_catalog": "...", "instruction": "...", "purpose": "..."}`
- **Result size:** 22,504 chars
- **Elapsed:** 118.0s

---

## Working Memory (final snapshot)

# Working Memory

## ID Catalog
<!-- PROTECTED — never compacted. Auto-populated by catalog ops. -->
### Resolved Entities
| type | global_id | registry_id | name |
|------|--------|----|------|
| comp | GLOBcomp_6 | propan-2-ol | propan-2-ol |
| comp | GLOBcomp_1 | water | water |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find compound IDs for isopropanol (2-propanol, IPA, CAS 67-63-0) and water (CAS 7732-18-5) in the ThermoML database → stored as L1_query_1 · validation: PASS
- [L1] Find dynamic viscosity data for binary mixture of isopropanol (propan-2-ol) and water → stored as L1_query_2 · validation: PASS

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: PASS

**Summary:** In the ThermoML database, isopropanol (propan-2-ol, CAS 67-63-0, C₃H₈O, SMILES: CC(C)O) is assigned compound ID GLOBcomp_6, and water (CAS 7732-18-5, H₂O, SMILES: O) is assigned compound ID GLOBcomp_1. Both were resolved with exact matches.

**Answer:**

The compound IDs for the requested substances in the ThermoML database are:

- **Isopropanol (propan-2-ol, 2-propanol, IPA, CAS 67-63-0):** GLOBcomp_6 (C₃H₈O, SMILES: CC(C)O)
- **Water (CAS 7732-18-5):** GLOBcomp_1 (H₂O, SMILES: O)

Both compounds were resolved with exact matches and are ready for use in subsequent property data searches (e.g., viscosity of IPA + water binary mixtures).

**Core claims:**
- In the ThermoML database, isopropanol (propan-2-ol, CAS 67-63-0, C₃H₈O, SMILES: CC(C)O) is identified as GLOBcomp_6, and water (CAS 7732-18-5, H₂O, SMILES: O) is identified as GLOBcomp_1.
- Both compounds were resolved with exact matches in the ThermoML database.

*Not stored here: 2 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.
### L1_query_2
**L1_query_2** — status: success · validation: PASS

**Summary:** Two ThermoML sources provide a total of 25 dynamic viscosity (Pa·s) data points for binary propan-2-ol + water mixtures in the liquid phase. Source GLOBlit_5585 (DOI 10.1016/j.jct.2019.105880, PROPblock_12) contains 12 points measured by falling/rolling sphere at 100.0 kPa, spanning 288.15–303.15 K and IPA mass fractions of 0.1, 0.2, and 0.3, with viscosities from 0.001208 to 0.004014 Pa·s; viscosity decreases with increasing temperature at all compositions. Source GLOBlit_11042 (DOI 10.1021/je700700f, PROPblock_15) contains 13 points measured by capillary Ubbelohde viscometry at 298.15 K and 101.0 kPa across the full IPA mole-fraction range (0–1), with viscosities from 0.00089 to 0.003087 Pa·s. The full-composition data reveal the well-known non-monotonic viscosity behavior: viscosity rises from 0.00089 Pa·s for pure water to a maximum of 0.003087 Pa·s near x(IPA) ≈ 0.2994, then decreases to 0.002082 Pa·s for pure IPA, attributed to enhanced hydrogen-bonding network restructuring and microheterogeneity. The two sources differ in composition basis (mass fraction vs. mole fraction) and measurement technique.

**Answer:**

#### Viscosity Data for Binary Propan-2-ol + Water Mixtures

Two literature sources in the ThermoML database provide dynamic viscosity (GLOBprop_4, Pa·s) data for binary mixtures of propan-2-ol (GLOBcomp_6) and water (GLOBcomp_1), totaling **25 data points** across two blocks:

---

##### Source 1: GLOBlit_5585 — PROPblock_12
- **DOI:** 10.1016/j.jct.2019.105880
- **Literature ID:** 2019-meh-haj-0
- **Data points:** 12
- **Measurement method:** Falling/rolling sphere (GLOBmeas_8)
- **Temperature range:** 288.15–303.15 K (variable)
- **Pressure:** 100.0 kPa (fixed constraint)
- **Composition:** Mass fraction of IPA (w): 0.1, 0.2, 0.3 (3 values)
- **Viscosity range:** 0.001208–0.004014 Pa·s
- **Phase:** Liquid

Representative data points (verbatim from inspection):

**WM_L1#3_Table#1_(Query_L1#3_Answer):**

| *row_id* | *Temperature (K)* | *w(IPA)* | *Viscosity (Pa·s)* |
|---|---|---|---|
| WM_L1#3_Table#1_Row#1 | 「288.15」 | 「0.1」 | 「0.001936」 |
| WM_L1#3_Table#1_Row#2 | 「288.15」 | 「0.2」 | 「0.003087」 |
| WM_L1#3_Table#1_Row#3 | 「288.15」 | 「0.3」 | 「0.004014」 |
| WM_L1#3_Table#1_Row#4 | 「298.15」 | 「0.1」 | 「0.001395」 |
| WM_L1#3_Table#1_Row#5 | 「298.15」 | 「0.2」 | 「0.002045」 |
| WM_L1#3_Table#1_Row#6 | 「298.15」 | 「0.3」 | 「0.002555」 |
| WM_L1#3_Table#1_Row#7 | 「303.15」 | 「0.1」 | 「0.001208」 |
| WM_L1#3_Table#1_Row#8 | 「303.15」 | 「0.2」 | 「0.00171」 |
| WM_L1#3_Table#1_Row#9 | 「303.15」 | 「0.3」 | 「0.002105」 |

---

##### Source 2: GLOBlit_11042 — PROPblock_15
- **DOI:** 10.1021/je700700f
- **Literature ID:** 2008-gon-cal-0
- **Data points:** 13 (10 shown by shape-preserving RDP subset)
- **Measurement method:** Capillary Ubbelohde (GLOBmeas_4)
- **Temperature:** 298.15 K (fixed constraint)
- **Pressure:** 101.0 kPa (fixed constraint)
- **Composition:** Mole fraction of IPA (x): 0–1 (full composition range, 13 values)
- **Viscosity range:** 0.00089–0.003087 Pa·s
- **Phase:** Liquid

Representative data points (verbatim from inspection):

**WM_L1#3_Table#2_(Query_L1#3_Answer):**

| *row_id* | *x(IPA)* | *Viscosity (Pa·s)* |
|---|---|---|
| WM_L1#3_Table#2_Row#1 | 「0」 | 「0.00089」 |
| WM_L1#3_Table#2_Row#2 | 「0.0491」 | 「0.001718」 |
| WM_L1#3_Table#2_Row#3 | 「0.1008」 | 「0.002495」 |
| WM_L1#3_Table#2_Row#4 | 「0.2011」 | 「0.003038」 |
| WM_L1#3_Table#2_Row#5 | 「0.2994」 | 「0.003087」 |
| WM_L1#3_Table#2_Row#6 | 「0.3992」 | 「0.002924」 |
| WM_L1#3_Table#2_Row#7 | 「0.6987」 | 「0.002274」 |
| WM_L1#3_Table#2_Row#8 | 「0.7993」 | 「0.002153」 |
| WM_L1#3_Table#2_Row#9 | 「0.8998」 | 「0.002073」 |
| WM_L1#3_Table#2_Row#10 | 「1」 | 「0.002082」 |

---

##### Chemistry Notes
- **PROPblock_15** (GLOBlit_11042) covers the full composition range at 298.15 K and reveals the well-known **non-monotonic viscosity behavior** of the IPA–water system. The viscosity rises from 0.00089 Pa·s (pure water, x = 0) to a maximum of 0.003087 Pa·s at x = 0.2994, then decreases toward 0.002082 Pa·s for pure IPA (x = 1). This maximum near x ≈ 0.3 is attributed to enhanced hydrogen-bonding network restructuring and microheterogeneity in the alcohol–water mixture.
- **PROPblock_12** (GLOBlit_5585) provides temperature-dependent data at three mass fractions in the water-rich region (w = 0.1–0.3), showing that viscosity decreases with increasing temperature at all compositions — consistent with thermally activated flow behavior.
- The two sources use different composition bases (mass fraction vs. mole fraction) and different measurement techniques (falling sphere vs. capillary Ubbelohde viscometry).

**Core claims:**
- Two ThermoML sources provide a total of 25 dynamic viscosity data points for binary propan-2-ol + water mixtures in the liquid phase.
- GLOBlit_5585 (DOI 10.1016/j.jct.2019.105880) contributes 12 data points measured by falling/rolling sphere viscometry at 100.0 kPa, covering temperatures 288.15–303.15 K and IPA mass fractions of 0.1, 0.2, and 0.3, with viscosities ranging from 0.001208–0.004014 Pa·s.
- GLOBlit_11042 (DOI 10.1021/je700700f) contributes 13 data points measured by capillary Ubbelohde viscometry at 298.15 K and 101.0 kPa, spanning the full IPA mole fraction range (0–1), with viscosities ranging from 0.00089–0.003087 Pa·s.
- The full-composition data at 298.15 K reveal non-monotonic viscosity behavior: viscosity rises from 0.00089 Pa·s for pure water (x = 0) to a maximum of 0.003087 Pa·s at x = 0.2994, then decreases to 0.002082 Pa·s for pure IPA (x = 1), attributed to enhanced hydrogen-bonding network restructuring and microheterogeneity.
- Temperature-dependent data in the water-rich region (w = 0.1–0.3) show that viscosity decreases with increasing temperature at all compositions, consistent with thermally activated flow behavior.

**Core blocks found:**

**WM_L1#3_Blocks_(Query_L1#3_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#3_Table#3 | 「GLOBlit_5585」 | 「PROPblock_12」 | 「GLOBcomp_1, GLOBcomp_6」 | 「GLOBprop_4」 | 「Dynamic viscosity of propan-2-ol + water binary mixture at 288.15–303.15 K, 100.0 kPa, mass fraction IPA 0.1–0.3; 12 data points via falling/rolling sphere viscometry.」 |
| WM_L1#3_Table#4 | 「GLOBlit_11042」 | 「PROPblock_15」 | 「GLOBcomp_6, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of propan-2-ol + water binary mixture at 298.15 K, 101.0 kPa, full mole fraction range (0–1); 13 data points via capillary Ubbelohde viscometry.」 |

*Not stored here: 2 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.

---

**Total:** 3 tool calls  |  396.1s  |  OK
