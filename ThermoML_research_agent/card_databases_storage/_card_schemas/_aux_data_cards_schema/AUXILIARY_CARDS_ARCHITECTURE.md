# Auxiliary Card Schemas — Architecture Documentation

> **Version**: 1.0.0  
> **Covers**: Systems Card Schema (SCS), Utility Summary Schema (USS)  
> **Role**: Discovery and orientation layers that sit above the four core schemas (PCS, CCS, RMS, MTDKS)

---

## Part 1: Systems Card Schema (SCS)

### 1.1 Overview

**Purpose**: The SCS is the **discovery layer** of the ThermoML agentic system. It answers the question: *"What data exists for this chemical system?"*

A **system** is a unique combination of compounds studied together — for example, ethanol + water is one system regardless of which paper measured it. Every `PureOrMixtureData` block in ThermoML maps to exactly one system; the SCS aggregates statistics across all papers that studied the same system.

| Statistic | Value |
|-----------|-------|
| Total unique systems | **44,630** |
| Systems with 1 paper | 37,525 (84%) |
| Systems with multiple papers | 7,105 (16%) |
| Systems with >10 papers | ~540 (1.2%) |
| Source blocks aggregated | 122,481 |
| Source data points aggregated | ~2,690,357 |

The SCS is **not** where actual measurement data lives — it is a precomputed index. Agents read SCS cards to decide *which* PCS cards to load, avoiding the cost of scanning the full dataset.

### 1.2 Card Structure

Each SCS card has four top-level sections:

```
SCS Card
├── identity          # What system is this?
├── components[]      # Which compounds?
├── data_coverage     # How much data, what properties, what ranges?
└── papers[]          # Which papers studied it? (top 20)
```

#### 1.2.1 `identity`

| Field | Type | Description |
|-------|------|-------------|
| `system_id` | string | **Primary key.** Sorted canonical SMILES joined by `::`. Example: `"CCO::O"` |
| `system_type` | string | One of: `"unary"`, `"binary"`, `"ternary"`, `"quaternary+"` |
| `n_components` | integer | Number of distinct compounds (1, 2, 3, …) |

#### 1.2.2 `components[]`

Array of compounds, **sorted by SMILES** for canonical ordering.

| Field | Type | Description |
|-------|------|-------------|
| `comp_num_id` | string | Global compound registry ID: `GLOBcomp_N` |
| `SMILES` | string | Canonical SMILES (RDKit-derived from InChI). **CCS lookup key.** |
| `name` | string | Most common name across all papers studying this system |
| `formula` | string | Molecular formula (`sFormulaMolec`) |

#### 1.2.3 `data_coverage`

Precomputed aggregates across **all** papers and blocks for this system. This is the primary discovery section — agents read it to decide whether the system has relevant data.

| Field | Type | Description |
|-------|------|-------------|
| `n_papers` | integer | Distinct DOIs that studied this system |
| `n_blocks` | integer | Total measurement blocks across all papers |
| `n_datapoints` | integer | Total data points across all blocks |
| `property_groups` | object | Map of `PropertyGroup → count`. E.g. `{"VolumetricProp": 42, "TransportProp": 18}` |
| `property_names` | string[] | All distinct property names (`ePropName`) measured |
| `phases_observed` | string[] | All distinct phases (`ePropPhase`) observed |
| `temperature_range_K` | object\|null | `{min, max}` across all data points and constraints |
| `pressure_range_kPa` | object\|null | `{min, max}` across all data points and constraints |

#### 1.2.4 `papers[]`

Array of papers that studied this system, **sorted by `n_blocks` descending** (most data first).

| Field | Type | Description |
|-------|------|-------------|
| `doi` | string | Paper DOI — key to RMS for full citation |
| `n_blocks` | integer | Measurement blocks from this paper for this system |
| `property_groups` | string[] | Which property groups this paper measured |

> **Truncation rule**: When `n_papers > 20`, only the top 20 papers (by block count) are included. This affects ~0.4% of systems. The true count is always available in `data_coverage.n_papers`.

### 1.3 System ID Construction

