# MTDKS Architecture — Measurement Technique Domain Knowledge Schema

> **Version:** 4.0.0 | **Scope:** ThermoML agentic system
> **Card family:** `MeasTech_DomainKnowledge_Schema` (MTDKS)
> **Database:** 11,923 papers · 130,104 block-property instances

---

## 1. Overview

### 1.1 Purpose

The MTDKS is the **instrumentation textbook** of the ThermoML card system. It encodes
*what measurement techniques exist*, *how they work*, and *which papers used them*. An
agent consulting MTDKS can:

- **Understand** the physical principle behind a technique name (e.g. "Vibrating tube
  method" ⟶ oscillation-period densimetry).
- **Evaluate** whether a technique is appropriate for a given property, phase, or sample
  type.
- **Assess** data quality by reading uncertainty models, failure modes, and limitations.
- **Discover** which papers used a technique and at what scale.

MTDKS is **not** individual measurement data — that lives in the PCS INDIV cards. MTDKS
is reference material the agent consults to *interpret* and *contextualize* data.

### 1.2 Two-Tier Design

```
┌─────────────────────────────────────────────────────────────────────┐
│                          MTDKS                                      │
│                                                                     │
│  ┌──────────────────────────────┐  ┌─────────────────────────────┐  │
│  │  TIER 1: ID & DK Cards      │  │  TIER 2: INDIV Cards        │  │
│  │  (per-technique)             │  │  (per-DOI)                  │  │
│  │                              │  │                             │  │
│  │  • 1 card per technique      │  │  • 1 card per paper         │  │
│  │  • Keyed by meas_ID          │  │  • Keyed by doi + lit_id    │  │
│  │  • Identity + classification │  │  • Which methods used       │  │
│  │  • Domain knowledge (DK)     │  │  • Which blocks used them   │  │
│  │  • DB usage statistics       │  │  • Instance counts          │  │
│  │  • ~160 cards in 16 folders  │  │  • 11,923 cards             │  │
│  └──────────────────────────────┘  └─────────────────────────────┘  │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │  GLOBAL INDEX: MTDKS_meas_summary.json                       │   │
│  │  Catalog of all 160 standard + 97 custom code techniques     │   │
│  │  Organized by 12 property groups and 16 technique families   │   │
│  └──────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

**Tier 1 — Technique ID & Domain Knowledge** (`Meas_ID_and_DK_cards/*.json`):
Static knowledge cards, one per measurement technique. Contain identity fields, domain
knowledge (physical principle, observables, setup, performance, uncertainty), and DB usage
statistics. These are the "encyclopedia entries."

**Tier 2 — INDIV Method Usage** (stored in `card_databases_storage/Individual_cards_dbs/MTDKS_INDIV.db`; diagnostic exports under workspace-root `_output/Query/Diagnostics/card_orchestrator/<doi>/mtdks_card.json`):
Per-paper cards recording which measurement techniques were used in that paper, which
property groups and blocks they served, and instance counts. These are the "lab notebook
indexes."

### 1.3 How Agents Use MTDKS

```
Agent receives query: "Find high-accuracy density data for ionic liquids"
  │
  ├─ 1. Consult PCS ID_and_DK for "Mass density" → knows property_group = VolumetricProp
  │
  ├─ 2. Consult MTDKS meas_summary → VolumetricProp techniques:
  │     vibrating_tube_method (13,110 instances), pycnometric_method (2,664), ...
  │
  ├─ 3. Load MTDKS ID_and_DK card for vibrating_tube_method →
  │     accuracy: "±0.00001 g/cm³", supports ionic liquids: YES
  │
  ├─ 4. Search MTDKS INDIV cards for papers using vibrating_tube_method
  │     in VolumetricProp → block_numbers tell which blocks to read
  │
  └─ 5. Load PCS INDIV card for the DOI → read data from those blocks
```

---

## 2. Tier 1: Technique ID & Domain Knowledge Cards

### 2.1 Card Location and Organization

Cards live under `Meas_ID_and_DK_cards/` organized into **16 technique family folders**:

| Folder | Family | # Cards | Principle |
|--------|--------|---------|-----------|
| `Acoustic_Speed_of_Sound/` | Acoustic / Speed of Sound | 9 | Sound wave propagation/resonance |
| `Calorimetry/` | Calorimetry | 21 | Heat exchange measurement |
| `Chromatography_Separation/` | Chromatography / Separation | 4 | Phase partitioning separation |
| `Conductivity_Electrochemistry/` | Conductivity / Electrochemistry | 3 | Ionic conductance / electrode potentials |
| `Densimetry/` | Densimetry | 10 | Mass/volume/buoyancy for density |
| `Differential_Scanning_Calorimetry_DSC_DTA/` | DSC/DTA | 5 | Temperature-scanning heat flow |
| `Diffusion/` | Diffusion | 6 | Molecular mass transport |
| `Extreme_conditions/` | Extreme Conditions | 3 | Rapid heating / containerless methods |
| `Optical_Refractometry/` | Optical / Refractometry | 5 | Refractive index / permittivity |
| `Other/` | Other | varies | Miscellaneous techniques |
| `PVT_Volumetric/` | PVT / Volumetric | 5 | Pressure-volume-temperature relations |
| `Surface_Tension/` | Surface Tension | 8 | Interface force/shape measurement |
| `Thermal_Conductivity/` | Thermal Conductivity | 4 | Heat transport through materials |
| `Vapor_Pressure_Volatility/` | Vapor Pressure / Volatility | 9+ | Equilibrium vapor pressure / boiling |
| `Viscometry/` | Viscometry | 9 | Resistance to flow / shear |
| `Visual_Direct_Observation/` | Visual / Direct Observation | 3 | Phase boundary observation |

### 2.2 meas_ID Construction

The `meas_ID` is the primary key — a slugified identifier derived from the canonical technique name.

**Rules:**
- Lowercase, underscores for spaces, no special characters
- Parenthetical qualifiers normalized: `(Ostwald; Ubbelohde)` → `ostwald_ubbelohde`
- Standard methods use the ThermoML `eMethodName` vocabulary
- Custom methods use the base abbreviation code or normalized free-text label

**Examples:**

| Source | meas_ID |
|--------|---------|
| `standard:Vibrating tube method` | `vibrating_tube_method` |
| `standard:Capillary tube (Ostwald; Ubbelohde) method` | `capillary_tube_ostwald_ubbelohde_method` |
| `standard:Small sample (50 mg) DSC` | `small_sample_50mg_dsc` |
| `custom:DTA (no standard equivalent)` | `dta` |
| `custom:Closed cell (Static) method` | `closed_cell_static` |

**UFactor variants** (e.g. `VIBTUB:UFactor:4`) share the `meas_ID` of their base technique
(`vibrating_tube_method`). The UFactor multiplier is per-paper metadata stored in MTDKS
INDIV, not per-technique identity.

### 2.3 Card Structure

Each ID_and_DK card has three top-level sections:

```
┌─────────────────────────────────────────┐
│  meas_ID: "vibrating_tube_method"       │  ◄── primary key
├─────────────────────────────────────────┤
│  identity:                              │  ◄── WHAT is this technique?
│    name, acronym, aliases               │
│    thermoml_standard_name               │
│    thermoml_custom_codes                │
│    measurement_family, modality         │
│    db_usage                             │
├─────────────────────────────────────────┤
│  domain_knowledge:                      │  ◄── HOW does it work?
│    structured_block:                    │
│      measurement_scope                  │
│      experimental_parameters            │
│      setup_and_requirements             │
│      performance                        │
│      data_and_interpretation            │
│      uncertainty                        │
│    description_block:                   │
│      (prose narrative)                  │
└─────────────────────────────────────────┘
```

#### 2.3.1 Identity Fields

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Full canonical name (e.g. "Vibrating tube method") |
| `acronym` | string | Standard abbreviation (e.g. "DSC", "GC"). Empty if none. |
| `aliases` | string[] | Alternative names, historical names, vendor-specific names |
| `thermoml_standard_name` | string\|null | Exact `eMethodName` from ThermoML vocabulary. `null` for custom-only. |
| `thermoml_custom_codes` | string[] | Custom abbreviation codes mapping to this technique (e.g. `["VIBTUB"]`) |
| `measurement_family` | string | Parent family (e.g. "Densimetry", "Calorimetry") |
| `modality.contact` | "yes"/"no"/"both" | Whether probe physically contacts sample |
| `modality.destructive` | "yes"/"no"/"partially" | Whether sample is consumed/altered |
| `modality.in_situ` | "yes"/"no"/"both" | Whether measured in process environment |
| `modality.imaging` | "yes"/"no"/"both" | Whether output is spatially resolved |

#### 2.3.2 db_usage Statistics

Each card carries per-technique database usage statistics:

| Field | Type | Description |
|-------|------|-------------|
| `instance_count` | integer | Total block-property instances across all papers |
| `property_groups` | string[] | Property groups this technique serves |
| `n_papers` | integer | Number of distinct DOIs using this technique |
| `per_group` | object | Breakdown of instances and papers per property group |

#### 2.3.3 Domain Knowledge: structured_block

The `structured_block` is the machine-parseable technical description. It follows the
template defined in `MTDKS_technique_skill_schema.md` and contains six sections:

**measurement_scope** — What the technique measures:
- `direct_observables` — Quantities the instrument directly records (signal level)
- `derived_observables` — Quantities computed via models or calibration
- `target_properties` — Thermodynamic/physical properties determined; maps to PCS `property_names`
- `phases_measured` — Applicable phase states
- `supported_sample_types` / `unsupported_sample_types` — Sample compatibility
- `typical_output_formats` — Data products (thermogram, isotherm, etc.)
- `units` — Key quantity → SI unit mapping

**experimental_parameters** — What is controlled vs. varied:
- `constraints[]` — Parameters held fixed (T, P, composition). Each has: `name`, `category` (thermodynamic/mechanical/chemical/temporal/geometric), `allowed_range`, `typical_values`, `required`
- `variables[]` — Parameters systematically varied (the x-axis). Each has: `name`, `category`, `comparison_role` (independent/scanning/stepped)

**setup_and_requirements** — Hardware, environment, sample prep:
- `instrument_components`, `environmental_requirements`, `sample_requirements` (geometry, size_limits, surface, mounting, preparation), `calibration_requirements`, `reference_materials`, `consumables`, `safety_notes`

**performance** — Quantitative capability envelope:
- `sensitivity`, `detection_limit`, `resolution` (spatial/temporal/spectral/energy), `dynamic_range`, `accuracy`, `precision`, `throughput`, `measurement_speed`

**data_and_interpretation** — Raw signal to result:
- `raw_signal_type`, `preprocessing_steps`, `analysis_methods`, `model_assumptions`, `fit_parameters`, `common_artifacts`, `quality_control_checks`, `failure_modes`

**uncertainty** — Error characterization:
- `level` (e.g. "0.1–0.5 %"), `random_sources`, `systematic_sources`, `operator_dependence` (low/moderate/high), `model_dependence`, `dominant_error_sources`, `reported_as`

#### 2.3.4 Domain Knowledge: description_block

Free-form prose narrative covering:
- Technique overview and historical context
- Operating principle explained in detail
- Practical considerations and best practices
- Comparison with related techniques

### 2.4 Example Card Walkthrough: `vibrating_tube_method`

**File:** `Meas_ID_and_DK_cards/Densimetry/vibrating_tube_method.json`

```
meas_ID:                  "vibrating_tube_method"
identity.name:            "Vibrating tube method"
identity.thermoml_standard_name: "Vibrating tube method"
identity.thermoml_custom_codes:  ["VIBTUB"]
identity.measurement_family:     "Densimetry"
identity.modality:        contact=yes, destructive=no, in_situ=no, imaging=no
identity.db_usage:
  instance_count:         13,110         ◄── most-used technique in VolumetricProp
  n_papers:               2,683
  property_groups:        ["VolumetricProp"]

domain_knowledge.structured_block:
  measurement_scope:
    direct_observables:   ["oscillation period τ of the vibrating U-tube",
                           "tube temperature (Pt-100 or NTC sensor)"]
    derived_observables:  ["density ρ via ρ = A·τ² + B",
                           "molar volume Vm = M/ρ",
                           "excess molar volume VE", ...]
    target_properties:    ["density ρ", "molar volume Vm", "excess molar volume VE",
                           "apparent molar volume Vφ", "thermal expansion αp", ...]
    phases_measured:       ["liquid", "compressed liquid", "supercritical fluid"]
    supported_sample_types: ["pure liquids", "binary mixtures", "ionic liquids",
                             "electrolyte solutions", "polymer solutions", ...]
    unsupported:          ["gases at ambient P", "solids/pastes/slurries",
                           "highly viscous >700 mPa·s without correction", ...]

  experimental_parameters:
    constraints:          T (278–363 K typical, to 473 K max)
                          P (0.1 MPa ambient, to 70 MPa with HP cell)
                          sample_viscosity (0.3–100 mPa·s uncorrected)
                          sample_volume (0.7–1.5 mL)
    variables:            temperature (5 K steps), pressure, composition

  performance:
    accuracy:             "±0.00001 g/cm³ (best case with DMA 5000)"
    precision:            "σ < 5×10⁻⁶ g/cm³"
    measurement_speed:    "1–3 min per equilibrated point"
```

### 2.5 Example Card Walkthrough: `calvet_calorimetry`

**File:** `Meas_ID_and_DK_cards/Calorimetry/calvet_calorimetry.json`

```
meas_ID:                  "calvet_calorimetry"
identity.name:            "Calvet calorimetry"
identity.thermoml_custom_codes:  ["CALVET"]
identity.measurement_family:     "Calorimetry"
identity.db_usage:
  instance_count:         911
  n_papers:               186
  property_groups:        ["ExcessPartialApparentEnergyProp"]

domain_knowledge.structured_block:
  measurement_scope:
    direct_observables:   ["thermopile voltage (V)",
                           "heat-flux signal (dQ/dt)",
                           "integrated thermopile signal"]
    derived_observables:  ["molar enthalpy of mixing (ΔmixH)",
                           "molar enthalpy of dissolution (ΔsolH)", ...]
    target_properties:    ["excess molar enthalpy HE",
                           "enthalpy of dissolution",
                           "heat capacity Cp", ...]
    supported_sample_types: ["liquid mixtures", "electrolyte solutions",
                             "ionic liquids", "polymer solutions", "solid powders"]
    unsupported:          ["gases at low P", "fast explosive reactions",
                           "sub-milliwatt detection needs"]
```

---

## 3. Tier 2: INDIV Method Usage Cards (Per-DOI)

### 3.1 Purpose and Scope

One MTDKS INDIV card per paper, recording **which techniques were used**. The parser
creates these at `_output/Query/Diagnostics/card_orchestrator/<doi>/mtdks_card.json`.

### 3.2 Card Structure

```json
{
  "key": {
    "doi": "10.1016/j.fluid.2016.03.016",
    "lit_id": "2016-sin-pan-0"
  },
  "methods_summary": {
    "n_unique_methods": 2,
    "n_standard": 1,
    "n_custom": 1,
    "technique_families": []
  },
  "methods": [
    {
      "method_type": "custom",
      "method_name": "isothermal titration calorimetry",
      "property_group": "ExcessPartialApparentEnergyProp",
      "property_names": ["Molar enthalpy of dilution, kJ/mol"],
      "block_numbers": [3, 5, 7, 9, 11, 15],
      "instance_count": 6
    },
    {
      "method_type": "standard",
      "method_name": "Vibrating tube method",
      "property_group": "VolumetricProp",
      "property_names": ["Mass density, kg/m3"],
      "block_numbers": [1, 2, 4, 6, 8, 10, 12, 13, 14],
      "instance_count": 9
    }
  ]
}
```

### 3.3 Field Reference

**key:**

| Field | Type | Description |
|-------|------|-------------|
| `doi` | string | DOI of the paper |
| `lit_id` | string | TRC literature identifier (`yrYrPub-sAuthor1-sAuthor2-nAuthorn`). 1:1 with DOI. |

**methods_summary:**

| Field | Type | Description |
|-------|------|-------------|
| `n_unique_methods` | integer | Distinct method_type:method_name combinations |
| `n_standard` | integer | Block-property instances using standard (controlled vocabulary) methods |
| `n_custom` | integer | Block-property instances using custom (free-text) methods |
| `technique_families` | string[] | Distinct technique families represented in this paper |

**methods[] array:**

| Field | Type | Description |
|-------|------|-------------|
| `method_type` | "standard"\|"custom" | Whether from controlled vocabulary or free-text |
| `method_name` | string | `eMethodName` (standard) or `sMethodName` (custom). UFactor suffix preserved. |
| `property_group` | string | Property group this method served in this paper |
| `property_names` | string[] | Specific `ePropName` values measured with this technique |
| `block_numbers` | integer[] | Block numbers where this technique was applied |
| `instance_count` | integer | Total block-property entries using this technique |

### 3.4 INDIV Card Examples from Parser Output

**Example 1 — Single standard method** (`10.1021/je060271a`):

```
DOI:     10.1021/je060271a
Methods: 1 unique, all standard
  [1] Vibrating tube method → VolumetricProp
      property_names: ["Mass density, kg/m3"]
      block_numbers:  [1, 2, 3, 4, 5]
      instance_count: 5
```
A straightforward density paper: one technique measured one property across 5 blocks.

**Example 2 — Mixed standard + custom** (`10.1016/j.fluid.2016.03.016`):

```
DOI:     10.1016/j.fluid.2016.03.016
Methods: 2 unique (1 standard, 1 custom)
  [1] custom: "isothermal titration calorimetry"
      → ExcessPartialApparentEnergyProp
      blocks: [3, 5, 7, 9, 11, 15]   instance_count: 6
  [2] standard: "Vibrating tube method"
      → VolumetricProp
      blocks: [1, 2, 4, 6, 8, 10, 12, 13, 14]   instance_count: 9
```
This paper used two techniques: density measurements (vibrating tube) and enthalpy of
dilution (ITC). Blocks interleave between the two methods.

**Example 3 — Custom method with UFactor** (`10.1016/j.fluid.2005.07.015`):

```
DOI:     10.1016/j.fluid.2005.07.015
Methods: 1 unique, all custom
  [1] custom: "CHROM:UFactor:4"
      → CompositionAtPhaseEquilibrium
      property_names: ["Mole fraction"]
      blocks: [1, 2]   instance_count: 9
```
This paper used chromatography (CHROM abbreviation) with uncertainty factor 4. The
UFactor encoding means the author assigned 4× the base uncertainty of chromatography.

### 3.5 Database-Wide Distribution

| Methods per paper | # Papers |
|-------------------|----------|
| 1 method | 4,598 |
| 2 methods | 3,309 |
| 3 methods | 2,049 |
| 4 methods | 1,090 |
| 5 methods | 482 |
| 6+ methods | 395 |

Average: **2.3 methods/paper** · Median: **2** · Max: **18**

---

## 4. Technique Summary Catalog

### 4.1 Purpose

`MTDKS_meas_summary.json` is the **global index** of all measurement techniques in
ThermoML. It serves as:

- Quick-lookup catalog for agents to discover available techniques
- Bridge between property groups and their measurement methods
- Reference for custom method abbreviation codes and UFactor encoding
- Source of technique family classifications

### 4.2 Standard Methods by Property Group

The summary lists all 160 standard methods organized by the 12 ThermoML property groups.
Top techniques by instance count per group:

| Property Group | Top Technique | Count | Total Std | Total Custom |
|----------------|--------------|-------|-----------|--------------|
| VolumetricProp | Vibrating tube method | 13,110 | 17,081 | 7,141 |
| CompositionAtPhaseEquilibrium | Chromatography | 12,275 | 15,187 | 16,509 |
| RefractionSurfaceTensionSoundSpeed | Abbe refractometry | 6,115 | 13,152 | 2,967 |
| ActivityFugacityOsmoticProp | Chromatography | 9,080 | 9,148 | 1,486 |
| TransportProp | Capillary tube (Ostwald) | 3,407 | 8,039 | 3,435 |
| VaporPBoilingTAzeotropTandP | Ebulliometric method | 3,230 | 4,581 | 6,672 |
| HeatCapacityAndDerivedProp | Small sample DSC | 1,160 | 3,545 | 1,491 |
| ExcessPartialApparentEnergyProp | Calvet calorimetry | 911 | 2,539 | 1,554 |
| PhaseTransition | Adiabatic calorimetry | 355 | 1,222 | 11,582 |
| ReactionStateChangeProp | Static bomb calorimetry | 472 | 892 | 254 |
| Criticals | Visual obs. (unstirred) | 284 | 704 | 822 |
| ReactionEquilibriumProp | NMR spectrometry | 48 | 94 | 6 |

### 4.3 Cross-Group Methods

20 standard methods serve **multiple property groups**. These are versatile techniques
whose measured quantity depends on context:

| Method | # Groups | Groups |
|--------|----------|--------|
| Chromatography | 5 | CompEq, Activity, VaporP, PhaseTrans, RxnEquil |
| Resistive pulse heating | 4 | HeatCap, Criticals, PhaseTrans, Transport |
| X-ray diffraction | 3 | PhaseTrans, Volumetric, CompEq |
| Flow calorimetry | 3 | HeatCap, ExcessEnergy, PhaseTrans |
| Levitation methods | 3 | Volumetric, Transport, HeatCap |

### 4.4 Custom Method Abbreviation Codes

97 unique base abbreviation codes map custom free-text methods back to standard
technique families. Selected mappings:

| Abbrev | Standard Equivalent | Family |
|--------|-------------------|--------|
| `VIBTUB` | Vibrating tube method | Densimetry |
| `CAPTUB` | Capillary tube (Ostwald; Ubbelohde) | Viscometry |
| `ABBE` | Standard Abbe refractometry | Optical |
| `CALVET` | Calvet calorimetry | Calorimetry |
| `EBULLIO` | Ebulliometric method (Recirculating still) | Vapor Pressure |
| `CHROM` | Chromatography | Chromatography |
| `DSC` | Small sample (50 mg) DSC | DSC/DTA |
| `DTA` | *(no standard equivalent)* | DSC/DTA |
| `KNUDSEN` | *(no standard equivalent)* | Vapor Pressure |

### 4.5 UFactor Encoding

Custom methods frequently carry a `:UFactor:N` suffix that encodes an **uncertainty
multiplier** assigned by the experimentalist:

```
Format:   <technique_abbrev>[:<qualifier>]*:UFactor:<integer>

Examples:
  VIBTUB:UFactor:4        → Vibrating tube, uncertainty × 4
  CAPTUB:UFactor:2        → Capillary viscometry, uncertainty × 2
  ABBE:UFactor:4          → Abbe refractometry, uncertainty × 4
  EBULLIO:UFactor:8       → Ebulliometric method, uncertainty × 8
  SMALLAD:dCP:0.2%:UFactor:2  → Small adiabatic, 0.2% Cp unc., factor × 2
```

**Statistics:** 16,800 instances carry UFactor suffixes across the 97 base codes.

The UFactor value **scales the base uncertainty** of the technique. A UFactor of 4 means
the author estimates 4× the typical uncertainty for that method, often due to
non-standard conditions, sample complexity, or instrument limitations.

### 4.6 Top Free-Text Custom Methods

The most common free-text custom methods (no UFactor code) used by experimentalists:

| Method | Count | Property Group |
|--------|-------|---------------|
| DTA | 4,038 | PhaseTransition |
| Titration method | 3,717 | CompositionAtPhaseEquilibrium |
| DSC | 3,437 | PhaseTransition |
| Closed cell (Static) method | 2,833 | VaporPBoilingTAzeotropTandP |
| VISOBS | 1,971 | PhaseTransition |
| OTHER | 1,464 | CompositionAtPhaseEquilibrium |
| gravimetric | 1,353 | CompositionAtPhaseEquilibrium |

---

## 5. Cross-Card References

### 5.1 Reference Diagram

```
  ┌─────────────┐          ┌──────────────────┐
  │   RMS       │◄─────────│   PCS INDIV      │
  │  (citation) │  key.doi │  (per-DOI data)  │
  └─────────────┘          └────────┬─────────┘
                                    │
                 ┌──────────────────┼──────────────────┐
                 │                  │                   │
                 ▼                  ▼                   ▼
        ┌────────────┐    ┌────────────────┐   ┌──────────────┐
        │ CCS        │    │ PCS ID_and_DK  │   │ MTDKS        │
        │ (compound) │    │ (property DK)  │   │ ID_and_DK    │
        │            │    │                │   │ (technique   │
        │ comp_id    │    │ prop_ID        │   │  DK)         │
        └────────────┘    └────────────────┘   └──────┬───────┘
                                                      │
                                               ┌──────┴───────┐
                                               │ MTDKS INDIV  │
                                               │ (per-DOI     │
                                               │  technique   │
                                               │  usage)      │
                                               └──────────────┘
```

### 5.2 PCS → MTDKS Link

The PCS INDIV card (per-DOI property data) links to MTDKS through two fields on each
property entry within a block:

```
blocks[].properties[].method_standard   → eMethodName string
blocks[].properties[].method_custom     → sMethodName string
blocks[].properties[].meas_ID          → slugified MTDKS ID_and_DK key
```

**Lookup path:**
1. Agent reads `blocks[i].properties[j].meas_ID` from PCS INDIV (e.g. `"vibrating_tube_method"`)
2. Agent loads `Meas_ID_and_DK_cards/Densimetry/vibrating_tube_method.json`
3. Agent reads domain knowledge: accuracy, failure modes, supported samples, etc.

When `meas_ID` is `null`, the property used a custom method with no mapped technique
card. The agent falls back to `method_custom` string for identification.

### 5.3 PCS INDIV Cross-Reference Map

The full cross-reference map from the PCS INDIV schema:

| PCS INDIV Field | Target Card | What It Provides |
|-----------------|-------------|------------------|
| `key.doi` | RMS (reference metadata) | Full citation, abstract, keywords |
| `blocks[].compounds[].comp_id` | CCS (compound identity) | SMILES, InChI, names |
| `blocks[].compounds[].comp_id + sample_num` | CCS (compound sample) | Purity, source, purification |
| `blocks[].properties[].prop_ID` | PCS ID_and_DK | Property domain knowledge |
| `blocks[].properties[].meas_ID` | **MTDKS ID_and_DK** | **Technique domain knowledge** |

### 5.4 MTDKS INDIV Block-Number Grouping

The MTDKS INDIV card groups block numbers by technique. This enables an agent to
quickly determine which blocks in a PCS INDIV card used which method:

```
MTDKS INDIV for DOI 10.1016/j.fluid.2016.03.016:
  methods[0]: "isothermal titration calorimetry" → blocks [3,5,7,9,11,15]
  methods[1]: "Vibrating tube method"            → blocks [1,2,4,6,8,10,12,13,14]

Agent needs enthalpy data → reads blocks 3,5,7,9,11,15 from PCS INDIV
Agent needs density data  → reads blocks 1,2,4,6,8,10,12,13,14 from PCS INDIV
```

---

## 6. Database Statistics

### 6.1 Global Counts

| Metric | Value |
|--------|-------|
| Total papers | 11,923 |
| Total block-property instances | 130,104 |
| Standard method instances | 76,184 (58.6%) |
| Custom method instances | 53,920 (41.4%) |
| Unique standard methods | 160 |
| Unique custom abbreviation codes | 97 |
| Unique free-text custom strings | 2,647 |
| Estimated distinct techniques (deduplicated) | ~160–200 |
| UFactor-encoded custom instances | 16,800 |

### 6.2 Methods per Paper Distribution

```
Methods/paper  │ Papers  │ Bar
───────────────┼─────────┼──────────────────────────────────────
 1             │  4,598  │ ████████████████████████████████████████
 2             │  3,309  │ ████████████████████████████
 3             │  2,049  │ █████████████████
 4             │  1,090  │ █████████
 5             │    482  │ ████
 6+            │    395  │ ███

 Average: 2.3  │ Median: 2  │ Max: 18
```

### 6.3 Top Techniques by Usage

| Rank | Technique | Instances | Papers | Family |
|------|-----------|-----------|--------|--------|
| 1 | Vibrating tube method | 13,110 | 2,683 | Densimetry |
| 2 | Chromatography | 12,275+ | — | Chromatography |
| 3 | Abbe refractometry | 6,115 | — | Optical |
| 4 | DTA *(custom)* | 4,038 | — | DSC/DTA |
| 5 | Titration method *(custom)* | 3,717 | — | Chromatography |
| 6 | DSC *(custom)* | 3,437 | — | DSC/DTA |
| 7 | Capillary tube (Ostwald) | 3,407 | 716 | Viscometry |
| 8 | Ebulliometric method | 3,230 | — | Vapor Pressure |
| 9 | Closed cell (Static) *(custom)* | 2,833 | — | Vapor Pressure |
| 10 | Pycnometric method | 2,664 | — | Densimetry |

### 6.4 Standard vs. Custom Balance by Group

```
Group                           Std %   Custom %    Notable
─────────────────────────────── ──────  ─────────   ─────────────────────────
VolumetricProp                   70.5%   29.5%      Dominated by vibrating tube
RefractionSurfaceTensionSS       81.6%   18.4%      Strong standard coverage
TransportProp                    70.1%   29.9%      Capillary tube leads
ActivityFugacityOsmoticProp      86.0%   14.0%      Chromatography dominates
ExcessPartialApparentEnergyProp  62.0%   38.0%      Calvet + flow calorimetry
HeatCapacityAndDerivedProp       70.4%   29.6%      DSC variants lead
ReactionStateChangeProp          77.8%   22.2%      Bomb calorimetry
ReactionEquilibriumProp          94.0%    6.0%      Nearly all standard
Criticals                        46.1%   53.9%      Many custom descriptions
VaporPBoilingTAzeotropTandP      40.7%   59.3%      Custom methods dominate
CompositionAtPhaseEquilibrium    47.9%   52.1%      Titration, gravimetric
PhaseTransition                   9.5%   90.5%  ◄── Overwhelmingly custom
```

**Key insight:** PhaseTransition has the highest custom-method fraction (90.5%),
reflecting the diversity of phase-transition detection methods that the standard
vocabulary does not cover (DTA, turbidity, visual observation variants, etc.).

---

## 7. Schema Files Reference

| File | Role |
|------|------|
| `MTDKS_meas_ID_and_DK_schema.json` | JSON schema for Tier 1 ID & DK cards |
| `MTDKS_meas_INDIV_metadata_schema.json` | JSON schema for Tier 2 INDIV cards |
| `MTDKS_meas_summary.json` | Global technique catalog (std methods, custom codes, families) |
| `MTDKS_technique_skill_schema.md` | Template/field-reference for structured_block content |
| `MTDKS_purpose.md` | Brief statement of MTDKS purpose |
| `_obsolete/generate_meas_cards.py` | Generator script for ID_and_DK cards from DB (one-shot; retained for provenance) |
| `Meas_ID_and_DK_cards/` | 16 family folders containing ~160 technique JSON cards |
