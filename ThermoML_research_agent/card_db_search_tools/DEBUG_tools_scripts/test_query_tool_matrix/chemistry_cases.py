"""Verified real-corpus inputs for the query-tool chemistry matrix."""

from __future__ import annotations

from typing import Any


DOI_CO2 = "10.1007/s10765-005-5566-6"
CO2_BLOCK = "PROPblock_1"
DOI_REACTION = "10.1007/s10765-009-0568-4"
REACTION_BLOCK = "RXNblock_1"


ADV_CO2: dict[str, Any] = {
    "compounds": "GLOBcomp_3 AS carbon_dioxide",
    "compound_match": "exact",
    "system_type": "unary",
    "system_size_min": 1,
    "system_size_max": 1,
    "parameters": [
        (
            "GLOBconstr_2 AS temperature PHASE GLOBphase_3 "
            "MIN_FINITE 4 MIN_DISTINCT 2"
        ),
        (
            "GLOBconstr_1 AS pressure PHASE GLOBphase_3 "
            "MIN_FINITE 4 MIN_DISTINCT 2"
        ),
    ],
    "targets": (
        "GLOBprop_34 AS conductivity PHASE GLOBphase_3 MIN_FINITE 4"
    ),
    "literature": f"DOI={DOI_CO2}",
    "phases": "GLOBphase_3",
    "where": (
        "temperature BETWEEN 151.85[degC] AND 155.85[degC] "
        "AND pressure BETWEEN 1[MPa] AND 5[MPa]"
    ),
    "minimum_common_points": 4,
    "select": "MEAN(conductivity) AS mean_conductivity",
    "limit": 5,
    "explanation": (
        "Average four aligned gas-phase carbon dioxide conductivity rows "
        "over the requested temperature and pressure interval."
    ),
}


ADV_REACTION: dict[str, Any] = {
    "compounds": "GLOBcomp_7883 AS potassium_benzoate IN any",
    "targets": "GLOBprop_36 AS reaction_enthalpy MIN_FINITE 1",
    "literature": f"DOI={DOI_REACTION}",
    "inline_state": [
        (
            "GLOBvar_1 AS reaction_temperature ON TARGET "
            "reaction_enthalpy WHERE VALUE BETWEEN 298[K] AND 299[K]"
        ),
        (
            "GLOBconstr_1 AS reaction_pressure ON TARGET "
            "reaction_enthalpy WHERE VALUE BETWEEN 199[kPa] AND 201[kPa]"
        ),
    ],
    "where": "reaction_enthalpy <= -600[kJ/mol]",
    "minimum_common_points": 1,
    "select": (
        "MEAN(reaction_enthalpy) AS mean_reaction_enthalpy"
    ),
    "limit": 5,
    "explanation": (
        "Find the reported potassium-benzoate reaction enthalpy at its "
        "target-scoped inline temperature and pressure."
    ),
}


L1_LIVE_CASES: dict[str, dict[str, Any]] = {
    "resolve_ids": {
        "entity_type": "variable",
        "queries": ["temperature", "pressure", "mole fraction"],
        "min_score": 50,
        "limit": 5,
    },
    "resolve_compound_ids": {
        "queries": ["water", "carbon dioxide", "methanol"],
        "min_score": 90,
        "limit": 5,
    },
    "resolve_property_ids": {
        "queries": ["mass density", "viscosity", "thermal conductivity"],
        "min_score": 90,
        "limit": 5,
    },
    "resolve_measurement_ids": {
        "queries": ["DSC", "hot wire"],
        "min_score": 50,
        "limit": 5,
    },
    "resolve_reference_ids": {
        "queries": DOI_CO2,
        "min_score": 90,
        "limit": 5,
    },
    "search_id_alignment": {
        "entity_type": "property",
        "query": "thermal conductivity",
        "limit": 10,
    },
    "search_blocks": {
        "compound": "GLOBcomp_3",
        "property": "GLOBprop_34",
        "literature": DOI_CO2,
        "system_type": "unary",
        "phase": "GLOBphase_3",
        "temperature_range": [425.0, 429.0],
        "pressure_range": [1000.0, 5000.0],
        "limit": 5,
    },
    "block_search_adv": ADV_CO2,
    "search_system_registry": {
        "compound": "GLOBcomp_7883",
        "property": "GLOBprop_36",
        "block_type": "ReactionData",
        "literature": DOI_REACTION,
        "include_reactions": True,
        "limit": 10,
    },
    "search_system_summary": {
        "compound": "GLOBcomp_3",
        "property": "GLOBprop_34",
        "system_type": "unary",
        "include_reactions": False,
        "limit": 5,
    },
    "search_similar_compounds": {
        "comp_num_id": "GLOBcomp_4",
        "top_k": 5,
        "min_similarity": 0.2,
        "metric": "morgan",
    },
}


L2_LIVE_CASES: dict[str, tuple[str, dict[str, Any]]] = {
    "search_comp_from_block": (
        "compound",
        {"doi": DOI_CO2, "block_number": CO2_BLOCK},
    ),
    "search_compound_dk": (
        "compound",
        {"compound": "GLOBcomp_3", "limit": 2},
    ),
    "search_compound_indiv": (
        "compound",
        {"compound": "GLOBcomp_3", "literature": DOI_CO2, "limit": 2},
    ),
    "search_meas_from_block": (
        "measurement",
        {"doi": DOI_CO2, "block_number": CO2_BLOCK},
    ),
    "search_measurement_dk": (
        "measurement",
        {"measurement": "GLOBmeas_41", "limit": 2},
    ),
    "search_measurement_indiv": (
        "measurement",
        {
            "literature": DOI_CO2,
            "property": "GLOBprop_34",
            "limit": 5,
        },
    ),
    "search_prop_dk_from_block": (
        "property",
        {"doi": DOI_CO2, "block_number": CO2_BLOCK},
    ),
    "search_property_dk": (
        "property",
        {"property": "GLOBprop_34", "limit": 2},
    ),
    "search_reference_from_block": (
        "reference",
        {"doi": DOI_CO2, "block_number": CO2_BLOCK},
    ),
    "search_references": (
        "reference",
        {"literature": DOI_CO2, "limit": 2},
    ),
}
