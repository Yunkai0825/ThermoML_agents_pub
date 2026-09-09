# Delegated query run — result

**Question:** Search for pure-component viscosity data for 1,3,5-trioxane (GLOBcomp_952). Also search for viscosity data for 1,3,5-trioxane in ANY binary system (not just water). List all blocks found with their properties, co-solvents, temperatures, and data ranges.

**Iterations:** 3  |  **Elapsed:** 230.9s  |  **Tools:** 2  |  **Timed out:** False

---

## Answer

{
  "answer": "## Viscosity Data for 1,3,5-Trioxane in ThermoML — Search Results\n\n**No viscosity data of any kind was found for 1,3,5-trioxane (GLOBcomp_952) in the ThermoML database.** This applies to:\n\n- **Pure-component (unary) systems:** No dynamic viscosity or kinematic viscosity data. In fact, no pure-component data blocks of any property exist for 1,3,5-trioxane.\n- **Binary mixture systems:** No dynamic viscosity (GLOBprop_4) or kinematic viscosity (GLOBprop_40) data with any co-solvent.\n\n---\n\n### What IS Available for 1,3,5-Trioxane in Binary Systems\n\nAlthough no viscosity data exists, the ThermoML database does contain **9 binary-mixture data blocks** for 1,3,5-trioxane across 5 publications:\n\n| # | Property | Co-solvent | Block | T range (K) | DOI | Literature ID |\n|---|----------|-----------|-------|-------------|-----|---------------|\n| 1 | Mass density (GLOBprop_1) | Water | PROPblock_5 | 278.15–373.15 | 10.1016/j.jct.2009.08.015 | GLOBlit_3147 |\n| 2 | Partial molar volume (GLOBprop_84) | Water | PROPblock_5 | 298.16–498.17 | 10.1016/j.jct.2009.11.005 | GLOBlit_3168 |\n| 3 | LLE temperature (GLOBprop_20) | Water | PROPblock_1 | 301.28–321.01 | 10.1021/je030243h | GLOBlit_8200 |\n| 4 | SLE mole fraction (GLOBprop_2) | Methanol | PROPblock_1 | 293.5–328.2 | 10.1021/je049978s | GLOBlit_8564 |\n| 5 | SLE mole fraction (GLOBprop_2) | Ethanol | PROPblock_2 | 294.3–328.3 | 10.1021/je049978s | GLOBlit_8564 |\n| 6 | SLE mole fraction (GLOBprop_2) | Propan-2-ol | PROPblock_3 | 297.3–328.3 | 10.1021/je049978s | GLOBlit_8564 |\n| 7 | Vapor pressure (GLOBprop_5) | Water | PROPblock_1 | 393.0–413.2 | 10.1021/je050015i | GLOBlit_8573 |\n| 8–9 | VLE mole fraction (GLOBprop_2) | Water | PROPblock_2 | 393.0–413.2 | 10.1021/je050015i | GLOBlit_8573 |\n\n### Chemistry Context\n\n1,3,5-Trioxane (trioxymethylene) is the cyclic trimer of formaldehyde. It is a solid at room temperature (melting point ~62 °C) and is highly soluble in water and common organic solvents. The available ThermoML data reflects its industrial relevance — it is a key intermediate in polyoxymethylene (POM) production. The SLE data with methanol, ethanol, and propan-2-ol (from GLOBlit_8564) and the LLE/VLE data with water (from GLOBlit_8200 and GLOBlit_8573) characterize its phase behavior in these solvents, but transport properties such as viscosity have not been deposited in ThermoML for this compound.",
  "core_claims": [
    "No viscosity data of any kind (dynamic or kinematic, pure-component or binary mixture) was found for 1,3,5-trioxane in the ThermoML database.",
    "The ThermoML database does contain 9 binary-mixture data blocks for 1,3,5-trioxane across 5 publications, covering properties such as mass density, partial molar volume, LLE temperature, SLE mole fraction, vapor pressure, and VLE mole fraction with co-solvents water, methanol, ethanol, and propan-2-ol.",
    "No pure-component data blocks of any property exist for 1,3,5-trioxane in ThermoML."
  ],
  "confidence": "high",
  "sources": [],
  "follow_up_suggestions": [
    "Search for viscosity data for 1,3,5-trioxane in other thermodynamic databases (e.g., DIPPR, Dortmund Data Bank) since ThermoML contains no viscosity records for this compound.",
    "Check whether any ternary or higher-order mixture systems in ThermoML contain viscosity data involving 1,3,5-trioxane.",
    "Consider searching for related cyclic ethers (e.g., 1,3-dioxolane, 1,4-dioxane) which may have viscosity data that could serve as analogs."
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
      "global_id": "GLOBcomp_6",
      "registry_id": "propan-2-ol",
      "name": "propan-2-ol"
    }
  ]
}
