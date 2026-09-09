# ThermoML_card_json_to_md_compactors — Architecture

> **Version**: 2.0
> **Diagnostic paths and test workflow reviewed**: 2026-09-09

## Overview

`ThermoML_card_json_to_md_compactors/` converts structured JSON card data from the
[card_databases_storage](../card_databases_storage/ARCHITECTURE.md) into compact, readable
Markdown strings consumed by LLM query agents. The package contains
**11 compactors** organized by card type, a **block-level cross-card
compactor**, a **data-point topology module**, a **card parser** for raw
ThermoML XML/JSON, and a comprehensive **test + validation suite**.

---

## Directory Layout

```
ThermoML_card_json_to_md_compactors/
│
├── _basic_compactors/                 ← Per-card-type compactors
│   ├── component_cards_compactor/
│   │   ├── ccs_compactor.py              CCS INDIV → markdown
│   │   ├── ccs_iddk_compactor.py         CCS ID+DK → markdown
│   │   ├── DEBUG_ccs_indiv.py
│   │   └── DEBUG_ccs_iddk.py
│   │
│   ├── measurement_cards_compactor/
│   │   ├── mtdks_compactor.py            MTDKS INDIV → markdown
│   │   ├── mtdks_iddk_compactor.py       MTDKS ID+DK → markdown (subsection format)
│   │   ├── DEBUG_mtdks_indiv.py
│   │   └── DEBUG_mtdks_iddk.py
│   │
│   ├── property_cards_compactor/
│   │   ├── pcs_compactor.py              PCS INDIV → markdown (dual: summary dict + block compact)
│   │   ├── pcs_iddk_compactor.py         PCS ID+DK → markdown
│   │   ├── DEBUG_pcs_indiv.py
│   │   └── DEBUG_pcs_iddk.py
│   │
│   ├── reference_cards_compactor/
│   │   ├── rms_compactor.py              RMS INDIV → markdown
│   │   └── DEBUG_rms_indiv.py
│   │
│   └── registry_cards_compactor/
│       ├── registry_block_compactor.py   Single block → markdown (PM + RXN)
│       ├── registry_paper_compactor.py   All blocks for a DOI → markdown (PM + RXN)
│       ├── DEBUG_pm_registry.py
│       └── DEBUG_rxn_registry.py
│
├── _cross_cards_compactors/           ← Multi-card cross-reference compactors
│   ├── __init__.py
│   └── block_cards_compactor/
│       ├── __init__.py
│       └── block_compactor.py            Block-level cross-card markdown
│
├── _data_points_compaction_topology/  ← Topological data-point compaction
│   ├── __init__.py
│   └── rdp_topology.py                  Ramer-Douglas-Peucker curve simplification
│
├── _db_access.py                      ← Database access helper
├── DEBUG_json_to_md_compact_output.py  ← Convert separately exported diagnostics JSON
│
├── _entry_by_entry_validator/         ← Test orchestrator + card parser
│   ├── run_all_compactor_tests.py        Direct SQLite sample harness
│   ├── thermoml_card_parser.py           Canonical parser facade
│   └── PARSER_EDGE_CASE_REPORT.md        Historical parser validation report
│
└── ARCHITECTURE.md                    ← This file
```

---

## Compactor API Reference

Card and registry-block rendering functions accept a Python dictionary and
return Markdown; registry-paper functions accept a list of rows.
`pcs_doi_summary()` instead returns a machine-readable dictionary.

> **Historical format examples:** The input structures and Markdown examples
> in this API reference describe an earlier schema. Bare numeric IDs and labels
> such as `lit#`, `comp#`, and `blk#` are incompatible with the current strict
> identifier contract; current output also differs in layout (for example, CCS
> uses a table). Do not copy these examples as current input fixtures. The
> authoritative identifier rules are in
> [id_schema.py](../ThermoML_raw_json_to_card_db_parsers/id_schema.py), with
> compactor payload checks in [strict_contracts.py](strict_contracts.py).
> Generate current JSON/Markdown examples with the SQLite harness below.

