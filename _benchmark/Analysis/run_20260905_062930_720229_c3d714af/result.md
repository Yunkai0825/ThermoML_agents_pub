# Analysis Run — 20260905_063725 (Round 1)

**Question:** At 25 °C, at what ethanol mole fraction is the viscosity of liquid ethanol + water greatest, and how does that composition shift as temperature rises?

**Time:** 440.1s | **Iterations:** 20 | **Tools:** 19

---

## Answer

{
  "answer": "## Viscosity Maximum in Ethanol + Water Mixtures: Composition and Temperature Dependence\n\n### Data Source\n\nAll results are from DOI **10.1016/j.jct.2018.02.022** (GLOBlit_5201), block **PROPblock_21** — dynamic viscosity of liquid ethanol + water measured by concentric-cylinders viscometry at 92.3 kPa. The block contains **100 data points** spanning four isotherms (293.15–308.15 K) over the full ethanol mole-fraction range (0 to 1), with 23 mixture compositions per isotherm.\n\n---\n\n### At 25 °C (298.15 K): Where Is the Viscosity Greatest?\n\nFrom the Redlich-Kister fit (Arrhenius mixing rule, BIC-selected order 4, R² = 0.999334, RMSE = 0.00661), the **viscosity maximum occurs at x(ethanol) ≈ 0.24**, with a predicted peak viscosity of **0.00241 Pa·s** (2.41 mPa·s).\n\nThis is roughly **2.7× the viscosity of pure water** (0.000897 Pa·s) and **2.2× that of pure ethanol** (0.001091 Pa·s) at the same temperature — a dramatic enhancement arising from strong ethanol–water hydrogen-bonding interactions that create structured, less mobile molecular clusters at intermediate compositions.\n\nRepresentative inspected data points at 298.15 K confirm the maximum near x ≈ 0.25:\n\n| x(ethanol) | Viscosity (Pa·s) |\n|:----------:|:----------------:|\n| 0          | 0.00089689       |\n| 0.1004     | 0.0019469        |\n| 0.1984     | 0.0023706        |\n| **0.2499** | **0.0024286**    |\n| 0.3499     | 0.0022633        |\n| 0.4989     | 0.0019557        |\n| 1          | 0.0010914        |\n\n---\n\n### How Does the Maximum Shift with Temperature?\n\nRedlich-Kister fits (Arrhenius mixing rule) were performed independently at each of the four isotherms. The predicted viscosity-maximum composition and peak value are:\n\n| T (K) | RK Order | R² | x(ethanol) at η_max | η_max (Pa·s) | Max ln-excess |\n|:------:|:--------:|:------:|:-------------------:|:------------:|:-------------:|\n| 293.15 | 5 | 0.99687 | **0.230** | 0.00292 | 0.979 |\n| 298.15 | 4 | 0.99933 | **0.240** | 0.00241 | 0.945 |\n| 303.15 | 5 | 0.99833 | **0.245** | 0.00204 | 0.852 |\n| 308.15 | 5 | 0.99754 | **0.250** | 0.00173 | 0.784 |\n\n**Key trends as temperature rises from 293 to 308 K:**\n\n1. **The maximum shifts to higher ethanol mole fractions** — from x ≈ 0.23 at 293 K to x ≈ 0.25 at 308 K (a shift of about +0.02 in mole fraction over 15 K).\n\n2. **The peak viscosity drops sharply** — from 0.00292 Pa·s at 293 K to 0.00173 Pa·s at 308 K (a ~41% decrease), consistent with the general Arrhenius-type thermal activation of molecular mobility.\n\n3. **The excess viscosity (ln-space) diminishes** — the maximum ln-excess decreases from 0.979 to 0.784, indicating that the hydrogen-bonding network responsible for the anomalous viscosity enhancement becomes progressively disrupted at higher temperatures.\n\n---\n\n### Redlich-Kister Coefficients (Arrhenius Mixing Rule)\n\nThe fitted model is: ln η_mix = x₁ ln η₁ + x₂ ln η₂ + x₁ x₂ Σᵢ Aᵢ (x₁ − x₂)ⁱ, where x₁ = x(ethanol).\n\n| T (K) | A₀ | A₁ | A₂ | A₃ | A₄ | A₅ |\n|:------:|:------:|:------:|:------:|:------:|:------:|:------:|\n| 293.15 | 2.778 | −2.369 | 2.917 | −4.225 | 0.925 | 2.756 |\n| 298.15 | 2.728 | −2.493 | 2.550 | −2.448 | 1.536 | — |\n| 303.15 | 2.480 | −2.120 | 2.387 | −3.144 | 0.855 | 1.730 |\n| 308.15 | 2.330 | −1.956 | 2.031 | −2.816 | 0.892 | 1.575 |\n\nPure-component values used (Pa·s):\n\n| T (K) | η(water) | η(ethanol) |\n|:------:|:--------:|:----------:|\n| 293.15 | 0.0010673 | 0.0012019 |\n| 298.15 | 0.00089689 | 0.0010914 |\n| 303.15 | 0.0008385 | 0.00099196 |\n| 308.15 | 0.00075887 | 0.00090388 |\n\n---\n\n### Physical Interpretation\n\nThe viscosity maximum near x(ethanol) ≈ 0.23–0.25 corresponds to roughly 1 ethanol molecule per 3–4 water molecules — a stoichiometry that maximizes the formation of extended hydrogen-bonded clusters (often described as ethanol–water clathrate-like structures). As temperature increases, thermal energy progressively disrupts these clusters, which has two effects: (i) the overall viscosity drops, and (ii) the optimal cluster-forming composition shifts slightly toward higher ethanol content (from 0.23 to 0.25), suggesting that at higher temperatures a somewhat higher ethanol concentration is needed to sustain the cooperative hydrogen-bonding network that produces the viscosity anomaly.",
  "core_claims": [
    "For ethanol + water mixtures at 298.15 K and 92.3 kPa, the dynamic viscosity maximum occurs at x(ethanol) ≈ 0.24 with a predicted peak viscosity of 0.00241 Pa·s, roughly 2.7× the viscosity of pure water (0.000897 Pa·s) and 2.2× that of pure ethanol (0.001091 Pa·s) at the same temperature.",
    "As temperature increases from 293.15 K to 308.15 K, the viscosity-maximum composition shifts to higher ethanol mole fractions, from x ≈ 0.230 to x ≈ 0.250.",
    "The peak viscosity drops sharply with increasing temperature, from 0.00292 Pa·s at 293.15 K to 0.00173 Pa·s at 308.15 K, consistent with Arrhenius-type thermal activation.",
    "The maximum ln-excess viscosity decreases from 0.979 at 293.15 K to 0.784 at 308.15 K, indicating progressive disruption of the hydrogen-bonding network responsible for the anomalous viscosity enhancement at higher temperatures.",
    "All results are derived from DOI 10.1016/j.jct.2018.02.022, block PROPblock_21, containing 100 data points across four isotherms (293.15–308.15 K) fitted with Redlich-Kister polynomials using an Arrhenius mixing rule (R² ≥ 0.99687 at all temperatures)."
  ],
  "sources": [
    {
      "doi": "10.1016/j.jct.2018.02.022",
      "lit_num_id": "GLOBlit_5201",
      "block": "PROPblock_21",
      "BLKsubsys_id": null,
      "description": "This block provides the dynamic viscosity of ethanol + water mixtures (100 data points, concentric-cylinders viscometry, 92.3 kPa) across four isotherms (293.15–308.15 K) and the full mole-fraction range (0–1). It is the sole data source for identifying the viscosity maximum near x(ethanol) ≈ 0.24 at 298.15 K and for characterizing how the peak composition and magnitude shift with temperature."
    }
  ],
  "fit_results": [
    {
      "doi": "10.1016/j.jct.2018.02.022",
      "lit_num_id": "GLOBlit_5201",
      "block_number": "PROPblock_21",
      "BLKsubsys_id": null,
      "property": "GLOBprop_4",
      "rk_order": 5,
      "rk_coeffs": [
        2.4797538236283185,
        -2.120004189707748,
        2.386992245605703,
        -3.1443732454296387,
        0.8552391192599589,
        1.7300032296545247
      ],
      "r_squared": 0.998334,
      "rmse": 0.00948397542567419,
      "n_points": 23,
      "temperature_K": 303.15,
      "mixing_rule": "arrhenius"
    },
    {
      "doi": "10.1016/j.jct.2018.02.022",
      "lit_num_id": "GLOBlit_5201",
      "block_number": "PROPblock_21",
      "BLKsubsys_id": null,
      "property": "T=293.15K",
      "rk_order": 5,
      "rk_coeffs": [
        2.777909177194302,
        -2.3688378692354166,
        2.9166124577732813,
        -4.224496287203014,
        0.9246777491739545,
        2.7559484465319213
      ],
      "r_squared": 0.99687,
      "rmse": 0.014946647676868378,
      "n_points": 23,
      "temperature_K": 293.15,
      "mixing_rule": "arrhenius"
    },
    {
      "doi": "10.1016/j.jct.2018.02.022",
      "lit_num_id": "GLOBlit_5201",
      "block_number": "PROPblock_21",
      "BLKsubsys_id": null,
      "property": "T=298.15K",
      "rk_order": 4,
      "rk_coeffs": [
        2.7279958938647066,
        -2.4925941810857495,
        2.5500472215385774,
        -2.4477499128574456,
        1.53644421556371
      ],
      "r_squared": 0.999334,
      "rmse": 0.006612838327445672,
      "n_points": 23,
      "temperature_K": 298.15,
      "mixing_rule": "arrhenius"
    },
    {
      "doi": "10.1016/j.jct.2018.02.022",
      "lit_num_id": "GLOBlit_5201",
      "block_number": "PROPblock_21",
      "BLKsubsys_id": null,
      "property": "T=303.15K",
      "rk_order": 5,
      "rk_coeffs": [
        2.4797538236283185,
        -2.120004189707748,
        2.386992245605703,
        -3.1443732454296387,
        0.8552391192599589,
        1.7300032296545247
      ],
      "r_squared": 0.998334,
      "rmse": 0.00948397542567419,
      "n_points": 23,
      "temperature_K": 303.15,
      "mixing_rule": "arrhenius"
    },
    {
      "doi": "10.1016/j.jct.2018.02.022",
      "lit_num_id": "GLOBlit_5201",
      "block_number": "PROPblock_21",
      "BLKsubsys_id": null,
      "property": "T=308.15K",
      "rk_order": 5,
      "rk_coeffs": [
        2.33015003706876,
        -1.9562817730603848,
        2.0314890727451007,
        -2.8160995147026564,
        0.8919625893625028,
        1.5752024920398033
      ],
      "r_squared": 0.997541,
      "rmse": 0.010669590029158437,
      "n_points": 23,
      "temperature_K": 308.15,
      "mixing_rule": "arrhenius"
    }
  ]
}

