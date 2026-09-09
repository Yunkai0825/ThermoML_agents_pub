"""Real-database execution and hardcoded-compaction coverage."""

from __future__ import annotations

import copy

import importlib.util
import sys
from pathlib import Path
from typing import Any

import pytest

from .chemistry_cases import (
    CO2_BLOCK,
    DOI_CO2,
    L1_LIVE_CASES,
    L2_LIVE_CASES,
)


L1_SEARCH_NAMES = tuple(L1_LIVE_CASES)


def _ids(result: dict[str, Any], field: str) -> set[str]:
    return {
        row[field]
        for row in result.get("results", [])
        if isinstance(row, dict) and isinstance(row.get(field), str)
    }


def _assert_l1_chemistry(name: str, result: dict[str, Any]) -> None:
    assert isinstance(result, dict), name
    assert result.get("error_code") not in {
        "QUERY_REFINEMENT_REQUIRED",
        "TOOL_ARGUMENT_REFINEMENT_REQUIRED",
    }, result

    if name == "resolve_ids":
        assert {
            "GLOBvar_1",
            "GLOBvar_2",
            "GLOBvar_3",
        }.issubset(_ids(result, "var_num_id"))
    elif name == "resolve_compound_ids":
        assert {
            "GLOBcomp_1",
            "GLOBcomp_3",
            "GLOBcomp_4",
        }.issubset(_ids(result, "comp_num_id"))
    elif name == "resolve_property_ids":
        assert {
            "GLOBprop_1",
            "GLOBprop_4",
            "GLOBprop_34",
        }.issubset(_ids(result, "prop_num_id"))
    elif name == "resolve_measurement_ids":
        assert {
            "GLOBmeas_41",
            "GLOBmeas_132",
        }.issubset(_ids(result, "meas_num_id"))
    elif name == "resolve_reference_ids":
        assert "GLOBlit_1" in _ids(result, "lit_num_id")
        assert any(
            row.get("doi") == DOI_CO2 for row in result["results"]
        )
    elif name == "search_id_alignment":
        assert "GLOBprop_34" in _ids(result, "prop_num_id")
    elif name == "search_blocks":
        assert result["n_results"] == 1
        row = result["results"][0]
        assert (row["doi"], row["block_number"]) == (
            DOI_CO2,
            CO2_BLOCK,
        )
        assert row["system_type"] == "unary"
    elif name == "block_search_adv":
        assert result["schema"] == "block_search_adv/result-v1"
        assert result["n_results"] == 1
        row = result["results"][0]
        block_id = row["block"].get(
            "block_number",
            row["block"].get("block_id"),
        )
        assert (
            row["block"]["doi"],
            block_id,
        ) == (DOI_CO2, CO2_BLOCK)
        match = row["binding_matches"][0]
        assert match["match_trace"]["rows_after_where"] == 4
        selected = match["selected"]
        assert selected["mean_conductivity"]["value"] == pytest.approx(
            0.0283025
        )
        normalized = result["normalized_query"]
        assert normalized["system_type"] == "unary"
        assert all(
            not isinstance(value, dict) for value in normalized.values()
        )
    elif name == "search_system_registry":
        assert result["n_results"] == 1
        row = result["results"][0]
        assert (row["doi"], row["block_number"], row["block_type"]) == (
            "10.1007/s10765-009-0568-4",
            "RXNblock_1",
            "ReactionData",
        )
    elif name == "search_system_summary":
        summary = result["summary"]
        assert summary["n_blocks"] > 0
        assert summary["n_papers"] > 0
        assert summary["n_targets"] >= summary["n_blocks"]
        assert summary["total_matching_datapoints"] > 0
    elif name == "search_similar_compounds":
        assert result["metric"] == "morgan"
        assert result["n_results"] == 5
        similarities = [row["similarity"] for row in result["results"]]
        assert similarities == sorted(similarities, reverse=True)
        assert min(similarities) >= 0.2
        assert all(
            row["comp_num_id"].startswith("GLOBcomp_")
            for row in result["results"]
        )
    else:  # pragma: no cover - protects matrix/catalog drift
        raise AssertionError(f"No chemistry assertion for {name}")


