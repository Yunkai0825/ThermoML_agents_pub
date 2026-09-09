# Q1.2 — Result

**Prompt:** For an equimolar liquid mixture of hexane + ethanol near 25 °C, which thermophysical properties have been measured?

**Tool calls:** 1  |  **Time:** 294.6s  |  **Iterations:** 2  |  **Timed out:** False

---

## Answer

{
  "answer": "## Thermophysical Properties Measured for an Equimolar Hexane + Ethanol Liquid Mixture near 25 °C\n\nThe ThermoML database contains **7 distinct thermophysical properties** for the binary liquid system **hexane (C₆H₁₄) + ethanol (C₂H₆O)** near 298.15 K (25 °C), reported across **9 data blocks** from **3 literature sources**:\n\n| # | Property | Source DOI | Block |\n|---|----------|-----------|-------|\n| 1 | Excess molar enthalpy (H_E) | 10.1016/j.fluid.2005.08.001 (GLOBlit_294) | PROPblock_5 |\n| 2 | Excess molar volume (V_E) | 10.1016/j.fluid.2005.08.001 (GLOBlit_294) | PROPblock_6 |\n| 3 | Refractive index (n_D, Na D-line) | 10.1016/j.jct.2007.02.008 (GLOBlit_2800) | PROPblock_22 |\n| 4 | Speed of sound | 10.1016/j.jct.2007.02.008 (GLOBlit_2800) | PROPblock_23 |\n| 5 | Mass density | 10.1016/j.jct.2007.02.008 (GLOBlit_2800) | PROPblock_24 |\n| 6 | Surface tension (liquid–gas) | 10.1021/je700215z (GLOBlit_10821) | PROPblock_5 |\n| 7 | Dynamic viscosity | 10.1021/je800925v (GLOBlit_11449) | PROPblock_9 |\n\nA second independent mass density dataset is also available from GLOBlit_11449 (PROPblock_10), covering 273.15–298.15 K.\n\n---\n\n### Representative Values near Equimolar Composition at 298.15 K\n\n| Property | x(ethanol) | Value | Unit | Conditions |\n|----------|-----------|-------|------|------------|\n| Excess molar enthalpy | 0.49 | 0.5637 | kJ/mol | T = 298.15 K, p = 101.325 kPa |\n| Excess molar enthalpy | 0.5191 | 0.5564 | kJ/mol | T = 298.15 K, p = 101.325 kPa |\n| Excess molar volume | 0.4524 | 4.12×10⁻⁷ | m³/mol | T = 298.15 K, p = 101.325 kPa |\n| Excess molar volume | 0.4995 | 4.08×10⁻⁷ | m³/mol | T = 298.15 K, p = 101.325 kPa |\n| Refractive index | 0.4999 | 1.36652 | — | T = 298.15 K, p = 101.0 kPa |\n| Speed of sound | 0.4999 | 1073 | m/s | T = 298.15 K, p = 101.0 kPa |\n| Mass density | 0.4999 | 692.1 | kg/m³ | T = 298.15 K, p = 101.0 kPa |\n\nSurface tension and viscosity data blocks were identified but specific near-equimolar values were not inspected in this query. The surface tension block covers x(ethanol) = 0.0855–0.932 and T = 283.15–313.15 K (77 data points); the viscosity block covers x(ethanol) = 0.0–1.0 and T = 273.15–298.15 K (103 data points).\n\n---\n\n### Chemical Insight\n\nHexane and ethanol form a highly non-ideal mixture. The **positive excess molar enthalpy** (≈ 0.56 kJ/mol near x = 0.5) reflects the endothermic disruption of ethanol's hydrogen-bond network upon dilution with the non-polar alkane. The **positive excess molar volume** (≈ 4.1×10⁻⁷ m³/mol ≈ 0.41 cm³/mol) indicates a volume expansion on mixing, consistent with weaker unlike (ethanol–hexane) interactions compared to the self-associations in pure ethanol. Both excess properties exhibit maxima near the equimolar region, which is characteristic of systems with strong hydrogen-bonding asymmetry.\n\nThe mass density at x(ethanol) ≈ 0.5 (692.1 kg/m³) falls between the pure-component values reported in the same dataset (hexane ≈ 650 kg/m³, ethanol ≈ 789 kg/m³), as do the speed of sound (1073 m/s) and refractive index (1.36652).",
  "core_claims": [
    "The ThermoML database contains 7 distinct thermophysical properties for the binary liquid system hexane + ethanol near 298.15 K: excess molar enthalpy, excess molar volume, refractive index, speed of sound, mass density, surface tension, and dynamic viscosity, reported across 9 data blocks from 3 literature sources.",
    "Near equimolar composition (x(ethanol) ≈ 0.5) at 298.15 K, representative values are: excess molar enthalpy ≈ 0.5637 kJ/mol (at x = 0.49), excess molar volume ≈ 4.08×10⁻⁷ m³/mol (at x = 0.4995), refractive index 1.36652, speed of sound 1073 m/s, and mass density 692.1 kg/m³ (all at x = 0.4999).",
    "The positive excess molar enthalpy (≈ 0.56 kJ/mol near x = 0.5) reflects endothermic disruption of ethanol's hydrogen-bond network upon mixing with non-polar hexane, and the positive excess molar volume (≈ 0.41 cm³/mol) indicates volume expansion on mixing due to weaker unlike interactions compared to ethanol self-association.",
    "Surface tension and dynamic viscosity data blocks were identified but specific near-equimolar values were not inspected; surface tension covers x(ethanol) = 0.0855–0.932 at T = 283.15–313.15 K, and viscosity covers x(ethanol) = 0.0–1.0 at T = 273.15–298.15 K."
  ],
  "confidence": "high",
  "sources": [
    {
      "doi": "10.1016/j.fluid.2005.08.001",
      "lit_num_id": "GLOBlit_294",
      "block": "PROPblock_5",
      "BLKsubsys_id": null,
      "description": "Provides excess molar enthalpy data for the ethanol + hexane binary at 298.15 K across the full composition range, with values up to 0.5795 kJ/mol. The answer quotes H_E ≈ 0.5637 kJ/mol near x = 0.49, consistent with this block's range."
    },
    {
      "doi": "10.1016/j.fluid.2005.08.001",
      "lit_num_id": "GLOBlit_294",
      "block": "PROPblock_6",
      "BLKsubsys_id": null,
      "description": "Provides excess molar volume data for ethanol + hexane at 298.15 K over the full composition range. The answer reports V_E ≈ 4.08×10⁻⁷ m³/mol near equimolar composition, sourced from this block."
    },
    {
      "doi": "10.1016/j.jct.2007.02.008",
      "lit_num_id": "GLOBlit_2800",
      "block": "PROPblock_22",
      "BLKsubsys_id": null,
      "description": "Provides refractive index (Na D-line) data for ethanol + hexane at temperatures including 298.15 K. The answer quotes n_D = 1.36652 at x(ethanol) = 0.4999, which falls within this block's reported range of 1.35725–1.37495."
    },
    {
      "doi": "10.1016/j.jct.2007.02.008",
      "lit_num_id": "GLOBlit_2800",
      "block": "PROPblock_23",
      "BLKsubsys_id": null,
      "description": "Provides speed of sound data for ethanol + hexane at temperatures including 298.15 K. The answer quotes 1073 m/s at x(ethanol) = 0.4999, consistent with this block's range of 1046–1160 m/s."
    },
    {
      "doi": "10.1016/j.jct.2007.02.008",
      "lit_num_id": "GLOBlit_2800",
      "block": "PROPblock_24",
      "BLKsubsys_id": null,
      "description": "Provides mass density data for ethanol + hexane at temperatures including 298.15 K. The answer quotes 692.1 kg/m³ at x(ethanol) = 0.4999, within this block's range of 650.4–789.3 kg/m³."
    },
    {
      "doi": "10.1021/je700215z",
      "lit_num_id": "GLOBlit_10821",
      "block": "PROPblock_5",
      "BLKsubsys_id": null,
      "description": "Provides surface tension data for ethanol + hexane over 283.15–313.15 K and x(ethanol) = 0.0855–0.932. The answer lists surface tension as one of the 7 distinct properties and describes this block's coverage."
    },
    {
      "doi": "10.1021/je800925v",
      "lit_num_id": "GLOBlit_11449",
      "block": "PROPblock_9",
      "BLKsubsys_id": null,
      "description": "Provides dynamic viscosity data for ethanol + hexane over 273.15–298.15 K and full composition range. The answer lists viscosity as one of the 7 distinct properties and describes this block's 103 data points."
    },
    {
      "doi": "10.1021/je800925v",
      "lit_num_id": "GLOBlit_11449",
      "block": "PROPblock_10",
      "BLKsubsys_id": null,
      "description": "Provides a second independent mass density dataset for ethanol + hexane over 273.15–298.15 K. The answer explicitly mentions this block as an additional density source covering that temperature range."
    }
  ],
  "follow_up_suggestions": [
    "Compare the excess molar enthalpy and excess molar volume composition dependence across the full mole-fraction range to identify asymmetry in the mixing behavior.",
    "Retrieve vapor–liquid equilibrium (VLE) data for hexane + ethanol near 25 °C to complement the liquid-phase thermophysical property measurements.",
    "Investigate how the measured speed of sound and density data can be used to derive isentropic compressibility for the hexane + ethanol system."
  ],
  "id_catalog_snapshot": [
    {
      "type": "comp",
      "global_id": "GLOBcomp_12",
      "registry_id": "hexane",
      "name": "hexane"
    },
    {
      "type": "comp",
      "global_id": "GLOBcomp_2",
      "registry_id": "ethanol",
      "name": "ethanol"
    }
  ]
}