The `system_id` is the canonical primary key. Construction:

1. Collect all `Compound[].sStandardInChI` from the block
2. Convert each InChI to canonical SMILES via RDKit
3. **Sort** the SMILES alphabetically
4. **Join** with `::` separator

```
Examples:
  Pure system:    "CCO"                        (ethanol)
  Binary system:  "CCO::O"                     (ethanol + water)
  Ternary system: "CCO::O::[Na+].[Cl-]"       (ethanol + water + NaCl)
```

This ensures the same system always produces the same ID regardless of the order compounds appear in the original XML. Sorting is critical: paper A listing `{water, ethanol}` and paper B listing `{ethanol, water}` both resolve to `"CCO::O"`.

**Edge case**: 61 compounds (across 57 files) lack InChI and will therefore lack SMILES. These are excluded from system ID generation.

### 1.4 Derivation from ThermoML Source

```
  ThermoML field                          SCS field
  ──────────────────────────────────      ─────────────────────────────────
  Compound[].sStandardInChI           →   SMILES (via RDKit)
                                          system_id (sorted, joined by ::)
  Compound[].sCommonName[0]           →   components[].name
  Compound[].sFormulaMolec            →   components[].formula
  (assigned in SMILES sort order)     →   components[].comp_id

  COUNT(DISTINCT sDOI)                →   data_coverage.n_papers
  COUNT(blocks with this system)      →   data_coverage.n_blocks
  SUM(len(NumValues[]))               →   data_coverage.n_datapoints
  COLLECT(PropertyGroup names)        →   data_coverage.property_groups
  COLLECT(DISTINCT ePropName)         →   data_coverage.property_names
  COLLECT(DISTINCT ePropPhase)        →   data_coverage.phases_observed
  MIN/MAX(Temperature vars/constr.)   →   data_coverage.temperature_range_K
  MIN/MAX(Pressure vars/constr.)      →   data_coverage.pressure_range_kPa

  GROUP BY doi                        →   papers[].doi, n_blocks, property_groups
```

### 1.5 Cross-Card References

SCS cards connect to three core schemas:

```
  SCS.components[].SMILES   ──→  CCS lookup   (compound identity, names, purity)
  SCS.papers[].doi           ──→  RMS lookup   (full citation, authors, abstract)
  SCS.data_coverage          ──→  PCS filter   (decide which property cards to load)
```

Detailed navigation:

| From SCS field | To Schema | Lookup key | You get |
|----------------|-----------|------------|---------|
| `components[].SMILES` | CCS (Tier 1) | SMILES / InChIKey | Full compound identity, all names, substance type |
| `components[].SMILES` + `papers[].doi` | CCS (Tier 2) | DOI + InChIKey + sample_num | Per-paper sample source, purity, purification |
| `papers[].doi` | RMS | DOI | Title, authors, journal, year, abstract, keywords |
| `data_coverage.property_names` | PCS (Tier 1) | prop_ID (slugified name) | Domain knowledge for each property |
| `papers[].doi` | PCS (Tier 2) | DOI | Actual measurement blocks and data points |

### 1.6 Agent Usage Patterns

**Pattern 1: System lookup**
> "What properties have been measured for water + ethanol?"

```
1. Build system_id: sort(["O", "CCO"]) → "CCO::O"
2. Load SCS card for "CCO::O"
3. Read data_coverage.property_names → list of all measured properties
4. Read data_coverage.property_groups → distribution by group
5. Read data_coverage.temperature_range_K, pressure_range_kPa → condition ranges
```

**Pattern 2: Paper discovery**
> "Which papers measured density for the NaCl + water system?"

```
1. Build system_id: "[Na+].[Cl-]::O"
2. Load SCS card → papers[] (top 20 by block count)
3. Filter papers where property_groups includes "VolumetricProp"
4. Load RMS cards for matching DOIs → full citations
```

**Pattern 3: Coverage assessment**
> "Is there enough viscosity data for ethanol + water to fit a model?"

```
1. Load SCS card for "CCO::O"
2. Check data_coverage: n_datapoints, temperature_range_K
3. Check if "Dynamic viscosity, Pa*s" in property_names
4. If promising → load PCS cards for actual data
```

