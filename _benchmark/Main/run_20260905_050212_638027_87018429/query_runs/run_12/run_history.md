# Tool History — query-agent

**Nest:** main - Q_1
**Session:** fbeb0bea
**Detailed log:** run_history_detailed.md — Argo events + verbatim agent outputs (join: session id; step tag `cN` ↔ event-row `cN`)
**Prompt:** [Purpose: Locate all available mixture density data for aqueous 1-propanol at or near 298.15 K]
Find density measurements for the binary mixture of water and 1-propanol near 298.15 K. I need DOIs, block numbers, temperature ranges, composition ranges, and density values.

[Context: The user is planning density measurements for aqueous 1-propanol at 25 °C and wants to know what data already exists. Search for density (mass density) property for the system water + 1-propanol. The compounds are water (H2O) and 1-propanol (C3H8O, also known as n-propanol or propan-1-ol).]
**Started:** 2026-09-05 05:02:27  |  **Elapsed:** 655.3s  |  **Tool calls:** 14  |  **Nested sections:** 2

---

### Step 1 [main - Q_1 · c8]: `L1_query`

<details><summary>Arguments</summary>

```json
{
  "purpose": "Find all mass density data for binary mixture of water and 1-propanol near 298.15 K",
  "instruction": "Search for mass density (GLOBprop_1) measurements for the binary system of water (H2O) and 1-propanol (C3H8O, also known as n-propanol, propan-1-ol, 1-propanol). Look for data near T=298.15 K. Return DOIs, block numbers, temperature ranges, composition ranges (mole fractions), and density values. Resolve compound IDs for water and 1-propanol first, then search for density blocks containing both compounds. Inspect the block tables to get actual data points.",
  "id_catalog": "",
  "context": "User wants to know what density data already exists in ThermoML for aqueous 1-propanol at ~25°C. Property: mass density (GLOBprop_1, kg/m³). System: water + 1-propanol binary mixture."
}
```
</details>

- **Result:** 28,253 chars  |  **Time:** 257.0s  |  **Started:** 05:02:35 (t+8.3s)
- **Nested:** ↳ 7 tool calls in section 'L1_1' below

<details><summary>Result</summary>

