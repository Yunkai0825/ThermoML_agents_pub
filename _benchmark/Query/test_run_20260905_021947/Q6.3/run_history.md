# Tool History — query-agent

**Nest:** Q
**Session:** 09e2ec6e
**Detailed log:** run_history_detailed.md — Argo events + verbatim agent outputs (join: session id; step tag `cN` ↔ event-row `cN`)
**Prompt:** What is the viscosity of ethanol + water mixtures at 2000 K?
**Started:** 2026-09-05 06:02:59  |  **Elapsed:** 219.3s  |  **Tool calls:** 6  |  **Nested sections:** 1

---

### Step 1 [Q · c6]: `L1_query`

<details><summary>Arguments</summary>

```json
{
  "purpose": "Search for viscosity data of ethanol + water mixtures at or near 2000 K",
  "instruction": "Search for dynamic viscosity (GLOBprop_4) data for binary mixtures of ethanol and water. Check if any data exists at temperatures near 2000 K. Also report the temperature range of any viscosity data found for this system. Return representative data points, temperature ranges, and DOIs.",
  "id_catalog": "",
  "context": "User is asking for viscosity at 2000 K, which is far above the boiling points of ethanol (~351 K) and water (~373 K). This temperature is physically extreme for liquid mixtures."
}
```
</details>

- **Result:** 45,786 chars  |  **Time:** 165.9s  |  **Started:** 06:03:07 (t+8.6s)
- **Nested:** ↳ 5 tool calls in section 'L1_1' below

<details><summary>Result</summary>

