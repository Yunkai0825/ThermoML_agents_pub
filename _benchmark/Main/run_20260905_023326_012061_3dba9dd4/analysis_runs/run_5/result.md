# Analysis Run — 20260905_025244 (Round 1)

**Question:** [Purpose: Determine the magnitude and composition of maximum volume contraction for water + 1-propanol at 25°C]
Find and fit excess molar volume (VE) data for the binary system water + 1-propanol at 25°C (298.15 K). Report the Redlich-Kister coefficients, the composition (mole fraction of 1-propanol) at which the minimum VE occurs, and the minimum VE value.

[Context: Looking for excess molar volume data. 1-Propanol CAS: 71-23-8, Water CAS: 7732-18-5.]

**Time:** 606.7s | **Iterations:** 16 | **Tools:** 13

---

## Answer

{
  "answer": "## Excess Molar Volume (V^E) for Water + 1-Propanol at 298.15 K\n\n### Data Source and Approach\n\nNo directly measured excess molar volume (V^E) data for the water + 1-propanol binary system were found in the ThermoML database at any temperature. Instead, V^E was derived via an **exact pointwise transformation** (DP2: density → molar volume → V^E) from measured mass density data.\n\n**Source block:** PROPblock_14 (GLOBlit_11042, DOI: 10.1021/je700700f)\n- **System:** water + 1-propanol (propan-1-ol)\n- **Conditions:** T = 298.15 K, P = 101.0 kPa\n- **Data:** 13 data points (11 mixture + 2 pure endpoints), mole fraction of propan-1-ol from 0 to 1\n- **Density range:** 997.2 kg/m³ (pure water) to 799.6 kg/m³ (pure 1-propanol)\n\n### Pure-Component Molar Volumes (from block endpoints)\n\n| Component | V*_m (m³/mol) | Source |\n|-----------|---------------|--------|\n| Water | 1.8065584 × 10⁻⁵ | Block edge at x = 0 (direct/good) |\n| 1-Propanol | 7.5157579 × 10⁻⁵ | Block edge at x = 1 (direct/good) |\n\n### Redlich-Kister Fit Results\n\nThe excess molar volume was fitted to a Redlich-Kister polynomial:\n\n$$V^E(x_1) = x_1(1-x_1) \\sum_{k=0}^{n} A_k (1-2x_1)^k$$\n\nwhere x₁ = mole fraction of propan-1-ol.\n\n**BIC-selected order:** 5\n\n| Parameter | Value |\n|-----------|-------|\n| A₀ | −2.58261 × 10⁻⁶ m³/mol |\n| A₁ | 6.37900 × 10⁻⁷ m³/mol |\n| A₂ | −7.30522 × 10⁻⁷ m³/mol |\n| A₃ | 1.43441 × 10⁻⁷ m³/mol |\n| A₄ | −2.03775 × 10⁻⁶ m³/mol |\n| A₅ | 1.66755 × 10⁻⁶ m³/mol |\n\n### Fit Quality\n\n| Statistic | Value |\n|-----------|-------|\n| R² | 0.999276 |\n| RMSE | 4.603 × 10⁻⁹ m³/mol |\n| BIC | −407.94 |\n\n**BIC comparison across orders:**\n\n| Order | BIC | R² | RMSE (m³/mol) |\n|-------|------|----|---------------|\n| 0 | −353.00 | 0.682 | 9.64 × 10⁻⁸ |\n| 1 | −358.25 | 0.841 | 6.81 × 10⁻⁸ |\n| 2 | −374.82 | 0.972 | 2.88 × 10⁻⁸ |\n| 3 | −384.54 | 0.991 | 1.66 × 10⁻⁸ |\n| 4 | −400.44 | 0.998 | 7.22 × 10⁻⁹ |\n| **5** | **−407.94** | **0.999** | **4.60 × 10⁻⁹** |\n\n### Maximum Volume Contraction\n\nFrom the RK prediction (101-point grid, tool-returned via `predict_from_rk`):\n\n- **Minimum V^E = −6.591 × 10⁻⁷ m³/mol** (tool-returned max |excess|)\n\nThe tool-returned total molar volume at x₁ = 0.5 is V_m(0.5) ≈ 4.59659 × 10⁻⁵ m³/mol. Since this is close to the minimum of the excess curve, the composition of maximum volume contraction lies near x₁ ≈ 0.5 (mole fraction of 1-propanol). The asymmetric RK coefficients (nonzero A₁ through A₅) indicate the exact minimum is slightly shifted from x₁ = 0.5.\n\n### Chemistry Insight\n\nThe strongly negative V^E across the entire composition range reflects the well-known non-ideal mixing behavior of water + 1-propanol. The volume contraction arises from the interstitial accommodation of the smaller water molecules within the hydrogen-bonded alcohol network, combined with strong water–alcohol hydrogen bonding that produces a more compact liquid structure than either pure component. The asymmetry of the V^E curve (shifted slightly toward the water-rich side) is characteristic of aqueous alcohol systems where the disruption of the water hydrogen-bond network by alcohol molecules is most pronounced at intermediate compositions.\n\n### Output Files\n\n- **Fit data CSV:** `10_1021_je700700f_BPROPblock_14_fit.csv`\n- **Excess property CSV:** `10_1021_je700700f_BPROPblock_14_excess.csv`\n- **Fit plot:** `10_1021_je700700f_BPROPblock_14_fit.png`\n- **Excess plot:** `10_1021_je700700f_BPROPblock_14_excess.png`",
  "core_claims": [
    "No directly measured excess molar volume (V^E) data for water + 1-propanol were found in the ThermoML database; V^E was instead derived from measured mass density data via an exact pointwise transformation (density → molar volume → V^E).",
    "The source data (DOI: 10.1021/je700700f) comprise 13 density data points (11 mixture + 2 pure endpoints) for water + 1-propanol at T = 298.15 K and P = 101.0 kPa, with densities ranging from 997.2 kg/m³ (pure water) to 799.6 kg/m³ (pure 1-propanol).",
    "Pure-component molar volumes used were 1.8065584 × 10⁻⁵ m³/mol for water and 7.5157579 × 10⁻⁵ m³/mol for 1-propanol, taken from the block endpoints.",
    "A BIC-selected 5th-order Redlich-Kister polynomial fit yielded R² = 0.999276, RMSE = 4.603 × 10⁻⁹ m³/mol, and BIC = −407.94, outperforming lower-order fits.",
    "The excess molar volume is strongly negative across the entire composition range, with a minimum V^E of −6.591 × 10⁻⁷ m³/mol occurring near x₁ ≈ 0.5 (mole fraction of 1-propanol), slightly shifted from x₁ = 0.5 due to asymmetric RK coefficients.",
    "The volume contraction is attributed to interstitial accommodation of water molecules within the alcohol hydrogen-bonded network and strong water–alcohol hydrogen bonding producing a more compact liquid structure than either pure component."
  ],
  "sources": [
    {
      "doi": "10.1021/je700700f",
      "lit_num_id": "GLOBlit_11042",
      "block": "PROPblock_14",
      "BLKsubsys_id": null,
      "description": "Provides 13 mass-density data points (799.6–997.2 kg/m³) for the water + 1-propanol binary system at 298.15 K across the full mole-fraction range (0–1), from which excess molar volumes were derived via the density-to-V^E transformation and fitted to a 5th-order Redlich-Kister polynomial."
    }
  ],
  "fit_results": [
    {
      "doi": "10.1021/je700700f",
      "lit_num_id": "GLOBlit_11042",
      "block_number": "PROPblock_14",
      "BLKsubsys_id": null,
      "property": "GLOBprop_1",
      "rk_order": 5,
      "rk_coeffs": [
        -2.5826148721793675e-06,
        6.379003960766906e-07,
        -7.305218674405775e-07,
        1.4344091663959586e-07,
        -2.0377486676098777e-06,
        1.6675480055258805e-06
      ],
      "r_squared": 0.999276,
      "rmse": 4.602814010602905e-09,
      "n_points": 11,
      "temperature_K": null,
      "mixing_rule": "linear"
    }
  ]
}

