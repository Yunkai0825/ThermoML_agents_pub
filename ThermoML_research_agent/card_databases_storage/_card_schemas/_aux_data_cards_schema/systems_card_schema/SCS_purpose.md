# Systems Card Schema (SCS)

**Purpose**: Canonical registry of chemical systems — unique combinations of compounds studied together. The discovery layer: agents query SCS to answer "what data exists for water + NaCl?" before loading any PCS cards.

**Scope**: One card per unique chemical system (unique sorted set of canonical SMILES). ~44,630 total systems.

---

## Schema File

| File | Cards | Description |
|------|-------|-------------|
| `SCS_systems_card_schema.json` | ~44,630 | One per unique system. Components, data coverage, paper list. |

---

## Card Sections

- **identity**: `system_id` (sorted canonical SMILES joined by `::`), `system_type`, `n_components`
- **components[]**: `comp_num_id` (`GLOBcomp_N`), `SMILES`, `name`, `formula` — sorted by SMILES for canonical ordering
- **data_coverage**: `n_papers`, `n_blocks`, `n_datapoints`, `property_groups{}` (group→count), `property_names[]`, `phases_observed[]`, `temperature_range_K`, `pressure_range_kPa`
- **papers[]**: DOIs sorted by n_blocks desc, with property_groups per paper. Truncated to top 20 for heavily-studied systems.

---

## Data Structure Diagram

### SCS Card Anatomy

```
┌─────────────────────────────────────────────────────────────────┐
│  SCS Card: "CCO::O"   (ethanol + water)                        │
├─────────────────────────────────────────────────────────────────┤
│  identity                                                       │
│    system_id:      "CCO::O"                                     │
│    system_type:    "binary"                                     │
│    n_components:   2                                            │
├─────────────────────────────────────────────────────────────────┤
│  components[]                                                   │
│    ┌──────────┬───────────┬───────────┬─────────┐               │
│    │ global ID  │ SMILES  │ name      │ formula │               │
│    ├──────────┼───────────┼───────────┼─────────┤               │
│    │ GLOBcomp_2 │ CCO     │ ethanol   │ C2H6O   │───→ CCS      │
│    │ GLOBcomp_1 │ O       │ water     │ H2O     │───→ CCS      │
│    └──────────┴───────────┴───────────┴─────────┘               │
├─────────────────────────────────────────────────────────────────┤
│  data_coverage                                                  │
│    n_papers:          73                                        │
│    n_blocks:          126                                       │
│    n_datapoints:      1,847                                     │
│    property_groups:   {VolumetricProp: 38, TransportProp: 22,   │
│                        RefractionSurface...: 19, ...}           │
│    property_names:    ["Mass density, kg/m3", ...]              │
│    phases_observed:   ["Liquid", "Crystal"]                     │
│    temperature_range_K:  {min: 273.15, max: 473.15}            │
│    pressure_range_kPa:  {min: 101.3, max: 5000}                │
├─────────────────────────────────────────────────────────────────┤
│  papers[]                                                       │
│    ┌────────────────────┬──────────┬───────────────────────┐    │
│    │ doi                │ n_blocks │ property_groups        │    │
│    ├────────────────────┼──────────┼───────────────────────┤    │
│    │ 10.1021/je050342f  │ 4        │ [VolumetricProp, ...]│───→ RMS
│    │ 10.1016/j.jct...   │ 3        │ [TransportProp]      │───→ RMS
│    │ ...                │          │                       │    │
│    └────────────────────┴──────────┴───────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

### How SCS Maps to Original ThermoML Data

```
   ORIGINAL ThermoML JSON                     SCS CARD
   (one file per paper)                       (one card per system)
  ┌──────────────────────────┐
  │ paper_A.json             │
  │  Citation: {sDOI: "A"}   │               ┌──────────────────────┐
  │  Compound: [{water},     │──┐            │ SCS: "CCO::O"        │
  │             {ethanol}]   │  │            │                      │
  │  PureOrMixtureData:      │  │  ┌──────→ │ components:           │
  │   [Block 1: water+EtOH  │──┼──┘        │   GLOBcomp_2: CCO    │
  │      Property: density   │  │           │   GLOBcomp_1: O      │
  │      NumValues: [...]    │  │           │                      │
  │    Block 2: water+EtOH  │──┼─────────→ │ data_coverage:        │
  │      Property: viscosity │  │           │   n_papers: 73       │
  │      NumValues: [...]]   │  │           │   n_blocks: 126      │
  └──────────────────────────┘  │           │   n_datapoints: 1847 │
                                │  AGGREGATE│   property_groups:    │
  ┌──────────────────────────┐  │  ───────→ │     {Volumetric: 38, │
  │ paper_B.json             │  │           │      Transport: 22}  │
  │  Citation: {sDOI: "B"}   │  │           │   property_names: ...│
  │  Compound: [{ethanol},   │──┤           │                      │
  │             {water}]     │  │           │ papers:               │
  │  PureOrMixtureData:      │  │  ┌─────→ │   [{doi:"A",blocks:2}│
  │   [Block 1: EtOH+water  │──┼──┘       │    {doi:"B",blocks:1}│
  │      Property: density   │  │           │    ...]              │
  │      NumValues: [...]]   │  │           └──────────────────────┘
  └──────────────────────────┘  │
                                │
  ┌──────────────────────────┐  │
  │ paper_C.json  ...        │──┘
  └──────────────────────────┘
       73 papers total
       with water+ethanol blocks
