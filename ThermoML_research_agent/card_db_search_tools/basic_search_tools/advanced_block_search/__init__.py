"""Private implementation package behind ``block_search_adv``."""

from .errors import AdvancedSearchError
from .flat_v2 import flat_error_result
from .lifecycle import (
    REVIEW_SCHEMA,
    assess_flat_search,
    render_review_markdown,
    review_or_execute_flat_search,
    validate_block_search_adv_guidance,
)

__all__ = [
    "AdvancedSearchError",
    "REVIEW_SCHEMA",
    "assess_flat_search",
    "flat_error_result",
    "render_review_markdown",
    "review_or_execute_flat_search",
    "validate_block_search_adv_guidance",
]