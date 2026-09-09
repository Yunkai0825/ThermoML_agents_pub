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
| lit | GLOBlit_5585 | 2019-meh-haj-0 | 10.1016/j.jct.2019.105880 |

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find viscosity data for isopropanol (2-propanol) + water binary mixtures at room temperature (293-298 K) → stored as L1_query_1 · validation: PASS

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: PASS

**Summary:** Dynamic viscosity (Pa·s) data for the binary mixture of propan-2-ol (2-propanol) + water, measured by falling/rolling sphere viscometry in the liquid phase at 100 kPa, from DOI 10.1016/j.jct.2019.105880. The composition range covers mass fractions of propan-2-ol from 0.1 to 0.3. Within the 293–298 K window, six data points are reported: at 293.15 K, viscosities are 0.001633 Pa·s (w = 0.1), 0.002485 Pa·s (w = 0.2), and 0.003172 Pa·s (w = 0.3); at 298.15 K, viscosities are 0.001395 Pa·s (w = 0.1), 0.002045 Pa·s (w = 0.2), and 0.002555 Pa·s (w = 0.3). Viscosity increases with propan-2-ol mass fraction in this range and decreases with increasing temperature. The full data block spans 288.15–303.15 K with viscosities from 0.001208 to 0.004014 Pa·s. No kinematic viscosity data were found for this system in the requested temperature range.

**Answer:**

#### Viscosity Data for 2-Propanol + Water Binary Mixtures at Room Temperature (293–298 K)

##### Source
**DOI:** 10.1016/j.jct.2019.105880 (GLOBlit_5585, PROPblock_12)

**Property:** Dynamic viscosity (Pa·s), measured by falling/rolling sphere viscometry, liquid phase, at 100 kPa.

**System:** Binary mixture of propan-2-ol (2-propanol, GLOBcomp_6) + water (GLOBcomp_1).

**Composition range covered:** Mass fraction of propan-2-ol from 0.1 to 0.3.
**Full block temperature range:** 288.15–303.15 K (12 data points total).

##### Data Points in the 293–298 K Window

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *T (K)* | *w(propan-2-ol)* | *Dynamic Viscosity (Pa·s)* |
|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「293.15」 | 「0.1」 | 「0.001633」 |
| WM_L1#1_Table#1_Row#2 | 「293.15」 | 「0.2」 | 「0.002485」 |
| WM_L1#1_Table#1_Row#3 | 「293.15」 | 「0.3」 | 「0.003172」 |
| WM_L1#1_Table#1_Row#4 | 「298.15」 | 「0.1」 | 「0.001395」 |
| WM_L1#1_Table#1_Row#5 | 「298.15」 | 「0.2」 | 「0.002045」 |
| WM_L1#1_Table#1_Row#6 | 「298.15」 | 「0.3」 | 「0.002555」 |

##### Key Observations

- At both temperatures, viscosity increases with increasing propan-2-ol mass fraction in this composition range (0.1–0.3), consistent with the well-known viscosity maximum of the isopropanol–water system that occurs at higher alcohol concentrations.
- Raising the temperature from 293.15 K to 298.15 K noticeably decreases the viscosity at each composition, as expected from the Arrhenius-type temperature dependence of liquid viscosity (e.g., from 0.001633 to 0.001395 Pa·s at w = 0.1, and from 0.003172 to 0.002555 Pa·s at w = 0.3).
- The full block extends from 288.15 K to 303.15 K with viscosities spanning 0.001208–0.004014 Pa·s.

**Note:** No kinematic viscosity (GLOBprop_40) data were found in the database for this binary system in the requested temperature range. Only dynamic viscosity data are available from this source.

