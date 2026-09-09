"""Internal pre-execution hierarchy regressions for ``block_search_adv``.

The three gates are walked AUTOMATICALLY by the framework inside
``review_or_execute_flat_search``; these regressions drive the internal
``assess_flat_search`` engine directly to prove the gates stay ordered,
content-addressed, and fail-closed.
"""

from __future__ import annotations

import copy

from advanced_block_search.lifecycle import (
    assess_flat_search,
    render_review_markdown,
    validate_block_search_adv_guidance,
)

from .conftest import reaction_request, unary_request


REVIEW_SCHEMA = "block_search_adv/preexecution-review-v1"


def _assess(request: dict) -> dict:
    """Run one internal assessment step and return its review (or None)."""
    kwargs = copy.deepcopy(request)
    assessment = assess_flat_search(**kwargs)
    return assessment.review


def _confirm(review: dict, request: dict) -> None:
    confirmation = review["confirmation"]
    request[confirmation["parameter"]] = confirmation["token"]


def test_three_reviews_are_ordered_and_do_not_open_raw_rows(adv_module, monkeypatch):
    import advanced_block_search.engine as engine

    def forbidden_raw_open():
        raise AssertionError("raw ThermoML opened during pre-execution review")

    monkeypatch.setattr(engine, "open_raw_db", forbidden_raw_open)
    request = unary_request()
    expected = (
        "composite_id_enrichment",
        "database_id_intent",
        "final_intent_and_syntax",
    )
    reviews = []
    for stage in expected:
        review = _assess(request)
        assert review["schema"] == REVIEW_SCHEMA
        assert review["stage"] == stage
        assert review["raw_rows_read"] is False
        reviews.append(review)
        _confirm(review, request)

    cross_role = next(
        item
        for item in reviews[0]["review"]["selectors"]
        if item["alias"] == "temperature"
    )
    assert cross_role["input_identity"] == "GLOBconstr_2"
    assert cross_role["input_catalog_role"] == "constraint"
    assert cross_role["requested_source_role"] == "variable"
    assert cross_role["required_role_global_id"] == "GLOBvar_1"
    assert cross_role["composite_selector_id"].startswith("ADVselector_")

    db_selector = next(
        item
        for item in reviews[1]["review"]["selectors"]
        if item["alias"] == "conductivity"
    )
    assert db_selector["actual_source_global_ids"] == ["GLOBprop_34"]
    assert db_selector["examples"][0]["source_local_key"] == "BLKprop_1"
    context = db_selector["examples"][0]["property_context"]
    assert context["presentation"] == "Direct value, X"
    assert context["meas_num_id"] == "GLOBmeas_41"

    assert "common finite raw rows after WHERE" in reviews[2]["review"][
        "not_yet_established"
    ]


def test_any_semantic_argument_change_invalidates_the_lowest_token(adv_module):
    request = unary_request()
    first = _assess(request)
    _confirm(first, request)
    request["explanation"] = "A changed chemistry goal must restart review."
    restarted = _assess(request)
    assert restarted["stage"] == "composite_id_enrichment"
    assert restarted["confirmation"]["invalid_or_stale_token_received"] is True
    assert restarted["confirmation"]["token"] != first["confirmation"]["token"]


def test_cross_stage_and_malformed_tokens_fail_closed(adv_module):
    request = unary_request()
    first = _assess(request)
    _confirm(first, request)
    request["database_intent_confirmation_token"] = first["confirmation"]["token"]
    second = _assess(request)
    assert second["stage"] == "database_id_intent"
    assert second["confirmation"]["invalid_or_stale_token_received"] is True

    _confirm(second, request)
    request["execution_confirmation_token"] = "bsa_final_not-a-real-token"
    third = _assess(request)
    assert third["stage"] == "final_intent_and_syntax"
    assert third["confirmation"]["invalid_or_stale_token_received"] is True


def test_zero_database_matches_are_reviewable_not_fabricated(adv_module):
    request = unary_request()
    request["targets"] = [
        "GLOBprop_34 AS conductivity PHASE GLOBphase_1 MIN_FINITE 4"
    ]
    request["phases"] = ["GLOBphase_1"]
    first = _assess(request)
    _confirm(first, request)
    second = _assess(request)
    assert second["stage"] == "database_id_intent"
    assert second["review"]["counts"]["bindable_blocks"] == 0
    codes = {item["code"] for item in second["review"]["warnings"]}
    assert "NO_BINDABLE_BLOCKS" in codes
    assert second["raw_rows_read"] is False


