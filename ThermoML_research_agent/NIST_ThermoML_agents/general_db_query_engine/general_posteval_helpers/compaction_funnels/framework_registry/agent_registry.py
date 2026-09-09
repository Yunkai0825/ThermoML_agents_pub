"""Agent registry — one AgentSpec per framework layer.

Envelope schema classes (field provenance, engine-verified):
ANSWER    — the agent-authored answer field (verbatim relay text)
WRITTEN   — LLM-written at synthesis (core_claims, confidence, ...)
WM        — workflow-assembled from working memory (sources, ...)
HYDRATED  — DB-hydrated deterministic enrichment (core_blocks_found,
            core_id_updates, construct_l2_* fields)
LEDGER    — deterministic data_inspections side-channel (post-synthesis
            merge; feeds the envelope DIRECTLY, never through context)
VERDICT   — verdict-runner output
SCAFFOLD  — JSON scaffolding remainder (chars-only)

``dispatchable`` lists what the layer can spawn; the delegation tree
resolves the ACTUAL parent-child pairs (type-agnostic: any layer that
holds a dispatcher tool — directly or via menu — can be the parent).
"""

from __future__ import annotations

from dataclasses import dataclass

from .tool_registry import TOOLS, MENU_PLANNER, MENU_WRAPPER


class FieldClass:
    ANSWER = "answer"
    WRITTEN = "written"
    WM = "wm"
    HYDRATED = "hydrated"
    LEDGER = "ledger"
    VERDICT = "verdict"
    SCAFFOLD = "scaffold"


# canonical field→class map shared by all envelope layers; per-agent
# schemas list which classes the layer actually produces
ENVELOPE_FIELD_CLASSES: dict[str, str] = {
    "answer": FieldClass.ANSWER,
    "core_claims": FieldClass.WRITTEN,
    "confidence": FieldClass.WRITTEN,
    "follow_up_suggestions": FieldClass.WRITTEN,
    "summary": FieldClass.WRITTEN,
    "sources": FieldClass.WM,
    "id_catalog_snapshot": FieldClass.WM,
    "fit_results": FieldClass.WM,
    "status": FieldClass.WM,
    "files": FieldClass.WM,
    "core_blocks_found": FieldClass.HYDRATED,
    "core_id_updates": FieldClass.HYDRATED,
    "data_inspections": FieldClass.LEDGER,
    "verdict": FieldClass.VERDICT,
}


# delegation layers, top to bottom — the pooled Sankey level merges
# same-type nodes per layer and dedups only at each layer's context
LAYERS = ("main", "Q", "A", "L1", "L2")


@dataclass(frozen=True)
class AgentSpec:
    key: str                       # MAIN | Q_L0 | Q_L1 | A_L0 | A_L1_ALIGN | L2_COMP...
    label: str                     # display token: Main, Q, L1, A, L1-align, L2-comp
    tools: tuple[str, ...]         # directly callable tool names
    dispatchable: tuple[str, ...] = ()  # dispatcher tool names ⊆ tools (+menu)
    menu_tools: bool = False       # can reach other catalogs via run_subagent_tool
    envelope: tuple[str, ...] = () # FieldClass values this layer produces ((),= no envelope)
    gate_tools: tuple[str, ...] = ()
    wm_kind: str = ""              # main | query_file | analysis_extract | ""
    support: tuple[str, ...] = ()  # SupportClass names instantiated by default
    terminal: bool = False         # root answer terminal (Main)
    layer: str = ""                # LAYERS member (pooled merge scope)


def _keys(*names: str) -> tuple[str, ...]:
    return tuple(names)


_EC = FieldClass

