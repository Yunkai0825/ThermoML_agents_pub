# Delegated query run — result

**Question:** Find experimental density (mass density) data for the binary mixture of ethanol (GLOBcomp_2) + water (GLOBcomp_1) at temperature near 298.15 K and mole fraction of ethanol near 0.5. I need specific data points with values, units, and block references.

**Iterations:** 2  |  **Elapsed:** 179.7s  |  **Tools:** 1  |  **Timed out:** False

---

## Answer

{
  "answer": "## Experimental Mass Density of Ethanol + Water at 298.15 K, x_ethanol ≈ 0.5\n\nExperimental mass density data for the binary mixture of **ethanol + water** near equimolar composition at 298.15 K were found in the ThermoML database.\n\n**Source:** DOI [10.1016/j.fluid.2004.11.019](https://doi.org/10.1016/j.fluid.2004.11.019) (GLOBlit_220, block PROPblock_2)\n\n### Key details\n\n- The dataset contains **810 data points** covering temperatures 298.15–348.15 K, pressures 100–40000 kPa, and ethanol mole fractions from 0.003 to 1.\n- **No data point exists at exactly x_ethanol = 0.500**; the closest composition is **x_ethanol = 0.498** (the next nearest above is 0.5501).\n\n### Data at T = 298.15 K, x_ethanol = 0.498\n\n| Pressure (kPa) | Mass Density (kg/m³) |\n|:-:|:-:|\n| 100 | 859.3 |\n| 10 000 | 865.4 |\n| 20 000 | 871.3 |\n| 30 000 | 876.8 |\n| 40 000 | 882.0 |\n\n### Atmospheric-pressure result\n\nAt **T = 298.15 K, P = 100 kPa, and x_ethanol = 0.498**, the mass density is **859.3 kg/m³**.\n\n### Chemistry context\n\nThis value sits between the densities of pure water (~997 kg/m³) and pure ethanol (~785 kg/m³) at the same temperature, but is closer to ethanol's value, reflecting the near-equimolar composition. The ethanol–water system is well known for its **negative excess volume** (volume contraction on mixing), meaning the actual mixture density is slightly higher than what a simple linear (ideal) mixing rule would predict. The systematic increase in density with pressure (859.3 → 882.0 kg/m³ over 100–40 000 kPa) is the expected isothermal compression behavior for a liquid mixture.\n\nNo uncertainty values were reported for these data points in the source block.",
  "core_claims": [
    "Experimental mass density data for ethanol + water near equimolar composition at 298.15 K were found in the ThermoML database from DOI 10.1016/j.fluid.2004.11.019.",
    "The closest available ethanol mole fraction to 0.500 in the dataset is x_ethanol = 0.498.",
    "At T = 298.15 K, P = 100 kPa, and x_ethanol = 0.498, the mass density is 859.3 kg/m³.",
    "At T = 298.15 K and x_ethanol = 0.498, the mass density increases with pressure from 859.3 kg/m³ at 100 kPa to 882.0 kg/m³ at 40 000 kPa.",
    "No uncertainty values were reported for these data points in the source block."
  ],
  "confidence": "high",
  "sources": [
    {
      "doi": "10.1016/j.fluid.2004.11.019",
      "lit_num_id": "GLOBlit_220",
      "block": "PROPblock_2",
      "BLKsubsys_id": null,
      "description": "This block provides mass density data for the ethanol + water binary system covering T = 298.15–348.15 K, P = 100–40000 kPa, and ethanol mole fractions 0.003–1.0 (810 data points). It directly supports the answer's reported density of 859.3 kg/m³ at T = 298.15 K, P = 100 kPa, x_ethanol = 0.498, which falls within the block's density range of 739.4–1012.7 kg/m³."
    }
  ],
  "follow_up_suggestions": [
    "Retrieve excess molar volume data for ethanol+water at 298.15 K to quantify the volume contraction on mixing.",
    "Compare density values from other ThermoML sources for ethanol+water at x_ethanol ≈ 0.5 and 298.15 K to assess inter-laboratory consistency.",
    "Look up density data at exactly x_ethanol = 0.500 from alternative literature sources in ThermoML."
  ],
  "id_catalog_snapshot": []
}

---

## Data Inspections (deterministic evidence ledger)

Hardcoded envelope merge — not agent-authored. 1 entr(ies); verbatim rows below.

- INSP_31ca7f6dfc0e — GLOBlit_220::PROPblock_2 · nearest · 5 rows

```json
[
  {
    "doi": "10.1016/j.fluid.2004.11.019",
    "block_number": "PROPblock_2",
    "table_mode": "nearest",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "pressure_kpa",
      "mole_fraction_<ethanol>",
      "mass_density_kg_m3"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_44",
        "temperature_k": "298.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.498",
        "mass_density_kg_m3": "859.3"
      },
      {
        "BLKpoint_id": "BLKpoint_98",
        "temperature_k": "298.15",
        "pressure_kpa": "10000",
        "mole_fraction_<ethanol>": "0.498",
        "mass_density_kg_m3": "865.4"
      },
      {
        "BLKpoint_id": "BLKpoint_152",
        "temperature_k": "298.15",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0.498",
        "mass_density_kg_m3": "871.3"
      },
      {
        "BLKpoint_id": "BLKpoint_206",
        "temperature_k": "298.15",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0.498",
        "mass_density_kg_m3": "876.8"
      },
      {
        "BLKpoint_id": "BLKpoint_260",
        "temperature_k": "298.15",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0.498",
        "mass_density_kg_m3": "882"
      }
    ],
    "inspection_id": "INSP_31ca7f6dfc0e",
    "lit_num_id": "GLOBlit_220"
  }
]
```