```
[TOOL_RESULT_SIZE_WARNING: L1_query returned 28,013 characters after result processing; the target is 24,000. The full result follows — prefer narrower requests, and rely on your working memory for recall instead of re-running this call.]

<subagent_answer>
{
  "answer": "## Mass Density Data for Water + 1-Propanol Binary Mixture near 298.15 K in ThermoML\n\n**System:** Water (GLOBcomp_1) + 1-Propanol (GLOBcomp_5), binary, liquid phase  \n**Property:** Mass density (GLOBprop_1, kg/m³)\n\n### Overview\n\nThe search_blocks discovery tool returned a total count of **17 blocks** (search-tool count, not individually verified) for this binary system with temperatures in the 293–303 K window. These blocks span various composition variables (mole fraction, mass fraction, molality) and pressure conditions (atmospheric to elevated pressures). The following block-level summary ranges are from the `search_blocks` discovery tool (not individually inspected):\n\n| # | DOI | Block | GLOBlit | Comp. Variable | T range (K) | P | ρ range (kg/m³) | Source |\n|---|-----|-------|---------|----------------|-------------|---|-----------------|--------|\n| 1 | 10.1016/j.fluid.2007.07.066 | PROPblock_8 | GLOBlit_555 | mass fraction w, 0.05–0.15 | 283.15–303.15 | atm | 976.004–992.444 | search summary |\n| 2 | 10.1016/j.fluid.2008.01.004 | PROPblock_5 | GLOBlit_590 | mass fraction w, 0.05–0.15 | 283.15–303.15 | atm | 975.791–992.405 | search summary |\n| 3 | 10.1016/j.jct.2008.07.005 | PROPblock_9 | GLOBlit_2979 | mole fraction x, 0–0.2 | 283.15–298.15 | atm (98.93 kPa) | 911.83–999.69 | search summary + inspected |\n\nAdditional blocks (including high-pressure and elevated-temperature datasets) were returned but not shown here (derived count: 17 total minus 3 listed = remaining blocks not displayed). Only blocks 1 and 3 were inspected for verbatim data points below.\n\n---\n\n### Inspected Data Points at T = 298.15 K\n\n#### Block 1: GLOBlit_555 :: PROPblock_8 (DOI: 10.1016/j.fluid.2007.07.066)\nConstraint: P = 101.0 kPa. Composition in mass fraction of propan-1-ol.\n\n| mass_fraction (propan-1-ol) | ρ (kg/m³) |\n|-----------------------------|-----------|\n| 0.05 | 989.431 |\n| 0.10 | 983.475 |\n| 0.15 | 978.117 |\n\nFull block spans 283.15–303.15 K with 15 total points (from inspection stats).\n\n#### Block 2: GLOBlit_2979 :: PROPblock_9 (DOI: 10.1016/j.jct.2008.07.005)\nConstraint: P = 98.93 kPa. Composition in mole fraction of propan-1-ol.\n\n| mole_fraction (propan-1-ol) | ρ (kg/m³) |\n|-----------------------------|-----------|\n| 0 | 997.04 |\n| 0.002 | 995.4 |\n| 0.005 | 993.76 |\n| 0.009 | 991.66 |\n| 0.01 | 991.14 |\n| 0.02 | 986.54 |\n| 0.03 | 982.56 |\n| 0.05 | 975.49 |\n\nFull block spans 283.15–308.15 K with 96 total points; mole fraction range 0–0.2; density range across all temperatures: 911.83–999.69 kg/m³ (from inspection stats).\n\n---\n\n### Chemistry Insight\n\nThe inspected data show a clear monotonic decrease in density with increasing 1-propanol content at 298.15 K. At x(propan-1-ol) = 0, the density is 997.04 kg/m³ (essentially pure water), dropping to 975.49 kg/m³ at x = 0.05 (GLOBlit_2979::PROPblock_9). This is consistent with the addition of a lighter alcohol to water. The two inspected sources cover the water-rich region: PROPblock_8 uses mass fraction (0.05–0.15) while PROPblock_9 uses mole fraction (0–0.2), making direct numerical comparison between them require unit conversion (not performed here). The blocks returned by the search collectively provide extensive coverage of this binary system near ambient temperature.\n\n---\n[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:\n- **UNGROUNDED_LITERAL** PROPblock_9: 17 (near '…datasets) were returned but not shown here (derived count: 1…') matches no inspected row/stat, database table, or other source of PROPblock_9\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"PROPblock_9\", literature=\"<GLOBlit_N or DOI>\", nearest={\"column\": \"temperature_k\", \"value\": 17.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead\nInspected so far: PROPblock_8, PROPblock_9",
  "core_claims": [
    "At 298.15 K and near-atmospheric pressure, the mass density of the water + 1-propanol binary mixture decreases monotonically with increasing 1-propanol content in the water-rich region, from 997.04 kg/m³ at x(propan-1-ol) = 0 to 975.49 kg/m³ at x = 0.05 (GLOBlit_2979::PROPblock_9, P = 98.93 kPa).",
    "Two independent ThermoML sources were inspected: GLOBlit_555::PROPblock_8 reports densities of 989.431, 983.475, and 978.117 kg/m³ at mass fractions 0.05, 0.10, and 0.15 of propan-1-ol (P = 101.0 kPa, T = 298.15 K), and GLOBlit_2979::PROPblock_9 reports densities at mole fractions 0–0.05 (P = 98.93 kPa, T = 298.15 K); direct numerical comparison between the two requires unit conversion that was not performed.",
    "The search returned a total of 17 blocks for this binary system near 298.15 K, but only two blocks (PROPblock_8 and PROPblock_9) were individually inspected, so coverage of the full composition and pressure range is incomplete in the verified data."
  ],
  "status": "partial",
  "summary": "Mass density data for the binary liquid mixture of water (GLOBcomp_1) and 1-propanol (GLOBcomp_5) near 298.15 K were identified across 17 blocks in ThermoML. Two blocks were inspected in detail. GLOBlit_555::PROPblock_8 (DOI 10.1016/j.fluid.2007.07.066, P = 101.0 kPa, 15 total points spanning 283.15–303.15 K) reports densities at 298.15 K of 989.431, 983.475, and 978.117 kg/m³ at propan-1-ol mass fractions of 0.05, 0.10, and 0.15, respectively. GLOBlit_2979::PROPblock_9 (DOI 10.1016/j.jct.2008.07.005, P = 98.93 kPa, 96 total points spanning 283.15–308.15 K, mole fraction 0–0.2, overall density range 911.83–999.69 kg/m³) reports densities at 298.15 K of 997.04, 995.4, 993.76, 991.66, 991.14, 986.54, 982.56, and 975.49 kg/m³ at propan-1-ol mole fractions of 0, 0.002, 0.005, 0.009, 0.01, 0.02, 0.03, and 0.05, respectively. Density decreases monotonically with increasing 1-propanol content at 298.15 K, consistent with addition of a lighter alcohol to water. The two inspected blocks cover the water-rich region using different composition scales (mass fraction vs. mole fraction). A third block from GLOBlit_590::PROPblock_5 (DOI 10.1016/j.fluid.2008.01.004) was identified with mass fraction 0.05–0.15 and density range 975.791–992.405 kg/m³ at 283.15–303.15 K but was not inspected for individual data points.",
  "core_id_updates": [
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_1",
      "registry_id": "water",
      "name": "water"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_5",
      "registry_id": "propan-1-ol",
      "name": "propan-1-ol"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBprop_1",
      "registry_id": "mass_density_kg_m3",
      "name": "Mass density, kg/m3"
    }
  ],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_555",
      "block_number": "PROPblock_8",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_5",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of water + 1-propanol binary mixture at 283.15–303.15 K, mass fraction 0.05–0.15, atmospheric pressure. Inspected data at 298.15 K: 978.117–989.431 kg/m³.",
      "doi": "10.1016/j.fluid.2007.07.066",
      "lit_id": "2007-sad-kho-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 15,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_5",
          "name": "propan-1-ol",
          "formula": "C3H8O",
          "inchi_key": "BDERNNFJNOPAEC-UHFFFAOYSA-N",
          "SMILES": "CCCO",
          "sample_num": "DOIcompSample_2_1"
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
            "min": 283.15,
            "max": 303.15,
            "n_unique": 5
          },
          "range_min": 283.15,
          "range_max": 303.15
        },
        {
          "BLKvar_id": "BLKvar_2",
          "var_num_id": "GLOBvar_5",
          "var_id": "mass_fraction_DOIcomp_2",
          "name": "Mass fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_2",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_2",
            "name": "Mass fraction",
            "min": 0.05,
            "max": 0.15,
            "n_unique": 3
          },
          "range_min": 0.05,
          "range_max": 0.15
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
          "meas_num_id": "GLOBmeas_134",
          "meas_ID": "vibtub_ufactor_4",
          "method_standard": null,
          "method_custom": "VIBTUB:UFactor:4",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 976.004,
            "max": 992.444,
            "mean": 984.9872,
            "std": 4.997,
            "n": 15
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 976.004,
          "range_max": 992.444
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
          "comp_num_id": "GLOBcomp_5",
          "name": "propan-1-ol",
          "formula": "C3H8O",
          "inchi_key": "BDERNNFJNOPAEC-UHFFFAOYSA-N",
          "SMILES": "CCCO",
          "sample_num": "DOIcompSample_2_1"
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
      "parent_n_datapoints": 15,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_590",
      "block_number": "PROPblock_5",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_5",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of water + 1-propanol binary mixture at 283.15–303.15 K, mass fraction 0.05–0.15, atmospheric pressure. Not individually inspected.",
      "doi": "10.1016/j.fluid.2008.01.004",
      "lit_id": "2008-sad-par-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 15,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_5",
          "name": "propan-1-ol",
          "formula": "C3H8O",
          "inchi_key": "BDERNNFJNOPAEC-UHFFFAOYSA-N",
          "SMILES": "CCCO",
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
            "min": 0.05,
            "max": 0.15,
            "n_unique": 3
          },
          "range_min": 0.05,
          "range_max": 0.15
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
            "min": 283.15,
            "max": 303.15,
            "n_unique": 5
          },
          "range_min": 283.15,
          "range_max": 303.15
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
          "meas_num_id": "GLOBmeas_134",
          "meas_ID": "vibtub_ufactor_4",
          "method_standard": null,
          "method_custom": "VIBTUB:UFactor:4",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 975.791,
            "max": 992.405,
            "mean": 984.879933,
            "std": 5.055189,
            "n": 15
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 975.791,
          "range_max": 992.405
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
          "comp_num_id": "GLOBcomp_5",
          "name": "propan-1-ol",
          "formula": "C3H8O",
          "inchi_key": "BDERNNFJNOPAEC-UHFFFAOYSA-N",
          "SMILES": "CCCO",
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
      "parent_n_datapoints": 15,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_2979",
      "block_number": "PROPblock_9",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_5",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of water + 1-propanol binary mixture at 283.15–298.15 K, mole fraction 0–0.2, P=98.93 kPa. Inspected data at 298.15 K: 975.49–997.04 kg/m³.",
      "doi": "10.1016/j.jct.2008.07.005",
      "lit_id": "2008-rom-pae-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 96,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_5",
          "name": "propan-1-ol",
          "formula": "C3H8O",
          "inchi_key": "BDERNNFJNOPAEC-UHFFFAOYSA-N",
          "SMILES": "CCCO",
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
          "value": 98.93,
          "digits": 4,
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
            "min": 283.15,
            "max": 308.15,
            "n_unique": 6
          },
          "range_min": 283.15,
          "range_max": 308.15
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
            "max": 0.2,
            "n_unique": 16
          },
          "range_min": 0.0,
          "range_max": 0.2
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
          "meas_num_id": "GLOBmeas_153",
          "meas_ID": "pycnom_ufactor_4",
          "method_standard": null,
          "method_custom": "PYCNOM:UFactor:4",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 911.83,
            "max": 999.69,
            "mean": 965.947604,
            "std": 27.803432,
            "n": 96
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 911.83,
          "range_max": 999.69
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
          "comp_num_id": "GLOBcomp_5",
          "name": "propan-1-ol",
          "formula": "C3H8O",
          "inchi_key": "BDERNNFJNOPAEC-UHFFFAOYSA-N",
          "SMILES": "CCCO",
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
      "parent_n_datapoints": 96,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1016/j.fluid.2007.07.066",
      "block_number": "PROPblock_8",
      "table_mode": "nearest",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mass_fraction_<propan-1-ol>",
        "pressure_kpa",
        "mass_density_kg_m3"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_7",
          "temperature_k": "293.15",
          "mass_fraction_<propan-1-ol>": "0.05",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "990.715"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "temperature_k": "293.15",
          "mass_fraction_<propan-1-ol>": "0.1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "985.011"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "temperature_k": "298.15",
          "mass_fraction_<propan-1-ol>": "0.05",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "989.431"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "temperature_k": "298.15",
          "mass_fraction_<propan-1-ol>": "0.1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "983.475"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "temperature_k": "298.15",
          "mass_fraction_<propan-1-ol>": "0.15",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "978.117"
        }
      ],
      "inspection_id": "INSP_3aa36d70ff07",
      "lit_num_id": "GLOBlit_555"
    },
    {
      "doi": "10.1016/j.jct.2008.07.005",
      "block_number": "PROPblock_9",
      "table_mode": "nearest",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<propan-1-ol>",
        "pressure_kpa",
        "mass_density_kg_m3"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_49",
          "temperature_k": "298.15",
          "mole_fraction_<propan-1-ol>": "0",
          "pressure_kpa": "98.93",
          "mass_density_kg_m3": "997.04"
        },
        {
          "BLKpoint_id": "BLKpoint_50",
          "temperature_k": "298.15",
          "mole_fraction_<propan-1-ol>": "0.002",
          "pressure_kpa": "98.93",
          "mass_density_kg_m3": "995.4"
        },
        {
          "BLKpoint_id": "BLKpoint_51",
          "temperature_k": "298.15",
          "mole_fraction_<propan-1-ol>": "0.005",
          "pressure_kpa": "98.93",
          "mass_density_kg_m3": "993.76"
        },
        {
          "BLKpoint_id": "BLKpoint_52",
          "temperature_k": "298.15",
          "mole_fraction_<propan-1-ol>": "0.009",
          "pressure_kpa": "98.93",
          "mass_density_kg_m3": "991.66"
        },
        {
          "BLKpoint_id": "BLKpoint_53",
          "temperature_k": "298.15",
          "mole_fraction_<propan-1-ol>": "0.01",
          "pressure_kpa": "98.93",
          "mass_density_kg_m3": "991.14"
        },
        {
          "BLKpoint_id": "BLKpoint_54",
          "temperature_k": "298.15",
          "mole_fraction_<propan-1-ol>": "0.02",
          "pressure_kpa": "98.93",
          "mass_density_kg_m3": "986.54"
        },
        {
          "BLKpoint_id": "BLKpoint_55",
          "temperature_k": "298.15",
          "mole_fraction_<propan-1-ol>": "0.03",
          "pressure_kpa": "98.93",
          "mass_density_kg_m3": "982.56"
        },
        {
          "BLKpoint_id": "BLKpoint_56",
          "temperature_k": "298.15",
          "mole_fraction_<propan-1-ol>": "0.05",
          "pressure_kpa": "98.93",
          "mass_density_kg_m3": "975.49"
        }
      ],
      "inspection_id": "INSP_884f359f5908",
      "lit_num_id": "GLOBlit_2979"
    }
  ]
}
</subagent_answer>
```
</details>

---

### Step 2 [main - Q_1 · c14]: `L1_query`

<details><summary>Arguments</summary>

