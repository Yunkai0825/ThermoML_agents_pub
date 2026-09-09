# Delegated query run — result

**Question:** Search for ANY property data blocks for the binary system of 1,3,5-trioxane (GLOBcomp_952) and water. What properties are available? List all blocks with their properties, temperatures, and compositions.

**Iterations:** 10  |  **Elapsed:** 531.0s  |  **Tools:** 8  |  **Timed out:** False

---

## Answer

{
  "answer": "## Property Data for the Binary System 1,3,5-Trioxane + Water in ThermoML\n\n**Six property data blocks** were found across **four literature sources**, totaling **308 data points**. The data cover volumetric, phase-equilibrium, vapor–liquid equilibrium, and acoustic properties. No viscosity data exists for this binary system.\n\n---\n\n### Block-by-Block Inventory\n\n| # | Property | GLOBprop | Block | Literature (GLOBlit) | DOI | Data Points | T Range (K) | P Range (kPa) | Composition Range | Phase |\n|---|----------|----------|-------|---------------------|-----|-------------|-------------|---------------|-------------------|-------|\n| 1 | Mass density (kg/m³) | GLOBprop_1 | PROPblock_5 | GLOBlit_3147 | 10.1016/j.jct.2009.08.015 | 175 | 278.15–373.15 | 101–530 | molality 0.049773–0.42135 mol/kg | Liquid |\n| 2 | Partial molar volume at infinite dilution (m³/mol) | GLOBprop_84 | PROPblock_5 | GLOBlit_3168 | 10.1016/j.jct.2009.11.005 | 25 | 298.16–498.17 | 2020–30070 | x(trioxane) = 0.0 | Liquid |\n| 3 | Liquid–liquid equilibrium temperature (K) | GLOBprop_20 | PROPblock_1 | GLOBlit_8200 | 10.1021/je030243h | 19 | 301.28–321.01 | 101.3 (fixed) | w(trioxane) 0.2037–0.8994 | Liquid mixture |\n| 4 | Vapor pressure (kPa) | GLOBprop_5 | PROPblock_1 | GLOBlit_8573 | 10.1021/je050015i | 17 | 393.0–413.2 | 226.8–450.1 | x(trioxane) 0.004–0.7619 | Liquid/Gas |\n| 5 | Gas-phase mole fraction | GLOBprop_2 | PROPblock_2 | GLOBlit_8573 | 10.1021/je050015i | 19 | 393.0–413.2 | — | x(trioxane, liq) 0.004–0.7619; y(trioxane, gas) 0.0199–0.4757 | Gas/Liquid |\n| 6 | Speed of sound (m/s) | GLOBprop_8 | PROPblock_5 | GLOBlit_10066 | 10.1021/je301352v | 53 | 278.15–318.15 | 101.0 (fixed) | molality 0.049773–0.401402 mol/kg | Liquid |\n\n---\n\n### Detailed Property Descriptions with Representative Data\n\n#### 1. Mass Density — GLOBlit_3147 (DOI: 10.1016/j.jct.2009.08.015)\nThe largest dataset with **175 points** measured by vibrating tube method. Covers atmospheric pressure (101 kPa) and elevated pressures (510–530 kPa) over T = 278.15–373.15 K, with trioxane molality from 0.049773 to 0.42135 mol/kg.\n\nRepresentative data points:\n- At 278.15 K, 101 kPa, m = 0.049773 mol/kg → ρ = 1.138 kg/m³\n- At 298.15 K, 101 kPa, m = 0.42135 mol/kg → ρ = 8.415 kg/m³\n- At 373.15 K, 530 kPa, m = 0.405965 mol/kg → ρ = 6.0576 kg/m³\n\n*(Note: the density values as stored appear to represent density increments Δρ rather than absolute densities, given their small magnitudes.)*\n\n#### 2. Partial Molar Volume at Infinite Dilution — GLOBlit_3168 (DOI: 10.1016/j.jct.2009.11.005)\n**25 data points** at x(trioxane) = 0.0 (infinite dilution), derived analytically. Covers high pressures (2020–30070 kPa) and temperatures from 298.16 to 498.17 K.\n\nRepresentative data points:\n- At 298.16 K, 15030 kPa → V∞ = 6.964×10⁻⁵ m³/mol\n- At 298.16 K, 30070 kPa → V∞ = 6.95×10⁻⁵ m³/mol\n- At 498.16 K, 3000 kPa → V∞ = 9.496×10⁻⁵ m³/mol\n- At 498.17 K, 30060 kPa → V∞ = 9.074×10⁻⁵ m³/mol\n\nThe partial molar volume increases with temperature (thermal expansion) and decreases with pressure (compression), as expected.\n\n#### 3. Liquid–Liquid Equilibrium Temperature — GLOBlit_8200 (DOI: 10.1021/je030243h)\n**19 data points** at atmospheric pressure (101.3 kPa) mapping the miscibility boundary. The LLE curve is non-monotonic, consistent with an **upper critical solution temperature (UCST)** phase diagram.\n\nRepresentative data points:\n- w(trioxane) = 0.2037 → T_LLE = 301.28 K\n- w(trioxane) = 0.4941 → T_LLE = 317.50 K\n- w(trioxane) = 0.6159 → T_LLE = 319.53 K (near the maximum)\n- w(trioxane) = 0.8928 → T_LLE = 321.01 K\n- w(trioxane) = 0.8994 → T_LLE = 319.88 K\n\nThe maximum LLE temperature near w ≈ 0.6–0.9 indicates the critical composition region of the UCST curve.\n\n#### 4. Vapor Pressure — GLOBlit_8573 (DOI: 10.1021/je050015i)\n**17 data points** measured by thin film evaporator at T = 393.0–413.2 K across x(trioxane) = 0.004–0.7619.\n\nRepresentative data points:\n- At 393.2 K, x = 0.0345 → P = 226.8 kPa\n- At 393.0 K, x = 0.4983 → P = 252.3 kPa\n- At 413.0 K, x = 0.436 → P = 450.1 kPa (pressure maximum)\n- At 413.1 K, x = 0.7619 → P = 385.2 kPa\n\nThe pressure maximum near x(trioxane) ≈ 0.436 at 413 K indicates **positive deviations from Raoult's law**, suggesting the system forms a positive azeotrope at these conditions.\n\n#### 5. Gas-Phase Mole Fraction — GLOBlit_8573 (DOI: 10.1021/je050015i)\n**19 data points** measured by chromatography, complementing the vapor pressure data from the same source. Gas-phase trioxane mole fractions range from 0.0199 to 0.4757 over the same temperature and liquid composition range.\n\n#### 6. Speed of Sound — GLOBlit_10066 (DOI: 10.1021/je301352v)\n**53 data points** measured by pulse-echo method at atmospheric pressure (101.0 kPa), T = 278.15–318.15 K, with trioxane molality from 0.049773 to 0.401402 mol/kg.\n\n---\n\n### Summary by Property Category\n\n| Category | Properties | Total Points | Sources |\n|----------|-----------|-------------|---------|\n| Volumetric | Mass density, Partial molar volume | 200 | 2 DOIs |\n| Phase equilibrium (LLE) | LLE temperature | 19 | 1 DOI |\n| Vapor–liquid equilibrium | Vapor pressure, Gas-phase mole fraction | 36 | 1 DOI |\n| Acoustic | Speed of sound | 53 | 1 DOI |\n| **Total** | **6 properties** | **308 points** | **4 DOIs** |\n\n### Key Chemical Insights\n\n1,3,5-Trioxane (the cyclic trimer of formaldehyde) exhibits **partial miscibility with water** at ambient temperatures, with a UCST-type phase diagram (LLE temperatures 301–321 K). At elevated temperatures (393–413 K), the system is fully miscible and shows **positive azeotrope behavior** in VLE. The volumetric data span a wide range of conditions from near-ambient to high pressure (up to 30 MPa), providing comprehensive thermodynamic characterization of this industrially relevant system.",
  "core_claims": [
    "Six property data blocks totaling 308 data points were found for the binary system 1,3,5-trioxane + water across four literature sources, covering mass density (175 points), partial molar volume at infinite dilution (25 points), liquid–liquid equilibrium temperature (19 points), vapor pressure (17 points), gas-phase mole fraction (19 points), and speed of sound (53 points).",
    "No viscosity data exists for this binary system in the surveyed ThermoML sources.",
    "The liquid–liquid equilibrium data (19 points at 101.3 kPa, T = 301.28–321.01 K, w(trioxane) = 0.2037–0.8994) show a non-monotonic curve consistent with an upper critical solution temperature (UCST) phase diagram.",
    "Vapor pressure data at T = 393.0–413.2 K show a pressure maximum near x(trioxane) ≈ 0.436 at 413 K (P = 450.1 kPa), indicating positive deviations from Raoult's law and suggesting positive azeotrope behavior.",
    "Partial molar volume at infinite dilution (25 points, T = 298.16–498.17 K, P = 2020–30070 kPa) increases with temperature and decreases with pressure, as expected from thermal expansion and compression effects.",
    "The mass density values as stored appear to represent density increments Δρ rather than absolute densities, given their small magnitudes."
  ],
  "confidence": "medium",
  "sources": [
    {
      "doi": "10.1016/j.jct.2009.08.015",
      "lit_num_id": "GLOBlit_3147",
      "block": "PROPblock_5",
      "BLKsubsys_id": null,
      "description": "Provides 175 mass density data points for the 1,3,5-trioxane + water binary system over T = 278.15–373.15 K, P = 101–530 kPa, and molality 0.049773–0.42135 mol/kg. The small magnitude values (1.019–9.391 kg/m³) likely represent density increments, as noted in the answer."
    },
    {
      "doi": "10.1016/j.jct.2009.11.005",
      "lit_num_id": "GLOBlit_3168",
      "block": "PROPblock_5",
      "BLKsubsys_id": null,
      "description": "Provides 25 partial molar volume at infinite dilution data points for 1,3,5-trioxane in water over T = 298.16–498.17 K and P = 2020–30070 kPa, with mole fraction constrained to 0.0. Values range from 6.9×10⁻⁵ to 9.5×10⁻⁵ m³/mol, consistent with the answer."
    },
    {
      "doi": "10.1021/je030243h",
      "lit_num_id": "GLOBlit_8200",
      "block": "PROPblock_1",
      "BLKsubsys_id": null,
      "description": "Provides 19 liquid–liquid equilibrium temperature data points at 101.3 kPa for the 1,3,5-trioxane + water system, with mass fraction 0.2037–0.8994 and T_LLE = 301.28–321.01 K, mapping the UCST miscibility boundary described in the answer."
    },
    {
      "doi": "10.1021/je050015i",
      "lit_num_id": "GLOBlit_8573",
      "block": "PROPblock_1",
      "BLKsubsys_id": null,
      "description": "Provides 17 vapor pressure data points for the 1,3,5-trioxane + water binary at T = 393.0–413.2 K and x(trioxane) = 0.004–0.7619, with pressures 226.8–450.1 kPa. Supports the VLE and positive azeotrope discussion in the answer."
    },
    {
      "doi": "10.1021/je050015i",
      "lit_num_id": "GLOBlit_8573",
      "block": "PROPblock_2",
      "BLKsubsys_id": null,
      "description": "Provides 19 gas-phase mole fraction data points complementing the vapor pressure block from the same source, with y(trioxane) = 0.0199–0.4757 measured by chromatography at T = 393.0–413.2 K, completing the VLE characterization."
    },
    {
      "doi": "10.1021/je301352v",
      "lit_num_id": "GLOBlit_10066",
      "block": "PROPblock_5",
      "BLKsubsys_id": null,
      "description": "Provides 53 speed of sound data points for 1,3,5-trioxane + water at 101.0 kPa, T = 278.15–318.15 K, and molality 0.049773–0.401402 mol/kg. The small values (1.75–22.38 m/s) likely represent speed-of-sound increments rather than absolute values."
    }
  ],
  "follow_up_suggestions": [
    "Retrieve detailed data arrays for any specific block (e.g., PROPblock_5 from GLOBlit_3147) to examine density values and confirm whether they represent absolute densities or density increments.",
    "Search for activity coefficient or excess enthalpy data for the 1,3,5-trioxane + water system to complement the existing VLE and LLE data.",
    "Investigate whether ternary systems involving 1,3,5-trioxane, water, and formaldehyde have property data in ThermoML, given the industrial relevance of formaldehyde polymerization."
  ],
  "id_catalog_snapshot": [
    {
      "type": "comp",
      "global_id": "GLOBcomp_952",
      "registry_id": "CAS:110-88-3",
      "name": "1,3,5-trioxane"
    },
    {
      "type": "lit",
      "global_id": "GLOBlit_3147",
      "registry_id": "10.1016/j.jct.2009.08.015",
      "name": "2010-cib-ale-0 (mass density)"
    },
    {
      "type": "lit",
      "global_id": "GLOBlit_3168",
      "registry_id": "10.1016/j.jct.2009.11.005",
      "name": "2010-cib--0 (partial molar volume)"
    },
    {
      "type": "lit",
      "global_id": "GLOBlit_8200",
      "registry_id": "10.1021/je030243h",
      "name": "2004-gru-has-0 (LLE temperature)"
    },
    {
      "type": "lit",
      "global_id": "GLOBlit_8573",
      "registry_id": "10.1021/je050015i",
      "name": "2005-alb-has-0 (VLE)"
    },
    {
      "type": "lit",
      "global_id": "GLOBlit_10066",
      "registry_id": "10.1021/je301352v",
      "name": "2013-cib--0 (speed of sound)"
    }
  ]
}

