# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_022024_992572_65a033ff`

### History
- [query:Q1] "Find experimental viscosity values for an equimolar (x=0.5) binary mixture of ac" (207s, 2 iters, validation=PASS verdict=## Verdict
The answer identifi)
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK

### Query Agent Results

#### Q1
**Q1** — confidence: high · validation: PASS

**Answer:**

#### Dynamic Viscosity of Acetonitrile + N,N-Dimethylformamide at Equimolar Composition and 298.15 K

Two independent ThermoML data blocks report experimental dynamic viscosity for the binary system **acetonitrile + N,N-dimethylformamide (DMF)** near equimolar composition at 298.15 K (25 °C):

---

##### Data Source 1 — Mole-fraction basis (closest match to x = 0.5)

**DOI:** 10.1021/acs.jced.8b00176 (GLOBlit_7481)  
**Block:** PROPblock_18  
**Method:** Falling/rolling sphere viscometer  
**Pressure:** 100.0 kPa  

There is **no exact data point at x(DMF) = 0.5000**; the nearest composition is **x(DMF) = 0.5029**. The data at 298.15 K surrounding the equimolar region are:

**WM_Q#1_Table#1_(Main_Q#1_Answer):**

| *row_id* | *T (K)* | *x(DMF)* | *p (kPa)* | *η (Pa·s)* | *η (mPa·s)* |
|---|---|---|---|---|---|
| WM_Q#1_Table#1_Row#1 | 「298.15」 | 「0.3932」 | 「100.0」 | 「0.00054」 | 「0.54」 |
| WM_Q#1_Table#1_Row#2 | 「**298.15**」 | 「**0.5029**」 | 「**100.0**」 | 「**0.00061**」 | 「**0.61**」 |
| WM_Q#1_Table#1_Row#3 | 「298.15」 | 「0.6002」 | 「100.0」 | 「0.00065」 | 「0.65」 |
| WM_Q#1_Table#1_Row#4 | 「298.15」 | 「0.6931」 | 「100.0」 | 「0.00069」 | 「0.69」 |

**Best available near-equimolar value: η = 0.00061 Pa·s (0.61 mPa·s) at x(DMF) = 0.5029, 298.15 K, 100.0 kPa.**

---

##### Data Source 2 — Mass-fraction basis

**DOI:** 10.1016/j.jct.2014.02.019 (GLOBlit_4124)  
**Block:** PROPblock_6  
**Method:** Capillary tube (Ostwald–Ubbelohde)  
**Pressure:** 101.0 kPa  

This block reports composition as mass fraction of DMF. An equimolar mixture (x = 0.5) corresponds to approximately w(DMF) ≈ 0.64 based on the molar masses of DMF (73.09 g/mol) and acetonitrile (41.05 g/mol). No exact row at w ≈ 0.64 exists; the bracketing data at 298.15 K are:

**WM_Q#1_Table#2_(Main_Q#1_Answer):**

| *row_id* | *T (K)* | *w(DMF)* | *p (kPa)* | *η (Pa·s)* | *η (mPa·s)* |
|---|---|---|---|---|---|
| WM_Q#1_Table#2_Row#1 | 「298.15」 | 「0.25」 | 「101.0」 | 「0.0003959」 | 「0.396」 |
| WM_Q#1_Table#2_Row#2 | 「298.15」 | 「0.50」 | 「101.0」 | 「0.0005214」 | 「0.521」 |
| WM_Q#1_Table#2_Row#3 | 「298.15」 | 「0.75」 | 「101.0」 | 「0.0006465」 | 「0.647」 |
| WM_Q#1_Table#2_Row#4 | 「298.15」 | 「1.00」 | 「101.0」 | 「0.0007986」 | 「0.799」 |

The equimolar value would fall between the w = 0.50 and w = 0.75 rows, but no exact match is available in this block.

---

##### Summary and Chemistry Insight

**WM_Q#1_Table#3_(Main_Q#1_Answer):**

| *row_id* | *Source* | *Composition basis* | *Nearest equimolar point* | *η (Pa·s)* | *η (mPa·s)* |
|---|---|---|---|---|---|
| WM_Q#1_Table#3_Row#1 | 「10.1021/acs.jced.8b00176 (GLOBlit_7481, PROPblock_18)」 | 「Mole fraction」 | 「x(DMF) = 0.5029」 | 「0.00061」 | 「0.61」 |
| WM_Q#1_Table#3_Row#2 | 「10.1016/j.jct.2014.02.019 (GLOBlit_4124, PROPblock_6)」 | 「Mass fraction」 | 「Bracketed between w = 0.50 and 0.75」 | 「0.0005214–0.0006465」 | 「0.521–0.647」 |

The viscosity of this mixture increases monotonically with DMF content, which is expected since pure DMF is substantially more viscous than pure acetonitrile at 298.15 K (η_DMF ≈ 0.00080 Pa·s vs. η_ACN ≈ 0.00034 Pa·s, from PROPblock_18). The near-equimolar value of 0.00061 Pa·s falls between the two pure-component viscosities, consistent with a relatively ideal mixing behavior — the acetonitrile–DMF system exhibits only weak intermolecular interactions beyond simple dipole–dipole forces, so no pronounced viscosity maximum or minimum (as seen in strongly associating systems) is observed.

**Core claims:**
- At 298.15 K and 100.0 kPa, the dynamic viscosity of the acetonitrile + N,N-dimethylformamide binary mixture near equimolar composition (x(DMF) = 0.5029) is 0.00061 Pa·s (0.61 mPa·s), as reported in DOI 10.1021/acs.jced.8b00176.
- A second independent source (DOI 10.1016/j.jct.2014.02.019) brackets the equimolar viscosity at 298.15 K between 0.0005214 Pa·s (w(DMF) = 0.50) and 0.0006465 Pa·s (w(DMF) = 0.75), consistent with the first source.
- The viscosity of the acetonitrile + DMF mixture increases monotonically with DMF content at 298.15 K, with the near-equimolar value falling between the pure-component viscosities (η_ACN ≈ 0.00034 Pa·s, η_DMF ≈ 0.00080 Pa·s), consistent with relatively ideal mixing behavior and the absence of a pronounced viscosity extremum.

**Sources:**

**WM_Q#1_Table#4_(Main_Q#1_Sources):**

| *row_id* | *lit_num_id* | *block* | *doi* | *BLKsubsys_id* | *description* |
|---|---|---|---|---|---|
| WM_Q#1_Table#4_Row#1 | 「GLOBlit_7481」 | 「PROPblock_18」 | 「10.1021/acs.jced.8b00176」 | 「—」 | 「This block provides dynamic viscosity of the acetonitrile + DMF binary system on a mole-fraction basis at 298.15 K and 100.0 kPa. It contains the nearest equimolar data point at x(DMF) = 0.5029 with η = 0.00061 Pa·s, which is the primary value reported in the answer.」 |
| WM_Q#1_Table#4_Row#2 | 「GLOBlit_4124」 | 「PROPblock_6」 | 「10.1016/j.jct.2014.02.019」 | 「—」 | 「This block provides dynamic viscosity of the acetonitrile + DMF binary system on a mass-fraction basis at 298.15 K and 101.0 kPa. It supplies bracketing values (w = 0.50 and w = 0.75) around the equimolar composition, serving as independent corroboration of the viscosity range reported in the answer.」 |

*Not stored here: 2 verbatim data_inspections table(s); 5 id_catalog_snapshot row(s) (catalog is merged separately). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.

