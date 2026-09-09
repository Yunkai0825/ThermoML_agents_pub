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
- [L1] Find viscosity data for the ternary mixture DMF + water + acetonitrile at 298 K → stored as L1_query_1 · validation: PASS
- [L1] Find binary viscosity data for DMF + water at 298 K → stored as L1_query_2 · validation: PASS
- [L1] Find binary viscosity data for DMF + acetonitrile at 298 K → stored as L1_query_3 · validation: FLAGGED(4)
- [L1] Find binary viscosity data for water + acetonitrile at 298 K → stored as L1_query_4 · validation: PASS

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: no_results · validation: PASS

**Summary:** No viscosity data exists in the ThermoML database for the ternary mixture of dimethylformamide (DMF) + water + acetonitrile at 298 K or any other temperature. Searches for dynamic viscosity with all three compounds required, using both ternary and unrestricted system type filters with and without temperature constraints, all returned zero results. Binary viscosity data for pairs of these compounds may exist but was not the focus of the search.

**Answer:**

No viscosity data was found in the ThermoML database for the ternary mixture of dimethylformamide (DMF, GLOBcomp_18) + water (GLOBcomp_1) + acetonitrile (GLOBcomp_15) at 298 K or at any other temperature.

Searches were conducted for dynamic viscosity (GLOBprop_4) with all three compounds required, using both ternary system type and unrestricted system type filters, with and without temperature constraints. All searches returned zero results, confirming that the ThermoML database does not contain viscosity measurements for a system that includes all three of these compounds together.

Binary viscosity data for pairs of these compounds (e.g., DMF + water, DMF + acetonitrile, or water + acetonitrile) may exist in the database but was not the focus of this search.

**Core claims:**
- No viscosity data was found in the ThermoML database for the ternary mixture of dimethylformamide (DMF) + water + acetonitrile at 298 K or at any other temperature.
- Searches using dynamic viscosity with all three compounds required, under both ternary and unrestricted system type filters and with and without temperature constraints, all returned zero results.
- Binary viscosity data for pairs of these compounds may exist in the database but was not investigated.

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.
### L1_query_2
**L1_query_2** — status: success · validation: PASS

**Summary:** Dynamic viscosity data for the binary mixture of dimethylformamide (DMF) + water at 298.15 K were retrieved from two independent ThermoML sources. Source 1 (DOI 10.1021/je050209y, GLOBlit_8676, PROPblock_9) provides 11 data points at P = 101.325 kPa over x(DMF) = 0.05–0.9488, with viscosities ranging from 0.000843 to 0.002491 Pa·s. Source 2 (DOI 10.1021/je300608v, GLOBlit_9900, PROPblock_3) provides 15 data points (12 shown) at P = 101.0 kPa over x(water) = 0–1, with viscosities ranging from 0.0008045 to 0.0024775 Pa·s, including pure component values of 0.0008045 Pa·s for pure DMF and 0.0008903 Pa·s for pure water. The system exhibits a pronounced viscosity maximum at approximately x(water) ≈ 0.7 (x(DMF) ≈ 0.3), reaching about 0.0025 Pa·s — roughly 3× the viscosity of either pure component — indicative of strong hydrogen-bonding interactions between DMF's carbonyl group and water. The two datasets are in good agreement near the maximum: Source 1 reports 0.002491 Pa·s and Source 2 reports 0.0024775 Pa·s at comparable compositions. Two additional blocks (GLOBlit_11030::PROPblock_3 and GLOBlit_11207::PROPblock_3) may also contain relevant data but were not inspected in detail.

**Answer:**

#### Binary Viscosity Data: DMF + Water at 298.15 K

Dynamic viscosity data for the binary mixture of dimethylformamide (DMF, GLOBcomp_18) + water (GLOBcomp_1) at 298.15 K were found in the ThermoML database from two independent sources.

---

##### Source 1: DOI 10.1021/je050209y (GLOBlit_8676, PROPblock_9)

All 11 data points measured at T = 298.15 K, P = 101.325 kPa. Composition is expressed as mole fraction of DMF (x_DMF).

