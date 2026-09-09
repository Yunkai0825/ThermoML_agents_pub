"""Database discovery and authoritative block reconstruction."""

from .discovery import discover_candidates
from .reader import (
    AuthoritativeBlock,
    AuthoritativeBlockReader,
    BlockGatheringResult,
    gather_authoritative_blocks,
)

__all__ = [
    "AuthoritativeBlock",
    "AuthoritativeBlockReader",
    "BlockGatheringResult",
    "discover_candidates",
    "gather_authoritative_blocks",
]
