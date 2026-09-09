# ThermoML Index — Raw JSON Coverage Validation Report

**Source**: `thermoml_raw.db` — full scan of all raw `json_data`

**Scanned**: 11,923 papers


## 1. Global Totals (from raw JSON scan)

| Metric | Count |
|---|---:|
| Papers parsed | 11,923 |
| Total blocks | 123,727 |
| — PureOrMixtureData | 122,481 |
| — ReactionData | 1,246 |
| Total datapoints (NumValues) | 2,692,934 |
| Total property instances | 130,104 |
| Total variable instances | 168,687 |
| Total constraint instances | 101,278 |
| Measurement — standard | 76,184 |
| Measurement — custom | 53,919 |
| Measurement — none | 1 |
| Compound entries (paper-level) | 61,113 |
| Unique canonical compound keys in raw JSON | 8,526 |
| Unique property names | 105 |
| Unique variable names | 34 |
| Unique constraint names | 24 |
| Unique standard methods | 129 |
| Unique custom methods | 2,647 |
| Unique property groups | 12 |

## 2. Property Coverage

- **CSV list**: 105 unique prop_ids
- **Raw JSON**: 105 unique names, 130,104 total instances
- **Type coverage**: 105/105 (100.0%)
- **Instance coverage**: 130,104/130,104 (100.00%)

### Full frequency table (from raw JSON):

