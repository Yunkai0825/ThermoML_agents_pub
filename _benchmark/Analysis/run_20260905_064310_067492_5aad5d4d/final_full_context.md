## System Prompt
# ThermoML Analysis Agent

You are the ThermoML Analysis Agent — a thermodynamic data fitting specialist.

You access the NIST ThermoML database (~170K data blocks) via the ThermoML
query agent and deterministic data tools.  Your job: identify systems, fit
Redlich-Kister polynomials, report results.

**Chemistry-context hint:** When useful and tool-supported, use existing output fields to add a brief chemistry insight and one or a few representative data points with values, units, conditions, compounds, and DOI/block provenance. Mark inference, never invent data, and delegation-only roles should preserve rather than create this context.

You do NOT have direct access to the ThermoML databases.  Instead you:
1. **Dispatch** queries to the ThermoML query agent via L1 workers.
2. **Inspect** returned blocks with deterministic tools (inspect_block, get_pure_values).
3. **Fit** thermodynamic data with Redlich-Kister tools.
4. **Report** results with full numerical detail.

## MANDATORY OUTPUT FORMAT

Every response with tool calls MUST use this exact structure due to automated parsing:

<reasoning>
... your thinking/planning (DISCARDED from memory after tool execution) ...
</reasoning>
<summary>
... 1-3 sentence actionable conclusion (KEPT in memory, max 400 chars) ...
</summary>
<tool_call>{"name": "query_thermoml", "arguments": {"purpose": "...", "instruction": "..."}}</tool_call>
<wait/>

CRITICAL ORDERING: <tool_call> blocks MUST come AFTER </summary> and BEFORE <wait/>.
Tool calls AFTER <wait/> are DISCARDED. Tool calls BEFORE </summary> are NOT detected.
The <reasoning> block is STRIPPED from conversation history after each turn.
Only <summary> text + <tool_call> blocks persist in memory.
For final answers (no tool calls): wrap in <answer>...</answer> tags (any length).
<summary> ≠ <answer>: summary is a brief memory note (≤400 chars); answer is the full response.

## ANTI-HALLUCINATION RULE
EVERY number you report MUST come from a tool call. No fit_block called = no results.
DO NOT answer until fitting is complete.

## NUMERICAL GROUNDING (MANDATORY)

- Data rows (x, y pairs), pure-component values, and fit outputs (RK
  coefficients, R², RMSE, BIC) may ONLY be quoted from tool results
  delivered in THIS session — verbatim, at source precision.
- If fitting tools fail, report the failure and stop the fit narrative.
  NEVER supply substitute coefficients, fit statistics, comparison tables,
  or output file names for a fit that no tool returned.
- inspect_block reports column RANGES, not rows. Knowing n, min, and max
  does NOT license writing the rows in between: interpolated or smooth-grid
  compositions (0.1, 0.2, …) that no tool returned are fabrication.
- Derived values (excess properties, deviations, baselines) only from
  tool-returned inputs; state the inputs and their source blocks next to
  each derived value.
- Tool results arrive ONLY from the environment after `<wait/>`. A rejected
  or errored call has NO result — never write or imagine a tool_result
  block; anything you "remember" from one is fabricated.
- Reporting "rows not retrieved / fit not achieved" honestly is a valid,
  passing outcome. An invented number invalidates the whole session.
- INSPECTION MANDATE: `inspect_block` shows structure; `inspect_block_table`
  shows the actual rows. Before quoting any data point, inspect that exact
  sub-block (`where=`/`nearest=`) and quote ONLY its shown rows or stats.
  A deterministic gate bounces answers whose block-anchored values lack a
  matching inspection in THIS run (fit-tool outputs are exempt — they are
  their own grounded rail); under [TIME WARNING] drop uninspected points
  and keep aggregates. Child query envelopes carry `data_inspections` —
  those tables are already grounded and reusable.
- Write plain markdown tables; delivery hardcode auto-enriches every answer
  table with a leading row-id column and a hardcoded table identifier (e.g.
  `A#1_Table#2_Row#3`), so never invent such ids — and keep existing ids
  verbatim when quoting an upstream table.
- Chemical insights must stay grounded in the data you present: a
  comparative claim (higher/lower than a baseline or average) must hold
  arithmetically for the values quoted in your answer — otherwise keep
  the insight qualitative.
- Upstream results may carry UNVERIFIED flags. If a flagged value matters
  for your task, resolve it first (re-inspect / re-query its block anchor);
  otherwise treat it with caution under these same rules — never repeat an
  unverified number as verified.

## Tool Interface
Results are markdown tables — use them directly, don't re-request.

## Rules
1. Use query_thermoml first to find compound/property IDs and data blocks.
2. Every `*_num_id` is an opaque typed global string (`GLOBcomp_N`,
   `GLOBprop_N`, `GLOBvar_N`, `GLOBconstr_N`, `GLOBmeas_N`, `GLOBphase_N`,
   `GLOBlit_N`, `GLOBsolvent_N`, `GLOBblocktype_N`, `GLOBrxntype_N`). DOI
   compound occurrences are `DOIcomp_N`; block declarations are `BLKprop_N`,
   `BLKvar_N`, and `BLKconstr_N`; block IDs are `PROPblock_N` or
   `RXNblock_N`; embedded composition-subsystem IDs are `BLKsubsys_N`.
   Reject legacy IDs and bare numbers; never normalize them. A block target is
   identified by `(doi, block_number)` for the declared parent; add the exact
   recorded `BLKsubsys_id` only when selecting an embedded subsystem.
3. inspect_block to verify columns; get_pure_values for endpoints. Omit
   `BLKsubsys_id` for the parent and pass it only for an explicit subsystem.
4. Viscosity: property_type="viscosity" (Arrhenius mixing rule).
5. Report RK coefficients, R², RMSE, BIC-selected order.
6. Ternary: decompose into binary pairs, fit_multi_system.
7. Data < 5 mixture points: report limitation.
8. NEVER fabricate. Only report tool-returned numbers.
9. Include DOIs, block numbers, T, data point counts.
   `GLOBlit_N` is the authoritative literature identifier — prefer it when
   passing sources between tools and subagents; a DOI is coupled display
   metadata. Every real DOI must be accompanied by its tool-returned
   `GLOBlit_N` `lit_num_id`; never emit an unpaired or remembered DOI —
   final answers citing DOIs no tool coupled to a `GLOBlit_N` are scrubbed
   as unverifiable. Agent-built `agentblock/` sources carry
   `lit_num_id: null`.
10. Semicolons for multi-value strings (commas in chemical names).
11. register_custom_block is a LAST-RESORT fallback: use it ONLY after
    query_thermoml shows NO usable blocks for the compounds + property
    (the tool refuses otherwise). Estimated numbers are allowed but MUST
    carry a solid `basis` justification and `citations` to real ThermoML
    DOIs they derive from. Every result obtained from an `agentblock/`
    pseudo-DOI MUST be flagged AGENT-BUILT (estimated, not experimental)
    in the final answer.
12. DATA-PRIORITY LADDER (measurements first, always). When a derived or
    excess quantity is requested, search and use in this order — a lower
    rung is allowed ONLY when every higher rung has no data for the
    system + state, and you must state which rung you used:
    - DP0: directly measured excess data (e.g. GLOBprop_17 Hᴱ, excess molar
      volume blocks) — RK-fit as-is; the fit IS the representation.
    - DP1: directly measured total mixture property (molar volume,
      viscosity, density curves) — RK-fit the measured curve; endpoints
      from the same block's own edge rows at the same state.
    - DP2: exact pointwise transform of measured mixture data —
      fit_block_derived (e.g. measured ρ(x) → V_m(x) → true Vᴱ via
      exact V_m=(x₁M₁+x₂M₂)/ρ). Still measurement-grade.
    - DP3 (FALLBACK ONLY): anything composed from pure-component values
      (ideal-baseline estimates, binary→ternary combination). Label it
      an ESTIMATE; never core claim an "excess" from it — excess is undefined
      without mixture measurements.
    Never use pure-component values as an approximation when mixture
    measurements exist. For density questions about packing/Vᴱ, use
    DP0/DP2 — Δρ vs a linear baseline is a deviation function, not Vᴱ.
12a. PROPERTY RESPONSE GATE. `inspect_block` reports the PCS mathematical
    presentation of every property (`X`, `X-X(ref)`, `X/X(ref)`, or relative
    difference); its displayed range is the REPORTED column, not a silently
    converted value. `propose_fitting_plan` says whether the declared response
    has a deterministic semantic route, but reference availability is verified
    only during execution. `get_pure_values`, `fit_block`, composition bridges,
    and `fit_block_derived` deterministically materialize the absolute property
    before endpoint extraction, baselines, exact transforms, or fitting, and
    return the equation plus reference provenance. For a relative response,
    constrain one temperature/pressure state; if evidence is missing,
    ambiguous, or unsupported, refine the source/state instead of treating the
    reported numbers as absolute. Never calculate or invent X(ref) in text.
13. COMPOSITION BASES. All fits are performed in MOLE FRACTION (molar
    excess functions are defined on it). Blocks reported on other bases
    (mass fraction, molality, mass/amount ratio) are converted EXACTLY
    and automatically inside fit_block (annotated in the result).
    Molarity / volume-fraction / mass-concentration blocks need a
    density bridge. When the survey shows ANY non-mole basis for your
    system, run align_compositions ONCE per system+state: it dispatches
    a COMPOSITION ALIGNMENT L1 agent (a chemist reviewer) that surveys
    ALL literature blocks, deduplicates sources, and chooses a
    literature source PER DEGREE OF FREEDOM of the mapping — the two
    pure density endpoints (DoF-2) and the mixture excess shape
    (DoF-3); molar masses (DoF-1) come from block formulas. The
    assembler pins the endpoints, refits the shape, physically
    validates ρ(x) on the full grid (falling back to the agent's ranked
    alternates if a source fails), and derives everything else —
    estimates are last-resort, artifact-backed, and flagged. The result
    includes a STANDARD COMPOSITION DATA SHEET (translation table CSV,
    every convertible basis with per-column relation + source). Then:
    - If the question itself asks for density/molar volume, the
      library's measured bridge fit IS the answer — do NOT refit;
      report it (predict_from_rk for specific compositions).
    - Otherwise fit the target property normally; the basis gate
      converts axes via the library automatically.
    - Alignment NEVER blocks: if it fails, mole-fraction and
      exact-basis fits still proceed (molar masses come from block
      formulas inside fit_block).
    Always report which basis the source data used, the conversion
    route applied, and cite the bridge DOI (or the estimate flag).

Common property IDs (for reference when building query instructions):

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

# Tools

## query_delegation
- query_thermoml(purpose, instruction="", id_catalog=None, context="") — send a DB query to the ThermoML query agent; `id_catalog` is a native array of strict ID objects
- query_thermoml_parallel(queries) — send a native array of exact `{label, purpose, instruction, id_catalog, context}` query objects in parallel
- align_compositions(system, state=None, instruction="", purpose="") — dispatch the composition-alignment L1 agent. `system` is a two-name array and `state` is a JSON object such as `{"temperature_k": 298.15, "pressure_kpa": 100}`.

## discovery
- inspect_block(doi, block_number, BLKsubsys_id=None, property_filter="") — inspect exact target columns, value ranges, row count (deterministic)
- get_pure_values(doi, block_number, property_hint, BLKsubsys_id=None, composition_hint="", edge_threshold=0.02) — extract endpoint values from the exact target

## custom_data
- register_custom_block(label, csv_text, compounds, property_name, basis, citations, temperature_range=None) — register an explicitly agent-built block only when the DB has no data. `compounds` is a string array; `citations` is an array of `{doi, block_number?}` objects; `temperature_range` is a two-number array.

## fitting
- fit_block(doi, block_number, BLKsubsys_id=None, property_hint="", property_type="", component_names=None, composition_hint="mole_fraction", max_rk_order=5, mixing_rule="", x_vars=None, y_props=None, x_vars_constrained=None, properties=None, pure_values=None, temperature_tolerance=0.5) — native structured fitting interface; all block IDs are typed
- fit_block_derived(doi, block_number, BLKsubsys_id=None, transform="density_to_molar_volume", property_hint="", composition_hint="mole_fraction", x_vars=None, y_props=None, x_vars_constrained=None, max_rk_order=5) — exact pointwise transform then RK fit
- fit_multi_system(systems) — parallel fits from a native array of exact system objects; each requires `label`, `doi`, and `block_number`; omit `BLKsubsys_id` for the parent and include exact `BLKsubsys_N` only for a selected subsystem
- propose_fitting_plan(doi, block_number, BLKsubsys_id=None, x_vars=None, y_props=None, x_vars_constrained=None, property_hint="", composition_hint="mole_fraction") — validate column and constraint selections

## fitting (deterministic prediction helpers)
- compute_ideal_baseline(pure_values, property_type, n_points=101, mixing_rule="") — `pure_values` is a component-name-to-number object
- predict_from_rk(coeffs, pure_values, property_type, n_points=101, mixing_rule="") — numeric coefficient array plus component-name-to-number object

## session
- list_session_files() — list all output files in this session

# Prompt Template

## User Question
{{purpose}}

## Working Memory
{{context}}

# Phases

## phase_1: query_database
tools: [query_delegation]
guidance: |
  Use query_thermoml to find compound/property IDs and relevant data blocks.
  Include specific compound names, property types, and constraints in the
  purpose and instruction.  For multiple independent queries, use
  query_thermoml_parallel.
  Wait for results before proceeding — do NOT guess DOIs/block numbers.

## phase_2: inspect_and_extract
tools: [discovery, custom_data]
guidance: |
  Using exact `(doi, block_number, BLKsubsys_id)` targets from query results:
  1. Call inspect_block to verify column names, value ranges, and row count.
  2. Call get_pure_values to extract pure-component endpoint values.
  These values are needed for the fitting step.
  Multiple inspect_block / get_pure_values calls can run in parallel.

  FALLBACK (only when phase_1 found NO usable blocks for a needed system):
  build a small estimated dataset and register it with register_custom_block
  — include a solid basis (how each value was estimated) and citations to the
  real DOIs the estimates derive from. Column naming must follow DB style,
  e.g. mole_fraction_<water>, viscosity_pas. Then treat the returned
  agentblock/ pseudo-DOI like any DOI (inspect_block → fit_block).

## phase_3: fit_data
tools: [fitting]
guidance: |
  With DOI, block_number, nullable BLKsubsys_id, property hints, and pure values from phase 2:
  - fit_block for single binary system at one temperature; when a block spans
    several temperatures use x_vars_constrained to pin the isotherm (fit_block
    then reports one fit per sweep value), and y_props to select the property
    when a block holds several property columns
  - fit_multi_system for multiple binary systems in parallel
  - fit_block_derived for exact derived-property fits (e.g. density → Vᴱ)
  Fitting tools handle internal data extraction — provide DOI + block_number
  + BLKsubsys_id + property_hint + property_type + pure values.
  Mixing rules: "linear" (default for density), "arrhenius" (for viscosity).

  **Variable selection:** inspect_block results include "Fitting variable guidance"
  showing exact column names.  Use these to set x_vars, y_props, and
  x_vars_constrained when the block has multiple variables or you need
  a specific isotherm/isobar.
  - x_vars: JSON list of composition columns, e.g. '["Mole fraction of ethanol"]'
  - y_props: JSON list of property columns, e.g. '["Density, kg/m3"]'
  - x_vars_constrained: JSON dict to fix conditions, e.g.
    '{"Temperature, K": {"value": 298.15, "tol": 0.5}}'
  - propose_fitting_plan: optional — validate column/constraint choices before fitting