### 1. CCS INDIV — `compact_ccs(card) → str`

**Module:** `_basic_compactors/component_cards_compactor/ccs_compactor.py`

**Input:** CCS_INDIV.db `json_data` parsed as dict. Structure:
```
{ key: {doi, lit_num_id, lit_id},
  compounds: [{org_num, comp_num_id, inchi_key, name, formula,
               samples: [{sample_num, source, status,
                          purity_steps: [{purification_methods, analysis_methods,
                                          purity: {mol_fraction, mass_fraction, ...},
                                          impurities: {water_mass_pct, ...}}]}]}] }
```

**Output format:**
```markdown
# CCS | {doi} | lit#{lit_num_id}
## org#{n} comp#{id} — {name} | Sample {s}
- **InChI Key:** XXXXXXXXXXX
- **Source:** supplier
- **Status:** as received
- **Purity:** 99.5 mol% (GC)
- **Purification:** distillation
```

**Helpers:** `_fmt_purity()`, `_summarise_steps()`

**CLI:** `python -m ... input.json [-o output.md]`

---

### 2. CCS ID+DK — `compact_ccs_iddk(card) → str`

**Module:** `_basic_compactors/component_cards_compactor/ccs_iddk_compactor.py`

**Input:** CCS_ID_DK.db `json_data`. Structure:
```
{ comp_num_id, identity: {inchi_key, formula, SMILES, InChI},
  names: {primary_name, all_names[]} }
```

**Output format:**
```markdown
# CCS-ID | comp#{cid} | {primary_name}
- **Formula:** C₂H₆O
- **InChI Key:** LFQSCWFLJHTTHZ-UHFFFAOYSA-N
- **SMILES:** CCO
- **InChI:** InChI=1S/C2H6O/c1-2-3/h3H,2H2,1H3
**Names:** ethanol; ethyl alcohol; … (+N more)
```

**Import-only** (no CLI).

---

### 3. MTDKS INDIV — `compact_mtdks(card) → str`

**Module:** `_basic_compactors/measurement_cards_compactor/mtdks_compactor.py`

**Input:** MTDKS_INDIV.db `json_data`. Structure:
```
{ key: {doi, lit_num_id, lit_id},
  methods_summary: {n_unique_methods, n_standard, n_custom, technique_families},
  methods: [{method_type, method_name, meas_num_id, meas_id, properties, block_numbers, instance_count}] }
```

**Output format:**
```markdown
# MTDKS | {doi} | lit#{lit_num_id}
**Methods:** 3 unique (2 std, 1 custom) | Families: Densimetry, Viscometry

| Type | meas# | meas_id | Method | Properties | Blocks | N |
|------|-------|---------|--------|------------|--------|---|
| std  | 42    | vibrating_tube_method | Vibrating tube | prop#1:mass_density_kg_m3 | 1-5 | 8 |
```

**CLI:** `python -m ... [input.json] [-o output.md]`

---

### 4. MTDKS ID+DK — `compact_mtdks_iddk(card) → str`

**Module:** `_basic_compactors/measurement_cards_compactor/mtdks_iddk_compactor.py`

**Input:** MTDKS_ID_DK.db `json_data`. Structure:
```
{ meas_ID, card_type: "standard_dk"|"custom_stub",
  identity: {name, measurement_family, acronym, aliases[], modality{},
             thermoml_standard_name, thermoml_custom_codes[],
             db_usage: {instance_count, n_papers, property_groups[], per_group{}}},
  domain_knowledge: {structured_block: {measurement_scope, experimental_parameters,
                     setup_and_requirements, performance, data_and_interpretation, uncertainty},
                     description_block: {technique_overview, …, reporting_checklist}} | null }
```

