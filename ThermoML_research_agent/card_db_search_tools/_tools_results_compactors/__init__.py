"""
card_search_tools_results_compactors — shared dict→markdown compactors.
=======================================================================
Each search tool in card_db_search_tools can import its compactor from
here and apply it *before* returning results to any agent.

Public API
----------
COMPACTOR_FUNCTIONS : list[callable]
    All tagged compactor functions.  Each has ``fn._compacts_tools``
    indicating which tools it serves.  Use
    ``CompactorCatalog.from_functions(COMPACTOR_FUNCTIONS)`` to build.
"""

from __future__ import annotations

from .basic_search_tools.compactors import (
    compact_resolve_compound_ids,
    compact_resolve_property_ids,
    compact_resolve_measurement_ids,
    compact_resolve_reference_ids,
    compact_resolve_variable_ids,
    compact_resolve_constraint_ids,
    compact_resolve_phase_ids,
    compact_resolve_solvent_ids,
    compact_resolve_ids,
    compact_search_id_alignment,
    compact_search_blocks,
    compact_search_system_registry,
    compact_search_system_summary,
    compact_search_similar_compounds,
    compact_search_compound_dk,
    compact_search_property_dk,
    compact_search_measurement_dk,
    compact_search_references,
    compact_search_compound_indiv,
    compact_search_measurement_indiv,
    compact_extract_block_csv,
    compact_extract_multi_block_csv,
    compact_resolve_card_md,
    compact_inspect_block_table,
)
from .basic_search_tools.block_search_adv_compactor import (
    compact_block_search_adv,
)
from .block_centric_search_tools.compactors import (
    compact_search_comp_from_block,
    compact_search_meas_from_block,
    compact_search_prop_dk_from_block,
    compact_search_reference_from_block,
)
from specialized_tools_pipelines.property_screening_ranking_tool.interface.agent import (
    compact_screen_property_systems,
)


# ═══════════════════════════════════════════════════════════════
#  COMPACTOR_FUNCTIONS — all tagged compactor callables
# ═══════════════════════════════════════════════════════════════

COMPACTOR_FUNCTIONS = [
    # ID resolution
    compact_resolve_ids,
    compact_resolve_compound_ids,
    compact_resolve_property_ids,
    compact_resolve_measurement_ids,
    compact_resolve_reference_ids,
    compact_resolve_variable_ids,
    compact_resolve_constraint_ids,
    compact_resolve_phase_ids,
    compact_resolve_solvent_ids,
    compact_search_id_alignment,
    # Block / Registry / Summary
    compact_search_blocks,
    compact_block_search_adv,
    compact_search_system_registry,
    compact_search_system_summary,
    # Compound similarity
    compact_search_similar_compounds,
    compact_search_compound_dk,
    compact_search_property_dk,
    compact_search_measurement_dk,
    compact_search_references,
    compact_search_compound_indiv,
    compact_search_measurement_indiv,
    compact_extract_block_csv,
    compact_extract_multi_block_csv,
    compact_resolve_card_md,
    compact_inspect_block_table,
    # Block-centric
    compact_search_comp_from_block,
    compact_search_meas_from_block,
    compact_search_prop_dk_from_block,
    compact_search_reference_from_block,
    # Specialized property screening/ranking
    compact_screen_property_systems,
]
