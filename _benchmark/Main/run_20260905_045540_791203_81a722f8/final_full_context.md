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
**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_045540_791203_81a722f8`

### History
- [query:Q1] "Find viscosity data for isopropanol (2-propanol) mixed with water at room temper" (144s, 2 iters, validation=PASS verdict=## Verdict
The answer identifi)
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK

### Query Agent Results

#### Q1
**Q1** — confidence: high · validation: PASS

**Answer:**

#### Viscosity Data for Isopropanol (2-Propanol) + Water Binary Mixtures at Room Temperature

##### Source

**DOI:** 10.1016/j.jct.2019.105880  
**Data block:** PROPblock_12  
**Property:** Dynamic viscosity (Pa·s), measured by falling/rolling sphere viscometry, liquid phase, at 100 kPa.  
**System:** Binary mixture of propan-2-ol (2-propanol / isopropanol) + water.

**Composition range covered:** Mass fraction of propan-2-ol from 0.1 to 0.3  
**Full block temperature range:** 288.15–303.15 K (12 data points total)

---

##### Data Points in the 293–298 K Window

**WM_Q#1_Table#1_(Main_Q#1_Answer):**

| *row_id* | *T (K)* | *w (propan-2-ol)* | *Dynamic Viscosity (Pa·s)* |
|---|---|---|---|
| WM_Q#1_Table#1_Row#1 | 「293.15」 | 「0.1」 | 「0.001633」 |
| WM_Q#1_Table#1_Row#2 | 「293.15」 | 「0.2」 | 「0.002485」 |
| WM_Q#1_Table#1_Row#3 | 「293.15」 | 「0.3」 | 「0.003172」 |
| WM_Q#1_Table#1_Row#4 | 「298.15」 | 「0.1」 | 「0.001395」 |
| WM_Q#1_Table#1_Row#5 | 「298.15」 | 「0.2」 | 「0.002045」 |
| WM_Q#1_Table#1_Row#6 | 「298.15」 | 「0.3」 | 「0.002555」 |

All measurements were made at a pressure of 100.0 kPa in the liquid phase.

---

##### Key Observations

1. **Viscosity increases with isopropanol content** in the 0.1–0.3 mass-fraction range at both temperatures. For example, at 293.15 K the viscosity nearly doubles from 0.001633 Pa·s (w = 0.1) to 0.003172 Pa·s (w = 0.3). This trend is consistent with the well-known viscosity maximum of the isopropanol–water system, which occurs at higher alcohol concentrations (typically around 0.6–0.7 mass fraction). In this composition range, the extensive hydrogen-bonding network between water and isopropanol molecules progressively increases internal friction.

2. **Viscosity decreases with increasing temperature**, as expected from the Arrhenius-type temperature dependence of liquid viscosity. At w = 0.3, the viscosity drops from 0.003172 Pa·s at 293.15 K to 0.002555 Pa·s at 298.15 K — a reduction of about 19% for just a 5 K increase.

3. **Full data block** extends from 288.15 K to 303.15 K, with viscosities spanning 0.001208–0.004014 Pa·s across all compositions and temperatures.

4. **No kinematic viscosity data** were found in the ThermoML database for this binary system in the requested temperature range. Only dynamic viscosity data are available from this source.

**Core claims:**
- Dynamic viscosity data for the binary mixture of propan-2-ol (isopropanol) + water were found in ThermoML (DOI: 10.1016/j.jct.2019.05880, PROPblock_12), covering mass fractions of propan-2-ol from 0.1 to 0.3 at 100 kPa, with six data points falling within the 293–298 K window.
- At 293.15 K and 100 kPa, the dynamic viscosity increases from 0.001633 Pa·s at w = 0.1 to 0.003172 Pa·s at w = 0.3; at 298.15 K it increases from 0.001395 Pa·s at w = 0.1 to 0.002555 Pa·s at w = 0.3.
- Viscosity decreases with increasing temperature: at w = 0.3, it drops from 0.003172 Pa·s at 293.15 K to 0.002555 Pa·s at 298.15 K.
- No kinematic viscosity data were found in the ThermoML database for this binary system in the requested temperature range; only dynamic viscosity data are available from this source.

**Sources:**

**WM_Q#1_Table#2_(Main_Q#1_Sources):**

| *row_id* | *lit_num_id* | *block* | *doi* | *BLKsubsys_id* | *description* |
|---|---|---|---|---|---|
| WM_Q#1_Table#2_Row#1 | 「GLOBlit_5585」 | 「PROPblock_12」 | 「10.1016/j.jct.2019.105880」 | 「—」 | 「This block provides dynamic viscosity data for the binary system propan-2-ol + water measured by falling/rolling sphere viscometry at 100 kPa. The temperature range 288.15–303.15 K covers the requested 293–298 K window, and the mass fraction range 0.1–0.3 with 12 data points directly supports the six viscosity values reported in the answer.」 |

*Not stored here: 1 verbatim data_inspections table(s); 3 id_catalog_snapshot row(s) (catalog is merged separately). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.

</memory>

## User
What viscosity data are available for rubbing alcohol mixed with water at room temperature?

## Assistant
<summary>Searching for viscosity data for isopropanol (rubbing alcohol) + water binary mixtures at room temperature (~293-298 K). Will query the database for available experimental data.</summary>
<tool_call>run_query_agent(question=Find viscosity da…, context=Rubbing alcohol i…)</tool_call>

## User
<tool_result>
(validation blocked run_query_agent earlier — corrected)
</tool_result>

## Assistant
<summary>Fixing tool call syntax to search for viscosity data for isopropanol (rubbing alcohol) + water mixtures at room temperature.</summary>
<tool_call>run_query_agent(question=Find viscosity da…, context=Rubbing alcohol i…)</tool_call>

## User
<tool_result>
<subagent_answer>
### Q#1 — run_query_agent return

**Status:** 2 iterations · 143.6s · 1 tool call(s) · agent=query
**Question:** Find viscosity data for isopropanol (2-propanol) mixed with water at room temperature (around 293-298 K). Rubbing alcohol is isopropanol.
**Session:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_045540_791203_81a722f8\query_runs\run_10`

