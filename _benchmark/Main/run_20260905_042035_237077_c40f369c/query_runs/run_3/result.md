# Delegated query run — result

**Question:** Find viscosity data for the binary mixture of methanol + ethanol at or near 30°C (303.15 K). I need dynamic viscosity as a function of composition (mole fraction). Return DOIs, block numbers, compound names, and any available data points.

**Iterations:** 2  |  **Elapsed:** 113.2s  |  **Tools:** 1  |  **Timed out:** False

---

## Answer

{
  "answer": "## Dynamic Viscosity of Methanol + Ethanol Binary Mixture at 303.15 K\n\n### Source\n\n- **DOI:** 10.1021/je800633a\n- **Block:** PROPblock_16\n- **Measurement method:** Capillary tube (Ostwald–Ubbelohde)\n\n### System Details\n\n| Parameter | Value |\n|-----------|-------|\n| **Compounds** | Methanol (CH₄O) + Ethanol (C₂H₆O) |\n| **System type** | Binary liquid mixture |\n| **Temperature** | 303.15 K (≈ 30 °C), fixed |\n| **Pressure** | 81.5 kPa, fixed |\n\n### Viscosity vs. Mole Fraction of Methanol\n\nTwelve data points spanning the composition range:\n\n| x(methanol) | η (Pa·s) |\n|:-----------:|:---------:|\n| 0.0417 | 0.000968 |\n| 0.1476 | 0.000906 |\n| 0.2214 | 0.000865 |\n| 0.2952 | 0.000828 |\n| 0.3644 | 0.000793 |\n| 0.4488 | 0.000753 |\n| 0.529  | 0.000717 |\n| 0.5995 | 0.000685 |\n| 0.6859 | 0.000648 |\n| 0.7442 | 0.000624 |\n| 0.832  | 0.000588 |\n| 0.9166 | 0.000556 |\n\n### Chemical Insight\n\nThe dynamic viscosity decreases monotonically from 0.000968 Pa·s at the ethanol-rich end (x(methanol) = 0.0417) to 0.000556 Pa·s at the methanol-rich end (x(methanol) = 0.9166). The decrease is nearly linear with composition, indicating relatively ideal mixing behavior with minimal excess viscosity effects in this system at 303.15 K.\n\nThis behavior is consistent with the molecular similarity of methanol and ethanol — both are small, linear aliphatic alcohols capable of hydrogen bonding. Methanol, being smaller (one carbon vs. two), has weaker van der Waals interactions and a less extensive hydrogen-bonding network, leading to its lower pure-component viscosity. The near-ideal mixing arises because the two components are structurally and chemically similar, so replacing ethanol molecules with methanol molecules in the mixture smoothly reduces the average intermolecular interaction strength without introducing significant structural disruption or preferential association.",
  "core_claims": [
    "For the methanol + ethanol binary liquid mixture at 303.15 K and 81.5 kPa (DOI 10.1021/je800633a, PROPblock_16), the dynamic viscosity decreases monotonically from 0.000968 Pa·s at x(methanol) = 0.0417 to 0.000556 Pa·s at x(methanol) = 0.9166, as measured by capillary tube (Ostwald–Ubbelohde) across twelve compositions.",
    "The decrease in viscosity with increasing methanol mole fraction is nearly linear, indicating relatively ideal mixing behavior with minimal excess viscosity effects, consistent with the structural and chemical similarity of the two small aliphatic alcohols."
  ],
  "confidence": "high",
  "sources": [
    {
      "doi": "10.1021/je800633a",
      "lit_num_id": "GLOBlit_11337",
      "block": "PROPblock_16",
      "BLKsubsys_id": null,
      "description": "This block provides the 12 dynamic viscosity data points for the methanol + ethanol binary mixture at 303.15 K and 81.5 kPa, spanning mole fractions 0.0417–0.9166 with viscosities 0.000556–0.000968 Pa·s, which directly constitute the answer's tabulated data and analysis."
    }
  ],
  "follow_up_suggestions": [
    "Search for excess viscosity or viscosity deviation data for methanol + ethanol to quantify non-ideal mixing contributions.",
    "Look for viscosity data at additional temperatures (e.g., 293.15 K, 313.15 K) under the same DOI to examine temperature dependence.",
    "Compare with density data for the same system and conditions to compute kinematic viscosity."
  ],
  "id_catalog_snapshot": []
}

---

## Data Inspections (deterministic evidence ledger)

Hardcoded envelope merge — not agent-authored. 1 entr(ies); verbatim rows below.

- INSP_e747e21118c7 — GLOBlit_11337::PROPblock_16 · complete · 12 rows

```json
[
  {
    "doi": "10.1021/je800633a",
    "block_number": "PROPblock_16",
    "table_mode": "complete",
    "columns": [
      "BLKpoint_id",
      "mole_fraction_<methanol>",
      "temperature_k",
      "pressure_kpa",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "mole_fraction_<methanol>": "0.0417",
        "temperature_k": "303.15",
        "pressure_kpa": "81.5",
        "viscosity_pa_s": "0.000968"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "mole_fraction_<methanol>": "0.1476",
        "temperature_k": "303.15",
        "pressure_kpa": "81.5",
        "viscosity_pa_s": "0.000906"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "mole_fraction_<methanol>": "0.2214",
        "temperature_k": "303.15",
        "pressure_kpa": "81.5",
        "viscosity_pa_s": "0.000865"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "mole_fraction_<methanol>": "0.2952",
        "temperature_k": "303.15",
        "pressure_kpa": "81.5",
        "viscosity_pa_s": "0.000828"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "mole_fraction_<methanol>": "0.3644",
        "temperature_k": "303.15",
        "pressure_kpa": "81.5",
        "viscosity_pa_s": "0.000793"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "mole_fraction_<methanol>": "0.4488",
        "temperature_k": "303.15",
        "pressure_kpa": "81.5",
        "viscosity_pa_s": "0.000753"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "mole_fraction_<methanol>": "0.529",
        "temperature_k": "303.15",
        "pressure_kpa": "81.5",
        "viscosity_pa_s": "0.000717"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "mole_fraction_<methanol>": "0.5995",
        "temperature_k": "303.15",
        "pressure_kpa": "81.5",
        "viscosity_pa_s": "0.000685"
      },
      {
        "BLKpoint_id": "BLKpoint_9",
        "mole_fraction_<methanol>": "0.6859",
        "temperature_k": "303.15",
        "pressure_kpa": "81.5",
        "viscosity_pa_s": "0.000648"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "mole_fraction_<methanol>": "0.7442",
        "temperature_k": "303.15",
        "pressure_kpa": "81.5",
        "viscosity_pa_s": "0.000624"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "mole_fraction_<methanol>": "0.832",
        "temperature_k": "303.15",
        "pressure_kpa": "81.5",
        "viscosity_pa_s": "0.000588"
      },
      {
        "BLKpoint_id": "BLKpoint_12",
        "mole_fraction_<methanol>": "0.9166",
        "temperature_k": "303.15",
        "pressure_kpa": "81.5",
        "viscosity_pa_s": "0.000556"
      }
    ],
    "inspection_id": "INSP_e747e21118c7",
    "lit_num_id": "GLOBlit_11337"
  }
]
```
