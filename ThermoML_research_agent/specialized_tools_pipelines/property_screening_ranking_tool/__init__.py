"""ThermoML property-screening and ranking pipeline.

The public runtime surface is deliberately one tool:
:func:`screen_property_systems`.  Scientific selection, normalization,
interpolation, baselines, and ranking are deterministic pipeline stages.  A
bounded read-only ReAct observer can comment on the completed result but cannot
search databases or mutate those authoritative stages.  The search catalog
reused by this package still imports its normalization helpers as a top-level
package, so its owning directory is registered once here before the
orchestrator is imported.
"""

from __future__ import annotations

import sys
from pathlib import Path


_QUERY_ROOT = Path(__file__).resolve().parents[2]
_BASIC_SEARCH_ROOT = _QUERY_ROOT / "card_db_search_tools" / "basic_search_tools"
if str(_BASIC_SEARCH_ROOT) not in sys.path:
    sys.path.insert(0, str(_BASIC_SEARCH_ROOT))

__all__ = ["screen_property_systems"]


def __getattr__(name: str):
    """Load the heavy orchestration tool only when its public symbol is used."""
    if name != "screen_property_systems":
        raise AttributeError(name)
    from .tool import screen_property_systems
    return screen_property_systems
