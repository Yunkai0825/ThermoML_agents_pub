# Delegated query run — result

**Question:** Find surface tension data for binary mixtures of methanol and acetonitrile near room temperature (around 293-303 K). I need DOIs, block numbers, composition ranges, and measured surface tension values.

**Iterations:** 2  |  **Elapsed:** 120.5s  |  **Tools:** 1  |  **Timed out:** False

---

## Answer

{
  "answer": "## Surface Tension of Methanol + Acetonitrile Binary Mixtures near Room Temperature\n\n### Source\n\n- **DOI:** 10.1021/je050519g\n- **Title:** *Density and Surface Tension of Binary Mixtures of Acetonitrile + 1-Alkanol at 293.15 K*\n- **Block:** PROPblock_13\n\n### Experimental Details\n\n| Detail | Value |\n|--------|-------|\n| **Compounds** | Acetonitrile (C₂H₃N) + Methanol (CH₄O) |\n| **Property** | Surface tension, liquid–gas (N/m) |\n| **Measurement method** | Pendant drop shape |\n| **Temperature** | 293.15 K (fixed) |\n| **Composition variable** | Mole fraction of acetonitrile in the liquid phase |\n| **Composition range** | 0.1001 – 0.8956 |\n\n### Measured Data (T = 293.15 K)\n\n| x(acetonitrile) | Surface tension γ (N/m) |\n|:---:|:---:|\n| 0.1001 | 0.0238 |\n| 0.2011 | 0.02473 |\n| 0.2996 | 0.02553 |\n| 0.4997 | 0.02685 |\n| 0.7012 | 0.02794 |\n| 0.8009 | 0.02842 |\n| 0.8956 | 0.02885 |\n\n### Composition Dependence and Chemical Insight\n\nThe surface tension increases **monotonically** with increasing acetonitrile mole fraction across the full measured composition range. At the methanol-rich end (x = 0.1001), γ = 0.0238 N/m, while at the acetonitrile-rich end (x = 0.8956), γ = 0.02885 N/m — a span of about 5 mN/m. This is consistent with the known pure-component surface tensions: methanol (~22.1 mN/m at 293 K) is lower than acetonitrile (~29.0 mN/m), so adding acetonitrile steadily raises the mixture's surface tension.\n\nThe smooth, monotonic trend with **no extrema** (no minimum or maximum) suggests relatively ideal mixing behavior at the liquid–gas interface for this system. Both components are small, polar molecules capable of hydrogen bonding (methanol as both donor and acceptor, acetonitrile primarily as an acceptor), and their similar molecular sizes and polarities lead to near-ideal surface behavior.\n\n### Data Availability Note\n\nOnly **one dataset** was found in the ThermoML database for this binary system, measured at a single temperature of **293.15 K**. No additional surface tension data at other temperatures within the 293–303 K window were available.",
  "core_claims": [
    "At 293.15 K, the surface tension of methanol + acetonitrile binary mixtures increases monotonically with increasing acetonitrile mole fraction, from 0.0238 N/m at x(acetonitrile) = 0.1001 to 0.02885 N/m at x(acetonitrile) = 0.8956, with no extrema observed.",
    "The monotonic increase is consistent with methanol having a lower pure-component surface tension (~22.1 mN/m) than acetonitrile (~29.0 mN/m) at 293 K, and the absence of extrema suggests relatively ideal mixing behavior at the liquid–gas interface.",
    "Only one dataset was found in the ThermoML database for this binary system, measured at a single temperature of 293.15 K using the pendant drop shape method; no additional surface tension data at other temperatures within the 293–303 K window were available."
  ],
  "confidence": "high",
  "sources": [
    {
      "doi": "10.1021/je050519g",
      "lit_num_id": "GLOBlit_8821",
      "block": "PROPblock_13",
      "BLKsubsys_id": null,
      "description": "This block provides the only available surface tension data for the methanol + acetonitrile binary system, with 7 datapoints at 293.15 K covering mole fractions 0.1001–0.8956 and surface tensions 0.0238–0.02885 N/m measured by pendant drop shape. It directly and fully supports the answer."
    }
  ],
  "follow_up_suggestions": [
    "Search for surface tension data of methanol + acetonitrile at other temperatures (e.g., 298.15 K or 303.15 K) using alternative DOIs or datasets in ThermoML.",
    "Compare the measured surface tension values with predictions from thermodynamic models such as the Parachor method or the UNIFAC-based surface tension correlation.",
    "Look for excess surface tension or surface tension deviation data for this binary system to quantify departures from ideal mixing at the liquid–gas interface."
  ],
  "id_catalog_snapshot": [
    {
      "type": "comp",
      "global_id": "GLOBcomp_15",
      "registry_id": "acetonitrile",
      "name": "acetonitrile"
    },
    {
      "type": "comp",
      "global_id": "GLOBcomp_4",
      "registry_id": "methanol",
      "name": "methanol"
    },
    {
      "type": "prop",
      "global_id": "GLOBprop_13",
      "registry_id": "surface_tension_liquidgas_n_m",
      "name": "Surface tension liquid-gas, N/m"
    },
    {
      "type": "meas",
      "global_id": "GLOBmeas_22",
      "registry_id": "pendant_drop_shape",
      "name": "Pendant drop shape"
    },
    {
      "type": "lit",
      "global_id": "GLOBlit_8821",
      "registry_id": "2006-tah-mod-0",
      "name": "10.1021/je050519g"
    }
  ]
}

