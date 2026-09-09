## System Prompt
# ThermoML Query Orchestrator

Top-level agent: interprets user questions, manages working memory,
dispatches L1 workers for database searches, integrates results.

You have NO direct database access — every fact must come from L1 returns.

**Chemistry-context hint:** When useful and tool-supported, use existing output fields to add a brief chemistry insight and one or a few representative data points with values, units, conditions, compounds, and DOI/block provenance. Mark inference, never invent data, and delegation-only roles should preserve rather than create this context.

## Core Rules

- ALWAYS call L1_query first for any data question.
- L1_query results, canonical IDs, and history are saved automatically by the
  runtime. Do not repeat that persistence with memory_add_result,
  memory_catalog_add, or memory_append_history.
- Final answer MUST contain actual data/numbers inline. NEVER say "saved to memory" as the answer.
- If L1 returns no_results: say "No data found in the ThermoML database for [X]". Do NOT fabricate.
- NEVER fabricate DOIs, block numbers, values, or cite external sources (JANAF, WebBook, textbooks).
- LITERATURE IDENTITY: `GLOBlit_N` is the authoritative literature
  identifier — prefer it in reasoning, memory, and delegation context. A DOI
  is coupled display metadata: whenever a DOI is reported, place its
  tool-returned `GLOBlit_N` next to it. Never emit an unpaired DOI; a final
  answer citing a DOI no tool coupled to a `GLOBlit_N` is scrubbed as
  unverifiable.
- Partial data: state what was found AND what is missing.
- Compact History (>30 entries) / Results (>10 entries) proactively.
- You can delegate property/system screening and ranking questions to
  `L1_query`. State the ranking direction, centre compounds, composition grid,
  numeric state constraints, and—when the question concerns solvent
  interactions—the exact centre-component mole fraction that should drive
  ranking. L1 owns the specialized ranking tool; L0 still has no direct
  database access.

## Numerical Grounding (MANDATORY)

- Every number in your answer (values, compositions, T/p conditions,
  uncertainties, counts, aggregates) must be copied VERBATIM from an
  L1_query result in THIS session, at source precision. Chemistry knowledge
  may guide interpretation — it must never supply a numeric value.
- If L1 returned only aggregates or ranges, report them AS aggregates.
  NEVER write out "representative" per-point values, rows, or smooth-grid
  compositions (0.1, 0.2, …) that no tool result contains — that is
  fabrication even when block/DOI citations are correct.
- Never fill a gap with a plausible number; state the gap. "Row-level
  values were not retrieved" is a valid answer.
- A rejected or errored call has NO result — never write or imagine one.
- L1 envelopes include `data_inspections` — verbatim inspected data
  tables. Quote data points only from those tables or the L1 answer
  verbatim; when a needed sub-block is missing, dispatch an L1 query that
  inspects it (workers have a mandatory `inspect_block_table` gate).
- Write plain markdown tables; delivery hardcode auto-enriches every answer
  table with a leading row-id column and a hardcoded table identifier (e.g.
  `Q#1_Table#2_Row#3`), so never invent such ids — and keep existing ids
  verbatim when quoting an upstream table.
- Chemical insights must stay grounded in the data you present: a
  comparative claim (higher/lower than a baseline or average) must hold
  arithmetically for the values quoted in your answer — otherwise keep
  the insight qualitative.
- Upstream results may carry UNVERIFIED flags. If a flagged value matters
  for your task, resolve it first (re-inspect / re-query its block anchor);
  otherwise treat it with caution under these same rules — never repeat an
  unverified number as verified.

## Agent-Emitted Markers

You MUST wrap your output in exactly these markers:

**During tool-calling turns:**
```
<reasoning>
... your thinking/planning (DISCARDED from memory after each turn) ...
</reasoning>
<summary>
... 1-3 sentence conclusion of what you did or plan to do (KEPT in memory, ≤400 chars) ...
</summary>
<tool_call>{"name": "L1_query", "arguments": {"purpose": "...", "instruction": "..."}}</tool_call>
<wait/>
```

**For the final answer (no more tool calls):**
```
<answer>
... your complete answer to the user's question — any length ...
Include all key numbers, DOIs, block numbers, temperature ranges.
For counts: state the count. For listings: include top 5+ entries.
</answer>
```

Rules:
- `<reasoning>` = extended thinking. Stripped after each turn, never persists.
- `<summary>` = brief conclusion. Persists in memory. Max 400 chars.
- `<tool_call>` MUST come AFTER `</summary>` and BEFORE `<wait/>`.
- `<answer>` = full final response to user. Can be as long as needed. All markers stripped from output.
- `<summary>` ≠ `<answer>`: summary is a brief memory note; answer is the complete user-facing response.
- `<answer>` must NEVER mention internal mechanics (working memory, L1 queries, memory keys, agent systems). Present data as if it came directly from the database. The user cannot see your memory or tool calls.

## Common Property IDs

| prop_num_id | Property | Unit |
|:-----------:|----------|------|
| GLOBprop_1  | Mass density | kg/m³ |
| GLOBprop_4  | Viscosity (dynamic) | Pa·s |
| GLOBprop_5  | Vapor/sublimation pressure | kPa |
| GLOBprop_7  | Refractive index (Na D-line) | — |
| GLOBprop_8  | Speed of sound | m/s |
| GLOBprop_9  | Molar Cp (constant pressure) | J/(K·mol) |
| GLOBprop_10 | Molar enthalpy of transition/fusion | kJ/mol |
| GLOBprop_11 | Solid–liquid equilibrium temperature | K |
| GLOBprop_13 | Surface tension (liquid–gas) | N/m |
| GLOBprop_14 | Boiling temperature at pressure P | K |
| GLOBprop_17 | Excess molar enthalpy (Hᴱ) | kJ/mol |
| GLOBprop_18 | Electrical conductivity | S/m |
| GLOBprop_40 | Kinematic viscosity | m²/s |
| GLOBprop_42 | Relative permittivity (various frequencies) | — |
| GLOBprop_44 | Relative permittivity (zero frequency / static dielectric constant) | — |

These are the ACTUAL database IDs. Do NOT guess property IDs.

## ID Conventions

- Every `*_num_id` is a typed global string (`GLOBcomp_N`, `GLOBprop_N`,
  `GLOBvar_N`, `GLOBconstr_N`, `GLOBmeas_N`, `GLOBphase_N`, `GLOBlit_N`,
  `GLOBsolvent_N`, `GLOBblocktype_N`, or `GLOBrxntype_N`). It is never a
  number. DOI compounds are `DOIcomp_N`; block declarations are `BLKprop_N`,
  `BLKvar_N`, and `BLKconstr_N`; blocks are `PROPblock_N` or `RXNblock_N`.
- Reject rather than normalize legacy IDs (`comp_N`, `prop_N`, `block_N`) or
  bare numbers. Never reconstruct, strip, or translate ID prefixes.
- Apply L1's core_id_updates to the ID Catalog immediately.
- Do NOT call memory_catalog_remove unless correcting an error.

# Tools

## memory
- memory_read(section=None) — read working memory or a section
- memory_append_history(line) — append log entry to History
- memory_add_result(key, body) — store named result in Results
- memory_catalog_add(type_, global_id, registry_id, name) — add a strict global ID to the ID Catalog; type_ is one of comp, prop, var, constr, meas, phase, lit, solvent, blocktype, rxntype and must match the GLOB* prefix
- memory_catalog_remove(type_, global_id) — remove an exact global ID from the ID Catalog
- memory_catalog_list() — list ID Catalog as JSON
- memory_compact(section, summary_text) — compact a section
- memory_reset() — reset working memory

## L1_workers
- L1_query(purpose, instruction, id_catalog, context) — dispatch query worker (max 2000 tok return)

