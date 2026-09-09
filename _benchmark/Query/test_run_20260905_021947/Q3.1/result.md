# Q3.1 — Result

**Prompt:** I need three binary liquid systems for jointly testing density and viscosity predictions. Which systems have both properties measured for the same mixture, and which papers should I start with?

**Tool calls:** 1  |  **Time:** 514.5s  |  **Iterations:** 2  |  **Timed out:** False

---

## Answer

{
  "answer": "## Binary Liquid Systems with Co-Measured Density and Viscosity\n\nThe ThermoML database contains **8 binary liquid systems** across three publications where both mass density (kg/m³) and dynamic viscosity (Pa·s) were measured on the same mixture. Here is a summary, followed by a recommended starting set of three.\n\n---\n\n### Paper 1 — Alkanes + Squalane (high-pressure data)\n**DOI:** 10.1007/s10765-006-0053-2 (GLOBlit_25)\n\n| System | Density Block | Viscosity Block | T range (K) | P range (kPa) | x(squalane) range | n points |\n|--------|--------------|----------------|-------------|---------------|-------------------|----------|\n| Butane + squalane | PROPblock_10 | PROPblock_9 | 273.15–333.15 | 100.0–30000.0 | 0.0–0.753 | 80 each |\n| Hexane + squalane | PROPblock_12 | PROPblock_11 | 273.15–333.15 | 100.0–30000.0 | 0.0–0.743 | 64 each |\n| Octane + squalane | PROPblock_14 | PROPblock_13 | 273.15–333.15 | 100.0–30000.0 | 0.0–1.0 | 80 each |\n\nDensity ranges from 529.0 to 835.0 kg/m³ and viscosity spans 0.000118 to 0.2614 Pa·s across these three systems — nearly three orders of magnitude in viscosity, driven by squalane's high molecular weight (C₃₀H₆₂). Squalane is a widely used viscosity reference fluid, making these data especially valuable for equation-of-state and transport-property model benchmarking under pressure.\n\n---\n\n### Paper 2 — Chlorobutane Isomers + Diisopropyl Ether (atmospheric pressure)\n**DOI:** 10.1007/s10765-010-0737-5 (GLOBlit_97)\n\n| System | Density Block | Viscosity Block | T range (K) | P (kPa) | x(chlorobutane) range | n points |\n|--------|--------------|----------------|-------------|---------|----------------------|----------|\n| 1-Chlorobutane + diisopropyl ether | PROPblock_12 | PROPblock_11 | 283.15–313.15 | 101.0 | 0.0–1.0 | 91 each |\n| 2-Chlorobutane + diisopropyl ether | PROPblock_14 | PROPblock_13 | 283.15–313.15 | 101.0 | 0.0–1.0 | 90–91 |\n| 1-Chloro-2-methylpropane + diisopropyl ether | PROPblock_16 | PROPblock_15 | 283.15–313.15 | 101.0 | 0.0–1.0 | 91 each |\n| 2-Chloro-2-methylpropane + diisopropyl ether | PROPblock_18 | PROPblock_17 | 283.15–313.15 | 101.0 | 0.0–1.0 | 91 each |\n\nDensity spans 702.378–897.339 kg/m³; viscosity spans 0.000272–0.000598 Pa·s. The four C₄H₉Cl isomers (linear, secondary, isobutyl, and tert-butyl chloride) with a common ether partner provide a systematic probe of how branching and chlorine position affect both properties.\n\n---\n\n### Paper 3 — Butan-1-ol + TEGDME (atmospheric pressure, three properties)\n**DOI:** 10.1007/s10765-013-1469-0 (GLOBlit_151)\n\n| Property | Block | T range (K) | P (kPa) | x(butan-1-ol) range | n points |\n|----------|-------|-------------|---------|---------------------|----------|\n| Mass density | PROPblock_7 | 288.15–333.15 | 101.0 | 0.0–1.0 | 110 |\n| Dynamic viscosity | PROPblock_8 | 288.15–333.15 | 101.0 | 0.0–1.0 | 110 |\n| Refractive index | PROPblock_9 | 288.15–333.15 | 101.0 | 0.0–1.0 | 110 |\n\nDensity: 778.056–1015.63 kg/m³; viscosity: 0.001104–0.004341 Pa·s; refractive index: 1.38237–1.4345. The alcohol + polyether (tetraethylene glycol dimethyl ether) system features hydrogen-bonding interactions that produce strongly non-ideal mixing, making it a stringent test for predictive models. A bonus: refractive index is also available for multi-property validation.\n\n---\n\n### Recommended Starting Set of Three Systems\n\nFor maximum diversity in chemistry, conditions, and model-testing value, I recommend one system from each paper:\n\n1. **Octane + squalane** (from DOI 10.1007/s10765-006-0053-2, GLOBlit_25) — Non-polar hydrocarbon pair with high-pressure data (up to 30 000 kPa), full composition range (x = 0.0–1.0), and a very wide viscosity span (0.000351–0.2614 Pa·s). Ideal for testing pressure-dependent transport models.\n\n2. **1-Chlorobutane + diisopropyl ether** (from DOI 10.1007/s10765-010-0737-5, GLOBlit_97) — Weakly polar/dispersion-dominated system at atmospheric pressure with 91 data points across 13 compositions and 7 temperatures. The three companion isomer systems in the same paper allow immediate extension to a structural-isomer study.\n\n3. **Butan-1-ol + TEGDME** (from DOI 10.1007/s10765-013-1469-0, GLOBlit_151) — Hydrogen-bonding system at atmospheric pressure with 110 data points, 11 compositions, and 10 temperatures. The strong non-ideality challenges mixing rules, and the co-measured refractive index adds a third property for multi-objective model testing.\n\nTogether these three systems span non-polar, weakly polar, and strongly associating chemistries; atmospheric and high-pressure conditions; and viscosity values covering roughly three orders of magnitude.",
  "core_claims": [
    "The ThermoML database contains 8 binary liquid systems across three publications where both mass density (kg/m³) and dynamic viscosity (Pa·s) were co-measured on the same mixture.",
    "Paper 1 (DOI 10.1007/s10765-006-0053-2) reports density and viscosity for butane + squalane, hexane + squalane, and octane + squalane over 273.15–333.15 K and 100.0–30000.0 kPa, with viscosity spanning 0.000118 to 0.2614 Pa·s — nearly three orders of magnitude.",
    "Paper 2 (DOI 10.1007/s10765-010-0737-5) reports density and viscosity at 101.0 kPa for four chlorobutane isomers (1-chlorobutane, 2-chlorobutane, 1-chloro-2-methylpropane, 2-chloro-2-methylpropane) each mixed with diisopropyl ether, over 283.15–313.15 K and full composition range.",
    "Paper 3 (DOI 10.1007/s10765-013-1469-0) reports density, dynamic viscosity, and refractive index for butan-1-ol + tetraethylene glycol dimethyl ether at 101.0 kPa over 288.15–333.15 K and full composition range, with 110 data points per property.",
    "The recommended starting set of three systems for maximum diversity comprises octane + squalane (non-polar, high-pressure), 1-chlorobutane + diisopropyl ether (weakly polar, atmospheric), and butan-1-ol + TEGDME (hydrogen-bonding, atmospheric with co-measured refractive index), collectively spanning non-polar, weakly polar, and strongly associating chemistries and roughly three orders of magnitude in viscosity."
  ],
  "confidence": "medium",
  "sources": [
    {
      "doi": "10.1007/s10765-006-0053-2",
      "lit_num_id": "GLOBlit_25",
      "block": "PROPblock_9",
      "BLKsubsys_id": null,
      "description": "Provides viscosity data (0.000118–0.0915 Pa·s) for the butane + squalane binary system at high pressures up to 30000 kPa, paired with the density block PROPblock_10 for the same system."
    },
    {
      "doi": "10.1007/s10765-006-0053-2",
      "lit_num_id": "GLOBlit_25",
      "block": "PROPblock_10",
      "BLKsubsys_id": null,
      "description": "Provides mass density data (529.0–825.0 kg/m³) for the butane + squalane binary system, complementing the viscosity block PROPblock_9 for the same system."
    },
    {
      "doi": "10.1007/s10765-006-0053-2",
      "lit_num_id": "GLOBlit_25",
      "block": "PROPblock_11",
      "BLKsubsys_id": null,
      "description": "Provides viscosity data (0.000218–0.0971 Pa·s) for the hexane + squalane binary system at high pressures, paired with density block PROPblock_12."
    },
    {
      "doi": "10.1007/s10765-006-0053-2",
      "lit_num_id": "GLOBlit_25",
      "block": "PROPblock_12",
      "BLKsubsys_id": null,
      "description": "Provides mass density data (623.0–824.0 kg/m³) for the hexane + squalane binary system, complementing viscosity block PROPblock_11."
    },
    {
      "doi": "10.1007/s10765-006-0053-2",
      "lit_num_id": "GLOBlit_25",
      "block": "PROPblock_13",
      "BLKsubsys_id": null,
      "description": "Provides viscosity data (0.000351–0.2614 Pa·s) for the octane + squalane binary system over full composition range, one of the three recommended systems."
    },
    {
      "doi": "10.1007/s10765-006-0053-2",
      "lit_num_id": "GLOBlit_25",
      "block": "PROPblock_14",
      "BLKsubsys_id": null,
      "description": "Provides mass density data (670.0–835.0 kg/m³) for the octane + squalane binary system, complementing viscosity block PROPblock_13 for the recommended system."
    },
    {
      "doi": "10.1007/s10765-010-0737-5",
      "lit_num_id": "GLOBlit_97",
      "block": "PROPblock_11",
      "BLKsubsys_id": null,
      "description": "Provides viscosity data (0.000272–0.000499 Pa·s) for 1-chlorobutane + diisopropyl ether at atmospheric pressure, one of the recommended systems."
    },
    {
      "doi": "10.1007/s10765-010-0737-5",
      "lit_num_id": "GLOBlit_97",
      "block": "PROPblock_12",
      "BLKsubsys_id": null,
      "description": "Provides mass density data (702.378–897.339 kg/m³) for 1-chlorobutane + diisopropyl ether, complementing viscosity block PROPblock_11."
    },
    {
      "doi": "10.1007/s10765-010-0737-5",
      "lit_num_id": "GLOBlit_97",
      "block": "PROPblock_13",
      "BLKsubsys_id": null,
      "description": "Provides viscosity data (0.000272–0.000463 Pa·s) for 2-chlorobutane + diisopropyl ether, part of the chlorobutane isomer series discussed in the answer."
    },
    {
      "doi": "10.1007/s10765-010-0737-5",
      "lit_num_id": "GLOBlit_97",
      "block": "PROPblock_14",
      "BLKsubsys_id": null,
      "description": "Provides mass density data (702.378–884.34 kg/m³) for 2-chlorobutane + diisopropyl ether, complementing viscosity block PROPblock_13."
    },
    {
      "doi": "10.1007/s10765-010-0737-5",
      "lit_num_id": "GLOBlit_97",
      "block": "PROPblock_15",
      "BLKsubsys_id": null,
      "description": "Provides viscosity data (0.000272–0.000516 Pa·s) for 1-chloro-2-methylpropane + diisopropyl ether, part of the chlorobutane isomer series."
    },
    {
      "doi": "10.1007/s10765-010-0737-5",
      "lit_num_id": "GLOBlit_97",
      "block": "PROPblock_16",
      "BLKsubsys_id": null,
      "description": "Provides mass density data (702.378–888.845 kg/m³) for 1-chloro-2-methylpropane + diisopropyl ether, complementing viscosity block PROPblock_15."
    },
    {
      "doi": "10.1007/s10765-010-0737-5",
      "lit_num_id": "GLOBlit_97",
      "block": "PROPblock_17",
      "BLKsubsys_id": null,
      "description": "Provides viscosity data (0.000272–0.000598 Pa·s) for 2-chloro-2-methylpropane + diisopropyl ether, completing the four-isomer series."
    },
    {
      "doi": "10.1007/s10765-010-0737-5",
      "lit_num_id": "GLOBlit_97",
      "block": "PROPblock_18",
      "BLKsubsys_id": null,
      "description": "Provides mass density data (702.378–855.249 kg/m³) for 2-chloro-2-methylpropane + diisopropyl ether, complementing viscosity block PROPblock_17."
    },
    {
      "doi": "10.1007/s10765-013-1469-0",
      "lit_num_id": "GLOBlit_151",
      "block": "PROPblock_7",
      "BLKsubsys_id": null,
      "description": "Provides mass density data (778.056–1015.63 kg/m³) for butan-1-ol + TEGDME, one of the three recommended systems."
    },
    {
      "doi": "10.1007/s10765-013-1469-0",
      "lit_num_id": "GLOBlit_151",
      "block": "PROPblock_8",
      "BLKsubsys_id": null,
      "description": "Provides viscosity data (0.001104–0.004341 Pa·s) for butan-1-ol + TEGDME, complementing density block PROPblock_7 for the recommended hydrogen-bonding system."
    },
    {
      "doi": "10.1007/s10765-013-1469-0",
      "lit_num_id": "GLOBlit_151",
      "block": "PROPblock_9",
      "BLKsubsys_id": null,
      "description": "Provides refractive index data (1.38237–1.4345) for butan-1-ol + TEGDME, mentioned in the answer as a bonus third co-measured property for multi-property validation."
    }
  ],
  "follow_up_suggestions": [
    "Compare excess molar volume and viscosity deviation from ideal mixing for the three recommended systems to quantify non-ideality strength.",
    "Extend the isomer study from GLOBlit_97 by testing all four chlorobutane + diisopropyl ether systems simultaneously against a group-contribution model.",
    "Use the high-pressure squalane data (GLOBlit_25) to benchmark free-volume or friction-theory viscosity models that couple to cubic or SAFT equations of state.",
    "Leverage the co-measured refractive index in GLOBlit_151 (butan-1-ol + TEGDME) for a multi-property objective function in parameter estimation."
  ],
  "id_catalog_snapshot": [
    {
      "type": "comp",
      "global_id": "GLOBcomp_102",
      "registry_id": "butane",
      "name": "butane"
    },
    {
      "type": "comp",
      "global_id": "GLOBcomp_284",
      "registry_id": "2,6,10,15,19,23-hexamethyltetracosane",
      "name": "2,6,10,15,19,23-hexamethyltetracosane"
    },
    {
      "type": "comp",
      "global_id": "GLOBcomp_12",
      "registry_id": "hexane",
      "name": "hexane"
    },
    {
      "type": "comp",
      "global_id": "GLOBcomp_17",
      "registry_id": "octane",
      "name": "octane"
    },
    {
      "type": "comp",
      "global_id": "GLOBcomp_131",
      "registry_id": "1-chlorobutane",
      "name": "1-chlorobutane"
    },
    {
      "type": "comp",
      "global_id": "GLOBcomp_52",
      "registry_id": "diisopropyl_ether",
      "name": "diisopropyl ether"
    },
    {
      "type": "comp",
      "global_id": "GLOBcomp_307",
      "registry_id": "2-chlorobutane",
      "name": "2-chlorobutane"
    },
    {
      "type": "comp",
      "global_id": "GLOBcomp_361",
      "registry_id": "1-chloro-2-methylpropane",
      "name": "1-chloro-2-methylpropane"
    },
    {
      "type": "comp",
      "global_id": "GLOBcomp_328",
      "registry_id": "2-chloro-2-methylpropane",
      "name": "2-chloro-2-methylpropane"
    },
    {
      "type": "comp",
      "global_id": "GLOBcomp_7",
      "registry_id": "butan-1-ol",
      "name": "butan-1-ol"
    },
    {
      "type": "comp",
      "global_id": "GLOBcomp_247",
      "registry_id": "2,5,8,11,14-pentaoxapentadecane",
      "name": "2,5,8,11,14-pentaoxapentadecane"
    },
    {
      "type": "prop",
      "global_id": "GLOBprop_1",
      "registry_id": "mass_density_kg_m3",
      "name": "Mass density, kg/m3"
    },
    {
      "type": "prop",
      "global_id": "GLOBprop_4",
      "registry_id": "viscosity_pa_s",
      "name": "Viscosity, Pa*s"
    },
    {
      "type": "prop",
      "global_id": "GLOBprop_7",
      "registry_id": "refractive_index_na_dline",
      "name": "Refractive index (Na D-line)"
    },
    {
      "type": "lit",
      "global_id": "GLOBlit_25",
      "registry_id": "2006-kum-tom-0",
      "name": "10.1007/s10765-006-0053-2"
    },
    {
      "type": "lit",
      "global_id": "GLOBlit_97",
      "registry_id": "2010-mon-gue-0",
      "name": "10.1007/s10765-010-0737-5"
    },
    {
      "type": "lit",
      "global_id": "GLOBlit_151",
      "registry_id": "2013-ziv-ser-0",
      "name": "10.1007/s10765-013-1469-0"
    }
  ]
}
