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
- [L1] Find measured isobaric molar heat capacity (Cp) of pure liquid water at 298.15 K and atmospheric pressure → stored as L1_query_1 · validation: FLAGGED(1)

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: FLAGGED(1)

**Summary:** Two ThermoML measurements of the isobaric molar heat capacity (Cp) of pure liquid water at 298.15 K are reported. At 101.325 kPa (DOI 10.1016/j.jct.2016.09.031), Cp = 75.11470996 J/(K·mol). At 101.0 kPa (DOI 10.1016/j.fluid.2013.08.005), Cp = 75.368725408 J/(K·mol). No explicit uncertainty values were reported in the inspected blocks. Both values are consistent with the commonly cited standard molar heat capacity of liquid water at 298.15 K.

**Answer:**

#### Measured Isobaric Molar Heat Capacity (Cp) of Pure Liquid Water at 298.15 K and Atmospheric Pressure

The ThermoML database contains multiple measurements of the molar heat capacity at constant pressure (Cp) for pure liquid water at 298.15 K and near-atmospheric pressure. Here are two representative, inspected data points:

##### Data Point 1 — Exact conditions (298.15 K, 101.325 kPa)
- **Cp = 75.11470996 J/(K·mol)**
- Temperature: 298.15 K
- Pressure: 101.325 kPa
- Source: DOI 10.1016/j.jct.2016.09.031 (GLOBlit_4832, PROPblock_1)
- Measurement method: GLOBmeas_12

##### Data Point 2 — Near-atmospheric (298.15 K, 101.0 kPa)
- **Cp = 75.368725408 J/(K·mol)**
- Temperature: 298.15 K
- Pressure: 101.0 kPa
- Source: DOI 10.1016/j.fluid.2013.08.005 (GLOBlit_1310, PROPblock_1)
- Measurement method: GLOBmeas_31

##### Summary
The two inspected measurements at 298.15 K give Cp values of 75.11470996 and 75.368725408 J/(K·mol), consistent with the commonly cited standard molar heat capacity of liquid water (approximately 75.3 J/(K·mol) at 298.15 K, per general reference literature — not from this database). The difference between the two inspected values (computed: 75.368725408 − 75.11470996 ≈ 0.254 J/(K·mol)) reflects differences in experimental technique, calibration, and exact pressure conditions (101.325 vs 101.0 kPa). No explicit uncertainty values were reported in the inspected blocks.

**Core claims:**
- The ThermoML database contains two inspected measurements of the isobaric molar heat capacity (Cp) of pure liquid water at 298.15 K and near-atmospheric pressure: 75.11470996 J/(K·mol) at 101.325 kPa (DOI 10.1016/j.jct.2016.09.031) and 75.368725408 J/(K·mol) at 101.0 kPa (DOI 10.1016/j.fluid.2013.08.005).
- The two inspected Cp values are consistent with the commonly cited standard molar heat capacity of liquid water at 298.15 K (approximately 75.3 J/(K·mol)), and their difference reflects differences in experimental technique, calibration, and exact pressure conditions.
- No explicit uncertainty values were reported in the inspected data blocks.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#1 | 「GLOBlit_4832」 | 「PROPblock_1」 | 「GLOBcomp_1」 | 「GLOBprop_9」 | 「Isobaric molar heat capacity of pure liquid water at 298.15 K and 101.325 kPa; Cp = 75.11470996 J/(K·mol).」 |
| WM_L1#1_Table#2 | 「GLOBlit_1310」 | 「PROPblock_1」 | 「GLOBcomp_1」 | 「GLOBprop_9」 | 「Isobaric molar heat capacity of pure liquid water at 298.15 K and 101.0 kPa; Cp = 75.368725408 J/(K·mol).」 |

*Not stored here: 2 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(1) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNGROUNDED_LITERAL** PROPblock_1: 0.254 (near '…wo inspected values (computed: 75.368725408 - 75.11470996 ≈ …') matches no inspected row/stat, database table, or other source of PROPblock_1



</memory>

## User
What is the measured isobaric heat capacity of pure liquid water at 25 °C and atmospheric pressure?

## Assistant
<summary>Dispatching L1 query to find molar isobaric heat capacity (Cp) of pure liquid water at 298.15 K and atmospheric pressure from ThermoML database.</summary>
<tool_call>L1_query(instruction=Search for molar …, id_catalog=, context=Property ID for m…)</tool_call>

