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
**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260815_194722_684644_49ae3f02`

### History
- [analysis:A1] "Fit a Redlich-Kister polynomial to the viscosity of the binary liquid mixture wa" (469s, 14 iters, validation=PASS verdict=**Data Quality**
The trace sho)

### Analysis Agent Results

#### A1
**A1** — validation: PASS

**Answer:**

#### Redlich-Kister Fit for Viscosity of Water + Ethylene Glycol at 298.15 K

##### System & Source

**WM_A#1_Table#1_(Main_A#1_Answer):**

| *row_id* | *Parameter* | *Value* |
|---|---|---|
| WM_A#1_Table#1_Row#1 | 「System」 | 「Water + 1,2-ethanediol (ethylene glycol), binary liquid」 |
| WM_A#1_Table#1_Row#2 | 「Source」 | 「GLOBlit_5201 / DOI 10.1016/j.jct.2018.02.022 / PROPblock_24」 |
| WM_A#1_Table#1_Row#3 | 「Measurement method」 | 「Concentric cylinders viscometry」 |
| WM_A#1_Table#1_Row#4 | 「Temperature」 | 「298.15 K」 |
| WM_A#1_Table#1_Row#5 | 「Pressure」 | 「92.3 kPa」 |
| WM_A#1_Table#1_Row#6 | 「Composition basis」 | 「Mole fraction of 1,2-ethanediol (*x*₁), range 0–1 (21 unique compositions)」 |
| WM_A#1_Table#1_Row#7 | 「Viscosity basis」 | 「Dynamic viscosity, η (Pa·s)」 |
| WM_A#1_Table#1_Row#8 | 「Data points used」 | 「19 mixture + 2 pure-component endpoints = 21 points」 |

##### Pure-Component Endpoint Values (from block edges)

**WM_A#1_Table#2_(Main_A#1_Answer):**

| *row_id* | *Component* | *η* (Pa·s)* |
|---|---|---|
| WM_A#1_Table#2_Row#1 | 「1,2-ethanediol (x₁ = 1)」 | 「0.016223」 |
| WM_A#1_Table#2_Row#2 | 「Water (x₁ = 0)」 | 「0.00089689」 |

##### Mixing Rule & RK Equation

Because viscosity spans nearly two orders of magnitude across the composition range, the **Arrhenius (logarithmic) mixing rule** is used:

$$\ln\eta = x_1 \ln\eta_1^* + (1 - x_1)\ln\eta_2^* + x_1(1 - x_1)\sum_{k=0}^{n} A_k\,(2x_1 - 1)^k$$

where *x*₁ = mole fraction of 1,2-ethanediol, η₁\* = 0.016223 Pa·s, η₂\* = 0.00089689 Pa·s.

##### BIC-Selected Fit: Order 3

**WM_A#1_Table#3_(Main_A#1_Answer):**

| *row_id* | *Coefficient* | *Value (dimensionless)* |
|---|---|---|
| WM_A#1_Table#3_Row#1 | 「A₀」 | 「2.39674」 |
| WM_A#1_Table#3_Row#2 | 「A₁」 | 「−1.04444」 |
| WM_A#1_Table#3_Row#3 | 「A₂」 | 「0.668173」 |
| WM_A#1_Table#3_Row#4 | 「A₃」 | 「−0.3209」 |

##### Fit Quality

**WM_A#1_Table#4_(Main_A#1_Answer):**

| *row_id* | *Metric* | *Value* |
|---|---|---|
| WM_A#1_Table#4_Row#1 | 「R²」 | 「0.999940」 |
| WM_A#1_Table#4_Row#2 | 「RMSE」 | 「0.001320 (in ln η space)」 |
| WM_A#1_Table#4_Row#3 | 「BIC」 | 「−240.17」 |

##### Model Selection (BIC Comparison)

**WM_A#1_Table#5_(Main_A#1_Answer):**

| *row_id* | *Order* | *BIC* | *R²* | *RMSE* |
|---|---|---|---|---|
| WM_A#1_Table#5_Row#1 | 「0」 | 「−90.89」 | 「0.7516」 | 「0.08465」 |
| WM_A#1_Table#5_Row#2 | 「1」 | 「−141.05」 | 「0.9848」 | 「0.02092」 |
| WM_A#1_Table#5_Row#3 | 「2」 | 「−194.71」 | 「0.9992」 | 「0.00472」 |
| WM_A#1_Table#5_Row#4 | 「**3**」 | 「**−240.17**」 | 「**0.9999**」 | 「**0.00132**」 |
| WM_A#1_Table#5_Row#5 | 「4」 | 「−237.59」 | 「0.9999」 | 「0.00131」 |
| WM_A#1_Table#5_Row#6 | 「5」 | 「−234.83」 | 「0.9999」 | 「0.00130」 |

Order 3 is selected by BIC — orders 4 and 5 offer negligible improvement and are penalized for additional parameters.

##### Chemistry Insight

The large, positive A₀ coefficient (+2.40) confirms a strong **positive deviation** of viscosity from the Arrhenius ideal-mixing baseline. This is characteristic of the water–ethylene glycol system, where the two hydroxyl groups of ethylene glycol form an extensive hydrogen-bonding network with water, creating transient supramolecular structures that resist flow more than either pure component would predict. The asymmetry captured by A₁ (−1.04) and higher-order terms reflects the fact that the viscosity maximum shifts toward the ethylene-glycol-rich side, consistent with the stoichiometry of the hydrogen-bonding complexes.

Representative data points at 298.15 K (from inspected block data):
- *x*₁ = 0 (pure water): η = 0.00089689 Pa·s
- *x*₁ = 0.2072: η = 0.0028109 Pa·s
- *x*₁ = 0.4446: η = 0.0060624 Pa·s
- *x*₁ = 1.0 (pure EG): η = 0.016223 Pa·s

##### Output Files

- Fit data CSV: `10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_fit.csv`
- Excess property CSV: `10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_excess.csv`
- Fit plot: `10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_fit.png`
- Excess plot: `10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_excess.png`

**Core claims:**
- For the water + 1,2-ethanediol (ethylene glycol) binary liquid system at 298.15 K and 92.3 kPa, dynamic viscosity across 21 compositions (x₁ = 0–1) is well described by an Arrhenius (logarithmic) mixing rule with a Redlich-Kister excess term of order 3, selected by BIC (BIC = −240.17, R² = 0.999940, RMSE = 0.001320 in ln η space).
- The fitted Redlich-Kister coefficients (dimensionless) are A₀ = 2.39674, A₁ = −1.04444, A₂ = 0.668173, A₃ = −0.3209, with pure-component endpoints η*(1,2-ethanediol) = 0.016223 Pa·s and η*(water) = 0.00089689 Pa·s.
- The large positive A₀ (+2.40) indicates a strong positive deviation of viscosity from the Arrhenius ideal-mixing baseline, attributed to extensive hydrogen-bonding interactions between the two hydroxyl groups of ethylene glycol and water that form transient supramolecular structures resisting flow.
- The asymmetry captured by A₁ (−1.04) and higher-order terms reflects a shift of the viscosity maximum toward the ethylene-glycol-rich side, consistent with the stoichiometry of hydrogen-bonding complexes.
- Orders 4 and 5 offer negligible improvement over order 3 and are penalized by BIC for additional parameters.

**Sources:**

**WM_A#1_Table#6_(Main_A#1_Sources):**

| *row_id* | *lit_num_id* | *block* | *doi* | *BLKsubsys_id* | *description* |
|---|---|---|---|---|---|
| WM_A#1_Table#6_Row#1 | 「GLOBlit_5201」 | 「PROPblock_24」 | 「10.1016/j.jct.2018.02.022」 | 「—」 | 「This block provides binary viscosity data for water + 1,2-ethanediol across the full mole-fraction range (0–1) at multiple temperatures including 298.15 K, measured by concentric cylinders viscometry at 92.3 kPa. The 21 data points at 298.15 K extracted from the 84-point block were used to perform the Redlich-Kister fit of order 3 in ln η space, yielding the reported coefficients and fit statistics.」 |

**Fit results:**

**WM_A#1_Table#7_(Main_A#1_FitResults):**

| *row_id* | *lit_num_id* | *block* | *property* | *rk_order* | *rk_coeffs* | *r_squared* | *rmse* | *n_points* | *T_K* | *mixing_rule* |
|---|---|---|---|---|---|---|---|---|---|---|
| WM_A#1_Table#7_Row#1 | 「GLOBlit_5201」 | 「PROPblock_24」 | 「GLOBprop_4」 | 「3」 | 「2.3967401058713325, -1.0444436005853195, 0.6681733607879681, -0.3209004397507546」 | 「0.99994」 | 「0.0013198945265291695」 | 「19」 | 「298.15」 | 「arrhenius」 |

*Not stored here: 6 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


**Verdict:** **Data Quality**
The trace shows multiple `fit_block` attempts, with the final call (step 11) returning 899 chars — likely a successful fit result. Data originates from a ThermoML DOI (10.1016/j.jct.2018.02.022), and the block was inspected before fitting. The composition basis is mole fraction, and the property is dynamic viscosity — appropriate. However, the representative data points quoted (x₁ = 0.2072, 0.4446, etc.) cannot be independently verified against tool results in the trace since inspect_block outputs are truncated. The Arrhenius mixing rule is correctly applied for viscosity spanning ~1.8 orders of magnitude. No composition-basis conversion issues are apparent.

**Fit Quality**
Order 3 selected by BIC is reasonable. R² = 0.999940 with RMSE = 0.00132 in ln η space is excellent. BIC comparison shows clear plateau at order 3 — no overfitting concern.

**Scientific Verdict**
The fit is scientifically sound: logarithmic mixing rule is appropriate for viscosity, and the positive A₀ aligns with known strong H-bonding in this system. The truncated answer text is a minor presentation issue. Results are reliable for engineering interpolation across the full composition range.
**Session:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260815_194722_684644_49ae3f02\analysis_runs\run_1`
</memory>

