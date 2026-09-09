"""Focused tests for field-isolated Query L2 construction tools."""

from __future__ import annotations

import json
import unittest

from .l2_field_construction import (
    L2_COMPOUND_CONSTRUCTION_TOOLS,
    L2_MEASUREMENT_CONSTRUCTION_TOOLS,
    L2_PROPERTY_CONSTRUCTION_TOOLS,
    L2_REFERENCE_CONSTRUCTION_TOOLS,
    L2FieldValidationError,
    construct_l2_compounds,
    construct_l2_measurements,
    construct_l2_properties,
    construct_l2_reference,
    refine_and_enrich_l2_compounds,
)
from ..strict_output_contracts import validate_l2_output


_COMP_CORE = {
    "lit_num_id": "GLOBlit_1",
    "block_number": "PROPblock_1",
    "BLKsubsys_id": None,
    "description": "Carbon dioxide sample in the selected block.",
    "comp_num_id": "GLOBcomp_3",
    "org_num": "DOIcomp_2",
}
_MEAS_CORE = {
    "lit_num_id": "GLOBlit_1",
    "block_number": "PROPblock_1",
    "BLKsubsys_id": None,
    "description": "Hot-wire measurement for the selected block property.",
    "meas_num_id": "GLOBmeas_41",
    "BLKprop_id": "BLKprop_1",
}
_PROP_CORE = {
    "lit_num_id": "GLOBlit_1",
    "block_number": "PROPblock_1",
    "BLKsubsys_id": None,
    "description": "Thermal conductivity reported by the selected property.",
    "BLKprop_id": "BLKprop_1",
    "prop_num_id": "GLOBprop_34",
}
_REF_CORE = {
    "lit_num_id": "GLOBlit_1",
    "block_number": "PROPblock_1",
    "BLKsubsys_id": None,
    "description": "Literature source for the selected block.",
    "lit_id": "2005-pat-klo-0",
}


class _CorrectionClient:
    def __init__(self, response: dict) -> None:
        self.response = response
        self.calls: list[dict] = []

    def call(self, prompt: str, system: str, *, max_tokens: int) -> str:
        self.calls.append(
            {"prompt": prompt, "system": system, "max_tokens": max_tokens}
        )
        return json.dumps(self.response)


