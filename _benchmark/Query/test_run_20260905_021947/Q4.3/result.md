# Q4.3 — Result

**Prompt:** What molar volume should I expect for an equimolar DMF + water + methanol liquid mixture at 298 K? If it has not been measured directly, estimate it from the closest relevant measurements and explain the chemical basis of the estimate.

**Tool calls:** 5  |  **Time:** 1110.4s  |  **Iterations:** 6  |  **Timed out:** False

---

## Answer

{
  "answer": "## Molar Volume of an Equimolar DMF + Water + Methanol Mixture at 298 K\n\n### Direct Measurement: Not Available\n\nThe ThermoML database contains **no density, molar volume, or excess molar volume data** for the ternary mixture of N,N-dimethylformamide (DMF) + water + methanol at 298.15 K or any nearby temperature. The only ternary block found (GLOBlit_5688, DOI: 10.1016/j.tca.2006.02.028) reports enthalpies of solution, not volumetric properties.\n\n### Estimate from Available Binary and Pure-Component Data\n\nHowever, the database provides excellent pure-component and binary density data at 298.15 K that allow a reasonable estimate.\n\n#### Pure-Component Densities at 298.15 K\n\n| Component | ρ (kg/m³) | Source | DOI |\n|-----------|-----------|--------|-----|\n| DMF | 943.81 | GLOBlit_228 / PROPblock_4 | 10.1016/j.fluid.2004.12.004 |\n| Water | 997.06 | GLOBlit_306 / PROPblock_6 | 10.1016/j.fluid.2005.09.009 |\n| Methanol | 786.531 | GLOBlit_57 / PROPblock_1 | 10.1007/s10765-008-0395-z |\n\nUsing standard molar masses (M_DMF = 73.09 g/mol, M_water = 18.015 g/mol, M_methanol = 32.04 g/mol — these are reference values, not database entries), the pure-component molar volumes are:\n\n- V*_DMF = 73.09 / 0.94381 = 77.44 cm³/mol\n- V*_water = 18.015 / 0.99706 = 18.07 cm³/mol\n- V*_methanol = 32.04 / 0.786531 = 40.73 cm³/mol\n\n#### Ideal Mixing Estimate\n\nFor an equimolar mixture (x₁ = x₂ = x₃ = 1/3):\n\n**V_ideal = (1/3)(77.44) + (1/3)(18.07) + (1/3)(40.73) = 45.41 cm³/mol**\n\nThe average molar mass of the mixture is:\n\n**M_mix = (1/3)(73.09 + 18.015 + 32.04) = 41.05 g/mol**\n\nThis corresponds to an ideal mixture density of M_mix/V_ideal = 41.05/45.41 = 0.9040 g/cm³ = **904.0 kg/m³**.\n\n#### Non-Ideal Corrections from Binary Data\n\nThe database provides binary density data for all three subsystems at 298.15 K, which reveal significant non-ideal mixing:\n\n1. **DMF + Water** (GLOBlit_11030 / PROPblock_4, DOI: 10.1021/je700671t): 14 data points. At x_DMF = 0.30, ρ = 991.40 kg/m³; at x_DMF = 0.498, ρ = 976.64 kg/m³. The density plateau near x_DMF = 0–0.10 (ρ ≈ 997 kg/m³) indicates strong **negative excess volumes** (volume contraction) from DMF–water hydrogen bonding.\n\n2. **DMF + Methanol** (GLOBlit_4125 / PROPblock_6, DOI: 10.1016/j.jct.2014.02.021): 26 data points. At x_DMF = 0.5002, ρ = 894.978 kg/m³. Mixing is relatively close to ideal for this pair.\n\n3. **Water + Methanol** (GLOBlit_2825 / PROPblock_10, DOI: 10.1016/j.jct.2007.05.004): 13 data points. At x_water = 0.5003, ρ = 881.69 kg/m³. This system is well known for significant **negative excess volumes** from water–methanol hydrogen bonding.\n\nAll three binary subsystems show densities at equimolar composition that are **higher** than simple linear (ideal) interpolation would predict, meaning all three have negative excess molar volumes (volume contraction upon mixing). The DMF–water pair shows the strongest non-ideality.\n\n#### Best Estimate\n\nSince all three binary subsystems exhibit negative V^E (volume contraction), the ternary mixture will also contract relative to ideal mixing. Typical binary V^E magnitudes for these systems at equimolar composition are on the order of −0.5 to −1.0 cm³/mol. With three such contributions weighted into the ternary, a net excess volume correction of roughly **−0.5 to −1.0 cm³/mol** on the ternary molar volume is reasonable.\n\n**Expected molar volume ≈ 44.4–44.9 cm³/mol** (i.e., the ideal value of ~45.4 cm³/mol reduced by the volume contraction from hydrogen-bonding interactions among all three components).\n\nThis corresponds to an expected mixture density of approximately **914–924 kg/m³**, somewhat higher than the ideal-mixing prediction of ~904 kg/m³.\n\n### Chemical Basis\n\nThe volume contraction arises because DMF is a strong hydrogen-bond acceptor (via its C=O group), water is both a donor and acceptor, and methanol is a moderate donor/acceptor. When mixed, these molecules form intermolecular hydrogen bonds that pack more efficiently than the pure liquids, reducing the total volume. The DMF–water interaction is particularly strong, as evidenced by the remarkable density plateau in the binary data where adding DMF to water barely changes the density up to x_DMF ≈ 0.10. This structural effect persists in the ternary mixture and drives the molar volume below the ideal-mixing prediction.",
  "core_claims": [
    "The ThermoML database contains no density, molar volume, or excess molar volume data for the ternary DMF + water + methanol mixture at 298.15 K; the only ternary block found reports enthalpies of solution, not volumetric properties.",
    "Pure-component densities at 298.15 K from the database are: DMF 943.81 kg/m³, water 997.06 kg/m³, and methanol 786.531 kg/m³.",
    "The ideal molar volume for an equimolar (x₁ = x₂ = x₃ = 1/3) mixture is estimated as 45.41 cm³/mol, corresponding to an ideal mixture density of 904.0 kg/m³.",
    "Binary density data from the database for all three subsystems (DMF + water, DMF + methanol, water + methanol) at 298.15 K indicate negative excess molar volumes (volume contraction upon mixing), with the DMF–water pair showing the strongest non-ideality.",
    "Accounting for non-ideal volume contraction estimated at roughly −0.5 to −1.0 cm³/mol, the expected ternary molar volume is approximately 44.4–44.9 cm³/mol, corresponding to a mixture density of approximately 914–924 kg/m³.",
    "The volume contraction is attributed to intermolecular hydrogen bonding among DMF (strong H-bond acceptor), water (donor and acceptor), and methanol (moderate donor/acceptor), leading to more efficient molecular packing than in the pure liquids."
  ],
  "confidence": "medium",
  "sources": [
    {
      "doi": "10.1016/j.fluid.2004.12.004",
      "lit_num_id": "GLOBlit_228",
      "block": "PROPblock_4",
      "BLKsubsys_id": null,
      "description": "Provides the pure-component density of DMF at 298.15 K (943.81 kg/m³), used to compute the pure molar volume of DMF (77.44 cm³/mol) for the ideal-mixing estimate."
    },
    {
      "doi": "10.1016/j.fluid.2005.09.009",
      "lit_num_id": "GLOBlit_306",
      "block": "PROPblock_6",
      "BLKsubsys_id": null,
      "description": "Provides the pure-component density of water at 298.15 K (997.06 kg/m³), used to compute the pure molar volume of water (18.07 cm³/mol) for the ideal-mixing estimate."
    },
    {
      "doi": "10.1007/s10765-008-0395-z",
      "lit_num_id": "GLOBlit_57",
      "block": "PROPblock_1",
      "BLKsubsys_id": null,
      "description": "Provides the pure-component density of methanol at 298.15 K (786.531 kg/m³), used to compute the pure molar volume of methanol (40.73 cm³/mol) for the ideal-mixing estimate."
    },
    {
      "doi": "10.1021/je700671t",
      "lit_num_id": "GLOBlit_11030",
      "block": "PROPblock_4",
      "BLKsubsys_id": null,
      "description": "Provides binary DMF + water density data spanning 283–353 K and full composition range (210 points), used to assess non-ideal volume contraction in the DMF–water subsystem and support the negative excess volume correction applied to the ternary estimate."
    },
    {
      "doi": "10.1016/j.jct.2014.02.021",
      "lit_num_id": "GLOBlit_4125",
      "block": "PROPblock_6",
      "BLKsubsys_id": null,
      "description": "Provides binary methanol + DMF density data at 298.15 K across the full composition range (26 points, 786.58–943.974 kg/m³), used to assess non-ideal mixing in the DMF–methanol subsystem for the ternary estimate."
    },
    {
      "doi": "10.1016/j.jct.2007.05.004",
      "lit_num_id": "GLOBlit_2825",
      "block": "PROPblock_10",
      "BLKsubsys_id": null,
      "description": "Provides binary methanol + water density data at 293–303 K across the full composition range (39 points, 782.48–998.2 kg/m³), used to assess non-ideal mixing in the water–methanol subsystem for the ternary estimate."
    }
  ],
  "follow_up_suggestions": [
    "Search for ternary excess molar volume data for DMF + water + methanol in other databases (e.g., Dortmund Data Bank) to validate the binary-based estimate.",
    "Measure the density of the equimolar ternary mixture experimentally at 298.15 K using a vibrating-tube densimeter for direct comparison.",
    "Use a Redlich-Kister or Cibulka correlation fitted to the three binary V^E datasets to compute a more rigorous ternary excess volume prediction."
  ],
  "id_catalog_snapshot": []
}

