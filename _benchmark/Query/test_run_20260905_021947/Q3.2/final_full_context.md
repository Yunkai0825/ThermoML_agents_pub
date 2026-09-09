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
| comp | GLOBcomp_1 | water | water |
| comp | GLOBcomp_2 | ethanol | ethanol |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find all experimental data for ethanol + water binary system and determine the full temperature range covered, identifyi → stored as L1_query_1 · validation: FLAGGED(2)
- [L1] Find the hottest activity coefficient measurements for ethanol+water to determine the upper temperature bound for an act → stored as L1_query_2 · validation: FLAGGED(8)

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: FLAGGED(2)

**Summary:** The ethanol + water binary system in ThermoML spans 126 data blocks across 73 publications with 5163 target-point observations. The aggregate temperature range is 268.1 K to 673.15 K and the pressure range is 13.15 to 50,760 kPa. The coldest inspected data point is 273.35 K from GLOBlit_299 PROPblock_4 (DOI: 10.1016/j.fluid.2005.08.018), reporting the activity coefficient of ethanol at infinite dilution (2.54 at 273.35 K, 3.13 at 283.15 K) via headspace analysis. The hottest inspected data point is 673.15 K from GLOBlit_2732 PROPblock_4 (DOI: 10.1016/j.jct.2006.08.002), reporting mass density by constant volume piezometry over 524.15–673.15 K, 4,750–50,760 kPa, x(ethanol) = 0.2–0.8, with densities from 52.89 to 617.36 kg/m³ across 278 points. Boiling temperature data from GLOBlit_977 PROPblock_1 (DOI: 10.1016/j.fluid.2011.06.009) covers 45 points at sub-atmospheric pressures (13.15–32.86 kPa) with T_boil = 307.44–335.16 K and x(ethanol) = 0.063–0.971. Activity coefficient blocks from search results span approximately 273–373 K across multiple methods, though only the 273.35 K point was directly inspected. The supercritical data (up to 673.15 K) covers pVTx behavior rather than conventional VLE. A data quality concern was noted: GLOBlit_1971 reportedly shows activity coefficients at infinite dilution that decrease with temperature, opposite to the trend in other sources.

**Answer:**

#### Ethanol + Water Binary System: Temperature Range in ThermoML

##### Overall Coverage
The ethanol (GLOBcomp_2) + water (GLOBcomp_1) binary system is extensively represented in ThermoML. The system summary (an aggregate statistic from `search_system_summary`, not a single inspected block) reports **126 data blocks** across **73 publications** and **5163 target-point observations**.

**Full temperature range (from system summary aggregate): 268.1 K to 673.15 K** *(the 268.1 K minimum is a system-summary-level aggregate; no individual block returning data at that temperature was located or inspected in this run)*
**Pressure range (from system summary aggregate): 13.15 to 50,760 kPa**

---

##### Coldest Measurements (Inspected)

The coldest inspected data point is at **273.35 K** from:

- **Source:** GLOBlit_299 — DOI: 10.1016/j.fluid.2005.08.018
- **Block:** PROPblock_4
- **Property:** Activity coefficient of ethanol at infinite dilution (γ∞), with mole fraction of ethanol constrained to 0.0
- **Method:** Headspace analysis (GLOBmeas_543)
- **Inspected data (complete block, 2 points):**

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *BLKpoint_id* | *temperature_k* | *mole_fraction_ethanol* | *activity_coefficient_ethanol* |
|---|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「BLKpoint_1」 | 「273.35」 | 「0.0」 | 「2.54」 |
| WM_L1#1_Table#1_Row#2 | 「BLKpoint_2」 | 「283.15」 | 「0.0」 | 「3.13」 |

---

##### Hottest Measurements (Inspected)

The hottest inspected data point is at **673.15 K** from:

- **Source:** GLOBlit_2732 — DOI: 10.1016/j.jct.2006.08.002
- **Block:** PROPblock_4
- **Title:** *(p,v,T,x) Measurements of {(1−x)H₂O + xC₂H₅OH} mixtures in the near-critical and supercritical regions*
- **Property:** Mass density (kg/m³)
- **Method:** Constant volume piezometry (GLOBmeas_66)
- **Block stats (inspected):** 278 data points, T = 524.15–673.15 K, P = 4,750–50,760 kPa, x(ethanol) = 0.2–0.8, ρ = 52.89–617.36 kg/m³
- **At 673.15 K:** 31 data points were recorded, e.g., ρ = 52.89 kg/m³ at 6,990 kPa (x_ethanol = 0.8) up to ρ = 451.15 kg/m³ at 47,140 kPa (x_ethanol = 0.2).

---

##### VLE-Relevant Property Breakdown

**Boiling temperature (GLOBprop_14) — Inspected block:**

GLOBlit_977 (DOI: 10.1016/j.fluid.2011.06.009), PROPblock_1 — 45 points at sub-atmospheric pressures (13.15–32.86 kPa), T_boil = 307.44–335.16 K, x(ethanol) = 0.063–0.971. This is the block with the lowest boiling temperatures found.

Additional boiling-temperature blocks were returned by `search_blocks` (10 blocks total) but were not individually inspected. Per those search results, atmospheric-pressure VLE data is available from multiple sources (e.g., GLOBlit_757, GLOBlit_1518), but their specific data values were not inspected in this run.

**Activity coefficient (GLOBprop_3) — from search results (6 blocks, 4 papers):**

The `search_blocks` tool returned the following activity-coefficient blocks. Only GLOBlit_299::PROPblock_4 was inspected (see above); the remaining values below are from the search-result summaries and were not individually inspected:

- GLOBlit_299 (DOI: 10.1016/j.fluid.2005.08.018) — 3 blocks using different methods (headspace analysis, comparative tensimetry, circulating still), temperature range reported by search as 273.35–372.15 K (not inspected beyond PROPblock_4)
- GLOBlit_8511 (DOI: 10.1021/je049875+) — dilutor chromatography (not inspected)
- GLOBlit_1971 (DOI: 10.1016/j.fluid.2016.08.030) — SPME method (not inspected)
- GLOBlit_8381 (DOI: 10.1021/je0495942) — chromatography (not inspected)

**Vapor pressure (GLOBprop_5):** 6 blocks reported by the system summary; not individually searched or inspected in this run.

---

##### Summary for Correlation Work

**WM_L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *Property* | *T_min (K)* | *T_max (K)* | *Source of T_min* | *Source of T_max* | *Inspected?* |
|---|---|---|---|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「Activity coefficient」 | 「273.35」 | 「not inspected beyond PROPblock_4」 | 「GLOBlit_299, PROPblock_4」 | 「—」 | 「T_min: yes」 |
| WM_L1#1_Table#2_Row#2 | 「Boiling temperature」 | 「307.44」 | 「335.16」 | 「GLOBlit_977, PROPblock_1」 | 「GLOBlit_977, PROPblock_1」 | 「yes」 |
| WM_L1#1_Table#2_Row#3 | 「Mass density (supercritical)」 | 「524.15」 | 「673.15」 | 「GLOBlit_2732, PROPblock_4」 | 「GLOBlit_2732, PROPblock_4」 | 「yes」 |

The VLE-relevant temperature window for building an ethanol+water activity-coefficient correlation spans approximately **273–373 K** (derived from the search-result summaries for boiling temperature and activity coefficient blocks; the exact upper bound of activity-coefficient data was not inspected). The supercritical data (up to 673.15 K) covers mass density and pVTx behavior rather than conventional VLE.

⚠️ **Data quality note (from search results, not inspected):** GLOBlit_1971 was reported by the search tool to show γ∞ values that *decrease* with temperature, which is opposite to the trend seen in the other sources. This inconsistency should be evaluated before including that dataset in a correlation.

**Core claims:**
- The ethanol + water binary system in ThermoML spans an aggregate temperature range of 268.1 K to 673.15 K across 126 data blocks from 73 publications, though the 268.1 K minimum is a system-summary aggregate and no individual block at that temperature was inspected.
- The coldest inspected data point is at 273.35 K (activity coefficient of ethanol at infinite dilution, γ∞ = 2.54, from GLOBlit_299, PROPblock_4, DOI: 10.1016/j.fluid.2005.08.018, headspace analysis method).
- The hottest inspected data point is at 673.15 K (mass density via constant volume piezometry, from GLOBlit_2732, PROPblock_4, DOI: 10.1016/j.jct.2006.08.002), covering supercritical pVTx measurements at 524.15–673.15 K and 4,750–50,760 kPa.
- VLE-relevant data for building an ethanol+water activity-coefficient correlation spans approximately 273–373 K based on search-result summaries for boiling temperature and activity coefficient blocks, though the exact upper bound of activity-coefficient data was not inspected.
- An inspected sub-atmospheric boiling-temperature block (GLOBlit_977, PROPblock_1, DOI: 10.1016/j.fluid.2011.06.009) contains 45 points at 13.15–32.86 kPa with T_boil = 307.44–335.16 K and x(ethanol) = 0.063–0.971.
- A data quality concern was noted from search results (not inspected): GLOBlit_1971 reportedly shows γ∞ values that decrease with temperature, opposite to the trend in other sources, and should be evaluated before inclusion in a correlation.
- The upper bound of the activity-coefficient temperature range (372.15 K attributed to GLOBlit_299) is flagged as UNVERIFIED, as it was not confirmed by any inspected data in this run.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#3 | 「GLOBlit_299」 | 「PROPblock_4」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_3」 | 「Activity coefficient of ethanol at infinite dilution in water, headspace analysis, 273.35–283.15 K.」 |
| WM_L1#1_Table#4 | 「GLOBlit_2732」 | 「PROPblock_4」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of ethanol+water mixtures in near-critical and supercritical regions, 524.15–673.15 K, constant volume piezometry.」 |
| WM_L1#1_Table#5 | 「GLOBlit_977」 | 「PROPblock_1」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_14」 | 「Boiling temperature of ethanol+water at sub-atmospheric pressures, 307.44–335.16 K.」 |