| Rank | Property Name | Instances | In CSV? |
|---:|---|---:|:---:|
| 1 | Mass density, kg/m3 | 23,070 | ✓ |
| 2 | Mole fraction | 20,920 | ✓ |
| 3 | Activity coefficient | 9,696 | ✓ |
| 4 | Viscosity, Pa*s | 8,475 | ✓ |
| 5 | Vapor or sublimation pressure, kPa | 8,067 | ✓ |
| 6 | Mass fraction | 7,072 | ✓ |
| 7 | Refractive index (Na D-line) | 6,772 | ✓ |
| 8 | Speed of sound, m/s | 5,781 | ✓ |
| 9 | Molar heat capacity at constant pressure, J/K/mol | 3,113 | ✓ |
| 10 | Molar enthalpy of transition or fusion, kJ/mol | 2,891 | ✓ |
| 11 | Solid-liquid equilibrium temperature, K | 2,786 | ✓ |
| 12 | Normal melting temperature, K | 2,756 | ✓ |
| 13 | Surface tension liquid-gas, N/m | 2,525 | ✓ |
| 14 | Boiling temperature at pressure P, K | 2,438 | ✓ |
| 15 | Molar enthalpy of solution, kJ/mol | 1,970 | ✓ |
| 16 | Triple point temperature, K | 1,963 | ✓ |
| 17 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | 1,703 | ✓ |
| 18 | Electrical conductivity, S/m | 1,162 | ✓ |
| 19 | Molality, mol/kg | 974 | ✓ |
| 20 | Molar enthalpy of vaporization or sublimation, kJ/mol | 903 | ✓ |
| 21 | Liquid-liquid equilibrium temperature, K | 896 | ✓ |
| 22 | Molar enthalpy, kJ/mol | 760 | ✓ |
| 23 | Amount concentration (molarity), mol/dm3 | 755 | ✓ |
| 24 | Critical temperature, K | 694 | ✓ |
| 25 | Specific internal energy of reaction at constant volume, J/g | 639 | ✓ |
| 26 | Critical pressure, kPa | 606 | ✓ |
| 27 | Normal boiling temperature, K | 590 | ✓ |
| 28 | Henry's Law constant (mole fraction scale), kPa | 549 | ✓ |
| 29 | Excess molar volume, m3/mol | 546 | ✓ |
| 30 | Binary diffusion coefficient, m2/s | 540 | ✓ |
| 31 | Molar entropy, J/K/mol | 521 | ✓ |
| 32 | Eutectic temperature, K | 518 | ✓ |
| 33 | (Relative) activity | 496 | ✓ |
| 34 | Thermal conductivity, W/m/K | 484 | ✓ |
| 35 | Mass ratio of solute to solvent | 413 | ✓ |
| 36 | Molar enthalpy of reaction, kJ/mol | 376 | ✓ |
| 37 | Molar conductivity, S*m2/mol | 310 | ✓ |
| 38 | Osmotic coefficient | 299 | ✓ |
| 39 | Refractive index (other wavelength) | 287 | ✓ |
| 40 | Kinematic viscosity, m2/s | 283 | ✓ |
| 41 | Molar volume, m3/mol | 282 | ✓ |
| 42 | Relative permittivity at various frequencies | 280 | ✓ |
| 43 | Molar heat capacity at saturation pressure, J/K/mol | 271 | ✓ |
| 44 | Relative permittivity at zero frequency | 264 | ✓ |
| 45 | Azeotropic composition: mole fraction | 247 | ✓ |
| 46 | Molar enthalpy of dilution, kJ/mol | 246 | ✓ |
| 47 | Eutectic composition: mole fraction | 228 | ✓ |
| 48 | Interfacial tension, N/m | 210 | ✓ |
| 49 | Molar enthalpy function {Hm(T)-Hm(0)}/T, J/K/mol | 210 | ✓ |
| 50 | Mass concentration, kg/m3 | 204 | ✓ |
| 51 | Thermal diffusivity, m2/s | 138 | ✓ |
| 52 | Critical density, kg/m3 | 107 | ✓ |
| 53 | Henry's Law constant (molality scale), kPa*kg/mol | 95 | ✓ |
| 54 | Mean ionic activity coefficient | 94 | ✓ |
| 55 | Upper consolute temperature, K | 89 | ✓ |
| 56 | Azeotropic temperature, K | 85 | ✓ |
| 57 | Isobaric coefficient of expansion, 1/K | 82 | ✓ |
| 58 | Thermodynamic equilibrium constant | 79 | ✓ |
| 59 | Apparent molar volume, m3/mol | 77 | ✓ |
| 60 | Azeotropic pressure, kPa | 73 | ✓ |
| 61 | Heat capacity at constant pressure per volume, J/K/m3 | 71 | ✓ |
| 62 | Apparent molar heat capacity, J/K/mol | 70 | ✓ |
| 63 | Molar Gibbs energy of reaction, kJ/mol | 68 | ✓ |
| 64 | Amount density, mol/m3 | 62 | ✓ |
| 65 | Molar internal energy of reaction at constant volume, kJ/mol | 62 | ✓ |
| 66 | Henry's Law constant (amount concentration scale), kPa*dm3/mol | 55 | ✓ |
| 67 | Quadruple (quintuple) point temperature, K | 55 | ✓ |
| 68 | Tracer diffusion coefficient, m2/s | 54 | ✓ |
| 69 | Molar heat capacity at constant volume, J/K/mol | 53 | ✓ |
| 70 | Fugacity coefficient | 49 | ✓ |
| 71 | Specific volume, m3/kg | 48 | ✓ |
| 72 | Amount ratio of solute to solvent | 42 | ✓ |
| 73 | Partial molar enthalpy, kJ/mol | 41 | ✓ |
| 74 | Upper consolute composition: mole fraction | 41 | ✓ |
| 75 | Eutectic composition: mass fraction | 38 | ✓ |
| 76 | Partial pressure, kPa | 35 | ✓ |
| 77 | Specific heat capacity at constant pressure, J/K/kg | 34 | ✓ |
| 78 | Monotectic temperature, K | 29 | ✓ |
| 79 | Self diffusion coefficient, m2/s | 28 | ✓ |
| 80 | Partial molar volume, m3/mol | 25 | ✓ |
| 81 | Excess molar heat capacity, J/K/mol | 23 | ✓ |
| 82 | Molar enthalpy of mixing with solvent, kJ/mol | 23 | ✓ |
| 83 | Equilibrium constant in terms of mole fraction | 16 | ✓ |
| 84 | Ostwald coefficient | 14 | ✓ |
| 85 | Critical molar volume, m3/mol | 14 | ✓ |
| 86 | Apparent molar enthalpy, kJ/mol | 12 | ✓ |
| 87 | Isothermal compressibility, 1/kPa | 11 | ✓ |
| 88 | Lower consolute temperature, K | 11 | ✓ |
| 89 | Peritectic temperature, K | 8 | ✓ |
| 90 | 2nd virial coefficient, m3/mol | 7 | ✓ |
| 91 | 3rd virial coefficient, m6/mol2 | 5 | ✓ |
| 92 | Equilibrium constant in terms of partial pressure, kPa^n | 5 | ✓ |
| 93 | Excess molar Gibbs energy, kJ/mol | 5 | ✓ |
| 94 | Compressibility factor | 4 | ✓ |
| 95 | Lower consolute composition: mole fraction | 4 | ✓ |
| 96 | Thermal pressure coefficient, kPa/K | 3 | ✓ |
| 97 | Joule-Thomson coefficient, K/kPa | 3 | ✓ |
| 98 | Upper consolute pressure, kPa | 3 | ✓ |
| 99 | Volume fraction | 3 | ✓ |
| 100 | Mole fraction in LLG critical state | 2 | ✓ |
| 101 | Ratio of amount of solute to mass of solution, mol/kg | 2 | ✓ |
| 102 | Monotectic composition: mole fraction | 2 | ✓ |
| 103 | Lower consolute pressure, kPa | 2 | ✓ |
| 104 | Molar entropy of reaction, J/K/mol | 1 | ✓ |
| 105 | Lower consolute composition: mass fraction | 1 | ✓ |

