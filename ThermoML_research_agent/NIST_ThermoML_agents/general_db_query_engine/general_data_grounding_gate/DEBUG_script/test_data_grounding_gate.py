"""Unit tests for the mandatory data-grounding gate (no DB, no LLM)."""

from __future__ import annotations

import json
import unittest

from NIST_ThermoML_agents.general_db_query_engine.general_data_grounding_gate import (
    FLAGS_HEADER,
    GATE_MARKER,
    build_evidence_log,
    build_flags_note,
    build_gate_nudge,
    build_grounded_context,
    build_timeout_gate_instruction,
    count_gate_bounces,
    export_inspections,
    gate_enabled,
    harvest_fit_artifacts,
    harvest_inspection_targets,
    harvest_inspections,
    parse_inspection_markdown,
    run_data_grounding_gate,
    write_grounding_evidence,
)


def _no_auth(lit, block):
    return None


def gate(answer, history, fetch=_no_auth, **kw):
    """Hermetic gate call — authoritative fetch stubbed unless injected."""
    return run_data_grounding_gate(
        answer, history, authoritative_fetch=fetch, **kw,
    )


def _fake_fetch(table_map):
    """Authoritative-fetch stub serving pre-built tables keyed by block."""
    def fetch(lit, block):
        return table_map.get(block)
    return fetch


def _envelope_history(block, doi, lit, values, inspection_id):
    """One tool-history item carrying a structured child inspection."""
    item = {
        "doi": doi,
        "lit_num_id": lit,
        "block_number": block,
        "columns": ["BLKpoint_id", "x"],
        "rows_shown": [
            {"BLKpoint_id": f"BLKpoint_{i + 1}", "x": str(v)}
            for i, v in enumerate(values)
        ],
        "inspection_id": inspection_id,
    }
    return {"tool": "L1_query",
            "result_full": json.dumps({"data_inspections": [item]})}

# Faithful copy of the tool's renderer output for the Case II truth block.
CASE2_MD = """**Data inspection** — 10.1021/je050519g :: PROPblock_13 (binary: methanol + acetonitrile)
filter: none (whole block)
block constraints: temperature_k = 293.15

| BLKpoint_id | mole_fraction_<acetonitrile> | temperature_k | surface_tension_liquidgas_n_m |
|---|---|---|---|
| BLKpoint_1 | 0.1001 | 293.15 | 0.0238 |
| BLKpoint_2 | 0.2011 | 293.15 | 0.02473 |
| BLKpoint_3 | 0.2996 | 293.15 | 0.02553 |
| BLKpoint_4 | 0.4997 | 293.15 | 0.02685 |
| BLKpoint_5 | 0.7012 | 293.15 | 0.02794 |
| BLKpoint_6 | 0.8009 | 293.15 | 0.02842 |
| BLKpoint_7 | 0.8956 | 293.15 | 0.02885 |

mode: complete — all 7 matched rows shown (block has 7)
topology: surface_tension_liquidgas_n_m vs mole_fraction_acetonitrile: monotonic↑
stats (matched, n=7): mole_fraction_acetonitrile 0.1001–0.8956 (n=7); temperature_k 293.15–293.15 (n=7); surface_tension_liquidgas_n_m 0.0238–0.02885 (n=7)
inspection_id: INSP_ace1f89aece6
Data points may be quoted ONLY verbatim from the table above or the stats lines.
"""

HISTORY = [{"iteration": 3, "tool": "inspect_block_table",
            "arguments": {}, "result_full": CASE2_MD}]

GROUNDED_ANSWER = (
    "For GLOBlit_8821::PROPblock_13 the surface tension rises monotonically "
    "from 0.0238 N/m at x(ACN)=0.1001 to 0.02885 N/m at x=0.8956 (293.15 K). "
    "Near x=0.5 the measured value is 0.02685 N/m (x=0.4997). "
    "Expressed in mN/m that is 26.85."
)

# The historical Case II fabrication: smooth invented interior grid.
FABRICATED_ANSWER = (
    "For GLOBlit_8821::PROPblock_13 at 293.15 K: x=0.1001 → 0.0238, "
    "x=0.2000 → 0.02446, x=0.3000 → 0.02522, x=0.5000 → 0.02640, "
    "x=0.7000 → 0.02762 N/m."
)