**Output format (standard_dk):**
```markdown
# MTDKS-DK | {meas_ID}
**Name:** Vibrating tube method
**Family:** Densimetry
**ThermoML std:** Vibrating tube method
**Modality:** contact=yes, destructive=no, …
**Usage:** 13,110 instances | 2,683 papers | groups=VolumetricProp
**Per-group:** VolumetricProp: 13,110 inst/2,683 papers

## Structured Knowledge
### measurement_scope
**direct_observables:**
- oscillation period τ of U-tube
…
### experimental_parameters
**constraints:**
- **temperature_range** — typical: 278–363 K — limits: …
…

## Description
### technique_overview
The vibrating tube method is a widely used…
```

**Output format (custom_stub):** Identity section only (5 lines).

**Helpers:** `_fmt_dict_item()` — formats constraint/variable/property dicts; `_fmt_field()` — routes by type (str → inline, list[str] → bullets, list[dict] → formatted bullets, dict → key/value pairs)

**Import-only** (no CLI).

---

### 5. PCS INDIV — Three functions

**Module:** `_basic_compactors/property_cards_compactor/pcs_compactor.py`

#### `pcs_doi_summary(card) → dict`

Returns a **machine-readable dict** (not markdown) summarizing the paper:
```python
{"doi", "lit_num_id", "title", "n_blocks", "total_datapoints",
 "temperature_range_K", "pressure_range_kPa",
 "compounds", "properties", "methods", "system_types", "block_index"}
```

#### `pcs_block_compact(block, key_info=None, compounds_map=None) → str`

Compacts a **single data block** (target < 200 lines):
```markdown
## blk#3 | P/M | binary | 45 pts | lit#7821
**Compounds:** 1=comp#42(ethanol), 2=comp#103(water)
**Properties:**
  prop#1:mass_density_kg_m3 | meas#42:vibrating_tube_method | [VolumetricProp] | ph#1:Liquid
**Variables:** v#1:temperature_K  v#3:mole_fraction @comp1
**Constraints:** c#2:pressure_kpa=101.325

| T(K)   | x_EtOH | ρ(kg/m³) | U(ρ)   |
|--------|--------|----------|--------|
| 298.15 | 0.100  | 981.2    | 0.05   |
```

**Helpers:** `_short_col()` — generates abbreviated column headers; `_build_compounds_map()` — maps org_num to label

#### `compact_pcs(card) → str`

Legacy convenience function combining `pcs_doi_summary()` inline stats + all blocks joined with `---` separators.

**CLI:** `python -m ... [input.json] [-o output.md] [--summary]`

---

### 6. PCS ID+DK — `compact_pcs_iddk(card) → str`

**Module:** `_basic_compactors/property_cards_compactor/pcs_iddk_compactor.py`

**Input:** PCS_ID_DK.db `json_data`. Structure:
```
{ prop_ID, identity: {name, property_group, property_class, unit, symbol, dimension,
                      is_intensive, is_molar, is_excess, …,
                      typical_variables, typical_constraints,
                      db_usage: {total_instances, n_papers, rank_overall, common_methods}},
  domain_knowledge: {structured_block, description_block} }
```

**Output format:**
```markdown
# PCS-DK | {prop_ID}
**Name:** Mass density  **Group:** VolumetricProp  **Unit:** kg/m³
**Symbol:** ρ  **Dimension:** M·L⁻³
**Flags:** intensive
**Variables:** temperature_K (98%), pressure_kPa (45%), …
**Constraints:** pressure_kPa (72%), temperature_K (15%), …
**Usage:** 23,070 instances | 4,891 papers | rank #1
**Top methods:** vibrating_tube_method (0.57), …

## Structured Knowledge
key = value …

## Description
### technique_overview
First 120 chars of prose…
```

**Import-only** (no CLI).

---

### 7. RMS INDIV — `compact_rms(card) → str`

**Module:** `_basic_compactors/reference_cards_compactor/rms_compactor.py`

**Input:** RMS_INDIV.db `json_data`. Structure:
```
{ identity: {doi, lit_num_id, lit_id},
  bibliographic: {title, authors[], journal, year, volume, pages, …},
  content: {abstract, keywords[]},
  data_inventory: {n_compounds, n_blocks, n_datapoints, has_pure_or_mixture_data,
                   has_reaction_data, temperature_range_K, pressure_range_kPa,
                   compound_list, properties, property_groups, system_types} }
```

