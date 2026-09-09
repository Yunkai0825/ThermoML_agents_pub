"""Live-DB contract tests for 13_block_rdp_inspection.inspect_block_table.

Anchored on GLOBlit_8821 (10.1021/je050519g) PROPblock_13 — the Case II
fabrication forensics block whose 7 true rows are the canonical regression
target — plus one large 2-variable block for RDP mode.
"""

from __future__ import annotations

import importlib

import pytest

_mod = importlib.import_module("13_block_rdp_inspection")
inspect_block_table = _mod.inspect_block_table

_extractor = importlib.import_module("11_block_data_extractor")
extract_block_csv = _extractor.extract_block_csv

from _tools_results_compactors.basic_search_tools.compactors import (  # noqa: E402
    compact_inspect_block_table,
)

CASE2 = "GLOBlit_8821::PROPblock_13"
CASE2_DOI = "10.1021/je050519g"
X_ALIAS = "mole_fraction_acetonitrile"
Y_ALIAS = "surface_tension_liquidgas_n_m"
CASE2_TRUTH = [
    ("0.1001", "0.0238"),
    ("0.2011", "0.02473"),
    ("0.2996", "0.02553"),
    ("0.4997", "0.02685"),
    ("0.7012", "0.02794"),
    ("0.8009", "0.02842"),
    ("0.8956", "0.02885"),
]
BIG_DOI = "10.1007/s10765-005-5566-6"
BIG_BLOCK = "PROPblock_1"  # 77 rows, T + p axes


def _cells(result, alias):
    column = {v: k for k, v in result["column_aliases"].items()}
    col = next(c for c, a in column.items() if a == alias)
    return [row[col] for row in result["rows_shown"]]


class TestCompleteMode:
    def test_case2_rows_verbatim(self):
        res = inspect_block_table(CASE2)
        assert res["error"] is None
        assert res["table_mode"] == "complete"
        assert res["n_rows_shown"] == res["n_rows_matched"] == 7
        pairs = list(zip(_cells(res, X_ALIAS), _cells(res, Y_ALIAS)))
        assert pairs == CASE2_TRUTH

    def test_markdown_contains_verbatim_values_and_rule(self):
        res = inspect_block_table(CASE2)
        for x, y in CASE2_TRUTH:
            assert f"| {x} |" in res["markdown"]
            assert f" {y} |" in res["markdown"]
        assert "quoted ONLY verbatim" in res["markdown"]
        assert res["inspection_id"].startswith("INSP_")

    def test_stats_are_verbatim_extremes(self):
        res = inspect_block_table(CASE2)
        stats = res["stats"]["matched"][Y_ALIAS]
        assert (stats["min"], stats["max"]) == ("0.0238", "0.02885")
        assert stats["n_finite"] == 7

    def test_deterministic_inspection_id(self):
        first = inspect_block_table(CASE2)
        second = inspect_block_table(CASE2)
        assert first["inspection_id"] == second["inspection_id"]

    def test_bare_block_with_doi_literature(self):
        res = inspect_block_table("PROPblock_13", literature=CASE2_DOI)
        assert res["error"] is None
        assert res["n_rows_shown"] == 7


class TestNearestAndBracket:
    def test_no_exact_row_at_half(self):
        res = inspect_block_table(
            CASE2, nearest={"column": X_ALIAS, "value": 0.5},
        )
        assert res["table_mode"] == "nearest"
        assert _cells(res, X_ALIAS) == ["0.4997"]
        bracket = res["bracket"]
        assert bracket["exact_match"] is False
        assert bracket["below"]["value"] == "0.4997"
        assert bracket["above"]["value"] == "0.7012"
        assert "0 matched rows strictly inside" in bracket["statement"]

    def test_exact_hit(self):
        res = inspect_block_table(
            CASE2, nearest={"column": X_ALIAS, "value": 0.4997},
        )
        assert res["bracket"]["exact_match"] is True

    def test_outside_range(self):
        res = inspect_block_table(
            CASE2, nearest={"column": X_ALIAS, "value": 0.05},
        )
        assert "outside the matched range" in res["bracket"]["statement"]

    def test_k_two_sorted_ascending(self):
        res = inspect_block_table(
            CASE2, nearest={"column": X_ALIAS, "value": 0.5, "k": 2},
        )
        assert _cells(res, X_ALIAS) == ["0.2996", "0.4997"]

    @pytest.mark.parametrize("bad", [
        {"column": X_ALIAS},
        {"column": X_ALIAS, "value": 0.5, "k": 0},
        {"column": X_ALIAS, "value": 0.5, "k": 9},
        {"column": X_ALIAS, "value": True},
        {"column": X_ALIAS, "value": 0.5, "extra": 1},
    ])
    def test_invalid_nearest_returns_error(self, bad):
        res = inspect_block_table(CASE2, nearest=bad)
        assert res["error"]
        assert res["rows_shown"] == []


