"""
Search & smart-query Flask Blueprint.

The ``/search`` route with its SQL query builder, similarity search
integration, and smart-query resolution-chip helpers.
"""

import traceback

from flask import Blueprint, abort, current_app, render_template, request

from card_db_search_tools.basic_search_tools.normalization_helpers.strict_id_inputs import (
    IdentifierRefinementError,
    validate_search_values,
)

search_bp = Blueprint('search', __name__)


# ---------------------------------------------------------------------------
# Lazy-loaded similarity search
# ---------------------------------------------------------------------------

_sim_search = None


def _get_sim_search():
    global _sim_search
    if _sim_search is None:
        import importlib
        mod = importlib.import_module(
            "card_db_search_tools.basic_search_tools.10_compound_similarity_search"
        )
        _sim_search = mod.search_similar_compounds
    return _sim_search


# ---------------------------------------------------------------------------
# Helper: collect query params from request
# ---------------------------------------------------------------------------

def _search_params():
    """Collect all search params into a dict for template rendering."""
    return {
        'smart_q': request.args.get('smart_q', '').strip(),
        'agentic': request.args.get('agentic', '').strip(),
        'agentic_limit': request.args.get('agentic_limit', '20').strip(),
        'doi': request.args.get('doi', '').strip(),
        'authors': request.args.get('authors', '').strip(),
        'title': request.args.get('title', '').strip(),
        'journal': request.args.get('journal', '').strip(),
        'year_min': request.args.get('year_min', '').strip(),
        'year_max': request.args.get('year_max', '').strip(),
        'compounds': request.args.get('compounds', '').strip(),
        'formula': request.args.get('formula', '').strip(),
        'system_type': request.args.get('system_type', '').strip(),
        'n_components': request.args.get('n_components', '').strip(),
        'sim_query': request.args.get('sim_query', '').strip(),
        'sim_threshold': request.args.get('sim_threshold', '').strip(),
        'sim_topk': request.args.get('sim_topk', '').strip(),
        'property': request.args.get('property', '').strip(),
        'property_kw': request.args.get('property_kw', '').strip(),
        'phase': request.args.get('phase', '').strip(),
        'block_type': request.args.get('block_type', '').strip(),
        'var_kw': request.args.get('var_kw', '').strip(),
        'variable': request.args.get('variable', '').strip(),
        'meas_kw': request.args.get('meas_kw', '').strip(),
        'measurement': request.args.get('measurement', '').strip(),
        'constr_kw': request.args.get('constr_kw', '').strip(),
        'constraint': request.args.get('constraint', '').strip(),
        'min_datapoints': request.args.get('min_datapoints', '').strip(),
        'max_wait_seconds': request.args.get('max_wait_seconds', '').strip(),
        'allow_query_agent': request.args.get('allow_query_agent', '').strip(),
        'agentic_all_fields': request.args.get('agentic_all_fields', '').strip(),
    }


# ---------------------------------------------------------------------------
# SQL query builder
# ---------------------------------------------------------------------------