**Answer:**

#### Viscosity Data for Isopropanol (2-Propanol) + Water Binary Mixtures at Room Temperature

##### Source

**DOI:** 10.1016/j.jct.2019.105880  
**Data block:** PROPblock_12  
**Property:** Dynamic viscosity (Pa·s), measured by falling/rolling sphere viscometry, liquid phase, at 100 kPa.  
**System:** Binary mixture of propan-2-ol (2-propanol / isopropanol) + water.

**Composition range covered:** Mass fraction of propan-2-ol from 0.1 to 0.3  
**Full block temperature range:** 288.15–303.15 K (12 data points total)

---

##### Data Points in the 293–298 K Window

**Q#1_Table#1_(Main_Q#1_Answer):**

| *row_id* | *T (K)* | *w (propan-2-ol)* | *Dynamic Viscosity (Pa·s)* |
|---|---|---|---|
| Q#1_Table#1_Row#1 | 「293.15」 | 「0.1」 | 「0.001633」 |
| Q#1_Table#1_Row#2 | 「293.15」 | 「0.2」 | 「0.002485」 |
| Q#1_Table#1_Row#3 | 「293.15」 | 「0.3」 | 「0.003172」 |
| Q#1_Table#1_Row#4 | 「298.15」 | 「0.1」 | 「0.001395」 |
| Q#1_Table#1_Row#5 | 「298.15」 | 「0.2」 | 「0.002045」 |
| Q#1_Table#1_Row#6 | 「298.15」 | 「0.3」 | 「0.002555」 |

All measurements were made at a pressure of 100.0 kPa in the liquid phase.

---

##### Key Observations

1. **Viscosity increases with isopropanol content** in the 0.1–0.3 mass-fraction range at both temperatures. For example, at 293.15 K the viscosity nearly doubles from 0.001633 Pa·s (w = 0.1) to 0.003172 Pa·s (w = 0.3). This trend is consistent with the well-known viscosity maximum of the isopropanol–water system, which occurs at higher alcohol concentrations (typically around 0.6–0.7 mass fraction). In this composition range, the extensive hydrogen-bonding network between water and isopropanol molecules progressively increases internal friction.

2. **Viscosity decreases with increasing temperature**, as expected from the Arrhenius-type temperature dependence of liquid viscosity. At w = 0.3, the viscosity drops from 0.003172 Pa·s at 293.15 K to 0.002555 Pa·s at 298.15 K — a reduction of about 19% for just a 5 K increase.

3. **Full data block** extends from 288.15 K to 303.15 K, with viscosities spanning 0.001208–0.004014 Pa·s across all compositions and temperatures.

4. **No kinematic viscosity data** were found in the ThermoML database for this binary system in the requested temperature range. Only dynamic viscosity data are available from this source.

**Core claims:**
- Dynamic viscosity data for the binary mixture of propan-2-ol (isopropanol) + water were found in ThermoML (DOI: 10.1016/j.jct.2019.05880, PROPblock_12), covering mass fractions of propan-2-ol from 0.1 to 0.3 at 100 kPa, with six data points falling within the 293–298 K window.
- At 293.15 K and 100 kPa, the dynamic viscosity increases from 0.001633 Pa·s at w = 0.1 to 0.003172 Pa·s at w = 0.3; at 298.15 K it increases from 0.001395 Pa·s at w = 0.1 to 0.002555 Pa·s at w = 0.3.
- Viscosity decreases with increasing temperature: at w = 0.3, it drops from 0.003172 Pa·s at 293.15 K to 0.002555 Pa·s at 298.15 K.
- No kinematic viscosity data were found in the ThermoML database for this binary system in the requested temperature range; only dynamic viscosity data are available from this source.

