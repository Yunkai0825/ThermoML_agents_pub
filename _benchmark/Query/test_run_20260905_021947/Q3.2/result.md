# Q3.2 — Result

**Prompt:** I am building an activity-coefficient correlation for ethanol + water over the widest possible temperature range. What range can the experimental literature support, and which studies provide the coldest and hottest measurements?

**Tool calls:** 2  |  **Time:** 630.8s  |  **Iterations:** 3  |  **Timed out:** False

---

## Answer

{
  "answer": "## Activity Coefficient Data for Ethanol + Water: Temperature Range and Key Studies\n\n### Verified Temperature Range\n\nThe ThermoML database contains **6 data blocks** of activity coefficient measurements for the ethanol + water binary system, spanning a verified temperature range of **273.35 K to 372.15 K** across **23 data points** from **4 publications**. All blocks report the **infinite-dilution activity coefficient of ethanol** (γ∞, with mole fraction of ethanol = 0.0).\n\n---\n\n### Coldest Measurement\n\n**273.35 K** — from Vrba, Fenclová et al. (DOI: 10.1016/j.fluid.2005.08.018), PROPblock_4, measured by headspace analysis:\n\n| Temperature (K) | x(ethanol) | γ∞(ethanol) |\n|:---:|:---:|:---:|\n| 273.35 | 0.0 | 2.54 |\n| 283.15 | 0.0 | 3.13 |\n\n### Hottest Measurement\n\n**372.15 K** — from the same publication (DOI: 10.1016/j.fluid.2005.08.018), PROPblock_6, measured by a circulating still method:\n\n| Temperature (K) | x(ethanol) | γ∞(ethanol) |\n|:---:|:---:|:---:|\n| 358.15 | 0.0 | 5.9 |\n| 363.15 | 0.0 | 6.0 |\n| 368.15 | 0.0 | 6.1 |\n| 372.15 | 0.0 | 6.2 |\n\n---\n\n### Complete Block-by-Block Inventory\n\n| Source | DOI | Block | Method | T range (K) | γ∞ range | Points | Trend |\n|---|---|---|---|:---:|:---:|:---:|:---:|\n| GLOBlit_299 | 10.1016/j.fluid.2005.08.018 | PROPblock_4 | Headspace analysis | 273.35–283.15 | 2.54–3.13 | 2 | ↑ |\n| GLOBlit_299 | 10.1016/j.fluid.2005.08.018 | PROPblock_5 | Comparative tensimetry | 303.15–333.15 | 4.14–5.3 | 7 | ↑ |\n| GLOBlit_299 | 10.1016/j.fluid.2005.08.018 | PROPblock_6 | Circulating still | 358.15–372.15 | 5.9–6.2 | 4 | ↑ |\n| GLOBlit_8381 | 10.1021/je0495942 | PROPblock_1 | Chromatography | 298.15 | 3.77 | 1 | — |\n| GLOBlit_8511 | 10.1021/je049875+ | PROPblock_1 | Dilutor chromatography | 303.25–343.25 | 5.03–5.96 | 5 | ↑ |\n| GLOBlit_1971 | 10.1016/j.fluid.2016.08.030 | PROPblock_1 | Solid-phase micro-extraction | 323.15–353.15 | 4.11–5.17 | 4 | **↓ (anomalous)** |\n\n---\n\n### Chemistry Insight and Recommendations for Correlation Building\n\n**Consistent data (5 of 6 blocks, 19 points):** In five blocks, γ∞ of ethanol increases monotonically with temperature — physically expected for a system where the hydrophobic interaction between ethanol and water weakens as thermal energy disrupts the hydrogen-bond network. The single most valuable publication is Vrba, Fenclová et al. (DOI: 10.1016/j.fluid.2005.08.018), which alone provides nearly continuous coverage from 273.35 K to 372.15 K using three complementary experimental techniques (headspace analysis, comparative tensimetry, circulating still), contributing 13 of the 19 consistent data points.\n\n**Anomalous dataset — GLOBlit_1971 (DOI: 10.1016/j.fluid.2016.08.030):** This SPME-method dataset shows γ∞ *decreasing* from 5.17 at 323.15 K to 4.11 at 353.15 K, which contradicts every other source. For direct comparison at ~323 K: GLOBlit_1971 reports 5.17, GLOBlit_8511 reports 5.54 (at 323.25 K), and GLOBlit_299 PROPblock_5 reports 5.03 (at 323.15 K). While the absolute values at the lowest temperature are in the same ballpark, the reversed temperature trend is physically suspect and this dataset should be critically evaluated — or excluded — before inclusion in a correlation.\n\n**Practical correlation range:** Your activity-coefficient correlation for ethanol + water can be reliably supported over **273.35 K to 372.15 K** using 19 data points from 3 independent publications with mutually consistent temperature trends.",
  "core_claims": [
    "The ThermoML database contains 6 data blocks of infinite-dilution activity coefficient measurements for ethanol in water, spanning a verified temperature range of 273.35 K to 372.15 K across 23 data points from 4 publications.",
    "All blocks report the infinite-dilution activity coefficient of ethanol (γ∞ at ethanol mole fraction = 0.0).",
    "The coldest measurement is 273.35 K (γ∞ = 2.54) and the hottest is 372.15 K (γ∞ = 6.2), both from Vrba, Fenclová et al. (DOI: 10.1016/j.fluid.2005.08.018).",
    "In 5 of 6 blocks (19 data points), γ∞ of ethanol increases monotonically with temperature, consistent with weakening hydrophobic interactions as thermal energy disrupts the hydrogen-bond network.",
    "One dataset (GLOBlit_1971, DOI: 10.1016/j.fluid.2016.08.030, SPME method, 4 points from 323.15–353.15 K) shows γ∞ decreasing from 5.17 to 4.11 with increasing temperature, contradicting every other source and exhibiting a physically suspect reversed temperature trend.",
    "A reliable activity-coefficient correlation for ethanol + water can be supported over 273.35 K to 372.15 K using 19 mutually consistent data points from 3 independent publications."
  ],
  "confidence": "high",
  "sources": [
    {
      "doi": "10.1016/j.fluid.2005.08.018",
      "lit_num_id": "GLOBlit_299",
      "block": "PROPblock_4",
      "BLKsubsys_id": null,
      "description": "Provides the coldest activity coefficient measurements for ethanol+water at 273.35–283.15 K (γ∞ = 2.54–3.13) via headspace analysis, establishing the lower bound of the verified temperature range."
    },
    {
      "doi": "10.1016/j.fluid.2005.08.018",
      "lit_num_id": "GLOBlit_299",
      "block": "PROPblock_5",
      "BLKsubsys_id": null,
      "description": "Supplies 7 data points of infinite-dilution activity coefficients for ethanol in water over 303.15–333.15 K (γ∞ = 4.14–5.3) by comparative tensimetry, filling the mid-temperature range."
    },
    {
      "doi": "10.1016/j.fluid.2005.08.018",
      "lit_num_id": "GLOBlit_299",
      "block": "PROPblock_6",
      "BLKsubsys_id": null,
      "description": "Provides the hottest measurements at 358.15–372.15 K (γ∞ = 5.9–6.2) via circulating still method, establishing the upper bound of the verified temperature range at 372.15 K."
    },
    {
      "doi": "10.1021/je0495942",
      "lit_num_id": "GLOBlit_8381",
      "block": "PROPblock_1",
      "BLKsubsys_id": null,
      "description": "Contributes a single infinite-dilution activity coefficient data point for ethanol in water at 298.15 K (γ∞ = 3.77) by chromatography, providing an independent check in the near-ambient region."
    },
    {
      "doi": "10.1021/je049875+",
      "lit_num_id": "GLOBlit_8511",
      "block": "PROPblock_1",
      "BLKsubsys_id": null,
      "description": "Provides 5 data points of γ∞ for ethanol in water over 303.25–343.25 K (γ∞ = 5.03–5.96) by dilutor chromatography, offering independent corroboration of the monotonically increasing trend in the mid-temperature range."
    },
    {
      "doi": "10.1016/j.fluid.2016.08.030",
      "lit_num_id": "GLOBlit_1971",
      "block": "PROPblock_1",
      "BLKsubsys_id": null,
      "description": "Provides 4 data points of γ∞ for ethanol in water over 323.15–353.15 K (γ∞ = 4.11–5.17) by SPME; the answer correctly identifies this block's anomalous decreasing trend and recommends critical evaluation before use in correlations."
    }
  ],
  "follow_up_suggestions": [
    "Retrieve finite-concentration activity coefficient data for ethanol + water to complement the infinite-dilution values and improve mid-range correlation accuracy.",
    "Search for VLE (vapor-liquid equilibrium) datasets for ethanol + water above 372 K to extend the correlation toward the mixture critical region.",
    "Investigate the SPME methodology used in GLOBlit_1971 to determine whether the anomalous decreasing trend in γ∞ with temperature is a systematic artifact before deciding on exclusion."
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

Hardcoded envelope merge — not agent-authored. 8 entr(ies); verbatim rows below.

- INSP_3198d97ab157 — GLOBlit_2732::PROPblock_4 · rdp · 28 rows
- INSP_a2f513326a7b — GLOBlit_299::PROPblock_4 · complete · 2 rows
- INSP_168e6ede2830 — GLOBlit_977::PROPblock_1 · rdp · 40 rows
- INSP_c78d07681916 — GLOBlit_299::PROPblock_6 · complete · 4 rows
- INSP_07cd1fbb6c30 — GLOBlit_299::PROPblock_5 · complete · 7 rows
- INSP_5c2b90e51939 — GLOBlit_1971::PROPblock_1 · complete · 4 rows
- INSP_af7f92cdc6e6 — GLOBlit_8511::PROPblock_1 · complete · 5 rows
- INSP_fd8734d59843 — GLOBlit_8381::PROPblock_1 · complete · 1 rows

```json
[
  {
    "doi": "10.1016/j.jct.2006.08.002",
    "block_number": "PROPblock_4",
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
        "BLKpoint_id": "BLKpoint_248",
        "temperature_k": "673.15",
        "pressure_kpa": "6990",
        "mole_fraction_<ethanol>": "0.8",
        "mass_density_kg_m3": "52.89"
      },
      {
        "BLKpoint_id": "BLKpoint_249",
        "temperature_k": "673.15",
        "pressure_kpa": "8570",
        "mole_fraction_<ethanol>": "0.5",
        "mass_density_kg_m3": "55.65"
      },
      {
        "BLKpoint_id": "BLKpoint_251",
        "temperature_k": "673.15",
        "pressure_kpa": "12250",
        "mole_fraction_<ethanol>": "0.5",
        "mass_density_kg_m3": "83.95"
      },
      {
        "BLKpoint_id": "BLKpoint_252",
        "temperature_k": "673.15",
        "pressure_kpa": "12980",
        "mole_fraction_<ethanol>": "0.2",
        "mass_density_kg_m3": "67.32"
      },
      {
        "BLKpoint_id": "BLKpoint_253",
        "temperature_k": "673.15",
        "pressure_kpa": "13010",
        "mole_fraction_<ethanol>": "0.8",
        "mass_density_kg_m3": "114.36"
      },
      {
        "BLKpoint_id": "BLKpoint_254",
        "temperature_k": "673.15",
        "pressure_kpa": "15740",
        "mole_fraction_<ethanol>": "0.5",
        "mass_density_kg_m3": "116.78"
      },
      {
        "BLKpoint_id": "BLKpoint_255",
        "temperature_k": "673.15",
        "pressure_kpa": "15940",
        "mole_fraction_<ethanol>": "0.2",
        "mass_density_kg_m3": "89.72"
      },
      {
        "BLKpoint_id": "BLKpoint_256",
        "temperature_k": "673.15",
        "pressure_kpa": "19310",
        "mole_fraction_<ethanol>": "0.8",
        "mass_density_kg_m3": "187.46"
      },
      {
        "BLKpoint_id": "BLKpoint_257",
        "temperature_k": "673.15",
        "pressure_kpa": "20680",
        "mole_fraction_<ethanol>": "0.5",
        "mass_density_kg_m3": "170.3"
      },
      {
        "BLKpoint_id": "BLKpoint_258",
        "temperature_k": "673.15",
        "pressure_kpa": "21310",
        "mole_fraction_<ethanol>": "0.2",
        "mass_density_kg_m3": "137.56"
      },
      {
        "BLKpoint_id": "BLKpoint_259",
        "temperature_k": "673.15",
        "pressure_kpa": "23620",
        "mole_fraction_<ethanol>": "0.8",
        "mass_density_kg_m3": "242.38"
      },
      {
        "BLKpoint_id": "BLKpoint_260",
        "temperature_k": "673.15",
        "pressure_kpa": "25130",
        "mole_fraction_<ethanol>": "0.8",
        "mass_density_kg_m3": "259.1"
      },
      {
        "BLKpoint_id": "BLKpoint_261",
        "temperature_k": "673.15",
        "pressure_kpa": "25740",
        "mole_fraction_<ethanol>": "0.5",
        "mass_density_kg_m3": "233.23"
      },
      {
        "BLKpoint_id": "BLKpoint_262",
        "temperature_k": "673.15",
        "pressure_kpa": "27230",
        "mole_fraction_<ethanol>": "0.8",
        "mass_density_kg_m3": "282.28"
      },
      {
        "BLKpoint_id": "BLKpoint_263",
        "temperature_k": "673.15",
        "pressure_kpa": "27430",
        "mole_fraction_<ethanol>": "0.2",
        "mass_density_kg_m3": "220.84"
      },
      {
        "BLKpoint_id": "BLKpoint_264",
        "temperature_k": "673.15",
        "pressure_kpa": "29500",
        "mole_fraction_<ethanol>": "0.8",
        "mass_density_kg_m3": "305.19"
      },
      {
        "BLKpoint_id": "BLKpoint_265",
        "temperature_k": "673.15",
        "pressure_kpa": "30040",
        "mole_fraction_<ethanol>": "0.8",
        "mass_density_kg_m3": "310.49"
      },
      {
        "BLKpoint_id": "BLKpoint_267",
        "temperature_k": "673.15",
        "pressure_kpa": "31230",
        "mole_fraction_<ethanol>": "0.2",
        "mass_density_kg_m3": "285.57"
      },
      {
        "BLKpoint_id": "BLKpoint_269",
        "temperature_k": "673.15",
        "pressure_kpa": "33730",
        "mole_fraction_<ethanol>": "0.2",
        "mass_density_kg_m3": "323.66"
      },
      {
        "BLKpoint_id": "BLKpoint_270",
        "temperature_k": "673.15",
        "pressure_kpa": "34050",
        "mole_fraction_<ethanol>": "0.5",
        "mass_density_kg_m3": "325.37"
      },
      {
        "BLKpoint_id": "BLKpoint_271",
        "temperature_k": "673.15",
        "pressure_kpa": "35510",
        "mole_fraction_<ethanol>": "0.2",
        "mass_density_kg_m3": "349.48"
      },
      {
        "BLKpoint_id": "BLKpoint_272",
        "temperature_k": "673.15",
        "pressure_kpa": "36420",
        "mole_fraction_<ethanol>": "0.8",
        "mass_density_kg_m3": "365.05"
      },
      {
        "BLKpoint_id": "BLKpoint_273",
        "temperature_k": "673.15",
        "pressure_kpa": "38700",
        "mole_fraction_<ethanol>": "0.8",
        "mass_density_kg_m3": "380.23"
      },
      {
        "BLKpoint_id": "BLKpoint_274",
        "temperature_k": "673.15",
        "pressure_kpa": "40850",
        "mole_fraction_<ethanol>": "0.5",
        "mass_density_kg_m3": "383.2"
      },
      {
        "BLKpoint_id": "BLKpoint_275",
        "temperature_k": "673.15",
        "pressure_kpa": "42660",
        "mole_fraction_<ethanol>": "0.2",
        "mass_density_kg_m3": "420.24"
      },
      {
        "BLKpoint_id": "BLKpoint_276",
        "temperature_k": "673.15",
        "pressure_kpa": "42950",
        "mole_fraction_<ethanol>": "0.8",
        "mass_density_kg_m3": "403.08"
      },
      {
        "BLKpoint_id": "BLKpoint_277",
        "temperature_k": "673.15",
        "pressure_kpa": "46620",
        "mole_fraction_<ethanol>": "0.5",
        "mass_density_kg_m3": "418.66"
      },
      {
        "BLKpoint_id": "BLKpoint_278",
        "temperature_k": "673.15",
        "pressure_kpa": "47140",
        "mole_fraction_<ethanol>": "0.2",
        "mass_density_kg_m3": "451.15"
      }
    ],
    "inspection_id": "INSP_3198d97ab157",
    "lit_num_id": "GLOBlit_2732"
  },
  {
    "doi": "10.1016/j.fluid.2005.08.018",
    "block_number": "PROPblock_4",
    "table_mode": "complete",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<ethanol>",
      "activity_coefficient_<ethanol>"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "273.35",
        "mole_fraction_<ethanol>": "0.0",
        "activity_coefficient_<ethanol>": "2.54"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "temperature_k": "283.15",
        "mole_fraction_<ethanol>": "0.0",
        "activity_coefficient_<ethanol>": "3.13"
      }
    ],
    "inspection_id": "INSP_a2f513326a7b",
    "lit_num_id": "GLOBlit_299"
  },
  {
    "doi": "10.1016/j.fluid.2011.06.009",
    "block_number": "PROPblock_1",
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
        "mole_fraction_<ethanol>": "0.063",
        "pressure_kpa": "32.86",
        "boiling_temperature_at_pressure_p_k": "335.16"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "mole_fraction_<ethanol>": "0.076",
        "pressure_kpa": "19.71",
        "boiling_temperature_at_pressure_p_k": "323.53"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "mole_fraction_<ethanol>": "0.104",
        "pressure_kpa": "32.86",
        "boiling_temperature_at_pressure_p_k": "332.54"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "mole_fraction_<ethanol>": "0.117",
        "pressure_kpa": "13.15",
        "boiling_temperature_at_pressure_p_k": "313.71"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "mole_fraction_<ethanol>": "0.141",
        "pressure_kpa": "19.71",
        "boiling_temperature_at_pressure_p_k": "320.52"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "mole_fraction_<ethanol>": "0.15",
        "pressure_kpa": "32.86",
        "boiling_temperature_at_pressure_p_k": "330.96"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "mole_fraction_<ethanol>": "0.241",
        "pressure_kpa": "13.15",
        "boiling_temperature_at_pressure_p_k": "310.7"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "mole_fraction_<ethanol>": "0.248",
        "pressure_kpa": "32.86",
        "boiling_temperature_at_pressure_p_k": "329.26"
      },
      {
        "BLKpoint_id": "BLKpoint_9",
        "mole_fraction_<ethanol>": "0.26",
        "pressure_kpa": "19.71",
        "boiling_temperature_at_pressure_p_k": "318.05"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "mole_fraction_<ethanol>": "0.383",
        "pressure_kpa": "13.15",
        "boiling_temperature_at_pressure_p_k": "309.53"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "mole_fraction_<ethanol>": "0.39",
        "pressure_kpa": "19.71",
        "boiling_temperature_at_pressure_p_k": "317.04"
      },
      {
        "BLKpoint_id": "BLKpoint_12",
        "mole_fraction_<ethanol>": "0.454",
        "pressure_kpa": "32.86",
        "boiling_temperature_at_pressure_p_k": "326.77"
      },
      {
        "BLKpoint_id": "BLKpoint_13",
        "mole_fraction_<ethanol>": "0.492",
        "pressure_kpa": "13.15",
        "boiling_temperature_at_pressure_p_k": "308.82"
      },
      {
        "BLKpoint_id": "BLKpoint_14",
        "mole_fraction_<ethanol>": "0.499",
        "pressure_kpa": "19.71",
        "boiling_temperature_at_pressure_p_k": "316.35"
      },
      {
        "BLKpoint_id": "BLKpoint_15",
        "mole_fraction_<ethanol>": "0.581",
        "pressure_kpa": "32.86",
        "boiling_temperature_at_pressure_p_k": "326.1"
      },
      {
        "BLKpoint_id": "BLKpoint_16",
        "mole_fraction_<ethanol>": "0.59",
        "pressure_kpa": "13.15",
        "boiling_temperature_at_pressure_p_k": "308.36"
      },
      {
        "BLKpoint_id": "BLKpoint_17",
        "mole_fraction_<ethanol>": "0.599",
        "pressure_kpa": "19.71",
        "boiling_temperature_at_pressure_p_k": "315.9"
      },
      {
        "BLKpoint_id": "BLKpoint_18",
        "mole_fraction_<ethanol>": "0.656",
        "pressure_kpa": "13.15",
        "boiling_temperature_at_pressure_p_k": "308.1"
      },
      {
        "BLKpoint_id": "BLKpoint_19",
        "mole_fraction_<ethanol>": "0.657",
        "pressure_kpa": "32.86",
        "boiling_temperature_at_pressure_p_k": "325.89"
      },
      {
        "BLKpoint_id": "BLKpoint_20",
        "mole_fraction_<ethanol>": "0.688",
        "pressure_kpa": "19.71",
        "boiling_temperature_at_pressure_p_k": "315.55"
      },
      {
        "BLKpoint_id": "BLKpoint_21",
        "mole_fraction_<ethanol>": "0.76",
        "pressure_kpa": "32.86",
        "boiling_temperature_at_pressure_p_k": "325.67"
      },
      {
        "BLKpoint_id": "BLKpoint_22",
        "mole_fraction_<ethanol>": "0.771",
        "pressure_kpa": "13.15",
        "boiling_temperature_at_pressure_p_k": "307.7"
      },
      {
        "BLKpoint_id": "BLKpoint_24",
        "mole_fraction_<ethanol>": "0.805",
        "pressure_kpa": "19.71",
        "boiling_temperature_at_pressure_p_k": "315.26"
      },
      {
        "BLKpoint_id": "BLKpoint_25",
        "mole_fraction_<ethanol>": "0.839",
        "pressure_kpa": "32.86",
        "boiling_temperature_at_pressure_p_k": "325.53"
      },
      {
        "BLKpoint_id": "BLKpoint_26",
        "mole_fraction_<ethanol>": "0.84",
        "pressure_kpa": "13.15",
        "boiling_temperature_at_pressure_p_k": "307.54"
      },
      {
        "BLKpoint_id": "BLKpoint_27",
        "mole_fraction_<ethanol>": "0.841",
        "pressure_kpa": "19.71",
        "boiling_temperature_at_pressure_p_k": "315.19"
      },
      {
        "BLKpoint_id": "BLKpoint_28",
        "mole_fraction_<ethanol>": "0.854",
        "pressure_kpa": "32.86",
        "boiling_temperature_at_pressure_p_k": "325.51"
      },
      {
        "BLKpoint_id": "BLKpoint_29",
        "mole_fraction_<ethanol>": "0.864",
        "pressure_kpa": "13.15",
        "boiling_temperature_at_pressure_p_k": "307.56"
      },
      {
        "BLKpoint_id": "BLKpoint_30",
        "mole_fraction_<ethanol>": "0.883",
        "pressure_kpa": "19.71",
        "boiling_temperature_at_pressure_p_k": "315.15"
      },
      {
        "BLKpoint_id": "BLKpoint_33",
        "mole_fraction_<ethanol>": "0.911",
        "pressure_kpa": "13.15",
        "boiling_temperature_at_pressure_p_k": "307.5"
      },
      {
        "BLKpoint_id": "BLKpoint_34",
        "mole_fraction_<ethanol>": "0.913",
        "pressure_kpa": "19.71",
        "boiling_temperature_at_pressure_p_k": "315.16"
      },
      {
        "BLKpoint_id": "BLKpoint_35",
        "mole_fraction_<ethanol>": "0.913",
        "pressure_kpa": "32.86",
        "boiling_temperature_at_pressure_p_k": "325.46"
      },
      {
        "BLKpoint_id": "BLKpoint_36",
        "mole_fraction_<ethanol>": "0.931",
        "pressure_kpa": "19.71",
        "boiling_temperature_at_pressure_p_k": "315.13"
      },
      {
        "BLKpoint_id": "BLKpoint_37",
        "mole_fraction_<ethanol>": "0.931",
        "pressure_kpa": "32.86",
        "boiling_temperature_at_pressure_p_k": "325.43"
      },
      {
        "BLKpoint_id": "BLKpoint_39",
        "mole_fraction_<ethanol>": "0.934",
        "pressure_kpa": "13.15",
        "boiling_temperature_at_pressure_p_k": "307.48"
      },
      {
        "BLKpoint_id": "BLKpoint_40",
        "mole_fraction_<ethanol>": "0.945",
        "pressure_kpa": "19.71",
        "boiling_temperature_at_pressure_p_k": "315.13"
      },
      {
        "BLKpoint_id": "BLKpoint_41",
        "mole_fraction_<ethanol>": "0.947",
        "pressure_kpa": "13.15",
        "boiling_temperature_at_pressure_p_k": "307.45"
      },
      {
        "BLKpoint_id": "BLKpoint_43",
        "mole_fraction_<ethanol>": "0.964",
        "pressure_kpa": "19.71",
        "boiling_temperature_at_pressure_p_k": "315.14"
      },
      {
        "BLKpoint_id": "BLKpoint_44",
        "mole_fraction_<ethanol>": "0.965",
        "pressure_kpa": "32.86",
        "boiling_temperature_at_pressure_p_k": "325.45"
      },
      {
        "BLKpoint_id": "BLKpoint_45",
        "mole_fraction_<ethanol>": "0.971",
        "pressure_kpa": "13.15",
        "boiling_temperature_at_pressure_p_k": "307.44"
      }
    ],
    "inspection_id": "INSP_168e6ede2830",
    "lit_num_id": "GLOBlit_977"
  },
  {
    "doi": "10.1016/j.fluid.2005.08.018",
    "block_number": "PROPblock_6",
    "table_mode": "complete",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<ethanol>",
      "activity_coefficient_<ethanol>"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "358.15",
        "mole_fraction_<ethanol>": "0.0",
        "activity_coefficient_<ethanol>": "5.9"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "temperature_k": "363.15",
        "mole_fraction_<ethanol>": "0.0",
        "activity_coefficient_<ethanol>": "6"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "temperature_k": "368.15",
        "mole_fraction_<ethanol>": "0.0",
        "activity_coefficient_<ethanol>": "6.1"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "temperature_k": "372.15",
        "mole_fraction_<ethanol>": "0.0",
        "activity_coefficient_<ethanol>": "6.2"
      }
    ],
    "inspection_id": "INSP_c78d07681916",
    "lit_num_id": "GLOBlit_299"
  },
  {
    "doi": "10.1016/j.fluid.2005.08.018",
    "block_number": "PROPblock_5",
    "table_mode": "complete",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<ethanol>",
      "activity_coefficient_<ethanol>"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "303.15",
        "mole_fraction_<ethanol>": "0.0",
        "activity_coefficient_<ethanol>": "4.14"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "temperature_k": "308.15",
        "mole_fraction_<ethanol>": "0.0",
        "activity_coefficient_<ethanol>": "4.43"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "temperature_k": "313.15",
        "mole_fraction_<ethanol>": "0.0",
        "activity_coefficient_<ethanol>": "4.66"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "temperature_k": "318.15",
        "mole_fraction_<ethanol>": "0.0",
        "activity_coefficient_<ethanol>": "4.85"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "temperature_k": "323.15",
        "mole_fraction_<ethanol>": "0.0",
        "activity_coefficient_<ethanol>": "5.03"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "temperature_k": "328.15",
        "mole_fraction_<ethanol>": "0.0",
        "activity_coefficient_<ethanol>": "5.2"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "temperature_k": "333.15",
        "mole_fraction_<ethanol>": "0.0",
        "activity_coefficient_<ethanol>": "5.3"
      }
    ],
    "inspection_id": "INSP_07cd1fbb6c30",
    "lit_num_id": "GLOBlit_299"
  },
  {
    "doi": "10.1016/j.fluid.2016.08.030",
    "block_number": "PROPblock_1",
    "table_mode": "complete",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "pressure_kpa",
      "mole_fraction_<ethanol>",
      "activity_coefficient_<ethanol>"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "323.15",
        "pressure_kpa": "101.0",
        "mole_fraction_<ethanol>": "0.0",
        "activity_coefficient_<ethanol>": "5.17"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "temperature_k": "333.15",
        "pressure_kpa": "101.0",
        "mole_fraction_<ethanol>": "0.0",
        "activity_coefficient_<ethanol>": "4.77"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "temperature_k": "343.15",
        "pressure_kpa": "101.0",
        "mole_fraction_<ethanol>": "0.0",
        "activity_coefficient_<ethanol>": "4.37"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "temperature_k": "353.15",
        "pressure_kpa": "101.0",
        "mole_fraction_<ethanol>": "0.0",
        "activity_coefficient_<ethanol>": "4.11"
      }
    ],
    "inspection_id": "INSP_5c2b90e51939",
    "lit_num_id": "GLOBlit_1971"
  },
  {
    "doi": "10.1021/je049875+",
    "block_number": "PROPblock_1",
    "table_mode": "complete",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "pressure_kpa",
      "mole_fraction_<ethanol>",
      "activity_coefficient_<ethanol>"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "303.25",
        "pressure_kpa": "101.325",
        "mole_fraction_<ethanol>": "0.0",
        "activity_coefficient_<ethanol>": "5.03"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "temperature_k": "313.25",
        "pressure_kpa": "101.325",
        "mole_fraction_<ethanol>": "0.0",
        "activity_coefficient_<ethanol>": "5.33"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "temperature_k": "323.25",
        "pressure_kpa": "101.325",
        "mole_fraction_<ethanol>": "0.0",
        "activity_coefficient_<ethanol>": "5.54"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "temperature_k": "333.25",
        "pressure_kpa": "101.325",
        "mole_fraction_<ethanol>": "0.0",
        "activity_coefficient_<ethanol>": "5.76"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "temperature_k": "343.25",
        "pressure_kpa": "101.325",
        "mole_fraction_<ethanol>": "0.0",
        "activity_coefficient_<ethanol>": "5.96"
      }
    ],
    "inspection_id": "INSP_af7f92cdc6e6",
    "lit_num_id": "GLOBlit_8511"
  },
  {
    "doi": "10.1021/je0495942",
    "block_number": "PROPblock_1",
    "table_mode": "complete",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "pressure_kpa",
      "mole_fraction_<ethanol>",
      "activity_coefficient_<ethanol>"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "298.15",
        "pressure_kpa": "101.325",
        "mole_fraction_<ethanol>": "0",
        "activity_coefficient_<ethanol>": "3.77"
      }
    ],
    "inspection_id": "INSP_fd8734d59843",
    "lit_num_id": "GLOBlit_8381"
  }
]
```
