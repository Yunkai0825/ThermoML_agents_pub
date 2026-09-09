# Q4.6 — Tool Trace

**Prompt:** Among aqueous mixtures of organic solvents, how does viscosity change with the molecular structure of the organic component, and which intermolecular interactions explain the trend?

**Summary:** 838.6s  |  4 iterations  |  3 tools

---

### Step 1: `L1_query`
- **Args:** `{"context": "...", "id_catalog": "...", "instruction": "...", "purpose": "..."}`
- **Result size:** 41,797 chars
- **Elapsed:** 259.3s

### Step 2: `L1_query`
- **Args:** `{"context": "...", "id_catalog": "...", "instruction": "...", "purpose": "..."}`
- **Result size:** 21,173 chars
- **Elapsed:** 98.3s

### Step 3: `L1_query`
- **Args:** `{"context": "...", "id_catalog": "...", "instruction": "...", "purpose": "..."}`
- **Result size:** 305 chars
- **Elapsed:** 328.5s

---

## Working Memory (final snapshot)

# Working Memory

## ID Catalog
<!-- PROTECTED — never compacted. Auto-populated by catalog ops. -->
### Resolved Entities
| type | global_id | registry_id | name |
|------|--------|----|------|
| comp | GLOBcomp_1 | water | water |
| comp | GLOBcomp_2 | ethanol | ethanol |
| comp | GLOBcomp_4 | methanol | methanol |
| comp | GLOBcomp_5 | propan-1-ol | propan-1-ol |
| comp | GLOBcomp_6 | propan-2-ol | propan-2-ol |
| prop | GLOBprop_4 | viscosity_pa_s | Viscosity, Pa*s |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|
| lit | GLOBlit_2825 | 2007-gon-cal-1 | 10.1016/j.jct.2007.05.004 |
| lit | GLOBlit_11042 | 2008-gon-cal-0 | 10.1021/je700700f |

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find viscosity data for aqueous mixtures of small alcohols (methanol, ethanol, 1-propanol, 2-propanol) to compare how al → stored as L1_query_1 · validation: FLAGGED(3)
- [L1] Inspect the 2-propanol + water viscosity data block PROPblock_15 to get verified individual data points → stored as L1_query_2 · validation: FLAGGED(1)

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: FLAGGED(3)

**Summary:** Dynamic viscosity (η, Pa·s) data at 298.15 K and 101 kPa were compiled for four binary alcohol–water systems from ThermoML sources (DOI 10.1016/j.jct.2007.05.004 and DOI 10.1021/je700700f), all measured by capillary tube (Ubbelohde). Three systems were fully inspected; the fourth (2-propanol + water) was identified but not inspected. For methanol + water, 12 data points span x(water) 0–1 with η ranging from 0.000545 (pure methanol) to a peak of 0.001554 Pa·s at x(water) ≈ 0.70. For ethanol + water, 12 data points span x(water) 0–1 with η ranging from 0.001082 (pure ethanol) to a peak of 0.0023 Pa·s at x(water) ≈ 0.80. For 1-propanol + water, 11 data points span x(1-propanol) 0–1 with η ranging from 0.00089 (pure water) to a peak of 0.002691 Pa·s at x(1-propanol) ≈ 0.30. Pure-component viscosities at 298.15 K are: water 0.00089, methanol 0.000545, ethanol 0.001082, and 1-propanol 0.002017 Pa·s. All systems exhibit a viscosity maximum at intermediate composition, attributed to strong hydrogen-bonding interactions and hydrophobic hydration effects. Peak viscosity increases with alkyl chain length: methanol (0.001554) < ethanol (0.0023) < 1-propanol (0.002691 Pa·s). The 2-propanol + water block (PROPblock_15, 13 data points) was identified with a search-level aggregate viscosity range of 0.00089–0.003087 Pa·s but individual data points were not verified by inspection and are flagged as unverified.

**Answer:**

#### Dynamic Viscosity of Aqueous Alcohol Mixtures at 298.15 K

##### Overview

Four binary alcohol–water systems were investigated for dynamic viscosity (η, Pa·s) data at 298.15 K and 101 kPa across the full composition range. Three systems were fully inspected; the fourth (2-propanol + water) was identified but not inspected in this run.

---

##### 1. Methanol + Water

