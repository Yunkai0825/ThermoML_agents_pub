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
| lit | GLOBlit_5585 | 2019-meh-haj-0 | 10.1016/j.jct.2019.105880 |

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find viscosity data for isopropanol (2-propanol) + water binary mixtures at room temperature (293-298 K) → stored as L1_query_1 · validation: PASS

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: PASS

**Summary:** Dynamic viscosity (Pa·s) data for the binary mixture of propan-2-ol (2-propanol) + water, measured by falling/rolling sphere viscometry in the liquid phase at 100 kPa, from DOI 10.1016/j.jct.2019.105880. The composition range covers mass fractions of propan-2-ol from 0.1 to 0.3. Within the 293–298 K window, six data points are reported: at 293.15 K, viscosities are 0.001633 Pa·s (w = 0.1), 0.002485 Pa·s (w = 0.2), and 0.003172 Pa·s (w = 0.3); at 298.15 K, viscosities are 0.001395 Pa·s (w = 0.1), 0.002045 Pa·s (w = 0.2), and 0.002555 Pa·s (w = 0.3). Viscosity increases with propan-2-ol mass fraction in this range and decreases with increasing temperature. The full data block spans 288.15–303.15 K with viscosities from 0.001208 to 0.004014 Pa·s. No kinematic viscosity data were found for this system in the requested temperature range.

**Answer:**

#### Viscosity Data for 2-Propanol + Water Binary Mixtures at Room Temperature (293–298 K)

##### Source
**DOI:** 10.1016/j.jct.2019.105880 (GLOBlit_5585, PROPblock_12)

**Property:** Dynamic viscosity (Pa·s), measured by falling/rolling sphere viscometry, liquid phase, at 100 kPa.

**System:** Binary mixture of propan-2-ol (2-propanol, GLOBcomp_6) + water (GLOBcomp_1).

**Composition range covered:** Mass fraction of propan-2-ol from 0.1 to 0.3.
**Full block temperature range:** 288.15–303.15 K (12 data points total).

##### Data Points in the 293–298 K Window

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *T (K)* | *w(propan-2-ol)* | *Dynamic Viscosity (Pa·s)* |
|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「293.15」 | 「0.1」 | 「0.001633」 |
| WM_L1#1_Table#1_Row#2 | 「293.15」 | 「0.2」 | 「0.002485」 |
| WM_L1#1_Table#1_Row#3 | 「293.15」 | 「0.3」 | 「0.003172」 |
| WM_L1#1_Table#1_Row#4 | 「298.15」 | 「0.1」 | 「0.001395」 |
| WM_L1#1_Table#1_Row#5 | 「298.15」 | 「0.2」 | 「0.002045」 |
| WM_L1#1_Table#1_Row#6 | 「298.15」 | 「0.3」 | 「0.002555」 |

##### Key Observations

- At both temperatures, viscosity increases with increasing propan-2-ol mass fraction in this composition range (0.1–0.3), consistent with the well-known viscosity maximum of the isopropanol–water system that occurs at higher alcohol concentrations.
- Raising the temperature from 293.15 K to 298.15 K noticeably decreases the viscosity at each composition, as expected from the Arrhenius-type temperature dependence of liquid viscosity (e.g., from 0.001633 to 0.001395 Pa·s at w = 0.1, and from 0.003172 to 0.002555 Pa·s at w = 0.3).
- The full block extends from 288.15 K to 303.15 K with viscosities spanning 0.001208–0.004014 Pa·s.

**Note:** No kinematic viscosity (GLOBprop_40) data were found in the database for this binary system in the requested temperature range. Only dynamic viscosity data are available from this source.

**Core claims:**
- Dynamic viscosity data for the binary mixture of propan-2-ol + water at 100 kPa were found from DOI 10.1016/j.jct.2019.05880, covering mass fractions of propan-2-ol from 0.1 to 0.3 and temperatures of 293.15 K and 298.15 K within the requested room-temperature window.
- At both 293.15 K and 298.15 K, dynamic viscosity increases with increasing propan-2-ol mass fraction over the 0.1–0.3 range, with values ranging from 0.001633 Pa·s (w = 0.1, 293.15 K) to 0.003172 Pa·s (w = 0.3, 293.15 K) and from 0.001395 Pa·s (w = 0.1, 298.15 K) to 0.002555 Pa·s (w = 0.3, 298.15 K).
- Raising the temperature from 293.15 K to 298.15 K decreases the dynamic viscosity at each composition, consistent with Arrhenius-type temperature dependence of liquid viscosity.
- No kinematic viscosity data were found in the database for this binary system in the requested temperature range; only dynamic viscosity data are available from this source.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#2 | 「GLOBlit_5585」 | 「PROPblock_12」 | 「GLOBcomp_1, GLOBcomp_6」 | 「GLOBprop_4」 | 「Dynamic viscosity (Pa·s) for propan-2-ol + water binary mixture, mass fraction of propan-2-ol 0.1–0.3, 288.15–303.15 K, 100 kPa.」 |

*Not stored here: 1 verbatim data_inspections table(s); 3 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


