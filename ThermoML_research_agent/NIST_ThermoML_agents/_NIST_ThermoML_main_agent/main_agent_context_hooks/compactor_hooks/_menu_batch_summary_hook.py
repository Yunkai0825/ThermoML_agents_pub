"""
Menu batch summary stage hook.
==============================
Fires after a parallel batch of ``run_subagent_tool`` calls in the
react loop.  Uses the main agent's ``MainToolResultCompactor`` (Layer 2
agentic KEEP/DISCARD subagent) to compact the batch of individually
compacted tool results into a single unified summary.

Each individual ``run_subagent_tool`` call already returns a fully
compacted ``ToolResult`` (Layer 1 + Layer 2 via the source agent's
compactor).  This hook aggregates those compacted texts and runs
them through the main agent's own Layer 2 subagent for batch-level
triage and synthesis.

This is a **stage hook**, not a tool — the main agent never calls it
directly.  It is wired into ``agent_turn`` via the
``batch_summary_hook`` parameter.
"""
from __future__ import annotations

import json
import logging
from typing import Callable

from .tool_result_compactor import MainToolResultCompactor

log = logging.getLogger("MAIN-MENU-BATCH-SUMMARY")

# ── Lazy singleton for the main agent's compactor ───────────
_compactor = None


def _ensure_compactor():
    global _compactor
    if _compactor is None:
        _compactor = MainToolResultCompactor()
    return _compactor


def build_menu_batch_summary_hook() -> Callable:
    """Return a stage hook that uses ``MainToolResultCompactor.call()``
    to produce a unified batch summary.

    Returns
    -------
    callable
        ``hook(tool_calls, result_parts) -> str | None``
        Returns summarised text, or None to skip (no menu tools in batch).
    """

    def hook(
        tool_calls: list[dict],
        result_parts: list[str],
        *,
        purpose: str = "",
        tasks: str = "",
    ) -> str | None:
        """Summarise a parallel batch if it contains menu tool calls.

        Uses the main agent's ``MainToolResultCompactor.call()`` —
        the same Layer 2 agentic KEEP/DISCARD pipeline used for
        individual tool results — to produce a single unified
        summary of the entire batch.

        Parameters
        ----------
        tool_calls : list[dict]
            Each dict has ``name`` and ``arguments``.
        result_parts : list[str]
            Corresponding compacted result strings (from individual
            ``run_subagent_tool`` calls that already went through
            their source agent's full compaction pipeline).
        purpose : str
            Main agent's current purpose.
        tasks : str
            Main agent's current tasks.

        Returns
        -------
        str | None
            Summarised result text, or None if no menu tools
            were in the batch (callers should fall through to
            default stage compaction).
        """
        # ── Filter for run_subagent_tool calls ───────────────
        menu_items: list[tuple[dict, str]] = []
        other_items: list[tuple[dict, str]] = []

        for tc, rp in zip(tool_calls, result_parts):
            if tc.get("name") == "run_subagent_tool":
                menu_items.append((tc, rp))
            else:
                other_items.append((tc, rp))

        if not menu_items:
            return None  # No menu tools → skip, let default hook handle it

        # ── Extract purpose/tasks from tool call args if not given ──
        if not purpose:
            for tc, _ in menu_items:
                args = tc.get("arguments", {})
                if isinstance(args, str):
                    try:
                        args = json.loads(args)
                    except Exception as exc:
                        log.error("Failed to parse menu-tool batch args JSON: %s", exc, exc_info=True)
                        args = {}
                if args.get("purpose"):
                    purpose = args["purpose"]
                if args.get("tasks"):
                    tasks = args["tasks"]
                if purpose:
                    break

        # ── Build combined compact_md from individual results ─
        parts = []
        tool_names = []
        for i, (tc, rp) in enumerate(menu_items, 1):
            args = tc.get("arguments", {})
            if isinstance(args, str):
                try:
                    args = json.loads(args)
                except Exception as exc:
                    log.error("Failed to parse tool args JSON for batch summary: %s", exc, exc_info=True)
            tname = args.get("tool_name", "?") if isinstance(args, dict) else "?"
            tool_names.append(tname)
            parts.append(f"### Tool {i}: {tname}\n{rp}")

        compact_md = "\n\n".join(parts)

        # Synthetic raw dict for the batch (consumed by ToolResult.raw)
        batch_raw = {
            "batch_tool_names": tool_names,
            "batch_size": len(menu_items),
            "individual_results": [rp for _, rp in menu_items],
        }

        if not isinstance(purpose, str) or not purpose.strip():
            raise ValueError(
                "TOOL_ARGUMENT_REFINEMENT_REQUIRED: menu batch purpose must be a non-empty string."
            )
        if not isinstance(tasks, str) or not tasks.strip():
            raise ValueError(
                "TOOL_ARGUMENT_REFINEMENT_REQUIRED: menu batch tasks must be a non-empty string."
            )

        # ── Run through MainToolResultCompactor Layer 2 ──────
        # Compaction is mandatory. An error must propagate so an incomplete
        # or silently truncated batch cannot enter the parent context.
        compactor = _ensure_compactor()
        result = compactor.call(
            tool_name="run_subagent_tool_batch",
            purpose=purpose,
            tasks=tasks,
            compact_md=compact_md,
            raw=batch_raw,
        )
        summary = result.text
        log.info(
            "Menu batch summary (MainToolResultCompactor): "
            "%d tools → %d chars, discarded=%s",
            len(menu_items), len(summary), result.discarded,
        )

        # ── Combine with non-menu results if any ────────────
        final_parts = [f"## Menu Tool Batch Summary\n\n{summary}"]
        for tc, rp in other_items:
            final_parts.append(f"### {tc.get('name', '?')}\n{rp}")

        return "\n\n".join(final_parts)

    return hook
