{
  "answer": "## Binary Mixture Viscosity Data: Ethylene Glycol + Methanol near 25 °C\n\n**One data block was found** in the ThermoML database containing dynamic viscosity measurements for the binary system 1,2-ethanediol (ethylene glycol) + methanol near 298.15 K.\n\n### Block Summary\n\n| Field | Value |\n|---|---|\n| **DOI** | 10.1016/j.fluid.2009.03.002 |\n| **Literature ID** | GLOBlit_692 |\n| **Block** | PROPblock_1 |\n| **Property** | Dynamic viscosity (GLOBprop_4), Pa·s |\n| **Method** | Capillary tube (Ostwald–Ubbelohde) |\n| **Phase** | Liquid |\n| **System** | Binary (1,2-ethanediol + methanol) |\n| **Temperature range** | 293.15–303.15 K |\n| **Pressure** | 101.0 kPa (fixed constraint) |\n| **Total data points** | 12 |\n| **Composition variable** | Mass fraction of 1,2-ethanediol (0.0–0.75) |\n\n### Data at 298.15 K (4 data points)\n\n| w(1,2-ethanediol) | T (K) | η (Pa·s) |\n|---|---|---|\n| 0.0 | 298.15 | 0.0005436 |\n| 0.25 | 298.15 | 0.0010295 |\n| 0.50 | 298.15 | 0.0020452 |\n| 0.75 | 298.15 | 0.004904 |\n\n### Full Data (all 12 points, all temperatures)\n\n| w(1,2-ethanediol) | T (K) | P (kPa) | η (Pa·s) |\n|---|---|---|---|\n| 0.0 | 293.15 | 101.0 | 0.0005814 |\n| 0.0 | 298.15 | 101.0 | 0.0005436 |\n| 0.0 | 303.15 | 101.0 | 0.0005112 |\n| 0.25 | 293.15 | 101.0 | 0.0011268 |\n| 0.25 | 298.15 | 101.0 | 0.0010295 |\n| 0.25 | 303.15 | 101.0 | 0.0009454 |\n| 0.50 | 293.15 | 101.0 | 0.0022692 |\n| 0.50 | 298.15 | 101.0 | 0.0020452 |\n| 0.50 | 303.15 | 101.0 | 0.0018101 |\n| 0.75 | 293.15 | 101.0 | 0.0057998 |\n| 0.75 | 298.15 | 101.0 | 0.004904 |\n| 0.75 | 303.15 | 101.0 | 0.0042319 |\n\n**Chemistry insight:** The viscosity increases strongly and nonlinearly with ethylene glycol mass fraction — at 298.15 K, the viscosity at w = 0.75 (0.004904 Pa·s) is about 9× that at w = 0.0 (0.0005436 Pa·s), reflecting the extensive hydrogen-bonding network of ethylene glycol (a diol) progressively dominating the mixture's flow resistance. The pure methanol value (0.0005436 Pa·s ≈ 0.54 mPa·s) is consistent with its known low viscosity as a small, mono-hydroxyl solvent. At each composition, viscosity decreases with increasing temperature (e.g., at w = 0.75: 0.0057998 Pa·s at 293.15 K → 0.004904 Pa·s at 298.15 K → 0.0042319 Pa·s at 303.15 K), as expected from the Arrhenius-type temperature dependence of liquid viscosity.",
  "core_claims": [
    "One ThermoML data block (DOI 10.1016/j.fluid.2009.03.002) reports dynamic viscosity for the binary liquid system 1,2-ethanediol + methanol at 101.0 kPa, covering temperatures 293.15–303.15 K and 1,2-ethanediol mass fractions 0.0–0.75, totaling 12 data points measured by capillary tube (Ostwald–Ubbelohde) method.",
    "At 298.15 K, the dynamic viscosity increases strongly and nonlinearly with ethylene glycol mass fraction, from 0.0005436 Pa·s at w = 0.0 to 0.004904 Pa·s at w = 0.75, reflecting the extensive hydrogen-bonding network of the diol progressively dominating flow resistance.",
    "At each composition, viscosity decreases with increasing temperature over the 293.15–303.15 K range, consistent with Arrhenius-type temperature dependence of liquid viscosity."
  ],
  "status": "success",
  "summary": "One ThermoML data block (DOI 10.1016/j.fluid.2009.03.002, GLOBlit_692, PROPblock_1) reports dynamic viscosity (Pa·s) for the binary liquid system 1,2-ethanediol (ethylene glycol) + methanol, measured by capillary tube (Ostwald–Ubbelohde) at 101.0 kPa over 293.15–303.15 K and mass fractions of 1,2-ethanediol from 0.0 to 0.75, totaling 12 data points. At 298.15 K the four reported viscosities are: w = 0.0, η = 0.0005436 Pa·s; w = 0.25, η = 0.0010295 Pa·s; w = 0.50, η = 0.0020452 Pa·s; w = 0.75, η = 0.004904 Pa·s. Viscosity increases strongly and nonlinearly with ethylene glycol content (roughly 9× from w = 0.0 to w = 0.75 at 298.15 K), reflecting the extensive hydrogen-bonding network of the diol. At each composition, viscosity decreases with increasing temperature, consistent with Arrhenius-type behavior.",
  "core_id_updates": [],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_692",
      "block_number": "PROPblock_1",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_4",
        "GLOBcomp_24"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity measurements for the binary mixture 1,2-ethanediol + methanol at 293.15–303.15 K and 101.0 kPa, 12 data points, mass fraction of 1,2-ethanediol 0.0–0.75.",
      "doi": "10.1016/j.fluid.2009.03.002",
      "lit_id": "2009-roy-pra-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 12,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
          "sample_num": "DOIcompSample_2_1"
        },
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": "OCCO",
          "sample_num": "DOIcompSample_1_1"
        }
      ],
      "solvents": [],
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
          "var_num_id": "GLOBvar_5",
          "var_id": "mass_fraction_DOIcomp_1",
          "name": "Mass fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_1",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_1",
            "name": "Mass fraction",
            "min": 0.0,
            "max": 0.75,
            "n_unique": 4
          },
          "range_min": 0.0,
          "range_max": 0.75
        },
        {
          "BLKvar_id": "BLKvar_2",
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
            "BLKvar_id": "BLKvar_2",
            "name": "Temperature, K",
            "min": 293.15,
            "max": 303.15,
            "n_unique": 3
          },
          "range_min": 293.15,
          "range_max": 303.15
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_4",
          "prop_ID": "viscosity_pa_s",
          "name": "Viscosity, Pa*s",
          "group": "TransportProp",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_4",
          "meas_ID": "capillary_tube_ostwald_ubbelohde_method",
          "method_standard": "Capillary tube (Ostwald; Ubbelohde) method",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.000511,
            "max": 0.0058,
            "mean": 0.00215,
            "std": 0.001831,
            "n": 12
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000511,
          "range_max": 0.0058
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
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
          "sample_num": "DOIcompSample_2_1"
        },
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": "OCCO",
          "sample_num": "DOIcompSample_1_1"
        }
      ],
      "parent_n_datapoints": 12,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1016/j.fluid.2009.03.002",
      "block_number": "PROPblock_1",
      "table_mode": "complete",
      "columns": [
        "BLKpoint_id",
        "mass_fraction_<1,2-ethanediol>",
        "temperature_k",
        "pressure_kpa",
        "viscosity_pa_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "mass_fraction_<1,2-ethanediol>": "0",
          "temperature_k": "293.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0005814"
        },
        {
          "BLKpoint_id": "BLKpoint_2",
          "mass_fraction_<1,2-ethanediol>": "0",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0005436"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "mass_fraction_<1,2-ethanediol>": "0",
          "temperature_k": "303.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0005112"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "mass_fraction_<1,2-ethanediol>": "0.25",
          "temperature_k": "293.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0011268"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "mass_fraction_<1,2-ethanediol>": "0.25",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0010295"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "mass_fraction_<1,2-ethanediol>": "0.25",
          "temperature_k": "303.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0009454"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "mass_fraction_<1,2-ethanediol>": "0.5",
          "temperature_k": "293.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0022692"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "mass_fraction_<1,2-ethanediol>": "0.5",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0020452"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "mass_fraction_<1,2-ethanediol>": "0.5",
          "temperature_k": "303.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0018101"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "mass_fraction_<1,2-ethanediol>": "0.75",
          "temperature_k": "293.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0057998"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "mass_fraction_<1,2-ethanediol>": "0.75",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.004904"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "mass_fraction_<1,2-ethanediol>": "0.75",
          "temperature_k": "303.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0042319"
        }
      ],
      "inspection_id": "INSP_1e57024e620c",
      "lit_num_id": "GLOBlit_692"
    }
  ]
}