# thermoml_raw.db — Structure & Recovery Guide

## Overview

`thermoml_raw.db` is a single-file SQLite database that bundles all 11,923 ThermoML
JSON files from `ThermoML.v2020-09-30.db/` into one queryable store.

| Metric               | Value           |
|----------------------|-----------------|
| JSON files ingested  | 11,923          |
| Database file size   | ~1.92 GB        |
| Raw JSON stored      | 1.90 GB (verbatim) |
| SQLite version       | 3.x             |
| Build script         | `build_thermoml_sqlite.py` |

### Zero-Loss Guarantee

Every original JSON file is stored **byte-for-byte** in `papers.json_data`.
The remaining tables (`compounds`, `blocks`, `block_properties`, `block_variables`)
are **derived indexes** — convenience views over the raw JSON for fast SQL queries.
They are never the source of truth; the full JSON always is.

---

## Table Schemas

### 1. `papers` — One row per JSON file (11,923 rows)

This is the **primary table**. It stores the complete, unmodified JSON string
alongside extracted metadata for indexing.

```sql
CREATE TABLE papers (
    doi                TEXT PRIMARY KEY,     -- e.g. '10.1021/je050342f'
    file_path          TEXT NOT NULL UNIQUE,  -- e.g. '10.1021/je050342f.json'
    json_data          TEXT NOT NULL,         -- VERBATIM original JSON string
    md5_checksum       TEXT,                  -- THERMOML_MD5_CHECKSUM from NIST
    n_compounds        INTEGER NOT NULL,      -- len(Compound[])
    n_pure_blocks      INTEGER NOT NULL,      -- len(PureOrMixtureData[])
    n_reaction_blocks  INTEGER NOT NULL,      -- len(ReactionData[])
    title              TEXT,                  -- Citation.sTitle
    year               INTEGER,              -- Citation.yrPubYr
    journal            TEXT,                  -- Citation.sPubName
    first_author       TEXT                   -- Citation.sAuthor[0]
);
```

**Key column — `json_data`**: Contains the exact JSON string read from the original
`.json` file. `json.loads(json_data)` reproduces the original Python dict structure
with zero loss. This is the column you use to recover any card.

**Key column — `md5_checksum`**: The NIST-assigned `THERMOML_MD5_CHECKSUM` value
embedded inside each JSON file. All 11,923 files have this field populated.
This is NOT a checksum we computed — it is the checksum NIST published with
their data release, and it can be used to verify data integrity.

### 2. `compounds` — One row per compound per paper (61,113 rows)

```sql
CREATE TABLE compounds (
    doi                TEXT NOT NULL,         -- FK → papers.doi
    org_num            INTEGER NOT NULL,      -- Compound.RegNum.nOrgNum
    standard_inchi     TEXT,                  -- Compound.sStandardInChI
    standard_inchi_key TEXT,                  -- Compound.sStandardInChIKey
    common_name        TEXT,                  -- Compound.sCommonName[0]
    formula            TEXT,                  -- Compound.sFormulaMolec
    cas_rn             TEXT,                  -- Compound.sCASRegistryNumber
    PRIMARY KEY (doi, org_num)
);
```

### 3. `blocks` — One row per data block (123,727 rows)

Each row maps to one `PureOrMixtureData` or `ReactionData` element.

```sql
CREATE TABLE blocks (
    doi                TEXT NOT NULL,         -- FK → papers.doi
    block_number       INTEGER NOT NULL,      -- nPureOrMixtureDataNumber or nReactionDataNumber
    block_type         TEXT NOT NULL,         -- 'PureOrMixtureData' or 'ReactionData'
    n_components       INTEGER NOT NULL,      -- Number of Component/Participant elements
    component_org_nums TEXT,                  -- JSON array, e.g. '[1, 2]'
    n_properties       INTEGER NOT NULL,      -- len(Property[])
    n_variables        INTEGER NOT NULL,      -- len(Variable[])
    n_constraints      INTEGER NOT NULL,      -- len(Constraint[])
    n_datapoints       INTEGER NOT NULL,      -- len(NumValues[])
    PRIMARY KEY (doi, block_number, block_type)
);
```

### 4. `block_properties` — One row per property per block (130,104 rows)

```sql
CREATE TABLE block_properties (
    doi                TEXT NOT NULL,
    block_number       INTEGER NOT NULL,
    block_type         TEXT NOT NULL,
    prop_number        INTEGER NOT NULL,      -- Property.nPropNumber
    prop_group         TEXT NOT NULL,         -- e.g. 'VolumetricProp'
    prop_name          TEXT NOT NULL,         -- e.g. 'Mass density, kg/m3'
    method_type        TEXT,                  -- 'standard' or 'custom'
    method_name        TEXT,                  -- eMethodName or sMethodName value
    presentation       TEXT,                  -- ePresentation value
    PRIMARY KEY (doi, block_number, block_type, prop_number)
);
```

### 5. `block_variables` — One row per variable per block (168,687 rows)