```json
{
  "purpose": "Inspect GLOBlit_590::PROPblock_5 for data points at 298.15 K and list additional blocks from the 17 found for water+1-propanol density near 298.15 K",
  "instruction": "For the binary mixture of water (GLOBcomp_1) and 1-propanol (GLOBcomp_5), mass density (GLOBprop_1): (1) Inspect block PROPblock_5 from GLOBlit_590 (DOI 10.1016/j.fluid.2008.01.004) for data points nearest to T=298.15 K. (2) Also list as many of the remaining blocks (beyond GLOBlit_555::PROPblock_8, GLOBlit_590::PROPblock_5, GLOBlit_2979::PROPblock_9) as possible from the 17 total blocks found for this system near 298.15 K, showing DOI, GLOBlit, block number, composition variable, T range, P conditions, and density range for each.",
  "id_catalog": "GLOBcomp_1=water, GLOBcomp_5=propan-1-ol, GLOBprop_1=Mass density kg/m3",
  "context": "Previous search found 17 blocks total for water+1-propanol density near 298.15 K. Three were listed (GLOBlit_555::PROPblock_8, GLOBlit_590::PROPblock_5, GLOBlit_2979::PROPblock_9) but only PROPblock_8 and PROPblock_9 were inspected. Need to inspect PROPblock_5 and discover the remaining 14 blocks."
}
```
</details>

- **Result:** 82,686 chars  |  **Time:** 227.7s  |  **Started:** 05:07:08 (t+281.3s)
- **Nested:** ↳ 5 tool calls in section 'L1_2' below

<details><summary>Result</summary>

