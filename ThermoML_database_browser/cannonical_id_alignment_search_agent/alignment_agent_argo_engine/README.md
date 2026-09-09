# Alignment Argo client

[argo_client.py](argo_client.py) defines `AlignmentClient`, a subclass of the
research project's `ArgoClient`. `AlignmentClient.for_l0()` constructs a client
with the alignment config's model and maximum output tokens and assigns the
`L0-alignment` tier label.

The factory constructs a client; it does not itself attach a tool catalog or
run a workflow. [The orchestrator](../alignment_agent_workflows/L0_orchestrator/orchestrator.py)
loads the prompt, builds the tool registry, applies the engine config, and calls
the shared ReAct loop. Use [the public alignment API](../README.md) for complete
search-field alignment.
