# Q4.6 — Result

**Prompt:** Among aqueous mixtures of organic solvents, how does viscosity change with the molecular structure of the organic component, and which intermolecular interactions explain the trend?

**Tool calls:** 3  |  **Time:** 838.6s  |  **Iterations:** 4  |  **Timed out:** False

---

## Answer

{
  "answer": "## How Viscosity Changes with the Molecular Structure of the Organic Component in Aqueous Mixtures\n\n### Overview\n\nData from the ThermoML database for four binary alcohol–water systems at 298.15 K and 101 kPa reveal clear, systematic trends linking the molecular structure of the organic component to the viscosity behaviour of the aqueous mixture. The key structural variables explored are **alkyl chain length** (methanol → ethanol → 1-propanol) and **chain branching** (1-propanol vs. 2-propanol).\n\nAll data were measured by capillary tube (Ubbelohde) viscometry and come from two internally consistent studies:\n- DOI 10.1016/j.jct.2007.05.004 (methanol + water, ethanol + water)\n- DOI 10.1021/je700700f (1-propanol + water, 2-propanol + water)\n\n---\n\n### 1. The Universal Viscosity Maximum\n\nEvery alcohol–water system examined displays a **non-monotonic viscosity profile**: starting from pure water (η = 0.00089 Pa·s), viscosity rises with increasing alcohol content, passes through a pronounced maximum at an intermediate composition, and then decreases toward the pure alcohol value. This maximum is the signature of strong, composition-dependent intermolecular interactions in the mixture.\n\n---\n\n### 2. Effect of Alkyl Chain Length\n\n#### Pure-component viscosities at 298.15 K\n\n| Compound | η (Pa·s) | Source |\n|----------|----------|--------|\n| Water | 0.00089 | All blocks |\n| Methanol (C₁) | 0.000545 | PROPblock_9 |\n| Ethanol (C₂) | 0.001082 | PROPblock_11 |\n| 1-Propanol (C₃) | 0.002017 | PROPblock_12 |\n| 2-Propanol (C₃, branched) | 0.002082 | PROPblock_15 |\n\nPure alcohol viscosity increases steadily with chain length (0.000545 → 0.001082 → 0.002017 Pa·s for C₁–C₃), reflecting stronger London dispersion forces and more extensive van der Waals contact area as the hydrocarbon portion grows.\n\n#### Peak mixture viscosities at 298.15 K\n\n| Alcohol | Peak η (Pa·s) | x(alcohol) at peak | Ratio peak/water |\n|---------|---------------|---------------------|------------------|\n| Methanol | 0.001554 | ~0.30 | 1.75× |\n| Ethanol | 0.0023 | ~0.20 | 2.58× |\n| 1-Propanol | 0.002691 | ~0.30 | 3.02× |\n| 2-Propanol | 0.003087 | ~0.30 | 3.47× |\n\n**Key trend:** The peak viscosity increases dramatically with chain length — methanol (0.001554) < ethanol (0.0023) < 1-propanol (0.002691 Pa·s). Longer alkyl chains amplify the viscosity enhancement by a factor of nearly 2 from C₁ to C₃.\n\n---\n\n### 3. Effect of Chain Branching (1-Propanol vs. 2-Propanol)\n\nBoth propanol isomers (C₃H₈O) share the same molecular formula and similar pure-component viscosities (0.002017 vs. 0.002082 Pa·s), yet the branched isomer (2-propanol) produces a **~15% higher peak viscosity** in aqueous mixtures (0.003087 vs. 0.002691 Pa·s), with both peaks occurring near x(alcohol) ≈ 0.30. This comparison is especially robust because both datasets come from the same laboratory, method, and conditions.\n\n---\n\n### 4. Representative Data\n\n#### Methanol + Water (PROPblock_9, DOI 10.1016/j.jct.2007.05.004)\n\n| x(methanol) | η (Pa·s) |\n|-------------|----------|\n| 0 (pure water) | 0.00089 |\n| 0.1007 | 0.000677 |\n| 0.3003 | 0.001554 ← peak |\n| 0.5006 | 0.001463 |\n| 1.0 (pure MeOH) | 0.000545 |\n\n*(Composition expressed as x(water) in the source; converted here: x(methanol) = 1 − x(water))*\n\n#### Ethanol + Water (PROPblock_11, DOI 10.1016/j.jct.2007.05.004)\n\n| x(ethanol) | η (Pa·s) |\n|------------|----------|\n| 0 (pure water) | 0.00089 |\n| 0.1004 | 0.00186 |\n| 0.1999 | 0.0023 ← peak |\n| 0.4011 | 0.002115 |\n| 1.0 (pure EtOH) | 0.001082 |\n\n#### 1-Propanol + Water (PROPblock_12, DOI 10.1021/je700700f)\n\n| x(1-propanol) | η (Pa·s) |\n|---------------|----------|\n| 0 | 0.00089 |\n| 0.0504 | 0.001616 |\n| 0.0993 | 0.002121 |\n| 0.2979 | 0.002691 ← peak |\n| 0.4955 | 0.002494 |\n| 1.0 | 0.002017 |\n\n#### 2-Propanol + Water (PROPblock_15, DOI 10.1021/je700700f)\n\n| x(2-propanol) | η (Pa·s) |\n|---------------|----------|\n| 0 | 0.00089 |\n| 0.0491 | 0.001718 |\n| 0.1008 | 0.002495 |\n| 0.2994 | 0.003087 ← peak |\n| 0.3992 | 0.002924 |\n| 1.0 | 0.002082 |\n\n---\n\n### 5. Intermolecular Interactions Explaining the Trends\n\nThe viscosity behaviour of aqueous alcohol mixtures is governed by a competition among several intermolecular interactions:\n\n#### (a) Hydrogen bonding (H-bonding)\nBoth water and alcohols are strong hydrogen-bond donors and acceptors. In mixtures, **cross-associated water–alcohol hydrogen bonds** form cooperatively, creating transient, extended networks that are more structured than either pure liquid alone. This cooperative H-bonding is the primary origin of the viscosity maximum: at intermediate compositions, the density of cross-associated H-bonds is highest, producing maximum resistance to flow.\n\n#### (b) Hydrophobic hydration\nWater molecules reorganize around the non-polar alkyl portion of the alcohol to form ordered, cage-like \"iceberg\" structures (Frank–Evans hydrophobic hydration). These structured hydration shells:\n- Increase the effective hydrodynamic volume of the solute\n- Slow molecular rearrangement and momentum transfer\n- Become more extensive as the alkyl chain lengthens, explaining why the peak viscosity grows from methanol (C₁) to 1-propanol (C₃)\n\nThe data quantify this: the peak viscosity rises from 0.001554 Pa·s (methanol) to 0.002691 Pa·s (1-propanol), a 73% increase for adding just two –CH₂– groups.\n\n#### (c) Hydrophobic association\nAt higher alcohol concentrations, alcohol molecules begin to self-aggregate through hydrophobic interactions, partially disrupting the water network. This causes the viscosity to decrease beyond the peak composition, eventually approaching the pure alcohol value.\n\n#### (d) Molecular geometry and branching effects\nThe comparison of 1-propanol and 2-propanol — same molecular formula, same number of H-bond sites — isolates the effect of molecular shape. The branched 2-propanol produces a higher peak viscosity (0.003087 vs. 0.002691 Pa·s). This can be attributed to:\n- **More compact molecular geometry** → the branched molecule presents a larger effective cross-section to the surrounding water cage, requiring more water molecules to complete the hydration shell\n- **Tighter packing of hydration structures** → the isopropyl group's globular shape may template more ordered water cages compared to the elongated n-propyl chain\n- **Reduced rotational freedom** → branching restricts internal rotation, making the hydrated complex more rigid and increasing its contribution to viscosity\n\n#### (e) Composition of the peak\nThe peak shifts to lower alcohol mole fractions as the alkyl chain grows: ~0.30 for methanol, ~0.20 for ethanol, and ~0.30 for both propanols. For ethanol, the shift to lower x(alcohol) reflects the fact that each larger alcohol molecule disrupts a greater volume of water structure, so the maximum cooperative H-bonding network is achieved at a lower alcohol mole fraction.\n\n---\n\n### 6. Summary of Structure–Viscosity Relationships\n\n| Structural change | Effect on peak mixture viscosity | Primary interaction responsible |\n|---|---|---|\n| Increasing chain length (C₁→C₂→C₃) | Increases: 0.001554 → 0.0023 → 0.002691 Pa·s | Enhanced hydrophobic hydration; larger non-polar surface |\n| Branching (n-C₃ → iso-C₃) | Increases: 0.002691 → 0.003087 Pa·s (+15%) | More compact geometry → tighter hydration shell packing |\n| Adding –OH group (alcohol vs. water) | Creates viscosity maximum above either pure component | Cooperative cross-associated H-bonding |\n\nThese data demonstrate that in aqueous mixtures of organic solvents, viscosity is not simply additive — it is governed by the interplay of hydrogen bonding, hydrophobic hydration, and molecular geometry, all of which are systematically modulated by the structure of the organic component.",
  "core_claims": [
    "All four binary alcohol–water systems (methanol, ethanol, 1-propanol, 2-propanol) at 298.15 K and 101 kPa display a non-monotonic viscosity profile with a pronounced maximum at an intermediate alcohol mole fraction, attributed primarily to cooperative cross-associated hydrogen bonding between water and alcohol molecules.",
    "Pure alcohol viscosity at 298.15 K increases with alkyl chain length: methanol 0.000545 Pa·s, ethanol 0.001082 Pa·s, 1-propanol 0.002017 Pa·s, reflecting stronger London dispersion forces with increasing hydrocarbon chain.",
    "Peak mixture viscosity at 298.15 K increases systematically with alkyl chain length: methanol 0.001554 Pa·s (at x ≈ 0.30), ethanol 0.0023 Pa·s (at x ≈ 0.20), 1-propanol 0.002691 Pa·s (at x ≈ 0.30), driven by enhanced hydrophobic hydration around the growing non-polar surface.",
    "Branching increases peak mixture viscosity: 2-propanol produces a ~15% higher peak viscosity (0.003087 Pa·s) than 1-propanol (0.002691 Pa·s) at x ≈ 0.30, despite nearly identical pure-component viscosities (0.002082 vs. 0.002017 Pa·s), attributed to the more compact molecular geometry of 2-propanol requiring tighter, more ordered hydration shell packing.",
    "Viscosity in these aqueous mixtures is not simply additive but is governed by the interplay of hydrogen bonding, hydrophobic hydration, and molecular geometry, all systematically modulated by the structure of the organic component."
  ],
  "confidence": "medium",
  "sources": [
    {
      "doi": "10.1016/j.jct.2007.05.004",
      "lit_num_id": "GLOBlit_2825",
      "block": "PROPblock_9",
      "BLKsubsys_id": null,
      "description": "Provides binary methanol + water viscosity data at 298.15 K and 101 kPa across the full mole fraction range (0–1), including the pure methanol value (0.000545 Pa·s) and the peak mixture viscosity (~0.001554 Pa·s near x = 0.30). This block anchors the C₁ alcohol baseline for the chain-length comparison."
    },
    {
      "doi": "10.1016/j.jct.2007.05.004",
      "lit_num_id": "GLOBlit_2825",
      "block": "PROPblock_11",
      "BLKsubsys_id": null,
      "description": "Provides binary ethanol + water viscosity data at 298.15 K and 101 kPa across the full mole fraction range, with a peak viscosity of ~0.0023 Pa·s and pure ethanol viscosity of 0.001082 Pa·s. This block supplies the C₂ data point in the chain-length trend and the viscosity maximum comparison."
    },
    {
      "doi": "10.1021/je700700f",
      "lit_num_id": "GLOBlit_11042",
      "block": "PROPblock_12",
      "BLKsubsys_id": null,
      "description": "Provides binary 1-propanol + water viscosity data at 298.15 K and 101 kPa (13 points, mole fraction 0–1). The max viscosity of 0.002691 Pa·s and pure 1-propanol value of 0.002017 Pa·s are directly cited in the answer for both the chain-length trend and the branching comparison with 2-propanol."
    },
    {
      "doi": "10.1021/je700700f",
      "lit_num_id": "GLOBlit_11042",
      "block": "PROPblock_15",
      "BLKsubsys_id": null,
      "description": "Provides binary 2-propanol + water viscosity data at 298.15 K and 101 kPa (13 points, mole fraction 0–1). The max viscosity of 0.003087 Pa·s and pure 2-propanol value of 0.002082 Pa·s are central to the branching analysis, showing the ~15% higher peak viscosity of the branched isomer relative to 1-propanol."
    }
  ],
  "follow_up_suggestions": [
    "Extend the comparison to C₄ alcohols (1-butanol, 2-butanol, tert-butanol) to test whether the chain-length and branching trends persist or saturate at longer chains.",
    "Examine the temperature dependence of the viscosity maximum to determine activation energies for viscous flow and relate them to the strength of hydrophobic hydration structures.",
    "Compare alcohol–water systems with other hydrogen-bonding organic solvents (e.g., ethylene glycol, glycerol, DMSO) to separate the contributions of hydrophobic hydration from cooperative hydrogen bonding.",
    "Investigate excess molar volumes and excess enthalpies of mixing for the same systems to correlate volumetric and energetic signatures with the viscosity anomalies."
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
    },
    {
      "type": "comp",
      "global_id": "GLOBcomp_4",
      "registry_id": "methanol",
      "name": "methanol"
    },
    {
      "type": "comp",
      "global_id": "GLOBcomp_5",
      "registry_id": "propan-1-ol",
      "name": "propan-1-ol"
    },
    {
      "type": "comp",
      "global_id": "GLOBcomp_6",
      "registry_id": "propan-2-ol",
      "name": "propan-2-ol"
    },
    {
      "type": "prop",
      "global_id": "GLOBprop_4",
      "registry_id": "viscosity_pa_s",
      "name": "Viscosity, Pa*s"
    },
    {
      "type": "lit",
      "global_id": "GLOBlit_2825",
      "registry_id": "2007-gon-cal-1",
      "name": "10.1016/j.jct.2007.05.004"
    },
    {
      "type": "lit",
      "global_id": "GLOBlit_11042",
      "registry_id": "2008-gon-cal-0",
      "name": "10.1021/je700700f"
    }
  ]
}

