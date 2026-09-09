"""
MTDKS (MeasTech DK Schema) INDIV card builder -- per-DOI method usage card.

Records which measurement techniques were used in a paper, indexed with
canonical measurement and property IDs from the CSV registry.
"""

from ThermoML_raw_json_to_card_db_parsers.shared_utils import extract_trc_ref_id, extract_property_info
from ThermoML_raw_json_to_card_db_parsers.index_lookup import ThermoMLIndex
from ThermoML_raw_json_to_card_db_parsers.id_schema import block_id


def build_mtdks_card(data, index):
    """Build MeasTech DK Schema INDIV (method usage) card.

    Args:
        data: Parsed ThermoML JSON dict for one paper.
        index: ThermoMLIndex instance for canonical ID lookups.
    """
    cit = data.get("Citation", {})
    doi = cit.get("sDOI", "")
    lit_id, _ = extract_trc_ref_id(cit.get("TRCRefID"))

    ref_row = index.lookup_reference(doi)
    if ref_row is None:
        raise ValueError(f"Reference registry has no canonical ID for DOI {doi!r}")
    lit_num_id = ref_row["lit_num_id"]

    pure_blocks = data.get("PureOrMixtureData", [])
    rxn_blocks = data.get("ReactionData", [])
    all_blocks = ([(b, "PureOrMixtureData") for b in pure_blocks]
                  + [(b, "ReactionData") for b in rxn_blocks])

    # (mtype, mname, pgroup) -> accumulator
    method_map = {}
    for blk, btype in all_blocks:
        if btype == "PureOrMixtureData":
            bnum = blk.get("nPureOrMixtureDataNumber")
        else:
            bnum = blk.get("nReactionDataNumber")
        typed_block_id = block_id(btype, bnum)

        for prop in blk.get("Property", []):
            pname, gname, method_std, method_cust, comp_org_num = extract_property_info(prop)
            if method_std:
                mtype, mname = "standard", method_std
            elif method_cust:
                mtype, mname = "custom", method_cust
            else:
                continue

            key = (mtype, mname, gname)
            if key not in method_map:
                meas_row = index.lookup_measurement(mname)
                if meas_row is None:
                    raise ValueError(
                        f"Measurement registry lookup failed for {mname!r} in DOI {doi!r}"
                    )
                method_map[key] = {
                    # Preserve the DOI-local component binding.  A property
                    # type such as mole_fraction_{DOIcomp_id} can occur for
                    # several compounds under the same method; collapsing to
                    # (name, component_linked) loses those distinct identities.
                    "prop_occurrences": set(),
                    "block_numbers": set(),
                    "count": 0,
                    "meas_row": meas_row,
                }
            method_map[key]["prop_occurrences"].add((pname, comp_org_num))
            method_map[key]["block_numbers"].add(typed_block_id)
            method_map[key]["count"] += 1

    methods_out = []
    n_std = 0
    n_cust = 0
    for (mtype, mname, pgroup), info in sorted(method_map.items()):
        meas_row = info["meas_row"]

        # Resolve property IDs
        prop_entries = []
        prop_occurrences = sorted(
            info["prop_occurrences"],
            key=lambda item: (
                item[0],
                -1 if item[1] is None else int(item[1]),
            ),
        )
        for pn, comp_org_num in prop_occurrences:
            component_linked = comp_org_num is not None
            prop_row = index.lookup_property(pn, component_linked)
            entry = {"name": pn, "component_linked": component_linked}
            if prop_row is None:
                raise ValueError(f"Property registry lookup failed for {pn!r} in DOI {doi!r}")
            entry["prop_num_id"] = prop_row["prop_num_id"]
            entry["prop_id"] = ThermoMLIndex.resolve_id(
                prop_row["prop_id"], comp_org_num
            )
            prop_entries.append(entry)

        methods_out.append({
            "method_type": mtype,
            "method_name": mname,
            "meas_num_id": meas_row["meas_num_id"],
            "meas_id": meas_row["meas_id"],
            "property_group": pgroup,
            "properties": prop_entries,
            "block_numbers": sorted(info["block_numbers"]),
            "instance_count": info["count"],
        })
        if mtype == "standard":
            n_std += 1
        else:
            n_cust += 1

    return {
        "key": {"doi": doi, "lit_id": lit_id, "lit_num_id": lit_num_id},
        "methods_summary": {
            "n_unique_methods": len(method_map),
            "n_standard": n_std,
            "n_custom": n_cust,
        },
        "methods": methods_out,
    }
