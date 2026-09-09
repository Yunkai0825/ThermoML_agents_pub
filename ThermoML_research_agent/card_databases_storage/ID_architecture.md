# ThermoML Identifier Architecture

Single reference for the strict ID grammar used across every generated card,
CSV registry, database, search tool, and agent answer. The authoritative
implementation is
[ThermoML_raw_json_to_card_db_parsers/id_schema.py](../ThermoML_raw_json_to_card_db_parsers/id_schema.py);
this document explains the levels and how they nest. There is **no legacy
compatibility**: retired unscoped forms (`comp_1`, `block_1`, `prop_2`, …) are
rejected everywhere, producers and consumers share one grammar.

---

## 1. Scope hierarchy (top → bottom)

```
Data source (paper)            DOI · lit_id · GLOBlit_N · trc_ref_id
  └── DOI-level compounds      DOIcomp_N  → GLOBcomp_N (+ InChI/SMILES/name)
        └── samples            DOIcompSample_<comp>_<sample>
  └── Data blocks              PROPblock_N | RXNblock_N (+ GLOBblocktype_N, system_type)
        ├── properties         BLKprop_N   → GLOBprop_N   (+ resolved template)
        ├── variables          BLKvar_N    → GLOBvar_N    (+ resolved template)
        ├── constraints        BLKconstr_N → GLOBconstr_N (+ resolved template)
        ├── phases             GLOBphase_N (per column/definition)
        ├── solvents           GLOBsolvent_N (component-linked)
        ├── measurement link   GLOBmeas_N (method used by the block)
        ├── sub-systems        BLKsubsys_N (e.g. binary part of a ternary block)
        └── data points        BLKpoint_N (rows of variable/property columns)
```

## 2. Data-source level

| Field | Example | Scope | Meaning |
|---|---|---|---|
| `doi` | `10.1007/s10765-005-5566-6` | Global | Paper source |
| `lit_id` | `2005-pat-klo-0` | Global | ThermoML literature full ID |
| `lit_num_id` | `GLOBlit_1` | Global | Numeric shortcut for the literature entry |
| `trc_ref_id` | `{year, author1, author2, …}` | Global | TRC reference metadata |

**`GLOBlit_N` is the authoritative citation key.** It is registered in
`Canonicalized_ID_name_lists_csvs/reference_ids.csv` together with its DOI.
Agents cite `GLOBlit_N` first and treat the DOI as the coupled human-readable
form; `attach_lit_num_ids` enriches every registered DOI with its sibling
`lit_num_id`, and `reconcile_literature_identities` repairs or scrubs any
final-answer citation whose DOI disagrees with the registered pair.

## 3. DOI level (per-paper declarations)

| Field | Example | Scope | Meaning |
|---|---|---|---|
| `org_num` → | `DOIcomp_2` | DOI-specific | Compound identity within one paper; mapped to global |
| `comp_num_id` | `GLOBcomp_3` | Global | Compound shared by all papers |
| `standard_inchi`, `smiles`, `name` | `InChI=1S/CO2/c2-1-3`, `O=C=O`, `carbon dioxide` | Global | Chemical identity |
| `sample_num` → | `DOIcompSample_2_1` | DOI-specific | First sample of `DOIcomp_2` |

`BLKcomp_N` deliberately does **not** exist: compound declarations belong to
the paper, and blocks reference the paper's `DOIcomp_N` values.

## 4. Block level

| Field | Example | Scope | Meaning |
|---|---|---|---|
| `block_number` | `PROPblock_1` \| `RXNblock_1` | DOI-specific | Data-table (or reaction) block within a paper |
| `block_type` | `PureOrMixtureData` | Global | Block type full ID |
| `blocktype_num_id` | `GLOBblocktype_1` | Global | Block type numeric ID |
| `system_type` | `binary` | Global | Chemical system type |

A block is addressed globally by the pair **DOI (or `GLOBlit_N`) +
`PROPblock_N`/`RXNblock_N`**.

### Block-local declarations → global registries

Properties, variables, and constraints follow the same three-part pattern:

| Kind | Within-block ID | Global ID | Registry template | Resolved form |
|---|---|---|---|---|
| Constraint | `BLKconstr_1` | `GLOBconstr_55` | `mass_fraction_{DOIcomp_id}` | `mass_fraction_DOIcomp_2` |
| Variable | `BLKvar_3` | `GLOBvar_44` | `molality_mol_kg_{DOIcomp_id}` | `molality_mol_kg_DOIcomp_2` |
| Property | `BLKprop_1` | `GLOBprop_1` | `mole_fraction_{DOIcomp_id}` | `mole_fraction_DOIcomp_2` |

Component-linked types keep a `{DOIcomp_id}` placeholder in the global
template (`component_template_id`); `resolve_component_id` substitutes the
block's actual compound. Each declaration also carries `phase_num_id`
(`GLOBphase_N`) and, for properties, the measurement method (`GLOBmeas_N`)
plus optional `BLKpropAssessment_<prop>_<assessment>` uncertainty entries.

### Block columns and points

| Field | Example | Scope | Meaning |
|---|---|---|---|
| `BLKsubsys_id` | `BLKsubsys_2` | Block-specific | Sub-system of a block (e.g. the binary pair inside a ternary study) |
| `BLKpoint_id` | `BLKpoint_17` | Block-specific | One data point (row) |
| `variable_values` | `(BLKvar_1, BLKvar_3, …)` | Block-specific | Measured variable columns |
| `property_values` | `(BLKprop_1, BLKprop_2, …)` | Block-specific | Measured property columns |

## 5. Measurement level

| Field | Example | Scope | Meaning |
|---|---|---|---|
| `meas_num_id` | `GLOBmeas_41` | Global | Measurement method numeric ID |
| `meas_ID` | `hot_wire_method` | Global | Method full ID |
| `doi` + `block_numbers` | `10.1007/… , (PROPblock_1, PROPblock_2)` | DOI-specific | Blocks that used this method |

Aliases from raw papers map to canonical methods via
`measurement_aliases.csv`.

## 6. Grammar summary (regex-enforced)

| Scope | Exact forms |
|---|---|
| Global registries | `GLOBlit_N`, `GLOBcomp_N`, `GLOBprop_N`, `GLOBvar_N`, `GLOBconstr_N`, `GLOBmeas_N`, `GLOBphase_N`, `GLOBblocktype_N`, `GLOBrxntype_N`, `GLOBsolvent_N` |
| DOI-local compound / sample | `DOIcomp_N`, `DOIcompSample_N_N` |
| Blocks | `PROPblock_N`, `RXNblock_N` |
| Block-local | `BLKprop_N`, `BLKvar_N`, `BLKconstr_N`, `BLKpoint_N`, `BLKsubsys_N` |
| Uncertainty assessment | `BLKpropAssessment_N_N` |
| Retired (rejected) | `lit_N`, `comp_N`, `sample_N`, `block_N`, `prop_N`, `var_N`, `constr_N`, `meas_N`, `phase_N`, `solvent_N` |

`validate_nested_identifiers` walks every tool result, card, and final answer
and raises on any value that violates this grammar; `require_*` constructors
are the only way producers mint IDs.

## 7. Registry CSVs

The canonical name/ID lists live in
[Canonicalized_ID_name_lists_csvs/](Canonicalized_ID_name_lists_csvs/) —
column contracts are specified in
[ThermoML_ids_schema.md](../ThermoML_raw_json_to_card_db_parsers/_index_builder/csv_ids_generation_helper/ThermoML_ids_schema.md).
Every `*_num_id` column stores the exact `GLOB*` string; counts stay numeric.
