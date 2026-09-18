# Reference alignment findings for Q1

These checks use the local raw ThermoML corpus, not model recollection or card-level min/max summaries. The unit-bearing property name, DOI, raw block number, one-based point number, component identity, temperature, pressure, composition basis, phase, method, and uncertainty are retained in `reference_evidence.json`. `reference_extract.py` and `reference_claim_checks.py` reproduce the evidence without database writes or API calls.

## SRD-46 scope

The local `SRD46_research_agent/NIST_SRD46_core_db_storage/srd46_cards.db` has 8,801 measured ligand pKa rows and 89,824 measured ligand-metal stability rows. Its schema contains equilibrium constant, ionic strength, solvent and temperature fields, not density, viscosity, heat capacity or a thermophysical measurement table. No scientific alignment/value score against SRD-46 is available for these six ThermoML questions. A solvent-name/25 C match does not make a stability constant the same observable as an activity coefficient, density or viscosity. The actual ThermoML numerical audit follows.

## Q1.1 — Equimolar ethanol + water density

- DOI `10.1016/j.fluid.2004.11.019`, block 2, point 44: **859.3 +/- 0.3 kg/m3**, ethanol mole fraction **0.498**, 298.15 K, 100 kPa, liquid, vibrating-tube method. This is near-equimolar, not an exact x=0.500 measurement.
- A closer composition exists: DOI `10.1021/je060335h`, block 1, point 153: **858.98 +/- 0.39 kg/m3** at x(ethanol)=0.49976, 298.15 K, 101 kPa.
- An exact equimolar row also exists: DOI `10.1021/je800150h`, block 9, point 55: **859.2 +/- 3.3 kg/m3**, x(water)=0.5, 298.15 K, 101 kPa, pycnometry.
- Thus about **859 kg/m3** is supported. A value of 927 kg/m3 is not a rounding/interpolation issue. Using densities averaged across pressure or across x=0.4--0.6 does not answer the precise stated condition.

## Q1.2 — Hexane + ethanol property coverage near 25 C

At or very near equimolar composition, the inspected binary blocks establish **eight property families**: density, viscosity, refractive index, sound speed, excess molar enthalpy, excess molar volume, surface tension, and binary diffusion coefficient. Critical points and atmospheric boiling/VLE data in this system do not establish 25 C liquid-property availability.

| Property | Raw source / block / point | Value and composition at 298.15 K |
|---|---|---|
| Density | `10.1016/j.jct.2007.02.008` / 24 / 20 | 692.1 kg/m3; x(ethanol)=0.4999; 101 kPa |
| Viscosity | `10.1021/je800925v` / 9 | 0.0004288 Pa s; x(ethanol)=0.496; pressure not explicit |
| Refractive index | `10.1016/j.jct.2007.02.008` / 22 / 20 | 1.36652; x(ethanol)=0.4999; 101 kPa |
| Sound speed | `10.1016/j.jct.2007.02.008` / 23 / 20 | 1073 m/s; x(ethanol)=0.4999; 101 kPa |
| Excess molar enthalpy | `10.1016/j.fluid.2005.08.001` / 5 / 10 | 0.5637 kJ/mol; x(ethanol)=0.49; 101.325 kPa |
| Excess molar volume | `10.1016/j.fluid.2005.08.001` / 6 / 11 | 4.08e-7 m3/mol; x(ethanol)=0.4995; 101.325 kPa |
| Surface tension | `10.1021/je700215z` / 5 | 0.01829 N/m; x(ethanol)=0.5071; pressure not explicit |
| Binary diffusion | `10.1021/je0497303` / 8 / 5 | **1.3e-9 m2/s at exact x(ethanol)=0.5**; 101.3 kPa |

The enthalpy block maximum is **0.5795 kJ/mol**, so 1.244 kJ/mol is not supported by that block. Diffusion is neither 1.81e-9 at x=0.5 nor limited to infinite dilution. The raw diffusion uncertainty is recorded as **0.07** despite the m2/s-valued property being order 1e-9; this is a suspicious source/serialization unit issue, retained verbatim and not treated as a sensible uncertainty.

The same refractive-index block gives pure hexane **1.37217** and pure ethanol **1.35929** at 298.15 K, 101 kPa. Therefore hexane has the *higher* refractive index in those data.

## Q1.3 — Equimolar propan-2-ol + water density

DOI `10.1021/je700700f`, block 17, point 7 gives **838.8 +/- 0.4 kg/m3**, x(propan-2-ol)=**0.4981**, 298.15 K, 101 kPa, liquid, vibrating-tube method. Near-equimolar retrieval is supported; an exact x=0.500 claim is not supported by this row. A molality=0.5 row is not equimolar and cannot be substituted.

Raw citation authors are **B. Gonzalez, N. Calvar, E. Gonzalez, A. Dominguez**, published in *J. Chem. Eng. Data* **53** (2008), 881--887. Neither a Soliman/Marschall attribution nor Pang attribution matches this DOI.

## Q1.4 — Aqueous LiCl activity coefficients

DOI `10.1016/j.fluid.2014.08.026`, block 13 contains **141 mean ionic activity coefficient points** for binary LiCl + water, **298.15 K, 101 kPa**, calculated from EMF cell potentials. LiCl molality spans **0.0033--1.5555 mol/kg** and gamma spans **0.7406--0.9425**.

