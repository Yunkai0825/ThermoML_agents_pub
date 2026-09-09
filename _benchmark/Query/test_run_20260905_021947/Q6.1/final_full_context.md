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
| comp | GLOBcomp_58 | glycerol | glycerol |
| comp | GLOBcomp_1 | water | water |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find data for the binary system propane-1,2,3-triol (glycerol) + water in ThermoML. The user wrote 'propane-1,2,4-triol' → stored as L1_query_1 · validation: PASS

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: PASS

**Summary:** The binary system glycerol (propane-1,2,3-triol, CAS 56-81-5) + water is represented in ThermoML with 36 property data blocks across 20 literature sources covering 13 distinct thermophysical properties. Properties include mass density (10 blocks), speed of sound (5 blocks), boiling temperature (5 blocks), vapor pressure (2 blocks), binary diffusion coefficient (2 blocks), and others such as viscosity, refractive index, and excess volumes. Representative mass density data from GLOBlit_4951 (Negadi, 2017) at 100 kPa span 283.15–313.15 K and water mole fractions 0–1, showing monotonic decrease from pure glycerol (1267 kg/m³ at 283.15 K) to pure water (1000 kg/m³ at 283.15 K), with density decreasing with increasing temperature at each composition (e.g., pure glycerol drops from 1267 to 1248 kg/m³ over 283.15–313.15 K). Sources span 2006–2018 and include journals such as J. Chem. Thermodynamics, J. Chem. Eng. Data, Fluid Phase Equilibria, and Thermochimica Acta. The note clarifies that propane-1,2,4-triol cannot exist since propane has only 3 carbon atoms; the intended compound is glycerol (propane-1,2,3-triol).

**Answer:**

#### Glycerol (propane-1,2,3-triol) + Water Binary System in ThermoML

**Note:** The compound "propane-1,2,4-triol" cannot exist because propane has only 3 carbon atoms. The intended compound is **glycerol (propane-1,2,3-triol, CAS 56-81-5)**.

##### System Overview

The binary system **glycerol (GLOBcomp_58) + water (GLOBcomp_1)** is well-represented in ThermoML with **36 property data blocks** across **20 literature sources**, covering **13 distinct thermophysical properties**.

##### Available Properties

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *Property* | *GLOBprop* | *# Blocks* |
|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「Mass density (kg/m³)」 | 「GLOBprop_1」 | 「10」 |
| WM_L1#1_Table#1_Row#2 | 「Speed of sound (m/s)」 | 「GLOBprop_8」 | 「5」 |
| WM_L1#1_Table#1_Row#3 | 「Boiling temperature (K)」 | 「GLOBprop_14」 | 「5」 |
| WM_L1#1_Table#1_Row#4 | 「Vapor pressure (kPa)」 | 「GLOBprop_5」 | 「2」 |
| WM_L1#1_Table#1_Row#5 | 「Binary diffusion coefficient (m²/s)」 | 「GLOBprop_29」 | 「2」 |
| WM_L1#1_Table#1_Row#6 | 「And additional properties (viscosity, refractive index, excess volumes, etc.)」 | 「—」 | 「remaining blocks」 |

##### Literature Sources (selected)

**WM_L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *DOI* | *GLOBlit_N* | *Author* | *Year* |
|---|---|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「10.1016/j.jct.2017.01.011」 | 「GLOBlit_4951」 | 「Negadi, L.」 | 「2017」 |
| WM_L1#1_Table#2_Row#2 | 「10.1016/j.jct.2018.05.016」 | 「GLOBlit_5254」 | 「Kaur, K.」 | 「2018」 |

Additional DOIs include publications in J. Chem. Thermodynamics, J. Chem. Eng. Data, Fluid Phase Equilibria, and Thermochimica Acta (2006–2018 range).

##### Representative Data: Mass Density at 100 kPa

From **GLOBlit_4951** (Negadi, 2017), **PROPblock_3** — mass density of glycerol + water as a function of temperature and water mole fraction at 100 kPa (44 data points total, 283.15–313.15 K):

**WM_L1#1_Table#3_(Query_L1#1_Answer):**