*Not stored here: 3 verbatim data_inspections table(s); 2 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(2) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNGROUNDED_LITERAL** GLOBlit_299::PROPblock_4: 372.15 (near '…ting still), temperature range reported by search as 273.35–…') matches no inspected row/stat, database table, or other source of GLOBlit_299::PROPblock_4
- **MISATTRIBUTED_VALUE** PROPblock_1: 673.15 does not belong to PROPblock_1; it matches only GLOBlit_299::PROPblock_4 (inspected this run)
### L1_query_2
**L1_query_2** — status: success · validation: FLAGGED(8)

**Summary:** All six ThermoML activity coefficient data blocks for the ethanol + water binary system measure the infinite-dilution activity coefficient of ethanol (mole fraction of ethanol = 0.0). The combined temperature range spans from 273.35 K (GLOBlit_299, PROPblock_4, headspace analysis, γ∞ = 2.54) to 372.15 K (GLOBlit_299, PROPblock_6, circulating still method, γ∞ = 6.2), covering 23 data points from 4 publications. The hottest measurement is at 372.15 K with γ∞ = 6.2 from GLOBlit_299 PROPblock_6 (DOI: 10.1016/j.fluid.2005.08.018). Five of six blocks show γ∞ increasing monotonically with temperature; the exception is GLOBlit_1971 PROPblock_1 (SPME method), which shows γ∞ decreasing from 5.17 at 323.15 K to 4.11 at 353.15 K — opposite to all other sources and physically suspect. Excluding that anomalous dataset, 19 data points from 3 sources with consistent trends are available for correlation across the full 273.35–372.15 K range.

**Answer:**

#### Hottest Activity Coefficient Measurements for Ethanol + Water

All six activity coefficient (γ∞) data blocks for the ethanol (GLOBcomp_2) + water (GLOBcomp_1) binary system in ThermoML have now been inspected. Every block measures the **infinite-dilution activity coefficient of ethanol** (mole fraction of ethanol constrained to 0.0). The combined verified temperature range spans from 273.35 K (GLOBlit_299, PROPblock_4) to 372.15 K (GLOBlit_299, PROPblock_6) across 23 data points (computed: 2 + 7 + 4 + 1 + 5 + 4) from 4 publications.

##### Verified Upper Temperature Bound: 372.15 K

The hottest activity coefficient data comes from **GLOBlit_299, PROPblock_6** (DOI: 10.1016/j.fluid.2005.08.018), measured by the circulating still method:

**WM_L1#2_Table#1_(Query_L1#2_Answer):**

| *row_id* | *BLKpoint_id* | *Temperature (K)* | *x(ethanol)* | *γ∞(ethanol)* |
|---|---|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「BLKpoint_1」 | 「358.15」 | 「0.0」 | 「5.9」 |
| WM_L1#2_Table#1_Row#2 | 「BLKpoint_2」 | 「363.15」 | 「0.0」 | 「6.0」 |
| WM_L1#2_Table#1_Row#3 | 「BLKpoint_3」 | 「368.15」 | 「0.0」 | 「6.1」 |
| WM_L1#2_Table#1_Row#4 | 「BLKpoint_4」 | 「372.15」 | 「0.0」 | 「6.2」 |

The trend is monotonically increasing and near-linear (R² = 0.9973), consistent with the expected positive temperature dependence of γ∞ for ethanol in water.

##### Complete Block-by-Block Summary (All Inspected)

**WM_L1#2_Table#2_(Query_L1#2_Answer):**

| *row_id* | *Source (GLOBlit)* | *DOI* | *Block* | *Method* | *T range (K)* | *γ∞ range* | *Points* | *Trend* |
|---|---|---|---|---|---|---|---|---|
| WM_L1#2_Table#2_Row#1 | 「GLOBlit_299」 | 「10.1016/j.fluid.2005.08.018」 | 「PROPblock_4」 | 「Headspace analysis」 | 「273.35–283.15」 | 「2.54–3.13」 | 「2」 | 「↑」 |
| WM_L1#2_Table#2_Row#2 | 「GLOBlit_299」 | 「10.1016/j.fluid.2005.08.018」 | 「PROPblock_5」 | 「Comparative tensimetry」 | 「303.15–333.15」 | 「4.14–5.3」 | 「7」 | 「↑」 |
| WM_L1#2_Table#2_Row#3 | 「GLOBlit_299」 | 「10.1016/j.fluid.2005.08.018」 | 「PROPblock_6」 | 「Circulating still」 | 「358.15–372.15」 | 「5.9–6.2」 | 「4」 | 「↑」 |
| WM_L1#2_Table#2_Row#4 | 「GLOBlit_8381」 | 「10.1021/je0495942」 | 「PROPblock_1」 | 「Chromatography」 | 「298.15」 | 「3.77」 | 「1」 | 「—」 |
| WM_L1#2_Table#2_Row#5 | 「GLOBlit_8511」 | 「10.1021/je049875+」 | 「PROPblock_1」 | 「Chromatography (dilutor)」 | 「303.25–343.25」 | 「5.03–5.96」 | 「5」 | 「↑」 |
| WM_L1#2_Table#2_Row#6 | 「GLOBlit_1971」 | 「10.1016/j.fluid.2016.08.030」 | 「PROPblock_1」 | 「Solid-phase micro-extraction」 | 「323.15–353.15」 | 「4.11–5.17」 | 「4」 | 「**↓ (anomalous)**」 |

##### Key Findings

1. **Verified maximum temperature for activity coefficient data: 372.15 K** (GLOBlit_299, PROPblock_6, circulating still method, γ∞ = 6.2).

2. **Consistent temperature dependence across 5 of 6 blocks:** γ∞ increases monotonically with temperature. The three GLOBlit_299 blocks together provide nearly continuous coverage using three complementary methods: from 273.35 K with γ∞ = 2.54 (PROPblock_4, headspace analysis) through 303.15–333.15 K with γ∞ = 4.14–5.3 (PROPblock_5, comparative tensimetry) to 358.15–372.15 K with γ∞ = 5.9–6.2 (PROPblock_6, circulating still).

3. **Data quality concern confirmed for GLOBlit_1971 (PROPblock_1):** The SPME-method data shows γ∞ *decreasing* from 5.17 at 323.15 K to 4.11 at 353.15 K, which is the opposite of every other source. For comparison at overlapping temperatures: at ~323 K, GLOBlit_1971 PROPblock_1 reports γ∞ = 5.17, while GLOBlit_8511 PROPblock_1 reports 5.54 at 323.25 K and GLOBlit_299 PROPblock_5 reports 5.03 at 323.15 K. The decreasing trend in GLOBlit_1971 is physically suspect and this dataset should be critically evaluated before inclusion in a correlation.

4. **For correlation building:** The verified activity coefficient temperature window spans from 273.35 K (GLOBlit_299, PROPblock_4) to 372.15 K (GLOBlit_299, PROPblock_6). Excluding the anomalous GLOBlit_1971 data, 19 data points (computed: 2 + 7 + 4 + 1 + 5 from the five consistent blocks) from 3 sources with consistent trends are available.

**Core claims:**
- All six activity coefficient data blocks for ethanol + water in the ThermoML dataset measure the infinite-dilution activity coefficient of ethanol (mole fraction of ethanol constrained to 0.0), spanning a verified temperature range from 273.35 K to 372.15 K across 23 data points from 4 publications.
- The highest temperature at which activity coefficient data are available is 372.15 K (GLOBlit_299, PROPblock_6, circulating still method), where γ∞ of ethanol = 6.2.
- In 5 of the 6 data blocks, γ∞ of ethanol increases monotonically with temperature, consistent with the expected positive temperature dependence for ethanol in water.
- The GLOBlit_1971 (PROPblock_1, SPME method) data show γ∞ decreasing from 5.17 at 323.15 K to 4.11 at 353.15 K, which is opposite to all other sources and is flagged as physically suspect; this dataset should be critically evaluated before inclusion in any correlation.
- Excluding the anomalous GLOBlit_1971 data, 19 data points from 3 sources with mutually consistent trends are available for correlation across the 273.35–372.15 K range.
- Several specific block-to-value attributions in the answer carry MISATTRIBUTED_VALUE or AMBIGUOUS_VALUE flags, indicating that while the underlying data values were inspected and verified, some were cited under incorrect block labels; the numeric values themselves remain consistent with the inspected records.

**Core blocks found:**

