# Analysis Run — 20260815_195729 (Round 1)

**Question:** [Purpose: Obtain a Redlich-Kister correlation for viscosity of water + ethylene glycol near 25 °C from ThermoML data.]
Fit a Redlich-Kister polynomial to the viscosity of the binary liquid mixture water + ethylene glycol near 25 °C. Use a single state-aligned composition series. Report the selected temperature, pressure, composition basis (mole or mass fraction), viscosity basis (dynamic or kinematic), the RK equation, polynomial order, coefficients with units, R², RMSE, and the composition range covered.

[Context: The user wants a complete RK fit report for viscosity of the water + ethylene glycol system. Search for experimental viscosity data (dynamic viscosity preferred) in ThermoML for this binary system near 298.15 K, select the best composition series, and perform the RK fit.]

**Time:** 469.5s | **Iterations:** 14 | **Tools:** 11

---

## Answer

{
  "answer": "## Redlich-Kister Fit for Viscosity of Water + Ethylene Glycol at 298.15 K\n\n### System & Source\n\n| Parameter | Value |\n|-----------|-------|\n| System | Water + 1,2-ethanediol (ethylene glycol), binary liquid |\n| Source | GLOBlit_5201 / DOI 10.1016/j.jct.2018.02.022 / PROPblock_24 |\n| Measurement method | Concentric cylinders viscometry |\n| Temperature | 298.15 K |\n| Pressure | 92.3 kPa |\n| Composition basis | Mole fraction of 1,2-ethanediol (*x*₁), range 0–1 (21 unique compositions) |\n| Viscosity basis | Dynamic viscosity, η (Pa·s) |\n| Data points used | 19 mixture + 2 pure-component endpoints = 21 points |\n\n### Pure-Component Endpoint Values (from block edges)\n\n| Component | η* (Pa·s) |\n|-----------|-----------|\n| 1,2-ethanediol (x₁ = 1) | 0.016223 |\n| Water (x₁ = 0) | 0.00089689 |\n\n### Mixing Rule & RK Equation\n\nBecause viscosity spans nearly two orders of magnitude across the composition range, the **Arrhenius (logarithmic) mixing rule** is used:\n\n$$\\ln\\eta = x_1 \\ln\\eta_1^* + (1 - x_1)\\ln\\eta_2^* + x_1(1 - x_1)\\sum_{k=0}^{n} A_k\\,(2x_1 - 1)^k$$\n\nwhere *x*₁ = mole fraction of 1,2-ethanediol, η₁\\* = 0.016223 Pa·s, η₂\\* = 0.00089689 Pa·s.\n\n### BIC-Selected Fit: Order 3\n\n| Coefficient | Value (dimensionless) |\n|-------------|----------------------|\n| A₀ | 2.39674 |\n| A₁ | −1.04444 |\n| A₂ | 0.668173 |\n| A₃ | −0.3209 |\n\n### Fit Quality\n\n| Metric | Value |\n|--------|-------|\n| R² | 0.999940 |\n| RMSE | 0.001320 (in ln η space) |\n| BIC | −240.17 |\n\n### Model Selection (BIC Comparison)\n\n| Order | BIC | R² | RMSE |\n|-------|------|----|------|\n| 0 | −90.89 | 0.7516 | 0.08465 |\n| 1 | −141.05 | 0.9848 | 0.02092 |\n| 2 | −194.71 | 0.9992 | 0.00472 |\n| **3** | **−240.17** | **0.9999** | **0.00132** |\n| 4 | −237.59 | 0.9999 | 0.00131 |\n| 5 | −234.83 | 0.9999 | 0.00130 |\n\nOrder 3 is selected by BIC — orders 4 and 5 offer negligible improvement and are penalized for additional parameters.\n\n### Chemistry Insight\n\nThe large, positive A₀ coefficient (+2.40) confirms a strong **positive deviation** of viscosity from the Arrhenius ideal-mixing baseline. This is characteristic of the water–ethylene glycol system, where the two hydroxyl groups of ethylene glycol form an extensive hydrogen-bonding network with water, creating transient supramolecular structures that resist flow more than either pure component would predict. The asymmetry captured by A₁ (−1.04) and higher-order terms reflects the fact that the viscosity maximum shifts toward the ethylene-glycol-rich side, consistent with the stoichiometry of the hydrogen-bonding complexes.\n\nRepresentative data points at 298.15 K (from inspected block data):\n- *x*₁ = 0 (pure water): η = 0.00089689 Pa·s\n- *x*₁ = 0.2072: η = 0.0028109 Pa·s\n- *x*₁ = 0.4446: η = 0.0060624 Pa·s\n- *x*₁ = 1.0 (pure EG): η = 0.016223 Pa·s\n\n### Output Files\n\n- Fit data CSV: `10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_fit.csv`\n- Excess property CSV: `10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_excess.csv`\n- Fit plot: `10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_fit.png`\n- Excess plot: `10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_excess.png`",
  "core_claims": [
    "For the water + 1,2-ethanediol (ethylene glycol) binary liquid system at 298.15 K and 92.3 kPa, dynamic viscosity across 21 compositions (x₁ = 0–1) is well described by an Arrhenius (logarithmic) mixing rule with a Redlich-Kister excess term of order 3, selected by BIC (BIC = −240.17, R² = 0.999940, RMSE = 0.001320 in ln η space).",
    "The fitted Redlich-Kister coefficients (dimensionless) are A₀ = 2.39674, A₁ = −1.04444, A₂ = 0.668173, A₃ = −0.3209, with pure-component endpoints η*(1,2-ethanediol) = 0.016223 Pa·s and η*(water) = 0.00089689 Pa·s.",
    "The large positive A₀ (+2.40) indicates a strong positive deviation of viscosity from the Arrhenius ideal-mixing baseline, attributed to extensive hydrogen-bonding interactions between the two hydroxyl groups of ethylene glycol and water that form transient supramolecular structures resisting flow.",
    "The asymmetry captured by A₁ (−1.04) and higher-order terms reflects a shift of the viscosity maximum toward the ethylene-glycol-rich side, consistent with the stoichiometry of hydrogen-bonding complexes.",
    "Orders 4 and 5 offer negligible improvement over order 3 and are penalized by BIC for additional parameters."
  ],
  "sources": [
    {
      "doi": "10.1016/j.jct.2018.02.022",
      "lit_num_id": "GLOBlit_5201",
      "block": "PROPblock_24",
      "BLKsubsys_id": null,
      "description": "This block provides binary viscosity data for water + 1,2-ethanediol across the full mole-fraction range (0–1) at multiple temperatures including 298.15 K, measured by concentric cylinders viscometry at 92.3 kPa. The 21 data points at 298.15 K extracted from the 84-point block were used to perform the Redlich-Kister fit of order 3 in ln η space, yielding the reported coefficients and fit statistics."
    }
  ],
  "fit_results": [
    {
      "doi": "10.1016/j.jct.2018.02.022",
      "lit_num_id": "GLOBlit_5201",
      "block_number": "PROPblock_24",
      "BLKsubsys_id": null,
      "property": "GLOBprop_4",
      "rk_order": 3,
      "rk_coeffs": [
        2.3967401058713325,
        -1.0444436005853195,
        0.6681733607879681,
        -0.3209004397507546
      ],
      "r_squared": 0.99994,
      "rmse": 0.0013198945265291695,
      "n_points": 19,
      "temperature_K": 298.15,
      "mixing_rule": "arrhenius"
    }
  ]
}

