# Q2.3 — Result

**Prompt:** For validating a liquid-density model near room temperature, should I use ethanol + water or methanol + water? Which system has measurements over the broader composition and temperature ranges?

**Tool calls:** 2  |  **Time:** 546.5s  |  **Iterations:** 3  |  **Timed out:** False

---

## Answer

{
  "answer": "## Ethanol + Water vs. Methanol + Water: Mass Density Data Comparison\n\nFor validating a liquid-density model near room temperature, **ethanol + water is the stronger choice** based on the ThermoML database holdings. It offers substantially more data, broader coverage in temperature and pressure, and denser composition grids at near-ambient conditions. Here is a side-by-side comparison:\n\n### Dataset Size and Coverage\n\n| Feature | Ethanol + Water | Methanol + Water |\n|---|---|---|\n| Data blocks | 29 | ~18 (search-level estimate) |\n| Distinct DOIs | 22 | ~15 (search-level estimate) |\n| Total data points | ~2,920 | ~1,610 (search-level estimate) |\n| Temperature range | 268.1–618.2 K | 287.15–417.15 K (block-verified) |\n| Pressure range | 100–40,000 kPa | 101–29,927 kPa (block-verified) |\n| Composition range | 0–1 (full) | 0–1 (full) |\n\n### Near Room Temperature (298.15 K, atmospheric pressure)\n\n**Ethanol + water** has **54 composition points** at 298.15 K and 100 kPa in a single block alone (GLOBlit_220, PROPblock_2; DOI 10.1016/j.fluid.2004.11.019), with density spanning from 995.3 kg/m³ at x(ethanol) = 0.003 to 785.7 kg/m³ at x(ethanol) = 1.0.\n\n**Methanol + water** has **13 composition points** at 298.15 K and 101 kPa (GLOBlit_2825, PROPblock_10; DOI 10.1016/j.jct.2007.05.004), with density spanning from 787.2 kg/m³ (pure methanol) to 997.05 kg/m³ (pure water).\n\nRepresentative density values at 298.15 K for both systems:\n\n| x(alcohol) ≈ | Ethanol + Water ρ (kg/m³) | Methanol + Water ρ (kg/m³) |\n|---|---|---|\n| 0 (pure water) | 995.3 (at x = 0.003) | 997.05 |\n| ~0.1 | 954.9 (x = 0.1296) | 804.11 (at x(water) = 0.0993, i.e. x(MeOH) ≈ 0.90) — *see note* |\n| ~0.3 | 904.5 (x = 0.3009) | 840.79 (at x(water) = 0.2983, i.e. x(MeOH) ≈ 0.70) |\n| ~0.5 | 859.3 (x = 0.498) | 881.69 (at x(water) = 0.5003, i.e. x(MeOH) ≈ 0.50) |\n| 1.0 (pure alcohol) | 785.7 | 787.2 |\n\n*Note: The methanol + water block reports composition as x(water), so x(methanol) = 1 − x(water). Pure methanol densities are very similar (785.7 vs. 787.2 kg/m³), as expected for these two small alcohols.*\n\n### Why Ethanol + Water Is Preferred for Model Validation\n\n1. **~1.8× more data points** (~2,920 vs. ~1,610), providing better statistical power for parameter fitting and residual analysis.\n\n2. **Broader temperature range** (268.1–618.2 K vs. 287.15–417.15 K verified), spanning from sub-ambient to supercritical-like conditions — a 350 K window versus ~130 K.\n\n3. **Broader pressure range** (100–40,000 kPa vs. 101–29,927 kPa verified), reaching 40 MPa.\n\n4. **Much denser composition grid near room temperature**: 54 mole-fraction points at 298.15 K in a single ethanol + water block versus 13 for methanol + water. This dense grid is critical for capturing the non-linear excess volume behavior that challenges density models.\n\n5. **More independent sources** (22 DOIs vs. ~15), allowing cross-validation between laboratories.\n\n### Chemistry Insight\n\nBoth systems exhibit the classic alcohol–water density behavior: a monotonic decrease from the high density of pure water (~997 kg/m³) to the lower density of the pure alcohol (~786–787 kg/m³). The non-linearity is most pronounced in the water-rich region, where even small additions of alcohol strongly disrupt water's hydrogen-bonding network, producing significant excess volumes. Ethanol, being larger and more hydrophobic than methanol, tends to produce larger excess volume effects, making the ethanol + water system a more demanding (and therefore more informative) test case for liquid density models.\n\n### Recommendation\n\nUse **ethanol + water** as your primary validation system. Its larger dataset, broader state-space coverage, denser composition grids, and more numerous independent sources make it the superior benchmark. The methanol + water system can serve as a useful secondary validation set, particularly at atmospheric pressure and near-ambient temperatures.",
  "core_claims": [
    "For validating a liquid-density model near room temperature, ethanol + water is the stronger choice over methanol + water based on ThermoML database holdings, offering substantially more data, broader coverage in temperature and pressure, and denser composition grids at near-ambient conditions.",
    "Ethanol + water has ~2,920 total data points across 29 data blocks and 22 DOIs, compared to ~1,610 data points, ~18 blocks, and ~15 DOIs for methanol + water (methanol estimates are search-level).",
    "Ethanol + water covers a temperature range of 268.1–618.2 K and a pressure range of 100–40,000 kPa, versus 287.15–417.15 K and 101–29,927 kPa (block-verified) for methanol + water.",
    "At 298.15 K and atmospheric pressure, ethanol + water provides 54 composition points in a single block (density spanning 995.3 kg/m³ at x(ethanol) = 0.003 to 785.7 kg/m³ at x(ethanol) = 1.0), whereas methanol + water provides 13 composition points (density spanning 787.2 kg/m³ to 997.05 kg/m³).",
    "Both systems exhibit monotonic density decrease from pure water (~997 kg/m³) to pure alcohol (~786–787 kg/m³), with non-linearity most pronounced in the water-rich region due to disruption of water's hydrogen-bonding network.",
    "Ethanol + water is a more demanding test case for density models because ethanol, being larger and more hydrophobic than methanol, tends to produce larger excess volume effects.",
    "Methanol + water can serve as a useful secondary validation set, particularly at atmospheric pressure and near-ambient temperatures."
  ],
  "confidence": "medium",
  "sources": [
    {
      "doi": "10.1016/j.fluid.2004.11.019",
      "lit_num_id": "GLOBlit_220",
      "block": "PROPblock_2",
      "BLKsubsys_id": null,
      "description": "This block provides 810 mass-density data points for ethanol + water covering 298.15–348.15 K, 100–40,000 kPa, and mole fractions 0.003–1.0. It is the primary evidence for the answer's claim that ethanol + water has a dense composition grid (54 points at 298.15 K / 100 kPa) and broad pressure coverage up to 40 MPa, and it supplies the representative density values quoted in the comparison table."
    },
    {
      "doi": "10.1016/j.jct.2007.05.004",
      "lit_num_id": "GLOBlit_2825",
      "block": "PROPblock_10",
      "BLKsubsys_id": null,
      "description": "This block provides 39 mass-density data points for methanol + water at 293.15–303.15 K, 101 kPa, and full mole-fraction range (0–1). It supplies the 13 composition points at 298.15 K cited in the answer and the representative methanol + water density values, serving as the direct comparison counterpart to the ethanol + water block."
    }
  ],
  "follow_up_suggestions": [
    "Compare excess molar volume (VE) data availability for ethanol + water vs. methanol + water to further assess non-ideal mixing behavior coverage.",
    "Check whether the ethanol + water blocks spanning 268–618 K include sub-ambient and high-temperature density data at multiple compositions, or only at limiting compositions.",
    "Investigate whether any ThermoML blocks report speed-of-sound or heat-capacity data for these same systems, enabling simultaneous multi-property model validation."
  ],
  "id_catalog_snapshot": [
    {
      "type": "comp",
      "global_id": "GLOBcomp_4",
      "registry_id": "methanol",
      "name": "methanol"
    }
  ]
}