def _build_search_query(q):
    """Build SQL WHERE clause from search params.

    Returns (select_sql, count_sql, params).
    """
    joins = []
    wheres = []
    params = []

    # -- Bibliography --
    if q['doi']:
        wheres.append("r.doi LIKE ?")
        params.append(f"%{q['doi']}%")
    if q['authors']:
        wheres.append("r.first_author LIKE ?")
        params.append(f"%{q['authors']}%")
    if q['title']:
        for word in q['title'].split():
            wheres.append("r.title LIKE ?")
            params.append(f"%{word}%")
    if q['journal']:
        wheres.append("r.journal = ?")
        params.append(q['journal'])
    if q['year_min']:
        wheres.append("r.year >= ?")
        params.append(int(q['year_min']))
    if q['year_max']:
        wheres.append("r.year <= ?")
        params.append(int(q['year_max']))

    # -- Chemistry --
    if q['compounds']:
        compounds = validate_search_values(
            "compound", q['compounds'], field="compounds"
        )
        for i, compound in enumerate(compounds):
            alias = f"bc_{i}"
            joins.append(
                f"JOIN block_compounds {alias} ON {alias}.doi = bi.doi "
                f"AND {alias}.block_number = bi.block_number AND {alias}.block_type = bi.block_type"
            )
            if compound.startswith("GLOBcomp_"):
                wheres.append(f"{alias}.comp_num_id = ?")
                params.append(compound)
            else:
                wheres.append(f"{alias}.comp_name LIKE ?")
                params.append(f"%{compound.lower()}%")

    if q['formula']:
        joins.append(
            "JOIN block_compounds bcf ON bcf.doi = bi.doi "
            "AND bcf.block_number = bi.block_number AND bcf.block_type = bi.block_type"
        )
        wheres.append("bcf.comp_formula LIKE ?")
        params.append(f"%{q['formula']}%")

    # -- Properties / Phase --
    if q['property']:
        joins.append(
            "JOIN block_properties bprop ON bprop.doi = bi.doi "
            "AND bprop.block_number = bi.block_number AND bprop.block_type = bi.block_type"
        )
        property_atoms = validate_search_values(
            "property", q['property'], field="property"
        )
        if len(property_atoms) != 1:
            raise ValueError("property accepts exactly one property search value")
        if property_atoms[0].startswith("GLOBprop_"):
            wheres.append("bprop.prop_num_id = ?")
            params.append(property_atoms[0])
        else:
            wheres.append("bprop.prop_name LIKE ?")
            params.append(f'%{property_atoms[0]}%')
    if q['property_kw']:
        for kw in validate_search_values(
            "property", q['property_kw'], field="property_kw"
        ):
            if "block_properties" not in " ".join(joins):
                joins.append(
                    "JOIN block_properties bpkw ON bpkw.doi = bi.doi "
                    "AND bpkw.block_number = bi.block_number AND bpkw.block_type = bi.block_type"
                )
            if kw.startswith("GLOBprop_"):
                wheres.append("bpkw.prop_num_id = ?")
                params.append(kw)
            else:
                wheres.append("bpkw.prop_name LIKE ?")
                params.append(f'%{kw}%')
    if q['phase']:
        phase_atoms = validate_search_values("phase", q['phase'], field="phase")
        if len(phase_atoms) != 1:
            raise ValueError("phase accepts exactly one phase search value")
        if phase_atoms[0].startswith("GLOBphase_"):
            phase_clause = "bp2.phase_num_id = ?"
            params.append(phase_atoms[0])
        else:
            phase_clause = "bp2.phase_id LIKE ?"
            params.append(f'%{phase_atoms[0]}%')
        wheres.append(
            "EXISTS (SELECT 1 FROM block_properties bp2 WHERE bp2.doi = bi.doi "
            "AND bp2.block_number = bi.block_number AND " + phase_clause + ")"
        )
    if q['block_type']:
        wheres.append("bi.block_type = ?")
        params.append(q['block_type'])

    # -- Variables --
    if q['variable']:
        joins.append(
            "JOIN block_variables bvar ON bvar.doi = bi.doi "
            "AND bvar.block_number = bi.block_number AND bvar.block_type = bi.block_type"
        )
        variable_atoms = validate_search_values(
            "variable", q['variable'], field="variable"
        )
        if len(variable_atoms) != 1:
            raise ValueError("variable accepts exactly one variable search value")
        if variable_atoms[0].startswith("GLOBvar_"):
            wheres.append("bvar.var_num_id = ?")
            params.append(variable_atoms[0])
        else:
            wheres.append("bvar.var_name LIKE ?")
            params.append(f'%{variable_atoms[0]}%')
    if q['var_kw']:
        for kw in validate_search_values("variable", q['var_kw'], field="var_kw"):
            if "block_variables" not in " ".join(joins):
                joins.append(
                    "JOIN block_variables bvkw ON bvkw.doi = bi.doi "
                    "AND bvkw.block_number = bi.block_number AND bvkw.block_type = bi.block_type"
                )
            if kw.startswith("GLOBvar_"):
                wheres.append("bvkw.var_num_id = ?")
                params.append(kw)
            else:
                wheres.append("bvkw.var_name LIKE ?")
                params.append(f'%{kw}%')

    # -- Measurements --
    if q['measurement']:
        joins.append(
            "JOIN block_measurements bmeas ON bmeas.doi = bi.doi "
            "AND bmeas.block_number = bi.block_number AND bmeas.block_type = bi.block_type"
        )
        measurement_atoms = validate_search_values(
            "measurement", q['measurement'], field="measurement"
        )
        if len(measurement_atoms) != 1:
            raise ValueError("measurement accepts exactly one measurement search value")
        if measurement_atoms[0].startswith("GLOBmeas_"):
            wheres.append("bmeas.meas_num_id = ?")
            params.append(measurement_atoms[0])
        else:
            wheres.append("bmeas.method_name LIKE ?")
            params.append(f'%{measurement_atoms[0]}%')
    if q['meas_kw']:
        for kw in validate_search_values(
            "measurement", q['meas_kw'], field="meas_kw"
        ):
            if "block_measurements" not in " ".join(joins):
                joins.append(
                    "JOIN block_measurements bmkw ON bmkw.doi = bi.doi "
                    "AND bmkw.block_number = bi.block_number AND bmkw.block_type = bi.block_type"
                )
            if kw.startswith("GLOBmeas_"):
                wheres.append("bmkw.meas_num_id = ?")
                params.append(kw)
            else:
                wheres.append("bmkw.method_name LIKE ?")
                params.append(f'%{kw}%')

    # -- Constraints --
    if q['constraint']:
        joins.append(
            "JOIN block_constraints bcon ON bcon.doi = bi.doi "
            "AND bcon.block_number = bi.block_number AND bcon.block_type = bi.block_type"
        )
        constraint_atoms = validate_search_values(
            "constraint", q['constraint'], field="constraint"
        )
        if len(constraint_atoms) != 1:
            raise ValueError("constraint accepts exactly one constraint search value")
        if constraint_atoms[0].startswith("GLOBconstr_"):
            wheres.append("bcon.constr_num_id = ?")
            params.append(constraint_atoms[0])
        else:
            wheres.append("bcon.constr_name LIKE ?")
            params.append(f'%{constraint_atoms[0]}%')
    if q['constr_kw']:
        for kw in validate_search_values(
            "constraint", q['constr_kw'], field="constr_kw"
        ):
            if "block_constraints" not in " ".join(joins):
                joins.append(
                    "JOIN block_constraints bckw ON bckw.doi = bi.doi "
                    "AND bckw.block_number = bi.block_number AND bckw.block_type = bi.block_type"
                )
            if kw.startswith("GLOBconstr_"):
                wheres.append("bckw.constr_num_id = ?")
                params.append(kw)
            else:
                wheres.append("bckw.constr_name LIKE ?")
                params.append(f'%{kw}%')

    # System type / n_components
    if q['system_type']:
        wheres.append("bi.system_type = ?")
        params.append(q['system_type'])
    if q['n_components']:
        wheres.append("bi.n_components = ?")
        params.append(int(q['n_components']))

    if q['min_datapoints']:
        wheres.append("bi.n_datapoints >= ?")
        params.append(int(q['min_datapoints']))

    # Assemble
    base_cols = (
        "bi.doi, bi.block_number, bi.block_type, bi.compound_system, "
        "bi.n_datapoints, bi.system_type, bi.n_components, r.doi as rdoi"
    )
    base = f"SELECT {base_cols} FROM block_index bi JOIN ref_index r ON r.doi = bi.doi"
    for j in joins:
        base += f" {j}"
    if wheres:
        base += " WHERE " + " AND ".join(wheres)

    count_sql = (
        "SELECT COUNT(*), COUNT(DISTINCT bi.doi), COALESCE(SUM(bi.n_datapoints),0) "
        "FROM block_index bi JOIN ref_index r ON r.doi = bi.doi"
    )
    for j in joins:
        count_sql += f" {j}"
    if wheres:
        count_sql += " WHERE " + " AND ".join(wheres)

    return base, count_sql, params


