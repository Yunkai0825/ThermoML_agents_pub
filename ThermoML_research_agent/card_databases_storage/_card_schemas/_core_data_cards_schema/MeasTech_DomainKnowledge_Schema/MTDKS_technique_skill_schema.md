# {{technique_name}}

> **Schema version:** 1.0.0
> **Card type:** MTDKS — Measurement Technique Skill
> **Scope:** One file per measurement technique. Shared structure across all techniques.
> **Card schema:** MTDKS_meas_ID_and_DK_schema.json (per-technique card, keyed by meas_ID)

---

## 1 — Structured Technique Block

```json
{
  "technique_metadata": {
    "name": "",
    "acronym": "",
    "aliases": [],
    "measurement_family": "",
    "modality": {
      "contact": "",
      "destructive": "",
      "in_situ": "",
      "imaging": ""
    }
  },

  "measurement_scope": {
    "direct_observables": [
      {
        "name": "",
        "description": "",
        "unit": ""
      }
    ],
    "derived_observables": [
      {
        "name": "",
        "derived_from": [],
        "description": "",
        "unit": ""
      }
    ],
    "target_properties": [
      {
        "name": "",
        "property_group": "",
        "unit": "",
        "description": ""
      }
    ],
    "phases_measured": [],
    "supported_sample_types": [],
    "unsupported_sample_types": [],
    "typical_output_formats": [],
    "units": {}
  },

  "experimental_parameters": {
    "constraints": [
      {
        "name": "",
        "category": "",
        "description": "",
        "unit": "",
        "allowed_range": "",
        "typical_values": [],
        "required": false
      }
    ],
    "variables": [
      {
        "name": "",
        "category": "",
        "description": "",
        "unit": "",
        "recommended_range": "",
        "comparison_role": ""
      }
    ]
  },

  "setup_and_requirements": {
    "instrument_components": [],
    "environmental_requirements": [],
    "sample_requirements": {
      "geometry": [],
      "size_limits": "",
      "thickness_limits": "",
      "surface_requirements": [],
      "mounting_requirements": [],
      "preparation_requirements": []
    },
    "calibration_requirements": [],
    "reference_materials": [],
    "consumables": [],
    "safety_notes": []
  },

  "performance": {
    "sensitivity": "",
    "detection_limit": "",
    "resolution": {
      "spatial": "",
      "temporal": "",
      "spectral": "",
      "energy": ""
    },
    "dynamic_range": "",
    "accuracy": "",
    "precision": "",
    "throughput": "",
    "measurement_speed": ""
  },

  "data_and_interpretation": {
    "raw_signal_type": "",
    "preprocessing_steps": [],
    "analysis_methods": [],
    "model_assumptions": [],
    "fit_parameters": [],
    "common_artifacts": [],
    "quality_control_checks": [],
    "failure_modes": []
  },

  "uncertainty": {
    "level": "",
    "random_sources": [],
    "systematic_sources": [],
    "operator_dependence": "",
    "model_dependence": "",
    "dominant_error_sources": [],
    "reported_as": []
  }
}
```

### Field reference — Structured block

| Section | Field | Type | Description |
|---|---|---|---|
| **technique_metadata** | `name` | string | Full canonical name of the technique |
| | `acronym` | string | Standard abbreviation (e.g. DSC, GC, NMR) |
| | `aliases` | string[] | Alternative names, historical names, vendor names |
| | `measurement_family` | string | Parent technique family (from MDKS ID_and_DK `technique_families`) |
| | `modality.contact` | "yes" / "no" / "both" | Whether the probe physically contacts the sample |
| | `modality.destructive` | "yes" / "no" / "partially" | Whether the sample is consumed or altered |
| | `modality.in_situ` | "yes" / "no" / "both" | Whether the measurement occurs in the process environment |
| | `modality.imaging` | "yes" / "no" / "both" | Whether the output is spatially resolved |
| **measurement_scope** | `direct_observables` | object[] | Quantities the instrument directly records (signal level) |
| | `derived_observables` | object[] | Quantities computed from direct observables via models or calibration |
| | `target_properties` | object[] | Thermodynamic / physical properties this technique is used to determine; maps to PCS `property_names` |
| | `phases_measured` | string[] | Applicable phase states (from PCS `phases`) |
| | `supported_sample_types` | string[] | Sample forms the technique can handle (pure liquid, binary mixture, powder, thin film, …) |
| | `unsupported_sample_types` | string[] | Sample forms that are incompatible or require modification |
| | `typical_output_formats` | string[] | Data products (thermogram, isotherm, spectrum, single value, …) |
| | `units` | object | Key quantity → SI unit mapping for this technique |
| **experimental_parameters** | `constraints` | object[] | Control parameters held fixed during a measurement run (T, P, composition, …) |
| | `constraints[].category` | string | "thermodynamic" / "mechanical" / "chemical" / "temporal" / "geometric" |
| | `constraints[].allowed_range` | string | Physical limits the instrument can sustain |
| | `constraints[].required` | boolean | Whether the constraint must be specified for valid data |
| | `variables` | object[] | Parameters systematically varied to produce comparison data (the x-axis) |
| | `variables[].comparison_role` | string | How the variable is used: "independent", "scanning", "stepped" |
| **setup_and_requirements** | `instrument_components` | string[] | Key hardware parts (cell, transducer, furnace, detector, …) |
| | `environmental_requirements` | string[] | Lab conditions needed (temperature stability, vibration isolation, inert atmosphere, …) |
| | `sample_requirements` | object | Geometry, size, surface, mounting, and preparation constraints |
| | `calibration_requirements` | string[] | Calibration protocols and frequency |
| | `reference_materials` | string[] | Standard reference substances or certified values used |
| | `consumables` | string[] | Items consumed per run (crucibles, columns, gases, …) |
| | `safety_notes` | string[] | Hazards and precautions |
| **performance** | `sensitivity` | string | Smallest detectable change in the target property |
| | `detection_limit` | string | Lowest absolute value reliably measurable |
| | `resolution.*` | string | Spatial, temporal, spectral, or energy resolution |
| | `dynamic_range` | string | Ratio of largest to smallest measurable signal |
| | `accuracy` | string | Closeness to true value (after calibration) |
| | `precision` | string | Repeatability / reproducibility |
| | `throughput` | string | Samples per unit time |
| | `measurement_speed` | string | Time per single measurement or scan |
| **data_and_interpretation** | `raw_signal_type` | string | Physical nature of the raw signal (voltage, frequency, mass loss, heat flow, …) |
| | `preprocessing_steps` | string[] | Baseline correction, smoothing, blank subtraction, … |
| | `analysis_methods` | string[] | Curve fitting, peak integration, extrapolation, equation of state, … |
| | `model_assumptions` | string[] | Physical models or approximations applied during analysis |
| | `fit_parameters` | string[] | Parameters extracted from fitting routines |
| | `common_artifacts` | string[] | Known artifacts that can contaminate results |
| | `quality_control_checks` | string[] | Reproducibility tests, standard checks, internal consistency tests |
| | `failure_modes` | string[] | Conditions under which the technique produces unreliable or meaningless results |
| **uncertainty** | `level` | string | Typical overall uncertainty magnitude (e.g. "0.1–0.5 %", "± 0.02 K") |
| | `random_sources` | string[] | Noise, sampling variability, environmental fluctuations |
| | `systematic_sources` | string[] | Calibration bias, sample impurity, model error |
| | `operator_dependence` | string | "low" / "moderate" / "high" — degree to which results depend on operator skill |
| | `model_dependence` | string | "low" / "moderate" / "high" — degree to which results depend on chosen model |
| | `dominant_error_sources` | string[] | The 1–3 largest contributors to total uncertainty |
| | `reported_as` | string[] | How uncertainty is expressed: "combined standard uncertainty", "expanded (k=2)", "confidence interval", … |

