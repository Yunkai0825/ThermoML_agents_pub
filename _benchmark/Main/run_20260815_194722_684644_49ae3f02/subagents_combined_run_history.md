# Combined Subagent History


---

## Subagent: Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1)

# Tool History — analysis-agent

**Nest:** main - A_1
**Session:** 64ee92c0
**Detailed log:** run_history_detailed.md — Argo events + verbatim agent outputs (join: session id; step tag `cN` ↔ event-row `cN`)
**Prompt:** [Purpose: Obtain a Redlich-Kister correlation for viscosity of water + ethylene glycol near 25 °C from ThermoML data.]
Fit a Redlich-Kister polynomial to the viscosity of the binary liquid mixture water + ethylene glycol near 25 °C. Use a single state-aligned composition series. Report the selected temperature, pressure, composition basis (mole or mass fraction), viscosity basis (dynamic or kinematic), the RK equation, polynomial order, coefficients with units, R², RMSE, and the composition range covered.

[Context: The user wants a complete RK fit report for viscosity of the water + ethylene glycol system. Search for experimental viscosity data (dynamic viscosity preferred) in ThermoML for this binary system near 298.15 K, select the best composition series, and perform the RK fit.]
**Started:** 2026-08-15 19:49:09  |  **Elapsed:** 500.2s  |  **Tool calls:** 30  |  **Nested sections:** 1

---

### Step 1 [Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1)] [main - A_1 · c1]: `query_thermoml` ❌ ERROR

<details><summary>Arguments</summary>

```json
{
  "purpose": "Find viscosity data blocks for binary mixture of water + ethylene glycol near 298.15 K",
  "instruction": "Search for blocks containing both water (H2O) and ethylene glycol (1,2-ethanediol, HOCH2CH2OH, CAS 107-21-1) with viscosity measurements (dynamic viscosity GLOBprop_4 or kinematic viscosity GLOBprop_40). I need binary mixture data near 25°C (298.15 K) with composition variation. Return DOIs, block numbers, temperature ranges, composition ranges, and number of data points.",
  "id_catalog": [
    {
      "id": "GLOBprop_4",
      "type": "property"
    },
    {
      "id": "GLOBprop_40",
      "type": "property"
    }
  ]
}
```
</details>

- **Result:** 189 chars  |  **Time:** 0.0s  |  **Started:** 19:49:19 (t+9.8s)
- **Error:** `{
  "error": "id_catalog[0] must contain exactly ['global_id', 'name', 'registry_id', 'type']; received ['id', 'type']",
  "error_code": "TOOL_EXECUTION_ERROR",
  "tool": "query_thermoml"
}`

---

### Step 2 [Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1)] [main - A_1 · c2]: `query_thermoml` ❌ ERROR

<details><summary>Arguments</summary>

```json
{
  "purpose": "Find dynamic viscosity data blocks for the binary mixture water + ethylene glycol near 298.15 K",
  "instruction": "Search for blocks containing viscosity (dynamic viscosity, GLOBprop_4) data for the binary system water + ethylene glycol (1,2-ethanediol) near 298.15 K. Return DOIs, block numbers, temperature ranges, composition ranges, and number of data points.",
  "id_catalog": [
    {
      "global_id": "GLOBprop_4",
      "name": "Viscosity",
      "registry_id": "",
      "type": "property"
    }
  ]
}
```
</details>

- **Result:** 233 chars  |  **Time:** 0.0s  |  **Started:** 19:49:25 (t+16.0s)
- **Error:** `{
  "error": "id_catalog[0].type is invalid: 'property'; valid types: ['blocktype', 'comp', 'constr', 'lit', 'meas', 'phase', 'prop', 'rxntype', 'solvent', 'var']",
  "error_code": "TOOL_EXECUTION_ERROR",
  "tool": "query_thermoml"
}`

---

### Step 3 [Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1)] [main - A_1 · c22]: `query_thermoml`

<details><summary>Arguments</summary>

```json
{
  "purpose": "Find viscosity data blocks for binary mixture water + ethylene glycol near 298.15 K",
  "instruction": "Search for blocks containing dynamic viscosity (GLOBprop_4) or kinematic viscosity (GLOBprop_40) data for the binary system of water and ethylene glycol (1,2-ethanediol). Temperature near 298.15 K. Return DOIs, block numbers, temperature ranges, composition ranges, and number of data points.",
  "id_catalog": [
    {
      "global_id": "GLOBprop_4",
      "name": "Viscosity",
      "registry_id": "",
      "type": "prop"
    },
    {
      "global_id": "GLOBprop_40",
      "name": "Kinematic viscosity",
      "registry_id": "",
      "type": "prop"
    }
  ]
}
```
</details>

- **Result:** 66,728 chars  |  **Time:** 300.3s  |  **Started:** 19:49:31 (t+21.8s)
- **Nested:** ↳ 19 tool calls in section 'L1_1' below

<details><summary>Result</summary>

