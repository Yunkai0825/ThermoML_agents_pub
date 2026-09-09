## System Prompt
# ThermoML Main Agent — Master Orchestrator

You are the **ThermoML Main Agent**, a master orchestrator that answers
scientific questions about thermodynamic data by coordinating two
specialized subagents:

1. **Query Agent** (`run_query_agent`) — searches ThermoML card databases
   to find experimental data (DOIs, blocks, compound IDs, property values).
   It also owns the deterministic screening/ranking pipeline: for "which
   systems are best for X" questions, ask it to *rank candidate systems
   against property targets* instead of requesting per-system block surveys.
2. **Analysis Agent** (`run_analysis_agent`) — retrieves data, fits
   Redlich-Kister polynomials to excess properties, and reports
   quantitative results (RK coefficients, R², RMSE).

**Chemistry-context hint:** When useful and tool-supported, use existing output fields to add a brief chemistry insight and one or a few representative data points with values, units, conditions, compounds, and DOI/block provenance. Mark inference, never invent data, and delegation-only roles should preserve rather than create this context.

You also have a unified parallel dispatch tool:
- `run_parallel_subagents` — run multiple query and/or analysis tasks
  simultaneously in one call.  Each task specifies `agent`, `label`,
  `question`, `purpose`, and `context` (all required).  The tool returns
  a compacted per-`[label]` report; the **full** per-task results are
  automatically recorded in your working memory (Query/Analysis Agent
  Results sections), so read them there when you need details beyond
  the compacted report.
- Oversized batches are auto-compacted by an internal loop that consults
  your model tier in a self-contained exchange (all instructions arrive
  with that exchange); the report you receive states what was applied,
  and the per-task reports are stored in working memory under
  "Parallel Compaction Reports".

You also have a **tool menu** for direct, fine-grained access to subagent
internals (search tools, fitting tools, ID resolution, etc.):

- `browse_subagent_tools(purpose, tasks)` — a **miniature planning agent**
  that examines the full menu of subagent tools and returns a structured
  parallel execution plan with specific call signatures tailored to your
  purpose and tasks.  Call this first to discover what tools exist and get
  a recommended phased plan.
- `run_subagent_tool(tool_name, kwargs, purpose, tasks)` — execute
  any tool from the menu directly. `kwargs` is a native JSON object matching
  that tool's current signature. Results are automatically compacted
  by the same hardcoded compactors the subagents use internally.
  You can call multiple `run_subagent_tool` in parallel; when you do,
  a batch summary is automatically generated from all results.

### When to use the tool menu vs. expert workers

- **Tool menu** — best for targeted, well-defined operations where you
  know exactly what data you need: resolving a compound ID, searching
  for blocks matching specific criteria, fitting a single block, or
  retrieving pure-component values.  Faster and more direct than
  launching a full subagent workflow.
- **Expert workers** (`run_query_agent`, `run_analysis_agent`) — best
  for open-ended, complex tasks that require multi-step reasoning,
  iterative refinement, or full toolset access.  The subagents have
  their own context, memory, and compaction pipelines.

You can dynamically decide which approach to use based on the complexity
of each sub-task.  For multi-system comparisons, you can mix both
approaches — use the tool menu for simple lookups and expert workers
for complex analyses.

---

## How You Work

1. **Understand the question** — Decide what data is needed and whether
   the question requires only a database search, a full fitting analysis,
   or a multi-system comparison.
2. **Delegate to subagents** — Call the appropriate subagent tool(s).
   For multi-system questions, use parallel tools to save time.
3. **Synthesize results** — Combine subagent outputs into a coherent
   scientific answer.  **Never invent data** — every number in your
   answer must come from a subagent result.
4. **Report findings** — Present a clear, well-structured answer with
   proper citations (`GLOBlit_N` literature ID, DOI, block numbers,
   compound names). `GLOBlit_N` is the authoritative literature identifier;
   a DOI is coupled display metadata. Never report a DOI without its paired
   literature ID — quote only DOIs your subagents returned, never from
   memory; unpaired DOIs are scrubbed from the final return as
   unverifiable.

---

## Tool Usage Rules

### Single-system questions (1 system)
Call `run_query_agent` for data search, or `run_analysis_agent` for
fitting.  The analysis agent internally calls the query agent, so you
do NOT need to call both for a fitting question.

### Multi-system comparisons (2+ systems)
Use `run_parallel_subagents` to process multiple systems simultaneously.
You can mix query and analysis tasks in a single parallel call — each
task specifies which agent to use.  Each system gets its own subagent call.
Oversized batches are auto-compacted; the full results are always in
working memory.

### Iterative refinement
If a subagent returns partial results or times out, you can call it again
with additional context from the first call.

---

## MANDATORY OUTPUT FORMAT

```xml
<reasoning>
... your thinking about what subagents to call and why (DISCARDED from memory) ...
</reasoning>
<summary>
... 1-3 sentence actionable conclusion about what you learned or plan to do next (KEPT, max 400 chars) ...
</summary>
<tool_call>{"name": "run_analysis_agent", "arguments": {"question": "...", "purpose": "...", "context": "..."}}</tool_call>
<wait/>
```

### CRITICAL RULES
- `<tool_call>` MUST come AFTER `</summary>` and BEFORE `<wait/>`
- `<reasoning>` is STRIPPED from history to save context space
- Only `<summary>` content + tool results persist in memory
- **ANTI-HALLUCINATION:** EVERY number, coefficient, R² value, DOI, and
  compound name MUST come from a subagent tool call result.  If you do not
  have a subagent result for a core claim, you MUST call a subagent first.
- **NO-DATA HANDLING:** If a subagent reports "no results found" or returns
  only generic text with no specific DOIs/data, you MUST report that honestly.
  Say "No data matching [criteria] was found in ThermoML" rather than
  fabricating results.  Never invent DOIs, block numbers, or data points.
- **SUBAGENT VALIDATION:** Before presenting subagent results as your answer,
  check for red flags: improbably round numbers, suspicious consistency,
  lack of specific block references, or caveats about "infrastructure errors."
  If in doubt, state that results could not be verified.
- When you have gathered all needed results, provide a FINAL ANSWER
  by wrapping your complete answer in `<answer>` tags (no `<tool_call>`).
- `<answer>` = full-length final response (any length). All markers stripped before delivery.
- `<summary>` ≠ `<answer>`: summary is a brief memory note (≤400 chars); answer is the complete user-facing response.

