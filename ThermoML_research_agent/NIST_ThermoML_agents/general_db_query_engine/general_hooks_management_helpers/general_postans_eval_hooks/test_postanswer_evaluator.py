"""Tests for the shared answer-only post-answer evaluation lifecycle."""

from __future__ import annotations

import json
import threading
import unittest
from contextvars import ContextVar

from ._postans_eval_anchors_catalog import POSTANS_PARALLEL_AGENTS_DISPATCH
from .postanswer_evaluator import (
    assemble_return_json,
    build_core_claims_schema,
    build_id_alignment_schema,
    build_id_alignment_agent_schema,
    validate_response_json_schema,
    evaluate_and_assemble_return,
    extract_answer_text,
    prepare_answer_only_system_prompt,
)


_DOI = "10.1007/s10765-005-5566-6"
_LIT = "GLOBlit_1"
_ACTIVE_RUN = ContextVar("postanswer_test_active_run", default=None)


class _ParallelFakeClient:
    def __init__(
        self,
        *,
        core_claims_evaluation: dict,
        id_alignment: dict,
        summary: dict | None = None,
        barrier: threading.Barrier | None = None,
    ) -> None:
        self.core_claims_evaluation = core_claims_evaluation
        self.id_alignment = id_alignment
        self.summary = summary or {"summary": "Concise supported summary."}
        self.barrier = barrier
        self.calls: list[dict] = []
        self._lock = threading.Lock()

    def call(self, prompt: str, system: str, *, max_tokens: int) -> str:
        if "core-claims distillation agent" in system:
            branch = "core_claims"
        elif "answer-summary constructor" in system:
            branch = "summary"
        else:
            branch = "id_alignment"
        with self._lock:
            self.calls.append(
                {
                    "branch": branch,
                    "prompt": prompt,
                    "system": system,
                    "max_tokens": max_tokens,
                    "thread_id": threading.get_ident(),
                    "active_run": _ACTIVE_RUN.get(),
                }
            )
        if self.barrier is not None:
            self.barrier.wait(timeout=3)
        if branch == "core_claims":
            value = self.core_claims_evaluation
        elif branch == "summary":
            value = self.summary
        else:
            value = self.id_alignment
        return json.dumps(value)


class PostAnswerEvaluatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.response_json_schema = {
            "answer": "Full answer.",
            "core_claims": ["Claim."],
            "status": "success | partial | no_results",
            "sources": [
                {
                    "doi": "...",
                    "lit_num_id": "GLOBlit_N",
                    "block": "PROPblock_N",
                }
            ],
        }

    @staticmethod
    def _passthrough_sources_processor(*, id_alignment, **_kwargs):
        """Sources-declaring schemas require a validator; tests pass through."""
        return id_alignment

    def test_working_prompt_requires_parser_redaction(self) -> None:
        leaked_source = """
# Agent

# Response JSON Schema

```json
{"answer": "...", "status": "success"}
```
"""
        with self.assertRaisesRegex(ValueError, "ANSWER_PROMPT_SCHEMA_LEAK"):
            prepare_answer_only_system_prompt(leaked_source)

        prepared = prepare_answer_only_system_prompt("# Agent\n\nDo chemistry.")
        self.assertNotIn("# Response JSON Schema", prepared)
        self.assertIn("Do not emit JSON", prepared)
        self.assertTrue(
            prepared.endswith(
                "parallel post-answer agents create every JSON field after "
                "termination."
            )
        )

    def test_answer_extraction_rejects_machine_fields(self) -> None:
        self.assertEqual(
            extract_answer_text("Water is the solvent."),
            "Water is the solvent.",
        )
        with self.assertRaisesRegex(
            ValueError,
            "WORKING_AGENT_ANSWER_CONTRACT_ERROR",
        ):
            extract_answer_text('{"answer": "Water is the solvent."}')
        with self.assertRaisesRegex(
            ValueError,
            "WORKING_AGENT_ANSWER_CONTRACT_ERROR",
        ):
            extract_answer_text(
                '{"answer": "Water is the solvent.", "core_claims": ["extra"]}'
            )

    def test_common_fields_are_owned_by_final_schema(self) -> None:
        final_schema = validate_response_json_schema(
            {"answer": "old", "core_claims": ["old"], "status": "success"}
        )
        self.assertEqual(
            list(final_schema),
            ["answer", "core_claims", "status"],
        )
        self.assertEqual(
            list(build_core_claims_schema(final_schema)),
            ["core_claims"],
        )
        self.assertEqual(
            list(build_id_alignment_schema(final_schema)),
            ["status"],
        )
        summary_schema = {
            "answer": "old",
            "core_claims": ["old"],
            "status": "success",
            "summary": "brief",
        }
        self.assertEqual(
            list(build_id_alignment_schema(summary_schema)),
            ["status", "summary"],
        )
        self.assertEqual(
            list(build_id_alignment_agent_schema(summary_schema)),
            ["status"],
        )

    def test_deterministic_assembly_keeps_answer_and_identifier_pair(self) -> None:
        answer = "The paper reports a carbon-dioxide data block."
        assembled = assemble_return_json(
            answer=answer,
            core_claims_evaluation={
                "core_claims": [
                    "The paper reports a carbon-dioxide data block.",
                    "The block retains the experimental context.",
                ],
            },
            id_alignment={
                "status": "success",
                "sources": [
                    {
                        "doi": _DOI,
                        "lit_num_id": _LIT,
                        "block": "PROPblock_1",
                    }
                ],
            },
            response_json_schema=self.response_json_schema,
        )
        self.assertEqual(assembled["answer"], answer)
        self.assertEqual(len(assembled["core_claims"]), 2)
        self.assertEqual(assembled["sources"][0]["doi"], _DOI)
        self.assertEqual(assembled["sources"][0]["lit_num_id"], _LIT)

    def test_two_agents_fire_in_parallel_from_one_anchor_then_join(self) -> None:
        core_claims_evaluation = {
            "core_claims": ["The block reports carbon-dioxide measurements."],
        }
        id_alignment = {
            "status": "success",
            "sources": [
                {
                    "doi": _DOI,
                    "lit_num_id": _LIT,
                    "block": "PROPblock_1",
                }
            ],
        }
        client = _ParallelFakeClient(
            core_claims_evaluation=core_claims_evaluation,
            id_alignment=id_alignment,
            barrier=threading.Barrier(2),
        )
        anchor_calls: list[dict] = []

        def _on_parallel_start(**kwargs):
            anchor_calls.append(kwargs)

        hooks = {
            POSTANS_PARALLEL_AGENTS_DISPATCH.anchor_type: (_on_parallel_start,),
        }
        validator_calls: list[dict] = []
        token = _ACTIVE_RUN.set("parent-run")
        try:
            result = evaluate_and_assemble_return(
                agent_answer=(
                    "The block reports carbon-dioxide measurements and provides "
                    "the experimental context needed to interpret them."
                ),
                response_json_schema=self.response_json_schema,
                client=client,
                label="fixture",
                task_context="Find the carbon-dioxide block.",
                tool_history=[
                    {
                        "iteration": 1,
                        "tool": "search_blocks",
                        "arguments": {"literature": _DOI},
                        "result_full": json.dumps(
                            {
                                "doi": _DOI,
                                "lit_num_id": _LIT,
                                "block_number": "PROPblock_1",
                            }
                        ),
                    }
                ],
                hooks=hooks,
                validator=lambda payload: validator_calls.append(payload),
                id_alignment_processor=self._passthrough_sources_processor,
                max_retries=0,
            )
        finally:
            _ACTIVE_RUN.reset(token)
        self.assertEqual(len(anchor_calls), 1)
        self.assertEqual(
            anchor_calls[0]["branches"],
            ("core_claims", "id_alignment"),
        )
        self.assertEqual(len(client.calls), 2)
        self.assertEqual(
            {call["branch"] for call in client.calls},
            {"core_claims", "id_alignment"},
        )
        self.assertEqual(
            len({call["thread_id"] for call in client.calls}),
            2,
        )
        self.assertEqual(
            {call["active_run"] for call in client.calls},
            {"parent-run"},
        )
        self.assertTrue(
            all("no tools" in call["system"] for call in client.calls)
        )
        core_claims_call = next(
            call for call in client.calls if call["branch"] == "core_claims"
        )
        id_call = next(
            call for call in client.calls if call["branch"] == "id_alignment"
        )
        self.assertNotIn("Completed run record", core_claims_call["prompt"])
        self.assertNotIn("Original task context", core_claims_call["prompt"])
        self.assertIn("one or several", core_claims_call["system"])
        self.assertIn("well-supported central", core_claims_call["system"])
        self.assertIn("Example input answer", core_claims_call["system"])
        self.assertIn('"core_claims"', core_claims_call["system"])
        self.assertIn("Completed run record", id_call["prompt"])
        self.assertNotIn('"answer":', core_claims_call["prompt"].split(
            "## Required core-claims JSON schema", 1
        )[1])
        self.assertNotIn('"core_claims":', id_call["prompt"].split(
            "## Required ID/metadata JSON schema", 1
        )[1])
        self.assertEqual(result.answer, result.assembled["answer"])
        self.assertEqual(result.core_claims_evaluation, core_claims_evaluation)
        self.assertEqual(result.id_alignment, id_alignment)
        self.assertEqual(validator_calls, [result.assembled])

    def test_summary_tool_is_separate_from_claims_and_id_agent(self) -> None:
        schema = {
            "answer": "Full answer.",
            "core_claims": ["Central claim."],
            "status": "success | partial | no_results",
            "sources": [],
            "summary": "Concise summary.",
        }
        client = _ParallelFakeClient(
            core_claims_evaluation={"core_claims": ["Supported claim."]},
            id_alignment={"status": "success", "sources": []},
            summary={"summary": "Answer-only summary."},
        )
        result = evaluate_and_assemble_return(
            agent_answer="The selected block supports the reported trend.",
            response_json_schema=schema,
            client=client,
            label="summary-fixture",
            id_alignment_processor=self._passthrough_sources_processor,
            max_retries=0,
        )
        self.assertEqual(result.assembled["summary"], "Answer-only summary.")
        self.assertEqual(len(client.calls), 3)
        calls = {call["branch"]: call for call in client.calls}
        self.assertEqual(set(calls), {"core_claims", "id_alignment", "summary"})
        self.assertNotIn('"summary"', calls["id_alignment"]["prompt"].split(
            "## Required ID/metadata JSON schema", 1
        )[1])
        self.assertNotIn("Completed run record", calls["summary"]["prompt"])
        self.assertNotIn("Original task context", calls["summary"]["prompt"])
        self.assertIn("answer-summary constructor", calls["summary"]["system"])
        self.assertIn("Example output", calls["core_claims"]["system"])
    def test_id_agent_cannot_add_core_claims_or_undeclared_fields(self) -> None:
        client = _ParallelFakeClient(
            core_claims_evaluation={"core_claims": ["Supported claim."]},
            id_alignment={
                "core_claims": ["Supported claim."],
                "status": "success",
                "sources": [],
                "extra": "not allowed",
            },
        )
        # undeclared fields are rejected by the json guard itself (it flags
        # extras for correction); with no retries the branch fails closed
        with self.assertRaisesRegex(
            ValueError,
            "id_alignment worker returned invalid JSON",
        ):
            evaluate_and_assemble_return(
                agent_answer="Supported claim.",
                response_json_schema=self.response_json_schema,
                client=client,
                label="fixture",
                id_alignment_processor=self._passthrough_sources_processor,
                max_retries=0,
            )


if __name__ == "__main__":
    unittest.main()

