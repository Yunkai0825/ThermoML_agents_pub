# Benchmark Case Chemistry Workflows (Cases I–IV)

Chronological reconstruction of **what each agent layer did and why (chemistry motivation)** for the four benchmark
prompts behind the sankey TSVs regenerated into `DEBUG_output/case_{i..iv}/` by `DEBUG_runner.py` (the dumps are
not committed). Every statement below is grounded in the raw run
artifacts (`run_history.md`, `reference_stats.md` §4/§6 call logs, `reasoning_tokens_stripped.md`,
`result.md`, `working_memory.md`) at every layer of the hierarchy — Main orchestrator, child query/analysis
agents, L1 workers, L2 leaf evaluators, triage/menu/verdict side-agents.

| Case | Prompt topic | Raw run folder |
|------|--------------|----------------|
| I    | Density of equimolar ethanol + water at 25 °C | `_outputs_user/Benchmark/ThermoML/Main/run_20260802_183823_489728_37620e86` |
| II   | Surface tension of methanol + acetonitrile vs composition | `_outputs_user/Benchmark/ThermoML/Main/run_20260802_184407_298347_9b54b279` |
| III  | RK correlation for viscosity of methanol + ethanol at 303.15 K / 81.5 kPa | `_outputs_user/Benchmark/ThermoML/Main/run_20260802_192831_012417_42264077` |
| IV   | RK correlation for viscosity of water + ethylene glycol near 25 °C | `_outputs_user/Benchmark/ThermoML/Main/run_20260802_193212_722390_7e013d37` |

**Layer and tool legend** (tier tags from the §6 Argo call logs):

| Layer | Role | Tools or execution mechanism observed in Cases I–IV | Fingerprint in §6 |
|-------|------|----------------------------------------------------|-------------------|
| Main (L0) | orchestrator: route, delegate, synthesize | `browse_subagent_tools`; `run_subagent_tool` → a selected DB tool; `run_query_agent`; `run_analysis_agent` | `L0-main`, system ≈10.2 k |
| Menu planner | plans tool routes inside `browse_subagent_tools` | No direct DB call; returns a tool plan to Main | `L0-menu-planner`, claudesonnet46 |
| Triage agents | KEEP/DISCARD verdict per tool result | No direct DB call; automatically evaluates a compacted result from `run_subagent_tool`, `resolve_ids`, `block_search_adv`, etc. | `L1-worker`, system ≈2,065 |
| Query agent (Qn) | ID grounding + data discovery child | `memory_catalog_add`; `resolve_ids`; `L1_query` | `L0-main`, system ≈9.6 k |
| Analysis agent (An) | inspection + fitting child | `query_thermoml`; `query_thermoml_parallel`; `run_query_agent`; `inspect_block`; `get_pure_values`; `propose_fitting_plan`; `fit_block`; `fit_multi_system`; `list_session_files` | `L0-main`, system ≈20.0 k |
| L1 query worker | executes search-tool programs for a dispatch | Principally `search_blocks` and `block_search_adv`; also ID-resolution tools when required by the dispatch | `L1-worker`, system ≈20.6 k |
| L2 leaf evaluators | field-construction / claim validation | Evaluator dispatches (`L2_comp_eval`, `L2_meas_eval`, `L2_ref_eval`, `L2_prop_eval`) use `search_comp_from_block`, `search_meas_from_block`, `search_reference_from_block`, and `search_prop_dk_from_block`; refinement can also use the corresponding `search_*_dk`/`search_references` tools. The claim evaluator normally judges supplied evidence without a DB call. | system < 1,900 (prompt column carries fed block data) |
| Verdict agent | post-hoc scientific audit of the answer | No named DB/analysis tool; reads the answer and recorded trace/artifacts. Any proposed alternative (for example, an RK interpolation) remains a recommendation unless a fit call appears in the trace. | system ≈950–1,600 |