## User
Near 25 °C, give me a Redlich–Kister correlation for the viscosity of liquid water + ethylene glycol using a single state-aligned composition series. State the selected temperature, pressure, composition basis, and viscosity basis, then report the equation, polynomial order, coefficients with units, R², RMSE, and composition range.

## Assistant
<summary>Delegating to the analysis agent to find viscosity data for water + ethylene glycol near 25°C and fit a Redlich-Kister polynomial to a single state-aligned composition series.</summary>
<tool_call>run_analysis_agent(question=Fit a Redlich-Kis…, context=The user wants a …)</tool_call>
<wait/> (4 deferred)

## User
<tool_result>
<subagent_answer>
### A#1 — run_analysis_agent return

**Status:** 14 iterations · 469.5s · 11 tool call(s) · agent=analysis
**Question:** Fit a Redlich-Kister polynomial to the viscosity of the binary liquid mixture water + ethylene glycol near 25 °C. Use a single state-aligned composition series. Report the selected temperature, pressure, composition basis (mole or mass fraction), viscosity basis (dynamic or kinematic), the RK equation, polynomial order, coefficients with units, R², RMSE, and the composition range covered.
**Session:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260815_194722_684644_49ae3f02\analysis_runs\run_1`

**Answer:**

#### Redlich-Kister Fit for Viscosity of Water + Ethylene Glycol at 298.15 K

##### System & Source

**A#1_Table#1_(Main_A#1_Answer):**

| *row_id* | *Parameter* | *Value* |
|---|---|---|
| A#1_Table#1_Row#1 | 「System」 | 「Water + 1,2-ethanediol (ethylene glycol), binary liquid」 |
| A#1_Table#1_Row#2 | 「Source」 | 「GLOBlit_5201 / DOI 10.1016/j.jct.2018.02.022 / PROPblock_24」 |
| A#1_Table#1_Row#3 | 「Measurement method」 | 「Concentric cylinders viscometry」 |
| A#1_Table#1_Row#4 | 「Temperature」 | 「298.15 K」 |
| A#1_Table#1_Row#5 | 「Pressure」 | 「92.3 kPa」 |
| A#1_Table#1_Row#6 | 「Composition basis」 | 「Mole fraction of 1,2-ethanediol (*x*₁), range 0–1 (21 unique compositions)」 |
| A#1_Table#1_Row#7 | 「Viscosity basis」 | 「Dynamic viscosity, η (Pa·s)」 |
| A#1_Table#1_Row#8 | 「Data points used」 | 「19 mixture + 2 pure-component endpoints = 21 points」 |

##### Pure-Component Endpoint Values (from block edges)

**A#1_Table#2_(Main_A#1_Answer):**

| *row_id* | *Component* | *η* (Pa·s)* |
|---|---|---|
| A#1_Table#2_Row#1 | 「1,2-ethanediol (x₁ = 1)」 | 「0.016223」 |
| A#1_Table#2_Row#2 | 「Water (x₁ = 0)」 | 「0.00089689」 |

##### Mixing Rule & RK Equation

Because viscosity spans nearly two orders of magnitude across the composition range, the **Arrhenius (logarithmic) mixing rule** is used:

$$\ln\eta = x_1 \ln\eta_1^* + (1 - x_1)\ln\eta_2^* + x_1(1 - x_1)\sum_{k=0}^{n} A_k\,(2x_1 - 1)^k$$

where *x*₁ = mole fraction of 1,2-ethanediol, η₁\* = 0.016223 Pa·s, η₂\* = 0.00089689 Pa·s.

##### BIC-Selected Fit: Order 3

**A#1_Table#3_(Main_A#1_Answer):**

| *row_id* | *Coefficient* | *Value (dimensionless)* |
|---|---|---|
| A#1_Table#3_Row#1 | 「A₀」 | 「2.39674」 |
| A#1_Table#3_Row#2 | 「A₁」 | 「−1.04444」 |
| A#1_Table#3_Row#3 | 「A₂」 | 「0.668173」 |
| A#1_Table#3_Row#4 | 「A₃」 | 「−0.3209」 |

##### Fit Quality

**A#1_Table#4_(Main_A#1_Answer):**

| *row_id* | *Metric* | *Value* |
|---|---|---|
| A#1_Table#4_Row#1 | 「R²」 | 「0.999940」 |
| A#1_Table#4_Row#2 | 「RMSE」 | 「0.001320 (in ln η space)」 |
| A#1_Table#4_Row#3 | 「BIC」 | 「−240.17」 |

##### Model Selection (BIC Comparison)

**A#1_Table#5_(Main_A#1_Answer):**

| *row_id* | *Order* | *BIC* | *R²* | *RMSE* |
|---|---|---|---|---|
| A#1_Table#5_Row#1 | 「0」 | 「−90.89」 | 「0.7516」 | 「0.08465」 |
| A#1_Table#5_Row#2 | 「1」 | 「−141.05」 | 「0.9848」 | 「0.02092」 |
| A#1_Table#5_Row#3 | 「2」 | 「−194.71」 | 「0.9992」 | 「0.00472」 |
| A#1_Table#5_Row#4 | 「**3**」 | 「**−240.17**」 | 「**0.9999**」 | 「**0.00132**」 |
| A#1_Table#5_Row#5 | 「4」 | 「−237.59」 | 「0.9999」 | 「0.00131」 |
| A#1_Table#5_Row#6 | 「5」 | 「−234.83」 | 「0.9999」 | 「0.00130」 |

Order 3 is selected by BIC — orders 4 and 5 offer negligible improvement and are penalized for additional parameters.

##### Chemistry Insight

The large, positive A₀ coefficient (+2.40) confirms a strong **positive deviation** of viscosity from the Arrhenius ideal-mixing baseline. This is characteristic of the water–ethylene glycol system, where the two hydroxyl groups of ethylene glycol form an extensive hydrogen-bonding network with water, creating transient supramolecular structures that resist flow more than either pure component would predict. The asymmetry captured by A₁ (−1.04) and higher-order terms reflects the fact that the viscosity maximum shifts toward the ethylene-glycol-rich side, consistent with the stoichiometry of the hydrogen-bonding complexes.

Representative data points at 298.15 K (from inspected block data):
- *x*₁ = 0 (pure water): η = 0.00089689 Pa·s
- *x*₁ = 0.2072: η = 0.0028109 Pa·s
- *x*₁ = 0.4446: η = 0.0060624 Pa·s
- *x*₁ = 1.0 (pure EG): η = 0.016223 Pa·s

##### Output Files

- Fit data CSV: `10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_fit.csv`
- Excess property CSV: `10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_excess.csv`
- Fit plot: `10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_fit.png`
- Excess plot: `10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_excess.png`

**Core claims:**
- For the water + 1,2-ethanediol (ethylene glycol) binary liquid system at 298.15 K and 92.3 kPa, dynamic viscosity across 21 compositions (x₁ = 0–1) is well described by an Arrhenius (logarithmic) mixing rule with a Redlich-Kister excess term of order 3, selected by BIC (BIC = −240.17, R² = 0.999940, RMSE = 0.001320 in ln η space).
- The fitted Redlich-Kister coefficients (dimensionless) are A₀ = 2.39674, A₁ = −1.04444, A₂ = 0.668173, A₃ = −0.3209, with pure-component endpoints η*(1,2-ethanediol) = 0.016223 Pa·s and η*(water) = 0.00089689 Pa·s.
- The large positive A₀ (+2.40) indicates a strong positive deviation of viscosity from the Arrhenius ideal-mixing baseline, attributed to extensive hydrogen-bonding interactions between the two hydroxyl groups of ethylene glycol and water that form transient supramolecular structures resisting flow.
- The asymmetry captured by A₁ (−1.04) and higher-order terms reflects a shift of the viscosity maximum toward the ethylene-glycol-rich side, consistent with the stoichiometry of hydrogen-bonding complexes.
- Orders 4 and 5 offer negligible improvement over order 3 and are penalized by BIC for additional parameters.

**Sources:**

**A#1_Table#6_(Main_A#1_Sources):**

| *row_id* | *lit_num_id* | *block* | *doi* | *BLKsubsys_id* | *description* |
|---|---|---|---|---|---|
| A#1_Table#6_Row#1 | 「GLOBlit_5201」 | 「PROPblock_24」 | 「10.1016/j.jct.2018.02.022」 | 「—」 | 「This block provides binary viscosity data for water + 1,2-ethanediol across the full mole-fraction range (0–1) at multiple temperatures including 298.15 K, measured by concentric cylinders viscometry at 92.3 kPa. The 21 data points at 298.15 K extracted from the 84-point block were used to perform the Redlich-Kister fit of order 3 in ln η space, yielding the reported coefficients and fit statistics.」 |

**Fit results:**

**A#1_Table#7_(Main_A#1_FitResults):**

| *row_id* | *lit_num_id* | *block* | *property* | *rk_order* | *rk_coeffs* | *r_squared* | *rmse* | *n_points* | *T_K* | *mixing_rule* |
|---|---|---|---|---|---|---|---|---|---|---|
| A#1_Table#7_Row#1 | 「GLOBlit_5201」 | 「PROPblock_24」 | 「GLOBprop_4」 | 「3」 | 「2.3967401058713325, -1.0444436005853195, 0.6681733607879681, -0.3209004397507546」 | 「0.99994」 | 「0.0013198945265291695」 | 「19」 | 「298.15」 | 「arrhenius」 |

#### Data inspections — verbatim ledger

```ledger
**A#1_Table#8_(Main_A#1_INSP):**
lit_num_id: GLOBlit_8106 | doi: 10.1021/je025610o | block: PROPblock_5
table_mode: rdp | inspection_id: INSP_475115ec48f0 | rows_shown: 16