UNINSPECTED_ANSWER = (
    "GLOBlit_4242::PROPblock_2 reports viscosity 14.23 mPa·s at 303.15 K "
    "and 10.90 mPa·s at 313.15 K."
)


class HarvestTests(unittest.TestCase):
    def test_markdown_round_trip(self):
        entry = parse_inspection_markdown(CASE2_MD)
        self.assertIsNotNone(entry)
        self.assertEqual(entry["doi"], "10.1021/je050519g")
        self.assertEqual(entry["block_number"], "PROPblock_13")
        self.assertEqual(entry["table_mode"], "complete")
        self.assertEqual(len(entry["rows_shown"]), 7)
        self.assertEqual(entry["rows_shown"][3]["surface_tension_liquidgas_n_m"],
                         "0.02685")
        self.assertIn(0.4997, entry["grounded_values"])
        self.assertIn(293.15, entry["grounded_values"])
        self.assertEqual(entry["inspection_id"], "INSP_ace1f89aece6")

    def test_error_and_alien_results_skipped(self):
        history = [
            {"tool": "inspect_block_table",
             "result_full": "**inspect_block_table error** — no rows"},
            {"tool": "search_blocks", "result_full": "some markdown"},
        ]
        self.assertEqual(harvest_inspections(history), [])

    def test_harvest_dedupes_by_inspection_id(self):
        entries = harvest_inspections(HISTORY + HISTORY)
        self.assertEqual(len(entries), 1)

    def test_child_envelope_import_and_export_round_trip(self):
        exported = export_inspections(harvest_inspections(HISTORY))
        self.assertEqual(len(exported), 1)
        self.assertNotIn("BLKsubsys_id", exported[0])
        envelope = json.dumps({"answer": "…", "data_inspections": exported})
        history = [{"tool": "L1_query", "result_full": envelope}]
        entries = harvest_inspections(history)
        self.assertEqual(len(entries), 1)
        self.assertIn(0.02685, entries[0]["grounded_values"])


