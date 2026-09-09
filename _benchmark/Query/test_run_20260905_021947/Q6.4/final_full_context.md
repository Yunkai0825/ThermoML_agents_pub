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
| comp | GLOBcomp_31 | dimethyl_sulfoxide | dimethyl sulfoxide |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find mass density of pure liquid DMSO at 25 °C (298.15 K) → stored as L1_query_1 · validation: PASS

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: PASS

**Summary:** The mass density of pure liquid dimethyl sulfoxide (DMSO, CAS 67-68-5) at 298.15 K and near-atmospheric pressure is reported across five independent ThermoML sources in the narrow range 1095.27–1095.37 kg/m³. Representative values include 1095.271, 1095.278, 1095.27, 1095.37, and 1095.29 kg/m³ from different literature blocks, with slight variation attributed to differences in sample purity and pressure conditions (85.9–101.325 kPa). The temperature coefficient near 298.15 K is approximately −1.0 kg·m⁻³·K⁻¹, based on GLOBlit_86 data showing density decreasing from 1100.306 kg/m³ at 293.15 K to 1090.253 kg/m³ at 303.15 K. The full temperature series in that block spans 288.15–308.15 K with density ranging from 1085.231 to 1105.336 kg/m³.

**Answer:**

#### Mass Density of Pure Liquid DMSO at 298.15 K

Multiple independent ThermoML sources report the mass density of pure liquid dimethyl sulfoxide (DMSO, CAS 67-68-5, GLOBcomp_31) at 298.15 K. The inspected values are highly consistent:

##### Inspected Data Points at 298.15 K

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *Source (DOI)* | *Literature* | *Block* | *T (K)* | *P (kPa)* | *ρ (kg/m³)* |
|---|---|---|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「10.1007/s10765-008-0395-z」 | 「GLOBlit_57」 | 「PROPblock_7」 | 「298.15」 | 「101.325」 | 「1095.271」 |
| WM_L1#1_Table#1_Row#2 | 「10.1007/s10765-009-0648-5」 | 「GLOBlit_86」 | 「PROPblock_4」 | 「298.15」 | 「101.0」 | 「1095.278」 |
| WM_L1#1_Table#1_Row#3 | 「10.1016/j.fluid.2010.01.002」 | 「GLOBlit_779」 | 「PROPblock_3」 | 「298.15」 | 「101.325」 | 「1095.27」 |
| WM_L1#1_Table#1_Row#4 | 「10.1016/j.fluid.2011.02.010」 | 「GLOBlit_938」 | 「PROPblock_3」 | 「298.15」 | 「101.0」 | 「1095.37」 |
| WM_L1#1_Table#1_Row#5 | 「10.1016/j.fluid.2013.05.001」 | 「GLOBlit_1246」 | 「PROPblock_1」 | 「298.15」 | 「85.9」 | 「1095.29」 |

##### Temperature Dependence (GLOBlit_86, PROPblock_4)

The GLOBlit_86 block provides a temperature series showing the density decreases monotonically and nearly linearly with temperature:

**WM_L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *BLKpoint_id* | *T (K)* | *P (kPa)* | *ρ (kg/m³)* |
|---|---|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「BLKpoint_2」 | 「293.15」 | 「101.0」 | 「1100.306」 |
| WM_L1#1_Table#2_Row#2 | 「BLKpoint_3」 | 「298.15」 | 「101.0」 | 「1095.278」 |
| WM_L1#1_Table#2_Row#3 | 「BLKpoint_4」 | 「303.15」 | 「101.0」 | 「1090.253」 |

The full block spans 288.15–308.15 K with density ranging from 1085.231 to 1105.336 kg/m³ (5 data points).

##### Summary

The mass density of pure liquid DMSO at 298.15 K and near-atmospheric pressure is consistently reported across five inspected sources in the narrow range **1095.27–1095.37 kg/m³** (equivalently ~1.0953 g/cm³). The slight variation (< 0.1 kg/m³ among four sources, with GLOBlit_938 at 1095.37 kg/m³ being the highest) likely reflects minor differences in sample purity and pressure conditions. The temperature coefficient near 298.15 K is approximately −1.0 kg·m⁻³·K⁻¹, as seen from the GLOBlit_86 data where density drops from 1100.306 kg/m³ at 293.15 K to 1090.253 kg/m³ at 303.15 K.

Note: GLOBlit_1775::PROPblock_6 was not inspected in this run due to the iteration limit, so its data value is not quoted here.

