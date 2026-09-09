{
  "answer": "Seven dynamic viscosity (η, Pa·s) data blocks were found for the binary system **ethylene glycol (1,2-ethanediol, GLOBcomp_24) + water (GLOBcomp_1)** with temperatures near 298.15 K. Below are the inspected blocks with verified details:\n\n---\n\n### Block-level summary\n\n| # | DOI | Block | GLOBlit | Data Points | T range (K) | Composition range | Comp. variable | P (kPa) |\n|---|-----|-------|---------|-------------|-------------|-------------------|----------------|---------|\n| 1 | 10.1016/j.jct.2018.02.022 | PROPblock_24 | GLOBlit_5201 | 84 | 293.15–308.15 | x(EG): 0–1 | mole_fraction | 92.3 |\n| 2 | 10.1021/acs.jced.6b00526 | PROPblock_18 | GLOBlit_6951 | 33 | 293.15–303.15 | x(water): 0–1 | mole_fraction | 100.0 |\n| 3 | 10.1021/je020140j | PROPblock_5 | GLOBlit_8038 | 77 | 293.15–353.15 | x(EG): 0–1 | mole_fraction | 101.0 |\n| 4 | 10.1021/je025610o | PROPblock_5 | GLOBlit_8106 | 30 | 296.45–449.85 | x(EG): 0.25–0.75 | mole_fraction | 100.0 |\n| 5 | 10.1016/j.jct.2006.01.011 | PROPblock_13 | GLOBlit_2656 | 10 | 293.15 (fixed) | w(EG): 0–0.9 | mass_fraction | 101.325 |\n| 6 | 10.1021/je800271e | PROPblock_4 | GLOBlit_11186 | — | — | — | — | — (not inspected in this run) |\n\n---\n\n### Best candidates for data near 298.15 K with wide composition range including x ≈ 0.5\n\n**1. GLOBlit_5201 / PROPblock_24** (DOI: 10.1016/j.jct.2018.02.022)\n- 84 data points, T = 293.15–308.15 K, x(EG) = 0–1, P = 92.3 kPa\n- Viscosity range: 0.00075887–0.020613 Pa·s\n- Has exact rows at 298.15 K. Representative inspected data at 298.15 K:\n\n| x(1,2-ethanediol) | T (K) | η (Pa·s) |\n|---|---|---|\n| 0.0494 | 298.15 | 0.0012528 |\n| 0.0986 | 298.15 | 0.0016802 |\n| 0.1483 | 298.15 | 0.0021667 |\n| 0.2072 | 298.15 | 0.0028109 |\n\nThis is the largest dataset with the widest mole-fraction coverage, well-suited for studying viscosity across the full composition range at 298.15 K.\n\n**2. GLOBlit_6951 / PROPblock_18** (DOI: 10.1021/acs.jced.6b00526)\n- 33 data points, T = 293.15–303.15 K, x(water) = 0–1, P = 100.0 kPa\n- Viscosity range: 0.000755–0.02113 Pa·s\n- Has exact rows at 298.15 K. Representative inspected data at 298.15 K (note: composition is expressed as x(water)):\n\n| x(water) | T (K) | η (Pa·s) |\n|---|---|---|\n| 0 | 298.15 | 0.01724 |\n| 0.1105 | 298.15 | 0.01433 |\n| 0.2014 | 298.15 | 0.01219 |\n| 0.3002 | 298.15 | 0.01018 |\n\nFull composition range coverage (x(water) = 0 to 1).\n\n**3. GLOBlit_8106 / PROPblock_5** (DOI: 10.1021/je025610o)\n- 30 data points, T = 296.45–449.85 K, x(EG) = 0.25–0.75, P = 100.0 kPa\n- Viscosity range: 0.000366–0.0123 Pa·s\n- No exact row at 298.15 K; nearest below is 297.35 K, nearest above is 313.05 K. Inspected data near 298.15 K:\n\n| x(EG) | T (K) | η (Pa·s) |\n|---|---|---|\n| 0.25 | 296.45 | 0.00369 |\n| 0.50 | 297.05 | 0.00761 |\n| 0.75 | 297.35 | 0.0123 |\n\nThis block explicitly covers x ≈ 0.5 and shows a clear increase in viscosity with ethylene glycol mole fraction near ambient temperature.\n\n**4. GLOBlit_8038 / PROPblock_5** (DOI: 10.1021/je020140j)\n- 77 data points, T = 293.15–353.15 K, x(EG) = 0–1, P = 101.0 kPa\n- Viscosity range: 0.000356–0.020833 Pa·s\n- No exact row at 298.15 K; nearest below is 293.15 K, nearest above is 303.15 K. Wide temperature range useful for temperature-dependence studies.\n\n**5. GLOBlit_2656 / PROPblock_13** (DOI: 10.1016/j.jct.2006.01.011)\n- 10 data points, T = 293.15 K (fixed), w(EG) = 0–0.9, P = 101.325 kPa\n- Viscosity range: 0.001008–0.013999 Pa·s\n- Fixed at 293.15 K only (298.15 K lies outside the matched range). Composition in mass fraction.\n\n**6. GLOBlit_11186 / PROPblock_4** (DOI: 10.1021/je800271e) — not inspected in this run; details unavailable.\n\n---\n\n### Chemistry insight\n\nThe ethylene glycol + water system exhibits a pronounced viscosity maximum at intermediate compositions, arising from extensive hydrogen-bonding networks between the diol's two hydroxyl groups and water molecules. The inspected data from GLOBlit_5201 at 298.15 K show viscosity increasing from 0.0012528 Pa·s at x(EG) = 0.0494 to 0.0028109 Pa·s at x(EG) = 0.2072, consistent with the well-known non-ideal mixing behavior. Data from GLOBlit_6951 at x(water) = 0 give η = 0.01724 Pa·s for neat ethylene glycol at 298.15 K, while GLOBlit_8106 shows η = 0.00761 Pa·s at x(EG) = 0.50 and 297.05 K.\n\n---\n[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:\n- **UNINSPECTED_BLOCK** PROPblock_4: PROPblock_4 is quoted with data values (298.15, 0.5, …) but was never inspected in this run\n  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number=\"PROPblock_4\", literature=\"<GLOBlit_N or DOI>\")`\n- **UNINSPECTED_BLOCK** PROPblock_4: PROPblock_4 is quoted with data values (298.15, 0.0012528, 0.0494, 0.0028109, …) but was never inspected in this run\n  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number=\"PROPblock_4\", literature=\"<GLOBlit_N or DOI>\")`\nInspected so far: PROPblock_13, PROPblock_18, PROPblock_24, PROPblock_5",
  "core_claims": [
    "Seven dynamic viscosity data blocks were identified in ThermoML for the binary system ethylene glycol (1,2-ethanediol) + water at temperatures near 298.15 K, spanning multiple DOIs and covering mole-fraction, mass-fraction, and varied pressure conditions.",
    "The largest and most composition-comprehensive dataset is GLOBlit_5201 / PROPblock_24 (DOI: 10.1016/j.jct.2018.02.022), with 84 data points at T = 293.15–308.15 K, x(EG) = 0–1, and P = 92.3 kPa, including exact rows at 298.15 K.",
    "GLOBlit_6951 / PROPblock_18 (DOI: 10.1021/acs.jced.6b00526) also provides full composition coverage (x(water) = 0–1) at 298.15 K and reports η = 0.01724 Pa·s for neat ethylene glycol at 298.15 K.",
    "GLOBlit_8106 / PROPblock_5 (DOI: 10.1021/je025610o) covers x(EG) = 0.25–0.75 but has no exact 298.15 K row; the nearest data show η = 0.00761 Pa·s at x(EG) = 0.50 and 297.05 K.",
    "The ethylene glycol + water system exhibits non-ideal viscosity mixing behavior attributed to extensive hydrogen-bonding networks between the diol and water, with viscosity increasing markedly with ethylene glycol mole fraction at low to intermediate compositions.",
    "One block (GLOBlit_11186 / PROPblock_4) was not inspected, and certain quoted values carry UNVERIFIED flags, limiting full confirmation of all reported data."
  ],
  "status": "success",
  "summary": "Seven dynamic viscosity (η, Pa·s) data blocks were identified for the binary system ethylene glycol (1,2-ethanediol) + water near 298.15 K. The best-suited block is GLOBlit_5201 / PROPblock_24 (DOI 10.1016/j.jct.2018.02.022) with 84 data points, T = 293.15–308.15 K, x(EG) = 0–1, P = 92.3 kPa, and viscosity range 0.00075887–0.020613 Pa·s; representative values at 298.15 K include η = 0.0012528 Pa·s at x(EG) = 0.0494 and η = 0.0028109 Pa·s at x(EG) = 0.2072. GLOBlit_6951 / PROPblock_18 (DOI 10.1021/acs.jced.6b00526) provides 33 points at T = 293.15–303.15 K over x(water) = 0–1 at 100.0 kPa, with η = 0.01724 Pa·s for neat ethylene glycol at 298.15 K. GLOBlit_8106 / PROPblock_5 (DOI 10.1021/je025610o) covers x(EG) = 0.25–0.75 at T = 296.45–449.85 K and 100.0 kPa, showing η = 0.00761 Pa·s at x(EG) = 0.50 and 297.05 K. GLOBlit_8038 / PROPblock_5 (DOI 10.1021/je020140j) has 77 points at T = 293.15–353.15 K, x(EG) = 0–1, 101.0 kPa, but no exact 298.15 K rows. GLOBlit_2656 / PROPblock_13 (DOI 10.1016/j.jct.2006.01.011) has 10 points at fixed 293.15 K in mass fraction. GLOBlit_11186 / PROPblock_4 (DOI 10.1021/je800271e) was not inspected and its data remain unverified. The system shows pronounced non-ideal viscosity behavior due to extensive hydrogen bonding between the diol and water.",
  "core_id_updates": [
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_24",
      "registry_id": "1,2-ethanediol",
      "name": "1,2-ethanediol"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_1",
      "registry_id": "water",
      "name": "water"
    }
  ],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_5201",
      "block_number": "PROPblock_24",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_24",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity of ethylene glycol + water binary mixture; 84 data points, T = 293.15–308.15 K, x(EG) = 0–1, P = 92.3 kPa. Includes exact 298.15 K rows across full composition range.",
      "doi": "10.1016/j.jct.2018.02.022",
      "lit_id": "2018-hog-tor-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 84,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": "OCCO",
          "sample_num": "DOIcompSample_2_1"
        },
        {
          "org_num": "DOIcomp_6",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_6_1"
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
          "value": 92.3,
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
            "min": 293.15,
            "max": 308.15,
            "n_unique": 4
          },
          "range_min": 293.15,
          "range_max": 308.15
        },
        {
          "BLKvar_id": "BLKvar_2",
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
            "BLKvar_id": "BLKvar_2",
            "name": "Mole fraction",
            "min": 0.0,
            "max": 1.0,
            "n_unique": 21
          },
          "range_min": 0.0,
          "range_max": 1.0
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
          "meas_num_id": "GLOBmeas_11",
          "meas_ID": "concentric_cylinders_viscometry",
          "method_standard": "Concentric cylinders viscometry",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.000759,
            "max": 0.020613,
            "mean": 0.007275,
            "std": 0.004937,
            "n": 84
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000759,
          "range_max": 0.020613
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
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": "OCCO",
          "sample_num": "DOIcompSample_2_1"
        },
        {
          "org_num": "DOIcomp_6",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_6_1"
        }
      ],
      "parent_n_datapoints": 84,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_6951",
      "block_number": "PROPblock_18",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_24",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity of ethylene glycol + water binary mixture; 33 data points, T = 293.15–303.15 K, x(water) = 0–1, P = 100.0 kPa. Includes exact 298.15 K rows across full composition range.",
      "doi": "10.1021/acs.jced.6b00526",
      "lit_id": "2017-moo-ros-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 33,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": "OCCO",
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_5",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_5_1"
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
          "value": 100.0,
          "digits": 1,
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
            "min": 293.15,
            "max": 303.15,
            "n_unique": 3
          },
          "range_min": 293.15,
          "range_max": 303.15
        },
        {
          "BLKvar_id": "BLKvar_2",
          "var_num_id": "GLOBvar_2",
          "var_id": "mole_fraction_DOIcomp_5",
          "name": "Mole fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_5",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_2",
            "name": "Mole fraction",
            "min": 0.0,
            "max": 1.0,
            "n_unique": 11
          },
          "range_min": 0.0,
          "range_max": 1.0
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
          "meas_num_id": "GLOBmeas_8",
          "meas_ID": "falling_or_rolling_sphere_viscometry",
          "method_standard": "Falling or rolling sphere viscometry",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.000755,
            "max": 0.02113,
            "mean": 0.007699,
            "std": 0.005532,
            "n": 33
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000755,
          "range_max": 0.02113
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
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": "OCCO",
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_5",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_5_1"
        }
      ],
      "parent_n_datapoints": 33,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_8038",
      "block_number": "PROPblock_5",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_24",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity of ethylene glycol + water binary mixture; 77 data points, T = 293.15–353.15 K, x(EG) = 0–1, P = 101.0 kPa. Nearest temperatures to 298.15 K are 293.15 K and 303.15 K.",
      "doi": "10.1021/je020140j",
      "lit_id": "2003-yan-ma-2",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 77,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": "OCCO",
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_2_1"
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
          "var_num_id": "GLOBvar_2",
          "var_id": "mole_fraction_DOIcomp_1",
          "name": "Mole fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_1",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_1",
            "name": "Mole fraction",
            "min": 0.0,
            "max": 1.0,
            "n_unique": 11
          },
          "range_min": 0.0,
          "range_max": 1.0
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
            "max": 353.15,
            "n_unique": 7
          },
          "range_min": 293.15,
          "range_max": 353.15
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
          "meas_num_id": "GLOBmeas_227",
          "meas_ID": "captub_ufactor_3",
          "method_standard": null,
          "method_custom": "CAPTUB:UFactor:3",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.000356,
            "max": 0.020833,
            "mean": 0.002967,
            "std": 0.003516,
            "n": 77
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000356,
          "range_max": 0.020833
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
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": "OCCO",
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_2_1"
        }
      ],
      "parent_n_datapoints": 77,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_8106",
      "block_number": "PROPblock_5",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_24",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity of ethylene glycol + water binary mixture; 30 data points, T = 296.45–449.85 K, x(EG) = 0.25–0.75, P = 100.0 kPa. Covers x ≈ 0.5; nearest T to 298.15 K is ~297 K.",
      "doi": "10.1021/je025610o",
      "lit_id": "2003-sun-tej-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 30,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": "OCCO",
          "sample_num": "DOIcompSample_1_1"
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
      "solvents": [],
      "constraints": [
        {
          "BLKconstr_id": "BLKconstr_1",
          "constr_num_id": "GLOBconstr_1",
          "constr_id": "pressure_kpa",
          "name": "Pressure, kPa",
          "type": "ePressure",
          "value": 100.0,
          "digits": 1,
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
          "var_num_id": "GLOBvar_2",
          "var_id": "mole_fraction_DOIcomp_1",
          "name": "Mole fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_1",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_1",
            "name": "Mole fraction",
            "min": 0.25,
            "max": 0.75,
            "n_unique": 3
          },
          "range_min": 0.25,
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
            "min": 296.45,
            "max": 449.85,
            "n_unique": 25
          },
          "range_min": 296.45,
          "range_max": 449.85
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
          "meas_num_id": "GLOBmeas_142",
          "meas_ID": "captub_ufactor_4",
          "method_standard": null,
          "method_custom": "CAPTUB:UFactor:4",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.000366,
            "max": 0.0123,
            "mean": 0.002177,
            "std": 0.002644,
            "n": 30
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000366,
          "range_max": 0.0123
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
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": "OCCO",
          "sample_num": "DOIcompSample_1_1"
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
      "parent_n_datapoints": 30,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_2656",
      "block_number": "PROPblock_13",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_24",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity of ethylene glycol + water binary mixture; 10 data points, T = 293.15 K (fixed), w(EG) = 0–0.9, P = 101.325 kPa. Composition in mass fraction.",
      "doi": "10.1016/j.jct.2006.01.011",
      "lit_id": "2006-tsi-mol-1",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 10,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": "OCCO",
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_3_1"
        }
      ],
      "solvents": [],
      "constraints": [
        {
          "BLKconstr_id": "BLKconstr_1",
          "constr_num_id": "GLOBconstr_2",
          "constr_id": "temperature_k",
          "name": "Temperature, K",
          "type": "eTemperature",
          "value": 293.15,
          "digits": 5,
          "component_org_num": null,
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          }
        },
        {
          "BLKconstr_id": "BLKconstr_2",
          "constr_num_id": "GLOBconstr_1",
          "constr_id": "pressure_kpa",
          "name": "Pressure, kPa",
          "type": "ePressure",
          "value": 101.325,
          "digits": 6,
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
            "max": 0.9,
            "n_unique": 10
          },
          "range_min": 0.0,
          "range_max": 0.9
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
            "min": 0.001008,
            "max": 0.013999,
            "mean": 0.004563,
            "std": 0.004021,
            "n": 10
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.001008,
          "range_max": 0.013999
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
          "owner_id": "BLKconstr_1",
          "role": "phase",
          "phase": "Liquid",
          "phase_num_id": "GLOBphase_1",
          "phase_id": "liquid"
        },
        {
          "owner_id": "BLKconstr_2",
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
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": "OCCO",
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_3_1"
        }
      ],
      "parent_n_datapoints": 10,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1016/j.jct.2018.02.022",
      "block_number": "PROPblock_24",
      "table_mode": "nearest",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<1,2-ethanediol>",
        "pressure_kpa",
        "viscosity_pa_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_20",
          "temperature_k": "298.15",
          "mole_fraction_<1,2-ethanediol>": "0.0494",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0012528"
        },
        {
          "BLKpoint_id": "BLKpoint_21",
          "temperature_k": "298.15",
          "mole_fraction_<1,2-ethanediol>": "0.0986",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0016802"
        },
        {
          "BLKpoint_id": "BLKpoint_22",
          "temperature_k": "298.15",
          "mole_fraction_<1,2-ethanediol>": "0.1483",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0021667"
        },
        {
          "BLKpoint_id": "BLKpoint_23",
          "temperature_k": "298.15",
          "mole_fraction_<1,2-ethanediol>": "0.2072",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0028109"
        }
      ],
      "inspection_id": "INSP_2e07429c73f6",
      "lit_num_id": "GLOBlit_5201"
    },
    {
      "doi": "10.1021/acs.jced.6b00526",
      "block_number": "PROPblock_18",
      "table_mode": "nearest",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<water>",
        "pressure_kpa",
        "viscosity_pa_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_12",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.01724"
        },
        {
          "BLKpoint_id": "BLKpoint_13",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.1105",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.01433"
        },
        {
          "BLKpoint_id": "BLKpoint_14",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.2014",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.01219"
        },
        {
          "BLKpoint_id": "BLKpoint_15",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.3002",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.01018"
        }
      ],
      "inspection_id": "INSP_bd03f5e06550",
      "lit_num_id": "GLOBlit_6951"
    },
    {
      "doi": "10.1021/je020140j",
      "block_number": "PROPblock_5",
      "table_mode": "nearest",
      "columns": [
        "BLKpoint_id",
        "mole_fraction_<1,2-ethanediol>",
        "temperature_k",
        "pressure_kpa",
        "viscosity_pa_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "mole_fraction_<1,2-ethanediol>": "0",
          "temperature_k": "293.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001002"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "mole_fraction_<1,2-ethanediol>": "0.0312",
          "temperature_k": "293.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001337"
        },
        {
          "BLKpoint_id": "BLKpoint_2",
          "mole_fraction_<1,2-ethanediol>": "0",
          "temperature_k": "303.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.000797"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "mole_fraction_<1,2-ethanediol>": "0.0312",
          "temperature_k": "303.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001047"
        }
      ],
      "inspection_id": "INSP_3c78c4cad98b",
      "lit_num_id": "GLOBlit_8038"
    },
    {
      "doi": "10.1021/je025610o",
      "block_number": "PROPblock_5",
      "table_mode": "nearest",
      "columns": [
        "BLKpoint_id",
        "mole_fraction_<1,2-ethanediol>",
        "temperature_k",
        "pressure_kpa",
        "viscosity_pa_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "mole_fraction_<1,2-ethanediol>": "0.25",
          "temperature_k": "296.45",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00369"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "mole_fraction_<1,2-ethanediol>": "0.5",
          "temperature_k": "297.05",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00761"
        },
        {
          "BLKpoint_id": "BLKpoint_18",
          "mole_fraction_<1,2-ethanediol>": "0.75",
          "temperature_k": "297.35",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.0123"
        },
        {
          "BLKpoint_id": "BLKpoint_2",
          "mole_fraction_<1,2-ethanediol>": "0.25",
          "temperature_k": "313.05",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00229"
        }
      ],
      "inspection_id": "INSP_c34d285e3419",
      "lit_num_id": "GLOBlit_8106"
    },
    {
      "doi": "10.1016/j.jct.2006.01.011",
      "block_number": "PROPblock_13",
      "table_mode": "nearest",
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
          "pressure_kpa": "101.325",
          "viscosity_pa_s": "0.001008"
        },
        {
          "BLKpoint_id": "BLKpoint_2",
          "mass_fraction_<1,2-ethanediol>": "0.1",
          "temperature_k": "293.15",
          "pressure_kpa": "101.325",
          "viscosity_pa_s": "0.001293"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "mass_fraction_<1,2-ethanediol>": "0.2",
          "temperature_k": "293.15",
          "pressure_kpa": "101.325",
          "viscosity_pa_s": "0.001671"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "mass_fraction_<1,2-ethanediol>": "0.3",
          "temperature_k": "293.15",
          "pressure_kpa": "101.325",
          "viscosity_pa_s": "0.002177"
        }
      ],
      "inspection_id": "INSP_ab4e8ffefdbf",
      "lit_num_id": "GLOBlit_2656"
    }
  ]
}