"""
Shared agentic subagent — tool-level ReAct KEEP/DISCARD compaction.
====================================================================
Parametrised implementation used by **both** the query agent and the
analysis agent.  Each provides its own ``client_factory`` (lazy LLM
client) and ``cfg`` (AGENT_CONFIG with SUBAGENT_* fields).

The subagent receives:
  - compact markdown produced by hardcoded compactors
  - the caller tool's PURPOSE and TASKS

…and decides whether to KEEP (extract structured data — or, for
overwhelming results, shortlist the most useful blocks + observation + 
a search refinement strategy) or DISCARD (explain + suggest refinement).

Thread-safe: no module-level mutable state.
"""

from __future__ import annotations

import json
import logging
import re
import time
from dataclasses import dataclass, field
from typing import Any, Callable, Dict

from ...general_hooks_management_helpers.general_context_hooks.history_tracking_hooks import (
    get_active_history_recorder,
)
from ...general_hooks_management_helpers.general_context_hooks.stats_references_tracking_hooks import (
    get_active_recorder,
)
from ThermoML_raw_json_to_card_db_parsers.id_schema import validate_nested_identifiers

log = logging.getLogger("agentic-subagent")


def _validate_raw_payload(raw: object) -> dict:
    """Validate a native result while preserving explicit refinement evidence."""
    if not isinstance(raw, dict):
        raise TypeError("raw must be an object")
    if "error_code" in raw:
        if not isinstance(raw["error_code"], str) or not raw["error_code"].strip():
            raise TypeError("raw.error_code must be a non-empty string")
        if "error" not in raw or not isinstance(raw["error"], str) or not raw["error"].strip():
            raise TypeError("raw.error must be a non-empty string")
        return raw
    validate_nested_identifiers(raw)
    return raw


# ═══════════════════════════════════════════════════════════════
#  ToolResult — returned by wrapped tools when subagent is active
# ═══════════════════════════════════════════════════════════════

@dataclass
class ToolResult:
    """Internal hand-off between compaction and memory instrumentation.

    If the subagent chose to DISCARD, ``discarded`` is True and
    ``.text`` contains an explanation + refinement suggestion.
    This object must never cross the public ReAct tool boundary.
    """
    raw: dict
    text: str
    discarded: bool = False

    def __post_init__(self) -> None:
        _validate_raw_payload(self.raw)
        if not isinstance(self.text, str) or not self.text.strip():
            raise TypeError("ToolResult.text must be a non-empty string")
        if not isinstance(self.discarded, bool):
            raise TypeError("ToolResult.discarded must be a boolean")


# ═══════════════════════════════════════════════════════════════
#  ReAct-style subagent system prompt (built per-call)
# ═══════════════════════════════════════════════════════════════

