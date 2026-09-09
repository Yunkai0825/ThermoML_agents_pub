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
- [L1] Find dynamic viscosity data for water + ethylene glycol binary mixtures across composition range → stored as L1_query_1 · validation: FLAGGED(2)
- [L1] Find excess molar enthalpy (Hᴱ) data for water + ethylene glycol (1,2-ethanediol) binary mixtures to quantify thermodyna → stored as L1_query_2 · validation: FLAGGED(1)

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: FLAGGED(2)

**Summary:** The ThermoML database contains 7 data blocks for dynamic viscosity of the water + ethylene glycol (1,2-ethanediol) binary system. The most comprehensive block covering the full composition range is GLOBlit_6951::PROPblock_18 (DOI: 10.1021/acs.jced.6b00526), with 33 data points measured by the falling/rolling sphere method at 100.0 kPa, spanning temperatures 293.15–303.15 K and water mole fractions from 0 to 1.0. Viscosity ranges from 0.000755 to 0.02113 Pa·s across all points. At 293.15 K, pure ethylene glycol has a viscosity of 0.02113 Pa·s and pure water 0.000949 Pa·s. The composition dependence is highly nonlinear, with substantial positive deviations from a log-linear ideal mixing rule, attributed to strong intermolecular hydrogen bonding between water and ethylene glycol. Temperature strongly reduces viscosity across all compositions, with pure EG viscosity dropping from 0.02113 Pa·s at 293.15 K to 0.01423 Pa·s at 303.15 K.

**Answer:**

#### Dynamic Viscosity Data for Water + Ethylene Glycol Binary Mixtures

##### Data Overview

The ThermoML database contains **7 data blocks** for the water (GLOBcomp_1) + 1,2-ethanediol/ethylene glycol (GLOBcomp_24) binary system with dynamic viscosity (GLOBprop_4) measurements. These blocks span a range of temperatures, compositions, and experimental methods from multiple literature sources.

The most comprehensive single block covering the full composition range is **GLOBlit_6951::PROPblock_18** (DOI: 10.1021/acs.jced.6b00526), which contains 33 data points measured by the falling/rolling sphere method at a fixed pressure of 100.0 kPa, covering temperatures 293.15–303.15 K and mole fraction of water from 0 to 1.0.

##### Composition-Dependent Viscosity Data

From **GLOBlit_6951::PROPblock_18** (inspected):

**At 293.15 K:**

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *x(water)* | *Viscosity (Pa·s)* |
|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「0 (pure EG)」 | 「0.02113」 |
| WM_L1#1_Table#1_Row#2 | 「0.2014」 | 「0.01495」 |
| WM_L1#1_Table#1_Row#3 | 「0.4011」 | 「0.01005」 |
| WM_L1#1_Table#1_Row#4 | 「0.6995」 | 「0.004584」 |
| WM_L1#1_Table#1_Row#5 | 「1.0 (pure water)」 | 「0.000949」 |

**At 298.15 K:**

**WM_L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *x(water)* | *Viscosity (Pa·s)* |
|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「0 (pure EG)」 | 「0.01724」 |
| WM_L1#1_Table#2_Row#2 | 「0.2014」 | 「0.01219」 |
| WM_L1#1_Table#2_Row#3 | 「0.4011」 | 「0.00831」 |
| WM_L1#1_Table#2_Row#4 | 「0.6995」 | 「0.003884」 |
| WM_L1#1_Table#2_Row#5 | 「1.0 (pure water)」 | 「0.000843」 |

**At 303.15 K:**

**WM_L1#1_Table#3_(Query_L1#1_Answer):**

| *row_id* | *x(water)* | *Viscosity (Pa·s)* |
|---|---|---|
| WM_L1#1_Table#3_Row#1 | 「0 (pure EG)」 | 「0.01423」 |
| WM_L1#1_Table#3_Row#2 | 「0.2014」 | 「0.01014」 |
| WM_L1#1_Table#3_Row#3 | 「0.4969」 | 「0.005653」 |
| WM_L1#1_Table#3_Row#4 | 「1.0 (pure water)」 | 「0.000755」 |

Overall stats for this block: viscosity ranges from **0.000755 to 0.02113 Pa·s** across all 33 data points.

##### Non-Ideal Mixing Behavior

The data reveal **strongly non-ideal mixing** in the viscosity of this system:

- Pure ethylene glycol is **far more viscous** than pure water at 293.15 K (0.02113 vs. 0.000949 Pa·s — a ratio of approximately 0.02113 ÷ 0.000949 ≈ 22, derived by dividing the two inspected endpoint values).
- The composition dependence is highly nonlinear. Under a simple log-linear (Arrhenius) ideal mixing rule at 293.15 K, the estimated viscosity at x(water) = 0.4011 would be approximately 0.006 Pa·s (derived calculation: exp((1 − 0.4011) × ln(0.02113) + 0.4011 × ln(0.000949)), where 1 − 0.4011 = 0.5989 is the complementary EG mole fraction), but the measured value is **0.01005 Pa·s** — a substantial **positive deviation** (derived comparison: the measured value is roughly 65% higher than the log-linear ideal estimate).
- This positive excess viscosity is characteristic of systems with strong intermolecular hydrogen bonding between the two components. Water and ethylene glycol form extensive H-bond networks, with EG acting as both donor and acceptor through its two hydroxyl groups, creating more structured and viscous mixtures than ideal mixing would predict.
- Temperature strongly reduces viscosity across all compositions, with pure EG viscosity dropping from 0.02113 Pa·s at 293.15 K to 0.01423 Pa·s at 303.15 K (a ~33% decrease over just 10 K; derived from inspected values).