**Source:** DOI 10.1016/j.jct.2007.05.004 [GLOBlit_2825], PROPblock_9
**Compounds:** water (GLOBcomp_1) + methanol (GLOBcomp_4)
**Method:** Capillary tube (Ubbelohde)
**Composition variable:** mole fraction of water

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *x(water)* | *η (Pa·s)* |
|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「0」 | 「0.000545」 |
| WM_L1#1_Table#1_Row#2 | 「0.049」 | 「0.000607」 |
| WM_L1#1_Table#1_Row#3 | 「0.0993」 | 「0.000677」 |
| WM_L1#1_Table#1_Row#4 | 「0.1973」 | 「0.000821」 |
| WM_L1#1_Table#1_Row#5 | 「0.2983」 | 「0.000987」 |
| WM_L1#1_Table#1_Row#6 | 「0.3985」 | 「0.00115」 |
| WM_L1#1_Table#1_Row#7 | 「0.5994」 | 「0.001463」 |
| WM_L1#1_Table#1_Row#8 | 「0.6997」 | 「0.001554」 |
| WM_L1#1_Table#1_Row#9 | 「0.7986」 | 「0.001542」 |
| WM_L1#1_Table#1_Row#10 | 「0.8999」 | 「0.001317」 |
| WM_L1#1_Table#1_Row#11 | 「0.9512」 | 「0.001121」 |
| WM_L1#1_Table#1_Row#12 | 「1.0」 | 「0.00089」 |

**Peak viscosity:** 0.001554 Pa·s at x(water) ≈ 0.70 (i.e., x(methanol) ≈ 0.30).

---

##### 2. Ethanol + Water

**Source:** DOI 10.1016/j.jct.2007.05.004 [GLOBlit_2825], PROPblock_11
**Compounds:** water (GLOBcomp_1) + ethanol (GLOBcomp_2)
**Method:** Capillary tube (Ubbelohde)
**Composition variable:** mole fraction of water

**WM_L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *x(water)* | *η (Pa·s)* |
|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「0」 | 「0.001082」 |
| WM_L1#1_Table#2_Row#2 | 「0.0501」 | 「0.001153」 |
| WM_L1#1_Table#2_Row#3 | 「0.0986」 | 「0.001232」 |
| WM_L1#1_Table#2_Row#4 | 「0.1961」 | 「0.00138」 |
| WM_L1#1_Table#2_Row#5 | 「0.2961」 | 「0.001531」 |
| WM_L1#1_Table#2_Row#6 | 「0.3991」 | 「0.001659」 |
| WM_L1#1_Table#2_Row#7 | 「0.5989」 | 「0.002115」 |
| WM_L1#1_Table#2_Row#8 | 「0.6991」 | 「0.002275」 |
| WM_L1#1_Table#2_Row#9 | 「0.8001」 | 「0.0023」 |
| WM_L1#1_Table#2_Row#10 | 「0.8996」 | 「0.00186」 |
| WM_L1#1_Table#2_Row#11 | 「0.9499」 | 「0.001388」 |
| WM_L1#1_Table#2_Row#12 | 「1.0」 | 「0.00089」 |

**Peak viscosity:** 0.0023 Pa·s at x(water) ≈ 0.80 (i.e., x(ethanol) ≈ 0.20).

---

##### 3. 1-Propanol + Water

**Source:** DOI 10.1021/je700700f [GLOBlit_11042], PROPblock_12
**Compounds:** water (GLOBcomp_1) + 1-propanol (GLOBcomp_5)
**Method:** Capillary tube (Ubbelohde)
**Composition variable:** mole fraction of 1-propanol

**WM_L1#1_Table#3_(Query_L1#1_Answer):**

| *row_id* | *x(1-propanol)* | *η (Pa·s)* |
|---|---|---|
| WM_L1#1_Table#3_Row#1 | 「0」 | 「0.00089」 |
| WM_L1#1_Table#3_Row#2 | 「0.0504」 | 「0.001616」 |
| WM_L1#1_Table#3_Row#3 | 「0.0993」 | 「0.002121」 |
| WM_L1#1_Table#3_Row#4 | 「0.1986」 | 「0.002599」 |
| WM_L1#1_Table#3_Row#5 | 「0.2979」 | 「0.002691」 |
| WM_L1#1_Table#3_Row#6 | 「0.3949」 | 「0.00261」 |
| WM_L1#1_Table#3_Row#7 | 「0.4955」 | 「0.002494」 |
| WM_L1#1_Table#3_Row#8 | 「0.5953」 | 「0.002339」 |
| WM_L1#1_Table#3_Row#9 | 「0.8983」 | 「0.002026」 |
| WM_L1#1_Table#3_Row#10 | 「0.9518」 | 「0.001998」 |
| WM_L1#1_Table#3_Row#11 | 「1.0」 | 「0.002017」 |