```sql
CREATE TABLE block_variables (
    doi                TEXT NOT NULL,
    block_number       INTEGER NOT NULL,
    block_type         TEXT NOT NULL,
    var_number         INTEGER NOT NULL,      -- Variable.nVarNumber
    var_type           TEXT NOT NULL,         -- e.g. 'Temperature, K'
    PRIMARY KEY (doi, block_number, block_type, var_number)
);
```

---

## Indexes

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

---

## Relationship Map

```
papers (11,923)
  │
  ├──< compounds (61,113)          FK: compounds.doi → papers.doi
  │
  ├──< blocks (123,727)            FK: blocks.doi → papers.doi
  │     │
  │     ├──< block_properties (130,104)  FK: (doi, block_number, block_type)
  │     │
  │     └──< block_variables (168,687)   FK: (doi, block_number, block_type)
  │
  └── json_data  ← FULL ORIGINAL JSON (source of truth)
```

---

## How to Recover the 1-to-1 JSON Mapping

### Recover a Single File

```python
import sqlite3, json

conn = sqlite3.connect('thermoml_raw.db')
row = conn.execute(
    'SELECT json_data FROM papers WHERE doi = ?',
    ('10.1021/je050342f',)
).fetchone()

# Option A: Write back to disk as the original file
with open('recovered.json', 'w', encoding='utf-8') as f:
    f.write(row[0])

# Option B: Parse into Python dict
data = json.loads(row[0])
```

### Recover by File Path

```python
row = conn.execute(
    'SELECT json_data FROM papers WHERE file_path = ?',
    ('10.1021/je050342f.json',)
).fetchone()
```

### Recover ALL Files (full directory reconstruction)

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
```

This regenerates the exact original directory structure:
```
recovered_json/
  10.1007/
    s10765-005-5566-6.json
    ...
  10.1016/
    j.jct.2005.03.002.json
    ...
  10.1021/
    je050342f.json
    ...
```

### Verify Recovery is Byte-Perfect

Every JSON file has a NIST-assigned MD5 checksum stored in the JSON itself
(`THERMOML_MD5_CHECKSUM`). Additionally, you can verify against the original
files on disk:

```python
import sqlite3, hashlib

conn = sqlite3.connect('thermoml_raw.db')
cursor = conn.execute('SELECT doi, json_data FROM papers')
for doi, json_data in cursor:
    md5 = hashlib.md5(json_data.encode('utf-8')).hexdigest()
    # Compare with original file or store for audit
```

---

## Common Query Patterns

### Find all papers containing a specific compound

```sql
SELECT p.doi, p.title, p.year
FROM papers p
JOIN compounds c ON c.doi = p.doi
WHERE c.standard_inchi_key = 'XLYOFNOQVPJJNP-UHFFFAOYSA-N'  -- water
ORDER BY p.year;
```

### Count data blocks by property name

```sql
SELECT prop_name, COUNT(*) as n_blocks
FROM block_properties
GROUP BY prop_name
ORDER BY n_blocks DESC;
```

### Get all density measurements for ethanol + water

```sql
SELECT p.doi, b.block_number, b.n_datapoints,
       bp.method_name, bp.method_type
FROM block_properties bp
JOIN blocks b ON b.doi = bp.doi
    AND b.block_number = bp.block_number
    AND b.block_type = bp.block_type
JOIN papers p ON p.doi = bp.doi
WHERE bp.prop_name = 'Mass density, kg/m3'
  AND b.component_org_nums LIKE '%[1, 2]%'
  AND EXISTS (
    SELECT 1 FROM compounds c
    WHERE c.doi = p.doi AND c.standard_inchi_key = 'LFQSCWFLJHTTHZ-UHFFFAOYSA-N'
  )
  AND EXISTS (
    SELECT 1 FROM compounds c
    WHERE c.doi = p.doi AND c.standard_inchi_key = 'XLYOFNOQVPJJNP-UHFFFAOYSA-N'
  );
```

### Fetch full JSON and parse a specific block

```python
import sqlite3, json

conn = sqlite3.connect('thermoml_raw.db')
row = conn.execute(
    'SELECT json_data FROM papers WHERE doi = ?',
    ('10.1021/je050342f',)
).fetchone()
data = json.loads(row[0])

block = data['PureOrMixtureData'][0]
for pt in block['NumValues']:
    print(pt['PropertyValue'], pt.get('VariableValue', []))
```

---

## Data Provenance

| Field | Source |
|-------|--------|
| `papers.json_data` | Verbatim content of `ThermoML.v2020-09-30.db/{prefix}/{filename}.json` |
| `papers.md5_checksum` | `THERMOML_MD5_CHECKSUM` value embedded in each JSON by NIST |
| `papers.file_path` | Relative path: `{doi_prefix}/{filename}.json` |
| Index tables | Derived from `json_data` during ingestion — never modified |

**Build command**: `python build_thermoml_sqlite.py`
**Build time**: ~10 minutes on typical hardware (19 files/s)
**Rebuild**: Re-running the script drops and recreates the database from scratch.
