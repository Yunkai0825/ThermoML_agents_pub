# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_042035_237077_c40f369c`

### History
- [parallel:3 tasks]
-   [query:MeOH_EtOH_visc] "Find viscosity data for the binary mixture of methanol + ethanol at or near 30°C" (113s, 2 iters, validation=PASS verdict=## Verdict
The answer appears )
-   [query:ACN_DMF_visc] "Find viscosity data for the binary mixture of acetonitrile + N,N-dimethylformami" (173s, 2 iters, validation=PASS verdict=## Verdict
The two DOIs and bl)
-   [query:Water_EG_visc] "Find viscosity data for the binary mixture of water + ethylene glycol at or near" (212s, 2 iters, validation=PASS verdict=## Verdict
The answer identifi)
- [parallel:auto-compacted] 3 per-task reports (agentic, targets ALL, philosophy elicited)
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → ERROR: where filter error: unknown column alias 'T'
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → ERROR: nearest must be {"column": alias, "value": number, "k": 1..8}
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → ERROR: `where` must be a non-empty filter string when given
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK

### Query Agent Results

#### MeOH_EtOH_visc
**MeOH_EtOH_visc** — confidence: high · validation: PASS

**Answer:**

#### Dynamic Viscosity of Methanol + Ethanol Binary Mixture at 303.15 K

##### Source

- **DOI:** 10.1021/je800633a
- **Block:** PROPblock_16
- **Measurement method:** Capillary tube (Ostwald–Ubbelohde)

##### System Details

**WM_Q#3_Table#1_(Main_Q#3_Answer):**

| *row_id* | *Parameter* | *Value* |
|---|---|---|
| WM_Q#3_Table#1_Row#1 | 「**Compounds**」 | 「Methanol (CH₄O) + Ethanol (C₂H₆O)」 |
| WM_Q#3_Table#1_Row#2 | 「**System type**」 | 「Binary liquid mixture」 |
| WM_Q#3_Table#1_Row#3 | 「**Temperature**」 | 「303.15 K (≈ 30 °C), fixed」 |
| WM_Q#3_Table#1_Row#4 | 「**Pressure**」 | 「81.5 kPa, fixed」 |

##### Viscosity vs. Mole Fraction of Methanol

Twelve data points spanning the composition range:

**WM_Q#3_Table#2_(Main_Q#3_Answer):**

| *row_id* | *x(methanol)* | *η (Pa·s)* |
|---|---|---|
| WM_Q#3_Table#2_Row#1 | 「0.0417」 | 「0.000968」 |
| WM_Q#3_Table#2_Row#2 | 「0.1476」 | 「0.000906」 |
| WM_Q#3_Table#2_Row#3 | 「0.2214」 | 「0.000865」 |
| WM_Q#3_Table#2_Row#4 | 「0.2952」 | 「0.000828」 |
| WM_Q#3_Table#2_Row#5 | 「0.3644」 | 「0.000793」 |
| WM_Q#3_Table#2_Row#6 | 「0.4488」 | 「0.000753」 |
| WM_Q#3_Table#2_Row#7 | 「0.529」 | 「0.000717」 |
| WM_Q#3_Table#2_Row#8 | 「0.5995」 | 「0.000685」 |
| WM_Q#3_Table#2_Row#9 | 「0.6859」 | 「0.000648」 |
| WM_Q#3_Table#2_Row#10 | 「0.7442」 | 「0.000624」 |
| WM_Q#3_Table#2_Row#11 | 「0.832」 | 「0.000588」 |
| WM_Q#3_Table#2_Row#12 | 「0.9166」 | 「0.000556」 |

##### Chemical Insight

The dynamic viscosity decreases monotonically from 0.000968 Pa·s at the ethanol-rich end (x(methanol) = 0.0417) to 0.000556 Pa·s at the methanol-rich end (x(methanol) = 0.9166). The decrease is nearly linear with composition, indicating relatively ideal mixing behavior with minimal excess viscosity effects in this system at 303.15 K.

