"""Export registry CSV files directly from thermoml_raw.db.

Parses all JSON cards in papers.json_data and aggregates properties,
variables, constraints, measurements, compounds, references, block types, and
solvents, phases, and reaction types into 10 CSV files.

All operations are READ-ONLY against the raw database.
"""

import csv
import json
import os
import shutil
import sqlite3
import sys
import time

try:
    from rdkit import Chem
    from rdkit import RDLogger
    RDLogger.DisableLog("rdApp.*")
    _HAS_RDKIT = True
except ImportError:
    _HAS_RDKIT = False

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from ThermoML_raw_json_to_card_db_parsers.shared_utils import (
    slugify, meas_id_slugify, strip_comp_suffix,
    extract_trc_ref_id, extract_property_info, canonical_compound_key,
    system_type_label, safe_float, safe_int, extract_var_or_constraint_type,
)
from ThermoML_raw_json_to_card_db_parsers.id_schema import (
    component_template_id,
    global_id,
)

HERE = os.path.dirname(os.path.abspath(__file__))
RAW_DB = os.path.join(HERE, '..', '..', '..', 'ThermoML.v2020-09-30.db', 'thermoml_raw.db')
ID_LIST_DIR = os.path.join(HERE, '..', 'id_name_lists')
CANONICAL_STORAGE_DIR = os.path.join(
    HERE, '..', '..', '..', 'card_databases_storage',
    'Canonicalized_ID_name_lists_csvs',
)


def _write_csv(path, headers, rows):
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)


# ═══════════════════════════════════════════════════════════════════════════════
#  Variable and constraint extraction (inlined from obsolete builder modules)
# ═══════════════════════════════════════════════════════════════════════════════

def _extract_variables(block):
    """Extract variable definitions from a ThermoML block dict."""
    results = []
    for var in block.get("Variable", []):
        vnum = var.get("nVarNumber", 0)
        vid = var.get("VariableID", {})
        vtype_dict = vid.get("VariableType", {})
        vname, vcat = extract_var_or_constraint_type(vtype_dict)
        comp_ref = vid.get("RegNum", {}).get("nOrgNum")
        results.append({
            "var_number": vnum,
            "var_id": slugify(vname) if vname else "",
            "var_name": vname,
            "var_type_key": vcat,
            "comp_org_num": comp_ref,
        })
    return results


def _extract_variable_ranges(block):
    """Scan NumValues to compute min/max/n_unique for each variable."""
    ranges = {}
    for nv in block.get("NumValues", []):
        for vv in nv.get("VariableValue", []):
            vnum = vv.get("nVarNumber")
            vval = safe_float(vv.get("nVarValue"))
            if vnum is not None and vval is not None:
                ranges.setdefault(vnum, []).append(vval)
    out = {}
    for vnum, vals in ranges.items():
        out[vnum] = {"min": min(vals), "max": max(vals), "n_unique": len(set(vals))}
    return out


def _build_variable_index(block):
    """Full variable index for a block: definitions + ranges merged."""
    defs = _extract_variables(block)
    ranges = _extract_variable_ranges(block)
    for d in defs:
        r = ranges.get(d["var_number"], {})
        d["min_value"] = r.get("min")
        d["max_value"] = r.get("max")
        d["n_unique"] = r.get("n_unique")
    return defs


def _extract_constraints(block):
    """Extract constraint definitions from a ThermoML block dict."""
    results = []
    for constr in block.get("Constraint", []):
        cnum = constr.get("nConstraintNumber", 0)
        cid = constr.get("ConstraintID", {})
        ctype_dict = cid.get("ConstraintType", {})
        cname, ccat = extract_var_or_constraint_type(ctype_dict)
        comp_ref = cid.get("RegNum", {}).get("nOrgNum")
        cval = safe_float(constr.get("nConstraintValue"))
        cdigits = safe_int(constr.get("nConstrDigits"))
        results.append({
            "constr_number": cnum,
            "constr_id": slugify(cname) if cname else "",
            "constr_name": cname,
            "constr_type_key": ccat,
            "value": cval,
            "digits": cdigits,
            "comp_org_num": comp_ref,
        })
    return results