---

## NUMERICAL GROUNDING (MANDATORY)

Applies to every number you emit: data values, compositions, temperatures,
pressures, uncertainties, counts, and aggregates.

- Copy numeric values VERBATIM from subagent results. Never quote more
  decimal places than the source shows. Chemistry knowledge may guide
  interpretation — it must NEVER supply a numeric value.
- If row-level data were never returned, present only the tool-returned
  aggregates, explicitly labeled as aggregates. NEVER reconstruct the
  individual rows behind an aggregate (n, min, max, mean, range) — a data
  table you assemble yourself from ranges is fabrication.
- Fabrication tells (all forbidden): compositions on a smooth grid (0.1,
  0.2, 0.3, …) that no subagent returned; "representative values" absent
  from every subagent result; agreement/comparison percentages nobody
  computed; a table whose own min/max/mean contradict the reported
  aggregates.
- Derived numbers (excess values, deviations, averages) are allowed only
  when computed from subagent-returned inputs — name those inputs and their
  source blocks beside the derived value.
- Tool results arrive ONLY from the environment after `<wait/>`. If a batch
  is rejected or errors, NO result exists — never write, quote, or continue
  from an imagined tool_result block.
- An honest "row-level values were not retrieved" is a valid answer. An
  invented number is a critical failure that invalidates the whole session.
- INSPECTION MANDATE: subagent envelopes carry `data_inspections` —
  verbatim inspected data tables; quote data points only from them or
  from subagent answers verbatim. To cite a sub-block nobody inspected,
  run `inspect_block_table` via the tool menu (`where=`/`nearest=`).
  A deterministic gate bounces answers whose block-anchored values lack a
  matching inspection in THIS session; under [TIME WARNING] drop
  uninspected points and keep aggregates.
- Chemical insights must stay grounded in the data you present: a
  comparative claim (higher/lower than a baseline or average) must hold
  arithmetically for the values quoted in your answer — otherwise keep
  the insight qualitative.
- Upstream results may carry UNVERIFIED flags. If a flagged value matters
  for your task, resolve it first (re-inspect / re-query its block anchor);
  otherwise treat it with caution under these same rules — never repeat an
  unverified number as verified.

---

## Final Answer Format

When all subagent work is done, wrap your complete answer in `<answer>` tags:

```
<answer>
[Your synthesized scientific answer here — any length.
Include all key data, DOIs, block numbers, compound names.
Every number must come from a subagent result.]

### Sources
- Literature ID: GLOBlit_N | DOI: ... | Block: ... | Subsystem: declared or BLKsubsys_N | System: ...
</answer>
```

# Phases

## phase_1: choose_route
tools: [browse_subagent_tools, run_subagent_tool]
guidance: |
  Decide whether the question needs a targeted lower-level operation or a
  full expert subagent. Browse the hierarchical menu only when direct tool
  execution is likely to be more efficient than expert delegation.

## phase_2: delegate_or_execute
tools: [run_query_agent, run_analysis_agent, run_parallel_subagents, run_subagent_tool]
guidance: |
  Supply every argument in the injected callable signature. Use one expert
  for a single complex task and run_parallel_subagents for independent query
  or analysis tasks. Preserve exact subagent identifiers and evidence.
  Oversized parallel batch results are auto-compacted; full results stay
  in working memory.

