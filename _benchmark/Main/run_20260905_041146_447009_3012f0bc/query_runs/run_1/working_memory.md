# Working Memory

## ID Catalog
<!-- PROTECTED — never compacted. Auto-populated by catalog ops. -->
### Resolved Entities
| type | global_id | registry_id | name |
|------|--------|----|------|
| comp | GLOBcomp_2 | ethanol | ethanol |
| comp | GLOBcomp_1 | water | water |
| prop | GLOBprop_4 | viscosity_pa_s | Viscosity, Pa*s |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find experimental viscosity data for ethanol+water binary mixtures at 298.15 K → stored as L1_query_1 · validation: PASS

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: PASS

**Summary:** Dynamic viscosity of ethanol (GLOBcomp_2) + water (GLOBcomp_1) binary mixtures at 298.15 K was reported from two ThermoML datasets. Dataset 1 (DOI: 10.1016/j.jct.2007.05.004, GLOBlit_2825, PROPblock_11) at 101.0 kPa provides 12 points with composition as mole fraction of water, spanning pure ethanol (η = 0.001082 Pa·s) to pure water (η = 0.000890 Pa·s), with a viscosity maximum of 0.002300 Pa·s at x(water) ≈ 0.80. Dataset 2 (DOI: 10.1016/j.jct.2018.02.022, GLOBlit_5201, PROPblock_21) at 92.3 kPa provides 25 points with composition as mole fraction of ethanol, spanning pure water (η = 0.00089689 Pa·s) to pure ethanol (η = 0.0010914 Pa·s), with a viscosity maximum of 0.0024286 Pa·s at x(ethanol) ≈ 0.25 (x(water) ≈ 0.75). Both datasets show a large positive deviation from ideal mixing: pure component viscosities are near 0.001 Pa·s, yet the mixture viscosity peaks above 0.0024 Pa·s, exceeding a factor of 2, attributed to strong hydrogen-bonding interactions and microheterogeneity. The viscosity maximum is shifted toward the water-rich side rather than occurring at equimolar composition.

**Answer:**

#### Dynamic Viscosity of Ethanol + Water Binary Mixtures at 298.15 K

Two comprehensive datasets were found in the ThermoML database for the dynamic viscosity of ethanol (GLOBcomp_2) + water (GLOBcomp_1) binary mixtures at 298.15 K.

---

##### Dataset 1 — DOI: 10.1016/j.jct.2007.05.004 (GLOBlit_2825, PROPblock_11)

Pressure: 101.0 kPa. Composition expressed as mole fraction of water.

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *x(water)* | *η (Pa·s)* |
|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「0 (pure ethanol)」 | 「0.001082」 |
| WM_L1#1_Table#1_Row#2 | 「0.0501」 | 「0.001153」 |
| WM_L1#1_Table#1_Row#3 | 「0.0986」 | 「0.001232」 |
| WM_L1#1_Table#1_Row#4 | 「0.1961」 | 「0.001380」 |
| WM_L1#1_Table#1_Row#5 | 「0.2961」 | 「0.001531」 |
| WM_L1#1_Table#1_Row#6 | 「0.3991」 | 「0.001659」 |
| WM_L1#1_Table#1_Row#7 | 「0.5989」 | 「0.002115」 |
| WM_L1#1_Table#1_Row#8 | 「0.6991」 | 「0.002275」 |
| WM_L1#1_Table#1_Row#9 | 「0.8001」 | 「0.002300」 |
| WM_L1#1_Table#1_Row#10 | 「0.8996」 | 「0.001860」 |
| WM_L1#1_Table#1_Row#11 | 「0.9499」 | 「0.001388」 |
| WM_L1#1_Table#1_Row#12 | 「1 (pure water)」 | 「0.000890」 |

**Pure component values:** η(ethanol) = 0.001082 Pa·s; η(water) = 0.000890 Pa·s.

---

##### Dataset 2 — DOI: 10.1016/j.jct.2018.02.022 (GLOBlit_5201, PROPblock_21)

Pressure: 92.3 kPa. Composition expressed as mole fraction of ethanol. This dataset has 25 data points at 298.15 K (shape-preserving subset of shown rows below); the full matched range spans x(ethanol) = 0–1 with η = 0.00089689–0.0024286 Pa·s.