# ═══════════════════════════════════════════════════════════════════════════════
#  Parse all JSON cards from the raw DB
# ═══════════════════════════════════════════════════════════════════════════════

def _parse_all_cards(raw_db):
    """Parse every JSON card, collecting aggregated registry data.

    Returns a dict with all accumulators needed for every CSV file.
    """
    conn = sqlite3.connect(f'file:{raw_db}?mode=ro', uri=True)

    # ── Compound metadata from the compounds table ───────────────────────
    comp_rows = conn.execute(
        "SELECT doi, org_num, standard_inchi_key, standard_inchi, common_name, formula, cas_rn "
        "FROM compounds"
    ).fetchall()

    comp_meta = {}          # canonical_key -> [common_name, formula, standard_inchi]
    comp_papers = {}        # canonical_key -> set(doi)
    paper_comp_key = {}     # (doi, org_num) -> canonical_key

    for doi, org_num, inchi_key, inchi, name, formula, cas_rn in comp_rows:
        ckey = canonical_compound_key(
            standard_inchi_key=inchi_key, standard_inchi=inchi,
            common_name=name, formula=formula, cas_rn=cas_rn,
        )
        comp_papers.setdefault(ckey, set()).add(doi)
        paper_comp_key[(doi, org_num)] = ckey
        if ckey not in comp_meta:
            comp_meta[ckey] = [name, formula, inchi]
        else:
            m = comp_meta[ckey]
            if not m[0] and name:
                m[0] = name
            if not m[1] and formula:
                m[1] = formula
            if not m[2] and inchi:
                m[2] = inchi

    # ── Accumulators ─────────────────────────────────────────────────────
    # Properties: (base_slug, prop_name, prop_group) -> {plain_count, comp_count}
    prop_plain = {}
    prop_comp = {}
    # Variables: (base_slug, var_name, var_type_key) -> {plain_count, comp_count}
    var_plain = {}
    var_comp = {}
    # Constraints: (base_slug, constr_name, constr_type_key) -> {plain_count, comp_count}
    constr_plain = {}
    constr_comp = {}
    # Measurements have two deliberately separate registries:
    #   meas_accum: global canonical slug -> total occurrence count
    #   meas_alias_accum: every exact raw label -> canonical slug + occurrence type
    # Keeping the alias table prevents a lossy slug collision from forcing lookup
    # code to guess or fall back to re-slugifying source values.
    meas_accum = {}
    meas_alias_accum = {}
    # References
    ref_rows = []
    # Block types: (block_type, system_type) -> count
    blocktype_counts = {}
    # Solvent compounds: canonical_key -> n_blocks_as_solvent
    solvent_counts = {}
    # Phases: phase_name -> n_occurrences (across PropPhaseID, block PhaseID, Participant ePhase)
    phase_counts = {}
    # Reaction types: reaction_type_name -> n_blocks
    rxn_type_counts = {}

    # ── Iterate all papers ───────────────────────────────────────────────
    papers = conn.execute("SELECT doi, json_data FROM papers").fetchall()
    conn.close()

    t0 = time.time()
    for idx, (doi, json_data) in enumerate(papers):
        data = json.loads(json_data)

        # Reference info
        cit = data.get("Citation", {})
        lit_id, _ = extract_trc_ref_id(cit.get("TRCRefID"))
        authors = cit.get("sAuthor", [])
        if isinstance(authors, str):
            authors = [authors]
        compounds = data.get("Compound", [])

        pure_blocks = data.get("PureOrMixtureData", [])
        rxn_blocks = data.get("ReactionData", [])
        all_blocks = (
            [(b, "PureOrMixtureData") for b in pure_blocks]
            + [(b, "ReactionData") for b in rxn_blocks]
        )

        total_pts = 0
        for blk, btype in all_blocks:
            total_pts += len(blk.get("NumValues", []))

        ref_rows.append((
            doi, lit_id,
            authors[0] if authors else "",
            safe_int(cit.get("yrPubYr")),
            cit.get("sPubName", ""),
            len(compounds),
            len(all_blocks),
            total_pts,
        ))

        # Compound lookup for this paper
        comp_lookup = {}
        for comp in compounds:
            on = comp.get("RegNum", {}).get("nOrgNum")
            if on is None:
                continue
            names = comp.get("sCommonName", [])
            if isinstance(names, str):
                names = [names]
            comp_lookup[on] = {
                "name": names[0] if names else comp.get("sFormulaMolec", ""),
                "formula": comp.get("sFormulaMolec", ""),
            }

        for blk, btype in all_blocks:
            solvent_org_nums = set()
            # Components
            comp_key_name = "Component" if btype == "PureOrMixtureData" else "Participant"
            n_comp = len(blk.get(comp_key_name, []))
            sys_type = system_type_label(n_comp)

            bt_key = (btype, sys_type)
            blocktype_counts[bt_key] = blocktype_counts.get(bt_key, 0) + 1

            # Reaction types (ReactionData only)
            if btype == "ReactionData":
                rt = blk.get("eReactionType") or "Unreported reaction type"
                rxn_type_counts[rt] = rxn_type_counts.get(rt, 0) + 1

            # Block-level PhaseID (PureOrMixtureData)
            if btype == "PureOrMixtureData":
                phase_id = blk.get("PhaseID")
                if phase_id:
                    phase_list = phase_id if isinstance(phase_id, list) else [phase_id]
                    for ph in phase_list:
                        ep = ph.get("ePhase") if isinstance(ph, dict) else None
                        if ep:
                            phase_counts[ep] = phase_counts.get(ep, 0) + 1

            # Participant ePhase (ReactionData)
            if btype == "ReactionData":
                for part in blk.get("Participant", []):
                    ep = part.get("ePhase")
                    if ep:
                        phase_counts[ep] = phase_counts.get(ep, 0) + 1

            # Properties
            for prop in blk.get("Property", []):
                pname, gname, method_std, method_cust, comp_org_num = extract_property_info(prop)
                pid = slugify(pname) if pname else ""
                if not pid:
                    continue
                base_slug = pid
                key = (base_slug, pname, gname)
                if comp_org_num is not None:
                    prop_comp[key] = prop_comp.get(key, 0) + 1
                else:
                    prop_plain[key] = prop_plain.get(key, 0) + 1

                # Measurements
                if method_std:
                    mid = meas_id_slugify(method_std)
                    mtype = "standard"
                    mname = method_std
                elif method_cust:
                    mid = meas_id_slugify(method_cust)
                    mtype = "custom"
                    mname = method_cust
                else:
                    mid = None
                    mtype = None
                    mname = None

                # A non-empty source label must never disappear merely because
                # punctuation normalization produces an empty slug.  The raw
                # corpus contains one such label ("?"); represent it explicitly.
                if mname and not mid:
                    mid = "unreported_measurement_method"

                if mid:
                    meas_accum[mid] = meas_accum.get(mid, 0) + 1
                    alias_key = (mid, mname, mtype)
                    meas_alias_accum[alias_key] = meas_alias_accum.get(alias_key, 0) + 1

                # PropPhaseID phases
                pphase = prop.get("PropPhaseID")
                if pphase:
                    ep = pphase.get("ePropPhase")
                    if ep:
                        phase_counts[ep] = phase_counts.get(ep, 0) + 1

                # Property-level Solvent can contain one or multiple DOI-local
                # compound references.  These are authoritative solvent uses,
                # independent of eSolventComposition variables/constraints.
                solvent = prop.get("Solvent")
                if solvent:
                    solvent_regs = solvent.get("RegNum", [])
                    if isinstance(solvent_regs, dict):
                        solvent_regs = [solvent_regs]
                    for solvent_reg in solvent_regs:
                        solvent_org_num = solvent_reg.get("nOrgNum")
                        if solvent_org_num is not None:
                            solvent_org_nums.add(solvent_org_num)

            # Variables
            var_index = _build_variable_index(blk)
            for v in var_index:
                vid = v["var_id"]
                if not vid:
                    continue
                base_slug = vid
                key = (base_slug, v["var_name"], v["var_type_key"])
                if v["comp_org_num"] is not None:
                    var_comp[key] = var_comp.get(key, 0) + 1
                else:
                    var_plain[key] = var_plain.get(key, 0) + 1
                if v.get("var_type_key") == "eSolventComposition" and v["comp_org_num"] is not None:
                    solvent_org_nums.add(v["comp_org_num"])

            # Constraints
            constrs = _extract_constraints(blk)
            for c in constrs:
                cid = c["constr_id"]
                if not cid:
                    continue
                base_slug = cid
                key = (base_slug, c["constr_name"], c["constr_type_key"])
                if c["comp_org_num"] is not None:
                    constr_comp[key] = constr_comp.get(key, 0) + 1
                else:
                    constr_plain[key] = constr_plain.get(key, 0) + 1
                if c.get("constr_type_key") == "eSolventComposition" and c["comp_org_num"] is not None:
                    solvent_org_nums.add(c["comp_org_num"])

            # Solvent compounds
            for on in solvent_org_nums:
                ckey = paper_comp_key.get((doi, on))
                if ckey:
                    solvent_counts[ckey] = solvent_counts.get(ckey, 0) + 1

        if (idx + 1) % 2000 == 0:
            elapsed = time.time() - t0
            print(f"  {idx+1:>6d}/{len(papers)} parsed ({(idx+1)/elapsed:.0f} papers/s)")

    elapsed = time.time() - t0
    print(f"  Parsed {len(papers)} papers in {elapsed:.1f}s")

    return {
        "prop_plain": prop_plain, "prop_comp": prop_comp,
        "var_plain": var_plain, "var_comp": var_comp,
        "constr_plain": constr_plain, "constr_comp": constr_comp,
        "meas_accum": meas_accum,
        "meas_alias_accum": meas_alias_accum,
        "comp_meta": comp_meta, "comp_papers": comp_papers,
        "ref_rows": ref_rows,
        "blocktype_counts": blocktype_counts,
        "solvent_counts": solvent_counts,
        "phase_counts": phase_counts,
        "rxn_type_counts": rxn_type_counts,
    }


