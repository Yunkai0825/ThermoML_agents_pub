"""General post-answer evaluation hooks.

Public lifecycle:

``answer text → parallel claim + ID-alignment agents → deterministic JSON``.
"""

from .postanswer_evaluator import (
    PostAnswerEvaluationResult,
    assemble_return_json,
    build_core_claims_schema,
    build_id_alignment_schema,
    build_id_alignment_agent_schema,
    validate_response_json_schema,
    evaluate_and_assemble_return,
    extract_answer_text,
    prepare_answer_only_system_prompt,
)
from .summary_construction import (
    SUMMARY_SCHEMA,
    construct_answer_summary,
    SummaryConstructionToolCatalog,
    SUMMARY_CONSTRUCTION_TOOL_CATALOG,
)
from ._postans_eval_anchors_catalog import (
    POSTANS_ANSWER_RECEIVED,
    POSTANS_EVALUATION_BEFORE,
    POSTANS_PARALLEL_AGENTS_DISPATCH,
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
    POSTANS_EVAL_ANCHORS,
    POSTANS_EVAL_ANCHOR_TYPES,
)

__all__ = [
    "PostAnswerEvaluationResult",
    "assemble_return_json",
    "build_core_claims_schema",
    "build_id_alignment_schema",
    "build_id_alignment_agent_schema",
    "validate_response_json_schema",
    "evaluate_and_assemble_return",
    "extract_answer_text",
    "prepare_answer_only_system_prompt",
    "SUMMARY_SCHEMA",
    "construct_answer_summary",
    "SummaryConstructionToolCatalog",
    "SUMMARY_CONSTRUCTION_TOOL_CATALOG",
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
