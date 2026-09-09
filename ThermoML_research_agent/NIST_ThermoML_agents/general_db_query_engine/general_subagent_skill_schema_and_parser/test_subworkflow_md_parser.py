"""Tests for the strict agent-skill response-schema channel."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from .subworkflow_md_parser import parse_workflow


def _skill_markdown(schema_heading: str, schema: dict) -> str:
    return f"""---
agent_id: fixture
layer: 1
parent: parent
---

<system_prompt>
# Agent

Do chemistry and return only the answer text.

# Prompt Template

## Purpose
{{{{purpose}}}}

{schema_heading}

```json
{json.dumps(schema, indent=2)}
```

# Phases

## phase_1: answer
tools: []
guidance: |
  Answer the task.
</system_prompt>
"""


class ResponseJsonSchemaParserTests(unittest.TestCase):
    def _parse_text(self, text: str) -> dict:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "fixture_workflow.md"
            path.write_text(text, encoding="utf-8")
            return parse_workflow(path)

    def test_schema_is_separated_from_answer_agent_prompt(self) -> None:
        schema = {
            "answer": "Complete chemistry answer.",
            "core_claims": ["One checkable chemistry claim."],
            "status": "success | partial | no_results",
        }
        parsed = self._parse_text(
            _skill_markdown("# Response JSON Schema", schema)
        )

        self.assertEqual(parsed["response_json_schema"], schema)
        self.assertNotIn("response_json_schema", parsed["system_prompt"])
        self.assertNotIn("# Response JSON Schema", parsed["system_prompt"])
        self.assertNotIn('"status"', parsed["system_prompt"])
        self.assertNotIn("output_schema", parsed)

    def test_legacy_output_schema_heading_is_rejected(self) -> None:
        text = _skill_markdown(
            "# Output Schema",
            {
                "answer": "Answer.",
                "core_claims": ["Claim."],
            },
        )
        with self.assertRaisesRegex(
            ValueError,
            "must contain exactly one '# Response JSON Schema'",
        ):
            self._parse_text(text)

    def test_duplicate_response_schema_is_rejected(self) -> None:
        schema = {
            "answer": "Answer.",
            "core_claims": ["Claim."],
        }
        text = _skill_markdown("# Response JSON Schema", schema)
        duplicate = """
# Response JSON Schema

```json
{"answer": "Answer.", "core_claims": ["Claim."]}
```
"""
        text = text.replace("</system_prompt>", duplicate + "\n</system_prompt>")
        with self.assertRaisesRegex(
            ValueError,
            "must contain exactly one '# Response JSON Schema'",
        ):
            self._parse_text(text)

    def test_required_common_fields_are_not_synthesized(self) -> None:
        with self.assertRaisesRegex(
            ValueError,
            "missing required fields: core_claims",
        ):
            self._parse_text(
                _skill_markdown(
                    "# Response JSON Schema",
                    {"answer": "Answer.", "status": "success"},
                )
            )

    def test_all_thermoml_agent_skills_use_the_separate_schema_channel(
        self,
    ) -> None:
        root = Path(__file__).resolve().parents[2]
        workflow_paths = sorted(root.rglob("*workflow.md"))
        self.assertEqual(len(workflow_paths), 10)

        agent_ids: set[str] = set()
        for path in workflow_paths:
            parsed = parse_workflow(path)
            agent_ids.add(parsed["front_matter"]["agent_id"])
            self.assertIn("response_json_schema", parsed, path.name)
            self.assertNotIn("output_schema", parsed, path.name)
            self.assertNotIn(
                "# Response JSON Schema",
                parsed["system_prompt"],
                path.name,
            )
            self.assertEqual(
                set(parsed["response_json_schema"]) & {"answer", "core_claims"},
                {"answer", "core_claims"},
                path.name,
            )

        self.assertEqual(
            agent_ids,
            {
                "L0_main",
                "L0_analysis",
                "L1_composition_alignment",
                "L1_query_delegation",
                "L0_orchestrator",
                "L1_query",
                "L2_comp_eval",
                "L2_meas_eval",
                "L2_prop_eval",
                "L2_ref_eval",
            },
        )


if __name__ == "__main__":
    unittest.main()
