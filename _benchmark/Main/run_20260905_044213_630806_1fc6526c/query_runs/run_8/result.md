# Delegated query run — result

**Question:** Find blocks with viscosity or dynamic viscosity data for the binary system water (GLOBcomp_1) + dimethyl sulfoxide (GLOBcomp_31) near 298.15 K. Report block numbers, literature IDs, DOIs, temperature ranges, and composition ranges.

**Iterations:** 2  |  **Elapsed:** 209.3s  |  **Tools:** 1  |  **Timed out:** False

---

## Answer

{
  "answer": "## Viscosity Data for Water + DMSO Binary System near 298.15 K\n\nTwo data blocks in the ThermoML database contain dynamic viscosity measurements for the binary system water + dimethyl sulfoxide (DMSO) at 298.15 K and 101 kPa.\n\n---\n\n### Block 1: GLOBlit_2781 :: PROPblock_3\n\n| Feature | Detail |\n|---------|--------|\n| **Literature ID** | GLOBlit_2781 |\n| **DOI** | 10.1016/j.jct.2006.12.012 |\n| **Property** | Dynamic viscosity (GLOBprop_4), Pa·s |\n| **Temperature range** | 298.15–318.15 K |\n| **Composition variable** | Mole fraction of DMSO, x = 0–1 (24 unique compositions) |\n| **Pressure** | 101.0 kPa (constant) |\n| **Total data points** | 120 |\n| **Viscosity range (full block)** | 0.000596–0.003735 Pa·s |\n| **Measurement method** | Capillary tube (GLOBmeas_140) |\n\n**Selected data at 298.15 K (18 of 24 compositions shown):**\n\n| x(DMSO) | η (Pa·s) |\n|---------|----------|\n| 0 | 0.0008901 |\n| 0.0238 | 0.0010331 |\n| 0.0489 | 0.0012576 |\n| 0.1587 | 0.0025493 |\n| 0.2036 | 0.0030165 |\n| 0.2379 | 0.0033011 |\n| 0.2768 | 0.0035372 |\n| 0.3074 | 0.0036564 |\n| 0.3335 | 0.0037144 |\n| **0.3638** | **0.0037353** |\n| 0.3906 | 0.0037169 |\n| 0.4412 | 0.0036062 |\n| 0.5193 | 0.0033124 |\n| 0.6195 | 0.0028832 |\n| 0.6813 | 0.0026556 |\n| 0.7595 | 0.0024317 |\n| 0.8856 | 0.0021754 |\n| 1 | 0.001996 |\n\n---\n\n### Block 2: GLOBlit_11517 :: PROPblock_3\n\n| Feature | Detail |\n|---------|--------|\n| **Literature ID** | GLOBlit_11517 |\n| **DOI** | 10.1021/je9001027 |\n| **Property** | Dynamic viscosity (GLOBprop_4), Pa·s |\n| **Temperature range** | 298.15–318.15 K |\n| **Composition variable** | Mass fraction of DMSO, w = 0–1 (7 unique compositions) |\n| **Pressure** | 101.0 kPa (constant) |\n| **Total data points** | 35 |\n| **Viscosity range (full block)** | 0.000535–0.003421 Pa·s |\n| **Measurement method** | Capillary tube (GLOBmeas_205) |\n\n**Complete data at 298.15 K:**\n\n| w(DMSO) | η (Pa·s) |\n|---------|----------|\n| 0 | 0.00089 |\n| 0.2 | 0.00134 |\n| 0.4 | 0.002221 |\n| 0.5 | 0.0028073 |\n| **0.6** | **0.003421** |\n| 0.7 | 0.0023568 |\n| 1 | 0.001966 |\n\n---\n\n### Summary Comparison\n\n| Feature | Block 1 (GLOBlit_2781) | Block 2 (GLOBlit_11517) |\n|---------|----------------------|----------------------|\n| DOI | 10.1016/j.jct.2006.12.012 | 10.1021/je9001027 |\n| Composition variable | Mole fraction | Mass fraction |\n| Points at 298.15 K | 24 | 7 |\n| η range at 298.15 K | 0.0008901–0.0037353 Pa·s | 0.00089–0.003421 Pa·s |\n| Viscosity maximum location | x(DMSO) ≈ 0.36 | w(DMSO) ≈ 0.6 (~x ≈ 0.33) |\n| Maximum η value | 0.0037353 Pa·s | 0.003421 Pa·s |\n\n### Chemistry Insight\n\nBoth datasets reveal a **pronounced viscosity maximum** in the water-rich region near x(DMSO) ≈ 0.33–0.36. At this composition, the mixture viscosity (0.0037353 Pa·s in Block 1) is roughly **4.2 times** that of pure water (0.0008901 Pa·s) and nearly **1.9 times** that of pure DMSO (0.001996 Pa·s). This dramatic non-ideal behavior arises because DMSO is a strong hydrogen-bond acceptor: its S=O group forms robust H-bonds with water, creating structured 1:2 DMSO–water hydration complexes that resist shear flow. The maximum near x ≈ 0.33 (i.e., 1 DMSO per 2 water molecules) is consistent with this stoichiometric clustering picture. Block 1 (GLOBlit_2781 :: PROPblock_3) provides the most detailed composition resolution for studying this phenomenon.",
  "core_claims": [
    "Two ThermoML data blocks contain dynamic viscosity measurements for the water + DMSO binary system at 298.15 K and 101.0 kPa: GLOBlit_2781 (DOI 10.1016/j.jct.2006.12.012, 24 compositions in mole fraction) and GLOBlit_11517 (DOI 10.1021/je9001027, 7 compositions in mass fraction).",
    "Both datasets reveal a pronounced viscosity maximum in the water-rich region near x(DMSO) ≈ 0.33–0.36, with the more detailed Block 1 reporting a maximum of 0.0037353 Pa·s at x(DMSO) ≈ 0.36.",
    "At the viscosity maximum, the mixture viscosity (0.0037353 Pa·s) is roughly 4.2 times that of pure water (0.0008901 Pa·s) and nearly 1.9 times that of pure DMSO (0.001996 Pa·s), indicating strongly non-ideal mixing behavior.",
    "The viscosity maximum near x ≈ 0.33 is consistent with the formation of structured 1:2 DMSO–water hydration complexes driven by hydrogen bonding between DMSO's S=O group and water.",
    "Block 1 (GLOBlit_2781 :: PROPblock_3) provides the most detailed composition resolution with 24 compositions at 298.15 K, compared to 7 compositions in Block 2."
  ],
  "confidence": "high",
  "sources": [
    {
      "doi": "10.1016/j.jct.2006.12.012",
      "lit_num_id": "GLOBlit_2781",
      "block": "PROPblock_3",
      "BLKsubsys_id": null,
      "description": "Provides detailed dynamic viscosity data (120 points) for the water + DMSO binary system at 298.15–318.15 K across 24 mole fraction compositions, directly supporting the answer's primary dataset including the viscosity maximum near x(DMSO) ≈ 0.36."
    },
    {
      "doi": "10.1021/je9001027",
      "lit_num_id": "GLOBlit_11517",
      "block": "PROPblock_3",
      "BLKsubsys_id": null,
      "description": "Provides complementary dynamic viscosity data (35 points) for the water + DMSO binary system at 298.15–318.15 K across 7 mass fraction compositions, serving as the answer's second dataset for cross-validation of the viscosity maximum and pure-component values."
    }
  ],
  "follow_up_suggestions": [
    "Retrieve excess molar volume data for water+DMSO near 298.15 K to correlate structural changes with the viscosity maximum.",
    "Search for viscosity data at additional temperatures (e.g., 288.15–338.15 K) to examine how the viscosity maximum shifts with temperature.",
    "Look for refractive index or speed-of-sound data for water+DMSO to further characterize the non-ideal mixing behavior near x(DMSO) ≈ 0.33."
  ],
  "id_catalog_snapshot": []
}