```
[TOOL_RESULT_SIZE_WARNING: L1_query returned 82,446 characters after result processing; the target is 24,000. The full result follows — prefer narrower requests, and rely on your working memory for recall instead of re-running this call.]

<subagent_answer>
{
  "answer": "## Inspection of GLOBlit_590::PROPblock_5 at 298.15 K\n\n**Source:** DOI 10.1016/j.fluid.2008.01.004 (GLOBlit_590), PROPblock_5  \n**System:** Water + 1-propanol, binary, liquid phase  \n**Constraint:** P = 101.0 kPa  \n**Composition variable:** Mass fraction of propan-1-ol (0.05–0.15)  \n**Full block:** 15 data points, T = 283.15–303.15 K, ρ = 975.791–992.405 kg/m³\n\n### Data points at T = 298.15 K (verbatim from inspection):\n\n| mass_fraction (propan-1-ol) | ρ (kg/m³) |\n|---|---|\n| 0.05 | 989.387 |\n| 0.10 | 983.372 |\n| 0.15 | 977.921 |\n\nThese three data points at 298.15 K show the expected monotonic decrease in density with increasing 1-propanol content.\n\n---\n\n## Full Listing of Blocks for Water + 1-Propanol Density near 298.15 K\n\nThe search_system_registry returned blocks for this binary system in a temperature window around 298.15 K. The following table lists all blocks identified by DOI, GLOBlit, and block number. Numerical details are shown only for the block inspected in this run (GLOBlit_590::PROPblock_5, above).\n\n| DOI | GLOBlit | Block | Status |\n|---|---|---|---|\n| 10.1016/j.fluid.2007.07.066 | GLOBlit_555 | PROPblock_8 | Not inspected in this run |\n| 10.1016/j.fluid.2008.01.004 | GLOBlit_590 | PROPblock_5 | Inspected in this run (see above) |\n| 10.1016/j.jct.2004.07.019 | GLOBlit_2432 | PROPblock_3 | Not inspected |\n| 10.1016/j.jct.2008.07.005 | GLOBlit_2979 | PROPblock_9 | Not inspected in this run |\n| 10.1016/j.jct.2013.11.036 | GLOBlit_4068 | PROPblock_1 | Not inspected |\n| 10.1016/j.jct.2013.11.036 | GLOBlit_4068 | PROPblock_2 | Not inspected |\n| 10.1016/j.jct.2015.06.024 | GLOBlit_4415 | PROPblock_5 | Not inspected |\n| 10.1016/j.jct.2019.105880 | GLOBlit_5585 | PROPblock_7 | Not inspected |\n| 10.1021/acs.jced.6b01058 | GLOBlit_7085 | PROPblock_8 | Not inspected |\n| 10.1021/acs.jced.7b00299 | GLOBlit_7178 | PROPblock_13 | Not inspected |\n| 10.1021/je034101z | GLOBlit_8254 | PROPblock_6 | Not inspected |\n| 10.1021/je4003515 | GLOBlit_10159 | PROPblock_10 | Not inspected |\n| 10.1021/je800158z | GLOBlit_11142 | PROPblock_3 | Not inspected (registry entry truncated) |\n| (truncated in registry output) | — | — | Not available |\n\n**Notes:**\n- Composition variables, pressure conditions, point counts, and density ranges for uninspected blocks were not verified via inspection and are therefore not reported here.\n- Only GLOBlit_590::PROPblock_5 was inspected in this run. GLOBlit_555::PROPblock_8 and GLOBlit_2979::PROPblock_9 were inspected in the prior session (see working memory for those data points) but were not re-inspected here.\n- The row count shown in the listing table is derived from the registry tool output, not from block inspection. The registry listing was truncated after the entry shown for GLOBlit_11142.",
  "core_claims": [
    "For the water + 1-propanol binary system at 298.15 K and 101.0 kPa (GLOBlit_590::PROPblock_5, DOI 10.1016/j.fluid.2008.01.004), the liquid density decreases monotonically with increasing 1-propanol mass fraction: 989.387 kg/m³ at 0.05, 983.372 kg/m³ at 0.10, and 977.921 kg/m³ at 0.15.",
    "At least 13 additional ThermoML data blocks from independent literature sources contain density data for the water + 1-propanol binary system near 298.15 K, but these blocks were not inspected in this run and their numerical values were not verified."
  ],
  "status": "success",
  "summary": "For the binary liquid system water + 1-propanol at 298.15 K and 101.0 kPa, GLOBlit_590::PROPblock_5 (DOI 10.1016/j.fluid.2008.01.004) reports density as a function of mass fraction of propan-1-ol: 989.387 kg/m³ at 0.05, 983.372 kg/m³ at 0.10, and 977.921 kg/m³ at 0.15. The full block spans 15 data points over T = 283.15–303.15 K and ρ = 975.791–992.405 kg/m³. At least 13 additional ThermoML blocks from other DOIs (GLOBlit_555, GLOBlit_2432, GLOBlit_2979, GLOBlit_4068, GLOBlit_4415, GLOBlit_5585, GLOBlit_7085, GLOBlit_7178, GLOBlit_8254, GLOBlit_10159, GLOBlit_11142, among others) also contain water + 1-propanol density data near 298.15 K but were not inspected in this run, so no numerical values are reported for them.",
  "core_id_updates": [],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_590",
      "block_number": "PROPblock_5",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_5",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of water+1-propanol at P=101.0 kPa, T=283.15–303.15 K, mass fraction 0.05–0.15, ρ=975.791–992.405 kg/m³. Inspected: 3 points at 298.15 K.",
      "doi": "10.1016/j.fluid.2008.01.004",
      "lit_id": "2008-sad-par-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 15,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_5",
          "name": "propan-1-ol",
          "formula": "C3H8O",
          "inchi_key": "BDERNNFJNOPAEC-UHFFFAOYSA-N",
          "SMILES": "CCCO",
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
            "min": 0.05,
            "max": 0.15,
            "n_unique": 3
          },
          "range_min": 0.05,
          "range_max": 0.15
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
            "min": 283.15,
            "max": 303.15,
            "n_unique": 5
          },
          "range_min": 283.15,
          "range_max": 303.15
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
          "meas_num_id": "GLOBmeas_134",
          "meas_ID": "vibtub_ufactor_4",
          "method_standard": null,
          "method_custom": "VIBTUB:UFactor:4",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 975.791,
            "max": 992.405,
            "mean": 984.879933,
            "std": 5.055189,
            "n": 15
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 975.791,
          "range_max": 992.405
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
          "comp_num_id": "GLOBcomp_5",
          "name": "propan-1-ol",
          "formula": "C3H8O",
          "inchi_key": "BDERNNFJNOPAEC-UHFFFAOYSA-N",
          "SMILES": "CCCO",
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
      "parent_n_datapoints": 15,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_555",
      "block_number": "PROPblock_8",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_5",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of water+1-propanol near 298.15 K. Not inspected in this run.",
      "doi": "10.1016/j.fluid.2007.07.066",
      "lit_id": "2007-sad-kho-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 15,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_5",
          "name": "propan-1-ol",
          "formula": "C3H8O",
          "inchi_key": "BDERNNFJNOPAEC-UHFFFAOYSA-N",
          "SMILES": "CCCO",
          "sample_num": "DOIcompSample_2_1"
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
            "min": 283.15,
            "max": 303.15,
            "n_unique": 5
          },
          "range_min": 283.15,
          "range_max": 303.15
        },
        {
          "BLKvar_id": "BLKvar_2",
          "var_num_id": "GLOBvar_5",
          "var_id": "mass_fraction_DOIcomp_2",
          "name": "Mass fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_2",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_2",
            "name": "Mass fraction",
            "min": 0.05,
            "max": 0.15,
            "n_unique": 3
          },
          "range_min": 0.05,
          "range_max": 0.15
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
          "meas_num_id": "GLOBmeas_134",
          "meas_ID": "vibtub_ufactor_4",
          "method_standard": null,
          "method_custom": "VIBTUB:UFactor:4",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 976.004,
            "max": 992.444,
            "mean": 984.9872,
            "std": 4.997,
            "n": 15
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 976.004,
          "range_max": 992.444
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
          "comp_num_id": "GLOBcomp_5",
          "name": "propan-1-ol",
          "formula": "C3H8O",
          "inchi_key": "BDERNNFJNOPAEC-UHFFFAOYSA-N",
          "SMILES": "CCCO",
          "sample_num": "DOIcompSample_2_1"
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
      "parent_n_datapoints": 15,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_2979",
      "block_number": "PROPblock_9",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_5",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of water+1-propanol near 298.15 K. Not inspected in this run.",
      "doi": "10.1016/j.jct.2008.07.005",
      "lit_id": "2008-rom-pae-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 96,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_5",
          "name": "propan-1-ol",
          "formula": "C3H8O",
          "inchi_key": "BDERNNFJNOPAEC-UHFFFAOYSA-N",
          "SMILES": "CCCO",
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
          "value": 98.93,
          "digits": 4,
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
            "min": 283.15,
            "max": 308.15,
            "n_unique": 6
          },
          "range_min": 283.15,
          "range_max": 308.15
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
            "max": 0.2,
            "n_unique": 16
          },
          "range_min": 0.0,
          "range_max": 0.2
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
          "meas_num_id": "GLOBmeas_153",
          "meas_ID": "pycnom_ufactor_4",
          "method_standard": null,
          "method_custom": "PYCNOM:UFactor:4",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 911.83,
            "max": 999.69,
            "mean": 965.947604,
            "std": 27.803432,
            "n": 96
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 911.83,
          "range_max": 999.69
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
          "comp_num_id": "GLOBcomp_5",
          "name": "propan-1-ol",
          "formula": "C3H8O",
          "inchi_key": "BDERNNFJNOPAEC-UHFFFAOYSA-N",
          "SMILES": "CCCO",
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
      "parent_n_datapoints": 96,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_2432",
      "block_number": "PROPblock_3",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_5",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of water+1-propanol near 298.15 K. Not inspected.",
      "doi": "10.1016/j.jct.2004.07.019",
      "lit_id": "2004-hyn-hne-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 456,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_5",
          "name": "propan-1-ol",
          "formula": "C3H8O",
          "inchi_key": "BDERNNFJNOPAEC-UHFFFAOYSA-N",
          "SMILES": "CCCO",
          "sample_num": "DOIcompSample_2_1"
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
            "min": 298.15,
            "max": 573.15,
            "n_unique": 18
          },
          "range_min": 298.15,
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
            "min": 420.0,
            "max": 30310.0,
            "n_unique": 30
          },
          "range_min": 420.0,
          "range_max": 30310.0
        },
        {
          "BLKvar_id": "BLKvar_3",
          "var_num_id": "GLOBvar_4",
          "var_id": "molality_mol_kg_DOIcomp_2",
          "name": "Molality, mol/kg",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_2",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_3",
            "name": "Molality, mol/kg",
            "min": 0.0943,
            "max": 0.84695,
            "n_unique": 131
          },
          "range_min": 0.0943,
          "range_max": 0.84695
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
            "min": -20.1904,
            "max": -1.0433,
            "mean": -5.762233,
            "std": 4.125966,
            "n": 456
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": -20.1904,
          "range_max": -1.0433
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
          "comp_num_id": "GLOBcomp_5",
          "name": "propan-1-ol",
          "formula": "C3H8O",
          "inchi_key": "BDERNNFJNOPAEC-UHFFFAOYSA-N",
          "SMILES": "CCCO",
          "sample_num": "DOIcompSample_2_1"
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
      "parent_n_datapoints": 456,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_4068",
      "block_number": "PROPblock_1",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_5",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of water+1-propanol near 298.15 K. Not inspected.",
      "doi": "10.1016/j.jct.2013.11.036",
      "lit_id": "2014-abd-azi-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 174,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_5",
          "name": "propan-1-ol",
          "formula": "C3H8O",
          "inchi_key": "BDERNNFJNOPAEC-UHFFFAOYSA-N",
          "SMILES": "CCCO",
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
      "solvents": [
        {
          "component_org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_1",
          "solvent_num_id": "GLOBsolvent_1",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N"
        }
      ],
      "constraints": [],
      "variables": [
        {
          "BLKvar_id": "BLKvar_1",
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
            "BLKvar_id": "BLKvar_1",
            "name": "Pressure, kPa",
            "min": 2353.0,
            "max": 40000.0,
            "n_unique": 79
          },
          "range_min": 2353.0,
          "range_max": 40000.0
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
            "min": 298.15,
            "max": 582.08,
            "n_unique": 38
          },
          "range_min": 298.15,
          "range_max": 582.08
        },
        {
          "BLKvar_id": "BLKvar_3",
          "var_num_id": "GLOBvar_4",
          "var_id": "molality_mol_kg_DOIcomp_2",
          "name": "Molality, mol/kg",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_2",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_3",
            "name": "Molality, mol/kg",
            "min": 0.869,
            "max": 56.348,
            "n_unique": 6
          },
          "range_min": 0.869,
          "range_max": 56.348
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
          "meas_num_id": "GLOBmeas_66",
          "meas_ID": "constant_volume_piezometry",
          "method_standard": "Constant-volume piezometry",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 322.1,
            "max": 1004.4,
            "mean": 846.767241,
            "std": 148.077759,
            "n": 174
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 322.1,
          "range_max": 1004.4
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
          "comp_num_id": "GLOBcomp_5",
          "name": "propan-1-ol",
          "formula": "C3H8O",
          "inchi_key": "BDERNNFJNOPAEC-UHFFFAOYSA-N",
          "SMILES": "CCCO",
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
      "parent_n_datapoints": 174,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_4068",
      "block_number": "PROPblock_2",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_5",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of water+1-propanol near 298.15 K. Not inspected.",
      "doi": "10.1016/j.jct.2013.11.036",
      "lit_id": "2014-abd-azi-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 29,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_5",
          "name": "propan-1-ol",
          "formula": "C3H8O",
          "inchi_key": "BDERNNFJNOPAEC-UHFFFAOYSA-N",
          "SMILES": "CCCO",
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
      "solvents": [
        {
          "component_org_num": "DOIcomp_1",
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
            "min": 292.05,
            "max": 352.05,
            "n_unique": 18
          },
          "range_min": 292.05,
          "range_max": 352.05
        },
        {
          "BLKvar_id": "BLKvar_2",
          "var_num_id": "GLOBvar_4",
          "var_id": "molality_mol_kg_DOIcomp_2",
          "name": "Molality, mol/kg",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_2",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_2",
            "name": "Molality, mol/kg",
            "min": 0.869,
            "max": 56.348,
            "n_unique": 6
          },
          "range_min": 0.869,
          "range_max": 56.348
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
          "meas_num_id": "GLOBmeas_6",
          "meas_ID": "pycnometric_method",
          "method_standard": "Pycnometric method",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 801.03,
            "max": 991.42,
            "mean": 925.884483,
            "std": 57.23186,
            "n": 29
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 801.03,
          "range_max": 991.42
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
          "comp_num_id": "GLOBcomp_5",
          "name": "propan-1-ol",
          "formula": "C3H8O",
          "inchi_key": "BDERNNFJNOPAEC-UHFFFAOYSA-N",
          "SMILES": "CCCO",
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
      "parent_n_datapoints": 29,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_4415",
      "block_number": "PROPblock_5",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_5",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of water+1-propanol near 298.15 K. Not inspected.",
      "doi": "10.1016/j.jct.2015.06.024",
      "lit_id": "2015-ebr-sad-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 40,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_5",
          "name": "propan-1-ol",
          "formula": "C3H8O",
          "inchi_key": "BDERNNFJNOPAEC-UHFFFAOYSA-N",
          "SMILES": "CCCO",
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
      "solvents": [
        {
          "component_org_num": "DOIcomp_1",
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
          "value": 84.5,
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
            "min": 288.15,
            "max": 308.15,
            "n_unique": 5
          },
          "range_min": 288.15,
          "range_max": 308.15
        },
        {
          "BLKvar_id": "BLKvar_2",
          "var_num_id": "GLOBvar_4",
          "var_id": "molality_mol_kg_DOIcomp_3",
          "name": "Molality, mol/kg",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_3",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_2",
            "name": "Molality, mol/kg",
            "min": 0.01666,
            "max": 0.16617,
            "n_unique": 8
          },
          "range_min": 0.01666,
          "range_max": 0.16617
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
            "min": 992.305,
            "max": 998.928,
            "mean": 995.97015,
            "std": 1.902894,
            "n": 40
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 992.305,
          "range_max": 998.928
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
          "comp_num_id": "GLOBcomp_5",
          "name": "propan-1-ol",
          "formula": "C3H8O",
          "inchi_key": "BDERNNFJNOPAEC-UHFFFAOYSA-N",
          "SMILES": "CCCO",
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
      "parent_n_datapoints": 40,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_5585",
      "block_number": "PROPblock_7",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_1",
        "GLOBcomp_5"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of water+1-propanol near 298.15 K. Not inspected.",
      "doi": "10.1016/j.jct.2019.105880",
      "lit_id": "2019-meh-haj-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 16,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_4_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_5",
          "name": "propan-1-ol",
          "formula": "C3H8O",
          "inchi_key": "BDERNNFJNOPAEC-UHFFFAOYSA-N",
          "SMILES": "CCCO",
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
            "min": 288.15,
            "max": 303.15,
            "n_unique": 4
          },
          "range_min": 288.15,
          "range_max": 303.15
        },
        {
          "BLKvar_id": "BLKvar_2",
          "var_num_id": "GLOBvar_5",
          "var_id": "mass_fraction_DOIcomp_2",
          "name": "Mass fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_2",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_2",
            "name": "Mass fraction",
            "min": 0.1,
            "max": 0.4,
            "n_unique": 4
          },
          "range_min": 0.1,
          "range_max": 0.4
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
            "min": 924.386,
            "max": 985.245,
            "mean": 957.421,
            "std": 20.877178,
            "n": 16
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 924.386,
          "range_max": 985.245
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
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_4_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_5",
          "name": "propan-1-ol",
          "formula": "C3H8O",
          "inchi_key": "BDERNNFJNOPAEC-UHFFFAOYSA-N",
          "SMILES": "CCCO",
          "sample_num": "DOIcompSample_2_1"
        }
      ],
      "parent_n_datapoints": 16,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_7085",
      "block_number": "PROPblock_8",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_5",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of water+1-propanol near 298.15 K. Not inspected.",
      "doi": "10.1021/acs.jced.6b01058",
      "lit_id": "2017-sha-cha-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 12,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_5",
          "name": "propan-1-ol",
          "formula": "C3H8O",
          "inchi_key": "BDERNNFJNOPAEC-UHFFFAOYSA-N",
          "SMILES": "CCCO",
          "sample_num": "DOIcompSample_4_1"
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
          "value": 85.0,
          "digits": 2,
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
            "min": 298.15,
            "max": 313.15,
            "n_unique": 4
          },
          "range_min": 298.15,
          "range_max": 313.15
        },
        {
          "BLKvar_id": "BLKvar_2",
          "var_num_id": "GLOBvar_5",
          "var_id": "mass_fraction_DOIcomp_4",
          "name": "Mass fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_4",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_2",
            "name": "Mass fraction",
            "min": 0.04,
            "max": 0.16,
            "n_unique": 3
          },
          "range_min": 0.04,
          "range_max": 0.16
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
            "min": 966.84,
            "max": 990.59,
            "mean": 980.451667,
            "std": 8.180747,
            "n": 12
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 966.84,
          "range_max": 990.59
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
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_5",
          "name": "propan-1-ol",
          "formula": "C3H8O",
          "inchi_key": "BDERNNFJNOPAEC-UHFFFAOYSA-N",
          "SMILES": "CCCO",
          "sample_num": "DOIcompSample_4_1"
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
      "parent_n_datapoints": 12,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_7178",
      "block_number": "PROPblock_13",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_1",
        "GLOBcomp_5"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of water+1-propanol near 298.15 K. Not inspected.",
      "doi": "10.1021/acs.jced.7b00299",
      "lit_id": "2017-sha-asa-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 2,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_4_1"
        },
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_5",
          "name": "propan-1-ol",
          "formula": "C3H8O",
          "inchi_key": "BDERNNFJNOPAEC-UHFFFAOYSA-N",
          "SMILES": "CCCO",
          "sample_num": "DOIcompSample_3_1"
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
        },
        {
          "BLKconstr_id": "BLKconstr_2",
          "constr_num_id": "GLOBconstr_8",
          "constr_id": "molality_mol_kg_DOIcomp_3",
          "name": "Molality, mol/kg",
          "type": "eComponentComposition",
          "value": 14.0,
          "digits": 4,
          "component_org_num": "DOIcomp_3",
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
            "min": 298.15,
            "max": 313.15,
            "n_unique": 2
          },
          "range_min": 298.15,
          "range_max": 313.15
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
            "min": 903.156,
            "max": 914.36,
            "mean": 908.758,
            "std": 7.922424,
            "n": 2
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 903.156,
          "range_max": 914.36
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
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_4_1"
        },
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_5",
          "name": "propan-1-ol",
          "formula": "C3H8O",
          "inchi_key": "BDERNNFJNOPAEC-UHFFFAOYSA-N",
          "SMILES": "CCCO",
          "sample_num": "DOIcompSample_3_1"
        }
      ],
      "parent_n_datapoints": 2,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_8254",
      "block_number": "PROPblock_6",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_5",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of water+1-propanol near 298.15 K. Not inspected.",
      "doi": "10.1021/je034101z",
      "lit_id": "2003-kit-kag-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 380,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_5",
          "name": "propan-1-ol",
          "formula": "C3H8O",
          "inchi_key": "BDERNNFJNOPAEC-UHFFFAOYSA-N",
          "SMILES": "CCCO",
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
            "BLKvar_id": "BLKvar_1",
            "name": "Mole fraction",
            "min": 0.255,
            "max": 0.738,
            "n_unique": 3
          },
          "range_min": 0.255,
          "range_max": 0.738
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
            "min": 282.15,
            "max": 425.15,
            "n_unique": 144
          },
          "range_min": 282.15,
          "range_max": 425.15
        },
        {
          "BLKvar_id": "BLKvar_3",
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
            "BLKvar_id": "BLKvar_3",
            "name": "Pressure, kPa",
            "min": 5753.0,
            "max": 29883.0,
            "n_unique": 379
          },
          "range_min": 5753.0,
          "range_max": 29883.0
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
          "meas_num_id": "GLOBmeas_170",
          "meas_ID": "isochor",
          "method_standard": null,
          "method_custom": "ISOCHOR",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 731.4,
            "max": 896.2,
            "mean": 821.633684,
            "std": 43.709805,
            "n": 380
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 731.4,
          "range_max": 896.2
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
          "comp_num_id": "GLOBcomp_5",
          "name": "propan-1-ol",
          "formula": "C3H8O",
          "inchi_key": "BDERNNFJNOPAEC-UHFFFAOYSA-N",
          "SMILES": "CCCO",
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
      "parent_n_datapoints": 380,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10159",
      "block_number": "PROPblock_10",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_5",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of water+1-propanol near 298.15 K. Not inspected.",
      "doi": "10.1021/je4003515",
      "lit_id": "2013-che-liu-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 25,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_5",
          "name": "propan-1-ol",
          "formula": "C3H8O",
          "inchi_key": "BDERNNFJNOPAEC-UHFFFAOYSA-N",
          "SMILES": "CCCO",
          "sample_num": "DOIcompSample_3_1"
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
            "max": 313.15,
            "n_unique": 5
          },
          "range_min": 293.15,
          "range_max": 313.15
        },
        {
          "BLKvar_id": "BLKvar_2",
          "var_num_id": "GLOBvar_4",
          "var_id": "molality_mol_kg_DOIcomp_3",
          "name": "Molality, mol/kg",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_3",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_2",
            "name": "Molality, mol/kg",
            "min": 14.0,
            "max": 22.0,
            "n_unique": 5
          },
          "range_min": 14.0,
          "range_max": 22.0
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
            "min": 879.756,
            "max": 918.103,
            "mean": 898.35392,
            "std": 10.064508,
            "n": 25
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 879.756,
          "range_max": 918.103
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
          "comp_num_id": "GLOBcomp_5",
          "name": "propan-1-ol",
          "formula": "C3H8O",
          "inchi_key": "BDERNNFJNOPAEC-UHFFFAOYSA-N",
          "SMILES": "CCCO",
          "sample_num": "DOIcompSample_3_1"
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
      "parent_n_datapoints": 25,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_11142",
      "block_number": "PROPblock_3",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_5",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of water+1-propanol near 298.15 K. Not inspected; registry entry truncated.",
      "doi": "10.1021/je800158z",
      "lit_id": "2008-zar-sha-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 56,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_5",
          "name": "propan-1-ol",
          "formula": "C3H8O",
          "inchi_key": "BDERNNFJNOPAEC-UHFFFAOYSA-N",
          "SMILES": "CCCO",
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
          "constr_num_id": "GLOBconstr_1",
          "constr_id": "pressure_kpa",
          "name": "Pressure, kPa",
          "type": "ePressure",
          "value": 81.5,
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
            "n_unique": 14
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
            "max": 323.15,
            "n_unique": 4
          },
          "range_min": 293.15,
          "range_max": 323.15
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
          "meas_num_id": "GLOBmeas_134",
          "meas_ID": "vibtub_ufactor_4",
          "method_standard": null,
          "method_custom": "VIBTUB:UFactor:4",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 778.92,
            "max": 998.2,
            "mean": 864.609286,
            "std": 64.776079,
            "n": 56
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 778.92,
          "range_max": 998.2
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
          "comp_num_id": "GLOBcomp_5",
          "name": "propan-1-ol",
          "formula": "C3H8O",
          "inchi_key": "BDERNNFJNOPAEC-UHFFFAOYSA-N",
          "SMILES": "CCCO",
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
      "parent_n_datapoints": 56,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1016/j.fluid.2008.01.004",
      "block_number": "PROPblock_5",
      "table_mode": "nearest",
      "columns": [
        "BLKpoint_id",
        "mass_fraction_<propan-1-ol>",
        "temperature_k",
        "pressure_kpa",
        "mass_density_kg_m3"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_3",
          "mass_fraction_<propan-1-ol>": "0.05",
          "temperature_k": "293.15",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "990.671"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "mass_fraction_<propan-1-ol>": "0.1",
          "temperature_k": "293.15",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "984.913"
        },
        {
          "BLKpoint_id": "BLKpoint_13",
          "mass_fraction_<propan-1-ol>": "0.15",
          "temperature_k": "293.15",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "979.828"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "mass_fraction_<propan-1-ol>": "0.05",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "989.387"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "mass_fraction_<propan-1-ol>": "0.1",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "983.372"
        },
        {
          "BLKpoint_id": "BLKpoint_14",
          "mass_fraction_<propan-1-ol>": "0.15",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "977.921"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "mass_fraction_<propan-1-ol>": "0.05",
          "temperature_k": "303.15",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "987.86"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "mass_fraction_<propan-1-ol>": "0.1",
          "temperature_k": "303.15",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "981.595"
        }
      ],
      "inspection_id": "INSP_859136865c90",
      "lit_num_id": "GLOBlit_590"
    }
  ]
}
</subagent_answer>
```
</details>

