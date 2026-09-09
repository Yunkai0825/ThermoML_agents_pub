# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_045540_791203_81a722f8`

### History
- [query:Q1] "Find viscosity data for isopropanol (2-propanol) mixed with water at room temper" (144s, 2 iters, validation=PASS verdict=## Verdict
The answer identifi)
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK

### Query Agent Results

#### Q1
**Q1** — confidence: high · validation: PASS

**Answer:**

#### Viscosity Data for Isopropanol (2-Propanol) + Water Binary Mixtures at Room Temperature

##### Source

**DOI:** 10.1016/j.jct.2019.105880  
**Data block:** PROPblock_12  
**Property:** Dynamic viscosity (Pa·s), measured by falling/rolling sphere viscometry, liquid phase, at 100 kPa.  
**System:** Binary mixture of propan-2-ol (2-propanol / isopropanol) + water.

**Composition range covered:** Mass fraction of propan-2-ol from 0.1 to 0.3  
**Full block temperature range:** 288.15–303.15 K (12 data points total)

---

##### Data Points in the 293–298 K Window

**WM_Q#1_Table#1_(Main_Q#1_Answer):**

| *row_id* | *T (K)* | *w (propan-2-ol)* | *Dynamic Viscosity (Pa·s)* |
|---|---|---|---|
| WM_Q#1_Table#1_Row#1 | 「293.15」 | 「0.1」 | 「0.001633」 |
| WM_Q#1_Table#1_Row#2 | 「293.15」 | 「0.2」 | 「0.002485」 |
| WM_Q#1_Table#1_Row#3 | 「293.15」 | 「0.3」 | 「0.003172」 |
| WM_Q#1_Table#1_Row#4 | 「298.15」 | 「0.1」 | 「0.001395」 |
| WM_Q#1_Table#1_Row#5 | 「298.15」 | 「0.2」 | 「0.002045」 |
| WM_Q#1_Table#1_Row#6 | 「298.15」 | 「0.3」 | 「0.002555」 |

All measurements were made at a pressure of 100.0 kPa in the liquid phase.

---

##### Key Observations

1. **Viscosity increases with isopropanol content** in the 0.1–0.3 mass-fraction range at both temperatures. For example, at 293.15 K the viscosity nearly doubles from 0.001633 Pa·s (w = 0.1) to 0.003172 Pa·s (w = 0.3). This trend is consistent with the well-known viscosity maximum of the isopropanol–water system, which occurs at higher alcohol concentrations (typically around 0.6–0.7 mass fraction). In this composition range, the extensive hydrogen-bonding network between water and isopropanol molecules progressively increases internal friction.

2. **Viscosity decreases with increasing temperature**, as expected from the Arrhenius-type temperature dependence of liquid viscosity. At w = 0.3, the viscosity drops from 0.003172 Pa·s at 293.15 K to 0.002555 Pa·s at 298.15 K — a reduction of about 19% for just a 5 K increase.

3. **Full data block** extends from 288.15 K to 303.15 K, with viscosities spanning 0.001208–0.004014 Pa·s across all compositions and temperatures.

4. **No kinematic viscosity data** were found in the ThermoML database for this binary system in the requested temperature range. Only dynamic viscosity data are available from this source.

**Core claims:**
- Dynamic viscosity data for the binary mixture of propan-2-ol (isopropanol) + water were found in ThermoML (DOI: 10.1016/j.jct.2019.05880, PROPblock_12), covering mass fractions of propan-2-ol from 0.1 to 0.3 at 100 kPa, with six data points falling within the 293–298 K window.
- At 293.15 K and 100 kPa, the dynamic viscosity increases from 0.001633 Pa·s at w = 0.1 to 0.003172 Pa·s at w = 0.3; at 298.15 K it increases from 0.001395 Pa·s at w = 0.1 to 0.002555 Pa·s at w = 0.3.
- Viscosity decreases with increasing temperature: at w = 0.3, it drops from 0.003172 Pa·s at 293.15 K to 0.002555 Pa·s at 298.15 K.
- No kinematic viscosity data were found in the ThermoML database for this binary system in the requested temperature range; only dynamic viscosity data are available from this source.

**Sources:**

**WM_Q#1_Table#2_(Main_Q#1_Sources):**

| *row_id* | *lit_num_id* | *block* | *doi* | *BLKsubsys_id* | *description* |
|---|---|---|---|---|---|
| WM_Q#1_Table#2_Row#1 | 「GLOBlit_5585」 | 「PROPblock_12」 | 「10.1016/j.jct.2019.105880」 | 「—」 | 「This block provides dynamic viscosity data for the binary system propan-2-ol + water measured by falling/rolling sphere viscometry at 100 kPa. The temperature range 288.15–303.15 K covers the requested 293–298 K window, and the mass fraction range 0.1–0.3 with 12 data points directly supports the six viscosity values reported in the answer.」 |

*Not stored here: 1 verbatim data_inspections table(s); 3 id_catalog_snapshot row(s) (catalog is merged separately). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.