**Output format:**
```markdown
# RMS | {doi} | lit#{lit_num_id}
## Bibliographic
**Title:** …
**Authors:** Smith; Jones; …
**Journal:** J. Chem. Eng. Data (2015) 60:1234–1240
## Abstract
…
## Data Inventory
| Metric | Value |
|--------|-------|
| Compounds | 3 |
| Blocks | 12 |
| Datapoints | 456 |
| T range (K) | 278–368 |
## Compounds
| org# | comp# | Name | InChI Key | Formula |
## Properties
- prop#1 | mass_density_kg_m3 | Mass density
```

**CLI:** `python -m ... [input.json] [-o output.md]`

---

### 8. Registry Block — `compact_pm_registry(row)` / `compact_rxn_registry(row)` → str

**Module:** `_basic_compactors/registry_cards_compactor/registry_block_compactor.py`

**Input:** Single `dict` from `block_registry` table (column names as keys).
JSON-encoded columns (`comp_ids_smiles`, `var_ids_ranges`, etc.) are parsed
internally via `_parse_json_col()`.

**Output format (PM):**
```markdown
# REG-PM | {doi} | blk#{block_number}
**Type:** PureOrMixtureData | binary | 3 components | 45 pts
**Compounds:** org1=comp#42 ethanol (CCO), org2=comp#103 water (O)
**Solvents:** org3=comp#200 toluene
**Variables:** temperature_K [278, 368]; mole_fraction [0, 1]
**Constraints:** pressure_kpa = 101.325
**Properties:**
- mass_density_kg_m3 | vibrating_tube_method | Mass density [780, 998]
**Phases:** Liquid (ph#1)
```

**Output format (RXN):** Same header style with `# REG-RXN`, plus
`**Reaction:** combustion_with_oxygen` and `**Participants:**` with
stoichiometric coefficients and phase annotations.

**Import-only** (no CLI).

---

### 9. Registry Paper — `compact_pm_paper(rows)` / `compact_rxn_paper(rows)` → str

**Module:** `_basic_compactors/registry_cards_compactor/registry_paper_compactor.py`

**Input:** `list[dict]` — all `block_registry` rows sharing one DOI.

**Output format (PM):**
```markdown
# REG-PM-PAPER | {doi}
**Blocks:** 12  **Total pts:** 456
**Systems:** binary×8; ternary×4
**Compounds:** ethanol (org1), water (org2), …
**Solvents:** toluene
**Variables:** temperature_K; mole_fraction; pressure_kpa
**Constraints:** pressure_kpa
**Properties:**
- mass_density_kg_m3 | vibrating_tube_method | Mass density
- viscosity_pa_s | capillary_tube | Dynamic viscosity
**Phases:** Liquid

**Block detail:**
- blk#1 | binary | 3c | 45pts | mass_density_kg_m3, viscosity_pa_s
- blk#2 | binary | 2c | 30pts | refractive_index
```

**Aggregation pattern:** Uses `Counter` for system type frequency,
`set`/`dict` for variable/constraint/property deduplication.

**Import-only** (no CLI).

---

## Compactor Summary Table

Markdown headers below retain the historical notation described above.