def test_non_direct_property_presentation_is_visible_before_execution(adv_module):
    request = {
        "targets": "GLOBprop_11 AS transition CARDINALITY EACH",
        "explanation": "Inspect reported solid-liquid transition observands.",
        "literature": "GLOBlit_104",
        "limit": 10,
    }
    first = _assess(request)
    _confirm(first, request)
    second = _assess(request)
    assert second["stage"] == "database_id_intent"
    contexts = [
        example.get("property_context")
        for selector in second["review"]["selectors"]
        for example in selector["examples"]
        if example.get("property_context")
    ]
    assert any(
        context["presentation"] == "Difference with the reference state, X-X(REF)"
        for context in contexts
    )
    codes = {item["code"] for item in second["review"]["warnings"]}
    assert "NON_DIRECT_PROPERTY_PRESENTATION" in codes


def test_component_annotation_on_non_component_quantity_is_rejected(adv_module):
    result = adv_module.block_search_adv(
        targets="GLOBprop_34 AS conductivity COMPONENT co2",
        explanation="This annotation is chemically invalid.",
        compounds="GLOBcomp_3 AS co2",
    )
    assert result["schema"] == "block_search_adv/error-v1"
    assert result["error"]["code"] == "COMPONENT_QUALIFIER_NOT_ALLOWED"


def test_doi_and_globlit_contradiction_is_rejected(adv_module):
    result = adv_module.block_search_adv(
        targets="GLOBprop_34 AS conductivity",
        explanation="Contradictory literature identity must fail closed.",
        literature=["DOI=10.1007/s10765-005-5566-6", "GLOBlit_2"],
    )
    assert result["schema"] == "block_search_adv/error-v1"
    assert result["error"]["code"] == "CONTRADICTORY_LITERATURE_IDS"


def test_sync_guidance_hook_releases_valid_calls_and_blocks_errors(adv_module):
    request = unary_request()
    guidance = validate_block_search_adv_guidance(
        tool_name="block_search_adv",
        call_kwargs={**request, "purpose": "test", "tasks": "test"},
    )
    assert guidance == ""

    broken = dict(request)
    broken["literature"] = ["DOI=10.1007/s10765-005-5566-6", "GLOBlit_2"]
    guidance = validate_block_search_adv_guidance(
        tool_name="block_search_adv",
        call_kwargs={**broken, "purpose": "test", "tasks": "test"},
    )
    assert isinstance(guidance, str) and guidance
    assert "pre-execution validation failed" in guidance
    assert "CONTRADICTORY_LITERATURE_IDS" in guidance
    assert "No raw rows were read" in guidance


def test_guidance_hook_ignores_legacy_token_arguments(adv_module):
    request = unary_request()
    guidance = validate_block_search_adv_guidance(
        tool_name="block_search_adv",
        call_kwargs={
            **request,
            "purpose": "test",
            "tasks": "test",
            "composite_confirmation_token": "bsa_comp_stale",
            "execution_confirmation_token": "bsa_final_stale",
        },
    )
    assert guidance == ""

def test_matching_pair_plus_extra_globlit_is_rejected(adv_module):
    result = adv_module.block_search_adv(
        targets="GLOBprop_34 AS conductivity",
        explanation="Every DOI must be paired with exactly its own GLOBlit identity.",
        literature=[
            "DOI=10.1007/s10765-005-5566-6",
            "GLOBlit_1",
            "GLOBlit_2",
        ],
    )
    assert result["schema"] == "block_search_adv/error-v1"
    assert result["error"]["code"] == "CONTRADICTORY_LITERATURE_IDS"
    assert result["error"]["details"]["extraneous_lit_num_ids"] == ["GLOBlit_2"]


def test_final_gate_restates_full_chemistry_plan(adv_module):
    request = reaction_request()
    first = _assess(request)
    _confirm(first, request)
    second = _assess(request)
    _confirm(second, request)
    third = _assess(request)

    assert third["stage"] == "final_intent_and_syntax"
    restatement = third["review"]["chemistry_intent_restatement"]
    assert restatement["explanation"] == request["explanation"]
    assert restatement["where_ast"] is not None
    assert restatement["fixed_and_inline_conditions"]
    assert restatement["selectors"]
    assert restatement["selections"]
    assert third["raw_rows_read"] is False


