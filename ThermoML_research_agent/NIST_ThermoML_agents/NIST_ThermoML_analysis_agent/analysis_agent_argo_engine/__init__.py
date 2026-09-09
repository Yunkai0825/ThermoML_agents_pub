"""Analysis-agent ArgoClient factories — registers AnalysisAgentConfig."""
from ...general_db_query_engine.general_argo_engine_helpers.engine_config import load_default_config
from ..ThermoML_analysis_argo_config import AGENT_CONFIG

# Import-time default only — never clobbers an already-active run config
load_default_config(AGENT_CONFIG)

from .argo_client import AnalysisClient  # noqa: F401,E402

__all__ = ["AnalysisClient"]
