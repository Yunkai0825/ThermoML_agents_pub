"""End-to-end tests against audited PCS cards and raw ThermoML records."""

from __future__ import annotations

import pytest

from .conftest import (
    binary_ranking_request,
    fixed_filter,
    missing_value_request,
    reaction_request,
    selector,
    target_translation_request,
    unary_request,
)


def _block_id(result_row: dict) -> str:
    return result_row["block"]["block_id"]


def _only_match(result_row: dict) -> dict:
    matches = result_row["binding_matches"]
    assert len(matches) == 1
    return matches[0]


def _selected_value(binding_match: dict, alias: str) -> float:
    selected = binding_match["selected"][alias]
    assert isinstance(selected, dict)
    assert isinstance(selected["value"], (int, float))
    assert isinstance(selected.get("unit"), str)
    return float(selected["value"])


def _fixed_evidence(binding_match: dict) -> dict[str, dict]:
    evidence = binding_match["fixed_filter_evidence"]
    assert isinstance(evidence, list)
    return {row["alias"]: row for row in evidence}


def _alias_resolution(result: dict, input_id: str) -> dict:
    matches = [
        row
        for row in result["alias_resolution"]
        if row["input"] == input_id
    ]
    assert len(matches) == 1
    return matches[0]


def test_unary_query_materializes_rows_beyond_card_display_cap(
    unary_result,
):
    assert len(unary_result["results"]) == 1
    row = unary_result["results"][0]
    match = _only_match(row)
    assert row["block"] == {
        **row["block"],
        "doi": "10.1007/s10765-005-5566-6",
        "block_id": "PROPblock_1",
        "source_block_number": 1,
        "block_type": "PureOrMixtureData",
        "system_type": "unary",
    }
    assert match["match_trace"]["rows_before_where"] == 77
    assert match["match_trace"]["rows_after_where"] == 4
    assert match["matched_complete_points"] == 4
    assert match["complete_point_aliases"] == [
        "temperature",
        "pressure",
        "conductivity",
    ]
    assert _selected_value(match, "mean_conductivity") == pytest.approx(
        0.0283025,
        rel=1e-12,
        abs=1e-15,
    )

    assert match["bindings"]["temperature"]["source_role"] == "variable"
    assert (
        match["bindings"]["temperature"]["occurrence_key"]
        == "variable|BLKvar_1"
    )
    assert (
        match["bindings"]["temperature"]["input_identity"]
        == "GLOBconstr_2"
    )
    assert match["bindings"]["pressure"]["source_role"] == "variable"
    assert (
        match["bindings"]["pressure"]["occurrence_key"]
        == "variable|BLKvar_2"
    )
    assert (
        match["bindings"]["pressure"]["input_identity"]
        == "GLOBconstr_1"
    )

    temperature = _alias_resolution(unary_result, "GLOBconstr_2")
    assert temperature["input_catalog_role"] == "constraint"
    assert temperature["quantity_key"] == "temperature_k"
    assert set(temperature["available_global_ids"]) == {
        "GLOBvar_1",
        "GLOBconstr_2",
    }


def test_unary_minimum_points_is_applied_after_exact_where(run_adv):
    result = run_adv(unary_request(minimum_count=5))
    assert result["results"] == []
    assert result["diagnostics"]["minimum_point_rejections"] >= 1