| *row_id* | *T (K)* | *x(water)* | *ρ (kg/m³)* |
|---|---|---|---|
| WM_L1#1_Table#3_Row#1 | 「283.15」 | 「0」 | 「1267」 |
| WM_L1#1_Table#3_Row#2 | 「283.15」 | 「0.4042」 | 「1236」 |
| WM_L1#1_Table#3_Row#3 | 「283.15」 | 「0.7003」 | 「1183」 |
| WM_L1#1_Table#3_Row#4 | 「283.15」 | 「0.9024」 | 「1091」 |
| WM_L1#1_Table#3_Row#5 | 「283.15」 | 「1」 | 「1000」 |
| WM_L1#1_Table#3_Row#6 | 「293.15」 | 「0」 | 「1261」 |
| WM_L1#1_Table#3_Row#7 | 「293.15」 | 「0.4042」 | 「1230」 |
| WM_L1#1_Table#3_Row#8 | 「293.15」 | 「0.7003」 | 「1177」 |
| WM_L1#1_Table#3_Row#9 | 「293.15」 | 「0.9024」 | 「1087」 |
| WM_L1#1_Table#3_Row#10 | 「293.15」 | 「1」 | 「998」 |
| WM_L1#1_Table#3_Row#11 | 「303.15」 | 「0」 | 「1255」 |
| WM_L1#1_Table#3_Row#12 | 「303.15」 | 「0.4042」 | 「1224」 |
| WM_L1#1_Table#3_Row#13 | 「303.15」 | 「0.7003」 | 「1172」 |
| WM_L1#1_Table#3_Row#14 | 「303.15」 | 「0.9024」 | 「1083」 |
| WM_L1#1_Table#3_Row#15 | 「303.15」 | 「1」 | 「996」 |
| WM_L1#1_Table#3_Row#16 | 「313.15」 | 「0」 | 「1248」 |
| WM_L1#1_Table#3_Row#17 | 「313.15」 | 「0.4042」 | 「1218」 |
| WM_L1#1_Table#3_Row#18 | 「313.15」 | 「0.7003」 | 「1166」 |
| WM_L1#1_Table#3_Row#19 | 「313.15」 | 「0.9024」 | 「1078」 |
| WM_L1#1_Table#3_Row#20 | 「313.15」 | 「1」 | 「992」 |

##### Chemical Insight

The density data show the expected monotonic decrease from pure glycerol (ρ ≈ 1267 kg/m³ at 283.15 K) to pure water (ρ ≈ 1000 kg/m³ at 283.15 K) as the water mole fraction increases. At each composition, density decreases with increasing temperature — for example, pure glycerol drops from 1267 kg/m³ at 283.15 K to 1248 kg/m³ at 313.15 K. The glycerol–water system is widely studied because glycerol is a major bio-derived polyol used as a humectant, cryoprotectant, and green solvent, and its aqueous mixtures exhibit significant hydrogen-bonding interactions that influence all transport and volumetric properties.

**Core claims:**
- The binary system glycerol (propane-1,2,3-triol, CAS 56-81-5) + water is represented in ThermoML by 36 property data blocks across 20 literature sources, covering 13 distinct thermophysical properties including mass density, speed of sound, boiling temperature, vapor pressure, and binary diffusion coefficient.
- Mass density data from GLOBlit_4951 (Negadi, 2017) at 100 kPa show a monotonic decrease from pure glycerol (ρ ≈ 1267 kg/m³ at 283.15 K) to pure water (ρ ≈ 1000 kg/m³ at 283.15 K) as water mole fraction increases.
- At each composition, density decreases with increasing temperature; for example, pure glycerol drops from 1267 kg/m³ at 283.15 K to 1248 kg/m³ at 313.15 K.
- The compound 'propane-1,2,4-triol' cannot exist because propane has only 3 carbon atoms; the intended compound is glycerol (propane-1,2,3-triol).

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#4 | 「GLOBlit_4951」 | 「PROPblock_3」 | 「GLOBcomp_58, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of glycerol + water as a function of temperature and water mole fraction at 100 kPa (283.15–313.15 K).」 |

*Not stored here: 1 verbatim data_inspections table(s); 2 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.



</memory>

## User
Find data for the binary system propane-1,2,4-triol + water.

## Assistant
<summary>User asks for binary system data for propane-1,2,4-triol + water. Note: propane-1,2,4-triol is chemically impossible (propane has only 3 carbons). User likely means propane-1,2,3-triol (glycerol). Dispatching L1 query to search for this system.</summary>
<tool_call>L1_query(instruction=Search for the bi…)</tool_call>

