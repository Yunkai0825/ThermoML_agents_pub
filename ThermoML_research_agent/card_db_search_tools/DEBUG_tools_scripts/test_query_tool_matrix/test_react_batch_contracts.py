"""Production wire-parser and ordered batch-execution regressions."""

from __future__ import annotations

import copy
import json
from dataclasses import replace
from functools import wraps
from typing import Any, Callable

import pytest

from .chemistry_cases import ADV_CO2, ADV_REACTION

from NIST_ThermoML_agents.NIST_ThermoML_query_agent.query_agent_context_hooks.hook_catalog import (
    build_agent_hooks,
)
from NIST_ThermoML_agents.general_db_query_engine.general_argo_engine_helpers.engine_react_helpers.react_loop import (
    _prevalidate_batch_arguments,
    agent_turn,
)
from NIST_ThermoML_agents.general_db_query_engine.general_argo_engine_helpers.engine_react_helpers import (
    react_helpers,
    react_loop as react_loop_module,
)
from NIST_ThermoML_agents.general_db_query_engine.general_argo_engine_helpers.engine_tool_interface_helpers.tool_call_parser import (
    extract_all_tool_calls,
)


def _wire(name: str, arguments: dict[str, Any]) -> str:
    payload = json.dumps(
        {"name": name, "arguments": arguments},
        ensure_ascii=False,
        allow_nan=False,
        separators=(",", ":"),
    )
    return f"<tool_call>{payload}</tool_call>"


class _SequenceClient:
    def __init__(self, responses: list[str]):
        self.responses = list(responses)
        self.prompts: list[str] = []

    def call(self, prompt: str, system: str, *args, **kwargs) -> str:
        del system, args, kwargs
        self.prompts.append(prompt)
        if not self.responses:
            raise AssertionError("deterministic ReAct client exhausted")
        return self.responses.pop(0)


def _run_sequence(
    responses: list[str],
    tools: dict[str, Callable],
    *,
    max_iterations: int = 5,
    batch_validator=None,
):
    client = _SequenceClient(responses)
    result = agent_turn(
        "Execute the chemistry regression.",
        system_prompt="Use canonical tool-call JSON.",
        tools=tools,
        memory=[],
        client=client,
        max_iterations=max_iterations,
        timeout=120,
        hooks=build_agent_hooks(batch_validator=batch_validator).engine_hooks,
    )
    return result, client


def test_parser_accepts_multiple_canonical_calls_before_wait() -> None:
    text = (
        _wire("resolve_compound_ids", {"queries": ["water", "methanol"]})
        + _wire("resolve_property_ids", {"queries": "viscosity"})
        + "<wait/>"
    )
    batch = extract_all_tool_calls(text)
    assert batch.syntax_valid
    assert batch.wait_detected
    assert batch.deferred_count == 0
    assert [call["name"] for call in batch.calls] == [
        "resolve_compound_ids",
        "resolve_property_ids",
    ]


def test_wait_is_a_dependency_barrier_and_discards_post_wait_calls() -> None:
    text = (
        _wire("resolve_compound_ids", {"queries": "carbon dioxide"})
        + "<wait/>"
        + _wire(
            "search_blocks",
            {
                "compound": "GLOBcomp_3",
                "property": "GLOBprop_34",
            },
        )
    )
    batch = extract_all_tool_calls(text)
    assert [call["name"] for call in batch.calls] == [
        "resolve_compound_ids"
    ]
    assert batch.wait_detected
    assert batch.deferred_count == 1


@pytest.mark.parametrize(
    "bad_block",
    [
        (
            '<tool_call>{"name":"resolve_property_ids",'
            '"arguments":{"queries":"density"},"extra":true}</tool_call>'
        ),
        (
            '<tool_call>{"name":"resolve_property_ids",'
            '"arguments":["density"]}</tool_call>'
        ),
        (
            '<tool_call>{"name":"resolve_property_ids",'
            '"arguments":{"queries":"density"}</tool_call>'
        ),
    ],
)
def test_malformed_sibling_rejects_entire_wire_batch(
    bad_block: str,
) -> None:
    batch = extract_all_tool_calls(
        _wire("resolve_compound_ids", {"queries": "water"}) + bad_block
    )
    assert not batch.syntax_valid
    assert batch.calls  # parser may recover valid siblings for diagnostics
    assert "entire tool batch was rejected" in batch.correction_message()
    assert "No tool in the batch ran" in batch.correction_message()


