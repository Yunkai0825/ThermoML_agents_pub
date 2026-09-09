# Delegated query run — result

**Question:** Find viscosity data for the binary mixture of ethanol and water at 25°C (298.15 K), especially near equimolar composition (mole fraction ~0.5). I need both mixture viscosity values and pure component viscosities to assess deviation from ideal mixing.

**Iterations:** 2  |  **Elapsed:** 187.7s  |  **Tools:** 1  |  **Timed out:** False

---

## Answer

{
  "answer": "## Dynamic Viscosity of Ethanol + Water Binary Mixtures at 298.15 K\n\nTwo comprehensive experimental datasets were found in the ThermoML database for the dynamic viscosity of ethanol + water binary mixtures at 298.15 K (25 °C).\n\n---\n\n### Dataset 1 — DOI: 10.1016/j.jct.2007.05.004\n\n**Source block:** PROPblock_11 · Pressure: 101.0 kPa · 12 data points at 298.15 K · Method: Capillary tube viscometry  \nComposition expressed as **mole fraction of water**.\n\n| x(water) | η (Pa·s) |\n|-----------|-----------|\n| 0 (pure ethanol) | 0.001082 |\n| 0.0501 | 0.001153 |\n| 0.0986 | 0.001232 |\n| 0.1961 | 0.001380 |\n| 0.2961 | 0.001531 |\n| 0.3991 | 0.001659 |\n| 0.5989 | 0.002115 |\n| 0.6991 | 0.002275 |\n| 0.8001 | **0.002300** (maximum) |\n| 0.8996 | 0.001860 |\n| 0.9499 | 0.001388 |\n| 1 (pure water) | 0.000890 |\n\n---\n\n### Dataset 2 — DOI: 10.1016/j.jct.2018.02.022\n\n**Source block:** PROPblock_21 · Pressure: 92.3 kPa · 25 data points at 298.15 K · Method: Concentric cylinders viscometry  \nComposition expressed as **mole fraction of ethanol**.\n\n| x(ethanol) | x(water) | η (Pa·s) |\n|------------|----------|-----------|\n| 0 (pure water) | 1 | 0.00089689 |\n| 0.0201 | ~0.98 | 0.001098 |\n| 0.1004 | ~0.90 | 0.0019469 |\n| 0.1499 | ~0.85 | 0.0022424 |\n| 0.1984 | ~0.80 | 0.0023706 |\n| 0.2499 | ~0.75 | **0.0024286** (maximum) |\n| 0.3499 | ~0.65 | 0.0022633 |\n| 0.3990 | ~0.60 | 0.0021697 |\n| **0.4989** | **~0.50** | **0.0019557** |\n| 0.5495 | ~0.45 | 0.0018796 |\n| 0.6067 | ~0.39 | 0.0017439 |\n| 0.6956 | ~0.30 | 0.0015722 |\n| 0.8475 | ~0.15 | 0.0013415 |\n| 1 (pure ethanol) | 0 | 0.0010914 |\n\n---\n\n### Pure Component Viscosities at 298.15 K\n\n| Component | Dataset 1 (η, Pa·s) | Dataset 2 (η, Pa·s) |\n|-----------|---------------------|---------------------|\n| Water | 0.000890 | 0.00089689 |\n| Ethanol | 0.001082 | 0.0010914 |\n\nThe two datasets agree closely: η(water) ≈ 0.00089–0.00090 Pa·s and η(ethanol) ≈ 0.00108–0.00109 Pa·s.\n\n---\n\n### Near-Equimolar Composition (x ≈ 0.5)\n\n- **Dataset 2** provides a direct measurement at x(ethanol) = 0.4989 (essentially equimolar): **η = 0.0019557 Pa·s**.\n- **Dataset 1** has its nearest point at x(water) = 0.5989 (x(ethanol) ≈ 0.40): η = 0.002115 Pa·s — slightly off equimolar but consistent with the trend.\n\nAt equimolar composition, the mixture viscosity (~0.00196 Pa·s) is roughly **double** that of either pure component (~0.001 Pa·s), demonstrating a very large positive deviation from ideal mixing.\n\n---\n\n### Deviation from Ideal Mixing — Analysis\n\nFor a simple linear (mole-fraction-weighted) ideal mixing rule:\n\n> η_ideal(x = 0.5) ≈ 0.5 × 0.00109 + 0.5 × 0.00090 ≈ 0.00100 Pa·s\n\nThe measured value at x(ethanol) ≈ 0.50 is **0.0019557 Pa·s** — nearly **twice** the ideal estimate. The excess viscosity (η_mix − η_ideal) at this composition is approximately +0.00096 Pa·s.\n\nEven more striking, the **viscosity maximum** does not occur at equimolar composition but is shifted strongly toward the water-rich side:\n\n- Dataset 1: maximum η = 0.002300 Pa·s at x(water) ≈ 0.80 (x(ethanol) ≈ 0.20)\n- Dataset 2: maximum η = 0.0024286 Pa·s at x(ethanol) ≈ 0.25 (x(water) ≈ 0.75)\n\nThe peak viscosity exceeds the ideal value by more than a **factor of 2.4**. This large positive excess viscosity is a hallmark of the ethanol–water system and is attributed to:\n\n1. **Extensive hydrogen-bond network reorganization** — water's tetrahedral H-bond network is disrupted and reformed around ethanol's hydrophobic methyl/methylene groups.\n2. **Microheterogeneity** — at water-rich compositions, ethanol molecules cluster into transient aggregates surrounded by structured water shells, increasing internal friction.\n3. **Asymmetric maximum** — the shift of the viscosity peak toward x(water) ≈ 0.75–0.80 reflects the stoichiometry of the most stable ethanol–water hydrogen-bonded complexes (roughly 1 ethanol : 3 water molecules).",
  "core_claims": [
    "Two ThermoML datasets (DOI: 10.1016/j.jct.2007.05.004 and DOI: 10.1016/j.jct.2018.02.022) provide dynamic viscosity data for ethanol + water binary mixtures at 298.15 K, with 12 and 25 data points respectively.",
    "Pure-component viscosities at 298.15 K agree closely between the two datasets: η(water) ≈ 0.00089–0.00090 Pa·s and η(ethanol) ≈ 0.00108–0.00109 Pa·s.",
    "At near-equimolar composition (x(ethanol) = 0.4989), Dataset 2 reports η = 0.0019557 Pa·s, which is approximately twice the value of either pure component (~0.001 Pa·s), demonstrating a large positive deviation from ideal mixing.",
    "The viscosity maximum does not occur at equimolar composition but is shifted toward the water-rich side: Dataset 1 reports a maximum of 0.002300 Pa·s at x(water) ≈ 0.80, and Dataset 2 reports a maximum of 0.0024286 Pa·s at x(ethanol) ≈ 0.25 (x(water) ≈ 0.75).",
    "The large positive excess viscosity is attributed to extensive hydrogen-bond network reorganization, microheterogeneity with transient ethanol aggregates in structured water shells, and the stoichiometry of the most stable ethanol–water hydrogen-bonded complexes (roughly 1 ethanol : 3 water molecules)."
  ],
  "confidence": "high",
  "sources": [
    {
      "doi": "10.1016/j.jct.2007.05.004",
      "lit_num_id": "GLOBlit_2825",
      "block": "PROPblock_11",
      "BLKsubsys_id": null,
      "description": "Provides dynamic viscosity of ethanol + water binary mixtures across the full mole-fraction range at 298.15 K (block spans 293.15–303.15 K), measured by capillary tube viscometry at 101.0 kPa. The answer quotes 12 data points from this block including pure-component values and the viscosity maximum near x(water) ≈ 0.80."
    },
    {
      "doi": "10.1016/j.jct.2018.02.022",
      "lit_num_id": "GLOBlit_5201",
      "block": "PROPblock_21",
      "BLKsubsys_id": null,
      "description": "Provides dynamic viscosity of ethanol + water binary mixtures across the full mole-fraction range at 298.15 K (block spans 293.15–308.15 K), measured by concentric cylinders viscometry at 92.3 kPa. The answer quotes 14 data points from this block including the near-equimolar measurement at x(ethanol) = 0.4989 and the viscosity maximum near x(ethanol) ≈ 0.25."
    }
  ],
  "follow_up_suggestions": [
    "Search for excess molar volume data for ethanol+water at 298.15 K to complement the viscosity deviation analysis.",
    "Look for temperature-dependent viscosity data (e.g., 288–318 K) for ethanol+water to assess how the viscosity maximum shifts with temperature.",
    "Search for kinematic viscosity or density data at matching compositions to cross-validate the dynamic viscosity values.",
    "Investigate ternary mixture viscosity data (e.g., ethanol+water+methanol) to compare hydrogen-bonding effects across similar systems."
  ],
  "id_catalog_snapshot": [
    {
      "type": "comp",
      "global_id": "GLOBcomp_2",
      "registry_id": "ethanol",
      "name": "ethanol"
    },
    {
      "type": "comp",
      "global_id": "GLOBcomp_1",
      "registry_id": "water",
      "name": "water"
    },
    {
      "type": "prop",
      "global_id": "GLOBprop_4",
      "registry_id": "viscosity_pa_s",
      "name": "Viscosity, Pa*s"
    }
  ]
}

