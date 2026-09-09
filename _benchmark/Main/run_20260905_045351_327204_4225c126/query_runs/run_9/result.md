# Delegated query run — result

**Question:** Find density data for ethanol-water binary mixtures at 1000 K. If no data exists at that temperature, report the closest available temperature range for density measurements of ethanol-water systems.

**Iterations:** 2  |  **Elapsed:** 180.5s  |  **Tools:** 1  |  **Timed out:** False

---

## Answer

{
  "answer": "## Density Data for Ethanol–Water Binary Mixtures at 1000 K\n\n### Data at 1000 K: Not Available\n\nThere is **no density data at or near 1000 K** (≈727 °C) for the ethanol–water system in the ThermoML database. This is physically expected:\n\n- **Ethanol** (C₂H₆O, CAS 64-17-5) has a normal boiling point of ~351.5 K (78.4 °C) and a critical temperature T_c ≈ 514 K.\n- **Water** (H₂O, CAS 7732-18-5) has a normal boiling point of ~373.15 K (100 °C) and a critical temperature T_c ≈ 647 K.\n\nAt 1000 K and moderate pressures, both substances would be supercritical gases with very low density, making experimental liquid-phase density measurements essentially impossible for this mixture.\n\n---\n\n### Closest Available Temperature Range\n\nThe ThermoML database contains **29 data blocks** with mass density measurements for the ethanol + water binary system, totaling approximately **2,924 raw data points** spanning **268.1–618.2 K** (approximately −5 °C to 345 °C).\n\nThe **highest-temperature data** comes from:\n\n- **Source:** DOI 10.1016/j.fluid.2017.09.005 (GLOBlit_2092)\n- **Block:** PROPblock_3\n- **Temperature range:** 523.2–618.2 K (250–345 °C)\n- **Pressure range:** 20,000–40,000 kPa (200–400 bar)\n- **Composition range:** x(ethanol) = 0–1\n- **Overall density range:** 250.4–834.3 kg/m³\n- **72 data points**, liquid phase, measured by vibrating tube method\n\nThese are high-pressure supercritical/compressed-liquid measurements — the elevated pressures keep the mixture in a dense fluid state even above the normal boiling points.\n\n---\n\n### Representative Data at the Highest Available Temperature (618.2 K)\n\n**At 618.2 K, 20,000 kPa:**\n\n| x(ethanol) | ρ (kg/m³) |\n|:----------:|:---------:|\n| 0          | 619.7     |\n| 0.2        | 281.3     |\n| 0.3        | 250.4     |\n| 1.0        | 314.6     |\n\n**At 618.2 K, 30,000 kPa:**\n\n| x(ethanol) | ρ (kg/m³) |\n|:----------:|:---------:|\n| 0          | 656.9     |\n| 0.2        | 501.5     |\n| 0.4        | 437.4     |\n| 0.6        | 420.1     |\n| 1.0        | 423.8     |\n\n**At 618.2 K, 40,000 kPa:**\n\n| x(ethanol) | ρ (kg/m³) |\n|:----------:|:---------:|\n| 0          | 682.3     |\n| 0.2        | 561.0     |\n| 0.4        | 509.1     |\n| 1.0        | 481.2     |\n\n---\n\n### Chemistry Insight\n\nAt 618.2 K and 20,000 kPa, the density drops sharply from pure water (619.7 kg/m³) to intermediate ethanol mole fractions — reaching as low as 250.4 kg/m³ at x(ethanol) = 0.3. This dramatic non-monotonic behavior reflects the proximity to ethanol's critical point (T_c ≈ 514 K), where the fluid becomes highly compressible and density is extremely sensitive to composition. Notably, pure ethanol at this condition (314.6 kg/m³) is actually denser than the x = 0.3 mixture, illustrating the complex interplay of near-critical fluctuations in the mixture.\n\nIncreasing pressure from 20,000 to 40,000 kPa at 618.2 K substantially raises the density across all compositions (e.g., pure water: 619.7 → 682.3 kg/m³; pure ethanol: 314.6 → 481.2 kg/m³), demonstrating the strong pressure dependence characteristic of near-critical and supercritical fluids.\n\n**The maximum available temperature in the ThermoML database for ethanol–water density is 618.2 K — approximately 382 K below the queried 1000 K, with no data to bridge this gap.**",
  "core_claims": [
    "No density data at or near 1000 K for the ethanol–water binary system exists in the ThermoML database; at 1000 K and moderate pressures both substances would be supercritical gases, making liquid-phase density measurements essentially impossible.",
    "The highest-temperature density data available for ethanol + water in ThermoML spans 523.2–618.2 K at 20,000–40,000 kPa, from DOI 10.1016/j.fluid.2017.09.005, comprising 72 data points with an overall density range of 250.4–834.3 kg/m³.",
    "At 618.2 K and 20,000 kPa, density exhibits strongly non-monotonic composition dependence: pure water is 619.7 kg/m³, the mixture at x(ethanol) = 0.3 drops to 250.4 kg/m³, while pure ethanol is 314.6 kg/m³, reflecting near-critical compressibility effects near ethanol's critical temperature (T_c ≈ 514 K).",
    "Increasing pressure from 20,000 to 40,000 kPa at 618.2 K substantially raises density across all compositions (e.g., pure water: 619.7 → 682.3 kg/m³; pure ethanol: 314.6 → 481.2 kg/m³), demonstrating strong pressure dependence characteristic of near-critical and supercritical fluids.",
    "The maximum available temperature in the ThermoML database for ethanol–water density is 618.2 K, approximately 382 K below the queried 1000 K, with no data to bridge this gap."
  ],
  "confidence": "high",
  "sources": [
    {
      "doi": "10.1016/j.fluid.2017.09.005",
      "lit_num_id": "GLOBlit_2092",
      "block": "PROPblock_3",
      "BLKsubsys_id": null,
      "description": "This block provides the highest-temperature mass density data for the ethanol–water binary system in ThermoML, covering 523.2–618.2 K at 20,000–40,000 kPa with 72 data points. The answer correctly uses it to demonstrate that no data exists at 1000 K and to present representative density values at the closest available temperatures (e.g., 250.4–834.3 kg/m³ range)."
    }
  ],
  "follow_up_suggestions": [
    "Search for supercritical density data of ethanol-water mixtures above 618 K in non-ThermoML sources such as NIST WebBook or IAPWS databases.",
    "Investigate whether any ThermoML entries report other thermodynamic properties (e.g., speed of sound, heat capacity) for ethanol-water at temperatures closer to 1000 K under very high pressures.",
    "Query for density data of pure supercritical water or pure supercritical ethanol individually at temperatures approaching 1000 K, which may exist at extreme pressures."
  ],
  "id_catalog_snapshot": [
    {
      "type": "comp",
      "global_id": "GLOBcomp_2",
      "registry_id": "ethanol",
      "name": "ethanol"
    },
    {
      "type": "comp",
      "global_id": "GLOBcomp_1",
      "registry_id": "water",
      "name": "water"
    },
    {
      "type": "prop",
      "global_id": "GLOBprop_1",
      "registry_id": "mass_density_kg_m3",
      "name": "Mass density, kg/m3"
    },
    {
      "type": "lit",
      "global_id": "GLOBlit_2092",
      "registry_id": "2017-ono-kyo-0",
      "name": "10.1016/j.fluid.2017.09.005"
    }
  ]
}