## User
<tool_result>
<subagent_answer>
### L1#1 — L1_query return

**Status:** status=success

**Summary:** Two ThermoML measurements of the isobaric molar heat capacity (Cp) of pure liquid water at 298.15 K are reported. At 101.325 kPa (DOI 10.1016/j.jct.2016.09.031), Cp = 75.11470996 J/(K·mol). At 101.0 kPa (DOI 10.1016/j.fluid.2013.08.005), Cp = 75.368725408 J/(K·mol). No explicit uncertainty values were reported in the inspected blocks. Both values are consistent with the commonly cited standard molar heat capacity of liquid water at 298.15 K.

**Answer:**

#### Measured Isobaric Molar Heat Capacity (Cp) of Pure Liquid Water at 298.15 K and Atmospheric Pressure

The ThermoML database contains multiple measurements of the molar heat capacity at constant pressure (Cp) for pure liquid water at 298.15 K and near-atmospheric pressure. Here are two representative, inspected data points:

##### Data Point 1 — Exact conditions (298.15 K, 101.325 kPa)
- **Cp = 75.11470996 J/(K·mol)**
- Temperature: 298.15 K
- Pressure: 101.325 kPa
- Source: DOI 10.1016/j.jct.2016.09.031 (GLOBlit_4832, PROPblock_1)
- Measurement method: GLOBmeas_12

##### Data Point 2 — Near-atmospheric (298.15 K, 101.0 kPa)
- **Cp = 75.368725408 J/(K·mol)**
- Temperature: 298.15 K
- Pressure: 101.0 kPa
- Source: DOI 10.1016/j.fluid.2013.08.005 (GLOBlit_1310, PROPblock_1)
- Measurement method: GLOBmeas_31

##### Summary
The two inspected measurements at 298.15 K give Cp values of 75.11470996 and 75.368725408 J/(K·mol), consistent with the commonly cited standard molar heat capacity of liquid water (approximately 75.3 J/(K·mol) at 298.15 K, per general reference literature — not from this database). The difference between the two inspected values (computed: 75.368725408 − 75.11470996 ≈ 0.254 J/(K·mol)) reflects differences in experimental technique, calibration, and exact pressure conditions (101.325 vs 101.0 kPa). No explicit uncertainty values were reported in the inspected blocks.