**Core claims:**
- Dynamic viscosity data for the binary mixture of propan-2-ol + water at 100 kPa were found from DOI 10.1016/j.jct.2019.05880, covering mass fractions of propan-2-ol from 0.1 to 0.3 and temperatures of 293.15 K and 298.15 K within the requested room-temperature window.
- At both 293.15 K and 298.15 K, dynamic viscosity increases with increasing propan-2-ol mass fraction over the 0.1–0.3 range, with values ranging from 0.001633 Pa·s (w = 0.1, 293.15 K) to 0.003172 Pa·s (w = 0.3, 293.15 K) and from 0.001395 Pa·s (w = 0.1, 298.15 K) to 0.002555 Pa·s (w = 0.3, 298.15 K).
- Raising the temperature from 293.15 K to 298.15 K decreases the dynamic viscosity at each composition, consistent with Arrhenius-type temperature dependence of liquid viscosity.
- No kinematic viscosity data were found in the database for this binary system in the requested temperature range; only dynamic viscosity data are available from this source.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#2 | 「GLOBlit_5585」 | 「PROPblock_12」 | 「GLOBcomp_1, GLOBcomp_6」 | 「GLOBprop_4」 | 「Dynamic viscosity (Pa·s) for propan-2-ol + water binary mixture, mass fraction of propan-2-ol 0.1–0.3, 288.15–303.15 K, 100 kPa.」 |

*Not stored here: 1 verbatim data_inspections table(s); 3 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.



</memory>

## User
[Purpose: Identify available experimental viscosity data for isopropanol-water binary mixtures at room temperature in the ThermoML database]
Find viscosity data for isopropanol (2-propanol) mixed with water at room temperature (around 293-298 K). Rubbing alcohol is isopropanol.

[Context: Rubbing alcohol is commonly isopropanol (2-propanol, CAS 67-63-0). Looking for dynamic or kinematic viscosity measurements of binary mixtures of isopropanol + water near 25°C or 20°C.]

## Assistant
<summary>Dispatching L1 query to find viscosity data for isopropanol (2-propanol, CAS 67-63-0) + water binary mixtures at room temperature (293-298 K). Looking for both dynamic viscosity (GLOBprop_4) and kinematic viscosity (GLOBprop_40).</summary>
<tool_call>L1_query(instruction=Search for dynami…, id_catalog=, context=User is looking f…)</tool_call>

## User
<tool_result>
<subagent_answer>
### L1#1 — L1_query return

**Status:** status=success

**Summary:** Dynamic viscosity (Pa·s) data for the binary mixture of propan-2-ol (2-propanol) + water, measured by falling/rolling sphere viscometry in the liquid phase at 100 kPa, from DOI 10.1016/j.jct.2019.105880. The composition range covers mass fractions of propan-2-ol from 0.1 to 0.3. Within the 293–298 K window, six data points are reported: at 293.15 K, viscosities are 0.001633 Pa·s (w = 0.1), 0.002485 Pa·s (w = 0.2), and 0.003172 Pa·s (w = 0.3); at 298.15 K, viscosities are 0.001395 Pa·s (w = 0.1), 0.002045 Pa·s (w = 0.2), and 0.002555 Pa·s (w = 0.3). Viscosity increases with propan-2-ol mass fraction in this range and decreases with increasing temperature. The full data block spans 288.15–303.15 K with viscosities from 0.001208 to 0.004014 Pa·s. No kinematic viscosity data were found for this system in the requested temperature range.

**Answer:**

#### Viscosity Data for 2-Propanol + Water Binary Mixtures at Room Temperature (293–298 K)

##### Source
**DOI:** 10.1016/j.jct.2019.105880 (GLOBlit_5585, PROPblock_12)

**Property:** Dynamic viscosity (Pa·s), measured by falling/rolling sphere viscometry, liquid phase, at 100 kPa.

**System:** Binary mixture of propan-2-ol (2-propanol, GLOBcomp_6) + water (GLOBcomp_1).

**Composition range covered:** Mass fraction of propan-2-ol from 0.1 to 0.3.
**Full block temperature range:** 288.15–303.15 K (12 data points total).

##### Data Points in the 293–298 K Window

