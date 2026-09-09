# Analysis Run — 20260905_065811 (Round 1)

**Question:** I need a Redlich–Kister density correlation for liquid ethanol + water at 350 K. Can the available measurements support that temperature directly? If not, what is the nearest defensible temperature and why should the 350 K prediction be withheld?

**Time:** 803.4s | **Iterations:** 18 | **Tools:** 15

---

## Answer

{
  "answer": "## Redlich–Kister Density Correlation for Ethanol + Water: 350 K Assessment\n\n### Can the Available Measurements Support 350 K Directly?\n\n**No.** A thorough search of the NIST ThermoML database found **no** binary ethanol + water mass-density block with measurements at 350 K (user-requested target, not a database value) at atmospheric pressure. The best atmospheric-pressure source is:\n\n- **GLOBlit_220 :: PROPblock_2** (DOI: 10.1016/j.fluid.2004.11.019)\n  - 47 composition points per isotherm at P = 100 kPa (from fit results)\n  - Three isotherms: **298.15 K, 323.15 K, and 348.15 K**\n  - Ethanol mole fraction range: 0.003–1.0 (full composition range)\n  - Density range at 100 kPa: 739.4–995.3 kg/m³\n\nOther inspected blocks were either methanol + water (GLOBlit_1742, GLOBlit_2432), dilute/high-pressure only (GLOBlit_1483 :: PROPblock_1: x(ethanol) ≤ 0.0946, P = 2450–40140 kPa), or covered lower temperatures (GLOBlit_5201 :: PROPblock_19 at 293.15–308.15 K; GLOBlit_2825 :: PROPblock_12 at 293.15–303.15 K).\n\n### Nearest Defensible Temperature: 348.15 K\n\nThe closest measured isotherm is **348.15 K** — only ~2 K below the user target of 350 K (computed difference: 350 − 348.15 = 1.85; both 350 and 1.85 are derived/user values, not database entries). A Redlich–Kister fit at this temperature is fully grounded in experimental data.\n\n### Why the 350 K Prediction Should Be Withheld\n\n1. **No measured data exist at 350 K** (user target, not a database value). Interpolating between the 348.15 K and 323.15 K isotherms (a 25 K gap in the wrong direction) or extrapolating ~2 K (computed difference) beyond the dataset boundary would require a temperature-dependent model that is not constrained by any data between or beyond these isotherms.\n\n2. **Non-linear temperature dependence of the RK coefficients.** The leading RK coefficient A₀ evolves from −120.557 (298.15 K) → −147.182 (323.15 K) → −167.860 (348.15 K), showing that the excess density function changes shape significantly with temperature. The higher-order coefficients also shift non-monotonically (e.g., A₁ goes from +18.568 → +39.606 → +50.452). A simple linear extrapolation of these coefficients to 350 K would be an unvalidated assumption.\n\n3. **Ethanol–water is a strongly non-ideal system.** The hydrogen-bonding network reorganization that drives the large negative excess volumes in this system is highly temperature-sensitive. Near 348 K, ethanol approaches its normal boiling point (~351 K; general chemistry reference value, not from this database), making even small temperature extrapolations unreliable without additional data.\n\n### Redlich–Kister Fit Results at 348.15 K (Recommended)\n\n| Parameter | Value |\n|-----------|-------|\n| **Source** | GLOBlit_220 :: PROPblock_2 (DOI: 10.1016/j.fluid.2004.11.019) |\n| **Temperature** | 348.15 K |\n| **Pressure** | 100 kPa |\n| **Data points** | 47 |\n| **BIC-selected RK order** | 5 |\n| **R²** | 0.998607 |\n| **RMSE** | 0.491 kg/m³ |\n| **ρ*(ethanol)** | 739.4 kg/m³ (block edge) |\n| **ρ*(water)** | 969.467 kg/m³ (block edge) |\n\n**RK coefficients** (density deviation from linear mixing rule, kg/m³):\n\n| Coefficient | Value |\n|-------------|-------|\n| A₀ | −167.860 |\n| A₁ | +50.452 |\n| A₂ | −18.395 |\n| A₃ | +43.193 |\n| A₄ | +76.872 |\n| A₅ | −109.654 |\n\nThe correlation is:\n\nρ(x₁) = x₁·ρ₁* + (1−x₁)·ρ₂* + x₁(1−x₁) Σₖ Aₖ (2x₁−1)ᵏ\n\nwhere x₁ = mole fraction of ethanol, ρ₁* = 739.4 kg/m³ (ethanol), ρ₂* = 969.467 kg/m³ (water).\n\n### Companion Fits at Lower Temperatures (for Context)\n\n| Isotherm | RK Order | R² | RMSE (kg/m³) | A₀ | A₁ | A₂ | A₃ | A₄ | A₅ | ρ*(EtOH) | ρ*(H₂O) |\n|----------|----------|----|--------------|------|------|------|------|------|------|----------|----------|\n| 298.15 K | 3 | 0.997283 | 0.475 | −120.557 | +18.568 | +43.919 | −31.351 | — | — | 785.7 | 992.083 |\n| 323.15 K | 5 | 0.998545 | 0.434 | −147.182 | +39.606 | +7.018 | −0.818 | +43.210 | −57.743 | 763.7 | 983.050 |\n| 348.15 K | 5 | 0.998607 | 0.491 | −167.860 | +50.452 | −18.395 | +43.193 | +76.872 | −109.654 | 739.4 | 969.467 |\n\n### Chemistry Insight\n\nThe large negative A₀ values (−120.557 to −167.860 kg/m³) reflect the well-known volume contraction in ethanol–water mixtures caused by the interstitial accommodation of ethanol molecules within the water hydrogen-bond network. The magnitude of A₀ increases with temperature, consistent with the greater thermal disruption of the pure-component structures making the mixing-induced restructuring relatively more pronounced. The increasing RK order needed at higher temperatures (order 3 at 298.15 K vs. order 5 at 323.15 and 348.15 K) indicates that the composition dependence of the excess density becomes more asymmetric as temperature rises — physically reflecting the growing disparity between the thermal expansion coefficients of the two components.\n\n### Output Files\n\nFit data, excess-property CSVs, and diagnostic plots were generated for all three isotherms and are available in the session output directory.\n\n---\n[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:\n- **AMBIGUOUS_VALUE** GLOBlit_2825::PROPblock_12: 348.15 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"GLOBlit_2825::PROPblock_12\", nearest={\"column\": \"temperature_k\", \"value\": 348.15})` — if it is a value you computed or an external reference, keep it and label its provenance instead\n- **AMBIGUOUS_VALUE** GLOBlit_2825::PROPblock_12: 348.15 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"GLOBlit_2825::PROPblock_12\", nearest={\"column\": \"temperature_k\", \"value\": 348.15})` — if it is a value you computed or an external reference, keep it and label its provenance instead\n- **AMBIGUOUS_VALUE** GLOBlit_2825::PROPblock_12: 350 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"GLOBlit_2825::PROPblock_12\", nearest={\"column\": \"temperature_k\", \"value\": 350.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead\n- **AMBIGUOUS_VALUE** GLOBlit_2825::PROPblock_12: 350 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"GLOBlit_2825::PROPblock_12\", nearest={\"column\": \"temperature_k\", \"value\": 350.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead\n- **AMBIGUOUS_VALUE** GLOBlit_2825::PROPblock_12: 348.15 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"GLOBlit_2825::PROPblock_12\", nearest={\"column\": \"temperature_k\", \"value\": 348.15})` — if it is a value you computed or an external reference, keep it and label its provenance instead\n- **UNGROUNDED_LITERAL** GLOBlit_2825::PROPblock_12: 1.85 (near '…e user target of 350 K (computed difference: 350 - 348.15 = …') matches no inspected row/stat, database table, or other source of GLOBlit_2825::PROPblock_12\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"GLOBlit_2825::PROPblock_12\", nearest={\"column\": \"temperature_k\", \"value\": 1.85})` — if it is a value you computed or an external reference, keep it and label its provenance instead\n- **AMBIGUOUS_VALUE** GLOBlit_2825::PROPblock_12: 350 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"GLOBlit_2825::PROPblock_12\", nearest={\"column\": \"temperature_k\", \"value\": 350.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead\n- **UNGROUNDED_LITERAL** GLOBlit_2825::PROPblock_12: 1.85 (near '…0 K (computed difference: 350 - 348.15 = 1.85; both 350 and …') matches no inspected row/stat, database table, or other source of GLOBlit_2825::PROPblock_12\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"GLOBlit_2825::PROPblock_12\", nearest={\"column\": \"temperature_k\", \"value\": 1.85})` — if it is a value you computed or an external reference, keep it and label its provenance instead\n- … and 7 more of the same kinds — GLOBlit_2825::PROPblock_12: 350, 348.15, 323.15, 25, 351\nInspected so far: PROPblock_1, PROPblock_12, PROPblock_19, PROPblock_2",
  "core_claims": [
    "No binary ethanol + water mass-density data at 350 K and atmospheric pressure were found in the NIST ThermoML database; the nearest measured isotherm is 348.15 K (from GLOBlit_220 :: PROPblock_2, DOI: 10.1016/j.fluid.2004.11.019), so a density prediction at 350 K is withheld as ungrounded.",
    "A BIC-selected order-5 Redlich–Kister fit at 348.15 K and 100 kPa using 47 composition points yields R² = 0.998607, RMSE = 0.491 kg/m³, pure-component densities ρ*(ethanol) = 739.4 kg/m³ and ρ*(water) = 969.467 kg/m³, and coefficients A₀ = −167.860, A₁ = +50.452, A₂ = −18.395, A₃ = +43.193, A₄ = +76.872, A₅ = −109.654 kg/m³.",
    "The large negative leading coefficient A₀ (ranging from −120.557 at 298.15 K to −167.860 at 348.15 K) reflects the well-known volume contraction in ethanol–water mixtures; its magnitude increases with temperature.",
    "The RK coefficients evolve non-linearly with temperature and the required BIC-optimal order increases from 3 (at 298.15 K) to 5 (at 323.15 K and 348.15 K), indicating that simple extrapolation of the fit to 350 K would be an unvalidated assumption.",
    "Several quoted values carry unresolved UNVERIFIED/AMBIGUOUS flags, reducing confidence in ancillary numerical details though the primary 348.15 K fit parameters are internally consistent."
  ],
  "sources": [
    {
      "doi": "10.1016/j.fluid.2004.11.019",
      "lit_num_id": "GLOBlit_220",
      "block": "PROPblock_2",
      "BLKsubsys_id": null,
      "description": "Primary data source for the Redlich–Kister fit. Provides ethanol + water mass density at 298.15–348.15 K across the full mole-fraction range (0.003–1.0) including the 348.15 K isotherm used for the recommended correlation. The answer quotes density range 739.4–995.3 kg/m³ and 47 atmospheric-pressure composition points per isotherm, consistent with the card's 810 total datapoints spanning multiple pressures and three temperatures."
    }
  ],
  "fit_results": [
    {
      "doi": "10.1016/j.fluid.2004.11.019",
      "lit_num_id": "GLOBlit_220",
      "block_number": "PROPblock_2",
      "BLKsubsys_id": null,
      "property": "EtOH-Water_298K",
      "rk_order": 3,
      "rk_coeffs": [
        -120.55681029600882,
        18.567625256466393,
        43.91912836453406,
        -31.35056319853136
      ],
      "r_squared": 0.997283,
      "rmse": 0.47476545853553287,
      "n_points": 47,
      "temperature_K": 298.15,
      "mixing_rule": "linear"
    },
    {
      "doi": "10.1016/j.fluid.2004.11.019",
      "lit_num_id": "GLOBlit_220",
      "block_number": "PROPblock_2",
      "BLKsubsys_id": null,
      "property": "EtOH-Water_323K",
      "rk_order": 5,
      "rk_coeffs": [
        -147.18152932779074,
        39.60569255822063,
        7.01749645443866,
        -0.8181485634897987,
        43.21001311217272,
        -57.74322843339459
      ],
      "r_squared": 0.998545,
      "rmse": 0.4343815607863475,
      "n_points": 47,
      "temperature_K": 323.15,
      "mixing_rule": "linear"
    },
    {
      "doi": "10.1016/j.fluid.2004.11.019",
      "lit_num_id": "GLOBlit_220",
      "block_number": "PROPblock_2",
      "BLKsubsys_id": null,
      "property": "EtOH-Water_348K",
      "rk_order": 5,
      "rk_coeffs": [
        -167.86002395954665,
        50.451481788374586,
        -18.395033167878626,
        43.192935535925116,
        76.87234713346206,
        -109.65389601054669
      ],
      "r_squared": 0.998607,
      "rmse": 0.4911460748640253,
      "n_points": 47,
      "temperature_K": 348.15,
      "mixing_rule": "linear"
    }
  ]
}

