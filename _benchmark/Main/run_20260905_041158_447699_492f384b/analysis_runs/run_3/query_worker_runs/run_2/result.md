{
  "answer": "## Density Data for Water + Ethanol Binary Mixture at 298.15 K\n\n### Best Candidate Block\n\n**DOI:** 10.1016/j.fluid.2004.11.019  \n**Literature ID:** GLOBlit_220  \n**Block:** PROPblock_2  \n**Property:** Mass density (GLOBprop_1), kg/m³  \n**Compounds:** Water (GLOBcomp_1) + Ethanol (GLOBcomp_2)  \n**System type:** Binary  \n\nThis block contains **810 total data points** across multiple temperatures (298.15–348.15 K) and pressures (100–40000 kPa). At the target conditions of **T = 298.15 K and P = 100 kPa (≈1 atm)**, there are **54 composition points** spanning the full mole fraction range of ethanol from 0.003 to 1.0 — excellent for deriving excess molar volume.\n\n### Representative Data at 298.15 K, 100 kPa\n\n| BLKpoint_id | x(ethanol) | ρ (kg/m³) |\n|---|---|---|\n| BLKpoint_1 | 0.003 | 995.3 |\n| BLKpoint_6 | 0.0184 | 988.4 |\n| BLKpoint_7 | 0.0219 | 987.6 |\n| BLKpoint_9 | 0.0279 | 984.7 |\n| BLKpoint_10 | 0.0315 | 984.0 |\n| BLKpoint_11 | 0.0366 | 981.6 |\n| BLKpoint_14 | 0.0483 | 977.5 |\n| BLKpoint_15 | 0.0516 | 977.1 |\n| BLKpoint_21 | 0.0801 | 968.6 |\n| BLKpoint_24 | 0.0926 | 965.6 |\n| BLKpoint_29 | 0.1296 | 954.9 |\n| BLKpoint_38 | 0.2502 | 918.5 |\n| BLKpoint_40 | 0.3009 | 904.5 |\n| BLKpoint_41 | 0.3500 | 891.9 |\n| BLKpoint_43 | 0.4501 | 868.8 |\n| BLKpoint_44 | 0.4980 | 859.3 |\n| BLKpoint_45 | 0.5501 | 849.5 |\n| BLKpoint_47 | 0.6489 | 832.7 |\n| BLKpoint_48 | 0.6967 | 825.2 |\n| BLKpoint_51 | 0.8484 | 804.4 |\n| BLKpoint_54 | 1.000 | 785.7 |\n\n(Shape-preserving RDP sampling of the 54 matched rows at these conditions; the full block contains additional intermediate compositions.)\n\n### Chemistry Note\n\nThe density decreases monotonically from near-pure water (~995 kg/m³) to pure ethanol (~786 kg/m³). To derive excess molar volume (V^E), one would compute V_mix = (x₁M₁ + x₂M₂)/ρ_mix and subtract the ideal volume V_ideal = x₁V₁* + x₂V₂*, where V_i* = Mᵢ/ρᵢ*. The water–ethanol system is well known for exhibiting negative excess molar volumes (volume contraction upon mixing), reflecting strong hydrogen-bonding interactions between water and ethanol molecules.\n\n### Search Overview\n\nA total of **22 blocks** of mass density data were found for binary water–ethanol systems near 298.15 K (the search used a temperature window up to 300 K). The GLOBlit_220::PROPblock_2 block stands out for its 54 atmospheric-pressure composition points at exactly 298.15 K, providing dense coverage across the full mole fraction range — ideal for accurate V^E derivation.",
  "core_claims": [
    "A ThermoML block (DOI 10.1016/j.fluid.2004.11.019, GLOBlit_220, PROPblock_2) provides mass density data for the water + ethanol binary system with 54 composition points at T = 298.15 K and P = 100 kPa, spanning ethanol mole fractions from 0.003 to 1.0.",
    "At 298.15 K and 100 kPa, the measured density decreases monotonically from approximately 995 kg/m³ near pure water to approximately 786 kg/m³ for pure ethanol.",
    "The water–ethanol system is well known for exhibiting negative excess molar volumes (volume contraction upon mixing), attributed to strong hydrogen-bonding interactions between water and ethanol molecules.",
    "Among 22 blocks of mass density data found for binary water–ethanol systems near 298.15 K, the selected block provides the densest atmospheric-pressure composition coverage across the full mole fraction range."
  ],
  "status": "success",
  "summary": "Density data for the water + ethanol binary mixture at 298.15 K and 100 kPa were identified in DOI 10.1016/j.fluid.2004.11.019 (GLOBlit_220, PROPblock_2). The block contains 810 total data points across multiple temperatures and pressures, with 54 composition points at exactly 298.15 K and 100 kPa spanning ethanol mole fractions from 0.003 to 1.0. Density decreases monotonically from ~995 kg/m³ (near-pure water) to 785.7 kg/m³ (pure ethanol). Representative values include 995.3 kg/m³ at x(ethanol)=0.003, 918.5 kg/m³ at 0.2502, 859.3 kg/m³ at 0.4980, and 785.7 kg/m³ at 1.000. This dataset is suitable for deriving excess molar volume, which is known to be negative for water–ethanol due to hydrogen-bonding-driven volume contraction. Among 22 candidate blocks found for binary water–ethanol density near 298.15 K, this block was selected for its dense full-range composition coverage at atmospheric pressure.",
  "core_id_updates": [],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_220",
      "block_number": "PROPblock_2",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density data for water + ethanol binary mixture at 298.15–348.15 K and 100–40000 kPa; 810 total data points with 54 composition points at 298.15 K and 100 kPa spanning x(ethanol) = 0.003 to 1.0.",
      "doi": "10.1016/j.fluid.2004.11.019",
      "lit_id": "2005-pec-dol-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 810,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_2_1"
        },
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_1_1"
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
        },
        {
          "BLKvar_id": "BLKvar_3",
          "var_num_id": "GLOBvar_2",
          "var_id": "mole_fraction_DOIcomp_2",
          "name": "Mole fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_2",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_3",
            "name": "Mole fraction",
            "min": 0.003,
            "max": 1.0,
            "n_unique": 54
          },
          "range_min": 0.003,
          "range_max": 1.0
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
            "max": 1012.7,
            "mean": 923.644444,
            "std": 66.683257,
            "n": 810
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 739.4,
          "range_max": 1012.7
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
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_2_1"
        },
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_1_1"
        }
      ],
      "parent_n_datapoints": 810,
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
      "block_number": "PROPblock_2",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "pressure_kpa",
        "mole_fraction_<ethanol>",
        "mass_density_kg_m3"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.003",
          "mass_density_kg_m3": "995.3"
        },
        {
          "BLKpoint_id": "BLKpoint_43",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.4501",
          "mass_density_kg_m3": "868.8"
        },
        {
          "BLKpoint_id": "BLKpoint_48",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.6967",
          "mass_density_kg_m3": "825.2"
        },
        {
          "BLKpoint_id": "BLKpoint_54",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "1",
          "mass_density_kg_m3": "785.7"
        },
        {
          "BLKpoint_id": "BLKpoint_55",
          "temperature_k": "298.15",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "0.003",
          "mass_density_kg_m3": "999.8"
        },
        {
          "BLKpoint_id": "BLKpoint_97",
          "temperature_k": "298.15",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "0.4501",
          "mass_density_kg_m3": "874.7"
        },
        {
          "BLKpoint_id": "BLKpoint_102",
          "temperature_k": "298.15",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "0.6967",
          "mass_density_kg_m3": "832.3"
        },
        {
          "BLKpoint_id": "BLKpoint_108",
          "temperature_k": "298.15",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "1",
          "mass_density_kg_m3": "794"
        },
        {
          "BLKpoint_id": "BLKpoint_109",
          "temperature_k": "298.15",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0.003",
          "mass_density_kg_m3": "1004.2"
        },
        {
          "BLKpoint_id": "BLKpoint_151",
          "temperature_k": "298.15",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0.4501",
          "mass_density_kg_m3": "880.4"
        },
        {
          "BLKpoint_id": "BLKpoint_156",
          "temperature_k": "298.15",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0.6967",
          "mass_density_kg_m3": "839"
        },
        {
          "BLKpoint_id": "BLKpoint_162",
          "temperature_k": "298.15",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "1",
          "mass_density_kg_m3": "801.9"
        },
        {
          "BLKpoint_id": "BLKpoint_163",
          "temperature_k": "298.15",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0.003",
          "mass_density_kg_m3": "1008.5"
        },
        {
          "BLKpoint_id": "BLKpoint_199",
          "temperature_k": "298.15",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0.2269",
          "mass_density_kg_m3": "938.7"
        },
        {
          "BLKpoint_id": "BLKpoint_205",
          "temperature_k": "298.15",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0.4501",
          "mass_density_kg_m3": "885.7"
        },
        {
          "BLKpoint_id": "BLKpoint_210",
          "temperature_k": "298.15",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0.6967",
          "mass_density_kg_m3": "845.1"
        },
        {
          "BLKpoint_id": "BLKpoint_216",
          "temperature_k": "298.15",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "1",
          "mass_density_kg_m3": "808.9"
        },
        {
          "BLKpoint_id": "BLKpoint_217",
          "temperature_k": "298.15",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.003",
          "mass_density_kg_m3": "1012.7"
        },
        {
          "BLKpoint_id": "BLKpoint_253",
          "temperature_k": "298.15",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.2269",
          "mass_density_kg_m3": "942.9"
        },
        {
          "BLKpoint_id": "BLKpoint_259",
          "temperature_k": "298.15",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.4501",
          "mass_density_kg_m3": "890.8"
        },
        {
          "BLKpoint_id": "BLKpoint_264",
          "temperature_k": "298.15",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.6967",
          "mass_density_kg_m3": "851"
        },
        {
          "BLKpoint_id": "BLKpoint_270",
          "temperature_k": "298.15",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "1",
          "mass_density_kg_m3": "815.7"
        },
        {
          "BLKpoint_id": "BLKpoint_271",
          "temperature_k": "323.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.003",
          "mass_density_kg_m3": "986.5"
        },
        {
          "BLKpoint_id": "BLKpoint_307",
          "temperature_k": "323.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.2269",
          "mass_density_kg_m3": "905.2"
        },
        {
          "BLKpoint_id": "BLKpoint_313",
          "temperature_k": "323.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.4501",
          "mass_density_kg_m3": "846.7"
        },
        {
          "BLKpoint_id": "BLKpoint_318",
          "temperature_k": "323.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.6967",
          "mass_density_kg_m3": "802.8"
        },
        {
          "BLKpoint_id": "BLKpoint_324",
          "temperature_k": "323.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "1",
          "mass_density_kg_m3": "763.7"
        },
        {
          "BLKpoint_id": "BLKpoint_325",
          "temperature_k": "323.15",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "0.003",
          "mass_density_kg_m3": "990.8"
        },
        {
          "BLKpoint_id": "BLKpoint_361",
          "temperature_k": "323.15",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "0.2269",
          "mass_density_kg_m3": "910.3"
        },
        {
          "BLKpoint_id": "BLKpoint_367",
          "temperature_k": "323.15",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "0.4501",
          "mass_density_kg_m3": "853.3"
        },
        {
          "BLKpoint_id": "BLKpoint_372",
          "temperature_k": "323.15",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "0.6967",
          "mass_density_kg_m3": "810.9"
        },
        {
          "BLKpoint_id": "BLKpoint_378",
          "temperature_k": "323.15",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "1",
          "mass_density_kg_m3": "773.4"
        },
        {
          "BLKpoint_id": "BLKpoint_379",
          "temperature_k": "323.15",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0.003",
          "mass_density_kg_m3": "994.9"
        },
        {
          "BLKpoint_id": "BLKpoint_415",
          "temperature_k": "323.15",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0.2269",
          "mass_density_kg_m3": "915.3"
        },
        {
          "BLKpoint_id": "BLKpoint_421",
          "temperature_k": "323.15",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0.4501",
          "mass_density_kg_m3": "859.7"
        },
        {
          "BLKpoint_id": "BLKpoint_426",
          "temperature_k": "323.15",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0.6967",
          "mass_density_kg_m3": "818.4"
        },
        {
          "BLKpoint_id": "BLKpoint_432",
          "temperature_k": "323.15",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "1",
          "mass_density_kg_m3": "782.3"
        },
        {
          "BLKpoint_id": "BLKpoint_433",
          "temperature_k": "323.15",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0.003",
          "mass_density_kg_m3": "999"
        },
        {
          "BLKpoint_id": "BLKpoint_469",
          "temperature_k": "323.15",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0.2269",
          "mass_density_kg_m3": "920.1"
        },
        {
          "BLKpoint_id": "BLKpoint_475",
          "temperature_k": "323.15",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0.4501",
          "mass_density_kg_m3": "865.7"
        },
        {
          "BLKpoint_id": "BLKpoint_480",
          "temperature_k": "323.15",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0.6967",
          "mass_density_kg_m3": "825.4"
        },
        {
          "BLKpoint_id": "BLKpoint_486",
          "temperature_k": "323.15",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "1",
          "mass_density_kg_m3": "790.3"
        },
        {
          "BLKpoint_id": "BLKpoint_487",
          "temperature_k": "323.15",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.003",
          "mass_density_kg_m3": "1003.1"
        },
        {
          "BLKpoint_id": "BLKpoint_523",
          "temperature_k": "323.15",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.2269",
          "mass_density_kg_m3": "924.7"
        },
        {
          "BLKpoint_id": "BLKpoint_529",
          "temperature_k": "323.15",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.4501",
          "mass_density_kg_m3": "871.3"
        },
        {
          "BLKpoint_id": "BLKpoint_534",
          "temperature_k": "323.15",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.6967",
          "mass_density_kg_m3": "831.9"
        },
        {
          "BLKpoint_id": "BLKpoint_540",
          "temperature_k": "323.15",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "1",
          "mass_density_kg_m3": "797.7"
        },
        {
          "BLKpoint_id": "BLKpoint_541",
          "temperature_k": "348.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.003",
          "mass_density_kg_m3": "973.1"
        },
        {
          "BLKpoint_id": "BLKpoint_575",
          "temperature_k": "348.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.1903",
          "mass_density_kg_m3": "895.8"
        },
        {
          "BLKpoint_id": "BLKpoint_582",
          "temperature_k": "348.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.4034",
          "mass_density_kg_m3": "833.4"
        },
        {
          "BLKpoint_id": "BLKpoint_587",
          "temperature_k": "348.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.6489",
          "mass_density_kg_m3": "785.6"
        },
        {
          "BLKpoint_id": "BLKpoint_594",
          "temperature_k": "348.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "1",
          "mass_density_kg_m3": "739.4"
        },
        {
          "BLKpoint_id": "BLKpoint_595",
          "temperature_k": "348.15",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "0.003",
          "mass_density_kg_m3": "977.5"
        },
        {
          "BLKpoint_id": "BLKpoint_630",
          "temperature_k": "348.15",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "0.1996",
          "mass_density_kg_m3": "898.1"
        },
        {
          "BLKpoint_id": "BLKpoint_636",
          "temperature_k": "348.15",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "0.4034",
          "mass_density_kg_m3": "840.7"
        },
        {
          "BLKpoint_id": "BLKpoint_641",
          "temperature_k": "348.15",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "0.6489",
          "mass_density_kg_m3": "794.6"
        },
        {
          "BLKpoint_id": "BLKpoint_648",
          "temperature_k": "348.15",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "1",
          "mass_density_kg_m3": "751.2"
        },
        {
          "BLKpoint_id": "BLKpoint_649",
          "temperature_k": "348.15",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0.003",
          "mass_density_kg_m3": "981.9"
        },
        {
          "BLKpoint_id": "BLKpoint_683",
          "temperature_k": "348.15",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0.1903",
          "mass_density_kg_m3": "906.5"
        },
        {
          "BLKpoint_id": "BLKpoint_690",
          "temperature_k": "348.15",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0.4034",
          "mass_density_kg_m3": "847.5"
        },
        {
          "BLKpoint_id": "BLKpoint_695",
          "temperature_k": "348.15",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0.6489",
          "mass_density_kg_m3": "802.9"
        },
        {
          "BLKpoint_id": "BLKpoint_702",
          "temperature_k": "348.15",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "1",
          "mass_density_kg_m3": "761.2"
        },
        {
          "BLKpoint_id": "BLKpoint_703",
          "temperature_k": "348.15",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0.003",
          "mass_density_kg_m3": "986.1"
        },
        {
          "BLKpoint_id": "BLKpoint_738",
          "temperature_k": "348.15",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0.1996",
          "mass_density_kg_m3": "908.5"
        },
        {
          "BLKpoint_id": "BLKpoint_744",
          "temperature_k": "348.15",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0.4034",
          "mass_density_kg_m3": "854"
        },
        {
          "BLKpoint_id": "BLKpoint_749",
          "temperature_k": "348.15",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0.6489",
          "mass_density_kg_m3": "810.6"
        },
        {
          "BLKpoint_id": "BLKpoint_756",
          "temperature_k": "348.15",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "1",
          "mass_density_kg_m3": "770.3"
        },
        {
          "BLKpoint_id": "BLKpoint_757",
          "temperature_k": "348.15",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.003",
          "mass_density_kg_m3": "990.1"
        },
        {
          "BLKpoint_id": "BLKpoint_791",
          "temperature_k": "348.15",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.1903",
          "mass_density_kg_m3": "916.4"
        },
        {
          "BLKpoint_id": "BLKpoint_798",
          "temperature_k": "348.15",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.4034",
          "mass_density_kg_m3": "860"
        },
        {
          "BLKpoint_id": "BLKpoint_803",
          "temperature_k": "348.15",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.6489",
          "mass_density_kg_m3": "817.8"
        },
        {
          "BLKpoint_id": "BLKpoint_810",
          "temperature_k": "348.15",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "1",
          "mass_density_kg_m3": "778.6"
        }
      ],
      "inspection_id": "INSP_38392edfd29c",
      "lit_num_id": "GLOBlit_220"
    },
    {
      "doi": "10.1016/j.fluid.2004.11.019",
      "block_number": "PROPblock_2",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "pressure_kpa",
        "mole_fraction_<ethanol>",
        "mass_density_kg_m3"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.003",
          "mass_density_kg_m3": "995.3"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.0184",
          "mass_density_kg_m3": "988.4"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.0219",
          "mass_density_kg_m3": "987.6"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.0279",
          "mass_density_kg_m3": "984.7"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.0315",
          "mass_density_kg_m3": "984"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.0366",
          "mass_density_kg_m3": "981.6"
        },
        {
          "BLKpoint_id": "BLKpoint_14",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.0483",
          "mass_density_kg_m3": "977.5"
        },
        {
          "BLKpoint_id": "BLKpoint_15",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.0516",
          "mass_density_kg_m3": "977.1"
        },
        {
          "BLKpoint_id": "BLKpoint_21",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.0801",
          "mass_density_kg_m3": "968.6"
        },
        {
          "BLKpoint_id": "BLKpoint_24",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.0926",
          "mass_density_kg_m3": "965.6"
        },
        {
          "BLKpoint_id": "BLKpoint_29",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.1296",
          "mass_density_kg_m3": "954.9"
        },
        {
          "BLKpoint_id": "BLKpoint_38",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.2502",
          "mass_density_kg_m3": "918.5"
        },
        {
          "BLKpoint_id": "BLKpoint_40",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.3009",
          "mass_density_kg_m3": "904.5"
        },
        {
          "BLKpoint_id": "BLKpoint_41",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.35",
          "mass_density_kg_m3": "891.9"
        },
        {
          "BLKpoint_id": "BLKpoint_43",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.4501",
          "mass_density_kg_m3": "868.8"
        },
        {
          "BLKpoint_id": "BLKpoint_44",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.498",
          "mass_density_kg_m3": "859.3"
        },
        {
          "BLKpoint_id": "BLKpoint_45",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.5501",
          "mass_density_kg_m3": "849.5"
        },
        {
          "BLKpoint_id": "BLKpoint_47",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.6489",
          "mass_density_kg_m3": "832.7"
        },
        {
          "BLKpoint_id": "BLKpoint_48",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.6967",
          "mass_density_kg_m3": "825.2"
        },
        {
          "BLKpoint_id": "BLKpoint_51",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.8484",
          "mass_density_kg_m3": "804.4"
        },
        {
          "BLKpoint_id": "BLKpoint_54",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "1",
          "mass_density_kg_m3": "785.7"
        }
      ],
      "inspection_id": "INSP_1061f889512c",
      "lit_num_id": "GLOBlit_220"
    }
  ]
}