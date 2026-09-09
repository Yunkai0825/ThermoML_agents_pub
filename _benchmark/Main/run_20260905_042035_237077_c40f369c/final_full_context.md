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
**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_042035_237077_c40f369c`

### History
- [parallel:3 tasks]
-   [query:MeOH_EtOH_visc] "Find viscosity data for the binary mixture of methanol + ethanol at or near 30°C" (113s, 2 iters, validation=PASS verdict=## Verdict
The answer appears )
-   [query:ACN_DMF_visc] "Find viscosity data for the binary mixture of acetonitrile + N,N-dimethylformami" (173s, 2 iters, validation=PASS verdict=## Verdict
The two DOIs and bl)
-   [query:Water_EG_visc] "Find viscosity data for the binary mixture of water + ethylene glycol at or near" (212s, 2 iters, validation=PASS verdict=## Verdict
The answer identifi)
- [parallel:auto-compacted] 3 per-task reports (agentic, targets ALL, philosophy elicited)
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → ERROR: where filter error: unknown column alias 'T'
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → ERROR: nearest must be {"column": alias, "value": number, "k": 1..8}
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → ERROR: `where` must be a non-empty filter string when given
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK

### Query Agent Results

#### MeOH_EtOH_visc
**MeOH_EtOH_visc** — confidence: high · validation: PASS

**Answer:**

#### Dynamic Viscosity of Methanol + Ethanol Binary Mixture at 303.15 K

##### Source

- **DOI:** 10.1021/je800633a
- **Block:** PROPblock_16
- **Measurement method:** Capillary tube (Ostwald–Ubbelohde)

##### System Details

**WM_Q#3_Table#1_(Main_Q#3_Answer):**

| *row_id* | *Parameter* | *Value* |
|---|---|---|
| WM_Q#3_Table#1_Row#1 | 「**Compounds**」 | 「Methanol (CH₄O) + Ethanol (C₂H₆O)」 |
| WM_Q#3_Table#1_Row#2 | 「**System type**」 | 「Binary liquid mixture」 |
| WM_Q#3_Table#1_Row#3 | 「**Temperature**」 | 「303.15 K (≈ 30 °C), fixed」 |
| WM_Q#3_Table#1_Row#4 | 「**Pressure**」 | 「81.5 kPa, fixed」 |

##### Viscosity vs. Mole Fraction of Methanol

Twelve data points spanning the composition range:

**WM_Q#3_Table#2_(Main_Q#3_Answer):**

| *row_id* | *x(methanol)* | *η (Pa·s)* |
|---|---|---|
| WM_Q#3_Table#2_Row#1 | 「0.0417」 | 「0.000968」 |
| WM_Q#3_Table#2_Row#2 | 「0.1476」 | 「0.000906」 |
| WM_Q#3_Table#2_Row#3 | 「0.2214」 | 「0.000865」 |
| WM_Q#3_Table#2_Row#4 | 「0.2952」 | 「0.000828」 |
| WM_Q#3_Table#2_Row#5 | 「0.3644」 | 「0.000793」 |
| WM_Q#3_Table#2_Row#6 | 「0.4488」 | 「0.000753」 |
| WM_Q#3_Table#2_Row#7 | 「0.529」 | 「0.000717」 |
| WM_Q#3_Table#2_Row#8 | 「0.5995」 | 「0.000685」 |
| WM_Q#3_Table#2_Row#9 | 「0.6859」 | 「0.000648」 |
| WM_Q#3_Table#2_Row#10 | 「0.7442」 | 「0.000624」 |
| WM_Q#3_Table#2_Row#11 | 「0.832」 | 「0.000588」 |
| WM_Q#3_Table#2_Row#12 | 「0.9166」 | 「0.000556」 |

##### Chemical Insight

The dynamic viscosity decreases monotonically from 0.000968 Pa·s at the ethanol-rich end (x(methanol) = 0.0417) to 0.000556 Pa·s at the methanol-rich end (x(methanol) = 0.9166). The decrease is nearly linear with composition, indicating relatively ideal mixing behavior with minimal excess viscosity effects in this system at 303.15 K.

This behavior is consistent with the molecular similarity of methanol and ethanol — both are small, linear aliphatic alcohols capable of hydrogen bonding. Methanol, being smaller (one carbon vs. two), has weaker van der Waals interactions and a less extensive hydrogen-bonding network, leading to its lower pure-component viscosity. The near-ideal mixing arises because the two components are structurally and chemically similar, so replacing ethanol molecules with methanol molecules in the mixture smoothly reduces the average intermolecular interaction strength without introducing significant structural disruption or preferential association.

**Core claims:**
- For the methanol + ethanol binary liquid mixture at 303.15 K and 81.5 kPa (DOI 10.1021/je800633a, PROPblock_16), the dynamic viscosity decreases monotonically from 0.000968 Pa·s at x(methanol) = 0.0417 to 0.000556 Pa·s at x(methanol) = 0.9166, as measured by capillary tube (Ostwald–Ubbelohde) across twelve compositions.
- The decrease in viscosity with increasing methanol mole fraction is nearly linear, indicating relatively ideal mixing behavior with minimal excess viscosity effects, consistent with the structural and chemical similarity of the two small aliphatic alcohols.

**Sources:**

**WM_Q#3_Table#3_(Main_Q#3_Sources):**

| *row_id* | *lit_num_id* | *block* | *doi* | *BLKsubsys_id* | *description* |
|---|---|---|---|---|---|
| WM_Q#3_Table#3_Row#1 | 「GLOBlit_11337」 | 「PROPblock_16」 | 「10.1021/je800633a」 | 「—」 | 「This block provides the 12 dynamic viscosity data points for the methanol + ethanol binary mixture at 303.15 K and 81.5 kPa, spanning mole fractions 0.0417–0.9166 with viscosities 0.000556–0.000968 Pa·s, which directly constitute the answer's tabulated data and analysis.」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### ACN_DMF_visc
**ACN_DMF_visc** — confidence: high · validation: PASS

**Answer:**

#### Dynamic Viscosity of Acetonitrile + N,N-Dimethylformamide (DMF) at 303.15 K

Two independent ThermoML data sources provide dynamic viscosity (η) measurements for the binary system **acetonitrile (CH₃CN)** + **N,N-dimethylformamide (DMF, C₃H₇NO)** at 303.15 K across the full composition range.

---

##### Source 1 — Mass-fraction basis

**DOI:** 10.1016/j.jct.2014.02.019 · **Block:** PROPblock_6  
**Compounds:** Acetonitrile (GLOBcomp_15) + Dimethylformamide (GLOBcomp_18)  
**Method:** Capillary tube (Ostwald/Ubbelohde) viscometry  
**Conditions:** T = 303.15 K, P = 101.0 kPa  
**Full block range:** 298.15–313.15 K, 20 total data points

**WM_Q#1_Table#1_(Main_Q#1_Answer):**

| *row_id* | *w(DMF)* | *η (Pa·s)* |
|---|---|---|
| WM_Q#1_Table#1_Row#1 | 「0」 | 「0.0003269」 |
| WM_Q#1_Table#1_Row#2 | 「0.25」 | 「0.0003598」 |
| WM_Q#1_Table#1_Row#3 | 「0.50」 | 「0.00046」 |
| WM_Q#1_Table#1_Row#4 | 「0.75」 | 「0.0006145」 |
| WM_Q#1_Table#1_Row#5 | 「1.00」 | 「0.000755」 |

---

##### Source 2 — Mole-fraction basis (recommended for your needs)

**DOI:** 10.1021/acs.jced.8b00176 · **Block:** PROPblock_18  
**Compounds:** Acetonitrile (GLOBcomp_15) + Dimethylformamide (GLOBcomp_18)  
**Method:** Falling/rolling sphere viscometry  
**Conditions:** T = 303.15 K, P = 100.0 kPa  
**Full block range:** 298.15–323.15 K, 66 total data points

**WM_Q#1_Table#2_(Main_Q#1_Answer):**

| *row_id* | *x(DMF)* | *η (Pa·s)* |
|---|---|---|
| WM_Q#1_Table#2_Row#1 | 「0」 | 「0.00032」 |
| WM_Q#1_Table#2_Row#2 | 「0.0989」 | 「0.00039」 |
| WM_Q#1_Table#2_Row#3 | 「0.1916」 | 「0.00042」 |
| WM_Q#1_Table#2_Row#4 | 「0.2925」 | 「0.00046」 |
| WM_Q#1_Table#2_Row#5 | 「0.3932」 | 「0.00051」 |
| WM_Q#1_Table#2_Row#6 | 「0.5029」 | 「0.00057」 |
| WM_Q#1_Table#2_Row#7 | 「0.6002」 | 「0.00061」 |
| WM_Q#1_Table#2_Row#8 | 「0.6931」 | 「0.00065」 |
| WM_Q#1_Table#2_Row#9 | 「0.7926」 | 「0.00070」 |
| WM_Q#1_Table#2_Row#10 | 「0.8996」 | 「0.00075」 |
| WM_Q#1_Table#2_Row#11 | 「1.0000」 | 「0.00077」 |

---

##### Chemical Insight

Both datasets show a **monotonic, slightly concave increase** in dynamic viscosity with increasing DMF content at 303.15 K. Pure DMF is roughly 2.4× more viscous than pure acetonitrile under these conditions (≈ 0.00077 vs. 0.00032 Pa·s). This trend reflects the stronger intermolecular interactions in DMF — it is a larger molecule with a higher dipole moment (~3.86 D vs. ~3.92 D for acetonitrile, but with a much larger molecular volume and stronger dipole–dipole/dispersion forces) and a pronounced hydrogen-bond-accepting capability via its carbonyl oxygen.

The two independent sources agree well at the pure-component endpoints (within ~2–3%), with minor differences attributable to different measurement techniques (capillary vs. falling-sphere viscometry) and a slight pressure difference (101.0 vs. 100.0 kPa). Source 2 (DOI 10.1021/acs.jced.8b00176) is particularly useful for your needs as it directly reports viscosity on a **mole-fraction basis** with 11 composition points spanning the full range, and covers a broader temperature window (298.15–323.15 K).

**Core claims:**
- Two independent ThermoML sources provide dynamic viscosity measurements for the acetonitrile + N,N-dimethylformamide binary system at 303.15 K across the full composition range.
- Both datasets show a monotonic, slightly concave increase in dynamic viscosity with increasing DMF content at 303.15 K, from approximately 0.00032 Pa·s (pure acetonitrile) to approximately 0.00077 Pa·s (pure DMF).
- Source 1 (DOI 10.1016/j.jct.2014.02.019) reports viscosity on a mass-fraction basis at 303.15 K and 101.0 kPa using capillary tube viscometry, with 5 composition points.
- Source 2 (DOI 10.1021/acs.jced.8b00176) reports viscosity on a mole-fraction basis at 303.15 K and 100.0 kPa using falling/rolling sphere viscometry, with 11 composition points spanning the full range and a broader temperature window of 298.15–323.15 K.
- The two independent sources agree at the pure-component endpoints within ~2–3%, with minor differences attributed to different measurement techniques and a slight pressure difference (101.0 vs. 100.0 kPa).
- The higher viscosity of pure DMF relative to pure acetonitrile is attributed to stronger intermolecular interactions in DMF, including its larger molecular volume, stronger dipole–dipole/dispersion forces, and hydrogen-bond-accepting capability via its carbonyl oxygen.

**Sources:**

**WM_Q#1_Table#3_(Main_Q#1_Sources):**

| *row_id* | *lit_num_id* | *block* | *doi* | *BLKsubsys_id* | *description* |
|---|---|---|---|---|---|
| WM_Q#1_Table#3_Row#1 | 「GLOBlit_4124」 | 「PROPblock_6」 | 「10.1016/j.jct.2014.02.019」 | 「—」 | 「Provides dynamic viscosity of the acetonitrile + DMF binary system on a mass-fraction basis at 303.15 K (within its 298.15–313.15 K range), measured by capillary tube viscometry at 101.0 kPa. The answer's Source 1 table values fall within the card's viscosity range of 0.000293–0.000799 Pa·s.」 |
| WM_Q#1_Table#3_Row#2 | 「GLOBlit_7481」 | 「PROPblock_18」 | 「10.1021/acs.jced.8b00176」 | 「—」 | 「Provides dynamic viscosity of the acetonitrile + DMF binary system on a mole-fraction basis at 303.15 K (within its 298.15–323.15 K range), measured by falling-sphere viscometry at 100.0 kPa with 66 data points spanning the full composition range. The answer's Source 2 table values fall within the card's viscosity range of 0.00028–0.00081 Pa·s.」 |

*Not stored here: 2 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### Water_EG_visc
**Water_EG_visc** — confidence: high · validation: PASS

**Answer:**

#### Dynamic Viscosity of Water + Ethylene Glycol (1,2-Ethanediol) at 303.15 K

Two independent ThermoML datasets provide dynamic viscosity data for the binary mixture of **water** and **1,2-ethanediol (ethylene glycol)** at exactly **303.15 K (30 °C)**, covering the full composition range.

---

##### Dataset 1 — DOI: 10.1016/j.jct.2018.02.022 · Block PROPblock_24

**Method:** Concentric cylinders viscometry · **Pressure:** 92.3 kPa · **Composition variable:** mole fraction of 1,2-ethanediol

**WM_Q#2_Table#1_(Main_Q#2_Answer):**

| *row_id* | *x(1,2-ethanediol)* | *Viscosity (Pa·s)* |
|---|---|---|
| WM_Q#2_Table#1_Row#1 | 「0」 | 「0.0008385」 |
| WM_Q#2_Table#1_Row#2 | 「0.0494」 | 「0.0011644」 |
| WM_Q#2_Table#1_Row#3 | 「0.0986」 | 「0.001555」 |
| WM_Q#2_Table#1_Row#4 | 「0.1483」 | 「0.0019899」 |
| WM_Q#2_Table#1_Row#5 | 「0.2072」 | 「0.0025643」 |
| WM_Q#2_Table#1_Row#6 | 「0.2466」 | 「0.0029649」 |
| WM_Q#2_Table#1_Row#7 | 「0.3399」 | 「0.0040293」 |
| WM_Q#2_Table#1_Row#8 | 「0.3921」 | 「0.0046704」 |
| WM_Q#2_Table#1_Row#9 | 「0.4446」 | 「0.0053492」 |
| WM_Q#2_Table#1_Row#10 | 「0.5485」 | 「0.0067709」 |
| WM_Q#2_Table#1_Row#11 | 「0.6451」 | 「0.0081729」 |
| WM_Q#2_Table#1_Row#12 | 「0.7012」 | 「0.0090846」 |
| WM_Q#2_Table#1_Row#13 | 「0.7435」 | 「0.0098077」 |
| WM_Q#2_Table#1_Row#14 | 「0.7907」 | 「0.010548」 |
| WM_Q#2_Table#1_Row#15 | 「0.8505」 | 「0.011535」 |
| WM_Q#2_Table#1_Row#16 | 「1」 | 「0.013867」 |

*(Shape-preserving subset of 21 matched rows at 303.15 K; viscosity ranges from 0.0008385 to 0.013867 Pa·s.)*

---

##### Dataset 2 — DOI: 10.1021/acs.jced.6b00526 · Block PROPblock_18

**Method:** Falling sphere viscometry · **Pressure:** 100.0 kPa · **Composition variable:** mole fraction of water

**WM_Q#2_Table#2_(Main_Q#2_Answer):**

| *row_id* | *x(water)* | *Viscosity (Pa·s)* |
|---|---|---|
| WM_Q#2_Table#2_Row#1 | 「0」 | 「0.01423」 |
| WM_Q#2_Table#2_Row#2 | 「0.1105」 | 「0.01186」 |
| WM_Q#2_Table#2_Row#3 | 「0.2014」 | 「0.01014」 |
| WM_Q#2_Table#2_Row#4 | 「0.3002」 | 「0.00845」 |
| WM_Q#2_Table#2_Row#5 | 「0.4011」 | 「0.006968」 |
| WM_Q#2_Table#2_Row#6 | 「0.4969」 | 「0.005653」 |
| WM_Q#2_Table#2_Row#7 | 「0.6022」 | 「0.004396」 |
| WM_Q#2_Table#2_Row#8 | 「0.6995」 | 「0.003345」 |
| WM_Q#2_Table#2_Row#9 | 「0.7994」 | 「0.002328」 |
| WM_Q#2_Table#2_Row#10 | 「0.8997」 | 「0.001446」 |
| WM_Q#2_Table#2_Row#11 | 「1」 | 「0.000755」 |

*(Complete isotherm — all 11 data points at 303.15 K.)*

---

##### Compounds

**WM_Q#2_Table#3_(Main_Q#2_Answer):**

| *row_id* | *Component* | *Formula* | *InChIKey* |
|---|---|---|---|
| WM_Q#2_Table#3_Row#1 | 「Water」 | 「H₂O」 | 「XLYOFNOQVPJJNP-UHFFFAOYSA-N」 |
| WM_Q#2_Table#3_Row#2 | 「1,2-Ethanediol (ethylene glycol)」 | 「C₂H₆O₂」 | 「LYCAIKOWRPUZTN-UHFFFAOYSA-N」 |

---

##### Chemistry Insight

Both datasets show a **monotonic increase** in viscosity with increasing ethylene glycol content. At 303.15 K:

- **Pure water:** 0.0008385 Pa·s (Dataset 1) / 0.000755 Pa·s (Dataset 2)
- **Pure ethylene glycol:** 0.013867 Pa·s (Dataset 1) / 0.01423 Pa·s (Dataset 2)

Pure ethylene glycol is roughly **17–19 times more viscous** than pure water at this temperature. This large difference arises because ethylene glycol has two hydroxyl groups that form an extensive intermolecular hydrogen-bonding network, creating much stronger cohesive interactions than water alone.

The viscosity–composition curve is **concave upward** (positive deviation from a simple linear mixing rule), which is characteristic of strongly associating aqueous–diol mixtures. The two datasets, measured by different techniques (concentric cylinders vs. falling sphere) and at slightly different pressures (92.3 vs. 100.0 kPa), are in good mutual agreement, lending confidence to the reported values.

Three additional ThermoML literature sources were also identified for this system and could provide further comparison data if needed.

**Core claims:**
- Two independent ThermoML datasets provide dynamic viscosity data for the water + 1,2-ethanediol (ethylene glycol) binary mixture at exactly 303.15 K, covering the full composition range.
- Dataset 1 (DOI: 10.1016/j.jct.2018.02.022, concentric cylinders viscometry, 92.3 kPa) reports viscosity ranging from 0.0008385 Pa·s (pure water) to 0.013867 Pa·s (pure ethylene glycol) as a function of 1,2-ethanediol mole fraction.
- Dataset 2 (DOI: 10.1021/acs.jced.6b00526, falling sphere viscometry, 100.0 kPa) reports viscosity ranging from 0.000755 Pa·s (pure water) to 0.01423 Pa·s (pure ethylene glycol) as a function of water mole fraction.
- Both datasets show a monotonic increase in viscosity with increasing ethylene glycol content at 303.15 K, with the viscosity–composition curve described as concave upward (positive deviation from linear mixing), characteristic of strongly associating aqueous–diol mixtures.
- The two datasets, measured by different techniques and at slightly different pressures (92.3 vs. 100.0 kPa), are reported to be in good mutual agreement.

**Sources:**

**WM_Q#2_Table#4_(Main_Q#2_Sources):**

| *row_id* | *lit_num_id* | *block* | *doi* | *BLKsubsys_id* | *description* |
|---|---|---|---|---|---|
| WM_Q#2_Table#4_Row#1 | 「GLOBlit_5201」 | 「PROPblock_24」 | 「10.1016/j.jct.2018.02.022」 | 「—」 | 「Provides dynamic viscosity of the water + 1,2-ethanediol binary system measured by concentric cylinders viscometry at 92.3 kPa. The block covers 293.15–308.15 K and mole fractions 0–1, so the 303.15 K isotherm extracted in the answer (viscosity 0.0008385–0.013867 Pa·s) falls squarely within its ranges.」 |
| WM_Q#2_Table#4_Row#2 | 「GLOBlit_6951」 | 「PROPblock_18」 | 「10.1021/acs.jced.6b00526」 | 「—」 | 「Provides dynamic viscosity of the water + 1,2-ethanediol binary system measured by falling sphere viscometry at 100.0 kPa. The temperature range extends to 303.15 K and mole fraction spans 0–1, supplying the 11-point isotherm (0.000755–0.01423 Pa·s) reported in the answer.」 |

*Not stored here: 2 verbatim data_inspections table(s); 3 id_catalog_snapshot row(s) (catalog is merged separately). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


### Parallel Compaction Reports

#### Compaction 1
**Philosophy (agentic, targets ALL, philosophy elicited):** Retain for each binary system: DOIs, compound names, temperature(s), and the full set of viscosity vs. mole-fraction data points (numerical values of x and η in mPa·s). Keep any noted deviations from ideal mixing or viscosity extrema. Drop raw XML snippets, redundant metadata, block-level structural details, and any commentary not directly conveying data values or source identifiers.

##### [MeOH_EtOH_visc]
**Summary:** Dynamic viscosity data for methanol + ethanol at 303.15 K found in DOI **10.1021/je800633a**, block **PROPblock_16** (GLOBlit_11337). Twelve points span x(methanol) = 0.0417–0.9166; viscosity decreases monotonically (nearly linearly), indicating near-ideal mixing.

**Source:** DOI `10.1021/je800633a` | `GLOBlit_11337` | `PROPblock_16` | T = 303.15 K | P = 81.5 kPa | Capillary tube (Ostwald–Ubbelohde)

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

**Notes:** Viscosity decreases monotonically from the ethanol

##### [ACN_DMF_visc]
Two ThermoML sources provide dynamic viscosity for **acetonitrile (GLOBcomp_15) + N,N-dimethylformamide (GLOBcomp_18)** at 303.15 K across the full composition range; viscosity increases monotonically from ~0.32 mPa·s (pure ACN) to ~0.77 mPa·s (pure DMF).

### Source 1 — Mass-fraction basis
**DOI:** 10.1016/j.jct.2014.02.019 | **GLOBlit_4124** | **PROPblock_6** | P = 101.0 kPa

| w(DMF) | η (Pa·s) |
|--------|-----------|
| 0 | 0.0003269 |
| 0.25 | 0.0003598 |
| 0.50 | 0.00046 |
| 0.75 | 0.0006145 |
| 1.00 | 0.000755 |

### Source 2 — Mole-fraction basis (recommended)
**DOI:** 10.1021/acs.jced.8b00176 | **GLOBlit_7481** | **PROPblock_18** | P = 100.0 kPa

| x(DMF) | η (Pa·s) |
|--------|-----------|
|

##### [Water_EG_visc]
Two independent ThermoML datasets provide dynamic viscosity of water (GLOBcomp_1) + 1,2-ethanediol (GLOBcomp_24) at exactly 303.15 K, covering the full composition range. Viscosity increases monotonically with ethylene glycol content.

**Dataset 1 — DOI: 10.1016/j.jct.2018.02.022 · GLOBlit_5201 · PROPblock_24 · 92.3 kPa**

| x(EG) | η (Pa·s) |
|--------|-----------|
| 0 | 0.0008385 |
| 0.0494 | 0.0011644 |
| 0.0986 | 0.001555 |
| 0.1483 | 0.0019899 |
| 0.2072 | 0.0025643 |
| 0.2466 | 0.0
</memory>

## User
At 30 °C, which mixture—methanol + ethanol, acetonitrile + N,N-dimethylformamide, or water + ethylene glycol—departs most strongly from ideal viscosity across composition, and what does the ordering reveal about molecular interactions in the three liquids?

## Assistant
<summary>Starting parallel searches for viscosity data at 30°C for three binary systems: methanol+ethanol, acetonitrile+DMF, and water+ethylene glycol. Will then analyze deviations from ideal mixing.</summary>
<tool_call>run_parallel_subagents()</tool_call>

## User
<tool_result>
**Parallel dispatch** — 3 task(s); combined results 53,708 chars exceeded the 50,000-char single-pass limit, so all tasks were auto-compacted under this philosophy (elicited): Retain for each binary system: DOIs, compound names, temperature(s), and the full set of viscosity vs. mole-fraction data points (numerical values of x and η in mPa·s). Keep any noted deviations from ideal mixing or viscosity extrema. Drop raw XML snippets, redundant metadata, block-level structural details, and any commentary not directly conveying data values or source identifiers.
Full JSON results are recorded in working memory.

## Consolidated Viscosity Data for Three Binary Systems at 303.15 K

All three systems returned usable ThermoML data. Two datasets (ACN+DMF Source 2, Water+EG Dataset 1) are **truncated** in the returned output — partial data preserved below; full JSON is in working memory.

---

### [MeOH_EtOH_visc]
**DOI:** `10.1021/je800633a` | `GLOBlit_11337` | `PROPblock_16` | T = 303.15 K | P = 81.5 kPa | 12 pts

| x(MeOH) | η (Pa·s) |
|----------|-----------|
| 0.0417 | 0.000968 |
| 0.1476 | 0.000906 |
| 0.2214 | 0.000865 |
| 0.2952 | 0.000828 |
| 0.3644 | 0.000793 |
| 0.4488 | 0.000753 |
| 0.529 | 0.000717 |
| 0.5995 | 0.000685 |
| 0.6859 | 0.000648 |
| 0.7442 | 0.000624
</tool_result>

## Assistant


<reasoning>
I have all the data I need from the working memory. Let me now compute the viscosity deviations from ideal mixing for each system.

For ideal viscosity mixing, I'll use the simple linear mixing rule on a mole-fraction basis:
η_ideal = x₁·η₁ + x₂·η₂

where η₁ and η₂ are the pure-component viscosities.

Let me compute Δη = η_measured - η_ideal for each system and find the maximum absolute deviation and the relative deviation.

### System 1: Methanol + Ethanol at 303.15 K
Pure ethanol (x_MeOH → 0): need to extrapolate. The data starts at x_MeOH = 0.0417. Let me use the endpoints available.
Actually, we don't have pure component values (x=0 and x=1). Let me use the data we have and estimate.

From the data:
- x_MeOH = 0.0417, η = 0.000968 → near pure ethanol
- x_MeOH = 0.9166, η = 0.000556 → near pure methanol

I can estimate pure component values by extrapolation, but that's risky. Let me just use the available data points and compute deviations using the two extreme points as pseudo-endpoints.

η_EtOH ≈ 0.000968 at x_MeOH=0.0417 (close to pure ethanol)
η_MeOH ≈ 0.000556 at x_MeOH=0.9166 (close to pure methanol)

Actually, for a fair comparison, let me use a different approach. Let me compute the fractional deviation from linearity between the two endpoints of each dataset.

For MeOH+EtOH: endpoints x=0.0417 (η=0.000968) and x=0.9166 (η=0.000556)
Linear interpolation between these: η_linear(x) = 0.000968 + (x - 0.0417)/(0.9166 - 0.0417) × (0.000556 - 0.000968)

Let me compute at each point:
Slope = (0.000556 - 0.000968)/(0.9166 - 0.0417) = -0.000412/0.8749 = -0.000471 per unit x

At x=0.2214: η_linear = 0.000968 + (0.2214-0.0417)×(-0.000471) = 0.000968 - 0.1797×0.000471 = 0.000968 - 0.0000846 = 0.000883
η_measured = 0.000865, Δη = 0.000865 - 0.000883 = -0.000018, relative = -2.0%

At x=0.4488: η_linear = 0.000968 + (0.4488-0.0417)×(-0.000471) = 0.000968 - 0.4071×0.000471 = 0.000968 - 0.000192 = 0.000776
η_measured = 0.000753, Δη = -0.000023, relative = -3.0%

At x=0.529: η_linear = 0.000968 - 0.4873×0.000471 = 0.000968 - 0.000230 = 0.000738
η_measured = 0.000717, Δη = -0.000021, relative = -2.8%

At x=0.6859: η_linear = 0.000968 - 0.6442×0.000471 = 0.000968 - 0.000303 = 0.000665
η_measured = 0.000648, Δη = -0.000017, relative = -2.6%

So maximum deviation is about -3% around x_MeOH ≈ 0.45. Very small, nearly ideal.

### System 2: ACN + DMF at 303.15 K (Source 2, mole-fraction basis)
Pure ACN: x_DMF = 0, η = 0.00032
Pure DMF: x_DMF = 1, η = 0.00077

Linear: η_ideal(x) = 0.00032 + x × (0.00077 - 0.00032) = 0.00032 + 0.00045x

At x_DMF = 0.0989: η_ideal = 0.00032 + 0.00045×0.0989 = 0.00032 + 0.0000445 = 0.000365
η_measured = 0.00039, Δη = +0.000025, relative = +6.8%

At x_DMF = 0.1916: η_ideal = 0.00032 + 0.00045×0.1916 = 0.00032 + 0.0000862 = 0.000406
η_measured = 0.00042, Δη = +0.000014, relative = +3.4%

At x_DMF = 0.2925: η_ideal = 0.00032 + 0.00045×0.2925 = 0.00032 + 0.000132 = 0.000452
η_measured = 0.00046, Δη = +0.000008, relative = +1.8%

At x_DMF = 0.3932: η_ideal = 0.00032 + 0.00045×0.3932 = 0.00032 + 0.000177 = 0.000497
η_measured = 0.00051, Δη = +0.000013, relative = +2.6%

At x_DMF = 0.5029: η_ideal = 0.00032 + 0.00045×0.5029 = 0.00032 + 0.000226 = 0.000546
η_measured = 0.00057, Δη = +0.000024, relative = +4.4%

At x_DMF = 0.6002: η_ideal = 0.00032 + 0.00045×0.6002 = 0.00032 + 0.000270 = 0.000590
η_measured = 0.00061, Δη = +0.000020, relative = +3.4%

At x_DMF = 0.6931: η_ideal = 0.00032 + 0.00045×0.6931 = 0.00032 + 0.000312 = 0.000632
η_measured = 0.00065, Δη = +0.000018, relative = +2.8%

At x_DMF = 0.7926: η_ideal = 0.00032 + 0.00045×0.7926 = 0.00032 + 0.000357 = 0.000677
η_measured = 0.00070, Δη = +0.000023, relative = +3.4%

At x_DMF = 0.8996: η_ideal = 0.00032 + 0.00045×0.8996 = 0.00032 + 0.000405 = 0.000725
η_measured = 0.00075, Δη = +0.000025, relative = +3.4%

Maximum deviation: ~+6.8% at x_DMF = 0.0989, but that's at the dilute end. Around the middle, it's about +4.4% at x_DMF ≈ 0.5. Positive deviations throughout — slightly more viscous than ideal.

Hmm, wait. Let me reconsider. The deviation at x_DMF=0.0989 seems high but it's at a low composition. Let me check: η_ideal = 0.000365, η_measured = 0.00039. That's a difference of 0.000025 Pa·s. The absolute deviation is small but relative is notable.

Actually, for viscosity, a more physically meaningful mixing rule is the logarithmic one (Arrhenius):
ln(η_ideal) = x₁·ln(η₁) + x₂·ln(η₂)

This is more commonly used for viscosity. Let me redo the calculations with this.

### Using logarithmic (Arrhenius) mixing rule:

#### System 1: MeOH + EtOH
I don't have pure component values. Let me estimate from the data.
Actually, I should note that the data doesn't include x=0 or x=1. But the near-linear behavior suggests deviations would be small regardless.

Let me use the ACN+DMF and Water+EG systems where I have pure component data.

#### System 2: ACN + DMF
η_ACN = 0.00032, η_DMF = 0.00077
ln(η_ACN) = ln(0.00032) = -8.047
ln(η_DMF) = ln(0.00077) = -7.170

At x_DMF = 0.5029:
ln(η_ideal) = (1-0.5029)×(-8.047) + 0.5029×(-7.170) = 0.4971×(-8.047) + 0.5029×(-7.170)
= -3.999 + (-3.606) = -7.605
η_ideal = exp(-7.605) = 0.000496
η_measured = 0.00057
Δη = +0.000074, relative = +14.9%

That's more significant! Let me check other points.

At x_DMF = 0.0989:
ln(η_ideal) = 0.9011×(-8.047) + 0.0989×(-7.170) = -7.251 + (-0.709) = -7.960
η_ideal = exp(-7.960) = 0.000348
η_measured = 0.00039
Δη = +0.000042, relative = +12.1%

At x_DMF = 0.3932:
ln(η_ideal) = 0.6068×(-8.047) + 0.3932×(-7.170) = -4.883 + (-2.820) = -7.703
η_ideal = exp(-7.703) = 0.000450
η_measured = 0.00051
Δη = +0.000060, relative = +13.3%

So with the Arrhenius mixing rule, ACN+DMF shows about 12-15% positive deviation.

#### System 3: Water + EG
Using Dataset 2 (mole fraction of water basis):
η_water (pure, x_water=1) = 0.000755
η_EG (pure, x_water=0) = 0.01423

ln(η_water) = ln(0.000755) = -7.189
ln(η_EG) = ln(0.01423) = -4.253

At x_water = 0.4969 (x_EG = 0.5031):
ln(η_ideal) = 0.4969×(-7.189) + 0.5031×(-4.253) = -3.572 + (-2.140) = -5.712
η_ideal = exp(-5.712) = 0.00331
η_measured = 0.005653
Δη = +0.002343, relative = +70.8%

At x_water = 0.6995 (x_EG = 0.3005):
ln(η_ideal) = 0.6995×(-7.189) + 0.3005×(-4.253) = -5.029 + (-1.278) = -6.307
η_ideal = exp(-6.307) = 0.001821
η_measured = 0.003345
Δη = +0.001524, relative = +83.7%

At x_water = 0.7994 (x_EG = 0.2006):
ln(η_ideal) = 0.7994×(-7.189) + 0.2006×(-4.253) = -5.747 + (-0.853) = -6.600
η_ideal = exp(-6.600) = 0.001360
η_measured = 0.002328
Δη = +0.000968, relative = +71.2%

At x_water = 0.3002 (x_EG = 0.6998):
ln(η_ideal) = 0.3002×(-7.189) + 0.6998×(-4.253) = -2.158 + (-2.977) = -5.135
η_ideal = exp(-5.135) = 0.00589
η_measured = 0.00845
Δη = +0.00256, relative = +43.5%

So the maximum deviation for Water+EG is around +70-84% using the Arrhenius rule! This is enormously larger than the other two systems.

Let me also do MeOH+EtOH with the Arrhenius rule. I'll need to estimate pure component viscosities. From the literature at 303.15 K:
- Pure ethanol viscosity ≈ 0.001 Pa·s (the data shows 0.000968 at x_MeOH=0.0417, so pure EtOH ≈ 0.00100)
- Pure methanol viscosity ≈ 0.00051 Pa·s (the data shows 0.000556 at x_MeOH=0.9166, so pure MeOH ≈ 0.00052)

Actually, I should be careful not to use values I don't have. Let me just use the two extreme data points as pseudo-endpoints.

η₁ (x_MeOH=0.0417) = 0.000968
η₂ (x_MeOH=0.9166) = 0.000556

For a point in the middle, say x_MeOH = 0.4488:
Relative position: (0.4488-0.0417)/(0.9166-0.0417) = 0.4071/0.8749 = 0.4653

Using Arrhenius between the two endpoints:
ln(η₁) = ln(0.000968) = -6.940
ln(η₂) = ln(0.000556) = -7.495

ln(η_ideal) = (1-0.4653)×(-6.940) + 0.4653×(-7.495) = 0.5347×(-6.940) + 0.4653×(-7.495)
= -3.711 + (-3.489) = -7.200
η_ideal = exp(-7.200) = 0.000749
η_measured = 0.000753
Δη = +0.000004, relative = +0.5%

Essentially zero deviation! This confirms MeOH+EtOH is nearly ideal.

So the ordering is clear:
1. **Water + Ethylene Glycol**: ~70-84% positive deviation (Arrhenius rule) — by far the largest
2. **Acetonitrile + DMF**: ~12-15% positive deviation — moderate
3. **Methanol + Ethanol**: ~0.5-3% deviation — nearly ideal

This makes perfect physical sense:
- Water + EG: Both are strong hydrogen-bond donors and acceptors. EG has two OH groups that can cross-link with water, creating an extensive, cooperative H-bond network that dramatically increases viscosity beyond what simple mixing would predict.
- ACN + DMF: Both are polar aprotic solvents. DMF is a strong H-bond acceptor (C=O), and ACN has a weakly acidic C-H that can interact with DMF's carbonyl. The positive deviation suggests some synergistic dipole-dipole interactions.
- MeOH + EtOH: Both are small aliphatic alcohols with very similar H-bonding capabilities. Replacing one with the other barely disrupts the H-bond network, so mixing is nearly ideal.

Now I have all the data and analysis. Let me present the final answer. I should be careful to note which calculations I performed myself from the subagent-returned data points.

Actually, I want to also use Dataset 1 for Water+EG to cross-check, since it has more points in the water-rich region.

Dataset 1 (x_EG basis):
η_water (x_EG=0) = 0.0008385
η_EG (x_EG=1) = 0.013867

ln(0.0008385) = -7.084
ln(0.013867) = -4.278

At x_EG = 0.2072:
ln(η_ideal) = 0.7928×(-7.084) + 0.2072×(-4.278) = -5.618 + (-0.886) = -6.504
η_ideal = exp(-6.504) = 0.001499
η_measured = 0.0025643
Δη = +0.001065, relative = +71.1%

At x_EG = 0.4446:
ln(η_ideal) = 0.5554×(-7.084) + 0.4446×(-4.278) = -3.935 + (-1.902) = -5.837
η_ideal = exp(-5.837) = 0.002926
η_measured = 0.0053492
Δη = +0.002423, relative = +82.8%

At x_EG = 0.5485:
ln(η_ideal) = 0.4515×(-7.084) + 0.5485×(-4.278) = -3.198 + (-2.347) = -5.545
η_ideal = exp(-5.545) = 0.003916
η_measured = 0.0067709
Δη = +0.002855, relative = +72.9%

At x_EG = 0.3399:
ln(η_ideal) = 0.6601×(-7.084) + 0.3399×(-4.278) = -4.676 + (-1.454) = -6.130
η_ideal = exp(-6.130) = 0.002176
η_measured = 0.0040293
Δη = +0.001853, relative = +85.2%

Maximum deviation around x_EG ≈ 0.34, about +85%. This is consistent with Dataset 2.

Great, I have a thorough analysis. Let me present the final answer now.

Let me also compute the deviation for the linear mixing rule for Water+EG to show both perspectives:

Linear: η_ideal = (1-x_EG)×0.0008385 + x_EG×0.013867

At x_EG = 0.3399:
η_ideal = 0.6601×0.0008385 + 0.3399×0.013867 = 0.000554 + 0.004714 = 0.005268
η_measured = 0.0040293
Δη = -0.001239, relative = -23.5% (negative! because linear overestimates)

Interesting — with the linear rule, the deviation is negative (the measured viscosity is LESS than the linear prediction). This is because the linear mixing rule overestimates when one component is much more viscous. The Arrhenius (logarithmic) rule is more physically appropriate for viscosity.

Actually, this is an important point. For viscosity, the Arrhenius mixing rule is the standard "ideal" reference:
ln(η_mix) = Σ xᵢ ln(ηᵢ)

The positive deviations from this rule indicate that the mixture is MORE viscous than the geometric mean prediction, which is the signature of strong cross-interactions (like H-bonding between unlike molecules).

Let me present the final answer with clear calculations.

I need to be careful about the MeOH+EtOH system since I don't have pure component values. Let me note this limitation. But the near-zero deviation between the available endpoints is strong evidence of near-ideal behavior.

Let me write the final answer now.
</reasoning>

<summary>
All three viscosity datasets are in working memory. I'll now compute deviations from ideal (Arrhenius) mixing for each system using the subagent-returned data points, then synthesize the final comparative answer. Water+EG shows ~70-85% positive deviation, ACN+DMF ~12-15%, MeOH+EtOH <1% — clear ordering driven by H-bonding cross-interactions.
</summary>

<answer>

## Viscosity Deviations from Ideal Mixing at 303.15 K (≈ 30 °C): A Three-System Comparison

### Short answer

**Water + ethylene glycol** departs most strongly from ideal viscosity — by a wide margin. The ordering of non-ideality is:

> **Water + ethylene glycol ≫ acetonitrile + DMF > methanol + ethanol ≈ ideal**

This ranking directly mirrors the strength and cooperativity of cross-species hydrogen bonding in each mixture.

---

### 1. Data sources

All viscosity-versus-composition data at 303.15 K come from ThermoML:

| System | Literature ID | DOI | Block | Points | Method | P (kPa) |
|--------|--------------|-----|-------|--------|--------|---------|
| Methanol + Ethanol | GLOBlit_11337 | 10.1021/je800633a | PROPblock_16 | 12 | Capillary (Ostwald–Ubbelohde) | 81.5 |
| Acetonitrile + DMF | GLOBlit_7481 | 10.1021/acs.jced.8b00176 | PROPblock_18 | 11 | Falling/rolling sphere | 100.0 |
| Water + Ethylene glycol (Dataset 1) | GLOBlit_5201 | 10.1016/j.jct.2018.02.022 | PROPblock_24 | 16 | Concentric cylinders | 92.3 |
| Water + Ethylene glycol (Dataset 2) | GLOBlit_6951 | 10.1021/acs.jced.6b00526 | PROPblock_18 | 11 | Falling sphere | 100.0 |

---

### 2. Ideal-mixing reference

For liquid viscosity, the standard "ideal" benchmark is the **Arrhenius (logarithmic) mixing rule**:

> ln η_ideal = x₁ ln η₁* + x₂ ln η₂*

where η₁* and η₂* are the pure-component viscosities. The **viscosity deviation** is then Δη = η_measured − η_ideal. A positive Δη means the mixture is *more viscous* than the geometric-mean prediction — the hallmark of strong cross-interactions.

---

### 3. Computed deviations

#### 3a. Methanol + Ethanol — nearly ideal

Pure-component endpoints are not in the dataset (data span x_MeOH = 0.0417–0.9166), so the Arrhenius interpolation is anchored at the two extreme measured points (η = 0.000968 Pa·s at x_MeOH = 0.0417; η = 0.000556 Pa·s at x_MeOH = 0.9166). Representative mid-range check:

| x(MeOH) | η_measured (Pa·s) | η_Arrhenius (Pa·s) | Relative deviation |
|----------|-------------------|---------------------|--------------------|
| 0.4488 | 0.000753 | 0.000749 | **+0.5%** |
| 0.529 | 0.000717 | 0.000722 | −0.7% |
| 0.5995 | 0.000685 |

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **UNINSPECTED_BLOCK** PROPblock_16 + PROPblock_18 + PROPblock_24: PROPblock_16 + PROPblock_18 + PROPblock_24 is quoted with data values (81.5, 100.0, 16, 92.3, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_16", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_18", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_24", literature="<GLOBlit_N or DOI>")`
- **UNINSPECTED_BLOCK** PROPblock_24: PROPblock_24 is quoted with data values (0.0417, 0.9166, 0.000968, 0.0417, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_24", literature="<GLOBlit_N or DOI>")`
- **UNINSPECTED_BLOCK** PROPblock_24: PROPblock_24 is quoted with data values (0.4488, 0.000753, 0.000749, 0.529, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_24", literature="<GLOBlit_N or DOI>")`

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

## Assistant
<summary>Need to inspect all four blocks cited in my answer to ground the data values. Running inspect_block_table for PROPblock_16/GLOBlit_11337, PROPblock_18/GLOBlit_7481, PROPblock_24/GLOBlit_5201, and PROPblock_18/GLOBlit_6951.</summary>
<tool_call>run_subagent_tool(tool_name=inspect_block_table, kwargs={'block_number': …)</tool_call>

## User
<tool_result>
**Summary:** PROPblock_16 (DOI: 10.1021/je800633a [GLOBlit_11337]) contains 12 viscosity data points for ethanol + methanol at T = 303.15 K and P = 81.5 kPa. Viscosity decreases monotonically from 0.000968 to 0.000556 Pa·s as methanol mole fraction increases from 0.0417 to 0.9166 (near-linear, R² = 0.9960).

| BLKpoint_id | x(methanol) | T (K) | P (kPa) | η (Pa·s) |
|---|---|---|---|---|
| BLKpoint_1 | 0.0417 | 303.15 | 81.5 | 0.000968 |
| BLKpoint_2 | 0.1476 | 303.15 | 81.5 | 0.000906 |
| BLKpoint_3 | 0.2214 | 303.15 | 81.5 | 0.000865 |
| BLKpoint_4 | 0.2952 | 303.15 | 81.5 | 0.000828 |
| BLKpoint_5 | 0.3644 | 303.15 | 81.5 | 0.000793 |
| BLKpoint_6 | 0.4488 | 303.15 | 81.5 | 0.000753 |
| BLKpoint_7 | 0.529 | 303.15 | 81.5 | 0.000717 |
| BLKpoint_8 | 0.5995 | 303.15 | 81.5 | 0.000685 |
| BLKpoint_9 | 0.6859 | 303.15 | 81.5 | 0.000648 |
| BLKpoint_10 | 0.7442 | 303.15 | 81.5 | 0.000624 |
| BLKpoint_11 | 0.832 | 303.15 | 81.5 | 0.000588 |
| BLKpoint_12 | 0.9166 | 303.15 | 81.5 | 0.000556 |

**Key IDs:** DOI `10.1021/je800633a [GLOBlit_11337]
</tool_result>

## Assistant
<summary>PROPblock_16 inspection confirmed all 12 MeOH+EtOH data points. Now need to inspect the remaining 3 blocks: PROPblock_18/GLOBlit_7481 (ACN+DMF), PROPblock_24/GLOBlit_5201 (Water+EG), and PROPblock_18/GLOBlit_6951 (Water+EG).</summary>
<tool_call>run_subagent_tool(tool_name=inspect_block_table, kwargs={'block_number': …)</tool_call>

## User
<tool_result>
**⚠ Tool `inspect_block_table` result discarded by subagent.**

1. **Explanation**: The query failed because the column alias `'T'` is not recognized. The block uses `temperature_k` as the alias for temperature.

2. **Refinement suggestion**: Retry `inspect_block_table` for `PROPblock_18` of `GLOBlit_7481` using the correct column alias in the `where` filter: `temperature_k = 303.15`. Available aliases are: `temperature_k`, `mole_fraction_dimethylformamide`, `pressure_kpa`, `viscosity_pa_s`.
</tool_result>

## Assistant
<summary>Filter alias error for PROPblock_18/GLOBlit_7481. Need to retry with correct column alias or no filter. Also need to inspect PROPblock_24/GLOBlit_5201 and PROPblock_18/GLOBlit_6951. Running all three inspections in parallel.</summary>
<tool_call>run_subagent_tool(tool_name=inspect_block_table, kwargs={'block_number': …)</tool_call>

## User
<tool_result>
**Summary:** PROPblock_18 (DOI: 10.1021/acs.jced.8b00176 [GLOBlit_7481]) contains 11 viscosity data points for dimethylformamide + acetonitrile at 303.15 K and 100.0 kPa, covering the full mole-fraction range of DMF (0 → 1). Viscosity increases monotonically from 0.00032 to 0.00077 Pa·s.

| BLKpoint_id | x(DMF) | viscosity (Pa·s) |
|---|---|---|
| BLKpoint_12 | 0 | 0.00032 |
| BLKpoint_13 | 0.0989 | 0.00039 |
| BLKpoint_14 | 0.1916 | 0.00042 |
| BLKpoint_15 | 0.2925 | 0.00046 |
| BLKpoint_16 | 0.3932 | 0.00051 |
| BLKpoint_17 | 0.5029 | 0.00057 |
| BLKpoint_18 | 0.6002 | 0.00061 |
| BLKpoint_19 | 0.6931 | 0.00065 |
| BLKpoint_20 | 0.7926 | 0.0007 |
| BLKpoint_21 | 0.8996 | 0.00075 |
| BLKpoint_22 | 1 | 0.00077 |

All at T = 303.15 K, P = 100.0 kPa. Source: DOI 10.1021/acs.jced.8b00176 [GLOBlit_7481], PROPblock_18 (inspection: INSP_0a0742d5bd6a).
</tool_result>

## Assistant
<summary>PROPblock_18/GLOBlit_7481 (ACN+DMF) confirmed with 11 points at 303.15 K, 100.0 kPa. Now need to inspect the two Water+EG blocks: PROPblock_24/GLOBlit_5201 and PROPblock_18/GLOBlit_6951.</summary>
<tool_call>run_subagent_tool(tool_name=inspect_block_table, kwargs={'block_number': …)</tool_call>

## User
<tool_result>
**Summary:** PROPblock_24 (GLOBlit_5201, DOI 10.1016/j.jct.2018.02.022) contains 21 data points for viscosity of 1,2-ethanediol + water at 303.15 K and 92.3 kPa, spanning the full composition range (x_EG = 0–1). 16 of 21 rows shown via RDP sampling; viscosity ranges from 0.0008385 Pa·s (pure water) to 0.013867 Pa·s (pure EG).

| BLKpoint_id | x(EG) | viscosity_pa_s |
|---|---|---|
| BLKpoint_79 | 0 | 0.0008385 |
| BLKpoint_39 | 0.0494 | 0.0011644 |
| BLKpoint_40 | 0.0986 | 0.001555 |
| BLKpoint_41 | 0.1483 | 0.0019899 |
| BLKpoint_42 | 0.2072 | 0.0025643 |
| BLKpoint_43 | 0.2466 | 0.0029649 |
| BLKpoint_45 | 0.3399 | 0.0040293 |
| BLKpoint_46 | 0.3921 | 0.0046704 |
| BLKpoint_47 | 0.4446 | 0.0053492 |
| BLKpoint_49 | 0.5485 | 0.0067709 |
| BLKpoint_51 | 0.6451 | 0.0081729 |
| BLKpoint_52 | 0.7012 | 0.0090846 |
| BLKpoint_53 | 0.7435 | 0.0098077 |
| BLKpoint_54 | 0.7907 | 0.010548 |
| BLKpoint_55 | 0.8505 | 0.011535 |
| BLKpoint_83 | 1 | 0.013867 |

All at T = 303.15 K, P =
</tool_result>

## Assistant
<summary>PROPblock_24/GLOBlit_5201 (Water+EG Dataset 1) confirmed with 16 shown points at 303.15 K, 92.3 kPa. Now need to inspect the last block: PROPblock_18/GLOBlit_6951 (Water+EG Dataset 2).</summary>
<tool_call>run_subagent_tool(tool_name=inspect_block_table, kwargs={'block_number': …)</tool_call>

## User
<tool_result>
**Summary:** The `inspect_block_table` call returned an error due to incorrect `nearest` parameter format, but it confirmed the block contains 33 data points with temperature range 293.15–303.15 K, water mole fraction 0–1, constant pressure 100 kPa, and viscosity 0.000755–0.02113 Pa·s. A retry is needed with proper filtering.

**Block metadata:**

| alias | n_finite | min | max |
|---|---|---|---|
| temperature_k | 33 | 293.15 | 303.15 |
| mole_fraction_water | 33 | 0 | 1 |
| pressure_kpa | 33 | 100 | 100 |
| viscosity_pa_s | 33 | 0.000755 | 0.02113 |

**Refinement:** Retry `inspect_block_table` using a `where` filter like `{"column": "temperature_k", "value": 303.15}` or use `nearest` with format `{"column": "temperature_k", "value": 303.15, "k": 8}` to extract data points at 303.15 K.
</tool_result>

## Assistant
<summary>Need to retry PROPblock_18/GLOBlit_6951 inspection with proper where filter to get the 303.15 K data points.</summary>
<tool_call>run_subagent_tool(tool_name=inspect_block_table, kwargs={'block_number': …)</tool_call>

## User
<tool_result>
**Summary:** PROPblock_18 (DOI 10.1021/acs.jced.6b00526, GLOBlit_6951) contains 11 viscosity data points at 303.15 K for the binary system 1,2-ethanediol + water, spanning the full composition range (x_water = 0 to 1) at 100.0 kPa.

| BLKpoint_id | temperature_k | mole_fraction_water | pressure_kpa | viscosity_pa_s |
|---|---|---|---|---|
| BLKpoint_23 | 303.15 | 0 | 100.0 | 0.01423 |
| BLKpoint_24 | 303.15 | 0.1105 | 100.0 | 0.01186 |
| BLKpoint_25 | 303.15 | 0.2014 | 100.0 | 0.01014 |
| BLKpoint_26 | 303.15 | 0.3002 | 100.0 | 0.00845 |
| BLKpoint_27 | 303.15 | 0.4011 | 100.0 | 0.006968 |
| BLKpoint_28 | 303.15 | 0.4969 | 100.0 | 0.005653 |
| BLKpoint_29 | 303.15 | 0.6022 | 100.0 | 0.004396 |
| BLKpoint_30 | 303.15 | 0.6995 | 100.0 | 0.003345 |
| BLKpoint_31 | 303.15 | 0.7994 | 100.0 | 0.002328 |
| BLKpoint_32 | 303.15 | 0.8997 | 100.0 | 0.001446 |
| BLKpoint_33 | 303.15 | 1 | 100.0 | 0.000755 |

- **11 matched rows** out of 33 total in the block (full block spans 293.15–303.15 K).
- Viscosity range at 303.15 K: 0.000755–0.01423 Pa·s.
</tool_result>

## Assistant
<reasoning>
All four blocks are now inspected. Let me now write the final answer using only the inspected data values.

Let me recompute the deviations carefully using only inspected values.

**Arrhenius ideal mixing rule:** ln η_ideal = x₁ ln η₁* + x₂ ln η₂*

### System 1: Methanol + Ethanol (PROPblock_16, GLOBlit_11337)
No pure-component endpoints available (data spans x_MeOH = 0.0417–0.9166).
Using the two extreme inspected points as pseudo-endpoints:
- η at x_MeOH = 0.0417: 0.000968 Pa·s
- η at x_MeOH = 0.9166: 0.000556 Pa·s

ln(0.000968) = -6.9401
ln(0.000556) = -7.4955

For a point at x_MeOH = 0.4488:
Fractional position between endpoints: (0.4488-0.0417)/(0.9166-0.0417) = 0.4071/0.8749 = 0.4653
ln(η_ideal) = (1-0.4653)×(-6.9401) + 0.4653×(-7.4955) = 0.5347×(-6.9401) + 0.4653×(-7.4955)
= -3.7116 + -3.4886 = -7.2002
η_ideal = exp(-7.2002) = 0.000749
η_measured = 0.000753
Relative deviation = (0.000753 - 0.000749)/0.000749 = +0.5%

At x_MeOH = 0.529:
Fractional position: (0.529-0.0417)/(0.9166-0.0417) = 0.4873/0.8749 = 0.5570
ln(η_ideal) = 0.4430×(-6.9401) + 0.5570×(-7.4955) = -3.0745 + -4.1750 = -7.2495
η_ideal = exp(-7.2495) = 0.000713
η_measured = 0.000717
Relative deviation = (0.000717-0.000713)/0.000713 = +0.6%

### System 2: ACN + DMF (PROPblock_18, GLOBlit_7481)
Pure ACN (x_DMF=0): η = 0.00032 Pa·s
Pure DMF (x_DMF=1): η = 0.00077 Pa·s

ln(0.00032) = -8.0472
ln(0.00077) = -7.1701

At x_DMF = 0.5029:
ln(η_ideal) = 0.4971×(-8.0472) + 0.5029×(-7.1701) = -3.9987 + -3.6063 = -7.6050
η_ideal = exp(-7.6050) = 0.000497
η_measured = 0.00057
Relative deviation = (0.00057-0.000497)/0.000497 = +14.7%

At x_DMF = 0.3932:
ln(η_ideal) = 0.6068×(-8.0472) + 0.3932×(-7.1701) = -4.8830 + -2.8201 = -7.7031
η_ideal = exp(-7.7031) = 0.000450
η_measured = 0.00051
Relative deviation = (0.00051-0.000450)/0.000450 = +13.3%

At x_DMF = 0.6931:
ln(η_ideal) = 0.3069×(-8.0472) + 0.6931×(-7.1701) = -2.4697 + -4.9680 = -7.4377
η_ideal = exp(-7.4377) = 0.000590
η_measured = 0.00065
Relative deviation = (0.00065-0.000590)/0.000590 = +10.2%

### System 3: Water + Ethylene Glycol

**Dataset 1 (PROPblock_24, GLOBlit_5201):**
Pure water (x_EG=0): η = 0.0008385 Pa·s
Pure EG (x_EG=1): η = 0.013867 Pa·s

ln(0.0008385) = -7.0838
ln(0.013867) = -4.2782

At x_EG = 0.3399:
ln(η_ideal) = 0.6601×(-7.0838) + 0.3399×(-4.2782) = -4.6760 + -1.4541 = -6.1301
η_ideal = exp(-6.1301) = 0.002176
η_measured = 0.0040293
Relative deviation = (0.0040293-0.002176)/0.002176 = +85.2%

At x_EG = 0.4446:
ln(η_ideal) = 0.5554×(-7.0838) + 0.4446×(-4.2782) = -3.9347 + -1.9021 = -5.8368
η_ideal = exp(-5.8368) = 0.002926
η_measured = 0.0053492
Relative deviation = (0.0053492-0.002926)/0.002926 = +82.8%

At x_EG = 0.2072:
ln(η_ideal) = 0.7928×(-7.0838) + 0.2072×(-4.2782) = -5.6173 + -0.8864 = -6.5037
η_ideal = exp(-6.5037) = 0.001499
η_measured = 0.0025643
Relative deviation = (0.0025643-0.001499)/0.001499 = +71.1%

**Dataset 2 (PROPblock_18, GLOBlit_6951):**
Pure water (x_water=1): η = 0.000755 Pa·s
Pure EG (x_water=0): η = 0.01423 Pa·s

ln(0.000755) = -7.1892
ln(0.01423) = -4.2530

At x_water = 0.4969 (x_EG = 0.5031):
ln(η_ideal) = 0.4969×(-7.1892) + 0.5031×(-4.2530) = -3.5717 + -2.1397 = -5.7114
η_ideal = exp(-5.7114) = 0.003313
η_measured = 0.005653
Relative deviation = (0.005653-0.003313)/0.003313 = +70.6%

At x_water = 0.6995 (x_EG = 0.3005):
ln(η_ideal) = 0.6995×(-7.1892) + 0.3005×(-4.2530) = -5.0289 + -1.2780 = -6.3069
η_ideal = exp(-6.3069) = 0.001822
η_measured = 0.003345
Relative deviation = (0.003345-0.001822)/0.001822 = +83.6%

So the maximum deviations are:
- MeOH+EtOH: ~+0.5% (essentially zero)
- ACN+DMF: ~+15% (moderate)
- Water+EG: ~+85% (very large)

The ordering is clear and robust across both Water+EG datasets.

Now let me write the final answer.
</reasoning>

<answer>

## Viscosity Deviations from Ideal Mixing at 303.15 K (≈ 30 °C): A Three-System Comparison

### Short answer

**Water + ethylene glycol** departs most strongly from ideal viscosity — by a wide margin. The ordering of non-ideality is:

> **Water + ethylene glycol ≫ acetonitrile + DMF > methanol + ethanol ≈ ideal**

This ranking directly mirrors the strength and cooperativity of cross-species hydrogen bonding in each mixture.

---

### 1. Data sources

All viscosity-versus-composition data at 303.15 K come from ThermoML:

| System | Literature ID | DOI | Block | Points at 303.15 K | Method | P (kPa) |
|--------|--------------|-----|-------|---------------------|--------|---------|
| Methanol + Ethanol | GLOBlit_11337 | 10.1021/je800633a | PROPblock_16 | 12 | Capillary (Ostwald–Ubbelohde) | 81.5 |
| Acetonitrile + DMF | GLOBlit_7481 | 10.1021/acs.jced.8b00176 | PROPblock_18 | 11 | Falling/rolling sphere | 100.0 |
| Water + Ethylene glycol (Dataset 1) | GLOBlit_5201 | 10.1016/j.jct.2018.02.022 | PROPblock_24 | 16 (of 21 shown) | Concentric cylinders | 92.3 |
| Water + Ethylene glycol (Dataset 2) | GLOBlit_6951 | 10.1021/acs.jced.6b00526 | PROPblock_18 | 11 | Falling sphere | 100.0 |

---

### 2. Ideal-mixing reference

For liquid viscosity, the standard "ideal" benchmark is the **Arrhenius (logarithmic) mixing rule**:

> ln η\_ideal = x₁ · ln η₁\* + x₂ · ln η₂\*

where η₁\* and η₂\* are the pure-component viscosities. A positive deviation Δη = η\_measured − η\_ideal means the mixture is *more viscous* than the geometric-mean prediction — the hallmark of strong cross-interactions that retard molecular flow.

---

### 3. Computed deviations (derived from inspected data)

#### 3a. Methanol + Ethanol — nearly ideal

This dataset lacks pure-component endpoints (x\_MeOH spans 0.0417–0.9166), so the Arrhenius interpolation is anchored at the two extreme inspected points: η = 0.000968 Pa·s at x\_MeOH = 0.0417 and η = 0.000556 Pa·s at x\_MeOH = 0.9166.

| x(MeOH) | η\_measured (Pa·s) | η\_Arrhenius (Pa·s) | Relative deviation |
|----------|-------------------|---------------------|--------------------|
| 0.4488 | 0.000753 | 0.000749 (derived) | **+0.5%** |
| 0.529 | 0.000717 | 0.000713 (derived) | **+0.6%** |

**Maximum deviation: ≈ +0.5–0.6%** — essentially ideal mixing.

*(Source: PROPblock_16, GLOBlit_11337, inspected data; Arrhenius values derived by this agent from the inspected endpoint viscosities.)*

#### 3b. Acetonitrile + DMF — moderate positive deviation

Pure-component endpoints from inspected data: η\_ACN = 0.00032 Pa·s (x\_DMF = 0), η\_DMF = 0.00077 Pa·s (x\_DMF = 1).

| x(DMF) | η\_measured (Pa·s) | η\_Arrhenius (Pa·s) | Relative deviation |
|--------|-------------------|---------------------|--------------------|
| 0.3932 | 0.00051 | 0.000450 (derived) | **+13.3%** |
| 0.5029 | 0.00057 | 0.000497 (derived) | **+14.7%** |
| 0.6931 | 0.00065 | 0.000590 (derived) | **+10.2%** |

**Maximum deviation: ≈ +15%** at x\_DMF ≈ 0.5 — a clear, moderate positive departure.

*(Source: PROPblock_18, GLOBlit_7481, inspected data; Arrhenius values derived by this agent from the inspected pure-component viscosities.)*

#### 3c. Water + Ethylene Glycol — very large positive deviation

**Dataset 1** (PROPblock_24, GLOBlit_5201): η\_water = 0.0008385 Pa·s (x\_EG = 0), η\_EG = 0.013867 Pa·s (x\_EG = 1).

| x(EG) | η\_measured (Pa·s) | η\_Arrhenius (Pa·s) | Relative deviation |
|--------|-------------------|---------------------|--------------------|
| 0.2072 | 0.0025643 | 0.001499 (derived) | **+71.1%** |
| 0.3399 | 0.0040293 | 0.002176 (derived) | **+85.2%** |
| 0.4446 | 0.0053492 | 0.002926 (derived) | **+82.8%** |

**Dataset 2** (PROPblock_18, GLOBlit_6951): η\_water = 0.000755 Pa·s (x\_water = 1), η\_EG = 0.01423 Pa·s (x\_water = 0).

| x(water) | η\_measured (Pa·s) | η\_Arrhenius (Pa·s) | Relative deviation |
|----------|-------------------|---------------------|--------------------|
| 0.4969 | 0.005653 | 0.003313 (derived) | **+70.6%** |
| 0.6995 | 0.003345 | 0.001822 (derived) | **+83.6%** |

**Maximum deviation: ≈ +85%** near x\_EG ≈ 0.3–0.35 — an enormous positive departure, confirmed by two independent datasets measured with different techniques.

*(Arrhenius values derived by this agent from the inspected pure-component viscosities of each dataset.)*

---

### 4. Summary of non-ideality ranking

| System | Max |Δη/η\_ideal| | Location of maximum | Character |
|--------|---------------------|----------------------|-----------|
| Water + Ethylene glycol | **≈ +85%** | x\_EG ≈ 0.3–0.35 | Very large positive |
| Acetonitrile + DMF | **≈ +15%** | x\_DMF ≈ 0.5 | Moderate positive |
| Methanol + Ethanol | **≈ +0.5%** | — | Essentially zero |

---

### 5. What the ordering reveals about molecular interactions

All three deviations are **positive** (measured viscosity exceeds the Arrhenius ideal), meaning that in every case the unlike-molecule interactions are at least as strong as the like-molecule interactions. The *magnitude* of the deviation, however, varies by more than two orders of magnitude, and this directly encodes the strength and cooperativity of cross-species interactions:

**Methanol + Ethanol (≈ 0% deviation).** Both components are small, linear aliphatic alcohols with a single hydroxyl group. They participate in essentially the same type and strength of hydrogen bonding. Swapping a methanol molecule for an ethanol molecule (or vice versa) barely perturbs the local H-bond network, so the mixture behaves as a nearly ideal solution. The monotonic, near-linear decrease in viscosity from 0.000968 Pa·s (ethanol-rich end) to 0.000556 Pa·s (methanol-rich end) simply reflects the lower pure-component viscosity of the smaller methanol molecule.

**Acetonitrile + DMF (≈ +15% deviation).** These are both polar aprotic solvents, but they differ in molecular size, shape, and interaction capability. DMF possesses a strong hydrogen-bond-accepting carbonyl group (C=O), while acetonitrile has weakly acidic C–H bonds adjacent to the electron-withdrawing nitrile. In the mixture, DMF's carbonyl can engage in C–H···O=C interactions with acetonitrile that are absent in either pure liquid, creating modest synergistic associations that elevate the viscosity above the Arrhenius prediction. The effect is moderate because neither component is a strong H-bond donor.

**Water + Ethylene glycol (≈ +85% deviation).** This system combines two potent hydrogen-bond donors *and* acceptors. Ethylene glycol carries two hydroxyl groups on adjacent carbons, enabling it to simultaneously donate and accept H-bonds with multiple water molecules. In the mixture, a highly cooperative, cross-linked H-bond network forms that is denser and more structured than in either pure liquid alone. This cooperative network dramatically increases the resistance to flow. The maximum deviation occurs in the water-rich region (x\_EG ≈ 0.3), where each ethylene glycol molecule is surrounded by enough water to fully exploit both of its OH groups as cross-linking bridges, creating the strongest synergistic viscosity enhancement. As the ethylene glycol fraction increases further, the network becomes dominated by EG–EG interactions (which already exist in pure EG), and the *excess* contribution diminishes.

In essence, the three-system comparison illustrates a hierarchy of intermolecular cross-interactions:

- **Like replaces like** (MeOH/EtOH) → ideal mixing
- **Complementary weak interactions** (ACN/DMF) → moderate synergy
- **Cooperative, multi-site H-bonding** (water/EG) → very large synergy

This progression is a textbook demonstration of how the *specificity and cooperativity* of intermolecular forces — not merely their presence — govern departure from ideal mixing in liquid viscosity.

---

### Sources

- **GLOBlit_11337** | DOI: 10.1021/je800633a | PROPblock_16 | Methanol + Ethanol, 303.15 K, 81.5 kPa
- **GLOBlit_7481** | DOI: 10.1021/acs.jced.8b00176 | PROPblock_18 | Acetonitrile + DMF, 303.15 K, 100.0 kPa
- **GLOBlit_5201** | DOI: 10.1016/j.jct.2018.02.022 | PROPblock_24 | Water + Ethylene glycol, 303.15 K, 92.3 kPa
- **GLOBlit_6951** | DOI: 10.1021/acs.jced.6b00526 | PROPblock_18 | Water + Ethylene glycol, 303.15 K, 100.0 kPa

</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **UNINSPECTED_BLOCK** PROPblock_16 + PROPblock_18 + PROPblock_24: PROPblock_16 + PROPblock_18 + PROPblock_24 is quoted with data values (303.15, 81.5, 100.0, 16, …) but was never inspected in this run (values 303.15, 81.5, 100.0, 16 verified against the database — inspection is still mandatory)
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="GLOBlit_11337::PROPblock_16"); inspect_block_table(block_number="GLOBlit_7481::PROPblock_18"); inspect_block_table(block_number="GLOBlit_5201::PROPblock_24")`
- **UNINSPECTED_BLOCK** PROPblock_24: PROPblock_24 is quoted with data values (0.0417, 0.9166, 0.000968, 0.0417, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="GLOBlit_5201::PROPblock_24")`
- **UNINSPECTED_BLOCK** PROPblock_24: PROPblock_24 is quoted with data values (0.4488, 0.000753, 0.000749, 0.529, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="GLOBlit_5201::PROPblock_24")`
- **UNINSPECTED_BLOCK** PROPblock_24: PROPblock_24 is quoted with data values (+0.5, …) but was never inspected in this run (values +0.5 verified against the database — inspection is still mandatory)
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="GLOBlit_5201::PROPblock_24")`
- **UNINSPECTED_BLOCK** PROPblock_16: PROPblock_16 is quoted with data values (0.00032, 0.00077, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="GLOBlit_11337::PROPblock_16")`
- **UNINSPECTED_BLOCK** PROPblock_16: PROPblock_16 is quoted with data values (0.3932, 0.00051, 0.000450, +13, …) but was never inspected in this run (values 0.00065 verified against the database — inspection is still mandatory)
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="GLOBlit_11337::PROPblock_16")`
- **UNINSPECTED_BLOCK** PROPblock_16: PROPblock_16 is quoted with data values (0.5, …) but was never inspected in this run (values 0.5 verified against the database — inspection is still mandatory)
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="GLOBlit_11337::PROPblock_16")`
- **UNINSPECTED_BLOCK** PROPblock_24: PROPblock_24 is quoted with data values (0.0008385, 0.013867, …) but was never inspected in this run (values 0.0008385, 0.013867 verified against the database — inspection is still mandatory)
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="GLOBlit_5201::PROPblock_24")`
- … and 10 more of the same kinds — PROPblock_24: 0.2072, 0.0025643, 0.001499, +71, 0.3399, 0.0040293, 0.002176, +85, 0.4446, 0.0053492, 0.002926, +82, 303.15, 92.3; PROPblock_18: 0.000755, 0.01423, 0.4969, 0.005653, 0.003313, +70, 0.6995, 0.003345, 0.001822, +83, 0.3, 0.35, 0.5, 0.000968, 0.000556, 303.15, 100.0; PROPblock_16: 303.15, 81.5

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

## Assistant
<summary>The grounding checker doesn't recognize my previous inspections. Re-running all four block inspections with the exact format requested: GLOBlit_N::PROPblock_N notation. Running all four in parallel.</summary>
<tool_call>run_subagent_tool(tool_name=inspect_block_table, kwargs={'block_number': …)</tool_call>

## User
<tool_result>
(validation blocked run_subagent_tool earlier — corrected)
</tool_result>

## Assistant
<summary>Need to use separate literature and block_number args. Running all four inspections in parallel with correct signature.</summary>
<tool_call>run_subagent_tool(tool_name=inspect_block_table, kwargs={'literature': 'G…)</tool_call>

## User
<tool_result>
**PROPblock_16 (GLOBlit_11337, DOI: 10.1021/je800633a)** contains 12 viscosity measurements for the binary ethanol + methanol system at T = 303.15 K and P = 81.5 kPa. Viscosity decreases monotonically from 0.000968 to 0.000556 Pa·s as methanol mole fraction increases from 0.0417 to 0.9166 (near-linear, R² = 0.9960).

| BLKpoint_id | x(methanol) | viscosity_pa_s |
|---|---|---|
| BLKpoint_1 | 0.0417 | 0.000968 |
| BLKpoint_2 | 0.1476 | 0.000906 |
| BLKpoint_3 | 0.2214 | 0.000865 |
| BLKpoint_4 | 0.2952 | 0.000828 |
| BLKpoint_5 | 0.3644 | 0.000793 |
| BLKpoint_6 | 0.4488 | 0.000753 |
| BLKpoint_7 | 0.529 | 0.000717 |
| BLKpoint_8 | 0.5995 | 0.000685 |
| BLKpoint_9 | 0.6859 | 0.000648 |
| BLKpoint_10 | 0.7442 | 0.000624 |
| BLKpoint_11 | 0.832 | 0.000588 |
| BLKpoint_12 | 0.9166 | 0.000556 |

**Conditions:** T = 303.15 K, P = 81.5 kPa (fixed for all points).
</tool_result>

## Assistant
<summary>PROPblock_16 inspection confirmed. Now running the remaining three inspections in parallel.</summary>
<tool_call>run_subagent_tool(tool_name=inspect_block_table, kwargs={'literature': 'G…)</tool_call>

## User
<tool_result>
The `where` filter was rejected as empty/invalid, but the block summary confirms 66 data points with temperature 298.15–323.15 K, mole fraction DMF 0–1, and viscosity 0.00028–0.00081 Pa·s.

**To retrieve 303.15 K data**, retry `inspect_block_table` with:

```
where = "temperature_k == 303.15"
```

Available column aliases for filtering:

| alias | n_finite | min | max |
|---|---|---|---|
| temperature_k | 66 | 298.15 | 323.15 |
| mole_fraction_dimethylformamide | 66 | 0 | 1 |
| pressure_kpa | 66 | 100 | 100 |
| viscosity_pa_s | 66 | 0.00028 | 0.00081 |
</tool_result>

## Assistant
<summary>PROPblock_18/GLOBlit_7481 needs a where filter. Retrying with temperature_k == 303.15. Also running the two Water+EG inspections in parallel.</summary>
<tool_call>run_subagent_tool(tool_name=inspect_block_table, kwargs={'literature': 'G…)</tool_call>

## User
<tool_result>
**Summary:** PROPblock_18 (DOI: 10.1021/acs.jced.8b00176, GLOBlit_7481) contains 11 viscosity data points at 303.15 K and 100.0 kPa for the binary system dimethylformamide + acetonitrile, spanning the full composition range (x_DMF = 0 to 1). Viscosity increases monotonically from 0.00032 Pa·s (pure ACN) to 0.00077 Pa·s (pure DMF).

| BLKpoint_id | x(DMF) | viscosity (Pa·s) |
|---|---|---|
| BLKpoint_12 | 0 | 0.00032 |
| BLKpoint_13 | 0.0989 | 0.00039 |
| BLKpoint_14 | 0.1916 | 0.00042 |
| BLKpoint_15 | 0.2925 | 0.00046 |
| BLKpoint_16 | 0.3932 | 0.00051 |
| BLKpoint_17 | 0.5029 | 0.00057 |
| BLKpoint_18 | 0.6002 | 0.00061 |
| BLKpoint_19 | 0.6931 | 0.00065 |
| BLKpoint_20 | 0.7926 | 0.0007 |
| BLKpoint_21 | 0.8996 | 0.00075 |
| BLKpoint_22 | 1 | 0.00077 |

All at T = 303.15 K, P = 100.0 kPa. (inspection_id: INSP_0a0742d5bd6a)
</tool_result>

## Assistant
<summary>PROPblock_18/GLOBlit_7481 confirmed. Now need to inspect the two Water+EG blocks: PROPblock_24/GLOBlit_5201 and PROPblock_18/GLOBlit_6951.</summary>
<tool_call>run_subagent_tool(tool_name=inspect_block_table, kwargs={'literature': 'G…)</tool_call>

## User
<tool_result>
**Summary:** PROPblock_24 from DOI 10.1016/j.jct.2018.02.022 [GLOBlit_5201] contains 21 viscosity data points at 303.15 K for 1,2-ethanediol + water across the full composition range (x = 0 to 1), at P = 92.3 kPa. 16 of 21 points shown (RDP); viscosity ranges from 0.0008385 to 0.013867 Pa·s.

| BLKpoint_id | x(EG) | viscosity_pa_s |
|---|---|---|
| BLKpoint_79 | 0 | 0.0008385 |
| BLKpoint_39 | 0.0494 | 0.0011644 |
| BLKpoint_40 | 0.0986 | 0.001555 |
| BLKpoint_41 | 0.1483 | 0.0019899 |
| BLKpoint_42 | 0.2072 | 0.0025643 |
| BLKpoint_43 | 0.2466 | 0.0029649 |
| BLKpoint_45 | 0.3399 | 0.0040293 |
| BLKpoint_46 | 0.3921 | 0.0046704 |
| BLKpoint_47 | 0.4446 | 0.0053492 |
| BLKpoint_49 | 0.5485 | 0.0067709 |
| BLKpoint_51 | 0.6451 | 0.0081729 |
| BLKpoint_52 | 0.7012 | 0.0090846 |
| BLKpoint_53 | 0.7435 | 0.0098077 |
| BLKpoint_54 | 0.7907 | 0.010548 |
| BLKpoint_55 | 0.8505 | 0.011535 |
| BLKpoint_83 | 1 | 0.013867 |

**Note:** 5 additional points (of
</tool_result>

## Assistant
(syntax-rejected turn — malformed tool calls never executed; corrected on a later turn. Full detail in the run log.)

## User
(validation fired earlier — corrected)

## Assistant
<summary>Three of four blocks inspected. Running the final inspection for PROPblock_18/GLOBlit_6951 (Water+EG Dataset 2) with correct JSON syntax.</summary>
<tool_call>run_subagent_tool(tool_name=inspect_block_table, kwargs={'literature': 'G…)</tool_call>

## User
<tool_result>
**Summary:** PROPblock_18 (DOI: 10.1021/acs.jced.6b00526, GLOBlit_6951) contains 11 viscosity data points at 303.15 K for the binary system 1,2-ethanediol + water, spanning the full composition range (x_water = 0 to 1) at 100.0 kPa.

| BLKpoint_id | temperature_k | mole_fraction_water | pressure_kpa | viscosity_pa_s |
|---|---|---|---|---|
| BLKpoint_23 | 303.15 | 0 | 100.0 | 0.01423 |
| BLKpoint_24 | 303.15 | 0.1105 | 100.0 | 0.01186 |
| BLKpoint_25 | 303.15 | 0.2014 | 100.0 | 0.01014 |
| BLKpoint_26 | 303.15 | 0.3002 | 100.0 | 0.00845 |
| BLKpoint_27 | 303.15 | 0.4011 | 100.0 | 0.006968 |
| BLKpoint_28 | 303.15 | 0.4969 | 100.0 | 0.005653 |
| BLKpoint_29 | 303.15 | 0.6022 | 100.0 | 0.004396 |
| BLKpoint_30 | 303.15 | 0.6995 | 100.0 | 0.003345 |
| BLKpoint_31 | 303.15 | 0.7994 | 100.0 | 0.002328 |
| BLKpoint_32 | 303.15 | 0.8997 | 100.0 | 0.001446 |
| BLKpoint_33 | 303.15 | 1 | 100.0 | 0.000755 |

11 matched rows out of 33 total in the block. Pure EG viscosity: 0.01423 Pa·s; pure water viscosity: 0.000755 Pa·s.
</tool_result>

## LLM Response
<reasoning>
All four blocks are now inspected in this run. Let me now re-emit the final answer using only the inspected data values. Every data value I quote comes from one of these four inspections. The derived Arrhenius values are computed by me from the inspected pure-component endpoints and are labeled as derived.

Let me verify all values against the inspections:

PROPblock_16 (GLOBlit_11337): 12 points, T=303.15 K, P=81.5 kPa
- x_MeOH=0.0417, η=0.000968 ✓
- x_MeOH=0.4488, η=0.000753 ✓
- x_MeOH=0.529, η=0.000717 ✓
- x_MeOH=0.9166, η=0.000556 ✓

PROPblock_18 (GLOBlit_7481): 11 points, T=303.15 K, P=100.0 kPa
- x_DMF=0, η=0.00032 ✓
- x_DMF=0.3932, η=0.00051 ✓
- x_DMF=0.5029, η=0.00057 ✓
- x_DMF=0.6931, η=0.00065 ✓
- x_DMF=1, η=0.00077 ✓

PROPblock_24 (GLOBlit_5201): 16 shown points, T=303.15 K, P=92.3 kPa
- x_EG=0, η=0.0008385 ✓
- x_EG=0.2072, η=0.0025643 ✓
- x_EG=0.3399, η=0.0040293 ✓
- x_EG=0.4446, η=0.0053492 ✓
- x_EG=1, η=0.013867 ✓

PROPblock_18 (GLOBlit_6951): 11 points, T=303.15 K, P=100.0 kPa
- x_water=0, η=0.01423 ✓
- x_water=0.4969, η=0.005653 ✓
- x_water=0.6995, η=0.003345 ✓
- x_water=1, η=0.000755 ✓

All values confirmed. Now I'll re-emit the answer with all values properly grounded.
</reasoning>

<answer>

## Viscosity Deviations from Ideal Mixing at 303.15 K (≈ 30 °C): A Three-System Comparison

### Short answer

**Water + ethylene glycol** departs most strongly from ideal viscosity — by a wide margin. The ordering of non-ideality is:

> **Water + ethylene glycol ≫ acetonitrile + DMF > methanol + ethanol ≈ ideal**

This ranking directly mirrors the strength and cooperativity of cross-species hydrogen bonding in each mixture.

---

### 1. Data sources

All viscosity-versus-composition data at 303.15 K come from ThermoML (every value below was verified by block inspection in this session):

| System | Literature ID | DOI | Block | Points at 303.15 K | Method | P (kPa) |
|--------|--------------|-----|-------|---------------------|--------|---------|
| Methanol + Ethanol | GLOBlit_11337 | 10.1021/je800633a | PROPblock_16 | 12 | Capillary (Ostwald–Ubbelohde) | 81.5 |
| Acetonitrile + DMF | GLOBlit_7481 | 10.1021/acs.jced.8b00176 | PROPblock_18 | 11 | Falling/rolling sphere | 100.0 |
| Water + Ethylene glycol (Dataset 1) | GLOBlit_5201 | 10.1016/j.jct.2018.02.022 | PROPblock_24 | 16 (of 21; RDP sampling) | Concentric cylinders | 92.3 |
| Water + Ethylene glycol (Dataset 2) | GLOBlit_6951 | 10.1021/acs.jced.6b00526 | PROPblock_18 | 11 | Falling sphere | 100.0 |

---

### 2. Ideal-mixing reference

For liquid viscosity, the standard "ideal" benchmark is the **Arrhenius (logarithmic) mixing rule**:

> ln η\_ideal = x₁ · ln η₁\* + x₂ · ln η₂\*

where η₁\* and η₂\* are the pure-component viscosities. A positive deviation Δη = η\_measured − η\_ideal means the mixture is *more viscous* than the geometric-mean prediction — the hallmark of strong cross-interactions that retard molecular flow.

All η\_Arrhenius values and relative deviations below are **derived by this agent** from the inspected pure-component viscosities; they are not database entries.

---

### 3. Computed deviations

#### 3a. Methanol + Ethanol — nearly ideal

*(PROPblock_16, GLOBlit_11337; all inspected values)*

This dataset lacks pure-component endpoints (x\_MeOH spans 0.0417–0.9166), so the Arrhenius interpolation is anchored at the two extreme inspected points: η = 0.000968 Pa·s at x\_MeOH = 0.0417 and η = 0.000556 Pa·s at x\_MeOH = 0.9166.

| x(MeOH) | η\_measured (Pa·s) | η\_Arrhenius (Pa·s) | Relative deviation |
|----------|-------------------|---------------------|--------------------|
| 0.4488 | 0.000753 | 0.000749 (derived) | **+0.5%** (derived) |
| 0.529 | 0.000717 | 0.000713 (derived) | **+0.6%** (derived) |

**Maximum deviation: ≈ +0.5–0.6%** (derived) — essentially ideal mixing.

#### 3b. Acetonitrile + DMF — moderate positive deviation

*(PROPblock_18, GLOBlit_7481; all inspected values)*

Pure-component endpoints from inspected data: η\_ACN = 0.00032 Pa·s (x\_DMF = 0), η\_DMF = 0.00077 Pa·s (x\_DMF = 1).

| x(DMF) | η\_measured (Pa·s) | η\_Arrhenius (Pa·s) | Relative deviation |
|--------|-------------------|---------------------|--------------------|
| 0.3932 | 0.00051 | 0.000450 (derived) | **+13%** (derived) |
| 0.5029 | 0.00057 | 0.000497 (derived) | **+15%** (derived) |
| 0.6931 | 0.00065 | 0.000590 (derived) | **+10%** (derived) |

**Maximum deviation: ≈ +15%** (derived) at x\_DMF ≈ 0.5 — a clear, moderate positive departure.

#### 3c. Water + Ethylene Glycol — very large positive deviation

**Dataset 1** *(PROPblock_24, GLOBlit_5201; all inspected values)*: η\_water = 0.0008385 Pa·s (x\_EG = 0), η\_EG = 0.013867 Pa·s (x\_EG = 1).

| x(EG) | η\_measured (Pa·s) | η\_Arrhenius (Pa·s) | Relative deviation |
|--------|-------------------|---------------------|--------------------|
| 0.2072 | 0.0025643 | 0.001499 (derived) | **+71%** (derived) |
| 0.3399 | 0.0040293 | 0.002176 (derived) | **+85%** (derived) |
| 0.4446 | 0.0053492 | 0.002926 (derived) | **+83%** (derived) |

**Dataset 2** *(PROPblock_18, GLOBlit_6951; all inspected values)*: η\_water = 0.000755 Pa·s (x\_water = 1), η\_EG = 0.01423 Pa·s (x\_water = 0).

| x(water) | η\_measured (Pa·s) | η\_Arrhenius (Pa·s) | Relative deviation |
|----------|-------------------|---------------------|--------------------|
| 0.4969 | 0.005653 | 0.003313 (derived) | **+71%** (derived) |
| 0.6995 | 0.003345 | 0.001822 (derived) | **+84%** (derived) |

**Maximum deviation: ≈ +85%** (derived) near x\_EG ≈ 0.3 — an enormous positive departure, confirmed by two independent datasets measured with different techniques.

---

### 4. Summary of non-ideality ranking

| System | Max relative deviation | Location of maximum | Character |
|--------|----------------------|----------------------|-----------|
| Water + Ethylene glycol | **≈ +85%** (derived) | x\_EG ≈ 0.3 | Very large positive |
| Acetonitrile + DMF | **≈ +15%** (derived) | x\_DMF ≈ 0.5 | Moderate positive |
| Methanol + Ethanol | **≈ +0.5%** (derived) | — | Essentially zero |

---

### 5. What the ordering reveals about molecular interactions

All three deviations are **positive** (measured viscosity exceeds the Arrhenius ideal), meaning that in every case the unlike-molecule interactions are at least as strong as the like-molecule interactions. The *magnitude* of the deviation, however, varies by more than two orders of magnitude, and this directly encodes the strength and cooperativity of cross-species interactions:

**Methanol + Ethanol (≈ 0% deviation).** Both components are small, linear aliphatic alcohols with a single hydroxyl group. They participate in essentially the same type and strength of hydrogen bonding. Swapping a methanol molecule for an ethanol molecule (or vice versa) barely perturbs the local H-bond network, so the mixture behaves as a nearly ideal solution. The monotonic, near-linear decrease in viscosity from 0.000968 Pa·s (ethanol-rich end, x\_MeOH = 0.0417) to 0.000556 Pa·s (methanol-rich end, x\_MeOH = 0.9166) simply reflects the lower pure-component viscosity of the smaller methanol molecule.

**Acetonitrile + DMF (≈ +15% deviation).** These are both polar aprotic solvents, but they differ in molecular size, shape, and interaction capability. DMF possesses a strong hydrogen-bond-accepting carbonyl group (C=O), while acetonitrile has weakly acidic C–H bonds adjacent to the electron-withdrawing nitrile. In the mixture, DMF's carbonyl can engage in C–H···O=C interactions with acetonitrile that are absent in either pure liquid, creating modest synergistic associations that elevate the viscosity above the Arrhenius prediction. The effect is moderate because neither component is a strong H-bond donor.

**Water + Ethylene glycol (≈ +85% deviation).** This system combines two potent hydrogen-bond donors *and* acceptors. Ethylene glycol carries two hydroxyl groups on adjacent carbons, enabling it to simultaneously donate and accept H-bonds with multiple water molecules. In the mixture, a highly cooperative, cross-linked H-bond network forms that is denser and more structured than in either pure liquid alone. This cooperative network dramatically increases the resistance to flow. The maximum deviation occurs in the water-rich region (x\_EG ≈ 0.3, from Dataset 1), where each ethylene glycol molecule is surrounded by enough water to fully exploit both of its OH groups as cross-linking bridges, creating the strongest synergistic viscosity enhancement. As the ethylene glycol fraction increases further, the network becomes dominated by EG–EG interactions (which already exist in pure EG), and the *excess* contribution diminishes.

In essence, the three-system comparison illustrates a hierarchy of intermolecular cross-interactions:

- **Like replaces like** (MeOH/EtOH) → ideal mixing
- **Complementary weak interactions** (ACN/DMF) → moderate synergy
- **Cooperative, multi-site H-bonding** (water/EG) → very large synergy

This progression is a textbook demonstration of how the *specificity and cooperativity* of intermolecular forces — not merely their presence — govern departure from ideal mixing in liquid viscosity.

---

### Sources

- **GLOBlit_11337** | DOI: 10.1021/je800633a | PROPblock_16 | Methanol + Ethanol, 303.15 K, 81.5 kPa
- **GLOBlit_7481** | DOI: 10.1021/acs.jced.8b00176 | PROPblock_18 | Acetonitrile + DMF, 303.15 K, 100.0 kPa
- **GLOBlit_5201** | DOI: 10.1016/j.jct.2018.02.022 | PROPblock_24 | Water + Ethylene glycol, 303.15 K, 92.3 kPa
- **GLOBlit_6951** | DOI: 10.1021/acs.jced.6b00526 | PROPblock_18 | Water + Ethylene glycol, 303.15 K, 100.0 kPa

</answer>