```
[TOOL_RESULT_SIZE_WARNING: query_thermoml returned 66,482 characters after result processing; the target is 24,000. The full result follows — prefer narrower requests, and rely on your working memory for recall instead of re-running this call.]

<subagent_answer>
{
  "answer": "## Viscosity Data for Binary Water + Ethylene Glycol System Near 298.15 K\n\n**Compounds:** Water (GLOBcomp_1) + 1,2-Ethanediol / Ethylene Glycol (GLOBcomp_24)\n\n**Properties searched:** Dynamic viscosity (GLOBprop_4) and Kinematic viscosity (GLOBprop_40)\n\n### Results\n\n**Dynamic viscosity (GLOBprop_4):** 7 blocks found in the binary system within the 290\u2013310 K search window.\n\n**Kinematic viscosity (GLOBprop_40):** No blocks found for this system in the database.\n\n### Block Details (from inspections)\n\n| # | DOI | Block | GLOBlit | Data Points | T Range (K) | Composition Variable & Range | P (kPa) |\n|---|-----|-------|---------|-------------|-------------|------------------------------|---------|\n| 1 | 10.1016/j.jct.2006.01.011 | PROPblock_13 | GLOBlit_2656 | 10 | 293.15\u2013293.15 | mass fraction EG: 0\u20130.9 | 101.325 |\n| 2 | 10.1016/j.jct.2018.02.022 | PROPblock_24 | GLOBlit_5201 | 84 | 293.15\u2013308.15 | mole fraction EG: 0\u20131 | 92.3 |\n| 3 | 10.1021/acs.jced.6b00526 | PROPblock_18 | GLOBlit_6951 | 33 | 293.15\u2013303.15 | mole fraction water: 0\u20131 | 100 |\n| 4 | 10.1021/je020140j | PROPblock_5 | GLOBlit_8038 | 77 | 293.15\u2013353.15 | mole fraction EG: 0\u20131 | 101 |\n| 5 | 10.1021/je025610o | PROPblock_5 | GLOBlit_8106 | 30 | 296.45\u2013449.85 | mole fraction EG: 0.25\u20130.75 | 100.0 |\n| 6 | 10.1021/je800271e | PROPblock_4 | GLOBlit_11186 | 52 | 308.15\u2013323.15 | mole fraction EG: 0\u20131 | (not reported) |\n\n(A 7th block was indicated in the search but its details were truncated in the search results.)\n\n### Key Observations\n\n- The largest dataset near 298.15 K is from GLOBlit_5201 (DOI: 10.1016/j.jct.2018.02.022, PROPblock_24) with 84 data points spanning 293.15\u2013308.15 K and the full composition range (mole fraction EG 0\u20131), with viscosity values ranging from 0.00075887 to 0.020613 Pa\u00b7s.\n- GLOBlit_6951 (DOI: 10.1021/acs.jced.6b00526, PROPblock_18) covers the full composition range (mole fraction water 0\u20131) with 33 points at 293.15\u2013303.15 K, viscosity 0.000755\u20130.02113 Pa\u00b7s.\n- GLOBlit_8038 (DOI: 10.1021/je020140j, PROPblock_5) provides 77 points over 293.15\u2013353.15 K with mole fraction EG 0\u20131, viscosity 0.000356\u20130.020833 Pa\u00b7s.\n- GLOBlit_8106 (DOI: 10.1021/je025610o, PROPblock_5) has 30 points at three compositions (mole fraction EG 0.25, 0.5, 0.75) over 296.45\u2013449.85 K, viscosity 0.000366\u20130.0123 Pa\u00b7s.\n- GLOBlit_2656 (DOI: 10.1016/j.jct.2006.01.011, PROPblock_13) is at a single temperature (293.15 K) with 10 points across mass fraction EG 0\u20130.9, viscosity 0.001008\u20130.013999 Pa\u00b7s.\n- GLOBlit_11186 (DOI: 10.1021/je800271e, PROPblock_4) starts at 308.15 K (52 points, 308.15\u2013323.15 K), above the 298.15 K target, with viscosity 0.00055\u20130.0092122 Pa\u00b7s.\n\nThe ethylene glycol\u2013water system shows a strong positive viscosity deviation from ideal mixing, with viscosity increasing substantially as ethylene glycol content rises, consistent with the extensive hydrogen-bonding network formed between the two hydroxyl groups of ethylene glycol and water molecules.\n\n---\n[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:\n- **AMBIGUOUS_VALUE** PROPblock_4: 298.15 matches 2 different sources \u2014 ambiguous; re-quote it from an inspection of the block you mean\n  fix: `inspect_block_table(block_number=\"PROPblock_4\", literature=\"<GLOBlit_N or DOI>\", nearest={\"column\": \"temperature_k\", \"value\": 298.15})`\n- **AMBIGUOUS_VALUE** PROPblock_4: 298.15 matches 2 different sources \u2014 ambiguous; re-quote it from an inspection of the block you mean\n  fix: `inspect_block_table(block_number=\"PROPblock_4\", literature=\"<GLOBlit_N or DOI>\", nearest={\"column\": \"temperature_k\", \"value\": 298.15})`\nInspected so far: PROPblock_13, PROPblock_18, PROPblock_24, PROPblock_4, PROPblock_5",
  "core_claims": [
    "The ThermoML database contains at least 6 identified blocks of dynamic viscosity data for the binary water + ethylene glycol system within the 290\u2013310 K temperature window; no kinematic viscosity blocks were found for this system.",
    "The largest dataset near 298.15 K is from GLOBlit_5201 (DOI: 10.1016/j.jct.2018.02.022, PROPblock_24) with 84 data points spanning 293.15\u2013308.15 K and the full composition range (mole fraction EG 0\u20131), with viscosity values ranging from 0.00075887 to 0.020613 Pa\u00b7s.",
    "Multiple independent sources (GLOBlit_5201, GLOBlit_6951, GLOBlit_8038) cover the full composition range of the water\u2013ethylene glycol system at temperatures encompassing 298.15 K, with reported dynamic viscosities spanning roughly 0.000356\u20130.020833 Pa\u00b7s across all compositions and temperatures.",
    "The ethylene glycol\u2013water system shows a strong positive viscosity deviation from ideal mixing, with viscosity increasing substantially as ethylene glycol content rises, consistent with extensive hydrogen bonding between the two components."
  ],
  "status": "success",
  "summary": "Dynamic viscosity data for the binary water + ethylene glycol (1,2-ethanediol) system near 298.15 K were found in 7 ThermoML blocks; no kinematic viscosity data were found. The largest dataset is from GLOBlit_5201 (DOI 10.1016/j.jct.2018.02.022, PROPblock_24) with 84 points spanning 293.15\u2013308.15 K over the full composition range (mole fraction EG 0\u20131), viscosity 0.00075887\u20130.020613 Pa\u00b7s at 92.3 kPa. GLOBlit_6951 (DOI 10.1021/acs.jced.6b00526, PROPblock_18) provides 33 points at 293.15\u2013303.15 K, mole fraction water 0\u20131, viscosity 0.000755\u20130.02113 Pa\u00b7s at 100 kPa. GLOBlit_8038 (DOI 10.1021/je020140j, PROPblock_5) gives 77 points over 293.15\u2013353.15 K, mole fraction EG 0\u20131, viscosity 0.000356\u20130.020833 Pa\u00b7s at 101 kPa. GLOBlit_8106 (DOI 10.1021/je025610o, PROPblock_5) has 30 points at mole fraction EG 0.25, 0.5, and 0.75 over 296.45\u2013449.85 K, viscosity 0.000366\u20130.0123 Pa\u00b7s at 100.0 kPa. GLOBlit_2656 (DOI 10.1016/j.jct.2006.01.011, PROPblock_13) contains 10 points at 293.15 K, mass fraction EG 0\u20130.9, viscosity 0.001008\u20130.013999 Pa\u00b7s at 101.325 kPa. GLOBlit_11186 (DOI 10.1021/je800271e, PROPblock_4) covers 308.15\u2013323.15 K with 52 points, mole fraction EG 0\u20131, viscosity 0.00055\u20130.0092122 Pa\u00b7s. The system exhibits a strong positive viscosity deviation from ideal mixing, attributed to extensive hydrogen bonding between ethylene glycol and water.",
  "core_id_updates": [
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_1",
      "registry_id": "water",
      "name": "water"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_24",
      "registry_id": "1,2-ethanediol",
      "name": "1,2-ethanediol"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBprop_4",
      "registry_id": "viscosity_pa_s",
      "name": "Viscosity, Pa*s"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBprop_40",
      "registry_id": "kinematic_viscosity_m2_s",
      "name": "Kinematic viscosity, m2/s"
    }
  ],
  "core_blocks_found": [
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
      "description": "Dynamic viscosity of water + ethylene glycol at 293.15 K, 10 points, mass fraction EG 0\u20130.9.",
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
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
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
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_3_1"
        }
      ],
      "parent_n_datapoints": 10,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
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
      "description": "Dynamic viscosity of water + ethylene glycol, 84 points, 293.15\u2013308.15 K, mole fraction EG 0\u20131.",
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
          "SMILES": null,
          "sample_num": "DOIcompSample_2_1"
        },
        {
          "org_num": "DOIcomp_6",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
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
          "SMILES": null,
          "sample_num": "DOIcompSample_2_1"
        },
        {
          "org_num": "DOIcomp_6",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
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
      "description": "Dynamic viscosity of water + ethylene glycol, 33 points, 293.15\u2013303.15 K, mole fraction water 0\u20131.",
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
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_5",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
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
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_5",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
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
      "description": "Dynamic viscosity of water + ethylene glycol, 77 points, 293.15\u2013353.15 K, mole fraction EG 0\u20131.",
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
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
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
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
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
      "description": "Dynamic viscosity of water + ethylene glycol, 30 points, 296.45\u2013449.85 K, mole fraction EG 0.25\u20130.75.",
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
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
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
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
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
      "lit_num_id": "GLOBlit_11186",
      "block_number": "PROPblock_4",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_24",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity of water + ethylene glycol, 52 points, 308.15\u2013323.15 K, mole fraction EG 0\u20131.",
      "doi": "10.1021/je800271e",
      "lit_id": "2008-zha-zha-2",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 52,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_3_1"
        },
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_4_1"
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
            "min": 308.15,
            "max": 323.15,
            "n_unique": 4
          },
          "range_min": 308.15,
          "range_max": 323.15
        },
        {
          "BLKvar_id": "BLKvar_2",
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
          "meas_num_id": "GLOBmeas_165",
          "meas_ID": "captub_ufactor_8",
          "method_standard": null,
          "method_custom": "CAPTUB:UFactor:8",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.00055,
            "max": 0.009212,
            "mean": 0.00189,
            "std": 0.00187,
            "n": 52
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.00055,
          "range_max": 0.009212
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
      "declared_system_type": "binary",
      "declared_n_components": 2,
      "declared_compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_3_1"
        },
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_4_1"
        }
      ],
      "parent_n_datapoints": 52,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1021/je025610o",
      "block_number": "PROPblock_5",
      "table_mode": "rdp",
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
          "BLKpoint_id": "BLKpoint_2",
          "mole_fraction_<1,2-ethanediol>": "0.25",
          "temperature_k": "313.05",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00229"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "mole_fraction_<1,2-ethanediol>": "0.25",
          "temperature_k": "353.05",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00099"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "mole_fraction_<1,2-ethanediol>": "0.25",
          "temperature_k": "435.55",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.000366"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "mole_fraction_<1,2-ethanediol>": "0.5",
          "temperature_k": "297.05",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00761"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "mole_fraction_<1,2-ethanediol>": "0.5",
          "temperature_k": "313.05",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00449"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "mole_fraction_<1,2-ethanediol>": "0.5",
          "temperature_k": "333.1",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00262"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "mole_fraction_<1,2-ethanediol>": "0.5",
          "temperature_k": "353.05",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.0017"
        },
        {
          "BLKpoint_id": "BLKpoint_13",
          "mole_fraction_<1,2-ethanediol>": "0.5",
          "temperature_k": "380.05",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00107"
        },
        {
          "BLKpoint_id": "BLKpoint_17",
          "mole_fraction_<1,2-ethanediol>": "0.5",
          "temperature_k": "440.65",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.0005"
        },
        {
          "BLKpoint_id": "BLKpoint_18",
          "mole_fraction_<1,2-ethanediol>": "0.75",
          "temperature_k": "297.35",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.0123"
        },
        {
          "BLKpoint_id": "BLKpoint_19",
          "mole_fraction_<1,2-ethanediol>": "0.75",
          "temperature_k": "313.05",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00697"
        },
        {
          "BLKpoint_id": "BLKpoint_20",
          "mole_fraction_<1,2-ethanediol>": "0.75",
          "temperature_k": "333.1",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00388"
        },
        {
          "BLKpoint_id": "BLKpoint_21",
          "mole_fraction_<1,2-ethanediol>": "0.75",
          "temperature_k": "353.05",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00242"
        },
        {
          "BLKpoint_id": "BLKpoint_22",
          "mole_fraction_<1,2-ethanediol>": "0.75",
          "temperature_k": "373.45",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00162"
        },
        {
          "BLKpoint_id": "BLKpoint_30",
          "mole_fraction_<1,2-ethanediol>": "0.75",
          "temperature_k": "449.85",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.000594"
        }
      ],
      "inspection_id": "INSP_475115ec48f0",
      "lit_num_id": "GLOBlit_8106"
    },
    {
      "doi": "10.1016/j.jct.2006.01.011",
      "block_number": "PROPblock_13",
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
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "mass_fraction_<1,2-ethanediol>": "0.4",
          "temperature_k": "293.15",
          "pressure_kpa": "101.325",
          "viscosity_pa_s": "0.002837"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "mass_fraction_<1,2-ethanediol>": "0.5",
          "temperature_k": "293.15",
          "pressure_kpa": "101.325",
          "viscosity_pa_s": "0.003558"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "mass_fraction_<1,2-ethanediol>": "0.6",
          "temperature_k": "293.15",
          "pressure_kpa": "101.325",
          "viscosity_pa_s": "0.004724"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "mass_fraction_<1,2-ethanediol>": "0.7",
          "temperature_k": "293.15",
          "pressure_kpa": "101.325",
          "viscosity_pa_s": "0.00636"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "mass_fraction_<1,2-ethanediol>": "0.8",
          "temperature_k": "293.15",
          "pressure_kpa": "101.325",
          "viscosity_pa_s": "0.008003"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "mass_fraction_<1,2-ethanediol>": "0.9",
          "temperature_k": "293.15",
          "pressure_kpa": "101.325",
          "viscosity_pa_s": "0.013999"
        }
      ],
      "inspection_id": "INSP_eb6a6a268c1a",
      "lit_num_id": "GLOBlit_2656"
    },
    {
      "doi": "10.1016/j.jct.2018.02.022",
      "block_number": "PROPblock_24",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<1,2-ethanediol>",
        "pressure_kpa",
        "viscosity_pa_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "293.15",
          "mole_fraction_<1,2-ethanediol>": "0.0494",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0015411"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "temperature_k": "293.15",
          "mole_fraction_<1,2-ethanediol>": "0.2072",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0035171"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "temperature_k": "293.15",
          "mole_fraction_<1,2-ethanediol>": "0.4446",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0076382"
        },
        {
          "BLKpoint_id": "BLKpoint_23",
          "temperature_k": "298.15",
          "mole_fraction_<1,2-ethanediol>": "0.2072",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0028109"
        },
        {
          "BLKpoint_id": "BLKpoint_28",
          "temperature_k": "298.15",
          "mole_fraction_<1,2-ethanediol>": "0.4446",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0060624"
        },
        {
          "BLKpoint_id": "BLKpoint_47",
          "temperature_k": "303.15",
          "mole_fraction_<1,2-ethanediol>": "0.4446",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0053492"
        },
        {
          "BLKpoint_id": "BLKpoint_65",
          "temperature_k": "308.15",
          "mole_fraction_<1,2-ethanediol>": "0.3921",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0040265"
        },
        {
          "BLKpoint_id": "BLKpoint_77",
          "temperature_k": "293.15",
          "mole_fraction_<1,2-ethanediol>": "0",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0010673"
        },
        {
          "BLKpoint_id": "BLKpoint_78",
          "temperature_k": "298.15",
          "mole_fraction_<1,2-ethanediol>": "0",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.00089689"
        },
        {
          "BLKpoint_id": "BLKpoint_79",
          "temperature_k": "303.15",
          "mole_fraction_<1,2-ethanediol>": "0",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0008385"
        },
        {
          "BLKpoint_id": "BLKpoint_80",
          "temperature_k": "308.15",
          "mole_fraction_<1,2-ethanediol>": "0",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.00075887"
        },
        {
          "BLKpoint_id": "BLKpoint_81",
          "temperature_k": "293.15",
          "mole_fraction_<1,2-ethanediol>": "1",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.020613"
        },
        {
          "BLKpoint_id": "BLKpoint_82",
          "temperature_k": "298.15",
          "mole_fraction_<1,2-ethanediol>": "1",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.016223"
        },
        {
          "BLKpoint_id": "BLKpoint_83",
          "temperature_k": "303.15",
          "mole_fraction_<1,2-ethanediol>": "1",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.013867"
        },
        {
          "BLKpoint_id": "BLKpoint_84",
          "temperature_k": "308.15",
          "mole_fraction_<1,2-ethanediol>": "1",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.011483"
        }
      ],
      "inspection_id": "INSP_10e84136b97d",
      "lit_num_id": "GLOBlit_5201"
    },
    {
      "doi": "10.1021/acs.jced.6b00526",
      "block_number": "PROPblock_18",
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
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.02113"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "0.2014",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.01495"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "0.4011",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.01005"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "0.6995",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.004584"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "1",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.000949"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.01724"
        },
        {
          "BLKpoint_id": "BLKpoint_14",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.2014",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.01219"
        },
        {
          "BLKpoint_id": "BLKpoint_16",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.4011",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00831"
        },
        {
          "BLKpoint_id": "BLKpoint_19",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.6995",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.003884"
        },
        {
          "BLKpoint_id": "BLKpoint_22",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "1",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.000843"
        },
        {
          "BLKpoint_id": "BLKpoint_23",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "0",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.01423"
        },
        {
          "BLKpoint_id": "BLKpoint_25",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "0.2014",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.01014"
        },
        {
          "BLKpoint_id": "BLKpoint_28",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "0.4969",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.005653"
        },
        {
          "BLKpoint_id": "BLKpoint_33",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "1",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.000755"
        }
      ],
      "inspection_id": "INSP_bdb58d28aae5",
      "lit_num_id": "GLOBlit_6951"
    },
    {
      "doi": "10.1021/je020140j",
      "block_number": "PROPblock_5",
      "table_mode": "rdp",
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
          "BLKpoint_id": "BLKpoint_7",
          "mole_fraction_<1,2-ethanediol>": "0",
          "temperature_k": "353.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.000356"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "mole_fraction_<1,2-ethanediol>": "0.0312",
          "temperature_k": "293.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001337"
        },
        {
          "BLKpoint_id": "BLKpoint_14",
          "mole_fraction_<1,2-ethanediol>": "0.0312",
          "temperature_k": "353.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.000434"
        },
        {
          "BLKpoint_id": "BLKpoint_15",
          "mole_fraction_<1,2-ethanediol>": "0.0676",
          "temperature_k": "293.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001785"
        },
        {
          "BLKpoint_id": "BLKpoint_21",
          "mole_fraction_<1,2-ethanediol>": "0.0676",
          "temperature_k": "353.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.000525"
        },
        {
          "BLKpoint_id": "BLKpoint_22",
          "mole_fraction_<1,2-ethanediol>": "0.1105",
          "temperature_k": "293.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.002272"
        },
        {
          "BLKpoint_id": "BLKpoint_24",
          "mole_fraction_<1,2-ethanediol>": "0.1105",
          "temperature_k": "313.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001319"
        },
        {
          "BLKpoint_id": "BLKpoint_28",
          "mole_fraction_<1,2-ethanediol>": "0.1105",
          "temperature_k": "353.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.000629"
        },
        {
          "BLKpoint_id": "BLKpoint_29",
          "mole_fraction_<1,2-ethanediol>": "0.162",
          "temperature_k": "293.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.002951"
        },
        {
          "BLKpoint_id": "BLKpoint_31",
          "mole_fraction_<1,2-ethanediol>": "0.162",
          "temperature_k": "313.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001677"
        },
        {
          "BLKpoint_id": "BLKpoint_35",
          "mole_fraction_<1,2-ethanediol>": "0.162",
          "temperature_k": "353.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.000758"
        },
        {
          "BLKpoint_id": "BLKpoint_36",
          "mole_fraction_<1,2-ethanediol>": "0.2248",
          "temperature_k": "293.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.003941"
        },
        {
          "BLKpoint_id": "BLKpoint_38",
          "mole_fraction_<1,2-ethanediol>": "0.2248",
          "temperature_k": "313.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.002132"
        },
        {
          "BLKpoint_id": "BLKpoint_42",
          "mole_fraction_<1,2-ethanediol>": "0.2248",
          "temperature_k": "353.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.000906"
        },
        {
          "BLKpoint_id": "BLKpoint_43",
          "mole_fraction_<1,2-ethanediol>": "0.3031",
          "temperature_k": "293.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.005102"
        },
        {
          "BLKpoint_id": "BLKpoint_45",
          "mole_fraction_<1,2-ethanediol>": "0.3031",
          "temperature_k": "313.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.002756"
        },
        {
          "BLKpoint_id": "BLKpoint_49",
          "mole_fraction_<1,2-ethanediol>": "0.3031",
          "temperature_k": "353.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0011"
        },
        {
          "BLKpoint_id": "BLKpoint_50",
          "mole_fraction_<1,2-ethanediol>": "0.4036",
          "temperature_k": "293.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.006898"
        },
        {
          "BLKpoint_id": "BLKpoint_52",
          "mole_fraction_<1,2-ethanediol>": "0.4036",
          "temperature_k": "313.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.003575"
        },
        {
          "BLKpoint_id": "BLKpoint_54",
          "mole_fraction_<1,2-ethanediol>": "0.4036",
          "temperature_k": "333.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.002053"
        },
        {
          "BLKpoint_id": "BLKpoint_56",
          "mole_fraction_<1,2-ethanediol>": "0.4036",
          "temperature_k": "353.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001359"
        },
        {
          "BLKpoint_id": "BLKpoint_57",
          "mole_fraction_<1,2-ethanediol>": "0.537",
          "temperature_k": "293.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.009696"
        },
        {
          "BLKpoint_id": "BLKpoint_58",
          "mole_fraction_<1,2-ethanediol>": "0.537",
          "temperature_k": "303.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.006749"
        },
        {
          "BLKpoint_id": "BLKpoint_59",
          "mole_fraction_<1,2-ethanediol>": "0.537",
          "temperature_k": "313.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.004776"
        },
        {
          "BLKpoint_id": "BLKpoint_61",
          "mole_fraction_<1,2-ethanediol>": "0.537",
          "temperature_k": "333.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.002684"
        },
        {
          "BLKpoint_id": "BLKpoint_63",
          "mole_fraction_<1,2-ethanediol>": "0.537",
          "temperature_k": "353.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001748"
        },
        {
          "BLKpoint_id": "BLKpoint_64",
          "mole_fraction_<1,2-ethanediol>": "0.723",
          "temperature_k": "293.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.014042"
        },
        {
          "BLKpoint_id": "BLKpoint_65",
          "mole_fraction_<1,2-ethanediol>": "0.723",
          "temperature_k": "303.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.009399"
        },
        {
          "BLKpoint_id": "BLKpoint_66",
          "mole_fraction_<1,2-ethanediol>": "0.723",
          "temperature_k": "313.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.006449"
        },
        {
          "BLKpoint_id": "BLKpoint_68",
          "mole_fraction_<1,2-ethanediol>": "0.723",
          "temperature_k": "333.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.00351"
        },
        {
          "BLKpoint_id": "BLKpoint_70",
          "mole_fraction_<1,2-ethanediol>": "0.723",
          "temperature_k": "353.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.002296"
        },
        {
          "BLKpoint_id": "BLKpoint_71",
          "mole_fraction_<1,2-ethanediol>": "1",
          "temperature_k": "293.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.020833"
        },
        {
          "BLKpoint_id": "BLKpoint_72",
          "mole_fraction_<1,2-ethanediol>": "1",
          "temperature_k": "303.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.013646"
        },
        {
          "BLKpoint_id": "BLKpoint_73",
          "mole_fraction_<1,2-ethanediol>": "1",
          "temperature_k": "313.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.009443"
        },
        {
          "BLKpoint_id": "BLKpoint_75",
          "mole_fraction_<1,2-ethanediol>": "1",
          "temperature_k": "333.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.00506"
        },
        {
          "BLKpoint_id": "BLKpoint_77",
          "mole_fraction_<1,2-ethanediol>": "1",
          "temperature_k": "353.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.003021"
        }
      ],
      "inspection_id": "INSP_ca607c3d05dd",
      "lit_num_id": "GLOBlit_8038"
    },
    {
      "doi": "10.1021/je800271e",
      "block_number": "PROPblock_4",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<1,2-ethanediol>",
        "viscosity_pa_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "308.15",
          "mole_fraction_<1,2-ethanediol>": "0",
          "viscosity_pa_s": "0.000721"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "temperature_k": "308.15",
          "mole_fraction_<1,2-ethanediol>": "0.1621",
          "viscosity_pa_s": "0.0015744"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "temperature_k": "308.15",
          "mole_fraction_<1,2-ethanediol>": "0.4035",
          "viscosity_pa_s": "0.0035116"
        },
        {
          "BLKpoint_id": "BLKpoint_13",
          "temperature_k": "308.15",
          "mole_fraction_<1,2-ethanediol>": "1",
          "viscosity_pa_s": "0.0092122"
        },
        {
          "BLKpoint_id": "BLKpoint_14",
          "temperature_k": "313.15",
          "mole_fraction_<1,2-ethanediol>": "0",
          "viscosity_pa_s": "0.0006532"
        },
        {
          "BLKpoint_id": "BLKpoint_21",
          "temperature_k": "313.15",
          "mole_fraction_<1,2-ethanediol>": "0.1621",
          "viscosity_pa_s": "0.0014047"
        },
        {
          "BLKpoint_id": "BLKpoint_24",
          "temperature_k": "313.15",
          "mole_fraction_<1,2-ethanediol>": "0.4035",
          "viscosity_pa_s": "0.0030166"
        },
        {
          "BLKpoint_id": "BLKpoint_26",
          "temperature_k": "313.15",
          "mole_fraction_<1,2-ethanediol>": "1",
          "viscosity_pa_s": "0.0079605"
        },
        {
          "BLKpoint_id": "BLKpoint_27",
          "temperature_k": "318.15",
          "mole_fraction_<1,2-ethanediol>": "0",
          "viscosity_pa_s": "0.00059"
        },
        {
          "BLKpoint_id": "BLKpoint_36",
          "temperature_k": "318.15",
          "mole_fraction_<1,2-ethanediol>": "0.3032",
          "viscosity_pa_s": "0.0018883"
        },
        {
          "BLKpoint_id": "BLKpoint_39",
          "temperature_k": "318.15",
          "mole_fraction_<1,2-ethanediol>": "1",
          "viscosity_pa_s": "0.0062933"
        },
        {
          "BLKpoint_id": "BLKpoint_40",
          "temperature_k": "323.15",
          "mole_fraction_<1,2-ethanediol>": "0",
          "viscosity_pa_s": "0.00055"
        },
        {
          "BLKpoint_id": "BLKpoint_49",
          "temperature_k": "323.15",
          "mole_fraction_<1,2-ethanediol>": "0.3032",
          "viscosity_pa_s": "0.0016786"
        },
        {
          "BLKpoint_id": "BLKpoint_52",
          "temperature_k": "323.15",
          "mole_fraction_<1,2-ethanediol>": "1",
          "viscosity_pa_s": "0.0054468"
        }
      ],
      "inspection_id": "INSP_5611a4a4b21d",
      "lit_num_id": "GLOBlit_11186"
    }
  ]
}
</subagent_answer>
```
</details>

---

### Step 4 [Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1)] [main - A_1 · c23]: `inspect_block` 🔒 VALIDATION BLOCKED

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1016/j.jct.2018.02.022",
  "block_number": "PROPblock_24",
  "purpose": "Verify column names and structure for fitting viscosity at 298.15 K"
}
```
</details>

