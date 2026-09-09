"""Fail-closed validation and synthetic raw-cell edge regressions."""

from __future__ import annotations

import copy
import inspect

import pytest

from advanced_block_search.engine import _materialize_series

from .conftest import target_translation_request, unary_request


def _error_result(adv_module, request: dict) -> dict:
    result = adv_module.block_search_adv(**copy.deepcopy(request))
    assert result["schema"] == "block_search_adv/error-v1"
    assert result["results"] == []
    assert isinstance(result["error"]["pointer"], str)
    return result


def test_prop_limit_is_null_but_not_miscounted_as_a_finite_value():
    raw_block = {
        "NumValues": [
            {
                "PropertyValue": [
                    {"nPropNumber": 1, "nPropValue": 1.25}
                ]
            },
            {
                "PropertyValue": [
                    {
                        "nPropNumber": 1,
                        "PropLimit": {"nPropLimitValue": 2.5},
                    }
                ]
            },
            {"PropertyValue": []},
        ]
    }
    statistic = {
        "source_role": "property",
        "source_local_key": "BLKprop_1",
        "occurrence_key": "property|BLKprop_1",
        "n_rows": 3,
        "n_values": 1,
        "n_limit_values": 1,
        "n_nonfinite": 0,
    }
    diagnostics = {
        "limit_cells_as_null": 0,
        "nonfinite_cells_as_null": 0,
    }
    assert _materialize_series(raw_block, statistic, diagnostics) == [
        1.25,
        None,
        None,
    ]
    assert diagnostics["limit_cells_as_null"] == 1


def test_decimal_in_one_sentence_explanation_is_valid(run_adv):
    request = unary_request()
    request["explanation"] = (
        "Find unary carbon dioxide conductivity near 298.15 K."
    )
    result = run_adv(request)
    assert result["schema"] == "block_search_adv/result-v1"
    assert result["normalized_query"]["input_contract"] == (
        "block_search_adv/flat-v2"
    )


def test_pure_is_rejected_in_favor_of_unary(adv_module):
    request = unary_request()
    request["system_type"] = "pure"
    result = _error_result(adv_module, request)
    assert result["error"]["code"] == "INVALID_REQUEST"
    assert result["error"]["pointer"] == "/system_type"


def test_raw_sql_text_is_rejected(adv_module):
    request = unary_request()
    request["where"] = "SELECT * FROM data_blocks;"
    result = _error_result(adv_module, request)
    assert result["error"]["code"] == "INVALID_EXPRESSION"
    assert result["error"]["pointer"] == "/where"


def test_dimensionally_incompatible_comparison_is_rejected(adv_module):
    request = unary_request()
    request["where"] = "temperature < pressure"
    result = _error_result(adv_module, request)
    assert result["error"]["code"] == "UNIT_MISMATCH"
    assert result["error"]["pointer"] == "/where"


def test_computed_alias_cycle_is_rejected(adv_module):
    request = unary_request()
    request["calculate"] = [
        "cycle_b AS cycle_a",
        "cycle_a AS cycle_b",
    ]
    result = _error_result(adv_module, request)
    assert result["error"]["code"] == "EXPRESSION_CYCLE"
    assert result["error"]["pointer"] == "/calculate"


def test_where_cannot_use_an_undeclared_identity(adv_module):
    request = unary_request()
    request["where"] = "temperature > 425[K] AND ghost > 0"
    result = _error_result(adv_module, request)
    assert result["error"]["code"] == "UNKNOWN_ALIAS"
    assert result["error"]["pointer"] == "/where"


def test_component_linked_exact_binding_requires_a_component(adv_module):
    request = target_translation_request()
    request["targets"][0] = request["targets"][0].replace(
        " COMPONENT pentafluoroethane",
        "",
    )
    result = _error_result(adv_module, request)
    assert result["error"]["code"] == "COMPONENT_QUALIFIER_REQUIRED"
    assert result["error"]["pointer"] == "/targets/0"


def test_inline_state_requires_an_explicit_target_link(adv_module):
    request = unary_request()
    request["inline_state"] = [
        (
            "GLOBvar_1 AS inline_temperature "
            "WHERE VALUE BETWEEN 298[K] AND 299[K]"
        )
    ]
    result = _error_result(adv_module, request)
    assert result["error"]["code"] == "INLINE_TARGET_REQUIRED"
    assert result["error"]["pointer"] == "/inline_state/0"


@pytest.mark.parametrize(
    ("field", "bad_value", "pointer"),
    [
        ("targets", {"conductivity": "GLOBprop_34"}, "/targets"),
        (
            "targets",
            [{"identity": "GLOBprop_34", "as": "conductivity"}],
            "/targets/0",
        ),
        (
            "parameters",
            [["GLOBconstr_2 AS temperature"]],
            "/parameters/0",
        ),
        (
            "compounds",
            {"carbon_dioxide": "GLOBcomp_3"},
            "/compounds",
        ),
    ],
)
def test_public_collections_reject_nested_shapes(
    adv_module,
    field,
    bad_value,
    pointer,
):
    request = unary_request()
    request[field] = bad_value
    result = _error_result(adv_module, request)
    assert result["error"]["code"] == "NESTING_NOT_ALLOWED"
    assert result["error"]["pointer"] == pointer


def test_nested_v1_arguments_are_not_part_of_the_public_signature(adv_module):
    parameters = inspect.signature(
        adv_module.block_search_adv
    ).parameters
    assert "compound_list" not in parameters
    assert "para_identity" not in parameters
    assert "target_identity" not in parameters
    assert "filtering_identity" not in parameters

    request = unary_request()
    request["compound_list"] = {
        "all_of": [],
        "exact_system": True,
    }
    with pytest.raises(TypeError, match="compound_list"):
        adv_module.block_search_adv(**request)


@pytest.mark.parametrize(
    "factory",
    [
        unary_request,
        target_translation_request,
    ],
)
def test_request_factories_have_at_most_one_collection_layer(factory):
    request = factory()
    assert request
    for value in request.values():
        assert not isinstance(value, dict)
        if isinstance(value, list):
            assert all(isinstance(item, str) for item in value)