AGENTS: dict[str, AgentSpec] = {s.key: s for s in [
    AgentSpec(
        key="MAIN", label="Main", terminal=True, menu_tools=True,
        layer="main",
        tools=_keys("run_query_agent", "run_analysis_agent",
                    "run_parallel_subagents", MENU_PLANNER, MENU_WRAPPER,
                    "list_session_files"),
        dispatchable=_keys("run_query_agent", "run_analysis_agent",
                           "run_parallel_subagents"),
        envelope=(),  # answer terminal — no envelope hand-off
        gate_tools=_keys(MENU_WRAPPER),
        wm_kind="main",
        support=("SEED", "WM_RENDER"),
    ),
    AgentSpec(
        key="Q_L0", label="Q", layer="Q",
        tools=_keys("memory_read", "memory_append_history",
                    "memory_add_result", "memory_catalog_add",
                    "memory_catalog_remove", "memory_catalog_list",
                    "memory_compact", "memory_reset", "L1_query"),
        dispatchable=_keys("L1_query"),
        envelope=(_EC.ANSWER, _EC.WRITTEN, _EC.WM, _EC.LEDGER,
                  _EC.VERDICT, _EC.SCAFFOLD),
        gate_tools=(),
        wm_kind="query_file",
        support=("BRIEF", "SEED", "WM_RENDER"),
    ),
    AgentSpec(
        key="Q_L1", label="L1", layer="L1",
        tools=_keys("resolve_ids", "resolve_compound_ids",
                    "resolve_property_ids", "resolve_measurement_ids",
                    "resolve_reference_ids", "search_id_alignment",
                    "search_blocks", "block_search_adv",
                    "search_system_registry", "search_system_summary",
                    "search_similar_compounds", "screen_property_systems",
                    "inspect_block_table",
                    "L2_comp_eval", "L2_meas_eval", "L2_ref_eval",
                    "L2_prop_eval"),
        dispatchable=_keys("L2_comp_eval", "L2_meas_eval", "L2_ref_eval",
                           "L2_prop_eval"),
        envelope=(_EC.ANSWER, _EC.WRITTEN, _EC.HYDRATED, _EC.LEDGER,
                  _EC.SCAFFOLD),
        gate_tools=_keys("inspect_block_table"),
        wm_kind="",
        support=("BRIEF", "SEED"),
    ),
    AgentSpec(
        key="A_L0", label="A", menu_tools=False, layer="A",
        tools=_keys("query_thermoml", "query_thermoml_parallel",
                    "run_query_agent", "run_query_agents_parallel",
                    "align_compositions",
                    "inspect_block", "inspect_batch_result",
                    "get_pure_values",
                    "fit_block", "fit_block_derived", "fit_multi_system",
                    "compute_ideal_baseline", "predict_from_rk",
                    "propose_fitting_plan",
                    "register_custom_block", "validate_dual_basis_block",
                    "register_estimated_bridge", "consume_estimations",
                    "list_session_files"),
        dispatchable=_keys("query_thermoml", "query_thermoml_parallel",
                           "run_query_agent", "run_query_agents_parallel",
                           "align_compositions"),
        envelope=(_EC.ANSWER, _EC.WRITTEN, _EC.WM, _EC.LEDGER,
                  _EC.VERDICT, _EC.SCAFFOLD),
        gate_tools=_keys("inspect_block"),
        wm_kind="analysis_extract",
        support=("BRIEF", "SEED", "WM_RENDER"),
    ),
    AgentSpec(
        key="A_L1_ALIGN", label="L1-align", layer="L1",
        tools=_keys("search_blocks", "search_system_registry",
                    "resolve_compound_ids", "inspect_block",
                    "inspect_block_table", "get_pure_values", "fit_block",
                    "validate_dual_basis_block",
                    "register_estimated_bridge"),
        dispatchable=(),
        envelope=(_EC.ANSWER, _EC.HYDRATED, _EC.SCAFFOLD),
        gate_tools=_keys("inspect_block", "inspect_block_table"),
        support=("BRIEF",),
    ),
    AgentSpec(
        key="L2_COMP", label="L2-comp", layer="L2",
        tools=_keys("search_comp_from_block", "search_compound_dk",
                    "search_compound_indiv"),
        envelope=(_EC.ANSWER, _EC.HYDRATED, _EC.SCAFFOLD),
        support=("BRIEF",),
    ),
    AgentSpec(
        key="L2_MEAS", label="L2-meas", layer="L2",
        tools=_keys("search_meas_from_block", "search_measurement_dk",
                    "search_measurement_indiv"),
        envelope=(_EC.ANSWER, _EC.HYDRATED, _EC.SCAFFOLD),
        support=("BRIEF",),
    ),
    AgentSpec(
        key="L2_REF", label="L2-ref", layer="L2",
        tools=_keys("search_reference_from_block", "search_references"),
        envelope=(_EC.ANSWER, _EC.HYDRATED, _EC.SCAFFOLD),
        support=("BRIEF",),
    ),
    AgentSpec(
        key="L2_PROP", label="L2-prop", layer="L2",
        tools=_keys("search_prop_dk_from_block", "search_property_dk"),
        envelope=(_EC.ANSWER, _EC.HYDRATED, _EC.SCAFFOLD),
        support=("BRIEF",),
    ),
]}


def agent_spec(key: str) -> AgentSpec:
    return AGENTS[key]


def agent_for_dispatcher(tool_name: str, child_hint: str = "") -> str:
    """Agent key spawned by a dispatcher tool.

    ``child_hint`` resolves MIXED batches ("query"/"analysis" from the
    claimed child directory kind).
    """
    spec = TOOLS.get(tool_name)
    target = spec.dispatches if spec else ""
    if target == "MIXED":
        return {"query": "Q_L0", "analysis": "A_L0"}.get(child_hint, "Q_L0")
    return target