- **Result:** 295 chars  |  **Time:** 0.0s  |  **Started:** 19:54:43 (t+333.8s)
- **Status:** blocked

<details><summary>Validation detail</summary>

```
**✗ inspect_block** — tool syntax or arguments need correction:
TOOL_ARGUMENT_REFINEMENT_REQUIRED: invalid call to inspect_block: missing a required argument: 'tasks'

_No tool in this batch executed. Re-emit the complete batch with only registered tool names and exact declared JSON arguments._
```
</details>

---

### Step 5 [Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1)] [main - A_1 · c24]: `inspect_block` 🔒 VALIDATION BLOCKED

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1016/j.jct.2018.02.022",
  "block_number": "PROPblock_24",
  "purpose": "Verify column names and structure for viscosity fitting at 298.15 K",
  "tasks": [
    "inspect block structure"
  ]
}
```
</details>

- **Result:** 349 chars  |  **Time:** 0.0s  |  **Started:** 19:54:48 (t+338.7s)
- **Status:** blocked

<details><summary>Validation detail</summary>

```
**✗ inspect_block** — tool syntax or arguments need correction:
TOOL_ARGUMENT_REFINEMENT_REQUIRED: inspect_block.tasks received ['inspect block structure'] (list); expected <class 'str'>; tool arguments are never coerced

