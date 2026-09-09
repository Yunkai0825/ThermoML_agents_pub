# Analysis Run — 20260905_122316 (Round 1)

**Question:** Near 25 °C, at what composition does liquid DMSO + water depart most strongly from ideal mixing, and does the answer change when volume, enthalpy, viscosity, or another measured property is considered?

**Time:** 1095.1s | **Iterations:** 24 | **Tools:** 21

---

## Answer

{
  "answer": "## Where Does Liquid DMSO + Water Depart Most Strongly from Ideal Mixing at 25 °C?\n\nThe answer depends on which property you examine. Using Redlich-Kister (RK) polynomial fits to experimental ThermoML data at 298.15 K, I fitted four measured properties across the full DMSO mole-fraction range and compared the composition of maximum departure from the ideal-mixing baseline for each.\n\n---\n\n### Summary of Results\n\n| Property | Data source (DOI / block) | n pts | RK order | R² | Composition of max |Δᴱ| | Max excess value | Relative departure |\n|---|---|---|---|---|---|---|---|\n| **Excess molar volume Vᴱ** | 10.1016/j.jct.2006.12.012 / PROPblock_4 | 22 | 5 | 0.999909 | x(DMSO) ≈ 0.33 (from predict_from_rk) | −9.57 × 10⁻⁷ m³/mol (from predict_from_rk) | ~2% of V_m (derived ratio) |\n| **Viscosity (Arrhenius excess)** | 10.1016/j.jct.2006.12.012 / PROPblock_3 | 22 | 5 | 0.999497 | **x(DMSO) ≈ 0.35** (from predict_from_rk) | ln-space excess = **+1.17** (from predict_from_rk) | **~320% above Arrhenius ideal** (derived from predict_from_rk: 0.00374/0.00115) |\n| **Surface tension (excess)** | 10.1021/je7001013 / PROPblock_9 | 15 | 5 | 0.985302 | x(DMSO) ≈ 0.15–0.20 (from predict_from_rk) | −0.0093 N/m (from predict_from_rk) | ~16% of γ (derived ratio) |\n| **Refractive index (excess)** | 10.1021/je7001013 / PROPblock_10 | 10 | 3 | 0.999858 | x(DMSO) ≈ 0.30–0.35 (from predict_from_rk) | +0.056 (from predict_from_rk) | ~4% of n_D (derived ratio) |\n| **Excess molar enthalpy (Hᴱ)** | *Not available in ThermoML* | — | — | — | — | — | — |\n\n---\n\n### Property-by-Property Detail\n\n#### 1. Excess Molar Volume (Vᴱ) — via density → molar volume transform (DP2)\n\nDensity data from GLOBlit_2781 (DOI: 10.1016/j.jct.2006.12.012, PROPblock_4, 24 compositions at 298.15 K) were exactly transformed to molar volume V_m = (x₁M₁ + x₂M₂)/ρ and fitted with a 5th-order RK polynomial.\n\n- **Pure endpoints:** V_m(water) = 1.807 × 10⁻⁵ m³/mol; V_m(DMSO) = 7.127 × 10⁻⁵ m³/mol (block-edge values from fit_block_derived)\n- **RK coefficients (Vᴱ):** [−3.581 × 10⁻⁶, 2.067 × 10⁻⁶, −2.931 × 10⁻⁷, −2.412 × 10⁻⁶, 1.618 × 10⁻⁶, 7.992 × 10⁻⁷]\n- **Maximum |Vᴱ|:** −9.57 × 10⁻⁷ m³/mol near x(DMSO) ≈ 0.33 (from predict_from_rk output)\n- R² = 0.999909, RMSE = 2.98 × 10⁻⁹ m³/mol\n\nThe **negative** Vᴱ indicates volume contraction upon mixing — the mixture packs more efficiently than ideal, consistent with strong DMSO–water hydrogen bonding.\n\n#### 2. Viscosity — Arrhenius mixing rule\n\nViscosity data from GLOBlit_2781 (DOI: 10.1016/j.jct.2006.12.012, PROPblock_3, 24 compositions at 298.15 K).\n\n- **Pure endpoints:** η(water) = 0.0008901 Pa·s; η(DMSO) = 0.001996 Pa·s (block-edge values)\n- **RK coefficients (ln η excess):** [3.7056, −3.8597, 2.1830, −0.8182, −1.8031, 2.5483]\n- **Maximum excess:** ln-space excess = +1.17 at x(DMSO) ≈ 0.35, corresponding to a predicted viscosity of ~0.00374 Pa·s versus an Arrhenius ideal of ~0.00115 Pa·s (both from predict_from_rk output). This is consistent with the measured maximum of 0.0037353 Pa·s at x(DMSO) = 0.3638 from the inspected data (GLOBlit_2781, PROPblock_3, BLKpoint_12).\n- R² = 0.999497, RMSE = 0.00882\n\nThis is by far the **largest relative departure** of any measured property. The viscosity maximum at x(DMSO) ≈ 0.33–0.36 is a hallmark of the DMSO–water system, attributed to the formation of strongly hydrogen-bonded DMSO·nH₂O complexes that dramatically enhance intermolecular friction.\n\n#### 3. Surface Tension\n\nSurface tension data from GLOBlit_10766 (DOI: 10.1021/je7001013, PROPblock_9, 15 mixture points at 298.15 K used in the fit).\n\n- **Pure endpoints:** γ(water) = 0.07135 N/m (GLOBlit_725, PROPblock_12); γ(DMSO) = 0.04278 N/m (GLOBlit_3840, PROPblock_1)\n- **RK coefficients (γᴱ):** [−0.03389, −0.00254, −0.03248, 0.08718, −0.00659, −0.08176]\n- **Maximum |γᴱ|:** −0.0093 N/m near x(DMSO) ≈ 0.15–0.20 (from predict_from_rk output)\n- R² = 0.985302, RMSE = 0.000271 N/m\n\nThe **negative** excess surface tension at low DMSO concentrations reflects DMSO's strong preferential adsorption at the air–water interface — even small amounts of DMSO dramatically lower the surface tension below the linear ideal.\n\n#### 4. Refractive Index\n\nRefractive index data from GLOBlit_10766 (DOI: 10.1021/je7001013, PROPblock_10, 11 compositions at 298.15 K).\n\n- **Pure endpoints:** n_D(water) = 1.3325 (GLOBlit_306, PROPblock_5); n_D(DMSO) = 1.4771 (GLOBlit_2957, PROPblock_11)\n- **RK coefficients (n_D excess):** [0.19713, −0.12848, 0.08421, −0.02640]\n- **Maximum |n_Dᴱ|:** +0.056 near x(DMSO) ≈ 0.30–0.35 (from predict_from_rk output)\n- R² = 0.999858, RMSE = 0.000178\n\nThe **positive** excess refractive index indicates enhanced polarizability in the mixture relative to ideal mixing, again consistent with strong intermolecular interactions.\n\n#### 5. Excess Molar Enthalpy (Hᴱ)\n\nA thorough search of the ThermoML database found **no Hᴱ data** for DMSO + water at any temperature. Twenty Hᴱ blocks exist for DMSO with organic co-solvents, but none with water. This property could not be assessed from the available database.\n\n---\n\n### Does the Composition of Maximum Departure Change with Property?\n\n**Yes — and significantly.** All composition values below are from predict_from_rk outputs (derived from the RK fits, not raw database values):\n\n| Property | x(DMSO) at max |Δᴱ| | Physical driver |\n|---|---|---|\n| Surface tension | **≈ 0.15–0.20** | Preferential surface adsorption of DMSO |\n| Excess molar volume | **≈ 0.33** | Efficient packing via H-bonding |\n| Refractive index | **≈ 0.30–0.35** | Enhanced polarizability from H-bond complexes |\n| Viscosity | **≈ 0.35** | Maximum intermolecular friction from DMSO·nH₂O network |\n\nThe **volumetric, optical, and transport** excess extrema cluster near x(DMSO) ≈ 0.30–0.35. The stoichiometric ratio x(DMSO) = 1/3 (i.e. a 1:2 DMSO:water molar ratio) is a theoretical reference point often discussed in the literature for this system. However, **surface tension** departs most at a much lower DMSO content (x ≈ 0.15–0.20), because the surface excess is governed by DMSO's amphiphilic character and preferential adsorption at the air–liquid interface — a surface phenomenon rather than a bulk one.\n\nIn terms of **magnitude**, viscosity shows by far the strongest departure: the predicted viscosity at x(DMSO) ≈ 0.35 from predict_from_rk is ~0.00374 Pa·s versus an Arrhenius ideal of ~0.00115 Pa·s (a ratio of ~0.00374/0.00115 ≈ 3.3, derived from predict_from_rk output values), whereas the volumetric contraction is only a few percent of V_m and the refractive index excess is ~4% of n_D. The viscosity anomaly is the most dramatic signature of non-ideal mixing in this system.\n\n---\n\n### Data Sources\n\n| Property | DOI | GLOBlit | Block | T (K) | P (kPa) |\n|---|---|---|---|---|---|\n| Density / Vᴱ | 10.1016/j.jct.2006.12.012 | GLOBlit_2781 | PROPblock_4 | 298.15 | 101.0 |\n| Viscosity | 10.1016/j.jct.2006.12.012 | GLOBlit_2781 | PROPblock_3 | 298.15 | 101.0 |\n| Surface tension | 10.1021/je7001013 | GLOBlit_10766 | PROPblock_9 | 298.15 | ambient |\n| Refractive index | 10.1021/je7001013 | GLOBlit_10766 | PROPblock_10 | 298.15 | 101.0 |\n| Pure DMSO γ | 10.1016/j.jct.2013.02.021 | GLOBlit_3840 | PROPblock_1 | 298.15 | — |\n| Pure water γ | 10.1016/j.fluid.2009.07.010 | GLOBlit_725 | PROPblock_12 | 298.15 | — |\n| Pure DMSO n_D | 10.1016/j.jct.2008.05.010 | GLOBlit_2957 | PROPblock_11 | 298.15 | 101.325 |\n| Pure water n_D | 10.1016/j.fluid.2005.09.009 | GLOBlit_306 | PROPblock_5 | 298.15 | 101.325 |\n\n---\n[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:\n- **MISATTRIBUTED_VALUE** PROPblock_11: 0.15 does not belong to PROPblock_11; it matches only GLOBlit_10766::PROPblock_10 (inspected this run)\n  fix (required — this IS a database value, under a different block): `re-anchor 0.15 to GLOBlit_10766::PROPblock_10 — no new tool call needed`\n- **AMBIGUOUS_VALUE** PROPblock_11: 0.33 matches 3 different sources — ambiguous; re-quote it from an inspection of the block you mean\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"PROPblock_11\", literature=\"<GLOBlit_N or DOI>\", nearest={\"column\": \"temperature_k\", \"value\": 0.33})` — if it is a value you computed or an external reference, keep it and label its provenance instead\n- **MISATTRIBUTED_VALUE** PROPblock_11: 0.15 does not belong to PROPblock_11; it matches only GLOBlit_10766::PROPblock_10 (inspected this run)\n  fix (required — this IS a database value, under a different block): `re-anchor 0.15 to GLOBlit_10766::PROPblock_10 — no new tool call needed`\n- **MISATTRIBUTED_VALUE** PROPblock_11: 0.00374 does not belong to PROPblock_11; it matches only GLOBlit_2652::PROPblock_3 (inspected this run)\n  fix (required — this IS a database value, under a different block): `re-anchor 0.00374 to GLOBlit_2652::PROPblock_3 — no new tool call needed`\n- **MISATTRIBUTED_VALUE** PROPblock_11: 0.00374 does not belong to PROPblock_11; it matches only GLOBlit_2652::PROPblock_3 (inspected this run)\n  fix (required — this IS a database value, under a different block): `re-anchor 0.00374 to GLOBlit_2652::PROPblock_3 — no new tool call needed`\n- **MISATTRIBUTED_VALUE** PROPblock_11: 3.3 does not belong to PROPblock_11; it matches only GLOBlit_2652::PROPblock_3 (inspected this run)\n  fix (required — this IS a database value, under a different block): `re-anchor 3.3 to GLOBlit_2652::PROPblock_3 — no new tool call needed`\nInspected so far: PROPblock_1, PROPblock_10, PROPblock_11, PROPblock_12, PROPblock_3, PROPblock_4, PROPblock_5, PROPblock_8, PROPblock_9",
  "core_claims": [
    "At 298.15 K, the DMSO + water system departs from ideal mixing in all four measured properties (excess molar volume, viscosity, surface tension, refractive index), but the composition of maximum departure differs by property.",
    "Viscosity shows by far the largest relative departure from ideal mixing: the predicted viscosity at x(DMSO) ≈ 0.35 is ~0.00374 Pa·s versus an Arrhenius ideal of ~0.00115 Pa·s (ln-space excess = +1.17), corresponding to roughly 320% above the Arrhenius ideal.",
    "Excess molar volume, refractive index, and viscosity extrema cluster near x(DMSO) ≈ 0.30–0.35, consistent with the often-discussed 1:2 DMSO:water stoichiometric ratio, whereas the surface tension excess peaks at a much lower DMSO content (x ≈ 0.15–0.20), reflecting DMSO's preferential adsorption at the air–liquid interface.",
    "The negative excess molar volume (maximum |Vᴱ| ≈ −9.57 × 10⁻⁷ m³/mol near x(DMSO) ≈ 0.33) indicates volume contraction upon mixing, consistent with strong DMSO–water hydrogen bonding.",
    "The negative excess surface tension (maximum |γᴱ| ≈ −0.0093 N/m near x(DMSO) ≈ 0.15–0.20) reflects DMSO's amphiphilic character and preferential surface adsorption — a surface rather than bulk phenomenon.",
    "No excess molar enthalpy (Hᴱ) data for DMSO + water were found in the ThermoML database at any temperature, so that property could not be assessed.",
    "Several quoted values carry UNVERIFIED or MISATTRIBUTED flags due to block-attribution discrepancies, reducing confidence in the precise provenance of some numeric results."
  ],
  "sources": [
    {
      "doi": "10.1016/j.jct.2006.12.012",
      "lit_num_id": "GLOBlit_2781",
      "block": "PROPblock_4",
      "BLKsubsys_id": null,
      "description": "Provides binary DMSO+water density data at 298.15 K across the full mole-fraction range (0.0–1.0), used to compute excess molar volume via V_m = (x₁M₁+x₂M₂)/ρ and fitted with a 5th-order RK polynomial showing maximum |Vᴱ| ≈ −9.57×10⁻⁷ m³/mol near x(DMSO) ≈ 0.33."
    },
    {
      "doi": "10.1016/j.jct.2006.12.012",
      "lit_num_id": "GLOBlit_2781",
      "block": "PROPblock_3",
      "BLKsubsys_id": null,
      "description": "Provides binary DMSO+water viscosity data at 298.15 K across the full mole-fraction range, used to compute Arrhenius excess viscosity. The maximum viscosity of 0.003735 Pa·s near x(DMSO) ≈ 0.35 represents the largest relative departure (~320%) from ideal mixing of any property examined."
    },
    {
      "doi": "10.1021/je7001013",
      "lit_num_id": "GLOBlit_10766",
      "block": "PROPblock_9",
      "BLKsubsys_id": null,
      "description": "Provides binary DMSO+water surface tension data at 298.15 K (range 0.0387–0.071 N/m), fitted with a 5th-order RK polynomial showing maximum |γᴱ| ≈ −0.0093 N/m near x(DMSO) ≈ 0.15–0.20, reflecting DMSO's preferential surface adsorption."
    },
    {
      "doi": "10.1021/je7001013",
      "lit_num_id": "GLOBlit_10766",
      "block": "PROPblock_10",
      "BLKsubsys_id": null,
      "description": "Provides binary DMSO+water refractive index data at 298.15 K (range 1.339–1.47), fitted with a 3rd-order RK polynomial showing maximum excess n_D ≈ +0.056 near x(DMSO) ≈ 0.30–0.35, indicating enhanced polarizability from intermolecular interactions."
    },
    {
      "doi": "10.1016/j.jct.2013.02.021",
      "lit_num_id": "GLOBlit_3840",
      "block": "PROPblock_1",
      "BLKsubsys_id": null,
      "description": "Provides pure DMSO surface tension data; the value at 298.15 K (within the 0.04103–0.04336 N/m range) was used as the pure-component endpoint γ(DMSO) = 0.04278 N/m for computing excess surface tension of the binary mixture."
    },
    {
      "doi": "10.1016/j.fluid.2009.07.010",
      "lit_num_id": "GLOBlit_725",
      "block": "PROPblock_12",
      "BLKsubsys_id": null,
      "description": "Provides the pure water surface tension value γ(water) = 0.07135 N/m at 298.15 K, used as the pure-component endpoint for computing excess surface tension of the DMSO+water mixture."
    },
    {
      "doi": "10.1016/j.jct.2008.05.010",
      "lit_num_id": "GLOBlit_2957",
      "block": "PROPblock_11",
      "BLKsubsys_id": null,
      "description": "Provides the pure DMSO refractive index n_D = 1.4771 at 298.15 K, used as the pure-component endpoint for computing excess refractive index of the DMSO+water mixture."
    },
    {
      "doi": "10.1016/j.fluid.2005.09.009",
      "lit_num_id": "GLOBlit_306",
      "block": "PROPblock_5",
      "BLKsubsys_id": null,
      "description": "Provides the pure water refractive index n_D = 1.3325 at 298.15 K, used as the pure-component endpoint for computing excess refractive index of the DMSO+water mixture."
    }
  ],
  "fit_results": [
    {
      "doi": "10.1016/j.jct.2006.12.012",
      "lit_num_id": "GLOBlit_2781",
      "block_number": "PROPblock_4",
      "BLKsubsys_id": null,
      "property": "GLOBprop_1",
      "rk_order": 5,
      "rk_coeffs": [
        -3.5811616129639533e-06,
        2.066912296384208e-06,
        -2.930798453481958e-07,
        -2.4117429303690355e-06,
        1.6183268427201442e-06,
        7.991724801824448e-07
      ],
      "r_squared": 0.999909,
      "rmse": 2.9839840842544677e-09,
      "n_points": 22,
      "temperature_K": 298.15,
      "mixing_rule": "linear"
    },
    {
      "doi": "10.1016/j.jct.2006.12.012",
      "lit_num_id": "GLOBlit_2781",
      "block_number": "PROPblock_3",
      "BLKsubsys_id": null,
      "property": "viscosity_298K",
      "rk_order": 5,
      "rk_coeffs": [
        3.7055558156480792,
        -3.8597209612010275,
        2.1830371021716743,
        -0.8181531956379644,
        -1.8030520692636798,
        2.5482666377117202
      ],
      "r_squared": 0.999497,
      "rmse": 0.00881979868119369,
      "n_points": 22,
      "temperature_K": 298.15,
      "mixing_rule": "arrhenius"
    },
    {
      "doi": "10.1021/je7001013",
      "lit_num_id": "GLOBlit_10766",
      "block_number": "PROPblock_9",
      "BLKsubsys_id": null,
      "property": "GLOBprop_13",
      "rk_order": 5,
      "rk_coeffs": [
        -0.03389357746760463,
        -0.00254063893274142,
        -0.03247669827392549,
        0.08718093299853281,
        -0.006591515080280431,
        -0.08176118440646336
      ],
      "r_squared": 0.985302,
      "rmse": 0.00027135333058068,
      "n_points": 15,
      "temperature_K": 298.15,
      "mixing_rule": "linear"
    },
    {
      "doi": "10.1021/je7001013",
      "lit_num_id": "GLOBlit_10766",
      "block_number": "PROPblock_10",
      "BLKsubsys_id": null,
      "property": "GLOBprop_7",
      "rk_order": 3,
      "rk_coeffs": [
        0.19712734829244696,
        -0.1284807255128319,
        0.0842113202724752,
        -0.026400335912482222
      ],
      "r_squared": 0.999858,
      "rmse": 0.00017833544272879883,
      "n_points": 10,
      "temperature_K": 298.15,
      "mixing_rule": "linear"
    }
  ]
}

