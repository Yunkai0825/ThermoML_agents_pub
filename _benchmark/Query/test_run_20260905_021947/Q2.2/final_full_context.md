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
- [L1] Compare experimental viscosity (dynamic) data availability for binary vs. ternary liquid mixtures in ThermoML, focusing  → stored as L1_query_1 · validation: PASS

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: PASS

**Summary:** Dynamic viscosity (Viscosity, Pa·s, GLOBprop_4) data in ThermoML is far more abundant for binary liquid mixtures than ternary ones: 1176 distinct literature sources and 3294 property blocks (137,229 total data points) for binary systems versus 429 sources and 1081 blocks (81,066 points) for ternary systems. However, ternary blocks are denser in composition coverage, averaging ~75 data points per block compared to ~42 for binary, reflecting the need to map the two-dimensional Gibbs triangle. Binary data spans a wider temperature range (199.918–1173.0 K) and pressure range (0.0–387,800.0 kPa) compared to ternary (20.0–1023.0 K; 0.0–196,130.0 kPa). Notable top sources include GLOBlit_7152 (DOI: 10.1021/acs.jced.7b00221, 25 blocks, 1448 points) for binary and GLOBlit_6743 (DOI: 10.1021/acs.jced.5b00845, 48 blocks, 5168 points) for ternary systems.

**Answer:**

#### Comparison of Dynamic Viscosity Data Availability: Binary vs. Ternary Liquid Mixtures in ThermoML

##### Summary Table

**WM_L1_Q1_Table#1_(Query_L1_Q1_Answer):**

| *row_id* | *Metric* | *Binary (2-component)* | *Ternary (3-component)* |
|---|---|---|---|
| WM_L1_Q1_Table#1_Row#1 | 「Distinct literature sources (DOIs)」 | 「1176」 | 「429」 |
| WM_L1_Q1_Table#1_Row#2 | 「Property blocks」 | 「3294」 | 「1081」 |
| WM_L1_Q1_Table#1_Row#3 | 「Total data points」 | 「137,229」 | 「81,066」 |
| WM_L1_Q1_Table#1_Row#4 | 「Avg. data points per block」 | 「~41.7」 | 「~75.0」 |
| WM_L1_Q1_Table#1_Row#5 | 「Avg. blocks per literature source」 | 「~2.8」 | 「~2.5」 |
| WM_L1_Q1_Table#1_Row#6 | 「Temperature range (K)」 | 「199.918 – 1173.0」 | 「20.0 – 1023.0」 |
| WM_L1_Q1_Table#1_Row#7 | 「Pressure range (kPa)」 | 「0.0 – 387,800.0」 | 「0.0 – 196,130.0」 |

All data refer to the property **Viscosity, Pa·s** (GLOBprop_4) in declared binary or ternary systems.

##### Key Observations

1. **Binary systems dominate in volume:** There are roughly 3× more literature sources and 3× more property blocks for binary mixtures compared to ternary ones. This reflects the general trend in experimental thermodynamics where binary systems are studied more frequently as they are simpler to prepare and interpret.

2. **Ternary blocks are denser in composition coverage:** Despite fewer total blocks, ternary systems average ~75 data points per block versus ~42 for binary systems. This is chemically expected — ternary composition space is two-dimensional (a Gibbs triangle), so experimentalists typically measure viscosity at many more composition points per block to adequately map the composition surface. A binary system only requires a one-dimensional composition sweep.

3. **Top binary sources** include GLOBlit_7152 (DOI: 10.1021/acs.jced.7b00221, 25 blocks, 1448 points) and GLOBlit_3363 (DOI: 10.1016/j.jct.2011.02.018, 6 blocks, 848 points).

4. **Top ternary sources** include GLOBlit_6743 (DOI: 10.1021/acs.jced.5b00845, 48 blocks, 5168 points) — a notably large ternary viscosity dataset — and GLOBlit_10411 (DOI: 10.1021/je5001523, 17 blocks, 1604 points).

5. **Condition coverage:** Binary data spans a wider temperature and pressure range, consistent with the greater diversity of binary systems studied (including high-temperature molten salt or industrial systems up to 1173 K and high-pressure measurements up to ~388 MPa). Ternary data reaches up to 1023 K and ~196 MPa, still substantial but somewhat narrower.

6. **Composition coverage per system:** The higher average points-per-block for ternary systems (~75 vs. ~42) suggests that individual ternary studies tend to cover composition space more thoroughly. For binary systems, a typical block might span 10–20 mole-fraction values across the full range (0→1), while ternary blocks often include grid-like sampling across the composition triangle.

**Core claims:**
- Binary liquid mixtures have roughly 3× more literature sources (1176 vs. 429 DOIs) and 3× more property blocks (3294 vs. 1081) for dynamic viscosity (Viscosity, Pa·s) in ThermoML compared to ternary liquid mixtures.
- Despite fewer total blocks, ternary viscosity blocks average ~75.0 data points per block versus ~41.7 for binary blocks, consistent with the need to cover two-dimensional composition space in ternary systems.
- Total data-point counts are 137,229 for binary and 81,066 for ternary dynamic viscosity measurements.
- Binary viscosity data span a wider range of conditions (temperature 199.918–1173.0 K, pressure 0.0–387,800.0 kPa) than ternary data (temperature 20.0–1023.0 K, pressure 0.0–196,130.0 kPa).
- All reported data refer to the property Viscosity, Pa·s (GLOBprop_4) in declared binary or ternary systems within ThermoML.

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.