This behavior is consistent with the molecular similarity of methanol and ethanol — both are small, linear aliphatic alcohols capable of hydrogen bonding. Methanol, being smaller (one carbon vs. two), has weaker van der Waals interactions and a less extensive hydrogen-bonding network, leading to its lower pure-component viscosity. The near-ideal mixing arises because the two components are structurally and chemically similar, so replacing ethanol molecules with methanol molecules in the mixture smoothly reduces the average intermolecular interaction strength without introducing significant structural disruption or preferential association.

**Core claims:**
- For the methanol + ethanol binary liquid mixture at 303.15 K and 81.5 kPa (DOI 10.1021/je800633a, PROPblock_16), the dynamic viscosity decreases monotonically from 0.000968 Pa·s at x(methanol) = 0.0417 to 0.000556 Pa·s at x(methanol) = 0.9166, as measured by capillary tube (Ostwald–Ubbelohde) across twelve compositions.
- The decrease in viscosity with increasing methanol mole fraction is nearly linear, indicating relatively ideal mixing behavior with minimal excess viscosity effects, consistent with the structural and chemical similarity of the two small aliphatic alcohols.

**Sources:**

**WM_Q#3_Table#3_(Main_Q#3_Sources):**

| *row_id* | *lit_num_id* | *block* | *doi* | *BLKsubsys_id* | *description* |
|---|---|---|---|---|---|
| WM_Q#3_Table#3_Row#1 | 「GLOBlit_11337」 | 「PROPblock_16」 | 「10.1021/je800633a」 | 「—」 | 「This block provides the 12 dynamic viscosity data points for the methanol + ethanol binary mixture at 303.15 K and 81.5 kPa, spanning mole fractions 0.0417–0.9166 with viscosities 0.000556–0.000968 Pa·s, which directly constitute the answer's tabulated data and analysis.」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### ACN_DMF_visc
**ACN_DMF_visc** — confidence: high · validation: PASS

**Answer:**

#### Dynamic Viscosity of Acetonitrile + N,N-Dimethylformamide (DMF) at 303.15 K

Two independent ThermoML data sources provide dynamic viscosity (η) measurements for the binary system **acetonitrile (CH₃CN)** + **N,N-dimethylformamide (DMF, C₃H₇NO)** at 303.15 K across the full composition range.

---

##### Source 1 — Mass-fraction basis

**DOI:** 10.1016/j.jct.2014.02.019 · **Block:** PROPblock_6  
**Compounds:** Acetonitrile (GLOBcomp_15) + Dimethylformamide (GLOBcomp_18)  
**Method:** Capillary tube (Ostwald/Ubbelohde) viscometry  
**Conditions:** T = 303.15 K, P = 101.0 kPa  
**Full block range:** 298.15–313.15 K, 20 total data points

**WM_Q#1_Table#1_(Main_Q#1_Answer):**

| *row_id* | *w(DMF)* | *η (Pa·s)* |
|---|---|---|
| WM_Q#1_Table#1_Row#1 | 「0」 | 「0.0003269」 |
| WM_Q#1_Table#1_Row#2 | 「0.25」 | 「0.0003598」 |
| WM_Q#1_Table#1_Row#3 | 「0.50」 | 「0.00046」 |
| WM_Q#1_Table#1_Row#4 | 「0.75」 | 「0.0006145」 |
| WM_Q#1_Table#1_Row#5 | 「1.00」 | 「0.000755」 |

---

##### Source 2 — Mole-fraction basis (recommended for your needs)

**DOI:** 10.1021/acs.jced.8b00176 · **Block:** PROPblock_18  
**Compounds:** Acetonitrile (GLOBcomp_15) + Dimethylformamide (GLOBcomp_18)  
**Method:** Falling/rolling sphere viscometry  
**Conditions:** T = 303.15 K, P = 100.0 kPa  
**Full block range:** 298.15–323.15 K, 66 total data points

**WM_Q#1_Table#2_(Main_Q#1_Answer):**

