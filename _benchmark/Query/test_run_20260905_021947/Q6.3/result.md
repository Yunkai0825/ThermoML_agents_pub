# Q6.3 — Result

**Prompt:** What is the viscosity of ethanol + water mixtures at 2000 K?

**Tool calls:** 1  |  **Time:** 222.2s  |  **Iterations:** 2  |  **Timed out:** False

---

## Answer

{
  "answer": "**No data found in the ThermoML database for viscosity of ethanol + water mixtures at 2000 K.**\n\nAt 2000 K, both ethanol and water would be far above their critical temperatures and normal boiling points, so a conventional liquid-phase viscosity measurement is not physically meaningful — both components would exist as supercritical fluids or thermal decomposition products. This explains why no such data exist in the archive.\n\n### What viscosity data *are* available for ethanol + water\n\nThe ThermoML database contains dynamic viscosity (η, Pa·s) data for ethanol + water binary mixtures across **14 data blocks from 14 publications**, but all measurements are in the **liquid phase** and span only **268.1 K to 618.2 K**.\n\n#### Highest-temperature data: up to 618.2 K\n\nThe closest data to your requested temperature come from two studies that used elevated pressures to keep the mixture in a dense/liquid state:\n\n| DOI | Literature ID | Block | T range (K) | P range (kPa) | x(ethanol) | η range (Pa·s) | Points |\n|-----|---------------|-------|-------------|---------------|------------|----------------|--------|\n| 10.1016/j.fluid.2017.09.005 | GLOBlit_2092 | PROPblock_4 | 523.2–618.2 | 20 000–40 000 | 0–1 | 3.1×10⁻⁵ – 1.34×10⁻⁴ | 72 |\n| 10.1016/j.fluid.2015.07.012 | GLOBlit_1742 | PROPblock_4 | 350.7–476.2 | 10 000–40 000 | 0.1–1 | 1.07×10⁻⁴ – 7.37×10⁻⁴ | 84 |\n\n**Selected data points at the highest available temperature (618.2 K)** from GLOBlit_2092 · PROPblock_4:\n\n| T (K) | P (kPa) | x(ethanol) | η (Pa·s) |\n|-------|---------|------------|----------|\n| 618.2 | 20 000 | 0 | 7.2×10⁻⁵ |\n| 618.2 | 20 000 | 0.2 | 3.5×10⁻⁵ |\n| 618.2 | 20 000 | 0.3 | 3.1×10⁻⁵ |\n| 618.2 | 20 000 | 1 | 3.9×10⁻⁵ |\n| 618.2 | 40 000 | 0 | 8.1×10⁻⁵ |\n| 618.2 | 40 000 | 1 | 6.7×10⁻⁵ |\n\n#### Near-ambient data: 293–303 K\n\nAt more conventional conditions (atmospheric pressure), data from GLOBlit_2825 · PROPblock_11 (DOI: 10.1016/j.jct.2007.05.004) cover 293.15–303.15 K at 101 kPa, with viscosities ranging from 7.97×10⁻⁴ to 2.705×10⁻³ Pa·s across the full water mole-fraction range.\n\n### Summary\n\nThe maximum temperature with viscosity data for this system in ThermoML is **618.2 K** — still far below 2000 K. No extrapolation to 2000 K is possible from these liquid-phase measurements, and no gas-phase or supercritical viscosity data for this mixture are present in the database.",
  "core_claims": [
    "No viscosity data for ethanol + water mixtures at 2000 K exist in the ThermoML database.",
    "At 2000 K, both ethanol and water would be far above their critical temperatures, so conventional liquid-phase viscosity measurement is not physically meaningful.",
    "The ThermoML database contains dynamic viscosity data for ethanol + water binary mixtures across 14 data blocks from 14 publications, all in the liquid phase, spanning only 268.1 K to 618.2 K.",
    "The highest-temperature viscosity data available are from DOI 10.1016/j.fluid.2017.09.005 (GLOBlit_2092, PROPblock_4), covering 523.2–618.2 K at 20 000–40 000 kPa, with viscosities of 3.1×10⁻⁵ – 1.34×10⁻⁴ Pa·s.",
    "No extrapolation from the available liquid-phase measurements to 2000 K is possible, and no gas-phase or supercritical viscosity data for this mixture are present in the database."
  ],
  "confidence": "high",
  "sources": [
    {
      "doi": "10.1016/j.fluid.2017.09.005",
      "lit_num_id": "GLOBlit_2092",
      "block": "PROPblock_4",
      "BLKsubsys_id": null,
      "description": "Provides the highest-temperature viscosity data for ethanol + water in ThermoML (523.2–618.2 K, 20 000–40 000 kPa, 72 points), demonstrating that even the closest available data fall far below the requested 2000 K. The answer quotes specific data points at 618.2 K from this block."
    },
    {
      "doi": "10.1016/j.fluid.2015.07.012",
      "lit_num_id": "GLOBlit_1742",
      "block": "PROPblock_4",
      "BLKsubsys_id": null,
      "description": "Supplies additional high-pressure viscosity data for ethanol + water at 350.7–476.2 K (84 points), reinforcing that available measurements span only up to ~618 K and no data exist near 2000 K."
    },
    {
      "doi": "10.1016/j.jct.2007.05.004",
      "lit_num_id": "GLOBlit_2825",
      "block": "PROPblock_11",
      "BLKsubsys_id": null,
      "description": "Provides near-ambient viscosity data for ethanol + water at 293.15–303.15 K and 101 kPa (37 points), cited in the answer to illustrate the range of conventional liquid-phase data available in ThermoML for this system."
    }
  ],
  "follow_up_suggestions": [
    "Would you like viscosity data for ethanol + water at the highest available temperature (up to 618.2 K) at elevated pressures?",
    "Would you like to see viscosity data for ethanol + water near ambient conditions (293–303 K)?",
    "Are you interested in other thermophysical properties of ethanol + water mixtures at high temperatures?"
  ],
  "id_catalog_snapshot": []
}

