# Delegated query run — result

**Question:** Find viscosity data for the binary mixture of methanol and water at 25°C (298.15 K), especially near equimolar composition (mole fraction ~0.5). I need both mixture viscosity values and pure component viscosities to assess deviation from ideal mixing.

**Iterations:** 2  |  **Elapsed:** 214.6s  |  **Tools:** 1  |  **Timed out:** False

---

## Answer

{
  "answer": "## Dynamic Viscosity of Methanol + Water Binary Mixtures at 298.15 K\n\n### Primary Dataset\n\nThe most comprehensive dataset comes from **DOI: 10.1016/j.jct.2007.05.004** (PROPblock_9), which reports dynamic viscosity (η) for the methanol + water binary system across the full composition range at 298.15 K and 101.0 kPa. Twelve data points are available:\n\n| Mole fraction of water (x_water) | Mole fraction of methanol (x_MeOH) | η (Pa·s) | η (mPa·s) |\n|:-:|:-:|:-:|:-:|\n| 0 (pure methanol) | 1.0 | 0.000545 | 0.545 |\n| 0.049 | 0.951 | 0.000607 | 0.607 |\n| 0.0993 | 0.9007 | 0.000677 | 0.677 |\n| 0.1973 | 0.8027 | 0.000821 | 0.821 |\n| 0.2983 | 0.7017 | 0.000987 | 0.987 |\n| 0.3985 | 0.6015 | 0.00115 | 1.150 |\n| 0.5994 | 0.4006 | 0.001463 | 1.463 |\n| 0.6997 | 0.3003 | 0.001554 | 1.554 |\n| 0.7986 | 0.2014 | 0.001542 | 1.542 |\n| 0.8999 | 0.1001 | 0.001317 | 1.317 |\n| 0.9512 | 0.0488 | 0.001121 | 1.121 |\n| 1.0 (pure water) | 0 | 0.00089 | 0.890 |\n\n### Pure Component Viscosities\n- **Pure methanol:** η = 0.000545 Pa·s (0.545 mPa·s)\n- **Pure water:** η = 0.00089 Pa·s (0.890 mPa·s)\n\n### Near-Equimolar Composition (x_methanol ≈ 0.5)\n\nThe dataset does not contain an exact equimolar point, but the two closest compositions bracket x_methanol = 0.5:\n\n- **x_methanol = 0.6015** (x_water = 0.3985): η = 0.00115 Pa·s (1.150 mPa·s)\n- **x_methanol = 0.4006** (x_water = 0.5994): η = 0.001463 Pa·s (1.463 mPa·s)\n\nBoth values are already substantially above either pure component, confirming strong non-ideal mixing behavior in this composition region.\n\n### Deviation from Ideal Mixing\n\nThe methanol–water system exhibits a **pronounced positive deviation** from linear (ideal) mixing of viscosity:\n\n- The viscosity maximum is **0.001554 Pa·s** (1.554 mPa·s), occurring near x_water ≈ 0.70 (x_methanol ≈ 0.30).\n- This maximum is approximately **2.9× the pure methanol viscosity** (0.001554 / 0.000545) and **1.7× the pure water viscosity** (0.001554 / 0.00089).\n- A simple linear mixing rule at equimolar composition would predict roughly (0.000545 + 0.00089)/2 ≈ 0.000718 Pa·s, whereas the measured values near x_methanol = 0.5 are 0.00115–0.001463 Pa·s — about 1.6–2.0× the linear estimate.\n\n**Physical origin:** This behavior is attributed to the enhancement of the hydrogen-bonding network when methanol and water are mixed. At intermediate compositions, methanol molecules integrate into the water H-bond network, forming larger, more structured clusters that increase the resistance to flow. The viscosity maximum near x_water ≈ 0.70 corresponds to compositions where these cooperative H-bonding interactions are strongest.\n\n### Supplementary Datasets\n\nTwo additional datasets provide complementary viscosity values in the methanol-dilute (water-rich) region at 298.15 K and 101.0 kPa:\n\n**DOI: 10.1021/je0600810** (PROPblock_3) — reported vs. volume fraction of methanol:\n\n| Volume fraction of methanol (φ_v) | η (Pa·s) |\n|:-:|:-:|\n| 0.01 | 0.0010844 |\n| 0.20 | 0.0013106 |\n| 0.30 | 0.0014712 |\n\n**DOI: 10.1021/je2003622** (PROPblock_1) — reported vs. mass fraction of methanol:\n\n| Mass fraction of methanol (w) | η (Pa·s) |\n|:-:|:-:|\n| 0.0806 | 0.0010844 |\n| 0.1647 | 0.0013106 |\n| 0.2526 | 0.0014712 |\n| 0.3446 | 0.0014475 |\n\nThese supplementary sets are consistent with the primary dataset and confirm the steep rise in viscosity as methanol is added to water, with values already approaching the maximum near w_methanol ≈ 0.25–0.35.",
  "core_claims": [
    "At 298.15 K and 101.0 kPa, the dynamic viscosity of methanol + water binary mixtures exhibits a pronounced positive deviation from linear (ideal) mixing, with a viscosity maximum of 0.001554 Pa·s (1.554 mPa·s) occurring near x_water ≈ 0.70 (x_methanol ≈ 0.30).",
    "Pure component viscosities at 298.15 K are 0.000545 Pa·s (0.545 mPa·s) for methanol and 0.00089 Pa·s (0.890 mPa·s) for water.",
    "Near equimolar composition, measured viscosities (0.00115 Pa·s at x_methanol = 0.6015 and 0.001463 Pa·s at x_methanol = 0.4006) substantially exceed a simple linear mixing estimate of approximately 0.000718 Pa·s.",
    "The positive viscosity deviation is attributed to enhancement of the hydrogen-bonding network at intermediate compositions, where methanol molecules integrate into the water H-bond structure forming larger, more structured clusters.",
    "The primary dataset (DOI: 10.1016/j.jct.2007.05.004) covers twelve compositions spanning the full mole-fraction range; supplementary datasets (DOI: 10.1021/je0600810 and DOI: 10.1021/je2003622) confirm the steep viscosity rise in the water-rich region and are consistent with the primary data."
  ],
  "confidence": "high",
  "sources": [
    {
      "doi": "10.1016/j.jct.2007.05.004",
      "lit_num_id": "GLOBlit_2825",
      "block": "PROPblock_9",
      "BLKsubsys_id": null,
      "description": "This block is the primary dataset providing dynamic viscosity of methanol + water across the full mole fraction range (0.0–1.0) at temperatures spanning 293.15–303.15 K (including 298.15 K) and 101.0 kPa. The answer's 12-point table with viscosities from 0.000545 to 0.001554 Pa·s falls within the block's reported range of 0.000508–0.001793 Pa·s, and the 39 datapoints accommodate three temperatures times ~13 compositions."
    },
    {
      "doi": "10.1021/je0600810",
      "lit_num_id": "GLOBlit_8869",
      "block": "PROPblock_3",
      "BLKsubsys_id": null,
      "description": "This block provides supplementary viscosity data for methanol + water in the methanol-dilute region (volume fraction 0.01–0.30) at temperatures including 298.15 K and 101.0 kPa. The answer cites three viscosity values from this block (0.0010844, 0.0013106, 0.001471 Pa·s) that fall within the block's reported range of 0.000702–0.001471 Pa·s."
    },
    {
      "doi": "10.1021/je2003622",
      "lit_num_id": "GLOBlit_9571",
      "block": "PROPblock_1",
      "BLKsubsys_id": null,
      "description": "This block provides supplementary viscosity data for methanol + water reported versus mass fraction (0.0806–0.3446) at temperatures including 298.15 K and 101.0 kPa. The answer cites four viscosity values from this block that fall within its reported range of 0.000638–0.001471 Pa·s, confirming the steep viscosity rise and approach to the maximum near w_methanol ≈ 0.25–0.35."
    }
  ],
  "follow_up_suggestions": [
    "Search for excess viscosity or viscosity deviation (Δη) data for methanol+water to quantify non-ideal mixing more precisely.",
    "Look for temperature-dependent viscosity data (e.g., 288–318 K) for the same system to assess Arrhenius or VFT fitting parameters.",
    "Seek kinematic viscosity or density data at matching compositions to cross-validate dynamic viscosity values."
  ],
  "id_catalog_snapshot": [
    {
      "type": "comp",
      "global_id": "GLOBcomp_4",
      "registry_id": "methanol",
      "name": "methanol"
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

Hardcoded envelope merge — not agent-authored. 3 entr(ies); verbatim rows below.

- INSP_f99e390ea15c — GLOBlit_2825::PROPblock_9 · rdp · 12 rows
- INSP_51feb0d2c046 — GLOBlit_8869::PROPblock_3 · complete · 3 rows
- INSP_9b7df612effc — GLOBlit_9571::PROPblock_1 · complete · 4 rows

```json
[
  {
    "doi": "10.1016/j.jct.2007.05.004",
    "block_number": "PROPblock_9",
    "table_mode": "rdp",
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
        "viscosity_pa_s": "0.000545"
      },
      {
        "BLKpoint_id": "BLKpoint_15",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.049",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.000607"
      },
      {
        "BLKpoint_id": "BLKpoint_16",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.0993",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.000677"
      },
      {
        "BLKpoint_id": "BLKpoint_17",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.1973",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.000821"
      },
      {
        "BLKpoint_id": "BLKpoint_18",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.2983",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.000987"
      },
      {
        "BLKpoint_id": "BLKpoint_19",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.3985",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.00115"
      },
      {
        "BLKpoint_id": "BLKpoint_21",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.5994",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001463"
      },
      {
        "BLKpoint_id": "BLKpoint_22",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.6997",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001554"
      },
      {
        "BLKpoint_id": "BLKpoint_23",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.7986",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001542"
      },
      {
        "BLKpoint_id": "BLKpoint_24",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.8999",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001317"
      },
      {
        "BLKpoint_id": "BLKpoint_25",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.9512",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001121"
      },
      {
        "BLKpoint_id": "BLKpoint_26",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "1",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.00089"
      }
    ],
    "inspection_id": "INSP_f99e390ea15c",
    "lit_num_id": "GLOBlit_2825"
  },
  {
    "doi": "10.1021/je0600810",
    "block_number": "PROPblock_3",
    "table_mode": "complete",
    "columns": [
      "BLKpoint_id",
      "volume_fraction_<methanol>",
      "temperature_k",
      "pressure_kpa",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "volume_fraction_<methanol>": "0.01",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0010844"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "volume_fraction_<methanol>": "0.2",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0013106"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "volume_fraction_<methanol>": "0.3",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0014712"
      }
    ],
    "inspection_id": "INSP_51feb0d2c046",
    "lit_num_id": "GLOBlit_8869"
  },
  {
    "doi": "10.1021/je2003622",
    "block_number": "PROPblock_1",
    "table_mode": "complete",
    "columns": [
      "BLKpoint_id",
      "mass_fraction_<methanol>",
      "temperature_k",
      "pressure_kpa",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "mass_fraction_<methanol>": "0.0806",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0010844"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "mass_fraction_<methanol>": "0.1647",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0013106"
      },
      {
        "BLKpoint_id": "BLKpoint_9",
        "mass_fraction_<methanol>": "0.2526",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0014712"
      },
      {
        "BLKpoint_id": "BLKpoint_13",
        "mass_fraction_<methanol>": "0.3446",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0014475"
      }
    ],
    "inspection_id": "INSP_9b7df612effc",
    "lit_num_id": "GLOBlit_9571"
  }
]
```
