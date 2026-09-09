"""Single source of configurable behavior for property screening.

Schema identifiers and parser grammar remain beside their implementations;
every numerical, chemistry-policy, search, cache, and context-window knob is
centralized here.
"""

from __future__ import annotations


# Public request and execution bounds.
MAX_RETURNED_SYSTEMS = 200
DISCOVERY_PAGE_SIZE = 512
CACHE_LOCK_TIMEOUT_SECONDS = 30.0

# Query-agent context compaction.
AGENT_MAX_RANKINGS = 20
AGENT_MAX_DIAGNOSTICS = 12
AGENT_MAX_MARKDOWN_CHARS = 28_000
AGENT_MAX_INLINE_PRIMARY_GRID_PROFILES = 2
AGENT_MAX_SECONDARY_COORDINATES = 10
AGENT_MAX_SECONDARY_RANKINGS_PER_COORDINATE = 4

# Ordered cross-system rankings at regulated composition coordinates other
# than the authoritative primary query coordinate. Every coordinate is a
# separate chemical comparison; equal geometric distance never merges panels.
SECONDARY_RANKING_LIMIT_DIVISOR = 5

# Read-only post-ranking result observer.  This nested ReAct worker may inspect
# the immutable deterministic result and call only the result-local tools
# declared by ``interface/result_observer.py``.  It cannot search databases or
# alter selected curves, interpolated values, baselines, scores, or ranks.
RESULT_OBSERVER_MAX_ITERATIONS = 4
RESULT_OBSERVER_MAX_SECONDS = 120
RESULT_OBSERVER_MAX_TOKENS = 2400
RESULT_OBSERVER_MAX_RANKINGS_PER_INSPECTION = 20
RESULT_OBSERVER_MAX_COMPARISON_RANKS = 6
RESULT_OBSERVER_TOP_RANKINGS_IN_QUALITY_SNAPSHOT = 5
RESULT_OBSERVER_MAX_STRENGTHS = 5
RESULT_OBSERVER_MAX_LIMITATIONS = 6
RESULT_OBSERVER_MAX_CHEMISTRY_INSIGHTS = 5
RESULT_OBSERVER_MAX_FOLLOW_UPS = 5

# Composition grids and strict source-local interpolation.
COMPOSITION_COORDINATE_ATOL = 1e-8
COMPOSITION_CLOSURE_ATOL = 1e-8
COMPOSITION_SELF_CONSISTENCY_ATOL = 1e-6
VOLUMETRIC_BRIDGE_SELF_CONSISTENCY_RTOL = 1e-6
COMPOSITION_SUPPORT_REFERENCE_POINTS = 20.0
COMPOSITION_GROUP_SCORE_WEIGHTS = {
    "coverage": 0.30,
    "support": 0.25,
    "exactness": 0.15,
    "bridge_independence": 0.10,
    "basis_directness": 0.10,
    "parsimony": 0.10,
}
BINARY_AUTO_RANKING_GRID_POINTS = 21
TERNARY_AUTO_RANKING_GRID_DENOMINATOR = 10
HIGHER_AUTO_RANKING_GRID_DENOMINATOR = 4
REGULATED_COMPOSITION_AXIS = (
    0.0,
    0.001,
    0.01,
    0.1,
    0.25,
    0.5,
    0.75,
    0.9,
    0.99,
    0.999,
    1.0,
)

# Soft state matching. Explicit user ±/tol values always override these rules.
# log10=0.1 means a multiplicative pressure window of 10**0.1 (~1.2589)
# on both sides, which is symmetric in log-pressure space.
SOFT_TOLERANCE_BY_QUANTITY = {
    "temperature_k": {"kind": "additive", "value": 5.0},
    "pressure_kpa": {"kind": "log10", "value": 0.1},
}
SOFT_TOLERANCE_BY_CANONICAL_UNIT = {
    "K": {"kind": "additive", "value": 5.0},
    "kPa": {"kind": "log10", "value": 0.1},
    "1": {"kind": "additive", "value": 0.01},
}
DEFAULT_SOFT_TOLERANCE = {
    "kind": "relative",
    "value": 0.05,
    "absolute_floor": 1e-12,
}
CONSTRAINT_PROXIMITY_AT_SOFT_LIMIT = 0.25

