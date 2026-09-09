# Delegated query run — result

**Question:** Find viscosity data for the binary mixture of acetonitrile + N,N-dimethylformamide (DMF) at or near 30°C (303.15 K). I need dynamic viscosity as a function of composition (mole fraction). Return DOIs, block numbers, compound names, and any available data points.

**Iterations:** 2  |  **Elapsed:** 173.1s  |  **Tools:** 1  |  **Timed out:** False

---

## Answer

{
  "answer": "## Dynamic Viscosity of Acetonitrile + N,N-Dimethylformamide (DMF) at 303.15 K\n\nTwo independent ThermoML data sources provide dynamic viscosity (η) measurements for the binary system **acetonitrile (CH₃CN)** + **N,N-dimethylformamide (DMF, C₃H₇NO)** at 303.15 K across the full composition range.\n\n---\n\n### Source 1 — Mass-fraction basis\n\n**DOI:** 10.1016/j.jct.2014.02.019 · **Block:** PROPblock_6  \n**Compounds:** Acetonitrile (GLOBcomp_15) + Dimethylformamide (GLOBcomp_18)  \n**Method:** Capillary tube (Ostwald/Ubbelohde) viscometry  \n**Conditions:** T = 303.15 K, P = 101.0 kPa  \n**Full block range:** 298.15–313.15 K, 20 total data points\n\n| w(DMF) | η (Pa·s) |\n|--------|----------|\n| 0      | 0.0003269 |\n| 0.25   | 0.0003598 |\n| 0.50   | 0.00046   |\n| 0.75   | 0.0006145 |\n| 1.00   | 0.000755  |\n\n---\n\n### Source 2 — Mole-fraction basis (recommended for your needs)\n\n**DOI:** 10.1021/acs.jced.8b00176 · **Block:** PROPblock_18  \n**Compounds:** Acetonitrile (GLOBcomp_15) + Dimethylformamide (GLOBcomp_18)  \n**Method:** Falling/rolling sphere viscometry  \n**Conditions:** T = 303.15 K, P = 100.0 kPa  \n**Full block range:** 298.15–323.15 K, 66 total data points\n\n| x(DMF) | η (Pa·s) |\n|--------|----------|\n| 0      | 0.00032  |\n| 0.0989 | 0.00039  |\n| 0.1916 | 0.00042  |\n| 0.2925 | 0.00046  |\n| 0.3932 | 0.00051  |\n| 0.5029 | 0.00057  |\n| 0.6002 | 0.00061  |\n| 0.6931 | 0.00065  |\n| 0.7926 | 0.00070  |\n| 0.8996 | 0.00075  |\n| 1.0000 | 0.00077  |\n\n---\n\n### Chemical Insight\n\nBoth datasets show a **monotonic, slightly concave increase** in dynamic viscosity with increasing DMF content at 303.15 K. Pure DMF is roughly 2.4× more viscous than pure acetonitrile under these conditions (≈ 0.00077 vs. 0.00032 Pa·s). This trend reflects the stronger intermolecular interactions in DMF — it is a larger molecule with a higher dipole moment (~3.86 D vs. ~3.92 D for acetonitrile, but with a much larger molecular volume and stronger dipole–dipole/dispersion forces) and a pronounced hydrogen-bond-accepting capability via its carbonyl oxygen.\n\nThe two independent sources agree well at the pure-component endpoints (within ~2–3%), with minor differences attributable to different measurement techniques (capillary vs. falling-sphere viscometry) and a slight pressure difference (101.0 vs. 100.0 kPa). Source 2 (DOI 10.1021/acs.jced.8b00176) is particularly useful for your needs as it directly reports viscosity on a **mole-fraction basis** with 11 composition points spanning the full range, and covers a broader temperature window (298.15–323.15 K).",
  "core_claims": [
    "Two independent ThermoML sources provide dynamic viscosity measurements for the acetonitrile + N,N-dimethylformamide binary system at 303.15 K across the full composition range.",
    "Both datasets show a monotonic, slightly concave increase in dynamic viscosity with increasing DMF content at 303.15 K, from approximately 0.00032 Pa·s (pure acetonitrile) to approximately 0.00077 Pa·s (pure DMF).",
    "Source 1 (DOI 10.1016/j.jct.2014.02.019) reports viscosity on a mass-fraction basis at 303.15 K and 101.0 kPa using capillary tube viscometry, with 5 composition points.",
    "Source 2 (DOI 10.1021/acs.jced.8b00176) reports viscosity on a mole-fraction basis at 303.15 K and 100.0 kPa using falling/rolling sphere viscometry, with 11 composition points spanning the full range and a broader temperature window of 298.15–323.15 K.",
    "The two independent sources agree at the pure-component endpoints within ~2–3%, with minor differences attributed to different measurement techniques and a slight pressure difference (101.0 vs. 100.0 kPa).",
    "The higher viscosity of pure DMF relative to pure acetonitrile is attributed to stronger intermolecular interactions in DMF, including its larger molecular volume, stronger dipole–dipole/dispersion forces, and hydrogen-bond-accepting capability via its carbonyl oxygen."
  ],
  "confidence": "high",
  "sources": [
    {
      "doi": "10.1016/j.jct.2014.02.019",
      "lit_num_id": "GLOBlit_4124",
      "block": "PROPblock_6",
      "BLKsubsys_id": null,
      "description": "Provides dynamic viscosity of the acetonitrile + DMF binary system on a mass-fraction basis at 303.15 K (within its 298.15–313.15 K range), measured by capillary tube viscometry at 101.0 kPa. The answer's Source 1 table values fall within the card's viscosity range of 0.000293–0.000799 Pa·s."
    },
    {
      "doi": "10.1021/acs.jced.8b00176",
      "lit_num_id": "GLOBlit_7481",
      "block": "PROPblock_18",
      "BLKsubsys_id": null,
      "description": "Provides dynamic viscosity of the acetonitrile + DMF binary system on a mole-fraction basis at 303.15 K (within its 298.15–323.15 K range), measured by falling-sphere viscometry at 100.0 kPa with 66 data points spanning the full composition range. The answer's Source 2 table values fall within the card's viscosity range of 0.00028–0.00081 Pa·s."
    }
  ],
  "follow_up_suggestions": [
    "Compare excess viscosity (Δη) or viscosity deviation from ideal mixing for this system at 303.15 K using the mole-fraction data from Source 2.",
    "Examine temperature dependence of viscosity across 298.15–323.15 K using the broader dataset in DOI 10.1021/acs.jced.8b00176.",
    "Search for density data for the same binary system at 303.15 K to compute kinematic viscosity from the dynamic viscosity values."
  ],
  "id_catalog_snapshot": []
}

