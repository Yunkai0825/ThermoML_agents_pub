# Q5.2 — Result

**Prompt:** What data is available for glycol + water mixtures?

**Tool calls:** 1  |  **Time:** 265.1s  |  **Iterations:** 2  |  **Timed out:** False

---

## Answer

{
  "answer": "## Glycol + Water Binary Mixture Data in the ThermoML Database\n\nThe ThermoML database contains extensive thermodynamic and transport property data for **four glycol + water binary systems**, totaling **161 property blocks** across **81 literature sources** (some shared across systems) with **10,081 data points**. These glycol–water mixtures are of major industrial importance as antifreeze formulations, heat-transfer fluids, and gas-dehydration agents.\n\n---\n\n### Cross-System Summary\n\n| Glycol + Water System | Blocks | Papers | Data Points | T range (K) | P range (kPa) |\n|---|---|---|---|---|---|\n| Ethylene glycol (1,2-ethanediol) | 59 | 32 | 2,584 | 258.32 – 573.23 | 50.0 – 350,200.0 |\n| Propylene glycol (1,2-propanediol) | 34 | 18 | 1,780 | 253.15 – 573.19 | 100.0 – 350,000.0 |\n| Diethylene glycol | 28 | 15 | 2,079 | 278.15 – 573.184 | 50.0 – 30,500.0 |\n| Triethylene glycol | 40 | 16 | 3,638 | 278.15 – 573.183 | 50.0 – 30,510.0 |\n| **Total** | **161** | **81*** | **10,081** | — | — |\n\n\\*Some papers cover multiple glycol systems, so the unique paper count is lower.\n\n---\n\n### 1. Ethylene Glycol (1,2-Ethanediol) + Water\n\nThe most widely studied system, with **59 blocks from 32 papers** and **2,584 data points**, spanning 258.32–573.23 K and up to 350,200 kPa (~350 MPa).\n\n**Properties measured (by number of blocks):**\n\n| Property | Blocks |\n|---|---|\n| Mass density (kg/m³) | 16 |\n| Speed of sound (m/s) | 8 |\n| Viscosity (Pa·s) | 7 |\n| Binary diffusion coefficient (m²/s) | 5 |\n| Surface tension liquid–gas (N/m) | 4 |\n| Vapor or sublimation pressure (kPa) | 3 |\n| Boiling temperature at pressure P (K) | 3 |\n| Mole fraction | 2 |\n| Refractive index (Na D-line) | 2 |\n| Specific volume (m³/kg) | 2 |\n\n**Top literature sources:**\n\n| DOI | Blocks | Points |\n|---|---|---|\n| 10.1016/j.jct.2018.02.022 | 3 | 456 |\n| 10.1021/je4001203 | 2 | 276 |\n| 10.1021/je020140j | 3 | 249 |\n| 10.1021/acs.jced.6b00526 | 3 | 236 |\n| 10.1016/j.fluid.2013.06.041 | 2 | 214 |\n\n---\n\n### 2. Propylene Glycol (1,2-Propanediol) + Water\n\n**34 blocks from 18 papers**, **1,780 data points**, spanning 253.15–573.19 K and up to 350,000 kPa (~350 MPa).\n\n**Properties measured (by number of blocks):**\n\n| Property | Blocks |\n|---|---|\n| Mass density (kg/m³) | 10 |\n| Speed of sound (m/s) | 4 |\n| Viscosity (Pa·s) | 4 |\n| Excess molar volume (m³/mol) | 2 |\n| Molar heat capacity at constant pressure (J/K/mol) | 2 |\n| Thermal conductivity (W/m/K) | 2 |\n| Specific volume (m³/kg) | 2 |\n| Excess molar heat capacity (J/K/mol) | 1 |\n| Surface tension liquid–gas (N/m) | 1 |\n| Excess molar enthalpy of mixing (kJ/mol) | 1 |\n\n**Top literature sources:**\n\n| DOI | Blocks | Points |\n|---|---|---|\n| 10.1021/je0340755 | 3 | 375 |\n| 10.1021/acs.jced.8b00403 | 3 | 291 |\n| 10.1021/je201184b | 2 | 212 |\n| 10.1016/j.fluid.2013.06.041 | 2 | 185 |\n| 10.1016/j.fluid.2014.12.040 | 2 | 168 |\n\n---\n\n### 3. Diethylene Glycol + Water\n\n**28 blocks from 15 papers**, **2,079 data points**, spanning 278.15–573.184 K and up to 30,500 kPa.\n\n**Properties measured (by number of blocks):**\n\n| Property | Blocks |\n|---|---|\n| Mass density (kg/m³) | 10 |\n| Speed of sound (m/s) | 6 |\n| Viscosity (Pa·s) | 4 |\n| Binary diffusion coefficient (m²/s) | 2 |\n| Excess molar enthalpy of mixing (kJ/mol) | 2 |\n| Molar heat capacity at constant pressure (J/K/mol) | 1 |\n| Boiling temperature at pressure P (K) | 1 |\n| Refractive index (Na D-line) | 1 |\n| Thermal conductivity (W/m/K) | 1 |\n\n**Top literature sources:**\n\n| DOI | Blocks | Points |\n|---|---|---|\n| 10.1016/j.jct.2016.07.016 | 1 | 588 |\n| 10.1016/j.jct.2018.02.022 | 3 | 456 |\n| 10.1021/je700672f | 2 | 286 |\n| 10.1021/je1009976 | 2 | 170 |\n| 10.1021/acs.jced.5b00498 | 2 | 140 |\n\n---\n\n### 4. Triethylene Glycol + Water\n\nThe **largest dataset** with **40 blocks from 16 papers** and **3,638 data points**, spanning 278.15–573.183 K and up to 30,510 kPa.\n\n**Properties measured (by number of blocks):**\n\n| Property | Blocks |\n|---|---|\n| Mass density (kg/m³) | 10 |\n| Refractive index (other wavelength) | 9 |\n| Speed of sound (m/s) | 6 |\n| Boiling temperature at pressure P (K) | 3 |\n| Viscosity (Pa·s) | 3 |\n| Binary diffusion coefficient (m²/s) | 2 |\n| Mole fraction | 2 |\n| Joule-Thomson coefficient (K/kPa) | 1 |\n| Molar heat capacity at constant pressure (J/K/mol) | 1 |\n| Excess molar enthalpy of mixing (kJ/mol) | 1 |\n\n**Top literature sources:**\n\n| DOI | Blocks | Points |\n|---|---|---|\n| 10.1016/j.fluid.2015.07.030 | 12 | 1,370 |\n| 10.1016/j.jct.2015.05.024 | 2 | 667 |\n| 10.1016/j.jct.2016.07.016 | 1 | 598 |\n| 10.1016/j.jct.2018.02.022 | 3 | 432 |\n| 10.1021/acs.jced.5b00498 | 2 | 140 |\n\n---\n\n### Key Observations & Chemical Context\n\n- **Mass density** is the most commonly measured property across all four systems (46 blocks total), reflecting its central importance for engineering design of glycol–water heat-transfer fluids and antifreeze formulations.\n- **Speed of sound** and **dynamic viscosity** are the next most common, each appearing in all four systems — critical for acoustic and flow characterization.\n- **Ethylene glycol + water** has the broadest literature coverage (32 papers), consistent with its dominant industrial role as an automotive antifreeze and coolant.\n- **Triethylene glycol + water** has the largest single dataset (3,638 points), driven largely by one comprehensive study (DOI: 10.1016/j.fluid.2015.07.030) contributing 1,370 points across 12 blocks — reflecting triethylene glycol's importance in natural gas dehydration.\n- **Ethylene glycol** and **propylene glycol** systems extend to much higher pressures (up to ~350 MPa), likely from high-pressure density studies relevant to deep-well and high-pressure process conditions.\n- All four systems reach similar upper temperatures (~573 K), covering conditions relevant to both ambient and elevated-temperature industrial processes.\n- **Transport properties** (diffusion coefficients, thermal conductivity) and **excess thermodynamic properties** (excess molar enthalpy, excess molar volume) are available but less common than volumetric and acoustic properties.\n- Several literature sources span multiple glycol systems (e.g., DOI: 10.1016/j.jct.2018.02.022 covers ethylene glycol, diethylene glycol, and triethylene glycol with water), enabling direct cross-system comparisons under identical experimental conditions.",
  "core_claims": [
    "The ThermoML database contains thermodynamic and transport property data for four glycol + water binary systems (ethylene glycol, propylene glycol, diethylene glycol, and triethylene glycol), totaling 161 property blocks across 81 literature sources with 10,081 data points.",
    "Ethylene glycol + water is the most widely studied system by literature coverage (59 blocks from 32 papers, 2,584 data points), spanning 258.32–573.23 K and up to 350,200.0 kPa.",
    "Triethylene glycol + water has the largest single dataset (40 blocks from 16 papers, 3,638 data points), driven largely by one study (DOI: 10.1016/j.fluid.2015.07.030) contributing 1,370 points across 12 blocks.",
    "Mass density is the most commonly measured property across all four systems (46 blocks total), followed by speed of sound and dynamic viscosity, which appear in all four systems.",
    "Ethylene glycol and propylene glycol systems extend to much higher pressures (up to ~350 MPa) compared to diethylene glycol (up to 30,500.0 kPa) and triethylene glycol (up to 30,510.0 kPa).",
    "All four systems reach similar upper temperatures (~573 K), covering conditions relevant to both ambient and elevated-temperature industrial processes.",
    "Transport properties (diffusion coefficients, thermal conductivity) and excess thermodynamic properties (excess molar enthalpy, excess molar volume) are available but less common than volumetric and acoustic properties."
  ],
  "confidence": "medium",
  "sources": [],
  "follow_up_suggestions": [
    "Retrieve detailed property data for a specific glycol + water system, e.g., 'Show all mass density data for ethylene glycol + water mixtures'",
    "Compare viscosity data across all four glycol + water systems at a specific temperature range",
    "Look up excess thermodynamic properties (excess molar enthalpy, excess molar volume) for propylene glycol + water",
    "Investigate high-pressure density data for ethylene glycol + water up to 350 MPa",
    "Search for glycol + water ternary systems (e.g., ethylene glycol + propylene glycol + water)",
    "Find vapor-liquid equilibrium data for triethylene glycol + water relevant to natural gas dehydration"
  ],
  "id_catalog_snapshot": [
    {
      "type": "comp",
      "global_id": "GLOBcomp_24",
      "registry_id": "1,2-ethanediol",
      "name": "1,2-ethanediol"
    },
    {
      "type": "comp",
      "global_id": "GLOBcomp_1",
      "registry_id": "water",
      "name": "water"
    },
    {
      "type": "comp",
      "global_id": "GLOBcomp_61",
      "registry_id": "1,2-propanediol",
      "name": "1,2-propanediol"
    },
    {
      "type": "comp",
      "global_id": "GLOBcomp_111",
      "registry_id": "diethylene_glycol",
      "name": "diethylene glycol"
    },
    {
      "type": "comp",
      "global_id": "GLOBcomp_113",
      "registry_id": "triethylene_glycol",
      "name": "triethylene glycol"
    },
    {
      "type": "lit",
      "global_id": "GLOBlit_5201",
      "registry_id": "2018-hog-tor-0",
      "name": "10.1016/j.jct.2018.02.022"
    },
    {
      "type": "lit",
      "global_id": "GLOBlit_10102",
      "registry_id": "2013-hne-cib-1",
      "name": "10.1021/je4001203"
    },
    {
      "type": "lit",
      "global_id": "GLOBlit_8038",
      "registry_id": "2003-yan-ma-2",
      "name": "10.1021/je020140j"
    },
    {
      "type": "lit",
      "global_id": "GLOBlit_6951",
      "registry_id": "2017-moo-ros-0",
      "name": "10.1021/acs.jced.6b00526"
    },
    {
      "type": "lit",
      "global_id": "GLOBlit_1283",
      "registry_id": "2013-zem-tro-0",
      "name": "10.1016/j.fluid.2013.06.041"
    },
    {
      "type": "lit",
      "global_id": "GLOBlit_8239",
      "registry_id": "2003-geo-sas-1",
      "name": "10.1021/je0340755"
    },
    {
      "type": "lit",
      "global_id": "GLOBlit_7545",
      "registry_id": "2018-mik-sko-0",
      "name": "10.1021/acs.jced.8b00403"
    },
    {
      "type": "lit",
      "global_id": "GLOBlit_9758",
      "registry_id": "2012-kat-hne-0",
      "name": "10.1021/je201184b"
    },
    {
      "type": "lit",
      "global_id": "GLOBlit_1623",
      "registry_id": "2015-cha-hsi-0",
      "name": "10.1016/j.fluid.2014.12.040"
    },
    {
      "type": "lit",
      "global_id": "GLOBlit_4754",
      "registry_id": "2017-cib--1",
      "name": "10.1016/j.jct.2016.07.016"
    },
    {
      "type": "lit",
      "global_id": "GLOBlit_11031",
      "registry_id": "2008-man-guz-0",
      "name": "10.1021/je700672f"
    },
    {
      "type": "lit",
      "global_id": "GLOBlit_9382",
      "registry_id": "2011-beg-cla-0",
      "name": "10.1021/je1009976"
    },
    {
      "type": "lit",
      "global_id": "GLOBlit_6630",
      "registry_id": "2016-cib--0",
      "name": "10.1021/acs.jced.5b00498"
    },
    {
      "type": "lit",
      "global_id": "GLOBlit_1753",
      "registry_id": "2015-ani-sin-0",
      "name": "10.1016/j.fluid.2015.07.030"
    },
    {
      "type": "lit",
      "global_id": "GLOBlit_4395",
      "registry_id": "2015-kli-str-1",
      "name": "10.1016/j.jct.2015.05.024"
    }
  ]
}
