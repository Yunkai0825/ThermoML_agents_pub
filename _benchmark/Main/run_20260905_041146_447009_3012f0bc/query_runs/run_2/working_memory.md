# Working Memory

## ID Catalog
<!-- PROTECTED — never compacted. Auto-populated by catalog ops. -->
### Resolved Entities
| type | global_id | registry_id | name |
|------|--------|----|------|
| comp | GLOBcomp_4 | methanol | methanol |
| comp | GLOBcomp_1 | water | water |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find experimental viscosity data for methanol+water binary mixtures at 298.15 K → stored as L1_query_1 · validation: FLAGGED(1)

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: FLAGGED(1)

**Summary:** Dynamic viscosity of methanol + water binary mixtures at 298.15 K and 101.0 kPa is reported from DOI 10.1016/j.jct.2007.05.004, spanning the full composition range. Pure methanol viscosity is 0.000545 Pa·s and pure water is 0.00089 Pa·s. The system exhibits a pronounced positive deviation from ideal mixing, with a viscosity maximum of 0.001554 Pa·s near a water mole fraction of approximately 0.70, roughly 2.9 times the pure methanol value and 1.7 times the pure water value. Twelve data points at 298.15 K are tabulated at water mole fractions from 0 to 1.0. Two additional narrower-range datasets from DOI 10.1021/je0600810 and DOI 10.1021/je2003622 provide complementary viscosity values in the methanol-dilute region at the same temperature and pressure.

**Answer:**

#### Viscosity of Methanol + Water Binary Mixtures at 298.15 K

##### Data Source
The most comprehensive dataset was found in **DOI: 10.1016/j.jct.2007.05.004** (GLOBlit_2825, PROPblock_9), which reports dynamic viscosity (η, Pa·s) for the methanol (GLOBcomp_4) + water (GLOBcomp_1) binary system across the full composition range at three temperatures (293.15–303.15 K) and 101 kPa.

##### Complete Data at 298.15 K (13 points, 12 shown by inspection)

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *mole fraction of water* | *η (Pa·s)* |
|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「0 (pure methanol)」 | 「0.000545」 |
| WM_L1#1_Table#1_Row#2 | 「0.049」 | 「0.000607」 |
| WM_L1#1_Table#1_Row#3 | 「0.0993」 | 「0.000677」 |
| WM_L1#1_Table#1_Row#4 | 「0.1973」 | 「0.000821」 |
| WM_L1#1_Table#1_Row#5 | 「0.2983」 | 「0.000987」 |
| WM_L1#1_Table#1_Row#6 | 「0.3985」 | 「0.00115」 |
| WM_L1#1_Table#1_Row#7 | 「0.5994」 | 「0.001463」 |
| WM_L1#1_Table#1_Row#8 | 「0.6997」 | 「0.001554」 |
| WM_L1#1_Table#1_Row#9 | 「0.7986」 | 「0.001542」 |
| WM_L1#1_Table#1_Row#10 | 「0.8999」 | 「0.001317」 |
| WM_L1#1_Table#1_Row#11 | 「0.9512」 | 「0.001121」 |
| WM_L1#1_Table#1_Row#12 | 「1.0 (pure water)」 | 「0.00089」 |

All measurements at **T = 298.15 K**, **P = 101.0 kPa**.

##### Pure Component Values (from the same dataset)
- **Pure methanol** (x_water = 0): η = 0.000545 Pa·s (0.545 mPa·s)
- **Pure water** (x_water = 1): η = 0.00089 Pa·s (0.89 mPa·s)

##### Key Observations — Deviation from Ideal Mixing

The data reveal a pronounced **positive deviation** from linear (ideal) mixing of viscosity. The viscosity reaches a maximum of **0.001554 Pa·s** (1.554 mPa·s) near x_water ≈ 0.70, which is substantially above both pure-component values. **Derived ratios** (computed by dividing inspected values): the maximum is roughly 0.001554 / 0.00089 ≈ 1.7× the viscosity of pure water, and 0.001554 / 0.000545 ≈ 2.9× that of pure methanol. These ratios are arithmetic derived from the inspected data rows, not direct database entries. This behavior indicates strong intermolecular interactions (hydrogen bonding network enhancement) in the methanol–water mixture at water-rich compositions.

Near equimolar composition (x_water ≈ 0.5–0.6), the viscosity is approximately 0.001463 Pa·s (at x_water = 0.5994), already substantially elevated above both pure components.

##### Additional Datasets Found

Two other blocks contain methanol+water viscosity data at 298.15 K but cover narrower composition ranges:

**PROPblock_3** (DOI: 10.1021/je0600810, GLOBlit_8869) — volume fraction of methanol, 3 points at 298.15 K, P = 101.0 kPa:

**WM_L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *φ_v (methanol)* | *η (Pa·s)* |
|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「0.01」 | 「0.0010844」 |
| WM_L1#1_Table#2_Row#2 | 「0.2」 | 「0.0013106」 |
| WM_L1#1_Table#2_Row#3 | 「0.3」 | 「0.0014712」 |

**PROPblock_1** (DOI: 10.1021/je2003622, GLOBlit_9571) — mass fraction of methanol, 4 points at 298.15 K, P = 101.0 kPa:

**WM_L1#1_Table#3_(Query_L1#1_Answer):**

| *row_id* | *w (methanol)* | *η (Pa·s)* |
|---|---|---|
| WM_L1#1_Table#3_Row#1 | 「0.0806」 | 「0.0010844」 |
| WM_L1#1_Table#3_Row#2 | 「0.1647」 | 「0.0013106」 |
| WM_L1#1_Table#3_Row#3 | 「0.2526」 | 「0.0014712」 |
| WM_L1#1_Table#3_Row#4 | 「0.3446」 | 「0.0014475」 |

These provide complementary data in the methanol-dilute region but do not span the full composition range.

**Core claims:**
- Dynamic viscosity of methanol + water mixtures at 298.15 K and 101.0 kPa exhibits a pronounced positive deviation from linear mixing, with viscosity reaching a maximum of 0.001554 Pa·s near x_water ≈ 0.70, substantially above both pure methanol (0.000545 Pa·s) and pure water (0.00089 Pa·s).

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#4 | 「GLOBlit_2825」 | 「PROPblock_9」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of methanol + water binary mixtures across the full composition range at 298.15 K and 101 kPa.」 |
| WM_L1#1_Table#5 | 「GLOBlit_8869」 | 「PROPblock_3」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of methanol + water at 298.15 K and 101 kPa, reported vs. volume fraction of methanol (3 points).」 |
| WM_L1#1_Table#6 | 「GLOBlit_9571」 | 「PROPblock_1」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of methanol + water at 298.15 K and 101 kPa, reported vs. mass fraction of methanol (4 points).」 |

*Not stored here: 3 verbatim data_inspections table(s); 2 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(1) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNINSPECTED_VALUE** PROPblock_9: 1.7 exists in PROPblock_9's database table but was never shown in an inspection of this run