This system is a textbook example of how hydrogen-bonding interactions between unlike molecules can produce transport-property deviations well beyond what thermodynamic excess Gibbs energy alone would suggest.

**Core claims:**
- The ThermoML database contains 7 data blocks for the water + ethylene glycol binary system with dynamic viscosity measurements, with the most comprehensive single block (GLOBlit_6951::PROPblock_18) covering 33 data points at 100.0 kPa, temperatures 293.15–303.15 K, and water mole fractions from 0 to 1.0.
- At 293.15 K, the dynamic viscosity decreases monotonically from 0.02113 Pa·s for pure ethylene glycol to 0.000949 Pa·s for pure water, spanning roughly a factor of 22 in magnitude.
- The composition dependence of viscosity is highly nonlinear, with the measured viscosity at x(water) = 0.4011 and 293.15 K being 0.01005 Pa·s, which represents a substantial positive deviation above a log-linear (Arrhenius) ideal mixing estimate, indicative of strongly non-ideal mixing attributed to extensive intermolecular hydrogen bonding between water and ethylene glycol.
- Temperature strongly reduces viscosity across all compositions; pure ethylene glycol viscosity drops from 0.02113 Pa·s at 293.15 K to 0.01423 Pa·s at 303.15 K over a 10 K interval.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#4 | 「GLOBlit_6951」 | 「PROPblock_18」 | 「GLOBcomp_24, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity measurements for water + 1,2-ethanediol (ethylene glycol) binary mixtures across full composition range at 293.15–303.15 K and 100.0 kPa, measured by falling/rolling sphere method.」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(2) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNGROUNDED_LITERAL** GLOBlit_6951::PROPblock_18: 22 (near '…000949 Pa·s — a ratio of approximately 0.02113 ÷ 0.000949 ≈ …') matches no inspected row/stat, database table, or other source of GLOBlit_6951::PROPblock_18
- **UNGROUNDED_LITERAL** GLOBlit_6951::PROPblock_18: 0.5989 (near '…× ln(0.02113) + 0.4011 × ln(0.000949)), where 1 - 0.4011 = 0…') matches no inspected row/stat, database table, or other source of GLOBlit_6951::PROPblock_18
### L1_query_2
**L1_query_2** — status: success · validation: FLAGGED(1)

**Summary:** The ThermoML database (DOI 10.1016/j.tca.2009.06.004) contains 13 excess molar enthalpy (Hᴱ) data points for the water + ethylene glycol binary system measured at 298.15 K and 101.0 kPa, spanning x(water) = 0.1014 to 0.915. Hᴱ is negative (exothermic) across the entire composition range, with the most exothermic value of −0.715 kJ/mol occurring at x(water) = 0.669, corresponding to roughly a 2:1 water-to-EG molar ratio. The Hᴱ curve is asymmetric, with the minimum shifted toward the water-rich side, consistent with the stoichiometry of hydrogen-bond formation involving ethylene glycol's two hydroxyl groups. The moderate magnitude of the exothermic mixing reflects partial disruption of existing hydrogen-bond networks in both pure components before new cross-interactions form.

**Answer:**

#### Excess Molar Enthalpy (Hᴱ) Data for Water + Ethylene Glycol Binary Mixtures

##### Data Source

The ThermoML database contains **1 data block** with excess molar enthalpy measurements for the water (GLOBcomp_1) + 1,2-ethanediol/ethylene glycol (GLOBcomp_24) binary system:

- **GLOBlit_5843::PROPblock_1** (DOI: 10.1016/j.tca.2009.06.004)
- **13 data points** measured by Calvet calorimetry at **298.15 K** and **101.0 kPa**
- Composition range: x(water) = 0.1014 to 0.915

##### Complete Composition-Dependent Hᴱ Data at 298.15 K

**WM_L1#2_Table#1_(Query_L1#2_Answer):**

| *row_id* | *x(water)* | *Hᴱ (kJ/mol)* |
|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「0.1014」 | 「−0.174」 |
| WM_L1#2_Table#1_Row#2 | 「0.1994」 | 「−0.337」 |
| WM_L1#2_Table#1_Row#3 | 「0.2091」 | 「−0.347」 |
| WM_L1#2_Table#1_Row#4 | 「0.3051」 | 「−0.48」 |
| WM_L1#2_Table#1_Row#5 | 「0.3674」 | 「−0.559」 |
| WM_L1#2_Table#1_Row#6 | 「0.3995」 | 「−0.59」 |
| WM_L1#2_Table#1_Row#7 | 「0.4807」 | 「−0.64」 |
| WM_L1#2_Table#1_Row#8 | 「0.5455」 | 「−0.666」 |
| WM_L1#2_Table#1_Row#9 | 「0.6144」 | 「−0.698」 |
| WM_L1#2_Table#1_Row#10 | 「0.669」 | 「−0.715」 |
| WM_L1#2_Table#1_Row#11 | 「0.7949」 | 「−0.681」 |
| WM_L1#2_Table#1_Row#12 | 「0.8656」 | 「−0.57」 |
| WM_L1#2_Table#1_Row#13 | 「0.915」 | 「−0.423」 |

##### Key Observations

- **Sign:** Hᴱ is **negative (exothermic)** across the entire measured composition range, indicating that mixing water and ethylene glycol releases heat.

- **Magnitude and extremum:** The minimum (most exothermic) value is **−0.715 kJ/mol at x(water) = 0.669**, corresponding to approximately a 2:1 water-to-EG molar ratio. The topology is non-monotonic with one extremum.

