# Alignment workflow

[L0_orchestrator/orchestrator.py](L0_orchestrator/orchestrator.py) drives the
alignment agent through the shared ReAct engine. It loads
[L0_orchestrator_workflow.md](L0_orchestrator/L0_orchestrator_workflow.md), which is
a runtime prompt specification with YAML frontmatter and exactly one
`<system_prompt>` block.

The orchestrator builds the explicit tool registry, adds tool instructions,
applies the alignment engine configuration, and submits the search text to
Argo. Settings provide an entry limit, a per-run time budget, and workflow hints
for Query-agent escalation and block filling. The public API supplies isolated
form state and returns its snapshot after the run.

The prompt guides parsing, canonical-ID resolution, field validation, block
filling, review, and finalization. These are model-guided steps, not a guaranteed
fixed call sequence. Use [the public API](../README.md) to choose this live
workflow or the deterministic alternative. Editing the workflow Markdown
changes model instructions and should be reviewed as a behavior change.