**Note**: The `papers[]` list is truncated to 20 for heavily-studied systems. When exhaustive paper coverage is needed, use RMS search by compound instead.

### 1.7 Statistics

#### Distribution by System Type

| System Type | Unique Systems | Blocks | % of Systems |
|-------------|---------------|--------|-------------|
| Unary | 8,502 | 45,821 | 19.1% |
| Binary | 28,982 | 58,292 | 64.9% |
| Ternary | 7,102 | 18,324 | 15.9% |
| Quaternary+ | 44 | 44 | 0.1% |
| **Total** | **44,630** | **122,481** | **100%** |

#### Top Systems by Block Count

| System | Blocks | Papers | Datapoints | Properties |
|--------|--------|--------|------------|------------|
| NaCl + water | 192 | 125 | 2,428 | 23 |
| ethanol + water | 126 | 73 | 1,847 | — |
| KCl + water | 124 | 91 | — | — |
| glycine + water | 124 | 79 | — | — |
| D-glucose + water | 94 | 48 | — | — |

#### Token Budget

| Card Profile | Typical Tokens |
|-------------|----------------|
| Unary, 1 paper | ~200 |
| Binary, 3 papers | ~360 |
| Ternary, typical | ~400–600 |
| Heavy system (NaCl+water, 20 papers listed) | ~1,600 |

### 1.8 SCS Card Anatomy (ASCII)

```
┌──────────────────────────────────────────────────────────────────┐
│  SCS Card: "CCO::O"   (ethanol + water)                         │
├──────────────────────────────────────────────────────────────────┤
│  identity                                                        │
│    system_id:      "CCO::O"                                      │
│    system_type:    "binary"                                      │
│    n_components:   2                                             │
├──────────────────────────────────────────────────────────────────┤
│  components[]                                                    │
│    ┌──────────┬───────────┬───────────┬─────────┐                │
│    │ global ID  │ SMILES  │ name      │ formula │                │
│    ├──────────┼───────────┼───────────┼─────────┤                │
│    │ GLOBcomp_2 │ CCO     │ ethanol   │ C2H6O   │──→ CCS        │
│    │ GLOBcomp_1 │ O       │ water     │ H2O     │──→ CCS        │
│    └──────────┴───────────┴───────────┴─────────┘                │
├──────────────────────────────────────────────────────────────────┤
│  data_coverage                                                   │
│    n_papers:          73                                         │
│    n_blocks:          126                                        │
│    n_datapoints:      1,847                                      │
│    property_groups:   {VolumetricProp: 38, TransportProp: 22,    │
│                        RefractionSurfaceTensionUltrasound: 19}   │
│    property_names:    ["Mass density, kg/m3", ...]               │
│    phases_observed:   ["Liquid", "Crystal"]                      │
│    temperature_range_K:  {min: 273.15, max: 473.15}             │
│    pressure_range_kPa:   {min: 101.3,  max: 5000}               │
├──────────────────────────────────────────────────────────────────┤
│  papers[]  (top 20 of 73)                                        │
│    ┌───────────────────────┬──────────┬────────────────────────┐ │
│    │ doi                   │ n_blocks │ property_groups         │ │
│    ├───────────────────────┼──────────┼────────────────────────┤ │
│    │ 10.1021/je050342f     │ 4        │ [VolumetricProp, ...]  │→RMS
│    │ 10.1016/j.jct.2007…  │ 3        │ [TransportProp]        │→RMS
│    │ …                     │          │                        │ │
│    └───────────────────────┴──────────┴────────────────────────┘ │
└──────────────────────────────────────────────────────────────────┘
```

### 1.9 What is NOT in SCS

| Data type | Where it lives |
|-----------|---------------|
| Actual data points and values | PCS (Tier 2 — INDIV snapshots) |
| Measurement method details | MTDKS |
| Compound purity and sample prep | CCS (Tier 2 — sample cards) |
| Full citation, authors, abstract | RMS |
| Domain knowledge for properties | PCS (Tier 1 — ID & DK cards) |

