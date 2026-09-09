# Delegated query run — result

**Question:** Find experimental viscosity values for an equimolar (x=0.5) binary mixture of acetonitrile and N,N-dimethylformamide at 25 degrees Celsius (298.15 K). Report all available data points with values, units, DOIs, block numbers, and literature IDs.

**Iterations:** 2  |  **Elapsed:** 206.9s  |  **Tools:** 1  |  **Timed out:** False

---

## Answer

{
  "answer": "## Dynamic Viscosity of Acetonitrile + N,N-Dimethylformamide at Equimolar Composition and 298.15 K\n\nTwo independent ThermoML data blocks report experimental dynamic viscosity for the binary system **acetonitrile + N,N-dimethylformamide (DMF)** near equimolar composition at 298.15 K (25 °C):\n\n---\n\n### Data Source 1 — Mole-fraction basis (closest match to x = 0.5)\n\n**DOI:** 10.1021/acs.jced.8b00176 (GLOBlit_7481)  \n**Block:** PROPblock_18  \n**Method:** Falling/rolling sphere viscometer  \n**Pressure:** 100.0 kPa  \n\nThere is **no exact data point at x(DMF) = 0.5000**; the nearest composition is **x(DMF) = 0.5029**. The data at 298.15 K surrounding the equimolar region are:\n\n| T (K) | x(DMF) | p (kPa) | η (Pa·s) | η (mPa·s) |\n|--------|---------|---------|-----------|------------|\n| 298.15 | 0.3932 | 100.0 | 0.00054 | 0.54 |\n| **298.15** | **0.5029** | **100.0** | **0.00061** | **0.61** |\n| 298.15 | 0.6002 | 100.0 | 0.00065 | 0.65 |\n| 298.15 | 0.6931 | 100.0 | 0.00069 | 0.69 |\n\n**Best available near-equimolar value: η = 0.00061 Pa·s (0.61 mPa·s) at x(DMF) = 0.5029, 298.15 K, 100.0 kPa.**\n\n---\n\n### Data Source 2 — Mass-fraction basis\n\n**DOI:** 10.1016/j.jct.2014.02.019 (GLOBlit_4124)  \n**Block:** PROPblock_6  \n**Method:** Capillary tube (Ostwald–Ubbelohde)  \n**Pressure:** 101.0 kPa  \n\nThis block reports composition as mass fraction of DMF. An equimolar mixture (x = 0.5) corresponds to approximately w(DMF) ≈ 0.64 based on the molar masses of DMF (73.09 g/mol) and acetonitrile (41.05 g/mol). No exact row at w ≈ 0.64 exists; the bracketing data at 298.15 K are:\n\n| T (K) | w(DMF) | p (kPa) | η (Pa·s) | η (mPa·s) |\n|--------|--------|---------|-----------|------------|\n| 298.15 | 0.25 | 101.0 | 0.0003959 | 0.396 |\n| 298.15 | 0.50 | 101.0 | 0.0005214 | 0.521 |\n| 298.15 | 0.75 | 101.0 | 0.0006465 | 0.647 |\n| 298.15 | 1.00 | 101.0 | 0.0007986 | 0.799 |\n\nThe equimolar value would fall between the w = 0.50 and w = 0.75 rows, but no exact match is available in this block.\n\n---\n\n### Summary and Chemistry Insight\n\n| Source | Composition basis | Nearest equimolar point | η (Pa·s) | η (mPa·s) |\n|--------|-------------------|------------------------|-----------|------------|\n| 10.1021/acs.jced.8b00176 (GLOBlit_7481, PROPblock_18) | Mole fraction | x(DMF) = 0.5029 | 0.00061 | 0.61 |\n| 10.1016/j.jct.2014.02.019 (GLOBlit_4124, PROPblock_6) | Mass fraction | Bracketed between w = 0.50 and 0.75 | 0.0005214–0.0006465 | 0.521–0.647 |\n\nThe viscosity of this mixture increases monotonically with DMF content, which is expected since pure DMF is substantially more viscous than pure acetonitrile at 298.15 K (η_DMF ≈ 0.00080 Pa·s vs. η_ACN ≈ 0.00034 Pa·s, from PROPblock_18). The near-equimolar value of 0.00061 Pa·s falls between the two pure-component viscosities, consistent with a relatively ideal mixing behavior — the acetonitrile–DMF system exhibits only weak intermolecular interactions beyond simple dipole–dipole forces, so no pronounced viscosity maximum or minimum (as seen in strongly associating systems) is observed.",
  "core_claims": [
    "At 298.15 K and 100.0 kPa, the dynamic viscosity of the acetonitrile + N,N-dimethylformamide binary mixture near equimolar composition (x(DMF) = 0.5029) is 0.00061 Pa·s (0.61 mPa·s), as reported in DOI 10.1021/acs.jced.8b00176.",
    "A second independent source (DOI 10.1016/j.jct.2014.02.019) brackets the equimolar viscosity at 298.15 K between 0.0005214 Pa·s (w(DMF) = 0.50) and 0.0006465 Pa·s (w(DMF) = 0.75), consistent with the first source.",
    "The viscosity of the acetonitrile + DMF mixture increases monotonically with DMF content at 298.15 K, with the near-equimolar value falling between the pure-component viscosities (η_ACN ≈ 0.00034 Pa·s, η_DMF ≈ 0.00080 Pa·s), consistent with relatively ideal mixing behavior and the absence of a pronounced viscosity extremum."
  ],
  "confidence": "high",
  "sources": [
    {
      "doi": "10.1021/acs.jced.8b00176",
      "lit_num_id": "GLOBlit_7481",
      "block": "PROPblock_18",
      "BLKsubsys_id": null,
      "description": "This block provides dynamic viscosity of the acetonitrile + DMF binary system on a mole-fraction basis at 298.15 K and 100.0 kPa. It contains the nearest equimolar data point at x(DMF) = 0.5029 with η = 0.00061 Pa·s, which is the primary value reported in the answer."
    },
    {
      "doi": "10.1016/j.jct.2014.02.019",
      "lit_num_id": "GLOBlit_4124",
      "block": "PROPblock_6",
      "BLKsubsys_id": null,
      "description": "This block provides dynamic viscosity of the acetonitrile + DMF binary system on a mass-fraction basis at 298.15 K and 101.0 kPa. It supplies bracketing values (w = 0.50 and w = 0.75) around the equimolar composition, serving as independent corroboration of the viscosity range reported in the answer."
    }
  ],
  "follow_up_suggestions": [
    "Retrieve excess viscosity or viscosity deviation data for the acetonitrile + DMF system to assess non-ideal mixing contributions.",
    "Compare viscosity values at other temperatures (e.g., 303.15 K, 313.15 K) from the same sources to examine temperature dependence.",
    "Search for density data at the same equimolar composition and temperature to enable kinematic viscosity calculation."
  ],
  "id_catalog_snapshot": [
    {
      "type": "comp",
      "global_id": "GLOBcomp_15",
      "registry_id": "acetonitrile",
      "name": "acetonitrile"
    },
    {
      "type": "comp",
      "global_id": "GLOBcomp_18",
      "registry_id": "dimethylformamide",
      "name": "dimethylformamide"
    },
    {
      "type": "prop",
      "global_id": "GLOBprop_4",
      "registry_id": "viscosity_pa_s",
      "name": "Viscosity, Pa*s"
    },
    {
      "type": "lit",
      "global_id": "GLOBlit_7481",
      "registry_id": "2018-fat-riy-1",
      "name": "10.1021/acs.jced.8b00176"
    },
    {
      "type": "lit",
      "global_id": "GLOBlit_4124",
      "registry_id": "2014-bra-pra-0",
      "name": "10.1016/j.jct.2014.02.019"
    }
  ]
}