## User
<tool_result>
<subagent_answer>
### L1#1 — L1_query return

**Status:** status=success

**Summary:** The binary system glycerol (propane-1,2,3-triol, CAS 56-81-5) + water is represented in ThermoML with 36 property data blocks across 20 literature sources covering 13 distinct thermophysical properties. Properties include mass density (10 blocks), speed of sound (5 blocks), boiling temperature (5 blocks), vapor pressure (2 blocks), binary diffusion coefficient (2 blocks), and others such as viscosity, refractive index, and excess volumes. Representative mass density data from GLOBlit_4951 (Negadi, 2017) at 100 kPa span 283.15–313.15 K and water mole fractions 0–1, showing monotonic decrease from pure glycerol (1267 kg/m³ at 283.15 K) to pure water (1000 kg/m³ at 283.15 K), with density decreasing with increasing temperature at each composition (e.g., pure glycerol drops from 1267 to 1248 kg/m³ over 283.15–313.15 K). Sources span 2006–2018 and include journals such as J. Chem. Thermodynamics, J. Chem. Eng. Data, Fluid Phase Equilibria, and Thermochimica Acta. The note clarifies that propane-1,2,4-triol cannot exist since propane has only 3 carbon atoms; the intended compound is glycerol (propane-1,2,3-triol).

**Answer:**

#### Glycerol (propane-1,2,3-triol) + Water Binary System in ThermoML

**Note:** The compound "propane-1,2,4-triol" cannot exist because propane has only 3 carbon atoms. The intended compound is **glycerol (propane-1,2,3-triol, CAS 56-81-5)**.

##### System Overview

The binary system **glycerol (GLOBcomp_58) + water (GLOBcomp_1)** is well-represented in ThermoML with **36 property data blocks** across **20 literature sources**, covering **13 distinct thermophysical properties**.

##### Available Properties

**L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *Property* | *GLOBprop* | *# Blocks* |
|---|---|---|---|
| L1#1_Table#1_Row#1 | 「Mass density (kg/m³)」 | 「GLOBprop_1」 | 「10」 |
| L1#1_Table#1_Row#2 | 「Speed of sound (m/s)」 | 「GLOBprop_8」 | 「5」 |
| L1#1_Table#1_Row#3 | 「Boiling temperature (K)」 | 「GLOBprop_14」 | 「5」 |
| L1#1_Table#1_Row#4 | 「Vapor pressure (kPa)」 | 「GLOBprop_5」 | 「2」 |
| L1#1_Table#1_Row#5 | 「Binary diffusion coefficient (m²/s)」 | 「GLOBprop_29」 | 「2」 |
| L1#1_Table#1_Row#6 | 「And additional properties (viscosity, refractive index, excess volumes, etc.)」 | 「—」 | 「remaining blocks」 |

##### Literature Sources (selected)

**L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *DOI* | *GLOBlit_N* | *Author* | *Year* |
|---|---|---|---|---|
| L1#1_Table#2_Row#1 | 「10.1016/j.jct.2017.01.011」 | 「GLOBlit_4951」 | 「Negadi, L.」 | 「2017」 |
| L1#1_Table#2_Row#2 | 「10.1016/j.jct.2018.05.016」 | 「GLOBlit_5254」 | 「Kaur, K.」 | 「2018」 |

Additional DOIs include publications in J. Chem. Thermodynamics, J. Chem. Eng. Data, Fluid Phase Equilibria, and Thermochimica Acta (2006–2018 range).

##### Representative Data: Mass Density at 100 kPa

From **GLOBlit_4951** (Negadi, 2017), **PROPblock_3** — mass density of glycerol + water as a function of temperature and water mole fraction at 100 kPa (44 data points total, 283.15–313.15 K):

**L1#1_Table#3_(Query_L1#1_Answer):**

