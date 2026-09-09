
# Overall card architecture

## Top level JSON card
Raw NIST JSON file
├─ 1.Version
├─ 2.Citation
├─ 3.Compound [0..*]
├─ 4.PureOrMixtureData [0..*]
├─ 5.ReactionData [0..*]
├─ 6.THERMOML_MD5_CHECKSUM   ← JSON-only archive field
└─ 7.tml_elements            ← JSON-only ordering helper

### 1.Version
Version
├─ nVersionMajor
└─ nVersionMinor

### 2.Citation/reference (stable, RMS cards)
Citation
├─ TRCRefID
│  ├─ yrYrPub
│  ├─ sAuthor1
│  ├─ sAuthor2
│  └─ nAuthorn
├─ eType
├─ eSourceType
├─ sAuthor [repeated]
├─ sPubName
├─ yrPubYr
├─ dateCit
├─ sTitle
├─ sAbstract
├─ sDOI
├─ sIDNum
├─ sPage
├─ sVol
└─ sKeyword [repeated]

### 3.Compound (stable, CCS cards, one for DK and ID, another for "Sample")
Compound
├─ RegNum
│  └─ nOrgNum
├─ sCommonName
├─ sFormulaMolec
├─ sStandardInChI
├─ sStandardInChIKey
└─ Sample [0..*]
   ├─ nSampleNm
   ├─ eSource
   ├─ eStatus
   └─ purity [0..*]
      ├─ nStep
      ├─ eAnalMeth
      ├─ sAnalMeth
      ├─ ePurifMethod
      ├─ sPurifMethod
      ├─ nPurityMol
      ├─ nPurityMolDigits
      ├─ nPurityMass
      ├─ nPurityMassDigits
      ├─ nPurityVol
      ├─ nPurityVolDigits
      ├─ nHalideMassPerCent
      ├─ nHalideMassPerCentDigits
      ├─ nHalideMolPerCent
      ├─ nHalideMolPerCentDigits
      ├─ nWaterMassPerCent
      ├─ nWaterMassPerCentDigits
      ├─ nUnknownPerCent
      └─ nUnknownPerCentDigits

### 4.PureOrMixtureData (main data)
PureOrMixtureData
├─ nPureOrMixtureDataNumber
├─ Component [1..*]
│  ├─ RegNum
│  │  └─ nOrgNum
│  └─ nSampleNm
├─ eExpPurpose
├─ sCompiler
├─ sContributor
├─ dateDateAdded
├─ Property [1..*]
│  ├─ nPropNumber
│  ├─ Property-MethodID
│  │  ├─ PropertyGroup
│  │  │  └─ <GroupName>
│  │  │     ├─ ePropName
│  │  │     ├─ eMethodName
│  │  │     └─ sMethodName
│  │  └─ RegNum
│  │     └─ nOrgNum
│  ├─ ePresentation
│  ├─ eStandardState
│  ├─ eRefStateType
│  ├─ nRefTemp
│  ├─ nRefTempDigits
│  ├─ nRefPressure
│  ├─ nRefPressureDigits
│  ├─ PropPhaseID
│  │  ├─ ePropPhase
│  │  └─ RegNum
│  │     └─ nOrgNum
│  ├─ RefPhaseID
│  │  ├─ eRefPhase
│  │  └─ RegNum
│  │     └─ nOrgNum
│  ├─ Solvent
│  │  └─ RegNum
│  │     └─ nOrgNum
│  └─ CombinedUncertainty [0..*]
│     ├─ nCombUncertAssessNum
│     ├─ eCombUncertEvalMethod
│     ├─ nCombUncertLevOfConfid
│     └─ sCombUncertEvaluator
├─ PhaseID [0..*]
│  ├─ ePhase
│  └─ RegNum
│     └─ nOrgNum
├─ Constraint [0..*]
│  ├─ nConstraintNumber
│  ├─ ConstraintID
│  │  ├─ ConstraintType
│  │  │  └─ eTemperature / ePressure / eComponentComposition / eSolventComposition / eMiscellaneous
│  │  └─ RegNum
│  │     └─ nOrgNum
│  ├─ nConstraintValue
│  ├─ nConstrDigits
│  └─ ConstraintPhaseID
│     ├─ eConstraintPhase
│     └─ RegNum
│        └─ nOrgNum
├─ Variable [0..*]
│  ├─ nVarNumber
│  ├─ VariableID
│  │  ├─ VariableType
│  │  │  └─ eTemperature / ePressure / eComponentComposition / eSolventComposition / eMiscellaneous
│  │  └─ RegNum
│  │     └─ nOrgNum
│  └─ VarPhaseID
│     ├─ eVarPhase
│     └─ RegNum
│        └─ nOrgNum
└─ NumValues [0..*]
   ├─ VariableValue [1..*]
   │  ├─ nVarNumber
   │  ├─ nVarValue
   │  └─ nVarDigits
   └─ PropertyValue [1..*]
      ├─ nPropNumber
      ├─ nPropValue
      ├─ nPropDigits
      └─ CombinedUncertainty
         ├─ nCombUncertAssessNum
         └─ nCombExpandUncertValue

