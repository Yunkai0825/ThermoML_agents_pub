"""ThermoML browser with imports anchored to the migrated project location."""

import sys
from pathlib import Path

_REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
_PROJECT_ROOT = _REPOSITORY_ROOT / "ThermoML_research_agent"
for _root in (_PROJECT_ROOT, _REPOSITORY_ROOT):
    if str(_root) not in sys.path:
        sys.path.insert(0, str(_root))
