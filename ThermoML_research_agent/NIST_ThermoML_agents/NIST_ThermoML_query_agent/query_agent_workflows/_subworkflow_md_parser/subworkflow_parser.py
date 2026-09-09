"""
Workflow-skill markdown parser — query agent thin wrapper.
==========================================================
Delegates to the shared ``subagent_skill_schema_and_parser`` module.
All existing ``from ..subworkflow_skill_templates.subworkflow_parser import ...``
statements continue to work unchanged.

Public API (re-exported)
----------
parse_workflow   — parse a workflow markdown file
render_prompt    — substitute template variables
"""

from ....general_db_query_engine.general_subagent_skill_schema_and_parser import parse_workflow, render_prompt  # noqa: F401

__all__ = ["parse_workflow", "render_prompt"]