**Peak viscosity:** 0.002691 Pa·s at x(1-propanol) ≈ 0.30. The topology is non-monotonic with 2 extrema.

---

##### 4. 2-Propanol + Water

**Source:** DOI 10.1021/je700700f [GLOBlit_11042], PROPblock_15
**Compounds:** water (GLOBcomp_1) + 2-propanol (GLOBcomp_6)
**Method:** Capillary tube (Ubbelohde)

This block was identified (13 data points at 298.15 K, x(2-propanol) = 0–1) but **was not inspected in this run**. Block-level aggregate from the search result: viscosity range 0.00089–0.003087 Pa·s across the full composition range. Individual data points cannot be quoted.

---

##### Comparative Chemistry Insights

All four alcohol–water systems display a **viscosity maximum** at an intermediate composition — a hallmark of strong hydrogen-bonding interactions between water and alcohol molecules that create transient, more structured networks compared to either pure component.

**Effect of chain length (methanol → ethanol → 1-propanol):**

Using the inspected peak viscosities at 298.15 K:

**WM_L1#1_Table#4_(Query_L1#1_Answer):**

| *row_id* | *Alcohol* | *Peak η (Pa·s)* | *Approx. x(alcohol) at peak* |
|---|---|---|---|
| WM_L1#1_Table#4_Row#1 | 「Methanol」 | 「0.001554」 | 「~0.30」 |
| WM_L1#1_Table#4_Row#2 | 「Ethanol」 | 「0.0023」 | 「~0.20」 |
| WM_L1#1_Table#4_Row#3 | 「1-Propanol」 | 「0.002691」 | 「~0.30」 |

The peak viscosity increases with increasing alkyl chain length: methanol (0.001554) < ethanol (0.0023) < 1-propanol (0.002691 Pa·s). Longer hydrocarbon chains enhance hydrophobic hydration effects, where water molecules form more ordered cage-like structures around the non-polar portion of the alcohol, increasing the effective viscosity of the mixture.

The peak shifts to lower alcohol mole fractions for ethanol compared to methanol, reflecting the greater disruption per molecule that a larger alcohol exerts on the water network.

**Effect of branching (1-propanol vs. 2-propanol):**

Both propanol isomers (C₃H₈O) were found in the database. The 1-propanol peak viscosity is 0.002691 Pa·s. The 2-propanol search-level aggregate indicates a maximum of 0.003087 Pa·s (from the search result, not individually inspected). If this aggregate is accurate, branching in 2-propanol may produce a slightly higher peak viscosity, possibly because the more compact, branched geometry promotes tighter hydration shell packing. However, this comparison should be confirmed with a full inspection of the 2-propanol data.

**Pure-component viscosities at 298.15 K** (from inspected data):
- Water: 0.00089 Pa·s (consistent across all blocks)
- Methanol: 0.000545 Pa·s
- Ethanol: 0.001082 Pa·s
- 1-Propanol: 0.002017 Pa·s

Pure alcohol viscosity increases with chain length, consistent with stronger van der Waals interactions and more extensive hydrogen-bonding networks in the longer-chain alcohols.

