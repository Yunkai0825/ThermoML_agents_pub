"""Focused tests for the two post-answer core-ID construction tools."""

from __future__ import annotations

import json
import unittest

from .core_id_management import (
    CORE_ID_MANAGEMENT_TOOL_CATALOG,
    CoreIDValidationError,
    construct_core_blocks_found,
    construct_core_id_updates,
    construct_l1_core_id_alignment,
    refine_and_enrich_l1_core_ids,
)
from ..strict_output_contracts import validate_l1_query_output
from ....general_db_query_engine.general_hooks_management_helpers.general_postans_eval_hooks import (
    POSTANS_CORE_ID_REFINEMENT,
    POSTANS_CORE_ID_TOOLS_AFTER,
    POSTANS_CORE_ID_TOOLS_BEFORE,
    POSTANS_SUBMISSION_REVIEW,
    evaluate_and_assemble_return,
)


_CORE_BLOCK = {
    "lit_num_id": "GLOBlit_1",
    "block_number": "PROPblock_1",
    "BLKsubsys_id": None,
    "system_type": "unary",
    "comp_num_ids": ["GLOBcomp_3"],
    "prop_num_ids": ["GLOBprop_34"],
    "description": "Thermal-conductivity measurements for carbon dioxide.",
}

_CORE_ALIGNMENT = {
    "status": "success",
    "summary": "One matching block.",
    "core_id_updates": [
        {"action": "add", "core_GLOB_id": "GLOBcomp_3"},
    ],
    "core_blocks_found": [_CORE_BLOCK],
}

_ALIGNMENT_SCHEMA = {
    "status": "success | partial | no_results",
    "summary": "Brief summary.",
    "core_id_updates": [
        {"action": "add", "core_GLOB_id": "GLOBcomp_3"},
    ],
    "core_blocks_found": [_CORE_BLOCK],
}


class _QueuedClient:
    def __init__(self, responses: list[dict]) -> None:
        self.responses = list(responses)
        self.calls: list[dict] = []

    def call(self, prompt: str, system: str, *, max_tokens: int) -> str:
        self.calls.append(
            {"prompt": prompt, "system": system, "max_tokens": max_tokens}
        )
        if not self.responses:
            raise AssertionError("unexpected model call")
        return json.dumps(self.responses.pop(0))

class _PostAnswerClient:
    def call(self, prompt: str, system: str, *, max_tokens: int) -> str:
        if "core-claims distillation agent" in system:
            return json.dumps({"core_claims": ["One block was found."]})
        if "answer-summary constructor" in system:
            return json.dumps({"summary": _CORE_ALIGNMENT["summary"]})
        if "ID-and-metadata alignment agent" in system:
            return json.dumps(
                {key: value for key, value in _CORE_ALIGNMENT.items()
                 if key != "summary"}
            )
        if "final submission reviewer" in system:
            return json.dumps(
                {"decision": "submit", "reason": "Validated and sufficient."}
            )
        raise AssertionError(f"unexpected post-answer system prompt: {system[:80]}")