# ═══════════════════════════════════════════════════════════════════════════════
#  Build registry entries (plain + {DOIcomp_id} variants)
# ═══════════════════════════════════════════════════════════════════════════════

def _build_comp_aware_entries(plain_counts, comp_counts):
    """Merge plain and comp-linked counts into registry entries.

    Returns list of (slug, name, extra, n_blocks) sorted by n_blocks desc.
    """
    entries = {}
    for key, n in plain_counts.items():
        base_slug = key[0]
        rest = key[1:]
        entries[(base_slug,) + rest] = entries.get((base_slug,) + rest, 0) + n
    for key, n in comp_counts.items():
        base_slug = key[0]
        rest = key[1:]
        declared = component_template_id(base_slug)
        entries[(declared,) + rest] = entries.get((declared,) + rest, 0) + n
    return sorted(entries.items(), key=lambda x: (-x[1], x[0]))


# ═══════════════════════════════════════════════════════════════════════════════
#  CSV writers
# ═══════════════════════════════════════════════════════════════════════════════

def _export_property_ids(data, out_dir):
    entries = _build_comp_aware_entries(data["prop_plain"], data["prop_comp"])
    headers = ['prop_num_id', 'prop_id', 'prop_name', 'prop_group', 'comp_id_linked', 'n_blocks']
    rows = []
    for source_ordinal, (key, count) in enumerate(entries, start=1):
        slug = key[0]
        comp_linked = 1 if '{DOIcomp_id}' in slug else 0
        rows.append((global_id('prop_num_id', source_ordinal), slug, key[1], key[2], comp_linked, count))
    _write_csv(os.path.join(out_dir, 'property_ids.csv'), headers, rows)
    return len(rows)


