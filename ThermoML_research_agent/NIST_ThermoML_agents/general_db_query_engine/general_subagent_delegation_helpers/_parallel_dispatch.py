"""
Parallel dispatch helper for subagent delegation.
===================================================
Wraps ``ThreadPoolExecutor`` with label management, error capture,
and ordered result collection.
"""
from __future__ import annotations

import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from contextvars import copy_context
from typing import Any, Callable, Dict, List

log = logging.getLogger(__name__)


def dispatch_parallel(
    tasks: list[dict],
    runner_fn: Callable[..., Dict[str, Any]],
    *,
    max_workers: int = 3,
    runner_kwargs_keys: tuple[str, ...] = ("question", "purpose", "tasks", "context"),
    default_agent: str = "query",
) -> Dict[str, Any]:
    """Validate a structured task array and dispatch via *runner_fn*.

    Parameters
    ----------
    tasks : list[dict]
        Task specs. Each object must contain ``label``
        and the keys listed in *runner_kwargs_keys*.
    runner_fn : callable
        ``(question, purpose, tasks, context, ...) -> dict``.
        Called once per task.
    max_workers : int
        Maximum concurrent threads.
    runner_kwargs_keys : tuple[str, ...]
        Which keys from each task dict to pass as kwargs to *runner_fn*.
    default_agent : str
        Agent type label for error dicts when *runner_fn* raises.

    Returns
    -------
    dict
        ``{"n_tasks": N, "results": [...]}``.
    """
    if not isinstance(tasks, list) or not tasks:
        raise TypeError("tasks must be a non-empty array of task objects")
    if isinstance(max_workers, bool) or not isinstance(max_workers, int) or max_workers < 1:
        raise TypeError("max_workers must be a positive integer")
    allowed = {"label", "agent", *runner_kwargs_keys}
    for index, task in enumerate(tasks):
        if not isinstance(task, dict):
            raise TypeError(f"tasks[{index}] must be an object")
        required = {"label", *runner_kwargs_keys}
        missing = sorted(required - set(task))
        unknown = sorted(set(task) - allowed)
        if missing:
            raise ValueError(f"tasks[{index}] is missing fields {missing}")
        if unknown:
            raise ValueError(f"tasks[{index}] has unknown fields {unknown}")
        for field in required:
            if not isinstance(task[field], str) or not task[field].strip():
                raise TypeError(f"tasks[{index}].{field} must be a non-empty string")
        if "agent" in task and (
            not isinstance(task["agent"], str) or not task["agent"].strip()
        ):
            raise TypeError(f"tasks[{index}].agent must be a non-empty string")

    effective_workers = min(len(tasks), max_workers)
    log.info("Parallel dispatch: %d tasks, %d workers", len(tasks), effective_workers)

    results: List[Dict[str, Any] | None] = [None] * len(tasks)

    with ThreadPoolExecutor(max_workers=effective_workers) as pool:
        future_to_idx: Dict[Any, int] = {}
        for i, t in enumerate(tasks):
            kwargs = {k: t[k] for k in runner_kwargs_keys}
            # ContextVars do not cross ThreadPoolExecutor boundaries by
            # default.  Each delegated call must receive an independent copy
            # of the submitting context so nested session/tool registries are
            # available without sharing a mutable Context object.
            task_context = copy_context()
            fut = pool.submit(task_context.run, runner_fn, **kwargs)
            future_to_idx[fut] = i

        for fut in as_completed(future_to_idx):
            idx = future_to_idx[fut]
            label = tasks[idx]["label"]
            agent = tasks[idx]["agent"] if "agent" in tasks[idx] else default_agent
            try:
                r = fut.result()
                if not isinstance(r, dict):
                    raise TypeError(
                        f"parallel task {label!r} returned {type(r).__name__}, not an object"
                    )
                r["label"] = label
                results[idx] = r
            except Exception as e:
                log.warning("Parallel task %d (%s) failed: %s", idx, label, e)
                results[idx] = {"label": label, "error": str(e), "agent": agent}

    return {"n_tasks": len(tasks), "results": results}  # type: ignore[dict-item]