| # | Compactor | Source DB | Input type | Public function(s) | Markdown header |
|---|---|---|---|---|---|
| 1 | CCS INDIV | CCS_INDIV.db | card dict | `compact_ccs` | `# CCS \| {doi}` |
| 2 | CCS ID+DK | CCS_ID_DK.db | card dict | `compact_ccs_iddk` | `# CCS-ID \| comp#{id}` |
| 3 | MTDKS INDIV | MTDKS_INDIV.db | card dict | `compact_mtdks` | `# MTDKS \| {doi}` |
| 4 | MTDKS ID+DK | MTDKS_ID_DK.db | card dict | `compact_mtdks_iddk` | `# MTDKS-DK \| {meas_ID}` |
| 5 | PCS INDIV | PCS_INDIV.db | card dict | `pcs_doi_summary` (dict), `pcs_block_compact` (str), `compact_pcs` (str) | `## blk#{n}` |
| 6 | PCS ID+DK | PCS_ID_DK.db | card dict | `compact_pcs_iddk` | `# PCS-DK \| {prop_ID}` |
| 7 | RMS INDIV | RMS_INDIV.db | card dict | `compact_rms` | `# RMS \| {doi}` |
| 8 | REG Block PM | PureOrMixtureData_registry.db | row dict | `compact_pm_registry` | `# REG-PM \| {doi} \| blk#{n}` |
| 9 | REG Block RXN | ReactionData_registry.db | row dict | `compact_rxn_registry` | `# REG-RXN \| {doi} \| blk#{n}` |
| 10 | REG Paper PM | PureOrMixtureData_registry.db | list[dict] | `compact_pm_paper` | `# REG-PM-PAPER \| {doi}` |
| 11 | REG Paper RXN | ReactionData_registry.db | list[dict] | `compact_rxn_paper` | `# REG-RXN-PAPER \| {doi}` |

---

## Formatting Conventions

### Historical ID notation

The following table records the old display notation only. Current compactors
require typed identifiers defined by
[id_schema.py](../ThermoML_raw_json_to_card_db_parsers/id_schema.py), including
`GLOBlit`, `GLOBcomp`, and `PROPblock` identifiers. These legacy labels are not
valid replacements for that contract:

| Entity | Format | Example |
|---|---|---|
| Paper | `lit#{lit_num_id}` | `lit#7821` |
| Compound | `comp#{comp_num_id}` | `comp#42` |
| Property | `prop#{num}:{prop_id}` | `prop#1:mass_density_kg_m3` |
| Method | `meas#{num}:{meas_id}` | `meas#42:vibrating_tube_method` |
| Variable | `v#{num}:{var_id}` | `v#1:temperature_K` |
| Constraint | `c#{num}:{constr_id}` | `c#2:pressure_kpa` |
| Phase | `ph#{num}:{phase}` | `ph#1:Liquid` |

### Historical Markdown Patterns

- **H1 headers:** `# CARD_TYPE | primary_key | lit#{id}` — one per card
- **H2 headers:** `## section` — major sections (Bibliographic, Structured Knowledge, Description)
- **H3 headers:** `### subsection` — within DK cards (measurement_scope, experimental_parameters, …)
- **Bold keys:** `**Key:** value` — metadata fields
- **Bullets:** `- item` — list entries
- **Tables:** `| col | col |` with `---` separator — data tables and method tables
- **Ranges:** `[min, max]` or `min–max unit`
- **Inline lists:** semicolon-separated

### Historical Truncation Rules

These recorded limits are not a complete current API contract; inspect the
selected compactor and generated examples before relying on exact formatting.

| Context | Limit |
|---|---|
| Compound names (CCS ID+DK) | 10 shown, "+N more" overflow |
| PCS DK description sections | First 120 chars per section |
| InChI Key in tables | Truncated to 20 chars |
| PCS data blocks | max_datapoints_per_block = 50 |
| Custom method names | Prefixed with `[custom:…]` |

---

## Testing Infrastructure

All paths in this section are relative to the repository root unless a different
working directory is stated. These diagnostics run locally against prepared
databases and do not require a model API.

### Direct SQLite compactor harness

[_entry_by_entry_validator/run_all_compactor_tests.py](_entry_by_entry_validator/run_all_compactor_tests.py)
exercises seven card compactors and four registry compactors. From the repository root:

```sh
python ThermoML_research_agent/ThermoML_card_json_to_md_compactors/_entry_by_entry_validator/run_all_compactor_tests.py
```

It reads the current SQLite databases directly; exported diagnostic JSON is not
an input or prerequisite for this harness.

