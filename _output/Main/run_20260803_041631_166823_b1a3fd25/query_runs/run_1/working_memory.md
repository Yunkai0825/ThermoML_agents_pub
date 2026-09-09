# Working Memory

## ID Catalog
<!-- PROTECTED — never compacted. Auto-populated by catalog ops. -->
### Resolved Entities
| type | global_id | registry_id | name |
|------|--------|----|------|
| comp | GLOBcomp_1 | water | water |
| comp | GLOBcomp_1586 | FeSO4 | iron(II) sulfate |
| prop | GLOBprop_1 | density | Mass density |
| prop | GLOBprop_4 | viscosity | Viscosity (dynamic) |
| prop | GLOBprop_13 | surface_tension | Surface tension (liquid-gas) |
| prop | GLOBprop_18 | conductivity | Electrical conductivity |
| prop | GLOBprop_37 | molar_conductivity | Molar conductivity |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find all data blocks containing iron(II) sulfate (GLOBcomp_1586) and water (GLOBcomp_1) with properties: density (GLOBpr → stored as L1_query_1

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
{
  "answer": "A comprehensive search of the ThermoML database for data blocks containing iron(II) sulfate (FeSO₄, GLOBcomp_1586) and water (GLOBcomp_1) yielded very limited results for the five target transport/physical properties. Iron(II) sulfate appears in only 3 data blocks across 3 publications in the entire database:\n\n**Matching block (target property found):**\n\n1. **Electrical conductivity (GLOBprop_18)**\n   - DOI: 10.1021/je101012n (GLOBlit_9386)\n   - Block: PROPblock_30\n   - System: binary (FeSO₄ + H₂O)\n   - Temperature range: 278.1–363.15 K\n   - Data points: 33\n\n**Non-matching blocks (property not among the five targets):**\n\n2. **Solubility as molality (GLOBprop_21)** — not a target property\n   - DOI: 10.1016/j.jct.2016.07.006 (GLOBlit_4745)\n   - Block: PROPblock_1\n   - System: ternary (FeSO₄ + H₂SO₄ + H₂O)\n   - Temperature: 298.15 K (fixed)\n   - Data points: 6\n\n3. **Solubility as molality (GLOBprop_21)** — not a target property\n   - DOI: 10.1021/acs.jced.6b00783 (GLOBlit_7012)\n   - Block: PROPblock_1\n   - System: ternary (FeSO₄ + HCl + H₂O)\n   - Temperature range: 293.15–313.15 K\n   - Data points: 55\n\n**Summary for the five requested properties:**\n\n| Property | GLOBprop | Blocks found |\n|----------|----------|-------------|\n| Mass density | GLOBprop_1 | 0 |\n| Dynamic viscosity | GLOBprop_4 | 0 |\n| Surface tension | GLOBprop_13 | 0 |\n| Electrical conductivity | GLOBprop_18 | 1 (PROPblock_30, GLOBlit_9386) |\n| Molar conductivity | GLOBprop_37 | 0 |\n\nOnly **one block** matches the search criteria: electrical conductivity of the binary FeSO₄ + H₂O system from DOI 10.1021/je101012n, with 33 data points spanning 278.1–363.15 K. No density, viscosity, surface tension, or molar conductivity data for aqueous iron(II) sulfate solutions were found in the ThermoML database.",
  "core_claims": [
    "In the ThermoML database, iron(II) sulfate (FeSO₄) with water appears in only 3 data blocks across 3 publications.",
    "Of the five target transport/physical properties searched (mass density, dynamic viscosity, surface tension, electrical conductivity, and molar conductivity), only electrical conductivity has available data for aqueous FeSO₄ solutions.",
    "The single matching block for electrical conductivity (PROPblock_30, DOI 10.1021/je101012n) covers the binary FeSO₄ + H₂O system with 33 data points spanning 278.1–363.15 K.",
    "No mass density, dynamic viscosity, surface tension, or molar conductivity data for aqueous iron(II) sulfate solutions were found in the ThermoML database.",
    "The two remaining blocks containing FeSO₄ report solubility as molality for ternary systems (FeSO₄ + H₂SO₄ + H₂O and FeSO₄ + HCl + H₂O), which were not among the five target properties."
  ],
  "status": "success",
  "summary": "A search of the ThermoML database for iron(II) sulfate (FeSO₄, GLOBcomp_1586) with water (GLOBcomp_1) across five target transport/physical properties found only one matching block. Electrical conductivity (GLOBprop_18) data exist in PROPblock_30 from DOI 10.1021/je101012n (GLOBlit_9386), covering the binary FeSO₄ + H₂O system with 33 data points over 278.1–363.15 K. No data were found for mass density (GLOBprop_1), dynamic viscosity (GLOBprop_4), surface tension (GLOBprop_13), or molar conductivity (GLOBprop_37). Two other blocks containing FeSO₄ report only solubility (GLOBprop_21) in ternary systems and do not match the target properties.",
  "core_id_updates": [],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_9386",
      "block_number": "PROPblock_30",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_1586",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_18"
      ],
      "description": "Electrical conductivity of binary FeSO4 + H2O system. 33 data points, temperature range 278.1–363.15 K. DOI: 10.1021/je101012n. This is the only block among the 3 blocks containing GLOBcomp_1586 that measures one of the five target properties (GLOBprop_1, GLOBprop_4, GLOBprop_13, GLOBprop_18, GLOBprop_37). The other two blocks (GLOBlit_4745/PROPblock_1 and GLOBlit_7012/PROPblock_1) measure solubility as molality (GLOBprop_21) in ternary systems and do not match the target property criteria.",
      "doi": "10.1021/je101012n",
      "lit_id": "2011-mcc--0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 33,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_31",
          "comp_num_id": "GLOBcomp_1586",
          "name": "iron(II) sulfate",
          "formula": "FeO4S",
          "inchi_key": "BAUYGSIQEAFULO-UHFFFAOYSA-L",
          "SMILES": null,
          "sample_num": "DOIcompSample_31_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_2_1"
        }
      ],
      "solvents": [
        {
          "component_org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_1",
          "solvent_num_id": "GLOBsolvent_1",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N"
        }
      ],
      "constraints": [
        {
          "BLKconstr_id": "BLKconstr_1",
          "constr_num_id": "GLOBconstr_1",
          "constr_id": "pressure_kpa",
          "name": "Pressure, kPa",
          "type": "ePressure",
          "value": 101.0,
          "digits": 3,
          "component_org_num": null,
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          }
        }
      ],
      "variables": [
        {
          "BLKvar_id": "BLKvar_1",
          "var_num_id": "GLOBvar_1",
          "var_id": "temperature_k",
          "name": "Temperature, K",
          "type": "eTemperature",
          "component_org_num": null,
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_1",
            "name": "Temperature, K",
            "min": 278.1,
            "max": 363.15,
            "n_unique": 7
          },
          "range_min": 278.1,
          "range_max": 363.15
        },
        {
          "BLKvar_id": "BLKvar_2",
          "var_num_id": "GLOBvar_4",
          "var_id": "molality_mol_kg_DOIcomp_31",
          "name": "Molality, mol/kg",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_31",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_2",
            "name": "Molality, mol/kg",
            "min": 0.00112,
            "max": 0.2576,
            "n_unique": 5
          },
          "range_min": 0.00112,
          "range_max": 0.2576
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_18",
          "prop_ID": "electrical_conductivity_s_m",
          "name": "Electrical conductivity, S/m",
          "group": "TransportProp",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_14",
          "meas_ID": "alternating_current_cell_with_electrodes",
          "method_standard": "Alternating current cell with electrodes",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Electrical conductivity, S/m",
            "min": 0.06212,
            "max": 4.11,
            "mean": 0.670357,
            "std": 1.067538,
            "n": 33
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.06212,
          "range_max": 4.11
        }
      ],
      "phases": [
        {
          "owner_id": "BLKprop_1",
          "role": "property_phase",
          "phase": "Liquid",
          "phase_num_id": "GLOBphase_1",
          "phase_id": "liquid"
        },
        {
          "owner_id": "BLKvar_1",
          "role": "phase",
          "phase": "Liquid",
          "phase_num_id": "GLOBphase_1",
          "phase_id": "liquid"
        },
        {
          "owner_id": "BLKvar_2",
          "role": "phase",
          "phase": "Liquid",
          "phase_num_id": "GLOBphase_1",
          "phase_id": "liquid"
        },
        {
          "owner_id": "BLKconstr_1",
          "role": "phase",
          "phase": "Liquid",
          "phase_num_id": "GLOBphase_1",
          "phase_id": "liquid"
        }
      ],
      "reaction_type": null,
      "participants": [],
      "notes": null,
      "declared_system_type": "binary",
      "declared_n_components": 2,
      "declared_compounds": [
        {
          "org_num": "DOIcomp_31",
          "comp_num_id": "GLOBcomp_1586",
          "name": "iron(II) sulfate",
          "formula": "FeO4S",
          "inchi_key": "BAUYGSIQEAFULO-UHFFFAOYSA-L",
          "SMILES": null,
          "sample_num": "DOIcompSample_31_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_2_1"
        }
      ],
      "parent_n_datapoints": 33,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ]
}