class GateTests(unittest.TestCase):
    def test_grounded_answer_passes(self):
        report = gate(GROUNDED_ANSWER, HISTORY)
        self.assertTrue(report.ok, report.violations)

    def test_unit_rescale_of_grounded_value_passes(self):
        report = gate(
            "GLOBlit_8821::PROPblock_13: maximum 28.85 mN/m.", HISTORY,
        )
        self.assertTrue(report.ok, report.violations)

    def test_fabricated_interior_grid_is_caught(self):
        report = gate(FABRICATED_ANSWER, HISTORY)
        self.assertFalse(report.ok)
        kinds = {v["kind"] for v in report.violations}
        self.assertEqual(kinds, {"UNGROUNDED_LITERAL"})
        flagged = {v["literals"][0] for v in report.violations}
        self.assertIn("0.02640", flagged)
        self.assertIn("0.02446", flagged)
        # Real endpoints quoted verbatim are NOT flagged.
        self.assertNotIn("0.0238", flagged)

    def test_uninspected_block_is_mandatory_violation(self):
        report = gate(UNINSPECTED_ANSWER, HISTORY)
        self.assertFalse(report.ok)
        self.assertEqual(report.violations[0]["kind"], "UNINSPECTED_BLOCK")
        self.assertIn("inspect_block_table", report.violations[0]["suggested_call"])
        self.assertIn("GLOBlit_4242::PROPblock_2",
                      report.violations[0]["suggested_call"])

    def test_answer_without_block_anchors_passes(self):
        report = gate(
            "The corpus contains many candidate systems.", HISTORY,
        )
        self.assertTrue(report.ok)

    def test_fit_metrics_are_exempt(self):
        report = gate(
            "GLOBlit_8821::PROPblock_13 Redlich–Kister fit: A0=0.014823, "
            "RMSE 0.00012, R² = 0.9987.", HISTORY,
        )
        self.assertTrue(report.ok, report.violations)

    def test_counts_years_and_ids_are_exempt(self):
        report = gate(
            "GLOBlit_8821::PROPblock_13 (7 rows, published 2005, "
            "BLKpoint_4) spans the full composition range.", HISTORY,
        )
        self.assertTrue(report.ok, report.violations)

    def test_nudge_flags_and_bounce_counting(self):
        report = gate(FABRICATED_ANSWER, HISTORY)
        nudge = build_gate_nudge(report)
        self.assertIn(GATE_MARKER, nudge)
        self.assertIn("inspect_block_table", nudge)
        self.assertIn(FLAGS_HEADER, build_flags_note(report))
        self.assertIn("DROP every uninspected",
                      build_timeout_gate_instruction(report))
        memory = [
            {"role": "user", "content": nudge},
            {"role": "assistant", "content": "…"},
            {"role": "user", "content": "other"},
        ]
        self.assertEqual(count_gate_bounces(memory), 1)

    def test_partially_grounded_anchor_reported_for_surgical_repair(self):
        report = gate(FABRICATED_ANSWER, HISTORY)
        self.assertEqual(report.verified, [])
        self.assertEqual(len(report.partially_grounded), 1)
        entry = report.partially_grounded[0]
        self.assertEqual(entry["anchor"], "GLOBlit_8821::PROPblock_13")
        self.assertIn("0.0238", entry["values"])       # real endpoint
        self.assertIn("0.1001", entry["values"])
        self.assertNotIn("0.02640", entry["values"])   # fabricated → flagged
        nudge = build_gate_nudge(report)
        self.assertIn("change ONLY the flagged one(s)", nudge)
        self.assertIn("Repair surgically", nudge)
        self.assertIn("- GLOBlit_8821::PROPblock_13:", nudge)
        self.assertIn("0.1001", nudge)

    def test_fully_verified_anchor_listed_alongside_violations(self):
        answer = GROUNDED_ANSWER + " Meanwhile " + UNINSPECTED_ANSWER
        report = gate(answer, HISTORY)
        self.assertFalse(report.ok)
        self.assertEqual([v["anchor"] for v in report.verified],
                         ["GLOBlit_8821::PROPblock_13"])
        context = build_grounded_context(report)
        self.assertIn("Verified as grounded", context)
        self.assertIn("GLOBlit_8821::PROPblock_13", context)
        self.assertIn("0.02685", context)              # itemized token
        self.assertIn("keep unchanged", context)
        self.assertIn("Verified as grounded",
                      build_timeout_gate_instruction(report))
        # The shipped flags note stays violations-only.
        self.assertNotIn("Verified as grounded", build_flags_note(report))

    def test_violation_overflow_itemizes_every_value_with_anchor(self):
        blocks = " ".join(
            f"GLOBlit_{n}::PROPblock_1 reports 1.234{n} mPa·s at 300.1{n} K."
            for n in range(1, 12)
        )
        report = gate(blocks, HISTORY)
        self.assertGreater(len(report.violations), 8)
        text = report.report_text
        # Every offending value is itemized with its anchor, even past the cap.
        self.assertIn("GLOBlit_11::PROPblock_1", text)
        self.assertIn("1.23411", text)
        self.assertNotIn("more violation(s) of the same kinds", text)

    def test_clean_report_has_no_grounded_context_noise(self):
        report = gate(GROUNDED_ANSWER, HISTORY)
        self.assertTrue(report.ok)
        self.assertEqual(report.partially_grounded, [])
        self.assertEqual([v["anchor"] for v in report.verified],
                         ["GLOBlit_8821::PROPblock_13"])
        self.assertIn("0.02685", report.verified[0]["values"])


AUTH_13 = {
    "doi": "10.1021/je050519g",
    "lit_num_id": "GLOBlit_8821",
    "block_number": "PROPblock_13",
    "n_rows": 9,
    "columns": ["BLKpoint_id", "mole_fraction_acetonitrile",
                "surface_tension_liquidgas_n_m"],
    # Superset of the inspection: 0.02741 exists in the DB, never inspected.
    "values": frozenset({0.1001, 0.2011, 0.6003, 0.02741, 0.0238, 0.02885}),
    "column_ranges": {
        "mole_fraction_acetonitrile": (0.1001, 0.8956),
        "surface_tension_liquidgas_n_m": (0.0238, 0.02885),
    },
}


