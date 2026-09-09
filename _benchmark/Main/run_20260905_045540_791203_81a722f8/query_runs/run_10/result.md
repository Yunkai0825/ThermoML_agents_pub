# Delegated query run — result

**Question:** Find viscosity data for isopropanol (2-propanol) mixed with water at room temperature (around 293-298 K). Rubbing alcohol is isopropanol.

**Iterations:** 2  |  **Elapsed:** 143.6s  |  **Tools:** 1  |  **Timed out:** False

---

## Answer

{
  "answer": "## Viscosity Data for Isopropanol (2-Propanol) + Water Binary Mixtures at Room Temperature\n\n### Source\n\n**DOI:** 10.1016/j.jct.2019.105880  \n**Data block:** PROPblock_12  \n**Property:** Dynamic viscosity (Pa·s), measured by falling/rolling sphere viscometry, liquid phase, at 100 kPa.  \n**System:** Binary mixture of propan-2-ol (2-propanol / isopropanol) + water.\n\n**Composition range covered:** Mass fraction of propan-2-ol from 0.1 to 0.3  \n**Full block temperature range:** 288.15–303.15 K (12 data points total)\n\n---\n\n### Data Points in the 293–298 K Window\n\n| T (K) | w (propan-2-ol) | Dynamic Viscosity (Pa·s) |\n|--------|-----------------|--------------------------|\n| 293.15 | 0.1             | 0.001633                 |\n| 293.15 | 0.2             | 0.002485                 |\n| 293.15 | 0.3             | 0.003172                 |\n| 298.15 | 0.1             | 0.001395                 |\n| 298.15 | 0.2             | 0.002045                 |\n| 298.15 | 0.3             | 0.002555                 |\n\nAll measurements were made at a pressure of 100.0 kPa in the liquid phase.\n\n---\n\n### Key Observations\n\n1. **Viscosity increases with isopropanol content** in the 0.1–0.3 mass-fraction range at both temperatures. For example, at 293.15 K the viscosity nearly doubles from 0.001633 Pa·s (w = 0.1) to 0.003172 Pa·s (w = 0.3). This trend is consistent with the well-known viscosity maximum of the isopropanol–water system, which occurs at higher alcohol concentrations (typically around 0.6–0.7 mass fraction). In this composition range, the extensive hydrogen-bonding network between water and isopropanol molecules progressively increases internal friction.\n\n2. **Viscosity decreases with increasing temperature**, as expected from the Arrhenius-type temperature dependence of liquid viscosity. At w = 0.3, the viscosity drops from 0.003172 Pa·s at 293.15 K to 0.002555 Pa·s at 298.15 K — a reduction of about 19% for just a 5 K increase.\n\n3. **Full data block** extends from 288.15 K to 303.15 K, with viscosities spanning 0.001208–0.004014 Pa·s across all compositions and temperatures.\n\n4. **No kinematic viscosity data** were found in the ThermoML database for this binary system in the requested temperature range. Only dynamic viscosity data are available from this source.",
  "core_claims": [
    "Dynamic viscosity data for the binary mixture of propan-2-ol (isopropanol) + water were found in ThermoML (DOI: 10.1016/j.jct.2019.05880, PROPblock_12), covering mass fractions of propan-2-ol from 0.1 to 0.3 at 100 kPa, with six data points falling within the 293–298 K window.",
    "At 293.15 K and 100 kPa, the dynamic viscosity increases from 0.001633 Pa·s at w = 0.1 to 0.003172 Pa·s at w = 0.3; at 298.15 K it increases from 0.001395 Pa·s at w = 0.1 to 0.002555 Pa·s at w = 0.3.",
    "Viscosity decreases with increasing temperature: at w = 0.3, it drops from 0.003172 Pa·s at 293.15 K to 0.002555 Pa·s at 298.15 K.",
    "No kinematic viscosity data were found in the ThermoML database for this binary system in the requested temperature range; only dynamic viscosity data are available from this source."
  ],
  "confidence": "high",
  "sources": [
    {
      "doi": "10.1016/j.jct.2019.105880",
      "lit_num_id": "GLOBlit_5585",
      "block": "PROPblock_12",
      "BLKsubsys_id": null,
      "description": "This block provides dynamic viscosity data for the binary system propan-2-ol + water measured by falling/rolling sphere viscometry at 100 kPa. The temperature range 288.15–303.15 K covers the requested 293–298 K window, and the mass fraction range 0.1–0.3 with 12 data points directly supports the six viscosity values reported in the answer."
    }
  ],
  "follow_up_suggestions": [
    "Search for additional viscosity data at higher isopropanol mass fractions (0.4–0.9) to capture the well-known viscosity maximum near w ≈ 0.6–0.7 in the isopropanol–water system.",
    "Look for kinematic viscosity or density data for the same system and temperature range to enable cross-checking between dynamic and kinematic viscosity.",
    "Explore other DOIs in ThermoML for isopropanol–water viscosity data at temperatures outside the 288–303 K range for broader temperature-dependence modeling."
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
    },
    {
      "type": "lit",
      "global_id": "GLOBlit_5585",
      "registry_id": "2019-meh-haj-0",
      "name": "10.1016/j.jct.2019.105880"
    }
  ]
}

---

## Data Inspections (deterministic evidence ledger)

Hardcoded envelope merge — not agent-authored. 1 entr(ies); verbatim rows below.

- INSP_5c8cad6c2b0f — GLOBlit_5585::PROPblock_12 · complete · 6 rows

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
      }
    ],
    "inspection_id": "INSP_5c8cad6c2b0f",
    "lit_num_id": "GLOBlit_5585"
  }
]
```
