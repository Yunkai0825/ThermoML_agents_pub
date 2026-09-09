# Q5.1 — Result

**Prompt:** Do you have viscosity data for IPA + water?

**Tool calls:** 3  |  **Time:** 396.1s  |  **Iterations:** 4  |  **Timed out:** False

---

## Answer

{
  "answer": "Yes! The ThermoML database contains dynamic viscosity data for binary isopropanol (propan-2-ol) + water mixtures from **two literature sources**, totaling **25 data points**.\n\n---\n\n### Source 1 — DOI: 10.1016/j.jct.2019.105880\n\n- **Measurement method:** Falling/rolling sphere viscometry\n- **Temperature range:** 288.15–303.15 K\n- **Pressure:** 100.0 kPa\n- **Composition basis:** Mass fraction of IPA (w = 0.1, 0.2, 0.3)\n- **12 data points**\n\n| Temperature (K) | w(IPA) | Viscosity (Pa·s) |\n|:---:|:---:|:---:|\n| 288.15 | 0.1 | 0.001936 |\n| 288.15 | 0.2 | 0.003087 |\n| 288.15 | 0.3 | 0.004014 |\n| 293.15 | 0.1 | 0.001633 |\n| 293.15 | 0.2 | 0.002485 |\n| 293.15 | 0.3 | 0.003172 |\n| 298.15 | 0.1 | 0.001395 |\n| 298.15 | 0.2 | 0.002045 |\n| 298.15 | 0.3 | 0.002555 |\n| 303.15 | 0.1 | 0.001208 |\n| 303.15 | 0.2 | 0.00171 |\n| 303.15 | 0.3 | 0.002105 |\n\n---\n\n### Source 2 — DOI: 10.1021/je700700f\n\n- **Measurement method:** Capillary Ubbelohde viscometry\n- **Temperature:** 298.15 K (isothermal)\n- **Pressure:** 101.0 kPa\n- **Composition basis:** Mole fraction of IPA (x = 0 to 1, full range)\n- **13 data points** (10 shown below via shape-preserving subset)\n\n| x(IPA) | Viscosity (Pa·s) |\n|:---:|:---:|\n| 0 | 0.00089 |\n| 0.0491 | 0.001718 |\n| 0.1008 | 0.002495 |\n| 0.2011 | 0.003038 |\n| 0.2994 | 0.003087 |\n| 0.3992 | 0.002924 |\n| 0.6987 | 0.002274 |\n| 0.7993 | 0.002153 |\n| 0.8998 | 0.002073 |\n| 1 | 0.002082 |\n\n---\n\n### Key Chemistry Insights\n\n1. **Non-monotonic viscosity maximum:** The full-composition data at 298.15 K (Source 2) beautifully illustrate the well-known anomalous viscosity behavior of the IPA–water system. The viscosity rises sharply from 0.00089 Pa·s for pure water to a maximum of 0.003087 Pa·s near x(IPA) ≈ 0.30, then gradually decreases to 0.002082 Pa·s for pure IPA. This maximum — roughly 3.5× the viscosity of pure water and 1.5× that of pure IPA — is attributed to enhanced hydrogen-bonding network restructuring and microheterogeneity in the alcohol–water mixture at intermediate compositions.\n\n2. **Temperature dependence:** Source 1 shows that viscosity decreases with increasing temperature at all three mass fractions studied (w = 0.1–0.3), consistent with thermally activated flow. For example, at w = 0.3, viscosity drops from 0.004014 Pa·s at 288.15 K to 0.002105 Pa·s at 303.15 K — nearly halving over just 15 K.\n\n3. **Complementary datasets:** The two sources use different composition bases (mass fraction vs. mole fraction) and different measurement techniques (falling sphere vs. capillary Ubbelohde), providing complementary coverage of the system.",
  "core_claims": [
    "The ThermoML database contains dynamic viscosity data for binary isopropanol (propan-2-ol) + water mixtures from two literature sources (DOI: 10.1016/j.jct.2019.105880 and DOI: 10.1021/je700700f), totaling 25 data points.",
    "Source 1 provides 12 data points measured by falling/rolling sphere viscometry at 288.15–303.15 K, 100.0 kPa, at IPA mass fractions w = 0.1, 0.2, and 0.3.",
    "Source 2 provides 13 data points measured by capillary Ubbelohde viscometry at 298.15 K, 101.0 kPa, spanning the full IPA mole fraction range (x = 0 to 1).",
    "The full-composition data at 298.15 K show a non-monotonic viscosity maximum near x(IPA) ≈ 0.30, where viscosity reaches 0.003087 Pa·s compared to 0.00089 Pa·s for pure water and 0.002082 Pa·s for pure IPA, attributed to enhanced hydrogen-bonding network restructuring and microheterogeneity.",
    "Viscosity decreases with increasing temperature at all three mass fractions studied; at w = 0.3, viscosity drops from 0.004014 Pa·s at 288.15 K to 0.002105 Pa·s at 303.15 K.",
    "The two sources use different composition bases (mass fraction vs. mole fraction) and different measurement techniques, providing complementary coverage of the system."
  ],
  "confidence": "high",
  "sources": [],
  "follow_up_suggestions": [
    "Would you like to compare these viscosity values with density data for the same IPA + water system?",
    "Should I look for viscosity data at higher temperatures or pressures for IPA + water?",
    "Would you like to see excess viscosity or viscosity deviation data for this system?",
    "Are you interested in viscosity data for other alcohol + water binary mixtures (e.g., methanol or ethanol + water) for comparison?"
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

Hardcoded envelope merge — not agent-authored. 2 entr(ies); verbatim rows below.

- INSP_2e872616482b — GLOBlit_5585::PROPblock_12 · complete · 12 rows
- INSP_e0a2d04e3e34 — GLOBlit_11042::PROPblock_15 · rdp · 10 rows

```json
[
  {
    "doi": "10.1016/j.jct.2019.105880",
    "block_number": "PROPblock_12",
    "table_mode": "complete",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mass_fraction_<propan-2-ol>",
      "pressure_kpa",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "288.15",
        "mass_fraction_<propan-2-ol>": "0.1",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.001936"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "temperature_k": "288.15",
        "mass_fraction_<propan-2-ol>": "0.2",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.003087"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "temperature_k": "288.15",
        "mass_fraction_<propan-2-ol>": "0.3",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.004014"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "temperature_k": "293.15",
        "mass_fraction_<propan-2-ol>": "0.1",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.001633"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "temperature_k": "293.15",
        "mass_fraction_<propan-2-ol>": "0.2",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.002485"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "temperature_k": "293.15",
        "mass_fraction_<propan-2-ol>": "0.3",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.003172"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "temperature_k": "298.15",
        "mass_fraction_<propan-2-ol>": "0.1",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.001395"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "temperature_k": "298.15",
        "mass_fraction_<propan-2-ol>": "0.2",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.002045"
      },
      {
        "BLKpoint_id": "BLKpoint_9",
        "temperature_k": "298.15",
        "mass_fraction_<propan-2-ol>": "0.3",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.002555"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "temperature_k": "303.15",
        "mass_fraction_<propan-2-ol>": "0.1",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.001208"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "temperature_k": "303.15",
        "mass_fraction_<propan-2-ol>": "0.2",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00171"
      },
      {
        "BLKpoint_id": "BLKpoint_12",
        "temperature_k": "303.15",
        "mass_fraction_<propan-2-ol>": "0.3",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.002105"
      }
    ],
    "inspection_id": "INSP_2e872616482b",
    "lit_num_id": "GLOBlit_5585"
  },
  {
    "doi": "10.1021/je700700f",
    "block_number": "PROPblock_15",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "mole_fraction_<propan-2-ol>",
      "temperature_k",
      "pressure_kpa",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "mole_fraction_<propan-2-ol>": "0",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.00089"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "mole_fraction_<propan-2-ol>": "0.0491",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001718"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "mole_fraction_<propan-2-ol>": "0.1008",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002495"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "mole_fraction_<propan-2-ol>": "0.2011",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.003038"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "mole_fraction_<propan-2-ol>": "0.2994",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.003087"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "mole_fraction_<propan-2-ol>": "0.3992",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002924"
      },
      {
        "BLKpoint_id": "BLKpoint_9",
        "mole_fraction_<propan-2-ol>": "0.6987",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002274"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "mole_fraction_<propan-2-ol>": "0.7993",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002153"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "mole_fraction_<propan-2-ol>": "0.8998",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002073"
      },
      {
        "BLKpoint_id": "BLKpoint_13",
        "mole_fraction_<propan-2-ol>": "1",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002082"
      }
    ],
    "inspection_id": "INSP_e0a2d04e3e34",
    "lit_num_id": "GLOBlit_11042"
  }
]
```