def test_sparse_valid_agent_call_is_released_without_agent_gates():
    guidance = validate_block_search_adv_guidance(
        tool_name="block_search_adv",
        call_kwargs={
            "targets": "GLOBprop_34 AS conductivity",
            "explanation": "Inspect conductivity records.",
            "purpose": "test",
            "tasks": "test",
        },
    )
    assert guidance == ""


def test_review_renderer_preserves_confirmation_footer_when_body_is_large():
    token = "bsa_final_preserve-this-token"
    review = {
        "stage": "final_intent_and_syntax",
        "stage_number": 3,
        "title": "Final chemistry intent and syntax",
        "review": {
            "chemistry_intent_restatement": {
                "explanation": "x" * 100_000,
                "selectors": [],
            },
            "not_yet_established": ["raw rows"],
        },
        "confirmation": {
            "parameter": "execution_confirmation_token",
            "token": token,
        },
    }
    markdown = render_review_markdown(review)
    assert len(markdown) <= 32_000
    assert token in markdown
    assert markdown.endswith(
        "invalidates the tokens and restarts the hierarchy."
    )


def test_one_shot_execution_entry_points_do_not_exist():
    import advanced_block_search.engine as engine
    import advanced_block_search.flat_v2 as flat_v2

    assert not hasattr(engine, "execute_search")
    assert not hasattr(flat_v2, "execute_flat_search")

def test_database_state_changes_invalidate_only_dependent_gates(adv_module, monkeypatch):
    import advanced_block_search.catalogs as catalog
    import advanced_block_search.lifecycle as lifecycle

    original_file_state = lifecycle._file_state
    epochs = {"pcs": 0, "raw": 0}

    def changing_file_state(path):
        value = dict(original_file_state(path))
        if path == catalog.PCS_DB:
            value["mtime_ns"] = int(value.get("mtime_ns") or 0) + epochs["pcs"]
        if path == catalog.RAW_DB:
            value["mtime_ns"] = int(value.get("mtime_ns") or 0) + epochs["raw"]
        return value

    monkeypatch.setattr(lifecycle, "_file_state", changing_file_state)
    request = unary_request()
    first = _assess(request)
    _confirm(first, request)
    second = _assess(request)
    _confirm(second, request)

    epochs["pcs"] = 1
    refreshed_second = _assess(request)
    assert refreshed_second["stage"] == "database_id_intent"
    assert refreshed_second["confirmation"]["invalid_or_stale_token_received"] is True
    assert refreshed_second["raw_rows_read"] is False
    _confirm(refreshed_second, request)

    third = _assess(request)
    assert third["stage"] == "final_intent_and_syntax"
    _confirm(third, request)

    epochs["raw"] = 1
    refreshed_third = _assess(request)
    assert refreshed_third["stage"] == "final_intent_and_syntax"
    assert refreshed_third["confirmation"]["invalid_or_stale_token_received"] is True
    assert refreshed_third["raw_rows_read"] is False


def test_public_call_walks_all_gates_automatically(adv_module, monkeypatch):
    import advanced_block_search.lifecycle as lifecycle

    seen_stages: list[str | None] = []
    original_assess = lifecycle.assess_flat_search

    def observing_assess(**kwargs):
        assessment = original_assess(**kwargs)
        seen_stages.append(
            assessment.review["stage"] if assessment.review else None
        )
        return assessment

    monkeypatch.setattr(lifecycle, "assess_flat_search", observing_assess)
    result = lifecycle.review_or_execute_flat_search(
        **unary_request(),
        composite_confirmation_token="bsa_comp_stale-agent-token",
    )
    assert seen_stages == [
        "composite_id_enrichment",
        "database_id_intent",
        "final_intent_and_syntax",
        None,
    ]
    assert result["schema"] == "block_search_adv/result-v1"
    review = result["preexecution_review"]
    assert review["raw_execution_authorized"] is True
    assert review["automatic_confirmation"] is True
    assert set(review["confirmation_tokens"]) == {
        "composite_confirmation_token",
        "database_intent_confirmation_token",
        "execution_confirmation_token",
    }