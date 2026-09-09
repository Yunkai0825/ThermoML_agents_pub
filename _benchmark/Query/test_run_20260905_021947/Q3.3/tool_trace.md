# Q3.3 — Tool Trace

**Prompt:** For aqueous propan-2-ol, which study provides the most complete experimental characterization? What properties were measured, which methods were used, and what purities were reported for the compounds?

**Summary:** 1000.2s  |  4 iterations  |  3 tools

---

### Step 1: `L1_query`
- **Args:** `{"context": "...", "id_catalog": "...", "instruction": "...", "purpose": "..."}`
- **Result size:** 415 chars
- **Elapsed:** 271.4s

### Step 2: `L1_query`
- **Args:** `{"context": "...", "id_catalog": "...", "instruction": "...", "purpose": "..."}`
- **Result size:** 278 chars
- **Elapsed:** 390.0s

### Step 3: `L1_query`
- **Args:** `{"context": "...", "id_catalog": "...", "instruction": "...", "purpose": "..."}`
- **Result size:** 5,904 chars
- **Elapsed:** 244.3s

---

## Working Memory (final snapshot)

# Working Memory

## ID Catalog
<!-- PROTECTED — never compacted. Auto-populated by catalog ops. -->
### Resolved Entities
| type | global_id | registry_id | name |
|------|--------|----|------|
| comp | GLOBcomp_1 | water | water |
| comp | GLOBcomp_6 | propan-2-ol | propan-2-ol |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find all literature entries (studies) in ThermoML that report experimental data for the binary system water + propan-2-o → stored as L1_query_1 · validation: PASS

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: PASS

**Summary:** The ThermoML database contains 71 declared binary data blocks across 38 distinct DOIs for the water + propan-2-ol system, totaling approximately 2,893 data points. Properties covered include boiling temperature, equilibrium mole fraction, azeotropic temperature and composition, mass density, molar heat capacity (Cp), viscosity, surface tension, speed of sound, refractive index, excess molar enthalpy, electrical conductivity, and vapor pressure. The most property-diverse study is GLOBlit_1423 (DOI 10.1016/j.fluid.2014.02.006), reporting four distinct VLE-related properties (boiling temperature, mole fraction, azeotropic temperature, azeotropic composition) across 36 data points. The most data-rich study is GLOBlit_1311 (DOI 10.1016/j.fluid.2013.08.007), with 1,248 data points covering mass density (1,110 pts) and molar Cp (138 pts). Other notable studies include GLOBlit_2096 (DOI 10.1016/j.fluid.2017.09.010, 3 properties, 37 points), GLOBlit_2432 (DOI 10.1016/j.jct.2004.07.019, mass density, 529 points), GLOBlit_11130 (DOI 10.1021/je8001305, compressed liquid mass density, 209 points), GLOBlit_1910 (DOI 10.1016/j.fluid.2016.04.007, surface tension, 60 points), and GLOBlit_2892 (DOI 10.1016/j.jct.2007.12.002, excess molar enthalpy, 45 points). VLE-related measurements are the most commonly reported property type, appearing in at least 8 distinct studies.

**Answer:**

#### Binary Water + Propan-2-ol: Literature Coverage in ThermoML

**System:** water (GLOBcomp_1) + propan-2-ol (GLOBcomp_6), binary

The ThermoML database contains **71 declared binary data blocks** across **38 distinct DOIs** for this system, totaling approximately **2,893 data points**. The properties covered span VLE data (boiling temperature, equilibrium mole fraction, azeotropic temperature and composition), mass density, molar heat capacity (Cp), viscosity, surface tension, speed of sound, refractive index, excess molar enthalpy, electrical conductivity, and vapor pressure.

##### Top 5 Most Comprehensive Studies (by number of distinct properties)

**WM_L1_Q1_Table#1_(Query_L1_Q1_Answer):**

