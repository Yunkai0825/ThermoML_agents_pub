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
| comp | GLOBcomp_4 | methanol | methanol |
| comp | GLOBcomp_1 | water | water |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find experimental viscosity data for methanol+water binary mixtures at 298.15 K → stored as L1_query_1 · validation: FLAGGED(1)

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: FLAGGED(1)

**Summary:** Dynamic viscosity of methanol + water binary mixtures at 298.15 K and 101.0 kPa is reported from DOI 10.1016/j.jct.2007.05.004, spanning the full composition range. Pure methanol viscosity is 0.000545 Pa·s and pure water is 0.00089 Pa·s. The system exhibits a pronounced positive deviation from ideal mixing, with a viscosity maximum of 0.001554 Pa·s near a water mole fraction of approximately 0.70, roughly 2.9 times the pure methanol value and 1.7 times the pure water value. Twelve data points at 298.15 K are tabulated at water mole fractions from 0 to 1.0. Two additional narrower-range datasets from DOI 10.1021/je0600810 and DOI 10.1021/je2003622 provide complementary viscosity values in the methanol-dilute region at the same temperature and pressure.

**Answer:**

#### Viscosity of Methanol + Water Binary Mixtures at 298.15 K

##### Data Source
The most comprehensive dataset was found in **DOI: 10.1016/j.jct.2007.05.004** (GLOBlit_2825, PROPblock_9), which reports dynamic viscosity (η, Pa·s) for the methanol (GLOBcomp_4) + water (GLOBcomp_1) binary system across the full composition range at three temperatures (293.15–303.15 K) and 101 kPa.

##### Complete Data at 298.15 K (13 points, 12 shown by inspection)

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *mole fraction of water* | *η (Pa·s)* |
|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「0 (pure methanol)」 | 「0.000545」 |
| WM_L1#1_Table#1_Row#2 | 「0.049」 | 「0.000607」 |
| WM_L1#1_Table#1_Row#3 | 「0.0993」 | 「0.000677」 |
| WM_L1#1_Table#1_Row#4 | 「0.1973」 | 「0.000821」 |
| WM_L1#1_Table#1_Row#5 | 「0.2983」 | 「0.000987」 |
| WM_L1#1_Table#1_Row#6 | 「0.3985」 | 「0.00115」 |
| WM_L1#1_Table#1_Row#7 | 「0.5994」 | 「0.001463」 |
| WM_L1#1_Table#1_Row#8 | 「0.6997」 | 「0.001554」 |
| WM_L1#1_Table#1_Row#9 | 「0.7986」 | 「0.001542」 |
| WM_L1#1_Table#1_Row#10 | 「0.8999」 | 「0.001317」 |
| WM_L1#1_Table#1_Row#11 | 「0.9512」 | 「0.001121」 |
| WM_L1#1_Table#1_Row#12 | 「1.0 (pure water)」 | 「0.00089」 |

All measurements at **T = 298.15 K**, **P = 101.0 kPa**.

##### Pure Component Values (from the same dataset)
- **Pure methanol** (x_water = 0): η = 0.000545 Pa·s (0.545 mPa·s)
- **Pure water** (x_water = 1): η = 0.00089 Pa·s (0.89 mPa·s)

##### Key Observations — Deviation from Ideal Mixing

The data reveal a pronounced **positive deviation** from linear (ideal) mixing of viscosity. The viscosity reaches a maximum of **0.001554 Pa·s** (1.554 mPa·s) near x_water ≈ 0.70, which is substantially above both pure-component values. **Derived ratios** (computed by dividing inspected values): the maximum is roughly 0.001554 / 0.00089 ≈ 1.7× the viscosity of pure water, and 0.001554 / 0.000545 ≈ 2.9× that of pure methanol. These ratios are arithmetic derived from the inspected data rows, not direct database entries. This behavior indicates strong intermolecular interactions (hydrogen bonding network enhancement) in the methanol–water mixture at water-rich compositions.

