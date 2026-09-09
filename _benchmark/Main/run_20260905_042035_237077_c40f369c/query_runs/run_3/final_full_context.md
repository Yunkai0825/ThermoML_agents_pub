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

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find dynamic viscosity data for binary mixture methanol + ethanol near 303.15 K as a function of composition → stored as L1_query_1 · validation: PASS

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: PASS

**Summary:** Dynamic viscosity of the methanol + ethanol binary liquid mixture at 303.15 K and 81.5 kPa, measured by capillary tube (Ostwald–Ubbelohde), from DOI 10.1021/je800633a. Twelve data points span methanol mole fractions from 0.0417 to 0.9166, with viscosity decreasing monotonically from 0.000968 Pa·s (ethanol-rich end) to 0.000556 Pa·s (methanol-rich end). The near-linear decrease (R² = 0.9960) indicates relatively ideal mixing behavior with minimal excess viscosity effects, consistent with methanol's smaller molecular size and weaker hydrogen-bonding network compared to ethanol.

**Answer:**

#### Dynamic Viscosity of Methanol + Ethanol Binary Mixture at 303.15 K

##### Source
**DOI:** 10.1021/je800633a (GLOBlit_11337)
**Block:** PROPblock_16
**Measurement method:** Capillary tube (Ostwald–Ubbelohde)

##### System
- **Compounds:** Methanol (GLOBcomp_4) + Ethanol (GLOBcomp_2)
- **System type:** Binary, liquid phase
- **Temperature:** 303.15 K (fixed)
- **Pressure:** 81.5 kPa (fixed)

##### Viscosity vs. Mole Fraction of Methanol

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *x(methanol)* | *η (Pa·s)* |
|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「0.0417」 | 「0.000968」 |
| WM_L1#1_Table#1_Row#2 | 「0.1476」 | 「0.000906」 |
| WM_L1#1_Table#1_Row#3 | 「0.2214」 | 「0.000865」 |
| WM_L1#1_Table#1_Row#4 | 「0.2952」 | 「0.000828」 |
| WM_L1#1_Table#1_Row#5 | 「0.3644」 | 「0.000793」 |
| WM_L1#1_Table#1_Row#6 | 「0.4488」 | 「0.000753」 |
| WM_L1#1_Table#1_Row#7 | 「0.5290」 | 「0.000717」 |
| WM_L1#1_Table#1_Row#8 | 「0.5995」 | 「0.000685」 |
| WM_L1#1_Table#1_Row#9 | 「0.6859」 | 「0.000648」 |
| WM_L1#1_Table#1_Row#10 | 「0.7442」 | 「0.000624」 |
| WM_L1#1_Table#1_Row#11 | 「0.8320」 | 「0.000588」 |
| WM_L1#1_Table#1_Row#12 | 「0.9166」 | 「0.000556」 |

All 12 data points are shown. The composition range spans x(methanol) = 0.0417 to 0.9166, and the viscosity ranges from 0.000968 Pa·s (ethanol-rich end) down to 0.000556 Pa·s (methanol-rich end).

##### Chemical Insight
The viscosity decreases monotonically and nearly linearly (R² = 0.9960) as the methanol mole fraction increases. This is consistent with methanol's smaller molecular size and weaker intermolecular hydrogen-bonding network compared to ethanol, resulting in lower viscosity at the methanol-rich end. The near-linear dependence suggests relatively ideal mixing behavior with minimal excess viscosity effects in this system at 303.15 K.

**Core claims:**
- For the methanol + ethanol binary liquid mixture at 303.15 K and 81.5 kPa (DOI 10.1021/je800633a), dynamic viscosity decreases monotonically from 0.000968 Pa·s at x(methanol) = 0.0417 to 0.000556 Pa·s at x(methanol) = 0.9166 across 12 data points measured by capillary tube (Ostwald–Ubbelohde).
- The near-linear decrease in viscosity with increasing methanol mole fraction (R² = 0.9960) suggests relatively ideal mixing behavior with minimal excess viscosity effects, consistent with methanol's smaller molecular size and weaker hydrogen-bonding network compared to ethanol.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#2 | 「GLOBlit_11337」 | 「PROPblock_16」 | 「GLOBcomp_2, GLOBcomp_4」 | 「GLOBprop_4」 | 「Dynamic viscosity measurements for the binary mixture methanol + ethanol at 303.15 K and 81.5 kPa as a function of methanol mole fraction.」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.



</memory>

## User
[Purpose: Locate ThermoML viscosity data for methanol + ethanol near 30°C]
Find viscosity data for the binary mixture of methanol + ethanol at or near 30°C (303.15 K). I need dynamic viscosity as a function of composition (mole fraction). Return DOIs, block numbers, compound names, and any available data points.

[Context: Binary system: methanol (CH3OH) + ethanol (C2H5OH). Looking for dynamic viscosity vs composition data.]

## Assistant
<summary>Dispatching L1 query to find dynamic viscosity data for methanol + ethanol binary mixture near 303.15 K.</summary>
<tool_call>L1_query(instruction=Search for dynami…, id_catalog=GLOBprop_4 = Visc…, context=Binary s…)</tool_call>