| *row_id* | *x(DMF)* | *η (Pa·s)* |
|---|---|---|
| WM_Q#1_Table#2_Row#1 | 「0」 | 「0.00032」 |
| WM_Q#1_Table#2_Row#2 | 「0.0989」 | 「0.00039」 |
| WM_Q#1_Table#2_Row#3 | 「0.1916」 | 「0.00042」 |
| WM_Q#1_Table#2_Row#4 | 「0.2925」 | 「0.00046」 |
| WM_Q#1_Table#2_Row#5 | 「0.3932」 | 「0.00051」 |
| WM_Q#1_Table#2_Row#6 | 「0.5029」 | 「0.00057」 |
| WM_Q#1_Table#2_Row#7 | 「0.6002」 | 「0.00061」 |
| WM_Q#1_Table#2_Row#8 | 「0.6931」 | 「0.00065」 |
| WM_Q#1_Table#2_Row#9 | 「0.7926」 | 「0.00070」 |
| WM_Q#1_Table#2_Row#10 | 「0.8996」 | 「0.00075」 |
| WM_Q#1_Table#2_Row#11 | 「1.0000」 | 「0.00077」 |

---

##### Chemical Insight

Both datasets show a **monotonic, slightly concave increase** in dynamic viscosity with increasing DMF content at 303.15 K. Pure DMF is roughly 2.4× more viscous than pure acetonitrile under these conditions (≈ 0.00077 vs. 0.00032 Pa·s). This trend reflects the stronger intermolecular interactions in DMF — it is a larger molecule with a higher dipole moment (~3.86 D vs. ~3.92 D for acetonitrile, but with a much larger molecular volume and stronger dipole–dipole/dispersion forces) and a pronounced hydrogen-bond-accepting capability via its carbonyl oxygen.

The two independent sources agree well at the pure-component endpoints (within ~2–3%), with minor differences attributable to different measurement techniques (capillary vs. falling-sphere viscometry) and a slight pressure difference (101.0 vs. 100.0 kPa). Source 2 (DOI 10.1021/acs.jced.8b00176) is particularly useful for your needs as it directly reports viscosity on a **mole-fraction basis** with 11 composition points spanning the full range, and covers a broader temperature window (298.15–323.15 K).

**Core claims:**
- Two independent ThermoML sources provide dynamic viscosity measurements for the acetonitrile + N,N-dimethylformamide binary system at 303.15 K across the full composition range.
- Both datasets show a monotonic, slightly concave increase in dynamic viscosity with increasing DMF content at 303.15 K, from approximately 0.00032 Pa·s (pure acetonitrile) to approximately 0.00077 Pa·s (pure DMF).
- Source 1 (DOI 10.1016/j.jct.2014.02.019) reports viscosity on a mass-fraction basis at 303.15 K and 101.0 kPa using capillary tube viscometry, with 5 composition points.
- Source 2 (DOI 10.1021/acs.jced.8b00176) reports viscosity on a mole-fraction basis at 303.15 K and 100.0 kPa using falling/rolling sphere viscometry, with 11 composition points spanning the full range and a broader temperature window of 298.15–323.15 K.
- The two independent sources agree at the pure-component endpoints within ~2–3%, with minor differences attributed to different measurement techniques and a slight pressure difference (101.0 vs. 100.0 kPa).
- The higher viscosity of pure DMF relative to pure acetonitrile is attributed to stronger intermolecular interactions in DMF, including its larger molecular volume, stronger dipole–dipole/dispersion forces, and hydrogen-bond-accepting capability via its carbonyl oxygen.

**Sources:**

**WM_Q#1_Table#3_(Main_Q#1_Sources):**

| *row_id* | *lit_num_id* | *block* | *doi* | *BLKsubsys_id* | *description* |
|---|---|---|---|---|---|
| WM_Q#1_Table#3_Row#1 | 「GLOBlit_4124」 | 「PROPblock_6」 | 「10.1016/j.jct.2014.02.019」 | 「—」 | 「Provides dynamic viscosity of the acetonitrile + DMF binary system on a mass-fraction basis at 303.15 K (within its 298.15–313.15 K range), measured by capillary tube viscometry at 101.0 kPa. The answer's Source 1 table values fall within the card's viscosity range of 0.000293–0.000799 Pa·s.」 |
| WM_Q#1_Table#3_Row#2 | 「GLOBlit_7481」 | 「PROPblock_18」 | 「10.1021/acs.jced.8b00176」 | 「—」 | 「Provides dynamic viscosity of the acetonitrile + DMF binary system on a mole-fraction basis at 303.15 K (within its 298.15–323.15 K range), measured by falling-sphere viscometry at 100.0 kPa with 66 data points spanning the full composition range. The answer's Source 2 table values fall within the card's viscosity range of 0.00028–0.00081 Pa·s.」 |