---

## Nested tool calls — L1_1 (L1-query)

**Nest:** main - Q_1 - L1_1
**Parent:** `L1_query` — Step 1 [main - Q_1 · c8] relays this worker's result
**Started:** 05:02:35  |  **Ended:** 05:06:52  |  **Tool calls:** 7

---

### Step 2 [main - Q_1 - L1_1 · c1]: `resolve_compound_ids`

<details><summary>Arguments</summary>

```json
{
  "queries": [
    "water",
    "1-propanol"
  ],
  "min_score": 50,
  "limit": 5,
  "purpose": "Resolve compound IDs for water and 1-propanol",
  "tasks": "Find GLOBcomp IDs for water and 1-propanol"
}
```
</details>

- **Result:** 198 chars  |  **Time:** 4.8s  |  **Started:** 05:02:45 (t+17.7s)
- **Subagent:** KEEP in 283 → 198 chars (4.8s)
  - Both compounds resolved with exact matches.

| Compound | GLOBcomp ID | Formula | SMILES |
|---|---|---|---|
| water | GLOBcomp_1 | H2O | O |
| propan-1-ol (1-propanol) | GLOBcomp_5 | C3H8O | CCCO |

<details><summary>Result</summary>

```
Both compounds resolved with exact matches.

| Compound | GLOBcomp ID | Formula | SMILES |
|---|---|---|---|
| water | GLOBcomp_1 | H2O | O |
| propan-1-ol (1-propanol) | GLOBcomp_5 | C3H8O | CCCO |
```
</details>