---

## Data Inspections (deterministic evidence ledger)

Hardcoded envelope merge — not agent-authored. 5 entr(ies); verbatim rows below.

- INSP_9bcc6ff79750 — GLOBlit_294::PROPblock_5 · nearest · 2 rows
- INSP_4dba237a1a29 — GLOBlit_294::PROPblock_6 · nearest · 2 rows
- INSP_85b1066ecf5a — GLOBlit_2800::PROPblock_22 · nearest · 2 rows
- INSP_96490346a1e2 — GLOBlit_2800::PROPblock_23 · nearest · 2 rows
- INSP_8a8467c370ae — GLOBlit_2800::PROPblock_24 · nearest · 2 rows

```json
[
  {
    "doi": "10.1016/j.fluid.2005.08.001",
    "block_number": "PROPblock_5",
    "table_mode": "nearest",
    "columns": [
      "BLKpoint_id",
      "mole_fraction_<ethanol>",
      "temperature_k",
      "pressure_kpa",
      "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_10",
        "mole_fraction_<ethanol>": "0.49",
        "temperature_k": "298.15",
        "pressure_kpa": "101.325",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.5637"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "mole_fraction_<ethanol>": "0.5191",
        "temperature_k": "298.15",
        "pressure_kpa": "101.325",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.5564"
      }
    ],
    "inspection_id": "INSP_9bcc6ff79750",
    "lit_num_id": "GLOBlit_294"
  },
  {
    "doi": "10.1016/j.fluid.2005.08.001",
    "block_number": "PROPblock_6",
    "table_mode": "nearest",
    "columns": [
      "BLKpoint_id",
      "mole_fraction_<ethanol>",
      "temperature_k",
      "pressure_kpa",
      "excess_molar_volume_m3_mol"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_10",
        "mole_fraction_<ethanol>": "0.4524",
        "temperature_k": "298.15",
        "pressure_kpa": "101.325",
        "excess_molar_volume_m3_mol": "4.12e-07"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "mole_fraction_<ethanol>": "0.4995",
        "temperature_k": "298.15",
        "pressure_kpa": "101.325",
        "excess_molar_volume_m3_mol": "4.08e-07"
      }
    ],
    "inspection_id": "INSP_4dba237a1a29",
    "lit_num_id": "GLOBlit_294"
  },
  {
    "doi": "10.1016/j.jct.2007.02.008",
    "block_number": "PROPblock_22",
    "table_mode": "nearest",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<ethanol>",
      "pressure_kpa",
      "refractive_index_na_dline"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_19",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.3987",
        "pressure_kpa": "101.0",
        "refractive_index_na_dline": "1.36768"
      },
      {
        "BLKpoint_id": "BLKpoint_20",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.4999",
        "pressure_kpa": "101.0",
        "refractive_index_na_dline": "1.36652"
      }
    ],
    "inspection_id": "INSP_85b1066ecf5a",
    "lit_num_id": "GLOBlit_2800"
  },
  {
    "doi": "10.1016/j.jct.2007.02.008",
    "block_number": "PROPblock_23",
    "table_mode": "nearest",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<ethanol>",
      "pressure_kpa",
      "speed_of_sound_m_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_19",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.3987",
        "pressure_kpa": "101.0",
        "speed_of_sound_m_s": "1070"
      },
      {
        "BLKpoint_id": "BLKpoint_20",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.4999",
        "pressure_kpa": "101.0",
        "speed_of_sound_m_s": "1073"
      }
    ],
    "inspection_id": "INSP_96490346a1e2",
    "lit_num_id": "GLOBlit_2800"
  },
  {
    "doi": "10.1016/j.jct.2007.02.008",
    "block_number": "PROPblock_24",
    "table_mode": "nearest",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<ethanol>",
      "pressure_kpa",
      "mass_density_kg_m3"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_19",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.3987",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "681.9"
      },
      {
        "BLKpoint_id": "BLKpoint_20",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.4999",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "692.1"
      }
    ],
    "inspection_id": "INSP_8a8467c370ae",
    "lit_num_id": "GLOBlit_2800"
  }
]
```