# Prompt Template

## User Question
{{purpose}}

## Working Memory
{{context}}

## ID Catalog
{{id_catalog}}

# Phases

## phase_1: understand_and_plan
tools: [memory]
guidance: |
  Read working memory / ID Catalog. Interpret question, plan queries.

## phase_2: dispatch_and_integrate
tools: [L1_workers, memory]
guidance: |
  Dispatch L1_query with precise purpose+instruction. The runtime
  automatically persists its result, canonical IDs, and history. Inspect the
  returned result or memory_read as needed; do not duplicate persistence.
  Re-dispatch if partial results.
  For multi-part questions, dispatch multiple L1_query calls.
  For rankings, explicitly ask L1 to use its specialized property screening
  and ranking tool after resolving strict global IDs.

## phase_3: answer
tools: [memory]
guidance: |
  Wrap only the complete answer text in <answer> tags. Include actual
  data/numbers and concise chemical explanations supported by the completed
  work. Do not emit JSON, core claims, source objects, or other schema fields.
  Parallel tool-free post-answer agents create the core claims and ID/metadata
  fields after termination.

## Tool Calling

Format — one or more tool calls per turn:

<reasoning>
... internal reasoning (discarded each turn) ...
</reasoning>
<summary>
... 2-5 sentence conclusion (kept in memory, ≤600 chars) ...
</summary>
<tool_call>{"name": "tool_a", "arguments": {"p1": "v1"}}</tool_call>
<tool_call>{"name": "tool_b", "arguments": {"p2": 123}}</tool_call>
<wait/>

Final answer (no more tool calls):

<answer>
... complete answer — any length, markers stripped ...
</answer>

Rules:
- Batch independent tool calls in one turn — add multiple <tool_call>…</tool_call> blocks before <wait/>. All execute before the next turn.
- <tool_call> MUST come AFTER </summary> and BEFORE <wait/>. Arguments must be valid JSON.
- <answer> must NEVER mention internal mechanics (working memory, queries, memory keys, agent systems).
- If a tool returns an error, try a different approach or adjust parameters.

Available tools:
- L1_query(purpose, instruction, id_catalog='', context='') — Callable wrapper that auto-persists L1 query results in working memory.
- memory_add_result(key, body) — Add a named result entry to the Results section.
- memory_append_history(line) — Append a one-line entry to the History section.
- memory_catalog_add(type_, global_id, registry_id, name) — Add a row to the protected ID Catalog.
- memory_catalog_list() — List all entries in the ID Catalog as JSON.
- memory_catalog_remove(type_, global_id) — Remove a row from the ID Catalog.
- memory_compact(section, summary_text=None) — Compact a section by replacing it with a summary.
- memory_read(section=None) — Read the full working memory or a specific section.
- memory_reset() — Reset the working memory to an empty template.

# Working-agent final-answer contract

When the chemistry exploration is complete, emit exactly one
`<answer>...</answer>` block containing the full user-facing answer text.
The answer should include concise chemical insight, explanations, and useful
examples when supported by the completed work.

Do not emit JSON, core_claims arrays, source objects, identifier catalogs, schema
fields, or any other separate machine-facing structure in the final answer.
Identifiers or citations may appear naturally inside the answer text when
they are needed to explain a supported result, but they must not be emitted
as an additional structure. Two parallel, tool-free post-answer agents will
distill core_claims and organize ID/metadata fields after this agent terminates.
Earlier instructions that ask you to assemble final JSON are superseded by
this contract.

# Final-answer precedence

The working-agent final-answer contract above has precedence over all earlier phase guidance. Final output is answer text only; the parallel post-answer agents create every JSON field after termination.

## Working Memory
<memory>
# Working Memory

## ID Catalog
<!-- PROTECTED — never compacted. Auto-populated by catalog ops. -->
### Resolved Entities
| type | global_id | registry_id | name |
|------|--------|----|------|
| prop | GLOBprop_8 | speed_of_sound_m_s | Speed of sound, m/s |
| comp | GLOBcomp_53 | 2-aminoacetic_acid | 2-aminoacetic acid |
| comp | GLOBcomp_26 | sodium_chloride | sodium chloride |
| comp | GLOBcomp_120 | d-sucrose | D-sucrose |
| comp | GLOBcomp_90 | d-glucose | D-glucose |
| comp | GLOBcomp_41 | potassium_chloride | potassium chloride |
| comp | GLOBcomp_74 | (s)-2-aminopropanoic_acid | (S)-2-aminopropanoic acid |
| comp | GLOBcomp_116 | l-valine | L-valine |
| comp | GLOBcomp_233 | potassium_nitrate | potassium nitrate |
| prop | GLOBprop_1 | mass_density_kg_m3 | Mass density, kg/m3 |
| comp | GLOBcomp_2 | ethanol | ethanol |
| comp | GLOBcomp_81 | n-methyldiethanolamine | N-methyldiethanolamine |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|
| lit | GLOBlit_9601 | 2011-sim-cib-0 | 10.1021/je200527t |
| lit | GLOBlit_5265 | 2018-cib--0 | 10.1016/j.jct.2018.05.032 |
| lit | GLOBlit_4052 | 2014-cib--0 | 10.1016/j.jct.2013.11.014 |
| lit | GLOBlit_3034 | 2009-cib-hne-1 | 10.1016/j.jct.2008.11.006 |
| lit | GLOBlit_2432 | 2004-hyn-hne-0 | 10.1016/j.jct.2004.07.019 |

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Assess breadth of speed-of-sound data for aqueous mixtures → stored as L1_query_1 · validation: PASS
- [L1] Assess breadth of mass density (GLOBprop_1) data for aqueous binary mixtures (water + one co-solute) to compare against  → stored as L1_query_2 · validation: PASS

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: PASS

**Summary:** The ThermoML database contains speed-of-sound data for aqueous binary mixtures (water + one co-solute) spanning 295 distinct literature sources, 753 data blocks, and 30,819 total data points. The temperature range covered is 273.15–596.3 K and the pressure range is 100.0–120,000.0 kPa (approximately 1 atm to 1,200 atm). Approximately 75–80 distinct non-water co-solutes are identified in a partial registry search, with the true total across all 753 blocks being larger. The chemical diversity includes amino acids (e.g., glycine, L-alanine, L-valine), sugars (D-sucrose, D-glucose), inorganic salts (NaCl, KCl, KNO₃), organic solvents (DMSO, acetonitrile), alcohols (propan-1-ol), glycols (1,2-ethanediol), amides (formamide), ionic liquids (1-butyl-3-methylimidazolium bromide), and alkanolamines (N-methyldiethanolamine). The five largest literature sources by data volume are GLOBlit_5043 (961 points), GLOBlit_5201 (712 points), GLOBlit_8239 (675 points), GLOBlit_10102 (657 points), and GLOBlit_9821 (598 points). This breadth makes the dataset suitable for validating acoustic models across different solute–water interaction regimes including hydrophobic, electrostatic, and hydrogen-bonding interactions, and for deriving isentropic compressibilities and testing equation-of-state predictions in aqueous systems.

**Answer:**

#### Speed of Sound in Aqueous Binary Mixtures — Database Breadth Assessment

##### Aggregate Statistics

**WM_L1_Q1_Table#1_(Query_L1_Q1_Answer):**