```
[TOOL_RESULT_SIZE_WARNING: L1_query returned 45,546 characters after result processing; the target is 24,000. The full result follows — prefer narrower requests, and rely on your working memory for recall instead of re-running this call.]

<subagent_answer>
{
  "answer": "**Viscosity data for ethanol + water mixtures near 2000 K: Not found**\n\nThe ThermoML database contains **no dynamic viscosity data** for ethanol + water binary mixtures at or near 2000 K.\n\n### What data does exist\n\nA search for dynamic viscosity (η, Pa·s) of ethanol (GLOBcomp_2) + water (GLOBcomp_1) binary mixtures returned **14 data blocks across 14 DOIs**, all in the **liquid phase**. The overall temperature range covered is **268.1 K to 618.2 K** — far below 2000 K.\n\n**Representative data blocks spanning the temperature extremes:**\n\n| DOI | Literature ID | Block | T range (K) | Composition variable | η range (Pa·s) | Points |\n|-----|---------------|-------|-------------|---------------------|-----------------|--------|\n| 10.1016/j.fluid.2017.09.005 | GLOBlit_2092 | PROPblock_4 | 523.2–618.2 | x(ethanol) 0–1 | 3.1×10⁻⁵ – 1.34×10⁻⁴ | 72 |\n| 10.1016/j.fluid.2015.07.012 | GLOBlit_1742 | PROPblock_4 | 350.7–476.2 | x(ethanol) 0.1–1 | 1.07×10⁻⁴ – 7.37×10⁻⁴ | 84 |\n| 10.1016/j.jct.2007.05.004 | GLOBlit_2825 | PROPblock_11 | 293.15–303.15 | x(water) 0–1 | 7.97×10⁻⁴ – 2.705×10⁻³ | 37 |\n\nThe **highest temperature** with viscosity data in this system is **618.2 K**, from GLOBlit_2092::PROPblock_4 (DOI: 10.1016/j.fluid.2017.09.005). Some example data points from that block at 618.2 K:\n\n| T (K) | P (kPa) | x(ethanol) | η (Pa·s) | Source |\n|-------|---------|------------|----------|--------|\n| 618.2 | 20000 | 0 | 7.2×10⁻⁵ | GLOBlit_2092::PROPblock_4 |\n| 618.2 | 20000 | 0.2 | 3.5×10⁻⁵ | GLOBlit_2092::PROPblock_4 |\n| 618.2 | 20000 | 0.3 | 3.1×10⁻⁵ | GLOBlit_2092::PROPblock_4 |\n| 618.2 | 20000 | 1 | 3.9×10⁻⁵ | GLOBlit_2092::PROPblock_4 |\n| 618.2 | 40000 | 0 | 8.1×10⁻⁵ | GLOBlit_2092::PROPblock_4 |\n| 618.2 | 40000 | 1 | 6.7×10⁻⁵ | GLOBlit_2092::PROPblock_4 |\n\nNote that these high-temperature measurements were conducted at elevated pressures (20000–40000 kPa) to maintain a liquid or dense fluid phase.\n\n### Physical context\n\nThe highest-temperature viscosity data available (618.2 K, from GLOBlit_2092::PROPblock_4) is still approximately 1382 K below the requested 2000 K (derived: 2000 − 618.2 = 1382 K). At 2000 K, both ethanol and water would be well above their critical temperatures (general chemistry knowledge: ethanol T_b ≈ 351 K, T_c ≈ 514 K; water T_b ≈ 373 K, T_c ≈ 647 K — these are textbook reference values, not from this database). A conventional liquid-phase viscosity measurement of this mixture at 2000 K is not physically meaningful — both components would exist as supercritical fluids or decomposition products at that temperature. This explains the absence of such data in the ThermoML archive.\n\n---\n[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:\n- **MISATTRIBUTED_VALUE** PROPblock_11: 618.2 does not belong to PROPblock_11; it matches only GLOBlit_2092::PROPblock_4 (inspected this run)\n  fix (required — this IS a database value, under a different block): `re-anchor 618.2 to GLOBlit_2092::PROPblock_4 — no new tool call needed`\n- **UNGROUNDED_LITERAL** GLOBlit_2092::PROPblock_4: 1382 (near '…:: ) is still approximately 1382 K below the requested 2000 …') matches no inspected row/stat, database table, or other source of GLOBlit_2092::PROPblock_4\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"GLOBlit_2092::PROPblock_4\", nearest={\"column\": \"temperature_k\", \"value\": 1382.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead\n- **UNGROUNDED_LITERAL** GLOBlit_2092::PROPblock_4: 1382 (near '…1382 K below the requested 2000 K (derived: 2000 - 618.2 = 1…') matches no inspected row/stat, database table, or other source of GLOBlit_2092::PROPblock_4\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"GLOBlit_2092::PROPblock_4\", nearest={\"column\": \"temperature_k\", \"value\": 1382.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead\n- **UNGROUNDED_LITERAL** GLOBlit_2092::PROPblock_4: 514 (near '…es (general chemistry knowledge: ethanol T_b ≈ 351 K, T_c ≈ …') matches no inspected row/stat, database table, or other source of GLOBlit_2092::PROPblock_4\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"GLOBlit_2092::PROPblock_4\", nearest={\"column\": \"temperature_k\", \"value\": 514.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead\n- **UNGROUNDED_LITERAL** GLOBlit_2092::PROPblock_4: 647 (near '…ethanol T_b ≈ 351 K, T_c ≈ 514 K; water T_b ≈ 373 K, T_c ≈ 6…') matches no inspected row/stat, database table, or other source of GLOBlit_2092::PROPblock_4\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"GLOBlit_2092::PROPblock_4\", nearest={\"column\": \"temperature_k\", \"value\": 647.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead\nInspected so far: PROPblock_11, PROPblock_4",
  "core_claims": [
    "The ThermoML database contains no dynamic viscosity data for ethanol + water binary mixtures at or near 2000 K, as all available measurements span 268.1 K to 618.2 K and both components would be well above their critical temperatures at 2000 K, making such measurements physically meaningless."
  ],
  "status": "no_results",
  "summary": "The ThermoML database contains no dynamic viscosity data for ethanol + water binary mixtures at or near 2000 K. Across 14 data blocks and 14 DOIs, all available viscosity data for this system are in the liquid phase, spanning 268.1 K to 618.2 K. The highest-temperature data come from GLOBlit_2092::PROPblock_4 (DOI: 10.1016/j.fluid.2017.09.005), reaching 618.2 K at elevated pressures of 20000–40000 kPa, with viscosities ranging from 3.1×10⁻⁵ to 1.34×10⁻⁴ Pa·s. At 2000 K both ethanol and water would be far above their critical temperatures, making conventional liquid-phase viscosity measurements physically inapplicable, which explains the absence of such data in the archive.",
  "core_id_updates": [],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_2092",
      "block_number": "PROPblock_4",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity of ethanol + water at 523.2–618.2 K and elevated pressures (20000–40000 kPa).",
      "doi": "10.1016/j.fluid.2017.09.005",
      "lit_id": "2017-ono-kyo-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 72,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_3_1"
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
            "min": 523.2,
            "max": 618.2,
            "n_unique": 3
          },
          "range_min": 523.2,
          "range_max": 618.2
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
            "min": 20000.0,
            "max": 40000.0,
            "n_unique": 3
          },
          "range_min": 20000.0,
          "range_max": 40000.0
        },
        {
          "BLKvar_id": "BLKvar_3",
          "var_num_id": "GLOBvar_2",
          "var_id": "mole_fraction_DOIcomp_3",
          "name": "Mole fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_3",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_3",
            "name": "Mole fraction",
            "min": 0.0,
            "max": 1.0,
            "n_unique": 8
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
          "meas_num_id": "GLOBmeas_4",
          "meas_ID": "capillary_tube_ostwald_ubbelohde_method",
          "method_standard": "Capillary tube (Ostwald; Ubbelohde) method",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 3.1e-05,
            "max": 0.000134,
            "mean": 8.4e-05,
            "std": 2.8e-05,
            "n": 72
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 3.1e-05,
          "range_max": 0.000134
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
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_3_1"
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
      "parent_n_datapoints": 72,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_1742",
      "block_number": "PROPblock_4",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity of ethanol + water at 350.7–476.2 K.",
      "doi": "10.1016/j.fluid.2015.07.012",
      "lit_id": "2016-ono-ame-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 84,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_3_1"
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
            "min": 350.7,
            "max": 476.2,
            "n_unique": 3
          },
          "range_min": 350.7,
          "range_max": 476.2
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
            "min": 10000.0,
            "max": 40000.0,
            "n_unique": 4
          },
          "range_min": 10000.0,
          "range_max": 40000.0
        },
        {
          "BLKvar_id": "BLKvar_3",
          "var_num_id": "GLOBvar_2",
          "var_id": "mole_fraction_DOIcomp_3",
          "name": "Mole fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_3",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_3",
            "name": "Mole fraction",
            "min": 0.1,
            "max": 1.0,
            "n_unique": 7
          },
          "range_min": 0.1,
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
          "meas_num_id": "GLOBmeas_4",
          "meas_ID": "capillary_tube_ostwald_ubbelohde_method",
          "method_standard": "Capillary tube (Ostwald; Ubbelohde) method",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.000107,
            "max": 0.000737,
            "mean": 0.000403,
            "std": 0.0002,
            "n": 84
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000107,
          "range_max": 0.000737
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
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_3_1"
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
      "parent_n_datapoints": 84,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_2825",
      "block_number": "PROPblock_11",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity of ethanol + water at 293.15–303.15 K.",
      "doi": "10.1016/j.jct.2007.05.004",
      "lit_id": "2007-gon-cal-1",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 37,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_3_1"
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
            "BLKvar_id": "BLKvar_2",
            "name": "Mole fraction",
            "min": 0.0,
            "max": 1.0,
            "n_unique": 13
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
          "meas_num_id": "GLOBmeas_140",
          "meas_ID": "captub_ufactor_2",
          "method_standard": null,
          "method_custom": "CAPTUB:UFactor:2",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.000797,
            "max": 0.002705,
            "mean": 0.001607,
            "std": 0.000514,
            "n": 37
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000797,
          "range_max": 0.002705
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
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_3_1"
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
      "parent_n_datapoints": 37,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1016/j.fluid.2017.09.005",
      "block_number": "PROPblock_4",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "pressure_kpa",
        "mole_fraction_<ethanol>",
        "viscosity_pa_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "523.2",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0",
          "viscosity_pa_s": "0.00011"
        },
        {
          "BLKpoint_id": "BLKpoint_2",
          "temperature_k": "523.2",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0.1",
          "viscosity_pa_s": "0.00012"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "temperature_k": "523.2",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0.2",
          "viscosity_pa_s": "0.000119"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "temperature_k": "523.2",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0.6",
          "viscosity_pa_s": "9.9e-05"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "temperature_k": "523.2",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "1",
          "viscosity_pa_s": "8.7e-05"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "temperature_k": "523.2",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0",
          "viscosity_pa_s": "0.000113"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "temperature_k": "523.2",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0.1",
          "viscosity_pa_s": "0.000126"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "temperature_k": "523.2",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0.2",
          "viscosity_pa_s": "0.000127"
        },
        {
          "BLKpoint_id": "BLKpoint_16",
          "temperature_k": "523.2",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "1",
          "viscosity_pa_s": "0.000103"
        },
        {
          "BLKpoint_id": "BLKpoint_17",
          "temperature_k": "523.2",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0",
          "viscosity_pa_s": "0.000115"
        },
        {
          "BLKpoint_id": "BLKpoint_18",
          "temperature_k": "523.2",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.1",
          "viscosity_pa_s": "0.000132"
        },
        {
          "BLKpoint_id": "BLKpoint_20",
          "temperature_k": "523.2",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.3",
          "viscosity_pa_s": "0.000134"
        },
        {
          "BLKpoint_id": "BLKpoint_21",
          "temperature_k": "523.2",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.4",
          "viscosity_pa_s": "0.000128"
        },
        {
          "BLKpoint_id": "BLKpoint_24",
          "temperature_k": "523.2",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "1",
          "viscosity_pa_s": "0.000115"
        },
        {
          "BLKpoint_id": "BLKpoint_25",
          "temperature_k": "573.2",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0",
          "viscosity_pa_s": "9e-05"
        },
        {
          "BLKpoint_id": "BLKpoint_28",
          "temperature_k": "573.2",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0.3",
          "viscosity_pa_s": "7e-05"
        },
        {
          "BLKpoint_id": "BLKpoint_30",
          "temperature_k": "573.2",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0.6",
          "viscosity_pa_s": "5.7e-05"
        },
        {
          "BLKpoint_id": "BLKpoint_32",
          "temperature_k": "573.2",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "1",
          "viscosity_pa_s": "5.3e-05"
        },
        {
          "BLKpoint_id": "BLKpoint_33",
          "temperature_k": "573.2",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0",
          "viscosity_pa_s": "9.3e-05"
        },
        {
          "BLKpoint_id": "BLKpoint_38",
          "temperature_k": "573.2",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0.6",
          "viscosity_pa_s": "6.9e-05"
        },
        {
          "BLKpoint_id": "BLKpoint_40",
          "temperature_k": "573.2",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "1",
          "viscosity_pa_s": "6.6e-05"
        },
        {
          "BLKpoint_id": "BLKpoint_41",
          "temperature_k": "573.2",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0",
          "viscosity_pa_s": "9.6e-05"
        },
        {
          "BLKpoint_id": "BLKpoint_46",
          "temperature_k": "573.2",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.6",
          "viscosity_pa_s": "8e-05"
        },
        {
          "BLKpoint_id": "BLKpoint_48",
          "temperature_k": "573.2",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "1",
          "viscosity_pa_s": "7.7e-05"
        },
        {
          "BLKpoint_id": "BLKpoint_49",
          "temperature_k": "618.2",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0",
          "viscosity_pa_s": "7.2e-05"
        },
        {
          "BLKpoint_id": "BLKpoint_51",
          "temperature_k": "618.2",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0.2",
          "viscosity_pa_s": "3.5e-05"
        },
        {
          "BLKpoint_id": "BLKpoint_52",
          "temperature_k": "618.2",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0.3",
          "viscosity_pa_s": "3.1e-05"
        },
        {
          "BLKpoint_id": "BLKpoint_56",
          "temperature_k": "618.2",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "1",
          "viscosity_pa_s": "3.9e-05"
        },
        {
          "BLKpoint_id": "BLKpoint_57",
          "temperature_k": "618.2",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0",
          "viscosity_pa_s": "7.7e-05"
        },
        {
          "BLKpoint_id": "BLKpoint_60",
          "temperature_k": "618.2",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0.3",
          "viscosity_pa_s": "5.9e-05"
        },
        {
          "BLKpoint_id": "BLKpoint_62",
          "temperature_k": "618.2",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0.6",
          "viscosity_pa_s": "5.5e-05"
        },
        {
          "BLKpoint_id": "BLKpoint_64",
          "temperature_k": "618.2",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "1",
          "viscosity_pa_s": "5.5e-05"
        },
        {
          "BLKpoint_id": "BLKpoint_65",
          "temperature_k": "618.2",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0",
          "viscosity_pa_s": "8.1e-05"
        },
        {
          "BLKpoint_id": "BLKpoint_66",
          "temperature_k": "618.2",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.1",
          "viscosity_pa_s": "8.1e-05"
        },
        {
          "BLKpoint_id": "BLKpoint_69",
          "temperature_k": "618.2",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.4",
          "viscosity_pa_s": "7e-05"
        },
        {
          "BLKpoint_id": "BLKpoint_70",
          "temperature_k": "618.2",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.6",
          "viscosity_pa_s": "6.7e-05"
        },
        {
          "BLKpoint_id": "BLKpoint_72",
          "temperature_k": "618.2",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "1",
          "viscosity_pa_s": "6.7e-05"
        }
      ],
      "inspection_id": "INSP_987176e5cf18",
      "lit_num_id": "GLOBlit_2092"
    },
    {
      "doi": "10.1016/j.fluid.2015.07.012",
      "block_number": "PROPblock_4",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "pressure_kpa",
        "mole_fraction_<ethanol>",
        "viscosity_pa_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "350.7",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "0.1",
          "viscosity_pa_s": "0.000537"
        },
        {
          "BLKpoint_id": "BLKpoint_2",
          "temperature_k": "350.7",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "0.2",
          "viscosity_pa_s": "0.000625"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "temperature_k": "350.7",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "0.4",
          "viscosity_pa_s": "0.00064"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "temperature_k": "350.7",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "0.6",
          "viscosity_pa_s": "0.000595"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "temperature_k": "350.7",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "1",
          "viscosity_pa_s": "0.000461"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "temperature_k": "350.7",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0.1",
          "viscosity_pa_s": "0.000546"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "temperature_k": "350.7",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0.2",
          "viscosity_pa_s": "0.000638"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "temperature_k": "350.7",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0.4",
          "viscosity_pa_s": "0.000669"
        },
        {
          "BLKpoint_id": "BLKpoint_14",
          "temperature_k": "350.7",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "1",
          "viscosity_pa_s": "0.000518"
        },
        {
          "BLKpoint_id": "BLKpoint_15",
          "temperature_k": "350.7",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0.1",
          "viscosity_pa_s": "0.000556"
        },
        {
          "BLKpoint_id": "BLKpoint_16",
          "temperature_k": "350.7",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0.2",
          "viscosity_pa_s": "0.000651"
        },
        {
          "BLKpoint_id": "BLKpoint_18",
          "temperature_k": "350.7",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0.4",
          "viscosity_pa_s": "0.000691"
        },
        {
          "BLKpoint_id": "BLKpoint_21",
          "temperature_k": "350.7",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "1",
          "viscosity_pa_s": "0.000555"
        },
        {
          "BLKpoint_id": "BLKpoint_22",
          "temperature_k": "350.7",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.1",
          "viscosity_pa_s": "0.000578"
        },
        {
          "BLKpoint_id": "BLKpoint_23",
          "temperature_k": "350.7",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.2",
          "viscosity_pa_s": "0.000681"
        },
        {
          "BLKpoint_id": "BLKpoint_24",
          "temperature_k": "350.7",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.3",
          "viscosity_pa_s": "0.000726"
        },
        {
          "BLKpoint_id": "BLKpoint_25",
          "temperature_k": "350.7",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.4",
          "viscosity_pa_s": "0.000737"
        },
        {
          "BLKpoint_id": "BLKpoint_28",
          "temperature_k": "350.7",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "1",
          "viscosity_pa_s": "0.00059"
        },
        {
          "BLKpoint_id": "BLKpoint_29",
          "temperature_k": "373.2",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "0.1",
          "viscosity_pa_s": "0.000401"
        },
        {
          "BLKpoint_id": "BLKpoint_30",
          "temperature_k": "373.2",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "0.2",
          "viscosity_pa_s": "0.000448"
        },
        {
          "BLKpoint_id": "BLKpoint_32",
          "temperature_k": "373.2",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "0.4",
          "viscosity_pa_s": "0.000462"
        },
        {
          "BLKpoint_id": "BLKpoint_34",
          "temperature_k": "373.2",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "0.8",
          "viscosity_pa_s": "0.000381"
        },
        {
          "BLKpoint_id": "BLKpoint_35",
          "temperature_k": "373.2",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "1",
          "viscosity_pa_s": "0.000364"
        },
        {
          "BLKpoint_id": "BLKpoint_36",
          "temperature_k": "373.2",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0.1",
          "viscosity_pa_s": "0.000397"
        },
        {
          "BLKpoint_id": "BLKpoint_37",
          "temperature_k": "373.2",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0.2",
          "viscosity_pa_s": "0.000449"
        },
        {
          "BLKpoint_id": "BLKpoint_39",
          "temperature_k": "373.2",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0.4",
          "viscosity_pa_s": "0.000477"
        },
        {
          "BLKpoint_id": "BLKpoint_42",
          "temperature_k": "373.2",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "1",
          "viscosity_pa_s": "0.000382"
        },
        {
          "BLKpoint_id": "BLKpoint_43",
          "temperature_k": "373.2",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0.1",
          "viscosity_pa_s": "0.000403"
        },
        {
          "BLKpoint_id": "BLKpoint_44",
          "temperature_k": "373.2",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0.2",
          "viscosity_pa_s": "0.000459"
        },
        {
          "BLKpoint_id": "BLKpoint_46",
          "temperature_k": "373.2",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0.4",
          "viscosity_pa_s": "0.000489"
        },
        {
          "BLKpoint_id": "BLKpoint_49",
          "temperature_k": "373.2",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "1",
          "viscosity_pa_s": "0.000404"
        },
        {
          "BLKpoint_id": "BLKpoint_50",
          "temperature_k": "373.2",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.1",
          "viscosity_pa_s": "0.000421"
        },
        {
          "BLKpoint_id": "BLKpoint_52",
          "temperature_k": "373.2",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.3",
          "viscosity_pa_s": "0.000515"
        },
        {
          "BLKpoint_id": "BLKpoint_56",
          "temperature_k": "373.2",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "1",
          "viscosity_pa_s": "0.000443"
        },
        {
          "BLKpoint_id": "BLKpoint_57",
          "temperature_k": "476.2",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "0.1",
          "viscosity_pa_s": "0.000148"
        },
        {
          "BLKpoint_id": "BLKpoint_63",
          "temperature_k": "476.2",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "1",
          "viscosity_pa_s": "0.000107"
        },
        {
          "BLKpoint_id": "BLKpoint_64",
          "temperature_k": "476.2",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0.1",
          "viscosity_pa_s": "0.000152"
        },
        {
          "BLKpoint_id": "BLKpoint_70",
          "temperature_k": "476.2",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "1",
          "viscosity_pa_s": "0.000123"
        },
        {
          "BLKpoint_id": "BLKpoint_71",
          "temperature_k": "476.2",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0.1",
          "viscosity_pa_s": "0.000159"
        },
        {
          "BLKpoint_id": "BLKpoint_77",
          "temperature_k": "476.2",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "1",
          "viscosity_pa_s": "0.000138"
        },
        {
          "BLKpoint_id": "BLKpoint_78",
          "temperature_k": "476.2",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.1",
          "viscosity_pa_s": "0.000164"
        },
        {
          "BLKpoint_id": "BLKpoint_84",
          "temperature_k": "476.2",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "1",
          "viscosity_pa_s": "0.000151"
        }
      ],
      "inspection_id": "INSP_2bf04912dbc3",
      "lit_num_id": "GLOBlit_1742"
    },
    {
      "doi": "10.1016/j.jct.2007.05.004",
      "block_number": "PROPblock_11",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<water>",
        "pressure_kpa",
        "viscosity_pa_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "0",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001187"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "0.2961",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001735"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "0.6991",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.002705"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "0.8001",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0027"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "0.8996",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.002223"
        },
        {
          "BLKpoint_id": "BLKpoint_13",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "1",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001002"
        },
        {
          "BLKpoint_id": "BLKpoint_14",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001082"
        },
        {
          "BLKpoint_id": "BLKpoint_19",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.3991",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001659"
        },
        {
          "BLKpoint_id": "BLKpoint_21",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.6991",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.002275"
        },
        {
          "BLKpoint_id": "BLKpoint_22",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.8001",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0023"
        },
        {
          "BLKpoint_id": "BLKpoint_23",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.8996",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.00186"
        },
        {
          "BLKpoint_id": "BLKpoint_25",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "1",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.00089"
        },
        {
          "BLKpoint_id": "BLKpoint_26",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "0",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.000987"
        },
        {
          "BLKpoint_id": "BLKpoint_33",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "0.6991",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001941"
        },
        {
          "BLKpoint_id": "BLKpoint_34",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "0.8001",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001937"
        },
        {
          "BLKpoint_id": "BLKpoint_35",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "0.8996",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.00158"
        },
        {
          "BLKpoint_id": "BLKpoint_37",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "1",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.000797"
        }
      ],
      "inspection_id": "INSP_78cce36f2f6f",
      "lit_num_id": "GLOBlit_2825"
    }
  ]
}
</subagent_answer>
```
</details>

