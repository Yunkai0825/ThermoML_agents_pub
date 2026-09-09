"""L1 query delegation — workflow-driven dispatch of DB queries.

Loads ``L1_query_delegation_workflow.md`` via the subworkflow parser
and dispatches queries to the ThermoML query agent's L1 search worker.

Public API
----------
dispatch_query(purpose, instruction, id_catalog, context) -> str
dispatch_queries_parallel(queries, max_workers) -> list[dict]
"""

from __future__ import annotations

import contextvars
import json
import logging
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import partial
from pathlib import Path
from typing import Any, Dict, List

from .._subworkflow_md_parser.subworkflow_parser import parse_workflow, render_prompt
from ....general_db_query_engine.general_argo_engine_helpers.json_answer_guard import (
    validate_against_schema,
)
from ....general_db_query_engine.general_hooks_management_helpers.general_memory_management_tools_hooks_helpers.session_manager_output_storage import (
    ensure_directory,
)
from ....NIST_ThermoML_query_agent.query_agent_workflows.L1_workers.l1_query_dispatcher import (
    L1DegradedResultError,
    dispatch_l1_query as _dispatch_l1_query,
)

log = logging.getLogger("ANALYSIS-L1-DELEGATION")

_HERE = Path(__file__).resolve().parent
_WORKFLOW_PATH = _HERE / "L1_query_delegation_workflow.md"

_ctx_dir_lock = threading.Lock()


def _next_worker_context_dir() -> Path | None:
    """Reserve ``<analysis session>/query_worker_runs/run_N`` for the
    dispatched query worker's final context (no active session → None)."""
    try:
        from ...analysis_agent_context_hooks.hook_catalog import session_manager
        sess = session_manager.get_session()
    except Exception:
        return None
    sdir = getattr(sess, "session_dir", None) if sess is not None else None
    if sdir is None:
        return None
    base = Path(sdir) / "query_worker_runs"
    with _ctx_dir_lock:
        n = 1
        while (base / f"run_{n}").exists():
            n += 1
        target = base / f"run_{n}"
        ensure_directory(target, exist_ok=False)
    return target


def _load_workflow() -> dict:
    """Parse the L1 query delegation workflow definition."""
    return parse_workflow(_WORKFLOW_PATH)


def _get_l1_dispatcher():
    """Return the query agent's L1 dispatcher."""
    return _dispatch_l1_query


def _validate_delegated_response(
    result: str,
    response_json_schema: dict[str, Any],
) -> str:
    """Require the delegated Query L1 JSON to match this skill exactly."""
    if not isinstance(result, str) or not result.strip():
        raise ValueError("Delegated Query L1 returned an empty response")
    try:
        parsed = json.loads(result)
    except json.JSONDecodeError as exc:
        raise ValueError("Delegated Query L1 returned malformed JSON") from exc
    if not isinstance(parsed, dict):
        raise ValueError("Delegated Query L1 response must be a JSON object")
    expected = set(response_json_schema)
    received = set(parsed)
    if received != expected:
        raise ValueError(
            "Delegated Query L1 response fields do not match "
            f"L1_query_delegation schema; missing={sorted(expected - received)}, "
            f"extra={sorted(received - expected)}"
        )
    violations = validate_against_schema(parsed, response_json_schema)
    if violations:
        raise ValueError(
            "Delegated Query L1 response violates L1_query_delegation schema: "
            + "; ".join(violations)
        )
    return result


def dispatch_query(
    purpose: str,
    instruction: str = "",
    id_catalog: str = "",
    context: str = "",
) -> str:
    """Dispatch a single DB query to the ThermoML query agent L1 worker.

    Uses the L1_query_delegation_workflow.md to structure the dispatch.

    Parameters
    ----------
    purpose : str
        High-level goal (e.g. "Find viscosity data for water + ethanol").
    instruction : str
        Detailed search instructions.
    id_catalog : str
        JSON string of current resolved IDs (optional).
    context : str
        Prior context from working memory (optional).

    Returns
    -------
    str
        The query agent L1 worker's structured response.
    """
    workflow = _load_workflow()
    log.info("L1 query dispatch [workflow=%s]: purpose=%s",
             workflow["front_matter"]["agent_id"], purpose[:120])

    dispatch = _get_l1_dispatcher()
    result = dispatch(
        purpose=purpose,
        instruction=instruction,
        id_catalog=id_catalog,
        context=context,
        launcher_tool="query_thermoml",
        final_context_dir=_next_worker_context_dir(),
    )
    result = _validate_delegated_response(
        result,
        workflow["response_json_schema"],
    )
    log.info("L1 query done: %d chars returned", len(result))
    return result


def dispatch_queries_parallel(
    queries: List[Dict[str, str]],
    max_workers: int = 4,
) -> List[Dict[str, Any]]:
    """Dispatch multiple DB queries to the query agent L1 worker in parallel.

    Uses the L1_query_delegation_workflow.md for structured dispatch.

    Parameters
    ----------
    queries : list of dict
        Each dict has keys: purpose, instruction?, id_catalog?, context?.
    max_workers : int
        Maximum parallel workers.

    Returns
    -------
    list of dict
        Each entry: {"label": str, "result": str} or {"label": str, "error": str}.
    """
    workflow = _load_workflow()
    dispatch = _get_l1_dispatcher()
    n = min(len(queries), max_workers)
    log.info("Parallel L1 dispatch [workflow=%s]: %d queries, %d workers",
             workflow["front_matter"]["agent_id"], len(queries), n)

    results: List[Dict[str, Any]] = [None] * len(queries)  # type: ignore[list-item]

    with ThreadPoolExecutor(max_workers=n) as pool:
        future_to_idx = {}
        for i, q in enumerate(queries):
            required = {"label", "purpose", "instruction", "id_catalog", "context"}
            missing = sorted(required - set(q))
            unknown = sorted(set(q) - required)
            if missing or unknown:
                raise ValueError(
                    f"queries[{i}] has missing={missing} and unknown={unknown} fields"
                )
            # copy_context propagates the parent's shared history/stats
            # recorder state into the pool thread so each worker records
            # into its own nested section of the parent history
            ctx = contextvars.copy_context()
            fut = pool.submit(
                ctx.run,
                partial(dispatch, launcher_tool="query_thermoml_parallel",
                        final_context_dir=_next_worker_context_dir()),
                purpose=q["purpose"],
                instruction=q["instruction"],
                id_catalog=q["id_catalog"],
                context=q["context"],
            )
            future_to_idx[fut] = i

        for fut in as_completed(future_to_idx):
            idx = future_to_idx[fut]
            label = queries[idx]["label"]
            try:
                answer = _validate_delegated_response(
                    fut.result(),
                    workflow["response_json_schema"],
                )
                results[idx] = {"label": label, "result": answer}
            except L1DegradedResultError as exc:
                # Search finished; only post-answer refinement failed — keep
                # the salvaged IDs/answer so L0 can refine further searches.
                log.warning("L1 query %d degraded (salvage kept): %s",
                            idx, exc.original_error)
                results[idx] = {"label": label, "error": exc.original_error,
                                "salvage": exc.salvage}
            except Exception as exc:
                log.warning("L1 query %d failed: %s", idx, exc, exc_info=True)
                results[idx] = {"label": label, "error": str(exc)}

    log.info("Parallel L1 dispatch complete: %d/%d succeeded",
             sum(1 for r in results if "result" in r), len(results))
    return results