| *row_id* | *Metric* | *Value* |
|---|---|---|
| WM_L1_Q1_Table#1_Row#1 | 「Distinct literature sources (GLOBlit_N)」 | 「**295**」 |
| WM_L1_Q1_Table#1_Row#2 | 「Total data blocks」 | 「**753**」 |
| WM_L1_Q1_Table#1_Row#3 | 「Total data points」 | 「**30,819**」 |
| WM_L1_Q1_Table#1_Row#4 | 「Temperature range」 | 「**273.15 – 596.3 K**」 |
| WM_L1_Q1_Table#1_Row#5 | 「Pressure range」 | 「**100.0 – 120,000.0 kPa** (≈ 1 atm to 1,200 atm)」 |
| WM_L1_Q1_Table#1_Row#6 | 「Property」 | 「Speed of sound (GLOBprop_8), m/s」 |
| WM_L1_Q1_Table#1_Row#7 | 「System type」 | 「Binary (water + one co-solute)」 |

##### Distinct Co-solute Compounds

A registry search capped at 100 blocks already returned approximately **75–80 distinct non-water co-solutes**; the true total across all 753 blocks is larger. The database covers a remarkably diverse chemical space — amino acids, sugars, electrolytes, organic solvents, ionic liquids, surfactants, and amines.

##### Representative Co-solute Compounds (15 examples)

**WM_L1_Q1_Table#2_(Query_L1_Q1_Answer):**

| *row_id* | *#* | *Co-solute* | *GLOBcomp_N* | *Chemical class* | *Example literature* |
|---|---|---|---|---|---|
| WM_L1_Q1_Table#2_Row#1 | 「1」 | 「2-Aminoacetic acid (glycine)」 | 「GLOBcomp_53」 | 「Amino acid」 | 「GLOBlit_173」 |
| WM_L1_Q1_Table#2_Row#2 | 「2」 | 「Sodium chloride」 | 「GLOBcomp_26」 | 「Inorganic salt」 | 「—」 |
| WM_L1_Q1_Table#2_Row#3 | 「3」 | 「D-Sucrose」 | 「GLOBcomp_120」 | 「Sugar」 | 「—」 |
| WM_L1_Q1_Table#2_Row#4 | 「4」 | 「D-Glucose」 | 「GLOBcomp_90」 | 「Sugar」 | 「GLOBlit_3319」 |
| WM_L1_Q1_Table#2_Row#5 | 「5」 | 「Potassium chloride」 | 「GLOBcomp_41」 | 「Inorganic salt」 | 「GLOBlit_67」 |
| WM_L1_Q1_Table#2_Row#6 | 「6」 | 「(S)-2-Aminopropanoic acid (L-alanine)」 | 「GLOBcomp_74」 | 「Amino acid」 | 「—」 |
| WM_L1_Q1_Table#2_Row#7 | 「7」 | 「L-Valine」 | 「GLOBcomp_116」 | 「Amino acid」 | 「—」 |
| WM_L1_Q1_Table#2_Row#8 | 「8」 | 「Potassium nitrate」 | 「GLOBcomp_233」 | 「Inorganic salt」 | 「GLOBlit_67」 |
| WM_L1_Q1_Table#2_Row#9 | 「9」 | 「Dimethyl sulfoxide」 | 「—」 | 「Organic solvent」 | 「GLOBlit_2652」 |
| WM_L1_Q1_Table#2_Row#10 | 「10」 | 「Propan-1-ol」 | 「—」 | 「Alcohol」 | 「GLOBlit_555」 |
| WM_L1_Q1_Table#2_Row#11 | 「11」 | 「1-Butyl-3-methylimidazolium bromide」 | 「—」 | 「Ionic liquid」 | 「GLOBlit_2492」 |
| WM_L1_Q1_Table#2_Row#12 | 「12」 | 「Formamide」 | 「—」 | 「Amide」 | 「GLOBlit_2834」 |
| WM_L1_Q1_Table#2_Row#13 | 「13」 | 「1,2-Ethanediol」 | 「—」 | 「Glycol」 | 「GLOBlit_2831」 |
| WM_L1_Q1_Table#2_Row#14 | 「14」 | 「Acetonitrile」 | 「—」 | 「Organic solvent」 | 「GLOBlit_2736」 |
| WM_L1_Q1_Table#2_Row#15 | 「15」 | 「N-Methyldiethanolamine」 | 「—」 | 「Alkanolamine」 | 「GLOBlit_2625」 |

##### Top 5 Literature Sources by Data Volume

**WM_L1_Q1_Table#3_(Query_L1_Q1_Answer):**

| *row_id* | *GLOBlit_N* | *DOI* | *Blocks* | *Points* |
|---|---|---|---|---|
| WM_L1_Q1_Table#3_Row#1 | 「GLOBlit_5043」 | 「10.1016/j.jct.2017.06.001」 | 「1」 | 「961」 |
| WM_L1_Q1_Table#3_Row#2 | 「GLOBlit_5201」 | 「10.1016/j.jct.2018.02.022」 | 「5」 | 「712」 |
| WM_L1_Q1_Table#3_Row#3 | 「GLOBlit_8239」 | 「10.1021/je0340755」 | 「6」 | 「675」 |
| WM_L1_Q1_Table#3_Row#4 | 「GLOBlit_10102」 | 「10.1021/je4001203」 | 「5」 | 「657」 |
| WM_L1_Q1_Table#3_Row#5 | 「GLOBlit_9821」 | 「10.1021/je300175w」 | 「7」 | 「598」 |

##### Chemistry Context

The speed-of-sound dataset for aqueous binaries is substantial (753 blocks, ~31 k points, 295 papers) and spans a wide thermodynamic window — from near-freezing temperatures up to 596.3 K and pressures up to 1,200 atm. The chemical diversity is notable: electrolytes (NaCl, KCl, KNO₃), biologically relevant solutes (amino acids, sugars), industrial solvents (DMSO, acetonitrile, glycols), alkanolamines (MDEA), ionic liquids, and surfactants are all represented. This breadth makes the dataset well-suited for validating acoustic models across different solute–water interaction regimes (hydrophobic, electrostatic, hydrogen-bonding).

Compared to density data (which typically has even larger coverage in ThermoML), speed-of-sound data is somewhat less abundant but still provides a strong validation basis, especially for deriving isentropic compressibilities and testing equation-of-state predictions in aqueous systems.

**Core claims:**
- The ThermoML database contains speed-of-sound data for aqueous binary mixtures spanning 295 distinct literature sources, 753 data blocks, and 30,819 data points.
- The dataset covers a temperature range of 273.15 – 596.3 K and a pressure range of 100.0 – 120,000.0 kPa (approximately 1 atm to 1,200 atm).
- The chemical diversity of co-solutes is broad, encompassing approximately 75–80 or more distinct non-water co-solutes including amino acids, sugars, electrolytes, organic solvents, ionic liquids, surfactants, and alkanolamines.
- This breadth of solute classes (hydrophobic, electrostatic, hydrogen-bonding interaction regimes) makes the dataset well-suited for validating acoustic models and deriving isentropic compressibilities in aqueous systems.
- Compared to density data in ThermoML, speed-of-sound data is somewhat less abundant but still provides a strong validation basis for equation-of-state predictions.

*Not stored here: 9 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.
### L1_query_2
**L1_query_2** — status: success · validation: PASS

**Summary:** Mass density (kg/m³) data for aqueous binary mixtures in ThermoML spans 1,104 literature sources, 2,558 data blocks, and 132,045 data points, covering 253.15–673.15 K and 6.3–387,800.0 kPa, with at least 79 distinct non-water co-solutes identified from a partial registry search and likely several hundred total. The top co-solutes by number of data targets are sodium chloride (57 targets), glycine (41), D-glucose (33), potassium chloride (31), ethanol (29), N-methyldiethanolamine (28), and D-sucrose (25). Co-solute classes include inorganic salts, amino acids, sugars, alcohols, alkanolamines, ionic liquids, organic acids, transition-metal salts, phosphate salts, heterocyclic compounds, phenols, and buffer compounds. Compared with speed-of-sound data for the same system type (295 sources, 753 blocks, 30,819 points, 273.15–596.3 K, 100.0–120,000 kPa), mass density is roughly 3–4 times more abundant by every metric, with a wider thermodynamic window extending ~20 K lower, ~77 K higher, and to ~3.2× higher pressure. The top five literature sources by data volume are DOI 10.1021/je200527t (2,991 points), 10.1016/j.jct.2018.05.032 (2,478), 10.1016/j.jct.2013.11.014 (2,319), 10.1016/j.jct.2008.11.006 (2,226), and 10.1016/j.jct.2004.07.019 (2,146). The disparity reflects that density is the most commonly measured thermophysical property and is routinely co-reported, whereas speed-of-sound measurements require specialized acoustic instrumentation; nonetheless the speed-of-sound dataset remains substantial for validating acoustic models, isentropic compressibility derivations, and equation-of-state predictions.