---

## Part 2: Utility Summary Schema (USS)

### 2.1 Overview

**Purpose**: The USS is the agent's **"table of contents"** — a compact global summary of the entire ThermoML database. It is the **first thing** an agent reads to orient itself before making any targeted queries.

Unlike SCS (one card per system) or PCS (one card per property per paper), USS is a **single summary artifact** covering the entire database. It provides database-wide aggregates, distributions, and quick-lookup indexes that allow an agent to scope queries efficiently.

**Role in context-window management**: By reading the USS first (~500–800 tokens), an agent can determine whether a question is answerable at all, which schemas to query, and roughly how much data to expect — before spending tokens on individual cards.

### 2.2 Card Structure

The USS contains the following sections:

#### 2.2.1 Database Overview

Global counts for the entire ThermoML archive:

| Field | Value | Description |
|-------|-------|-------------|
| `total_papers` | 11,923 | Distinct DOIs in the database |
| `total_unique_compounds` | ~8,517 | By InChI deduplication |
| `total_compound_names` | ~22,587 | Including all aliases |
| `total_measurement_blocks` | 123,727 | 122,481 PureOrMixture + 1,246 Reaction |
| `total_datapoints` | ~2,700,000 | Across all blocks |
| `doi_prefixes` | 10.1016, 10.1021, 10.1063 | Elsevier, ACS, AIP |

#### 2.2.2 System Distribution

Blocks by system complexity:

| System type | Blocks |
|------------|--------|
| Unary | ~46,000 |
| Binary | ~58,000 |
| Ternary | ~18,000 |
| Quaternary+ | ~1,000 |
| **Unique deduplicated systems** | **~44,630** |

#### 2.2.3 Property Coverage

| Field | Description |
|-------|-------------|
| `property_groups` | 13 PropertyGroups (11 PureOrMixture + 2 Reaction) |
| `distinct_property_names` | 105 observed in data (of 188 defined in the ThermoML XSD) |
| `per_group_block_counts` | Block count per PropertyGroup |
| `per_group_datapoint_counts` | Datapoint count per PropertyGroup |
| `top_N_properties` | Most frequently measured properties |

#### 2.2.4 Phase Coverage

| Phase | Approximate blocks |
|-------|--------------------|
| Liquid | ~59,000 |
| Liquid + Gas (VLE) | ~19,000 |
| Liquid + Crystal (SLE) | ~12,000 |
| LLE | ~5,600 + ~2,700 |
| Crystal, Gas, Fluid, Solution, Glass | represented |

#### 2.2.5 Temporal Coverage

Publication year range and distribution across the database (2003–2019).

#### 2.2.6 Quick Lookup Indexes

Pre-built indexes for common agent queries:

| Index | Maps | Usage |
|-------|------|-------|
| PropertyGroup → property names → block counts | Group name → list of properties | "What transport properties exist?" |
| Compound name → compound_id | Common name → InChIKey/SMILES | "Find ethanol" → CCS lookup key |
| Common system shortcuts | Informal name → system_id | "water+ethanol" → `"CCO::O"` |

### 2.3 Agent Usage Patterns

**Pattern 1: Orientation**
> "How much vapor-liquid equilibrium data exists in the database?"

```
1. Agent reads USS
2. Checks phase_coverage: Liquid+Gas VLE → ~19,000 blocks
3. Checks property_groups: CompositionAtPhaseEquilibrium → block count
4. Agent can now answer without loading any individual cards
```

**Pattern 2: Feasibility check**
> "Can I build a viscosity model for ionic liquids?"

```
1. Agent reads USS → TransportProp group has X blocks
2. USS doesn't tell about ionic liquids specifically → need SCS
3. Agent searches SCS for systems containing ionic liquid SMILES
4. Checks data_coverage.property_names for viscosity
```

**Pattern 3: Schema navigation**
> "Where do I find purity data for a compound?"

```
1. Agent reads USS → oriented on the schema hierarchy
2. USS points to CCS (Tier 2) for sample/purity data
3. Agent loads CCS sample card keyed by {doi, InChIKey, sample_num}
```