# Composite source evidence. Chemical compatibility remains a hard gate;
# these weights describe the quality of one reported block-local curve and
# do not make incompatible evidence usable.
PROPERTY_SUPPORT_REFERENCE_POINTS = 20.0
PROPERTY_SOURCE_SCORE_WEIGHTS = {
    "support": 0.20,
    "composition_coverage": 0.15,
    "constraint_proximity": 0.25,
    "composition_reliability": 0.20,
    "uncertainty_reporting": 0.10,
    "target_directness": 0.10,
}
# Whole-curve property selection. One experimental block is selected for each
# comparable system/property/state group; independent blocks are never
# averaged pointwise. Primary-grid coverage is evaluated before selection so
# a high-quality curve that cannot answer the confirmed query cannot perturb
# the primary result; it can be retained only for regulated-coordinate context.
PROPERTY_CURVE_SELECTION_SCORE_WEIGHTS = {
    "support": 0.16,
    "composition_coverage": 0.12,
    "selection_grid_coverage": 0.20,
    "constraint_proximity": 0.20,
    "composition_reliability": 0.16,
    "uncertainty_reporting": 0.08,
    "target_directness": 0.08,
}
# Ranking numerical equality.
RANKING_SCORE_SIGNIFICANT_DIGITS = 12
RANKING_SCORE_ABSOLUTE_TOLERANCE = 1e-12
RANKING_SCORE_RELATIVE_TOLERANCE = 1e-12

# Deterministic volume-density-molar dependency graph.  These IDs are looked
# up as evidence whenever any member is the ranking target.  Transformations
# remain chemically gated by composition, molecular mass, phase/state, and
# (for excess/real conversion) unary molar-volume availability.
VOLUMETRIC_EVIDENCE_GLOBAL_IDS = {
    "GLOBprop_1": (
        "GLOBprop_1", "GLOBprop_41", "GLOBprop_28",
        "GLOBprop_67", "GLOBprop_74",
    ),
    "GLOBprop_28": (
        "GLOBprop_28", "GLOBprop_41", "GLOBprop_1",
        "GLOBprop_67", "GLOBprop_74",
    ),
    "GLOBprop_41": (
        "GLOBprop_41", "GLOBprop_28", "GLOBprop_1",
        "GLOBprop_67", "GLOBprop_74",
    ),
    "GLOBprop_67": (
        "GLOBprop_67", "GLOBprop_41", "GLOBprop_28",
        "GLOBprop_1", "GLOBprop_74",
    ),
    "GLOBprop_74": (
        "GLOBprop_74", "GLOBprop_1", "GLOBprop_41",
        "GLOBprop_28", "GLOBprop_67",
    ),
}

# Baseline chemistry policies.
LINEAR_MOLAR_BASELINE_PREFIXES = (
    "molar_volume",
    "molar_enthalpy",
    "molar_internal_energy",
    "molar_entropy",
    "molar_heat_capacity",
)
NO_UNIVERSAL_IDEAL_MARKERS = (
    "viscosity",
    "speed_of_sound",
    "thermal_conductivity",
    "electrical_conductivity",
    "diffusion",
    "surface_tension",
)

