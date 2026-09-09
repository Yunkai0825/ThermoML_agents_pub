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
| comp | GLOBcomp_24 | 1,2-ethanediol | 1,2-ethanediol |
| comp | GLOBcomp_1 | water | water |
| comp | GLOBcomp_61 | 1,2-propanediol | 1,2-propanediol |
| comp | GLOBcomp_111 | diethylene_glycol | diethylene glycol |
| comp | GLOBcomp_113 | triethylene_glycol | triethylene glycol |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|
| lit | GLOBlit_5201 | 2018-hog-tor-0 | 10.1016/j.jct.2018.02.022 |
| lit | GLOBlit_10102 | 2013-hne-cib-1 | 10.1021/je4001203 |
| lit | GLOBlit_8038 | 2003-yan-ma-2 | 10.1021/je020140j |
| lit | GLOBlit_6951 | 2017-moo-ros-0 | 10.1021/acs.jced.6b00526 |
| lit | GLOBlit_1283 | 2013-zem-tro-0 | 10.1016/j.fluid.2013.06.041 |
| lit | GLOBlit_8239 | 2003-geo-sas-1 | 10.1021/je0340755 |
| lit | GLOBlit_7545 | 2018-mik-sko-0 | 10.1021/acs.jced.8b00403 |
| lit | GLOBlit_9758 | 2012-kat-hne-0 | 10.1021/je201184b |
| lit | GLOBlit_1623 | 2015-cha-hsi-0 | 10.1016/j.fluid.2014.12.040 |
| lit | GLOBlit_4754 | 2017-cib--1 | 10.1016/j.jct.2016.07.016 |
| lit | GLOBlit_11031 | 2008-man-guz-0 | 10.1021/je700672f |
| lit | GLOBlit_9382 | 2011-beg-cla-0 | 10.1021/je1009976 |
| lit | GLOBlit_6630 | 2016-cib--0 | 10.1021/acs.jced.5b00498 |
| lit | GLOBlit_1753 | 2015-ani-sin-0 | 10.1016/j.fluid.2015.07.030 |
| lit | GLOBlit_4395 | 2015-kli-str-1 | 10.1016/j.jct.2015.05.024 |

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find all available data for glycol + water mixtures in ThermoML → stored as L1_query_1 · validation: PASS

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: PASS

**Summary:** The ThermoML database contains extensive binary mixture data for four glycol + water systems, totaling 161 property blocks across 81 literature sources (with some shared across systems) and 10,081 data points. Ethylene glycol (GLOBcomp_24) + water (GLOBcomp_1) has 59 blocks, 32 papers, 2,584 points, spanning 258.32–573.23 K and 50.0–350,200.0 kPa. Propylene glycol (GLOBcomp_61) + water has 34 blocks, 18 papers, 1,780 points, spanning 253.15–573.19 K and 100.0–350,000.0 kPa. Diethylene glycol (GLOBcomp_111) + water has 28 blocks, 15 papers, 2,079 points, spanning 278.15–573.184 K and 50.0–30,500.0 kPa. Triethylene glycol (GLOBcomp_113) + water has 40 blocks, 16 papers, 3,638 points, spanning 278.15–573.183 K and 50.0–30,510.0 kPa. Mass density is the most commonly measured property across all four systems (46 blocks total), followed by speed of sound and viscosity. Triethylene glycol + water has the largest dataset, driven largely by a single study (DOI 10.1016/j.fluid.2015.07.030, GLOBlit_1753) contributing 1,370 points across 12 blocks. Ethylene glycol + water has the broadest literature coverage. All four systems reach similar upper temperatures (~573 K), but ethylene glycol and propylene glycol systems extend to higher pressures (~350 MPa). Transport properties and excess thermodynamic properties are available but less common than volumetric and acoustic properties.

**Answer:**

#### Glycol + Water Binary Mixture Data in ThermoML — Comprehensive Overview

The ThermoML database contains extensive data for four glycol + water binary systems, totaling **161 property blocks** across **81 literature sources** (some shared across systems) with **10,081 data points**.

---

##### 1. Ethylene Glycol (1,2-Ethanediol) + Water

- **Compound IDs:** GLOBcomp_24 + GLOBcomp_1
- **Coverage:** 59 blocks, 32 papers, 2,584 data points
- **Temperature range:** 258.32 – 573.23 K
- **Pressure range:** 50.0 – 350,200.0 kPa

**Properties measured (blocks):**

**WM_L1_Q1_Table#1_(Query_L1_Q1_Answer):**

| *row_id* | *Property* | *Blocks* |
|---|---|---|
| WM_L1_Q1_Table#1_Row#1 | 「Mass density, kg/m³」 | 「16」 |
| WM_L1_Q1_Table#1_Row#2 | 「Speed of sound, m/s」 | 「8」 |
| WM_L1_Q1_Table#1_Row#3 | 「Viscosity, Pa·s」 | 「7」 |
| WM_L1_Q1_Table#1_Row#4 | 「Binary diffusion coefficient, m²/s」 | 「5」 |
| WM_L1_Q1_Table#1_Row#5 | 「Surface tension liquid-gas, N/m」 | 「4」 |
| WM_L1_Q1_Table#1_Row#6 | 「Vapor or sublimation pressure, kPa」 | 「3」 |
| WM_L1_Q1_Table#1_Row#7 | 「Boiling temperature at pressure P, K」 | 「3」 |
| WM_L1_Q1_Table#1_Row#8 | 「Mole fraction」 | 「2」 |
| WM_L1_Q1_Table#1_Row#9 | 「Refractive index (Na D-line)」 | 「2」 |
| WM_L1_Q1_Table#1_Row#10 | 「Specific volume, m³/kg」 | 「2」 |

