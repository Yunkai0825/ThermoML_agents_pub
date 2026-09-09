# Delegated query run — result

**Question:** Find experimental data for binary mixtures of ethanol and water near room temperature (around 293-303 K). I need excess molar volume, excess molar enthalpy, and any other excess or mixing properties available. Return DOIs, block numbers, compound names, property types, temperature ranges, and composition ranges.

**Iterations:** 5  |  **Elapsed:** 893.0s  |  **Tools:** 4  |  **Timed out:** False

---

## Answer

{
  "answer": "# Ethanol + Water Binary Mixture: Thermodynamic Data near 298 K from the ThermoML Database\n\n## Overview\n\nThe ThermoML database contains extensive experimental data for the ethanol + water binary system in the 293–303 K temperature window: **10 distinct property types** across **39 data blocks** from **26 publications**, totaling **3,263 matching data points**.\n\n---\n\n## 1. Excess Molar Enthalpy (H^E)\n\nThree verified data blocks provide excess molar enthalpy measurements at 298.15 K.\n\n### Source 1: DOI 10.1016/j.fluid.2007.06.007 (GLOBlit_528)\n\nTwo complementary dilute-solution blocks measured by Calvet calorimetry at 298.15 K and 101.0 kPa.\n\n**Block PROPblock_1 — Dilute ethanol in water** (15 data points)\n\n| x(ethanol) | T (K) | P (kPa) | H^E (kJ/mol) |\n|---|---|---|---|\n| 0.000102 | 298.15 | 101.0 | −0.00104 |\n| 0.000206 | 298.15 | 101.0 | −0.00208 |\n| 0.000308 | 298.15 | 101.0 | −0.00312 |\n| 0.000516 | 298.15 | 101.0 | −0.00518 |\n| 0.000619 | 298.15 | 101.0 | −0.00621 |\n| 0.000723 | 298.15 | 101.0 | −0.00722 |\n| 0.000827 | 298.15 | 101.0 | −0.00826 |\n| 0.000931 | 298.15 | 101.0 | −0.00927 |\n| 0.001034 | 298.15 | 101.0 | −0.0103 |\n| 0.001241 | 298.15 | 101.0 | −0.01233 |\n| 0.001345 | 298.15 | 101.0 | −0.01334 |\n| 0.001551 | 298.15 | 101.0 | −0.01537 |\n\n- Composition range: x(ethanol) = 0.000102–0.001551\n- H^E range: −0.01537 to −0.00104 kJ/mol\n\n**Block PROPblock_2 — Dilute water in ethanol** (15 data points)\n\n| x(water) | T (K) | P (kPa) | H^E (kJ/mol) |\n|---|---|---|---|\n| 0.001021 | 298.15 | 101.0 | −0.00212 |\n| 0.00205 | 298.15 | 101.0 | −0.00424 |\n| 0.004102 | 298.15 | 101.0 | −0.00835 |\n| 0.006155 | 298.15 | 101.0 | −0.01238 |\n| 0.007179 | 298.15 | 101.0 | −0.01437 |\n| 0.010239 | 298.15 | 101.0 | −0.02023 |\n| 0.011252 | 298.15 | 101.0 | −0.02213 |\n| 0.012264 | 298.15 | 101.0 | −0.02405 |\n| 0.013276 | 298.15 | 101.0 | −0.0259 |\n| 0.014283 | 298.15 | 101.0 | −0.02777 |\n| 0.015286 | 298.15 | 101.0 | −0.02961 |\n\n- Composition range: x(water) = 0.001021–0.015286\n- H^E range: −0.02961 to −0.00212 kJ/mol\n\n### Source 2: DOI 10.1016/j.tca.2017.05.023 (GLOBlit_6377)\n\n**Block PROPblock_1** — Flow calorimetry, single data point at moderate composition:\n\n| x(ethanol) | T (K) | P (kPa) | H^E (kJ/mol) |\n|---|---|---|---|\n| 0.102 | 298.15 | 100 | −0.70659 |\n\n**Chemistry insight:** All H^E values are **negative**, confirming that mixing ethanol and water at 298.15 K is exothermic. In the dilute regime, |H^E| is on the order of 0.001–0.03 kJ/mol, but at x(ethanol) = 0.102 it already reaches −0.707 kJ/mol, consistent with the well-known strongly exothermic mixing behaviour where the H^E minimum occurs near x(ethanol) ≈ 0.2–0.3. The nearly linear H^E–composition relationship in the dilute regime reflects the partial molar excess enthalpy at infinite dilution.\n\n---\n\n## 2. Excess Molar Volume (V^E)\n\n**No data found in the ThermoML database.** Searches were conducted with and without temperature restrictions and across both declared binary studies and binary subsystems in multicomponent datasets — no V^E data blocks exist for ethanol + water at any temperature or composition. However, the extensive mass density data (17 blocks; see below) could in principle be used to compute V^E.\n\n---\n\n## 3. Other Properties Available (293–303 K)\n\n| Property | Unit | Number of Blocks |\n|---|---|---|\n| Mass density | kg/m³ | 17 |\n| Dynamic viscosity | Pa·s | 7 |\n| Speed of sound | m/s | 3 |\n| Refractive index (Na D-line) | — | 3 |\n| Thermal conductivity | W/(m·K) | 2 |\n| Henry's Law constant (mole fraction) | kPa | 2 |\n| Excess molar enthalpy | kJ/mol | 2 |\n| Vapor or sublimation pressure | kPa | 1 |\n| Surface tension (liquid–gas) | N/m | 1 |\n| Activity coefficient | — | 1 |\n\n### Top 5 Sources by Number of Data Points (293–303 K)\n\n| Literature ID | DOI | Property Types | Matching Points |\n|---|---|---|---|\n| GLOBlit_220 | 10.1016/j.fluid.2004.11.019 | 1 | 810 |\n| GLOBlit_2432 | 10.1016/j.jct.2004.07.019 | 1 | 565 |\n| GLOBlit_5201 | 10.1016/j.jct.2018.02.022 | 3 | 496 |\n| GLOBlit_11136 | 10.1021/je800150h | 2 | 216 |\n| GLOBlit_9006 | 10.1021/je060335h | 1 | 164 |\n\n### Representative Data: Speed of Sound (GLOBlit_5201, PROPblock_20)\n\nDOI 10.1016/j.jct.2018.02.022 — 152 data points at 92.3 kPa and 3.0 MHz, T = 293.15–308.15 K, x(ethanol) = 0–1. Selected values at 298.15 K:\n\n| x(ethanol) | T (K) | P (kPa) | Speed of sound (m/s) |\n|---|---|---|---|\n| 0 | 298.15 | 92.3 | 1496.99 |\n| 0.0997 | 298.15 | 92.3 | 1618.97 |\n| 0.1497 | 298.15 | 92.3 | 1600.11 |\n| 0.3507 | 298.15 | 92.3 | 1426.17 |\n| 0.5002 | 298.15 | 92.3 | 1337.91 |\n| 1 | 298.15 | 92.3 | 1143.50 |\n\nThe speed of sound exhibits a pronounced **non-monotonic maximum** near x(ethanol) ≈ 0.1, reaching 1618.97 m/s — well above pure water (1496.99 m/s) or pure ethanol (1143.50 m/s). This reflects the strong intermolecular interactions and structural reorganization of the hydrogen-bond network in ethanol–water mixtures.\n\n### Representative Data: Mass Density (GLOBlit_220, PROPblock_2)\n\nDOI 10.1016/j.fluid.2004.11.019 — 810 data points, T = 298.15–348.15 K, P = 100–40,000 kPa, x(ethanol) = 0.003–1.0. Density range: 739.4–1012.7 kg/m³.\n\n---\n\n## Summary of Key Findings\n\n| Property | Available? | Sources (DOIs) | Key Observations |\n|---|---|---|---|\n| Excess molar enthalpy (H^E) | ✅ Yes (3 blocks, 31 points) | 10.1016/j.fluid.2007.06.007, 10.1016/j.tca.2017.05.023 | All negative (exothermic mixing); −0.707 kJ/mol at x(EtOH) = 0.102 |\n| Excess molar volume (V^E) | ❌ Not in database | — | Not directly reported; could be derived from density data |\n| Mass density | ✅ Yes (17 blocks) | Multiple (see above) | 739.4–1012.7 kg/m³ across full composition range |\n| Dynamic viscosity | ✅ Yes (7 blocks) | Multiple | — |\n| Speed of sound | ✅ Yes (3 blocks) | 10.1016/j.jct.2018.02.022 | Maximum ~1619 m/s near x(EtOH) ≈ 0.1 at 298.15 K |\n| Refractive index | ✅ Yes (3 blocks) | Multiple | — |\n| Thermal conductivity | ✅ Yes (2 blocks) | Multiple | — |\n| Henry's Law constant | ✅ Yes (2 blocks) | Multiple | — |\n| Vapor pressure | ✅ Yes (1 block) | — | — |\n| Surface tension | ✅ Yes (1 block) | — | — |\n| Activity coefficient | ✅ Yes (1 block) | — | — |\n\n**Chemistry context:** The ethanol–water system is one of the most studied binary mixtures in thermodynamics. The strongly negative H^E values reflect the disruption and reorganization of the hydrogen-bond network upon mixing: water's tetrahedral H-bond structure is partially broken as ethanol molecules are incorporated, releasing energy. The non-monotonic speed of sound (maximum near x ≈ 0.1) and the well-known viscosity maximum near x(ethanol) ≈ 0.15–0.2 both point to the formation of microheterogeneous structures — ethanol-rich and water-rich clusters — that characterize this system at intermediate compositions. While V^E is not directly stored in ThermoML, the 17 mass density blocks spanning the full composition range provide the raw data needed to compute it.",
  "core_claims": [
    "The ThermoML database contains extensive experimental data for the ethanol + water binary system in the 293–303 K window: 10 distinct property types across 39 data blocks from 26 publications, totaling 3,263 matching data points.",
    "Three verified data blocks provide excess molar enthalpy (H^E) measurements at 298.15 K; all H^E values are negative (exothermic mixing), ranging from −0.00104 kJ/mol at x(ethanol) = 0.000102 to −0.70659 kJ/mol at x(ethanol) = 0.102.",
    "Excess molar volume (V^E) is not directly reported in the ThermoML database for ethanol + water at any temperature or composition, though 17 mass density data blocks spanning the full composition range could in principle be used to compute it.",
    "Speed of sound at 298.15 K exhibits a non-monotonic maximum near x(ethanol) ≈ 0.1, reaching 1618.97 m/s — above pure water (1496.99 m/s) and pure ethanol (1143.50 m/s) — reflecting strong intermolecular interactions and hydrogen-bond network reorganization.",
    "Mass density data span 739.4–1012.7 kg/m³ across the full composition range at temperatures from 298.15–348.15 K and pressures from 100–40,000 kPa (17 blocks)."
  ],
  "confidence": "high",
  "sources": [
    {
      "doi": "10.1016/j.fluid.2007.06.007",
      "lit_num_id": "GLOBlit_528",
      "block": "PROPblock_1",
      "BLKsubsys_id": null,
      "description": "Provides 15 dilute-ethanol-in-water excess molar enthalpy data points at 298.15 K and 101.0 kPa, with H^E ranging from −0.01537 to −0.00104 kJ/mol, directly quoted in the answer's Section 1 tables."
    },
    {
      "doi": "10.1016/j.fluid.2007.06.007",
      "lit_num_id": "GLOBlit_528",
      "block": "PROPblock_2",
      "BLKsubsys_id": null,
      "description": "Provides 15 dilute-water-in-ethanol excess molar enthalpy data points at 298.15 K and 101.0 kPa, with H^E ranging from −0.02961 to −0.00212 kJ/mol, directly quoted in the answer's Section 1 tables."
    },
    {
      "doi": "10.1016/j.tca.2017.05.023",
      "lit_num_id": "GLOBlit_6377",
      "block": "PROPblock_1",
      "BLKsubsys_id": null,
      "description": "Provides a single excess molar enthalpy measurement of −0.70659 kJ/mol at x(ethanol) = 0.102 and 298.15 K, directly quoted in the answer to illustrate the magnitude of exothermic mixing at moderate composition."
    },
    {
      "doi": "10.1016/j.jct.2018.02.022",
      "lit_num_id": "GLOBlit_5201",
      "block": "PROPblock_20",
      "BLKsubsys_id": null,
      "description": "Provides 152 speed-of-sound data points for ethanol + water at 293.15–308.15 K across the full composition range, with representative 298.15 K values quoted in the answer showing the non-monotonic maximum near x(ethanol) ≈ 0.1."
    },
    {
      "doi": "10.1016/j.fluid.2004.11.019",
      "lit_num_id": "GLOBlit_220",
      "block": "PROPblock_2",
      "BLKsubsys_id": null,
      "description": "Provides 810 mass density data points for ethanol + water spanning 298.15–348.15 K and 100–40000 kPa across the full composition range, cited in the answer as the largest single data source and as representative density data."
    }
  ],
  "follow_up_suggestions": [
    "Compute excess molar volume (V^E) from the 17 mass density blocks available for ethanol + water, using pure-component molar volumes at matching T and P.",
    "Search for excess molar heat capacity (Cp^E) data for ethanol + water to complement the H^E measurements.",
    "Retrieve the activity coefficient and vapor pressure blocks to examine vapor–liquid equilibrium behavior near 298 K.",
    "Extend the temperature range beyond 293–303 K to study the temperature dependence of H^E and density for ethanol + water mixtures."
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
    }
  ]
}

