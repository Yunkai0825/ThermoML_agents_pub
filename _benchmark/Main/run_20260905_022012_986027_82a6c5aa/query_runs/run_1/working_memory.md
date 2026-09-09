# Working Memory

## ID Catalog
<!-- PROTECTED — never compacted. Auto-populated by catalog ops. -->
### Resolved Entities
| type | global_id | registry_id | name |
|------|--------|----|------|
| comp | GLOBcomp_4 | methanol | methanol |
| comp | GLOBcomp_1 | water | water |
| prop | GLOBprop_4 | viscosity_pa_s | Viscosity, Pa*s |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|
| lit | GLOBlit_2825 | 2007-gon-cal-1 | 10.1016/j.jct.2007.05.004 |

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find dynamic viscosity measurement for methanol + water binary mixture at mole fraction 0.5, T=298.15 K, P=101.325 kPa → stored as L1_query_1 · validation: FLAGGED(1)

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: FLAGGED(1)

**Summary:** In DOI 10.1016/j.jct.2007.05.004 (GLOBlit_2825, PROPblock_9), the dynamic viscosity of the methanol + water binary mixture at T = 298.15 K, P = 101.0 kPa, and x(water) = 0.5003 is reported as 0.001309 Pa·s. No uncertainty is reported for this data point. The mole fraction of methanol at this composition (0.4997) is not a database datum but is computed as 1 − 0.5003. The viscosity at this near-equimolar composition is significantly higher than that of pure methanol (0.000545 Pa·s), reflecting hydrogen-bonding network restructuring. The data indicate the viscosity maximum lies in the water-rich region near x(water) ≈ 0.7, where η reaches 0.001554 Pa·s at x(water) = 0.6997.

**Answer:**

#### Dynamic Viscosity of Methanol + Water at x(methanol) ≈ 0.5, T = 298.15 K

**Source:** DOI 10.1016/j.jct.2007.05.004 (GLOBlit_2825), PROPblock_9

**Compounds:**
- Methanol (GLOBcomp_4)
- Water (GLOBcomp_1)

**System:** Binary mixture (methanol + water)

**Target conditions:** T = 298.15 K, P = 101.0 kPa, mole fraction of methanol ≈ 0.5

**Result:** There is no data point at exactly x(methanol) = 0.5000 in this block. The nearest data point is at **x(water) = 0.5003** (the corresponding x(methanol) is computed as 1 − 0.5003 = 0.4997, a derived value, not a database datum):

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *Temperature (K)* | *x(water)* | *Pressure (kPa)* | *Dynamic Viscosity (Pa·s)* |
|---|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「298.15」 | 「0.5003」 | 「101.0」 | 「0.001309」 |

**Viscosity value: η = 0.001309 Pa·s (≈ 1.309 mPa·s or 1.309 cP)** at T = 298.15 K, P = 101.0 kPa, and x(water) = 0.5003.

No explicit uncertainty is reported for this specific data point in the inspected table.

**Chemistry context:** The equimolar methanol–water mixture shows a viscosity significantly higher than pure methanol at the same temperature (pure methanol η = 0.000545 Pa·s at x(water) = 0). This well-known viscosity enhancement in the methanol–water system arises from extensive hydrogen-bonding network restructuring. At x(water) = 0.5003, the viscosity (0.001309 Pa·s) is already well above pure methanol but has not yet reached the maximum. The inspected data show that viscosity continues to rise to η = 0.001554 Pa·s at x(water) = 0.6997 and η = 0.001542 Pa·s at x(water) = 0.7986, indicating the viscosity maximum lies in the water-rich region near x(water) ≈ 0.7. Beyond that, viscosity decreases again (e.g., η = 0.001317 Pa·s at x(water) = 0.8999).

**Core claims:**
- The dynamic viscosity of the methanol + water mixture at T = 298.15 K, P = 101.0 kPa, and x(water) = 0.5003 is 0.001309 Pa·s, as reported in DOI 10.1016/j.jct.2007.05.004 (PROPblock_9).
- No data point exists at exactly x(methanol) = 0.5000 in the inspected block; x(water) = 0.5003 is the nearest available composition.
- No explicit uncertainty is reported for this specific data point.
- The equimolar methanol–water mixture viscosity (0.001309 Pa·s) is significantly higher than that of pure methanol at the same temperature (0.000545 Pa·s at x(water) = 0), consistent with hydrogen-bonding network restructuring in this system.
- The inspected data indicate the viscosity maximum in the methanol–water system at 298.15 K lies in the water-rich region near x(water) ≈ 0.7, with viscosity values of 0.001554 Pa·s at x(water) = 0.6997 and 0.001542 Pa·s at x(water) = 0.7986, decreasing to 0.001317 Pa·s at x(water) = 0.8999.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#2 | 「GLOBlit_2825」 | 「PROPblock_9」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity measurements for methanol + water binary mixture.」 |

*Not stored here: 2 verbatim data_inspections table(s); 4 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(1) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNGROUNDED_LITERAL** PROPblock_9: 0.4997 (near '…(the corresponding x(methanol) is computed as 1 - 0.5003 = 0…') matches no inspected row/stat, database table, or other source of PROPblock_9