def test_binary_role_translation_constraints_nested_math_and_sorting(
    binary_result,
):
    rows = binary_result["results"]
    assert [_block_id(row) for row in rows] == [
        "PROPblock_1",
        "PROPblock_4",
        "PROPblock_7",
    ]
    expected = {
        "PROPblock_1": (3, 24.88804929385309),
        "PROPblock_4": (4, 12.945066607168359),
        "PROPblock_7": (4, 9.722671646438744),
    }
    assert len(
        {
            (
                row["block"]["doi"],
                row["block"]["block_id"],
                _only_match(row)["bindings"]["x_ionic_liquid"][
                    "occurrence_key"
                ],
                _only_match(row)["bindings"]["h_excess"]["occurrence_key"],
            )
            for row in rows
        }
    ) == len(rows)

    for row in rows:
        match = _only_match(row)
        complete, selected = expected[_block_id(row)]
        assert match["match_trace"]["rows_before_where"] == 5
        assert match["match_trace"]["rows_after_where"] == complete
        assert match["matched_complete_points"] == complete
        assert _selected_value(match, "mean_scaled_h") == pytest.approx(
            selected,
            rel=1e-12,
            abs=1e-12,
        )
        composition = match["bindings"]["x_ionic_liquid"]
        assert composition["source_role"] == "variable"
        assert composition["occurrence_key"] == "variable|BLKvar_1"
        assert composition["input_identity"] == "GLOBconstr_3"
        target = match["bindings"]["h_excess"]
        assert target["source_role"] == "property"
        assert target["occurrence_key"] == "property|BLKprop_1"

        evidence = _fixed_evidence(match)
        assert evidence["pressure_constraint"]["source_role"] == "constraint"
        assert (
            evidence["pressure_constraint"]["occurrence_key"]
            == "constraint|BLKconstr_1"
        )
        assert evidence["pressure_constraint"]["value"] == pytest.approx(101.3)
        assert (
            evidence["temperature_constraint"]["occurrence_key"]
            == "constraint|BLKconstr_2"
        )
        assert evidence["temperature_constraint"]["value"] == pytest.approx(
            298.15
        )

    composition_resolution = _alias_resolution(
        binary_result,
        "GLOBconstr_3",
    )
    assert composition_resolution["input_catalog_role"] == "constraint"
    assert composition_resolution["quantity_key"] == (
        "mole_fraction_{DOIcomp_id}"
    )
    assert set(composition_resolution["available_global_ids"]) == {
        "GLOBprop_2",
        "GLOBvar_2",
        "GLOBconstr_3",
    }


@pytest.mark.parametrize(
    "input_id",
    ["GLOBprop_2", "GLOBvar_2", "GLOBconstr_3"],
)
def test_parameter_alias_permutations_return_one_copy_per_binding(
    run_adv,
    input_id,
):
    result = run_adv(
        binary_ranking_request(mole_fraction_id=input_id)
    )
    rows = result["results"]
    assert [_block_id(row) for row in rows] == [
        "PROPblock_1",
        "PROPblock_4",
        "PROPblock_7",
    ]
    assert len(
        {
            (
                row["block"]["doi"],
                row["block"]["block_id"],
                _only_match(row)["bindings"]["x_ionic_liquid"][
                    "occurrence_key"
                ],
            )
            for row in rows
        }
    ) == 3
    assert all(
        _only_match(row)["bindings"]["x_ionic_liquid"]["source_role"]
        == "variable"
        for row in rows
    )


def test_binary_minimum_points_and_limit_are_stable(run_adv):
    four_points = run_adv(binary_ranking_request(minimum_count=4))
    assert [_block_id(row) for row in four_points["results"]] == [
        "PROPblock_4",
        "PROPblock_7",
    ]

    five_points = run_adv(binary_ranking_request(minimum_count=5))
    assert five_points["results"] == []

    limited = run_adv(binary_ranking_request(limit=2))
    assert [_block_id(row) for row in limited["results"]] == [
        "PROPblock_1",
        "PROPblock_4",
    ]
    assert limited["truncated"] is True
    assert limited["total_matching_blocks_before_limit"] == 3


@pytest.mark.parametrize(
    "target_id",
    ["GLOBprop_2", "GLOBvar_2", "GLOBconstr_3"],
)
def test_target_translation_retains_property_role_and_exponential_math(
    run_adv,
    target_id,
):
    result = run_adv(target_translation_request(target_id=target_id))
    assert len(result["results"]) == 1
    row = result["results"][0]
    match = _only_match(row)
    assert _block_id(row) == "PROPblock_4"
    target = match["bindings"]["liquid_x"]
    assert target["source_role"] == "property"
    assert target["occurrence_key"] == "property|BLKprop_1"
    assert target["input_identity"] == target_id
    assert match["match_trace"]["rows_before_where"] == 4
    assert match["match_trace"]["rows_after_where"] == 2
    assert match["matched_complete_points"] == 2
    assert _selected_value(match, "mean_x_roundtrip") == pytest.approx(
        0.742,
        rel=1e-12,
        abs=1e-15,
    )


def test_target_translation_minimum_points_rejects_three(run_adv):
    result = run_adv(target_translation_request(minimum_count=3))
    assert result["results"] == []


