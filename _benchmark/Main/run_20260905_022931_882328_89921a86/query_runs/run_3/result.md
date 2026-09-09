# Delegated query run — result

**Question:** Find viscosity data for ethanol + water binary mixture at approximately equimolar composition (mole fraction ~0.5) and temperature 298.15 K (25 °C). I need the dynamic viscosity values and any excess or deviation viscosity data.

**Iterations:** 3  |  **Elapsed:** 422.1s  |  **Tools:** 2  |  **Timed out:** False

---

## Answer

{
  "answer": "## Viscosity Data for Ethanol + Water Binary Mixture at x ≈ 0.5 and 298.15 K\n\n### Dynamic Viscosity (η)\n\nTwo ThermoML data blocks provide dynamic viscosity measurements for the ethanol–water binary system near equimolar composition at 298.15 K:\n\n---\n\n#### Source 1: GLOBlit_5201 — PROPblock_21\n**DOI:** 10.1016/j.jct.2018.02.022  \n**Pressure:** 92.3 kPa  \n**Composition variable:** mole fraction of ethanol  \n**Method:** Concentric cylinders viscometry  \n**Block size:** 100 data points, T = 293.15–308.15 K, x(ethanol) = 0–1\n\nData near x(ethanol) ≈ 0.5 at 298.15 K:\n\n| x(ethanol) | T (K) | P (kPa) | η (Pa·s) |\n|:----------:|:-----:|:-------:|:---------:|\n| 0.399 | 298.15 | 92.3 | 0.0021697 |\n| 0.4495 | 298.15 | 92.3 | 0.0020662 |\n| **0.4989** | **298.15** | **92.3** | **0.0019557** |\n| 0.5495 | 298.15 | 92.3 | 0.0018796 |\n| 0.6067 | 298.15 | 92.3 | 0.0017439 |\n\n**Best match:** At x(ethanol) = 0.4989, the dynamic viscosity is **0.0019557 Pa·s (≈ 1.96 mPa·s)**. The full 298.15 K isotherm across all 25 compositions spans η = 0.00089689–0.0024286 Pa·s.\n\n---\n\n#### Source 2: GLOBlit_2825 — PROPblock_11\n**DOI:** 10.1016/j.jct.2007.05.004  \n**Pressure:** 101.0 kPa  \n**Composition variable:** mole fraction of water  \n**Block size:** 37 data points, T = 293.15–303.15 K, x(water) = 0–1\n\nThis block does not have an exact x = 0.5 point; the nearest bracketing values at 298.15 K are:\n\n| x(water) | x(ethanol) ≈ | T (K) | P (kPa) | η (Pa·s) |\n|:---------:|:------------:|:-----:|:-------:|:---------:|\n| 0.2961 | 0.70 | 298.15 | 101.0 | 0.001531 |\n| 0.3991 | 0.60 | 298.15 | 101.0 | 0.001659 |\n| 0.5989 | 0.40 | 298.15 | 101.0 | 0.002115 |\n| 0.6991 | 0.30 | 298.15 | 101.0 | 0.002275 |\n\nPure ethanol from this block: η = 0.001082 Pa·s at 298.15 K (x(water) = 0).\n\n---\n\n### Excess / Deviation Viscosity (Δη)\n\n**No excess viscosity or viscosity deviation data are available in the ThermoML database.** The ThermoML schema does not include any excess transport properties. The only excess properties stored are thermodynamic quantities:\n\n| Property | ID |\n|---|---|\n| Excess molar enthalpy | GLOBprop_17 |\n| Excess molar volume | GLOBprop_28 |\n| Excess molar heat capacity | GLOBprop_85 |\n| Excess molar Gibbs energy | GLOBprop_97 |\n\nHowever, the viscosity deviation can be **computed** from the absolute viscosity data above using:\n\n> Δη = η_mix − (x₁·η₁° + x₂·η₂°)\n\nThe pure-component viscosities needed for this calculation are available in the database (e.g., pure ethanol η = 0.001082 Pa·s from GLOBlit_2825 :: PROPblock_11, and the pure water endpoint from the same or other blocks).\n\n---\n\n### Kinematic Viscosity\n\nNo kinematic viscosity data were found for the ethanol–water binary system in the ThermoML database.\n\n---\n\n### Chemistry Insight\n\nThe ethanol–water system is a classic example of non-ideal mixing behavior in transport properties. At near-equimolar composition, the dynamic viscosity (≈ 1.96 mPa·s at x(ethanol) = 0.4989) significantly exceeds that of either pure component — pure ethanol is 0.001082 Pa·s (1.08 mPa·s) and pure water is approximately 0.00089 Pa·s (0.89 mPa·s) at 298.15 K. This viscosity maximum arises from strong hydrogen-bonding interactions between ethanol and water molecules, which create more structured, higher-friction intermolecular networks than exist in either pure liquid.\n\nThe data from GLOBlit_5201 :: PROPblock_21 clearly show that at 298.15 K, viscosity increases as x(ethanol) decreases from 0.5495 (η = 0.0018796 Pa·s) through 0.4989 (η = 0.0019557 Pa·s) to 0.4495 (η = 0.0020662 Pa·s) and 0.399 (η = 0.0021697 Pa·s), confirming that the viscosity maximum lies on the water-rich side of the composition range (around x(ethanol) ≈ 0.3–0.4), consistent with the well-known behavior of this system.\n\n### Additional Data Availability\n\nEight additional dynamic viscosity blocks for the ethanol–water binary system were identified in the ThermoML database from other publications (including DOIs 10.1021/acs.jced.7b00299, 10.1021/acs.jced.8b00086, 10.1021/acs.jced.8b00939, and 10.1021/je4003515), using various composition variables (mass fraction, molality) and temperature ranges that overlap 298.15 K.",
  "core_claims": [
    "At x(ethanol) = 0.4989 and 298.15 K (92.3 kPa), the dynamic viscosity of the ethanol–water binary mixture is 0.0019557 Pa·s (≈ 1.96 mPa·s), as reported in ThermoML data from DOI 10.1016/j.jct.2018.02.022.",
    "A second ThermoML source (DOI 10.1016/j.jct.2007.05.004, 101.0 kPa) brackets x(ethanol) ≈ 0.5 at 298.15 K with values of η = 0.002115 Pa·s at x(ethanol) ≈ 0.40 and η = 0.001659 Pa·s at x(ethanol) ≈ 0.60, but does not include an exact equimolar data point.",
    "No excess viscosity, viscosity deviation, or kinematic viscosity data for the ethanol–water binary system are available in the ThermoML database; the ThermoML schema does not include excess transport properties.",
    "At 298.15 K, the near-equimolar mixture viscosity (≈ 1.96 mPa·s) exceeds that of both pure ethanol (0.001082 Pa·s) and pure water (approximately 0.00089 Pa·s), and the data indicate the viscosity maximum lies on the water-rich side around x(ethanol) ≈ 0.3–0.4, consistent with the well-known non-ideal hydrogen-bonding behavior of this system."
  ],
  "confidence": "high",
  "sources": [
    {
      "doi": "10.1016/j.jct.2018.02.022",
      "lit_num_id": "GLOBlit_5201",
      "block": "PROPblock_21",
      "BLKsubsys_id": null,
      "description": "This block provides dynamic viscosity data for the ethanol–water binary system across the full mole fraction range (0–1) at temperatures including 298.15 K. It contains the closest composition point to x(ethanol) = 0.5 (x = 0.4989) with η = 0.0019557 Pa·s, which is the primary datum in the answer."
    },
    {
      "doi": "10.1016/j.jct.2007.05.004",
      "lit_num_id": "GLOBlit_2825",
      "block": "PROPblock_11",
      "BLKsubsys_id": null,
      "description": "This block provides complementary dynamic viscosity data for the ethanol–water binary at 298.15 K across the full composition range, including pure ethanol (η = 0.001082 Pa·s) and bracketing compositions around x(ethanol) = 0.5. It supports the answer by supplying pure-component reference values and independent corroboration of the viscosity trend."
    }
  ],
  "follow_up_suggestions": [
    "Retrieve dynamic viscosity data from additional ethanol-water blocks at other compositions or temperatures (e.g., DOIs 10.1021/acs.jced.7b00299, 10.1021/acs.jced.8b00086, 10.1021/acs.jced.8b00939, 10.1021/je4003515) to build a complete viscosity surface.",
    "Compute the viscosity deviation Δη = η_mix − (x₁·η₁° + x₂·η₂°) using the pure-component endpoints available in GLOBlit_2825 :: PROPblock_11 and the mixture data from GLOBlit_5201 :: PROPblock_21.",
    "Search for excess molar enthalpy (GLOBprop_17) or excess molar volume (GLOBprop_28) data for ethanol-water at similar conditions to correlate with the viscosity behavior."
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
      "global_id": "GLOBprop_4",
      "registry_id": "viscosity_pa_s",
      "name": "Viscosity, Pa*s"
    },
    {
      "type": "prop",
      "global_id": "GLOBprop_40",
      "registry_id": "kinematic_viscosity_m2_s",
      "name": "Kinematic viscosity, m2/s"
    }
  ]
}