_No tool in this batch executed. Re-emit the complete batch with only registered tool names and exact declared JSON arguments._
```
</details>

---

### Step 6 [Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1)] [main - A_1 · c25]: `inspect_block`

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1016/j.jct.2018.02.022",
  "block_number": "PROPblock_24",
  "purpose": "Verify column names and structure for viscosity fitting at 298.15 K",
  "tasks": "Inspect block structure, columns, value ranges, and row count"
}
```
</details>

- **Result:** 1,379 chars  |  **Time:** 0.4s  |  **Started:** 19:54:53 (t+343.8s)

<details><summary>Result</summary>

```
**Block GLOBlit_5201 / DOI 10.1016/j.jct.2018.02.022 / PROPblock_24 @ declared** (PureOrMixtureData)
Compounds: 1,2-ethanediol, water | Rows: 84
x‑columns: ['mole_fraction_<1,2-ethanediol>'] | y‑columns: ['viscosity_pa_s']

**Property response semantics (reported metadata; values are not materialized here)**
- **BLKprop_1 / GLOBprop_4** `viscosity_pa_s` (viscosity_pa_s)
  - reported response: Direct value, X
  - measurement: GLOBmeas_11 / concentric_cylinders_viscometry
  - property phase: Liquid (GLOBphase_1; liquid)
  - reference: none; T=unspecified K; P=unspecified kPa
  - reference phase: none
  - component_org_num: none

**Selected property response contract (inspection only; values are not materialized here)**
- **BLKprop_1 / GLOBprop_4** `viscosity_pa_s` (viscosity_pa_s)
  - reported response: Direct value, X [direct]
  - units: reported=Pa*s; absolute=Pa*s
  - preparation gate: reference_materialization=False; normalized_composition=False; supported=True
  - reference: none; T=unspecified K; P=unspecified kPa
  - property phase: Liquid (GLOBphase_1; liquid)
  - reference phase: none
  - component_org_num: none

| Column | Min | Max | Valid pts |
|--------|-----|-----|-----------|
| temperature_k | 293.15 | 308.15 | 84 |
| mole_fraction_<1,2-ethanediol> | 0 | 1 | 84 |
| pressure_kpa | 92.3 | 92.3 | 84 |
| viscosity_pa_s | 0.000759 | 0.020613 | 84 |

```
</details>

---

### Step 7 [Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1)] [main - A_1 · c26]: `fit_block` 🔒 VALIDATION BLOCKED

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1016/j.jct.2018.02.022",
  "block_number": "PROPblock_24",
  "property_hint": "viscosity",
  "property_type": "viscosity",
  "composition_hint": "mole_fraction",
  "max_rk_order": 5,
  "mixing_rule": "arrhenius",
  "x_vars": [
    "Mole fraction of 1,2-ethanediol"
  ],
  "y_props": [
    "Viscosity, Pa*s"
  ],
  "x_vars_constrained": {
    "Temperature, K": {
      "value": 298.15,
      "tol": 0.5
    }
  },
  "temperature_tolerance": 0.5
}
```
</details>

- **Result:** 289 chars  |  **Time:** 0.0s  |  **Started:** 19:55:03 (t+353.9s)
- **Status:** blocked

<details><summary>Validation detail</summary>

```
**✗ fit_block** — tool syntax or arguments need correction:
TOOL_ARGUMENT_REFINEMENT_REQUIRED: invalid call to fit_block: missing a required argument: 'purpose'

_No tool in this batch executed. Re-emit the complete batch with only registered tool names and exact declared JSON arguments._
```
</details>

---

### Step 8 [Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1)] [main - A_1 · c27]: `fit_block` 🔒 VALIDATION BLOCKED

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1016/j.jct.2018.02.022",
  "block_number": "PROPblock_24",
  "property_hint": "viscosity",
  "property_type": "viscosity",
  "composition_hint": "mole_fraction",
  "max_rk_order": 5,
  "mixing_rule": "arrhenius",
  "x_vars_constrained": {
    "Temperature, K": {
      "value": 298.15,
      "tol": 0.5
    }
  },
  "purpose": "Fit Redlich-Kister polynomial to dynamic viscosity of water + ethylene glycol at 298.15 K using Arrhenius mixing rule"
}
```
</details>

- **Result:** 287 chars  |  **Time:** 0.0s  |  **Started:** 19:55:15 (t+366.4s)
- **Status:** blocked

<details><summary>Validation detail</summary>

```
**✗ fit_block** — tool syntax or arguments need correction:
TOOL_ARGUMENT_REFINEMENT_REQUIRED: invalid call to fit_block: missing a required argument: 'tasks'

_No tool in this batch executed. Re-emit the complete batch with only registered tool names and exact declared JSON arguments._
```
</details>

---

### Step 9 [Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1)] [main - A_1 · c28]: `fit_block` 🔒 VALIDATION BLOCKED

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1016/j.jct.2018.02.022",
  "block_number": "PROPblock_24",
  "property_hint": "viscosity",
  "property_type": "viscosity",
  "mixing_rule": "arrhenius",
  "x_vars": [
    "Mole fraction of 1,2-ethanediol"
  ],
  "y_props": [
    "Viscosity, Pa*s"
  ],
  "x_vars_constrained": {
    "Temperature, K": {
      "value": 298.15,
      "tol": 0.5
    }
  },
  "max_rk_order": 5,
  "purpose": "Fit Redlich-Kister polynomial to dynamic viscosity of water + ethylene glycol at 298.15 K using Arrhenius mixing rule",
  "tasks": [
    "Fit RK polynomial to viscosity data at 298.15 K isotherm"
  ]
}
```
</details>

- **Result:** 374 chars  |  **Time:** 0.0s  |  **Started:** 19:55:22 (t+373.1s)
- **Status:** blocked

<details><summary>Validation detail</summary>

```
**✗ fit_block** — tool syntax or arguments need correction:
TOOL_ARGUMENT_REFINEMENT_REQUIRED: fit_block.tasks received ['Fit RK polynomial to viscosity data at 298.15 K isotherm'] (list); expected <class 'str'>; tool arguments are never coerced

_No tool in this batch executed. Re-emit the complete batch with only registered tool names and exact declared JSON arguments._
```
</details>

---

### Step 10 [Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1)] [main - A_1 · c29]: `fit_block`

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1016/j.jct.2018.02.022",
  "block_number": "PROPblock_24",
  "property_hint": "viscosity",
  "property_type": "viscosity",
  "mixing_rule": "arrhenius",
  "x_vars": [
    "Mole fraction of 1,2-ethanediol"
  ],
  "y_props": [
    "Viscosity, Pa*s"
  ],
  "x_vars_constrained": {
    "Temperature, K": {
      "value": 298.15,
      "tol": 0.5
    }
  },
  "max_rk_order": 5,
  "purpose": "Fit Redlich-Kister polynomial to dynamic viscosity of water + ethylene glycol at 298.15 K",
  "tasks": "Fit RK polynomial to viscosity data at 298.15 K isotherm using Arrhenius mixing rule"
}
```
</details>