## User
<tool_result>
<subagent_answer>
### L1#1 — L1_query return

**Status:** status=success

**Summary:** Dynamic viscosity of the methanol + ethanol binary liquid mixture at 303.15 K and 81.5 kPa, measured by capillary tube (Ostwald–Ubbelohde), from DOI 10.1021/je800633a. Twelve data points span methanol mole fractions from 0.0417 to 0.9166, with viscosity decreasing monotonically from 0.000968 Pa·s (ethanol-rich end) to 0.000556 Pa·s (methanol-rich end). The near-linear decrease (R² = 0.9960) indicates relatively ideal mixing behavior with minimal excess viscosity effects, consistent with methanol's smaller molecular size and weaker hydrogen-bonding network compared to ethanol.

**Answer:**

#### Dynamic Viscosity of Methanol + Ethanol Binary Mixture at 303.15 K

##### Source
**DOI:** 10.1021/je800633a (GLOBlit_11337)
**Block:** PROPblock_16
**Measurement method:** Capillary tube (Ostwald–Ubbelohde)

##### System
- **Compounds:** Methanol (GLOBcomp_4) + Ethanol (GLOBcomp_2)
- **System type:** Binary, liquid phase
- **Temperature:** 303.15 K (fixed)
- **Pressure:** 81.5 kPa (fixed)

##### Viscosity vs. Mole Fraction of Methanol

**L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *x(methanol)* | *η (Pa·s)* |
|---|---|---|
| L1#1_Table#1_Row#1 | 「0.0417」 | 「0.000968」 |
| L1#1_Table#1_Row#2 | 「0.1476」 | 「0.000906」 |
| L1#1_Table#1_Row#3 | 「0.2214」 | 「0.000865」 |
| L1#1_Table#1_Row#4 | 「0.2952」 | 「0.000828」 |
| L1#1_Table#1_Row#5 | 「0.3644」 | 「0.000793」 |
| L1#1_Table#1_Row#6 | 「0.4488」 | 「0.000753」 |
| L1#1_Table#1_Row#7 | 「0.5290」 | 「0.000717」 |
| L1#1_Table#1_Row#8 | 「0.5995」 | 「0.000685」 |
| L1#1_Table#1_Row#9 | 「0.6859」 | 「0.000648」 |
| L1#1_Table#1_Row#10 | 「0.7442」 | 「0.000624」 |
| L1#1_Table#1_Row#11 | 「0.8320」 | 「0.000588」 |
| L1#1_Table#1_Row#12 | 「0.9166」 | 「0.000556」 |

All 12 data points are shown. The composition range spans x(methanol) = 0.0417 to 0.9166, and the viscosity ranges from 0.000968 Pa·s (ethanol-rich end) down to 0.000556 Pa·s (methanol-rich end).

##### Chemical Insight
The viscosity decreases monotonically and nearly linearly (R² = 0.9960) as the methanol mole fraction increases. This is consistent with methanol's smaller molecular size and weaker intermolecular hydrogen-bonding network compared to ethanol, resulting in lower viscosity at the methanol-rich end. The near-linear dependence suggests relatively ideal mixing behavior with minimal excess viscosity effects in this system at 303.15 K.

**Core claims:**
- For the methanol + ethanol binary liquid mixture at 303.15 K and 81.5 kPa (DOI 10.1021/je800633a), dynamic viscosity decreases monotonically from 0.000968 Pa·s at x(methanol) = 0.0417 to 0.000556 Pa·s at x(methanol) = 0.9166 across 12 data points measured by capillary tube (Ostwald–Ubbelohde).
- The near-linear decrease in viscosity with increasing methanol mole fraction (R² = 0.9960) suggests relatively ideal mixing behavior with minimal excess viscosity effects, consistent with methanol's smaller molecular size and weaker hydrogen-bonding network compared to ethanol.

#### Core blocks found — verbatim ledger

```ledger
**L1#1_Table#2_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_11337 | lit_id: 2009-zar-mir-0 | doi: 10.1021/je800633a
block: PROPblock_16 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 12
compounds: ethanol (C2H6O; GLOBcomp_2; DOIcomp_1; InChIKey LFQSCWFLJHTTHZ-UHFFFAOYSA-N); methanol (CH4O; GLOBcomp_4; DOIcomp_3; InChIKey OKKJLVBELUTLKV-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_4
description: Dynamic viscosity measurements for the binary mixture methanol + ethanol at 303.15 K and 81.5 kPa as a function of methanol mole fraction.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#2_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_2」 | 「Temperature, K」 | 「value=303.15 · phase=Liquid」 |
| L1#1_Table#2_Row#2 | 「constraint」 | 「BLKconstr_2/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=81.5 · phase=Liquid」 |
| L1#1_Table#2_Row#3 | 「variable」 | 「BLKvar_1/GLOBvar_2」 | 「Mole fraction of methanol」 | 「range=0.0417–0.9166 · n_unique=12 · phase=Liquid」 |
| L1#1_Table#2_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_4」 | 「Viscosity, Pa*s」 | 「method=Capillary tube (Ostwald; Ubbelohde) method (GLOBmeas_4) · range=0.000556–0.000968 · mean=0.000744 · n=12 · phase=Liquid」 |
```