def _build_system_prompt(max_tokens: int, pipeline_label: str) -> str:
    return f"""\
You are a data-extraction subagent inside a ThermoML thermodynamic
{pipeline_label} pipeline.  You receive:

- **PURPOSE**: Why the main agent called this tool.
- **TASKS**: What specific information to extract and highlight.
- **RAW DATA**: The tool output, already compacted to markdown.

You MUST follow this ReAct loop:

### Step 1 — Thought  (wrapped in <thought>...</thought>)
Reason about the RAW DATA:
- Does it contain what PURPOSE and TASKS ask for?
- Are there errors, missing fields, or unexpected values?
- Is the data usable, or should the main agent retry with different parameters?
- Is the volume manageable for full extraction, or overwhelming (→ triage mode)?

### Step 2 — Action  (one line: <action>KEEP</action> or <action>DISCARD</action>)

### Step 3 — Output

**If KEEP** — pick a compaction mode on a sliding scale, judged by how much
of RAW DATA is useful for TASKS versus your {max_tokens}-token budget:

*Extraction mode* (default — the useful data fits):
1. A 1-2 sentence **summary/verdict** answering PURPOSE. Preserve every key
   ID exactly as received: global `GLOB*_N` IDs, DOI-local `DOIcomp_N`,
   block-local `BLKprop_N`/`BLKvar_N`/`BLKconstr_N`, typed
   `PROPblock_N`/`RXNblock_N`, DOI, and identifiers that map to raw data.
2. If applicable, 1-3 **markdown tables or JSON snippets** with the structured data
   requested by TASKS. Must preserve exact values (DOIs, typed block IDs,
   scoped IDs, coefficients, R², RMSE, pure-component values, temperatures).
   Reduce redundant/duplicate entries only.

*Triage mode* (escape path — RAW DATA is overwhelming: far more
blocks/entries than TASKS needs or than fits the budget):
1. The same 1-2 sentence **summary/verdict**, plus one line stating the
   triage, e.g. "82 blocks returned — shortlisting the 5 most relevant".
2. A **most-useful shortlist** (markdown table, ≤10 rows): the blocks/entries
   best matching PURPOSE/TASKS, each with its exact scoped IDs
   (`GLOBlit_N`, `PROPblock_N`/`RXNblock_N`, DOI) and the deciding stats
   copied verbatim from RAW DATA (pts, T/P/composition ranges, property,
   phase). Rank ONLY by criteria visible in RAW DATA — never invent scores.
3. A **search-refinement strategy**: 1-3 concrete follow-up calls (exact
   parameter names + values taken from RAW DATA) that would narrow the
   result to the shortlist, e.g. a tighter temperature window, a
   property filter, or a single DOI.

Between the extremes, slide gradually: first drop clearly irrelevant
entries and shorten tables; switch to triage mode only when extraction
would blow the budget or bury the useful entries.

**If DISCARD:**
1. A 1-2 sentence **explanation** of why the result is not useful.
2. A 1-2 sentence **refinement suggestion** — what the main agent should change
   (different parameters, alternative tool, broader/narrower query, etc.)
   to get a usable result.

Rules:
- Include ONLY key identifiers and data relevant to TASKS — omit irrelevant columns.
- NUMERICAL FIDELITY: reproduce numeric values EXACTLY as they appear in
  RAW DATA — never round, rescale, average, extrapolate, or invent numbers.
  When shortening, drop whole rows/entries; never replace dropped rows with
  synthesized "representative" values. Your output must contain NO number
  that is absent from RAW DATA.
- Never strip, shorten, synthesize, translate, or renumber an ID. Never emit
  legacy `comp_N`/`prop_N`/`block_N` forms or bare numeric IDs.
- If RAW DATA contains `ID_REFINEMENT_REQUIRED`, DISCARD and reproduce its
  field, received value, expected namespace, and reason in the refinement.
- Do NOT add interpretation beyond what the raw data shows.
- STRICTLY based on the RAW DATA — no outside knowledge or assumptions.
- Keep total output ≤ {max_tokens} tokens (tables count toward limit).
"""


# ═══════════════════════════════════════════════════════════════
#  Parsing helpers
# ═══════════════════════════════════════════════════════════════

_THOUGHT_RE = re.compile(r"<thought>(.*?)</thought>", re.DOTALL)
_ACTION_RE  = re.compile(r"<action>\s*(KEEP|DISCARD)\s*</action>", re.IGNORECASE)

# A KEEP whose post-<action> payload is this small is a max_tokens cut
# (the model overspent its budget inside <thought>, the tail got
# truncated mid-output) — shipping the stump would silently destroy a
# successful tool result.
_MIN_KEEP_OUTPUT_CHARS = 40


def parse_subagent_response(text: str) -> tuple[str, str, str]:
    """Parse a ReAct subagent response into (thought, action, output).

    Returns
    -------
    thought : str
        Content of the <thought> block (empty if absent).
    action : str
        'KEEP' or 'DISCARD'. A missing action tag is a schema error.
    output : str
        Everything after the <action> tag.
    """
    m = _THOUGHT_RE.search(text)
    if not m or not m.group(1).strip():
        raise ValueError("Compaction subagent omitted required non-empty <thought> tag")
    thought = m.group(1).strip()

    m_act = _ACTION_RE.search(text)
    if not m_act:
        raise ValueError("Compaction subagent omitted required <action>KEEP|DISCARD</action> tag")
    action = m_act.group(1).upper()

    output = text[m_act.end():].strip()
    if not output:
        raise ValueError("Compaction subagent emitted no output after its action tag")
    if action == "KEEP" and len(output) < _MIN_KEEP_OUTPUT_CHARS:
        raise ValueError(
            f"KEEP output is a {len(output)}-char stump — the reply was "
            f"almost certainly truncated at the token budget before the "
            f"extraction section; keep <thought> to 2-3 short sentences "
            f"so the output fits")

    return thought, action, output