## 3. Variable Coverage

- **CSV list**: 34 unique var_ids
- **Raw JSON**: 34 unique names, 168,687 total instances
- **Type coverage**: 34/34 (100.0%)
- **Instance coverage**: 168,687/168,687 (100.00%)

### Full frequency table (from raw JSON):

| Rank | Variable Name | Instances | In CSV? |
|---:|---|---:|:---:|
| 1 | Temperature, K | 88,800 | ✓ |
| 2 | Mole fraction | 32,453 | ✓ |
| 3 | Pressure, kPa | 23,843 | ✓ |
| 4 | Molality, mol/kg | 8,702 | ✓ |
| 5 | Mass fraction | 7,097 | ✓ |
| 6 | Solvent: Molality, mol/kg | 1,751 | ✓ |
| 7 | Solvent: Mass fraction | 1,634 | ✓ |
| 8 | Solvent: Mole fraction | 1,621 | ✓ |
| 9 | Amount concentration (molarity), mol/dm3 | 1,286 | ✓ |
| 10 | Solvent: Amount concentration (molarity), mol/dm3 | 221 | ✓ |
| 11 | Final molality of solute, mol/kg | 192 | ✓ |
| 12 | Initial molality of solute, mol/kg | 169 | ✓ |
| 13 | Solvent: Amount ratio of component to other component of binary solvent | 133 | ✓ |
| 14 | Mass ratio of solute to solvent | 116 | ✓ |
| 15 | Solvent: Volume fraction | 107 | ✓ |
| 16 | Frequency, MHz | 85 | ✓ |
| 17 | Volume fraction | 81 | ✓ |
| 18 | Amount ratio of solute to solvent | 79 | ✓ |
| 19 | Ratio of amount of solute to mass of solution, mol/kg | 74 | ✓ |
| 20 | Mass density, kg/m3 | 49 | ✓ |
| 21 | Wavelength, nm | 41 | ✓ |
| 22 | Solvent: Mass ratio of component to other component of binary solvent | 38 | ✓ |
| 23 | Ratio of mass of solute to volume of solution, kg/m3 | 31 | ✓ |
| 24 | Solvent: Volume ratio of component to other component of binary solvent | 29 | ✓ |
| 25 | Solvent: Ratio of component mass to volume of solvent, kg/m3 | 14 | ✓ |
| 26 | Lower temperature, K | 10 | ✓ |
| 27 | Upper temperature, K | 10 | ✓ |
| 28 | Solvent: Ratio of amount of component to mass of solvent, mol/kg | 8 | ✓ |
| 29 | Amount density, mol/m3 | 3 | ✓ |
| 30 | Specific volume, m3/kg | 2 | ✓ |
| 31 | Initial mass fraction of solute | 2 | ✓ |
| 32 | Initial mole fraction of solute | 2 | ✓ |
| 33 | Final mole fraction of solute | 2 | ✓ |
| 34 | Volume ratio of solute to solvent | 2 | ✓ |