# ---------------------------------------------------------------------------
# Registry list helpers (used by search template dropdowns)
# ---------------------------------------------------------------------------

def _get_property_list(db):
    return db.execute(
        "SELECT prop_name, n_blocks FROM prop_registry ORDER BY n_blocks DESC"
    ).fetchall()


def _get_phase_list(db):
    return [r['phase_name'] for r in db.execute(
        "SELECT phase_name, n_occurrences FROM phase_registry ORDER BY n_occurrences DESC"
    ).fetchall()]


def _get_variable_list(db):
    return db.execute(
        "SELECT var_name, n_blocks FROM var_registry ORDER BY n_blocks DESC"
    ).fetchall()


def _get_measurement_list(db):
    return db.execute(
        "SELECT method_name, n_blocks FROM meas_registry ORDER BY n_blocks DESC"
    ).fetchall()


def _get_constraint_list(db):
    return db.execute(
        "SELECT constr_name, n_blocks FROM constr_registry ORDER BY n_blocks DESC"
    ).fetchall()


# ---------------------------------------------------------------------------
# Resolution chips (smart search feedback)
# ---------------------------------------------------------------------------

def _build_resolution_chips(rq):
    """Convert a ResolvedQuery into chip dicts for the template."""
    chips = []
    for r in rq.compounds:
        chips.append({'type': 'compound', 'type_label': 'Compound',
                      'text': r.display_name, 'global_id': r.global_id, 'score': r.score})
    for r in rq.properties:
        chips.append({'type': 'property', 'type_label': 'Property',
                      'text': r.display_name, 'global_id': r.global_id, 'score': r.score})
    for r in rq.measurements:
        chips.append({'type': 'measurement', 'type_label': 'Method',
                      'text': r.display_name, 'global_id': r.global_id, 'score': r.score})
    for r in rq.variables:
        chips.append({'type': 'variable', 'type_label': 'Variable',
                      'text': r.display_name, 'global_id': r.global_id, 'score': r.score})
    for r in rq.constraints:
        chips.append({'type': 'constraint', 'type_label': 'Constraint',
                      'text': r.display_name, 'global_id': r.global_id, 'score': r.score})
    for d in rq.dois:
        chips.append({'type': 'bibliography', 'type_label': 'DOI',
                      'text': d, 'global_id': None, 'score': None})
    for w in rq.title_words:
        chips.append({'type': 'bibliography', 'type_label': 'Title',
                      'text': w, 'global_id': None, 'score': None})
    for a in rq.authors:
        chips.append({'type': 'bibliography', 'type_label': 'Author',
                      'text': a, 'global_id': None, 'score': None})
    if rq.year_min:
        txt = str(rq.year_min)
        if rq.year_max:
            txt += f'\u2013{rq.year_max}'
        chips.append({'type': 'filter', 'type_label': 'Year',
                      'text': txt, 'global_id': None, 'score': None})
    if rq.system_type:
        chips.append({'type': 'filter', 'type_label': 'System',
                      'text': rq.system_type, 'global_id': None, 'score': None})
    if rq.block_type:
        chips.append({'type': 'filter', 'type_label': 'Block',
                      'text': rq.block_type, 'global_id': None, 'score': None})
    if rq.n_components:
        chips.append({'type': 'filter', 'type_label': '#Comp',
                      'text': str(rq.n_components), 'global_id': None, 'score': None})
    for f in rq.formulas:
        chips.append({'type': 'compound', 'type_label': 'Formula',
                      'text': f, 'global_id': None, 'score': None})
    return {
        'chips': chips,
        'unresolved': rq.unresolved,
        'log': rq.resolution_log,
    }