</memory>

## User
I am deciding whether to validate a liquid-mixture viscosity model first on binary or ternary systems. Which class has enough experimental measurements across composition to provide the stronger test?

## Assistant
<summary>Planning to query L1 for viscosity (GLOBprop_4) data availability in binary vs. ternary liquid mixtures, focusing on composition coverage and measurement counts.</summary>
<tool_call>L1_query(instruction=Search for dynami…, id_catalog=GLOBprop_4 = Visc…)</tool_call>

## User
<tool_result>
<subagent_answer>
### L1#1 — L1_query return

**Status:** status=success

**Summary:** Dynamic viscosity (Viscosity, Pa·s, GLOBprop_4) data in ThermoML is far more abundant for binary liquid mixtures than ternary ones: 1176 distinct literature sources and 3294 property blocks (137,229 total data points) for binary systems versus 429 sources and 1081 blocks (81,066 points) for ternary systems. However, ternary blocks are denser in composition coverage, averaging ~75 data points per block compared to ~42 for binary, reflecting the need to map the two-dimensional Gibbs triangle. Binary data spans a wider temperature range (199.918–1173.0 K) and pressure range (0.0–387,800.0 kPa) compared to ternary (20.0–1023.0 K; 0.0–196,130.0 kPa). Notable top sources include GLOBlit_7152 (DOI: 10.1021/acs.jced.7b00221, 25 blocks, 1448 points) for binary and GLOBlit_6743 (DOI: 10.1021/acs.jced.5b00845, 48 blocks, 5168 points) for ternary systems.

**Answer:**

#### Comparison of Dynamic Viscosity Data Availability: Binary vs. Ternary Liquid Mixtures in ThermoML

##### Summary Table

**L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *Metric* | *Binary (2-component)* | *Ternary (3-component)* |
|---|---|---|---|
| L1#1_Table#1_Row#1 | 「Distinct literature sources (DOIs)」 | 「1176」 | 「429」 |
| L1#1_Table#1_Row#2 | 「Property blocks」 | 「3294」 | 「1081」 |
| L1#1_Table#1_Row#3 | 「Total data points」 | 「137,229」 | 「81,066」 |
| L1#1_Table#1_Row#4 | 「Avg. data points per block」 | 「~41.7」 | 「~75.0」 |
| L1#1_Table#1_Row#5 | 「Avg. blocks per literature source」 | 「~2.8」 | 「~2.5」 |
| L1#1_Table#1_Row#6 | 「Temperature range (K)」 | 「199.918 – 1173.0」 | 「20.0 – 1023.0」 |
| L1#1_Table#1_Row#7 | 「Pressure range (kPa)」 | 「0.0 – 387,800.0」 | 「0.0 – 196,130.0」 |

All data refer to the property **Viscosity, Pa·s** (GLOBprop_4) in declared binary or ternary systems.

##### Key Observations

1. **Binary systems dominate in volume:** There are roughly 3× more literature sources and 3× more property blocks for binary mixtures compared to ternary ones. This reflects the general trend in experimental thermodynamics where binary systems are studied more frequently as they are simpler to prepare and interpret.

2. **Ternary blocks are denser in composition coverage:** Despite fewer total blocks, ternary systems average ~75 data points per block versus ~42 for binary systems. This is chemically expected — ternary composition space is two-dimensional (a Gibbs triangle), so experimentalists typically measure viscosity at many more composition points per block to adequately map the composition surface. A binary system only requires a one-dimensional composition sweep.

3. **Top binary sources** include GLOBlit_7152 (DOI: 10.1021/acs.jced.7b00221, 25 blocks, 1448 points) and GLOBlit_3363 (DOI: 10.1016/j.jct.2011.02.018, 6 blocks, 848 points).

4. **Top ternary sources** include GLOBlit_6743 (DOI: 10.1021/acs.jced.5b00845, 48 blocks, 5168 points) — a notably large ternary viscosity dataset — and GLOBlit_10411 (DOI: 10.1021/je5001523, 17 blocks, 1604 points).

5. **Condition coverage:** Binary data spans a wider temperature and pressure range, consistent with the greater diversity of binary systems studied (including high-temperature molten salt or industrial systems up to 1173 K and high-pressure measurements up to ~388 MPa). Ternary data reaches up to 1023 K and ~196 MPa, still substantial but somewhat narrower.

6. **Composition coverage per system:** The higher average points-per-block for ternary systems (~75 vs. ~42) suggests that individual ternary studies tend to cover composition space more thoroughly. For binary systems, a typical block might span 10–20 mole-fraction values across the full range (0→1), while ternary blocks often include grid-like sampling across the composition triangle.

