"""Tool registry — every framework tool with its compaction contract.

Flags mirror the live ToolEntry registrations (introspected 2026-08-15):
``det``            — a deterministic (hardcoded) compactor exists.
``skip_compactor`` — native result bypasses the det compactor.
``skip_subagent``  — no agentic KEEP/DISCARD triage stage.

Chain shapes derived from the flags (see ``chain_shape``):
FULL_PIPELINE  raw → hardcoded → agentic kept/DISCARD-stub → context
DET_ONLY       raw → hardcoded → delivered as-is → context
EXEMPT         raw → delivered as-is → context
RELAY          dispatcher: child subgraph + child envelope →
               [hardcoded → agentic per flags] relay → context

Use-time ownership is ALWAYS the calling agent instance; ``catalog``
only names the pipeline family whose compactors run (the menu executes
the owning subagent's pipeline inside Main's lane).
"""

from __future__ import annotations

from dataclasses import dataclass

# ── chain shapes ──────────────────────────────────────────────
FULL_PIPELINE = "full_pipeline"
DET_ONLY = "det_only"
EXEMPT = "exempt"
RELAY = "relay"

# menu tools (Main)
MENU_WRAPPER = "run_subagent_tool"
MENU_PLANNER = "browse_subagent_tools"

# pipeline-table rows under these names fold into the owning tool's
# chain (registered as extra compactors only, never standalone calls)
SUBSTEP_KEYS = frozenset({
    "resolve_compounds",
    "resolve_properties",
    "query_blocks",
    "query_system_summary",
    "find_similar_compounds",
    "run_subagent_tool_batch",   # menu batch consolidation event row
})


@dataclass(frozen=True)
class ToolSpec:
    name: str
    catalog: str                 # compacting pipeline family: query|analysis|main|l2_comp|l2_meas|l2_ref|l2_prop|self
    det: bool = False            # deterministic compactor exists
    skip_compactor: bool = False
    skip_subagent: bool = True
    dispatches: str = ""         # AgentSpec key spawned ("" = plain tool; "MIXED" = per-child kind)
    batch: bool = False          # one call may claim several children
    inspection: bool = False     # validation lane (grounding inspections)
    fit_rail: bool = False       # delivered render registers FIT_ artifacts
    stateful: bool = False       # native not reproducible from args (chars-only raw ids inherit det)
    menu_only: bool = False      # reachable only via Main's menu
    notes: str = ""

    @property
    def is_dispatcher(self) -> bool:
        return bool(self.dispatches)


def chain_shape(spec: ToolSpec) -> str:
    if spec.is_dispatcher:
        return RELAY
    if spec.det and not spec.skip_compactor:
        return DET_ONLY if spec.skip_subagent else FULL_PIPELINE
    return EXEMPT


def _t(*a, **k) -> ToolSpec:
    return ToolSpec(*a, **k)


