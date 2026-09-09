"""Chemistry-prompt regressions for the shallow advanced-search contract."""

from __future__ import annotations

import copy

import pytest

from advanced_block_search.flat_v2 import (
    _parse_expression,
    compile_flat_request,
)

from .conftest import (
    binary_ranking_request,
    missing_value_request,
    reaction_request,
    target_translation_request,
    unary_request,
)


def _error_result(adv_module, request: dict) -> dict:
    result = adv_module.block_search_adv(**copy.deepcopy(request))
    assert result["schema"] == "block_search_adv/error-v1"
    assert result["results"] == []
    return result


def _block_ids(result: dict) -> list[str]:
    return [row["block"]["block_id"] for row in result["results"]]


def test_mixed_case_aliases_and_common_units_normalize_to_existing_result(
    run_adv,
):
    request = unary_request()
    request["parameters"] = [
        item.replace(" AS temperature ", " AS Temperature ")
        .replace(" AS pressure ", " AS Pressure ")
        for item in request["parameters"]
    ]
    request["targets"] = [
        request["targets"][0].replace(
            " AS conductivity ",
            " AS Conductivity ",
        )
    ]
    request["where"] = (
        "Temperature BETWEEN 151.85 [degC] AND 155.85 [degC] "
        "AND Pressure BETWEEN 1 [MPa] AND 5 [MPa]"
    )
    request["select"] = (
        "MEAN(Conductivity) AS Mean_Conductivity"
    )

    result = run_adv(request)
    assert _block_ids(result) == ["PROPblock_1"]
    match = result["results"][0]["binding_matches"][0]
    assert match["match_trace"]["rows_after_where"] == 4
    assert match["selected"]["mean_conductivity"]["value"] == pytest.approx(
        0.0283025,
        rel=1e-12,
        abs=1e-15,
    )
    assert set(match["bindings"]) == {
        "temperature",
        "pressure",
        "conductivity",
    }


def test_casefolding_detects_alias_collision(adv_module):
    request = unary_request()
    request["parameters"][1] = request["parameters"][1].replace(
        " AS pressure ",
        " AS Temperature ",
    )
    result = _error_result(adv_module, request)
    assert result["error"]["code"] == "DUPLICATE_ALIAS"
    assert result["error"]["pointer"] == "/parameters/1"


def test_component_qualifier_rejected_for_non_component_quantity(adv_module):
    request = unary_request()
    request["targets"][0] = request["targets"][0].replace(
        " AS conductivity ",
        " AS conductivity COMPONENT carbon_dioxide ",
    )
    result = _error_result(adv_module, request)
    assert result["error"]["code"] == "COMPONENT_QUALIFIER_NOT_ALLOWED"
    assert result["error"]["pointer"] == "/targets/0/component"


def test_single_strings_are_normalized_to_flat_lists(run_adv):
    request = unary_request()
    for field in ("compounds", "targets", "phases", "select"):
        assert len(request[field]) == 1
        request[field] = request[field][0]

    result = run_adv(request)
    assert _block_ids(result) == ["PROPblock_1"]
    normalized = result["normalized_query"]
    for field in ("compounds", "targets", "phases", "select"):
        assert isinstance(normalized[field], list)
        assert len(normalized[field]) == 1


def test_compound_and_phase_clause_modes_lower_without_nested_objects():
    request = unary_request()
    request["compound_match"] = "all"
    request["compounds"] = [
        "REQUIRE GLOBcomp_3 AS CO2",
        "ANY GLOBcomp_1 AS Water IN solvent",
        "ANY GLOBcomp_4 AS Methanol IN solvent",
        "EXCLUDE GLOBcomp_2 AS Nitrogen",
    ]
    request["phases"] = [
        "REQUIRE GLOBphase_3",
        "ANY GLOBphase_1",
        "ANY GLOBphase_5",
        "EXCLUDE GLOBphase_2",
    ]
    compiled = compile_flat_request(**request)

    compounds = compiled.engine_kwargs["compound_list"]
    assert [item["as"] for item in compounds["all_of"]] == ["co2"]
    assert [item["as"] for item in compounds["any_of"]] == [
        "water",
        "methanol",
    ]
    assert [item["as"] for item in compounds["none_of"]] == ["nitrogen"]
    assert compiled.engine_kwargs["phase"] == {
        "all_of": ["GLOBphase_3"],
        "any_of": ["GLOBphase_1", "GLOBphase_5"],
        "none_of": ["GLOBphase_2"],
    }


def test_exact_system_rejects_any_or_excluded_compounds(adv_module):
    request = unary_request()
    request["compounds"].append("ANY GLOBcomp_1 AS water")
    result = _error_result(adv_module, request)
    assert result["error"]["code"] == "INVALID_DECLARATION"
    assert result["error"]["pointer"] == "/compounds/1"


def test_presence_only_fixed_constraints_keep_real_binary_matches(run_adv):
    request = binary_ranking_request()
    request["fixed_constraints"] = [
        declaration.split(" WHERE ", 1)[0]
        for declaration in request["fixed_constraints"]
    ]
    result = run_adv(request)
    assert _block_ids(result) == [
        "PROPblock_1",
        "PROPblock_4",
        "PROPblock_7",
    ]
    for row in result["results"]:
        evidence = row["binding_matches"][0]["fixed_filter_evidence"]
        assert {item["alias"] for item in evidence} == {
            "pressure_constraint",
            "temperature_constraint",
        }