class CoreIDManagementTests(unittest.TestCase):
    def test_catalog_registers_exactly_two_hidden_batch_tools(self) -> None:
        self.assertEqual(
            set(CORE_ID_MANAGEMENT_TOOL_CATALOG.tools),
            {"construct_core_blocks_found", "construct_core_id_updates"},
        )
        for entry in CORE_ID_MANAGEMENT_TOOL_CATALOG.entries.values():
            self.assertTrue(entry.skip_compactor)
            self.assertTrue(entry.skip_subagent)

    def test_block_tool_constructs_database_context(self) -> None:
        result = construct_core_blocks_found([dict(_CORE_BLOCK)])
        self.assertEqual(set(result), {"core_blocks_found"})
        block = result["core_blocks_found"][0]
        self.assertEqual(block["doi"], "10.1007/s10765-005-5566-6")
        self.assertEqual(block["n_datapoints"], 77)
        self.assertEqual(block["compounds"][0]["name"], "carbon dioxide")
        self.assertEqual(block["variables"][0]["BLKvar_id"], "BLKvar_1")
        self.assertEqual(block["properties"][0]["BLKprop_id"], "BLKprop_1")
        self.assertIn("range_min", block["properties"][0])

    def test_real_subsystem_block_context_is_projected_from_raw_rows(self) -> None:
        result = construct_core_blocks_found([{
            "lit_num_id": "GLOBlit_608",
            "block_number": "PROPblock_1",
            "BLKsubsys_id": "BLKsubsys_2",
            "system_type": "binary",
            "comp_num_ids": ["GLOBcomp_74", "GLOBcomp_1"],
            "prop_num_ids": ["GLOBprop_8"],
            "description": "Aqueous alanine binary composition face.",
        }])["core_blocks_found"][0]
        self.assertEqual(result["n_datapoints"], 72)
        self.assertEqual(result["declared_system_type"], "ternary")
        self.assertEqual(result["declared_n_components"], 3)
        self.assertEqual(
            [item["comp_num_id"] for item in result["compounds"]],
            ["GLOBcomp_74", "GLOBcomp_1"],
        )
        self.assertEqual(
            [item["BLKvar_id"] for item in result["variables"]],
            ["BLKvar_2", "BLKvar_3"],
        )
        prop = result["properties"][0]
        self.assertEqual(prop["range"]["n"], 72)
        self.assertEqual(prop["range_min"], 1447.59)
        self.assertEqual(prop["range_max"], 1588.1)
        self.assertEqual(result["subsystem_point_runs"], [[1, 72]])
        self.assertEqual(result["subsystem_evidence_quality"], "exact_reported_zero")

    def test_block_tool_rejects_checksum_mismatch(self) -> None:
        wrong = dict(_CORE_BLOCK)
        wrong["comp_num_ids"] = ["GLOBcomp_1"]
        with self.assertRaisesRegex(
            CoreIDValidationError,
            "construct|checksum mismatch|comp_num_ids",
        ):
            construct_l1_core_id_alignment(
                {**_CORE_ALIGNMENT, "core_blocks_found": [wrong]}
            )

    def test_update_tool_constructs_registry_owned_names(self) -> None:
        result = construct_core_id_updates(
            [{"action": "add", "core_GLOB_id": "GLOBcomp_3"}]
        )
        self.assertEqual(
            result["core_id_updates"],
            [
                {
                    "action": "add",
                    "core_GLOB_id": "GLOBcomp_3",
                    "registry_id": "carbon_dioxide",
                    "name": "carbon dioxide",
                }
            ],
        )

    def test_strict_final_validator_reconstructs_tool_outputs(self) -> None:
        constructed = construct_l1_core_id_alignment(_CORE_ALIGNMENT)
        payload = {
            "answer": "Carbon-dioxide conductivity data were found.",
            "core_claims": ["One matching carbon-dioxide block was found."],
            "data_inspections": [],
            **constructed,
        }
        self.assertIs(validate_l1_query_output(payload), payload)
        payload["core_id_updates"][0]["name"] = "agent-authored replacement"
        with self.assertRaisesRegex(ValueError, "canonical output"):
            validate_l1_query_output(payload)

    def test_validation_error_becomes_react_observation(self) -> None:
        wrong = dict(_CORE_BLOCK)
        wrong["prop_num_ids"] = ["GLOBprop_1"]
        corrected = {
            **_CORE_ALIGNMENT,
            "core_blocks_found": [dict(_CORE_BLOCK)],
        }
        client = _QueuedClient(
            [
                {key: value for key, value in corrected.items()
                 if key != "summary"},
                {"decision": "submit", "reason": "Validated and sufficient."},
            ]
        )
        result = refine_and_enrich_l1_core_ids(
            id_alignment={
                **_CORE_ALIGNMENT,
                "core_blocks_found": [wrong],
            },
            client=client,
            id_alignment_schema=_ALIGNMENT_SCHEMA,
            id_alignment_prompt="base alignment prompt",
            answer="One matching carbon-dioxide block was found.",
            core_claims_evaluation={"core_claims": ["One block was found."]},
            completed_run_record="[]",
            label="test-L1",
            max_tokens=2000,
        )
        self.assertEqual(result["core_blocks_found"][0]["prop_num_ids"], ["GLOBprop_34"])
        self.assertEqual(len(client.calls), 2)
        self.assertIn("checksum mismatch", client.calls[0]["prompt"])
        self.assertEqual(result["summary"], _CORE_ALIGNMENT["summary"])
        self.assertNotIn('"summary"', client.calls[0]["prompt"].split(
            "## Current minimal core-ID action", 1
        )[1])

    def test_final_review_can_route_back_to_refinement(self) -> None:
        client = _QueuedClient(
            [
                {"decision": "refine", "reason": "Recheck the selected block."},
                {key: value for key, value in _CORE_ALIGNMENT.items()
                 if key != "summary"},
                {"decision": "submit", "reason": "Validated after refinement."},
            ]
        )
        result = refine_and_enrich_l1_core_ids(
            id_alignment=dict(_CORE_ALIGNMENT),
            client=client,
            id_alignment_schema=_ALIGNMENT_SCHEMA,
            id_alignment_prompt="base alignment prompt",
            answer="One matching carbon-dioxide block was found.",
            core_claims_evaluation={"core_claims": ["One block was found."]},
            completed_run_record="[]",
            label="test-L1",
            max_tokens=2000,
        )
        self.assertEqual(result["core_blocks_found"][0]["n_datapoints"], 77)
        self.assertEqual(len(client.calls), 3)
        self.assertIn("Final submission review", client.calls[1]["prompt"])

    def test_hidden_tool_lifecycle_anchors_cover_refinement_and_review(self) -> None:
        wrong = dict(_CORE_BLOCK)
        wrong["comp_num_ids"] = ["GLOBcomp_1"]
        client = _QueuedClient(
            [
                {key: value for key, value in _CORE_ALIGNMENT.items()
                 if key != "summary"},
                {"decision": "submit", "reason": "Validated after correction."},
            ]
        )
        events: list[tuple[str, dict]] = []

        def capture(name: str):
            def _capture(**kwargs):
                events.append((name, kwargs))
            return _capture

        hooks = {
            POSTANS_CORE_ID_TOOLS_BEFORE.anchor_type: (capture("before"),),
            POSTANS_CORE_ID_TOOLS_AFTER.anchor_type: (capture("after"),),
            POSTANS_CORE_ID_REFINEMENT.anchor_type: (capture("refine"),),
            POSTANS_SUBMISSION_REVIEW.anchor_type: (capture("review"),),
        }
        result = refine_and_enrich_l1_core_ids(
            id_alignment={
                **_CORE_ALIGNMENT,
                "core_blocks_found": [wrong],
            },
            client=client,
            id_alignment_schema=_ALIGNMENT_SCHEMA,
            id_alignment_prompt="base alignment prompt",
            answer="One matching carbon-dioxide block was found.",
            core_claims_evaluation={"core_claims": ["One block was found."]},
            completed_run_record="[]",
            label="test-L1",
            max_tokens=2000,
            engine_hooks=hooks,
        )
        self.assertEqual(result["core_blocks_found"][0]["n_datapoints"], 77)
        self.assertEqual(
            [name for name, _ in events],
            ["before", "after", "refine", "before", "after", "review"],
        )
        self.assertTrue(events[1][1]["errors"])
        self.assertEqual(events[-1][1]["decision"], "submit")

    def test_shared_postanswer_evaluator_runs_hidden_tool_processor(self) -> None:
        final_schema = {
            "answer": "Full chemistry answer.",
            "core_claims": ["One central claim."],
            "data_inspections": [],
            **_ALIGNMENT_SCHEMA,
        }
        events: list[str] = []
        hooks = {
            POSTANS_CORE_ID_TOOLS_BEFORE.anchor_type: (
                lambda **_: events.append("before"),
            ),
            POSTANS_CORE_ID_TOOLS_AFTER.anchor_type: (
                lambda **_: events.append("after"),
            ),
            POSTANS_SUBMISSION_REVIEW.anchor_type: (
                lambda **_: events.append("review"),
            ),
        }
        result = evaluate_and_assemble_return(
            agent_answer="One matching carbon-dioxide block was found.",
            response_json_schema=final_schema,
            client=_PostAnswerClient(),
            label="test-query-L1",
            tool_history=[],
            task_context="Find carbon-dioxide conductivity data.",
            hooks=hooks,
            validator=validate_l1_query_output,
            id_alignment_processor=refine_and_enrich_l1_core_ids,
            deterministic_fields={"data_inspections": []},
        )
        self.assertEqual(
            result.assembled["core_blocks_found"][0]["n_datapoints"],
            77,
        )
        self.assertEqual(
            result.assembled["core_id_updates"][0]["registry_id"],
            "carbon_dioxide",
        )
        self.assertEqual(events, ["before", "after", "review"])


if __name__ == "__main__":
    unittest.main()
