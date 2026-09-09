{
  "answer": "**No meaningful excess molar enthalpy (Hᴱ) data found for the binary system 1-propanol + water in the ThermoML database.**\n\nA comprehensive search was conducted:\n\n1. **Direct binary search** (declared scope) for GLOBcomp_5 (1-propanol) + GLOBcomp_1 (water) with GLOBprop_17 (excess molar enthalpy) returned **zero blocks** — both with and without temperature constraints.\n\n2. **Subsystem search** (scope = \"either\") found only **one block**: GLOBlit_1766 (DOI: 10.1016/j.fluid.2015.07.053), PROPblock_1, BLKsubsys_1. This is a binary subsystem extracted from a ternary (propan-1-ol + water + acetic acid) dataset. However, it contains only **3 data points**, all with **Hᴱ = 0 kJ/mol** at mole fractions of 0.25, 0.50, and 0.75 — and at **313.15 K**. These zero values represent the acetic-acid-free boundary of the ternary system and do not constitute useful binary mixing enthalpy data.\n\n3. **Broad search** for any Hᴱ blocks involving 1-propanol (without specifying water) returned 50 blocks across many partner compounds, but **none with water** as the second component in a declared binary system.\n\n**Conclusion:** The ThermoML database does not contain excess molar enthalpy data for the 1-propanol + water binary system. No composition-dependent Hᴱ data spanning the full mole fraction range is available for this system.",
  "core_claims": [
    "No meaningful excess molar enthalpy (Hᴱ) data for the binary system 1-propanol + water were found in the ThermoML database; the only related block found (GLOBlit_1766, DOI: 10.1016/j.fluid.2015.07.053) is a binary subsystem extracted from a ternary dataset containing only 3 data points all with Hᴱ = 0 kJ/mol, representing the acetic-acid-free boundary rather than useful binary mixing enthalpy data, and a broad search for any Hᴱ blocks involving 1-propanol returned 50 blocks across many partner compounds but none with water as the second component in a declared binary system."
  ],
  "status": "no_results",
  "summary": "No meaningful excess molar enthalpy (Hᴱ) data were found for the binary system 1-propanol + water in the ThermoML database. A direct binary search returned zero blocks. A subsystem search found only one block (DOI: 10.1016/j.fluid.2015.07.053), containing 3 data points all with Hᴱ = 0 kJ/mol at mole fractions of 0.25, 0.50, and 0.75 at 313.15 K; these are the acetic-acid-free boundary of a ternary (propan-1-ol + water + acetic acid) dataset and do not constitute useful binary mixing enthalpy data. A broad search for any Hᴱ blocks involving 1-propanol returned 50 blocks across many partner compounds, but none with water as the second component in a declared binary system. No composition-dependent Hᴱ data spanning the full mole fraction range is available for this system.",
  "core_id_updates": [],
  "core_blocks_found": [],
  "data_inspections": [
    {
      "doi": "10.1016/j.fluid.2015.07.053",
      "block_number": "PROPblock_1",
      "table_mode": "complete",
      "columns": [
        "BLKpoint_id",
        "mole_fraction_<propan-1-ol>",
        "temperature_k",
        "pressure_kpa",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "mole_fraction_<propan-1-ol>": "0.5",
          "temperature_k": "313.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0"
        },
        {
          "BLKpoint_id": "BLKpoint_22",
          "mole_fraction_<propan-1-ol>": "0.75",
          "temperature_k": "313.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0"
        },
        {
          "BLKpoint_id": "BLKpoint_41",
          "mole_fraction_<propan-1-ol>": "0.25",
          "temperature_k": "313.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0"
        }
      ],
      "inspection_id": "INSP_a2b2c0724aa7",
      "lit_num_id": "GLOBlit_1766",
      "BLKsubsys_id": "BLKsubsys_1"
    }
  ]
}