| *row_id* | *Rank* | *GLOBlit ID* | *DOI* | *Blocks* | *Distinct Properties* | *Properties Measured* | *Total Points* |
|---|---|---|---|---|---|---|---|
| WM_L1_Q1_Table#1_Row#1 | 「1」 | 「GLOBlit_1423」 | 「10.1016/j.fluid.2014.02.006」 | 「4」 | 「4」 | 「Boiling temperature, Mole fraction, Azeotropic temperature, Azeotropic composition」 | 「36」 |
| WM_L1_Q1_Table#1_Row#2 | 「2」 | 「GLOBlit_2096」 | 「10.1016/j.fluid.2017.09.010」 | 「3」 | 「3」 | 「Boiling temperature, Mole fraction, Azeotropic composition」 | 「37」 |
| WM_L1_Q1_Table#1_Row#3 | 「3」 | 「GLOBlit_1311」 | 「10.1016/j.fluid.2013.08.007」 | 「2」 | 「2」 | 「Mass density, Molar Cp」 | 「1,248」 |
| WM_L1_Q1_Table#1_Row#4 | 「4」 | 「GLOBlit_1827」 | 「10.1016/j.fluid.2015.11.034」 | 「2」 | 「2」 | 「Boiling temperature, Mole fraction」 | 「28」 |
| WM_L1_Q1_Table#1_Row#5 | 「5」 | 「GLOBlit_2687」 | 「10.1016/j.jct.2006.04.006」 | 「2」 | 「2」 | 「Boiling temperature, Mole fraction」 | 「34」 |

##### Additional Notable Studies (1 property each, but large datasets or unique properties)

**WM_L1_Q1_Table#2_(Query_L1_Q1_Answer):**

| *row_id* | *GLOBlit ID* | *DOI* | *Property* | *Points* |
|---|---|---|---|---|
| WM_L1_Q1_Table#2_Row#1 | 「GLOBlit_2432」 | 「10.1016/j.jct.2004.07.019」 | 「Mass density」 | 「529」 |
| WM_L1_Q1_Table#2_Row#2 | 「GLOBlit_11130」 | 「10.1021/je8001305」 | 「Mass density (compressed liquid)」 | 「209」 |
| WM_L1_Q1_Table#2_Row#3 | 「GLOBlit_1910」 | 「10.1016/j.fluid.2016.04.007」 | 「Surface tension」 | 「60」 |
| WM_L1_Q1_Table#2_Row#4 | 「GLOBlit_378」 | 「10.1016/j.fluid.2006.03.021」 | 「Boiling temperature」 | 「48」 |
| WM_L1_Q1_Table#2_Row#5 | 「GLOBlit_2892」 | 「10.1016/j.jct.2007.12.002」 | 「Excess molar enthalpy」 | 「45」 |

##### Key Observations

- **GLOBlit_1423** is the most property-diverse study, reporting four distinct VLE-related properties (boiling temperature, equilibrium mole fraction, and azeotropic temperature and composition) for the water + propan-2-ol system.
- **GLOBlit_1311** is the most data-rich study overall, with 1,248 data points covering mass density (1,110 pts) and molar heat capacity (138 pts) across multiple temperatures and compositions.
- The database also contains blocks with viscosity, speed of sound, refractive index, electrical conductivity, and vapor pressure data from additional DOIs among the 38 total literature sources, though detailed property assignments for all 71 blocks could not be fully enumerated within the 50-block search limit.
- VLE-related measurements (boiling temperature, equilibrium mole fraction, azeotropic data) are the most commonly reported property type for this system, appearing in at least 8 distinct studies.

**Core claims:**
- The ThermoML database contains 71 declared binary data blocks across 38 distinct DOIs for the water + propan-2-ol system, totaling approximately 2,893 data points.
- Properties covered span VLE data (boiling temperature, equilibrium mole fraction, azeotropic temperature and composition), mass density, molar heat capacity, viscosity, surface tension, speed of sound, refractive index, excess molar enthalpy, electrical conductivity, and vapor pressure.
- GLOBlit_1423 (DOI 10.1016/j.fluid.2014.02.006) is the most property-diverse study, reporting four distinct VLE-related properties: boiling temperature, equilibrium mole fraction, azeotropic temperature, and azeotropic composition.
- GLOBlit_1311 (DOI 10.1016/j.fluid.2013.08.007) is the most data-rich study with 1,248 data points covering mass density (1,110 pts) and molar heat capacity (138 pts).
- VLE-related measurements are the most commonly reported property type for this system, appearing in at least 8 distinct studies.
- Detailed property assignments for all 71 blocks could not be fully enumerated within the 50-block search limit.

*Not stored here: 2 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.

---

**Total:** 3 tool calls  |  1000.2s  |  OK