| *row_id* | *BLKpoint_id* | *mole_fraction_<1,2-ethanediol>* | *temperature_k* | *pressure_kpa* | *viscosity_pa_s* |
|---|---|---|---|---|---|
| A#1_Table#8_Row#1 | 「BLKpoint_1」 | 「0.25」 | 「296.45」 | 「100.0」 | 「0.00369」 |
| A#1_Table#8_Row#2 | 「BLKpoint_2」 | 「0.25」 | 「313.05」 | 「100.0」 | 「0.00229」 |
| A#1_Table#8_Row#3 | 「BLKpoint_4」 | 「0.25」 | 「353.05」 | 「100.0」 | 「0.00099」 |
| A#1_Table#8_Row#4 | 「BLKpoint_8」 | 「0.25」 | 「435.55」 | 「100.0」 | 「0.000366」 |
| A#1_Table#8_Row#5 | 「BLKpoint_9」 | 「0.5」 | 「297.05」 | 「100.0」 | 「0.00761」 |
| A#1_Table#8_Row#6 | 「BLKpoint_10」 | 「0.5」 | 「313.05」 | 「100.0」 | 「0.00449」 |
| A#1_Table#8_Row#7 | 「BLKpoint_11」 | 「0.5」 | 「333.1」 | 「100.0」 | 「0.00262」 |
| A#1_Table#8_Row#8 | 「BLKpoint_12」 | 「0.5」 | 「353.05」 | 「100.0」 | 「0.0017」 |
| A#1_Table#8_Row#9 | 「BLKpoint_13」 | 「0.5」 | 「380.05」 | 「100.0」 | 「0.00107」 |
| A#1_Table#8_Row#10 | 「BLKpoint_17」 | 「0.5」 | 「440.65」 | 「100.0」 | 「0.0005」 |
| A#1_Table#8_Row#11 | 「BLKpoint_18」 | 「0.75」 | 「297.35」 | 「100.0」 | 「0.0123」 |
| A#1_Table#8_Row#12 | 「BLKpoint_19」 | 「0.75」 | 「313.05」 | 「100.0」 | 「0.00697」 |
| A#1_Table#8_Row#13 | 「BLKpoint_20」 | 「0.75」 | 「333.1」 | 「100.0」 | 「0.00388」 |
| A#1_Table#8_Row#14 | 「BLKpoint_21」 | 「0.75」 | 「353.05」 | 「100.0」 | 「0.00242」 |
| A#1_Table#8_Row#15 | 「BLKpoint_22」 | 「0.75」 | 「373.45」 | 「100.0」 | 「0.00162」 |
| A#1_Table#8_Row#16 | 「BLKpoint_30」 | 「0.75」 | 「449.85」 | 「100.0」 | 「0.000594」 |
```

```ledger
**A#1_Table#9_(Main_A#1_INSP):**
lit_num_id: GLOBlit_2656 | doi: 10.1016/j.jct.2006.01.011 | block: PROPblock_13
table_mode: complete | inspection_id: INSP_eb6a6a268c1a | rows_shown: 10

