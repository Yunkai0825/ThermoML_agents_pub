# Q6.4 — Result

**Prompt:** I need the density of pure liquid DMSO at 25 °C for a calculation. If ThermoML does not contain it, use an accepted value from another source.

**Tool calls:** 1  |  **Time:** 202.4s  |  **Iterations:** 2  |  **Timed out:** False

---

## Answer

{
  "answer": "## Density of Pure Liquid DMSO at 25 °C (298.15 K)\n\nThe ThermoML database contains this value from **five independent experimental sources**, all in excellent mutual agreement. Here are the reported values at 298.15 K and near-atmospheric pressure:\n\n| Source (DOI) | Literature | Block | *T* (K) | *P* (kPa) | ρ (kg/m³) |\n|---|---|---|---|---|---|\n| 10.1007/s10765-008-0395-z | GLOBlit_57 | PROPblock_7 | 298.15 | 101.325 | **1095.271** |\n| 10.1007/s10765-009-0648-5 | GLOBlit_86 | PROPblock_4 | 298.15 | 101.0 | **1095.278** |\n| 10.1016/j.fluid.2010.01.002 | GLOBlit_779 | PROPblock_3 | 298.15 | 101.325 | **1095.27** |\n| 10.1016/j.fluid.2011.02.010 | GLOBlit_938 | PROPblock_3 | 298.15 | 101.0 | **1095.37** |\n| 10.1016/j.fluid.2013.05.001 | GLOBlit_1246 | PROPblock_1 | 298.15 | 85.9 | **1095.29** |\n\n### Recommended value for your calculation\n\n> **ρ(DMSO, 25 °C) ≈ 1095.3 kg/m³  (1.0953 g/cm³)**\n\nAll five sources fall in the narrow range **1095.27–1095.37 kg/m³**, so any value in that interval is well-supported. The spread of < 0.1 kg/m³ (among four of the five sources) reflects minor differences in sample purity and exact pressure conditions.\n\n### Temperature dependence near 25 °C\n\nFrom the GLOBlit_86 dataset (DOI 10.1007/s10765-009-0648-5), density decreases nearly linearly with temperature:\n\n| *T* (K) | *P* (kPa) | ρ (kg/m³) |\n|---|---|---|\n| 293.15 | 101.0 | 1100.306 |\n| 298.15 | 101.0 | 1095.278 |\n| 303.15 | 101.0 | 1090.253 |\n\nThis gives a temperature coefficient of approximately **−1.0 kg·m⁻³·K⁻¹** near 25 °C, which is useful if your calculation involves a slightly different temperature.\n\n### Chemistry note\n\nDMSO (CH₃–SO–CH₃, M = 78.13 g/mol) is denser than water at 25 °C because of its relatively high molecular mass and strong dipole–dipole interactions (μ ≈ 3.96 D). The S=O bond creates a compact, highly polar structure that packs efficiently in the liquid phase.",
  "core_claims": [
    "Five independent ThermoML sources report the density of pure liquid DMSO at 298.15 K and near-atmospheric pressure in the narrow range 1095.27–1095.37 kg/m³, yielding a recommended value of ρ(DMSO, 25 °C) ≈ 1095.3 kg/m³ (1.0953 g/cm³).",
    "The spread among four of the five sources is less than 0.1 kg/m³, reflecting minor differences in sample purity and exact pressure conditions.",
    "Near 25 °C, the density of liquid DMSO decreases approximately linearly with temperature, with a temperature coefficient of approximately −1.0 kg·m⁻³·K⁻¹."
  ],
  "confidence": "high",
  "sources": [
    {
      "doi": "10.1007/s10765-008-0395-z",
      "lit_num_id": "GLOBlit_57",
      "block": "PROPblock_7",
      "BLKsubsys_id": null,
      "description": "Provides a single pure DMSO density measurement of 1095.271 kg/m³ at 298.15 K and 101.325 kPa, directly supporting the recommended value of ~1095.3 kg/m³."
    },
    {
      "doi": "10.1007/s10765-009-0648-5",
      "lit_num_id": "GLOBlit_86",
      "block": "PROPblock_4",
      "BLKsubsys_id": null,
      "description": "Contains 5 pure DMSO density datapoints spanning 288.15–308.15 K at 101.0 kPa, with the 298.15 K value of 1095.278 kg/m³ supporting the answer and the temperature series providing the cited temperature coefficient of approximately −1.0 kg·m⁻³·K⁻¹."
    },
    {
      "doi": "10.1016/j.fluid.2010.01.002",
      "lit_num_id": "GLOBlit_779",
      "block": "PROPblock_3",
      "BLKsubsys_id": null,
      "description": "Reports pure DMSO density with a maximum value of 1095.27 kg/m³ at 298.15 K and 101.325 kPa, corroborating the recommended density value."
    },
    {
      "doi": "10.1016/j.fluid.2011.02.010",
      "lit_num_id": "GLOBlit_938",
      "block": "PROPblock_3",
      "BLKsubsys_id": null,
      "description": "Reports pure DMSO density with a maximum value of 1095.37 kg/m³ at 298.15 K and 101.0 kPa, representing the upper bound of the cited 1095.27–1095.37 kg/m³ range."
    },
    {
      "doi": "10.1016/j.fluid.2013.05.001",
      "lit_num_id": "GLOBlit_1246",
      "block": "PROPblock_1",
      "BLKsubsys_id": null,
      "description": "Provides a single pure DMSO density measurement of 1095.29 kg/m³ at 298.15 K and 85.9 kPa, further supporting the recommended value of ~1095.3 kg/m³."
    }
  ],
  "follow_up_suggestions": [
    "Query ThermoML for DMSO density at other temperatures (e.g., 20 °C or 30 °C) to build a temperature-dependent correlation.",
    "Look up DMSO viscosity at 25 °C in ThermoML if your calculation also requires transport properties.",
    "Check for DMSO + water mixture density data in ThermoML if your system involves aqueous DMSO solutions."
  ],
  "id_catalog_snapshot": [
    {
      "type": "comp",
      "global_id": "GLOBcomp_31",
      "registry_id": "dimethyl_sulfoxide",
      "name": "dimethyl sulfoxide"
    }
  ]
}