---

## Data Inspections (deterministic evidence ledger)

Hardcoded envelope merge — not agent-authored. 6 entr(ies); verbatim rows below.

- INSP_475115ec48f0 — GLOBlit_8106::PROPblock_5 · rdp · 16 rows
- INSP_eb6a6a268c1a — GLOBlit_2656::PROPblock_13 · complete · 10 rows
- INSP_10e84136b97d — GLOBlit_5201::PROPblock_24 · rdp · 15 rows
- INSP_bdb58d28aae5 — GLOBlit_6951::PROPblock_18 · rdp · 14 rows
- INSP_ca607c3d05dd — GLOBlit_8038::PROPblock_5 · rdp · 37 rows
- INSP_5611a4a4b21d — GLOBlit_11186::PROPblock_4 · rdp · 14 rows

```json
[
  {
    "doi": "10.1021/je025610o",
    "block_number": "PROPblock_5",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "mole_fraction_<1,2-ethanediol>",
      "temperature_k",
      "pressure_kpa",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "mole_fraction_<1,2-ethanediol>": "0.25",
        "temperature_k": "296.45",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00369"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "mole_fraction_<1,2-ethanediol>": "0.25",
        "temperature_k": "313.05",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00229"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "mole_fraction_<1,2-ethanediol>": "0.25",
        "temperature_k": "353.05",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00099"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "mole_fraction_<1,2-ethanediol>": "0.25",
        "temperature_k": "435.55",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.000366"
      },
      {
        "BLKpoint_id": "BLKpoint_9",
        "mole_fraction_<1,2-ethanediol>": "0.5",
        "temperature_k": "297.05",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00761"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "mole_fraction_<1,2-ethanediol>": "0.5",
        "temperature_k": "313.05",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00449"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "mole_fraction_<1,2-ethanediol>": "0.5",
        "temperature_k": "333.1",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00262"
      },
      {
        "BLKpoint_id": "BLKpoint_12",
        "mole_fraction_<1,2-ethanediol>": "0.5",
        "temperature_k": "353.05",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.0017"
      },
      {
        "BLKpoint_id": "BLKpoint_13",
        "mole_fraction_<1,2-ethanediol>": "0.5",
        "temperature_k": "380.05",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00107"
      },
      {
        "BLKpoint_id": "BLKpoint_17",
        "mole_fraction_<1,2-ethanediol>": "0.5",
        "temperature_k": "440.65",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.0005"
      },
      {
        "BLKpoint_id": "BLKpoint_18",
        "mole_fraction_<1,2-ethanediol>": "0.75",
        "temperature_k": "297.35",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.0123"
      },
      {
        "BLKpoint_id": "BLKpoint_19",
        "mole_fraction_<1,2-ethanediol>": "0.75",
        "temperature_k": "313.05",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00697"
      },
      {
        "BLKpoint_id": "BLKpoint_20",
        "mole_fraction_<1,2-ethanediol>": "0.75",
        "temperature_k": "333.1",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00388"
      },
      {
        "BLKpoint_id": "BLKpoint_21",
        "mole_fraction_<1,2-ethanediol>": "0.75",
        "temperature_k": "353.05",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00242"
      },
      {
        "BLKpoint_id": "BLKpoint_22",
        "mole_fraction_<1,2-ethanediol>": "0.75",
        "temperature_k": "373.45",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00162"
      },
      {
        "BLKpoint_id": "BLKpoint_30",
        "mole_fraction_<1,2-ethanediol>": "0.75",
        "temperature_k": "449.85",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.000594"
      }
    ],
    "inspection_id": "INSP_475115ec48f0",
    "lit_num_id": "GLOBlit_8106"
  },
  {
    "doi": "10.1016/j.jct.2006.01.011",
    "block_number": "PROPblock_13",
    "table_mode": "complete",
    "columns": [
      "BLKpoint_id",
      "mass_fraction_<1,2-ethanediol>",
      "temperature_k",
      "pressure_kpa",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "mass_fraction_<1,2-ethanediol>": "0",
        "temperature_k": "293.15",
        "pressure_kpa": "101.325",
        "viscosity_pa_s": "0.001008"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "mass_fraction_<1,2-ethanediol>": "0.1",
        "temperature_k": "293.15",
        "pressure_kpa": "101.325",
        "viscosity_pa_s": "0.001293"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "mass_fraction_<1,2-ethanediol>": "0.2",
        "temperature_k": "293.15",
        "pressure_kpa": "101.325",
        "viscosity_pa_s": "0.001671"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "mass_fraction_<1,2-ethanediol>": "0.3",
        "temperature_k": "293.15",
        "pressure_kpa": "101.325",
        "viscosity_pa_s": "0.002177"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "mass_fraction_<1,2-ethanediol>": "0.4",
        "temperature_k": "293.15",
        "pressure_kpa": "101.325",
        "viscosity_pa_s": "0.002837"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "mass_fraction_<1,2-ethanediol>": "0.5",
        "temperature_k": "293.15",
        "pressure_kpa": "101.325",
        "viscosity_pa_s": "0.003558"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "mass_fraction_<1,2-ethanediol>": "0.6",
        "temperature_k": "293.15",
        "pressure_kpa": "101.325",
        "viscosity_pa_s": "0.004724"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "mass_fraction_<1,2-ethanediol>": "0.7",
        "temperature_k": "293.15",
        "pressure_kpa": "101.325",
        "viscosity_pa_s": "0.00636"
      },
      {
        "BLKpoint_id": "BLKpoint_9",
        "mass_fraction_<1,2-ethanediol>": "0.8",
        "temperature_k": "293.15",
        "pressure_kpa": "101.325",
        "viscosity_pa_s": "0.008003"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "mass_fraction_<1,2-ethanediol>": "0.9",
        "temperature_k": "293.15",
        "pressure_kpa": "101.325",
        "viscosity_pa_s": "0.013999"
      }
    ],
    "inspection_id": "INSP_eb6a6a268c1a",
    "lit_num_id": "GLOBlit_2656"
  },
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
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "293.15",
        "mole_fraction_<1,2-ethanediol>": "0.0494",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0015411"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "temperature_k": "293.15",
        "mole_fraction_<1,2-ethanediol>": "0.2072",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0035171"
      },
      {
        "BLKpoint_id": "BLKpoint_9",
        "temperature_k": "293.15",
        "mole_fraction_<1,2-ethanediol>": "0.4446",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0076382"
      },
      {
        "BLKpoint_id": "BLKpoint_23",
        "temperature_k": "298.15",
        "mole_fraction_<1,2-ethanediol>": "0.2072",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0028109"
      },
      {
        "BLKpoint_id": "BLKpoint_28",
        "temperature_k": "298.15",
        "mole_fraction_<1,2-ethanediol>": "0.4446",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0060624"
      },
      {
        "BLKpoint_id": "BLKpoint_47",
        "temperature_k": "303.15",
        "mole_fraction_<1,2-ethanediol>": "0.4446",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0053492"
      },
      {
        "BLKpoint_id": "BLKpoint_65",
        "temperature_k": "308.15",
        "mole_fraction_<1,2-ethanediol>": "0.3921",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0040265"
      },
      {
        "BLKpoint_id": "BLKpoint_77",
        "temperature_k": "293.15",
        "mole_fraction_<1,2-ethanediol>": "0",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0010673"
      },
      {
        "BLKpoint_id": "BLKpoint_78",
        "temperature_k": "298.15",
        "mole_fraction_<1,2-ethanediol>": "0",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.00089689"
      },
      {
        "BLKpoint_id": "BLKpoint_79",
        "temperature_k": "303.15",
        "mole_fraction_<1,2-ethanediol>": "0",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0008385"
      },
      {
        "BLKpoint_id": "BLKpoint_80",
        "temperature_k": "308.15",
        "mole_fraction_<1,2-ethanediol>": "0",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.00075887"
      },
      {
        "BLKpoint_id": "BLKpoint_81",
        "temperature_k": "293.15",
        "mole_fraction_<1,2-ethanediol>": "1",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.020613"
      },
      {
        "BLKpoint_id": "BLKpoint_82",
        "temperature_k": "298.15",
        "mole_fraction_<1,2-ethanediol>": "1",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.016223"
      },
      {
        "BLKpoint_id": "BLKpoint_83",
        "temperature_k": "303.15",
        "mole_fraction_<1,2-ethanediol>": "1",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.013867"
      },
      {
        "BLKpoint_id": "BLKpoint_84",
        "temperature_k": "308.15",
        "mole_fraction_<1,2-ethanediol>": "1",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.011483"
      }
    ],
    "inspection_id": "INSP_10e84136b97d",
    "lit_num_id": "GLOBlit_5201"
  },
  {
    "doi": "10.1021/acs.jced.6b00526",
    "block_number": "PROPblock_18",
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
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.02113"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "temperature_k": "293.15",
        "mole_fraction_<water>": "0.2014",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.01495"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "temperature_k": "293.15",
        "mole_fraction_<water>": "0.4011",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.01005"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "temperature_k": "293.15",
        "mole_fraction_<water>": "0.6995",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.004584"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "temperature_k": "293.15",
        "mole_fraction_<water>": "1",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.000949"
      },
      {
        "BLKpoint_id": "BLKpoint_12",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.01724"
      },
      {
        "BLKpoint_id": "BLKpoint_14",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.2014",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.01219"
      },
      {
        "BLKpoint_id": "BLKpoint_16",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.4011",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00831"
      },
      {
        "BLKpoint_id": "BLKpoint_19",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.6995",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.003884"
      },
      {
        "BLKpoint_id": "BLKpoint_22",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "1",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.000843"
      },
      {
        "BLKpoint_id": "BLKpoint_23",
        "temperature_k": "303.15",
        "mole_fraction_<water>": "0",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.01423"
      },
      {
        "BLKpoint_id": "BLKpoint_25",
        "temperature_k": "303.15",
        "mole_fraction_<water>": "0.2014",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.01014"
      },
      {
        "BLKpoint_id": "BLKpoint_28",
        "temperature_k": "303.15",
        "mole_fraction_<water>": "0.4969",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.005653"
      },
      {
        "BLKpoint_id": "BLKpoint_33",
        "temperature_k": "303.15",
        "mole_fraction_<water>": "1",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.000755"
      }
    ],
    "inspection_id": "INSP_bdb58d28aae5",
    "lit_num_id": "GLOBlit_6951"
  },
  {
    "doi": "10.1021/je020140j",
    "block_number": "PROPblock_5",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "mole_fraction_<1,2-ethanediol>",
      "temperature_k",
      "pressure_kpa",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "mole_fraction_<1,2-ethanediol>": "0",
        "temperature_k": "293.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001002"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "mole_fraction_<1,2-ethanediol>": "0",
        "temperature_k": "353.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.000356"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "mole_fraction_<1,2-ethanediol>": "0.0312",
        "temperature_k": "293.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001337"
      },
      {
        "BLKpoint_id": "BLKpoint_14",
        "mole_fraction_<1,2-ethanediol>": "0.0312",
        "temperature_k": "353.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.000434"
      },
      {
        "BLKpoint_id": "BLKpoint_15",
        "mole_fraction_<1,2-ethanediol>": "0.0676",
        "temperature_k": "293.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001785"
      },
      {
        "BLKpoint_id": "BLKpoint_21",
        "mole_fraction_<1,2-ethanediol>": "0.0676",
        "temperature_k": "353.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.000525"
      },
      {
        "BLKpoint_id": "BLKpoint_22",
        "mole_fraction_<1,2-ethanediol>": "0.1105",
        "temperature_k": "293.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002272"
      },
      {
        "BLKpoint_id": "BLKpoint_24",
        "mole_fraction_<1,2-ethanediol>": "0.1105",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001319"
      },
      {
        "BLKpoint_id": "BLKpoint_28",
        "mole_fraction_<1,2-ethanediol>": "0.1105",
        "temperature_k": "353.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.000629"
      },
      {
        "BLKpoint_id": "BLKpoint_29",
        "mole_fraction_<1,2-ethanediol>": "0.162",
        "temperature_k": "293.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002951"
      },
      {
        "BLKpoint_id": "BLKpoint_31",
        "mole_fraction_<1,2-ethanediol>": "0.162",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001677"
      },
      {
        "BLKpoint_id": "BLKpoint_35",
        "mole_fraction_<1,2-ethanediol>": "0.162",
        "temperature_k": "353.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.000758"
      },
      {
        "BLKpoint_id": "BLKpoint_36",
        "mole_fraction_<1,2-ethanediol>": "0.2248",
        "temperature_k": "293.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.003941"
      },
      {
        "BLKpoint_id": "BLKpoint_38",
        "mole_fraction_<1,2-ethanediol>": "0.2248",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002132"
      },
      {
        "BLKpoint_id": "BLKpoint_42",
        "mole_fraction_<1,2-ethanediol>": "0.2248",
        "temperature_k": "353.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.000906"
      },
      {
        "BLKpoint_id": "BLKpoint_43",
        "mole_fraction_<1,2-ethanediol>": "0.3031",
        "temperature_k": "293.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.005102"
      },
      {
        "BLKpoint_id": "BLKpoint_45",
        "mole_fraction_<1,2-ethanediol>": "0.3031",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002756"
      },
      {
        "BLKpoint_id": "BLKpoint_49",
        "mole_fraction_<1,2-ethanediol>": "0.3031",
        "temperature_k": "353.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0011"
      },
      {
        "BLKpoint_id": "BLKpoint_50",
        "mole_fraction_<1,2-ethanediol>": "0.4036",
        "temperature_k": "293.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.006898"
      },
      {
        "BLKpoint_id": "BLKpoint_52",
        "mole_fraction_<1,2-ethanediol>": "0.4036",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.003575"
      },
      {
        "BLKpoint_id": "BLKpoint_54",
        "mole_fraction_<1,2-ethanediol>": "0.4036",
        "temperature_k": "333.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002053"
      },
      {
        "BLKpoint_id": "BLKpoint_56",
        "mole_fraction_<1,2-ethanediol>": "0.4036",
        "temperature_k": "353.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001359"
      },
      {
        "BLKpoint_id": "BLKpoint_57",
        "mole_fraction_<1,2-ethanediol>": "0.537",
        "temperature_k": "293.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.009696"
      },
      {
        "BLKpoint_id": "BLKpoint_58",
        "mole_fraction_<1,2-ethanediol>": "0.537",
        "temperature_k": "303.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.006749"
      },
      {
        "BLKpoint_id": "BLKpoint_59",
        "mole_fraction_<1,2-ethanediol>": "0.537",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.004776"
      },
      {
        "BLKpoint_id": "BLKpoint_61",
        "mole_fraction_<1,2-ethanediol>": "0.537",
        "temperature_k": "333.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002684"
      },
      {
        "BLKpoint_id": "BLKpoint_63",
        "mole_fraction_<1,2-ethanediol>": "0.537",
        "temperature_k": "353.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001748"
      },
      {
        "BLKpoint_id": "BLKpoint_64",
        "mole_fraction_<1,2-ethanediol>": "0.723",
        "temperature_k": "293.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.014042"
      },
      {
        "BLKpoint_id": "BLKpoint_65",
        "mole_fraction_<1,2-ethanediol>": "0.723",
        "temperature_k": "303.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.009399"
      },
      {
        "BLKpoint_id": "BLKpoint_66",
        "mole_fraction_<1,2-ethanediol>": "0.723",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.006449"
      },
      {
        "BLKpoint_id": "BLKpoint_68",
        "mole_fraction_<1,2-ethanediol>": "0.723",
        "temperature_k": "333.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.00351"
      },
      {
        "BLKpoint_id": "BLKpoint_70",
        "mole_fraction_<1,2-ethanediol>": "0.723",
        "temperature_k": "353.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002296"
      },
      {
        "BLKpoint_id": "BLKpoint_71",
        "mole_fraction_<1,2-ethanediol>": "1",
        "temperature_k": "293.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.020833"
      },
      {
        "BLKpoint_id": "BLKpoint_72",
        "mole_fraction_<1,2-ethanediol>": "1",
        "temperature_k": "303.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.013646"
      },
      {
        "BLKpoint_id": "BLKpoint_73",
        "mole_fraction_<1,2-ethanediol>": "1",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.009443"
      },
      {
        "BLKpoint_id": "BLKpoint_75",
        "mole_fraction_<1,2-ethanediol>": "1",
        "temperature_k": "333.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.00506"
      },
      {
        "BLKpoint_id": "BLKpoint_77",
        "mole_fraction_<1,2-ethanediol>": "1",
        "temperature_k": "353.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.003021"
      }
    ],
    "inspection_id": "INSP_ca607c3d05dd",
    "lit_num_id": "GLOBlit_8038"
  },
  {
    "doi": "10.1021/je800271e",
    "block_number": "PROPblock_4",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<1,2-ethanediol>",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "308.15",
        "mole_fraction_<1,2-ethanediol>": "0",
        "viscosity_pa_s": "0.000721"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "temperature_k": "308.15",
        "mole_fraction_<1,2-ethanediol>": "0.1621",
        "viscosity_pa_s": "0.0015744"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "temperature_k": "308.15",
        "mole_fraction_<1,2-ethanediol>": "0.4035",
        "viscosity_pa_s": "0.0035116"
      },
      {
        "BLKpoint_id": "BLKpoint_13",
        "temperature_k": "308.15",
        "mole_fraction_<1,2-ethanediol>": "1",
        "viscosity_pa_s": "0.0092122"
      },
      {
        "BLKpoint_id": "BLKpoint_14",
        "temperature_k": "313.15",
        "mole_fraction_<1,2-ethanediol>": "0",
        "viscosity_pa_s": "0.0006532"
      },
      {
        "BLKpoint_id": "BLKpoint_21",
        "temperature_k": "313.15",
        "mole_fraction_<1,2-ethanediol>": "0.1621",
        "viscosity_pa_s": "0.0014047"
      },
      {
        "BLKpoint_id": "BLKpoint_24",
        "temperature_k": "313.15",
        "mole_fraction_<1,2-ethanediol>": "0.4035",
        "viscosity_pa_s": "0.0030166"
      },
      {
        "BLKpoint_id": "BLKpoint_26",
        "temperature_k": "313.15",
        "mole_fraction_<1,2-ethanediol>": "1",
        "viscosity_pa_s": "0.0079605"
      },
      {
        "BLKpoint_id": "BLKpoint_27",
        "temperature_k": "318.15",
        "mole_fraction_<1,2-ethanediol>": "0",
        "viscosity_pa_s": "0.00059"
      },
      {
        "BLKpoint_id": "BLKpoint_36",
        "temperature_k": "318.15",
        "mole_fraction_<1,2-ethanediol>": "0.3032",
        "viscosity_pa_s": "0.0018883"
      },
      {
        "BLKpoint_id": "BLKpoint_39",
        "temperature_k": "318.15",
        "mole_fraction_<1,2-ethanediol>": "1",
        "viscosity_pa_s": "0.0062933"
      },
      {
        "BLKpoint_id": "BLKpoint_40",
        "temperature_k": "323.15",
        "mole_fraction_<1,2-ethanediol>": "0",
        "viscosity_pa_s": "0.00055"
      },
      {
        "BLKpoint_id": "BLKpoint_49",
        "temperature_k": "323.15",
        "mole_fraction_<1,2-ethanediol>": "0.3032",
        "viscosity_pa_s": "0.0016786"
      },
      {
        "BLKpoint_id": "BLKpoint_52",
        "temperature_k": "323.15",
        "mole_fraction_<1,2-ethanediol>": "1",
        "viscosity_pa_s": "0.0054468"
      }
    ],
    "inspection_id": "INSP_5611a4a4b21d",
    "lit_num_id": "GLOBlit_11186"
  }
]
```