**WM_L1#2_Table#1_(Query_L1#2_Answer):**

| *row_id* | *x(DMF)* | *Viscosity (Pa·s)* |
|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「0.05」 | 「0.00131」 |
| WM_L1#2_Table#1_Row#2 | 「0.1001」 | 「0.001728」 |
| WM_L1#2_Table#1_Row#3 | 「0.2」 | 「0.002346」 |
| WM_L1#2_Table#1_Row#4 | 「0.299」 | 「0.002491」 |
| WM_L1#2_Table#1_Row#5 | 「0.3998」 | 「0.002273」 |
| WM_L1#2_Table#1_Row#6 | 「0.4997」 | 「0.001878」 |
| WM_L1#2_Table#1_Row#7 | 「0.5993」 | 「0.001532」 |
| WM_L1#2_Table#1_Row#8 | 「0.6995」 | 「0.001243」 |
| WM_L1#2_Table#1_Row#9 | 「0.8」 | 「0.001045」 |
| WM_L1#2_Table#1_Row#10 | 「0.8991」 | 「0.000901」 |
| WM_L1#2_Table#1_Row#11 | 「0.9488」 | 「0.000843」 |

**Range:** viscosity 0.000843–0.002491 Pa·s over x(DMF) = 0.05–0.9488.

---

##### Source 2: DOI 10.1021/je300608v (GLOBlit_9900, PROPblock_3)

15 data points at T = 298.15 K, P = 101.0 kPa (12 shown via RDP compression). Composition is expressed as mole fraction of water (x_water). This dataset includes both pure component endpoints.

**WM_L1#2_Table#2_(Query_L1#2_Answer):**

| *row_id* | *x(water)* | *Viscosity (Pa·s)* |
|---|---|---|
| WM_L1#2_Table#2_Row#1 | 「0」 | 「0.0008045」 |
| WM_L1#2_Table#2_Row#2 | 「0.1」 | 「0.0009018」 |
| WM_L1#2_Table#2_Row#3 | 「0.2」 | 「0.0010386」 |
| WM_L1#2_Table#2_Row#4 | 「0.3」 | 「0.0012331」 |
| WM_L1#2_Table#2_Row#5 | 「0.4」 | 「0.0015078」 |
| WM_L1#2_Table#2_Row#6 | 「0.5」 | 「0.0018528」 |
| WM_L1#2_Table#2_Row#7 | 「0.6」 | 「0.0022264」 |
| WM_L1#2_Table#2_Row#8 | 「0.7」 | 「0.0024775」 |
| WM_L1#2_Table#2_Row#9 | 「0.8」 | 「0.0023495」 |
| WM_L1#2_Table#2_Row#10 | 「0.9」 | 「0.0017464」 |
| WM_L1#2_Table#2_Row#11 | 「0.94」 | 「0.0014116」 |
| WM_L1#2_Table#2_Row#12 | 「1」 | 「0.0008903」 |

**Range:** viscosity 0.0008045–0.0024775 Pa·s over x(water) = 0–1.

**Pure component viscosities at 298.15 K (from Source 2):**
- Pure DMF (x_water = 0): 0.0008045 Pa·s
- Pure water (x_water = 1): 0.0008903 Pa·s

---

##### Chemical Insight