**Top literature sources:**

**WM_L1_Q1_Table#2_(Query_L1_Q1_Answer):**

| *row_id* | *DOI* | *Blocks* | *Points* |
|---|---|---|---|
| WM_L1_Q1_Table#2_Row#1 | 「10.1016/j.jct.2018.02.022 (GLOBlit_5201)」 | 「3」 | 「456」 |
| WM_L1_Q1_Table#2_Row#2 | 「10.1021/je4001203 (GLOBlit_10102)」 | 「2」 | 「276」 |
| WM_L1_Q1_Table#2_Row#3 | 「10.1021/je020140j (GLOBlit_8038)」 | 「3」 | 「249」 |
| WM_L1_Q1_Table#2_Row#4 | 「10.1021/acs.jced.6b00526 (GLOBlit_6951)」 | 「3」 | 「236」 |
| WM_L1_Q1_Table#2_Row#5 | 「10.1016/j.fluid.2013.06.041 (GLOBlit_1283)」 | 「2」 | 「214」 |

---

##### 2. Propylene Glycol (1,2-Propanediol) + Water

- **Compound IDs:** GLOBcomp_61 + GLOBcomp_1
- **Coverage:** 34 blocks, 18 papers, 1,780 data points
- **Temperature range:** 253.15 – 573.19 K
- **Pressure range:** 100.0 – 350,000.0 kPa

**Properties measured (blocks):**

**WM_L1_Q1_Table#3_(Query_L1_Q1_Answer):**

| *row_id* | *Property* | *Blocks* |
|---|---|---|
| WM_L1_Q1_Table#3_Row#1 | 「Mass density, kg/m³」 | 「10」 |
| WM_L1_Q1_Table#3_Row#2 | 「Speed of sound, m/s」 | 「4」 |
| WM_L1_Q1_Table#3_Row#3 | 「Viscosity, Pa·s」 | 「4」 |
| WM_L1_Q1_Table#3_Row#4 | 「Excess molar volume, m³/mol」 | 「2」 |
| WM_L1_Q1_Table#3_Row#5 | 「Molar heat capacity at constant pressure, J/K/mol」 | 「2」 |
| WM_L1_Q1_Table#3_Row#6 | 「Thermal conductivity, W/m/K」 | 「2」 |
| WM_L1_Q1_Table#3_Row#7 | 「Specific volume, m³/kg」 | 「2」 |
| WM_L1_Q1_Table#3_Row#8 | 「Excess molar heat capacity, J/K/mol」 | 「1」 |
| WM_L1_Q1_Table#3_Row#9 | 「Surface tension liquid-gas, N/m」 | 「1」 |
| WM_L1_Q1_Table#3_Row#10 | 「Excess molar enthalpy (molar enthalpy of mixing), kJ/mol」 | 「1」 |

**Top literature sources:**

**WM_L1_Q1_Table#4_(Query_L1_Q1_Answer):**

| *row_id* | *DOI* | *Blocks* | *Points* |
|---|---|---|---|
| WM_L1_Q1_Table#4_Row#1 | 「10.1021/je0340755 (GLOBlit_8239)」 | 「3」 | 「375」 |
| WM_L1_Q1_Table#4_Row#2 | 「10.1021/acs.jced.8b00403 (GLOBlit_7545)」 | 「3」 | 「291」 |
| WM_L1_Q1_Table#4_Row#3 | 「10.1021/je201184b (GLOBlit_9758)」 | 「2」 | 「212」 |
| WM_L1_Q1_Table#4_Row#4 | 「10.1016/j.fluid.2013.06.041 (GLOBlit_1283)」 | 「2」 | 「185」 |
| WM_L1_Q1_Table#4_Row#5 | 「10.1016/j.fluid.2014.12.040 (GLOBlit_1623)」 | 「2」 | 「168」 |

---

##### 3. Diethylene Glycol + Water

- **Compound IDs:** GLOBcomp_111 + GLOBcomp_1
- **Coverage:** 28 blocks, 15 papers, 2,079 data points
- **Temperature range:** 278.15 – 573.184 K
- **Pressure range:** 50.0 – 30,500.0 kPa

**Properties measured (blocks):**

**WM_L1_Q1_Table#5_(Query_L1_Q1_Answer):**

| *row_id* | *Property* | *Blocks* |
|---|---|---|
| WM_L1_Q1_Table#5_Row#1 | 「Mass density, kg/m³」 | 「10」 |
| WM_L1_Q1_Table#5_Row#2 | 「Speed of sound, m/s」 | 「6」 |
| WM_L1_Q1_Table#5_Row#3 | 「Viscosity, Pa·s」 | 「4」 |
| WM_L1_Q1_Table#5_Row#4 | 「Binary diffusion coefficient, m²/s」 | 「2」 |
| WM_L1_Q1_Table#5_Row#5 | 「Excess molar enthalpy (molar enthalpy of mixing), kJ/mol」 | 「2」 |
| WM_L1_Q1_Table#5_Row#6 | 「Molar heat capacity at constant pressure, J/K/mol」 | 「1」 |
| WM_L1_Q1_Table#5_Row#7 | 「Boiling temperature at pressure P, K」 | 「1」 |
| WM_L1_Q1_Table#5_Row#8 | 「Refractive index (Na D-line)」 | 「1」 |
| WM_L1_Q1_Table#5_Row#9 | 「Thermal conductivity, W/m/K」 | 「1」 |

**Top literature sources:**

**WM_L1_Q1_Table#6_(Query_L1_Q1_Answer):**