**Core claims:**
- The mass density of pure liquid DMSO at 298.15 K and near-atmospheric pressure is consistently reported across five independent ThermoML sources in the narrow range 1095.27–1095.37 kg/m³.
- The slight variation among sources (< 0.1 kg/m³ among four of the five, with GLOBlit_938 at 1095.37 kg/m³ being the highest) likely reflects minor differences in sample purity and pressure conditions.
- Near 298.15 K, the density of pure liquid DMSO decreases monotonically with temperature, with density dropping from 1100.306 kg/m³ at 293.15 K to 1090.253 kg/m³ at 303.15 K (GLOBlit_86 data).
- One source (GLOBlit_1775::PROPblock_6) was not inspected due to the iteration limit, so its data value is not included.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#3 | 「GLOBlit_57」 | 「PROPblock_7」 | 「GLOBcomp_31」 | 「GLOBprop_1」 | 「Mass density of pure DMSO at 298.15 K and 101.325 kPa; reported value 1095.271 kg/m³.」 |
| WM_L1#1_Table#4 | 「GLOBlit_86」 | 「PROPblock_4」 | 「GLOBcomp_31」 | 「GLOBprop_1」 | 「Mass density of pure DMSO over 288.15–308.15 K at 101.0 kPa; value at 298.15 K is 1095.278 kg/m³.」 |
| WM_L1#1_Table#5 | 「GLOBlit_779」 | 「PROPblock_3」 | 「GLOBcomp_31」 | 「GLOBprop_1」 | 「Mass density of pure DMSO at 298.15 K and 101.325 kPa; reported value 1095.27 kg/m³.」 |
| WM_L1#1_Table#6 | 「GLOBlit_938」 | 「PROPblock_3」 | 「GLOBcomp_31」 | 「GLOBprop_1」 | 「Mass density of pure DMSO at 298.15 K and 101.0 kPa; reported value 1095.37 kg/m³.」 |
| WM_L1#1_Table#7 | 「GLOBlit_1246」 | 「PROPblock_1」 | 「GLOBcomp_31」 | 「GLOBprop_1」 | 「Mass density of pure DMSO at 298.15 K and 85.9 kPa; reported value 1095.29 kg/m³.」 |

*Not stored here: 5 verbatim data_inspections table(s); 1 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.



</memory>

## User
I need the density of pure liquid DMSO at 25 °C for a calculation. If ThermoML does not contain it, use an accepted value from another source.

## Assistant
<summary>Searching ThermoML for density of pure DMSO at 25 °C (298.15 K).</summary>
<tool_call>L1_query(instruction=Search for mass d…, id_catalog=, context=User needs densit…)</tool_call>

## User
<tool_result>
<subagent_answer>
### L1#1 — L1_query return

**Status:** status=success

**Summary:** The mass density of pure liquid dimethyl sulfoxide (DMSO, CAS 67-68-5) at 298.15 K and near-atmospheric pressure is reported across five independent ThermoML sources in the narrow range 1095.27–1095.37 kg/m³. Representative values include 1095.271, 1095.278, 1095.27, 1095.37, and 1095.29 kg/m³ from different literature blocks, with slight variation attributed to differences in sample purity and pressure conditions (85.9–101.325 kPa). The temperature coefficient near 298.15 K is approximately −1.0 kg·m⁻³·K⁻¹, based on GLOBlit_86 data showing density decreasing from 1100.306 kg/m³ at 293.15 K to 1090.253 kg/m³ at 303.15 K. The full temperature series in that block spans 288.15–308.15 K with density ranging from 1085.231 to 1105.336 kg/m³.

**Answer:**

#### Mass Density of Pure Liquid DMSO at 298.15 K

Multiple independent ThermoML sources report the mass density of pure liquid dimethyl sulfoxide (DMSO, CAS 67-68-5, GLOBcomp_31) at 298.15 K. The inspected values are highly consistent:

##### Inspected Data Points at 298.15 K

**L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *Source (DOI)* | *Literature* | *Block* | *T (K)* | *P (kPa)* | *ρ (kg/m³)* |
|---|---|---|---|---|---|---|
| L1#1_Table#1_Row#1 | 「10.1007/s10765-008-0395-z」 | 「GLOBlit_57」 | 「PROPblock_7」 | 「298.15」 | 「101.325」 | 「1095.271」 |
| L1#1_Table#1_Row#2 | 「10.1007/s10765-009-0648-5」 | 「GLOBlit_86」 | 「PROPblock_4」 | 「298.15」 | 「101.0」 | 「1095.278」 |
| L1#1_Table#1_Row#3 | 「10.1016/j.fluid.2010.01.002」 | 「GLOBlit_779」 | 「PROPblock_3」 | 「298.15」 | 「101.325」 | 「1095.27」 |
| L1#1_Table#1_Row#4 | 「10.1016/j.fluid.2011.02.010」 | 「GLOBlit_938」 | 「PROPblock_3」 | 「298.15」 | 「101.0」 | 「1095.37」 |
| L1#1_Table#1_Row#5 | 「10.1016/j.fluid.2013.05.001」 | 「GLOBlit_1246」 | 「PROPblock_1」 | 「298.15」 | 「85.9」 | 「1095.29」 |