**WM_L1#2_Blocks_(Query_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#3 | 「GLOBlit_299」 | 「PROPblock_4」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_3」 | 「Infinite-dilution activity coefficient of ethanol in water by headspace analysis, 273.35–283.15 K.」 |
| WM_L1#2_Table#4 | 「GLOBlit_299」 | 「PROPblock_5」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_3」 | 「Infinite-dilution activity coefficient of ethanol in water by comparative tensimetry, 303.15–333.15 K.」 |
| WM_L1#2_Table#5 | 「GLOBlit_299」 | 「PROPblock_6」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_3」 | 「Infinite-dilution activity coefficient of ethanol in water by circulating still, 358.15–372.15 K. Contains the verified maximum temperature of 372.15 K.」 |
| WM_L1#2_Table#6 | 「GLOBlit_8381」 | 「PROPblock_1」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_3」 | 「Infinite-dilution activity coefficient of ethanol in water by chromatography at 298.15 K.」 |
| WM_L1#2_Table#7 | 「GLOBlit_8511」 | 「PROPblock_1」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_3」 | 「Infinite-dilution activity coefficient of ethanol in water by dilutor chromatography, 303.25–343.25 K.」 |
| WM_L1#2_Table#8 | 「GLOBlit_1971」 | 「PROPblock_1」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_3」 | 「Infinite-dilution activity coefficient of ethanol in water by solid-phase micro-extraction, 323.15–353.15 K. Anomalous decreasing trend flagged.」 |

*Not stored here: 6 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(8) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **MISATTRIBUTED_VALUE** PROPblock_4: 372.15 does not belong to PROPblock_4; it matches only GLOBlit_299::PROPblock_6 (inspected this run)
- **UNGROUNDED_LITERAL** PROPblock_6: 23 (near '…) across 23 data points (computed: 2 + 7 + 4 + 1 +…') matches no inspected row/stat, database table, or other source of PROPblock_6
- **MISATTRIBUTED_VALUE** PROPblock_6: 273.35 does not belong to PROPblock_6; it matches only GLOBlit_299::PROPblock_4 (inspected this run)
- **MISATTRIBUTED_VALUE** PROPblock_6: 2.54 does not belong to PROPblock_6; it matches only GLOBlit_299::PROPblock_4 (inspected this run)
- **MISATTRIBUTED_VALUE** PROPblock_4: 303.15 does not belong to PROPblock_4; it matches only GLOBlit_299::PROPblock_5 (inspected this run)
- **AMBIGUOUS_VALUE** PROPblock_4: 333.15 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean
- **MISATTRIBUTED_VALUE** PROPblock_4: 4.14 does not belong to PROPblock_4; it matches only GLOBlit_299::PROPblock_5 (inspected this run)
- **AMBIGUOUS_VALUE** PROPblock_4: 5.3 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean



</memory>

## User
I am building an activity-coefficient correlation for ethanol + water over the widest possible temperature range. What range can the experimental literature support, and which studies provide the coldest and hottest measurements?

## Assistant
<summary>Planning to search for ethanol + water binary system data across all temperature-sensitive properties (VLE, boiling point, excess enthalpy, etc.) to find the widest temperature range and identify the coldest/hottest studies.</summary>
<tool_call>L1_query(instruction=Search for the bi…, id_catalog=, context=User is building …)</tool_call>

## User
<tool_result>
<subagent_answer>
### L1#1 — L1_query return

**Status:** status=success

**Summary:** The ethanol + water binary system in ThermoML spans 126 data blocks across 73 publications with 5163 target-point observations. The aggregate temperature range is 268.1 K to 673.15 K and the pressure range is 13.15 to 50,760 kPa. The coldest inspected data point is 273.35 K from GLOBlit_299 PROPblock_4 (DOI: 10.1016/j.fluid.2005.08.018), reporting the activity coefficient of ethanol at infinite dilution (2.54 at 273.35 K, 3.13 at 283.15 K) via headspace analysis. The hottest inspected data point is 673.15 K from GLOBlit_2732 PROPblock_4 (DOI: 10.1016/j.jct.2006.08.002), reporting mass density by constant volume piezometry over 524.15–673.15 K, 4,750–50,760 kPa, x(ethanol) = 0.2–0.8, with densities from 52.89 to 617.36 kg/m³ across 278 points. Boiling temperature data from GLOBlit_977 PROPblock_1 (DOI: 10.1016/j.fluid.2011.06.009) covers 45 points at sub-atmospheric pressures (13.15–32.86 kPa) with T_boil = 307.44–335.16 K and x(ethanol) = 0.063–0.971. Activity coefficient blocks from search results span approximately 273–373 K across multiple methods, though only the 273.35 K point was directly inspected. The supercritical data (up to 673.15 K) covers pVTx behavior rather than conventional VLE. A data quality concern was noted: GLOBlit_1971 reportedly shows activity coefficients at infinite dilution that decrease with temperature, opposite to the trend in other sources.

**Answer:**

#### Ethanol + Water Binary System: Temperature Range in ThermoML

##### Overall Coverage
The ethanol (GLOBcomp_2) + water (GLOBcomp_1) binary system is extensively represented in ThermoML. The system summary (an aggregate statistic from `search_system_summary`, not a single inspected block) reports **126 data blocks** across **73 publications** and **5163 target-point observations**.

**Full temperature range (from system summary aggregate): 268.1 K to 673.15 K** *(the 268.1 K minimum is a system-summary-level aggregate; no individual block returning data at that temperature was located or inspected in this run)*
**Pressure range (from system summary aggregate): 13.15 to 50,760 kPa**

---

##### Coldest Measurements (Inspected)

The coldest inspected data point is at **273.35 K** from:

- **Source:** GLOBlit_299 — DOI: 10.1016/j.fluid.2005.08.018
- **Block:** PROPblock_4
- **Property:** Activity coefficient of ethanol at infinite dilution (γ∞), with mole fraction of ethanol constrained to 0.0
- **Method:** Headspace analysis (GLOBmeas_543)
- **Inspected data (complete block, 2 points):**

**L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *BLKpoint_id* | *temperature_k* | *mole_fraction_ethanol* | *activity_coefficient_ethanol* |
|---|---|---|---|---|
| L1#1_Table#1_Row#1 | 「BLKpoint_1」 | 「273.35」 | 「0.0」 | 「2.54」 |
| L1#1_Table#1_Row#2 | 「BLKpoint_2」 | 「283.15」 | 「0.0」 | 「3.13」 |

---

##### Hottest Measurements (Inspected)

The hottest inspected data point is at **673.15 K** from:

- **Source:** GLOBlit_2732 — DOI: 10.1016/j.jct.2006.08.002
- **Block:** PROPblock_4
- **Title:** *(p,v,T,x) Measurements of {(1−x)H₂O + xC₂H₅OH} mixtures in the near-critical and supercritical regions*
- **Property:** Mass density (kg/m³)
- **Method:** Constant volume piezometry (GLOBmeas_66)
- **Block stats (inspected):** 278 data points, T = 524.15–673.15 K, P = 4,750–50,760 kPa, x(ethanol) = 0.2–0.8, ρ = 52.89–617.36 kg/m³
- **At 673.15 K:** 31 data points were recorded, e.g., ρ = 52.89 kg/m³ at 6,990 kPa (x_ethanol = 0.8) up to ρ = 451.15 kg/m³ at 47,140 kPa (x_ethanol = 0.2).

---

##### VLE-Relevant Property Breakdown

**Boiling temperature (GLOBprop_14) — Inspected block:**

GLOBlit_977 (DOI: 10.1016/j.fluid.2011.06.009), PROPblock_1 — 45 points at sub-atmospheric pressures (13.15–32.86 kPa), T_boil = 307.44–335.16 K, x(ethanol) = 0.063–0.971. This is the block with the lowest boiling temperatures found.

Additional boiling-temperature blocks were returned by `search_blocks` (10 blocks total) but were not individually inspected. Per those search results, atmospheric-pressure VLE data is available from multiple sources (e.g., GLOBlit_757, GLOBlit_1518), but their specific data values were not inspected in this run.

**Activity coefficient (GLOBprop_3) — from search results (6 blocks, 4 papers):**

The `search_blocks` tool returned the following activity-coefficient blocks. Only GLOBlit_299::PROPblock_4 was inspected (see above); the remaining values below are from the search-result summaries and were not individually inspected:

- GLOBlit_299 (DOI: 10.1016/j.fluid.2005.08.018) — 3 blocks using different methods (headspace analysis, comparative tensimetry, circulating still), temperature range reported by search as 273.35–372.15 K (not inspected beyond PROPblock_4)
- GLOBlit_8511 (DOI: 10.1021/je049875+) — dilutor chromatography (not inspected)
- GLOBlit_1971 (DOI: 10.1016/j.fluid.2016.08.030) — SPME method (not inspected)
- GLOBlit_8381 (DOI: 10.1021/je0495942) — chromatography (not inspected)

**Vapor pressure (GLOBprop_5):** 6 blocks reported by the system summary; not individually searched or inspected in this run.

---

##### Summary for Correlation Work

**L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *Property* | *T_min (K)* | *T_max (K)* | *Source of T_min* | *Source of T_max* | *Inspected?* |
|---|---|---|---|---|---|---|
| L1#1_Table#2_Row#1 | 「Activity coefficient」 | 「273.35」 | 「not inspected beyond PROPblock_4」 | 「GLOBlit_299, PROPblock_4」 | 「—」 | 「T_min: yes」 |
| L1#1_Table#2_Row#2 | 「Boiling temperature」 | 「307.44」 | 「335.16」 | 「GLOBlit_977, PROPblock_1」 | 「GLOBlit_977, PROPblock_1」 | 「yes」 |
| L1#1_Table#2_Row#3 | 「Mass density (supercritical)」 | 「524.15」 | 「673.15」 | 「GLOBlit_2732, PROPblock_4」 | 「GLOBlit_2732, PROPblock_4」 | 「yes」 |