---

## Data Inspections (deterministic evidence ledger)

Hardcoded envelope merge — not agent-authored. 1 entr(ies); verbatim rows below.

- INSP_c6457ac47ddc — GLOBlit_2092::PROPblock_3 · rdp · 41 rows

```json
[
  {
    "doi": "10.1016/j.fluid.2017.09.005",
    "block_number": "PROPblock_3",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "pressure_kpa",
      "mole_fraction_<ethanol>",
      "mass_density_kg_m3"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "523.2",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0",
        "mass_density_kg_m3": "816.1"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "temperature_k": "523.2",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0.2",
        "mass_density_kg_m3": "694.1"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "temperature_k": "523.2",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0.4",
        "mass_density_kg_m3": "622.3"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "temperature_k": "523.2",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0.6",
        "mass_density_kg_m3": "578.5"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "temperature_k": "523.2",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "1",
        "mass_density_kg_m3": "533.1"
      },
      {
        "BLKpoint_id": "BLKpoint_9",
        "temperature_k": "523.2",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0",
        "mass_density_kg_m3": "825.5"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "temperature_k": "523.2",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0.2",
        "mass_density_kg_m3": "713.6"
      },
      {
        "BLKpoint_id": "BLKpoint_13",
        "temperature_k": "523.2",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0.4",
        "mass_density_kg_m3": "650.7"
      },
      {
        "BLKpoint_id": "BLKpoint_14",
        "temperature_k": "523.2",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0.6",
        "mass_density_kg_m3": "612.4"
      },
      {
        "BLKpoint_id": "BLKpoint_16",
        "temperature_k": "523.2",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "1",
        "mass_density_kg_m3": "573.6"
      },
      {
        "BLKpoint_id": "BLKpoint_17",
        "temperature_k": "523.2",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0",
        "mass_density_kg_m3": "834.3"
      },
      {
        "BLKpoint_id": "BLKpoint_20",
        "temperature_k": "523.2",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0.3",
        "mass_density_kg_m3": "694.7"
      },
      {
        "BLKpoint_id": "BLKpoint_22",
        "temperature_k": "523.2",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0.6",
        "mass_density_kg_m3": "636.3"
      },
      {
        "BLKpoint_id": "BLKpoint_24",
        "temperature_k": "523.2",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "1",
        "mass_density_kg_m3": "601.3"
      },
      {
        "BLKpoint_id": "BLKpoint_25",
        "temperature_k": "573.2",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0",
        "mass_density_kg_m3": "734.8"
      },
      {
        "BLKpoint_id": "BLKpoint_27",
        "temperature_k": "573.2",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0.2",
        "mass_density_kg_m3": "585.4"
      },
      {
        "BLKpoint_id": "BLKpoint_29",
        "temperature_k": "573.2",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0.4",
        "mass_density_kg_m3": "494.9"
      },
      {
        "BLKpoint_id": "BLKpoint_30",
        "temperature_k": "573.2",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0.6",
        "mass_density_kg_m3": "446.2"
      },
      {
        "BLKpoint_id": "BLKpoint_32",
        "temperature_k": "573.2",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "1",
        "mass_density_kg_m3": "421.1"
      },
      {
        "BLKpoint_id": "BLKpoint_33",
        "temperature_k": "573.2",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0",
        "mass_density_kg_m3": "750.7"
      },
      {
        "BLKpoint_id": "BLKpoint_35",
        "temperature_k": "573.2",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0.2",
        "mass_density_kg_m3": "621.4"
      },
      {
        "BLKpoint_id": "BLKpoint_37",
        "temperature_k": "573.2",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0.4",
        "mass_density_kg_m3": "553.5"
      },
      {
        "BLKpoint_id": "BLKpoint_38",
        "temperature_k": "573.2",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0.6",
        "mass_density_kg_m3": "517.6"
      },
      {
        "BLKpoint_id": "BLKpoint_40",
        "temperature_k": "573.2",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "1",
        "mass_density_kg_m3": "491.5"
      },
      {
        "BLKpoint_id": "BLKpoint_41",
        "temperature_k": "573.2",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0",
        "mass_density_kg_m3": "764.3"
      },
      {
        "BLKpoint_id": "BLKpoint_43",
        "temperature_k": "573.2",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0.2",
        "mass_density_kg_m3": "647.6"
      },
      {
        "BLKpoint_id": "BLKpoint_45",
        "temperature_k": "573.2",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0.4",
        "mass_density_kg_m3": "587.9"
      },
      {
        "BLKpoint_id": "BLKpoint_48",
        "temperature_k": "573.2",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "1",
        "mass_density_kg_m3": "531"
      },
      {
        "BLKpoint_id": "BLKpoint_49",
        "temperature_k": "618.2",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0",
        "mass_density_kg_m3": "619.7"
      },
      {
        "BLKpoint_id": "BLKpoint_51",
        "temperature_k": "618.2",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0.2",
        "mass_density_kg_m3": "281.3"
      },
      {
        "BLKpoint_id": "BLKpoint_52",
        "temperature_k": "618.2",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0.3",
        "mass_density_kg_m3": "250.4"
      },
      {
        "BLKpoint_id": "BLKpoint_56",
        "temperature_k": "618.2",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "1",
        "mass_density_kg_m3": "314.6"
      },
      {
        "BLKpoint_id": "BLKpoint_57",
        "temperature_k": "618.2",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0",
        "mass_density_kg_m3": "656.9"
      },
      {
        "BLKpoint_id": "BLKpoint_59",
        "temperature_k": "618.2",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0.2",
        "mass_density_kg_m3": "501.5"
      },
      {
        "BLKpoint_id": "BLKpoint_61",
        "temperature_k": "618.2",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0.4",
        "mass_density_kg_m3": "437.4"
      },
      {
        "BLKpoint_id": "BLKpoint_62",
        "temperature_k": "618.2",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0.6",
        "mass_density_kg_m3": "420.1"
      },
      {
        "BLKpoint_id": "BLKpoint_64",
        "temperature_k": "618.2",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "1",
        "mass_density_kg_m3": "423.8"
      },
      {
        "BLKpoint_id": "BLKpoint_65",
        "temperature_k": "618.2",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0",
        "mass_density_kg_m3": "682.3"
      },
      {
        "BLKpoint_id": "BLKpoint_67",
        "temperature_k": "618.2",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0.2",
        "mass_density_kg_m3": "561"
      },
      {
        "BLKpoint_id": "BLKpoint_69",
        "temperature_k": "618.2",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0.4",
        "mass_density_kg_m3": "509.1"
      },
      {
        "BLKpoint_id": "BLKpoint_72",
        "temperature_k": "618.2",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "1",
        "mass_density_kg_m3": "481.2"
      }
    ],
    "inspection_id": "INSP_c6457ac47ddc",
    "lit_num_id": "GLOBlit_2092"
  }
]
```