---

## Nested tool calls — L1_1 (L1-query)

**Nest:** Q - L1_1
**Parent:** `L1_query` — Step 1 [Q · c6] relays this worker's result
**Started:** 06:03:07  |  **Ended:** 06:05:53  |  **Tool calls:** 5

---

### Step 2 [Q - L1_1 · c1]: `resolve_compound_ids`

<details><summary>Arguments</summary>

```json
{
  "queries": [
    "ethanol",
    "water"
  ],
  "min_score": 80,
  "limit": 5,
  "purpose": "Resolve ethanol and water to global compound IDs",
  "tasks": "Find GLOBcomp IDs for ethanol and water"
}
```
</details>

- **Result:** 222 chars  |  **Time:** 6.9s  |  **Started:** 06:03:19 (t+20.3s)
- **Subagent:** KEEP in 278 → 222 chars (6.8s)
  - Both ethanol and water were resolved with exact name matches.

| Compound | Global ID | Formula | SMILES |
|----------|-----------|---------|--------|
| ethanol | GLOBcomp_2 | C2H6O | CCO |
| water | 

<details><summary>Result</summary>

```
Both ethanol and water were resolved with exact name matches.

| Compound | Global ID | Formula | SMILES |
|----------|-----------|---------|--------|
| ethanol | GLOBcomp_2 | C2H6O | CCO |
| water | GLOBcomp_1 | H2O | O |
```
</details>

