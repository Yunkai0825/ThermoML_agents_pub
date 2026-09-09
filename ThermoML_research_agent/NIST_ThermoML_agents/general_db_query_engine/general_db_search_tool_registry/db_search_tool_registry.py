"""
DB Search Tool Registry — auto-discovered catalog of all card_db_search_tools.
===============================================================================
Scans the ``card_db_search_tools/`` tree at import time to build a structured
registry of canonical agent-facing search functions and their compactors.

Source of truth
---------------
- **Search functions** — discovered by scanning ``.py`` files in
  ``basic_search_tools/`` and ``block_centric_search_tools/`` for canonical
  public definitions. Implementation adapters named ``*_tool`` are excluded;
  runtime catalogs expose them under their canonical unsuffixed aliases.
- **Compactors** — discovered from ``COMPACTOR_FUNCTIONS`` in
  ``_tools_results_compactors/__init__.py`` by reading each function's
  ``_compacts_tools`` attribute (set by the ``@compacts(...)`` decorator).

Calling ``generate_report_md()`` produces a markdown document summarising
the full tool→compactor mapping.

Usage::

    from general_db_search_tool_registry import (
        SEARCH_TOOL_REGISTRY,   # dict[str, SearchToolEntry]
        COMPACTOR_MODULE_MAP,   # dict[str, str]
        CATEGORIES,
        list_tools_with_compactors,
        list_tools_without_compactors,
        tools_by_category,
        generate_report_md,
    )
"""

from __future__ import annotations

import ast
import inspect
import logging
import re
import sys
import textwrap
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Dict, List, Optional

log = logging.getLogger("db-search-tool-registry")

# ── Locate card_db_search_tools/ root ──────────────────────────
_HERE = Path(__file__).resolve().parent
_ENGINE_ROOT = _HERE.parent        # general_db_query_engine/
_AGENTS_ROOT = _ENGINE_ROOT.parent  # NIST_ThermoML_agents/
# card_db_search_tools/ lives in the workspace root (ThermoML_research_agent/),
# one level above NIST_ThermoML_agents/.
_SEARCH_ROOT = _AGENTS_ROOT.parent / "card_db_search_tools"

# Sub-directories that contain tool modules
_BASIC_DIR = _SEARCH_ROOT / "basic_search_tools"
_BLOCK_DIR = _SEARCH_ROOT / "block_centric_search_tools"
_COMPACTOR_ROOT = _SEARCH_ROOT / "_tools_results_compactors"


# ═══════════════════════════════════════════════════════════════
#  Dataclass
# ═══════════════════════════════════════════════════════════════

@dataclass(frozen=True)
class SearchToolEntry:
    """Describes one public search function in card_db_search_tools."""

    tool_name: str
    """Canonical name used in agent tool dicts and compactor registries."""

    category: str
    """One of: id_resolution, basic_search, advanced_search, block_centric,
    data_extraction.
    """

    module_file: str
    """Filename (relative to card_db_search_tools/) that defines the function."""

    description: str
    """First line of the docstring (auto-extracted)."""

    compactor_fn_name: Optional[str] = None
    """Name of the ``compact_*`` function (None = no compactor)."""

    compactor_module_file: Optional[str] = None
    """Compactor's module path relative to _tools_results_compactors/."""


# ═══════════════════════════════════════════════════════════════
#  Static AST scanner — extract public function signatures
# ═══════════════════════════════════════════════════════════════

_CATEGORY_MAP = {
    "_id_alignment_search.py": "id_resolution",
    "1_block_search.py":       "basic_search",
    "2_system_registry_search.py": "basic_search",
    "3_compound_DK_search.py": "basic_search",
    "4_reference_search.py":   "basic_search",
    "5_meas_DK_search.py":     "basic_search",
    "6_meas_INDIV_search.py":  "basic_search",
    "7_prop_DK_search.py":     "basic_search",
    "8_compound_INDIV_search.py": "basic_search",
    "9_system_summary_search.py": "basic_search",
    "10_compound_similarity_search.py": "basic_search",
    "11_block_data_extractor.py": "data_extraction",
    "12_block_search_adv.py": "advanced_search",
    "13_block_rdp_inspection.py": "data_extraction",
}