@pytest.mark.parametrize("tool_name", L1_SEARCH_NAMES)
def test_every_l1_search_executes_and_hard_compacts(
    tool_name: str,
    l1_catalog,
) -> None:
    entry = l1_catalog.entries[tool_name]
    arguments = copy.deepcopy(L1_LIVE_CASES[tool_name])
    result = entry.fn(**arguments)
    _assert_l1_chemistry(tool_name, result)

    markdown = l1_catalog.compact_tool_result(tool_name, result)
    assert isinstance(markdown, str)
    assert markdown.strip()
    assert len(markdown) < 200_000


def _assert_l2_chemistry(name: str, result: dict[str, Any]) -> None:
    assert isinstance(result, dict), name
    assert "error_code" not in result, result

    if name.endswith("_from_block"):
        assert result["doi"] == DOI_CO2
        assert result["block_number"] == CO2_BLOCK
    if name == "search_comp_from_block":
        assert "GLOBcomp_3" in result["comp_num_ids"]
        assert result["ccs_indiv_md"].strip()
    elif name == "search_meas_from_block":
        assert "GLOBmeas_41" in result["meas_num_ids"]
        assert result["mtdks_indiv_md"].strip()
    elif name == "search_prop_dk_from_block":
        assert "GLOBprop_34" in result["prop_num_ids"]
        assert result["pcs_dk"]
    elif name == "search_reference_from_block":
        assert result["rms_indiv_md"].strip()
    else:
        assert result["n_results"] > 0
        assert result["results"]


@pytest.mark.parametrize("tool_name", tuple(L2_LIVE_CASES))
def test_every_underlying_l2_database_tool_executes(
    tool_name: str,
    l2_catalogs,
) -> None:
    catalog_name, arguments = L2_LIVE_CASES[tool_name]
    result = l2_catalogs[catalog_name].tools[tool_name](**arguments)
    _assert_l2_chemistry(tool_name, result)