---

### Step 3 [Q - L1_1 · c2]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_2",
    "GLOBcomp_1"
  ],
  "property": "GLOBprop_4",
  "system_type": "binary",
  "limit": 50,
  "purpose": "Find viscosity data for ethanol+water binary mixtures",
  "tasks": "Search for dynamic viscosity blocks, report temperature ranges and DOIs"
}
```
</details>

- **Result:** 1,260 chars  |  **Time:** 20.9s  |  **Started:** 06:03:33 (t+34.6s)
- **Subagent:** KEEP in 8,844 → 1,242 chars (14.7s)
  - **Summary:** 14 dynamic viscosity (Pa·s) blocks found for ethanol + water binary mixtures across 14 DOIs, all liquid phase, covering temperatures from 268.1 K to 618.2 K. Data spans ambient to high-pr

<details><summary>Result</summary>

```
**Summary:** 14 dynamic viscosity (Pa·s) blocks found for ethanol + water binary mixtures across 14 DOIs, all liquid phase, covering temperatures from 268.1 K to 618.2 K. Data spans ambient to high-pressure conditions with various composition variables (mole fraction, mass fraction, volume fraction, molality).

| # | DOI | Block | GLOBlit | T (K) | Composition | η range (Pa·s) | Pts (kept) |
|---|-----|-------|---------|--------|-------------|-----------------|------------|
| 1 | 10.1016/j.fluid.2015.07.012 | PROPblock_4 | GLOBlit_1742 | 350.7–373.2 | x(ethanol) 0.1–1 | 0.000364–0.000737 | 36 |
| 2 | 10.1016/j.fluid.2017.09.005 | PROPblock_4 | GLOBlit_2092 | 523.2–618.2 | x(ethanol) 0–1 | 5.3e-05–0.000134 | 28 |
| 3 | 10.1016/j.jct.2007.05.004 | PROPblock_11 | GLOBlit_2825 | 293.15–303.15 | x(water) 0–1 | 0.000797–0.002705 | 17 |
| 4 | 10.1016/j.jct.2018.02.022 | PROPblock_21 | GLOBlit_5201 | 293.15–303.15 | x(ethanol) 0.0201–0.929 | 0.0009816–0.0028641 | 14 |
| 5 | 10.1021/acs.jced.7b00299 | PROPblock_11 | GLOBlit_7178 | 298.15–303.15 | fixed molality | 0.001992–0.002367 | 2 |
| 6 | 10.1021/acs.jced.8b00086 | PROPblock_47 | GLOBlit_7448 | fixed T | w(water) 0.206–0.508 | 0.001676–0.002235 | 6 |
| 7 | 10.1021/acs.jced.8b00 [lit_num_id=null]
```
</details>

---

### Step 5 [Q - L1_1 · c3]: `inspect_block_table`

<details><summary>Arguments</summary>

```json
{
  "block_number": "PROPblock_4",
  "literature": "GLOBlit_2092",
  "purpose": "Ground temperature and viscosity values for highest-T ethanol+water viscosity block",
  "tasks": "Return data rows with T, composition, and viscosity values"
}
```
</details>

- **Result:** 2,405 chars  |  **Time:** 0.1s  |  **Started:** 06:04:21 (t+82.1s)

<details><summary>Result</summary>

```
**Data inspection** — 10.1016/j.fluid.2017.09.005 [GLOBlit_2092] :: PROPblock_4 (binary: ethanol + water)
filter: none (whole block)