- **Asymmetry:** The Hᴱ curve is asymmetric, with the minimum shifted toward the water-rich side (x(water) ≈ 0.67 rather than 0.5). This is consistent with the stoichiometry of hydrogen-bond formation: each ethylene glycol molecule has two hydroxyl groups that can each interact with water molecules, so the optimal interaction occurs when there is an excess of water relative to EG.

- **Connection to viscosity non-ideality:** The negative Hᴱ values confirm strong, favorable intermolecular interactions (hydrogen bonding) between water and ethylene glycol. This thermodynamic evidence of exothermic mixing is consistent with the positive excess viscosity previously found in the viscosity data for this system (from prior working memory, not inspected in this run): the same hydrogen-bonding network that releases enthalpy upon mixing also creates more structured, viscous solutions than ideal mixing would predict.

- **Moderate magnitude:** While clearly exothermic, the maximum absolute magnitude of Hᴱ is |−0.715| = 0.715 kJ/mol (derived: absolute value of the inspected minimum at x(water) = 0.669), which is moderate compared to strongly associating systems, reflecting the fact that both pure components already have extensive hydrogen-bond networks that must be partially disrupted before new cross-interactions form.

**Core claims:**
- At 298.15 K and 101.0 kPa, the excess molar enthalpy (Hᴱ) of water + ethylene glycol mixtures is negative (exothermic) across the entire measured composition range x(water) = 0.1014 to 0.915, based on 13 Calvet calorimetry data points from DOI 10.1016/j.tca.2009.06.004.
- The most exothermic measured value is Hᴱ = −0.715 kJ/mol at x(water) = 0.669, indicating the Hᴱ minimum is shifted toward the water-rich side rather than at equimolar composition.
- The asymmetry of the Hᴱ curve, with its minimum near a 2:1 water-to-EG molar ratio, is consistent with the stoichiometry of hydrogen-bond formation involving ethylene glycol's two hydroxyl groups.
- The moderate magnitude of Hᴱ (maximum |Hᴱ| of 0.715 kJ/mol) reflects partial disruption of existing hydrogen-bond networks in both pure components before new cross-interactions form.

**Core blocks found:**

**WM_L1#2_Blocks_(Query_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#2 | 「GLOBlit_5843」 | 「PROPblock_1」 | 「GLOBcomp_24, GLOBcomp_1」 | 「GLOBprop_17」 | 「Excess molar enthalpy data for water + 1,2-ethanediol at 298.15 K and 101.0 kPa, 13 data points covering x(water) = 0.1014 to 0.915, measured by Calvet calorimetry.」 |

*Not stored here: 2 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(1) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNGROUNDED_LITERAL** GLOBlit_5843::PROPblock_1: 0.715 (near '…thermic, the maximum absolute magnitude of Hᴱ is |-0.715| = …') matches no inspected row/stat, database table, or other source of GLOBlit_5843::PROPblock_1



</memory>

## User
How strongly does water + ethylene glycol deviate from ideal mixing in its transport properties, and what's the chemical reason behind?

## Assistant
<summary>Planning to search ThermoML for transport property data (viscosity) on water + ethylene glycol mixtures to quantify deviations from ideal mixing behavior. Will also look for excess enthalpy data as a thermodynamic indicator of non-ideality.</summary>
<tool_call>L1_query(instruction=Search for dynami…, id_catalog=, context=User wants to und…)</tool_call>

## User
<tool_result>
<subagent_answer>
### L1#1 — L1_query return

**Status:** status=success

**Summary:** The ThermoML database contains 7 data blocks for dynamic viscosity of the water + ethylene glycol (1,2-ethanediol) binary system. The most comprehensive block covering the full composition range is GLOBlit_6951::PROPblock_18 (DOI: 10.1021/acs.jced.6b00526), with 33 data points measured by the falling/rolling sphere method at 100.0 kPa, spanning temperatures 293.15–303.15 K and water mole fractions from 0 to 1.0. Viscosity ranges from 0.000755 to 0.02113 Pa·s across all points. At 293.15 K, pure ethylene glycol has a viscosity of 0.02113 Pa·s and pure water 0.000949 Pa·s. The composition dependence is highly nonlinear, with substantial positive deviations from a log-linear ideal mixing rule, attributed to strong intermolecular hydrogen bonding between water and ethylene glycol. Temperature strongly reduces viscosity across all compositions, with pure EG viscosity dropping from 0.02113 Pa·s at 293.15 K to 0.01423 Pa·s at 303.15 K.

**Answer:**

#### Dynamic Viscosity Data for Water + Ethylene Glycol Binary Mixtures

##### Data Overview

The ThermoML database contains **7 data blocks** for the water (GLOBcomp_1) + 1,2-ethanediol/ethylene glycol (GLOBcomp_24) binary system with dynamic viscosity (GLOBprop_4) measurements. These blocks span a range of temperatures, compositions, and experimental methods from multiple literature sources.

The most comprehensive single block covering the full composition range is **GLOBlit_6951::PROPblock_18** (DOI: 10.1021/acs.jced.6b00526), which contains 33 data points measured by the falling/rolling sphere method at a fixed pressure of 100.0 kPa, covering temperatures 293.15–303.15 K and mole fraction of water from 0 to 1.0.

##### Composition-Dependent Viscosity Data

From **GLOBlit_6951::PROPblock_18** (inspected):

**At 293.15 K:**