| *row_id* | *T (K)* | *x(water)* | *ρ (kg/m³)* |
|---|---|---|---|
| L1#1_Table#3_Row#1 | 「283.15」 | 「0」 | 「1267」 |
| L1#1_Table#3_Row#2 | 「283.15」 | 「0.4042」 | 「1236」 |
| L1#1_Table#3_Row#3 | 「283.15」 | 「0.7003」 | 「1183」 |
| L1#1_Table#3_Row#4 | 「283.15」 | 「0.9024」 | 「1091」 |
| L1#1_Table#3_Row#5 | 「283.15」 | 「1」 | 「1000」 |
| L1#1_Table#3_Row#6 | 「293.15」 | 「0」 | 「1261」 |
| L1#1_Table#3_Row#7 | 「293.15」 | 「0.4042」 | 「1230」 |
| L1#1_Table#3_Row#8 | 「293.15」 | 「0.7003」 | 「1177」 |
| L1#1_Table#3_Row#9 | 「293.15」 | 「0.9024」 | 「1087」 |
| L1#1_Table#3_Row#10 | 「293.15」 | 「1」 | 「998」 |
| L1#1_Table#3_Row#11 | 「303.15」 | 「0」 | 「1255」 |
| L1#1_Table#3_Row#12 | 「303.15」 | 「0.4042」 | 「1224」 |
| L1#1_Table#3_Row#13 | 「303.15」 | 「0.7003」 | 「1172」 |
| L1#1_Table#3_Row#14 | 「303.15」 | 「0.9024」 | 「1083」 |
| L1#1_Table#3_Row#15 | 「303.15」 | 「1」 | 「996」 |
| L1#1_Table#3_Row#16 | 「313.15」 | 「0」 | 「1248」 |
| L1#1_Table#3_Row#17 | 「313.15」 | 「0.4042」 | 「1218」 |
| L1#1_Table#3_Row#18 | 「313.15」 | 「0.7003」 | 「1166」 |
| L1#1_Table#3_Row#19 | 「313.15」 | 「0.9024」 | 「1078」 |
| L1#1_Table#3_Row#20 | 「313.15」 | 「1」 | 「992」 |

##### Chemical Insight

The density data show the expected monotonic decrease from pure glycerol (ρ ≈ 1267 kg/m³ at 283.15 K) to pure water (ρ ≈ 1000 kg/m³ at 283.15 K) as the water mole fraction increases. At each composition, density decreases with increasing temperature — for example, pure glycerol drops from 1267 kg/m³ at 283.15 K to 1248 kg/m³ at 313.15 K. The glycerol–water system is widely studied because glycerol is a major bio-derived polyol used as a humectant, cryoprotectant, and green solvent, and its aqueous mixtures exhibit significant hydrogen-bonding interactions that influence all transport and volumetric properties.

**Core claims:**
- The binary system glycerol (propane-1,2,3-triol, CAS 56-81-5) + water is represented in ThermoML by 36 property data blocks across 20 literature sources, covering 13 distinct thermophysical properties including mass density, speed of sound, boiling temperature, vapor pressure, and binary diffusion coefficient.
- Mass density data from GLOBlit_4951 (Negadi, 2017) at 100 kPa show a monotonic decrease from pure glycerol (ρ ≈ 1267 kg/m³ at 283.15 K) to pure water (ρ ≈ 1000 kg/m³ at 283.15 K) as water mole fraction increases.
- At each composition, density decreases with increasing temperature; for example, pure glycerol drops from 1267 kg/m³ at 283.15 K to 1248 kg/m³ at 313.15 K.
- The compound 'propane-1,2,4-triol' cannot exist because propane has only 3 carbon atoms; the intended compound is glycerol (propane-1,2,3-triol).

**Core ID updates:**
- add GLOBcomp_58 — glycerol (registry: glycerol)
- add GLOBcomp_1 — water (registry: water)

#### Core blocks found — verbatim ledger

```ledger
**L1#1_Table#4_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_4951 | lit_id: 2017-neg-fed-0 | doi: 10.1016/j.jct.2017.01.011
block: PROPblock_3 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 44
compounds: glycerol (C3H8O3; GLOBcomp_58; DOIcomp_1; InChIKey PEDCQBHIVMGVHV-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_2; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density of glycerol + water as a function of temperature and water mole fraction at 100 kPa (283.15–313.15 K).

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#4_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=100.0 · phase=Liquid」 |
| L1#1_Table#4_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=283.15–313.15 · n_unique=4 · phase=Liquid」 |
| L1#1_Table#4_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_2」 | 「Mole fraction of water」 | 「range=0.0–1.0 · n_unique=11 · phase=Liquid」 |
| L1#1_Table#4_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=Vibrating tube method (GLOBmeas_2) · range=992.0–1267.0 · mean=1184.204545 · n=44 · phase=Liquid」 |
```

