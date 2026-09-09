# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_022012_986027_82a6c5aa`

### History
- [query:Q1] "Find measured viscosity data for a binary mixture of methanol and water at equim" (169s, 2 iters, validation=PASS verdict=## Verdict
The primary data po)

### Query Agent Results

#### Q1
**Q1** — confidence: high · validation: PASS

**Answer:**

#### Dynamic Viscosity of Methanol + Water at Equimolar Composition, 298.15 K

##### Result

The measured dynamic viscosity of the **methanol + water** binary mixture at near-equimolar composition is:

**WM_Q#1_Table#1_(Main_Q#1_Answer):**

| *row_id* | *Temperature (K)* | *x(water)* | *Pressure (kPa)* | *Dynamic Viscosity (Pa·s)* |
|---|---|---|---|---|
| WM_Q#1_Table#1_Row#1 | 「298.15」 | 「0.5003」 | 「101.0」 | 「0.001309」 |

**η = 0.001309 Pa·s (≈ 1.309 mPa·s or 1.309 cP)**

##### Source Details

- **DOI:** 10.1016/j.jct.2007.05.004
- **Block:** PROPblock_9
- **Measurement method:** Capillary tube viscometry (CAPTUB)

##### Compound Details

**WM_Q#1_Table#2_(Main_Q#1_Answer):**

| *row_id* | *Compound* | *Formula* | *InChIKey* |
|---|---|---|---|
| WM_Q#1_Table#2_Row#1 | 「Methanol」 | 「CH₄O」 | 「OKKJLVBELUTLKV-UHFFFAOYSA-N」 |
| WM_Q#1_Table#2_Row#2 | 「Water」 | 「H₂O」 | 「XLYOFNOQVPJJNP-UHFFFAOYSA-N」 |

##### Notes

- **Composition:** No data point exists at exactly x(methanol) = 0.5000 in this dataset. The nearest available composition is **x(water) = 0.5003**, corresponding to x(methanol) ≈ 0.4997.
- **Pressure:** The reported pressure in the dataset is **101.0 kPa**, slightly below the requested 101.325 kPa. At liquid-phase conditions this small difference has negligible effect on viscosity.
- **Uncertainty:** No explicit uncertainty is reported for this data point.

##### Chemistry Context

The viscosity of the equimolar methanol–water mixture (0.001309 Pa·s) is significantly higher than that of pure methanol at the same temperature (0.000545 Pa·s at x(water) = 0). This well-known viscosity enhancement arises from extensive hydrogen-bonding network restructuring when water and methanol molecules interact. The data from this source show that viscosity continues to increase beyond equimolar composition, reaching a maximum near x(water) ≈ 0.7:

**WM_Q#1_Table#3_(Main_Q#1_Answer):**

| *row_id* | *Temperature (K)* | *x(water)* | *Pressure (kPa)* | *Dynamic Viscosity (Pa·s)* |
|---|---|---|---|---|
| WM_Q#1_Table#3_Row#1 | 「298.15」 | 「0.3985」 | 「101.0」 | 「0.00115」 |
| WM_Q#1_Table#3_Row#2 | 「298.15」 | 「0.5003」 | 「101.0」 | 「0.001309」 |
| WM_Q#1_Table#3_Row#3 | 「298.15」 | 「0.5994」 | 「101.0」 | 「0.001463」 |
| WM_Q#1_Table#3_Row#4 | 「298.15」 | 「0.6997」 | 「101.0」 | 「0.001554」 |
| WM_Q#1_Table#3_Row#5 | 「298.15」 | 「0.7986」 | 「101.0」 | 「0.001542」 |
| WM_Q#1_Table#3_Row#6 | 「298.15」 | 「0.8999」 | 「101.0」 | 「0.001317」 |

The viscosity maximum at x(water) ≈ 0.7 (η = 0.001554 Pa·s) reflects the composition where the mixed hydrogen-bonding network is most structured, creating the greatest resistance to flow. Beyond this point, the system transitions toward the pure-water hydrogen-bonding structure and viscosity decreases.

**Core claims:**
- The dynamic viscosity of the methanol + water binary mixture at x(water) = 0.5003, 298.15 K, and 101.0 kPa is 0.001309 Pa·s, as measured by capillary tube viscometry (DOI: 10.1016/j.jct.2007.05.004).
- No data point exists at exactly equimolar composition; the nearest available is x(water) = 0.5003 (x(methanol) ≈ 0.4997), and the reported pressure of 101.0 kPa is slightly below the standard 101.325 kPa, with negligible effect on liquid-phase viscosity.
- The equimolar mixture viscosity (0.001309 Pa·s) is significantly higher than that of pure methanol at the same temperature (0.000545 Pa·s), consistent with hydrogen-bonding network restructuring in methanol–water mixtures.
- The data show a viscosity maximum near x(water) ≈ 0.7 (η = 0.001554 Pa·s at 298.15 K), beyond which viscosity decreases toward pure-water values.
- No explicit uncertainty is reported for the viscosity measurement.

**Sources:**

**WM_Q#1_Table#4_(Main_Q#1_Sources):**

| *row_id* | *lit_num_id* | *block* | *doi* | *BLKsubsys_id* | *description* |
|---|---|---|---|---|---|
| WM_Q#1_Table#4_Row#1 | 「GLOBlit_2825」 | 「PROPblock_9」 | 「10.1016/j.jct.2007.05.004」 | 「—」 | 「This block provides dynamic viscosity (Pa·s) of the methanol + water binary mixture measured by capillary tube viscometry at 101.0 kPa, covering temperatures 293.15–303.15 K and mole fractions 0.0–1.0. It directly supplies the reported value of 0.001309 Pa·s at 298.15 K and x(water) = 0.5003.」 |

*Not stored here: 2 verbatim data_inspections table(s); 4 id_catalog_snapshot row(s) (catalog is merged separately). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.