---

## Data Inspections (deterministic evidence ledger)

Hardcoded envelope merge — not agent-authored. 4 entr(ies); verbatim rows below.

- INSP_1f2b6352c2ae — GLOBlit_3147::PROPblock_5 · rdp · 30 rows
- INSP_e706dc37d6a0 — GLOBlit_3168::PROPblock_5 · rdp · 21 rows
- INSP_93df686bae96 — GLOBlit_8200::PROPblock_1 · rdp · 9 rows
- INSP_3ced41568ce1 — GLOBlit_8573::PROPblock_1 · rdp · 12 rows

```json
[
  {
    "doi": "10.1016/j.jct.2009.08.015",
    "block_number": "PROPblock_5",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "pressure_kpa",
      "temperature_k",
      "molality_mol_kg_<1,3,5-trioxane>",
      "mass_density_kg_m3"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "pressure_kpa": "101",
        "temperature_k": "278.15",
        "molality_mol_kg_<1,3,5-trioxane>": "0.049773",
        "mass_density_kg_m3": "1.138"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "pressure_kpa": "101",
        "temperature_k": "278.15",
        "molality_mol_kg_<1,3,5-trioxane>": "0.049773",
        "mass_density_kg_m3": "1.138"
      },
      {
        "BLKpoint_id": "BLKpoint_17",
        "pressure_kpa": "101",
        "temperature_k": "278.15",
        "molality_mol_kg_<1,3,5-trioxane>": "0.42135",
        "mass_density_kg_m3": "9.391"
      },
      {
        "BLKpoint_id": "BLKpoint_18",
        "pressure_kpa": "101",
        "temperature_k": "283.15",
        "molality_mol_kg_<1,3,5-trioxane>": "0.049773",
        "mass_density_kg_m3": "1.104"
      },
      {
        "BLKpoint_id": "BLKpoint_20",
        "pressure_kpa": "101",
        "temperature_k": "283.15",
        "molality_mol_kg_<1,3,5-trioxane>": "0.049773",
        "mass_density_kg_m3": "1.104"
      },
      {
        "BLKpoint_id": "BLKpoint_21",
        "pressure_kpa": "101",
        "temperature_k": "283.15",
        "molality_mol_kg_<1,3,5-trioxane>": "0.049773",
        "mass_density_kg_m3": "1.104"
      },
      {
        "BLKpoint_id": "BLKpoint_37",
        "pressure_kpa": "101",
        "temperature_k": "283.15",
        "molality_mol_kg_<1,3,5-trioxane>": "0.42135",
        "mass_density_kg_m3": "9.106"
      },
      {
        "BLKpoint_id": "BLKpoint_38",
        "pressure_kpa": "101",
        "temperature_k": "288.15",
        "molality_mol_kg_<1,3,5-trioxane>": "0.049773",
        "mass_density_kg_m3": "1.072"
      },
      {
        "BLKpoint_id": "BLKpoint_56",
        "pressure_kpa": "101",
        "temperature_k": "288.15",
        "molality_mol_kg_<1,3,5-trioxane>": "0.401402",
        "mass_density_kg_m3": "8.45"
      },
      {
        "BLKpoint_id": "BLKpoint_57",
        "pressure_kpa": "101",
        "temperature_k": "288.15",
        "molality_mol_kg_<1,3,5-trioxane>": "0.401402",
        "mass_density_kg_m3": "8.45"
      },
      {
        "BLKpoint_id": "BLKpoint_60",
        "pressure_kpa": "101",
        "temperature_k": "293.15",
        "molality_mol_kg_<1,3,5-trioxane>": "0.049773",
        "mass_density_kg_m3": "1.046"
      },
      {
        "BLKpoint_id": "BLKpoint_62",
        "pressure_kpa": "101",
        "temperature_k": "293.15",
        "molality_mol_kg_<1,3,5-trioxane>": "0.049773",
        "mass_density_kg_m3": "1.046"
      },
      {
        "BLKpoint_id": "BLKpoint_82",
        "pressure_kpa": "101",
        "temperature_k": "293.15",
        "molality_mol_kg_<1,3,5-trioxane>": "0.42135",
        "mass_density_kg_m3": "8.623"
      },
      {
        "BLKpoint_id": "BLKpoint_84",
        "pressure_kpa": "101",
        "temperature_k": "298.15",
        "molality_mol_kg_<1,3,5-trioxane>": "0.049773",
        "mass_density_kg_m3": "1.019"
      },
      {
        "BLKpoint_id": "BLKpoint_101",
        "pressure_kpa": "101",
        "temperature_k": "298.15",
        "molality_mol_kg_<1,3,5-trioxane>": "0.42135",
        "mass_density_kg_m3": "8.415"
      },
      {
        "BLKpoint_id": "BLKpoint_103",
        "pressure_kpa": "101",
        "temperature_k": "308.15",
        "molality_mol_kg_<1,3,5-trioxane>": "0.063363",
        "mass_density_kg_m3": "1.242"
      },
      {
        "BLKpoint_id": "BLKpoint_107",
        "pressure_kpa": "101",
        "temperature_k": "308.15",
        "molality_mol_kg_<1,3,5-trioxane>": "0.42135",
        "mass_density_kg_m3": "8.033"
      },
      {
        "BLKpoint_id": "BLKpoint_108",
        "pressure_kpa": "101",
        "temperature_k": "318.15",
        "molality_mol_kg_<1,3,5-trioxane>": "0.063363",
        "mass_density_kg_m3": "1.192"
      },
      {
        "BLKpoint_id": "BLKpoint_115",
        "pressure_kpa": "101",
        "temperature_k": "318.15",
        "molality_mol_kg_<1,3,5-trioxane>": "0.42135",
        "mass_density_kg_m3": "7.699"
      },
      {
        "BLKpoint_id": "BLKpoint_116",
        "pressure_kpa": "510",
        "temperature_k": "298.15",
        "molality_mol_kg_<1,3,5-trioxane>": "0.102316",
        "mass_density_kg_m3": "2.0828"
      },
      {
        "BLKpoint_id": "BLKpoint_127",
        "pressure_kpa": "510",
        "temperature_k": "298.15",
        "molality_mol_kg_<1,3,5-trioxane>": "0.413939",
        "mass_density_kg_m3": "8.2453"
      },
      {
        "BLKpoint_id": "BLKpoint_130",
        "pressure_kpa": "510",
        "temperature_k": "318.15",
        "molality_mol_kg_<1,3,5-trioxane>": "0.102316",
        "mass_density_kg_m3": "1.9136"
      },
      {
        "BLKpoint_id": "BLKpoint_137",
        "pressure_kpa": "510",
        "temperature_k": "318.15",
        "molality_mol_kg_<1,3,5-trioxane>": "0.413939",
        "mass_density_kg_m3": "7.5556"
      },
      {
        "BLKpoint_id": "BLKpoint_142",
        "pressure_kpa": "520",
        "temperature_k": "338.15",
        "molality_mol_kg_<1,3,5-trioxane>": "0.102316",
        "mass_density_kg_m3": "1.7694"
      },
      {
        "BLKpoint_id": "BLKpoint_149",
        "pressure_kpa": "520",
        "temperature_k": "338.15",
        "molality_mol_kg_<1,3,5-trioxane>": "0.413939",
        "mass_density_kg_m3": "6.9865"
      },
      {
        "BLKpoint_id": "BLKpoint_153",
        "pressure_kpa": "520",
        "temperature_k": "358.15",
        "molality_mol_kg_<1,3,5-trioxane>": "0.110502",
        "mass_density_kg_m3": "1.7816"
      },
      {
        "BLKpoint_id": "BLKpoint_154",
        "pressure_kpa": "520",
        "temperature_k": "358.15",
        "molality_mol_kg_<1,3,5-trioxane>": "0.110502",
        "mass_density_kg_m3": "1.7816"
      },
      {
        "BLKpoint_id": "BLKpoint_161",
        "pressure_kpa": "520",
        "temperature_k": "358.15",
        "molality_mol_kg_<1,3,5-trioxane>": "0.405965",
        "mass_density_kg_m3": "6.3864"
      },
      {
        "BLKpoint_id": "BLKpoint_166",
        "pressure_kpa": "530",
        "temperature_k": "373.15",
        "molality_mol_kg_<1,3,5-trioxane>": "0.110502",
        "mass_density_kg_m3": "1.6892"
      },
      {
        "BLKpoint_id": "BLKpoint_175",
        "pressure_kpa": "530",
        "temperature_k": "373.15",
        "molality_mol_kg_<1,3,5-trioxane>": "0.405965",
        "mass_density_kg_m3": "6.0576"
      }
    ],
    "inspection_id": "INSP_1f2b6352c2ae",
    "lit_num_id": "GLOBlit_3147"
  },
  {
    "doi": "10.1016/j.jct.2009.11.005",
    "block_number": "PROPblock_5",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "pressure_kpa",
      "mole_fraction_<1,3,5-trioxane>",
      "partial_molar_volume_m3_mol_<1,3,5-trioxane>"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "298.16",
        "pressure_kpa": "15030",
        "mole_fraction_<1,3,5-trioxane>": "0.0",
        "partial_molar_volume_m3_mol_<1,3,5-trioxane>": "6.964e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "temperature_k": "298.16",
        "pressure_kpa": "30070",
        "mole_fraction_<1,3,5-trioxane>": "0.0",
        "partial_molar_volume_m3_mol_<1,3,5-trioxane>": "6.95e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "temperature_k": "318.16",
        "pressure_kpa": "15030",
        "mole_fraction_<1,3,5-trioxane>": "0.0",
        "partial_molar_volume_m3_mol_<1,3,5-trioxane>": "7.151e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "temperature_k": "318.16",
        "pressure_kpa": "30050",
        "mole_fraction_<1,3,5-trioxane>": "0.0",
        "partial_molar_volume_m3_mol_<1,3,5-trioxane>": "7.125e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "temperature_k": "338.15",
        "pressure_kpa": "15050",
        "mole_fraction_<1,3,5-trioxane>": "0.0",
        "partial_molar_volume_m3_mol_<1,3,5-trioxane>": "7.332e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "temperature_k": "338.15",
        "pressure_kpa": "30040",
        "mole_fraction_<1,3,5-trioxane>": "0.0",
        "partial_molar_volume_m3_mol_<1,3,5-trioxane>": "7.293e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "temperature_k": "358.17",
        "pressure_kpa": "15020",
        "mole_fraction_<1,3,5-trioxane>": "0.0",
        "partial_molar_volume_m3_mol_<1,3,5-trioxane>": "7.513e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "temperature_k": "358.17",
        "pressure_kpa": "30010",
        "mole_fraction_<1,3,5-trioxane>": "0.0",
        "partial_molar_volume_m3_mol_<1,3,5-trioxane>": "7.466e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_9",
        "temperature_k": "373.18",
        "pressure_kpa": "30040",
        "mole_fraction_<1,3,5-trioxane>": "0.0",
        "partial_molar_volume_m3_mol_<1,3,5-trioxane>": "7.603e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "temperature_k": "373.19",
        "pressure_kpa": "15050",
        "mole_fraction_<1,3,5-trioxane>": "0.0",
        "partial_molar_volume_m3_mol_<1,3,5-trioxane>": "7.657e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "temperature_k": "398.18",
        "pressure_kpa": "2020",
        "mole_fraction_<1,3,5-trioxane>": "0.0",
        "partial_molar_volume_m3_mol_<1,3,5-trioxane>": "7.984e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_13",
        "temperature_k": "398.18",
        "pressure_kpa": "30060",
        "mole_fraction_<1,3,5-trioxane>": "0.0",
        "partial_molar_volume_m3_mol_<1,3,5-trioxane>": "7.832e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_14",
        "temperature_k": "423.17",
        "pressure_kpa": "2040",
        "mole_fraction_<1,3,5-trioxane>": "0.0",
        "partial_molar_volume_m3_mol_<1,3,5-trioxane>": "8.27e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_16",
        "temperature_k": "423.18",
        "pressure_kpa": "30050",
        "mole_fraction_<1,3,5-trioxane>": "0.0",
        "partial_molar_volume_m3_mol_<1,3,5-trioxane>": "8.087e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_17",
        "temperature_k": "448.16",
        "pressure_kpa": "2050",
        "mole_fraction_<1,3,5-trioxane>": "0.0",
        "partial_molar_volume_m3_mol_<1,3,5-trioxane>": "8.614e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_19",
        "temperature_k": "448.17",
        "pressure_kpa": "30060",
        "mole_fraction_<1,3,5-trioxane>": "0.0",
        "partial_molar_volume_m3_mol_<1,3,5-trioxane>": "8.367e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_20",
        "temperature_k": "473.17",
        "pressure_kpa": "15030",
        "mole_fraction_<1,3,5-trioxane>": "0.0",
        "partial_molar_volume_m3_mol_<1,3,5-trioxane>": "8.849e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_21",
        "temperature_k": "473.17",
        "pressure_kpa": "30040",
        "mole_fraction_<1,3,5-trioxane>": "0.0",
        "partial_molar_volume_m3_mol_<1,3,5-trioxane>": "8.689e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_22",
        "temperature_k": "473.18",
        "pressure_kpa": "2070",
        "mole_fraction_<1,3,5-trioxane>": "0.0",
        "partial_molar_volume_m3_mol_<1,3,5-trioxane>": "9.013e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_23",
        "temperature_k": "498.16",
        "pressure_kpa": "3000",
        "mole_fraction_<1,3,5-trioxane>": "0.0",
        "partial_molar_volume_m3_mol_<1,3,5-trioxane>": "9.496e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_25",
        "temperature_k": "498.17",
        "pressure_kpa": "30060",
        "mole_fraction_<1,3,5-trioxane>": "0.0",
        "partial_molar_volume_m3_mol_<1,3,5-trioxane>": "9.074e-05"
      }
    ],
    "inspection_id": "INSP_e706dc37d6a0",
    "lit_num_id": "GLOBlit_3168"
  },
  {
    "doi": "10.1021/je030243h",
    "block_number": "PROPblock_1",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "mass_fraction_<1,3,5-trioxane>",
      "pressure_kpa",
      "liquidliquid_equilibrium_temperature_k"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "mass_fraction_<1,3,5-trioxane>": "0.2037",
        "pressure_kpa": "101.3",
        "liquidliquid_equilibrium_temperature_k": "301.28"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "mass_fraction_<1,3,5-trioxane>": "0.4941",
        "pressure_kpa": "101.3",
        "liquidliquid_equilibrium_temperature_k": "317.5"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "mass_fraction_<1,3,5-trioxane>": "0.496",
        "pressure_kpa": "101.3",
        "liquidliquid_equilibrium_temperature_k": "317.35"
      },
      {
        "BLKpoint_id": "BLKpoint_9",
        "mass_fraction_<1,3,5-trioxane>": "0.5992",
        "pressure_kpa": "101.3",
        "liquidliquid_equilibrium_temperature_k": "319.4"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "mass_fraction_<1,3,5-trioxane>": "0.5999",
        "pressure_kpa": "101.3",
        "liquidliquid_equilibrium_temperature_k": "318.39"
      },
      {
        "BLKpoint_id": "BLKpoint_12",
        "mass_fraction_<1,3,5-trioxane>": "0.6159",
        "pressure_kpa": "101.3",
        "liquidliquid_equilibrium_temperature_k": "319.53"
      },
      {
        "BLKpoint_id": "BLKpoint_13",
        "mass_fraction_<1,3,5-trioxane>": "0.654",
        "pressure_kpa": "101.3",
        "liquidliquid_equilibrium_temperature_k": "319.05"
      },
      {
        "BLKpoint_id": "BLKpoint_18",
        "mass_fraction_<1,3,5-trioxane>": "0.8928",
        "pressure_kpa": "101.3",
        "liquidliquid_equilibrium_temperature_k": "321.01"
      },
      {
        "BLKpoint_id": "BLKpoint_19",
        "mass_fraction_<1,3,5-trioxane>": "0.8994",
        "pressure_kpa": "101.3",
        "liquidliquid_equilibrium_temperature_k": "319.88"
      }
    ],
    "inspection_id": "INSP_93df686bae96",
    "lit_num_id": "GLOBlit_8200"
  },
  {
    "doi": "10.1021/je050015i",
    "block_number": "PROPblock_1",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<1,3,5-trioxane>",
      "vapor_or_sublimation_pressure_kpa"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "393",
        "mole_fraction_<1,3,5-trioxane>": "0.4983",
        "vapor_or_sublimation_pressure_kpa": "252.3"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "temperature_k": "393.1",
        "mole_fraction_<1,3,5-trioxane>": "0.0953",
        "vapor_or_sublimation_pressure_kpa": "246.2"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "temperature_k": "393.2",
        "mole_fraction_<1,3,5-trioxane>": "0.0345",
        "vapor_or_sublimation_pressure_kpa": "226.8"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "temperature_k": "412.2",
        "mole_fraction_<1,3,5-trioxane>": "0.004",
        "vapor_or_sublimation_pressure_kpa": "363.9"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "temperature_k": "413",
        "mole_fraction_<1,3,5-trioxane>": "0.1212",
        "vapor_or_sublimation_pressure_kpa": "445.9"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "temperature_k": "413",
        "mole_fraction_<1,3,5-trioxane>": "0.436",
        "vapor_or_sublimation_pressure_kpa": "450.1"
      },
      {
        "BLKpoint_id": "BLKpoint_9",
        "temperature_k": "413.1",
        "mole_fraction_<1,3,5-trioxane>": "0.0192",
        "vapor_or_sublimation_pressure_kpa": "394.6"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "temperature_k": "413.1",
        "mole_fraction_<1,3,5-trioxane>": "0.1007",
        "vapor_or_sublimation_pressure_kpa": "441.9"
      },
      {
        "BLKpoint_id": "BLKpoint_12",
        "temperature_k": "413.1",
        "mole_fraction_<1,3,5-trioxane>": "0.7619",
        "vapor_or_sublimation_pressure_kpa": "385.2"
      },
      {
        "BLKpoint_id": "BLKpoint_13",
        "temperature_k": "413.2",
        "mole_fraction_<1,3,5-trioxane>": "0.011",
        "vapor_or_sublimation_pressure_kpa": "383.4"
      },
      {
        "BLKpoint_id": "BLKpoint_16",
        "temperature_k": "413.2",
        "mole_fraction_<1,3,5-trioxane>": "0.0546",
        "vapor_or_sublimation_pressure_kpa": "432.1"
      },
      {
        "BLKpoint_id": "BLKpoint_17",
        "temperature_k": "413.2",
        "mole_fraction_<1,3,5-trioxane>": "0.1009",
        "vapor_or_sublimation_pressure_kpa": "441.1"
      }
    ],
    "inspection_id": "INSP_3ced41568ce1",
    "lit_num_id": "GLOBlit_8573"
  }
]
```