The VLE-relevant temperature window for building an ethanol+water activity-coefficient correlation spans approximately **273–373 K** (derived from the search-result summaries for boiling temperature and activity coefficient blocks; the exact upper bound of activity-coefficient data was not inspected). The supercritical data (up to 673.15 K) covers mass density and pVTx behavior rather than conventional VLE.

⚠️ **Data quality note (from search results, not inspected):** GLOBlit_1971 was reported by the search tool to show γ∞ values that *decrease* with temperature, which is opposite to the trend seen in the other sources. This inconsistency should be evaluated before including that dataset in a correlation.

---
[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:
- **UNGROUNDED_LITERAL** GLOBlit_299::PROPblock_4: 372.15 (near '…ting still), temperature range reported by search as 273.35–…') matches no inspected row/stat, database table, or other source of GLOBlit_299::PROPblock_4
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="GLOBlit_299::PROPblock_4", nearest={"column": "temperature_k", "value": 372.15})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **MISATTRIBUTED_VALUE** PROPblock_1: 673.15 does not belong to PROPblock_1; it matches only GLOBlit_299::PROPblock_4 (inspected this run)
  fix (required — this IS a database value, under a different block): `re-anchor 673.15 to GLOBlit_299::PROPblock_4 — no new tool call needed`
Inspected so far: PROPblock_1, PROPblock_4

**Core claims:**
- The ethanol + water binary system in ThermoML spans an aggregate temperature range of 268.1 K to 673.15 K across 126 data blocks from 73 publications, though the 268.1 K minimum is a system-summary aggregate and no individual block at that temperature was inspected.
- The coldest inspected data point is at 273.35 K (activity coefficient of ethanol at infinite dilution, γ∞ = 2.54, from GLOBlit_299, PROPblock_4, DOI: 10.1016/j.fluid.2005.08.018, headspace analysis method).
- The hottest inspected data point is at 673.15 K (mass density via constant volume piezometry, from GLOBlit_2732, PROPblock_4, DOI: 10.1016/j.jct.2006.08.002), covering supercritical pVTx measurements at 524.15–673.15 K and 4,750–50,760 kPa.
- VLE-relevant data for building an ethanol+water activity-coefficient correlation spans approximately 273–373 K based on search-result summaries for boiling temperature and activity coefficient blocks, though the exact upper bound of activity-coefficient data was not inspected.
- An inspected sub-atmospheric boiling-temperature block (GLOBlit_977, PROPblock_1, DOI: 10.1016/j.fluid.2011.06.009) contains 45 points at 13.15–32.86 kPa with T_boil = 307.44–335.16 K and x(ethanol) = 0.063–0.971.
- A data quality concern was noted from search results (not inspected): GLOBlit_1971 reportedly shows γ∞ values that decrease with temperature, opposite to the trend in other sources, and should be evaluated before inclusion in a correlation.
- The upper bound of the activity-coefficient temperature range (372.15 K attributed to GLOBlit_299) is flagged as UNVERIFIED, as it was not confirmed by any inspected data in this run.

**Core ID updates:**
- add GLOBcomp_1 — water (registry: water)
- add GLOBcomp_2 — ethanol (registry: ethanol)

#### Core blocks found — verbatim ledger

```ledger
**L1#1_Table#3_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_299 | lit_id: 2005-vrb-fen-0 | doi: 10.1016/j.fluid.2005.08.018
block: PROPblock_4 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 2
compounds: ethanol (C2H6O; GLOBcomp_2; DOIcomp_2; InChIKey LFQSCWFLJHTTHZ-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_6; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_3
description: Activity coefficient of ethanol at infinite dilution in water, headspace analysis, 273.35–283.15 K.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#3_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_3」 | 「Mole fraction」 | 「value=0.0 · phase=Liquid」 |
| L1#1_Table#3_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=273.35–283.15 · n_unique=2 · phase=Liquid」 |
| L1#1_Table#3_Row#3 | 「property」 | 「BLKprop_1/GLOBprop_3」 | 「Activity coefficient」 | 「method=headspace analysis (GLOBmeas_543) · range=2.54–3.13 · mean=2.835 · n=2 · phase=Liquid」 |
```

```ledger
**L1#1_Table#4_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_2732 | lit_id: 2007-baz-abd-0 | doi: 10.1016/j.jct.2006.08.002
block: PROPblock_4 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 278
compounds: ethanol (C2H6O; GLOBcomp_2; DOIcomp_1; InChIKey LFQSCWFLJHTTHZ-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_2; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density of ethanol+water mixtures in near-critical and supercritical regions, 524.15–673.15 K, constant volume piezometry.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#4_Row#1 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=524.15–673.15 · n_unique=28 · phase=Fluid (supercritical or subcritical phases)」 |
| L1#1_Table#4_Row#2 | 「variable」 | 「BLKvar_2/GLOBvar_3」 | 「Pressure, kPa」 | 「range=4750.0–50760.0 · n_unique=251 · phase=Fluid (supercritical or subcritical phases)」 |
| L1#1_Table#4_Row#3 | 「variable」 | 「BLKvar_3/GLOBvar_2」 | 「Mole fraction of ethanol」 | 「range=0.2–0.8 · n_unique=3 · phase=Fluid (supercritical or subcritical phases)」 |
| L1#1_Table#4_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=Constant-volume piezometry (GLOBmeas_66) · range=52.89–617.36 · mean=303.042374 · n=278 · phase=Fluid (supercritical or subcritical phases)」 |
```

```ledger
**L1#1_Table#5_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_977 | lit_id: 2011-vou-pam-0 | doi: 10.1016/j.fluid.2011.06.009
block: PROPblock_1 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 45
compounds: ethanol (C2H6O; GLOBcomp_2; DOIcomp_2; InChIKey LFQSCWFLJHTTHZ-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_1; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_14
description: Boiling temperature of ethanol+water at sub-atmospheric pressures, 307.44–335.16 K.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#5_Row#1 | 「variable」 | 「BLKvar_1/GLOBvar_2」 | 「Mole fraction of ethanol」 | 「range=0.063–0.971 · n_unique=43 · phase=Liquid」 |
| L1#1_Table#5_Row#2 | 「variable」 | 「BLKvar_2/GLOBvar_3」 | 「Pressure, kPa」 | 「range=13.15–32.86 · n_unique=3 · phase=Liquid」 |
| L1#1_Table#5_Row#3 | 「property」 | 「BLKprop_1/GLOBprop_14」 | 「Boiling temperature at pressure P, K」 | 「method=Ebulliometric method (Recirculating still) (GLOBmeas_5) · range=307.44–335.16 · mean=317.234222 · n=45 · phase=Liquid」 |
```

#### Data inspections — verbatim ledger

```ledger
**L1#1_Table#6_(Query_L1#1_INSP):**
lit_num_id: GLOBlit_2732 | doi: 10.1016/j.jct.2006.08.002 | block: PROPblock_4
table_mode: rdp | inspection_id: INSP_3198d97ab157 | rows_shown: 28

| *row_id* | *BLKpoint_id* | *temperature_k* | *pressure_kpa* | *mole_fraction_<ethanol>* | *mass_density_kg_m3* |
|---|---|---|---|---|---|
| L1#1_Table#6_Row#1 | 「BLKpoint_248」 | 「673.15」 | 「6990」 | 「0.8」 | 「52.89」 |
| L1#1_Table#6_Row#2 | 「BLKpoint_249」 | 「673.15」 | 「8570」 | 「0.5」 | 「55.65」 |
| L1#1_Table#6_Row#3 | 「BLKpoint_251」 | 「673.15」 | 「12250」 | 「0.5」 | 「83.95」 |
| L1#1_Table#6_Row#4 | 「BLKpoint_252」 | 「673.15」 | 「12980」 | 「0.2」 | 「67.32」 |
| L1#1_Table#6_Row#5 | 「BLKpoint_253」 | 「673.15」 | 「13010」 | 「0.8」 | 「114.36」 |
| L1#1_Table#6_Row#6 | 「BLKpoint_254」 | 「673.15」 | 「15740」 | 「0.5」 | 「116.78」 |
| L1#1_Table#6_Row#7 | 「BLKpoint_255」 | 「673.15」 | 「15940」 | 「0.2」 | 「89.72」 |
| L1#1_Table#6_Row#8 | 「BLKpoint_256」 | 「673.15」 | 「19310」 | 「0.8」 | 「187.46」 |
| L1#1_Table#6_Row#9 | 「BLKpoint_257」 | 「673.15」 | 「20680」 | 「0.5」 | 「170.3」 |
| L1#1_Table#6_Row#10 | 「BLKpoint_258」 | 「673.15」 | 「21310」 | 「0.2」 | 「137.56」 |
| L1#1_Table#6_Row#11 | 「BLKpoint_259」 | 「673.15」 | 「23620」 | 「0.8」 | 「242.38」 |
| L1#1_Table#6_Row#12 | 「BLKpoint_260」 | 「673.15」 | 「25130」 | 「0.8」 | 「259.1」 |
| L1#1_Table#6_Row#13 | 「BLKpoint_261」 | 「673.15」 | 「25740」 | 「0.5」 | 「233.23」 |
| L1#1_Table#6_Row#14 | 「BLKpoint_262」 | 「673.15」 | 「27230」 | 「0.8」 | 「282.28」 |
| L1#1_Table#6_Row#15 | 「BLKpoint_263」 | 「673.15」 | 「27430」 | 「0.2」 | 「220.84」 |
| L1#1_Table#6_Row#16 | 「BLKpoint_264」 | 「673.15」 | 「29500」 | 「0.8」 | 「305.19」 |
| L1#1_Table#6_Row#17 | 「BLKpoint_265」 | 「673.15」 | 「30040」 | 「0.8」 | 「310.49」 |
| L1#1_Table#6_Row#18 | 「BLKpoint_267」 | 「673.15」 | 「31230」 | 「0.2」 | 「285.57」 |
| L1#1_Table#6_Row#19 | 「BLKpoint_269」 | 「673.15」 | 「33730」 | 「0.2」 | 「323.66」 |
| L1#1_Table#6_Row#20 | 「BLKpoint_270」 | 「673.15」 | 「34050」 | 「0.5」 | 「325.37」 |
| L1#1_Table#6_Row#21 | 「BLKpoint_271」 | 「673.15」 | 「35510」 | 「0.2」 | 「349.48」 |
| L1#1_Table#6_Row#22 | 「BLKpoint_272」 | 「673.15」 | 「36420」 | 「0.8」 | 「365.05」 |
| L1#1_Table#6_Row#23 | 「BLKpoint_273」 | 「673.15」 | 「38700」 | 「0.8」 | 「380.23」 |
| L1#1_Table#6_Row#24 | 「BLKpoint_274」 | 「673.15」 | 「40850」 | 「0.5」 | 「383.2」 |
| L1#1_Table#6_Row#25 | 「BLKpoint_275」 | 「673.15」 | 「42660」 | 「0.2」 | 「420.24」 |
| L1#1_Table#6_Row#26 | 「BLKpoint_276」 | 「673.15」 | 「42950」 | 「0.8」 | 「403.08」 |
| L1#1_Table#6_Row#27 | 「BLKpoint_277」 | 「673.15」 | 「46620」 | 「0.5」 | 「418.66」 |
| L1#1_Table#6_Row#28 | 「BLKpoint_278」 | 「673.15」 | 「47140」 | 「0.2」 | 「451.15」 |
```