---

## Data Inspections (deterministic evidence ledger)

Hardcoded envelope merge — not agent-authored. 4 entr(ies); verbatim rows below.

- INSP_1061f889512c — GLOBlit_220::PROPblock_2 · rdp · 21 rows
- INSP_4471b90596fd — GLOBlit_8254::PROPblock_4 · rdp · 58 rows
- INSP_10785849f385 — GLOBlit_2825::PROPblock_10 · nearest · 8 rows
- INSP_5d31e929df24 — GLOBlit_2825::PROPblock_10 · rdp · 12 rows

```json
[
  {
    "doi": "10.1016/j.fluid.2004.11.019",
    "block_number": "PROPblock_2",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "pressure_kpa",
      "mole_fraction_<ethanol>",
      "mass_density_kg_m3"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "298.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.003",
        "mass_density_kg_m3": "995.3"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "temperature_k": "298.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.0184",
        "mass_density_kg_m3": "988.4"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "temperature_k": "298.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.0219",
        "mass_density_kg_m3": "987.6"
      },
      {
        "BLKpoint_id": "BLKpoint_9",
        "temperature_k": "298.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.0279",
        "mass_density_kg_m3": "984.7"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "temperature_k": "298.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.0315",
        "mass_density_kg_m3": "984"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "temperature_k": "298.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.0366",
        "mass_density_kg_m3": "981.6"
      },
      {
        "BLKpoint_id": "BLKpoint_14",
        "temperature_k": "298.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.0483",
        "mass_density_kg_m3": "977.5"
      },
      {
        "BLKpoint_id": "BLKpoint_15",
        "temperature_k": "298.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.0516",
        "mass_density_kg_m3": "977.1"
      },
      {
        "BLKpoint_id": "BLKpoint_21",
        "temperature_k": "298.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.0801",
        "mass_density_kg_m3": "968.6"
      },
      {
        "BLKpoint_id": "BLKpoint_24",
        "temperature_k": "298.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.0926",
        "mass_density_kg_m3": "965.6"
      },
      {
        "BLKpoint_id": "BLKpoint_29",
        "temperature_k": "298.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.1296",
        "mass_density_kg_m3": "954.9"
      },
      {
        "BLKpoint_id": "BLKpoint_38",
        "temperature_k": "298.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.2502",
        "mass_density_kg_m3": "918.5"
      },
      {
        "BLKpoint_id": "BLKpoint_40",
        "temperature_k": "298.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.3009",
        "mass_density_kg_m3": "904.5"
      },
      {
        "BLKpoint_id": "BLKpoint_41",
        "temperature_k": "298.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.35",
        "mass_density_kg_m3": "891.9"
      },
      {
        "BLKpoint_id": "BLKpoint_43",
        "temperature_k": "298.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.4501",
        "mass_density_kg_m3": "868.8"
      },
      {
        "BLKpoint_id": "BLKpoint_44",
        "temperature_k": "298.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.498",
        "mass_density_kg_m3": "859.3"
      },
      {
        "BLKpoint_id": "BLKpoint_45",
        "temperature_k": "298.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.5501",
        "mass_density_kg_m3": "849.5"
      },
      {
        "BLKpoint_id": "BLKpoint_47",
        "temperature_k": "298.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.6489",
        "mass_density_kg_m3": "832.7"
      },
      {
        "BLKpoint_id": "BLKpoint_48",
        "temperature_k": "298.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.6967",
        "mass_density_kg_m3": "825.2"
      },
      {
        "BLKpoint_id": "BLKpoint_51",
        "temperature_k": "298.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.8484",
        "mass_density_kg_m3": "804.4"
      },
      {
        "BLKpoint_id": "BLKpoint_54",
        "temperature_k": "298.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "1",
        "mass_density_kg_m3": "785.7"
      }
    ],
    "inspection_id": "INSP_1061f889512c",
    "lit_num_id": "GLOBlit_220"
  },
  {
    "doi": "10.1021/je034101z",
    "block_number": "PROPblock_4",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "mole_fraction_<methanol>",
      "temperature_k",
      "pressure_kpa",
      "mass_density_kg_m3"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "mole_fraction_<methanol>": "0.059",
        "temperature_k": "346.15",
        "pressure_kpa": "8815",
        "mass_density_kg_m3": "966"
      },
      {
        "BLKpoint_id": "BLKpoint_17",
        "mole_fraction_<methanol>": "0.059",
        "temperature_k": "362.15",
        "pressure_kpa": "28959",
        "mass_density_kg_m3": "964.2"
      },
      {
        "BLKpoint_id": "BLKpoint_18",
        "mole_fraction_<methanol>": "0.059",
        "temperature_k": "364.15",
        "pressure_kpa": "4292",
        "mass_density_kg_m3": "951.9"
      },
      {
        "BLKpoint_id": "BLKpoint_36",
        "mole_fraction_<methanol>": "0.059",
        "temperature_k": "382.15",
        "pressure_kpa": "28600",
        "mass_density_kg_m3": "949.8"
      },
      {
        "BLKpoint_id": "BLKpoint_37",
        "mole_fraction_<methanol>": "0.059",
        "temperature_k": "385.15",
        "pressure_kpa": "10606",
        "mass_density_kg_m3": "937.2"
      },
      {
        "BLKpoint_id": "BLKpoint_50",
        "mole_fraction_<methanol>": "0.059",
        "temperature_k": "398.15",
        "pressure_kpa": "29222",
        "mass_density_kg_m3": "935.6"
      },
      {
        "BLKpoint_id": "BLKpoint_51",
        "mole_fraction_<methanol>": "0.059",
        "temperature_k": "400.15",
        "pressure_kpa": "5808",
        "mass_density_kg_m3": "919"
      },
      {
        "BLKpoint_id": "BLKpoint_67",
        "mole_fraction_<methanol>": "0.059",
        "temperature_k": "416.15",
        "pressure_kpa": "29157",
        "mass_density_kg_m3": "917.2"
      },
      {
        "BLKpoint_id": "BLKpoint_68",
        "mole_fraction_<methanol>": "0.352",
        "temperature_k": "291.15",
        "pressure_kpa": "8041",
        "mass_density_kg_m3": "933.5"
      },
      {
        "BLKpoint_id": "BLKpoint_83",
        "mole_fraction_<methanol>": "0.352",
        "temperature_k": "306.15",
        "pressure_kpa": "25201",
        "mass_density_kg_m3": "932.2"
      },
      {
        "BLKpoint_id": "BLKpoint_84",
        "mole_fraction_<methanol>": "0.352",
        "temperature_k": "307.15",
        "pressure_kpa": "3721",
        "mass_density_kg_m3": "922.5"
      },
      {
        "BLKpoint_id": "BLKpoint_89",
        "mole_fraction_<methanol>": "0.352",
        "temperature_k": "309.15",
        "pressure_kpa": "28914",
        "mass_density_kg_m3": "931.9"
      },
      {
        "BLKpoint_id": "BLKpoint_90",
        "mole_fraction_<methanol>": "0.352",
        "temperature_k": "310.15",
        "pressure_kpa": "7400",
        "mass_density_kg_m3": "922.2"
      },
      {
        "BLKpoint_id": "BLKpoint_107",
        "mole_fraction_<methanol>": "0.352",
        "temperature_k": "327.15",
        "pressure_kpa": "28981",
        "mass_density_kg_m3": "920.6"
      },
      {
        "BLKpoint_id": "BLKpoint_108",
        "mole_fraction_<methanol>": "0.352",
        "temperature_k": "331.15",
        "pressure_kpa": "10996",
        "mass_density_kg_m3": "909.4"
      },
      {
        "BLKpoint_id": "BLKpoint_121",
        "mole_fraction_<methanol>": "0.352",
        "temperature_k": "344.15",
        "pressure_kpa": "28202",
        "mass_density_kg_m3": "908"
      },
      {
        "BLKpoint_id": "BLKpoint_122",
        "mole_fraction_<methanol>": "0.352",
        "temperature_k": "345.15",
        "pressure_kpa": "9340",
        "mass_density_kg_m3": "897.6"
      },
      {
        "BLKpoint_id": "BLKpoint_123",
        "mole_fraction_<methanol>": "0.352",
        "temperature_k": "345.15",
        "pressure_kpa": "29545",
        "mass_density_kg_m3": "907.9"
      },
      {
        "BLKpoint_id": "BLKpoint_124",
        "mole_fraction_<methanol>": "0.352",
        "temperature_k": "346.15",
        "pressure_kpa": "10663",
        "mass_density_kg_m3": "897.5"
      },
      {
        "BLKpoint_id": "BLKpoint_137",
        "mole_fraction_<methanol>": "0.352",
        "temperature_k": "359.15",
        "pressure_kpa": "28029",
        "mass_density_kg_m3": "896.2"
      },
      {
        "BLKpoint_id": "BLKpoint_138",
        "mole_fraction_<methanol>": "0.352",
        "temperature_k": "360.15",
        "pressure_kpa": "8932",
        "mass_density_kg_m3": "884.8"
      },
      {
        "BLKpoint_id": "BLKpoint_139",
        "mole_fraction_<methanol>": "0.352",
        "temperature_k": "360.15",
        "pressure_kpa": "29375",
        "mass_density_kg_m3": "896.1"
      },
      {
        "BLKpoint_id": "BLKpoint_140",
        "mole_fraction_<methanol>": "0.352",
        "temperature_k": "361.15",
        "pressure_kpa": "10269",
        "mass_density_kg_m3": "884.8"
      },
      {
        "BLKpoint_id": "BLKpoint_153",
        "mole_fraction_<methanol>": "0.352",
        "temperature_k": "374.15",
        "pressure_kpa": "27836",
        "mass_density_kg_m3": "883.4"
      },
      {
        "BLKpoint_id": "BLKpoint_154",
        "mole_fraction_<methanol>": "0.352",
        "temperature_k": "378.15",
        "pressure_kpa": "11440",
        "mass_density_kg_m3": "870"
      },
      {
        "BLKpoint_id": "BLKpoint_163",
        "mole_fraction_<methanol>": "0.352",
        "temperature_k": "387.15",
        "pressure_kpa": "23492",
        "mass_density_kg_m3": "869.1"
      },
      {
        "BLKpoint_id": "BLKpoint_164",
        "mole_fraction_<methanol>": "0.352",
        "temperature_k": "388.15",
        "pressure_kpa": "6236",
        "mass_density_kg_m3": "856.9"
      },
      {
        "BLKpoint_id": "BLKpoint_165",
        "mole_fraction_<methanol>": "0.352",
        "temperature_k": "388.15",
        "pressure_kpa": "24839",
        "mass_density_kg_m3": "869"
      },
      {
        "BLKpoint_id": "BLKpoint_166",
        "mole_fraction_<methanol>": "0.352",
        "temperature_k": "389.15",
        "pressure_kpa": "7545",
        "mass_density_kg_m3": "856.8"
      },
      {
        "BLKpoint_id": "BLKpoint_171",
        "mole_fraction_<methanol>": "0.352",
        "temperature_k": "391.15",
        "pressure_kpa": "28891",
        "mass_density_kg_m3": "868.7"
      },
      {
        "BLKpoint_id": "BLKpoint_172",
        "mole_fraction_<methanol>": "0.352",
        "temperature_k": "392.15",
        "pressure_kpa": "11481",
        "mass_density_kg_m3": "856.5"
      },
      {
        "BLKpoint_id": "BLKpoint_181",
        "mole_fraction_<methanol>": "0.352",
        "temperature_k": "401.15",
        "pressure_kpa": "23367",
        "mass_density_kg_m3": "855.6"
      },
      {
        "BLKpoint_id": "BLKpoint_182",
        "mole_fraction_<methanol>": "0.352",
        "temperature_k": "402.15",
        "pressure_kpa": "7258",
        "mass_density_kg_m3": "843.1"
      },
      {
        "BLKpoint_id": "BLKpoint_183",
        "mole_fraction_<methanol>": "0.352",
        "temperature_k": "402.15",
        "pressure_kpa": "24695",
        "mass_density_kg_m3": "855.5"
      },
      {
        "BLKpoint_id": "BLKpoint_184",
        "mole_fraction_<methanol>": "0.352",
        "temperature_k": "403.15",
        "pressure_kpa": "8545",
        "mass_density_kg_m3": "843.1"
      },
      {
        "BLKpoint_id": "BLKpoint_189",
        "mole_fraction_<methanol>": "0.352",
        "temperature_k": "405.15",
        "pressure_kpa": "28682",
        "mass_density_kg_m3": "855.2"
      },
      {
        "BLKpoint_id": "BLKpoint_190",
        "mole_fraction_<methanol>": "0.352",
        "temperature_k": "406.15",
        "pressure_kpa": "12414",
        "mass_density_kg_m3": "842.8"
      },
      {
        "BLKpoint_id": "BLKpoint_201",
        "mole_fraction_<methanol>": "0.352",
        "temperature_k": "417.15",
        "pressure_kpa": "26686",
        "mass_density_kg_m3": "841.8"
      },
      {
        "BLKpoint_id": "BLKpoint_202",
        "mole_fraction_<methanol>": "0.502",
        "temperature_k": "287.15",
        "pressure_kpa": "8823",
        "mass_density_kg_m3": "884.1"
      },
      {
        "BLKpoint_id": "BLKpoint_219",
        "mole_fraction_<methanol>": "0.502",
        "temperature_k": "304.15",
        "pressure_kpa": "29322",
        "mass_density_kg_m3": "882.4"
      },
      {
        "BLKpoint_id": "BLKpoint_220",
        "mole_fraction_<methanol>": "0.502",
        "temperature_k": "308.15",
        "pressure_kpa": "6151",
        "mass_density_kg_m3": "868.1"
      },
      {
        "BLKpoint_id": "BLKpoint_245",
        "mole_fraction_<methanol>": "0.502",
        "temperature_k": "333.15",
        "pressure_kpa": "29426",
        "mass_density_kg_m3": "865.9"
      },
      {
        "BLKpoint_id": "BLKpoint_246",
        "mole_fraction_<methanol>": "0.502",
        "temperature_k": "336.15",
        "pressure_kpa": "9956",
        "mass_density_kg_m3": "852.4"
      },
      {
        "BLKpoint_id": "BLKpoint_262",
        "mole_fraction_<methanol>": "0.502",
        "temperature_k": "352.15",
        "pressure_kpa": "28463",
        "mass_density_kg_m3": "850.8"
      },
      {
        "BLKpoint_id": "BLKpoint_263",
        "mole_fraction_<methanol>": "0.502",
        "temperature_k": "355.15",
        "pressure_kpa": "8187",
        "mass_density_kg_m3": "834.9"
      },
      {
        "BLKpoint_id": "BLKpoint_282",
        "mole_fraction_<methanol>": "0.502",
        "temperature_k": "374.15",
        "pressure_kpa": "29927",
        "mass_density_kg_m3": "833.2"
      },
      {
        "BLKpoint_id": "BLKpoint_283",
        "mole_fraction_<methanol>": "0.502",
        "temperature_k": "377.15",
        "pressure_kpa": "5641",
        "mass_density_kg_m3": "804.7"
      },
      {
        "BLKpoint_id": "BLKpoint_312",
        "mole_fraction_<methanol>": "0.502",
        "temperature_k": "406.15",
        "pressure_kpa": "29592",
        "mass_density_kg_m3": "802.6"
      },
      {
        "BLKpoint_id": "BLKpoint_313",
        "mole_fraction_<methanol>": "0.708",
        "temperature_k": "319.15",
        "pressure_kpa": "6096",
        "mass_density_kg_m3": "819.1"
      },
      {
        "BLKpoint_id": "BLKpoint_335",
        "mole_fraction_<methanol>": "0.708",
        "temperature_k": "341.15",
        "pressure_kpa": "29116",
        "mass_density_kg_m3": "817.2"
      },
      {
        "BLKpoint_id": "BLKpoint_336",
        "mole_fraction_<methanol>": "0.708",
        "temperature_k": "343.15",
        "pressure_kpa": "8107",
        "mass_density_kg_m3": "807.4"
      },
      {
        "BLKpoint_id": "BLKpoint_356",
        "mole_fraction_<methanol>": "0.708",
        "temperature_k": "363.15",
        "pressure_kpa": "28356",
        "mass_density_kg_m3": "805.6"
      },
      {
        "BLKpoint_id": "BLKpoint_357",
        "mole_fraction_<methanol>": "0.708",
        "temperature_k": "367.15",
        "pressure_kpa": "10222",
        "mass_density_kg_m3": "786.2"
      },
      {
        "BLKpoint_id": "BLKpoint_373",
        "mole_fraction_<methanol>": "0.708",
        "temperature_k": "383.15",
        "pressure_kpa": "25781",
        "mass_density_kg_m3": "784.8"
      },
      {
        "BLKpoint_id": "BLKpoint_374",
        "mole_fraction_<methanol>": "0.708",
        "temperature_k": "384.15",
        "pressure_kpa": "6211",
        "mass_density_kg_m3": "764.1"
      },
      {
        "BLKpoint_id": "BLKpoint_379",
        "mole_fraction_<methanol>": "0.708",
        "temperature_k": "386.15",
        "pressure_kpa": "28748",
        "mass_density_kg_m3": "784.6"
      },
      {
        "BLKpoint_id": "BLKpoint_380",
        "mole_fraction_<methanol>": "0.708",
        "temperature_k": "387.15",
        "pressure_kpa": "8903",
        "mass_density_kg_m3": "763.9"
      },
      {
        "BLKpoint_id": "BLKpoint_401",
        "mole_fraction_<methanol>": "0.708",
        "temperature_k": "408.15",
        "pressure_kpa": "28475",
        "mass_density_kg_m3": "762.2"
      }
    ],
    "inspection_id": "INSP_4471b90596fd",
    "lit_num_id": "GLOBlit_8254"
  },
  {
    "doi": "10.1016/j.jct.2007.05.004",
    "block_number": "PROPblock_10",
    "table_mode": "nearest",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<water>",
      "pressure_kpa",
      "mass_density_kg_m3"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_14",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "787.2"
      },
      {
        "BLKpoint_id": "BLKpoint_15",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.049",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "795.47"
      },
      {
        "BLKpoint_id": "BLKpoint_16",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.0993",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "804.11"
      },
      {
        "BLKpoint_id": "BLKpoint_17",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.1973",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "821.73"
      },
      {
        "BLKpoint_id": "BLKpoint_18",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.2983",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "840.79"
      },
      {
        "BLKpoint_id": "BLKpoint_19",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.3985",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "860.59"
      },
      {
        "BLKpoint_id": "BLKpoint_20",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.5003",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "881.69"
      },
      {
        "BLKpoint_id": "BLKpoint_21",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.5994",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "902.96"
      }
    ],
    "inspection_id": "INSP_10785849f385",
    "lit_num_id": "GLOBlit_2825"
  },
  {
    "doi": "10.1016/j.jct.2007.05.004",
    "block_number": "PROPblock_10",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<water>",
      "pressure_kpa",
      "mass_density_kg_m3"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_14",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "787.2"
      },
      {
        "BLKpoint_id": "BLKpoint_15",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.049",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "795.47"
      },
      {
        "BLKpoint_id": "BLKpoint_16",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.0993",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "804.11"
      },
      {
        "BLKpoint_id": "BLKpoint_17",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.1973",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "821.73"
      },
      {
        "BLKpoint_id": "BLKpoint_18",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.2983",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "840.79"
      },
      {
        "BLKpoint_id": "BLKpoint_19",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.3985",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "860.59"
      },
      {
        "BLKpoint_id": "BLKpoint_20",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.5003",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "881.69"
      },
      {
        "BLKpoint_id": "BLKpoint_21",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.5994",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "902.96"
      },
      {
        "BLKpoint_id": "BLKpoint_23",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.7986",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "947.17"
      },
      {
        "BLKpoint_id": "BLKpoint_24",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.8999",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "969.84"
      },
      {
        "BLKpoint_id": "BLKpoint_25",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.9512",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "982.53"
      },
      {
        "BLKpoint_id": "BLKpoint_26",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "1",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "997.05"
      }
    ],
    "inspection_id": "INSP_5d31e929df24",
    "lit_num_id": "GLOBlit_2825"
  }
]
```
