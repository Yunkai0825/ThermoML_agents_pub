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
| comp | GLOBcomp_6 | propan-2-ol | propan-2-ol |
| comp | GLOBcomp_1 | water | water |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find mass density data for equimolar propan-2-ol + water liquid mixture at 25 °C and atmospheric pressure → stored as L1_query_1 · validation: PASS

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: PASS

**Summary:** The mass density of a binary liquid mixture of propan-2-ol and water at 298.15 K and 101.0 kPa was reported from DOI 10.1021/je700700f (GLOBlit_11042, PROPblock_17). At the nearest-to-equimolar composition of x(propan-2-ol) = 0.4981, the mass density is 838.8 kg/m³. Density decreases monotonically with increasing propan-2-ol mole fraction, from 997.2 kg/m³ for pure water to 780.7 kg/m³ for pure propan-2-ol. The dataset comprises 13 data points spanning the full mole-fraction range. The system exhibits negative excess volumes (volume contraction on mixing), especially in the water-rich region, attributed to strong hydrogen-bonding interactions.

**Answer:**

#### Mass Density of Equimolar Propan-2-ol + Water at 25 °C and Atmospheric Pressure

A binary liquid mixture of propan-2-ol (isopropanol, GLOBcomp_6) and water (GLOBcomp_1) has been measured for mass density at 298.15 K and 101 kPa (atmospheric pressure) across the full mole-fraction range.

##### Data at Near-Equimolar Composition

From the dataset reported by Soliman and Marschall (DOI: 10.1021/je700700f, GLOBlit_11042, PROPblock_17), the following density values bracket the equimolar composition:

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *Mole fraction of propan-2-ol* | *Temperature (K)* | *Pressure (kPa)* | *Mass density (kg/m³)* |
|---|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「0.3992」 | 「298.15」 | 「101.0」 | 「857.7」 |
| WM_L1#1_Table#1_Row#2 | 「**0.4981**」 | 「**298.15**」 | 「**101.0**」 | 「**838.8**」 |
| WM_L1#1_Table#1_Row#3 | 「0.5979」 | 「298.15」 | 「101.0」 | 「823.5」 |

The closest measurement to equimolar (x = 0.5) is at **x(propan-2-ol) = 0.4981**, where the mass density is **838.8 kg/m³** at 298.15 K and 101.0 kPa. There is no data point at exactly x = 0.5; the nearest recorded compositions bracket it at 0.4981 (below) and 0.5979 (above).

##### Chemical Insight

The density decreases monotonically with increasing propan-2-ol mole fraction across the full composition range (from 997.2 kg/m³ for pure water to 780.7 kg/m³ for pure propan-2-ol at 298.15 K). At the near-equimolar composition, the density (838.8 kg/m³) is closer to that of pure propan-2-ol than to pure water, reflecting the significant contribution of the lighter, bulkier alcohol molecules to the mixture volume. This system is well known for exhibiting negative excess volumes (volume contraction on mixing), particularly in the water-rich region, due to strong hydrogen-bonding interactions between propan-2-ol and water.

**Source:** DOI 10.1021/je700700f (GLOBlit_11042, PROPblock_17) — 13 data points covering x(propan-2-ol) = 0 to 1 at 298.15 K and 101.0 kPa.

**Core claims:**
- At x(propan-2-ol) = 0.4981 (the nearest measured composition to equimolar), the mass density of the propan-2-ol + water binary mixture is 838.8 kg/m³ at 298.15 K and 101.0 kPa, as reported by Soliman and Marschall (DOI: 10.1021/je700700f).
- The mass density of the propan-2-ol + water mixture decreases monotonically with increasing propan-2-ol mole fraction across the full composition range, from 997.2 kg/m³ for pure water to 780.7 kg/m³ for pure propan-2-ol at 298.15 K.
- No data point exists at exactly x(propan-2-ol) = 0.5; the nearest recorded compositions bracket it at 0.4981 and 0.5979.
- The propan-2-ol + water system is known to exhibit negative excess volumes (volume contraction on mixing), particularly in the water-rich region, attributed to strong hydrogen-bonding interactions.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#2 | 「GLOBlit_11042」 | 「PROPblock_17」 | 「GLOBcomp_6, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density measurements for propan-2-ol + water binary mixture at 298.15 K and 101.0 kPa across the full mole-fraction range.」 |

*Not stored here: 1 verbatim data_inspections table(s); 2 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.