| BLKpoint_id | temperature_k | pressure_kpa | mole_fraction_<ethanol> | viscosity_pa_s |
|---|---|---|---|---|
| BLKpoint_1 | 523.2 | 20000 | 0 | 0.00011 |
| BLKpoint_2 | 523.2 | 20000 | 0.1 | 0.00012 |
| BLKpoint_3 | 523.2 | 20000 | 0.2 | 0.000119 |
| BLKpoint_6 | 523.2 | 20000 | 0.6 | 9.9e-05 |
| BLKpoint_8 | 523.2 | 20000 | 1 | 8.7e-05 |
| BLKpoint_9 | 523.2 | 30000 | 0 | 0.000113 |
| BLKpoint_10 | 523.2 | 30000 | 0.1 | 0.000126 |
| BLKpoint_11 | 523.2 | 30000 | 0.2 | 0.000127 |
| BLKpoint_16 | 523.2 | 30000 | 1 | 0.000103 |
| BLKpoint_17 | 523.2 | 40000 | 0 | 0.000115 |
| BLKpoint_18 | 523.2 | 40000 | 0.1 | 0.000132 |
| BLKpoint_20 | 523.2 | 40000 | 0.3 | 0.000134 |
| BLKpoint_21 | 523.2 | 40000 | 0.4 | 0.000128 |
| BLKpoint_24 | 523.2 | 40000 | 1 | 0.000115 |
| BLKpoint_25 | 573.2 | 20000 | 0 | 9e-05 |
| BLKpoint_28 | 573.2 | 20000 | 0.3 | 7e-05 |
| BLKpoint_30 | 573.2 | 20000 | 0.6 | 5.7e-05 |
| BLKpoint_32 | 573.2 | 20000 | 1 | 5.3e-05 |
| BLKpoint_33 | 573.2 | 30000 | 0 | 9.3e-05 |
| BLKpoint_38 | 573.2 | 30000 | 0.6 | 6.9e-05 |
| BLKpoint_40 | 573.2 | 30000 | 1 | 6.6e-05 |
| BLKpoint_41 | 573.2 | 40000 | 0 | 9.6e-05 |
| BLKpoint_46 | 573.2 | 40000 | 0.6 | 8e-05 |
| BLKpoint_48 | 573.2 | 40000 | 1 | 7.7e-05 |
| BLKpoint_49 | 618.2 | 20000 | 0 | 7.2e-05 |
| BLKpoint_51 | 618.2 | 20000 | 0.2 | 3.5e-05 |
| BLKpoint_52 | 618.2 | 20000 | 0.3 | 3.1e-05 |
| BLKpoint_56 | 618.2 | 20000 | 1 | 3.9e-05 |
| BLKpoint_57 | 618.2 | 30000 | 0 | 7.7e-05 |
| BLKpoint_60 | 618.2 | 30000 | 0.3 | 5.9e-05 |
| BLKpoint_62 | 618.2 | 30000 | 0.6 | 5.5e-05 |
| BLKpoint_64 | 618.2 | 30000 | 1 | 5.5e-05 |
| BLKpoint_65 | 618.2 | 40000 | 0 | 8.1e-05 |
| BLKpoint_66 | 618.2 | 40000 | 0.1 | 8.1e-05 |
| BLKpoint_69 | 618.2 | 40000 | 0.4 | 7e-05 |
| BLKpoint_70 | 618.2 | 40000 | 0.6 | 6.7e-05 |
| BLKpoint_72 | 618.2 | 40000 | 1 | 6.7e-05 |