# ═══════════════════════════════════════════════════════════════
#  Subagent call — parametrised core
# ═══════════════════════════════════════════════════════════════

def call_tool_subagent(
    tool_name: str,
    purpose: str,
    tasks: str,
    compact_md: str,
    raw: dict,
    *,
    client_factory: Callable,
    cfg: Any,
    pipeline_label: str = "query",
    reasoning_hook: Callable[[str, str], None] | None = None,
) -> ToolResult:
    """Send (purpose, tasks, compact_md) to a ReAct-style LLM subagent.

    Parameters
    ----------
    tool_name : str
        Name of the calling tool (for logging).
    purpose : str
        1-2 paragraph explanation of *why* the main agent is calling.
    tasks : str
        1-2 paragraph description of *what* to extract.
    compact_md : str
        Hardcoded markdown compaction of the raw result.
    raw : dict
        The original raw dict (preserved for working memory).
    client_factory : callable
        ``() -> ArgoClient`` — lazy constructor for the LLM client.
    cfg : object
        Agent config with attrs: SUBAGENT_CHAR_LIMIT and
        SUBAGENT_MAX_TOKENS.
    pipeline_label : str
        ``"query"`` or ``"analysis"`` — inserted into the system prompt.

    Returns
    -------
    ToolResult
        ``.raw`` = original dict, ``.text`` = subagent output,
        ``.discarded`` = True if subagent chose DISCARD.
    """
    if not isinstance(tool_name, str) or not tool_name.strip():
        raise TypeError("tool_name must be a non-empty string")
    if not isinstance(purpose, str) or not purpose.strip():
        raise TypeError("purpose must be a non-empty string")
    if not isinstance(tasks, str) or not tasks.strip():
        raise TypeError("tasks must be a non-empty string")
    if not isinstance(compact_md, str) or not compact_md.strip():
        raise TypeError("compact_md must be a non-empty string")
    _validate_raw_payload(raw)
    if cfg is None:
        raise TypeError("cfg is required")
    _CHAR_LIMIT = cfg.SUBAGENT_CHAR_LIMIT
    _MAX_TOKENS = cfg.SUBAGENT_MAX_TOKENS
    if isinstance(_CHAR_LIMIT, bool) or not isinstance(_CHAR_LIMIT, int) or _CHAR_LIMIT <= 0:
        raise TypeError("cfg.SUBAGENT_CHAR_LIMIT must be a positive integer")
    if isinstance(_MAX_TOKENS, bool) or not isinstance(_MAX_TOKENS, int) or _MAX_TOKENS <= 0:
        raise TypeError("cfg.SUBAGENT_MAX_TOKENS must be a positive integer")
    if pipeline_label not in {"query", "analysis", "main"}:
        raise ValueError("pipeline_label must be query, analysis, or main")

    history_recorder = get_active_history_recorder()
    stats_recorder = get_active_recorder()

    # ── Oversized-result contract guard ───────────────────────
    if len(compact_md) > _CHAR_LIMIT:
        est_tokens = len(compact_md) // 4
        table_rows = sum(1 for ln in compact_md.splitlines()
                         if ln.strip().startswith("|"))
        key_lines = []
        for k, v in raw.items():
            if isinstance(v, list):
                key_lines.append(f"  - `{k}`: list[{len(v)}]")
            elif isinstance(v, dict):
                key_lines.append(f"  - `{k}`: dict({len(v)} keys)")
            elif isinstance(v, str):
                key_lines.append(f"  - `{k}`: str({len(v)} chars)")
            else:
                key_lines.append(f"  - `{k}`: {type(v).__name__}")
        notice = (
            f"Tool `{tool_name}` result is too large for its mandatory subagent "
            f"(~{est_tokens:,} tokens / {len(compact_md):,} chars "
            f"after hardcoded compaction).**\n\n"
            f"### Result Stats\n"
            f"- **After compaction:** {len(compact_md):,} chars (~{est_tokens:,} tokens)\n"
            f"- **Markdown table rows:** {table_rows}\n"
            f"- **Top-level keys:**\n" + "\n".join(key_lines) + "\n\n"
            f"Narrow the query or add a dedicated deterministic compaction tier."
        )
        log.warning(
            "Rejecting oversized compaction input for %s: compact_md=%d chars (limit=%d)",
            tool_name, len(compact_md), _CHAR_LIMIT,
        )
        history_recorder.log_oversized_guard(tool_name, len(compact_md), notice[:500])
        history_recorder.log_subagent_event(
            tool_name=tool_name, event="OVERSIZED",
            detail=f"compact_md={len(compact_md):,} chars > limit={_CHAR_LIMIT:,}",
            output_chars=len(notice),
            input_chars=len(compact_md),
        )
        raise ValueError(notice)

    # ── Extract error/query context from raw dict ──────────
    _ctx_parts = []
    if "error_code" in raw:
        _ctx_parts.append(f"**Error from tool:** {raw['error']}")
    if "n_results" in raw and raw["n_results"] == 0:
        _ctx_parts.append("**Note:** Tool returned 0 results.")
    if "query_params" in raw:
        qp_str = json.dumps(raw["query_params"], indent=2, ensure_ascii=False)
        _ctx_parts.append(f"**Query parameters used:**\n```json\n{qp_str}\n```")
    _context_block = ("### CONTEXT\n" + "\n".join(_ctx_parts) + "\n\n") if _ctx_parts else ""

    prompt = (
        f"## Tool: `{tool_name}`\n\n"
        f"### PURPOSE\n{purpose}\n\n"
        f"### TASKS\n{tasks}\n\n"
        f"{_context_block}"
        f"### RAW DATA\n{compact_md}"
    )

    system = _build_system_prompt(_MAX_TOKENS, pipeline_label)

    try:
        _sa_t0 = time.perf_counter()
        response = client_factory().call(
            prompt,
            system,
            max_tokens=_MAX_TOKENS,
        )
        _sa_elapsed = time.perf_counter() - _sa_t0
        if not isinstance(response, str) or not response.strip():
            raise TypeError("compaction subagent response must be a non-empty string")

        # ── Record compactor reasoning before stripping ───────
        if reasoning_hook is not None:
            reasoning_hook(f"subagent/{tool_name}", response)

        try:
            thought, action, output = parse_subagent_response(response)
        except ValueError as parse_error:
            # One bounded retry: a single malformed reply must not discard a
            # successful tool execution.  A doubled budget covers the
            # truncated-at-max_tokens case the stump guard just rejected.
            log.warning(
                "Compaction subagent reply for %s was malformed (%s); retrying once",
                tool_name, parse_error,
            )
            retry_prompt = (
                prompt
                + "\n\n### FORMAT CORRECTION REQUIRED\nYour previous reply was "
                f"rejected: {parse_error}. Reply again following the required "
                "<thought>/<action>/<output> structure exactly. Keep <thought> "
                "to at most 3 short sentences so the output section fits in "
                "the token budget."
            )
            response = client_factory().call(
                retry_prompt,
                system,
                max_tokens=_MAX_TOKENS * 2,
            )
            _sa_elapsed = time.perf_counter() - _sa_t0
            if not isinstance(response, str) or not response.strip():
                raise TypeError(
                    "compaction subagent retry response must be a non-empty string"
                )
            if reasoning_hook is not None:
                reasoning_hook(f"subagent/{tool_name}/retry", response)
            thought, action, output = parse_subagent_response(response)

        if thought:
            log.info("Subagent thought for %s: %.120s...", tool_name, thought)

        if action == "DISCARD":
            log.info(
                "Subagent DISCARDED %s result (%d chars). Reason: %.120s",
                tool_name, len(compact_md), output[:120],
            )
            stats_recorder.log_subagent_verdict(
                tool_name=tool_name,
                verdict="DISCARD",
                subagent_output_chars=len(output),
                subagent_elapsed_s=round(_sa_elapsed, 1),
                subagent_input_chars=len(compact_md),
            )
            discard_text = (
                f"**\u26a0 Tool `{tool_name}` result discarded by subagent.**\n\n"
                f"{output}"
            )
            history_recorder.log_subagent_event(
                tool_name=tool_name, event="DISCARD",
                detail=output[:200], output_chars=len(discard_text),
                elapsed_s=round(_sa_elapsed, 1),
                input_chars=len(compact_md),
            )
            return ToolResult(raw=raw, text=discard_text, discarded=True)

        # KEEP path
        log.info(
            "Subagent for %s returned %d chars (KEEP)",
            tool_name, len(output),
        )
        stats_recorder.log_subagent_verdict(
            tool_name=tool_name,
            verdict="KEEP",
            subagent_output_chars=len(output),
            subagent_elapsed_s=round(_sa_elapsed, 1),
            subagent_input_chars=len(compact_md),
        )
        history_recorder.log_subagent_event(
            tool_name=tool_name, event="KEEP",
            detail=output[:200], output_chars=len(output),
            elapsed_s=round(_sa_elapsed, 1),
            input_chars=len(compact_md),
        )
        return ToolResult(raw=raw, text=output)

    except Exception as e:
        log.error("Subagent call failed for %s: %s", tool_name, e, exc_info=True)
        history_recorder.log_subagent_event(
            tool_name=tool_name, event="ERROR",
            detail=str(e)[:200], output_chars=0,
            input_chars=len(compact_md),
        )
        raise RuntimeError(
            f"Mandatory agentic compaction failed for tool {tool_name!r}"
        ) from e