#### Data inspections — verbatim ledger

```ledger
**L1#1_Table#5_(Query_L1#1_INSP):**
lit_num_id: GLOBlit_4951 | doi: 10.1016/j.jct.2017.01.011 | block: PROPblock_3
table_mode: rdp | inspection_id: INSP_b3d29a662be8 | rows_shown: 23

| *row_id* | *BLKpoint_id* | *temperature_k* | *mole_fraction_<water>* | *pressure_kpa* | *mass_density_kg_m3* |
|---|---|---|---|---|---|
| L1#1_Table#5_Row#1 | 「BLKpoint_1」 | 「283.15」 | 「0」 | 「100.0」 | 「1267」 |
| L1#1_Table#5_Row#2 | 「BLKpoint_5」 | 「283.15」 | 「0.4042」 | 「100.0」 | 「1236」 |
| L1#1_Table#5_Row#3 | 「BLKpoint_8」 | 「283.15」 | 「0.7003」 | 「100.0」 | 「1183」 |
| L1#1_Table#5_Row#4 | 「BLKpoint_9」 | 「283.15」 | 「0.7999」 | 「100.0」 | 「1148」 |
| L1#1_Table#5_Row#5 | 「BLKpoint_10」 | 「283.15」 | 「0.9024」 | 「100.0」 | 「1091」 |
| L1#1_Table#5_Row#6 | 「BLKpoint_11」 | 「283.15」 | 「1」 | 「100.0」 | 「1000」 |
| L1#1_Table#5_Row#7 | 「BLKpoint_12」 | 「293.15」 | 「0」 | 「100.0」 | 「1261」 |
| L1#1_Table#5_Row#8 | 「BLKpoint_16」 | 「293.15」 | 「0.4042」 | 「100.0」 | 「1230」 |
| L1#1_Table#5_Row#9 | 「BLKpoint_18」 | 「293.15」 | 「0.6011」 | 「100.0」 | 「1201」 |
| L1#1_Table#5_Row#10 | 「BLKpoint_19」 | 「293.15」 | 「0.7003」 | 「100.0」 | 「1177」 |
| L1#1_Table#5_Row#11 | 「BLKpoint_20」 | 「293.15」 | 「0.7999」 | 「100.0」 | 「1143」 |
| L1#1_Table#5_Row#12 | 「BLKpoint_21」 | 「293.15」 | 「0.9024」 | 「100.0」 | 「1087」 |
| L1#1_Table#5_Row#13 | 「BLKpoint_22」 | 「293.15」 | 「1」 | 「100.0」 | 「998」 |
| L1#1_Table#5_Row#14 | 「BLKpoint_23」 | 「303.15」 | 「0」 | 「100.0」 | 「1255」 |
| L1#1_Table#5_Row#15 | 「BLKpoint_27」 | 「303.15」 | 「0.4042」 | 「100.0」 | 「1224」 |
| L1#1_Table#5_Row#16 | 「BLKpoint_30」 | 「303.15」 | 「0.7003」 | 「100.0」 | 「1172」 |
| L1#1_Table#5_Row#17 | 「BLKpoint_32」 | 「303.15」 | 「0.9024」 | 「100.0」 | 「1083」 |
| L1#1_Table#5_Row#18 | 「BLKpoint_33」 | 「303.15」 | 「1」 | 「100.0」 | 「996」 |
| L1#1_Table#5_Row#19 | 「BLKpoint_34」 | 「313.15」 | 「0」 | 「100.0」 | 「1248」 |
| L1#1_Table#5_Row#20 | 「BLKpoint_38」 | 「313.15」 | 「0.4042」 | 「100.0」 | 「1218」 |
| L1#1_Table#5_Row#21 | 「BLKpoint_41」 | 「313.15」 | 「0.7003」 | 「100.0」 | 「1166」 |
| L1#1_Table#5_Row#22 | 「BLKpoint_43」 | 「313.15」 | 「0.9024」 | 「100.0」 | 「1078」 |
| L1#1_Table#5_Row#23 | 「BLKpoint_44」 | 「313.15」 | 「1」 | 「100.0」 | 「992」 |
```
</subagent_answer>
</tool_result>