**Confidence:** high

**Sources:**

**Q#1_Table#2_(Main_Q#1_Sources):**

| *row_id* | *lit_num_id* | *block* | *doi* | *BLKsubsys_id* | *description* |
|---|---|---|---|---|---|
| Q#1_Table#2_Row#1 | 「GLOBlit_5585」 | 「PROPblock_12」 | 「10.1016/j.jct.2019.105880」 | 「—」 | 「This block provides dynamic viscosity data for the binary system propan-2-ol + water measured by falling/rolling sphere viscometry at 100 kPa. The temperature range 288.15–303.15 K covers the requested 293–298 K window, and the mass fraction range 0.1–0.3 with 12 data points directly supports the six viscosity values reported in the answer.」 |

**ID catalog snapshot:**

| *type* | *global_id* | *registry_id* | *name* |
|---|---|---|---|
| comp | 「GLOBcomp_6」 | 「propan-2-ol」 | 「propan-2-ol」 |
| comp | 「GLOBcomp_1」 | 「water」 | 「water」 |
| lit | 「GLOBlit_5585」 | 「2019-meh-haj-0」 | 「10.1016/j.jct.2019.105880」 |

**Follow-up suggestions:**
- Search for additional viscosity data at higher isopropanol mass fractions (0.4–0.9) to capture the well-known viscosity maximum near w ≈ 0.6–0.7 in the isopropanol–water system.
- Look for kinematic viscosity or density data for the same system and temperature range to enable cross-checking between dynamic and kinematic viscosity.
- Explore other DOIs in ThermoML for isopropanol–water viscosity data at temperatures outside the 288–303 K range for broader temperature-dependence modeling.

#### Data inspections — verbatim ledger

```ledger
**Q#1_Table#3_(Main_Q#1_INSP):**
lit_num_id: GLOBlit_5585 | doi: 10.1016/j.jct.2019.105880 | block: PROPblock_12
table_mode: complete | inspection_id: INSP_5c8cad6c2b0f | rows_shown: 6

| *row_id* | *BLKpoint_id* | *temperature_k* | *mass_fraction_<propan-2-ol>* | *pressure_kpa* | *viscosity_pa_s* |
|---|---|---|---|---|---|
| Q#1_Table#3_Row#1 | 「BLKpoint_4」 | 「293.15」 | 「0.1」 | 「100.0」 | 「0.001633」 |
| Q#1_Table#3_Row#2 | 「BLKpoint_5」 | 「293.15」 | 「0.2」 | 「100.0」 | 「0.002485」 |
| Q#1_Table#3_Row#3 | 「BLKpoint_6」 | 「293.15」 | 「0.3」 | 「100.0」 | 「0.003172」 |
| Q#1_Table#3_Row#4 | 「BLKpoint_7」 | 「298.15」 | 「0.1」 | 「100.0」 | 「0.001395」 |
| Q#1_Table#3_Row#5 | 「BLKpoint_8」 | 「298.15」 | 「0.2」 | 「100.0」 | 「0.002045」 |
| Q#1_Table#3_Row#6 | 「BLKpoint_9」 | 「298.15」 | 「0.3」 | 「100.0」 | 「0.002555」 |
```

**Verdict:**

#### Verdict
The answer identifies one relevant source, but the six individual data points (specific viscosity values at each composition and temperature) are **UNVERIFIED** — the tool call returned a single text block, and it is unclear whether point-by-point numeric values were explicitly present or interpolated/fabricated. The smooth composition grid (w = 0.1, 0.2, 0.3 at exactly two temperatures) is a suspicious pattern warranting caution.

#### Explanation
The DOI and general description (dynamic viscosity, isopropanol+water, 288–303 K) appear plausible. However, the limited composition range (0.1–0.3 mass fraction) misses the well-known viscosity maximum near w ≈ 0.6–0.7, which the answer acknowledges. Only one source was found; additional ThermoML entries likely exist for this extensively studied system, suggesting incomplete database coverage.

#### Flags
- Individual numeric viscosity values: **UNVERIFIED** against tool output.
- Evenly spaced compositions suggest possible fabrication.
- Narrow composition range limits practical utility.
</subagent_answer>
</tool_result>

## Assistant
<reasoning>
The query agent returned the same data as before from working memory. The data comes from PROPblock_12 in GLOBlit_5585 (DOI: 10.1016/j.jct.2019.105880). The inspection ledger confirms the six data points are verbatim from the database. The verdict flags about "UNVERIFIED" and "suspicious pattern" are overly cautious — the inspection table (INSP_5c8cad6c2b0f) confirms each value at the BLKpoint level, so these are verified. The evenly spaced compositions (0.1, 0.2, 0.3) are simply how the experimenters chose their samples, which is completely normal in experimental work.

I have all the data I need to answer the user's question. "Rubbing alcohol" is commonly isopropanol (2-propanol), so the data applies directly.
</reasoning>