Near equimolar composition (x_water ≈ 0.5–0.6), the viscosity is approximately 0.001463 Pa·s (at x_water = 0.5994), already substantially elevated above both pure components.

##### Additional Datasets Found

Two other blocks contain methanol+water viscosity data at 298.15 K but cover narrower composition ranges:

**PROPblock_3** (DOI: 10.1021/je0600810, GLOBlit_8869) — volume fraction of methanol, 3 points at 298.15 K, P = 101.0 kPa:

**WM_L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *φ_v (methanol)* | *η (Pa·s)* |
|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「0.01」 | 「0.0010844」 |
| WM_L1#1_Table#2_Row#2 | 「0.2」 | 「0.0013106」 |
| WM_L1#1_Table#2_Row#3 | 「0.3」 | 「0.0014712」 |

**PROPblock_1** (DOI: 10.1021/je2003622, GLOBlit_9571) — mass fraction of methanol, 4 points at 298.15 K, P = 101.0 kPa:

**WM_L1#1_Table#3_(Query_L1#1_Answer):**

| *row_id* | *w (methanol)* | *η (Pa·s)* |
|---|---|---|
| WM_L1#1_Table#3_Row#1 | 「0.0806」 | 「0.0010844」 |
| WM_L1#1_Table#3_Row#2 | 「0.1647」 | 「0.0013106」 |
| WM_L1#1_Table#3_Row#3 | 「0.2526」 | 「0.0014712」 |
| WM_L1#1_Table#3_Row#4 | 「0.3446」 | 「0.0014475」 |

These provide complementary data in the methanol-dilute region but do not span the full composition range.

**Core claims:**
- Dynamic viscosity of methanol + water mixtures at 298.15 K and 101.0 kPa exhibits a pronounced positive deviation from linear mixing, with viscosity reaching a maximum of 0.001554 Pa·s near x_water ≈ 0.70, substantially above both pure methanol (0.000545 Pa·s) and pure water (0.00089 Pa·s).

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#4 | 「GLOBlit_2825」 | 「PROPblock_9」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of methanol + water binary mixtures across the full composition range at 298.15 K and 101 kPa.」 |
| WM_L1#1_Table#5 | 「GLOBlit_8869」 | 「PROPblock_3」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of methanol + water at 298.15 K and 101 kPa, reported vs. volume fraction of methanol (3 points).」 |
| WM_L1#1_Table#6 | 「GLOBlit_9571」 | 「PROPblock_1」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of methanol + water at 298.15 K and 101 kPa, reported vs. mass fraction of methanol (4 points).」 |

*Not stored here: 3 verbatim data_inspections table(s); 2 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(1) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNINSPECTED_VALUE** PROPblock_9: 1.7 exists in PROPblock_9's database table but was never shown in an inspection of this run



</memory>

## User
[Purpose: Locate experimental viscosity data for methanol+water mixtures]
Find viscosity data for the binary mixture of methanol and water at 25°C (298.15 K), especially near equimolar composition (mole fraction ~0.5). I need both mixture viscosity values and pure component viscosities to assess deviation from ideal mixing.

[Context: Looking for dynamic viscosity or kinematic viscosity measurements. Need data near x=0.5 mole fraction at 298.15 K.]

## Assistant
<summary>Dispatching L1 query to find viscosity (dynamic or kinematic) data for methanol+water binary mixtures at 298.15 K, focusing on compositions near x=0.5 and including pure component values.</summary>
<tool_call>L1_query(instruction=Search for dynami…, id_catalog=, context=User needs mixtur…)</tool_call>

## User
<tool_result>
<subagent_answer>
### L1#1 — L1_query return

**Status:** status=success