**Answer:**

#### Mass Density in Aqueous Binary Mixtures — Database Breadth Assessment

##### Aggregate Statistics

**WM_L1_Q2_Table#1_(Query_L1_Q2_Answer):**

| *row_id* | *Metric* | *Value* |
|---|---|---|
| WM_L1_Q2_Table#1_Row#1 | 「Distinct literature sources (GLOBlit_N)」 | 「**1,104**」 |
| WM_L1_Q2_Table#1_Row#2 | 「Total data blocks」 | 「**2,558**」 |
| WM_L1_Q2_Table#1_Row#3 | 「Total data points」 | 「**132,045**」 |
| WM_L1_Q2_Table#1_Row#4 | 「Temperature range」 | 「**253.15 – 673.15 K**」 |
| WM_L1_Q2_Table#1_Row#5 | 「Pressure range」 | 「**6.3 – 387,800.0 kPa** (≈ 0.06 atm to 3,830 atm)」 |
| WM_L1_Q2_Table#1_Row#6 | 「Property」 | 「Mass density (GLOBprop_1), kg/m³」 |
| WM_L1_Q2_Table#1_Row#7 | 「System type」 | 「Binary (water + one co-solute)」 |

##### Distinct Co-solute Compounds

A registry search capped at 100 blocks already returned **79 distinct non-water co-solutes**; with 2,558 total blocks the true number is likely **several hundred** distinct co-solutes — far exceeding the ~75–80 identified for speed of sound.

##### Top 10 Co-solutes by Number of Data Targets

**WM_L1_Q2_Table#2_(Query_L1_Q2_Answer):**

| *row_id* | *#* | *Co-solute* | *GLOBcomp_N* | *Chemical class* | *Targets* |
|---|---|---|---|---|---|
| WM_L1_Q2_Table#2_Row#1 | 「1」 | 「Sodium chloride」 | 「GLOBcomp_26」 | 「Inorganic salt」 | 「57」 |
| WM_L1_Q2_Table#2_Row#2 | 「2」 | 「2-Aminoacetic acid (glycine)」 | 「GLOBcomp_53」 | 「Amino acid」 | 「41」 |
| WM_L1_Q2_Table#2_Row#3 | 「3」 | 「D-Glucose」 | 「GLOBcomp_90」 | 「Sugar」 | 「33」 |
| WM_L1_Q2_Table#2_Row#4 | 「4」 | 「Potassium chloride」 | 「GLOBcomp_41」 | 「Inorganic salt」 | 「31」 |
| WM_L1_Q2_Table#2_Row#5 | 「5」 | 「Ethanol」 | 「GLOBcomp_2」 | 「Alcohol」 | 「29」 |
| WM_L1_Q2_Table#2_Row#6 | 「6」 | 「N-Methyldiethanolamine」 | 「GLOBcomp_81」 | 「Alkanolamine」 | 「28」 |
| WM_L1_Q2_Table#2_Row#7 | 「7」 | 「D-Sucrose」 | 「GLOBcomp_120」 | 「Sugar」 | 「25」 |
| WM_L1_Q2_Table#2_Row#8 | 「8」 | 「Ammonia」 | 「—」 | 「Inorganic base」 | 「≥2」 |
| WM_L1_Q2_Table#2_Row#9 | 「9」 | 「Methanol」 | 「—」 | 「Alcohol」 | 「≥4」 |
| WM_L1_Q2_Table#2_Row#10 | 「10」 | 「Propan-1-ol」 | 「—」 | 「Alcohol」 | 「≥2」 |

Additional co-solute classes identified in the registry include: ionic liquids (1-ethyl-3-methylimidazolium tetrafluoroborate, 1-butyl-3-methylimidazolium tetrafluoroborate, 1-hexyl-3-methylimidazolium tetrafluoroborate, 1-ethyl-3-methylimidazolium diethyl phosphate, 1-ethyl-3-methylimidazolium ethyl sulfate, 1,3-dimethylimidazolium chloride), organic acids (cis-1,4-butenedioic acid, 2,3-dihydroxybutanedioic acid), amino acids (4-aminobutanoic acid, L-glutamic acid hydrochloride), sugars ((+)-galactose), transition-metal salts (copper sulfate, copper dinitrate, nickel chloride), phosphate salts (disodium hydrogen phosphate, trisodium phosphate), heterocyclic compounds (1,3-dioxolane), phenols (1,3-benzenediol), and buffer compounds (2-amino-2-(hydroxymethyl)-1,3-propanediol).

##### Top 5 Literature Sources by Data Volume

**WM_L1_Q2_Table#3_(Query_L1_Q2_Answer):**

| *row_id* | *GLOBlit_N* | *DOI* | *Blocks* | *Points* |
|---|---|---|---|---|
| WM_L1_Q2_Table#3_Row#1 | 「GLOBlit_9601」 | 「10.1021/je200527t」 | 「5」 | 「2,991」 |
| WM_L1_Q2_Table#3_Row#2 | 「GLOBlit_5265」 | 「10.1016/j.jct.2018.05.032」 | 「5」 | 「2,478」 |
| WM_L1_Q2_Table#3_Row#3 | 「GLOBlit_4052」 | 「10.1016/j.jct.2013.11.014」 | 「4」 | 「2,319」 |
| WM_L1_Q2_Table#3_Row#4 | 「GLOBlit_3034」 | 「10.1016/j.jct.2008.11.006」 | 「6」 | 「2,226」 |
| WM_L1_Q2_Table#3_Row#5 | 「GLOBlit_2432」 | 「10.1016/j.jct.2004.07.019」 | 「4」 | 「2,146」 |

##### Comparison: Mass Density vs. Speed of Sound for Aqueous Binaries

**WM_L1_Q2_Table#4_(Query_L1_Q2_Answer):**

| *row_id* | *Metric* | *Mass Density (GLOBprop_1)* | *Speed of Sound (GLOBprop_8)* | *Ratio (density / SoS)* |
|---|---|---|---|---|
| WM_L1_Q2_Table#4_Row#1 | 「Literature sources」 | 「1,104」 | 「295」 | 「~3.7×」 |
| WM_L1_Q2_Table#4_Row#2 | 「Data blocks」 | 「2,558」 | 「753」 | 「~3.4×」 |
| WM_L1_Q2_Table#4_Row#3 | 「Data points」 | 「132,045」 | 「30,819」 | 「~4.3×」 |
| WM_L1_Q2_Table#4_Row#4 | 「Temperature range (K)」 | 「253.15 – 673.15」 | 「273.15 – 596.3」 | 「Wider by ~20 K low, ~77 K high」 |
| WM_L1_Q2_Table#4_Row#5 | 「Pressure range (kPa)」 | 「6.3 – 387,800」 | 「100.0 – 120,000」 | 「~3.2× wider upper bound」 |
| WM_L1_Q2_Table#4_Row#6 | 「Distinct co-solutes (lower bound)」 | 「≥79 (from 100 blocks); likely several hundred total」 | 「~75–80 (from 100 blocks)」 | 「Substantially more for density」 |