class AuthoritativeLadderTests(unittest.TestCase):
    def test_uninspected_value_found_in_authoritative_table(self):
        report = gate(
            "GLOBlit_8821::PROPblock_13 also reports 0.02741 N/m.",
            HISTORY, fetch=_fake_fetch({"PROPblock_13": AUTH_13}),
        )
        self.assertFalse(report.ok)
        violation = report.violations[0]
        self.assertEqual(violation["kind"], "UNINSPECTED_VALUE")
        self.assertIn("database table", violation["detail"])
        # Range-aware axis pick: 0.02741 lies in the surface-tension range.
        self.assertIn('"surface_tension_liquidgas_n_m"',
                      violation["suggested_call"])
        self.assertIn("0.02741", violation["suggested_call"])

    def test_misattributed_value_cites_single_true_source(self):
        history = HISTORY + [_envelope_history(
            "PROPblock_7", "10.1/bbb", "GLOBlit_9", ["1.0421"],
            "INSP_bbbbbbbbbbbb",
        )]
        report = gate(
            "GLOBlit_8821::PROPblock_13 gives 1.0421 at equimolar mix.",
            history,
        )
        self.assertFalse(report.ok)
        violation = report.violations[0]
        self.assertEqual(violation["kind"], "MISATTRIBUTED_VALUE")
        self.assertIn("GLOBlit_9::PROPblock_7", violation["detail"])
        self.assertIn("inspected this run", violation["detail"])
        self.assertIn("re-anchor", violation["suggested_call"])
        self.assertIn("no new tool call needed", violation["suggested_call"])

    def test_ambiguous_value_flags_count_without_listing_blocks(self):
        history = HISTORY + [
            _envelope_history("PROPblock_7", "10.1/bbb", "GLOBlit_9",
                              ["55.55"], "INSP_bbbbbbbbbbbb"),
            _envelope_history("PROPblock_8", "10.1/ccc", "GLOBlit_10",
                              ["55.55"], "INSP_cccccccccccc"),
        ]
        report = gate(
            "GLOBlit_8821::PROPblock_13 shows 55.55 mN/m at the endpoint.",
            history,
        )
        self.assertFalse(report.ok)
        violation = report.violations[0]
        self.assertEqual(violation["kind"], "AMBIGUOUS_VALUE")
        self.assertIn("matches 2 different sources", violation["detail"])
        self.assertNotIn("PROPblock_7", violation["detail"])
        self.assertNotIn("PROPblock_8", violation["detail"])

    def test_answer_table_merges_all_cited_sources(self):
        history = HISTORY + [_envelope_history(
            "PROPblock_7", "10.1/bbb", "GLOBlit_9", ["1.0421"],
            "INSP_bbbbbbbbbbbb",
        )]
        answer = (
            "Comparison across sources:\n\n"
            "| block | value |\n"
            "|---|---|\n"
            "| GLOBlit_8821::PROPblock_13 | 1.0421 |\n"
            "| GLOBlit_9::PROPblock_7 | 0.02685 |\n"
        )
        # Each value sits in the OTHER block's row — table-level merge passes.
        report = gate(answer, history)
        self.assertTrue(report.ok, report.violations)
        self.assertEqual(len(report.verified), 1)
        self.assertIn(" + ", report.verified[0]["anchor"])

    def test_uninspected_block_notes_db_confirmation_but_still_bounces(self):
        fetch = _fake_fetch({"PROPblock_2": {
            "doi": "10.1/ddd", "lit_num_id": "GLOBlit_4242",
            "block_number": "PROPblock_2", "n_rows": 4,
            "columns": ["BLKpoint_id", "viscosity"],
            "values": frozenset({14.23, 303.15, 10.90, 313.15}),
            "column_ranges": {"viscosity": (10.90, 14.23)},
        }})
        report = gate(UNINSPECTED_ANSWER, HISTORY, fetch=fetch)
        self.assertFalse(report.ok)
        violation = report.violations[0]
        self.assertEqual(violation["kind"], "UNINSPECTED_BLOCK")
        self.assertIn("verified against the database", violation["detail"])
        self.assertIn("inspection is still mandatory", violation["detail"])

    def test_no_silent_union_pass_anymore(self):
        # A foreign inspected value inside another block's prose segment is
        # flagged (previously the union fallback passed it silently).
        history = HISTORY + [_envelope_history(
            "PROPblock_7", "10.1/bbb", "GLOBlit_9", ["1.0421"],
            "INSP_bbbbbbbbbbbb",
        )]
        report = gate(
            "GLOBlit_8821::PROPblock_13 spans 0.0238–0.02885 N/m and "
            "reaches 1.0421 nowhere.", history,
        )
        self.assertFalse(report.ok)
        self.assertEqual(report.violations[0]["kind"], "MISATTRIBUTED_VALUE")
        # The genuine endpoints stay verified for the surgical keep-list.
        self.assertEqual(len(report.partially_grounded), 1)
        self.assertIn("0.0238", report.partially_grounded[0]["values"])