| *row_id* | *BLKpoint_id* | *mass_fraction_<1,2-ethanediol>* | *temperature_k* | *pressure_kpa* | *viscosity_pa_s* |
|---|---|---|---|---|---|
| A#1_Table#9_Row#1 | 「BLKpoint_1」 | 「0」 | 「293.15」 | 「101.325」 | 「0.001008」 |
| A#1_Table#9_Row#2 | 「BLKpoint_2」 | 「0.1」 | 「293.15」 | 「101.325」 | 「0.001293」 |
| A#1_Table#9_Row#3 | 「BLKpoint_3」 | 「0.2」 | 「293.15」 | 「101.325」 | 「0.001671」 |
| A#1_Table#9_Row#4 | 「BLKpoint_4」 | 「0.3」 | 「293.15」 | 「101.325」 | 「0.002177」 |
| A#1_Table#9_Row#5 | 「BLKpoint_5」 | 「0.4」 | 「293.15」 | 「101.325」 | 「0.002837」 |
| A#1_Table#9_Row#6 | 「BLKpoint_6」 | 「0.5」 | 「293.15」 | 「101.325」 | 「0.003558」 |
| A#1_Table#9_Row#7 | 「BLKpoint_7」 | 「0.6」 | 「293.15」 | 「101.325」 | 「0.004724」 |
| A#1_Table#9_Row#8 | 「BLKpoint_8」 | 「0.7」 | 「293.15」 | 「101.325」 | 「0.00636」 |
| A#1_Table#9_Row#9 | 「BLKpoint_9」 | 「0.8」 | 「293.15」 | 「101.325」 | 「0.008003」 |
| A#1_Table#9_Row#10 | 「BLKpoint_10」 | 「0.9」 | 「293.15」 | 「101.325」 | 「0.013999」 |
```

```ledger
**A#1_Table#10_(Main_A#1_INSP):**
lit_num_id: GLOBlit_5201 | doi: 10.1016/j.jct.2018.02.022 | block: PROPblock_24
table_mode: rdp | inspection_id: INSP_10e84136b97d | rows_shown: 15

