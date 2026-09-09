# Q4.5 — Result

**Prompt:** How strongly does water + ethylene glycol deviate from ideal mixing in its transport properties, and what's the chemical reason behind?

**Tool calls:** 2  |  **Time:** 390.8s  |  **Iterations:** 3  |  **Timed out:** False

---

## Answer

{
  "answer": "## Non-Ideal Transport Properties of Water + Ethylene Glycol Mixtures\n\nThe water + ethylene glycol (1,2-ethanediol) binary system shows **strongly non-ideal mixing** in its transport properties, and the ThermoML database provides both viscosity and thermodynamic data that quantify and explain this behavior.\n\n---\n\n### 1. Dynamic Viscosity — Large Positive Deviations\n\nFrom **GLOBlit_6951::PROPblock_18** (DOI: 10.1021/acs.jced.6b00526), 33 data points were measured by falling/rolling sphere viscometry at 100.0 kPa across the full composition range.\n\n**Viscosity across composition at 293.15 K:**\n\n| x(water) | Viscosity (Pa·s) |\n|-----------|-----------------|\n| 0 (pure EG) | 0.02113 |\n| 0.2014 | 0.01495 |\n| 0.4011 | 0.01005 |\n| 0.6995 | 0.004584 |\n| 1.0 (pure water) | 0.000949 |\n\n**At 298.15 K:**\n\n| x(water) | Viscosity (Pa·s) |\n|-----------|-----------------|\n| 0 (pure EG) | 0.01724 |\n| 0.2014 | 0.01219 |\n| 0.4011 | 0.00831 |\n| 0.6995 | 0.003884 |\n| 1.0 (pure water) | 0.000843 |\n\n**At 303.15 K:**\n\n| x(water) | Viscosity (Pa·s) |\n|-----------|-----------------|\n| 0 (pure EG) | 0.01423 |\n| 0.2014 | 0.01014 |\n| 0.4969 | 0.005653 |\n| 1.0 (pure water) | 0.000755 |\n\n#### How large is the deviation?\n\nPure ethylene glycol is roughly **22× more viscous** than pure water at 293.15 K (0.02113 vs. 0.000949 Pa·s; ratio derived from the two endpoint values). Under a log-linear (Arrhenius) ideal mixing rule, the viscosity at x(water) = 0.4011 would be approximately 0.006 Pa·s (derived: exp[0.5989 × ln(0.02113) + 0.4011 × ln(0.000949)]). The **measured value is 0.01005 Pa·s** — a substantial **positive deviation of roughly +65%** above the ideal estimate. This means the mixture is significantly more viscous than one would predict from a simple interpolation between the pure-component values.\n\nTemperature strongly reduces viscosity at all compositions: pure EG drops from 0.02113 Pa·s at 293.15 K to 0.01423 Pa·s at 303.15 K — about a 33% decrease over just 10 K (derived from the inspected endpoint values).\n\n---\n\n### 2. Excess Molar Enthalpy — Thermodynamic Confirmation\n\nFrom **GLOBlit_5843::PROPblock_1** (DOI: 10.1016/j.tca.2009.06.004), 13 Calvet calorimetry data points at 298.15 K and 101.0 kPa:\n\n| x(water) | Hᴱ (kJ/mol) |\n|-----------|-------------|\n| 0.1014 | −0.174 |\n| 0.1994 | −0.337 |\n| 0.2091 | −0.347 |\n| 0.3051 | −0.48 |\n| 0.3674 | −0.559 |\n| 0.3995 | −0.59 |\n| 0.4807 | −0.64 |\n| 0.5455 | −0.666 |\n| 0.6144 | −0.698 |\n| 0.669 | **−0.715** |\n| 0.7949 | −0.681 |\n| 0.8656 | −0.57 |\n| 0.915 | −0.423 |\n\nHᴱ is **negative (exothermic) across the entire composition range**, confirming that mixing water and ethylene glycol is energetically favorable. The most exothermic point is **−0.715 kJ/mol at x(water) = 0.669**, corresponding to roughly a **2:1 water-to-EG molar ratio**.\n\n---\n\n### 3. The Chemical Explanation\n\nThe non-ideal transport behavior has a clear molecular origin: **extensive cross-species hydrogen bonding**.\n\n- **Ethylene glycol has two hydroxyl (–OH) groups** on adjacent carbons, making it both a strong hydrogen-bond donor and acceptor. Each –OH group can form hydrogen bonds with water molecules.\n\n- **The Hᴱ minimum at x(water) ≈ 0.67** (a 2:1 water:EG ratio) is chemically significant — it matches the stoichiometry where each of EG's two –OH groups is optimally solvated by one water molecule. This is the composition of maximum cross-interaction.\n\n- **The asymmetry of the Hᴱ curve** (minimum shifted toward the water-rich side rather than at x = 0.5) directly reflects this 2:1 stoichiometry.\n\n- **Why positive excess viscosity?** When water and EG mix, they form a more extensive and structured hydrogen-bond network than exists in either pure component alone. These cross-linked H-bond clusters resist flow more effectively than the individual pure-component networks, producing viscosities that exceed the ideal mixing prediction. The same favorable interactions that release enthalpy (negative Hᴱ) also create more rigid, cooperative molecular structures that increase viscous drag.\n\n- **Why is the Hᴱ magnitude moderate** (|Hᴱ|_max = 0.715 kJ/mol)? Both pure water and pure ethylene glycol already possess extensive hydrogen-bond networks. Mixing requires **partial disruption** of these existing networks before new, favorable water–EG bonds can form. The observed Hᴱ is the net balance: the energy cost of breaking some water–water and EG–EG bonds is partially offset by the energy released from forming water–EG bonds. The net exotherm confirms that the cross-interactions are thermodynamically preferred, but the magnitude is tempered by the disruption cost.\n\n### Summary\n\nThe water + ethylene glycol system deviates strongly from ideal mixing in its viscosity — measured values exceed log-linear ideal predictions by roughly 65% at intermediate compositions. This positive excess viscosity is driven by the formation of extensive cross-species hydrogen-bond networks, thermodynamically confirmed by uniformly negative excess molar enthalpies peaking at −0.715 kJ/mol near a 2:1 water:EG molar ratio that matches the stoichiometry of EG's two hydroxyl groups.",
  "core_claims": [
    "The water + ethylene glycol binary system exhibits strongly non-ideal mixing in its transport properties, with measured dynamic viscosities showing large positive deviations above log-linear (Arrhenius) ideal mixing predictions — approximately +65% at intermediate compositions near x(water) ≈ 0.4 at 293.15 K.",
    "Pure ethylene glycol is roughly 22× more viscous than pure water at 293.15 K (0.02113 vs. 0.000949 Pa·s), and temperature strongly reduces viscosity at all compositions, with pure EG dropping from 0.02113 Pa·s at 293.15 K to 0.01423 Pa·s at 303.15 K.",
    "Excess molar enthalpy (Hᴱ) at 298.15 K is negative (exothermic) across the entire composition range, with a minimum of −0.715 kJ/mol at x(water) = 0.669, corresponding to a roughly 2:1 water-to-EG molar ratio consistent with the stoichiometry of EG's two hydroxyl groups.",
    "The asymmetry of the Hᴱ curve, with its minimum shifted toward the water-rich side rather than at x = 0.5, reflects the 2:1 stoichiometry where each of EG's two –OH groups is optimally solvated by one water molecule.",
    "The positive excess viscosity is attributed to extensive cross-species hydrogen bonding between water and ethylene glycol, forming a more structured hydrogen-bond network than in either pure component, which resists flow more effectively and is thermodynamically confirmed by the uniformly negative Hᴱ values."
  ],
  "confidence": "medium",
  "sources": [
    {
      "doi": "10.1021/acs.jced.6b00526",
      "lit_num_id": "GLOBlit_6951",
      "block": "PROPblock_18",
      "BLKsubsys_id": null,
      "description": "Provides 33 dynamic viscosity data points for the water + 1,2-ethanediol binary system across the full mole-fraction range (0–1) at 293.15–303.15 K and 100.0 kPa, which the answer uses to demonstrate large positive deviations from ideal mixing (~65% excess viscosity at intermediate compositions)."
    },
    {
      "doi": "10.1016/j.tca.2009.06.004",
      "lit_num_id": "GLOBlit_5843",
      "block": "PROPblock_1",
      "BLKsubsys_id": null,
      "description": "Provides 13 excess molar enthalpy measurements for the water + 1,2-ethanediol binary at 298.15 K and 101.0 kPa, showing uniformly negative values with a minimum of −0.715 kJ/mol near x(water) = 0.669, which the answer uses to thermodynamically confirm the strong cross-species hydrogen bonding that drives the non-ideal viscosity behavior."
    }
  ],
  "follow_up_suggestions": [
    "How does the excess viscosity of water + ethylene glycol compare quantitatively to water + propylene glycol or water + glycerol systems?",
    "Is there ThermoML data on the diffusion coefficients of water + ethylene glycol mixtures to further characterize transport non-ideality?",
    "How does the excess molar volume of water + ethylene glycol correlate with the excess viscosity across composition?"
  ],
  "id_catalog_snapshot": []
}