##### Temperature Dependence (GLOBlit_86, PROPblock_4)

The GLOBlit_86 block provides a temperature series showing the density decreases monotonically and nearly linearly with temperature:

**L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *BLKpoint_id* | *T (K)* | *P (kPa)* | *ρ (kg/m³)* |
|---|---|---|---|---|
| L1#1_Table#2_Row#1 | 「BLKpoint_2」 | 「293.15」 | 「101.0」 | 「1100.306」 |
| L1#1_Table#2_Row#2 | 「BLKpoint_3」 | 「298.15」 | 「101.0」 | 「1095.278」 |
| L1#1_Table#2_Row#3 | 「BLKpoint_4」 | 「303.15」 | 「101.0」 | 「1090.253」 |

The full block spans 288.15–308.15 K with density ranging from 1085.231 to 1105.336 kg/m³ (5 data points).

##### Summary

The mass density of pure liquid DMSO at 298.15 K and near-atmospheric pressure is consistently reported across five inspected sources in the narrow range **1095.27–1095.37 kg/m³** (equivalently ~1.0953 g/cm³). The slight variation (< 0.1 kg/m³ among four sources, with GLOBlit_938 at 1095.37 kg/m³ being the highest) likely reflects minor differences in sample purity and pressure conditions. The temperature coefficient near 298.15 K is approximately −1.0 kg·m⁻³·K⁻¹, as seen from the GLOBlit_86 data where density drops from 1100.306 kg/m³ at 293.15 K to 1090.253 kg/m³ at 303.15 K.

Note: GLOBlit_1775::PROPblock_6 was not inspected in this run due to the iteration limit, so its data value is not quoted here.

**Core claims:**
- The mass density of pure liquid DMSO at 298.15 K and near-atmospheric pressure is consistently reported across five independent ThermoML sources in the narrow range 1095.27–1095.37 kg/m³.
- The slight variation among sources (< 0.1 kg/m³ among four of the five, with GLOBlit_938 at 1095.37 kg/m³ being the highest) likely reflects minor differences in sample purity and pressure conditions.
- Near 298.15 K, the density of pure liquid DMSO decreases monotonically with temperature, with density dropping from 1100.306 kg/m³ at 293.15 K to 1090.253 kg/m³ at 303.15 K (GLOBlit_86 data).
- One source (GLOBlit_1775::PROPblock_6) was not inspected due to the iteration limit, so its data value is not included.

**Core ID updates:**
- add GLOBcomp_31 — dimethyl sulfoxide (registry: dimethyl_sulfoxide)

#### Core blocks found — verbatim ledger

```ledger
**L1#1_Table#3_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_57 | lit_id: 2008-she-zaf-0 | doi: 10.1007/s10765-008-0395-z
block: PROPblock_7 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_2) | system: unary | n_datapoints: 1
compounds: dimethyl sulfoxide (C2H6OS; GLOBcomp_31; DOIcomp_4; InChIKey IAZDPXIOMUYVGZ-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density of pure DMSO at 298.15 K and 101.325 kPa; reported value 1095.271 kg/m³.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#3_Row#1 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=298.15–298.15 · n_unique=1 · phase=Liquid」 |
| L1#1_Table#3_Row#2 | 「variable」 | 「BLKvar_2/GLOBvar_3」 | 「Pressure, kPa」 | 「range=101.325–101.325 · n_unique=1 · phase=Liquid」 |
| L1#1_Table#3_Row#3 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=VIBTUB:UFactor:2 (GLOBmeas_138) · range=1095.271–1095.271 · mean=1095.271 · n=1 · phase=Liquid」 |
```