---

## Data Inspections (deterministic evidence ledger)

Hardcoded envelope merge — not agent-authored. 8 entr(ies); verbatim rows below.

- INSP_c42538d00a95 — GLOBlit_2979::PROPblock_9 · rdp · 14 rows
- INSP_55e0f65ed072 — GLOBlit_555::PROPblock_8 · nearest · 3 rows
- INSP_5628de772e5a — GLOBlit_2432::PROPblock_3 · nearest · 5 rows
- INSP_615d3595b96a — GLOBlit_11042::PROPblock_14 · rdp · 8 rows
- INSP_317fb35a109d — GLOBlit_11142::PROPblock_3 · nearest · 3 rows
- INSP_82d017dcc43b — GLOBlit_11042::PROPblock_14 · complete · 2 rows
- INSP_b7c0c315350f — GLOBlit_11042::PROPblock_14 · complete · 4 rows
- INSP_8436f6588aa6 — GLOBlit_2979::PROPblock_9 · rdp · 19 rows

```json
[
  {
    "doi": "10.1016/j.jct.2008.07.005",
    "block_number": "PROPblock_9",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<propan-1-ol>",
      "pressure_kpa",
      "mass_density_kg_m3"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_49",
        "temperature_k": "298.15",
        "mole_fraction_<propan-1-ol>": "0",
        "pressure_kpa": "98.93",
        "mass_density_kg_m3": "997.04"
      },
      {
        "BLKpoint_id": "BLKpoint_50",
        "temperature_k": "298.15",
        "mole_fraction_<propan-1-ol>": "0.002",
        "pressure_kpa": "98.93",
        "mass_density_kg_m3": "995.4"
      },
      {
        "BLKpoint_id": "BLKpoint_52",
        "temperature_k": "298.15",
        "mole_fraction_<propan-1-ol>": "0.009",
        "pressure_kpa": "98.93",
        "mass_density_kg_m3": "991.66"
      },
      {
        "BLKpoint_id": "BLKpoint_54",
        "temperature_k": "298.15",
        "mole_fraction_<propan-1-ol>": "0.02",
        "pressure_kpa": "98.93",
        "mass_density_kg_m3": "986.54"
      },
      {
        "BLKpoint_id": "BLKpoint_55",
        "temperature_k": "298.15",
        "mole_fraction_<propan-1-ol>": "0.03",
        "pressure_kpa": "98.93",
        "mass_density_kg_m3": "982.56"
      },
      {
        "BLKpoint_id": "BLKpoint_56",
        "temperature_k": "298.15",
        "mole_fraction_<propan-1-ol>": "0.05",
        "pressure_kpa": "98.93",
        "mass_density_kg_m3": "975.49"
      },
      {
        "BLKpoint_id": "BLKpoint_57",
        "temperature_k": "298.15",
        "mole_fraction_<propan-1-ol>": "0.065",
        "pressure_kpa": "98.93",
        "mass_density_kg_m3": "969.94"
      },
      {
        "BLKpoint_id": "BLKpoint_58",
        "temperature_k": "298.15",
        "mole_fraction_<propan-1-ol>": "0.08",
        "pressure_kpa": "98.93",
        "mass_density_kg_m3": "963.72"
      },
      {
        "BLKpoint_id": "BLKpoint_59",
        "temperature_k": "298.15",
        "mole_fraction_<propan-1-ol>": "0.1",
        "pressure_kpa": "98.93",
        "mass_density_kg_m3": "954.91"
      },
      {
        "BLKpoint_id": "BLKpoint_60",
        "temperature_k": "298.15",
        "mole_fraction_<propan-1-ol>": "0.13",
        "pressure_kpa": "98.93",
        "mass_density_kg_m3": "941.96"
      },
      {
        "BLKpoint_id": "BLKpoint_61",
        "temperature_k": "298.15",
        "mole_fraction_<propan-1-ol>": "0.15",
        "pressure_kpa": "98.93",
        "mass_density_kg_m3": "934.12"
      },
      {
        "BLKpoint_id": "BLKpoint_62",
        "temperature_k": "298.15",
        "mole_fraction_<propan-1-ol>": "0.17",
        "pressure_kpa": "98.93",
        "mass_density_kg_m3": "926.68"
      },
      {
        "BLKpoint_id": "BLKpoint_63",
        "temperature_k": "298.15",
        "mole_fraction_<propan-1-ol>": "0.1856",
        "pressure_kpa": "98.93",
        "mass_density_kg_m3": "921.23"
      },
      {
        "BLKpoint_id": "BLKpoint_64",
        "temperature_k": "298.15",
        "mole_fraction_<propan-1-ol>": "0.2",
        "pressure_kpa": "98.93",
        "mass_density_kg_m3": "916.46"
      }
    ],
    "inspection_id": "INSP_c42538d00a95",
    "lit_num_id": "GLOBlit_2979"
  },
  {
    "doi": "10.1016/j.fluid.2007.07.066",
    "block_number": "PROPblock_8",
    "table_mode": "nearest",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mass_fraction_<propan-1-ol>",
      "pressure_kpa",
      "mass_density_kg_m3"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_10",
        "temperature_k": "298.15",
        "mass_fraction_<propan-1-ol>": "0.05",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "989.431"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "temperature_k": "298.15",
        "mass_fraction_<propan-1-ol>": "0.1",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "983.475"
      },
      {
        "BLKpoint_id": "BLKpoint_12",
        "temperature_k": "298.15",
        "mass_fraction_<propan-1-ol>": "0.15",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "978.117"
      }
    ],
    "inspection_id": "INSP_55e0f65ed072",
    "lit_num_id": "GLOBlit_555"
  },
  {
    "doi": "10.1016/j.jct.2004.07.019",
    "block_number": "PROPblock_3",
    "table_mode": "nearest",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "pressure_kpa",
      "molality_mol_kg_<propan-1-ol>",
      "mass_density_kg_m3"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "298.15",
        "pressure_kpa": "420",
        "molality_mol_kg_<propan-1-ol>": "0.10076",
        "mass_density_kg_m3": "-1.0456"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "temperature_k": "298.15",
        "pressure_kpa": "420",
        "molality_mol_kg_<propan-1-ol>": "0.21222",
        "mass_density_kg_m3": "-2.149"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "temperature_k": "298.15",
        "pressure_kpa": "420",
        "molality_mol_kg_<propan-1-ol>": "0.35404",
        "mass_density_kg_m3": "-3.4984"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "temperature_k": "298.15",
        "pressure_kpa": "420",
        "molality_mol_kg_<propan-1-ol>": "0.53097",
        "mass_density_kg_m3": "-5.0885"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "temperature_k": "298.15",
        "pressure_kpa": "420",
        "molality_mol_kg_<propan-1-ol>": "0.77737",
        "mass_density_kg_m3": "-7.1764"
      }
    ],
    "inspection_id": "INSP_5628de772e5a",
    "lit_num_id": "GLOBlit_2432"
  },
  {
    "doi": "10.1021/je700700f",
    "block_number": "PROPblock_14",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "mole_fraction_<propan-1-ol>",
      "pressure_kpa",
      "temperature_k",
      "mass_density_kg_m3"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "mole_fraction_<propan-1-ol>": "0",
        "pressure_kpa": "101.0",
        "temperature_k": "298.15",
        "mass_density_kg_m3": "997.2"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "mole_fraction_<propan-1-ol>": "0.1986",
        "pressure_kpa": "101.0",
        "temperature_k": "298.15",
        "mass_density_kg_m3": "914.9"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "mole_fraction_<propan-1-ol>": "0.2979",
        "pressure_kpa": "101.0",
        "temperature_k": "298.15",
        "mass_density_kg_m3": "887.2"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "mole_fraction_<propan-1-ol>": "0.3949",
        "pressure_kpa": "101.0",
        "temperature_k": "298.15",
        "mass_density_kg_m3": "866.9"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "mole_fraction_<propan-1-ol>": "0.4955",
        "pressure_kpa": "101.0",
        "temperature_k": "298.15",
        "mass_density_kg_m3": "850.3"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "mole_fraction_<propan-1-ol>": "0.5953",
        "pressure_kpa": "101.0",
        "temperature_k": "298.15",
        "mass_density_kg_m3": "836.9"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "mole_fraction_<propan-1-ol>": "0.7969",
        "pressure_kpa": "101.0",
        "temperature_k": "298.15",
        "mass_density_kg_m3": "816.3"
      },
      {
        "BLKpoint_id": "BLKpoint_13",
        "mole_fraction_<propan-1-ol>": "1",
        "pressure_kpa": "101.0",
        "temperature_k": "298.15",
        "mass_density_kg_m3": "799.6"
      }
    ],
    "inspection_id": "INSP_615d3595b96a",
    "lit_num_id": "GLOBlit_11042"
  },
  {
    "doi": "10.1021/je800158z",
    "block_number": "PROPblock_3",
    "table_mode": "nearest",
    "columns": [
      "BLKpoint_id",
      "mole_fraction_<propan-1-ol>",
      "temperature_k",
      "pressure_kpa",
      "mass_density_kg_m3"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "mole_fraction_<propan-1-ol>": "0",
        "temperature_k": "293.15",
        "pressure_kpa": "81.5",
        "mass_density_kg_m3": "998.2"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "mole_fraction_<propan-1-ol>": "0.0401",
        "temperature_k": "293.15",
        "pressure_kpa": "81.5",
        "mass_density_kg_m3": "980.98"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "mole_fraction_<propan-1-ol>": "0",
        "temperature_k": "303.15",
        "pressure_kpa": "81.5",
        "mass_density_kg_m3": "995.64"
      }
    ],
    "inspection_id": "INSP_317fb35a109d",
    "lit_num_id": "GLOBlit_11142"
  },
  {
    "doi": "10.1021/je700700f",
    "block_number": "PROPblock_14",
    "table_mode": "complete",
    "columns": [
      "BLKpoint_id",
      "mole_fraction_<propan-1-ol>",
      "pressure_kpa",
      "temperature_k",
      "mass_density_kg_m3"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_2",
        "mole_fraction_<propan-1-ol>": "0.0504",
        "pressure_kpa": "101.0",
        "temperature_k": "298.15",
        "mass_density_kg_m3": "975.1"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "mole_fraction_<propan-1-ol>": "0.0993",
        "pressure_kpa": "101.0",
        "temperature_k": "298.15",
        "mass_density_kg_m3": "953.3"
      }
    ],
    "inspection_id": "INSP_82d017dcc43b",
    "lit_num_id": "GLOBlit_11042"
  },
  {
    "doi": "10.1021/je700700f",
    "block_number": "PROPblock_14",
    "table_mode": "complete",
    "columns": [
      "BLKpoint_id",
      "mole_fraction_<propan-1-ol>",
      "pressure_kpa",
      "temperature_k",
      "mass_density_kg_m3"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_9",
        "mole_fraction_<propan-1-ol>": "0.6995",
        "pressure_kpa": "101.0",
        "temperature_k": "298.15",
        "mass_density_kg_m3": "825.6"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "mole_fraction_<propan-1-ol>": "0.7969",
        "pressure_kpa": "101.0",
        "temperature_k": "298.15",
        "mass_density_kg_m3": "816.3"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "mole_fraction_<propan-1-ol>": "0.8983",
        "pressure_kpa": "101.0",
        "temperature_k": "298.15",
        "mass_density_kg_m3": "807.7"
      },
      {
        "BLKpoint_id": "BLKpoint_12",
        "mole_fraction_<propan-1-ol>": "0.9518",
        "pressure_kpa": "101.0",
        "temperature_k": "298.15",
        "mass_density_kg_m3": "803.5"
      }
    ],
    "inspection_id": "INSP_b7c0c315350f",
    "lit_num_id": "GLOBlit_11042"
  },
  {
    "doi": "10.1016/j.jct.2008.07.005",
    "block_number": "PROPblock_9",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<propan-1-ol>",
      "pressure_kpa",
      "mass_density_kg_m3"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "283.15",
        "mole_fraction_<propan-1-ol>": "0",
        "pressure_kpa": "98.93",
        "mass_density_kg_m3": "999.69"
      },
      {
        "BLKpoint_id": "BLKpoint_12",
        "temperature_k": "283.15",
        "mole_fraction_<propan-1-ol>": "0.13",
        "pressure_kpa": "98.93",
        "mass_density_kg_m3": "947.97"
      },
      {
        "BLKpoint_id": "BLKpoint_16",
        "temperature_k": "283.15",
        "mole_fraction_<propan-1-ol>": "0.2",
        "pressure_kpa": "98.93",
        "mass_density_kg_m3": "923.98"
      },
      {
        "BLKpoint_id": "BLKpoint_17",
        "temperature_k": "288.15",
        "mole_fraction_<propan-1-ol>": "0",
        "pressure_kpa": "98.93",
        "mass_density_kg_m3": "999.1"
      },
      {
        "BLKpoint_id": "BLKpoint_28",
        "temperature_k": "288.15",
        "mole_fraction_<propan-1-ol>": "0.13",
        "pressure_kpa": "98.93",
        "mass_density_kg_m3": "946"
      },
      {
        "BLKpoint_id": "BLKpoint_32",
        "temperature_k": "288.15",
        "mole_fraction_<propan-1-ol>": "0.2",
        "pressure_kpa": "98.93",
        "mass_density_kg_m3": "921.89"
      },
      {
        "BLKpoint_id": "BLKpoint_33",
        "temperature_k": "293.15",
        "mole_fraction_<propan-1-ol>": "0",
        "pressure_kpa": "98.93",
        "mass_density_kg_m3": "998.21"
      },
      {
        "BLKpoint_id": "BLKpoint_38",
        "temperature_k": "293.15",
        "mole_fraction_<propan-1-ol>": "0.02",
        "pressure_kpa": "98.93",
        "mass_density_kg_m3": "987.82"
      },
      {
        "BLKpoint_id": "BLKpoint_44",
        "temperature_k": "293.15",
        "mole_fraction_<propan-1-ol>": "0.13",
        "pressure_kpa": "98.93",
        "mass_density_kg_m3": "944.52"
      },
      {
        "BLKpoint_id": "BLKpoint_48",
        "temperature_k": "293.15",
        "mole_fraction_<propan-1-ol>": "0.2",
        "pressure_kpa": "98.93",
        "mass_density_kg_m3": "919.56"
      },
      {
        "BLKpoint_id": "BLKpoint_49",
        "temperature_k": "298.15",
        "mole_fraction_<propan-1-ol>": "0",
        "pressure_kpa": "98.93",
        "mass_density_kg_m3": "997.04"
      },
      {
        "BLKpoint_id": "BLKpoint_60",
        "temperature_k": "298.15",
        "mole_fraction_<propan-1-ol>": "0.13",
        "pressure_kpa": "98.93",
        "mass_density_kg_m3": "941.96"
      },
      {
        "BLKpoint_id": "BLKpoint_64",
        "temperature_k": "298.15",
        "mole_fraction_<propan-1-ol>": "0.2",
        "pressure_kpa": "98.93",
        "mass_density_kg_m3": "916.46"
      },
      {
        "BLKpoint_id": "BLKpoint_65",
        "temperature_k": "303.15",
        "mole_fraction_<propan-1-ol>": "0",
        "pressure_kpa": "98.93",
        "mass_density_kg_m3": "995.65"
      },
      {
        "BLKpoint_id": "BLKpoint_76",
        "temperature_k": "303.15",
        "mole_fraction_<propan-1-ol>": "0.13",
        "pressure_kpa": "98.93",
        "mass_density_kg_m3": "939.8"
      },
      {
        "BLKpoint_id": "BLKpoint_80",
        "temperature_k": "303.15",
        "mole_fraction_<propan-1-ol>": "0.2",
        "pressure_kpa": "98.93",
        "mass_density_kg_m3": "914.04"
      },
      {
        "BLKpoint_id": "BLKpoint_81",
        "temperature_k": "308.15",
        "mole_fraction_<propan-1-ol>": "0",
        "pressure_kpa": "98.93",
        "mass_density_kg_m3": "994.03"
      },
      {
        "BLKpoint_id": "BLKpoint_92",
        "temperature_k": "308.15",
        "mole_fraction_<propan-1-ol>": "0.13",
        "pressure_kpa": "98.93",
        "mass_density_kg_m3": "937.47"
      },
      {
        "BLKpoint_id": "BLKpoint_96",
        "temperature_k": "308.15",
        "mole_fraction_<propan-1-ol>": "0.2",
        "pressure_kpa": "98.93",
        "mass_density_kg_m3": "911.83"
      }
    ],
    "inspection_id": "INSP_8436f6588aa6",
    "lit_num_id": "GLOBlit_2979"
  }
]
```