mode: RDP — 37 of 72 matched rows shown (shape-preserving; block has 72). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
stats (matched, n=72): temperature_k 523.2–618.2 (n=72); pressure_kpa 20000–40000 (n=72); mole_fraction_ethanol 0–1 (n=72); viscosity_pa_s 3.1e-05–0.000134 (n=72)
inspection_id: INSP_987176e5cf18
Data points may be quoted ONLY verbatim from the table above or the stats lines.
```
</details>

---

### Step 6 [Q - L1_1 · c4]: `inspect_block_table`

<details><summary>Arguments</summary>

```json
{
  "block_number": "PROPblock_4",
  "literature": "GLOBlit_1742",
  "purpose": "Ground data values for ethanol+water viscosity block",
  "tasks": "Inspect PROPblock_4 from GLOBlit_1742 to verify T range and viscosity values"
}
```
</details>

- **Result:** 2,697 chars  |  **Time:** 0.1s  |  **Started:** 06:04:30 (t+91.2s)

<details><summary>Result</summary>

```
**Data inspection** — 10.1016/j.fluid.2015.07.012 [GLOBlit_1742] :: PROPblock_4 (binary: ethanol + water)
filter: none (whole block)

| BLKpoint_id | temperature_k | pressure_kpa | mole_fraction_<ethanol> | viscosity_pa_s |
|---|---|---|---|---|
| BLKpoint_1 | 350.7 | 10000 | 0.1 | 0.000537 |
| BLKpoint_2 | 350.7 | 10000 | 0.2 | 0.000625 |
| BLKpoint_4 | 350.7 | 10000 | 0.4 | 0.00064 |
| BLKpoint_5 | 350.7 | 10000 | 0.6 | 0.000595 |
| BLKpoint_7 | 350.7 | 10000 | 1 | 0.000461 |
| BLKpoint_8 | 350.7 | 20000 | 0.1 | 0.000546 |
| BLKpoint_9 | 350.7 | 20000 | 0.2 | 0.000638 |
| BLKpoint_11 | 350.7 | 20000 | 0.4 | 0.000669 |
| BLKpoint_14 | 350.7 | 20000 | 1 | 0.000518 |
| BLKpoint_15 | 350.7 | 30000 | 0.1 | 0.000556 |
| BLKpoint_16 | 350.7 | 30000 | 0.2 | 0.000651 |
| BLKpoint_18 | 350.7 | 30000 | 0.4 | 0.000691 |
| BLKpoint_21 | 350.7 | 30000 | 1 | 0.000555 |
| BLKpoint_22 | 350.7 | 40000 | 0.1 | 0.000578 |
| BLKpoint_23 | 350.7 | 40000 | 0.2 | 0.000681 |
| BLKpoint_24 | 350.7 | 40000 | 0.3 | 0.000726 |
| BLKpoint_25 | 350.7 | 40000 | 0.4 | 0.000737 |
| BLKpoint_28 | 350.7 | 40000 | 1 | 0.00059 |
| BLKpoint_29 | 373.2 | 10000 | 0.1 | 0.000401 |
| BLKpoint_30 | 373.2 | 10000 | 0.2 | 0.000448 |
| BLKpoint_32 | 373.2 | 10000 | 0.4 | 0.000462 |
| BLKpoint_34 | 373.2 | 10000 | 0.8 | 0.000381 |
| BLKpoint_35 | 373.2 | 10000 | 1 | 0.000364 |
| BLKpoint_36 | 373.2 | 20000 | 0.1 | 0.000397 |
| BLKpoint_37 | 373.2 | 20000 | 0.2 | 0.000449 |
| BLKpoint_39 | 373.2 | 20000 | 0.4 | 0.000477 |
| BLKpoint_42 | 373.2 | 20000 | 1 | 0.000382 |
| BLKpoint_43 | 373.2 | 30000 | 0.1 | 0.000403 |
| BLKpoint_44 | 373.2 | 30000 | 0.2 | 0.000459 |
| BLKpoint_46 | 373.2 | 30000 | 0.4 | 0.000489 |
| BLKpoint_49 | 373.2 | 30000 | 1 | 0.000404 |
| BLKpoint_50 | 373.2 | 40000 | 0.1 | 0.000421 |
| BLKpoint_52 | 373.2 | 40000 | 0.3 | 0.000515 |
| BLKpoint_56 | 373.2 | 40000 | 1 | 0.000443 |
| BLKpoint_57 | 476.2 | 10000 | 0.1 | 0.000148 |
| BLKpoint_63 | 476.2 | 10000 | 1 | 0.000107 |
| BLKpoint_64 | 476.2 | 20000 | 0.1 | 0.000152 |
| BLKpoint_70 | 476.2 | 20000 | 1 | 0.000123 |
| BLKpoint_71 | 476.2 | 30000 | 0.1 | 0.000159 |
| BLKpoint_77 | 476.2 | 30000 | 1 | 0.000138 |
| BLKpoint_78 | 476.2 | 40000 | 0.1 | 0.000164 |
| BLKpoint_84 | 476.2 | 40000 | 1 | 0.000151 |