| *row_id* | *BLKpoint_id* | *temperature_k* | *mole_fraction_<1,2-ethanediol>* | *pressure_kpa* | *viscosity_pa_s* |
|---|---|---|---|---|---|
| A#1_Table#10_Row#1 | 「BLKpoint_1」 | 「293.15」 | 「0.0494」 | 「92.3」 | 「0.0015411」 |
| A#1_Table#10_Row#2 | 「BLKpoint_4」 | 「293.15」 | 「0.2072」 | 「92.3」 | 「0.0035171」 |
| A#1_Table#10_Row#3 | 「BLKpoint_9」 | 「293.15」 | 「0.4446」 | 「92.3」 | 「0.0076382」 |
| A#1_Table#10_Row#4 | 「BLKpoint_23」 | 「298.15」 | 「0.2072」 | 「92.3」 | 「0.0028109」 |
| A#1_Table#10_Row#5 | 「BLKpoint_28」 | 「298.15」 | 「0.4446」 | 「92.3」 | 「0.0060624」 |
| A#1_Table#10_Row#6 | 「BLKpoint_47」 | 「303.15」 | 「0.4446」 | 「92.3」 | 「0.0053492」 |
| A#1_Table#10_Row#7 | 「BLKpoint_65」 | 「308.15」 | 「0.3921」 | 「92.3」 | 「0.0040265」 |
| A#1_Table#10_Row#8 | 「BLKpoint_77」 | 「293.15」 | 「0」 | 「92.3」 | 「0.0010673」 |
| A#1_Table#10_Row#9 | 「BLKpoint_78」 | 「298.15」 | 「0」 | 「92.3」 | 「0.00089689」 |
| A#1_Table#10_Row#10 | 「BLKpoint_79」 | 「303.15」 | 「0」 | 「92.3」 | 「0.0008385」 |
| A#1_Table#10_Row#11 | 「BLKpoint_80」 | 「308.15」 | 「0」 | 「92.3」 | 「0.00075887」 |
| A#1_Table#10_Row#12 | 「BLKpoint_81」 | 「293.15」 | 「1」 | 「92.3」 | 「0.020613」 |
| A#1_Table#10_Row#13 | 「BLKpoint_82」 | 「298.15」 | 「1」 | 「92.3」 | 「0.016223」 |
| A#1_Table#10_Row#14 | 「BLKpoint_83」 | 「303.15」 | 「1」 | 「92.3」 | 「0.013867」 |
| A#1_Table#10_Row#15 | 「BLKpoint_84」 | 「308.15」 | 「1」 | 「92.3」 | 「0.011483」 |
```

```ledger
**A#1_Table#11_(Main_A#1_INSP):**
lit_num_id: GLOBlit_6951 | doi: 10.1021/acs.jced.6b00526 | block: PROPblock_18
table_mode: rdp | inspection_id: INSP_bdb58d28aae5 | rows_shown: 14