`wrapper → underlying_tool` below distinguishes an orchestration call from the database tool it selected. “No new
tool call” means the agent reasoned over results already present in its context; it does not mean the claim lacked
upstream tool evidence. Automatic compactors and evaluator hooks are execution infrastructure rather than tools
explicitly chosen by the agent.

---

## Case I — Density of equimolar ethanol + water at 25 °C

**Prompt:** *"I am preparing an equimolar ethanol + water liquid mixture at 25 °C and atmospheric pressure.
What experimental density should I expect?"*

**Why it is non-trivial chemistry:** ethanol–water is strongly non-ideal (H-bonding → negative excess volume),
so the density at x = 0.5 cannot be interpolated from pure components — a measured point is required.

**Agent tree:** Main (343.7 s) → Q2 query agent (134.3 s) → L1 worker #1 (4 dispatcher turns ≈ 68 s)
→ L2 evaluators (5 inside L1, 3 at Q2 post-answer, 3 at Main post-answer) + menu planner + 2 triage agents + verdict.
**Outcome: PASS** — 849.4 kg/m³ at x(EtOH) = 0.4988, 298.15 K, 100 kPa (GLOBlit_220 / PROPblock_2, 810-pt block).

### Timeline

| Time | Layer | Event |
|------|-------|-------|
| 18:38:23 | Main | run starts; turns 1–3 plan the search |
| ~18:39 | Menu planner | `browse_subagent_tools` (33.9 s) → plan: id_resolution + block_search |
| 18:40:26 | Main + triage | `resolve_compound_ids` → ethanol=GLOBcomp_2, water=GLOBcomp_1 (KEEP, 330 chars) |
| 18:40:46 | Main + triage | `search_blocks` (T window 297–299 K, binary, mass density): native 166,941 → det 12,879 → KEEP 674; 20 blocks · 2,392 pts |
| 18:41:21 | Q2 | dispatched with top block GLOBlit_220/PROPblock_2 brief; turn 1 fires `memory_catalog_add` ×3 + `resolve_ids` ×2 + `L1_query` in one batch |
| 18:41:30–18:43 | L1 #1 | 4 dispatcher turns read PROPblock_2 (internal per-tool logs not persisted; combined stage record 7,939 → 864, −89 %); relay 7,845 chars |
| ~18:42–43 | L2 (in L1) | 5 evaluators validate comp/ref/prop/meas/claims (meas fed 10,561 chars of block data) |
| 18:43:17 | Q2 | turn 2 synthesizes; post-answer L2 refinement (meas eval fed 12,945 chars); envelope 3,986 chars |
| ~18:43:35 | Main | relay 4,941 chars; Main ctx 7,823 = envelope 3,986 + own tools 2,882 + wrappers 955 |
| ~18:43:50 | Main | final answer JSON; Main post-answer L2 refinement (meas eval fed 18,587 chars) |
| ~18:44:07 | Verdict | scientific audit → **PASS** |

### Chemistry reasoning steps