def test_reaction_inline_state_is_target_scoped_and_type_safe(
    reaction_result,
):
    assert len(reaction_result["results"]) == 1
    row = reaction_result["results"][0]
    match = _only_match(row)
    assert row["block"]["doi"] == "10.1007/s10765-009-0568-4"
    assert row["block"]["block_id"] == "RXNblock_1"
    assert row["block"]["source_block_number"] == 1
    assert row["block"]["block_type"] == "ReactionData"
    assert match["bindings"]["reaction_enthalpy"]["source_role"] == "property"
    assert (
        match["bindings"]["reaction_enthalpy"]["occurrence_key"]
        == "property|BLKprop_1"
    )
    assert match["matched_complete_points"] == 1
    assert _selected_value(
        match,
        "mean_reaction_enthalpy",
    ) == pytest.approx(-610.94)

    evidence = _fixed_evidence(match)
    assert set(evidence) == {
        "reaction_temperature",
        "reaction_pressure",
    }
    expected = {
        "reaction_temperature": (
            "inline_state|BLKprop_1|temperature_K",
            298.15,
        ),
        "reaction_pressure": (
            "inline_state|BLKprop_1|pressure_kPa",
            200.0,
        ),
    }
    for alias, (occurrence, value) in expected.items():
        item = evidence[alias]
        assert item["source_role"] == "inline_state"
        assert item["occurrence_key"] == occurrence
        assert item["value"] == pytest.approx(value)
        assert (
            item["applies_to_occurrence_key"]
            == "property|BLKprop_1"
        )

    assert all(
        result["block"]["block_id"] != "PROPblock_1"
        for result in reaction_result["results"]
    )


def test_inline_state_cannot_satisfy_constraint_or_parameter_role(run_adv):
    as_constraint = reaction_request()
    as_constraint["inline_state"] = []
    as_constraint["fixed_constraints"] = [
        fixed_filter(
            "temperature_constraint",
            "GLOBvar_1",
            298,
            299,
            "K",
            "thermodynamic_temperature",
        )
    ]
    assert run_adv(as_constraint)["results"] == []

    as_parameter = reaction_request()
    as_parameter["inline_state"] = []
    as_parameter["parameters"] = [
        selector(
            "temperature_parameter",
            "GLOBconstr_2",
            min_values=1,
        )
    ]
    assert run_adv(as_parameter)["results"] == []


def test_minimum_common_points_counts_real_missing_cells(run_adv):
    result = run_adv(missing_value_request(minimum_count=8))
    assert len(result["results"]) == 1
    row = result["results"][0]
    match = _only_match(row)
    assert row["block"]["doi"] == "10.1016/j.fluid.2007.04.018"
    assert row["block"]["block_id"] == "PROPblock_11"
    assert match["match_trace"]["rows_before_where"] == 9
    assert match["match_trace"]["rows_after_where"] == 9
    assert match["matched_complete_points"] == 8
    assert match["complete_point_aliases"] == [
        "feed_methanol_x",
        "ether_x",
        "methanol_x",
    ]
    assert _selected_value(match, "rows_after_where") == 9
    assert match["bindings"]["ether_x"]["occurrence_key"] == (
        "property|BLKprop_2"
    )
    assert match["bindings"]["methanol_x"]["occurrence_key"] == (
        "property|BLKprop_3"
    )

    rejected = run_adv(missing_value_request(minimum_count=9))
    assert rejected["results"] == []


def test_cardinality_rejects_ambiguity_but_all_preserves_real_bindings(
    run_adv,
):
    ambiguous = missing_value_request(
        minimum_count=1,
        ambiguous_target=True,
        target_cardinality="exactly_one",
    )
    rejected = run_adv(ambiguous)
    assert rejected["results"] == []
    assert rejected["diagnostics"]["ambiguous_binding_rejections"] >= 1

    expanded = missing_value_request(
        minimum_count=1,
        ambiguous_target=True,
        target_cardinality="all",
    )
    result = run_adv(expanded)
    assert len(result["results"]) == 1
    assert result["n_binding_matches"] == 2
    block_result = result["results"][0]
    assert {
        match["bindings"]["ether_x"]["occurrence_key"]
        for match in block_result["binding_matches"]
    } == {
        "property|BLKprop_1",
        "property|BLKprop_2",
    }
    assert (
        block_result["block"]["doi"],
        block_result["block"]["block_id"],
    ) == ("10.1016/j.fluid.2007.04.018", "PROPblock_11")
