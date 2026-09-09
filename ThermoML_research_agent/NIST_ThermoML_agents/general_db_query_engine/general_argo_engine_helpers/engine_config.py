"""
EngineConfig — shared configuration shape for the Argo ReAct engine.
===================================================================
Each agent defines its own dataclass subclass:

- ``ThermoML_query_argo_config.py``    → ``QueryAgentConfig(EngineConfig)``
- ``ThermoML_analysis_argo_config.py`` → ``AnalysisAgentConfig(EngineConfig)``

At startup the agent's engine package calls ``load_config(AGENT_CONFIG)``
to establish an import-context default.  Every public agent runner is also
decorated with ``with_engine_config(AGENT_CONFIG)`` so nested and concurrent
agents read their own configuration for the complete lifetime of a run.
"""

from __future__ import annotations

from contextvars import ContextVar
from dataclasses import dataclass, field
from functools import wraps
import inspect
from typing import List


@dataclass
class EngineConfig:
    """Configuration required by the shared Argo engine.

    No defaults — each agent subclass must define every value.
    These fields are consumed by the four core engine modules:
      - argo_client_caller.py  (ArgoClient factory methods)
      - react_loop.py          (synchronous agent_turn)
      - react_loop_async.py    (asynchronous async_agent_turn)
      - react_helpers.py       (result-size contract, compaction threshold)
    """

    # ── API connection ──────────────────────────────────────
    API_URL: str            # Argo REST chat endpoint; used by ArgoClient.call()
    API_USER: str           # Argo API username; sent in every request payload
    HEADERS: dict           # HTTP headers (Content-Type); passed to requests.post()

    # ── Model names ─────────────────────────────────────────
    MODEL: str              # Primary LLM for the L0 orchestrator and L1 workers
    VERDICT_MODEL: str      # LLM for post-job quality review; ArgoClient.for_verdict()
    PLANNER_MODEL: str      # LLM for strategy planning; ArgoClient.for_planner()

    # ── Generation parameters ───────────────────────────────
    TEMPERATURE: float      # Sampling temperature for the primary MODEL
    TOP_P: float            # Nucleus-sampling p (omitted for Claude models)
    MAX_TOKENS: int         # Max tokens per LLM response (primary calls)
    HTTP_TIMEOUT: int       # Seconds before requests.post() raises a timeout

    # ── Agent loop limits (L0) ──────────────────────────────
    MAX_TOOL_ITERATIONS: int  # Hard cap on tool-call iterations in react_loop.agent_turn()
    MAX_TURN_SECONDS: int     # Wall-clock budget for one agent_turn() call

    # ── L2 async limits ─────────────────────────────────────
    L2_MAX_ITERATIONS: int  # Iteration cap for async_agent_turn() (L2 leaf evaluators)
    L2_MAX_SECONDS: int     # Time budget for each async L2 evaluator call

    # ── Time warnings ───────────────────────────────────────
    WARN_THRESHOLDS: List[float]  # Fraction-of-budget breakpoints for [TIME WARNING] injection
    MAX_WRAP_WARNINGS: int        # Max "wrap up" reminders before hard-stop
    MAX_EMPTY_WAITS: int          # Max consecutive empty LLM responses before abort

    # ── Tool result contract ────────────────────────────────
    TOOL_RESULT_CHAR_LIMIT: int   # Oversized post-compaction results get a visible warning banner

    # ── Compaction ──────────────────────────────────────────
    COMPACTION_TRIGGER_CHARS: int  # Context size (chars) that triggers LLM-driven compaction
    SUMMARY_MAX_CHARS: int         # Target length for each compacted summary block
    GUIDANCE_MAX_TOKENS: int       # Token budget for the compaction-guidance LLM call

    # ── Verdict client ──────────────────────────────────────
    VERDICT_TEMPERATURE: float  # Temperature for the verdict LLM; low = deterministic review
    VERDICT_MAX_TOKENS: int     # Max tokens for the verdict response

    # ── Compactor client ────────────────────────────────────
    COMPACTOR_TEMPERATURE: float  # Temperature for the compaction sub-agent
    COMPACTOR_MAX_TOKENS: int     # Max tokens allowed for each compaction response

    # ── Planner client ──────────────────────────────────────
    PLANNER_TEMPERATURE: float  # Temperature for strategy-planning LLM calls
    PLANNER_MAX_TOKENS: int     # Max tokens for each planner response
    # ── Subagent-return ledger rendering ───────────────────
    # Per-transition-pair ledger abstraction levels for the single-source
    # subagent-return renderer (engine_react_helpers.subagent_context_render):
    #   {"context": {pair: level}, "memory": {pair: level}}
    # pair keys: "main/Qi", "main/Ai", "main/L1", "main/L2", "Ai/Qi",
    # "Ai/L1", "Qi/L1", "L1/L2" (plus optional "default"); levels:
    # "full" | "summary" | "none".  Missing entries fall back to
    # "full" (context surface) / "summary" (working-memory surface).
    # ROOT PRECEDENCE: the outermost with_engine_config runner claims this
    # map for the WHOLE session tree — nested subagent runners keep their
    # own configs for everything else, but ledger levels come from the
    # root.  Each session config must therefore list EVERY pair reachable
    # from its root down to the deepest ledger-bearing layer.
    SUBAGENT_LEDGER_LEVELS: dict = field(default_factory=dict)
    def is_claude_model(self, model_name: str) -> bool:
        """Return True for Claude models, which require omitting top_p."""
        return "claude" in model_name.lower()