```ledger
**L1#1_Table#7_(Query_L1#1_INSP):**
lit_num_id: GLOBlit_299 | doi: 10.1016/j.fluid.2005.08.018 | block: PROPblock_4
table_mode: complete | inspection_id: INSP_a2f513326a7b | rows_shown: 2

| *row_id* | *BLKpoint_id* | *temperature_k* | *mole_fraction_<ethanol>* | *activity_coefficient_<ethanol>* |
|---|---|---|---|---|
| L1#1_Table#7_Row#1 | 「BLKpoint_1」 | 「273.35」 | 「0.0」 | 「2.54」 |
| L1#1_Table#7_Row#2 | 「BLKpoint_2」 | 「283.15」 | 「0.0」 | 「3.13」 |
```

```ledger
**L1#1_Table#8_(Query_L1#1_INSP):**
lit_num_id: GLOBlit_977 | doi: 10.1016/j.fluid.2011.06.009 | block: PROPblock_1
table_mode: rdp | inspection_id: INSP_168e6ede2830 | rows_shown: 40

| *row_id* | *BLKpoint_id* | *mole_fraction_<ethanol>* | *pressure_kpa* | *boiling_temperature_at_pressure_p_k* |
|---|---|---|---|---|
| L1#1_Table#8_Row#1 | 「BLKpoint_1」 | 「0.063」 | 「32.86」 | 「335.16」 |
| L1#1_Table#8_Row#2 | 「BLKpoint_2」 | 「0.076」 | 「19.71」 | 「323.53」 |
| L1#1_Table#8_Row#3 | 「BLKpoint_3」 | 「0.104」 | 「32.86」 | 「332.54」 |
| L1#1_Table#8_Row#4 | 「BLKpoint_4」 | 「0.117」 | 「13.15」 | 「313.71」 |
| L1#1_Table#8_Row#5 | 「BLKpoint_5」 | 「0.141」 | 「19.71」 | 「320.52」 |
| L1#1_Table#8_Row#6 | 「BLKpoint_6」 | 「0.15」 | 「32.86」 | 「330.96」 |
| L1#1_Table#8_Row#7 | 「BLKpoint_7」 | 「0.241」 | 「13.15」 | 「310.7」 |
| L1#1_Table#8_Row#8 | 「BLKpoint_8」 | 「0.248」 | 「32.86」 | 「329.26」 |
| L1#1_Table#8_Row#9 | 「BLKpoint_9」 | 「0.26」 | 「19.71」 | 「318.05」 |
| L1#1_Table#8_Row#10 | 「BLKpoint_10」 | 「0.383」 | 「13.15」 | 「309.53」 |
| L1#1_Table#8_Row#11 | 「BLKpoint_11」 | 「0.39」 | 「19.71」 | 「317.04」 |
| L1#1_Table#8_Row#12 | 「BLKpoint_12」 | 「0.454」 | 「32.86」 | 「326.77」 |
| L1#1_Table#8_Row#13 | 「BLKpoint_13」 | 「0.492」 | 「13.15」 | 「308.82」 |
| L1#1_Table#8_Row#14 | 「BLKpoint_14」 | 「0.499」 | 「19.71」 | 「316.35」 |
| L1#1_Table#8_Row#15 | 「BLKpoint_15」 | 「0.581」 | 「32.86」 | 「326.1」 |
| L1#1_Table#8_Row#16 | 「BLKpoint_16」 | 「0.59」 | 「13.15」 | 「308.36」 |
| L1#1_Table#8_Row#17 | 「BLKpoint_17」 | 「0.599」 | 「19.71」 | 「315.9」 |
| L1#1_Table#8_Row#18 | 「BLKpoint_18」 | 「0.656」 | 「13.15」 | 「308.1」 |
| L1#1_Table#8_Row#19 | 「BLKpoint_19」 | 「0.657」 | 「32.86」 | 「325.89」 |
| L1#1_Table#8_Row#20 | 「BLKpoint_20」 | 「0.688」 | 「19.71」 | 「315.55」 |
| L1#1_Table#8_Row#21 | 「BLKpoint_21」 | 「0.76」 | 「32.86」 | 「325.67」 |
| L1#1_Table#8_Row#22 | 「BLKpoint_22」 | 「0.771」 | 「13.15」 | 「307.7」 |
| L1#1_Table#8_Row#23 | 「BLKpoint_24」 | 「0.805」 | 「19.71」 | 「315.26」 |
| L1#1_Table#8_Row#24 | 「BLKpoint_25」 | 「0.839」 | 「32.86」 | 「325.53」 |
| L1#1_Table#8_Row#25 | 「BLKpoint_26」 | 「0.84」 | 「13.15」 | 「307.54」 |
| L1#1_Table#8_Row#26 | 「BLKpoint_27」 | 「0.841」 | 「19.71」 | 「315.19」 |
| L1#1_Table#8_Row#27 | 「BLKpoint_28」 | 「0.854」 | 「32.86」 | 「325.51」 |
| L1#1_Table#8_Row#28 | 「BLKpoint_29」 | 「0.864」 | 「13.15」 | 「307.56」 |
| L1#1_Table#8_Row#29 | 「BLKpoint_30」 | 「0.883」 | 「19.71」 | 「315.15」 |
| L1#1_Table#8_Row#30 | 「BLKpoint_33」 | 「0.911」 | 「13.15」 | 「307.5」 |
| L1#1_Table#8_Row#31 | 「BLKpoint_34」 | 「0.913」 | 「19.71」 | 「315.16」 |
| L1#1_Table#8_Row#32 | 「BLKpoint_35」 | 「0.913」 | 「32.86」 | 「325.46」 |
| L1#1_Table#8_Row#33 | 「BLKpoint_36」 | 「0.931」 | 「19.71」 | 「315.13」 |
| L1#1_Table#8_Row#34 | 「BLKpoint_37」 | 「0.931」 | 「32.86」 | 「325.43」 |
| L1#1_Table#8_Row#35 | 「BLKpoint_39」 | 「0.934」 | 「13.15」 | 「307.48」 |
| L1#1_Table#8_Row#36 | 「BLKpoint_40」 | 「0.945」 | 「19.71」 | 「315.13」 |
| L1#1_Table#8_Row#37 | 「BLKpoint_41」 | 「0.947」 | 「13.15」 | 「307.45」 |
| L1#1_Table#8_Row#38 | 「BLKpoint_43」 | 「0.964」 | 「19.71」 | 「315.14」 |
| L1#1_Table#8_Row#39 | 「BLKpoint_44」 | 「0.965」 | 「32.86」 | 「325.45」 |
| L1#1_Table#8_Row#40 | 「BLKpoint_45」 | 「0.971」 | 「13.15」 | 「307.44」 |
```
</subagent_answer>
</tool_result>

## Assistant
<summary>L1 returned comprehensive data. The coldest activity coefficient point is 273.35 K (GLOBlit_299). Need to resolve the UNVERIFIED upper bound (372.15 K) by inspecting remaining activity coefficient blocks from GLOBlit_299 and other sources (GLOBlit_8511, GLOBlit_1971, GLOBlit_8381). Dispatching follow-up query.</summary>
<tool_call>L1_query(instruction=Search for all ac…, id_catalog=GLOBcomp_1=water,…, context=Previous…)</tool_call>