def _load_extractor(query_root: Path):
    path = (
        query_root
        / "card_db_search_tools"
        / "basic_search_tools"
        / "11_block_data_extractor.py"
    )
    spec = importlib.util.spec_from_file_location(
        "_query_matrix_block_extractor",
        path,
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_auxiliary_extractors_execute_and_label_merged_rows(
    query_root: Path,
) -> None:
    extractor = _load_extractor(query_root)
    one = extractor.extract_block_csv(
        DOI_CO2,
        "PROPblock_1",
        property_filter="conductivity",
    )
    assert not one.get("error")
    assert one["n_rows"] == 77
    assert one["metadata"]["n_datapoints"] == 77
    assert "conductivity" in one["csv_text"].lower()

    merged = extractor.extract_multi_block_csv(
        [
            {
                "doi": DOI_CO2,
                "block_number": "PROPblock_1",
                "label": "unary_CO2",
            },
            {
                "doi": DOI_CO2,
                "block_number": "PROPblock_2",
                "label": "binary_CH4_CO2",
            },
        ],
        property_filter="conductivity",
    )
    assert merged["n_rows"] == 257
    assert merged["columns"][0] == "_source"
    assert not merged["errors"]


def test_auxiliary_single_block_export_is_uncapped(
    query_root: Path,
) -> None:
    extractor = _load_extractor(query_root)
    result = extractor.extract_block_csv(
        DOI_CO2,
        "PROPblock_1",
        property_filter="conductivity",
    )
    assert result["n_rows"] == result["metadata"]["n_datapoints"] == 77



def test_real_embedded_binary_target_projects_every_l2_and_extractor_context(
    query_root: Path,
    l2_catalogs,
) -> None:
    target = {
        "doi": "10.1016/j.fluid.2008.02.015",
        "block_number": "PROPblock_1",
        "BLKsubsys_id": "BLKsubsys_2",
    }
    compound = l2_catalogs["compound"].tools["search_comp_from_block"](
        **target
    )
    assert compound["lit_num_id"] == "GLOBlit_608"
    assert compound["comp_num_ids"] == ["GLOBcomp_1", "GLOBcomp_74"]
    assert "GLOBcomp_2004" not in compound["ccs_indiv_md"]
    assert "**Compounds:** 2" in compound["ccs_indiv_md"]

    measurement = l2_catalogs["measurement"].tools[
        "search_meas_from_block"
    ](**target)
    assert measurement["meas_num_ids"] == ["GLOBmeas_7"]
    assert "PROPblock_1" in measurement["mtdks_indiv_md"]
    assert "PROPblock_2" not in measurement["mtdks_indiv_md"]

    prop = l2_catalogs["property"].tools["search_prop_dk_from_block"](
        **target
    )
    assert prop["prop_num_ids"] == ["GLOBprop_8"]
    reference = l2_catalogs["reference"].tools[
        "search_reference_from_block"
    ](**target)
    assert reference["lit_num_id"] == "GLOBlit_608"
    assert reference["BLKsubsys_id"] == "BLKsubsys_2"

    extractor = _load_extractor(query_root)
    extracted = extractor.extract_block_csv(**target)
    assert extracted["n_rows"] == 72
    assert extracted["metadata"]["system_type"] == "binary"
    assert extracted["metadata"]["declared_system_type"] == "ternary"
    assert [
        item["comp_num_id"] for item in extracted["metadata"]["compounds"]
    ] == ["GLOBcomp_74", "GLOBcomp_1"]
    assert [
        item["comp_num_id"]
        for item in extracted["metadata"]["declared_compounds"]
    ] == ["GLOBcomp_74", "GLOBcomp_2004", "GLOBcomp_1"]
    assert not any(
        "potassium dihydrogen citrate" in column
        for column in extracted["columns"]
    )
    assert extracted["metadata"]["matched_subsystem"]["evidence_quality"] == (
        "exact_reported_zero"
    )



def test_real_embedded_binary_search_scopes_are_distinct(l1_catalog) -> None:
    search = l1_catalog.entries["search_blocks"].fn
    arguments = {
        "compound": ["GLOBcomp_74", "GLOBcomp_1"],
        "property": "GLOBprop_8",
        "literature": "GLOBlit_608",
        "system_type": "binary",
        "limit": 20,
    }
    assert search(**arguments, system_scope="declared")["n_results"] == 0
    subsystem = search(**arguments, system_scope="subsystem")
    assert subsystem["n_results"] == 1
    row = subsystem["results"][0]
    assert (
        row["doi"], row["block_number"], row["BLKsubsys_id"],
        row["system_type"], row["n_datapoints"],
    ) == (
        "10.1016/j.fluid.2008.02.015", "PROPblock_1",
        "BLKsubsys_2", "binary", 72,
    )
    either = search(**arguments, system_scope="either")
    assert [
        (item["doi"], item["block_number"], item["BLKsubsys_id"])
        for item in either["results"]
    ] == [("10.1016/j.fluid.2008.02.015", "PROPblock_1", "BLKsubsys_2")]



def test_analysis_inspector_preserves_exact_subsystem_target() -> None:
    from NIST_ThermoML_agents.NIST_ThermoML_analysis_agent.analysis_agent_toolbox.discovery_tools import (
        inspect_block,
    )

    result = inspect_block(
        "10.1016/j.fluid.2008.02.015",
        "PROPblock_1",
        BLKsubsys_id="BLKsubsys_2",
    )
    assert result["BLKsubsys_id"] == "BLKsubsys_2"
    assert result["n_rows"] == 72
    assert [item["comp_num_id"] for item in result["compounds"]] == [
        "GLOBcomp_74", "GLOBcomp_1"
    ]
    assert result["identified_x"] == [
        "molality_mol_kg_<(S)-2-aminopropanoic acid>"
    ]
    assert result["identified_y"] == ["speed_of_sound_m_s"]
    assert "BLKpoint_id" not in result["identified_x"] + result["identified_y"]