**Core claims:**
- At 298.15 K and 101 kPa, aqueous mixtures of methanol, ethanol, and 1-propanol each exhibit a viscosity maximum at an intermediate composition, attributed to strong hydrogen-bonding interactions and transient structured networks between water and alcohol molecules.
- The inspected peak dynamic viscosities at 298.15 K increase with alcohol chain length: methanol 0.001554 Pa·s at x(methanol) ≈ 0.30, ethanol 0.0023 Pa·s at x(ethanol) ≈ 0.20, and 1-propanol 0.002691 Pa·s at x(1-propanol) ≈ 0.30.
- Pure-component dynamic viscosities at 298.15 K from the inspected data are: water 0.00089 Pa·s, methanol 0.000545 Pa·s, ethanol 0.001082 Pa·s, and 1-propanol 0.002017 Pa·s, with pure alcohol viscosity increasing with chain length.
- The 2-propanol + water system was identified but not inspected; its aggregate search-level maximum viscosity of 0.003087 Pa·s and any comparison with 1-propanol remain unverified.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#5 | 「GLOBlit_2825」 | 「PROPblock_9」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of methanol + water binary mixture at 298.15 K across the full composition range, measured by capillary tube (Ubbelohde) method.」 |
| WM_L1#1_Table#6 | 「GLOBlit_2825」 | 「PROPblock_11」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of ethanol + water binary mixture at 298.15 K across the full composition range, measured by capillary tube (Ubbelohde) method.」 |
| WM_L1#1_Table#7 | 「GLOBlit_11042」 | 「PROPblock_12」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of 1-propanol + water binary mixture at 298.15 K across the full composition range, measured by capillary tube (Ubbelohde) method.」 |
| WM_L1#1_Table#8 | 「GLOBlit_11042」 | 「PROPblock_15」 | 「GLOBcomp_6, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of 2-propanol + water binary mixture at 298.15 K across the full composition range. Block identified but not inspected; individual data points unverified.」 |

*Not stored here: 3 verbatim data_inspections table(s); 8 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(3) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNINSPECTED_BLOCK** PROPblock_15: PROPblock_15 is quoted with data values (13, 298.15, 0.00089, 0.003087, …) but was never inspected in this run
- **UNINSPECTED_BLOCK** PROPblock_15: PROPblock_15 is quoted with data values (0.001554, 0.30, 0.0023, 0.20, …) but was never inspected in this run
- **UNINSPECTED_BLOCK** PROPblock_15: PROPblock_15 is quoted with data values (0.001554, 0.0023, 0.002691, 0.002691, …) but was never inspected in this run
### L1_query_2
**L1_query_2** — status: success · validation: FLAGGED(1)

**Summary:** Dynamic viscosity of 2-propanol + water mixtures at 298.15 K and 101.0 kPa from DOI 10.1021/je700700f (PROPblock_15), measured by capillary tube (Ubbelohde). Composition spans x(2-propanol) = 0–1 (13 data points). The viscosity is non-monotonic, peaking at 0.003087 Pa·s near x(2-propanol) ≈ 0.30. Pure-component viscosities: water 0.00089 Pa·s, 2-propanol 0.002082 Pa·s. Compared with 1-propanol + water data from the same source (PROPblock_12), the branched isomer 2-propanol yields a higher peak viscosity (0.003087 vs. 0.002691 Pa·s, ~15% increase) at a similar composition, despite comparable pure-component viscosities (2-propanol 0.002082 vs. 1-propanol 0.002017 Pa·s), suggesting enhanced hydrophobic hydration effects for the branched geometry.

**Answer:**

###### 2-Propanol + Water: Dynamic Viscosity at 298.15 K (Inspected Data)

**Source:** DOI 10.1021/je700700f [GLOBlit_11042], PROPblock_15  
**Compounds:** water (GLOBcomp_1) + 2-propanol (GLOBcomp_6)  
**Method:** Capillary tube (Ubbelohde)  
**Conditions:** T = 298.15 K, P = 101.0 kPa  
**Composition variable:** mole fraction of 2-propanol  

**WM_L1#2_Table#1_(Query_L1#2_Answer):**

| *row_id* | *x(2-propanol)* | *η (Pa·s)* |
|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「0」 | 「0.00089」 |
| WM_L1#2_Table#1_Row#2 | 「0.0491」 | 「0.001718」 |
| WM_L1#2_Table#1_Row#3 | 「0.1008」 | 「0.002495」 |
| WM_L1#2_Table#1_Row#4 | 「0.2011」 | 「0.003038」 |
| WM_L1#2_Table#1_Row#5 | 「0.2994」 | 「0.003087」 |
| WM_L1#2_Table#1_Row#6 | 「0.3992」 | 「0.002924」 |
| WM_L1#2_Table#1_Row#7 | 「0.6987」 | 「0.002274」 |
| WM_L1#2_Table#1_Row#8 | 「0.7993」 | 「0.002153」 |
| WM_L1#2_Table#1_Row#9 | 「0.8998」 | 「0.002073」 |
| WM_L1#2_Table#1_Row#10 | 「1」 | 「0.002082」 |