<summary>
Found dynamic viscosity data for isopropanol (rubbing alcohol) + water from ThermoML. Six data points at 293.15 K and 298.15 K, mass fractions 0.1–0.3, from GLOBlit_5585 / PROPblock_12 (DOI: 10.1016/j.jct.2019.105880). Data verified via block-level inspection. Ready to deliver final answer.
</summary>

<answer>
## Viscosity Data for Rubbing Alcohol (Isopropanol) + Water at Room Temperature

"Rubbing alcohol" is isopropanol (propan-2-ol, 2-propanol). The ThermoML database contains **dynamic viscosity** measurements for the binary mixture of isopropanol + water near room temperature.

### Source

- **Literature ID:** GLOBlit_5585
- **DOI:** 10.1016/j.jct.2019.105880
- **Data block:** PROPblock_12
- **Method:** Falling/rolling sphere viscometry
- **Phase:** Liquid
- **Pressure:** 100 kPa
- **Full temperature range in block:** 288.15–303.15 K (12 data points total)
- **Composition range:** Mass fraction of isopropanol from 0.1 to 0.3

### Data at Room Temperature (293–298 K)

Six data points fall within the standard "room temperature" window:

| Temperature (K) | Mass fraction of isopropanol | Dynamic Viscosity (Pa·s) |
|:---:|:---:|:---:|
| 293.15 | 0.1 | 0.001633 |
| 293.15 | 0.2 | 0.002485 |
| 293.15 | 0.3 | 0.003172 |
| 298.15 | 0.1 | 0.001395 |
| 298.15 | 0.2 | 0.002045 |
| 298.15 | 0.3 | 0.002555 |

All measurements at 100.0 kPa in the liquid phase.

### Key Observations

1. **Viscosity increases with isopropanol content** across the 0.1–0.3 mass-fraction range. At 293.15 K, the viscosity nearly doubles from 0.001633 Pa·s (w = 0.1) to 0.003172 Pa·s (w = 0.3). This reflects the strong hydrogen-bonding interactions between isopropanol and water molecules, which progressively increase internal friction as more alcohol is added. The well-known viscosity maximum for this system occurs at higher alcohol concentrations (around w ≈ 0.6–0.7), so the data here capture the rising portion of that curve.

2. **Viscosity decreases with increasing temperature**, consistent with the typical Arrhenius-type behavior of liquid viscosity. For example, at w = 0.3, the viscosity drops from 0.003172 Pa·s at 293.15 K to 0.002555 Pa·s at 298.15 K — a reduction of roughly 19% for just a 5 K increase.

3. **Only dynamic viscosity** (not kinematic viscosity) was found in ThermoML for this system in this temperature range.

4. **Composition coverage is limited** to mass fractions 0.1–0.3 in this source. The full block spans 288.15–303.15 K with viscosities ranging from 0.001208 to 0.004014 Pa·s across all compositions and temperatures.

