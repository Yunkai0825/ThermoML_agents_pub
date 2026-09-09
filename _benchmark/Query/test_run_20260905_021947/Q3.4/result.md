# Q3.4 — Result

**Prompt:** I need an ethanol + water study suitable for cross-checking several measured properties from the same experimental source. Which paper is the best candidate, and what other chemical systems does it report?

**Tool calls:** 4  |  **Time:** 1100.8s  |  **Iterations:** 5  |  **Timed out:** False

---

## Answer

{
  "answer": "## Best Candidate for Cross-Checking: Ethanol + Water\n\nBased on a search of the ThermoML database, **six papers** were identified that report measured properties for the ethanol + water binary system. The best candidate for cross-checking multiple properties from a single experimental source is:\n\n### Top Recommendation: GLOBlit_3971 (DOI: 10.1016/j.jct.2013.08.020)\n\nThis paper reports **4 distinct measured properties** for ethanol + water, all from isobaric vapor–liquid equilibrium (VLE) measurements at 101.3 kPa:\n\n| Property | Block | Data Points | Range |\n|----------|-------|-------------|-------|\n| Boiling temperature (GLOBprop_14) | PROPblock_9 | 16 | 351.33–373.15 K |\n| Vapor-phase mole fraction (GLOBprop_2) | PROPblock_10 | 16 | 0.0–1.0 |\n| Azeotropic temperature (GLOBprop_58) | PROPblock_11 | 1 | 351.32 K |\n| Azeotropic mole fraction (GLOBprop_45) | PROPblock_12 | 1 | 0.891 |\n\n**Representative verified data** from PROPblock_9 (boiling temperature at 101.3 kPa):\n\n| x(ethanol) | T_boil (K) |\n|------------|------------|\n| 0 | 373.15 |\n| 0.035 | 365.61 |\n| 0.1 | 359.79 |\n| 0.183 | 356.66 |\n| 0.292 | 354.88 |\n| 0.631 | 352.04 |\n| 0.899 | 351.33 |\n| 1.0 | 351.45 |\n\nThe data clearly show the characteristic ethanol–water positive azeotrope: the boiling temperature decreases from 373.15 K (pure water) to a minimum of 351.33 K near x(ethanol) = 0.899, then rises slightly to 351.45 K for pure ethanol. The reported azeotropic composition of x(ethanol) = 0.891 at 351.32 K is consistent with the well-known literature azeotrope (~95.6 wt% ethanol).\n\n### Other Chemical Systems in This Paper\n\nUnfortunately, my attempts to query the database for additional chemical systems reported in GLOBlit_3971 encountered technical errors and could not be completed in the available time. Given that the paper's DOI (10.1016/j.jct.2013.08.020) indicates a study of isobaric VLE, it is likely that the paper also reports VLE data for other binary systems (common practice in such studies), but I cannot confirm which specific systems without verified database results.\n\n### Notable Alternatives\n\nIf a data-rich study with transport/volumetric properties is preferred over VLE data:\n\n- **GLOBlit_5201** (DOI: 10.1016/j.jct.2018.02.022) — 3 properties (mass density, speed of sound, dynamic viscosity) with **496 total data points** across temperatures 293.15–308.15 K and up to 59 unique compositions at 92.3 kPa. This is the most data-dense source.\n\n- **GLOBlit_7448** (DOI: 10.1021/acs.jced.8b00086) — 3 properties (mass density, viscosity, surface tension) all measured at the same conditions (298.2 K, 100.0 kPa), making it ideal for direct property-to-property comparison at identical state points.\n\n- **GLOBlit_7178** (DOI: 10.1021/acs.jced.7b00299) — 3 properties (mass density, viscosity, refractive index).\n\n- **GLOBlit_2732** (DOI: 10.1016/j.jct.2006.08.002) — 2 properties (vapor pressure, mass density) with 326 data points.",
  "core_claims": [
    "Six papers in the ThermoML database report measured properties for the ethanol + water binary system.",
    "GLOBlit_3971 (DOI: 10.1016/j.jct.2013.08.020) reports 4 distinct measured properties for ethanol + water from isobaric VLE measurements at 101.3 kPa: boiling temperature (351.33–373.15 K), vapor-phase mole fraction (0.0–1.0), azeotropic temperature (351.32 K), and azeotropic mole fraction (0.891).",
    "The boiling temperature data from GLOBlit_3971 show the characteristic ethanol–water positive azeotrope, decreasing from 373.15 K (pure water) to a minimum of 351.33 K near x(ethanol) = 0.899, then rising slightly to 351.45 K for pure ethanol.",
    "GLOBlit_5201 (DOI: 10.1016/j.jct.2018.02.022) is the most data-dense source with 496 total data points covering mass density, speed of sound, and dynamic viscosity across temperatures 293.15–308.15 K and up to 59 unique compositions at 92.3 kPa.",
    "Attempts to query the database for additional chemical systems reported in GLOBlit_3971 encountered technical errors and could not be completed."
  ],
  "confidence": "medium",
  "sources": [
    {
      "doi": "10.1016/j.jct.2013.08.020",
      "lit_num_id": "GLOBlit_3971",
      "block": "PROPblock_9",
      "BLKsubsys_id": null,
      "description": "Provides 16 boiling-temperature data points for ethanol + water at 101.3 kPa spanning 351.33–373.15 K, which the answer quotes directly and uses to illustrate the positive azeotrope behavior."
    },
    {
      "doi": "10.1016/j.jct.2013.08.020",
      "lit_num_id": "GLOBlit_3971",
      "block": "PROPblock_10",
      "BLKsubsys_id": null,
      "description": "Provides 16 vapor-phase mole-fraction data points for ethanol + water at 101.3 kPa, constituting the second measured VLE property from this source and supporting the cross-check of isobaric VLE."
    },
    {
      "doi": "10.1016/j.jct.2013.08.020",
      "lit_num_id": "GLOBlit_3971",
      "block": "PROPblock_11",
      "BLKsubsys_id": null,
      "description": "Reports the azeotropic temperature of 351.32 K for ethanol + water at 101.3 kPa, which the answer cites as one of the four distinct properties from this source."
    },
    {
      "doi": "10.1016/j.jct.2013.08.020",
      "lit_num_id": "GLOBlit_3971",
      "block": "PROPblock_12",
      "BLKsubsys_id": null,
      "description": "Reports the azeotropic mole fraction of 0.891 for ethanol + water at 101.3 kPa, directly quoted in the answer and consistent with the well-known literature azeotrope."
    }
  ],
  "follow_up_suggestions": [
    "Query GLOBlit_3971 for all chemical systems beyond ethanol + water to identify additional binary mixtures reported in the same paper.",
    "Compare the azeotropic composition and temperature from GLOBlit_3971 against literature reference values for the ethanol–water azeotrope.",
    "For transport-property cross-checking, examine GLOBlit_5201 in detail — it offers 496 data points across density, speed of sound, and viscosity for ethanol + water."
  ],
  "id_catalog_snapshot": [
    {
      "type": "comp",
      "global_id": "GLOBcomp_1",
      "registry_id": "water",
      "name": "water"
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

Hardcoded envelope merge — not agent-authored. 1 entr(ies); verbatim rows below.

- INSP_d3928e4cdf0a — GLOBlit_3971::PROPblock_9 · rdp · 8 rows

```json
[
  {
    "doi": "10.1016/j.jct.2013.08.020",
    "block_number": "PROPblock_9",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "mole_fraction_<ethanol>",
      "pressure_kpa",
      "boiling_temperature_at_pressure_p_k"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "mole_fraction_<ethanol>": "0",
        "pressure_kpa": "101.3",
        "boiling_temperature_at_pressure_p_k": "373.15"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "mole_fraction_<ethanol>": "0.035",
        "pressure_kpa": "101.3",
        "boiling_temperature_at_pressure_p_k": "365.61"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "mole_fraction_<ethanol>": "0.1",
        "pressure_kpa": "101.3",
        "boiling_temperature_at_pressure_p_k": "359.79"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "mole_fraction_<ethanol>": "0.183",
        "pressure_kpa": "101.3",
        "boiling_temperature_at_pressure_p_k": "356.66"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "mole_fraction_<ethanol>": "0.292",
        "pressure_kpa": "101.3",
        "boiling_temperature_at_pressure_p_k": "354.88"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "mole_fraction_<ethanol>": "0.631",
        "pressure_kpa": "101.3",
        "boiling_temperature_at_pressure_p_k": "352.04"
      },
      {
        "BLKpoint_id": "BLKpoint_14",
        "mole_fraction_<ethanol>": "0.899",
        "pressure_kpa": "101.3",
        "boiling_temperature_at_pressure_p_k": "351.33"
      },
      {
        "BLKpoint_id": "BLKpoint_16",
        "mole_fraction_<ethanol>": "1",
        "pressure_kpa": "101.3",
        "boiling_temperature_at_pressure_p_k": "351.45"
      }
    ],
    "inspection_id": "INSP_d3928e4cdf0a",
    "lit_num_id": "GLOBlit_3971"
  }
]
```