**WM_L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *x(ethanol)* | *η (Pa·s)* |
|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「0 (pure water)」 | 「0.00089689」 |
| WM_L1#1_Table#2_Row#2 | 「0.0201」 | 「0.001098」 |
| WM_L1#1_Table#2_Row#3 | 「0.1004」 | 「0.0019469」 |
| WM_L1#1_Table#2_Row#4 | 「0.1499」 | 「0.0022424」 |
| WM_L1#1_Table#2_Row#5 | 「0.1984」 | 「0.0023706」 |
| WM_L1#1_Table#2_Row#6 | 「0.2499」 | 「0.0024286」 |
| WM_L1#1_Table#2_Row#7 | 「0.3499」 | 「0.0022633」 |
| WM_L1#1_Table#2_Row#8 | 「0.3990」 | 「0.0021697」 |
| WM_L1#1_Table#2_Row#9 | 「0.4989」 | 「0.0019557」 |
| WM_L1#1_Table#2_Row#10 | 「0.5495」 | 「0.0018796」 |
| WM_L1#1_Table#2_Row#11 | 「0.6067」 | 「0.0017439」 |
| WM_L1#1_Table#2_Row#12 | 「0.6956」 | 「0.0015722」 |
| WM_L1#1_Table#2_Row#13 | 「0.8475」 | 「0.0013415」 |
| WM_L1#1_Table#2_Row#14 | 「1 (pure ethanol)」 | 「0.0010914」 |

**Pure component values:** η(water) = 0.00089689 Pa·s; η(ethanol) = 0.0010914 Pa·s.

---

##### Key Observations

**Near-equimolar composition:** At x(ethanol) ≈ 0.50, Dataset 2 (GLOBlit_5201, PROPblock_21) gives η = 0.0019557 Pa·s. In Dataset 1 (GLOBlit_2825, PROPblock_11), the nearest point is x(water) = 0.5989 (i.e., x(ethanol) ≈ 0.40), giving η = 0.002115 Pa·s. Both datasets show that the viscosity near equimolar composition is roughly double that of either pure component.

**Maximum viscosity:** The viscosity maximum does not occur at equimolar composition but is shifted toward the water-rich side. In Dataset 1 (GLOBlit_2825, PROPblock_11), the maximum is at x(water) ≈ 0.80 (η = 0.002300 Pa·s). In Dataset 2 (GLOBlit_5201, PROPblock_21), the maximum is at x(ethanol) ≈ 0.25 (i.e., x(water) ≈ 0.75), with η = 0.0024286 Pa·s. This is a well-known feature of the ethanol–water system, attributed to strong hydrogen-bonding interactions and microheterogeneity in the mixture structure.

**Deviation from ideal mixing:** Both pure component viscosities are near 0.001 Pa·s, yet the mixture viscosity peaks above 0.0024 Pa·s — a positive deviation exceeding a factor of 2. This large positive excess viscosity reflects the extensive hydrogen-bond network reorganization that occurs when ethanol and water are mixed.

**Core claims:**
- Two ThermoML datasets provide dynamic viscosity data for ethanol + water binary mixtures at 298.15 K: Dataset 1 (DOI 10.1016/j.jct.2007.05.004) at 101.0 kPa with 12 data points spanning η from 0.000890 Pa·s (pure water) to 0.002300 Pa·s, and Dataset 2 (DOI 10.1016/j.jct.2018.02.022) at 92.3 kPa with 25 data points spanning η from 0.00089689 Pa·s (pure water) to 0.0024286 Pa·s.
- The viscosity maximum is shifted toward the water-rich side of the composition range: Dataset 1 shows a maximum of 0.002300 Pa·s at x(water) ≈ 0.80, and Dataset 2 shows a maximum of 0.0024286 Pa·s at x(ethanol) ≈ 0.25 (x(water) ≈ 0.75).
- Both pure component viscosities are near 0.001 Pa·s, yet the mixture viscosity peaks above 0.0024 Pa·s, indicating a large positive excess viscosity attributed to extensive hydrogen-bond network reorganization upon mixing.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#3 | 「GLOBlit_2825」 | 「PROPblock_11」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of ethanol + water binary mixture at 298.15 K and 101.0 kPa across full composition range.」 |
| WM_L1#1_Table#4 | 「GLOBlit_5201」 | 「PROPblock_21」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of ethanol + water binary mixture at 298.15 K and 92.3 kPa with 25 data points across full composition range.」 |

*Not stored here: 3 verbatim data_inspections table(s); 3 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


