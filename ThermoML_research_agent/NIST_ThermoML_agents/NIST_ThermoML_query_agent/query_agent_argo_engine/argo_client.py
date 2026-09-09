"""
QueryClient — ArgoClient with query-agent-specific factory methods.
===================================================================
Thin subclass that adds ``for_l0``, ``for_l1``, ``for_l2`` convenience
constructors using the query agent's own config values.
"""
from __future__ import annotations

from dataclasses import dataclass

from ...general_db_query_engine.general_argo_engine_helpers import ArgoClient
from ..ThermoML_query_argo_config import AGENT_CONFIG as cfg


@dataclass
class QueryClient(ArgoClient):
    """ArgoClient configured for the ThermoML query agent."""

    @classmethod
    def for_l0(cls) -> QueryClient:
        """L0 orchestrator client."""
        return cls(model=cfg.MODEL, max_tokens=cfg.MAX_TOKENS, _tier="L0-main")

    @classmethod
    def for_l1(cls) -> QueryClient:
        """L1 worker client."""
        return cls(model=cfg.L1_MODEL, max_tokens=cfg.MAX_TOKENS, _tier="L1-worker")

    @classmethod
    def for_l2(cls) -> QueryClient:
        """L2 leaf evaluator client."""
        return cls(model=cfg.L2_MODEL, max_tokens=cfg.L2_MAX_TOKENS, _tier="L2-leaf")