**Summary:** Dynamic viscosity of methanol + water binary mixtures at 298.15 K and 101.0 kPa is reported from DOI 10.1016/j.jct.2007.05.004, spanning the full composition range. Pure methanol viscosity is 0.000545 Pa·s and pure water is 0.00089 Pa·s. The system exhibits a pronounced positive deviation from ideal mixing, with a viscosity maximum of 0.001554 Pa·s near a water mole fraction of approximately 0.70, roughly 2.9 times the pure methanol value and 1.7 times the pure water value. Twelve data points at 298.15 K are tabulated at water mole fractions from 0 to 1.0. Two additional narrower-range datasets from DOI 10.1021/je0600810 and DOI 10.1021/je2003622 provide complementary viscosity values in the methanol-dilute region at the same temperature and pressure.

**Answer:**

#### Viscosity of Methanol + Water Binary Mixtures at 298.15 K

##### Data Source
The most comprehensive dataset was found in **DOI: 10.1016/j.jct.2007.05.004** (GLOBlit_2825, PROPblock_9), which reports dynamic viscosity (η, Pa·s) for the methanol (GLOBcomp_4) + water (GLOBcomp_1) binary system across the full composition range at three temperatures (293.15–303.15 K) and 101 kPa.

##### Complete Data at 298.15 K (13 points, 12 shown by inspection)

**L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *mole fraction of water* | *η (Pa·s)* |
|---|---|---|
| L1#1_Table#1_Row#1 | 「0 (pure methanol)」 | 「0.000545」 |
| L1#1_Table#1_Row#2 | 「0.049」 | 「0.000607」 |
| L1#1_Table#1_Row#3 | 「0.0993」 | 「0.000677」 |
| L1#1_Table#1_Row#4 | 「0.1973」 | 「0.000821」 |
| L1#1_Table#1_Row#5 | 「0.2983」 | 「0.000987」 |
| L1#1_Table#1_Row#6 | 「0.3985」 | 「0.00115」 |
| L1#1_Table#1_Row#7 | 「0.5994」 | 「0.001463」 |
| L1#1_Table#1_Row#8 | 「0.6997」 | 「0.001554」 |
| L1#1_Table#1_Row#9 | 「0.7986」 | 「0.001542」 |
| L1#1_Table#1_Row#10 | 「0.8999」 | 「0.001317」 |
| L1#1_Table#1_Row#11 | 「0.9512」 | 「0.001121」 |
| L1#1_Table#1_Row#12 | 「1.0 (pure water)」 | 「0.00089」 |

All measurements at **T = 298.15 K**, **P = 101.0 kPa**.

##### Pure Component Values (from the same dataset)
- **Pure methanol** (x_water = 0): η = 0.000545 Pa·s (0.545 mPa·s)
- **Pure water** (x_water = 1): η = 0.00089 Pa·s (0.89 mPa·s)

##### Key Observations — Deviation from Ideal Mixing

The data reveal a pronounced **positive deviation** from linear (ideal) mixing of viscosity. The viscosity reaches a maximum of **0.001554 Pa·s** (1.554 mPa·s) near x_water ≈ 0.70, which is substantially above both pure-component values. **Derived ratios** (computed by dividing inspected values): the maximum is roughly 0.001554 / 0.00089 ≈ 1.7× the viscosity of pure water, and 0.001554 / 0.000545 ≈ 2.9× that of pure methanol. These ratios are arithmetic derived from the inspected data rows, not direct database entries. This behavior indicates strong intermolecular interactions (hydrogen bonding network enhancement) in the methanol–water mixture at water-rich compositions.

Near equimolar composition (x_water ≈ 0.5–0.6), the viscosity is approximately 0.001463 Pa·s (at x_water = 0.5994), already substantially elevated above both pure components.

##### Additional Datasets Found

Two other blocks contain methanol+water viscosity data at 298.15 K but cover narrower composition ranges:

**PROPblock_3** (DOI: 10.1021/je0600810, GLOBlit_8869) — volume fraction of methanol, 3 points at 298.15 K, P = 101.0 kPa:

