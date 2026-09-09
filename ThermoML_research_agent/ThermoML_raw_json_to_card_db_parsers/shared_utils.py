"""
Shared utility functions for ThermoML card builders.
"""

import logging
import re

from ThermoML_raw_json_to_card_db_parsers.id_schema import doi_comp_id

log = logging.getLogger("thermoml-shared-utils")


def slugify(name):
    """Convert property/method name to slug."""
    s = name.lower()
    s = re.sub(r'[,/\s*()]+', '_', s)
    s = re.sub(r'[^a-z0-9_]', '', s)
    s = re.sub(r'_+', '_', s)
    return s.strip('_')


def meas_id_slugify(name):
    """Slugify for measurement technique IDs (matching MTDKS convention)."""
    s = name.lower()
    s = s.replace('(ostwald; ubbelohde)', 'ostwald_ubbelohde')
    s = s.replace('(recirculating still)', 'recirculating_still')
    s = s.replace('(50 mg)', '50mg')
    s = s.replace('(1 g)', '1g')
    s = s.replace('(less than 1 g)', 'less_than_1g')
    s = s.replace('(monochromatic)', 'monochromatic')
    s = s.replace('(static)', 'static')
    s = s.replace('(no electrode)', 'no_electrode')
    s = s.replace(' / ', '_')
    s = s.replace('/', '_')
    s = re.sub(r'[^a-z0-9]+', '_', s)
    s = s.strip('_')
    s = re.sub(r'_+', '_', s)
    return s


def canonical_compound_key(standard_inchi_key=None, standard_inchi=None,
                           common_name=None, formula=None, cas_rn=None):
    """Return a stable compound key with deterministic fallbacks.

    Real InChIKeys are used as-is. When a source record has no InChIKey,
    a synthetic key is generated from the next-best stable identifiers.
    """
    if standard_inchi_key:
        return standard_inchi_key
    if standard_inchi:
        return f"NO_INCHIKEY:inchi:{standard_inchi}"
    if cas_rn:
        return f"NO_INCHIKEY:cas:{cas_rn}"

    name_slug = slugify(common_name or "")
    formula_slug = slugify(formula or "")
    if name_slug or formula_slug:
        return f"NO_INCHIKEY:name_formula:{name_slug}:{formula_slug}"

    return "NO_INCHIKEY:unknown"


def _first_nonempty_text(value):
    """Return the first nonempty string from a scalar/list source value."""
    if isinstance(value, str):
        return value if value.strip() else None
    if isinstance(value, (list, tuple)):
        for item in value:
            if isinstance(item, str) and item.strip():
                return item
    return None


def resolve_compound_structure_identifiers(compound, registry_row):
    """Resolve canonical structure identifiers for an embedded compound.

    ThermoML source documents frequently omit ``sSmiles`` even when they carry
    a usable standard InChI.  The canonical compound registry already contains
    the normalized SMILES generated during index construction, so card builders
    must use that value instead of preserving a source-level omission.

    The registry is authoritative for canonical SMILES.  Raw ThermoML values
    remain fallbacks so this helper also works with minimal/custom indexes.
    InChI and InChIKey retain the source value when present and otherwise use
    the matching registry row.
    """
    if not isinstance(compound, dict):
        raise TypeError("compound must be an object")
    if not isinstance(registry_row, dict):
        raise TypeError("registry_row must be an object")

    raw_smiles = _first_nonempty_text(compound.get("sSmiles"))
    canonical_smiles = _first_nonempty_text(registry_row.get("smiles"))
    raw_inchi = _first_nonempty_text(compound.get("sStandardInChI"))
    registry_inchi = _first_nonempty_text(registry_row.get("standard_inchi"))
    raw_inchi_key = _first_nonempty_text(compound.get("sStandardInChIKey"))
    registry_inchi_key = _first_nonempty_text(registry_row.get("inchi_key"))

    return {
        "inchi_key": raw_inchi_key or registry_inchi_key,
        "SMILES": canonical_smiles or raw_smiles,
        "InChI": raw_inchi or registry_inchi,
    }


def system_type_label(n_components):
    """Convert component count to system type label."""
    labels = {1: "unary", 2: "binary", 3: "ternary", 4: "quaternary"}
    return labels.get(n_components, f"{n_components}-component")


def extract_trc_ref_id(trc_ref):
    """Parse TRCRefID into structured lit_id."""
    if not trc_ref:
        return None, {}
    year = trc_ref.get("yrYrPub", "")
    a1 = trc_ref.get("sAuthor1", "")
    a2 = trc_ref.get("sAuthor2", "")
    an = trc_ref.get("nAuthorn", "")
    lit_id = f"{year}-{a1}-{a2}-{an}" if year else None
    return lit_id, {
        "year": year,
        "author1": a1,
        "author2": a2,
        "author_n": str(an)
    }


def extract_phase_info(phase_dict):
    """Extract phase info from PhaseID/PropPhaseID/VarPhaseID/ConstraintPhaseID."""
    if not phase_dict:
        return None
    for key in ("ePhase", "ePropPhase", "eVarPhase", "eConstraintPhase"):
        if key in phase_dict:
            result = {"phase": phase_dict[key]}
            comp_ref = phase_dict.get("RegNum", {}).get("nOrgNum")
            if comp_ref is not None:
                result["component_org_num"] = doi_comp_id(comp_ref)
            return result
    return None


def extract_var_or_constraint_type(type_dict):
    """Extract variable/constraint type name and category from VariableType/ConstraintType dict."""
    if not type_dict:
        return "", ""
    for key, val in type_dict.items():
        if key == "tml_elements":
            continue
        if isinstance(val, str):
            return val, key
    return "", ""


def extract_property_info(prop):
    """Extract property name, group, method, and component reference from Property-MethodID structure."""
    pmid = prop.get("Property-MethodID", {})
    pg = pmid.get("PropertyGroup", {})
    comp_org_num = pmid.get("RegNum", {}).get("nOrgNum")

    for gname, gdata in pg.items():
        if gname == "tml_elements" or not isinstance(gdata, dict):
            continue
        pname = gdata.get("ePropName", "")
        em = gdata.get("eMethodName")
        sm = gdata.get("sMethodName")
        method_standard = em if em else None
        method_custom = sm if sm else None
        return pname, gname, method_standard, method_custom, comp_org_num

    return "", "", None, None, comp_org_num


def safe_float(val):
    """Convert to float safely."""
    if val is None:
        return None
    try:
        return float(val)
    except (ValueError, TypeError) as exc:
        log.debug("safe_float failed for %r: %s", val, exc)
        return None


def safe_int(val):
    """Convert to int safely."""
    if val is None:
        return None
    try:
        return int(val)
    except (ValueError, TypeError) as exc:
        log.debug("safe_int failed for %r: %s", val, exc)
        return None
def bind_source_doi(data, source_doi):
    """Bind the authoritative raw-database DOI to one parsed ThermoML document.

    The raw database's ``papers.doi`` column is the canonical record key.  Most
    embedded Citation objects repeat it, but at least one valid record omits
    ``Citation.sDOI``.  A conflicting embedded value is rejected; an absent
    value is populated before card construction.
    """
    if not isinstance(source_doi, str) or not source_doi.strip():
        raise ValueError(f"Invalid source DOI {source_doi!r}")
    source_doi = source_doi.strip()
    citation = data.setdefault("Citation", {})
    embedded = citation.get("sDOI")
    if embedded and embedded != source_doi:
        raise ValueError(
            f"Raw database DOI {source_doi!r} conflicts with Citation.sDOI {embedded!r}"
        )
    citation["sDOI"] = source_doi
    return source_doi