| Source | Selection |
|---|---|
| Seven card databases in `ThermoML_research_agent/card_databases_storage/Individual_cards_dbs/` | Decode `cards.json_data` at first, middle, and last offsets ordered by `rowid`; duplicate offsets are removed for very small databases |
| Additional `MTDKS_ID_DK` examples | Two `registry_stub` extremes by instance count and one seeded random registry stub |
| PM/RXN registry blocks | Two extremes by datapoint/component counts and one seeded random row from `block_registry` |
| PM/RXN registry papers | DOI groups with the most blocks and most total datapoints, plus one seeded random DOI |

Registry inputs are `PureOrMixtureData_registry.db` and `ReactionData_registry.db`
under `ThermoML_research_agent/card_databases_storage/`. Random selections use
`random.seed(42)`; reproducibility also depends on the installed database contents
and row order.

The generated output is:

```text
_output/Query/Diagnostics/compactor_tests/compactor_test_output/
├── CCS_ID_DK/
├── CCS_INDIV/
├── MTDKS_ID_DK/
├── MTDKS_INDIV/
├── PCS_ID_DK/
├── PCS_INDIV/
├── RMS_INDIV/
├── PM_REGISTRY/
├── RXN_REGISTRY/
├── PM_REGISTRY_PAPER/
└── RXN_REGISTRY_PAPER/
```

At startup, the harness clears and recreates only this `compactor_test_output`
directory. Each case writes `{label}.json` with the selected input and
`{label}.md` with its compacted output. The final console tally reports the
actual subdirectory and file counts; counts from older archived runs are not
expected outputs of the current harness. Empty databases, invalid card payloads,
or missing required registry-stub examples cause a failure.

### Exported diagnostic JSON conversion

[DEBUG_json_to_md_compact_output.py](DEBUG_json_to_md_compact_output.py) is a
separate workflow. It reads existing JSON under
`_output/Query/Diagnostics/card_databases/<TYPE>/` for the seven card types,
validates their identifiers, and writes Markdown beside each JSON file.
It also generates `PCS_BLOCK` JSON/Markdown pairs using the block with the most
data points from each exported PCS card.

```sh
python ThermoML_research_agent/ThermoML_card_json_to_md_compactors/DEBUG_json_to_md_compact_output.py
```

This converter expects all seven diagnostic type directories to exist. Its input
is not the SQLite harness's `compactor_test_output` tree; prepare the exported
cards before running it. Existing matching Markdown files are overwritten.

### Per-module diagnostic scripts

Nine `DEBUG_*.py` scripts in `_basic_compactors/` query their matching database
and save paired JSON/Markdown examples under
`_output/Query/Diagnostics/card_databases/<TYPE>/`. They select two edge cases
and one seeded random case; the exact criteria are specified in each script.

| Script | Source database |
|---|---|
| [DEBUG_ccs_iddk.py](_basic_compactors/component_cards_compactor/DEBUG_ccs_iddk.py) | `CCS_ID_DK.db` |
| [DEBUG_ccs_indiv.py](_basic_compactors/component_cards_compactor/DEBUG_ccs_indiv.py) | `CCS_INDIV.db` |
| [DEBUG_mtdks_iddk.py](_basic_compactors/measurement_cards_compactor/DEBUG_mtdks_iddk.py) | `MTDKS_ID_DK.db` |
| [DEBUG_mtdks_indiv.py](_basic_compactors/measurement_cards_compactor/DEBUG_mtdks_indiv.py) | `MTDKS_INDIV.db` |
| [DEBUG_pcs_iddk.py](_basic_compactors/property_cards_compactor/DEBUG_pcs_iddk.py) | `PCS_ID_DK.db` |
| [DEBUG_pcs_indiv.py](_basic_compactors/property_cards_compactor/DEBUG_pcs_indiv.py) | `PCS_INDIV.db` |
| [DEBUG_rms_indiv.py](_basic_compactors/reference_cards_compactor/DEBUG_rms_indiv.py) | `RMS_INDIV.db` |
| [DEBUG_pm_registry.py](_basic_compactors/registry_cards_compactor/DEBUG_pm_registry.py) | `PureOrMixtureData_registry.db` |
| [DEBUG_rxn_registry.py](_basic_compactors/registry_cards_compactor/DEBUG_rxn_registry.py) | `ReactionData_registry.db` |