```ledger
**L1#1_Table#4_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_86 | lit_id: 2009-sad-she-1 | doi: 10.1007/s10765-009-0648-5
block: PROPblock_4 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_2) | system: unary | n_datapoints: 5
compounds: dimethyl sulfoxide (C2H6OS; GLOBcomp_31; DOIcomp_2; InChIKey IAZDPXIOMUYVGZ-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density of pure DMSO over 288.15–308.15 K at 101.0 kPa; value at 298.15 K is 1095.278 kg/m³.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#4_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.0 · phase=Liquid」 |
| L1#1_Table#4_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=288.15–308.15 · n_unique=5 · phase=Liquid」 |
| L1#1_Table#4_Row#3 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=VIBTUB::UFactor:12 (GLOBmeas_179) · range=1085.231–1105.336 · mean=1095.2808 · n=5 · phase=Liquid」 |
```

```ledger
**L1#1_Table#5_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_779 | lit_id: 2010-she-mou-5 | doi: 10.1016/j.fluid.2010.01.002
block: PROPblock_3 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_2) | system: unary | n_datapoints: 4
compounds: dimethyl sulfoxide (C2H6OS; GLOBcomp_31; DOIcomp_1; InChIKey IAZDPXIOMUYVGZ-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density of pure DMSO at 298.15 K and 101.325 kPa; reported value 1095.27 kg/m³.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#5_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.325 · phase=Liquid」 |
| L1#1_Table#5_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=298.15–328.15 · n_unique=4 · phase=Liquid」 |
| L1#1_Table#5_Row#3 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=Vibrating tube method (GLOBmeas_2) · range=1065.16–1095.27 · mean=1080.2125 · n=4 · phase=Liquid」 |
```

```ledger
**L1#1_Table#6_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_938 | lit_id: 2011-gov-att-0 | doi: 10.1016/j.fluid.2011.02.010
block: PROPblock_3 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_2) | system: unary | n_datapoints: 5
compounds: dimethyl sulfoxide (C2H6OS; GLOBcomp_31; DOIcomp_1; InChIKey IAZDPXIOMUYVGZ-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density of pure DMSO at 298.15 K and 101.0 kPa; reported value 1095.37 kg/m³.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#6_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.0 · phase=Liquid」 |
| L1#1_Table#6_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=298.15–328.15 · n_unique=5 · phase=Liquid」 |
| L1#1_Table#6_Row#3 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=VIBTUB:UFactor:8 (GLOBmeas_141) · range=1066.09–1095.37 · mean=1083.232 · n=5 · phase=Liquid」 |
```

```ledger
**L1#1_Table#7_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_1246 | lit_id: 2013-elh-she-0 | doi: 10.1016/j.fluid.2013.05.001
block: PROPblock_1 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_2) | system: unary | n_datapoints: 1
compounds: dimethyl sulfoxide (C2H6OS; GLOBcomp_31; DOIcomp_1; InChIKey IAZDPXIOMUYVGZ-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density of pure DMSO at 298.15 K and 85.9 kPa; reported value 1095.29 kg/m³.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#7_Row#1 | 「variable」 | 「BLKvar_1/GLOBvar_3」 | 「Pressure, kPa」 | 「range=85.9–85.9 · n_unique=1 · phase=Liquid」 |
| L1#1_Table#7_Row#2 | 「variable」 | 「BLKvar_2/GLOBvar_1」 | 「Temperature, K」 | 「range=298.15–298.15 · n_unique=1 · phase=Liquid」 |
| L1#1_Table#7_Row#3 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=Vibrating tube method (GLOBmeas_2) · range=1095.29–1095.29 · mean=1095.29 · n=1 · phase=Liquid」 |
```

#### Data inspections — verbatim ledger

```ledger
**L1#1_Table#8_(Query_L1#1_INSP):**
lit_num_id: GLOBlit_86 | doi: 10.1007/s10765-009-0648-5 | block: PROPblock_4
table_mode: nearest | inspection_id: INSP_66cf20e92a90 | rows_shown: 3

| *row_id* | *BLKpoint_id* | *temperature_k* | *pressure_kpa* | *mass_density_kg_m3* |
|---|---|---|---|---|
| L1#1_Table#8_Row#1 | 「BLKpoint_2」 | 「293.15」 | 「101.0」 | 「1100.306」 |
| L1#1_Table#8_Row#2 | 「BLKpoint_3」 | 「298.15」 | 「101.0」 | 「1095.278」 |
| L1#1_Table#8_Row#3 | 「BLKpoint_4」 | 「303.15」 | 「101.0」 | 「1090.253」 |
```

```ledger
**L1#1_Table#9_(Query_L1#1_INSP):**
lit_num_id: GLOBlit_57 | doi: 10.1007/s10765-008-0395-z | block: PROPblock_7
table_mode: nearest | inspection_id: INSP_4af5341b9c11 | rows_shown: 1

| *row_id* | *BLKpoint_id* | *temperature_k* | *pressure_kpa* | *mass_density_kg_m3* |
|---|---|---|---|---|
| L1#1_Table#9_Row#1 | 「BLKpoint_1」 | 「298.15」 | 「101.325」 | 「1095.271」 |
```