---

## Data Inspections (deterministic evidence ledger)

Hardcoded envelope merge — not agent-authored. 4 entr(ies); verbatim rows below.

- INSP_e0e7d5bc600c — GLOBlit_528::PROPblock_1 · rdp · 12 rows
- INSP_b146b18bf0c3 — GLOBlit_528::PROPblock_2 · rdp · 11 rows
- INSP_b04400bcb35b — GLOBlit_6377::PROPblock_1 · complete · 1 rows
- INSP_d2c2205c2128 — GLOBlit_5201::PROPblock_20 · rdp · 27 rows

```json
[
  {
    "doi": "10.1016/j.fluid.2007.06.007",
    "block_number": "PROPblock_1",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "mole_fraction_<ethanol>",
      "temperature_k",
      "pressure_kpa",
      "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "mole_fraction_<ethanol>": "0.000102",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.00104"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "mole_fraction_<ethanol>": "0.000206",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.00208"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "mole_fraction_<ethanol>": "0.000308",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.00312"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "mole_fraction_<ethanol>": "0.000516",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.00518"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "mole_fraction_<ethanol>": "0.000619",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.00621"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "mole_fraction_<ethanol>": "0.000723",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.00722"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "mole_fraction_<ethanol>": "0.000827",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.00826"
      },
      {
        "BLKpoint_id": "BLKpoint_9",
        "mole_fraction_<ethanol>": "0.000931",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.00927"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "mole_fraction_<ethanol>": "0.001034",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.0103"
      },
      {
        "BLKpoint_id": "BLKpoint_12",
        "mole_fraction_<ethanol>": "0.001241",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.01233"
      },
      {
        "BLKpoint_id": "BLKpoint_13",
        "mole_fraction_<ethanol>": "0.001345",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.01334"
      },
      {
        "BLKpoint_id": "BLKpoint_15",
        "mole_fraction_<ethanol>": "0.001551",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.01537"
      }
    ],
    "inspection_id": "INSP_e0e7d5bc600c",
    "lit_num_id": "GLOBlit_528"
  },
  {
    "doi": "10.1016/j.fluid.2007.06.007",
    "block_number": "PROPblock_2",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "mole_fraction_<water>",
      "temperature_k",
      "pressure_kpa",
      "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "mole_fraction_<water>": "0.001021",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.00212"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "mole_fraction_<water>": "0.00205",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.00424"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "mole_fraction_<water>": "0.004102",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.00835"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "mole_fraction_<water>": "0.006155",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.01238"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "mole_fraction_<water>": "0.007179",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.01437"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "mole_fraction_<water>": "0.010239",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.02023"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "mole_fraction_<water>": "0.011252",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.02213"
      },
      {
        "BLKpoint_id": "BLKpoint_12",
        "mole_fraction_<water>": "0.012264",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.02405"
      },
      {
        "BLKpoint_id": "BLKpoint_13",
        "mole_fraction_<water>": "0.013276",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.0259"
      },
      {
        "BLKpoint_id": "BLKpoint_14",
        "mole_fraction_<water>": "0.014283",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.02777"
      },
      {
        "BLKpoint_id": "BLKpoint_15",
        "mole_fraction_<water>": "0.015286",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.02961"
      }
    ],
    "inspection_id": "INSP_b146b18bf0c3",
    "lit_num_id": "GLOBlit_528"
  },
  {
    "doi": "10.1016/j.tca.2017.05.023",
    "block_number": "PROPblock_1",
    "table_mode": "complete",
    "columns": [
      "BLKpoint_id",
      "mole_fraction_<ethanol>",
      "pressure_kpa",
      "temperature_k",
      "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "mole_fraction_<ethanol>": "0.102",
        "pressure_kpa": "100",
        "temperature_k": "298.15",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.70659"
      }
    ],
    "inspection_id": "INSP_b04400bcb35b",
    "lit_num_id": "GLOBlit_6377"
  },
  {
    "doi": "10.1016/j.jct.2018.02.022",
    "block_number": "PROPblock_20",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<ethanol>",
      "pressure_kpa",
      "frequency_mhz",
      "speed_of_sound_m_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "293.15",
        "mole_fraction_<ethanol>": "0.0024",
        "pressure_kpa": "92.3",
        "frequency_mhz": "3.0",
        "speed_of_sound_m_s": "1487.73"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "temperature_k": "293.15",
        "mole_fraction_<ethanol>": "0.0707",
        "pressure_kpa": "92.3",
        "frequency_mhz": "3.0",
        "speed_of_sound_m_s": "1604.25"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "temperature_k": "293.15",
        "mole_fraction_<ethanol>": "0.0997",
        "pressure_kpa": "92.3",
        "frequency_mhz": "3.0",
        "speed_of_sound_m_s": "1625.74"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "temperature_k": "293.15",
        "mole_fraction_<ethanol>": "0.1294",
        "pressure_kpa": "92.3",
        "frequency_mhz": "3.0",
        "speed_of_sound_m_s": "1623.76"
      },
      {
        "BLKpoint_id": "BLKpoint_15",
        "temperature_k": "293.15",
        "mole_fraction_<ethanol>": "0.2998",
        "pressure_kpa": "92.3",
        "frequency_mhz": "3.0",
        "speed_of_sound_m_s": "1478.23"
      },
      {
        "BLKpoint_id": "BLKpoint_18",
        "temperature_k": "293.15",
        "mole_fraction_<ethanol>": "0.4514",
        "pressure_kpa": "92.3",
        "frequency_mhz": "3.0",
        "speed_of_sound_m_s": "1379.03"
      },
      {
        "BLKpoint_id": "BLKpoint_22",
        "temperature_k": "293.15",
        "mole_fraction_<ethanol>": "0.6503",
        "pressure_kpa": "92.3",
        "frequency_mhz": "3.0",
        "speed_of_sound_m_s": "1288.48"
      },
      {
        "BLKpoint_id": "BLKpoint_46",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.0997",
        "pressure_kpa": "92.3",
        "frequency_mhz": "3.0",
        "speed_of_sound_m_s": "1618.97"
      },
      {
        "BLKpoint_id": "BLKpoint_48",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.1497",
        "pressure_kpa": "92.3",
        "frequency_mhz": "3.0",
        "speed_of_sound_m_s": "1600.11"
      },
      {
        "BLKpoint_id": "BLKpoint_52",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.3507",
        "pressure_kpa": "92.3",
        "frequency_mhz": "3.0",
        "speed_of_sound_m_s": "1426.17"
      },
      {
        "BLKpoint_id": "BLKpoint_55",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.5002",
        "pressure_kpa": "92.3",
        "frequency_mhz": "3.0",
        "speed_of_sound_m_s": "1337.91"
      },
      {
        "BLKpoint_id": "BLKpoint_81",
        "temperature_k": "303.15",
        "mole_fraction_<ethanol>": "0.0904",
        "pressure_kpa": "92.3",
        "frequency_mhz": "3.0",
        "speed_of_sound_m_s": "1610.77"
      },
      {
        "BLKpoint_id": "BLKpoint_83",
        "temperature_k": "303.15",
        "mole_fraction_<ethanol>": "0.1294",
        "pressure_kpa": "92.3",
        "frequency_mhz": "3.0",
        "speed_of_sound_m_s": "1602.74"
      },
      {
        "BLKpoint_id": "BLKpoint_88",
        "temperature_k": "303.15",
        "mole_fraction_<ethanol>": "0.3507",
        "pressure_kpa": "92.3",
        "frequency_mhz": "3.0",
        "speed_of_sound_m_s": "1411.8"
      },
      {
        "BLKpoint_id": "BLKpoint_91",
        "temperature_k": "303.15",
        "mole_fraction_<ethanol>": "0.5002",
        "pressure_kpa": "92.3",
        "frequency_mhz": "3.0",
        "speed_of_sound_m_s": "1322.3"
      },
      {
        "BLKpoint_id": "BLKpoint_116",
        "temperature_k": "308.15",
        "mole_fraction_<ethanol>": "0.0801",
        "pressure_kpa": "92.3",
        "frequency_mhz": "3.0",
        "speed_of_sound_m_s": "1602.67"
      },
      {
        "BLKpoint_id": "BLKpoint_119",
        "temperature_k": "308.15",
        "mole_fraction_<ethanol>": "0.1294",
        "pressure_kpa": "92.3",
        "frequency_mhz": "3.0",
        "speed_of_sound_m_s": "1592.26"
      },
      {
        "BLKpoint_id": "BLKpoint_124",
        "temperature_k": "308.15",
        "mole_fraction_<ethanol>": "0.3507",
        "pressure_kpa": "92.3",
        "frequency_mhz": "3.0",
        "speed_of_sound_m_s": "1397.33"
      },
      {
        "BLKpoint_id": "BLKpoint_127",
        "temperature_k": "308.15",
        "mole_fraction_<ethanol>": "0.5002",
        "pressure_kpa": "92.3",
        "frequency_mhz": "3.0",
        "speed_of_sound_m_s": "1306.71"
      },
      {
        "BLKpoint_id": "BLKpoint_145",
        "temperature_k": "293.15",
        "mole_fraction_<ethanol>": "0",
        "pressure_kpa": "92.3",
        "frequency_mhz": "3.0",
        "speed_of_sound_m_s": "1482.78"
      },
      {
        "BLKpoint_id": "BLKpoint_146",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0",
        "pressure_kpa": "92.3",
        "frequency_mhz": "3.0",
        "speed_of_sound_m_s": "1496.99"
      },
      {
        "BLKpoint_id": "BLKpoint_147",
        "temperature_k": "303.15",
        "mole_fraction_<ethanol>": "0",
        "pressure_kpa": "92.3",
        "frequency_mhz": "3.0",
        "speed_of_sound_m_s": "1509.32"
      },
      {
        "BLKpoint_id": "BLKpoint_148",
        "temperature_k": "308.15",
        "mole_fraction_<ethanol>": "0",
        "pressure_kpa": "92.3",
        "frequency_mhz": "3.0",
        "speed_of_sound_m_s": "1519.89"
      },
      {
        "BLKpoint_id": "BLKpoint_149",
        "temperature_k": "293.15",
        "mole_fraction_<ethanol>": "1",
        "pressure_kpa": "92.3",
        "frequency_mhz": "3.0",
        "speed_of_sound_m_s": "1160.65"
      },
      {
        "BLKpoint_id": "BLKpoint_150",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "1",
        "pressure_kpa": "92.3",
        "frequency_mhz": "3.0",
        "speed_of_sound_m_s": "1143.5"
      },
      {
        "BLKpoint_id": "BLKpoint_151",
        "temperature_k": "303.15",
        "mole_fraction_<ethanol>": "1",
        "pressure_kpa": "92.3",
        "frequency_mhz": "3.0",
        "speed_of_sound_m_s": "1126.44"
      },
      {
        "BLKpoint_id": "BLKpoint_152",
        "temperature_k": "308.15",
        "mole_fraction_<ethanol>": "1",
        "pressure_kpa": "92.3",
        "frequency_mhz": "3.0",
        "speed_of_sound_m_s": "1109.59"
      }
    ],
    "inspection_id": "INSP_d2c2205c2128",
    "lit_num_id": "GLOBlit_5201"
  }
]
```
