"""
CSV-backed index for canonical ID lookups across ThermoML card builders.

Loads all registry CSV files from _index_builder/id_name_lists/ and provides
lookup methods for compounds, properties, measurements, variables, constraints,
references, phases, and reaction types.

Usage:
    from ThermoML_raw_json_to_card_db_parsers.index_lookup import ThermoMLIndex
    index = ThermoMLIndex()
    row = index.lookup_compound(inchi_key="XLYOFNOQVPJJNP-UHFFFAOYSA-N")
    # row = {'comp_num_id': 1, 'inchi_key': '...', 'common_name': 'water', ...}
"""

import csv
import os
import re

from ThermoML_raw_json_to_card_db_parsers.id_schema import (
    base_component_id,
    require_global_id,
    resolve_component_id,
)

_CSV_DIR = os.path.join(os.path.dirname(__file__), '_index_builder', 'id_name_lists')


def _slugify(name):
    """Reproduce shared_utils.slugify for synthetic key construction."""
    s = name.lower()
    s = re.sub(r'[,/\s*()]+', '_', s)
    s = re.sub(r'[^a-z0-9_]', '', s)
    s = re.sub(r'_+', '_', s)
    return s.strip('_')


class ThermoMLIndex:
    """Loads all CSV index files once and provides fast lookup methods."""

    def __init__(self, csv_dir=None):
        self._csv_dir = csv_dir or _CSV_DIR
        self._compound_by_inchikey = {}
        self._compound_by_inchi = {}
        self._property_by_name = {}
        self._measurement_by_name = {}
        self._measurement_by_slug = {}
        self._variable_by_name = {}
        self._constraint_by_name = {}
        self._reference_by_doi = {}
        self._phase_by_name = {}
        self._reaction_type_by_name = {}
        self._block_type_by_key = {}
        self._solvent_by_comp_num_id = {}
        self._load_all()

    # ── CSV loading ───────────────────────────────────────────────────────

    def _load_csv(self, filename):
        path = os.path.join(self._csv_dir, filename)
        with open(path, encoding='utf-8', newline='') as f:
            return list(csv.DictReader(f))

    def _load_all(self):
        # Compounds — dual-keyed by inchi_key and standard_inchi
        for row in self._load_csv('compound_ids.csv'):
            row['comp_num_id'] = require_global_id('comp_num_id', row['comp_num_id'])
            row['n_papers'] = int(row['n_papers'])
            ik = row.get('inchi_key', '')
            if ik:
                self._compound_by_inchikey[ik] = row
            inchi = row.get('standard_inchi', '')
            if inchi:
                self._compound_by_inchi[inchi] = row

        # Properties — occurrence semantics include whether the type is linked
        # to a DOI-local component.  Name alone is not a unique registry key.
        for row in self._load_csv('property_ids.csv'):
            row['prop_num_id'] = require_global_id('prop_num_id', row['prop_num_id'])
            row['comp_id_linked'] = int(row['comp_id_linked'])
            row['n_blocks'] = int(row['n_blocks'])
            self._property_by_name[(row['prop_name'], bool(row['comp_id_linked']))] = row

        # Measurements — canonical global types plus an exact raw-name alias table.
        for row in self._load_csv('measurement_ids.csv'):
            row['meas_num_id'] = require_global_id('meas_num_id', row['meas_num_id'])
            row['n_blocks'] = int(row['n_blocks'])
            self._measurement_by_slug[row['meas_id']] = row

        for alias in self._load_csv('measurement_aliases.csv'):
            meas_num_id = require_global_id('meas_num_id', alias['meas_num_id'])
            canonical = self._measurement_by_slug.get(alias['meas_id'])
            if canonical is None or canonical['meas_num_id'] != meas_num_id:
                raise ValueError(
                    "Measurement alias registry is not referentially closed: "
                    f"{alias!r}"
                )
            resolved = dict(canonical)
            resolved['source_method_name'] = alias['source_method_name']
            resolved['source_method_type'] = alias['source_method_type']
            self._measurement_by_name[alias['source_method_name']] = resolved

        # Variables — keyed by var_name
        for row in self._load_csv('variable_ids.csv'):
            row['var_num_id'] = require_global_id('var_num_id', row['var_num_id'])
            row['comp_id_linked'] = int(row['comp_id_linked'])
            row['n_blocks'] = int(row['n_blocks'])
            self._variable_by_name[(row['var_name'], bool(row['comp_id_linked']))] = row

        # Constraints — keyed by constr_name
        for row in self._load_csv('constraint_ids.csv'):
            row['constr_num_id'] = require_global_id('constr_num_id', row['constr_num_id'])
            row['comp_id_linked'] = int(row['comp_id_linked'])
            row['n_blocks'] = int(row['n_blocks'])
            self._constraint_by_name[(row['constr_name'], bool(row['comp_id_linked']))] = row

        # References — keyed by doi
        for row in self._load_csv('reference_ids.csv'):
            row['lit_num_id'] = require_global_id('lit_num_id', row['lit_num_id'])
            row['year'] = int(row['year'])
            row['n_compounds'] = int(row['n_compounds'])
            row['n_blocks'] = int(row['n_blocks'])
            row['total_datapoints'] = int(row['total_datapoints'])
            self._reference_by_doi[row['doi']] = row

        # Phases — keyed by phase_name
        for row in self._load_csv('phase_ids.csv'):
            row['phase_num_id'] = require_global_id('phase_num_id', row['phase_num_id'])
            row['n_occurrences'] = int(row['n_occurrences'])
            self._phase_by_name[row['phase_name']] = row

        # Reaction types — keyed by rxn_type_name
        for row in self._load_csv('reaction_type_ids.csv'):
            row['rxn_type_num_id'] = require_global_id('rxn_type_num_id', row['rxn_type_num_id'])
            row['n_blocks'] = int(row['n_blocks'])
            self._reaction_type_by_name[row['rxn_type_name']] = row

        for row in self._load_csv('block_types.csv'):
            row['blocktype_num_id'] = require_global_id(
                'blocktype_num_id', row['blocktype_num_id']
            )
            row['n_blocks'] = int(row['n_blocks'])
            self._block_type_by_key[(row['block_type'], row['system_type'])] = row

        for row in self._load_csv('solvent_components.csv'):
            row['solvent_num_id'] = require_global_id(
                'solvent_num_id', row['solvent_num_id']
            )
            row['comp_num_id'] = require_global_id('comp_num_id', row['comp_num_id'])
            row['n_blocks_as_solvent'] = int(row['n_blocks_as_solvent'])
            self._solvent_by_comp_num_id[row['comp_num_id']] = row

    # ── Lookup methods ────────────────────────────────────────────────────

    def lookup_compound(self, inchi_key=None, standard_inchi=None,
                         common_name=None, formula=None):
        """Look up compound by InChIKey, Standard InChI, or synthetic key fallback.

        Falls back to NO_INCHIKEY:name_formula:{name}:{formula} when both
        InChIKey and InChI are missing (matches canonical_compound_key logic).
        """
        if inchi_key:
            result = self._compound_by_inchikey.get(inchi_key)
            if result:
                return result
        if standard_inchi:
            result = self._compound_by_inchi.get(standard_inchi)
            if result:
                return result
        # Synthetic key fallback for compounds without InChI (e.g. graphite)
        name_slug = _slugify(common_name or "")
        formula_slug = _slugify(formula or "")
        if name_slug or formula_slug:
            synthetic = f"NO_INCHIKEY:name_formula:{name_slug}:{formula_slug}"
            return self._compound_by_inchikey.get(synthetic)
        return None

    def lookup_property(self, prop_name, component_linked):
        """Look up an exact property occurrence type."""
        return self._property_by_name.get((prop_name, bool(component_linked)))

    def lookup_measurement(self, method_name):
        """Look up a measurement technique by its exact source name."""
        return self._measurement_by_name.get(method_name)

    def lookup_variable(self, var_name, component_linked):
        """Look up an exact variable occurrence type."""
        return self._variable_by_name.get((var_name, bool(component_linked)))

    def lookup_constraint(self, constr_name, component_linked):
        """Look up an exact constraint occurrence type."""
        return self._constraint_by_name.get((constr_name, bool(component_linked)))

    def lookup_reference(self, doi):
        """Look up reference by DOI. Returns row dict or None."""
        return self._reference_by_doi.get(doi)

    def lookup_phase(self, phase_name):
        """Look up phase by name (ePhase). Returns row dict or None."""
        return self._phase_by_name.get(phase_name)

    def lookup_reaction_type(self, rxn_type_name):
        """Look up reaction type by name. Returns row dict or None."""
        return self._reaction_type_by_name.get(rxn_type_name)

    def lookup_block_type(self, block_type, system_type):
        """Look up one canonical block-type/system-type pair."""
        return self._block_type_by_key.get((block_type, system_type))

    def lookup_solvent(self, comp_num_id):
        """Look up a solvent registry row by canonical compound ID."""
        require_global_id('comp_num_id', comp_num_id)
        return self._solvent_by_comp_num_id.get(comp_num_id)

    # ── ID resolution helpers ─────────────────────────────────────────────

    @staticmethod
    def resolve_id(id_template, comp_org_num):
        """Resolve the ``{DOIcomp_id}`` placeholder in a registry ID.

        Example: resolve_id("mole_fraction_{DOIcomp_id}", 3)
        → "mole_fraction_DOIcomp_3"
        """
        return resolve_component_id(id_template, comp_org_num)

    @staticmethod
    def base_id(id_with_template):
        """Strip ``{DOIcomp_id}`` to get the base ID for Tier 1 lookup.

        Example: base_id("mole_fraction_{DOIcomp_id}") → "mole_fraction"
        """
        return base_component_id(id_with_template)