### 2.4 What is NOT in USS

USS does **not** contain per-system, per-paper, or per-compound details. It is strictly aggregate. For specific systems, use SCS. For specific compounds, use CCS. For specific papers, use RMS.

---

## Part 3: Auxiliary vs Core Cards

### 3.1 The Six Schemas

The ThermoML agentic system has **six schemas** organized in two tiers:

| Tier | Schema | Abbr | Cards | Granularity |
|------|--------|------|-------|-------------|
| **Auxiliary** | Utility Summary Schema | USS | 1 | Entire database |
| **Auxiliary** | Systems Card Schema | SCS | ~44,630 | One per unique system |
| **Core** | Property Card Schema | PCS | ~130,104 | One per property per paper (Tier 2) + 105 DK cards (Tier 1) |
| **Core** | Component Card Schema | CCS | ~8,502 identity + ~58,814 sample | One per compound + one per compound per paper |
| **Core** | Reference Metadata Schema | RMS | 11,726 | One per paper |
| **Core** | MeasTech Domain Knowledge Schema | MTDKS | per technique | Reference knowledge for measurement methods |

### 3.2 Read Hierarchy

Agents follow a **top-down** reading pattern to minimize context-window usage:

```
  Level 0 — ORIENTATION (read first, always)
  ┌─────────────────────────────────────────────────────────────┐
  │                         USS                                  │
  │  "Table of contents" for the entire database                 │
  │  Global stats, property/phase coverage, lookup indexes       │
  │  Token cost: ~500–800                                        │
  └──────────────────────────┬──────────────────────────────────┘
                             │
                             ▼
  Level 1 — DISCOVERY (read to scope and plan)
  ┌──────────────────────────┬──────────────────────────────────┐
  │          SCS             │              RMS                  │
  │  "What data exists       │  "What papers exist              │
  │   for this system?"      │   and what do they cover?"       │
  │  ~200–1,600 tok/card     │  ~300–600 tok/card               │
  └─────────────┬────────────┴──────────────┬───────────────────┘
                │                           │
                ▼                           ▼
  Level 2 — DATA ACCESS (read for actual values and knowledge)
  ┌──────────────────┬──────────────────┬───────────────────────┐
  │       PCS        │       CCS        │       MTDKS           │
  │  Property data   │  Compound info   │  Measurement method   │
  │  & domain know.  │  & sample purity │  domain knowledge     │
  │  Tier 1: DK      │  Tier 1: ID      │                       │
  │  Tier 2: data    │  Tier 2: sample   │                       │
  └──────────────────┴──────────────────┴───────────────────────┘
```

### 3.3 Information Flow Diagram

```
  ┌──────────────────────────────────────────────────────────────────────┐
  │                                                                      │
  │   USS (1 card)                                                       │
  │   ├── total_papers: 11,923                                           │
  │   ├── total_compounds: ~8,517                                        │
  │   ├── total_blocks: 123,727                                          │
  │   ├── property_groups: 13 groups, 105 properties                     │
  │   └── quick_lookup_indexes                                           │
  │         │                                                            │
  │         │  "What systems have density data for ethanol + water?"      │
  │         ▼                                                            │
  │   SCS (~44,630 cards)                                                │
  │   ├── system_id: "CCO::O"                                           │
  │   ├── components[]: SMILES, name, formula                            │
  │   ├── data_coverage: 73 papers, 126 blocks, 1847 pts                │
  │   │     ├── property_groups: {VolumetricProp: 38, ...}               │
  │   │     ├── property_names: ["Mass density, kg/m3", ...]             │
  │   │     └── temperature_range_K: {min: 273, max: 473}               │
  │   └── papers[]: top 20 DOIs with block counts                        │
  │         │           │            │                                   │
  │         │           │            │                                   │
  │    ┌────┘      ┌────┘       ┌────┘                                   │
  │    ▼           ▼            ▼                                        │
  │   CCS         PCS          RMS                                       │
  │  (SMILES)   (DOI)        (DOI)                                       │
  │  compound   property      full citation                              │
  │  identity   data &        authors, year                              │
  │  + purity   domain know.  abstract, kw                               │
  │                  │                                                   │
  │                  ▼                                                   │
  │               MTDKS                                                  │
  │             measurement                                              │
  │             technique DK                                             │
  └──────────────────────────────────────────────────────────────────────┘
```