def test_presence_only_inline_state_keeps_target_linked_reaction(run_adv):
    request = reaction_request()
    request["inline_state"] = [
        declaration.split(" WHERE ", 1)[0]
        for declaration in request["inline_state"]
    ]
    result = run_adv(request)
    assert _block_ids(result) == ["RXNblock_1"]
    evidence = result["results"][0]["binding_matches"][0][
        "fixed_filter_evidence"
    ]
    assert {
        item["applies_to_occurrence_key"] for item in evidence
    } == {"property|BLKprop_1"}


def test_parenthesized_derived_between_and_multiple_between_lower_cleanly():
    expression = _parse_expression(
        "Temperature BETWEEN 151.85 [degC] AND 155.85 [degC] "
        "AND (1[1] - Temperature / 1000[K]) "
        "BETWEEN 0[1] AND 1[1]",
        "/where",
    )
    assert expression["op"] == "and"
    first, second = expression["args"]
    assert first == {
        "op": "between",
        "expr": {"ref": "temperature"},
        "lower": {"literal": 425.0, "unit": "K"},
        "upper": {"literal": 429.0, "unit": "K"},
    }
    assert second["op"] == "between"
    assert second["expr"]["op"] == "subtract"


def test_between_accepts_nested_row_operations_on_the_left():
    expression = _parse_expression(
        "(1[1] - EXP(LN(x))) BETWEEN 0[1] AND 1[1]",
        "/where",
    )
    assert expression["op"] == "between"
    assert expression["expr"]["op"] == "subtract"
    assert expression["expr"]["args"][1]["op"] == "exp"

    function_expression = _parse_expression(
        "COALESCE(x, EXP(LN(y))) BETWEEN 0[1] AND 1[1]",
        "/where",
    )
    assert function_expression["op"] == "between"
    assert function_expression["expr"]["op"] == "coalesce"


def test_between_accepts_canonical_units_containing_parentheses():
    expression = _parse_expression(
        "conductivity BETWEEN 0.02 [W/(m K)] "
        "AND 0.04 [W/(m K)]",
        "/where",
    )
    assert expression == {
        "op": "between",
        "expr": {"ref": "conductivity"},
        "lower": {"literal": 0.02, "unit": "W/(m K)"},
        "upper": {"literal": 0.04, "unit": "W/(m K)"},
    }


def test_unit_normalizer_rejects_out_of_range_exponents():
    with pytest.raises(Exception) as captured:
        _parse_expression("pressure < 1e999999 [Pa]", "/where")
    error = captured.value
    assert getattr(error, "code", None) == "INVALID_EXPRESSION"
    assert getattr(error, "pointer", None) == "/where"


def test_parenthesized_derived_between_executes_on_real_target(run_adv):
    request = target_translation_request()
    request["where"] = (
        "temperature BETWEEN 290 [K] AND 310 [K] "
        "AND (1[1] - liquid_x) BETWEEN 0.19[1] AND 0.31[1]"
    )
    result = run_adv(request)
    assert _block_ids(result) == ["PROPblock_4"]
    match = result["results"][0]["binding_matches"][0]
    assert match["match_trace"]["rows_after_where"] == 2


def test_direct_aggregate_and_selected_alias_are_valid_in_having(run_adv):
    request = unary_request()
    request["select"] = (
        "MEAN(conductivity) AS Mean_Conductivity"
    )
    request["having"] = (
        "Mean_Conductivity > 0 [W/(m K)] AND COUNT(*) >= 4"
    )
    result = run_adv(request)
    assert _block_ids(result) == ["PROPblock_1"]
    selected = result["results"][0]["binding_matches"][0]["selected"]
    assert set(selected) == {"mean_conductivity"}


def test_targets_remain_mandatory(adv_module):
    request = unary_request()
    request["targets"] = []
    result = _error_result(adv_module, request)
    assert result["error"]["code"] == "INVALID_REQUEST"
    assert result["error"]["pointer"] == "/targets"


def test_cardinality_each_aggregates_each_occurrence_independently(run_adv):
    request = missing_value_request(
        minimum_count=1,
        ambiguous_target=True,
        target_cardinality="all",
    )
    request["select"] = "MEAN(ether_x) AS mean_ether_x"
    result = run_adv(request)
    assert result["n_binding_matches"] == 2
    matches = result["results"][0]["binding_matches"]
    assert {
        match["bindings"]["ether_x"]["occurrence_key"]
        for match in matches
    } == {"property|BLKprop_1", "property|BLKprop_2"}
    assert all("mean_ether_x" in match["selected"] for match in matches)

def test_system_scope_is_strict_and_reaches_the_private_plan(adv_module):
    request = unary_request()
    request["system_scope"] = "subsystem"
    compiled = compile_flat_request(**request)
    assert compiled.engine_kwargs["compound_list"]["system_scope"] == "subsystem"
    assert compiled.public_query["system_scope"] == "subsystem"

    request["system_scope"] = "parent_or_child"
    result = _error_result(adv_module, request)
    assert result["error"]["code"] == "INVALID_REQUEST"
    assert result["error"]["pointer"] == "/system_scope"


def test_flat_contract_accepts_unbounded_canonical_component_counts():
    request = unary_request()
    request["system_type"] = "11-component"
    compiled = compile_flat_request(**request)
    assert compiled.public_query["system_type"] == "11-component"