- **Result:** 269 chars  |  **Time:** 0.1s  |  **Started:** 19:55:29 (t+380.2s)

<details><summary>Result</summary>

```
**Fit error** (GLOBlit_5201 / DOI 10.1016/j.jct.2018.02.022 / PROPblock_24): Requested x column 'Mole fraction of 1,2-ethanediol' not found in block
Columns available: ['BLKpoint_id', 'temperature_k', 'mole_fraction_<1,2-ethanediol>', 'pressure_kpa', 'viscosity_pa_s']

```
</details>

---

### Step 11 [Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1)] [main - A_1 · c30]: `fit_block`

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1016/j.jct.2018.02.022",
  "block_number": "PROPblock_24",
  "property_hint": "viscosity",
  "property_type": "viscosity",
  "mixing_rule": "arrhenius",
  "max_rk_order": 5,
  "x_vars": [
    "mole_fraction_<1,2-ethanediol>"
  ],
  "y_props": [
    "viscosity_pa_s"
  ],
  "x_vars_constrained": {
    "temperature_k": {
      "value": 298.15,
      "tol": 0.5
    }
  },
  "purpose": "Fit Redlich-Kister polynomial to dynamic viscosity of water + ethylene glycol at 298.15 K using Arrhenius mixing rule",
  "tasks": "fit_block"
}
```
</details>

- **Result:** 899 chars  |  **Time:** 2.0s  |  **Started:** 19:55:37 (t+387.8s)

<details><summary>Result</summary>

```
**RK Fit** — GLOBlit_5201 / DOI 10.1016/j.jct.2018.02.022 / PROPblock_24 @ declared
Components: 1,2-ethanediol, water | Mixing rule: arrhenius
Points: 19 mixture / 84 total
Property response: BLKprop_1 / GLOBprop_4; kind=direct; equation=X = reported X; reference_sources=0; units=Pa*s -> Pa*s.

| Component | Pure value |
|-----------|-----------|
| 1,2-ethanediol | 0.016223 |
| water | 0.00089689 |
Pure values: block-edges (water: direct/good, 1,2-ethanediol: direct/good)

BIC-selected order: 3 | R² = 0.999940 | RMSE = 0.00131989 | BIC = -240.17
Coefficients: [2.39674, -1.04444, 0.668173, -0.3209]

| Order | BIC | R² | RMSE |
|-------|-----|----|------|
| 0 | -90.89 | 0.751578 | 0.0846469 |
| 1 | -141.05 | 0.984821 | 0.0209237 |
| 2 | -194.71 | 0.999228 | 0.00471853 |
| 3 | -240.17 | 0.999940 | 0.00131989 |
| 4 | -237.59 | 0.999941 | 0.00130734 |
| 5 | -234.83 | 0.999941 | 0.00130104 |

```
</details>

---

## Nested tool calls — L1_1 (L1-query)

**Nest:** main - A_1 - L1_1
**Parent:** `query_thermoml` — Step 3 [main - A_1 · c22] relays this worker's result
**Started:** 19:49:31  |  **Ended:** 19:54:31  |  **Tool calls:** 19

---

### Step 1 [Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1)] [main - A_1 - L1_1 · c3]: `resolve_compound_ids`

<details><summary>Arguments</summary>

```json
{
  "queries": [
    "water",
    "ethylene glycol"
  ],
  "purpose": "Resolve compound IDs for water and ethylene glycol",
  "tasks": "Find global IDs for water and ethylene glycol (1,2-ethanediol)"
}
```
</details>

- **Result:** 193 chars  |  **Time:** 4.1s  |  **Started:** 19:49:36 (t+26.8s)
- **Subagent:** KEEP in 288 → 193 chars (4.0s)
  - Both compounds resolved with exact name matches.

| Compound | Global ID | Formula | SMILES |
|---|---|---|---|
| water | GLOBcomp_1 | H2O | O |
| 1,2-ethanediol | GLOBcomp_24 | C2H6O2 | OCCO |

<details><summary>Result</summary>

```
Both compounds resolved with exact name matches.

| Compound | Global ID | Formula | SMILES |
|---|---|---|---|
| water | GLOBcomp_1 | H2O | O |
| 1,2-ethanediol | GLOBcomp_24 | C2H6O2 | OCCO |
```
</details>

---

### Step 3 [Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1)] [main - A_1 - L1_1 · c4]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_1",
    "GLOBcomp_24"
  ],
  "property": "GLOBprop_4",
  "system_type": "binary",
  "temperature_range": [
    290.0,
    310.0
  ],
  "limit": 50,
  "purpose": "Find dynamic viscosity data blocks for water + ethylene glycol binary near 298.15 K",
  "tasks": "Search for blocks with GLOBprop_4 in binary water+ethylene glycol system"
}
```
</details>

- **Result:** 1,273 chars  |  **Time:** 19.9s  |  **Started:** 19:49:53 (t+44.2s)
- **Subagent:** KEEP in 9,915 → 1,273 chars (13.9s)
  - **Summary:** 7 viscosity (GLOBprop_4) blocks found for the water (GLOBcomp_1) + ethylene glycol (GLOBcomp_24) binary system in the 290–310 K range, all scoring 100. Coverage ranges from 10 to 84 point

<details><summary>Result</summary>

```
**Summary:** 7 viscosity (GLOBprop_4) blocks found for the water (GLOBcomp_1) + ethylene glycol (GLOBcomp_24) binary system in the 290–310 K range, all scoring 100. Coverage ranges from 10 to 84 points per block, with varying composition variables (mole fraction or mass fraction).

| # | DOI | Block | GLOBlit | Pts | T range (K) | Composition var | P (kPa) | Method |
|---|-----|-------|---------|-----|-------------|-----------------|---------|--------|
| 1 | 10.1016/j.jct.2006.01.011 | PROPblock_13 | GLOBlit_2656 | 10 | 293.15 (fixed) | mass_fraction EG | 101.325 | capillary_tube_ostwald_ubbelohde |
| 2 | 10.1016/j.jct.2018.02.022 | PROPblock_24 | GLOBlit_5201 | 84 | 293.15–303.15 | mole_fraction EG (0.0494–0.9532) | 92.3 | concentric_cylinders |
| 3 | 10.1021/acs.jced.6b00526 | PROPblock_18 | GLOBlit_6951 | 33 | 293.15–303.15 | mole_fraction water (0.0–1.0) | 100.0 | falling_or_rolling_sphere |
| 4 | 10.1021/je020140j | PROPblock_5 | GLOBlit_8038 | 77 | 293.15–353.15 | mole_fraction EG (0.0–0.4036) | 101.0 | captub_ufactor_3 |
| 5 | 10.1021/je025610o | PROPblock_5 | GLOBlit_8106 | 30 | 296.45–449.85 | mole_fraction EG (0.25–0.75) | 100.0 | captub_ufactor_4 |
| 6 | 10.1021/je800271e | PROPblock_4 | GLOBlit_11186 | 52 | 308.15–323.15 | mole_fraction EG (
```
</details>

---

### Step 3 [Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1)] [main - A_1 - L1_1 · c5]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_1",
    "GLOBcomp_24"
  ],
  "property": "GLOBprop_40",
  "system_type": "binary",
  "temperature_range": [
    290.0,
    310.0
  ],
  "limit": 50,
  "purpose": "Find kinematic viscosity data blocks for water + ethylene glycol binary near 298.15 K",
  "tasks": "Search for blocks with GLOBprop_40 in binary water+ethylene glycol system"
}
```
</details>

- **Result:** 1,162 chars  |  **Time:** 14.9s  |  **Started:** 19:50:13 (t+64.1s)
- **Subagent:** DISCARD in 39 → 1,162 chars (9.4s)
  - 1. **Explanation:** The search returned zero results for kinematic viscosity (GLOBprop_40) in the binary water (GLOBcomp_1) + ethylene glycol (GLOBcomp_24) system within 290–310 K. This means either n

<details><summary>Result</summary>

```
**⚠ Tool `search_blocks` result discarded by subagent.**

1. **Explanation:** The search returned zero results for kinematic viscosity (GLOBprop_40) in the binary water (GLOBcomp_1) + ethylene glycol (GLOBcomp_24) system within 290–310 K. This means either no ThermoML entries exist for this specific property/system combination, or the compound/property IDs may not match available data.

2. **Refinement suggestions:**
   - **Try dynamic viscosity instead:** Search with the dynamic viscosity property ID (e.g., GLOBprop_29 or whichever maps to dynamic/absolute viscosity), as ThermoML datasets more commonly report dynamic viscosity rather than kinematic viscosity for aqueous mixtures.
   - **Broaden the temperature range:** Widen to e.g. 273–373 K to check if any kinematic viscosity data exists at other temperatures.
   - **Remove temperature constraint:** Search without `temperature_range` to see if any blocks at all exist for GLOBprop_40 with these two compounds.
   - **Verify compound ID:** Confirm that GLOBcomp_24 correctly maps to ethylene glycol (1,2-ethanediol) — try searching with just one compound or using an alternative identifier lookup.