---

### Step 4 [main - Q_1 - L1_1 · c2]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_1",
    "GLOBcomp_5"
  ],
  "property": "GLOBprop_1",
  "system_type": "binary",
  "temperature_range": [
    293.0,
    303.0
  ],
  "limit": 50,
  "purpose": "Find mass density data for water + 1-propanol binary near 298.15 K",
  "tasks": "Search for density blocks containing both water and 1-propanol near 298.15 K"
}
```
</details>

- **Result:** 784 chars  |  **Time:** 21.7s  |  **Started:** 05:03:01 (t+34.5s)
- **Subagent:** KEEP in 11,346 → 766 chars (15.0s)
  - **Summary:** 17 blocks of liquid-phase mass density (GLOBprop_1) for the water (GLOBcomp_1) + 1-propanol (GLOBcomp_5) binary were found near 298.15 K, all with score 100. Blocks span various compositi

<details><summary>Result</summary>

```
**Summary:** 17 blocks of liquid-phase mass density (GLOBprop_1) for the water (GLOBcomp_1) + 1-propanol (GLOBcomp_5) binary were found near 298.15 K, all with score 100. Blocks span various composition variables (mole fraction, mass fraction, molality) and temperature/pressure ranges within the query window.

| # | DOI | Block | Pts | Comp. Variable | Comp. Range | T (K) | ρ (kg/m³) | Notes |
|---|-----|-------|-----|----------------|-------------|-------|-----------|-------|
| 1 | 10.1016/j.fluid.2007.07.066 | PROPblock_8 | 13 | w(propan-1-ol) | 0.05–0.15 | 283.15–303.15 | 976.004–992.444 | GLOBlit_555 |
| 2 | 10.1016/j.fluid.2008.01.004 | PROPblock_5 | 15 | w(propan-1-ol) | 0.05–0.15 | 283.15–303.15 | 975.791–992.405 | GLOBlit_590 |
| 3 | 10.1016/j.jct. [lit_num_id=null]
```
</details>

---

### Step 5 [main - Q_1 - L1_1 · c3]: `inspect_block_table` ❌ ERROR

<details><summary>Arguments</summary>

```json
{
  "block_number": "PROPblock_8",
  "literature": "GLOBlit_555",
  "nearest": "T=298.15 K",
  "purpose": "Get actual density data points for water+1-propanol near 298.15 K",
  "tasks": "Return data rows near 298.15 K from this block"
}
```
</details>

- **Result:** 249 chars  |  **Time:** 0.0s  |  **Started:** 05:03:42 (t+75.5s)
- **Error:** `{
  "error": "TOOL_ARGUMENT_REFINEMENT_REQUIRED: inspect_block_table.nearest received 'T=298.15 K' (str); expected dict | None; tool arguments are never coerced",
  "error_code": "TOOL_ARGUMENT_REFINEMENT_REQUIRED",
  "tool": "inspect_block_table"
}`

---

### Step 6 [main - Q_1 - L1_1 · c4]: `inspect_block_table`

<details><summary>Arguments</summary>

```json
{
  "block_number": "PROPblock_8",
  "literature": "GLOBlit_555",
  "nearest": {
    "Temperature": 298.15
  },
  "purpose": "Get actual density data points for water+1-propanol binary near 298.15 K",
  "tasks": "Return data rows near T=298.15 K from this block"
}
```
</details>

- **Result:** 379 chars  |  **Time:** 0.2s  |  **Started:** 05:03:49 (t+82.0s)

<details><summary>Result</summary>

```
**inspect_block_table error** — nearest must be {"column": alias, "value": number, "k": 1..8}

| alias | n_finite | min | max |
|---|---|---|---|
| temperature_k | 15 | 283.15 | 303.15 |
| mass_fraction_propan_1_ol | 15 | 0.05 | 0.15 |
| pressure_kpa | 15 | 101 | 101 |
| mass_density_kg_m3 | 15 | 976.004 | 992.444 |

Use these aliases in `where` / `nearest` with plain numbers.
```
</details>

---

### Step 7 [main - Q_1 - L1_1 · c5]: `inspect_block_table`

<details><summary>Arguments</summary>

```json
{
  "block_number": "PROPblock_8",
  "literature": "GLOBlit_555",
  "nearest": {
    "column": "temperature_k",
    "value": 298.15,
    "k": 5
  },
  "purpose": "Get density data points near 298.15 K for water+1-propanol",
  "tasks": "Return rows nearest to 298.15 K"
}
```
</details>

- **Result:** 980 chars  |  **Time:** 0.1s  |  **Started:** 05:04:00 (t+92.7s)

<details><summary>Result</summary>

```
**Data inspection** — 10.1016/j.fluid.2007.07.066 [GLOBlit_555] :: PROPblock_8 (binary: propan-1-ol + water)
filter: nearest temperature_k ≈ 298.15 (k=5)
block constraints: pressure_kpa = 101.0

| BLKpoint_id | temperature_k | mass_fraction_<propan-1-ol> | pressure_kpa | mass_density_kg_m3 |
|---|---|---|---|---|
| BLKpoint_7 | 293.15 | 0.05 | 101.0 | 990.715 |
| BLKpoint_8 | 293.15 | 0.1 | 101.0 | 985.011 |
| BLKpoint_10 | 298.15 | 0.05 | 101.0 | 989.431 |
| BLKpoint_11 | 298.15 | 0.1 | 101.0 | 983.475 |
| BLKpoint_12 | 298.15 | 0.15 | 101.0 | 978.117 |