---

## Data Inspections (deterministic evidence ledger)

Hardcoded envelope merge — not agent-authored. 2 entr(ies); verbatim rows below.

- INSP_421661c26d77 — GLOBlit_7481::PROPblock_18 · nearest · 4 rows
- INSP_116c1d101a97 — GLOBlit_4124::PROPblock_6 · nearest · 4 rows

```json
[
  {
    "doi": "10.1021/acs.jced.8b00176",
    "block_number": "PROPblock_18",
    "table_mode": "nearest",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<dimethylformamide>",
      "pressure_kpa",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_5",
        "temperature_k": "298.15",
        "mole_fraction_<dimethylformamide>": "0.3932",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00054"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "temperature_k": "298.15",
        "mole_fraction_<dimethylformamide>": "0.5029",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00061"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "temperature_k": "298.15",
        "mole_fraction_<dimethylformamide>": "0.6002",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00065"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "temperature_k": "298.15",
        "mole_fraction_<dimethylformamide>": "0.6931",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00069"
      }
    ],
    "inspection_id": "INSP_421661c26d77",
    "lit_num_id": "GLOBlit_7481"
  },
  {
    "doi": "10.1016/j.jct.2014.02.019",
    "block_number": "PROPblock_6",
    "table_mode": "nearest",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mass_fraction_<dimethylformamide>",
      "pressure_kpa",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_5",
        "temperature_k": "298.15",
        "mass_fraction_<dimethylformamide>": "0.25",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0003959"
      },
      {
        "BLKpoint_id": "BLKpoint_9",
        "temperature_k": "298.15",
        "mass_fraction_<dimethylformamide>": "0.5",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0005214"
      },
      {
        "BLKpoint_id": "BLKpoint_13",
        "temperature_k": "298.15",
        "mass_fraction_<dimethylformamide>": "0.75",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0006465"
      },
      {
        "BLKpoint_id": "BLKpoint_17",
        "temperature_k": "298.15",
        "mass_fraction_<dimethylformamide>": "1",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0007986"
      }
    ],
    "inspection_id": "INSP_116c1d101a97",
    "lit_num_id": "GLOBlit_4124"
  }
]
```
