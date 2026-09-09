# Q1.4 — Result

**Prompt:** Have activity coefficients been measured for aqueous lithium chloride near 25 °C, and over what concentration range?

**Tool calls:** 1  |  **Time:** 258.3s  |  **Iterations:** 2  |  **Timed out:** False

---

## Answer

{
  "answer": "Yes — the ThermoML database contains **mean ionic activity coefficient (γ±)** measurements for the binary system **lithium chloride (LiCl) + water** at exactly **298.15 K (25 °C)** and **101.0 kPa**.\n\n## Source\n\n- **DOI:** 10.1016/j.fluid.2014.08.026\n- **Method:** Calculated from EMF (electromotive force) cell potential measurements\n- **Total data points:** 141\n\n## Concentration Range\n\nThe dataset spans **LiCl molality from 0.0033 to 1.5555 mol/kg**, covering a wide range from very dilute to moderately concentrated solutions.\n\n## Activity Coefficient Range\n\nγ± values range from **0.7406 to 0.9425** across the 141 data points.\n\n## Representative Data Points\n\n**Dilute region:**\n\n| Molality (mol/kg) | γ± |\n|---|---|\n| 0.0033 | 0.9425 |\n| 0.0033 | 0.9398 |\n| 0.0035 | 0.9388 |\n| 0.004 | 0.935 |\n\n**Concentrated region:**\n\n| Molality (mol/kg) | γ± |\n|---|---|\n| 1.485 | 0.8424 |\n| 1.5095 | 0.839 |\n| 1.5483 | 0.845 |\n| 1.5555 | 0.8461 |\n\n## Chemistry Insight\n\nThe data exhibit the characteristic **non-monotonic (U-shaped) trend** expected for a strong 1:1 electrolyte like LiCl in water:\n\n1. **Dilute limit:** γ± starts near unity (~0.94 at 0.003 mol/kg), consistent with Debye–Hückel theory predicting ideal behavior at infinite dilution.\n2. **Intermediate molalities:** γ± decreases to a minimum of about **0.74**, driven by long-range electrostatic ion–ion interactions that lower the effective activity.\n3. **Higher concentrations:** γ± rises again to ~0.85 near 1.5 mol/kg, reflecting the growing importance of short-range ion–solvent interactions (strong Li⁺ hydration) and ion-pairing effects that cause positive deviations from Debye–Hückel predictions.\n\nThis upturn at higher concentrations is especially pronounced for lithium salts because the small Li⁺ ion has a very high charge density and binds water molecules tightly, effectively reducing the amount of \"free\" solvent and increasing the effective salt concentration — and hence the activity coefficient. The EMF method used is a standard electrochemical technique well-suited for precise determination of mean ionic activity coefficients in electrolyte solutions.",
  "core_claims": [
    "The ThermoML database contains mean ionic activity coefficient (γ±) measurements for the binary system LiCl + water at 298.15 K and 101.0 kPa, sourced from DOI 10.1016/j.fluid.2014.08.026, comprising 141 data points derived from EMF cell potential measurements.",
    "The dataset spans LiCl molality from 0.0033 to 1.5555 mol/kg, with γ± values ranging from 0.7406 to 0.9425.",
    "The data exhibit a non-monotonic (U-shaped) trend: γ± starts near unity in the dilute limit (~0.94 at 0.003 mol/kg), decreases to a minimum of about 0.74 at intermediate molalities due to long-range electrostatic ion–ion interactions, and rises again to ~0.85 near 1.5 mol/kg due to short-range ion–solvent interactions and strong Li⁺ hydration."
  ],
  "confidence": "medium",
  "sources": [],
  "follow_up_suggestions": [
    "Compare LiCl activity coefficients with other alkali metal chlorides (NaCl, KCl) at 25 °C to examine the effect of cation size on the U-shaped γ± trend.",
    "Search for LiCl activity coefficient data at higher molalities (above 1.6 mol/kg) or at other temperatures to map the full concentration and temperature dependence.",
    "Look for osmotic coefficient data for aqueous LiCl near 25 °C to cross-validate the activity coefficient measurements via the Gibbs–Duhem relation."
  ],
  "id_catalog_snapshot": [
    {
      "type": "comp",
      "global_id": "GLOBcomp_107",
      "registry_id": "lithium_chloride",
      "name": "lithium chloride"
    },
    {
      "type": "comp",
      "global_id": "GLOBcomp_1",
      "registry_id": "water",
      "name": "water"
    },
    {
      "type": "prop",
      "global_id": "GLOBprop_56",
      "registry_id": "mean_ionic_activity_coefficient_{DOIcomp_id}",
      "name": "Mean ionic activity coefficient"
    },
    {
      "type": "meas",
      "global_id": "GLOBmeas_185",
      "registry_id": "calculated_from_emf_cell_potential",
      "name": "Calculated from EMF cell potential"
    },
    {
      "type": "lit",
      "global_id": "GLOBlit_1540",
      "registry_id": "2014-zha-li-3",
      "name": "10.1016/j.fluid.2014.08.026"
    }
  ]
}