---

## Data Inspections (deterministic evidence ledger)

Hardcoded envelope merge — not agent-authored. 2 entr(ies); verbatim rows below.

- INSP_d0495ab20e5e — GLOBlit_5201::PROPblock_21 · rdp · 14 rows
- INSP_4b352e3d2858 — GLOBlit_11136::PROPblock_8 · rdp · 40 rows

```json
[
  {
    "doi": "10.1016/j.jct.2018.02.022",
    "block_number": "PROPblock_21",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<ethanol>",
      "pressure_kpa",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_24",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.0201",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.001098"
      },
      {
        "BLKpoint_id": "BLKpoint_29",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.1004",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0019469"
      },
      {
        "BLKpoint_id": "BLKpoint_30",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.1499",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0022424"
      },
      {
        "BLKpoint_id": "BLKpoint_31",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.1984",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0023706"
      },
      {
        "BLKpoint_id": "BLKpoint_32",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.2499",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0024286"
      },
      {
        "BLKpoint_id": "BLKpoint_34",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.3499",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0022633"
      },
      {
        "BLKpoint_id": "BLKpoint_35",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.399",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0021697"
      },
      {
        "BLKpoint_id": "BLKpoint_37",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.4989",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0019557"
      },
      {
        "BLKpoint_id": "BLKpoint_38",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.5495",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0018796"
      },
      {
        "BLKpoint_id": "BLKpoint_39",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.6067",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0017439"
      },
      {
        "BLKpoint_id": "BLKpoint_41",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.6956",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0015722"
      },
      {
        "BLKpoint_id": "BLKpoint_44",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.8475",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0013415"
      },
      {
        "BLKpoint_id": "BLKpoint_94",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.00089689"
      },
      {
        "BLKpoint_id": "BLKpoint_98",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "1",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0010914"
      }
    ],
    "inspection_id": "INSP_d0495ab20e5e",
    "lit_num_id": "GLOBlit_5201"
  },
  {
    "doi": "10.1021/je800150h",
    "block_number": "PROPblock_8",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "mole_fraction_<water>",
      "temperature_k",
      "pressure_kpa",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "mole_fraction_<water>": "0.1",
        "temperature_k": "268.1",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002307"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "mole_fraction_<water>": "0.1",
        "temperature_k": "293.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001355"
      },
      {
        "BLKpoint_id": "BLKpoint_12",
        "mole_fraction_<water>": "0.1",
        "temperature_k": "323.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.00076"
      },
      {
        "BLKpoint_id": "BLKpoint_13",
        "mole_fraction_<water>": "0.2",
        "temperature_k": "268.1",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002805"
      },
      {
        "BLKpoint_id": "BLKpoint_18",
        "mole_fraction_<water>": "0.2",
        "temperature_k": "293.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001515"
      },
      {
        "BLKpoint_id": "BLKpoint_24",
        "mole_fraction_<water>": "0.2",
        "temperature_k": "323.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.000839"
      },
      {
        "BLKpoint_id": "BLKpoint_25",
        "mole_fraction_<water>": "0.3",
        "temperature_k": "268.1",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.003345"
      },
      {
        "BLKpoint_id": "BLKpoint_30",
        "mole_fraction_<water>": "0.3",
        "temperature_k": "293.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001715"
      },
      {
        "BLKpoint_id": "BLKpoint_36",
        "mole_fraction_<water>": "0.3",
        "temperature_k": "323.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.000902"
      },
      {
        "BLKpoint_id": "BLKpoint_37",
        "mole_fraction_<water>": "0.4",
        "temperature_k": "268.1",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.003991"
      },
      {
        "BLKpoint_id": "BLKpoint_39",
        "mole_fraction_<water>": "0.4",
        "temperature_k": "278.1",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.00298"
      },
      {
        "BLKpoint_id": "BLKpoint_42",
        "mole_fraction_<water>": "0.4",
        "temperature_k": "293.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001901"
      },
      {
        "BLKpoint_id": "BLKpoint_44",
        "mole_fraction_<water>": "0.4",
        "temperature_k": "303.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001446"
      },
      {
        "BLKpoint_id": "BLKpoint_48",
        "mole_fraction_<water>": "0.4",
        "temperature_k": "323.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.000932"
      },
      {
        "BLKpoint_id": "BLKpoint_49",
        "mole_fraction_<water>": "0.5",
        "temperature_k": "268.1",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.004829"
      },
      {
        "BLKpoint_id": "BLKpoint_51",
        "mole_fraction_<water>": "0.5",
        "temperature_k": "278.1",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.003518"
      },
      {
        "BLKpoint_id": "BLKpoint_54",
        "mole_fraction_<water>": "0.5",
        "temperature_k": "293.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002153"
      },
      {
        "BLKpoint_id": "BLKpoint_57",
        "mole_fraction_<water>": "0.5",
        "temperature_k": "308.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001407"
      },
      {
        "BLKpoint_id": "BLKpoint_60",
        "mole_fraction_<water>": "0.5",
        "temperature_k": "323.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.00102"
      },
      {
        "BLKpoint_id": "BLKpoint_61",
        "mole_fraction_<water>": "0.6",
        "temperature_k": "268.1",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.005931"
      },
      {
        "BLKpoint_id": "BLKpoint_63",
        "mole_fraction_<water>": "0.6",
        "temperature_k": "278.1",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.004176"
      },
      {
        "BLKpoint_id": "BLKpoint_66",
        "mole_fraction_<water>": "0.6",
        "temperature_k": "293.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002463"
      },
      {
        "BLKpoint_id": "BLKpoint_69",
        "mole_fraction_<water>": "0.6",
        "temperature_k": "308.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001582"
      },
      {
        "BLKpoint_id": "BLKpoint_72",
        "mole_fraction_<water>": "0.6",
        "temperature_k": "323.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.00114"
      },
      {
        "BLKpoint_id": "BLKpoint_73",
        "mole_fraction_<water>": "0.7",
        "temperature_k": "268.1",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.007172"
      },
      {
        "BLKpoint_id": "BLKpoint_75",
        "mole_fraction_<water>": "0.7",
        "temperature_k": "278.1",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.004933"
      },
      {
        "BLKpoint_id": "BLKpoint_77",
        "mole_fraction_<water>": "0.7",
        "temperature_k": "288.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.003372"
      },
      {
        "BLKpoint_id": "BLKpoint_79",
        "mole_fraction_<water>": "0.7",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.00235"
      },
      {
        "BLKpoint_id": "BLKpoint_84",
        "mole_fraction_<water>": "0.7",
        "temperature_k": "323.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.00117"
      },
      {
        "BLKpoint_id": "BLKpoint_85",
        "mole_fraction_<water>": "0.8",
        "temperature_k": "268.1",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.007549"
      },
      {
        "BLKpoint_id": "BLKpoint_87",
        "mole_fraction_<water>": "0.8",
        "temperature_k": "278.1",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.005037"
      },
      {
        "BLKpoint_id": "BLKpoint_88",
        "mole_fraction_<water>": "0.8",
        "temperature_k": "283.1",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.004102"
      },
      {
        "BLKpoint_id": "BLKpoint_90",
        "mole_fraction_<water>": "0.8",
        "temperature_k": "293.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002841"
      },
      {
        "BLKpoint_id": "BLKpoint_93",
        "mole_fraction_<water>": "0.8",
        "temperature_k": "308.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001772"
      },
      {
        "BLKpoint_id": "BLKpoint_96",
        "mole_fraction_<water>": "0.8",
        "temperature_k": "323.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001202"
      },
      {
        "BLKpoint_id": "BLKpoint_97",
        "mole_fraction_<water>": "0.9",
        "temperature_k": "268.1",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.006025"
      },
      {
        "BLKpoint_id": "BLKpoint_99",
        "mole_fraction_<water>": "0.9",
        "temperature_k": "278.1",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.004089"
      },
      {
        "BLKpoint_id": "BLKpoint_101",
        "mole_fraction_<water>": "0.9",
        "temperature_k": "288.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002706"
      },
      {
        "BLKpoint_id": "BLKpoint_104",
        "mole_fraction_<water>": "0.9",
        "temperature_k": "303.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001656"
      },
      {
        "BLKpoint_id": "BLKpoint_108",
        "mole_fraction_<water>": "0.9",
        "temperature_k": "323.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.000975"
      }
    ],
    "inspection_id": "INSP_4b352e3d2858",
    "lit_num_id": "GLOBlit_11136"
  }
]
```