#### Data point report style (PureOrMixtureData)

- **Property** = what is measured; can be component-specific (RegNum.nOrgNum) and phase-specific (PropPhaseID)
- **Variable** = independent condition swept across rows; can also be phase- and component-specific
- **Constraint** = independent condition held constant for every row in the block
- **NumValues** = one row per data point (variable values + property values + per-point uncertainty)
- A block can carry **multiple properties** — typically the same property name measured for different components or in different phases (e.g. mole fractions on each side of an LLE tie-line)
- Each block is self-contained: its own components, properties, variables, constraints, phases, and data

Real example — DOI 10.1016/j.fluid.2010.05.013, block #13
(ternary liquid-liquid equilibrium: CO₂ + lactic acid + ionic liquid):

```
DataReport  (4 compounds in paper; block #13 uses 3)
│
├─ Compound: nOrgNum=1, sCommonName="carbon dioxide",     sFormulaMolec="CO2"
│   └─ Sample: nSampleNm=1, eSource="Commercial source"
├─ Compound: nOrgNum=2, sCommonName="2-hydroxypropanoic acid", sFormulaMolec="C3H6O3"
│   └─ Sample: nSampleNm=1, eSource="Commercial source"
├─ Compound: nOrgNum=4, sCommonName="[EMIM][NTf2]",       sFormulaMolec="C8H11F6N3O4S2"
│   └─ Sample: nSampleNm=1, eSource="Commercial source"
│
└─ PureOrMixtureData  nPureOrMixtureDataNumber=13
   │
   ├─ eExpPurpose = "Principal objective of the work"
   ├─ sCompiler = "KNA"
   ├─ dateDateAdded = "10/2/2010"
   │
   ├─ Component: RegNum.nOrgNum=2  nSampleNm=1   ← lactic acid
   ├─ Component: RegNum.nOrgNum=1  nSampleNm=1   ← CO₂
   ├─ Component: RegNum.nOrgNum=4  nSampleNm=1   ← [EMIM][NTf2]
   │
   ├─ PhaseID: ePhase="Liquid mixture 1"          ← IL-rich phase
   ├─ PhaseID: ePhase="Liquid mixture 2"          ← CO₂-rich phase
   │
   │  ┌──────────────────────────────────────────────────────────────────┐
   │  │  3 properties — same ePropName "Mole fraction" but each        │
   │  │  targets a different (component, phase) pair.  The block-level │
   │  │  CombinedUncertainty (assess #1) is referenced by per-point    │
   │  │  uncertainty in NumValues.                                      │
   │  └──────────────────────────────────────────────────────────────────┘
   │
   ├─ Property #1                                ← x(lactic acid) in CO₂-rich phase
   │   ├─ nPropNumber = 1
   │   ├─ PropertyGroup → CompositionAtPhaseEquilibrium
   │   │   ├─ ePropName  = "Mole fraction"
   │   │   └─ eMethodName = "Chromatography"
   │   ├─ Property-MethodID.RegNum.nOrgNum = 2   ← property is for compound 2
   │   ├─ ePresentation = "Direct value, X"
   │   ├─ PropPhaseID.ePropPhase = "Liquid mixture 2"
   │   └─ CombinedUncertainty
   │       ├─ nCombUncertAssessNum = 1
   │       ├─ eCombUncertEvalMethod = "Propagation of evaluated standard uncertainties"
   │       └─ nCombUncertLevOfConfid = 95
   │
   ├─ Property #2                                ← x(lactic acid) in IL-rich phase
   │   ├─ nPropNumber = 2
   │   ├─ PropertyGroup → CompositionAtPhaseEquilibrium
   │   │   ├─ ePropName  = "Mole fraction"
   │   │   └─ eMethodName = "Chromatography"
   │   ├─ Property-MethodID.RegNum.nOrgNum = 2   ← same compound, different phase
   │   ├─ ePresentation = "Direct value, X"
   │   ├─ PropPhaseID.ePropPhase = "Liquid mixture 1"
   │   └─ CombinedUncertainty
   │       ├─ nCombUncertAssessNum = 1
   │       ├─ eCombUncertEvalMethod = "Propagation of evaluated standard uncertainties"
   │       └─ nCombUncertLevOfConfid = 95
   │
   ├─ Property #3                                ← x([EMIM][NTf2]) in IL-rich phase
   │   ├─ nPropNumber = 3
   │   ├─ PropertyGroup → CompositionAtPhaseEquilibrium
   │   │   ├─ ePropName  = "Mole fraction"
   │   │   └─ eMethodName = "Chromatography"
   │   ├─ Property-MethodID.RegNum.nOrgNum = 4   ← different compound
   │   ├─ ePresentation = "Direct value, X"
   │   ├─ PropPhaseID.ePropPhase = "Liquid mixture 1"
   │   └─ CombinedUncertainty
   │       ├─ nCombUncertAssessNum = 1
   │       ├─ eCombUncertEvalMethod = "Propagation of evaluated standard uncertainties"
   │       └─ nCombUncertLevOfConfid = 95
   │
   ├─ Constraint #1                              ← temperature fixed for entire block
   │   ├─ nConstraintNumber = 1
   │   ├─ ConstraintType → eTemperature = "Temperature, K"
   │   ├─ nConstraintValue = 313.15
   │   └─ nConstrDigits = 5
   │
   ├─ Variable #1                                ← pressure (phase-specific)
   │   ├─ nVarNumber = 1
   │   ├─ VariableType → ePressure = "Pressure, kPa"
   │   └─ VarPhaseID.eVarPhase = "Liquid mixture 1"
   │
   ├─ Variable #2                                ← x([EMIM][NTf2]) in CO₂-rich phase
   │   ├─ nVarNumber = 2
   │   ├─ VariableType → eComponentComposition = "Mole fraction"
   │   ├─ VariableID.RegNum.nOrgNum = 4          ← composition of compound 4
   │   └─ VarPhaseID.eVarPhase = "Liquid mixture 2"
   │
   │  ┌──────────────────────────────────────────────────────────────────────────────────┐
   │  │  Each NumValues row: 2 variable values + 3 property values (+ per-point uncert) │
   │  └──────────────────────────────────────────────────────────────────────────────────┘
   │
   ├─ NumValues  (row 1 of 4)
   │   ├─ VariableValue: nVarNumber=1 nVarValue=9000  nVarDigits=1     ← P = 9000 kPa
   │   ├─ VariableValue: nVarNumber=2 nVarValue=0.299 nVarDigits=3     ← x₄(L2)=0.299
   │   ├─ PropertyValue: nPropNumber=1 nPropValue=0.632 nPropDigits=3  ← x₂(L2)
   │   │   └─ CombinedUncertainty: nCombUncertAssessNum=1 nCombExpandUncertValue=0.005
   │   ├─ PropertyValue: nPropNumber=2 nPropValue=0.01  nPropDigits=2  ← x₂(L1)
   │   │   └─ CombinedUncertainty: nCombUncertAssessNum=1 nCombExpandUncertValue=0.004
   │   └─ PropertyValue: nPropNumber=3 nPropValue=0.898 nPropDigits=3  ← x₄(L1)
   │
   ├─ NumValues  (row 2 of 4)
   │   ├─ VariableValue: nVarNumber=1 nVarValue=9000  nVarDigits=1
   │   ├─ VariableValue: nVarNumber=2 nVarValue=0.225 nVarDigits=3
   │   ├─ PropertyValue: nPropNumber=1 nPropValue=0.624 nPropDigits=3
   │   │   └─ CombinedUncertainty: nCombUncertAssessNum=1 nCombExpandUncertValue=0.005
   │   ├─ PropertyValue: nPropNumber=2 nPropValue=0.019 nPropDigits=2
   │   │   └─ CombinedUncertainty: nCombUncertAssessNum=1 nCombExpandUncertValue=0.004
   │   └─ PropertyValue: nPropNumber=3 nPropValue=0.429 nPropDigits=3
   │
   ├─ NumValues  (row 3 of 4)
   │   ├─ VariableValue: nVarNumber=1 nVarValue=10000 nVarDigits=1
   │   ├─ VariableValue: nVarNumber=2 nVarValue=0.289 nVarDigits=3
   │   ├─ PropertyValue: nPropNumber=1 nPropValue=0.622 nPropDigits=3
   │   │   └─ CombinedUncertainty: nCombUncertAssessNum=1 nCombExpandUncertValue=0.005
   │   ├─ PropertyValue: nPropNumber=2 nPropValue=0.034 nPropDigits=2
   │   │   └─ CombinedUncertainty: nCombUncertAssessNum=1 nCombExpandUncertValue=0.004
   │   └─ PropertyValue: nPropNumber=3 nPropValue=0.41  nPropDigits=3
   │
   └─ NumValues  (row 4 of 4)
       ├─ VariableValue: nVarNumber=1 nVarValue=10000 nVarDigits=1
       ├─ VariableValue: nVarNumber=2 nVarValue=0.228 nVarDigits=3
       ├─ PropertyValue: nPropNumber=1 nPropValue=0.593 nPropDigits=3
       │   └─ CombinedUncertainty: nCombUncertAssessNum=1 nCombExpandUncertValue=0.005
       ├─ PropertyValue: nPropNumber=2 nPropValue=0.032 nPropDigits=2
       │   └─ CombinedUncertainty: nCombUncertAssessNum=1 nCombExpandUncertValue=0.004
       └─ PropertyValue: nPropNumber=3 nPropValue=0.41  nPropDigits=3
```

