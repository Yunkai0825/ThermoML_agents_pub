# Working Memory

## ID Catalog
<!-- PROTECTED — never compacted. Auto-populated by catalog ops. -->
### Resolved Entities
| type | global_id | registry_id | name |
|------|--------|----|------|
| comp | GLOBcomp_15 | acetonitrile | acetonitrile |
| comp | GLOBcomp_18 | dimethylformamide | dimethylformamide |
| prop | GLOBprop_4 | viscosity_pa_s | Viscosity, Pa*s |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|
| lit | GLOBlit_7481 | 2018-fat-riy-1 | 10.1021/acs.jced.8b00176 |
| lit | GLOBlit_4124 | 2014-bra-pra-0 | 10.1016/j.jct.2014.02.019 |

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find experimental dynamic viscosity data for acetonitrile + N,N-dimethylformamide binary mixture at equimolar compositio → stored as L1_query_1 · validation: PASS

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: PASS

**Summary:** For the binary system acetonitrile + N,N-dimethylformamide at 298.15 K, the dynamic viscosity nearest to equimolar composition is reported from DOI 10.1021/acs.jced.8b00176 (falling/rolling sphere viscometer, 100.0 kPa). No exact x(DMF) = 0.5000 row exists; the closest composition is x(DMF) = 0.5029, giving η = 0.00061 Pa·s (0.61 mPa·s). Bracketing values at 298.15 K are η = 0.00054 Pa·s at x(DMF) = 0.3932 and η = 0.00065 Pa·s at x(DMF) = 0.6002. A second data block (DOI 10.1016/j.jct.2014.02.019, capillary tube method, 101.0 kPa) reports viscosity on a mass-fraction basis; the equimolar composition (~w(DMF) ≈ 0.64) falls between w(DMF) = 0.50 (η = 0.0005214 Pa·s) and w(DMF) = 0.75 (η = 0.0006465 Pa·s) with no exact match available. Pure-component viscosities at 298.15 K from the same source are approximately 0.00080 Pa·s for DMF and 0.00034 Pa·s for acetonitrile; the near-equimolar mixture value lies between these, consistent with a relatively ideal system showing monotonic increase in viscosity with DMF content.

**Answer:**

#### Dynamic Viscosity of Acetonitrile + N,N-Dimethylformamide at Equimolar Composition and 298.15 K

Two ThermoML data blocks contain dynamic viscosity measurements for the binary system acetonitrile (GLOBcomp_15) + N,N-dimethylformamide (GLOBcomp_18) covering 298.15 K:

---

##### Block 1 — Mole-fraction basis (closest to the requested x₁ = 0.5)

**Source:** DOI 10.1021/acs.jced.8b00176 (GLOBlit_7481, PROPblock_18)  
**Method:** Falling/rolling sphere viscometer  
**Pressure:** 100.0 kPa  

There is **no exact row at x(DMF) = 0.5000**; the nearest composition is **x(DMF) = 0.5029**. Bracketing rows at 298.15 K:

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *BLKpoint_id* | *T (K)* | *x(DMF)* | *p (kPa)* | *η (Pa·s)* |
|---|---|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「BLKpoint_5」 | 「298.15」 | 「0.3932」 | 「100.0」 | 「0.00054」 |
| WM_L1#1_Table#1_Row#2 | 「**BLKpoint_6**」 | 「**298.15**」 | 「**0.5029**」 | 「**100.0**」 | 「**0.00061**」 |
| WM_L1#1_Table#1_Row#3 | 「BLKpoint_7」 | 「298.15」 | 「0.6002」 | 「100.0」 | 「0.00065」 |
| WM_L1#1_Table#1_Row#4 | 「BLKpoint_8」 | 「298.15」 | 「0.6931」 | 「100.0」 | 「0.00069」 |

**Best available value near equimolar: η = 0.00061 Pa·s (0.61 mPa·s) at x(DMF) = 0.5029, 298.15 K, 100 kPa.**

---

##### Block 2 — Mass-fraction basis

**Source:** DOI 10.1016/j.jct.2014.02.019 (GLOBlit_4124, PROPblock_6)  
**Method:** Capillary tube (Ostwald–Ubbelohde)  
**Pressure:** 101.0 kPa  

This block reports composition as mass fraction of DMF. An equimolar mixture (x = 0.5) corresponds to approximately w(DMF) ≈ 0.64 (this conversion is derived from the known molar masses of DMF and acetonitrile, which are standard chemistry reference values and not sourced from this database). No exact row at w = 0.64 exists; the bracketing data at 298.15 K are:

**WM_L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *BLKpoint_id* | *T (K)* | *w(DMF)* | *p (kPa)* | *η (Pa·s)* |
|---|---|---|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「BLKpoint_9」 | 「298.15」 | 「0.50」 | 「101.0」 | 「0.0005214」 |
| WM_L1#1_Table#2_Row#2 | 「BLKpoint_13」 | 「298.15」 | 「0.75」 | 「101.0」 | 「0.0006465」 |

The equimolar value would fall between these two points but cannot be interpolated from the database.

---

##### Chemistry Insight

The viscosity of the acetonitrile + DMF mixture increases monotonically with DMF content, consistent with DMF being the more viscous pure component (η_DMF ≈ 0.00080 Pa·s vs. η_ACN ≈ 0.00034 Pa·s at 298.15 K, both from PROPblock_18). At the near-equimolar composition (x(DMF) = 0.5029), the measured viscosity of 0.00061 Pa·s lies between the pure-component values, as expected for this relatively ideal system.

**Core claims:**
- The dynamic viscosity of the acetonitrile + N,N-dimethylformamide binary mixture near equimolar composition (x(DMF) = 0.5029) at 298.15 K and 100.0 kPa is η = 0.00061 Pa·s (0.61 mPa·s), as measured by a falling/rolling sphere viscometer (DOI 10.1021/acs.jced.8b00176).
- No exact equimolar (x = 0.5000) data point exists in the available ThermoML data; x(DMF) = 0.5029 is the nearest composition.
- The mixture viscosity increases monotonically with DMF content, consistent with DMF being the more viscous pure component (η_DMF ≈ 0.00080 Pa·s vs. η_ACN ≈ 0.00034 Pa·s at 298.15 K), and the near-equimolar value of 0.00061 Pa·s lies between the pure-component values.
- A second data block (DOI 10.1016/j.jct.2014.02.019) reports viscosity on a mass-fraction basis at 101.0 kPa, but lacks a data point at the mass fraction corresponding to equimolar composition (w(DMF) ≈ 0.64), with bracketing values of 0.0005214 Pa·s at w = 0.50 and 0.0006465 Pa·s at w = 0.75.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#3 | 「GLOBlit_7481」 | 「PROPblock_18」 | 「GLOBcomp_18, GLOBcomp_15」 | 「GLOBprop_4」 | 「Dynamic viscosity measurements for acetonitrile + N,N-dimethylformamide binary mixture via falling/rolling sphere viscometer at 298.15 K and 100.0 kPa on mole-fraction basis; nearest equimolar point at x(DMF)=0.5029 gives η=0.00061 Pa·s.」 |
| WM_L1#1_Table#4 | 「GLOBlit_4124」 | 「PROPblock_6」 | 「GLOBcomp_18, GLOBcomp_15」 | 「GLOBprop_4」 | 「Dynamic viscosity measurements for acetonitrile + N,N-dimethylformamide binary mixture via capillary tube (Ostwald–Ubbelohde) at 298.15 K and 101.0 kPa on mass-fraction basis; bracketing rows at w(DMF)=0.50 and 0.75.」 |

*Not stored here: 2 verbatim data_inspections table(s); 5 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