---

## Data Inspections (deterministic evidence ledger)

Hardcoded envelope merge — not agent-authored. 3 entr(ies); verbatim rows below.

- INSP_987176e5cf18 — GLOBlit_2092::PROPblock_4 · rdp · 37 rows
- INSP_2bf04912dbc3 — GLOBlit_1742::PROPblock_4 · rdp · 42 rows
- INSP_78cce36f2f6f — GLOBlit_2825::PROPblock_11 · rdp · 17 rows

```json
[
  {
    "doi": "10.1016/j.fluid.2017.09.005",
    "block_number": "PROPblock_4",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "pressure_kpa",
      "mole_fraction_<ethanol>",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "523.2",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0",
        "viscosity_pa_s": "0.00011"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "temperature_k": "523.2",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0.1",
        "viscosity_pa_s": "0.00012"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "temperature_k": "523.2",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0.2",
        "viscosity_pa_s": "0.000119"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "temperature_k": "523.2",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0.6",
        "viscosity_pa_s": "9.9e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "temperature_k": "523.2",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "1",
        "viscosity_pa_s": "8.7e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_9",
        "temperature_k": "523.2",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0",
        "viscosity_pa_s": "0.000113"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "temperature_k": "523.2",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0.1",
        "viscosity_pa_s": "0.000126"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "temperature_k": "523.2",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0.2",
        "viscosity_pa_s": "0.000127"
      },
      {
        "BLKpoint_id": "BLKpoint_16",
        "temperature_k": "523.2",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "1",
        "viscosity_pa_s": "0.000103"
      },
      {
        "BLKpoint_id": "BLKpoint_17",
        "temperature_k": "523.2",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0",
        "viscosity_pa_s": "0.000115"
      },
      {
        "BLKpoint_id": "BLKpoint_18",
        "temperature_k": "523.2",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0.1",
        "viscosity_pa_s": "0.000132"
      },
      {
        "BLKpoint_id": "BLKpoint_20",
        "temperature_k": "523.2",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0.3",
        "viscosity_pa_s": "0.000134"
      },
      {
        "BLKpoint_id": "BLKpoint_21",
        "temperature_k": "523.2",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0.4",
        "viscosity_pa_s": "0.000128"
      },
      {
        "BLKpoint_id": "BLKpoint_24",
        "temperature_k": "523.2",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "1",
        "viscosity_pa_s": "0.000115"
      },
      {
        "BLKpoint_id": "BLKpoint_25",
        "temperature_k": "573.2",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0",
        "viscosity_pa_s": "9e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_28",
        "temperature_k": "573.2",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0.3",
        "viscosity_pa_s": "7e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_30",
        "temperature_k": "573.2",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0.6",
        "viscosity_pa_s": "5.7e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_32",
        "temperature_k": "573.2",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "1",
        "viscosity_pa_s": "5.3e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_33",
        "temperature_k": "573.2",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0",
        "viscosity_pa_s": "9.3e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_38",
        "temperature_k": "573.2",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0.6",
        "viscosity_pa_s": "6.9e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_40",
        "temperature_k": "573.2",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "1",
        "viscosity_pa_s": "6.6e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_41",
        "temperature_k": "573.2",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0",
        "viscosity_pa_s": "9.6e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_46",
        "temperature_k": "573.2",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0.6",
        "viscosity_pa_s": "8e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_48",
        "temperature_k": "573.2",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "1",
        "viscosity_pa_s": "7.7e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_49",
        "temperature_k": "618.2",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0",
        "viscosity_pa_s": "7.2e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_51",
        "temperature_k": "618.2",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0.2",
        "viscosity_pa_s": "3.5e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_52",
        "temperature_k": "618.2",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0.3",
        "viscosity_pa_s": "3.1e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_56",
        "temperature_k": "618.2",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "1",
        "viscosity_pa_s": "3.9e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_57",
        "temperature_k": "618.2",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0",
        "viscosity_pa_s": "7.7e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_60",
        "temperature_k": "618.2",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0.3",
        "viscosity_pa_s": "5.9e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_62",
        "temperature_k": "618.2",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0.6",
        "viscosity_pa_s": "5.5e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_64",
        "temperature_k": "618.2",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "1",
        "viscosity_pa_s": "5.5e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_65",
        "temperature_k": "618.2",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0",
        "viscosity_pa_s": "8.1e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_66",
        "temperature_k": "618.2",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0.1",
        "viscosity_pa_s": "8.1e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_69",
        "temperature_k": "618.2",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0.4",
        "viscosity_pa_s": "7e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_70",
        "temperature_k": "618.2",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0.6",
        "viscosity_pa_s": "6.7e-05"
      },
      {
        "BLKpoint_id": "BLKpoint_72",
        "temperature_k": "618.2",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "1",
        "viscosity_pa_s": "6.7e-05"
      }
    ],
    "inspection_id": "INSP_987176e5cf18",
    "lit_num_id": "GLOBlit_2092"
  },
  {
    "doi": "10.1016/j.fluid.2015.07.012",
    "block_number": "PROPblock_4",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "pressure_kpa",
      "mole_fraction_<ethanol>",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "350.7",
        "pressure_kpa": "10000",
        "mole_fraction_<ethanol>": "0.1",
        "viscosity_pa_s": "0.000537"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "temperature_k": "350.7",
        "pressure_kpa": "10000",
        "mole_fraction_<ethanol>": "0.2",
        "viscosity_pa_s": "0.000625"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "temperature_k": "350.7",
        "pressure_kpa": "10000",
        "mole_fraction_<ethanol>": "0.4",
        "viscosity_pa_s": "0.00064"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "temperature_k": "350.7",
        "pressure_kpa": "10000",
        "mole_fraction_<ethanol>": "0.6",
        "viscosity_pa_s": "0.000595"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "temperature_k": "350.7",
        "pressure_kpa": "10000",
        "mole_fraction_<ethanol>": "1",
        "viscosity_pa_s": "0.000461"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "temperature_k": "350.7",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0.1",
        "viscosity_pa_s": "0.000546"
      },
      {
        "BLKpoint_id": "BLKpoint_9",
        "temperature_k": "350.7",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0.2",
        "viscosity_pa_s": "0.000638"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "temperature_k": "350.7",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0.4",
        "viscosity_pa_s": "0.000669"
      },
      {
        "BLKpoint_id": "BLKpoint_14",
        "temperature_k": "350.7",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "1",
        "viscosity_pa_s": "0.000518"
      },
      {
        "BLKpoint_id": "BLKpoint_15",
        "temperature_k": "350.7",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0.1",
        "viscosity_pa_s": "0.000556"
      },
      {
        "BLKpoint_id": "BLKpoint_16",
        "temperature_k": "350.7",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0.2",
        "viscosity_pa_s": "0.000651"
      },
      {
        "BLKpoint_id": "BLKpoint_18",
        "temperature_k": "350.7",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0.4",
        "viscosity_pa_s": "0.000691"
      },
      {
        "BLKpoint_id": "BLKpoint_21",
        "temperature_k": "350.7",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "1",
        "viscosity_pa_s": "0.000555"
      },
      {
        "BLKpoint_id": "BLKpoint_22",
        "temperature_k": "350.7",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0.1",
        "viscosity_pa_s": "0.000578"
      },
      {
        "BLKpoint_id": "BLKpoint_23",
        "temperature_k": "350.7",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0.2",
        "viscosity_pa_s": "0.000681"
      },
      {
        "BLKpoint_id": "BLKpoint_24",
        "temperature_k": "350.7",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0.3",
        "viscosity_pa_s": "0.000726"
      },
      {
        "BLKpoint_id": "BLKpoint_25",
        "temperature_k": "350.7",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0.4",
        "viscosity_pa_s": "0.000737"
      },
      {
        "BLKpoint_id": "BLKpoint_28",
        "temperature_k": "350.7",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "1",
        "viscosity_pa_s": "0.00059"
      },
      {
        "BLKpoint_id": "BLKpoint_29",
        "temperature_k": "373.2",
        "pressure_kpa": "10000",
        "mole_fraction_<ethanol>": "0.1",
        "viscosity_pa_s": "0.000401"
      },
      {
        "BLKpoint_id": "BLKpoint_30",
        "temperature_k": "373.2",
        "pressure_kpa": "10000",
        "mole_fraction_<ethanol>": "0.2",
        "viscosity_pa_s": "0.000448"
      },
      {
        "BLKpoint_id": "BLKpoint_32",
        "temperature_k": "373.2",
        "pressure_kpa": "10000",
        "mole_fraction_<ethanol>": "0.4",
        "viscosity_pa_s": "0.000462"
      },
      {
        "BLKpoint_id": "BLKpoint_34",
        "temperature_k": "373.2",
        "pressure_kpa": "10000",
        "mole_fraction_<ethanol>": "0.8",
        "viscosity_pa_s": "0.000381"
      },
      {
        "BLKpoint_id": "BLKpoint_35",
        "temperature_k": "373.2",
        "pressure_kpa": "10000",
        "mole_fraction_<ethanol>": "1",
        "viscosity_pa_s": "0.000364"
      },
      {
        "BLKpoint_id": "BLKpoint_36",
        "temperature_k": "373.2",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0.1",
        "viscosity_pa_s": "0.000397"
      },
      {
        "BLKpoint_id": "BLKpoint_37",
        "temperature_k": "373.2",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0.2",
        "viscosity_pa_s": "0.000449"
      },
      {
        "BLKpoint_id": "BLKpoint_39",
        "temperature_k": "373.2",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0.4",
        "viscosity_pa_s": "0.000477"
      },
      {
        "BLKpoint_id": "BLKpoint_42",
        "temperature_k": "373.2",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "1",
        "viscosity_pa_s": "0.000382"
      },
      {
        "BLKpoint_id": "BLKpoint_43",
        "temperature_k": "373.2",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0.1",
        "viscosity_pa_s": "0.000403"
      },
      {
        "BLKpoint_id": "BLKpoint_44",
        "temperature_k": "373.2",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0.2",
        "viscosity_pa_s": "0.000459"
      },
      {
        "BLKpoint_id": "BLKpoint_46",
        "temperature_k": "373.2",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0.4",
        "viscosity_pa_s": "0.000489"
      },
      {
        "BLKpoint_id": "BLKpoint_49",
        "temperature_k": "373.2",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "1",
        "viscosity_pa_s": "0.000404"
      },
      {
        "BLKpoint_id": "BLKpoint_50",
        "temperature_k": "373.2",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0.1",
        "viscosity_pa_s": "0.000421"
      },
      {
        "BLKpoint_id": "BLKpoint_52",
        "temperature_k": "373.2",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0.3",
        "viscosity_pa_s": "0.000515"
      },
      {
        "BLKpoint_id": "BLKpoint_56",
        "temperature_k": "373.2",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "1",
        "viscosity_pa_s": "0.000443"
      },
      {
        "BLKpoint_id": "BLKpoint_57",
        "temperature_k": "476.2",
        "pressure_kpa": "10000",
        "mole_fraction_<ethanol>": "0.1",
        "viscosity_pa_s": "0.000148"
      },
      {
        "BLKpoint_id": "BLKpoint_63",
        "temperature_k": "476.2",
        "pressure_kpa": "10000",
        "mole_fraction_<ethanol>": "1",
        "viscosity_pa_s": "0.000107"
      },
      {
        "BLKpoint_id": "BLKpoint_64",
        "temperature_k": "476.2",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0.1",
        "viscosity_pa_s": "0.000152"
      },
      {
        "BLKpoint_id": "BLKpoint_70",
        "temperature_k": "476.2",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "1",
        "viscosity_pa_s": "0.000123"
      },
      {
        "BLKpoint_id": "BLKpoint_71",
        "temperature_k": "476.2",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0.1",
        "viscosity_pa_s": "0.000159"
      },
      {
        "BLKpoint_id": "BLKpoint_77",
        "temperature_k": "476.2",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "1",
        "viscosity_pa_s": "0.000138"
      },
      {
        "BLKpoint_id": "BLKpoint_78",
        "temperature_k": "476.2",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0.1",
        "viscosity_pa_s": "0.000164"
      },
      {
        "BLKpoint_id": "BLKpoint_84",
        "temperature_k": "476.2",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "1",
        "viscosity_pa_s": "0.000151"
      }
    ],
    "inspection_id": "INSP_2bf04912dbc3",
    "lit_num_id": "GLOBlit_1742"
  },
  {
    "doi": "10.1016/j.jct.2007.05.004",
    "block_number": "PROPblock_11",
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
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "293.15",
        "mole_fraction_<water>": "0",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001187"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "temperature_k": "293.15",
        "mole_fraction_<water>": "0.2961",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001735"
      },
      {
        "BLKpoint_id": "BLKpoint_9",
        "temperature_k": "293.15",
        "mole_fraction_<water>": "0.6991",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002705"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "temperature_k": "293.15",
        "mole_fraction_<water>": "0.8001",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0027"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "temperature_k": "293.15",
        "mole_fraction_<water>": "0.8996",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002223"
      },
      {
        "BLKpoint_id": "BLKpoint_13",
        "temperature_k": "293.15",
        "mole_fraction_<water>": "1",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001002"
      },
      {
        "BLKpoint_id": "BLKpoint_14",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001082"
      },
      {
        "BLKpoint_id": "BLKpoint_19",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.3991",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001659"
      },
      {
        "BLKpoint_id": "BLKpoint_21",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.6991",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002275"
      },
      {
        "BLKpoint_id": "BLKpoint_22",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.8001",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0023"
      },
      {
        "BLKpoint_id": "BLKpoint_23",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.8996",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.00186"
      },
      {
        "BLKpoint_id": "BLKpoint_25",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "1",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.00089"
      },
      {
        "BLKpoint_id": "BLKpoint_26",
        "temperature_k": "303.15",
        "mole_fraction_<water>": "0",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.000987"
      },
      {
        "BLKpoint_id": "BLKpoint_33",
        "temperature_k": "303.15",
        "mole_fraction_<water>": "0.6991",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001941"
      },
      {
        "BLKpoint_id": "BLKpoint_34",
        "temperature_k": "303.15",
        "mole_fraction_<water>": "0.8001",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001937"
      },
      {
        "BLKpoint_id": "BLKpoint_35",
        "temperature_k": "303.15",
        "mole_fraction_<water>": "0.8996",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.00158"
      },
      {
        "BLKpoint_id": "BLKpoint_37",
        "temperature_k": "303.15",
        "mole_fraction_<water>": "1",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.000797"
      }
    ],
    "inspection_id": "INSP_78cce36f2f6f",
    "lit_num_id": "GLOBlit_2825"
  }
]
```