**L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *x(water)* | *Viscosity (Pa·s)* |
|---|---|---|
| L1#1_Table#1_Row#1 | 「0 (pure EG)」 | 「0.02113」 |
| L1#1_Table#1_Row#2 | 「0.2014」 | 「0.01495」 |
| L1#1_Table#1_Row#3 | 「0.4011」 | 「0.01005」 |
| L1#1_Table#1_Row#4 | 「0.6995」 | 「0.004584」 |
| L1#1_Table#1_Row#5 | 「1.0 (pure water)」 | 「0.000949」 |

**At 298.15 K:**

**L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *x(water)* | *Viscosity (Pa·s)* |
|---|---|---|
| L1#1_Table#2_Row#1 | 「0 (pure EG)」 | 「0.01724」 |
| L1#1_Table#2_Row#2 | 「0.2014」 | 「0.01219」 |
| L1#1_Table#2_Row#3 | 「0.4011」 | 「0.00831」 |
| L1#1_Table#2_Row#4 | 「0.6995」 | 「0.003884」 |
| L1#1_Table#2_Row#5 | 「1.0 (pure water)」 | 「0.000843」 |

**At 303.15 K:**

**L1#1_Table#3_(Query_L1#1_Answer):**

| *row_id* | *x(water)* | *Viscosity (Pa·s)* |
|---|---|---|
| L1#1_Table#3_Row#1 | 「0 (pure EG)」 | 「0.01423」 |
| L1#1_Table#3_Row#2 | 「0.2014」 | 「0.01014」 |
| L1#1_Table#3_Row#3 | 「0.4969」 | 「0.005653」 |
| L1#1_Table#3_Row#4 | 「1.0 (pure water)」 | 「0.000755」 |

Overall stats for this block: viscosity ranges from **0.000755 to 0.02113 Pa·s** across all 33 data points.

##### Non-Ideal Mixing Behavior

The data reveal **strongly non-ideal mixing** in the viscosity of this system:

- Pure ethylene glycol is **far more viscous** than pure water at 293.15 K (0.02113 vs. 0.000949 Pa·s — a ratio of approximately 0.02113 ÷ 0.000949 ≈ 22, derived by dividing the two inspected endpoint values).
- The composition dependence is highly nonlinear. Under a simple log-linear (Arrhenius) ideal mixing rule at 293.15 K, the estimated viscosity at x(water) = 0.4011 would be approximately 0.006 Pa·s (derived calculation: exp((1 − 0.4011) × ln(0.02113) + 0.4011 × ln(0.000949)), where 1 − 0.4011 = 0.5989 is the complementary EG mole fraction), but the measured value is **0.01005 Pa·s** — a substantial **positive deviation** (derived comparison: the measured value is roughly 65% higher than the log-linear ideal estimate).
- This positive excess viscosity is characteristic of systems with strong intermolecular hydrogen bonding between the two components. Water and ethylene glycol form extensive H-bond networks, with EG acting as both donor and acceptor through its two hydroxyl groups, creating more structured and viscous mixtures than ideal mixing would predict.
- Temperature strongly reduces viscosity across all compositions, with pure EG viscosity dropping from 0.02113 Pa·s at 293.15 K to 0.01423 Pa·s at 303.15 K (a ~33% decrease over just 10 K; derived from inspected values).

This system is a textbook example of how hydrogen-bonding interactions between unlike molecules can produce transport-property deviations well beyond what thermodynamic excess Gibbs energy alone would suggest.