---

## Data Inspections (deterministic evidence ledger)

Hardcoded envelope merge — not agent-authored. 2 entr(ies); verbatim rows below.

- INSP_186265bdb491 — GLOBlit_1540::PROPblock_13 · nearest · 4 rows
- INSP_1a64ad047f12 — GLOBlit_1540::PROPblock_13 · nearest · 4 rows

```json
[
  {
    "doi": "10.1016/j.fluid.2014.08.026",
    "block_number": "PROPblock_13",
    "table_mode": "nearest",
    "columns": [
      "BLKpoint_id",
      "molality_mol_kg_<lithium chloride>",
      "temperature_k",
      "pressure_kpa",
      "mean_ionic_activity_coefficient_<lithium chloride>"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_56",
        "molality_mol_kg_<lithium chloride>": "0.0033",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "mean_ionic_activity_coefficient_<lithium chloride>": "0.9425"
      },
      {
        "BLKpoint_id": "BLKpoint_115",
        "molality_mol_kg_<lithium chloride>": "0.0033",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "mean_ionic_activity_coefficient_<lithium chloride>": "0.9398"
      },
      {
        "BLKpoint_id": "BLKpoint_1",
        "molality_mol_kg_<lithium chloride>": "0.0035",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "mean_ionic_activity_coefficient_<lithium chloride>": "0.9388"
      },
      {
        "BLKpoint_id": "BLKpoint_84",
        "molality_mol_kg_<lithium chloride>": "0.004",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "mean_ionic_activity_coefficient_<lithium chloride>": "0.935"
      }
    ],
    "inspection_id": "INSP_186265bdb491",
    "lit_num_id": "GLOBlit_1540"
  },
  {
    "doi": "10.1016/j.fluid.2014.08.026",
    "block_number": "PROPblock_13",
    "table_mode": "nearest",
    "columns": [
      "BLKpoint_id",
      "molality_mol_kg_<lithium chloride>",
      "temperature_k",
      "pressure_kpa",
      "mean_ionic_activity_coefficient_<lithium chloride>"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_83",
        "molality_mol_kg_<lithium chloride>": "1.485",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "mean_ionic_activity_coefficient_<lithium chloride>": "0.8424"
      },
      {
        "BLKpoint_id": "BLKpoint_26",
        "molality_mol_kg_<lithium chloride>": "1.5095",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "mean_ionic_activity_coefficient_<lithium chloride>": "0.839"
      },
      {
        "BLKpoint_id": "BLKpoint_141",
        "molality_mol_kg_<lithium chloride>": "1.5483",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "mean_ionic_activity_coefficient_<lithium chloride>": "0.845"
      },
      {
        "BLKpoint_id": "BLKpoint_55",
        "molality_mol_kg_<lithium chloride>": "1.5555",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "mean_ionic_activity_coefficient_<lithium chloride>": "0.8461"
      }
    ],
    "inspection_id": "INSP_1a64ad047f12",
    "lit_num_id": "GLOBlit_1540"
  }
]
```
