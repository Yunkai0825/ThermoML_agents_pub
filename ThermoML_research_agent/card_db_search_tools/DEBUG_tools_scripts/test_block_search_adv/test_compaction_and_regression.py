"""Compactor registration and unchanged existing-search regression tests."""

from __future__ import annotations

import importlib
import importlib.util
import os
import sys
from pathlib import Path

from .conftest import (
    BASIC_TOOLS,
    QUERY_ROOT,
    binary_ranking_request,
    reaction_request,
)


def _registered_compactor(tool_name: str):
    package = importlib.import_module(
        "card_db_search_tools._tools_results_compactors"
    )
    matches = [
        function
        for function in package.COMPACTOR_FUNCTIONS
        if tool_name in getattr(function, "_compacts_tools", ())
    ]
    assert len(matches) == 1
    return matches[0]


def _load_numeric_module(path: Path):
    name = "_unchanged_search_blocks_regression"
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def test_advanced_compactor_is_registered_exactly_once():
    function = _registered_compactor("block_search_adv")
    assert callable(function)


def test_preexecution_review_compaction_is_actionable(adv_module):
    from advanced_block_search.lifecycle import assess_flat_search

    review = assess_flat_search(
        targets="GLOBprop_34 AS conductivity PHASE GLOBphase_3",
        explanation="Review carbon dioxide conductivity identity before execution.",
        compounds="GLOBcomp_3 AS carbon_dioxide",
        literature="GLOBlit_1",
    ).review
    markdown = _registered_compactor("block_search_adv")(review)
    assert "pre-execution gate 1/3" in markdown
    assert "GLOBprop_34" in markdown
    assert "thermal conductivity" in markdown.casefold()
    assert "ADVselector_" in markdown
    assert "composite_confirmation_token=bsa_comp_" in markdown
    assert "not executed raw ThermoML data" in markdown

def test_advanced_compaction_preserves_decisions_not_source_payload(
    binary_result,
):
    markdown = _registered_compactor("block_search_adv")(binary_result)
    assert isinstance(markdown, str)
    assert markdown.strip()
    assert len(markdown) < 12_000
    assert "block_search_adv" in markdown
    assert "10.1016/j.jct.2010.11.014" in markdown
    positions = [
        markdown.index(block_id)
        for block_id in ("PROPblock_1", "PROPblock_4", "PROPblock_7")
    ]
    assert positions == sorted(positions)
    assert "mean_scaled_h" in markdown
    assert "variable|BLKvar_1" in markdown
    assert "101.3" in markdown
    assert "298.15" in markdown
    assert "complete" in markdown.casefold()
    assert "key_permutations" not in markdown
    assert '"normalized_query"' not in markdown
    assert '"statistics"' not in markdown
    assert '"data_points"' not in markdown


def test_reaction_compaction_retains_inline_state_applicability(
    reaction_result,
):
    markdown = _registered_compactor("block_search_adv")(reaction_result)
    assert "RXNblock_1" in markdown
    assert "ReactionData" in markdown
    assert "inline_state" in markdown
    assert "inline_state|BLKprop_1|temperature_K" in markdown
    assert "inline_state|BLKprop_1|pressure_kPa" in markdown
    assert "property|BLKprop_1" in markdown
    assert "298.15" in markdown
    assert "200" in markdown


def test_zero_match_compaction_is_explicit(run_adv):
    result = run_adv(binary_ranking_request(minimum_count=5))
    markdown = _registered_compactor("block_search_adv")(result)
    assert "0" in markdown
    assert "block_search_adv" in markdown
    assert len(markdown) < 2_000


def test_search_blocks_declared_scope_is_explicit_and_compactable():
    module = _load_numeric_module(BASIC_TOOLS / "1_block_search.py")
    result = module.search_blocks(
        literature="10.1007/s10765-005-5566-6",
        system_scope="declared",
        limit=10,
    )
    assert result["n_results"] == 2
    assert [
        (row["block_number"], row["n_datapoints"])
        for row in result["results"]
    ] == [
        ("PROPblock_1", 77),
        ("PROPblock_2", 180),
    ]
    assert all(row["BLKsubsys_id"] is None for row in result["results"])
    assert all(row["search_scope"] == "declared" for row in result["results"])
    serialized = str(result)
    assert "derived_indexes" not in serialized
    assert "key_permutations" not in serialized
    markdown = _registered_compactor("search_blocks")(result)
    assert "declared" in markdown
    assert "PROPblock_1" in markdown
    assert "PROPblock_2" in markdown


def test_private_advanced_package_is_importable():
    package = importlib.import_module("advanced_block_search")
    assert package.__file__
    assert Path(os.fspath(package.__file__)).is_file()