mode: RDP — 42 of 84 matched rows shown (shape-preserving; block has 84). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
stats (matched, n=84): temperature_k 350.7–476.2 (n=84); pressure_kpa 10000–40000 (n=84); mole_fraction_ethanol 0.1–1 (n=84); viscosity_pa_s 0.000107–0.000737 (n=84)
inspection_id: INSP_2bf04912dbc3
Data points may be quoted ONLY verbatim from the table above or the stats lines.
```
</details>

---

### Step 7 [Q - L1_1 · c5]: `inspect_block_table`

<details><summary>Arguments</summary>

```json
{
  "block_number": "PROPblock_11",
  "literature": "GLOBlit_2825",
  "purpose": "Ground data values for ethanol+water viscosity block at lower temperatures",
  "tasks": "Inspect block to verify T range and viscosity values"
}
```
</details>

- **Result:** 1,568 chars  |  **Time:** 0.1s  |  **Started:** 06:04:37 (t+98.5s)

<details><summary>Result</summary>

```
**Data inspection** — 10.1016/j.jct.2007.05.004 [GLOBlit_2825] :: PROPblock_11 (binary: ethanol + water)
filter: none (whole block)
block constraints: pressure_kpa = 101.0

| BLKpoint_id | temperature_k | mole_fraction_<water> | pressure_kpa | viscosity_pa_s |
|---|---|---|---|---|
| BLKpoint_1 | 293.15 | 0 | 101.0 | 0.001187 |
| BLKpoint_5 | 293.15 | 0.2961 | 101.0 | 0.001735 |
| BLKpoint_9 | 293.15 | 0.6991 | 101.0 | 0.002705 |
| BLKpoint_10 | 293.15 | 0.8001 | 101.0 | 0.0027 |
| BLKpoint_11 | 293.15 | 0.8996 | 101.0 | 0.002223 |
| BLKpoint_13 | 293.15 | 1 | 101.0 | 0.001002 |
| BLKpoint_14 | 298.15 | 0 | 101.0 | 0.001082 |
| BLKpoint_19 | 298.15 | 0.3991 | 101.0 | 0.001659 |
| BLKpoint_21 | 298.15 | 0.6991 | 101.0 | 0.002275 |
| BLKpoint_22 | 298.15 | 0.8001 | 101.0 | 0.0023 |
| BLKpoint_23 | 298.15 | 0.8996 | 101.0 | 0.00186 |
| BLKpoint_25 | 298.15 | 1 | 101.0 | 0.00089 |
| BLKpoint_26 | 303.15 | 0 | 101.0 | 0.000987 |
| BLKpoint_33 | 303.15 | 0.6991 | 101.0 | 0.001941 |
| BLKpoint_34 | 303.15 | 0.8001 | 101.0 | 0.001937 |
| BLKpoint_35 | 303.15 | 0.8996 | 101.0 | 0.00158 |
| BLKpoint_37 | 303.15 | 1 | 101.0 | 0.000797 |