def _scan_module_for_public_fns(filepath: Path) -> List[dict]:
    """Parse *filepath* with AST and return info on each public function.

    Returns a list of dicts with keys: name, docstring.
    """
    try:
        source = filepath.read_text(encoding="utf-8")
    except OSError:
        return []
    try:
        tree = ast.parse(source, filename=str(filepath))
    except SyntaxError:
        return []

    results = []
    for node in ast.iter_child_nodes(tree):
        if not isinstance(node, ast.FunctionDef):
            continue
        if node.name.startswith("_") or node.name.endswith("_tool"):
            continue
        doc = ast.get_docstring(node) or ""
        first_line = doc.split("\n")[0].strip() if doc else ""
        results.append({"name": node.name, "docstring": first_line})
    return results


def _scan_directory(directory: Path, prefix: str, default_category: str) -> List[dict]:
    """Scan a directory for .py tool modules and extract public functions.

    Returns list of dicts: name, docstring, module_file, category.
    """
    if not directory.is_dir():
        return []
    results = []
    for py_file in sorted(directory.glob("*.py")):
        if py_file.name.startswith("__") or py_file.name == "test_all_search_tools.py":
            continue
        cat = _CATEGORY_MAP.get(py_file.name, default_category)
        rel = f"{prefix}/{py_file.name}"
        for fn_info in _scan_module_for_public_fns(py_file):
            results.append({
                "name": fn_info["name"],
                "docstring": fn_info["docstring"],
                "module_file": rel,
                "category": cat,
            })
    return results


# ═══════════════════════════════════════════════════════════════
#  Compactor discovery — read _compacts_tools from tagged functions
# ═══════════════════════════════════════════════════════════════

def _discover_compactors() -> Dict[str, dict]:
    """Import COMPACTOR_FUNCTIONS and build {tool_name: info} from tags.

    Returns dict: tool_name → {fn_name, module_file, fn}.
    """
    # Ensure search tool paths are on sys.path so the import works
    for p in (_BASIC_DIR, _BLOCK_DIR, _SEARCH_ROOT, _COMPACTOR_ROOT):
        ps = str(p)
        if ps not in sys.path:
            sys.path.insert(0, ps)

    compactor_map: Dict[str, dict] = {}
    from _tools_results_compactors import COMPACTOR_FUNCTIONS

    for fn in COMPACTOR_FUNCTIONS:
        tool_names = getattr(fn, "_compacts_tools", ())
        # Resolve the module file relative to _tools_results_compactors/
        try:
            mod = inspect.getmodule(fn)
            if mod and hasattr(mod, "__file__") and mod.__file__:
                mod_path = Path(mod.__file__).resolve()
                try:
                    rel = mod_path.relative_to(_COMPACTOR_ROOT)
                    module_file = str(rel).replace("\\", "/")
                except ValueError:
                    module_file = mod_path.name
            else:
                module_file = "?"
        except Exception:
            module_file = "?"

        for tool_name in tool_names:
            compactor_map[tool_name] = {
                "fn_name": fn.__name__,
                "module_file": module_file,
                "fn": fn,
            }
    return compactor_map


# ═══════════════════════════════════════════════════════════════
#  Build the registry
# ═══════════════════════════════════════════════════════════════

def _build_registry() -> List[SearchToolEntry]:
    """Scan tool modules + compactors and return a list of SearchToolEntry."""
    # 1. Discover compactors
    compactor_map = _discover_compactors()

    # 2. Scan search-tool directories
    raw_tools: List[dict] = []
    raw_tools.extend(_scan_directory(_BASIC_DIR, "basic_search_tools", "basic_search"))
    raw_tools.extend(_scan_directory(_BLOCK_DIR, "block_centric_search_tools", "block_centric"))

    # 3. Build entries
    entries: List[SearchToolEntry] = []
    for t in raw_tools:
        c = compactor_map.get(t["name"])
        entries.append(SearchToolEntry(
            tool_name=t["name"],
            category=t["category"],
            module_file=t["module_file"],
            description=t["docstring"],
            compactor_fn_name=c["fn_name"] if c else None,
            compactor_module_file=c["module_file"] if c else None,
        ))
    return entries