| *row_id* | *BLKpoint_id* | *temperature_k* | *mole_fraction_<water>* | *pressure_kpa* | *viscosity_pa_s* |
|---|---|---|---|---|---|
| A#1_Table#11_Row#1 | 「BLKpoint_1」 | 「293.15」 | 「0」 | 「100.0」 | 「0.02113」 |
| A#1_Table#11_Row#2 | 「BLKpoint_3」 | 「293.15」 | 「0.2014」 | 「100.0」 | 「0.01495」 |
| A#1_Table#11_Row#3 | 「BLKpoint_5」 | 「293.15」 | 「0.4011」 | 「100.0」 | 「0.01005」 |
| A#1_Table#11_Row#4 | 「BLKpoint_8」 | 「293.15」 | 「0.6995」 | 「100.0」 | 「0.004584」 |
| A#1_Table#11_Row#5 | 「BLKpoint_11」 | 「293.15」 | 「1」 | 「100.0」 | 「0.000949」 |
| A#1_Table#11_Row#6 | 「BLKpoint_12」 | 「298.15」 | 「0」 | 「100.0」 | 「0.01724」 |
| A#1_Table#11_Row#7 | 「BLKpoint_14」 | 「298.15」 | 「0.2014」 | 「100.0」 | 「0.01219」 |
| A#1_Table#11_Row#8 | 「BLKpoint_16」 | 「298.15」 | 「0.4011」 | 「100.0」 | 「0.00831」 |
| A#1_Table#11_Row#9 | 「BLKpoint_19」 | 「298.15」 | 「0.6995」 | 「100.0」 | 「0.003884」 |
| A#1_Table#11_Row#10 | 「BLKpoint_22」 | 「298.15」 | 「1」 | 「100.0」 | 「0.000843」 |
| A#1_Table#11_Row#11 | 「BLKpoint_23」 | 「303.15」 | 「0」 | 「100.0」 | 「0.01423」 |
| A#1_Table#11_Row#12 | 「BLKpoint_25」 | 「303.15」 | 「0.2014」 | 「100.0」 | 「0.01014」 |
| A#1_Table#11_Row#13 | 「BLKpoint_28」 | 「303.15」 | 「0.4969」 | 「100.0」 | 「0.005653」 |
| A#1_Table#11_Row#14 | 「BLKpoint_33」 | 「303.15」 | 「1」 | 「100.0」 | 「0.000755」 |
```

```ledger
**A#1_Table#12_(Main_A#1_INSP):**
lit_num_id: GLOBlit_8038 | doi: 10.1021/je020140j | block: PROPblock_5
table_mode: rdp | inspection_id: INSP_ca607c3d05dd | rows_shown: 37

| *row_id* | *BLKpoint_id* | *mole_fraction_<1,2-ethanediol>* | *temperature_k* | *pressure_kpa* | *viscosity_pa_s* |
|---|---|---|---|---|---|
| A#1_Table#12_Row#1 | 「BLKpoint_1」 | 「0」 | 「293.15」 | 「101.0」 | 「0.001002」 |
| A#1_Table#12_Row#2 | 「BLKpoint_7」 | 「0」 | 「353.15」 | 「101.0」 | 「0.000356」 |
| A#1_Table#12_Row#3 | 「BLKpoint_8」 | 「0.0312」 | 「293.15」 | 「101.0」 | 「0.001337」 |
| A#1_Table#12_Row#4 | 「BLKpoint_14」 | 「0.0312」 | 「353.15」 | 「101.0」 | 「0.000434」 |
| A#1_Table#12_Row#5 | 「BLKpoint_15」 | 「0.0676」 | 「293.15」 | 「101.0」 | 「0.001785」 |
| A#1_Table#12_Row#6 | 「BLKpoint_21」 | 「0.0676」 | 「353.15」 | 「101.0」 | 「0.000525」 |
| A#1_Table#12_Row#7 | 「BLKpoint_22」 | 「0.1105」 | 「293.15」 | 「101.0」 | 「0.002272」 |
| A#1_Table#12_Row#8 | 「BLKpoint_24」 | 「0.1105」 | 「313.15」 | 「101.0」 | 「0.001319」 |
| A#1_Table#12_Row#9 | 「BLKpoint_28」 | 「0.1105」 | 「353.15」 | 「101.0」 | 「0.000629」 |
| A#1_Table#12_Row#10 | 「BLKpoint_29」 | 「0.162」 | 「293.15」 | 「101.0」 | 「0.002951」 |
| A#1_Table#12_Row#11 | 「BLKpoint_31」 | 「0.162」 | 「313.15」 | 「101.0」 | 「0.001677」 |
| A#1_Table#12_Row#12 | 「BLKpoint_35」 | 「0.162」 | 「353.15」 | 「101.0」 | 「0.000758」 |
| A#1_Table#12_Row#13 | 「BLKpoint_36」 | 「0.2248」 | 「293.15」 | 「101.0」 | 「0.003941」 |
| A#1_Table#12_Row#14 | 「BLKpoint_38」 | 「0.2248」 | 「313.15」 | 「101.0」 | 「0.002132」 |
| A#1_Table#12_Row#15 | 「BLKpoint_42」 | 「0.2248」 | 「353.15」 | 「101.0」 | 「0.000906」 |
| A#1_Table#12_Row#16 | 「BLKpoint_43」 | 「0.3031」 | 「293.15」 | 「101.0」 | 「0.005102」 |
| A#1_Table#12_Row#17 | 「BLKpoint_45」 | 「0.3031」 | 「313.15」 | 「101.0」 | 「0.002756」 |
| A#1_Table#12_Row#18 | 「BLKpoint_49」 | 「0.3031」 | 「353.15」 | 「101.0」 | 「0.0011」 |
| A#1_Table#12_Row#19 | 「BLKpoint_50」 | 「0.4036」 | 「293.15」 | 「101.0」 | 「0.006898」 |
| A#1_Table#12_Row#20 | 「BLKpoint_52」 | 「0.4036」 | 「313.15」 | 「101.0」 | 「0.003575」 |
| A#1_Table#12_Row#21 | 「BLKpoint_54」 | 「0.4036」 | 「333.15」 | 「101.0」 | 「0.002053」 |
| A#1_Table#12_Row#22 | 「BLKpoint_56」 | 「0.4036」 | 「353.15」 | 「101.0」 | 「0.001359」 |
| A#1_Table#12_Row#23 | 「BLKpoint_57」 | 「0.537」 | 「293.15」 | 「101.0」 | 「0.009696」 |
| A#1_Table#12_Row#24 | 「BLKpoint_58」 | 「0.537」 | 「303.15」 | 「101.0」 | 「0.006749」 |
| A#1_Table#12_Row#25 | 「BLKpoint_59」 | 「0.537」 | 「313.15」 | 「101.0」 | 「0.004776」 |
| A#1_Table#12_Row#26 | 「BLKpoint_61」 | 「0.537」 | 「333.15」 | 「101.0」 | 「0.002684」 |
| A#1_Table#12_Row#27 | 「BLKpoint_63」 | 「0.537」 | 「353.15」 | 「101.0」 | 「0.001748」 |
| A#1_Table#12_Row#28 | 「BLKpoint_64」 | 「0.723」 | 「293.15」 | 「101.0」 | 「0.014042」 |
| A#1_Table#12_Row#29 | 「BLKpoint_65」 | 「0.723」 | 「303.15」 | 「101.0」 | 「0.009399」 |
| A#1_Table#12_Row#30 | 「BLKpoint_66」 | 「0.723」 | 「313.15」 | 「101.0」 | 「0.006449」 |
| A#1_Table#12_Row#31 | 「BLKpoint_68」 | 「0.723」 | 「333.15」 | 「101.0」 | 「0.00351」 |
| A#1_Table#12_Row#32 | 「BLKpoint_70」 | 「0.723」 | 「353.15」 | 「101.0」 | 「0.002296」 |
| A#1_Table#12_Row#33 | 「BLKpoint_71」 | 「1」 | 「293.15」 | 「101.0」 | 「0.020833」 |
| A#1_Table#12_Row#34 | 「BLKpoint_72」 | 「1」 | 「303.15」 | 「101.0」 | 「0.013646」 |
| A#1_Table#12_Row#35 | 「BLKpoint_73」 | 「1」 | 「313.15」 | 「101.0」 | 「0.009443」 |
| A#1_Table#12_Row#36 | 「BLKpoint_75」 | 「1」 | 「333.15」 | 「101.0」 | 「0.00506」 |
| A#1_Table#12_Row#37 | 「BLKpoint_77」 | 「1」 | 「353.15」 | 「101.0」 | 「0.003021」 |
```

```ledger
**A#1_Table#13_(Main_A#1_INSP):**
lit_num_id: GLOBlit_11186 | doi: 10.1021/je800271e | block: PROPblock_4
table_mode: rdp | inspection_id: INSP_5611a4a4b21d | rows_shown: 14