---

## Data Inspections (deterministic evidence ledger)

Hardcoded envelope merge — not agent-authored. 3 entr(ies); verbatim rows below.

- INSP_bdb58d28aae5 — GLOBlit_6951::PROPblock_18 · rdp · 14 rows
- INSP_2c1af1f114b2 — GLOBlit_5843::PROPblock_1 · rdp · 8 rows
- INSP_8383e8943328 — GLOBlit_5843::PROPblock_1 · complete · 8 rows

```json
[
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
    "doi": "10.1016/j.tca.2009.06.004",
    "block_number": "PROPblock_1",
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
        "mole_fraction_<water>": "0.1014",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.174"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "mole_fraction_<water>": "0.1994",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.337"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "mole_fraction_<water>": "0.3995",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.59"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "mole_fraction_<water>": "0.4807",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.64"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "mole_fraction_<water>": "0.669",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.715"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "mole_fraction_<water>": "0.7949",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.681"
      },
      {
        "BLKpoint_id": "BLKpoint_12",
        "mole_fraction_<water>": "0.8656",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.57"
      },
      {
        "BLKpoint_id": "BLKpoint_13",
        "mole_fraction_<water>": "0.915",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.423"
      }
    ],
    "inspection_id": "INSP_2c1af1f114b2",
    "lit_num_id": "GLOBlit_5843"
  },
  {
    "doi": "10.1016/j.tca.2009.06.004",
    "block_number": "PROPblock_1",
    "table_mode": "complete",
    "columns": [
      "BLKpoint_id",
      "mole_fraction_<water>",
      "temperature_k",
      "pressure_kpa",
      "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_3",
        "mole_fraction_<water>": "0.2091",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.347"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "mole_fraction_<water>": "0.3051",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.48"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "mole_fraction_<water>": "0.3674",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.559"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "mole_fraction_<water>": "0.3995",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.59"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "mole_fraction_<water>": "0.4807",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.64"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "mole_fraction_<water>": "0.5455",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.666"
      },
      {
        "BLKpoint_id": "BLKpoint_9",
        "mole_fraction_<water>": "0.6144",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.698"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "mole_fraction_<water>": "0.669",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.715"
      }
    ],
    "inspection_id": "INSP_8383e8943328",
    "lit_num_id": "GLOBlit_5843"
  }
]
```