def _export_variable_ids(data, out_dir):
    entries = _build_comp_aware_entries(data["var_plain"], data["var_comp"])
    headers = ['var_num_id', 'var_id', 'var_name', 'var_type_key', 'comp_id_linked', 'n_blocks']
    rows = []
    for source_ordinal, (key, count) in enumerate(entries, start=1):
        slug = key[0]
        comp_linked = 1 if '{DOIcomp_id}' in slug else 0
        rows.append((global_id('var_num_id', source_ordinal), slug, key[1], key[2], comp_linked, count))
    _write_csv(os.path.join(out_dir, 'variable_ids.csv'), headers, rows)
    return len(rows)


def _export_constraint_ids(data, out_dir):
    entries = _build_comp_aware_entries(data["constr_plain"], data["constr_comp"])
    headers = ['constr_num_id', 'constr_id', 'constr_name', 'constr_type_key', 'comp_id_linked', 'n_blocks']
    rows = []
    for source_ordinal, (key, count) in enumerate(entries, start=1):
        slug = key[0]
        comp_linked = 1 if '{DOIcomp_id}' in slug else 0
        rows.append((global_id('constr_num_id', source_ordinal), slug, key[1], key[2], comp_linked, count))
    _write_csv(os.path.join(out_dir, 'constraint_ids.csv'), headers, rows)
    return len(rows)