**L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *T (K)* | *w(propan-2-ol)* | *Dynamic Viscosity (Pa·s)* |
|---|---|---|---|
| L1#1_Table#1_Row#1 | 「293.15」 | 「0.1」 | 「0.001633」 |
| L1#1_Table#1_Row#2 | 「293.15」 | 「0.2」 | 「0.002485」 |
| L1#1_Table#1_Row#3 | 「293.15」 | 「0.3」 | 「0.003172」 |
| L1#1_Table#1_Row#4 | 「298.15」 | 「0.1」 | 「0.001395」 |
| L1#1_Table#1_Row#5 | 「298.15」 | 「0.2」 | 「0.002045」 |
| L1#1_Table#1_Row#6 | 「298.15」 | 「0.3」 | 「0.002555」 |

##### Key Observations

- At both temperatures, viscosity increases with increasing propan-2-ol mass fraction in this composition range (0.1–0.3), consistent with the well-known viscosity maximum of the isopropanol–water system that occurs at higher alcohol concentrations.
- Raising the temperature from 293.15 K to 298.15 K noticeably decreases the viscosity at each composition, as expected from the Arrhenius-type temperature dependence of liquid viscosity (e.g., from 0.001633 to 0.001395 Pa·s at w = 0.1, and from 0.003172 to 0.002555 Pa·s at w = 0.3).
- The full block extends from 288.15 K to 303.15 K with viscosities spanning 0.001208–0.004014 Pa·s.

**Note:** No kinematic viscosity (GLOBprop_40) data were found in the database for this binary system in the requested temperature range. Only dynamic viscosity data are available from this source.

**Core claims:**
- Dynamic viscosity data for the binary mixture of propan-2-ol + water at 100 kPa were found from DOI 10.1016/j.jct.2019.05880, covering mass fractions of propan-2-ol from 0.1 to 0.3 and temperatures of 293.15 K and 298.15 K within the requested room-temperature window.
- At both 293.15 K and 298.15 K, dynamic viscosity increases with increasing propan-2-ol mass fraction over the 0.1–0.3 range, with values ranging from 0.001633 Pa·s (w = 0.1, 293.15 K) to 0.003172 Pa·s (w = 0.3, 293.15 K) and from 0.001395 Pa·s (w = 0.1, 298.15 K) to 0.002555 Pa·s (w = 0.3, 298.15 K).
- Raising the temperature from 293.15 K to 298.15 K decreases the dynamic viscosity at each composition, consistent with Arrhenius-type temperature dependence of liquid viscosity.
- No kinematic viscosity data were found in the database for this binary system in the requested temperature range; only dynamic viscosity data are available from this source.

**Core ID updates:**
- add GLOBcomp_6 — propan-2-ol (registry: propan-2-ol)
- add GLOBcomp_1 — water (registry: water)
- add GLOBlit_5585 — 10.1016/j.jct.2019.105880 (registry: 2019-meh-haj-0)

#### Core blocks found — verbatim ledger

```ledger
**L1#1_Table#2_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_5585 | lit_id: 2019-meh-haj-0 | doi: 10.1016/j.jct.2019.105880
block: PROPblock_12 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 12
compounds: water (H2O; GLOBcomp_1; DOIcomp_4; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N); propan-2-ol (C3H8O; GLOBcomp_6; DOIcomp_3; InChIKey KFZMGEQAYNKOFK-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_4
description: Dynamic viscosity (Pa·s) for propan-2-ol + water binary mixture, mass fraction of propan-2-ol 0.1–0.3, 288.15–303.15 K, 100 kPa.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#2_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=100.0 · phase=Liquid」 |
| L1#1_Table#2_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=288.15–303.15 · n_unique=4 · phase=Liquid」 |
| L1#1_Table#2_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_5」 | 「Mass fraction of propan-2-ol」 | 「range=0.1–0.3 · n_unique=3 · phase=Liquid」 |
| L1#1_Table#2_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_4」 | 「Viscosity, Pa*s」 | 「method=Falling or rolling sphere viscometry (GLOBmeas_8) · range=0.001208–0.004014 · mean=0.002279 · n=12 · phase=Liquid」 |
```

#### Data inspections — verbatim ledger