class ArgumentPoolTests(unittest.TestCase):
    """Lit↔block chains recovered from recorded tool ARGUMENTS."""

    def test_harvest_pools_all_argument_forms(self):
        history = [
            # qualified form inside block_number
            {"tool": "inspect_block_table",
             "arguments": {"block_number": "GLOBlit_7::PROPblock_3"},
             "result_full": "**inspect_block_table error** — no rows"},
            # bare block + literature (GLOBlit)
            {"tool": "inspect_block_table",
             "arguments": {"block_number": "PROPblock_4",
                           "literature": "GLOBlit_2574"},
             "result_full": "error"},
            # bare block + DOI hint (passed through verbatim)
            {"tool": "inspect_block_table",
             "arguments": {"block_number": "PROPblock_9",
                           "literature": "10.1016/j.tca.2006.02.028"},
             "result_full": "error"},
            # menu wrapper nesting + qualified pair in purpose prose
            {"tool": "run_subagent_tool",
             "arguments": {"tool_name": "inspect_block_table",
                           "kwargs": {"block_number": "PROPblock_5",
                                      "literature": "GLOBlit_11"},
                           "purpose": "verify GLOBlit_12::RXNblock_2 rows"},
             "result_full": "error"},
            # duplicate — deduped
            {"tool": "inspect_block_table",
             "arguments": {"block_number": "GLOBlit_7::PROPblock_3"},
             "result_full": "error"},
        ]
        targets = harvest_inspection_targets(history)
        self.assertEqual(targets["PROPblock_3"], ["GLOBlit_7"])
        self.assertEqual(targets["PROPblock_4"], ["GLOBlit_2574"])
        self.assertEqual(targets["PROPblock_9"],
                         ["10.1016/j.tca.2006.02.028"])
        self.assertEqual(targets["PROPblock_5"], ["GLOBlit_11"])
        self.assertEqual(targets["RXNblock_2"], ["GLOBlit_12"])

    def test_errored_inspect_arguments_still_key_authoritative_fetch(self):
        # The inspect call FAILED (no parseable markdown) but its arguments
        # carry the full chain — the bare answer anchor must still reach
        # the database table through the pooled arguments.
        seen: list[tuple] = []

        def fetch(lit, block):
            seen.append((lit, block))
            if block == "PROPblock_2":
                return {
                    "doi": "10.1/ddd", "lit_num_id": "GLOBlit_4242",
                    "block_number": "PROPblock_2", "n_rows": 4,
                    "columns": ["BLKpoint_id", "viscosity"],
                    "values": frozenset({14.23, 303.15}),
                    "column_ranges": {"viscosity": (10.90, 14.23)},
                }
            return None

        history = HISTORY + [{
            "tool": "inspect_block_table",
            "arguments": {"block_number": "PROPblock_2",
                          "literature": "GLOBlit_4242",
                          "nearest": {"column": "viscosity", "value": 14.23}},
            "result_full": "**inspect_block_table error** — nearest column",
        }]
        report = gate(
            "PROPblock_2 reports 14.23 mPa·s at 303.15 K.",
            history, fetch=fetch,
        )
        self.assertIn(("GLOBlit_4242", "PROPblock_2"), seen)
        self.assertFalse(report.ok)
        violation = report.violations[0]
        self.assertEqual(violation["kind"], "UNINSPECTED_BLOCK")
        self.assertIn("verified against the database", violation["detail"])
        self.assertIn('"GLOBlit_4242::PROPblock_2"',
                      violation["suggested_call"])


class EvidenceLogTests(unittest.TestCase):
    def test_build_evidence_log_is_json_safe_and_renders(self):
        inspections = harvest_inspections(HISTORY)
        report = gate(FABRICATED_ANSWER, HISTORY, inspections=inspections)
        payload, markdown = build_evidence_log(report, inspections)
        json.dumps(payload)                       # JSON-safe end to end
        self.assertFalse(payload["gate_ok"])
        self.assertIn("PROPblock_13", payload["evidence"]["cited_blocks"])
        verdicts = {v["verdict"] for v in payload["evidence"]["literal_verdicts"]}
        self.assertIn("verified", verdicts)
        self.assertIn("ungrounded", verdicts)
        self.assertIn("## Literal verdicts", markdown)
        self.assertIn("## Inspections (verbatim)", markdown)
        self.assertIn("INSP_ace1f89aece6", markdown)

    def test_write_grounding_evidence_files_and_skip(self):
        import tempfile
        from pathlib import Path
        with tempfile.TemporaryDirectory() as tmp:
            path = write_grounding_evidence(
                tmp, GROUNDED_ANSWER, HISTORY, authoritative_fetch=_no_auth,
            )
            self.assertIsNotNone(path)
            self.assertTrue(Path(tmp, "grounding_evidence.json").is_file())
            self.assertTrue(Path(tmp, "grounding_evidence.md").is_file())
            skipped = write_grounding_evidence(
                Path(tmp) / "empty", "No data quoted here.", [],
                authoritative_fetch=_no_auth,
            )
            self.assertIsNone(skipped)


