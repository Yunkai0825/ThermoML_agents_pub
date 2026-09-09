# Working Memory

## ID Catalog
<!-- PROTECTED — never compacted. Auto-populated by catalog ops. -->
### Resolved Entities
| type | global_id | registry_id | name |
|------|--------|----|------|
| comp | GLOBcomp_1 | water | water |
| comp | GLOBcomp_24 | 1,2-ethanediol | 1,2-ethanediol |
| prop | GLOBprop_4 | viscosity_pa_s | Viscosity, Pa*s |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find dynamic viscosity data for water + ethylene glycol binary mixture near 303.15 K → stored as L1_query_1 · validation: PASS

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: PASS

**Summary:** Two independent ThermoML datasets report dynamic viscosity for the water + 1,2-ethanediol (ethylene glycol) binary mixture at 303.15 K across the full composition range. Dataset 1 (DOI 10.1016/j.jct.2018.02.022, concentric cylinders, 92.3 kPa, mole fraction of 1,2-ethanediol) provides 21 matched rows spanning 0.0008385 Pa·s (pure water) to 0.013867 Pa·s (pure EG). Dataset 2 (DOI 10.1021/acs.jced.6b00526, falling sphere, 100.0 kPa, mole fraction of water) provides 11 data points spanning 0.000755 Pa·s (pure water, x(water)=1) to 0.01423 Pa·s (pure EG, x(water)=0). Both datasets show a monotonic increase in viscosity with increasing ethylene glycol content, with pure EG roughly seventeen- to nineteen-fold more viscous than pure water. The viscosity–composition curve is concave upward, characteristic of strongly associating aqueous–diol mixtures. The two datasets are in good mutual agreement. Three additional ThermoML blocks (GLOBlit_8038, GLOBlit_1, GLOBlit_3891) were also identified for possible further comparison.

**Answer:**

#### Dynamic Viscosity of Water + Ethylene Glycol (1,2-Ethanediol) at 303.15 K

Two independent ThermoML datasets provide dynamic viscosity data for the binary mixture of water (GLOBcomp_1) and 1,2-ethanediol (GLOBcomp_24) at exactly 303.15 K, covering the full composition range.

---

##### Dataset 1 — DOI: 10.1016/j.jct.2018.02.022 (GLOBlit_5201, PROPblock_24)

**Method:** Concentric cylinders · **Pressure:** 92.3 kPa · **Composition basis:** mole fraction of 1,2-ethanediol

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *x(1,2-ethanediol)* | *Viscosity (Pa·s)* |
|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「0」 | 「0.0008385」 |
| WM_L1#1_Table#1_Row#2 | 「0.0494」 | 「0.0011644」 |
| WM_L1#1_Table#1_Row#3 | 「0.0986」 | 「0.001555」 |
| WM_L1#1_Table#1_Row#4 | 「0.1483」 | 「0.0019899」 |
| WM_L1#1_Table#1_Row#5 | 「0.2072」 | 「0.0025643」 |
| WM_L1#1_Table#1_Row#6 | 「0.2466」 | 「0.0029649」 |
| WM_L1#1_Table#1_Row#7 | 「0.3399」 | 「0.0040293」 |
| WM_L1#1_Table#1_Row#8 | 「0.3921」 | 「0.0046704」 |
| WM_L1#1_Table#1_Row#9 | 「0.4446」 | 「0.0053492」 |
| WM_L1#1_Table#1_Row#10 | 「0.5485」 | 「0.0067709」 |
| WM_L1#1_Table#1_Row#11 | 「0.6451」 | 「0.0081729」 |
| WM_L1#1_Table#1_Row#12 | 「0.7012」 | 「0.0090846」 |
| WM_L1#1_Table#1_Row#13 | 「0.7435」 | 「0.0098077」 |
| WM_L1#1_Table#1_Row#14 | 「0.7907」 | 「0.010548」 |
| WM_L1#1_Table#1_Row#15 | 「0.8505」 | 「0.011535」 |
| WM_L1#1_Table#1_Row#16 | 「1」 | 「0.013867」 |

Full isotherm stats (21 matched rows at 303.15 K; the above is an RDP shape-preserving subset): viscosity ranges from 0.0008385 to 0.013867 Pa·s.

---

##### Dataset 2 — DOI: 10.1021/acs.jced.6b00526 (GLOBlit_6951, PROPblock_18)