### Canonical parser facade

[_entry_by_entry_validator/thermoml_card_parser.py](_entry_by_entry_validator/thermoml_card_parser.py)
delegates parsing and validation to
[card_orchestrator.py](../ThermoML_raw_json_to_card_db_parsers/card_orchestrator.py).
It does not implement a second parser or translate legacy identifiers.
`--doi <DOI>` processes one source document; `--edge-cases` or `--check` runs the
canonical edge-case suite. Default outputs follow the orchestrator's
`_output/Query/Diagnostics/card_orchestrator/` directory.

[PARSER_EDGE_CASE_REPORT.md](_entry_by_entry_validator/PARSER_EDGE_CASE_REPORT.md)
is a historical report, not evidence that the current checkout has just passed
validation. Current success and generated-file counts come from a new run.

---

## Data Flow

```
┌──────────────────────────────────────────────────────┐
│                   card_databases_storage/                      │
│                                                        │
│  ┌────────────────┐  ┌────────────┐  ┌──────────────┐ │
│  │ 4 INDIV DBs    │  │ 3 ID+DK DBs│  │ 2 Registry   │ │
│  │ (per-DOI cards)│  │ (per-entity)│  │ DBs (blocks) │ │
│  └───────┬────────┘  └─────┬──────┘  └──────┬───────┘ │
└──────────┼──────────────────┼────────────────┼─────────┘
           │                  │                │
     json.loads()       json.loads()    dict(row)
           │                  │                │
           ▼                  ▼                ▼
┌──────────────────────────────────────────────────────┐
│                 ThermoML_card_json_to_md_compactors/                    │
│                                                        │
│  ┌────────────────────────────────────────────────┐   │
│  │  4 INDIV compactors     3 ID+DK compactors     │   │
│  │  compact_ccs()          compact_ccs_iddk()      │   │
│  │  compact_mtdks()        compact_mtdks_iddk()    │   │
│  │  compact_pcs()          compact_pcs_iddk()      │   │
│  │  compact_rms()                                  │   │
│  └─────────────────────────┬──────────────────────┘   │
│                             │                          │
│  ┌──────────────────────────┼─────────────────────┐   │
│  │  4 Registry compactors                          │   │
│  │  compact_pm_registry()   compact_rxn_registry() │   │
│  │  compact_pm_paper()      compact_rxn_paper()    │   │
│  └─────────────────────────┬──────────────────────┘   │
│                             │                          │
│                             ▼                          │
│                    Markdown strings                     │
│              (consumed by LLM query agents)             │
└────────────────────────────────────────────────────────┘
```

---

## Key Design Decisions

1. **Separate rendering and diagnostics** — Rendering functions consume card
   dictionaries or registry rows. Diagnostic scripts load the source databases
   and write the paired JSON/Markdown artifacts. PCS also exposes a dictionary
   summary for programmatic consumers.

2. **Dual-level PCS** — The property compactor exposes both
   `pcs_doi_summary()` (machine-readable dict for programmatic routing) and
   `pcs_block_compact()` (human-readable markdown per block) to support
   different consumer needs.

3. **Subsection-based DK rendering** — MTDKS ID+DK uses `### section_name`
   headers with type-aware field formatting (`_fmt_field` dispatches on str /
   list[str] / list[dict] / dict) rather than flattening everything to
   single-line `key=[…]` blocks.

4. **Registry at two granularities** — Block-level compactors answer
   "what's in this specific data block?" while paper-level compactors answer
   "what did this paper measure overall?" Both read from the same
   `block_registry` table.

5. **Direct sample testing** — The harness samples first/middle/last card rows
   from SQLite and adds registry extremes and seeded random examples. Individual
   diagnostic scripts provide additional edge-case selection; sample counts
   depend on the current database contents.

6. **Paired output** — Every test writes both the input JSON and the output
   Markdown side-by-side, enabling visual inspection and regression diffing.
