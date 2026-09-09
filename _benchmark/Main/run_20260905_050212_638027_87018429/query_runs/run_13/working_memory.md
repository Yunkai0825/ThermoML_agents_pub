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
- [L1] Find experimental density of pure water at 298.15 K → stored as L1_query_1 · validation: PASS

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: PASS

**Summary:** Multiple independent ThermoML sources report the mass density of pure liquid water at 298.15 K and ambient pressure (~101 kPa). Two inspected values are 997.06 kg/m³ (DOI 10.1016/j.fluid.2005.09.009, GLOBlit_306, 101.325 kPa) and 997.043 kg/m³ (DOI 10.1016/j.fluid.2007.07.066, GLOBlit_555, 101.0 kPa). Across at least six independent single-point measurements and several multi-point datasets, the reported density consistently falls in the range 997.04–997.06 kg/m³. The two inspected values are in excellent mutual agreement and can serve as a reliable baseline for comparing mixture density measurements.

**Answer:**

#### Experimental Density of Pure Water at 298.15 K

Multiple independent ThermoML sources report the mass density of pure liquid water at 298.15 K. Here are two representative, inspected data points:

##### Source 1 — Single-point measurement
- **DOI:** 10.1016/j.fluid.2005.09.009 (GLOBlit_306)
- **Block:** PROPblock_6
- **Density:** 997.06 kg/m³
- **Temperature:** 298.15 K
- **Pressure:** 101.325 kPa
- **Phase:** Liquid

##### Source 2 — Multi-point measurement
- **DOI:** 10.1016/j.fluid.2007.07.066 (GLOBlit_555)
- **Block:** PROPblock_2
- **Density:** 997.043 kg/m³
- **Temperature:** 298.15 K
- **Pressure:** 101.0 kPa
- **Phase:** Liquid

##### Summary
Across the ThermoML database, at least six independent single-point measurements and several multi-point datasets consistently report the mass density of pure water at 298.15 K in the range **997.04–997.06 kg/m³** at ambient pressure (~101 kPa). The two inspected values — 997.06 kg/m³ (GLOBlit_306) and 997.043 kg/m³ (GLOBlit_555) — are in excellent mutual agreement. This value can serve as a reliable baseline for comparing mixture density measurements.

**Core claims:**
- Multiple independent ThermoML sources report the mass density of pure liquid water at 298.15 K and ambient pressure (~101 kPa) consistently in the range 997.04–997.06 kg/m³, with two inspected values of 997.06 kg/m³ and 997.043 kg/m³ in excellent mutual agreement.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#1 | 「GLOBlit_306」 | 「PROPblock_6」 | 「GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of pure water at 298.15 K, 101.325 kPa; reported value 997.06 kg/m³.」 |
| WM_L1#1_Table#2 | 「GLOBlit_555」 | 「PROPblock_2」 | 「GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of pure water at 298.15 K, 101.0 kPa; reported value 997.043 kg/m³.」 |

*Not stored here: 2 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


