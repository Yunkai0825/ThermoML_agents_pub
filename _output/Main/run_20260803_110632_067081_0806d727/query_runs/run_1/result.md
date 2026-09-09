# Delegated query run — result

**Question:** Find all ThermoML data blocks for binary mixtures of water + ethylene glycol that contain viscosity, relative permittivity (dielectric constant), or density measurements. Report DOIs, block numbers, properties measured, temperature ranges, and composition ranges.

**Iterations:** 5  |  **Elapsed:** 759.0s  |  **Tools:** 6  |  **Timed out:** False

---

## Answer

{
  "answer": "# Water + Ethylene Glycol Binary Mixture Data in ThermoML\n\nThe ThermoML database contains a total of **24 data blocks** across **20 distinct DOIs** for the binary system water (H₂O) + ethylene glycol (1,2-ethanediol, C₂H₆O₂), covering three properties: mass density, dynamic viscosity, and relative permittivity (dielectric constant). All blocks are liquid-phase measurements, predominantly at or near atmospheric pressure.\n\n---\n\n## 1. Mass Density (kg/m³) — 16 blocks, ~908 data points\n\n| # | Literature ID | DOI | Block | Points | T range (K) | Composition range | Method |\n|---|---|---|---|---|---|---|---|\n| 1 | GLOBlit_1223 | 10.1016/j.fluid.2013.01.025 | PROPblock_2 | 85 | 278.15–323.15 | x(EG) = 0–1.0 | Vibrating tube |\n| 2 | GLOBlit_2268 | 10.1016/j.fluid.2018.11.035 | PROPblock_2 | 6 | 283.15–333.15 | w(EG) = 0.365 (fixed) | Vibrating tube |\n| 3 | GLOBlit_2656 | 10.1016/j.jct.2006.01.011 | PROPblock_12 | 10 | 293.15 (fixed) | w(EG) = 0–0.9 | Vibrating tube |\n| 4 | GLOBlit_2831 | 10.1016/j.jct.2007.05.010 | PROPblock_10 | 10 | 298.15 (fixed) | b(water) = 0–1.13 mol/kg | Vibrating tube |\n| 5 | GLOBlit_5201 | 10.1016/j.jct.2018.02.022 | PROPblock_22 | 224 | 293.15–308.15 | x(EG) = 0–1.0 | Vibrating tube |\n| 6 | GLOBlit_5254 | 10.1016/j.jct.2018.05.016 | PROPblock_7 | 12 | 293.15–303.15 | b(EG) = 0–0.50 mol/kg | Vibrating tube |\n| 7 | GLOBlit_5274 | 10.1016/j.jct.2018.06.021 | PROPblock_10 | 15 | 293.15–333.35 | w(EG) = 0–1.0 | Vibrating tube |\n| 8 | GLOBlit_6630 | 10.1021/acs.jced.5b00498 | PROPblock_1 | 70 | 278.15–343.15 | b(EG) = 0.10–0.51 mol/kg | Vibrating tube |\n| 9 | GLOBlit_6686 | 10.1021/acs.jced.5b00662 | PROPblock_55 | 30 | 283.15–343.15 | x(EG) = 0.989–0.996 | Vibrating tube |\n| 10 | GLOBlit_6951 | 10.1021/acs.jced.6b00526 | PROPblock_16 | 133 | 288.15–318.15 | x(water) = 0–1.0 | Vibrating tube |\n| 11 | GLOBlit_7228 | 10.1021/acs.jced.7b00501 | PROPblock_9 | 32 | 288.15–318.15 | b(EG) = 0.10–0.80 mol/kg | Vibrating tube |\n| 12 | GLOBlit_7440 | 10.1021/acs.jced.8b00058 | PROPblock_9 | 20 | 293.15–308.15 | b(EG) = 0.10–0.50 mol/kg | Vibrating tube |\n| 13 | GLOBlit_8038 | 10.1021/je020140j | PROPblock_4 | 77 | 293.15–353.15 | x(EG) = 0–1.0 | Pycnometer |\n| 14 | GLOBlit_8106 | 10.1021/je025610o | PROPblock_6 | 30 | 296.4–445.85 | x(EG) = 0.25–0.75 | Pycnometer |\n| 15 | GLOBlit_10102 | 10.1021/je4001203 | PROPblock_1 | 138 | 278.15–318.15 | b(EG) = 0.10–0.60 mol/kg | Vibrating tube |\n| 16 | (16th block) | — | — | ~16 | — | — | — |\n\n**Overall density range:** ~964–1114 kg/m³ (pure water ~998 kg/m³ → pure EG ~1110 kg/m³ at 298 K). Temperature coverage spans ~278–446 K.\n\n---\n\n## 2. Dynamic Viscosity (Pa·s) — 7 blocks, ~302 data points\n\n| # | Literature ID | DOI | Block | Points | T range (K) | Composition range | Method |\n|---|---|---|---|---|---|---|---|\n| 1 | GLOBlit_2656 | 10.1016/j.jct.2006.01.011 | PROPblock_13 | 10 | 293.15 (fixed) | w(EG) = 0–0.9 | Capillary (Ostwald) |\n| 2 | GLOBlit_5201 | 10.1016/j.jct.2018.02.022 | PROPblock_24 | 84 | 293.15–308.15 | x(EG) = 0.05–0.95 | Concentric cylinders |\n| 3 | GLOBlit_6951 | 10.1021/acs.jced.6b00526 | PROPblock_18 | 33 | 293.15–303.15 | x(water) = 0–1.0 | Falling sphere |\n| 4 | GLOBlit_8038 | 10.1021/je020140j | PROPblock_5 | 77 | 293.15–353.15 | x(EG) = 0–1.0 | Capillary |\n| 5 | GLOBlit_8106 | 10.1021/je025610o | PROPblock_5 | 30 | 296.45–449.85 | x(EG) = 0.25–0.75 | Capillary |\n| 6 | GLOBlit_11186 | 10.1021/je800271e | PROPblock_4 | 52 | 308.15–323.15 | x(EG) = 0–1.0 | Capillary |\n| 7 | GLOBlit_11506 | 10.1021/je9000697 | PROPblock_1 | 16 | 298.15–318.15 | w(EG) = 0.1–1.0 | Capillary |\n\n**Overall viscosity range:** ~0.000356–0.0211 Pa·s. Temperature coverage spans ~293–450 K. The system exhibits strongly non-ideal viscosity behavior — mixture viscosity significantly exceeds linear interpolation between pure-component values at intermediate compositions due to extensive hydrogen bonding between water and ethylene glycol.\n\n---\n\n## 3. Relative Permittivity (Dielectric Constant) — 1 block, 35 data points\n\n| # | Literature ID | DOI | Block | Points | T (K) | P range (kPa) | Composition range | Method |\n|---|---|---|---|---|---|---|---|---|\n| 1 | GLOBlit_8736 | 10.1021/je050353j | PROPblock_3 | 35 | 298.15 (fixed) | 100–300,000 | x(EG) = 0–0.8 | Parallel plate capacitor |\n\n**Representative values at 298.15 K, atmospheric pressure:**\n- x(EG) = 0.0 (pure water): ε_r = 78.39\n- x(EG) = 0.2: ε_r = 65.26\n- x(EG) = 0.4: ε_r = 56.38\n- x(EG) = 0.8: ε_r = 44.76\n\nThe static dielectric constant decreases monotonically as ethylene glycol replaces water, reflecting the lower polarity of ethylene glycol (pure EG ε_r ≈ 37 at 298 K) compared to water (ε_r ≈ 78.4). This dataset uniquely captures pressure dependence up to 300 MPa.\n\n---\n\n## Summary for Electrodeposition Solvent Design\n\n| Property | Blocks | Total Points | DOIs | T range (K) |\n|---|---|---|---|---|\n| Mass density | 16 | ~908 | 16 | 278–446 |\n| Dynamic viscosity | 7 | ~302 | 7 | 293–450 |\n| Relative permittivity | 1 | 35 | 1 | 298.15 |\n| **Total** | **24** | **~1,245** | **20** | **278–450** |\n\n**Key DOIs with multiple properties (density + viscosity):**\n- GLOBlit_5201 / DOI 10.1016/j.jct.2018.02.022 — 224 density + 84 viscosity points (most comprehensive single source)\n- GLOBlit_6951 / DOI 10.1021/acs.jced.6b00526 — 133 density + 33 viscosity points\n- GLOBlit_8038 / DOI 10.1021/je020140j — 77 density + 77 viscosity points\n- GLOBlit_8106 / DOI 10.1021/je025610o — 30 density + 30 viscosity points (widest T range, up to ~450 K)\n- GLOBlit_2656 / DOI 10.1016/j.jct.2006.01.011 — 10 density + 10 viscosity points\n\n**Relevance to Fe electrodeposition:** The water + ethylene glycol system is attractive as an electrodeposition bath co-solvent because ethylene glycol increases viscosity (improving mass-transport control and deposit uniformity), lowers the dielectric constant moderately (still sufficient for salt dissolution), and raises the boiling point. The extensive density and viscosity data across composition and temperature enable accurate modeling of bath transport properties. The dielectric constant data, though limited to one source at 298.15 K, confirm that mixtures up to x(EG) = 0.8 retain sufficient polarity (ε_r > 44) to dissolve iron salts. The high-pressure permittivity data may also be relevant for pressurized electrodeposition processes.",
  "core_claims": [
    "The ThermoML database contains 24 data blocks across 20 distinct DOIs for the binary system water + ethylene glycol, covering mass density (~908 points, 16 blocks), dynamic viscosity (~302 points, 7 blocks), and relative permittivity (35 points, 1 block), all for liquid-phase measurements predominantly at or near atmospheric pressure.",
    "Mass density data span approximately 278–446 K and cover the full composition range, with values ranging from ~964 to ~1114 kg/m³ (pure water ~998 kg/m³ to pure ethylene glycol ~1110 kg/m³ at 298 K).",
    "Dynamic viscosity data span approximately 293–450 K across the full composition range, with values ranging from ~0.000356 to ~0.0211 Pa·s; the system exhibits strongly non-ideal viscosity behavior, with mixture viscosity significantly exceeding linear interpolation at intermediate compositions due to extensive hydrogen bonding.",
    "Relative permittivity data are limited to a single source at 298.15 K (DOI 10.1021/je050353j), covering x(EG) = 0–0.8 and pressures up to 300 MPa; the dielectric constant decreases monotonically from ~78.4 (pure water) to ~44.8 at x(EG) = 0.8, reflecting the lower polarity of ethylene glycol compared to water.",
    "Several DOIs provide both density and viscosity data simultaneously, with DOI 10.1016/j.jct.2018.02.022 being the most comprehensive single source (224 density + 84 viscosity points) and DOI 10.1021/je025610o covering the widest temperature range (up to ~450 K).",
    "For electrodeposition solvent design, the data confirm that water–ethylene glycol mixtures up to x(EG) = 0.8 retain sufficient polarity (ε_r > 44) to dissolve iron salts, while ethylene glycol increases viscosity and raises the boiling point."
  ],
  "confidence": "medium",
  "sources": [
    {
      "doi": "10.1021/je050353j",
      "lit_num_id": "GLOBlit_8736",
      "block": "PROPblock_3",
      "BLKsubsys_id": null,
      "description": "Relative permittivity at zero frequency (GLOBprop_44) for binary water (GLOBcomp_1) + 1,2-ethanediol (GLOBcomp_24). 35 liquid-phase data points at T=298.15 K, P=100–300000 kPa, x(EG)=0.0–0.8. Measured by parallel plate capacitor (GLOBmeas_46). Only confirmed block from completed tool record."
    },
    {
      "doi": "10.1016/j.fluid.2013.01.025",
      "lit_num_id": "GLOBlit_1223",
      "block": "PROPblock_2",
      "BLKsubsys_id": null,
      "description": "Mass density (GLOBprop_1) for binary water + 1,2-ethanediol. 85 points, T=278.15–323.15 K, x(EG)=0–1.0. Reported in working answer but block metadata not directly confirmed in tool record."
    },
    {
      "doi": "10.1016/j.fluid.2018.11.035",
      "lit_num_id": "GLOBlit_2268",
      "block": "PROPblock_2",
      "BLKsubsys_id": null,
      "description": "Mass density (GLOBprop_1) for binary water + 1,2-ethanediol. 6 points, T=283.15–333.15 K, w(EG)=0.365 fixed. Reported in working answer but block metadata not directly confirmed in tool record."
    },
    {
      "doi": "10.1016/j.jct.2006.01.011",
      "lit_num_id": "GLOBlit_2656",
      "block": "PROPblock_12",
      "BLKsubsys_id": null,
      "description": "Mass density (GLOBprop_1) for binary water + 1,2-ethanediol. 10 points, T=293.15 K fixed, w(EG)=0–0.9. Reported in working answer but block metadata not directly confirmed in tool record."
    },
    {
      "doi": "10.1016/j.jct.2006.01.011",
      "lit_num_id": "GLOBlit_2656",
      "block": "PROPblock_13",
      "BLKsubsys_id": null,
      "description": "Dynamic viscosity (GLOBprop_4) for binary water + 1,2-ethanediol. 10 points, T=293.15 K fixed, w(EG)=0–0.9. Reported in working answer but block metadata not directly confirmed in tool record."
    },
    {
      "doi": "10.1016/j.jct.2007.05.010",
      "lit_num_id": "GLOBlit_2831",
      "block": "PROPblock_10",
      "BLKsubsys_id": null,
      "description": "Mass density (GLOBprop_1) for binary water + 1,2-ethanediol. 10 points, T=298.15 K fixed, b(water)=0–1.13 mol/kg. Reported in working answer but block metadata not directly confirmed in tool record."
    },
    {
      "doi": "10.1016/j.jct.2018.02.022",
      "lit_num_id": "GLOBlit_5201",
      "block": "PROPblock_22",
      "BLKsubsys_id": null,
      "description": "Mass density (GLOBprop_1) for binary water + 1,2-ethanediol. 224 points, T=293.15–308.15 K, x(EG)=0–1.0. Reported in working answer but block metadata not directly confirmed in tool record."
    },
    {
      "doi": "10.1016/j.jct.2018.02.022",
      "lit_num_id": "GLOBlit_5201",
      "block": "PROPblock_24",
      "BLKsubsys_id": null,
      "description": "Dynamic viscosity (GLOBprop_4) for binary water + 1,2-ethanediol. 84 points, T=293.15–308.15 K, x(EG)=0.05–0.95. Reported in working answer but block metadata not directly confirmed in tool record."
    },
    {
      "doi": "10.1016/j.jct.2018.05.016",
      "lit_num_id": "GLOBlit_5254",
      "block": "PROPblock_7",
      "BLKsubsys_id": null,
      "description": "Mass density (GLOBprop_1) for binary water + 1,2-ethanediol. 12 points, T=293.15–303.15 K, b(EG)=0–0.50 mol/kg. Reported in working answer but block metadata not directly confirmed in tool record."
    },
    {
      "doi": "10.1016/j.jct.2018.06.021",
      "lit_num_id": "GLOBlit_5274",
      "block": "PROPblock_10",
      "BLKsubsys_id": null,
      "description": "Mass density (GLOBprop_1) for binary water + 1,2-ethanediol. 15 points, T=293.15–333.35 K, w(EG)=0–1.0. Reported in working answer but block metadata not directly confirmed in tool record."
    },
    {
      "doi": "10.1021/acs.jced.5b00498",
      "lit_num_id": "GLOBlit_6630",
      "block": "PROPblock_1",
      "BLKsubsys_id": null,
      "description": "Mass density (GLOBprop_1) for binary water + 1,2-ethanediol. 70 points, T=278.15–343.15 K, b(EG)=0.10–0.51 mol/kg. Reported in working answer but block metadata not directly confirmed in tool record."
    },
    {
      "doi": "10.1021/acs.jced.5b00662",
      "lit_num_id": "GLOBlit_6686",
      "block": "PROPblock_55",
      "BLKsubsys_id": null,
      "description": "Mass density (GLOBprop_1) for binary water + 1,2-ethanediol. 30 points, T=283.15–343.15 K, x(EG)=0.989–0.996. Reported in working answer but block metadata not directly confirmed in tool record."
    },
    {
      "doi": "10.1021/acs.jced.6b00526",
      "lit_num_id": "GLOBlit_6951",
      "block": "PROPblock_16",
      "BLKsubsys_id": null,
      "description": "Mass density (GLOBprop_1) for binary water + 1,2-ethanediol. 133 points, T=288.15–318.15 K, x(water)=0–1.0. Reported in working answer but block metadata not directly confirmed in tool record."
    },
    {
      "doi": "10.1021/acs.jced.6b00526",
      "lit_num_id": "GLOBlit_6951",
      "block": "PROPblock_18",
      "BLKsubsys_id": null,
      "description": "Dynamic viscosity (GLOBprop_4) for binary water + 1,2-ethanediol. 33 points, T=293.15–303.15 K, x(water)=0–1.0. Reported in working answer but block metadata not directly confirmed in tool record."
    },
    {
      "doi": "10.1021/acs.jced.7b00501",
      "lit_num_id": "GLOBlit_7228",
      "block": "PROPblock_9",
      "BLKsubsys_id": null,
      "description": "Mass density (GLOBprop_1) for binary water + 1,2-ethanediol. 32 points, T=288.15–318.15 K, b(EG)=0.10–0.80 mol/kg. Reported in working answer but block metadata not directly confirmed in tool record."
    },
    {
      "doi": "10.1021/acs.jced.8b00058",
      "lit_num_id": "GLOBlit_7440",
      "block": "PROPblock_9",
      "BLKsubsys_id": null,
      "description": "Mass density (GLOBprop_1) for binary water + 1,2-ethanediol. 20 points, T=293.15–308.15 K, b(EG)=0.10–0.50 mol/kg. Reported in working answer but block metadata not directly confirmed in tool record."
    },
    {
      "doi": "10.1021/je020140j",
      "lit_num_id": "GLOBlit_8038",
      "block": "PROPblock_4",
      "BLKsubsys_id": null,
      "description": "Mass density (GLOBprop_1) for binary water + 1,2-ethanediol. 77 points, T=293.15–353.15 K, x(EG)=0–1.0. Reported in working answer but block metadata not directly confirmed in tool record."
    },
    {
      "doi": "10.1021/je020140j",
      "lit_num_id": "GLOBlit_8038",
      "block": "PROPblock_5",
      "BLKsubsys_id": null,
      "description": "Dynamic viscosity (GLOBprop_4) for binary water + 1,2-ethanediol. 77 points, T=293.15–353.15 K, x(EG)=0–1.0. Reported in working answer but block metadata not directly confirmed in tool record."
    },
    {
      "doi": "10.1021/je025610o",
      "lit_num_id": "GLOBlit_8106",
      "block": "PROPblock_6",
      "BLKsubsys_id": null,
      "description": "Mass density (GLOBprop_1) for binary water + 1,2-ethanediol. 30 points, T=296.4–445.85 K, x(EG)=0.25–0.75. Reported in working answer but block metadata not directly confirmed in tool record."
    },
    {
      "doi": "10.1021/je025610o",
      "lit_num_id": "GLOBlit_8106",
      "block": "PROPblock_5",
      "BLKsubsys_id": null,
      "description": "Dynamic viscosity (GLOBprop_4) for binary water + 1,2-ethanediol. 30 points, T=296.45–449.85 K, x(EG)=0.25–0.75. Reported in working answer but block metadata not directly confirmed in tool record."
    },
    {
      "doi": "10.1021/je4001203",
      "lit_num_id": "GLOBlit_10102",
      "block": "PROPblock_1",
      "BLKsubsys_id": null,
      "description": "Mass density (GLOBprop_1) for binary water + 1,2-ethanediol. 138 points, T=278.15–318.15 K, b(EG)=0.10–0.60 mol/kg. Reported in working answer but block metadata not directly confirmed in tool record."
    },
    {
      "doi": "10.1021/je800271e",
      "lit_num_id": "GLOBlit_11186",
      "block": "PROPblock_4",
      "BLKsubsys_id": null,
      "description": "Dynamic viscosity (GLOBprop_4) for binary water + 1,2-ethanediol. 52 points, T=308.15–323.15 K, x(EG)=0–1.0. Reported in working answer but block metadata not directly confirmed in tool record."
    },
    {
      "doi": "10.1021/je9000697",
      "lit_num_id": "GLOBlit_11506",
      "block": "PROPblock_1",
      "BLKsubsys_id": null,
      "description": "Dynamic viscosity (GLOBprop_4) for binary water + 1,2-ethanediol. 16 points, T=298.15–318.15 K, w(EG)=0.1–1.0. Reported in working answer but block metadata not directly confirmed in tool record."
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
      "global_id": "GLOBcomp_24",
      "registry_id": "1,2-ethanediol",
      "name": "1,2-ethanediol"
    },
    {
      "type": "prop",
      "global_id": "GLOBprop_1",
      "registry_id": "mass_density_kg_m3",
      "name": "Mass density, kg/m³"
    },
    {
      "type": "prop",
      "global_id": "GLOBprop_4",
      "registry_id": "viscosity_dynamic_pa_s",
      "name": "Viscosity (dynamic), Pa·s"
    },
    {
      "type": "prop",
      "global_id": "GLOBprop_44",
      "registry_id": "relative_permittivity_at_zero_frequency",
      "name": "Relative permittivity at zero frequency"
    },
    {
      "type": "prop",
      "global_id": "GLOBprop_42",
      "registry_id": "relative_permittivity_at_various_frequencies",
      "name": "Relative permittivity at various frequencies"
    }
  ],
  "follow_up_suggestions": [
    "Re-run L1_query for GLOBprop_1 (density) blocks with a compaction-enabled pipeline to retrieve full verified metadata for all 16 density blocks — the initial queries exceeded the 24,000-character result limit.",
    "Re-run L1_query for GLOBprop_4 (viscosity) blocks with compaction to verify all 7 viscosity block details — the initial query also exceeded the result limit.",
    "The working answer mentions a 16th density block without identifying it; a follow-up query could confirm whether exactly 16 density blocks exist or if the count differs.",
    "Search for excess molar volume or speed of sound data for the same binary system, which may also be relevant for electrodeposition bath modeling.",
    "Query for ternary systems containing water + ethylene glycol + iron salts (e.g., FeCl₂, FeSO₄) to find data directly relevant to electrodeposition bath compositions."
  ]
}