```
</details>

---

### Step 5 [Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1)] [main - A_1 - L1_1 · c6]: `inspect_block_table` ❌ ERROR

<details><summary>Arguments</summary>

```json
{
  "block_number": "PROPblock_13",
  "literature": "GLOBlit_2656",
  "nearest": "Temperature = 298.15 K",
  "purpose": "Ground viscosity data values for water+EG binary",
  "tasks": "Return data rows near 298.15 K"
}
```
</details>

- **Result:** 261 chars  |  **Time:** 0.0s  |  **Started:** 19:52:00 (t+171.6s)
- **Error:** `{
  "error": "TOOL_ARGUMENT_REFINEMENT_REQUIRED: inspect_block_table.nearest received 'Temperature = 298.15 K' (str); expected dict | None; tool arguments are never coerced",
  "error_code": "TOOL_ARGUMENT_REFINEMENT_REQUIRED",
  "tool": "inspect_block_table"
}`

---

### Step 5 [Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1)] [main - A_1 - L1_1 · c7]: `inspect_block_table` ❌ ERROR

<details><summary>Arguments</summary>

```json
{
  "block_number": "PROPblock_24",
  "literature": "GLOBlit_5201",
  "nearest": "Temperature = 298.15 K",
  "purpose": "Ground viscosity data values for water+EG binary",
  "tasks": "Return data rows near 298.15 K"
}
```
</details>

- **Result:** 261 chars  |  **Time:** 0.0s  |  **Started:** 19:52:01 (t+171.6s)
- **Error:** `{
  "error": "TOOL_ARGUMENT_REFINEMENT_REQUIRED: inspect_block_table.nearest received 'Temperature = 298.15 K' (str); expected dict | None; tool arguments are never coerced",
  "error_code": "TOOL_ARGUMENT_REFINEMENT_REQUIRED",
  "tool": "inspect_block_table"
}`

---

### Step 5 [Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1)] [main - A_1 - L1_1 · c8]: `inspect_block_table` ❌ ERROR

<details><summary>Arguments</summary>

```json
{
  "block_number": "PROPblock_18",
  "literature": "GLOBlit_6951",
  "nearest": "Temperature = 298.15 K",
  "purpose": "Ground viscosity data values for water+EG binary",
  "tasks": "Return data rows near 298.15 K"
}
```
</details>

- **Result:** 261 chars  |  **Time:** 0.0s  |  **Started:** 19:52:01 (t+171.7s)
- **Error:** `{
  "error": "TOOL_ARGUMENT_REFINEMENT_REQUIRED: inspect_block_table.nearest received 'Temperature = 298.15 K' (str); expected dict | None; tool arguments are never coerced",
  "error_code": "TOOL_ARGUMENT_REFINEMENT_REQUIRED",
  "tool": "inspect_block_table"
}`

---

### Step 5 [Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1)] [main - A_1 - L1_1 · c9]: `inspect_block_table` ❌ ERROR

<details><summary>Arguments</summary>

```json
{
  "block_number": "PROPblock_5",
  "literature": "GLOBlit_8038",
  "nearest": "Temperature = 298.15 K",
  "purpose": "Ground viscosity data values for water+EG binary",
  "tasks": "Return data rows near 298.15 K"
}
```
</details>

- **Result:** 261 chars  |  **Time:** 0.0s  |  **Started:** 19:52:01 (t+171.8s)
- **Error:** `{
  "error": "TOOL_ARGUMENT_REFINEMENT_REQUIRED: inspect_block_table.nearest received 'Temperature = 298.15 K' (str); expected dict | None; tool arguments are never coerced",
  "error_code": "TOOL_ARGUMENT_REFINEMENT_REQUIRED",
  "tool": "inspect_block_table"
}`

---

### Step 5 [Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1)] [main - A_1 - L1_1 · c10]: `inspect_block_table` ❌ ERROR

<details><summary>Arguments</summary>

```json
{
  "block_number": "PROPblock_4",
  "literature": "GLOBlit_11186",
  "nearest": "Temperature = 298.15 K",
  "purpose": "Ground viscosity data values for water+EG binary",
  "tasks": "Return data rows near 298.15 K"
}
```
</details>

- **Result:** 261 chars  |  **Time:** 0.0s  |  **Started:** 19:52:01 (t+171.9s)
- **Error:** `{
  "error": "TOOL_ARGUMENT_REFINEMENT_REQUIRED: inspect_block_table.nearest received 'Temperature = 298.15 K' (str); expected dict | None; tool arguments are never coerced",
  "error_code": "TOOL_ARGUMENT_REFINEMENT_REQUIRED",
  "tool": "inspect_block_table"
}`

---

### Step 6 [Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1)] [main - A_1 - L1_1 · c11]: `inspect_block_table`

<details><summary>Arguments</summary>

```json
{
  "block_number": "PROPblock_13",
  "literature": "GLOBlit_2656",
  "nearest": {
    "Temperature": 298.15
  },
  "purpose": "Inspect viscosity block for water+EG",
  "tasks": "Get data points near 298.15 K"
}
```
</details>

- **Result:** 384 chars  |  **Time:** 0.1s  |  **Started:** 19:52:08 (t+179.6s)

<details><summary>Result</summary>

```
**inspect_block_table error** — nearest must be {"column": alias, "value": number, "k": 1..8}

| alias | n_finite | min | max |
|---|---|---|---|
| mass_fraction_1_2_ethanediol | 10 | 0 | 0.9 |
| temperature_k | 10 | 293.15 | 293.15 |
| pressure_kpa | 10 | 101.325 | 101.325 |
| viscosity_pa_s | 10 | 0.001008 | 0.013999 |

Use these aliases in `where` / `nearest` with plain numbers.
```
</details>

---

### Step 6 [Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1)] [main - A_1 - L1_1 · c12]: `inspect_block_table`

<details><summary>Arguments</summary>

```json
{
  "block_number": "PROPblock_24",
  "literature": "GLOBlit_5201",
  "nearest": {
    "Temperature": 298.15
  },
  "purpose": "Inspect viscosity block for water+EG",
  "tasks": "Get data points near 298.15 K"
}
```
</details>

- **Result:** 378 chars  |  **Time:** 0.1s  |  **Started:** 19:52:09 (t+179.8s)

<details><summary>Result</summary>

```
**inspect_block_table error** — nearest must be {"column": alias, "value": number, "k": 1..8}

| alias | n_finite | min | max |
|---|---|---|---|
| temperature_k | 84 | 293.15 | 308.15 |
| mole_fraction_1_2_ethanediol | 84 | 0 | 1 |
| pressure_kpa | 84 | 92.3 | 92.3 |
| viscosity_pa_s | 84 | 0.00075887 | 0.020613 |

Use these aliases in `where` / `nearest` with plain numbers.
```
</details>

---

### Step 6 [Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1)] [main - A_1 - L1_1 · c13]: `inspect_block_table`

<details><summary>Arguments</summary>

```json
{
  "block_number": "PROPblock_18",
  "literature": "GLOBlit_6951",
  "nearest": {
    "Temperature": 298.15
  },
  "purpose": "Inspect viscosity block for water+EG",
  "tasks": "Get data points near 298.15 K"
}
```
</details>

- **Result:** 364 chars  |  **Time:** 0.2s  |  **Started:** 19:52:09 (t+179.9s)

<details><summary>Result</summary>

```
**inspect_block_table error** — nearest must be {"column": alias, "value": number, "k": 1..8}

| alias | n_finite | min | max |
|---|---|---|---|
| temperature_k | 33 | 293.15 | 303.15 |
| mole_fraction_water | 33 | 0 | 1 |
| pressure_kpa | 33 | 100 | 100 |
| viscosity_pa_s | 33 | 0.000755 | 0.02113 |

Use these aliases in `where` / `nearest` with plain numbers.
```
</details>

---

### Step 6 [Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1)] [main - A_1 - L1_1 · c14]: `inspect_block_table`

<details><summary>Arguments</summary>

```json
{
  "block_number": "PROPblock_5",
  "literature": "GLOBlit_8038",
  "nearest": {
    "Temperature": 298.15
  },
  "purpose": "Inspect viscosity block for water+EG",
  "tasks": "Get data points near 298.15 K"
}
```
</details>

- **Result:** 374 chars  |  **Time:** 0.1s  |  **Started:** 19:52:09 (t+180.3s)

<details><summary>Result</summary>

```
**inspect_block_table error** — nearest must be {"column": alias, "value": number, "k": 1..8}

| alias | n_finite | min | max |
|---|---|---|---|
| mole_fraction_1_2_ethanediol | 77 | 0 | 1 |
| temperature_k | 77 | 293.15 | 353.15 |
| pressure_kpa | 77 | 101 | 101 |
| viscosity_pa_s | 77 | 0.000356 | 0.020833 |

Use these aliases in `where` / `nearest` with plain numbers.
```
</details>

---

### Step 6 [Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1)] [main - A_1 - L1_1 · c15]: `inspect_block_table`

<details><summary>Arguments</summary>

```json
{
  "block_number": "PROPblock_4",
  "literature": "GLOBlit_11186",
  "nearest": {
    "Temperature": 298.15
  },
  "purpose": "Inspect viscosity block for water+EG",
  "tasks": "Get data points near 298.15 K"
}
```
</details>

- **Result:** 340 chars  |  **Time:** 0.1s  |  **Started:** 19:52:09 (t+180.5s)

<details><summary>Result</summary>

```
**inspect_block_table error** — nearest must be {"column": alias, "value": number, "k": 1..8}

| alias | n_finite | min | max |
|---|---|---|---|
| temperature_k | 52 | 308.15 | 323.15 |
| mole_fraction_1_2_ethanediol | 52 | 0 | 1 |
| viscosity_pa_s | 52 | 0.00055 | 0.0092122 |

Use these aliases in `where` / `nearest` with plain numbers.
```
</details>

---

### Step 7 [Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1)] [main - A_1 - L1_1 · c16]: `inspect_block_table`

<details><summary>Arguments</summary>

```json
{
  "block_number": "PROPblock_5",
  "literature": "GLOBlit_8106",
  "purpose": "Inspect viscosity block for water+EG binary from GLOBlit_8106",
  "tasks": "Get column stats for temperature, composition, viscosity"
}
```
</details>

- **Result:** 1,513 chars  |  **Time:** 0.1s  |  **Started:** 19:52:52 (t+222.7s)

<details><summary>Result</summary>

```
**Data inspection** — 10.1021/je025610o [GLOBlit_8106] :: PROPblock_5 (binary: 1,2-ethanediol + water)
filter: none (whole block)
block constraints: pressure_kpa = 100.0

| BLKpoint_id | mole_fraction_<1,2-ethanediol> | temperature_k | pressure_kpa | viscosity_pa_s |
|---|---|---|---|---|
| BLKpoint_1 | 0.25 | 296.45 | 100.0 | 0.00369 |
| BLKpoint_2 | 0.25 | 313.05 | 100.0 | 0.00229 |
| BLKpoint_4 | 0.25 | 353.05 | 100.0 | 0.00099 |
| BLKpoint_8 | 0.25 | 435.55 | 100.0 | 0.000366 |
| BLKpoint_9 | 0.5 | 297.05 | 100.0 | 0.00761 |
| BLKpoint_10 | 0.5 | 313.05 | 100.0 | 0.00449 |
| BLKpoint_11 | 0.5 | 333.1 | 100.0 | 0.00262 |
| BLKpoint_12 | 0.5 | 353.05 | 100.0 | 0.0017 |
| BLKpoint_13 | 0.5 | 380.05 | 100.0 | 0.00107 |
| BLKpoint_17 | 0.5 | 440.65 | 100.0 | 0.0005 |
| BLKpoint_18 | 0.75 | 297.35 | 100.0 | 0.0123 |
| BLKpoint_19 | 0.75 | 313.05 | 100.0 | 0.00697 |
| BLKpoint_20 | 0.75 | 333.1 | 100.0 | 0.00388 |
| BLKpoint_21 | 0.75 | 353.05 | 100.0 | 0.00242 |
| BLKpoint_22 | 0.75 | 373.45 | 100.0 | 0.00162 |
| BLKpoint_30 | 0.75 | 449.85 | 100.0 | 0.000594 |