def _export_measurement_ids(data, out_dir):
    meas = data["meas_accum"]
    aliases = data["meas_alias_accum"]
    aliases_by_slug = {}
    for (meas_id, method_name, method_type), count in aliases.items():
        aliases_by_slug.setdefault(meas_id, []).append((method_name, method_type, count))

    # Choose a stable display label for each global type.  Exact input resolution
    # never uses this representative label; it uses measurement_aliases.csv.
    canonical = {}
    for meas_id, entries in aliases_by_slug.items():
        standard = [entry for entry in entries if entry[1] == 'standard']
        candidates = standard or entries
        representative = sorted(candidates, key=lambda x: (-x[2], x[0]))[0]
        canonical[meas_id] = {
            "method_name": representative[0],
            "method_type": "standard" if standard else "custom",
            "n_aliases": len(entries),
        }

    # Sort: standard-backed global types first, then frequency, then slug.
    ordered = sorted(
        meas.items(),
        key=lambda x: (
            0 if canonical[x[0]]["method_type"] == 'standard' else 1,
            -x[1],
            x[0],
        )
    )
    headers = [
        'meas_num_id', 'meas_id', 'method_name', 'method_type',
        'n_blocks', 'n_aliases',
    ]
    rows = []
    slug_to_num_id = {}
    for i, (mid, count) in enumerate(ordered, start=1):
        meas_num_id = global_id('meas_num_id', i)
        slug_to_num_id[mid] = meas_num_id
        info = canonical[mid]
        rows.append((
            meas_num_id, mid, info["method_name"], info["method_type"],
            count, info["n_aliases"],
        ))
    _write_csv(os.path.join(out_dir, 'measurement_ids.csv'), headers, rows)
    return len(rows), slug_to_num_id


def _export_measurement_aliases(data, out_dir, slug_to_num_id):
    """Export every exact raw method label as a first-class canonical alias."""
    headers = [
        'source_method_name', 'source_method_type', 'meas_num_id',
        'meas_id', 'n_blocks',
    ]
    rows = [
        (method_name, method_type, slug_to_num_id[meas_id], meas_id, count)
        for (meas_id, method_name, method_type), count
        in data["meas_alias_accum"].items()
    ]
    rows.sort(key=lambda row: (row[0], row[1], row[3]))
    _write_csv(os.path.join(out_dir, 'measurement_aliases.csv'), headers, rows)
    return len(rows)