class TestWhereFilter:
    def test_between_subset_and_full_stats(self):
        res = inspect_block_table(
            CASE2, where=f"{X_ALIAS} BETWEEN 0.2 AND 0.8",
        )
        assert res["n_rows_matched"] == 4
        assert _cells(res, X_ALIAS) == ["0.2011", "0.2996", "0.4997", "0.7012"]
        assert res["stats"]["full"][X_ALIAS]["max"] == "0.8956"

    def test_equality_and_in_agree(self):
        eq = inspect_block_table(CASE2, where=f"{X_ALIAS} = 0.4997")
        isin = inspect_block_table(CASE2, where=f"{X_ALIAS} IN (0.4997)")
        assert _cells(eq, X_ALIAS) == _cells(isin, X_ALIAS) == ["0.4997"]

    def test_compact_operators_lex(self):
        res = inspect_block_table(CASE2, where=f"{X_ALIAS}<0.3")
        assert res["n_rows_matched"] == 3

    def test_and_conjunction(self):
        res = inspect_block_table(
            CASE2,
            where=f"{X_ALIAS} > 0.2 AND {Y_ALIAS} <= 0.02685",
        )
        assert _cells(res, X_ALIAS) == ["0.2011", "0.2996", "0.4997"]

    def test_no_match_reports_ranges(self):
        res = inspect_block_table(CASE2, where=f"{X_ALIAS} > 0.99")
        assert res["error"]
        assert any(c["alias"] == X_ALIAS for c in res["columns_help"])

    @pytest.mark.parametrize("bad", [
        "bogus_col > 1",
        f"{X_ALIAS} > 0.1 OR {X_ALIAS} < 0.9",
        f"{X_ALIAS} BETWEEN 0.1",
        f"{X_ALIAS} > 0.1 AND",
        f"{X_ALIAS} IN (0.1,",
    ])
    def test_where_errors_are_results_with_help(self, bad):
        res = inspect_block_table(CASE2, where=bad)
        assert res["error"]
        assert res["columns_help"]
        assert "alias" in res["markdown"]


class TestRdpMode:
    def test_large_block_rdp_subset_is_verbatim(self):
        res = inspect_block_table(BIG_BLOCK, literature=BIG_DOI)
        assert res["table_mode"] == "rdp"
        assert res["n_rows_matched"] == 77
        assert 12 < res["n_rows_shown"] < 77
        raw = extract_block_csv(BIG_DOI, BIG_BLOCK)
        raw_rows = {line for line in raw["csv_text"].splitlines()}
        for row in res["rows_shown"]:
            line = ",".join(row[c] for c in res["columns"])
            assert line in raw_rows
        assert "narrow `where`" in res["markdown"]

    def test_endpoints_kept(self):
        res = inspect_block_table(BIG_BLOCK, literature=BIG_DOI)
        ids = [row["BLKpoint_id"] for row in res["rows_shown"]]
        assert ids[0] == "BLKpoint_1"
        assert ids[-1] == "BLKpoint_77"

    def test_isotherm_slice_goes_complete(self):
        res = inspect_block_table(
            BIG_BLOCK, literature=BIG_DOI,
            where="temperature_k BETWEEN 298 AND 301",
        )
        assert res["table_mode"] == "complete"
        assert res["n_rows_matched"] <= 12


class TestAddressingContracts:
    def test_bare_block_without_literature_is_refinement(self):
        res = inspect_block_table("PROPblock_13")
        assert res.get("error_code") == "ID_REFINEMENT_REQUIRED"

    def test_double_literature_scope_is_refinement(self):
        res = inspect_block_table(CASE2, literature=CASE2_DOI)
        assert res.get("error_code") == "ID_REFINEMENT_REQUIRED"

    def test_unknown_literature_is_error_result(self):
        res = inspect_block_table("PROPblock_1", literature="10.9999/nope")
        assert res["error"]

    def test_unknown_block_reports_available(self):
        res = inspect_block_table("PROPblock_99", literature=CASE2_DOI)
        assert res["error"]
        assert "Available" in res["error"]


class TestCompactorContract:
    def test_passthrough_markdown(self):
        res = inspect_block_table(CASE2)
        assert compact_inspect_block_table(res) == res["markdown"]

    def test_error_result_passthrough(self):
        res = inspect_block_table(CASE2, where="bogus > 1")
        assert compact_inspect_block_table(res).startswith(
            "**inspect_block_table error**"
        )

    def test_missing_markdown_rejected(self):
        with pytest.raises(ValueError):
            compact_inspect_block_table({"error": None, "rows_shown": []})
