# DATABASE_ARCHITECTURE.md — ThermoML Raw Database & NIST Data Architecture

> **Current workspace note (2026-09-09):** Use [docs/DATA.md](../../docs/DATA.md) for the inspected inventory and runnable data interfaces. This directory now contains `thermoml_raw.db` and the browser's compressed `thermoml_raw_corpus.db`, without loose DOI directories. The `build_thermoml_sqlite.py` named in the historical reconstruction examples below is not included; those examples are not a supplied rebuild command. Full upstream byte-for-byte reconstruction claims below describe the earlier source-building workflow and were not revalidated for every record during this publication pass.

> **Database**: `thermoml_raw.db` (~1.92 GB)  
> **Archive version**: ThermoML.v2020-09-30  
> **Build script**: `build_thermoml_sqlite.py`  
> **Last verified**: 2026-03

---

## Table of Contents

1. [Overview](#1-overview)
2. [Source Data: NIST ThermoML XML Structure](#2-source-data-nist-thermoml-xml-structure)
3. [SQLite Database Schema](#3-sqlite-database-schema)
4. [Indexes](#4-indexes)
5. [Table Relationships](#5-table-relationships)
6. [Key Query Patterns](#6-key-query-patterns)
7. [Data Statistics](#7-data-statistics)
8. [Recovery & Reconstruction](#8-recovery--reconstruction)
9. [Database → Card Pipeline](#9-database--card-pipeline)

---

## 1. Overview

### What is ThermoML?

ThermoML is the **IUPAC/NIST standard XML format** for exchanging experimentally
determined thermodynamic and thermophysical property data. It was developed by the
Thermodynamics Research Center (TRC) at NIST as an open, machine-readable markup
language that encodes:

- **Bibliographic metadata** (publication, authors, DOI)
- **Chemical identities** (InChI, InChIKey, CAS, SMILES, molecular formula)
- **Sample provenance** (source, purification steps, purity values)
- **Measurement metadata** (method, property group, phases, conditions)
- **Tabular data** (variables, properties, uncertainties per data point)
- **Fitted equations** (Antoine, Wagner, polynomial, Helmholtz, etc.)

The schema (ThermoML.xsd v4.0) defines 188 property types across 13 property groups,
49 variable/constraint types, 32 phase descriptors, and ~500+ total enumeration values.

### The NIST ThermoML Archive (v2020-09-30)

The archive snapshot `ThermoML.v2020-09-30.db/` contains **11,923 data files**
spanning publications from approximately **2003 to 2019**. Each file corresponds
to one journal article or data report and is organized by DOI prefix:

```
ThermoML.v2020-09-30.db/
├── 10.1007/          ← Springer journals (Int. J. Thermophys., J. Sol. Chem., ...)
├── 10.1016/          ← Elsevier journals (Fluid Phase Equilib., J. Chem. Thermodyn., ...)
├── 10.1021/          ← ACS journals (J. Chem. Eng. Data, J. Phys. Chem., ...)
├── thermoml_raw.db   ← SQLite database consolidating all 11,923 files
├── thermoml_raw_db_README.md
├── NIST_thermoML_architecture.md
└── DATABASE_ARCHITECTURE.md  (this file)
```

The upstream release contains `.json` files named by DOI suffix
(e.g., `10.1021/je050342f.json`) paired with XML. NIST generates XML from JSON;
JSON can retain information outside the ThermoML XML schema. The extracted
directory tree shown above is historical; the current workspace stores these
documents in SQLite. See the [NIST data record](https://data.nist.gov/pdr/lps/ark%3A/88434/mds2-2422).

### Purpose of thermoml_raw.db

`thermoml_raw.db` is a single-file SQLite database that consolidates all 11,923
JSON files into one queryable store. It serves two roles:

1. **Verbatim archive** — every original JSON file is stored byte-for-byte in
   `papers.json_data`, enabling full round-trip recovery of all original data
2. **Query index** — four derived tables (`compounds`, `blocks`, `block_properties`,
   `block_variables`) extract key fields for fast SQL lookups without parsing JSON

### Zero-Loss Guarantee

Every original JSON file is stored **byte-for-byte** in `papers.json_data`.
The derived index tables are convenience views — they are **never** the source
of truth. Given `thermoml_raw.db`, you can reconstruct the entire original
`ThermoML.v2020-09-30.db/` directory tree with zero information loss.

Additionally, every JSON file contains a `THERMOML_MD5_CHECKSUM` field assigned
by NIST at publication time. This checksum is preserved in `papers.md5_checksum`
and can be used to verify data integrity against NIST's official release.

---

## 2. Source Data: NIST ThermoML XML Structure

### 2.1 Complete XML Element Tree

The ThermoML `DataReport` root element contains five top-level sections.
The JSON representation preserves this structure exactly, with two additional
JSON-only fields (`THERMOML_MD5_CHECKSUM` and `tml_elements`):

```
DataReport  (= one JSON file = one row in papers)
│
├─ Version
│  ├─ nVersionMajor
│  └─ nVersionMinor
│
├─ Citation                              ← bibliographic metadata
│  ├─ TRCRefID
│  │  ├─ yrYrPub                         ← publication year (TRC format)
│  │  ├─ sAuthor1                        ← first author abbreviation
│  │  ├─ sAuthor2                        ← second author abbreviation
│  │  └─ nAuthorn                        ← author distinguisher number
│  ├─ eType                              ← 10 enums (journal, book, thesis, patent, ...)
│  ├─ eSourceType                        ← 3 enums (Original, ChemicalAbstracts, Other)
│  ├─ sAuthor [repeated]                 ← full author names
│  ├─ sPubName                           ← journal/publication name
│  ├─ yrPubYr                            ← publication year
│  ├─ dateCit                            ← citation date
│  ├─ sTitle                             ← article title
│  ├─ sAbstract                          ← abstract text
│  ├─ sDOI                               ← Digital Object Identifier
│  ├─ sIDNum                             ← issue number
│  ├─ sPage                              ← page range
│  ├─ sVol                               ← volume number
│  └─ sKeyword [repeated]               ← keywords
│
├─ Compound [0..*]                       ← chemical substance definitions
│  ├─ RegNum
│  │  └─ nOrgNum                         ← TRC organization number (local compound ID)
│  ├─ sCommonName [0..*]                 ← common chemical names
│  ├─ sFormulaMolec                      ← molecular formula
│  ├─ sStandardInChI                     ← IUPAC InChI identifier
│  ├─ sStandardInChIKey                  ← hashed InChI key (27 chars)
│  ├─ sCASRegistryNumber                 ← CAS registry number
│  └─ Sample [0..*]                      ← physical sample provenance
│     ├─ nSampleNm                       ← sample number
│     ├─ eSource                         ← 7 enums (Commercial, Synthesized, SRM, ...)
│     ├─ eStatus                         ← 4 enums (unknown, notDescribed, ...)
│     └─ purity [0..*]                   ← per-purification-step purity
│        ├─ nStep                        ← purification step number
│        ├─ eAnalMeth / sAnalMeth        ← analysis method (enum or free-text)
│        ├─ ePurifMethod / sPurifMethod  ← purification method (enum or free-text)
│        ├─ nPurityMol / nPurityMolDigits
│        ├─ nPurityMass / nPurityMassDigits
│        ├─ nPurityVol / nPurityVolDigits
│        ├─ nWaterMassPerCent / nWaterMassPerCentDigits
│        ├─ nHalideMassPerCent / nHalideMassPerCentDigits
│        ├─ nHalideMolPerCent / nHalideMolPerCentDigits
│        └─ nUnknownPerCent / nUnknownPerCentDigits
│
├─ PureOrMixtureData [0..*]             ← measurement blocks (non-reaction)
│  ├─ nPureOrMixtureDataNumber           ← unique block ID within paper
│  ├─ Component [1..*]                   ← which compounds are studied
│  │  ├─ RegNum.nOrgNum                  ← references Compound by nOrgNum
│  │  └─ nSampleNm                       ← which sample was used
│  ├─ eExpPurpose                        ← 3 enums (Principal, Secondary, Identification)
│  ├─ sCompiler / sContributor / dateDateAdded
│  │
│  ├─ Property [1..*]                    ← what was measured
│  │  ├─ nPropNumber                     ← property ID within block
│  │  ├─ Property-MethodID
│  │  │  ├─ PropertyGroup
│  │  │  │  └─ <GroupName>               ← one of 11 groups (see §2.3)
│  │  │  │     ├─ ePropName              ← e.g. "Mass density, kg/m3"
│  │  │  │     ├─ eMethodName            ← standard method (enum)
│  │  │  │     └─ sMethodName            ← custom method (free-text)
│  │  │  └─ RegNum.nOrgNum              ← property is for this compound
│  │  ├─ ePresentation                   ← 7 enums (Direct value, Difference, Mean, ...)
│  │  ├─ eStandardState                  ← 5 enums (Pure compound, Infinite dilution, ...)
│  │  ├─ eRefStateType                   ← 12 enums (various reference states)
│  │  ├─ nRefTemp / nRefPressure         ← reference T and P
│  │  ├─ PropPhaseID                     ← which phase this property describes
│  │  │  ├─ ePropPhase                   ← 32-value phase enum
│  │  │  └─ RegNum.nOrgNum              ← component-specific phase
│  │  ├─ RefPhaseID                      ← reference phase
│  │  ├─ Solvent                         ← solvent compound reference
│  │  └─ CombinedUncertainty [0..*]     ← block-level uncertainty definition
│  │     ├─ nCombUncertAssessNum         ← assessment ID (referenced by data points)
│  │     ├─ eCombUncertEvalMethod        ← evaluation method
│  │     ├─ nCombUncertLevOfConfid       ← confidence level (e.g. 95)
│  │     └─ sCombUncertEvaluator         ← who evaluated
│  │
│  ├─ PhaseID [0..*]                     ← phases present in the system
│  │  ├─ ePhase                          ← 32-value phase enum
│  │  └─ RegNum.nOrgNum                 ← component-specific phase
│  │
│  ├─ Constraint [0..*]                  ← fixed conditions
│  │  ├─ nConstraintNumber               ← constraint ID within block
│  │  ├─ ConstraintID
│  │  │  ├─ ConstraintType
│  │  │  │  └─ eTemperature / ePressure / eComponentComposition / ...
│  │  │  └─ RegNum.nOrgNum              ← for component-specific constraints
│  │  ├─ nConstraintValue                ← the fixed value
│  │  ├─ nConstrDigits                   ← significant digits
│  │  └─ ConstraintPhaseID              ← phase for this constraint
│  │
│  ├─ Variable [0..*]                    ← swept conditions
│  │  ├─ nVarNumber                      ← variable ID within block
│  │  ├─ VariableID
│  │  │  ├─ VariableType
│  │  │  │  └─ eTemperature / ePressure / eComponentComposition / ...
│  │  │  └─ RegNum.nOrgNum              ← for component-specific variables
│  │  └─ VarPhaseID                      ← phase for this variable
│  │
│  └─ NumValues [0..*]                   ← tabulated data (one element = one row)
│     ├─ VariableValue [1..*]
│     │  ├─ nVarNumber                   ← links to Variable definition
│     │  ├─ nVarValue                    ← measured value
│     │  └─ nVarDigits                   ← significant digits
│     └─ PropertyValue [1..*]
│        ├─ nPropNumber                  ← links to Property definition
│        ├─ nPropValue                   ← measured value
│        ├─ nPropDigits                  ← significant digits
│        └─ CombinedUncertainty         ← per-point uncertainty
│           ├─ nCombUncertAssessNum      ← references block-level assessment
│           └─ nCombExpandUncertValue    ← expanded uncertainty value
│
├─ ReactionData [0..*]                   ← measurement blocks (reactions)
│  ├─ nReactionDataNumber                ← unique block ID within paper
│  ├─ eReactionType                      ← 25 enums (Combustion, Hydrogenation, ...)
│  ├─ eReactionFormalism                 ← 2 enums (Chemical, Biochemical)
│  ├─ Participant [1..*]                 ← reactants and products
│  │  ├─ RegNum.nOrgNum                 ← compound reference
│  │  ├─ nSampleNm                       ← sample used
│  │  ├─ ePhase                          ← phase of this participant
│  │  ├─ nStoichiometricCoef             ← stoichiometry (negative = reactant)
│  │  └─ eCompositionRepresentation      ← 8 enums
│  ├─ Property [1..*]                    ← same structure as PureOrMixtureData
│  │  └─ PropertyGroup → ReactionStateChangeProp | ReactionEquilibriumProp
│  ├─ Constraint [0..*]                  ← same structure
│  ├─ Variable [0..*]                    ← same structure
│  └─ NumValues [0..*]                   ← same structure
│
├─ THERMOML_MD5_CHECKSUM                 ← JSON-only: NIST-assigned integrity hash
└─ tml_elements                          ← JSON-only: element ordering helper
```

### 2.2 The 13 Property Groups

Each Property belongs to exactly one group. Groups 1–11 appear in
`PureOrMixtureData`; groups 12–13 appear in `ReactionData`:

```
 #  PropertyGroup Name                        Props  Domain
──  ──────────────────────────────────────────  ─────  ──────────────────────────────
 1  Criticals                                    10   Critical T, P, V, density
 2  VaporPBoilingTAzeotropTandP                   5   Vapor pressure, boiling point
 3  PhaseTransition                              12   Melting T, triple point, glass Tg
 4  CompositionAtPhaseEquilibrium                31   Solubility, Henry's law, UCST/LCST
 5  ActivityFugacityOsmoticProp                   8   Activity coeff., fugacity, osmotic
 6  VolumetricProp                               24   Density, molar volume, compressibility
 7  HeatCapacityAndDerivedProp                   20   Cp, Cv, Joule-Thomson
 8  ExcessPartialApparentEnergyProp              22   ΔH mixing, dilution, vaporization
 9  TransportProp                                12   Viscosity, diffusion, conductivity
10  RefractionSurfaceTensionSoundSpeed           14   Refractive index, surface tension
11  BioProperties                                 5   Optical rotation, isoelectric point
12  ReactionStateChangeProp                      10   ΔH, ΔG, ΔS, cell potential
13  ReactionEquilibriumProp                      15   Equilibrium constants (K, ln K)
──  ──────────────────────────────────────────  ─────  ──────────────────────────────
    TOTAL                                       188
```

### 2.3 Variable/Constraint Type System

Variables (swept conditions) and Constraints (fixed conditions) share the same
`ConstraintVariableType` with 49 enumerated values across 7 categories:

```
Category                   # Enums  Examples
─────────────────────────  ───────  ────────────────────────────────────────
eTemperature                    3   Temperature K, Upper/Lower temperature K
ePressure                       4   Pressure kPa, Partial pressure kPa
eComponentComposition          16   Mole fraction, Mass fraction, Molality, Molarity
eSolventComposition            10   Solvent: Mole/Mass/Volume fraction, ratios
eMiscellaneous                  9   Wavelength nm, Frequency MHz, Molar volume
eBioVariables                   5   pH, Ionic strength
eParticipantAmount              2   Amount mol, Mass kg
─────────────────────────  ───────
TOTAL                          49
```

### 2.4 Key Design Patterns of ThermoML XML

#### nOrgNum + RegNum Compound Reference System

Compounds are defined once at the top level with `RegNum.nOrgNum` as their local ID.
They are then **referenced by nOrgNum** everywhere else:

```
Compound[0].RegNum.nOrgNum = 1    ← "water" defined here
Compound[1].RegNum.nOrgNum = 2    ← "ethanol" defined here
    ...
PureOrMixtureData[0].Component[0].RegNum.nOrgNum = 1   ← references water
PureOrMixtureData[0].Component[1].RegNum.nOrgNum = 2   ← references ethanol
PureOrMixtureData[0].Property[0].Property-MethodID.RegNum.nOrgNum = 1  ← property FOR water
PureOrMixtureData[0].Property[0].PropPhaseID.RegNum.nOrgNum = 1        ← phase OF water
```

This reference system avoids duplication and decouples chemical identity from
measurement context. The same compound can appear in many blocks with different
phases, samples, and roles.

#### Property/Variable/Constraint Numbering

Within each data block, properties, variables, and constraints are assigned
sequential integer IDs (`nPropNumber`, `nVarNumber`, `nConstraintNumber`).
These IDs are **local to the block** and serve as join keys into `NumValues`:

```
Property:   nPropNumber = 1, 2, 3, ...
Variable:   nVarNumber  = 1, 2, 3, ...
Constraint: nConstraintNumber = 1, 2, 3, ...

NumValues[i]:
  VariableValue[].nVarNumber   → links to Variable definition
  PropertyValue[].nPropNumber  → links to Property definition
```

#### Standard vs. Custom Method Encoding

Each Property carries a measurement method, encoded as either:

- **Standard method** (`eMethodName`): a controlled-vocabulary enum (e.g., "Vibrating tube method")
- **Custom method** (`sMethodName`): free-text string, often using the **UFactor encoding**:

```
UFactor pattern:   ABBREV:UFactor:N
                   ABBREV:Qualifier:UFactor:N

Examples:
  "VIBTUB:UFactor:4"            ← Vibrating tube + uncertainty factor 4
  "SMALLAD:dCP:0.2:UFactor:2"   ← Small-angle adiabatic + dCP=0.2 + UFactor 2
  "DTA"                          ← Pure free-text (no UFactor)
```

The database contains 160 unique standard method names and 2,647 unique custom
method strings (97 unique UFactor abbreviation base codes).

#### Multi-Property Block Semantics

A single data block can carry **multiple properties** — typically the same
property name for different (component, phase) combinations. For example, a
ternary LLE block might measure "Mole fraction" three times:

```
Property #1: Mole fraction of compound 2 in Liquid mixture 2
Property #2: Mole fraction of compound 2 in Liquid mixture 1
Property #3: Mole fraction of compound 4 in Liquid mixture 1
```

Each `NumValues` row then contains one value per property, all at the same
variable conditions. The `Property-MethodID.RegNum.nOrgNum` and `PropPhaseID`
fields disambiguate what would otherwise be identical "Mole fraction" entries.

#### Phase Assignment

ThermoML compounds are **phase-agnostic** — phase information belongs to
measurements, not compounds. The 32-value `ePhaseName` enum appears in:

| Location          | Element           | Purpose                              |
|-------------------|-------------------|--------------------------------------|
| Block level       | `PhaseID`         | Phases present in the system         |
| Property level    | `PropPhaseID`     | Which phase the property describes   |
| Variable level    | `VarPhaseID`      | Phase for a composition variable     |
| Constraint level  | `ConstraintPhaseID` | Phase for a constrained condition  |
| Reaction          | `Participant.ePhase` | Phase of each reactant/product    |

---

## 3. SQLite Database Schema

### 3.1 Table: `papers` — One Row Per JSON File (11,923 rows)

The **primary table** and single source of truth. `json_data` stores the complete,
unmodified JSON string from each original file.

```sql
CREATE TABLE papers (
    doi                TEXT PRIMARY KEY,      -- e.g. '10.1021/je050342f'
    file_path          TEXT NOT NULL UNIQUE,   -- e.g. '10.1021/je050342f.json'
    json_data          TEXT NOT NULL,          -- VERBATIM original JSON string
    md5_checksum       TEXT,                   -- NIST THERMOML_MD5_CHECKSUM
    n_compounds        INTEGER NOT NULL,       -- len(Compound[])
    n_pure_blocks      INTEGER NOT NULL,       -- len(PureOrMixtureData[])
    n_reaction_blocks  INTEGER NOT NULL,       -- len(ReactionData[])
    title              TEXT,                   -- Citation.sTitle
    year               INTEGER,               -- Citation.yrPubYr
    journal            TEXT,                   -- Citation.sPubName
    first_author       TEXT                    -- Citation.sAuthor[0]
);
```

| Column | Purpose |
|--------|---------|
| `doi` | Primary key. DOI of the source publication. |
| `file_path` | Relative path within the archive (e.g., `10.1021/je050342f.json`). |
| `json_data` | **Byte-for-byte** copy of the original JSON file. This is the source of truth. |
| `md5_checksum` | NIST-assigned `THERMOML_MD5_CHECKSUM` embedded in each JSON. Not a computed hash — an integrity token from NIST's data release. All 11,923 files have this populated. |
| `n_compounds` | Number of `Compound` elements. |
| `n_pure_blocks` | Number of `PureOrMixtureData` blocks. |
| `n_reaction_blocks` | Number of `ReactionData` blocks. |
| `title` | Article title, extracted for quick browsing. |
| `year` | Publication year, extracted for temporal queries. |
| `journal` | Journal name, extracted for source filtering. |
| `first_author` | First author name, extracted for author queries. |

### 3.2 Table: `compounds` — One Row Per Compound Per Paper (61,113 rows)

Derived index for chemical identity lookups. Each row represents one compound
as it appears in one paper. The same chemical may appear in many papers with
different nOrgNum values.

```sql
CREATE TABLE compounds (
    doi                TEXT NOT NULL,          -- FK → papers.doi
    org_num            INTEGER NOT NULL,       -- Compound.RegNum.nOrgNum
    standard_inchi     TEXT,                   -- Compound.sStandardInChI
    standard_inchi_key TEXT,                   -- Compound.sStandardInChIKey
    common_name        TEXT,                   -- Compound.sCommonName[0]
    formula            TEXT,                   -- Compound.sFormulaMolec
    cas_rn             TEXT,                   -- Compound.sCASRegistryNumber
    PRIMARY KEY (doi, org_num),
    FOREIGN KEY (doi) REFERENCES papers(doi)
);
```

| Column | Purpose |
|--------|---------|
| `doi` | Foreign key to `papers`. |
| `org_num` | The `nOrgNum` identifier local to this paper. |
| `standard_inchi` | Full InChI string (when available). |
| `standard_inchi_key` | 27-character InChIKey — the best cross-paper compound identifier. |
| `common_name` | First common name from `sCommonName[]` array. |
| `formula` | Molecular formula (e.g., "C2H6O"). |
| `cas_rn` | CAS Registry Number (when available). |

**Note**: 61,113 rows represent compound-per-paper appearances, not unique compounds.
There are approximately **8,502 unique InChIKey values** across all papers.

### 3.3 Table: `blocks` — One Row Per Data Block (123,727 rows)

Derived index for measurement block metadata. Each row maps to one
`PureOrMixtureData` or `ReactionData` element.

```sql
CREATE TABLE blocks (
    doi                TEXT NOT NULL,          -- FK → papers.doi
    block_number       INTEGER NOT NULL,       -- nPureOrMixtureDataNumber or nReactionDataNumber
    block_type         TEXT NOT NULL,          -- 'PureOrMixtureData' or 'ReactionData'
    n_components       INTEGER NOT NULL,       -- Number of Component/Participant elements
    component_org_nums TEXT,                   -- JSON array, e.g. '[1, 2]'
    n_properties       INTEGER NOT NULL,       -- len(Property[])
    n_variables        INTEGER NOT NULL,       -- len(Variable[])
    n_constraints      INTEGER NOT NULL,       -- len(Constraint[])
    n_datapoints       INTEGER NOT NULL,       -- len(NumValues[])
    PRIMARY KEY (doi, block_number, block_type),
    FOREIGN KEY (doi) REFERENCES papers(doi)
);
```

| Column | Purpose |
|--------|---------|
| `doi` | Foreign key to `papers`. |
| `block_number` | The integer ID assigned by ThermoML within the paper. |
| `block_type` | Distinguishes `PureOrMixtureData` (physical properties) from `ReactionData` (reaction properties). |
| `n_components` | Number of compounds in the block (unary=1, binary=2, etc.). |
| `component_org_nums` | JSON array of nOrgNum values to link back to `compounds`. |
| `n_properties` | Number of distinct properties measured in this block. |
| `n_variables` | Number of swept independent variables. |
| `n_constraints` | Number of fixed conditions. |
| `n_datapoints` | Number of `NumValues` rows (data points). |

### 3.4 Table: `block_properties` — One Row Per Property Per Block (130,104 rows)

Derived index for property/method lookups. Enables queries like
"find all blocks measuring viscosity with a capillary method."

```sql
CREATE TABLE block_properties (
    doi                TEXT NOT NULL,
    block_number       INTEGER NOT NULL,
    block_type         TEXT NOT NULL,
    prop_number        INTEGER NOT NULL,       -- Property.nPropNumber
    prop_group         TEXT NOT NULL,          -- e.g. 'VolumetricProp'
    prop_name          TEXT NOT NULL,          -- e.g. 'Mass density, kg/m3'
    method_type        TEXT,                   -- 'standard' or 'custom'
    method_name        TEXT,                   -- eMethodName or sMethodName value
    presentation       TEXT,                   -- ePresentation value
    PRIMARY KEY (doi, block_number, block_type, prop_number),
    FOREIGN KEY (doi) REFERENCES papers(doi)
);
```

| Column | Purpose |
|--------|---------|
| `prop_number` | Property ID local to the block. |
| `prop_group` | The PropertyGroup name (e.g., "VolumetricProp", "TransportProp"). |
| `prop_name` | The `ePropName` value with unit (e.g., "Mass density, kg/m3"). |
| `method_type` | `"standard"` if `eMethodName` is used, `"custom"` if `sMethodName`. |
| `method_name` | The method name string — either controlled vocabulary or free-text/UFactor. |
| `presentation` | How the value is expressed (e.g., "Direct value, X"). |

### 3.5 Table: `block_variables` — One Row Per Variable Per Block (168,687 rows)

Derived index for variable type lookups.

```sql
CREATE TABLE block_variables (
    doi                TEXT NOT NULL,
    block_number       INTEGER NOT NULL,
    block_type         TEXT NOT NULL,
    var_number         INTEGER NOT NULL,       -- Variable.nVarNumber
    var_type           TEXT NOT NULL,          -- e.g. 'Temperature, K'
    PRIMARY KEY (doi, block_number, block_type, var_number),
    FOREIGN KEY (doi) REFERENCES papers(doi)
);
```

| Column | Purpose |
|--------|---------|
| `var_number` | Variable ID local to the block. |
| `var_type` | The variable type name (e.g., "Temperature, K", "Pressure, kPa", "Mole fraction"). |

---

## 4. Indexes

Nine indexes optimize the most common query patterns:

```sql
CREATE INDEX idx_papers_year        ON papers(year);
CREATE INDEX idx_compounds_inchikey ON compounds(standard_inchi_key);
CREATE INDEX idx_compounds_name     ON compounds(common_name);
CREATE INDEX idx_compounds_cas      ON compounds(cas_rn);
CREATE INDEX idx_blocks_type        ON blocks(block_type);
CREATE INDEX idx_bprop_group        ON block_properties(prop_group);
CREATE INDEX idx_bprop_name         ON block_properties(prop_name);
CREATE INDEX idx_bprop_method       ON block_properties(method_name);
CREATE INDEX idx_bvar_type          ON block_variables(var_type);
```

| Index | Column | Optimizes |
|-------|--------|-----------|
| `idx_papers_year` | `papers.year` | Temporal filtering (papers by decade, year range) |
| `idx_compounds_inchikey` | `compounds.standard_inchi_key` | Cross-paper compound lookup (the primary compound ID) |
| `idx_compounds_name` | `compounds.common_name` | Name-based compound search |
| `idx_compounds_cas` | `compounds.cas_rn` | CAS number lookup |
| `idx_blocks_type` | `blocks.block_type` | PureOrMixtureData vs ReactionData filtering |
| `idx_bprop_group` | `block_properties.prop_group` | Filter by property category (VolumetricProp, TransportProp, ...) |
| `idx_bprop_name` | `block_properties.prop_name` | Find specific property measurements (Mass density, Viscosity, ...) |
| `idx_bprop_method` | `block_properties.method_name` | Find measurements by technique |
| `idx_bvar_type` | `block_variables.var_type` | Find blocks with specific variables (Temperature, Pressure, ...) |

---

## 5. Table Relationships

### Entity-Relationship Diagram

```
+------------------------------+
|          papers               |      SOURCE OF TRUTH
|------------------------------|
| PK: doi                TEXT  |
|     file_path           TEXT  |
|     json_data           TEXT  |  ◄── complete original JSON
|     md5_checksum        TEXT  |
|     n_compounds         INT   |
|     n_pure_blocks       INT   |
|     n_reaction_blocks   INT   |
|     title               TEXT  |
|     year                INT   |
|     journal             TEXT  |
|     first_author        TEXT  |
+-----+--------+---------------+
      |        |
      |        |  1:N
      |        |
      |   +----v----------------------------+
      |   |         compounds                |
      |   |------------------------------- --|
      |   | PK: doi            TEXT          |
      |   | PK: org_num        INT           |
      |   |     standard_inchi      TEXT      |
      |   |     standard_inchi_key  TEXT      |
      |   |     common_name         TEXT      |
      |   |     formula             TEXT      |
      |   |     cas_rn              TEXT      |
      |   +----------------------------------+
      |
      |  1:N
      |
+-----v----------------------------+
|           blocks                  |
|----------------------------------|
| PK: doi            TEXT          |
| PK: block_number   INT           |
| PK: block_type     TEXT          |
|     n_components    INT           |
|     component_org_nums TEXT (JSON)|  ──── references compounds.org_num
|     n_properties    INT           |
|     n_variables     INT           |
|     n_constraints   INT           |
|     n_datapoints    INT           |
+-----+--------+-------------------+
      |        |
      |        |  1:N
      |        |
      |   +----v----------------------------+
      |   |     block_properties             |
      |   |------------------------------- --|
      |   | PK: doi            TEXT          |
      |   | PK: block_number   INT           |
      |   | PK: block_type     TEXT          |
      |   | PK: prop_number    INT           |
      |   |     prop_group     TEXT          |
      |   |     prop_name      TEXT          |
      |   |     method_type    TEXT          |
      |   |     method_name    TEXT          |
      |   |     presentation   TEXT          |
      |   +----------------------------------+
      |
      |  1:N
      |
+-----v----------------------------+
|       block_variables             |
|----------------------------------|
| PK: doi            TEXT          |
| PK: block_number   INT           |
| PK: block_type     TEXT          |
| PK: var_number     INT           |
|     var_type        TEXT          |
+----------------------------------+
```

### Relationship Summary

```
papers ─────1:N───── compounds         FK: compounds.doi → papers.doi
papers ─────1:N───── blocks            FK: blocks.doi → papers.doi
blocks ─────1:N───── block_properties  FK: (doi, block_number, block_type)
blocks ─────1:N───── block_variables   FK: (doi, block_number, block_type)

blocks.component_org_nums ──ref──> compounds.org_num  (logical, via JSON array)
```

### Cross-Table Compound Linkage

The `blocks.component_org_nums` column stores a JSON array like `[1, 2]`.
These integers are `nOrgNum` values that link to `compounds.org_num` within
the same DOI. To resolve a block's compounds:

```sql
-- Given a block, find its compound details
SELECT c.*
FROM compounds c
WHERE c.doi = '10.1021/je050342f'
  AND c.org_num IN (
    SELECT value FROM json_each(
      (SELECT component_org_nums FROM blocks
       WHERE doi = '10.1021/je050342f'
         AND block_number = 1
         AND block_type = 'PureOrMixtureData')
    )
  );
```

---

## 6. Key Query Patterns

### 6.1 Retrieve a Single Paper's Full JSON Data

```sql
SELECT json_data FROM papers WHERE doi = '10.1021/je050342f';
```

Parse in Python:
```python
import sqlite3, json
conn = sqlite3.connect('thermoml_raw.db')
row = conn.execute('SELECT json_data FROM papers WHERE doi = ?',
                    ('10.1021/je050342f',)).fetchone()
data = json.loads(row[0])
```

### 6.2 Find All Blocks for a Compound (by InChIKey)

```sql
SELECT b.doi, b.block_number, b.block_type, b.n_datapoints,
       bp.prop_name, bp.method_name
FROM blocks b
JOIN compounds c ON c.doi = b.doi
JOIN block_properties bp ON bp.doi = b.doi
     AND bp.block_number = b.block_number
     AND bp.block_type = b.block_type
WHERE c.standard_inchi_key = 'XLYOFNOQVPJJNP-UHFFFAOYSA-N'   -- water
  AND b.component_org_nums LIKE '%' || c.org_num || '%';
```

### 6.3 Find All Papers Measuring a Specific Property

```sql
SELECT DISTINCT p.doi, p.title, p.year, p.journal
FROM papers p
JOIN block_properties bp ON bp.doi = p.doi
WHERE bp.prop_name = 'Mass density, kg/m3'
ORDER BY p.year DESC;
```

### 6.4 Find All Binary System Blocks with Method Filter

```sql
SELECT b.doi, b.block_number, bp.prop_name, bp.method_name, b.n_datapoints
FROM blocks b
JOIN block_properties bp ON bp.doi = b.doi
     AND bp.block_number = b.block_number
     AND bp.block_type = b.block_type
WHERE b.n_components = 2
  AND bp.prop_group = 'VolumetricProp'
  AND bp.method_type = 'standard'
  AND bp.method_name = 'Vibrating tube method';
```

### 6.5 Count Property Instances by Group

```sql
SELECT prop_group, COUNT(*) as n_instances,
       COUNT(DISTINCT prop_name) as n_distinct_properties
FROM block_properties
GROUP BY prop_group
ORDER BY n_instances DESC;
```

### 6.6 Find Papers with Temperature-Dependent Data in a Range

```sql
SELECT DISTINCT p.doi, p.title
FROM papers p
JOIN blocks b ON b.doi = p.doi
JOIN block_variables bv ON bv.doi = b.doi
     AND bv.block_number = b.block_number
     AND bv.block_type = b.block_type
WHERE bv.var_type = 'Temperature, K';
```

### 6.7 JSON Extraction Patterns for Nested Data

SQLite's `json_extract()` can access nested values directly from `json_data`:

```sql
-- Get the title from Citation
SELECT json_extract(json_data, '$.Citation.sTitle') AS title
FROM papers WHERE doi = '10.1021/je050342f';

-- Get the first compound's InChIKey
SELECT json_extract(json_data, '$.Compound[0].sStandardInChIKey')
FROM papers WHERE doi = '10.1021/je050342f';

-- Count PureOrMixtureData blocks
SELECT json_array_length(json_data, '$.PureOrMixtureData')
FROM papers WHERE doi = '10.1021/je050342f';

-- Get property name from first block's first property
SELECT json_extract(json_data,
  '$.PureOrMixtureData[0].Property[0].Property-MethodID.PropertyGroup')
FROM papers WHERE doi = '10.1021/je050342f';
```

### 6.8 Method Distribution Analysis

```sql
-- Top 20 measurement methods
SELECT method_type, method_name, COUNT(*) as count
FROM block_properties
WHERE method_name IS NOT NULL
GROUP BY method_type, method_name
ORDER BY count DESC
LIMIT 20;

-- UFactor-encoded custom methods
SELECT method_name, COUNT(*) as count
FROM block_properties
WHERE method_type = 'custom' AND method_name LIKE '%UFactor%'
GROUP BY method_name
ORDER BY count DESC;
```

---

## 7. Data Statistics

### 7.1 Table Row Counts

| Table | Rows | Description |
|-------|-----:|-------------|
| `papers` | 11,923 | One per JSON file (= one per publication) |
| `compounds` | 61,113 | Compound-per-paper appearances (~8,502 unique InChIKeys) |
| `blocks` | 123,727 | PureOrMixtureData + ReactionData blocks |
| `block_properties` | 130,104 | Properties (one per property per block) |
| `block_variables` | 168,687 | Variables (one per variable per block) |

### 7.2 Database File

| Metric | Value |
|--------|-------|
| Database file size | ~1.92 GB |
| Raw JSON stored | ~1.90 GB (verbatim in `papers.json_data`) |
| SQLite version | 3.x |
| Build script | `build_thermoml_sqlite.py` |

### 7.3 Temporal & Content Coverage

| Metric | Value |
|--------|-------|
| Publication year range | ~2003–2019 |
| Number of journals | Major thermodynamic journals (JCED, FPE, JCT, IJT, JSC, ...) |
| DOI prefix distribution | `10.1021/` (ACS), `10.1016/` (Elsevier), `10.1007/` (Springer) |
| Unique compounds (InChIKey) | ~8,502 |
| Unique property names | ~113 (from a vocabulary of 188) |
| Unique standard methods | ~160 |
| Unique custom method strings | ~2,647 |
| Property groups represented | 12 of 13 (BioProperties has minimal presence in v2020 data) |

### 7.4 Block Type Distribution

| Block Type | Count |
|------------|------:|
| PureOrMixtureData | ~122,000 (vast majority) |
| ReactionData | ~1,700 |

---

## 8. Recovery & Reconstruction

### 8.1 Recover the Entire XML Archive from thermoml_raw.db

```python
import sqlite3, os

conn = sqlite3.connect('thermoml_raw.db')
cursor = conn.execute('SELECT file_path, json_data FROM papers')

output_dir = 'recovered_json'
for file_path, json_data in cursor:
    out = os.path.join(output_dir, file_path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w', encoding='utf-8') as f:
        f.write(json_data)
# Produces:
#   recovered_json/10.1007/...
#   recovered_json/10.1016/...
#   recovered_json/10.1021/...
```

### 8.2 Recover a Single Paper

```python
import sqlite3, json

conn = sqlite3.connect('thermoml_raw.db')
row = conn.execute('SELECT json_data FROM papers WHERE doi = ?',
                    ('10.1021/je050342f',)).fetchone()
data = json.loads(row[0])
```

### 8.3 XML File Organization by DOI Prefix

The original archive organizes files by publisher DOI prefix:

```
ThermoML.v2020-09-30.db/
├── 10.1007/                    ← Springer
│   ├── s10765-010-0714-z.json
│   ├── s10765-008-0458-4.json
│   └── ...
├── 10.1016/                    ← Elsevier
│   ├── j.fluid.2016.03.016.json
│   ├── j.jct.2005.03.002.json
│   └── ...
└── 10.1021/                    ← ACS
    ├── je050342f.json
    ├── je060063v.json
    └── ...
```

### 8.4 Rebuild thermoml_raw.db from Original JSON Files

The build script `build_thermoml_sqlite.py` reads all JSON files from the archive
directory and produces the SQLite database:

```python
# Core pattern from build_thermoml_sqlite.py:
import json, os, sqlite3

DB_DIR = "ThermoML.v2020-09-30.db"
OUTPUT = "thermoml_raw.db"

conn = sqlite3.connect(OUTPUT)
conn.executescript(SCHEMA)  # Creates all 5 tables + 9 indexes

for prefix in sorted(os.listdir(DB_DIR)):
    pdir = os.path.join(DB_DIR, prefix)
    if not os.path.isdir(pdir):
        continue
    for fname in sorted(os.listdir(pdir)):
        if fname.endswith(".json"):
            fpath = os.path.join(pdir, fname)
            with open(fpath, encoding="utf-8") as fh:
                raw_json = fh.read()           # read verbatim
            data = json.loads(raw_json)

            # Insert verbatim JSON into papers
            doi = data.get("Citation", {}).get("sDOI", "")
            conn.execute("INSERT INTO papers VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                         (doi, f"{prefix}/{fname}", raw_json, ...))

            # Extract derived indexes into compounds, blocks,
            # block_properties, block_variables
            ...

conn.commit()
```

Key extraction functions:
- **`extract_compounds(data)`** — yields `(org_num, inchi, inchikey, name, formula, cas)` per compound
- **`extract_blocks(data, block_type, blocks_list)`** — yields `(block_row, prop_rows, var_rows)` per block

### 8.5 Determinism Guarantee

Given the same input JSON files, `build_thermoml_sqlite.py` produces a
**functionally identical** database every time because:

1. Files are iterated in sorted order (`sorted(os.listdir(...))`)
2. All source data is deterministically extracted from immutable JSON
3. No random or time-dependent fields in any table
4. `INSERT OR REPLACE` ensures idempotent operation

---

## 9. Database → Card Pipeline

### 9.1 Pipeline Overview

The card generation system reads from `thermoml_raw.db` and produces structured
JSON cards in six schema families. The pipeline is **fully deterministic** — the
same database always produces identical cards.

```
thermoml_raw.db
=================
papers.json_data   ← SINGLE SOURCE OF TRUTH
  |
  +--< compounds   ← derived index
  +--< blocks      ← derived index
  +--< block_properties  ← derived index
  +--< block_variables   ← derived index
       |
       |  Card Generation Scripts
       |  (regenerate_cards_from_db.py, generate_property_cards.py, etc.)
       |
       v
  +----------+----------+----------+----------+----------+----------+
  |   RMS    |  CCS-ID  | CCS-SAM  |   SCS    |   PCS    |  MTDKS   |
  | 11,726   |  8,502   | ~32,730  |  44,630  | ~130,104 |    18    |
  | papers   | compounds| samples  | systems  | prop-    | domain   |
  |          |          |          |          | cards    | knowledge|
  +----------+----------+----------+----------+----------+----------+
```

### 9.2 Which Tables Feed Which Card Types

#### RMS — Reference Metadata Schema (11,726 cards)

```
Source:  papers.json_data → Citation subtree
         + aggregate counts from Compound[], PureOrMixtureData[], ReactionData[]
Method:  Single-pass over papers table
Key:     doi
```

The RMS card extracts bibliographic metadata from `Citation` and computes
a `data_inventory` section by scanning all blocks in the paper for property
names, temperature/pressure ranges, and total data point count.

#### CCS — Component/Compound Card Schema (8,502 ID cards + ~32,730 sample cards)

```
Source:  papers.json_data → Compound subtree
         compounds table → fast InChIKey-based iteration
Method:  Cross-paper aggregation: for each unique InChIKey, collect all
         names, formulas, and sample records across all papers
Key:     InChIKey (ID card), (doi, InChIKey, sample_num) (sample card)
```

The `compounds` table provides fast lookup of which papers contain a given
compound. The full compound data (including `Sample[]` and `purity[]`) is
then extracted from `papers.json_data`.

#### SCS — Systems Card Schema (44,630 cards)

```
Source:  papers.json_data → PureOrMixtureData[].Component[]
         blocks table → fast system enumeration
         compounds table → InChIKey resolution
Method:  Cross-paper aggregation: for each unique sorted set of InChIKeys,
         aggregate all blocks measuring that system
Key:     system_id (sorted InChIKeys joined by '::')
```

The `blocks.component_org_nums` array identifies which compounds appear in
each block. These are resolved to InChIKeys via `compounds`, then sorted
and joined to form the `system_id`.

#### PCS — Property Card Schema (~130,104 cards)

```
Source:  papers.json_data → PureOrMixtureData[block].Property[prop]
                          → PureOrMixtureData[block].Variable[]
                          → PureOrMixtureData[block].Constraint[]
                          → PureOrMixtureData[block].NumValues[]
                          → Compound[] (for compound metadata)
                          → Citation (for paper metadata)
         blocks table → enumerate blocks
         block_properties table → enumerate properties per block
Method:  Per-block-property: one card per (doi, block_type, block_number, prop_number)
Key:     (doi, block_type, block_number, prop_number)
```

Each PCS card contains the complete measurement context for one property
in one block: compound identities, method, phases, variables, constraints,
data points with values and uncertainties, and provenance.

#### MTDKS — Measurement Technique Domain Knowledge Schema (18 cards)

```
Source:  block_properties table → method statistics
         papers.json_data → method detail extraction
Method:  Global aggregation: scan ALL block_properties to build
         12 property-group knowledge cards + 6 cross-cutting cards
Key:     group_name (property groups) or card_type (cross-cutting)
```

The MTDKS cards are reference catalogs, not per-measurement cards. They
aggregate method usage statistics, UFactor encodings, and technique
family relationships across the entire database.

### 9.3 Data Flow: From Raw JSON to Card Fields

```
papers.json_data
│
├─ Citation ────────────────────────────────► RMS card
│  ├─ sDOI ──────────────────────────────────► RMS.doi, PCS.identity.DOI
│  ├─ sTitle ────────────────────────────────► RMS.bibliographic.title
│  ├─ sAuthor[] ─────────────────────────────► RMS.bibliographic.authors
│  ├─ sPubName ──────────────────────────────► RMS.bibliographic.journal
│  └─ yrPubYr ──────────────────────────────► RMS.bibliographic.year
│
├─ Compound[] ──────────────────────────────► CCS cards
│  ├─ sStandardInChIKey ────────────────────► CCS.InChIKey, PCS.compounds[].InChIKey
│  ├─ sCommonName[] ────────────────────────► CCS.names.all_names
│  ├─ sFormulaMolec ────────────────────────► CCS.formula
│  └─ Sample[] ─────────────────────────────► CCS-Sample cards
│     └─ purity[] ──────────────────────────► CCS-Sample.purity_steps[]
│
├─ PureOrMixtureData[] ────────────────────► PCS cards, SCS cards
│  ├─ Component[] ──────────────────────────► PCS.compounds[], SCS.system_id
│  ├─ Property[] ───────────────────────────► PCS.property, MTDKS method stats
│  │  ├─ PropertyGroup.<name>.ePropName ───► PCS.property.name
│  │  ├─ PropertyGroup.<name>.eMethodName ─► PCS.property.method_standard, MTDKS
│  │  ├─ PropertyGroup.<name>.sMethodName ─► PCS.property.method_custom, MTDKS
│  │  └─ PropPhaseID ──────────────────────► PCS.phases.property_phase
│  ├─ Variable[] ───────────────────────────► PCS.variables[]
│  ├─ Constraint[] ─────────────────────────► PCS.constraints[]
│  └─ NumValues[] ──────────────────────────► PCS.data_points[]
│
└─ ReactionData[] ─────────────────────────► PCS cards (reaction type)
   ├─ Participant[] ────────────────────────► PCS.reaction.participants[]
   ├─ Property[] ───────────────────────────► PCS.property
   └─ NumValues[] ──────────────────────────► PCS.data_points[]
```

### 9.4 Card Cardinality Summary

| Card Type | Count | Derives From | Aggregation Level |
|-----------|------:|-------------|-------------------|
| RMS | 11,726 | 1 paper → 1 card | Per-paper |
| CCS-Identity | 8,502 | N papers → 1 card per unique compound | Cross-paper |
| CCS-Sample | ~32,730 | 1 paper, 1 compound → 1 card per sample | Per-paper-compound-sample |
| SCS | 44,630 | N papers → 1 card per unique system | Cross-paper |
| PCS | ~130,104 | 1 block, 1 property → 1 card | Per-block-property |
| MTDKS | 18 | ALL papers → 12+6 knowledge cards | Global aggregate |

---

*End of document.*