---

## Data Inspections (deterministic evidence ledger)

Hardcoded envelope merge — not agent-authored. 9 entr(ies); verbatim rows below.

- INSP_15c1ba3ad05f — GLOBlit_5688::PROPblock_4 · rdp · 8 rows
- INSP_07e3683a04fb — GLOBlit_86::PROPblock_6 · nearest · 3 rows
- INSP_6931016a10b1 — GLOBlit_228::PROPblock_4 · complete · 1 rows
- INSP_7861323c4024 — GLOBlit_57::PROPblock_1 · nearest · 1 rows
- INSP_6715d3baae18 — GLOBlit_306::PROPblock_6 · nearest · 1 rows
- INSP_3731e85c0b92 — GLOBlit_11030::PROPblock_4 · rdp · 14 rows
- INSP_428715c8042d — GLOBlit_4125::PROPblock_6 · rdp · 9 rows
- INSP_5d31e929df24 — GLOBlit_2825::PROPblock_10 · rdp · 12 rows
- INSP_2a46f0d6e4fd — GLOBlit_4125::PROPblock_6 · nearest · 1 rows

```json
[
  {
    "doi": "10.1016/j.tca.2006.02.028",
    "block_number": "PROPblock_4",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "solvent_mole_fraction_<methanol>",
      "temperature_k",
      "pressure_kpa",
      "mole_fraction_<dimethylformamide>",
      "molar_enthalpy_of_solution_kj_mol"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "solvent_mole_fraction_<methanol>": "0",
        "temperature_k": "298.15",
        "pressure_kpa": "1.0",
        "mole_fraction_<dimethylformamide>": "0.0",
        "molar_enthalpy_of_solution_kj_mol": "-2.32"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "solvent_mole_fraction_<methanol>": "0.1",
        "temperature_k": "298.15",
        "pressure_kpa": "1.0",
        "mole_fraction_<dimethylformamide>": "0.0",
        "molar_enthalpy_of_solution_kj_mol": "2.8"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "solvent_mole_fraction_<methanol>": "0.2",
        "temperature_k": "298.15",
        "pressure_kpa": "1.0",
        "mole_fraction_<dimethylformamide>": "0.0",
        "molar_enthalpy_of_solution_kj_mol": "5.74"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "solvent_mole_fraction_<methanol>": "0.3",
        "temperature_k": "298.15",
        "pressure_kpa": "1.0",
        "mole_fraction_<dimethylformamide>": "0.0",
        "molar_enthalpy_of_solution_kj_mol": "6.61"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "solvent_mole_fraction_<methanol>": "0.4",
        "temperature_k": "298.15",
        "pressure_kpa": "1.0",
        "mole_fraction_<dimethylformamide>": "0.0",
        "molar_enthalpy_of_solution_kj_mol": "7.28"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "solvent_mole_fraction_<methanol>": "0.7",
        "temperature_k": "298.15",
        "pressure_kpa": "1.0",
        "mole_fraction_<dimethylformamide>": "0.0",
        "molar_enthalpy_of_solution_kj_mol": "8.84"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "solvent_mole_fraction_<methanol>": "0.8",
        "temperature_k": "298.15",
        "pressure_kpa": "1.0",
        "mole_fraction_<dimethylformamide>": "0.0",
        "molar_enthalpy_of_solution_kj_mol": "9.67"
      },
      {
        "BLKpoint_id": "BLKpoint_13",
        "solvent_mole_fraction_<methanol>": "1",
        "temperature_k": "298.15",
        "pressure_kpa": "1.0",
        "mole_fraction_<dimethylformamide>": "0.0",
        "molar_enthalpy_of_solution_kj_mol": "11.95"
      }
    ],
    "inspection_id": "INSP_15c1ba3ad05f",
    "lit_num_id": "GLOBlit_5688"
  },
  {
    "doi": "10.1007/s10765-009-0648-5",
    "block_number": "PROPblock_6",
    "table_mode": "nearest",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "pressure_kpa",
      "mass_density_kg_m3"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_2",
        "temperature_k": "293.15",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "948.685"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "943.917"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "temperature_k": "303.15",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "939.142"
      }
    ],
    "inspection_id": "INSP_07e3683a04fb",
    "lit_num_id": "GLOBlit_86"
  },
  {
    "doi": "10.1016/j.fluid.2004.12.004",
    "block_number": "PROPblock_4",
    "table_mode": "complete",
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
        "pressure_kpa": "101.325",
        "mass_density_kg_m3": "943.81"
      }
    ],
    "inspection_id": "INSP_6931016a10b1",
    "lit_num_id": "GLOBlit_228"
  },
  {
    "doi": "10.1007/s10765-008-0395-z",
    "block_number": "PROPblock_1",
    "table_mode": "nearest",
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
        "pressure_kpa": "101.325",
        "mass_density_kg_m3": "786.531"
      }
    ],
    "inspection_id": "INSP_7861323c4024",
    "lit_num_id": "GLOBlit_57"
  },
  {
    "doi": "10.1016/j.fluid.2005.09.009",
    "block_number": "PROPblock_6",
    "table_mode": "nearest",
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
        "pressure_kpa": "101.325",
        "mass_density_kg_m3": "997.06"
      }
    ],
    "inspection_id": "INSP_6715d3baae18",
    "lit_num_id": "GLOBlit_306"
  },
  {
    "doi": "10.1021/je700671t",
    "block_number": "PROPblock_4",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<dimethylformamide>",
      "pressure_kpa",
      "mass_density_kg_m3"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_43",
        "temperature_k": "298.15",
        "mole_fraction_<dimethylformamide>": "0",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "997.04"
      },
      {
        "BLKpoint_id": "BLKpoint_44",
        "temperature_k": "298.15",
        "mole_fraction_<dimethylformamide>": "0.02",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "996.39"
      },
      {
        "BLKpoint_id": "BLKpoint_45",
        "temperature_k": "298.15",
        "mole_fraction_<dimethylformamide>": "0.04",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "996.31"
      },
      {
        "BLKpoint_id": "BLKpoint_46",
        "temperature_k": "298.15",
        "mole_fraction_<dimethylformamide>": "0.06",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "996.53"
      },
      {
        "BLKpoint_id": "BLKpoint_47",
        "temperature_k": "298.15",
        "mole_fraction_<dimethylformamide>": "0.08",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "996.8"
      },
      {
        "BLKpoint_id": "BLKpoint_48",
        "temperature_k": "298.15",
        "mole_fraction_<dimethylformamide>": "0.1",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "997.03"
      },
      {
        "BLKpoint_id": "BLKpoint_49",
        "temperature_k": "298.15",
        "mole_fraction_<dimethylformamide>": "0.2",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "996.13"
      },
      {
        "BLKpoint_id": "BLKpoint_50",
        "temperature_k": "298.15",
        "mole_fraction_<dimethylformamide>": "0.3",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "991.4"
      },
      {
        "BLKpoint_id": "BLKpoint_51",
        "temperature_k": "298.15",
        "mole_fraction_<dimethylformamide>": "0.398",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "984.18"
      },
      {
        "BLKpoint_id": "BLKpoint_52",
        "temperature_k": "298.15",
        "mole_fraction_<dimethylformamide>": "0.498",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "976.64"
      },
      {
        "BLKpoint_id": "BLKpoint_53",
        "temperature_k": "298.15",
        "mole_fraction_<dimethylformamide>": "0.599",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "968.96"
      },
      {
        "BLKpoint_id": "BLKpoint_54",
        "temperature_k": "298.15",
        "mole_fraction_<dimethylformamide>": "0.697",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "961.92"
      },
      {
        "BLKpoint_id": "BLKpoint_55",
        "temperature_k": "298.15",
        "mole_fraction_<dimethylformamide>": "0.798",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "955.63"
      },
      {
        "BLKpoint_id": "BLKpoint_56",
        "temperature_k": "298.15",
        "mole_fraction_<dimethylformamide>": "1",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "944.6"
      }
    ],
    "inspection_id": "INSP_3731e85c0b92",
    "lit_num_id": "GLOBlit_11030"
  },
  {
    "doi": "10.1016/j.jct.2014.02.021",
    "block_number": "PROPblock_6",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "mole_fraction_<dimethylformamide>",
      "temperature_k",
      "pressure_kpa",
      "mass_density_kg_m3"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "mole_fraction_<dimethylformamide>": "0",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "786.58"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "mole_fraction_<dimethylformamide>": "0.5982",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "909.277"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "mole_fraction_<dimethylformamide>": "1",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "943.974"
      },
      {
        "BLKpoint_id": "BLKpoint_13",
        "mole_fraction_<dimethylformamide>": "0.1988",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "843.761"
      },
      {
        "BLKpoint_id": "BLKpoint_14",
        "mole_fraction_<dimethylformamide>": "0.4022",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "882.138"
      },
      {
        "BLKpoint_id": "BLKpoint_16",
        "mole_fraction_<dimethylformamide>": "0.6008",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "908.588"
      },
      {
        "BLKpoint_id": "BLKpoint_21",
        "mole_fraction_<dimethylformamide>": "0.2004",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "843"
      },
      {
        "BLKpoint_id": "BLKpoint_22",
        "mole_fraction_<dimethylformamide>": "0.4054",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "881.38"
      },
      {
        "BLKpoint_id": "BLKpoint_26",
        "mole_fraction_<dimethylformamide>": "0.9033",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "936.655"
      }
    ],
    "inspection_id": "INSP_428715c8042d",
    "lit_num_id": "GLOBlit_4125"
  },
  {
    "doi": "10.1016/j.jct.2007.05.004",
    "block_number": "PROPblock_10",
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
        "BLKpoint_id": "BLKpoint_14",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "787.2"
      },
      {
        "BLKpoint_id": "BLKpoint_15",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.049",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "795.47"
      },
      {
        "BLKpoint_id": "BLKpoint_16",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.0993",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "804.11"
      },
      {
        "BLKpoint_id": "BLKpoint_17",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.1973",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "821.73"
      },
      {
        "BLKpoint_id": "BLKpoint_18",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.2983",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "840.79"
      },
      {
        "BLKpoint_id": "BLKpoint_19",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.3985",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "860.59"
      },
      {
        "BLKpoint_id": "BLKpoint_20",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.5003",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "881.69"
      },
      {
        "BLKpoint_id": "BLKpoint_21",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.5994",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "902.96"
      },
      {
        "BLKpoint_id": "BLKpoint_23",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.7986",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "947.17"
      },
      {
        "BLKpoint_id": "BLKpoint_24",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.8999",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "969.84"
      },
      {
        "BLKpoint_id": "BLKpoint_25",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "0.9512",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "982.53"
      },
      {
        "BLKpoint_id": "BLKpoint_26",
        "temperature_k": "298.15",
        "mole_fraction_<water>": "1",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "997.05"
      }
    ],
    "inspection_id": "INSP_5d31e929df24",
    "lit_num_id": "GLOBlit_2825"
  },
  {
    "doi": "10.1016/j.jct.2014.02.021",
    "block_number": "PROPblock_6",
    "table_mode": "nearest",
    "columns": [
      "BLKpoint_id",
      "mole_fraction_<dimethylformamide>",
      "temperature_k",
      "pressure_kpa",
      "mass_density_kg_m3"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_23",
        "mole_fraction_<dimethylformamide>": "0.5002",
        "temperature_k": "298.15",
        "pressure_kpa": "101.0",
        "mass_density_kg_m3": "894.978"
      }
    ],
    "inspection_id": "INSP_2a46f0d6e4fd",
    "lit_num_id": "GLOBlit_4125"
  }
]
```