*Not stored here: 2 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### Water_EG_visc
**Water_EG_visc** — confidence: high · validation: PASS

**Answer:**

#### Dynamic Viscosity of Water + Ethylene Glycol (1,2-Ethanediol) at 303.15 K

Two independent ThermoML datasets provide dynamic viscosity data for the binary mixture of **water** and **1,2-ethanediol (ethylene glycol)** at exactly **303.15 K (30 °C)**, covering the full composition range.

---

##### Dataset 1 — DOI: 10.1016/j.jct.2018.02.022 · Block PROPblock_24

**Method:** Concentric cylinders viscometry · **Pressure:** 92.3 kPa · **Composition variable:** mole fraction of 1,2-ethanediol

**WM_Q#2_Table#1_(Main_Q#2_Answer):**

| *row_id* | *x(1,2-ethanediol)* | *Viscosity (Pa·s)* |
|---|---|---|
| WM_Q#2_Table#1_Row#1 | 「0」 | 「0.0008385」 |
| WM_Q#2_Table#1_Row#2 | 「0.0494」 | 「0.0011644」 |
| WM_Q#2_Table#1_Row#3 | 「0.0986」 | 「0.001555」 |
| WM_Q#2_Table#1_Row#4 | 「0.1483」 | 「0.0019899」 |
| WM_Q#2_Table#1_Row#5 | 「0.2072」 | 「0.0025643」 |
| WM_Q#2_Table#1_Row#6 | 「0.2466」 | 「0.0029649」 |
| WM_Q#2_Table#1_Row#7 | 「0.3399」 | 「0.0040293」 |
| WM_Q#2_Table#1_Row#8 | 「0.3921」 | 「0.0046704」 |
| WM_Q#2_Table#1_Row#9 | 「0.4446」 | 「0.0053492」 |
| WM_Q#2_Table#1_Row#10 | 「0.5485」 | 「0.0067709」 |
| WM_Q#2_Table#1_Row#11 | 「0.6451」 | 「0.0081729」 |
| WM_Q#2_Table#1_Row#12 | 「0.7012」 | 「0.0090846」 |
| WM_Q#2_Table#1_Row#13 | 「0.7435」 | 「0.0098077」 |
| WM_Q#2_Table#1_Row#14 | 「0.7907」 | 「0.010548」 |
| WM_Q#2_Table#1_Row#15 | 「0.8505」 | 「0.011535」 |
| WM_Q#2_Table#1_Row#16 | 「1」 | 「0.013867」 |

*(Shape-preserving subset of 21 matched rows at 303.15 K; viscosity ranges from 0.0008385 to 0.013867 Pa·s.)*

---

##### Dataset 2 — DOI: 10.1021/acs.jced.6b00526 · Block PROPblock_18

**Method:** Falling sphere viscometry · **Pressure:** 100.0 kPa · **Composition variable:** mole fraction of water

**WM_Q#2_Table#2_(Main_Q#2_Answer):**

| *row_id* | *x(water)* | *Viscosity (Pa·s)* |
|---|---|---|
| WM_Q#2_Table#2_Row#1 | 「0」 | 「0.01423」 |
| WM_Q#2_Table#2_Row#2 | 「0.1105」 | 「0.01186」 |
| WM_Q#2_Table#2_Row#3 | 「0.2014」 | 「0.01014」 |
| WM_Q#2_Table#2_Row#4 | 「0.3002」 | 「0.00845」 |
| WM_Q#2_Table#2_Row#5 | 「0.4011」 | 「0.006968」 |
| WM_Q#2_Table#2_Row#6 | 「0.4969」 | 「0.005653」 |
| WM_Q#2_Table#2_Row#7 | 「0.6022」 | 「0.004396」 |
| WM_Q#2_Table#2_Row#8 | 「0.6995」 | 「0.003345」 |
| WM_Q#2_Table#2_Row#9 | 「0.7994」 | 「0.002328」 |
| WM_Q#2_Table#2_Row#10 | 「0.8997」 | 「0.001446」 |
| WM_Q#2_Table#2_Row#11 | 「1」 | 「0.000755」 |