## 4. Constraint Coverage

- **CSV list**: 24 unique constr_ids
- **Raw JSON**: 24 unique names, 101,278 total instances
- **Type coverage**: 24/24 (100.0%)
- **Instance coverage**: 101,278/101,278 (100.00%)

### Full frequency table (from raw JSON):

| Rank | Constraint Name | Instances | In CSV? |
|---:|---|---:|:---:|
| 1 | Pressure, kPa | 69,532 | ✓ |
| 2 | Temperature, K | 15,426 | ✓ |
| 3 | Mole fraction | 11,333 | ✓ |
| 4 | Frequency, MHz | 1,885 | ✓ |
| 5 | Mass fraction | 482 | ✓ |
| 6 | Solvent: Molality, mol/kg | 469 | ✓ |
| 7 | Solvent: Mole fraction | 444 | ✓ |
| 8 | Molality, mol/kg | 431 | ✓ |
| 9 | Wavelength, nm | 246 | ✓ |
| 10 | Solvent: Mass fraction | 228 | ✓ |
| 11 | Solvent: Amount concentration (molarity), mol/dm3 | 202 | ✓ |
| 12 | Amount concentration (molarity), mol/dm3 | 170 | ✓ |
| 13 | Amount ratio of solute to solvent | 107 | ✓ |
| 14 | Initial molality of solute, mol/kg | 71 | ✓ |
| 15 | Solvent: Amount ratio of component to other component of binary solvent | 67 | ✓ |
| 16 | Final molality of solute, mol/kg | 49 | ✓ |
| 17 | Ratio of amount of solute to mass of solution, mol/kg | 48 | ✓ |
| 18 | Solvent: Mass ratio of component to other component of binary solvent | 30 | ✓ |
| 19 | Solvent: Volume fraction | 26 | ✓ |
| 20 | Mass ratio of solute to solvent | 12 | ✓ |
| 21 | Volume fraction | 9 | ✓ |
| 22 | Mass density, kg/m3 | 8 | ✓ |
| 23 | Solvent: Ratio of component mass to volume of solvent, kg/m3 | 2 | ✓ |
| 24 | Final mass fraction of solute | 1 | ✓ |

## 5. Standard Measurement Method Coverage

- **CSV list**: 129 unique meas_ids
- **Raw JSON**: 129 unique names, 76,184 total instances
- **Type coverage**: 129/129 (100.0%)
- **Instance coverage**: 76,184/76,184 (100.00%)

### Full frequency table (from raw JSON):