#### Data inspections — verbatim ledger

```ledger
**L1#1_Table#3_(Query_L1#1_INSP):**
lit_num_id: GLOBlit_11337 | doi: 10.1021/je800633a | block: PROPblock_16
table_mode: complete | inspection_id: INSP_e747e21118c7 | rows_shown: 12

| *row_id* | *BLKpoint_id* | *mole_fraction_<methanol>* | *temperature_k* | *pressure_kpa* | *viscosity_pa_s* |
|---|---|---|---|---|---|
| L1#1_Table#3_Row#1 | 「BLKpoint_1」 | 「0.0417」 | 「303.15」 | 「81.5」 | 「0.000968」 |
| L1#1_Table#3_Row#2 | 「BLKpoint_2」 | 「0.1476」 | 「303.15」 | 「81.5」 | 「0.000906」 |
| L1#1_Table#3_Row#3 | 「BLKpoint_3」 | 「0.2214」 | 「303.15」 | 「81.5」 | 「0.000865」 |
| L1#1_Table#3_Row#4 | 「BLKpoint_4」 | 「0.2952」 | 「303.15」 | 「81.5」 | 「0.000828」 |
| L1#1_Table#3_Row#5 | 「BLKpoint_5」 | 「0.3644」 | 「303.15」 | 「81.5」 | 「0.000793」 |
| L1#1_Table#3_Row#6 | 「BLKpoint_6」 | 「0.4488」 | 「303.15」 | 「81.5」 | 「0.000753」 |
| L1#1_Table#3_Row#7 | 「BLKpoint_7」 | 「0.529」 | 「303.15」 | 「81.5」 | 「0.000717」 |
| L1#1_Table#3_Row#8 | 「BLKpoint_8」 | 「0.5995」 | 「303.15」 | 「81.5」 | 「0.000685」 |
| L1#1_Table#3_Row#9 | 「BLKpoint_9」 | 「0.6859」 | 「303.15」 | 「81.5」 | 「0.000648」 |
| L1#1_Table#3_Row#10 | 「BLKpoint_10」 | 「0.7442」 | 「303.15」 | 「81.5」 | 「0.000624」 |
| L1#1_Table#3_Row#11 | 「BLKpoint_11」 | 「0.832」 | 「303.15」 | 「81.5」 | 「0.000588」 |
| L1#1_Table#3_Row#12 | 「BLKpoint_12」 | 「0.9166」 | 「303.15」 | 「81.5」 | 「0.000556」 |
```
</subagent_answer>
</tool_result>

## LLM Response
<reasoning>
The L1 query returned comprehensive data. The results match what was already in working memory from a previous query. I have all the information needed to provide a complete answer to the user.
</reasoning>

<answer>

## Dynamic Viscosity of Methanol + Ethanol Binary Mixture at 303.15 K

### Source

- **DOI:** 10.1021/je800633a
- **Block:** PROPblock_16
- **Measurement method:** Capillary tube (Ostwald–Ubbelohde)

### System Details

| Parameter | Value |
|-----------|-------|
| **Compounds** | Methanol (CH₄O) + Ethanol (C₂H₆O) |
| **System type** | Binary liquid mixture |
| **Temperature** | 303.15 K (≈ 30 °C), fixed |
| **Pressure** | 81.5 kPa, fixed |

### Viscosity vs. Mole Fraction of Methanol

Twelve data points spanning the composition range:

| x(methanol) | η (Pa·s) |
|:-----------:|:---------:|
| 0.0417 | 0.000968 |
| 0.1476 | 0.000906 |
| 0.2214 | 0.000865 |
| 0.2952 | 0.000828 |
| 0.3644 | 0.000793 |
| 0.4488 | 0.000753 |
| 0.529  | 0.000717 |
| 0.5995 | 0.000685 |
| 0.6859 | 0.000648 |
| 0.7442 | 0.000624 |
| 0.832  | 0.000588 |
| 0.9166 | 0.000556 |

### Chemical Insight

The dynamic viscosity decreases monotonically from 0.000968 Pa·s at the ethanol-rich end (x(methanol) = 0.0417) to 0.000556 Pa·s at the methanol-rich end (x(methanol) = 0.9166). The decrease is nearly linear with composition, indicating relatively ideal mixing behavior with minimal excess viscosity effects in this system at 303.15 K.

This behavior is consistent with the molecular similarity of methanol and ethanol — both are small, linear aliphatic alcohols capable of hydrogen bonding. Methanol, being smaller (one carbon vs. two), has weaker van der Waals interactions and a less extensive hydrogen-bonding network, leading to its lower pure-component viscosity. The near-ideal mixing arises because the two components are structurally and chemically similar, so replacing ethanol molecules with methanol molecules in the mixture smoothly reduces the average intermolecular interaction strength without introducing significant structural disruption or preferential association.

</answer>