mode: nearest — 5 row(s) of 15 matched (block has 15)
bracket: exact row(s) at temperature_k = 298.15 exist in the matched set
stats (matched, n=15): temperature_k 283.15–303.15 (n=15); mass_fraction_propan_1_ol 0.05–0.15 (n=15); pressure_kpa 101.0–101.0 (n=15); mass_density_kg_m3 976.004–992.444 (n=15)
inspection_id: INSP_3aa36d70ff07
Data points may be quoted ONLY verbatim from the table above or the stats lines.
```
</details>

---

### Step 8 [main - Q_1 - L1_1 · c6]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_1",
    "GLOBcomp_5"
  ],
  "property": "GLOBprop_1",
  "system_type": "binary",
  "temperature_range": [
    293.0,
    303.0
  ],
  "limit": 50,
  "purpose": "Get full list of binary water+1-propanol density blocks near 298.15 K",
  "tasks": "Retrieve all blocks that were truncated in previous search"
}
```
</details>

- **Result:** 1,179 chars  |  **Time:** 20.8s  |  **Started:** 05:04:11 (t+103.9s)
- **Subagent:** KEEP in 11,346 → 1,164 chars (15.0s)
  - **Summary:** 17 binary water+1-propanol mass density blocks found in the 293–303 K window, all scoring 100. They span various composition variables (mole fraction, mass fraction, molality) and pressur

<details><summary>Result</summary>

```
**Summary:** 17 binary water+1-propanol mass density blocks found in the 293–303 K window, all scoring 100. They span various composition variables (mole fraction, mass fraction, molality) and pressure conditions (atmospheric to ~30 MPa).

| # | DOI | Block | GLOBlit | Pts(kept) | Comp. Var | Comp. Range | T (K) | P note | ρ (kg/m³) |
|---|-----|-------|---------|-----------|-----------|-------------|--------|--------|-----------|
| 1 | 10.1016/j.fluid.2007.07.066 | PROPblock_8 | GLOBlit_555 | 13 | GLOBvar_5 w | 0.05–0.15 | 283.15–303.15 | atm | 976.004–992.444 |
| 2 | 10.1016/j.fluid.2008.01.004 | PROPblock_5 | GLOBlit_590 | 15 | GLOBvar_5 w | 0.05–0.15 | 283.15–303.15 | atm | 975.791–992.405 |
| 3 | 10.1016/j.jct.2004.07.019 | PROPblock_3 | GLOBlit_2432 | 19 | GLOBvar_4 b | 0.10076–0.77737 | 298.15–318.14 | 420–29930 kPa | -7.7183– -1.0456 |
| 4 | 10.1016/j.jct.2008.07.005 | PROPblock_9 | GLOBlit_2979 | 12 | GLOBvar_2 x | 0–0.2 | 283.15–298.15 | atm | 919.56–999.69 |
| 5 | 10.1016/j.jct.2013.11.036 | PROPblock_1 | GLOBlit_4068 | 48 | GLOBvar_4 b | 2.531–14.377 | 302.13–582.08 | 2353–14377 kPa | 540–977.7 |
| 6 | 10.1016/j.jct.2013.11.036 [GLOBlit_4068] | PROP
```
</details>

---

### Step 9 [main - Q_1 - L1_1 · c7]: `inspect_block_table`

<details><summary>Arguments</summary>

```json
{
  "block_number": "PROPblock_9",
  "literature": "GLOBlit_2979",
  "nearest": {
    "column": "temperature_k",
    "value": 298.15,
    "k": 8
  },
  "purpose": "Get density data points near 298.15 K for water+1-propanol binary",
  "tasks": "Return data rows near 298.15 K with mole fraction and density values"
}
```
</details>

- **Result:** 1,118 chars  |  **Time:** 0.1s  |  **Started:** 05:04:41 (t+133.7s)

<details><summary>Result</summary>

```
**Data inspection** — 10.1016/j.jct.2008.07.005 [GLOBlit_2979] :: PROPblock_9 (binary: propan-1-ol + water)
filter: nearest temperature_k ≈ 298.15 (k=8)
block constraints: pressure_kpa = 98.93

| BLKpoint_id | temperature_k | mole_fraction_<propan-1-ol> | pressure_kpa | mass_density_kg_m3 |
|---|---|---|---|---|
| BLKpoint_49 | 298.15 | 0 | 98.93 | 997.04 |
| BLKpoint_50 | 298.15 | 0.002 | 98.93 | 995.4 |
| BLKpoint_51 | 298.15 | 0.005 | 98.93 | 993.76 |
| BLKpoint_52 | 298.15 | 0.009 | 98.93 | 991.66 |
| BLKpoint_53 | 298.15 | 0.01 | 98.93 | 991.14 |
| BLKpoint_54 | 298.15 | 0.02 | 98.93 | 986.54 |
| BLKpoint_55 | 298.15 | 0.03 | 98.93 | 982.56 |
| BLKpoint_56 | 298.15 | 0.05 | 98.93 | 975.49 |

mode: nearest — 8 row(s) of 96 matched (block has 96)
bracket: exact row(s) at temperature_k = 298.15 exist in the matched set
stats (matched, n=96): temperature_k 283.15–308.15 (n=96); mole_fraction_propan_1_ol 0–0.2 (n=96); pressure_kpa 98.93–98.93 (n=96); mass_density_kg_m3 911.83–999.69 (n=96)
inspection_id: INSP_884f359f5908
Data points may be quoted ONLY verbatim from the table above or the stats lines.
```
</details>

---

## Nested tool calls — L1_2 (L1-query)

**Nest:** main - Q_1 - L1_2
**Parent:** `L1_query` — Step 2 [main - Q_1 · c14] relays this worker's result
**Started:** 05:07:08  |  **Ended:** 05:10:56  |  **Tool calls:** 5

---

### Step 1 [main - Q_1 - L1_2 · c9]: `inspect_block_table` ❌ ERROR

<details><summary>Arguments</summary>

```json
{
  "block_number": "PROPblock_5",
  "literature": "GLOBlit_590",
  "nearest": "T=298.15 K",
  "purpose": "Inspect mass density data for water+1-propanol at 298.15 K",
  "tasks": "Return verbatim data points nearest to T=298.15 K from GLOBlit_590::PROPblock_5"
}
```
</details>

- **Result:** 249 chars  |  **Time:** 0.0s  |  **Started:** 05:07:16 (t+289.5s)
- **Error:** `{
  "error": "TOOL_ARGUMENT_REFINEMENT_REQUIRED: inspect_block_table.nearest received 'T=298.15 K' (str); expected dict | None; tool arguments are never coerced",
  "error_code": "TOOL_ARGUMENT_REFINEMENT_REQUIRED",
  "tool": "inspect_block_table"
}`

---

### Step 2 [main - Q_1 - L1_2 · c10]: `inspect_block_table`

<details><summary>Arguments</summary>

```json
{
  "block_number": "PROPblock_5",
  "literature": "GLOBlit_590",
  "nearest": {
    "Temperature": 298.15
  },
  "purpose": "Inspect GLOBlit_590::PROPblock_5 for data points at 298.15 K",
  "tasks": "Return verbatim data rows nearest to T=298.15 K for water+1-propanol mass density block"
}
```
</details>

- **Result:** 379 chars  |  **Time:** 0.2s  |  **Started:** 05:07:21 (t+294.3s)

<details><summary>Result</summary>

```
**inspect_block_table error** — nearest must be {"column": alias, "value": number, "k": 1..8}

| alias | n_finite | min | max |
|---|---|---|---|
| mass_fraction_propan_1_ol | 15 | 0.05 | 0.15 |
| temperature_k | 15 | 283.15 | 303.15 |
| pressure_kpa | 15 | 101 | 101 |
| mass_density_kg_m3 | 15 | 975.791 | 992.405 |

Use these aliases in `where` / `nearest` with plain numbers.
```
</details>

---

### Step 3 [main - Q_1 - L1_2 · c11]: `inspect_block_table`

<details><summary>Arguments</summary>

```json
{
  "block_number": "PROPblock_5",
  "literature": "GLOBlit_590",
  "nearest": {
    "column": "temperature_k",
    "value": 298.15,
    "k": 8
  },
  "purpose": "Inspect GLOBlit_590::PROPblock_5 for data points nearest 298.15 K",
  "tasks": "Return verbatim density data at or near 298.15 K for water+1-propanol binary"
}
```
</details>

- **Result:** 1,125 chars  |  **Time:** 0.2s  |  **Started:** 05:07:34 (t+307.1s)

<details><summary>Result</summary>