| *row_id* | *DOI* | *Blocks* | *Points* |
|---|---|---|---|
| WM_L1_Q1_Table#6_Row#1 | 「10.1016/j.jct.2016.07.016 (GLOBlit_4754)」 | 「1」 | 「588」 |
| WM_L1_Q1_Table#6_Row#2 | 「10.1016/j.jct.2018.02.022 (GLOBlit_5201)」 | 「3」 | 「456」 |
| WM_L1_Q1_Table#6_Row#3 | 「10.1021/je700672f (GLOBlit_11031)」 | 「2」 | 「286」 |
| WM_L1_Q1_Table#6_Row#4 | 「10.1021/je1009976 (GLOBlit_9382)」 | 「2」 | 「170」 |
| WM_L1_Q1_Table#6_Row#5 | 「10.1021/acs.jced.5b00498 (GLOBlit_6630)」 | 「2」 | 「140」 |

---

##### 4. Triethylene Glycol + Water

- **Compound IDs:** GLOBcomp_113 + GLOBcomp_1
- **Coverage:** 40 blocks, 16 papers, 3,638 data points
- **Temperature range:** 278.15 – 573.183 K
- **Pressure range:** 50.0 – 30,510.0 kPa

**Properties measured (blocks):**

**WM_L1_Q1_Table#7_(Query_L1_Q1_Answer):**

| *row_id* | *Property* | *Blocks* |
|---|---|---|
| WM_L1_Q1_Table#7_Row#1 | 「Mass density, kg/m³」 | 「10」 |
| WM_L1_Q1_Table#7_Row#2 | 「Refractive index (other wavelength)」 | 「9」 |
| WM_L1_Q1_Table#7_Row#3 | 「Speed of sound, m/s」 | 「6」 |
| WM_L1_Q1_Table#7_Row#4 | 「Boiling temperature at pressure P, K」 | 「3」 |
| WM_L1_Q1_Table#7_Row#5 | 「Viscosity, Pa·s」 | 「3」 |
| WM_L1_Q1_Table#7_Row#6 | 「Binary diffusion coefficient, m²/s」 | 「2」 |
| WM_L1_Q1_Table#7_Row#7 | 「Mole fraction」 | 「2」 |
| WM_L1_Q1_Table#7_Row#8 | 「Joule-Thomson coefficient, K/kPa」 | 「1」 |
| WM_L1_Q1_Table#7_Row#9 | 「Molar heat capacity at constant pressure, J/K/mol」 | 「1」 |
| WM_L1_Q1_Table#7_Row#10 | 「Excess molar enthalpy (molar enthalpy of mixing), kJ/mol」 | 「1」 |

**Top literature sources:**

**WM_L1_Q1_Table#8_(Query_L1_Q1_Answer):**

| *row_id* | *DOI* | *Blocks* | *Points* |
|---|---|---|---|
| WM_L1_Q1_Table#8_Row#1 | 「10.1016/j.fluid.2015.07.030 (GLOBlit_1753)」 | 「12」 | 「1370」 |
| WM_L1_Q1_Table#8_Row#2 | 「10.1016/j.jct.2015.05.024 (GLOBlit_4395)」 | 「2」 | 「667」 |
| WM_L1_Q1_Table#8_Row#3 | 「10.1016/j.jct.2016.07.016 (GLOBlit_4754)」 | 「1」 | 「598」 |
| WM_L1_Q1_Table#8_Row#4 | 「10.1016/j.jct.2018.02.022 (GLOBlit_5201)」 | 「3」 | 「432」 |
| WM_L1_Q1_Table#8_Row#5 | 「10.1021/acs.jced.5b00498 (GLOBlit_6630)」 | 「2」 | 「140」 |

---

##### Cross-System Summary

**WM_L1_Q1_Table#9_(Query_L1_Q1_Answer):**

| *row_id* | *Glycol + Water System* | *Blocks* | *Papers* | *Data Points* | *T range (K)* | *P range (kPa)* |
|---|---|---|---|---|---|---|
| WM_L1_Q1_Table#9_Row#1 | 「Ethylene glycol」 | 「59」 | 「32」 | 「2,584」 | 「258.32 – 573.23」 | 「50.0 – 350,200.0」 |
| WM_L1_Q1_Table#9_Row#2 | 「Propylene glycol」 | 「34」 | 「18」 | 「1,780」 | 「253.15 – 573.19」 | 「100.0 – 350,000.0」 |
| WM_L1_Q1_Table#9_Row#3 | 「Diethylene glycol」 | 「28」 | 「15」 | 「2,079」 | 「278.15 – 573.184」 | 「50.0 – 30,500.0」 |
| WM_L1_Q1_Table#9_Row#4 | 「Triethylene glycol」 | 「40」 | 「16」 | 「3,638」 | 「278.15 – 573.183」 | 「50.0 – 30,510.0」 |
| WM_L1_Q1_Table#9_Row#5 | 「**Total**」 | 「**161**」 | 「**81***」 | 「**10,081**」 | 「—」 | 「—」 |

*Some papers appear in multiple systems (e.g., GLOBlit_5201 and GLOBlit_1283 cover multiple glycol systems), so the unique paper count is lower.

##### Key Observations