The DMF + water system exhibits a pronounced viscosity maximum at approximately x(water) ≈ 0.7 (equivalently x(DMF) ≈ 0.3), where viscosity reaches about 0.0025 Pa·s — roughly 3× the viscosity of either pure component. This non-monotonic behavior with a single extremum is characteristic of strong intermolecular interactions (hydrogen bonding between DMF's carbonyl group and water) that create structured molecular associations in the mixture. The two independent datasets are in good agreement: at comparable compositions near x(DMF) ≈ 0.3, Source 1 (GLOBlit_8676, PROPblock_9) reports 0.002491 Pa·s and Source 2 (GLOBlit_9900, PROPblock_3) reports 0.0024775 Pa·s.

Two additional blocks (GLOBlit_11030::PROPblock_3 and GLOBlit_11207::PROPblock_3) also contain DMF + water viscosity data that may include 298.15 K measurements but were not inspected in detail.

**Core claims:**
- Dynamic viscosity data for the DMF + water binary mixture at 298.15 K were found in two independent ThermoML sources (DOI 10.1021/je050209y and DOI 10.1021/je300608v), covering the full composition range.
- The system exhibits a pronounced viscosity maximum at approximately x(water) ≈ 0.7 (x(DMF) ≈ 0.3), where viscosity reaches about 0.0025 Pa·s — roughly 3× the viscosity of either pure component.
- Pure component viscosities at 298.15 K from Source 2 are 0.0008045 Pa·s for DMF and 0.0008903 Pa·s for water.
- The two independent datasets are in good agreement near x(DMF) ≈ 0.3: Source 1 reports 0.002491 Pa·s and Source 2 reports 0.0024775 Pa·s.
- The non-monotonic viscosity behavior with a single maximum is attributed to strong intermolecular hydrogen bonding between DMF's carbonyl group and water, creating structured molecular associations in the mixture.

**Core blocks found:**

**WM_L1#2_Blocks_(Query_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#3 | 「GLOBlit_8676」 | 「PROPblock_9」 | 「GLOBcomp_18, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of DMF + water at 298.15 K; 11 data points over x(DMF) = 0.05–0.9488, viscosity range 0.000843–0.002491 Pa·s.」 |
| WM_L1#2_Table#4 | 「GLOBlit_9900」 | 「PROPblock_3」 | 「GLOBcomp_18, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of DMF + water at 298.15 K; 15 data points (12 shown) over x(water) = 0–1 including pure component endpoints, viscosity range 0.0008045–0.0024775 Pa·s.」 |

*Not stored here: 2 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.
### L1_query_3
**L1_query_3** — status: success · validation: FLAGGED(4)

**Summary:** Dynamic viscosity data for the binary mixture of dimethylformamide (DMF) + acetonitrile at 298.15 K were retrieved from two independent ThermoML sources. Source 1 (DOI 10.1016/j.jct.2014.02.019) provides 5 data points by capillary (Ubbelohde) viscometry at 101.0 kPa as a function of mass fraction of DMF, with viscosity ranging from 0.000342 Pa·s (pure acetonitrile) to 0.0007986 Pa·s (pure DMF). Source 2 (DOI 10.1021/acs.jced.8b00176) provides 11 data points by falling sphere viscometry at 100.0 kPa as a function of mole fraction of DMF, with viscosity ranging from 0.00034 Pa·s (pure acetonitrile) to 0.00081 Pa·s (pure DMF). Pure component viscosities from the two sources are in excellent agreement. Unlike DMF + water, which shows a pronounced viscosity maximum due to strong hydrogen bonding, the DMF + acetonitrile system exhibits a nearly monotonic increase in viscosity from pure acetonitrile to pure DMF with no significant extremum, consistent with weaker, non-specific interactions between two aprotic solvents.

**Answer:**

###### Binary Viscosity Data: DMF + Acetonitrile at 298.15 K

Dynamic viscosity data for the binary mixture of dimethylformamide (DMF, GLOBcomp_18) + acetonitrile (GLOBcomp_15) at 298.15 K were found in the ThermoML database from two independent sources.

---

####### Source 1: DOI 10.1016/j.jct.2014.02.019 (GLOBlit_4124, PROPblock_6)

Measured by capillary (Ubbelohde) viscometry at T = 298.15 K, P = 101.0 kPa. Composition is expressed as mass fraction of DMF (w_DMF). 5 data points covering the full composition range including both pure component endpoints.

**WM_L1#3_Table#1_(Query_L1#3_Answer):**

| *row_id* | *w(DMF)* | *Viscosity (Pa·s)* |
|---|---|---|
| WM_L1#3_Table#1_Row#1 | 「0」 | 「0.000342」 |
| WM_L1#3_Table#1_Row#2 | 「0.25」 | 「0.0003959」 |
| WM_L1#3_Table#1_Row#3 | 「0.5」 | 「0.0005214」 |
| WM_L1#3_Table#1_Row#4 | 「0.75」 | 「0.0006465」 |
| WM_L1#3_Table#1_Row#5 | 「1」 | 「0.0007986」 |

**Range:** viscosity 0.000342–0.0007986 Pa·s over w(DMF) = 0–1.

---

####### Source 2: DOI 10.1021/acs.jced.8b00176 (GLOBlit_7481, PROPblock_18)

Measured by falling sphere viscometry at T = 298.15 K, P = 100.0 kPa. Composition is expressed as mole fraction of DMF (x_DMF). 11 data points covering the full composition range including both pure component endpoints.

**WM_L1#3_Table#2_(Query_L1#3_Answer):**

| *row_id* | *x(DMF)* | *Viscosity (Pa·s)* |
|---|---|---|
| WM_L1#3_Table#2_Row#1 | 「0」 | 「0.00034」 |
| WM_L1#3_Table#2_Row#2 | 「0.0989」 | 「0.0004」 |
| WM_L1#3_Table#2_Row#3 | 「0.1916」 | 「0.00044」 |
| WM_L1#3_Table#2_Row#4 | 「0.2925」 | 「0.00048」 |
| WM_L1#3_Table#2_Row#5 | 「0.3932」 | 「0.00054」 |
| WM_L1#3_Table#2_Row#6 | 「0.5029」 | 「0.00061」 |
| WM_L1#3_Table#2_Row#7 | 「0.6002」 | 「0.00065」 |
| WM_L1#3_Table#2_Row#8 | 「0.6931」 | 「0.00069」 |
| WM_L1#3_Table#2_Row#9 | 「0.7926」 | 「0.00075」 |
| WM_L1#3_Table#2_Row#10 | 「0.8996」 | 「0.00079」 |
| WM_L1#3_Table#2_Row#11 | 「1」 | 「0.00081」 |

**Range:** viscosity 0.00034–0.00081 Pa·s over x(DMF) = 0–1.

---

####### Pure Component Viscosities at 298.15 K

- **Pure acetonitrile:** 0.000342 Pa·s (GLOBlit_4124::PROPblock_6) and 0.00034 Pa·s (GLOBlit_7481::PROPblock_18) — in excellent agreement between the two independent sources.
- **Pure DMF:** 0.0007986 Pa·s (GLOBlit_4124::PROPblock_6) and 0.00081 Pa·s (GLOBlit_7481::PROPblock_18) — in good agreement between the two independent sources.

####### Chemical Insight

Unlike the DMF + water system, which exhibits a pronounced viscosity maximum (~3× pure component values) due to strong hydrogen bonding, the DMF + acetonitrile system shows a nearly monotonic increase in viscosity from pure acetonitrile to pure DMF with no significant extremum. This indicates weaker, non-specific intermolecular interactions between DMF and acetonitrile — both are aprotic solvents, so the strong hydrogen-bond-driven association seen with water is absent. The viscosity varies smoothly from 0.00034 Pa·s (pure acetonitrile, GLOBlit_7481::PROPblock_18) to 0.00081 Pa·s (pure DMF, GLOBlit_7481::PROPblock_18), a ratio of approximately 2.4× (derived by dividing 0.00081 by 0.00034, both from GLOBlit_7481::PROPblock_18).

**Core claims:**
- Dynamic viscosity data for the binary mixture DMF + acetonitrile at 298.15 K are available from two independent ThermoML sources: one (DOI 10.1016/j.jct.2014.02.019) reports 5 data points by mass fraction via Ubbelohde viscometry spanning 0.000342–0.0007986 Pa·s, and the other (DOI 10.1021/acs.jced.8b00176) reports 11 data points by mole fraction via falling sphere viscometry spanning 0.00034–0.00081 Pa·s.
- Pure acetonitrile viscosity at 298.15 K is reported as 0.000342 Pa·s (Source 1) and 0.00034 Pa·s (Source 2), in excellent agreement; pure DMF viscosity is reported as 0.0007986 Pa·s (Source 1) and 0.00081 Pa·s (Source 2), in good agreement.
- The DMF + acetonitrile system shows a nearly monotonic increase in viscosity from pure acetonitrile to pure DMF with no significant extremum, indicating weaker, non-specific intermolecular interactions between these two aprotic solvents, in contrast to the pronounced viscosity maximum seen in the DMF + water system.
- Several value-to-source attributions in the answer were flagged as misattributed between the two data blocks, though the numeric values themselves were verified as present in the database under the correct respective sources.

**Core blocks found:**

**WM_L1#3_Blocks_(Query_L1#3_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#3_Table#3 | 「GLOBlit_4124」 | 「PROPblock_6」 | 「GLOBcomp_18, GLOBcomp_15」 | 「GLOBprop_4」 | 「Dynamic viscosity of DMF + acetonitrile binary mixture at 298.15 K as a function of mass fraction of DMF (5 data points, w_DMF = 0–1, viscosity 0.000342–0.0007986 Pa·s).」 |
| WM_L1#3_Table#4 | 「GLOBlit_7481」 | 「PROPblock_18」 | 「GLOBcomp_18, GLOBcomp_15」 | 「GLOBprop_4」 | 「Dynamic viscosity of DMF + acetonitrile binary mixture at 298.15 K as a function of mole fraction of DMF (11 data points, x_DMF = 0–1, viscosity 0.00034–0.00081 Pa·s).」 |

*Not stored here: 2 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(4) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **MISATTRIBUTED_VALUE** PROPblock_18: 0.000342 does not belong to PROPblock_18; it matches only GLOBlit_4124::PROPblock_6 (inspected this run)
- **MISATTRIBUTED_VALUE** GLOBlit_7481::PROPblock_18: 0.0007986 does not belong to GLOBlit_7481::PROPblock_18; it matches only GLOBlit_4124::PROPblock_6 (inspected this run)
- **MISATTRIBUTED_VALUE** GLOBlit_4124::PROPblock_6: 0.00081 does not belong to GLOBlit_4124::PROPblock_6; it matches only GLOBlit_7481::PROPblock_18 (inspected this run)
- **UNGROUNDED_LITERAL** GLOBlit_7481::PROPblock_18: 2.4 (near '…:: ), a ratio of approximately 2.4× (derived by dividing 0.0…') matches no inspected row/stat, database table, or other source of GLOBlit_7481::PROPblock_18
### L1_query_4
**L1_query_4** — status: success · validation: PASS

**Summary:** Dynamic viscosity data for the binary mixture water + acetonitrile at 298.15 K were found in the ThermoML database from DOI 10.1016/j.jct.2005.08.009 (GLOBlit_2602, PROPblock_3), measured by capillary tube viscometry at P = 101.0 kPa. The dataset contains 16 data points covering the full composition range (mole fraction of acetonitrile 0–1), with viscosity ranging from 0.0003417 to 0.0009849 Pa·s. Pure water viscosity is 0.0008901 Pa·s and pure acetonitrile viscosity is 0.0003417 Pa·s. A small viscosity maximum of 0.0009849 Pa·s occurs near x(acetonitrile) ≈ 0.051, slightly above the pure water value; beyond this composition viscosity decreases monotonically toward pure acetonitrile. The slight maximum at dilute acetonitrile content suggests modest enhancement of the hydrogen-bond network, consistent with acetonitrile being a weaker hydrogen-bond acceptor than DMF. The full block also contains data at temperatures up to 318.15 K (80 total data points across all temperatures), but only the 298.15 K isotherm was inspected.

**Answer:**

###### Binary Viscosity Data: Water + Acetonitrile at 298.15 K

Dynamic viscosity data for the binary mixture of water (GLOBcomp_1) + acetonitrile (GLOBcomp_15) at 298.15 K were found in the ThermoML database from one source.

---

####### Source: DOI 10.1016/j.jct.2005.08.009 (GLOBlit_2602, PROPblock_3)

Measured by capillary tube viscometry (GLOBmeas_140) at T = 298.15 K, P = 101.0 kPa. Composition is expressed as mole fraction of acetonitrile (x_ACN). The block contains 16 data points at 298.15 K, covering the full composition range including both pure component endpoints.

**WM_L1#4_Table#1_(Query_L1#4_Answer):**

| *row_id* | *x(acetonitrile)* | *Viscosity (Pa·s)* |
|---|---|---|
| WM_L1#4_Table#1_Row#1 | 「0」 | 「0.0008901」 |
| WM_L1#4_Table#1_Row#2 | 「0.051」 | 「0.0009849」 |
| WM_L1#4_Table#1_Row#3 | 「0.1169」 | 「0.0009567」 |
| WM_L1#4_Table#1_Row#4 | 「0.1971」 | 「0.0008743」 |
| WM_L1#4_Table#1_Row#5 | 「0.4417」 | 「0.0006061」 |
| WM_L1#4_Table#1_Row#6 | 「0.5204」 | 「0.0005387」 |
| WM_L1#4_Table#1_Row#7 | 「0.6012」 | 「0.0004802」 |
| WM_L1#4_Table#1_Row#8 | 「0.6671」 | 「0.0004415」 |
| WM_L1#4_Table#1_Row#9 | 「0.7398」 | 「0.0004064」 |
| WM_L1#4_Table#1_Row#10 | 「0.8253」 | 「0.0003722」 |
| WM_L1#4_Table#1_Row#11 | 「0.886」 | 「0.0003561」 |
| WM_L1#4_Table#1_Row#12 | 「0.9389」 | 「0.0003478」 |
| WM_L1#4_Table#1_Row#13 | 「1」 | 「0.0003417」 |

**Range:** viscosity 0.0003417–0.0009849 Pa·s over x(acetonitrile) = 0–1 (16 data points total at 298.15 K).

---

####### Pure Component Viscosities at 298.15 K

- **Pure water** (x_ACN = 0): 0.0008901 Pa·s
- **Pure acetonitrile** (x_ACN = 1): 0.0003417 Pa·s

---

####### Chemical Insight

The water + acetonitrile system exhibits a small viscosity maximum near x(acetonitrile) ≈ 0.051, where viscosity reaches 0.0009849 Pa·s — slightly above the pure water value of 0.0008901 Pa·s. Beyond this low-acetonitrile composition, viscosity decreases monotonically toward pure acetonitrile (0.0003417 Pa·s). The slight maximum at very low acetonitrile content suggests modest enhancement of the hydrogen-bond network at dilute acetonitrile concentrations, but the effect is far less pronounced than in the DMF + water system (which, per prior query results not inspected in this run, reaches a substantially higher viscosity maximum). This is consistent with acetonitrile being a weaker hydrogen-bond acceptor than DMF, leading to less structured molecular associations with water.

The full block (GLOBlit_2602::PROPblock_3) also contains viscosity data at temperatures up to 318.15 K (80 total data points across all temperatures), but only the 298.15 K isotherm was inspected here.

**Core claims:**
- Dynamic viscosity data for the water + acetonitrile binary mixture at 298.15 K and 101.0 kPa were obtained from one ThermoML source (DOI 10.1016/j.jct.2005.08.009), measured by capillary tube viscometry, covering 16 data points across the full composition range (x_ACN = 0 to 1).
- Viscosity ranges from 0.0003417 Pa·s (pure acetonitrile) to 0.0009849 Pa·s over the composition range, with pure water at 0.0008901 Pa·s.
- A small viscosity maximum of 0.0009849 Pa·s occurs near x(acetonitrile) ≈ 0.051, slightly above the pure water value; beyond this composition viscosity decreases monotonically toward pure acetonitrile.
- The slight viscosity maximum at low acetonitrile content suggests modest enhancement of the hydrogen-bond network at dilute acetonitrile concentrations, but the effect is far less pronounced than in the DMF + water system, consistent with acetonitrile being a weaker hydrogen-bond acceptor than DMF.
- The inspected data cover only the 298.15 K isotherm; the full source block contains 80 data points across temperatures up to 318.15 K.

**Core blocks found:**

**WM_L1#4_Blocks_(Query_L1#4_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#4_Table#2 | 「GLOBlit_2602」 | 「PROPblock_3」 | 「GLOBcomp_15, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity data for water + acetonitrile at 298.15 K covering full composition range (16 data points), measured by capillary tube viscometry at 101.0 kPa.」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