def _build_argo_resolution_chips(fld, argo_result):
    """Convert Argo agent resolved fields into chip dicts."""
    chips = []
    _ENTITY_MAP = {
        'compounds': ('compound', 'Compound'),
        'properties': ('property', 'Property'),
        'measurements': ('measurement', 'Method'),
        'variables': ('variable', 'Variable'),
        'constraints': ('constraint', 'Constraint'),
        'phases': ('phase', 'Phase'),
    }
    for key, (typ, label) in _ENTITY_MAP.items():
        for e in fld.get(key, []):
            chips.append({
                'type': typ, 'type_label': label,
                'text': e.get('name', ''), 'global_id': e.get('global_id'),
                'score': e.get('score'),
            })
    if fld.get('doi'):
        chips.append({'type': 'bibliography', 'type_label': 'DOI',
                      'text': fld['doi'], 'global_id': None, 'score': None})
    if fld.get('title_keywords'):
        chips.append({'type': 'bibliography', 'type_label': 'Title',
                      'text': fld['title_keywords'], 'global_id': None, 'score': None})
    if fld.get('authors'):
        chips.append({'type': 'bibliography', 'type_label': 'Author',
                      'text': fld['authors'], 'global_id': None, 'score': None})
    if fld.get('year_min'):
        txt = str(fld['year_min'])
        if fld.get('year_max'):
            txt += f'\u2013{fld["year_max"]}'
        chips.append({'type': 'filter', 'type_label': 'Year',
                      'text': txt, 'global_id': None, 'score': None})
    if fld.get('system_type'):
        chips.append({'type': 'filter', 'type_label': 'System',
                      'text': fld['system_type'], 'global_id': None, 'score': None})
    if fld.get('block_type'):
        chips.append({'type': 'filter', 'type_label': 'Block',
                      'text': fld['block_type'], 'global_id': None, 'score': None})
    if fld.get('formula'):
        chips.append({'type': 'compound', 'type_label': 'Formula',
                      'text': fld['formula'], 'global_id': None, 'score': None})
    return {
        'chips': chips,
        'unresolved': fld.get('unresolved', []),
        'log': fld.get('resolution_log', []),
        'argo_iterations': argo_result.iterations,
        'argo_elapsed': round(argo_result.elapsed_seconds, 1),
    }


