"""Master test for all public basic-search tools and strict ID contracts."""
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, _REPO_ROOT)
sys.path.insert(0, _HERE)

passed = []
failed = []

def test(name, fn):
    try:
        fn()
        passed.append(name)
        print(f"  PASS: {name}")
    except Exception as e:
        failed.append((name, str(e)))
        print(f"  FAIL: {name} — {e}")

# ── 0. ID Alignment ─────────────────────────────────────────────────────────
from _id_alignment_search import search_id_alignment

def t_id_compound():
    r = search_id_alignment("compound", "ethanol", limit=3)
    assert r["n_results"] >= 1
    assert r["results"][0]["common_name"] == "ethanol"
    assert r["results"][0]["score"] == 100

def t_id_property():
    r = search_id_alignment("property", "viscosity", limit=3)
    assert r["n_results"] >= 1
    assert "viscosity" in r["results"][0]["prop_name"].lower()

def t_id_ref():
    r = search_id_alignment("reference", "10.1007/s10765-005-5566-6", limit=2)
    assert r["n_results"] == 1
    assert r["results"][0]["doi"] == "10.1007/s10765-005-5566-6"

test("id_alignment: compound", t_id_compound)
test("id_alignment: property", t_id_property)
test("id_alignment: reference", t_id_ref)

# ── 1. Block Search ──────────────────────────────────────────────────────────
from importlib import import_module
m1 = import_module("1_block_search")

def t_block_doi():
    r = m1.search_blocks(literature="10.1007/s10765-005-5566-6", limit=10)
    assert r["n_results"] >= 1
    assert r["results"][0]["doi"] == "10.1007/s10765-005-5566-6"

def t_block_compound_prop():
    r = m1.search_blocks(compound="water", property="density", limit=5)
    assert r["n_results"] >= 1

test("block_search: doi", t_block_doi)
test("block_search: compound+property", t_block_compound_prop)

# ── 2. System Registry Search ────────────────────────────────────────────────
m2 = import_module("2_system_registry_search")

def t_registry_compound():
    r = m2.search_system_registry(compound="water", limit=5)
    assert r["n_results"] >= 1

def t_registry_system_type():
    r = m2.search_system_registry(compound="ethanol", system_type="binary", limit=5)
    assert r["n_results"] >= 1

test("system_registry: compound", t_registry_compound)
test("system_registry: compound+system_type", t_registry_system_type)

# ── 3. Compound DK Search ────────────────────────────────────────────────────
m3 = import_module("3_compound_DK_search")

def t_comp_dk_name():
    r = m3.search_compound_dk(compound="water", limit=3)
    assert r["n_results"] >= 1
    res = r["results"][0]
    assert res["comp_num_id"] == "GLOBcomp_1"
    assert "identity" in res or "names" in res

def t_comp_dk_smiles():
    r = m3.search_compound_dk(compound="CCO", limit=3)
    assert r["n_results"] >= 1

test("compound_dk: name", t_comp_dk_name)
test("compound_dk: SMILES", t_comp_dk_smiles)

# ── 4. Reference Search ──────────────────────────────────────────────────────
m4 = import_module("4_reference_search")

def t_ref_doi():
    r = m4.search_references(literature="10.1007/s10765-005-5566-6", limit=5)
    assert r["n_results"] >= 1

def t_ref_year_compound():
    r = m4.search_references(year=2005, compound="methane", limit=5)
    assert r["n_results"] >= 1

test("reference: doi", t_ref_doi)
test("reference: year+compound", t_ref_year_compound)

# ── 5. Measurement DK Search ─────────────────────────────────────────────────
m5 = import_module("5_meas_DK_search")

def t_meas_dk():
    r = m5.search_measurement_dk(measurement="DSC", limit=3)
    assert r["n_results"] >= 1
    assert r["results"][0]["meas_num_id"] == "GLOBmeas_132"

test("measurement_dk: DSC", t_meas_dk)

# ── 6. Measurement INDIV Search ──────────────────────────────────────────────
m6 = import_module("6_meas_INDIV_search")

def t_meas_indiv_doi():
    r = m6.search_measurement_indiv(literature="10.1007/s10765-005-5566-6", limit=10)
    assert r["n_results"] >= 1

def t_meas_indiv_method():
    r = m6.search_measurement_indiv(method="DSC", limit=5)
    assert r["n_results"] >= 1

test("measurement_indiv: doi", t_meas_indiv_doi)
test("measurement_indiv: method", t_meas_indiv_method)

