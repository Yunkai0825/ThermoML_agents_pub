"""
MainClient — ArgoClient with main-agent-specific factory methods.
=================================================================
Thin subclass that adds ``for_l0`` convenience constructor using the
main agent's own config values.
"""
from __future__ import annotations

from dataclasses import dataclass

from ...general_db_query_engine.general_argo_engine_helpers import ArgoClient
from ..ThermoML_main_argo_config import AGENT_CONFIG as cfg


@dataclass
class MainClient(ArgoClient):
    """ArgoClient configured for the ThermoML main agent."""

    @classmethod
    def for_l0(cls) -> MainClient:
        """L0 orchestrator client."""
        return cls(model=cfg.MODEL, max_tokens=cfg.MAX_TOKENS, _tier="L0-main")
