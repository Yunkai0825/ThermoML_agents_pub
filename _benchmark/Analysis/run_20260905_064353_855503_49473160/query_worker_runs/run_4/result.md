{
  "answer": "**Inspection of GLOBlit_2432 PROPblock_1**\n\nThis block does **not** contain ethanol + water density data. It contains **methanol + water** density data instead.\n\n**Details:**\n\n- **DOI:** 10.1016/j.jct.2004.07.019 (GLOBlit_2432)\n- **Compounds:** water (GLOBcomp_1) + methanol (GLOBcomp_4) — a binary system\n- **Property:** Mass density (kg/m³), measured as density differences relative to pure solvent water, using the vibrating-tube method\n- **Phase:** Liquid\n- **Temperature range:** 298.16–573.15 K\n- **Pressure range:** 390–30320 kPa (high-pressure measurements)\n- **Composition range:** Methanol molality 0.07706–1.04694 mol/kg\n- **Total data points:** 596\n- **Density difference values:** range from −13.3065 to −0.4632 kg/m³ (all negative, indicating methanol solutions are less dense than pure water at the same T and P)\n\nFor example, at 298.16 K and 14450 kPa, the density difference at methanol molality 0.10243 mol/kg is −0.6308 kg/m³ (BLKpoint_1), while at molality 0.98932 mol/kg it is −5.7028 kg/m³ (BLKpoint_6), showing the expected trend of increasing density reduction with higher methanol content.\n\n**Conclusion:** This block is **not** ethanol + water mass density data. The second component is methanol (CH₄O, GLOBcomp_4), not ethanol.",
  "core_claims": [
    "PROPblock_1 of GLOBlit_2432 (DOI 10.1016/j.jct.2004.07.019) contains methanol + water density data, not ethanol + water density data; the second component is methanol (CH₄O, GLOBcomp_4).",
    "The block reports liquid-phase mass density differences (kg/m³) relative to pure water for the methanol + water binary system, covering 298.16–573.15 K, 390–30320 kPa, methanol molality 0.07706–1.04694 mol/kg, with 596 data points.",
    "All reported density difference values are negative (ranging from −13.3065 to −0.4632 kg/m³), indicating that methanol solutions are less dense than pure water at the same temperature and pressure, with the magnitude of the density reduction increasing with higher methanol content."
  ],
  "status": "success",
  "summary": "GLOBlit_2432 PROPblock_1 does not contain ethanol + water density data. It contains methanol + water density data. The DOI is 10.1016/j.jct.2004.07.019. The compounds are water (GLOBcomp_1) and methanol (GLOBcomp_4). The property is mass density (kg/m³), measured as density differences relative to pure water using the vibrating-tube method, in the liquid phase. The temperature range is 298.16–573.15 K, pressure range is 390–30320 kPa, methanol molality range is 0.07706–1.04694 mol/kg, and there are 596 data points. Density difference values range from −13.3065 to −0.4632 kg/m³, all negative, indicating methanol solutions are less dense than pure water at the same T and P. For example, at 298.16 K and 14450 kPa, the density difference at methanol molality 0.10243 mol/kg is −0.6308 kg/m³ and at molality 0.98932 mol/kg is −5.7028 kg/m³. The second component is methanol (CH₄O), not ethanol.",
  "core_id_updates": [],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_2432",
      "block_number": "PROPblock_1",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_4",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density difference measurements for methanol + water at 298.16–573.15 K, 390–30320 kPa, methanol molality 0.07706–1.04694 mol/kg; 596 data points. Not ethanol + water density data.",
      "doi": "10.1016/j.jct.2004.07.019",
      "lit_id": "2004-hyn-hne-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 596,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_5",
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
          "sample_num": "DOIcompSample_5_1"
        },
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_4_1"
        }
      ],
      "solvents": [
        {
          "component_org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_1",
          "solvent_num_id": "GLOBsolvent_1",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N"
        }
      ],
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
            "min": 298.16,
            "max": 573.15,
            "n_unique": 16
          },
          "range_min": 298.16,
          "range_max": 573.15
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
            "min": 390.0,
            "max": 30320.0,
            "n_unique": 32
          },
          "range_min": 390.0,
          "range_max": 30320.0
        },
        {
          "BLKvar_id": "BLKvar_3",
          "var_num_id": "GLOBvar_4",
          "var_id": "molality_mol_kg_DOIcomp_5",
          "name": "Molality, mol/kg",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_5",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_3",
            "name": "Molality, mol/kg",
            "min": 0.07706,
            "max": 1.04694,
            "n_unique": 161
          },
          "range_min": 0.07706,
          "range_max": 1.04694
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
          "meas_num_id": "GLOBmeas_2",
          "meas_ID": "vibrating_tube_method",
          "method_standard": "Vibrating tube method",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": -13.3065,
            "max": -0.4632,
            "mean": -3.693235,
            "std": 2.632762,
            "n": 596
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": -13.3065,
          "range_max": -0.4632
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
          "owner_id": "BLKvar_3",
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
          "org_num": "DOIcomp_5",
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
          "sample_num": "DOIcompSample_5_1"
        },
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_4_1"
        }
      ],
      "parent_n_datapoints": 596,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1016/j.jct.2004.07.019",
      "block_number": "PROPblock_1",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "pressure_kpa",
        "molality_mol_kg_<methanol>",
        "mass_density_kg_m3"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "298.16",
          "pressure_kpa": "14450",
          "molality_mol_kg_<methanol>": "0.10243",
          "mass_density_kg_m3": "-0.6308"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "temperature_k": "298.16",
          "pressure_kpa": "14450",
          "molality_mol_kg_<methanol>": "0.98932",
          "mass_density_kg_m3": "-5.7028"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "temperature_k": "298.16",
          "pressure_kpa": "29990",
          "molality_mol_kg_<methanol>": "0.98931",
          "mass_density_kg_m3": "-5.7779"
        },
        {
          "BLKpoint_id": "BLKpoint_31",
          "temperature_k": "298.16",
          "pressure_kpa": "29990",
          "molality_mol_kg_<methanol>": "0.10243",
          "mass_density_kg_m3": "-0.6295"
        },
        {
          "BLKpoint_id": "BLKpoint_47",
          "temperature_k": "298.24",
          "pressure_kpa": "400",
          "molality_mol_kg_<methanol>": "0.98932",
          "mass_density_kg_m3": "-5.6141"
        },
        {
          "BLKpoint_id": "BLKpoint_57",
          "temperature_k": "298.24",
          "pressure_kpa": "400",
          "molality_mol_kg_<methanol>": "0.07706",
          "mass_density_kg_m3": "-0.4632"
        },
        {
          "BLKpoint_id": "BLKpoint_77",
          "temperature_k": "318.14",
          "pressure_kpa": "390",
          "molality_mol_kg_<methanol>": "0.71144",
          "mass_density_kg_m3": "-4.175"
        },
        {
          "BLKpoint_id": "BLKpoint_82",
          "temperature_k": "318.14",
          "pressure_kpa": "15370",
          "molality_mol_kg_<methanol>": "0.71146",
          "mass_density_kg_m3": "-4.2"
        },
        {
          "BLKpoint_id": "BLKpoint_93",
          "temperature_k": "318.14",
          "pressure_kpa": "390",
          "molality_mol_kg_<methanol>": "0.09689",
          "mass_density_kg_m3": "-0.5893"
        },
        {
          "BLKpoint_id": "BLKpoint_98",
          "temperature_k": "318.14",
          "pressure_kpa": "15370",
          "molality_mol_kg_<methanol>": "0.09689",
          "mass_density_kg_m3": "-0.5958"
        },
        {
          "BLKpoint_id": "BLKpoint_107",
          "temperature_k": "318.15",
          "pressure_kpa": "29980",
          "molality_mol_kg_<methanol>": "0.71149",
          "mass_density_kg_m3": "-4.215"
        },
        {
          "BLKpoint_id": "BLKpoint_113",
          "temperature_k": "318.15",
          "pressure_kpa": "29980",
          "molality_mol_kg_<methanol>": "0.09818",
          "mass_density_kg_m3": "-0.6009"
        },
        {
          "BLKpoint_id": "BLKpoint_123",
          "temperature_k": "338.15",
          "pressure_kpa": "14810",
          "molality_mol_kg_<methanol>": "0.98922",
          "mass_density_kg_m3": "-5.8941"
        },
        {
          "BLKpoint_id": "BLKpoint_130",
          "temperature_k": "338.15",
          "pressure_kpa": "14810",
          "molality_mol_kg_<methanol>": "0.10242",
          "mass_density_kg_m3": "-0.6333"
        },
        {
          "BLKpoint_id": "BLKpoint_141",
          "temperature_k": "338.16",
          "pressure_kpa": "460",
          "molality_mol_kg_<methanol>": "0.98929",
          "mass_density_kg_m3": "-5.9152"
        },
        {
          "BLKpoint_id": "BLKpoint_146",
          "temperature_k": "338.16",
          "pressure_kpa": "30210",
          "molality_mol_kg_<methanol>": "0.71142",
          "mass_density_kg_m3": "-4.2846"
        },
        {
          "BLKpoint_id": "BLKpoint_158",
          "temperature_k": "338.16",
          "pressure_kpa": "460",
          "molality_mol_kg_<methanol>": "0.10243",
          "mass_density_kg_m3": "-0.6372"
        },
        {
          "BLKpoint_id": "BLKpoint_164",
          "temperature_k": "338.16",
          "pressure_kpa": "30210",
          "molality_mol_kg_<methanol>": "0.09688",
          "mass_density_kg_m3": "-0.6051"
        },
        {
          "BLKpoint_id": "BLKpoint_180",
          "temperature_k": "373.17",
          "pressure_kpa": "14890",
          "molality_mol_kg_<methanol>": "0.98915",
          "mass_density_kg_m3": "-6.2575"
        },
        {
          "BLKpoint_id": "BLKpoint_186",
          "temperature_k": "373.17",
          "pressure_kpa": "30120",
          "molality_mol_kg_<methanol>": "1.0111",
          "mass_density_kg_m3": "-6.3192"
        },
        {
          "BLKpoint_id": "BLKpoint_205",
          "temperature_k": "373.17",
          "pressure_kpa": "2090",
          "molality_mol_kg_<methanol>": "0.10241",
          "mass_density_kg_m3": "-0.6788"
        },
        {
          "BLKpoint_id": "BLKpoint_210",
          "temperature_k": "373.17",
          "pressure_kpa": "2090",
          "molality_mol_kg_<methanol>": "0.98918",
          "mass_density_kg_m3": "-6.3363"
        },
        {
          "BLKpoint_id": "BLKpoint_211",
          "temperature_k": "373.17",
          "pressure_kpa": "14890",
          "molality_mol_kg_<methanol>": "0.094",
          "mass_density_kg_m3": "-0.6107"
        },
        {
          "BLKpoint_id": "BLKpoint_217",
          "temperature_k": "373.17",
          "pressure_kpa": "30120",
          "molality_mol_kg_<methanol>": "0.09399",
          "mass_density_kg_m3": "-0.6082"
        },
        {
          "BLKpoint_id": "BLKpoint_234",
          "temperature_k": "408.15",
          "pressure_kpa": "15000",
          "molality_mol_kg_<methanol>": "1.01107",
          "mass_density_kg_m3": "-6.8718"
        },
        {
          "BLKpoint_id": "BLKpoint_240",
          "temperature_k": "408.15",
          "pressure_kpa": "2070",
          "molality_mol_kg_<methanol>": "1.01108",
          "mass_density_kg_m3": "-7.0201"
        },
        {
          "BLKpoint_id": "BLKpoint_247",
          "temperature_k": "408.15",
          "pressure_kpa": "2070",
          "molality_mol_kg_<methanol>": "0.09399",
          "mass_density_kg_m3": "-0.6721"
        },
        {
          "BLKpoint_id": "BLKpoint_252",
          "temperature_k": "408.15",
          "pressure_kpa": "2070",
          "molality_mol_kg_<methanol>": "1.01108",
          "mass_density_kg_m3": "-7.0201"
        },
        {
          "BLKpoint_id": "BLKpoint_253",
          "temperature_k": "408.15",
          "pressure_kpa": "15000",
          "molality_mol_kg_<methanol>": "0.09399",
          "mass_density_kg_m3": "-0.6616"
        },
        {
          "BLKpoint_id": "BLKpoint_271",
          "temperature_k": "408.16",
          "pressure_kpa": "30030",
          "molality_mol_kg_<methanol>": "0.09399",
          "mass_density_kg_m3": "-0.644"
        },
        {
          "BLKpoint_id": "BLKpoint_276",
          "temperature_k": "408.16",
          "pressure_kpa": "30030",
          "molality_mol_kg_<methanol>": "1.01105",
          "mass_density_kg_m3": "-6.7209"
        },
        {
          "BLKpoint_id": "BLKpoint_282",
          "temperature_k": "443.16",
          "pressure_kpa": "30320",
          "molality_mol_kg_<methanol>": "1.01097",
          "mass_density_kg_m3": "-7.1798"
        },
        {
          "BLKpoint_id": "BLKpoint_283",
          "temperature_k": "443.16",
          "pressure_kpa": "30320",
          "molality_mol_kg_<methanol>": "0.09398",
          "mass_density_kg_m3": "-0.6829"
        },
        {
          "BLKpoint_id": "BLKpoint_316",
          "temperature_k": "443.17",
          "pressure_kpa": "2040",
          "molality_mol_kg_<methanol>": "0.09399",
          "mass_density_kg_m3": "-0.7315"
        },
        {
          "BLKpoint_id": "BLKpoint_321",
          "temperature_k": "443.17",
          "pressure_kpa": "2040",
          "molality_mol_kg_<methanol>": "1.01102",
          "mass_density_kg_m3": "-7.6916"
        },
        {
          "BLKpoint_id": "BLKpoint_322",
          "temperature_k": "443.17",
          "pressure_kpa": "14920",
          "molality_mol_kg_<methanol>": "0.09398",
          "mass_density_kg_m3": "-0.7087"
        },
        {
          "BLKpoint_id": "BLKpoint_327",
          "temperature_k": "443.17",
          "pressure_kpa": "14920",
          "molality_mol_kg_<methanol>": "1.01099",
          "mass_density_kg_m3": "-7.4388"
        },
        {
          "BLKpoint_id": "BLKpoint_333",
          "temperature_k": "473.16",
          "pressure_kpa": "2750",
          "molality_mol_kg_<methanol>": "1.01093",
          "mass_density_kg_m3": "-8.3743"
        },
        {
          "BLKpoint_id": "BLKpoint_339",
          "temperature_k": "473.16",
          "pressure_kpa": "15010",
          "molality_mol_kg_<methanol>": "1.0109",
          "mass_density_kg_m3": "-8.0216"
        },
        {
          "BLKpoint_id": "BLKpoint_345",
          "temperature_k": "473.16",
          "pressure_kpa": "30060",
          "molality_mol_kg_<methanol>": "1.01641",
          "mass_density_kg_m3": "-7.7256"
        },
        {
          "BLKpoint_id": "BLKpoint_352",
          "temperature_k": "473.16",
          "pressure_kpa": "15010",
          "molality_mol_kg_<methanol>": "0.10575",
          "mass_density_kg_m3": "-0.8604"
        },
        {
          "BLKpoint_id": "BLKpoint_364",
          "temperature_k": "473.16",
          "pressure_kpa": "2750",
          "molality_mol_kg_<methanol>": "0.09398",
          "mass_density_kg_m3": "-0.7983"
        },
        {
          "BLKpoint_id": "BLKpoint_370",
          "temperature_k": "473.16",
          "pressure_kpa": "15010",
          "molality_mol_kg_<methanol>": "0.10575",
          "mass_density_kg_m3": "-0.8604"
        },
        {
          "BLKpoint_id": "BLKpoint_376",
          "temperature_k": "473.16",
          "pressure_kpa": "30060",
          "molality_mol_kg_<methanol>": "0.10575",
          "mass_density_kg_m3": "-0.8231"
        },
        {
          "BLKpoint_id": "BLKpoint_392",
          "temperature_k": "498.15",
          "pressure_kpa": "15030",
          "molality_mol_kg_<methanol>": "1.01635",
          "mass_density_kg_m3": "-8.6519"
        },
        {
          "BLKpoint_id": "BLKpoint_399",
          "temperature_k": "498.15",
          "pressure_kpa": "30150",
          "molality_mol_kg_<methanol>": "1.01637",
          "mass_density_kg_m3": "-8.1703"
        },
        {
          "BLKpoint_id": "BLKpoint_413",
          "temperature_k": "498.15",
          "pressure_kpa": "30150",
          "molality_mol_kg_<methanol>": "0.10575",
          "mass_density_kg_m3": "-0.8706"
        },
        {
          "BLKpoint_id": "BLKpoint_419",
          "temperature_k": "498.15",
          "pressure_kpa": "3840",
          "molality_mol_kg_<methanol>": "0.10575",
          "mass_density_kg_m3": "-0.9656"
        },
        {
          "BLKpoint_id": "BLKpoint_424",
          "temperature_k": "498.15",
          "pressure_kpa": "3840",
          "molality_mol_kg_<methanol>": "1.0164",
          "mass_density_kg_m3": "-9.112"
        },
        {
          "BLKpoint_id": "BLKpoint_425",
          "temperature_k": "498.15",
          "pressure_kpa": "15030",
          "molality_mol_kg_<methanol>": "0.10574",
          "mass_density_kg_m3": "-0.9218"
        },
        {
          "BLKpoint_id": "BLKpoint_441",
          "temperature_k": "523.14",
          "pressure_kpa": "5880",
          "molality_mol_kg_<methanol>": "1.01632",
          "mass_density_kg_m3": "-9.9531"
        },
        {
          "BLKpoint_id": "BLKpoint_447",
          "temperature_k": "523.14",
          "pressure_kpa": "15600",
          "molality_mol_kg_<methanol>": "1.01629",
          "mass_density_kg_m3": "-9.3473"
        },
        {
          "BLKpoint_id": "BLKpoint_453",
          "temperature_k": "523.14",
          "pressure_kpa": "30090",
          "molality_mol_kg_<methanol>": "1.01627",
          "mass_density_kg_m3": "-8.6936"
        },
        {
          "BLKpoint_id": "BLKpoint_472",
          "temperature_k": "523.14",
          "pressure_kpa": "5880",
          "molality_mol_kg_<methanol>": "0.10574",
          "mass_density_kg_m3": "-1.0594"
        },
        {
          "BLKpoint_id": "BLKpoint_478",
          "temperature_k": "523.14",
          "pressure_kpa": "15600",
          "molality_mol_kg_<methanol>": "0.10574",
          "mass_density_kg_m3": "-0.993"
        },
        {
          "BLKpoint_id": "BLKpoint_484",
          "temperature_k": "523.14",
          "pressure_kpa": "30090",
          "molality_mol_kg_<methanol>": "0.10573",
          "mass_density_kg_m3": "-0.9275"
        },
        {
          "BLKpoint_id": "BLKpoint_495",
          "temperature_k": "548.16",
          "pressure_kpa": "8000",
          "molality_mol_kg_<methanol>": "1.01623",
          "mass_density_kg_m3": "-11.0973"
        },
        {
          "BLKpoint_id": "BLKpoint_501",
          "temperature_k": "548.16",
          "pressure_kpa": "15970",
          "molality_mol_kg_<methanol>": "1.01618",
          "mass_density_kg_m3": "-10.2986"
        },
        {
          "BLKpoint_id": "BLKpoint_507",
          "temperature_k": "548.16",
          "pressure_kpa": "30120",
          "molality_mol_kg_<methanol>": "1.04694",
          "mass_density_kg_m3": "-9.5934"
        },
        {
          "BLKpoint_id": "BLKpoint_526",
          "temperature_k": "548.16",
          "pressure_kpa": "8000",
          "molality_mol_kg_<methanol>": "0.09819",
          "mass_density_kg_m3": "-1.0956"
        },
        {
          "BLKpoint_id": "BLKpoint_532",
          "temperature_k": "548.16",
          "pressure_kpa": "15970",
          "molality_mol_kg_<methanol>": "0.09819",
          "mass_density_kg_m3": "-1.0204"
        },
        {
          "BLKpoint_id": "BLKpoint_537",
          "temperature_k": "548.16",
          "pressure_kpa": "30120",
          "molality_mol_kg_<methanol>": "0.09819",
          "mass_density_kg_m3": "-0.9253"
        },
        {
          "BLKpoint_id": "BLKpoint_548",
          "temperature_k": "573.15",
          "pressure_kpa": "10140",
          "molality_mol_kg_<methanol>": "1.04693",
          "mass_density_kg_m3": "-13.3065"
        },
        {
          "BLKpoint_id": "BLKpoint_554",
          "temperature_k": "573.15",
          "pressure_kpa": "17990",
          "molality_mol_kg_<methanol>": "1.0469",
          "mass_density_kg_m3": "-11.8248"
        },
        {
          "BLKpoint_id": "BLKpoint_567",
          "temperature_k": "573.15",
          "pressure_kpa": "17990",
          "molality_mol_kg_<methanol>": "0.09818",
          "mass_density_kg_m3": "-1.1328"
        },
        {
          "BLKpoint_id": "BLKpoint_579",
          "temperature_k": "573.15",
          "pressure_kpa": "10140",
          "molality_mol_kg_<methanol>": "0.09819",
          "mass_density_kg_m3": "-1.2695"
        },
        {
          "BLKpoint_id": "BLKpoint_585",
          "temperature_k": "573.15",
          "pressure_kpa": "17990",
          "molality_mol_kg_<methanol>": "0.09818",
          "mass_density_kg_m3": "-1.1328"
        },
        {
          "BLKpoint_id": "BLKpoint_591",
          "temperature_k": "573.15",
          "pressure_kpa": "30110",
          "molality_mol_kg_<methanol>": "0.09818",
          "mass_density_kg_m3": "-1.0044"
        },
        {
          "BLKpoint_id": "BLKpoint_596",
          "temperature_k": "573.15",
          "pressure_kpa": "30110",
          "molality_mol_kg_<methanol>": "1.04688",
          "mass_density_kg_m3": "-10.4212"
        }
      ],
      "inspection_id": "INSP_1dc375d4da8a",
      "lit_num_id": "GLOBlit_2432"
    }
  ]
}