```

### Key Derivation Rules

```
  ThermoML field                        SCS field
  ─────────────────────────────────     ──────────────────────
  Compound[].sStandardInChI         →   SMILES (via RDKit)
                                        system_id (sorted, joined by ::)
  Compound[].sCommonName[0]         →   components[].name
  Compound[].sFormulaMolec          →   components[].formula
  (assigned in sort order)          →   components[].comp_id

  COUNT(DISTINCT sDOI)              →   data_coverage.n_papers
  COUNT(blocks with this system)    →   data_coverage.n_blocks
  SUM(len(NumValues[]))             →   data_coverage.n_datapoints
  COLLECT(PropertyGroup names)      →   data_coverage.property_groups
  COLLECT(DISTINCT ePropName)       →   data_coverage.property_names
  COLLECT(DISTINCT ePropPhase)      →   data_coverage.phases_observed
  MIN/MAX(Temperature variables)    →   data_coverage.temperature_range_K
  MIN/MAX(Pressure variables)       →   data_coverage.pressure_range_kPa

  GROUP BY doi                      →   papers[].doi, n_blocks, property_groups
```

### Cross-Card Navigation

```
                     ┌──────────┐
                     │   SCS    │  "What systems have density data?"
                     │  44,630  │  "What's measured for ethanol+water?"
                     │  cards   │
                     └────┬─────┘
                          │
           ┌──────────────┼──────────────┐
           │              │              │
           ▼              ▼              ▼
     ┌──────────┐  ┌──────────┐   ┌──────────┐
     │   CDS    │  │   PCS    │   │   RMS    │
     │  8,502   │  │ ~130,104 │   │ 11,923   │
     │compounds │  │  cards   │   │ papers   │
     └──────────┘  └──────────┘   └──────────┘
     comp_id/SMILES  block data     full citation
     names, formula  actual values  authors, year
     purity/sample   uncertainties  abstract, DOI

  SCS.components[].SMILES  ───→  CDS lookup (compound details)
  SCS.papers[].doi         ───→  RMS lookup (full citation)
  SCS.data_coverage        ───→  PCS filter  (which cards to load)
```

---

## Database Statistics (full scan: 11,923 files)

| System Type | Unique Systems | Blocks |
|------------|---------------|--------|
| Unary | 8,502 | 45,821 |
| Binary | 28,982 | 58,292 |
| Ternary | 7,102 | 18,324 |
| Quaternary+ | 44 | 44 |
| **Total** | **44,630** | **122,481** |

- Systems with multiple papers: 7,105 (16%)
- Systems with 1 paper: 37,525 (84%)
- Systems with >10 papers: ~540 (1.2%)
- Top system: NaCl + water — 192 blocks, 125 papers, 2,428 data points, 23 property names
- SMILES derived from InChI via RDKit; 61 compounds (57 files) missing InChI will lack SMILES

---

## Token Budget

| Card Type | Typical | Heavy (NaCl+water) |
|-----------|---------|---------------------|
| Unary (1 paper) | ~200 tokens | — |
| Binary (3 papers) | ~360 tokens | ~1,600 tokens |
| Ternary | ~400-600 tokens | — |

---

## What is NOT Here

Actual data points, measurement details, purity data. Those belong to PCS. Full citation details belong to RMS. Compound identity/purity details belong to CDS.

## Agent Use

System discovery, property coverage lookup, "what's been measured for X+Y?" queries, filtering candidates before loading full PCS cards.
