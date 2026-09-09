# Delegated query run — result

**Question:** Find all ThermoML data blocks for binary mixtures of water + propylene glycol (1,2-propanediol) that contain viscosity, relative permittivity (dielectric constant), or density measurements. Report DOIs, block numbers, properties measured, temperature ranges, and composition ranges.

**Iterations:** 4  |  **Elapsed:** 981.4s  |  **Tools:** 5  |  **Timed out:** False

---

## Answer

{
  "answer": "# ThermoML Data for Binary Water + Propylene Glycol (1,2-Propanediol) Mixtures\n\n## System Overview\n\nThe ThermoML database contains **34 binary data blocks** for the water (H₂O) + 1,2-propanediol (propylene glycol, C₃H₈O₂) system. Among these, **15 blocks** report viscosity, density, or relative permittivity (dielectric constant) measurements — the three properties most relevant to iron electrodeposition bath design.\n\n---\n\n## Dynamic Viscosity — 4 Blocks (264 total data points)\n\n| Block | Literature | DOI | Points | T range (K) | Composition range | P (kPa) | Method |\n|-------|-----------|-----|--------|-------------|-------------------|---------|--------|\n| PROPblock_4 | GLOBlit_5233 | 10.1016/j.jct.2018.04.007 | 4 | 293–323 | w(PG) = 0.3 (fixed) | 96.2 | Cone & plate |\n| PROPblock_14 | GLOBlit_7545 | 10.1021/acs.jced.8b00403 | 105 | 253–353 | w(PG) = 0–1 (full range) | 101.325 | Concentric cylinders |\n| PROPblock_28 | GLOBlit_8239 | 10.1021/je0340755 | 125 | 298–338 | x(H₂O) = 0.044–0.995 | 101.3 | Capillary/Ubbelohde |\n| PROPblock_11 | GLOBlit_8556 | 10.1021/je049960h | 30 | 297–450 | x(PG) = 0.25–0.75 | 101.3 | Capillary/Ubbelohde |\n\n**Key values:** Viscosity ranges from 0.000344 Pa·s (dilute PG, high T) to 1.77 Pa·s (pure PG, low T). The most comprehensive dataset (GLOBlit_7545, PROPblock_14) covers the full mass-fraction range at 13 temperatures. The widest temperature range (up to ~450 K) is from GLOBlit_8556 but is limited to intermediate compositions.\n\n---\n\n## Relative Permittivity (Dielectric Constant) — 1 Block (28 data points)\n\n| Block | Literature | DOI | Points | T (K) | Composition range | P range (kPa) | Method |\n|-------|-----------|-----|--------|-------|-------------------|---------------|--------|\n| PROPblock_1 | GLOBlit_8686 | 10.1021/je050237g | 28 | 298.15 (fixed) | x(PG) = 0.2–0.8 | 100–300,000 | Transformer ratio-arm bridge |\n\n**Key values:** Relative permittivity ranges from 32.25 to 63.61 across the composition and pressure range. This is notably a **high-pressure dielectric study** (0.1–300 MPa) at a single temperature, covering intermediate mole fractions where the largest deviations from ideal mixing are expected. No ambient-pressure temperature-sweep permittivity data were found for this binary system.\n\n---\n\n## Mass Density — 10 Blocks\n\n| # | Block | Literature | DOI | Points | T range (K) | Composition range | P (kPa) | Method |\n|---|-------|-----------|-----|--------|-------------|-------------------|---------|--------|\n| 1 | PROPblock_9 | GLOBlit_1623 | 10.1016/j.fluid.2014.12.040 | 84 | 298–328 | x(PG) = 0–1 (full) | 100.0 | Vibrating tube |\n| 2 | PROPblock_12 | GLOBlit_2831 | 10.1016/j.jct.2007.05.010 | 8 | 298.15 (fixed) | m(H₂O) = 0–1.02 mol/kg | 101.0 | Vibrating tube variant |\n| 3 | PROPblock_6 | GLOBlit_2979 | 10.1016/j.jct.2008.07.005 | 96 | 283–308 | x(PG) = 0–0.2 (dilute) | 98.93 | Pycnometry variant |\n| 4 | PROPblock_5 | GLOBlit_3180 | 10.1016/j.jct.2009.11.018 | 14 | 298.15 (fixed) | x(PG) = 0.073–0.936 | 101.0 | Pycnometry |\n| 5 | PROPblock_1 | GLOBlit_5233 | 10.1016/j.jct.2018.04.007 | 4 | 293–323 | w(PG) = 0.3 (fixed) | 96.2 | Pycnometry |\n| 6 | PROPblock_2 | GLOBlit_9758 | 10.1021/je201184b | 106 | 278–318 | m(PG) = 0.1–0.6 mol/kg | 101.0 | Vibrating tube |\n| 7–10 | — | — | — | — | — | — | — | Details truncated in search |\n\n**Key values:** Density spans approximately 985–1044 kg/m³ across all compositions and temperatures. Pure 1,2-propanediol is slightly denser than water at 298 K (~1036 vs. ~997 kg/m³). The most comprehensive block (GLOBlit_1623, PROPblock_9) covers the full mole-fraction range (0–1) across four temperatures with 84 vibrating-tube densimetry points. Note: Block PROPblock_2 (GLOBlit_9758) reports values of 0.46–3.46, suggesting it contains density differences (Δρ) or apparent molar quantities rather than absolute mass density.\n\n---\n\n## Relevance to Iron Electrodeposition Bath Design\n\nThese data are directly useful for designing water + propylene glycol co-solvent baths for Fe electrodeposition:\n\n- **Viscosity** controls mass transport of Fe²⁺/Fe³⁺ ions to the cathode. The viscosity increases dramatically with PG content — from ~0.89 mPa·s (pure water) to ~56 mPa·s (pure PG) at 25 °C — so bath compositions above ~50 wt% PG will significantly reduce limiting current density.\n\n- **Dielectric constant** governs ionic dissociation of iron salts and double-layer structure. The permittivity drops from ~78 (water) toward ~32 (pure PG), meaning higher PG fractions will reduce salt solubility and ion-pair dissociation. The available high-pressure data (DOI: 10.1021/je050237g, GLOBlit_8686) shows permittivity values of 32–64 at intermediate compositions, but ambient-pressure temperature-dependent data are not available in ThermoML for this system.\n\n- **Density** data support accurate solution preparation (gravimetric/volumetric conversion) and computational fluid dynamics modeling of the electrochemical cell.\n\n## Additional Properties Available\n\nBeyond the three target properties, ThermoML also contains data for this binary system on: excess molar volume, speed of sound, surface tension, heat capacity, thermal conductivity, refractive index, partial molar volume, excess enthalpy, vapor pressure, specific volume, and solid–liquid equilibrium temperature — all potentially useful for comprehensive bath characterization.",
  "core_claims": [
    "The ThermoML database contains 34 binary data blocks for the water + 1,2-propanediol (propylene glycol) system, of which 15 blocks report viscosity, density, or relative permittivity measurements relevant to iron electrodeposition bath design.",
    "Dynamic viscosity data (4 blocks, 264 points) span temperatures from 253 to 450 K and the full mass-fraction range, with values ranging from 0.000344 Pa·s (dilute PG, high T) to 1.77 Pa·s (pure PG, low T); viscosity increases dramatically with PG content, rising from ~0.89 mPa·s (pure water) to ~56 mPa·s (pure PG) at 25 °C.",
    "Relative permittivity data (1 block, 28 points) are available only at 298.15 K over a high-pressure range (0.1–300 MPa) for intermediate mole fractions (x(PG) = 0.2–0.8), with values of 32.25–63.61; no ambient-pressure temperature-sweep permittivity data were found for this binary system in ThermoML.",
    "Mass density data (10 blocks) span approximately 985–1044 kg/m³ across all compositions and temperatures, with the most comprehensive block covering the full mole-fraction range at four temperatures using vibrating-tube densimetry; one block likely reports density differences or apparent molar quantities rather than absolute mass density.",
    "Higher propylene glycol fractions reduce the dielectric constant from ~78 (water) toward ~32 (pure PG), which would decrease iron salt solubility and ion-pair dissociation, while the accompanying viscosity increase would significantly reduce limiting current density above ~50 wt% PG.",
    "Additional properties available in ThermoML for this system include excess molar volume, speed of sound, surface tension, heat capacity, thermal conductivity, refractive index, partial molar volume, excess enthalpy, vapor pressure, specific volume, and solid–liquid equilibrium temperature."
  ],
  "confidence": "medium",
  "sources": [
    {
      "doi": "10.1016/j.fluid.2014.12.040",
      "lit_num_id": "GLOBlit_1623",
      "block": "PROPblock_9",
      "BLKsubsys_id": null,
      "description": "Mass density (GLOBprop_1) for binary water + 1,2-propanediol. 84 data points, T 298.15–328.15 K, x(PG) 0–1, P = 100.0 kPa, vibrating tube method."
    },
    {
      "doi": "10.1021/je050237g",
      "lit_num_id": "GLOBlit_8686",
      "block": "PROPblock_1",
      "BLKsubsys_id": null,
      "description": "Relative permittivity at zero frequency (GLOBprop_44) for binary water + 1,2-propanediol. 28 data points, T = 298.15 K (fixed), P 100–300000 kPa, x(PG) 0.2–0.8, transformer ratio-arm bridge method."
    },
    {
      "doi": "10.1016/j.jct.2018.04.007",
      "lit_num_id": "GLOBlit_5233",
      "block": "PROPblock_4",
      "BLKsubsys_id": null,
      "description": "Dynamic viscosity (GLOBprop_4) for binary water + 1,2-propanediol. 4 data points, T 293–323 K, w(PG) = 0.3 (fixed), P = 96.2 kPa."
    },
    {
      "doi": "10.1016/j.jct.2018.04.007",
      "lit_num_id": "GLOBlit_5233",
      "block": "PROPblock_1",
      "BLKsubsys_id": null,
      "description": "Mass density (GLOBprop_1) for binary water + 1,2-propanediol. 4 data points, T 293–323 K, w(PG) = 0.3 (fixed), P = 96.2 kPa."
    },
    {
      "doi": "10.1021/acs.jced.8b00403",
      "lit_num_id": "GLOBlit_7545",
      "block": "PROPblock_14",
      "BLKsubsys_id": null,
      "description": "Dynamic viscosity (GLOBprop_4) for binary water + 1,2-propanediol. 105 data points, T 253–353 K, w(PG) = 0–1 (full range), P = 101.325 kPa."
    },
    {
      "doi": "10.1021/je0340755",
      "lit_num_id": "GLOBlit_8239",
      "block": "PROPblock_28",
      "BLKsubsys_id": null,
      "description": "Dynamic viscosity (GLOBprop_4) for binary water + 1,2-propanediol. 125 data points, T 298–338 K, x(H2O) = 0.044–0.995, P = 101.3 kPa."
    },
    {
      "doi": "10.1021/je049960h",
      "lit_num_id": "GLOBlit_8556",
      "block": "PROPblock_11",
      "BLKsubsys_id": null,
      "description": "Dynamic viscosity (GLOBprop_4) for binary water + 1,2-propanediol. 30 data points, T 297–450 K, x(PG) = 0.25–0.75, P = 101.3 kPa."
    },
    {
      "doi": "10.1016/j.jct.2007.05.010",
      "lit_num_id": "GLOBlit_2831",
      "block": "PROPblock_12",
      "BLKsubsys_id": null,
      "description": "Mass density (GLOBprop_1) for binary water + 1,2-propanediol. 8 data points, T = 298.15 K, m(H2O) = 0–1.02 mol/kg, P = 101.0 kPa."
    },
    {
      "doi": "10.1016/j.jct.2008.07.005",
      "lit_num_id": "GLOBlit_2979",
      "block": "PROPblock_6",
      "BLKsubsys_id": null,
      "description": "Mass density (GLOBprop_1) for binary water + 1,2-propanediol. 96 data points, T 283–308 K, x(PG) = 0–0.2 (dilute region), P = 98.93 kPa."
    },
    {
      "doi": "10.1016/j.jct.2009.11.018",
      "lit_num_id": "GLOBlit_3180",
      "block": "PROPblock_5",
      "BLKsubsys_id": null,
      "description": "Mass density (GLOBprop_1) for binary water + 1,2-propanediol. 14 data points, T = 298.15 K, x(PG) = 0.073–0.936, P = 101.0 kPa."
    },
    {
      "doi": "10.1021/je201184b",
      "lit_num_id": "GLOBlit_9758",
      "block": "PROPblock_2",
      "BLKsubsys_id": null,
      "description": "Mass density (GLOBprop_1) for binary water + 1,2-propanediol. 106 data points, T 278–318 K, m(PG) = 0.1–0.6 mol/kg, P = 101.0 kPa. Values (0.46–3.46) suggest density differences or apparent molar quantities rather than absolute mass density."
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
      "global_id": "GLOBcomp_61",
      "registry_id": "1,2-propanediol",
      "name": "1,2-propanediol"
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
      "global_id": "GLOBprop_40",
      "registry_id": "kinematic_viscosity_m2_s",
      "name": "Kinematic viscosity, m2/s"
    },
    {
      "type": "prop",
      "global_id": "GLOBprop_42",
      "registry_id": "relative_permittivity_at_various_frequencies",
      "name": "Relative permittivity at various frequencies"
    },
    {
      "type": "prop",
      "global_id": "GLOBprop_44",
      "registry_id": "relative_permittivity_at_zero_frequency",
      "name": "Relative permittivity at zero frequency"
    }
  ],
  "follow_up_suggestions": [
    "Retrieve the remaining ~4 density blocks whose details were truncated or lost due to compaction errors (the working answer mentions 10 density blocks but only 6 are fully detailed in the tool record).",
    "Query for kinematic viscosity (GLOBprop_40) blocks in this binary system, which may provide additional viscosity coverage.",
    "Search for ambient-pressure, temperature-dependent relative permittivity data for water + 1,2-propanediol outside ThermoML, since only one high-pressure isothermal block (GLOBlit_8686) was found.",
    "Retrieve electrical conductivity or ionic conductivity data for this binary system if available, as these are also critical for electrodeposition bath design.",
    "Query for ternary systems containing water + 1,2-propanediol + iron salts (e.g., FeCl2, FeSO4) to find directly relevant electrodeposition bath property data."
  ]
}