- **Mass density** is the most commonly measured property across all four systems (46 blocks total), reflecting its importance for engineering applications of glycol-water heat transfer fluids and antifreeze formulations.
- **Speed of sound** and **viscosity** are the next most common, each appearing in all four systems.
- **Triethylene glycol + water** has the largest dataset (3,638 points), driven largely by a single comprehensive study (GLOBlit_1753, DOI: 10.1016/j.fluid.2015.07.030) contributing 1,370 points across 12 blocks.
- **Ethylene glycol + water** has the broadest literature coverage (32 papers), consistent with its widespread industrial use as an antifreeze and coolant.
- All four systems span similar upper temperature ranges (~573 K), but ethylene glycol and propylene glycol systems extend to higher pressures (up to ~350 MPa), likely from high-pressure density studies.
- Transport properties (diffusion coefficients, thermal conductivity) and excess thermodynamic properties (excess molar enthalpy, excess molar volume) are available but less common than volumetric and acoustic properties.

**Core claims:**
- The ThermoML database contains data for four glycol + water binary systems (ethylene glycol, propylene glycol, diethylene glycol, triethylene glycol), totaling 161 property blocks across 81 literature sources (some shared across systems) with 10,081 data points.
- Ethylene glycol + water has the broadest literature coverage (59 blocks, 32 papers, 2,584 data points), spanning 258.32 – 573.23 K and 50.0 – 350,200.0 kPa.
- Propylene glycol + water covers 34 blocks, 18 papers, and 1,780 data points, spanning 253.15 – 573.19 K and 100.0 – 350,000.0 kPa.
- Diethylene glycol + water covers 28 blocks, 15 papers, and 2,079 data points, spanning 278.15 – 573.184 K and 50.0 – 30,500.0 kPa.
- Triethylene glycol + water has the largest dataset (40 blocks, 16 papers, 3,638 data points), spanning 278.15 – 573.183 K and 50.0 – 30,510.0 kPa, driven largely by a single study (DOI: 10.1016/j.fluid.2015.07.030) contributing 1,370 points across 12 blocks.
- Mass density is the most commonly measured property across all four systems (46 blocks total), followed by speed of sound and viscosity, each appearing in all four systems.
- Ethylene glycol and propylene glycol systems extend to higher pressures (up to ~350 MPa), likely from high-pressure density studies, while all four systems span similar upper temperature ranges (~573 K).
- Transport properties (diffusion coefficients, thermal conductivity) and excess thermodynamic properties (excess molar enthalpy, excess molar volume) are available but less common than volumetric and acoustic properties.

*Not stored here: 20 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.



</memory>

## User
What data is available for glycol + water mixtures?

## Assistant
<summary>Dispatching L1 query to search for glycol + water mixture data in ThermoML database, covering common glycols (ethylene glycol, propylene glycol, diethylene glycol, etc.).</summary>
<tool_call>L1_query(instruction=Search for binary…, id_catalog=, context=User wants a broa…)</tool_call>

## User
<tool_result>
<subagent_answer>
### L1#1 — L1_query return

**Status:** status=success

**Summary:** The ThermoML database contains extensive binary mixture data for four glycol + water systems, totaling 161 property blocks across 81 literature sources (with some shared across systems) and 10,081 data points. Ethylene glycol (GLOBcomp_24) + water (GLOBcomp_1) has 59 blocks, 32 papers, 2,584 points, spanning 258.32–573.23 K and 50.0–350,200.0 kPa. Propylene glycol (GLOBcomp_61) + water has 34 blocks, 18 papers, 1,780 points, spanning 253.15–573.19 K and 100.0–350,000.0 kPa. Diethylene glycol (GLOBcomp_111) + water has 28 blocks, 15 papers, 2,079 points, spanning 278.15–573.184 K and 50.0–30,500.0 kPa. Triethylene glycol (GLOBcomp_113) + water has 40 blocks, 16 papers, 3,638 points, spanning 278.15–573.183 K and 50.0–30,510.0 kPa. Mass density is the most commonly measured property across all four systems (46 blocks total), followed by speed of sound and viscosity. Triethylene glycol + water has the largest dataset, driven largely by a single study (DOI 10.1016/j.fluid.2015.07.030, GLOBlit_1753) contributing 1,370 points across 12 blocks. Ethylene glycol + water has the broadest literature coverage. All four systems reach similar upper temperatures (~573 K), but ethylene glycol and propylene glycol systems extend to higher pressures (~350 MPa). Transport properties and excess thermodynamic properties are available but less common than volumetric and acoustic properties.

**Answer:**

#### Glycol + Water Binary Mixture Data in ThermoML — Comprehensive Overview

The ThermoML database contains extensive data for four glycol + water binary systems, totaling **161 property blocks** across **81 literature sources** (some shared across systems) with **10,081 data points**.

---

##### 1. Ethylene Glycol (1,2-Ethanediol) + Water

- **Compound IDs:** GLOBcomp_24 + GLOBcomp_1
- **Coverage:** 59 blocks, 32 papers, 2,584 data points
- **Temperature range:** 258.32 – 573.23 K
- **Pressure range:** 50.0 – 350,200.0 kPa

**Properties measured (blocks):**

**L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *Property* | *Blocks* |
|---|---|---|
| L1#1_Table#1_Row#1 | 「Mass density, kg/m³」 | 「16」 |
| L1#1_Table#1_Row#2 | 「Speed of sound, m/s」 | 「8」 |
| L1#1_Table#1_Row#3 | 「Viscosity, Pa·s」 | 「7」 |
| L1#1_Table#1_Row#4 | 「Binary diffusion coefficient, m²/s」 | 「5」 |
| L1#1_Table#1_Row#5 | 「Surface tension liquid-gas, N/m」 | 「4」 |
| L1#1_Table#1_Row#6 | 「Vapor or sublimation pressure, kPa」 | 「3」 |
| L1#1_Table#1_Row#7 | 「Boiling temperature at pressure P, K」 | 「3」 |
| L1#1_Table#1_Row#8 | 「Mole fraction」 | 「2」 |
| L1#1_Table#1_Row#9 | 「Refractive index (Na D-line)」 | 「2」 |
| L1#1_Table#1_Row#10 | 「Specific volume, m³/kg」 | 「2」 |