---

## 2 — Technique Description Block

### Technique overview

{{One-paragraph summary of what the technique measures, why it is used, and where it sits among related techniques.}}

### How the technique operates

{{Describe the measurement workflow from sample loading through excitation/probing, signal generation, signal collection, and readout. Include timing and sequencing if relevant.}}

### Core theory

{{State the physical, chemical, optical, electrical, mechanical, or statistical principle behind the measurement. Reference governing equations or laws by name.}}

### Setup

{{Describe the instrument configuration, key components, geometry, operating environment, and calibration references. Mention typical commercial implementations if widely known.}}

### Suitable for

{{Describe the types of materials, samples, scientific questions, property ranges, and scales for which this technique is well suited. Note where it is the gold standard.}}

### Core limitations

{{State the main technical, physical, practical, and interpretive limits of the technique. Include temperature/pressure/composition bounds, sample restrictions, and inherent assumptions.}}

### Sample preparation

{{Describe cleaning, degassing, drying, mounting, shaping, conditioning, storage, and handling requirements. Note preparation steps that critically affect measurement quality.}}

### Calibration and references

{{Describe the calibration protocol: what reference materials or standards are used, how often calibration must be performed, and what systematic errors calibration corrects.}}

### Data interpretation

{{Explain how raw signals are converted into meaningful quantities, what models or equations are applied, what assumptions are used, and how results should be validated or compared against literature.}}

### Common pitfalls

{{List frequent mistakes in setup, acquisition, sample handling, preprocessing, fitting, interpretation, and reporting. Distinguish operator errors from instrument limitations.}}

### Artifacts and failure modes

{{Describe major artifact sources (thermal lag, adsorption, convection, baseline drift, …), conditions that trigger failure modes, and how to detect or mitigate each.}}

### Reporting checklist

{{List the minimum parameters, sample details, instrument settings, preprocessing steps, model choices, and uncertainty information that must always be reported for reproducibility. This section addresses the reproducibility gap common across techniques.}}

---

## Appendix — Schema usage notes

- **One file per technique.** Each measurement technique recognized in the ThermoML database gets its own markdown file following this schema.
- **Naming convention:** `MTDKS_skill_{{ACRONYM}}_{{short_name}}.md` (e.g. `MTDKS_skill_DSC_differential_scanning_calorimetry.md`). Stored in `Meas_skills/`.
- **Companion JSON card:** Each skill markdown file has a corresponding JSON card in `Meas_ID_and_DK_cards/` following `MTDKS_meas_ID_and_DK_schema.json`. The JSON carries the structured block; the markdown carries both blocks.
- **JSON block is machine-readable.** Agents parse the fenced JSON to match user queries to applicable techniques, filter by phase/property/sample type, and retrieve performance bounds.
- **Description block is agent-readable prose.** Agents use it for explanations, recommendations, and answering "how does this work?" questions.
- **Cross-references:** `target_properties[].property_group` maps to PCS `property_groups`; `phases_measured` maps to PCS `phases`; `measurement_family` maps to MTDKS_meas_summary.json `technique_families`.
- **Empty fields:** Leave fields as empty strings `""`, empty arrays `[]`, or `false` if not applicable. Do not omit fields.