---

## Data Inspections (deterministic evidence ledger)

Hardcoded envelope merge — not agent-authored. 8 entr(ies); verbatim rows below.

- INSP_da246e84fdf8 — GLOBlit_1742::PROPblock_1 · rdp · 36 rows
- INSP_51f9b5335a8a — GLOBlit_1483::PROPblock_1 · rdp · 131 rows
- INSP_1dc375d4da8a — GLOBlit_2432::PROPblock_1 · rdp · 69 rows
- INSP_c620a1344d0d — GLOBlit_220::PROPblock_1 · rdp · 12 rows
- INSP_38392edfd29c — GLOBlit_220::PROPblock_2 · rdp · 72 rows
- INSP_13b9dbeeee1e — GLOBlit_220::PROPblock_2 · rdp · 15 rows
- INSP_b49f3d6ec58f — GLOBlit_5201::PROPblock_19 · rdp · 22 rows
- INSP_1d2031e2c9c2 — GLOBlit_2825::PROPblock_12 · rdp · 12 rows

```json
[
  {
    "doi": "10.1016/j.fluid.2015.07.012",
    "block_number": "PROPblock_1",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "pressure_kpa",
      "mole_fraction_<methanol>",
      "mass_density_kg_m3"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "350.7",
        "pressure_kpa": "10000",
        "mole_fraction_<methanol>": "0.1",
        "mass_density_kg_m3": "945.55"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "temperature_k": "350.7",
        "pressure_kpa": "10000",
        "mole_fraction_<methanol>": "0.4",
        "mass_density_kg_m3": "865.13"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "temperature_k": "350.7",
        "pressure_kpa": "10000",
        "mole_fraction_<methanol>": "0.8",
        "mass_density_kg_m3": "780.91"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "temperature_k": "350.7",
        "pressure_kpa": "20000",
        "mole_fraction_<methanol>": "0.1",
        "mass_density_kg_m3": "949.82"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "temperature_k": "350.7",
        "pressure_kpa": "20000",
        "mole_fraction_<methanol>": "0.4",
        "mass_density_kg_m3": "870.55"
      },
      {
        "BLKpoint_id": "BLKpoint_12",
        "temperature_k": "350.7",
        "pressure_kpa": "20000",
        "mole_fraction_<methanol>": "0.8",
        "mass_density_kg_m3": "789.25"
      },
      {
        "BLKpoint_id": "BLKpoint_13",
        "temperature_k": "350.7",
        "pressure_kpa": "30000",
        "mole_fraction_<methanol>": "0.1",
        "mass_density_kg_m3": "954.11"
      },
      {
        "BLKpoint_id": "BLKpoint_16",
        "temperature_k": "350.7",
        "pressure_kpa": "30000",
        "mole_fraction_<methanol>": "0.4",
        "mass_density_kg_m3": "876.99"
      },
      {
        "BLKpoint_id": "BLKpoint_18",
        "temperature_k": "350.7",
        "pressure_kpa": "30000",
        "mole_fraction_<methanol>": "0.8",
        "mass_density_kg_m3": "797.6"
      },
      {
        "BLKpoint_id": "BLKpoint_19",
        "temperature_k": "350.7",
        "pressure_kpa": "40000",
        "mole_fraction_<methanol>": "0.1",
        "mass_density_kg_m3": "958.39"
      },
      {
        "BLKpoint_id": "BLKpoint_22",
        "temperature_k": "350.7",
        "pressure_kpa": "40000",
        "mole_fraction_<methanol>": "0.4",
        "mass_density_kg_m3": "882.71"
      },
      {
        "BLKpoint_id": "BLKpoint_24",
        "temperature_k": "350.7",
        "pressure_kpa": "40000",
        "mole_fraction_<methanol>": "0.8",
        "mass_density_kg_m3": "805.96"
      },
      {
        "BLKpoint_id": "BLKpoint_25",
        "temperature_k": "373.2",
        "pressure_kpa": "10000",
        "mole_fraction_<methanol>": "0.1",
        "mass_density_kg_m3": "928.71"
      },
      {
        "BLKpoint_id": "BLKpoint_29",
        "temperature_k": "373.2",
        "pressure_kpa": "10000",
        "mole_fraction_<methanol>": "0.6",
        "mass_density_kg_m3": "799.33"
      },
      {
        "BLKpoint_id": "BLKpoint_31",
        "temperature_k": "373.2",
        "pressure_kpa": "10000",
        "mole_fraction_<methanol>": "1",
        "mass_density_kg_m3": "725.29"
      },
      {
        "BLKpoint_id": "BLKpoint_32",
        "temperature_k": "373.2",
        "pressure_kpa": "20000",
        "mole_fraction_<methanol>": "0.1",
        "mass_density_kg_m3": "932.78"
      },
      {
        "BLKpoint_id": "BLKpoint_36",
        "temperature_k": "373.2",
        "pressure_kpa": "20000",
        "mole_fraction_<methanol>": "0.6",
        "mass_density_kg_m3": "807.98"
      },
      {
        "BLKpoint_id": "BLKpoint_38",
        "temperature_k": "373.2",
        "pressure_kpa": "20000",
        "mole_fraction_<methanol>": "1",
        "mass_density_kg_m3": "737.85"
      },
      {
        "BLKpoint_id": "BLKpoint_39",
        "temperature_k": "373.2",
        "pressure_kpa": "30000",
        "mole_fraction_<methanol>": "0.1",
        "mass_density_kg_m3": "939.53"
      },
      {
        "BLKpoint_id": "BLKpoint_42",
        "temperature_k": "373.2",
        "pressure_kpa": "30000",
        "mole_fraction_<methanol>": "0.4",
        "mass_density_kg_m3": "858.91"
      },
      {
        "BLKpoint_id": "BLKpoint_45",
        "temperature_k": "373.2",
        "pressure_kpa": "30000",
        "mole_fraction_<methanol>": "1",
        "mass_density_kg_m3": "748.83"
      },
      {
        "BLKpoint_id": "BLKpoint_46",
        "temperature_k": "373.2",
        "pressure_kpa": "40000",
        "mole_fraction_<methanol>": "0.1",
        "mass_density_kg_m3": "943.52"
      },
      {
        "BLKpoint_id": "BLKpoint_50",
        "temperature_k": "373.2",
        "pressure_kpa": "40000",
        "mole_fraction_<methanol>": "0.6",
        "mass_density_kg_m3": "823.64"
      },
      {
        "BLKpoint_id": "BLKpoint_52",
        "temperature_k": "373.2",
        "pressure_kpa": "40000",
        "mole_fraction_<methanol>": "1",
        "mass_density_kg_m3": "758.66"
      },
      {
        "BLKpoint_id": "BLKpoint_53",
        "temperature_k": "476.2",
        "pressure_kpa": "10000",
        "mole_fraction_<methanol>": "0.1",
        "mass_density_kg_m3": "822.65"
      },
      {
        "BLKpoint_id": "BLKpoint_56",
        "temperature_k": "476.2",
        "pressure_kpa": "10000",
        "mole_fraction_<methanol>": "0.4",
        "mass_density_kg_m3": "714.67"
      },
      {
        "BLKpoint_id": "BLKpoint_59",
        "temperature_k": "476.2",
        "pressure_kpa": "10000",
        "mole_fraction_<methanol>": "1",
        "mass_density_kg_m3": "576.84"
      },
      {
        "BLKpoint_id": "BLKpoint_60",
        "temperature_k": "476.2",
        "pressure_kpa": "20000",
        "mole_fraction_<methanol>": "0.1",
        "mass_density_kg_m3": "831.4"
      },
      {
        "BLKpoint_id": "BLKpoint_63",
        "temperature_k": "476.2",
        "pressure_kpa": "20000",
        "mole_fraction_<methanol>": "0.4",
        "mass_density_kg_m3": "730.97"
      },
      {
        "BLKpoint_id": "BLKpoint_66",
        "temperature_k": "476.2",
        "pressure_kpa": "20000",
        "mole_fraction_<methanol>": "1",
        "mass_density_kg_m3": "612.56"
      },
      {
        "BLKpoint_id": "BLKpoint_67",
        "temperature_k": "476.2",
        "pressure_kpa": "30000",
        "mole_fraction_<methanol>": "0.1",
        "mass_density_kg_m3": "838.61"
      },
      {
        "BLKpoint_id": "BLKpoint_70",
        "temperature_k": "476.2",
        "pressure_kpa": "30000",
        "mole_fraction_<methanol>": "0.4",
        "mass_density_kg_m3": "744.11"
      },
      {
        "BLKpoint_id": "BLKpoint_73",
        "temperature_k": "476.2",
        "pressure_kpa": "30000",
        "mole_fraction_<methanol>": "1",
        "mass_density_kg_m3": "636.82"
      },
      {
        "BLKpoint_id": "BLKpoint_74",
        "temperature_k": "476.2",
        "pressure_kpa": "40000",
        "mole_fraction_<methanol>": "0.1",
        "mass_density_kg_m3": "845.82"
      },
      {
        "BLKpoint_id": "BLKpoint_77",
        "temperature_k": "476.2",
        "pressure_kpa": "40000",
        "mole_fraction_<methanol>": "0.4",
        "mass_density_kg_m3": "754.89"
      },
      {
        "BLKpoint_id": "BLKpoint_80",
        "temperature_k": "476.2",
        "pressure_kpa": "40000",
        "mole_fraction_<methanol>": "1",
        "mass_density_kg_m3": "655.67"
      }
    ],
    "inspection_id": "INSP_da246e84fdf8",
    "lit_num_id": "GLOBlit_1742"
  },
  {
    "doi": "10.1016/j.fluid.2014.05.032",
    "block_number": "PROPblock_1",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "pressure_kpa",
      "temperature_k",
      "mole_fraction_<ethanol>",
      "mass_density_kg_m3"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "pressure_kpa": "39170",
        "temperature_k": "297.05",
        "mole_fraction_<ethanol>": "0.0163",
        "mass_density_kg_m3": "1006.1"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "pressure_kpa": "30810",
        "temperature_k": "297.05",
        "mole_fraction_<ethanol>": "0.0163",
        "mass_density_kg_m3": "1003.2"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "pressure_kpa": "21070",
        "temperature_k": "297.05",
        "mole_fraction_<ethanol>": "0.0163",
        "mass_density_kg_m3": "997.5"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "pressure_kpa": "11280",
        "temperature_k": "297.05",
        "mole_fraction_<ethanol>": "0.0163",
        "mass_density_kg_m3": "993.5"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "pressure_kpa": "2490",
        "temperature_k": "297.05",
        "mole_fraction_<ethanol>": "0.0163",
        "mass_density_kg_m3": "990.8"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "pressure_kpa": "38480",
        "temperature_k": "323.15",
        "mole_fraction_<ethanol>": "0.0163",
        "mass_density_kg_m3": "995.2"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "pressure_kpa": "30890",
        "temperature_k": "323.15",
        "mole_fraction_<ethanol>": "0.0163",
        "mass_density_kg_m3": "992.3"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "pressure_kpa": "21080",
        "temperature_k": "323.15",
        "mole_fraction_<ethanol>": "0.0163",
        "mass_density_kg_m3": "988.4"
      },
      {
        "BLKpoint_id": "BLKpoint_9",
        "pressure_kpa": "11390",
        "temperature_k": "323.15",
        "mole_fraction_<ethanol>": "0.0163",
        "mass_density_kg_m3": "984.4"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "pressure_kpa": "2570",
        "temperature_k": "323.15",
        "mole_fraction_<ethanol>": "0.0163",
        "mass_density_kg_m3": "980.6"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "pressure_kpa": "39910",
        "temperature_k": "348.15",
        "mole_fraction_<ethanol>": "0.0163",
        "mass_density_kg_m3": "982.3"
      },
      {
        "BLKpoint_id": "BLKpoint_12",
        "pressure_kpa": "29500",
        "temperature_k": "348.15",
        "mole_fraction_<ethanol>": "0.0163",
        "mass_density_kg_m3": "978.3"
      },
      {
        "BLKpoint_id": "BLKpoint_13",
        "pressure_kpa": "20750",
        "temperature_k": "348.15",
        "mole_fraction_<ethanol>": "0.0163",
        "mass_density_kg_m3": "974.7"
      },
      {
        "BLKpoint_id": "BLKpoint_14",
        "pressure_kpa": "10980",
        "temperature_k": "348.15",
        "mole_fraction_<ethanol>": "0.0163",
        "mass_density_kg_m3": "970.6"
      },
      {
        "BLKpoint_id": "BLKpoint_15",
        "pressure_kpa": "3220",
        "temperature_k": "348.15",
        "mole_fraction_<ethanol>": "0.0163",
        "mass_density_kg_m3": "967.1"
      },
      {
        "BLKpoint_id": "BLKpoint_16",
        "pressure_kpa": "35700",
        "temperature_k": "373.15",
        "mole_fraction_<ethanol>": "0.0163",
        "mass_density_kg_m3": "964.6"
      },
      {
        "BLKpoint_id": "BLKpoint_17",
        "pressure_kpa": "30600",
        "temperature_k": "373.15",
        "mole_fraction_<ethanol>": "0.0163",
        "mass_density_kg_m3": "962.5"
      },
      {
        "BLKpoint_id": "BLKpoint_18",
        "pressure_kpa": "21160",
        "temperature_k": "373.15",
        "mole_fraction_<ethanol>": "0.0163",
        "mass_density_kg_m3": "958.3"
      },
      {
        "BLKpoint_id": "BLKpoint_19",
        "pressure_kpa": "11320",
        "temperature_k": "373.15",
        "mole_fraction_<ethanol>": "0.0163",
        "mass_density_kg_m3": "953.8"
      },
      {
        "BLKpoint_id": "BLKpoint_20",
        "pressure_kpa": "3370",
        "temperature_k": "373.15",
        "mole_fraction_<ethanol>": "0.0163",
        "mass_density_kg_m3": "950.2"
      },
      {
        "BLKpoint_id": "BLKpoint_21",
        "pressure_kpa": "39890",
        "temperature_k": "398.15",
        "mole_fraction_<ethanol>": "0.0163",
        "mass_density_kg_m3": "948"
      },
      {
        "BLKpoint_id": "BLKpoint_22",
        "pressure_kpa": "30790",
        "temperature_k": "398.15",
        "mole_fraction_<ethanol>": "0.0163",
        "mass_density_kg_m3": "943.7"
      },
      {
        "BLKpoint_id": "BLKpoint_23",
        "pressure_kpa": "21360",
        "temperature_k": "398.15",
        "mole_fraction_<ethanol>": "0.0163",
        "mass_density_kg_m3": "939.3"
      },
      {
        "BLKpoint_id": "BLKpoint_24",
        "pressure_kpa": "11630",
        "temperature_k": "398.15",
        "mole_fraction_<ethanol>": "0.0163",
        "mass_density_kg_m3": "934.4"
      },
      {
        "BLKpoint_id": "BLKpoint_25",
        "pressure_kpa": "3710",
        "temperature_k": "398.15",
        "mole_fraction_<ethanol>": "0.0163",
        "mass_density_kg_m3": "930.3"
      },
      {
        "BLKpoint_id": "BLKpoint_26",
        "pressure_kpa": "39560",
        "temperature_k": "423.15",
        "mole_fraction_<ethanol>": "0.0163",
        "mass_density_kg_m3": "927.2"
      },
      {
        "BLKpoint_id": "BLKpoint_27",
        "pressure_kpa": "30570",
        "temperature_k": "423.15",
        "mole_fraction_<ethanol>": "0.0163",
        "mass_density_kg_m3": "922.4"
      },
      {
        "BLKpoint_id": "BLKpoint_28",
        "pressure_kpa": "20970",
        "temperature_k": "423.15",
        "mole_fraction_<ethanol>": "0.0163",
        "mass_density_kg_m3": "917"
      },
      {
        "BLKpoint_id": "BLKpoint_29",
        "pressure_kpa": "10170",
        "temperature_k": "423.15",
        "mole_fraction_<ethanol>": "0.0163",
        "mass_density_kg_m3": "911"
      },
      {
        "BLKpoint_id": "BLKpoint_30",
        "pressure_kpa": "2680",
        "temperature_k": "423.15",
        "mole_fraction_<ethanol>": "0.0163",
        "mass_density_kg_m3": "906.7"
      },
      {
        "BLKpoint_id": "BLKpoint_31",
        "pressure_kpa": "38340",
        "temperature_k": "448.15",
        "mole_fraction_<ethanol>": "0.0163",
        "mass_density_kg_m3": "903.5"
      },
      {
        "BLKpoint_id": "BLKpoint_32",
        "pressure_kpa": "31050",
        "temperature_k": "448.15",
        "mole_fraction_<ethanol>": "0.0163",
        "mass_density_kg_m3": "899.4"
      },
      {
        "BLKpoint_id": "BLKpoint_33",
        "pressure_kpa": "21530",
        "temperature_k": "448.15",
        "mole_fraction_<ethanol>": "0.0163",
        "mass_density_kg_m3": "893.7"
      },
      {
        "BLKpoint_id": "BLKpoint_34",
        "pressure_kpa": "11920",
        "temperature_k": "448.15",
        "mole_fraction_<ethanol>": "0.0163",
        "mass_density_kg_m3": "887.5"
      },
      {
        "BLKpoint_id": "BLKpoint_35",
        "pressure_kpa": "3960",
        "temperature_k": "448.15",
        "mole_fraction_<ethanol>": "0.0163",
        "mass_density_kg_m3": "882.3"
      },
      {
        "BLKpoint_id": "BLKpoint_36",
        "pressure_kpa": "39230",
        "temperature_k": "292.95",
        "mole_fraction_<ethanol>": "0.073",
        "mass_density_kg_m3": "988"
      },
      {
        "BLKpoint_id": "BLKpoint_37",
        "pressure_kpa": "30930",
        "temperature_k": "292.95",
        "mole_fraction_<ethanol>": "0.073",
        "mass_density_kg_m3": "985"
      },
      {
        "BLKpoint_id": "BLKpoint_38",
        "pressure_kpa": "21120",
        "temperature_k": "292.95",
        "mole_fraction_<ethanol>": "0.073",
        "mass_density_kg_m3": "981.2"
      },
      {
        "BLKpoint_id": "BLKpoint_39",
        "pressure_kpa": "11320",
        "temperature_k": "292.95",
        "mole_fraction_<ethanol>": "0.073",
        "mass_density_kg_m3": "977.6"
      },
      {
        "BLKpoint_id": "BLKpoint_40",
        "pressure_kpa": "2450",
        "temperature_k": "292.95",
        "mole_fraction_<ethanol>": "0.073",
        "mass_density_kg_m3": "974.2"
      },
      {
        "BLKpoint_id": "BLKpoint_41",
        "pressure_kpa": "38600",
        "temperature_k": "323.15",
        "mole_fraction_<ethanol>": "0.073",
        "mass_density_kg_m3": "973.6"
      },
      {
        "BLKpoint_id": "BLKpoint_42",
        "pressure_kpa": "30360",
        "temperature_k": "323.15",
        "mole_fraction_<ethanol>": "0.073",
        "mass_density_kg_m3": "970.6"
      },
      {
        "BLKpoint_id": "BLKpoint_43",
        "pressure_kpa": "20790",
        "temperature_k": "323.15",
        "mole_fraction_<ethanol>": "0.073",
        "mass_density_kg_m3": "966.7"
      },
      {
        "BLKpoint_id": "BLKpoint_44",
        "pressure_kpa": "10940",
        "temperature_k": "323.15",
        "mole_fraction_<ethanol>": "0.073",
        "mass_density_kg_m3": "962.8"
      },
      {
        "BLKpoint_id": "BLKpoint_45",
        "pressure_kpa": "2610",
        "temperature_k": "323.15",
        "mole_fraction_<ethanol>": "0.073",
        "mass_density_kg_m3": "959.3"
      },
      {
        "BLKpoint_id": "BLKpoint_46",
        "pressure_kpa": "39600",
        "temperature_k": "348.15",
        "mole_fraction_<ethanol>": "0.073",
        "mass_density_kg_m3": "958.9"
      },
      {
        "BLKpoint_id": "BLKpoint_48",
        "pressure_kpa": "20870",
        "temperature_k": "348.15",
        "mole_fraction_<ethanol>": "0.073",
        "mass_density_kg_m3": "950.8"
      },
      {
        "BLKpoint_id": "BLKpoint_49",
        "pressure_kpa": "11060",
        "temperature_k": "348.15",
        "mole_fraction_<ethanol>": "0.073",
        "mass_density_kg_m3": "946.6"
      },
      {
        "BLKpoint_id": "BLKpoint_50",
        "pressure_kpa": "3330",
        "temperature_k": "348.15",
        "mole_fraction_<ethanol>": "0.073",
        "mass_density_kg_m3": "943"
      },
      {
        "BLKpoint_id": "BLKpoint_51",
        "pressure_kpa": "37230",
        "temperature_k": "373.15",
        "mole_fraction_<ethanol>": "0.073",
        "mass_density_kg_m3": "939.9"
      },
      {
        "BLKpoint_id": "BLKpoint_52",
        "pressure_kpa": "30670",
        "temperature_k": "373.15",
        "mole_fraction_<ethanol>": "0.073",
        "mass_density_kg_m3": "937"
      },
      {
        "BLKpoint_id": "BLKpoint_53",
        "pressure_kpa": "21080",
        "temperature_k": "373.15",
        "mole_fraction_<ethanol>": "0.073",
        "mass_density_kg_m3": "932.5"
      },
      {
        "BLKpoint_id": "BLKpoint_54",
        "pressure_kpa": "11320",
        "temperature_k": "373.15",
        "mole_fraction_<ethanol>": "0.073",
        "mass_density_kg_m3": "927.7"
      },
      {
        "BLKpoint_id": "BLKpoint_55",
        "pressure_kpa": "3510",
        "temperature_k": "373.15",
        "mole_fraction_<ethanol>": "0.073",
        "mass_density_kg_m3": "923.9"
      },
      {
        "BLKpoint_id": "BLKpoint_56",
        "pressure_kpa": "39500",
        "temperature_k": "398.15",
        "mole_fraction_<ethanol>": "0.073",
        "mass_density_kg_m3": "920.7"
      },
      {
        "BLKpoint_id": "BLKpoint_57",
        "pressure_kpa": "30790",
        "temperature_k": "398.15",
        "mole_fraction_<ethanol>": "0.073",
        "mass_density_kg_m3": "916.3"
      },
      {
        "BLKpoint_id": "BLKpoint_58",
        "pressure_kpa": "21160",
        "temperature_k": "398.15",
        "mole_fraction_<ethanol>": "0.073",
        "mass_density_kg_m3": "911.4"
      },
      {
        "BLKpoint_id": "BLKpoint_59",
        "pressure_kpa": "11510",
        "temperature_k": "398.15",
        "mole_fraction_<ethanol>": "0.073",
        "mass_density_kg_m3": "906.2"
      },
      {
        "BLKpoint_id": "BLKpoint_60",
        "pressure_kpa": "3710",
        "temperature_k": "398.15",
        "mole_fraction_<ethanol>": "0.073",
        "mass_density_kg_m3": "901.9"
      },
      {
        "BLKpoint_id": "BLKpoint_61",
        "pressure_kpa": "40110",
        "temperature_k": "423.15",
        "mole_fraction_<ethanol>": "0.073",
        "mass_density_kg_m3": "898.6"
      },
      {
        "BLKpoint_id": "BLKpoint_62",
        "pressure_kpa": "30490",
        "temperature_k": "423.15",
        "mole_fraction_<ethanol>": "0.073",
        "mass_density_kg_m3": "893"
      },
      {
        "BLKpoint_id": "BLKpoint_63",
        "pressure_kpa": "20110",
        "temperature_k": "423.15",
        "mole_fraction_<ethanol>": "0.073",
        "mass_density_kg_m3": "887.1"
      },
      {
        "BLKpoint_id": "BLKpoint_64",
        "pressure_kpa": "10710",
        "temperature_k": "423.15",
        "mole_fraction_<ethanol>": "0.073",
        "mass_density_kg_m3": "881.1"
      },
      {
        "BLKpoint_id": "BLKpoint_65",
        "pressure_kpa": "2760",
        "temperature_k": "423.15",
        "mole_fraction_<ethanol>": "0.073",
        "mass_density_kg_m3": "875.9"
      },
      {
        "BLKpoint_id": "BLKpoint_66",
        "pressure_kpa": "37210",
        "temperature_k": "448.15",
        "mole_fraction_<ethanol>": "0.073",
        "mass_density_kg_m3": "873"
      },
      {
        "BLKpoint_id": "BLKpoint_67",
        "pressure_kpa": "31170",
        "temperature_k": "448.15",
        "mole_fraction_<ethanol>": "0.073",
        "mass_density_kg_m3": "869.2"
      },
      {
        "BLKpoint_id": "BLKpoint_68",
        "pressure_kpa": "21690",
        "temperature_k": "448.15",
        "mole_fraction_<ethanol>": "0.073",
        "mass_density_kg_m3": "862.7"
      },
      {
        "BLKpoint_id": "BLKpoint_69",
        "pressure_kpa": "12160",
        "temperature_k": "448.15",
        "mole_fraction_<ethanol>": "0.073",
        "mass_density_kg_m3": "855.6"
      },
      {
        "BLKpoint_id": "BLKpoint_70",
        "pressure_kpa": "4000",
        "temperature_k": "448.15",
        "mole_fraction_<ethanol>": "0.073",
        "mass_density_kg_m3": "849.3"
      },
      {
        "BLKpoint_id": "BLKpoint_71",
        "pressure_kpa": "40030",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.0946",
        "mass_density_kg_m3": "979.8"
      },
      {
        "BLKpoint_id": "BLKpoint_72",
        "pressure_kpa": "29980",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.0946",
        "mass_density_kg_m3": "976.1"
      },
      {
        "BLKpoint_id": "BLKpoint_73",
        "pressure_kpa": "20060",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.0946",
        "mass_density_kg_m3": "972.4"
      },
      {
        "BLKpoint_id": "BLKpoint_74",
        "pressure_kpa": "10120",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.0946",
        "mass_density_kg_m3": "968.6"
      },
      {
        "BLKpoint_id": "BLKpoint_75",
        "pressure_kpa": "2560",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.0946",
        "mass_density_kg_m3": "965.8"
      },
      {
        "BLKpoint_id": "BLKpoint_76",
        "pressure_kpa": "39810",
        "temperature_k": "323.15",
        "mole_fraction_<ethanol>": "0.0946",
        "mass_density_kg_m3": "966.2"
      },
      {
        "BLKpoint_id": "BLKpoint_77",
        "pressure_kpa": "32400",
        "temperature_k": "323.15",
        "mole_fraction_<ethanol>": "0.0946",
        "mass_density_kg_m3": "963.3"
      },
      {
        "BLKpoint_id": "BLKpoint_78",
        "pressure_kpa": "20710",
        "temperature_k": "323.15",
        "mole_fraction_<ethanol>": "0.0946",
        "mass_density_kg_m3": "958.8"
      },
      {
        "BLKpoint_id": "BLKpoint_79",
        "pressure_kpa": "11140",
        "temperature_k": "323.15",
        "mole_fraction_<ethanol>": "0.0946",
        "mass_density_kg_m3": "954.9"
      },
      {
        "BLKpoint_id": "BLKpoint_80",
        "pressure_kpa": "2730",
        "temperature_k": "323.15",
        "mole_fraction_<ethanol>": "0.0946",
        "mass_density_kg_m3": "951.3"
      },
      {
        "BLKpoint_id": "BLKpoint_81",
        "pressure_kpa": "37790",
        "temperature_k": "348.15",
        "mole_fraction_<ethanol>": "0.0946",
        "mass_density_kg_m3": "948.7"
      },
      {
        "BLKpoint_id": "BLKpoint_82",
        "pressure_kpa": "29730",
        "temperature_k": "348.15",
        "mole_fraction_<ethanol>": "0.0946",
        "mass_density_kg_m3": "945.4"
      },
      {
        "BLKpoint_id": "BLKpoint_83",
        "pressure_kpa": "20870",
        "temperature_k": "348.15",
        "mole_fraction_<ethanol>": "0.0946",
        "mass_density_kg_m3": "941.6"
      },
      {
        "BLKpoint_id": "BLKpoint_84",
        "pressure_kpa": "11390",
        "temperature_k": "348.15",
        "mole_fraction_<ethanol>": "0.0946",
        "mass_density_kg_m3": "937.4"
      },
      {
        "BLKpoint_id": "BLKpoint_85",
        "pressure_kpa": "2730",
        "temperature_k": "348.15",
        "mole_fraction_<ethanol>": "0.0946",
        "mass_density_kg_m3": "933.7"
      },
      {
        "BLKpoint_id": "BLKpoint_86",
        "pressure_kpa": "39410",
        "temperature_k": "373.15",
        "mole_fraction_<ethanol>": "0.0946",
        "mass_density_kg_m3": "927.3"
      },
      {
        "BLKpoint_id": "BLKpoint_87",
        "pressure_kpa": "30850",
        "temperature_k": "373.15",
        "mole_fraction_<ethanol>": "0.0946",
        "mass_density_kg_m3": "922.3"
      },
      {
        "BLKpoint_id": "BLKpoint_88",
        "pressure_kpa": "21200",
        "temperature_k": "373.15",
        "mole_fraction_<ethanol>": "0.0946",
        "mass_density_kg_m3": "917.7"
      },
      {
        "BLKpoint_id": "BLKpoint_90",
        "pressure_kpa": "3330",
        "temperature_k": "373.15",
        "mole_fraction_<ethanol>": "0.0946",
        "mass_density_kg_m3": "908.6"
      },
      {
        "BLKpoint_id": "BLKpoint_91",
        "pressure_kpa": "39610",
        "temperature_k": "398.15",
        "mole_fraction_<ethanol>": "0.0946",
        "mass_density_kg_m3": "905.3"
      },
      {
        "BLKpoint_id": "BLKpoint_92",
        "pressure_kpa": "30850",
        "temperature_k": "398.15",
        "mole_fraction_<ethanol>": "0.0946",
        "mass_density_kg_m3": "901.1"
      },
      {
        "BLKpoint_id": "BLKpoint_93",
        "pressure_kpa": "21200",
        "temperature_k": "398.15",
        "mole_fraction_<ethanol>": "0.0946",
        "mass_density_kg_m3": "896"
      },
      {
        "BLKpoint_id": "BLKpoint_94",
        "pressure_kpa": "11430",
        "temperature_k": "398.15",
        "mole_fraction_<ethanol>": "0.0946",
        "mass_density_kg_m3": "890.4"
      },
      {
        "BLKpoint_id": "BLKpoint_95",
        "pressure_kpa": "3510",
        "temperature_k": "398.15",
        "mole_fraction_<ethanol>": "0.0946",
        "mass_density_kg_m3": "885.8"
      },
      {
        "BLKpoint_id": "BLKpoint_96",
        "pressure_kpa": "39860",
        "temperature_k": "423.15",
        "mole_fraction_<ethanol>": "0.0946",
        "mass_density_kg_m3": "882.2"
      },
      {
        "BLKpoint_id": "BLKpoint_97",
        "pressure_kpa": "30100",
        "temperature_k": "423.15",
        "mole_fraction_<ethanol>": "0.0946",
        "mass_density_kg_m3": "875.5"
      },
      {
        "BLKpoint_id": "BLKpoint_98",
        "pressure_kpa": "20200",
        "temperature_k": "423.15",
        "mole_fraction_<ethanol>": "0.0946",
        "mass_density_kg_m3": "869.5"
      },
      {
        "BLKpoint_id": "BLKpoint_99",
        "pressure_kpa": "10050",
        "temperature_k": "423.15",
        "mole_fraction_<ethanol>": "0.0946",
        "mass_density_kg_m3": "863.9"
      },
      {
        "BLKpoint_id": "BLKpoint_100",
        "pressure_kpa": "2750",
        "temperature_k": "423.15",
        "mole_fraction_<ethanol>": "0.0946",
        "mass_density_kg_m3": "860.1"
      },
      {
        "BLKpoint_id": "BLKpoint_101",
        "pressure_kpa": "40140",
        "temperature_k": "448.15",
        "mole_fraction_<ethanol>": "0.0946",
        "mass_density_kg_m3": "858.6"
      },
      {
        "BLKpoint_id": "BLKpoint_102",
        "pressure_kpa": "30990",
        "temperature_k": "448.15",
        "mole_fraction_<ethanol>": "0.0946",
        "mass_density_kg_m3": "852.6"
      },
      {
        "BLKpoint_id": "BLKpoint_103",
        "pressure_kpa": "21690",
        "temperature_k": "448.15",
        "mole_fraction_<ethanol>": "0.0946",
        "mass_density_kg_m3": "845.8"
      },
      {
        "BLKpoint_id": "BLKpoint_104",
        "pressure_kpa": "11550",
        "temperature_k": "448.15",
        "mole_fraction_<ethanol>": "0.0946",
        "mass_density_kg_m3": "837.9"
      },
      {
        "BLKpoint_id": "BLKpoint_105",
        "pressure_kpa": "3860",
        "temperature_k": "448.15",
        "mole_fraction_<ethanol>": "0.0946",
        "mass_density_kg_m3": "831.7"
      },
      {
        "BLKpoint_id": "BLKpoint_106",
        "pressure_kpa": "39150",
        "temperature_k": "298.35",
        "mole_fraction_<ethanol>": "0.0343",
        "mass_density_kg_m3": "998.6"
      },
      {
        "BLKpoint_id": "BLKpoint_107",
        "pressure_kpa": "31040",
        "temperature_k": "298.35",
        "mole_fraction_<ethanol>": "0.0343",
        "mass_density_kg_m3": "995.7"
      },
      {
        "BLKpoint_id": "BLKpoint_108",
        "pressure_kpa": "21300",
        "temperature_k": "298.35",
        "mole_fraction_<ethanol>": "0.0343",
        "mass_density_kg_m3": "991.9"
      },
      {
        "BLKpoint_id": "BLKpoint_110",
        "pressure_kpa": "2590",
        "temperature_k": "298.35",
        "mole_fraction_<ethanol>": "0.0343",
        "mass_density_kg_m3": "984.1"
      },
      {
        "BLKpoint_id": "BLKpoint_112",
        "pressure_kpa": "30930",
        "temperature_k": "323.65",
        "mole_fraction_<ethanol>": "0.0343",
        "mass_density_kg_m3": "985.2"
      },
      {
        "BLKpoint_id": "BLKpoint_113",
        "pressure_kpa": "21200",
        "temperature_k": "323.65",
        "mole_fraction_<ethanol>": "0.0343",
        "mass_density_kg_m3": "981.4"
      },
      {
        "BLKpoint_id": "BLKpoint_114",
        "pressure_kpa": "11320",
        "temperature_k": "323.65",
        "mole_fraction_<ethanol>": "0.0343",
        "mass_density_kg_m3": "977.4"
      },
      {
        "BLKpoint_id": "BLKpoint_115",
        "pressure_kpa": "2610",
        "temperature_k": "323.65",
        "mole_fraction_<ethanol>": "0.0343",
        "mass_density_kg_m3": "973.6"
      },
      {
        "BLKpoint_id": "BLKpoint_116",
        "pressure_kpa": "39860",
        "temperature_k": "348.15",
        "mole_fraction_<ethanol>": "0.0343",
        "mass_density_kg_m3": "974.7"
      },
      {
        "BLKpoint_id": "BLKpoint_117",
        "pressure_kpa": "30850",
        "temperature_k": "348.15",
        "mole_fraction_<ethanol>": "0.0343",
        "mass_density_kg_m3": "971.3"
      },
      {
        "BLKpoint_id": "BLKpoint_118",
        "pressure_kpa": "21160",
        "temperature_k": "348.15",
        "mole_fraction_<ethanol>": "0.0343",
        "mass_density_kg_m3": "967.5"
      },
      {
        "BLKpoint_id": "BLKpoint_119",
        "pressure_kpa": "11590",
        "temperature_k": "348.15",
        "mole_fraction_<ethanol>": "0.0343",
        "mass_density_kg_m3": "963.5"
      },
      {
        "BLKpoint_id": "BLKpoint_121",
        "pressure_kpa": "39000",
        "temperature_k": "373.15",
        "mole_fraction_<ethanol>": "0.0343",
        "mass_density_kg_m3": "957.9"
      },
      {
        "BLKpoint_id": "BLKpoint_122",
        "pressure_kpa": "30520",
        "temperature_k": "373.15",
        "mole_fraction_<ethanol>": "0.0343",
        "mass_density_kg_m3": "954.5"
      },
      {
        "BLKpoint_id": "BLKpoint_123",
        "pressure_kpa": "21120",
        "temperature_k": "373.15",
        "mole_fraction_<ethanol>": "0.0343",
        "mass_density_kg_m3": "950.3"
      },
      {
        "BLKpoint_id": "BLKpoint_124",
        "pressure_kpa": "11470",
        "temperature_k": "373.15",
        "mole_fraction_<ethanol>": "0.0343",
        "mass_density_kg_m3": "945.9"
      },
      {
        "BLKpoint_id": "BLKpoint_126",
        "pressure_kpa": "37300",
        "temperature_k": "398.15",
        "mole_fraction_<ethanol>": "0.0343",
        "mass_density_kg_m3": "938.3"
      },
      {
        "BLKpoint_id": "BLKpoint_127",
        "pressure_kpa": "30930",
        "temperature_k": "398.15",
        "mole_fraction_<ethanol>": "0.0343",
        "mass_density_kg_m3": "935.2"
      },
      {
        "BLKpoint_id": "BLKpoint_128",
        "pressure_kpa": "21530",
        "temperature_k": "398.15",
        "mole_fraction_<ethanol>": "0.0343",
        "mass_density_kg_m3": "930.7"
      },
      {
        "BLKpoint_id": "BLKpoint_129",
        "pressure_kpa": "11730",
        "temperature_k": "398.15",
        "mole_fraction_<ethanol>": "0.0343",
        "mass_density_kg_m3": "925.8"
      },
      {
        "BLKpoint_id": "BLKpoint_131",
        "pressure_kpa": "39680",
        "temperature_k": "423.15",
        "mole_fraction_<ethanol>": "0.0343",
        "mass_density_kg_m3": "918.2"
      },
      {
        "BLKpoint_id": "BLKpoint_132",
        "pressure_kpa": "30640",
        "temperature_k": "423.15",
        "mole_fraction_<ethanol>": "0.0343",
        "mass_density_kg_m3": "913.4"
      },
      {
        "BLKpoint_id": "BLKpoint_133",
        "pressure_kpa": "21070",
        "temperature_k": "423.15",
        "mole_fraction_<ethanol>": "0.0343",
        "mass_density_kg_m3": "908.1"
      },
      {
        "BLKpoint_id": "BLKpoint_135",
        "pressure_kpa": "2680",
        "temperature_k": "423.15",
        "mole_fraction_<ethanol>": "0.0343",
        "mass_density_kg_m3": "897.3"
      },
      {
        "BLKpoint_id": "BLKpoint_136",
        "pressure_kpa": "40060",
        "temperature_k": "448.15",
        "mole_fraction_<ethanol>": "0.0343",
        "mass_density_kg_m3": "894.8"
      },
      {
        "BLKpoint_id": "BLKpoint_137",
        "pressure_kpa": "31010",
        "temperature_k": "448.15",
        "mole_fraction_<ethanol>": "0.0343",
        "mass_density_kg_m3": "889.8"
      },
      {
        "BLKpoint_id": "BLKpoint_138",
        "pressure_kpa": "22180",
        "temperature_k": "448.15",
        "mole_fraction_<ethanol>": "0.0343",
        "mass_density_kg_m3": "884.2"
      },
      {
        "BLKpoint_id": "BLKpoint_140",
        "pressure_kpa": "4080",
        "temperature_k": "448.15",
        "mole_fraction_<ethanol>": "0.0343",
        "mass_density_kg_m3": "872.1"
      }
    ],
    "inspection_id": "INSP_51f9b5335a8a",
    "lit_num_id": "GLOBlit_1483"
  },
  {
    "doi": "10.1016/j.jct.2004.07.019",
    "block_number": "PROPblock_1",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "pressure_kpa",
      "molality_mol_kg_<methanol>",
      "mass_density_kg_m3"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "298.16",
        "pressure_kpa": "14450",
        "molality_mol_kg_<methanol>": "0.10243",
        "mass_density_kg_m3": "-0.6308"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "temperature_k": "298.16",
        "pressure_kpa": "14450",
        "molality_mol_kg_<methanol>": "0.98932",
        "mass_density_kg_m3": "-5.7028"
      },
      {
        "BLKpoint_id": "BLKpoint_12",
        "temperature_k": "298.16",
        "pressure_kpa": "29990",
        "molality_mol_kg_<methanol>": "0.98931",
        "mass_density_kg_m3": "-5.7779"
      },
      {
        "BLKpoint_id": "BLKpoint_31",
        "temperature_k": "298.16",
        "pressure_kpa": "29990",
        "molality_mol_kg_<methanol>": "0.10243",
        "mass_density_kg_m3": "-0.6295"
      },
      {
        "BLKpoint_id": "BLKpoint_47",
        "temperature_k": "298.24",
        "pressure_kpa": "400",
        "molality_mol_kg_<methanol>": "0.98932",
        "mass_density_kg_m3": "-5.6141"
      },
      {
        "BLKpoint_id": "BLKpoint_57",
        "temperature_k": "298.24",
        "pressure_kpa": "400",
        "molality_mol_kg_<methanol>": "0.07706",
        "mass_density_kg_m3": "-0.4632"
      },
      {
        "BLKpoint_id": "BLKpoint_77",
        "temperature_k": "318.14",
        "pressure_kpa": "390",
        "molality_mol_kg_<methanol>": "0.71144",
        "mass_density_kg_m3": "-4.175"
      },
      {
        "BLKpoint_id": "BLKpoint_82",
        "temperature_k": "318.14",
        "pressure_kpa": "15370",
        "molality_mol_kg_<methanol>": "0.71146",
        "mass_density_kg_m3": "-4.2"
      },
      {
        "BLKpoint_id": "BLKpoint_93",
        "temperature_k": "318.14",
        "pressure_kpa": "390",
        "molality_mol_kg_<methanol>": "0.09689",
        "mass_density_kg_m3": "-0.5893"
      },
      {
        "BLKpoint_id": "BLKpoint_98",
        "temperature_k": "318.14",
        "pressure_kpa": "15370",
        "molality_mol_kg_<methanol>": "0.09689",
        "mass_density_kg_m3": "-0.5958"
      },
      {
        "BLKpoint_id": "BLKpoint_107",
        "temperature_k": "318.15",
        "pressure_kpa": "29980",
        "molality_mol_kg_<methanol>": "0.71149",
        "mass_density_kg_m3": "-4.215"
      },
      {
        "BLKpoint_id": "BLKpoint_113",
        "temperature_k": "318.15",
        "pressure_kpa": "29980",
        "molality_mol_kg_<methanol>": "0.09818",
        "mass_density_kg_m3": "-0.6009"
      },
      {
        "BLKpoint_id": "BLKpoint_123",
        "temperature_k": "338.15",
        "pressure_kpa": "14810",
        "molality_mol_kg_<methanol>": "0.98922",
        "mass_density_kg_m3": "-5.8941"
      },
      {
        "BLKpoint_id": "BLKpoint_130",
        "temperature_k": "338.15",
        "pressure_kpa": "14810",
        "molality_mol_kg_<methanol>": "0.10242",
        "mass_density_kg_m3": "-0.6333"
      },
      {
        "BLKpoint_id": "BLKpoint_141",
        "temperature_k": "338.16",
        "pressure_kpa": "460",
        "molality_mol_kg_<methanol>": "0.98929",
        "mass_density_kg_m3": "-5.9152"
      },
      {
        "BLKpoint_id": "BLKpoint_146",
        "temperature_k": "338.16",
        "pressure_kpa": "30210",
        "molality_mol_kg_<methanol>": "0.71142",
        "mass_density_kg_m3": "-4.2846"
      },
      {
        "BLKpoint_id": "BLKpoint_158",
        "temperature_k": "338.16",
        "pressure_kpa": "460",
        "molality_mol_kg_<methanol>": "0.10243",
        "mass_density_kg_m3": "-0.6372"
      },
      {
        "BLKpoint_id": "BLKpoint_164",
        "temperature_k": "338.16",
        "pressure_kpa": "30210",
        "molality_mol_kg_<methanol>": "0.09688",
        "mass_density_kg_m3": "-0.6051"
      },
      {
        "BLKpoint_id": "BLKpoint_180",
        "temperature_k": "373.17",
        "pressure_kpa": "14890",
        "molality_mol_kg_<methanol>": "0.98915",
        "mass_density_kg_m3": "-6.2575"
      },
      {
        "BLKpoint_id": "BLKpoint_186",
        "temperature_k": "373.17",
        "pressure_kpa": "30120",
        "molality_mol_kg_<methanol>": "1.0111",
        "mass_density_kg_m3": "-6.3192"
      },
      {
        "BLKpoint_id": "BLKpoint_205",
        "temperature_k": "373.17",
        "pressure_kpa": "2090",
        "molality_mol_kg_<methanol>": "0.10241",
        "mass_density_kg_m3": "-0.6788"
      },
      {
        "BLKpoint_id": "BLKpoint_210",
        "temperature_k": "373.17",
        "pressure_kpa": "2090",
        "molality_mol_kg_<methanol>": "0.98918",
        "mass_density_kg_m3": "-6.3363"
      },
      {
        "BLKpoint_id": "BLKpoint_211",
        "temperature_k": "373.17",
        "pressure_kpa": "14890",
        "molality_mol_kg_<methanol>": "0.094",
        "mass_density_kg_m3": "-0.6107"
      },
      {
        "BLKpoint_id": "BLKpoint_217",
        "temperature_k": "373.17",
        "pressure_kpa": "30120",
        "molality_mol_kg_<methanol>": "0.09399",
        "mass_density_kg_m3": "-0.6082"
      },
      {
        "BLKpoint_id": "BLKpoint_234",
        "temperature_k": "408.15",
        "pressure_kpa": "15000",
        "molality_mol_kg_<methanol>": "1.01107",
        "mass_density_kg_m3": "-6.8718"
      },
      {
        "BLKpoint_id": "BLKpoint_240",
        "temperature_k": "408.15",
        "pressure_kpa": "2070",
        "molality_mol_kg_<methanol>": "1.01108",
        "mass_density_kg_m3": "-7.0201"
      },
      {
        "BLKpoint_id": "BLKpoint_247",
        "temperature_k": "408.15",
        "pressure_kpa": "2070",
        "molality_mol_kg_<methanol>": "0.09399",
        "mass_density_kg_m3": "-0.6721"
      },
      {
        "BLKpoint_id": "BLKpoint_252",
        "temperature_k": "408.15",
        "pressure_kpa": "2070",
        "molality_mol_kg_<methanol>": "1.01108",
        "mass_density_kg_m3": "-7.0201"
      },
      {
        "BLKpoint_id": "BLKpoint_253",
        "temperature_k": "408.15",
        "pressure_kpa": "15000",
        "molality_mol_kg_<methanol>": "0.09399",
        "mass_density_kg_m3": "-0.6616"
      },
      {
        "BLKpoint_id": "BLKpoint_271",
        "temperature_k": "408.16",
        "pressure_kpa": "30030",
        "molality_mol_kg_<methanol>": "0.09399",
        "mass_density_kg_m3": "-0.644"
      },
      {
        "BLKpoint_id": "BLKpoint_276",
        "temperature_k": "408.16",
        "pressure_kpa": "30030",
        "molality_mol_kg_<methanol>": "1.01105",
        "mass_density_kg_m3": "-6.7209"
      },
      {
        "BLKpoint_id": "BLKpoint_282",
        "temperature_k": "443.16",
        "pressure_kpa": "30320",
        "molality_mol_kg_<methanol>": "1.01097",
        "mass_density_kg_m3": "-7.1798"
      },
      {
        "BLKpoint_id": "BLKpoint_283",
        "temperature_k": "443.16",
        "pressure_kpa": "30320",
        "molality_mol_kg_<methanol>": "0.09398",
        "mass_density_kg_m3": "-0.6829"
      },
      {
        "BLKpoint_id": "BLKpoint_316",
        "temperature_k": "443.17",
        "pressure_kpa": "2040",
        "molality_mol_kg_<methanol>": "0.09399",
        "mass_density_kg_m3": "-0.7315"
      },
      {
        "BLKpoint_id": "BLKpoint_321",
        "temperature_k": "443.17",
        "pressure_kpa": "2040",
        "molality_mol_kg_<methanol>": "1.01102",
        "mass_density_kg_m3": "-7.6916"
      },
      {
        "BLKpoint_id": "BLKpoint_322",
        "temperature_k": "443.17",
        "pressure_kpa": "14920",
        "molality_mol_kg_<methanol>": "0.09398",
        "mass_density_kg_m3": "-0.7087"
      },
      {
        "BLKpoint_id": "BLKpoint_327",
        "temperature_k": "443.17",
        "pressure_kpa": "14920",
        "molality_mol_kg_<methanol>": "1.01099",
        "mass_density_kg_m3": "-7.4388"
      },
      {
        "BLKpoint_id": "BLKpoint_333",
        "temperature_k": "473.16",
        "pressure_kpa": "2750",
        "molality_mol_kg_<methanol>": "1.01093",
        "mass_density_kg_m3": "-8.3743"
      },
      {
        "BLKpoint_id": "BLKpoint_339",
        "temperature_k": "473.16",
        "pressure_kpa": "15010",
        "molality_mol_kg_<methanol>": "1.0109",
        "mass_density_kg_m3": "-8.0216"
      },
      {
        "BLKpoint_id": "BLKpoint_345",
        "temperature_k": "473.16",
        "pressure_kpa": "30060",
        "molality_mol_kg_<methanol>": "1.01641",
        "mass_density_kg_m3": "-7.7256"
      },
      {
        "BLKpoint_id": "BLKpoint_352",
        "temperature_k": "473.16",
        "pressure_kpa": "15010",
        "molality_mol_kg_<methanol>": "0.10575",
        "mass_density_kg_m3": "-0.8604"
      },
      {
        "BLKpoint_id": "BLKpoint_364",
        "temperature_k": "473.16",
        "pressure_kpa": "2750",
        "molality_mol_kg_<methanol>": "0.09398",
        "mass_density_kg_m3": "-0.7983"
      },
      {
        "BLKpoint_id": "BLKpoint_370",
        "temperature_k": "473.16",
        "pressure_kpa": "15010",
        "molality_mol_kg_<methanol>": "0.10575",
        "mass_density_kg_m3": "-0.8604"
      },
      {
        "BLKpoint_id": "BLKpoint_376",
        "temperature_k": "473.16",
        "pressure_kpa": "30060",
        "molality_mol_kg_<methanol>": "0.10575",
        "mass_density_kg_m3": "-0.8231"
      },
      {
        "BLKpoint_id": "BLKpoint_392",
        "temperature_k": "498.15",
        "pressure_kpa": "15030",
        "molality_mol_kg_<methanol>": "1.01635",
        "mass_density_kg_m3": "-8.6519"
      },
      {
        "BLKpoint_id": "BLKpoint_399",
        "temperature_k": "498.15",
        "pressure_kpa": "30150",
        "molality_mol_kg_<methanol>": "1.01637",
        "mass_density_kg_m3": "-8.1703"
      },
      {
        "BLKpoint_id": "BLKpoint_413",
        "temperature_k": "498.15",
        "pressure_kpa": "30150",
        "molality_mol_kg_<methanol>": "0.10575",
        "mass_density_kg_m3": "-0.8706"
      },
      {
        "BLKpoint_id": "BLKpoint_419",
        "temperature_k": "498.15",
        "pressure_kpa": "3840",
        "molality_mol_kg_<methanol>": "0.10575",
        "mass_density_kg_m3": "-0.9656"
      },
      {
        "BLKpoint_id": "BLKpoint_424",
        "temperature_k": "498.15",
        "pressure_kpa": "3840",
        "molality_mol_kg_<methanol>": "1.0164",
        "mass_density_kg_m3": "-9.112"
      },
      {
        "BLKpoint_id": "BLKpoint_425",
        "temperature_k": "498.15",
        "pressure_kpa": "15030",
        "molality_mol_kg_<methanol>": "0.10574",
        "mass_density_kg_m3": "-0.9218"
      },
      {
        "BLKpoint_id": "BLKpoint_441",
        "temperature_k": "523.14",
        "pressure_kpa": "5880",
        "molality_mol_kg_<methanol>": "1.01632",
        "mass_density_kg_m3": "-9.9531"
      },
      {
        "BLKpoint_id": "BLKpoint_447",
        "temperature_k": "523.14",
        "pressure_kpa": "15600",
        "molality_mol_kg_<methanol>": "1.01629",
        "mass_density_kg_m3": "-9.3473"
      },
      {
        "BLKpoint_id": "BLKpoint_453",
        "temperature_k": "523.14",
        "pressure_kpa": "30090",
        "molality_mol_kg_<methanol>": "1.01627",
        "mass_density_kg_m3": "-8.6936"
      },
      {
        "BLKpoint_id": "BLKpoint_472",
        "temperature_k": "523.14",
        "pressure_kpa": "5880",
        "molality_mol_kg_<methanol>": "0.10574",
        "mass_density_kg_m3": "-1.0594"
      },
      {
        "BLKpoint_id": "BLKpoint_478",
        "temperature_k": "523.14",
        "pressure_kpa": "15600",
        "molality_mol_kg_<methanol>": "0.10574",
        "mass_density_kg_m3": "-0.993"
      },
      {
        "BLKpoint_id": "BLKpoint_484",
        "temperature_k": "523.14",
        "pressure_kpa": "30090",
        "molality_mol_kg_<methanol>": "0.10573",
        "mass_density_kg_m3": "-0.9275"
      },
      {
        "BLKpoint_id": "BLKpoint_495",
        "temperature_k": "548.16",
        "pressure_kpa": "8000",
        "molality_mol_kg_<methanol>": "1.01623",
        "mass_density_kg_m3": "-11.0973"
      },
      {
        "BLKpoint_id": "BLKpoint_501",
        "temperature_k": "548.16",
        "pressure_kpa": "15970",
        "molality_mol_kg_<methanol>": "1.01618",
        "mass_density_kg_m3": "-10.2986"
      },
      {
        "BLKpoint_id": "BLKpoint_507",
        "temperature_k": "548.16",
        "pressure_kpa": "30120",
        "molality_mol_kg_<methanol>": "1.04694",
        "mass_density_kg_m3": "-9.5934"
      },
      {
        "BLKpoint_id": "BLKpoint_526",
        "temperature_k": "548.16",
        "pressure_kpa": "8000",
        "molality_mol_kg_<methanol>": "0.09819",
        "mass_density_kg_m3": "-1.0956"
      },
      {
        "BLKpoint_id": "BLKpoint_532",
        "temperature_k": "548.16",
        "pressure_kpa": "15970",
        "molality_mol_kg_<methanol>": "0.09819",
        "mass_density_kg_m3": "-1.0204"
      },
      {
        "BLKpoint_id": "BLKpoint_537",
        "temperature_k": "548.16",
        "pressure_kpa": "30120",
        "molality_mol_kg_<methanol>": "0.09819",
        "mass_density_kg_m3": "-0.9253"
      },
      {
        "BLKpoint_id": "BLKpoint_548",
        "temperature_k": "573.15",
        "pressure_kpa": "10140",
        "molality_mol_kg_<methanol>": "1.04693",
        "mass_density_kg_m3": "-13.3065"
      },
      {
        "BLKpoint_id": "BLKpoint_554",
        "temperature_k": "573.15",
        "pressure_kpa": "17990",
        "molality_mol_kg_<methanol>": "1.0469",
        "mass_density_kg_m3": "-11.8248"
      },
      {
        "BLKpoint_id": "BLKpoint_567",
        "temperature_k": "573.15",
        "pressure_kpa": "17990",
        "molality_mol_kg_<methanol>": "0.09818",
        "mass_density_kg_m3": "-1.1328"
      },
      {
        "BLKpoint_id": "BLKpoint_579",
        "temperature_k": "573.15",
        "pressure_kpa": "10140",
        "molality_mol_kg_<methanol>": "0.09819",
        "mass_density_kg_m3": "-1.2695"
      },
      {
        "BLKpoint_id": "BLKpoint_585",
        "temperature_k": "573.15",
        "pressure_kpa": "17990",
        "molality_mol_kg_<methanol>": "0.09818",
        "mass_density_kg_m3": "-1.1328"
      },
      {
        "BLKpoint_id": "BLKpoint_591",
        "temperature_k": "573.15",
        "pressure_kpa": "30110",
        "molality_mol_kg_<methanol>": "0.09818",
        "mass_density_kg_m3": "-1.0044"
      },
      {
        "BLKpoint_id": "BLKpoint_596",
        "temperature_k": "573.15",
        "pressure_kpa": "30110",
        "molality_mol_kg_<methanol>": "1.04688",
        "mass_density_kg_m3": "-10.4212"
      }
    ],
    "inspection_id": "INSP_1dc375d4da8a",
    "lit_num_id": "GLOBlit_2432"
  },
  {
    "doi": "10.1016/j.fluid.2004.11.019",
    "block_number": "PROPblock_1",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "pressure_kpa",
      "mass_density_kg_m3"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "298.15",
        "pressure_kpa": "100",
        "mass_density_kg_m3": "785.7"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "temperature_k": "298.15",
        "pressure_kpa": "20000",
        "mass_density_kg_m3": "801.9"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "temperature_k": "298.15",
        "pressure_kpa": "40000",
        "mass_density_kg_m3": "815.7"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "temperature_k": "323.15",
        "pressure_kpa": "100",
        "mass_density_kg_m3": "763.7"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "temperature_k": "323.15",
        "pressure_kpa": "10000",
        "mass_density_kg_m3": "773.4"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "temperature_k": "323.15",
        "pressure_kpa": "20000",
        "mass_density_kg_m3": "782.3"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "temperature_k": "323.15",
        "pressure_kpa": "40000",
        "mass_density_kg_m3": "797.7"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "temperature_k": "348.15",
        "pressure_kpa": "100",
        "mass_density_kg_m3": "739.4"
      },
      {
        "BLKpoint_id": "BLKpoint_12",
        "temperature_k": "348.15",
        "pressure_kpa": "10000",
        "mass_density_kg_m3": "751.2"
      },
      {
        "BLKpoint_id": "BLKpoint_13",
        "temperature_k": "348.15",
        "pressure_kpa": "20000",
        "mass_density_kg_m3": "761.2"
      },
      {
        "BLKpoint_id": "BLKpoint_14",
        "temperature_k": "348.15",
        "pressure_kpa": "30000",
        "mass_density_kg_m3": "770.3"
      },
      {
        "BLKpoint_id": "BLKpoint_15",
        "temperature_k": "348.15",
        "pressure_kpa": "40000",
        "mass_density_kg_m3": "778.6"
      }
    ],
    "inspection_id": "INSP_c620a1344d0d",
    "lit_num_id": "GLOBlit_220"
  },
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
        "BLKpoint_id": "BLKpoint_43",
        "temperature_k": "298.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.4501",
        "mass_density_kg_m3": "868.8"
      },
      {
        "BLKpoint_id": "BLKpoint_48",
        "temperature_k": "298.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.6967",
        "mass_density_kg_m3": "825.2"
      },
      {
        "BLKpoint_id": "BLKpoint_54",
        "temperature_k": "298.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "1",
        "mass_density_kg_m3": "785.7"
      },
      {
        "BLKpoint_id": "BLKpoint_55",
        "temperature_k": "298.15",
        "pressure_kpa": "10000",
        "mole_fraction_<ethanol>": "0.003",
        "mass_density_kg_m3": "999.8"
      },
      {
        "BLKpoint_id": "BLKpoint_97",
        "temperature_k": "298.15",
        "pressure_kpa": "10000",
        "mole_fraction_<ethanol>": "0.4501",
        "mass_density_kg_m3": "874.7"
      },
      {
        "BLKpoint_id": "BLKpoint_102",
        "temperature_k": "298.15",
        "pressure_kpa": "10000",
        "mole_fraction_<ethanol>": "0.6967",
        "mass_density_kg_m3": "832.3"
      },
      {
        "BLKpoint_id": "BLKpoint_108",
        "temperature_k": "298.15",
        "pressure_kpa": "10000",
        "mole_fraction_<ethanol>": "1",
        "mass_density_kg_m3": "794"
      },
      {
        "BLKpoint_id": "BLKpoint_109",
        "temperature_k": "298.15",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0.003",
        "mass_density_kg_m3": "1004.2"
      },
      {
        "BLKpoint_id": "BLKpoint_151",
        "temperature_k": "298.15",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0.4501",
        "mass_density_kg_m3": "880.4"
      },
      {
        "BLKpoint_id": "BLKpoint_156",
        "temperature_k": "298.15",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0.6967",
        "mass_density_kg_m3": "839"
      },
      {
        "BLKpoint_id": "BLKpoint_162",
        "temperature_k": "298.15",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "1",
        "mass_density_kg_m3": "801.9"
      },
      {
        "BLKpoint_id": "BLKpoint_163",
        "temperature_k": "298.15",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0.003",
        "mass_density_kg_m3": "1008.5"
      },
      {
        "BLKpoint_id": "BLKpoint_199",
        "temperature_k": "298.15",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0.2269",
        "mass_density_kg_m3": "938.7"
      },
      {
        "BLKpoint_id": "BLKpoint_205",
        "temperature_k": "298.15",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0.4501",
        "mass_density_kg_m3": "885.7"
      },
      {
        "BLKpoint_id": "BLKpoint_210",
        "temperature_k": "298.15",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0.6967",
        "mass_density_kg_m3": "845.1"
      },
      {
        "BLKpoint_id": "BLKpoint_216",
        "temperature_k": "298.15",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "1",
        "mass_density_kg_m3": "808.9"
      },
      {
        "BLKpoint_id": "BLKpoint_217",
        "temperature_k": "298.15",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0.003",
        "mass_density_kg_m3": "1012.7"
      },
      {
        "BLKpoint_id": "BLKpoint_253",
        "temperature_k": "298.15",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0.2269",
        "mass_density_kg_m3": "942.9"
      },
      {
        "BLKpoint_id": "BLKpoint_259",
        "temperature_k": "298.15",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0.4501",
        "mass_density_kg_m3": "890.8"
      },
      {
        "BLKpoint_id": "BLKpoint_264",
        "temperature_k": "298.15",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0.6967",
        "mass_density_kg_m3": "851"
      },
      {
        "BLKpoint_id": "BLKpoint_270",
        "temperature_k": "298.15",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "1",
        "mass_density_kg_m3": "815.7"
      },
      {
        "BLKpoint_id": "BLKpoint_271",
        "temperature_k": "323.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.003",
        "mass_density_kg_m3": "986.5"
      },
      {
        "BLKpoint_id": "BLKpoint_307",
        "temperature_k": "323.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.2269",
        "mass_density_kg_m3": "905.2"
      },
      {
        "BLKpoint_id": "BLKpoint_313",
        "temperature_k": "323.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.4501",
        "mass_density_kg_m3": "846.7"
      },
      {
        "BLKpoint_id": "BLKpoint_318",
        "temperature_k": "323.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.6967",
        "mass_density_kg_m3": "802.8"
      },
      {
        "BLKpoint_id": "BLKpoint_324",
        "temperature_k": "323.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "1",
        "mass_density_kg_m3": "763.7"
      },
      {
        "BLKpoint_id": "BLKpoint_325",
        "temperature_k": "323.15",
        "pressure_kpa": "10000",
        "mole_fraction_<ethanol>": "0.003",
        "mass_density_kg_m3": "990.8"
      },
      {
        "BLKpoint_id": "BLKpoint_361",
        "temperature_k": "323.15",
        "pressure_kpa": "10000",
        "mole_fraction_<ethanol>": "0.2269",
        "mass_density_kg_m3": "910.3"
      },
      {
        "BLKpoint_id": "BLKpoint_367",
        "temperature_k": "323.15",
        "pressure_kpa": "10000",
        "mole_fraction_<ethanol>": "0.4501",
        "mass_density_kg_m3": "853.3"
      },
      {
        "BLKpoint_id": "BLKpoint_372",
        "temperature_k": "323.15",
        "pressure_kpa": "10000",
        "mole_fraction_<ethanol>": "0.6967",
        "mass_density_kg_m3": "810.9"
      },
      {
        "BLKpoint_id": "BLKpoint_378",
        "temperature_k": "323.15",
        "pressure_kpa": "10000",
        "mole_fraction_<ethanol>": "1",
        "mass_density_kg_m3": "773.4"
      },
      {
        "BLKpoint_id": "BLKpoint_379",
        "temperature_k": "323.15",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0.003",
        "mass_density_kg_m3": "994.9"
      },
      {
        "BLKpoint_id": "BLKpoint_415",
        "temperature_k": "323.15",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0.2269",
        "mass_density_kg_m3": "915.3"
      },
      {
        "BLKpoint_id": "BLKpoint_421",
        "temperature_k": "323.15",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0.4501",
        "mass_density_kg_m3": "859.7"
      },
      {
        "BLKpoint_id": "BLKpoint_426",
        "temperature_k": "323.15",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0.6967",
        "mass_density_kg_m3": "818.4"
      },
      {
        "BLKpoint_id": "BLKpoint_432",
        "temperature_k": "323.15",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "1",
        "mass_density_kg_m3": "782.3"
      },
      {
        "BLKpoint_id": "BLKpoint_433",
        "temperature_k": "323.15",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0.003",
        "mass_density_kg_m3": "999"
      },
      {
        "BLKpoint_id": "BLKpoint_469",
        "temperature_k": "323.15",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0.2269",
        "mass_density_kg_m3": "920.1"
      },
      {
        "BLKpoint_id": "BLKpoint_475",
        "temperature_k": "323.15",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0.4501",
        "mass_density_kg_m3": "865.7"
      },
      {
        "BLKpoint_id": "BLKpoint_480",
        "temperature_k": "323.15",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0.6967",
        "mass_density_kg_m3": "825.4"
      },
      {
        "BLKpoint_id": "BLKpoint_486",
        "temperature_k": "323.15",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "1",
        "mass_density_kg_m3": "790.3"
      },
      {
        "BLKpoint_id": "BLKpoint_487",
        "temperature_k": "323.15",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0.003",
        "mass_density_kg_m3": "1003.1"
      },
      {
        "BLKpoint_id": "BLKpoint_523",
        "temperature_k": "323.15",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0.2269",
        "mass_density_kg_m3": "924.7"
      },
      {
        "BLKpoint_id": "BLKpoint_529",
        "temperature_k": "323.15",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0.4501",
        "mass_density_kg_m3": "871.3"
      },
      {
        "BLKpoint_id": "BLKpoint_534",
        "temperature_k": "323.15",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0.6967",
        "mass_density_kg_m3": "831.9"
      },
      {
        "BLKpoint_id": "BLKpoint_540",
        "temperature_k": "323.15",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "1",
        "mass_density_kg_m3": "797.7"
      },
      {
        "BLKpoint_id": "BLKpoint_541",
        "temperature_k": "348.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.003",
        "mass_density_kg_m3": "973.1"
      },
      {
        "BLKpoint_id": "BLKpoint_575",
        "temperature_k": "348.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.1903",
        "mass_density_kg_m3": "895.8"
      },
      {
        "BLKpoint_id": "BLKpoint_582",
        "temperature_k": "348.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.4034",
        "mass_density_kg_m3": "833.4"
      },
      {
        "BLKpoint_id": "BLKpoint_587",
        "temperature_k": "348.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.6489",
        "mass_density_kg_m3": "785.6"
      },
      {
        "BLKpoint_id": "BLKpoint_594",
        "temperature_k": "348.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "1",
        "mass_density_kg_m3": "739.4"
      },
      {
        "BLKpoint_id": "BLKpoint_595",
        "temperature_k": "348.15",
        "pressure_kpa": "10000",
        "mole_fraction_<ethanol>": "0.003",
        "mass_density_kg_m3": "977.5"
      },
      {
        "BLKpoint_id": "BLKpoint_630",
        "temperature_k": "348.15",
        "pressure_kpa": "10000",
        "mole_fraction_<ethanol>": "0.1996",
        "mass_density_kg_m3": "898.1"
      },
      {
        "BLKpoint_id": "BLKpoint_636",
        "temperature_k": "348.15",
        "pressure_kpa": "10000",
        "mole_fraction_<ethanol>": "0.4034",
        "mass_density_kg_m3": "840.7"
      },
      {
        "BLKpoint_id": "BLKpoint_641",
        "temperature_k": "348.15",
        "pressure_kpa": "10000",
        "mole_fraction_<ethanol>": "0.6489",
        "mass_density_kg_m3": "794.6"
      },
      {
        "BLKpoint_id": "BLKpoint_648",
        "temperature_k": "348.15",
        "pressure_kpa": "10000",
        "mole_fraction_<ethanol>": "1",
        "mass_density_kg_m3": "751.2"
      },
      {
        "BLKpoint_id": "BLKpoint_649",
        "temperature_k": "348.15",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0.003",
        "mass_density_kg_m3": "981.9"
      },
      {
        "BLKpoint_id": "BLKpoint_683",
        "temperature_k": "348.15",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0.1903",
        "mass_density_kg_m3": "906.5"
      },
      {
        "BLKpoint_id": "BLKpoint_690",
        "temperature_k": "348.15",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0.4034",
        "mass_density_kg_m3": "847.5"
      },
      {
        "BLKpoint_id": "BLKpoint_695",
        "temperature_k": "348.15",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "0.6489",
        "mass_density_kg_m3": "802.9"
      },
      {
        "BLKpoint_id": "BLKpoint_702",
        "temperature_k": "348.15",
        "pressure_kpa": "20000",
        "mole_fraction_<ethanol>": "1",
        "mass_density_kg_m3": "761.2"
      },
      {
        "BLKpoint_id": "BLKpoint_703",
        "temperature_k": "348.15",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0.003",
        "mass_density_kg_m3": "986.1"
      },
      {
        "BLKpoint_id": "BLKpoint_738",
        "temperature_k": "348.15",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0.1996",
        "mass_density_kg_m3": "908.5"
      },
      {
        "BLKpoint_id": "BLKpoint_744",
        "temperature_k": "348.15",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0.4034",
        "mass_density_kg_m3": "854"
      },
      {
        "BLKpoint_id": "BLKpoint_749",
        "temperature_k": "348.15",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "0.6489",
        "mass_density_kg_m3": "810.6"
      },
      {
        "BLKpoint_id": "BLKpoint_756",
        "temperature_k": "348.15",
        "pressure_kpa": "30000",
        "mole_fraction_<ethanol>": "1",
        "mass_density_kg_m3": "770.3"
      },
      {
        "BLKpoint_id": "BLKpoint_757",
        "temperature_k": "348.15",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0.003",
        "mass_density_kg_m3": "990.1"
      },
      {
        "BLKpoint_id": "BLKpoint_791",
        "temperature_k": "348.15",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0.1903",
        "mass_density_kg_m3": "916.4"
      },
      {
        "BLKpoint_id": "BLKpoint_798",
        "temperature_k": "348.15",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0.4034",
        "mass_density_kg_m3": "860"
      },
      {
        "BLKpoint_id": "BLKpoint_803",
        "temperature_k": "348.15",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "0.6489",
        "mass_density_kg_m3": "817.8"
      },
      {
        "BLKpoint_id": "BLKpoint_810",
        "temperature_k": "348.15",
        "pressure_kpa": "40000",
        "mole_fraction_<ethanol>": "1",
        "mass_density_kg_m3": "778.6"
      }
    ],
    "inspection_id": "INSP_38392edfd29c",
    "lit_num_id": "GLOBlit_220"
  },
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
        "BLKpoint_id": "BLKpoint_38",
        "temperature_k": "298.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.2502",
        "mass_density_kg_m3": "918.5"
      },
      {
        "BLKpoint_id": "BLKpoint_43",
        "temperature_k": "298.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.4501",
        "mass_density_kg_m3": "868.8"
      },
      {
        "BLKpoint_id": "BLKpoint_48",
        "temperature_k": "298.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.6967",
        "mass_density_kg_m3": "825.2"
      },
      {
        "BLKpoint_id": "BLKpoint_54",
        "temperature_k": "298.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "1",
        "mass_density_kg_m3": "785.7"
      },
      {
        "BLKpoint_id": "BLKpoint_271",
        "temperature_k": "323.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.003",
        "mass_density_kg_m3": "986.5"
      },
      {
        "BLKpoint_id": "BLKpoint_307",
        "temperature_k": "323.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.2269",
        "mass_density_kg_m3": "905.2"
      },
      {
        "BLKpoint_id": "BLKpoint_313",
        "temperature_k": "323.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.4501",
        "mass_density_kg_m3": "846.7"
      },
      {
        "BLKpoint_id": "BLKpoint_318",
        "temperature_k": "323.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.6967",
        "mass_density_kg_m3": "802.8"
      },
      {
        "BLKpoint_id": "BLKpoint_324",
        "temperature_k": "323.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "1",
        "mass_density_kg_m3": "763.7"
      },
      {
        "BLKpoint_id": "BLKpoint_541",
        "temperature_k": "348.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.003",
        "mass_density_kg_m3": "973.1"
      },
      {
        "BLKpoint_id": "BLKpoint_575",
        "temperature_k": "348.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.1903",
        "mass_density_kg_m3": "895.8"
      },
      {
        "BLKpoint_id": "BLKpoint_582",
        "temperature_k": "348.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.4034",
        "mass_density_kg_m3": "833.4"
      },
      {
        "BLKpoint_id": "BLKpoint_587",
        "temperature_k": "348.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "0.6489",
        "mass_density_kg_m3": "785.6"
      },
      {
        "BLKpoint_id": "BLKpoint_594",
        "temperature_k": "348.15",
        "pressure_kpa": "100",
        "mole_fraction_<ethanol>": "1",
        "mass_density_kg_m3": "739.4"
      }
    ],
    "inspection_id": "INSP_13b9dbeeee1e",
    "lit_num_id": "GLOBlit_220"
  },
  {
    "doi": "10.1016/j.jct.2018.02.022",
    "block_number": "PROPblock_19",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<ethanol>",
      "pressure_kpa",
      "mass_density_kg_m3"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "293.15",
        "mole_fraction_<ethanol>": "0.0024",
        "pressure_kpa": "92.3",
        "mass_density_kg_m3": "997.039"
      },
      {
        "BLKpoint_id": "BLKpoint_23",
        "temperature_k": "293.15",
        "mole_fraction_<ethanol>": "0.7006",
        "pressure_kpa": "92.3",
        "mass_density_kg_m3": "829.434"
      },
      {
        "BLKpoint_id": "BLKpoint_59",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.7006",
        "pressure_kpa": "92.3",
        "mass_density_kg_m3": "825.07"
      },
      {
        "BLKpoint_id": "BLKpoint_95",
        "temperature_k": "303.15",
        "mole_fraction_<ethanol>": "0.7006",
        "pressure_kpa": "92.3",
        "mass_density_kg_m3": "820.66"
      },
      {
        "BLKpoint_id": "BLKpoint_131",
        "temperature_k": "308.15",
        "mole_fraction_<ethanol>": "0.7006",
        "pressure_kpa": "92.3",
        "mass_density_kg_m3": "816.2"
      },
      {
        "BLKpoint_id": "BLKpoint_145",
        "temperature_k": "293.15",
        "mole_fraction_<ethanol>": "0",
        "pressure_kpa": "92.3",
        "mass_density_kg_m3": "998.429"
      },
      {
        "BLKpoint_id": "BLKpoint_146",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0",
        "pressure_kpa": "92.3",
        "mass_density_kg_m3": "997.267"
      },
      {
        "BLKpoint_id": "BLKpoint_147",
        "temperature_k": "303.15",
        "mole_fraction_<ethanol>": "0",
        "pressure_kpa": "92.3",
        "mass_density_kg_m3": "995.867"
      },
      {
        "BLKpoint_id": "BLKpoint_148",
        "temperature_k": "308.15",
        "mole_fraction_<ethanol>": "0",
        "pressure_kpa": "92.3",
        "mass_density_kg_m3": "994.252"
      },
      {
        "BLKpoint_id": "BLKpoint_149",
        "temperature_k": "293.15",
        "mole_fraction_<ethanol>": "1",
        "pressure_kpa": "92.3",
        "mass_density_kg_m3": "789.547"
      },
      {
        "BLKpoint_id": "BLKpoint_150",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "1",
        "pressure_kpa": "92.3",
        "mass_density_kg_m3": "785.26"
      },
      {
        "BLKpoint_id": "BLKpoint_151",
        "temperature_k": "303.15",
        "mole_fraction_<ethanol>": "1",
        "pressure_kpa": "92.3",
        "mass_density_kg_m3": "780.941"
      },
      {
        "BLKpoint_id": "BLKpoint_152",
        "temperature_k": "308.15",
        "mole_fraction_<ethanol>": "1",
        "pressure_kpa": "92.3",
        "mass_density_kg_m3": "776.592"
      },
      {
        "BLKpoint_id": "BLKpoint_160",
        "temperature_k": "293.15",
        "mole_fraction_<ethanol>": "0.1984",
        "pressure_kpa": "92.3",
        "mass_density_kg_m3": "935.19"
      },
      {
        "BLKpoint_id": "BLKpoint_165",
        "temperature_k": "293.15",
        "mole_fraction_<ethanol>": "0.4495",
        "pressure_kpa": "92.3",
        "mass_density_kg_m3": "873.57"
      },
      {
        "BLKpoint_id": "BLKpoint_183",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.1984",
        "pressure_kpa": "92.3",
        "mass_density_kg_m3": "931.84"
      },
      {
        "BLKpoint_id": "BLKpoint_188",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.4495",
        "pressure_kpa": "92.3",
        "mass_density_kg_m3": "869.34"
      },
      {
        "BLKpoint_id": "BLKpoint_206",
        "temperature_k": "303.15",
        "mole_fraction_<ethanol>": "0.1984",
        "pressure_kpa": "92.3",
        "mass_density_kg_m3": "928.77"
      },
      {
        "BLKpoint_id": "BLKpoint_211",
        "temperature_k": "303.15",
        "mole_fraction_<ethanol>": "0.4495",
        "pressure_kpa": "92.3",
        "mass_density_kg_m3": "865.03"
      },
      {
        "BLKpoint_id": "BLKpoint_229",
        "temperature_k": "308.15",
        "mole_fraction_<ethanol>": "0.1984",
        "pressure_kpa": "92.3",
        "mass_density_kg_m3": "925.04"
      },
      {
        "BLKpoint_id": "BLKpoint_234",
        "temperature_k": "308.15",
        "mole_fraction_<ethanol>": "0.4495",
        "pressure_kpa": "92.3",
        "mass_density_kg_m3": "860.66"
      },
      {
        "BLKpoint_id": "BLKpoint_244",
        "temperature_k": "308.15",
        "mole_fraction_<ethanol>": "0.929",
        "pressure_kpa": "92.3",
        "mass_density_kg_m3": "785.46"
      }
    ],
    "inspection_id": "INSP_b49f3d6ec58f",
    "lit_num_id": "GLOBlit_5201"
  },
  {
    "doi": "10.1016/j.jct.2007.05.004",
    "block_number": "PROPblock_12",
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
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "293.15",
        "mole_fraction_<water>": "0",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "789.75"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "temperature_k": "293.15",
        "mole_fraction_<water>": "0.4971",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "862.82"
      },
      {
        "BLKpoint_id": "BLKpoint_9",
        "temperature_k": "293.15",
        "mole_fraction_<water>": "0.6991",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "908.69"
      },
      {
        "BLKpoint_id": "BLKpoint_13",
        "temperature_k": "293.15",
        "mole_fraction_<water>": "1",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "998.2"
      },
      {
        "BLKpoint_id": "BLKpoint_14",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "785.46"
      },
      {
        "BLKpoint_id": "BLKpoint_19",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.3991",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "840.94"
      },
      {
        "BLKpoint_id": "BLKpoint_20",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.5989",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "879.89"
      },
      {
        "BLKpoint_id": "BLKpoint_25",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "1",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "997.05"
      },
      {
        "BLKpoint_id": "BLKpoint_26",
        "temperature_k": "303.15",
        "mole_fraction_<water>": "0",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "781.15"
      },
      {
        "BLKpoint_id": "BLKpoint_30",
        "temperature_k": "303.15",
        "mole_fraction_<water>": "0.2961",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "820.29"
      },
      {
        "BLKpoint_id": "BLKpoint_32",
        "temperature_k": "303.15",
        "mole_fraction_<water>": "0.5989",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "875.63"
      },
      {
        "BLKpoint_id": "BLKpoint_37",
        "temperature_k": "303.15",
        "mole_fraction_<water>": "1",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "995.65"
      }
    ],
    "inspection_id": "INSP_1d2031e2c9c2",
    "lit_num_id": "GLOBlit_2825"
  }
]
```