---

## Verdict

**Data Quality**
The agent used real measured viscosity data from DOI 10.1016/j.jct.2018.02.022, and the quoted data points (e.g., x=0.2499, η=0.0024286 at 298.15 K) appear consistent with inspect_block results. The fit_multi_system call (step 15) returned 2088 chars with results for four isotherms. The Arrhenius mixing rule operates on ln(η), fitting excess ln-viscosity via RK in mole fraction — appropriate. Data are in mole fraction; no conversion issues. However, predict_from_rk calls (steps 16–19) returned only ~213 chars each, making it unclear whether the precise peak compositions (0.230, 0.240, etc.) were tool-derived or interpolated by the agent. This is a minor concern.

**Fit Quality**
R² values (0.997–0.999) with RK orders 4–5 are reasonable for viscosity. No overfitting concerns given 23 compositions per isotherm.

**Scientific Verdict**
Results are physically sound: viscosity maximum at x≈0.24 shifting slightly ethanol-rich with temperature is well-established in literature. The temperature trends (decreasing peak height, diminishing excess) are consistent. Answer is reliable and well-documented.

---

## Output Files

- **data**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_062930_720229_c3d714af\data\10_1016_j_jct_2018_02_022_BPROPblock_21_T303.1_fit.csv` — RK fit data — 10.1016/j.jct.2018.02.022 PROPblock_21_T303.1
- **data**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_062930_720229_c3d714af\data\10_1016_j_jct_2018_02_022_BPROPblock_21_T303.1_excess.csv` — Excess property — 10.1016/j.jct.2018.02.022 PROPblock_21_T303.1
- **plot**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_062930_720229_c3d714af\plots\10_1016_j_jct_2018_02_022_BPROPblock_21_T303.1_fit.png` — RK fit plot — 10.1016/j.jct.2018.02.022 PROPblock_21_T303.1
- **plot**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_062930_720229_c3d714af\plots\10_1016_j_jct_2018_02_022_BPROPblock_21_T303.1_excess.png` — Excess plot — 10.1016/j.jct.2018.02.022 PROPblock_21_T303.1
- **data**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_062930_720229_c3d714af\data\10_1016_j_jct_2018_02_022_BPROPblock_21_T308.1_fit.csv` — RK fit data — 10.1016/j.jct.2018.02.022 PROPblock_21_T308.1
- **data**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_062930_720229_c3d714af\data\10_1016_j_jct_2018_02_022_BPROPblock_21_T298.1_fit.csv` — RK fit data — 10.1016/j.jct.2018.02.022 PROPblock_21_T298.1
- **data**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_062930_720229_c3d714af\data\10_1016_j_jct_2018_02_022_BPROPblock_21_T293.1_fit.csv` — RK fit data — 10.1016/j.jct.2018.02.022 PROPblock_21_T293.1
- **data**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_062930_720229_c3d714af\data\10_1016_j_jct_2018_02_022_BPROPblock_21_T308.1_excess.csv` — Excess property — 10.1016/j.jct.2018.02.022 PROPblock_21_T308.1
- **data**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_062930_720229_c3d714af\data\10_1016_j_jct_2018_02_022_BPROPblock_21_T298.1_excess.csv` — Excess property — 10.1016/j.jct.2018.02.022 PROPblock_21_T298.1
- **data**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_062930_720229_c3d714af\data\10_1016_j_jct_2018_02_022_BPROPblock_21_T293.1_excess.csv` — Excess property — 10.1016/j.jct.2018.02.022 PROPblock_21_T293.1
- **plot**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_062930_720229_c3d714af\plots\10_1016_j_jct_2018_02_022_BPROPblock_21_T298.1_fit.png` — RK fit plot — 10.1016/j.jct.2018.02.022 PROPblock_21_T298.1
- **plot**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_062930_720229_c3d714af\plots\10_1016_j_jct_2018_02_022_BPROPblock_21_T293.1_fit.png` — RK fit plot — 10.1016/j.jct.2018.02.022 PROPblock_21_T293.1
- **plot**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_062930_720229_c3d714af\plots\10_1016_j_jct_2018_02_022_BPROPblock_21_T308.1_fit.png` — RK fit plot — 10.1016/j.jct.2018.02.022 PROPblock_21_T308.1
- **plot**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_062930_720229_c3d714af\plots\10_1016_j_jct_2018_02_022_BPROPblock_21_T298.1_excess.png` — Excess plot — 10.1016/j.jct.2018.02.022 PROPblock_21_T298.1
- **plot**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_062930_720229_c3d714af\plots\10_1016_j_jct_2018_02_022_BPROPblock_21_T293.1_excess.png` — Excess plot — 10.1016/j.jct.2018.02.022 PROPblock_21_T293.1
- **plot**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_062930_720229_c3d714af\plots\10_1016_j_jct_2018_02_022_BPROPblock_21_T308.1_excess.png` — Excess plot — 10.1016/j.jct.2018.02.022 PROPblock_21_T308.1