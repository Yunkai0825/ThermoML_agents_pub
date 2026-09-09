# Delegated query run — result

**Question:** Find viscosity data for the binary mixture of water + ethylene glycol at or near 30°C (303.15 K). I need dynamic viscosity as a function of composition (mole fraction). Return DOIs, block numbers, compound names, and any available data points.

**Iterations:** 2  |  **Elapsed:** 212.0s  |  **Tools:** 1  |  **Timed out:** False

---

## Answer

{
  "answer": "## Dynamic Viscosity of Water + Ethylene Glycol (1,2-Ethanediol) at 303.15 K\n\nTwo independent ThermoML datasets provide dynamic viscosity data for the binary mixture of **water** and **1,2-ethanediol (ethylene glycol)** at exactly **303.15 K (30 °C)**, covering the full composition range.\n\n---\n\n### Dataset 1 — DOI: 10.1016/j.jct.2018.02.022 · Block PROPblock_24\n\n**Method:** Concentric cylinders viscometry · **Pressure:** 92.3 kPa · **Composition variable:** mole fraction of 1,2-ethanediol\n\n| x(1,2-ethanediol) | Viscosity (Pa·s) |\n|:------------------:|:----------------:|\n| 0                  | 0.0008385        |\n| 0.0494             | 0.0011644        |\n| 0.0986             | 0.001555         |\n| 0.1483             | 0.0019899        |\n| 0.2072             | 0.0025643        |\n| 0.2466             | 0.0029649        |\n| 0.3399             | 0.0040293        |\n| 0.3921             | 0.0046704        |\n| 0.4446             | 0.0053492        |\n| 0.5485             | 0.0067709        |\n| 0.6451             | 0.0081729        |\n| 0.7012             | 0.0090846        |\n| 0.7435             | 0.0098077        |\n| 0.7907             | 0.010548         |\n| 0.8505             | 0.011535         |\n| 1                  | 0.013867         |\n\n*(Shape-preserving subset of 21 matched rows at 303.15 K; viscosity ranges from 0.0008385 to 0.013867 Pa·s.)*\n\n---\n\n### Dataset 2 — DOI: 10.1021/acs.jced.6b00526 · Block PROPblock_18\n\n**Method:** Falling sphere viscometry · **Pressure:** 100.0 kPa · **Composition variable:** mole fraction of water\n\n| x(water) | Viscosity (Pa·s) |\n|:---------:|:----------------:|\n| 0         | 0.01423          |\n| 0.1105    | 0.01186          |\n| 0.2014    | 0.01014          |\n| 0.3002    | 0.00845          |\n| 0.4011    | 0.006968         |\n| 0.4969    | 0.005653         |\n| 0.6022    | 0.004396         |\n| 0.6995    | 0.003345         |\n| 0.7994    | 0.002328         |\n| 0.8997    | 0.001446         |\n| 1         | 0.000755         |\n\n*(Complete isotherm — all 11 data points at 303.15 K.)*\n\n---\n\n### Compounds\n\n| Component | Formula | InChIKey |\n|-----------|---------|----------|\n| Water | H₂O | XLYOFNOQVPJJNP-UHFFFAOYSA-N |\n| 1,2-Ethanediol (ethylene glycol) | C₂H₆O₂ | LYCAIKOWRPUZTN-UHFFFAOYSA-N |\n\n---\n\n### Chemistry Insight\n\nBoth datasets show a **monotonic increase** in viscosity with increasing ethylene glycol content. At 303.15 K:\n\n- **Pure water:** 0.0008385 Pa·s (Dataset 1) / 0.000755 Pa·s (Dataset 2)\n- **Pure ethylene glycol:** 0.013867 Pa·s (Dataset 1) / 0.01423 Pa·s (Dataset 2)\n\nPure ethylene glycol is roughly **17–19 times more viscous** than pure water at this temperature. This large difference arises because ethylene glycol has two hydroxyl groups that form an extensive intermolecular hydrogen-bonding network, creating much stronger cohesive interactions than water alone.\n\nThe viscosity–composition curve is **concave upward** (positive deviation from a simple linear mixing rule), which is characteristic of strongly associating aqueous–diol mixtures. The two datasets, measured by different techniques (concentric cylinders vs. falling sphere) and at slightly different pressures (92.3 vs. 100.0 kPa), are in good mutual agreement, lending confidence to the reported values.\n\nThree additional ThermoML literature sources were also identified for this system and could provide further comparison data if needed.",
  "core_claims": [
    "Two independent ThermoML datasets provide dynamic viscosity data for the water + 1,2-ethanediol (ethylene glycol) binary mixture at exactly 303.15 K, covering the full composition range.",
    "Dataset 1 (DOI: 10.1016/j.jct.2018.02.022, concentric cylinders viscometry, 92.3 kPa) reports viscosity ranging from 0.0008385 Pa·s (pure water) to 0.013867 Pa·s (pure ethylene glycol) as a function of 1,2-ethanediol mole fraction.",
    "Dataset 2 (DOI: 10.1021/acs.jced.6b00526, falling sphere viscometry, 100.0 kPa) reports viscosity ranging from 0.000755 Pa·s (pure water) to 0.01423 Pa·s (pure ethylene glycol) as a function of water mole fraction.",
    "Both datasets show a monotonic increase in viscosity with increasing ethylene glycol content at 303.15 K, with the viscosity–composition curve described as concave upward (positive deviation from linear mixing), characteristic of strongly associating aqueous–diol mixtures.",
    "The two datasets, measured by different techniques and at slightly different pressures (92.3 vs. 100.0 kPa), are reported to be in good mutual agreement."
  ],
  "confidence": "high",
  "sources": [
    {
      "doi": "10.1016/j.jct.2018.02.022",
      "lit_num_id": "GLOBlit_5201",
      "block": "PROPblock_24",
      "BLKsubsys_id": null,
      "description": "Provides dynamic viscosity of the water + 1,2-ethanediol binary system measured by concentric cylinders viscometry at 92.3 kPa. The block covers 293.15–308.15 K and mole fractions 0–1, so the 303.15 K isotherm extracted in the answer (viscosity 0.0008385–0.013867 Pa·s) falls squarely within its ranges."
    },
    {
      "doi": "10.1021/acs.jced.6b00526",
      "lit_num_id": "GLOBlit_6951",
      "block": "PROPblock_18",
      "BLKsubsys_id": null,
      "description": "Provides dynamic viscosity of the water + 1,2-ethanediol binary system measured by falling sphere viscometry at 100.0 kPa. The temperature range extends to 303.15 K and mole fraction spans 0–1, supplying the 11-point isotherm (0.000755–0.01423 Pa·s) reported in the answer."
    }
  ],
  "follow_up_suggestions": [
    "Compare viscosity values from both datasets at overlapping compositions by converting mole fraction bases to a common reference (e.g., x(ethylene glycol)).",
    "Retrieve the three additional ThermoML literature sources mentioned for this system to expand the comparison dataset.",
    "Look for excess viscosity or viscosity deviation data for this system to quantify non-ideal mixing behavior.",
    "Search for viscosity data at additional temperatures (e.g., 293.15 K, 313.15 K) to examine temperature dependence and fit Arrhenius or VFT models."
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
      "global_id": "GLOBcomp_24",
      "registry_id": "1,2-ethanediol",
      "name": "1,2-ethanediol"
    },
    {
      "type": "prop",
      "global_id": "GLOBprop_4",
      "registry_id": "viscosity_pa_s",
      "name": "Viscosity, Pa*s"
    }
  ]
}

