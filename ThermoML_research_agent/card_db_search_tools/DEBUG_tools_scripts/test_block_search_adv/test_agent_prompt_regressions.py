"""Prompt-contract regressions for chemistry-agent ``block_search_adv`` inputs.

These cases keep the public contract shallow: every collection is a scalar
string or one flat ``list[str]``.  Mock-ID cases stop at the flat compiler;
live-ID cases reuse the corpus request builders and execution fixture.
"""

from __future__ import annotations

from .conftest import (  # noqa: F401  (fixtures are imported for pytest)
    adv_module,
    missing_value_request,
    reaction_request,
    run_adv,
    target_translation_request,
)

from advanced_block_search.flat_v2 import compile_flat_request


def _flat_request(**overrides):
    request = {
        "compounds": [],
        "compound_match": "all",
        "system_scope": "declared",
        "system_type": None,
        "system_size_min": None,
        "system_size_max": None,
        "parameters": [],
        "targets": ["GLOBprop_34 AS measured_result MIN_FINITE 1"],
        "literature": [],
        "phases": [],
        "phase_match": "all",
        "where": None,
        "fixed_constraints": [],
        "inline_state": [],
        "minimum_common_points": 1,
        "calculate": [],
        "select": ["COUNT(*) AS point_count"],
        "having": None,
        "order_by": [],
        "limit": 50,
        "explanation": "Exercise one corrected chemistry-agent call shape.",
    }
    request.update(overrides)
    return request


def _block_ids(result):
    return [item["block"]["block_id"] for item in result["results"]]


def test_required_solute_with_multiple_any_solvents_lowers_to_and_or():
    """CO2 is required while water or methanol satisfies one solvent OR."""

    compiled = compile_flat_request(
        **_flat_request(
            compounds=[
                "REQUIRE GLOBcomp_3 AS carbon_dioxide",
                "ANY GLOBcomp_1 AS water IN solvent",
                "ANY GLOBcomp_4 AS methanol IN solvent",
            ],
            system_type="binary",
            system_size_min=2,
            system_size_max=2,
            targets=[
                "GLOBprop_34 AS conductivity PHASE GLOBphase_3 "
                "MIN_FINITE 1"
            ],
            explanation=(
                "Find binary carbon dioxide conductivity data using either "
                "water or methanol as the solvent."
            ),
        )
    )

    compound_query = compiled.engine_kwargs["compound_list"]
    assert [item["as"] for item in compound_query["all_of"]] == [
        "carbon_dioxide"
    ]
    assert [item["as"] for item in compound_query["any_of"]] == [
        "water",
        "methanol",
    ]
    assert compound_query["exact_system"] is False


def test_exact_binary_component_qualified_target_executes(run_adv):
    """An exact binary system can bind a target to one named component."""

    result = run_adv(target_translation_request())

    assert _block_ids(result) == ["PROPblock_4"]
    assert result["normalized_query"]["compound_match"] == "exact"
    binding = result["results"][0]["binding_matches"][0]["bindings"][
        "liquid_x"
    ]
    assert binding["component_org_num"] is not None
    assert binding["phase_num_id"] == "GLOBphase_4"


def test_ternary_derived_composition_nested_between_and_direct_having(
    run_adv,
):
    """Derive the third liquid composition and filter both rows and blocks."""

    request = missing_value_request(minimum_count=1)
    request["where"] = (
        "feed_methanol_x BETWEEN 0[1] AND 1[1] AND "
        "((1[1] - ether_x) - methanol_x) "
        "BETWEEN -0.01[1] AND 1.01[1]"
    )
    request["calculate"] = [
        "((1[1] - ether_x) - methanol_x) AS water_x"
    ]
    request["select"] = [
        "MEAN(water_x) AS mean_water_x",
        "COUNT(*) AS complete_rows",
    ]
    request["having"] = (
        "COUNT(*) >= 1 AND "
        "MEAN(water_x) BETWEEN -0.01[1] AND 1.01[1]"
    )

    result = run_adv(request)

    assert _block_ids(result) == ["PROPblock_11"]
    selected = result["results"][0]["binding_matches"][0]["selected"]
    assert set(selected) == {"mean_water_x", "complete_rows"}
    assert selected["complete_rows"]["value"] >= 1


