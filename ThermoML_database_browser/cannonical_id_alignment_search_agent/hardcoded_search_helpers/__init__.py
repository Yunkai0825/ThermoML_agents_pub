"""
Hardcoded (deterministic) search helpers — no LLM dependency.

Modules
-------
search_parser          — free-text → SearchBlock  (split on ; and +)
id_workers             — fuzzy ID resolution against canonical registries
dispatcher             — orchestrate parse → resolve → validate → (review → escalate)
bibliography_scorer    — two-pass title + keyword scoring
validation_tools       — field validation against registries
review_workers         — specialised review agents that suggest field edits
"""

from .search_parser import SearchBlock, parse_search_input
from .id_workers import ResolvedID
from .dispatcher import ResolvedQuery, dispatch_search, dispatch_search_validated
from .bibliography_scorer import TitleHit, score_titles

__all__ = [
    "SearchBlock",
    "parse_search_input",
    "ResolvedID",
    "ResolvedQuery",
    "dispatch_search",
    "dispatch_search_validated",
    "TitleHit",
    "score_titles",
]