---

## Data Inspections (deterministic evidence ledger)

Hardcoded envelope merge — not agent-authored. 2 entr(ies); verbatim rows below.

- INSP_b08a03233872 — GLOBlit_2781::PROPblock_3 · rdp · 18 rows
- INSP_c018a8ec4dd8 — GLOBlit_11517::PROPblock_3 · complete · 7 rows

```json
[
  {
    "doi": "10.1016/j.jct.2006.12.012",
    "block_number": "PROPblock_3",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<dimethyl sulfoxide>",
      "pressure_kpa",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0008901"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.0238",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0010331"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.0489",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0012576"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.1587",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0025493"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.2036",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0030165"
      },
      {
        "BLKpoint_id": "BLKpoint_8",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.2379",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0033011"
      },
      {
        "BLKpoint_id": "BLKpoint_9",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.2768",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0035372"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.3074",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0036564"
      },
      {
        "BLKpoint_id": "BLKpoint_11",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.3335",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0037144"
      },
      {
        "BLKpoint_id": "BLKpoint_12",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.3638",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0037353"
      },
      {
        "BLKpoint_id": "BLKpoint_13",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.3906",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0037169"
      },
      {
        "BLKpoint_id": "BLKpoint_14",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.4412",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0036062"
      },
      {
        "BLKpoint_id": "BLKpoint_15",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.5193",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0033124"
      },
      {
        "BLKpoint_id": "BLKpoint_17",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.6195",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0028832"
      },
      {
        "BLKpoint_id": "BLKpoint_18",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.6813",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0026556"
      },
      {
        "BLKpoint_id": "BLKpoint_19",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.7595",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0024317"
      },
      {
        "BLKpoint_id": "BLKpoint_21",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "0.8856",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0021754"
      },
      {
        "BLKpoint_id": "BLKpoint_24",
        "temperature_k": "298.15",
        "mole_fraction_<dimethyl sulfoxide>": "1",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001996"
      }
    ],
    "inspection_id": "INSP_b08a03233872",
    "lit_num_id": "GLOBlit_2781"
  },
  {
    "doi": "10.1021/je9001027",
    "block_number": "PROPblock_3",
    "table_mode": "complete",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mass_fraction_<dimethyl sulfoxide>",
      "pressure_kpa",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "temperature_k": "298.15",
        "mass_fraction_<dimethyl sulfoxide>": "0",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.00089"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "temperature_k": "298.15",
        "mass_fraction_<dimethyl sulfoxide>": "0.2",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.00134"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "temperature_k": "298.15",
        "mass_fraction_<dimethyl sulfoxide>": "0.4",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.002221"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "temperature_k": "298.15",
        "mass_fraction_<dimethyl sulfoxide>": "0.5",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0028073"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "temperature_k": "298.15",
        "mass_fraction_<dimethyl sulfoxide>": "0.6",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.003421"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "temperature_k": "298.15",
        "mass_fraction_<dimethyl sulfoxide>": "0.7",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0023568"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "temperature_k": "298.15",
        "mass_fraction_<dimethyl sulfoxide>": "1",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.001966"
      }
    ],
    "inspection_id": "INSP_c018a8ec4dd8",
    "lit_num_id": "GLOBlit_11517"
  }
]
```