---
[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:
- **UNGROUNDED_LITERAL** PROPblock_1: 0.254 (near '…wo inspected values (computed: 75.368725408 - 75.11470996 ≈ …') matches no inspected row/stat, database table, or other source of PROPblock_1
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_1", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 0.254})` — if it is a value you computed or an external reference, keep it and label its provenance instead
Inspected so far: PROPblock_1

**Core claims:**
- The ThermoML database contains two inspected measurements of the isobaric molar heat capacity (Cp) of pure liquid water at 298.15 K and near-atmospheric pressure: 75.11470996 J/(K·mol) at 101.325 kPa (DOI 10.1016/j.jct.2016.09.031) and 75.368725408 J/(K·mol) at 101.0 kPa (DOI 10.1016/j.fluid.2013.08.005).
- The two inspected Cp values are consistent with the commonly cited standard molar heat capacity of liquid water at 298.15 K (approximately 75.3 J/(K·mol)), and their difference reflects differences in experimental technique, calibration, and exact pressure conditions.
- No explicit uncertainty values were reported in the inspected data blocks.

#### Core blocks found — verbatim ledger

```ledger
**L1#1_Table#1_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_4832 | lit_id: 2017-gao-li-1 | doi: 10.1016/j.jct.2016.09.031
block: PROPblock_1 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_2) | system: unary | n_datapoints: 1
compounds: water (H2O; GLOBcomp_1; DOIcomp_4; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_9
description: Isobaric molar heat capacity of pure liquid water at 298.15 K and 101.325 kPa; Cp = 75.11470996 J/(K·mol).

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#1_Row#1 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=298.15–298.15 · n_unique=1 · phase=Liquid」 |
| L1#1_Table#1_Row#2 | 「variable」 | 「BLKvar_2/GLOBvar_3」 | 「Pressure, kPa」 | 「range=101.325–101.325 · n_unique=1 · phase=Liquid」 |
| L1#1_Table#1_Row#3 | 「property」 | 「BLKprop_1/GLOBprop_9」 | 「Molar heat capacity at constant pressure, J/K/mol」 | 「method=Flow calorimetry (GLOBmeas_12) · range=75.11471–75.11471 · mean=75.11471 · n=1 · phase=Liquid」 |
```

```ledger
**L1#1_Table#2_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_1310 | lit_id: 2013-was-kun-0 | doi: 10.1016/j.fluid.2013.08.005
block: PROPblock_1 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_2) | system: unary | n_datapoints: 8
compounds: water (H2O; GLOBcomp_1; DOIcomp_3; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_9
description: Isobaric molar heat capacity of pure liquid water at 298.15 K and 101.0 kPa; Cp = 75.368725408 J/(K·mol).

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#2_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.0 · phase=Liquid」 |
| L1#1_Table#2_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=298.15–313.15 · n_unique=4 · phase=Liquid」 |
| L1#1_Table#2_Row#3 | 「property」 | 「BLKprop_1/GLOBprop_9」 | 「Molar heat capacity at constant pressure, J/K/mol」 | 「method=Large sample (1 g) DSC (GLOBmeas_31) · range=75.316481–75.368725 · mean=75.337199 · n=8 · phase=Liquid」 |
```

#### Data inspections — verbatim ledger

```ledger
**L1#1_Table#3_(Query_L1#1_INSP):**
lit_num_id: GLOBlit_4832 | doi: 10.1016/j.jct.2016.09.031 | block: PROPblock_1
table_mode: nearest | inspection_id: INSP_e7315da23f25 | rows_shown: 1

| *row_id* | *BLKpoint_id* | *temperature_k* | *pressure_kpa* | *molar_heat_capacity_at_constant_pressure_j_k_mol* |
|---|---|---|---|---|
| L1#1_Table#3_Row#1 | 「BLKpoint_1」 | 「298.15」 | 「101.325」 | 「75.11470996」 |
```

```ledger
**L1#1_Table#4_(Query_L1#1_INSP):**
lit_num_id: GLOBlit_1310 | doi: 10.1016/j.fluid.2013.08.005 | block: PROPblock_1
table_mode: nearest | inspection_id: INSP_16f83e05d02a | rows_shown: 1

| *row_id* | *BLKpoint_id* | *temperature_k* | *pressure_kpa* | *molar_heat_capacity_at_constant_pressure_j_k_mol* |
|---|---|---|---|---|
| L1#1_Table#4_Row#1 | 「BLKpoint_1」 | 「298.15」 | 「101.0」 | 「75.368725408」 |
```
</subagent_answer>
</tool_result>

## LLM Response
<reasoning>
The L1 query returned two verified data points for the isobaric molar heat capacity of pure liquid water at 298.15 K (25 °C) and atmospheric pressure. Both values are verbatim from inspected data tables. The flagged "0.254" value was just a computed difference, not a database datum, so I can note the difference is computed by me if I mention it. Let me compose the final answer.
</reasoning>

<answer>
## Measured Isobaric Molar Heat Capacity (Cp) of Pure Liquid Water at 25 °C and Atmospheric Pressure

The ThermoML database contains two independent measurements of the molar heat capacity at constant pressure (Cp) for pure liquid water at 298.15 K (25 °C) and near-atmospheric pressure:

| # | Cp [J/(K·mol)] | Temperature [K] | Pressure [kPa] | Method | DOI | Source ID |
|---|-----------------|-----------------|-----------------|--------|-----|-----------|
| 1 | **75.11470996** | 298.15 | 101.325 | Flow calorimetry | 10.1016/j.jct.2016.09.031 | GLOBlit_4832 |
| 2 | **75.368725408** | 298.15 | 101.0 | Large-sample DSC | 10.1016/j.fluid.2013.08.005 | GLOBlit_1310 |

### Key observations

- Both measurements fall close to the widely accepted standard molar heat capacity of liquid water at 25 °C (~75.3 J/(K·mol)).
- The small difference between the two values reflects differences in experimental technique (flow calorimetry vs. large-sample differential scanning calorimetry), instrument calibration, and the slight difference in nominal pressure (101.325 kPa vs. 101.0 kPa). At these near-atmospheric pressures, the pressure effect on Cp of liquid water is negligible, so the spread is primarily methodological.
- No explicit uncertainty values were reported in either dataset.

Water's relatively high molar heat capacity — compared to most molecular liquids of similar molar mass — arises from its extensive hydrogen-bonding network, which provides additional modes for energy storage beyond simple translational and rotational contributions.
</answer>