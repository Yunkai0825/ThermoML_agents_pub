# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260815_190212_574300_1e8b238b`

### History
- [menu:browse] {'text': 'I need to explore the available tools in the subme
- [menu:run] search_id_alignment → OK
- [menu:run] search_id_alignment → OK
- [query:Q1] "Find experimental density (mass density) data for the binary mixture of ethanol " (180s, 2 iters, validation=PASS verdict=## Verdict
The answer is scien)

### Query Agent Results

#### Q1
**Q1** — confidence: high · validation: PASS

**Answer:**

#### Experimental Mass Density of Ethanol + Water at 298.15 K, x_ethanol ≈ 0.5

Experimental mass density data for the binary mixture of **ethanol + water** near equimolar composition at 298.15 K were found in the ThermoML database.

**Source:** DOI [10.1016/j.fluid.2004.11.019](https://doi.org/10.1016/j.fluid.2004.11.019) (GLOBlit_220, block PROPblock_2)

##### Key details

- The dataset contains **810 data points** covering temperatures 298.15–348.15 K, pressures 100–40000 kPa, and ethanol mole fractions from 0.003 to 1.
- **No data point exists at exactly x_ethanol = 0.500**; the closest composition is **x_ethanol = 0.498** (the next nearest above is 0.5501).

##### Data at T = 298.15 K, x_ethanol = 0.498

| Pressure (kPa) | Mass Density (kg/m³) |
|:-:|:-:|
| 100 | 859.3 |
| 10 000 | 865.4 |
| 20 000 | 871.3 |
| 30 000 | 876.8 |
| 40 000 | 882.0 |

##### Atmospheric-pressure result

At **T = 298.15 K, P = 100 kPa, and x_ethanol = 0.498**, the mass density is **859.3 kg/m³**.

##### Chemistry context

This value sits between the densities of pure water (~997 kg/m³) and pure ethanol (~785 kg/m³) at the same temperature, but is closer to ethanol's value, reflecting the near-equimolar composition. The ethanol–water system is well known for its **negative excess volume** (volume contraction on mixing), meaning the actual mixture density is slightly higher than what a simple linear (ideal) mixing rule would predict. The systematic increase in density with pressure (859.3 → 882.0 kg/m³ over 100–40 000 kPa) is the expected isothermal compression behavior for a liquid mixture.

No uncertainty values were reported for these data points in the source block.

**Core claims:**
- Experimental mass density data for ethanol + water near equimolar composition at 298.15 K were found in the ThermoML database from DOI 10.1016/j.fluid.2004.11.019.
- The closest available ethanol mole fraction to 0.500 in the dataset is x_ethanol = 0.498.
- At T = 298.15 K, P = 100 kPa, and x_ethanol = 0.498, the mass density is 859.3 kg/m³.
- At T = 298.15 K and x_ethanol = 0.498, the mass density increases with pressure from 859.3 kg/m³ at 100 kPa to 882.0 kg/m³ at 40 000 kPa.
- No uncertainty values were reported for these data points in the source block.

**Sources:**

**WM_Q#1_Table#1_(Main_Q#1_Sources):**

| *row_id* | *lit_num_id* | *block* | *doi* | *BLKsubsys_id* | *description* |
|---|---|---|---|---|---|
| WM_Q#1_Table#1_Row#1 | 「GLOBlit_220」 | 「PROPblock_2」 | 「10.1016/j.fluid.2004.11.019」 | 「—」 | 「This block provides mass density data for the ethanol + water binary system covering T = 298.15–348.15 K, P = 100–40000 kPa, and ethanol mole fractions 0.003–1.0 (810 data points). It directly supports the answer's reported density of 859.3 kg/m³ at T = 298.15 K, P = 100 kPa, x_ethanol = 0.498, which falls within the block's density range of 739.4–1012.7 kg/m³.」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.