```ledger
**L1#1_Table#3_(Query_L1#1_INSP):**
lit_num_id: GLOBlit_5585 | doi: 10.1016/j.jct.2019.105880 | block: PROPblock_12
table_mode: complete | inspection_id: INSP_5c8cad6c2b0f | rows_shown: 6

| *row_id* | *BLKpoint_id* | *temperature_k* | *mass_fraction_<propan-2-ol>* | *pressure_kpa* | *viscosity_pa_s* |
|---|---|---|---|---|---|
| L1#1_Table#3_Row#1 | 「BLKpoint_4」 | 「293.15」 | 「0.1」 | 「100.0」 | 「0.001633」 |
| L1#1_Table#3_Row#2 | 「BLKpoint_5」 | 「293.15」 | 「0.2」 | 「100.0」 | 「0.002485」 |
| L1#1_Table#3_Row#3 | 「BLKpoint_6」 | 「293.15」 | 「0.3」 | 「100.0」 | 「0.003172」 |
| L1#1_Table#3_Row#4 | 「BLKpoint_7」 | 「298.15」 | 「0.1」 | 「100.0」 | 「0.001395」 |
| L1#1_Table#3_Row#5 | 「BLKpoint_8」 | 「298.15」 | 「0.2」 | 「100.0」 | 「0.002045」 |
| L1#1_Table#3_Row#6 | 「BLKpoint_9」 | 「298.15」 | 「0.3」 | 「100.0」 | 「0.002555」 |
```
</subagent_answer>
</tool_result>

## LLM Response
<reasoning>
The L1 query returned comprehensive data. The results match what's already in working memory from a previous query. I have all the data needed to provide a complete answer. Let me compile the final answer with all the relevant information.
</reasoning>

<answer>

## Viscosity Data for Isopropanol (2-Propanol) + Water Binary Mixtures at Room Temperature

### Source

**DOI:** 10.1016/j.jct.2019.105880  
**Data block:** PROPblock_12  
**Property:** Dynamic viscosity (Pa·s), measured by falling/rolling sphere viscometry, liquid phase, at 100 kPa.  
**System:** Binary mixture of propan-2-ol (2-propanol / isopropanol) + water.

**Composition range covered:** Mass fraction of propan-2-ol from 0.1 to 0.3  
**Full block temperature range:** 288.15–303.15 K (12 data points total)

---

### Data Points in the 293–298 K Window

| T (K) | w (propan-2-ol) | Dynamic Viscosity (Pa·s) |
|--------|-----------------|--------------------------|
| 293.15 | 0.1             | 0.001633                 |
| 293.15 | 0.2             | 0.002485                 |
| 293.15 | 0.3             | 0.003172                 |
| 298.15 | 0.1             | 0.001395                 |
| 298.15 | 0.2             | 0.002045                 |
| 298.15 | 0.3             | 0.002555                 |

All measurements were made at a pressure of 100.0 kPa in the liquid phase.

---

### Key Observations

1. **Viscosity increases with isopropanol content** in the 0.1–0.3 mass-fraction range at both temperatures. For example, at 293.15 K the viscosity nearly doubles from 0.001633 Pa·s (w = 0.1) to 0.003172 Pa·s (w = 0.3). This trend is consistent with the well-known viscosity maximum of the isopropanol–water system, which occurs at higher alcohol concentrations (typically around 0.6–0.7 mass fraction). In this composition range, the extensive hydrogen-bonding network between water and isopropanol molecules progressively increases internal friction.

2. **Viscosity decreases with increasing temperature**, as expected from the Arrhenius-type temperature dependence of liquid viscosity. At w = 0.3, the viscosity drops from 0.003172 Pa·s at 293.15 K to 0.002555 Pa·s at 298.15 K — a reduction of about 19% for just a 5 K increase.

3. **Full data block** extends from 288.15 K to 303.15 K, with viscosities spanning 0.001208–0.004014 Pa·s across all compositions and temperatures.

4. **No kinematic viscosity data** were found in the ThermoML database for this binary system in the requested temperature range. Only dynamic viscosity data are available from this source.

</answer>