---

## Data Inspections (deterministic evidence ledger)

Hardcoded envelope merge — not agent-authored. 13 entr(ies); verbatim rows below.

- INSP_859c666658c3 — GLOBlit_2652::PROPblock_3 · complete · 6 rows
- INSP_4c118f2b8c2e — GLOBlit_10766::PROPblock_9 · rdp · 12 rows
- INSP_6c692cd44b0e — GLOBlit_10766::PROPblock_10 · complete · 11 rows
- INSP_b08a03233872 — GLOBlit_2781::PROPblock_3 · rdp · 18 rows
- INSP_c018a8ec4dd8 — GLOBlit_11517::PROPblock_3 · complete · 7 rows
- INSP_469eacdbeda0 — GLOBlit_2584::PROPblock_8 · rdp · 24 rows
- INSP_4fb8c018b67f — GLOBlit_2781::PROPblock_3 · rdp · 33 rows
- INSP_5165d05564e1 — GLOBlit_11018::PROPblock_1 · complete · 1 rows
- INSP_9268af01c703 — GLOBlit_2781::PROPblock_4 · rdp · 30 rows
- INSP_e4b65cd8115a — GLOBlit_3840::PROPblock_1 · nearest · 1 rows
- INSP_3d7d879c463b — GLOBlit_2957::PROPblock_11 · nearest · 1 rows
- INSP_cf6ea779f190 — GLOBlit_725::PROPblock_12 · nearest · 1 rows
- INSP_b9acf5321bd9 — GLOBlit_306::PROPblock_5 · nearest · 1 rows