@pytest.mark.parametrize(
    "payload",
    [
        (
            '{"name":"resolve_compound_ids","name":"search_blocks",'
            '"arguments":{"queries":"water"}}'
        ),
        (
            '{"name":"resolve_compound_ids","arguments":'
            '{"queries":"water","queries":"methanol"}}'
        ),
        (
            '{"name":"search_similar_compounds","arguments":'
            '{"smiles":"C","min_similarity":NaN}}'
        ),
        (
            '{"name":"search_similar_compounds","arguments":'
            '{"smiles":"C","min_similarity":Infinity}}'
        ),
        (
            '{"name":"search_similar_compounds","arguments":'
            '{"smiles":"C","min_similarity":-Infinity}}'
        ),
        (
            '{"name":"search_similar_compounds","arguments":'
            '{"smiles":"C","min_similarity":1e400}}'
        ),
    ],
)
def test_canonical_json_rejects_duplicate_keys_and_nonfinite_numbers(
    payload: str,
) -> None:
    batch = extract_all_tool_calls(f"<tool_call>{payload}</tool_call>")
    assert not batch.syntax_valid
    assert not batch.calls
    assert "invalid JSON" in batch.correction_message()


def test_rejected_turn_is_archived_stripped_of_narration() -> None:
    executed: list[int] = []

    def echo(value: int) -> dict:
        executed.append(value)
        return {"value": value}

    good = _wire("echo", {"value": 1})
    bad = '<tool_call>{"name":"echo","arguments":{"value":2}</tool_call>'
    fake = "FABRICATED_SESSION_NARRATION " * 120
    memory: list[dict] = []
    client = _SequenceClient([
        fake + good + bad + "<wait/>" + fake,
        "<answer>Recovered.</answer>",
    ])
    result = agent_turn(
        "Run the echo regression.",
        system_prompt="Use canonical tool-call JSON.",
        tools={"echo": echo},
        memory=memory,
        client=client,
        max_iterations=3,
        timeout=120,
        hooks=build_agent_hooks(batch_validator=None).engine_hooks,
    )
    assert result.answer == "Recovered."
    assert executed == []  # atomic rejection: nothing in the batch ran
    rejected = next(m for m in memory if m["role"] == "assistant")
    assert "FABRICATED_SESSION_NARRATION" not in rejected["content"]
    assert "SYNTAX-REJECTED TURN" in rejected["content"]
    assert good in rejected["content"]  # calls kept verbatim for correction
    assert bad in rejected["content"]
    # Rejected calls never pollute tool_history (logs/envelopes/counts).
    assert all(
        not h["tool"].startswith("<malformed") for h in result.tool_history
    )


def test_rejection_debris_scrubbed_after_successful_recovery() -> None:
    executed: list[int] = []

    def echo(value: int) -> dict:
        executed.append(value)
        return {"value": value}

    bad = '<tool_call>{"name":"echo","arguments":{"value":2}</tool_call>'
    fake = "FABRICATED_SESSION_NARRATION " * 120
    memory: list[dict] = []
    client = _SequenceClient([
        fake + bad + "<wait/>",                      # rejected turn
        _wire("echo", {"value": 3}) + "<wait/>",      # successful recovery
        "<answer>Recovered cleanly.</answer>",
    ])
    result = agent_turn(
        "Run the echo regression.",
        system_prompt="Use canonical tool-call JSON.",
        tools={"echo": echo},
        memory=memory,
        client=client,
        max_iterations=4,
        timeout=120,
        hooks=build_agent_hooks(batch_validator=None).engine_hooks,
    )
    assert result.answer == "Recovered cleanly."
    assert executed == [3]
    # The archived rejected turn collapses to a stub once a valid batch runs.
    stubs = [
        m for m in memory
        if m["role"] == "assistant"
        and m["content"].startswith("(syntax-rejected turn")
    ]
    assert len(stubs) == 1
    joined = "\n".join(m["content"] for m in memory)
    assert "SYNTAX-REJECTED TURN" not in joined
    assert "FABRICATED_SESSION_NARRATION" not in joined
    assert bad not in joined  # malformed block gone from working context
    # Clean histories: only the real executed call remains.
    assert [h["tool"] for h in result.tool_history] == ["echo"]


def test_wrapped_l1_preflight_accepts_flat_calls_with_purpose_tasks(
    l1_catalog,
) -> None:
    wrapped = l1_catalog.wrapped_tools()
    calls = [
        {
            "name": "resolve_compound_ids",
            "arguments": {
                "queries": ["water", "carbon dioxide"],
                "purpose": "Resolve compounds for a later block search.",
                "tasks": "Return strict global compound IDs.",
            },
        },
        {
            "name": "block_search_adv",
            "arguments": {
                **copy.deepcopy(ADV_CO2),
                "purpose": "Find exact aligned conductivity rows.",
                "tasks": "Filter, aggregate, and retain DOI/block anchors.",
            },
        },
    ]
    assert _prevalidate_batch_arguments(calls, wrapped) is None