mode: RDP — 17 of 37 matched rows shown (shape-preserving; block has 37). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
stats (matched, n=37): temperature_k 293.15–303.15 (n=37); mole_fraction_water 0–1 (n=37); pressure_kpa 101.0–101.0 (n=37); viscosity_pa_s 0.000797–0.002705 (n=37)
inspection_id: INSP_78cce36f2f6f
Data points may be quoted ONLY verbatim from the table above or the stats lines.
```
</details>

---

## Tool Compaction Pipeline (5 calls)

| # | Tool | Pipeline | Native | Hardcoded | Agentic | Verdict | Native→Final | Section |
|--:|------|----------|-------:|----------:|--------:|---------|-------------:|---------|
| 1 | `resolve_compound_ids` | query | 555 | 278 | 222 | KEEP | −60% | L1_1 |
| 2 | `search_blocks` | query | 87,988 | 8,844 | 1,242 | KEEP | −99% | L1_1 |
| 3 | `inspect_block_table` | query | 9,194 | 2,390 | 2,390 | SKIP | −74% | L1_1 |
| 4 | `inspect_block_table` | query | 10,276 | 2,682 | 2,682 | SKIP | −74% | L1_1 |
| 5 | `inspect_block_table` | query | 5,506 | 1,553 | 1,553 | SKIP | −72% | L1_1 |

## Subagent Summary (2 events)

| Tool | Verdict | Input Chars | Output Chars | Time | Section |
|------|---------|-------------|-------------|------|---------|
| resolve_compound_ids | KEEP | 278 | 222 | 6.8s | L1_1 |
| search_blocks | KEEP | 8,844 | 1,242 | 14.7s | L1_1 |

---

**Total:** 6 tool calls  |  Tool time: 194.0s  |  Wall: 219.3s  |  **Status:** OK