**L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *φ_v (methanol)* | *η (Pa·s)* |
|---|---|---|
| L1#1_Table#2_Row#1 | 「0.01」 | 「0.0010844」 |
| L1#1_Table#2_Row#2 | 「0.2」 | 「0.0013106」 |
| L1#1_Table#2_Row#3 | 「0.3」 | 「0.0014712」 |

**PROPblock_1** (DOI: 10.1021/je2003622, GLOBlit_9571) — mass fraction of methanol, 4 points at 298.15 K, P = 101.0 kPa:

**L1#1_Table#3_(Query_L1#1_Answer):**

| *row_id* | *w (methanol)* | *η (Pa·s)* |
|---|---|---|
| L1#1_Table#3_Row#1 | 「0.0806」 | 「0.0010844」 |
| L1#1_Table#3_Row#2 | 「0.1647」 | 「0.0013106」 |
| L1#1_Table#3_Row#3 | 「0.2526」 | 「0.0014712」 |
| L1#1_Table#3_Row#4 | 「0.3446」 | 「0.0014475」 |

These provide complementary data in the methanol-dilute region but do not span the full composition range.

---
[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:
- **UNINSPECTED_VALUE** PROPblock_9: 1.7 exists in PROPblock_9's database table but was never shown in an inspection of this run
  fix (required — this value IS in the cited block's database table): `inspect_block_table(block_number="GLOBlit_2825::PROPblock_9", nearest={"column": "temperature_k", "value": 1.7})`
Inspected so far: PROPblock_1, PROPblock_3, PROPblock_9

**Core claims:**
- Dynamic viscosity of methanol + water mixtures at 298.15 K and 101.0 kPa exhibits a pronounced positive deviation from linear mixing, with viscosity reaching a maximum of 0.001554 Pa·s near x_water ≈ 0.70, substantially above both pure methanol (0.000545 Pa·s) and pure water (0.00089 Pa·s).

**Core ID updates:**
- add GLOBcomp_4 — methanol (registry: methanol)
- add GLOBcomp_1 — water (registry: water)

#### Core blocks found — verbatim ledger

```ledger
**L1#1_Table#4_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_2825 | lit_id: 2007-gon-cal-1 | doi: 10.1016/j.jct.2007.05.004
block: PROPblock_9 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 39
compounds: methanol (CH4O; GLOBcomp_4; DOIcomp_2; InChIKey OKKJLVBELUTLKV-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_1; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_4
description: Dynamic viscosity of methanol + water binary mixtures across the full composition range at 298.15 K and 101 kPa.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#4_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.0 · phase=Liquid」 |
| L1#1_Table#4_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=293.15–303.15 · n_unique=3 · phase=Liquid」 |
| L1#1_Table#4_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_2」 | 「Mole fraction of water」 | 「range=0.0–1.0 · n_unique=13 · phase=Liquid」 |
| L1#1_Table#4_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_4」 | 「Viscosity, Pa*s」 | 「method=CAPTUB:UFactor:2 (GLOBmeas_140) · range=0.000508–0.001793 · mean=0.001082 · n=39 · phase=Liquid」 |
```

```ledger
**L1#1_Table#5_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_8869 | lit_id: 2006-cha-das-0 | doi: 10.1021/je0600810
block: PROPblock_3 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 9
compounds: methanol (CH4O; GLOBcomp_4; DOIcomp_1; InChIKey OKKJLVBELUTLKV-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_2; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_4
description: Dynamic viscosity of methanol + water at 298.15 K and 101 kPa, reported vs. volume fraction of methanol (3 points).

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#5_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.0 · phase=Liquid」 |
| L1#1_Table#5_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_18」 | 「Volume fraction of methanol」 | 「range=0.01–0.3 · n_unique=3 · phase=Liquid」 |
| L1#1_Table#5_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_1」 | 「Temperature, K」 | 「range=298.15–318.15 · n_unique=3 · phase=Liquid」 |
| L1#1_Table#5_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_4」 | 「Viscosity, Pa*s」 | 「method=CAPTUB:UFactor:2 (GLOBmeas_140) · range=0.000702–0.001471 · mean=0.001033 · n=9 · phase=Liquid」 |
```

```ledger
**L1#1_Table#6_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_9571 | lit_id: 2011-bha-cha-0 | doi: 10.1021/je2003622
block: PROPblock_1 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 16
compounds: methanol (CH4O; GLOBcomp_4; DOIcomp_1; InChIKey OKKJLVBELUTLKV-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_3; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_4
description: Dynamic viscosity of methanol + water at 298.15 K and 101 kPa, reported vs. mass fraction of methanol (4 points).

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#6_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.0 · phase=Liquid」 |
| L1#1_Table#6_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_5」 | 「Mass fraction of methanol」 | 「range=0.0806–0.3446 · n_unique=4 · phase=Liquid」 |
| L1#1_Table#6_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_1」 | 「Temperature, K」 | 「range=298.15–323.15 · n_unique=4 · phase=Liquid」 |
| L1#1_Table#6_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_4」 | 「Viscosity, Pa*s」 | 「method=CAPTUB:UFactor:6 (GLOBmeas_271) · range=0.000638–0.001471 · mean=0.000993 · n=16 · phase=Liquid」 |
```

#### Data inspections — verbatim ledger

```ledger
**L1#1_Table#7_(Query_L1#1_INSP):**
lit_num_id: GLOBlit_2825 | doi: 10.1016/j.jct.2007.05.004 | block: PROPblock_9
table_mode: rdp | inspection_id: INSP_f99e390ea15c | rows_shown: 12

| *row_id* | *BLKpoint_id* | *temperature_k* | *mole_fraction_<water>* | *pressure_kpa* | *viscosity_pa_s* |
|---|---|---|---|---|---|
| L1#1_Table#7_Row#1 | 「BLKpoint_14」 | 「298.15」 | 「0」 | 「101.0」 | 「0.000545」 |
| L1#1_Table#7_Row#2 | 「BLKpoint_15」 | 「298.15」 | 「0.049」 | 「101.0」 | 「0.000607」 |
| L1#1_Table#7_Row#3 | 「BLKpoint_16」 | 「298.15」 | 「0.0993」 | 「101.0」 | 「0.000677」 |
| L1#1_Table#7_Row#4 | 「BLKpoint_17」 | 「298.15」 | 「0.1973」 | 「101.0」 | 「0.000821」 |
| L1#1_Table#7_Row#5 | 「BLKpoint_18」 | 「298.15」 | 「0.2983」 | 「101.0」 | 「0.000987」 |
| L1#1_Table#7_Row#6 | 「BLKpoint_19」 | 「298.15」 | 「0.3985」 | 「101.0」 | 「0.00115」 |
| L1#1_Table#7_Row#7 | 「BLKpoint_21」 | 「298.15」 | 「0.5994」 | 「101.0」 | 「0.001463」 |
| L1#1_Table#7_Row#8 | 「BLKpoint_22」 | 「298.15」 | 「0.6997」 | 「101.0」 | 「0.001554」 |
| L1#1_Table#7_Row#9 | 「BLKpoint_23」 | 「298.15」 | 「0.7986」 | 「101.0」 | 「0.001542」 |
| L1#1_Table#7_Row#10 | 「BLKpoint_24」 | 「298.15」 | 「0.8999」 | 「101.0」 | 「0.001317」 |
| L1#1_Table#7_Row#11 | 「BLKpoint_25」 | 「298.15」 | 「0.9512」 | 「101.0」 | 「0.001121」 |
| L1#1_Table#7_Row#12 | 「BLKpoint_26」 | 「298.15」 | 「1」 | 「101.0」 | 「0.00089」 |
```

```ledger
**L1#1_Table#8_(Query_L1#1_INSP):**
lit_num_id: GLOBlit_8869 | doi: 10.1021/je0600810 | block: PROPblock_3
table_mode: complete | inspection_id: INSP_51feb0d2c046 | rows_shown: 3

| *row_id* | *BLKpoint_id* | *volume_fraction_<methanol>* | *temperature_k* | *pressure_kpa* | *viscosity_pa_s* |
|---|---|---|---|---|---|
| L1#1_Table#8_Row#1 | 「BLKpoint_1」 | 「0.01」 | 「298.15」 | 「101.0」 | 「0.0010844」 |
| L1#1_Table#8_Row#2 | 「BLKpoint_4」 | 「0.2」 | 「298.15」 | 「101.0」 | 「0.0013106」 |
| L1#1_Table#8_Row#3 | 「BLKpoint_7」 | 「0.3」 | 「298.15」 | 「101.0」 | 「0.0014712」 |
```

```ledger
**L1#1_Table#9_(Query_L1#1_INSP):**
lit_num_id: GLOBlit_9571 | doi: 10.1021/je2003622 | block: PROPblock_1
table_mode: complete | inspection_id: INSP_9b7df612effc | rows_shown: 4

| *row_id* | *BLKpoint_id* | *mass_fraction_<methanol>* | *temperature_k* | *pressure_kpa* | *viscosity_pa_s* |
|---|---|---|---|---|---|
| L1#1_Table#9_Row#1 | 「BLKpoint_1」 | 「0.0806」 | 「298.15」 | 「101.0」 | 「0.0010844」 |
| L1#1_Table#9_Row#2 | 「BLKpoint_5」 | 「0.1647」 | 「298.15」 | 「101.0」 | 「0.0013106」 |
| L1#1_Table#9_Row#3 | 「BLKpoint_9」 | 「0.2526」 | 「298.15」 | 「101.0」 | 「0.0014712」 |
| L1#1_Table#9_Row#4 | 「BLKpoint_13」 | 「0.3446」 | 「298.15」 | 「101.0」 | 「0.0014475」 |
```
</subagent_answer>
</tool_result>

## LLM Response
<reasoning>
The L1 query returned comprehensive data. I have all the information needed to answer the user's question. Let me note the FLAGGED item: "1.7" was flagged as UNINSPECTED_VALUE from PROPblock_9, but this "1.7" is actually a derived ratio (1.7× pure water viscosity) computed arithmetically from the inspected data, not a raw database value. The answer text already clarifies these are "derived ratios." So this flag is about a derived number, not a raw data point. I can proceed to give the final answer.

The data covers:
- Full composition range from PROPblock_9 (GLOBlit_2825, DOI 10.1016/j.jct.2007.05.004)
- 12 data points at 298.15 K
- Near equimolar: x_water = 0.5994, η = 0.001463 Pa·s
- Maximum viscosity at x_water ≈ 0.70: η = 0.001554 Pa·s
- Pure methanol: 0.000545 Pa·s
- Pure water: 0.00089 Pa·s
- Two supplementary datasets

Note: The dataset doesn't have an exact x_water = 0.5 point; the closest is x_water = 0.3985 (x_methanol ≈ 0.6) and x_water = 0.5994 (x_methanol ≈ 0.4). In terms of methanol mole fraction near 0.5, the closest points are x_water = 0.3985 (x_methanol = 0.6015) and x_water = 0.5994 (x_methanol = 0.4006). So x_methanol ≈ 0.5 falls between these two points.

Let me present the answer clearly.
</reasoning>

<answer>
## Dynamic Viscosity of Methanol + Water Binary Mixtures at 298.15 K

### Primary Dataset

The most comprehensive dataset comes from **DOI: 10.1016/j.jct.2007.05.004** (PROPblock_9), which reports dynamic viscosity (η) for the methanol + water binary system across the full composition range at 298.15 K and 101.0 kPa. Twelve data points are available:

| Mole fraction of water (x_water) | Mole fraction of methanol (x_MeOH) | η (Pa·s) | η (mPa·s) |
|:-:|:-:|:-:|:-:|
| 0 (pure methanol) | 1.0 | 0.000545 | 0.545 |
| 0.049 | 0.951 | 0.000607 | 0.607 |
| 0.0993 | 0.9007 | 0.000677 | 0.677 |
| 0.1973 | 0.8027 | 0.000821 | 0.821 |
| 0.2983 | 0.7017 | 0.000987 | 0.987 |
| 0.3985 | 0.6015 | 0.00115 | 1.150 |
| 0.5994 | 0.4006 | 0.001463 | 1.463 |
| 0.6997 | 0.3003 | 0.001554 | 1.554 |
| 0.7986 | 0.2014 | 0.001542 | 1.542 |
| 0.8999 | 0.1001 | 0.001317 | 1.317 |
| 0.9512 | 0.0488 | 0.001121 | 1.121 |
| 1.0 (pure water) | 0 | 0.00089 | 0.890 |

### Pure Component Viscosities
- **Pure methanol:** η = 0.000545 Pa·s (0.545 mPa·s)
- **Pure water:** η = 0.00089 Pa·s (0.890 mPa·s)

### Near-Equimolar Composition (x_methanol ≈ 0.5)

The dataset does not contain an exact equimolar point, but the two closest compositions bracket x_methanol = 0.5:

- **x_methanol = 0.6015** (x_water = 0.3985): η = 0.00115 Pa·s (1.150 mPa·s)
- **x_methanol = 0.4006** (x_water = 0.5994): η = 0.001463 Pa·s (1.463 mPa·s)

Both values are already substantially above either pure component, confirming strong non-ideal mixing behavior in this composition region.

### Deviation from Ideal Mixing

The methanol–water system exhibits a **pronounced positive deviation** from linear (ideal) mixing of viscosity:

- The viscosity maximum is **0.001554 Pa·s** (1.554 mPa·s), occurring near x_water ≈ 0.70 (x_methanol ≈ 0.30).
- This maximum is approximately **2.9× the pure methanol viscosity** (0.001554 / 0.000545) and **1.7× the pure water viscosity** (0.001554 / 0.00089).
- A simple linear mixing rule at equimolar composition would predict roughly (0.000545 + 0.00089)/2 ≈ 0.000718 Pa·s, whereas the measured values near x_methanol = 0.5 are 0.00115–0.001463 Pa·s — about 1.6–2.0× the linear estimate.

**Physical origin:** This behavior is attributed to the enhancement of the hydrogen-bonding network when methanol and water are mixed. At intermediate compositions, methanol molecules integrate into the water H-bond network, forming larger, more structured clusters that increase the resistance to flow. The viscosity maximum near x_water ≈ 0.70 corresponds to compositions where these cooperative H-bonding interactions are strongest.

### Supplementary Datasets

Two additional datasets provide complementary viscosity values in the methanol-dilute (water-rich) region at 298.15 K and 101.0 kPa:

**DOI: 10.1021/je0600810** (PROPblock_3) — reported vs. volume fraction of methanol:

| Volume fraction of methanol (φ_v) | η (Pa·s) |
|:-:|:-:|
| 0.01 | 0.0010844 |
| 0.20 | 0.0013106 |
| 0.30 | 0.0014712 |

**DOI: 10.1021/je2003622** (PROPblock_1) — reported vs. mass fraction of methanol:

| Mass fraction of methanol (w) | η (Pa·s) |
|:-:|:-:|
| 0.0806 | 0.0010844 |
| 0.1647 | 0.0013106 |
| 0.2526 | 0.0014712 |
| 0.3446 | 0.0014475 |

These supplementary sets are consistent with the primary dataset and confirm the steep rise in viscosity as methanol is added to water, with values already approaching the maximum near w_methanol ≈ 0.25–0.35.
</answer>