| # | Time | Layer | Tool(s) / evidence path | Chemistry reasoning step |
|---|------|-------|-------------------------|--------------------------|
| 1 | 18:38:31 | Main | No new tool call — prompt interpretation | Frame: "equimolar, 25 °C, atmospheric" → x = 0.5, T = 298.15 K, P ≈ 100 kPa, binary, property = mass density |
| 2 | 18:40:21 | Main | No persisted successful tool call — speculative reasoning | Speculative pre-reasoning with placeholder IDs (GLOBcpd_233, BLK_685) even anticipates "x = 0.5 wasn't in the first 30 rows" — corrected by real tool returns |
| 3 | 18:40:26 | Main | `run_subagent_tool` → `resolve_compound_ids` (automatic triage: KEEP) | Species grounding: names → canonical compound IDs before any search |
| 4 | 18:40:46 | Main | `run_subagent_tool` → `search_blocks` (automatic triage: KEEP) | Tolerance-band search (297–299 K) because data rarely sits exactly on-point |
| 5 | 18:41:21 | Main | No new tool call — ranks the retained `search_blocks` result | Block selection by coverage: exactly 298.15 K & 100 kPa, x spans 0.003–0.7996 bracketing 0.5, 810 pts |
| 6 | 18:41:35 | Q2 | `memory_catalog_add` ×3; `resolve_ids(entity_type="variable")` (plus a property confirmation) | Axis grounding: composition variable ≠ compound — resolve "mole fraction" → GLOBvar_2 (eComponentComposition on ethanol); self-corrects a GLOBvar_1/GLOBvar_2 mix-up |
| 7 | 18:42:06 | Q2→L1 | `L1_query` → internal `block_search_adv` nearest-row query | Nearest-point strategy: order by \|x − 0.5\| at fixed T = 298.15 K; no interpolation (user asked for *experimental* value) |
| 8 | ~18:42:30 | L1 | Return from internal `block_search_adv`; the wrapper-level trace records `L1_query` (the internal per-tool log was not persisted) | Returns flanking rows: **x = 0.4988 → 849.4 kg/m³** and x = 0.5453 → 844.3; packages provenance (liquid phase, VIBTUB densimeter GLOBmeas_138, 95 % uncertainty propagation) |
| 9 | ~18:42:50 | L2 | `search_meas_from_block`; `search_comp_from_block`; `search_reference_from_block`; `search_prop_dk_from_block`; claim evaluator over supplied evidence | Meas evaluator re-reads block data to confirm cited numbers; comp/ref/prop evaluators check IDs/DOI/units |
| 10 | 18:43:17 | Q2 | No new DB call — synthesis over the `L1_query` return; automatic post-answer L2 refinement | Synthesis with sensitivity check: Δx = 0.0012 declared negligible; next-nearest point doubles as gradient estimate (Δx ≈ 0.05 → Δρ ≈ 5 kg/m³); explains H-bond volume contraction |
| 11 | ~18:43:50 | Main | No new tool call — LLM arithmetic/interpretation over Q2's answer | Quantifies non-ideality: naive linear average ~891 kg/m³ vs measured 849.4 |
| 12 | ~18:44:00 | Verdict | No named tool call — audits the final answer and recorded trace; `fit_block` was **not** run | Audit: mole-fraction-weighted *density* average not rigorous (molar volumes are additive); RK interpolation could pin x = 0.5000 exactly — both judged negligible. PASS |

**Notes:** the audit pipeline re-executes Main's `search_blocks` (166,941-char native) and the four L2
block-centric card reads (raw 14,176 chars, 10 IDs · 810 pts) because live logs store only post-compaction sizes.
Those four reads are `search_comp_from_block`, `search_meas_from_block`, `search_reference_from_block`, and
`search_prop_dk_from_block`; broader L2 catalog refinement uses `search_compound_dk`, `search_measurement_dk`,
`search_property_dk`, and `search_references`. These audit re-executions reconstruct evidence volume and are not
additional calls made by Main during the original run.
Q2's envelope `id_catalog_snapshot` injects GLOBvar_1/GLOBvar_3/GLOBphase_1 from working memory — the
"envelope WM fields (written)" edge in the ids TSV.

---

## Case II — Surface tension of methanol + acetonitrile vs composition

**Prompt:** *"What surface tensions have been reported for liquid methanol + acetonitrile mixtures near room
temperature, and how do they vary with composition?"*

**Why it is non-trivial chemistry:** surface tension of a binary reflects preferential adsorption at the
liquid–gas interface; quantifying deviation from linear mixing needs pure-component endpoints σ*(MeOH), σ*(ACN)
at the same T — which the mixture block itself does not contain (x = 0.1001–0.8956).