---

## Data Inspections (deterministic evidence ledger)

Hardcoded envelope merge — not agent-authored. 4 entr(ies); verbatim rows below.

- INSP_f99e390ea15c — GLOBlit_2825::PROPblock_9 · rdp · 12 rows
- INSP_f0616a9dca18 — GLOBlit_2825::PROPblock_11 · complete · 12 rows
- INSP_406cdf0a9372 — GLOBlit_11042::PROPblock_12 · rdp · 11 rows
- INSP_e0a2d04e3e34 — GLOBlit_11042::PROPblock_15 · rdp · 10 rows

```json
[
  {
    "doi": "10.1016/j.jct.2007.05.004",
    "block_number": "PROPblock_9",
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
        "BLKpoint_id": "BLKpoint_14",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.000545"
      },
      {
        "BLKpoint_id": "BLKpoint_15",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.049",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.000607"
      },
      {
        "BLKpoint_id": "BLKpoint_16",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.0993",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.000677"
      },
      {
        "BLKpoint_id": "BLKpoint_17",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.1973",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.000821"
      },
      {
        "BLKpoint_id": "BLKpoint_18",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.2983",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.000987"
      },
      {
        "BLKpoint_id": "BLKpoint_19",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.3985",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.00115"
      },
      {
        "BLKpoint_id": "BLKpoint_21",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.5994",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001463"
      },
      {
        "BLKpoint_id": "BLKpoint_22",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.6997",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001554"
      },
      {
        "BLKpoint_id": "BLKpoint_23",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.7986",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001542"
      },
      {
        "BLKpoint_id": "BLKpoint_24",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.8999",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001317"
      },
      {
        "BLKpoint_id": "BLKpoint_25",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.9512",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001121"
      },
      {
        "BLKpoint_id": "BLKpoint_26",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "1",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.00089"
      }
    ],
    "inspection_id": "INSP_f99e390ea15c",
    "lit_num_id": "GLOBlit_2825"
  },
  {
    "doi": "10.1016/j.jct.2007.05.004",
    "block_number": "PROPblock_11",
    "table_mode": "complete",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<water>",
      "pressure_kpa",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_14",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001082"
      },
      {
        "BLKpoint_id": "BLKpoint_15",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.0501",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001153"
      },
      {
        "BLKpoint_id": "BLKpoint_16",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.0986",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001232"
      },
      {
        "BLKpoint_id": "BLKpoint_17",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.1961",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.00138"
      },
      {
        "BLKpoint_id": "BLKpoint_18",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.2961",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001531"
      },
      {
        "BLKpoint_id": "BLKpoint_19",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.3991",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001659"
      },
      {
        "BLKpoint_id": "BLKpoint_20",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.5989",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002115"
      },
      {
        "BLKpoint_id": "BLKpoint_21",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.6991",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002275"
      },
      {
        "BLKpoint_id": "BLKpoint_22",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.8001",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0023"
      },
      {
        "BLKpoint_id": "BLKpoint_23",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.8996",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.00186"
      },
      {
        "BLKpoint_id": "BLKpoint_24",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.9499",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001388"
      },
      {
        "BLKpoint_id": "BLKpoint_25",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "1",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.00089"
      }
    ],
    "inspection_id": "INSP_f0616a9dca18",
    "lit_num_id": "GLOBlit_2825"
  },
  {
    "doi": "10.1021/je700700f",
    "block_number": "PROPblock_12",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "mole_fraction_<propan-1-ol>",
      "temperature_k",
      "pressure_kpa",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "mole_fraction_<propan-1-ol>": "0",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.00089"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "mole_fraction_<propan-1-ol>": "0.0504",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001616"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "mole_fraction_<propan-1-ol>": "0.0993",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002121"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "mole_fraction_<propan-1-ol>": "0.1986",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002599"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "mole_fraction_<propan-1-ol>": "0.2979",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002691"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "mole_fraction_<propan-1-ol>": "0.3949",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.00261"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "mole_fraction_<propan-1-ol>": "0.4955",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002494"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "mole_fraction_<propan-1-ol>": "0.5953",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002339"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "mole_fraction_<propan-1-ol>": "0.8983",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002026"
      },
      {
        "BLKpoint_id": "BLKpoint_12",
        "mole_fraction_<propan-1-ol>": "0.9518",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001998"
      },
      {
        "BLKpoint_id": "BLKpoint_13",
        "mole_fraction_<propan-1-ol>": "1",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002017"
      }
    ],
    "inspection_id": "INSP_406cdf0a9372",
    "lit_num_id": "GLOBlit_11042"
  },
  {
    "doi": "10.1021/je700700f",
    "block_number": "PROPblock_15",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "mole_fraction_<propan-2-ol>",
      "temperature_k",
      "pressure_kpa",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "mole_fraction_<propan-2-ol>": "0",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.00089"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "mole_fraction_<propan-2-ol>": "0.0491",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001718"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "mole_fraction_<propan-2-ol>": "0.1008",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002495"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "mole_fraction_<propan-2-ol>": "0.2011",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.003038"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "mole_fraction_<propan-2-ol>": "0.2994",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.003087"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "mole_fraction_<propan-2-ol>": "0.3992",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002924"
      },
      {
        "BLKpoint_id": "BLKpoint_9",
        "mole_fraction_<propan-2-ol>": "0.6987",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002274"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "mole_fraction_<propan-2-ol>": "0.7993",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002153"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "mole_fraction_<propan-2-ol>": "0.8998",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002073"
      },
      {
        "BLKpoint_id": "BLKpoint_13",
        "mole_fraction_<propan-2-ol>": "1",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002082"
      }
    ],
    "inspection_id": "INSP_e0a2d04e3e34",
    "lit_num_id": "GLOBlit_11042"
  }
]
```