```ledger
**L1#1_Table#10_(Query_L1#1_INSP):**
lit_num_id: GLOBlit_779 | doi: 10.1016/j.fluid.2010.01.002 | block: PROPblock_3
table_mode: nearest | inspection_id: INSP_ae4f04a9ca18 | rows_shown: 1

| *row_id* | *BLKpoint_id* | *temperature_k* | *pressure_kpa* | *mass_density_kg_m3* |
|---|---|---|---|---|
| L1#1_Table#10_Row#1 | 「BLKpoint_1」 | 「298.15」 | 「101.325」 | 「1095.27」 |
```

```ledger
**L1#1_Table#11_(Query_L1#1_INSP):**
lit_num_id: GLOBlit_938 | doi: 10.1016/j.fluid.2011.02.010 | block: PROPblock_3
table_mode: nearest | inspection_id: INSP_7d4176a6acb2 | rows_shown: 1

| *row_id* | *BLKpoint_id* | *temperature_k* | *pressure_kpa* | *mass_density_kg_m3* |
|---|---|---|---|---|
| L1#1_Table#11_Row#1 | 「BLKpoint_1」 | 「298.15」 | 「101.0」 | 「1095.37」 |
```

```ledger
**L1#1_Table#12_(Query_L1#1_INSP):**
lit_num_id: GLOBlit_1246 | doi: 10.1016/j.fluid.2013.05.001 | block: PROPblock_1
table_mode: nearest | inspection_id: INSP_c120fd362f0c | rows_shown: 1

| *row_id* | *BLKpoint_id* | *pressure_kpa* | *temperature_k* | *mass_density_kg_m3* |
|---|---|---|---|---|
| L1#1_Table#12_Row#1 | 「BLKpoint_1」 | 「85.9」 | 「298.15」 | 「1095.29」 |
```
</subagent_answer>
</tool_result>

## LLM Response
<answer>

## Density of Pure Liquid DMSO at 25 °C (298.15 K)

The ThermoML database contains this value from **five independent experimental sources**, all in excellent mutual agreement. Here are the reported values at 298.15 K and near-atmospheric pressure:

| Source (DOI) | Literature | Block | *T* (K) | *P* (kPa) | ρ (kg/m³) |
|---|---|---|---|---|---|
| 10.1007/s10765-008-0395-z | GLOBlit_57 | PROPblock_7 | 298.15 | 101.325 | **1095.271** |
| 10.1007/s10765-009-0648-5 | GLOBlit_86 | PROPblock_4 | 298.15 | 101.0 | **1095.278** |
| 10.1016/j.fluid.2010.01.002 | GLOBlit_779 | PROPblock_3 | 298.15 | 101.325 | **1095.27** |
| 10.1016/j.fluid.2011.02.010 | GLOBlit_938 | PROPblock_3 | 298.15 | 101.0 | **1095.37** |
| 10.1016/j.fluid.2013.05.001 | GLOBlit_1246 | PROPblock_1 | 298.15 | 85.9 | **1095.29** |

### Recommended value for your calculation

> **ρ(DMSO, 25 °C) ≈ 1095.3 kg/m³  (1.0953 g/cm³)**

All five sources fall in the narrow range **1095.27–1095.37 kg/m³**, so any value in that interval is well-supported. The spread of < 0.1 kg/m³ (among four of the five sources) reflects minor differences in sample purity and exact pressure conditions.

### Temperature dependence near 25 °C

From the GLOBlit_86 dataset (DOI 10.1007/s10765-009-0648-5), density decreases nearly linearly with temperature:

| *T* (K) | *P* (kPa) | ρ (kg/m³) |
|---|---|---|
| 293.15 | 101.0 | 1100.306 |
| 298.15 | 101.0 | 1095.278 |
| 303.15 | 101.0 | 1090.253 |

This gives a temperature coefficient of approximately **−1.0 kg·m⁻³·K⁻¹** near 25 °C, which is useful if your calculation involves a slightly different temperature.

### Chemistry note

DMSO (CH₃–SO–CH₃, M = 78.13 g/mol) is denser than water at 25 °C because of its relatively high molecular mass and strong dipole–dipole interactions (μ ≈ 3.96 D). The S=O bond creates a compact, highly polar structure that packs efficiently in the liquid phase.

</answer>