**Top literature sources:**

**L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *DOI* | *Blocks* | *Points* |
|---|---|---|---|
| L1#1_Table#2_Row#1 | 「10.1016/j.jct.2018.02.022 (GLOBlit_5201)」 | 「3」 | 「456」 |
| L1#1_Table#2_Row#2 | 「10.1021/je4001203 (GLOBlit_10102)」 | 「2」 | 「276」 |
| L1#1_Table#2_Row#3 | 「10.1021/je020140j (GLOBlit_8038)」 | 「3」 | 「249」 |
| L1#1_Table#2_Row#4 | 「10.1021/acs.jced.6b00526 (GLOBlit_6951)」 | 「3」 | 「236」 |
| L1#1_Table#2_Row#5 | 「10.1016/j.fluid.2013.06.041 (GLOBlit_1283)」 | 「2」 | 「214」 |

---

##### 2. Propylene Glycol (1,2-Propanediol) + Water

- **Compound IDs:** GLOBcomp_61 + GLOBcomp_1
- **Coverage:** 34 blocks, 18 papers, 1,780 data points
- **Temperature range:** 253.15 – 573.19 K
- **Pressure range:** 100.0 – 350,000.0 kPa

**Properties measured (blocks):**

**L1#1_Table#3_(Query_L1#1_Answer):**

| *row_id* | *Property* | *Blocks* |
|---|---|---|
| L1#1_Table#3_Row#1 | 「Mass density, kg/m³」 | 「10」 |
| L1#1_Table#3_Row#2 | 「Speed of sound, m/s」 | 「4」 |
| L1#1_Table#3_Row#3 | 「Viscosity, Pa·s」 | 「4」 |
| L1#1_Table#3_Row#4 | 「Excess molar volume, m³/mol」 | 「2」 |
| L1#1_Table#3_Row#5 | 「Molar heat capacity at constant pressure, J/K/mol」 | 「2」 |
| L1#1_Table#3_Row#6 | 「Thermal conductivity, W/m/K」 | 「2」 |
| L1#1_Table#3_Row#7 | 「Specific volume, m³/kg」 | 「2」 |
| L1#1_Table#3_Row#8 | 「Excess molar heat capacity, J/K/mol」 | 「1」 |
| L1#1_Table#3_Row#9 | 「Surface tension liquid-gas, N/m」 | 「1」 |
| L1#1_Table#3_Row#10 | 「Excess molar enthalpy (molar enthalpy of mixing), kJ/mol」 | 「1」 |

**Top literature sources:**

**L1#1_Table#4_(Query_L1#1_Answer):**

| *row_id* | *DOI* | *Blocks* | *Points* |
|---|---|---|---|
| L1#1_Table#4_Row#1 | 「10.1021/je0340755 (GLOBlit_8239)」 | 「3」 | 「375」 |
| L1#1_Table#4_Row#2 | 「10.1021/acs.jced.8b00403 (GLOBlit_7545)」 | 「3」 | 「291」 |
| L1#1_Table#4_Row#3 | 「10.1021/je201184b (GLOBlit_9758)」 | 「2」 | 「212」 |
| L1#1_Table#4_Row#4 | 「10.1016/j.fluid.2013.06.041 (GLOBlit_1283)」 | 「2」 | 「185」 |
| L1#1_Table#4_Row#5 | 「10.1016/j.fluid.2014.12.040 (GLOBlit_1623)」 | 「2」 | 「168」 |

---

##### 3. Diethylene Glycol + Water

- **Compound IDs:** GLOBcomp_111 + GLOBcomp_1
- **Coverage:** 28 blocks, 15 papers, 2,079 data points
- **Temperature range:** 278.15 – 573.184 K
- **Pressure range:** 50.0 – 30,500.0 kPa

**Properties measured (blocks):**

**L1#1_Table#5_(Query_L1#1_Answer):**

| *row_id* | *Property* | *Blocks* |
|---|---|---|
| L1#1_Table#5_Row#1 | 「Mass density, kg/m³」 | 「10」 |
| L1#1_Table#5_Row#2 | 「Speed of sound, m/s」 | 「6」 |
| L1#1_Table#5_Row#3 | 「Viscosity, Pa·s」 | 「4」 |
| L1#1_Table#5_Row#4 | 「Binary diffusion coefficient, m²/s」 | 「2」 |
| L1#1_Table#5_Row#5 | 「Excess molar enthalpy (molar enthalpy of mixing), kJ/mol」 | 「2」 |
| L1#1_Table#5_Row#6 | 「Molar heat capacity at constant pressure, J/K/mol」 | 「1」 |
| L1#1_Table#5_Row#7 | 「Boiling temperature at pressure P, K」 | 「1」 |
| L1#1_Table#5_Row#8 | 「Refractive index (Na D-line)」 | 「1」 |
| L1#1_Table#5_Row#9 | 「Thermal conductivity, W/m/K」 | 「1」 |

**Top literature sources:**

**L1#1_Table#6_(Query_L1#1_Answer):**

| *row_id* | *DOI* | *Blocks* | *Points* |
|---|---|---|---|
| L1#1_Table#6_Row#1 | 「10.1016/j.jct.2016.07.016 (GLOBlit_4754)」 | 「1」 | 「588」 |
| L1#1_Table#6_Row#2 | 「10.1016/j.jct.2018.02.022 (GLOBlit_5201)」 | 「3」 | 「456」 |
| L1#1_Table#6_Row#3 | 「10.1021/je700672f (GLOBlit_11031)」 | 「2」 | 「286」 |
| L1#1_Table#6_Row#4 | 「10.1021/je1009976 (GLOBlit_9382)」 | 「2」 | 「170」 |
| L1#1_Table#6_Row#5 | 「10.1021/acs.jced.5b00498 (GLOBlit_6630)」 | 「2」 | 「140」 |