---

## Data Inspections (deterministic evidence ledger)

Hardcoded envelope merge — not agent-authored. 3 entr(ies); verbatim rows below.

- INSP_f0616a9dca18 — GLOBlit_2825::PROPblock_11 · complete · 12 rows
- INSP_d0495ab20e5e — GLOBlit_5201::PROPblock_21 · rdp · 14 rows
- INSP_a80f5dc78817 — GLOBlit_5201::PROPblock_21 · nearest · 1 rows

```json
[
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
    "doi": "10.1016/j.jct.2018.02.022",
    "block_number": "PROPblock_21",
    "table_mode": "rdp",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<ethanol>",
      "pressure_kpa",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_24",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.0201",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.001098"
      },
      {
        "BLKpoint_id": "BLKpoint_29",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.1004",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0019469"
      },
      {
        "BLKpoint_id": "BLKpoint_30",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.1499",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0022424"
      },
      {
        "BLKpoint_id": "BLKpoint_31",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.1984",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0023706"
      },
      {
        "BLKpoint_id": "BLKpoint_32",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.2499",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0024286"
      },
      {
        "BLKpoint_id": "BLKpoint_34",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.3499",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0022633"
      },
      {
        "BLKpoint_id": "BLKpoint_35",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.399",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0021697"
      },
      {
        "BLKpoint_id": "BLKpoint_37",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.4989",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0019557"
      },
      {
        "BLKpoint_id": "BLKpoint_38",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.5495",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0018796"
      },
      {
        "BLKpoint_id": "BLKpoint_39",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.6067",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0017439"
      },
      {
        "BLKpoint_id": "BLKpoint_41",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.6956",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0015722"
      },
      {
        "BLKpoint_id": "BLKpoint_44",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0.8475",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0013415"
      },
      {
        "BLKpoint_id": "BLKpoint_94",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "0",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.00089689"
      },
      {
        "BLKpoint_id": "BLKpoint_98",
        "temperature_k": "298.15",
        "mole_fraction_<ethanol>": "1",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0010914"
      }
    ],
    "inspection_id": "INSP_d0495ab20e5e",
    "lit_num_id": "GLOBlit_5201"
  },
  {
    "doi": "10.1016/j.jct.2018.02.022",
    "block_number": "PROPblock_21",
    "table_mode": "nearest",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<ethanol>",
      "pressure_kpa",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_19",
        "temperature_k": "293.15",
        "mole_fraction_<ethanol>": "0.75",
        "pressure_kpa": "92.3",
        "viscosity_pa_s": "0.0016797"
      }
    ],
    "inspection_id": "INSP_a80f5dc78817",
    "lit_num_id": "GLOBlit_5201"
  }
]
```