# Faithful excerpts of the fit tools' deterministic renders (A2.3 run).
FIT_MULTI_MD = """**Multi-system RK Fit** — 3 systems
Errors: EG_methanol: No pure values given and the block's composition coverage is insufficient to extract direct endpoints.

| Label | DOI | Block | Components | Order | R² | RMSE | n pts |
|-------|-----|-------|------------|-------|----|------|-------|
| EG_water | GLOBlit_5201 / DOI 10.1016/j.jct.2018.02.022 | PROPblock_24 @ declared | 1,2-ethanediol, water | 3 | 0.999940 | 0.00131989 | 19 |
| water_methanol | GLOBlit_2825 / DOI 10.1016/j.jct.2007.05.004 | PROPblock_9 @ declared | water, methanol | 3 | 0.999903 | 0.00204968 | 11 |

**EG_water** coeffs: [2.39674, -1.04444, 0.668173, -0.3209]
  pure values (x = mole_fraction_<1,2-ethanediol>): 1,2-ethanediol=0.016223, water=0.00089689

**water_methanol** coeffs: [2.53477, 1.42214, 1.33593, 0.754488]
  pure values (x = mole_fraction_<water>): water=0.00089, methanol=0.000545
"""

FIT_BLOCK_MD = """**RK Fit** — GLOBlit_692 / DOI 10.1016/j.fluid.2009.03.002 / PROPblock_1 @ declared
Components: 1,2-ethanediol, methanol | Mixing rule: arrhenius
Points: 3 mixture / 12 total

BIC-selected order: 0 | R² = -4.949320 | RMSE = 0.0355904 | BIC = -14.01
Coefficients: [0.714727]
"""

FIT_HISTORY = [
    {"tool": "fit_multi_system", "arguments": {}, "result_full": FIT_MULTI_MD},
    {"tool": "fit_block", "arguments": {}, "result_full": FIT_BLOCK_MD},
]