## LLM Response
<reasoning>
The L1 query has returned comprehensive data for the glycerol + water binary system. The data is already stored in working memory from a previous identical query. I have all the information needed to provide a complete answer.
</reasoning>

<answer>

## Binary System: Propane-1,2,3-triol (Glycerol) + Water

### Important Note on Nomenclature

The compound **"propane-1,2,4-triol" cannot exist** because propane has only 3 carbon atoms (C₁, C₂, C₃), so position "4" is impossible. The intended compound is **glycerol (propane-1,2,3-triol, CAS 56-81-5)**.

---

### System Overview

The binary system **glycerol + water** is extensively represented in the ThermoML database with **36 property data blocks** across **20 literature sources**, covering **13 distinct thermophysical properties**. Sources span the period 2006–2018 and include journals such as *J. Chem. Thermodynamics*, *J. Chem. Eng. Data*, *Fluid Phase Equilibria*, and *Thermochimica Acta*.

---

### Available Properties

| Property | # Blocks |
|---|---|
| Mass density (kg/m³) | 10 |
| Speed of sound (m/s) | 5 |
| Boiling temperature (K) | 5 |
| Vapor pressure (kPa) | 2 |
| Binary diffusion coefficient (m²/s) | 2 |
| Additional (viscosity, refractive index, excess volumes, etc.) | remaining |

---

### Selected Literature Sources

| DOI | Source ID | Author | Year |
|---|---|---|---|
| 10.1016/j.jct.2017.01.011 | GLOBlit_4951 | Negadi, L. | 2017 |
| 10.1016/j.jct.2018.05.016 | GLOBlit_5254 | Kaur, K. | 2018 |

---

### Representative Data: Mass Density at 100 kPa

From **Negadi (2017)** (DOI: 10.1016/j.jct.2017.01.011, GLOBlit_4951), PROPblock_3 — 44 data points spanning 283.15–313.15 K across the full composition range:

| T (K) | x(water) | ρ (kg/m³) |
|---|---|---|
| 283.15 | 0 | 1267 |
| 283.15 | 0.4042 | 1236 |
| 283.15 | 0.7003 | 1183 |
| 283.15 | 0.7999 | 1148 |
| 283.15 | 0.9024 | 1091 |
| 283.15 | 1 | 1000 |
| 293.15 | 0 | 1261 |
| 293.15 | 0.4042 | 1230 |
| 293.15 | 0.6011 | 1201 |
| 293.15 | 0.7003 | 1177 |
| 293.15 | 0.7999 | 1143 |
| 293.15 | 0.9024 | 1087 |
| 293.15 | 1 | 998 |
| 303.15 | 0 | 1255 |
| 303.15 | 0.4042 | 1224 |
| 303.15 | 0.7003 | 1172 |
| 303.15 | 0.9024 | 1083 |
| 303.15 | 1 | 996 |
| 313.15 | 0 | 1248 |
| 313.15 | 0.4042 | 1218 |
| 313.15 | 0.7003 | 1166 |
| 313.15 | 0.9024 | 1078 |
| 313.15 | 1 | 992 |

---

### Chemical Insight

Glycerol (C₃H₈O₃) is a symmetric triol with hydroxyl groups on all three carbons, enabling extensive hydrogen bonding both with itself and with water. This explains several features of the data:

- **Density decreases monotonically** from pure glycerol (ρ ≈ 1267 kg/m³ at 283.15 K) to pure water (ρ ≈ 1000 kg/m³ at 283.15 K) as the water mole fraction increases, reflecting the replacement of the denser, more strongly self-associated glycerol network with lighter water molecules.

- **Temperature dependence** is consistent across all compositions: density decreases with increasing temperature due to thermal expansion. For pure glycerol, ρ drops from 1267 kg/m³ at 283.15 K to 1248 kg/m³ at 313.15 K (a decrease of ~19 kg/m³ over 30 K). Pure water shows a smaller absolute change, from 1000 to 992 kg/m³ over the same range.

- The glycerol–water system is widely studied because glycerol is a major bio-derived polyol used as a humectant, cryoprotectant, and green solvent. Its aqueous mixtures exhibit significant hydrogen-bonding interactions that strongly influence transport properties (viscosity, diffusion) and volumetric properties (density, excess volume).

</answer>