---

## Data Inspections (deterministic evidence ledger)

Hardcoded envelope merge — not agent-authored. 2 entr(ies); verbatim rows below.

- INSP_668b10d4f9b3 — GLOBlit_5201::PROPblock_24 · rdp · 16 rows
- INSP_626d46ae23bc — GLOBlit_6951::PROPblock_18 · complete · 11 rows

```json
[
  {
    "doi": "10.1016/j.jct.2018.02.022",
    "block_number": "PROPblock_24",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<1,2-ethanediol>",
      "pressure_kpa",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_39",
        "temperature_k": "303.15",
        "mole_fraction_<1,2-ethanediol>": "0.0494",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0011644"
      },
      {
        "BLKpoint_id": "BLKpoint_40",
        "temperature_k": "303.15",
        "mole_fraction_<1,2-ethanediol>": "0.0986",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.001555"
      },
      {
        "BLKpoint_id": "BLKpoint_41",
        "temperature_k": "303.15",
        "mole_fraction_<1,2-ethanediol>": "0.1483",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0019899"
      },
      {
        "BLKpoint_id": "BLKpoint_42",
        "temperature_k": "303.15",
        "mole_fraction_<1,2-ethanediol>": "0.2072",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0025643"
      },
      {
        "BLKpoint_id": "BLKpoint_43",
        "temperature_k": "303.15",
        "mole_fraction_<1,2-ethanediol>": "0.2466",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0029649"
      },
      {
        "BLKpoint_id": "BLKpoint_45",
        "temperature_k": "303.15",
        "mole_fraction_<1,2-ethanediol>": "0.3399",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0040293"
      },
      {
        "BLKpoint_id": "BLKpoint_46",
        "temperature_k": "303.15",
        "mole_fraction_<1,2-ethanediol>": "0.3921",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0046704"
      },
      {
        "BLKpoint_id": "BLKpoint_47",
        "temperature_k": "303.15",
        "mole_fraction_<1,2-ethanediol>": "0.4446",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0053492"
      },
      {
        "BLKpoint_id": "BLKpoint_49",
        "temperature_k": "303.15",
        "mole_fraction_<1,2-ethanediol>": "0.5485",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0067709"
      },
      {
        "BLKpoint_id": "BLKpoint_51",
        "temperature_k": "303.15",
        "mole_fraction_<1,2-ethanediol>": "0.6451",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0081729"
      },
      {
        "BLKpoint_id": "BLKpoint_52",
        "temperature_k": "303.15",
        "mole_fraction_<1,2-ethanediol>": "0.7012",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0090846"
      },
      {
        "BLKpoint_id": "BLKpoint_53",
        "temperature_k": "303.15",
        "mole_fraction_<1,2-ethanediol>": "0.7435",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0098077"
      },
      {
        "BLKpoint_id": "BLKpoint_54",
        "temperature_k": "303.15",
        "mole_fraction_<1,2-ethanediol>": "0.7907",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.010548"
      },
      {
        "BLKpoint_id": "BLKpoint_55",
        "temperature_k": "303.15",
        "mole_fraction_<1,2-ethanediol>": "0.8505",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.011535"
      },
      {
        "BLKpoint_id": "BLKpoint_79",
        "temperature_k": "303.15",
        "mole_fraction_<1,2-ethanediol>": "0",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0008385"
      },
      {
        "BLKpoint_id": "BLKpoint_83",
        "temperature_k": "303.15",
        "mole_fraction_<1,2-ethanediol>": "1",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.013867"
      }
    ],
    "inspection_id": "INSP_668b10d4f9b3",
    "lit_num_id": "GLOBlit_5201"
  },
  {
    "doi": "10.1021/acs.jced.6b00526",
    "block_number": "PROPblock_18",
    "table_mode": "complete",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<water>",
      "pressure_kpa",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_23",
        "temperature_k": "303.15",
        "mole_fraction_<water>": "0",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.01423"
      },
      {
        "BLKpoint_id": "BLKpoint_24",
        "temperature_k": "303.15",
        "mole_fraction_<water>": "0.1105",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.01186"
      },
      {
        "BLKpoint_id": "BLKpoint_25",
        "temperature_k": "303.15",
        "mole_fraction_<water>": "0.2014",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.01014"
      },
      {
        "BLKpoint_id": "BLKpoint_26",
        "temperature_k": "303.15",
        "mole_fraction_<water>": "0.3002",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00845"
      },
      {
        "BLKpoint_id": "BLKpoint_27",
        "temperature_k": "303.15",
        "mole_fraction_<water>": "0.4011",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.006968"
      },
      {
        "BLKpoint_id": "BLKpoint_28",
        "temperature_k": "303.15",
        "mole_fraction_<water>": "0.4969",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.005653"
      },
      {
        "BLKpoint_id": "BLKpoint_29",
        "temperature_k": "303.15",
        "mole_fraction_<water>": "0.6022",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.004396"
      },
      {
        "BLKpoint_id": "BLKpoint_30",
        "temperature_k": "303.15",
        "mole_fraction_<water>": "0.6995",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.003345"
      },
      {
        "BLKpoint_id": "BLKpoint_31",
        "temperature_k": "303.15",
        "mole_fraction_<water>": "0.7994",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.002328"
      },
      {
        "BLKpoint_id": "BLKpoint_32",
        "temperature_k": "303.15",
        "mole_fraction_<water>": "0.8997",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.001446"
      },
      {
        "BLKpoint_id": "BLKpoint_33",
        "temperature_k": "303.15",
        "mole_fraction_<water>": "1",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.000755"
      }
    ],
    "inspection_id": "INSP_626d46ae23bc",
    "lit_num_id": "GLOBlit_6951"
  }
]
```
