# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260815_194252_569587_5a4acc5e`

### History
- [query:Q1] "Find surface tension data for binary mixtures of methanol and acetonitrile near " (120s, 2 iters, validation=PASS verdict=## Verdict
The answer appears )

### Query Agent Results

#### Q1
**Q1** — confidence: high · validation: PASS

**Answer:**

#### Surface Tension of Methanol + Acetonitrile Binary Mixtures near Room Temperature

##### Source

- **DOI:** 10.1021/je050519g
- **Title:** *Density and Surface Tension of Binary Mixtures of Acetonitrile + 1-Alkanol at 293.15 K*
- **Block:** PROPblock_13

##### Experimental Details

**WM_Q#1_Table#1_(Main_Q#1_Answer):**

| *row_id* | *Detail* | *Value* |
|---|---|---|
| WM_Q#1_Table#1_Row#1 | 「**Compounds**」 | 「Acetonitrile (C₂H₃N) + Methanol (CH₄O)」 |
| WM_Q#1_Table#1_Row#2 | 「**Property**」 | 「Surface tension, liquid–gas (N/m)」 |
| WM_Q#1_Table#1_Row#3 | 「**Measurement method**」 | 「Pendant drop shape」 |
| WM_Q#1_Table#1_Row#4 | 「**Temperature**」 | 「293.15 K (fixed)」 |
| WM_Q#1_Table#1_Row#5 | 「**Composition variable**」 | 「Mole fraction of acetonitrile in the liquid phase」 |
| WM_Q#1_Table#1_Row#6 | 「**Composition range**」 | 「0.1001 – 0.8956」 |

##### Measured Data (T = 293.15 K)

**WM_Q#1_Table#2_(Main_Q#1_Answer):**

| *row_id* | *x(acetonitrile)* | *Surface tension γ (N/m)* |
|---|---|---|
| WM_Q#1_Table#2_Row#1 | 「0.1001」 | 「0.0238」 |
| WM_Q#1_Table#2_Row#2 | 「0.2011」 | 「0.02473」 |
| WM_Q#1_Table#2_Row#3 | 「0.2996」 | 「0.02553」 |
| WM_Q#1_Table#2_Row#4 | 「0.4997」 | 「0.02685」 |
| WM_Q#1_Table#2_Row#5 | 「0.7012」 | 「0.02794」 |
| WM_Q#1_Table#2_Row#6 | 「0.8009」 | 「0.02842」 |
| WM_Q#1_Table#2_Row#7 | 「0.8956」 | 「0.02885」 |

##### Composition Dependence and Chemical Insight

The surface tension increases **monotonically** with increasing acetonitrile mole fraction across the full measured composition range. At the methanol-rich end (x = 0.1001), γ = 0.0238 N/m, while at the acetonitrile-rich end (x = 0.8956), γ = 0.02885 N/m — a span of about 5 mN/m. This is consistent with the known pure-component surface tensions: methanol (~22.1 mN/m at 293 K) is lower than acetonitrile (~29.0 mN/m), so adding acetonitrile steadily raises the mixture's surface tension.

The smooth, monotonic trend with **no extrema** (no minimum or maximum) suggests relatively ideal mixing behavior at the liquid–gas interface for this system. Both components are small, polar molecules capable of hydrogen bonding (methanol as both donor and acceptor, acetonitrile primarily as an acceptor), and their similar molecular sizes and polarities lead to near-ideal surface behavior.

##### Data Availability Note

Only **one dataset** was found in the ThermoML database for this binary system, measured at a single temperature of **293.15 K**. No additional surface tension data at other temperatures within the 293–303 K window were available.

**Core claims:**
- At 293.15 K, the surface tension of methanol + acetonitrile binary mixtures increases monotonically with increasing acetonitrile mole fraction, from 0.0238 N/m at x(acetonitrile) = 0.1001 to 0.02885 N/m at x(acetonitrile) = 0.8956, with no extrema observed.
- The monotonic increase is consistent with methanol having a lower pure-component surface tension (~22.1 mN/m) than acetonitrile (~29.0 mN/m) at 293 K, and the absence of extrema suggests relatively ideal mixing behavior at the liquid–gas interface.
- Only one dataset was found in the ThermoML database for this binary system, measured at a single temperature of 293.15 K using the pendant drop shape method; no additional surface tension data at other temperatures within the 293–303 K window were available.

**Sources:**

**WM_Q#1_Table#3_(Main_Q#1_Sources):**

| *row_id* | *lit_num_id* | *block* | *doi* | *BLKsubsys_id* | *description* |
|---|---|---|---|---|---|
| WM_Q#1_Table#3_Row#1 | 「GLOBlit_8821」 | 「PROPblock_13」 | 「10.1021/je050519g」 | 「—」 | 「This block provides the only available surface tension data for the methanol + acetonitrile binary system, with 7 datapoints at 293.15 K covering mole fractions 0.1001–0.8956 and surface tensions 0.0238–0.02885 N/m measured by pendant drop shape. It directly and fully supports the answer.」 |

*Not stored here: 1 verbatim data_inspections table(s); 5 id_catalog_snapshot row(s) (catalog is merged separately). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.

