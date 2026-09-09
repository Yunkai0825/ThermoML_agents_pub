"""
AlignmentClient — ArgoClient with alignment-agent-specific factory methods.
==========================================================================
"""
from __future__ import annotations

from dataclasses import dataclass

from NIST_ThermoML_agents.general_db_query_engine.general_argo_engine_helpers import ArgoClient
from ..alignment_agent_argo_config import AGENT_CONFIG as cfg


@dataclass
class AlignmentClient(ArgoClient):
    """ArgoClient configured for the canonical ID alignment agent."""

    @classmethod
    def for_l0(cls) -> AlignmentClient:
        """L0 orchestrator client — main ReAct loop."""
        return cls(model=cfg.MODEL, max_tokens=cfg.MAX_TOKENS, _tier="L0-alignment")