```json
[
  {
    "doi": "10.1016/j.jct.2006.01.007",
    "block_number": "PROPblock_3",
    "table_mode": "complete",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<dimethyl sulfoxide>",
      "pressure_kpa",
      "speed_of_sound_m_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "288.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.0385",
        "pressure_kpa": "101.0",
        "speed_of_sound_m_s": "1555.18"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "temperature_k": "293.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.0385",
        "pressure_kpa": "101.0",
        "speed_of_sound_m_s": "1562.46"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.0385",
        "pressure_kpa": "101.0",
        "speed_of_sound_m_s": "1568.53"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "temperature_k": "303.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.0385",
        "pressure_kpa": "101.0",
        "speed_of_sound_m_s": "1573.38"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "temperature_k": "308.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.0385",
        "pressure_kpa": "101.0",
        "speed_of_sound_m_s": "1577"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "temperature_k": "313.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.0385",
        "pressure_kpa": "101.0",
        "speed_of_sound_m_s": "1579.41"
      }
    ],
    "inspection_id": "INSP_859c666658c3",
    "lit_num_id": "GLOBlit_2652"
  },
  {
    "doi": "10.1021/je7001013",
    "block_number": "PROPblock_9",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<dimethyl sulfoxide>",
      "surface_tension_liquidgas_n_m"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.0121",
        "surface_tension_liquidgas_n_m": "0.071"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.1044",
        "surface_tension_liquidgas_n_m": "0.0612"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.1979",
        "surface_tension_liquidgas_n_m": "0.0567"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.2507",
        "surface_tension_liquidgas_n_m": "0.0554"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.2999",
        "surface_tension_liquidgas_n_m": "0.0533"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.3536",
        "surface_tension_liquidgas_n_m": "0.0526"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.4523",
        "surface_tension_liquidgas_n_m": "0.0503"
      },
      {
        "BLKpoint_id": "BLKpoint_12",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.501",
        "surface_tension_liquidgas_n_m": "0.0483"
      },
      {
        "BLKpoint_id": "BLKpoint_13",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.59",
        "surface_tension_liquidgas_n_m": "0.046"
      },
      {
        "BLKpoint_id": "BLKpoint_14",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.7027",
        "surface_tension_liquidgas_n_m": "0.044"
      },
      {
        "BLKpoint_id": "BLKpoint_15",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.8088",
        "surface_tension_liquidgas_n_m": "0.0426"
      },
      {
        "BLKpoint_id": "BLKpoint_16",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.8945",
        "surface_tension_liquidgas_n_m": "0.042"
      }
    ],
    "inspection_id": "INSP_4c118f2b8c2e",
    "lit_num_id": "GLOBlit_10766"
  },
  {
    "doi": "10.1021/je7001013",
    "block_number": "PROPblock_10",
    "table_mode": "complete",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<dimethyl sulfoxide>",
      "pressure_kpa",
      "refractive_index_na_dline"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.0121",
        "pressure_kpa": "101.0",
        "refractive_index_na_dline": "1.34"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.0202",
        "pressure_kpa": "101.0",
        "refractive_index_na_dline": "1.344"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.1467",
        "pressure_kpa": "101.0",
        "refractive_index_na_dline": "1.396"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.2455",
        "pressure_kpa": "101.0",
        "refractive_index_na_dline": "1.4215"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.2959",
        "pressure_kpa": "101.0",
        "refractive_index_na_dline": "1.4305"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.3213",
        "pressure_kpa": "101.0",
        "refractive_index_na_dline": "1.4345"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.3713",
        "pressure_kpa": "101.0",
        "refractive_index_na_dline": "1.4415"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.3967",
        "pressure_kpa": "101.0",
        "refractive_index_na_dline": "1.4445"
      },
      {
        "BLKpoint_id": "BLKpoint_9",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.4301",
        "pressure_kpa": "101.0",
        "refractive_index_na_dline": "1.4475"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.5964",
        "pressure_kpa": "101.0",
        "refractive_index_na_dline": "1.461"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.7685",
        "pressure_kpa": "101.0",
        "refractive_index_na_dline": "1.47"
      }
    ],
    "inspection_id": "INSP_6c692cd44b0e",
    "lit_num_id": "GLOBlit_10766"
  },
  {
    "doi": "10.1016/j.jct.2006.12.012",
    "block_number": "PROPblock_3",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<dimethyl sulfoxide>",
      "pressure_kpa",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0008901"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.0238",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0010331"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.0489",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0012576"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.1587",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0025493"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.2036",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0030165"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.2379",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0033011"
      },
      {
        "BLKpoint_id": "BLKpoint_9",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.2768",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0035372"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.3074",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0036564"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.3335",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0037144"
      },
      {
        "BLKpoint_id": "BLKpoint_12",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.3638",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0037353"
      },
      {
        "BLKpoint_id": "BLKpoint_13",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.3906",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0037169"
      },
      {
        "BLKpoint_id": "BLKpoint_14",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.4412",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0036062"
      },
      {
        "BLKpoint_id": "BLKpoint_15",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.5193",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0033124"
      },
      {
        "BLKpoint_id": "BLKpoint_17",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.6195",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0028832"
      },
      {
        "BLKpoint_id": "BLKpoint_18",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.6813",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0026556"
      },
      {
        "BLKpoint_id": "BLKpoint_19",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.7595",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0024317"
      },
      {
        "BLKpoint_id": "BLKpoint_21",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.8856",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0021754"
      },
      {
        "BLKpoint_id": "BLKpoint_24",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "1",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001996"
      }
    ],
    "inspection_id": "INSP_b08a03233872",
    "lit_num_id": "GLOBlit_2781"
  },
  {
    "doi": "10.1021/je9001027",
    "block_number": "PROPblock_3",
    "table_mode": "complete",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mass_fraction_<dimethyl sulfoxide>",
      "pressure_kpa",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "298.15",
        "mass_fraction_<dimethyl sulfoxide>": "0",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.00089"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "temperature_k": "298.15",
        "mass_fraction_<dimethyl sulfoxide>": "0.2",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.00134"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "temperature_k": "298.15",
        "mass_fraction_<dimethyl sulfoxide>": "0.4",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002221"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "temperature_k": "298.15",
        "mass_fraction_<dimethyl sulfoxide>": "0.5",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0028073"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "temperature_k": "298.15",
        "mass_fraction_<dimethyl sulfoxide>": "0.6",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.003421"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "temperature_k": "298.15",
        "mass_fraction_<dimethyl sulfoxide>": "0.7",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0023568"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "temperature_k": "298.15",
        "mass_fraction_<dimethyl sulfoxide>": "1",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001966"
      }
    ],
    "inspection_id": "INSP_c018a8ec4dd8",
    "lit_num_id": "GLOBlit_11517"
  },
  {
    "doi": "10.1016/j.jct.2005.07.012",
    "block_number": "PROPblock_8",
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
        "temperature_k": "288.15",
        "mole_fraction_<water>": "0.0308",
        "pressure_kpa": "100.0",
        "mass_density_kg_m3": "1105.54"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "temperature_k": "288.15",
        "mole_fraction_<water>": "0.499",
        "pressure_kpa": "100.0",
        "mass_density_kg_m3": "1107.78"
      },
      {
        "BLKpoint_id": "BLKpoint_12",
        "temperature_k": "288.15",
        "mole_fraction_<water>": "0.5992",
        "pressure_kpa": "100.0",
        "mass_density_kg_m3": "1104.45"
      },
      {
        "BLKpoint_id": "BLKpoint_14",
        "temperature_k": "288.15",
        "mole_fraction_<water>": "0.6987",
        "pressure_kpa": "100.0",
        "mass_density_kg_m3": "1096.45"
      },
      {
        "BLKpoint_id": "BLKpoint_17",
        "temperature_k": "288.15",
        "mole_fraction_<water>": "0.8495",
        "pressure_kpa": "100.0",
        "mass_density_kg_m3": "1065.42"
      },
      {
        "BLKpoint_id": "BLKpoint_24",
        "temperature_k": "288.15",
        "mole_fraction_<water>": "0.9798",
        "pressure_kpa": "100.0",
        "mass_density_kg_m3": "1009.97"
      },
      {
        "BLKpoint_id": "BLKpoint_25",
        "temperature_k": "293.15",
        "mole_fraction_<water>": "0.0308",
        "pressure_kpa": "100.0",
        "mass_density_kg_m3": "1100.52"
      },
      {
        "BLKpoint_id": "BLKpoint_34",
        "temperature_k": "293.15",
        "mole_fraction_<water>": "0.499",
        "pressure_kpa": "100.0",
        "mass_density_kg_m3": "1103.24"
      },
      {
        "BLKpoint_id": "BLKpoint_36",
        "temperature_k": "293.15",
        "mole_fraction_<water>": "0.5992",
        "pressure_kpa": "100.0",
        "mass_density_kg_m3": "1100.14"
      },
      {
        "BLKpoint_id": "BLKpoint_38",
        "temperature_k": "293.15",
        "mole_fraction_<water>": "0.6987",
        "pressure_kpa": "100.0",
        "mass_density_kg_m3": "1092.41"
      },
      {
        "BLKpoint_id": "BLKpoint_41",
        "temperature_k": "293.15",
        "mole_fraction_<water>": "0.8495",
        "pressure_kpa": "100.0",
        "mass_density_kg_m3": "1062.38"
      },
      {
        "BLKpoint_id": "BLKpoint_48",
        "temperature_k": "293.15",
        "mole_fraction_<water>": "0.9798",
        "pressure_kpa": "100.0",
        "mass_density_kg_m3": "1008.78"
      },
      {
        "BLKpoint_id": "BLKpoint_49",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.0308",
        "pressure_kpa": "100.0",
        "mass_density_kg_m3": "1095.32"
      },
      {
        "BLKpoint_id": "BLKpoint_58",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.499",
        "pressure_kpa": "100.0",
        "mass_density_kg_m3": "1098.66"
      },
      {
        "BLKpoint_id": "BLKpoint_60",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.5992",
        "pressure_kpa": "100.0",
        "mass_density_kg_m3": "1095.77"
      },
      {
        "BLKpoint_id": "BLKpoint_62",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.6987",
        "pressure_kpa": "100.0",
        "mass_density_kg_m3": "1088.33"
      },
      {
        "BLKpoint_id": "BLKpoint_65",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.8495",
        "pressure_kpa": "100.0",
        "mass_density_kg_m3": "1059.24"
      },
      {
        "BLKpoint_id": "BLKpoint_72",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.9798",
        "pressure_kpa": "100.0",
        "mass_density_kg_m3": "1007.35"
      },
      {
        "BLKpoint_id": "BLKpoint_73",
        "temperature_k": "303.15",
        "mole_fraction_<water>": "0.0308",
        "pressure_kpa": "100.0",
        "mass_density_kg_m3": "1090.32"
      },
      {
        "BLKpoint_id": "BLKpoint_82",
        "temperature_k": "303.15",
        "mole_fraction_<water>": "0.499",
        "pressure_kpa": "100.0",
        "mass_density_kg_m3": "1094.06"
      },
      {
        "BLKpoint_id": "BLKpoint_84",
        "temperature_k": "303.15",
        "mole_fraction_<water>": "0.5992",
        "pressure_kpa": "100.0",
        "mass_density_kg_m3": "1091.42"
      },
      {
        "BLKpoint_id": "BLKpoint_86",
        "temperature_k": "303.15",
        "mole_fraction_<water>": "0.6987",
        "pressure_kpa": "100.0",
        "mass_density_kg_m3": "1084.2"
      },
      {
        "BLKpoint_id": "BLKpoint_89",
        "temperature_k": "303.15",
        "mole_fraction_<water>": "0.8495",
        "pressure_kpa": "100.0",
        "mass_density_kg_m3": "1056.02"
      },
      {
        "BLKpoint_id": "BLKpoint_96",
        "temperature_k": "303.15",
        "mole_fraction_<water>": "0.9798",
        "pressure_kpa": "100.0",
        "mass_density_kg_m3": "1005.71"
      }
    ],
    "inspection_id": "INSP_469eacdbeda0",
    "lit_num_id": "GLOBlit_2584"
  },
  {
    "doi": "10.1016/j.jct.2006.12.012",
    "block_number": "PROPblock_3",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<dimethyl sulfoxide>",
      "pressure_kpa",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0008901"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.2379",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0033011"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.3074",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0036564"
      },
      {
        "BLKpoint_id": "BLKpoint_12",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.3638",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0037353"
      },
      {
        "BLKpoint_id": "BLKpoint_14",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.4412",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0036062"
      },
      {
        "BLKpoint_id": "BLKpoint_19",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.7595",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0024317"
      },
      {
        "BLKpoint_id": "BLKpoint_24",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "1",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001996"
      },
      {
        "BLKpoint_id": "BLKpoint_25",
        "temperature_k": "303.15",
        "mole_fraction_<dimethyl sulfoxide>": "0",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0007973"
      },
      {
        "BLKpoint_id": "BLKpoint_31",
        "temperature_k": "303.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.2036",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002704"
      },
      {
        "BLKpoint_id": "BLKpoint_33",
        "temperature_k": "303.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.2768",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.003162"
      },
      {
        "BLKpoint_id": "BLKpoint_35",
        "temperature_k": "303.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.3335",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0033221"
      },
      {
        "BLKpoint_id": "BLKpoint_38",
        "temperature_k": "303.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.4412",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0032411"
      },
      {
        "BLKpoint_id": "BLKpoint_42",
        "temperature_k": "303.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.6813",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0024208"
      },
      {
        "BLKpoint_id": "BLKpoint_48",
        "temperature_k": "303.15",
        "mole_fraction_<dimethyl sulfoxide>": "1",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0018357"
      },
      {
        "BLKpoint_id": "BLKpoint_49",
        "temperature_k": "308.15",
        "mole_fraction_<dimethyl sulfoxide>": "0",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0007193"
      },
      {
        "BLKpoint_id": "BLKpoint_55",
        "temperature_k": "308.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.2036",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002389"
      },
      {
        "BLKpoint_id": "BLKpoint_57",
        "temperature_k": "308.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.2768",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002786"
      },
      {
        "BLKpoint_id": "BLKpoint_59",
        "temperature_k": "308.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.3335",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0029301"
      },
      {
        "BLKpoint_id": "BLKpoint_62",
        "temperature_k": "308.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.4412",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002876"
      },
      {
        "BLKpoint_id": "BLKpoint_67",
        "temperature_k": "308.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.7595",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0020086"
      },
      {
        "BLKpoint_id": "BLKpoint_72",
        "temperature_k": "308.15",
        "mole_fraction_<dimethyl sulfoxide>": "1",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0016689"
      },
      {
        "BLKpoint_id": "BLKpoint_73",
        "temperature_k": "313.15",
        "mole_fraction_<dimethyl sulfoxide>": "0",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.000653"
      },
      {
        "BLKpoint_id": "BLKpoint_79",
        "temperature_k": "313.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.2036",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0020754"
      },
      {
        "BLKpoint_id": "BLKpoint_83",
        "temperature_k": "313.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.3335",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0025395"
      },
      {
        "BLKpoint_id": "BLKpoint_86",
        "temperature_k": "313.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.4412",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0025085"
      },
      {
        "BLKpoint_id": "BLKpoint_91",
        "temperature_k": "313.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.7595",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0018182"
      },
      {
        "BLKpoint_id": "BLKpoint_96",
        "temperature_k": "313.15",
        "mole_fraction_<dimethyl sulfoxide>": "1",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0015351"
      },
      {
        "BLKpoint_id": "BLKpoint_97",
        "temperature_k": "318.15",
        "mole_fraction_<dimethyl sulfoxide>": "0",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0005961"
      },
      {
        "BLKpoint_id": "BLKpoint_103",
        "temperature_k": "318.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.2036",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0017611"
      },
      {
        "BLKpoint_id": "BLKpoint_107",
        "temperature_k": "318.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.3335",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0021491"
      },
      {
        "BLKpoint_id": "BLKpoint_110",
        "temperature_k": "318.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.4412",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0021416"
      },
      {
        "BLKpoint_id": "BLKpoint_115",
        "temperature_k": "318.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.7595",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0016159"
      },
      {
        "BLKpoint_id": "BLKpoint_120",
        "temperature_k": "318.15",
        "mole_fraction_<dimethyl sulfoxide>": "1",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0013935"
      }
    ],
    "inspection_id": "INSP_4fb8c018b67f",
    "lit_num_id": "GLOBlit_2781"
  },
  {
    "doi": "10.1021/je700645p",
    "block_number": "PROPblock_1",
    "table_mode": "complete",
    "columns": [
      "BLKpoint_id",
      "pressure_kpa",
      "temperature_k",
      "refractive_index_na_dline"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "pressure_kpa": "81.5",
        "temperature_k": "298.15",
        "refractive_index_na_dline": "1.3417"
      }
    ],
    "inspection_id": "INSP_5165d05564e1",
    "lit_num_id": "GLOBlit_11018"
  },
  {
    "doi": "10.1016/j.jct.2006.12.012",
    "block_number": "PROPblock_4",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<dimethyl sulfoxide>",
      "pressure_kpa",
      "mass_density_kg_m3"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "997.05"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.1587",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "1061.32"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.3074",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "1088.96"
      },
      {
        "BLKpoint_id": "BLKpoint_13",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.3906",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "1095.11"
      },
      {
        "BLKpoint_id": "BLKpoint_15",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.5193",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "1098.34"
      },
      {
        "BLKpoint_id": "BLKpoint_24",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "1",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "1096.29"
      },
      {
        "BLKpoint_id": "BLKpoint_25",
        "temperature_k": "303.15",
        "mole_fraction_<dimethyl sulfoxide>": "0",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "995.65"
      },
      {
        "BLKpoint_id": "BLKpoint_30",
        "temperature_k": "303.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.1587",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "1058.32"
      },
      {
        "BLKpoint_id": "BLKpoint_34",
        "temperature_k": "303.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.3074",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "1085.02"
      },
      {
        "BLKpoint_id": "BLKpoint_37",
        "temperature_k": "303.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.3906",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "1091.09"
      },
      {
        "BLKpoint_id": "BLKpoint_39",
        "temperature_k": "303.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.5193",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "1094.01"
      },
      {
        "BLKpoint_id": "BLKpoint_48",
        "temperature_k": "303.15",
        "mole_fraction_<dimethyl sulfoxide>": "1",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "1091.44"
      },
      {
        "BLKpoint_id": "BLKpoint_49",
        "temperature_k": "308.15",
        "mole_fraction_<dimethyl sulfoxide>": "0",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "994.03"
      },
      {
        "BLKpoint_id": "BLKpoint_54",
        "temperature_k": "308.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.1587",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "1055.11"
      },
      {
        "BLKpoint_id": "BLKpoint_57",
        "temperature_k": "308.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.2768",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "1077.51"
      },
      {
        "BLKpoint_id": "BLKpoint_61",
        "temperature_k": "308.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.3906",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "1086.84"
      },
      {
        "BLKpoint_id": "BLKpoint_65",
        "temperature_k": "308.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.6195",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "1089.61"
      },
      {
        "BLKpoint_id": "BLKpoint_72",
        "temperature_k": "308.15",
        "mole_fraction_<dimethyl sulfoxide>": "1",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "1086.41"
      },
      {
        "BLKpoint_id": "BLKpoint_73",
        "temperature_k": "313.15",
        "mole_fraction_<dimethyl sulfoxide>": "0",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "992.22"
      },
      {
        "BLKpoint_id": "BLKpoint_78",
        "temperature_k": "313.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.1587",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "1051.58"
      },
      {
        "BLKpoint_id": "BLKpoint_80",
        "temperature_k": "313.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.2379",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "1067.99"
      },
      {
        "BLKpoint_id": "BLKpoint_83",
        "temperature_k": "313.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.3335",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "1079.21"
      },
      {
        "BLKpoint_id": "BLKpoint_87",
        "temperature_k": "313.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.5193",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "1085.1"
      },
      {
        "BLKpoint_id": "BLKpoint_96",
        "temperature_k": "313.15",
        "mole_fraction_<dimethyl sulfoxide>": "1",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "1081.59"
      },
      {
        "BLKpoint_id": "BLKpoint_97",
        "temperature_k": "318.15",
        "mole_fraction_<dimethyl sulfoxide>": "0",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "990.21"
      },
      {
        "BLKpoint_id": "BLKpoint_102",
        "temperature_k": "318.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.1587",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "1047.91"
      },
      {
        "BLKpoint_id": "BLKpoint_104",
        "temperature_k": "318.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.2379",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "1063.81"
      },
      {
        "BLKpoint_id": "BLKpoint_107",
        "temperature_k": "318.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.3335",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "1074.68"
      },
      {
        "BLKpoint_id": "BLKpoint_111",
        "temperature_k": "318.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.5193",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "1080.42"
      },
      {
        "BLKpoint_id": "BLKpoint_120",
        "temperature_k": "318.15",
        "mole_fraction_<dimethyl sulfoxide>": "1",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "1076.46"
      }
    ],
    "inspection_id": "INSP_9268af01c703",
    "lit_num_id": "GLOBlit_2781"
  },
  {
    "doi": "10.1016/j.jct.2013.02.021",
    "block_number": "PROPblock_1",
    "table_mode": "nearest",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "surface_tension_liquidgas_n_m"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_2",
        "temperature_k": "298.15",
        "surface_tension_liquidgas_n_m": "0.04278"
      }
    ],
    "inspection_id": "INSP_e4b65cd8115a",
    "lit_num_id": "GLOBlit_3840"
  },
  {
    "doi": "10.1016/j.jct.2008.05.010",
    "block_number": "PROPblock_11",
    "table_mode": "nearest",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "pressure_kpa",
      "refractive_index_na_dline"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "298.15",
        "pressure_kpa": "101.325",
        "refractive_index_na_dline": "1.4771"
      }
    ],
    "inspection_id": "INSP_3d7d879c463b",
    "lit_num_id": "GLOBlit_2957"
  },
  {
    "doi": "10.1016/j.fluid.2009.07.010",
    "block_number": "PROPblock_12",
    "table_mode": "nearest",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "surface_tension_liquidgas_n_m"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "298.15",
        "surface_tension_liquidgas_n_m": "0.07135"
      }
    ],
    "inspection_id": "INSP_cf6ea779f190",
    "lit_num_id": "GLOBlit_725"
  },
  {
    "doi": "10.1016/j.fluid.2005.09.009",
    "block_number": "PROPblock_5",
    "table_mode": "nearest",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "pressure_kpa",
      "refractive_index_na_dline"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "298.15",
        "pressure_kpa": "101.325",
        "refractive_index_na_dline": "1.3325"
      }
    ],
    "inspection_id": "INSP_b9acf5321bd9",
    "lit_num_id": "GLOBlit_306"
  }
]
```

