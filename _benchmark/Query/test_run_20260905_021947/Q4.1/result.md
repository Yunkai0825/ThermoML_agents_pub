# Q4.1 — Result

**Prompt:** What viscosity should I expect for an equimolar DMF + water + acetonitrile liquid mixture at 298 K? If no direct measurement is available, estimate it from the closest relevant measurements and explain the chemical basis of the estimate.

**Tool calls:** 4  |  **Time:** 629.2s  |  **Iterations:** 5  |  **Timed out:** False

---

## Answer

{
  "answer": "## Estimated Viscosity of Equimolar DMF + Water + Acetonitrile at 298 K\n\n### Direct Measurement: Not Available\n\nNo viscosity data exists in the ThermoML database for the ternary mixture of dimethylformamide (DMF) + water + acetonitrile at 298 K (or any other temperature). However, comprehensive binary viscosity data for all three constituent pairs are available, enabling a well-grounded estimate.\n\n---\n\n### Estimation from Binary Subsystem Data\n\n#### Pure Component Viscosities at 298.15 K (from ThermoML)\n\n| Component | η (Pa·s) | Source |\n|-----------|----------|--------|\n| DMF | 0.0008045 | DOI 10.1021/je300608v (GLOBlit_9900, PROPblock_3) |\n| Water | 0.0008903 | DOI 10.1021/je300608v (GLOBlit_9900, PROPblock_3) |\n| Acetonitrile | 0.0003417 | DOI 10.1016/j.jct.2005.08.009 (GLOBlit_2602, PROPblock_3) |\n\n#### Binary Mixture Viscosities at ~Equimolar Composition, 298.15 K\n\n| Binary pair | Composition | η (Pa·s) | Source |\n|-------------|-------------|----------|--------|\n| DMF + Water | x(water) = 0.5 | 0.0018528 | DOI 10.1021/je300608v (GLOBlit_9900, PROPblock_3) |\n| DMF + Acetonitrile | x(DMF) = 0.5029 | 0.00061 | DOI 10.1021/acs.jced.8b00176 (GLOBlit_7481, PROPblock_18) |\n| Water + Acetonitrile | x(ACN) = 0.5204 | 0.0005387 | DOI 10.1016/j.jct.2005.08.009 (GLOBlit_2602, PROPblock_3) |\n\n---\n\n### Estimation Method: Grunberg–Nissan with Binary Interaction Parameters\n\nThe Grunberg–Nissan equation for a ternary mixture is:\n\n**ln(η_mix) = x₁ ln(η₁) + x₂ ln(η₂) + x₃ ln(η₃) + x₁x₂ G₁₂ + x₁x₃ G₁₃ + x₂x₃ G₂₃**\n\nwhere the binary interaction parameters G_ij capture deviations from ideal (Arrhenius) mixing and are extracted from the measured binary data at equimolar composition:\n\n**G_ij = [ln(η_binary) − x_i ln(η_i) − x_j ln(η_j)] / (x_i · x_j)**\n\n#### Extracted Binary Interaction Parameters\n\n| Pair (i–j) | G_ij | Physical meaning |\n|------------|------|-----------------|\n| DMF–Water (1–2) | **+3.14** | Very strong positive deviation — extensive H-bonding |\n| DMF–Acetonitrile (1–3) | **+0.59** | Weak positive deviation — mild dipolar interactions |\n| Water–Acetonitrile (2–3) | **≈ −0.01** | Essentially ideal — minimal specific interactions |\n\n#### Calculation for x(DMF) = x(Water) = x(ACN) = 1/3\n\n- **Ideal (Arrhenius) contribution:**\n  (1/3) × ln(0.0008045) + (1/3) × ln(0.0008903) + (1/3) × ln(0.0003417) = −7.376\n\n- **Excess (interaction) contribution:**\n  (1/9) × (3.14 + 0.59 − 0.01) = (1/9) × 3.72 = +0.413\n\n- **Total:** ln(η_mix) = −7.376 + 0.413 = **−6.963**\n\n- **η_mix = exp(−6.963) ≈ 0.00095 Pa·s ≈ 0.95 mPa·s**\n\n---\n\n### Result Summary\n\n| Estimate | η (Pa·s) | η (mPa·s) |\n|----------|----------|------------|\n| Ideal Arrhenius (no interactions) | ~0.00063 | ~0.63 |\n| **Grunberg–Nissan (with binary interactions)** | **~0.00095** | **~0.95** |\n\n**Best estimate: η ≈ 0.95 mPa·s (0.00095 Pa·s) at 298.15 K**\n\n---\n\n### Chemical Basis of the Estimate\n\n1. **DMF–Water interaction dominates the excess viscosity.** The DMF + water binary exhibits a dramatic viscosity maximum at x(DMF) ≈ 0.3, reaching 0.0024775 Pa·s — roughly 3× the viscosity of either pure component. This arises from strong hydrogen bonding between water's O–H groups and DMF's carbonyl (C=O) group, which creates structured, long-lived molecular associations that resist flow. The large positive G₁₂ = 3.14 captures this effect. Even at the ternary equimolar composition (where each binary pair is \"diluted\" by the third component), this interaction raises the mixture viscosity well above the ideal prediction.\n\n2. **DMF–Acetonitrile interaction is weak.** Both are aprotic solvents, so no strong hydrogen bonding occurs. The binary viscosity increases nearly monotonically from pure acetonitrile (0.00034 Pa·s) to pure DMF (0.00081 Pa·s) with only a mild positive deviation (G₁₃ ≈ 0.59), attributable to dipole–dipole interactions between DMF (μ ≈ 3.8 D) and acetonitrile (μ ≈ 3.9 D).\n\n3. **Water–Acetonitrile interaction is nearly ideal at equimolar composition.** Although a tiny viscosity maximum (0.0009849 Pa·s) appears at very low acetonitrile content (x_ACN ≈ 0.051), the equimolar binary viscosity (0.0005387 Pa·s) is almost exactly what ideal mixing predicts (G₂₃ ≈ 0). This reflects the well-known microheterogeneity of water–acetonitrile mixtures: at intermediate compositions, the two solvents partially segregate into water-rich and acetonitrile-rich domains rather than forming strong cross-associations.\n\n4. **Net effect in the ternary mixture.** The estimated viscosity of ~0.95 mPa·s is about 50% higher than the ideal Arrhenius prediction (~0.63 mPa·s). The enhancement is almost entirely driven by DMF–water hydrogen bonding. The value falls between the pure water viscosity (0.89 mPa·s) and the DMF–water binary maximum (2.48 mPa·s), which is physically reasonable: the presence of acetonitrile (a low-viscosity, non-hydrogen-bonding diluent) disrupts some of the DMF–water associations, preventing the mixture from reaching the extreme viscosities seen in the DMF–water binary.\n\n### Caveats\n\n- This estimate assumes that ternary interaction terms (x₁x₂x₃ contributions) are negligible. In systems with strong specific interactions like DMF–water, ternary terms can be significant, potentially shifting the result by ±10–20%.\n- The Grunberg–Nissan parameters were extracted at approximately equimolar binary compositions; composition-dependent G_ij values would improve accuracy.\n- No experimental ternary viscosity data exist in ThermoML to validate this estimate.\n\n### Data Sources\n\n| Binary system | DOI | Literature ID | Block |\n|---------------|-----|---------------|-------|\n| DMF + Water | 10.1021/je300608v | GLOBlit_9900 | PROPblock_3 |\n| DMF + Water | 10.1021/je050209y | GLOBlit_8676 | PROPblock_9 |\n| DMF + Acetonitrile | 10.1021/acs.jced.8b00176 | GLOBlit_7481 | PROPblock_18 |\n| DMF + Acetonitrile | 10.1016/j.jct.2014.02.019 | GLOBlit_4124 | PROPblock_6 |\n| Water + Acetonitrile | 10.1016/j.jct.2005.08.009 | GLOBlit_2602 | PROPblock_3 |",
  "core_claims": [
    "No viscosity data exists in the ThermoML database for the ternary mixture of dimethylformamide (DMF) + water + acetonitrile at 298 K.",
    "Using the Grunberg–Nissan equation with binary interaction parameters extracted from ThermoML binary viscosity data, the estimated viscosity of the equimolar ternary mixture at 298.15 K is ~0.95 mPa·s (0.00095 Pa·s).",
    "The DMF–water binary interaction dominates the excess viscosity (G₁₂ = +3.14), arising from strong hydrogen bonding between water and DMF's carbonyl group; the DMF–acetonitrile interaction is weak (G₁₃ ≈ +0.59), and the water–acetonitrile interaction at equimolar composition is essentially ideal (G₂₃ ≈ −0.01).",
    "The estimated ternary viscosity (~0.95 mPa·s) is about 50% higher than the ideal Arrhenius prediction (~0.63 mPa·s), with the enhancement almost entirely driven by DMF–water hydrogen bonding.",
    "The estimate assumes negligible ternary interaction terms (x₁x₂x₃ contributions); in systems with strong specific interactions like DMF–water, such terms could shift the result by ±10–20%, and no experimental ternary data exist in ThermoML to validate the estimate."
  ],
  "confidence": "medium",
  "sources": [
    {
      "doi": "10.1021/je300608v",
      "lit_num_id": "GLOBlit_9900",
      "block": "PROPblock_3",
      "BLKsubsys_id": null,
      "description": "Provides binary DMF + water viscosity data at 298.15 K across the full mole fraction range (0–1), including the equimolar point (~0.00185 Pa·s) and pure-component values for DMF and water used to extract the Grunberg–Nissan interaction parameter G₁₂ = 3.14."
    },
    {
      "doi": "10.1021/je050209y",
      "lit_num_id": "GLOBlit_8676",
      "block": "PROPblock_9",
      "BLKsubsys_id": null,
      "description": "Provides an independent set of DMF + water binary viscosity data at 298.15 K (11 points, x = 0.05–0.95), serving as corroboration for the primary DMF–water source and confirming the viscosity maximum near x(DMF) ≈ 0.3."
    },
    {
      "doi": "10.1021/acs.jced.8b00176",
      "lit_num_id": "GLOBlit_7481",
      "block": "PROPblock_18",
      "BLKsubsys_id": null,
      "description": "Provides binary DMF + acetonitrile viscosity data at 298.15 K over the full mole fraction range, including the equimolar value (~0.00061 Pa·s) used to extract the Grunberg–Nissan interaction parameter G₁₃ = 0.59."
    },
    {
      "doi": "10.1016/j.jct.2014.02.019",
      "lit_num_id": "GLOBlit_4124",
      "block": "PROPblock_6",
      "BLKsubsys_id": null,
      "description": "Provides corroborating binary DMF + acetonitrile viscosity data at 298.15 K (mass fraction basis), confirming the viscosity range (0.000293–0.000799 Pa·s) consistent with the primary DMF–acetonitrile source."
    },
    {
      "doi": "10.1016/j.jct.2005.08.009",
      "lit_num_id": "GLOBlit_2602",
      "block": "PROPblock_3",
      "BLKsubsys_id": null,
      "description": "Provides binary water + acetonitrile viscosity data at 298.15 K across the full mole fraction range, including the equimolar value (~0.000539 Pa·s) and the pure acetonitrile viscosity (0.0003417 Pa·s) used to extract the Grunberg–Nissan interaction parameter G₂₃ ≈ −0.01."
    }
  ],
  "follow_up_suggestions": [
    "Search for experimental ternary viscosity data for DMF + water + acetonitrile in other databases (e.g., Dortmund Data Bank) to validate the Grunberg–Nissan estimate.",
    "Investigate composition-dependent Grunberg–Nissan interaction parameters for the DMF + water binary to improve accuracy across the full composition range.",
    "Consider measuring the ternary viscosity experimentally, as the strong DMF–water hydrogen bonding may produce significant ternary interaction terms not captured by binary-only models."
  ],
  "id_catalog_snapshot": []
}