| Rank | Method Name | Instances | In CSV? |
|---:|---|---:|:---:|
| 1 | Chromatography | 21,413 | ✓ |
| 2 | Vibrating tube method | 13,110 | ✓ |
| 3 | Standard Abbe refractometry | 6,115 | ✓ |
| 4 | Capillary tube (Ostwald; Ubbelohde) method | 3,407 | ✓ |
| 5 | Ebulliometric method (Recirculating still) | 3,244 | ✓ |
| 6 | Pycnometric method | 2,664 | ✓ |
| 7 | Sing-around technique in a fixed-path interferometer | 2,259 | ✓ |
| 8 | Falling or rolling sphere viscometry | 1,243 | ✓ |
| 9 | Small sample (50 mg) DSC | 1,173 | ✓ |
| 10 | Density calibration data | 1,157 | ✓ |
| 11 | Concentric cylinders viscometry | 1,082 | ✓ |
| 12 | Flow calorimetry | 1,003 | ✓ |
| 13 | Calvet calorimetry | 911 | ✓ |
| 14 | Alternating current cell with electrodes | 906 | ✓ |
| 15 | Linear variable-path acoustic interferometer | 905 | ✓ |
| 16 | Phase equilibration | 806 | ✓ |
| 17 | Vacuum adiabatic calorimetry | 778 | ✓ |
| 18 | Single path-length method | 732 | ✓ |
| 19 | Ring tensiometer | 719 | ✓ |
| 20 | Pulse-echo method | 702 | ✓ |
| 21 | Small (less than 1 g) adiabatic calorimetry | 606 | ✓ |
| 22 | Pendant drop shape | 592 | ✓ |
| 23 | Transpiration method | 585 | ✓ |
| 24 | Index of refraction calibration data | 522 | ✓ |
| 25 | Static bomb calorimetry | 472 | ✓ |
| 26 | Titration calorimetry | 456 | ✓ |
| 27 | Calculated with densities of this investigation | 370 | ✓ |
| 28 | Adiabatic calorimetry | 355 | ✓ |
| 29 | Large sample (1 g) DSC | 343 | ✓ |
| 30 | Drop calorimetry | 343 | ✓ |
| 31 | Drop volume | 311 | ✓ |
| 32 | Cone and plate viscometry | 291 | ✓ |
| 33 | Power-compensation calorimetry | 289 | ✓ |
| 34 | Maximal bubble pressure | 286 | ✓ |
| 35 | Visual observation in an unstirred cell | 284 | ✓ |
| 36 | By X=Y | 265 | ✓ |
| 37 | Taylor dispersion method | 264 | ✓ |
| 38 | Correlation gas chromatography | 258 | ✓ |
| 39 | Derived from phase diagram analysis | 246 | ✓ |
| 40 | Hot wire method | 244 | ✓ |
| 41 | Rotating bomb calorimetry | 236 | ✓ |
| 42 | Direct measurement | 234 | ✓ |
| 43 | X-ray diffraction | 213 | ✓ |
| 44 | Parallel plate capacitor | 199 | ✓ |
| 45 | Derived by Second law | 189 | ✓ |
| 46 | Gas chromatography | 185 | ✓ |
| 47 | Static calorimetry | 182 | ✓ |
| 48 | Direct current cell with electrodes | 164 | ✓ |
| 49 | Buoyancy - hydrostatic balance with magnetic suspension - one sinker | 151 | ✓ |
| 50 | Vibrating wire viscometry | 141 | ✓ |
| 51 | Solution calorimetry | 137 | ✓ |
| 52 | Distillation | 128 | ✓ |
| 53 | Coaxial cylinder capacitor | 126 | ✓ |
| 54 | Buoyancy - hydrostatic balance | 125 | ✓ |
| 55 | Direct dilatometry | 123 | ✓ |
| 56 | Other PVT measurement | 93 | ✓ |
| 57 | Extra sensitive DSC | 92 | ✓ |
| 58 | Capillary rise | 85 | ✓ |
| 59 | Rate of evaporation | 78 | ✓ |
| 60 | Manometric method | 77 | ✓ |
| 61 | Derived from PVT data | 71 | ✓ |
| 62 | Resistive pulse heating | 66 | ✓ |
| 63 | Bellows volumetry | 65 | ✓ |
| 64 | Constant-volume piezometry | 64 | ✓ |
| 65 | Heating/Cooling curves | 57 | ✓ |
| 66 | Drop weight | 56 | ✓ |
| 67 | Moving piston method | 55 | ✓ |
| 68 | Large-sample thermal analysis | 55 | ✓ |
| 69 | Visual observation in a stirred cell | 52 | ✓ |
| 70 | By T or P extreme | 51 | ✓ |
| 71 | Diaphragm manometer | 51 | ✓ |
| 72 | NMR spectrometry | 48 | ✓ |
| 73 | Micro-bomb calorimetry | 46 | ✓ |
| 74 | Oscillating disk viscometry | 43 | ✓ |
| 75 | Twin ebulliometer | 42 | ✓ |
| 76 | Buoyancy - hydrostatic balance with magnetic suspension - two sinkers | 38 | ✓ |
| 77 | Coaxial cylinder method | 36 | ✓ |
| 78 | Parallel plate method | 34 | ✓ |
| 79 | Static method | 34 | ✓ |
| 80 | Burnett expansion method | 31 | ✓ |
| 81 | Open capillary | 30 | ✓ |
| 82 | NMR spin-echo technique | 30 | ✓ |
| 83 | By T(X) extreme | 29 | ✓ |
| 84 | Differential ebulliometry | 29 | ✓ |
| 85 | Isoperibol calorimetry | 28 | ✓ |
| 86 | Torsion effusion method | 26 | ✓ |
| 87 | By P(X) extreme | 25 | ✓ |
| 88 | Isothermal displacement | 22 | ✓ |
| 89 | Derived analytically | 19 | ✓ |
| 90 | Dispersion | 18 | ✓ |
| 91 | Chemical equilibration / Heterogeneous equilibration | 17 | ✓ |
| 92 | Light diffraction method | 14 | ✓ |
| 93 | Reentrant cavity resonator | 14 | ✓ |
| 94 | Inclined piston gauge | 13 | ✓ |
| 95 | Hot disk method | 11 | ✓ |
| 96 | Optical interferometry | 11 | ✓ |
| 97 | Speed of sound calibration data | 11 | ✓ |
| 98 | Levitation methods | 10 | ✓ |
| 99 | Differential flow calorimetry | 9 | ✓ |
| 100 | Spherical resonator | 9 | ✓ |
| 101 | Derived from speed of sound | 9 | ✓ |
| 102 | Voltage change across transformer (no electrode) | 9 | ✓ |
| 103 | Laser pulse heating | 8 | ✓ |
| 104 | Derived graphically | 8 | ✓ |
| 105 | Cylindrical cavity resonance method | 8 | ✓ |
| 106 | Thin-film microcalorimeter | 8 | ✓ |
| 107 | Optical method | 8 | ✓ |
| 108 | Drop ice or diphenyl ether calorimetry | 8 | ✓ |
| 109 | Dual path-length method | 7 | ✓ |
| 110 | Spherical cavity resonance method | 6 | ✓ |
| 111 | Dynamic equilibration | 6 | ✓ |
| 112 | Mass-spectrometry | 6 | ✓ |
| 113 | Isoteniscope | 5 | ✓ |
| 114 | AC calorimetry | 5 | ✓ |
| 115 | Volume change | 5 | ✓ |
| 116 | Sessile Drop | 5 | ✓ |
| 117 | Rectilinear diameter | 5 | ✓ |
| 118 | Gamma attenuation method | 4 | ✓ |
| 119 | Closed cup calorimetry  | 4 | ✓ |
| 120 | Extrapolated vapor pressure | 3 | ✓ |
| 121 | Expansion technique | 3 | ✓ |
| 122 | Static equilibration | 3 | ✓ |
| 123 | Vibrating wire densiometer | 3 | ✓ |
| 124 | Photoacoustic method | 3 | ✓ |
| 125 | Draining crucible | 2 | ✓ |
| 126 | Flame calorimetry | 1 | ✓ |
| 127 | Oscillating viscometer | 1 | ✓ |
| 128 | Multiple path-length method | 1 | ✓ |
| 129 | Dipping refractometry (monochromatic) | 1 | ✓ |

