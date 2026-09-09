# Q3.3 — Result

**Prompt:** For aqueous propan-2-ol, which study provides the most complete experimental characterization? What properties were measured, which methods were used, and what purities were reported for the compounds?

**Tool calls:** 3  |  **Time:** 1000.2s  |  **Iterations:** 4  |  **Timed out:** False

---

## Answer

{
  "answer": "## Most Complete Experimental Characterization of Aqueous Propan-2-ol in ThermoML\n\nBased on a search of the ThermoML database covering **71 declared binary data blocks across 38 distinct DOIs** for the water + propan-2-ol system, two studies stand out as the most comprehensive, depending on the criterion used:\n\n---\n\n### 1. Most Property-Diverse Study: GLOBlit_1423 (DOI: 10.1016/j.fluid.2014.02.006)\n\nThis study reports **four distinct VLE-related properties** across 4 data blocks and 36 data points:\n\n| Property | Description |\n|----------|-------------|\n| Boiling temperature | Bubble-point temperature at specified pressure |\n| Equilibrium mole fraction | Liquid–vapor equilibrium composition |\n| Azeotropic temperature | Temperature of the azeotrope |\n| Azeotropic composition | Composition at the azeotropic point |\n\nThis is the most property-diverse single study for this binary system in the database.\n\n---\n\n### 2. Most Data-Rich Study: GLOBlit_1311 (DOI: 10.1016/j.fluid.2013.08.007)\n\nThis study provides the largest dataset with **1,248 data points** across 2 data blocks:\n\n| Property | Data Points |\n|----------|-------------|\n| Mass density | 1,110 |\n| Molar heat capacity (Cp) | 138 |\n\nThis extensive coverage of thermophysical properties (density and heat capacity) across multiple temperatures and compositions makes it the most data-rich single study.\n\n---\n\n### Other Notable Studies\n\n| GLOBlit ID | DOI | Property | Points |\n|------------|-----|----------|--------|\n| GLOBlit_2096 | 10.1016/j.fluid.2017.09.010 | Boiling temperature, Mole fraction, Azeotropic composition | 37 |\n| GLOBlit_2432 | 10.1016/j.jct.2004.07.019 | Mass density | 529 |\n| GLOBlit_11130 | 10.1021/je8001305 | Mass density (compressed liquid) | 209 |\n| GLOBlit_1910 | 10.1016/j.fluid.2016.04.007 | Surface tension | 60 |\n| GLOBlit_2892 | 10.1016/j.jct.2007.12.002 | Excess molar enthalpy | 45 |\n\n---\n\n### Measurement Methods and Purities\n\nUnfortunately, detailed metadata on **measurement methods** (e.g., vibrating-tube densimetry, differential scanning calorimetry, ebulliometry) and **compound purities** for these specific studies could not be retrieved within the available query window. The ThermoML database does encode such metadata in its XML records, but the current search was limited to property-level and block-level summaries.\n\n### Chemistry Context\n\nWater + propan-2-ol (isopropanol) is a well-studied system because it forms a **minimum-boiling azeotrope** near 80.4 °C at atmospheric pressure (≈ 0.68 mole fraction isopropanol), which is industrially important for separation processes. The breadth of properties measured — from VLE and azeotropic data to density, heat capacity, surface tension, excess enthalpy, viscosity, speed of sound, refractive index, and electrical conductivity — reflects the system's relevance to chemical engineering design and thermodynamic modeling. The 38 studies and ~2,893 data points in ThermoML provide a rich experimental foundation for validating equations of state and activity coefficient models for this system.",
  "core_claims": [
    "Across 71 declared binary data blocks and 38 distinct DOIs in ThermoML for the water + propan-2-ol system, the most property-diverse single study is DOI 10.1016/j.fluid.2014.02.006, reporting four distinct VLE-related properties (boiling temperature, equilibrium mole fraction, azeotropic temperature, and azeotropic composition) across 4 data blocks and 36 data points.",
    "The most data-rich single study is DOI 10.1016/j.fluid.2013.08.007, providing 1,248 data points across 2 data blocks covering mass density (1,110 points) and molar heat capacity (138 points).",
    "The total ThermoML coverage for this binary system comprises approximately 2,893 data points spanning properties including VLE, density, heat capacity, surface tension, excess molar enthalpy, viscosity, speed of sound, refractive index, and electrical conductivity.",
    "Detailed metadata on measurement methods and compound purities for these studies could not be retrieved within the available query window."
  ],
  "confidence": "medium",
  "sources": [],
  "follow_up_suggestions": [
    "Retrieve detailed measurement methods (e.g., vibrating-tube densimetry, DSC, ebulliometry) for GLOBlit_1311 and GLOBlit_1423 from the full ThermoML XML records.",
    "Query compound purity metadata for water and propan-2-ol as reported in GLOBlit_1311 (10.1016/j.fluid.2013.08.007) and GLOBlit_1423 (10.1016/j.fluid.2014.02.006).",
    "Compare the azeotropic temperature and composition values reported in GLOBlit_1423 and GLOBlit_2096 to assess inter-study consistency.",
    "Investigate whether any ThermoML studies for aqueous propan-2-ol report activity coefficients or excess Gibbs energy data that could complement the VLE measurements."
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
      "global_id": "GLOBcomp_6",
      "registry_id": "propan-2-ol",
      "name": "propan-2-ol"
    }
  ]
}
