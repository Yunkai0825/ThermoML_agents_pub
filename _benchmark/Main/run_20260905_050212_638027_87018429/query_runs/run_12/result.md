# Delegated query run — result

**Question:** Find density measurements for the binary mixture of water and 1-propanol near 298.15 K. I need DOIs, block numbers, temperature ranges, composition ranges, and density values.

**Iterations:** 3  |  **Elapsed:** 566.5s  |  **Tools:** 2  |  **Timed out:** False

---

## Answer

{
  "answer": "## Mass Density Data for the Binary Mixture of Water + 1-Propanol near 298.15 K\n\n**System:** Water (H₂O) + 1-Propanol (C₃H₈O), binary liquid mixture  \n**Property:** Mass density (kg/m³)\n\n### Overview\n\nA search of the ThermoML database identified **13 data blocks** from **11 independent literature sources** containing mass density measurements for the water + 1-propanol binary system with temperatures encompassing or near 298.15 K. These blocks span a wide range of compositions (dilute aqueous to nearly pure 1-propanol), pressures (atmospheric to ~40 MPa), and temperature ranges. Three blocks were inspected in detail for verbatim data points at exactly 298.15 K.\n\n---\n\n### Complete Block Inventory\n\n| # | DOI | Block | T range (K) | Composition variable & range | P (kPa) | ρ range (kg/m³) | N pts | Method |\n|---|-----|-------|-------------|------------------------------|---------|-----------------|-------|--------|\n| 1 | 10.1016/j.fluid.2007.07.066 | PROPblock_8 | 283.15–303.15 | Mass fraction, 0.05–0.15 | 101.0 | 976.004–992.444 | 15 | Vibrating tube |\n| 2 | 10.1016/j.fluid.2008.01.004 | PROPblock_5 | 283.15–303.15 | Mass fraction, 0.05–0.15 | 101.0 | 975.791–992.405 | 15 | Vibrating tube |\n| 3 | 10.1016/j.jct.2004.07.019 | PROPblock_3 | 298.15–573.15 | Molality, 0.0943–0.84695 mol/kg | 420–30310 | (excess density reported) | 456 | Vibrating tube |\n| 4 | 10.1016/j.jct.2008.07.005 | PROPblock_9 | 283.15–308.15 | Mole fraction, 0.0–0.2 | 98.93 | 911.83–999.69 | 96 | Pycnometric |\n| 5 | 10.1016/j.jct.2013.11.036 | PROPblock_1 | 298.15–582.08 | Molality, 0.869–56.348 mol/kg | 2353–40000 | 322.1–1004.4 | 174 | Constant-volume piezometry |\n| 6 | 10.1016/j.jct.2013.11.036 | PROPblock_2 | 292.05–352.05 | Molality, 0.869–56.348 mol/kg | 101.0 | 801.03–991.42 | 29 | Pycnometric |\n| 7 | 10.1016/j.jct.2015.06.024 | PROPblock_5 | 288.15–308.15 | Molality, 0.01666–0.16617 mol/kg | 84.5 | 992.305–998.928 | 40 | Vibrating tube |\n| 8 | 10.1016/j.jct.2019.105880 | PROPblock_7 | 288.15–303.15 | Mass fraction, 0.1–0.4 | 100.0 | 924.386–985.245 | 16 | Vibrating tube |\n| 9 | 10.1021/acs.jced.6b01058 | PROPblock_8 | 298.15–313.15 | Mass fraction, 0.04–0.16 | 85.0 | 966.84–990.59 | 12 | Vibrating tube |\n| 10 | 10.1021/acs.jced.7b00299 | PROPblock_13 | 298.15–313.15 | Molality = 14.0 mol/kg (fixed) | 100.0 | 903.156–914.36 | 2 | Vibrating tube |\n| 11 | 10.1021/je034101z | PROPblock_6 | 282.15–425.15 | Mole fraction, 0.255–0.738 | 5753–29883 | 731.4–896.2 | 380 | Isochoric |\n| 12 | 10.1021/je4003515 | PROPblock_10 | 293.15–313.15 | Molality, 14.0–22.0 mol/kg | 101.0 | 879.756–918.103 | 25 | Vibrating tube |\n| 13 | 10.1021/je800158z | PROPblock_3 | 293.15–323.15 | Mole fraction, 0.0–1.0 | 81.5 | 778.92–998.2 | 56 | Vibrating tube |\n\n**Notes on block types:**\n- Blocks 1, 2, 4, 7, 8, 9, 13 are **atmospheric-pressure** datasets most directly relevant to standard 298.15 K measurements.\n- Blocks 3, 5, 11 are **high-pressure** datasets (up to ~40 MPa) and may report excess or differential densities.\n- Block 13 (DOI 10.1021/je800158z) provides the widest composition coverage at atmospheric pressure, spanning the **full mole-fraction range 0.0–1.0**.\n\n---\n\n### Inspected Data Points at T = 298.15 K\n\n#### Source 1: DOI 10.1016/j.fluid.2007.07.066, PROPblock_8\n**Constraint:** P = 101.0 kPa | **Composition:** mass fraction of 1-propanol\n\n| Mass fraction (1-propanol) | ρ (kg/m³) |\n|---|---|\n| 0.05 | 989.431 |\n| 0.10 | 983.475 |\n| 0.15 | 978.117 |\n\n#### Source 2: DOI 10.1016/j.fluid.2008.01.004, PROPblock_5\n**Constraint:** P = 101.0 kPa | **Composition:** mass fraction of 1-propanol\n\n| Mass fraction (1-propanol) | ρ (kg/m³) |\n|---|---|\n| 0.05 | 989.387 |\n| 0.10 | 983.372 |\n| 0.15 | 977.921 |\n\n#### Source 3: DOI 10.1016/j.jct.2008.07.005, PROPblock_9\n**Constraint:** P = 98.93 kPa | **Composition:** mole fraction of 1-propanol\n\n| Mole fraction (1-propanol) | ρ (kg/m³) |\n|---|---|\n| 0 | 997.04 |\n| 0.002 | 995.4 |\n| 0.005 | 993.76 |\n| 0.009 | 991.66 |\n| 0.01 | 991.14 |\n| 0.02 | 986.54 |\n| 0.03 | 982.56 |\n| 0.05 | 975.49 |\n\n---\n\n### Chemistry Insights\n\n1. **Monotonic density decrease:** All three inspected sources consistently show that density decreases monotonically with increasing 1-propanol content at 298.15 K. Starting from ~997 kg/m³ for pure water, the density drops to ~975 kg/m³ at a mole fraction of 0.05 (Source 3). This reflects the lower intrinsic density of 1-propanol (~803 kg/m³ at 298.15 K) compared to water.\n\n2. **Inter-source consistency:** Sources 1 and 2 use the same composition variable (mass fraction) at the same pressure (101.0 kPa) and show excellent agreement — e.g., at w = 0.05, the densities are 989.431 vs. 989.387 kg/m³ (difference of only 0.044 kg/m³), providing confidence in the data quality.\n\n3. **Composition coverage:** The inspected data cover only the water-rich region. For broader coverage including the 1-propanol-rich side, the block from DOI 10.1021/je800158z (PROPblock_3, mole fraction 0.0–1.0, 56 points, 293.15–323.15 K) and DOI 10.1016/j.jct.2013.11.036 (PROPblock_2, molality 0.869–56.348 mol/kg, 29 points at 101.0 kPa) would be the most relevant uninspected atmospheric-pressure sources.\n\n4. **High-pressure data:** Three blocks (from DOIs 10.1016/j.jct.2004.07.019, 10.1016/j.jct.2013.11.036, and 10.1021/je034101z) provide density data at elevated pressures up to ~40 MPa, useful for equation-of-state modeling.",
  "core_claims": [
    "Thirteen data blocks from eleven independent ThermoML literature sources were identified containing mass density measurements for the water + 1-propanol binary liquid mixture at or near 298.15 K, spanning compositions from dilute aqueous to nearly pure 1-propanol and pressures from atmospheric to ~40 MPa.",
    "At 298.15 K and atmospheric pressure, all three inspected sources consistently show that mass density decreases monotonically with increasing 1-propanol content, from ~997 kg/m³ for pure water to ~975 kg/m³ at a 1-propanol mole fraction of 0.05.",
    "Two independent sources at 101.0 kPa and mass fraction 0.05 of 1-propanol report densities of 989.431 and 989.387 kg/m³, a difference of only 0.044 kg/m³, indicating excellent inter-source consistency.",
    "The three inspected data blocks cover only the water-rich composition region; broader composition coverage including the 1-propanol-rich side is available in uninspected blocks but was not verified."
  ],
  "confidence": "medium",
  "sources": [
    {
      "doi": "10.1016/j.fluid.2007.07.066",
      "lit_num_id": "GLOBlit_555",
      "block": "PROPblock_8",
      "BLKsubsys_id": null,
      "description": "Provides mass density of water + 1-propanol at 298.15 K and 101.0 kPa for mass fractions 0.05–0.15; verbatim data points (989.431, 983.475, 978.117 kg/m³) are quoted in the answer."
    },
    {
      "doi": "10.1016/j.fluid.2008.01.004",
      "lit_num_id": "GLOBlit_590",
      "block": "PROPblock_5",
      "BLKsubsys_id": null,
      "description": "Provides mass density of water + 1-propanol at 298.15 K and 101.0 kPa for mass fractions 0.05–0.15; verbatim data points (989.387, 983.372, 977.921 kg/m³) are quoted and used for inter-source consistency comparison."
    },
    {
      "doi": "10.1016/j.jct.2004.07.019",
      "lit_num_id": "GLOBlit_2432",
      "block": "PROPblock_3",
      "BLKsubsys_id": null,
      "description": "High-pressure density data for water + 1-propanol starting at 298.15 K; the card shows negative property values indicating excess/differential density rather than absolute density, which the answer correctly notes. Contributes to the high-pressure data inventory."
    },
    {
      "doi": "10.1016/j.jct.2008.07.005",
      "lit_num_id": "GLOBlit_2979",
      "block": "PROPblock_9",
      "BLKsubsys_id": null,
      "description": "Provides mass density of water + 1-propanol at 298.15 K and 98.93 kPa for mole fractions 0.0–0.2; verbatim data points (997.04 down to 975.49 kg/m³) are quoted in the answer's inspected data section."
    },
    {
      "doi": "10.1016/j.jct.2013.11.036",
      "lit_num_id": "GLOBlit_4068",
      "block": "PROPblock_1",
      "BLKsubsys_id": null,
      "description": "High-pressure (2353–40000 kPa) mass density data for water + 1-propanol including 298.15 K; contributes to the answer's inventory of high-pressure datasets for equation-of-state modeling."
    },
    {
      "doi": "10.1016/j.jct.2013.11.036",
      "lit_num_id": "GLOBlit_4068",
      "block": "PROPblock_2",
      "BLKsubsys_id": null,
      "description": "Atmospheric-pressure (101.0 kPa) pycnometric density data for water + 1-propanol spanning 292.05–352.05 K and molality 0.869–56.348 mol/kg, providing broad composition coverage including the 1-propanol-rich region as noted in the answer."
    },
    {
      "doi": "10.1016/j.jct.2015.06.024",
      "lit_num_id": "GLOBlit_4415",
      "block": "PROPblock_5",
      "BLKsubsys_id": null,
      "description": "Provides mass density of dilute water + 1-propanol mixtures (molality 0.017–0.166 mol/kg) at temperatures including 298.15 K; contributes atmospheric-pressure data in the very dilute composition regime."
    },
    {
      "doi": "10.1016/j.jct.2019.105880",
      "lit_num_id": "GLOBlit_5585",
      "block": "PROPblock_7",
      "BLKsubsys_id": null,
      "description": "Provides mass density at 288.15–303.15 K and 100.0 kPa for mass fractions 0.1–0.4, extending composition coverage to higher 1-propanol content than Sources 1 and 2 in the answer."
    },
    {
      "doi": "10.1021/acs.jced.6b01058",
      "lit_num_id": "GLOBlit_7085",
      "block": "PROPblock_8",
      "BLKsubsys_id": null,
      "description": "Provides mass density at 298.15–313.15 K and 85.0 kPa for mass fractions 0.04–0.16; contributes atmospheric-pressure data at 298.15 K in the water-rich region."
    },
    {
      "doi": "10.1021/acs.jced.7b00299",
      "lit_num_id": "GLOBlit_7178",
      "block": "PROPblock_13",
      "BLKsubsys_id": null,
      "description": "Provides mass density at fixed molality 14.0 mol/kg (1-propanol-rich) at 298.15 and 313.15 K; contributes a data point in the propanol-rich composition regime at 298.15 K."
    },
    {
      "doi": "10.1021/je034101z",
      "lit_num_id": "GLOBlit_8254",
      "block": "PROPblock_6",
      "BLKsubsys_id": null,
      "description": "High-pressure isochoric density data for water + 1-propanol at mole fractions 0.255–0.738 and temperatures including near 298.15 K; contributes to the answer's high-pressure data inventory."
    },
    {
      "doi": "10.1021/je4003515",
      "lit_num_id": "GLOBlit_10159",
      "block": "PROPblock_10",
      "BLKsubsys_id": null,
      "description": "Provides mass density at 293.15–313.15 K and 101.0 kPa for molality 14.0–22.0 mol/kg, covering the 1-propanol-rich composition range at atmospheric pressure including near 298.15 K."
    },
    {
      "doi": "10.1021/je800158z",
      "lit_num_id": "GLOBlit_11142",
      "block": "PROPblock_3",
      "BLKsubsys_id": null,
      "description": "Provides mass density spanning the full mole-fraction range 0.0–1.0 at 293.15–323.15 K and 81.5 kPa; the answer highlights this as the widest composition coverage atmospheric-pressure source."
    }
  ],
  "follow_up_suggestions": [
    "Inspect PROPblock_3 from DOI 10.1021/je800158z for verbatim data points at 298.15 K across the full mole-fraction range (0.0–1.0) to obtain complete atmospheric-pressure density coverage.",
    "Inspect PROPblock_2 from DOI 10.1016/j.jct.2013.11.036 for data points near 298.15 K at 101.0 kPa covering the 1-propanol-rich composition region.",
    "Search for excess molar volume data for water + 1-propanol at 298.15 K to complement the absolute density measurements.",
    "Compare the high-pressure density data from DOI 10.1016/j.jct.2004.07.019 and DOI 10.1021/je034101z for equation-of-state parameterization of the water + 1-propanol system."
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
      "global_id": "GLOBcomp_5",
      "registry_id": "propan-1-ol",
      "name": "propan-1-ol"
    },
    {
      "type": "prop",
      "global_id": "GLOBprop_1",
      "registry_id": "mass_density_kg_m3",
      "name": "Mass density, kg/m3"
    }
  ]
}