---

##### 4. Triethylene Glycol + Water

- **Compound IDs:** GLOBcomp_113 + GLOBcomp_1
- **Coverage:** 40 blocks, 16 papers, 3,638 data points
- **Temperature range:** 278.15 – 573.183 K
- **Pressure range:** 50.0 – 30,510.0 kPa

**Properties measured (blocks):**

**L1#1_Table#7_(Query_L1#1_Answer):**

| *row_id* | *Property* | *Blocks* |
|---|---|---|
| L1#1_Table#7_Row#1 | 「Mass density, kg/m³」 | 「10」 |
| L1#1_Table#7_Row#2 | 「Refractive index (other wavelength)」 | 「9」 |
| L1#1_Table#7_Row#3 | 「Speed of sound, m/s」 | 「6」 |
| L1#1_Table#7_Row#4 | 「Boiling temperature at pressure P, K」 | 「3」 |
| L1#1_Table#7_Row#5 | 「Viscosity, Pa·s」 | 「3」 |
| L1#1_Table#7_Row#6 | 「Binary diffusion coefficient, m²/s」 | 「2」 |
| L1#1_Table#7_Row#7 | 「Mole fraction」 | 「2」 |
| L1#1_Table#7_Row#8 | 「Joule-Thomson coefficient, K/kPa」 | 「1」 |
| L1#1_Table#7_Row#9 | 「Molar heat capacity at constant pressure, J/K/mol」 | 「1」 |
| L1#1_Table#7_Row#10 | 「Excess molar enthalpy (molar enthalpy of mixing), kJ/mol」 | 「1」 |

**Top literature sources:**

**L1#1_Table#8_(Query_L1#1_Answer):**

| *row_id* | *DOI* | *Blocks* | *Points* |
|---|---|---|---|
| L1#1_Table#8_Row#1 | 「10.1016/j.fluid.2015.07.030 (GLOBlit_1753)」 | 「12」 | 「1370」 |
| L1#1_Table#8_Row#2 | 「10.1016/j.jct.2015.05.024 (GLOBlit_4395)」 | 「2」 | 「667」 |
| L1#1_Table#8_Row#3 | 「10.1016/j.jct.2016.07.016 (GLOBlit_4754)」 | 「1」 | 「598」 |
| L1#1_Table#8_Row#4 | 「10.1016/j.jct.2018.02.022 (GLOBlit_5201)」 | 「3」 | 「432」 |
| L1#1_Table#8_Row#5 | 「10.1021/acs.jced.5b00498 (GLOBlit_6630)」 | 「2」 | 「140」 |

---

##### Cross-System Summary

**L1#1_Table#9_(Query_L1#1_Answer):**

| *row_id* | *Glycol + Water System* | *Blocks* | *Papers* | *Data Points* | *T range (K)* | *P range (kPa)* |
|---|---|---|---|---|---|---|
| L1#1_Table#9_Row#1 | 「Ethylene glycol」 | 「59」 | 「32」 | 「2,584」 | 「258.32 – 573.23」 | 「50.0 – 350,200.0」 |
| L1#1_Table#9_Row#2 | 「Propylene glycol」 | 「34」 | 「18」 | 「1,780」 | 「253.15 – 573.19」 | 「100.0 – 350,000.0」 |
| L1#1_Table#9_Row#3 | 「Diethylene glycol」 | 「28」 | 「15」 | 「2,079」 | 「278.15 – 573.184」 | 「50.0 – 30,500.0」 |
| L1#1_Table#9_Row#4 | 「Triethylene glycol」 | 「40」 | 「16」 | 「3,638」 | 「278.15 – 573.183」 | 「50.0 – 30,510.0」 |
| L1#1_Table#9_Row#5 | 「**Total**」 | 「**161**」 | 「**81***」 | 「**10,081**」 | 「—」 | 「—」 |

*Some papers appear in multiple systems (e.g., GLOBlit_5201 and GLOBlit_1283 cover multiple glycol systems), so the unique paper count is lower.

##### Key Observations

- **Mass density** is the most commonly measured property across all four systems (46 blocks total), reflecting its importance for engineering applications of glycol-water heat transfer fluids and antifreeze formulations.
- **Speed of sound** and **viscosity** are the next most common, each appearing in all four systems.
- **Triethylene glycol + water** has the largest dataset (3,638 points), driven largely by a single comprehensive study (GLOBlit_1753, DOI: 10.1016/j.fluid.2015.07.030) contributing 1,370 points across 12 blocks.
- **Ethylene glycol + water** has the broadest literature coverage (32 papers), consistent with its widespread industrial use as an antifreeze and coolant.
- All four systems span similar upper temperature ranges (~573 K), but ethylene glycol and propylene glycol systems extend to higher pressures (up to ~350 MPa), likely from high-pressure density studies.
- Transport properties (diffusion coefficients, thermal conductivity) and excess thermodynamic properties (excess molar enthalpy, excess molar volume) are available but less common than volumetric and acoustic properties.