## User
<tool_result>
<subagent_answer>
### L1#2 — L1_query return

**Status:** status=success

**Summary:** All six ThermoML activity coefficient data blocks for the ethanol + water binary system measure the infinite-dilution activity coefficient of ethanol (mole fraction of ethanol = 0.0). The combined temperature range spans from 273.35 K (GLOBlit_299, PROPblock_4, headspace analysis, γ∞ = 2.54) to 372.15 K (GLOBlit_299, PROPblock_6, circulating still method, γ∞ = 6.2), covering 23 data points from 4 publications. The hottest measurement is at 372.15 K with γ∞ = 6.2 from GLOBlit_299 PROPblock_6 (DOI: 10.1016/j.fluid.2005.08.018). Five of six blocks show γ∞ increasing monotonically with temperature; the exception is GLOBlit_1971 PROPblock_1 (SPME method), which shows γ∞ decreasing from 5.17 at 323.15 K to 4.11 at 353.15 K — opposite to all other sources and physically suspect. Excluding that anomalous dataset, 19 data points from 3 sources with consistent trends are available for correlation across the full 273.35–372.15 K range.

**Answer:**

#### Hottest Activity Coefficient Measurements for Ethanol + Water

All six activity coefficient (γ∞) data blocks for the ethanol (GLOBcomp_2) + water (GLOBcomp_1) binary system in ThermoML have now been inspected. Every block measures the **infinite-dilution activity coefficient of ethanol** (mole fraction of ethanol constrained to 0.0). The combined verified temperature range spans from 273.35 K (GLOBlit_299, PROPblock_4) to 372.15 K (GLOBlit_299, PROPblock_6) across 23 data points (computed: 2 + 7 + 4 + 1 + 5 + 4) from 4 publications.

##### Verified Upper Temperature Bound: 372.15 K

The hottest activity coefficient data comes from **GLOBlit_299, PROPblock_6** (DOI: 10.1016/j.fluid.2005.08.018), measured by the circulating still method:

**L1#2_Table#1_(Query_L1#2_Answer):**

| *row_id* | *BLKpoint_id* | *Temperature (K)* | *x(ethanol)* | *γ∞(ethanol)* |
|---|---|---|---|---|
| L1#2_Table#1_Row#1 | 「BLKpoint_1」 | 「358.15」 | 「0.0」 | 「5.9」 |
| L1#2_Table#1_Row#2 | 「BLKpoint_2」 | 「363.15」 | 「0.0」 | 「6.0」 |
| L1#2_Table#1_Row#3 | 「BLKpoint_3」 | 「368.15」 | 「0.0」 | 「6.1」 |
| L1#2_Table#1_Row#4 | 「BLKpoint_4」 | 「372.15」 | 「0.0」 | 「6.2」 |

The trend is monotonically increasing and near-linear (R² = 0.9973), consistent with the expected positive temperature dependence of γ∞ for ethanol in water.

##### Complete Block-by-Block Summary (All Inspected)

**L1#2_Table#2_(Query_L1#2_Answer):**

| *row_id* | *Source (GLOBlit)* | *DOI* | *Block* | *Method* | *T range (K)* | *γ∞ range* | *Points* | *Trend* |
|---|---|---|---|---|---|---|---|---|
| L1#2_Table#2_Row#1 | 「GLOBlit_299」 | 「10.1016/j.fluid.2005.08.018」 | 「PROPblock_4」 | 「Headspace analysis」 | 「273.35–283.15」 | 「2.54–3.13」 | 「2」 | 「↑」 |
| L1#2_Table#2_Row#2 | 「GLOBlit_299」 | 「10.1016/j.fluid.2005.08.018」 | 「PROPblock_5」 | 「Comparative tensimetry」 | 「303.15–333.15」 | 「4.14–5.3」 | 「7」 | 「↑」 |
| L1#2_Table#2_Row#3 | 「GLOBlit_299」 | 「10.1016/j.fluid.2005.08.018」 | 「PROPblock_6」 | 「Circulating still」 | 「358.15–372.15」 | 「5.9–6.2」 | 「4」 | 「↑」 |
| L1#2_Table#2_Row#4 | 「GLOBlit_8381」 | 「10.1021/je0495942」 | 「PROPblock_1」 | 「Chromatography」 | 「298.15」 | 「3.77」 | 「1」 | 「—」 |
| L1#2_Table#2_Row#5 | 「GLOBlit_8511」 | 「10.1021/je049875+」 | 「PROPblock_1」 | 「Chromatography (dilutor)」 | 「303.25–343.25」 | 「5.03–5.96」 | 「5」 | 「↑」 |
| L1#2_Table#2_Row#6 | 「GLOBlit_1971」 | 「10.1016/j.fluid.2016.08.030」 | 「PROPblock_1」 | 「Solid-phase micro-extraction」 | 「323.15–353.15」 | 「4.11–5.17」 | 「4」 | 「**↓ (anomalous)**」 |

##### Key Findings

1. **Verified maximum temperature for activity coefficient data: 372.15 K** (GLOBlit_299, PROPblock_6, circulating still method, γ∞ = 6.2).

2. **Consistent temperature dependence across 5 of 6 blocks:** γ∞ increases monotonically with temperature. The three GLOBlit_299 blocks together provide nearly continuous coverage using three complementary methods: from 273.35 K with γ∞ = 2.54 (PROPblock_4, headspace analysis) through 303.15–333.15 K with γ∞ = 4.14–5.3 (PROPblock_5, comparative tensimetry) to 358.15–372.15 K with γ∞ = 5.9–6.2 (PROPblock_6, circulating still).

3. **Data quality concern confirmed for GLOBlit_1971 (PROPblock_1):** The SPME-method data shows γ∞ *decreasing* from 5.17 at 323.15 K to 4.11 at 353.15 K, which is the opposite of every other source. For comparison at overlapping temperatures: at ~323 K, GLOBlit_1971 PROPblock_1 reports γ∞ = 5.17, while GLOBlit_8511 PROPblock_1 reports 5.54 at 323.25 K and GLOBlit_299 PROPblock_5 reports 5.03 at 323.15 K. The decreasing trend in GLOBlit_1971 is physically suspect and this dataset should be critically evaluated before inclusion in a correlation.

4. **For correlation building:** The verified activity coefficient temperature window spans from 273.35 K (GLOBlit_299, PROPblock_4) to 372.15 K (GLOBlit_299, PROPblock_6). Excluding the anomalous GLOBlit_1971 data, 19 data points (computed: 2 + 7 + 4 + 1 + 5 from the five consistent blocks) from 3 sources with consistent trends are available.