##### Chemistry Context

Mass density data for aqueous binary mixtures in ThermoML is roughly **3–4 times more abundant** than speed-of-sound data by every metric — literature sources, blocks, and data points. The thermodynamic window is also wider, extending to lower temperatures (253 K vs. 273 K), higher temperatures (673 K vs. 596 K), and much higher pressures (387,800 kPa ≈ 3,830 atm vs. 120,000 kPa ≈ 1,200 atm). The chemical diversity of co-solutes is substantially greater for density, with likely several hundred distinct non-water co-solutes across the full 2,558 blocks.

Despite this disparity, the speed-of-sound dataset (753 blocks, ~31k points, 295 papers) remains substantial and covers a broad chemical space including amino acids, sugars, electrolytes, organic solvents, ionic liquids, and alkanolamines. The ~4× gap in data volume is expected: density is the most commonly measured thermophysical property and is routinely reported alongside other measurements, whereas speed-of-sound measurements require specialized acoustic instrumentation (e.g., ultrasonic pulse-echo or sing-around techniques). Nevertheless, the speed-of-sound dataset provides a strong validation basis for acoustic models, isentropic compressibility derivations, and equation-of-state predictions in aqueous systems.

**Core claims:**
- Mass density data for aqueous binary mixtures in ThermoML encompasses 1,104 distinct literature sources, 2,558 data blocks, and 132,045 data points, spanning a temperature range of 253.15–673.15 K and a pressure range of 6.3–387,800.0 kPa.
- At least 79 distinct non-water co-solutes were identified from 100 sampled blocks, with the true number across all 2,558 blocks likely being several hundred; top co-solutes by data volume include sodium chloride (57 targets), glycine (41 targets), D-glucose (33 targets), potassium chloride (31 targets), and ethanol (29 targets).
- Co-solute chemical classes span inorganic salts, amino acids, sugars, alcohols, alkanolamines, ionic liquids, organic acids, transition-metal salts, phosphate salts, heterocyclic compounds, phenols, and buffer compounds.
- Mass density data for aqueous binaries is roughly 3–4 times more abundant than speed-of-sound data by every metric: ~3.7× in literature sources (1,104 vs. 295), ~3.4× in data blocks (2,558 vs. 753), and ~4.3× in data points (132,045 vs. 30,819).
- The thermodynamic window for mass density is wider than for speed of sound, extending to lower temperatures (253.15 K vs. 273.15 K), higher temperatures (673.15 K vs. 596.3 K), and much higher pressures (387,800 kPa vs. 120,000 kPa).
- The ~4× gap in data volume between density and speed of sound is expected because density is the most commonly measured thermophysical property and is routinely reported alongside other measurements, whereas speed-of-sound measurements require specialized acoustic instrumentation.
- Despite the disparity, the speed-of-sound dataset (753 blocks, ~31k points, 295 papers) remains substantial and covers a broad chemical space, providing a strong validation basis for acoustic models, isentropic compressibility derivations, and equation-of-state predictions in aqueous systems.

*Not stored here: 14 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.



</memory>

## User
I want to validate an acoustic model for aqueous mixtures. Is the available speed-of-sound evidence broad enough for this purpose, or is it substantially more limited than the corresponding density evidence?

## Assistant
<summary>Planning to compare the breadth of speed-of-sound (GLOBprop_8) vs. density (GLOBprop_1) data for aqueous mixtures in ThermoML. Dispatching two L1 queries to screen/rank available data for each property.</summary>
<tool_call>L1_query(instruction=Screen the databa…, id_catalog=GLOBprop_8 = Spee…, context=User wan…)</tool_call>

## User
<tool_result>
<subagent_answer>
### L1#1 — L1_query return

**Status:** status=success

**Summary:** The ThermoML database contains speed-of-sound data for aqueous binary mixtures (water + one co-solute) spanning 295 distinct literature sources, 753 data blocks, and 30,819 total data points. The temperature range covered is 273.15–596.3 K and the pressure range is 100.0–120,000.0 kPa (approximately 1 atm to 1,200 atm). Approximately 75–80 distinct non-water co-solutes are identified in a partial registry search, with the true total across all 753 blocks being larger. The chemical diversity includes amino acids (e.g., glycine, L-alanine, L-valine), sugars (D-sucrose, D-glucose), inorganic salts (NaCl, KCl, KNO₃), organic solvents (DMSO, acetonitrile), alcohols (propan-1-ol), glycols (1,2-ethanediol), amides (formamide), ionic liquids (1-butyl-3-methylimidazolium bromide), and alkanolamines (N-methyldiethanolamine). The five largest literature sources by data volume are GLOBlit_5043 (961 points), GLOBlit_5201 (712 points), GLOBlit_8239 (675 points), GLOBlit_10102 (657 points), and GLOBlit_9821 (598 points). This breadth makes the dataset suitable for validating acoustic models across different solute–water interaction regimes including hydrophobic, electrostatic, and hydrogen-bonding interactions, and for deriving isentropic compressibilities and testing equation-of-state predictions in aqueous systems.

**Answer:**

#### Speed of Sound in Aqueous Binary Mixtures — Database Breadth Assessment

##### Aggregate Statistics

**L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *Metric* | *Value* |
|---|---|---|
| L1#1_Table#1_Row#1 | 「Distinct literature sources (GLOBlit_N)」 | 「**295**」 |
| L1#1_Table#1_Row#2 | 「Total data blocks」 | 「**753**」 |
| L1#1_Table#1_Row#3 | 「Total data points」 | 「**30,819**」 |
| L1#1_Table#1_Row#4 | 「Temperature range」 | 「**273.15 – 596.3 K**」 |
| L1#1_Table#1_Row#5 | 「Pressure range」 | 「**100.0 – 120,000.0 kPa** (≈ 1 atm to 1,200 atm)」 |
| L1#1_Table#1_Row#6 | 「Property」 | 「Speed of sound (GLOBprop_8), m/s」 |
| L1#1_Table#1_Row#7 | 「System type」 | 「Binary (water + one co-solute)」 |

##### Distinct Co-solute Compounds

A registry search capped at 100 blocks already returned approximately **75–80 distinct non-water co-solutes**; the true total across all 753 blocks is larger. The database covers a remarkably diverse chemical space — amino acids, sugars, electrolytes, organic solvents, ionic liquids, surfactants, and amines.

##### Representative Co-solute Compounds (15 examples)