**Core claims:**
- The ThermoML database contains data for four glycol + water binary systems (ethylene glycol, propylene glycol, diethylene glycol, triethylene glycol), totaling 161 property blocks across 81 literature sources (some shared across systems) with 10,081 data points.
- Ethylene glycol + water has the broadest literature coverage (59 blocks, 32 papers, 2,584 data points), spanning 258.32 – 573.23 K and 50.0 – 350,200.0 kPa.
- Propylene glycol + water covers 34 blocks, 18 papers, and 1,780 data points, spanning 253.15 – 573.19 K and 100.0 – 350,000.0 kPa.
- Diethylene glycol + water covers 28 blocks, 15 papers, and 2,079 data points, spanning 278.15 – 573.184 K and 50.0 – 30,500.0 kPa.
- Triethylene glycol + water has the largest dataset (40 blocks, 16 papers, 3,638 data points), spanning 278.15 – 573.183 K and 50.0 – 30,510.0 kPa, driven largely by a single study (DOI: 10.1016/j.fluid.2015.07.030) contributing 1,370 points across 12 blocks.
- Mass density is the most commonly measured property across all four systems (46 blocks total), followed by speed of sound and viscosity, each appearing in all four systems.
- Ethylene glycol and propylene glycol systems extend to higher pressures (up to ~350 MPa), likely from high-pressure density studies, while all four systems span similar upper temperature ranges (~573 K).
- Transport properties (diffusion coefficients, thermal conductivity) and excess thermodynamic properties (excess molar enthalpy, excess molar volume) are available but less common than volumetric and acoustic properties.

**Core ID updates:**
- add GLOBcomp_24 — 1,2-ethanediol (registry: 1,2-ethanediol)
- add GLOBcomp_1 — water (registry: water)
- add GLOBcomp_61 — 1,2-propanediol (registry: 1,2-propanediol)
- add GLOBcomp_111 — diethylene glycol (registry: diethylene_glycol)
- add GLOBcomp_113 — triethylene glycol (registry: triethylene_glycol)
- add GLOBlit_5201 — 10.1016/j.jct.2018.02.022 (registry: 2018-hog-tor-0)
- add GLOBlit_10102 — 10.1021/je4001203 (registry: 2013-hne-cib-1)
- add GLOBlit_8038 — 10.1021/je020140j (registry: 2003-yan-ma-2)
- add GLOBlit_6951 — 10.1021/acs.jced.6b00526 (registry: 2017-moo-ros-0)
- add GLOBlit_1283 — 10.1016/j.fluid.2013.06.041 (registry: 2013-zem-tro-0)
- add GLOBlit_8239 — 10.1021/je0340755 (registry: 2003-geo-sas-1)
- add GLOBlit_7545 — 10.1021/acs.jced.8b00403 (registry: 2018-mik-sko-0)
- add GLOBlit_9758 — 10.1021/je201184b (registry: 2012-kat-hne-0)
- add GLOBlit_1623 — 10.1016/j.fluid.2014.12.040 (registry: 2015-cha-hsi-0)
- add GLOBlit_4754 — 10.1016/j.jct.2016.07.016 (registry: 2017-cib--1)
- add GLOBlit_11031 — 10.1021/je700672f (registry: 2008-man-guz-0)
- add GLOBlit_9382 — 10.1021/je1009976 (registry: 2011-beg-cla-0)
- add GLOBlit_6630 — 10.1021/acs.jced.5b00498 (registry: 2016-cib--0)
- add GLOBlit_1753 — 10.1016/j.fluid.2015.07.030 (registry: 2015-ani-sin-0)
- add GLOBlit_4395 — 10.1016/j.jct.2015.05.024 (registry: 2015-kli-str-1)
</subagent_answer>
</tool_result>

## LLM Response
<reasoning>
The L1 query has returned comprehensive results. The data is already in working memory from a previous query, and the L1 return confirms all the same information. I can now provide the final answer.
</reasoning>

<answer>

## Glycol + Water Binary Mixture Data in the ThermoML Database

The ThermoML database contains extensive thermodynamic and transport property data for **four glycol + water binary systems**, totaling **161 property blocks** across **81 literature sources** (some shared across systems) with **10,081 data points**. These glycol–water mixtures are of major industrial importance as antifreeze formulations, heat-transfer fluids, and gas-dehydration agents.

---

### Cross-System Summary

| Glycol + Water System | Blocks | Papers | Data Points | T range (K) | P range (kPa) |
|---|---|---|---|---|---|
| Ethylene glycol (1,2-ethanediol) | 59 | 32 | 2,584 | 258.32 – 573.23 | 50.0 – 350,200.0 |
| Propylene glycol (1,2-propanediol) | 34 | 18 | 1,780 | 253.15 – 573.19 | 100.0 – 350,000.0 |
| Diethylene glycol | 28 | 15 | 2,079 | 278.15 – 573.184 | 50.0 – 30,500.0 |
| Triethylene glycol | 40 | 16 | 3,638 | 278.15 – 573.183 | 50.0 – 30,510.0 |
| **Total** | **161** | **81*** | **10,081** | — | — |

\*Some papers cover multiple glycol systems, so the unique paper count is lower.

---

### 1. Ethylene Glycol (1,2-Ethanediol) + Water

The most widely studied system, with **59 blocks from 32 papers** and **2,584 data points**, spanning 258.32–573.23 K and up to 350,200 kPa (~350 MPa).

**Properties measured (by number of blocks):**

| Property | Blocks |
|---|---|
| Mass density (kg/m³) | 16 |
| Speed of sound (m/s) | 8 |
| Viscosity (Pa·s) | 7 |
| Binary diffusion coefficient (m²/s) | 5 |
| Surface tension liquid–gas (N/m) | 4 |
| Vapor or sublimation pressure (kPa) | 3 |
| Boiling temperature at pressure P (K) | 3 |
| Mole fraction | 2 |
| Refractive index (Na D-line) | 2 |
| Specific volume (m³/kg) | 2 |