# ── Run-local active configuration ──────────────────────────

_active_config: ContextVar[EngineConfig | None] = ContextVar(
    "thermoml_active_engine_config",
    default=None,
)
# Ledger-level policy of the ROOT session: claimed by the OUTERMOST
# with_engine_config runner in the execution context and inherited by
# every nested subagent runner, so the root agent's per-pair settings
# overwrite the subagent configs' own maps for the whole session tree.
_root_ledger_levels: ContextVar[dict | None] = ContextVar(
    "thermoml_root_subagent_ledger_levels",
    default=None,
)


def get_root_ledger_levels() -> dict | None:
    """Return the root session's ``SUBAGENT_LEDGER_LEVELS`` map (or None).

    ``None`` means no :func:`with_engine_config` runner is active in this
    context — callers should fall back to the active config's own map.
    """
    return _root_ledger_levels.get()

def load_config(config: EngineConfig) -> None:
    """Set the active configuration in the current execution context.

    Import-time calls provide a default for direct single-agent use.  Agent
    runners must use :func:`with_engine_config` so the value is restored after
    nested calls and isolated across threads and asyncio tasks.
    """
    if not isinstance(config, EngineConfig):
        raise TypeError("config must be an EngineConfig instance")
    _active_config.set(config)


def load_default_config(config: EngineConfig) -> None:
    """Provide an import-time default without clobbering an active run.

    Lazy imports of a sibling agent's engine package mid-run (e.g. the main
    agent importing query/analysis compactors) must not overwrite the
    running agent's active configuration.
    """
    if not isinstance(config, EngineConfig):
        raise TypeError("config must be an EngineConfig instance")
    if _active_config.get() is None:
        _active_config.set(config)


def get_config() -> EngineConfig:
    """Return the active engine configuration.

    Raises ``RuntimeError`` if no agent has called ``load_config()`` yet.
    """
    config = _active_config.get()
    if config is None:
        raise RuntimeError(
            "Engine config not loaded. Call load_config() with your "
            "agent's EngineConfig before using the engine."
        )
    return config


def with_engine_config(config: EngineConfig):
    """Decorate one complete agent run with an isolated engine config.

    ``ContextVar`` state is inherited by asyncio tasks and by the explicit
    ``copy_context`` bridges used by post-answer worker pools.  The token reset
    is essential for nested Main → Query/Analysis calls executed in one thread.

    The OUTERMOST decorated runner also claims the session tree's
    ``SUBAGENT_LEDGER_LEVELS`` policy (root precedence): nested runners keep
    swapping the active config but never the root ledger map.
    """
    if not isinstance(config, EngineConfig):
        raise TypeError("config must be an EngineConfig instance")

    def _claim_root_levels():
        if _root_ledger_levels.get() is not None:
            return None
        return _root_ledger_levels.set(
            getattr(config, "SUBAGENT_LEDGER_LEVELS", None) or {})

    def decorator(func):
        if inspect.iscoroutinefunction(func):
            @wraps(func)
            async def async_wrapper(*args, **kwargs):
                token = _active_config.set(config)
                root_token = _claim_root_levels()
                try:
                    return await func(*args, **kwargs)
                finally:
                    if root_token is not None:
                        _root_ledger_levels.reset(root_token)
                    _active_config.reset(token)

            return async_wrapper

        @wraps(func)
        def wrapper(*args, **kwargs):
            token = _active_config.set(config)
            root_token = _claim_root_levels()
            try:
                return func(*args, **kwargs)
            finally:
                if root_token is not None:
                    _root_ledger_levels.reset(root_token)
                _active_config.reset(token)

        return wrapper

    return decorator
