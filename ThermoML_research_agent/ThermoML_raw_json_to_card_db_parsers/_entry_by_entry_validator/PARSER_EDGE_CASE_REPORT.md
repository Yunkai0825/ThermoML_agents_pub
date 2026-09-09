# ThermoML Prototype Parser — Edge Case Report

## Summary

**Parser**: `thermoml_card_parser.py`
**Historical prototype result**: 8/8 edge-case DOIs parsed successfully, 0 validation errors
**Historical outputs**: 4 card types × 8 DOIs = 32 JSON files. The current validator delegates to the production card orchestrator and writes under workspace-root `_output/Query/Diagnostics/card_orchestrator/` by default. This prototype report is not a fresh validation of the current typed-ID schema.

---

## Edge Cases Tested

### 1. Simple Unary — `10.1007/s10765-005-5568-4`
- 4 pure compounds, each in its own block, 1 property (thermal conductivity), 5 data points
- Variable: Temperature sweep. Constraint: fixed Pressure at 101.325 kPa
- **Parser output**: Clean. Block-level uncertainty propagated. T/P ranges correctly extracted.

### 2. ReactionData — `10.1016/j.fluid.2016.01.035`
- 6 PureOrMixture + 8 ReactionData blocks (combustion, formation from elements)
- Reaction blocks have **inline T/P** on Property (not as Variables/Constraints)
- Participants carry `stoichiometric_coef` and `phase` (Crystal, Gas, Liquid)
- **Parser output**: `reaction` field populated with participants, coefficients, reaction type. T/P extracted from `nTemperature-K` and `nPressure-kPa`. Empty `variable_values {}` handled correctly.

### 3. Multi-Property Block (6 props) — `10.1016/j.fluid.2005.07.015`
- Block 1: 6 "Mole fraction" properties, each for a different (component, phase) pair
- Phases: Liquid mixture 1, Liquid mixture 2, Gas (VLLE data)
- Each `NumValues` entry has all 6 property values
- **Parser output**: All 6 properties correctly listed with distinct `component_org_num` and `property_phase`. Data points carry all 6 prop values per row.

### 4. Binary VLE — `10.1007/s10765-006-0018-5`
- 8 blocks for 2 compounds (1-butanol + p-xylene)
- Includes azeotropic composition/temperature and boiling T blocks
- Variables link to specific components via `RegNum.nOrgNum`
- Phase information on variables (`VarPhaseID`) and constraints (`ConstraintPhaseID`)
- **Parser output**: Phase and component references correctly extracted for all variables and properties.

### 5. Complex Constraints — `10.1016/j.fluid.2016.03.016`
- Up to 4 constraints: `eSolventComposition`, `eComponentComposition` (initial/final molality), `ePressure`
- Property-level `Solvent` object with `RegNum` reference to solvent compound
- `eSolventComposition` constraint carries `component_org_num` (which compound the solvent refers to)
- **Parser output**: All constraint types, values, and component references captured. Solvent field on property extracted.

### 6. Large Block — `10.1021/je060271a`
- 5 blocks, largest has 10,245 data points (32,441 total)
- Mass density measured by vibrating tube
- **Parser output**: Data summary stats computed for full dataset. Data points capped at 20 in prototype mode. No performance issues.

### 7. Many Compounds — `10.1021/je3010535`
- 94 compounds across 93 blocks (Henry's Law constants)
- **Parser output**: All 94 compounds in RMS compound_list, 93 blocks in PCS. CCS has 94 compound entries with sample info.

### 8. Mixed Block Types — `10.1016/j.jct.2003.08.017`
- 4 PureOrMixture + 1 ReactionData block in same paper
- ReactionData is combustion calorimetry (4 participants, quaternary system)
- PureOrMixture includes heat capacity, fusion enthalpy, triple point
- **Parser output**: Both block types correctly distinguished. Reaction type and participants extracted. `block_type` field distinguishes them in the index.

---

## Key Structural Observations for Card Schemas

### A. PropertyGroup is a Choice Element
The Property's `PropertyGroup` dict has exactly **one meaningful key** (the group name like `TransportProp`, `CompositionAtPhaseEquilibrium`, `ReactionStateChangeProp`, etc.) plus an optional `tml_elements` ordering key. The parser iterates and skips `tml_elements`.

### B. ReactionData vs PureOrMixtureData
| Feature | PureOrMixtureData | ReactionData |
|---|---|---|
| Compounds key | `Component` | `Participant` |
| Block number key | `nPureOrMixtureDataNumber` | `nReactionDataNumber` |
| T/P location | Variables or Constraints | **Inline on Property** (`nTemperature-K`, `nPressure-kPa`) |
| Stoichiometry | n/a | `nStoichiometricCoef` on each Participant |
| Reaction type | n/a | `eReactionType` on block |
| VariableValue | Populated | Usually **empty** |

### C. Multi-Property Blocks
When a block has N properties, **every NumValues entry carries N PropertyValues** (one per `nPropNumber`). Properties are distinguished by their component reference and phase assignment, not by name (all may be "Mole fraction").

### D. Phase Hierarchies
- `PhaseID` on block: Overall phases present (e.g., Gas + Liquid)
- `PropPhaseID` on property: Which phase this property measures
- `VarPhaseID` on variable: Which phase this variable's condition applies to
- `ConstraintPhaseID` on constraint: Which phase is constrained

### E. Component References
`RegNum.nOrgNum` appears in multiple locations:
- `Component` / `Participant` → which compound
- `Property-MethodID.RegNum` → which component this property is about
- `VariableID.RegNum` → which component this variable refers to
- `ConstraintID.RegNum` → which component this constraint applies to
- `Solvent.RegNum` → which compound is the solvent

### F. Uncertainty Structure
Two levels:
- **Block-level**: `CombinedUncertainty` on Property → evaluation method, confidence level, evaluator
- **Point-level**: `CombinedUncertainty` on PropertyValue → `nCombExpandUncertValue` (expanded uncertainty)

### G. Unused XSD Elements (confirmed empty in corpus)
- `AuxiliarySubstance` — defined in XSD but **never** appears
- `Equation` / `EqProperty` — defined but **no** structured equation data
- `PropRepeat` — repeat measurements, not encountered

---

## Card Mapping Summary

| ThermoML Source | → Card | Key Fields |
|---|---|---|
| `Citation` | **RMS** | doi, lit_id, authors, title, year, journal |
| `Compound[].Sample[].purity[]` | **CCS** | comp_id, samples, purity_steps (mol/mass/vol fractions, analysis/purification methods) |
| Property `eMethodName` / `sMethodName` | **MTDKS** | method_type, method_name, property_group, block_numbers |
| Block + Property + NumValues | **PCS** | block_number, compounds, properties, variables, constraints, data_points, reaction |

---

## Next Steps

1. **Schema Tightening**: The PCS property entry has `temperature_K` / `pressure_kPa` fields only used by ReactionData — consider making this a sub-object `inline_conditions` or keeping it flat with null for PureOrMixture.
2. **Phase ID Normalization**: Phase strings like "Liquid mixture 1" could be normalized to structured `{phase_type: "Liquid", qualifier: "mixture 1"}`.
3. **Constraint Component Resolution**: Some constraints (e.g., initial/final molality) don't carry `RegNum` — the component is implied by context. May need a resolver.
4. **Custom Method Parsing**: Custom methods like "CHROM:UFactor:4" and "BOMBST:Method:BOMBST" encode technique + uncertainty info in a colon-separated format. Consider parsing these into structured fields.
5. **SQL Pipeline**: Once card structure is finalized, add `INSERT` statements for each card type table.