def _inchi_to_smiles(inchi: str | None) -> str:
    """Convert an InChI string to canonical SMILES via RDKit. Returns '' on failure."""
    if not inchi or not _HAS_RDKIT:
        return ""
    mol = Chem.MolFromInchi(inchi)
    if mol is None:
        return ""
    return Chem.MolToSmiles(mol)


def _normalize_comp_id(name):
    """Derive comp_id from common_name: lowercase, spaces → underscores."""
    return name.replace(' ', '_').lower() if name else ""


def _export_compound_ids(data, out_dir):
    comp_meta = data["comp_meta"]
    comp_papers = data["comp_papers"]
    ordered = sorted(comp_papers, key=lambda k: (-len(comp_papers[k]), k))
    headers = ['comp_num_id', 'comp_id', 'inchi_key', 'common_name', 'formula', 'smiles', 'standard_inchi', 'n_papers']
    rows = []
    for source_ordinal, ckey in enumerate(ordered, start=1):
        name, formula, inchi = comp_meta[ckey]
        smiles = _inchi_to_smiles(inchi)
        comp_id = _normalize_comp_id(name)
        rows.append((global_id('comp_num_id', source_ordinal), comp_id, ckey, name, formula, smiles, inchi, len(comp_papers[ckey])))
    _write_csv(os.path.join(out_dir, 'compound_ids.csv'), headers, rows)
    return len(rows)


def _export_solvent_components(data, out_dir):
    solvent_counts = data["solvent_counts"]
    if not solvent_counts:
        return 0
    comp_meta = data["comp_meta"]
    comp_papers = data["comp_papers"]
    # Build canonical_key -> comp_num_id (same ordering as compound_ids.csv)
    ordered_keys = sorted(comp_papers, key=lambda k: (-len(comp_papers[k]), k))
    key_to_num = {
        k: global_id('comp_num_id', i)
        for i, k in enumerate(ordered_keys, start=1)
    }

    results = []
    for ckey, n_blocks in solvent_counts.items():
        num = key_to_num.get(ckey)
        if num is None:
            continue
        name, formula, inchi = comp_meta.get(ckey, ["", "", ""])
        results.append((num, ckey, name, formula, n_blocks))

    results.sort(key=lambda r: (-r[4], r[0]))
    headers = ['solvent_num_id', 'comp_num_id', 'inchi_key', 'common_name', 'formula', 'n_blocks_as_solvent']
    rows = [
        (global_id('solvent_num_id', i), r[0], r[1], r[2], r[3], r[4])
        for i, r in enumerate(results, start=1)
    ]
    _write_csv(os.path.join(out_dir, 'solvent_components.csv'), headers, rows)
    return len(rows)


def _export_reference_ids(data, out_dir):
    refs = sorted(data["ref_rows"], key=lambda r: r[0])  # sort by DOI
    headers = ['lit_num_id', 'doi', 'lit_id', 'first_author', 'year', 'journal',
               'n_compounds', 'n_blocks', 'total_datapoints']
    rows = [(global_id('lit_num_id', i), *r) for i, r in enumerate(refs, start=1)]
    _write_csv(os.path.join(out_dir, 'reference_ids.csv'), headers, rows)
    return len(rows)


def _export_block_types(data, out_dir):
    bt = data["blocktype_counts"]
    ordered = sorted(bt.items(), key=lambda x: (-x[1], x[0]))
    headers = ['blocktype_num_id', 'block_type', 'system_type', 'n_blocks']
    rows = [
        (global_id('blocktype_num_id', i), k[0], k[1], n)
        for i, (k, n) in enumerate(ordered, start=1)
    ]
    _write_csv(os.path.join(out_dir, 'block_types.csv'), headers, rows)
    return len(rows)