---

## Verdict

**Data Quality**
The trace shows multiple `fit_block` attempts, with the final call (step 11) returning 899 chars — likely a successful fit result. Data originates from a ThermoML DOI (10.1016/j.jct.2018.02.022), and the block was inspected before fitting. The composition basis is mole fraction, and the property is dynamic viscosity — appropriate. However, the representative data points quoted (x₁ = 0.2072, 0.4446, etc.) cannot be independently verified against tool results in the trace since inspect_block outputs are truncated. The Arrhenius mixing rule is correctly applied for viscosity spanning ~1.8 orders of magnitude. No composition-basis conversion issues are apparent.

**Fit Quality**
Order 3 selected by BIC is reasonable. R² = 0.999940 with RMSE = 0.00132 in ln η space is excellent. BIC comparison shows clear plateau at order 3 — no overfitting concern.

**Scientific Verdict**
The fit is scientifically sound: logarithmic mixing rule is appropriate for viscosity, and the positive A₀ aligns with known strong H-bonding in this system. The truncated answer text is a minor presentation issue. Results are reliable for engineering interpolation across the full composition range.

---

## Output Files

- **data**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260815_194722_684644_49ae3f02\analysis_runs\run_1\data\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_fit.csv` — RK fit data — 10.1016/j.jct.2018.02.022 PROPblock_24_T298.1
- **data**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260815_194722_684644_49ae3f02\analysis_runs\run_1\data\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_excess.csv` — Excess property — 10.1016/j.jct.2018.02.022 PROPblock_24_T298.1
- **plot**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260815_194722_684644_49ae3f02\analysis_runs\run_1\plots\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_fit.png` — RK fit plot — 10.1016/j.jct.2018.02.022 PROPblock_24_T298.1
- **plot**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260815_194722_684644_49ae3f02\analysis_runs\run_1\plots\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_excess.png` — Excess plot — 10.1016/j.jct.2018.02.022 PROPblock_24_T298.1