# ── 7. Property DK Search ────────────────────────────────────────────────────
m7 = import_module("7_prop_DK_search")

def t_prop_dk():
    r = m7.search_property_dk(property="density", limit=3)
    assert r["n_results"] >= 1
    assert "density" in r["results"][0]["identity"]["name"].lower()

test("property_dk: density", t_prop_dk)

# ── 8. Compound INDIV Search ─────────────────────────────────────────────────
m8 = import_module("8_compound_INDIV_search")

def t_comp_indiv():
    r = m8.search_compound_indiv(compound="water", limit=5)
    assert r["n_results"] >= 1

def t_comp_indiv_doi():
    r = m8.search_compound_indiv(literature="10.1007/s10765-005-5567-5", limit=10)
    assert r["n_results"] >= 1

test("compound_indiv: water", t_comp_indiv)
test("compound_indiv: doi", t_comp_indiv_doi)

# ── 9. System Summary Search ─────────────────────────────────────────────────
m9 = import_module("9_system_summary_search")

def t_summary_compound():
    r = m9.search_system_summary(compound="water", limit=5)
    assert "summary" in r
    assert r["summary"]["n_blocks"] > 0
    assert r["summary"]["n_papers"] > 0

def t_summary_prop():
    r = m9.search_system_summary(property="viscosity", limit=5)
    assert r["summary"]["n_blocks"] > 0

test("system_summary: water", t_summary_compound)
test("system_summary: viscosity", t_summary_prop)

# ── 10. Strict scoped-ID contract ───────────────────────────────────────────
m10 = import_module("10_compound_similarity_search")
m11 = import_module("11_block_data_extractor")

def _assert_refinement(result, field):
    assert result["error_code"] == "ID_REFINEMENT_REQUIRED"
    assert result["refinement"]["field"] == field

def t_strict_global_accepts():
    r = m3.search_compound_dk(compound="GLOBcomp_1", limit=1)
    assert r["results"][0]["comp_num_id"] == "GLOBcomp_1"

def t_legacy_compound_rejected():
    _assert_refinement(m1.search_blocks(compound="comp_1"), "compound")

def t_bare_global_rejected():
    _assert_refinement(m3.search_compound_dk(compound=1), "compound")

def t_wrong_global_namespace_rejected():
    _assert_refinement(m1.search_blocks(compound="GLOBprop_1"), "compound")

def t_native_multi_value_accepts():
    r = m1.search_blocks(compound=["GLOBcomp_1", "GLOBcomp_3"], limit=1)
    assert r["query_params"]["compound"] == ["GLOBcomp_1", "GLOBcomp_3"]

def t_semicolon_multi_value_rejected():
    _assert_refinement(
        m1.search_blocks(compound="GLOBcomp_1;GLOBcomp_3", limit=1),
        "compound",
    )

def t_similarity_requires_global_id():
    _assert_refinement(m10.search_similar_compounds(comp_num_id="comp_1"), "comp_num_id")

def t_legacy_block_rejected():
    _assert_refinement(
        m11.extract_block_csv("10.1007/s10765-005-5566-6", "block_1"),
        "block_number",
    )

def t_typed_block_accepts():
    r = m11.extract_block_csv(
        "10.1007/s10765-005-5566-6", "PROPblock_1"
    )
    assert r["block_number"] == "PROPblock_1"

test("strict IDs: canonical global accepted", t_strict_global_accepts)
test("strict IDs: legacy compound rejected", t_legacy_compound_rejected)
test("strict IDs: bare global rejected", t_bare_global_rejected)
test("strict IDs: wrong global namespace rejected", t_wrong_global_namespace_rejected)
test("strict IDs: native multi-value accepted", t_native_multi_value_accepts)
test("strict IDs: semicolon multi-value rejected", t_semicolon_multi_value_rejected)
test("strict IDs: similarity requires GLOBcomp", t_similarity_requires_global_id)
test("strict IDs: legacy block rejected", t_legacy_block_rejected)
test("strict IDs: typed block accepted", t_typed_block_accepts)

# ── Summary ──────────────────────────────────────────────────────────────────
print()
print("=" * 60)
print(f"RESULTS: {len(passed)} passed, {len(failed)} failed")
print("=" * 60)
if failed:
    for name, err in failed:
        print(f"  FAILED: {name} — {err}")
    raise SystemExit(1)
else:
    print("  ALL TESTS PASSED!")
