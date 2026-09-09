"""
AnalysisClient — ArgoClient subclass for the ThermoML Analysis Agent.
=====================================================================
Subclasses the shared ``ArgoClient`` from ``argo_engine_helpers`` and
adds factory methods (``for_l0``, ``for_l1_data``, ``for_l1_fit``)
that read defaults from ``ThermoML_analysis_argo_config.AGENT_CONFIG``.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Any

from ...general_db_query_engine.general_argo_engine_helpers import ArgoClient as _BaseClient
from ..ThermoML_analysis_argo_config import AGENT_CONFIG as cfg

log = logging.getLogger("AnalysisArgoClient")


@dataclass
class AnalysisClient(_BaseClient):
    """ArgoClient configured for the analysis agent."""

    model: str = cfg.MODEL
    temperature: float = cfg.TEMPERATURE
    top_p: float = cfg.TOP_P
    max_tokens: int = cfg.MAX_TOKENS

    @classmethod
    def for_l0(cls) -> "AnalysisClient":
        return cls(model=cfg.MODEL, max_tokens=cfg.MAX_TOKENS, _tier="L0-main")

    @classmethod
    def for_l1_data(cls) -> "AnalysisClient":
        return cls(model=cfg.L1_MODEL, max_tokens=cfg.MAX_TOKENS, _tier="L1-subagent")

    @classmethod
    def for_l1_fit(cls) -> "AnalysisClient":
        return cls(model=cfg.L1_MODEL, max_tokens=cfg.MAX_TOKENS, _tier="L1-fit")