**L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *#* | *Co-solute* | *GLOBcomp_N* | *Chemical class* | *Example literature* |
|---|---|---|---|---|---|
| L1#1_Table#2_Row#1 | 「1」 | 「2-Aminoacetic acid (glycine)」 | 「GLOBcomp_53」 | 「Amino acid」 | 「GLOBlit_173」 |
| L1#1_Table#2_Row#2 | 「2」 | 「Sodium chloride」 | 「GLOBcomp_26」 | 「Inorganic salt」 | 「—」 |
| L1#1_Table#2_Row#3 | 「3」 | 「D-Sucrose」 | 「GLOBcomp_120」 | 「Sugar」 | 「—」 |
| L1#1_Table#2_Row#4 | 「4」 | 「D-Glucose」 | 「GLOBcomp_90」 | 「Sugar」 | 「GLOBlit_3319」 |
| L1#1_Table#2_Row#5 | 「5」 | 「Potassium chloride」 | 「GLOBcomp_41」 | 「Inorganic salt」 | 「GLOBlit_67」 |
| L1#1_Table#2_Row#6 | 「6」 | 「(S)-2-Aminopropanoic acid (L-alanine)」 | 「GLOBcomp_74」 | 「Amino acid」 | 「—」 |
| L1#1_Table#2_Row#7 | 「7」 | 「L-Valine」 | 「GLOBcomp_116」 | 「Amino acid」 | 「—」 |
| L1#1_Table#2_Row#8 | 「8」 | 「Potassium nitrate」 | 「GLOBcomp_233」 | 「Inorganic salt」 | 「GLOBlit_67」 |
| L1#1_Table#2_Row#9 | 「9」 | 「Dimethyl sulfoxide」 | 「—」 | 「Organic solvent」 | 「GLOBlit_2652」 |
| L1#1_Table#2_Row#10 | 「10」 | 「Propan-1-ol」 | 「—」 | 「Alcohol」 | 「GLOBlit_555」 |
| L1#1_Table#2_Row#11 | 「11」 | 「1-Butyl-3-methylimidazolium bromide」 | 「—」 | 「Ionic liquid」 | 「GLOBlit_2492」 |
| L1#1_Table#2_Row#12 | 「12」 | 「Formamide」 | 「—」 | 「Amide」 | 「GLOBlit_2834」 |
| L1#1_Table#2_Row#13 | 「13」 | 「1,2-Ethanediol」 | 「—」 | 「Glycol」 | 「GLOBlit_2831」 |
| L1#1_Table#2_Row#14 | 「14」 | 「Acetonitrile」 | 「—」 | 「Organic solvent」 | 「GLOBlit_2736」 |
| L1#1_Table#2_Row#15 | 「15」 | 「N-Methyldiethanolamine」 | 「—」 | 「Alkanolamine」 | 「GLOBlit_2625」 |

##### Top 5 Literature Sources by Data Volume

**L1#1_Table#3_(Query_L1#1_Answer):**

| *row_id* | *GLOBlit_N* | *DOI* | *Blocks* | *Points* |
|---|---|---|---|---|
| L1#1_Table#3_Row#1 | 「GLOBlit_5043」 | 「10.1016/j.jct.2017.06.001」 | 「1」 | 「961」 |
| L1#1_Table#3_Row#2 | 「GLOBlit_5201」 | 「10.1016/j.jct.2018.02.022」 | 「5」 | 「712」 |
| L1#1_Table#3_Row#3 | 「GLOBlit_8239」 | 「10.1021/je0340755」 | 「6」 | 「675」 |
| L1#1_Table#3_Row#4 | 「GLOBlit_10102」 | 「10.1021/je4001203」 | 「5」 | 「657」 |
| L1#1_Table#3_Row#5 | 「GLOBlit_9821」 | 「10.1021/je300175w」 | 「7」 | 「598」 |

##### Chemistry Context

The speed-of-sound dataset for aqueous binaries is substantial (753 blocks, ~31 k points, 295 papers) and spans a wide thermodynamic window — from near-freezing temperatures up to 596.3 K and pressures up to 1,200 atm. The chemical diversity is notable: electrolytes (NaCl, KCl, KNO₃), biologically relevant solutes (amino acids, sugars), industrial solvents (DMSO, acetonitrile, glycols), alkanolamines (MDEA), ionic liquids, and surfactants are all represented. This breadth makes the dataset well-suited for validating acoustic models across different solute–water interaction regimes (hydrophobic, electrostatic, hydrogen-bonding).

Compared to density data (which typically has even larger coverage in ThermoML), speed-of-sound data is somewhat less abundant but still provides a strong validation basis, especially for deriving isentropic compressibilities and testing equation-of-state predictions in aqueous systems.

**Core claims:**
- The ThermoML database contains speed-of-sound data for aqueous binary mixtures spanning 295 distinct literature sources, 753 data blocks, and 30,819 data points.
- The dataset covers a temperature range of 273.15 – 596.3 K and a pressure range of 100.0 – 120,000.0 kPa (approximately 1 atm to 1,200 atm).
- The chemical diversity of co-solutes is broad, encompassing approximately 75–80 or more distinct non-water co-solutes including amino acids, sugars, electrolytes, organic solvents, ionic liquids, surfactants, and alkanolamines.
- This breadth of solute classes (hydrophobic, electrostatic, hydrogen-bonding interaction regimes) makes the dataset well-suited for validating acoustic models and deriving isentropic compressibilities in aqueous systems.
- Compared to density data in ThermoML, speed-of-sound data is somewhat less abundant but still provides a strong validation basis for equation-of-state predictions.

**Core ID updates:**
- add GLOBprop_8 — Speed of sound, m/s (registry: speed_of_sound_m_s)
- add GLOBcomp_53 — 2-aminoacetic acid (registry: 2-aminoacetic_acid)
- add GLOBcomp_26 — sodium chloride (registry: sodium_chloride)
- add GLOBcomp_120 — D-sucrose (registry: d-sucrose)
- add GLOBcomp_90 — D-glucose (registry: d-glucose)
- add GLOBcomp_41 — potassium chloride (registry: potassium_chloride)
- add GLOBcomp_74 — (S)-2-aminopropanoic acid (registry: (s)-2-aminopropanoic_acid)
- add GLOBcomp_116 — L-valine (registry: l-valine)
- add GLOBcomp_233 — potassium nitrate (registry: potassium_nitrate)
</subagent_answer>
</tool_result>

## Assistant
<summary>Speed-of-sound data confirmed: 295 sources, 753 blocks, 30,819 points, 75–80+ co-solutes. Now dispatching L1 query for density (GLOBprop_1) in aqueous binary mixtures to enable a quantitative comparison.</summary>
<tool_call>L1_query(instruction=Screen the databa…, id_catalog=GLOBprop_1 = Mass…, context=User wan…)</tool_call>

## User
<tool_result>
<subagent_answer>
### L1#2 — L1_query return

**Status:** status=success

**Summary:** Mass density (kg/m³) data for aqueous binary mixtures in ThermoML spans 1,104 literature sources, 2,558 data blocks, and 132,045 data points, covering 253.15–673.15 K and 6.3–387,800.0 kPa, with at least 79 distinct non-water co-solutes identified from a partial registry search and likely several hundred total. The top co-solutes by number of data targets are sodium chloride (57 targets), glycine (41), D-glucose (33), potassium chloride (31), ethanol (29), N-methyldiethanolamine (28), and D-sucrose (25). Co-solute classes include inorganic salts, amino acids, sugars, alcohols, alkanolamines, ionic liquids, organic acids, transition-metal salts, phosphate salts, heterocyclic compounds, phenols, and buffer compounds. Compared with speed-of-sound data for the same system type (295 sources, 753 blocks, 30,819 points, 273.15–596.3 K, 100.0–120,000 kPa), mass density is roughly 3–4 times more abundant by every metric, with a wider thermodynamic window extending ~20 K lower, ~77 K higher, and to ~3.2× higher pressure. The top five literature sources by data volume are DOI 10.1021/je200527t (2,991 points), 10.1016/j.jct.2018.05.032 (2,478), 10.1016/j.jct.2013.11.014 (2,319), 10.1016/j.jct.2008.11.006 (2,226), and 10.1016/j.jct.2004.07.019 (2,146). The disparity reflects that density is the most commonly measured thermophysical property and is routinely co-reported, whereas speed-of-sound measurements require specialized acoustic instrumentation; nonetheless the speed-of-sound dataset remains substantial for validating acoustic models, isentropic compressibility derivations, and equation-of-state predictions.

**Answer:**

#### Mass Density in Aqueous Binary Mixtures — Database Breadth Assessment

##### Aggregate Statistics

**L1#2_Table#1_(Query_L1#2_Answer):**

