# Q4.2 — Result

**Prompt:** Does the nonideality of alcohol + water mixtures grow with the alcohol chain length?

**Tool calls:** 4  |  **Time:** 931.6s  |  **Iterations:** 5  |  **Timed out:** False

---

## Answer

{
  "answer": "## Does the Nonideality of Alcohol + Water Mixtures Grow with Alcohol Chain Length?\n\nThis is a classic question in solution thermodynamics. Using excess molar enthalpy (Hᴱ) as a measure of nonideality, the ThermoML database provides data for two alcohol + water binary systems at 298.15 K and 101.0 kPa, allowing a partial but informative comparison.\n\n---\n\n### Available Data\n\n#### Methanol + Water (DOI: 10.1016/j.tca.2006.02.028, GLOBlit_5688 :: PROPblock_1)\n- **Method:** Titration calorimetry, T = 298.15 K, P = 101.0 kPa\n- Entirely exothermic (negative Hᴱ) across the full composition range\n- **Minimum Hᴱ = −0.850 kJ/mol** at x(methanol) ≈ 0.3\n- Hᴱ at x = 0.5: **−0.777 kJ/mol**\n\n| x(methanol) | Hᴱ (kJ/mol) |\n|:-----------:|:------------:|\n| 0.05 | −0.326 |\n| 0.15 | −0.714 |\n| 0.20 | −0.806 |\n| 0.30 | −0.850 |\n| 0.40 | −0.841 |\n| 0.50 | −0.777 |\n| 0.70 | −0.583 |\n| 0.90 | −0.241 |\n\n#### Ethanol + Water (DOI: 10.1016/j.jct.2005.06.018, GLOBlit_2574 :: PROPblock_4)\n- **Method:** Calvet calorimetry, T = 298.15 K, P = 101.0 kPa\n- Entirely exothermic (negative Hᴱ) across the full composition range\n- **Minimum Hᴱ = −0.77 kJ/mol** at x(ethanol) ≈ 0.15\n- Hᴱ at x = 0.5: **−0.391 kJ/mol**\n\n| x(ethanol) | Hᴱ (kJ/mol) |\n|:----------:|:------------:|\n| 0.0582 | −0.492 |\n| 0.1198 | −0.747 |\n| 0.15 | −0.77 |\n| 0.1837 | −0.767 |\n| 0.25 | −0.702 |\n| 0.2981 | −0.649 |\n| 0.4127 | −0.501 |\n| 0.50 | −0.391 |\n| 0.701 | −0.271 |\n| 0.90 | −0.148 |\n\n#### 1-Propanol + Water and Longer Chains\n**No binary Hᴱ data** for 1-propanol + water (or any longer-chain alcohol + water) were found in the ThermoML database, despite extensive coverage of other properties (density, VLE, heat capacity, etc.) for the 1-propanol + water pair.\n\n---\n\n### Summary Comparison at 298.15 K, 101.0 kPa\n\n| System | Min Hᴱ (kJ/mol) | x(alcohol) at minimum | Hᴱ at x = 0.5 (kJ/mol) | Source |\n|--------|:-----------------:|:---------------------:|:-----------------------:|--------|\n| Methanol + water | −0.850 | ≈ 0.3 | −0.777 | GLOBlit_5688 :: PROPblock_1 |\n| Ethanol + water | −0.77 | ≈ 0.15 | −0.391 | GLOBlit_2574 :: PROPblock_4 |\n| 1-Propanol + water | — | — | — | Not found in database |\n\n---\n\n### Interpretation\n\nThe comparison between methanol and ethanol reveals a nuanced picture:\n\n1. **The minimum Hᴱ values are comparable in magnitude** (−0.850 vs −0.77 kJ/mol), so the *peak* exothermic interaction does not increase dramatically from C₁ to C₂.\n\n2. **The Hᴱ curve becomes markedly more asymmetric with increasing chain length.** The minimum shifts from x ≈ 0.3 (methanol) to x ≈ 0.15 (ethanol) — further toward the water-rich side. This means the strongest enthalpic interactions occur at increasingly dilute alcohol concentrations as the alkyl chain grows.\n\n3. **At equimolar composition (x = 0.5), the nonideality actually *decreases* from methanol to ethanol** (−0.777 vs −0.391 kJ/mol). This reflects the fact that at higher alcohol mole fractions, the longer-chain ethanol disrupts the water hydrogen-bond network so thoroughly that the exothermic contribution from forming alcohol–water hydrogen bonds is diminished.\n\n4. **The growing asymmetry is the key signature of increasing hydrophobic character.** As the alkyl chain lengthens, the hydrophobic moiety increasingly disrupts the cooperative water hydrogen-bond network. At low alcohol concentrations, water can accommodate the solute (hydrophobic hydration), producing strong exothermic effects. At higher concentrations, the water structure is overwhelmed, and the mixing becomes less exothermic.\n\nIn summary, the data available in the ThermoML database show that nonideality in alcohol + water mixtures does evolve with chain length, but in a composition-dependent way: the Hᴱ curve becomes more asymmetric and its minimum shifts to lower alcohol mole fractions. The peak |Hᴱ| values are similar for methanol and ethanol, but the overall shape of the curve changes dramatically, reflecting the growing importance of hydrophobic interactions. A complete chain-length series (including 1-propanol and beyond) could not be constructed from the database, as binary Hᴱ data for 1-propanol + water are not available in ThermoML.",
  "core_claims": [
    "At 298.15 K and 101.0 kPa, the minimum excess molar enthalpy (Hᴱ) for methanol + water is −0.850 kJ/mol at x(methanol) ≈ 0.3, while for ethanol + water it is −0.77 kJ/mol at x(ethanol) ≈ 0.15, indicating comparable peak magnitudes but a shift of the minimum toward lower alcohol mole fractions with increasing chain length.",
    "At equimolar composition (x = 0.5), Hᴱ is −0.777 kJ/mol for methanol + water and −0.391 kJ/mol for ethanol + water, showing that at this composition the exothermic nonideality decreases from methanol to ethanol.",
    "The Hᴱ curve becomes markedly more asymmetric from methanol to ethanol, with the minimum shifting to lower alcohol mole fractions, reflecting the growing importance of hydrophobic interactions as alkyl chain length increases.",
    "No binary Hᴱ data for 1-propanol + water or any longer-chain alcohol + water were found in the ThermoML database, preventing construction of a complete chain-length series."
  ],
  "confidence": "medium",
  "sources": [
    {
      "doi": "10.1016/j.tca.2006.02.028",
      "lit_num_id": "GLOBlit_5688",
      "block": "PROPblock_1",
      "BLKsubsys_id": null,
      "description": "Provides excess molar enthalpy data for methanol + water at 298.15 K and 101.0 kPa across the full composition range, with a minimum Hᴱ of −0.85 kJ/mol near x ≈ 0.3, serving as the C₁ alcohol baseline for the chain-length comparison."
    },
    {
      "doi": "10.1016/j.jct.2005.06.018",
      "lit_num_id": "GLOBlit_2574",
      "block": "PROPblock_4",
      "BLKsubsys_id": null,
      "description": "Provides excess molar enthalpy data for ethanol + water including 298.15 K at 101.0 kPa, with a minimum Hᴱ of −0.77 kJ/mol near x ≈ 0.15, serving as the C₂ alcohol data point and enabling direct comparison of Hᴱ curve shape and asymmetry with the methanol + water system."
    }
  ],
  "follow_up_suggestions": [
    "Search for excess molar enthalpy data for 1-propanol + water and 1-butanol + water in other thermodynamic databases (e.g., NIST TDE, Dortmund Data Bank) to extend the chain-length comparison beyond ethanol.",
    "Examine excess molar volume (Vᴱ) data for the methanol/ethanol/1-propanol + water series in ThermoML as an alternative nonideality measure, since volumetric data may be more widely available than calorimetric data.",
    "Compare activity coefficient data (γ∞ at infinite dilution) for the homologous alcohol series in water to quantify the monotonic increase in hydrophobic nonideality with chain length."
  ],
  "id_catalog_snapshot": [
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

- INSP_6bf554d45167 — GLOBlit_5688::PROPblock_1 · rdp · 10 rows
- INSP_2eac99beae5d — GLOBlit_2520::PROPblock_3 · nearest · 5 rows
- INSP_e0e7d5bc600c — GLOBlit_528::PROPblock_1 · rdp · 12 rows
- INSP_b146b18bf0c3 — GLOBlit_528::PROPblock_2 · rdp · 11 rows
- INSP_62d83367dded — GLOBlit_2574::PROPblock_1 · complete · 12 rows
- INSP_6d19d0a7d0d6 — GLOBlit_2574::PROPblock_4 · complete · 12 rows
- INSP_78268b3f306d — GLOBlit_5688::PROPblock_1 · nearest · 1 rows
- INSP_6b232fc9d0f6 — GLOBlit_1766::PROPblock_1 · rdp · 39 rows

```json
[
  {
    "doi": "10.1016/j.tca.2006.02.028",
    "block_number": "PROPblock_1",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "mole_fraction_<methanol>",
      "temperature_k",
      "pressure_kpa",
      "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "mole_fraction_<methanol>": "0",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "mole_fraction_<methanol>": "0.05",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.326"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "mole_fraction_<methanol>": "0.15",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.714"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "mole_fraction_<methanol>": "0.2",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.806"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "mole_fraction_<methanol>": "0.3",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.85"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "mole_fraction_<methanol>": "0.4",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.841"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "mole_fraction_<methanol>": "0.5",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.777"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "mole_fraction_<methanol>": "0.7",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.583"
      },
      {
        "BLKpoint_id": "BLKpoint_12",
        "mole_fraction_<methanol>": "0.9",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.241"
      },
      {
        "BLKpoint_id": "BLKpoint_13",
        "mole_fraction_<methanol>": "1",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0"
      }
    ],
    "inspection_id": "INSP_6bf554d45167",
    "lit_num_id": "GLOBlit_5688"
  },
  {
    "doi": "10.1016/j.jct.2005.03.012",
    "block_number": "PROPblock_3",
    "table_mode": "nearest",
    "columns": [
      "BLKpoint_id",
      "pressure_kpa",
      "mole_fraction_<methanol>",
      "temperature_k",
      "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_113",
        "pressure_kpa": "5000",
        "mole_fraction_<methanol>": "0.5",
        "temperature_k": "323.15",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.6592"
      },
      {
        "BLKpoint_id": "BLKpoint_114",
        "pressure_kpa": "5000",
        "mole_fraction_<methanol>": "0.5",
        "temperature_k": "325.16",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.6406"
      },
      {
        "BLKpoint_id": "BLKpoint_115",
        "pressure_kpa": "5000",
        "mole_fraction_<methanol>": "0.5",
        "temperature_k": "330.5",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.6011"
      },
      {
        "BLKpoint_id": "BLKpoint_116",
        "pressure_kpa": "5000",
        "mole_fraction_<methanol>": "0.5",
        "temperature_k": "332.3",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.5838"
      },
      {
        "BLKpoint_id": "BLKpoint_117",
        "pressure_kpa": "5000",
        "mole_fraction_<methanol>": "0.5",
        "temperature_k": "348.15",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.4457"
      }
    ],
    "inspection_id": "INSP_2eac99beae5d",
    "lit_num_id": "GLOBlit_2520"
  },
  {
    "doi": "10.1016/j.fluid.2007.06.007",
    "block_number": "PROPblock_1",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "mole_fraction_<ethanol>",
      "temperature_k",
      "pressure_kpa",
      "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "mole_fraction_<ethanol>": "0.000102",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.00104"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "mole_fraction_<ethanol>": "0.000206",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.00208"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "mole_fraction_<ethanol>": "0.000308",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.00312"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "mole_fraction_<ethanol>": "0.000516",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.00518"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "mole_fraction_<ethanol>": "0.000619",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.00621"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "mole_fraction_<ethanol>": "0.000723",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.00722"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "mole_fraction_<ethanol>": "0.000827",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.00826"
      },
      {
        "BLKpoint_id": "BLKpoint_9",
        "mole_fraction_<ethanol>": "0.000931",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.00927"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "mole_fraction_<ethanol>": "0.001034",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.0103"
      },
      {
        "BLKpoint_id": "BLKpoint_12",
        "mole_fraction_<ethanol>": "0.001241",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.01233"
      },
      {
        "BLKpoint_id": "BLKpoint_13",
        "mole_fraction_<ethanol>": "0.001345",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.01334"
      },
      {
        "BLKpoint_id": "BLKpoint_15",
        "mole_fraction_<ethanol>": "0.001551",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.01537"
      }
    ],
    "inspection_id": "INSP_e0e7d5bc600c",
    "lit_num_id": "GLOBlit_528"
  },
  {
    "doi": "10.1016/j.fluid.2007.06.007",
    "block_number": "PROPblock_2",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "mole_fraction_<water>",
      "temperature_k",
      "pressure_kpa",
      "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "mole_fraction_<water>": "0.001021",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.00212"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "mole_fraction_<water>": "0.00205",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.00424"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "mole_fraction_<water>": "0.004102",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.00835"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "mole_fraction_<water>": "0.006155",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.01238"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "mole_fraction_<water>": "0.007179",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.01437"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "mole_fraction_<water>": "0.010239",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.02023"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "mole_fraction_<water>": "0.011252",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.02213"
      },
      {
        "BLKpoint_id": "BLKpoint_12",
        "mole_fraction_<water>": "0.012264",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.02405"
      },
      {
        "BLKpoint_id": "BLKpoint_13",
        "mole_fraction_<water>": "0.013276",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.0259"
      },
      {
        "BLKpoint_id": "BLKpoint_14",
        "mole_fraction_<water>": "0.014283",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.02777"
      },
      {
        "BLKpoint_id": "BLKpoint_15",
        "mole_fraction_<water>": "0.015286",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.02961"
      }
    ],
    "inspection_id": "INSP_b146b18bf0c3",
    "lit_num_id": "GLOBlit_528"
  },
  {
    "doi": "10.1016/j.jct.2005.06.018",
    "block_number": "PROPblock_1",
    "table_mode": "complete",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<1,2-propanediol>",
      "pressure_kpa",
      "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "298.15",
        "mole_fraction_<1,2-propanediol>": "0.0266",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.279"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "temperature_k": "298.15",
        "mole_fraction_<1,2-propanediol>": "0.0579",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.562"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "temperature_k": "298.15",
        "mole_fraction_<1,2-propanediol>": "0.1214",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.878"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "temperature_k": "298.15",
        "mole_fraction_<1,2-propanediol>": "0.205",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.97"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "temperature_k": "298.15",
        "mole_fraction_<1,2-propanediol>": "0.304",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.913"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "temperature_k": "298.15",
        "mole_fraction_<1,2-propanediol>": "0.3872",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.837"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "temperature_k": "298.15",
        "mole_fraction_<1,2-propanediol>": "0.4957",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.702"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "temperature_k": "298.15",
        "mole_fraction_<1,2-propanediol>": "0.5454",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.635"
      },
      {
        "BLKpoint_id": "BLKpoint_9",
        "temperature_k": "298.15",
        "mole_fraction_<1,2-propanediol>": "0.6431",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.542"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "temperature_k": "298.15",
        "mole_fraction_<1,2-propanediol>": "0.7386",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.436"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "temperature_k": "298.15",
        "mole_fraction_<1,2-propanediol>": "0.8236",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.325"
      },
      {
        "BLKpoint_id": "BLKpoint_12",
        "temperature_k": "298.15",
        "mole_fraction_<1,2-propanediol>": "0.9233",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.15"
      }
    ],
    "inspection_id": "INSP_62d83367dded",
    "lit_num_id": "GLOBlit_2574"
  },
  {
    "doi": "10.1016/j.jct.2005.06.018",
    "block_number": "PROPblock_4",
    "table_mode": "complete",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<ethanol>",
      "pressure_kpa",
      "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.0582",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.492"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.1198",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.747"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.77"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.1837",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.767"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.25",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.702"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.2981",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.649"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.4127",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.501"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.5",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.391"
      },
      {
        "BLKpoint_id": "BLKpoint_9",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.607",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.323"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.701",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.271"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.812",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.206"
      },
      {
        "BLKpoint_id": "BLKpoint_12",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.9",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.148"
      }
    ],
    "inspection_id": "INSP_6d19d0a7d0d6",
    "lit_num_id": "GLOBlit_2574"
  },
  {
    "doi": "10.1016/j.tca.2006.02.028",
    "block_number": "PROPblock_1",
    "table_mode": "nearest",
    "columns": [
      "BLKpoint_id",
      "mole_fraction_<methanol>",
      "temperature_k",
      "pressure_kpa",
      "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_6",
        "mole_fraction_<methanol>": "0.3",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.85"
      }
    ],
    "inspection_id": "INSP_78268b3f306d",
    "lit_num_id": "GLOBlit_5688"
  },
  {
    "doi": "10.1016/j.fluid.2015.07.053",
    "block_number": "PROPblock_1",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "mole_fraction_<propan-1-ol>",
      "mole_fraction_<acetic acid>",
      "temperature_k",
      "pressure_kpa",
      "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "mole_fraction_<propan-1-ol>": "0.5",
        "mole_fraction_<acetic acid>": "0",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "mole_fraction_<propan-1-ol>": "0.2501",
        "mole_fraction_<acetic acid>": "0.5002",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.312"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "mole_fraction_<propan-1-ol>": "0.2001",
        "mole_fraction_<acetic acid>": "0.5983",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.338"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "mole_fraction_<propan-1-ol>": "0.2397",
        "mole_fraction_<acetic acid>": "0.4813",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.317"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "mole_fraction_<propan-1-ol>": "0.2999",
        "mole_fraction_<acetic acid>": "0.4",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.262"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "mole_fraction_<propan-1-ol>": "0.2",
        "mole_fraction_<acetic acid>": "0.5997",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.33"
      },
      {
        "BLKpoint_id": "BLKpoint_9",
        "mole_fraction_<propan-1-ol>": "0.1508",
        "mole_fraction_<acetic acid>": "0.7017",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.337"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "mole_fraction_<propan-1-ol>": "0.1503",
        "mole_fraction_<acetic acid>": "0.7004",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.335"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "mole_fraction_<propan-1-ol>": "0.1001",
        "mole_fraction_<acetic acid>": "0.8027",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.299"
      },
      {
        "BLKpoint_id": "BLKpoint_13",
        "mole_fraction_<propan-1-ol>": "0.0517",
        "mole_fraction_<acetic acid>": "0.8969",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.192"
      },
      {
        "BLKpoint_id": "BLKpoint_14",
        "mole_fraction_<propan-1-ol>": "0.0533",
        "mole_fraction_<acetic acid>": "0.8918",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.216"
      },
      {
        "BLKpoint_id": "BLKpoint_16",
        "mole_fraction_<propan-1-ol>": "0.3458",
        "mole_fraction_<acetic acid>": "0.2974",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.231"
      },
      {
        "BLKpoint_id": "BLKpoint_17",
        "mole_fraction_<propan-1-ol>": "0.3983",
        "mole_fraction_<acetic acid>": "0.1995",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.186"
      },
      {
        "BLKpoint_id": "BLKpoint_19",
        "mole_fraction_<propan-1-ol>": "0.452",
        "mole_fraction_<acetic acid>": "0.1",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.116"
      },
      {
        "BLKpoint_id": "BLKpoint_22",
        "mole_fraction_<propan-1-ol>": "0.75",
        "mole_fraction_<acetic acid>": "0",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0"
      },
      {
        "BLKpoint_id": "BLKpoint_24",
        "mole_fraction_<propan-1-ol>": "0.6729",
        "mole_fraction_<acetic acid>": "0.101",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.073"
      },
      {
        "BLKpoint_id": "BLKpoint_27",
        "mole_fraction_<propan-1-ol>": "0.5194",
        "mole_fraction_<acetic acid>": "0.2983",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.178"
      },
      {
        "BLKpoint_id": "BLKpoint_29",
        "mole_fraction_<propan-1-ol>": "0.4503",
        "mole_fraction_<acetic acid>": "0.4013",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.232"
      },
      {
        "BLKpoint_id": "BLKpoint_30",
        "mole_fraction_<propan-1-ol>": "0.3752",
        "mole_fraction_<acetic acid>": "0.4998",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.267"
      },
      {
        "BLKpoint_id": "BLKpoint_31",
        "mole_fraction_<propan-1-ol>": "0.2987",
        "mole_fraction_<acetic acid>": "0.5969",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.306"
      },
      {
        "BLKpoint_id": "BLKpoint_32",
        "mole_fraction_<propan-1-ol>": "0.3017",
        "mole_fraction_<acetic acid>": "0.6047",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.31"
      },
      {
        "BLKpoint_id": "BLKpoint_33",
        "mole_fraction_<propan-1-ol>": "0.2263",
        "mole_fraction_<acetic acid>": "0.7066",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.316"
      },
      {
        "BLKpoint_id": "BLKpoint_35",
        "mole_fraction_<propan-1-ol>": "0.1505",
        "mole_fraction_<acetic acid>": "0.7996",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.285"
      },
      {
        "BLKpoint_id": "BLKpoint_36",
        "mole_fraction_<propan-1-ol>": "0.1487",
        "mole_fraction_<acetic acid>": "0.7984",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.283"
      },
      {
        "BLKpoint_id": "BLKpoint_37",
        "mole_fraction_<propan-1-ol>": "0.075",
        "mole_fraction_<acetic acid>": "0.8975",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.194"
      },
      {
        "BLKpoint_id": "BLKpoint_41",
        "mole_fraction_<propan-1-ol>": "0.25",
        "mole_fraction_<acetic acid>": "0",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0"
      },
      {
        "BLKpoint_id": "BLKpoint_42",
        "mole_fraction_<propan-1-ol>": "0.2244",
        "mole_fraction_<acetic acid>": "0.1",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.193"
      },
      {
        "BLKpoint_id": "BLKpoint_44",
        "mole_fraction_<propan-1-ol>": "0.1994",
        "mole_fraction_<acetic acid>": "0.1993",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.287"
      },
      {
        "BLKpoint_id": "BLKpoint_46",
        "mole_fraction_<propan-1-ol>": "0.1719",
        "mole_fraction_<acetic acid>": "0.2924",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.359"
      },
      {
        "BLKpoint_id": "BLKpoint_48",
        "mole_fraction_<propan-1-ol>": "0.1512",
        "mole_fraction_<acetic acid>": "0.3997",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.392"
      },
      {
        "BLKpoint_id": "BLKpoint_49",
        "mole_fraction_<propan-1-ol>": "0.1506",
        "mole_fraction_<acetic acid>": "0.402",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.393"
      },
      {
        "BLKpoint_id": "BLKpoint_50",
        "mole_fraction_<propan-1-ol>": "0.1247",
        "mole_fraction_<acetic acid>": "0.4991",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.412"
      },
      {
        "BLKpoint_id": "BLKpoint_52",
        "mole_fraction_<propan-1-ol>": "0.1065",
        "mole_fraction_<acetic acid>": "0.5911",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.415"
      },
      {
        "BLKpoint_id": "BLKpoint_53",
        "mole_fraction_<propan-1-ol>": "0.0998",
        "mole_fraction_<acetic acid>": "0.5973",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.421"
      },
      {
        "BLKpoint_id": "BLKpoint_54",
        "mole_fraction_<propan-1-ol>": "0.0735",
        "mole_fraction_<acetic acid>": "0.7004",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.402"
      },
      {
        "BLKpoint_id": "BLKpoint_55",
        "mole_fraction_<propan-1-ol>": "0.0754",
        "mole_fraction_<acetic acid>": "0.699",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.4"
      },
      {
        "BLKpoint_id": "BLKpoint_56",
        "mole_fraction_<propan-1-ol>": "0.0487",
        "mole_fraction_<acetic acid>": "0.798",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.347"
      },
      {
        "BLKpoint_id": "BLKpoint_58",
        "mole_fraction_<propan-1-ol>": "0.0261",
        "mole_fraction_<acetic acid>": "0.9054",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.214"
      },
      {
        "BLKpoint_id": "BLKpoint_59",
        "mole_fraction_<propan-1-ol>": "0.0301",
        "mole_fraction_<acetic acid>": "0.8982",
        "temperature_k": "313.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0.223"
      }
    ],
    "inspection_id": "INSP_6b232fc9d0f6",
    "lit_num_id": "GLOBlit_1766"
  }
]
```