def test_wrapped_l1_preflight_atomically_holds_valid_sibling(
    l1_catalog,
) -> None:
    wrapped = l1_catalog.wrapped_tools()
    calls = [
        {
            "name": "resolve_compound_ids",
            "arguments": {
                "queries": "water",
                "purpose": "Resolve water.",
                "tasks": "Return its strict global ID.",
            },
        },
        {
            "name": "block_search_adv",
            "arguments": {
                "compound_list": [],
                "target_identity": [],
                "explanation": "Use a deliberately retired contract.",
                "purpose": "Exercise atomic preflight.",
                "tasks": "Reject obsolete parameter names.",
            },
        },
    ]
    message = _prevalidate_batch_arguments(calls, wrapped)
    assert message is not None
    assert "compound_list" in message
    assert "held back because the batch is atomic" in message
    assert "No tool in this batch executed" in message


def test_real_independent_resolvers_execute_in_one_ordered_batch(
    l1_catalog,
) -> None:
    events: list[str] = []
    compound_fn = l1_catalog.entries["resolve_compound_ids"].fn
    property_fn = l1_catalog.entries["resolve_property_ids"].fn

    @wraps(compound_fn)
    def compound(**kwargs):
        events.append("compound")
        return compound_fn(**kwargs)

    @wraps(property_fn)
    def prop(**kwargs):
        events.append("property")
        return property_fn(**kwargs)

    responses = [
        (
            _wire("compound", {"queries": ["water", "methanol"], "limit": 3})
            + _wire("prop", {"queries": ["density", "viscosity"], "limit": 3})
            + "<wait/>"
        ),
        "<answer>Both independent resolver calls completed.</answer>",
    ]
    result, _ = _run_sequence(
        responses,
        {"compound": compound, "prop": prop},
    )
    assert result.answer == "Both independent resolver calls completed."
    assert events == ["compound", "property"]


def test_runtime_exception_does_not_cancel_later_batch_sibling() -> None:
    events: list[str] = []

    def fails(query: str) -> dict:
        events.append(f"fail:{query}")
        raise RuntimeError("synthetic chemistry failure")

    def succeeds(query: str) -> dict:
        events.append(f"ok:{query}")
        return {"query": query, "n_results": 1, "results": [{"id": 1}]}
    responses = [
        _wire("fails", {"query": "unobtainium"})
        + _wire("succeeds", {"query": "water"})
        + "<wait/>",
        "<answer>The valid sibling still completed.</answer>",
    ]
    result, client = _run_sequence(
        responses,
        {"fails": fails, "succeeds": succeeds},
    )
    assert result.answer == "The valid sibling still completed."
    assert events == ["fail:unobtainium", "ok:water"]
    assert any(
        "TOOL_EXECUTION_ERROR" in prompt for prompt in client.prompts[1:]
    )


def test_block_search_adv_review_must_be_alone_in_a_batch(l1_catalog) -> None:
    advanced = l1_catalog.entries["block_search_adv"].fn
    events: list[str] = []

    @wraps(advanced)
    def observed(**kwargs):
        events.append(kwargs["explanation"])
        return advanced(**kwargs)

    responses = [
        _wire("block_search_adv", copy.deepcopy(ADV_CO2))
        + _wire("block_search_adv", copy.deepcopy(ADV_REACTION))
        + "<wait/>",
        "<answer>The lifecycle calls must be retried separately.</answer>",
    ]
    result, client = _run_sequence(
        responses,
        {"block_search_adv": observed},
        batch_validator=l1_catalog.validate_batch,
    )
    assert result.answer == "The lifecycle calls must be retried separately."
    assert events == []
    assert len(result.tool_history) == 2
    assert all("[validation " in item["result_full"] for item in result.tool_history)
    prompts = "\n".join(client.prompts[1:])
    assert "must be the only tool call in its batch" in prompts
    assert "No tool in this batch executed" in prompts

