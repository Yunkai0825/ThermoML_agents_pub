# Delegated query run — result

**Question:** Find all data blocks containing iron(II) sulfate (GLOBcomp_1586) and water (GLOBcomp_1) with properties: viscosity (GLOBprop_4), density (GLOBprop_1), surface tension (GLOBprop_13), electrical conductivity (GLOBprop_18), or molar conductivity (GLOBprop_37). Report DOIs, block numbers, temperature ranges, concentration ranges, and property types.

**Iterations:** 2  |  **Elapsed:** 152.1s  |  **Tools:** 8  |  **Timed out:** False

---

## Answer

{
  "answer": "## Transport Property Data for Aqueous Iron(II) Sulfate (FeSO₄) in the ThermoML Database\n\nA comprehensive search of the ThermoML database for data blocks containing iron(II) sulfate (FeSO₄) and water across five transport/physical properties yielded the following results:\n\n### Data Found\n\n**Electrical Conductivity (GLOBprop_18)**\n- **DOI:** 10.1021/je101012n (GLOBlit_9386)\n- **Block:** PROPblock_30\n- **System:** Binary (FeSO₄ + H₂O)\n- **Temperature range:** 278.1–363.15 K (7 unique temperatures)\n- **Concentration range:** 0.00112–0.2576 mol/kg (molality, 5 unique concentrations)\n- **Conductivity range:** 0.06212–4.11 S/m\n- **Data points:** 33\n- **Measurement method:** Alternating current cell with electrodes\n- **Pressure:** 101.0 kPa (fixed)\n- **Phase:** Liquid\n- **Uncertainty:** Propagation of evaluated standard uncertainties at 95% confidence level\n\n### Properties Not Found\n\n| Property | ID | Blocks Found |\n|----------|-----|:---:|\n| Mass density | GLOBprop_1 | 0 |\n| Dynamic viscosity | GLOBprop_4 | 0 |\n| Surface tension (liquid–gas) | GLOBprop_13 | 0 |\n| Molar conductivity | GLOBprop_37 | 0 |\n\n### Additional Context\n\nIron(II) sulfate appears in only **3 total data blocks** across 3 publications in the ThermoML database. The two other blocks report **solubility as molality** (GLOBprop_21) for ternary systems:\n\n1. FeSO₄ + H₂SO₄ + H₂O at 298.15 K (DOI: 10.1016/j.jct.2016.07.006, GLOBlit_4745)\n2. FeSO₄ + HCl + H₂O at 293.15–313.15 K (DOI: 10.1021/acs.jced.6b00783, GLOBlit_7012)\n\n### Summary for Fe Electrodeposition Applications\n\nFor electrodeposition processes, electrical conductivity is a critical transport property governing current distribution and energy efficiency. The available dataset from McCleskey (2011) covers a useful temperature range (278–363 K) and dilute-to-moderate concentrations (up to ~0.26 mol/kg), which is relevant for understanding ion mobility in FeSO₄ electrolytes. However, the ThermoML database lacks density, viscosity, surface tension, and molar conductivity data for this system — properties that are also important for modeling mass transport, bubble dynamics, and electrolyte flow in electrodeposition cells.",
  "core_claims": [
    "The ThermoML database contains electrical conductivity data for the binary FeSO₄ + H₂O system (DOI: 10.1021/je101012n), covering 278.1–363.15 K, 0.00112–0.2576 mol/kg, and 0.06212–4.11 S/m at 101.0 kPa, comprising 33 data points measured by alternating current cell with electrodes.",
    "No mass density, dynamic viscosity, surface tension, or molar conductivity data for aqueous FeSO₄ were found in the ThermoML database.",
    "Iron(II) sulfate appears in only 3 total data blocks across 3 publications in the ThermoML database; the two blocks beyond the conductivity data report solubility for ternary systems (FeSO₄ + H₂SO₄ + H₂O and FeSO₄ + HCl + H₂O)."
  ],
  "confidence": "high",
  "sources": [
    {
      "doi": "10.1021/je101012n",
      "lit_num_id": "GLOBlit_9386",
      "block": "PROPblock_30",
      "BLKsubsys_id": null,
      "description": "Electrical conductivity (GLOBprop_18) of binary FeSO4 + H2O system. 33 data points, temperature range 278.1–363.15 K, molality range 0.00112–0.2576 mol/kg, conductivity range 0.06212–4.11 S/m. Pressure fixed at 101.0 kPa, liquid phase. Measurement method: alternating current cell with electrodes."
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
      "global_id": "GLOBcomp_1586",
      "registry_id": "FeSO4",
      "name": "iron(II) sulfate"
    },
    {
      "type": "prop",
      "global_id": "GLOBprop_1",
      "registry_id": "density",
      "name": "Mass density"
    },
    {
      "type": "prop",
      "global_id": "GLOBprop_4",
      "registry_id": "viscosity",
      "name": "Viscosity (dynamic)"
    },
    {
      "type": "prop",
      "global_id": "GLOBprop_13",
      "registry_id": "surface_tension",
      "name": "Surface tension (liquid-gas)"
    },
    {
      "type": "prop",
      "global_id": "GLOBprop_18",
      "registry_id": "conductivity",
      "name": "Electrical conductivity"
    },
    {
      "type": "prop",
      "global_id": "GLOBprop_37",
      "registry_id": "molar_conductivity",
      "name": "Molar conductivity"
    }
  ],
  "follow_up_suggestions": [
    "Search for density (GLOBprop_1) and viscosity (GLOBprop_4) data for other iron salts such as iron(II) chloride or iron(III) sulfate in aqueous solution, which may serve as proxies or complementary data for Fe electrodeposition modeling.",
    "Query for molar conductivity (GLOBprop_37) of other divalent metal sulfates (e.g., CuSO4, ZnSO4, NiSO4) in water to compare ion mobility trends relevant to electrodeposition.",
    "Retrieve the full 33-point dataset from GLOBlit_9386/PROPblock_30 to extract specific conductivity values at individual temperature and concentration conditions for electrodeposition process design.",
    "Search external databases (e.g., NIST, Dortmund Data Bank) for FeSO4 density and viscosity data not covered in ThermoML."
  ]
}