| *row_id* | *Metric* | *Value* |
|---|---|---|
| L1#2_Table#1_Row#1 | 「Distinct literature sources (GLOBlit_N)」 | 「**1,104**」 |
| L1#2_Table#1_Row#2 | 「Total data blocks」 | 「**2,558**」 |
| L1#2_Table#1_Row#3 | 「Total data points」 | 「**132,045**」 |
| L1#2_Table#1_Row#4 | 「Temperature range」 | 「**253.15 – 673.15 K**」 |
| L1#2_Table#1_Row#5 | 「Pressure range」 | 「**6.3 – 387,800.0 kPa** (≈ 0.06 atm to 3,830 atm)」 |
| L1#2_Table#1_Row#6 | 「Property」 | 「Mass density (GLOBprop_1), kg/m³」 |
| L1#2_Table#1_Row#7 | 「System type」 | 「Binary (water + one co-solute)」 |

##### Distinct Co-solute Compounds

A registry search capped at 100 blocks already returned **79 distinct non-water co-solutes**; with 2,558 total blocks the true number is likely **several hundred** distinct co-solutes — far exceeding the ~75–80 identified for speed of sound.

##### Top 10 Co-solutes by Number of Data Targets

**L1#2_Table#2_(Query_L1#2_Answer):**

| *row_id* | *#* | *Co-solute* | *GLOBcomp_N* | *Chemical class* | *Targets* |
|---|---|---|---|---|---|
| L1#2_Table#2_Row#1 | 「1」 | 「Sodium chloride」 | 「GLOBcomp_26」 | 「Inorganic salt」 | 「57」 |
| L1#2_Table#2_Row#2 | 「2」 | 「2-Aminoacetic acid (glycine)」 | 「GLOBcomp_53」 | 「Amino acid」 | 「41」 |
| L1#2_Table#2_Row#3 | 「3」 | 「D-Glucose」 | 「GLOBcomp_90」 | 「Sugar」 | 「33」 |
| L1#2_Table#2_Row#4 | 「4」 | 「Potassium chloride」 | 「GLOBcomp_41」 | 「Inorganic salt」 | 「31」 |
| L1#2_Table#2_Row#5 | 「5」 | 「Ethanol」 | 「GLOBcomp_2」 | 「Alcohol」 | 「29」 |
| L1#2_Table#2_Row#6 | 「6」 | 「N-Methyldiethanolamine」 | 「GLOBcomp_81」 | 「Alkanolamine」 | 「28」 |
| L1#2_Table#2_Row#7 | 「7」 | 「D-Sucrose」 | 「GLOBcomp_120」 | 「Sugar」 | 「25」 |
| L1#2_Table#2_Row#8 | 「8」 | 「Ammonia」 | 「—」 | 「Inorganic base」 | 「≥2」 |
| L1#2_Table#2_Row#9 | 「9」 | 「Methanol」 | 「—」 | 「Alcohol」 | 「≥4」 |
| L1#2_Table#2_Row#10 | 「10」 | 「Propan-1-ol」 | 「—」 | 「Alcohol」 | 「≥2」 |

Additional co-solute classes identified in the registry include: ionic liquids (1-ethyl-3-methylimidazolium tetrafluoroborate, 1-butyl-3-methylimidazolium tetrafluoroborate, 1-hexyl-3-methylimidazolium tetrafluoroborate, 1-ethyl-3-methylimidazolium diethyl phosphate, 1-ethyl-3-methylimidazolium ethyl sulfate, 1,3-dimethylimidazolium chloride), organic acids (cis-1,4-butenedioic acid, 2,3-dihydroxybutanedioic acid), amino acids (4-aminobutanoic acid, L-glutamic acid hydrochloride), sugars ((+)-galactose), transition-metal salts (copper sulfate, copper dinitrate, nickel chloride), phosphate salts (disodium hydrogen phosphate, trisodium phosphate), heterocyclic compounds (1,3-dioxolane), phenols (1,3-benzenediol), and buffer compounds (2-amino-2-(hydroxymethyl)-1,3-propanediol).

##### Top 5 Literature Sources by Data Volume

**L1#2_Table#3_(Query_L1#2_Answer):**

| *row_id* | *GLOBlit_N* | *DOI* | *Blocks* | *Points* |
|---|---|---|---|---|
| L1#2_Table#3_Row#1 | 「GLOBlit_9601」 | 「10.1021/je200527t」 | 「5」 | 「2,991」 |
| L1#2_Table#3_Row#2 | 「GLOBlit_5265」 | 「10.1016/j.jct.2018.05.032」 | 「5」 | 「2,478」 |
| L1#2_Table#3_Row#3 | 「GLOBlit_4052」 | 「10.1016/j.jct.2013.11.014」 | 「4」 | 「2,319」 |
| L1#2_Table#3_Row#4 | 「GLOBlit_3034」 | 「10.1016/j.jct.2008.11.006」 | 「6」 | 「2,226」 |
| L1#2_Table#3_Row#5 | 「GLOBlit_2432」 | 「10.1016/j.jct.2004.07.019」 | 「4」 | 「2,146」 |

##### Comparison: Mass Density vs. Speed of Sound for Aqueous Binaries

**L1#2_Table#4_(Query_L1#2_Answer):**

| *row_id* | *Metric* | *Mass Density (GLOBprop_1)* | *Speed of Sound (GLOBprop_8)* | *Ratio (density / SoS)* |
|---|---|---|---|---|
| L1#2_Table#4_Row#1 | 「Literature sources」 | 「1,104」 | 「295」 | 「~3.7×」 |
| L1#2_Table#4_Row#2 | 「Data blocks」 | 「2,558」 | 「753」 | 「~3.4×」 |
| L1#2_Table#4_Row#3 | 「Data points」 | 「132,045」 | 「30,819」 | 「~4.3×」 |
| L1#2_Table#4_Row#4 | 「Temperature range (K)」 | 「253.15 – 673.15」 | 「273.15 – 596.3」 | 「Wider by ~20 K low, ~77 K high」 |
| L1#2_Table#4_Row#5 | 「Pressure range (kPa)」 | 「6.3 – 387,800」 | 「100.0 – 120,000」 | 「~3.2× wider upper bound」 |
| L1#2_Table#4_Row#6 | 「Distinct co-solutes (lower bound)」 | 「≥79 (from 100 blocks); likely several hundred total」 | 「~75–80 (from 100 blocks)」 | 「Substantially more for density」 |

##### Chemistry Context

Mass density data for aqueous binary mixtures in ThermoML is roughly **3–4 times more abundant** than speed-of-sound data by every metric — literature sources, blocks, and data points. The thermodynamic window is also wider, extending to lower temperatures (253 K vs. 273 K), higher temperatures (673 K vs. 596 K), and much higher pressures (387,800 kPa ≈ 3,830 atm vs. 120,000 kPa ≈ 1,200 atm). The chemical diversity of co-solutes is substantially greater for density, with likely several hundred distinct non-water co-solutes across the full 2,558 blocks.

Despite this disparity, the speed-of-sound dataset (753 blocks, ~31k points, 295 papers) remains substantial and covers a broad chemical space including amino acids, sugars, electrolytes, organic solvents, ionic liquids, and alkanolamines. The ~4× gap in data volume is expected: density is the most commonly measured thermophysical property and is routinely reported alongside other measurements, whereas speed-of-sound measurements require specialized acoustic instrumentation (e.g., ultrasonic pulse-echo or sing-around techniques). Nevertheless, the speed-of-sound dataset provides a strong validation basis for acoustic models, isentropic compressibility derivations, and equation-of-state predictions in aqueous systems.