</memory>

## User
What density has been measured for an equimolar propan-2-ol + water liquid mixture at 25 °C and atmospheric pressure?

## Assistant
<summary>Searching for density (GLOBprop_1) data for propan-2-ol + water binary mixture at 298.15 K, focusing on equimolar composition (x = 0.5).</summary>
<tool_call>L1_query(instruction=Search for mass d…)</tool_call>

## User
<tool_result>
<subagent_answer>
### L1#1 — L1_query return

**Status:** status=success

**Summary:** The mass density of a binary liquid mixture of propan-2-ol and water at 298.15 K and 101.0 kPa was reported from DOI 10.1021/je700700f (GLOBlit_11042, PROPblock_17). At the nearest-to-equimolar composition of x(propan-2-ol) = 0.4981, the mass density is 838.8 kg/m³. Density decreases monotonically with increasing propan-2-ol mole fraction, from 997.2 kg/m³ for pure water to 780.7 kg/m³ for pure propan-2-ol. The dataset comprises 13 data points spanning the full mole-fraction range. The system exhibits negative excess volumes (volume contraction on mixing), especially in the water-rich region, attributed to strong hydrogen-bonding interactions.

**Answer:**

#### Mass Density of Equimolar Propan-2-ol + Water at 25 °C and Atmospheric Pressure

A binary liquid mixture of propan-2-ol (isopropanol, GLOBcomp_6) and water (GLOBcomp_1) has been measured for mass density at 298.15 K and 101 kPa (atmospheric pressure) across the full mole-fraction range.

##### Data at Near-Equimolar Composition

From the dataset reported by Soliman and Marschall (DOI: 10.1021/je700700f, GLOBlit_11042, PROPblock_17), the following density values bracket the equimolar composition:

**L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *Mole fraction of propan-2-ol* | *Temperature (K)* | *Pressure (kPa)* | *Mass density (kg/m³)* |
|---|---|---|---|---|
| L1#1_Table#1_Row#1 | 「0.3992」 | 「298.15」 | 「101.0」 | 「857.7」 |
| L1#1_Table#1_Row#2 | 「**0.4981**」 | 「**298.15**」 | 「**101.0**」 | 「**838.8**」 |
| L1#1_Table#1_Row#3 | 「0.5979」 | 「298.15」 | 「101.0」 | 「823.5」 |

The closest measurement to equimolar (x = 0.5) is at **x(propan-2-ol) = 0.4981**, where the mass density is **838.8 kg/m³** at 298.15 K and 101.0 kPa. There is no data point at exactly x = 0.5; the nearest recorded compositions bracket it at 0.4981 (below) and 0.5979 (above).

##### Chemical Insight

The density decreases monotonically with increasing propan-2-ol mole fraction across the full composition range (from 997.2 kg/m³ for pure water to 780.7 kg/m³ for pure propan-2-ol at 298.15 K). At the near-equimolar composition, the density (838.8 kg/m³) is closer to that of pure propan-2-ol than to pure water, reflecting the significant contribution of the lighter, bulkier alcohol molecules to the mixture volume. This system is well known for exhibiting negative excess volumes (volume contraction on mixing), particularly in the water-rich region, due to strong hydrogen-bonding interactions between propan-2-ol and water.

**Source:** DOI 10.1021/je700700f (GLOBlit_11042, PROPblock_17) — 13 data points covering x(propan-2-ol) = 0 to 1 at 298.15 K and 101.0 kPa.

**Core claims:**
- At x(propan-2-ol) = 0.4981 (the nearest measured composition to equimolar), the mass density of the propan-2-ol + water binary mixture is 838.8 kg/m³ at 298.15 K and 101.0 kPa, as reported by Soliman and Marschall (DOI: 10.1021/je700700f).
- The mass density of the propan-2-ol + water mixture decreases monotonically with increasing propan-2-ol mole fraction across the full composition range, from 997.2 kg/m³ for pure water to 780.7 kg/m³ for pure propan-2-ol at 298.15 K.
- No data point exists at exactly x(propan-2-ol) = 0.5; the nearest recorded compositions bracket it at 0.4981 and 0.5979.
- The propan-2-ol + water system is known to exhibit negative excess volumes (volume contraction on mixing), particularly in the water-rich region, attributed to strong hydrogen-bonding interactions.

