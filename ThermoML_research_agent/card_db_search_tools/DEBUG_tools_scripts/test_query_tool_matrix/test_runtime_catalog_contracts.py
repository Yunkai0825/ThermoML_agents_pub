"""Catalog, signature, and agent-description drift checks."""

from __future__ import annotations

import inspect

from NIST_ThermoML_agents.general_db_query_engine.general_subagent_skill_schema_and_parser.subworkflow_md_tool_descriptions import (
    build_tool_instructions,
)


L1_SEARCH_TOOLS = {
    "resolve_ids",
    "resolve_compound_ids",
    "resolve_property_ids",
    "resolve_measurement_ids",
    "resolve_reference_ids",
    "search_id_alignment",
    "search_blocks",
    "block_search_adv",
    "inspect_block_table",
    "search_system_registry",
    "search_system_summary",
    "search_similar_compounds",
    "screen_property_systems",
}
L1_DELEGATION_TOOLS = {
    "L2_comp_eval",
    "L2_meas_eval",
    "L2_ref_eval",
    "L2_prop_eval",
}
ADV_FLAT_PARAMETERS = (
    "targets",
    "explanation",
    "compounds",
    "compound_match",
    "system_type",
    "system_scope",
    "system_size_min",
    "system_size_max",
    "parameters",
    "literature",
    "phases",
    "phase_match",
    "fixed_constraints",
    "inline_state",
    "where",
    "minimum_common_points",
    "calculate",
    "select",
    "having",
    "order_by",
    "limit",
)
ADV_RETIRED_PARAMETERS = {
    "request",
    "schema",
    "compound_list",
    "para_identity",
    "target_identity",
    "filtering_identity",
    "constraint_filter",
    "inline_state_filter",
    "compute",
}


def test_runtime_l1_catalog_is_exact_and_all_searches_have_compactors(
    l1_catalog,
) -> None:
    names = set(l1_catalog.entries)
    assert names == L1_SEARCH_TOOLS | L1_DELEGATION_TOOLS
    assert set(l1_catalog.compactor_registry) == L1_SEARCH_TOOLS

    for name in L1_SEARCH_TOOLS:
        entry = l1_catalog.entries[name]
        assert entry.compactor_fn is not None
        assert not entry.skip_compactor
    for name in L1_DELEGATION_TOOLS:
        entry = l1_catalog.entries[name]
        assert entry.skip_compactor and entry.skip_subagent


def test_model_visible_l1_signatures_match_runtime_contract(
    l1_catalog,
) -> None:
    wrapped = l1_catalog.wrapped_tools()
    for name in L1_SEARCH_TOOLS:
        parameters = inspect.signature(wrapped[name]).parameters
        assert parameters["purpose"].kind is inspect.Parameter.KEYWORD_ONLY
        assert parameters["tasks"].kind is inspect.Parameter.KEYWORD_ONLY

    advanced = inspect.signature(wrapped["block_search_adv"]).parameters
    assert tuple(
        name for name in advanced if name not in {"purpose", "tasks"}
    ) == ADV_FLAT_PARAMETERS
    assert not ADV_RETIRED_PARAMETERS.intersection(advanced)


def test_generated_instruction_block_exposes_batch_and_required_context(
    l1_catalog,
) -> None:
    instructions = build_tool_instructions(l1_catalog.wrapped_tools())
    assert "Batch independent tool calls in one turn" in instructions
    assert "block_search_adv(targets, explanation, compounds=" in instructions
    assert "screen_property_systems(" in instructions
    assert "purpose, tasks)" in instructions
    assert "compound_list" not in instructions
    assert "extract_block_csv" not in instructions
    assert "compact_block(" not in instructions


def test_handwritten_workflow_teaches_only_live_contract(
    query_root,
) -> None:
    workflow = (
        query_root
        / "NIST_ThermoML_agents"
        / "NIST_ThermoML_query_agent"
        / "query_agent_workflows"
        / "L1_workers"
        / "L1_query_workflow.md"
    ).read_text(encoding="utf-8")

    assert "block_search_adv(targets, explanation" in workflow
    for retired in ADV_RETIRED_PARAMETERS:
        assert f"`{retired}`" not in workflow
    assert 'system_type="unary"' in workflow
    assert 'system_type="pure"' not in workflow
    assert "not callable tools" in workflow
    assert "purpose` and `tasks`" in workflow


def test_basic_search_runtime_rejects_retired_encodings_despite_old_docstrings(
    l1_catalog,
) -> None:
    for name in (
        "search_blocks",
        "search_system_registry",
        "search_system_summary",
    ):
        result = l1_catalog.entries[name].fn(
            compound="GLOBcomp_1;GLOBcomp_3",
            limit=1,
        )
        assert result["error_code"] == "ID_REFINEMENT_REQUIRED"

    for name in (
        "search_blocks",
        "search_system_registry",
        "search_system_summary",
    ):
        try:
            l1_catalog.entries[name].fn(
                compound="GLOBcomp_1",
                system_type="pure",
                limit=1,
            )
        except ValueError as exc:
            assert "unary" in str(exc)
        else:  # pragma: no cover
            raise AssertionError(
                f"{name} accepted retired system_type='pure'"
            )


def test_l2_catalogs_cover_every_underlying_database_tool(
    l2_catalogs,
) -> None:
    expected = {
        "compound": {
            "search_comp_from_block",
            "search_compound_dk",
            "search_compound_indiv",
        },
        "measurement": {
            "search_meas_from_block",
            "search_measurement_dk",
            "search_measurement_indiv",
        },
        "reference": {
            "search_reference_from_block",
            "search_references",
        },
        "property": {
            "search_prop_dk_from_block",
            "search_property_dk",
        },
    }
    assert {
        name: set(catalog.tools)
        for name, catalog in l2_catalogs.items()
    } == expected