## 6. Compound Coverage

- **CSV list**: 8,526 unique canonical compound keys
- **Raw JSON**: 8,526 unique canonical compound keys, 61,113 total compound entries
- **Type coverage**: 8,526/8,526 (100.0%)
- **Instance coverage**: 61,113/61,113 (100.00%)

**All canonical compound keys from raw JSON are present in the CSV.**

**Note**: 61 compound entries in raw JSON have no InChIKey and are covered by fallback canonical keys.


## 7. Property Group Distribution

| Rank | Group Name | Block Instances |
|---:|---|---:|
| 1 | CompositionAtPhaseEquilibrium | 31,696 |
| 2 | VolumetricProp | 24,222 |
| 3 | RefractionSurfaceTensionSoundSpeed | 16,119 |
| 4 | PhaseTransition | 12,805 |
| 5 | TransportProp | 11,474 |
| 6 | VaporPBoilingTAzeotropTandP | 11,253 |
| 7 | ActivityFugacityOsmoticProp | 10,634 |
| 8 | HeatCapacityAndDerivedProp | 5,036 |
| 9 | ExcessPartialApparentEnergyProp | 4,093 |
| 10 | Criticals | 1,526 |
| 11 | ReactionStateChangeProp | 1,146 |
| 12 | ReactionEquilibriumProp | 100 |