---

## Data Inspections (deterministic evidence ledger)

Hardcoded envelope merge — not agent-authored. 2 entr(ies); verbatim rows below.

- INSP_5e97b19eeb51 — GLOBlit_4124::PROPblock_6 · complete · 5 rows
- INSP_0a0742d5bd6a — GLOBlit_7481::PROPblock_18 · complete · 11 rows

```json
[
  {
    "doi": "10.1016/j.jct.2014.02.019",
    "block_number": "PROPblock_6",
    "table_mode": "complete",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mass_fraction_<dimethylformamide>",
      "pressure_kpa",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_2",
        "temperature_k": "303.15",
        "mass_fraction_<dimethylformamide>": "0",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0003269"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "temperature_k": "303.15",
        "mass_fraction_<dimethylformamide>": "0.25",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0003598"
      },
      {
        "BLKpoint_id": "BLKpoint_10",
        "temperature_k": "303.15",
        "mass_fraction_<dimethylformamide>": "0.5",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.00046"
      },
      {
        "BLKpoint_id": "BLKpoint_14",
        "temperature_k": "303.15",
        "mass_fraction_<dimethylformamide>": "0.75",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.0006145"
      },
      {
        "BLKpoint_id": "BLKpoint_18",
        "temperature_k": "303.15",
        "mass_fraction_<dimethylformamide>": "1",
        "pressure_kpa": "101.0",
        "viscosity_pa_s": "0.000755"
      }
    ],
    "inspection_id": "INSP_5e97b19eeb51",
    "lit_num_id": "GLOBlit_4124"
  },
  {
    "doi": "10.1021/acs.jced.8b00176",
    "block_number": "PROPblock_18",
    "table_mode": "complete",
    "columns": [
      "BLKpoint_id",
      "temperature_k",
      "mole_fraction_<dimethylformamide>",
      "pressure_kpa",
      "viscosity_pa_s"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_12",
        "temperature_k": "303.15",
        "mole_fraction_<dimethylformamide>": "0",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00032"
      },
      {
        "BLKpoint_id": "BLKpoint_13",
        "temperature_k": "303.15",
        "mole_fraction_<dimethylformamide>": "0.0989",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00039"
      },
      {
        "BLKpoint_id": "BLKpoint_14",
        "temperature_k": "303.15",
        "mole_fraction_<dimethylformamide>": "0.1916",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00042"
      },
      {
        "BLKpoint_id": "BLKpoint_15",
        "temperature_k": "303.15",
        "mole_fraction_<dimethylformamide>": "0.2925",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00046"
      },
      {
        "BLKpoint_id": "BLKpoint_16",
        "temperature_k": "303.15",
        "mole_fraction_<dimethylformamide>": "0.3932",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00051"
      },
      {
        "BLKpoint_id": "BLKpoint_17",
        "temperature_k": "303.15",
        "mole_fraction_<dimethylformamide>": "0.5029",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00057"
      },
      {
        "BLKpoint_id": "BLKpoint_18",
        "temperature_k": "303.15",
        "mole_fraction_<dimethylformamide>": "0.6002",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00061"
      },
      {
        "BLKpoint_id": "BLKpoint_19",
        "temperature_k": "303.15",
        "mole_fraction_<dimethylformamide>": "0.6931",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00065"
      },
      {
        "BLKpoint_id": "BLKpoint_20",
        "temperature_k": "303.15",
        "mole_fraction_<dimethylformamide>": "0.7926",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.0007"
      },
      {
        "BLKpoint_id": "BLKpoint_21",
        "temperature_k": "303.15",
        "mole_fraction_<dimethylformamide>": "0.8996",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00075"
      },
      {
        "BLKpoint_id": "BLKpoint_22",
        "temperature_k": "303.15",
        "mole_fraction_<dimethylformamide>": "1",
        "pressure_kpa": "100.0",
        "viscosity_pa_s": "0.00077"
      }
    ],
    "inspection_id": "INSP_0a0742d5bd6a",
    "lit_num_id": "GLOBlit_7481"
  }
]
```
