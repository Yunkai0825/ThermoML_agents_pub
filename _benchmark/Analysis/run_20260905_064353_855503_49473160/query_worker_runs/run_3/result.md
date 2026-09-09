{
  "answer": "**GLOBlit_220 PROPblock_1 — Inspection Result**\n\nThis block contains **pure ethanol density data only** — it is **not** ethanol + water mixture data.\n\n**Details:**\n\n| Field | Value |\n|---|---|\n| DOI | 10.1016/j.fluid.2004.11.019 (GLOBlit_220) |\n| Block | PROPblock_1 |\n| System type | Unary (pure component) |\n| Compound | Ethanol (GLOBcomp_2, C₂H₆O) |\n| Property | Mass density (GLOBprop_1), kg/m³ |\n| Phase | Liquid |\n| Temperature range | 298.15–348.15 K (15 points) |\n| Pressure range | 100–40000 kPa (15 points) |\n| Density range | 739.4–815.7 kg/m³ (15 points) |\n| Data points | 15 total (12 shown via RDP) |\n| Composition | None (pure ethanol — no water present) |\n\n**Inspected data (12 of 15 points shown):**\n\n| BLKpoint_id | Temperature (K) | Pressure (kPa) | Mass density (kg/m³) |\n|---|---|---|---|\n| BLKpoint_1 | 298.15 | 100 | 785.7 |\n| BLKpoint_3 | 298.15 | 20000 | 801.9 |\n| BLKpoint_5 | 298.15 | 40000 | 815.7 |\n| BLKpoint_6 | 323.15 | 100 | 763.7 |\n| BLKpoint_7 | 323.15 | 10000 | 773.4 |\n| BLKpoint_8 | 323.15 | 20000 | 782.3 |\n| BLKpoint_10 | 323.15 | 40000 | 797.7 |\n| BLKpoint_11 | 348.15 | 100 | 739.4 |\n| BLKpoint_12 | 348.15 | 10000 | 751.2 |\n| BLKpoint_13 | 348.15 | 20000 | 761.2 |\n| BLKpoint_14 | 348.15 | 30000 | 770.3 |\n| BLKpoint_15 | 348.15 | 40000 | 778.6 |\n\n**Conclusion:** This block does **not** contain ethanol + water binary density data. Although the parent DOI (10.1016/j.fluid.2004.11.019) references ethanol–water mixtures in its title, PROPblock_1 specifically holds only pure ethanol measurements. Other blocks within GLOBlit_220 (e.g., PROPblock_2, PROPblock_3, etc.) should be checked for the binary mixture data.",
  "core_claims": [
    "GLOBlit_220 PROPblock_1 contains pure ethanol density data only, not ethanol + water binary mixture data, despite the parent DOI (10.1016/j.fluid.2004.11.019) referencing ethanol–water mixtures in its title.",
    "The block reports 15 liquid-phase mass density data points for pure ethanol spanning 298.15–348.15 K in temperature, 100–40000 kPa in pressure, and 739.4–815.7 kg/m³ in density.",
    "Other blocks within GLOBlit_220 (e.g., PROPblock_2, PROPblock_3) would need to be checked for binary ethanol + water mixture data."
  ],
  "status": "success",
  "summary": "GLOBlit_220 PROPblock_1 (DOI 10.1016/j.fluid.2004.11.019) contains pure ethanol density data only, not ethanol + water mixture data. The block reports 15 liquid-phase mass density measurements for pure ethanol (C₂H₆O) over 298.15–348.15 K and 100–40000 kPa, with densities ranging from 739.4 to 815.7 kg/m³. No water is present; no composition variable is included. Binary ethanol–water mixture data, if present in this DOI, would be in other blocks (e.g., PROPblock_2, PROPblock_3, etc.).",
  "core_id_updates": [],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_220",
      "block_number": "PROPblock_1",
      "BLKsubsys_id": null,
      "system_type": "unary",
      "comp_num_ids": [
        "GLOBcomp_2"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Pure ethanol mass density measurements at 298.15–348.15 K and 100–40000 kPa, 15 data points, liquid phase. Not ethanol+water binary data.",
      "doi": "10.1016/j.fluid.2004.11.019",
      "lit_id": "2005-pec-dol-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_2",
      "n_datapoints": 15,
      "n_components": 1,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_2_1"
        }
      ],
      "solvents": [],
      "constraints": [],
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
            "min": 298.15,
            "max": 348.15,
            "n_unique": 3
          },
          "range_min": 298.15,
          "range_max": 348.15
        },
        {
          "BLKvar_id": "BLKvar_2",
          "var_num_id": "GLOBvar_3",
          "var_id": "pressure_kpa",
          "name": "Pressure, kPa",
          "type": "ePressure",
          "component_org_num": null,
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_2",
            "name": "Pressure, kPa",
            "min": 100.0,
            "max": 40000.0,
            "n_unique": 5
          },
          "range_min": 100.0,
          "range_max": 40000.0
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_1",
          "prop_ID": "mass_density_kg_m3",
          "name": "Mass density, kg/m3",
          "group": "VolumetricProp",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_138",
          "meas_ID": "vibtub_ufactor_2",
          "method_standard": null,
          "method_custom": "VIBTUB:UFactor:2",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 739.4,
            "max": 815.7,
            "mean": 780.953333,
            "std": 21.489827,
            "n": 15
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 739.4,
          "range_max": 815.7
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
        }
      ],
      "reaction_type": null,
      "participants": [],
      "notes": null,
      "declared_system_type": "unary",
      "declared_n_components": 1,
      "declared_compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_2_1"
        }
      ],
      "parent_n_datapoints": 15,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1016/j.fluid.2004.11.019",
      "block_number": "PROPblock_1",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "pressure_kpa",
        "mass_density_kg_m3"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mass_density_kg_m3": "785.7"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "temperature_k": "298.15",
          "pressure_kpa": "20000",
          "mass_density_kg_m3": "801.9"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "temperature_k": "298.15",
          "pressure_kpa": "40000",
          "mass_density_kg_m3": "815.7"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "temperature_k": "323.15",
          "pressure_kpa": "100",
          "mass_density_kg_m3": "763.7"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "temperature_k": "323.15",
          "pressure_kpa": "10000",
          "mass_density_kg_m3": "773.4"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "temperature_k": "323.15",
          "pressure_kpa": "20000",
          "mass_density_kg_m3": "782.3"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "temperature_k": "323.15",
          "pressure_kpa": "40000",
          "mass_density_kg_m3": "797.7"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "temperature_k": "348.15",
          "pressure_kpa": "100",
          "mass_density_kg_m3": "739.4"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "temperature_k": "348.15",
          "pressure_kpa": "10000",
          "mass_density_kg_m3": "751.2"
        },
        {
          "BLKpoint_id": "BLKpoint_13",
          "temperature_k": "348.15",
          "pressure_kpa": "20000",
          "mass_density_kg_m3": "761.2"
        },
        {
          "BLKpoint_id": "BLKpoint_14",
          "temperature_k": "348.15",
          "pressure_kpa": "30000",
          "mass_density_kg_m3": "770.3"
        },
        {
          "BLKpoint_id": "BLKpoint_15",
          "temperature_k": "348.15",
          "pressure_kpa": "40000",
          "mass_density_kg_m3": "778.6"
        }
      ],
      "inspection_id": "INSP_c620a1344d0d",
      "lit_num_id": "GLOBlit_220"
    }
  ]
}