---

## Verdict

**Data Quality**
The agent used measured mixture data from ThermoML (density, viscosity, surface tension, refractive index) and applied appropriate transforms (e.g., density→molar volume). However, the answer quotes smooth-grid compositions (0.33, 0.35, 0.15–0.20) from predict_from_rk outputs, which is acceptable for extremum identification. Multiple fit_block and predict_from_rk calls appear in the trace, confirming fits were performed. No fabrication detected. Composition basis appears to be mole fraction throughout. The answer is truncated but substantive content is present.

**Fit Quality**
RK order 5 with R² > 0.999 for volume and viscosity is excellent. Surface tension R² = 0.985 is adequate but slightly lower, possibly due to fewer points or stronger asymmetry. Order 3 for refractive index with R² = 0.9999 is appropriate.

**Scientific Verdict**
The analysis correctly identifies viscosity as showing the largest relative departure (~320%) near x(DMSO) ≈ 0.33–0.36, consistent with known DMSO·2H₂O complex formation. Different properties peak at different compositions (volume ~0.33, surface tension ~0.15–0.20), demonstrating that "maximum non-ideality" is property-dependent. Absence of H^E data is honestly noted.

---

## Output Files

- **data**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_120350_743093_e3b9ce8c\data\10_1016_j_jct_2006_12_012_BPROPblock_4_T298.1_fit.csv` — RK fit data — 10.1016/j.jct.2006.12.012 PROPblock_4_T298.1
- **data**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_120350_743093_e3b9ce8c\data\10_1016_j_jct_2006_12_012_BPROPblock_4_T298.1_excess.csv` — Excess property — 10.1016/j.jct.2006.12.012 PROPblock_4_T298.1
- **plot**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_120350_743093_e3b9ce8c\plots\10_1016_j_jct_2006_12_012_BPROPblock_4_T298.1_fit.png` — RK fit plot — 10.1016/j.jct.2006.12.012 PROPblock_4_T298.1
- **plot**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_120350_743093_e3b9ce8c\plots\10_1016_j_jct_2006_12_012_BPROPblock_4_T298.1_excess.png` — Excess plot — 10.1016/j.jct.2006.12.012 PROPblock_4_T298.1
- **data**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_120350_743093_e3b9ce8c\data\10_1016_j_jct_2006_12_012_BPROPblock_3_T298.1_fit.csv` — RK fit data — 10.1016/j.jct.2006.12.012 PROPblock_3_T298.1
- **data**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_120350_743093_e3b9ce8c\data\10_1016_j_jct_2006_12_012_BPROPblock_3_T298.1_excess.csv` — Excess property — 10.1016/j.jct.2006.12.012 PROPblock_3_T298.1
- **plot**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_120350_743093_e3b9ce8c\plots\10_1016_j_jct_2006_12_012_BPROPblock_3_T298.1_fit.png` — RK fit plot — 10.1016/j.jct.2006.12.012 PROPblock_3_T298.1
- **plot**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_120350_743093_e3b9ce8c\plots\10_1016_j_jct_2006_12_012_BPROPblock_3_T298.1_excess.png` — Excess plot — 10.1016/j.jct.2006.12.012 PROPblock_3_T298.1
- **data**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_120350_743093_e3b9ce8c\data\10_1021_je7001013_BPROPblock_9_T298.1_fit.csv` — RK fit data — 10.1021/je7001013 PROPblock_9_T298.1
- **data**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_120350_743093_e3b9ce8c\data\10_1021_je7001013_BPROPblock_9_T298.1_excess.csv` — Excess property — 10.1021/je7001013 PROPblock_9_T298.1
- **plot**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_120350_743093_e3b9ce8c\plots\10_1021_je7001013_BPROPblock_9_T298.1_fit.png` — RK fit plot — 10.1021/je7001013 PROPblock_9_T298.1
- **plot**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_120350_743093_e3b9ce8c\plots\10_1021_je7001013_BPROPblock_9_T298.1_excess.png` — Excess plot — 10.1021/je7001013 PROPblock_9_T298.1
- **data**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_120350_743093_e3b9ce8c\data\10_1021_je7001013_BPROPblock_10_T298.1_fit.csv` — RK fit data — 10.1021/je7001013 PROPblock_10_T298.1
- **data**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_120350_743093_e3b9ce8c\data\10_1021_je7001013_BPROPblock_10_T298.1_excess.csv` — Excess property — 10.1021/je7001013 PROPblock_10_T298.1
- **plot**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_120350_743093_e3b9ce8c\plots\10_1021_je7001013_BPROPblock_10_T298.1_fit.png` — RK fit plot — 10.1021/je7001013 PROPblock_10_T298.1
- **plot**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_120350_743093_e3b9ce8c\plots\10_1021_je7001013_BPROPblock_10_T298.1_excess.png` — Excess plot — 10.1021/je7001013 PROPblock_10_T298.1