**Reading this block:** Ternary LLE tie-line data for CO₂ + lactic acid + [EMIM][NTf2]
at 313.15 K, pressure varied (9–10 MPa). Three mole-fraction properties capture the
compositions of two different compounds across two liquid phases — illustrating how
multi-property blocks use `Property-MethodID.RegNum.nOrgNum` and `PropPhaseID` to
disambiguate what would otherwise be identical "Mole fraction" entries. Per-point
expanded uncertainty (95 % confidence) is attached to Properties #1 and #2 via
`nCombUncertAssessNum=1`, referencing the block-level assessment definition.

### 5.ReactionData (main data)
ReactionData
├─ nReactionDataNumber
├─ eReactionType
├─ eExpPurpose
├─ sCompiler
├─ sContributor
├─ dateDateAdded
├─ Participant [1..*]
│  ├─ RegNum
│  │  └─ nOrgNum
│  ├─ nSampleNm
│  ├─ ePhase
│  └─ nStoichiometricCoef
├─ Property [1..*]
│  ├─ nPropNumber
│  ├─ Property-MethodID
│  │  └─ PropertyGroup
│  │     └─ <GroupName>
│  │        ├─ ePropName
│  │        ├─ eMethodName
│  │        └─ sMethodName
│  ├─ eStandardState
│  ├─ nTemperature-K
│  ├─ nTemperatureDigits
│  ├─ nPressure-kPa
│  ├─ nPressureDigits
│  └─ CombinedUncertainty [0..*]
│     ├─ nCombUncertAssessNum
│     ├─ eCombUncertEvalMethod
│     ├─ nCombUncertLevOfConfid
│     └─ sCombUncertEvaluator
├─ Constraint [0..*]
│  ├─ nConstraintNumber
│  ├─ ConstraintID
│  │  ├─ ConstraintType
│  │  │  └─ eTemperature / ePressure / eComponentComposition / eSolventComposition / eMiscellaneous
│  │  └─ RegNum
│  │     └─ nOrgNum
│  ├─ nConstraintValue
│  ├─ nConstrDigits
│  └─ ConstraintPhaseID
│     ├─ eConstraintPhase
│     └─ RegNum
│        └─ nOrgNum
├─ Variable [0..*]
│  ├─ nVarNumber
│  ├─ VariableID
│  │  ├─ VariableType
│  │  │  └─ eTemperature / ePressure / eComponentComposition / eSolventComposition / eMiscellaneous
│  │  └─ RegNum
│  │     └─ nOrgNum
│  └─ VarPhaseID
│     ├─ eVarPhase
│     └─ RegNum
│        └─ nOrgNum
└─ NumValues [0..*]
   ├─ VariableValue [0..*]
   │  ├─ nVarNumber
   │  ├─ nVarValue
   │  └─ nVarDigits
   └─ PropertyValue [1..*]
      ├─ nPropNumber
      ├─ nPropValue
      ├─ nPropDigits
      └─ CombinedUncertainty
         ├─ nCombUncertAssessNum
         └─ nCombExpandUncertValue