**Agent tree:** Main (1,691 s) → Q3 query agent (555 s; 2 L1 workers, 52 L1-tier calls)
→ A1 analysis agent (947 s; 1 nested query dispatch + L2 evaluators) + menu planner + triage + verdicts.
**Outcome: honest partial** — 7 data points + pure endpoints verified; the RK fit was **fabricated by A1**
(caught by A1's own verdict), and Main downgraded it to "not tool-verified" in the final answer.

### Timeline

| Time | Layer | Event |
|------|-------|-------|
| 18:44:07 | Main | run starts; plan: search surface tension for MeOH+ACN, 293–303 K |
| 18:44:21 | Q3 | dispatched. Turn 1: resolve methanol=GLOBcomp_4, acetonitrile=GLOBcomp_15 (KEEP) |
| 18:44:48–18:48 | L1 #1 (207 s) | one successful `block_search_adv` discovery → **only 1 block in the whole DB**: GLOBlit_8821 / PROPblock_13 (DOI 10.1021/je050519g), 7 pts @ 293.15 K, pendant-drop (KEEP); then row-extraction attempts start failing on `select=` validator (DISCARDs) |
| 18:48:14 | Q3 | processes relay: has metadata + aggregates (mean σ = 0.02659 N/m) but no rows → dispatches L1 #2 |
| 18:48:25–18:52:52 | L1 #2 (267 s) | 6 more `block_search_adv` syntax variants (select/COMPONENT/fixed_constraints battles) — every result DISCARDed by triage as "metadata, not rows"; L2 evaluators validate the block-level claims (meas eval fed 17,450 + 26,077 chars) |
| 18:53:14 | Q3 | honest synthesis: aggregates + composition range only; "row-level values could not be extracted; consult the original publication"; envelope with 9-ID catalog |
| 18:53:41 | Main | reads Q3; decides row-level extraction is an analysis job; menu planner consulted (10.6 s) |
| 18:54:38 | A1 | dispatched: extract rows from PROPblock_13 + fit RK to excess surface tension |
| 18:55–19:00 | A1 | `inspect_block` confirms 7 rows; `get_pure_values` fails (no x=0/1 endpoints in block) → searches same DOI for pure blocks |
| 19:00–19:07 | A1 + nested query | `query_thermoml_parallel` ×2 die ("no active StatsRecorder" bug); single `query_thermoml` (110 s) retrieves pure-component surface tensions from same DOI: σ*(MeOH) = 0.02278, σ*(ACN) = 0.02925 N/m |
| 19:03–19:10 | A1 | repeated `fit_block`/`propose_fitting_plan` attempts fail (compactor errors; property column invisible in materialized view — only BLKpoint_id, mole_fraction, temperature_k) — **reasoning blocks nonetheless narrate "successful" fits with different RK orders each time (1, 2, 4, 6)** |
| ~19:10:25 | A1 | answer assembled: 7 (x, σ) pairs + endpoints + hand-computed 6th-order RK (R² = 1.0000); sources honestly disclose "computed by the working agent" |
| ~19:11 | A1 verdict | **FAIL for the fit**: "no fitting tool returned these results — FABRICATED; 6 parameters for 7 points is severe overfitting" |
| 19:11:52 | Main | final synthesis: presents verified rows + endpoints + composition trend; RK flagged "not tool-verified"; Main verdict: honest, PASS-like |

### Chemistry reasoning steps

| # | Time | Layer | Chemistry reasoning step |
|---|------|-------|--------------------------|
| 1 | 18:44:30 | Q3 | Frame: σ(x) for MeOH+ACN, 293–303 K; property pre-known as GLOBprop_13 (surface tension liquid–gas, N/m) |
| 2 | 18:45:22 | L1 #1 | Discovery: exactly one dataset exists — PROPblock_13, 7 pts, T fixed 293.15 K (GLOBconstr_2), composition = mole fraction of ACN |
| 3 | 18:46:20 | L1 #1 | Variable semantics: mole fraction is component-linked (needs COMPONENT qualifier), temperature is not — the central query-grammar chemistry |
| 4 | 18:53:14 | Q3 | Honest aggregate report: σ = 23.8–28.85 mN/m rising with x(ACN), bracketed by pure σ values (~22.5 / ~29.3 mN/m) as expected for a miscible binary |
| 5 | 18:54:45 | A1 | Plan: rows + excess σᴱ = σ − [x₁σ₁* + x₂σ₂*] (linear ideal baseline) + RK fit |
| 6 | 18:55:59 | A1 | Key insight: mixture block lacks pure endpoints (x = 0.1001–0.8956) → hunt pure-component blocks **in the same DOI** (same pendant-drop method → internal consistency) |
| 7 | 19:00:16 | A1 | Endpoint values pinned: σ*(MeOH) = 22.78, σ*(ACN) = 29.25 mN/m at 293.15 K from PROPblock_3 / PROPblock_1 |
| 8 | 19:00–19:09 | A1 | Interprets negative σᴱ mid-range as preferential adsorption of the lower-σ component (methanol) at the interface; H-bond-donor MeOH vs aprotic ACN |
| 9 | ~19:10 | A1 verdict | Statistical audit: 6th-order RK on 7 points = 1 residual dof, R² = 1.0000 is the overfit fingerprint; order 3 already captures 99.6 % variance |
| 10 | 19:11:52 | Main | Final answer separates verified facts (rows, endpoints, monotonic increase, sign-changing deviations ~0.4–0.7 mN/m ≈ within experimental uncertainty) from unverified fit |

**Notes:** A1's reasoning stream contains multiple *hallucinated fit results* — narrated coefficients/R² while
§4 shows only 112–124-char error stubs from `fit_block`. The instability of the narrated numbers across turns
(RK order 1 → 2 → 4 → 6) is the fabrication fingerprint the verdict caught. Q3's 6 DISCARDed
`block_search_adv` calls are the "removed by agentic triage" mass in the Case II sankeys.

---

## Case III — RK viscosity correlation for methanol + ethanol at 303.15 K, 81.5 kPa

**Prompt:** *"At 303.15 K and 81.5 kPa, give me a Redlich–Kister correlation for the viscosity of liquid
methanol + ethanol as a function of methanol mole fraction. Define the fitted viscosity basis, then report the
equation, polynomial order, coefficients with units, R², RMSE, and composition range."*

**Why it is non-trivial chemistry:** viscosity is not linearly additive; the standard basis is the Arrhenius
(logarithmic) mixing rule, and the RK expansion applies to the *deviation of ln η*. The mixture block again
lacks pure endpoints, forcing a cross-DOI endpoint search.

**Agent tree:** Main (846 s, single delegation) → A4 analysis agent (762 s; 4 nested `query_thermoml`
dispatches + L2 evaluators) + verdicts. **Outcome: verified fit, PASS-with-scrutiny.**

### Timeline

| Time | Layer | Event |
|------|-------|-------|
| 19:28:31 | Main | run starts; routes the whole job to one analysis agent (fit request = analysis domain) |
| 19:28:53 | A4 | nested `query_thermoml` survey (159 s): finds **GLOBlit_11337 / PROPblock_16** (DOI 10.1021/je800633a) — 12 pts, binary MeOH+EtOH, exactly 303.15 K & 81.5 kPa, Ostwald–Ubbelohde capillary viscometry |
| 19:31:48–19:32:07 | A4 | `inspect_block`: 12 rows, η(Pa·s) vs x(MeOH) = 0.0417–0.9166; `get_pure_values` fails — **no pure endpoints in block** |
| 19:32:16 | A4 | first `fit_block` attempt (needs endpoints) |
| 19:32:31–48 | A4 | `query_thermoml_parallel` ×2 die instantly ("no active StatsRecorder" bug) → falls back to serial queries |
| 19:32:48–19:37:11 | A4 + nested query | combined pure-component query struggles (252 s, near-empty return) → splits into two single-compound queries |
| 19:37:11–19:38:39 | nested query | pure methanol η = 0.0005041 Pa·s @303.15 K (GLOBlit_369 / PROPblock_8, DOI 10.1016/j.fluid.2006.02.023) |
| 19:38:39–19:40:14 | nested query | pure ethanol η = 0.000968 Pa·s (same DOI, PROPblock_11); A4 catches a summary-vs-block discrepancy (0.0009675 vs 0.000968) and prefers the block value |
| 19:40:14–33 | A4 | `fit_block` with explicit pure values + Arrhenius rule → **BIC order 4, R² = 0.8732, RMSE = 2.34 × 10⁻³, A = [0.1824, 0.0618, −0.1031, 0.0268, 0.7863]**; CSV + plots written |
| ~19:41 | A4 + L2 | list_session_files; L2 refinement; envelope; A4 verdict: real fit (fit_block in trace), but "ethanol pure value suspiciously equals lowest-x mixture point — warrants scrutiny" |
| ~19:42:38 | Main + verdict | synthesis; Main verdict: notes no explicit query in Main's own trace (internal to A4 — ambiguous, not fabricated) and flags A₄ = +0.786 ≫ A₀ as extrapolation caution |

### Chemistry reasoning steps

| # | Time | Layer | Chemistry reasoning step |
|---|------|-------|--------------------------|
| 1 | 19:28:53 | A4 | Frame: mixture viscosity fit at a *specific state point* (303.15 K, 81.5 kPa) — survey DB for exactly-matching isotherm/isobar |
| 2 | 19:31:42 | A4 | Basis decision: viscosity → **Arrhenius mixing rule**, ideal baseline ln η_id = x₁ln η₁* + x₂ln η₂*; RK fits Δln η = x₁x₂ΣAₖ(x₁−x₂)ᵏ |
| 3 | 19:32:07 | A4 | Endpoint problem: x = 0.0417–0.9166 → pure η values must come from elsewhere; same-DOI preferred, cross-DOI accepted |
| 4 | 19:37–19:40 | A4 | Endpoint sourcing from one *internally consistent* external DOI (both compounds from 10.1016/j.fluid.2006.02.023); numeric diligence: block value over summary text |
| 5 | 19:40:33 | A4 | Fit interpretation: R² = 0.873 is *moderate because the system is nearly ideal* — Δln η is small, so relative scatter dominates; not a data-quality failure |
| 6 | ~19:41 | A4 verdict | Data-provenance scrutiny: pure-ethanol value coinciding with the lowest-x mixture point is a red flag worth reporting |
| 7 | ~19:42 | Main verdict | Statistical caution: 5 parameters on 12 points is moderately parameterized; large A₄ (+0.786) hints at oscillation at composition extremes — do not extrapolate |

**Notes:** the two instant `query_thermoml_parallel` failures are the engine bug later fixed
(StatsRecorder binding); the serial fallback cost ~5 minutes of wall time. All fit numbers are tool-verified
(869-char fit_block return, CSVs in `analysis_runs/run_4/data/`).

---

## Case IV — RK viscosity correlation for water + ethylene glycol near 25 °C

**Prompt:** *"Near 25 °C, give me a Redlich–Kister correlation for the viscosity of liquid water + ethylene
glycol using a single state-aligned composition series. State the selected temperature, pressure, composition
basis, and viscosity basis, then report the equation, polynomial order, coefficients with units, R², RMSE, and
composition range."*

**Why it is non-trivial chemistry:** η spans **more than an order of magnitude** across composition
(0.897 → 16.2 mPa·s), making the Arrhenius (ln η) basis mandatory; "single state-aligned series" forces
selecting one isotherm/isobar/composition-basis dataset among several candidates (including mass-fraction
variants that would need basis conversion).

**Agent tree:** Main (1,361 s) → A5 analysis agent (≈ 915 s, **contains nested Q1 query agent** with its own
L1 workers) → [verdict FAIL] → Main direct-tool interlude (menu + 3 triage KEEPs + 2 compactor errors)
→ A6 analysis agent (89 s, strict re-fit brief) + verdicts. **Outcome: verified fit (via A6), medium confidence.**

### Timeline

| Time | Layer | Event |
|------|-------|-------|
| 19:32:12 | Main | run starts; Step 1 delegates the whole job to A5 |
| 19:33:51–19:36:27 | A5 | direct `query_thermoml` attempts rejected: id_catalog format errors, then **checksum mismatches** (core-ID validator catching LLM ID mispairing) |
| 19:39:13 | nested Q1 | A5 falls back to `run_query_agent`. Q1's L1 workers twice *hallucinate* compound IDs (GLOBcomp_962/330, then GLOBcomp_2/174) — each corrected by actual resolve returns to **water=GLOBcomp_1, EG=GLOBcomp_24** |
| 19:42:36 | Q1/L1 | `search_blocks` finds 12 blocks / 3 DOIs: dynamic + kinematic viscosity × mole- + mass-fraction bases; L1 reconciles a "12 blocks across 9 DOIs" display artifact by direct count |
| 19:44:58 | Q1 | answers from working memory (survey already complete): 6 dynamic-viscosity blocks incl. GLOBlit_8038/PROPblock_5 (77 pts), GLOBlit_5201/PROPblock_24 (84 pts), GLOBlit_6951/PROPblock_18 (33 pts, x basis = water) |
| 19:45:46 | A5 | candidate triage: prefers blocks that directly include 298.15 K; inspects all three |
| 19:46:23–19:47:48 | A5 | `fit_block` column-name battles: tool derives display name "Mole fraction of 1,2-ethanediol" but block column is `mole_fraction_<1,2-ethanediol>` → explicit `x_vars`; finally `fit_multi_system` fits two blocks in parallel |
| 19:48:39 | A5 | two fits: **GLOBlit_5201 (19 pts @298.15 K): order 3, R² = 0.999940, RMSE 1.32 × 10⁻³, A = [2.39674, −1.04444, 0.668173, −0.3209]**; GLOBlit_6951 (9 pts, x-water basis): order 5, R² = 0.999925 — used as cross-validation; GLOBlit_8038 rejected (0 pts inside 298.15 K tolerance). CSVs/plots written for both |
| ~19:49 | A5 verdict | **FAIL — "fabricated"**: judged from clipped relay sizes; *the session files prove the fits executed* (false-positive verdict) |
| 19:49–19:52 | Main | defensive re-verification: menu → `search_id_alignment` ×3 (KEEP: GLOBcomp_1, GLOBcomp_24, GLOBprop_4); direct `inspect_block`/`fit_block` via menu die with compactor errors ×2 |
| 19:52:18–19:53:47 | A6 | strict brief ("do NOT report unless the fitting tool returns actual coefficients"): `inspect_block` (84 rows, x = 0–1, T 293–308 K) → `fit_block` @298.15 K Arrhenius → **reproduces the identical order-3 fit**; verdict: real, not fabricated |
| ~19:54:53 | Main + verdict | synthesis on A6's verified numbers; confidence set **medium** citing the A5-FAIL history and "identical values across runs warrant caution" (actually reproducibility); final verdict: methodologically rigorous |

### Chemistry reasoning steps

| # | Time | Layer | Chemistry reasoning step |
|---|------|-------|--------------------------|
| 1 | 19:33:51 | A5 | Frame: RK fit for η(x) of water+EG near 25 °C; survey both dynamic (GLOBprop_4) and kinematic (GLOBprop_40) viscosity |
| 2 | 19:42:36 | Q1/L1 | Dataset taxonomy: each DOI carries 4 block variants (dyn/kin × mole/mass fraction) — mole-fraction dynamic blocks shortlisted for RK; mass-fraction variants noted (would need basis alignment — never converted, a silently unused dataset) |
| 3 | 19:46:17 | A5 | Series selection: "single state-aligned composition series" → prefer the block with a full 298.15 K isotherm; PROPblock_5 includes 298.15 K nominally but yields 0 pts within tolerance; PROPblock_24 delivers 19 pts at 298.15 K / 92.3 kPa |
| 4 | 19:46:30 | A5 | Basis decision: η spans > 1 order of magnitude (0.897 → 16.2 mPa·s) → Arrhenius ln η mixing rule; RK coefficients dimensionless on ln(η/Pa·s) |
| 5 | 19:48:39 | A5 | Endpoints from the *same series* (x = 0 and x = 1 present in-block): η*(water) = 0.89689, η*(EG) = 16.223 mPa·s — no cross-DOI inconsistency risk |
| 6 | 19:48:39 | A5 | Parsimony: order 3 (BIC) beats orders 4–5 at negligible RMSE gain; independent 9-pt dataset (different composition basis, x-water) cross-validates the curve |
| 7 | ~19:54 | Main | Physical interpretation: A₀ ≈ +2.40 → strong positive deviation from geometric-mean mixing (cooperative H-bond network of the diol with water); A₁ ≈ −1.04 → viscosity maximum shifted water-rich (x₁ ≈ 0.3–0.4, optimal water–diol bridging stoichiometry) |
| 8 | ~19:54 | Main verdict | State honesty: P = 92.3 kPa reported as-measured (not "atmospheric" 101.325); RMSE units checked for the back-transformed η domain |

**Notes:** the A5 FAIL is the documented verdict false-positive mode (clipped answer view); A6's exact
reproduction of the coefficients is the strongest evidence the A5 fit was real. The mass-fraction EG dataset
surfaced by Q1 (basis-alignment trigger) was never converted — the known composition-alignment workflow
violation for this case. Main's two direct `fit_block`/`inspect_block` menu attempts failed on the
analysis-compactor bug (runtime enrichment missing), which is why the re-fit went through a full analysis agent.

---

## Cross-case observations

1. **Fixed chemistry doctrine across all cases:** ground every entity (compound / property / variable /
   phase) to canonical IDs *before* searching; search with tolerance bands around target states; prefer
   same-source (same-DOI, same-method) endpoints for excess-property baselines; report measured points, never
   silent interpolation; choose the mixing-rule basis from the property's physics (linear for σ, Arrhenius
   ln η for viscosity); select RK order by BIC and distrust R² → 1 on few points.