- Point 56: molality 0.0033, gamma **0.9425**.
- Point 46: molality **0.4743**, gamma minimum **0.7406**.
- Point 55: molality **1.5555**, gamma **0.8461**.

The curve is not monotonic decreasing to a minimum at the highest concentration. Explicitly denying activity-coefficient data is contradicted by this block. DOI `10.1016/j.jct.2016.07.003`, block 4 is a separate binary LiCl + water **osmotic coefficient** dataset; its broader molality range must not be described as directly measured ionic activity coefficients. Its block 5 is relative activity, another distinct observable.

## Q1.5 — Pure ethanol viscosity methods

Capillary values cited around **1.077--1.093 mPa s** are supported by their raw pure-ethanol rows. Correct directly matched examples of other methods include:

| Method | Raw source / block / point | Dynamic viscosity | Conditions |
|---|---|---:|---|
| Falling/rolling sphere | `10.1016/j.jct.2009.06.023` / 1 / 4 | 0.0010569 Pa s | 298.15 K, 101.325 kPa |
| Falling/rolling sphere | `10.1016/j.jct.2012.10.008` / 6 / 2 | 0.001134 Pa s | 298.15 K, 101.325 kPa |
| Falling/rolling sphere | `10.1016/j.jct.2013.09.044` / 6 / 1 | 0.0011866 Pa s | 298.2 K, 100 kPa |
| Concentric cylinders (rotational) | `10.1021/je200600p` / 3 / 2 | **0.0010371 Pa s** | 298.15 K, 101.325 kPa |
| Concentric cylinders (rotational) | `10.1016/j.jct.2018.02.022` / 3 / 2 | 0.0010914 Pa s | 298.15 K, **92.3 kPa**, not standard atmosphere |

Thus a categorical absence of rotational viscometry is false. The exact-data table is more informative than averaging a high-pressure block across temperatures and pressures.

Some citations to additional techniques are wrong at the block/component level even though ethanol appears elsewhere in the same paper. `10.1016/j.fluid.2014.10.044` concentric-cylinder block 8 is **choline chloride + hydroxyethanoic acid**, not ethanol. `10.1016/j.fluid.2015.01.011` concentric-cylinder blocks concern ionic-liquid systems, not ethanol. `10.1016/j.fluid.2017.09.005` pressure-drop block 2 is **methanol + water**; its ethanol + water block 4 does contain pure endpoints but uses **capillary** viscometry at **523.2--618.2 K**, not pressure-drop viscosity near25C. `10.1016/j.jct.2011.02.018` concentric-cylinder block 2 is ethanol + MTBE with MTBE mole fraction **0.0097--0.9868, no zero fraction**; thus no pure ethanol endpoint. `10.1016/j.jct.2012.10.002` moving-piston block 9 is ethanol + CO2 with CO2 mole fraction **0.049--0.589, no zero fraction**, at1020--6080kPa/T303.2--323.2K. Its principal mismatch is absence of pure-ethanol data, not merely using a slightly different temperature. Full variable ranges are in `reference_claim_checks.json`.

## Q1.6 — Pure water isobaric heat capacity

Eight raw 298.15 K liquid points from **seven DOIs** have explicit pressure conditions of 100, 101 or 101.325 kPa; values span **74.79944256--75.664176 J/(mol K)**. A central answer near **75.3 J/(mol K)** is supported. These are individual experimental results, not a rigorously weighted consensus.

For the actual hierarchical answer's two cited studies, explicit pure-water block 1 supports the values, and mixture block 3 also contains valid **zero-solute pure-water endpoints** (the later endpoint audit corrects the initial overly restrictive exact-component-block interpretation):

- `10.1016/j.fluid.2013.08.005`, block 1, point 1: **75.368725408 +/- 1.3061078 J/(mol K)**; point 5 at the same temperature: **75.350710128 +/- 1.304306272**; 101 kPa.
- `10.1016/j.jct.2016.09.031`, block 1, point 1: **75.11470996 +/- 1.506077408 J/(mol K)**; 101.325 kPa.

The assertion that these datasets contain no explicit uncertainties is false. `jct.2016.09.031` block 3 point 9 has molality zero and the same 75.11470996 value at 298.15 K but **100 kPa**, whereas explicit pure block 1 uses 101.325 kPa. `fluid.2013.08.005` block 3 point 1 has molality zero, value **75.368725408**, 298.15 K and 101 kPa. Thus these block-3 citations are not categorically wrong system pointers; the hierarchical source description still incorrectly substitutes the block-wide minimum75.329092 as the cited zero-solute value. Endpoint evidence is preserved in `reference_zero_solute_endpoints.json`.

`10.1021/acs.jced.7b00483`, block 1, point 1 gives **75.664176 +/- 0.16213752**; its stated interval does not contain 75.315. This is not automatically a fatal inconsistency, but calling it fully consistent *within its quoted uncertainty* is unsupported. The full observed range is about **1.15%** of 75.3, not less than 1%.

## Audit boundaries

This is a transparent targeted reference audit, not automated verification of every sentence or every possible subsystem. Exact pure/binary component-block matching avoids false joins across document-local IDs. All relevant extracted raw rows are retained, including off-target conditions. Unknown pressure, near rather than exact composition, distinct observable definitions, and source uncertainties are kept explicit. Card summaries are not treated as coordinate-matched experimental rows. No answer files, source databases or benchmark runs were modified by this audit.
