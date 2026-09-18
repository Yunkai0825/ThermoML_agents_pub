# Templates

Jinja2 HTML templates.  All extend `base.html` which provides the
Bootstrap 5 layout, nav bar, and common CSS/JS includes.

## Files

| Template | Route | Description |
|----------|-------|-------------|
| `base.html` | — | Base layout: nav bar, Bootstrap 5, Bootstrap Icons CDN |
| `index.html` | `/` | Landing page — DB stats (papers, compounds, properties) |
| `search.html` | `/search` | 5-panel ICSD-style advanced search with results table |
| `papers.html` | `/papers` | Paginated paper listing with title search |
| `paper.html` | `/paper/<doi>` | Paper detail — bibliography, compounds, parsed data blocks |
| `compound.html` | `/compound/<inchikey>` | Compound detail — all papers referencing the compound |
| `agents.html` | `/agents` | Agent runner — type selector, live progress, reasoning snapshots, past runs |
| `analysis.html` | `/analysis` | Analysis workbench — tool cards, per-tool settings, Chart.js plots |

## Front-end Libraries (CDN)

- Bootstrap 5.3 (CSS + JS bundle)
- Bootstrap Icons 1.11
- Chart.js 4.4 (analysis page only)