---

## Data Inspections (deterministic evidence ledger)

Hardcoded envelope merge — not agent-authored. 1 entr(ies); verbatim rows below.

- INSP_ace1f89aece6 — GLOBlit_8821::PROPblock_13 · complete · 7 rows

```json
[
  {
    "doi": "10.1021/je050519g",
    "block_number": "PROPblock_13",
    "table_mode": "complete",
    "columns": [
      "BLKpoint_id",
      "mole_fraction_<acetonitrile>",
      "temperature_k",
      "surface_tension_liquidgas_n_m"
    ],
    "rows_shown": [
      {
        "BLKpoint_id": "BLKpoint_1",
        "mole_fraction_<acetonitrile>": "0.1001",
        "temperature_k": "293.15",
        "surface_tension_liquidgas_n_m": "0.0238"
      },
      {
        "BLKpoint_id": "BLKpoint_2",
        "mole_fraction_<acetonitrile>": "0.2011",
        "temperature_k": "293.15",
        "surface_tension_liquidgas_n_m": "0.02473"
      },
      {
        "BLKpoint_id": "BLKpoint_3",
        "mole_fraction_<acetonitrile>": "0.2996",
        "temperature_k": "293.15",
        "surface_tension_liquidgas_n_m": "0.02553"
      },
      {
        "BLKpoint_id": "BLKpoint_4",
        "mole_fraction_<acetonitrile>": "0.4997",
        "temperature_k": "293.15",
        "surface_tension_liquidgas_n_m": "0.02685"
      },
      {
        "BLKpoint_id": "BLKpoint_5",
        "mole_fraction_<acetonitrile>": "0.7012",
        "temperature_k": "293.15",
        "surface_tension_liquidgas_n_m": "0.02794"
      },
      {
        "BLKpoint_id": "BLKpoint_6",
        "mole_fraction_<acetonitrile>": "0.8009",
        "temperature_k": "293.15",
        "surface_tension_liquidgas_n_m": "0.02842"
      },
      {
        "BLKpoint_id": "BLKpoint_7",
        "mole_fraction_<acetonitrile>": "0.8956",
        "temperature_k": "293.15",
        "surface_tension_liquidgas_n_m": "0.02885"
      }
    ],
    "inspection_id": "INSP_ace1f89aece6",
    "lit_num_id": "GLOBlit_8821"
  }
]
```