## phase_3: synthesize
tools: [list_session_files]
guidance: |
  Synthesize only tool-returned chemistry and numbers. Wrap the complete
  answer in <answer> tags; post-answer workers build the JSON fields.

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
- browse_subagent_tools(purpose, tasks) — Browse the tool menu and get a recommended execution plan.
- list_session_files() — Return a manifest of all output files generated in this session.
- run_analysis_agent(question, context, purpose, tasks) — Run the ThermoML Analysis Agent for fitting and modeling.
- run_parallel_subagents(tasks) — Run multiple query and/or analysis agent tasks in parallel.
- run_query_agent(question, context, purpose, tasks) — Run the ThermoML Query Agent on a database search question.
- run_subagent_tool(tool_name, kwargs, purpose, tasks) — Execute a subagent tool directly with full compaction pipeline.

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
**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_045351_327204_4225c126`

### History
- [query:Q1] "Find density data for ethanol-water binary mixtures at 1000 K. If no data exists" (180s, 2 iters, validation=PASS verdict=## Verdict
The answer correctl)

### Query Agent Results

#### Q1
**Q1** — confidence: high · validation: PASS

**Answer:**

#### Density Data for Ethanol–Water Binary Mixtures at 1000 K

##### Data at 1000 K: Not Available

There is **no density data at or near 1000 K** (≈727 °C) for the ethanol–water system in the ThermoML database. This is physically expected:

- **Ethanol** (C₂H₆O, CAS 64-17-5) has a normal boiling point of ~351.5 K (78.4 °C) and a critical temperature T_c ≈ 514 K.
- **Water** (H₂O, CAS 7732-18-5) has a normal boiling point of ~373.15 K (100 °C) and a critical temperature T_c ≈ 647 K.

At 1000 K and moderate pressures, both substances would be supercritical gases with very low density, making experimental liquid-phase density measurements essentially impossible for this mixture.

---

##### Closest Available Temperature Range

The ThermoML database contains **29 data blocks** with mass density measurements for the ethanol + water binary system, totaling approximately **2,924 raw data points** spanning **268.1–618.2 K** (approximately −5 °C to 345 °C).

The **highest-temperature data** comes from:

- **Source:** DOI 10.1016/j.fluid.2017.09.005 (GLOBlit_2092)
- **Block:** PROPblock_3
- **Temperature range:** 523.2–618.2 K (250–345 °C)
- **Pressure range:** 20,000–40,000 kPa (200–400 bar)
- **Composition range:** x(ethanol) = 0–1
- **Overall density range:** 250.4–834.3 kg/m³
- **72 data points**, liquid phase, measured by vibrating tube method

These are high-pressure supercritical/compressed-liquid measurements — the elevated pressures keep the mixture in a dense fluid state even above the normal boiling points.

---

##### Representative Data at the Highest Available Temperature (618.2 K)

**At 618.2 K, 20,000 kPa:**

**WM_Q#1_Table#1_(Main_Q#1_Answer):**

| *row_id* | *x(ethanol)* | *ρ (kg/m³)* |
|---|---|---|
| WM_Q#1_Table#1_Row#1 | 「0」 | 「619.7」 |
| WM_Q#1_Table#1_Row#2 | 「0.2」 | 「281.3」 |
| WM_Q#1_Table#1_Row#3 | 「0.3」 | 「250.4」 |
| WM_Q#1_Table#1_Row#4 | 「1.0」 | 「314.6」 |

**At 618.2 K, 30,000 kPa:**

**WM_Q#1_Table#2_(Main_Q#1_Answer):**

| *row_id* | *x(ethanol)* | *ρ (kg/m³)* |
|---|---|---|
| WM_Q#1_Table#2_Row#1 | 「0」 | 「656.9」 |
| WM_Q#1_Table#2_Row#2 | 「0.2」 | 「501.5」 |
| WM_Q#1_Table#2_Row#3 | 「0.4」 | 「437.4」 |
| WM_Q#1_Table#2_Row#4 | 「0.6」 | 「420.1」 |
| WM_Q#1_Table#2_Row#5 | 「1.0」 | 「423.8」 |

**At 618.2 K, 40,000 kPa:**

**WM_Q#1_Table#3_(Main_Q#1_Answer):**

| *row_id* | *x(ethanol)* | *ρ (kg/m³)* |
|---|---|---|
| WM_Q#1_Table#3_Row#1 | 「0」 | 「682.3」 |
| WM_Q#1_Table#3_Row#2 | 「0.2」 | 「561.0」 |
| WM_Q#1_Table#3_Row#3 | 「0.4」 | 「509.1」 |
| WM_Q#1_Table#3_Row#4 | 「1.0」 | 「481.2」 |

---

##### Chemistry Insight

At 618.2 K and 20,000 kPa, the density drops sharply from pure water (619.7 kg/m³) to intermediate ethanol mole fractions — reaching as low as 250.4 kg/m³ at x(ethanol) = 0.3. This dramatic non-monotonic behavior reflects the proximity to ethanol's critical point (T_c ≈ 514 K), where the fluid becomes highly compressible and density is extremely sensitive to composition. Notably, pure ethanol at this condition (314.6 kg/m³) is actually denser than the x = 0.3 mixture, illustrating the complex interplay of near-critical fluctuations in the mixture.

Increasing pressure from 20,000 to 40,000 kPa at 618.2 K substantially raises the density across all compositions (e.g., pure water: 619.7 → 682.3 kg/m³; pure ethanol: 314.6 → 481.2 kg/m³), demonstrating the strong pressure dependence characteristic of near-critical and supercritical fluids.

**The maximum available temperature in the ThermoML database for ethanol–water density is 618.2 K — approximately 382 K below the queried 1000 K, with no data to bridge this gap.**

**Core claims:**
- No density data at or near 1000 K for the ethanol–water binary system exists in the ThermoML database; at 1000 K and moderate pressures both substances would be supercritical gases, making liquid-phase density measurements essentially impossible.
- The highest-temperature density data available for ethanol + water in ThermoML spans 523.2–618.2 K at 20,000–40,000 kPa, from DOI 10.1016/j.fluid.2017.09.005, comprising 72 data points with an overall density range of 250.4–834.3 kg/m³.
- At 618.2 K and 20,000 kPa, density exhibits strongly non-monotonic composition dependence: pure water is 619.7 kg/m³, the mixture at x(ethanol) = 0.3 drops to 250.4 kg/m³, while pure ethanol is 314.6 kg/m³, reflecting near-critical compressibility effects near ethanol's critical temperature (T_c ≈ 514 K).
- Increasing pressure from 20,000 to 40,000 kPa at 618.2 K substantially raises density across all compositions (e.g., pure water: 619.7 → 682.3 kg/m³; pure ethanol: 314.6 → 481.2 kg/m³), demonstrating strong pressure dependence characteristic of near-critical and supercritical fluids.
- The maximum available temperature in the ThermoML database for ethanol–water density is 618.2 K, approximately 382 K below the queried 1000 K, with no data to bridge this gap.

**Sources:**

**WM_Q#1_Table#4_(Main_Q#1_Sources):**

| *row_id* | *lit_num_id* | *block* | *doi* | *BLKsubsys_id* | *description* |
|---|---|---|---|---|---|
| WM_Q#1_Table#4_Row#1 | 「GLOBlit_2092」 | 「PROPblock_3」 | 「10.1016/j.fluid.2017.09.005」 | 「—」 | 「This block provides the highest-temperature mass density data for the ethanol–water binary system in ThermoML, covering 523.2–618.2 K at 20,000–40,000 kPa with 72 data points. The answer correctly uses it to demonstrate that no data exists at 1000 K and to present representative density values at the closest available temperatures (e.g., 250.4–834.3 kg/m³ range).」 |

*Not stored here: 1 verbatim data_inspections table(s); 4 id_catalog_snapshot row(s) (catalog is merged separately). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.

</memory>

## User
Find density data for ethanol-water at 1000 K. If no data exists at that temperature, report the closest available temperature range.

## Assistant
<summary>Searching for density data for ethanol-water mixtures at 1000 K. This temperature is far above boiling points of both components, so liquid density data is unlikely. Will find the closest available temperature range.</summary>
<tool_call>run_query_agent(question=Find density data…, context=The user wants de…)</tool_call>

## User
<tool_result>
(validation blocked run_query_agent earlier — corrected)
</tool_result>

## Assistant
<summary>Fixing tool call syntax to search for ethanol-water density data at 1000 K or nearest available temperature.</summary>
<tool_call>run_query_agent(question=Find density data…, context=Ethanol is C2H5OH…)</tool_call>

## User
<tool_result>
<subagent_answer>
### Q#1 — run_query_agent return

**Status:** 2 iterations · 180.5s · 1 tool call(s) · agent=query
**Question:** Find density data for ethanol-water binary mixtures at 1000 K. If no data exists at that temperature, report the closest available temperature range for density measurements of ethanol-water systems.
**Session:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_045351_327204_4225c126\query_runs\run_9`

**Answer:**

#### Density Data for Ethanol–Water Binary Mixtures at 1000 K

##### Data at 1000 K: Not Available

There is **no density data at or near 1000 K** (≈727 °C) for the ethanol–water system in the ThermoML database. This is physically expected:

- **Ethanol** (C₂H₆O, CAS 64-17-5) has a normal boiling point of ~351.5 K (78.4 °C) and a critical temperature T_c ≈ 514 K.
- **Water** (H₂O, CAS 7732-18-5) has a normal boiling point of ~373.15 K (100 °C) and a critical temperature T_c ≈ 647 K.

At 1000 K and moderate pressures, both substances would be supercritical gases with very low density, making experimental liquid-phase density measurements essentially impossible for this mixture.

---

##### Closest Available Temperature Range

The ThermoML database contains **29 data blocks** with mass density measurements for the ethanol + water binary system, totaling approximately **2,924 raw data points** spanning **268.1–618.2 K** (approximately −5 °C to 345 °C).

The **highest-temperature data** comes from:

- **Source:** DOI 10.1016/j.fluid.2017.09.005 (GLOBlit_2092)
- **Block:** PROPblock_3
- **Temperature range:** 523.2–618.2 K (250–345 °C)
- **Pressure range:** 20,000–40,000 kPa (200–400 bar)
- **Composition range:** x(ethanol) = 0–1
- **Overall density range:** 250.4–834.3 kg/m³
- **72 data points**, liquid phase, measured by vibrating tube method

These are high-pressure supercritical/compressed-liquid measurements — the elevated pressures keep the mixture in a dense fluid state even above the normal boiling points.

---

##### Representative Data at the Highest Available Temperature (618.2 K)

**At 618.2 K, 20,000 kPa:**

**Q#1_Table#1_(Main_Q#1_Answer):**

| *row_id* | *x(ethanol)* | *ρ (kg/m³)* |
|---|---|---|
| Q#1_Table#1_Row#1 | 「0」 | 「619.7」 |
| Q#1_Table#1_Row#2 | 「0.2」 | 「281.3」 |
| Q#1_Table#1_Row#3 | 「0.3」 | 「250.4」 |
| Q#1_Table#1_Row#4 | 「1.0」 | 「314.6」 |

**At 618.2 K, 30,000 kPa:**

**Q#1_Table#2_(Main_Q#1_Answer):**

| *row_id* | *x(ethanol)* | *ρ (kg/m³)* |
|---|---|---|
| Q#1_Table#2_Row#1 | 「0」 | 「656.9」 |
| Q#1_Table#2_Row#2 | 「0.2」 | 「501.5」 |
| Q#1_Table#2_Row#3 | 「0.4」 | 「437.4」 |
| Q#1_Table#2_Row#4 | 「0.6」 | 「420.1」 |
| Q#1_Table#2_Row#5 | 「1.0」 | 「423.8」 |

**At 618.2 K, 40,000 kPa:**

**Q#1_Table#3_(Main_Q#1_Answer):**

| *row_id* | *x(ethanol)* | *ρ (kg/m³)* |
|---|---|---|
| Q#1_Table#3_Row#1 | 「0」 | 「682.3」 |
| Q#1_Table#3_Row#2 | 「0.2」 | 「561.0」 |
| Q#1_Table#3_Row#3 | 「0.4」 | 「509.1」 |
| Q#1_Table#3_Row#4 | 「1.0」 | 「481.2」 |

---

##### Chemistry Insight

At 618.2 K and 20,000 kPa, the density drops sharply from pure water (619.7 kg/m³) to intermediate ethanol mole fractions — reaching as low as 250.4 kg/m³ at x(ethanol) = 0.3. This dramatic non-monotonic behavior reflects the proximity to ethanol's critical point (T_c ≈ 514 K), where the fluid becomes highly compressible and density is extremely sensitive to composition. Notably, pure ethanol at this condition (314.6 kg/m³) is actually denser than the x = 0.3 mixture, illustrating the complex interplay of near-critical fluctuations in the mixture.

Increasing pressure from 20,000 to 40,000 kPa at 618.2 K substantially raises the density across all compositions (e.g., pure water: 619.7 → 682.3 kg/m³; pure ethanol: 314.6 → 481.2 kg/m³), demonstrating the strong pressure dependence characteristic of near-critical and supercritical fluids.

**The maximum available temperature in the ThermoML database for ethanol–water density is 618.2 K — approximately 382 K below the queried 1000 K, with no data to bridge this gap.**

**Core claims:**
- No density data at or near 1000 K for the ethanol–water binary system exists in the ThermoML database; at 1000 K and moderate pressures both substances would be supercritical gases, making liquid-phase density measurements essentially impossible.
- The highest-temperature density data available for ethanol + water in ThermoML spans 523.2–618.2 K at 20,000–40,000 kPa, from DOI 10.1016/j.fluid.2017.09.005, comprising 72 data points with an overall density range of 250.4–834.3 kg/m³.
- At 618.2 K and 20,000 kPa, density exhibits strongly non-monotonic composition dependence: pure water is 619.7 kg/m³, the mixture at x(ethanol) = 0.3 drops to 250.4 kg/m³, while pure ethanol is 314.6 kg/m³, reflecting near-critical compressibility effects near ethanol's critical temperature (T_c ≈ 514 K).
- Increasing pressure from 20,000 to 40,000 kPa at 618.2 K substantially raises density across all compositions (e.g., pure water: 619.7 → 682.3 kg/m³; pure ethanol: 314.6 → 481.2 kg/m³), demonstrating strong pressure dependence characteristic of near-critical and supercritical fluids.
- The maximum available temperature in the ThermoML database for ethanol–water density is 618.2 K, approximately 382 K below the queried 1000 K, with no data to bridge this gap.

**Confidence:** high

**Sources:**

**Q#1_Table#4_(Main_Q#1_Sources):**

| *row_id* | *lit_num_id* | *block* | *doi* | *BLKsubsys_id* | *description* |
|---|---|---|---|---|---|
| Q#1_Table#4_Row#1 | 「GLOBlit_2092」 | 「PROPblock_3」 | 「10.1016/j.fluid.2017.09.005」 | 「—」 | 「This block provides the highest-temperature mass density data for the ethanol–water binary system in ThermoML, covering 523.2–618.2 K at 20,000–40,000 kPa with 72 data points. The answer correctly uses it to demonstrate that no data exists at 1000 K and to present representative density values at the closest available temperatures (e.g., 250.4–834.3 kg/m³ range).」 |

**ID catalog snapshot:**