def test_stage_compacted_batch_can_be_inspected_on_the_next_turn(
    monkeypatch,
) -> None:
    base_config = react_loop_module.get_config()
    monkeypatch.setattr(
        react_loop_module,
        "get_config",
        lambda: replace(base_config, STAGE_COMPACT_BUDGET=10),
    )

    def first(query: str) -> dict:
        return {"query": query, "payload": "full-first-result"}

    def second(query: str) -> dict:
        return {"query": query, "payload": "full-second-result"}

    tools = {"first": first, "second": second}
    responses = [
        _wire("first", {"query": "water"})
        + _wire("second", {"query": "methanol"})
        + "<wait/>",
        _wire("inspect_batch_result", {"tool_number": 1}) + "<wait/>",
        "<answer>The inspected result remained available.</answer>",
    ]
    result, client = _run_sequence(responses, tools)
    assert result.answer == "The inspected result remained available."
    assert [item["tool"] for item in result.tool_history] == [
        "first",
        "second",
        "inspect_batch_result",
    ]
    assert "full-first-result" in result.tool_history[-1]["result_full"]
    assert "full-first-result" in client.prompts[-1]
    assert "inspect_batch_result" not in tools


def test_oversized_result_gets_warning_banner_and_sibling_runs(
    monkeypatch,
) -> None:
    base_config = react_helpers.get_config()
    monkeypatch.setattr(
        react_helpers,
        "get_config",
        lambda: replace(base_config, TOOL_RESULT_CHAR_LIMIT=120),
    )
    events: list[str] = []

    def oversized(query: str) -> dict:
        events.append(f"large:{query}")
        return {"query": query, "payload": "x" * 500}

    def ordinary(query: str) -> dict:
        events.append(f"ordinary:{query}")
        return {"query": query, "status": "ok"}

    responses = [
        _wire("oversized", {"query": "water"})
        + _wire("ordinary", {"query": "methanol"})
        + "<wait/>",
        "<answer>The second result survived the first size warning.</answer>",
    ]
    result, _ = _run_sequence(
        responses,
        {"oversized": oversized, "ordinary": ordinary},
    )
    assert result.answer == (
        "The second result survived the first size warning."
    )
    assert events == ["large:water", "ordinary:methanol"]
    assert [
        item["tool"] for item in result.tool_history
    ] == ["oversized", "ordinary"]
    # The oversized result carries the banner AND the full payload.
    assert (
        "TOOL_RESULT_SIZE_WARNING"
        in result.tool_history[0]["result_full"]
    )
    assert "x" * 500 in result.tool_history[0]["result_full"]
    assert (
        "TOOL_RESULT_SIZE_WARNING"
        not in result.tool_history[1]["result_full"]
    )


def test_four_l2_delegation_boundaries_parse_and_dispatch_as_a_batch(
    monkeypatch,
) -> None:
    from NIST_ThermoML_agents.NIST_ThermoML_query_agent.query_agent_workflows.L1_workers import (
        l1_query_dispatcher as dispatcher,
    )

    events: list[tuple[str, str]] = []

    def fake(kind: str):
        def dispatch(
            purpose: str,
            instruction: str = "",
            context: str = "",
            id_catalog: str = "",
            **kwargs,
        ) -> str:
            del purpose, instruction, id_catalog, kwargs
            events.append((kind, context))
            return f"{kind} evaluation complete for {context}"

        return dispatch

    monkeypatch.setattr(dispatcher, "dispatch_l2_comp_eval", fake("compound"))
    monkeypatch.setattr(
        dispatcher,
        "dispatch_l2_meas_eval",
        fake("measurement"),
    )
    monkeypatch.setattr(
        dispatcher,
        "dispatch_l2_ref_eval",
        fake("reference"),
    )
    monkeypatch.setattr(
        dispatcher,
        "dispatch_l2_prop_eval",
        fake("property"),
    )
    catalog = dispatcher.QueryL1Catalog()
    tools = {
        name: catalog.tools[name]
        for name in (
            "L2_comp_eval",
            "L2_meas_eval",
            "L2_ref_eval",
            "L2_prop_eval",
        )
    }
    context = (
        "DOI 10.1007/s10765-005-5566-6, PROPblock_1, "
        "GLOBcomp_3, GLOBprop_34"
    )
    responses = [
        "".join(
            _wire(
                name,
                {
                    "purpose": f"Evaluate {kind} metadata.",
                    "instruction": "Use the explicit block context.",
                    "context": context,
                    "id_catalog": "",
                },
            )
            for name, kind in (
                ("L2_comp_eval", "compound"),
                ("L2_meas_eval", "measurement"),
                ("L2_ref_eval", "reference"),
                ("L2_prop_eval", "property"),
            )
        )
        + "<wait/>",
        "<answer>All four block-domain evaluations completed.</answer>",
    ]
    result, _ = _run_sequence(responses, tools)
    assert result.answer == "All four block-domain evaluations completed."
    assert [kind for kind, _ in events] == [
        "compound",
        "measurement",
        "reference",
        "property",
    ]
    assert all(block_context == context for _, block_context in events)