### 3.4 Cross-Reference Map

```
  USS ──────────────────────────────────────────────────────────────
   │   (global stats scope query)
   │
   ├──→ SCS ──→ CCS    via components[].SMILES
   │     │
   │     ├──→ RMS      via papers[].doi
   │     │
   │     └──→ PCS      via data_coverage (filter), papers[].doi (load)
   │
   ├──→ RMS             via DOI prefix distribution
   │     │
   │     └──→ CCS      via data_inventory.compound_list[].SMILES
   │     └──→ PCS      via DOI (load all property cards for a paper)
   │
   └──→ PCS (Tier 1)   via property_groups → prop_ID
         │
         └──→ MTDKS    via PCS DK card's measurement method references
```

### 3.5 Auxiliary vs Core: Design Rationale

| Aspect | Auxiliary (USS, SCS) | Core (PCS, CCS, RMS, MTDKS) |
|--------|---------------------|------------------------------|
| **Purpose** | Discovery and orientation | Data access and domain knowledge |
| **Granularity** | Database-wide or system-level | Per-paper, per-compound, per-property |
| **When read** | First (every query) | On demand (after discovery) |
| **Contains data points** | No — only counts and ranges | Yes (PCS Tier 2 has all values) |
| **Token cost** | Low (~200–1,600 per card) | Variable (~120–4,000+ per card) |
| **Update frequency** | When new papers added | When new papers added |
| **Duplication** | Aggregates from core cards | Authoritative source |

### 3.6 Typical Agent Workflow

```
  Step 1:  Read USS
           → "Is my question answerable? How much data exists?"
           → Decide which schemas to query next

  Step 2:  Read SCS for the target system(s)
           → "What properties are measured? How many papers? Condition ranges?"
           → Decide which DOIs / property groups to load

  Step 3:  (Optional) Read RMS for relevant papers
           → "Who measured this? Published when? What was the study about?"

  Step 4:  Read PCS Tier 1 (ID & DK) for the target property
           → "What does this property mean? Typical ranges? Quality indicators?"

  Step 5:  Read PCS Tier 2 (INDIV snapshots) for specific DOIs
           → "Give me the actual data points with uncertainties"

  Step 6:  (Optional) Read CCS for compound purity
           → "What was the sample purity? How was it purified?"

  Step 7:  (Optional) Read MTDKS for measurement technique knowledge
           → "What method was used? What are its limitations?"
```

---

## Appendix: Schema File Inventory

| Path | Schema | Description |
|------|--------|-------------|
| `_aux_data_cards/systems_card_schema/SCS_systems_card_schema.json` | SCS | Systems card JSON schema |
| `_aux_data_cards/systems_card_schema/SCS_purpose.md` | SCS | Purpose and design notes |
| `_aux_data_cards/_untility_summary_schema/USS_purpose.md` | USS | Purpose and design notes |
| `_core_data_cards/Property_Card_Schema/PCS_property_ID_and_DK_schema.json` | PCS Tier 1 | Property domain knowledge schema |
| `_core_data_cards/Property_Card_Schema/PCS_property_INDIV_snapshot_schema.json` | PCS Tier 2 | Property data snapshot schema |
| `_core_data_cards/Component_Card_Schema/CCS_compound_ID_and_DK_schema.json` | CCS Tier 1 | Compound identity schema |
| `_core_data_cards/Component_Card_Schema/CCS_compound_INDIV_sample_prep_schema.json` | CCS Tier 2 | Compound sample/purity schema |
| `_core_data_cards/Reference_Metadata_Schema/RMS_reference_metadata_schema.json` | RMS | Reference metadata schema |
| `_core_data_cards/MeasTech_DomainKnowledge_Schema/MTDKS_meas_ID_and_DK_schema.json` | MTDKS | Measurement technique schema |