def _build_hardcoded_resolution_chips(fld, result):
    """Convert hardcoded pipeline fields into chip dicts."""
    chips_data = _build_argo_resolution_chips(fld, result)
    chips_data.pop('argo_iterations', None)
    chips_data.pop('argo_elapsed', None)
    chips_data['deterministic'] = True
    chips_data['elapsed'] = round(result.elapsed_seconds, 3)
    chips_data['log'] = result.resolution_log or []
    return chips_data


# ---------------------------------------------------------------------------
# Route: Advanced Search
# ---------------------------------------------------------------------------

def _resolve_dynamic_name(name: str, component_name: str | None) -> str:
    """Append compound name to a dynamic entity name."""
    if component_name:
        return f"{name} ({component_name})"
    return name


@search_bp.route('/search')
def search_page():
    # Resolve through the active mounted app. Importing a module named ``app``
    # can refer to an unrelated module; use this application's registered accessor.
    db = current_app.extensions['thermoml_get_db']()
    q = _search_params()
    action = request.args.get('action', '')
    page = request.args.get('page', 1, type=int)

    # Dropdown data
    journals = [r[0] for r in db.execute(
        "SELECT DISTINCT journal FROM ref_index ORDER BY journal"
    ).fetchall()]
    top_properties = _get_property_list(db)
    phases = _get_phase_list(db)
    top_variables = _get_variable_list(db)
    top_measurements = _get_measurement_list(db)
    top_constraints = _get_constraint_list(db)

    # Stats for empty state
    stats = {
        'papers': db.execute("SELECT COUNT(*) FROM ref_index").fetchone()[0],
        'compounds': db.execute(
            "SELECT COUNT(*) FROM compound_registry"
        ).fetchone()[0],
        'blocks': db.execute("SELECT COUNT(*) FROM block_index").fetchone()[0],
    }

    # Structural similarity (independent of SQL search)
    sim_results = []
    if q['sim_query']:
        fn = _get_sim_search()
        if fn:
            try:
                threshold = float(q['sim_threshold'] or 0.5)
                topk = int(q['sim_topk'] or 20)
                queries = [s.strip() for s in q['sim_query'].split(';') if s.strip()]

                if len(queries) == 1:
                    res = fn(name=queries[0], top_k=topk, min_similarity=threshold)
                    if 'error' in res:
                        raise ValueError(res['error'])
                    for r in res['results']:
                        sim_results.append({
                            'name': r['common_name'],
                            'formula': r['formula'],
                            'smiles': r['smiles'],
                            'similarity': r['similarity'],
                            'n_papers': r['n_papers'],
                            'inchikey': r['inchi_key'],
                            'matched_query': queries[0],
                        })
                else:
                    combined = {}
                    for qname in queries:
                        per_q_k = max(topk * 2, 50)
                        res = fn(name=qname, top_k=per_q_k, min_similarity=0.0)
                        if 'error' in res:
                            raise ValueError(res['error'])
                        for r in res['results']:
                            cname = r['common_name']
                            ckey = (cname, r['formula'], r['smiles'])
                            if ckey not in combined:
                                combined[ckey] = {
                                    'scores': {},
                                    'info': {
                                        'name': cname,
                                        'formula': r['formula'],
                                        'smiles': r['smiles'],
                                        'n_papers': r['n_papers'],
                                        'inchikey': r['inchi_key'],
                                    },
                                }
                            prev = combined[ckey]['scores'].get(qname, 0)
                            combined[ckey]['scores'][qname] = max(prev, r['similarity'])

                    n_queries = len(queries)
                    scored = []
                    for ckey, entry in combined.items():
                        total = sum(entry['scores'].get(qn, 0) for qn in queries)
                        avg = total / n_queries
                        if avg < threshold:
                            continue
                        best_q = max(entry['scores'], key=entry['scores'].get)
                        scored.append({
                            **entry['info'],
                            'similarity': round(avg, 4),
                            'matched_query': best_q,
                            'per_query': {qn: round(entry['scores'].get(qn, 0), 4)
                                          for qn in queries},
                        })
                    scored.sort(key=lambda x: -x['similarity'])
                    sim_results = scored[:topk]
            except Exception:
                traceback.print_exc()
                raise

    # -- Smart search: parse free-text smart_q and merge into q --
    resolution_info = None
    if q['smart_q'] and action:
        use_argo = q.get('agentic', '') in ('1', 'on', 'true')
        try:
            from ..cannonical_id_alignment_search_agent.alignment_agent_api import (
                alignment_agent_run,
            )
            agentic_limit_text = q.get('agentic_limit', '20')
            if agentic_limit_text == "all":
                agentic_limit = 500
            elif agentic_limit_text.isdigit() and int(agentic_limit_text) > 0:
                agentic_limit = int(agentic_limit_text)
            else:
                raise ValueError("agentic_limit must be a positive integer or 'all'")
            max_wait = q.get('max_wait_seconds', '')
            allow_qagent = q.get('allow_query_agent', '') in ('1', 'on', 'true')
            agentic_all = q.get('agentic_all_fields', '') in ('1', 'on', 'true')
            align_settings: dict = {
                'use_agent': use_argo,
                'entry_limit': agentic_limit,
                'allow_query_agent': allow_qagent,
                'agentic_all_fields': agentic_all,
            }
            if max_wait and str(max_wait).isdigit():
                align_settings['max_wait_seconds'] = int(max_wait)

            result = alignment_agent_run(q['smart_q'], settings=align_settings)
            fld = result.fields

            if use_argo:
                resolution_info = _build_argo_resolution_chips(fld, result)
            else:
                resolution_info = _build_hardcoded_resolution_chips(fld, result)

            # Merge resolved fields into q (only fill empty fields)
            if fld.get('compounds') and not q['compounds']:
                q['compounds'] = '; '.join(c['global_id'] for c in fld['compounds'])
            if fld.get('properties') and not q['property_kw']:
                q['property_kw'] = '; '.join(p['global_id'] for p in fld['properties'])
            if fld.get('phases') and not q['phase']:
                q['phase'] = fld['phases'][0]['global_id']
            if fld.get('title_keywords') and not q['title']:
                q['title'] = fld['title_keywords']
            if fld.get('doi') and not q['doi']:
                q['doi'] = fld['doi']
            if fld.get('authors') and not q['authors']:
                q['authors'] = fld['authors']
            if fld.get('journal') and not q['journal']:
                q['journal'] = fld['journal']
            if fld.get('year_min') and not q['year_min']:
                q['year_min'] = str(fld['year_min'])
            if fld.get('year_max') and not q['year_max']:
                q['year_max'] = str(fld['year_max'])
            if fld.get('system_type') and not q['system_type']:
                q['system_type'] = fld['system_type']
            if fld.get('block_type') and not q['block_type']:
                q['block_type'] = fld['block_type']
            if fld.get('n_components') and not q['n_components']:
                q['n_components'] = str(fld['n_components'])
            if fld.get('min_datapoints') and not q['min_datapoints']:
                q['min_datapoints'] = str(fld['min_datapoints'])
            if fld.get('formula') and not q['formula']:
                q['formula'] = fld['formula']
            if fld.get('variables') and not q['var_kw']:
                q['var_kw'] = '; '.join(v['global_id'] for v in fld['variables'])
            if fld.get('measurements') and not q['meas_kw']:
                q['meas_kw'] = '; '.join(m['global_id'] for m in fld['measurements'])
            if fld.get('constraints') and not q['constr_kw']:
                q['constr_kw'] = '; '.join(c['global_id'] for c in fld['constraints'])
        except Exception:
            traceback.print_exc()

    # Check if any non-similarity filter is active
    has_filter = any(q[k] for k in q if k not in
                     ('sim_query', 'sim_threshold', 'sim_topk', 'smart_q', 'agentic',
                      'agentic_limit', 'max_wait_seconds',
                      'allow_query_agent', 'agentic_all_fields'))

    results = []
    total = n_papers = total_points = 0
    total_pages = 1
    count_only = False
    offset = 0

    if has_filter and action:
        try:
            select_sql, count_sql, params = _build_search_query(q)
        except IdentifierRefinementError as exc:
            abort(400, description=str(exc))

        row = db.execute(count_sql, params).fetchone()
        total, n_papers, total_points = row[0], row[1], row[2]

        if action == 'count':
            count_only = True
        else:
            per_page = 50
            offset = (page - 1) * per_page
            total_pages = max(1, (total + per_page - 1) // per_page)

            select_sql += f" ORDER BY bi.n_datapoints DESC LIMIT {per_page} OFFSET {offset}"
            rows = db.execute(select_sql, params).fetchall()

            for r in rows:
                comp_rows = db.execute(
                    "SELECT comp_name FROM block_compounds "
                    "WHERE doi = ? AND block_number = ? AND block_type = ?",
                    (r['doi'], r['block_number'], r['block_type']),
                ).fetchall()
                comp_names_list = [c['comp_name'] for c in comp_rows if c['comp_name']]

                prop_rows = db.execute(
                    "SELECT bp.prop_name, bp.component_org_num, bc.comp_name "
                    "FROM block_properties bp "
                    "LEFT JOIN block_compounds bc "
                    "ON bc.doi = bp.doi "
                    "AND bc.block_number = bp.block_number "
                    "AND bc.block_type = bp.block_type "
                    "AND bc.org_num = bp.component_org_num "
                    "WHERE bp.doi = ? AND bp.block_number = ? "
                    "AND bp.block_type = ?",
                    (r['doi'], r['block_number'], r['block_type']),
                ).fetchall()
                prop_names = [_resolve_dynamic_name(p['prop_name'], p['comp_name'])
                              for p in prop_rows]

                results.append({
                    'doi': r['doi'],
                    'block_number': r['block_number'],
                    'block_type': r['block_type'],
                    'compound_names': comp_names_list,
                    'property_names': prop_names,
                    'system_type': r['system_type'] or '',
                    'n_datapoints': r['n_datapoints'],
                })

    return render_template(
        'search.html',
        q=q,
        journals=journals,
        top_properties=top_properties,
        phases=phases,
        top_variables=top_variables,
        top_measurements=top_measurements,
        top_constraints=top_constraints,
        stats=stats,
        results=results,
        sim_results=sim_results,
        total=total,
        n_papers=n_papers,
        total_points=total_points,
        total_pages=total_pages,
        page=page,
        offset=offset,
        count_only=count_only,
        resolution_info=resolution_info,
    )
