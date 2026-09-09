"""
Normalization helpers for ThermoML search tools.

Resolves free-text agent inputs (names, formulas, SMILES, DOIs, etc.)
to canonical IDs used in the card databases.
"""

from .resolve import (
    resolve_compound,
    resolve_property,
    resolve_measurement,
    resolve_reference,
    resolve_variable,
    resolve_constraint,
    resolve_phase,
    resolve_solvent,
    resolve_block_type,
    resolve_reaction_type,
)
from .paths import (
    card_db_path,
    registry_db_path,
    csv_path,
    CARD_DBS,
    REGISTRY_DBS,
    CSV_FILES,
)
from .compact import compact_card, compact_block
from .comp_alias import expand_comp_alias
from .prop_alias import expand_prop_alias
from .meas_alias import expand_meas_alias
from .var_alias import expand_var_alias
from .constr_alias import expand_constr_alias
from .range_helpers import validate_range, ranges_overlap
from .registry_parsers import (
    parse_json_array_col,
    parse_comp_ids_smiles,
    parse_var_ids_ranges,
    parse_prop_ids_meas_ranges,
    parse_phase_ids,
    parse_constr_ids_values,
    parse_participants,
    parse_reaction_type,
    format_pm_row,
    format_rxn_row,
    build_prop_patterns,
)
from .purity_helpers import best_purity
from .compound_id_helpers import (
    resolve_comp_in_id,
    build_column_map,
    build_compound_map,
    extract_comp_ref,
)
from .db_helpers import open_db

__all__ = [
    "resolve_compound",
    "resolve_property",
    "resolve_measurement",
    "resolve_reference",
    "resolve_variable",
    "resolve_constraint",
    "resolve_phase",
    "resolve_solvent",
    "resolve_block_type",
    "resolve_reaction_type",
    "card_db_path",
    "registry_db_path",
    "csv_path",
    "CARD_DBS",
    "REGISTRY_DBS",
    "CSV_FILES",
    "compact_card",
    "compact_block",
    "expand_comp_alias",
    "expand_prop_alias",
    "expand_meas_alias",
    "expand_var_alias",
    "expand_constr_alias",
    # Range helpers
    "validate_range",
    "ranges_overlap",
    # Registry parsers
    "parse_json_array_col",
    "parse_comp_ids_smiles",
    "parse_var_ids_ranges",
    "parse_prop_ids_meas_ranges",
    "parse_phase_ids",
    "parse_constr_ids_values",
    "parse_participants",
    "parse_reaction_type",
    "format_pm_row",
    "format_rxn_row",
    "build_prop_patterns",
    # Purity helpers
    "best_purity",
    # Compound ID helpers
    "resolve_comp_in_id",
    "build_column_map",
    "build_compound_map",
    "extract_comp_ref",
    # DB helpers
    "open_db",
]