**Core ID updates:**
- add GLOBcomp_6 — propan-2-ol (registry: propan-2-ol)
- add GLOBcomp_1 — water (registry: water)

#### Core blocks found — verbatim ledger

```ledger
**L1#1_Table#2_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_11042 | lit_id: 2008-gon-cal-0 | doi: 10.1021/je700700f
block: PROPblock_17 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 13
compounds: propan-2-ol (C3H8O; GLOBcomp_6; DOIcomp_2; InChIKey KFZMGEQAYNKOFK-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_3; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density measurements for propan-2-ol + water binary mixture at 298.15 K and 101.0 kPa across the full mole-fraction range.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#2_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.0 · phase=Liquid」 |
| L1#1_Table#2_Row#2 | 「constraint」 | 「BLKconstr_2/GLOBconstr_2」 | 「Temperature, K」 | 「value=298.15 · phase=Liquid」 |
| L1#1_Table#2_Row#3 | 「variable」 | 「BLKvar_1/GLOBvar_2」 | 「Mole fraction of propan-2-ol」 | 「range=0.0–1.0 · n_unique=13 · phase=Liquid」 |
| L1#1_Table#2_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=VIBTUB:UFactor:4 (GLOBmeas_134) · range=780.7–997.2 · mean=861.961538 · n=13 · phase=Liquid」 |
```

#### Data inspections — verbatim ledger

```ledger
**L1#1_Table#3_(Query_L1#1_INSP):**
lit_num_id: GLOBlit_11042 | doi: 10.1021/je700700f | block: PROPblock_17
table_mode: nearest | inspection_id: INSP_ca3d51c69341 | rows_shown: 3

| *row_id* | *BLKpoint_id* | *mole_fraction_<propan-2-ol>* | *pressure_kpa* | *temperature_k* | *mass_density_kg_m3* |
|---|---|---|---|---|---|
| L1#1_Table#3_Row#1 | 「BLKpoint_6」 | 「0.3992」 | 「101.0」 | 「298.15」 | 「857.7」 |
| L1#1_Table#3_Row#2 | 「BLKpoint_7」 | 「0.4981」 | 「101.0」 | 「298.15」 | 「838.8」 |
| L1#1_Table#3_Row#3 | 「BLKpoint_8」 | 「0.5979」 | 「101.0」 | 「298.15」 | 「823.5」 |
```
</subagent_answer>
</tool_result>

## LLM Response
<answer>

## Mass Density of Equimolar Propan-2-ol + Water at 25 °C and Atmospheric Pressure

The mass density of a binary liquid mixture of propan-2-ol (isopropanol) and water has been measured at 298.15 K (25 °C) and 101.0 kPa (atmospheric pressure) across the full mole-fraction range by Soliman and Marschall (DOI: 10.1021/je700700f, GLOBlit_11042).

### Data Near the Equimolar Composition

There is no data point at exactly x(propan-2-ol) = 0.5000, but the nearest measured composition is very close. The three points bracketing the equimolar composition are:

| Mole fraction of propan-2-ol | Temperature (K) | Pressure (kPa) | Mass density (kg/m³) |
|:---:|:---:|:---:|:---:|
| 0.3992 | 298.15 | 101.0 | 857.7 |
| **0.4981** | **298.15** | **101.0** | **838.8** |
| 0.5979 | 298.15 | 101.0 | 823.5 |

**At the nearest-to-equimolar composition of x(propan-2-ol) = 0.4981, the mass density is 838.8 kg/m³** at 298.15 K and 101.0 kPa.

### Chemical Context

- The density decreases monotonically with increasing propan-2-ol mole fraction, from 997.2 kg/m³ for pure water down to 780.7 kg/m³ for pure propan-2-ol at 298.15 K.
- At the near-equimolar composition, the density (838.8 kg/m³) is notably closer to that of pure propan-2-ol (780.7 kg/m³) than to pure water (997.2 kg/m³). This reflects the significant contribution of the lighter, bulkier alcohol molecules to the mixture volume.
- The propan-2-ol + water system is well known for exhibiting **negative excess volumes** (volume contraction on mixing), particularly in the water-rich region, due to strong hydrogen-bonding interactions between propan-2-ol and water molecules.

**Source:** DOI 10.1021/je700700f (GLOBlit_11042, PROPblock_17) — 13 data points covering x(propan-2-ol) = 0 to 1 at 298.15 K and 101.0 kPa.

</answer>