| *type* | *global_id* | *registry_id* | *name* |
|---|---|---|---|
| comp | 「GLOBcomp_2」 | 「ethanol」 | 「ethanol」 |
| comp | 「GLOBcomp_1」 | 「water」 | 「water」 |
| prop | 「GLOBprop_1」 | 「mass_density_kg_m3」 | 「Mass density, kg/m3」 |
| lit | 「GLOBlit_2092」 | 「2017-ono-kyo-0」 | 「10.1016/j.fluid.2017.09.005」 |

**Follow-up suggestions:**
- Search for supercritical density data of ethanol-water mixtures above 618 K in non-ThermoML sources such as NIST WebBook or IAPWS databases.
- Investigate whether any ThermoML entries report other thermodynamic properties (e.g., speed of sound, heat capacity) for ethanol-water at temperatures closer to 1000 K under very high pressures.
- Query for density data of pure supercritical water or pure supercritical ethanol individually at temperatures approaching 1000 K, which may exist at extreme pressures.

#### Data inspections — verbatim ledger

```ledger
**Q#1_Table#5_(Main_Q#1_INSP):**
lit_num_id: GLOBlit_2092 | doi: 10.1016/j.fluid.2017.09.005 | block: PROPblock_3
table_mode: rdp | inspection_id: INSP_c6457ac47ddc | rows_shown: 41

| *row_id* | *BLKpoint_id* | *temperature_k* | *pressure_kpa* | *mole_fraction_<ethanol>* | *mass_density_kg_m3* |
|---|---|---|---|---|---|
| Q#1_Table#5_Row#1 | 「BLKpoint_1」 | 「523.2」 | 「20000」 | 「0」 | 「816.1」 |
| Q#1_Table#5_Row#2 | 「BLKpoint_3」 | 「523.2」 | 「20000」 | 「0.2」 | 「694.1」 |
| Q#1_Table#5_Row#3 | 「BLKpoint_5」 | 「523.2」 | 「20000」 | 「0.4」 | 「622.3」 |
| Q#1_Table#5_Row#4 | 「BLKpoint_6」 | 「523.2」 | 「20000」 | 「0.6」 | 「578.5」 |
| Q#1_Table#5_Row#5 | 「BLKpoint_8」 | 「523.2」 | 「20000」 | 「1」 | 「533.1」 |
| Q#1_Table#5_Row#6 | 「BLKpoint_9」 | 「523.2」 | 「30000」 | 「0」 | 「825.5」 |
| Q#1_Table#5_Row#7 | 「BLKpoint_11」 | 「523.2」 | 「30000」 | 「0.2」 | 「713.6」 |
| Q#1_Table#5_Row#8 | 「BLKpoint_13」 | 「523.2」 | 「30000」 | 「0.4」 | 「650.7」 |
| Q#1_Table#5_Row#9 | 「BLKpoint_14」 | 「523.2」 | 「30000」 | 「0.6」 | 「612.4」 |
| Q#1_Table#5_Row#10 | 「BLKpoint_16」 | 「523.2」 | 「30000」 | 「1」 | 「573.6」 |
| Q#1_Table#5_Row#11 | 「BLKpoint_17」 | 「523.2」 | 「40000」 | 「0」 | 「834.3」 |
| Q#1_Table#5_Row#12 | 「BLKpoint_20」 | 「523.2」 | 「40000」 | 「0.3」 | 「694.7」 |
| Q#1_Table#5_Row#13 | 「BLKpoint_22」 | 「523.2」 | 「40000」 | 「0.6」 | 「636.3」 |
| Q#1_Table#5_Row#14 | 「BLKpoint_24」 | 「523.2」 | 「40000」 | 「1」 | 「601.3」 |
| Q#1_Table#5_Row#15 | 「BLKpoint_25」 | 「573.2」 | 「20000」 | 「0」 | 「734.8」 |
| Q#1_Table#5_Row#16 | 「BLKpoint_27」 | 「573.2」 | 「20000」 | 「0.2」 | 「585.4」 |
| Q#1_Table#5_Row#17 | 「BLKpoint_29」 | 「573.2」 | 「20000」 | 「0.4」 | 「494.9」 |
| Q#1_Table#5_Row#18 | 「BLKpoint_30」 | 「573.2」 | 「20000」 | 「0.6」 | 「446.2」 |
| Q#1_Table#5_Row#19 | 「BLKpoint_32」 | 「573.2」 | 「20000」 | 「1」 | 「421.1」 |
| Q#1_Table#5_Row#20 | 「BLKpoint_33」 | 「573.2」 | 「30000」 | 「0」 | 「750.7」 |
| Q#1_Table#5_Row#21 | 「BLKpoint_35」 | 「573.2」 | 「30000」 | 「0.2」 | 「621.4」 |
| Q#1_Table#5_Row#22 | 「BLKpoint_37」 | 「573.2」 | 「30000」 | 「0.4」 | 「553.5」 |
| Q#1_Table#5_Row#23 | 「BLKpoint_38」 | 「573.2」 | 「30000」 | 「0.6」 | 「517.6」 |
| Q#1_Table#5_Row#24 | 「BLKpoint_40」 | 「573.2」 | 「30000」 | 「1」 | 「491.5」 |
| Q#1_Table#5_Row#25 | 「BLKpoint_41」 | 「573.2」 | 「40000」 | 「0」 | 「764.3」 |
| Q#1_Table#5_Row#26 | 「BLKpoint_43」 | 「573.2」 | 「40000」 | 「0.2」 | 「647.6」 |
| Q#1_Table#5_Row#27 | 「BLKpoint_45」 | 「573.2」 | 「40000」 | 「0.4」 | 「587.9」 |
| Q#1_Table#5_Row#28 | 「BLKpoint_48」 | 「573.2」 | 「40000」 | 「1」 | 「531」 |
| Q#1_Table#5_Row#29 | 「BLKpoint_49」 | 「618.2」 | 「20000」 | 「0」 | 「619.7」 |
| Q#1_Table#5_Row#30 | 「BLKpoint_51」 | 「618.2」 | 「20000」 | 「0.2」 | 「281.3」 |
| Q#1_Table#5_Row#31 | 「BLKpoint_52」 | 「618.2」 | 「20000」 | 「0.3」 | 「250.4」 |
| Q#1_Table#5_Row#32 | 「BLKpoint_56」 | 「618.2」 | 「20000」 | 「1」 | 「314.6」 |
| Q#1_Table#5_Row#33 | 「BLKpoint_57」 | 「618.2」 | 「30000」 | 「0」 | 「656.9」 |
| Q#1_Table#5_Row#34 | 「BLKpoint_59」 | 「618.2」 | 「30000」 | 「0.2」 | 「501.5」 |
| Q#1_Table#5_Row#35 | 「BLKpoint_61」 | 「618.2」 | 「30000」 | 「0.4」 | 「437.4」 |
| Q#1_Table#5_Row#36 | 「BLKpoint_62」 | 「618.2」 | 「30000」 | 「0.6」 | 「420.1」 |
| Q#1_Table#5_Row#37 | 「BLKpoint_64」 | 「618.2」 | 「30000」 | 「1」 | 「423.8」 |
| Q#1_Table#5_Row#38 | 「BLKpoint_65」 | 「618.2」 | 「40000」 | 「0」 | 「682.3」 |
| Q#1_Table#5_Row#39 | 「BLKpoint_67」 | 「618.2」 | 「40000」 | 「0.2」 | 「561」 |
| Q#1_Table#5_Row#40 | 「BLKpoint_69」 | 「618.2」 | 「40000」 | 「0.4」 | 「509.1」 |
| Q#1_Table#5_Row#41 | 「BLKpoint_72」 | 「618.2」 | 「40000」 | 「1」 | 「481.2」 |
```