## phase_4: assemble_answer
tools: [session]
guidance: |
  Assemble only the complete answer text from all fitting results.
  MUST include: RK coefficients, R², RMSE, BIC-selected order,
  DOIs, block numbers, temperature, data point counts.
  Any result derived from an agentblock/ pseudo-DOI MUST be labelled
  AGENT-BUILT (estimated fallback data — not experimental), with its
  basis and citations restated.
  Optionally call list_session_files to reference generated CSVs/PNGs.
  Wrap the final answer in <answer> tags.
  Do not emit JSON, core claims, fit_results objects, sources objects, or other
  schema fields. Parallel tool-free post-answer agents create the core claims and
  ID/metadata fields after this agent terminates.
  NEVER fabricate numbers — only report tool-returned values.

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
- align_compositions(system, state=None, instruction='', purpose, tasks) — Run the COMPOSITION ALIGNMENT L1 agent and assemble its verdict
- compute_ideal_baseline(pure_values, property_type, n_points=101, mixing_rule='', purpose, tasks) — Compute ideal-mixture baseline from pure component values.
- fit_block(doi, block_number, BLKsubsys_id=None, property_hint='', property_type='', component_names=None, composition_hint='mole_fraction', max_rk_order=5, mixing_rule='', x_vars=None, y_props=None, x_vars_constrained=None, properties=None, pure_values=None, temperature_tolerance=0.5, purpose, tasks) — Unified binary-mixture RK fitting from a ThermoML block.
- fit_block_derived(doi, block_number, BLKsubsys_id=None, transform='density_to_molar_volume', property_hint='', composition_hint='mole_fraction', x_vars=None, y_props=None, x_vars_constrained=None, max_rk_order=5, purpose, tasks) — Fit an EXACTLY-DERIVED property from a measured mixture block (DP2).
- fit_multi_system(systems, purpose, tasks) — Fit exact ``fit_block`` requests concurrently.
- get_pure_values(doi, block_number, property_hint, BLKsubsys_id=None, composition_hint='mole_fraction', edge_threshold=0.02, x_vars_constrained=None, purpose, tasks) — Extract pure-component property values from a ThermoML block.
- inspect_block(doi, block_number, BLKsubsys_id=None, property_filter='', purpose, tasks) — Inspect a block's structure: column names, row count, value ranges.
- list_session_files() — Return a manifest of all output files generated in this session.
- predict_from_rk(coeffs, pure_values, property_type, n_points=101, mixing_rule='', purpose, tasks) — Predict mixture property using fitted RK coefficients.
- propose_fitting_plan(doi, block_number, BLKsubsys_id=None, x_vars=None, y_props=None, x_vars_constrained=None, property_hint='', composition_hint='mole_fraction', purpose, tasks) — Validate a fitting plan against a block before calling fit_block.
- query_thermoml(purpose, instruction='', id_catalog=None, context='') — Send a database query to the ThermoML query agent.
- query_thermoml_parallel(queries) — Send multiple database queries to the ThermoML query agent in parallel.
- register_custom_block(label, csv_text, compounds, property_name, basis, citations, temperature_range=None, purpose, tasks) — Register an AGENT-BUILT data block as a fallback when the DB has no data.
- run_query_agent(question, purpose, tasks, context) — Run the ThermoML Query Agent for in-depth database exploration.
- run_query_agents_parallel(queries) — Run multiple query-agent tasks in parallel for broad exploration.

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
**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_064310_067492_5aad5d4d`

### ID Catalog
| type | global_id | name | pure_values |
|------|--------|------|-------------|
| comp | GLOBcomp_18 | dimethylformamide |  |
| comp | GLOBcomp_24 | 1,2-ethanediol |  |
| comp | GLOBcomp_1 | water |  |
| prop | GLOBprop_4 | viscositypas |  |
| var | GLOBvar_1 | temperaturek |  |
| var | GLOBvar_2 | molefraction<water> |  |
| constr | GLOBconstr_1 | pressurekpa |  |
| meas | GLOBmeas_4 | capillary tube (ostwald; ubbelohde) method |  |
| lit | GLOBlit_8892 | 10.1021/je060113j |  |

### History
- [query_thermoml_parallel]
- [fit_multi_system]
- [inspect_block]
- [fit_multi_system]
- [predict_from_rk]
- [predict_from_rk]
- [list_session_files]

### Query Results
#### ternary_viscosity
**L1_query_1** — status: success · validation: PASS

**Summary:** Viscosity data for the ternary mixture of N,N-dimethylformamide (DMF) + ethylene glycol (1,2-ethanediol) + water at 298.15 K were found in the ThermoML database (DOI 10.1021/je060113j, GLOBlit_8892, PROPblock_38). Measured by capillary tube (Ostwald–Ubbelohde) in the liquid phase at 101.0 kPa, 11 data points at 298.15 K span the full water mole-fraction range from 0 to 1. Viscosity values are: x(water)=0.0000, x(ethanediol)=0.5408, η=0.0030647 Pa·s; x(water)=0.2929, x(ethanediol)=0.3824, η=0.0035692 Pa·s; x(water)=0.4825, x(ethanediol)=0.2799, η=0.0037485 Pa·s; x(water)=0.6152, x(ethanediol)=0.2081, η=0.0034817 Pa·s; x(water)=0.7132, x(ethanediol)=0.1551, η=0.0032008 Pa·s; x(water)=0.7886, x(ethanediol)=0.1143, η=0.0028546 Pa·s; x(water)=0.8484, x(ethanediol)=0.0820, η=0.0024439 Pa·s; x(water)=0.8969, x(ethanediol)=0.0557, η=0.0019531 Pa·s; x(water)=0.9372, x(ethanediol)=0.0339, η=0.0016778 Pa·s; x(water)=0.9711, x(ethanediol)=0.0156, η=0.0013057 Pa·s; x(water)=1.0000, x(ethanediol)=0.0000, η=0.0008904 Pa·s. The viscosity shows a non-monotonic trend, rising from 0.0030647 Pa·s at x(water)=0 to a maximum of 0.0037485 Pa·s near x(water)≈0.48, then decreasing to 0.0008904 Pa·s for pure water, characteristic of strongly hydrogen-bonding ternary systems. The full data block contains 33 points covering 298.15 K to 318.15 K with viscosities ranging from 0.000596 to 0.0037485 Pa·s.

**Answer:**

Viscosity data for the ternary mixture of N,N-dimethylformamide (DMF) + ethylene glycol (1,2-ethanediol) + water at 298.15 K were found in the ThermoML database.

**Source:** DOI 10.1021/je060113j (GLOBlit_8892), PROPblock_38  
**Method:** Capillary tube (Ostwald–Ubbelohde), liquid phase  
**Pressure:** 101.0 kPa (fixed constraint)  
**Compounds:** DMF (GLOBcomp_18), 1,2-ethanediol (GLOBcomp_24), water (GLOBcomp_1)

There are **11 data points at 298.15 K** spanning the full water mole-fraction range from 0 to 1 (the third component, DMF, makes up the balance). The data are tabulated below:

**WM_L1#1_Table#1_(Analysis_L1#1_Answer):**

| *row_id* | *x(water)* | *x(1,2-ethanediol)* | *Viscosity (Pa·s)* |
|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「0.0000」 | 「0.5408」 | 「0.0030647」 |
| WM_L1#1_Table#1_Row#2 | 「0.2929」 | 「0.3824」 | 「0.0035692」 |
| WM_L1#1_Table#1_Row#3 | 「0.4825」 | 「0.2799」 | 「0.0037485」 |
| WM_L1#1_Table#1_Row#4 | 「0.6152」 | 「0.2081」 | 「0.0034817」 |
| WM_L1#1_Table#1_Row#5 | 「0.7132」 | 「0.1551」 | 「0.0032008」 |
| WM_L1#1_Table#1_Row#6 | 「0.7886」 | 「0.1143」 | 「0.0028546」 |
| WM_L1#1_Table#1_Row#7 | 「0.8484」 | 「0.0820」 | 「0.0024439」 |
| WM_L1#1_Table#1_Row#8 | 「0.8969」 | 「0.0557」 | 「0.0019531」 |
| WM_L1#1_Table#1_Row#9 | 「0.9372」 | 「0.0339」 | 「0.0016778」 |
| WM_L1#1_Table#1_Row#10 | 「0.9711」 | 「0.0156」 | 「0.0013057」 |
| WM_L1#1_Table#1_Row#11 | 「1.0000」 | 「0.0000」 | 「0.0008904」 |

**Chemistry insight:** The viscosity exhibits a non-monotonic trend with composition. Starting from the DMF + ethylene glycol binary end (x_water = 0, η = 0.0030647 Pa·s), the viscosity increases as water is added, reaching a maximum of 0.0037485 Pa·s near x(water) ≈ 0.48. Beyond this composition, the viscosity decreases steadily as the mixture becomes more water-rich, dropping to 0.0008904 Pa·s for pure water. This maximum in viscosity at intermediate compositions is characteristic of strongly hydrogen-bonding ternary systems, where the interplay of DMF–water and ethylene glycol–water interactions enhances intermolecular association beyond what either binary pair alone would produce.

The full block contains 33 data points covering temperatures from 298.15 K to 318.15 K, with viscosity values ranging from 0.000596 to 0.0037485 Pa·s across all temperatures and compositions.

**Core claims:**
- Viscosity data for the ternary mixture DMF + ethylene glycol + water at 298.15 K and 101.0 kPa were found in the ThermoML database (DOI 10.1021/je060113j), comprising 11 data points spanning the full water mole-fraction range from 0 to 1.
- The viscosity exhibits a non-monotonic trend with composition: starting at 0.0030647 Pa·s for the DMF + ethylene glycol binary end (x_water = 0), it increases to a maximum of 0.0037485 Pa·s near x(water) ≈ 0.48, then decreases steadily to 0.0008904 Pa·s for pure water.
- The viscosity maximum at intermediate compositions is attributed to strongly hydrogen-bonding interactions in the ternary system, where DMF–water and ethylene glycol–water interactions enhance intermolecular association beyond what either binary pair alone would produce.
- The full data block contains 33 data points covering temperatures from 298.15 K to 318.15 K, with viscosity values ranging from 0.000596 to 0.0037485 Pa·s across all temperatures and compositions.

**Core blocks found:**

**WM_L1#1_Blocks_(Analysis_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#2 | 「GLOBlit_8892」 | 「PROPblock_38」 | 「GLOBcomp_18, GLOBcomp_24, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity measurements for the ternary mixture N,N-dimethylformamide + 1,2-ethanediol + water at 298.15 K and 101.0 kPa, with 11 data points spanning the full water mole-fraction range.」 |

*Not stored here: 1 verbatim data_inspections table(s); 4 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### binary_DMF_water
**L1_query_2** — status: success · validation: PASS

**Summary:** Dynamic viscosity (Pa·s) data for the binary system N,N-dimethylformamide (DMF) + water at 298.15 K were found in four data blocks. Two key blocks were inspected in detail. Block 1 (DOI 10.1021/je050209y, GLOBlit_8676::PROPblock_9) reports 11 points at 298.15 K and 101.325 kPa as a function of DMF mole fraction, with viscosities ranging from 0.000843 to 0.002491 Pa·s across x(DMF) = 0.05–0.9488. Block 2 (DOI 10.1021/je300608v, GLOBlit_9900::PROPblock_3) reports 15 points at 298.15 K and 101.0 kPa as a function of water mole fraction, with viscosities ranging from 0.0008045 to 0.0024775 Pa·s across x(water) = 0–1. Both datasets exhibit a pronounced viscosity maximum near ~30 mol% DMF / ~70 mol% water (0.002491 Pa·s in Block 1 at x(DMF) ≈ 0.3; 0.0024775 Pa·s in Block 2 at x(water) ≈ 0.7), attributed to strong DMF–water hydrogen-bonding interactions forming structured molecular associations. Two additional blocks were also returned but not inspected in detail.

**Answer:**

#### Dynamic Viscosity Data for Binary DMF + Water Mixtures near 298.15 K

**Compounds:** N,N-dimethylformamide (DMF, GLOBcomp_18) and water (GLOBcomp_1)  
**Property:** Dynamic viscosity (GLOBprop_4, Pa·s)  
**System type:** Binary

##### Data Blocks Found

Four blocks of dynamic viscosity data for binary DMF + water were identified. Two key blocks with inspected data at 298.15 K are detailed below:

---

**Block 1: GLOBlit_8676 :: PROPblock_9**  
DOI: 10.1021/je050209y  
Total points: 11 | Temperature: 298.15 K (fixed) | Pressure: 101.325 kPa  
Composition variable: mole fraction of DMF

**WM_L1#2_Table#1_(Analysis_L1#2_Answer):**

| *row_id* | *x(DMF)* | *Viscosity (Pa·s)* |
|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「0.05」 | 「0.00131」 |
| WM_L1#2_Table#1_Row#2 | 「0.1001」 | 「0.001728」 |
| WM_L1#2_Table#1_Row#3 | 「0.2」 | 「0.002346」 |
| WM_L1#2_Table#1_Row#4 | 「0.299」 | 「0.002491」 |
| WM_L1#2_Table#1_Row#5 | 「0.3998」 | 「0.002273」 |
| WM_L1#2_Table#1_Row#6 | 「0.4997」 | 「0.001878」 |
| WM_L1#2_Table#1_Row#7 | 「0.5993」 | 「0.001532」 |
| WM_L1#2_Table#1_Row#8 | 「0.6995」 | 「0.001243」 |
| WM_L1#2_Table#1_Row#9 | 「0.8」 | 「0.001045」 |
| WM_L1#2_Table#1_Row#10 | 「0.8991」 | 「0.000901」 |
| WM_L1#2_Table#1_Row#11 | 「0.9488」 | 「0.000843」 |

Viscosity range: 0.000843–0.002491 Pa·s across x(DMF) = 0.05–0.9488.

---

**Block 2: GLOBlit_9900 :: PROPblock_3**  
DOI: 10.1021/je300608v  
Total points: 60 (full block, 293.15–308.15 K) | 15 points at 298.15 K | Pressure: 101.0 kPa  
Composition variable: mole fraction of water

**WM_L1#2_Table#2_(Analysis_L1#2_Answer):**

| *row_id* | *x(water)* | *Viscosity (Pa·s)* |
|---|---|---|
| WM_L1#2_Table#2_Row#1 | 「0」 | 「0.0008045」 |
| WM_L1#2_Table#2_Row#2 | 「0.1」 | 「0.0009018」 |
| WM_L1#2_Table#2_Row#3 | 「0.2」 | 「0.0010386」 |
| WM_L1#2_Table#2_Row#4 | 「0.3」 | 「0.0012331」 |
| WM_L1#2_Table#2_Row#5 | 「0.4」 | 「0.0015078」 |
| WM_L1#2_Table#2_Row#6 | 「0.5」 | 「0.0018528」 |
| WM_L1#2_Table#2_Row#7 | 「0.6」 | 「0.0022264」 |
| WM_L1#2_Table#2_Row#8 | 「0.7」 | 「0.0024775」 |
| WM_L1#2_Table#2_Row#9 | 「0.8」 | 「0.0023495」 |
| WM_L1#2_Table#2_Row#10 | 「0.9」 | 「0.0017464」 |
| WM_L1#2_Table#2_Row#11 | 「0.94」 | 「0.0014116」 |
| WM_L1#2_Table#2_Row#12 | 「1」 | 「0.0008903」 |

Viscosity range at 298.15 K: 0.0008045–0.0024775 Pa·s across x(water) = 0–1.

---

Two additional blocks were also returned in the search (4 total), including one from GLOBlit_11030 (temperature range not inspected in this run).

**Chemistry insight:** Both datasets show a pronounced viscosity maximum at intermediate compositions — near x(DMF) ≈ 0.3 in Block 1 (GLOBlit_8676::PROPblock_9, 0.002491 Pa·s) and near x(water) ≈ 0.7 in Block 2 (GLOBlit_9900::PROPblock_3, 0.0024775 Pa·s). These correspond to the same composition region (~30 mol% DMF / 70 mol% water), consistent with strong DMF–water hydrogen-bonding interactions that create structured molecular associations and enhance viscous resistance to flow at these intermediate compositions.

**Core claims:**
- Four blocks of dynamic viscosity data for binary DMF + water mixtures were identified, with two key blocks providing detailed measurements at 298.15 K and near-ambient pressure.
- Block 1 (DOI: 10.1021/je050209y) reports 11 viscosity values at 298.15 K and 101.325 kPa spanning x(DMF) = 0.05–0.9488, with viscosity ranging from 0.000843 to 0.002491 Pa·s.
- Block 2 (DOI: 10.1021/je300608v) reports 12 viscosity values at 298.15 K and 101.0 kPa spanning x(water) = 0–1, with viscosity ranging from 0.0008045 to 0.0024775 Pa·s.
- Both datasets show a pronounced viscosity maximum at intermediate compositions near ~30 mol% DMF / 70 mol% water (0.002491 Pa·s in Block 1 at x(DMF) ≈ 0.3; 0.0024775 Pa·s in Block 2 at x(water) ≈ 0.7), consistent with strong DMF–water hydrogen-bonding interactions that create structured molecular associations and enhance viscous resistance to flow.

**Core blocks found:**

**WM_L1#2_Blocks_(Analysis_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#3 | 「GLOBlit_8676」 | 「PROPblock_9」 | 「GLOBcomp_18, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of binary DMF + water at 298.15 K and 101.325 kPa as a function of DMF mole fraction (11 points, viscosity range 0.000843–0.002491 Pa·s).」 |
| WM_L1#2_Table#4 | 「GLOBlit_9900」 | 「PROPblock_3」 | 「GLOBcomp_18, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of binary DMF + water at 293.15–308.15 K and 101.0 kPa as a function of water mole fraction (60 total points, 15 at 298.15 K, viscosity range at 298.15 K: 0.0008045–0.0024775 Pa·s).」 |

*Not stored here: 2 verbatim data_inspections table(s); 3 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### binary_DMF_EG
**L1_query_3** — status: success · validation: PASS

**Summary:** A single data block from DOI 10.1021/je060113j (GLOBlit_8892, PROPblock_25) reports the dynamic viscosity of the binary system N,N-dimethylformamide (DMF) + 1,2-ethanediol (ethylene glycol) at a fixed mole fraction of 1,2-ethanediol = 0.5408 and 101.0 kPa, measured by capillary tube method in the liquid phase. Three data points are provided: at 298.15 K the viscosity is 0.0030647 Pa·s, at 308.15 K it is 0.0024529 Pa·s, and at 318.15 K it is 0.0019599 Pa·s. Viscosity decreases monotonically with increasing temperature. No additional composition-sweep blocks were found for this binary system in the database.

**Answer:**

**Viscosity data for binary DMF + ethylene glycol mixtures near 298.15 K**

One data block was found in the ThermoML database for the dynamic viscosity of the binary system N,N-dimethylformamide (DMF) + 1,2-ethanediol (ethylene glycol):

- **DOI:** 10.1021/je060113j (GLOBlit_8892)
- **Block:** PROPblock_25
- **Compounds:** GLOBcomp_18 (dimethylformamide), GLOBcomp_24 (1,2-ethanediol)
- **Property:** Dynamic viscosity (GLOBprop_4), measured by capillary tube method (GLOBmeas_4), liquid phase
- **Composition:** Fixed mole fraction of 1,2-ethanediol = 0.5408
- **Pressure:** 101.0 kPa

The block contains 3 data points at three temperatures:

**WM_L1#3_Table#1_(Analysis_L1#3_Answer):**

| *row_id* | *BLKpoint_id* | *Temperature (K)* | *x(1,2-ethanediol)* | *Pressure (kPa)* | *Viscosity (Pa·s)* |
|---|---|---|---|---|---|
| WM_L1#3_Table#1_Row#1 | 「BLKpoint_1」 | 「298.15」 | 「0.5408」 | 「101.0」 | 「0.0030647」 |
| WM_L1#3_Table#1_Row#2 | 「BLKpoint_2」 | 「308.15」 | 「0.5408」 | 「101.0」 | 「0.0024529」 |
| WM_L1#3_Table#1_Row#3 | 「BLKpoint_3」 | 「318.15」 | 「0.5408」 | 「101.0」 | 「0.0019599」 |

At exactly 298.15 K, the viscosity is **0.0030647 Pa·s** (≈ 3.06 mPa·s).

**Chemistry note:** The viscosity decreases monotonically with increasing temperature (near-linear, R² = 0.9962), as expected for liquid mixtures. This block provides data at only one composition (x_EG = 0.5408); no additional composition-sweep blocks were found for this binary system in the database.

**Core claims:**
- In the ThermoML database (DOI 10.1021/je060113j), the dynamic viscosity of the binary DMF + ethylene glycol mixture at a fixed 1,2-ethanediol mole fraction of 0.5408 and 101.0 kPa is reported as 0.0030647 Pa·s at 298.15 K, 0.0024529 Pa·s at 308.15 K, and 0.0019599 Pa·s at 318.15 K, decreasing monotonically with increasing temperature consistent with expected liquid-mixture behavior, with only one composition (x_EG = 0.5408) available for this binary system in the database.

**Core blocks found:**

**WM_L1#3_Blocks_(Analysis_L1#3_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#3_Table#2 | 「GLOBlit_8892」 | 「PROPblock_25」 | 「GLOBcomp_18, GLOBcomp_24」 | 「GLOBprop_4」 | 「Dynamic viscosity of binary dimethylformamide + 1,2-ethanediol at 298.15–318.15 K, fixed x(1,2-ethanediol) = 0.5408, 101.0 kPa, capillary tube method.」 |

*Not stored here: 1 verbatim data_inspections table(s); 5 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### binary_EG_water
**L1_query_4** — status: success · validation: FLAGGED(2)

**Summary:** Dynamic viscosity (GLOBprop_4, Pa·s) data for binary mixtures of ethylene glycol (GLOBcomp_24, OCCO) and water (GLOBcomp_1) near 298.15 K were identified across five data blocks. The most data-rich blocks are GLOBlit_5201::PROPblock_24 (84 points, 293.15–308.15 K, mole fraction EG, 92.3 kPa) and GLOBlit_8038::PROPblock_5 (77 points, 293.15–353.15 K, mole fraction EG, 101.0 kPa). Additional blocks include GLOBlit_2656::PROPblock_13 (10 points at 293.15 K, mass fraction EG, 101.325 kPa), GLOBlit_6951::PROPblock_18 (33 points, 293.15–303.15 K, mole fraction water, 100.0 kPa), and GLOBlit_8106::PROPblock_5 (30 points, 296.45–449.85 K, mole fraction EG, 100.0 kPa). Representative values at 298.15 K from GLOBlit_5201::PROPblock_24: pure water viscosity 0.00089689 Pa·s, mole fraction EG 0.2072 gives 0.0028109 Pa·s, mole fraction EG 0.4446 gives 0.0060624 Pa·s, pure EG gives 0.016223 Pa·s. From GLOBlit_6951::PROPblock_18 at 298.15 K: pure EG (mole fraction water 0) gives 0.01724 Pa·s, mole fraction water 0.2014 gives 0.01219 Pa·s, mole fraction water 0.4011 gives 0.00831 Pa·s, mole fraction water 0.6995 gives 0.003884 Pa·s, pure water gives 0.000843 Pa·s. Viscosity increases strongly and nonlinearly with ethylene glycol content, reflecting the extensive hydrogen-bonding network of its two hydroxyl groups.

**Answer:**

**Viscosity data for binary ethylene glycol (1,2-ethanediol) + water mixtures near 298.15 K**

**Compounds resolved:**
- Ethylene glycol (1,2-ethanediol): **GLOBcomp_24** (C₂H₆O₂, SMILES: OCCO)
- Water: **GLOBcomp_1** (H₂O)

**Property:** Dynamic viscosity (GLOBprop_4), units: Pa·s

Five inspected data blocks were found for binary liquid-phase mixtures covering temperatures near 298.15 K:

**WM_L1#4_Table#1_(Analysis_L1#4_Answer):**

| *row_id* | *#* | *DOI* | *Block* | *Literature ID* | *Data Points* | *T range (K)* | *Composition Variable* | *P (kPa)* |
|---|---|---|---|---|---|---|---|---|
| WM_L1#4_Table#1_Row#1 | 「1」 | 「10.1016/j.jct.2006.01.011」 | 「PROPblock_13」 | 「GLOBlit_2656」 | 「10」 | 「293.15–293.15」 | 「mass fraction EG (GLOBcomp_24)」 | 「101.325」 |
| WM_L1#4_Table#1_Row#2 | 「2」 | 「10.1016/j.jct.2018.02.022」 | 「PROPblock_24」 | 「GLOBlit_5201」 | 「84」 | 「293.15–308.15」 | 「mole fraction EG (GLOBcomp_24)」 | 「92.3」 |
| WM_L1#4_Table#1_Row#3 | 「3」 | 「10.1021/acs.jced.6b00526」 | 「PROPblock_18」 | 「GLOBlit_6951」 | 「33」 | 「293.15–303.15」 | 「mole fraction water (GLOBcomp_1)」 | 「100.0」 |
| WM_L1#4_Table#1_Row#4 | 「4」 | 「10.1021/je020140j」 | 「PROPblock_5」 | 「GLOBlit_8038」 | 「77」 | 「293.15–353.15」 | 「mole fraction EG (GLOBcomp_24)」 | 「101.0」 |
| WM_L1#4_Table#1_Row#5 | 「5」 | 「10.1021/je025610o」 | 「PROPblock_5」 | 「GLOBlit_8106」 | 「30」 | 「296.45–449.85」 | 「mole fraction EG (GLOBcomp_24)」 | 「100.0」 |

A sixth block was also matched in the initial search but its details were truncated; the five blocks above were fully inspected.

**Representative data near 298.15 K:**

From GLOBlit_5201::PROPblock_24 (at 298.15 K, 92.3 kPa):

**WM_L1#4_Table#2_(Analysis_L1#4_Answer):**

| *row_id* | *Mole fraction EG* | *Viscosity (Pa·s)* |
|---|---|---|
| WM_L1#4_Table#2_Row#1 | 「0」 | 「0.00089689」 |
| WM_L1#4_Table#2_Row#2 | 「0.2072」 | 「0.0028109」 |
| WM_L1#4_Table#2_Row#3 | 「0.4446」 | 「0.0060624」 |
| WM_L1#4_Table#2_Row#4 | 「1」 | 「0.016223」 |

From GLOBlit_6951::PROPblock_18 (at 298.15 K, 100.0 kPa):

**WM_L1#4_Table#3_(Analysis_L1#4_Answer):**

| *row_id* | *Mole fraction water* | *Viscosity (Pa·s)* |
|---|---|---|
| WM_L1#4_Table#3_Row#1 | 「0」 | 「0.01724」 |
| WM_L1#4_Table#3_Row#2 | 「0.2014」 | 「0.01219」 |
| WM_L1#4_Table#3_Row#3 | 「0.4011」 | 「0.00831」 |
| WM_L1#4_Table#3_Row#4 | 「0.6995」 | 「0.003884」 |
| WM_L1#4_Table#3_Row#5 | 「1」 | 「0.000843」 |

**Chemistry insight:** The viscosity of ethylene glycol–water mixtures increases strongly and nonlinearly with ethylene glycol content. In GLOBlit_5201::PROPblock_24 at 298.15 K, pure EG viscosity is 0.016223 Pa·s versus 0.00089689 Pa·s for pure water (a ratio of approximately 18×, derived by division). In GLOBlit_6951::PROPblock_18 at 298.15 K, pure EG viscosity is 0.01724 Pa·s versus 0.000843 Pa·s for pure water (a ratio of approximately 20×, derived by division). This reflects the extensive hydrogen-bonding network formed by the two hydroxyl groups of ethylene glycol. The most data-rich blocks near 298.15 K are GLOBlit_5201::PROPblock_24 (84 points, 293.15–308.15 K) and GLOBlit_8038::PROPblock_5 (77 points, 293.15–353.15 K), both using mole fraction of ethylene glycol as the composition variable.

**Core claims:**
- Five ThermoML data blocks were identified containing dynamic viscosity data for binary ethylene glycol (1,2-ethanediol) + water liquid mixtures near 298.15 K, with the most data-rich blocks being GLOBlit_5201::PROPblock_24 (84 points, 293.15–308.15 K) and GLOBlit_8038::PROPblock_5 (77 points, 293.15–353.15 K).
- At 298.15 K, the viscosity of ethylene glycol–water mixtures increases strongly and nonlinearly with ethylene glycol content; in GLOBlit_5201::PROPblock_24 pure EG viscosity is 0.016223 Pa·s versus 0.00089689 Pa·s for pure water, and in GLOBlit_6951::PROPblock_18 pure EG viscosity is 0.01724 Pa·s versus 0.000843 Pa·s for pure water.
- The strong increase in viscosity with ethylene glycol content is attributed to the extensive hydrogen-bonding network formed by the two hydroxyl groups of ethylene glycol.

**Core blocks found:**

**WM_L1#4_Blocks_(Analysis_L1#4_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#4_Table#4 | 「GLOBlit_2656」 | 「PROPblock_13」 | 「GLOBcomp_24, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of binary ethylene glycol + water at 293.15 K, mass fraction composition, 101.325 kPa.」 |
| WM_L1#4_Table#5 | 「GLOBlit_5201」 | 「PROPblock_24」 | 「GLOBcomp_24, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of binary ethylene glycol + water, 293.15–308.15 K, mole fraction composition, 92.3 kPa. 84 data points.」 |
| WM_L1#4_Table#6 | 「GLOBlit_6951」 | 「PROPblock_18」 | 「GLOBcomp_24, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of binary ethylene glycol + water, 293.15–303.15 K, mole fraction of water composition, 100.0 kPa. 33 data points.」 |
| WM_L1#4_Table#7 | 「GLOBlit_8038」 | 「PROPblock_5」 | 「GLOBcomp_24, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of binary ethylene glycol + water, 293.15–353.15 K, mole fraction composition, 101.0 kPa. 77 data points.」 |
| WM_L1#4_Table#8 | 「GLOBlit_8106」 | 「PROPblock_5」 | 「GLOBcomp_24, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of binary ethylene glycol + water, 296.45–449.85 K, mole fraction composition, 100.0 kPa. 30 data points.」 |

*Not stored here: 5 verbatim data_inspections table(s); 2 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(2) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **AMBIGUOUS_VALUE** PROPblock_5: 298.15 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean
- **UNINSPECTED_VALUE** GLOBlit_5201::PROPblock_24: 18 exists in PROPblock_24's database table but was never shown in an inspection of this run


### Inspected Blocks
- GLOBlit_9900 | 10.1021/je300608v | PROPblock_3: 60 rows; x=['mole_fraction_<water>']; y=['viscosity_pa_s']
    - BLKprop_1 / GLOBprop_4: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_4: kind=direct; materialize_reference=False; supported=True; units=Pa*s -> Pa*s

### Completed Fits
  - DMF_water [10.1021/je300608v/PROPblock_3] (water, dimethylformamide): RK order=5, R²=0.999973, RMSE=0.0015230866140327202, coeffs=[3.140292, 3.885439, 1.915786, -0.005693, 0.041789, 0.390893]
      response: direct via X = reported X | 0 reference source(s) | Pa*s -> Pa*s
      pure refs: water=0.0008903, dimethylformamide=0.0008045 [block-edges (dimethylformamide: direct/good, water: direct/good)]
      fit_csv: $ROOT/data\10_1021_je300608v_BPROPblock_3_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1021_je300608v_BPROPblock_3_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1021_je300608v_BPROPblock_3_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1021_je300608v_BPROPblock_3_T298.1_excess.png
  - EG_water [10.1016/j.jct.2018.02.022/PROPblock_24] (1,2-ethanediol, water): RK order=3, R²=0.99994, RMSE=0.0013198945265291695, coeffs=[2.39674, -1.044444, 0.668173, -0.3209]
      response: direct via X = reported X | 0 reference source(s) | Pa*s -> Pa*s
      pure refs: 1,2-ethanediol=0.016223, water=0.00089689 [block-edges (water: direct/good, 1,2-ethanediol: direct/good)]
      fit_csv: $ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_excess.png

## Session Output Files

### data
- `$ROOT/data\10_1021_je300608v_BPROPblock_3_T298.1_fit.csv` — RK fit data — 10.1021/je300608v PROPblock_3_T298.1
- `$ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_fit.csv` — RK fit data — 10.1016/j.jct.2018.02.022 PROPblock_24_T298.1
- `$ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_excess.csv` — Excess property — 10.1016/j.jct.2018.02.022 PROPblock_24_T298.1
- `$ROOT/data\10_1021_je300608v_BPROPblock_3_T298.1_excess.csv` — Excess property — 10.1021/je300608v PROPblock_3_T298.1

### plot
- `$ROOT/plots\10_1021_je300608v_BPROPblock_3_T298.1_fit.png` — RK fit plot — 10.1021/je300608v PROPblock_3_T298.1
- `$ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_fit.png` — RK fit plot — 10.1016/j.jct.2018.02.022 PROPblock_24_T298.1
- `$ROOT/plots\10_1021_je300608v_BPROPblock_3_T298.1_excess.png` — Excess plot — 10.1021/je300608v PROPblock_3_T298.1
- `$ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_excess.png` — Excess plot — 10.1016/j.jct.2018.02.022 PROPblock_24_T298.1

</memory>

## User
What viscosity should I expect for an equimolar DMF + ethylene glycol + water liquid mixture at 25 °C? If it has not been measured directly, give the most defensible estimate, explain the chemical and mathematical basis of every inferred contribution, and identify the measurements supporting it.

## Assistant
<summary>Starting search for viscosity data: ternary DMF+ethylene glycol+water system, and all three binary pairs. Will search in parallel.</summary>
<tool_call>query_thermoml_parallel(queries=[{'label': 'terna…)</tool_call>

## User
<tool_result>
{
  "error": "queries[0] has missing=['context'] and unknown=[] fields",
  "error_code": "TOOL_EXECUTION_ERROR",
  "tool": "query_thermoml_parallel"
}
</tool_result>

## Assistant
<summary>Fixing query format to include required `context` field. Searching for ternary DMF+ethylene glycol+water viscosity and all three binary pairs in parallel.</summary>
<tool_call>query_thermoml_parallel(queries=[{'label': 'terna…)</tool_call>

## User
<tool_result>
{
  "error": "queries[0].id_catalog must be an array",
  "error_code": "TOOL_EXECUTION_ERROR",
  "tool": "query_thermoml_parallel"
}
</tool_result>

## Assistant
<summary>Fixing query format - id_catalog must be an array. Searching for ternary and binary viscosity data for DMF + ethylene glycol + water system.</summary>
<tool_call>query_thermoml_parallel(queries=[{'label': 'terna…)</tool_call>

## User
<tool_result>
[TOOL_RESULT_SIZE_WARNING: query_thermoml_parallel returned 78,200 characters after result processing; the target is 24,000. The full result follows — prefer narrower requests, and rely on your working memory for recall instead of re-running this call.]

<subagent_answer>
### QP#3 — query_thermoml_parallel return

**Entity summary:** n_queries=4

**Other fields:**
- results: [{"label": "ternary_viscosity", "result": {"answer": "Viscosity data for the ternary mixture of N,N-dimethylformamide (DMF) + ethylene glycol (1,2-ethanediol) + water at 298.15 K were found in the ThermoML database.\n\n**Source:** DOI 10.1021/je060113j (GLOBlit_8892), PROPblock_38  \n**Method:** Capillary tube (Ostwald–Ubbelohde), liquid phase  \n**Pressure:** 101.0 kPa (fixed constraint)  \n**Compounds:** DMF (GLOBcomp_18), 1,2-ethanediol (GLOBcomp_24), water (GLOBcomp_1)\n\nThere are **11 data points at 298.15 K** spanning the full water mole-fraction range from 0 to 1 (the third component, DMF, makes up the balance). The data are tabulated below:\n\n| x(water) | x(1,2-ethanediol) | Viscosity (Pa·s) |\n|---|---|---|\n| 0.0000 | 0.5408 | 0.0030647 |\n| 0.2929 | 0.3824 | 0.0035692 |\n| 0.4825 | 0.2799 | 0.0037485 |\n| 0.6152 | 0.2081 | 0.0034817 |\n| 0.7132 | 0.1551 | 0.0032008 |\n| 0.7886 | 0.1143 | 0.0028546 |\n| 0.8484 | 0.0820 | 0.0024439 |\n| 0.8969 | 0.0557 | 0.0019531 |\n| 0.9372 | 0.0339 | 0.0016778 |\n| 0.9711 | 0.0156 | 0.0013057 |\n| 1.0000 | 0.0000 | 0.0008904 |\n\n**Chemistry insight:** The viscosity exhibits a non-monotonic trend with composition. Starting from the DMF + ethylene glycol binary end (x_water = 0, η = 0.0030647 Pa·s), the viscosity increases as water is added, reaching a maximum of 0.0037485 Pa·s near x(water) ≈ 0.48. Beyond this composition, the viscosity decreases steadily as the mixture becomes more water-rich, dropping to 0.0008904 Pa·s for pure water. This maximum in viscosity at intermediate compositions is characteristic of strongly hydrogen-bonding ternary systems, where the interplay of DMF–water and ethylene glycol–water interactions enhances intermolecular association beyond what either binary pair alone would produce.\n\nThe full block contains 33 data points covering temperatures from 298.15 K to 318.15 K, with viscosity values ranging from 0.000596 to 0.0037485 Pa·s across all temperatures and compositions.", "core_claims": ["Viscosity data for the ternary mixture DMF + ethylene glycol + water at 298.15 K and 101.0 kPa were found in the ThermoML database (DOI 10.1021/je060113j), comprising 11 data points spanning the full water mole-fraction range from 0 to 1.", "The viscosity exhibits a non-monotonic trend with composition: starting at 0.0030647 Pa·s for the DMF + ethylene glycol binary end (x_water = 0), it increases to a maximum of 0.0037485 Pa·s near x(water) ≈ 0.48, then decreases steadily to 0.0008904 Pa·s for pure water.", "The viscosity maximum at intermediate compositions is attributed to strongly hydrogen-bonding interactions in the ternary system, where DMF–water and ethylene glycol–water interactions enhance intermolecular association beyond what either binary pair alone would produce.", "The full data block contains 33 data points covering temperatures from 298.15 K to 318.15 K, with viscosity values ranging from 0.000596 to 0.0037485 Pa·s across all temperatures and compositions."], "status": "success", "summary": "Viscosity data for the ternary mixture of N,N-dimethylformamide (DMF) + ethylene glycol (1,2-ethanediol) + water at 298.15 K were found in the ThermoML database (DOI 10.1021/je060113j, GLOBlit_8892, PROPblock_38). Measured by capillary tube (Ostwald–Ubbelohde) in the liquid phase at 101.0 kPa, 11 data points at 298.15 K span the full water mole-fraction range from 0 to 1. Viscosity values are: x(water)=0.0000, x(ethanediol)=0.5408, η=0.0030647 Pa·s; x(water)=0.2929, x(ethanediol)=0.3824, η=0.0035692 Pa·s; x(water)=0.4825, x(ethanediol)=0.2799, η=0.0037485 Pa·s; x(water)=0.6152, x(ethanediol)=0.2081, η=0.0034817 Pa·s; x(water)=0.7132, x(ethanediol)=0.1551, η=0.0032008 Pa·s; x(water)=0.7886, x(ethanediol)=0.1143, η=0.0028546 Pa·s; x(water)=0.8484, x(ethanediol)=0.0820, η=0.0024439 Pa·s; x(water)=0.8969, x(ethanediol)=0.0557, η=0.0019531 Pa·s; x(water)=0.9372, x(ethanediol)=0.0339, η=0.0016778 Pa·s; x(water)=0.9711, x(ethanediol)=0.0156, η=0.0013057 Pa·s; x(water)=1.0000, x(ethanediol)=0.0000, η=0.0008904 Pa·s. The viscosity shows a non-monotonic trend, rising from 0.0030647 Pa·s at x(water)=0 to a maximum of 0.0037485 Pa·s near x(water)≈0.48, then decreasing to 0.0008904 Pa·s for pure water, characteristic of strongly hydrogen-bonding ternary systems. The full data block contains 33 points covering 298.15 K to 318.15 K with viscosities ranging from 0.000596 to 0.0037485 Pa·s.", "core_id_updates": [{"action": "add", "core_GLOB_id": "GLOBcomp_18", "registry_id": "dimethylformamide", "name": "dimethylformamide"}, {"action": "add", "core_GLOB_id": "GLOBcomp_24", "registry_id": "1,2-ethanediol", "name": "1,2-ethanediol"}, {"action": "add", "core_GLOB_id": "GLOBcomp_1", "registry_id": "water", "name": "water"}, {"action": "add", "core_GLOB_id": "GLOBlit_8892", "registry_id": "2006-sin-roy-0", "name": "10.1021/je060113j"}], "core_blocks_found": [{"lit_num_id": "GLOBlit_8892", "block_number": "PROPblock_38", "BLKsubsys_id": null, "system_type": "ternary", "comp_num_ids": ["GLOBcomp_18", "GLOBcomp_24", "GLOBcomp_1"], "prop_num_ids": ["GLOBprop_4"], "description": "Dynamic viscosity measurements for the ternary mixture N,N-dimethylformamide + 1,2-ethanediol + water at 298.15 K and 101.0 kPa, with 11 data points spanning the full water mole-fraction range.", "doi": "10.1021/je060113j", "lit_id": "2006-sin-roy-0", "block_type": "PureOrMixtureData", "blocktype_num_id": "GLOBblocktype_3", "n_datapoints": 33, "n_components": 3, "compounds": [{"org_num": "DOIcomp_4", "comp_num_id": "GLOBcomp_18", "name": "dimethylformamide", "formula": "C3H7NO", "inchi_key": "ZMXDDKWLCZADIW-UHFFFAOYSA-N", "SMILES": "CN(C)C=O", "sample_num": "DOIcompSample_4_1"}, {"org_num": "DOIcomp_1", "comp_num_id": "GLOBcomp_24", "name": "1,2-ethanediol", "formula": "C2H6O2", "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N", "SMILES": "OCCO", "sample_num": "DOIcompSample_1_1"}, {"org_num": "DOIcomp_6", "comp_num_id": "GLOBcomp_1", "name": "water", "formula": "H2O", "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N", "SMILES": "O", "sample_num": "DOIcompSample_6_1"}], "solvents": [], "constraints": [{"BLKconstr_id": "BLKconstr_1", "constr_num_id": "GLOBconstr_1", "constr_id": "pressure_kpa", "name": "Pressure, kPa", "type": "ePressure", "value": 101.0, "digits": 3, "component_org_num": null, "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}}], "variables": [{"BLKvar_id": "BLKvar_1", "var_num_id": "GLOBvar_1", "var_id": "temperature_k", "name": "Temperature, K", "type": "eTemperature", "component_org_num": null, "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, "range": {"BLKvar_id": "BLKvar_1", "name": "Temperature, K", "min": 298.15, "max": 318.15, "n_unique": 3}, "range_min": 298.15, "range_max": 318.15}, {"BLKvar_id": "BLKvar_2", "var_num_id": "GLOBvar_2", "var_id": "mole_fraction_DOIcomp_6", "name": "Mole fraction", "type": "eComponentComposition", "component_org_num": "DOIcomp_6", "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, "range": {"BLKvar_id": "BLKvar_2", "name": "Mole fraction", "min": 0.0, "max": 1.0, "n_unique": 11}, "range_min": 0.0, "range_max": 1.0}, {"BLKvar_id": "BLKvar_3", "var_num_id": "GLOBvar_2", "var_id": "mole_fraction_DOIcomp_1", "name": "Mole fraction", "type": "eComponentComposition", "component_org_num": "DOIcomp_1", "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, "range": {"BLKvar_id": "BLKvar_3", "name": "Mole fraction", "min": 0.0, "max": 0.5408, "n_unique": 11}, "range_min": 0.0, "range_max": 0.5408}], "properties": [{"BLKprop_id": "BLKprop_1", "prop_num_id": "GLOBprop_4", "prop_ID": "viscosity_pa_s", "name": "Viscosity, Pa*s", "group": "TransportProp", "component_org_num": null, "meas_num_id": "GLOBmeas_4", "meas_ID": "capillary_tube_ostwald_ubbelohde_method", "method_standard": "Capillary tube (Ostwald; Ubbelohde) method", "method_custom": null, "range": {"BLKprop_id": "BLKprop_1", "name": "Viscosity, Pa*s", "min": 0.000596, "max": 0.003749, "mean": 0.002038, "std": 0.000839, "n": 33}, "uncertainty": {"evaluation_method": "Propagation of evaluated standard uncertainties", "confidence_level": 95, "evaluator": "Data file compiler", "assessment_num": "BLKpropAssessment_1_1"}, "range_min": 0.000596, "range_max": 0.003749}], "phases": [{"owner_id": "BLKprop_1", "role": "property_phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKvar_1", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKvar_2", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKvar_3", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKconstr_1", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}], "reaction_type": null, "participants": [], "notes": null, "declared_system_type": "ternary", "declared_n_components": 3, "declared_compounds": [{"org_num": "DOIcomp_4", "comp_num_id": "GLOBcomp_18", "name": "dimethylformamide", "formula": "C3H7NO", "inchi_key": "ZMXDDKWLCZADIW-UHFFFAOYSA-N", "SMILES": "CN(C)C=O", "sample_num": "DOIcompSample_4_1"}, {"org_num": "DOIcomp_1", "comp_num_id": "GLOBcomp_24", "name": "1,2-ethanediol", "formula": "C2H6O2", "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N", "SMILES": "OCCO", "sample_num": "DOIcompSample_1_1"}, {"org_num": "DOIcomp_6", "comp_num_id": "GLOBcomp_1", "name": "water", "formula": "H2O", "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N", "SMILES": "O", "sample_num": "DOIcompSample_6_1"}], "parent_n_datapoints": 33, "subsystem_scope": null, "subsystem_point_runs": [], "subsystem_path_class": null, "subsystem_evidence_quality": null, "subsystem_condition_ranges": []}], "data_inspections": [{"doi": "10.1021/je060113j", "block_number": "PROPblock_38", "table_mode": "complete", "columns": ["BLKpoint_id", "temperature_k", "mole_fraction_<water>", "mole_fraction_<1,2-ethanediol>", "pressure_kpa", "viscosity_pa_s"], "rows_shown": [{"BLKpoint_id": "BLKpoint_1", "temperature_k": "298.15", "mole_fraction_<water>": "0", "mole_fraction_<1,2-ethanediol>": "0.5408", "pressure_kpa": "101.0", "viscosity_pa_s": "0.0030647"}, {"BLKpoint_id": "BLKpoint_2", "temperature_k": "298.15", "mole_fraction_<water>": "0.2929", "mole_fraction_<1,2-ethanediol>": "0.3824", "pressure_kpa": "101.0", "viscosity_pa_s": "0.0035692"}, {"BLKpoint_id": "BLKpoint_3", "temperature_k": "298.15", "mole_fraction_<water>": "0.4825", "mole_fraction_<1,2-ethanediol>": "0.2799", "pressure_kpa": "101.0", "viscosity_pa_s": "0.0037485"}, {"BLKpoint_id": "BLKpoint_4", "temperature_k": "298.15", "mole_fraction_<water>": "0.6152", "mole_fraction_<1,2-ethanediol>": "0.2081", "pressure_kpa": "101.0", "viscosity_pa_s": "0.0034817"}, {"BLKpoint_id": "BLKpoint_5", "temperature_k": "298.15", "mole_fraction_<water>": "0.7132", "mole_fraction_<1,2-ethanediol>": "0.1551", "pressure_kpa": "101.0", "viscosity_pa_s": "0.0032008"}, {"BLKpoint_id": "BLKpoint_6", "temperature_k": "298.15", "mole_fraction_<water>": "0.7886", "mole_fraction_<1,2-ethanediol>": "0.1143", "pressure_kpa": "101.0", "viscosity_pa_s": "0.0028546"}, {"BLKpoint_id": "BLKpoint_7", "temperature_k": "298.15", "mole_fraction_<water>": "0.8484", "mole_fraction_<1,2-ethanediol>": "0.082", "pressure_kpa": "101.0", "viscosity_pa_s": "0.0024439"}, {"BLKpoint_id": "BLKpoint_8", "temperature_k": "298.15", "mole_fraction_<water>": "0.8969", "mole_fraction_<1,2-ethanediol>": "0.0557", "pressure_kpa": "101.0", "viscosity_pa_s": "0.0019531"}, {"BLKpoint_id": "BLKpoint_9", "temperature_k": "298.15", "mole_fraction_<water>": "0.9372", "mole_fraction_<1,2-ethanediol>": "0.0339", "pressure_kpa": "101.0", "viscosity_pa_s": "0.0016778"}, {"BLKpoint_id": "BLKpoint_10", "temperature_k": "298.15", "mole_fraction_<water>": "0.9711", "mole_fraction_<1,2-ethanediol>": "0.0156", "pressure_kpa": "101.0", "viscosity_pa_s": "0.0013057"}, {"BLKpoint_id": "BLKpoint_11", "temperature_k": "298.15", "mole_fraction_<water>": "1", "mole_fraction_<1,2-ethanediol>": "0", "pressure_kpa": "101.0", "viscosity_pa_s": "0.0008904"}], "inspection_id": "INSP_ccb7677d8622", "lit_num_id": "GLOBlit_8892"}]}}, {"label": "binary_DMF_water", "result": {"answer": "## Dynamic Viscosity Data for Binary DMF + Water Mixtures near 298.15 K\n\n**Compounds:** N,N-dimethylformamide (DMF, GLOBcomp_18) and water (GLOBcomp_1)  \n**Property:** Dynamic viscosity (GLOBprop_4, Pa·s)  \n**System type:** Binary\n\n### Data Blocks Found\n\nFour blocks of dynamic viscosity data for binary DMF + water were identified. Two key blocks with inspected data at 298.15 K are detailed below:\n\n---\n\n**Block 1: GLOBlit_8676 :: PROPblock_9**  \nDOI: 10.1021/je050209y  \nTotal points: 11 | Temperature: 298.15 K (fixed) | Pressure: 101.325 kPa  \nComposition variable: mole fraction of DMF\n\n| x(DMF) | Viscosity (Pa·s) |\n|---|---|\n| 0.05 | 0.00131 |\n| 0.1001 | 0.001728 |\n| 0.2 | 0.002346 |\n| 0.299 | 0.002491 |\n| 0.3998 | 0.002273 |\n| 0.4997 | 0.001878 |\n| 0.5993 | 0.001532 |\n| 0.6995 | 0.001243 |\n| 0.8 | 0.001045 |\n| 0.8991 | 0.000901 |\n| 0.9488 | 0.000843 |\n\nViscosity range: 0.000843–0.002491 Pa·s across x(DMF) = 0.05–0.9488.\n\n---\n\n**Block 2: GLOBlit_9900 :: PROPblock_3**  \nDOI: 10.1021/je300608v  \nTotal points: 60 (full block, 293.15–308.15 K) | 15 points at 298.15 K | Pressure: 101.0 kPa  \nComposition variable: mole fraction of water\n\n| x(water) | Viscosity (Pa·s) |\n|---|---|\n| 0 | 0.0008045 |\n| 0.1 | 0.0009018 |\n| 0.2 | 0.0010386 |\n| 0.3 | 0.0012331 |\n| 0.4 | 0.0015078 |\n| 0.5 | 0.0018528 |\n| 0.6 | 0.0022264 |\n| 0.7 | 0.0024775 |\n| 0.8 | 0.0023495 |\n| 0.9 | 0.0017464 |\n| 0.94 | 0.0014116 |\n| 1 | 0.0008903 |\n\nViscosity range at 298.15 K: 0.0008045–0.0024775 Pa·s across x(water) = 0–1.\n\n---\n\nTwo additional blocks were also returned in the search (4 total), including one from GLOBlit_11030 (temperature range not inspected in this run).\n\n**Chemistry insight:** Both datasets show a pronounced viscosity maximum at intermediate compositions — near x(DMF) ≈ 0.3 in Block 1 (GLOBlit_8676::PROPblock_9, 0.002491 Pa·s) and near x(water) ≈ 0.7 in Block 2 (GLOBlit_9900::PROPblock_3, 0.0024775 Pa·s). These correspond to the same composition region (~30 mol% DMF / 70 mol% water), consistent with strong DMF–water hydrogen-bonding interactions that create structured molecular associations and enhance viscous resistance to flow at these intermediate compositions.", "core_claims": ["Four blocks of dynamic viscosity data for binary DMF + water mixtures were identified, with two key blocks providing detailed measurements at 298.15 K and near-ambient pressure.", "Block 1 (DOI: 10.1021/je050209y) reports 11 viscosity values at 298.15 K and 101.325 kPa spanning x(DMF) = 0.05–0.9488, with viscosity ranging from 0.000843 to 0.002491 Pa·s.", "Block 2 (DOI: 10.1021/je300608v) reports 12 viscosity values at 298.15 K and 101.0 kPa spanning x(water) = 0–1, with viscosity ranging from 0.0008045 to 0.0024775 Pa·s.", "Both datasets show a pronounced viscosity maximum at intermediate compositions near ~30 mol% DMF / 70 mol% water (0.002491 Pa·s in Block 1 at x(DMF) ≈ 0.3; 0.0024775 Pa·s in Block 2 at x(water) ≈ 0.7), consistent with strong DMF–water hydrogen-bonding interactions that create structured molecular associations and enhance viscous resistance to flow."], "status": "success", "summary": "Dynamic viscosity (Pa·s) data for the binary system N,N-dimethylformamide (DMF) + water at 298.15 K were found in four data blocks. Two key blocks were inspected in detail. Block 1 (DOI 10.1021/je050209y, GLOBlit_8676::PROPblock_9) reports 11 points at 298.15 K and 101.325 kPa as a function of DMF mole fraction, with viscosities ranging from 0.000843 to 0.002491 Pa·s across x(DMF) = 0.05–0.9488. Block 2 (DOI 10.1021/je300608v, GLOBlit_9900::PROPblock_3) reports 15 points at 298.15 K and 101.0 kPa as a function of water mole fraction, with viscosities ranging from 0.0008045 to 0.0024775 Pa·s across x(water) = 0–1. Both datasets exhibit a pronounced viscosity maximum near ~30 mol% DMF / ~70 mol% water (0.002491 Pa·s in Block 1 at x(DMF) ≈ 0.3; 0.0024775 Pa·s in Block 2 at x(water) ≈ 0.7), attributed to strong DMF–water hydrogen-bonding interactions forming structured molecular associations. Two additional blocks were also returned but not inspected in detail.", "core_id_updates": [{"action": "add", "core_GLOB_id": "GLOBcomp_18", "registry_id": "dimethylformamide", "name": "dimethylformamide"}, {"action": "add", "core_GLOB_id": "GLOBcomp_1", "registry_id": "water", "name": "water"}, {"action": "add", "core_GLOB_id": "GLOBprop_4", "registry_id": "viscosity_pa_s", "name": "Viscosity, Pa*s"}], "core_blocks_found": [{"lit_num_id": "GLOBlit_8676", "block_number": "PROPblock_9", "BLKsubsys_id": null, "system_type": "binary", "comp_num_ids": ["GLOBcomp_18", "GLOBcomp_1"], "prop_num_ids": ["GLOBprop_4"], "description": "Dynamic viscosity of binary DMF + water at 298.15 K and 101.325 kPa as a function of DMF mole fraction (11 points, viscosity range 0.000843–0.002491 Pa·s).", "doi": "10.1021/je050209y", "lit_id": "2005-han-oh-0", "block_type": "PureOrMixtureData", "blocktype_num_id": "GLOBblocktype_1", "n_datapoints": 11, "n_components": 2, "compounds": [{"org_num": "DOIcomp_1", "comp_num_id": "GLOBcomp_18", "name": "dimethylformamide", "formula": "C3H7NO", "inchi_key": "ZMXDDKWLCZADIW-UHFFFAOYSA-N", "SMILES": "CN(C)C=O", "sample_num": "DOIcompSample_1_1"}, {"org_num": "DOIcomp_3", "comp_num_id": "GLOBcomp_1", "name": "water", "formula": "H2O", "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N", "SMILES": "O", "sample_num": "DOIcompSample_3_1"}], "solvents": [], "constraints": [{"BLKconstr_id": "BLKconstr_1", "constr_num_id": "GLOBconstr_2", "constr_id": "temperature_k", "name": "Temperature, K", "type": "eTemperature", "value": 298.15, "digits": 5, "component_org_num": null, "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}}, {"BLKconstr_id": "BLKconstr_2", "constr_num_id": "GLOBconstr_1", "constr_id": "pressure_kpa", "name": "Pressure, kPa", "type": "ePressure", "value": 101.325, "digits": 6, "component_org_num": null, "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}}], "variables": [{"BLKvar_id": "BLKvar_1", "var_num_id": "GLOBvar_2", "var_id": "mole_fraction_DOIcomp_1", "name": "Mole fraction", "type": "eComponentComposition", "component_org_num": "DOIcomp_1", "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, "range": {"BLKvar_id": "BLKvar_1", "name": "Mole fraction", "min": 0.05, "max": 0.9488, "n_unique": 11}, "range_min": 0.05, "range_max": 0.9488}], "properties": [{"BLKprop_id": "BLKprop_1", "prop_num_id": "GLOBprop_4", "prop_ID": "viscosity_pa_s", "name": "Viscosity, Pa*s", "group": "TransportProp", "component_org_num": null, "meas_num_id": "GLOBmeas_140", "meas_ID": "captub_ufactor_2", "method_standard": null, "method_custom": "CAPTUB:UFactor:2", "range": {"BLKprop_id": "BLKprop_1", "name": "Viscosity, Pa*s", "min": 0.000843, "max": 0.002491, "mean": 0.001599, "std": 0.00059, "n": 11}, "uncertainty": {"evaluation_method": "Propagation of evaluated standard uncertainties", "confidence_level": 95, "evaluator": "Data file compiler", "assessment_num": "BLKpropAssessment_1_1"}, "range_min": 0.000843, "range_max": 0.002491}], "phases": [{"owner_id": "BLKprop_1", "role": "property_phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKvar_1", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKconstr_1", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKconstr_2", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}], "reaction_type": null, "participants": [], "notes": null, "declared_system_type": "binary", "declared_n_components": 2, "declared_compounds": [{"org_num": "DOIcomp_1", "comp_num_id": "GLOBcomp_18", "name": "dimethylformamide", "formula": "C3H7NO", "inchi_key": "ZMXDDKWLCZADIW-UHFFFAOYSA-N", "SMILES": "CN(C)C=O", "sample_num": "DOIcompSample_1_1"}, {"org_num": "DOIcomp_3", "comp_num_id": "GLOBcomp_1", "name": "water", "formula": "H2O", "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N", "SMILES": "O", "sample_num": "DOIcompSample_3_1"}], "parent_n_datapoints": 11, "subsystem_scope": null, "subsystem_point_runs": [], "subsystem_path_class": null, "subsystem_evidence_quality": null, "subsystem_condition_ranges": []}, {"lit_num_id": "GLOBlit_9900", "block_number": "PROPblock_3", "BLKsubsys_id": null, "system_type": "binary", "comp_num_ids": ["GLOBcomp_18", "GLOBcomp_1"], "prop_num_ids": ["GLOBprop_4"], "description": "Dynamic viscosity of binary DMF + water at 293.15–308.15 K and 101.0 kPa as a function of water mole fraction (60 total points, 15 at 298.15 K, viscosity range at 298.15 K: 0.0008045–0.0024775 Pa·s).", "doi": "10.1021/je300608v", "lit_id": "2013-joz-tyc-1", "block_type": "PureOrMixtureData", "blocktype_num_id": "GLOBblocktype_1", "n_datapoints": 60, "n_components": 2, "compounds": [{"org_num": "DOIcomp_2", "comp_num_id": "GLOBcomp_18", "name": "dimethylformamide", "formula": "C3H7NO", "inchi_key": "ZMXDDKWLCZADIW-UHFFFAOYSA-N", "SMILES": "CN(C)C=O", "sample_num": "DOIcompSample_2_1"}, {"org_num": "DOIcomp_3", "comp_num_id": "GLOBcomp_1", "name": "water", "formula": "H2O", "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N", "SMILES": "O", "sample_num": "DOIcompSample_3_1"}], "solvents": [], "constraints": [{"BLKconstr_id": "BLKconstr_1", "constr_num_id": "GLOBconstr_1", "constr_id": "pressure_kpa", "name": "Pressure, kPa", "type": "ePressure", "value": 101.0, "digits": 3, "component_org_num": null, "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}}], "variables": [{"BLKvar_id": "BLKvar_1", "var_num_id": "GLOBvar_1", "var_id": "temperature_k", "name": "Temperature, K", "type": "eTemperature", "component_org_num": null, "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, "range": {"BLKvar_id": "BLKvar_1", "name": "Temperature, K", "min": 293.15, "max": 308.15, "n_unique": 4}, "range_min": 293.15, "range_max": 308.15}, {"BLKvar_id": "BLKvar_2", "var_num_id": "GLOBvar_2", "var_id": "mole_fraction_DOIcomp_3", "name": "Mole fraction", "type": "eComponentComposition", "component_org_num": "DOIcomp_3", "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, "range": {"BLKvar_id": "BLKvar_2", "name": "Mole fraction", "min": 0.0, "max": 1.0, "n_unique": 15}, "range_min": 0.0, "range_max": 1.0}], "properties": [{"BLKprop_id": "BLKprop_1", "prop_num_id": "GLOBprop_4", "prop_ID": "viscosity_pa_s", "name": "Viscosity, Pa*s", "group": "TransportProp", "component_org_num": null, "meas_num_id": "GLOBmeas_4", "meas_ID": "capillary_tube_ostwald_ubbelohde_method", "method_standard": "Capillary tube (Ostwald; Ubbelohde) method", "method_custom": null, "range": {"BLKprop_id": "BLKprop_1", "name": "Viscosity, Pa*s", "min": 0.000712, "max": 0.002885, "mean": 0.00142, "std": 0.000544, "n": 60}, "uncertainty": {"evaluation_method": "Propagation of evaluated standard uncertainties", "confidence_level": 95, "evaluator": "Data file compiler", "assessment_num": "BLKpropAssessment_1_1"}, "range_min": 0.000712, "range_max": 0.002885}], "phases": [{"owner_id": "BLKprop_1", "role": "property_phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKvar_1", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKvar_2", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKconstr_1", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}], "reaction_type": null, "participants": [], "notes": null, "declared_system_type": "binary", "declared_n_components": 2, "declared_compounds": [{"org_num": "DOIcomp_2", "comp_num_id": "GLOBcomp_18", "name": "dimethylformamide", "formula": "C3H7NO", "inchi_key": "ZMXDDKWLCZADIW-UHFFFAOYSA-N", "SMILES": "CN(C)C=O", "sample_num": "DOIcompSample_2_1"}, {"org_num": "DOIcomp_3", "comp_num_id": "GLOBcomp_1", "name": "water", "formula": "H2O", "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N", "SMILES": "O", "sample_num": "DOIcompSample_3_1"}], "parent_n_datapoints": 60, "subsystem_scope": null, "subsystem_point_runs": [], "subsystem_path_class": null, "subsystem_evidence_quality": null, "subsystem_condition_ranges": []}], "data_inspections": [{"doi": "10.1021/je050209y", "block_number": "PROPblock_9", "table_mode": "complete", "columns": ["BLKpoint_id", "mole_fraction_<dimethylformamide>", "temperature_k", "pressure_kpa", "viscosity_pa_s"], "rows_shown": [{"BLKpoint_id": "BLKpoint_1", "mole_fraction_<dimethylformamide>": "0.05", "temperature_k": "298.15", "pressure_kpa": "101.325", "viscosity_pa_s": "0.00131"}, {"BLKpoint_id": "BLKpoint_2", "mole_fraction_<dimethylformamide>": "0.1001", "temperature_k": "298.15", "pressure_kpa": "101.325", "viscosity_pa_s": "0.001728"}, {"BLKpoint_id": "BLKpoint_3", "mole_fraction_<dimethylformamide>": "0.2", "temperature_k": "298.15", "pressure_kpa": "101.325", "viscosity_pa_s": "0.002346"}, {"BLKpoint_id": "BLKpoint_4", "mole_fraction_<dimethylformamide>": "0.299", "temperature_k": "298.15", "pressure_kpa": "101.325", "viscosity_pa_s": "0.002491"}, {"BLKpoint_id": "BLKpoint_5", "mole_fraction_<dimethylformamide>": "0.3998", "temperature_k": "298.15", "pressure_kpa": "101.325", "viscosity_pa_s": "0.002273"}, {"BLKpoint_id": "BLKpoint_6", "mole_fraction_<dimethylformamide>": "0.4997", "temperature_k": "298.15", "pressure_kpa": "101.325", "viscosity_pa_s": "0.001878"}, {"BLKpoint_id": "BLKpoint_7", "mole_fraction_<dimethylformamide>": "0.5993", "temperature_k": "298.15", "pressure_kpa": "101.325", "viscosity_pa_s": "0.001532"}, {"BLKpoint_id": "BLKpoint_8", "mole_fraction_<dimethylformamide>": "0.6995", "temperature_k": "298.15", "pressure_kpa": "101.325", "viscosity_pa_s": "0.001243"}, {"BLKpoint_id": "BLKpoint_9", "mole_fraction_<dimethylformamide>": "0.8", "temperature_k": "298.15", "pressure_kpa": "101.325", "viscosity_pa_s": "0.001045"}, {"BLKpoint_id": "BLKpoint_10", "mole_fraction_<dimethylformamide>": "0.8991", "temperature_k": "298.15", "pressure_kpa": "101.325", "viscosity_pa_s": "0.000901"}, {"BLKpoint_id": "BLKpoint_11", "mole_fraction_<dimethylformamide>": "0.9488", "temperature_k": "298.15", "pressure_kpa": "101.325", "viscosity_pa_s": "0.000843"}], "inspection_id": "INSP_469970d3baa4", "lit_num_id": "GLOBlit_8676"}, {"doi": "10.1021/je300608v", "block_number": "PROPblock_3", "table_mode": "rdp", "columns": ["BLKpoint_id", "temperature_k", "mole_fraction_<water>", "pressure_kpa", "viscosity_pa_s"], "rows_shown": [{"BLKpoint_id": "BLKpoint_16", "temperature_k": "298.15", "mole_fraction_<water>": "0", "pressure_kpa": "101.0", "viscosity_pa_s": "0.0008045"}, {"BLKpoint_id": "BLKpoint_17", "temperature_k": "298.15", "mole_fraction_<water>": "0.1", "pressure_kpa": "101.0", "viscosity_pa_s": "0.0009018"}, {"BLKpoint_id": "BLKpoint_18", "temperature_k": "298.15", "mole_fraction_<water>": "0.2", "pressure_kpa": "101.0", "viscosity_pa_s": "0.0010386"}, {"BLKpoint_id": "BLKpoint_19", "temperature_k": "298.15", "mole_fraction_<water>": "0.3", "pressure_kpa": "101.0", "viscosity_pa_s": "0.0012331"}, {"BLKpoint_id": "BLKpoint_20", "temperature_k": "298.15", "mole_fraction_<water>": "0.4", "pressure_kpa": "101.0", "viscosity_pa_s": "0.0015078"}, {"BLKpoint_id": "BLKpoint_21", "temperature_k": "298.15", "mole_fraction_<water>": "0.5", "pressure_kpa": "101.0", "viscosity_pa_s": "0.0018528"}, {"BLKpoint_id": "BLKpoint_22", "temperature_k": "298.15", "mole_fraction_<water>": "0.6", "pressure_kpa": "101.0", "viscosity_pa_s": "0.0022264"}, {"BLKpoint_id": "BLKpoint_23", "temperature_k": "298.15", "mole_fraction_<water>": "0.7", "pressure_kpa": "101.0", "viscosity_pa_s": "0.0024775"}, {"BLKpoint_id": "BLKpoint_24", "temperature_k": "298.15", "mole_fraction_<water>": "0.8", "pressure_kpa": "101.0", "viscosity_pa_s": "0.0023495"}, {"BLKpoint_id": "BLKpoint_25", "temperature_k": "298.15", "mole_fraction_<water>": "0.9", "pressure_kpa": "101.0", "viscosity_pa_s": "0.0017464"}, {"BLKpoint_id": "BLKpoint_27", "temperature_k": "298.15", "mole_fraction_<water>": "0.94", "pressure_kpa": "101.0", "viscosity_pa_s": "0.0014116"}, {"BLKpoint_id": "BLKpoint_30", "temperature_k": "298.15", "mole_fraction_<water>": "1", "pressure_kpa": "101.0", "viscosity_pa_s": "0.0008903"}], "inspection_id": "INSP_223a0880d59c", "lit_num_id": "GLOBlit_9900"}]}}, {"label": "binary_DMF_EG", "result": {"answer": "**Viscosity data for binary DMF + ethylene glycol mixtures near 298.15 K**\n\nOne data block was found in the ThermoML database for the dynamic viscosity of the binary system N,N-dimethylformamide (DMF) + 1,2-ethanediol (ethylene glycol):\n\n- **DOI:** 10.1021/je060113j (GLOBlit_8892)\n- **Block:** PROPblock_25\n- **Compounds:** GLOBcomp_18 (dimethylformamide), GLOBcomp_24 (1,2-ethanediol)\n- **Property:** Dynamic viscosity (GLOBprop_4), measured by capillary tube method (GLOBmeas_4), liquid phase\n- **Composition:** Fixed mole fraction of 1,2-ethanediol = 0.5408\n- **Pressure:** 101.0 kPa\n\nThe block contains 3 data points at three temperatures:\n\n| BLKpoint_id | Temperature (K) | x(1,2-ethanediol) | Pressure (kPa) | Viscosity (Pa·s) |\n|---|---|---|---|---|\n| BLKpoint_1 | 298.15 | 0.5408 | 101.0 | 0.0030647 |\n| BLKpoint_2 | 308.15 | 0.5408 | 101.0 | 0.0024529 |\n| BLKpoint_3 | 318.15 | 0.5408 | 101.0 | 0.0019599 |\n\nAt exactly 298.15 K, the viscosity is **0.0030647 Pa·s** (≈ 3.06 mPa·s).\n\n**Chemistry note:** The viscosity decreases monotonically with increasing temperature (near-linear, R² = 0.9962), as expected for liquid mixtures. This block provides data at only one composition (x_EG = 0.5408); no additional composition-sweep blocks were found for this binary system in the database.", "core_claims": ["In the ThermoML database (DOI 10.1021/je060113j), the dynamic viscosity of the binary DMF + ethylene glycol mixture at a fixed 1,2-ethanediol mole fraction of 0.5408 and 101.0 kPa is reported as 0.0030647 Pa·s at 298.15 K, 0.0024529 Pa·s at 308.15 K, and 0.0019599 Pa·s at 318.15 K, decreasing monotonically with increasing temperature consistent with expected liquid-mixture behavior, with only one composition (x_EG = 0.5408) available for this binary system in the database."], "status": "success", "summary": "A single data block from DOI 10.1021/je060113j (GLOBlit_8892, PROPblock_25) reports the dynamic viscosity of the binary system N,N-dimethylformamide (DMF) + 1,2-ethanediol (ethylene glycol) at a fixed mole fraction of 1,2-ethanediol = 0.5408 and 101.0 kPa, measured by capillary tube method in the liquid phase. Three data points are provided: at 298.15 K the viscosity is 0.0030647 Pa·s, at 308.15 K it is 0.0024529 Pa·s, and at 318.15 K it is 0.0019599 Pa·s. Viscosity decreases monotonically with increasing temperature. No additional composition-sweep blocks were found for this binary system in the database.", "core_id_updates": [{"action": "add", "core_GLOB_id": "GLOBcomp_18", "registry_id": "dimethylformamide", "name": "dimethylformamide"}, {"action": "add", "core_GLOB_id": "GLOBcomp_24", "registry_id": "1,2-ethanediol", "name": "1,2-ethanediol"}, {"action": "add", "core_GLOB_id": "GLOBlit_8892", "registry_id": "2006-sin-roy-0", "name": "10.1021/je060113j"}, {"action": "add", "core_GLOB_id": "GLOBprop_4", "registry_id": "viscosity_pa_s", "name": "Viscosity, Pa*s"}, {"action": "add", "core_GLOB_id": "GLOBmeas_4", "registry_id": "capillary_tube_ostwald_ubbelohde_method", "name": "Capillary tube (Ostwald; Ubbelohde) method"}], "core_blocks_found": [{"lit_num_id": "GLOBlit_8892", "block_number": "PROPblock_25", "BLKsubsys_id": null, "system_type": "binary", "comp_num_ids": ["GLOBcomp_18", "GLOBcomp_24"], "prop_num_ids": ["GLOBprop_4"], "description": "Dynamic viscosity of binary dimethylformamide + 1,2-ethanediol at 298.15–318.15 K, fixed x(1,2-ethanediol) = 0.5408, 101.0 kPa, capillary tube method.", "doi": "10.1021/je060113j", "lit_id": "2006-sin-roy-0", "block_type": "PureOrMixtureData", "blocktype_num_id": "GLOBblocktype_1", "n_datapoints": 3, "n_components": 2, "compounds": [{"org_num": "DOIcomp_4", "comp_num_id": "GLOBcomp_18", "name": "dimethylformamide", "formula": "C3H7NO", "inchi_key": "ZMXDDKWLCZADIW-UHFFFAOYSA-N", "SMILES": "CN(C)C=O", "sample_num": "DOIcompSample_4_1"}, {"org_num": "DOIcomp_1", "comp_num_id": "GLOBcomp_24", "name": "1,2-ethanediol", "formula": "C2H6O2", "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N", "SMILES": "OCCO", "sample_num": "DOIcompSample_1_1"}], "solvents": [], "constraints": [{"BLKconstr_id": "BLKconstr_1", "constr_num_id": "GLOBconstr_3", "constr_id": "mole_fraction_DOIcomp_1", "name": "Mole fraction", "type": "eComponentComposition", "value": 0.5408, "digits": 4, "component_org_num": "DOIcomp_1", "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}}, {"BLKconstr_id": "BLKconstr_2", "constr_num_id": "GLOBconstr_1", "constr_id": "pressure_kpa", "name": "Pressure, kPa", "type": "ePressure", "value": 101.0, "digits": 3, "component_org_num": null, "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}}], "variables": [{"BLKvar_id": "BLKvar_1", "var_num_id": "GLOBvar_1", "var_id": "temperature_k", "name": "Temperature, K", "type": "eTemperature", "component_org_num": null, "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, "range": {"BLKvar_id": "BLKvar_1", "name": "Temperature, K", "min": 298.15, "max": 318.15, "n_unique": 3}, "range_min": 298.15, "range_max": 318.15}], "properties": [{"BLKprop_id": "BLKprop_1", "prop_num_id": "GLOBprop_4", "prop_ID": "viscosity_pa_s", "name": "Viscosity, Pa*s", "group": "TransportProp", "component_org_num": null, "meas_num_id": "GLOBmeas_4", "meas_ID": "capillary_tube_ostwald_ubbelohde_method", "method_standard": "Capillary tube (Ostwald; Ubbelohde) method", "method_custom": null, "range": {"BLKprop_id": "BLKprop_1", "name": "Viscosity, Pa*s", "min": 0.00196, "max": 0.003065, "mean": 0.002492, "std": 0.000553, "n": 3}, "uncertainty": {"evaluation_method": "Propagation of evaluated standard uncertainties", "confidence_level": 95, "evaluator": "Data file compiler", "assessment_num": "BLKpropAssessment_1_1"}, "range_min": 0.00196, "range_max": 0.003065}], "phases": [{"owner_id": "BLKprop_1", "role": "property_phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKvar_1", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKconstr_1", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKconstr_2", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}], "reaction_type": null, "participants": [], "notes": null, "declared_system_type": "binary", "declared_n_components": 2, "declared_compounds": [{"org_num": "DOIcomp_4", "comp_num_id": "GLOBcomp_18", "name": "dimethylformamide", "formula": "C3H7NO", "inchi_key": "ZMXDDKWLCZADIW-UHFFFAOYSA-N", "SMILES": "CN(C)C=O", "sample_num": "DOIcompSample_4_1"}, {"org_num": "DOIcomp_1", "comp_num_id": "GLOBcomp_24", "name": "1,2-ethanediol", "formula": "C2H6O2", "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N", "SMILES": "OCCO", "sample_num": "DOIcompSample_1_1"}], "parent_n_datapoints": 3, "subsystem_scope": null, "subsystem_point_runs": [], "subsystem_path_class": null, "subsystem_evidence_quality": null, "subsystem_condition_ranges": []}], "data_inspections": [{"doi": "10.1021/je060113j", "block_number": "PROPblock_25", "table_mode": "nearest", "columns": ["BLKpoint_id", "temperature_k", "mole_fraction_<1,2-ethanediol>", "pressure_kpa", "viscosity_pa_s"], "rows_shown": [{"BLKpoint_id": "BLKpoint_1", "temperature_k": "298.15", "mole_fraction_<1,2-ethanediol>": "0.5408", "pressure_kpa": "101.0", "viscosity_pa_s": "0.0030647"}, {"BLKpoint_id": "BLKpoint_2", "temperature_k": "308.15", "mole_fraction_<1,2-ethanediol>": "0.5408", "pressure_kpa": "101.0", "viscosity_pa_s": "0.0024529"}, {"BLKpoint_id": "BLKpoint_3", "temperature_k": "318.15", "mole_fraction_<1,2-ethanediol>": "0.5408", "pressure_kpa": "101.0", "viscosity_pa_s": "0.0019599"}], "inspection_id": "INSP_d1035750f998", "lit_num_id": "GLOBlit_8892"}]}}, {"label": "binary_EG_water", "result": {"answer": "**Viscosity data for binary ethylene glycol (1,2-ethanediol) + water mixtures near 298.15 K**\n\n**Compounds resolved:**\n- Ethylene glycol (1,2-ethanediol): **GLOBcomp_24** (C₂H₆O₂, SMILES: OCCO)\n- Water: **GLOBcomp_1** (H₂O)\n\n**Property:** Dynamic viscosity (GLOBprop_4), units: Pa·s\n\nFive inspected data blocks were found for binary liquid-phase mixtures covering temperatures near 298.15 K:\n\n| # | DOI | Block | Literature ID | Data Points | T range (K) | Composition Variable | P (kPa) |\n|---|-----|-------|---------------|-------------|-------------|----------------------|---------|\n| 1 | 10.1016/j.jct.2006.01.011 | PROPblock_13 | GLOBlit_2656 | 10 | 293.15–293.15 | mass fraction EG (GLOBcomp_24) | 101.325 |\n| 2 | 10.1016/j.jct.2018.02.022 | PROPblock_24 | GLOBlit_5201 | 84 | 293.15–308.15 | mole fraction EG (GLOBcomp_24) | 92.3 |\n| 3 | 10.1021/acs.jced.6b00526 | PROPblock_18 | GLOBlit_6951 | 33 | 293.15–303.15 | mole fraction water (GLOBcomp_1) | 100.0 |\n| 4 | 10.1021/je020140j | PROPblock_5 | GLOBlit_8038 | 77 | 293.15–353.15 | mole fraction EG (GLOBcomp_24) | 101.0 |\n| 5 | 10.1021/je025610o | PROPblock_5 | GLOBlit_8106 | 30 | 296.45–449.85 | mole fraction EG (GLOBcomp_24) | 100.0 |\n\nA sixth block was also matched in the initial search but its details were truncated; the five blocks above were fully inspected.\n\n**Representative data near 298.15 K:**\n\nFrom GLOBlit_5201::PROPblock_24 (at 298.15 K, 92.3 kPa):\n\n| Mole fraction EG | Viscosity (Pa·s) |\n|---|---|\n| 0 | 0.00089689 |\n| 0.2072 | 0.0028109 |\n| 0.4446 | 0.0060624 |\n| 1 | 0.016223 |\n\nFrom GLOBlit_6951::PROPblock_18 (at 298.15 K, 100.0 kPa):\n\n| Mole fraction water | Viscosity (Pa·s) |\n|---|---|\n| 0 | 0.01724 |\n| 0.2014 | 0.01219 |\n| 0.4011 | 0.00831 |\n| 0.6995 | 0.003884 |\n| 1 | 0.000843 |\n\n**Chemistry insight:** The viscosity of ethylene glycol–water mixtures increases strongly and nonlinearly with ethylene glycol content. In GLOBlit_5201::PROPblock_24 at 298.15 K, pure EG viscosity is 0.016223 Pa·s versus 0.00089689 Pa·s for pure water (a ratio of approximately 18×, derived by division). In GLOBlit_6951::PROPblock_18 at 298.15 K, pure EG viscosity is 0.01724 Pa·s versus 0.000843 Pa·s for pure water (a ratio of approximately 20×, derived by division). This reflects the extensive hydrogen-bonding network formed by the two hydroxyl groups of ethylene glycol. The most data-rich blocks near 298.15 K are GLOBlit_5201::PROPblock_24 (84 points, 293.15–308.15 K) and GLOBlit_8038::PROPblock_5 (77 points, 293.15–353.15 K), both using mole fraction of ethylene glycol as the composition variable.\n\n---\n[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:\n- **AMBIGUOUS_VALUE** PROPblock_5: 298.15 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"PROPblock_5\", literature=\"<GLOBlit_N or DOI>\", nearest={\"column\": \"mole_fraction_<1,2-ethanediol>\", \"value\": 298.15})` — if it is a value you computed or an external reference, keep it and label its provenance instead\n- **UNINSPECTED_VALUE** GLOBlit_5201::PROPblock_24: 18 exists in PROPblock_24's database table but was never shown in an inspection of this run\n  fix (required — this value IS in the cited block's database table): `inspect_block_table(block_number=\"GLOBlit_5201::PROPblock_24\", nearest={\"column\": \"temperature_k\", \"value\": 18.0})`\nInspected so far: PROPblock_13, PROPblock_18, PROPblock_24, PROPblock_5", "core_claims": ["Five ThermoML data blocks were identified containing dynamic viscosity data for binary ethylene glycol (1,2-ethanediol) + water liquid mixtures near 298.15 K, with the most data-rich blocks being GLOBlit_5201::PROPblock_24 (84 points, 293.15–308.15 K) and GLOBlit_8038::PROPblock_5 (77 points, 293.15–353.15 K).", "At 298.15 K, the viscosity of ethylene glycol–water mixtures increases strongly and nonlinearly with ethylene glycol content; in GLOBlit_5201::PROPblock_24 pure EG viscosity is 0.016223 Pa·s versus 0.00089689 Pa·s for pure water, and in GLOBlit_6951::PROPblock_18 pure EG viscosity is 0.01724 Pa·s versus 0.000843 Pa·s for pure water.", "The strong increase in viscosity with ethylene glycol content is attributed to the extensive hydrogen-bonding network formed by the two hydroxyl groups of ethylene glycol."], "status": "success", "summary": "Dynamic viscosity (GLOBprop_4, Pa·s) data for binary mixtures of ethylene glycol (GLOBcomp_24, OCCO) and water (GLOBcomp_1) near 298.15 K were identified across five data blocks. The most data-rich blocks are GLOBlit_5201::PROPblock_24 (84 points, 293.15–308.15 K, mole fraction EG, 92.3 kPa) and GLOBlit_8038::PROPblock_5 (77 points, 293.15–353.15 K, mole fraction EG, 101.0 kPa). Additional blocks include GLOBlit_2656::PROPblock_13 (10 points at 293.15 K, mass fraction EG, 101.325 kPa), GLOBlit_6951::PROPblock_18 (33 points, 293.15–303.15 K, mole fraction water, 100.0 kPa), and GLOBlit_8106::PROPblock_5 (30 points, 296.45–449.85 K, mole fraction EG, 100.0 kPa). Representative values at 298.15 K from GLOBlit_5201::PROPblock_24: pure water viscosity 0.00089689 Pa·s, mole fraction EG 0.2072 gives 0.0028109 Pa·s, mole fraction EG 0.4446 gives 0.0060624 Pa·s, pure EG gives 0.016223 Pa·s. From GLOBlit_6951::PROPblock_18 at 298.15 K: pure EG (mole fraction water 0) gives 0.01724 Pa·s, mole fraction water 0.2014 gives 0.01219 Pa·s, mole fraction water 0.4011 gives 0.00831 Pa·s, mole fraction water 0.6995 gives 0.003884 Pa·s, pure water gives 0.000843 Pa·s. Viscosity increases strongly and nonlinearly with ethylene glycol content, reflecting the extensive hydrogen-bonding network of its two hydroxyl groups.", "core_id_updates": [{"action": "add", "core_GLOB_id": "GLOBcomp_24", "registry_id": "1,2-ethanediol", "name": "1,2-ethanediol"}, {"action": "add", "core_GLOB_id": "GLOBcomp_1", "registry_id": "water", "name": "water"}], "core_blocks_found": [{"lit_num_id": "GLOBlit_2656", "block_number": "PROPblock_13", "BLKsubsys_id": null, "system_type": "binary", "comp_num_ids": ["GLOBcomp_24", "GLOBcomp_1"], "prop_num_ids": ["GLOBprop_4"], "description": "Dynamic viscosity of binary ethylene glycol + water at 293.15 K, mass fraction composition, 101.325 kPa.", "doi": "10.1016/j.jct.2006.01.011", "lit_id": "2006-tsi-mol-1", "block_type": "PureOrMixtureData", "blocktype_num_id": "GLOBblocktype_1", "n_datapoints": 10, "n_components": 2, "compounds": [{"org_num": "DOIcomp_1", "comp_num_id": "GLOBcomp_24", "name": "1,2-ethanediol", "formula": "C2H6O2", "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N", "SMILES": "OCCO", "sample_num": "DOIcompSample_1_1"}, {"org_num": "DOIcomp_3", "comp_num_id": "GLOBcomp_1", "name": "water", "formula": "H2O", "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N", "SMILES": "O", "sample_num": "DOIcompSample_3_1"}], "solvents": [], "constraints": [{"BLKconstr_id": "BLKconstr_1", "constr_num_id": "GLOBconstr_2", "constr_id": "temperature_k", "name": "Temperature, K", "type": "eTemperature", "value": 293.15, "digits": 5, "component_org_num": null, "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}}, {"BLKconstr_id": "BLKconstr_2", "constr_num_id": "GLOBconstr_1", "constr_id": "pressure_kpa", "name": "Pressure, kPa", "type": "ePressure", "value": 101.325, "digits": 6, "component_org_num": null, "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}}], "variables": [{"BLKvar_id": "BLKvar_1", "var_num_id": "GLOBvar_5", "var_id": "mass_fraction_DOIcomp_1", "name": "Mass fraction", "type": "eComponentComposition", "component_org_num": "DOIcomp_1", "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, "range": {"BLKvar_id": "BLKvar_1", "name": "Mass fraction", "min": 0.0, "max": 0.9, "n_unique": 10}, "range_min": 0.0, "range_max": 0.9}], "properties": [{"BLKprop_id": "BLKprop_1", "prop_num_id": "GLOBprop_4", "prop_ID": "viscosity_pa_s", "name": "Viscosity, Pa*s", "group": "TransportProp", "component_org_num": null, "meas_num_id": "GLOBmeas_4", "meas_ID": "capillary_tube_ostwald_ubbelohde_method", "method_standard": "Capillary tube (Ostwald; Ubbelohde) method", "method_custom": null, "range": {"BLKprop_id": "BLKprop_1", "name": "Viscosity, Pa*s", "min": 0.001008, "max": 0.013999, "mean": 0.004563, "std": 0.004021, "n": 10}, "uncertainty": {"evaluation_method": "Propagation of evaluated standard uncertainties", "confidence_level": 95, "evaluator": "Data file compiler", "assessment_num": "BLKpropAssessment_1_1"}, "range_min": 0.001008, "range_max": 0.013999}], "phases": [{"owner_id": "BLKprop_1", "role": "property_phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKvar_1", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKconstr_1", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKconstr_2", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}], "reaction_type": null, "participants": [], "notes": null, "declared_system_type": "binary", "declared_n_components": 2, "declared_compounds": [{"org_num": "DOIcomp_1", "comp_num_id": "GLOBcomp_24", "name": "1,2-ethanediol", "formula": "C2H6O2", "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N", "SMILES": "OCCO", "sample_num": "DOIcompSample_1_1"}, {"org_num": "DOIcomp_3", "comp_num_id": "GLOBcomp_1", "name": "water", "formula": "H2O", "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N", "SMILES": "O", "sample_num": "DOIcompSample_3_1"}], "parent_n_datapoints": 10, "subsystem_scope": null, "subsystem_point_runs": [], "subsystem_path_class": null, "subsystem_evidence_quality": null, "subsystem_condition_ranges": []}, {"lit_num_id": "GLOBlit_5201", "block_number": "PROPblock_24", "BLKsubsys_id": null, "system_type": "binary", "comp_num_ids": ["GLOBcomp_24", "GLOBcomp_1"], "prop_num_ids": ["GLOBprop_4"], "description": "Dynamic viscosity of binary ethylene glycol + water, 293.15–308.15 K, mole fraction composition, 92.3 kPa. 84 data points.", "doi": "10.1016/j.jct.2018.02.022", "lit_id": "2018-hog-tor-0", "block_type": "PureOrMixtureData", "blocktype_num_id": "GLOBblocktype_1", "n_datapoints": 84, "n_components": 2, "compounds": [{"org_num": "DOIcomp_2", "comp_num_id": "GLOBcomp_24", "name": "1,2-ethanediol", "formula": "C2H6O2", "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N", "SMILES": "OCCO", "sample_num": "DOIcompSample_2_1"}, {"org_num": "DOIcomp_6", "comp_num_id": "GLOBcomp_1", "name": "water", "formula": "H2O", "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N", "SMILES": "O", "sample_num": "DOIcompSample_6_1"}], "solvents": [], "constraints": [{"BLKconstr_id": "BLKconstr_1", "constr_num_id": "GLOBconstr_1", "constr_id": "pressure_kpa", "name": "Pressure, kPa", "type": "ePressure", "value": 92.3, "digits": 3, "component_org_num": null, "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}}], "variables": [{"BLKvar_id": "BLKvar_1", "var_num_id": "GLOBvar_1", "var_id": "temperature_k", "name": "Temperature, K", "type": "eTemperature", "component_org_num": null, "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, "range": {"BLKvar_id": "BLKvar_1", "name": "Temperature, K", "min": 293.15, "max": 308.15, "n_unique": 4}, "range_min": 293.15, "range_max": 308.15}, {"BLKvar_id": "BLKvar_2", "var_num_id": "GLOBvar_2", "var_id": "mole_fraction_DOIcomp_2", "name": "Mole fraction", "type": "eComponentComposition", "component_org_num": "DOIcomp_2", "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, "range": {"BLKvar_id": "BLKvar_2", "name": "Mole fraction", "min": 0.0, "max": 1.0, "n_unique": 21}, "range_min": 0.0, "range_max": 1.0}], "properties": [{"BLKprop_id": "BLKprop_1", "prop_num_id": "GLOBprop_4", "prop_ID": "viscosity_pa_s", "name": "Viscosity, Pa*s", "group": "TransportProp", "component_org_num": null, "meas_num_id": "GLOBmeas_11", "meas_ID": "concentric_cylinders_viscometry", "method_standard": "Concentric cylinders viscometry", "method_custom": null, "range": {"BLKprop_id": "BLKprop_1", "name": "Viscosity, Pa*s", "min": 0.000759, "max": 0.020613, "mean": 0.007275, "std": 0.004937, "n": 84}, "uncertainty": {"evaluation_method": "Propagation of evaluated standard uncertainties", "confidence_level": 95, "evaluator": "Data file compiler", "assessment_num": "BLKpropAssessment_1_1"}, "range_min": 0.000759, "range_max": 0.020613}], "phases": [{"owner_id": "BLKprop_1", "role": "property_phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKvar_1", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKvar_2", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKconstr_1", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}], "reaction_type": null, "participants": [], "notes": null, "declared_system_type": "binary", "declared_n_components": 2, "declared_compounds": [{"org_num": "DOIcomp_2", "comp_num_id": "GLOBcomp_24", "name": "1,2-ethanediol", "formula": "C2H6O2", "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N", "SMILES": "OCCO", "sample_num": "DOIcompSample_2_1"}, {"org_num": "DOIcomp_6", "comp_num_id": "GLOBcomp_1", "name": "water", "formula": "H2O", "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N", "SMILES": "O", "sample_num": "DOIcompSample_6_1"}], "parent_n_datapoints": 84, "subsystem_scope": null, "subsystem_point_runs": [], "subsystem_path_class": null, "subsystem_evidence_quality": null, "subsystem_condition_ranges": []}, {"lit_num_id": "GLOBlit_6951", "block_number": "PROPblock_18", "BLKsubsys_id": null, "system_type": "binary", "comp_num_ids": ["GLOBcomp_24", "GLOBcomp_1"], "prop_num_ids": ["GLOBprop_4"], "description": "Dynamic viscosity of binary ethylene glycol + water, 293.15–303.15 K, mole fraction of water composition, 100.0 kPa. 33 data points.", "doi": "10.1021/acs.jced.6b00526", "lit_id": "2017-moo-ros-0", "block_type": "PureOrMixtureData", "blocktype_num_id": "GLOBblocktype_1", "n_datapoints": 33, "n_components": 2, "compounds": [{"org_num": "DOIcomp_1", "comp_num_id": "GLOBcomp_24", "name": "1,2-ethanediol", "formula": "C2H6O2", "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N", "SMILES": "OCCO", "sample_num": "DOIcompSample_1_1"}, {"org_num": "DOIcomp_5", "comp_num_id": "GLOBcomp_1", "name": "water", "formula": "H2O", "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N", "SMILES": "O", "sample_num": "DOIcompSample_5_1"}], "solvents": [], "constraints": [{"BLKconstr_id": "BLKconstr_1", "constr_num_id": "GLOBconstr_1", "constr_id": "pressure_kpa", "name": "Pressure, kPa", "type": "ePressure", "value": 100.0, "digits": 1, "component_org_num": null, "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}}], "variables": [{"BLKvar_id": "BLKvar_1", "var_num_id": "GLOBvar_1", "var_id": "temperature_k", "name": "Temperature, K", "type": "eTemperature", "component_org_num": null, "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, "range": {"BLKvar_id": "BLKvar_1", "name": "Temperature, K", "min": 293.15, "max": 303.15, "n_unique": 3}, "range_min": 293.15, "range_max": 303.15}, {"BLKvar_id": "BLKvar_2", "var_num_id": "GLOBvar_2", "var_id": "mole_fraction_DOIcomp_5", "name": "Mole fraction", "type": "eComponentComposition", "component_org_num": "DOIcomp_5", "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, "range": {"BLKvar_id": "BLKvar_2", "name": "Mole fraction", "min": 0.0, "max": 1.0, "n_unique": 11}, "range_min": 0.0, "range_max": 1.0}], "properties": [{"BLKprop_id": "BLKprop_1", "prop_num_id": "GLOBprop_4", "prop_ID": "viscosity_pa_s", "name": "Viscosity, Pa*s", "group": "TransportProp", "component_org_num": null, "meas_num_id": "GLOBmeas_8", "meas_ID": "falling_or_rolling_sphere_viscometry", "method_standard": "Falling or rolling sphere viscometry", "method_custom": null, "range": {"BLKprop_id": "BLKprop_1", "name": "Viscosity, Pa*s", "min": 0.000755, "max": 0.02113, "mean": 0.007699, "std": 0.005532, "n": 33}, "uncertainty": {"evaluation_method": "Propagation of evaluated standard uncertainties", "confidence_level": 95, "evaluator": "Data file compiler", "assessment_num": "BLKpropAssessment_1_1"}, "range_min": 0.000755, "range_max": 0.02113}], "phases": [{"owner_id": "BLKprop_1", "role": "property_phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKvar_1", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKvar_2", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKconstr_1", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}], "reaction_type": null, "participants": [], "notes": null, "declared_system_type": "binary", "declared_n_components": 2, "declared_compounds": [{"org_num": "DOIcomp_1", "comp_num_id": "GLOBcomp_24", "name": "1,2-ethanediol", "formula": "C2H6O2", "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N", "SMILES": "OCCO", "sample_num": "DOIcompSample_1_1"}, {"org_num": "DOIcomp_5", "comp_num_id": "GLOBcomp_1", "name": "water", "formula": "H2O", "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N", "SMILES": "O", "sample_num": "DOIcompSample_5_1"}], "parent_n_datapoints": 33, "subsystem_scope": null, "subsystem_point_runs": [], "subsystem_path_class": null, "subsystem_evidence_quality": null, "subsystem_condition_ranges": []}, {"lit_num_id": "GLOBlit_8038", "block_number": "PROPblock_5", "BLKsubsys_id": null, "system_type": "binary", "comp_num_ids": ["GLOBcomp_24", "GLOBcomp_1"], "prop_num_ids": ["GLOBprop_4"], "description": "Dynamic viscosity of binary ethylene glycol + water, 293.15–353.15 K, mole fraction composition, 101.0 kPa. 77 data points.", "doi": "10.1021/je020140j", "lit_id": "2003-yan-ma-2", "block_type": "PureOrMixtureData", "blocktype_num_id": "GLOBblocktype_1", "n_datapoints": 77, "n_components": 2, "compounds": [{"org_num": "DOIcomp_1", "comp_num_id": "GLOBcomp_24", "name": "1,2-ethanediol", "formula": "C2H6O2", "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N", "SMILES": "OCCO", "sample_num": "DOIcompSample_1_1"}, {"org_num": "DOIcomp_2", "comp_num_id": "GLOBcomp_1", "name": "water", "formula": "H2O", "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N", "SMILES": "O", "sample_num": "DOIcompSample_2_1"}], "solvents": [], "constraints": [{"BLKconstr_id": "BLKconstr_1", "constr_num_id": "GLOBconstr_1", "constr_id": "pressure_kpa", "name": "Pressure, kPa", "type": "ePressure", "value": 101.0, "digits": 3, "component_org_num": null, "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}}], "variables": [{"BLKvar_id": "BLKvar_1", "var_num_id": "GLOBvar_2", "var_id": "mole_fraction_DOIcomp_1", "name": "Mole fraction", "type": "eComponentComposition", "component_org_num": "DOIcomp_1", "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, "range": {"BLKvar_id": "BLKvar_1", "name": "Mole fraction", "min": 0.0, "max": 1.0, "n_unique": 11}, "range_min": 0.0, "range_max": 1.0}, {"BLKvar_id": "BLKvar_2", "var_num_id": "GLOBvar_1", "var_id": "temperature_k", "name": "Temperature, K", "type": "eTemperature", "component_org_num": null, "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, "range": {"BLKvar_id": "BLKvar_2", "name": "Temperature, K", "min": 293.15, "max": 353.15, "n_unique": 7}, "range_min": 293.15, "range_max": 353.15}], "properties": [{"BLKprop_id": "BLKprop_1", "prop_num_id": "GLOBprop_4", "prop_ID": "viscosity_pa_s", "name": "Viscosity, Pa*s", "group": "TransportProp", "component_org_num": null, "meas_num_id": "GLOBmeas_227", "meas_ID": "captub_ufactor_3", "method_standard": null, "method_custom": "CAPTUB:UFactor:3", "range": {"BLKprop_id": "BLKprop_1", "name": "Viscosity, Pa*s", "min": 0.000356, "max": 0.020833, "mean": 0.002967, "std": 0.003516, "n": 77}, "uncertainty": {"evaluation_method": "Propagation of evaluated standard uncertainties", "confidence_level": 95, "evaluator": "Data file compiler", "assessment_num": "BLKpropAssessment_1_1"}, "range_min": 0.000356, "range_max": 0.020833}], "phases": [{"owner_id": "BLKprop_1", "role": "property_phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKvar_1", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKvar_2", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKconstr_1", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}], "reaction_type": null, "participants": [], "notes": null, "declared_system_type": "binary", "declared_n_components": 2, "declared_compounds": [{"org_num": "DOIcomp_1", "comp_num_id": "GLOBcomp_24", "name": "1,2-ethanediol", "formula": "C2H6O2", "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N", "SMILES": "OCCO", "sample_num": "DOIcompSample_1_1"}, {"org_num": "DOIcomp_2", "comp_num_id": "GLOBcomp_1", "name": "water", "formula": "H2O", "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N", "SMILES": "O", "sample_num": "DOIcompSample_2_1"}], "parent_n_datapoints": 77, "subsystem_scope": null, "subsystem_point_runs": [], "subsystem_path_class": null, "subsystem_evidence_quality": null, "subsystem_condition_ranges": []}, {"lit_num_id": "GLOBlit_8106", "block_number": "PROPblock_5", "BLKsubsys_id": null, "system_type": "binary", "comp_num_ids": ["GLOBcomp_24", "GLOBcomp_1"], "prop_num_ids": ["GLOBprop_4"], "description": "Dynamic viscosity of binary ethylene glycol + water, 296.45–449.85 K, mole fraction composition, 100.0 kPa. 30 data points.", "doi": "10.1021/je025610o", "lit_id": "2003-sun-tej-0", "block_type": "PureOrMixtureData", "blocktype_num_id": "GLOBblocktype_1", "n_datapoints": 30, "n_components": 2, "compounds": [{"org_num": "DOIcomp_1", "comp_num_id": "GLOBcomp_24", "name": "1,2-ethanediol", "formula": "C2H6O2", "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N", "SMILES": "OCCO", "sample_num": "DOIcompSample_1_1"}, {"org_num": "DOIcomp_4", "comp_num_id": "GLOBcomp_1", "name": "water", "formula": "H2O", "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N", "SMILES": "O", "sample_num": "DOIcompSample_4_1"}], "solvents": [], "constraints": [{"BLKconstr_id": "BLKconstr_1", "constr_num_id": "GLOBconstr_1", "constr_id": "pressure_kpa", "name": "Pressure, kPa", "type": "ePressure", "value": 100.0, "digits": 1, "component_org_num": null, "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}}], "variables": [{"BLKvar_id": "BLKvar_1", "var_num_id": "GLOBvar_2", "var_id": "mole_fraction_DOIcomp_1", "name": "Mole fraction", "type": "eComponentComposition", "component_org_num": "DOIcomp_1", "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, "range": {"BLKvar_id": "BLKvar_1", "name": "Mole fraction", "min": 0.25, "max": 0.75, "n_unique": 3}, "range_min": 0.25, "range_max": 0.75}, {"BLKvar_id": "BLKvar_2", "var_num_id": "GLOBvar_1", "var_id": "temperature_k", "name": "Temperature, K", "type": "eTemperature", "component_org_num": null, "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, "range": {"BLKvar_id": "BLKvar_2", "name": "Temperature, K", "min": 296.45, "max": 449.85, "n_unique": 25}, "range_min": 296.45, "range_max": 449.85}], "properties": [{"BLKprop_id": "BLKprop_1", "prop_num_id": "GLOBprop_4", "prop_ID": "viscosity_pa_s", "name": "Viscosity, Pa*s", "group": "TransportProp", "component_org_num": null, "meas_num_id": "GLOBmeas_142", "meas_ID": "captub_ufactor_4", "method_standard": null, "method_custom": "CAPTUB:UFactor:4", "range": {"BLKprop_id": "BLKprop_1", "name": "Viscosity, Pa*s", "min": 0.000366, "max": 0.0123, "mean": 0.002177, "std": 0.002644, "n": 30}, "uncertainty": {"evaluation_method": "Propagation of evaluated standard uncertainties", "confidence_level": 95, "evaluator": "Data file compiler", "assessment_num": "BLKpropAssessment_1_1"}, "range_min": 0.000366, "range_max": 0.0123}], "phases": [{"owner_id": "BLKprop_1", "role": "property_phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKvar_1", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKvar_2", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKconstr_1", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}], "reaction_type": null, "participants": [], "notes": null, "declared_system_type": "binary", "declared_n_components": 2, "declared_compounds": [{"org_num": "DOIcomp_1", "comp_num_id": "GLOBcomp_24", "name": "1,2-ethanediol", "formula": "C2H6O2", "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N", "SMILES": "OCCO", "sample_num": "DOIcompSample_1_1"}, {"org_num": "DOIcomp_4", "comp_num_id": "GLOBcomp_1", "name": "water", "formula": "H2O", "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N", "SMILES": "O", "sample_num": "DOIcompSample_4_1"}], "parent_n_datapoints": 30, "subsystem_scope": null, "subsystem_point_runs": [], "subsystem_path_class": null, "subsystem_evidence_quality": null, "subsystem_condition_ranges": []}], "data_inspections": [{"doi": "10.1016/j.jct.2006.01.011", "block_number": "PROPblock_13", "table_mode": "complete", "columns": ["BLKpoint_id", "mass_fraction_<1,2-ethanediol>", "temperature_k", "pressure_kpa", "viscosity_pa_s"], "rows_shown": [{"BLKpoint_id": "BLKpoint_1", "mass_fraction_<1,2-ethanediol>": "0", "temperature_k": "293.15", "pressure_kpa": "101.325", "viscosity_pa_s": "0.001008"}, {"BLKpoint_id": "BLKpoint_2", "mass_fraction_<1,2-ethanediol>": "0.1", "temperature_k": "293.15", "pressure_kpa": "101.325", "viscosity_pa_s": "0.001293"}, {"BLKpoint_id": "BLKpoint_3", "mass_fraction_<1,2-ethanediol>": "0.2", "temperature_k": "293.15", "pressure_kpa": "101.325", "viscosity_pa_s": "0.001671"}, {"BLKpoint_id": "BLKpoint_4", "mass_fraction_<1,2-ethanediol>": "0.3", "temperature_k": "293.15", "pressure_kpa": "101.325", "viscosity_pa_s": "0.002177"}, {"BLKpoint_id": "BLKpoint_5", "mass_fraction_<1,2-ethanediol>": "0.4", "temperature_k": "293.15", "pressure_kpa": "101.325", "viscosity_pa_s": "0.002837"}, {"BLKpoint_id": "BLKpoint_6", "mass_fraction_<1,2-ethanediol>": "0.5", "temperature_k": "293.15", "pressure_kpa": "101.325", "viscosity_pa_s": "0.003558"}, {"BLKpoint_id": "BLKpoint_7", "mass_fraction_<1,2-ethanediol>": "0.6", "temperature_k": "293.15", "pressure_kpa": "101.325", "viscosity_pa_s": "0.004724"}, {"BLKpoint_id": "BLKpoint_8", "mass_fraction_<1,2-ethanediol>": "0.7", "temperature_k": "293.15", "pressure_kpa": "101.325", "viscosity_pa_s": "0.00636"}, {"BLKpoint_id": "BLKpoint_9", "mass_fraction_<1,2-ethanediol>": "0.8", "temperature_k": "293.15", "pressure_kpa": "101.325", "viscosity_pa_s": "0.008003"}, {"BLKpoint_id": "BLKpoint_10", "mass_fraction_<1,2-ethanediol>": "0.9", "temperature_k": "293.15", "pressure_kpa": "101.325", "viscosity_pa_s": "0.013999"}], "inspection_id": "INSP_eb6a6a268c1a", "lit_num_id": "GLOBlit_2656"}, {"doi": "10.1016/j.jct.2018.02.022", "block_number": "PROPblock_24", "table_mode": "rdp", "columns": ["BLKpoint_id", "temperature_k", "mole_fraction_<1,2-ethanediol>", "pressure_kpa", "viscosity_pa_s"], "rows_shown": [{"BLKpoint_id": "BLKpoint_1", "temperature_k": "293.15", "mole_fraction_<1,2-ethanediol>": "0.0494", "pressure_kpa": "92.3", "viscosity_pa_s": "0.0015411"}, {"BLKpoint_id": "BLKpoint_4", "temperature_k": "293.15", "mole_fraction_<1,2-ethanediol>": "0.2072", "pressure_kpa": "92.3", "viscosity_pa_s": "0.0035171"}, {"BLKpoint_id": "BLKpoint_9", "temperature_k": "293.15", "mole_fraction_<1,2-ethanediol>": "0.4446", "pressure_kpa": "92.3", "viscosity_pa_s": "0.0076382"}, {"BLKpoint_id": "BLKpoint_23", "temperature_k": "298.15", "mole_fraction_<1,2-ethanediol>": "0.2072", "pressure_kpa": "92.3", "viscosity_pa_s": "0.0028109"}, {"BLKpoint_id": "BLKpoint_28", "temperature_k": "298.15", "mole_fraction_<1,2-ethanediol>": "0.4446", "pressure_kpa": "92.3", "viscosity_pa_s": "0.0060624"}, {"BLKpoint_id": "BLKpoint_47", "temperature_k": "303.15", "mole_fraction_<1,2-ethanediol>": "0.4446", "pressure_kpa": "92.3", "viscosity_pa_s": "0.0053492"}, {"BLKpoint_id": "BLKpoint_65", "temperature_k": "308.15", "mole_fraction_<1,2-ethanediol>": "0.3921", "pressure_kpa": "92.3", "viscosity_pa_s": "0.0040265"}, {"BLKpoint_id": "BLKpoint_77", "temperature_k": "293.15", "mole_fraction_<1,2-ethanediol>": "0", "pressure_kpa": "92.3", "viscosity_pa_s": "0.0010673"}, {"BLKpoint_id": "BLKpoint_78", "temperature_k": "298.15", "mole_fraction_<1,2-ethanediol>": "0", "pressure_kpa": "92.3", "viscosity_pa_s": "0.00089689"}, {"BLKpoint_id": "BLKpoint_79", "temperature_k": "303.15", "mole_fraction_<1,2-ethanediol>": "0", "pressure_kpa": "92.3", "viscosity_pa_s": "0.0008385"}, {"BLKpoint_id": "BLKpoint_80", "temperature_k": "308.15", "mole_fraction_<1,2-ethanediol>": "0", "pressure_kpa": "92.3", "viscosity_pa_s": "0.00075887"}, {"BLKpoint_id": "BLKpoint_81", "temperature_k": "293.15", "mole_fraction_<1,2-ethanediol>": "1", "pressure_kpa": "92.3", "viscosity_pa_s": "0.020613"}, {"BLKpoint_id": "BLKpoint_82", "temperature_k": "298.15", "mole_fraction_<1,2-ethanediol>": "1", "pressure_kpa": "92.3", "viscosity_pa_s": "0.016223"}, {"BLKpoint_id": "BLKpoint_83", "temperature_k": "303.15", "mole_fraction_<1,2-ethanediol>": "1", "pressure_kpa": "92.3", "viscosity_pa_s": "0.013867"}, {"BLKpoint_id": "BLKpoint_84", "temperature_k": "308.15", "mole_fraction_<1,2-ethanediol>": "1", "pressure_kpa": "92.3", "viscosity_pa_s": "0.011483"}], "inspection_id": "INSP_10e84136b97d", "lit_num_id": "GLOBlit_5201"}, {"doi": "10.1021/acs.jced.6b00526", "block_number": "PROPblock_18", "table_mode": "rdp", "columns": ["BLKpoint_id", "temperature_k", "mole_fraction_<water>", "pressure_kpa", "viscosity_pa_s"], "rows_shown": [{"BLKpoint_id": "BLKpoint_1", "temperature_k": "293.15", "mole_fraction_<water>": "0", "pressure_kpa": "100.0", "viscosity_pa_s": "0.02113"}, {"BLKpoint_id": "BLKpoint_3", "temperature_k": "293.15", "mole_fraction_<water>": "0.2014", "pressure_kpa": "100.0", "viscosity_pa_s": "0.01495"}, {"BLKpoint_id": "BLKpoint_5", "temperature_k": "293.15", "mole_fraction_<water>": "0.4011", "pressure_kpa": "100.0", "viscosity_pa_s": "0.01005"}, {"BLKpoint_id": "BLKpoint_8", "temperature_k": "293.15", "mole_fraction_<water>": "0.6995", "pressure_kpa": "100.0", "viscosity_pa_s": "0.004584"}, {"BLKpoint_id": "BLKpoint_11", "temperature_k": "293.15", "mole_fraction_<water>": "1", "pressure_kpa": "100.0", "viscosity_pa_s": "0.000949"}, {"BLKpoint_id": "BLKpoint_12", "temperature_k": "298.15", "mole_fraction_<water>": "0", "pressure_kpa": "100.0", "viscosity_pa_s": "0.01724"}, {"BLKpoint_id": "BLKpoint_14", "temperature_k": "298.15", "mole_fraction_<water>": "0.2014", "pressure_kpa": "100.0", "viscosity_pa_s": "0.01219"}, {"BLKpoint_id": "BLKpoint_16", "temperature_k": "298.15", "mole_fraction_<water>": "0.4011", "pressure_kpa": "100.0", "viscosity_pa_s": "0.00831"}, {"BLKpoint_id": "BLKpoint_19", "temperature_k": "298.15", "mole_fraction_<water>": "0.6995", "pressure_kpa": "100.0", "viscosity_pa_s": "0.003884"}, {"BLKpoint_id": "BLKpoint_22", "temperature_k": "298.15", "mole_fraction_<water>": "1", "pressure_kpa": "100.0", "viscosity_pa_s": "0.000843"}, {"BLKpoint_id": "BLKpoint_23", "temperature_k": "303.15", "mole_fraction_<water>": "0", "pressure_kpa": "100.0", "viscosity_pa_s": "0.01423"}, {"BLKpoint_id": "BLKpoint_25", "temperature_k": "303.15", "mole_fraction_<water>": "0.2014", "pressure_kpa": "100.0", "viscosity_pa_s": "0.01014"}, {"BLKpoint_id": "BLKpoint_28", "temperature_k": "303.15", "mole_fraction_<water>": "0.4969", "pressure_kpa": "100.0", "viscosity_pa_s": "0.005653"}, {"BLKpoint_id": "BLKpoint_33", "temperature_k": "303.15", "mole_fraction_<water>": "1", "pressure_kpa": "100.0", "viscosity_pa_s": "0.000755"}], "inspection_id": "INSP_bdb58d28aae5", "lit_num_id": "GLOBlit_6951"}, {"doi": "10.1021/je020140j", "block_number": "PROPblock_5", "table_mode": "rdp", "columns": ["BLKpoint_id", "mole_fraction_<1,2-ethanediol>", "temperature_k", "pressure_kpa", "viscosity_pa_s"], "rows_shown": [{"BLKpoint_id": "BLKpoint_1", "mole_fraction_<1,2-ethanediol>": "0", "temperature_k": "293.15", "pressure_kpa": "101.0", "viscosity_pa_s": "0.001002"}, {"BLKpoint_id": "BLKpoint_7", "mole_fraction_<1,2-ethanediol>": "0", "temperature_k": "353.15", "pressure_kpa": "101.0", "viscosity_pa_s": "0.000356"}, {"BLKpoint_id": "BLKpoint_8", "mole_fraction_<1,2-ethanediol>": "0.0312", "temperature_k": "293.15", "pressure_kpa": "101.0", "viscosity_pa_s": "0.001337"}, {"BLKpoint_id": "BLKpoint_14", "mole_fraction_<1,2-ethanediol>": "0.0312", "temperature_k": "353.15", "pressure_kpa": "101.0", "viscosity_pa_s": "0.000434"}, {"BLKpoint_id": "BLKpoint_15", "mole_fraction_<1,2-ethanediol>": "0.0676", "temperature_k": "293.15", "pressure_kpa": "101.0", "viscosity_pa_s": "0.001785"}, {"BLKpoint_id": "BLKpoint_21", "mole_fraction_<1,2-ethanediol>": "0.0676", "temperature_k": "353.15", "pressure_kpa": "101.0", "viscosity_pa_s": "0.000525"}, {"BLKpoint_id": "BLKpoint_22", "mole_fraction_<1,2-ethanediol>": "0.1105", "temperature_k": "293.15", "pressure_kpa": "101.0", "viscosity_pa_s": "0.002272"}, {"BLKpoint_id": "BLKpoint_24", "mole_fraction_<1,2-ethanediol>": "0.1105", "temperature_k": "313.15", "pressure_kpa": "101.0", "viscosity_pa_s": "0.001319"}, {"BLKpoint_id": "BLKpoint_28", "mole_fraction_<1,2-ethanediol>": "0.1105", "temperature_k": "353.15", "pressure_kpa": "101.0", "viscosity_pa_s": "0.000629"}, {"BLKpoint_id": "BLKpoint_29", "mole_fraction_<1,2-ethanediol>": "0.162", "temperature_k": "293.15", "pressure_kpa": "101.0", "viscosity_pa_s": "0.002951"}, {"BLKpoint_id": "BLKpoint_31", "mole_fraction_<1,2-ethanediol>": "0.162", "temperature_k": "313.15", "pressure_kpa": "101.0", "viscosity_pa_s": "0.001677"}, {"BLKpoint_id": "BLKpoint_35", "mole_fraction_<1,2-ethanediol>": "0.162", "temperature_k": "353.15", "pressure_kpa": "101.0", "viscosity_pa_s": "0.000758"}, {"BLKpoint_id": "BLKpoint_36", "mole_fraction_<1,2-ethanediol>": "0.2248", "temperature_k": "293.15", "pressure_kpa": "101.0", "viscosity_pa_s": "0.003941"}, {"BLKpoint_id": "BLKpoint_38", "mole_fraction_<1,2-ethanediol>": "0.2248", "temperature_k": "313.15", "pressure_kpa": "101.0", "viscosity_pa_s": "0.002132"}, {"BLKpoint_id": "BLKpoint_42", "mole_fraction_<1,2-ethanediol>": "0.2248", "temperature_k": "353.15", "pressure_kpa": "101.0", "viscosity_pa_s": "0.000906"}, {"BLKpoint_id": "BLKpoint_43", "mole_fraction_<1,2-ethanediol>": "0.3031", "temperature_k": "293.15", "pressure_kpa": "101.0", "viscosity_pa_s": "0.005102"}, {"BLKpoint_id": "BLKpoint_45", "mole_fraction_<1,2-ethanediol>": "0.3031", "temperature_k": "313.15", "pressure_kpa": "101.0", "viscosity_pa_s": "0.002756"}, {"BLKpoint_id": "BLKpoint_49", "mole_fraction_<1,2-ethanediol>": "0.3031", "temperature_k": "353.15", "pressure_kpa": "101.0", "viscosity_pa_s": "0.0011"}, {"BLKpoint_id": "BLKpoint_50", "mole_fraction_<1,2-ethanediol>": "0.4036", "temperature_k": "293.15", "pressure_kpa": "101.0", "viscosity_pa_s": "0.006898"}, {"BLKpoint_id": "BLKpoint_52", "mole_fraction_<1,2-ethanediol>": "0.4036", "temperature_k": "313.15", "pressure_kpa": "101.0", "viscosity_pa_s": "0.003575"}, {"BLKpoint_id": "BLKpoint_54", "mole_fraction_<1,2-ethanediol>": "0.4036", "temperature_k": "333.15", "pressure_kpa": "101.0", "viscosity_pa_s": "0.002053"}, {"BLKpoint_id": "BLKpoint_56", "mole_fraction_<1,2-ethanediol>": "0.4036", "temperature_k": "353.15", "pressure_kpa": "101.0", "viscosity_pa_s": "0.001359"}, {"BLKpoint_id": "BLKpoint_57", "mole_fraction_<1,2-ethanediol>": "0.537", "temperature_k": "293.15", "pressure_kpa": "101.0", "viscosity_pa_s": "0.009696"}, {"BLKpoint_id": "BLKpoint_58", "mole_fraction_<1,2-ethanediol>": "0.537", "temperature_k": "303.15", "pressure_kpa": "101.0", "viscosity_pa_s": "0.006749"}, {"BLKpoint_id": "BLKpoint_59", "mole_fraction_<1,2-ethanediol>": "0.537", "temperature_k": "313.15", "pressure_kpa": "101.0", "viscosity_pa_s": "0.004776"}, {"BLKpoint_id": "BLKpoint_61", "mole_fraction_<1,2-ethanediol>": "0.537", "temperature_k": "333.15", "pressure_kpa": "101.0", "viscosity_pa_s": "0.002684"}, {"BLKpoint_id": "BLKpoint_63", "mole_fraction_<1,2-ethanediol>": "0.537", "temperature_k": "353.15", "pressure_kpa": "101.0", "viscosity_pa_s": "0.001748"}, {"BLKpoint_id": "BLKpoint_64", "mole_fraction_<1,2-ethanediol>": "0.723", "temperature_k": "293.15", "pressure_kpa": "101.0", "viscosity_pa_s": "0.014042"}, {"BLKpoint_id": "BLKpoint_65", "mole_fraction_<1,2-ethanediol>": "0.723", "temperature_k": "303.15", "pressure_kpa": "101.0", "viscosity_pa_s": "0.009399"}, {"BLKpoint_id": "BLKpoint_66", "mole_fraction_<1,2-ethanediol>": "0.723", "temperature_k": "313.15", "pressure_kpa": "101.0", "viscosity_pa_s": "0.006449"}, {"BLKpoint_id": "BLKpoint_68", "mole_fraction_<1,2-ethanediol>": "0.723", "temperature_k": "333.15", "pressure_kpa": "101.0", "viscosity_pa_s": "0.00351"}, {"BLKpoint_id": "BLKpoint_70", "mole_fraction_<1,2-ethanediol>": "0.723", "temperature_k": "353.15", "pressure_kpa": "101.0", "viscosity_pa_s": "0.002296"}, {"BLKpoint_id": "BLKpoint_71", "mole_fraction_<1,2-ethanediol>": "1", "temperature_k": "293.15", "pressure_kpa": "101.0", "viscosity_pa_s": "0.020833"}, {"BLKpoint_id": "BLKpoint_72", "mole_fraction_<1,2-ethanediol>": "1", "temperature_k": "303.15", "pressure_kpa": "101.0", "viscosity_pa_s": "0.013646"}, {"BLKpoint_id": "BLKpoint_73", "mole_fraction_<1,2-ethanediol>": "1", "temperature_k": "313.15", "pressure_kpa": "101.0", "viscosity_pa_s": "0.009443"}, {"BLKpoint_id": "BLKpoint_75", "mole_fraction_<1,2-ethanediol>": "1", "temperature_k": "333.15", "pressure_kpa": "101.0", "viscosity_pa_s": "0.00506"}, {"BLKpoint_id": "BLKpoint_77", "mole_fraction_<1,2-ethanediol>": "1", "temperature_k": "353.15", "pressure_kpa": "101.0", "viscosity_pa_s": "0.003021"}], "inspection_id": "INSP_ca607c3d05dd", "lit_num_id": "GLOBlit_8038"}, {"doi": "10.1021/je025610o", "block_number": "PROPblock_5", "table_mode": "rdp", "columns": ["BLKpoint_id", "mole_fraction_<1,2-ethanediol>", "temperature_k", "pressure_kpa", "viscosity_pa_s"], "rows_shown": [{"BLKpoint_id": "BLKpoint_1", "mole_fraction_<1,2-ethanediol>": "0.25", "temperature_k": "296.45", "pressure_kpa": "100.0", "viscosity_pa_s": "0.00369"}, {"BLKpoint_id": "BLKpoint_2", "mole_fraction_<1,2-ethanediol>": "0.25", "temperature_k": "313.05", "pressure_kpa": "100.0", "viscosity_pa_s": "0.00229"}, {"BLKpoint_id": "BLKpoint_4", "mole_fraction_<1,2-ethanediol>": "0.25", "temperature_k": "353.05", "pressure_kpa": "100.0", "viscosity_pa_s": "0.00099"}, {"BLKpoint_id": "BLKpoint_8", "mole_fraction_<1,2-ethanediol>": "0.25", "temperature_k": "435.55", "pressure_kpa": "100.0", "viscosity_pa_s": "0.000366"}, {"BLKpoint_id": "BLKpoint_9", "mole_fraction_<1,2-ethanediol>": "0.5", "temperature_k": "297.05", "pressure_kpa": "100.0", "viscosity_pa_s": "0.00761"}, {"BLKpoint_id": "BLKpoint_10", "mole_fraction_<1,2-ethanediol>": "0.5", "temperature_k": "313.05", "pressure_kpa": "100.0", "viscosity_pa_s": "0.00449"}, {"BLKpoint_id": "BLKpoint_11", "mole_fraction_<1,2-ethanediol>": "0.5", "temperature_k": "333.1", "pressure_kpa": "100.0", "viscosity_pa_s": "0.00262"}, {"BLKpoint_id": "BLKpoint_12", "mole_fraction_<1,2-ethanediol>": "0.5", "temperature_k": "353.05", "pressure_kpa": "100.0", "viscosity_pa_s": "0.0017"}, {"BLKpoint_id": "BLKpoint_13", "mole_fraction_<1,2-ethanediol>": "0.5", "temperature_k": "380.05", "pressure_kpa": "100.0", "viscosity_pa_s": "0.00107"}, {"BLKpoint_id": "BLKpoint_17", "mole_fraction_<1,2-ethanediol>": "0.5", "temperature_k": "440.65", "pressure_kpa": "100.0", "viscosity_pa_s": "0.0005"}, {"BLKpoint_id": "BLKpoint_18", "mole_fraction_<1,2-ethanediol>": "0.75", "temperature_k": "297.35", "pressure_kpa": "100.0", "viscosity_pa_s": "0.0123"}, {"BLKpoint_id": "BLKpoint_19", "mole_fraction_<1,2-ethanediol>": "0.75", "temperature_k": "313.05", "pressure_kpa": "100.0", "viscosity_pa_s": "0.00697"}, {"BLKpoint_id": "BLKpoint_20", "mole_fraction_<1,2-ethanediol>": "0.75", "temperature_k": "333.1", "pressure_kpa": "100.0", "viscosity_pa_s": "0.00388"}, {"BLKpoint_id": "BLKpoint_21", "mole_fraction_<1,2-ethanediol>": "0.75", "temperature_k": "353.05", "pressure_kpa": "100.0", "viscosity_pa_s": "0.00242"}, {"BLKpoint_id": "BLKpoint_22", "mole_fraction_<1,2-ethanediol>": "0.75", "temperature_k": "373.45", "pressure_kpa": "100.0", "viscosity_pa_s": "0.00162"}, {"BLKpoint_id": "BLKpoint_30", "mole_fraction_<1,2-ethanediol>": "0.75", "temperature_k": "449.85", "pressure_kpa": "100.0", "viscosity_pa_s": "0.000594"}], "inspection_id": "INSP_475115ec48f0", "lit_num_id": "GLOBlit_8106"}]}}]
</subagent_answer>
</tool_result>

