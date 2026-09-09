"""Strict numeric-range validation for ThermoML search tools."""


def validate_range(val: list[float] | None, *, field: str) -> tuple[float, float] | None:
    """Validate one exact two-number JSON array without string coercion."""
    if val is None:
        return None
    if not isinstance(val, list) or len(val) != 2:
        raise TypeError(
            f"TOOL_ARGUMENT_REFINEMENT_REQUIRED: {field} must be a JSON array "
            "with exactly two numeric values [minimum, maximum]"
        )
    if any(isinstance(item, bool) or not isinstance(item, (int, float)) for item in val):
        raise TypeError(
            f"TOOL_ARGUMENT_REFINEMENT_REQUIRED: {field} values must be JSON numbers"
        )
    lo, hi = float(val[0]), float(val[1])
    if lo > hi:
        raise ValueError(
            f"TOOL_ARGUMENT_REFINEMENT_REQUIRED: {field} minimum exceeds maximum"
        )
    return lo, hi


def ranges_overlap(data_range, query_range: tuple[float, float]) -> bool:
    """Return True if two (min, max) ranges overlap.

    *data_range* must be the database's exact two-number array;
    *query_range* is always a 2-element (lo, hi).
    """
    if not isinstance(data_range, (list, tuple)) or len(data_range) != 2:
        raise ValueError(f"Malformed database range: {data_range!r}")
    d_lo, d_hi = data_range
    if d_lo is None or d_hi is None:
        return False
    if any(isinstance(item, bool) or not isinstance(item, (int, float)) for item in (d_lo, d_hi)):
        raise ValueError(f"Malformed non-numeric database range: {data_range!r}")
    d_lo, d_hi = float(d_lo), float(d_hi)
    q_lo, q_hi = query_range
    return d_lo <= q_hi and d_hi >= q_lo
