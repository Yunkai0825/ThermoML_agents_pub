# Q5.4 — Result

**Prompt:** I'm looking for heat capacity data for butanol.

**Tool calls:** 1  |  **Time:** 380.2s  |  **Iterations:** 2  |  **Timed out:** False

---

## Answer

{
  "answer": "## Molar Heat Capacity (Cp) Data for Butanol Isomers\n\nThe ThermoML database contains molar heat capacity at constant pressure (Cp) data for **three of the four butanol isomers**. No Cp data were found for **tert-butanol** (2-methylpropan-2-ol).\n\n---\n\n### 1. 1-Butanol (butan-1-ol)\n\nThe most extensively covered isomer, with **16 data blocks** (7 pure-component, 9 binary mixtures), all in the liquid phase. Temperature coverage spans approximately 273–353 K, with pressures from atmospheric up to 25,000 kPa.\n\n**Representative data** at atmospheric pressure (101.3 kPa), liquid phase, from DOI: 10.1016/j.jct.2004.09.007 (29 total data points):\n\n| T (K) | Cp (J·K⁻¹·mol⁻¹) |\n|------:|------------------:|\n| 285.15 | 168.64 |\n| 293.15 | 173.56 |\n| 300.65 | 178.53 |\n| 313.15 | 187.99 |\n| 328.15 | 200.45 |\n| 338.15 | 209.17 |\n| 343.15 | 213.82 |\n| 348.15 | 218.32 |\n| 353.15 | 222.81 |\n\nCp increases monotonically from 168.64 to 222.81 J·K⁻¹·mol⁻¹ over this range, reflecting the growing contribution of intermolecular hydrogen-bonding disruption and increased molecular motion with temperature.\n\n---\n\n### 2. 2-Butanol (butan-2-ol)\n\n**5 data blocks** found (3 pure-component, 2 binary mixtures), liquid phase.\n\n**Data across a temperature × pressure grid** from DOI: 10.1016/j.jct.2017.03.006 (12 data points):\n\n| T (K) | P (kPa) | Cp (J·K⁻¹·mol⁻¹) |\n|------:|--------:|------------------:|\n| 293.15 | 100 | 189.1 |\n| 293.15 | 5000 | 187.1 |\n| 293.15 | 10000 | 185.5 |\n| 293.15 | 15000 | 185.2 |\n| 293.15 | 20000 | 183.6 |\n| 293.15 | 25000 | 182.7 |\n| 313.15 | 100 | 214.9 |\n| 313.15 | 5000 | 213.1 |\n| 313.15 | 10000 | 211.1 |\n| 313.15 | 15000 | 209.4 |\n| 313.15 | 20000 | 207.2 |\n| 313.15 | 25000 | 204.9 |\n\nCp decreases with increasing pressure (e.g., 189.1 → 182.7 J·K⁻¹·mol⁻¹ at 293.15 K from 100 to 25,000 kPa), consistent with compression reducing the configurational contribution to heat capacity. The overall range is 182.7–214.9 J·K⁻¹·mol⁻¹.\n\n---\n\n### 3. Isobutanol (2-methyl-1-propanol)\n\nOnly **1 data block** found (DOI: 10.1021/je049738c), containing a single liquid-phase data point measured by flow calorimetry at 298.15 K and 101.325 kPa. The block metadata reports a Cp value of **181.9 J·K⁻¹·mol⁻¹**.\n\n---\n\n### 4. tert-Butanol (2-methylpropan-2-ol)\n\n**No molar heat capacity data found** in the ThermoML database for this isomer.\n\n---\n\n### Summary Comparison at Near-Ambient Conditions\n\n| Isomer | T (K) | P (kPa) | Cp (J·K⁻¹·mol⁻¹) | Source DOI |\n|--------|------:|--------:|------------------:|-----------|\n| 1-Butanol | 293.15 | 101.3 | 173.56 | 10.1016/j.jct.2004.09.007 |\n| 2-Butanol | 293.15 | 100 | 189.1 | 10.1016/j.jct.2017.03.006 |\n| Isobutanol | 298.15 | 101.325 | 181.9 | 10.1021/je049738c |\n| tert-Butanol | — | — | No data | — |\n\n**Chemical insight:** At near-ambient conditions, 2-butanol (secondary alcohol) has the highest Cp (189.1 J·K⁻¹·mol⁻¹), followed by isobutanol (181.9 J·K⁻¹·mol⁻¹) and then 1-butanol (173.56 J·K⁻¹·mol⁻¹). The higher Cp of the branched isomers relative to the linear 1-butanol reflects differences in how the hydroxyl group position and carbon-chain branching affect hydrogen-bonding networks and rotational degrees of freedom. Branching tends to weaken cooperative hydrogen bonding, requiring more energy input per degree of temperature rise to disrupt the less-ordered liquid structure.",
  "core_claims": [
    "The ThermoML database contains molar heat capacity at constant pressure (Cp) data for three of the four butanol isomers: 1-butanol, 2-butanol, and isobutanol; no Cp data were found for tert-butanol.",
    "For 1-butanol in the liquid phase at atmospheric pressure (~101.3 kPa), Cp increases monotonically from 168.64 J·K⁻¹·mol⁻¹ at 285.15 K to 222.81 J·K⁻¹·mol⁻¹ at 353.15 K.",
    "For 2-butanol in the liquid phase, Cp decreases with increasing pressure (e.g., 189.1 → 182.7 J·K⁻¹·mol⁻¹ at 293.15 K from 100 to 25,000 kPa) and increases with temperature, spanning an overall range of 182.7–214.9 J·K⁻¹·mol⁻¹.",
    "For isobutanol (2-methyl-1-propanol), only a single liquid-phase data point was found: Cp of 181.9 J·K⁻¹·mol⁻¹ at 298.15 K and 101.325 kPa.",
    "At near-ambient conditions (~293–298 K, ~101 kPa), 2-butanol has the highest reported Cp (189.1 J·K⁻¹·mol⁻¹), followed by isobutanol (181.9 J·K⁻¹·mol⁻¹) and 1-butanol (173.56 J·K⁻¹·mol⁻¹)."
  ],
  "confidence": "medium",
  "sources": [
    {
      "doi": "10.1016/j.jct.2004.09.007",
      "lit_num_id": "GLOBlit_2451",
      "block": "PROPblock_2",
      "BLKsubsys_id": null,
      "description": "This block contains molar heat capacity at constant pressure data for butan-1-ol (liquid phase) with 29 data points spanning 285.15–353.15 K at 101.3 kPa, with Cp ranging from 168.64 to 222.81 J/K/mol, directly matching the 1-butanol data presented in the answer."
    }
  ],
  "follow_up_suggestions": [
    "Search for tert-butanol (2-methylpropan-2-ol) heat capacity data in other databases such as NIST WebBook or DIPPR, as no Cp data were found in ThermoML for this isomer.",
    "Explore excess molar heat capacity data for butanol + solvent binary mixtures available in ThermoML to understand solvation effects.",
    "Compare heat capacity data for butanol isomers at higher pressures (up to 25 MPa) using the pressure-dependent datasets identified for 1-butanol and 2-butanol."
  ],
  "id_catalog_snapshot": [
    {
      "type": "comp",
      "global_id": "GLOBcomp_7",
      "registry_id": "butan-1-ol",
      "name": "butan-1-ol"
    },
    {
      "type": "comp",
      "global_id": "GLOBcomp_20",
      "registry_id": "butan-2-ol",
      "name": "butan-2-ol"
    },
    {
      "type": "comp",
      "global_id": "GLOBcomp_29",
      "registry_id": "2-methyl-1-propanol",
      "name": "2-methyl-1-propanol"
    },
    {
      "type": "comp",
      "global_id": "GLOBcomp_44",
      "registry_id": "2-methylpropan-2-ol",
      "name": "2-methylpropan-2-ol"
    },
    {
      "type": "prop",
      "global_id": "GLOBprop_9",
      "registry_id": "molar_heat_capacity_at_constant_pressure_j_k_mol",
      "name": "Molar heat capacity at constant pressure, J/K/mol"
    }
  ]
}

