"""Anchor catalog for the general post-answer evaluation lifecycle."""

from __future__ import annotations

from ...general_argo_engine_helpers.engine_hooks_anchors import define_anchor


POSTANS_ANSWER_RECEIVED = define_anchor(
    "postans_answer_received",
    "postans.answer.received",
)
POSTANS_EVALUATION_BEFORE = define_anchor(
    "postans_evaluation_before",
    "postans.evaluation.before",
)
# Semantic alias: this single anchor is the common launch point for both
# parallel post-answer agents. It is intentionally one anchor, not one
# branch-specific anchor per agent.
POSTANS_PARALLEL_AGENTS_DISPATCH = POSTANS_EVALUATION_BEFORE
POSTANS_EVALUATION_AFTER = define_anchor(
    "postans_evaluation_after",
    "postans.evaluation.after",
)
POSTANS_SUMMARY_TOOL_BEFORE = define_anchor(
    "postans_summary_tool_before",
    "postans.summary_tool.before",
)
POSTANS_SUMMARY_TOOL_AFTER = define_anchor(
    "postans_summary_tool_after",
    "postans.summary_tool.after",
)
POSTANS_L2_FIELD_TOOL_BEFORE = define_anchor(
    "postans_l2_field_tool_before",
    "postans.l2_field_tool.before",
)
POSTANS_L2_FIELD_TOOL_AFTER = define_anchor(
    "postans_l2_field_tool_after",
    "postans.l2_field_tool.after",
)
POSTANS_L2_FIELD_REFINEMENT = define_anchor(
    "postans_l2_field_refinement",
    "postans.l2_field.refinement",
)
POSTANS_CORE_ID_TOOLS_BEFORE = define_anchor(
    "postans_core_id_tools_before",
    "postans.core_id_tools.before",
)
POSTANS_CORE_ID_TOOLS_AFTER = define_anchor(
    "postans_core_id_tools_after",
    "postans.core_id_tools.after",
)
POSTANS_CORE_ID_REFINEMENT = define_anchor(
    "postans_core_id_refinement",
    "postans.core_id.refinement",
)
POSTANS_SUBMISSION_REVIEW = define_anchor(
    "postans_submission_review",
    "postans.submission.review",
)
POSTANS_ASSEMBLY_BEFORE = define_anchor(
    "postans_assembly_before",
    "postans.assembly.before",
)
POSTANS_ASSEMBLY_AFTER = define_anchor(
    "postans_assembly_after",
    "postans.assembly.after",
)
POSTANS_VALIDATION_FAILED = define_anchor(
    "postans_validation_failed",
    "postans.validation.failed",
)

POSTANS_EVAL_ANCHORS = (
    POSTANS_ANSWER_RECEIVED,
    POSTANS_EVALUATION_BEFORE,
    POSTANS_EVALUATION_AFTER,
    POSTANS_SUMMARY_TOOL_BEFORE,
    POSTANS_SUMMARY_TOOL_AFTER,
    POSTANS_L2_FIELD_TOOL_BEFORE,
    POSTANS_L2_FIELD_TOOL_AFTER,
    POSTANS_L2_FIELD_REFINEMENT,
    POSTANS_CORE_ID_TOOLS_BEFORE,
    POSTANS_CORE_ID_TOOLS_AFTER,
    POSTANS_CORE_ID_REFINEMENT,
    POSTANS_SUBMISSION_REVIEW,
    POSTANS_ASSEMBLY_BEFORE,
    POSTANS_ASSEMBLY_AFTER,
    POSTANS_VALIDATION_FAILED,
)
POSTANS_EVAL_ANCHOR_TYPES = frozenset(
    anchor.anchor_type for anchor in POSTANS_EVAL_ANCHORS
)

__all__ = [
    "POSTANS_ANSWER_RECEIVED",
    "POSTANS_EVALUATION_BEFORE",
    "POSTANS_PARALLEL_AGENTS_DISPATCH",
    "POSTANS_EVALUATION_AFTER",
    "POSTANS_SUMMARY_TOOL_BEFORE",
    "POSTANS_SUMMARY_TOOL_AFTER",
    "POSTANS_L2_FIELD_TOOL_BEFORE",
    "POSTANS_L2_FIELD_TOOL_AFTER",
    "POSTANS_L2_FIELD_REFINEMENT",
    "POSTANS_CORE_ID_TOOLS_BEFORE",
    "POSTANS_CORE_ID_TOOLS_AFTER",
    "POSTANS_CORE_ID_REFINEMENT",
    "POSTANS_SUBMISSION_REVIEW",
    "POSTANS_ASSEMBLY_BEFORE",
    "POSTANS_ASSEMBLY_AFTER",
    "POSTANS_VALIDATION_FAILED",
    "POSTANS_EVAL_ANCHORS",
    "POSTANS_EVAL_ANCHOR_TYPES",
]