---

## Data Inspections (deterministic evidence ledger)

Hardcoded envelope merge — not agent-authored. 5 entr(ies); verbatim rows below.

- INSP_469970d3baa4 — GLOBlit_8676::PROPblock_9 · complete · 11 rows
- INSP_223a0880d59c — GLOBlit_9900::PROPblock_3 · rdp · 12 rows
- INSP_5ce79feb1bd5 — GLOBlit_4124::PROPblock_6 · complete · 5 rows
- INSP_fbc270263cf3 — GLOBlit_7481::PROPblock_18 · complete · 11 rows
- INSP_98abce7cba9c — GLOBlit_2602::PROPblock_3 · rdp · 13 rows

```json
[
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
    "doi": "10.1016/j.jct.2014.02.019",
    "block_number": "PROPblock_6",
    "table_mode": "complete",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mass_fraction_<dimethylformamide>",
      "pressure_kpa",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "298.15",
        "mass_fraction_<dimethylformamide>": "0",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.000342"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "temperature_k": "298.15",
        "mass_fraction_<dimethylformamide>": "0.25",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0003959"
      },
      {
        "BLKpoint_id": "BLKpoint_9",
        "temperature_k": "298.15",
        "mass_fraction_<dimethylformamide>": "0.5",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0005214"
      },
      {
        "BLKpoint_id": "BLKpoint_13",
        "temperature_k": "298.15",
        "mass_fraction_<dimethylformamide>": "0.75",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0006465"
      },
      {
        "BLKpoint_id": "BLKpoint_17",
        "temperature_k": "298.15",
        "mass_fraction_<dimethylformamide>": "1",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0007986"
      }
    ],
    "inspection_id": "INSP_5ce79feb1bd5",
    "lit_num_id": "GLOBlit_4124"
  },
  {
    "doi": "10.1021/acs.jced.8b00176",
    "block_number": "PROPblock_18",
    "table_mode": "complete",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<dimethylformamide>",
      "pressure_kpa",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "298.15",
        "mole_fraction_<dimethylformamide>": "0",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00034"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "temperature_k": "298.15",
        "mole_fraction_<dimethylformamide>": "0.0989",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.0004"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "temperature_k": "298.15",
        "mole_fraction_<dimethylformamide>": "0.1916",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00044"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "temperature_k": "298.15",
        "mole_fraction_<dimethylformamide>": "0.2925",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00048"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "temperature_k": "298.15",
        "mole_fraction_<dimethylformamide>": "0.3932",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00054"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "temperature_k": "298.15",
        "mole_fraction_<dimethylformamide>": "0.5029",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00061"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "temperature_k": "298.15",
        "mole_fraction_<dimethylformamide>": "0.6002",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00065"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "temperature_k": "298.15",
        "mole_fraction_<dimethylformamide>": "0.6931",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00069"
      },
      {
        "BLKpoint_id": "BLKpoint_9",
        "temperature_k": "298.15",
        "mole_fraction_<dimethylformamide>": "0.7926",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00075"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "temperature_k": "298.15",
        "mole_fraction_<dimethylformamide>": "0.8996",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00079"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "temperature_k": "298.15",
        "mole_fraction_<dimethylformamide>": "1",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00081"
      }
    ],
    "inspection_id": "INSP_fbc270263cf3",
    "lit_num_id": "GLOBlit_7481"
  },
  {
    "doi": "10.1016/j.jct.2005.08.009",
    "block_number": "PROPblock_3",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<acetonitrile>",
      "pressure_kpa",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "298.15",
        "mole_fraction_<acetonitrile>": "0",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0008901"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "temperature_k": "298.15",
        "mole_fraction_<acetonitrile>": "0.051",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0009849"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "temperature_k": "298.15",
        "mole_fraction_<acetonitrile>": "0.1169",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0009567"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "temperature_k": "298.15",
        "mole_fraction_<acetonitrile>": "0.1971",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0008743"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "temperature_k": "298.15",
        "mole_fraction_<acetonitrile>": "0.4417",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0006061"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "temperature_k": "298.15",
        "mole_fraction_<acetonitrile>": "0.5204",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0005387"
      },
      {
        "BLKpoint_id": "BLKpoint_9",
        "temperature_k": "298.15",
        "mole_fraction_<acetonitrile>": "0.6012",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0004802"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "temperature_k": "298.15",
        "mole_fraction_<acetonitrile>": "0.6671",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0004415"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "temperature_k": "298.15",
        "mole_fraction_<acetonitrile>": "0.7398",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0004064"
      },
      {
        "BLKpoint_id": "BLKpoint_12",
        "temperature_k": "298.15",
        "mole_fraction_<acetonitrile>": "0.8253",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0003722"
      },
      {
        "BLKpoint_id": "BLKpoint_13",
        "temperature_k": "298.15",
        "mole_fraction_<acetonitrile>": "0.886",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0003561"
      },
      {
        "BLKpoint_id": "BLKpoint_14",
        "temperature_k": "298.15",
        "mole_fraction_<acetonitrile>": "0.9389",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0003478"
      },
      {
        "BLKpoint_id": "BLKpoint_16",
        "temperature_k": "298.15",
        "mole_fraction_<acetonitrile>": "1",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0003417"
      }
    ],
    "inspection_id": "INSP_98abce7cba9c",
    "lit_num_id": "GLOBlit_2602"
  }
]
```