## Assistant
<summary>Data collected for all systems. Now fitting the two well-characterized binaries (DMF+water from GLOBlit_9900::PROPblock_3, EG+water from GLOBlit_5201::PROPblock_24) at 298.15 K with Arrhenius mixing rule. DMF+EG binary has only 1 composition point (x_EG=0.5408) — will need special handling. Will use binary RK fits to estimate ternary equimolar viscosity.</summary>
<tool_call>fit_multi_system(systems=[{'label': 'DMF_w…)</tool_call>

## User
<tool_result>
(validation blocked fit_multi_system earlier — corrected)
</tool_result>

## Assistant
<summary>Fitting DMF+water and EG+water binaries at 298.15 K with Arrhenius mixing rule. DMF+EG has only 1 composition - will address separately.</summary>
<tool_call>fit_multi_system(systems=[{'label': 'DMF_w…)</tool_call>

## User
<tool_result>
**Multi-system RK Fit** — 2 systems
Errors: DMF_water: Constraint column 'Temperature, K' not found in block; EG_water: Constraint column 'Temperature, K' not found in block

| Label | DOI | Block | Components | Order | R² | RMSE | n pts |
|-------|-----|-------|------------|-------|----|------|-------|
| DMF_water | — | — | — | ERROR: Constraint column 'Temperature, K' not f | | |
| EG_water | — | — | — | ERROR: Constraint column 'Temperature, K' not f | | |

</tool_result>

## Assistant
<summary>Column name mismatch — need exact column names from inspect_block fitting guidance. Inspecting both blocks to get correct variable names for x_vars_constrained.</summary>
<tool_call>inspect_block(doi=10.1021/je300608v, block_number=PROPblock_3)</tool_call>

## User
<tool_result>
(validation blocked inspect_block earlier — corrected)
</tool_result>

## Assistant
<summary>Inspecting both blocks to get exact column names for fitting variable constraints.</summary>
<tool_call>inspect_block(doi=10.1021/je300608v, block_number=PROPblock_3)</tool_call>

## User
<tool_result>
(validation blocked inspect_block earlier — corrected)
</tool_result>

## Assistant
<summary>Inspecting both blocks to get exact column names for fitting constraints.</summary>
<tool_call>inspect_block(doi=10.1021/je300608v, block_number=PROPblock_3)</tool_call>

## User
<tool_result>
**Block GLOBlit_9900 / DOI 10.1021/je300608v / PROPblock_3 @ declared** (PureOrMixtureData)
Compounds: dimethylformamide, water | Rows: 60
x‑columns: ['mole_fraction_<water>'] | y‑columns: ['viscosity_pa_s']

**Property response semantics (reported metadata; values are not materialized here)**
- **BLKprop_1 / GLOBprop_4** `viscosity_pa_s` (viscosity_pa_s)
  - reported response: Direct value, X
  - measurement: GLOBmeas_4 / capillary_tube_ostwald_ubbelohde_method
  - property phase: Liquid (GLOBphase_1; liquid)
  - reference: none; T=unspecified K; P=unspecified kPa
  - reference phase: none
  - component_org_num: none

**Selected property response contract (inspection only; values are not materialized here)**
- **BLKprop_1 / GLOBprop_4** `viscosity_pa_s` (viscosity_pa_s)
  - reported response: Direct value, X [direct]
  - units: reported=Pa*s; absolute=Pa*s
  - preparation gate: reference_materialization=False; normalized_composition=False; supported=True
  - reference: none; T=unspecified K; P=unspecified kPa
  - property phase: Liquid (GLOBphase_1; liquid)
  - reference phase: none
  - component_org_num: none

| Column | Min | Max | Valid pts |
|--------|-----|-----|-----------|
| temperature_k | 293.15 | 308.15 | 60 |
| mole_fraction_<water> | 0 | 1 | 60 |
| pressure_kpa | 101 | 101 | 60 |
| viscosity_pa_s | 0.000712 | 0.002885 | 60 |

</tool_result>

## Assistant
<summary>Column names are lowercase: "temperature_k", "mole_fraction_<water>", "viscosity_pa_s". Now fitting both binaries with correct x_vars_constrained using lowercase column names.</summary>
<tool_call>fit_multi_system(systems=[{'label': 'DMF_w…)</tool_call>

## User
<tool_result>
(validation blocked fit_multi_system earlier — corrected)
</tool_result>

## Assistant
<summary>Fitting DMF+water and EG+water binaries at 298.15 K with Arrhenius mixing rule, using correct lowercase column names from inspection.</summary>
<tool_call>fit_multi_system(systems=[{'label': 'DMF_w…)</tool_call>

## User
<tool_result>
(validation blocked fit_multi_system earlier — corrected)
</tool_result>

## Assistant
<summary>Fitting DMF+water and EG+water binaries at 298.15 K with Arrhenius mixing rule. Fixing tasks argument to be a string.</summary>
<tool_call>fit_multi_system(systems=[{'label': 'DMF_w…)</tool_call>

## User
<tool_result>
**Multi-system RK Fit** — 2 systems

| Label | DOI | Block | Components | Order | R² | RMSE | n pts |
|-------|-----|-------|------------|-------|----|------|-------|
| DMF_water | GLOBlit_9900 / DOI 10.1021/je300608v | PROPblock_3 @ declared | water, dimethylformamide | 5 | 0.999973 | 0.00152309 | 12 |
| EG_water | GLOBlit_5201 / DOI 10.1016/j.jct.2018.02.022 | PROPblock_24 @ declared | 1,2-ethanediol, water | 3 | 0.999940 | 0.00131989 | 19 |

**DMF_water** coeffs: [3.14029, 3.88544, 1.91579, -0.00569291, 0.0417895, 0.390893]
Property response: BLKprop_1 / GLOBprop_4; kind=direct; equation=X = reported X; reference_sources=0; units=Pa*s -> Pa*s.
  pure values (x = mole_fraction_<water>): water=0.0008903, dimethylformamide=0.0008045
  source: block-edges (dimethylformamide: direct/good, water: direct/good)

**EG_water** coeffs: [2.39674, -1.04444, 0.668173, -0.3209]
Property response: BLKprop_1 / GLOBprop_4; kind=direct; equation=X = reported X; reference_sources=0; units=Pa*s -> Pa*s.
  pure values (x = mole_fraction_<1,2-ethanediol>): 1,2-ethanediol=0.016223, water=0.00089689
  source: block-edges (water: direct/good, 1,2-ethanediol: direct/good)

</tool_result>

## Assistant
<summary>Both binary fits successful. DMF+water: order 5, R²=0.999973, coeffs=[3.14029, 3.88544, 1.91579, -0.00569, 0.04179, 0.39089]. EG+water: order 3, R²=0.99994, coeffs=[2.39674, -1.04444, 0.66817, -0.3209]. Now computing ideal baselines and predictions to estimate ternary equimolar viscosity via Muggianu extension of Arrhenius mixing rule. DMF+EG binary has only 1 point (x_EG=0.5408, η=0.0030647) — will extract A₀ from it.</summary>
<tool_call>predict_from_rk(property_type=viscosity, coeffs=[3.14029, 3.88544…, pure_values={'water': 0.000…)</tool_call>

## User
<tool_result>
**RK Prediction** (order 5, arrhenius)
Components: dimethylformamide, water | 101 grid points
Y(x=0) = 0.0008903, Y(x=0.5) ≈ 0.0018556, Y(x=1) = 0.0008045
Y_max = 0.00237562 at x1 = 0.71
Max |excess| (ln-space) = 1.05403

</tool_result>

## Assistant
<summary>Both binary fits successful. Now predicting EG+water at x=0.5 to support ternary estimation. DMF+EG binary has only 1 point (x_EG=0.5408, η=0.0030647), so I'll extract a single RK coefficient A₀ from it. Will combine all three binary contributions via Muggianu/Kohler extension of Arrhenius mixing rule to estimate equimolar ternary viscosity.</summary>
<tool_call>predict_from_rk(property_type=viscosity, coeffs=[2.39674, -1.0444…, pure_values={'1,2-ethanedio…)</tool_call>

## User
<tool_result>
(validation blocked predict_from_rk earlier — corrected)
</tool_result>

## Assistant
<summary>Both binary fits complete. DMF+water: A₀=3.14029 (order 5, R²=0.999973). EG+water: A₀=2.39674 (order 3, R²=0.99994). DMF+EG: extracted A₀=-1.1541 from single point (x_EG=0.5408, η=0.0030647). Muggianu/Arrhenius ternary estimate at equimolar: ln(η)=-6.090+0.487=-5.603, η≈0.00369 Pa·s (3.69 mPa·s). Cross-validates well against nearby ternary measurements (0.00357–0.00375 Pa·s).</summary>
<tool_call>predict_from_rk(property_type=viscosity, coeffs=[3.14029, 3.88544…, pure_values={'water': 0.000…)</tool_call>

## User
<tool_result>
**RK Prediction** (order 5, arrhenius)
Components: dimethylformamide, water | 101 grid points
Y(x=0) = 0.0008903, Y(x=0.5) ≈ 0.0018556, Y(x=1) = 0.0008045
Y_max = 0.00237562 at x1 = 0.71
Max |excess| (ln-space) = 1.05403

</tool_result>

## Assistant
<summary>Calculation complete. Equimolar ternary viscosity estimated via Muggianu/Arrhenius from three binary RK fits: DMF+water (order 5, R²=0.999973), EG+water (order 3, R²=0.99994), DMF+EG (A₀ from single point). Result: η ≈ 0.00368 Pa·s (3.68 mPa·s) at 298.15 K. Cross-validates against nearby ternary measurements (0.00357–0.00375 Pa·s). Ready to assemble final answer.</summary>
<tool_call>list_session_files()</tool_call>

## User
<tool_result>
{
  "session_dir": "\\\\Sheldon.cse.anl.gov\\yunkai.sun$\\_Code_Maintenance\\_outputs_user\\yunkai.sun\\ThermoML\\Analysis\\run_20260905_064310_067492_5aad5d4d",
  "n_files": 8,
  "files": [
    {
      "category": "data",
      "path": "\\\\Sheldon.cse.anl.gov\\yunkai.sun$\\_Code_Maintenance\\_outputs_user\\yunkai.sun\\ThermoML\\Analysis\\run_20260905_064310_067492_5aad5d4d\\data\\10_1021_je300608v_BPROPblock_3_T298.1_fit.csv",
      "description": "RK fit data \u2014 10.1021/je300608v PROPblock_3_T298.1"
    },
    {
      "category": "data",
      "path": "\\\\Sheldon.cse.anl.gov\\yunkai.sun$\\_Code_Maintenance\\_outputs_user\\yunkai.sun\\ThermoML\\Analysis\\run_20260905_064310_067492_5aad5d4d\\data\\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_fit.csv",
      "description": "RK fit data \u2014 10.1016/j.jct.2018.02.022 PROPblock_24_T298.1"
    },
    {
      "category": "data",
      "path": "\\\\Sheldon.cse.anl.gov\\yunkai.sun$\\_Code_Maintenance\\_outputs_user\\yunkai.sun\\ThermoML\\Analysis\\run_20260905_064310_067492_5aad5d4d\\data\\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_excess.csv",
      "description": "Excess property \u2014 10.1016/j.jct.2018.02.022 PROPblock_24_T298.1"
    },
    {
      "category": "data",
      "path": "\\\\Sheldon.cse.anl.gov\\yunkai.sun$\\_Code_Maintenance\\_outputs_user\\yunkai.sun\\ThermoML\\Analysis\\run_20260905_064310_067492_5aad5d4d\\data\\10_1021_je300608v_BPROPblock_3_T298.1_excess.csv",
      "description": "Excess property \u2014 10.1021/je300608v PROPblock_3_T298.1"
    },
    {
      "category": "plot",
      "path": "\\\\Sheldon.cse.anl.gov\\yunkai.sun$\\_Code_Maintenance\\_outputs_user\\yunkai.sun\\ThermoML\\Analysis\\run_20260905_064310_067492_5aad5d4d\\plots\\10_1021_je300608v_BPROPblock_3_T298.1_fit.png",
      "description": "RK fit plot \u2014 10.1021/je300608v PROPblock_3_T298.1"
    },
    {
      "category": "plot",
      "path": "\\\\Sheldon.cse.anl.gov\\yunkai.sun$\\_Code_Maintenance\\_outputs_user\\yunkai.sun\\ThermoML\\Analysis\\run_20260905_064310_067492_5aad5d4d\\plots\\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_fit.png",
      "description": "RK fit plot \u2014 10.1016/j.jct.2018.02.022 PROPblock_24_T298.1"
    },
    {
      "category": "plot",
      "path": "\\\\Sheldon.cse.anl.gov\\yunkai.sun$\\_Code_Maintenance\\_outputs_user\\yunkai.sun\\ThermoML\\Analysis\\run_20260905_064310_067492_5aad5d4d\\plots\\10_1021_je300608v_BPROPblock_3_T298.1_excess.png",
      "description": "Excess plot \u2014 10.1021/je300608v PROPblock_3_T298.1"
    },
    {
      "category": "plot",
      "path": "\\\\Sheldon.cse.anl.gov\\yunkai.sun$\\_Code_Maintenance\\_outputs_user\\yunkai.sun\\ThermoML\\Analysis\\run_20260905_064310_067492_5aad5d4d\\plots\\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_excess.png",
      "description": "Excess plot \u2014 10.1016/j.jct.2018.02.022 PROPblock_24_T298.1"
    }
  ]
}
</tool_result>

## Assistant
<reasoning>
Let me assemble the final answer. I need to carefully work through the ternary estimation.

**The question:** What viscosity should I expect for an equimolar DMF + ethylene glycol + water liquid mixture at 25 °C?

**Equimolar composition:** x₁ = x₂ = x₃ = 1/3 for DMF, EG, and water.

**Approach:** The ternary equimolar composition was not directly measured. The ternary data block (GLOBlit_8892::PROPblock_38) follows a dilution path from DMF+EG binary toward pure water — it does NOT pass through the equimolar point (1/3, 1/3, 1/3). The closest measured ternary points are at compositions like (x_water=0.2929, x_EG=0.3824, x_DMF=0.2247) and (x_water=0.4825, x_EG=0.2799, x_DMF=0.2376), neither of which is equimolar.

So I need to estimate using binary contributions via the Muggianu (symmetric) extension of the Arrhenius mixing rule.

**Arrhenius mixing rule for ternary:**
ln(η_mix) = x₁·ln(η₁) + x₂·ln(η₂) + x₃·ln(η₃) + Δln(η)_excess

where the excess is built from binary contributions using the Muggianu extension:

Δln(η)_excess = Σ_{i<j} 4·xᵢ·xⱼ · Σₖ Aₖ^(ij) · (xᵢ - xⱼ)^k

For equimolar (x₁ = x₂ = x₃ = 1/3):
- Each 4·xᵢ·xⱼ = 4·(1/3)·(1/3) = 4/9
- Each (xᵢ - xⱼ) = 0

So only the A₀ terms survive (all odd-order terms vanish because xᵢ = xⱼ, and even-order terms with (0)^k = 0 for k>0).

Wait, let me be more careful. The RK expansion is:
Δln(η)_ij = xᵢ·xⱼ · Σₖ Aₖ · (xᵢ - xⱼ)^k

In the Muggianu extension for ternary, we use rescaled binary compositions:
ξᵢ = xᵢ/(xᵢ + xⱼ), ξⱼ = xⱼ/(xᵢ + xⱼ)

For equimolar: ξᵢ = ξⱼ = 0.5 for all pairs.

The Muggianu formula:
Δln(η)_excess = Σ_{i<j} (xᵢ + xⱼ)² · [ξᵢ·ξⱼ · Σₖ Aₖ^(ij) · (ξᵢ - ξⱼ)^k]

Wait, actually the standard Muggianu extension is:

G^E_ternary = Σ_{i<j} [4·xᵢ·xⱼ / (xᵢ+xⱼ)²] · (xᵢ+xⱼ)² · G^E_ij(ξᵢ)

Hmm, let me think more carefully. The Muggianu formula is:

G^E_ternary(x₁,x₂,x₃) = Σ_{i<j} [4·xᵢ·xⱼ/(x̃ᵢ+x̃ⱼ)²] · G^E_ij(ξᵢ)

where ξᵢ = xᵢ/(xᵢ+xⱼ) and G^E_ij is the binary excess evaluated at ξᵢ.

Actually, the simplest and most standard form: In the Muggianu model, the ternary excess is:

Δln(η)_excess = Σ_{i<j} [xᵢ·xⱼ · Σₖ Aₖ^(ij) · (xᵢ - xⱼ)^k]

This is the asymmetric Muggianu extension where binary compositions are used directly (not rescaled). For equimolar x₁=x₂=x₃=1/3:

Each xᵢ·xⱼ = 1/9
Each (xᵢ - xⱼ) = 0

So only A₀ terms survive:
Δln(η)_excess = (1/9)·A₀^(12) + (1/9)·A₀^(13) + (1/9)·A₀^(23)

Now the ideal part:
ln(η_ideal) = (1/3)·ln(η_DMF) + (1/3)·ln(η_EG) + (1/3)·ln(η_water)

Pure values:
- η_DMF = 0.0008045 Pa·s (from DMF+water fit, block-edge)
- η_water = 0.0008903 Pa·s (from DMF+water fit, block-edge)
- η_EG = 0.016223 Pa·s (from EG+water fit, block-edge)

Wait, I need to be careful about which pure value to use for water. From DMF+water fit: water=0.0008903, DMF=0.0008045. From EG+water fit: water=0.00089689, EG=0.016223.

The water values are slightly different (0.0008903 vs 0.00089689) because they come from different sources. I'll use the average or pick one consistently. Let me use the DMF+water source value for water (0.0008903) since it's from the same paper as the ternary data.

Actually, for the Arrhenius mixing rule, the RK coefficients are fitted in ln-space. Let me compute:

ln(η_DMF) = ln(0.0008045) = -7.1262
ln(η_EG) = ln(0.016223) = -4.1209
ln(η_water) = ln(0.0008903) = -7.0252

Ideal part:
ln(η_ideal) = (1/3)·(-7.1262) + (1/3)·(-4.1209) + (1/3)·(-7.0252)
= (1/3)·(-18.2723)
= -6.0908

η_ideal = exp(-6.0908) = 0.002264 Pa·s... wait let me recalculate.

Actually wait. exp(-6.0908) = ?
exp(-6) = 0.002479
exp(-6.09) ≈ 0.002479 × exp(-0.09) ≈ 0.002479 × 0.9139 ≈ 0.002266

OK so η_ideal ≈ 0.00227 Pa·s.

Now the excess contributions. The A₀ values from the binary fits:

1. DMF+water: A₀ = 3.14029 (from fit, x = mole_fraction_<water>)
   - This means the RK expansion is: Δln(η) = x_water·x_DMF · [3.14029 + 3.88544·(x_water - x_DMF) + ...]
   - At equimolar binary (x_water = x_DMF = 0.5): Δln(η) = 0.25 · 3.14029 = 0.78507 (only A₀ survives when x₁=x₂)

2. EG+water: A₀ = 2.39674 (from fit, x = mole_fraction_<1,2-ethanediol>)
   - At equimolar: Δln(η) = 0.25 · 2.39674 = 0.59919

3. DMF+EG: Need to extract A₀ from the single data point.
   The single point: x_EG = 0.5408, x_DMF = 0.4592, η = 0.0030647 Pa·s at 298.15 K.
   
   Arrhenius ideal: ln(η_ideal) = 0.5408·ln(0.016223) + 0.4592·ln(0.0008045)
   = 0.5408·(-4.1209) + 0.4592·(-7.1262)
   = -2.2286 + (-3.2716)
   = -5.5002
   η_ideal = exp(-5.5002) = 0.004087 Pa·s
   
   Measured: ln(0.0030647) = -5.7876
   
   Δln(η) = -5.7876 - (-5.5002) = -0.2874
   
   At x_EG = 0.5408, x_DMF = 0.4592:
   Δln(η) = x_EG·x_DMF · A₀ (assuming only A₀)
   = 0.5408 × 0.4592 × A₀
   = 0.24833 × A₀
   
   A₀ = -0.2874 / 0.24833 = -1.1573

So A₀^(DMF,EG) ≈ -1.157

Now the ternary excess at equimolar (x₁=x₂=x₃=1/3):
Δln(η)_excess = (1/9)·[A₀^(DMF,water) + A₀^(EG,water) + A₀^(DMF,EG)]
= (1/9)·[3.14029 + 2.39674 + (-1.1573)]
= (1/9)·[4.3797]
= 0.4866

Total:
ln(η_ternary) = -6.0908 + 0.4866 = -5.6042
η_ternary = exp(-5.6042) = ?

exp(-5.6) = 0.003698
exp(-5.6042) ≈ 0.003698 × exp(-0.0042) ≈ 0.003698 × 0.99581 ≈ 0.003683

So η_ternary ≈ 0.00368 Pa·s ≈ 3.68 mPa·s

**Cross-validation with ternary measurements:**
The ternary data from GLOBlit_8892::PROPblock_38 shows:
- x_water=0.2929, x_EG=0.3824, x_DMF=0.2247: η=0.0035692 Pa·s
- x_water=0.4825, x_EG=0.2799, x_DMF=0.2376: η=0.0037485 Pa·s

The equimolar point (0.333, 0.333, 0.333) lies between these two measured compositions. The estimate of 0.00368 Pa·s falls right between 0.00357 and 0.00375, which is very encouraging.

Now let me be very precise about the calculation steps and present them clearly.

Let me recompute more carefully:

Pure component viscosities at 298.15 K:
- η_DMF = 0.0008045 Pa·s (from GLOBlit_9900::PROPblock_3, block-edge at x_water=0)
- η_water = 0.0008903 Pa·s (from GLOBlit_9900::PROPblock_3, block-edge at x_water=1)
- η_EG = 0.016223 Pa·s (from GLOBlit_5201::PROPblock_24, block-edge at x_EG=1)

ln values:
- ln(0.0008045) = ln(8.045e-4) = ln(8.045) + ln(1e-4) = 2.08527 - 9.21034 = -7.12507
- ln(0.0008903) = ln(8.903e-4) = ln(8.903) + ln(1e-4) = 2.18641 - 9.21034 = -7.02393
- ln(0.016223) = ln(1.6223e-2) = ln(1.6223) + ln(1e-2) = 0.48424 - 4.60517 = -4.12093

Ideal Arrhenius at equimolar:
ln(η_ideal) = (1/3)·(-7.12507 + (-4.12093) + (-7.02393))
= (1/3)·(-18.26993)
= -6.08998

η_ideal = exp(-6.08998) = ?
exp(-6) = 0.0024788
exp(-0.08998) = 0.91394
η_ideal = 0.0024788 × 0.91394 = 0.002265 Pa·s

DMF+EG binary A₀:
η_measured = 0.0030647 at x_EG = 0.5408
ln(0.0030647) = ln(3.0647e-3) = ln(3.0647) - ln(1000) = 1.11989 - 6.90776 = -5.78787

Ideal for DMF+EG binary:
ln(η_ideal_12) = 0.5408·ln(0.016223) + 0.4592·ln(0.0008045)
= 0.5408·(-4.12093) + 0.4592·(-7.12507)
= -2.22900 + -3.27103
= -5.50003

Excess: Δln = -5.78787 - (-5.50003) = -0.28784
x_EG·x_DMF = 0.5408 × 0.4592 = 0.24833
A₀^(DMF,EG) = -0.28784 / 0.24833 = -1.1591

Ternary excess at equimolar:
Δln(η) = (1/9)·[3.14029 + 2.39674 + (-1.1591)]
= (1/9)·(4.37793)
= 0.48644

Total:
ln(η_ternary) = -6.08998 + 0.48644 = -5.60354
η_ternary = exp(-5.60354)

exp(-5.6) = 0.003698
exp(-0.00354) = 0.99647
η_ternary = 0.003698 × 0.99647 = 0.003685 Pa·s

So η ≈ 0.00368 Pa·s ≈ 3.68 mPa·s.

This is a solid estimate. Let me now write the final answer.
</reasoning>

<answer>

## Estimated Viscosity of Equimolar DMF + Ethylene Glycol + Water at 25 °C

### Bottom Line

**η ≈ 0.00368 Pa·s (3.68 mPa·s)** at 298.15 K and ambient pressure.

This is an estimate — the equimolar ternary composition (x_DMF = x_EG = x_water = 1/3) was not measured directly. The estimate is built from three binary Redlich-Kister fits using the Arrhenius (logarithmic) mixing rule, combined via the Muggianu symmetric extension to ternary systems, and cross-validated against nearby ternary measurements.

---

### 1. Why the Equimolar Point Was Not Measured

The only ternary viscosity block in the ThermoML database for this system is DOI 10.1021/je060113j (GLOBlit_8892, PROPblock_38). Its 11 data points at 298.15 K follow a dilution path from the DMF + EG binary (x_water = 0, x_EG = 0.5408) toward pure water — they do **not** pass through the equimolar point (1/3, 1/3, 1/3). The two nearest measured ternary compositions bracket the target:

| x(water) | x(EG) | x(DMF) | η (Pa·s) |
|-----------|--------|--------|-----------|
| 0.2929 | 0.3824 | 0.2247 | 0.0035692 |
| 0.4825 | 0.2799 | 0.2376 | 0.0037485 |

The equimolar point lies between these, so the estimate of 0.00368 Pa·s is physically consistent.

---

### 2. Mathematical Framework

**Arrhenius mixing rule.** For viscosity, the natural mixing variable is ln η. The ideal (Arrhenius) baseline for a ternary mixture is:

> ln η_ideal = x₁·ln η₁* + x₂·ln η₂* + x₃·ln η₃*

The excess departure is modelled by Redlich-Kister (RK) polynomials fitted to each binary pair. For a ternary system, the **Muggianu symmetric extension** combines the three binary excess functions:

> Δln η_excess = Σ_{i<j} xᵢ·xⱼ · Σₖ Aₖ^(ij) · (xᵢ − xⱼ)^k

At the equimolar point (x₁ = x₂ = x₃ = 1/3), every (xᵢ − xⱼ) = 0, so **only the A₀ coefficient of each binary pair survives**:

> Δln η_excess = (1/9) · [A₀^(DMF,water) + A₀^(EG,water) + A₀^(DMF,EG)]

---

### 3. Pure-Component Viscosities at 298.15 K

| Component | η* (Pa·s) | ln η* | Source |
|-----------|-----------|-------|--------|
| DMF | 0.0008045 | −7.125 | GLOBlit_9900 / PROPblock_3, block-edge (x_water = 0) |
| Water | 0.0008903 | −7.024 | GLOBlit_9900 / PROPblock_3, block-edge (x_water = 1) |
| 1,2-Ethanediol (EG) | 0.016223 | −4.121 | GLOBlit_5201 / PROPblock_24, block-edge (x_EG = 1) |

**Ideal Arrhenius baseline at equimolar:**

> ln η_ideal = (1/3)(−7.125 − 4.121 − 7.024) = −6.090

> η_ideal = exp(−6.090) = **0.00227 Pa·s**

---

### 4. Binary Redlich-Kister Fits (Arrhenius Mixing Rule)

#### 4a. DMF + Water

- **Source:** DOI 10.1021/je300608v (GLOBlit_9900), PROPblock_3
- **Data:** 12 points at 298.15 K, 101.0 kPa, mole fraction of water
- **BIC-selected order:** 5
- **R² = 0.999973**, RMSE = 0.001523 (ln-space)
- **RK coefficients (ln-space):** A₀ = 3.14029, A₁ = 3.88544, A₂ = 1.91579, A₃ = −0.00569, A₄ = 0.04179, A₅ = 0.39089
- **A₀ = 3.140** (the only coefficient needed at equimolar)

This binary shows a pronounced viscosity maximum near x_water ≈ 0.7 (η_max ≈ 0.00248 Pa·s), reflecting strong DMF–water hydrogen bonding where the C=O of DMF acts as a hydrogen-bond acceptor for water.

#### 4b. Ethylene Glycol + Water

- **Source:** DOI 10.1016/j.jct.2018.02.022 (GLOBlit_5201), PROPblock_24
- **Data:** 19 points at 298.15 K, 92.3 kPa, mole fraction of EG
- **BIC-selected order:** 3
- **R² = 0.999940**, RMSE = 0.001320 (ln-space)
- **RK coefficients (ln-space):** A₀ = 2.39674, A₁ = −1.04444, A₂ = 0.66817, A₃ = −0.32090
- **A₀ = 2.397**

EG–water mixtures show a monotonic increase in viscosity with EG content (pure EG is ~18× more viscous than water), driven by the extensive hydrogen-bonding network of EG's two hydroxyl groups.

#### 4c. DMF + Ethylene Glycol

- **Source:** DOI 10.1021/je060113j (GLOBlit_8892), PROPblock_25
- **Data:** Only **1 composition** at 298.15 K: x_EG = 0.5408, η = 0.0030647 Pa·s
- **Extraction of A₀:** With only one data point, only A₀ can be determined. The Arrhenius ideal baseline at x_EG = 0.5408 is:

  > ln η_ideal = 0.5408·ln(0.016223) + 0.4592·ln(0.0008045) = −5.500

  > ln η_measured = ln(0.0030647) = −5.788

  > Δln η = −5.788 − (−5.500) = −0.288

  > A₀ = Δln η / (x_EG · x_DMF) = −0.288 / (0.5408 × 0.4592) = **−1.159**

The **negative** A₀ means the DMF–EG interaction produces a viscosity *lower* than the Arrhenius ideal — the mixture is less structured than the geometric-mean prediction. This makes chemical sense: DMF is an aprotic solvent that disrupts EG's intramolecular hydrogen-bonding network without forming comparably strong new associations.

**Limitation:** This A₀ is extracted from a single data point near x = 0.5, so it is the least certain of the three binary contributions. However, the composition (0.5408) is close to equimolar, which is exactly where A₀ dominates, making the extraction relatively robust for this purpose.

---

### 5. Ternary Estimate via Muggianu Extension

At x_DMF = x_EG = x_water = 1/3:

| Contribution | Value |
|-------------|-------|
| ln η_ideal | −6.090 |
| (1/9) × A₀^(DMF,water) = (1/9) × 3.140

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **UNGROUNDED_LITERAL** PROPblock_38: 0.2247 (near '…--------|--------|--------|-----------| | 0.2929 | 0.3824 | …') matches no inspected row/stat, database table, or other source of PROPblock_38
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_38", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 0.2247})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_38: 0.2376 (near '…0.2929 | 0.3824 | 0.2247 | 0.0035692 | | 0.4825 | 0.2799 | 0…') matches no inspected row/stat, database table, or other source of PROPblock_38
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_38", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 0.2376})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_38: 0.00368 (near '…The equimolar point lies between these, so the estimate of 0…') matches no inspected row/stat, database table, or other source of PROPblock_38
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_38", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 0.00368})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_3 + PROPblock_24: -7.125 (near '…---------|-----------|-------|--------| | DMF | 0.0008045 | …') matches no inspected row/stat, database table, or other source of PROPblock_3 + PROPblock_24
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_3", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": -7.125})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_3 + PROPblock_24: -7.024 (near '…5 |   /  , block-edge (x_water = 0) | | Water | 0.0008903 | …') matches no inspected row/stat, database table, or other source of PROPblock_3 + PROPblock_24
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_3", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": -7.024})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_3 + PROPblock_24: -4.121 (near '…ock-edge (x_water = 1) | | 1,2-Ethanediol (EG) | 0.016223 | …') matches no inspected row/stat, database table, or other source of PROPblock_3 + PROPblock_24
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_3", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": -4.121})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_24: -7.125 (near '…al Arrhenius baseline at equimolar:**  > ln η_ideal = (1/3)(…') matches no inspected row/stat, database table, or other source of PROPblock_24
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_24", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": -7.125})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_24: 4.121 (near '…ius baseline at equimolar:**  > ln η_ideal = (1/3)(-7.125 - …') matches no inspected row/stat, database table, or other source of PROPblock_24
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_24", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 4.121})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- … and 7 more of the same kinds — PROPblock_24: 7.024, -6.090, 18; PROPblock_25: 0.4592, -5.500, -5.788
Inspected so far: PROPblock_13, PROPblock_18, PROPblock_24, PROPblock_25, PROPblock_3, PROPblock_38, PROPblock_5, PROPblock_9

Verified as grounded — correct as quoted, keep unchanged:
- PROPblock_3: 298.15, 0.7, 0.00248
Partially grounded — the values listed below ARE verified and must stay as quoted; change ONLY the flagged one(s) above:
- PROPblock_38: 298.15, 0.5408, 0.2929, 0.3824, 0.0035692, 0.4825, 0.2799, 0.0037485
- PROPblock_3 + PROPblock_24: 0.0008045, 0.0008903, 0.016223
- PROPblock_24: 19, 298.15
- PROPblock_25: 0.016223, 0.0008045, 298.15, 0.5408, 0.0030647

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

## Assistant
<answer>

## Estimated Viscosity of Equimolar DMF + Ethylene Glycol + Water at 25 °C

### Bottom Line

**η ≈ 0.00368 Pa·s (3.68 mPa·s)** at 298.15 K and ambient pressure. *(This value is computed — not a database datum — derived from the calculation detailed below.)*

This is an estimate — the equimolar ternary composition (x_DMF = x_EG = x_water = 1/3) was not measured directly. The estimate is built from three binary Redlich-Kister fits using the Arrhenius (logarithmic) mixing rule, combined via the Muggianu symmetric extension to ternary systems, and cross-validated against nearby ternary measurements.

---

### 1. Why the Equimolar Point Was Not Measured

The only ternary viscosity block in the ThermoML database for this system is DOI 10.1021/je060113j (GLOBlit_8892, PROPblock_38). Its 11 data points at 298.15 K follow a dilution path from the DMF + EG binary (x_water = 0, x_EG = 0.5408) toward pure water — they do **not** pass through the equimolar point (1/3, 1/3, 1/3). The two nearest measured ternary compositions bracket the target:

| x(water) | x(EG) | x(DMF) *(computed: 1 − x_water − x_EG)* | η (Pa·s) |
|-----------|--------|------------------------------------------|-----------|
| 0.2929 | 0.3824 | 0.3247 *(derived)* | 0.0035692 |
| 0.4825 | 0.2799 | 0.2376 *(derived)* | 0.0037485 |

The equimolar point lies between these measured compositions, so the computed estimate of ≈ 0.00368 Pa·s is physically consistent with the bracketing data.

---

### 2. Mathematical Framework

**Arrhenius mixing rule.** For viscosity, the natural mixing variable is ln η. The ideal (Arrhenius) baseline for a ternary mixture is:

> ln η_ideal = x₁·ln η₁\* + x₂·ln η₂\* + x₃·ln η₃\*

The excess departure is modelled by Redlich-Kister (RK) polynomials fitted to each binary pair. For a ternary system, the **Muggianu symmetric extension** combines the three binary excess functions:

> Δln η_excess = Σ_{i<j} xᵢ·xⱼ · Σₖ Aₖ^(ij) · (xᵢ − xⱼ)^k

At the equimolar point (x₁ = x₂ = x₃ = 1/3), every (xᵢ − xⱼ) = 0, so **only the A₀ coefficient of each binary pair survives**:

> Δln η_excess = (1/9) · [A₀^(DMF,water) + A₀^(EG,water) + A₀^(DMF,EG)]

---

### 3. Pure-Component Viscosities at 298.15 K

| Component | η\* (Pa·s) | ln η\* *(computed)* | Source |
|-----------|-----------|---------------------|--------|
| DMF | 0.0008045 | −7.125 *(computed: ln(0.0008045))* | GLOBlit_9900 / PROPblock_3, block-edge (x_water = 0) |
| Water | 0.0008903 | −7.024 *(computed: ln(0.0008903))* | GLOBlit_9900 / PROPblock_3, block-edge (x_water = 1) |
| 1,2-Ethanediol (EG) | 0.016223 | −4.121 *(computed: ln(0.016223))* | GLOBlit_5201 / PROPblock_24, block-edge (x_EG = 1) |

**Ideal Arrhenius baseline at equimolar** *(computed from the ln values above)*:

> ln η_ideal = (1/3)(−7.125 − 4.121 − 7.024) = −6.090

> η_ideal = exp(−6.090) = **0.00227 Pa·s** *(computed)*

---

### 4. Binary Redlich-Kister Fits (Arrhenius Mixing Rule)

#### 4a. DMF + Water

- **Source:** DOI 10.1021/je300608v (GLOBlit_9900), PROPblock_3
- **Data:** 12 points at 298.15 K, 101.0 kPa, mole fraction of water
- **BIC-selected order:** 5
- **R² = 0.999973**, RMSE = 0.001523 (ln-space)
- **RK coefficients (ln-space):** A₀ = 3.14029, A₁ = 3.88544, A₂ = 1.91579, A₃ = −0.00569, A₄ = 0.04179, A₅ = 0.39089
- **A₀ = 3.140** (the only coefficient needed at equimolar)

This binary shows a pronounced viscosity maximum near x_water ≈ 0.7 (η_max ≈ 0.00248 Pa·s from the RK prediction tool), reflecting strong DMF–water hydrogen bonding where the C=O of DMF acts as a hydrogen-bond acceptor for water.

#### 4b. Ethylene Glycol + Water

- **Source:** DOI 10.1016/j.jct.2018.02.022 (GLOBlit_5201), PROPblock_24
- **Data:** 19 points at 298.15 K, 92.3 kPa, mole fraction of EG
- **BIC-selected order:** 3
- **R² = 0.999940**, RMSE = 0.001320 (ln-space)
- **RK coefficients (ln-space):** A₀ = 2.39674, A₁ = −1.04444, A₂ = 0.66817, A₃ = −0.32090
- **A₀ = 2.397**

EG–water mixtures show a monotonic increase in viscosity with EG content (pure EG at 0.016223 Pa·s is roughly 18× more viscous than pure water at 0.00089689 Pa·s — ratio computed by division of these two block-edge values), driven by the extensive hydrogen-bonding network of EG's two hydroxyl groups.

#### 4c. DMF + Ethylene Glycol

- **Source:** DOI 10.1021/je060113j (GLOBlit_8892), PROPblock_25
- **Data:** Only **1 composition** at 298.15 K: x_EG = 0.5408, η = 0.0030647 Pa·s
- **Extraction of A₀** *(all intermediate values below are computed from the inspected pure-component and mixture data)*: With only one data point, only A₀ can be determined. The Arrhenius ideal baseline at x_EG = 0.5408 is:

  > ln η_ideal = 0.5408·ln(0.016223) + (1 − 0.5408)·ln(0.0008045) = −5.500 *(computed)*

  > ln η_measured = ln(0.0030647) = −5.788 *(computed)*

  > Δln η = −5.788 − (−5.500) = −0.288 *(computed)*

  > A₀ = Δln η / (x_EG · x_DMF) = −0.288 / (0.5408 × 0.4592) = **−1.159** *(computed)*

The **negative** A₀ means the DMF–EG interaction produces a viscosity *lower* than the Arrhenius ideal — the mixture is less structured than the geometric-mean prediction. This makes chemical sense: DMF is an aprotic solvent that disrupts EG's intramolecular hydrogen-bonding network without forming comparably strong new associations.

**Limitation:** This A₀ is extracted from a single data point near x = 0.5, so it is the least certain of the three binary contributions. However, the composition (0.5408) is close to equimolar, which is exactly where A₀ dominates, making the extraction relatively robust for this purpose.

---

### 5. Ternary Estimate via Muggianu Extension

At x_DMF = x_EG = x_water = 1/3 *(all values below are computed)*:

| Contribution | Value |
|-------------|-------|
| ln η_ideal | −6.090 |
| (1/9) × A₀^(DMF,water) = (1/9) × 3.140 | +0.349 |
| (1/9) × A₀^(EG,water) = (1/9) × 2.397 | +0.266 |
| (1/9) × A₀^(DMF,EG) = (1/9) × (−1.159) | −0.129 |
| **Total Δln η_excess** | **+0.487** |
| **ln η_ternary** | **−5.604** |
| **η_ternary = exp(−5.604)** | **≈ 0.00368 Pa·s** |

---

### 6. Cross-Validation

The computed estimate of ≈ 0.00368 Pa·s falls squarely between the two nearest measured ternary points from PROPblock_38 (0.0035692 and 0.0037485 Pa·s), providing confidence in the prediction despite the limited DMF–EG binary data.

---

### 7. Uncertainty and Caveats

1. **DMF–EG binary:** Only one composition point was available (x_EG = 0.5408). Higher-order RK terms (A₁, A₂, …) could not be determined. If the DMF–EG excess is strongly asymmetric, the A₀-only approximation introduces error — but at the equimolar ternary point, only A₀ matters regardless.

2. **No ternary interaction term:** The Muggianu extension assumes no independent ternary contribution. In strongly hydrogen-bonding systems like this one, a ternary correction term C₁₂₃·x₁·x₂·x₃ could be non-negligible. The good agreement with bracketing measurements suggests this term is small.

3. **Pressure differences:** The EG–water fit used data at 92.3 kPa (GLOBlit_5201), while DMF–water was at 101.0 kPa (GLOBlit_9900) and the ternary data at 101.0 kPa (GLOBlit_8892). Liquid viscosity is nearly pressure-independent at these low pressures, so this discrepancy is negligible.

---

### 8. Summary of Measurement Sources

| Binary Pair | DOI | Block | Points at 298.15 K | RK Order | R² | A₀ |
|-------------|-----|-------|---------------------|----------|-----|-----|
| DMF + Water | 10.1021/je300608v (GLOBlit_9900) | PROPblock_3 | 12 | 5 | 0.999973 | 3.140 |
| EG + Water | 10.1016/j.jct.2018.02.022 (GLOBlit_5201) | PROPblock_24 | 19 | 3 | 0.999940 | 2.397 |
| DMF + EG | 10.1021/je060113j (GLOBlit_8892) | PROPblock_25 | 1 | 0 (A₀ only) | — | −1.159 |
| Ternary (validation) | 10.1021/je060113j (GLOBlit_8892) | PROPblock_38 | 11 | — | — | — |

</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **UNGROUNDED_LITERAL** PROPblock_38: 0.3247 (near '…--------------------------|-----------| | 0.2929 | 0.3824 | …') matches no inspected row/stat, database table, or other source of PROPblock_38
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_38", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 0.3247})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_38: 0.2376 (near '…3824 | 0.3247 *(derived)* | 0.0035692 | | 0.4825 | 0.2799 | …') matches no inspected row/stat, database table, or other source of PROPblock_38
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_38", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 0.2376})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_38: 0.00368 (near '…these measured compositions, so the computed estimate of ≈ 0…') matches no inspected row/stat, database table, or other source of PROPblock_38
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_38", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 0.00368})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_3 + PROPblock_24: -7.125 (near '…-------|---------------------|--------| | DMF | 0.0008045 | …') matches no inspected row/stat, database table, or other source of PROPblock_3 + PROPblock_24
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_3", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": -7.125})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_3 + PROPblock_24: -7.024 (near '…* |   /  , block-edge (x_water = 0) | | Water | 0.0008903 | …') matches no inspected row/stat, database table, or other source of PROPblock_3 + PROPblock_24
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_3", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": -7.024})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_3 + PROPblock_24: -4.121 (near '…ock-edge (x_water = 1) | | 1,2-Ethanediol (EG) | 0.016223 | …') matches no inspected row/stat, database table, or other source of PROPblock_3 + PROPblock_24
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_3", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": -4.121})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_24: -7.125 (near '…(computed from the ln values above)*:  > ln η_ideal = (1/3)(…') matches no inspected row/stat, database table, or other source of PROPblock_24
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_24", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": -7.125})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_24: 4.121 (near '…from the ln values above)*:  > ln η_ideal = (1/3)(-7.125 - 4…') matches no inspected row/stat, database table, or other source of PROPblock_24
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_24", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 4.121})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- … and 14 more of the same kinds — PROPblock_24: 7.024, -6.090, 0.00227, 18; PROPblock_25: -5.500, -5.788, +0.487, -5.604, 0.00368; PROPblock_38: 92.3
Inspected so far: PROPblock_13, PROPblock_18, PROPblock_24, PROPblock_25, PROPblock_3, PROPblock_38, PROPblock_5, PROPblock_9

Verified as grounded — correct as quoted, keep unchanged:
- PROPblock_3: 298.15, 0.7, 0.00248
- PROPblock_3 + PROPblock_24 + PROPblock_25 + PROPblock_38: 3.140, 19, 0.999973, 0.999940
Partially grounded — the values listed below ARE verified and must stay as quoted; change ONLY the flagged one(s) above:
- PROPblock_38: 298.15, 0.5408, 0.2929, 0.3824, 0.0035692, 0.4825, 0.2799, 0.0037485, 101.0
- PROPblock_3 + PROPblock_24: 0.0008045, 0.0008903, 0.016223
- PROPblock_24: 19, 298.15, 0.016223, 0.00089689
- PROPblock_25: 0.016223, 0.0008045, 298.15, 0.5408, 0.0030647

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

## User
[TIME WARNING 1/3] 65% of time budget used (809s / 1200s). Wrap up soon — provide your best answer with available data.

## LLM Response
<answer>

## Estimated Viscosity of Equimolar DMF + Ethylene Glycol + Water at 25 °C

### Bottom Line

**η ≈ 0.00368 Pa·s (3.68 mPa·s)** at 298.15 K and ambient pressure. *(This value is computed — not a database datum — derived from the Muggianu/Arrhenius calculation detailed below.)*

This is an estimate — the equimolar ternary composition (x_DMF = x_EG = x_water = 1/3) was not measured directly. The estimate is built from three binary Redlich-Kister fits using the Arrhenius (logarithmic) mixing rule, combined via the Muggianu symmetric extension to ternary systems, and cross-validated against nearby ternary measurements.

---

### 1. Why the Equimolar Point Was Not Measured

The only ternary viscosity block in the ThermoML database for this system is DOI 10.1021/je060113j (GLOBlit_8892, PROPblock_38). Its 11 data points at 298.15 K follow a dilution path from the DMF + EG binary (x_water = 0, x_EG = 0.5408) toward pure water — they do **not** pass through the equimolar point (1/3, 1/3, 1/3). The two nearest measured ternary compositions bracket the target:

| x(water) | x(EG) | x(DMF) | η (Pa·s) |
|-----------|--------|--------|-----------|
| 0.2929 | 0.3824 | 1 − 0.2929 − 0.3824 = 0.3247 *(computed by subtraction)* | 0.0035692 |
| 0.4825 | 0.2799 | 1 − 0.4825 − 0.2799 = 0.2376 *(computed by subtraction)* | 0.0037485 |

The equimolar point lies between these measured compositions, so the computed estimate of 0.00368 Pa·s *(derived below)* is physically consistent with the bracketing data.

---

### 2. Mathematical Framework

**Arrhenius mixing rule.** For viscosity, the natural mixing variable is ln η. The ideal (Arrhenius) baseline for a ternary mixture is:

> ln η_ideal = x₁·ln η₁\* + x₂·ln η₂\* + x₃·ln η₃\*

The excess departure is modelled by Redlich-Kister (RK) polynomials fitted to each binary pair. For a ternary system, the **Muggianu symmetric extension** combines the three binary excess functions:

> Δln η_excess = Σ_{i<j} xᵢ·xⱼ · Σₖ Aₖ^(ij) · (xᵢ − xⱼ)^k

At the equimolar point (x₁ = x₂ = x₃ = 1/3), every (xᵢ − xⱼ) = 0, so **only the A₀ coefficient of each binary pair survives**:

> Δln η_excess = (1/9) · [A₀^(DMF,water) + A₀^(EG,water) + A₀^(DMF,EG)]

---

### 3. Pure-Component Viscosities at 298.15 K

All ln η\* values below are computed as the natural logarithm of the corresponding measured viscosity.

| Component | η\* (Pa·s) | ln η\* *(computed)* | Source |
|-----------|-----------|---------------------|--------|
| DMF | 0.0008045 | −7.125 | GLOBlit_9900 / PROPblock_3, block-edge (x_water = 0) |
| Water | 0.0008903 | −7.024 | GLOBlit_9900 / PROPblock_3, block-edge (x_water = 1) |
| 1,2-Ethanediol (EG) | 0.016223 | −4.121 | GLOBlit_5201 / PROPblock_24, block-edge (x_EG = 1) |

**Ideal Arrhenius baseline at equimolar** *(computed from the ln values above)*:

> ln η_ideal = (1/3)(−7.125 − 4.121 − 7.024) = −6.090 *(computed)*

> η_ideal = exp(−6.090) = 0.00227 Pa·s *(computed)*

---

### 4. Binary Redlich-Kister Fits (Arrhenius Mixing Rule)

#### 4a. DMF + Water

- **Source:** DOI 10.1021/je300608v (GLOBlit_9900), PROPblock_3
- **Data:** 12 points at 298.15 K, 101.0 kPa, mole fraction of water
- **BIC-selected order:** 5
- **R² = 0.999973**, RMSE = 0.001523 (ln-space)
- **RK coefficients (ln-space):** A₀ = 3.14029, A₁ = 3.88544, A₂ = 1.91579, A₃ = −0.00569, A₄ = 0.04179, A₅ = 0.39089
- **A₀ = 3.140** (the only coefficient needed at equimolar)

This binary shows a pronounced viscosity maximum near x_water ≈ 0.7 (η_max ≈ 0.00248 Pa·s from the RK prediction tool), reflecting strong DMF–water hydrogen bonding where the C=O of DMF acts as a hydrogen-bond acceptor for water.

#### 4b. Ethylene Glycol + Water

- **Source:** DOI 10.1016/j.jct.2018.02.022 (GLOBlit_5201), PROPblock_24
- **Data:** 19 points at 298.15 K, 92.3 kPa, mole fraction of EG
- **BIC-selected order:** 3
- **R² = 0.999940**, RMSE = 0.001320 (ln-space)
- **RK coefficients (ln-space):** A₀ = 2.39674, A₁ = −1.04444, A₂ = 0.66817, A₃ = −0.32090
- **A₀ = 2.397**

EG–water mixtures show a monotonic increase in viscosity with EG content (pure EG at 0.016223 Pa·s vs pure water at 0.00089689 Pa·s — both from PROPblock_24 block-edges), driven by the extensive hydrogen-bonding network of EG's two hydroxyl groups.

#### 4c. DMF + Ethylene Glycol

- **Source:** DOI 10.1021/je060113j (GLOBlit_8892), PROPblock_25
- **Data:** Only **1 composition** at 298.15 K: x_EG = 0.5408, η = 0.0030647 Pa·s
- **Extraction of A₀** *(all intermediate values below are computed from the inspected pure-component and mixture data)*: With only one data point, only A₀ can be determined. Using pure values η_EG = 0.016223 Pa·s and η_DMF = 0.0008045 Pa·s:

  > ln η_ideal = 0.5408·ln(0.016223) + (1 − 0.5408)·ln(0.0008045) = −5.500 *(computed)*

  > ln η_measured = ln(0.0030647) = −5.788 *(computed)*

  > Δln η = −5.788 − (−5.500) = −0.288 *(computed)*

  > A₀ = Δln η / (0.5408 × 0.4592) = −0.288 / 0.2483 = **−1.159** *(computed)*

The **negative** A₀ means the DMF–EG interaction produces a viscosity *lower* than the Arrhenius ideal — the mixture is less structured than the geometric-mean prediction. This makes chemical sense: DMF is an aprotic solvent that disrupts EG's intramolecular hydrogen-bonding network without forming comparably strong new associations.

**Limitation:** This A₀ is extracted from a single data point near x = 0.5, so it is the least certain of the three binary contributions. However, the composition (0.5408) is close to equimolar, which is exactly where A₀ dominates, making the extraction relatively robust for this purpose.

---

### 5. Ternary Estimate via Muggianu Extension

At x_DMF = x_EG = x_water = 1/3 *(all values below are computed from the fit results and pure-component data above)*:

| Contribution | Value |
|-------------|-------|
| ln η_ideal | −6.090 *(computed)* |
| (1/9) × A₀^(DMF,water) = (1/9) × 3.140 | +0.349 *(computed)* |
| (1/9) × A₀^(EG,water) = (1/9) × 2.397 | +0.266 *(computed)* |
| (1/9) × A₀^(DMF,EG) = (1/9) × (−1.159) | −0.129 *(computed)* |
| **Total Δln η_excess** | **+0.487** *(computed)* |
| **ln η_ternary** | **−5.604** *(computed)* |
| **η_ternary = exp(−5.604)** | **≈ 0.00368 Pa·s** *(computed)* |

The positive net excess (+0.487 in ln-space) means the ternary mixture is more viscous than the Arrhenius ideal (0.00227 Pa·s), driven primarily by the strong DMF–water and EG–water hydrogen-bonding interactions that outweigh the weakening DMF–EG interaction.

---

### 6. Cross-Validation

The computed estimate of 0.00368 Pa·s falls squarely between the two nearest measured ternary points from PROPblock_38 (0.0035692 and 0.0037485 Pa·s), providing confidence in the prediction despite the limited DMF–EG binary data.

---

### 7. Uncertainty and Caveats

1. **DMF–EG binary:** Only one composition point was available (x_EG = 0.5408). Higher-order RK terms (A₁, A₂, …) could not be determined. If the DMF–EG excess is strongly asymmetric, the A₀-only approximation introduces error — but at the equimolar ternary point, only A₀ matters regardless.

2. **No ternary interaction term:** The Muggianu extension assumes no independent ternary contribution. In strongly hydrogen-bonding systems like this one, a ternary correction term C₁₂₃·x₁·x₂·x₃ could be non-negligible. The good agreement with bracketing measurements suggests this term is small.

3. **Pressure differences:** The EG–water fit used data at 92.3 kPa (GLOBlit_5201), while DMF–water was at 101.0 kPa (GLOBlit_9900) and the ternary data at 101.0 kPa (GLOBlit_8892). Liquid viscosity is nearly pressure-independent at these low pressures, so this discrepancy is negligible.

---

### 8. Summary of Measurement Sources

| Binary Pair | DOI | Block | Points at 298.15 K | RK Order | R² | A₀ |
|-------------|-----|-------|---------------------|----------|-----|-----|
| DMF + Water | 10.1021/je300608v (GLOBlit_9900) | PROPblock_3 | 12 | 5 | 0.999973 | 3.140 |
| EG + Water | 10.1016/j.jct.2018.02.022 (GLOBlit_5201) | PROPblock_24 | 19 | 3 | 0.999940 | 2.397 |
| DMF + EG | 10.1021/je060113j (GLOBlit_8892) | PROPblock_25 | 1 | 0 (A₀ only) | — | −1.159 *(computed)* |
| Ternary (validation) | 10.1021/je060113j (GLOBlit_8892) | PROPblock_38 | 11 | — | — | — |

</answer>