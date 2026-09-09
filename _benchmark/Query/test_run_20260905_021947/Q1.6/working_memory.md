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
- [L1] Find measured isobaric molar heat capacity (Cp) of pure liquid water at 298.15 K and atmospheric pressure → stored as L1_query_1 · validation: FLAGGED(1)

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: FLAGGED(1)

**Summary:** Two ThermoML measurements of the isobaric molar heat capacity (Cp) of pure liquid water at 298.15 K are reported. At 101.325 kPa (DOI 10.1016/j.jct.2016.09.031), Cp = 75.11470996 J/(K·mol). At 101.0 kPa (DOI 10.1016/j.fluid.2013.08.005), Cp = 75.368725408 J/(K·mol). No explicit uncertainty values were reported in the inspected blocks. Both values are consistent with the commonly cited standard molar heat capacity of liquid water at 298.15 K.

**Answer:**

#### Measured Isobaric Molar Heat Capacity (Cp) of Pure Liquid Water at 298.15 K and Atmospheric Pressure

The ThermoML database contains multiple measurements of the molar heat capacity at constant pressure (Cp) for pure liquid water at 298.15 K and near-atmospheric pressure. Here are two representative, inspected data points:

##### Data Point 1 — Exact conditions (298.15 K, 101.325 kPa)
- **Cp = 75.11470996 J/(K·mol)**
- Temperature: 298.15 K
- Pressure: 101.325 kPa
- Source: DOI 10.1016/j.jct.2016.09.031 (GLOBlit_4832, PROPblock_1)
- Measurement method: GLOBmeas_12

##### Data Point 2 — Near-atmospheric (298.15 K, 101.0 kPa)
- **Cp = 75.368725408 J/(K·mol)**
- Temperature: 298.15 K
- Pressure: 101.0 kPa
- Source: DOI 10.1016/j.fluid.2013.08.005 (GLOBlit_1310, PROPblock_1)
- Measurement method: GLOBmeas_31

##### Summary
The two inspected measurements at 298.15 K give Cp values of 75.11470996 and 75.368725408 J/(K·mol), consistent with the commonly cited standard molar heat capacity of liquid water (approximately 75.3 J/(K·mol) at 298.15 K, per general reference literature — not from this database). The difference between the two inspected values (computed: 75.368725408 − 75.11470996 ≈ 0.254 J/(K·mol)) reflects differences in experimental technique, calibration, and exact pressure conditions (101.325 vs 101.0 kPa). No explicit uncertainty values were reported in the inspected blocks.

**Core claims:**
- The ThermoML database contains two inspected measurements of the isobaric molar heat capacity (Cp) of pure liquid water at 298.15 K and near-atmospheric pressure: 75.11470996 J/(K·mol) at 101.325 kPa (DOI 10.1016/j.jct.2016.09.031) and 75.368725408 J/(K·mol) at 101.0 kPa (DOI 10.1016/j.fluid.2013.08.005).
- The two inspected Cp values are consistent with the commonly cited standard molar heat capacity of liquid water at 298.15 K (approximately 75.3 J/(K·mol)), and their difference reflects differences in experimental technique, calibration, and exact pressure conditions.
- No explicit uncertainty values were reported in the inspected data blocks.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#1 | 「GLOBlit_4832」 | 「PROPblock_1」 | 「GLOBcomp_1」 | 「GLOBprop_9」 | 「Isobaric molar heat capacity of pure liquid water at 298.15 K and 101.325 kPa; Cp = 75.11470996 J/(K·mol).」 |
| WM_L1#1_Table#2 | 「GLOBlit_1310」 | 「PROPblock_1」 | 「GLOBcomp_1」 | 「GLOBprop_9」 | 「Isobaric molar heat capacity of pure liquid water at 298.15 K and 101.0 kPa; Cp = 75.368725408 J/(K·mol).」 |

*Not stored here: 2 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(1) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNGROUNDED_LITERAL** PROPblock_1: 0.254 (near '…wo inspected values (computed: 75.368725408 - 75.11470996 ≈ …') matches no inspected row/stat, database table, or other source of PROPblock_1