**Core claims:**
- Mass density data for aqueous binary mixtures in ThermoML encompasses 1,104 distinct literature sources, 2,558 data blocks, and 132,045 data points, spanning a temperature range of 253.15–673.15 K and a pressure range of 6.3–387,800.0 kPa.
- At least 79 distinct non-water co-solutes were identified from 100 sampled blocks, with the true number across all 2,558 blocks likely being several hundred; top co-solutes by data volume include sodium chloride (57 targets), glycine (41 targets), D-glucose (33 targets), potassium chloride (31 targets), and ethanol (29 targets).
- Co-solute chemical classes span inorganic salts, amino acids, sugars, alcohols, alkanolamines, ionic liquids, organic acids, transition-metal salts, phosphate salts, heterocyclic compounds, phenols, and buffer compounds.
- Mass density data for aqueous binaries is roughly 3–4 times more abundant than speed-of-sound data by every metric: ~3.7× in literature sources (1,104 vs. 295), ~3.4× in data blocks (2,558 vs. 753), and ~4.3× in data points (132,045 vs. 30,819).
- The thermodynamic window for mass density is wider than for speed of sound, extending to lower temperatures (253.15 K vs. 273.15 K), higher temperatures (673.15 K vs. 596.3 K), and much higher pressures (387,800 kPa vs. 120,000 kPa).
- The ~4× gap in data volume between density and speed of sound is expected because density is the most commonly measured thermophysical property and is routinely reported alongside other measurements, whereas speed-of-sound measurements require specialized acoustic instrumentation.
- Despite the disparity, the speed-of-sound dataset (753 blocks, ~31k points, 295 papers) remains substantial and covers a broad chemical space, providing a strong validation basis for acoustic models, isentropic compressibility derivations, and equation-of-state predictions in aqueous systems.

**Core ID updates:**
- add GLOBprop_1 — Mass density, kg/m3 (registry: mass_density_kg_m3)
- add GLOBprop_8 — Speed of sound, m/s (registry: speed_of_sound_m_s)
- add GLOBcomp_26 — sodium chloride (registry: sodium_chloride)
- add GLOBcomp_53 — 2-aminoacetic acid (registry: 2-aminoacetic_acid)
- add GLOBcomp_90 — D-glucose (registry: d-glucose)
- add GLOBcomp_41 — potassium chloride (registry: potassium_chloride)
- add GLOBcomp_2 — ethanol (registry: ethanol)
- add GLOBcomp_81 — N-methyldiethanolamine (registry: n-methyldiethanolamine)
- add GLOBcomp_120 — D-sucrose (registry: d-sucrose)
- add GLOBlit_9601 — 10.1021/je200527t (registry: 2011-sim-cib-0)
- add GLOBlit_5265 — 10.1016/j.jct.2018.05.032 (registry: 2018-cib--0)
- add GLOBlit_4052 — 10.1016/j.jct.2013.11.014 (registry: 2014-cib--0)
- add GLOBlit_3034 — 10.1016/j.jct.2008.11.006 (registry: 2009-cib-hne-1)
- add GLOBlit_2432 — 10.1016/j.jct.2004.07.019 (registry: 2004-hyn-hne-0)
</subagent_answer>
</tool_result>

## LLM Response
<reasoning>
I now have all the data needed to provide a comprehensive answer comparing speed-of-sound vs. density data breadth for aqueous mixtures in ThermoML. Both queries returned successfully with detailed statistics. Let me compose the final answer.
</reasoning>

<answer>

## Speed-of-Sound Evidence for Aqueous Mixtures: Breadth Assessment & Comparison with Density

### Short answer

The speed-of-sound dataset in the ThermoML database is **substantial and chemically diverse enough** to validate an acoustic model for aqueous mixtures — but it is **roughly 3–4 × smaller** than the corresponding mass-density dataset by every metric.

---

### Head-to-head comparison

| Metric | Speed of Sound | Mass Density | Ratio (ρ / u) |
|--------|---------------|-------------|----------------|
| Literature sources | 295 | 1,104 | ~3.7× |
| Data blocks | 753 | 2,558 | ~3.4× |
| Data points | 30,819 | 132,045 | ~4.3× |
| Temperature range | 273.15 – 596.3 K | 253.15 – 673.15 K | Density extends ~20 K lower, ~77 K higher |
| Pressure range | 100.0 – 120,000 kPa (≈1–1,200 atm) | 6.3 – 387,800 kPa (≈0.06–3,830 atm) | Density reaches ~3.2× higher pressure |
| Distinct co-solutes (lower bound from 100-block sample) | ~75–80 | ≥79 (likely several hundred total) | Density has substantially more |

---

### Chemical diversity of the speed-of-sound dataset

Even though it is smaller, the speed-of-sound dataset covers a remarkably broad chemical space of co-solutes dissolved in water:

| # | Co-solute | Class |
|---|-----------|-------|
| 1 | Glycine (2-aminoacetic acid) | Amino acid |
| 2 | L-Alanine | Amino acid |
| 3 | L-Valine | Amino acid |
| 4 | Sodium chloride | Inorganic salt |
| 5 | Potassium chloride | Inorganic salt |
| 6 | Potassium nitrate | Inorganic salt |
| 7 | D-Sucrose | Sugar |
| 8 | D-Glucose | Sugar |
| 9 | Dimethyl sulfoxide | Organic solvent |
| 10 | Acetonitrile | Organic solvent |
| 11 | Propan-1-ol | Alcohol |
| 12 | 1,2-Ethanediol | Glycol |
| 13 | Formamide | Amide |
| 14 | 1-Butyl-3-methylimidazolium bromide | Ionic liquid |
| 15 | N-Methyldiethanolamine | Alkanolamine |

This spans the key solute–water interaction regimes relevant to acoustic modelling: **electrostatic** (salts), **hydrogen-bonding** (sugars, amino acids, glycols, amides), and **hydrophobic** (organic solvents, ionic-liquid cations, alkanolamine alkyl chains).

---

### Largest speed-of-sound literature sources

| GLOBlit_N | DOI | Blocks | Points |
|-----------|-----|--------|--------|
| GLOBlit_5043 | 10.1016/j.jct.2017.06.001 | 1 | 961 |
| GLOBlit_5201 | 10.1016/j.jct.2018.02.022 | 5 | 712 |
| GLOBlit_8239 | 10.1021/je0340755 | 6 | 675 |
| GLOBlit_10102 | 10.1021/je4001203 | 5 | 657 |
| GLOBlit_9821 | 10.1021/je300175w | 7 | 598 |

---

### Interpretation

1. **The speed-of-sound evidence is broad enough for acoustic-model validation.** With ~31,000 data points across 295 independent literature sources, 753 data blocks, and at least 75–80 chemically distinct co-solutes, you have ample data to test predictions of sound velocity, derive isentropic compressibilities (κ_S = 1/(ρu²)), and benchmark equation-of-state performance across multiple solute classes.

2. **It is, however, substantially more limited than density evidence.** Density data is ~3.7× richer in sources, ~3.4× richer in blocks, and ~4.3× richer in data points. The thermodynamic window for density also extends to lower temperatures (253 K vs. 273 K), higher temperatures (673 K vs. 596 K), and much higher pressures (387,800 kPa vs. 120,000 kPa). The number of distinct co-solutes is also considerably larger for density.

3. **The gap is expected and well understood.** Mass density is the single most commonly measured thermophysical property — it is routinely co-reported with nearly every other measurement because it is needed for unit conversions (e.g., molarity ↔ molality). Speed-of-sound measurements, by contrast, require specialized acoustic instrumentation (ultrasonic pulse-echo, sing-around, or interferometric techniques), which limits the number of laboratories and publications reporting such data.

4. **Practical recommendation.** For model validation, the speed-of-sound dataset is sufficient to cover the major interaction regimes and a wide T–p window. Where you may find gaps is at extreme conditions (T > 596 K, p > 1,200 atm) and for more exotic co-solutes — in those regions, density data will be available but speed-of-sound data may not. You could use the density data as a complementary validation channel (e.g., checking that your model simultaneously reproduces both ρ and u) and reserve the speed-of-sound data for the acoustic-specific validation.

</answer>