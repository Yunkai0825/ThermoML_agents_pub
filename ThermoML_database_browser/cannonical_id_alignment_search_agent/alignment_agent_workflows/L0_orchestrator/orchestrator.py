"""L0 Orchestrator for the canonical ID alignment agent.

Loads the workflow markdown, builds the tool registry, injects
tool descriptions, and drives the ReAct loop via ``agent_turn()``.

Public API
----------
run(search_text, settings=None) -> AgentTurnResult
    Synchronous entry point — parse → resolve → validate → fill → finalize.
"""

from __future__ import annotations

import logging
import sys
import os
from pathlib import Path
from typing import Any, Dict, Optional

# ── Ensure workspace root is on sys.path ────────────────────
_WS_ROOT = os.path.normpath(
    os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'ThermoML_research_agent')
)
if _WS_ROOT not in sys.path:
    sys.path.insert(0, _WS_ROOT)

# ── Engine helpers ──────────────────────────────────────────
from NIST_ThermoML_agents.general_db_query_engine.general_argo_engine_helpers import (
    agent_turn,
    AgentTurnResult,
    with_engine_config,
)
from NIST_ThermoML_agents.general_db_query_engine.general_subagent_skill_schema_and_parser.subworkflow_md_tool_descriptions import (
    build_tool_instructions,
)

# ── Alignment-agent specifics ──────────────────────────────
from ...alignment_agent_argo_config import AGENT_CONFIG
from ...alignment_agent_argo_engine.argo_client import AlignmentClient
from ...alignment_agent_toolbox.tool_catalog import L0_CATALOG
from ...alignment_agent_toolbox.mcp_tools import get_fields

log = logging.getLogger("Alignment-L0")

_HERE = Path(__file__).resolve().parent
_WORKFLOW_PATH = _HERE / "L0_orchestrator_workflow.md"


# ═══════════════════════════════════════════════════════════════
#  Helpers
# ═══════════════════════════════════════════════════════════════

def _load_workflow_prompt() -> str:
    """Read the system prompt from the workflow markdown.

    Requires and extracts exactly one ``<system_prompt>`` block.
    """
    text = _WORKFLOW_PATH.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError("Alignment workflow requires YAML frontmatter")
    parts = text.split("---", 2)
    if len(parts) != 3:
        raise ValueError("Alignment workflow has malformed YAML frontmatter")
    body = parts[2]
    open_tag = "<system_prompt>"
    close_tag = "</system_prompt>"
    if body.count(open_tag) != 1 or body.count(close_tag) != 1:
        raise ValueError("Alignment workflow requires exactly one <system_prompt> block")
    prompt = body.split(open_tag, 1)[1].split(close_tag, 1)[0].strip()
    if not prompt:
        raise ValueError("Alignment workflow system prompt is empty")
    return prompt


# ═══════════════════════════════════════════════════════════════
#  Main entry point
# ═══════════════════════════════════════════════════════════════

@with_engine_config(AGENT_CONFIG)
def run(
    search_text: str,
    settings: Optional[Dict[str, Any]] = None,
) -> AgentTurnResult:
    """Run the alignment agent on a free-text search input.

    Parameters
    ----------
    search_text : str
        Raw user search text (e.g. "ethanol + viscosity ; water + density").
    settings : dict, optional
        Optional settings overrides (not used yet, reserved for future
        toggles like escalation_enabled).

    Returns
    -------
    AgentTurnResult
        Contains answer, iterations, elapsed time, tool history.
        The resolved fields are also available via ``get_fields().snapshot()``.
    """
    if settings is None:
        settings = {}
    if not isinstance(settings, dict):
        raise TypeError("settings must be an object")

    # Per-run time budget.  Never mutate the module-level config singleton:
    # concurrent or later runs must retain the configured default.
    max_wait = settings["max_wait_seconds"] if "max_wait_seconds" in settings else None
    if max_wait is not None:
        if isinstance(max_wait, bool) or not isinstance(max_wait, int) or max_wait < 1:
            raise TypeError("settings.max_wait_seconds must be a positive integer")

    # Reset shared field state for this run
    fields = get_fields()
    fields.reset()

    # Build LLM client
    client = AlignmentClient.for_l0()

    # Build tool registry
    tools: Dict[str, Any] = dict(L0_CATALOG.tools)

    # Build system prompt
    system_prompt = _load_workflow_prompt()
    system_prompt += "\n\n" + build_tool_instructions(tools)

    # Compose the user question
    entry_limit = settings["entry_limit"] if "entry_limit" in settings else 20
    if isinstance(entry_limit, bool) or not isinstance(entry_limit, int) or entry_limit < 1:
        raise TypeError("settings.entry_limit must be a positive integer")
    limit_note = (
        f"\n\nIMPORTANT: The user wants up to {entry_limit} entries. "
        f"When calling resolve_entity or search_titles, use limit={entry_limit}."
    )
    user_message = (
        f"Please resolve the following search input and fill all search "
        f"form fields:\n\n{search_text}{limit_note}"
    )
    if max_wait is not None:
        user_message += (
            f"\n\nTIME BUDGET: You have {int(max_wait)} seconds. "
            "Be efficient — focus on the most impactful resolutions first."
        )

    # Escalation & block-filler settings
    allow_qa = settings["allow_query_agent"] if "allow_query_agent" in settings else False
    agentic_all = settings["agentic_all_fields"] if "agentic_all_fields" in settings else False
    if not isinstance(allow_qa, bool) or not isinstance(agentic_all, bool):
        raise TypeError("allow_query_agent and agentic_all_fields must be booleans")
    if not allow_qa:
        user_message += (
            "\n\nESCALATION DISABLED: Do NOT call escalate_to_query_agent. "
            "If you cannot resolve an entity, mark it as unresolved and continue."
        )
    if agentic_all:
        user_message += (
            "\n\nAGENTIC ALL FIELDS: The user wants you to resolve and fill "
            "ALL filter blocks (bibliography, chemistry, properties). "
            "Use fill_bibliography_block, fill_chemistry_block, and "
            "fill_properties_block to fill each section systematically."
        )

    # Run the ReAct loop
    memory: list[dict] = []
    result = agent_turn(
        user_message,
        system_prompt=system_prompt,
        tools=tools,
        memory=memory,
        client=client,
        timeout=max_wait,
    )

    log.info(
        "Alignment L0 done: %d iterations, %.1fs, timed_out=%s",
        result.iterations, result.elapsed_seconds, result.timed_out,
    )

    return result