mode: RDP — 16 of 30 matched rows shown (shape-preserving; block has 30). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
stats (matched, n=30): mole_fraction_1_2_ethanediol 0.25–0.75 (n=30); temperature_k 296.45–449.85 (n=30); pressure_kpa 100.0–100.0 (n=30); viscosity_pa_s 0.000366–0.0123 (n=30)
inspection_id: INSP_475115ec48f0
Data points may be quoted ONLY verbatim from the table above or the stats lines.
```
</details>

---

### Step 9 [Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1)] [main - A_1 - L1_1 · c17]: `inspect_block_table`

<details><summary>Arguments</summary>

```json
{
  "block_number": "GLOBlit_2656::PROPblock_13",
  "purpose": "Ground values for PROPblock_13",
  "tasks": "Inspect block table"
}
```
</details>

- **Result:** 1,253 chars  |  **Time:** 0.1s  |  **Started:** 19:53:24 (t+255.4s)

<details><summary>Result</summary>

```
**Data inspection** — 10.1016/j.jct.2006.01.011 [GLOBlit_2656] :: PROPblock_13 (binary: 1,2-ethanediol + water)
filter: none (whole block)
block constraints: temperature_k = 293.15; pressure_kpa = 101.325

| BLKpoint_id | mass_fraction_<1,2-ethanediol> | temperature_k | pressure_kpa | viscosity_pa_s |
|---|---|---|---|---|
| BLKpoint_1 | 0 | 293.15 | 101.325 | 0.001008 |
| BLKpoint_2 | 0.1 | 293.15 | 101.325 | 0.001293 |
| BLKpoint_3 | 0.2 | 293.15 | 101.325 | 0.001671 |
| BLKpoint_4 | 0.3 | 293.15 | 101.325 | 0.002177 |
| BLKpoint_5 | 0.4 | 293.15 | 101.325 | 0.002837 |
| BLKpoint_6 | 0.5 | 293.15 | 101.325 | 0.003558 |
| BLKpoint_7 | 0.6 | 293.15 | 101.325 | 0.004724 |
| BLKpoint_8 | 0.7 | 293.15 | 101.325 | 0.00636 |
| BLKpoint_9 | 0.8 | 293.15 | 101.325 | 0.008003 |
| BLKpoint_10 | 0.9 | 293.15 | 101.325 | 0.013999 |

mode: complete — all 10 matched rows shown (block has 10)
topology: viscosity_pa_s vs mass_fraction_1_2_ethanediol: monotonic↑
stats (matched, n=10): mass_fraction_1_2_ethanediol 0–0.9 (n=10); temperature_k 293.15–293.15 (n=10); pressure_kpa 101.325–101.325 (n=10); viscosity_pa_s 0.001008–0.013999 (n=10)
inspection_id: INSP_eb6a6a268c1a
Data points may be quoted ONLY verbatim from the table above or the stats lines.
```
</details>

---

### Step 9 [Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1)] [main - A_1 - L1_1 · c18]: `inspect_block_table`

<details><summary>Arguments</summary>

```json
{
  "block_number": "GLOBlit_5201::PROPblock_24",
  "purpose": "Ground values for PROPblock_24",
  "tasks": "Inspect block table"
}
```
</details>

- **Result:** 1,481 chars  |  **Time:** 0.1s  |  **Started:** 19:53:24 (t+255.5s)

<details><summary>Result</summary>

```
**Data inspection** — 10.1016/j.jct.2018.02.022 [GLOBlit_5201] :: PROPblock_24 (binary: 1,2-ethanediol + water)
filter: none (whole block)
block constraints: pressure_kpa = 92.3

| BLKpoint_id | temperature_k | mole_fraction_<1,2-ethanediol> | pressure_kpa | viscosity_pa_s |
|---|---|---|---|---|
| BLKpoint_1 | 293.15 | 0.0494 | 92.3 | 0.0015411 |
| BLKpoint_4 | 293.15 | 0.2072 | 92.3 | 0.0035171 |
| BLKpoint_9 | 293.15 | 0.4446 | 92.3 | 0.0076382 |
| BLKpoint_23 | 298.15 | 0.2072 | 92.3 | 0.0028109 |
| BLKpoint_28 | 298.15 | 0.4446 | 92.3 | 0.0060624 |
| BLKpoint_47 | 303.15 | 0.4446 | 92.3 | 0.0053492 |
| BLKpoint_65 | 308.15 | 0.3921 | 92.3 | 0.0040265 |
| BLKpoint_77 | 293.15 | 0 | 92.3 | 0.0010673 |
| BLKpoint_78 | 298.15 | 0 | 92.3 | 0.00089689 |
| BLKpoint_79 | 303.15 | 0 | 92.3 | 0.0008385 |
| BLKpoint_80 | 308.15 | 0 | 92.3 | 0.00075887 |
| BLKpoint_81 | 293.15 | 1 | 92.3 | 0.020613 |
| BLKpoint_82 | 298.15 | 1 | 92.3 | 0.016223 |
| BLKpoint_83 | 303.15 | 1 | 92.3 | 0.013867 |
| BLKpoint_84 | 308.15 | 1 | 92.3 | 0.011483 |

mode: RDP — 15 of 84 matched rows shown (shape-preserving; block has 84). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
stats (matched, n=84): temperature_k 293.15–308.15 (n=84); mole_fraction_1_2_ethanediol 0–1 (n=84); pressure_kpa 92.3–92.3 (n=84); viscosity_pa_s 0.00075887–0.020613 (n=84)
inspection_id: INSP_10e84136b97d
Data points may be quoted ONLY verbatim from the table above or the stats lines.
```
</details>

---

### Step 9 [Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1)] [main - A_1 - L1_1 · c19]: `inspect_block_table`

<details><summary>Arguments</summary>

```json
{
  "block_number": "GLOBlit_6951::PROPblock_18",
  "purpose": "Ground values for PROPblock_18",
  "tasks": "Inspect block table"
}
```
</details>

- **Result:** 1,412 chars  |  **Time:** 0.1s  |  **Started:** 19:53:25 (t+255.7s)

<details><summary>Result</summary>

```
**Data inspection** — 10.1021/acs.jced.6b00526 [GLOBlit_6951] :: PROPblock_18 (binary: 1,2-ethanediol + water)
filter: none (whole block)
block constraints: pressure_kpa = 100.0

| BLKpoint_id | temperature_k | mole_fraction_<water> | pressure_kpa | viscosity_pa_s |
|---|---|---|---|---|
| BLKpoint_1 | 293.15 | 0 | 100.0 | 0.02113 |
| BLKpoint_3 | 293.15 | 0.2014 | 100.0 | 0.01495 |
| BLKpoint_5 | 293.15 | 0.4011 | 100.0 | 0.01005 |
| BLKpoint_8 | 293.15 | 0.6995 | 100.0 | 0.004584 |
| BLKpoint_11 | 293.15 | 1 | 100.0 | 0.000949 |
| BLKpoint_12 | 298.15 | 0 | 100.0 | 0.01724 |
| BLKpoint_14 | 298.15 | 0.2014 | 100.0 | 0.01219 |
| BLKpoint_16 | 298.15 | 0.4011 | 100.0 | 0.00831 |
| BLKpoint_19 | 298.15 | 0.6995 | 100.0 | 0.003884 |
| BLKpoint_22 | 298.15 | 1 | 100.0 | 0.000843 |
| BLKpoint_23 | 303.15 | 0 | 100.0 | 0.01423 |
| BLKpoint_25 | 303.15 | 0.2014 | 100.0 | 0.01014 |
| BLKpoint_28 | 303.15 | 0.4969 | 100.0 | 0.005653 |
| BLKpoint_33 | 303.15 | 1 | 100.0 | 0.000755 |

mode: RDP — 14 of 33 matched rows shown (shape-preserving; block has 33). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
stats (matched, n=33): temperature_k 293.15–303.15 (n=33); mole_fraction_water 0–1 (n=33); pressure_kpa 100.0–100.0 (n=33); viscosity_pa_s 0.000755–0.02113 (n=33)
inspection_id: INSP_bdb58d28aae5
Data points may be quoted ONLY verbatim from the table above or the stats lines.
```
</details>

---

### Step 9 [Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1)] [main - A_1 - L1_1 · c20]: `inspect_block_table`

<details><summary>Arguments</summary>

```json
{
  "block_number": "GLOBlit_8038::PROPblock_5",
  "purpose": "Ground values for PROPblock_5 GLOBlit_8038",
  "tasks": "Inspect block table"
}
```
</details>

- **Result:** 2,629 chars  |  **Time:** 0.1s  |  **Started:** 19:53:25 (t+255.9s)

<details><summary>Result</summary>

```
**Data inspection** — 10.1021/je020140j [GLOBlit_8038] :: PROPblock_5 (binary: 1,2-ethanediol + water)
filter: none (whole block)
block constraints: pressure_kpa = 101.0