---

## Verdict

**Data Quality**
The agent correctly identified that no 350 K data exist and located the nearest isotherm at 348.15 K from a well-documented source. A `fit_multi_system` call appears in the trace (step 15, returning 1616 chars), confirming fits were not fabricated. However, the fit uses density deviation from linear mixing (Δρ) rather than true excess volume, which is acceptable for a density correlation but should be noted. The composition basis appears to be mole fraction from the source. Pure-component values are taken as block-edge values rather than independent references—reasonable but approximate.

**Fit Quality**
R² = 0.9986 with RK order 5 for 47 points is good, though order 5 with 6 parameters for a deviation function raises mild overfitting concern (BIC selection mitigates this). RMSE of 0.49 kg/m³ is acceptable.

**Scientific Verdict**
The agent's recommendation to withhold the 350 K prediction is scientifically sound—proximity to ethanol's boiling point and non-linear coefficient evolution make extrapolation unreliable. The 348.15 K correlation is well-supported. **PASS.**

---

## Output Files

- **data**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_064353_855503_49473160\data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_fit.csv` — RK fit data — 10.1016/j.fluid.2004.11.019 PROPblock_2_T298.1
- **data**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_064353_855503_49473160\data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T323.1_fit.csv` — RK fit data — 10.1016/j.fluid.2004.11.019 PROPblock_2_T323.1
- **data**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_064353_855503_49473160\data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T348.1_fit.csv` — RK fit data — 10.1016/j.fluid.2004.11.019 PROPblock_2_T348.1
- **data**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_064353_855503_49473160\data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_excess.csv` — Excess property — 10.1016/j.fluid.2004.11.019 PROPblock_2_T298.1
- **data**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_064353_855503_49473160\data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T348.1_excess.csv` — Excess property — 10.1016/j.fluid.2004.11.019 PROPblock_2_T348.1
- **data**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_064353_855503_49473160\data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T323.1_excess.csv` — Excess property — 10.1016/j.fluid.2004.11.019 PROPblock_2_T323.1
- **plot**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_064353_855503_49473160\plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T323.1_fit.png` — RK fit plot — 10.1016/j.fluid.2004.11.019 PROPblock_2_T323.1
- **plot**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_064353_855503_49473160\plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_fit.png` — RK fit plot — 10.1016/j.fluid.2004.11.019 PROPblock_2_T298.1
- **plot**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_064353_855503_49473160\plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T348.1_fit.png` — RK fit plot — 10.1016/j.fluid.2004.11.019 PROPblock_2_T348.1
- **plot**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_064353_855503_49473160\plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T323.1_excess.png` — Excess plot — 10.1016/j.fluid.2004.11.019 PROPblock_2_T323.1
- **plot**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_064353_855503_49473160\plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_excess.png` — Excess plot — 10.1016/j.fluid.2004.11.019 PROPblock_2_T298.1
- **plot**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_064353_855503_49473160\plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T348.1_excess.png` — Excess plot — 10.1016/j.fluid.2004.11.019 PROPblock_2_T348.1