*(10 of 13 data points shown via RDP shape-preserving selection; full block contains 13 points spanning x = 0–1)*

**Peak viscosity:** 0.003087 Pa·s at x(2-propanol) ≈ 0.30.  
**Full range (from stats, n = 13):** η = 0.00089–0.003087 Pa·s.  
**Topology:** Non-monotonic with 2 extrema.

**Pure-component viscosities at 298.15 K:**
- Water: 0.00089 Pa·s (x = 0)
- 2-Propanol: 0.002082 Pa·s (x = 1)

####### Comparison: 1-Propanol vs. 2-Propanol (Branching Effect)

Both propanol isomers (C₃H₈O) in water show a viscosity maximum near x(alcohol) ≈ 0.30:

**WM_L1#2_Table#2_(Query_L1#2_Answer):**

| *row_id* | *Alcohol* | *Peak η (Pa·s)* | *x(alcohol) at peak* | *Pure alcohol η (Pa·s)* | *Source block* |
|---|---|---|---|---|---|
| WM_L1#2_Table#2_Row#1 | 「1-Propanol」 | 「0.002691 *(PROPblock_12, GLOBlit_11042, inspected this run)*」 | 「~0.30」 | 「0.002017 *(PROPblock_12, GLOBlit_11042, inspected this run)*」 | 「PROPblock_12」 |
| WM_L1#2_Table#2_Row#2 | 「2-Propanol」 | 「0.003087」 | 「~0.30」 | 「0.002082」 | 「PROPblock_15」 |

The branched isomer (2-propanol) produces a **higher peak viscosity** (0.003087 Pa·s from PROPblock_15 vs. 0.002691 Pa·s from PROPblock_12, a ~15% increase) despite having a similar pure-component viscosity. This suggests that the more compact, branched geometry of 2-propanol promotes tighter hydration shell packing and stronger hydrophobic hydration effects in aqueous mixtures compared to the linear 1-propanol isomer.

Both data sets come from the same laboratory (DOI 10.1021/je700700f), measured by the same capillary tube method at identical conditions, making the comparison internally consistent.

**Core claims:**
- For 2-propanol + water at 298.15 K and 101.0 kPa (DOI 10.1021/je700700f, PROPblock_15), dynamic viscosity is non-monotonic with composition, exhibiting a peak of 0.003087 Pa·s at x(2-propanol) ≈ 0.30, compared to pure-component values of 0.00089 Pa·s (water) and 0.002082 Pa·s (2-propanol).
- Both 1-propanol and 2-propanol in water show a viscosity maximum near x(alcohol) ≈ 0.30; the branched isomer (2-propanol) exhibits a higher peak viscosity (0.003087 Pa·s from PROPblock_15) than the linear isomer (0.002691 Pa·s from PROPblock_12), despite similar pure-component viscosities, based on internally consistent data from the same laboratory and method.
- The 1-propanol peak viscosity value of 0.002691 Pa·s is attributed to PROPblock_12 (not PROPblock_15); a misattribution flag was raised and corrected within the answer.

**Core blocks found:**

**WM_L1#2_Blocks_(Query_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#3 | 「GLOBlit_11042」 | 「PROPblock_15」 | 「GLOBcomp_6, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of 2-propanol + water at 298.15 K and 101 kPa across the full composition range (13 data points, 10 returned via RDP selection). Peak viscosity 0.003087 Pa·s at x(2-propanol) ≈ 0.30.」 |
| WM_L1#2_Table#4 | 「GLOBlit_11042」 | 「PROPblock_12」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of 1-propanol + water referenced for branching comparison; peak viscosity 0.002691 Pa·s at x ≈ 0.30, pure 1-propanol 0.002017 Pa·s.」 |

*Not stored here: 2 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(1) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **MISATTRIBUTED_VALUE** PROPblock_15: 0.002691 does not belong to PROPblock_15; it matches only GLOBlit_11042::PROPblock_12 (inspected this run)

---

**Total:** 3 tool calls  |  838.6s  |  OK