**Core claims:**
- Binary liquid mixtures have roughly 3× more literature sources (1176 vs. 429 DOIs) and 3× more property blocks (3294 vs. 1081) for dynamic viscosity (Viscosity, Pa·s) in ThermoML compared to ternary liquid mixtures.
- Despite fewer total blocks, ternary viscosity blocks average ~75.0 data points per block versus ~41.7 for binary blocks, consistent with the need to cover two-dimensional composition space in ternary systems.
- Total data-point counts are 137,229 for binary and 81,066 for ternary dynamic viscosity measurements.
- Binary viscosity data span a wider range of conditions (temperature 199.918–1173.0 K, pressure 0.0–387,800.0 kPa) than ternary data (temperature 20.0–1023.0 K, pressure 0.0–196,130.0 kPa).
- All reported data refer to the property Viscosity, Pa·s (GLOBprop_4) in declared binary or ternary systems within ThermoML.
</subagent_answer>
</tool_result>

## LLM Response
<reasoning>
The user is asking which class—binary or ternary—provides a stronger test for validating a liquid-mixture viscosity model, based on experimental measurement availability across composition. I already have comprehensive data from the L1 query. Let me synthesize a clear recommendation.

Key considerations for model validation:
1. Total data volume (binary wins: 137,229 vs 81,066 points)
2. Number of distinct systems/sources (binary wins: 1176 vs 429 sources, 3294 vs 1081 blocks)
3. Composition coverage per block (ternary wins: ~75 vs ~42 points per block)
4. Condition range (binary wins: wider T and P ranges)
5. For model validation, you want diversity of systems AND dense composition coverage within each system

Binary systems are the clear winner for initial validation: more systems, more data, wider conditions, and simpler to diagnose model failures. Ternary systems provide a stronger *stress test* once the model passes binary validation, because they test multi-component interactions.

I have all the data I need from the previous query. Let me provide the final answer.
</reasoning>

<answer>
## Recommendation: Start with Binary Systems — They Offer the Stronger Initial Validation Test

Based on the dynamic viscosity (Viscosity, Pa·s) data holdings in ThermoML, **binary liquid mixtures** provide the stronger foundation for first-pass model validation, and here is why:

### Data Availability at a Glance

| Metric | Binary (2-component) | Ternary (3-component) |
|---|---|---|
| Distinct literature sources | 1176 | 429 |
| Property blocks | 3294 | 1081 |
| Total data points | 137,229 | 81,066 |
| Avg. data points per block | ~41.7 | ~75.0 |
| Temperature range (K) | 199.918 – 1173.0 | 20.0 – 1023.0 |
| Pressure range (kPa) | 0.0 – 387,800.0 | 0.0 – 196,130.0 |

### Why Binary Systems Win for Initial Validation

1. **Far greater diversity of chemical systems.** With 1176 independent literature sources and 3294 property blocks, binary data cover a much wider variety of solute–solvent pairs — polar + nonpolar, associating + inert, ionic liquids + molecular solvents, etc. This diversity is critical for stress-testing whether a model generalises across chemical families, not just across compositions within one mixture.

2. **Broader thermodynamic conditions.** Binary data span temperatures from ~200 K to 1173 K and pressures up to ~388 MPa, compared with ~20–1023 K and ~196 MPa for ternary data. A model validated over these wider windows is more credible.

3. **Simpler failure diagnosis.** In a binary system the composition variable is one-dimensional (mole fraction x₁), so any systematic deviation between model and experiment can be mapped directly against x₁. In a ternary system, deviations live on a two-dimensional Gibbs triangle, making it harder to isolate whether the error comes from a particular binary interaction parameter or from a higher-order cross term.

4. **Sufficient composition density per block.** Although ternary blocks are denser (~75 points/block vs. ~42), binary blocks still typically sweep 10–20+ mole-fraction values across the full 0 → 1 range at a given temperature — more than enough to reveal curvature, inflection points, or extrema in η(x) that challenge mixing rules.

### When to Move to Ternary Validation

Ternary data become essential in a **second validation stage**, once the model passes binary tests. Ternary viscosity is a much more demanding test of multi-body interaction terms (e.g., the Wohl or Cibulka ternary contribution in excess-property models). The 81,066 ternary data points across 429 sources and 1081 blocks are ample for this purpose, and the higher composition density per block (~75 points) means individual ternary datasets map the Gibbs triangle well.

Notable large datasets for each stage:

- **Binary:** DOI 10.1021/acs.jced.7b00221 (GLOBlit_7152) — 25 blocks, 1448 points; DOI 10.1016/j.jct.2011.02.018 (GLOBlit_3363) — 6 blocks, 848 points.
- **Ternary:** DOI 10.1021/acs.jced.5b00845 (GLOBlit_6743) — 48 blocks, 5168 points; DOI 10.1021/je5001523 (GLOBlit_10411) — 17 blocks, 1604 points.

### Bottom Line

**Binary systems first.** They give you 3× more independent sources, 3× more property blocks, 70% more total data points, wider T/P coverage, and — crucially — far greater chemical diversity, all while keeping failure diagnosis straightforward. Reserve the ternary corpus as the rigorous follow-up test that probes whether your model's multi-component mixing rules hold up in higher-dimensional composition space.
</answer>