class FitArtifactTests(unittest.TestCase):
    def test_gate_enabled_for_analysis_inspect_block(self):
        self.assertTrue(gate_enabled({"inspect_block", "fit_block"}))
        self.assertTrue(gate_enabled({"inspect_block_table"}))
        self.assertFalse(gate_enabled({"fit_block", "query_thermoml"}))

    def test_harvest_pools_values_under_deterministic_fit_ids(self):
        fits = harvest_fit_artifacts(FIT_HISTORY)
        self.assertEqual(len(fits), 2)
        again = harvest_fit_artifacts(FIT_HISTORY + FIT_HISTORY)  # dedup
        self.assertEqual(
            {f["fit_id"] for f in fits}, {f["fit_id"] for f in again},
        )
        multi = next(f for f in fits if "Multi-system" in f["heading"])
        self.assertTrue(multi["fit_id"].startswith("FIT_"))
        self.assertEqual(multi["blocks"], ["PROPblock_24", "PROPblock_9"])
        self.assertIn(2.53477, multi["values"])
        self.assertIn(0.00089689, multi["values"])
        # DOI fragments are masked — no junk floats from 10.1016/j.jct.2018…
        self.assertNotIn(2018.02, multi["values"])
        self.assertNotIn(10.1016, multi["values"])
        single = next(f for f in fits if f is not multi)
        self.assertIn(-4.94932, single["values"])
        self.assertIn(0.714727, single["values"])

    def test_harvest_detects_the_whole_fitting_family(self):
        family = [
            "**Dual-baseline RK Fit** — GLOBlit_1 / PROPblock_2\nR² = 0.91\n",
            "**Sweep RK Fit** — GLOBlit_1 / PROPblock_2\n303.15 K: A0=1.5\n",
            "**Multi-property RK Fit** — GLOBlit_1 / PROPblock_2 — 2 props\n",
            "**RK Prediction** (order 3, arrhenius)\nx=0.5 → 0.00161\n",
            "**Ideal baseline** (arrhenius)\nln η = -6.43 at x=0.5\n",
            "**Pure values** from GLOBlit_5201 / PROPblock_24 (298.15 K)\n"
            "water: 0.00089689\n",
            "**⚠ AGENT-BUILT BLOCK REGISTERED (not experimental DB data)**\n"
            "value 42.42\n",                     # excluded: not a fit rail
        ]
        fits = harvest_fit_artifacts(
            [{"tool": "t", "arguments": {}, "result_full": md}
             for md in family]
        )
        self.assertEqual(len(fits), 6)
        pooled = set().union(*(f["values"] for f in fits))
        self.assertIn(0.00161, pooled)
        self.assertIn(-6.43, pooled)
        self.assertIn(0.00089689, pooled)
        self.assertNotIn(42.42, pooled)

    def test_fit_coefficients_in_answer_table_are_grounded(self):
        # The A2.3 storm: rounded coefficients/stats in a block-anchored
        # table, blocks never inspected — pure fit regions must not flag.
        answer = (
            "| Pair | Block | A0 val | Rsq val | RMSE val |\n"
            "|---|---|---|---|---|\n"
            "| EG + water | PROPblock_24 | 2.397 | 0.9999 | 0.00132 |\n"
            "| water + methanol | PROPblock_9 | 2.535 | 0.9999 | 0.00205 |\n"
            "| EG + methanol | PROPblock_1 | 0.715 | -4.95 | 0.0356 |\n"
        )
        report = gate(answer, FIT_HISTORY)
        self.assertTrue(report.ok, report.violations)
        by_verdict = {}
        for verdict in report.evidence["literal_verdicts"]:
            by_verdict.setdefault(verdict["verdict"], []).append(verdict)
        tokens = {v["token"] for v in by_verdict.get("fit_artifact", [])}
        self.assertIn("2.535", tokens)
        self.assertIn("-4.95", tokens)
        for verdict in by_verdict.get("fit_artifact", []):
            self.assertTrue(verdict["source"].startswith("FIT_"))
        self.assertEqual(
            report.evidence["fit_artifacts"][0]["n_values"] > 0, True,
        )

    def test_inspection_match_takes_precedence_over_fit_pool(self):
        # 293.15 exists in both the inspection and a fit render → verified.
        history = HISTORY + [{
            "tool": "fit_block", "arguments": {},
            "result_full": "**RK Fit** — X\nfitted at 293.15 K, R² = 0.99\n",
        }]
        report = gate(
            "GLOBlit_8821::PROPblock_13 measured 0.02685 N/m at 293.15 K.",
            history,
        )
        self.assertTrue(report.ok)
        verdicts = {
            v["token"]: v["verdict"]
            for v in report.evidence["literal_verdicts"]
        }
        self.assertEqual(verdicts["293.15"], "verified")
        self.assertEqual(verdicts["0.02685"], "verified")

    def test_derived_values_still_flag_next_to_fit_values(self):
        answer = (
            "| Pair | Block | A0 val | Share val |\n"
            "|---|---|---|---|\n"
            "| EG + water | PROPblock_24 | 2.397 | 0.266 |\n"
        )
        report = gate(answer, FIT_HISTORY)
        self.assertFalse(report.ok)
        self.assertEqual(len(report.violations), 1)
        self.assertEqual(report.violations[0]["literals"], ["0.266"])
        self.assertEqual(  # the fit-grounded neighbour is kept verified
            report.partially_grounded,
            [{"anchor": "PROPblock_24", "values": ["2.397"]}],
        )

    def test_evidence_markdown_renders_fit_rail(self):
        answer = (
            "| Pair | Block | A0 val |\n|---|---|---|\n"
            "| EG + water | PROPblock_24 | 2.397 |\n"
        )
        report = gate(answer, FIT_HISTORY)
        payload, markdown = build_evidence_log(report, [])
        json.dumps(payload)
        self.assertIn("## Fit artifacts (grounded rail)", markdown)
        self.assertIn("Multi-system RK Fit", markdown)
        self.assertIn("fit_artifact", markdown)


if __name__ == "__main__":
    unittest.main()