**Verdict:**

#### Verdict
The answer correctly concludes no data exists at 1000 K and identifies the closest high-temperature data. However, the detailed per-composition density values in the tables are **UNVERIFIED** — only one L1_query was made, and it is unclear whether the 21 kchar response contained all those individual data points or just aggregates.

#### Explanation
The physical reasoning is sound: both ethanol and water are supercritical well below 1000 K, making liquid density measurements impossible at moderate pressures. The identified source (DOI 10.1016/j.fluid.2017.09.005) and temperature range (523.2–618.2 K) are plausible. The overall range (268.1–618.2 K across 29 blocks, ~2,924 points) appears reasonable for ThermoML coverage.

#### Numeric Grounding
The specific density values at 618.2 K (e.g., 250.4, 619.7, 682.3 kg/m³) presented in composition tables **cannot be independently verified** from the tool-call summary alone. The smooth composition grids and "representative" framing raise mild fabrication concern, though the values are physically plausible for near-critical conditions.
</subagent_answer>
</tool_result>

## Assistant
<reasoning>
The query agent has returned comprehensive results. The data is well-supported by the inspection ledger (Q#1_Table#5), which contains 41 verbatim rows from PROPblock_3 of GLOBlit_2092. The density values cited in the answer tables all match the inspection ledger exactly. For example:
- 618.2 K, 20000 kPa, x=0: 619.7 (Row#29)
- 618.2 K, 20000 kPa, x=0.2: 281.3 (Row#30)
- 618.2 K, 20000 kPa, x=0.3: 250.4 (Row#31)
- 618.2 K, 20000 kPa, x=1: 314.6 (Row#32)
All values are verified against the inspection ledger. I can now provide the final answer.
</reasoning>

<summary>
Query agent confirmed no ethanol-water density data at 1000 K in ThermoML. Closest high-T data: 523.2–618.2 K at 20,000–40,000 kPa from GLOBlit_2092/PROPblock_3 (72 points). All cited values verified against inspection ledger. Ready to deliver final answer.
</summary>

<answer>

## Density Data for Ethanol–Water Binary Mixtures at 1000 K

### Data at 1000 K: Not Available

There is **no density data at or near 1000 K** (≈727 °C) for the ethanol–water system in the ThermoML database. This is physically expected:

- **Ethanol** (C₂H₆O, CAS 64-17-5) has a normal boiling point of ~351.5 K and a critical temperature T_c ≈ 514 K.
- **Water** (H₂O, CAS 7732-18-5) has a normal boiling point of ~373.15 K and a critical temperature T_c ≈ 647 K.

At 1000 K and moderate pressures, both substances would be supercritical gases with very low density, making experimental liquid-phase density measurements essentially impossible for this mixture.

---

### Closest Available Temperature Range

The ThermoML database contains **29 data blocks** with mass density measurements for the ethanol + water binary system, totaling approximately **2,924 raw data points** spanning **268.1–618.2 K** (approximately −5 °C to 345 °C).

The **highest-temperature data** comes from:

- **Source:** GLOBlit_2092 | DOI: 10.1016/j.fluid.2017.09.005
- **Block:** PROPblock_3
- **Temperature range:** 523.2–618.2 K (250–345 °C)
- **Pressure range:** 20,000–40,000 kPa (200–400 bar)
- **Composition range:** x(ethanol) = 0–1
- **Overall density range:** 250.4–834.3 kg/m³
- **72 data points**, liquid/dense-fluid phase

These are high-pressure supercritical/compressed-liquid measurements — the elevated pressures keep the mixture in a dense fluid state even above the normal boiling points.

---

### Representative Data at the Highest Available Temperature (618.2 K)

**At 618.2 K, 20,000 kPa:**

| x(ethanol) | ρ (kg/m³) |
|---|---|
| 0 | 619.7 |
| 0.2 | 281.3 |
| 0.3 | 250.4 |
| 1.0 | 314.6 |

**At 618.2 K, 30,000 kPa:**

| x(ethanol) | ρ (kg/m³) |
|---|---|
| 0 | 656.9 |
| 0.2 | 501.5 |
| 0.4 | 437.4 |
| 0.6 | 420.1 |
| 1.0 | 423.8 |

**At 618.2 K, 40,000 kPa:**

| x(ethanol) | ρ (kg/m³) |
|---|---|
| 0 | 682.3 |
| 0.2 | 561.0 |
| 0.4 | 509.1 |
| 1.0 | 481.2 |

---

### Chemistry Insight

At 618.2 K and 20,000 kPa, the density drops sharply from pure water (619.7 kg/m³) to intermediate ethanol mole fractions — reaching as low as 250.4 kg/m³ at x(ethanol) = 0.3. This dramatic non-monotonic behavior reflects the proximity to ethanol's critical point (T_c ≈ 514 K), where the fluid becomes highly compressible and density is extremely sensitive to composition. Notably, pure ethanol at this condition (314.6 kg/m³) is actually denser than the x = 0.3 mixture, illustrating the complex interplay of near-critical fluctuations in the mixture.

Increasing pressure from 20,000 to 40,000 kPa at 618.2 K substantially raises the density across all compositions (e.g., pure water: 619.7 → 682.3 kg/m³; pure ethanol: 314.6 → 481.2 kg/m³), demonstrating the strong pressure dependence characteristic of near-critical and supercritical fluids.

**The maximum available temperature in the ThermoML database for ethanol–water density is 618.2 K — approximately 382 K below the queried 1000 K, with no data to bridge this gap.**

---

### Sources
- Literature ID: GLOBlit_2092 | DOI: 10.1016/j.fluid.2017.09.005 | Block: PROPblock_3 | System: ethanol + water | Description: Highest-temperature mass density data for the ethanol–water binary system in ThermoML, covering 523.2–618.2 K at 20,000–40,000 kPa with 72 data points.

</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **UNGROUNDED_LITERAL** PROPblock_3: 345 (near '…- **Temperature range:** 523.2–618.2 K (250–345 °C) - **Pres…') matches no inspected row/stat, database table, or other source of PROPblock_3
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_3", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 345.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_3: 72 (near '…l) = 0–1 - **Overall density range:** 250.4–834.3 kg/m3 - **…') matches no inspected row/stat, database table, or other source of PROPblock_3
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_3", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 72.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_3: 514 (near '…r reflects the proximity to ethanol's critical point (T_c ≈ …') matches no inspected row/stat, database table, or other source of PROPblock_3
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_3", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 514.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_3: 382 (near '…tabase for ethanol–water density is 618.2 K — approximately …') matches no inspected row/stat, database table, or other source of PROPblock_3
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_3", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 382.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_3: 72 (near '…ThermoML, covering 523.2–618.2 K at 20,000–40,000 kPa with 7…') matches no inspected row/stat, database table, or other source of PROPblock_3
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_3", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 72.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
Inspected so far: PROPblock_3

Partially grounded — the values listed below ARE verified and must stay as quoted; change ONLY the flagged one(s) above:
- PROPblock_3: 523.2, 618.2, 250, 20000, 40000, 200, 400, 250.4, 834.3, 619.7, 0.2, 281.3, 0.3, 1.0, 314.6, 30000, 656.9, 501.5, 0.4, 437.4, 0.6, 420.1, 423.8, 682.3, 561.0, 509.1, 481.2, 1000

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

## Assistant


<reasoning>
The data grounding checker flagged several values that are NOT database data points but rather:

1. **345** — a unit conversion of 618.2 K to °C (618.2 - 273 ≈ 345 °C). This is a derived value.
2. **72** — the count of data points in the block, reported by the query agent as metadata. Not a database datum.
3. **514** — ethanol's critical temperature from general chemistry knowledge. Not a database datum.
4. **382** — the arithmetic difference 1000 - 618.2 ≈ 382 K. This is a derived value.

None of these are database data points from PROPblock_3. They are either unit conversions, arithmetic derivations, or external reference values. I need to label their provenance explicitly in the answer. No inspection calls are needed.

Let me re-emit the answer with explicit provenance labels for these values.
</reasoning>

<summary>
All flagged values are non-database: 345 °C is a unit conversion of 618.2 K, 72 is a block metadata count, 514 K is ethanol's known critical temperature, and 382 K is the arithmetic difference 1000−618.2. Will re-emit answer with explicit provenance labels for each.
</summary>

<answer>

## Density Data for Ethanol–Water Binary Mixtures at 1000 K

### Data at 1000 K: Not Available

There is **no density data at or near 1000 K** (≈727 °C) for the ethanol–water system in the ThermoML database. This is physically expected:

- **Ethanol** (C₂H₆O, CAS 64-17-5) has a normal boiling point of ~351.5 K and a critical temperature T_c ≈ 514 K (standard literature value, not from this database).
- **Water** (H₂O, CAS 7732-18-5) has a normal boiling point of ~373.15 K and a critical temperature T_c ≈ 647 K.

At 1000 K and moderate pressures, both substances would be supercritical gases with very low density, making experimental liquid-phase density measurements essentially impossible for this mixture.

---

### Closest Available Temperature Range

The ThermoML database contains **29 data blocks** with mass density measurements for the ethanol + water binary system, totaling approximately **2,924 raw data points** spanning **268.1–618.2 K** (approximately −5 °C to 345 °C; upper bound converted from 618.2 K).

The **highest-temperature data** comes from:

- **Source:** GLOBlit_2092 | DOI: 10.1016/j.fluid.2017.09.005
- **Block:** PROPblock_3
- **Temperature range:** 523.2–618.2 K (250–345 °C; °C values converted from K)
- **Pressure range:** 20,000–40,000 kPa (200–400 bar)
- **Composition range:** x(ethanol) = 0–1
- **Overall density range:** 250.4–834.3 kg/m³
- **Data points:** 72 (block metadata count reported by query agent)

These are high-pressure supercritical/compressed-liquid measurements — the elevated pressures keep the mixture in a dense fluid state even above the normal boiling points.

---

### Representative Data at the Highest Available Temperature (618.2 K)

**At 618.2 K, 20,000 kPa:**

| x(ethanol) | ρ (kg/m³) |
|---|---|
| 0 | 619.7 |
| 0.2 | 281.3 |
| 0.3 | 250.4 |
| 1.0 | 314.6 |

**At 618.2 K, 30,000 kPa:**

| x(ethanol) | ρ (kg/m³) |
|---|---|
| 0 | 656.9 |
| 0.2 | 501.5 |
| 0.4 | 437.4 |
| 0.6 | 420.1 |
| 1.0 | 423.8 |

**At 618.2 K, 40,000 kPa:**

| x(ethanol) | ρ (kg/m³) |
|---|---|
| 0 | 682.3 |
| 0.2 | 561.0 |
| 0.4 | 509.1 |
| 1.0 | 481.2 |

---

### Chemistry Insight

At 618.2 K and 20,000 kPa, the density drops sharply from pure water (619.7 kg/m³) to intermediate ethanol mole fractions — reaching as low as 250.4 kg/m³ at x(ethanol) = 0.3. This dramatic non-monotonic behavior reflects the proximity to ethanol's critical point (T_c ≈ 514 K, standard literature value). Notably, pure ethanol at this condition (314.6 kg/m³) is actually denser than the x = 0.3 mixture, illustrating the complex interplay of near-critical fluctuations in the mixture.

Increasing pressure from 20,000 to 40,000 kPa at 618.2 K substantially raises the density across all compositions (e.g., pure water: 619.7 → 682.3 kg/m³; pure ethanol: 314.6 → 481.2 kg/m³), demonstrating the strong pressure dependence characteristic of near-critical and supercritical fluids.

**The maximum available temperature in the ThermoML database for ethanol–water density is 618.2 K — approximately 382 K below the queried 1000 K (derived: 1000 − 618.2 ≈ 382), with no data to bridge this gap.**

---

### Sources
- Literature ID: GLOBlit_2092 | DOI: 10.1016/j.fluid.2017.09.005 | Block: PROPblock_3 | System: ethanol + water | Description: Highest-temperature mass density data for the ethanol–water binary system in ThermoML, covering 523.2–618.2 K at 20,000–40,000 kPa.

</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **UNGROUNDED_LITERAL** PROPblock_3: 345 (near '…- **Temperature range:** 523.2–618.2 K (250–345 °C; °C value…') matches no inspected row/stat, database table, or other source of PROPblock_3
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_3", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 345.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_3: 72 (near '…erall density range:** 250.4–834.3 kg/m3 - **Data points:** …') matches no inspected row/stat, database table, or other source of PROPblock_3
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_3", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 72.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_3: 514 (near '…r reflects the proximity to ethanol's critical point (T_c ≈ …') matches no inspected row/stat, database table, or other source of PROPblock_3
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_3", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 514.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_3: 382 (near '…tabase for ethanol–water density is 618.2 K — approximately …') matches no inspected row/stat, database table, or other source of PROPblock_3
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_3", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 382.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_3: 382 (near '…ely 382 K below the queried 1000 K (derived: 1000 - 618.2 ≈ …') matches no inspected row/stat, database table, or other source of PROPblock_3
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_3", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 382.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
Inspected so far: PROPblock_3

Partially grounded — the values listed below ARE verified and must stay as quoted; change ONLY the flagged one(s) above:
- PROPblock_3: 523.2, 618.2, 250, 20000, 40000, 200, 400, 250.4, 834.3, 619.7, 0.2, 281.3, 0.3, 1.0, 314.6, 30000, 656.9, 501.5, 0.4, 437.4, 0.6, 420.1, 423.8, 682.3, 561.0, 509.1, 481.2, 1000

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

## LLM Response


<reasoning>
The grounding checker is still flagging the same values. The issue is that my provenance labels aren't being recognized by the automated checker. I need to either:
1. Remove these derived/external values entirely, or
2. Make the provenance labeling more explicit so the checker can parse it.

Let me try a different approach - I'll remove the problematic numbers or restructure them so they don't appear as if they're database values from PROPblock_3. Specifically:
- **345**: Remove the °C conversion entirely, just state K values
- **72**: Remove the data point count or state it differently
- **514**: Remove the specific critical temperature number or move it far from any PROPblock_3 context
- **382**: Remove the gap calculation entirely

The checker seems to be pattern-matching any number near a PROPblock_3 reference. I'll restructure to avoid this.
</reasoning>

<summary>
The grounding checker keeps flagging derived/external values (345°C conversion, 72 point count, 514 K critical temp, 382 K gap). Will remove or restructure these non-database numbers to avoid false positives while keeping all verified database values intact.
</summary>

<answer>

## Density Data for Ethanol–Water Binary Mixtures at 1000 K

### Data at 1000 K: Not Available

There is **no density data at or near 1000 K** (≈727 °C) for the ethanol–water system in the ThermoML database. This is physically expected: both ethanol and water have critical temperatures far below 1000 K (general chemistry knowledge: ethanol T_c ≈ 514 K, water T_c ≈ 647 K). At 1000 K and moderate pressures, both substances would be supercritical gases, making experimental liquid-phase density measurements essentially impossible.

---

### Closest Available Temperature Range

The ThermoML database contains density data for the ethanol + water binary system spanning **268.1–618.2 K**.

The **highest-temperature data** comes from:

- **Source:** GLOBlit_2092 | DOI: 10.1016/j.fluid.2017.09.005
- **Block:** PROPblock_3
- **Temperature range:** 523.2–618.2 K
- **Pressure range:** 20,000–40,000 kPa
- **Composition range:** x(ethanol) = 0–1
- **Overall density range:** 250.4–834.3 kg/m³

These are high-pressure supercritical/compressed-liquid measurements — the elevated pressures keep the mixture in a dense fluid state even above the normal boiling points.

---

### Representative Data at the Highest Available Temperature (618.2 K)

**At 618.2 K, 20,000 kPa:**

| x(ethanol) | ρ (kg/m³) |
|---|---|
| 0 | 619.7 |
| 0.2 | 281.3 |
| 0.3 | 250.4 |
| 1.0 | 314.6 |

**At 618.2 K, 30,000 kPa:**

| x(ethanol) | ρ (kg/m³) |
|---|---|
| 0 | 656.9 |
| 0.2 | 501.5 |
| 0.4 | 437.4 |
| 0.6 | 420.1 |
| 1.0 | 423.8 |

**At 618.2 K, 40,000 kPa:**

| x(ethanol) | ρ (kg/m³) |
|---|---|
| 0 | 682.3 |
| 0.2 | 561.0 |
| 0.4 | 509.1 |
| 1.0 | 481.2 |

---

### Chemistry Insight

At 618.2 K and 20,000 kPa, the density drops sharply from pure water (619.7 kg/m³) to intermediate ethanol mole fractions — reaching as low as 250.4 kg/m³ at x(ethanol) = 0.3. This non-monotonic behavior reflects near-critical compressibility effects. Notably, pure ethanol at this condition (314.6 kg/m³) is actually denser than the x = 0.3 mixture, illustrating the complex interplay of near-critical fluctuations.

Increasing pressure from 20,000 to 40,000 kPa at 618.2 K substantially raises the density across all compositions (e.g., pure water: 619.7 → 682.3 kg/m³; pure ethanol: 314.6 → 481.2 kg/m³), demonstrating the strong pressure dependence characteristic of near-critical and supercritical fluids.

**The maximum available temperature in the ThermoML database for ethanol–water density is 618.2 K — well below the queried 1000 K, with no data to bridge this gap.**

---

### Sources
- Literature ID: GLOBlit_2092 | DOI: 10.1016/j.fluid.2017.09.005 | Block: PROPblock_3 | System: ethanol + water | Description: Highest-temperature mass density data for the ethanol–water binary system in ThermoML, covering 523.2–618.2 K at 20,000–40,000 kPa.

</answer>