### Sources
- Literature ID: GLOBlit_5585 | DOI: 10.1016/j.jct.2019.105880 | Block: PROPblock_12 | System: propan-2-ol (isopropanol) + water
</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **UNINSPECTED_VALUE** PROPblock_12: 288.15 exists in PROPblock_12's database table but was never shown in an inspection of this run
  fix (required — this value IS in the cited block's database table): `inspect_block_table(block_number="GLOBlit_5585::PROPblock_12", nearest={"column": "temperature_k", "value": 288.15})`
- **UNINSPECTED_VALUE** PROPblock_12: 303.15 exists in PROPblock_12's database table but was never shown in an inspection of this run
  fix (required — this value IS in the cited block's database table): `inspect_block_table(block_number="GLOBlit_5585::PROPblock_12", nearest={"column": "temperature_k", "value": 303.15})`
- **UNGROUNDED_LITERAL** PROPblock_12: 0.6 (near '…system occurs at higher alcohol concentrations (around w ≈ 0…') matches no inspected row/stat, database table, or other source of PROPblock_12
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_12", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 0.6})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_12: 0.7 (near '…tem occurs at higher alcohol concentrations (around w ≈ 0.6–…') matches no inspected row/stat, database table, or other source of PROPblock_12
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_12", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 0.7})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNINSPECTED_VALUE** PROPblock_12: 288.15 exists in PROPblock_12's database table but was never shown in an inspection of this run
  fix (required — this value IS in the cited block's database table): `inspect_block_table(block_number="GLOBlit_5585::PROPblock_12", nearest={"column": "temperature_k", "value": 288.15})`
- **UNINSPECTED_VALUE** PROPblock_12: 303.15 exists in PROPblock_12's database table but was never shown in an inspection of this run
  fix (required — this value IS in the cited block's database table): `inspect_block_table(block_number="GLOBlit_5585::PROPblock_12", nearest={"column": "temperature_k", "value": 303.15})`
- **UNINSPECTED_VALUE** PROPblock_12: 0.001208 exists in PROPblock_12's database table but was never shown in an inspection of this run
  fix (required — this value IS in the cited block's database table): `inspect_block_table(block_number="GLOBlit_5585::PROPblock_12", nearest={"column": "viscosity_pa_s", "value": 0.001208})`
- **UNINSPECTED_VALUE** PROPblock_12: 0.004014 exists in PROPblock_12's database table but was never shown in an inspection of this run
  fix (required — this value IS in the cited block's database table): `inspect_block_table(block_number="GLOBlit_5585::PROPblock_12", nearest={"column": "viscosity_pa_s", "value": 0.004014})`
Inspected so far: PROPblock_12

Partially grounded — the values listed below ARE verified and must stay as quoted; change ONLY the flagged one(s) above:
- PROPblock_12: 100, 0.1, 0.3, 293, 298, 293.15, 0.001633, 0.2, 0.002485, 0.003172, 298.15, 0.001395, 0.002045, 0.002555, 100.0

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

## Assistant
(syntax-rejected turn — malformed tool calls never executed; corrected on a later turn. Full detail in the run log.)

## User
(validation fired earlier — corrected)

## Assistant
<summary>Running inspect_block_table calls to verify the flagged uninspected values: 288.15 K, 303.15 K, min viscosity 0.001208, and max viscosity 0.004014 in PROPblock_12.</summary>
<tool_call>run_subagent_tool(tool_name=inspect_block_table, kwargs={'block_number': …)</tool_call>

## User
<tool_result>
(validation blocked run_subagent_tool earlier — corrected)
</tool_result>

## Assistant
<summary>Re-running inspect_block_table with required `literature` parameter for all four flagged values in PROPblock_12.</summary>
<tool_call>run_subagent_tool(tool_name=inspect_block_table, kwargs={'literature': 'G…)</tool_call>

## User
<tool_result>
**Verdict:** The 288.15 K data point in PROPblock_12 is confirmed. At T = 288.15 K, mass fraction of propan-2-ol = 0.1, and pressure = 100.0 kPa, the viscosity is 0.001936 Pa·s.

| BLKpoint_id | temperature_k | mass_fraction_<propan-2-ol> | pressure_kpa | viscosity_pa_s |
|---|---|---|---|---|
| BLKpoint_1 | 288.15 | 0.1 | 100.0 | 0.001936 |

Block stats (all 12 rows): T range 288.15–303.15 K; mass_fraction_propan_2_ol 0.1–0.3; viscosity 0.001208–0.004014 Pa·s.
</tool_result>

## Assistant
<summary>First inspection confirmed 288.15 K (viscosity 0.001936 Pa·s at w=0.1). Now inspecting 303.15 K, min viscosity 0.001208, and max viscosity 0.004014 in PROPblock_12.</summary>
<tool_call>run_subagent_tool(tool_name=inspect_block_table, kwargs={'literature': 'G…)</tool_call>

## User
<tool_result>
**Verdict:** PROPblock_12 contains an exact data point at T = 303.15 K. The viscosity of the water + propan-2-ol mixture (mass fraction 0.1 propan-2-ol) at 100.0 kPa is **0.001208 Pa·s**.

| Field | Value |
|---|---|
| BLKpoint_id | BLKpoint_10 |
| temperature_k | 303.15 |
| mass_fraction (propan-2-ol) | 0.1 |
| pressure_kpa | 100.0 |
| viscosity_pa_s | 0.001208 |

Block stats (all 12 points): T range 288.15–303.15 K; mass fraction propan-2-ol 0.1–0.3; viscosity 0.001208–0.004014 Pa·s.
</tool_result>

## Assistant
<summary>Confirmed 303.15 K point (viscosity 0.001208 Pa·s at w=0.1). This also confirms the minimum viscosity 0.001208. Now need to inspect the maximum viscosity 0.004014 Pa·s.</summary>
<tool_call>run_subagent_tool(tool_name=inspect_block_table, kwargs={'literature': 'G…)</tool_call>

## User
<tool_result>
**Verdict:** Confirmed — the maximum viscosity in PROPblock_12 is **0.004014 Pa·s**, found at BLKpoint_3.

| Field | Value |
|---|---|
| BLKpoint_id | BLKpoint_3 |
| temperature_k | 288.15 |
| mass_fraction_propan-2-ol | 0.3 |
| pressure_kpa | 100.0 |
| viscosity_pa_s | 0.004014 |

Block-wide stats (n=12): viscosity range 0.001208–0.004014 Pa·s; temperature range 288.15–303.15 K; mass_fraction_propan-2-ol range 0.1–0.3.
</tool_result>

## Assistant
<reasoning>
All flagged values are now inspected and confirmed:
- 288.15 K: confirmed (BLKpoint_1, viscosity 0.001936 Pa·s at w=0.1)
- 303.15 K: confirmed (BLKpoint_10, viscosity 0.001208 Pa·s at w=0.1)
- 0.001208 Pa·s: confirmed as minimum viscosity (BLKpoint_10, T=303.15 K, w=0.1)
- 0.004014 Pa·s: confirmed as maximum viscosity (BLKpoint_3, T=288.15 K, w=0.3)

The values 0.6 and 0.7 for the viscosity maximum location are general chemistry knowledge, not database data. I need to label them as such in the answer.

Now I can re-issue the final answer with all values grounded.
</reasoning>

<summary>
All flagged values now inspected and confirmed: 288.15 K, 303.15 K, min viscosity 0.001208 Pa·s (BLKpoint_10), max viscosity 0.004014 Pa·s (BLKpoint_3). The w≈0.6–0.7 viscosity maximum reference is general chemistry knowledge, not database data — will label accordingly.
</summary>

<answer>
## Viscosity Data for Rubbing Alcohol (Isopropanol) + Water at Room Temperature

"Rubbing alcohol" is isopropanol (propan-2-ol, 2-propanol). The ThermoML database contains **dynamic viscosity** measurements for the binary mixture of isopropanol + water near room temperature.

### Source

- **Literature ID:** GLOBlit_5585
- **DOI:** 10.1016/j.jct.2019.105880
- **Data block:** PROPblock_12
- **Method:** Falling/rolling sphere viscometry
- **Phase:** Liquid
- **Pressure:** 100 kPa
- **Full temperature range in block:** 288.15–303.15 K (12 data points total)
- **Composition range:** Mass fraction of isopropanol from 0.1 to 0.3

### Data at Room Temperature (293–298 K)

Six data points fall within the standard "room temperature" window:

| Temperature (K) | Mass fraction of isopropanol | Dynamic Viscosity (Pa·s) |
|:---:|:---:|:---:|
| 293.15 | 0.1 | 0.001633 |
| 293.15 | 0.2 | 0.002485 |
| 293.15 | 0.3 | 0.003172 |
| 298.15 | 0.1 | 0.001395 |
| 298.15 | 0.2 | 0.002045 |
| 298.15 | 0.3 | 0.002555 |

All measurements at 100.0 kPa in the liquid phase.

### Additional Inspected Data Points

The full block also includes data at the boundary temperatures:

| Temperature (K) | Mass fraction of isopropanol | Dynamic Viscosity (Pa·s) |
|:---:|:---:|:---:|
| 288.15 | 0.1 | 0.001936 |
| 288.15 | 0.3 | 0.004014 |
| 303.15 | 0.1 | 0.001208 |

### Key Observations

1. **Viscosity increases with isopropanol content** across the 0.1–0.3 mass-fraction range. At 293.15 K, the viscosity nearly doubles from 0.001633 Pa·s (w = 0.1) to 0.003172 Pa·s (w = 0.3). This reflects the strong hydrogen-bonding interactions between isopropanol and water molecules, which progressively increase internal friction as more alcohol is added. It is well known from the general physical chemistry literature (not from this database) that the viscosity maximum for this system occurs at higher alcohol concentrations, around w ≈ 0.6–0.7; the data here capture the rising portion of that curve.

2. **Viscosity decreases with increasing temperature**, consistent with the typical Arrhenius-type behavior of liquid viscosity. For example, at w = 0.3, the viscosity drops from 0.003172 Pa·s at 293.15 K to 0.002555 Pa·s at 298.15 K — a reduction of roughly 19% for just a 5 K increase.

3. **Only dynamic viscosity** (not kinematic viscosity) was found in ThermoML for this system in this temperature range.

4. **Across the full block** (288.15–303.15 K, w = 0.1–0.3), viscosities range from 0.001208 Pa·s (at 303.15 K, w = 0.1) to 0.004014 Pa·s (at 288.15 K, w = 0.3).

### Sources
- Literature ID: GLOBlit_5585 | DOI: 10.1016/j.jct.2019.105880 | Block: PROPblock_12 | System: propan-2-ol (isopropanol) + water
</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **UNINSPECTED_VALUE** PROPblock_12: 288.15 exists in PROPblock_12's database table but was never shown in an inspection of this run
  fix (required — this value IS in the cited block's database table): `inspect_block_table(block_number="GLOBlit_5585::PROPblock_12", nearest={"column": "temperature_k", "value": 288.15})`
- **UNINSPECTED_VALUE** PROPblock_12: 303.15 exists in PROPblock_12's database table but was never shown in an inspection of this run
  fix (required — this value IS in the cited block's database table): `inspect_block_table(block_number="GLOBlit_5585::PROPblock_12", nearest={"column": "temperature_k", "value": 303.15})`
- **UNINSPECTED_VALUE** PROPblock_12: 288.15 exists in PROPblock_12's database table but was never shown in an inspection of this run
  fix (required — this value IS in the cited block's database table): `inspect_block_table(block_number="GLOBlit_5585::PROPblock_12", nearest={"column": "temperature_k", "value": 288.15})`
- **UNINSPECTED_VALUE** PROPblock_12: 0.001936 exists in PROPblock_12's database table but was never shown in an inspection of this run
  fix (required — this value IS in the cited block's database table): `inspect_block_table(block_number="GLOBlit_5585::PROPblock_12", nearest={"column": "viscosity_pa_s", "value": 0.001936})`
- **UNINSPECTED_VALUE** PROPblock_12: 288.15 exists in PROPblock_12's database table but was never shown in an inspection of this run
  fix (required — this value IS in the cited block's database table): `inspect_block_table(block_number="GLOBlit_5585::PROPblock_12", nearest={"column": "temperature_k", "value": 288.15})`
- **UNINSPECTED_VALUE** PROPblock_12: 0.004014 exists in PROPblock_12's database table but was never shown in an inspection of this run
  fix (required — this value IS in the cited block's database table): `inspect_block_table(block_number="GLOBlit_5585::PROPblock_12", nearest={"column": "viscosity_pa_s", "value": 0.004014})`
- **UNINSPECTED_VALUE** PROPblock_12: 303.15 exists in PROPblock_12's database table but was never shown in an inspection of this run
  fix (required — this value IS in the cited block's database table): `inspect_block_table(block_number="GLOBlit_5585::PROPblock_12", nearest={"column": "temperature_k", "value": 303.15})`
- **UNINSPECTED_VALUE** PROPblock_12: 0.001208 exists in PROPblock_12's database table but was never shown in an inspection of this run
  fix (required — this value IS in the cited block's database table): `inspect_block_table(block_number="GLOBlit_5585::PROPblock_12", nearest={"column": "viscosity_pa_s", "value": 0.001208})`
- … and 8 more of the same kinds — PROPblock_12: 0.6, 0.7, 288.15, 303.15, 0.001208, 0.004014
Inspected so far: PROPblock_12

Partially grounded — the values listed below ARE verified and must stay as quoted; change ONLY the flagged one(s) above:
- PROPblock_12: 100, 0.1, 0.3, 293, 298, 293.15, 0.001633, 0.2, 0.002485, 0.003172, 298.15, 0.001395, 0.002045, 0.002555, 100.0

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

NOTE: 1 tool-call block(s) on turn(s) 4 were rejected for malformed syntax and NEVER EXECUTED — no result exists for them. Repair the answer from executed tool results only; do not quote anything you 'remember' from those rejected turns.

## Assistant
<summary>Re-running inspect_block_table calls for all flagged values so they register properly in the inspection ledger: 288.15 K, 303.15 K, viscosity 0.001936, 0.004014, 0.001208.</summary>
<tool_call>run_subagent_tool(tool_name=inspect_block_table, kwargs={'literature': 'G…)</tool_call>

## User
<tool_result>
**Verdict:** PROPblock_12 contains an exact data point at 288.15 K. The viscosity of the water + propan-2-ol binary mixture at that temperature is 0.001936 Pa·s (mass fraction of propan-2-ol = 0.1, pressure = 100.0 kPa).

| BLKpoint_id | temperature_k | mass_fraction_\<propan-2-ol\> | pressure_kpa | viscosity_pa_s |
|---|---|---|---|---|
| BLKpoint_1 | 288.15 | 0.1 | 100.0 | 0.001936 |

**Block stats (n=12):** T range 288.15–303.15 K; mass fraction propan-2-ol 0.1–0.3; viscosity 0.001208–0.004014 Pa·s; pressure fixed at 100.0 kPa.
</tool_result>

## Assistant
<summary>Got 288.15 K inspection confirmed. Now inspecting 303.15 K, max viscosity 0.004014, and min viscosity 0.001208.</summary>
<tool_call>run_subagent_tool(tool_name=inspect_block_table, kwargs={'literature': 'G…)</tool_call>

## User
<tool_result>
**Verified:** PROPblock_12 contains an exact data point at T = 303.15 K. The row confirms viscosity of the water + propan-2-ol binary mixture at the specified conditions.

| BLKpoint_id | temperature_k | mass_fraction_propan-2-ol | pressure_kpa | viscosity_pa_s |
|---|---|---|---|---|
| BLKpoint_10 | 303.15 | 0.1 | 100.0 | 0.001208 |

**Block stats (all 12 points):** T range 288.15–303.15 K; mass fraction propan-2-ol 0.1–0.3; pressure 100.0 kPa (constant); viscosity 0.001208–0.004014 Pa·s.
</tool_result>

## Assistant
<summary>Got 303.15 K and 0.001208 confirmed. Now inspecting max viscosity 0.004014 Pa·s.</summary>
<tool_call>run_subagent_tool(tool_name=inspect_block_table, kwargs={'literature': 'G…)</tool_call>

## User
<tool_result>
**Verdict:** Confirmed — the maximum viscosity in PROPblock_12 is exactly **0.004014 Pa·s**, occurring at BLKpoint_3 (T = 288.15 K, mass fraction propan-2-ol = 0.3, P = 100.0 kPa). Block stats show the full viscosity range is 0.001208–0.004014 Pa·s across 12 data points.

| Field | Value |
|---|---|
| BLKpoint_id | BLKpoint_3 |
| temperature_k | 288.15 |
| mass_fraction_propan-2-ol | 0.3 |
| pressure_kpa | 100.0 |
| viscosity_pa_s | 0.004014 |
| Block viscosity range | 0.001208–0.004014 (n=12) |
| inspection_id | INSP_f9ca73817903 |
</tool_result>

## LLM Response
<reasoning>
Now all flagged values have been properly inspected in this run:
- 288.15 K: confirmed (BLKpoint_1, viscosity 0.001936 Pa·s at w=0.1)
- 303.15 K: confirmed (BLKpoint_10, viscosity 0.001208 Pa·s at w=0.1)
- 0.001936 Pa·s: confirmed (BLKpoint_1, T=288.15 K, w=0.1)
- 0.001208 Pa·s: confirmed (BLKpoint_10, T=303.15 K, w=0.1) — minimum viscosity
- 0.004014 Pa·s: confirmed (BLKpoint_3, T=288.15 K, w=0.3) — maximum viscosity

The values 0.6 and 0.7 are general chemistry knowledge about the viscosity maximum location, not database data — I'll label them explicitly as such.

Now I can issue the final answer with all values grounded.
</reasoning>

<summary>
All flagged values now inspected and confirmed in this run: 288.15 K (BLKpoint_1), 303.15 K (BLKpoint_10), 0.001936 Pa·s, 0.001208 Pa·s, 0.004014 Pa·s. Values 0.6–0.7 are general chemistry knowledge, will label as such. Ready for final answer.
</summary>

<answer>
## Viscosity Data for Rubbing Alcohol (Isopropanol) + Water at Room Temperature

"Rubbing alcohol" is isopropanol (propan-2-ol, 2-propanol). The ThermoML database contains **dynamic viscosity** measurements for the binary mixture of isopropanol + water near room temperature.

### Source

- **Literature ID:** GLOBlit_5585
- **DOI:** 10.1016/j.jct.2019.105880
- **Data block:** PROPblock_12
- **Method:** Falling/rolling sphere viscometry
- **Phase:** Liquid
- **Pressure:** 100 kPa
- **Full temperature range in block:** 288.15–303.15 K (12 data points total)
- **Composition range:** Mass fraction of isopropanol from 0.1 to 0.3

### Data at Room Temperature (293–298 K)

Six data points fall within the standard "room temperature" window:

| Temperature (K) | Mass fraction of isopropanol | Dynamic Viscosity (Pa·s) |
|:---:|:---:|:---:|
| 293.15 | 0.1 | 0.001633 |
| 293.15 | 0.2 | 0.002485 |
| 293.15 | 0.3 | 0.003172 |
| 298.15 | 0.1 | 0.001395 |
| 298.15 | 0.2 | 0.002045 |
| 298.15 | 0.3 | 0.002555 |

All measurements at 100.0 kPa in the liquid phase.

### Additional Inspected Data Points

The full block also includes data at the boundary temperatures:

| Temperature (K) | Mass fraction of isopropanol | Dynamic Viscosity (Pa·s) |
|:---:|:---:|:---:|
| 288.15 | 0.1 | 0.001936 |
| 288.15 | 0.3 | 0.004014 |
| 303.15 | 0.1 | 0.001208 |

### Key Observations

1. **Viscosity increases with isopropanol content** across the 0.1–0.3 mass-fraction range. At 293.15 K, the viscosity nearly doubles from 0.001633 Pa·s (w = 0.1) to 0.003172 Pa·s (w = 0.3). This reflects the strong hydrogen-bonding interactions between isopropanol and water molecules, which progressively increase internal friction as more alcohol is added. It is well known from the general physical chemistry literature (not from this database) that the viscosity maximum for this system occurs at higher alcohol concentrations, around w ≈ 0.6–0.7; the data here capture the rising portion of that curve.

2. **Viscosity decreases with increasing temperature**, consistent with the typical Arrhenius-type behavior of liquid viscosity. For example, at w = 0.3, the viscosity drops from 0.003172 Pa·s at 293.15 K to 0.002555 Pa·s at 298.15 K — a reduction of roughly 19% for just a 5 K increase.

3. **Only dynamic viscosity** (not kinematic viscosity) was found in ThermoML for this system in this temperature range.

4. **Across the full block** (288.15–303.15 K, w = 0.1–0.3), viscosities range from 0.001208 Pa·s (at 303.15 K, w = 0.1) to 0.004014 Pa·s (at 288.15 K, w = 0.3).

### Sources
- Literature ID: GLOBlit_5585 | DOI: 10.1016/j.jct.2019.105880 | Block: PROPblock_12 | System: propan-2-ol (isopropanol) + water
</answer>