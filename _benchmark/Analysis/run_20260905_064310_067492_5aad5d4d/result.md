# Analysis Run — 20260905_065838 (Round 1)

**Question:** What viscosity should I expect for an equimolar DMF + ethylene glycol + water liquid mixture at 25 °C? If it has not been measured directly, give the most defensible estimate, explain the chemical and mathematical basis of every inferred contribution, and identify the measurements supporting it.

**Time:** 873.8s | **Iterations:** 18 | **Tools:** 15

---

## Answer

{
  "answer": "## Estimated Viscosity of Equimolar DMF + Ethylene Glycol + Water at 25 °C\n\n### Bottom Line\n\n**η ≈ 0.00368 Pa·s (3.68 mPa·s)** at 298.15 K and ambient pressure. *(This value is computed — not a database datum — derived from the Muggianu/Arrhenius calculation detailed below.)*\n\nThis is an estimate — the equimolar ternary composition (x_DMF = x_EG = x_water = 1/3) was not measured directly. The estimate is built from three binary Redlich-Kister fits using the Arrhenius (logarithmic) mixing rule, combined via the Muggianu symmetric extension to ternary systems, and cross-validated against nearby ternary measurements.\n\n---\n\n### 1. Why the Equimolar Point Was Not Measured\n\nThe only ternary viscosity block in the ThermoML database for this system is DOI 10.1021/je060113j (GLOBlit_8892, PROPblock_38). Its 11 data points at 298.15 K follow a dilution path from the DMF + EG binary (x_water = 0, x_EG = 0.5408) toward pure water — they do **not** pass through the equimolar point (1/3, 1/3, 1/3). The two nearest measured ternary compositions bracket the target:\n\n| x(water) | x(EG) | x(DMF) | η (Pa·s) |\n|-----------|--------|--------|-----------|\n| 0.2929 | 0.3824 | 1 − 0.2929 − 0.3824 = 0.3247 *(computed by subtraction)* | 0.0035692 |\n| 0.4825 | 0.2799 | 1 − 0.4825 − 0.2799 = 0.2376 *(computed by subtraction)* | 0.0037485 |\n\nThe equimolar point lies between these measured compositions, so the computed estimate of 0.00368 Pa·s *(derived below)* is physically consistent with the bracketing data.\n\n---\n\n### 2. Mathematical Framework\n\n**Arrhenius mixing rule.** For viscosity, the natural mixing variable is ln η. The ideal (Arrhenius) baseline for a ternary mixture is:\n\n> ln η_ideal = x₁·ln η₁\\* + x₂·ln η₂\\* + x₃·ln η₃\\*\n\nThe excess departure is modelled by Redlich-Kister (RK) polynomials fitted to each binary pair. For a ternary system, the **Muggianu symmetric extension** combines the three binary excess functions:\n\n> Δln η_excess = Σ_{i<j} xᵢ·xⱼ · Σₖ Aₖ^(ij) · (xᵢ − xⱼ)^k\n\nAt the equimolar point (x₁ = x₂ = x₃ = 1/3), every (xᵢ − xⱼ) = 0, so **only the A₀ coefficient of each binary pair survives**:\n\n> Δln η_excess = (1/9) · [A₀^(DMF,water) + A₀^(EG,water) + A₀^(DMF,EG)]\n\n---\n\n### 3. Pure-Component Viscosities at 298.15 K\n\nAll ln η\\* values below are computed as the natural logarithm of the corresponding measured viscosity.\n\n| Component | η\\* (Pa·s) | ln η\\* *(computed)* | Source |\n|-----------|-----------|---------------------|--------|\n| DMF | 0.0008045 | −7.125 | GLOBlit_9900 / PROPblock_3, block-edge (x_water = 0) |\n| Water | 0.0008903 | −7.024 | GLOBlit_9900 / PROPblock_3, block-edge (x_water = 1) |\n| 1,2-Ethanediol (EG) | 0.016223 | −4.121 | GLOBlit_5201 / PROPblock_24, block-edge (x_EG = 1) |\n\n**Ideal Arrhenius baseline at equimolar** *(computed from the ln values above)*:\n\n> ln η_ideal = (1/3)(−7.125 − 4.121 − 7.024) = −6.090 *(computed)*\n\n> η_ideal = exp(−6.090) = 0.00227 Pa·s *(computed)*\n\n---\n\n### 4. Binary Redlich-Kister Fits (Arrhenius Mixing Rule)\n\n#### 4a. DMF + Water\n\n- **Source:** DOI 10.1021/je300608v (GLOBlit_9900), PROPblock_3\n- **Data:** 12 points at 298.15 K, 101.0 kPa, mole fraction of water\n- **BIC-selected order:** 5\n- **R² = 0.999973**, RMSE = 0.001523 (ln-space)\n- **RK coefficients (ln-space):** A₀ = 3.14029, A₁ = 3.88544, A₂ = 1.91579, A₃ = −0.00569, A₄ = 0.04179, A₅ = 0.39089\n- **A₀ = 3.140** (the only coefficient needed at equimolar)\n\nThis binary shows a pronounced viscosity maximum near x_water ≈ 0.7 (η_max ≈ 0.00248 Pa·s from the RK prediction tool), reflecting strong DMF–water hydrogen bonding where the C=O of DMF acts as a hydrogen-bond acceptor for water.\n\n#### 4b. Ethylene Glycol + Water\n\n- **Source:** DOI 10.1016/j.jct.2018.02.022 (GLOBlit_5201), PROPblock_24\n- **Data:** 19 points at 298.15 K, 92.3 kPa, mole fraction of EG\n- **BIC-selected order:** 3\n- **R² = 0.999940**, RMSE = 0.001320 (ln-space)\n- **RK coefficients (ln-space):** A₀ = 2.39674, A₁ = −1.04444, A₂ = 0.66817, A₃ = −0.32090\n- **A₀ = 2.397**\n\nEG–water mixtures show a monotonic increase in viscosity with EG content (pure EG at 0.016223 Pa·s vs pure water at 0.00089689 Pa·s — both from PROPblock_24 block-edges), driven by the extensive hydrogen-bonding network of EG's two hydroxyl groups.\n\n#### 4c. DMF + Ethylene Glycol\n\n- **Source:** DOI 10.1021/je060113j (GLOBlit_8892), PROPblock_25\n- **Data:** Only **1 composition** at 298.15 K: x_EG = 0.5408, η = 0.0030647 Pa·s\n- **Extraction of A₀** *(all intermediate values below are computed from the inspected pure-component and mixture data)*: With only one data point, only A₀ can be determined. Using pure values η_EG = 0.016223 Pa·s and η_DMF = 0.0008045 Pa·s:\n\n  > ln η_ideal = 0.5408·ln(0.016223) + (1 − 0.5408)·ln(0.0008045) = −5.500 *(computed)*\n\n  > ln η_measured = ln(0.0030647) = −5.788 *(computed)*\n\n  > Δln η = −5.788 − (−5.500) = −0.288 *(computed)*\n\n  > A₀ = Δln η / (0.5408 × 0.4592) = −0.288 / 0.2483 = **−1.159** *(computed)*\n\nThe **negative** A₀ means the DMF–EG interaction produces a viscosity *lower* than the Arrhenius ideal — the mixture is less structured than the geometric-mean prediction. This makes chemical sense: DMF is an aprotic solvent that disrupts EG's intramolecular hydrogen-bonding network without forming comparably strong new associations.\n\n**Limitation:** This A₀ is extracted from a single data point near x = 0.5, so it is the least certain of the three binary contributions. However, the composition (0.5408) is close to equimolar, which is exactly where A₀ dominates, making the extraction relatively robust for this purpose.\n\n---\n\n### 5. Ternary Estimate via Muggianu Extension\n\nAt x_DMF = x_EG = x_water = 1/3 *(all values below are computed from the fit results and pure-component data above)*:\n\n| Contribution | Value |\n|-------------|-------|\n| ln η_ideal | −6.090 *(computed)* |\n| (1/9) × A₀^(DMF,water) = (1/9) × 3.140 | +0.349 *(computed)* |\n| (1/9) × A₀^(EG,water) = (1/9) × 2.397 | +0.266 *(computed)* |\n| (1/9) × A₀^(DMF,EG) = (1/9) × (−1.159) | −0.129 *(computed)* |\n| **Total Δln η_excess** | **+0.487** *(computed)* |\n| **ln η_ternary** | **−5.604** *(computed)* |\n| **η_ternary = exp(−5.604)** | **≈ 0.00368 Pa·s** *(computed)* |\n\nThe positive net excess (+0.487 in ln-space) means the ternary mixture is more viscous than the Arrhenius ideal (0.00227 Pa·s), driven primarily by the strong DMF–water and EG–water hydrogen-bonding interactions that outweigh the weakening DMF–EG interaction.\n\n---\n\n### 6. Cross-Validation\n\nThe computed estimate of 0.00368 Pa·s falls squarely between the two nearest measured ternary points from PROPblock_38 (0.0035692 and 0.0037485 Pa·s), providing confidence in the prediction despite the limited DMF–EG binary data.\n\n---\n\n### 7. Uncertainty and Caveats\n\n1. **DMF–EG binary:** Only one composition point was available (x_EG = 0.5408). Higher-order RK terms (A₁, A₂, …) could not be determined. If the DMF–EG excess is strongly asymmetric, the A₀-only approximation introduces error — but at the equimolar ternary point, only A₀ matters regardless.\n\n2. **No ternary interaction term:** The Muggianu extension assumes no independent ternary contribution. In strongly hydrogen-bonding systems like this one, a ternary correction term C₁₂₃·x₁·x₂·x₃ could be non-negligible. The good agreement with bracketing measurements suggests this term is small.\n\n3. **Pressure differences:** The EG–water fit used data at 92.3 kPa (GLOBlit_5201), while DMF–water was at 101.0 kPa (GLOBlit_9900) and the ternary data at 101.0 kPa (GLOBlit_8892). Liquid viscosity is nearly pressure-independent at these low pressures, so this discrepancy is negligible.\n\n---\n\n### 8. Summary of Measurement Sources\n\n| Binary Pair | DOI | Block | Points at 298.15 K | RK Order | R² | A₀ |\n|-------------|-----|-------|---------------------|----------|-----|-----|\n| DMF + Water | 10.1021/je300608v (GLOBlit_9900) | PROPblock_3 | 12 | 5 | 0.999973 | 3.140 |\n| EG + Water | 10.1016/j.jct.2018.02.022 (GLOBlit_5201) | PROPblock_24 | 19 | 3 | 0.999940 | 2.397 |\n| DMF + EG | 10.1021/je060113j (GLOBlit_8892) | PROPblock_25 | 1 | 0 (A₀ only) | — | −1.159 *(computed)* |\n| Ternary (validation) | 10.1021/je060113j (GLOBlit_8892) | PROPblock_38 | 11 | — | — | — |\n\n---\n[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:\n- **UNGROUNDED_LITERAL** PROPblock_38: 0.3247 (near '…----|-----------| | 0.2929 | 0.3824 | 1 - 0.2929 - 0.3824 = …') matches no inspected row/stat, database table, or other source of PROPblock_38\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"PROPblock_38\", literature=\"<GLOBlit_N or DOI>\", nearest={\"column\": \"temperature_k\", \"value\": 0.3247})` — if it is a value you computed or an external reference, keep it and label its provenance instead\n- **UNGROUNDED_LITERAL** PROPblock_38: 0.2376 (near '…n)* | 0.0035692 | | 0.4825 | 0.2799 | 1 - 0.4825 - 0.2799 = …') matches no inspected row/stat, database table, or other source of PROPblock_38\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"PROPblock_38\", literature=\"<GLOBlit_N or DOI>\", nearest={\"column\": \"temperature_k\", \"value\": 0.2376})` — if it is a value you computed or an external reference, keep it and label its provenance instead\n- **UNGROUNDED_LITERAL** PROPblock_38: 0.00368 (near '…en these measured compositions, so the computed estimate of …') matches no inspected row/stat, database table, or other source of PROPblock_38\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"PROPblock_38\", literature=\"<GLOBlit_N or DOI>\", nearest={\"column\": \"temperature_k\", \"value\": 0.00368})` — if it is a value you computed or an external reference, keep it and label its provenance instead\n- **UNGROUNDED_LITERAL** PROPblock_3 + PROPblock_24: -7.125 (near '…-------|---------------------|--------| | DMF | 0.0008045 | …') matches no inspected row/stat, database table, or other source of PROPblock_3 + PROPblock_24\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"PROPblock_3\", literature=\"<GLOBlit_N or DOI>\", nearest={\"column\": \"temperature_k\", \"value\": -7.125})` — if it is a value you computed or an external reference, keep it and label its provenance instead\n- **UNGROUNDED_LITERAL** PROPblock_3 + PROPblock_24: -7.024 (near '…5 |   /  , block-edge (x_water = 0) | | Water | 0.0008903 | …') matches no inspected row/stat, database table, or other source of PROPblock_3 + PROPblock_24\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"PROPblock_3\", literature=\"<GLOBlit_N or DOI>\", nearest={\"column\": \"temperature_k\", \"value\": -7.024})` — if it is a value you computed or an external reference, keep it and label its provenance instead\n- **UNGROUNDED_LITERAL** PROPblock_3 + PROPblock_24: -4.121 (near '…ock-edge (x_water = 1) | | 1,2-Ethanediol (EG) | 0.016223 | …') matches no inspected row/stat, database table, or other source of PROPblock_3 + PROPblock_24\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"PROPblock_3\", literature=\"<GLOBlit_N or DOI>\", nearest={\"column\": \"temperature_k\", \"value\": -4.121})` — if it is a value you computed or an external reference, keep it and label its provenance instead\n- **UNGROUNDED_LITERAL** PROPblock_24: -7.125 (near '…(computed from the ln values above)*:  > ln η_ideal = (1/3)(…') matches no inspected row/stat, database table, or other source of PROPblock_24\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"PROPblock_24\", literature=\"<GLOBlit_N or DOI>\", nearest={\"column\": \"temperature_k\", \"value\": -7.125})` — if it is a value you computed or an external reference, keep it and label its provenance instead\n- **UNGROUNDED_LITERAL** PROPblock_24: 4.121 (near '…from the ln values above)*:  > ln η_ideal = (1/3)(-7.125 - 4…') matches no inspected row/stat, database table, or other source of PROPblock_24\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"PROPblock_24\", literature=\"<GLOBlit_N or DOI>\", nearest={\"column\": \"temperature_k\", \"value\": 4.121})` — if it is a value you computed or an external reference, keep it and label its provenance instead\n- … and 15 more of the same kinds — PROPblock_24: 7.024, -6.090, 0.00227; PROPblock_25: -5.500, -5.788, +0.487, -5.604, 0.00368, 0.00227; PROPblock_38: 92.3\nInspected so far: PROPblock_13, PROPblock_18, PROPblock_24, PROPblock_25, PROPblock_3, PROPblock_38, PROPblock_5, PROPblock_9",
  "core_claims": [
    "The equimolar ternary composition (x_DMF = x_EG = x_water = 1/3) was not directly measured; the viscosity estimate of ≈ 0.00368 Pa·s (3.68 mPa·s) at 298.15 K and ambient pressure is computed, not a database datum.",
    "The estimate uses the Muggianu symmetric extension of binary Redlich-Kister fits under an Arrhenius (logarithmic) mixing rule, combining three binary excess contributions at the equimolar point where only each binary's A₀ coefficient survives.",
    "Binary Redlich-Kister A₀ coefficients (ln-space) are: DMF + Water A₀ = 3.140 (12 data points, R² = 0.999973), EG + Water A₀ = 2.397 (19 data points, R² = 0.999940), and DMF + EG A₀ = −1.159 (extracted from a single composition point at x_EG = 0.5408).",
    "The DMF–EG binary A₀ is the least certain contribution because it is derived from only one data point; higher-order Redlich-Kister terms could not be determined, though at the equimolar ternary point only A₀ matters.",
    "The positive net excess in ln η (+0.487) indicates the ternary mixture is more viscous than the Arrhenius ideal (0.00227 Pa·s), driven by strong DMF–water and EG–water hydrogen-bonding interactions that outweigh the weakening DMF–EG interaction.",
    "The computed estimate of 0.00368 Pa·s falls between the two nearest measured ternary viscosities from PROPblock_38 (0.0035692 Pa·s and 0.0037485 Pa·s), providing cross-validation support.",
    "No independent ternary interaction term was included in the model; in strongly hydrogen-bonding systems such a term could be non-negligible, but agreement with bracketing measurements suggests it is small."
  ],
  "sources": [
    {
      "doi": "10.1021/je300608v",
      "lit_num_id": "GLOBlit_9900",
      "block": "PROPblock_3",
      "BLKsubsys_id": null,
      "description": "Provides DMF + water binary viscosity data (12 points at 298.15 K across the full mole fraction range) used to fit the Redlich-Kister polynomial yielding A₀ = 3.140, and supplies the pure-component viscosities for DMF (0.0008045 Pa·s) and water (0.0008903 Pa·s) as block-edge values."
    },
    {
      "doi": "10.1016/j.jct.2018.02.022",
      "lit_num_id": "GLOBlit_5201",
      "block": "PROPblock_24",
      "BLKsubsys_id": null,
      "description": "Provides EG + water binary viscosity data (19 points at 298.15 K across the full mole fraction range) used to fit the Redlich-Kister polynomial yielding A₀ = 2.397, and supplies the pure-component viscosity for EG (0.016223 Pa·s) as a block-edge value."
    },
    {
      "doi": "10.1021/je060113j",
      "lit_num_id": "GLOBlit_8892",
      "block": "PROPblock_25",
      "BLKsubsys_id": null,
      "description": "Provides the single DMF + EG binary viscosity data point at 298.15 K (x_EG = 0.5408, η = 0.0030647 Pa·s) from which the A₀ = −1.159 coefficient was extracted for the Muggianu ternary extension."
    },
    {
      "doi": "10.1021/je060113j",
      "lit_num_id": "GLOBlit_8892",
      "block": "PROPblock_38",
      "BLKsubsys_id": null,
      "description": "Provides ternary DMF + EG + water viscosity measurements at 298.15 K used for cross-validation; the two nearest measured compositions bracket the equimolar estimate (0.0035692 and 0.0037485 Pa·s), confirming the computed value of 0.00368 Pa·s is physically consistent."
    }
  ],
  "fit_results": [
    {
      "doi": "10.1021/je300608v",
      "lit_num_id": "GLOBlit_9900",
      "block_number": "PROPblock_3",
      "BLKsubsys_id": null,
      "property": "DMF_water",
      "rk_order": 5,
      "rk_coeffs": [
        3.1402922316632518,
        3.8854391654848013,
        1.915786421193988,
        -0.005692912831677055,
        0.04178949155707623,
        0.39089340704625575
      ],
      "r_squared": 0.999973,
      "rmse": 0.0015230866140327202,
      "n_points": 12,
      "temperature_K": 298.15,
      "mixing_rule": "arrhenius"
    },
    {
      "doi": "10.1016/j.jct.2018.02.022",
      "lit_num_id": "GLOBlit_5201",
      "block_number": "PROPblock_24",
      "BLKsubsys_id": null,
      "property": "EG_water",
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

Hardcoded envelope merge — not agent-authored. 9 entr(ies); verbatim rows below.

- INSP_eb6a6a268c1a — GLOBlit_2656::PROPblock_13 · complete · 10 rows
- INSP_10e84136b97d — GLOBlit_5201::PROPblock_24 · rdp · 15 rows
- INSP_bdb58d28aae5 — GLOBlit_6951::PROPblock_18 · rdp · 14 rows
- INSP_ca607c3d05dd — GLOBlit_8038::PROPblock_5 · rdp · 37 rows
- INSP_475115ec48f0 — GLOBlit_8106::PROPblock_5 · rdp · 16 rows
- INSP_d1035750f998 — GLOBlit_8892::PROPblock_25 · nearest · 3 rows
- INSP_469970d3baa4 — GLOBlit_8676::PROPblock_9 · complete · 11 rows
- INSP_223a0880d59c — GLOBlit_9900::PROPblock_3 · rdp · 12 rows
- INSP_ccb7677d8622 — GLOBlit_8892::PROPblock_38 · complete · 11 rows

```json
[
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
    "doi": "10.1021/je060113j",
    "block_number": "PROPblock_25",
    "table_mode": "nearest",
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
        "temperature_k": "298.15",
        "mole_fraction_<1,2-ethanediol>": "0.5408",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0030647"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "temperature_k": "308.15",
        "mole_fraction_<1,2-ethanediol>": "0.5408",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0024529"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "temperature_k": "318.15",
        "mole_fraction_<1,2-ethanediol>": "0.5408",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0019599"
      }
    ],
    "inspection_id": "INSP_d1035750f998",
    "lit_num_id": "GLOBlit_8892"
  },
  {
    "doi": "10.1021/je050209y",
    "block_number": "PROPblock_9",
    "table_mode": "complete",
    "columns": [
      "BLKpoint_id",
      "mole_fraction_<dimethylformamide>",
      "temperature_k",
      "pressure_kpa",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "mole_fraction_<dimethylformamide>": "0.05",
        "temperature_k": "298.15",
        "pressure_kpa": "101.325",
        "viscosity_pa_s": "0.00131"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "mole_fraction_<dimethylformamide>": "0.1001",
        "temperature_k": "298.15",
        "pressure_kpa": "101.325",
        "viscosity_pa_s": "0.001728"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "mole_fraction_<dimethylformamide>": "0.2",
        "temperature_k": "298.15",
        "pressure_kpa": "101.325",
        "viscosity_pa_s": "0.002346"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "mole_fraction_<dimethylformamide>": "0.299",
        "temperature_k": "298.15",
        "pressure_kpa": "101.325",
        "viscosity_pa_s": "0.002491"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "mole_fraction_<dimethylformamide>": "0.3998",
        "temperature_k": "298.15",
        "pressure_kpa": "101.325",
        "viscosity_pa_s": "0.002273"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "mole_fraction_<dimethylformamide>": "0.4997",
        "temperature_k": "298.15",
        "pressure_kpa": "101.325",
        "viscosity_pa_s": "0.001878"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "mole_fraction_<dimethylformamide>": "0.5993",
        "temperature_k": "298.15",
        "pressure_kpa": "101.325",
        "viscosity_pa_s": "0.001532"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "mole_fraction_<dimethylformamide>": "0.6995",
        "temperature_k": "298.15",
        "pressure_kpa": "101.325",
        "viscosity_pa_s": "0.001243"
      },
      {
        "BLKpoint_id": "BLKpoint_9",
        "mole_fraction_<dimethylformamide>": "0.8",
        "temperature_k": "298.15",
        "pressure_kpa": "101.325",
        "viscosity_pa_s": "0.001045"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "mole_fraction_<dimethylformamide>": "0.8991",
        "temperature_k": "298.15",
        "pressure_kpa": "101.325",
        "viscosity_pa_s": "0.000901"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "mole_fraction_<dimethylformamide>": "0.9488",
        "temperature_k": "298.15",
        "pressure_kpa": "101.325",
        "viscosity_pa_s": "0.000843"
      }
    ],
    "inspection_id": "INSP_469970d3baa4",
    "lit_num_id": "GLOBlit_8676"
  },
  {
    "doi": "10.1021/je300608v",
    "block_number": "PROPblock_3",
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
        "BLKpoint_id": "BLKpoint_16",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0008045"
      },
      {
        "BLKpoint_id": "BLKpoint_17",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.1",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0009018"
      },
      {
        "BLKpoint_id": "BLKpoint_18",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.2",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0010386"
      },
      {
        "BLKpoint_id": "BLKpoint_19",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.3",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0012331"
      },
      {
        "BLKpoint_id": "BLKpoint_20",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.4",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0015078"
      },
      {
        "BLKpoint_id": "BLKpoint_21",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.5",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0018528"
      },
      {
        "BLKpoint_id": "BLKpoint_22",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.6",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0022264"
      },
      {
        "BLKpoint_id": "BLKpoint_23",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.7",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0024775"
      },
      {
        "BLKpoint_id": "BLKpoint_24",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.8",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0023495"
      },
      {
        "BLKpoint_id": "BLKpoint_25",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.9",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0017464"
      },
      {
        "BLKpoint_id": "BLKpoint_27",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.94",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0014116"
      },
      {
        "BLKpoint_id": "BLKpoint_30",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "1",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0008903"
      }
    ],
    "inspection_id": "INSP_223a0880d59c",
    "lit_num_id": "GLOBlit_9900"
  },
  {
    "doi": "10.1021/je060113j",
    "block_number": "PROPblock_38",
    "table_mode": "complete",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<water>",
      "mole_fraction_<1,2-ethanediol>",
      "pressure_kpa",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0",
        "mole_fraction_<1,2-ethanediol>": "0.5408",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0030647"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.2929",
        "mole_fraction_<1,2-ethanediol>": "0.3824",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0035692"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.4825",
        "mole_fraction_<1,2-ethanediol>": "0.2799",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0037485"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.6152",
        "mole_fraction_<1,2-ethanediol>": "0.2081",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0034817"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.7132",
        "mole_fraction_<1,2-ethanediol>": "0.1551",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0032008"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.7886",
        "mole_fraction_<1,2-ethanediol>": "0.1143",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0028546"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.8484",
        "mole_fraction_<1,2-ethanediol>": "0.082",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0024439"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.8969",
        "mole_fraction_<1,2-ethanediol>": "0.0557",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0019531"
      },
      {
        "BLKpoint_id": "BLKpoint_9",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.9372",
        "mole_fraction_<1,2-ethanediol>": "0.0339",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0016778"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.9711",
        "mole_fraction_<1,2-ethanediol>": "0.0156",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0013057"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "1",
        "mole_fraction_<1,2-ethanediol>": "0",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0008904"
      }
    ],
    "inspection_id": "INSP_ccb7677d8622",
    "lit_num_id": "GLOBlit_8892"
  }
]
```

---

## Verdict

**Data Quality**
The agent correctly identified that no direct ternary equimolar measurement exists and used binary RK fits from real ThermoML data (DOIs 10.1021/je300608v, 10.1016/j.jct.2018.02.022). The fit_multi_system calls appear in the trace, confirming fits were performed rather than fabricated. However, the DMF+EG binary fit is truncated/missing from the answer, and the final A₀ value for that pair is not shown. The bracketing ternary data from DOI 10.1021/je060113j provides useful validation. Composition basis appears to be mole fraction throughout. The answer was cut off before completion.

**Fit Quality**
R² values (~0.9999) for the two visible binary fits are excellent. BIC-selected orders (5 and 3) seem reasonable given data density, though order-5 for 12 points risks slight overfitting.

**Scientific Verdict**
The Muggianu/Arrhenius approach is chemically sound for this H-bonding system. The estimate of ~3.68 mPa·s is consistent with bracketing ternary measurements (3.57–3.75 mPa·s). However, the answer is **incomplete** — the DMF+EG binary contribution and final calculation are truncated. **CONDITIONAL PASS** pending the missing third binary fit details.

---

## Output Files

- **data**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_064310_067492_5aad5d4d\data\10_1021_je300608v_BPROPblock_3_T298.1_fit.csv` — RK fit data — 10.1021/je300608v PROPblock_3_T298.1
- **data**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_064310_067492_5aad5d4d\data\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_fit.csv` — RK fit data — 10.1016/j.jct.2018.02.022 PROPblock_24_T298.1
- **data**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_064310_067492_5aad5d4d\data\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_excess.csv` — Excess property — 10.1016/j.jct.2018.02.022 PROPblock_24_T298.1
- **data**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_064310_067492_5aad5d4d\data\10_1021_je300608v_BPROPblock_3_T298.1_excess.csv` — Excess property — 10.1021/je300608v PROPblock_3_T298.1
- **plot**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_064310_067492_5aad5d4d\plots\10_1021_je300608v_BPROPblock_3_T298.1_fit.png` — RK fit plot — 10.1021/je300608v PROPblock_3_T298.1
- **plot**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_064310_067492_5aad5d4d\plots\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_fit.png` — RK fit plot — 10.1016/j.jct.2018.02.022 PROPblock_24_T298.1
- **plot**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_064310_067492_5aad5d4d\plots\10_1021_je300608v_BPROPblock_3_T298.1_excess.png` — Excess plot — 10.1021/je300608v PROPblock_3_T298.1
- **plot**: `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_064310_067492_5aad5d4d\plots\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_excess.png` — Excess plot — 10.1016/j.jct.2018.02.022 PROPblock_24_T298.1