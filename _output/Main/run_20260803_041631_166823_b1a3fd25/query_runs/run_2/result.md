# Delegated query run — result

**Question:** Search for binary mixture data blocks containing water (GLOBcomp_1) with any of these co-solvents: ethanol (GLOBcomp_2), methanol (GLOBcomp_4), ethylene glycol (GLOBcomp_24), glycerol (GLOBcomp_58), DMSO (GLOBcomp_31), acetonitrile (GLOBcomp_15), 2-propanol (GLOBcomp_6). Look for properties: viscosity (GLOBprop_4), density (GLOBprop_1), surface tension (GLOBprop_13), excess molar volume (GLOBprop_28), electrical conductivity (GLOBprop_18). Report which co-solvent systems have the most comprehensive data coverage across these properties, with DOIs, block numbers, temperature ranges, and composition ranges.

**Iterations:** 2  |  **Elapsed:** 1041.0s  |  **Tools:** 4  |  **Timed out:** False

---

## Answer

{
  "answer": "# Water + Co-Solvent Binary Systems: Transport and Excess Property Data Coverage in ThermoML\n\n## Overview\n\nBased on comprehensive searches of the ThermoML database, here is the data availability for binary mixtures of water with seven co-solvents across five electrodeposition-relevant properties: viscosity, mass density, surface tension, excess molar volume, and electrical conductivity.\n\n---\n\n## Summary Comparison Table\n\n| Property | Water+Ethanol | Water+Methanol | Water+Ethylene Glycol | Water+Glycerol | Water+DMSO | Water+Acetonitrile | Water+2-Propanol |\n|----------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|\n| **Mass Density** (GLOBprop_1) | 29 blocks, 22 DOIs, 268–618 K | 18 blocks, 14 DOIs, ~273–619 K | 16 blocks, ~278–446 K | * | * | * | * |\n| **Viscosity** (GLOBprop_4) | 14 blocks, 14 DOIs, 268–618 K | 6 blocks, 6 DOIs, 273–618 K | 7 blocks, ~273–450 K | * | * | * | * |\n| **Surface Tension** (GLOBprop_13) | 3 blocks, 293–313 K | **None** | 4 blocks, 283–323 K | * | * | * | * |\n| **Excess Molar Volume** (GLOBprop_28) | **None** | 2 blocks, 298–623 K | 1 block, 283–313 K | * | * | * | * |\n| **Electrical Conductivity** (GLOBprop_18) | 1 block (sparse) | **None** | **None** | * | * | * | * |\n\n\\* Data for glycerol, DMSO, acetonitrile, and 2-propanol systems could not be retrieved within the time constraints due to query size limits. The three fully characterized systems are detailed below.\n\n---\n\n## Detailed Results by System\n\n### 1. Water + Ethanol (GLOBcomp_1 + GLOBcomp_2) — Best Overall Coverage\n\n- **Mass Density**: 29 blocks from 22 DOIs, 268–618 K, pressures from atmospheric to 40 MPa. Richest dataset. Representative: GLOBlit_220/PROPblock_2 (DOI: 10.1016/j.fluid.2004.11.019) — 810 data points at 298–348 K, 100–40,000 kPa, x(ethanol) 0.003–1.0, density range 739–1013 kg/m³.\n- **Viscosity**: 14 blocks from 14 DOIs, 268–618 K. Representative: GLOBlit_5201/PROPblock_21 (DOI: 10.1016/j.jct.2018.02.022) — 100 points, 293–308 K, x(ethanol) 0.02–0.93, viscosity 0.76–2.86 mPa·s.\n- **Surface Tension**: 3 blocks, 293–313 K. Best: GLOBlit_7794/PROPblock_16 (DOI: 10.1021/acs.jced.9b00026) — 10 points, 298–313 K, w(ethanol) 0–0.2, γ = 36.7–72.0 mN/m.\n- **Electrical Conductivity**: 1 block only — GLOBlit_7483/PROPblock_11 (DOI: 10.1021/acs.jced.8b00181) — 6 points at 298 K, ethanol molality 0.9–9.51 mol/kg, σ = 0.248–0.311 mS/m.\n- **Excess Molar Volume**: No data found.\n\n### 2. Water + Methanol (GLOBcomp_1 + GLOBcomp_4) — Good Density/Viscosity, Has V^E\n\n- **Mass Density**: 18 blocks from 14 DOIs, ~273–619 K, atmospheric to 60 MPa. Representative: GLOBlit_2432/PROPblock_1 (DOI: 10.1016/j.jct.2004.07.019) — 596 points, 298–573 K, 390–30,300 kPa.\n- **Viscosity**: 6 blocks from 6 DOIs, 273–618 K. Representative: GLOBlit_2825/PROPblock_9 (DOI: 10.1016/j.jct.2007.05.004) — 39 points, 293–303 K, x(water) 0–1.0, viscosity 0.51–1.79 mPa·s at 101 kPa.\n- **Excess Molar Volume**: 2 blocks (240 total points). Best near-ambient: GLOBlit_2395/PROPblock_1 (DOI: 10.1016/j.jct.2004.03.011) — 206 points, 298–523 K, 100–60,000 kPa, x(MeOH) 0.25–0.75, V^E negative throughout. Supercritical: GLOBlit_895/PROPblock_2 (DOI: 10.1016/j.fluid.2010.10.005) — 34 points at 623 K.\n- **Surface Tension**: No data found.\n- **Electrical Conductivity**: No data found.\n\n### 3. Water + Ethylene Glycol (GLOBcomp_1 + GLOBcomp_24) — Best Surface Tension Coverage\n\n- **Mass Density**: 16 blocks, ~278–446 K. Representative: GLOBlit_5201/PROPblock_22 (DOI: 10.1016/j.jct.2018.02.022) — 224 points, 293–308 K, x(EG) 0–1.0, density 994–1114 kg/m³.\n- **Viscosity**: 7 blocks, ~273–450 K. Representative: GLOBlit_5201/PROPblock_24 (DOI: 10.1016/j.jct.2018.02.022) — 84 points, 293–308 K, x(EG) 0–1.0, viscosity 0.76–20.6 mPa·s. Note the much higher viscosity range compared to ethanol/methanol systems — ethylene glycol is ~20× more viscous than water.\n- **Surface Tension**: 4 blocks, 283–323 K. Best: GLOBlit_3286/PROPblock_4 (DOI: 10.1016/j.jct.2010.09.003) — 54 points, 283–308 K, x(EG) 0.008–0.899, γ = 47.9–73.5 mN/m. Also: GLOBlit_11186/PROPblock_3 (DOI: 10.1021/je800271e) — 52 points, 308–323 K, full composition range.\n- **Excess Molar Volume**: 1 block — GLOBlit_1283/PROPblock_11 (DOI: 10.1016/j.fluid.2013.06.041) — 135 points, 283–313 K, x(EG) 0.01–0.94, all V^E values negative (indicating attractive water–EG interactions and volume contraction on mixing).\n- **Electrical Conductivity**: No data found.\n\n---\n\n## Ranking by Comprehensiveness\n\n| Rank | System | Properties Covered (of 5) | Total Blocks | Strengths | Gaps |\n|------|--------|:---:|:---:|-----------|------|\n| 1 | **Water + Ethanol** | 4/5 | ~47 | Most density & viscosity blocks; only system with conductivity data | No excess molar volume |\n| 2 | **Water + Ethylene Glycol** | 4/5 | ~28 | Best surface tension coverage (4 blocks); has V^E data | No conductivity |\n| 3 | **Water + Methanol** | 3/5 | ~26 | Best excess molar volume coverage (2 blocks, 240 pts); good density | No surface tension, no conductivity |\n\n---\n\n## Key Chemistry Insights for Electrodeposition Applications\n\n1. **Electrical conductivity is the scarcest property** across all three fully characterized systems. Only water+ethanol has any data (6 points at a single temperature from one source). This is a critical gap for electrodeposition bath design, where ionic transport is paramount.\n\n2. **Viscosity varies dramatically** across co-solvents: water+ethylene glycol mixtures reach ~20 mPa·s (pure EG at 293 K), while water+ethanol and water+methanol stay below ~3 mPa·s. Higher viscosity reduces mass transport rates to the electrode, which can limit deposition current density but may improve deposit uniformity.\n\n3. **Surface tension** is best characterized for water+ethylene glycol (47.9–73.5 mN/m across compositions). Ethylene glycol's high surface tension (~48 mN/m pure) compared to ethanol (~22 mN/m) means water+EG mixtures maintain better wetting characteristics, which is important for uniform coating.\n\n4. **Excess molar volumes are uniformly negative** for both water+methanol and water+ethylene glycol, indicating strong hydrogen-bonding interactions and volume contraction on mixing — relevant for predicting solution densities at intermediate compositions.\n\n5. **For comprehensive electrodeposition solvent design**, the water+ethanol system offers the broadest property coverage including the only available conductivity data, while water+ethylene glycol provides the best surface tension characterization. A combined dataset from multiple systems would be needed for robust solvent optimization.\n\n---\n\n## Data Gaps and Recommendations\n\n- **Glycerol, DMSO, acetonitrile, and 2-propanol** systems with water could not be fully characterized within the query constraints. These systems likely have data in ThermoML but require individual targeted searches.\n- **Electrical conductivity** is critically underrepresented for all aqueous co-solvent systems — additional experimental measurements or alternative data sources would be needed for electrodeposition modeling.\n- **Temperature coverage** is best for density and viscosity (extending to supercritical conditions for ethanol and methanol), but surface tension and excess volume data are largely limited to near-ambient conditions (283–323 K).",
  "core_claims": [
    "Of the seven water + co-solvent binary systems targeted (ethanol, methanol, ethylene glycol, glycerol, DMSO, acetonitrile, 2-propanol), only the first three could be fully characterized from ThermoML within the query constraints; glycerol, DMSO, acetonitrile, and 2-propanol systems were not retrieved.",
    "Water + ethanol has the broadest overall ThermoML coverage (4 of 5 target properties, ~47 blocks), including the only electrical conductivity data found (6 points at 298 K from one source), but lacks excess molar volume data.",
    "Water + ethylene glycol has the best surface tension coverage (4 blocks, 283–323 K, γ = 47.9–73.5 mN/m) and also provides excess molar volume and viscosity data, but lacks electrical conductivity data.",
    "Water + methanol has the best excess molar volume coverage (2 blocks, 240 points, 298–623 K) with uniformly negative V^E values, but lacks surface tension and electrical conductivity data.",
    "Electrical conductivity is the scarcest property across all characterized systems, representing a critical data gap for electrodeposition bath design where ionic transport is essential.",
    "Excess molar volumes are uniformly negative for both water + methanol and water + ethylene glycol, indicating strong hydrogen-bonding interactions and volume contraction on mixing.",
    "Viscosity varies dramatically across co-solvents: water + ethylene glycol mixtures reach ~20 mPa·s (pure EG at 293 K), while water + ethanol and water + methanol remain below ~3 mPa·s.",
    "Temperature coverage is broadest for density and viscosity (extending to ~618–623 K for ethanol and methanol systems), whereas surface tension and excess molar volume data are largely limited to near-ambient conditions (283–323 K)."
  ],
  "confidence": "medium",
  "sources": [
    {
      "doi": "10.1016/j.fluid.2004.11.019",
      "lit_num_id": "GLOBlit_220",
      "block": "PROPblock_2",
      "BLKsubsys_id": null,
      "description": "Water+ethanol mass density: 810 data points, 298–348 K, 100–40000 kPa, x(ethanol) 0.003–1.0, density 739–1013 kg/m³"
    },
    {
      "doi": "10.1016/j.jct.2018.02.022",
      "lit_num_id": "GLOBlit_5201",
      "block": "PROPblock_21",
      "BLKsubsys_id": null,
      "description": "Water+ethanol viscosity: 100 points, 293–308 K, x(ethanol) 0.02–0.93, viscosity 0.76–2.86 mPa·s"
    },
    {
      "doi": "10.1021/acs.jced.9b00026",
      "lit_num_id": "GLOBlit_7794",
      "block": "PROPblock_16",
      "BLKsubsys_id": null,
      "description": "Water+ethanol surface tension: 10 points, 298–313 K, w(ethanol) 0–0.2, γ = 36.7–72.0 mN/m"
    },
    {
      "doi": "10.1021/acs.jced.8b00181",
      "lit_num_id": "GLOBlit_7483",
      "block": "PROPblock_11",
      "BLKsubsys_id": null,
      "description": "Water+ethanol electrical conductivity: 6 points at 298 K, ethanol molality 0.9–9.51 mol/kg, σ = 0.248–0.311 mS/m"
    },
    {
      "doi": "10.1016/j.jct.2004.07.019",
      "lit_num_id": "GLOBlit_2432",
      "block": "PROPblock_1",
      "BLKsubsys_id": null,
      "description": "Water+methanol mass density: 596 points, 298–573 K, 390–30300 kPa"
    },
    {
      "doi": "10.1016/j.jct.2007.05.004",
      "lit_num_id": "GLOBlit_2825",
      "block": "PROPblock_9",
      "BLKsubsys_id": null,
      "description": "Water+methanol viscosity: 39 points, 293–303 K, x(water) 0–1.0, viscosity 0.51–1.79 mPa·s at 101 kPa"
    },
    {
      "doi": "10.1016/j.jct.2004.03.011",
      "lit_num_id": "GLOBlit_2395",
      "block": "PROPblock_1",
      "BLKsubsys_id": null,
      "description": "Water+methanol excess molar volume: 206 points, 298–523 K, 100–60000 kPa, x(MeOH) 0.25–0.75, V^E negative throughout"
    },
    {
      "doi": "10.1016/j.fluid.2010.10.005",
      "lit_num_id": "GLOBlit_895",
      "block": "PROPblock_2",
      "BLKsubsys_id": null,
      "description": "Water+methanol excess molar volume: 34 points at 623 K (supercritical)"
    },
    {
      "doi": "10.1016/j.jct.2018.02.022",
      "lit_num_id": "GLOBlit_5201",
      "block": "PROPblock_22",
      "BLKsubsys_id": null,
      "description": "Water+ethylene glycol mass density: 224 points, 293–308 K, x(EG) 0–1.0, density 994–1114 kg/m³"
    },
    {
      "doi": "10.1016/j.jct.2018.02.022",
      "lit_num_id": "GLOBlit_5201",
      "block": "PROPblock_24",
      "BLKsubsys_id": null,
      "description": "Water+ethylene glycol viscosity: 84 points, 293–308 K, x(EG) 0–1.0, viscosity 0.76–20.6 mPa·s"
    },
    {
      "doi": "10.1016/j.jct.2010.09.003",
      "lit_num_id": "GLOBlit_3286",
      "block": "PROPblock_4",
      "BLKsubsys_id": null,
      "description": "Water+ethylene glycol surface tension: 54 points, 283–308 K, x(EG) 0.008–0.899, γ = 47.9–73.5 mN/m"
    },
    {
      "doi": "10.1021/je800271e",
      "lit_num_id": "GLOBlit_11186",
      "block": "PROPblock_3",
      "BLKsubsys_id": null,
      "description": "Water+ethylene glycol surface tension: 52 points, 308–323 K, full composition range"
    },
    {
      "doi": "10.1016/j.fluid.2013.06.041",
      "lit_num_id": "GLOBlit_1283",
      "block": "PROPblock_11",
      "BLKsubsys_id": null,
      "description": "Water+ethylene glycol excess molar volume: 135 points, 283–313 K, x(EG) 0.01–0.94, all V^E negative"
    }
  ],
  "id_catalog_snapshot": [
    {
      "type": "comp",
      "global_id": "GLOBcomp_1",
      "registry_id": "water",
      "name": "water"
    },
    {
      "type": "comp",
      "global_id": "GLOBcomp_2",
      "registry_id": "ethanol",
      "name": "ethanol"
    },
    {
      "type": "comp",
      "global_id": "GLOBcomp_4",
      "registry_id": "methanol",
      "name": "methanol"
    },
    {
      "type": "comp",
      "global_id": "GLOBcomp_24",
      "registry_id": "ethylene_glycol",
      "name": "ethylene glycol"
    },
    {
      "type": "comp",
      "global_id": "GLOBcomp_58",
      "registry_id": "glycerol",
      "name": "glycerol"
    },
    {
      "type": "comp",
      "global_id": "GLOBcomp_31",
      "registry_id": "DMSO",
      "name": "dimethyl sulfoxide"
    },
    {
      "type": "comp",
      "global_id": "GLOBcomp_15",
      "registry_id": "acetonitrile",
      "name": "acetonitrile"
    },
    {
      "type": "comp",
      "global_id": "GLOBcomp_6",
      "registry_id": "2-propanol",
      "name": "2-propanol"
    },
    {
      "type": "prop",
      "global_id": "GLOBprop_1",
      "registry_id": "density",
      "name": "mass density"
    },
    {
      "type": "prop",
      "global_id": "GLOBprop_4",
      "registry_id": "viscosity",
      "name": "viscosity"
    },
    {
      "type": "prop",
      "global_id": "GLOBprop_13",
      "registry_id": "surface_tension",
      "name": "surface tension"
    },
    {
      "type": "prop",
      "global_id": "GLOBprop_28",
      "registry_id": "excess_molar_volume",
      "name": "excess molar volume"
    },
    {
      "type": "prop",
      "global_id": "GLOBprop_18",
      "registry_id": "conductivity",
      "name": "electrical conductivity"
    }
  ],
  "follow_up_suggestions": [
    "Run targeted L1_query searches for water+glycerol (GLOBcomp_58), water+DMSO (GLOBcomp_31), water+acetonitrile (GLOBcomp_15), and water+2-propanol (GLOBcomp_6) individually with narrower property filters to avoid result compaction errors.",
    "Retry the water+DMSO query with corrected system_type specification (binary rather than unary) to resolve the checksum mismatch error encountered.",
    "Search specifically for electrical conductivity (GLOBprop_18) across all seven co-solvent systems, as this property is critically underrepresented and most important for electrodeposition bath design.",
    "Investigate whether ThermoML contains ternary system data (water + co-solvent + electrolyte salt) that would be more directly relevant to electrodeposition bath formulation."
  ]
}