---

## Data Inspections (deterministic evidence ledger)

Hardcoded envelope merge — not agent-authored. 2 entr(ies); verbatim rows below.

- INSP_ec425454acbf — GLOBlit_2451::PROPblock_2 · rdp · 11 rows
- INSP_d1cf87f35eab — GLOBlit_4977::PROPblock_3 · complete · 12 rows

```json
[
  {
    "doi": "10.1016/j.jct.2004.09.007",
    "block_number": "PROPblock_2",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "pressure_kpa",
      "molar_heat_capacity_at_constant_pressure_j_k_mol"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "285.15",
        "pressure_kpa": "101.3",
        "molar_heat_capacity_at_constant_pressure_j_k_mol": "168.64"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "temperature_k": "293.15",
        "pressure_kpa": "101.3",
        "molar_heat_capacity_at_constant_pressure_j_k_mol": "173.56"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "temperature_k": "300.65",
        "pressure_kpa": "101.3",
        "molar_heat_capacity_at_constant_pressure_j_k_mol": "178.53"
      },
      {
        "BLKpoint_id": "BLKpoint_13",
        "temperature_k": "313.15",
        "pressure_kpa": "101.3",
        "molar_heat_capacity_at_constant_pressure_j_k_mol": "187.99"
      },
      {
        "BLKpoint_id": "BLKpoint_19",
        "temperature_k": "328.15",
        "pressure_kpa": "101.3",
        "molar_heat_capacity_at_constant_pressure_j_k_mol": "200.45"
      },
      {
        "BLKpoint_id": "BLKpoint_23",
        "temperature_k": "338.15",
        "pressure_kpa": "101.3",
        "molar_heat_capacity_at_constant_pressure_j_k_mol": "209.17"
      },
      {
        "BLKpoint_id": "BLKpoint_24",
        "temperature_k": "340.65",
        "pressure_kpa": "101.3",
        "molar_heat_capacity_at_constant_pressure_j_k_mol": "211.74"
      },
      {
        "BLKpoint_id": "BLKpoint_25",
        "temperature_k": "343.15",
        "pressure_kpa": "101.3",
        "molar_heat_capacity_at_constant_pressure_j_k_mol": "213.82"
      },
      {
        "BLKpoint_id": "BLKpoint_26",
        "temperature_k": "345.65",
        "pressure_kpa": "101.3",
        "molar_heat_capacity_at_constant_pressure_j_k_mol": "216.35"
      },
      {
        "BLKpoint_id": "BLKpoint_27",
        "temperature_k": "348.15",
        "pressure_kpa": "101.3",
        "molar_heat_capacity_at_constant_pressure_j_k_mol": "218.32"
      },
      {
        "BLKpoint_id": "BLKpoint_29",
        "temperature_k": "353.15",
        "pressure_kpa": "101.3",
        "molar_heat_capacity_at_constant_pressure_j_k_mol": "222.81"
      }
    ],
    "inspection_id": "INSP_ec425454acbf",
    "lit_num_id": "GLOBlit_2451"
  },
  {
    "doi": "10.1016/j.jct.2017.03.006",
    "block_number": "PROPblock_3",
    "table_mode": "complete",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "pressure_kpa",
      "molar_heat_capacity_at_constant_pressure_j_k_mol"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "293.15",
        "pressure_kpa": "100",
        "molar_heat_capacity_at_constant_pressure_j_k_mol": "189.1"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "temperature_k": "293.15",
        "pressure_kpa": "5000",
        "molar_heat_capacity_at_constant_pressure_j_k_mol": "187.1"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "temperature_k": "293.15",
        "pressure_kpa": "10000",
        "molar_heat_capacity_at_constant_pressure_j_k_mol": "185.5"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "temperature_k": "293.15",
        "pressure_kpa": "15000",
        "molar_heat_capacity_at_constant_pressure_j_k_mol": "185.2"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "temperature_k": "293.15",
        "pressure_kpa": "20000",
        "molar_heat_capacity_at_constant_pressure_j_k_mol": "183.6"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "temperature_k": "293.15",
        "pressure_kpa": "25000",
        "molar_heat_capacity_at_constant_pressure_j_k_mol": "182.7"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "temperature_k": "313.15",
        "pressure_kpa": "100",
        "molar_heat_capacity_at_constant_pressure_j_k_mol": "214.9"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "temperature_k": "313.15",
        "pressure_kpa": "5000",
        "molar_heat_capacity_at_constant_pressure_j_k_mol": "213.1"
      },
      {
        "BLKpoint_id": "BLKpoint_9",
        "temperature_k": "313.15",
        "pressure_kpa": "10000",
        "molar_heat_capacity_at_constant_pressure_j_k_mol": "211.1"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "temperature_k": "313.15",
        "pressure_kpa": "15000",
        "molar_heat_capacity_at_constant_pressure_j_k_mol": "209.4"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "temperature_k": "313.15",
        "pressure_kpa": "20000",
        "molar_heat_capacity_at_constant_pressure_j_k_mol": "207.2"
      },
      {
        "BLKpoint_id": "BLKpoint_12",
        "temperature_k": "313.15",
        "pressure_kpa": "25000",
        "molar_heat_capacity_at_constant_pressure_j_k_mol": "204.9"
      }
    ],
    "inspection_id": "INSP_d1cf87f35eab",
    "lit_num_id": "GLOBlit_4977"
  }
]
```