_ALL_ENTRIES = _build_registry()


# ═══════════════════════════════════════════════════════════════
#  Derived look-ups
# ═══════════════════════════════════════════════════════════════

SEARCH_TOOL_REGISTRY: Dict[str, SearchToolEntry] = {
    e.tool_name: e for e in _ALL_ENTRIES
}
"""Canonical registry: tool_name → SearchToolEntry."""

COMPACTOR_MODULE_MAP: Dict[str, str] = {
    e.tool_name: e.compactor_module_file
    for e in _ALL_ENTRIES
    if e.compactor_module_file is not None
}
"""Subset: tool_name → compactor module file (only tools that have one)."""

CATEGORIES = sorted({e.category for e in _ALL_ENTRIES})
"""All distinct category labels."""


def list_tools_with_compactors() -> List[str]:
    """Tool names that have a registered hardcoded compactor."""
    return [e.tool_name for e in _ALL_ENTRIES if e.compactor_fn_name is not None]


def list_tools_without_compactors() -> List[str]:
    """Tool names that violate the required search-tool compactor contract."""
    return [e.tool_name for e in _ALL_ENTRIES if e.compactor_fn_name is None]


def tools_by_category(category: str) -> List[SearchToolEntry]:
    """All entries belonging to *category*."""
    return [e for e in _ALL_ENTRIES if e.category == category]


# ═══════════════════════════════════════════════════════════════
#  Markdown report generator
# ═══════════════════════════════════════════════════════════════

def generate_report_md() -> str:
    """Generate a markdown report of all DB search tools and compactors.

    The report includes:
    - Summary statistics
    - Per-category tables of tools with compactor coverage
    - Orphan compactors (tags that don't match any scanned tool)
    """
    lines: List[str] = []
    w = lines.append

    n_total = len(_ALL_ENTRIES)
    n_with = len(list_tools_with_compactors())
    n_without = len(list_tools_without_compactors())

    w("# DB Search Tool & Compactor Registry")
    w("")
    w(f"*Auto-generated by `db_search_tool_registry.py`*")
    w("")
    w("## Summary")
    w("")
    w(f"| Metric | Count |")
    w(f"|--------|-------|")
    w(f"| Total search tools | {n_total} |")
    w(f"| With compactor | {n_with} |")
    w(f"| Without compactor | {n_without} |")
    w(f"| Categories | {len(CATEGORIES)} |")
    w("")

    # ── Per-category tables ─────────────────────────────────
    for cat in CATEGORIES:
        cat_tools = tools_by_category(cat)
        w(f"## {cat.replace('_', ' ').title()}  ({len(cat_tools)} tools)")
        w("")
        w("| Tool | Module | Compactor | Compactor Module |")
        w("|------|--------|-----------|------------------|")
        for e in cat_tools:
            comp_name = e.compactor_fn_name or "—"
            comp_mod = e.compactor_module_file or "—"
            w(f"| `{e.tool_name}` | `{e.module_file}` | `{comp_name}` | `{comp_mod}` |")
        w("")

    # ── Tools without compactors ────────────────────────────
    no_comp = list_tools_without_compactors()
    if no_comp:
        w("## Tools Without Compactors")
        w("")
        w("These tools either return markdown/text directly or have no "
          "hardcoded dict→md formatter yet:")
        w("")
        for name in no_comp:
            e = SEARCH_TOOL_REGISTRY[name]
            w(f"- `{name}` — {e.description or '(no description)'}")
        w("")

    # ── Orphan compactors ───────────────────────────────────
    compactor_map = _discover_compactors()
    orphans = [tn for tn in compactor_map if tn not in SEARCH_TOOL_REGISTRY]
    if orphans:
        w("## Orphan Compactors")
        w("")
        w("Compactors tagged via `@compacts(...)` for tool names that "
          "were not found in any scanned module:")
        w("")
        for tn in sorted(orphans):
            info = compactor_map[tn]
            w(f"- `{tn}` → `{info['fn_name']}` in `{info['module_file']}`")
        w("")

    return "\n".join(lines)