class L2FieldConstructionTests(unittest.TestCase):
    def test_each_l2_catalog_exposes_only_its_designated_tool(self) -> None:
        expected = (
            (L2_COMPOUND_CONSTRUCTION_TOOLS, {"construct_l2_compounds"}),
            (
                L2_MEASUREMENT_CONSTRUCTION_TOOLS,
                {"construct_l2_measurements"},
            ),
            (L2_PROPERTY_CONSTRUCTION_TOOLS, {"construct_l2_properties"}),
            (L2_REFERENCE_CONSTRUCTION_TOOLS, {"construct_l2_reference"}),
        )
        for catalog, tool_names in expected:
            self.assertEqual(set(catalog.tools), tool_names)
            self.assertEqual(set(catalog.entries), tool_names)
            entry = next(iter(catalog.entries.values()))
            self.assertTrue(entry.skip_compactor)
            self.assertTrue(entry.skip_subagent)

    def test_all_four_tools_construct_authoritative_context(self) -> None:
        compound = construct_l2_compounds([dict(_COMP_CORE)])["compounds"][0]
        self.assertEqual(compound["registry_id"], "carbon_dioxide")
        self.assertEqual(compound["purity"], 99.98)
        self.assertEqual(compound["source"], "Commercial source")

        measurement = construct_l2_measurements([dict(_MEAS_CORE)])[
            "measurements"
        ][0]
        self.assertEqual(measurement["prop_num_id"], "GLOBprop_34")
        self.assertEqual(measurement["registry_id"], "hot_wire_method")
        self.assertEqual(measurement["uncertainty_coverage"], 0.95)
        self.assertIn("platinum wire", measurement["instrument"])

        prop = construct_l2_properties([dict(_PROP_CORE)])["properties"][0]
        self.assertEqual(prop["registry_id"], "thermal_conductivity_w_m_k")
        self.assertEqual(prop["phase"], "gas")
        self.assertIn("W/m/K", prop["definition"])

        reference = construct_l2_reference(dict(_REF_CORE))["reference"]
        self.assertEqual(reference["doi"], "10.1007/s10765-005-5566-6")
        self.assertEqual(reference["n_blocks"], 2)
        self.assertIn("carbon dioxide", reference["compounds_measured"])

    def test_real_subsystem_constructors_validate_retained_chemistry(self) -> None:
        target = {
            "lit_num_id": "GLOBlit_608",
            "block_number": "PROPblock_1",
            "BLKsubsys_id": "BLKsubsys_2",
        }
        compound = construct_l2_compounds([{
            **target,
            "description": "Alanine retained in the binary aqueous face.",
            "comp_num_id": "GLOBcomp_74",
            "org_num": "DOIcomp_1",
        }])["compounds"][0]
        self.assertEqual(compound["registry_id"], "(s)-2-aminopropanoic_acid")
        self.assertEqual(compound["BLKsubsys_id"], "BLKsubsys_2")

        prop = construct_l2_properties([{
            **target,
            "description": "Speed of sound on the selected binary face.",
            "BLKprop_id": "BLKprop_1",
            "prop_num_id": "GLOBprop_8",
        }])["properties"][0]
        self.assertEqual(prop["registry_id"], "speed_of_sound_m_s")

        measurement = construct_l2_measurements([{
            **target,
            "description": "Sing-around measurement for this property.",
            "meas_num_id": "GLOBmeas_7",
            "BLKprop_id": "BLKprop_1",
        }])["measurements"][0]
        self.assertEqual(
            measurement["registry_id"],
            "sing_around_technique_in_a_fixed_path_interferometer",
        )

        reference = construct_l2_reference({
            **target,
            "description": "Source paper for the selected binary face.",
            "lit_id": "2008-sad-goo-1",
        })["reference"]
        self.assertEqual(reference["doi"], "10.1016/j.fluid.2008.02.015")

        with self.assertRaises(L2FieldValidationError):
            construct_l2_compounds([{
                **target,
                "description": "Excluded salt must not enter this face.",
                "comp_num_id": "GLOBcomp_2004",
                "org_num": "DOIcomp_2",
            }])

    def test_validation_ids_are_checksums_not_agent_owned_content(self) -> None:
        wrong = dict(_COMP_CORE)
        wrong["comp_num_id"] = "GLOBcomp_1"
        with self.assertRaisesRegex(
            L2FieldValidationError,
            "checksum|resolved",
        ):
            construct_l2_compounds([wrong])

    def test_l2_correction_loop_preserves_tool_generated_summary(self) -> None:
        wrong = dict(_COMP_CORE)
        wrong["comp_num_id"] = "GLOBcomp_1"
        correction = {"status": "success", "compounds": [dict(_COMP_CORE)]}
        client = _CorrectionClient(correction)
        schema = {
            "status": "success | partial | no_results",
            "compounds": [dict(_COMP_CORE)],
            "summary": "Answer-only summary.",
        }
        result = refine_and_enrich_l2_compounds(
            id_alignment={
                "status": "success",
                "compounds": [wrong],
                "summary": "Summary made by the hidden summary tool.",
            },
            client=client,
            id_alignment_schema=schema,
            id_alignment_prompt="base ID alignment prompt",
            answer="The selected block contains carbon dioxide.",
            core_claims_evaluation={"core_claims": ["Carbon dioxide is used."]},
            completed_run_record="[]",
            label="test-L2-comp",
            max_tokens=2000,
        )
        self.assertEqual(
            result["summary"],
            "Summary made by the hidden summary tool.",
        )
        self.assertEqual(result["compounds"][0]["comp_num_id"], "GLOBcomp_3")
        self.assertEqual(len(client.calls), 1)
        self.assertNotIn(
            '"summary"',
            client.calls[0]["prompt"].split(
                "## Current minimal field selection", 1
            )[1],
        )
        self.assertIn("Do not emit answer, core_claims, or summary", client.calls[0]["system"])

    def test_strict_validators_reconstruct_every_l2_tool_output(self) -> None:
        base = {
            "answer": "Supported chemistry assessment.",
            "core_claims": ["One supported central claim."],
            "status": "success",
            "summary": "Concise supported summary.",
        }
        outputs = {
            "comp": construct_l2_compounds([dict(_COMP_CORE)]),
            "meas": construct_l2_measurements([dict(_MEAS_CORE)]),
            "prop": construct_l2_properties([dict(_PROP_CORE)]),
            "ref": construct_l2_reference(dict(_REF_CORE)),
        }
        for kind, fields in outputs.items():
            payload = {**base, **fields}
            self.assertIs(validate_l2_output(kind, payload), payload)

        tampered = {**base, **outputs["prop"]}
        tampered["properties"][0]["definition"] = "agent-authored replacement"
        with self.assertRaisesRegex(ValueError, "authoritative output"):
            validate_l2_output("prop", tampered)


if __name__ == "__main__":
    unittest.main()