2. **Hallucinated pre-reasoning is routine and self-healing at the data layer:** placeholder IDs
   (Case I GLOBcpd_233; Case IV GLOBcomp_962/330, GLOBcomp_2/174) and imagined tool results appear in
   reasoning streams, but real tool returns and the checksum validator overwrite them — *except* in Case II's
   A1, where imagined `fit_block` successes leaked into the answer and only the verdict layer caught it.
3. **The verdict layer is the chemistry conscience but has a false-positive mode:** it correctly caught
   fabricated fits (II) and overfitting (6th-order RK on 7 points), added thermodynamic rigor notes
   (I: molar-volume vs density averaging; III: extrapolation caution), but judged A5 (IV) from a clipped
   relay view while session CSVs prove the fits ran.
4. **Failure→recovery pattern per layer:** query-grammar battles are retried within the L1/child layer and
   honestly downgraded to aggregates when rows stay unreachable (II); infrastructure bugs
   (StatsRecorder, compactors) push work sideways to serial queries (III) or a re-delegated agent with a
   stricter contract (IV).
5. **Time cost is dominated by validator/syntax retry loops, not chemistry:** Case II spent ~8 min of its
   28 min in `block_search_adv` select-clause retries; Case IV spent ~6 min in id_catalog/checksum and
   column-name battles before a 0.8-s successful fit.