def test_literature_year_and_first_author_clauses_stay_flat():
    compiled = compile_flat_request(
        **_flat_request(
            literature=[
                "YEAR BETWEEN 2005 AND 2015",
                "FIRST_AUTHOR CONTAINS Smith",
            ],
            explanation=(
                "Find reported measurements published from 2005 through "
                "2015 by a first author named Smith."
            ),
        )
    )

    assert compiled.engine_kwargs["literature"] == {
        "year": {"min": 2005, "max": 2015},
        "first_author": "Smith",
    }
    assert compiled.public_query["literature"] == [
        "YEAR BETWEEN 2005 AND 2015",
        "FIRST_AUTHOR CONTAINS Smith",
    ]


def test_component_unspecified_cardinality_each_expands_occurrences():
    """CARDINALITY EACH handles a component-linked quantity left unspecified."""

    target = (
        "GLOBvar_2 AS component_x MIN_FINITE 1 CARDINALITY EACH"
    )
    compiled = compile_flat_request(
        **_flat_request(
            compounds=[
                "REQUIRE GLOBcomp_4 AS methanol",
                "REQUIRE GLOBcomp_4625 AS ether",
                "REQUIRE GLOBcomp_1 AS water",
            ],
            compound_match="exact",
            system_type="ternary",
            system_size_min=3,
            system_size_max=3,
            targets=[target],
            explanation=(
                "Return each reported component mole-fraction occurrence in "
                "the exact methanol, ether, and water ternary system."
            ),
        )
    )

    selector = compiled.engine_kwargs["target_identity"][0]
    assert "component" not in selector
    assert selector["cardinality"] == "all"
    assert compiled.public_query["targets"] == [target]


def test_reaction_inline_state_is_evidence_and_is_not_selected(run_adv):
    """Reaction temperature and pressure remain target-linked evidence."""

    request = reaction_request()
    assert all("ON TARGET reaction_enthalpy" in item for item in request["inline_state"])
    assert request["select"] == [
        "MEAN(reaction_enthalpy) AS mean_reaction_enthalpy"
    ]

    result = run_adv(request)

    assert _block_ids(result) == ["RXNblock_1"]
    match = result["results"][0]["binding_matches"][0]
    assert set(match["selected"]) == {"mean_reaction_enthalpy"}
    evidence = match["fixed_filter_evidence"]
    assert {item["alias"] for item in evidence} == {
        "reaction_temperature",
        "reaction_pressure",
    }
    assert all(
        item["applies_to_occurrence_key"] == "property|BLKprop_1"
        for item in evidence
    )



def test_real_embedded_binary_subsystem_is_exactly_searchable(run_adv):
    result = run_adv(dict(
        targets="GLOBprop_8 AS speed MIN_FINITE 1",
        explanation=(
            "Find the exact alanine plus water binary composition face "
            "embedded in a higher-component speed-of-sound block."
        ),
        compounds=[
            "REQUIRE GLOBcomp_74 AS alanine",
            "REQUIRE GLOBcomp_1 AS water",
        ],
        compound_match="all",
        system_type="binary",
        system_scope="subsystem",
        system_size_min=2,
        system_size_max=2,
        literature="GLOBlit_608",
        minimum_common_points=1,
        select="COUNT(*) AS point_count",
        limit=20,
    ))
    assert result["schema"] == "block_search_adv/result-v1"
    assert result["n_results"] == 1
    row = result["results"][0]
    assert row["block"] == {
        **row["block"],
        "doi": "10.1016/j.fluid.2008.02.015",
        "block_id": "PROPblock_1",
        "BLKsubsys_id": "BLKsubsys_2",
        "search_scope": "subsystem",
        "system_type": "binary",
        "n_components": 2,
        "n_matching_datapoints": 72,
        "declared_system_type": "ternary",
        "declared_n_components": 3,
    }
    evidence = row["match_evidence"]["subsystem"]
    assert [item["comp_num_id"] for item in evidence["retained_components"]] == [
        "GLOBcomp_74", "GLOBcomp_1"
    ]
    assert [item["comp_num_id"] for item in evidence["excluded_components"]] == [
        "GLOBcomp_2004"
    ]
    match = row["binding_matches"][0]
    assert match["selected"]["point_count"]["value"] == 72
    assert match["match_trace"]["point_scope"] == "subsystem_inclusive_runs"
    assert match["match_trace"]["parent_rows"] == 300