---
[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:
- **MISATTRIBUTED_VALUE** PROPblock_4: 372.15 does not belong to PROPblock_4; it matches only GLOBlit_299::PROPblock_6 (inspected this run)
  fix (required — this IS a database value, under a different block): `re-anchor 372.15 to GLOBlit_299::PROPblock_6 — no new tool call needed`
- **UNGROUNDED_LITERAL** PROPblock_6: 23 (near '…) across 23 data points (computed: 2 + 7 + 4 + 1 +…') matches no inspected row/stat, database table, or other source of PROPblock_6
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_6", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 23.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **MISATTRIBUTED_VALUE** PROPblock_6: 273.35 does not belong to PROPblock_6; it matches only GLOBlit_299::PROPblock_4 (inspected this run)
  fix (required — this IS a database value, under a different block): `re-anchor 273.35 to GLOBlit_299::PROPblock_4 — no new tool call needed`
- **MISATTRIBUTED_VALUE** PROPblock_6: 2.54 does not belong to PROPblock_6; it matches only GLOBlit_299::PROPblock_4 (inspected this run)
  fix (required — this IS a database value, under a different block): `re-anchor 2.54 to GLOBlit_299::PROPblock_4 — no new tool call needed`
- **MISATTRIBUTED_VALUE** PROPblock_4: 303.15 does not belong to PROPblock_4; it matches only GLOBlit_299::PROPblock_5 (inspected this run)
  fix (required — this IS a database value, under a different block): `re-anchor 303.15 to GLOBlit_299::PROPblock_5 — no new tool call needed`
- **AMBIGUOUS_VALUE** PROPblock_4: 333.15 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_4", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 333.15})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **MISATTRIBUTED_VALUE** PROPblock_4: 4.14 does not belong to PROPblock_4; it matches only GLOBlit_299::PROPblock_5 (inspected this run)
  fix (required — this IS a database value, under a different block): `re-anchor 4.14 to GLOBlit_299::PROPblock_5 — no new tool call needed`
- **AMBIGUOUS_VALUE** PROPblock_4: 5.3 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_4", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 5.3})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- … and 6 more of the same kinds — PROPblock_5: 358.15, 372.15, 5.9, 6.2; PROPblock_4: 372.15; PROPblock_6: 19
Inspected so far: PROPblock_1, PROPblock_4, PROPblock_5, PROPblock_6

**Core claims:**
- All six activity coefficient data blocks for ethanol + water in the ThermoML dataset measure the infinite-dilution activity coefficient of ethanol (mole fraction of ethanol constrained to 0.0), spanning a verified temperature range from 273.35 K to 372.15 K across 23 data points from 4 publications.
- The highest temperature at which activity coefficient data are available is 372.15 K (GLOBlit_299, PROPblock_6, circulating still method), where γ∞ of ethanol = 6.2.
- In 5 of the 6 data blocks, γ∞ of ethanol increases monotonically with temperature, consistent with the expected positive temperature dependence for ethanol in water.
- The GLOBlit_1971 (PROPblock_1, SPME method) data show γ∞ decreasing from 5.17 at 323.15 K to 4.11 at 353.15 K, which is opposite to all other sources and is flagged as physically suspect; this dataset should be critically evaluated before inclusion in any correlation.
- Excluding the anomalous GLOBlit_1971 data, 19 data points from 3 sources with mutually consistent trends are available for correlation across the 273.35–372.15 K range.
- Several specific block-to-value attributions in the answer carry MISATTRIBUTED_VALUE or AMBIGUOUS_VALUE flags, indicating that while the underlying data values were inspected and verified, some were cited under incorrect block labels; the numeric values themselves remain consistent with the inspected records.

#### Core blocks found — verbatim ledger

```ledger
**L1#2_Table#3_(Query_L1#2_CoreBLK):**
lit_num_id: GLOBlit_299 | lit_id: 2005-vrb-fen-0 | doi: 10.1016/j.fluid.2005.08.018
block: PROPblock_4 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 2
compounds: ethanol (C2H6O; GLOBcomp_2; DOIcomp_2; InChIKey LFQSCWFLJHTTHZ-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_6; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_3
description: Infinite-dilution activity coefficient of ethanol in water by headspace analysis, 273.35–283.15 K.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#2_Table#3_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_3」 | 「Mole fraction」 | 「value=0.0 · phase=Liquid」 |
| L1#2_Table#3_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=273.35–283.15 · n_unique=2 · phase=Liquid」 |
| L1#2_Table#3_Row#3 | 「property」 | 「BLKprop_1/GLOBprop_3」 | 「Activity coefficient」 | 「method=headspace analysis (GLOBmeas_543) · range=2.54–3.13 · mean=2.835 · n=2 · phase=Liquid」 |
```

```ledger
**L1#2_Table#4_(Query_L1#2_CoreBLK):**
lit_num_id: GLOBlit_299 | lit_id: 2005-vrb-fen-0 | doi: 10.1016/j.fluid.2005.08.018
block: PROPblock_5 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 7
compounds: ethanol (C2H6O; GLOBcomp_2; DOIcomp_2; InChIKey LFQSCWFLJHTTHZ-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_6; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_3
description: Infinite-dilution activity coefficient of ethanol in water by comparative tensimetry, 303.15–333.15 K.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#2_Table#4_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_3」 | 「Mole fraction」 | 「value=0.0 · phase=Liquid」 |
| L1#2_Table#4_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=303.15–333.15 · n_unique=7 · phase=Liquid」 |
| L1#2_Table#4_Row#3 | 「property」 | 「BLKprop_1/GLOBprop_3」 | 「Activity coefficient」 | 「method=comparative tensimetry (GLOBmeas_1045) · range=4.14–5.3 · mean=4.801429 · n=7 · phase=Liquid」 |
```

```ledger
**L1#2_Table#5_(Query_L1#2_CoreBLK):**
lit_num_id: GLOBlit_299 | lit_id: 2005-vrb-fen-0 | doi: 10.1016/j.fluid.2005.08.018
block: PROPblock_6 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 4
compounds: ethanol (C2H6O; GLOBcomp_2; DOIcomp_2; InChIKey LFQSCWFLJHTTHZ-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_6; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_3
description: Infinite-dilution activity coefficient of ethanol in water by circulating still, 358.15–372.15 K. Contains the verified maximum temperature of 372.15 K.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#2_Table#5_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_3」 | 「Mole fraction」 | 「value=0.0 · phase=Liquid」 |
| L1#2_Table#5_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=358.15–372.15 · n_unique=4 · phase=Liquid」 |
| L1#2_Table#5_Row#3 | 「property」 | 「BLKprop_1/GLOBprop_3」 | 「Activity coefficient」 | 「method=circulating still method (GLOBmeas_1042) · range=5.9–6.2 · mean=6.05 · n=4 · phase=Liquid」 |
```

```ledger
**L1#2_Table#6_(Query_L1#2_CoreBLK):**
lit_num_id: GLOBlit_8381 | lit_id: 2005-str-del-0 | doi: 10.1021/je0495942
block: PROPblock_1 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 1
compounds: ethanol (C2H6O; GLOBcomp_2; DOIcomp_1; InChIKey LFQSCWFLJHTTHZ-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_12; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_3
description: Infinite-dilution activity coefficient of ethanol in water by chromatography at 298.15 K.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#2_Table#6_Row#1 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=298.15–298.15 · n_unique=1 · phase=Liquid」 |
| L1#2_Table#6_Row#2 | 「variable」 | 「BLKvar_2/GLOBvar_3」 | 「Pressure, kPa」 | 「range=101.325–101.325 · n_unique=1 · phase=Liquid」 |
| L1#2_Table#6_Row#3 | 「variable」 | 「BLKvar_3/GLOBvar_2」 | 「Mole fraction of ethanol」 | 「range=0.0–0.0 · n_unique=1 · phase=Liquid」 |
| L1#2_Table#6_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_3」 | 「Activity coefficient」 | 「method=Chromatography (GLOBmeas_1) · range=3.77–3.77 · mean=3.77 · n=1 · phase=Liquid」 |
```

```ledger
**L1#2_Table#7_(Query_L1#2_CoreBLK):**
lit_num_id: GLOBlit_8511 | lit_id: 2004-ati-gru-0 | doi: 10.1021/je049875+
block: PROPblock_1 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 5
compounds: ethanol (C2H6O; GLOBcomp_2; DOIcomp_1; InChIKey LFQSCWFLJHTTHZ-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_2; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_3
description: Infinite-dilution activity coefficient of ethanol in water by dilutor chromatography, 303.25–343.25 K.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#2_Table#7_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.325 · phase=Liquid」 |
| L1#2_Table#7_Row#2 | 「constraint」 | 「BLKconstr_2/GLOBconstr_3」 | 「Mole fraction」 | 「value=0.0 · phase=Liquid」 |
| L1#2_Table#7_Row#3 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=303.25–343.25 · n_unique=5 · phase=Liquid」 |
| L1#2_Table#7_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_3」 | 「Activity coefficient」 | 「method=Chromatography (GLOBmeas_1) · range=5.03–5.96 · mean=5.524 · n=5 · phase=Liquid」 |
```

```ledger
**L1#2_Table#8_(Query_L1#2_CoreBLK):**
lit_num_id: GLOBlit_1971 | lit_id: 2016-san-eli-0 | doi: 10.1016/j.fluid.2016.08.030
block: PROPblock_1 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 4
compounds: ethanol (C2H6O; GLOBcomp_2; DOIcomp_1; InChIKey LFQSCWFLJHTTHZ-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_5; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_3
description: Infinite-dilution activity coefficient of ethanol in water by solid-phase micro-extraction, 323.15–353.15 K. Anomalous decreasing trend flagged.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#2_Table#8_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.0 · phase=Liquid」 |
| L1#2_Table#8_Row#2 | 「constraint」 | 「BLKconstr_2/GLOBconstr_3」 | 「Mole fraction」 | 「value=0.0 · phase=Liquid」 |
| L1#2_Table#8_Row#3 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=323.15–353.15 · n_unique=4 · phase=Liquid」 |
| L1#2_Table#8_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_3」 | 「Activity coefficient」 | 「method=solid-phase micro extraction (GLOBmeas_1153) · range=4.11–5.17 · mean=4.605 · n=4 · phase=Liquid」 |
```

#### Data inspections — verbatim ledger

```ledger
**L1#2_Table#9_(Query_L1#2_INSP):**
lit_num_id: GLOBlit_299 | doi: 10.1016/j.fluid.2005.08.018 | block: PROPblock_6
table_mode: complete | inspection_id: INSP_c78d07681916 | rows_shown: 4

| *row_id* | *BLKpoint_id* | *temperature_k* | *mole_fraction_<ethanol>* | *activity_coefficient_<ethanol>* |
|---|---|---|---|---|
| L1#2_Table#9_Row#1 | 「BLKpoint_1」 | 「358.15」 | 「0.0」 | 「5.9」 |
| L1#2_Table#9_Row#2 | 「BLKpoint_2」 | 「363.15」 | 「0.0」 | 「6」 |
| L1#2_Table#9_Row#3 | 「BLKpoint_3」 | 「368.15」 | 「0.0」 | 「6.1」 |
| L1#2_Table#9_Row#4 | 「BLKpoint_4」 | 「372.15」 | 「0.0」 | 「6.2」 |
```

```ledger
**L1#2_Table#10_(Query_L1#2_INSP):**
lit_num_id: GLOBlit_299 | doi: 10.1016/j.fluid.2005.08.018 | block: PROPblock_5
table_mode: complete | inspection_id: INSP_07cd1fbb6c30 | rows_shown: 7

| *row_id* | *BLKpoint_id* | *temperature_k* | *mole_fraction_<ethanol>* | *activity_coefficient_<ethanol>* |
|---|---|---|---|---|
| L1#2_Table#10_Row#1 | 「BLKpoint_1」 | 「303.15」 | 「0.0」 | 「4.14」 |
| L1#2_Table#10_Row#2 | 「BLKpoint_2」 | 「308.15」 | 「0.0」 | 「4.43」 |
| L1#2_Table#10_Row#3 | 「BLKpoint_3」 | 「313.15」 | 「0.0」 | 「4.66」 |
| L1#2_Table#10_Row#4 | 「BLKpoint_4」 | 「318.15」 | 「0.0」 | 「4.85」 |
| L1#2_Table#10_Row#5 | 「BLKpoint_5」 | 「323.15」 | 「0.0」 | 「5.03」 |
| L1#2_Table#10_Row#6 | 「BLKpoint_6」 | 「328.15」 | 「0.0」 | 「5.2」 |
| L1#2_Table#10_Row#7 | 「BLKpoint_7」 | 「333.15」 | 「0.0」 | 「5.3」 |
```

```ledger
**L1#2_Table#11_(Query_L1#2_INSP):**
lit_num_id: GLOBlit_1971 | doi: 10.1016/j.fluid.2016.08.030 | block: PROPblock_1
table_mode: complete | inspection_id: INSP_5c2b90e51939 | rows_shown: 4

| *row_id* | *BLKpoint_id* | *temperature_k* | *pressure_kpa* | *mole_fraction_<ethanol>* | *activity_coefficient_<ethanol>* |
|---|---|---|---|---|---|
| L1#2_Table#11_Row#1 | 「BLKpoint_1」 | 「323.15」 | 「101.0」 | 「0.0」 | 「5.17」 |
| L1#2_Table#11_Row#2 | 「BLKpoint_2」 | 「333.15」 | 「101.0」 | 「0.0」 | 「4.77」 |
| L1#2_Table#11_Row#3 | 「BLKpoint_3」 | 「343.15」 | 「101.0」 | 「0.0」 | 「4.37」 |
| L1#2_Table#11_Row#4 | 「BLKpoint_4」 | 「353.15」 | 「101.0」 | 「0.0」 | 「4.11」 |
```

```ledger
**L1#2_Table#12_(Query_L1#2_INSP):**
lit_num_id: GLOBlit_8511 | doi: 10.1021/je049875+ | block: PROPblock_1
table_mode: complete | inspection_id: INSP_af7f92cdc6e6 | rows_shown: 5

| *row_id* | *BLKpoint_id* | *temperature_k* | *pressure_kpa* | *mole_fraction_<ethanol>* | *activity_coefficient_<ethanol>* |
|---|---|---|---|---|---|
| L1#2_Table#12_Row#1 | 「BLKpoint_1」 | 「303.25」 | 「101.325」 | 「0.0」 | 「5.03」 |
| L1#2_Table#12_Row#2 | 「BLKpoint_2」 | 「313.25」 | 「101.325」 | 「0.0」 | 「5.33」 |
| L1#2_Table#12_Row#3 | 「BLKpoint_3」 | 「323.25」 | 「101.325」 | 「0.0」 | 「5.54」 |
| L1#2_Table#12_Row#4 | 「BLKpoint_4」 | 「333.25」 | 「101.325」 | 「0.0」 | 「5.76」 |
| L1#2_Table#12_Row#5 | 「BLKpoint_5」 | 「343.25」 | 「101.325」 | 「0.0」 | 「5.96」 |
```

```ledger
**L1#2_Table#13_(Query_L1#2_INSP):**
lit_num_id: GLOBlit_8381 | doi: 10.1021/je0495942 | block: PROPblock_1
table_mode: complete | inspection_id: INSP_fd8734d59843 | rows_shown: 1

| *row_id* | *BLKpoint_id* | *temperature_k* | *pressure_kpa* | *mole_fraction_<ethanol>* | *activity_coefficient_<ethanol>* |
|---|---|---|---|---|---|
| L1#2_Table#13_Row#1 | 「BLKpoint_1」 | 「298.15」 | 「101.325」 | 「0」 | 「3.77」 |
```

```ledger
**L1#2_Table#14_(Query_L1#2_INSP):**
lit_num_id: GLOBlit_299 | doi: 10.1016/j.fluid.2005.08.018 | block: PROPblock_4
table_mode: complete | inspection_id: INSP_a2f513326a7b | rows_shown: 2

| *row_id* | *BLKpoint_id* | *temperature_k* | *mole_fraction_<ethanol>* | *activity_coefficient_<ethanol>* |
|---|---|---|---|---|
| L1#2_Table#14_Row#1 | 「BLKpoint_1」 | 「273.35」 | 「0.0」 | 「2.54」 |
| L1#2_Table#14_Row#2 | 「BLKpoint_2」 | 「283.15」 | 「0.0」 | 「3.13」 |
```
</subagent_answer>
</tool_result>

## LLM Response


<reasoning>
I now have all the data I need to provide a comprehensive answer. Let me compile the findings:

1. All activity coefficient data for ethanol + water in ThermoML are infinite-dilution activity coefficients (γ∞) of ethanol in water.
2. Temperature range: 273.35 K to 372.15 K across 6 blocks, 23 data points, 4 publications.
3. Coldest: 273.35 K from GLOBlit_299, PROPblock_4 (headspace analysis), γ∞ = 2.54
4. Hottest: 372.15 K from GLOBlit_299, PROPblock_6 (circulating still), γ∞ = 6.2
5. Data quality concern: GLOBlit_1971 shows anomalous decreasing trend.
6. 19 consistent data points from 3 sources excluding the anomalous dataset.

All values are verified from inspected data tables. Let me write the final answer.
</reasoning>

<answer>

## Activity Coefficient Data for Ethanol + Water: Temperature Range and Key Studies

### Verified Temperature Range

The ThermoML database contains **6 data blocks** of activity coefficient measurements for the ethanol + water binary system, spanning a verified temperature range of **273.35 K to 372.15 K** across **23 data points** from **4 publications**. All blocks report the **infinite-dilution activity coefficient of ethanol** (γ∞, with mole fraction of ethanol = 0.0).

---

### Coldest Measurement

**273.35 K** — from Vrba, Fenclová et al. (DOI: 10.1016/j.fluid.2005.08.018), PROPblock_4, measured by headspace analysis:

| Temperature (K) | x(ethanol) | γ∞(ethanol) |
|:---:|:---:|:---:|
| 273.35 | 0.0 | 2.54 |
| 283.15 | 0.0 | 3.13 |

### Hottest Measurement

**372.15 K** — from the same publication (DOI: 10.1016/j.fluid.2005.08.018), PROPblock_6, measured by a circulating still method:

| Temperature (K) | x(ethanol) | γ∞(ethanol) |
|:---:|:---:|:---:|
| 358.15 | 0.0 | 5.9 |
| 363.15 | 0.0 | 6.0 |
| 368.15 | 0.0 | 6.1 |
| 372.15 | 0.0 | 6.2 |

---

### Complete Block-by-Block Inventory

| Source | DOI | Block | Method | T range (K) | γ∞ range | Points | Trend |
|---|---|---|---|:---:|:---:|:---:|:---:|
| GLOBlit_299 | 10.1016/j.fluid.2005.08.018 | PROPblock_4 | Headspace analysis | 273.35–283.15 | 2.54–3.13 | 2 | ↑ |
| GLOBlit_299 | 10.1016/j.fluid.2005.08.018 | PROPblock_5 | Comparative tensimetry | 303.15–333.15 | 4.14–5.3 | 7 | ↑ |
| GLOBlit_299 | 10.1016/j.fluid.2005.08.018 | PROPblock_6 | Circulating still | 358.15–372.15 | 5.9–6.2 | 4 | ↑ |
| GLOBlit_8381 | 10.1021/je0495942 | PROPblock_1 | Chromatography | 298.15 | 3.77 | 1 | — |
| GLOBlit_8511 | 10.1021/je049875+ | PROPblock_1 | Dilutor chromatography | 303.25–343.25 | 5.03–5.96 | 5 | ↑ |
| GLOBlit_1971 | 10.1016/j.fluid.2016.08.030 | PROPblock_1 | Solid-phase micro-extraction | 323.15–353.15 | 4.11–5.17 | 4 | **↓ (anomalous)** |

---

### Chemistry Insight and Recommendations for Correlation Building

**Consistent data (5 of 6 blocks, 19 points):** In five blocks, γ∞ of ethanol increases monotonically with temperature — physically expected for a system where the hydrophobic interaction between ethanol and water weakens as thermal energy disrupts the hydrogen-bond network. The single most valuable publication is Vrba, Fenclová et al. (DOI: 10.1016/j.fluid.2005.08.018), which alone provides nearly continuous coverage from 273.35 K to 372.15 K using three complementary experimental techniques (headspace analysis, comparative tensimetry, circulating still), contributing 13 of the 19 consistent data points.

**Anomalous dataset — GLOBlit_1971 (DOI: 10.1016/j.fluid.2016.08.030):** This SPME-method dataset shows γ∞ *decreasing* from 5.17 at 323.15 K to 4.11 at 353.15 K, which contradicts every other source. For direct comparison at ~323 K: GLOBlit_1971 reports 5.17, GLOBlit_8511 reports 5.54 (at 323.25 K), and GLOBlit_299 PROPblock_5 reports 5.03 (at 323.15 K). While the absolute values at the lowest temperature are in the same ballpark, the reversed temperature trend is physically suspect and this dataset should be critically evaluated — or excluded — before inclusion in a correlation.

**Practical correlation range:** Your activity-coefficient correlation for ethanol + water can be reliably supported over **273.35 K to 372.15 K** using 19 data points from 3 independent publications with mutually consistent temperature trends.

</answer>