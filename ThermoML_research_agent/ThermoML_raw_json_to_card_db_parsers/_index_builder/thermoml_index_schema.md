# ThermoML search index schema (`prefixed-v2`)

`card_databases_storage/ThermoML_index.db` is the read-only cross-card search
index. Its IDs use the same strict scope grammar as the generated cards and
canonical CSVs. The current build contains 11,923 literature cards and 123,727
typed blocks.

## Identity model

| Entity | Safe identity / reference |
|---|---|
| Literature | `doi` and `GLOBlit_N` |
| Block | `(doi, PROPblock_N)` or `(doi, RXNblock_N)` |
| DOI compound occurrence | `(doi, DOIcomp_N)` |
| Global compound | `GLOBcomp_N` |
| Block property declaration | `(doi, block_number, BLKprop_N)` |
| Block variable declaration | `(doi, block_number, BLKvar_N)` |
| Block constraint declaration | `(doi, block_number, BLKconstr_N)` |

There is no generic `num_id` column and no `BLKcomp_N` namespace.

## Registry tables

| Table | Exact ID column | Other identity columns |
|---|---|---|
| `ref_index` | `lit_num_id` | `doi, lit_id, file_path` plus citation/count fields |
| `compound_registry` | `comp_num_id` | `comp_id, inchi_key, common_name, formula, smiles, standard_inchi` |
| `prop_registry` | `prop_num_id` | `prop_id, prop_name, prop_group` |
| `var_registry` | `var_num_id` | `var_id, var_name, var_type_key` |
| `constr_registry` | `constr_num_id` | `constr_id, constr_name, constr_type_key` |
| `meas_registry` | `meas_num_id` | `meas_id, method_name, method_type` |
| `meas_alias_registry` | `meas_num_id` | source method fields and canonical `meas_id` |
| `phase_registry` | `phase_num_id` | `phase_id, phase_name` |
| `blocktype_registry` | `blocktype_num_id` | `block_type, system_type` |
| `rxn_type_registry` | `rxn_type_num_id` | `rxn_type_id, rxn_type_name` |
| `solvent_registry` | `solvent_num_id` | global `comp_num_id`, structure/name fields |

## Block tables

| Table | Local/global ID content |
|---|---|
| `block_index` | typed `block_number`, `blocktype_num_id`, and JSON arrays of exact global compound/property/variable/constraint/measurement/solvent IDs |
| `block_compounds` | `org_num=DOIcomp_N`, `comp_num_id=GLOBcomp_N`, and DOI-local `sample_num` |
| `block_properties` | `BLKprop_id`, `prop_num_id`, optional `component_org_num`, global phase IDs, and `assessment_num` |
| `block_measurements` | `BLKprop_id` plus global `meas_num_id` |
| `block_variables` | `BLKvar_id`, global `var_num_id`, optional `component_org_num`, and global phase IDs |
| `block_constraints` | `BLKconstr_id`, global `constr_num_id`, optional `component_org_num`, and global phase IDs |
| `block_reaction` | typed block ID, global reaction-type IDs, and participants encoded with DOI/global IDs |

The human-readable registry databases retain denormalized JSON fields such as
`comp_ids_smiles`, `var_ids_ranges`, and `participants`; their embedded IDs are
also exact `GLOB*` strings.

## Interface rules

- SQL consumers join using the exact typed column for the entity.
- Public tools never cast IDs to integers or infer scope from an ordinal.
- `component_org_num` joins to `block_compounds.org_num`; it is not a global
  compound ID.
- Card paths in `ref_index.file_path` point to the canonical raw-corpus member
  name `<doi>.json`.
- Wrong-scope and retired IDs return an explicit refinement error; no fallback
  scan or alias conversion is performed.
