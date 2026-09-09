"""Tests for subagent-answer context envelopes."""

from __future__ import annotations

import json
import unittest
from types import SimpleNamespace
from unittest.mock import patch

from .context_markers import (
    ALL_CONTEXT_MARKERS_RE,
    MARKERS,
    mark_subagent_answer_tool,
    wrap_subagent_answer,
)
from ..general_argo_engine_helpers.engine_react_helpers.react_loop import agent_turn
from ..general_tool_management_helpers.general_agent_tool_catalog import (
    AgentToolCatalog,
    ToolEntry,
)


class _TwoTurnClient:
    def __init__(self) -> None:
        self.prompts: list[str] = []
        self.responses = [
            '<tool_call>{"name":"delegated","arguments":{}}</tool_call>\n<wait/>',
            '<answer>Finished.</answer>',
        ]

    def call(self, prompt: str, system: str, **kwargs) -> str:
        self.prompts.append(prompt)
        return self.responses.pop(0)


class SubagentAnswerMarkerTests(unittest.TestCase):
    def test_wraps_complete_json_exactly_once(self) -> None:
        payload = {
            "answer": "Water is the solvent.",
            "core_claims": ["Water is the central solvent."],
            "sources": [{"lit_num_id": "GLOBlit_1"}],
        }
        wrapped = wrap_subagent_answer(payload)
        self.assertTrue(wrapped.startswith("<subagent_answer>\n"))
        self.assertTrue(wrapped.endswith("\n</subagent_answer>"))
        match = MARKERS.subagent_answer_re.fullmatch(wrapped)
        self.assertIsNotNone(match)
        self.assertEqual(json.loads(match.group(1)), payload)
        self.assertEqual(wrap_subagent_answer(wrapped), wrapped)
        self.assertEqual(wrapped.count("<subagent_answer>"), 1)
        self.assertEqual(wrapped.count("</subagent_answer>"), 1)

    def test_rejects_non_json_subagent_content(self) -> None:
        with self.assertRaisesRegex(ValueError, "must be a JSON object or array"):
            wrap_subagent_answer("ordinary prose")

    def test_rejects_malformed_content_inside_existing_envelope(self) -> None:
        with self.assertRaisesRegex(ValueError, "must be a JSON object or array"):
            wrap_subagent_answer(
                "<subagent_answer>\nordinary prose\n</subagent_answer>"
            )
    def test_master_marker_cleanup_knows_subagent_answer(self) -> None:
        wrapped = wrap_subagent_answer({"answer": "A", "core_claims": ["C"]})
        stripped = ALL_CONTEXT_MARKERS_RE.sub("", wrapped).strip()
        self.assertEqual(json.loads(stripped)["answer"], "A")

    def test_sync_react_wraps_marked_tool_json_before_parent_reads_it(self) -> None:
        @mark_subagent_answer_tool
        def delegated() -> dict:
            return {
                "answer": "Subagent answer.",
                "core_claims": ["Central supported claim."],
                "status": "success",
            }

        client = _TwoTurnClient()
        test_config = SimpleNamespace(
            WARN_THRESHOLDS=[0.75, 0.9],
            MAX_WRAP_WARNINGS=2,
            MAX_EMPTY_WAITS=2,
            SUMMARY_MAX_CHARS=2_000,
            STAGE_COMPACT_BUDGET=100_000,
            STAGE_NOTE_CHARS=1_000,
            GUIDANCE_MAX_TOKENS=500,
            TOOL_RESULT_CHAR_LIMIT=100_000,
            COMPACTION_TRIGGER_CHARS=100_000,
        )
        hooks = {
            "context.sync.time_budget.tracker.create": (
                lambda **_: object(),
            ),
            "context.sync.time_budget.warnings.apply": (
                lambda **_: None,
            ),
            "context.sync.time_budget.hard_stop.check": (
                lambda **_: False,
            ),
            "tool.sync.tool_calls_memory.compact": (
                lambda tool_calls, **_: "\n".join(
                    f"{call['name']}()" for call in tool_calls
                ),
            ),
        }
        with patch(
            "NIST_ThermoML_agents.general_db_query_engine."
            "general_argo_engine_helpers.engine_react_helpers.react_loop.get_config",
            return_value=test_config,
        ), patch(
            "NIST_ThermoML_agents.general_db_query_engine."
            "general_argo_engine_helpers.engine_react_helpers.react_helpers.get_config",
            return_value=test_config,
        ):
            result = agent_turn(
                "Use the delegated agent.",
                system_prompt="Call the tool, then answer.",
                tools={"delegated": delegated},
                memory=[],
                client=client,
                max_iterations=3,
                timeout=30,
                hooks=hooks,
            )
        self.assertEqual(result.answer, "Finished.")
        self.assertEqual(len(result.tool_history), 1)
        recorded = result.tool_history[0]["result_full"]
        self.assertEqual(recorded.count("<subagent_answer>"), 1)
        self.assertIn('"core_claims"', recorded)
        self.assertIn("<subagent_answer>", client.prompts[1])
        self.assertIn("</subagent_answer>", client.prompts[1])

    def test_catalog_agent_result_bypasses_compaction_and_keeps_full_json(self) -> None:
        @mark_subagent_answer_tool
        def delegated() -> dict:
            return {
                "answer": "Full result.",
                "core_claims": ["Full central claim."],
                "nested": {"kept": [1, 2, 3]},
            }

        def forbidden_compactor(data: dict) -> str:
            raise AssertionError("subagent JSON must not be compacted")

        catalog = AgentToolCatalog(entries=[
            ToolEntry(
                "delegated",
                delegated,
                compactor_fn=forbidden_compactor,
                skip_subagent=True,
            )
        ])
        wrapped_tool = catalog.wrapped_tools()["delegated"]
        result = wrapped_tool(purpose="Obtain full result", tasks="Return all fields")
        self.assertEqual(result.count("<subagent_answer>"), 1)
        parsed = json.loads(MARKERS.subagent_answer_re.fullmatch(result).group(1))
        self.assertEqual(parsed["nested"], {"kept": [1, 2, 3]})
        self.assertTrue(getattr(wrapped_tool, "_returns_subagent_answer", False))


if __name__ == "__main__":
    unittest.main()
