# Browser templates

Jinja templates implement the pages documented in [the browser guide](../README.md).
Most full pages extend [base.html](base.html). The embedded specialized-tool view
uses [specialized_tools_embedded_base.html](specialized_tools_embedded_base.html);
underscore-prefixed files provide shared fragments/macros.

| Template | Purpose |
|---|---|
| [index.html](index.html) | Database overview |
| [search.html](search.html) | Structured and smart search, resolution chips, results |
| [papers.html](papers.html), [paper.html](paper.html) | Paper list and parsed measurement details |
| [compound.html](compound.html) | Compound and matching references |
| [agents.html](agents.html) | Agent settings, terminal/SSE output, reasoning, and completed results |
| [agent_history.html](agent_history.html) | Shared freeform and benchmark history, detail tabs, artifacts |
| [analysis.html](analysis.html) | Deterministic calculation workbench |
| [specialized_tools.html](specialized_tools.html) | Saved specialized-tool result tables, figures, and downloads |
| [_raw_json_panel.html](_raw_json_panel.html) | Lazy raw-JSON panel macro |
| [_agent_subnav.html](_agent_subnav.html) | Navigation shared by agent pages |

Raw JSON and detailed run panels are available without a username or debug flag.
There is no master-platform session, guest badge, or unload-triggered output
cleanup. The history parameter `scope=user` identifies the shared freeform
category, not an individual user.

## Frontend dependencies

The templates load external CDN libraries: Bootstrap and Bootstrap Icons;
Chart.js for analysis and paper charts; marked and DOMPurify for agent Markdown;
KaTeX for mathematics on the agent page; and Plotly for history and specialized
tool plots. See each template's script/link tags for the actual versions.
These assets are not bundled for fully offline operation.

Local JavaScript in [../static/](../static/) implements canonical-ID links,
result-panel toggles, composition-aware plots, workflow rendering, and
specialized-tool tables. Some page-specific scripts remain inline in templates.

For frontend changes, compile the Jinja templates and check JavaScript syntax
in rendered pages as well as static scripts. The local browser `tests/` suite
(excluded from the published snapshot) checks that detailed agent sections remain
visible without user state.