---

## Data Inspections (deterministic evidence ledger)

Hardcoded envelope merge — not agent-authored. 3 entr(ies); verbatim rows below.

- INSP_3aa36d70ff07 — GLOBlit_555::PROPblock_8 · nearest · 5 rows
- INSP_884f359f5908 — GLOBlit_2979::PROPblock_9 · nearest · 8 rows
- INSP_859136865c90 — GLOBlit_590::PROPblock_5 · nearest · 8 rows

```json
[
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
        "BLKpoint_id": "BLKpoint_7",
        "temperature_k": "293.15",
        "mass_fraction_<propan-1-ol>": "0.05",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "990.715"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "temperature_k": "293.15",
        "mass_fraction_<propan-1-ol>": "0.1",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "985.011"
      },
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
    "inspection_id": "INSP_3aa36d70ff07",
    "lit_num_id": "GLOBlit_555"
  },
  {
    "doi": "10.1016/j.jct.2008.07.005",
    "block_number": "PROPblock_9",
    "table_mode": "nearest",
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
        "BLKpoint_id": "BLKpoint_51",
        "temperature_k": "298.15",
        "mole_fraction_<propan-1-ol>": "0.005",
        "pressure_kpa": "98.93",
        "mass_density_kg_m3": "993.76"
      },
      {
        "BLKpoint_id": "BLKpoint_52",
        "temperature_k": "298.15",
        "mole_fraction_<propan-1-ol>": "0.009",
        "pressure_kpa": "98.93",
        "mass_density_kg_m3": "991.66"
      },
      {
        "BLKpoint_id": "BLKpoint_53",
        "temperature_k": "298.15",
        "mole_fraction_<propan-1-ol>": "0.01",
        "pressure_kpa": "98.93",
        "mass_density_kg_m3": "991.14"
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
      }
    ],
    "inspection_id": "INSP_884f359f5908",
    "lit_num_id": "GLOBlit_2979"
  },
  {
    "doi": "10.1016/j.fluid.2008.01.004",
    "block_number": "PROPblock_5",
    "table_mode": "nearest",
    "columns": [
      "BLKpoint_id",
      "mass_fraction_<propan-1-ol>",
      "temperature_k",
      "pressure_kpa",
      "mass_density_kg_m3"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_3",
        "mass_fraction_<propan-1-ol>": "0.05",
        "temperature_k": "293.15",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "990.671"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "mass_fraction_<propan-1-ol>": "0.1",
        "temperature_k": "293.15",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "984.913"
      },
      {
        "BLKpoint_id": "BLKpoint_13",
        "mass_fraction_<propan-1-ol>": "0.15",
        "temperature_k": "293.15",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "979.828"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "mass_fraction_<propan-1-ol>": "0.05",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "989.387"
      },
      {
        "BLKpoint_id": "BLKpoint_9",
        "mass_fraction_<propan-1-ol>": "0.1",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "983.372"
      },
      {
        "BLKpoint_id": "BLKpoint_14",
        "mass_fraction_<propan-1-ol>": "0.15",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "977.921"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "mass_fraction_<propan-1-ol>": "0.05",
        "temperature_k": "303.15",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "987.86"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "mass_fraction_<propan-1-ol>": "0.1",
        "temperature_k": "303.15",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "981.595"
      }
    ],
    "inspection_id": "INSP_859136865c90",
    "lit_num_id": "GLOBlit_590"
  }
]
```