*(Complete isotherm — all 11 data points at 303.15 K.)*

---

##### Compounds

**WM_Q#2_Table#3_(Main_Q#2_Answer):**

| *row_id* | *Component* | *Formula* | *InChIKey* |
|---|---|---|---|
| WM_Q#2_Table#3_Row#1 | 「Water」 | 「H₂O」 | 「XLYOFNOQVPJJNP-UHFFFAOYSA-N」 |
| WM_Q#2_Table#3_Row#2 | 「1,2-Ethanediol (ethylene glycol)」 | 「C₂H₆O₂」 | 「LYCAIKOWRPUZTN-UHFFFAOYSA-N」 |

---

##### Chemistry Insight

Both datasets show a **monotonic increase** in viscosity with increasing ethylene glycol content. At 303.15 K:

- **Pure water:** 0.0008385 Pa·s (Dataset 1) / 0.000755 Pa·s (Dataset 2)
- **Pure ethylene glycol:** 0.013867 Pa·s (Dataset 1) / 0.01423 Pa·s (Dataset 2)

Pure ethylene glycol is roughly **17–19 times more viscous** than pure water at this temperature. This large difference arises because ethylene glycol has two hydroxyl groups that form an extensive intermolecular hydrogen-bonding network, creating much stronger cohesive interactions than water alone.

The viscosity–composition curve is **concave upward** (positive deviation from a simple linear mixing rule), which is characteristic of strongly associating aqueous–diol mixtures. The two datasets, measured by different techniques (concentric cylinders vs. falling sphere) and at slightly different pressures (92.3 vs. 100.0 kPa), are in good mutual agreement, lending confidence to the reported values.

Three additional ThermoML literature sources were also identified for this system and could provide further comparison data if needed.

**Core claims:**
- Two independent ThermoML datasets provide dynamic viscosity data for the water + 1,2-ethanediol (ethylene glycol) binary mixture at exactly 303.15 K, covering the full composition range.
- Dataset 1 (DOI: 10.1016/j.jct.2018.02.022, concentric cylinders viscometry, 92.3 kPa) reports viscosity ranging from 0.0008385 Pa·s (pure water) to 0.013867 Pa·s (pure ethylene glycol) as a function of 1,2-ethanediol mole fraction.
- Dataset 2 (DOI: 10.1021/acs.jced.6b00526, falling sphere viscometry, 100.0 kPa) reports viscosity ranging from 0.000755 Pa·s (pure water) to 0.01423 Pa·s (pure ethylene glycol) as a function of water mole fraction.
- Both datasets show a monotonic increase in viscosity with increasing ethylene glycol content at 303.15 K, with the viscosity–composition curve described as concave upward (positive deviation from linear mixing), characteristic of strongly associating aqueous–diol mixtures.
- The two datasets, measured by different techniques and at slightly different pressures (92.3 vs. 100.0 kPa), are reported to be in good mutual agreement.

**Sources:**

**WM_Q#2_Table#4_(Main_Q#2_Sources):**

| *row_id* | *lit_num_id* | *block* | *doi* | *BLKsubsys_id* | *description* |
|---|---|---|---|---|---|
| WM_Q#2_Table#4_Row#1 | 「GLOBlit_5201」 | 「PROPblock_24」 | 「10.1016/j.jct.2018.02.022」 | 「—」 | 「Provides dynamic viscosity of the water + 1,2-ethanediol binary system measured by concentric cylinders viscometry at 92.3 kPa. The block covers 293.15–308.15 K and mole fractions 0–1, so the 303.15 K isotherm extracted in the answer (viscosity 0.0008385–0.013867 Pa·s) falls squarely within its ranges.」 |
| WM_Q#2_Table#4_Row#2 | 「GLOBlit_6951」 | 「PROPblock_18」 | 「10.1021/acs.jced.6b00526」 | 「—」 | 「Provides dynamic viscosity of the water + 1,2-ethanediol binary system measured by falling sphere viscometry at 100.0 kPa. The temperature range extends to 303.15 K and mole fraction spans 0–1, supplying the 11-point isotherm (0.000755–0.01423 Pa·s) reported in the answer.」 |