**Top literature sources:**

| DOI | Blocks | Points |
|---|---|---|
| 10.1016/j.jct.2018.02.022 | 3 | 456 |
| 10.1021/je4001203 | 2 | 276 |
| 10.1021/je020140j | 3 | 249 |
| 10.1021/acs.jced.6b00526 | 3 | 236 |
| 10.1016/j.fluid.2013.06.041 | 2 | 214 |

---

### 2. Propylene Glycol (1,2-Propanediol) + Water

**34 blocks from 18 papers**, **1,780 data points**, spanning 253.15–573.19 K and up to 350,000 kPa (~350 MPa).

**Properties measured (by number of blocks):**

| Property | Blocks |
|---|---|
| Mass density (kg/m³) | 10 |
| Speed of sound (m/s) | 4 |
| Viscosity (Pa·s) | 4 |
| Excess molar volume (m³/mol) | 2 |
| Molar heat capacity at constant pressure (J/K/mol) | 2 |
| Thermal conductivity (W/m/K) | 2 |
| Specific volume (m³/kg) | 2 |
| Excess molar heat capacity (J/K/mol) | 1 |
| Surface tension liquid–gas (N/m) | 1 |
| Excess molar enthalpy of mixing (kJ/mol) | 1 |

**Top literature sources:**

| DOI | Blocks | Points |
|---|---|---|
| 10.1021/je0340755 | 3 | 375 |
| 10.1021/acs.jced.8b00403 | 3 | 291 |
| 10.1021/je201184b | 2 | 212 |
| 10.1016/j.fluid.2013.06.041 | 2 | 185 |
| 10.1016/j.fluid.2014.12.040 | 2 | 168 |

---

### 3. Diethylene Glycol + Water

**28 blocks from 15 papers**, **2,079 data points**, spanning 278.15–573.184 K and up to 30,500 kPa.

**Properties measured (by number of blocks):**

| Property | Blocks |
|---|---|
| Mass density (kg/m³) | 10 |
| Speed of sound (m/s) | 6 |
| Viscosity (Pa·s) | 4 |
| Binary diffusion coefficient (m²/s) | 2 |
| Excess molar enthalpy of mixing (kJ/mol) | 2 |
| Molar heat capacity at constant pressure (J/K/mol) | 1 |
| Boiling temperature at pressure P (K) | 1 |
| Refractive index (Na D-line) | 1 |
| Thermal conductivity (W/m/K) | 1 |

**Top literature sources:**

| DOI | Blocks | Points |
|---|---|---|
| 10.1016/j.jct.2016.07.016 | 1 | 588 |
| 10.1016/j.jct.2018.02.022 | 3 | 456 |
| 10.1021/je700672f | 2 | 286 |
| 10.1021/je1009976 | 2 | 170 |
| 10.1021/acs.jced.5b00498 | 2 | 140 |

---

### 4. Triethylene Glycol + Water

The **largest dataset** with **40 blocks from 16 papers** and **3,638 data points**, spanning 278.15–573.183 K and up to 30,510 kPa.

**Properties measured (by number of blocks):**

| Property | Blocks |
|---|---|
| Mass density (kg/m³) | 10 |
| Refractive index (other wavelength) | 9 |
| Speed of sound (m/s) | 6 |
| Boiling temperature at pressure P (K) | 3 |
| Viscosity (Pa·s) | 3 |
| Binary diffusion coefficient (m²/s) | 2 |
| Mole fraction | 2 |
| Joule-Thomson coefficient (K/kPa) | 1 |
| Molar heat capacity at constant pressure (J/K/mol) | 1 |
| Excess molar enthalpy of mixing (kJ/mol) | 1 |

**Top literature sources:**

| DOI | Blocks | Points |
|---|---|---|
| 10.1016/j.fluid.2015.07.030 | 12 | 1,370 |
| 10.1016/j.jct.2015.05.024 | 2 | 667 |
| 10.1016/j.jct.2016.07.016 | 1 | 598 |
| 10.1016/j.jct.2018.02.022 | 3 | 432 |
| 10.1021/acs.jced.5b00498 | 2 | 140 |

---

### Key Observations & Chemical Context

- **Mass density** is the most commonly measured property across all four systems (46 blocks total), reflecting its central importance for engineering design of glycol–water heat-transfer fluids and antifreeze formulations.
- **Speed of sound** and **dynamic viscosity** are the next most common, each appearing in all four systems — critical for acoustic and flow characterization.
- **Ethylene glycol + water** has the broadest literature coverage (32 papers), consistent with its dominant industrial role as an automotive antifreeze and coolant.
- **Triethylene glycol + water** has the largest single dataset (3,638 points), driven largely by one comprehensive study (DOI: 10.1016/j.fluid.2015.07.030) contributing 1,370 points across 12 blocks — reflecting triethylene glycol's importance in natural gas dehydration.
- **Ethylene glycol** and **propylene glycol** systems extend to much higher pressures (up to ~350 MPa), likely from high-pressure density studies relevant to deep-well and high-pressure process conditions.
- All four systems reach similar upper temperatures (~573 K), covering conditions relevant to both ambient and elevated-temperature industrial processes.
- **Transport properties** (diffusion coefficients, thermal conductivity) and **excess thermodynamic properties** (excess molar enthalpy, excess molar volume) are available but less common than volumetric and acoustic properties.
- Several literature sources span multiple glycol systems (e.g., DOI: 10.1016/j.jct.2018.02.022 covers ethylene glycol, diethylene glycol, and triethylene glycol with water), enabling direct cross-system comparisons under identical experimental conditions.

</answer>