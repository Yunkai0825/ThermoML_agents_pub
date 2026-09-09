# Canonical ThermoML ID CSV schema

This document describes the active `prefixed-v2` CSV contract. Registry IDs
are opaque strings. Consumers must never strip a prefix, cast an ID to an
integer, or accept the retired unscoped syntax.

## Scope grammar

| Scope | Exact forms |
|---|---|
| Global registry | `GLOBlit_N`, `GLOBcomp_N`, `GLOBprop_N`, `GLOBvar_N`, `GLOBconstr_N`, `GLOBmeas_N`, `GLOBphase_N`, `GLOBblocktype_N`, `GLOBrxntype_N`, `GLOBsolvent_N` |
| DOI-local compound | `DOIcomp_N` |
| DOI-local sample | `DOIcompSample_<compound ordinal>_<sample ordinal>` |
| Block | `PROPblock_N` or `RXNblock_N` |
| Block-local declaration | `BLKprop_N`, `BLKvar_N`, `BLKconstr_N` |
| Property uncertainty assessment | `BLKpropAssessment_<property ordinal>_<assessment ordinal>` |

`BLKcomp_N` is not a stored namespace: ThermoML compound declarations belong
to a literature/DOI card and blocks reference their `DOIcomp_N` values.

## CSV files

| File | Exact columns |
|---|---|
| `reference_ids.csv` | `lit_num_id, doi, lit_id, first_author, year, journal, n_compounds, n_blocks, total_datapoints` |
| `compound_ids.csv` | `comp_num_id, comp_id, inchi_key, common_name, formula, smiles, standard_inchi, n_papers` |
| `property_ids.csv` | `prop_num_id, prop_id, prop_name, prop_group, comp_id_linked, n_blocks` |
| `variable_ids.csv` | `var_num_id, var_id, var_name, var_type_key, comp_id_linked, n_blocks` |
| `constraint_ids.csv` | `constr_num_id, constr_id, constr_name, constr_type_key, comp_id_linked, n_blocks` |
| `measurement_ids.csv` | `meas_num_id, meas_id, method_name, method_type, n_blocks, n_aliases` |
| `measurement_aliases.csv` | `source_method_name, source_method_type, meas_num_id, meas_id, n_blocks` |
| `phase_ids.csv` | `phase_num_id, phase_id, phase_name, n_occurrences` |
| `block_types.csv` | `blocktype_num_id, block_type, system_type, n_blocks` |
| `reaction_type_ids.csv` | `rxn_type_num_id, rxn_type_id, rxn_type_name, n_blocks` |
| `solvent_components.csv` | `solvent_num_id, comp_num_id, inchi_key, common_name, formula, n_blocks_as_solvent` |

Every `*_num_id` column contains its exact `GLOB*` value. Frequency/count
columns remain numeric because they are data, not identifiers.

## Component-linked type IDs

Global property, variable, and constraint templates use the literal
`{DOIcomp_id}` placeholder, for example `mole_fraction_{DOIcomp_id}`.
Within a card it resolves to a DOI-local occurrence such as
`mole_fraction_DOIcomp_2`; the declaration separately retains its global type
ID such as `GLOBvar_2`.

## Contract enforcement

Writers use `ThermoML_raw_json_to_card_db_parsers.id_schema`. Public search
interfaces accept human-readable search values or exact global IDs and return
`ID_REFINEMENT_REQUIRED` for bare ordinals, wrong-scope IDs, or retired forms.
There is no compatibility conversion.