## 8. Custom Measurement Methods (top 30)

These methods have no standard `meas_id` — they are free-text author descriptions.

| Rank | Custom Method Name | Block Instances |
|---:|---|---:|
| 1 | DTA | 4,038 |
| 2 | Titration method | 3,717 |
| 3 | DSC | 3,437 |
| 4 | Closed cell (Static) method | 2,833 |
| 5 | VISOBS | 1,971 |
| 6 | VIBTUB:UFactor:4 | 1,788 |
| 7 | OTHER | 1,464 |
| 8 | gravimetric | 1,353 |
| 9 | VIBTUB:UFactor:2 | 793 |
| 10 | VIBTUB:UFactor:8 | 595 |
| 11 | CAPTUB:UFactor:2 | 591 |
| 12 | VIBTUB:UFactor:6 | 556 |
| 13 | ISOPERIBOL | 542 |
| 14 | gravimetric method | 530 |
| 15 | CHROM:UFactor:4 | 507 |
| 16 | CAPTUB:UFactor:4 | 486 |
| 17 | Gravimetric | 423 |
| 18 | EBULLIO:UFactor:8 | 399 |
| 19 | Calculated from knudsen effusion weight loss | 358 |
| 20 | CHROM:UFactor:2 | 355 |
| 21 | CHROM:UFactor:8 | 346 |
| 22 | SPECTR | 343 |
| 23 | VIBTUB:UFactor:16 | 336 |
| 24 | VISOBS:UFactor:4 | 262 |
| 25 | EBULLIO:UFactor:4 | 260 |
| 26 | DTA:corrimp | 259 |
| 27 | PYCNOM:UFactor:4 | 247 |
| 28 | EBULLIO:UFactor:2 | 237 |
| 29 | VIBTUB::UFactor:4 | 236 |
| 30 | CCELL:UFactor:8 | 230 |
| ... | +2617 more unique custom methods | |

## 9. Coverage Summary

| Entity | CSV Types | Raw Types | Type Coverage | Instance Coverage |
|---|---:|---:|---:|---:|
| Properties | 105 | 105 | 105/105 (100.0%) | 130,104/130,104 (100.00%) |
| Variables | 34 | 34 | 34/34 (100.0%) | 168,687/168,687 (100.00%) |
| Constraints | 24 | 24 | 24/24 (100.0%) | 101,278/101,278 (100.00%) |
| Std Methods | 129 | 129 | 129/129 (100.0%) | 76,184/76,184 (100.00%) |
| Compounds | 8,526 | 8,526 | 8526/8526 (100.0%) | 61,113/61,113 (100.00%) |

