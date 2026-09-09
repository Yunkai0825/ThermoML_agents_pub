# Workflow Skill Templates

Infrastructure for defining agents via structured markdown files,
parsing them into executable configurations, and running them with
optional parallel dispatch.

## Files

| File | Purpose |
|------|---------|
| `_subworkflow_parsing_schema.md` | Formal schema definition for workflow `.md` files |
| `subworkflow_md_parser.py` | `parse_workflow()` + `render_prompt()` |
| `subworkflow_md_tool_descriptions.py` | Generates tool-description XML from parsed workflow definitions |

## Workflow Markdown Format

Each agent layer is fully defined by a `.md` file:

```markdown
---
agent_id: L1_query
layer: 1
model: claudeopus46
---
# System Prompt
(agent instructions)

# Tools
## search_tools
- search_blocks(compounds, properties, ...)
## subagent_tools
- L2_comp_eval(purpose, instruction, context)

# Prompt Template
## Purpose
{{purpose}}
## Instruction
{{instruction}}

# Response JSON Schema
```json
{
  "answer": "Plain-text chemistry answer copied during assembly.",
  "core_claims": ["Claim distilled after the answer agent terminates."],
  "status": "success | partial | no_results"
}
```

The one `core_claims` element in this document is a type exemplar. The
post-answer core-claims agent may return one or several non-empty central
claims.

# Phases
## phase_1: resolve_ids
tools: [search_tools]
guidance: Start by resolving compound names to num_ids.
```

## Parser API

```python
from subworkflow_skill_templates.subworkflow_parser import parse_workflow, render_prompt

parsed = parse_workflow("path/to/workflow.md")
# Returns: {
#   "front_matter": {...},
#   "system_prompt": "...",  # Response JSON Schema removed
#   "tools": {"search_tools": [...], "subagent_tools": [...]},
#   "prompt_template": "...",
#   "response_json_schema": {...},  # post-answer workers only
#   "phases": [{"name": "resolve_ids", "tools": [...], "guidance": "...",
#               "parallel_dispatch": None | {...}}]
# }

prompt = render_prompt(parsed, purpose="...", instruction="...", context="...")
# Substitutes {{purpose}}, {{instruction}}, {{context}}, {{id_catalog}}
```

There is one schema path and no legacy alias. Parsing fails if
`# Response JSON Schema` is absent, duplicated, malformed, or cannot be
removed from the `<system_prompt>` block. The answer-agent runtime receives
only `parsed["system_prompt"]`; the parallel core claim/ID post-answer stage
receives `parsed["response_json_schema"]`.

## Async Runner (moved)

`fan_out()`, `run_phase()`, and `run_workflow()` have moved to
`general_argo_engine_helpers/async_runner.py`.

```python
from general_argo_engine_helpers.async_runner import fan_out

# Parallel dispatch with semaphore-based concurrency control
results = await fan_out(
    items=[block1, block2, block3],
    call_fn=evaluate_block,
    max_concurrent=8
)
```

`run_workflow(parsed, tool_executor, context=...)` executes all phases
sequentially, with parallel fan-out within phases that declare
`parallel_dispatch:` in their definition.