TOOLS: dict[str, ToolSpec] = {t.name: t for t in [
    # ── Main L0 (catalog "main"; dispatch relays compacted by main pipeline) ──
    _t("run_query_agent", "main", det=True, skip_subagent=False,
       dispatches="Q_L0", notes="relay det=compact_query_result + triage"),
    _t("run_analysis_agent", "main", det=True, skip_subagent=False,
       dispatches="A_L0", notes="relay det=compact_analysis_result + triage"),
    _t("run_parallel_subagents", "main", skip_compactor=True,
       dispatches="MIXED", batch=True,
       notes="self-compacting batch (philosophy hook); snapshot fallback"),
    _t(MENU_PLANNER, "main", skip_compactor=True, notes="LLM planner, exempt"),
    _t(MENU_WRAPPER, "main", skip_compactor=True,
       notes="menu executor; unwraps to inner tool's owning pipeline"),
    _t("list_session_files", "self", skip_compactor=True,
       notes="runtime util on Main + A_L0"),

    # ── Query L0 (8 memory tools + runtime L1 dispatcher) ──
    _t("memory_read", "query", skip_compactor=True),
    _t("memory_append_history", "query", skip_compactor=True),
    _t("memory_add_result", "query", skip_compactor=True),
    _t("memory_catalog_add", "query", skip_compactor=True),
    _t("memory_catalog_remove", "query", skip_compactor=True),
    _t("memory_catalog_list", "query", skip_compactor=True),
    _t("memory_compact", "query", skip_compactor=True),
    _t("memory_reset", "query", skip_compactor=True),
    _t("L1_query", "self", skip_compactor=True, dispatches="Q_L1",
       notes="runtime-registered self-compacting L1 relay"),

    # ── Query L1 worker (search catalog; full pipeline unless noted) ──
    _t("resolve_ids", "query", det=True, skip_subagent=False),
    _t("resolve_compound_ids", "query", det=True, skip_subagent=False),
    _t("resolve_property_ids", "query", det=True, skip_subagent=False),
    _t("resolve_measurement_ids", "query", det=True, skip_subagent=False),
    _t("resolve_reference_ids", "query", det=True, skip_subagent=False),
    _t("search_id_alignment", "query", det=True, skip_subagent=False),
    _t("search_blocks", "query", det=True, skip_subagent=False),
    _t("block_search_adv", "query", det=True, skip_subagent=False),
    _t("search_system_registry", "query", det=True, skip_subagent=False),
    _t("search_system_summary", "query", det=True, skip_subagent=False),
    _t("search_similar_compounds", "query", det=True, skip_subagent=False),
    _t("screen_property_systems", "query", det=True, skip_subagent=False),
    _t("inspect_block_table", "query", det=True, inspection=True),
    _t("L2_comp_eval", "self", skip_compactor=True, dispatches="L2_COMP"),
    _t("L2_meas_eval", "self", skip_compactor=True, dispatches="L2_MEAS"),
    _t("L2_ref_eval", "self", skip_compactor=True, dispatches="L2_REF"),
    _t("L2_prop_eval", "self", skip_compactor=True, dispatches="L2_PROP"),

    # ── L2 leaf evaluators (only the meas family is det-compacted) ──
    _t("search_comp_from_block", "l2_comp", skip_compactor=True),
    _t("search_compound_dk", "l2_comp", skip_compactor=True),
    _t("search_compound_indiv", "l2_comp", skip_compactor=True),
    _t("search_meas_from_block", "l2_meas", det=True),
    _t("search_measurement_dk", "l2_meas", det=True),
    _t("search_measurement_indiv", "l2_meas", det=True),
    _t("search_reference_from_block", "l2_ref", skip_compactor=True),
    _t("search_references", "l2_ref", skip_compactor=True),
    _t("search_prop_dk_from_block", "l2_prop", skip_compactor=True),
    _t("search_property_dk", "l2_prop", skip_compactor=True),

    # ── Analysis L0 ──
    _t("query_thermoml", "self", skip_compactor=True, dispatches="Q_L1",
       notes="in-process L1 query worker under analysis"),
    _t("query_thermoml_parallel", "self", skip_compactor=True,
       dispatches="Q_L1", batch=True),
    _t("run_query_agents_parallel", "analysis", skip_compactor=True,
       dispatches="Q_L0", batch=True),
    _t("align_compositions", "analysis", det=True,
       dispatches="A_L1_ALIGN", notes="relay det-compacted, no triage"),
    _t("inspect_block", "analysis", det=True, inspection=True),
    _t("inspect_batch_result", "analysis", det=True, inspection=True,
       notes="runtime/legacy occurrences only"),
    _t("get_pure_values", "analysis", det=True),
    _t("fit_block", "analysis", det=True, fit_rail=True, stateful=True),
    _t("fit_block_derived", "analysis", det=True, fit_rail=True, stateful=True),
    _t("fit_multi_system", "analysis", det=True, fit_rail=True, stateful=True),
    _t("compute_ideal_baseline", "analysis", det=True, fit_rail=True, stateful=True),
    _t("predict_from_rk", "analysis", det=True, fit_rail=True, stateful=True),
    _t("propose_fitting_plan", "analysis", det=True, fit_rail=True, stateful=True),
    _t("register_custom_block", "analysis", det=True, skip_subagent=False,
       stateful=True, notes="full pipeline; NOT a grounded rail"),
    _t("validate_dual_basis_block", "analysis", skip_compactor=True, stateful=True),
    _t("register_estimated_bridge", "analysis", skip_compactor=True, stateful=True),
    _t("consume_estimations", "analysis", skip_compactor=True, stateful=True),
]}

# The discovery trio + resolve extras appear in histories only as menu
# targets or pipeline sub-step rows — SUBSTEP_KEYS folds the sub-step
# rows; menu steps carry the plain names and resolve through TOOLS via
# _MENU_FALLBACK specs below.
_MENU_FALLBACK: dict[str, ToolSpec] = {
    "query_system_summary": _t("query_system_summary", "analysis", det=True, menu_only=True),
    "query_blocks": _t("query_blocks", "analysis", det=True, menu_only=True),
    "find_similar_compounds": _t("find_similar_compounds", "analysis", det=True, menu_only=True),
}


def tool_spec(name: str) -> ToolSpec:
    """Resolve a history tool name to its spec (menu fallbacks included)."""
    if name in TOOLS:
        return TOOLS[name]
    if name in _MENU_FALLBACK:
        return _MENU_FALLBACK[name]
    # Unknown tools degrade to exempt pass-through (audit reports them).
    return ToolSpec(name=name, catalog="self", skip_compactor=True,
                    notes="UNREGISTERED tool name")
