# Working Memory

## ID Catalog
<!-- PROTECTED — never compacted. Auto-populated by catalog ops. -->
### Resolved Entities
| type | global_id | registry_id | name |
|------|--------|----|------|
| comp | GLOBcomp_15 | acetonitrile | acetonitrile |
| comp | GLOBcomp_4 | methanol | methanol |
| prop | GLOBprop_13 | surface_tension_liquidgas_n_m | Surface tension liquid-gas, N/m |
| meas | GLOBmeas_22 | pendant_drop_shape | Pendant drop shape |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|
| lit | GLOBlit_8821 | 2006-tah-mod-0 | 10.1021/je050519g |

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find surface tension measurements for methanol + acetonitrile binary mixtures near room temperature (293-303 K) → stored as L1_query_1 · validation: PASS

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: PASS

**Summary:** Surface tension (liquid–gas) of binary mixtures of acetonitrile (C₂H₃N) and methanol (CH₄O) was measured at 293.15 K using the pendant drop shape method, as reported in DOI 10.1021/je050519g. Seven compositions were studied. Surface tension increases monotonically with acetonitrile mole fraction: from 0.0238 N/m at x(acetonitrile) = 0.1001 to 0.02885 N/m at x(acetonitrile) = 0.8956. Intermediate values are 0.02473 N/m (x = 0.2011), 0.02553 N/m (x = 0.2996), 0.02685 N/m (x = 0.4997), 0.02794 N/m (x = 0.7012), and 0.02842 N/m (x = 0.8009). The smooth monotonic trend with no extrema suggests relatively ideal mixing behavior at the liquid–gas interface. Only one dataset at a single temperature (293.15 K) was found in the ThermoML database for this binary system.

**Answer:**

#### Surface Tension of Methanol + Acetonitrile Binary Mixtures near Room Temperature

##### Source
**DOI:** 10.1021/je050519g (GLOBlit_8821)
**Title:** *Density and Surface Tension of Binary Mixtures of Acetonitrile + 1-Alkanol at 293.15 K*
**Block:** PROPblock_13 (binary system, declared)

##### Experimental Details
- **Compounds:** Acetonitrile (GLOBcomp_15, C₂H₃N) + Methanol (GLOBcomp_4, CH₄O)
- **Property:** Surface tension, liquid–gas (GLOBprop_13), in N/m
- **Measurement method:** Pendant drop shape (GLOBmeas_22)
- **Temperature:** 293.15 K (fixed constraint)
- **Composition variable:** Mole fraction of acetonitrile in the liquid phase

##### Data Table (T = 293.15 K)

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *x(acetonitrile)* | *Surface tension γ (N/m)* |
|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「0.1001」 | 「0.0238」 |
| WM_L1#1_Table#1_Row#2 | 「0.2011」 | 「0.02473」 |
| WM_L1#1_Table#1_Row#3 | 「0.2996」 | 「0.02553」 |
| WM_L1#1_Table#1_Row#4 | 「0.4997」 | 「0.02685」 |
| WM_L1#1_Table#1_Row#5 | 「0.7012」 | 「0.02794」 |
| WM_L1#1_Table#1_Row#6 | 「0.8009」 | 「0.02842」 |
| WM_L1#1_Table#1_Row#7 | 「0.8956」 | 「0.02885」 |

##### Chemical Insight
The surface tension increases monotonically with increasing acetonitrile mole fraction across the full composition range (0.1001–0.8956), spanning from 0.0238 N/m (methanol-rich, x = 0.1001) to 0.02885 N/m (acetonitrile-rich, x = 0.8956). The smooth, monotonic trend with no extrema suggests relatively ideal mixing behavior at the liquid–gas interface for this system.

Only one dataset was found in the ThermoML database for this binary system, and it is at a single temperature of 293.15 K, which falls within the requested near-room-temperature window. No data at other temperatures within this window were found.

**Core claims:**
- At 293.15 K, the surface tension of methanol + acetonitrile binary mixtures increases monotonically with increasing acetonitrile mole fraction, ranging from 0.0238 N/m at x(acetonitrile) = 0.1001 to 0.02885 N/m at x(acetonitrile) = 0.8956, with no extrema observed.
- The data were measured by the pendant drop shape method and reported in a single dataset (DOI 10.1021/je050519g); no additional ThermoML data at other near-room-temperature conditions were found for this binary system.
- The smooth, monotonic trend in surface tension suggests relatively ideal mixing behavior at the liquid–gas interface for this system.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#2 | 「GLOBlit_8821」 | 「PROPblock_13」 | 「GLOBcomp_4, GLOBcomp_15」 | 「GLOBprop_13」 | 「Surface tension (liquid–gas) measurements for acetonitrile + methanol binary mixture at 293.15 K, measured by pendant drop shape method.」 |

*Not stored here: 1 verbatim data_inspections table(s); 5 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