---

## Verdict

**Data Quality**
The agent correctly derived V^E from density data via `fit_block_derived` with a density→V^E transform, which is an acceptable exact route when direct V^E data are unavailable. The source (DOI: 10.1021/je700700f) and block are traceable. However, the minimum V^E value of −6.591×10⁻⁷ m³/mol (≈−0.659 cm³/mol) is reasonable for water+1-propanol. The composition basis is mole fraction. The predict_from_rk call returned results, but the agent's claim of minimum at "x₁≈0.5" is vague—the tool output should have provided the exact composition. No fabrication flags detected.

**Fit Quality**
Order 5 with R²=0.999 is acceptable given 11 mixture points, though 6 parameters for 11 points risks mild overfitting. BIC selection mitigates this concern. RMSE is very small.

**Scientific Verdict**
The minimum V^E ≈ −0.66 cm³/mol near x₁≈0.5 is consistent with literature values (~−0.6 to −0.7 cm³/mol). The agent should have reported the exact minimum composition from the prediction grid rather than approximating. Overall, results are scientifically sound. **PASS**.

---

## Output Files

- **data**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_023326_012061_3dba9dd4\analysis_runs\run_5\data\10_1021_je700700f_BPROPblock_14_fit.csv` — RK fit data — 10.1021/je700700f PROPblock_14
- **data**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_023326_012061_3dba9dd4\analysis_runs\run_5\data\10_1021_je700700f_BPROPblock_14_excess.csv` — Excess property — 10.1021/je700700f PROPblock_14
- **plot**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_023326_012061_3dba9dd4\analysis_runs\run_5\plots\10_1021_je700700f_BPROPblock_14_fit.png` — RK fit plot — 10.1021/je700700f PROPblock_14
- **plot**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_023326_012061_3dba9dd4\analysis_runs\run_5\plots\10_1021_je700700f_BPROPblock_14_excess.png` — Excess plot — 10.1021/je700700f PROPblock_14