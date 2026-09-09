"""Sanctioned re-execution: pre-delivery stage content from LOGGED args.

The exhaustive logs carry exact SIZES for native/hardcoded/agentic
stages (pipeline table) but verbatim TEXT only for the delivered stage.
For id/text content of the earlier stages, pure DB read tools are
re-executed FROM THE VERBATIM LOGGED ARGUMENTS through the real det
compactors — never from reconstructed or hardcoded argument paths.
Stateful tools (fit family, register_*) are never re-executed: their
raw stage stays chars-only and inherits the det ids.

Char counts from re-execution are cross-checked against the logged
pipeline table by the audits (drift → WARN "DB changed since run").
"""

from __future__ import annotations

import importlib
import inspect
import json
import sys
from pathlib import Path

from funnel_evidence.measures import measure, Measure

_AGENT_REPO = Path(__file__).resolve().parents[5]
for _p in (_AGENT_REPO, _AGENT_REPO / "card_db_search_tools",
           _AGENT_REPO / "card_db_search_tools" / "basic_search_tools"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

# pure, argument-deterministic DB read tools (module, function)
SEARCH_FNS = {
    "resolve_ids": ("basic_search_tools._id_alignment_search", "resolve_ids_tool"),
    "resolve_compound_ids": ("basic_search_tools._id_alignment_search", "resolve_compound_ids_tool"),
    "resolve_property_ids": ("basic_search_tools._id_alignment_search", "resolve_property_ids_tool"),
    "resolve_measurement_ids": ("basic_search_tools._id_alignment_search", "resolve_measurement_ids_tool"),
    "resolve_reference_ids": ("basic_search_tools._id_alignment_search", "resolve_reference_ids_tool"),
    "search_id_alignment": ("basic_search_tools._id_alignment_search", "search_id_alignment"),
    "search_blocks": ("basic_search_tools.1_block_search", "search_blocks"),
    "block_search_adv": ("basic_search_tools.12_block_search_adv", "block_search_adv"),
    "search_system_registry": ("basic_search_tools.2_system_registry_search", "search_system_registry"),
    "search_system_summary": ("basic_search_tools.9_system_summary_search", "search_system_summary"),
    "search_similar_compounds": ("basic_search_tools.10_compound_similarity_search", "search_similar_compounds"),
    "inspect_block_table": ("basic_search_tools.13_block_rdp_inspection", "inspect_block_table"),
}

_ANALYSIS_PKG = "NIST_ThermoML_agents.NIST_ThermoML_analysis_agent"
ANALYSIS_FNS = {
    "inspect_block": ("analysis_agent_toolbox.hardcoded_data_tools", "inspect_block"),
    "get_pure_values": ("analysis_agent_toolbox.discovery_tools", "get_pure_values"),
    "query_blocks": ("analysis_agent_toolbox.discovery_tools", "query_blocks"),
    "query_system_summary": ("analysis_agent_toolbox.discovery_tools", "query_system_summary"),
    "resolve_compounds": ("analysis_agent_toolbox.discovery_tools", "resolve_compounds"),
    "resolve_properties": ("analysis_agent_toolbox.discovery_tools", "resolve_properties"),
    "find_similar_compounds": ("analysis_agent_toolbox.discovery_tools", "find_similar_compounds"),
}

_FN_CACHE: dict[str, object] = {}
_COMPACTORS: dict[str, dict] = {}
_RESULT_CACHE: dict[tuple[str, str], tuple[Measure, Measure] | None] = {}


def _load_fn(tool: str):
    if tool in _FN_CACHE:
        return _FN_CACHE[tool]
    fn = None
    if tool in SEARCH_FNS:
        module, name = SEARCH_FNS[tool]
        fn = getattr(importlib.import_module(module), name)
    elif tool in ANALYSIS_FNS:
        module, name = ANALYSIS_FNS[tool]
        fn = getattr(importlib.import_module(f"{_ANALYSIS_PKG}.{module}"),
                     name)
    _FN_CACHE[tool] = fn
    return fn


def _compactor(tool: str, catalog: str):
    key = catalog
    if key not in _COMPACTORS:
        registry = {}
        try:
            if catalog == "analysis":
                mod = importlib.import_module(
                    f"{_ANALYSIS_PKG}.analysis_agent_context_hooks.hook_catalog")
            else:
                mod = importlib.import_module(
                    "NIST_ThermoML_agents.NIST_ThermoML_query_agent."
                    "query_agent_context_hooks.hook_catalog")
            registry = dict(getattr(mod, "COMPACTOR_REGISTRY", {}) or {})
        except Exception as exc:
            print(f"warning: compactor registry '{catalog}' unavailable: {exc}")
        _COMPACTORS[key] = registry
    return _COMPACTORS[key].get(tool)


def _serialize(raw) -> str:
    # engine native sizes are measured on default-separator json.dumps
    return raw if isinstance(raw, str) else json.dumps(
        raw, ensure_ascii=False, default=str)


# agent-facing wrapper keys the raw tools never accept
_WRAPPER_KEYS = {"purpose", "tasks"}


def _call_kwargs(fn, kwargs: dict) -> dict:
    cleaned = {k: v for k, v in kwargs.items() if k not in _WRAPPER_KEYS}
    try:
        params = inspect.signature(fn).parameters
    except (TypeError, ValueError):
        return cleaned
    if any(p.kind is inspect.Parameter.VAR_KEYWORD for p in params.values()):
        return cleaned
    return {k: v for k, v in cleaned.items() if k in params}


def reexec_stages(tool: str, kwargs: dict, catalog: str) -> tuple[Measure, Measure] | None:
    """(native, det) Measures from verbatim logged kwargs; None when the
    tool is not a pure re-executable DB read or the call fails."""
    if not isinstance(kwargs, dict):
        return None
    cache_key = (tool, json.dumps(kwargs, sort_keys=True, default=str))
    if cache_key in _RESULT_CACHE:
        return _RESULT_CACHE[cache_key]
    result: tuple[Measure, Measure] | None = None
    fn = _load_fn(tool)
    if fn is not None:
        try:
            raw = fn(**_call_kwargs(fn, kwargs))
            raw_text = _serialize(raw)
            native = measure(raw_text)
            compactor = _compactor(tool,
                                   "analysis" if tool in ANALYSIS_FNS
                                   else "query")
            if compactor is not None:
                det_out = compactor(raw)
                det_text = (det_out if isinstance(det_out, str)
                            else getattr(det_out, "compact_md", None)
                            or _serialize(det_out))
                det = measure(det_text)
            else:
                det = native
            result = (native, det)
        except Exception as exc:
            print(f"warning: re-exec {tool} failed: {exc}")
            result = None
    _RESULT_CACHE[cache_key] = result
    return result
