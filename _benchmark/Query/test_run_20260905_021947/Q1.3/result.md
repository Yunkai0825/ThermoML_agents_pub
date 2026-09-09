# Q1.3 — Result

**Prompt:** What density has been measured for an equimolar propan-2-ol + water liquid mixture at 25 °C and atmospheric pressure?

**Tool calls:** 1  |  **Time:** 256.1s  |  **Iterations:** 2  |  **Timed out:** False

---

## Answer

{
  "answer": "## Mass Density of Equimolar Propan-2-ol + Water at 25 °C and Atmospheric Pressure\n\nThe mass density of a binary liquid mixture of propan-2-ol (isopropanol) and water has been measured at 298.15 K (25 °C) and 101.0 kPa (atmospheric pressure) across the full mole-fraction range by Soliman and Marschall (DOI: 10.1021/je700700f, GLOBlit_11042).\n\n### Data Near the Equimolar Composition\n\nThere is no data point at exactly x(propan-2-ol) = 0.5000, but the nearest measured composition is very close. The three points bracketing the equimolar composition are:\n\n| Mole fraction of propan-2-ol | Temperature (K) | Pressure (kPa) | Mass density (kg/m³) |\n|:---:|:---:|:---:|:---:|\n| 0.3992 | 298.15 | 101.0 | 857.7 |\n| **0.4981** | **298.15** | **101.0** | **838.8** |\n| 0.5979 | 298.15 | 101.0 | 823.5 |\n\n**At the nearest-to-equimolar composition of x(propan-2-ol) = 0.4981, the mass density is 838.8 kg/m³** at 298.15 K and 101.0 kPa.\n\n### Chemical Context\n\n- The density decreases monotonically with increasing propan-2-ol mole fraction, from 997.2 kg/m³ for pure water down to 780.7 kg/m³ for pure propan-2-ol at 298.15 K.\n- At the near-equimolar composition, the density (838.8 kg/m³) is notably closer to that of pure propan-2-ol (780.7 kg/m³) than to pure water (997.2 kg/m³). This reflects the significant contribution of the lighter, bulkier alcohol molecules to the mixture volume.\n- The propan-2-ol + water system is well known for exhibiting **negative excess volumes** (volume contraction on mixing), particularly in the water-rich region, due to strong hydrogen-bonding interactions between propan-2-ol and water molecules.\n\n**Source:** DOI 10.1021/je700700f (GLOBlit_11042, PROPblock_17) — 13 data points covering x(propan-2-ol) = 0 to 1 at 298.15 K and 101.0 kPa.",
  "core_claims": [
    "At the nearest-to-equimolar composition of x(propan-2-ol) = 0.4981, the mass density of the propan-2-ol + water binary mixture is 838.8 kg/m³ at 298.15 K and 101.0 kPa, as reported by Soliman and Marschall (DOI: 10.1021/je700700f).",
    "The density of the propan-2-ol + water mixture decreases monotonically with increasing propan-2-ol mole fraction, from 997.2 kg/m³ for pure water to 780.7 kg/m³ for pure propan-2-ol at 298.15 K.",
    "No data point exists at exactly x(propan-2-ol) = 0.5000; the reported value is for the nearest measured composition of 0.4981.",
    "The propan-2-ol + water system is known to exhibit negative excess volumes (volume contraction on mixing), particularly in the water-rich region, due to hydrogen-bonding interactions."
  ],
  "confidence": "high",
  "sources": [
    {
      "doi": "10.1021/je700700f",
      "lit_num_id": "GLOBlit_11042",
      "block": "PROPblock_17",
      "BLKsubsys_id": null,
      "description": "This block provides mass density of the propan-2-ol + water binary system at 298.15 K and 101.0 kPa across 13 compositions (mole fraction 0–1), with density ranging from 780.7 to 997.2 kg/m³. The answer reports the near-equimolar point (x = 0.4981, ρ = 838.8 kg/m³) directly from this block."
    }
  ],
  "follow_up_suggestions": [
    "Compare with excess molar volume data for propan-2-ol + water at 25 °C to quantify the volume contraction on mixing.",
    "Examine temperature dependence of density for the equimolar propan-2-ol + water mixture using additional ThermoML sources.",
    "Look up density data from other literature sources for the same system to assess inter-laboratory agreement."
  ],
  "id_catalog_snapshot": [
    {
      "type": "comp",
      "global_id": "GLOBcomp_6",
      "registry_id": "propan-2-ol",
      "name": "propan-2-ol"
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

Hardcoded envelope merge — not agent-authored. 1 entr(ies); verbatim rows below.

- INSP_ca3d51c69341 — GLOBlit_11042::PROPblock_17 · nearest · 3 rows

```json
[
  {
    "doi": "10.1021/je700700f",
    "block_number": "PROPblock_17",
    "table_mode": "nearest",
    "columns": [
      "BLKpoint_id",
      "mole_fraction_<propan-2-ol>",
      "pressure_kpa",
      "temperature_k",
      "mass_density_kg_m3"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_6",
        "mole_fraction_<propan-2-ol>": "0.3992",
        "pressure_kpa": "101.0",
        "temperature_k": "298.15",
        "mass_density_kg_m3": "857.7"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "mole_fraction_<propan-2-ol>": "0.4981",
        "pressure_kpa": "101.0",
        "temperature_k": "298.15",
        "mass_density_kg_m3": "838.8"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "mole_fraction_<propan-2-ol>": "0.5979",
        "pressure_kpa": "101.0",
        "temperature_k": "298.15",
        "mass_density_kg_m3": "823.5"
      }
    ],
    "inspection_id": "INSP_ca3d51c69341",
    "lit_num_id": "GLOBlit_11042"
  }
]
```