*Not stored here: 2 verbatim data_inspections table(s); 3 id_catalog_snapshot row(s) (catalog is merged separately). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


### Parallel Compaction Reports

#### Compaction 1
**Philosophy (agentic, targets ALL, philosophy elicited):** Retain for each binary system: DOIs, compound names, temperature(s), and the full set of viscosity vs. mole-fraction data points (numerical values of x and η in mPa·s). Keep any noted deviations from ideal mixing or viscosity extrema. Drop raw XML snippets, redundant metadata, block-level structural details, and any commentary not directly conveying data values or source identifiers.

##### [MeOH_EtOH_visc]
**Summary:** Dynamic viscosity data for methanol + ethanol at 303.15 K found in DOI **10.1021/je800633a**, block **PROPblock_16** (GLOBlit_11337). Twelve points span x(methanol) = 0.0417–0.9166; viscosity decreases monotonically (nearly linearly), indicating near-ideal mixing.

**Source:** DOI `10.1021/je800633a` | `GLOBlit_11337` | `PROPblock_16` | T = 303.15 K | P = 81.5 kPa | Capillary tube (Ostwald–Ubbelohde)

| x(methanol) | η (Pa·s) |
|:-----------:|:---------:|
| 0.0417 | 0.000968 |
| 0.1476 | 0.000906 |
| 0.2214 | 0.000865 |
| 0.2952 | 0.000828 |
| 0.3644 | 0.000793 |
| 0.4488 | 0.000753 |
| 0.529  | 0.000717 |
| 0.5995 | 0.000685 |
| 0.6859 | 0.000648 |
| 0.7442 | 0.000624 |
| 0.832  | 0.000588 |
| 0.9166 | 0.000556 |

**Notes:** Viscosity decreases monotonically from the ethanol

##### [ACN_DMF_visc]
Two ThermoML sources provide dynamic viscosity for **acetonitrile (GLOBcomp_15) + N,N-dimethylformamide (GLOBcomp_18)** at 303.15 K across the full composition range; viscosity increases monotonically from ~0.32 mPa·s (pure ACN) to ~0.77 mPa·s (pure DMF).

### Source 1 — Mass-fraction basis
**DOI:** 10.1016/j.jct.2014.02.019 | **GLOBlit_4124** | **PROPblock_6** | P = 101.0 kPa

| w(DMF) | η (Pa·s) |
|--------|-----------|
| 0 | 0.0003269 |
| 0.25 | 0.0003598 |
| 0.50 | 0.00046 |
| 0.75 | 0.0006145 |
| 1.00 | 0.000755 |

### Source 2 — Mole-fraction basis (recommended)
**DOI:** 10.1021/acs.jced.8b00176 | **GLOBlit_7481** | **PROPblock_18** | P = 100.0 kPa

| x(DMF) | η (Pa·s) |
|--------|-----------|
|

##### [Water_EG_visc]
Two independent ThermoML datasets provide dynamic viscosity of water (GLOBcomp_1) + 1,2-ethanediol (GLOBcomp_24) at exactly 303.15 K, covering the full composition range. Viscosity increases monotonically with ethylene glycol content.

**Dataset 1 — DOI: 10.1016/j.jct.2018.02.022 · GLOBlit_5201 · PROPblock_24 · 92.3 kPa**

| x(EG) | η (Pa·s) |
|--------|-----------|
| 0 | 0.0008385 |
| 0.0494 | 0.0011644 |
| 0.0986 | 0.001555 |
| 0.1483 | 0.0019899 |
| 0.2072 | 0.0025643 |
| 0.2466 | 0.0