| BLKpoint_id | mole_fraction_<1,2-ethanediol> | temperature_k | pressure_kpa | viscosity_pa_s |
|---|---|---|---|---|
| BLKpoint_1 | 0 | 293.15 | 101.0 | 0.001002 |
| BLKpoint_7 | 0 | 353.15 | 101.0 | 0.000356 |
| BLKpoint_8 | 0.0312 | 293.15 | 101.0 | 0.001337 |
| BLKpoint_14 | 0.0312 | 353.15 | 101.0 | 0.000434 |
| BLKpoint_15 | 0.0676 | 293.15 | 101.0 | 0.001785 |
| BLKpoint_21 | 0.0676 | 353.15 | 101.0 | 0.000525 |
| BLKpoint_22 | 0.1105 | 293.15 | 101.0 | 0.002272 |
| BLKpoint_24 | 0.1105 | 313.15 | 101.0 | 0.001319 |
| BLKpoint_28 | 0.1105 | 353.15 | 101.0 | 0.000629 |
| BLKpoint_29 | 0.162 | 293.15 | 101.0 | 0.002951 |
| BLKpoint_31 | 0.162 | 313.15 | 101.0 | 0.001677 |
| BLKpoint_35 | 0.162 | 353.15 | 101.0 | 0.000758 |
| BLKpoint_36 | 0.2248 | 293.15 | 101.0 | 0.003941 |
| BLKpoint_38 | 0.2248 | 313.15 | 101.0 | 0.002132 |
| BLKpoint_42 | 0.2248 | 353.15 | 101.0 | 0.000906 |
| BLKpoint_43 | 0.3031 | 293.15 | 101.0 | 0.005102 |
| BLKpoint_45 | 0.3031 | 313.15 | 101.0 | 0.002756 |
| BLKpoint_49 | 0.3031 | 353.15 | 101.0 | 0.0011 |
| BLKpoint_50 | 0.4036 | 293.15 | 101.0 | 0.006898 |
| BLKpoint_52 | 0.4036 | 313.15 | 101.0 | 0.003575 |
| BLKpoint_54 | 0.4036 | 333.15 | 101.0 | 0.002053 |
| BLKpoint_56 | 0.4036 | 353.15 | 101.0 | 0.001359 |
| BLKpoint_57 | 0.537 | 293.15 | 101.0 | 0.009696 |
| BLKpoint_58 | 0.537 | 303.15 | 101.0 | 0.006749 |
| BLKpoint_59 | 0.537 | 313.15 | 101.0 | 0.004776 |
| BLKpoint_61 | 0.537 | 333.15 | 101.0 | 0.002684 |
| BLKpoint_63 | 0.537 | 353.15 | 101.0 | 0.001748 |
| BLKpoint_64 | 0.723 | 293.15 | 101.0 | 0.014042 |
| BLKpoint_65 | 0.723 | 303.15 | 101.0 | 0.009399 |
| BLKpoint_66 | 0.723 | 313.15 | 101.0 | 0.006449 |
| BLKpoint_68 | 0.723 | 333.15 | 101.0 | 0.00351 |
| BLKpoint_70 | 0.723 | 353.15 | 101.0 | 0.002296 |
| BLKpoint_71 | 1 | 293.15 | 101.0 | 0.020833 |
| BLKpoint_72 | 1 | 303.15 | 101.0 | 0.013646 |
| BLKpoint_73 | 1 | 313.15 | 101.0 | 0.009443 |
| BLKpoint_75 | 1 | 333.15 | 101.0 | 0.00506 |
| BLKpoint_77 | 1 | 353.15 | 101.0 | 0.003021 |

mode: RDP — 37 of 77 matched rows shown (shape-preserving; block has 77). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
stats (matched, n=77): mole_fraction_1_2_ethanediol 0–1 (n=77); temperature_k 293.15–353.15 (n=77); pressure_kpa 101.0–101.0 (n=77); viscosity_pa_s 0.000356–0.020833 (n=77)
inspection_id: INSP_ca607c3d05dd
Data points may be quoted ONLY verbatim from the table above or the stats lines.
```
</details>

---

### Step 9 [Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1)] [main - A_1 - L1_1 · c21]: `inspect_block_table`

<details><summary>Arguments</summary>

```json
{
  "block_number": "GLOBlit_11186::PROPblock_4",
  "purpose": "Ground values for PROPblock_4",
  "tasks": "Inspect block table"
}
```
</details>

- **Result:** 1,229 chars  |  **Time:** 0.1s  |  **Started:** 19:53:25 (t+256.0s)

<details><summary>Result</summary>

```
**Data inspection** — 10.1021/je800271e [GLOBlit_11186] :: PROPblock_4 (binary: 1,2-ethanediol + water)
filter: none (whole block)

| BLKpoint_id | temperature_k | mole_fraction_<1,2-ethanediol> | viscosity_pa_s |
|---|---|---|---|
| BLKpoint_1 | 308.15 | 0 | 0.000721 |
| BLKpoint_8 | 308.15 | 0.1621 | 0.0015744 |
| BLKpoint_11 | 308.15 | 0.4035 | 0.0035116 |
| BLKpoint_13 | 308.15 | 1 | 0.0092122 |
| BLKpoint_14 | 313.15 | 0 | 0.0006532 |
| BLKpoint_21 | 313.15 | 0.1621 | 0.0014047 |
| BLKpoint_24 | 313.15 | 0.4035 | 0.0030166 |
| BLKpoint_26 | 313.15 | 1 | 0.0079605 |
| BLKpoint_27 | 318.15 | 0 | 0.00059 |
| BLKpoint_36 | 318.15 | 0.3032 | 0.0018883 |
| BLKpoint_39 | 318.15 | 1 | 0.0062933 |
| BLKpoint_40 | 323.15 | 0 | 0.00055 |
| BLKpoint_49 | 323.15 | 0.3032 | 0.0016786 |
| BLKpoint_52 | 323.15 | 1 | 0.0054468 |

mode: RDP — 14 of 52 matched rows shown (shape-preserving; block has 52). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
stats (matched, n=52): temperature_k 308.15–323.15 (n=52); mole_fraction_1_2_ethanediol 0–1 (n=52); viscosity_pa_s 0.00055–0.0092122 (n=52)
inspection_id: INSP_5611a4a4b21d
Data points may be quoted ONLY verbatim from the table above or the stats lines.
```
</details>

**🔀 Stage compaction** (batch of 5 tools)
- 8,132 → 1,584 chars (−81%)

---

## Stage Compaction Summary (1 events)

| Iter | Tools | Before | After | Reduction |
|------|-------|--------|-------|-----------|
| 9 | 5 | 8,132 | 1,584 | −81% |

## Tool Compaction Pipeline (17 calls)

| # | Tool | Pipeline | Native | Hardcoded | Agentic | Verdict | Native→Final | Section |
|--:|------|----------|-------:|----------:|--------:|---------|-------------:|---------|
| 1 | `resolve_compound_ids` | query | 574 | 288 | 193 | KEEP | −66% | L1_1 |
| 2 | `search_blocks` | query | 43,758 | 9,915 | 1,273 | KEEP | −97% | L1_1 |
| 3 | `search_blocks` | query | 222 | 39 | 1,162 | DISCARD | −-423% | L1_1 |
| 4 | `inspect_block_table` | query | 1,151 | 384 | 384 | SKIP | −67% | L1_1 |
| 5 | `inspect_block_table` | query | 1,139 | 378 | 378 | SKIP | −67% | L1_1 |
| 6 | `inspect_block_table` | query | 1,101 | 364 | 364 | SKIP | −67% | L1_1 |
| 7 | `inspect_block_table` | query | 1,122 | 374 | 374 | SKIP | −67% | L1_1 |
| 8 | `inspect_block_table` | query | 991 | 340 | 340 | SKIP | −66% | L1_1 |
| 9 | `inspect_block_table` | query | 5,474 | 1,498 | 1,498 | SKIP | −73% | L1_1 |
| 10 | `inspect_block_table` | query | 4,458 | 1,238 | 1,238 | SKIP | −72% | L1_1 |
| 11 | `inspect_block_table` | query | 5,300 | 1,466 | 1,466 | SKIP | −72% | L1_1 |
| 12 | `inspect_block_table` | query | 4,902 | 1,397 | 1,397 | SKIP | −72% | L1_1 |
| 13 | `inspect_block_table` | query | 9,928 | 2,614 | 2,614 | SKIP | −74% | L1_1 |
| 14 | `inspect_block_table` | query | 4,302 | 1,213 | 1,213 | SKIP | −72% | L1_1 |
| 15 | `inspect_block` | analysis | 2,889 | 1,379 | 1,379 | SKIP | −52% | — |
| 16 | `fit_block` | analysis | 327 | 269 | 269 | SKIP | −18% | — |
| 17 | `fit_block` | analysis | 3,302 | 899 | 899 | SKIP | −73% | — |

## Subagent Summary (3 events)

| Tool | Verdict | Input Chars | Output Chars | Time | Section |
|------|---------|-------------|-------------|------|---------|
| resolve_compound_ids | KEEP | 288 | 193 | 4.0s | L1_1 |
| search_blocks | KEEP | 9,915 | 1,273 | 13.9s | L1_1 |
| search_blocks | DISCARD | 39 | 1,162 | 9.4s | L1_1 |

## Errors (7)

- **Step 1** `query_thermoml` (exception): {
  "error": "id_catalog[0] must contain exactly ['global_id', 'name', 'registry_id', 'type']; received ['id', 'type']",
  "error_code": "TOOL_EXECUTION_ERROR",
  "tool": "query_thermoml"
}
- **Step 2** `query_thermoml` (exception): {
  "error": "id_catalog[0].type is invalid: 'property'; valid types: ['blocktype', 'comp', 'constr', 'lit', 'meas', 'phase', 'prop', 'rxntype', 'solvent', 'var']",
  "error_code": "TOOL_EXECUTION_ERR
- **Step 5 · L1_1** `inspect_block_table` (exception): {
  "error": "TOOL_ARGUMENT_REFINEMENT_REQUIRED: inspect_block_table.nearest received 'Temperature = 298.15 K' (str); expected dict | None; tool arguments are never coerced",
  "error_code": "TOOL_ARG
- **Step 5 · L1_1** `inspect_block_table` (exception): {
  "error": "TOOL_ARGUMENT_REFINEMENT_REQUIRED: inspect_block_table.nearest received 'Temperature = 298.15 K' (str); expected dict | None; tool arguments are never coerced",
  "error_code": "TOOL_ARG
- **Step 5 · L1_1** `inspect_block_table` (exception): {
  "error": "TOOL_ARGUMENT_REFINEMENT_REQUIRED: inspect_block_table.nearest received 'Temperature = 298.15 K' (str); expected dict | None; tool arguments are never coerced",
  "error_code": "TOOL_ARG
- **Step 5 · L1_1** `inspect_block_table` (exception): {
  "error": "TOOL_ARGUMENT_REFINEMENT_REQUIRED: inspect_block_table.nearest received 'Temperature = 298.15 K' (str); expected dict | None; tool arguments are never coerced",
  "error_code": "TOOL_ARG
- **Step 5 · L1_1** `inspect_block_table` (exception): {
  "error": "TOOL_ARGUMENT_REFINEMENT_REQUIRED: inspect_block_table.nearest received 'Temperature = 298.15 K' (str); expected dict | None; tool arguments are never coerced",
  "error_code": "TOOL_ARG

---

**Total:** 30 tool calls  |  Tool time: 342.9s  |  Wall: 500.2s  |  **Status:** OK