---

## Data Inspections (deterministic evidence ledger)

Hardcoded envelope merge — not agent-authored. 5 entr(ies); verbatim rows below.

- INSP_66cf20e92a90 — GLOBlit_86::PROPblock_4 · nearest · 3 rows
- INSP_4af5341b9c11 — GLOBlit_57::PROPblock_7 · nearest · 1 rows
- INSP_ae4f04a9ca18 — GLOBlit_779::PROPblock_3 · nearest · 1 rows
- INSP_7d4176a6acb2 — GLOBlit_938::PROPblock_3 · nearest · 1 rows
- INSP_c120fd362f0c — GLOBlit_1246::PROPblock_1 · nearest · 1 rows

```json
[
  {
    "doi": "10.1007/s10765-009-0648-5",
    "block_number": "PROPblock_4",
    "table_mode": "nearest",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "pressure_kpa",
      "mass_density_kg_m3"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_2",
        "temperature_k": "293.15",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "1100.306"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "1095.278"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "temperature_k": "303.15",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "1090.253"
      }
    ],
    "inspection_id": "INSP_66cf20e92a90",
    "lit_num_id": "GLOBlit_86"
  },
  {
    "doi": "10.1007/s10765-008-0395-z",
    "block_number": "PROPblock_7",
    "table_mode": "nearest",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "pressure_kpa",
      "mass_density_kg_m3"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "298.15",
        "pressure_kpa": "101.325",
        "mass_density_kg_m3": "1095.271"
      }
    ],
    "inspection_id": "INSP_4af5341b9c11",
    "lit_num_id": "GLOBlit_57"
  },
  {
    "doi": "10.1016/j.fluid.2010.01.002",
    "block_number": "PROPblock_3",
    "table_mode": "nearest",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "pressure_kpa",
      "mass_density_kg_m3"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "298.15",
        "pressure_kpa": "101.325",
        "mass_density_kg_m3": "1095.27"
      }
    ],
    "inspection_id": "INSP_ae4f04a9ca18",
    "lit_num_id": "GLOBlit_779"
  },
  {
    "doi": "10.1016/j.fluid.2011.02.010",
    "block_number": "PROPblock_3",
    "table_mode": "nearest",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "pressure_kpa",
      "mass_density_kg_m3"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "1095.37"
      }
    ],
    "inspection_id": "INSP_7d4176a6acb2",
    "lit_num_id": "GLOBlit_938"
  },
  {
    "doi": "10.1016/j.fluid.2013.05.001",
    "block_number": "PROPblock_1",
    "table_mode": "nearest",
    "columns": [
      "BLKpoint_id",
      "pressure_kpa",
      "temperature_k",
      "mass_density_kg_m3"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "pressure_kpa": "85.9",
        "temperature_k": "298.15",
        "mass_density_kg_m3": "1095.29"
      }
    ],
    "inspection_id": "INSP_c120fd362f0c",
    "lit_num_id": "GLOBlit_1246"
  }
]
```
