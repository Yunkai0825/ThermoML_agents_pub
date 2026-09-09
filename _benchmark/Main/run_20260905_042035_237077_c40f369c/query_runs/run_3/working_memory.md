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
- [L1] Find dynamic viscosity data for binary mixture methanol + ethanol near 303.15 K as a function of composition → stored as L1_query_1 · validation: PASS

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: PASS

**Summary:** Dynamic viscosity of the methanol + ethanol binary liquid mixture at 303.15 K and 81.5 kPa, measured by capillary tube (Ostwald–Ubbelohde), from DOI 10.1021/je800633a. Twelve data points span methanol mole fractions from 0.0417 to 0.9166, with viscosity decreasing monotonically from 0.000968 Pa·s (ethanol-rich end) to 0.000556 Pa·s (methanol-rich end). The near-linear decrease (R² = 0.9960) indicates relatively ideal mixing behavior with minimal excess viscosity effects, consistent with methanol's smaller molecular size and weaker hydrogen-bonding network compared to ethanol.

**Answer:**

#### Dynamic Viscosity of Methanol + Ethanol Binary Mixture at 303.15 K

##### Source
**DOI:** 10.1021/je800633a (GLOBlit_11337)
**Block:** PROPblock_16
**Measurement method:** Capillary tube (Ostwald–Ubbelohde)

##### System
- **Compounds:** Methanol (GLOBcomp_4) + Ethanol (GLOBcomp_2)
- **System type:** Binary, liquid phase
- **Temperature:** 303.15 K (fixed)
- **Pressure:** 81.5 kPa (fixed)

##### Viscosity vs. Mole Fraction of Methanol

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *x(methanol)* | *η (Pa·s)* |
|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「0.0417」 | 「0.000968」 |
| WM_L1#1_Table#1_Row#2 | 「0.1476」 | 「0.000906」 |
| WM_L1#1_Table#1_Row#3 | 「0.2214」 | 「0.000865」 |
| WM_L1#1_Table#1_Row#4 | 「0.2952」 | 「0.000828」 |
| WM_L1#1_Table#1_Row#5 | 「0.3644」 | 「0.000793」 |
| WM_L1#1_Table#1_Row#6 | 「0.4488」 | 「0.000753」 |
| WM_L1#1_Table#1_Row#7 | 「0.5290」 | 「0.000717」 |
| WM_L1#1_Table#1_Row#8 | 「0.5995」 | 「0.000685」 |
| WM_L1#1_Table#1_Row#9 | 「0.6859」 | 「0.000648」 |
| WM_L1#1_Table#1_Row#10 | 「0.7442」 | 「0.000624」 |
| WM_L1#1_Table#1_Row#11 | 「0.8320」 | 「0.000588」 |
| WM_L1#1_Table#1_Row#12 | 「0.9166」 | 「0.000556」 |

All 12 data points are shown. The composition range spans x(methanol) = 0.0417 to 0.9166, and the viscosity ranges from 0.000968 Pa·s (ethanol-rich end) down to 0.000556 Pa·s (methanol-rich end).

##### Chemical Insight
The viscosity decreases monotonically and nearly linearly (R² = 0.9960) as the methanol mole fraction increases. This is consistent with methanol's smaller molecular size and weaker intermolecular hydrogen-bonding network compared to ethanol, resulting in lower viscosity at the methanol-rich end. The near-linear dependence suggests relatively ideal mixing behavior with minimal excess viscosity effects in this system at 303.15 K.

**Core claims:**
- For the methanol + ethanol binary liquid mixture at 303.15 K and 81.5 kPa (DOI 10.1021/je800633a), dynamic viscosity decreases monotonically from 0.000968 Pa·s at x(methanol) = 0.0417 to 0.000556 Pa·s at x(methanol) = 0.9166 across 12 data points measured by capillary tube (Ostwald–Ubbelohde).
- The near-linear decrease in viscosity with increasing methanol mole fraction (R² = 0.9960) suggests relatively ideal mixing behavior with minimal excess viscosity effects, consistent with methanol's smaller molecular size and weaker hydrogen-bonding network compared to ethanol.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#2 | 「GLOBlit_11337」 | 「PROPblock_16」 | 「GLOBcomp_2, GLOBcomp_4」 | 「GLOBprop_4」 | 「Dynamic viscosity measurements for the binary mixture methanol + ethanol at 303.15 K and 81.5 kPa as a function of methanol mole fraction.」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


