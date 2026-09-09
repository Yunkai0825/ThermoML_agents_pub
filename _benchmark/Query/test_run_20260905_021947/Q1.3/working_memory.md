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
- [L1] Find mass density data for equimolar propan-2-ol + water liquid mixture at 25 °C and atmospheric pressure → stored as L1_query_1 · validation: PASS

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: PASS

**Summary:** The mass density of a binary liquid mixture of propan-2-ol and water at 298.15 K and 101.0 kPa was reported from DOI 10.1021/je700700f (GLOBlit_11042, PROPblock_17). At the nearest-to-equimolar composition of x(propan-2-ol) = 0.4981, the mass density is 838.8 kg/m³. Density decreases monotonically with increasing propan-2-ol mole fraction, from 997.2 kg/m³ for pure water to 780.7 kg/m³ for pure propan-2-ol. The dataset comprises 13 data points spanning the full mole-fraction range. The system exhibits negative excess volumes (volume contraction on mixing), especially in the water-rich region, attributed to strong hydrogen-bonding interactions.

**Answer:**

#### Mass Density of Equimolar Propan-2-ol + Water at 25 °C and Atmospheric Pressure

A binary liquid mixture of propan-2-ol (isopropanol, GLOBcomp_6) and water (GLOBcomp_1) has been measured for mass density at 298.15 K and 101 kPa (atmospheric pressure) across the full mole-fraction range.

##### Data at Near-Equimolar Composition

From the dataset reported by Soliman and Marschall (DOI: 10.1021/je700700f, GLOBlit_11042, PROPblock_17), the following density values bracket the equimolar composition:

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *Mole fraction of propan-2-ol* | *Temperature (K)* | *Pressure (kPa)* | *Mass density (kg/m³)* |
|---|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「0.3992」 | 「298.15」 | 「101.0」 | 「857.7」 |
| WM_L1#1_Table#1_Row#2 | 「**0.4981**」 | 「**298.15**」 | 「**101.0**」 | 「**838.8**」 |
| WM_L1#1_Table#1_Row#3 | 「0.5979」 | 「298.15」 | 「101.0」 | 「823.5」 |

The closest measurement to equimolar (x = 0.5) is at **x(propan-2-ol) = 0.4981**, where the mass density is **838.8 kg/m³** at 298.15 K and 101.0 kPa. There is no data point at exactly x = 0.5; the nearest recorded compositions bracket it at 0.4981 (below) and 0.5979 (above).

##### Chemical Insight

The density decreases monotonically with increasing propan-2-ol mole fraction across the full composition range (from 997.2 kg/m³ for pure water to 780.7 kg/m³ for pure propan-2-ol at 298.15 K). At the near-equimolar composition, the density (838.8 kg/m³) is closer to that of pure propan-2-ol than to pure water, reflecting the significant contribution of the lighter, bulkier alcohol molecules to the mixture volume. This system is well known for exhibiting negative excess volumes (volume contraction on mixing), particularly in the water-rich region, due to strong hydrogen-bonding interactions between propan-2-ol and water.

**Source:** DOI 10.1021/je700700f (GLOBlit_11042, PROPblock_17) — 13 data points covering x(propan-2-ol) = 0 to 1 at 298.15 K and 101.0 kPa.

**Core claims:**
- At x(propan-2-ol) = 0.4981 (the nearest measured composition to equimolar), the mass density of the propan-2-ol + water binary mixture is 838.8 kg/m³ at 298.15 K and 101.0 kPa, as reported by Soliman and Marschall (DOI: 10.1021/je700700f).
- The mass density of the propan-2-ol + water mixture decreases monotonically with increasing propan-2-ol mole fraction across the full composition range, from 997.2 kg/m³ for pure water to 780.7 kg/m³ for pure propan-2-ol at 298.15 K.
- No data point exists at exactly x(propan-2-ol) = 0.5; the nearest recorded compositions bracket it at 0.4981 and 0.5979.
- The propan-2-ol + water system is known to exhibit negative excess volumes (volume contraction on mixing), particularly in the water-rich region, attributed to strong hydrogen-bonding interactions.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#2 | 「GLOBlit_11042」 | 「PROPblock_17」 | 「GLOBcomp_6, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density measurements for propan-2-ol + water binary mixture at 298.15 K and 101.0 kPa across the full mole-fraction range.」 |

*Not stored here: 1 verbatim data_inspections table(s); 2 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