---
[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:
- **UNGROUNDED_LITERAL** GLOBlit_6951::PROPblock_18: 22 (near '…000949 Pa·s — a ratio of approximately 0.02113 ÷ 0.000949 ≈ …') matches no inspected row/stat, database table, or other source of GLOBlit_6951::PROPblock_18
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="GLOBlit_6951::PROPblock_18", nearest={"column": "temperature_k", "value": 22.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** GLOBlit_6951::PROPblock_18: 0.5989 (near '…× ln(0.02113) + 0.4011 × ln(0.000949)), where 1 - 0.4011 = 0…') matches no inspected row/stat, database table, or other source of GLOBlit_6951::PROPblock_18
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="GLOBlit_6951::PROPblock_18", nearest={"column": "temperature_k", "value": 0.5989})` — if it is a value you computed or an external reference, keep it and label its provenance instead
Inspected so far: PROPblock_18

**Core claims:**
- The ThermoML database contains 7 data blocks for the water + ethylene glycol binary system with dynamic viscosity measurements, with the most comprehensive single block (GLOBlit_6951::PROPblock_18) covering 33 data points at 100.0 kPa, temperatures 293.15–303.15 K, and water mole fractions from 0 to 1.0.
- At 293.15 K, the dynamic viscosity decreases monotonically from 0.02113 Pa·s for pure ethylene glycol to 0.000949 Pa·s for pure water, spanning roughly a factor of 22 in magnitude.
- The composition dependence of viscosity is highly nonlinear, with the measured viscosity at x(water) = 0.4011 and 293.15 K being 0.01005 Pa·s, which represents a substantial positive deviation above a log-linear (Arrhenius) ideal mixing estimate, indicative of strongly non-ideal mixing attributed to extensive intermolecular hydrogen bonding between water and ethylene glycol.
- Temperature strongly reduces viscosity across all compositions; pure ethylene glycol viscosity drops from 0.02113 Pa·s at 293.15 K to 0.01423 Pa·s at 303.15 K over a 10 K interval.

#### Core blocks found — verbatim ledger

```ledger
**L1#1_Table#4_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_6951 | lit_id: 2017-moo-ros-0 | doi: 10.1021/acs.jced.6b00526
block: PROPblock_18 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 33
compounds: 1,2-ethanediol (C2H6O2; GLOBcomp_24; DOIcomp_1; InChIKey LYCAIKOWRPUZTN-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_5; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_4
description: Dynamic viscosity measurements for water + 1,2-ethanediol (ethylene glycol) binary mixtures across full composition range at 293.15–303.15 K and 100.0 kPa, measured by falling/rolling sphere method.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#4_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=100.0 · phase=Liquid」 |
| L1#1_Table#4_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=293.15–303.15 · n_unique=3 · phase=Liquid」 |
| L1#1_Table#4_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_2」 | 「Mole fraction of water」 | 「range=0.0–1.0 · n_unique=11 · phase=Liquid」 |
| L1#1_Table#4_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_4」 | 「Viscosity, Pa*s」 | 「method=Falling or rolling sphere viscometry (GLOBmeas_8) · range=0.000755–0.02113 · mean=0.007699 · n=33 · phase=Liquid」 |
```

#### Data inspections — verbatim ledger

```ledger
**L1#1_Table#5_(Query_L1#1_INSP):**
lit_num_id: GLOBlit_6951 | doi: 10.1021/acs.jced.6b00526 | block: PROPblock_18
table_mode: rdp | inspection_id: INSP_bdb58d28aae5 | rows_shown: 14

| *row_id* | *BLKpoint_id* | *temperature_k* | *mole_fraction_<water>* | *pressure_kpa* | *viscosity_pa_s* |
|---|---|---|---|---|---|
| L1#1_Table#5_Row#1 | 「BLKpoint_1」 | 「293.15」 | 「0」 | 「100.0」 | 「0.02113」 |
| L1#1_Table#5_Row#2 | 「BLKpoint_3」 | 「293.15」 | 「0.2014」 | 「100.0」 | 「0.01495」 |
| L1#1_Table#5_Row#3 | 「BLKpoint_5」 | 「293.15」 | 「0.4011」 | 「100.0」 | 「0.01005」 |
| L1#1_Table#5_Row#4 | 「BLKpoint_8」 | 「293.15」 | 「0.6995」 | 「100.0」 | 「0.004584」 |
| L1#1_Table#5_Row#5 | 「BLKpoint_11」 | 「293.15」 | 「1」 | 「100.0」 | 「0.000949」 |
| L1#1_Table#5_Row#6 | 「BLKpoint_12」 | 「298.15」 | 「0」 | 「100.0」 | 「0.01724」 |
| L1#1_Table#5_Row#7 | 「BLKpoint_14」 | 「298.15」 | 「0.2014」 | 「100.0」 | 「0.01219」 |
| L1#1_Table#5_Row#8 | 「BLKpoint_16」 | 「298.15」 | 「0.4011」 | 「100.0」 | 「0.00831」 |
| L1#1_Table#5_Row#9 | 「BLKpoint_19」 | 「298.15」 | 「0.6995」 | 「100.0」 | 「0.003884」 |
| L1#1_Table#5_Row#10 | 「BLKpoint_22」 | 「298.15」 | 「1」 | 「100.0」 | 「0.000843」 |
| L1#1_Table#5_Row#11 | 「BLKpoint_23」 | 「303.15」 | 「0」 | 「100.0」 | 「0.01423」 |
| L1#1_Table#5_Row#12 | 「BLKpoint_25」 | 「303.15」 | 「0.2014」 | 「100.0」 | 「0.01014」 |
| L1#1_Table#5_Row#13 | 「BLKpoint_28」 | 「303.15」 | 「0.4969」 | 「100.0」 | 「0.005653」 |
| L1#1_Table#5_Row#14 | 「BLKpoint_33」 | 「303.15」 | 「1」 | 「100.0」 | 「0.000755」 |
```
</subagent_answer>
</tool_result>

## Assistant
<summary>Received comprehensive viscosity data for water + EG from GLOBlit_6951::PROPblock_18. Now searching for excess molar enthalpy (Hᴱ) data for the same system to provide thermodynamic evidence of the hydrogen-bonding interactions driving transport property deviations.</summary>
<tool_call>L1_query(instruction=Search for excess…, id_catalog=GLOBcomp_1=water,…, context=User is …)</tool_call>

## User
<tool_result>
<subagent_answer>
### L1#2 — L1_query return

**Status:** status=success

**Summary:** The ThermoML database (DOI 10.1016/j.tca.2009.06.004) contains 13 excess molar enthalpy (Hᴱ) data points for the water + ethylene glycol binary system measured at 298.15 K and 101.0 kPa, spanning x(water) = 0.1014 to 0.915. Hᴱ is negative (exothermic) across the entire composition range, with the most exothermic value of −0.715 kJ/mol occurring at x(water) = 0.669, corresponding to roughly a 2:1 water-to-EG molar ratio. The Hᴱ curve is asymmetric, with the minimum shifted toward the water-rich side, consistent with the stoichiometry of hydrogen-bond formation involving ethylene glycol's two hydroxyl groups. The moderate magnitude of the exothermic mixing reflects partial disruption of existing hydrogen-bond networks in both pure components before new cross-interactions form.

**Answer:**

#### Excess Molar Enthalpy (Hᴱ) Data for Water + Ethylene Glycol Binary Mixtures

##### Data Source

The ThermoML database contains **1 data block** with excess molar enthalpy measurements for the water (GLOBcomp_1) + 1,2-ethanediol/ethylene glycol (GLOBcomp_24) binary system:

- **GLOBlit_5843::PROPblock_1** (DOI: 10.1016/j.tca.2009.06.004)
- **13 data points** measured by Calvet calorimetry at **298.15 K** and **101.0 kPa**
- Composition range: x(water) = 0.1014 to 0.915

##### Complete Composition-Dependent Hᴱ Data at 298.15 K

**L1#2_Table#1_(Query_L1#2_Answer):**

| *row_id* | *x(water)* | *Hᴱ (kJ/mol)* |
|---|---|---|
| L1#2_Table#1_Row#1 | 「0.1014」 | 「−0.174」 |
| L1#2_Table#1_Row#2 | 「0.1994」 | 「−0.337」 |
| L1#2_Table#1_Row#3 | 「0.2091」 | 「−0.347」 |
| L1#2_Table#1_Row#4 | 「0.3051」 | 「−0.48」 |
| L1#2_Table#1_Row#5 | 「0.3674」 | 「−0.559」 |
| L1#2_Table#1_Row#6 | 「0.3995」 | 「−0.59」 |
| L1#2_Table#1_Row#7 | 「0.4807」 | 「−0.64」 |
| L1#2_Table#1_Row#8 | 「0.5455」 | 「−0.666」 |
| L1#2_Table#1_Row#9 | 「0.6144」 | 「−0.698」 |
| L1#2_Table#1_Row#10 | 「0.669」 | 「−0.715」 |
| L1#2_Table#1_Row#11 | 「0.7949」 | 「−0.681」 |
| L1#2_Table#1_Row#12 | 「0.8656」 | 「−0.57」 |
| L1#2_Table#1_Row#13 | 「0.915」 | 「−0.423」 |

##### Key Observations

- **Sign:** Hᴱ is **negative (exothermic)** across the entire measured composition range, indicating that mixing water and ethylene glycol releases heat.

- **Magnitude and extremum:** The minimum (most exothermic) value is **−0.715 kJ/mol at x(water) = 0.669**, corresponding to approximately a 2:1 water-to-EG molar ratio. The topology is non-monotonic with one extremum.

- **Asymmetry:** The Hᴱ curve is asymmetric, with the minimum shifted toward the water-rich side (x(water) ≈ 0.67 rather than 0.5). This is consistent with the stoichiometry of hydrogen-bond formation: each ethylene glycol molecule has two hydroxyl groups that can each interact with water molecules, so the optimal interaction occurs when there is an excess of water relative to EG.

- **Connection to viscosity non-ideality:** The negative Hᴱ values confirm strong, favorable intermolecular interactions (hydrogen bonding) between water and ethylene glycol. This thermodynamic evidence of exothermic mixing is consistent with the positive excess viscosity previously found in the viscosity data for this system (from prior working memory, not inspected in this run): the same hydrogen-bonding network that releases enthalpy upon mixing also creates more structured, viscous solutions than ideal mixing would predict.

- **Moderate magnitude:** While clearly exothermic, the maximum absolute magnitude of Hᴱ is |−0.715| = 0.715 kJ/mol (derived: absolute value of the inspected minimum at x(water) = 0.669), which is moderate compared to strongly associating systems, reflecting the fact that both pure components already have extensive hydrogen-bond networks that must be partially disrupted before new cross-interactions form.

---
[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:
- **UNGROUNDED_LITERAL** GLOBlit_5843::PROPblock_1: 0.715 (near '…thermic, the maximum absolute magnitude of Hᴱ is |-0.715| = …') matches no inspected row/stat, database table, or other source of GLOBlit_5843::PROPblock_1
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="GLOBlit_5843::PROPblock_1", nearest={"column": "mole_fraction_<water>", "value": 0.715})` — if it is a value you computed or an external reference, keep it and label its provenance instead
Inspected so far: PROPblock_1

**Core claims:**
- At 298.15 K and 101.0 kPa, the excess molar enthalpy (Hᴱ) of water + ethylene glycol mixtures is negative (exothermic) across the entire measured composition range x(water) = 0.1014 to 0.915, based on 13 Calvet calorimetry data points from DOI 10.1016/j.tca.2009.06.004.
- The most exothermic measured value is Hᴱ = −0.715 kJ/mol at x(water) = 0.669, indicating the Hᴱ minimum is shifted toward the water-rich side rather than at equimolar composition.
- The asymmetry of the Hᴱ curve, with its minimum near a 2:1 water-to-EG molar ratio, is consistent with the stoichiometry of hydrogen-bond formation involving ethylene glycol's two hydroxyl groups.
- The moderate magnitude of Hᴱ (maximum |Hᴱ| of 0.715 kJ/mol) reflects partial disruption of existing hydrogen-bond networks in both pure components before new cross-interactions form.

#### Core blocks found — verbatim ledger

```ledger
**L1#2_Table#2_(Query_L1#2_CoreBLK):**
lit_num_id: GLOBlit_5843 | lit_id: 2009-zeh-coq-1 | doi: 10.1016/j.tca.2009.06.004
block: PROPblock_1 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 13
compounds: 1,2-ethanediol (C2H6O2; GLOBcomp_24; DOIcomp_2; InChIKey LYCAIKOWRPUZTN-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_6; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_17
description: Excess molar enthalpy data for water + 1,2-ethanediol at 298.15 K and 101.0 kPa, 13 data points covering x(water) = 0.1014 to 0.915, measured by Calvet calorimetry.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#2_Table#2_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_2」 | 「Temperature, K」 | 「value=298.15 · phase=Liquid」 |
| L1#2_Table#2_Row#2 | 「constraint」 | 「BLKconstr_2/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.0 · phase=Liquid」 |
| L1#2_Table#2_Row#3 | 「variable」 | 「BLKvar_1/GLOBvar_2」 | 「Mole fraction of water」 | 「range=0.1014–0.915 · n_unique=13 · phase=Liquid」 |
| L1#2_Table#2_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_17」 | 「Excess molar enthalpy (molar enthalpy of mixing), kJ/mol」 | 「method=Calvet calorimetry (GLOBmeas_13) · range=-0.715–-0.174 · mean=-0.529231 · n=13 · phase=Liquid」 |
```

#### Data inspections — verbatim ledger

```ledger
**L1#2_Table#3_(Query_L1#2_INSP):**
lit_num_id: GLOBlit_5843 | doi: 10.1016/j.tca.2009.06.004 | block: PROPblock_1
table_mode: rdp | inspection_id: INSP_2c1af1f114b2 | rows_shown: 8

| *row_id* | *BLKpoint_id* | *mole_fraction_<water>* | *temperature_k* | *pressure_kpa* | *excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol* |
|---|---|---|---|---|---|
| L1#2_Table#3_Row#1 | 「BLKpoint_1」 | 「0.1014」 | 「298.15」 | 「101.0」 | 「-0.174」 |
| L1#2_Table#3_Row#2 | 「BLKpoint_2」 | 「0.1994」 | 「298.15」 | 「101.0」 | 「-0.337」 |
| L1#2_Table#3_Row#3 | 「BLKpoint_6」 | 「0.3995」 | 「298.15」 | 「101.0」 | 「-0.59」 |
| L1#2_Table#3_Row#4 | 「BLKpoint_7」 | 「0.4807」 | 「298.15」 | 「101.0」 | 「-0.64」 |
| L1#2_Table#3_Row#5 | 「BLKpoint_10」 | 「0.669」 | 「298.15」 | 「101.0」 | 「-0.715」 |
| L1#2_Table#3_Row#6 | 「BLKpoint_11」 | 「0.7949」 | 「298.15」 | 「101.0」 | 「-0.681」 |
| L1#2_Table#3_Row#7 | 「BLKpoint_12」 | 「0.8656」 | 「298.15」 | 「101.0」 | 「-0.57」 |
| L1#2_Table#3_Row#8 | 「BLKpoint_13」 | 「0.915」 | 「298.15」 | 「101.0」 | 「-0.423」 |
```

```ledger
**L1#2_Table#4_(Query_L1#2_INSP):**
lit_num_id: GLOBlit_5843 | doi: 10.1016/j.tca.2009.06.004 | block: PROPblock_1
table_mode: complete | inspection_id: INSP_8383e8943328 | rows_shown: 8

| *row_id* | *BLKpoint_id* | *mole_fraction_<water>* | *temperature_k* | *pressure_kpa* | *excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol* |
|---|---|---|---|---|---|
| L1#2_Table#4_Row#1 | 「BLKpoint_3」 | 「0.2091」 | 「298.15」 | 「101.0」 | 「-0.347」 |
| L1#2_Table#4_Row#2 | 「BLKpoint_4」 | 「0.3051」 | 「298.15」 | 「101.0」 | 「-0.48」 |
| L1#2_Table#4_Row#3 | 「BLKpoint_5」 | 「0.3674」 | 「298.15」 | 「101.0」 | 「-0.559」 |
| L1#2_Table#4_Row#4 | 「BLKpoint_6」 | 「0.3995」 | 「298.15」 | 「101.0」 | 「-0.59」 |
| L1#2_Table#4_Row#5 | 「BLKpoint_7」 | 「0.4807」 | 「298.15」 | 「101.0」 | 「-0.64」 |
| L1#2_Table#4_Row#6 | 「BLKpoint_8」 | 「0.5455」 | 「298.15」 | 「101.0」 | 「-0.666」 |
| L1#2_Table#4_Row#7 | 「BLKpoint_9」 | 「0.6144」 | 「298.15」 | 「101.0」 | 「-0.698」 |
| L1#2_Table#4_Row#8 | 「BLKpoint_10」 | 「0.669」 | 「298.15」 | 「101.0」 | 「-0.715」 |
```
</subagent_answer>
</tool_result>

## LLM Response
<reasoning>
I now have comprehensive data from both queries:

1. **Dynamic viscosity** (GLOBlit_6951::PROPblock_18, DOI: 10.1021/acs.jced.6b00526): 33 data points at 293.15–303.15 K, full composition range. Shows strongly nonlinear composition dependence with positive excess viscosity.

2. **Excess molar enthalpy** (GLOBlit_5843::PROPblock_1, DOI: 10.1016/j.tca.2009.06.004): 13 data points at 298.15 K, x(water) = 0.1014–0.915. All negative (exothermic), minimum at −0.715 kJ/mol at x(water) = 0.669.

The flagged values (22, 0.5989, 0.715) are all derived calculations, not database values, so they're fine to use as long as I label them as derived. Let me compose a comprehensive final answer.

Key points to make:
- Quantify the deviation: at x(water) = 0.4011 and 293.15 K, measured viscosity is 0.01005 Pa·s vs. a log-linear ideal estimate of ~0.006 Pa·s (derived), roughly 65% positive deviation
- The Hᴱ data confirms strong favorable cross-interactions
- Chemical explanation: hydrogen bonding between water and EG's two –OH groups
- The Hᴱ minimum at x(water) ≈ 0.669 (~2:1 water:EG ratio) matches the stoichiometry of H-bond formation with EG's two hydroxyl groups
</reasoning>

<answer>
## Non-Ideal Transport Properties of Water + Ethylene Glycol Mixtures

The water + ethylene glycol (1,2-ethanediol) binary system shows **strongly non-ideal mixing** in its transport properties, and the ThermoML database provides both viscosity and thermodynamic data that quantify and explain this behavior.

---

### 1. Dynamic Viscosity — Large Positive Deviations

From **GLOBlit_6951::PROPblock_18** (DOI: 10.1021/acs.jced.6b00526), 33 data points were measured by falling/rolling sphere viscometry at 100.0 kPa across the full composition range.

**Viscosity across composition at 293.15 K:**

| x(water) | Viscosity (Pa·s) |
|-----------|-----------------|
| 0 (pure EG) | 0.02113 |
| 0.2014 | 0.01495 |
| 0.4011 | 0.01005 |
| 0.6995 | 0.004584 |
| 1.0 (pure water) | 0.000949 |

**At 298.15 K:**

| x(water) | Viscosity (Pa·s) |
|-----------|-----------------|
| 0 (pure EG) | 0.01724 |
| 0.2014 | 0.01219 |
| 0.4011 | 0.00831 |
| 0.6995 | 0.003884 |
| 1.0 (pure water) | 0.000843 |

**At 303.15 K:**

| x(water) | Viscosity (Pa·s) |
|-----------|-----------------|
| 0 (pure EG) | 0.01423 |
| 0.2014 | 0.01014 |
| 0.4969 | 0.005653 |
| 1.0 (pure water) | 0.000755 |

#### How large is the deviation?

Pure ethylene glycol is roughly **22× more viscous** than pure water at 293.15 K (0.02113 vs. 0.000949 Pa·s; ratio derived from the two endpoint values). Under a log-linear (Arrhenius) ideal mixing rule, the viscosity at x(water) = 0.4011 would be approximately 0.006 Pa·s (derived: exp[0.5989 × ln(0.02113) + 0.4011 × ln(0.000949)]). The **measured value is 0.01005 Pa·s** — a substantial **positive deviation of roughly +65%** above the ideal estimate. This means the mixture is significantly more viscous than one would predict from a simple interpolation between the pure-component values.

Temperature strongly reduces viscosity at all compositions: pure EG drops from 0.02113 Pa·s at 293.15 K to 0.01423 Pa·s at 303.15 K — about a 33% decrease over just 10 K (derived from the inspected endpoint values).

---

### 2. Excess Molar Enthalpy — Thermodynamic Confirmation

From **GLOBlit_5843::PROPblock_1** (DOI: 10.1016/j.tca.2009.06.004), 13 Calvet calorimetry data points at 298.15 K and 101.0 kPa:

| x(water) | Hᴱ (kJ/mol) |
|-----------|-------------|
| 0.1014 | −0.174 |
| 0.1994 | −0.337 |
| 0.2091 | −0.347 |
| 0.3051 | −0.48 |
| 0.3674 | −0.559 |
| 0.3995 | −0.59 |
| 0.4807 | −0.64 |
| 0.5455 | −0.666 |
| 0.6144 | −0.698 |
| 0.669 | **−0.715** |
| 0.7949 | −0.681 |
| 0.8656 | −0.57 |
| 0.915 | −0.423 |

Hᴱ is **negative (exothermic) across the entire composition range**, confirming that mixing water and ethylene glycol is energetically favorable. The most exothermic point is **−0.715 kJ/mol at x(water) = 0.669**, corresponding to roughly a **2:1 water-to-EG molar ratio**.

---

### 3. The Chemical Explanation

The non-ideal transport behavior has a clear molecular origin: **extensive cross-species hydrogen bonding**.

- **Ethylene glycol has two hydroxyl (–OH) groups** on adjacent carbons, making it both a strong hydrogen-bond donor and acceptor. Each –OH group can form hydrogen bonds with water molecules.

- **The Hᴱ minimum at x(water) ≈ 0.67** (a 2:1 water:EG ratio) is chemically significant — it matches the stoichiometry where each of EG's two –OH groups is optimally solvated by one water molecule. This is the composition of maximum cross-interaction.

- **The asymmetry of the Hᴱ curve** (minimum shifted toward the water-rich side rather than at x = 0.5) directly reflects this 2:1 stoichiometry.

- **Why positive excess viscosity?** When water and EG mix, they form a more extensive and structured hydrogen-bond network than exists in either pure component alone. These cross-linked H-bond clusters resist flow more effectively than the individual pure-component networks, producing viscosities that exceed the ideal mixing prediction. The same favorable interactions that release enthalpy (negative Hᴱ) also create more rigid, cooperative molecular structures that increase viscous drag.

- **Why is the Hᴱ magnitude moderate** (|Hᴱ|_max = 0.715 kJ/mol)? Both pure water and pure ethylene glycol already possess extensive hydrogen-bond networks. Mixing requires **partial disruption** of these existing networks before new, favorable water–EG bonds can form. The observed Hᴱ is the net balance: the energy cost of breaking some water–water and EG–EG bonds is partially offset by the energy released from forming water–EG bonds. The net exotherm confirms that the cross-interactions are thermodynamically preferred, but the magnitude is tempered by the disruption cost.

### Summary

The water + ethylene glycol system deviates strongly from ideal mixing in its viscosity — measured values exceed log-linear ideal predictions by roughly 65% at intermediate compositions. This positive excess viscosity is driven by the formation of extensive cross-species hydrogen-bond networks, thermodynamically confirmed by uniformly negative excess molar enthalpies peaking at −0.715 kJ/mol near a 2:1 water:EG molar ratio that matches the stoichiometry of EG's two hydroxyl groups.
</answer>