# ═══════════════════════════════════════════════════════════════
#  Base dataclass — subclass in each agent's compactor_hooks/
# ═══════════════════════════════════════════════════════════════

@dataclass
class ToolResultCompactor:
    """Unified tool-result compaction: hardcoded dict→markdown + agentic
    KEEP/DISCARD via ReAct subagent.

    Subclass in ``<agent>_context_hooks/compactor_hooks/`` and set
    *client_factory*, *cfg*, *pipeline_label*, and *compactor_registry*.

    Two-layer pipeline
    ------------------
    1. ``compact_tool_result(tool_name, data)`` — applies the hardcoded
       dict→markdown compactor registered in *compactor_registry*.
    2. ``call(tool_name, purpose, tasks, compact_md, raw)`` — sends the
       markdown to the LLM subagent for KEEP/DISCARD triage.
    3. ``compact_and_call(tool_name, purpose, tasks, raw)`` — convenience
       method that chains both steps.
    """

    client_factory: Callable | None = None
    cfg: Any = None
    pipeline_label: str = "query"
    compactor_registry: Dict[str, Any] = field(default_factory=dict)
    reasoning_hook: Callable[[str, str], None] | None = None

    # ── Layer 1: hardcoded dict→markdown ────────────────────

    def compact_tool_result(self, tool_name: str, data: dict) -> str:
        """Look up the compactor for *tool_name* and return markdown.

        Every non-pass-through tool must have a registered compactor.
        Missing or failing compactors are contract errors.
        """
        if tool_name not in self.compactor_registry:
            raise KeyError(f"No compactor registered for tool {tool_name!r}")
        fn = self.compactor_registry[tool_name]
        try:
            compact_md = fn(data)
        except Exception as exc:
            raise RuntimeError(f"Compactor for {tool_name!r} failed") from exc
        if not isinstance(compact_md, str) or not compact_md.strip():
            raise TypeError(f"Compactor for {tool_name!r} must return non-empty markdown")
        return compact_md

    # ── Layer 2: agentic KEEP/DISCARD ───────────────────────

    def call(
        self,
        tool_name: str,
        purpose: str,
        tasks: str,
        compact_md: str,
        raw: dict,
    ) -> ToolResult:
        if self.client_factory is None:
            raise RuntimeError("ToolResultCompactor.client_factory not set")
        return call_tool_subagent(
            tool_name, purpose, tasks, compact_md, raw,
            client_factory=self.client_factory,
            cfg=self.cfg,
            pipeline_label=self.pipeline_label,
            reasoning_hook=self.reasoning_hook,
        )

    # ── Convenience: both layers in one call ────────────────

    def compact_and_call(
        self,
        tool_name: str,
        purpose: str,
        tasks: str,
        raw: dict,
    ) -> ToolResult:
        """Hardcoded compaction → agentic subagent in a single step."""
        compact_md = self.compact_tool_result(tool_name, raw)
        return self.call(tool_name, purpose, tasks, compact_md, raw)