**Method:** Falling sphere · **Pressure:** 100.0 kPa · **Composition basis:** mole fraction of water

**WM_L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *x(water)* | *Viscosity (Pa·s)* |
|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「0」 | 「0.01423」 |
| WM_L1#1_Table#2_Row#2 | 「0.1105」 | 「0.01186」 |
| WM_L1#1_Table#2_Row#3 | 「0.2014」 | 「0.01014」 |
| WM_L1#1_Table#2_Row#4 | 「0.3002」 | 「0.00845」 |
| WM_L1#1_Table#2_Row#5 | 「0.4011」 | 「0.006968」 |
| WM_L1#1_Table#2_Row#6 | 「0.4969」 | 「0.005653」 |
| WM_L1#1_Table#2_Row#7 | 「0.6022」 | 「0.004396」 |
| WM_L1#1_Table#2_Row#8 | 「0.6995」 | 「0.003345」 |
| WM_L1#1_Table#2_Row#9 | 「0.7994」 | 「0.002328」 |
| WM_L1#1_Table#2_Row#10 | 「0.8997」 | 「0.001446」 |
| WM_L1#1_Table#2_Row#11 | 「1」 | 「0.000755」 |

All 11 data points at 303.15 K shown (complete isotherm).

---

##### Chemistry Insight

Both datasets show a monotonic increase in viscosity with increasing ethylene glycol content. From Dataset 1 (PROPblock_24), pure 1,2-ethanediol has a viscosity of 0.013867 Pa·s compared to 0.0008385 Pa·s for pure water — pure EG is roughly an order of magnitude more viscous (computed ratio: 0.013867 ÷ 0.0008385 ≈ seventeen-fold). From Dataset 2 (PROPblock_18), the corresponding pure-component values are 0.01423 Pa·s (pure EG, x(water) = 0) and 0.000755 Pa·s (pure water, x(water) = 1), yielding a similar computed ratio of 0.01423 ÷ 0.000755 ≈ nineteen-fold. This large viscosity difference reflects the extensive hydrogen-bonding network of the diol.

The two datasets are in good agreement. For comparison at a similar mid-range composition: Dataset 1 (PROPblock_24) gives 0.0067709 Pa·s at x(EG) = 0.5485, while Dataset 2 (PROPblock_18) gives 0.005653 Pa·s at x(water) = 0.4969 (i.e., x(EG) = 1 minus 0.4969, a derived complement). The values are consistent within the expected range given the slightly different compositions and pressures. The viscosity–composition curve is concave upward, characteristic of strongly associating aqueous–diol mixtures.

Three additional blocks were also found in the initial search (GLOBlit_8038, GLOBlit_1, GLOBlit_3891) if further comparison is needed.

**Core claims:**
- Two independent ThermoML datasets provide dynamic viscosity data for the water + 1,2-ethanediol binary mixture at 303.15 K across the full composition range, measured by concentric cylinders (92.3 kPa) and falling sphere (100.0 kPa) methods respectively.
- Both datasets show a monotonic increase in viscosity with increasing ethylene glycol mole fraction, with pure 1,2-ethanediol being roughly an order of magnitude more viscous than pure water at 303.15 K.
- From Dataset 1, pure water viscosity is 0.0008385 Pa·s and pure 1,2-ethanediol viscosity is 0.013867 Pa·s; from Dataset 2, the corresponding values are 0.000755 Pa·s and 0.01423 Pa·s.
- The two datasets are in good agreement, and the viscosity–composition curve is concave upward, characteristic of strongly associating aqueous–diol mixtures.
- The large viscosity difference between the pure components reflects the extensive hydrogen-bonding network of the diol.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#3 | 「GLOBlit_5201」 | 「PROPblock_24」 | 「GLOBcomp_24, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of water + 1,2-ethanediol binary mixture at 303.15 K, measured by concentric cylinders at 92.3 kPa, covering full mole fraction range with 21 data points.」 |
| WM_L1#1_Table#4 | 「GLOBlit_6951」 | 「PROPblock_18」 | 「GLOBcomp_24, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of water + 1,2-ethanediol binary mixture at 303.15 K, measured by falling sphere at 100.0 kPa, 11 data points covering full composition range.」 |

*Not stored here: 2 verbatim data_inspections table(s); 3 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