| *row_id* | *BLKpoint_id* | *temperature_k* | *mole_fraction_<1,2-ethanediol>* | *viscosity_pa_s* |
|---|---|---|---|---|
| A#1_Table#13_Row#1 | 「BLKpoint_1」 | 「308.15」 | 「0」 | 「0.000721」 |
| A#1_Table#13_Row#2 | 「BLKpoint_8」 | 「308.15」 | 「0.1621」 | 「0.0015744」 |
| A#1_Table#13_Row#3 | 「BLKpoint_11」 | 「308.15」 | 「0.4035」 | 「0.0035116」 |
| A#1_Table#13_Row#4 | 「BLKpoint_13」 | 「308.15」 | 「1」 | 「0.0092122」 |
| A#1_Table#13_Row#5 | 「BLKpoint_14」 | 「313.15」 | 「0」 | 「0.0006532」 |
| A#1_Table#13_Row#6 | 「BLKpoint_21」 | 「313.15」 | 「0.1621」 | 「0.0014047」 |
| A#1_Table#13_Row#7 | 「BLKpoint_24」 | 「313.15」 | 「0.4035」 | 「0.0030166」 |
| A#1_Table#13_Row#8 | 「BLKpoint_26」 | 「313.15」 | 「1」 | 「0.0079605」 |
| A#1_Table#13_Row#9 | 「BLKpoint_27」 | 「318.15」 | 「0」 | 「0.00059」 |
| A#1_Table#13_Row#10 | 「BLKpoint_36」 | 「318.15」 | 「0.3032」 | 「0.0018883」 |
| A#1_Table#13_Row#11 | 「BLKpoint_39」 | 「318.15」 | 「1」 | 「0.0062933」 |
| A#1_Table#13_Row#12 | 「BLKpoint_40」 | 「323.15」 | 「0」 | 「0.00055」 |
| A#1_Table#13_Row#13 | 「BLKpoint_49」 | 「323.15」 | 「0.3032」 | 「0.0016786」 |
| A#1_Table#13_Row#14 | 「BLKpoint_52」 | 「323.15」 | 「1」 | 「0.0054468」 |
```

**Output files:**
- [data] `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260815_194722_684644_49ae3f02\analysis_runs\run_1\data\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_fit.csv` — RK fit data — 10.1016/j.jct.2018.02.022 PROPblock_24_T298.1
- [data] `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260815_194722_684644_49ae3f02\analysis_runs\run_1\data\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_excess.csv` — Excess property — 10.1016/j.jct.2018.02.022 PROPblock_24_T298.1
- [plot] `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260815_194722_684644_49ae3f02\analysis_runs\run_1\plots\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_fit.png` — RK fit plot — 10.1016/j.jct.2018.02.022 PROPblock_24_T298.1
- [plot] `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260815_194722_684644_49ae3f02\analysis_runs\run_1\plots\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_excess.png` — Excess plot — 10.1016/j.jct.2018.02.022 PROPblock_24_T298.1

**Verdict:**

**Data Quality**
The trace shows multiple `fit_block` attempts, with the final call (step 11) returning 899 chars — likely a successful fit result. Data originates from a ThermoML DOI (10.1016/j.jct.2018.02.022), and the block was inspected before fitting. The composition basis is mole fraction, and the property is dynamic viscosity — appropriate. However, the representative data points quoted (x₁ = 0.2072, 0.4446, etc.) cannot be independently verified against tool results in the trace since inspect_block outputs are truncated. The Arrhenius mixing rule is correctly applied for viscosity spanning ~1.8 orders of magnitude. No composition-basis conversion issues are apparent.

**Fit Quality**
Order 3 selected by BIC is reasonable. R² = 0.999940 with RMSE = 0.00132 in ln η space is excellent. BIC comparison shows clear plateau at order 3 — no overfitting concern.

**Scientific Verdict**
The fit is scientifically sound: logarithmic mixing rule is appropriate for viscosity, and the positive A₀ aligns with known strong H-bonding in this system. The truncated answer text is a minor presentation issue. Results are reliable for engineering interpolation across the full composition range.
</subagent_answer>

[WAIT BARRIER COMPLETE] 1 tool(s) finished (run_analysis_agent). 4 deferred call(s) were discarded. Use the results above to plan your next tool calls with correct IDs/DOIs — do NOT guess.
</tool_result>

## LLM Response
<answer>

## Redlich–Kister Correlation for the Dynamic Viscosity of Water + Ethylene Glycol at 298.15 K

### System & Conditions

| Parameter | Value |
|---|---|
| **System** | Water + 1,2-ethanediol (ethylene glycol), binary liquid |
| **Temperature** | 298.15 K (25.00 °C) |
| **Pressure** | 92.3 kPa |
| **Composition basis** | Mole fraction of 1,2-ethanediol, *x*₁ (single state-aligned series, 21 unique compositions from *x*₁ = 0 to 1) |
| **Viscosity basis** | Dynamic viscosity, η (Pa·s) |
| **Data points** | 19 mixture compositions + 2 pure-component endpoints = 21 points |
| **Measurement method** | Concentric cylinders viscometry |

### Pure-Component Endpoint Viscosities

| Component | η\* (Pa·s) |
|---|---|
| 1,2-Ethanediol (*x*₁ = 1) | 0.016223 |
| Water (*x*₁ = 0) | 0.00089689 |

### Mixing Rule & Redlich–Kister Equation

Because the dynamic viscosity spans nearly two orders of magnitude across the composition range (from ~0.9 × 10⁻³ to ~16 × 10⁻³ Pa·s), the **Arrhenius (logarithmic) mixing rule** is employed. The Redlich–Kister excess term is applied in ln η space:

$$\ln\eta = x_1 \ln\eta_1^{*} + (1 - x_1)\ln\eta_2^{*} \;+\; x_1(1 - x_1)\sum_{k=0}^{n} A_k\,(2x_1 - 1)^k$$

where *x*₁ is the mole fraction of 1,2-ethanediol, η₁\* = 0.016223 Pa·s (pure ethylene glycol), and η₂\* = 0.00089689 Pa·s (pure water).

### BIC-Selected Polynomial Order: 3

The Bayesian Information Criterion (BIC) selects **order 3** as optimal. Orders 4 and 5 offer negligible improvement in R² and RMSE while incurring a parameter-count penalty.

### Fitted Coefficients

| Coefficient | Value (dimensionless) |
|---|---|
| A₀ | +2.39674 |
| A₁ | −1.04444 |
| A₂ | +0.668173 |
| A₃ | −0.3209 |

The coefficients are dimensionless because the Redlich–Kister polynomial acts on ln η (also dimensionless).

### Fit Quality

| Metric | Value |
|---|---|
| R² | 0.999940 |
| RMSE | 0.001320 (in ln η space) |
| BIC | −240.17 |

### Model Selection Summary

| Order | BIC | R² | RMSE |
|---|---|---|---|
| 0 | −90.89 | 0.7516 | 0.08465 |
| 1 | −141.05 | 0.9848 | 0.02092 |
| 2 | −194.71 | 0.9992 | 0.00472 |
| **3** | **−240.17** | **0.9999** | **0.00132** |
| 4 | −237.59 | 0.9999 | 0.00131 |
| 5 | −234.83 | 0.9999 | 0.00130 |

### Composition Range

The correlation covers the **full mole-fraction range** of 1,2-ethanediol: *x*₁ = 0 (pure water) to *x*₁ = 1 (pure ethylene glycol), with 19 intermediate mixture compositions.

### Representative Data Points (298.15 K, from inspected block)

| *x*₁ (1,2-ethanediol) | η (Pa·s) |
|---|---|
| 0 (pure water) | 0.00089689 |
| 0.2072 | 0.0028109 |
| 0.4446 | 0.0060624 |
| 1.0 (pure EG) | 0.016223 |

### Chemistry Insight

The large, positive A₀ coefficient (+2.40) confirms a strong **positive deviation** of viscosity from the Arrhenius ideal-mixing baseline. This is characteristic of the water–ethylene glycol system: the two hydroxyl groups of ethylene glycol form an extensive hydrogen-bonding network with water, creating transient supramolecular structures that resist flow more than either pure component would predict. The asymmetry captured by A₁ (−1.04) and higher-order terms reflects the fact that the viscosity enhancement peaks on the ethylene-glycol-rich side, consistent with the stoichiometry of the dominant hydrogen-bonding complexes.

### Sources

- **Literature ID:** GLOBlit_5201 | **DOI:** 10.1016/j.jct.2018.02.022 | **Block:** PROPblock_24 — Binary viscosity data for water + 1,2-ethanediol across the full mole-fraction range at multiple temperatures including 298.15 K, measured by concentric cylinders viscometry at 92.3 kPa. The 21 data points at 298.15 K were used for the Redlich–Kister fit.

</answer>