```
**Data inspection** — 10.1016/j.fluid.2008.01.004 [GLOBlit_590] :: PROPblock_5 (binary: propan-1-ol + water)
filter: nearest temperature_k ≈ 298.15 (k=8)
block constraints: pressure_kpa = 101.0

| BLKpoint_id | mass_fraction_<propan-1-ol> | temperature_k | pressure_kpa | mass_density_kg_m3 |
|---|---|---|---|---|
| BLKpoint_3 | 0.05 | 293.15 | 101.0 | 990.671 |
| BLKpoint_8 | 0.1 | 293.15 | 101.0 | 984.913 |
| BLKpoint_13 | 0.15 | 293.15 | 101.0 | 979.828 |
| BLKpoint_4 | 0.05 | 298.15 | 101.0 | 989.387 |
| BLKpoint_9 | 0.1 | 298.15 | 101.0 | 983.372 |
| BLKpoint_14 | 0.15 | 298.15 | 101.0 | 977.921 |
| BLKpoint_5 | 0.05 | 303.15 | 101.0 | 987.86 |
| BLKpoint_10 | 0.1 | 303.15 | 101.0 | 981.595 |

mode: nearest — 8 row(s) of 15 matched (block has 15)
bracket: exact row(s) at temperature_k = 298.15 exist in the matched set
stats (matched, n=15): mass_fraction_propan_1_ol 0.05–0.15 (n=15); temperature_k 283.15–303.15 (n=15); pressure_kpa 101.0–101.0 (n=15); mass_density_kg_m3 975.791–992.405 (n=15)
inspection_id: INSP_859136865c90
Data points may be quoted ONLY verbatim from the table above or the stats lines.
```
</details>

---

### Step 5 [main - Q_1 - L1_2 · c12]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_1",
    "GLOBcomp_5"
  ],
  "property": "GLOBprop_1",
  "system_type": "binary",
  "temperature_range": [
    293.0,
    303.0
  ],
  "limit": 50,
  "purpose": "Find all mass density blocks for water+1-propanol binary near 298.15 K",
  "tasks": "List all blocks with DOI, GLOBlit, block number, composition variable, T range, P, density range"
}
```
</details>

- **Result:** 1,186 chars  |  **Time:** 22.7s  |  **Started:** 05:07:48 (t+321.0s)
- **Subagent:** KEEP in 11,346 → 1,186 chars (15.4s)
  - **Summary:** 17 mass density blocks found for water + 1-propanol binary systems within 293–303 K. All report liquid-phase mass density (GLOBprop_1, kg/m³). Composition variables vary across blocks (mo

<details><summary>Result</summary>

```
**Summary:** 17 mass density blocks found for water + 1-propanol binary systems within 293–303 K. All report liquid-phase mass density (GLOBprop_1, kg/m³). Composition variables vary across blocks (mole fraction x, mass fraction w, or molality b). Most are at atmospheric pressure (constraint); a few span elevated pressures.

| # | DOI | GLOBlit | Block | Comp. Var | T (K) | P (kPa) | ρ (kg/m³) | Pts |
|---|-----|---------|-------|-----------|--------|----------|-----------|-----|
| 1 | 10.1016/j.fluid.2007.07.066 | GLOBlit_555 | PROPblock_8 | w (GLOBvar_5) 0.05–0.15 | 283.15–303.15 | constr (atm) | 976.004–992.444 | 13 |
| 2 | 10.1016/j.fluid.2008.01.004 | GLOBlit_590 | PROPblock_5 | w (GLOBvar_5) 0.05–0.15 | 283.15–303.15 | constr (atm) | 975.791–992.405 | 15 |
| 3 | 10.1016/j.jct.2004.07.019 | GLOBlit_2432 | PROPblock_3 | b (GLOBvar_4) 0.10076–0.77737 | 298.15–318.14 | 420–29930 | −7.7183––1.0456 | 19 |
| 4 | 10.1016/j.jct.2008.07.005 | GLOBlit_2979 | PROPblock_9 | x (GLOBvar_2) 0–0.2 | 283.15–298.15 | constr (atm) | 919.56–999.69 | 12 |
| 5 | 10.1016/j.jct.2013.11.036 | GLOBlit_4068 | PROPblock_1 | b (GLOBvar_4) 2.531–14.377 | 302.13–582.08 | 2353–14377 | 540–977.7
```
</details>

---

### Step 6 [main - Q_1 - L1_2 · c13]: `search_system_registry`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_1",
    "GLOBcomp_5"
  ],
  "property": "GLOBprop_1",
  "system_type": "binary",
  "temperature_range": [
    293,
    303
  ],
  "limit": 50,
  "purpose": "List all blocks for water+1-propanol binary density near 298.15 K",
  "tasks": "Return full list of blocks with DOI, GLOBlit, block number, composition variable, T range, P, density range"
}
```
</details>

- **Result:** 1,214 chars  |  **Time:** 17.9s  |  **Started:** 05:08:18 (t+351.3s)
- **Subagent:** KEEP in 2,231 → 1,019 chars (12.8s)
  - **Summary:** 14 binary water + propan-1-ol density blocks were found in the 293–303 K window. The block detail sections are empty, so composition variable, exact T range, P, and density range per bloc

<details><summary>Result</summary>

```
**Summary:** 14 binary water + propan-1-ol density blocks were found in the 293–303 K window. The block detail sections are empty, so composition variable, exact T range, P, and density range per block are **not available** from this search — only DOI, block ID, and point count are returned.

| # | DOI | Block | Points |
|---|-----|-------|--------|
| 1 | 10.1016/j.fluid.2007.07.066 [GLOBlit_555] | PROPblock_8 | 15 |
| 2 | 10.1016/j.fluid.2008.01.004 [GLOBlit_590] | PROPblock_5 | 15 |
| 3 | 10.1016/j.jct.2004.07.019 [GLOBlit_2432] | PROPblock_3 | 456 |
| 4 | 10.1016/j.jct.2008.07.005 [GLOBlit_2979] | PROPblock_9 | 96 |
| 5 | 10.1016/j.jct.2013.11.036 [GLOBlit_4068] | PROPblock_1 | 174 |
| 6 | 10.1016/j.jct.2013.11.036 [GLOBlit_4068] | PROPblock_2 | 29 |
| 7 | 10.1016/j.jct.2015.06.024 [GLOBlit_4415] | PROPblock_5 | 40 |
| 8 | 10.1016/j.jct.2019.105880 [GLOBlit_5585] | PROPblock_7 | 16 |
| 9 | 10.1021/acs.jced.6b01058 [GLOBlit_7085] | PROPblock_8 | 12 |
| 10 | 10.1021/acs.jced.7b00299 [GLOBlit_7178] | PROPblock_13 | 2 |
| 11 | 10.1021/je034101z [GLOBlit_8254] | PROPblock_6 | 380 |
| 12 | 10.1021/je4003515 [GLOBlit_10159] | PROPblock_10 | 25 |
| 13 | 10.1021/je800158z [GLOBlit_11142] | PROPblock_3
```
</details>

---

## Tool Compaction Pipeline (10 calls)

| # | Tool | Pipeline | Native | Hardcoded | Agentic | Verdict | Native→Final | Section |
|--:|------|----------|-------:|----------:|--------:|---------|-------------:|---------|
| 1 | `resolve_compound_ids` | query | 568 | 283 | 198 | KEEP | −65% | L1_1 |
| 2 | `search_blocks` | query | 108,641 | 11,346 | 766 | KEEP | −99% | L1_1 |
| 3 | `inspect_block_table` | query | 1,142 | 379 | 379 | SKIP | −67% | L1_1 |
| 4 | `inspect_block_table` | query | 3,566 | 966 | 966 | SKIP | −73% | L1_1 |
| 5 | `search_blocks` | query | 108,641 | 11,346 | 1,164 | KEEP | −99% | L1_1 |
| 6 | `inspect_block_table` | query | 4,156 | 1,103 | 1,103 | SKIP | −73% | L1_1 |
| 7 | `inspect_block_table` | query | 1,142 | 379 | 379 | SKIP | −67% | L1_2 |
| 8 | `inspect_block_table` | query | 4,176 | 1,111 | 1,111 | SKIP | −73% | L1_2 |
| 9 | `search_blocks` | query | 108,641 | 11,346 | 1,186 | KEEP | −99% | L1_2 |
| 10 | `search_system_registry` | query | 61,525 | 2,231 | 1,019 | KEEP | −98% | L1_2 |

## Subagent Summary (5 events)

| Tool | Verdict | Input Chars | Output Chars | Time | Section |
|------|---------|-------------|-------------|------|---------|
| resolve_compound_ids | KEEP | 283 | 198 | 4.8s | L1_1 |
| search_blocks | KEEP | 11,346 | 766 | 15.0s | L1_1 |
| search_blocks | KEEP | 11,346 | 1,164 | 15.0s | L1_1 |
| search_blocks | KEEP | 11,346 | 1,186 | 15.4s | L1_2 |
| search_system_registry | KEEP | 2,231 | 1,019 | 12.8s | L1_2 |

## Errors (2)

- **Step 5 · L1_1** `inspect_block_table` (exception): {
  "error": "TOOL_ARGUMENT_REFINEMENT_REQUIRED: inspect_block_table.nearest received 'T=298.15 K' (str); expected dict | None; tool arguments are never coerced",
  "error_code": "TOOL_ARGUMENT_REFINE
- **Step 1 · L1_2** `inspect_block_table` (exception): {
  "error": "TOOL_ARGUMENT_REFINEMENT_REQUIRED: inspect_block_table.nearest received 'T=298.15 K' (str); expected dict | None; tool arguments are never coerced",
  "error_code": "TOOL_ARGUMENT_REFINE

---

**Total:** 14 tool calls  |  Tool time: 573.4s  |  Wall: 655.3s  |  **Status:** OK
