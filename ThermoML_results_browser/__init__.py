"""ThermoML results browser beside its research-agent project."""
from pathlib import Path
import sys

_RESEARCH_ROOT = Path(__file__).resolve().parents[1] / "ThermoML_research_agent"
if str(_RESEARCH_ROOT) not in sys.path:
    sys.path.insert(0, str(_RESEARCH_ROOT))