def _export_phase_ids(data, out_dir):
    pc = data["phase_counts"]
    ordered = sorted(pc.items(), key=lambda x: (-x[1], x[0]))
    headers = ['phase_num_id', 'phase_id', 'phase_name', 'n_occurrences']
    rows = [
        (global_id('phase_num_id', i), slugify(name), name, count)
        for i, (name, count) in enumerate(ordered, start=1)
    ]
    _write_csv(os.path.join(out_dir, 'phase_ids.csv'), headers, rows)
    return len(rows)


def _export_reaction_type_ids(data, out_dir):
    rt = data["rxn_type_counts"]
    ordered = sorted(rt.items(), key=lambda x: (-x[1], x[0]))
    headers = ['rxn_type_num_id', 'rxn_type_id', 'rxn_type_name', 'n_blocks']
    rows = [
        (global_id('rxn_type_num_id', i), slugify(name), name, count)
        for i, (name, count) in enumerate(ordered, start=1)
    ]
    _write_csv(os.path.join(out_dir, 'reaction_type_ids.csv'), headers, rows)
    return len(rows)


# ═══════════════════════════════════════════════════════════════════════════════
#  Main entry points
# ═══════════════════════════════════════════════════════════════════════════════

def export_all_csvs(raw_db=RAW_DB, out_dir=ID_LIST_DIR, mirror_dir=CANONICAL_STORAGE_DIR):
    """Export all 10 CSV files by parsing thermoml_raw.db JSON cards directly.

    Args:
        raw_db:   Path to thermoml_raw.db.
        out_dir:  Directory to write CSV files into.
    """
    os.makedirs(out_dir, exist_ok=True)
    print(f"Generating CSVs from raw DB: {raw_db}")
    data = _parse_all_cards(raw_db)

    n_prop = _export_property_ids(data, out_dir)
    n_var = _export_variable_ids(data, out_dir)
    n_constr = _export_constraint_ids(data, out_dir)
    n_meas, meas_slug_to_num_id = _export_measurement_ids(data, out_dir)
    n_meas_alias = _export_measurement_aliases(data, out_dir, meas_slug_to_num_id)
    n_comp = _export_compound_ids(data, out_dir)
    n_solv = _export_solvent_components(data, out_dir)
    n_ref = _export_reference_ids(data, out_dir)
    n_bt = _export_block_types(data, out_dir)
    n_ph = _export_phase_ids(data, out_dir)
    n_rt = _export_reaction_type_ids(data, out_dir)

    if mirror_dir:
        os.makedirs(mirror_dir, exist_ok=True)
        for filename in (
            'property_ids.csv', 'variable_ids.csv', 'constraint_ids.csv',
            'measurement_ids.csv', 'measurement_aliases.csv',
            'compound_ids.csv', 'solvent_components.csv',
            'reference_ids.csv', 'block_types.csv', 'phase_ids.csv',
            'reaction_type_ids.csv',
        ):
            shutil.copy2(os.path.join(out_dir, filename), os.path.join(mirror_dir, filename))

    print(f"  property_ids.csv:        {n_prop:>6,d} rows")
    print(f"  variable_ids.csv:        {n_var:>6,d} rows")
    print(f"  constraint_ids.csv:      {n_constr:>6,d} rows")
    print(f"  measurement_ids.csv:     {n_meas:>6,d} rows")
    print(f"  measurement_aliases.csv: {n_meas_alias:>6,d} rows")
    print(f"  compound_ids.csv:        {n_comp:>6,d} rows")
    print(f"  solvent_components.csv:  {n_solv:>6,d} rows")
    print(f"  reference_ids.csv:       {n_ref:>6,d} rows")
    print(f"  block_types.csv:         {n_bt:>6,d} rows")
    print(f"  phase_ids.csv:           {n_ph:>6,d} rows")
    print(f"  reaction_type_ids.csv:   {n_rt:>6,d} rows")


if __name__ == '__main__':
    export_all_csvs()
