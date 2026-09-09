# Working Memory

## ID Catalog
<!-- PROTECTED — never compacted. Auto-populated by catalog ops. -->
### Resolved Entities
| type | global_id | registry_id | name |
|------|--------|----|------|
| comp | GLOBcomp_107 | lithium_chloride | lithium chloride |
| comp | GLOBcomp_1 | water | water |
| prop | GLOBprop_56 | mean_ionic_activity_coefficient_{DOIcomp_id} | Mean ionic activity coefficient |
| meas | GLOBmeas_185 | calculated_from_emf_cell_potential | Calculated from EMF cell potential |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|
| lit | GLOBlit_1540 | 2014-zha-li-3 | 10.1016/j.fluid.2014.08.026 |

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find activity coefficient measurements for aqueous lithium chloride (LiCl) near 25 °C (298.15 K), including the concentr → stored as L1_query_1 · validation: PASS

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: PASS

**Summary:** ThermoML contains mean ionic activity coefficient (γ±) data for aqueous lithium chloride (LiCl, GLOBcomp_107) with water (GLOBcomp_1) at 298.15 K and 101.0 kPa, sourced from DOI 10.1016/j.fluid.2014.08.026 (GLOBlit_1540), property GLOBprop_56, method GLOBmeas_185 (calculated from EMF cell potential), block PROPblock_13. The dataset comprises 141 data points spanning molality from 0.0033 to 1.5555 mol/kg. γ± ranges from 0.7406 to 0.9425, showing a characteristic non-monotonic U-shaped trend: near unity at very low molality (~0.94 at 0.003 mol/kg), decreasing to a minimum of about 0.74 at intermediate molalities, then rising again to ~0.85 near 1.5 mol/kg.

**Answer:**

#### Activity Coefficient Data for Aqueous Lithium Chloride (LiCl) at 25 °C in ThermoML

##### Data Availability

Yes — ThermoML contains **mean ionic activity coefficient (γ±)** data for the binary system **lithium chloride + water** at exactly **298.15 K** and **101.0 kPa**.

##### Identifiers

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *Entity* | *Global ID* | *Name* |
|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「Lithium chloride」 | 「GLOBcomp_107」 | 「LiCl」 |
| WM_L1#1_Table#1_Row#2 | 「Water」 | 「GLOBcomp_1」 | 「H₂O」 |
| WM_L1#1_Table#1_Row#3 | 「Property」 | 「GLOBprop_56」 | 「Mean ionic activity coefficient」 |
| WM_L1#1_Table#1_Row#4 | 「Measurement method」 | 「GLOBmeas_185」 | 「Calculated from EMF cell potential」 |

##### Source

- **DOI:** 10.1016/j.fluid.2014.08.026 (GLOBlit_1540)
- **Block:** PROPblock_13
- **Total data points:** 141

##### Concentration Range

The data covers **molality of LiCl from 0.0033 to 1.5555 mol/kg** (roughly 0.003 to 1.56 mol/kg), all at a fixed temperature of 298.15 K and pressure of 101.0 kPa.

##### Representative Data Points

**Low-molality region (dilute):**

**WM_L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *Molality (mol/kg)* | *γ±* |
|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「0.0033」 | 「0.9425」 |
| WM_L1#1_Table#2_Row#2 | 「0.0033」 | 「0.9398」 |
| WM_L1#1_Table#2_Row#3 | 「0.0035」 | 「0.9388」 |
| WM_L1#1_Table#2_Row#4 | 「0.004」 | 「0.935」 |

**High-molality region (concentrated):**

**WM_L1#1_Table#3_(Query_L1#1_Answer):**

| *row_id* | *Molality (mol/kg)* | *γ±* |
|---|---|---|
| WM_L1#1_Table#3_Row#1 | 「1.485」 | 「0.8424」 |
| WM_L1#1_Table#3_Row#2 | 「1.5095」 | 「0.839」 |
| WM_L1#1_Table#3_Row#3 | 「1.5483」 | 「0.845」 |
| WM_L1#1_Table#3_Row#4 | 「1.5555」 | 「0.8461」 |

**Overall range of γ±:** 0.7406 – 0.9425 across all 141 points.

##### Chemistry Insight

The data shows the characteristic behavior of LiCl in water: at very low molality, γ± is close to unity (~0.94 at 0.003 mol/kg), then decreases with increasing concentration — reaching a minimum of about 0.74 at intermediate molalities — before rising again at higher concentrations (γ± ≈ 0.85 near 1.5 mol/kg). This non-monotonic trend (with considerable scatter among the 141 measured points around the underlying U-shaped curve) is typical of strong 1:1 electrolytes like LiCl, where short-range ion–solvent interactions cause the activity coefficient to increase again after the Debye–Hückel minimum. The values were derived from EMF (electromotive force) cell potential measurements, a standard electrochemical technique for precise activity coefficient determination.

**Core claims:**
- ThermoML contains mean ionic activity coefficient (γ±) data for the binary system lithium chloride + water at 298.15 K and 101.0 kPa, sourced from DOI 10.1016/j.fluid.2014.08.026.
- The dataset comprises 141 data points covering LiCl molality from 0.0033 to 1.5555 mol/kg, with γ± values ranging from 0.7406 to 0.9425.
- The activity coefficients were calculated from EMF (electromotive force) cell potential measurements.
- The data exhibit a non-monotonic (U-shaped) trend: γ± is close to unity at very low molality (~0.94 at 0.003 mol/kg), decreases to a minimum of about 0.74 at intermediate molalities, and rises again to ~0.85 near 1.5 mol/kg, which is characteristic of strong 1:1 electrolytes like LiCl.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#4 | 「GLOBlit_1540」 | 「PROPblock_13」 | 「GLOBcomp_107, GLOBcomp_1」 | 「GLOBprop_56」 | 「Mean ionic activity coefficient measurements for lithium chloride in water at 298.15 K and 101.0 kPa, covering molality 0.0033 to 1.5555 mol/kg, 141 data points calculated from EMF cell potential.」 |

*Not stored here: 2 verbatim data_inspections table(s); 5 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