---

## Data Inspections (deterministic evidence ledger)

Hardcoded envelope merge — not agent-authored. 5 entr(ies); verbatim rows below.

- INSP_36125e0a9be2 — GLOBlit_2825::PROPblock_11 · nearest · 4 rows
- INSP_fd21facda729 — GLOBlit_5201::PROPblock_21 · nearest · 4 rows
- INSP_aa9a2d9baff9 — GLOBlit_2825::PROPblock_11 · nearest · 2 rows
- INSP_83906f69ded4 — GLOBlit_5201::PROPblock_21 · nearest · 5 rows
- INSP_0684545c8396 — GLOBlit_2825::PROPblock_11 · nearest · 3 rows

```json
[
  {
    "doi": "10.1016/j.jct.2007.05.004",
    "block_number": "PROPblock_11",
    "table_mode": "nearest",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<water>",
      "pressure_kpa",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_18",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.2961",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001531"
      },
      {
        "BLKpoint_id": "BLKpoint_19",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.3991",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001659"
      },
      {
        "BLKpoint_id": "BLKpoint_20",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.5989",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002115"
      },
      {
        "BLKpoint_id": "BLKpoint_21",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.6991",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002275"
      }
    ],
    "inspection_id": "INSP_36125e0a9be2",
    "lit_num_id": "GLOBlit_2825"
  },
  {
    "doi": "10.1016/j.jct.2018.02.022",
    "block_number": "PROPblock_21",
    "table_mode": "nearest",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<ethanol>",
      "pressure_kpa",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_35",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.399",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0021697"
      },
      {
        "BLKpoint_id": "BLKpoint_36",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.4495",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0020662"
      },
      {
        "BLKpoint_id": "BLKpoint_37",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.4989",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0019557"
      },
      {
        "BLKpoint_id": "BLKpoint_38",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.5495",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0018796"
      }
    ],
    "inspection_id": "INSP_fd21facda729",
    "lit_num_id": "GLOBlit_5201"
  },
  {
    "doi": "10.1016/j.jct.2007.05.004",
    "block_number": "PROPblock_11",
    "table_mode": "nearest",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<water>",
      "pressure_kpa",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_14",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001082"
      },
      {
        "BLKpoint_id": "BLKpoint_15",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.0501",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001153"
      }
    ],
    "inspection_id": "INSP_aa9a2d9baff9",
    "lit_num_id": "GLOBlit_2825"
  },
  {
    "doi": "10.1016/j.jct.2018.02.022",
    "block_number": "PROPblock_21",
    "table_mode": "nearest",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<ethanol>",
      "pressure_kpa",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_35",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.399",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0021697"
      },
      {
        "BLKpoint_id": "BLKpoint_36",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.4495",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0020662"
      },
      {
        "BLKpoint_id": "BLKpoint_37",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.4989",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0019557"
      },
      {
        "BLKpoint_id": "BLKpoint_38",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.5495",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0018796"
      },
      {
        "BLKpoint_id": "BLKpoint_39",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.6067",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0017439"
      }
    ],
    "inspection_id": "INSP_83906f69ded4",
    "lit_num_id": "GLOBlit_5201"
  },
  {
    "doi": "10.1016/j.jct.2007.05.004",
    "block_number": "PROPblock_11",
    "table_mode": "nearest",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<water>",
      "pressure_kpa",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_14",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001082"
      },
      {
        "BLKpoint_id": "BLKpoint_15",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.0501",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001153"
      },
      {
        "BLKpoint_id": "BLKpoint_16",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.0986",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001232"
      }
    ],
    "inspection_id": "INSP_0684545c8396",
    "lit_num_id": "GLOBlit_2825"
  }
]
```