def runtime_settings_snapshot() -> dict:
    """Return the exact JSON-safe configuration recorded with every run."""
    return {
        "max_returned_systems": MAX_RETURNED_SYSTEMS,
        "discovery_page_size": DISCOVERY_PAGE_SIZE,
        "cache_lock_timeout_seconds": CACHE_LOCK_TIMEOUT_SECONDS,
        "agent_max_rankings": AGENT_MAX_RANKINGS,
        "agent_max_diagnostics": AGENT_MAX_DIAGNOSTICS,
        "agent_max_markdown_chars": AGENT_MAX_MARKDOWN_CHARS,
        "agent_max_inline_primary_grid_profiles": (
            AGENT_MAX_INLINE_PRIMARY_GRID_PROFILES
        ),
        "agent_max_secondary_coordinates": (
            AGENT_MAX_SECONDARY_COORDINATES
        ),
        "agent_max_secondary_rankings_per_coordinate": (
            AGENT_MAX_SECONDARY_RANKINGS_PER_COORDINATE
        ),
        "secondary_ranking_limit_divisor": (
            SECONDARY_RANKING_LIMIT_DIVISOR
        ),
        "result_observer_max_iterations": RESULT_OBSERVER_MAX_ITERATIONS,
        "result_observer_max_seconds": RESULT_OBSERVER_MAX_SECONDS,
        "result_observer_max_tokens": RESULT_OBSERVER_MAX_TOKENS,
        "result_observer_max_rankings_per_inspection": (
            RESULT_OBSERVER_MAX_RANKINGS_PER_INSPECTION
        ),
        "result_observer_max_comparison_ranks": (
            RESULT_OBSERVER_MAX_COMPARISON_RANKS
        ),
        "result_observer_top_rankings_in_quality_snapshot": (
            RESULT_OBSERVER_TOP_RANKINGS_IN_QUALITY_SNAPSHOT
        ),
        "result_observer_max_strengths": RESULT_OBSERVER_MAX_STRENGTHS,
        "result_observer_max_limitations": RESULT_OBSERVER_MAX_LIMITATIONS,
        "result_observer_max_chemistry_insights": (
            RESULT_OBSERVER_MAX_CHEMISTRY_INSIGHTS
        ),
        "result_observer_max_follow_ups": RESULT_OBSERVER_MAX_FOLLOW_UPS,
        "composition_coordinate_atol": COMPOSITION_COORDINATE_ATOL,
        "composition_closure_atol": COMPOSITION_CLOSURE_ATOL,
        "composition_self_consistency_atol": (
            COMPOSITION_SELF_CONSISTENCY_ATOL
        ),
        "volumetric_bridge_self_consistency_rtol": (
            VOLUMETRIC_BRIDGE_SELF_CONSISTENCY_RTOL
        ),
        "composition_support_reference_points": (
            COMPOSITION_SUPPORT_REFERENCE_POINTS
        ),
        "composition_group_score_weights": (
            COMPOSITION_GROUP_SCORE_WEIGHTS
        ),
        "binary_auto_ranking_grid_points": BINARY_AUTO_RANKING_GRID_POINTS,
        "ternary_auto_ranking_grid_denominator": (
            TERNARY_AUTO_RANKING_GRID_DENOMINATOR
        ),
        "higher_auto_ranking_grid_denominator": (
            HIGHER_AUTO_RANKING_GRID_DENOMINATOR
        ),
        "regulated_composition_axis": list(REGULATED_COMPOSITION_AXIS),
        "soft_tolerance_by_quantity": SOFT_TOLERANCE_BY_QUANTITY,
        "soft_tolerance_by_canonical_unit": (
            SOFT_TOLERANCE_BY_CANONICAL_UNIT
        ),
        "default_soft_tolerance": DEFAULT_SOFT_TOLERANCE,
        "constraint_proximity_at_soft_limit": (
            CONSTRAINT_PROXIMITY_AT_SOFT_LIMIT
        ),
        "property_support_reference_points": (
            PROPERTY_SUPPORT_REFERENCE_POINTS
        ),
        "property_source_score_weights": PROPERTY_SOURCE_SCORE_WEIGHTS,
        "property_curve_selection_score_weights": (
            PROPERTY_CURVE_SELECTION_SCORE_WEIGHTS
        ),
        "ranking_score_significant_digits": (
            RANKING_SCORE_SIGNIFICANT_DIGITS
        ),
        "ranking_score_absolute_tolerance": (
            RANKING_SCORE_ABSOLUTE_TOLERANCE
        ),
        "ranking_score_relative_tolerance": (
            RANKING_SCORE_RELATIVE_TOLERANCE
        ),
        "volumetric_evidence_global_ids": {
            key: list(value)
            for key, value in VOLUMETRIC_EVIDENCE_GLOBAL_IDS.items()
        },
        "linear_molar_baseline_prefixes": list(
            LINEAR_MOLAR_BASELINE_PREFIXES
        ),
        "no_universal_ideal_markers": list(
            NO_UNIVERSAL_IDEAL_MARKERS
        ),
    }
