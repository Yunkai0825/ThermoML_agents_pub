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
- [L1] Find dynamic viscosity data for the binary mixture of acetonitrile + N,N-dimethylformamide (DMF) at or near 303.15 K as  → stored as L1_query_1 · validation: PASS

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: PASS

**Summary:** Dynamic viscosity data for the binary system acetonitrile + N,N-dimethylformamide (DMF) at 303.15 K were found in two ThermoML sources. Source 1 (DOI 10.1016/j.jct.2014.02.019, PROPblock_6) reports 5 points on a mass-fraction basis at 101.0 kPa, with η ranging from 0.0003269 Pa·s (pure acetonitrile) to 0.000755 Pa·s (pure DMF). Source 2 (DOI 10.1021/acs.jced.8b00176, PROPblock_18) reports 11 points on a mole-fraction basis at 100.0 kPa, with η ranging from 0.00032 Pa·s (pure acetonitrile) to 0.00077 Pa·s (pure DMF). Both datasets show a monotonic, slightly concave increase in viscosity with increasing DMF content, consistent with stronger intermolecular interactions in DMF. The two sources agree well at the pure-component endpoints, with minor differences attributed to different measurement techniques and slight pressure differences.

**Answer:**

#### Dynamic Viscosity of Acetonitrile + N,N-Dimethylformamide (DMF) at 303.15 K

Two ThermoML data sources were found for the binary system acetonitrile (CH₃CN) + DMF (C₃H₇NO) containing dynamic viscosity measurements at 303.15 K.

---

##### Source 1 — Mass-fraction basis (capillary/Ubbelohde viscometer)

**DOI:** 10.1016/j.jct.2014.02.019 (GLOBlit_4124, PROPblock_6)
**Conditions:** T = 303.15 K, P = 101.0 kPa

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *w(DMF)* | *η (Pa·s)* |
|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「0」 | 「0.0003269」 |
| WM_L1#1_Table#1_Row#2 | 「0.25」 | 「0.0003598」 |
| WM_L1#1_Table#1_Row#3 | 「0.50」 | 「0.00046」 |
| WM_L1#1_Table#1_Row#4 | 「0.75」 | 「0.0006145」 |
| WM_L1#1_Table#1_Row#5 | 「1.00」 | 「0.000755」 |

5 data points spanning the full mass-fraction range. The full block covers 298.15–313.15 K with 20 total points.

---

##### Source 2 — Mole-fraction basis (falling-sphere viscometer)

**DOI:** 10.1021/acs.jced.8b00176 (GLOBlit_7481, PROPblock_18)
**Conditions:** T = 303.15 K, P = 100.0 kPa

**WM_L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *x(DMF)* | *η (Pa·s)* |
|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「0」 | 「0.00032」 |
| WM_L1#1_Table#2_Row#2 | 「0.0989」 | 「0.00039」 |
| WM_L1#1_Table#2_Row#3 | 「0.1916」 | 「0.00042」 |
| WM_L1#1_Table#2_Row#4 | 「0.2925」 | 「0.00046」 |
| WM_L1#1_Table#2_Row#5 | 「0.3932」 | 「0.00051」 |
| WM_L1#1_Table#2_Row#6 | 「0.5029」 | 「0.00057」 |
| WM_L1#1_Table#2_Row#7 | 「0.6002」 | 「0.00061」 |
| WM_L1#1_Table#2_Row#8 | 「0.6931」 | 「0.00065」 |
| WM_L1#1_Table#2_Row#9 | 「0.7926」 | 「0.00070」 |
| WM_L1#1_Table#2_Row#10 | 「0.8996」 | 「0.00075」 |
| WM_L1#1_Table#2_Row#11 | 「1.0000」 | 「0.00077」 |

11 data points spanning the full mole-fraction range. The full block covers 298.15–323.15 K with 66 total points.

---

##### Chemical Insight

Both datasets show a monotonic increase in dynamic viscosity with increasing DMF content at 303.15 K. The increase is smooth and slightly concave, consistent with the stronger intermolecular interactions (dipole–dipole and hydrogen-bond-accepting character) in DMF compared to acetonitrile.

From Source 1 (PROPblock_6), pure acetonitrile has η = 0.0003269 Pa·s and pure DMF has η = 0.000755 Pa·s at P = 101.0 kPa. From Source 2 (PROPblock_18), pure acetonitrile has η = 0.00032 Pa·s and pure DMF has η = 0.00077 Pa·s at P = 100.0 kPa. The two sources agree well at the pure-component endpoints, with minor differences attributable to different measurement techniques and slight pressure differences (PROPblock_6: 101.0 kPa; PROPblock_18: 100.0 kPa).

**Core claims:**
- Two independent ThermoML sources provide dynamic viscosity data for the acetonitrile + DMF binary system at 303.15 K across the full composition range.
- Source 1 (DOI 10.1016/j.jct.2014.02.019) reports 5 data points on a mass-fraction basis at P = 101.0 kPa, with η ranging from 0.0003269 Pa·s (pure acetonitrile) to 0.000755 Pa·s (pure DMF).
- Source 2 (DOI 10.1021/acs.jced.8b00176) reports 11 data points on a mole-fraction basis at P = 100.0 kPa, with η ranging from 0.00032 Pa·s (pure acetonitrile) to 0.00077 Pa·s (pure DMF).
- Both datasets show a monotonic increase in dynamic viscosity with increasing DMF content at 303.15 K, with a smooth, slightly concave composition dependence.
- The two sources agree well at the pure-component endpoints, with minor differences attributable to different measurement techniques and slight pressure differences.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#3 | 「GLOBlit_4124」 | 「PROPblock_6」 | 「GLOBcomp_18, GLOBcomp_15」 | 「GLOBprop_4」 | 「Dynamic viscosity of acetonitrile + N,N-dimethylformamide at 303.15 K (mass-fraction basis, 5 data points at 303.15 K, full block 298.15–313.15 K, P = 101.0 kPa).」 |
| WM_L1#1_Table#4 | 「GLOBlit_7481」 | 「PROPblock_18」 | 「GLOBcomp_18, GLOBcomp_15」 | 「GLOBprop_4」 | 「Dynamic viscosity of acetonitrile + N,N-dimethylformamide at 303.15 K (mole-fraction basis, 11 data points at 303.15 K, full block 298.15–323.15 K, P = 100.0 kPa).」 |

*Not stored here: 2 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


